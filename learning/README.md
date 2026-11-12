# Learning route

[Project overview](../README.md) · [Scientific account](../science/README.md) · [Milestone map](milestones.md)

The scientific question is whether a precise quantum clock can keep its useful timing advantage when each cycle includes a finite thermal reset. Answering it requires following the same device through three descriptions: physical transitions, random durations and signed tick counts, and heat exchanged with the baths.

## Start with the mechanism

The [anchor bridge](anchor_bridge.md) connects those descriptions and includes a complete three-state calculation. It shows why the intervals between positive captures are insufficient to determine the signed current's fluctuations, how reset delay and noise enter, and which additional ingredients yield the quantum advantage.

The single educational anchor is **Landi, Kewming, Mitchison, and Potts, “Current Fluctuations in Open Quantum Systems: Bridging the Gap Between Quantum Continuous Measurements and Full Counting Statistics,” PRX Quantum 5, 020201 (2024)**. The bridge provides the [short section route and notation translation](anchor_bridge.md#1-one-anchor-and-a-short-reading-route), with links to the published article and its full PDF. The primary research sources used for the construction and comparison remain in the [bibliography](../references/REFERENCES.md).

## Follow the 30-milestone map

The [map](milestones.md) states the understanding targets, dependencies, and source pointers for the complete project. Its two phases follow the scientific argument from individual objects to the combined result.

| Phase | Milestones | Role in the story |
|---|---|---|
| Background and preliminaries | M01–M12 | Connect state evolution, jumps, waiting times, signed records, fluctuations, and thermal pairs into one framework |
| Narrative and innovation | M13–M30 | Assemble the retained reset mechanism, quantitative transfer bound, accurate input family, classical comparison, and resource account |

The twelve background milestones build the tools needed to state the problem precisely. The eighteen narrative milestones follow how those tools establish and qualify the result. M12 integrates the statistical descriptions; M30 integrates the contribution, physical resources, and limit order.

## Choose a direct reading route

| Question | Starting point | Continue with |
|---|---|---|
| What operation was idealized, and what replaces it? | [Interpretation](../science/interpretation.md) | [Device and record](../science/model.md) |
| How can a whole cycle carry a random signed reward? | [Bridge, Section 2](anchor_bridge.md#2-the-missing-statistical-step-blocks-carry-signed-rewards) | [Exact counting derivation](../science/counting_statistics.md) |
| What do the formulas produce in a small example? | [Three-state calculation](anchor_bridge.md#4-a-complete-three-state-example) | [Finite verification](../verification/README.md) |
| Which bound preserves precision at finite reset rate? | [Finite-rate theorem](../science/finite_rate_recycling.md) | [Quasiideal application](../science/quasiideal_application.md) |
| Why is this a timing advantage under a matched budget? | [Performance conventions](../science/model.md#4-performance-conventions) | [Classical comparison](../science/classical_comparison.md) |
| Which thermal resources and physical assumptions are charged? | [Thermodynamics](../science/thermodynamics.md) | [Related work and scope](../references/RELATED_WORK.md) |

The anchor supplies the counting-statistics framework. The project's pages supply the finite-rate conversion argument. The accurate quantum input family and the classical comparison have their own research-level source dependencies. Keeping those roles explicit makes it possible to understand the mechanism while retaining a direct route to each load-bearing proof.
