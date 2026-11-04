# Sharp variance ordering for rotating Gaussian samplers

*Rotation helps every observable exactly when friction is at least √2 — and what happens below it.*

Release 0.2.0-candidate, 4 November 2026 (citation correction of 0.1.0-candidate, [10.5281/zenodo.23941497](https://doi.org/10.5281/zenodo.23941497); see [CORRECTIONS.md](CORRECTIONS.md)). Author: Anonymous. Unrefereed, AI-assisted research candidate.

- Version DOI: [10.5281/zenodo.23946160](https://doi.org/10.5281/zenodo.23946160); concept DOI (all versions): [10.5281/zenodo.23941496](https://doi.org/10.5281/zenodo.23941496)
- Release page: https://evidencepress.org/releases/rotating-gaussian-variance-ordering/
- Paper: [research_sampling/output/pdf/rotating_gaussian_variance.pdf](research_sampling/output/pdf/rotating_gaussian_variance.pdf) (29 pages; Markdown source [research_sampling/manuscript.md](research_sampling/manuscript.md))

## What this is about

A Markov chain sampler estimates an average from one long simulated trajectory. Its accuracy is the long-run
(asymptotic) variance of that time average. Adding a deterministic rotation that preserves the target distribution
(a *nonreversible perturbation*) is known to help every observable for overdamped Langevin samplers (Hwang, Normand
and Wu 2015; Rey-Bellet and Spiliopoulos 2015-2016). For *kinetic* (underdamped) Langevin samplers, with position,
momentum and friction γ, Duncan, Nüsken and Pavliotis (J. Stat. Phys. 2017) proved a local improvement for linear
and quadratic observables of a Gaussian target when γ > √2, and conjectured it for every square-integrable observable.

## Main results

Exact stationary Gaussian dynamics, matched position and momentum rotations, position observables:

1. **Sharp ordering (Theorem 1).** Every square-integrable observable's long-run variance never increases with the
   rotation strength if and only if γ ≥ √2 (endpoint included): a global form of the conjecture. Mechanism: the
   oscillator's power spectrum S(ξ) = 2γ / (ξ⁴ + (γ² − 2)ξ² + 1) is single-peaked exactly when there is no
   resonance; rotation shifts the spectrum; convolution keeps single peaks single (Theorem 2).
2. **Exact curvature domain (Theorem 5, Proposition 6).** The literal second-derivative statement holds exactly on an
   explicit weighted Hermite class containing every polynomial; rough observables have sharper-than-quadratic cusps.
3. **Below the threshold (Theorem 4A).** For any friction, even observables still improve at every rotation, only
   finitely many odd Hermite degrees can be hurt, and one finite rotation strength improves every observable
   (Table 1: for γ ≥ 1 only linear parts can be hurt; at γ = 0.1, odd degrees up to 41).
4. **Large-rotation rates (Proposition 7, Theorem 8, Section 7).** Fourth-order decay for each polynomial; uniform
   worst case ~ √(2π/e)/(|μ|ω*); slower or no algebraic rate for incommensurate rotation speeds.
5. **Matrix criterion (Theorem 10, Corollaries 11-12).** For noncommuting stiffness K and friction Γ the ordering
   holds iff Γ³ − ΓK − KΓ ⪰ 0; the least safe friction is (2K)^{1/2}, a safety boundary rather than an optimal
   friction; two coupled replicas make the criterion apply to any Gaussian target.
6. **Observation schedules (Section 9).** Fixed horizons and regular sampling (aliasing) can reverse the ordering;
   independent Poisson sampling preserves it.

## Scope and credit

Gaussian targets only. Nothing is claimed about numerical cost or discretised integrators; Duncan, Nüsken and
Pavliotis found small friction (about 0.1) best in practice, and the threshold is a safety boundary, not a
recommendation. Classical ingredients are credited, not claimed: Breuer-Major Hermite covariance identities,
closure of symmetric unimodality under convolution (Lefèvre-Utev), Maini (2026)'s convolution-power variance formula,
DNP's invariant-projection limit, and established replica coupling. No earlier statement of the main results was found (see the novelty report).
Assurance: internal AI-assisted review only, no human peer review, independent reproduction or formal verification.

## Layout

| Path | Contents |
| --- | --- |
| [research_sampling/](research_sampling/) | Manuscript (Markdown, LaTeX, PDF), three verification scripts and their JSON reports, figure, extension notes, novelty reports, frozen targets, rating-free review record; see its [README](research_sampling/README.md) |
| [refs.bib](refs.bib), [refs/records/](refs/records/) | Bibliography and the Crossref, DataCite and arXiv records it was generated from |
| [AI_INDEX.md](AI_INDEX.md) | Machine-oriented map of claims, evidence and limits |
| [RESEARCH_GATES.json](RESEARCH_GATES.json) | Contribution map, sources read, limitation triage |
| [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json), [LICENSE](LICENSE) | Citation, archive metadata, licences (text CC0-1.0, code MIT) |
| [MANIFEST.sha256](MANIFEST.sha256) | SHA-256 of every file (the bundle's own [research_sampling/MANIFEST.sha256](research_sampling/MANIFEST.sha256) covers the bundle) |

## Reproduce

Python 3.10 or later with NumPy, SciPy and Matplotlib (SymPy for `--symbolic`). The scripts write only where told:

```sh
cd research_sampling
uv run --with numpy --with scipy --with matplotlib --with sympy python3 -I -B code/verify.py --symbolic --output /tmp/rg/verification_results.json --figures-dir /tmp/rg/figures
uv run --with numpy --with scipy python3 -I -B code/verify_matrix_extension.py --output /tmp/rg/matrix_extension_results.json
uv run --with numpy --with scipy python3 -I -B code/verify_below_threshold.py --output /tmp/rg/below_threshold_results.json
```

The first two take seconds; the third about two to four minutes. Add `-O`: every check raises `RuntimeError` on
failure and none relies on `assert`. At release the three scripts were replayed from fresh copies with and without
`-O` (Python 3.12.11, NumPy 2.5.4, SciPy 1.18.1, Matplotlib 3.11.2, SymPy 1.14.0): every report reproduced the shipped
JSON with identical exact fields and floats equal to round-off. The shipped reports themselves record the environment
that produced them (Python 3.11.14, NumPy 2.4.6, SciPy 1.17.1); the version sentence in the bundle README predates that
final regeneration. Finite checks support the proofs; they do not establish the universal statements.

## Licence

Text, figures, data and records: CC0-1.0. Code (`research_sampling/code/*.py` and the CI workflow): MIT. See [LICENSE](LICENSE).
