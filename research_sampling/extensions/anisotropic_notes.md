# Matrix friction and anisotropic kinetic variance ordering

Research notes, 1 November 2026. These are an extension to the scalar-covariance theorem in the main manuscript. The principal additional result is an exact matrix criterion that allows the precision and friction matrices to fail to commute. Formula-first prior-art checks are recorded in `anisotropic_target.yaml`; the independent extension novelty audit is in `../review/extension_novelty.md` when completed.

## 1. Exact scope and main theorem

Let \(K,\Gamma\in\mathbb R^{d\times d}\) be symmetric positive definite, and let \(J^T=-J\). Assume

\[
[J,K]=[J,\Gamma]=0. \tag{1}
\]

We do **not** require \([K,\Gamma]=0\). Consider the stationary unit-mass process

\[
\begin{aligned}
dq_t&=(p_t-\mu Jq_t)\,dt,\\
dp_t&=(-Kq_t-\Gamma p_t-\mu Jp_t)\,dt+\sqrt{2\Gamma}\,dW_t.
\end{aligned} \tag{2}
\]

Its invariant law is \(\mathcal N(0,K^{-1})\otimes\mathcal N(0,I)\). For a real position observable \(f\in L^2(\mathcal N(0,K^{-1}))\), let

\[
V_f(\mu)=\lim_{T\to\infty}T\operatorname{Var}\!\left(\frac1T\int_0^T f(q_t)\,dt\right).
\tag{3}
\]

This is the full CLT variance; it is twice the variance convention used in the originating DNP paper.

Define the symmetric matrices

\[
B=\Gamma-K\Gamma^{-1}-\Gamma^{-1}K,
\qquad
D=\Gamma^3-\Gamma K-K\Gamma=\Gamma B\Gamma.
\tag{4}
\]

**Theorem 1 (matrix criterion).** If \(D\succeq0\), then \(V_f(\mu)\) is nonincreasing in \(|\mu|\) for every real \(L^2\) position observable. For \(0\le\mu_1<\mu_2\), equality holds if and only if

\[
f(e^{tJ}q)=f(q)\quad\text{in }L^2,\quad\text{for every }t\in\mathbb R.
\tag{5}
\]

If \(J\) is invertible, the following statements are equivalent:

1. \(D\succeq0\).
2. \(V_f\) is nonincreasing in \(|\mu|\) for every real \(L^2\) position observable.
3. \(V_f(\mu)\le V_f(0)\) for every real linear position observable and every \(\mu\) in a neighbourhood of zero.

No necessity assertion is made here for an arbitrary singular \(J\). Its zero-frequency position block is not tested by linear observables under rotation.

The proof is organised so that the only genuinely matrix-valued step is transparent. We first identify when the position spectral density decreases in Loewner order, then show this property survives the tensor convolution that gives every Gaussian chaos spectrum.

## 2. Stability, stationary covariance and the matrix spectrum

For \(\mu=0\), the deterministic system is \(\ddot q+\Gamma\dot q+Kq=0\). Its energy \((q^TKq+p^Tp)/2\) has derivative \(-p^T\Gamma p\). The corresponding first-order matrix has all eigenvalues in the open left half-plane. One direct verification is to take an eigenpair \(\lambda,q\ne0\) of the second-order pencil. The scalar identity

\[
\lambda^2\|q\|^2+\lambda q^*\Gamma q+q^*Kq=0
\]

has positive real coefficients. A real root is negative; if \(\operatorname{Im}\lambda\ne0\), its imaginary part gives \(\operatorname{Re}\lambda=-q^*\Gamma q/(2\|q\|^2)<0\). Thus all covariance functions decay exponentially, allowing a polynomial prefactor in the non-diagonalisable case. The covariance \(\operatorname{diag}(K^{-1},I)\) solves the Lyapunov equation. Assumption (1) makes the perturbation commute with the unperturbed drift and preserve this covariance. Equivalently, (2) is the unperturbed process viewed through the rotation \(e^{-\mu Jt}\), with the rotated driving noise having the same law.

Use the Fourier convention \(\widehat C(\xi)=\int_{\mathbb R}C(t)e^{-i\xi t}\,dt\). The standard transfer-function formula gives the physical-position spectrum

\[
S_q(\xi)=2H_\xi\Gamma H_\xi^*,
\qquad H_\xi=(K-\xi^2I+i\xi\Gamma)^{-1}.
\tag{6}
\]

The transfer-function identity itself is standard linear systems theory, not a novelty claim. What is useful here is its inverse. Put \(A_\xi=K-\xi^2I\). Then

\[
\begin{aligned}
(H_\xi\Gamma H_\xi^*)^{-1}
&=(A_\xi-i\xi\Gamma)\Gamma^{-1}(A_\xi+i\xi\Gamma)\\
&=A_\xi\Gamma^{-1}A_\xi+\xi^2\Gamma\\
&=K\Gamma^{-1}K+\xi^2B+\xi^4\Gamma^{-1}
=:Q(\xi).
\end{aligned} \tag{7}
\]

The imaginary cross terms cancel without requiring \(K\Gamma=\Gamma K\). In particular,

\[
S_q(\xi)=2Q(\xi)^{-1}. \tag{8}
\]

Whiten position by \(x=K^{1/2}q\), and set

\[
R(t)=\mathbb E[x_t x_0^T]\quad(\mu=0),
\qquad S(\xi)=2K^{1/2}Q(\xi)^{-1}K^{1/2}.
\tag{9}
\]

The spectrum \(S\) is real, symmetric, even, positive definite and \(O(|\xi|^{-4})\). Consequently \(R\) is symmetric and even. It commutes with \(J\), as do all the matrices in (7). The perturbed covariance is

\[
R_\mu(t)=e^{-\mu Jt}R(t)=R(t)e^{-\mu Jt}. \tag{10}
\]

By Cauchy–Schwarz, \(\|R(t)\|\le1\). It decays exponentially, so \(\int\|R(t)\|\,dt<\infty\).

**Lemma 2 (exact spectral criterion).** The matrix function \(S\) is nonincreasing in Loewner order on \([0,\infty)\) if and only if \(B\succeq0\). Under this condition,

\[
S(a)-S(b)\succ0\quad(0\le a<b),
\qquad -S'(b)\succ0\quad(b>0). \tag{11}
\]

**Proof.** The derivative of the inverse spectral pencil is

\[
Q'(\xi)=2\xi\bigl(B+2\xi^2\Gamma^{-1}\bigr). \tag{12}
\]

If \(B\succeq0\), this is positive definite for every \(\xi>0\). Inversion reverses Loewner order, and congruence by \(K^{1/2}\) preserves it, yielding (11). Conversely, decreasing \(S\) implies increasing \(Q\). Divide \(Q(\xi)-Q(0)\succeq0\) by \(\xi^2\) and let \(\xi\to0\) to obtain \(B\succeq0\). This also makes clear why semidefinite boundary cases still give strict decrease away from zero: the quartic term is positive definite. \(\square\)

## 3. Tensor convolution preserves Loewner unimodality

For matrix-valued functions acting on finite-dimensional real Hilbert spaces \(E\) and \(F\), respectively, define

\[
(A\star_\otimes B)(x)=\int_{\mathbb R}A(x-y)\otimes B(y)\,dy.
\tag{13}
\]

This is an operator on \(E\otimes F\); it is not matrix multiplication under a convolution sign.

**Lemma 3.** Suppose \(A,B\) are continuous, even, integrable, positive semidefinite matrix functions, nonincreasing in Loewner order on \([0,\infty)\). Suppose also that \(B\) is continuously differentiable and \(B(r)\to0\) as \(r\to\infty\). Then \(A\star_\otimes B\) is even, positive semidefinite and nonincreasing in Loewner order. If

\[
A(a)-A(b)\succ0\quad(0\le a<b),
\qquad -B'(r)\succ0\quad(r>0),
\tag{14}
\]

then \(-(A\star_\otimes B)'(x)\succ0\) for every \(x>0\), whenever differentiation below is justified. These hypotheses and the required integrability hold for all successive tensor convolutions used here.

**Proof.** The layer-cake representation, with positive semidefinite matrix layers, is

\[
B(y)=\int_{|y|}^\infty[-B'(r)]\,dr.
\]

Substitution and Fubini give

\[
(A\star_\otimes B)(x)
=\int_0^\infty
\left(\int_{x-r}^{x+r}A(u)\,du\right)\otimes[-B'(r)]\,dr.
\tag{15}
\]

For \(x,r>0\),

\[
\frac d{dx}\int_{x-r}^{x+r}A(u)\,du
=A(x+r)-A(x-r)\preceq0,
\tag{16}
\]

because \(x+r>|x-r|\) and \(A\) is even. Tensor products of positive semidefinite operators remain positive semidefinite. Integrating (16) tensor \(-B'(r)\) proves the assertion. Under (14), each such integrand is negative definite for \(r>0\), so the derivative is negative definite. Fubini can be justified first in scalar quadratic forms by positivity; boundedness of \(A\) and integrability of \(\|B'\|\) justify differentiation. For \(B=S\), monotonicity gives \(\int_0^\infty\|S'(r)\|dr\le\operatorname{tr}S(0)<\infty\). The convolution remains bounded and continuous, and induction is therefore valid. No commutation between \(A(x)\), \(A(y)\), \(B(x)\) and \(B(y)\) is required. \(\square\)

This is the tensor version of the elementary layer-cake proof for convolution of symmetric unimodal scalar functions. We do not claim historical novelty for the underlying argument. Its utility is that it handles spectra at different frequencies that are not simultaneously diagonalisable.

## 4. Gaussian chaos proof of sufficiency and strictness

Work with the whitened position law \(\nu=\mathcal N(0,I)\). Let \(I_n\) denote the Wick isometry from the symmetric tensor space \(\operatorname{Sym}^n(\mathbb R^d)\) into the \(n\)th Hermite chaos, normalised so that

\[
\|I_n(u)\|_{L^2(\nu)}^2=\|u\|^2.
\]

After centring \(f\), write \(f=\sum_{n\ge1}I_n(u_n)\), with \(\sum_n\|u_n\|^2=\|f\|_2^2\). For a jointly standard Gaussian pair with cross-covariance \(R(t)\), Wick contraction gives the chaos covariance operator

\[
R(t)^{\odot n}=R(t)^{\otimes n}|_{\operatorname{Sym}^n}.
\tag{17}
\]

Its spectral density is

\[
\mathcal S_n(\xi)
=(2\pi)^{1-n}
P_n\bigl(S\star_\otimes\cdots\star_\otimes S\bigr)(\xi)P_n
\big|_{\operatorname{Sym}^n},
\tag{18}
\]

where there are \(n\) factors and \(P_n\) is orthogonal symmetrisation. The unsymmetrised convolution commutes with permutations of the tensor factors, so (18) is also the restriction to the symmetric subspace. Every \(\mathcal S_n(\xi)\) is positive definite. Under \(B\succeq0\), Lemmas 2 and 3 show that it is even and strictly decreasing in Loewner order on \([0,\infty)\).

Complexify each chaos space. The induced rotation \((e^{tJ})^{\odot n}\) has finitely many frequencies \(\omega\). Decompose orthogonally

\[
u_n=\sum_\omega u_{n,\omega}.
\]

Every \(R(t)^{\odot n}\), and hence every \(\mathcal S_n(\xi)\), commutes with that rotation. Orthogonality of the angular subspaces and (10) give

\[
V_f(\mu)=\sum_{n\ge1}\sum_\omega
\langle u_{n,\omega},\mathcal S_n(\mu\omega)u_{n,\omega}\rangle.
\tag{19}
\]

The sign of the Fourier argument is immaterial because the spectra are even. Real observables have conjugate components at opposite frequencies.

The formula extends from polynomials to all \(L^2\) observables without additional regularity. Indeed,

\[
|\operatorname{Cov}(f(x_t),f(x_0))|
\le\sum_{n\ge1}\|u_n\|^2\|R(t)\|^n
\le\|f\|_2^2\|R(t)\|,
\tag{20}
\]

uniformly in \(\mu\). This is integrable, so covariance integration, chaos truncation and the large-\(T\) limit defining (3) are justified. Each summand in (19) is nonnegative, and the series is finite.

For \(0\le\mu_1<\mu_2\), each nonzero-frequency summand decreases strictly unless its coefficient vanishes. Zero-frequency terms are constant. Thus equality holds exactly when all \(u_{n,\omega}\) with \(\omega\ne0\) vanish, which is precisely (5). This proves sufficiency and the equality characterisation in Theorem 1.

## 5. Necessity, including an explicit witness

Assume \(J\) is invertible. Decompose physical position space into the mutually orthogonal real speed subspaces

\[
W_\lambda=\ker(J^2+\lambda^2I),\qquad \lambda>0.
\tag{21}
\]

All of \(K,\Gamma,B,Q(\xi),S_q(\xi)\) preserve these subspaces. For a real linear observable \(f(q)=a^Tq\), with \(a\in W_\lambda\), the sine contribution to its covariance vanishes: the product of the symmetric covariance with the commuting skew matrix \(J\) is skew. Consequently,

\[
V_f(\mu)=a^TS_q(\lambda\mu)a. \tag{22}
\]

If \(B\not\succeq0\), one speed subspace contains \(v\) with \(v^TBv<0\). Set \(Q_0=K\Gamma^{-1}K\) and \(a=Q_0v\). Expansion of (8) yields

\[
S_q(\xi)=2Q_0^{-1}-2\xi^2Q_0^{-1}BQ_0^{-1}+O(\xi^4),
\]

and therefore

\[
V_f''(0)=-4\lambda^2v^TBv>0. \tag{23}
\]

This violates the weak local inequality in Theorem 1. Thus even universal improvement against \(\mu=0\), restricted to linear observables and arbitrarily small amplitudes, forces the exact same matrix criterion.

### Independent isotropic blocks

Suppose \(K=\bigoplus_j k_j I\), \(\Gamma=\bigoplus_j\gamma_jI\), and \(J=\bigoplus_jJ_j\), where every \(J_j\ne0\). Then universal ordering holds if and only if

\[
\gamma_j^2\ge2k_j\quad\text{for every }j. \tag{24}
\]

Necessity follows by placing a linear observable in a nonzero rotating plane of any block violating its scalar condition; sufficiency follows from Theorem 1. Individual \(J_j\) may have a kernel here, because each scalar block is tested in one of its nonzero rotating planes. If an entire block has \(J_j=0\), (24) remains sufficient, but this argument does not show it necessary.

## 6. Exact design consequences for the friction matrix

### Fixed shape, variable scale

For \(\Gamma=\gamma G\), with \(G\succ0\),

\[
D=\gamma\bigl(\gamma^2G^3-GK-KG\bigr).
\]

Hence the exact threshold is

\[
\boxed{\gamma^2\ge\lambda_{\max}\!\left[G^{-3/2}(GK+KG)G^{-3/2}\right].}
\tag{25}
\]

The largest eigenvalue is positive: the matrix inside has trace \(2\operatorname{tr}(KG^{-2})>0\). Commuting symmetry (1) must still be respected. For replica rotation below, it holds for every base shape \(G\).

### A least admissible matrix in Loewner order

**Corollary 4.** Every \(\Gamma\succ0\) satisfying \(D\succeq0\) obeys

\[
\Gamma\succeq\sqrt{2K}. \tag{26}
\]

The matrix \(\Gamma_*=\sqrt{2K}\) is admissible, with \(D=0\). Thus it is the unique least admissible friction matrix in Loewner order. In particular,

\[
\min\operatorname{tr}\Gamma=\sqrt2\,\operatorname{tr}\sqrt K,
\]

with the unique minimiser \(\Gamma_*\).

**Proof.** Put \(H=\Gamma^2/2-K\). It solves the Lyapunov equation

\[
\Gamma H+H\Gamma=D.
\]

Its unique solution has the positive integral representation

\[
H=\int_0^\infty e^{-\Gamma t}D e^{-\Gamma t}\,dt\succeq0.
\tag{27}
\]

Therefore \(\Gamma^2\succeq2K\). Monotonicity of the positive square-root function gives (26). One may verify the required operator monotonicity directly from

\[
\sqrt A=\frac1\pi\int_0^\infty t^{-1/2}A(A+tI)^{-1}\,dt
\]

and the order-reversing property of inversion. Substituting \(\Gamma_*\) gives \(D=0\). Equality of traces under (26) forces equality of matrices. \(\square\)

This minimises friction only within the class guaranteeing universal rotation ordering. It does not minimise asymptotic variance at a chosen amplitude, mixing time, discretisation error, or computing cost.

The weaker squared inequality \(\Gamma^2\succeq2K\) is **not** sufficient when the matrices fail to commute. For example,

\[
\Gamma=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
K=\begin{pmatrix}1/4&-1/4\\-1/4&7/4\end{pmatrix}
\]

give

\[
\Gamma^2-2K=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\succeq0,
\qquad
D=\frac14\begin{pmatrix}2&3\\3&4\end{pmatrix},
\quad\det D=-\frac1{16}.
\tag{28}
\]

The admissible set should not be described as the entire upper Loewner cone above \(\sqrt{2K}\).

## 7. Noncommuting examples and exact formula fingerprints

Start with the base matrices

\[
K_0=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad
\Gamma_0=\begin{pmatrix}3&0\\0&4\end{pmatrix}.
\tag{29}
\]

They do not commute. Their criterion is

\[
B_0=\begin{pmatrix}5/3&-7/12\\-7/12&5/2\end{pmatrix},
\qquad
\lambda(B_0)=\frac{25\pm\sqrt{74}}{12}>0.
\tag{30}
\]

To realise a nonzero commuting rotation, duplicate the base space:

\[
K=\operatorname{diag}(K_0,K_0),\quad
\Gamma=\operatorname{diag}(\Gamma_0,\Gamma_0),\quad
J=\begin{pmatrix}0&-I_2\\I_2&0\end{pmatrix}.
\tag{31}
\]

The four-dimensional \(J\) is invertible and commutes with both matrices, while \([K,\Gamma]\ne0\). With \(x=\xi^2\), the base physical-position spectrum has the exact expression

\[
S_q(\xi)=
\frac{\begin{pmatrix}6x^2+60x+62&14x-34\\14x-34&8x^2+40x+38\end{pmatrix}}
{x^4+15x^3+61x^2+119x+25}.
\tag{32}
\]

In particular,

\[
S_q(0)=\frac1{25}\begin{pmatrix}62&-34\\-34&38\end{pmatrix},\quad
S_q(1)=\frac1{221}\begin{pmatrix}128&-20\\-20&86\end{pmatrix},\quad
S_q(2)=\frac1{2693}\begin{pmatrix}398&22\\22&326\end{pmatrix}.
\]

These matrices are not simultaneously diagonalisable; for example the upper off-diagonal entry of \([S_q(0),S_q(1)]\) is \(948/5525\). The whitened spectra also fail to commute: the same entry of \([S(0),S(1)]\) is \(8\sqrt5/221\). Thus diagonal scalar-mode reasoning does not prove the result.

For an exact failure witness, retain \(K_0\) and replace \(\Gamma_0\) by \(\operatorname{diag}(2,3)\). Then

\[
B_0=\begin{pmatrix}0&-5/6\\-5/6&1\end{pmatrix},\qquad
D_0=\begin{pmatrix}0&-5\\-5&9\end{pmatrix}.
\tag{33}
\]

The naive diagonal checks \(\gamma_i^2\ge2(K_0)_{ii}\) both hold, yet the actual criterion fails. Duplicate as in (31), and take \(f(q)=11q_1+13q_2\) in the first replica. Its exact variance is

\[
V_f(\mu)=
\frac{1498\mu^4+4312\mu^2+2950}
{\mu^8+3\mu^6+11\mu^4+34\mu^2+25}
=118+12\mu^2+O(\mu^4).
\tag{34}
\]

For verification, \(v=(3,2)^T\) gives \(v^TB_0v=-6\), and \(K_0\Gamma_0^{-1}K_0v=(11,13)^T\). Formula (23) then gives \(V_f''(0)=24\), agreeing with (34).

An alternative exact admissible example, already included in the computational verification file, is

\[
K=\operatorname{diag}(1,4)\otimes I_2,\qquad
\Gamma=\begin{pmatrix}4&1\\1&4\end{pmatrix}\otimes I_2,\qquad
J=I_2\otimes\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Here \(D=\begin{pmatrix}68&44\\44&44\end{pmatrix}\otimes I_2\succ0\), with base determinant \(1056\).

## 8. Replica rotation removes the symmetry restriction on the base target

The need for a nonzero \(J\) commuting with both \(K\) and \(\Gamma\) may appear restrictive on a single copy. Duplication supplies this symmetry for arbitrary base matrices. Let \(K_0,\Gamma_0\succ0\) be arbitrary \(r\times r\) matrices. Put

\[
K=I_2\otimes K_0,\quad
\Gamma=I_2\otimes\Gamma_0,\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\otimes I_r.
\tag{35}
\]

This \(J\) is invertible, and the exact criterion reduces to

\[
\Gamma_0^3-\Gamma_0K_0-K_0\Gamma_0\succeq0. \tag{36}
\]

At stationarity the two replicas are independent, each with the desired position law. Their trajectories are coupled by rotation.

The idea of nonreversible duplicated Langevin systems is established prior work: Ohzeki and Ichiki (2015), *Langevin dynamics neglecting detailed balance condition*, DOI [10.1103/PhysRevE.92.012105](https://doi.org/10.1103/PhysRevE.92.012105), explicitly constructs an overdamped duplicated system. Ichiki and Ohzeki (2021), *Stochastic dynamics without detailed balance condition connecting simple gradient method and Hamiltonian Monte Carlo*, [arXiv:2107.08633](https://arxiv.org/abs/2107.08633), Section VI, also explicitly discusses using both replicas to estimate expectations. The claim here is the exact kinetic matrix criterion and the resulting universal observable statements, not the invention of replica coupling or replica averaging.

Let a centred base observable have Hermite decomposition \(f=\sum_{n\ge1}f_n\), after position whitening. Write \(V_n\) for the unperturbed base asymptotic variance of \(f_n\). Then \(V_n>0\) whenever \(f_n\ne0\), and \(V_f^0=\sum_nV_n\). Define

\[
b_{2m}=\frac{\binom{2m}{m}}{4^m},\qquad b_{2m+1}=0.
\tag{37}
\]

### Using one replica

For the observable \(F(q^{(1)},q^{(2)})=f(q^{(1)})\), Theorem 1 gives strict decrease for every nonconstant \(f\), because a one-replica observable invariant under a quarter-turn would satisfy \(f(q^{(1)})=f(q^{(2)})\) for independent replicas and hence be constant. The high-amplitude limit is

\[
\lim_{|\mu|\to\infty}V_F(\mu)=\sum_{n\ge1}b_nV_n
\le\frac12V_f^0. \tag{38}
\]

For a nonzero centred observable, equality in the final bound holds exactly when it lies entirely in second chaos; the zero observable also gives equality. If \(f\) is odd, the limiting variance is zero.

### Averaging the same two replicas

For the more natural comparison at the same replica count, let

\[
F(q^{(1)},q^{(2)})=\frac{f(q^{(1)})+f(q^{(2)})}{2}.
\tag{39}
\]

At zero rotation \(V_F(0)=V_f^0/2\), while

\[
\lim_{|\mu|\to\infty}V_F(\mu)=\sum_{n\ge1}b_nV_n. \tag{40}
\]

Under (36), \(V_F\) decreases strictly between distinct nonnegative amplitudes if and only if \(f\) has a nonzero component outside the second chaos. Every centred quadratic observable gives a constant variance for this two-replica average, because the sum of its values is rotation invariant. Any purely odd observable has a limiting variance of zero. These are continuous-time statements; they do not assert a reduction in cost after discretisation.

**Proof of the replica formulas.** Write \(c_n(t)\) for the unperturbed base covariance of \(f_n\). The cross-covariance matrix between the first replica at time \(t\) and itself at zero is \(\cos(\mu t)R_0(t)\). Thus the covariance for a first-replica observable on chaos \(n\) is

\[
c_n(t)\cos^n(\mu t). \tag{41}
\]

For the average (39), the two cross-replica covariance matrices have opposite sine signs. The corresponding covariance is

\[
\begin{cases}
\tfrac12c_n(t)\cos^n(\mu t),&n\text{ odd},\\
\tfrac12c_n(t)\bigl[\cos^n(\mu t)+\sin^n(\mu t)\bigr],&n\text{ even}.
\end{cases} \tag{42}
\]

The constant Fourier coefficient of \(\cos^n\) is \(b_n\); that of \(\sin^{2m}\) is also \(b_{2m}\). All nonconstant Fourier terms vanish after covariance integration as \(|\mu|\to\infty\), by the Riemann–Lebesgue lemma. Bound (20) permits truncation and passage to the limit for general \(L^2\) observables. This proves (38) and (40), in fact for arbitrary positive definite friction; the matrix criterion is needed for monotonicity.

For the strictness statement in (39), on a single chaos the normalised inner product of the replica average with its image under a rotation through \(\theta\) is \(\cos^n\theta\) for odd \(n\), and \(\cos^n\theta+\sin^n\theta\) for even \(n\). At \(\theta=\pi/4\), this is less than one for every \(n\ne2\); the degree-two component is invariant for every \(\theta\). Orthogonality of chaoses and Theorem 1 give the stated characterisation. \(\square\)

## 9. Prior-art boundaries and intended use

The originating scalar conjecture is in Duncan, Nüsken and Pavliotis (2017), [DOI 10.1007/s10955-017-1906-8](https://doi.org/10.1007/s10955-017-1906-8), following Eq. (27). The present result genuinely leaves the scalar-covariance setting: neither the physical-position spectra in (32) nor their whitened counterparts need share an eigenbasis over frequency.

Chak, Kantas, Lelièvre and Pavliotis, *Optimal friction matrix for underdamped Langevin sampling*, [arXiv:2112.06844](https://arxiv.org/abs/2112.06844), optimises asymptotic variance with respect to friction for specified observables. Its quadratic calculations and commuting special cases concern a different optimisation objective. Corollary 4 above chooses the least friction that guarantees ordering in a separate rotation amplitude simultaneously for all position observables. It must not be presented as universally optimal friction for sampling.

Mashreghi, Nasri and Vishwakarma, *Functional Calculi, Positivity, and Convolution of Matrices*, [arXiv:2512.24575](https://arxiv.org/abs/2512.24575), uses a different object. Definition 3.1 defines the finite-array Jury product \((A\diamond B)_{ij}=\sum_{\ell\le i,\kappa\le j}a_{\ell\kappa}b_{i-\ell,j-\kappa}\). This is not the real-line tensor convolution (13). The title similarity does not identify a mathematical collision.

Formula and alias searches found no exact match for (4), (25), or the all-\(L^2\) theorem within the searched sources. That is a bounded literature-search result, not proof of novelty. The standard transfer spectrum, Gaussian chaos representation, scalar convolution argument and replica construction should be credited or described as established ingredients. The proposed contribution is their use to give an exact, noncommuting matrix boundary and universal observable ordering, with the design and replica consequences proved above.

The application remains exactly Gaussian and continuous time, with a symmetry-preserving matched rotation. The result gives a rigorous tuning rule and an analytic benchmark. It does not currently establish a robust non-Gaussian algorithm, an optimal numerical step size, or a reduction in work per effective sample.
