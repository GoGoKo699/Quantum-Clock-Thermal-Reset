# Relation to prior work

The question here is whether a nearquadratic quantum-clock dimension advantage survives continuous thermal recycling when the return stage has finite rates and its reverse transitions are counted. The output is a stationary signed count. The relevant resources include the full jump-effect budget, the recycling states, thermal gaps and temperatures, and entropy per net cycle.

The added result is a quantitative transfer theorem for the expanded finite-rate generator. The quasiideal core, serial thermal bridge, and general idea of suppressing reverse transitions with logarithmic affinity all have prior antecedents. The comparison below identifies those ingredients explicitly.

## The closest architecture: Meier et al. 2025

[Meier et al.](REFERENCES.md#meier2025) already establish a quantum precision advantage exponential in entropy production. Their ring clock transports a coherent excitation and closes the ring through a thermally biased reset. The Methods propose the serial path $`\ell\to m\to e\to r`$ and adiabatically eliminate its intermediate states to obtain the effective endpoint jump. The same Methods explain that polynomially small reverse-jump strength gives logarithmic entropy, while acknowledging the role of dimension-dependent spectral sensitivity. Their numerical family has precision approximately $`n^{1.31}`$ and tests a reverse ratio $`n^{-4}`$ through $`n=200`$.

The present bridge is a multichannel extension of that architecture. Its distinguishing claim is a uniform finite-rate timing estimate for the retained interface, followed by transfer of the stronger quasiideal dimension scaling. It does not introduce the thermal-bridge principle or the exponential precision-entropy separation. Replacing a core and quoting a fast-interface limit would not establish the result: the full device's increasingly small count variance must be controlled under the common rate budget.

## Inherited ideal-clock construction

[Woods et al.](REFERENCES.md#woods2022) construct quasiideal clocks with precision arbitrarily close to quadratic in clock dimension and establish their advantage over finite classical clocks in their specified model. That construction supplies the clean timing resource here. Its Hamiltonian, summed capture effect, nonzero lower hazard, and actual waiting-time moments are checked after a common strength normalization; they are not new ideal-clock results.

The transfer controls stationary signed-count precision after adding thermal recycling. It does not upgrade the one-tick dimension limits of [Woods et al.](REFERENCES.md#woods2022) or [Yang and Renner](REFERENCES.md#yang2020) into a universal bound for all stationary nonrenewal clocks. Correlations retained between ticks can change that comparison.

## Light-matter realization and the unresolved reset step

[Dost and Woods](REFERENCES.md#dost2023) give a light-matter realization of quasiideal emission and analyze its entropy. Their Section IV explicitly distinguishes emission from resetting the clockwork. Appendix C proposes multiple copies, photon-triggered switching, and preparation of the inactive copy within a sufficiently long window. The initial state can require a non-energy-preserving unitary.

This is a concrete antecedent for physical quasiideal time signals, but it does not supply the continuous two-temperature finite-rate recycling analyzed here. The present contribution is not a more accurate clean emission law; it is the preservation of its useful timing performance under a specified cyclic thermal interface, with the corresponding operating entropy accounted for.

## Thermal probability concentration and finite decay rates

[Schwarzhans et al. 2021](REFERENCES.md#schwarzhans2021) separate coherent temporal probability concentration from the irreversible mechanism that produces ticks. They construct thermal-machine clockworks from many qubits and show why a finite decay rate can limit the usefulness of an increasingly narrow excitation peak. Their analysis begins from thermal machine preparations, with coherent evolution faster than rethermalization; the low-temperature decay model suppresses the reverse process. The explored accuracy regime is linear in target-ladder size before the finite-decay limitation, while the full machine has additional complexity.

That work makes finite irreversible rates a substantive resource rather than an innocuous implementation detail. It does not contain a uniform recycling theorem for arbitrary complete-reset cores or the simultaneous nearquadratic dimension, logarithmic entropy, and bounded-strength timing result considered here.

## What the pinned companion results already establish

The [entropy-limit notes](REFERENCES.md#clock-entropy) study one complete rank-one forward/reverse jump pair and derive an affinity-only ceiling on signed-count precision. Their finite-bias construction establishes logarithmic affinity order, but has net tick rate $`\Theta(gd^{-2})`$ and precision at least $`d`$. They also derive the exact serial entropy balance before elimination and explicitly leave finite-rate timing transfer open. Neither the entropy telescoping identity nor logarithmic cost order is new here. The expanded multichannel recycling generator also falls outside the single-pair converse's literal hypotheses, so that converse is not presented as a matching lower bound for this device class.

The [restart-limit notes](REFERENCES.md#clock-restart) normalize the Woods construction to a common Hamiltonian and jump-strength scale, then study independent hidden Poisson faults that reset the entire device. They introduce a useful elapsed-time comparison: regular ticks obtained only by slowing a device need not improve timing diffusion. The present application inherits that normalization and distinction. Thermal reverse events and finite auxiliary residence times are a different physical perturbation, and the stationary signed-count proof must handle them explicitly.

## Microscopic thermal foundations and general realization theorems

The microscopic interpretation uses the nearly degenerate weak-coupling setting of [Trushechkin](REFERENCES.md#trushechkin2021), with counted-generator thermodynamics informed by [Gerry and Segal](REFERENCES.md#gerry2023). Our [thermodynamic account](../science/thermodynamics.md) specifies the bare Hamiltonian, static channels, Lamb-shift tuning, and order of limits. A scalar adjoint rate ratio alone is insufficient to justify those choices.

[Luo et al. 2026](REFERENCES.md#luo2026) prove an equivalence between thermal Lindbladians, energy-conserving thermal collision models, and Markovian thermal operations for nontrivial system Hamiltonians. Protocol I constructs collisions for an already specified thermal generator and gives finite-time simulation errors. Their multibath example combines bath-specific collisions into sequential strokes. This is a relevant realization theorem, including degenerate energy subspaces, but it does not supply the clock's finite-rate capture/recycling transformation, its uniform dimension-dependent count-variance bound, or a fixed-coupling infinite-time microscopic counting theorem.

General autonomy constructions also answer different questions. [Woods and Horodecki](REFERENCES.md#woodshorodecki2023) add an explicit clock to control thermodynamic operations and bound its degradation. [Burgarth, Facchi, and Hillier](REFERENCES.md#burgarth2023) give autonomous dilations using an infinite-dimensional clock and singular localized states. Such constructions do not automatically preserve the finite clock-resource budget used here. None is invoked as a substitute for analyzing the retained recycling dynamics.

## Readout and recent clock proposals

[Meier et al. 2026](REFERENCES.md#meier2026) exploit quantum correlations between successive ticks. Their mechanism is nonrenewal and differs from sharpening each complete-reset cycle. It is an important reason to state the output and memory assumptions precisely; no universal optimality claim over such correlated clocks follows from this work.

[Nelmes et al. 2026](REFERENCES.md#nelmes2026) study engineered coherent transport approaching the precision-resolution exponent and propose repeated operation through a sudden-quench initialization and detachment protocol. Robustness to coarse quench timing is useful, but it is a different resource contract from an always-connected two-bath recycling stage. Their result is not used to certify the present achievability statement.

[Wadhia et al.](REFERENCES.md#wadhia2025) experimentally separate microscopic clockwork dissipation from charge-sensor dissipation, with the latter dominating in their apparatus. [Schwarzhans et al. 2026](REFERENCES.md#schwarzhans2026) model an autonomous thermal detector and analyze efficiency, jitter, dead time, and dark counts. [Gong's comment](REFERENCES.md#gong2026) disputes interpreting particular readout dissipation as a universal fundamental cost. These sources concern resources beyond the cyclic core reset priced here. The present entropy formula includes the complete recycling interface, but assumes an ideal signed output record; it does not solve detector amplification or record-erasure costs.

[Prech et al.](REFERENCES.md#prech2025) distinguish optimal estimation from a full untimed Markov event record from the performance of a selected current. That distinction also applies here: signed-tick precision is the stated observable, and the calibrated elapsed-time diffusion is computed for that output. Access to additional channels or an independently timestamped record would be a different inference problem.

## Precise added statement

The finite-rate result transfers a clean complete-reset clock with a polynomial absorption-time bound into a two-temperature device with two additional system states. It controls the first two signed-count cumulants, includes all reverse events, and keeps the complete jump-effect budget bounded. Applied to the quasiideal source, it retains nearquadratic dimension precision together with improving elapsed-time diffusion and logarithmic stationary bath entropy.

The physical interpretation has a stated order of limits. The fixed-gap construction uses a progressively colder reservoir; the fixed-temperature construction uses logarithmically growing bare gaps and an explicitly slower hot transition. The theorem does not assert that all of these resources remain fixed simultaneously, nor that finite-time microscopic state convergence automatically supplies infinite-time counting convergence.
