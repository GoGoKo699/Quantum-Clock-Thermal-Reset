#!/usr/bin/env python3
"""Finite algebra checks for the thermal reset clock.

The full tilted generator, its stationary response, and regenerative block
moments must give the same signed current and count diffusion. General hot
ratios are included, as is the zero-affinity control h=z**2. At this control
the current vanishes, so neither a Fano factor nor timing diffusion is formed.

These are finite-dimensional checks of algebra and counting conventions.
They do not simulate asymptotic scaling or validate a microscopic bath model.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigvals, solve


TOLERANCES = {
    "linear_residual": 2e-11,
    "state_difference": 2e-10,
    "imaginary_part": 2e-10,
    "current_difference": 2e-10,
    "noise_difference": 2e-9,
    "fano_difference": 2e-8,
    "reset_moment_relative": 2e-11,
    "baseline_moment_relative": 2e-10,
    "laplace_difference": 2e-12,
    "tilted_current_difference": 2e-8,
    "tilted_noise_difference": 2e-7,
    "entropy_difference": 2e-10,
    "positivity_slack": 2e-11,
    "activity_slack": 2e-11,
}

CASES = (
    {"name": "irreversible_reference", "d": 2, "seed": 2718,
     "g": 1.0, "h": 0.5, "z": 0.0, "stall": False},
    {"name": "finite_reverse_slow_reset", "d": 3, "seed": 3141,
     "g": 0.7, "h": 0.08, "z": 0.012, "stall": False},
    {"name": "slower_reset_multichannel", "d": 4, "seed": 1618,
     "g": 1.3, "h": 0.025, "z": 0.035, "stall": False},
    {"name": "thermal_stall", "d": 3, "seed": 1414,
     "g": 1.0, "h": 0.4**2, "z": 0.4, "stall": True},
)


class VerificationError(RuntimeError):
    """A numerical check failed its declared tolerance."""


class Checks:
    def __init__(self) -> None:
        self.maximum_errors: dict[str, float] = {}
        self.count = 0

    def error(self, label: str, value: float, tolerance: str) -> float:
        value = float(abs(value))
        if not np.isfinite(value):
            raise VerificationError(f"{label}: nonfinite error {value}")
        limit = TOLERANCES[tolerance]
        self.maximum_errors[tolerance] = max(
            value, self.maximum_errors.get(tolerance, 0.0)
        )
        self.count += 1
        if value > limit:
            raise VerificationError(f"{label}: {value:.6g} exceeds {limit:.6g}")
        return value

    def require(self, condition: bool, description: str) -> None:
        self.count += 1
        if not condition:
            raise VerificationError(description)

    def real(self, label: str, value: complex, scale: float = 1.0) -> float:
        self.error(label + " imaginary part", np.imag(value) / scale,
                   "imaginary_part")
        return float(np.real(value))


def vec(matrix: np.ndarray) -> np.ndarray:
    return np.asarray(matrix, dtype=complex).reshape(-1, order="F")


def unvec(vector: np.ndarray, n: int) -> np.ndarray:
    return vector.reshape((n, n), order="F")


def recycling(jump: np.ndarray) -> np.ndarray:
    return np.kron(jump.conj(), jump)


def dissipator(jump: np.ndarray) -> np.ndarray:
    n = jump.shape[0]
    effect = jump.conj().T @ jump
    return recycling(jump) - 0.5 * (
        np.kron(np.eye(n), effect) + np.kron(effect.T, np.eye(n))
    )


def commutator_generator(hamiltonian: np.ndarray) -> np.ndarray:
    n = hamiltonian.shape[0]
    return -1j * (
        np.kron(np.eye(n), hamiltonian)
        - np.kron(hamiltonian.T, np.eye(n))
    )


def constrained_solve(generator: np.ndarray, rhs: np.ndarray,
                      trace_value: float) -> tuple[np.ndarray, complex]:
    """Solve L x = rhs with tr(x) fixed, retaining every original row."""
    n = int(round(np.sqrt(rhs.size)))
    trace = vec(np.eye(n)).conj()
    reference = vec(np.eye(n) / n)
    bordered = np.zeros((rhs.size + 1, rhs.size + 1), dtype=complex)
    bordered[:-1, :-1] = generator
    bordered[:-1, -1] = reference
    bordered[-1, :-1] = trace
    target = np.concatenate((rhs, np.array([trace_value], dtype=complex)))
    solution = solve(bordered, target)
    return solution[:-1], solution[-1]


def make_core(d: int, g: float, seed: int) -> dict[str, np.ndarray]:
    """A reproducible full-rank, noncommuting, nonorthogonal-channel core."""
    rng = np.random.default_rng(seed)

    def random_complex(rows: int, columns: int) -> np.ndarray:
        return rng.normal(size=(rows, columns)) + 1j * rng.normal(
            size=(rows, columns)
        )

    raw_h = random_complex(d, d)
    hamiltonian = (raw_h + raw_h.conj().T) / 2
    spectrum = np.linalg.eigvalsh(hamiltonian)
    hamiltonian -= (spectrum[0] + spectrum[-1]) * np.eye(d) / 2
    hamiltonian *= 0.23 * g / np.linalg.norm(hamiltonian, 2)

    basis, _ = np.linalg.qr(random_complex(d, d))
    effect_eigenvalues = g * np.linspace(0.15, 0.72, d)
    root_effect = (basis * np.sqrt(effect_eigenvalues)) @ basis.conj().T
    isometry, _ = np.linalg.qr(random_complex(d + 2, d), mode="reduced")
    vectors = root_effect @ isometry.conj().T
    effect = vectors @ vectors.conj().T

    psi = random_complex(d, 1)[:, 0]
    psi /= np.linalg.norm(psi)
    return {"H": hamiltonian, "Q": effect, "vectors": vectors, "psi": psi}


def build_generator(core: dict[str, np.ndarray], g: float,
                    h: float, z: float) -> dict[str, np.ndarray | int | float]:
    d = core["H"].shape[0]
    n = d + 2
    m, e = d, d + 1
    ket = np.eye(n, dtype=complex)
    psi = np.zeros(n, dtype=complex)
    psi[:d] = core["psi"]
    carrier_gap = 0.9 * g
    carrier = np.diag([carrier_gap] * d + [0.0, 2 * carrier_gap])
    hamiltonian = carrier.astype(complex)
    hamiltonian[:d, :d] += core["H"]

    captures = []
    for column in core["vectors"].T:
        v = np.zeros(n, dtype=complex)
        v[:d] = column
        captures.append(np.outer(ket[:, m], v.conj()))
    hot_up = np.sqrt(g * h) * np.outer(ket[:, e], ket[:, m])
    hot_down = np.sqrt(g) * np.outer(ket[:, m], ket[:, e])
    release = np.sqrt(g) * np.outer(psi, ket[:, e])

    shape = (n * n, n * n)
    plus = sum((recycling(a) for a in captures), np.zeros(shape, complex))
    minus = z * sum((recycling(a.conj().T) for a in captures),
                    np.zeros(shape, complex))
    hot_current = recycling(hot_up) - recycling(hot_down)
    release_current = recycling(release) - z * recycling(release.conj().T)
    generator = commutator_generator(hamiltonian)
    effect = np.zeros((n, n), dtype=complex)
    pair_generators = []
    for a in captures:
        pair = dissipator(a) + z * dissipator(a.conj().T)
        generator += pair
        pair_generators.append(pair)
        effect += a.conj().T @ a + z * a @ a.conj().T
    hot_pair = dissipator(hot_up) + dissipator(hot_down)
    release_pair = dissipator(release) + z * dissipator(release.conj().T)
    generator += hot_pair + release_pair
    pair_generators.extend((hot_pair, release_pair))
    effect += hot_up.conj().T @ hot_up + hot_down.conj().T @ hot_down
    effect += release.conj().T @ release + z * release @ release.conj().T
    return {
        "n": n, "L": generator, "plus": plus, "minus": minus,
        "hot_current": hot_current, "release_current": release_current,
        "effect": effect, "start": vec(np.outer(ket[:, m], ket[:, m])),
        "pair_generators": np.array(pair_generators),
        "carrier_gap": carrier_gap,
    }


def reset_moments(g: float, h: float, checks: Checks) -> dict[str, float]:
    """Independent two-state absorbing-chain calculation."""
    transient = g * np.array([[-h, h], [1.0, -2.0]])
    first_vector = solve(-transient, np.ones(2))
    second_vector = solve(-transient, 2 * first_vector)
    mean = float(first_vector[0])
    second = float(second_vector[0])
    variance = second - mean**2
    mean_formula = (1 + 2 / h) / g
    second_formula = (2 + 6 / h + 8 / h**2) / g**2
    variance_formula = (1 + 2 / h + 4 / h**2) / g**2
    errors = {}
    for label, actual, expected in (
        ("mean", mean, mean_formula),
        ("second_moment", second, second_formula),
        ("variance", variance, variance_formula),
    ):
        errors[label] = checks.error(
            "reset " + label, (actual - expected) / abs(expected),
            "reset_moment_relative",
        )
    laplace_errors = []
    absorption = np.array([0.0, g])
    for s_over_g in (0.0, 0.1, 1.3):
        s = s_over_g * g
        actual = float(solve(s * np.eye(2) - transient, absorption)[0])
        expected = g**2 * h / (s**2 + g * (h + 2) * s + g**2 * h)
        laplace_errors.append(checks.error(
            "reset Laplace transform", actual - expected, "laplace_difference"
        ))
    return {
        "mean": mean, "second_moment": second, "variance": variance,
        "relative_errors": errors,
        "maximum_laplace_error": max(laplace_errors),
    }


def block_moments(system: dict, g: float, checks: Checks) -> dict:
    n, generator = system["n"], system["L"]
    trace = vec(np.eye(n)).conj()
    start, minus = system["start"], system["minus"]
    killed = generator - system["plus"]
    resolvent = solve(-killed, np.eye(n * n, dtype=complex))
    first = resolvent @ start
    second = resolvent @ first
    mean = checks.real("block duration", trace @ first, 1 / g)
    second_moment = checks.real("block second moment", 2 * trace @ second, 1 / g**2)
    mean_negative = checks.real("reverse count", trace @ minus @ first)
    factorial_negative = checks.real(
        "reverse factorial moment", 2 * trace @ minus @ resolvent @ minus @ first
    )
    mixed = checks.real(
        "duration-reverse mixed moment",
        trace @ (resolvent @ minus @ first + minus @ second), 1 / g,
    )
    reward_mean = 1 - mean_negative
    reward_second = 1 - mean_negative + factorial_negative
    reward_time = mean - mixed
    current = reward_mean / mean
    diffusion = (
        reward_second - 2 * current * reward_time + current**2 * second_moment
    ) / mean
    checks.require(mean > 0, "Block mean duration must be positive")
    checks.require(diffusion >= -TOLERANCES["positivity_slack"] * g,
                   "Block count diffusion must be nonnegative")
    spectral_abscissa = float(np.max(eigvals(killed).real))
    checks.require(spectral_abscissa < 0, "Killed generator must be stable")
    inverse_error = np.linalg.norm((-killed) @ resolvent - np.eye(n * n), np.inf)
    checks.error("killed inverse", inverse_error, "linear_residual")
    return {
        "mean": mean, "second_moment": second_moment,
        "mean_reverse_count": mean_negative,
        "reverse_factorial_second": factorial_negative,
        "duration_reverse_moment": mixed,
        "current": current, "noise": diffusion,
        "rho": first / mean,
        "killed_spectral_abscissa_over_g": spectral_abscissa / g,
    }


def stationary_cumulants(system: dict, g: float, checks: Checks) -> dict:
    n, generator = system["n"], system["L"]
    trace = vec(np.eye(n)).conj()
    zero = np.zeros(n * n, dtype=complex)
    rho, multiplier = constrained_solve(generator, zero, 1.0)
    first_derivative = system["plus"] - system["minus"]
    second_derivative = system["plus"] + system["minus"]
    current = checks.real("stationary current", trace @ first_derivative @ rho, g)
    response_rhs = current * rho - first_derivative @ rho
    response, response_multiplier = constrained_solve(generator, response_rhs, 0.0)
    noise = checks.real(
        "stationary noise",
        trace @ second_derivative @ rho + 2 * trace @ first_derivative @ response,
        g,
    )
    checks.error("trace preservation", np.linalg.norm(trace @ generator, np.inf) / g,
                 "linear_residual")
    checks.error("stationary equation", np.linalg.norm(generator @ rho, np.inf) / g,
                 "linear_residual")
    checks.error("stationary multiplier", abs(multiplier) / g, "linear_residual")
    checks.error("stationary trace", abs(trace @ rho - 1), "linear_residual")
    checks.error("response equation", np.linalg.norm(
        generator @ response - response_rhs, np.inf) / g, "linear_residual")
    checks.error("response multiplier", abs(response_multiplier) / g, "linear_residual")
    checks.error("response trace", abs(trace @ response), "linear_residual")
    matrix = unvec(rho, n)
    hermiticity_error = np.linalg.norm(matrix - matrix.conj().T, np.inf)
    checks.error("state Hermiticity", hermiticity_error, "state_difference")
    minimum_eigenvalue = float(np.linalg.eigvalsh((matrix + matrix.conj().T) / 2)[0])
    checks.error("state positivity", max(0.0, -minimum_eigenvalue), "positivity_slack")
    checks.require(noise >= -TOLERANCES["positivity_slack"] * g,
                   "Stationary count diffusion must be nonnegative")
    return {
        "rho": rho, "current": current, "noise": noise,
        "minimum_state_eigenvalue": minimum_eigenvalue,
        "hot_current": checks.real(
            "hot current", trace @ system["hot_current"] @ rho, g),
        "release_current": checks.real(
            "release current", trace @ system["release_current"] @ rho, g),
    }


def eigenvalue_cumulants(system: dict, g: float, checks: Checks) -> dict:
    """Independent finite differences of the full tilted matrix eigenvalue."""
    step = 1e-3
    values = {}
    for index in (-2, -1, 0, 1, 2):
        chi = index * step
        tilted = (system["L"] + np.expm1(chi) * system["plus"]
                  + np.expm1(-chi) * system["minus"])
        spectrum = eigvals(tilted)
        value = spectrum[np.argmax(spectrum.real)]
        values[index] = checks.real("tilted dominant eigenvalue", value, g)
    current = (values[-2] - 8 * values[-1] + 8 * values[1] - values[2]) / (12 * step)
    noise = (-values[2] + 16 * values[1] - 30 * values[0]
             + 16 * values[-1] - values[-2]) / (12 * step**2)
    checks.error("zero tilted eigenvalue", values[0] / g, "linear_residual")
    return {
        "step": step, "current": current, "noise": noise,
        "eigenvalues": {str(k * step): value for k, value in values.items()},
    }


def check_case(spec: dict, checks: Checks) -> dict:
    d, g, h, z = spec["d"], spec["g"], spec["h"], spec["z"]
    core = make_core(d, g, spec["seed"])
    core_commutator = core["H"] @ core["Q"] - core["Q"] @ core["H"]
    noncommutation = float(np.linalg.norm(core_commutator, 2) / g**2)
    gram = core["vectors"].conj().T @ core["vectors"]
    nonorthogonality = float(np.max(np.abs(gram - np.diag(np.diag(gram)))) / g)
    checks.require(noncommutation > 1e-3, "Test core must be noncommuting")
    checks.require(nonorthogonality > 1e-3, "Test capture channels must be nonorthogonal")
    system = build_generator(core, g, h, z)
    activity = float(np.linalg.eigvalsh(system["effect"])[-1] / g)
    checks.error("full activity", max(0.0, activity - 2), "activity_slack")
    reset = reset_moments(g, h, checks)

    # The reference keeps h fixed and removes only the cold reverse channels.
    baseline = block_moments(build_generator(core, g, h, 0.0), g, checks)
    q = core["Q"]
    core_killed = commutator_generator(core["H"]) - 0.5 * (
        np.kron(np.eye(d), q) + np.kron(q.T, np.eye(d))
    )
    core_resolvent = solve(-core_killed, np.eye(d * d, dtype=complex))
    core_trace = vec(np.eye(d)).conj()
    core_start = vec(np.outer(core["psi"], core["psi"].conj()))
    core_mean = checks.real("clean mean", core_trace @ core_resolvent @ core_start, 1 / g)
    core_second = checks.real(
        "clean second moment", 2 * core_trace @ core_resolvent @ core_resolvent @ core_start,
        1 / g**2,
    )
    expected_mean = core_mean + reset["mean"]
    expected_second = core_second + 2 * core_mean * reset["mean"] + reset["second_moment"]
    baseline_mean_error = checks.error(
        "frozen-h baseline mean", (baseline["mean"] - expected_mean) / expected_mean,
        "baseline_moment_relative",
    )
    baseline_second_error = checks.error(
        "frozen-h baseline second moment",
        (baseline["second_moment"] - expected_second) / expected_second,
        "baseline_moment_relative",
    )

    blocks = block_moments(system, g, checks)
    stationary = stationary_cumulants(system, g, checks)
    tilted = eigenvalue_cumulants(system, g, checks)
    errors = {
        "current_over_g": checks.error(
            "stationary versus block current",
            (stationary["current"] - blocks["current"]) / g, "current_difference"),
        "noise_over_g": checks.error(
            "stationary versus block noise",
            (stationary["noise"] - blocks["noise"]) / g, "noise_difference"),
        "stationary_state": checks.error(
            "stationary versus regenerative state",
            np.linalg.norm(stationary["rho"] - blocks["rho"], np.inf), "state_difference"),
        "tilted_current_over_g": checks.error(
            "eigenvalue versus stationary current",
            (tilted["current"] - stationary["current"]) / g, "tilted_current_difference"),
        "tilted_noise_over_g": checks.error(
            "eigenvalue versus stationary noise",
            (tilted["noise"] - stationary["noise"]) / g, "tilted_noise_difference"),
        "hot_current_conservation_over_g": checks.error(
            "hot-current conservation",
            (stationary["hot_current"] - stationary["current"]) / g, "current_difference"),
        "release_current_conservation_over_g": checks.error(
            "release-current conservation",
            (stationary["release_current"] - stationary["current"]) / g, "current_difference"),
    }

    affinity = entropy_rate = entropy_error = None
    if z > 0:
        affinity = 2 * np.log(1 / z) - np.log(1 / h)
        entropy_rate = (
            np.log(1 / z) * (stationary["current"] + stationary["release_current"])
            - np.log(1 / h) * stationary["hot_current"]
        )
        entropy_error = checks.error(
            "entropy-current identity",
            (entropy_rate - affinity * stationary["current"]) / g,
            "entropy_difference",
        )

    stall_result = None
    fano_stationary = fano_blocks = timing_diffusion = None
    if spec["stall"]:
        checks.error("stall ratio", h - z**2, "linear_residual")
        weights = np.array([1.0] * d + [1 / z, z])
        gibbs = vec(np.diag(weights / weights.sum()))
        gibbs_residual = checks.error(
            "bare Gibbs stationary equation", np.linalg.norm(system["L"] @ gibbs, np.inf) / g,
            "linear_residual",
        )
        gibbs_distance = checks.error(
            "bare Gibbs stationary state", np.linalg.norm(stationary["rho"] - gibbs, np.inf),
            "state_difference",
        )
        pair_residuals = [
            checks.error("equilibrium jump pair", np.linalg.norm(pair @ gibbs, np.inf) / g,
                         "linear_residual")
            for pair in system["pair_generators"]
        ]
        stall_currents = {}
        for label in ("current", "hot_current", "release_current"):
            stall_currents[label] = checks.error(
                "stall " + label, stationary[label] / g, "current_difference"
            )
        checks.error("stall block reward", blocks["mean_reverse_count"] - 1,
                     "current_difference")
        checks.error("stall affinity", affinity, "entropy_difference")
        stall_result = {
            "bare_gibbs_unnormalized_weights": weights.tolist(),
            "gibbs_residual_over_g": gibbs_residual,
            "gibbs_state_distance": gibbs_distance,
            "maximum_jump_pair_residual_over_g": max(pair_residuals),
            "absolute_currents_over_g": stall_currents,
            "fano_and_timing_diffusion_formed": False,
        }
    else:
        checks.require(stationary["current"] > 1e-6 * g,
                       "Driven test must have a positive non-negligible current")
        fano_stationary = stationary["noise"] / stationary["current"]
        m, mu = blocks["mean_reverse_count"], blocks["mean"]
        fano_blocks = ((1 - m) * blocks["second_moment"] / mu**2 - 1
                      + 2 * blocks["duration_reverse_moment"] / mu
                      + blocks["reverse_factorial_second"] / (1 - m))
        errors["fano"] = checks.error(
            "expanded signed Fano formula", fano_stationary - fano_blocks,
            "fano_difference",
        )
        timing_diffusion = stationary["noise"] / stationary["current"]**2

    return {
        **spec,
        "capture_channels": core["vectors"].shape[1],
        "core_commutator_norm_over_g_squared": noncommutation,
        "maximum_channel_overlap_over_g": nonorthogonality,
        "core_effect_spectrum_over_g": (np.linalg.eigvalsh(q) / g).tolist(),
        "active_hamiltonian_norm_over_g": float(np.linalg.norm(core["H"], 2) / g),
        "carrier_gap": system["carrier_gap"],
        "maximum_full_jump_effect_over_g": activity,
        "reset": reset,
        "frozen_h_reference": {
            "clean_mean": core_mean, "clean_second_moment": core_second,
            "block_mean": baseline["mean"],
            "block_second_moment": baseline["second_moment"],
            "relative_mean_error": baseline_mean_error,
            "relative_second_moment_error": baseline_second_error,
        },
        "regenerative": {k: v for k, v in blocks.items() if k != "rho"},
        "stationary": {k: v for k, v in stationary.items() if k != "rho"},
        "tilted_eigenvalue_derivatives": tilted,
        "fano_stationary": fano_stationary,
        "fano_regenerative_expansion": fano_blocks,
        "timing_diffusion": timing_diffusion,
        "affinity": affinity, "entropy_rate": entropy_rate,
        "entropy_identity_error_over_g": entropy_error,
        "errors": errors, "stall_control": stall_result,
    }


def run() -> dict:
    start_time = time.perf_counter()
    checks = Checks()
    cases = [check_case(dict(spec), checks) for spec in CASES]
    return {
        "status": "passed",
        "scope": "Finite algebra and counting-convention checks; not asymptotic scaling or microscopic bath validation.",
        "error_normalization": (
            "Currents, count noise, generator residuals and entropy rates are divided by g. "
            "States and Fano factors use absolute errors. Reset and reference moments use relative errors."
        ),
        "case_count": len(cases),
        "check_count": checks.count,
        "tolerances": TOLERANCES,
        "maximum_errors": checks.maximum_errors,
        "cases": cases,
        "runtime_versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "float_dtype": "complex128 / float64",
        },
        "runtime_seconds": time.perf_counter() - start_time,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "reproduce": "python verification/check_clock.py --output verification/finite_results.json",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="write the JSON record to this file instead of standard output")
    arguments = parser.parse_args()
    record = run()
    encoded = json.dumps(record, indent=2, allow_nan=False) + "\n"
    if arguments.output is None:
        sys.stdout.write(encoded)
    else:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded, encoding="utf-8")
        print(f"Passed {record['check_count']} checks across {record['case_count']} cases; "
              f"wrote {arguments.output}.")


if __name__ == "__main__":
    main()
