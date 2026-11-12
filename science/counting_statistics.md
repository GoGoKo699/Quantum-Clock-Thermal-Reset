# Signed counting statistics

[Model](model.md) · [Finite-rate recycling](finite_rate_recycling.md) · [Thermodynamics](thermodynamics.md)

The thermodynamic current is the number of captures minus the number of reverse captures. Its diffusion is not determined by the distribution of positive capture intervals alone. This page derives the joint duration–reverse-count transform, the exact signed Fano factor, and its equivalence to the tilted-generator cumulants.

The hot ratio $`h`$ is fixed. Write $`\mathcal L_z`$ for the full enlarged generator and

```math
\mathcal K_z=\mathcal L_z-\mathcal C_+,
\qquad
\mathcal R_z=(-\mathcal K_z)^{-1},
\qquad
\mathcal C_+(\rho)=P_m\ell_+(\rho).
```

Assume the stability condition proved in [Finite-rate recycling](finite_rate_recycling.md#4-stability-before-inversion). It ensures that all states reach a positive capture with an exponentially decaying survival tail.

## 1. Exit normalization and regeneration

Since all removed trace loss is positive-capture loss,

```math
\operatorname{Tr}\mathcal K_z(\rho)=-\ell_+(\rho).
```

Integrating this identity along the killed semigroup and using its decay gives the operator identity

```math
\ell_+\mathcal R_z=\operatorname{Tr}.
```

In particular, the positive-capture density from $`P_m`$ is

```math
p_z(t)=\ell_+e^{t\mathcal K_z}(P_m),
\qquad
\int_0^\infty p_z(t)\,dt=1.
```

At that capture the normalized state is again $`P_m`$. The future law is therefore independent of the past. With the block conventions from the [model](model.md), successive duration–count pairs $`(T,M)`$ are independent and identically distributed, and each complete block contributes $`Y=1-M`$ to the signed record.

The first block from an arbitrary initial state can have a different law. Its exponentially decaying duration does not change the long-time current or diffusion.

## 2. The joint transform of duration and reverse count

The reverse-capture recycling map, without its factor $`z`$, is

```math
\mathcal I_-(\rho)
=\langle m|\rho|m\rangle Q.
```

Multiplying each reverse-capture trajectory by a factor $`u`$ changes its recycling term from $`z\mathcal I_-`$ to $`zu\mathcal I_-`$. All its anticommutator terms stay unchanged. Therefore

```math
\begin{aligned}
\Phi_z(s,u)
&:=\mathbb E\!\left[e^{-sT}u^M\right]\\
&=\ell_+\left[s\mathbb I-\mathcal K_z
-z(u-1)\mathcal I_-\right]^{-1}(P_m).
\end{aligned}
```

Here $`\mathbb I`$ is the identity superoperator. At $`(s,u)=(0,1)`$, the inverse exists. Its finite-dimensional analytic continuation exists in a neighborhood of that point. For real parameters sufficiently close to it, the perturbed killed semigroup remains exponentially stable and its trajectory expansion has nonnegative weights. Thus the transform is an actual exponential-moment transform there, not just a formal matrix expression. This establishes the joint moments needed below.

Differentiate the inverse and use $`\ell_+\mathcal R_z=\operatorname{Tr}`$. The first two duration moments are

```math
\mu_z=\mathbb ET
=\operatorname{Tr}\mathcal R_z(P_m),
\qquad
v_z=\mathbb ET^2
=2\operatorname{Tr}\mathcal R_z^2(P_m).
```

The reverse-count moments are

```math
\begin{aligned}
m_z:=\mathbb EM
&=z\operatorname{Tr}\mathcal I_-\mathcal R_z(P_m),\\
f_z:=\mathbb E[M(M-1)]
&=2z^2\operatorname{Tr}
\mathcal I_-\mathcal R_z\mathcal I_-\mathcal R_z(P_m).
\end{aligned}
```

The mixed derivative gives

```math
\begin{aligned}
w_z:=\mathbb E[TM]
&=-\partial_s\partial_u\Phi_z(0,1)\\
&=z\operatorname{Tr}\!\left[
\bigl(\mathcal R_z\mathcal I_-\mathcal R_z
+\mathcal I_-\mathcal R_z^2\bigr)(P_m)
\right].
\end{aligned}
```

Both summands are required. The reverse event can be placed at different points in the elapsed block, and its occurrence changes the distribution of the remaining duration.

## 3. Current and diffusion from block rewards

For $`Y=1-M`$,

```math
\mathbb EY=1-m_z,
\qquad
\mathbb EY^2=1-m_z+f_z,
\qquad
\mathbb E[YT]=\mu_z-w_z.
```

The renewal-reward current and diffusion are

```math
j=\frac{\mathbb EY}{\mathbb ET}
=\frac{1-m_z}{\mu_z},
\qquad
D_N=\frac{\mathbb E[(Y-jT)^2]}{\mu_z}.
```

The joint exponential moments justify the long-time second-moment limit, including the unfinished final block. Equivalently, the tilted-generator derivation below obtains the same coefficients directly from a simple spectral eigenvalue.

When $`m_z<1`$, the current is positive and

```math
\begin{aligned}
F=\frac{D_N}{j}
&=\frac{\mathbb EY^2-2j\mathbb E[YT]
+j^2\mathbb ET^2}{1-m_z}\\
&=(1-m_z)\frac{v_z}{\mu_z^2}-1
+\frac{2w_z}{\mu_z}
+\frac{f_z}{1-m_z}.
\end{aligned}
```

At $`z=0`$, the reverse count is identically zero and this reduces to the ordinary renewal result

```math
F_0=\frac{v_0}{\mu_0^2}-1
=\frac{\operatorname{Var}T_0}{\mu_0^2}.
```

At finite $`z`$, replacing $`F`$ by $`\operatorname{Var}T/\mu_z^2`$ would describe a different record: it would count every positive capture, including positive captures that cancel an earlier reverse capture.

## 4. The stationary state and its positivity

The stable killed inverse gives an explicit stationary density matrix:

```math
\rho_{\mathrm{ss}}
=\frac{\mathcal R_z(P_m)}{\mu_z}.
```

It is positive because $`\mathcal R_z`$ is completely positive, and its trace is one by definition of $`\mu_z`$. Moreover,

```math
\begin{aligned}
\mathcal L_z\mathcal R_z(P_m)
&=\mathcal K_z\mathcal R_z(P_m)
+P_m\ell_+\mathcal R_z(P_m)\\
&=-P_m+P_m=0.
\end{aligned}
```

It is the unique stationary density matrix. In fact, if $`\mathcal L_z(\rho)=0`$, invertibility of $`\mathcal K_z`$ forces

```math
\rho=\mathcal R_z(P_m)\ell_+(\rho),
```

so trace normalization fixes $`\rho`$ uniquely. This argument does not require $`Q`$ to have full rank.

The stationary positive and reverse capture intensities are, respectively,

```math
j_+=\ell_+(\rho_{\mathrm{ss}})=\frac1{\mu_z},
\qquad
j_-=z\operatorname{Tr}\mathcal I_-(\rho_{\mathrm{ss}})
=\frac{m_z}{\mu_z}.
```

Their difference agrees with the regenerative current.

### Faithfulness and relaxation when $`Q>0`$

Suppose $`z>0`$ and $`Q>0`$. The vectors $`v_k`$ then span the core. All capture operators and their adjoints occur with nonzero coefficients, and their products generate every matrix unit on $`\mathcal H_C\oplus\operatorname{span}\{m\}`$. The two hot operators connect $`e`$ to $`m`$. Hence the jump operators generate the full matrix algebra and occur in adjoint pairs.

To see why the stationary state is faithful, let $`P`$ be its support. For any vector orthogonal to this support, the corresponding diagonal matrix element of $`\mathcal L_z(\rho_{\mathrm{ss}})=0`$ is a sum of nonnegative jump contributions. Each must vanish, so every jump preserves the support. Because the adjoints also occur, the support is a reducing subspace for the full jump algebra. That algebra has no nontrivial reducing subspace. Thus $`P=I`$.

There are also no nonconstant observables with a purely imaginary generator eigenvalue. The dissipative product identity is

```math
\mathcal L_z^\dagger(X^\dagger X)
-\mathcal L_z^\dagger(X^\dagger)X
-X^\dagger\mathcal L_z^\dagger(X)
=\sum_\alpha[L_\alpha,X]^\dagger[L_\alpha,X].
```

If $`\mathcal L_z^\dagger(X)=i\nu X`$ with real $`\nu`$, its stationary expectation makes the left side zero. Faithfulness forces every commutator on the right to vanish. The full jump algebra then makes $`X`$ scalar and $`\nu=0`$. A Jordan block on the imaginary axis is excluded by boundedness of the quantum Markov semigroup. The stationary eigenvalue is consequently simple and separated from all other eigenvalues by a strictly positive decay rate at each fixed dimension.

No dimension-independent lower bound on that stationary spectral gap is assumed in the recycling theorem. Its perturbation estimates use the explicitly bounded killed inverse instead.

## 5. Tilted generator and the renewal equation

Introduce the signed-count tilted generator

```math
\mathcal L_z(\chi)
=\mathcal L_z
+(e^\chi-1)\mathcal C_+
+z(e^{-\chi}-1)\mathcal I_-.
```

For real $`\chi`$ near zero,

```math
\mathbb E_\rho[e^{\chi N(t)}]
=\operatorname{Tr}e^{t\mathcal L_z(\chi)}(\rho).
```

Under the faithfulness conditions just proved, the eigenvalue issuing from zero is simple, analytic, and dominant near $`\chi=0`$. Denote it by $`\lambda(\chi)`$, with $`\lambda(0)=0`$. It gives

```math
\lambda'(0)=j,
\qquad
\lambda''(0)=D_N.
```

These cumulants can be identified without solving the full eigenproblem. Write

```math
\mathcal L_z(\chi)
=\mathcal K_z
+z(e^{-\chi}-1)\mathcal I_-
+e^\chi\mathcal C_+.
```

Because $`\mathcal C_+`$ has the rank-one form $`P_m\ell_+`$, an eigenvalue near zero satisfies

```math
1=e^\chi\ell_+
\left[\lambda(\chi)\mathbb I-\mathcal K_z
-z(e^{-\chi}-1)\mathcal I_-\right]^{-1}(P_m).
```

By the joint transform, this is exactly

```math
\boxed{
\mathbb E\!\left[e^{\chi Y-\lambda(\chi)T}\right]=1.
}
```

At $`\chi=0`$, differentiation with respect to the eigenvalue gives $`-\mu_z\ne0`$, so the implicit function is locally unique. Differentiating once and twice in $`\chi`$ gives

```math
\begin{aligned}
0&=\mathbb E[Y-\lambda'(0)T],\\
0&=\mathbb E[(Y-\lambda'(0)T)^2]
-\lambda''(0)\mathbb ET.
\end{aligned}
```

This proves the current and diffusion formulas in Section 3 and shows that the finite-rate theorem controls the first two cumulants of the same signed output record used in the entropy account.
