## Appendix B. Regularity and rates for matrix kinetic systems

This appendix extends the regularity and rate arguments to the matrix model of Section 8. Let $K,\Gamma>0$ be real symmetric matrices, let $J$ be real skew with $[J,K]=[J,\Gamma]=0$, and use stationary position law $\mathcal N(0,K^{-1})$. The results here require no friction-threshold inequality. A kernel of $J$ is allowed. Coordinates are whitened by $x=K^{1/2}q$, so the Hermite decomposition and its norm refer to standard Gaussian measure.

Write $C(t)=\Cov(x_t^0,x_0^0)$. It is real symmetric and even. Its short-time expansion on $t\ge0$ is

$$
C(t)=I-\tfrac12Kt^2+\tfrac16Lt^3+O(t^4),
\qquad L=K^{1/2}\Gamma K^{1/2}. \tag{B1}
$$

All its derivatives on the positive half-line decay exponentially. Also $\|C(t)\|<1$ for every $t>0$: the conditional covariance $I-C(t)C(t)^\top$ contains the strictly positive covariance of the noise reaching position over $(0,t)$. The position response to momentum noise is $sI+O(s^2)$ near zero, and $\Gamma>0$, which proves strict positivity in every direction. Consequently, for some $c,C,\delta>0$,

$$
e^{-Ct^2}I\preceq C(t)\preceq e^{-ct^2}I
\quad(0\le t\le\delta),\qquad
\rho=\sup_{|t|\ge\delta}\|C(t)\|<1. \tag{B2}
$$

Let $\mathscr C_n(t)=C(t)^{\otimes n}$ restricted to the symmetric tensor space, and let $\mathscr S_n=\widehat{\mathscr C_n}$. Use the isometric identification of that space with the $n$th Hermite chaos. These spectral operators are positive semidefinite and commute with the angular projections. If $f_{n,\omega}$ denotes a projected chaos component, then

$$
V_f(\mu)=\sum_{n,\omega}
\langle f_{n,\omega},\mathscr S_n(\mu\omega)f_{n,\omega}\rangle. \tag{B3}
$$

The convention includes both signs of each nonzero frequency. The bound $\|\mathscr C_n(t)\|\le\|C(t)\|^n\le\|C(t)\|$ makes the sum absolutely integrable for every $f\in L^2$.

### B.1. Exact regularity

**Proposition B1.** Every real square-integrable position observable has $V_f\in C^1(\mathbb R)$ and $V_f'(0)=0$. It has a finite ordinary second derivative at zero if and only if

$$
\sum_{n,\omega}\omega^2n^{-3/2}\|f_{n,\omega}\|_2^2<\infty. \tag{B4}
$$

This is also equivalent to $V_f\in C^2(\mathbb R)$. If (B4) diverges, $(V_f(\mu)-V_f(0))/\mu^2\to-\infty$ as $\mu\to0$.

**Proof.** The split in (B2) gives

$$
\int_0^\infty t^k\|C(t)\|^n\,\mathrm dt\le C_k n^{-(k+1)/2}.
$$

Since $|\omega|\le n\|J\|$, the first derivative of every matrix term in (B3) is bounded by a constant times $\|f_{n,\omega}\|_2^2$. The weighted second derivative is bounded by a constant times the summand in (B4). Uniform convergence proves the stated sufficiency and first differentiability.

For necessity, restrict the cosine-difference integral to $[0,\delta]$. Its kernels are positive semidefinite by (B2), and

$$
\int_0^\delta t^2\langle v,\mathscr C_n(t)v\rangle\,\mathrm dt
\ge c_1 n^{-3/2}\|v\|^2.
$$

Fatou's lemma therefore forces the positive small-time contribution to the divided difference to diverge when (B4) diverges. The absolute value of the complementary contribution is bounded by
$C_2\|J\|^2\sup_n(n^2\rho^{n-1})\|f\|_2^2$, using $1-\cos u\le u^2/2$. It cannot cancel the divergence. This also excludes a finite ordinary second derivative. $\square$

### B.2. A uniform matrix Fourier approximation

Define the positive operator on the symmetric tensor space

$$
A_n=\sum_{j=1}^n I^{\otimes(j-1)}\otimes K\otimes I^{\otimes(n-j)},
\qquad T_n=A_n/n.
$$

Its spectrum lies in the fixed interval $[\lambda_{\min}(K),\lambda_{\max}(K)]$. We claim

$$
\sup_{x\in\mathbb R}(1+|x|)\left\|
\sqrt n\,\mathscr S_n(\sqrt n x)
-\sqrt{2\pi}\,T_n^{-1/2}e^{-x^2T_n^{-1}/2}
\right\|\longrightarrow0. \tag{B5}
$$

Here the comparison operator depends on $n$; no convergence of $T_n$ is asserted.

To prove (B5), compare $C(|u|/\sqrt n)^{\otimes n}$ with $e^{-A_nu^2/(2n)}$. On $|u|\le\delta\sqrt n$, telescope the tensor factors and use (B1). The norm of the difference is bounded by
$C_3n^{-1/2}|u|^3e^{-c_3u^2}$. Differentiating the tensor products adds a bound
$C_4n^{-1/2}(|u|^2+|u|^4)e^{-c_4u^2}$ for the derivative difference. These bounds follow from
$C(t)-e^{-Kt^2/2}=O(t^3)$ and $C'(t)+(Kt)e^{-Kt^2/2}=O(t^2)$; the other tensor factors supply the Gaussian bound in (B2).

On the complement, the function and derivative integrals for the covariance tensor are bounded respectively by

$$
2\sqrt n\,\rho^{n-1}\int_\delta^\infty\|C(t)\|\,\mathrm dt,
\qquad
2n\rho^{n-2}\int_\delta^\infty\|C(t)\|\,\|C'(t)\|\,\mathrm dt.
$$

Both tend to zero; the comparison Gaussian has uniformly Gaussian tails. Thus the difference tends to zero in operator-norm $W^{1,1}$. Fourier transformation, and integration by parts for the frequency-weighted transform, prove (B5). Symmetric-tensor restriction can only decrease the operator norm.

### B.3. Exact angular-gap constant and polynomial asymptotics

Define $D_J$ as in (23), using the present Gaussian law and projection. It equals
$\sup_{n,\omega\ne0}\|\mathscr S_n(\mu\omega)|_{\mathcal H_{n,\omega}}\|$; real observables realise the same supremum by combining conjugate components.

**Proposition B2.** For any fixed $K,\Gamma>0$ and commuting skew $J$, $D_J(\mu)\to0$. If the nonzero angular frequency group is $\omega_*\mathbb Z$, then

$$
D_J(\mu)\sim\frac{\sqrt{2\pi/e}}{|\mu|\omega_*}. \tag{B6}
$$

The leading constant is independent of $K$ and $\Gamma$. The Diophantine condition in Proposition 9 still gives $D_J(\mu)=O(|\mu|^{-1/(2\tau+1)})$.

**Proof.** The moment estimate gives $\|\mathscr S_n\|_\infty\le Cn^{-1/2}$. This controls high degrees, and finitely many low-degree spectral matrices vanish at infinity. Thus $D_J\to0$.

For the upper bound in (B6), put $x=|\mu\omega|/\sqrt n$ in (B5). For every positive scalar $\kappa$,

$$
\sup_{x\ge0}x\kappa^{-1/2}e^{-x^2/(2\kappa)}=e^{-1/2}.
$$

Functional calculus for $T_n$ therefore bounds the high-degree part of $|\mu|\omega_*D_J(\mu)$ by $\sqrt{2\pi/e}+o(1)$. For each bounded degree, $|\xi|\mathscr S_n(\xi)\to0$, by the Riemann–Lebesgue lemma applied to its integrable derivative. These degrees contribute $o(1)$.

For the lower bound, $K$ and $J$ have a common complex orthonormal eigenbasis. Choose a nonzero symmetric tensor that has angular frequency $\omega_*$ and $A_{n_0}$ eigenvalue $a_0>0$. Append $k$ copies of a conjugate eigenvector pair. Its angular frequency remains $\omega_*$, its degree is $n_0+2k$, and its stiffness eigenvalue is $a_0+2k\kappa$, for some $\kappa>0$. Choose $k$ so that this last value is nearest to $(\mu\omega_*)^2$. The unweighted part of (B5) then gives the lower constant $\sqrt{2\pi/e}$. The tensor is nonzero because it corresponds to a product of nonzero linear polynomials.

Finally, (B5) gives $\sup_{n,\xi}|\xi|\|\mathscr S_n(\xi)\|<\infty$. Combining this with $Cn^{-1/2}$ gives the same degree split as Proposition 9. $\square$

For completeness, fixed polynomials have the matrix counterpart of (24). Let
$L_n=\sum_{j=1}^n I^{\otimes(j-1)}\otimes L\otimes I^{\otimes(n-j)}$. Six integrations by parts, using $\mathscr C_n'(0)=0$ and $\mathscr C_n'''(0)=L_n$, give

$$
V_f(\mu)-V_{\Pi_Jf}(0)
=\frac2{\mu^4}\sum_{n,\omega\ne0}
\frac{\langle f_{n,\omega},L_nf_{n,\omega}\rangle}{\omega^4}
+O_{f,K,\Gamma,J}(|\mu|^{-6}). \tag{B7}
$$

The leading coefficient is strictly positive exactly for non-invariant $f$, since every $L_n$ is positive definite. The scalar formulas are recovered by $K=I$, $\Gamma=\gamma I$.
