# Novelty gate: matrix friction and kinetic replica extension

**Search and assessment date:** 1 November 2026.  
**Scope:** Formula-level prior-art audit of the v1.1 matrix-friction theorem and its replica consequences, extended by Appendix A below to the matrix regularity and rate results in the manuscript's Appendix B. This supplements [the base report](../novelty_report.md); it does not replace a mathematical proof review or certify global priority.

**Decision:** The exact noncommuting matrix criterion remains a candidate contribution within the sources inspected. Replica duplication, including kinetic duplication and averaging both replicas, has explicit antecedents and must be credited. The proposed result should be presented as a sharp theorem for a specified Gaussian kinetic system, with friction-design and estimator consequences. No claim of a new general replica algorithm or universal computational improvement is supported.

## 1. Frozen claim and exclusions

The detailed formula record is [anisotropic_target.yaml](../extensions/anisotropic_target.yaml), SHA-256 **efc2bf252c536ec1a4245524bd5f49438af9633c5a24de6009c567401e000e3b** at this audit. The earlier comparison record is [extension_target.yaml](extension_target.yaml). The inspected proof notes are [anisotropic_notes.md](../extensions/anisotropic_notes.md). The target evolved from the scalar oscillator theorem to independent oscillator blocks and then to matrix spectra without assuming that precision and friction commute. Duplication supplies a commuting rotation for an arbitrary base pair of precision and friction matrices.

Let $K,\Gamma$ be real symmetric positive definite, $J^\top=-J$, and $[J,K]=[J,\Gamma]=0$. Consider

$$
dq=(p-\mu Jq)\,dt,\qquad
dp=(-Kq-\Gamma p-\mu Jp)\,dt+\sqrt{2\Gamma}\,dW.
$$

The stationary law is $\mathcal N(0,K^{-1})\otimes\mathcal N(0,I)$. The proposed theorem says that

$$
D=\Gamma^3-\Gamma K-K\Gamma\succeq0
$$

implies that the full stationary asymptotic variance $V_f(\mu)$ is nonincreasing in $|\mu|$ for every real square-integrable position observable. Equality between distinct nonnegative amplitudes occurs exactly for rotation-invariant observables. If $J$ is invertible, the condition is necessary even for universal local improvement of linear observables. Necessity for arbitrary singular $J$ is excluded.

Further claims are that $\sqrt{2K}$ is the least admissible friction in Loewner order, that a prescribed friction shape has an exact scalar threshold, and that replica rotation gives explicit surviving-chaos weights. The target excludes non-Gaussian guarantees, discretisation guarantees, fixed-time guarantees, computational-cost comparisons, and any identification of least admissible friction with observable-specific optimal friction. The standard transfer spectrum, Gaussian chaos, scalar unimodal convolution, elementary tensor layer-cake argument, and replica idea are not independent novelty claims.

## 2. Normalisation and object identity

| Object | Convention here | Comparison needed |
|---|---|---|
| Precision and mass | Position precision $K$; unit mass and temperature | A covariance denoted $\Sigma$ in friction papers is $K^{-1}$ |
| Variance | $V_f=\lim_{T\to\infty}T\operatorname{Var}(T^{-1}\int_0^T f(q_t)\,dt)$ | The originating DNP paper uses $V_f/2$ |
| Spectrum | $\widehat C(\xi)=\int_{\mathbb R}C(t)e^{-i\xi t}\,dt$ | Probability spectral density differs by $2\pi$ |
| Rotation | The same $-\mu J$ acts on position and momentum | Cross-Hamiltonian replica couplings are different displayed equations |
| Matrix ordering | Loewner order of the entire spectrum | Entrywise ordering differs; a decreasing scalar trace is insufficient |
| Matrix convolution | $\int A(x-y)\otimes B(y)\,dy$ | Neither ordinary matrix multiplication nor finite-array convolution |
| Friction selection | Least friction subject to universal rotation ordering | Different from minimising one observable's variance |
| Replica baseline | One-copy observable: $V_f(0)$; two-copy average: $V_f(0)/2$ | A comparison must retain the number of simulated copies |

In particular, the noncommuting case cannot be silently reduced to scalar oscillator coordinates by diagonalising $K$ alone. Whitening positions retains a matrix covariance.

## 3. Formula and matrix fingerprints

The same condition has the inverse-spectrum form

$$
B=\Gamma-K\Gamma^{-1}-\Gamma^{-1}K\succeq0,\qquad
\Gamma B\Gamma=D,
$$

and the physical-position spectral density is

$$
S_q(\xi)=2\left[K\Gamma^{-1}K+\xi^2B+\xi^4\Gamma^{-1}\right]^{-1}.
$$

These identities are the principal fingerprints. For $\Gamma=\gamma G$, the candidate threshold is

$$
\gamma^2\ge
\lambda_{\max}\!\left[G^{-3/2}(GK+KG)G^{-3/2}\right].
$$

The least-friction argument uses the classical positive inverse of a Lyapunov map:
$H=\Gamma^2/2-K$ solves $\Gamma H+H\Gamma=D$. Its application to this admissibility set is the proposed corollary; the Lyapunov representation itself is an ingredient.

One exact noncommuting test pair is

$$
K=\begin{pmatrix}2&1\\1&3\end{pmatrix},\quad
\Gamma=\begin{pmatrix}3&0\\0&4\end{pmatrix},\quad
B=\begin{pmatrix}5/3&-7/12\\-7/12&5/2\end{pmatrix}.
$$

The target records the denominator polynomial
$x^4+15x^3+61x^2+119x+25$, with $x=\xi^2$, and

$$
S_q(0)=\frac1{25}\begin{pmatrix}62&-34\\-34&38\end{pmatrix},\qquad
S_q(1)=\frac1{221}\begin{pmatrix}128&-20\\-20&86\end{pmatrix}.
$$

These are identity checks and search fingerprints, not evidence of novelty merely because an exact numeric query has no match. The scalar specialisation $K=1,\Gamma=2$ gives the classical squared-Lorentzian spectrum $4/(1+\xi^2)^2$; its collisions are detailed in the base report.

For two identical kinetic copies, use

$$
J=\begin{pmatrix}0&-I\\ I&0\end{pmatrix}.
$$

The surviving weights are the classical cosine moments

$$
b_{2m}=\binom{2m}{m}/4^m,\qquad b_{2m+1}=0.
$$

The weights are not a new sequence. The proposed consequence is their exact role in the long-run variance of this kinetic replica coupling. Both the first-copy observable and the two-copy mean have limit $\sum_n b_n V_{f_n}(0)$; their baselines differ by a factor of two. Pure centred quadratic observables make the two-copy mean invariant. The limit formula does not require the friction criterion; monotonicity does.

## 4. Alias map

| Mathematical object | Aliases searched or compared |
|---|---|
| Kinetic process | Underdamped Langevin, second-order Langevin, harmonic Langevin, replicated Langevin |
| Matrix spectrum | Dynamic stiffness, mechanical transfer spectrum, nonproportional damping, absence of resonance |
| Ordering mechanism | Matrix-valued symmetric unimodality, Loewner unimodality, operator-valued spectral density |
| Higher chaoses | Gaussian second quantisation, Hermite covariance, symmetric tensor powers, tensor convolution |
| Replica application | Ohzeki–Ichiki dynamics, duplicated systems, antisymmetric replica coupling, Hamiltonian bridge |
| Friction design | Optimal friction matrix, prescribed friction shape, Lyapunov inequality, quadratic matrix pencil |
| Limiting coefficients | Central binomial coefficients, circle average, cosine-power moments |

## 5. Executed search log

Live searches used two web engines and primary articles, author preprints and a primary seminar document. Searches for current Ohzeki work included a 365-day recency filter. The following are actual query strings or grouped executions from this extension audit; the base search log is separate.

| Query family | Executed queries | Consequence |
|---|---|---|
| Kinetic replicas | “Ohzeki” “Ichiki” “underdamped”; “duplicated” “Langevin” “underdamped”; “Ohzeki” “Ichiki” “kinetic”; “Langevin” “replica” “underdamped” variance coupling; “kinetic” “replicated” Langevin asymptotic variance | Found the OI family and kinetic Potts-model precedent |
| Duplicate systems | “duplicated systems” “Langevin” Hamilton Potts; “Ohzeki” “gauge” “2026” Fokker Planck | Followed primary slides to a paper supplement; inspected 2026 APS paper |
| Exact criterion | “Gamma^3” “Gamma K” Langevin; “Gamma^3” “Gamma” “Langevin”; “Langevin” “friction” “Gamma” “cube”; “friction” “Gamma” “K” “Loewner” | No same matrix criterion located in returned primary material |
| Mechanical aliases | “Gamma” “K” “non-resonance” damping matrix spectral; “damping matrix” “spectral density” “monotone”; “damping matrix” “monotonic” spectrum; “damping” “K” “C^-1” “resonance” matrix; “damping” “K C” “C K” “C^3” spectrum | Standard mechanical-transfer material; no verified theorem collision |
| Matrix convolution | “matrix” “spectral density” “unimodal” convolution tensor; “matrix-valued” “symmetric unimodal” convolution; “Loewner” “convolution” “unimodal”; “tensor convolution” “unimodality” | Screened finite-array matrix-convolution paper at its definition |
| Spectral aliases | “Langevin” “friction” “spectral density” “monotonic”; “matrix-valued” “spectral density” “decreasing”; “multivariate” “autoregressive” “unimodal” spectrum; “matrix-valued” “unimodal” Gaussian | No verified exact kinetic ordering theorem in returned results |
| Numeric and sequence fingerprints | “x^4+15x^3+61x^2+119x+25”; “Langevin” “replica” “central binomial” | No useful exact hit; cosine moments retained as classical |

Some broad queries returned irrelevant mathematical uses of “Gamma”, “Loewner” or “tensor”. Such results do not count as cleared antecedents. Formula indexing is incomplete, especially for older engineering literature.

## 6. Verified antecedents, collisions and differences

### A. The originating kinetic question

Duncan, Nüsken and Pavliotis, *Using Perturbed Underdamped Langevin Dynamics to Efficiently Sample from Probability Distributions* (2017), [primary article](https://doi.org/10.1007/s10955-017-1906-8). The relevant theorem and conjecture after Eq. (27), together with the Gaussian preconditioning and strong-rotation discussion, were inspected in the base audit. Their scalar matched setting is recovered by the new criterion; their known projection limit must remain credited. This extension adds the noncommuting precision/friction case and its sharp matrix condition. The source does not become an antecedent for that extension merely because it allows general matrices elsewhere in the dynamics.

### B. Universal amplitude ordering is known for reversible-base overdamped dynamics

Duncan, Lelièvre and Pavliotis, *Variance Reduction Using Nonreversible Langevin Samplers*, J. Stat. Phys. 163, 457–491 (2016), [full primary text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4939425/), [DOI](https://doi.org/10.1007/s10955-016-1491-2). Eq. (34) and Theorem 4 give a spectral sum with denominators $1+\alpha^2\lambda_n^2$ for all centred $L^2$ observables under their assumptions. Thus amplitude ordering and invariant-component limits are established concepts. Here the baseline already contains kinetic Hamiltonian transport; changing an additional matched rotation is a different comparison. The candidate matrix condition identifies when that kinetic comparison holds.

### C. Duplicate nonreversible systems

Ohzeki and Ichiki, *Langevin dynamics neglecting detailed balance condition*, Phys. Rev. E 92, 012105 (2015), [full preprint](https://arxiv.org/pdf/1307.0434), [DOI](https://doi.org/10.1103/PhysRevE.92.012105). The five-page primary text was inspected. Its baseline is explicitly overdamped; Eqs. (5), (7) and (8) couple the two systems through opposite signed gradients of the other potential while preserving the product Gibbs law. This is a direct antecedent for the broad replica-coupling idea. The proposed process instead has momentum-only noise and simultaneous rotations of position and momentum; the proposed contribution is the kinetic matrix theorem, not the use of an antisymmetric coupling.

### D. Hamiltonian interpretation and using both replicas

Ichiki and Ohzeki, *Stochastic dynamics without detailed balance condition connecting simple gradient method and Hamiltonian Monte Carlo* (2021), [full primary preprint](https://arxiv.org/pdf/2107.08633). Eqs. (20)–(24), the surrounding construction and the discussion in Section VI were inspected. Choosing a quadratic auxiliary Hamiltonian gives a momentum interpretation and a Hamiltonian limit. At finite coupling, the displayed process has direct damping and noise in both coordinate blocks. Section VI also discusses estimating the target expectation using both copies when their potentials agree. Replica averaging and the Hamiltonian connection therefore cannot be claimed as new. The inspected text does not give the matrix-friction condition or the exact kinetic Hermite-weight statement considered here.

### E. Explicit kinetic duplication and replica means already appear in 2023

Kobayashi, Nakagawa and Sasa, *Control of Metastable States by Heat Flux in the Hamiltonian Potts Model*, [full primary preprint and supplement](https://arxiv.org/pdf/2212.12289), version 3, 20 June 2023. Supplemental Section III.B.3, Eq. (S.71), and Eqs. (S.75)–(S.76) were inspected. The former gives coupled kinetic copies, and the latter explicitly averages them. With unit kinetic energy, the displayed position equations are $\dot q_1=p_1-p_2$, $\dot q_2=p_2+p_1$, while momentum receives cross-potential forces and its own friction/noise. This modifies the Hamiltonian cross blocks; it is not the simultaneous $-Jq,-Jp$ rotation studied here. The source is a firm collision for any broad claim of first kinetic duplication or first use of the two-copy mean.

The discovery lead was Michikazu Kobayashi's [primary seminar slides](https://www2.yukawa.kyoto-u.ac.jp/~japan-france/slide/Kobayashi.pdf), *Phase coexisting heat conduction in the Hamilton Potts model*, Japan–France seminar, 16 March 2023. Slide 16, physical PDF page 19, was visually inspected; it displays the same coupling and credits Ohzeki–Ichiki. The initial web-size retrieval failure was resolved by inspection of the downloaded primary document.

### F. The current OI Gaussian benchmark has a different drift and objective

Ohzeki, *Nonreversible gauge fields in Fokker–Planck dynamics: Supersymmetric Hamiltonians and learned finite forces*, Phys. Rev. Research 8, 033170 (10 August 2026), [full APS primary PDF](https://journals.aps.org/prresearch/pdf/10.1103/tg4c-7cnr), [DOI](https://doi.org/10.1103/tg4c-7cnr). The complete PDF was retrieved; Sections VII–VIII and Eqs. (77)–(97) were inspected in detail. The Gaussian benchmark has elliptic Ornstein–Uhlenbeck drift $(I-aS)K$ and direct full-coordinate noise. It studies spectral relaxation, a two-dimensional transition, and a finite-time objective with force cost. It is a close conceptual antecedent for anisotropic Gaussian nonreversible design, but its equations and optimisation objective differ from the kinetic universal-variance criterion. The full APS text, rather than an abstract alone, supports this distinction.

### G. “Optimal friction” is an existing but different optimisation problem

Chak, Kantas, Lelièvre and Pavliotis, *Optimal friction matrix for underdamped Langevin sampling*, [full primary preprint](https://arxiv.org/pdf/2112.06844). Eq. (1.1), the objective and derivative formula in Section 1, and Section 4.1 were inspected. Their goal optimises friction for a specified observable or finite collection. Proposition 4.5 gives $\Gamma=\Sigma^{-1/2}$ in its commuting quadratic setting, where $\Sigma$ is target covariance. The proposed $\sqrt{2K}$ minimises friction within a class guaranteeing ordering in a different parameter for all position observables. It is not a new solution of the same optimisation problem and should never be labelled universally optimal friction.

### H. A matrix-convolution title match is a different object

Mashreghi, Nasri and Vishwakarma, *Functional Calculi, Positivity, and Convolution of Matrices*, [full primary preprint](https://arxiv.org/pdf/2512.24575). Definition 3.1 on PDF page 5 defines the finite-array Jury product
$(A\diamond B)_{ij}=\sum_{\ell\le i,\,k\le j}a_{\ell k}b_{i-\ell,j-k}$.
Theorem 3.5 concerns positivity for that product. This is not the real-line tensor convolution used for Gaussian chaos spectra. The definition was inspected rather than clearing the paper by title or abstract. The scalar symmetric-unimodal convolution theorem and Gaussian tensor representation remain established ingredients, as documented in the base report.

## 7. Missingness and limits of this gate

The most relevant OI papers and the kinetic-replica supplement were inspected at the level of their equations. No outstanding retrieval problem remains for those comparisons. The 2026 APS PDF resolves the failed arXiv retrieval for that paper; the locally inspected slide PDF resolves its original size restriction.

The search covered the sources above. It was not an exhaustive scan of engineering texts on matrix resonance, the full literature on operator-valued unimodality, every dissertation, or every unindexed preprint. Recent “kinetic interacting particle” and other broadly related search results were screened, and none is relied on.

Sections 1–10 gate the matrix criterion, friction-design consequences and replica estimator statements. Appendix A records the subsequent rerun for the matrix regularity and rate results; it reuses the scalar antecedents assessed in the base report and adds precise formula and object comparisons. Neither audit nor a short proof establishes future influence, numerical efficiency or a REF grade.

## 8. Contribution-unit outcomes

| Unit | Outcome | Permitted positioning |
|---|---|---|
| Standard mechanical transfer spectrum and Gaussian tensor-chaos identity | **Ingredient collision / established machinery** | Derive or cite; do not advertise as discoveries |
| Scalar symmetric-unimodal convolution and its tensor layer-cake proof | **Established ingredient / elementary extension** | Use transparently; no separate priority claim |
| Antisymmetric duplication, kinetic duplication, and averaging both copies | **Verified collision** | Credit OI and the kinetic Potts-model precedent |
| Sharp $D\succeq0$ criterion, all-$L^2$ ordering, strict equality class, invertible-$J$ necessity | **No earlier statement found; candidate theorem survives this gate** | State the exact hypotheses and compare with the sources above |
| Least admissible friction and prescribed-shape threshold | **Candidate corollaries / bridge** | Explain the admissibility objective; distinguish observable-specific optimisation |
| Central-binomial coefficients alone | **Classical identity** | No new-sequence claim |
| Exact surviving-chaos variance formula and quadratic exception for this replica mean | **Candidate consequence / bridge** | Retain baseline and coupling distinctions; avoid algorithmic priority claims |
| Computational speed-up or general non-Gaussian applicability | **Unsupported by this target** | Exclude |

## 9. Research decision and defensible claim language

The extension merits mathematical development and independent proof review as a specified matrix theorem. It broadens the scalar setting by allowing noncommuting precision and friction, and duplication supplies its required symmetry for an arbitrary base pair. The literature comparison supports treating this as a possible bridge between matrix spectral ordering, Gaussian chaos and replica variance design.

A defensible statement is:

> We prove a necessary and sufficient matrix condition for universal position-observable variance ordering under matched kinetic rotations, with necessity for invertible rotation. For identical replicas, it yields exact variance limits and an equality classification. We found no equivalent theorem in the primary sources examined; replica coupling and averaging themselves have established antecedents.

This is a research positioning statement, and the extension does not automatically establish a higher REF rating.

## 10. Rerun triggers

Rerun the gate if the criterion is rewritten as a previously named resonance condition; if a coordinate transformation identifies the full position-observable problem with a known reversible-base result; if necessity is extended to singular rotations; if the rotation no longer commutes with precision/friction; if a non-Gaussian or numerical-efficiency claim is added; or if a new source contains the same all-observable criterion, equality class or replica formula.

The matrix regularity and arithmetic-rate extension triggered the formula-level rerun recorded next. Any further enlargement of that target requires another gate. The classical identities and verified replica antecedents above remain constraints on the wording.

## Appendix A. Matrix regularity and rate rerun

**Date:** 1 November 2026.  
**Frozen record:** [matrix_rates_target.yaml](matrix_rates_target.yaml), SHA-256 **33a39c18d3df2533a8069a4b0cea1f693b6f4d6497b5e0443122bb615fb97c90**.  
**Frozen mathematical snapshot:** Manuscript Appendix B, from its heading to the end of the file, SHA-256 **84ff26c6f190399f7befae6c6499a72f3d68810f018c3cec4e7b356bdbeecbfd**. This includes the $n\ge2$ clarification for the large-degree derivative-tail bound. The subsequently compared snapshot, SHA-256 **d9984719119dd60184c9ba4e69c424b7bf0bbb1bd89310eade6f5851a476c845**, adds explicit centring and a formula display; its theorem units are unchanged. The supporting source is [matrix_rates_appendix.md](../extensions/matrix_rates_appendix.md).

### A.1. Exact units added to the target

The kinetic model and commuting-rotation assumptions are those of Section 1. These quantitative results allow arbitrary positive definite $K,\Gamma$, including noncommuting pairs, and do **not** require the variance-ordering friction inequality. A kernel of $J$ is allowed.

Write $C(t)=\operatorname{Cov}(K^{1/2}q_t^0,K^{1/2}q_0^0)$ and let $\mathscr S_n$ be the Fourier transform of $C(t)^{\otimes n}$ on the symmetric tensor space. The target comprises four units:

1. **Exact curvature domain.** Every real $L^2$ position observable has $V_f\in C^1(\mathbb R)$ and $V_f'(0)=0$. Finite ordinary curvature at zero, global $C^2$ regularity, and
   $Q_f=\sum_{n,\omega}\omega^2n^{-3/2}\|f_{n,\omega}\|_2^2<\infty$
   are equivalent. If $Q_f=\infty$, the second divided difference tends to $-\infty$.
2. **A weighted operator Fourier approximation.** With $A_n=d\Gamma_n(K)$ denoting the sum of $K$ acting in each tensor factor, and $T_n=A_n/n$,
   $C(|u|/\sqrt n)^{\otimes n}-e^{-T_nu^2/2}\to0$
   in operator-norm $W^{1,1}$. Consequently,

$$
\sup_x(1+|x|)\left\|
\sqrt n\,\mathscr S_n(\sqrt n x)
-\sqrt{2\pi}\,T_n^{-1/2}e^{-x^2T_n^{-1}/2}
\right\|\longrightarrow0.
$$

3. **Uniform variance convergence and its exact angular-gap constant.** The supremum over unit-norm centred position observables of $V_f(\mu)-V_{\Pi_Jf}(0)$ tends to zero. If the angular-frequency group is $\omega_*\mathbb Z$ with $\omega_*>0$, then
   $D_J(\mu)\sim\sqrt{2\pi/e}/(|\mu|\omega_*)$.
   The leading constant is independent of $K,\Gamma$. The degree-frequency condition $|\omega|\ge cn^{-\tau}$ gives $D_J(\mu)=O(|\mu|^{-1/(2\tau+1)})$.
4. **Fixed-polynomial coefficient.** Set $L=K^{1/2}\Gamma K^{1/2}$ and $L_n=d\Gamma_n(L)$. For a fixed polynomial,

$$
V_f(\mu)-V_{\Pi_Jf}(0)
=\frac2{\mu^4}\sum_{n,\omega\ne0}
\frac{\langle f_{n,\omega},L_nf_{n,\omega}\rangle}{\omega^4}
+O_{f,K,\Gamma,J}(|\mu|^{-6}).
$$

The tensor comparison operator depends on $n$; no convergence of $T_n$ itself is asserted. The supremum defining $D_J$ allows the observable to vary with $\mu$. A fixed polynomial has a different rate. These distinctions are part of the object identity, not technical qualifications added after comparison.

### A.2. Formula fingerprints and inherited ingredients

The local expansion is

$$
C(t)=I-\tfrac12Kt^2+\tfrac16K^{1/2}\Gamma K^{1/2}t^3+O(t^4),
\qquad t\downarrow0.
$$

Its Gaussian small-time scale gives
$\int_0^\infty t^k\|C(t)\|^n\,dt=O(n^{-(k+1)/2})$.
The curvature exponent $-3/2$, the angular weight $\omega^2$, and the number-operator alias $J_{\rm ang}N^{-3/4}$ were retained together in the target. An ordinary quarter-order Hermite condition alone is only a sufficient condition and does not identify the sharper angularly weighted domain.

For the sharp constant, the exact scalar optimisation is

$$
\sup_{x\ge0}x\kappa^{-1/2}e^{-x^2/(2\kappa)}=e^{-1/2}.
$$

This elementary identity explains why the stiffness cancels from the leading worst-case constant. It is not a new numerical constant in isolation. The polynomial coefficient is the second-quantised form of the third one-sided derivative of the covariance, followed by repeated Fourier integration by parts.

Gaussian tensor representations, Laplace scaling near a nondegenerate quadratic maximum, local Gaussian approximation, tensor telescoping, Fourier differentiation, and integration by parts are treated as ingredients. No priority claim is made for a generic local central limit theorem or for the idea of a Gaussian approximation to tensor powers.

### A.3. Executed query log

This was a rerun using the same two public search engines and primary-source retrieval as the earlier audits. Exact-symbol queries were supplemented by subject aliases because mathematical formulas are inconsistently indexed.

| Family | Actual queries | Result of screening |
|---|---|---|
| Curvature domain | “asymptotic variance” “Hermite” “n” “regularity” rotation; “kinetic Langevin” “asymptotic variance” “regularity”; “n^{-3/2}” “asymptotic variance”; “asymptotic variance” “Hermite” “curvature” | No exact weighted angular-Hermite curvature theorem located |
| Tensor approximation | “Gaussian” “tensor powers” “local limit”; “operator-valued” “local central limit” Gaussian; “Gaussian” “tensor powers” “operator norm” “limit”; “W^{1,1}” “tensor” “Gaussian”; “matrix” “covariance” “tensor powers” “Fourier” | Found a tensor-power norm paper; its full definitions and main formulas distinguish the object |
| Second quantisation | “second quantization” “variance” “rotation”; “asymptotic variance” “second quantisation” | Recovered the originating kinetic Hermite decomposition and unrelated uses; no exact matrix-rate antecedent located |
| Sharp constant and uniform rate | “asymptotic variance” “sqrt” “2” “pi” “rotation”; “asymptotic variance” “sqrt{2” “pi”; “sqrt{2\pi/e}” “variance”; “asymptotic variance” “sqrt{2\\pi/e}” OR “sqrt(2*pi/e)” “variance”; “asymptotic variance” “uniform” “rate” “rotation”; “Langevin” “uniform” “variance” “Diophantine” | No exact kinetic gap constant located; existing uniform-variance literature remained a comparison boundary |
| Polynomial tail | “Langevin” “spectral density” “fourth” “Hermite”; “Langevin” “Hermite” “fourth-order” variance | Returned spectral-method and numerical-order material; no same fixed-polynomial amplitude expansion identified |
| Existing near sources | Exact title *A note on the asymptotic variance of drift accelerated diffusions* plus “pdf”; exact Maini title with a 30-day recency filter | Both sources were later read in full on 4 November 2026; see the novelty report, Section 7.1 |

The search did not treat unrelated tensor-norm, random-tensor covariance, numerical fourth-order convergence, or Hermite-domain system-identification results as matches. Uninspected broad hits were not counted as theorem-level clearances.

### A.4. Closest comparisons and inspection depth

**The originating projection limit remains prior work.** DNP (2017), particularly its Hermite decomposition, Theorem 5 and large-amplitude discussion, was already inspected in the base audit. The new quantitative unit is operator-norm convergence with the stated rates and constants, not the fact that a rotation-invariant component survives.

**Gaussian-chaos covariance remains established machinery.** The previously inspected [Breuer–Major primary paper](https://static.renyi.hu/~major/articles/breuer.pdf) supplies the scalar Hermite covariance and spectral-convolution antecedents. The present tensor formulation is used as the matrix counterpart, not promoted as a new representation.

**Uniform-over-observable variance convergence has explicit prior context.** Franke, Hwang, Ouled Said and Pai (2021), [DOI 10.1016/j.spl.2021.109128](https://doi.org/10.1016/j.spl.2021.109128), proves uniform convergence for drift-accelerated overdamped diffusions. Its authors' version was read in full on 4 November 2026 and does not supply the kinetic matrix constant. The report does not claim that uniform variance convergence is a new general phenomenon.

**Arithmetic effects on Gaussian variance are established context.** Lachièze-Rey's [*Diophantine Gaussian excursions and random walks*](https://arxiv.org/pdf/2104.07290), whose setting and principal statements were inspected in the scalar audit, links Gaussian excursion variance to Diophantine properties. The current claim concerns the worst-observable rate for rotated matrix kinetic covariances, with a degree-frequency lower bound. The conceptual role of arithmetic should be credited without equating the theorem statements.

**A close tensor-power title concerns different norms and a different limit.** Aubrun and Müller-Hermes, [*Limit formulas for norms of tensor power operators*](https://arxiv.org/pdf/2410.23063), arXiv:2410.23063, was retrieved in full. Introduction Eqs. (1)–(2) and Section 2.1's definitions were inspected. It studies the $k$th root of tensor-power operator norms between injective, projective and Hilbertian tensor products for a fixed operator. Appendix B uses the ordinary Hilbert-space operator norm of a difference of time-dependent covariance tensor powers, with an $n^{-1/2}$ time rescaling and a $W^{1,1}$ Fourier estimate. The shared words “tensor power” and “limit” do not identify the two objects.

**A current Fourier-Hermite paper.** Leonardo Maini, [*Spectral delocalization and central limit theorems for Fourier functionals of stationary Gaussian fields*](https://arxiv.org/abs/2610.37113), submitted 27 October 2026, concerns Gaussian fluctuations of Fourier-Hermite functionals and convolution small-ball estimates. It was read in full on 4 November 2026. It has the convolution-power variance, credited in the manuscript, and no matrix kinetic, rotated or sampler content.

### A.5. Unit decisions and corpus limits

| Unit | Outcome | Positioning |
|---|---|---|
| Exact matrix curvature domain and infinite second divided difference outside it | **Candidate theorem survives this rerun** | State the angular weight and all-$L^2$ quantifier exactly |
| Operator-norm $W^{1,1}$ tensor approximation | **Technical bridge built from established methods** | Give the complete estimate; no generic local-CLT priority claim |
| Uniform convergence and exact $\sqrt{2\pi/e}/\omega_*$ leading constant independent of $K,\Gamma$ | **Candidate quantitative theorem; no earlier statement found** | Distinguish the exact kinetic claim from known uniform-convergence concepts |
| Diophantine exponent in the matrix model | **Candidate extension of the scalar estimate** | Credit existing arithmetic Gaussian-variance context; retain the degree-frequency hypothesis |
| Fixed-polynomial coefficient $2d\Gamma_n(K^{1/2}\Gamma K^{1/2})$ | **Candidate explicit consequence** | Treat Fourier-tail derivation as standard machinery; keep fixed-observable quantifiers |

This rerun found no exact collision for these matrix theorem units in the material actually inspected. It did not search authenticated bibliographic databases or the full historical literature on operator-valued local limits, Gaussian Sobolev domains or rapidly driven diffusions. Exact formula indexing was weak.

Together with the scalar gate and Sections 1–10, this appendix covers the manuscript's stated mathematical contribution units at the level of a prior-art audit. It permits completion and review of the specified claims, with attribution and uncertainty preserved. It does not justify categorical priority language or a stronger REF assessment by itself.
