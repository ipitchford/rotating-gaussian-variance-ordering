# Rotating Gaussian kinetic samplers: research bundle

Version 1.3 research materials, 4 November 2026. Author: Anonymous. Text CC0-1.0; code MIT.

Published as release 0.2.0-candidate, a citation correction of 0.1.0-candidate ([10.5281/zenodo.23941497](https://doi.org/10.5281/zenodo.23941497)): version DOI [10.5281/zenodo.23946160](https://doi.org/10.5281/zenodo.23946160) (concept DOI [10.5281/zenodo.23941496](https://doi.org/10.5281/zenodo.23941496), all versions).

## Main outcome

This bundle gives a candidate proof of a sharp universal variance-ordering theorem for the Gaussian kinetic sampler studied by Duncan, Nüsken and Pavliotis (2017), and extends it to noncommuting precision and friction matrices. It also shows that the literal finite-second-derivative form of their conjecture needs qualification for arbitrary square-integrable observables: every such variance curve is continuously differentiable, but explicit observables have a second difference quotient tending to negative infinity at zero. The manuscript gives the exact finite-curvature domain, sharp large-rotation operator rates, and boundaries imposed by finite horizons and observation schedules.

The stationary, unit-mass matrix model is

\[
dq=(p-\mu Jq)\,dt,\qquad
dp=(-Kq-\Gamma p-\mu Jp)\,dt+\sqrt{2\Gamma}\,dW,
\]

where \(K,\Gamma\) are symmetric positive definite, \(J^T=-J\), and \([J,K]=[J,\Gamma]=0\). Its invariant law is \(\mathcal N(0,K^{-1})\otimes\mathcal N(0,I)\); \(K\Gamma=\Gamma K\) is **not** required. The condition

\[
\boxed{\Gamma^3-\Gamma K-K\Gamma\succeq0}
\]

guarantees that asymptotic variance is nonincreasing in \(|\mu|\) for every real \(L^2\) position observable. Decrease is strict unless the observable is invariant under the rotation. The condition is also necessary when \(J\) is invertible; only sufficiency is asserted for general singular \(J\). For \(K=I\), \(\Gamma=\gamma I\), and a nonzero rotation, the exact scalar threshold is \(\gamma\ge\sqrt2\).

Below the threshold, observables with only even Hermite components still improve on the unrotated sampler at every rotation strength, and a single finite rotation strength improves every observable at once (Theorem 4A). The least admissible friction in Loewner order is \(\sqrt{2K}\). Replication supplies an invertible commuting rotation for arbitrary base matrices, yielding explicit limiting variance formulas for both one-replica observables and the average of two replicas. These are ordering and continuous-time variance results, not claims of optimal computational cost.

## Read the bundle

| Material | Purpose |
|---|---|
| [manuscript.md](manuscript.md), [PDF](output/pdf/rotating_gaussian_variance.pdf) | Main statements, analytic proofs, interpretation and references. |
| [BUILD.md](BUILD.md) | Pandoc and LaTeX commands, document dependencies and PDF regeneration. |
| [anisotropic_notes.md](extensions/anisotropic_notes.md), [matrix_rates_appendix.md](extensions/matrix_rates_appendix.md) | Detailed matrix-extension proofs and technical regularity/rate derivations underlying version 1.1. |
| [code/README.md](code/README.md) | Detailed reproduction instructions and interpretation of the checks. |
| [verify.py](code/verify.py), [verification_results.json](code/verification_results.json) | Scalar spectral fingerprints, covariance/Poisson checks, observation counterexamples, local limits and figure generation. |
| [verify_matrix_extension.py](code/verify_matrix_extension.py), [matrix_extension_results.json](code/matrix_extension_results.json) | Noncommuting matrix spectrum, tensor-convolution/Lyapunov agreement, exact-criterion boundary and mismatch checks. |
| [verify_below_threshold.py](code/verify_below_threshold.py), [below_threshold_results.json](code/below_threshold_results.json) | Crossing points of Table 1 (friction below the threshold), from an exact formula cross-checked by quadrature. |
| [variance_landscape.pdf](figures/variance_landscape.pdf), [PNG](figures/variance_landscape.png) | Four-panel analytic illustration; see [figure notes](figures/README.md). |
| [novelty_report.md](novelty_report.md), [extension_novelty.md](review/extension_novelty.md), [independent extension search](review/extension_independent_novelty.md) | Primary-source novelty investigations for the base result and extension. |
| [target.yaml](target.yaml), [formula_fingerprints.json](formula_fingerprints.json), [matrix target](extensions/anisotropic_target.yaml) | Frozen theorem targets, exact formulas, normalisations and prior-art search fingerprints. |
| [REVIEW_RECORD.md](review/REVIEW_RECORD.md) | Internal AI-assisted review of version 1.2: objections, responses and what was left open. |
| [LaTeX source](output/latex/rotating_gaussian_variance.tex) | Editable source for the rendered mathematical manuscript. |

## Reproduce the checks

Use Python 3.10 or later. From this bundle directory:

```bash
python -m pip install numpy scipy matplotlib
python code/verify.py --output /tmp/verification_results.json --figures-dir /tmp/figures
python code/verify_matrix_extension.py --output /tmp/matrix_extension_results.json
python code/verify_below_threshold.py --output /tmp/below_threshold_results.json
```

Each script writes its report to `--output` (default: the current directory) and never modifies the bundle unless pointed at it. Every check raises an explicit error on failure, including under `python -O`.

All three scripts accept absolute paths and can run from any working directory. `verify.py` also regenerates the PDF/PNG figure in `--figures-dir`; add `--no-figures` to skip it. An optional exact symbolic comparison is available through:

```bash
python -m pip install sympy
python code/verify.py --symbolic --no-figures
```

SymPy is unnecessary for the default runs: their exact polynomial arithmetic uses Python integers and `fractions.Fraction`. The checked environment recorded in the JSON reports is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and, for the base script, Matplotlib 3.10.8. All three supplied reports record successful checks. The scripts use deterministic formulas and quadrature; no simulation, random seed, network request or external dataset is involved. Finite checks support the proofs and do not establish their universal quantifiers.

## Conventions, scope and review status

Throughout, the variance is

\[
V_f=\lim_{T\to\infty}T\operatorname{Var}\!\left(T^{-1}\int_0^T f(q_t)\,dt\right)
=2\int_0^\infty\operatorname{Cov}(f(q_t),f(q_0))\,dt.
\]

This is **twice** the quantity \(\sigma_f^2\) in the originating [Duncan–Nüsken–Pavliotis paper](https://doi.org/10.1007/s10955-017-1906-8). Results concern stationary Gaussian dynamics and position observables. The rotations must preserve the stated symmetry. General non-Gaussian targets, arbitrary perturbations, numerical integrators and fixed-step observations do not inherit the ordering theorem automatically; explicit boundary examples are included.

No earlier statement of the main results was found in the literature search recorded in the novelty reports; Maini (2026) and Franke et al. (2021) were read in full. Standard transfer spectra, Gaussian chaos methods, unimodal convolution and existing replica coupling/averaging are acknowledged ingredients. The proposed contribution is the sharp criterion, universal ordering, exact regularity, quantitative rates and their proved consequences.

The review record summarises AI-assisted internal checks. It is **not external peer review**.
