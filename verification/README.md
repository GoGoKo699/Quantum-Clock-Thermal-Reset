# Finite verification

The analytical claims are proved in the [scientific account](../science/README.md). The numerical checks here test finite generator algebra, signed-count conventions, reset moments, and thermodynamic consistency. They do not approximate the large-dimension quasiideal family or establish a microscopic reservoir limit.

## Reproduce

The recorded environment uses Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_clock.py --output verification/finite_results.json
```

The script exits unsuccessfully if a declared tolerance fails. Its checks use explicit exceptions and remain active under Python optimization. The committed [finite_results.json](finite_results.json) records the input cases, tolerances, normalization of errors, runtime versions, script SHA256 and individual results. Runtime duration can change between runs; agreement is assessed through the stated numerical tolerances, not byte identity of floating-point output.

## Independent calculations

For each finite device, the script builds its complete matrix generator, including both directions of each thermal transition and the carrier Hamiltonian. The core Hamiltonian and capture effect do not commute, and the capture channels are nonorthogonal. The deliberately overcomplete channel representation exercises the summed-effect formulas; it can be compressed through a spectral decomposition of the same effect without changing the generator or aggregated count.

Three calculations are compared:

1. **Stationary response of the full tilted generator.** A bordered linear solve gives the stationary state and the derivative of its tilted eigenvector. These give the mean current and second counting cumulant.
2. **Direct tilted eigenvalues.** Five-point finite differences of the dominant eigenvalue give a separate check of the current and noise convention.
3. **Regenerative block moments.** The killed inverse gives duration moments, reverse-count moments and their mixed moment. The renewal-reward expression must give the same current, noise and stationary state.

The two-state reset is also checked separately. Its backward equations and Laplace transform reproduce the general-hot-ratio formulas. At each chosen hot ratio, removing only the cold reverse channels gives the exact convolution of that reset and the clean core interval. This checks the frozen-hot-rate comparison used in the proof.

## Cases and recorded agreement

| Case | Core dimension | Hot ratio | Cold reverse ratio | Purpose |
|---|---:|---:|---:|---|
| Irreversible reference | 2 | 0.5 | 0 | Reset convolution and the reference counting law |
| Finite reverse, slow reset | 3 | 0.08 | 0.012 | Duration–reverse-count correlations |
| Slower reset | 4 | 0.025 | 0.035 | Retained auxiliary dynamics and substantial backtracking |
| Thermal stall | 3 | 0.16 | 0.4 | Equal-temperature Gibbs state and vanishing currents |

In the committed run, stationary and regenerative noise agree within $`8.4\times10^{-17}g`$, and their expanded Fano factors within $`4.5\times10^{-16}`$. The direct eigenvalue finite difference agrees in noise within $`5.5\times10^{-10}g`$. General reset moments and frozen-hot reference moments agree at relative error below $`1.1\times10^{-15}`$. These small numbers describe the tested matrices and implementation, not an accuracy guarantee for arbitrary dimension or hardware.

At stall, $`h=z^2`$ makes the bath temperatures equal and the affinity zero. The expected bare Gibbs weights are

```math
\rho_\beta\ \propto\ I_C+z^{-1}P_m+zP_e.
```

Every jump pair preserves this state separately, and the capture, hot and release currents vanish. The committed stationary-state difference is below $`3.1\times10^{-16}`$, with all three currents below $`4.8\times10^{-17}g`$. The program does not divide by the zero current: precision and timing diffusion are recorded as null at this control.

## What establishes each claim

| Claim | Evidence |
|---|---|
| Every positive-capture block terminates under the finite conditions | Lyapunov survival proof in [theorem Section 4](../science/finite_rate_recycling.md#4-stability-before-inversion) |
| Finite reverse rates preserve the first two signed cumulants within the stated bound | Exact joint transform, resolvent inequalities and reward calculation in [theorem Sections 5–6](../science/finite_rate_recycling.md#5-duration-and-reverse-count-moments) and [counting statistics](../science/counting_statistics.md) |
| The quasiideal input has bounded strength and a polynomial survival inverse | Source reconstruction and positive absorption floor in [the application](../science/quasiideal_application.md#1-clean-input-lemma) |
| Nearquadratic precision and decreasing timing diffusion survive the thermal cycle | Dimension-dependent parameter substitution and explicit gates in [application Section 2](../science/quasiideal_application.md#2-application-with-two-fixed-temperatures) |
| The classical comparison charges all device events | Uniformization proof in [classical comparison](../science/classical_comparison.md#2-uniformization-proof) |
| The entropy per cycle includes all retained thermal transitions | Exact occupation and heat identities in [thermodynamics](../science/thermodynamics.md#2-exact-entropy-telescoping-before-eliminating-any-state) |
| Finite implementations of the formulas agree | The reproducible matrix checks in this directory |

The generic finite examples are not quasiideal scaling demonstrations and need not beat the classical timing benchmark. The asymptotic advantage rests on the cited clean-clock theorem and the explicit conversion proof. No experiment, uniform microscopic bath approximation, detector-cost bound, or calibration-cost bound is certified by these checks.
