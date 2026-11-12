# Scientific account

The central question is whether an ideal quantum clock's useful timing advantage survives a finite thermal reset. The result is a quantitative conversion theorem for pure complete-reset clocks, together with an explicit nearquadratic application and a classical comparison under the same full-device event-rate cap.

The account has three connected layers. The [model](model.md), [finite-rate theorem](finite_rate_recycling.md), and [counting statistics](counting_statistics.md) establish the exact finite-generator statement. The [quasiideal application](quasiideal_application.md) supplies a growing family with a controlled absorption-time inverse, and the [classical comparison](classical_comparison.md) identifies its operational advantage. The [thermal account](thermodynamics.md) assigns heat and entropy to the retained interface and states the resources and limit order needed for its physical interpretation.

## Main claims and dependencies

| Claim | Conditions that matter | Proof route |
|---|---|---|
| Finite-rate recycling changes signed inverse precision by an explicit controlled amount | Pure complete reset; stable core; supplied all-input survival inverse; sufficiently small cold reverse ratio; hot ratio frozen in the comparison | [Finite-rate theorem, Sections 1–7](finite_rate_recycling.md) |
| The controlled observable is the full signed current and its diffusion | Reverse counts correlated with block durations; positive captures regenerate the whole device | [Counting statistics, Sections 1–5](counting_statistics.md) |
| Nearquadratic precision and decreasing elapsed-time diffusion survive recycling | Quasiideal source; fixed target exponent loss; polynomial absorption floor; the stated bath resources | [Quasiideal application](quasiideal_application.md) |
| Classical timing diffusion stays above the inverse complete activity cap | Finite-state time-homogeneous Markov dynamics; all events charged; supplied mean current | [Classical comparison](classical_comparison.md) |
| Entropy per net cycle is logarithmic in dimension | Static thermal pairs for a bare-degenerate core; exact serial occupation balance; long time at fixed device | [Thermodynamics, Sections 1–4](thermodynamics.md) |
| Static reservoirs support the effective model in a controlled ordered limit | Clustered weak coupling; engineered spectra and channels; explicit Lamb-shift tuning | [Thermodynamics, Section 5](thermodynamics.md#5-static-weak-coupling-foundation) |

The [interpretation](interpretation.md) explains why precision alone is insufficient, how finite reset noise enters, and which cost gap the theorem closes. The [related-work account](../references/RELATED_WORK.md) separates the imported clock and thermal architecture from the new finite-rate bound.

## Reading routes

For the mechanism and conclusion, read [interpretation](interpretation.md), [model](model.md), the result in [theorem Section 1](finite_rate_recycling.md#1-the-finite-conditions-and-conclusion), and the [application](quasiideal_application.md).

For the proof, read the [model](model.md), [reference inverse and perturbation argument](finite_rate_recycling.md#3-the-killed-generator-and-its-survival-inverse), [joint counting transform](counting_statistics.md#2-the-joint-transform-of-duration-and-reverse-count), and the [precision comparison](finite_rate_recycling.md#6-signed-precision-comparison). Then check the [source reconstruction](quasiideal_application.md#1-clean-input-lemma) and [classical bound](classical_comparison.md#2-uniformization-proof).

For physical resource accounting, read [thermodynamics](thermodynamics.md) with the [model's complete activity sum](model.md#count-the-complete-device-activity). The exact finite-generator theorem and the microscopic weak-coupling interpretation have different scopes.

The [finite verification](../verification/README.md) checks independent count-statistics calculations, reset moments and a thermal equilibrium control. It supplies reproducible algebraic checks; the asymptotic law is established by the written proof and the cited quasiideal theorem.
