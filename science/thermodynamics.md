# Thermal realization and resource account

The recycling device has an exact entropy balance within the specified thermal GKLS model. Its timing theorem concerns that finite-rate generator. A static, clustered weak-coupling construction supplies a microscopic foundation in an ordered limit; it does not by itself establish convergence of infinite-time counting cumulants at fixed microscopic coupling. These two statements are kept separate below.

Throughout, $`k_B=\hbar=1`$. The cold reverse ratio is $`z\in(0,1)`$, the hot upward/downward rate ratio is $`h\in(0,1)`$, and $`g>0`$ sets the active dynamical scale. The case $`z=0`$ is an analytical comparison process, not a finite-temperature implementation.

## 1. The generator and its thermal channels

Let $`\mathcal H_C`$ be the $`d`$-dimensional clock core, with Hamiltonian $`H_C`$, normalized reset vector $`|\psi\rangle`$, and positive effect

```math
Q=\sum_{k=1}^{K}|v_k\rangle\langle v_k|\le g I_C,
\qquad a=\operatorname{Tr}Q.
```

Add orthogonal states $`|m\rangle,|e\rangle`$. Write $`P_m=|m\rangle\langle m|`$, $`P_e=|e\rangle\langle e|`$, and extend $`H_C`$ by zero on the auxiliary states. The jump pairs are

| Transition | Forward jump | Reverse jump | Forward environment entropy |
|---|---|---|---|
| Capture, core to $`m`$ | $`A_k=\lvert m\rangle\langle v_k\rvert`$ | $`\sqrt z\,A_k^\dagger`$ | $`\ell=\log(1/z)`$ |
| Heating, $`m`$ to $`e`$ | $`\sqrt{gh}\,\lvert e\rangle\langle m\rvert`$ | $`\sqrt g\,\lvert m\rangle\langle e\rvert`$ | $`-b=-\log(1/h)`$ |
| Release, $`e`$ to core | $`\sqrt g\,\lvert\psi\rangle\langle e\rvert`$ | $`\sqrt{zg}\,\lvert e\rangle\langle\psi\rvert`$ | $`\ell`$ |

To give these ratios a thermal meaning, choose a bare energy gap $`q>0`$ and the reference Hamiltonian

```math
H_0=q\Pi_C+2qP_e,
\qquad
z=e^{-\beta_C q},
\qquad
h=e^{-2\beta_H q}.
```

Here $`m`$ has energy zero, all core states have bare energy $`q`$, and $`e`$ has energy $`2q`$. Adding a common scalar to $`H_0`$ is immaterial. The commutators are

```math
[H_0,A_k]=-qA_k,
\qquad
[H_0,|\psi\rangle\langle e|]=-q|\psi\rangle\langle e|,
\qquad
[H_0,|e\rangle\langle m|]=2q|e\rangle\langle m|.
```

Consequently, the two downward cold transitions release energy $`q`$ each, and the hot upward transition absorbs energy $`2q`$. A hot-to-cold device has $`0<\beta_H<\beta_C`$, equivalently $`z^2<h<1`$.

The capture operators need not be Bohr eigenoperators of the fully split core Hamiltonian. Their eigenoperator property above is with respect to $`H_0`$. Merely writing adjoint jump pairs with scalar rate ratios would not justify a thermal interpretation relative to an arbitrary full Hamiltonian.

Direct substitution also shows that each bath dissipator separately preserves its reference Gibbs state:

```math
\mathcal D_r\!\left(\frac{e^{-\beta_rH_0}}{\operatorname{Tr}e^{-\beta_rH_0}}\right)=0,
\qquad r\in\{C,H\}.
```

The core Hamiltonian commutes with $`H_0`$ and hence with both reference Gibbs states. This is the thermal structure of the effective model; the two baths need not share a stationary state.

## 2. Exact entropy telescoping before eliminating any state

Let $`N_1(t)`$, $`N_H(t)`$, and $`N_2(t)`$ denote signed capture, heating, and release counts. A forward event adds one and its reverse subtracts one. All capture channels contribute to the same count $`N_1`$. Let $`n_m,n_e\in\{0,1\}`$ denote auxiliary occupations along a jump trajectory, and $`\Delta n_x=n_x(t)-n_x(0)`$.

For a trajectory initialized in a definite core/auxiliary sector, conservation of occupation gives

```math
\Delta n_m=N_1-N_H,
\qquad
\Delta n_e=N_H-N_2.
```

These identities also give the corresponding ensemble balances for mixed preparations. The coherent core evolution changes neither auxiliary occupation. The environment entropy is therefore

```math
\begin{aligned}
S_{\rm env}(t)
 &=\beta_Cq\,[N_1(t)+N_2(t)]-2\beta_Hq\,N_H(t)\\
 &=\ell[N_1(t)+N_2(t)]-bN_H(t)\\
 &=\Sigma N_1(t)+(b-\ell)\Delta n_m-\ell\Delta n_e,\\
\Sigma&=2\ell-b=2q(\beta_C-\beta_H)
       =\log\!\frac{h}{z^2}.
\end{aligned}
```

This is an exact identity for arbitrary positive $`z,h`$ in the specified generator. It does not require renewal statistics, negligible reverse events, an instantaneous reset, or elimination of $`m,e`$.

At each fixed $`d,z,h`$, the correction is a bounded endpoint quantity. Hence, if $`j=\lim_{t\to\infty}\mathbb E N_1(t)/t>0`$,

```math
\lim_{t\to\infty}\frac{\mathbb E S_{\rm env}(t)}t=\Sigma j,
\qquad
\lim_{t\to\infty}
\frac{\mathbb E S_{\rm env}(t)}{\mathbb E N_1(t)}=\Sigma.
```

The finite-dimensional system entropy changes by at most $`\log(d+2)`$. It therefore does not alter the stationary entropy production per net tick. Counts on the three edges differ by bounded occupations and have the same stationary mean and diffusion coefficient whenever those limits exist. The ordering “long time at fixed device, then growing dimension” matters because the entropy endpoint coefficients grow with $`\log d`$ in the families below.

The energy identity is equally direct:

```math
2qN_H-q(N_1+N_2)=\Delta H_0=q(\Delta n_e-\Delta n_m).
```

Thus each stationary net cycle transfers $`2q`$ from the hot reservoir to the cold reservoir. The entropy formula is a heat balance for the entire retained interface, not an assignment of the total cycle entropy to a single microscopic capture photon.

The serial heat accounting has a direct antecedent in the [pinned entropy-limit notes](../references/REFERENCES.md#clock-entropy). The contribution here is the accompanying finite-rate timing bound, not this conservation identity alone.

## 3. Rates, channels, and state count

The Hilbert-space dimension of the clock plus recycling states is $`d+2`$. The complete summed jump effect is

```math
\sum_\alpha L_\alpha^\dagger L_\alpha
 = Q+zg|\psi\rangle\langle\psi|
   +(gh+za)P_m+2gP_e.
```

In particular, the reverse-capture escape rate from $`m`$ is $`za`$, not $`zg`$. Since $`a\le dg`$, the sufficient conditions $`z\le1`$ and $`gh+za\le2g`$ give

```math
\sum_\alpha L_\alpha^\dagger L_\alpha\le2gI_{Cme}.
```

The applications $`z=d^{-11}`$, $`h\le1`$ satisfy this bound. The classical rate comparison must use the same complete budget, including the auxiliaries.

The number of thermal channels is a separate resource from system dimension. One may replace any redundant capture representation by a spectral decomposition of $`Q`$, retaining the same dissipator and aggregated capture count, so $`K\le d`$ suffices. A simple realization uses $`K`$ independent cold capture channels, one independent cold release channel, and one hot channel. “Two baths” means two temperatures; it does not mean only two independent coupling operators. Independence, or a suitable diagonal bath correlation matrix, prevents unwanted cross terms between the equal-frequency capture and release transitions. In the full-rank application, $`K=d`$.

The operators selecting $`|v_k\rangle`$ and $`|\psi\rangle`$ are static. A thermal release can prepare coherence within the degenerate $`H_0`$ core eigenspace without a periodically driven phase reference. Engineering these coupling vectors, suppressing unwanted channels, and compensating energy shifts remain physical specifications of the device.

## 4. Two distinct ways to obtain logarithmic entropy

The timing construction uses $`z_d=d^{-11}`$. Fix an exponent loss $`\eta\in(0,1)`$ in the nearquadratic precision statement.

### Fixed bare gaps and fixed return-time scale

Choose $`q=q_0>0`$ and $`h=1/2`$. Then

```math
\beta_C(d)=\frac{11\log d}{q_0},
\qquad
\beta_H=\frac{\log2}{2q_0},
\qquad
\Sigma_d=22\log d-\log2.
```

The bare energy width is $`2q_0`$, and the return stage has a dimension-independent time scale. The cold temperature decreases as $`1/\log d`$; the temperature ratio grows as $`\log d`$. One cannot claim both fixed temperatures and fixed gaps for this choice. Equivalently, holding the cold temperature fixed with $`h=1/2`$ requires growing $`q`$ and hot temperature.

### Fixed temperatures and a slower return stage

Choose fixed $`\beta_C>\beta_H>0`$ with $`\theta=\beta_H/\beta_C`$, and set

```math
q_d=\frac{11\log d}{\beta_C},
\qquad
h_d=z_d^{2\theta}=d^{-22\theta},
\qquad
\Sigma_d=22(1-\theta)\log d.
```

The temperatures are now independent of dimension, but the bare energy width is $`2q_d=O(\log d)`$ and the hot upward rate is $`gh_d`$. For the reference process at $`z=0`$ with this same $`h_d`$, the auxiliary return time $`R`$ obeys the exact formulas

```math
\mathbb E R=\frac{2/h_d+1}{g},
\qquad
\operatorname{Var}R=\frac{4/h_d^2+2/h_d+1}{g^2}.
```

If $`\theta\le\eta/44`$, then $`\operatorname{Var}R=O(d^\eta/g^2)`$ and $`\mathbb ER=O(d^{\eta/2}/g)`$. The return time is therefore subleading to the core mean $`\Theta(d/g)`$, and its variance fits within the allowed nearquadratic precision loss. The [finite-rate timing theorem](finite_rate_recycling.md) compares the physical generator to the reference at the same $`h_d`$; it does not set the hot ratio to a dimension-independent value during this comparison.

The quantifier is: for every fixed $`\eta>0`$, choose a sufficiently large but fixed temperature ratio, then take $`d\to\infty`$. This argument does not show that a single prescribed finite temperature ratio achieves every exponent arbitrarily close to two.

| Resource | Fixed-gap choice | Fixed-temperature choice |
|---|---|---|
| System dimension | $`d+2`$ | $`d+2`$ |
| Complete jump effect | At most $`2gI`$ | At most $`2gI`$ |
| Active core bandwidth | $`O(g)`$ | $`O(g)`$ |
| Bare energy width | $`2q_0`$ | $`22\log d/\beta_C`$ |
| Reservoir temperatures | $`T_C=\Theta(1/\log d)`$, fixed $`T_H`$ | Both fixed; $`\beta_H/\beta_C\le\eta/44`$ |
| Hot upward rate | $`g/2`$ | $`g d^{-22\theta}`$ |
| Thermal coupling channels | At most $`d+2`$ | At most $`d+2`$ |
| Stationary entropy per net tick | $`22\log d-\log2`$ | $`22(1-\theta)\log d`$ |

Adding $`H_0`$ to the specified effective Hamiltonian does not change the core/auxiliary-sector counting statistics. In the fixed-gap choice its specified width is bounded by the bare width plus the active core width. This is a statement about the effective generator being specified; it is not a dimension-uniform bandwidth theorem for every microscopic Hamiltonian and its Lamb-shift counterterms.

## 5. Static weak-coupling foundation

[Trushechkin's unified weak-coupling construction](../references/REFERENCES.md#trushechkin2021) allows

```math
H_S(\lambda)=H_0+\lambda^2\delta H,
\qquad [H_0,\delta H]=0,
```

with thermal dissipation resolved by the separated frequencies of $`H_0`$ while retaining coherent dynamics within a nearly degenerate cluster. This gives an appropriate framework for the present device.

For each fixed dimension, take static Hermitian system-bath couplings proportional to $`A_k+A_k^\dagger`$, $`|\psi\rangle\langle e|+|e\rangle\langle\psi|`$, and $`|e\rangle\langle m|+|m\rangle\langle e|`$, with the channel independence specified above. Choose their spectra at $`q`$ and $`2q`$ to produce the desired downward rates; the thermal KMS relations then fix the upward ratios. In the interaction picture of $`H_0`$ and slow time $`\tau=\lambda^2t`$, choose $`\delta H`$ so that the core Hamiltonian plus the Lamb shift is the desired $`H_C`$. All couplings and counterterms are time independent.

This application assumes ordinary weak-coupling hypotheses: appropriate decay of reservoir correlations, separated bare frequency clusters, and bath spectra sufficiently regular over the shrinking intracluster splittings. It is an existence construction using engineered channels, not a claim that a generic thermal environment realizes arbitrary $`Q`$ and $`|\psi\rangle`$.

### Lamb shifts are part of the implementation

With bounded spectral coefficients, the core contribution from independent capture channels is controlled by $`Q`$ and can be $`O(g)`$. The auxiliary scalar contribution can instead contain $`\sum_k\langle v_k|v_k\rangle=a=O(dg)`$ in slow-time units. Cancelling or absorbing that scalar shift into the specified auxiliary energies is an explicit static tuning assumption. At every fixed $`d`$, its physical size is $`O(\lambda^2dg)`$ and can be small relative to the bare gaps in the ordered limit. No uniform microscopic counterterm bound is inferred from the effective activity bound.

### Order of limits and counting scope

Trushechkin's theorem gives reduced-state convergence uniformly over each fixed finite interval $`0\le\lambda^2t\le\tau_1`$. Its thermodynamic accounting uses $`H_0`$ at the order retained by the master equation; replacing it by the fully split Hamiltonian changes terms beyond that order. [Gerry and Segal](../references/REFERENCES.md#gerry2023) develop fluctuation statistics for the unified generator. Neither statement alone is a uniform microscopic theorem for all long-time count cumulants of this growing family.

The established sequence here is

```math
\text{fixed }d\text{ weak-coupling limit}
\quad\longrightarrow\quad
\text{long-time statistics of the limiting GKLS device}
\quad\longrightarrow\quad
d\to\infty.
```

A fixed-coupling microscopic theorem would additionally need error control for the tilted dynamics or the relevant current cumulants, with its dimension dependence. That extension is not used in the timing result. The entropy telescoping formula is exact within the limiting thermal generator and needs no assumption of a same-protocol fluctuation symmetry under time reversal of complex coupling phases.

Common weak-coupling slowing is visible in the units. For physical active rate $`g_{\rm phys}=\lambda^2g`$, a slow-time timing-diffusion coefficient $`D_{\rm time}`$ becomes $`D_{\rm time,phys}=D_{\rm time}/\lambda^2`$. Thus

```math
g_{\rm phys}D_{\rm time,phys}=gD_{\rm time}.
```

This preserves the normalized comparison with a classical device under the same physical rate budget. It does not fix an absolute operating speed as $`d`$ and the microscopic approximation requirements vary.

## 6. What the entropy quantity covers

$`\Sigma`$ counts the bath entropy produced by stationary operation of the core and the complete retained recycling interface. It includes reverse capture, reverse release, and repeated hot excursions. It excludes macroscopic amplification, imperfect photon detection, storage or erasure of the external tick record, calibration of an initially unknown generator, and preparation or maintenance of the reservoirs themselves. Those resources are distinct from cyclic reset; [detector and readout studies](../references/RELATED_WORK.md#readout-and-recent-clock-proposals) illustrate why they cannot be inferred from this entropy balance.
