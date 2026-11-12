# Model and charged resources

[Overview](../README.md) · [Finite-rate recycling](finite_rate_recycling.md) · [Counting statistics](counting_statistics.md) · [Thermodynamics](thermodynamics.md) · [Quasiideal application](quasiideal_application.md) · [Classical comparison](classical_comparison.md)

The object of study is a finite-dimensional clock whose ideal tick prepares one fixed pure state. We replace that instantaneous preparation by two auxiliary levels and a serial sequence of thermal jump pairs. The enlarged generator is time independent, includes every reverse transition, and retains the reset delay in its counting statistics.

The result concerns an explicitly specified thermal GKLS model. Its bath interpretation and the distinction between bare and dressed energy are given in [Thermodynamics](thermodynamics.md). A uniform finite-coupling approximation by microscopic reservoirs is a separate requirement.

## 1. The input clock

Let $`\mathcal H_C`$ have dimension $`d`$, let $`H=H^\dagger`$ act on this space, and let $`|\psi\rangle`$ be normalized. The ideal counted jumps are

```math
J_k=|\psi\rangle\langle v_k|,
\qquad
Q=\sum_k |v_k\rangle\langle v_k|,
\qquad
0\le Q\le gI_C,
```

where $`g>0`$ is a rate scale. There are no additional uncounted dissipators in the input model. Every ideal tick returns the entire input clock to $`P_\psi=|\psi\rangle\langle\psi|`$, irrespective of its channel label. This complete-reset property makes the ideal waiting times independent and identically distributed.

We use

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
\qquad
\mathcal L_C(\rho)
=-i[H,\rho]+\sum_k\mathcal D[J_k](\rho).
```

Removing only the counted recycling terms gives the core no-tick generator

```math
\mathcal K(\rho)
=-i[H,\rho]-\frac12\{Q,\rho\}.
```

Assume its semigroup is stable and define

```math
\mathcal R_C=(-\mathcal K)^{-1}
=\int_0^\infty e^{t\mathcal K}\,dt,
\qquad
\|\mathcal R_C\|_{1\to1}\le B_C<\infty.
```

All superoperator norms below are induced trace norms. For a completely positive map $`\mathcal A`$,

```math
\|\mathcal A\|_{1\to1}
=\|\mathcal A^\dagger(I)\|_\infty.
```

Consequently, $`B_C`$ bounds the mean time to a tick from every initial core state, including states produced by a reverse transition. Controlling only the mean from $`P_\psi`$ would not provide this guarantee.

A sufficient stability condition is a positive absorption floor:

```math
Q\ge q_{\min}I_C
\quad\Longrightarrow\quad
\|e^{t\mathcal K}\|_{1\to1}\le e^{-q_{\min}t},
\qquad
B_C\le q_{\min}^{-1}.
```

The floor is a lower bound; it need not equal the smallest eigenvalue of $`Q`$.

Let $`X`$ be the first ideal tick time from $`P_\psi`$, and write

```math
\mu=\mathbb E X,
\qquad
\sigma^2=\mathrm{Var}X,
\qquad
\mathbb E X^n
=n!\mathrm{Tr}\!\left[\mathcal R_C^n(P_\psi)\right].
```

In particular, $`\mu\le B_C`$. The recycling theorem does not require a Hamiltonian norm bound, but a comparison at bounded coherent strength must impose one separately. The [quasiideal application](quasiideal_application.md) uses $`\min_c\|H-cI_C\|_\infty\lt g/4`$ in addition to $`Q\le gI_C`$.

## 2. The enlarged clock

Add two orthogonal states $`|m\rangle`$ and $`|e\rangle`$:

```math
\mathcal H=\mathcal H_C\oplus\mathrm{span}\{|m\rangle,|e\rangle\},
\qquad
\dim\mathcal H=d+2.
```

Define $`A_k=|m\rangle\langle v_k|`$. The cold reverse ratio is $`z\in[0,1]`$, and the hot upward-to-downward ratio is $`h\in(0,1]`$. The physical finite-temperature constructions use $`z>0`$ and $`h<1`$; $`z=0`$ is a comparison model.

| Transition | Jump operator | Increment of the counted record |
|---|---|---:|
| Capture from the core | $`A_k`$ | $`+1`$ |
| Reverse capture | $`\sqrt z\,A_k^\dagger`$ | $`-1`$ |
| Hot excitation $`m\to e`$ | $`\sqrt{gh}\,\lvert e\rangle\langle m\rvert`$ | $`0`$ |
| Hot relaxation $`e\to m`$ | $`\sqrt g\,\lvert m\rangle\langle e\rvert`$ | $`0`$ |
| Release $`e\to\psi`$ | $`\sqrt g\,\lvert\psi\rangle\langle e\rvert`$ | $`0`$ |
| Reverse release $`\psi\to e`$ | $`\sqrt{zg}\,\lvert e\rangle\langle\psi\rvert`$ | $`0`$ |

The full generator $`\mathcal L_z^{(h)}`$ consists of the Hamiltonian commutator and the dissipators of all these operators. The coherent core Hamiltonian is extended by zero on the auxiliary space.

One may add the carrier Hamiltonian

```math
H_0
=\omega I_C+(\omega-q)P_m+(\omega+q)P_e,
\qquad q>0,
```

to obtain the physical system Hamiltonian $`H_0+(H\oplus0)`$. It assigns energies to the thermal transitions. Since both Hamiltonians preserve the three sectors and $`H_0`$ is scalar on the core, it does not change their populations or the capture counting statistics. The proof therefore suppresses this carrier term when writing no-tick generators. The cost of its energy gaps is accounted for separately in [Thermodynamics](thermodynamics.md).

### Count the complete device activity

Write $`a=\mathrm{Tr}Q\le dg`$. The sum of the effects of every physical jump is exactly

```math
\sum_\alpha L_\alpha^\dagger L_\alpha
=\bigl(Q+zgP_\psi\bigr)
\oplus(gh+za)P_m
\oplus2gP_e.
```

It follows that

```math
z\le1,
\qquad gh+za\le2g
\quad\Longrightarrow\quad
\sum_\alpha L_\alpha^\dagger L_\alpha\le2gI.
```

This is a bound on the full instantaneous event intensity, not on each channel separately. It includes hot backtracking, both cold reverse families, and the final release. In particular, many capture channels cannot conceal an unbounded total jump rate under this condition.

## 3. Observable record and block boundaries

The observable is the signed capture count

```math
N(t)=N_+(t)-N_-(t).
```

Channel labels $`k`$, hot events and release events need not be supplied to a decoder. They can be used as latent trajectories in the proof. The dynamics does not depend on whether an observer reads the record, and it contains no measurement-conditioned control.

Every positive capture returns the full device to $`P_m`$. Start a block immediately after one positive capture and end it at the next positive capture. If $`T`$ is the block duration and $`M`$ is the number of reverse captures within it, the net block reward is

```math
Y=1-M.
```

Successive $`(T,M)`$ pairs are independent and identically distributed. The final positive capture belongs to the block that it ends. A negative capture can prepare a different core state, but it does not end the block.

This regenerative structure is why reverse events cannot be treated by simply adding their mean rate to the ideal tick rate. Their number is correlated with the duration of the block. [Counting statistics](counting_statistics.md) retains that correlation explicitly.

## 4. Performance conventions

When the net current is positive, define

```math
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}t,
\qquad
D_N=\lim_{t\to\infty}\frac{\mathrm{Var}N(t)}t,
\qquad
F=\frac{D_N}{j},
\qquad
P=\frac1F.
```

There is no factor of two in the definition of $`D_N`$. The elapsed-time estimator based on the count is $`\widehat t=N(t)/j`$, whose long-time diffusion coefficient is

```math
D_{\mathrm{time}}
=\lim_{t\to\infty}\frac{\mathrm{Var}\widehat t}{t}
=\frac{D_N}{j^2}
=\frac Fj.
```

The mean current $`j`$ is assumed known for this estimator. Its calibration, and the dissipation of a detector or finite classical memory used to read the count, are outside the reset conversion theorem.

## 5. A fixed comparison when parameters depend on dimension

The perturbation parameter is $`z`$. Throughout the comparison between $`\mathcal L_z^{(h)}`$ and $`\mathcal L_0^{(h)}`$, the hot ratio $`h`$ is held fixed. Only reverse capture and reverse release are removed in the comparison model.

For a family with $`h_d=z_d^{2\theta}`$, first choose $`h_d`$ and then compare the two generators at that same value:

```math
\mathcal L_{z_d}^{(h_d)}
\quad\hbox{and}\quad
\mathcal L_0^{(h_d)}.
```

Sending $`h`$ to zero together with the comparison parameter would turn off the hot pump. That is a different, non-regenerating reference process and is not used in the proof.
