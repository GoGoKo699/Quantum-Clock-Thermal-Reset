# Quasiideal clocks with a finite thermal reset

The [finite-rate compiler](finite_rate_recycling.md) preserves a near-quadratic precision law and a decreasing time-estimation diffusion coefficient for an explicit family of quasiideal clocks. This page reconstructs the clean input, including its summed jump effect, positive absorption floor and actual mean period, before applying the compiler. The quasiideal accuracy theorem is inherited from [Woods, Silva, Pütz, Stupar and Renner, *Quantum Clocks are More Accurate Than Classical Ones*, PRX Quantum 3, 010319 (2022), Appendix F](https://doi.org/10.1103/PRXQuantum.3.010319). The parameter choice and bounded-strength rescaling agree with the [pinned construction in Quantum-Clock-Restart-Limits](https://github.com/GoGoKo699/Quantum-Clock-Restart-Limits/blob/4e275bdc621e7fa250a19c2e29f122499095bdfc/science/quantum_construction.md).

## 1. Clean input lemma

Fix $`g>0`$ and a fixed exponent loss $`0<\varepsilon<1`$. For all sufficiently large even $`d`$, there is a time-independent clock on a $`d`$-dimensional core with Hamiltonian $`H_d`$, pure reset state $`|\psi_d\rangle`$ and jumps $`J_{d,k}=|\psi_d\rangle\langle v_{d,k}|`$, and no uncounted dissipators, such that

```math
\begin{aligned}
\|H_d\|&<g/4,\\
g d^{-3}I\ \leq\ Q_d:=\sum_kJ_{d,k}^{\dagger}J_{d,k}&\leq gI,\\
\frac{2\pi}{3}\frac d g\ \leq\ \mu_d:=\mathbb EX_d&\leq8\pi\frac d g,\\
\frac{\operatorname{Var}X_d}{\mu_d^2}&\leq24d^{-2+\varepsilon},\\
B_{C,d}:=\|(-K_d)^{-1}\|_{1\to1}&\leq\frac{d^3}{g}.
\end{aligned}
```

Here $`X_d`$ is the clean first-tick time from $`|\psi_d\rangle`$, and

```math
K_d(\rho)=-i[H_d,\rho]-\frac12\{Q_d,\rho\}
```

is the no-tick generator. The Hamiltonian is centered on its spectrum. The dimension threshold may depend on $`\varepsilon`$. All later limits keep this loss fixed while taking $`d\to\infty`$.

### Explicit source parameters

The following construction uses the published Appendix F equations before their final renaming of the accuracy parameter. Set

```math
\begin{gathered}
\xi=\varepsilon/5,\qquad
\epsilon_5=\epsilon_8=\xi/16,\qquad
\epsilon_6=2\xi,\qquad
\epsilon_7=\xi/4,\qquad
\epsilon_9=\xi/2,\\
\sigma_d=d^{2\xi},\qquad \delta_{\rm s}=d^{\xi/16},\qquad
\alpha_0=1,\qquad n_0=(d-1)/2,\qquad k_0=0,\\
N_{\rm f}=\left\lceil12/\xi-3\right\rceil,
\qquad \kappa=0.792.
\end{gathered}
```

The source's parameter $`\eta`$ in Eqs. (F243)–(F245) is $`\xi`$ here. The source's $`N,n,\delta,\gamma`$ are denoted $`N_{\rm f},\nu_d,\delta_{\rm s},\gamma_{\rm s}`$ below, to distinguish them from output counts and compiler parameters. In particular,

```math
0<\epsilon_5<\epsilon_6<1,\qquad
\epsilon_5+\epsilon_8<\epsilon_7<\xi/2,\qquad
0<\epsilon_9<\xi,\qquad
3-4\epsilon_5-\epsilon_9>0.
```

The additional constraint $`4/\sigma_d<d^{\xi/2}\leq d/\sigma_d`$ holds eventually: its upper inequality is $`5\xi/2\leq1`$. The source's filter-order formula (F18), equivalently (F239), reduces exactly to the stated $`N_{\rm f}`$.

At source period one, define

```math
H_d^{(1)}=2\pi\sum_{r=0}^{d-1}r|E_r\rangle\langle E_r|,
\qquad
|\theta_k\rangle=\frac1{\sqrt d}\sum_{r=0}^{d-1}
e^{-2\pi i rk/d}|E_r\rangle.
```

The normalized initial state from Eqs. (F25)–(F30) is

```math
|\psi_d\rangle=
A_d\sum_{k\in\mathcal S_d(0)}
e^{-\pi k^2/\sigma_d^2}e^{2\pi i n_0k/d}|\theta_k\rangle,
\qquad
\mathcal S_d(0)=\{k\in\mathbb Z:-d/2<k\leq d/2\}.
```

Fourier labels are taken modulo $`d`$ and $`A_d`$ is the normalization. The midpoint choice of $`n_0`$ gives $`\alpha_0=1`$.

For the positive absorption potential of Eqs. (F14)–(F24), let

```math
\begin{aligned}
I_{N_{\rm f}}&=\int_{\mathbb R}\operatorname{sinc}^{2N_{\rm f}}(x)\,dx,
&\operatorname{sinc}(x)&=\frac{\sin(\pi x)}{\pi x},\\
C_0&=1+2\pi N_{\rm f}+\frac{2N_{\rm f}+1}{I_{N_{\rm f}}},
&\nu_d&=\frac{\log(\pi\sigma_d^2)}{2\pi C_0\kappa}
\frac{d^{1-\xi/16}}{\delta_{\rm s}\sigma_d},\\
m_d&=2\left\lfloor\frac12d^{\xi/2}\sigma_d+1\right\rfloor,
&\gamma_{\rm s}&=\frac{m_d-2}{d},\\
x_{\rm vr}&=\frac{d^{\xi/4}\sigma_d}{\pi d},
&x_0&=\pi+x_{\rm vr}+\pi\gamma_{\rm s}.
\end{aligned}
```

The scale $`\nu_d`$ need not be an integer. It tends to infinity. Define

```math
\begin{aligned}
b_d&=\frac{1-2\pi/(\delta_{\rm s}d^2)}{I_{N_{\rm f}}},\\
\bar V_{0,d}(x)&=\frac1{\delta_{\rm s}d^2}
+\nu_d b_d\sum_{p\in\mathbb Z}
\operatorname{sinc}^{2N_{\rm f}}\!\left(\nu_d(x-x_0-2\pi p)\right).
\end{aligned}
```

Its integral over a period is one and it is everywhere at least $`1/(\delta_{\rm s}d^2)`$. The fixed-period absorption operator and jump operators are

```math
\begin{aligned}
V_d^{(1)}&=2\pi\delta_{\rm s}\sum_{k=0}^{d-1}
\bar V_{0,d}(2\pi k/d)|\theta_k\rangle\langle\theta_k|,\\
J_{d,k}^{(1)}&=\sqrt{4\pi\delta_{\rm s}\bar V_{0,d}(2\pi k/d)}
\,|\psi_d\rangle\langle\theta_k|.
\end{aligned}
```

Thus the no-tick amplitude generator is $`-iH_d^{(1)}-V_d^{(1)}`$. The factor of two in the total effect is essential:

```math
Q_d^{(1)}=\sum_kJ_{d,k}^{(1)\dagger}J_{d,k}^{(1)}=2V_d^{(1)}.
```

### Summed effect, physical scale and resolvent

The explicit $`C_0`$ satisfies the source's derivative bound (F20), proved in Lemma 28. One can check it directly: the Fourier transform of $`\operatorname{sinc}^{2N_{\rm f}}`$ is the $`N_{\rm f}`$-fold convolution of the triangular density, supported in $`[-N_{\rm f},N_{\rm f}]`$ and bounded by one. The periodic potential therefore has Fourier modes only at $`|\ell|\leq2\pi\nu_dN_{\rm f}`$. Summing their absolute values bounds its supremum by $`\nu_d[1+(2N_{\rm f}+1)/I_{N_{\rm f}}]`$; an $`r`$th derivative adds at most $`(2\pi\nu_dN_{\rm f})^r`$. The chosen $`C_0`$ bounds both constants, giving

```math
\sup_x|\bar V_{0,d}^{(r)}(x)|\leq\nu_d^{r+1}C_0^{r+1},
\qquad r\geq0.
```

Choose the physical timescale

```math
\lambda_d=\frac{g}{4\pi d},\qquad
H_d=\lambda_d\left(H_d^{(1)}-\pi(d-1)I\right),\qquad
J_{d,k}=\sqrt{\lambda_d}\,J_{d,k}^{(1)}.
```

This multiplies all waiting times by $`1/\lambda_d`$ and leaves their coefficient of variation unchanged. It gives $`\|H_d\|=g(d-1)/(4d)<g/4`$, and

```math
\begin{aligned}
Q_d&\geq\lambda_d\frac{4\pi}{d^2}I=gd^{-3}I,\\
\|Q_d\|&\leq\lambda_d4\pi\delta_{\rm s}\nu_d C_0
=g\,\frac{\log(\pi d^{4\xi})}{2\pi\kappa}
d^{-33\xi/16}=o(g).
\end{aligned}
```

In particular, $`Q_d\leq gI`$ eventually. This accounts for the sum of all $`d`$ tick-channel effects, rather than assigning a separate allowance to each channel.

For every initial density matrix, the no-tick survival obeys

```math
\frac{d}{dt}\operatorname{tr}(e^{tK_d}\rho)
=-\operatorname{tr}(Q_de^{tK_d}\rho)
\leq-gd^{-3}\operatorname{tr}(e^{tK_d}\rho).
```

Consequently $`\|e^{tK_d}\|_{1\to1}\leq e^{-gt/d^3}`$ and

```math
\|(-K_d)^{-1}\|_{1\to1}
\leq\int_0^\infty e^{-gt/d^3}\,dt=\frac{d^3}{g}.
```

The trace-norm statement follows from complete positivity, equivalently from the operator norm of the adjoint map on the identity. The floor also makes every clean waiting-time moment finite at each fixed dimension. Its value is a sufficient lower bound, not a claim that the least eigenvalue equals the floor.

### Accuracy and the actual mean

Equation (F243), with the parameters above, gives the clean precision

```math
\frac{(\mathbb EX_d^{(1)})^2}{\operatorname{Var}X_d^{(1)}}
\geq\frac1{12}\frac{d^{2-\xi}}{\sigma_d^2}
+o\!\left(\frac{d^{2-\xi}}{\sigma_d^2}\right)
=\frac1{12}d^{2-\varepsilon}+o(d^{2-\varepsilon}).
```

Thus the asserted upper bound $`24d^{-2+\varepsilon}`$ on the squared coefficient of variation holds eventually. This uses the intermediate bound with its explicit parameters, rather than relying on the final source theorem's parameter renaming.

The mean needs an additional check. The source's survival inequalities (F75)–(F82) use a capture window beginning at $`t_1=1/2`$ and ending at $`t_2=1/2+x_{\rm vr}/\pi+\gamma_{\rm s}=1/2+o(1)`$. With the displayed choice,

```math
\gamma_{\rm s}=\Theta(d^{-1+5\xi/2}),\qquad
x_{\rm vr}=o(\gamma_{\rm s}),\qquad
\delta_{\rm s}\to\infty.
```

The Gaussian tail and wavepacket errors in (F38), (F78), (F81) and (F153)–(F158) decay faster than any inverse power of $`d`$. For example, the slowest wavepacket exponential has exponent of order $`-d^{\xi/8}`$. The potential tail from (F240) obeys

```math
\delta_{\rm s}\widetilde\epsilon_V
=O_{\varepsilon}\!\left(
\frac{d^{-2+9\xi/2}}{(\log d)^{2N_{\rm f}-1}}
\right)+O(d^{-2})
=o(\gamma_{\rm s}^2).
```

The lower and upper survival bounds therefore imply

```math
\Pr(X_d^{(1)}\geq1/3)\geq1-o(1),\qquad
\Pr(X_d^{(1)}>1)=o(1).
```

For large $`d`$, both useful probabilities, $`\Pr(X_d^{(1)}\geq1/3)`$ and $`\Pr(X_d^{(1)}\leq1)`$, are at least one half. The first gives $`\mathbb EX_d^{(1)}\geq1/6`$. If the mean were greater than two, the second would give

```math
\operatorname{Var}X_d^{(1)}
\geq\tfrac12(\mathbb EX_d^{(1)}-1)^2
>\tfrac18(\mathbb EX_d^{(1)})^2,
```

contradicting the diverging precision just established. Hence $`1/6\leq\mathbb EX_d^{(1)}\leq2`$ eventually. Rescaling gives the claimed mean interval. In particular, the conclusion is not inferred from a narrow central peak while leaving rare tails uncontrolled.

### Equation correspondence

The pinned reconstruction uses the consecutively numbered arXiv equations. The published Appendix F numbering used above has the following correspondence, checked against the [published PDF](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.3.010319).

| Input | Published Appendix F | Numbering in the pinned reconstruction |
|---|---|---|
| Positive potential and parameter definitions | (F14)–(F24) | (359)–(369) |
| Initial state and midpoint energy | (F25)–(F30) | (370)–(375) |
| Survival bounds and capture window | (F75)–(F82), (F121)–(F124) | (420)–(427), (466)–(469) |
| Derivative bound | Lemma 28, (F185) | Lemma 28, (530) |
| Potential-tail estimate | (F240) | (585) |
| Accuracy bound and parameter constraints | (F243)–(F245) | (588)–(590) |

## 2. Application with two fixed temperatures

Fix a target loss $`0<\eta<1`$. Choose inverse temperatures $`0<\beta_H<\beta_C`$, independent of $`d`$, satisfying

```math
0<\theta:=\frac{\beta_H}{\beta_C}\leq\frac{\eta}{44}.
```

Use the clean lemma with $`\varepsilon=\eta`$. In the compiler, choose the cold reverse factor, cold carrier gap, and hot upward/downward ratio as

```math
z_d=d^{-11},\qquad
q_d=\frac{11\log d}{\beta_C},\qquad
h_d=e^{-2\beta_Hq_d}=d^{-22\theta}.
```

The hot upward rate is $`gh_d`$; its downward rate and the forward cold release rate are $`g`$. For each fixed $`d`$, compare $`L_{z_d}^{(h_d)}`$ with $`L_0^{(h_d)}`$, keeping $`h_d>0`$ fixed while switching on only the cold reverse channels. A simultaneous reference limit $`z\to0`$ with $`h=z^{2\theta}`$ would turn off the pump, make the reference reset incomplete, and invalidate the resolvent comparison.

### Reset delay and perturbation gates

The reference reset delay $`R_{h_d}`$ has exact moments

```math
\begin{aligned}
r_{h_d}:=\mathbb ER_{h_d}&=\frac{1+2/h_d}{g}
=O(d^{22\theta}/g),\\
s_{h_d}:=\mathbb ER_{h_d}^2&=\frac{2+6/h_d+8/h_d^2}{g^2},\\
\operatorname{Var}R_{h_d}&=\frac{1+2/h_d+4/h_d^2}{g^2}
=O(d^{44\theta}/g^2).
\end{aligned}
```

The independent reference interval is $`T_0=R_{h_d}+X_d`$. Hence

```math
\begin{aligned}
\mu_0&=\mu_d+r_{h_d}=\Theta_\eta(d/g),\\
v_0&=\mathbb EX_d^2+2\mu_dr_{h_d}+s_{h_d},\\
F_0&=\frac{\operatorname{Var}X_d+\operatorname{Var}R_{h_d}}{\mu_0^2}
=O_\eta(d^{-2+\eta}).
\end{aligned}
```

Here the reset mean is $`O(d^{\eta/2}/g)=o(d/g)`$ and its variance is $`O(d^\eta/g^2)`$. All reset waiting time is included.

The clean lemma and the compiler's norm estimates give, eventually,

```math
B=B_{C,d}+r_{h_d}\leq2d^3/g,\qquad
a=\operatorname{Tr}Q_d\leq dg,\qquad
\Lambda=2(a+g)\leq4dg,\qquad
\delta=z_d\Lambda\leq4g d^{-10}.
```

Consequently $`\delta B=O(d^{-7})`$, $`2\delta B^2/\mu_0=O(d^{-5})`$, and $`2z_daB=O(d^{-7})`$. The additional second-moment gate is $`v_0/\mu_0^2=1+F_0\to1`$. All sufficient conditions of the finite-rate theorem therefore hold for large $`d`$.

Applying its signed-Fano bound,

```math
\begin{aligned}
F\leq F_0
&+48\frac{\delta B^3}{\mu_0^2}
+40\frac{\delta B^2}{\mu_0}
+32\frac{z_daB^2}{\mu_0}
+16z_d^2a^2B^2\\
&=O_\eta(d^{-2+\eta})
+O(d^{-3})+O(d^{-5})+O(d^{-5})+O(d^{-14}).
\end{aligned}
```

The actual mean block duration differs from $`\mu_0`$ by $`O(d^{-4}/g)`$. The expected reverse-capture count per block is $`O(d^{-7})`$. Thus the actual positive signed mean current satisfies $`j=\Theta_\eta(g/d)`$.

### Simultaneous performance and resource statement

Let $`N(t)`$ count positive captures minus reverse captures, and define

```math
j=\lim_{t\to\infty}\frac{\mathbb EN(t)}t,\qquad
D_{\rm count}=\lim_{t\to\infty}\frac{\operatorname{Var}N(t)}t,
\qquad F=D_{\rm count}/j.
```

For the constructed family, at fixed $`g`$, $`\eta`$ and chosen temperatures,

```math
\boxed{
\mathcal P:=\frac1F\geq c_\eta d^{2-\eta},\qquad
j=\Theta_\eta(g/d),\qquad
D_{\rm time}:=\lim_{t\to\infty}
\frac{\operatorname{Var}[N(t)/j]}t
=\frac Fj\leq\frac{C_\eta}{g}d^{-1+\eta}.
}
```

The calibrated estimator uses the supplied actual current $`j`$. The [long-time signed-current precision](counting_statistics.md) $`\mathcal P`$ is not the reciprocal coefficient of variation of positive capture intervals once reverse captures occur. The relation $`D_{\rm time}=F/j`$ shows why the result remains useful for time estimation despite the growing mean period. Under the same total event-rate allowance, the [classical comparison](classical_comparison.md) gives $`D_{\rm time}\geq1/(2g)`$.

The full compiled device has $`d+2`$ states. Its sum of all jump effects is at most $`2gI`$: on the core it is $`Q_d+z_dgP_{\psi_d}`$, on $`m`$ it is $`gh_d+z_d\operatorname{Tr}Q_d`$, and on $`e`$ it is $`2g`$. This includes every modeled capture, reverse event, release and hot transition. There are $`d`$ capture channels and their reverses; the two-state increase does not imply a dimension-independent number of engineered bath channels.

In the [bare-energy thermodynamic model](thermodynamics.md), the entropy per net tick is exactly

```math
\Sigma_d=2\log(1/z_d)-\log(1/h_d)
=22(1-\theta)\log d.
```

The cold gap $`q_d`$ and hot gap $`2q_d`$ grow logarithmically with $`d`$. The active core Hamiltonian remains bounded by $`g/4`$, while the full bare Hamiltonian has range $`2q_d`$. These are different resource statements.

The temperature quantifiers are essential: for every fixed target loss $`\eta`$, one chooses a sufficiently small temperature ratio that remains fixed as $`d`$ grows. A single positive $`\theta`$ does not establish the exponent $`2-o(1)`$; the explicit reset variance incurs the fixed loss $`44\theta`$. The coefficient 44 is sufficient and is not claimed optimal.

The exact statements here concern the [specified finite-dimensional GKLS generator](model.md). Its [thermal interpretation](thermodynamics.md) uses the clustered weak-coupling construction at each fixed dimension. The weak-coupling limit precedes the long-time counting limit and the subsequent dimension limit. No uniform finite-coupling, infinite-time, growing-dimension assertion is needed for this application.
