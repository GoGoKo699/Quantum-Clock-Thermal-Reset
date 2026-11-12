# Quantum Clock Thermal Reset

**Finite thermal recycling can preserve a quantum clock's precision and elapsed-time advantage.** This project replaces an ideal pure-state reset with a time-independent thermal interface, retains its finite waiting time and reverse transitions, and bounds the resulting signed-count noise.

The interface adds two levels to a complete-reset clock. Its quantitative theorem controls the mean period, reverse-count correlations, and variance without eliminating the reset states. Applied to the quasiideal clock family, it gives the following result for every fixed exponent loss $`0<\eta<1`$ and sufficiently large core dimension $`d`$:

```math
P_d\ge c_\eta d^{2-\eta},\qquad
j_d=\Theta_\eta(g/d),\qquad
gD_{{\rm time},d}\le C_\eta d^{-1+\eta}\longrightarrow0.
```

Here $`P=j/D_N`$ is signed-count precision, $`D_N=\lim_{t\to\infty}\operatorname{Var}N(t)/t`$, and $`D_{\rm time}=D_N/j^2`$ is the variance growth rate of the calibrated estimate $`N(t)/j`$. Every physical jump in the enlarged device is charged to the common bound $`\sum_\alpha L_\alpha^\dagger L_\alpha\le2gI`$.

Under the same complete-device event-rate budget, every finite-state classical Markov clock satisfies

```math
gD_{{\rm time},{\rm C}}\ge\frac12.
```

Thus the advantage concerns useful elapsed-time accuracy, including the longer period of a larger clock and the entire modeled reset process.

## Thermal resources

For a chosen $`\eta`$, both bath temperatures can remain fixed as $`d`$ grows. A sufficient condition is $`\theta:=\beta_H/\beta_C\le\eta/44`$. The construction then uses

```math
z_d=d^{-11},\qquad
h_d=d^{-22\theta},\qquad
q_d=\frac{11\log d}{\beta_C},\qquad
\Sigma_d=22(1-\theta)\log d.
```

$`z_d`$ and $`h_d`$ are the cold and hot upward/downward ratios, $`q_d`$ is the cold energy gap, and $`\Sigma_d`$ is stationary bath entropy per net tick in units of $`k_B`$. The hot absorption slows with dimension, but its reset delay remains subleading to the core period and its variance fits within the specified exponent loss.

| Resource or output | Supported account |
|---|---|
| Complete clock dimension | $`d+2`$ |
| Sum of all jump effects | At most $`2gI`$, including every reset and reverse event |
| Active core Hamiltonian | Centered norm less than $`g/4`$ |
| Two fixed temperatures | Chosen for the desired fixed $`\eta`$ |
| Bare energy width | $`2q_d=O(\log d)`$ |
| Engineered thermal coupling channels | At most $`d+2`$ |
| Stationary bath entropy per net tick | $`O(\log d)`$ |

A separate fixed-gap version has a dimension-independent reset-time scale but requires a progressively colder reservoir. The [resource account](science/thermodynamics.md#4-two-distinct-ways-to-obtain-logarithmic-entropy) keeps these choices separate.

## Read the science

The [scientific overview](science/README.md) gives the complete reading route. The [physical interpretation](science/interpretation.md) explains how the reset mechanism and the performance measures fit together.

| To inspect | Read |
|---|---|
| Input clock, full jump model, output and charged resources | [Model](science/model.md) |
| Explicit finite hypotheses and quantitative transfer bound | [Finite-rate recycling theorem](science/finite_rate_recycling.md) |
| Reverse-event correlations, stationary state and tilted cumulants | [Signed counting statistics](science/counting_statistics.md) |
| Clean-clock source reconstruction and dimension asymptotics | [Quasiideal application](science/quasiideal_application.md) |
| Classical benchmark with all reset activity included | [Classical comparison](science/classical_comparison.md) |
| Heat balance, bath channels and microscopic limit order | [Thermodynamics](science/thermodynamics.md) |
| Inherited ingredients and the precise contribution | [Related work](references/RELATED_WORK.md) and [references](references/REFERENCES.md) |
| Reproducible finite calculations and their limits | [Verification](verification/README.md) |

The quasiideal core is inherited from Woods et al. The serial thermal bridge and logarithmic-affinity strategy have direct antecedents in Meier et al. The added result is a quantitative bound for the retained finite-rate interface and its simultaneous dimension, entropy and elapsed-time consequences; the [comparison](references/RELATED_WORK.md) credits those dependencies explicitly.

## Scope

The theorem is exact for the specified finite-dimensional thermal GKLS generator. Its microscopic foundation takes a clustered weak-coupling limit at each fixed dimension, followed by long-time statistics of the limiting generator and then the dimension limit. Uniform infinite-time counting convergence at fixed microscopic coupling is not established.

The device uses static engineered coupling vectors and explicit thermal energy resources. The signed output record and the actual mean current are supplied to the estimator. Detector amplification, record erasure, learning an unknown calibration, reservoir preparation and fabrication are separate costs. The result closes the modeled cyclic reset gap; it does not price a complete laboratory clock.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
