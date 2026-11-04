# Independent novelty gate: matrix kinetic rotation and replica consequences

**Search date:** 1 November 2026.  
**Reviewer:** independent AI review agent; this is not external human peer review.  
**Corpus boundary:** the primary papers and preprints identified below, their relevant full-text passages, public web indexes, and the supplied DNP/thesis material. No comprehensive MathSciNet or zbMATH search and no author enquiries were completed.  
**Intended contribution unit:** exact theorem and a bridge from matrix spectral order to all Gaussian chaoses, with design and replica consequences.

## 1. Frozen claim

### Exact statement

For symmetric positive definite \(K,\Gamma\), and an invertible real skew matrix \(J\) commuting with each, consider unit-mass stationary kinetic Langevin dynamics with simultaneous \(-\mu J\) rotations of position and momentum. Universal nonincrease of the position asymptotic variance in \(|\mu|\), over all real \(L^2\) observables, is equivalent to
\[
\Gamma^3-\Gamma K-K\Gamma\succeq0.
\]
Under this condition equality at distinct nonnegative amplitudes characterizes rotation-invariant observables. The positive square root \(\sqrt{2K}\) is the least admissible friction in Loewner order. Duplicating an arbitrary base pair \(K_0,\Gamma_0\) supplies the required commuting invertible rotation.

The subsequent rate claim is also frozen: after whitening, the covariance tensor has an operator-norm \(W^{1,1}\) Gaussian approximation; this gives the exact curvature domain and the same angular-gap leading constant \(\sqrt{2\pi/e}\) as in the scalar case.

### Exclusions

No claim is made to invent kinetic Langevin dynamics, transfer-function spectra, Gaussian chaos, symmetric unimodal convolution, matrix square-root monotonicity, replica coupling, or use of both replicas in an estimator. There is no non-Gaussian theorem or cost-after-discretization theorem. The least admissible friction is not an observable-specific variance optimizer.

### Permitted claim language before the gate

“An exact matrix criterion and proof are proposed.” Priority is not implied by the initial description.

## 2. Normalisation and translation table

| Original object | Canonical object | Transformation checked |
|---|---|---|
| Position precision \(K\), friction \(\Gamma\) | Dynamic stiffness \(K-\xi^2I+i\xi\Gamma\) | Unit mass and temperature one |
| Physical spectrum | \(2[Q_0+\xi^2B+\xi^4\Gamma^{-1}]^{-1}\) | \(Q_0=K\Gamma^{-1}K\), \(B=\Gamma-K\Gamma^{-1}-\Gamma^{-1}K\) |
| Cubic criterion | \(\Gamma B\Gamma\succeq0\) | Congruence gives \(\Gamma B\Gamma=\Gamma^3-\Gamma K-K\Gamma\) |
| Whitened spectrum | \(K^{1/2}S_qK^{1/2}\) | Preserves positivity and Loewner order |
| Chaos spectrum | \((2\pi)^{1-n}\) times the \(n\)-fold tensor convolution | Fourier transform is \(\int e^{-i\xi t}\cdot\,dt\); compress to symmetric tensors |
| Friction square gap | \(H=\Gamma^2/2-K\) | \(\Gamma H+H\Gamma=\Gamma^3-\Gamma K-K\Gamma\) |
| Replica coefficients | Circle averages of powers of cosine | \(b_{2m}=\binom{2m}{m}/4^m\), \(b_{2m+1}=0\) |
| Matrix local limit | \(T_n=n^{-1}\sum_j K_j\) | No scalar covariance or convergence of \(T_n\) is assumed |

## 3. Fingerprints

### Sequences and generating functions

For positive chaos degrees, the replica coefficients begin
\[
0,\quad \tfrac12,\quad0,\quad\tfrac38,\quad0,\quad\tfrac5{16},
\quad0,\quad\tfrac{35}{128}.
\]
Their even subsequence has generating function
\[
\sum_{m\ge0}b_{2m}z^m=(1-z)^{-1/2}.
\]
This is a classical central-binomial sequence. Its appearance alone carries no novelty. For the mean of two replicas the baseline is \(V_f(0)/2\); hence the pure even-degree residual fractions are \(2b_{2m}\), beginning \(1,3/4,5/8\).

### Small matrices and kernels

Independent exact checks covered three base dimensions, with duplication yielding rotation spaces of dimensions two, four and six:

| Base \(K,\Gamma\) | Cubic criterion \(D\) | Fingerprint |
|---|---|---|
| \(K=[1],\Gamma=[2]\) | \([4]\) | Scalar reduction agrees with \(\gamma^2\ge2k\) |
| \(K=\left(\begin{smallmatrix}1&1/4\\1/4&2\end{smallmatrix}\right),\Gamma=\operatorname{diag}(2,3)\) | \(\left(\begin{smallmatrix}4&-5/4\\-5/4&15\end{smallmatrix}\right)\) | \(\det D=935/16>0\), while \(K\Gamma\ne\Gamma K\) |
| \(K=\left(\begin{smallmatrix}1&1/4&0\\1/4&2&1/5\\0&1/5&3\end{smallmatrix}\right),\Gamma=\operatorname{diag}(3,4,5)\) | Diagonal \(21,48,95\), off-diagonals \(-7/4,-9/5,0\) | Leading minors \(21,16079/16,38160409/400\), all positive |

For every case, symbolic multiplication checked the inverse-spectrum cancellation, the congruence identity and the Lyapunov identity. A separate exact counterexample has \(\Gamma=\operatorname{diag}(1,2)\), \(K=\left(\begin{smallmatrix}2/5&-1/10\\-1/10&19/10\end{smallmatrix}\right)\). Here \(\Gamma^2-2K\succeq0\) but \(\det D=-1/100\). Therefore replacing the cubic criterion by the squared order inequality changes the theorem.

### Invariants and recurrences

Simultaneous orthogonal conjugation leaves the claim unchanged. Replica duplication preserves the base criterion. Second-chaos replica means are invariant under circle rotation, whereas a nonconstant one-replica observable is not invariant. A conjugate pair in the common \(K,J\) eigenbasis raises the chaos degree by two without changing angular frequency; this is the invariant behind the sharp rate lower bound.

## 4. Alias map

| Analysis | Probability | Combinatorics | Mathematical physics | Control and statistics |
|---|---|---|---|---|
| Loewner unimodality; operator-valued layer cake; tensor convolution | Gaussian chaos; Wick covariance; spectral density; additive-functional variance | Central binomial coefficients; cosine moments; symmetric tensor powers | Harmonic networks; fluctuation-dissipation; replica rotation | Dynamic stiffness; nonproportional damping; resonance; friction selection; coupled estimators |

The scalar threshold is the absence-of-resonance threshold \(\gamma^2\ge2k\), not the mechanical critical-damping threshold \(\gamma^2=4k\). This distinction matters when searching damping terminology.

## 5. Search log

All rows refer to searches or direct primary-source checks completed on 1 November 2026.

| Corpus or source | Query or location | Result inspected | Consequence |
|---|---|---|---|
| General web indexes, two search systems | “Gamma^3” “Gamma K” damping; “Γ3” “ΓK” Langevin; noncommuting friction variance Langevin | Formula and topic results | No exact cubic criterion was located; formula indexing is incomplete |
| Control and vibration terminology | damping matrix spectral density monotonic; nonresonant damping; frequency response Loewner monotone | Relevant-looking titles and available primary abstracts | No matched all-observable theorem found |
| Probability and analysis terminology | tensor convolution unimodal; matrix-valued symmetric unimodal; Gaussian tensor convolution Loewner | Results including a superficially similar matrix-convolution preprint | Distinguish tensor convolution from array convolution |
| DNP 2017 and Nüsken thesis | Original conjecture after Eq. (27); thesis repeated conjecture and projection limit | Full originating article and supplied thesis OCR, already audited in the base review | Direct open-problem lineage is scalar matched dynamics |
| Chak et al. | Full arXiv:2112.06844, Proposition 4.5 and Sections 1, 4 | Quadratic-observable optimization with \(\Gamma=K^{1/2}\) in its commuting class | Different objective from the new universal-ordering admissibility problem |
| Skeel and Hartmann | Full publisher article, Sections 1 and 5 | Worst-observable autocorrelation and scalar damping choice | Different optimization problem; not a matrix rotation criterion |
| Ohzeki and Ichiki 2015 | Full arXiv:1307.0434v8, Eqs. (7)–(8) | Cross-gradient coupling of duplicated overdamped systems | Replica coupling itself is established prior art |
| Ichiki and Ohzeki 2021 | Full arXiv:2107.08633, Eqs. (20)–(21), Section VI | Noisy gradient dynamics in both variables; both replicas may estimate target expectations | Replica averaging itself is established prior art |
| Kobayashi, Nakagawa and Sasa 2023 | Full arXiv:2212.12289 supplement, Eqs. (S.71), (S.75)–(S.76) | Kinetic duplication and arithmetic averaging of both copies | Even kinetic replica construction has an explicit prior precedent; the exact coupling and theorem must distinguish the present claim |
| Ohzeki 2026 | Full publisher PDF, DOI 10.1103/tg4c-7cnr, Sections VII–VIII | Auxiliary-variable dynamics and finite-time regularized gauge optimization | Gaussian benchmark is overdamped and the objective differs from universal asymptotic variance ordering |
| Mashreghi et al. | Full arXiv:2512.24575, Definition 3.1 | Jury product of finite arrays | Does not identify the real-line tensor convolution in this proof |
| Freshness pass | Past-year queries for Langevin friction rotation variance, underdamped unimodal variance, Gaussian tensor convolution Loewner | Primary results available through 1 November 2026 | No exact later collision located in the inspected corpus |

## 6. Verified collisions or bridges

The established replica mechanism is a genuine ingredient-level collision: Ohzeki and Ichiki's Eqs. (7)–(8) add opposite cross-gradient forces between two copies. The present duplicated kinetic system instead retains momentum variables and rotates both positions and momenta. This translation preserves the historical credit while distinguishing the theorem's model. Their 2021 Section VI also explicitly uses the auxiliary copy to estimate the target expectation. Thus neither duplication nor averaging is a new contribution here.

The final integration audit additionally inspected Kobayashi, Nakagawa and Sasa (2023), DOI 10.1103/PhysRevLett.130.247102, full supplement at https://arxiv.org/pdf/2212.12289. Their Eq. (S.71) duplicates positions and momenta, with cross-coupling through Hamiltonian derivatives. Eqs. (S.75)–(S.76) average the two systems' observables. This strengthens the prior-art boundary to kinetic duplication itself. The coupling is distinct from simultaneous position and momentum rotations; no cubic matrix ordering criterion was located in that material.

Ohzeki (2026), https://doi.org/10.1103/tg4c-7cnr, was checked in the full publisher PDF. Equations (77)–(78) use diffusion in both auxiliary-variable blocks; the Gaussian benchmark in Eqs. (88)–(97) is overdamped and optimizes a finite-time relaxation/force-cost objective. These model and objective differences prevent identification with the present cubic criterion.

Chak et al.'s Proposition 4.5, under its commuting hypotheses and selected quadratic observable, has optimizer \(\Gamma=\Sigma^{-1/2}\). With \(\Sigma=K^{-1}\), this is \(K^{1/2}\). The new least admissible matrix is \(\sqrt{2}K^{1/2}\). The difference is explained by different objective functions, not conflicting answers to one optimization problem.

The scalar layer-cake argument and Hermite covariance/convolution identities are established ingredients. The proposed bridge combines their tensor versions with a necessary and sufficient kinetic matrix spectral condition. No inspected primary source was found that supplies this whole implication with these hypotheses.

Mashreghi et al.'s Definition 3.1 sums array indices within fixed matrix dimensions. The manuscript integrates frequency and takes tensor products, increasing the operator space. These are different operations; a title match is insufficient to identify their theorems.

## 7. Negative evidence and missingness audit

No comprehensive subscription bibliographic search, citation-network exhaustion, author enquiry, or non-English historical control-theory search was completed. Older operator-valued unimodality results could use terminology absent from the queries. Formula search may omit superscripts, inverse matrices and noncommutative order. The standard transfer spectrum is not itself a priority claim. The published Chak paper was checked against its accessible author preprint and publication metadata; no claim is made to have compared every revision.

These limitations leave priority uncertain. They do not create a gap in the proof supplied for the claim.

## 8. Outcome by contribution unit

| Unit | Outcome | Confidence | Allowed wording | Forbidden wording |
|---|---|---|---|---|
| Exact matrix statement | No earlier statement found | Moderate | “We prove this exact criterion; no exact prior match was found in the stated search” | “The first possible matrix criterion” |
| Complete proof | Bridge; correctness audit passed | Moderately high | “A self-contained proof via matrix spectra and tensor convolution” | “All ingredients are new” |
| Cross-identification | Established ingredients plus apparently new combination | Moderate | “Extends the scalar spectral method to noncommuting \(K,\Gamma\)” | “Invents replica coupling or replica averaging” |
| Verification artifact | Reproduced supporting calculation | High for the finite checks | “Independent formulations agree in the checked cases” | “The code proves the all-\(L^2\) theorem” |

## 9. Decision

**No earlier statement found, with a substantive BRIDGE.**

The inspected literature does not defeat the exact matrix theorem or the matrix rate extension. Several ingredients are demonstrably established and should be presented that way. The most defensible contribution is the necessary and sufficient noncommuting matrix boundary, its transfer to every position observable, and the associated sharp regularity/rate and friction-design consequences.

## 10. Rerun triggers

Rerun the gate if a source is found on operator-valued symmetric unimodality, nonresonant fluctuation-dissipation spectra with nonproportional damping, kinetic replica variance ordering, or the exact cubic condition under a different name. Also rerun if the claim changes to a non-Gaussian target, a different rotation, arbitrary mass without a verified coordinate transformation, or cost after discretization.
