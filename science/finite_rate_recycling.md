# Finite-rate recycling theorem

[Model](model.md) · [Counting statistics](counting_statistics.md) · [Thermodynamics](thermodynamics.md) · [Quasiideal application](quasiideal_application.md)

This theorem replaces the ideal preparation after a tick by a finite-rate serial reset. It bounds the change in the signed count variance, including thermal reverse events and the correlations they create. The required reverse suppression is expressed through an all-input survival inverse. If that inverse grows polynomially with dimension, inverse-polynomial reverse rates suffice.

The notation and all jump operators are specified in the [model](model.md). The hot ratio $`h>0`$ is fixed throughout each perturbation comparison.

## 1. The finite conditions and conclusion

Let the input clock satisfy $`Q\le gI_C`$ and $`\|\mathcal R_C\|_{1\to1}\le B_C`$. Its ideal waiting time from $`P_\psi`$ has mean $`\mu`$ and variance $`\sigma^2`$. Define

```math
\begin{aligned}
r_h&=\frac{2/h+1}{g},
&s_h&=\frac{8/h^2+6/h+2}{g^2},
&v_h&=\frac{4/h^2+2/h+1}{g^2},\\
\mu_0&=\mu+r_h,
&v_0&=\mathbb E X^2+2\mu r_h+s_h,
&F_0&=\frac{\sigma^2+v_h}{\mu_0^2},\\
B&=B_C+r_h,
&a&=\mathrm{Tr}Q,
&\Lambda&=2(a+g),
\qquad \delta=z\Lambda.
\end{aligned}
```

The quantities $`r_h,s_h,v_h`$ are the mean, second moment and variance of the reset phase in the reference model. In particular, $`v_0=\mu_0^2(1+F_0)`$.

For a finite $`z>0`$, assume

```math
\boxed{
\delta B\le\frac12,
\qquad
2\delta B^2\le\frac{\mu_0}{2},
\qquad
2zaB\le\frac12,
\qquad
v_0\le2\mu_0^2.
}
```

Then every block between positive captures terminates almost surely, has exponential moments in a neighborhood of zero, and the net current is positive. The signed inverse precision satisfies

```math
\boxed{
F\le F_0
+\frac{48\delta B^3}{\mu_0^2}
+\frac{40\delta B^2}{\mu_0}
+\frac{32zaB^2}{\mu_0}
+16z^2a^2B^2.
}
```

The current also obeys the explicit bounds

```math
\frac1{3\mu_0}\le j\le\frac2{\mu_0}.
```

These counting statements apply to the regenerative process started after a positive capture. When $`Q>0`$, the full finite-$`z`$ generator has a unique faithful stationary state and no other peripheral eigenvalues; the same limits hold from every initial state. The [counting proof](counting_statistics.md) gives the stationary state and the tilted-generator derivation.

To impose the full-device activity budget, also require

```math
z\le1,
\qquad gh+za\le2g.
```

The enlarged device then has exactly $`d+2`$ states and summed jump effect at most $`2gI`$.

The last moment condition in the theorem is mild. Since $`v_h\le r_h^2`$, it follows whenever the clean clock satisfies $`\sigma^2\le\mu^2`$:

```math
\mathrm{Var}(X+R_h)
=\sigma^2+v_h
\le\mu^2+r_h^2
\le(\mu+r_h)^2.
```

No assumption about an instantaneous or rapidly eliminated reset is made.

## 2. The exact reference reset

At $`z=0`$, a capture leaves the device in $`m`$. Before release to $`\psi`$, its auxiliary population follows a classical two-state absorption process with transient generator

```math
G_h=g
\begin{pmatrix}
-h&h\\
1&-2
\end{pmatrix}.
```

Rows label the current state $`m,e`$. At $`e`$, relaxation to $`m`$ and release to $`\psi`$ each have rate $`g`$. Let $`R_h`$ be the time to release starting at $`m`$.

For completeness, write $`r_m,r_e`$ for the first moments from the two auxiliary states. First-step equations give

```math
r_m=\frac1{gh}+r_e,
\qquad
r_e=\frac1{2g}+\frac12r_m.
```

Thus

```math
r_m=r_h=\frac{2/h+1}{g},
\qquad
r_e=\frac{1/h+1}{g}.
```

If $`s_m,s_e`$ are the corresponding second moments, the backward moment equation $`G_h s=-2r`$ gives

```math
gh(s_m-s_e)=2r_m,
\qquad
g(2s_e-s_m)=2r_e.
```

Solving yields $`s_m=s_h`$ and $`s_h-r_h^2=v_h`$ as stated above. For $`h=1/2`$,

```math
\mathbb E R_{1/2}=\frac5g,
\qquad
\mathbb E R_{1/2}^2=\frac{46}{g^2},
\qquad
\mathrm{Var}R_{1/2}=\frac{21}{g^2}.
```

The release prepares exactly $`P_\psi`$. The next core waiting time is therefore independent of the entire preceding reset phase. The reference positive-capture block is exactly

```math
T_0=R_h+X.
```

This identity gives $`\mu_0,v_0,F_0`$ and retains the reset time and its variance in full.

## 3. The killed generator and its survival inverse

Let $`\mathcal C_+`$ be the positive-capture recycling map,

```math
\mathcal C_+(\rho)
=\sum_kA_k\rho A_k^\dagger
=P_m\,\ell_+(\rho),
\qquad
\ell_+(\rho)=\mathrm{Tr}(Q\rho_C).
```

Here $`\rho_C`$ denotes the core block of $`\rho`$. Remove this map from the full generator but retain its anticommutator:

```math
\mathcal K_z^{(h)}
=\mathcal L_z^{(h)}-\mathcal C_+.
```

Its semigroup is completely positive and trace nonincreasing. Its trace is the probability that the next positive capture has not occurred. For the rest of the proof, suppress the fixed superscript $`h`$.

### Reference inverse

The core is stable and the auxiliary reset phase absorbs with finite moments. The reference mean survival is therefore finite from every initial state. Its completely positive time integral defines the reference inverse.

Write

```math
\mathcal R_0=(-\mathcal K_0)^{-1},
\qquad
S_C=\mathcal R_C^\dagger(I_C),
\qquad
S_0=\mathcal R_0^\dagger(I).
```

The mean-survival operator is block diagonal:

```math
S_0
=S_C
\oplus(\mu+r_h)P_m
\oplus(\mu+r_e)P_e.
```

Indeed, starting in the core gives the clean first-tick time; starting in an auxiliary level gives its release time followed by a clean cycle. Off-diagonal blocks do not enter any future population: the Hamiltonian and all jump effects preserve the three sectors, and the recycling terms depend only on their diagonal blocks. They therefore contribute nothing to the trace-survival functional.

Since $`S_C\le B_CI_C`$, $`\mu\le B_C`$ and $`r_e\le r_h`$,

```math
\|\mathcal R_0\|_{1\to1}
=\|S_0\|_\infty
\le B_C+r_h=B.
```

Also $`S_0\ge I/g`$. To see this directly, the positive-capture hazard is at most $`g`$ in every state. Hence any normalized initial state has reference survival at least $`e^{-gt}`$, and integrating gives mean survival at least $`1/g`$.

### Perturbation norm

At fixed $`h`$, the difference between the finite-$`z`$ and reference killed generators is

```math
\mathcal K_z=\mathcal K_0+z\mathcal V,
\qquad
\mathcal V
=\sum_k\mathcal D[A_k^\dagger]
+g\mathcal D[|e\rangle\langle\psi|].
```

The reverse-capture recycling map is

```math
\mathcal I_-(\rho)
=\sum_kA_k^\dagger\rho A_k
=\langle m|\rho|m\rangle Q,
\qquad
\|\mathcal I_-\|_{1\to1}=a.
```

The reverse-capture dissipators have total effect $`aP_m`$. Their recycling and anticommutator parts each have norm at most $`a`$. The reverse-release dissipator has norm at most $`2g`$. Therefore

```math
\|\mathcal V\|_{1\to1}\le2(a+g)=\Lambda,
\qquad
\|z\mathcal V\|_{1\to1}\le\delta.
```

This is where the number and combined strength of the reverse capture channels enter the perturbation estimate.

## 4. Stability before inversion

A formal inverse expansion alone does not establish that every block terminates. We first prove survival decay using the reference mean-survival operator.

The identity $`\mathcal K_0^\dagger(S_0)=-I`$ and the dual norm bound give

```math
\mathcal K_z^\dagger(S_0)
=-I+z\mathcal V^\dagger(S_0)
\le-(1-\delta B)I.
```

For a normalized positive initial state, let $`\rho_t=e^{t\mathcal K_z}(\rho)`$ and $`u(t)=\mathrm{Tr}(S_0\rho_t)`$. If $`\delta B<1`$,

```math
u'(t)
\le-(1-\delta B)\mathrm{Tr}\rho_t
\le-\frac{1-\delta B}{B}u(t).
```

Using $`I/g\le S_0\le BI`$ gives the explicit tail bound

```math
\mathrm{Tr}\rho_t
\le gB\exp\!\left[-\frac{1-\delta B}{B}t\right].
```

Thus the next positive capture occurs almost surely, with exponentially decaying survival. The integral

```math
\mathcal R_z
=\int_0^\infty e^{t\mathcal K_z}\,dt
=(-\mathcal K_z)^{-1}
```

exists as a completely positive map. Integrating the first inequality for $`u'(t)`$ yields

```math
\|\mathcal R_z\|_{1\to1}
\le\frac{B}{1-\delta B}.
```

Only now use the resolvent identity

```math
\mathcal R_z-\mathcal R_0
=\mathcal R_z(z\mathcal V)\mathcal R_0.
```

Under $`\delta B\le1/2`$, it proves

```math
\boxed{
\|\mathcal R_z\|_{1\to1}\le2B,
\qquad
\|\mathcal R_z-\mathcal R_0\|_{1\to1}
\le2\delta B^2.
}
```

The dependence on the inverse survival scale is explicit. A small reverse rate by itself is insufficient when $`B`$ is large.

## 5. Duration and reverse-count moments

For a block starting at $`P_m`$, define

```math
\mu_z=\mathbb ET,
\qquad
v_z=\mathbb ET^2,
\qquad
m_z=\mathbb EM,
\qquad
f_z=\mathbb E[M(M-1)],
\qquad
w_z=\mathbb E[TM].
```

The [joint-transform calculation](counting_statistics.md#2-the-joint-transform-of-duration-and-reverse-count) gives

```math
\begin{aligned}
\mu_z&=\mathrm{Tr}\mathcal R_z(P_m),\\
v_z&=2\mathrm{Tr}\mathcal R_z^2(P_m),\\
m_z&=z\mathrm{Tr}\mathcal I_-\mathcal R_z(P_m),\\
f_z&=2z^2\mathrm{Tr}
\mathcal I_-\mathcal R_z\mathcal I_-\mathcal R_z(P_m),\\
w_z&=z\mathrm{Tr}
\bigl(\mathcal R_z\mathcal I_-\mathcal R_z
+\mathcal I_-\mathcal R_z^2\bigr)(P_m).
\end{aligned}
```

The last expression retains the correlation between reverse events and elapsed time. Since $`\|P_m\|_1=1`$, the resolvent estimates imply

```math
\boxed{
\begin{aligned}
|\mu_z-\mu_0|&\le2\delta B^2,\\
|v_z-v_0|&\le12\delta B^3,\\
m_z&\le2zaB,\\
f_z&\le8z^2a^2B^2,\\
w_z&\le8zaB^2.
\end{aligned}
}
```

For the second-moment bound, use

```math
\|\mathcal R_z^2-\mathcal R_0^2\|
\le\|\mathcal R_z-\mathcal R_0\|
\bigl(\|\mathcal R_z\|+\|\mathcal R_0\|\bigr)
\le6\delta B^3,
```

and multiply by two. The other bounds follow directly from the displayed moment formulas. Reverse release is included in $`\mathcal V`$ and $`\mathcal R_z`$, even though it does not increment $`M`$.

## 6. Signed precision comparison

The exact renewal-reward formula is

```math
j=\frac{1-m_z}{\mu_z},
\qquad
F=(1-m_z)\frac{v_z}{\mu_z^2}-1
+\frac{2w_z}{\mu_z}
+\frac{f_z}{1-m_z}.
```

Under the finite conditions in Section 1,

```math
\frac{\mu_0}{2}\le\mu_z\le\frac{3\mu_0}{2},
\qquad
0\le m_z\le\frac12.
```

This immediately proves positivity of the current and the stated current bounds. For the variance comparison, drop the nonpositive term $`-m_zv_z/\mu_z^2`$ and use

```math
\left|\frac1{\mu_z^2}-\frac1{\mu_0^2}\right|
\le\frac{10|\mu_z-\mu_0|}{\mu_0^3}.
```

The four resulting contributions are bounded by

```math
\begin{aligned}
\frac{|v_z-v_0|}{\mu_z^2}
&\le\frac{48\delta B^3}{\mu_0^2},\\
v_0\left|\frac1{\mu_z^2}-\frac1{\mu_0^2}\right|
&\le\frac{40\delta B^2}{\mu_0},\\
\frac{2w_z}{\mu_z}
&\le\frac{32zaB^2}{\mu_0},\\
\frac{f_z}{1-m_z}
&\le16z^2a^2B^2.
\end{aligned}
```

Their sum proves the theorem. Every term is dimensionless, and uniform rescaling of all dynamical rates leaves the bound unchanged.

## 7. An explicit choice for a prescribed error

The theorem can be used without asymptotic notation. Suppose $`v_0\le2\mu_0^2`$, and define

```math
\mathcal E
=\frac{48\Lambda B^3}{\mu_0^2}
+\frac{40\Lambda B^2}{\mu_0}
+\frac{32aB^2}{\mu_0},
\qquad
\mathcal G=16a^2B^2.
```

Given any target additive inverse-precision error $`\tau>0`$, choose a positive $`z`$ satisfying

```math
z\le\min\left\{
1,
\frac{2g-gh}{a},
\frac1{2\Lambda B},
\frac{\mu_0}{4\Lambda B^2},
\frac1{4aB},
\frac{\tau}{2\mathcal E},
\sqrt{\frac{\tau}{2\mathcal G}}
\right\}.
```

Stability of the input implies $`a>0`$, so these denominators are well defined. This finite choice enforces both the theorem's gates and the full activity budget, and yields

```math
F\le F_0+\tau.
```

The dependence on $`B`$ is polynomial. After measuring times in units of $`1/g`$, if the supplied inverse $`gB_C`$ and $`1/h`$ grow at most polynomially with $`d`$, and $`\tau`$ is inverse polynomial, the right-hand side contains only inverse-polynomial requirements. Taking $`z`$ to be a sufficiently small inverse power of $`d`$ then suffices. By the [entropy identity](thermodynamics.md), this corresponds to logarithmic affinity when $`h`$ is also fixed or inverse polynomial and the chosen forward direction is thermodynamically allowed.

The statement needs quantitative control of the survival inverse. Eventual ticking at each finite dimension, without a bound on $`B_C`$, does not establish a logarithmic reset cost for a growing family.

The [quasiideal application](quasiideal_application.md) supplies the bound $`B_C\le d^3/g`$, checks all finite conditions, and obtains nearquadratic precision with $`z=d^{-11}`$.
