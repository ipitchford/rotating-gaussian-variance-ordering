# AI index: sharp variance ordering for rotating Gaussian samplers (v0.3.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with [README.md](README.md) and the
paper [research_sampling/output/pdf/rotating_gaussian_variance.pdf](research_sampling/output/pdf/rotating_gaussian_variance.pdf)
(source [research_sampling/manuscript.md](research_sampling/manuscript.md); generated LaTeX in
[research_sampling/output/latex/rotating_gaussian_variance.tex](research_sampling/output/latex/rotating_gaussian_variance.tex)).
Version DOI 10.5281/zenodo.23953250; concept DOI 10.5281/zenodo.23941496. Originating question: the conjecture of
Duncan, Nüsken and Pavliotis (J. Stat. Phys. 169 (2017) 1098-1131, DOI 10.1007/s10955-017-1906-8) stated after their
parameter conditions (27) (arXiv:1705.00170v1 (35a)-(35c)).

## Notation

Unit-mass kinetic Langevin dynamics dq = (p − μJq)dt, dp = (−Kq − Γp − μJp)dt + sqrt(2Γ) dW with J skew, [J,K] = [J,Γ] = 0;
scalar case K = I, Γ = γI. Stationary law N(0, K^{-1}) ⊗ N(0, I). Observable f in L²(π) of the position. Long-run
variance V_f(μ) = lim T·Var(T^{-1}∫_0^T f(q_t)dt) = 2∫_0^∞ Cov(f(q_t), f(q_0))dt (twice DNP's σ_f²). Π_J f: projection onto
rotation-invariant functions. Scalar spectrum S_γ(ξ) = 2γ/(ξ⁴ + (γ² − 2)ξ² + 1); S_n = 2π p^{*n} with p = S_γ/(2π)
(degree-n Hermite chaos). Hermite/angular weights a_{n,ω} ≥ 0 with V_f(μ) = Σ a_{n,ω} S_n(μω) (formula (6)).

## Claims and where they are proved

| ID | Claim | Location | Evidence type |
|---|---|---|---|
| C1 | For J ≠ 0: V_f(μ) nonincreasing in abs(μ) for every real f in L²(π) iff γ ≥ √2 (endpoint included); strict unless f = Π_J f | Theorem 1 | analytic proof |
| C2 | For any rotated stationary Gaussian process with integrable covariance: universal ordering iff the scalar spectral density is nonincreasing on [0, ∞) | Theorem 2, Lemma 3 | analytic proof (classical unimodal-convolution closure credited) |
| C3 | Below the threshold (any γ > 0): even observables improve at every μ ≠ 0; only finitely many odd degrees can be hurt; one finite amplitude μ_0(γ,J) improves every non-invariant observable; small amplitudes hurt a linear observable when γ < √2 | Theorem 4A | analytic proof; Table 1 crossing points are numerical computations (verify_below_threshold.py), not part of the proof |
| C4 | Every V_f is C¹ with V_f'(0) = 0; finite second derivative at 0 (and C²) iff Q_J(f) = Σ a_{n,ω} ω² n^{-3/2} < ∞, a class containing all polynomials; explicit fractional and logarithmic cusps outside | Theorem 5, Proposition 6 | analytic proof |
| C5 | Large rotations: O(μ^{-4}) for each polynomial; uniform worst case D_J(μ) ~ sqrt(2π/e)/(abs(μ) ω*) for commensurate speeds; Diophantine bound; explicit abs(μ)^{-1/3} example; no algebraic rate for a Liouville example | Proposition 7, Theorem 8, Corollary 8A, Proposition 9, Section 7 | analytic proof |
| C6 | Matrix case (K, Γ noncommuting): ordering for every L² position observable iff D = Γ³ − ΓK − KΓ ⪰ 0 (necessity when J invertible); least admissible friction Γ = (2K)^{1/2} (a safety boundary, not an optimum); Γ² ⪰ 2K alone is insufficient | Theorem 10, Lemma 10A, Corollary 11, Section 8.2 | analytic proof; finite checks in verify_matrix_extension.py |
| C7 | Two coupled replicas supply an invertible commuting rotation for any Gaussian target, with explicit limiting variances for single-copy observables and replica averages | Section 8.4, Corollary 12 | analytic proof (replica coupling and averaging are established devices, credited) |
| C8 | Phase-space (momentum) observables, fixed finite horizons and regular sampling can reverse the ordering; independent Poisson sampling preserves it (τ² = ‖f‖² + λV_f) | Section 9 | analytic proof and exact rational certificate (Section 9.2); Poisson identity presented as an elementary application |
| C9 | Matrix regularity and rates (Appendix B) | Propositions B1, B2 | analytic proof |
| C10 | Not claimed: non-Gaussian targets; unmatched rotations; discretised integrators or computational cost; an optimal friction; novelty of the Hermite/convolution ingredients, DNP's projection limit or replica constructions | Sections 1.4, 4.1, 10 | statement of scope |

## Verification artefacts (supplementary to the proofs)

- [research_sampling/code/verify.py](research_sampling/code/verify.py): exact rational spectral fingerprints, covariance and Poisson/Lyapunov checks, finite-horizon and observation counterexamples, high-degree limits, figure; report [verification_results.json](research_sampling/code/verification_results.json); figure [variance_landscape.pdf](research_sampling/figures/variance_landscape.pdf).
- [research_sampling/code/verify_matrix_extension.py](research_sampling/code/verify_matrix_extension.py): noncommuting example, tensor-convolution versus Lyapunov, insufficiency of Γ² ⪰ 2K, least-friction identity; report [matrix_extension_results.json](research_sampling/code/matrix_extension_results.json).
- [research_sampling/code/verify_below_threshold.py](research_sampling/code/verify_below_threshold.py): Table 1 crossing points from an exact exponential-sum formula cross-checked by quadrature; report [below_threshold_results.json](research_sampling/code/below_threshold_results.json).
- Every check raises `RuntimeError` on failure, including under `python -O`. Replay commands: [README.md](README.md); details: [research_sampling/code/README.md](research_sampling/code/README.md); CI: [.github/workflows/replay.yml](.github/workflows/replay.yml).

## Sources, novelty and provenance

- [refs.bib](refs.bib) and [refs/records/](refs/records/): bibliography and the registry records it was generated from.
- [research_sampling/novelty_report.md](research_sampling/novelty_report.md), [research_sampling/review/search_log.md](research_sampling/review/search_log.md), [research_sampling/review/extension_novelty.md](research_sampling/review/extension_novelty.md), [research_sampling/review/extension_independent_novelty.md](research_sampling/review/extension_independent_novelty.md): dated, bounded audits (1 November 2026; literature updated 4 November 2026).
- Frozen targets: [research_sampling/target.yaml](research_sampling/target.yaml), [research_sampling/extensions/anisotropic_target.yaml](research_sampling/extensions/anisotropic_target.yaml); fingerprints: [research_sampling/formula_fingerprints.json](research_sampling/formula_fingerprints.json).
- Internal review (rating-free): [research_sampling/review/REVIEW_RECORD.md](research_sampling/review/REVIEW_RECORD.md).
- [RESEARCH_GATES.json](RESEARCH_GATES.json): contribution map, sources read, limitation triage.
- [CORRECTIONS.md](CORRECTIONS.md): what changed between versions.
- Integrity: [MANIFEST.sha256](MANIFEST.sha256) and [research_sampling/MANIFEST.sha256](research_sampling/MANIFEST.sha256). Licences: [LICENSE](LICENSE). Citation: [CITATION.cff](CITATION.cff); archive metadata: [.zenodo.json](.zenodo.json).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or formal
verification. Exact stationary continuous-time Gaussian dynamics with matched rotations; position observables.
Table 1 values are computed, not proved. No statement about step-size discretisation, cost or optimal friction
(DNP found small friction, about 0.1, best in practice). No earlier statement of the main results was found in the searches recorded in the novelty report.
