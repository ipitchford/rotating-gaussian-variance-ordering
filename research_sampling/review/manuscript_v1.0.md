---
title: 'Sharp variance ordering for rotating Gaussian samplers'
subtitle: 'A spectral criterion, an exact regularity boundary and arithmetic convergence rates'
date: '1 November 2026 — research manuscript, version 1.0'
author: 'Evidence Press research draft'
lang: en-GB
fontsize: 11pt
papersize: a4
geometry: margin=24mm
colorlinks: true
linkcolor: black
urlcolor: teal
toc: false
header-includes:
  - '\usepackage{amsmath,amssymb,mathtools,microtype,booktabs}'
  - '\DeclareMathOperator{\Var}{Var}'
  - '\DeclareMathOperator{\Cov}{Cov}'
  - '\DeclareMathOperator{\Rea}{Re}'
  - '\DeclareMathOperator{\Ran}{Ran}'
  - '\DeclareMathOperator{\diag}{diag}'
  - '\allowdisplaybreaks'
---

## Abstract

We study stationary kinetic Langevin dynamics with a Gaussian target and equal skew rotations in position and momentum. Duncan, Nüsken and Pavliotis (2017) proved local variance reduction for linear and quadratic position observables and conjectured an extension to all square-integrable observables. We prove a stronger ordering: increasing the rotation amplitude reduces the long-run variance of every such observable if and only if the dimensionless friction is at least $\sqrt2$. Equality between distinct amplitudes occurs exactly for rotation-invariant observables. The proof characterises universal variance ordering for rotated isotropic Gaussian processes through unimodality of their scalar spectral density. The literal finite-curvature formulation requires a correction: every square-integrable observable has a continuously differentiable variance, but finite second curvature is equivalent to an explicit weighted Hermite condition. We construct fractional and logarithmic cusps outside that domain. At large amplitudes, each non-invariant polynomial has a fourth-order variance remainder, whereas the sharp uniform rate is first order for commensurate rotations, one-third order for a concrete irrational rotation, and slower than every algebraic rate for a Liouville example. Fixed horizons and regularly spaced observations can violate the ordering; independent Poisson observation preserves it exactly. These are mathematical statements about stationary Gaussian sampling, with no claim of reduced numerical cost for general targets.

**Keywords:** kinetic Langevin dynamics; nonreversible sampling; asymptotic variance; Gaussian chaos; symmetric unimodality; small divisors.

## 1. The question and the contribution

An invariant distribution does not determine the accuracy of time averages obtained from a stochastic process. Correlations between successive observations also matter. One way to alter those correlations is to add a deterministic rotation that preserves the target distribution.

Duncan, Nüsken and Pavliotis (2017), hereafter DNP, introduced matched position and momentum perturbations of kinetic Langevin dynamics. Their Theorem 3 proves a local variance improvement for linear and quadratic position observables when $\gamma>\sqrt2$. The paragraph following their equation (27) conjectures the corresponding derivative statement for arbitrary $L^2$ observables. Nüsken's thesis (2018, p. 62) repeats that conjecture. DNP's Theorem 5 already identifies the large-amplitude limit as the variance of the rotation-invariant part of the observable.

We settle the variance-ordering question globally, and correct the regularity implicit in the derivative formulation. The distinction matters. A strictly decreasing even function can have a stationary maximum at zero without possessing a finite second derivative there. That behaviour occurs for explicit square-integrable observables in the model considered by DNP.

Our method uses classical ingredients: Gaussian Hermite expansions, Fourier transforms of covariance powers, and closure of symmetric unimodality under convolution. Breuer and Major (1983, pp. 428, 430) explicitly give the Hermite covariance and spectral-convolution identities. Lefèvre and Utev (2013) discuss and extend the classical convolution closure property. These Gaussian spectral expansions also appear in other applications, for example Muscinelli, Gerstner and Schwalger (2019, equations (37), (42)–(43)). At critical damping, the scalar spectral density belongs to the scaled Student family whose convolution formulas are studied by Berg and Vignat (2008). We do not claim those ingredients, or DNP's invariant-projection limit, as new.

The proposed contributions are an exact universal ordering criterion, the resulting sharp kinetic theorem, and the regularity and rate results proved below. Uniform variance convergence has earlier theory for drift-accelerated overdamped diffusions (Franke et al., 2021). Arithmetic effects on variance are also established in a different Gaussian-field setting: Lachièze-Rey (2022) studies excursion volumes over growing spatial windows with atomic spectral measures. Our convergence parameter is the kinetic rotation amplitude; the precise angular-gap constant, curvature domain and arithmetic operator rates concern that distinct problem.

The literature search was completed on 1 November 2026. It inspected the originating paper and thesis, related nonreversible-sampling work, and formula-level aliases across Gaussian spectral analysis and convolution theory. No earlier statement of the full results below was found within that search. This is a bounded priority assessment; the separate novelty report records the search boundary and remaining uncertainty.

## 2. Model and main theorem

Let $d\ge2$, let $J\in\mathbb R^{d\times d}$ satisfy $J^\top=-J$, and let $\gamma>0$. We consider

$$
\begin{aligned}
\mathrm dq_t&=(p_t-\mu Jq_t)\,\mathrm dt,\\
\mathrm dp_t&=(-q_t-\gamma p_t-\mu Jp_t)\,\mathrm dt
                 +\sqrt{2\gamma}\,\mathrm dW_t .
\end{aligned} \tag{1}
$$

Time and coordinates are normalised so that the harmonic frequency and the position and momentum variances are one. The stationary law is $\widehat\pi=\mathcal N(0,I_{2d})$, and the position marginal is $\pi=\mathcal N(0,I_d)$. We start the process in stationarity. An observable is a real function $f\in L^2(\pi)$ of position alone. Subtracting its mean changes none of the results, so we take $\pi(f)=0$.

Define its long-run variance by

$$
V_f(\mu)=\lim_{T\to\infty}T\Var\left(
\frac1T\int_0^T f(q_t)\,\mathrm dt\right). \tag{2}
$$

We prove existence of this limit directly. This convention is twice DNP's $\sigma_f^2$. We use the variance limit as the definition; no central limit theorem is needed in our proofs.

Write $U_\theta f(q)=f(e^{-\theta J}q)$. Let $\Pi_J$ denote the orthogonal projection in $L^2(\pi)$ onto the functions invariant under every $U_\theta$. It preserves centred functions and fixes constants.

**Theorem 1 (sharp global ordering).** Suppose $J\ne0$. The following are equivalent:

1. $\gamma\ge\sqrt2$.
2. For every real $f\in L^2(\pi)$ and every $0\le a<b$, $V_f(b)\le V_f(a)$.

When these conditions hold, equality at any one such pair occurs if and only if $f=\Pi_Jf$. Thus each non-invariant observable has strictly decreasing variance on $[0,\infty)$. The variance is even in $\mu$. If $0<\gamma<\sqrt2$, a linear observable has $V_f(\mu)>V_f(0)$ for all sufficiently small nonzero $\mu$.

The threshold includes $\gamma=\sqrt2$, although a linear observable then has zero second curvature at the origin. If $J=0$, all variances are constant for every $\gamma$, so the nonzero assumption is necessary for the equivalence.

Theorem 1 concerns the Gaussian model with exactly matched rotations. It does not assert the same ordering for general target distributions, arbitrary phase-space observables, or unmatched perturbations. Section 8 gives explicit observation-related boundaries.

## 3. A spectral characterisation for Gaussian processes

We first prove a statement that does not require a Markov process.

**Theorem 2 (spectral criterion).** Let $(X_t)_{t\in\mathbb R}$ be a centred, mean-square continuous, stationary Gaussian process in $\mathbb R^d$ satisfying

$$
\Cov(X_t,X_s)=r(t-s)I_d,\qquad r(0)=1,\qquad r\in L^1(\mathbb R).
$$

Fix a nonzero real skew matrix $J$, and put $Q_t^\mu=e^{-\mu tJ}X_t$. Use the Fourier convention

$$
S(\xi)=\widehat r(\xi)=\int_{\mathbb R}e^{-i\xi t}r(t)\,\mathrm dt .
$$

Every real centred $f\in L^2(\pi)$ has a finite variance limit (2), with $q$ replaced by $Q$. These limits are nonincreasing in $|\mu|$ for every such $f$ if and only if $S$ is nonincreasing on $[0,\infty)$. If $S$ is strictly decreasing there, the ordering is strict precisely for non-invariant observables.

### 3.1. Hermite and rotation decomposition

The process $Q^\mu$ is stationary because it is Gaussian with constant mean and covariance

$$
\Cov(Q_t^\mu,Q_s^\mu)=r(t-s)e^{-\mu(t-s)J}.
$$

Write $L^2_0(\pi)=\bigoplus_{n\ge1}\mathcal H_n$ for the orthogonal decomposition into position Hermite chaoses. Here $\mathcal H_n$ is the span of multivariate Hermite polynomials of total degree $n$. Each space is finite dimensional. The Mehler operator

$$
T_\rho f(x)=\mathbb E\big[f(\rho x+\sqrt{1-\rho^2}Z)\big],
\qquad Z\sim\pi,
$$

acts as multiplication by $\rho^n$ on $\mathcal H_n$, also for negative $\rho$. Orthogonal rotations preserve each chaos and commute with $T_\rho$.

Complexify each chaos and diagonalise the unitary group $U_\theta$. Let $E_{n,\omega}$ be its spectral projection with

$$
U_\theta E_{n,\omega}=e^{i\omega\theta}E_{n,\omega},
\qquad
a_{n,\omega}=\|E_{n,\omega}f_n\|_2^2.
$$

The index $\omega$ ranges over the finite set of rotation frequencies in degree $n$. These weights satisfy

$$
a_{n,\omega}\ge0,\quad a_{n,-\omega}=a_{n,\omega},\quad
\sum_{n,\omega}a_{n,\omega}=\|f\|_2^2,
\quad |\omega|\le n\|J\|. \tag{3}
$$

Both signs of a nonzero frequency are included in this convention; their weights are not counted twice elsewhere.

Joint Gaussian conditioning gives

$$
\mathbb E[f(Q_t^\mu)\mid Q_0^\mu=x]
=T_{r(t)}U_{\mu t}f(x).
$$

Orthogonality and (3) therefore give the covariance expansion

$$
C_f(t;\mu)=\sum_{n,\omega}a_{n,\omega}r(t)^n\cos(\mu\omega t). \tag{4}
$$

As a covariance normalised at zero, $|r(t)|\le1$. Consequently,

$$
|C_f(t;\mu)|\le\|f\|_2^2|r(t)|,
\qquad
\sum_{n,\omega}a_{n,\omega}\int_{\mathbb R}|r(t)|^n\,\mathrm dt
\le\|f\|_2^2\|r\|_1. \tag{5}
$$

These bounds justify all subsequent exchanges of sums and integrals. The stationary variance identity

$$
T\Var(\overline f_T)=2\int_0^T(1-t/T)C_f(t;\mu)\,\mathrm dt
$$

and dominated convergence prove existence of (2).

Since $r$ is continuous, positive definite and integrable, $S$ is a continuous nonnegative integrable spectral density and $\int S=2\pi$. Set $p=S/(2\pi)$ and

$$
S_n(\xi)=\widehat{r^n}(\xi)
=(2\pi)^{1-n}S^{*n}(\xi)=2\pi p^{*n}(\xi).
$$

We obtain the exact nonnegative expansion

$$
\boxed{\displaystyle V_f(\mu)=\sum_{n\ge1,\omega}
a_{n,\omega}S_n(\mu\omega).} \tag{6}
$$

Time-domain covariances can change sign. Their spectral densities in (6) remain nonnegative.

### 3.2. Convolution lemma and proof of the criterion

**Lemma 3.** The convolution of two even, nonnegative, integrable functions that are nonincreasing on $[0,\infty)$ has the same properties. If one is continuous and strictly decreasing, and the other is nonzero, their convolution is strictly decreasing on $[0,\infty)$.

**Proof.** Represent the second function by its superlevel intervals, using the layer-cake identity. For each interval radius $R>0$, convolution of the first function $a$ with its indicator gives

$$
H_R(x)=\int_{x-R}^{x+R}a(u)\,\mathrm du .
$$

If $a$ is continuous and strictly decreasing away from zero, then

$$
H_R'(x)=a(x+R)-a(x-R)<0\qquad(x>0),
$$

because $a$ is even and $|x-R|<x+R$. The weak version follows by the same interval comparison without differentiability. Integrate over the superlevel intervals. For a nonzero second function, positive radii occur on a set of levels of positive measure, which preserves strictness between any two distinct nonnegative arguments. $\square$

If $S$ is nonincreasing, Lemma 3 applies to every convolution power in (6), proving sufficiency in Theorem 2. Under strict decrease, every summand with $\omega\ne0$ and positive weight decreases strictly. Such a summand exists exactly when $f\ne\Pi_Jf$.

For necessity, choose a two-dimensional rotation plane of $J$ with nonzero speed $\lambda>0$, and a unit linear observable in that plane. Its covariance is $r(t)\cos(\lambda\mu t)$ and its variance is $S(\lambda\mu)$. As $\mu$ traverses $[0,\infty)$, so does $\lambda\mu$. Universal monotonicity therefore forces monotonicity of $S$. $\square$

## 4. Applying the criterion to kinetic Langevin dynamics

The drift matrix of (1) is

$$
B_\mu=\begin{pmatrix}\mu J&-I\\I&\gamma I+\mu J\end{pmatrix}
=B_0+\mu\diag(J,J).
$$

The two summands commute. Also $B_\mu+B_\mu^\top=2\diag(0,\gamma I)$, and all drift eigenvalues have positive real parts. Thus $I_{2d}$ is the stationary covariance, and

$$
\Cov(q_t,q_0)=r_\gamma(t)e^{-\mu tJ},
\quad r_\gamma''+\gamma r_\gamma'+r_\gamma=0,
\quad r_\gamma(0)=1,\quad r_\gamma'(0)=0. \tag{7}
$$

The scalar covariance decays exponentially, allowing a polynomial prefactor at $\gamma=2$. Its Laplace transform is

$$
R_\gamma(s)=\frac{s+\gamma}{s^2+\gamma s+1}.
$$

Extending $r_\gamma$ evenly, we find

$$
S_\gamma(\xi)=2\Rea R_\gamma(i\xi)
=\frac{2\gamma}{\xi^4+(\gamma^2-2)\xi^2+1}, \tag{8}
$$

and

$$
S_\gamma'(\xi)=
\frac{-4\gamma\xi(2\xi^2+\gamma^2-2)}
{[\xi^4+(\gamma^2-2)\xi^2+1]^2}. \tag{9}
$$

For $\gamma\ge\sqrt2$, (9) is strictly negative for every $\xi>0$. Theorem 2 proves the positive direction of Theorem 1, including its equality statement.

Conversely, the unit linear observable used in the necessity argument has

$$
V_f(\mu)=\frac{2\gamma}
{1+(\gamma^2-2)(\lambda\mu)^2+(\lambda\mu)^4}. \tag{10}
$$

For $\gamma<\sqrt2$, this exceeds $V_f(0)=2\gamma$ whenever
$0<(\lambda\mu)^2<2-\gamma^2$. This proves the converse. At $\gamma=\sqrt2$, its leading decrease is fourth order, which explains why global strictness and negative second curvature have different endpoint conditions. $\square$

**General Gaussian targets.** Let the target have precision matrix $S>0$. In DNP's notation, take mass $M=S$, friction $\Gamma=\gamma S$, $J_2=SJ_1S$, and equal perturbation amplitudes. The change of variables

$$
\widetilde q=S^{1/2}q,\quad
\widetilde p=S^{-1/2}p,\quad
\widetilde J=S^{1/2}J_1S^{1/2}
$$

reduces the dynamics to (1). Apply Theorem 1 to $f(S^{-1/2}\widetilde q)$. This statement requires the specified preconditioning; it gives no uniform tolerance to covariance misspecification.

## 5. The exact regularity boundary

In this section $\gamma>0$ is arbitrary and $S_n=\widehat{r_\gamma^n}$. Thus the regularity statements also apply below the monotonicity threshold.

### 5.1. Moment and Fourier estimates

**Lemma 4.** For every nonnegative integer $k$, there is a finite $C_{\gamma,k}$ such that

$$
\int_0^\infty t^k|r_\gamma(t)|^n\,\mathrm dt
\le C_{\gamma,k}n^{-(k+1)/2}. \tag{11}
$$

Moreover,

$$
n^{(k+1)/2}\int_0^\infty t^kr_\gamma(t)^n\,\mathrm dt
\longrightarrow\int_0^\infty u^ke^{-u^2/2}\,\mathrm du. \tag{12}
$$

In particular,

$$
-S_n''(0)\sim\sqrt{2\pi}\,n^{-3/2},\qquad
\sqrt n S_n(\sqrt n x)\longrightarrow\sqrt{2\pi}e^{-x^2/2}, \tag{13}
$$

the latter uniformly over $x\in\mathbb R$.

**Proof.** The oscillator energy has derivative
$(r^2+(r')^2)'=-2\gamma(r')^2$. Since $r''(0)=-1$, its energy is strictly below one at every positive time. Hence $|r(t)|<1$ for $t>0$. At zero,

$$
r(t)=1-\tfrac12t^2+\tfrac\gamma6t^3+O(t^4).
$$

Choose $\delta>0$ so that $r(t)>0$ and $r(t)\le e^{-ct^2}$ on $[0,\delta]$. On the complement, $\rho=\sup_{t\ge\delta}|r(t)|<1$, and

$$
\int_\delta^\infty t^k|r(t)|^n\,\mathrm dt
\le\rho^{n-1}\int_\delta^\infty t^k|r(t)|\,\mathrm dt .
$$

The small-time Gaussian bound proves (11). Substitution $u=\sqrt n\,t$ and dominated convergence prove (12). The even rescaled functions $r(|u|/\sqrt n)^n$ converge in $L^1(\mathrm du)$ to $e^{-u^2/2}$ by the same split; Fourier transformation proves the uniform assertion in (13). $\square$

### 5.2. First and second derivatives

**Theorem 5 (exact curvature domain).** Every real $f\in L^2(\pi)$ has $V_f\in C^1(\mathbb R)$ and $V_f'(0)=0$. Define

$$
\mathcal Q_J(f)=\sum_{n,\omega}a_{n,\omega}\omega^2 n^{-3/2}. \tag{14}
$$

The following are equivalent: $\mathcal Q_J(f)<\infty$; $V_f$ has a finite ordinary second derivative at zero; and $V_f\in C^2(\mathbb R)$. Under these conditions,

$$
V_f''(\mu)=-2\sum_{n,\omega}a_{n,\omega}\omega^2
\int_0^\infty t^2r_\gamma(t)^n\cos(\mu\omega t)\,\mathrm dt . \tag{15}
$$

If $\mathcal Q_J(f)=\infty$, then

$$
\frac{V_f(\mu)-V_f(0)}{\mu^2}\longrightarrow-\infty
\quad\text{as }\mu\to0. \tag{16}
$$

Equation (16) concerns the symmetric difference quotient. It does not, by itself, assert an extended derivative of $V_f'$.

**Proof.** By (3) and (11),

$$
|\omega S_n'(\mu\omega)|
\le2|\omega|\int_0^\infty t|r(t)|^n\,\mathrm dt
\le2\|J\|C_{\gamma,1}.
$$

The first-derivative series in (6) therefore converges uniformly, because the weights sum to $\|f\|_2^2$. Each term has derivative zero at zero. This proves the $C^1$ assertion. If (14) is finite, (11) with $k=2$ gives uniform convergence of the second-derivative series, proving sufficiency and (15).

For necessity, the possibility that $r(t)$ is negative must be handled. Decompose $r(t)^n=P_n(t)-N_n(t)$ into its nonnegative positive and negative parts. Every negative part lies in $[\delta,\infty)$ for the $\delta$ in Lemma 4, and

$$
\int_0^\infty t^2N_n(t)\,\mathrm dt\le B_\gamma\rho^{n-1}.
$$

Using $1-\cos x\le x^2/2$, its total contribution to

$$
\frac{V_f(0)-V_f(\mu)}{\mu^2}
=2\sum_{n,\omega}a_{n,\omega}
\int_0^\infty r(t)^n\frac{1-\cos(\mu\omega t)}{\mu^2}\,\mathrm dt
$$

is bounded uniformly in $\mu\ne0$ by

$$
B_\gamma\|J\|^2
\sup_{n\ge1}(n^2\rho^{n-1})\,\|f\|_2^2<\infty.
$$

The positive-part second moments are asymptotic to
$\sqrt{\pi/2}\,n^{-3/2}$ by (12). If (14) diverges, Fatou's lemma applied to the positive-part integrands makes their contribution diverge to $+\infty$. The bounded negative contribution cannot cancel it. This proves (16). A finite ordinary second derivative, together with $V_f'(0)=0$, would give a finite symmetric difference quotient, so (14) is necessary. $\square$

In spectral notation, $\mathcal Q_J(f)=\|N^{-3/4}R_Jf\|_2^2$, where $N$ is the positive Hermite number operator and $R_J=(Jq)\cdot\nabla$ is interpreted spectrally. A sufficient condition is $f\in D(N^{1/4})$, since $|\omega|\le n\|J\|$. It is not necessary: invariant components require no extra regularity.

**Curvature sign above the threshold.** For $\gamma>\sqrt2$, every $S_n''(0)<0$. For $n=1$ this follows from (8). For $n\ge2$, write $p=S_\gamma/(2\pi)$ and $h=p^{*(n-1)}$. Their smooth derivatives are negative on $(0,\infty)$. To verify this statement inductively, if $g$ is an even smooth density with $g'(y)<0$ for $y>0$, then

$$
(p*g)'(x)=\int_0^\infty g'(y)\,[p(x-y)-p(x+y)]\,\mathrm dy<0
\qquad(x>0).
$$

The bracket is positive because $|x-y|<x+y$ and $p$ is even and strictly decreasing. Integration by parts now gives

$$
(p*h)''(0)=-\int_{\mathbb R}p'(y)h'(y)\,\mathrm dy<0.
$$

The integrability and boundary conditions follow from the rational decay of $p$ and its derivatives and their convolution representations. The same argument applies for $n\ge2$ when $\gamma=\sqrt2$; only $n=1$ then has zero curvature. Thus, for $\gamma>\sqrt2$, the derivative formulation conjectured by DNP is valid precisely on the finite-curvature domain (14), with strict negativity for non-invariant $f$. Global strict ordering needs only $f\in L^2$.

### 5.3. Explicit fractional and logarithmic cusps

Take $d=2$ and $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$. Set

$$
\phi_n(q)=\frac{\Rea(q_1+iq_2)^n}{\sqrt{2^{n-1}n!}},\qquad n\ge1.
$$

These are real orthonormal chaos elements. The polynomial is homogeneous and harmonic, so its Hermite degree is $n$; rotational symmetry and
$\mathbb E|q_1+iq_2|^{2n}=2^n n!$ give the normalisation. Its angular frequencies are $\pm n$, and its covariance is $r(t)^n\cos(n\mu t)$.

For $1<p\le3/2$, define the $L^2$-convergent series

$$
f_p=\sum_{m\ge1}m^{-p/2}\phi_{2m},\qquad
\|f_p\|_2^2=\zeta(p). \tag{17}
$$

**Proposition 6.** For every $\gamma>0$ and $1<p<3/2$,

$$
V_{f_p}(0)-V_{f_p}(\mu)
\sim\frac{\sqrt\pi\,\Gamma(3/2-p)}{p-1/2}|\mu|^{2p-1}, \tag{18}
$$

and

$$
V_{f_p}'(\mu)\sim-2\sqrt\pi\,\Gamma(3/2-p)
\operatorname{sgn}(\mu)|\mu|^{2p-2}. \tag{19}
$$

At $p=3/2$,

$$
\begin{aligned}
V_{f_{3/2}}(0)-V_{f_{3/2}}(\mu)
&\sim2\sqrt\pi\,\mu^2\log(1/|\mu|),\\
V_{f_{3/2}}'(\mu)&\sim-4\sqrt\pi\,\mu\log(1/|\mu|).
\end{aligned} \tag{20}
$$

**Proof.** Formula (6) gives $V_{f_p}(\mu)=\sum m^{-p}S_{2m}(2m\mu)$. The even powers of $r$ make all time kernels nonnegative. With $h=\mu^2$ and $x=mh$, (13) gives the locally uniform scaled difference

$$
\frac{S_{2m}(0)-S_{2m}(2m\mu)}{|\mu|}
\longrightarrow\sqrt{\pi/x}(1-e^{-x}).
$$

Lemma 4 and the two elementary cosine bounds give

$$
0\le S_{2m}(0)-S_{2m}(2m\mu)
\le C\min\{m^{-1/2},\mu^2m^{1/2}\}. \tag{21}
$$

After rescaling, the summands are dominated by a constant times
$\min(x^{1/2-p},x^{-p-1/2})$. Its integral is finite at zero and infinity for the stated range. Splitting the Riemann sums into a compact interval and two tails yields

$$
\lim_{\mu\to0}\frac{V_{f_p}(0)-V_{f_p}(\mu)}{|\mu|^{2p-1}}
=\sqrt\pi\int_0^\infty x^{-p-1/2}(1-e^{-x})\,\mathrm dx.
$$

Integration by parts evaluates this integral as the constant in (18). The derivative scaling follows by differentiating the Fourier integral after the $u=\sqrt n t$ substitution. In particular,
$nS_n'(\sqrt n x)\to-\sqrt{2\pi}x e^{-x^2/2}$ on compact sets. The bound

$$
|2mS_{2m}'(2m\mu)|\le C\min\{1,|\mu|\sqrt m\}
$$

supplies the integrable Riemann-sum envelope
$\min(x^{-p},x^{1/2-p})$, proving (19).

For $p=3/2$, split at $K=\lfloor\mu^{-2}\rfloor$. Replacing $1-\cos(2m\mu t)$ by its quadratic term for $m\le K$ creates total error $O(\mu^4K)=O(\mu^2)$, by (11) with $k=4$. Its main coefficient is asymptotic to $\sqrt\pi/m$, whose sum is $\sqrt\pi\log K$. The tail is $O(\mu^2)$ by (21). This proves the first part of (20). The cubic sine remainder and the first-derivative bound similarly give an $O(|\mu|)$ error for the derivative, proving the second part. $\square$

For example, $p=4/3$ gives a variance cusp of order $|\mu|^{5/3}$. These examples directly refute finite second differentiability for every $L^2$ observable. Their leading constants are independent of friction because the short-time covariance starts as $1-t^2/2$ for every $\gamma$.

The regularity is also sharp at first order. For (17) with $1<p<3/2$, the derivative is globally Hölder continuous of exponent $2p-2$, by summing
$m^{-p}\min(1,\sqrt m|\mu-\nu|)$; (19) rules out a larger exponent at zero. At $p=3/2$, this bound gives the small-increment modulus $O(\delta\log(1/\delta))$, where $\delta=|\mu-\nu|$; (20) rules out Lipschitz continuity at zero. For a single example with no positive Hölder exponent, take $\gamma\ge\sqrt2$,
$n_j=2^{2^j}$, and $f=\sum_{j\ge1}j^{-1}\phi_{n_j}$. At $\mu_j=n_j^{-1/2}$, the derivative local limit gives
$-V_f'(\mu_j)\ge c j^{-2}$ for large $j$, since every spectral derivative has the same sign. This exceeds every constant multiple of $\mu_j^\alpha$ along the sequence, for every $\alpha>0$, although Theorem 5 still gives $V_f\in C^1$.

## 6. Large amplitudes: polynomial and uniform rates

For any $\gamma>0$, the Riemann–Lebesgue lemma in (6), dominated using (5), gives

$$
\lim_{|\mu|\to\infty}V_f(\mu)=V_{\Pi_Jf}(0). \tag{22}
$$

This is DNP's known projection limit. We now quantify it. Define

$$
D_J(\mu)=\sup_{\substack{f\in L^2_0(\pi)\text{ real}\\\|f\|_2=1}}
\{V_f(\mu)-V_{\Pi_Jf}(0)\}
=\sup_{n,\omega\ne0}S_n(\mu\omega). \tag{23}
$$

The last equality follows by concentrating the spectral mass on a conjugate frequency pair. We define the empty supremum to be zero when $J=0$, so $D_0\equiv0$. The remainder is nonnegative, including when $\gamma<\sqrt2$.

### 6.1. Every fixed polynomial has fourth-order decay

**Proposition 7.** For a polynomial observable,

$$
V_f(\mu)-V_{\Pi_Jf}(0)
=\frac{2\gamma}{\mu^4}
\sum_{n,\omega\ne0}\frac{n a_{n,\omega}}{\omega^4}
+O_{f,J,\gamma}(|\mu|^{-6}). \tag{24}
$$

The leading coefficient is positive exactly when $f$ is non-invariant.

**Proof.** For fixed $n$, put $g_n(t)=r_\gamma(t)^n$ on $t\ge0$. Every derivative decays exponentially up to a polynomial factor. Also $g_n'(0)=0$ and $g_n'''(0)=n\gamma$. Six integrations by parts in the cosine transform give
$S_n(\xi)=2n\gamma\xi^{-4}+O_{n,\gamma}(|\xi|^{-6})$. A polynomial has only finitely many chaos components and frequencies, so summing gives (24). $\square$

### 6.2. Exact uniform rate for commensurate rotations

Let $G_J$ be the additive subgroup of $\mathbb R$ generated by the positive rotation speeds of $J$. The union of all chaos frequencies equals $G_J$: positive and negative eigenvectors in symmetric tensor powers realise every integer combination. If $G_J$ is discrete and $J\ne0$, write $G_J=\omega_*\mathbb Z$, where $\omega_*>0$. This is exactly the case of commensurate nonzero rotation speeds.

**Theorem 8.** For every $\gamma>0$ and every fixed finite-dimensional $J$, $D_J(\mu)\to0$ as $|\mu|\to\infty$. If $G_J=\omega_*\mathbb Z$ with $\omega_*>0$, then

$$
\boxed{\displaystyle
D_J(\mu)\sim\frac{\sqrt{2\pi/e}}{|\mu|\omega_*}.} \tag{25}
$$

**Proof.** Lemma 4 gives $S_n(\xi)\le C_\gamma n^{-1/2}$ uniformly in $\xi$. High degrees are therefore uniformly small. Each bounded set of degrees contains finitely many nonzero frequencies, and their transforms vanish at infinity. This proves $D_J\to0$ without any arithmetic assumption.

To obtain the exact constant, strengthen the scaling in (13). Set
$g_n(u)=r_\gamma(|u|/\sqrt n)^n$. The proof of Lemma 4 also gives

$$
g_n\longrightarrow e^{-u^2/2}\quad\text{in }W^{1,1}(\mathbb R).
$$

Indeed, near zero the derivatives converge to $-u e^{-u^2/2}$ and are bounded by $C|u|e^{-cu^2}$. Outside $|u|\le\delta\sqrt n$, their $L^1$ norm is at most
$2n\rho^{n-2}\int_\delta^\infty|rr'|\,\mathrm dt$, which tends to zero. Fourier transformation of the derivatives yields

$$
\sup_{x\in\mathbb R}\left|x\left[
\sqrt n S_n(\sqrt n x)-\sqrt{2\pi}e^{-x^2/2}
\right]\right|\longrightarrow0. \tag{26}
$$

For $\omega\ne0$, set $x=|\mu\omega|/\sqrt n$. The expression
$|\mu|\omega_*S_n(\mu\omega)$ equals
$(\omega_*/|\omega|)x\sqrt n S_n(\sqrt n x)$.
For sufficiently large $n$, (26) bounds it by
$\max_{x\ge0}\sqrt{2\pi}x e^{-x^2/2}+o(1)=\sqrt{2\pi/e}+o(1)$, uniformly in the frequencies. Every finite set of low degrees contributes $o(1)$ after multiplication by $|\mu|$, by the fixed-degree tail used in Proposition 7. This proves the upper bound in (25).

The frequency $\omega_*$ occurs in some degree $n_0$ and in every degree $n_0+2k$: append one positive and one negative eigenvector from any rotation plane to a nonzero symmetric tensor. Choose such a degree nearest to $(\mu\omega_*)^2$. The local limit (13), evaluated at $x\to1$, gives the matching lower bound. $\square$

For $\gamma\ge\sqrt2$ there is also a simple bound at every nonzero amplitude. Every symmetric decreasing probability density $h$ satisfies $h(x)\le1/(2|x|)$, by integrating over $[-|x|,|x|]$. Applying this to $S_n/(2\pi)$ gives

$$
0\le V_f(\mu)-V_{\Pi_Jf}(0)
\le\frac{\pi}{|\mu|}
\sum_{n,\omega\ne0}\frac{a_{n,\omega}}{|\omega|}. \tag{27}
$$

When a gap $\omega_*$ holds, the right side is at most
$\pi\|f-\Pi_Jf\|_2^2/(|\mu|\omega_*)$. Formula (25) sharpens its asymptotic constant.

The observable attaining the lower scale in (25) changes with $\mu$ and has degree of order $\mu^2$. Thus (24) and (25) address different quantifiers: one fixed polynomial versus the worst unit-norm $L^2$ observable at each amplitude.

## 7. Arithmetic rates and small divisors

There need not be a positive angular gap when several rotation speeds are incommensurate. This changes the uniform rate without destroying convergence.

**Proposition 9 (Diophantine bound).** Suppose there exist $c>0$ and $\tau\ge0$ such that every nonzero frequency in degree $n$ satisfies $|\omega|\ge c n^{-\tau}$. Then, for every $\gamma>0$,

$$
D_J(\mu)=O(|\mu|^{-1/(2\tau+1)}). \tag{28}
$$

**Proof.** The $W^{1,1}$ estimate used in (26), together with the finitely many remaining degrees, gives $|\xi|S_n(\xi)\le C_\gamma$ uniformly in $n,\xi$. Combining it with Lemma 4 gives

$$
S_n(\mu\omega)\le C\min\{n^{-1/2},n^\tau/|\mu|\}.
$$

Split the degrees at $n\asymp|\mu|^{2/(2\tau+1)}$ to obtain (28). $\square$

**A sharp irrational example.** Let $d=4$ and let the two rotation speeds be $1$ and $\sqrt2$. Every degree-$n$ frequency is $a+b\sqrt2$ with integers $|a|+|b|\le n$. If it is nonzero, then

$$
|a+b\sqrt2|\ge\frac1{|a-b\sqrt2|}\ge\frac1{\sqrt2 n},
$$

because $a^2-2b^2$ is a nonzero integer. Proposition 9 gives $D_J(\mu)=O(|\mu|^{-1/3})$.

For the lower bound, write $p_k+q_k\sqrt2=(1+\sqrt2)^k$, and put
$n_k=p_k+q_k$, $\omega_k=|p_k-q_k\sqrt2|=(1+\sqrt2)^{-k}$.
These frequencies occur in degree $n_k$. With
$\mu_k=\sqrt{n_k}/\omega_k$, we have $\mu_k\asymp n_k^{3/2}$ and bounded successive ratios $\mu_{k+1}/\mu_k$. For $\mu_k\le|\mu|<\mu_{k+1}$, the argument
$|\mu|\omega_k/\sqrt{n_k}$ remains in a fixed compact subset of $(0,\infty)$. The uniform local limit (13) then gives
$S_{n_k}(\mu\omega_k)\ge c n_k^{-1/2}\ge c'|\mu|^{-1/3}$ for large $k$. Hence

$$
D_J(\mu)=\Theta(|\mu|^{-1/3}) \tag{29}
$$

for this explicit four-dimensional example.

**No algebraic rate in general.** Let the two speeds instead be $1$ and a positive Liouville number, for example $\alpha=\sum_{j\ge1}10^{-j!}$. It admits positive integer approximants $p_k/q_k$ with increasing denominators and

$$
0<\omega_k=|q_k\alpha-p_k|<2q_k^{-k},\qquad n_k=p_k+q_k\asymp q_k.
$$

A unit real chaos element $\psi_k$ of degree $n_k$ has frequency pair $\pm\omega_k$. At $\mu_k=\sqrt{n_k}/\omega_k$, (13) gives

$$
D_J(\mu_k)\ge S_{n_k}(\sqrt{n_k})
\sim\sqrt{2\pi/e}\,n_k^{-1/2}.
$$

For every $\beta>0$, the quantity $\mu_k^\beta D_J(\mu_k)$ diverges. Therefore $D_J$ has no bound $O(|\mu|^{-\beta})$ for any $\beta>0$, despite tending to zero. The same obstruction holds for one fixed observable: after retaining distinct degrees, take
$f=c\sum_{k\ge1}k^{-1}\psi_k$ with unit $L^2$ norm. Each spectral term is nonnegative, so
$V_f(\mu_k)\ge c^2k^{-2}S_{n_k}(\sqrt{n_k})$; the same comparison proves failure of every algebraic rate. This example has $\Pi_Jf=0$.

## 8. Observation rules and the scope of the theorem

### 8.1. Phase-space observables

The position restriction is essential. For a unit momentum observable in a rotation plane of speed $\lambda$, the spectrum gives

$$
V_p(\mu)=(\lambda\mu)^2S_\gamma(\lambda\mu).
$$

This is zero at $\mu=0$ and positive otherwise. At zero rotation, the time integral of momentum is a difference of position endpoints. Thus Theorem 1 cannot be extended to every function of $(q,p)$.

### 8.2. A fixed finite horizon

Take $\gamma=2$, the standard planar rotation, $f(q)=q_1$, and horizon $T=1$. Then $r(t)=(1+t)e^{-t}$ and

$$
W(\mu)=\Var\left(\int_0^1q_1(t)\,\mathrm dt\right)
=2\int_0^1(1-t^2)e^{-t}\cos(\mu t)\,\mathrm dt.
$$

With $z=-1+i\mu$, direct integration gives

$$
W(\mu)=2\Rea\left[-\frac1z+\frac{2e^z}{z^2}
+\frac{2(1-e^z)}{z^3}\right]. \tag{30}
$$

It follows that
$W(2\pi)\simeq0.01932908316$ and $W(3\pi)\simeq0.04028633541$.
The reversal can also be certified without floating-point reliance. At $u=k\pi$,

$$
W(k\pi)=
\frac{2u^4+16u^2-2+(4/e)(-1)^k(2-3u^2-u^4)}{(1+u^2)^3}.
$$

Using $9<\pi^2<10$ and $e<3$ gives

$$
W(3\pi)>\frac{70456}{2260713}
>\frac{1548}{50653}>W(2\pi).
$$

The difference between the middle fractions is
$69224044/114511895589>0$.
In contrast, the long-run variance is $4/(1+\mu^2)^2$, strictly decreasing. A long-run ordering therefore does not establish ordering at each observation horizon.

### 8.3. Regular observation and exact aliasing

For the same example, sample at interval $\Delta>0$. The asymptotic variance per recorded sample is

$$
\tau_\Delta^2(\mu)=1+2\sum_{k\ge1}(1+k\Delta)e^{-k\Delta}
\cos(k\Delta\mu).
$$

Putting $z=e^{-\Delta+i\Delta\mu}$ yields

$$
\tau_\Delta^2(\mu)=1+2\Rea\left[
\frac z{1-z}+\frac{\Delta z}{(1-z)^2}\right]. \tag{31}
$$

This is a nonconstant periodic function of $\mu$, of period $2\pi/\Delta$, and cannot be globally nonincreasing. In fact, the entire sampled Gaussian law repeats with this period. This is observation aliasing even under exact simulation, rather than an error caused by a numerical integrator. Multiplication by $\Delta$ converts (31) to variance per physical observation time.

### 8.4. Poisson observation preserves the ordering

Observe at arrival times of an independent Poisson process of rate $\lambda>0$, and average a fixed number $N$ of observations. Let $\tau_{\mathrm P,\lambda}^2(\mu)$ denote the limit of $N$ times the variance of this sample mean, averaging over both the stationary dynamics and the independent observation clock. The gap between observations $k$ positions apart has the Gamma$(k,\lambda)$ density. Since

$$
\sum_{k\ge1}\frac{\lambda^kt^{k-1}e^{-\lambda t}}{(k-1)!}=\lambda,
$$

integrable covariance and the covariance-sum identity give

$$
\boxed{\displaystyle
\tau_{\mathrm P,\lambda}^2(\mu)=\|f\|_2^2+\lambda V_f(\mu).} \tag{32}
$$

Thus independent Poisson observation preserves every ordering in Theorem 1 at every observation rate. Per mean elapsed time, the corresponding variance is
$V_f(\mu)+\|f\|_2^2/\lambda$. This extra term is an observation noise floor, so (32) does not establish superiority over regularly spaced observations at equal cost. The identity is a direct consequence of standard Poisson sampling, presented as an application of the theorem rather than a separate priority claim.

## 9. Reproducibility and interpretation

The accompanying deterministic verification script checks the covariance reduction against matrix exponentials, the linear and quadratic variance formulas against independent linear-system calculations, Fourier transforms against quadrature, and the finite-horizon and observation-rule examples. It also records exact polynomial fingerprints and the high-degree scaling in (13). The checks support the derivation and catch normalisation errors; the proofs above establish the infinite-dimensional and all-parameter assertions.

![Exact model calculations. The friction threshold governs the continuous-time long-run variance; higher chaoses inherit the ordering. Fixed horizons and regular observations can reverse it. Independent Poisson observation retains the ordering with an additional observation variance term. These curves illustrate proved formulas and are not Monte Carlo estimates.](figures/variance_landscape.pdf){width=100%}

The main theorem settles a stated question about Gaussian kinetic sampling, including every square-integrable position observable and every perturbation amplitude. The regularity result also identifies a failure in the literal unrestricted derivative formulation. The arithmetic results explain why a fast decay for each fixed polynomial does not control the worst observable uniformly.

These conclusions depend on a Gaussian joint law, a scalar unrotated position covariance after preconditioning, and matched rotations. A non-Gaussian extension would require control of couplings between chaos degrees or another replacement for (6). A numerical-efficiency result would require a specified discretisation, cost model and error tolerance. Neither follows from the present results. The manuscript has undergone separate AI proof checks and computational verification, but has not undergone external human peer review or formal proof-assistant verification.

## References

### Sampling and the originating question

Duncan, A. B., Lelièvre, T., & Pavliotis, G. A. (2016). Variance reduction using nonreversible Langevin samplers. *Journal of Statistical Physics, 163*, 457–491. <https://doi.org/10.1007/s10955-016-1491-2>

Duncan, A. B., Nüsken, N., & Pavliotis, G. A. (2017). Using perturbed underdamped Langevin dynamics to efficiently sample from probability distributions. *Journal of Statistical Physics, 169*, 1098–1131. <https://doi.org/10.1007/s10955-017-1906-8>

Franke, B., Hwang, C.-R., Ouled Said, A., & Pai, H.-M. (2021). A note on the asymptotic variance of drift accelerated diffusions. *Statistics & Probability Letters, 175*, 109128. <https://doi.org/10.1016/j.spl.2021.109128>

Nüsken, N. (2018). *Topics in sampling schemes based on Markov processes* [Doctoral thesis, Imperial College London]. Spiral. <https://doi.org/10.25560/63868>

### Spectral and convolution ingredients

Berg, C., & Vignat, C. (2008). Linearization coefficients of Bessel polynomials and properties of Student t-distributions. *Constructive Approximation, 27*, 15–32. <https://doi.org/10.1007/s00365-006-0643-6>

Breuer, P., & Major, P. (1983). Central limit theorems for non-linear functionals of Gaussian fields. *Journal of Multivariate Analysis, 13*(3), 425–441. <https://doi.org/10.1016/0047-259X(83)90019-2>

Lefèvre, C., & Utev, S. (2013). Convolution property and exponential bounds for symmetric monotone densities. *ESAIM: Probability and Statistics, 17*, 605–613. <https://doi.org/10.1051/ps/2012012>

Muscinelli, S. P., Gerstner, W., & Schwalger, T. (2019). How single neuron properties shape chaotic dynamics and signal transmission in random neural networks. *PLOS Computational Biology, 15*(6), e1007122. <https://doi.org/10.1371/journal.pcbi.1007122>

### Related arithmetic variance phenomena

Lachièze-Rey, R. (2022). *Diophantine Gaussian excursions and random walks* (arXiv:2104.07290, version 4). arXiv. <https://doi.org/10.48550/arXiv.2104.07290>

\newpage

## Appendix A. Explicit fingerprints and checks

At $\gamma=2$, the oscillator covariance is $r(t)=(1+t)e^{-t}$ for $t\ge0$. Hence

$$
S_n(\xi)=2\Rea\sum_{k=0}^n\binom nk\frac{k!}{(n-i\xi)^{k+1}}. \tag{33}
$$

The first zero-frequency values are $S_1(0)=4$, $S_2(0)=5/2$, and $S_3(0)=52/27$. The first spectral density is $4/(1+\xi^2)^2$; normalised by $2\pi$, it is a scaled Student distribution with three degrees of freedom. Berg and Vignat (2008) study the associated convolution family. These fingerprints locate classical distributional and spectral ingredients. The separate novelty report also records the exact connection between $nS_n(0)/2$ and the integral defining OEIS sequence A090878.

For $f=q_1$ and a unit planar rotation, (10) gives the following exact checks:

$$
\begin{array}{c|ccc}
&\mu=0&\mu=1/2&\mu=1\\\hline
\gamma=1&2&32/13&2\\
\gamma=\sqrt2&2\sqrt2&32\sqrt2/17&\sqrt2\\
\gamma=2&4&64/25&1
\end{array}
$$

The below-threshold row initially increases. The two other rows decrease, including the threshold itself. At zero perturbation, (10) gives $V_{q_1}(0)=2\gamma$; integrating (7) directly gives $\int_0^\infty r_\gamma(t)\,\mathrm dt=\gamma$, confirming the factor of two in (2).

For a real quadratic observable $f(q)=q^\top Kq-\operatorname{tr}K$, $K=K^\top$, let $A=\diag(K,0)$ and solve

$$
B_\mu^\top C+CB_\mu=A.
$$

Then $x^\top Cx-\operatorname{tr}C$ solves the Poisson equation for $f$, and Wick's identity gives $V_f(\mu)=4\operatorname{tr}(AC)$. This is an independent finite-dimensional check on the chaos expansion. It is not used to infer the result for general $L^2$ observables.
