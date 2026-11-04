# Novelty-gate report: sharp variance ordering for rotating Gaussian samplers

**Search date:** 1 November 2026.  
**Prepared by:** AI-assisted mathematical research; this report is not an external referee opinion.  
**Manuscript assessed:** *Sharp variance ordering for rotating Gaussian samplers*, version 1.0, 1 November 2026.  
**Corpus boundary:** Publicly indexed web literature; arXiv; accessible Springer, PLOS, ESAIM/Numdam and other publisher full text; Imperial College's Spiral repository; author-hosted manuscripts; and OEIS formula records.  
**Intended contribution units:** Precise theorem statements, their complete proofs, an application of established Gaussian spectral methods, and a reproducibility package.

**Decision:** No direct collision with the full kinetic ordering, regularity or rate statements was found in the bounded search recorded here. Several mathematical ingredients and exact scalar fingerprints are demonstrably classical. The aggregate priority assessment is **BOUNDED UNCERTAINTY**, with the proposed theorems clear for proof development within this recorded boundary. A failed search is not proof of historical priority.

## 1. Frozen claim

### 1.1. Exact statement

The supplied [target.yaml](target.yaml) is the frozen target record, identified as `matched-rotation-underdamped-gaussian-variance`. For $d\ge2$, a nonzero real skew matrix $J\in\mathbb R^{d\times d}$, and $\gamma>0$, consider the stationary diffusion

$$
\mathrm dq_t=(p_t-\mu Jq_t)\,\mathrm dt,\qquad
\mathrm dp_t=(-q_t-\gamma p_t-\mu Jp_t)\,\mathrm dt
             +\sqrt{2\gamma}\,\mathrm dW_t.
$$

Its invariant law is $\mathcal N(0,I_{2d})$. For every real $f\in L^2(\pi)$, $\pi=\mathcal N(0,I_d)$, define

$$
V_f(\mu)=\lim_{T\to\infty}T\operatorname{Var}\left[
T^{-1}\int_0^T f(q_t)\,\mathrm dt\right].
$$

The central claim is the equivalence

$$
\gamma\ge\sqrt2
\quad\Longleftrightarrow\quad
V_f(b)\le V_f(a)
\text{ for every real }f\in L^2(\pi)\text{ and every }0\le a<b.
$$

Under this condition, equality for one pair $a<b$ holds exactly when $f$ is invariant under every rotation $e^{tJ}$. Thus the assertion includes every amplitude, the endpoint $\gamma=\sqrt2$, all square-integrable position observables, and an equality classification. The lower-threshold counterexample is a linear observable.

The originating question is the conjecture after equation (27) in Duncan, Nüsken and Pavliotis (2017). That conjecture is phrased through first and second derivatives at zero. The present statement separates the intended variance comparison from finite second differentiability, which fails for some $L^2$ observables. [DNP17]

### 1.2. Additional contribution units assessed

The current manuscript also proposes:

1. A spectral criterion for a stationary isotropic Gaussian process with integrable scalar covariance: universal variance ordering under rotation is equivalent to the scalar spectral density being nonincreasing on the positive half-line.
2. An exact curvature domain. If $a_{n,\omega}$ are the squared Hermite/angular coefficients, then finite ordinary second derivative at zero, global $C^2$ regularity, and
   $$
   \mathcal Q_J(f)=\sum_{n,\omega}a_{n,\omega}\omega^2n^{-3/2}<\infty
   $$

   are equivalent. All $L^2$ observables give a $C^1$ variance. Explicit observables outside this domain exhibit fractional or logarithmic cusps.
3. Quantitative convergence to the previously known invariant-projection limit: fourth-order decay for each fixed polynomial; the exact uniform constant $\sqrt{2\pi/e}/\omega_*$ at order $1/|\mu|$ for commensurate rotations; a Diophantine rate bound; an explicit $1/|\mu|^{1/3}$ example; and absence of every algebraic rate for a Liouville example.
4. Explicit scope examples for finite horizons and regular observation, and the Poisson-observation identity $\tau_{\mathrm P,\lambda}^2=\|f\|_2^2+\lambda V_f$. The last identity is presented as an elementary application, without an independent priority claim.

### 1.3. Exclusions

This assessment does not cover general non-Gaussian targets, unmatched rotations, unrestricted phase-space observables, numerical discretisations, or computational cost. It does not claim finite second derivatives for all $L^2$ observables. The invariant-projection limit, Gaussian covariance identities, the oscillator spectrum, and classical convolution facts are excluded from novelty claims.

No conclusion that this is the most important open problem in applied mathematics follows from this report. Research significance and a prospective REF rating require a separate assessment of originality, significance and rigour.

### 1.4. Target evolution and reruns

| Stage | Structural discovery | Consequence for the target and search |
| --- | --- | --- |
| Originating question | DNP's derivative conjecture for Gaussian kinetic sampling | Separate the exact source statement from the broader intended variance comparison. |
| Covariance reduction | $\operatorname{Cov}(q_t,q_0)=r_\gamma(t)e^{-\mu tJ}$ | Search rotating Gaussian processes, damped oscillators and scalar spectral formulas. |
| Chaos reduction | $V_f=\sum a_{n,\omega}\,2\pi p_\gamma^{*n}(\mu\omega)$ | Rerun under Hermite expansions, spectral convolution, nonlinear Gaussian functionals and symmetric unimodality. |
| All-$L^2$ limit | Curvature weights grow as $\omega^2n^{-3/2}$ | Replace unrestricted finite-curvature language by an exact domain; search fractional Gaussian/Hermite regularity. |
| High-degree scaling | $\sqrt n S_n(\sqrt n x)\to\sqrt{2\pi}e^{-x^2/2}$ | Distinguish fixed-observable decay from a supremum over all observables; search local-limit and arithmetic aliases. |
| Critical damping | $p_2(x)=2/[\pi(1+x^2)^2]$ | Identify the Student-$t_3$, squared-Lorentzian and Bessel-polynomial collisions. |
| Exact zero-frequency sequence | $n^nS_n(0)/2=(n-1)!\sum_{j=0}^n n^j/j!$ | Identify Schenker sums, truncated exponentials, birthday/urn expectations and tree-function aliases; stop any sequence-novelty claim. |

**Further proposed extension:** An anisotropic independent-block extension is outside the frozen target and is not cleared by this report. It requires an exact statement, its own normalisation and fingerprints, and a fresh prior-art gate before being included in any novelty claim.

## 2. Normalisation and translation table

| Original or alternative notation | Canonical notation here | Transformation checked |
| --- | --- | --- |
| DNP's $\sigma_f^2$ | $V_f$ | $V_f=2\sigma_f^2$; all constants in the manuscript use the full variance limit. |
| DNP's Gaussian precision $S$, $M=S$, $\Gamma=\gamma S$, $J_2=SJ_1S$, $\nu=\mu$ | Unit position and momentum covariances, one skew matrix $J$ | $\widetilde q=S^{1/2}q$, $\widetilde p=S^{-1/2}p$, $\widetilde J=S^{1/2}J_1S^{1/2}$. |
| One-sided Laplace transform | Even-covariance Fourier transform | $R_\gamma(s)=(s+\gamma)/(s^2+\gamma s+1)$; $S_\gamma(\xi)=2\operatorname{Re}R_\gamma(i\xi)$. |
| Spectral probability density | $p_\gamma=S_\gamma/(2\pi)$ | $\int p_\gamma=1$, $r_\gamma(t)=\int e^{it\xi}p_\gamma(\xi)\,\mathrm d\xi$. |
| Hermite-chaos covariance $r^n$ | $S_n=\widehat{r^n}$ | $S_n=(2\pi)^{1-n}S_1^{*n}=2\pi p_\gamma^{*n}$. |
| Complex angular eigenvectors | Real-observable coefficients $a_{n,\omega}$ | Both signs of each frequency are included; $a_{n,-\omega}=a_{n,\omega}$. |
| Standard Student variable $T_3$ | Density $p_2$ | $T_3/\sqrt3$ has density $2/[\pi(1+x^2)^2]$. |
| OEIS integral $I_n=\int_0^\infty e^{-x}(1+x/n)^n\,\mathrm dx$ | Critical-damping $S_n(0)$ | Substitution $x=nt$ gives $I_n=nS_n(0)/2$. |
| Schenker sum $b_n=n!\sum_{j=0}^n n^j/j!$ | Integer fingerprint $A_n=n^nS_n(0)/2$ | $A_n=b_n/n=n^{n-1}I_n$. |

The distinction between $\gamma=2$, the critical-damping value, and $\gamma=\sqrt2$, the variance-ordering threshold, is essential. The Student fingerprint occurs at the former.

## 3. Fingerprints

The supplied [formula_fingerprints.json](formula_fingerprints.json) records exact critical-damping values, normalisation and drift convention. The original target and JSON were retained rather than rewritten after the sequence match.

### 3.1. Rational and integer sequences

At $\gamma=2$, $r(t)=(1+t)e^{-t}$ for $t\ge0$. The first ten exact values are:

| $n$ | $S_n(0)$ | $A_n=n^nS_n(0)/2$ |
| ---: | ---: | ---: |
| 1 | $4$ | 2 |
| 2 | $5/2$ | 5 |
| 3 | $52/27$ | 26 |
| 4 | $103/64$ | 206 |
| 5 | $4388/3125$ | 2194 |
| 6 | $1223/972$ | 29352 |
| 7 | $945460/823543$ | 472730 |
| 8 | $556403/524288$ | 8902448 |
| 9 | $42647972/43046721$ | 191915874 |
| 10 | $7281587/7812500$ | 4660215680 |

The integer sequence beginning **2, 5, 26, 206, 2194, 29352** is classical. It is the Schenker sequence A063170 divided termwise by $n$. A090878 instead lists the *reduced numerators* of $I_n$, beginning **2, 5, 26, 103, 2194, 1223**. These sequences must not be conflated. The exact transformation, not a matching prefix alone, establishes the collision. [OEIS-S; OEIS-I; ACM13]

The ten-term integer prefix also appears in the 27 April 2014 post *Expmath2 – Generalized continued fractions*, which links A090878. That post was a discovery lead; the OEIS formulas and the primary Schenker-sum paper supply the mathematical identification. [EM14]

### 3.2. Rational transforms and canonical formulas

The scalar oscillator spectrum is

$$
S_\gamma(\xi)=\frac{2\gamma}{\xi^4+(\gamma^2-2)\xi^2+1}
=\frac{2\gamma}{(1-\xi^2)^2+\gamma^2\xi^2}.
$$

Its denominator coefficient vector in decreasing powers of $\xi$ is $(1,0,\gamma^2-2,0,1)$. At $\gamma=2$, the denominator is $(1+\xi^2)^2$; at $\gamma=\sqrt2$, it is $1+\xi^4$. These are aliases of a damped-oscillator power spectrum, not newly defined density families.

At critical damping,

$$
S_n(\xi)=2\operatorname{Re}\sum_{k=0}^n
\binom nk\frac{k!}{(n-i\xi)^{k+1}},\qquad
A_n=(n-1)!\sum_{j=0}^n\frac{n^j}{j!}.
$$

The latter expression belongs to the truncated-exponential/Schenker family. A063170 also records its exponential generating function $1/(1-T(x))^2$, with the tree function defined by $T=xe^T$. This is an additional alias of the scalar sequence, not a generating function for the full kinetic variance theorem. [OEIS-S]

### 3.3. Small matrices and angular spectra

The planar matrix is $J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, with characteristic polynomial $z^2+1$, rank two, trace zero and determinant one. The drift is

$$
B_\mu=\begin{pmatrix}\mu J&-I\\I&\gamma I+\mu J\end{pmatrix}.
$$

For the planar case at $\gamma=2$, three exact instances are:

| $\mu$ | Characteristic polynomial of $B_\mu$ | Rank | Trace | Determinant |
| ---: | --- | ---: | ---: | ---: |
| 0 | $(z-1)^4$ | 4 | 4 | 1 |
| $1/2$ | $((z-1)^2+1/4)^2$ | 4 | 4 | $25/16$ |
| 1 | $((z-1)^2+1)^2$ | 4 | 4 | 4 |

For a unit planar rotation, degree $n$ has angular frequencies $-n,-n+2,\ldots,n$, each with complex multiplicity one. A zero frequency occurs exactly at even degree. These finite objects fix signs and indexing. No novel-matrix claim is made.

### 3.4. Invariants, scales and regularity

The stationary covariance is $I_{2d}$, and $B_\mu+B_\mu^\top=2\operatorname{diag}(0,\gamma I)$. The scalar covariance satisfies $r''+\gamma r'+r=0$, $r(0)=1$, $r'(0)=0$. Its short-time expansion starts with $1-t^2/2$, giving the scaling $S_n(0)\asymp n^{-1/2}$ and $-S_n''(0)\sim\sqrt{2\pi}n^{-3/2}$.

Writing $N$ for the Hermite number operator, the condition $f\in\operatorname{Dom}(N^{1/4})$ is sufficient for finite curvature because $|\omega|\le n\|J\|$. It is sharp as a uniform degree-based condition. It is **not** the exact necessary condition for every observable: angularly invariant components have zero curvature weight whatever their degree. The exact condition is $\mathcal Q_J(f)<\infty$.

### 3.5. Snapshot checksums

SHA-256 checksums of the frozen input records inspected for this report:

```text
target.yaml
faf3f0c0da1579934bec5404100d96f0790b3dd2125019ac2bdffcb0331d810f

formula_fingerprints.json
6b9d7205b2dcc7fcbb94b2f301bbc30a93730ceaeb1e43ddef099a53258958e3
```

## 4. Alias map

| Analysis | Probability | Combinatorics / representation theory | Mathematical physics | Statistics and applications |
| --- | --- | --- | --- | --- |
| Fourier transform of covariance powers | Nonlinear stationary Gaussian functionals | Hermite chaos, Wick products, symmetric tensor powers | Oscillator displacement spectrum | Kinetic/nonreversible sampling; long-run estimator variance |
| Symmetric decreasing convolution | Symmetric unimodal probability densities | Layer-cake mixtures | Resonance threshold | Universal ordering over observables |
| Squared Lorentzian | Scaled Student $t_3$, inverse-gamma Gaussian mixtures | Bessel polynomial products | Critically damped oscillator | Exact reference model |
| Truncated exponential sums, incomplete gamma | Birthday/urn stopping expectations | Schenker sums, tree function, labelled mappings | Critical-damping covariance integral | Exact check sequence |
| Weighted Fourier local limits | Convolution-power local limits | Angular frequency lattice | Rotating frame | Uniform versus fixed-observable rates |
| Small divisors, Diophantine approximation | Gaussian excursion variance | Pell approximants, Liouville frequencies | Incommensurate rotations | Slow worst-observable convergence |
| Fractional powers of the number operator | Gaussian Sobolev/Hermite regularity | High-degree harmonic polynomials | Short-time covariance scale | Parameter sensitivity and divergent curvature |

## 5. Search log

The companion [review/search_log.md](review/search_log.md) gives reproducible query families and inspected outcomes. All listed searches were run on 1 November 2026. The search was organised in concentric rings:

| Ring | Queries or method | Main consequence |
| --- | --- | --- |
| Original question | Exact title, author names, conjecture, and related sampling work | Located the precise 2017 conjecture and its repetition in the 2018 thesis; separated the known projection limit. |
| Formula fingerprints | Scalar rational spectrum, critical-damping rational values and the ten-term integer rescaling | Identified Student/Bessel and Schenker collisions. |
| Gaussian aliases | Hermite covariance, spectral convolution, nonlinear Gaussian spectra, rotation and unimodality | Located classical Gaussian identities and cross-disciplinary uses. |
| Regularity | Hermite/quarter-power/fractional-domain terms with asymptotic variance and kinetic Langevin | No source with the exact curvature domain or explicit cusp statements was found. |
| Rates and arithmetic | Uniform asymptotic variance, small divisors, Diophantine, Liouville, irrational rotation | Located adjacent overdamped and Gaussian-excursion results; no exact kinetic-rate collision found. |
| Freshness and follow-up | Current web-indexed literature, including a late-October 2026 Gaussian spectral preprint | Found an abstract-only recent source that remains uninspected in full. |

The search did not attempt an exhaustive forward-citation census or claim complete coverage of all mathematical literature.

## 6. Verified collisions, related results and inspection depth

### 6.1. Originating kinetic statement and the known limit

**[DNP17]** A. B. Duncan, N. Nüsken and G. A. Pavliotis (2017), *Using perturbed underdamped Langevin dynamics to efficiently sample from probability distributions*, Journal of Statistical Physics 169, 1098–1131. [DOI](https://doi.org/10.1007/s10955-017-1906-8); [full text](https://link.springer.com/article/10.1007/s10955-017-1906-8).

**Inspected:** Full publisher text, conditions (27), conjecture immediately following them, Theorem 3, the normalised Gaussian dynamics, and Theorem 5. The local derivative result covers linear/quadratic position observables; the large-amplitude invariant-projection limit is already established. **Outcome:** collision for that limit and those special cases; no inspected theorem supplies the full proposed global ordering.

**Mismatch boundary:** Remark 5, Figure 1b and Remark 9 already describe variance growth and divergence when the two rotations are only approximately matched. A newly computed closed-form example of this behaviour is an illustrative certificate of that known failure, not a new theorem about mismatch. This exclusion applies if such an example is added to the manuscript.

**[N18]** N. Nüsken (2018), *Topics in sampling schemes based on Markov processes*, Imperial College London doctoral thesis. [DOI](https://doi.org/10.25560/63868); [repository record](https://spiral.imperial.ac.uk/entities/publication/83cfbc60-ae29-4e4f-8a49-9d89464aa3fb).

**Inspected:** Complete local text/OCR, including the conjecture on printed page 62, Section 5.1's quadratic analysis, Section 5.3's projection limit and discussion on page 99. The inspected thesis repeats rather than resolves the conjecture. This supplies a later documented occurrence, not proof that no subsequent resolution exists.

### 6.2. Symmetric unimodality

**[LU13]** C. Lefèvre and S. Utev (2013), *Convolution property and exponential bounds for symmetric monotone densities*, ESAIM: Probability and Statistics 17, 605–613. [DOI](https://doi.org/10.1051/ps/2012012); [full PDF](https://www.numdam.org/article/PS_2013__17__605_0.pdf).

**Inspected:** Full PDF, especially Section 1.2 and Theorem 1.1. Page 606 explicitly attributes closure of symmetric unimodality under convolution to Wintner and discusses its mixture proof; the paper extends the property to a broader class. Our density $p_\gamma$ is symmetric and decreasing exactly above the threshold, so its convolution powers meet this established theorem. The strict version used in the manuscript follows from interval integration. **Outcome:** classical ingredient collision; no independent novelty claim for the convolution lemma.

### 6.3. Hermite covariance and spectral convolution

**[BM83]** P. Breuer and P. Major (1983), *Central limit theorems for non-linear functionals of Gaussian fields*, Journal of Multivariate Analysis 13(3), 425–441. [DOI](https://doi.org/10.1016/0047-259X(83)90019-2); [author-hosted PDF](https://static.renyi.hu/~major/articles/breuer.pdf).

**Inspected:** Full PDF. Page 428 states the spectral-measure convolution identity for a Hermite functional in the discrete-time setting; equation (2.1) gives the Hermite covariance formula. With the Fourier convention in Section 2, the corresponding continuous-time identity is $S_n=2\pi p^{*n}$. **Outcome:** exact established ingredient.

**[MGS19]** S. P. Muscinelli, W. Gerstner and T. Schwalger (2019), *How single neuron properties shape chaotic dynamics and signal transmission in random neural networks*, PLOS Computational Biology 15(6), e1007122. [Full text and DOI](https://doi.org/10.1371/journal.pcbi.1007122).

**Inspected:** Publisher full-text sections surrounding equations (37) and (42)–(43). These use covariance-power and self-convolution expansions for nonlinear Gaussian signals. They establish another disciplinary alias for the same machinery. **Outcome:** related spectral ingredient, not a kinetic-ordering theorem.

### 6.4. Student and Bessel identities

**[BV08]** C. Berg and C. Vignat, *Linearization coefficients of Bessel polynomials and properties of Student t-distributions*, Constructive Approximation 27, 15–32 (2008); 2005 preprint titled *Linearization coefficients of Bessel polynomials*. [DOI](https://doi.org/10.1007/s00365-006-0643-6); [arXiv record](https://arxiv.org/abs/math/0506458); [full PDF](https://arxiv.org/pdf/math/0506458).

**Inspected:** Full preprint, especially equation (3), equations (4)–(6), equation (10) and Theorem 2.6. Its density $A_\nu(1+x^2)^{-\nu-1/2}$, at $\nu=3/2$, is exactly $p_2$. Its Bessel-polynomial characteristic functions include $(1+|t|)e^{-|t|}$, and the paper provides finite-mixture identities for convolutions. **Outcome:** exact collision for the critical-damping distribution and convolution family; no claim of a new density or characteristic function.

### 6.5. Schenker and truncated-exponential sequence identity

**[OEIS-I]** OEIS A090878, originally entered by Robert G. Wilson v in 2004, with later corrections and formula comments. [Full entry](https://oeis.org/A090878). **[OEIS-S]** OEIS A063170, *Schenker sums with n-th term*. [Full entry](https://oeis.org/A063170).

**Inspected:** Definitions, displayed terms, formula sections and linked primary references. The substitutions in Section 2 prove $I_n=nS_n(0)/2$ and $A_n=\mathrm{A063170}(n)/n$. The reduced-numerator nature of A090878 was checked explicitly. **Outcome:** exact scalar sequence collision. Neither the rational values nor the integer rescaling is claimed as new.

**[ACM13]** T. Amdeberhan, D. Callan and V. Moll (2013), *Valuations and combinatorics of truncated exponential sums*, Integers 13, #A21. [Publisher PDF](https://math.colgate.edu/~integers/n21/n21.pdf).

**Inspected:** Full PDF retrieved; the load-bearing inspection was the introduction, equation (1.5)'s finite exponential sum and equation (1.9)'s integral representation. These give a primary-paper confirmation of the scalar identity and point to earlier Ramanujan/Knuth appearances. Their arithmetic valuation theorems concern the scalar sequence; they do not supply the kinetic variance-ordering assertion.

**[EM14]** *Expmath2 – Generalized continued fractions*, experimental math, 27 April 2014. [Archive containing the post](https://experimentalmath.wordpress.com/2014/04/).

**Inspected:** The fourth continued-fraction example and its ten-term related sequence. It exactly matches $A_n$. This was used as a discovery lead; the formula collision rests on the independently checked OEIS and primary-paper identities.

### 6.6. Related overdamped results

**[DLP16]** A. B. Duncan, T. Lelièvre and G. A. Pavliotis (2016), *Variance reduction using nonreversible Langevin samplers*, Journal of Statistical Physics 163, 457–491. [DOI](https://doi.org/10.1007/s10955-016-1491-2); [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4939425/).

**Inspected:** The variance-reduction framework and Gaussian/rotation discussion. This concerns perturbations of a reversible overdamped baseline. It is essential prior context; the kinetic baseline considered here is already nonreversible and fails universal ordering below the threshold. **Outcome:** related prior theory, not an identical theorem after the checked normalisation.

**[FHOP21]** B. Franke, C.-R. Hwang, A. Ouled Said and H.-M. Pai (2021), *A note on the asymptotic variance of drift accelerated diffusions*, Statistics & Probability Letters 175, 109128. [DOI](https://doi.org/10.1016/j.spl.2021.109128); [publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0167715221000900).

**Inspected:** Publicly indexed primary publisher introduction and theorem excerpts, including the uniform-over-observable convergence criterion and irrational-rotation discussion. Direct full-text access returned a restriction. **Outcome:** material adjacent theorem; uniform variance convergence itself is not a general new phenomenon. The exact kinetic rates were not found in the inspected material. Because full text was unavailable, this comparison remains partial.

### 6.7. Arithmetic effects in Gaussian variance

**[LR22]** R. Lachièze-Rey, *Diophantine Gaussian excursions and random walks*, arXiv:2104.07290 (2021; revised 2022). [Record](https://arxiv.org/abs/2104.07290); [full PDF](https://arxiv.org/pdf/2104.07290).

**Inspected:** Full PDF retrieved; introduction, setting and principal variance/Diophantine statements examined. The work studies excursion-volume variance for Gaussian fields with incommensurable spectral atoms as spatial observation windows grow. Our parameter is rotation amplitude in a continuously damped kinetic model, and the main rate quantity is a supremum over unit $L^2$ observables. **Outcome:** substantial conceptual precedent, not a verified collision with these kinetic rate statements. Arithmetic dependence of Gaussian variance must not be described as unprecedented.

### 6.8. Differentiation with respect to friction

**[C22]** M. Chak (2022), *Convergence and variance reduction for stochastic differential equations in sampling and optimisation*, Imperial College London doctoral thesis. [DOI](https://doi.org/10.25560/100327); [full PDF](https://spiral.imperial.ac.uk/bitstreams/9d7fd6ca-34e5-490b-8067-63a52579dd3f/download).

**Inspected:** Full PDF retrieved, Chapter 3 introduction and relevant parameter-derivative passages examined, especially pages 67–70. That work differentiates asymptotic variance with respect to the friction matrix through Poisson-equation gradients. Rotation amplitude is a different parameter. No exact quarter-Hermite domain or the stated cusp constructions was found in the inspected material. **Outcome:** related sensitivity theory; this is not a claim to have exhaustively audited every differentiability result in the literature.

## 7. Negative evidence and missingness audit

The negative finding is specific: no earlier statement or proof of the full candidate kinetic ordering, exact curvature domain, or sharp kinetic rate results was found in the recorded query families and inspected sources. It is not a finding that these results are globally unknown.

The principal limitations are:

- **Very recent source unavailable in full.** An indexed abstract identified Leonardo Maini's *Spectral delocalization and central limit theorems for Fourier functionals of stationary Gaussian fields*, arXiv:2610.37113, dated 27 October 2026. [Primary record attempted](https://arxiv.org/abs/2610.37113). The abstract discusses Fourier-Hermite CLTs, convolution powers and conditional spectral delocalization. Primary abstract/HTML/PDF retrieval repeatedly failed. No theorem-level clearance of this work is asserted.
- **Restricted publisher material.** The Franke–Hwang–Ouled Said–Pai comparison relies on indexed primary text and theorem excerpts, not a complete inspected manuscript.
- **Database coverage.** No comprehensive authenticated MathSciNet, zbMATH, Scopus or Web of Science search was performed. A web query targeting OEIS is not a substitute for searching every transformed sequence in its entire database.
- **Language and naming.** Searches primarily used English titles, formulas and aliases. Older non-English literature, differently indexed theses and unpublished notes may be missed.
- **Citation coverage.** Relevant references and follow-ups were inspected selectively; a complete citing-paper census was not performed.
- **Enquiries.** No author enquiry or independent specialist priority confirmation has been completed.

These gaps justify bounded priority language. The inaccessible recent abstract is not evidence of a collision, but it also cannot be treated as cleared. A specialist check of current follow-ups to DNP and the most recent Gaussian spectral literature is the next useful priority check before submission.

## 8. Outcome by contribution unit

| Unit | Outcome | Confidence within the search boundary | Allowed wording | Forbidden wording |
| --- | --- | --- | --- | --- |
| Full kinetic ordering statement | CLEAR TO PROVE within the recorded boundary; historical priority remains uncertain | Moderate | “We prove the stated global ordering; no earlier statement was found in the documented search.” | “Definitely globally new”; “first proof” based solely on the search; “the most important open problem.” |
| Complete proof of that statement | CLEAR TO PROVE within the recorded boundary | Moderate | “A complete spectral proof is supplied, using established ingredients.” | “The first complete proof” without a complete priority check. |
| General Gaussian spectral criterion | BRIDGE / BOUNDED UNCERTAINTY | Moderate | “An exact criterion packages the Gaussian expansion and unimodal convolution into this application.” | Claiming invention of Gaussian spectral convolution or unimodal closure. |
| Exact curvature domain and rough-observable constructions | CLEAR TO PROVE within the recorded boundary | Moderate | “The manuscript proves the stated domain and examples; no matching result was found.” | Finite curvature for all $L^2$; a necessary quarter-power domain without accounting for angular invariance. |
| Sharp kinetic uniform rates and arithmetic examples | CLEAR TO PROVE within the recorded boundary | Moderate | “The exact constant and these kinetic rate statements were not found in the bounded search.” | Claiming the first arithmetic effect in Gaussian variance, or novelty of uniform convergence in general. |
| Invariant-projection limit | COLLISION | High | “We quantify the known DNP limit.” | Claiming discovery of the limit. |
| Failure under mismatched rotations | COLLISION for the phenomenon; exact example may be illustrative | High | “An explicit calculation illustrates the mismatch failure already described by DNP.” | Claiming discovery that approximate matching can cause divergent variance. |
| Student/Bessel family, Schenker sequence, Hermite and unimodal-convolution ingredients | COLLISION | High | “Classical formulas used as proof ingredients and fingerprints.” | New density, new scalar sequence, or new general convolution identity. |
| Observation-rule examples and Poisson identity | Application / no separate priority claim | High for the elementary derivation; priority not investigated exhaustively | “These formulas show the theorem's observation boundaries.” | Claiming a new general Poisson-sampling theory. |
| Verification artefact | New implementation/exposition in this package; not a mathematical priority claim | High for what the package contains | “Deterministic checks reproduce the displayed formulas and normalisations.” | Treating finite numerical checks as proof of all-$L^2$ assertions or historical novelty. |

## 9. Decision and permitted manuscript language

**Aggregate decision: BOUNDED UNCERTAINTY.** The proof project may proceed on the precise candidate statements, with classical collisions excluded from its contribution claims. This report does not certify first discovery, first proof, publication novelty, or a REF rating.

Suitable wording is:

> The results provide a global variance-ordering theorem and a precise regularity correction to the Gaussian kinetic question posed by Duncan, Nüsken and Pavliotis. The proof uses established Gaussian spectral and convolution methods. No earlier statement of the full ordering, regularity and rate results was found in the bounded search described in the accompanying novelty report.

The report supports mathematical claims only to the extent of the supplied proofs. A description such as “conjecture resolution” must retain the qualification that the literal unrestricted finite-second-derivative statement is false: the variance-ordering question is settled while the differentiability formulation is corrected.

## 10. Rerun triggers

A new gate is required if the scope changes to anisotropic blocks, noncommuting drifts, non-Gaussian targets, unmatched perturbations, numerical algorithms, or a new observation-cost theorem. It is also required if the proof yields a named semigroup comparison, a stronger standard local-limit theorem that directly implies the sharp constant, a further classical transform identity, or an exact theorem in one of the unavailable sources.

Before journal submission, update the current-literature search, inspect the remaining full texts where obtainable, and seek a specialist assessment of whether the full statements or equivalent proofs have appeared elsewhere. These steps refine priority and significance; they are distinct from checking the mathematical proof already supplied.
