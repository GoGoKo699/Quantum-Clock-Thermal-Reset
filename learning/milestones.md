# Thirty milestones for the finite thermal reset

[Learning overview](README.md) · [Anchor bridge](anchor_bridge.md) · [Scientific account](../science/README.md)

This map follows the scientific question: **when does an ideal quantum clock retain useful timing performance after its reset becomes a finite thermal process?** Its targets concern the model, the quantitative conversion, the inherited clock family, and the resources required by the final result.

The educational anchor is Landi, Kewming, Mitchison and Potts, *Current Fluctuations in Open Quantum Systems: Bridging the Gap Between Quantum Continuous Measurements and Full Counting Statistics*, PRX Quantum 5, 020201 (2024), [author-hosted published PDF](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf). Page numbers below refer to that PDF and its printed article pages. It supplies the jump, waiting-time and counting-statistics framework. The quantitative recycling bound, quasiideal input and clustered thermal realization have their own canonical project proofs and primary-source dependencies; a pointer to the anchor does not attribute those results to the review.

## Allocation and dependencies

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | M01–M12 | Connect individual jumps and conditional evolution to renewal clocks, signed currents, noise and thermal pairing. M12 integrates the two descriptions of a complete clock record. |
| Narrative/innovation | M13–M30 | Follow the retained reset through its finite-time law, stability and moment control, then connect that theorem to heat, the inherited coherent core, the classical benchmark and the precise advantage. M30 integrates the result and its scope. |

The 12/18 allocation reflects the argument's structure. Twelve foundational targets are enough to connect the two mathematical descriptions of the output—waiting intervals and accumulated counts—without turning the review's entire contents into prerequisites. The larger second phase is needed because preserving precision requires several linked controls: the reset duration, reverse-event correlations, an all-input survival bound, complete event activity, thermal resource choices and an imported dimension scaling. The map follows those connections rather than splitting individual algebraic steps into separate milestones.

Within each phase, dependencies move from local objects to the complete claim. The final milestone of each phase is a synthesis. The map identifies the load-bearing ideas; the canonical science pages retain the detailed proofs and parameters.

## Phase I — Background/preliminaries

### M01 — A clock as a physical process with an output

- **Central question:** Which part of a quantum clock is the evolving system, and which part is the information used to tell time?
- **Understanding target:** Distinguish the density matrix, time-independent generator and emitted record. Explain why a master equation describes an average evolution while a clock's performance depends on fluctuations of individual records.
- **Dependencies and story role:** Starting point. Establishes the objects whose dynamics, output and cost will be tracked separately throughout this phase.
- **Conceptual connection:** An open quantum system becomes a timekeeping device only after an output convention and a performance quantity are specified.
- **Source pointers:** Anchor [II A, “Basic setting,” p. 4, Eqs. (5)–(7)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=4). Project: [input clock](../science/model.md#1-the-input-clock), [observable record](../science/model.md#3-observable-record-and-block-boundaries).

### M02 — Jump probability, backaction and total activity

- **Central question:** What does one jump operator determine about an event?
- **Understanding target:** Connect its recycling map to the post-event state and its effect operator to the event probability. Distinguish one channel's rate from the sum of all channel effects, including events that leave an internal state unchanged.
- **Dependencies and story role:** Uses M01. Moves from the average generator to the local event rule from which both records and resource accounting are built.
- **Conceptual connection:** The same operator specifies both a physical state change and its statistical weight; this is why adding reset channels changes the activity budget.
- **Source pointers:** Anchor [II C, “Quantum jumps,” pp. 7–9, especially Eqs. (17)–(25) on pp. 7–8](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=7). Project: [jump model](../science/model.md#2-the-enlarged-clock), [complete activity](../science/model.md#count-the-complete-device-activity).

### M03 — Evolution conditioned on no observed tick

- **Central question:** What still happens while the selected output remains silent?
- **Understanding target:** Explain why removing a monitored recycling term produces a trace-decreasing conditional generator. Distinguish “no positive capture” from “no physical event”: unobserved hot transitions and negative captures remain inside the former evolution.
- **Dependencies and story role:** Uses M01–M02. Introduces the conditional dynamics needed to turn an output event into a first-passage problem.
- **Conceptual connection:** A choice of observed channels determines which evolution is killed and which processes continue during the waiting interval.
- **Source pointers:** Anchor [VI A, “Waiting-time distributions,” pp. 39–40, Eqs. (254)–(261)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=39). Project: [killed generator](../science/finite_rate_recycling.md#3-the-killed-generator-and-its-survival-inverse).

### M04 — Survival, absorption and waiting-time moments

- **Central question:** How does the probability of remaining silent determine a mean waiting time and its variance?
- **Understanding target:** Relate survival probability to the first-event density and interpret the killed inverse as integrated survival. Distinguish finite moments from a dark component that can survive forever, and understand why moment formulas require stability.
- **Dependencies and story role:** Uses M03. Converts conditional evolution into statistical quantities that can later be bounded.
- **Conceptual connection:** The operator $`(-\mathcal K)^{-1}`$ packages all waiting times from all initial states; its norm will carry physical information about rare long excursions.
- **Source pointers:** Anchor [VI A, p. 40, Eqs. (258)–(266)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=40). Project: [clean survival inverse and moment identities](../science/model.md#1-the-input-clock).

### M05 — Complete reset and independent cycles

- **Central question:** When can successive waiting intervals be treated as independent copies of one experiment?
- **Understanding target:** Identify a complete reset by its state-independent normalized output. Explain why a common output state across aggregated channels gives regeneration, whereas resetting only a subsystem can preserve memory between events.
- **Dependencies and story role:** Uses M02–M04. Connects a local jump property to the global structure of a long record.
- **Conceptual connection:** A rank-one recycling map turns an open-system trajectory into a renewal construction without replacing coherent evolution inside a cycle by a classical process.
- **Source pointers:** Anchor [VI B.2, “Renewal processes,” p. 43, Eqs. (288)–(293)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43). Project: [complete-reset input](../science/model.md#1-the-input-clock), [exit normalization and regeneration](../science/counting_statistics.md#1-exit-normalization-and-regeneration).

### M06 — Signed marks and the chosen observable

- **Central question:** Why are a count of positive events and a net forward-minus-reverse count different clocks?
- **Understanding target:** Read a current as a weighted sum of jump records and distinguish channel labels, unsigned activity and signed transport. Explain why unobserved channel labels can be summed while the sign of a reverse capture remains consequential.
- **Dependencies and story role:** Uses M02 and M05. Specifies the output before relating its fluctuation statistics to timing.
- **Conceptual connection:** Thermodynamic transport uses oriented events; a block may therefore contain several events while carrying a net reward smaller than one.
- **Source pointers:** Anchor [II D, “Output currents,” p. 10, Eqs. (37)–(40)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=10). Project: [record and block boundaries](../science/model.md#3-observable-record-and-block-boundaries).

### M07 — Mean current, count noise and interval precision

- **Central question:** How are the regularity of one interval and the fluctuation growth of a long count related?
- **Understanding target:** Distinguish mean current $`j`$, count-noise rate $`D_N`$, Fano factor $`F=D_N/j`$ and precision $`P=1/F`$. Explain when the ordinary renewal relation $`D_N=\sigma^2/\mu^3`$ applies and why it cannot be transferred unchanged to arbitrary signed rewards.
- **Dependencies and story role:** Uses M04–M06. Connects individual-cycle statistics to the observable used by the theorem.
- **Conceptual connection:** An interval distribution determines count diffusion only with the appropriate independence and reward assumptions. The project uses no factor of two in $`D_N`$.
- **Source pointers:** Anchor [III C, “The noise,” pp. 19–20, Eqs. (85)–(89)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=19), and [VI B.2, p. 43, Eq. (294)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43). Project: [performance conventions](../science/model.md#4-performance-conventions).

### M08 — Time estimation charges the period

- **Central question:** Does a larger tick precision necessarily mean a better elapsed-time estimate?
- **Understanding target:** Explain the calibrated estimator $`N(t)/j`$ and its diffusion $`D_{\rm time}=D_N/j^2=1/(jP)`$. Distinguish improving regularity from merely slowing the output, and identify the assumption that the actual mean current is already known.
- **Dependencies and story role:** Uses M07. Gives the operational meaning needed to judge the eventual quantum advantage.
- **Conceptual connection:** The current's mean and variance must be combined before a claim about useful timekeeping follows from a precision law.
- **Source pointers:** Anchor [III C, pp. 19–20, noise and long-time estimation](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=19). Project: [precision paired with the period](../science/interpretation.md#precision-must-be-paired-with-the-period), [performance conventions](../science/model.md#4-performance-conventions). The elapsed-time application is supplied by the project.

### M09 — Counting fields encode the signed-count distribution

- **Central question:** How can a deterministic matrix equation encode the distribution of a random signed count?
- **Understanding target:** Explain why a counting field multiplies recycling terms by event weights while leaving loss terms unchanged. Translate the anchor's Fourier factors $`e^{i\chi\nu_k}`$ to the project's real moment-generating factors $`e^{\pm\chi}`$ without confusing the derivative conventions.
- **Dependencies and story role:** Uses M03 and M06–M07. Introduces a second route to the same current statistics.
- **Conceptual connection:** Conditional event histories and tilted generators are two representations of one marked physical process.
- **Source pointers:** Anchor [IV A, “Quantum jumps,” p. 24, Eqs. (113)–(120)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=24). Project: [tilted generator](../science/counting_statistics.md#5-tilted-generator-and-the-renewal-equation).

### M10 — Stationarity and the long-time eigenvalue

- **Central question:** Which spectral information determines the long-time current and its noise?
- **Understanding target:** Relate the derivatives of the dominant tilted eigenvalue to the first two count cumulants. Distinguish the ordinary inverse of a stable killed generator from solving an equation for a trace-preserving generator with a stationary zero eigenvalue; recognize the needed stationarity and relaxation assumptions.
- **Dependencies and story role:** Uses M04 and M09. Connects finite conditional dynamics to long-time statistics while making the mathematical domains explicit.
- **Conceptual connection:** Waiting-time inverses and stationary response methods act on related generators but are not interchangeable inverses.
- **Source pointers:** Anchor [IV D, “Cumulant generating function,” p. 27, Eqs. (131)–(135)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=27), and [V A, auxiliary-equation method, p. 29](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=29). Project: [stationary state](../science/counting_statistics.md#4-the-stationary-state-and-its-positivity).

### M11 — Thermal pairing needs an energy reference

- **Central question:** What makes a forward/reverse jump ratio a thermal statement?
- **Understanding target:** Connect paired events, an assigned energy exchange and a reservoir temperature to the entropy carried by a jump. Distinguish an algebraic adjoint pairing from a thermal realization with respect to a specified Hamiltonian, and identify the role of energy degeneracy in coherent preparation.
- **Dependencies and story role:** Uses M01–M02 and M06. Adds the physical resource interpretation to the counting framework before its synthesis.
- **Conceptual connection:** The same oriented events can carry information about time and transfer heat, but the latter interpretation requires additional physical structure.
- **Source pointers:** Anchor [VI E.1, “Fluctuation theorems,” pp. 48–49, especially local detailed balance in Eq. (338)](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=49). Project: [thermal channels and bare Hamiltonian](../science/thermodynamics.md#1-the-generator-and-its-thermal-channels). The project's clustered realization is an additional ingredient.

### M12 — Phase synthesis: one clock, two statistical descriptions

- **Central question:** How do jump trajectories, renewal intervals and tilted counting statistics describe the same complete-reset clock?
- **Understanding target:** Connect state preparation, conditional survival, cycle completion, output marks and stationary noise in one account. Explain where ordinary renewal formulas suffice, where signed rewards require more information, and how the chosen current becomes a calibrated time estimate with a separate thermal interpretation.
- **Dependencies and story role:** Integrates M01–M11. Closes the background phase by assembling its local objects into the framework used by the conversion theorem.
- **Conceptual connection:** A complete physical model must align its generator, record, statistical assumptions and resource interpretation before different calculation methods can be compared.
- **Source pointers:** Anchor [VI B.2, p. 43](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43), and [IV D, p. 27](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=27). Project: [model](../science/model.md), [counting-statistics account](../science/counting_statistics.md), [physical interpretation](../science/interpretation.md).

## Phase II — Narrative/innovation

### M13 — Retaining the physical reset stage

- **Central question:** What changes when preparation of the next core state becomes part of the clock's dynamics?
- **Understanding target:** Explain the serial capture–heating–release path through $`m,e`$, including its reverse transitions. Identify why a positive capture regenerates the enlarged device even though later negative captures can prepare different core states.
- **Dependencies and story role:** Uses M05–M06 and M12. Begins the project narrative with the retained mechanism and its exact block boundary.
- **Conceptual connection:** Regeneration survives enlargement, allowing an existing thermal bridge architecture to support a new finite-rate quantitative analysis.
- **Source pointers:** Anchor [VI B.2, p. 43, reset criterion](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43). Project: [enlarged clock](../science/model.md#2-the-enlarged-clock), [cycle](../science/interpretation.md#the-cycle), [closest architectural antecedent](../references/RELATED_WORK.md#the-closest-architecture-meier-et-al-2025).

### M14 — Charging the enlarged device

- **Central question:** Which quantity prevents reset channels from becoming a hidden unlimited rate resource?
- **Understanding target:** Explain the three blocks of the summed jump effect and why reverse capture has total rate $`z\mathrm{Tr}Q`$ from $`m`$. Distinguish the two added system states from the number of engineered bath channels.
- **Dependencies and story role:** Uses M02 and M13. Establishes the local resource account before any performance comparison.
- **Conceptual connection:** Aggregating an output does not remove the activity of its microscopic channels; the full rate constraint must survive the conversion.
- **Source pointers:** Anchor [II C, pp. 7–9, jump probabilities](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=7). Project: [complete activity sum](../science/model.md#count-the-complete-device-activity), [rates, channels and state count](../science/thermodynamics.md#3-rates-channels-and-state-count).

### M15 — The reference reset has duration and noise

- **Central question:** What does the reset cost before cold reverse events are introduced?
- **Understanding target:** Interpret the two-state absorption process and the independent sum $`T_0=R_h+X`$. Explain the hot backtracking contribution to the mean and variance, and why the comparison removes cold reverse events while keeping $`h>0`$ fixed.
- **Dependencies and story role:** Uses M04–M05 and M13. Builds an exactly solvable physical reference instead of replacing the reset by an instantaneous map.
- **Conceptual connection:** A finite reset can be compatible with a precise clock if its variance fits the core's error allowance; its mean alone cannot decide this.
- **Source pointers:** Anchor [VI A, p. 40, waiting-time moments](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=40). Project: [exact reference reset](../science/finite_rate_recycling.md#2-the-exact-reference-reset), [fixed comparison](../science/model.md#5-a-fixed-comparison-when-parameters-depend-on-dimension).

### M16 — Controlling every possible return state

- **Central question:** Why is the clean mean from $`\psi`$ insufficient to control reverse-event damage?
- **Understanding target:** Explain why reverse capture can inject a different core state and why $`B_C`$ bounds absorption from every input. Connect the reset residence time to the enlarged reference bound $`B=B_C+r_h`$, including the possibility of rare long excursions.
- **Dependencies and story role:** Uses M04, M13 and M15. Identifies the load-bearing input to the conversion theorem.
- **Conceptual connection:** A robust conversion needs control over states reached by the added dynamics, not only over the clean clock's intended initial preparation.
- **Source pointers:** Anchor [VI A, pp. 39–40, initial-state dependence and survival](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=39). Project: [input survival bound](../science/model.md#1-the-input-clock), [reference inverse](../science/finite_rate_recycling.md#reference-inverse).

### M17 — Stability before perturbative inversion

- **Central question:** Why must absorption be established before expanding the perturbed inverse?
- **Understanding target:** Explain how the positive mean-survival operator controls the perturbed killed evolution when $`\delta B`$ is small. Distinguish a proved decay estimate from assuming that a formal inverse automatically represents a terminating physical waiting process.
- **Dependencies and story role:** Uses M14–M16. Supplies the justification on which the subsequent resolvent and moment bounds depend.
- **Conceptual connection:** The perturbation norm and the longest controlled survival scale must be compared before small reverse rates can be called harmless.
- **Source pointers:** Anchor [VI A, p. 40, absorption and the killed inverse](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=40). Project: [perturbation norm](../science/finite_rate_recycling.md#perturbation-norm), [stability before inversion](../science/finite_rate_recycling.md#4-stability-before-inversion). The quantitative stability argument is supplied by the project.

### M18 — The joint duration–reverse-count law

- **Central question:** What information is lost if a block is described only by its completion time?
- **Understanding target:** Interpret the joint transform $`\mathbb E[e^{-sT}u^M]`$ and why reverse-capture weights alter recycling terms inside the killed dynamics. Identify the duration, reverse-count, factorial and mixed moments needed to recover the signed record.
- **Dependencies and story role:** Uses M06, M09 and M17. Extends first-passage reasoning to the actual marked block process.
- **Conceptual connection:** A noisy reset changes both the time taken and the reward accumulated during that time; the same transform retains their correlation.
- **Source pointers:** Anchor [IV A, p. 24, weighted recycling](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=24), and [VI B, pp. 41–42, path probabilities](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=41). Project: [joint transform](../science/counting_statistics.md#2-the-joint-transform-of-duration-and-reverse-count).

### M19 — Signed noise from correlated block rewards

- **Central question:** How do correlations between a block's length and its reverse events enter timing precision?
- **Understanding target:** Explain $`Y=1-M`$, $`j=\mathbb EY/\mathbb ET`$ and the centered reward $`Y-jT`$. Identify why the mixed moment $`\mathbb E[TM]`$ is indispensable in the signed Fano factor and why positive-capture interval variance alone describes a different observable.
- **Dependencies and story role:** Uses M07 and M18. Converts the joint block law into the performance quantity controlled by the theorem.
- **Conceptual connection:** Renewal of blocks permits correlated rewards within each block; it does not imply an ordinary renewal law for the signed event count.
- **Source pointers:** Anchor [VI B.2, p. 43, ordinary renewal noise as the special case](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43). Project: [current and diffusion from block rewards](../science/counting_statistics.md#3-current-and-diffusion-from-block-rewards).

### M20 — From regeneration to stationary counting statistics

- **Central question:** Why does the block calculation describe the long-time output of the complete generator?
- **Understanding target:** Interpret the stationary state $`\rho_{\rm ss}=\mathcal R_z(P_m)/\mu_z`$ as normalized cycle occupation. Connect the renewal equation for the tilted eigenvalue to the current and noise, retaining the conditions that give faithfulness and relaxation when $`Q>0`$.
- **Dependencies and story role:** Uses M10 and M17–M19. Joins the cycle analysis to the global stationary process without assuming a dimension-independent stationary gap.
- **Conceptual connection:** Regeneration provides both a stationary-state construction and a direct route to the same cumulants obtained from full counting statistics.
- **Source pointers:** Anchor [VI B.1, “Stationarity,” p. 42](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=42), and [IV D, p. 27](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=27). Project: [stationary state](../science/counting_statistics.md#4-the-stationary-state-and-its-positivity), [tilted renewal equation](../science/counting_statistics.md#5-tilted-generator-and-the-renewal-equation).

### M21 — The quantitative finite-rate conversion

- **Central question:** Which finite conditions make the reset-induced precision change controllable?
- **Understanding target:** Relate the four theorem gates to stability, mean control, positive net reward and the reference second moment. Explain how bounds on duration and reward moments yield $`F\leq F_0+\text{controlled error}`$ and a current of order $`1/\mu_0`$, including a finite choice of $`z`$ for a prescribed additive error.
- **Dependencies and story role:** Uses M14–M20. Integrates the local proof ingredients into the conversion theorem before a particular core family is selected.
- **Conceptual connection:** The result is quantitative in the all-input inverse. Polynomial control of that inverse supports inverse-polynomial reverse suppression; eventual absorption alone does not.
- **Source pointers:** Anchor [V A, p. 29, noise from a generator equation](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=29). Project: [finite conditions and conclusion](../science/finite_rate_recycling.md#1-the-finite-conditions-and-conclusion), [precision comparison](../science/finite_rate_recycling.md#6-signed-precision-comparison), [prescribed-error choice](../science/finite_rate_recycling.md#7-an-explicit-choice-for-a-prescribed-error). The bound itself is project-specific.

### M22 — Heat balance through the retained interface

- **Central question:** How can every failed excursion be included while entropy per net cycle remains simple?
- **Understanding target:** Explain the auxiliary occupation balances linking capture, heating and release counts. Identify the bounded endpoint correction in $`S_{\rm env}=\Sigma N+\text{endpoint terms}`$ and the resulting stationary affinity $`\Sigma=\log(h/z^2)`$ without deleting reverse events or auxiliary states.
- **Dependencies and story role:** Uses M11, M13 and M19. Connects the controlled signed record to the physical thermal cost.
- **Conceptual connection:** Conservation relates different event currents globally, so repeated backtracking contributes through signed heat and endpoints rather than an omitted waiting-time branch.
- **Source pointers:** Anchor [VI C.1, pp. 43–45, multiple currents](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=43), and [VI E.1, pp. 48–49](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=48). Project: [exact entropy telescoping](../science/thermodynamics.md#2-exact-entropy-telescoping-before-eliminating-any-state).

### M23 — The thermal model and its microscopic domain

- **Central question:** Under what interpretation can static thermal channels prepare the coherent core state?
- **Understanding target:** Distinguish the bare-degenerate energy operator from the active core Hamiltonian and its small splitting in the clustered weak-coupling construction. Identify static channel engineering and Lamb-shift tuning as resources, and explain why fixed-dimension finite-time convergence does not itself establish infinite-time counting convergence at fixed coupling.
- **Dependencies and story role:** Uses M11, M20 and M22. Gives the finite-generator theorem its justified physical domain before taking a growing-family limit.
- **Conceptual connection:** An effective thermal generator can be exact within its model while its microscopic realization has a particular order of limits.
- **Source pointers:** Anchor [II A, p. 4, master-equation setting](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=4), and [VI E.1, p. 49, thermal assumptions](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=49). Project: [static weak-coupling foundation](../science/thermodynamics.md#5-static-weak-coupling-foundation), [limit order](../science/thermodynamics.md#order-of-limits-and-counting-scope). The clustered construction is an additional primary-source dependency.

### M24 — The inherited coherent core meets the input contract

- **Central question:** What must be checked before a dimension-precision theorem can be used by this conversion?
- **Understanding target:** Connect the quasiideal source parameters and common rescaling to bounded active Hamiltonian, summed capture effect, actual mean $`\Theta(d/g)`$ and small interval variance. Explain how the positive floor $`Q_d\geq gd^{-3}I`$ supplies $`B_C\leq d^3/g`$, and why the mean requires control of rare tails.
- **Dependencies and story role:** Uses M04, M08, M16 and M21. Supplies an explicit admissible family rather than treating a clean accuracy exponent as a sufficient input by itself.
- **Conceptual connection:** Source transfer preserves the physical timescale and all-input stability information needed by the new theorem.
- **Source pointers:** Anchor [VI A, p. 40, survival and moments](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=40). Project: [clean input lemma and reconstruction](../science/quasiideal_application.md#1-clean-input-lemma), [equation correspondence](../science/quasiideal_application.md#equation-correspondence), [Woods2022 primary reference](../references/REFERENCES.md#woods2022). The quasiideal accuracy theorem is inherited, not supplied by the anchor.

### M25 — Reverse suppression and dimension-dependent sensitivity

- **Central question:** Why is “a small reverse rate” not a sufficient asymptotic argument?
- **Understanding target:** Explain how the powers of $`B`$, $`a`$ and the mean interval amplify a reverse perturbation as dimension grows. Track why $`z_d=d^{-11}`$ makes the leading added inverse-precision error $`O(d^{-3})`$ while preserving the mean-current scale, with the hot ratio fixed during each comparison.
- **Dependencies and story role:** Uses M15–M17, M21 and M24. Converts the generic finite estimate into a controlled scaling statement.
- **Conceptual connection:** A shrinking intrinsic noise level requires a correspondingly quantitative perturbation bound; continuity at each fixed dimension would not establish the growing-family result.
- **Source pointers:** Anchor [IV D, p. 27, long-time cumulants](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=27), as counting context. Project: [reset delay and perturbation gates](../science/quasiideal_application.md#reset-delay-and-perturbation-gates), [explicit finite choice](../science/finite_rate_recycling.md#7-an-explicit-choice-for-a-prescribed-error).

### M26 — Fixed temperatures require a quantified tradeoff

- **Central question:** Which thermal resources change when the dimension grows while both bath temperatures stay fixed?
- **Understanding target:** Connect $`q_d\propto\log d`$, $`h_d=d^{-22\theta}`$ and the slower reset variance to the target exponent loss. State the quantifier correctly: for each fixed $`0<\eta<1`$, choose a dimension-independent $`0<\theta\leq\eta/44`$; one fixed positive ratio does not give exponent $`2-o(1)`$ by this bound.
- **Dependencies and story role:** Uses M15 and M22–M25. Combines the timing estimate with an explicit thermal-resource family.
- **Conceptual connection:** Logarithmic bias can be paid through changing gaps or temperatures, and a fixed-temperature choice also changes the pump timescale.
- **Source pointers:** Anchor [VI E.1, p. 49, rate ratios and entropy weights](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=49). Project: [two resource choices](../science/thermodynamics.md#4-two-distinct-ways-to-obtain-logarithmic-entropy), [fixed-temperature application](../science/quasiideal_application.md#2-application-with-two-fixed-temperatures).

### M27 — A classical benchmark with complete activity accounting

- **Central question:** Why can a finite classical Markov clock not remove timing diffusion by adding more reset or auxiliary states under the same rate cap?
- **Understanding target:** Interpret uniformization as a Poisson opportunity process independent of an embedded marked chain. Explain how conditional variance gives $`D_{{\rm time},C}\geq1/(2g)`$ even with correlated marks, hidden transitions and physical self-events, and identify the matched-current condition for a precision-only comparison.
- **Dependencies and story role:** Uses M02, M06, M08 and M14. Establishes the operational benchmark against which the compiled family is compared.
- **Conceptual connection:** A global event-rate cap limits the random opportunities available to every classical component, including its reset circuitry.
- **Source pointers:** Anchor [VI F, “Thermodynamic and kinetic uncertainty relations,” pp. 51–53](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=51), as uncertainty-relation context. Project: [complete classical model](../science/classical_comparison.md#1-device-and-readout-convention), [uniformization proof](../science/classical_comparison.md#2-uniformization-proof). The project supplies the specific proof used here.

### M28 — The simultaneous advantage

- **Central question:** What follows when timing, thermodynamics and the matched rate budget are imposed together?
- **Understanding target:** Explain the simultaneous laws $`P_d\geq c_\eta d^{2-\eta}`$, $`j_d=\Theta_\eta(g/d)`$, $`gD_{{\rm time},d}=O_\eta(d^{-1+\eta})`$ and $`\Sigma_d=O(\log d)`$. Identify why decreasing time diffusion establishes a useful advantage beyond regular ticks, with every modeled reset and reverse event included.
- **Dependencies and story role:** Uses M08 and M21–M27. Joins the separate controls into the main scientific consequence.
- **Conceptual connection:** The finite-rate conversion preserves the combination of precision and speed that matters for time estimation while assigning an explicit stationary thermal cost.
- **Source pointers:** Anchor [III C, pp. 19–20, count noise](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=19), and [VI F, pp. 51–53](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=51). Project: [simultaneous statement](../science/quasiideal_application.md#simultaneous-performance-and-resource-statement), [classical comparison](../science/classical_comparison.md#3-comparison-with-the-compiled-quantum-family).

### M29 — What the finite checks establish

- **Central question:** Which possible errors can finite computations detect, and which claims require analytical or microscopic arguments?
- **Understanding target:** Distinguish agreement of regenerative moments, stationary response and tilted eigenvalue derivatives from proof of an asymptotic exponent. Explain the general-$`h`$ reset-moment check and the thermal stall control $`h=z^2`$, where currents vanish and no Fano factor is formed by dividing by the current.
- **Dependencies and story role:** Uses M10, M15, M19–M20, M22 and M28. Connects each result to the kind of evidence that actually supports it.
- **Conceptual connection:** Independent calculations test signs, factors, correlations and thermal conventions; the source theorem and finite-rate estimates establish the growing-family law.
- **Source pointers:** Anchor [V A–C, pp. 29–31, auxiliary equations and vectorization](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=29). Project: [independent finite calculations](../verification/README.md#independent-calculations), [claim-to-evidence account](../verification/README.md#what-establishes-each-claim), [verification program](../verification/check_clock.py).

### M30 — Phase synthesis: the closed reset gap and its boundary

- **Central question:** What exactly has been added to quantum-clock advantage, and under which resource and limit assumptions does it hold?
- **Understanding target:** Give one connected account of the inherited quasiideal core and thermal bridge, the new quantitative control of the retained finite-rate interface, the signed-current observable and the simultaneous advantage. Keep the target-dependent temperature ratio, growing bare gaps, static engineered channels and ordered microscopic limit visible. Identify calibration, detector operation, record erasure and reservoir maintenance as separate costs from the cyclic reset accounted for here.
- **Dependencies and story role:** Integrates M13–M29 using the framework synthesized in M12. Closes the narrative phase with the contribution, its operational meaning and its domain rather than another isolated ingredient.
- **Conceptual connection:** A component-level resource gap is closed by aligning the physical model, proof, source transfer, comparison and limitations; it does not require claiming a new thermal architecture or a complete apparatus cost theorem.
- **Source pointers:** Anchor [VI A–B, pp. 39–43](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=39), and [IV D, p. 27](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf#page=27), for the integrated statistical framework. Project: [scientific account](../science/README.md), [physical meaning and boundary](../science/interpretation.md#the-comparison-and-its-boundary), [precise added statement](../references/RELATED_WORK.md#precise-added-statement), [thermal scope](../science/thermodynamics.md#6-what-the-entropy-quantity-covers).
