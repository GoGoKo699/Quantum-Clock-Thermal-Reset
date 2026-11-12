# From current fluctuations to a thermal clock

[Learning route](README.md) · [Milestone map](milestones.md) · [Scientific account](../science/README.md)

A clock converts an evolving physical system into a count that can be used to estimate elapsed time. If a tick also prepares the clock for its next cycle, that preparation is part of the clock's operation. This project asks how much precision remains when the preparation takes time, fluctuates, and has thermal reverse transitions.

The educational anchor supplies the language of quantum jumps, waiting times, and counting fluctuations. The project then supplies a particular thermal recycling mechanism, a quantitative bound on its added noise, and the resources needed for a quantum timing advantage.

## 1. One anchor and a short reading route

**Gabriel T. Landi, Michael J. Kewming, Mark T. Mitchison, and Patrick P. Potts, “Current Fluctuations in Open Quantum Systems: Bridging the Gap Between Quantum Continuous Measurements and Full Counting Statistics,” PRX Quantum 5, 020201 (2024).** [Published article](https://doi.org/10.1103/PRXQuantum.5.020201) · [Author-hosted full PDF](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf).

Use the following passages in the listed order. Page numbers are the article's printed page numbers, beginning with 020201-1.

| Step | Anchor passage | Equations | Use here |
|---|---|---|---|
| Dynamics and records | II A, p. 4; II C, pp. 7–9; II D, p. 10 | (5)–(7), (22)–(25), (37)–(40) | Generator, jump update, weighted count |
| Time until a selected event | VI A, pp. 39–40 | (254), (258)–(265) | Survival and waiting-time moments |
| Repeated resets | VI B.2, p. 43 | (288)–(294) | Regeneration and unsigned renewal noise |
| Fluctuations of the count | IV A, p. 24; IV D, p. 27 | (114)–(116), (131)–(135) | Tilted generator and cumulants |
| Thermal pairs | VI E.1, pp. 48–49 | (338) | Reverse channels and entropy weights |

Section V contains solution methods. Its sections A and C are useful when implementing the numerical checks, after the statistical definitions are clear. The fluctuation theorem following the anchor's Eq. (338) adds time-reversal assumptions in Eq. (339); this project's entropy balance is instead proved directly from occupation conservation.

### Translate notation before combining formulas

| Anchor notation | Project notation and meaning |
|---|---|
| $`L_k`$, a jump operator | The physical operators listed in the [model](../science/model.md#2-the-enlarged-clock), including capture, heating, release, and their reverses |
| $`\mathcal L_k(\rho)=L_k\rho L_k^\dagger`$ | A recycling superoperator; the aggregate positive-capture map is $`\mathcal C_+`$ |
| $`\mathcal L_0`$, with selected recycling terms removed | $`\mathcal K_z=\mathcal L_z-\mathcal C_+`$ when the stopping event is the next positive capture |
| Weights $`\nu_k`$ | $`+1`$ for capture, $`-1`$ for reverse capture, and $`0`$ for the remaining channels |
| Mean current $`J`$ and noise $`D`$ | $`j`$ and $`D_N`$; there is no factor of two in the variance rate |
| Fourier field $`\chi_{\rm A}`$ in $`e^{i\chi_{\rm A}N}`$ | Real moment-generating field $`\chi`$ in $`e^{\chi N}`$; use $`\chi_{\rm A}=-i\chi`$ |

The anchor's $`F(\tau)`$ is a current correlation function. The project's $`F=D_N/j`$ is a Fano factor. They are different quantities. The core's ideal mean and variance are $`\mu,\sigma^2`$; the enlarged device's positive-capture block mean is $`\mu_z`$.

## 2. The missing statistical step: blocks carry signed rewards

The input clock has jumps

```math
J_k=|\psi\rangle\langle v_k|.
```

Every ideal tick prepares the same state $`P_\psi`$. This is the complete-reset assumption. The compiled device captures the core into an auxiliary state $`m`$, passes through a second auxiliary state $`e`$, and eventually releases it into $`\psi`$. All three stages have reverse transitions. The observable is

```math
N(t)=N_+(t)-N_-(t),
```

where $`N_+`$ counts captures and $`N_-`$ counts reverse captures. Hot transitions and release events affect elapsed time but add zero to this record.

Every positive capture prepares $`P_m`$. Define a block from immediately after one positive capture to the next positive capture. Let $`T`$ be its duration and $`M`$ the number of reverse captures within it. Successive pairs $`(T,M)`$ have the same distribution and are independent. Their signed contribution is

```math
Y=1-M.
```

Thus the regenerative object is the pair of a duration and a reward. A long block can contain more reverse events, so their correlation matters. For a positive mean reward, the [counting proof](../science/counting_statistics.md#3-current-and-diffusion-from-block-rewards) gives

```math
j=\frac{\mathbb EY}{\mathbb ET},
\qquad
D_N=\frac{\mathbb E[(Y-jT)^2]}{\mathbb ET},
\qquad
F=\frac{D_N}{j}.
```

When $`Y=1`$ in every block, these expressions reduce to ordinary renewal counting:

```math
j=\frac1{\mathbb ET},
\qquad
D_N=\frac{\mathrm{Var}T}{(\mathbb ET)^3},
\qquad
F=\frac{\mathrm{Var}T}{(\mathbb ET)^2}.
```

This is the setting of the anchor's Eq. (294). At positive reverse ratio $`z`$, the last formula describes the positive-capture count, rather than the signed observable of this project.

The choice of stopping event also determines the killed generator. Removing $`\mathcal C_+`$ conditions on the absence of a positive capture. Reverse captures, heating, and release still take place inside the block. Reverse captures are retained in the evolution and marked when forming the joint transform. Killing both signs would define a different interval.

The elapsed-time estimator uses a supplied calibrated mean current:

```math
\widehat t=\frac{N(t)}j,
\qquad
D_{\mathrm{time}}
=\lim_{t\to\infty}\frac{\mathrm{Var}\widehat t}{t}
=\frac{D_N}{j^2}
=\frac Fj.
```

Precision $`P=1/F`$ and timing diffusion answer different questions. The latter also includes the rate at which useful net ticks arrive. The cost of learning $`j`$ is outside the theorem.

## 3. What must be added to obtain the project's result

### Charge the return time and its variance

Set the cold reverse ratio to zero while keeping the same hot ratio $`h`$. This is an analytical reference process. If $`X`$ is the ideal core waiting time and $`R`$ the auxiliary return time, then

```math
T_0=R+X,
\qquad
\mathbb ER=\frac{2/h+1}{g},
\qquad
\mathrm{Var}R=\frac{4/h^2+2/h+1}{g^2}.
```

The release prepares a fixed state, so $`R`$ and $`X`$ are independent. Consequently,

```math
\mathbb ET_0=\mu+\frac{2/h+1}{g},
\qquad
F_0=
\frac{\sigma^2+(4/h^2+2/h+1)/g^2}
     {[\mu+(2/h+1)/g]^2}.
```

The return stage contributes to both the period and its fluctuations. A statement that an auxiliary state can eventually prepare $`\psi`$ supplies neither of these two costs. The [reference calculation](../science/finite_rate_recycling.md#2-the-exact-reference-reset) supplies them exactly.

### Control all states that a reverse event can prepare

A reverse capture can return the core to a state different from $`\psi`$. The proof therefore needs a bound on survival from every core state, expressed by

```math
\|(-\mathcal K)^{-1}\|_{1\to1}\le B_C.
```

The [finite-rate theorem](../science/finite_rate_recycling.md) uses this bound to control the enlarged killed generator and the joint duration–reverse-count moments. Its explicit error estimate determines how small $`z`$ must be as dimension grows. Continuity at fixed dimension alone would leave that dependence undetermined. When $`h`$ depends on dimension, the physical generator and its zero-$`z`$ reference use the same $`h`$ at each dimension.

### Supply an accurate input clock and retain its time scale

The nearquadratic input family is imported from Woods and collaborators, with the source assumptions reconstructed in the [quasiideal application](../science/quasiideal_application.md). The project adds finite-rate recycling to that family. For each fixed target loss $`\eta\in(0,1)`$, the stated construction gives, for sufficiently large dimension,

```math
P\ge c_\eta d^{2-\eta},
\qquad
j=\Theta(g/d),
\qquad
D_{\mathrm{time}}
\le \frac{C_\eta}{g}d^{-1+\eta}.
```

The last bound supplies the operational timing comparison. The complete enlarged device obeys $`\sum_\alpha L_\alpha^\dagger L_\alpha\le2gI`$. Under that same complete activity cap, the [classical comparison](../science/classical_comparison.md) gives $`D_{\mathrm{time}}\ge1/(2g)`$ for the specified classical class.

### Price the thermal bias and state the physical scope

For a bare gap $`q`$ and inverse temperatures $`\beta_C,\beta_H`$, the ratios are

```math
z=e^{-\beta_Cq},
\qquad
h=e^{-2\beta_Hq},
\qquad
\Sigma=\log\frac{h}{z^2}
=2q(\beta_C-\beta_H).
```

Occupation conservation makes $`\Sigma`$ the stationary environment entropy per net tick, including the entire return path. The construction achieves $`\Sigma=O(\log d)`$ with $`d+2`$ system states and up to $`d+2`$ independently engineered bath couplings. Each coupling supplies a forward/reverse pair; their number is separate from the two bath temperatures.

There are two resource choices. Fixed bare gaps require a cold temperature that decreases with dimension. Fixed bath temperatures require gaps growing as $`\log d`$ and a slower hot excitation. For the latter, $`\theta=\beta_H/\beta_C\le\eta/44`$ suffices for the displayed exponent loss. The ratio is selected for the target $`\eta`$ before taking dimension large.

The [thermal account](../science/thermodynamics.md) uses a bare Hamiltonian degenerate on the core, static engineered couplings, and a clustered weak-coupling limit. It also records Lamb-shift compensation and the distinction between bare and full energies. The finite-generator result is exact for the specified GKLS model. Its microscopic foundation takes weak coupling first at fixed device, then long time in the limiting model, then growing dimension. It does not prove infinite-time counting convergence at fixed microscopic coupling. Detector amplification, storage, and calibration are additional resources outside this reset result.

## 4. A complete three-state example

Take a one-dimensional core state $`c=\psi`$, no coherent motion, and $`Q=g`$. Add $`m,e`$ and choose

```math
z=h=\frac14.
```

The process is a classical three-state instance of the same construction. It makes the statistical and thermal accounting explicit.

| State transition | Rate | Record increment |
|---|---:|---:|
| $`c\to m`$ | $`g`$ | $`+1`$ |
| $`m\to c`$ | $`g/4`$ | $`-1`$ |
| $`m\to e`$ | $`g/4`$ | $`0`$ |
| $`e\to m`$ | $`g`$ | $`0`$ |
| $`e\to c`$ | $`g`$ | $`0`$ |
| $`c\to e`$ | $`g/4`$ | $`0`$ |

Use the order $`(c,m,e)`$ and put the source state in each matrix column. The population generator and stationary distribution are

```math
\frac{L}{g}=
\begin{pmatrix}
-5/4&1/4&1\\
1&-1/2&1\\
1/4&1/4&-2
\end{pmatrix},
\qquad
\pi=
\begin{pmatrix}2/9\\2/3\\1/9\end{pmatrix}.
```

Indeed, the columns sum to zero, $`L\pi=0`$, and the entries of $`\pi`$ sum to one. The signed mean current is

```math
j=g\pi_c-\frac g4\pi_m=\frac g{18}.
```

### Positive-capture intervals

Remove only the $`c\to m`$ recycling entry to form $`K`$. Its inverse is

```math
g(-K)^{-1}=
\begin{pmatrix}
1&1&1\\
1/3&3&5/3\\
1/6&1/2&5/6
\end{pmatrix}.
```

Let $`p_m=(0,1,0)^{\mathsf T}`$ and $`\mathbf1^{\mathsf T}=(1,1,1)`$. Multiplication gives

```math
\begin{aligned}
\mathbb ET
&=\mathbf1^{\mathsf T}(-K)^{-1}p_m=\frac9{2g},\\
\mathbb ET^2
&=2\mathbf1^{\mathsf T}(-K)^{-2}p_m=\frac{67}{2g^2},\\
\mathrm{Var}T&=\frac{53}{4g^2}.
\end{aligned}
```

Thus the positive-capture rate is $`2g/9`$ and its unsigned Fano factor is $`53/81`$. Each block contains on average $`\mathbb EM=3/4`$ reverse captures, since the reverse rate is $`g\pi_m/4=g/6`$ and the block rate is $`2g/9`$. Its average net reward is therefore $`1/4`$, reproducing $`j=(1/4)/[9/(2g)]=g/18`$.

### Signed fluctuations

For the real counting field, multiply only the $`c\to m`$ entry by $`e^\chi`$ and the $`m\to c`$ entry by $`e^{-\chi}`$. Keep the diagonal entries fixed. Let $`x(\chi)=\lambda(\chi)/g`$ be the eigenvalue branch with $`x(0)=0`$. Its characteristic equation is

```math
x^3+\frac{15}{4}x^2+\frac{27}{8}x
+\frac5{16}-\frac14e^\chi-\frac1{16}e^{-\chi}=0.
```

One and two derivatives at zero give

```math
\frac{27}{8}x'(0)=\frac3{16},
\qquad
\frac{27}{8}x''(0)+\frac{15}{2}[x'(0)]^2=\frac5{16}.
```

Hence

```math
\begin{aligned}
j&=g x'(0)=\frac g{18},\\
D_N&=g x''(0)=\frac{125g}{1458},\\
F&=\frac{D_N}{j}=\frac{125}{81},\\
D_{\mathrm{time}}&=\frac{F}{j}=\frac{250}{9g}.
\end{aligned}
```

The positive-capture value $`53/81`$ and the signed value $`125/81`$ refer to different records from the same device. Treating a block as one useful tick would discard its reverse counts.

### Reset and heat costs in the same example

The zero-$`z`$ reference at the same $`h=1/4`$ has a core mean and variance $`1/g,1/g^2`$. Its return stage contributes $`9/g`$ to the mean and $`73/g^2`$ to the variance. The total reference interval therefore has mean $`10/g`$ and variance $`74/g^2`$. These costs are present before finite reverse events are added.

For the finite example, choose any $`q>0`$ and

```math
\beta_C=\frac{\log4}{q},
\qquad
\beta_H=\frac{\log4}{2q}.
```

The entropy per net tick is $`\Sigma=\log4`$, and the largest total escape rate is $`2g`$, attained at $`e`$. This example establishes how to compute and charge the quantities. The growing quantum advantage uses the accurate higher-dimensional input family and the finite-rate bound described in Section 3.

Continue with the [30-milestone map](milestones.md) for the connected conceptual route, or the [finite-rate theorem](../science/finite_rate_recycling.md) for its precise hypotheses and error estimate.
