# Structured literature-search log

**Date:** 1 November 2026.  
**Subject:** Matched rotations in Gaussian kinetic Langevin sampling, universal variance ordering, regularity and convergence rates.  
**Related records:** [Novelty report](../novelty_report.md), [frozen target](../target.yaml), [formula fingerprints](../formula_fingerprints.json).

This is a grouped log of executed query families and inspected evidence. It records query strings and consequences, rather than claiming a complete export of every ranked result. Both available public web-search engines were used. Primary full texts were opened. No author correspondence was sent.

## 1. Originating problem and possible follow-ups

| Exact query or lookup | Corpus | Inspected result / consequence |
|---|---|---|
| "Duncan" "Nüsken" "Pavliotis" "conjecture" variance | Public web, primary publisher full text | Duncan–Nüsken–Pavliotis (2017), conjecture after Eq. (27), Theorem 3 and known projection limit. |
| "Duncan" "Nüsken" "conjecture" "gamma" | Public web | No later full global-ordering theorem identified in returned results. |
| "perturbed underdamped" "monotonic" | Public web | Related sampling material; no direct collision found. |
| "perturbed underdamped" "arbitrary" observables | Public web | Located the exact all-square-integrable scope of the conjecture. |
| Exact originating title and Nüsken thesis record | Springer; Imperial Spiral | Full originating paper and thesis text/OCR examined. Thesis printed p. 62 repeats the conjecture. |
| "kinetic Langevin" "monotonicity" variance | Public web | No equivalent full theorem found in inspected results. |
| DNP Remark 5, Figure 1b and Remark 9, reopened after a mismatch calculation | Springer primary full text | Mismatched-rotation variance growth/divergence is explicitly known. Any new exact example is illustrative, not a discovery of that phenomenon. |

Primary records:

- Duncan, Nüsken and Pavliotis (2017): https://doi.org/10.1007/s10955-017-1906-8
- Nüsken (2018): https://doi.org/10.25560/63868

## 2. Spectral criterion, nonlinear Gaussian observables and unimodality

| Exact query or lookup | Corpus | Inspected result / consequence |
|---|---|---|
| "underdamped" "asymptotic variance" "unimodal" | Public web | No direct kinetic theorem found. |
| "underdamped" "unimodal" spectral density | Public web | Oscillator-spectrum aliases and unrelated stationary-density results. |
| "Langevin" "variance" "unimodality" | Public web | No direct criterion theorem found. |
| "Langevin" "asymptotic variance" "spectral density" | Public web | Related spectral/variance literature. |
| "rotating" "Gaussian process" "unimodal" spectral | Public web | No direct full rotational-variance criterion identified. |
| "rotation" "Gaussian" "spectral density" "unimodal" | Public web | Same criterion checked under the rotation alias. |
| "Gaussian process" "spectral density" "Hermite" "convolution" | Public web; author-hosted papers | Located established Gaussian Hermite and spectral-convolution machinery. |
| "spectral density" "unimodal" "variance reduction" | Public web | No direct kinetic theorem identified. |
| "Gaussian" "rotation" "variance reduction" "spectral" | Public web | Related Gaussian/nonreversible sampling material. |
| Exact Lefèvre–Utev title | Public web; Numdam primary PDF | Section 1.2 explicitly states the classical Wintner closure theorem; Theorem 1.1 generalises it. |
| Muscinelli–Gerstner–Schwalger DOI | PLOS primary full text | Sections surrounding Eqs. (37), (42)–(43) use covariance powers and spectral self-convolution. |
| Breuer–Major author-hosted PDF | Primary paper | Page 428's convolution identity and Eq. (2.1)'s Hermite covariance formula inspected. |

Primary records:

- Lefèvre and Utev (2013): https://www.numdam.org/article/PS_2013__17__605_0.pdf
- Breuer and Major (1983): https://static.renyi.hu/~major/articles/breuer.pdf
- Muscinelli, Gerstner and Schwalger (2019): https://doi.org/10.1371/journal.pcbi.1007122

**Consequence:** Spectral convolution and unimodal-convolution closure are established ingredients. The current exact application/criterion was not found as a previously stated theorem in the inspected results; no earlier statement was found.

## 3. Critical-damping formulas and classical aliases

| Exact query or lookup | Corpus | Inspected result / consequence |
|---|---|---|
| "Student" "t" "Bessel polynomials" convolution density | Public web; arXiv primary PDF | Berg–Vignat's distribution family matches the critical-damping density exactly. |
| "2" "pi" "1+x^2" "Student" convolution | Public web | Checked the density under a literal formula alias. |
| "Berg" "Vignat" "Linearization coefficients of Bessel polynomials" doi | Public web; arXiv record | Matched the preprint and published bibliographic identities. |
| "4, 5/2, 52/27" | Public web | Rational fingerprint searched; the decisive hit came after integer rescaling. |
| "2, 5, 26, 206, 2194, 29352" | Public web | Exact sequence match in experimental math's 2013/2014 posts. |
| site:oeis.org "2, 5, 26, 206" | Public web index | Search alone did not adjudicate identity; followed the linked OEIS record. |
| OEIS A090878 | OEIS full record | Defines reduced numerators of the integral I_n; substitution gives I_n=n S_n(0)/2. |
| OEIS A063170 | OEIS full record | Schenker formula gives A_n=A063170(n)/n; its terms differ from A090878's reduced numerators. |
| Amdeberhan–Callan–Moll paper linked by A063170 | Primary publisher PDF | Eqs. (1.5) and (1.9) confirm the truncated-exponential sum and integral formula. |
| Prodinger paper linked by A063170 | Primary publisher abstract | Confirmed the tree-function/Lambert-W/Ramanujan-Q aliases; no theorem claim relies on its uninspected PDF. |

Primary records:

- Berg and Vignat: https://arxiv.org/abs/math/0506458 and https://arxiv.org/pdf/math/0506458
- OEIS integral record: https://oeis.org/A090878
- OEIS Schenker record: https://oeis.org/A063170
- Amdeberhan, Callan and Moll (2013): https://math.colgate.edu/~integers/n21/n21.pdf
- Prodinger (2013): https://doi.org/10.37236/3309

Discovery lead:

- *Expmath2 – Generalized continued fractions*, 27 April 2014: https://experimentalmath.wordpress.com/2014/04/

**Consequence:** Exact ingredient collisions. No novel-density, novel-characteristic-function or novel-scalar-sequence claim survives this gate. The identified sources do not state the full kinetic variance theorem in the inspected passages.

## 4. Curvature, fractional regularity and rough observables

| Exact query or lookup | Corpus | Inspected result / consequence |
|---|---|---|
| "Langevin" "variance" "Hermite" "perturbation" | Public web | Related Gaussian/sampling literature; no exact curvature-domain theorem found. |
| "kinetic" "Langevin" "asymptotic variance" "Hermite" | Public web | Checked chaos language in the kinetic setting. |
| "Hermite" "quarter" "asymptotic variance" | Public web | No direct match found. |
| "Hermite" "asymptotic variance" "regularity" kinetic | Public web | No exact weighted angular-Hermite domain found. |
| "kinetic Langevin" "fractional" "regularity" variance | Public web | Related fractional/regularity work; no direct collision found. |
| "Langevin" "Hermite" "1/4" variance | Public web | No direct match found. |
| "Hermite" "variance" "N^{-3/4}" | Public web | No direct match found. |
| "asymptotic variance" "Langevin" "differentiability" | Public web; Imperial Spiral | Located friction-parameter differentiation in Chak's thesis and related work. |
| "asymptotic variance" "Hermite" "Sobolev" | Public web | No exact curvature-domain or explicit cusp result found. |
| "Gaussian" "variance" "Hermite" "quarter" regularity | Public web | Repeated the quarter-power alias after the final regularity statement. |

Primary record inspected:

- Chak (2022), Chapter 3 and relevant differentiation passages: https://spiral.imperial.ac.uk/bitstreams/9d7fd6ca-34e5-490b-8067-63a52579dd3f/download

**Consequence:** No direct collision found with the exact rotation-curvature condition or explicit cusp constructions. This does not clear all fractional Gaussian Sobolev literature; the number-operator quarter-power condition must be distinguished from the sharper angularly weighted domain.

## 5. Uniform convergence, sharp rates and arithmetic

| Exact query or lookup | Corpus | Inspected result / consequence |
|---|---|---|
| "Langevin" "variance" "Liouville" | Public web | No matching kinetic rate theorem found. |
| "Langevin" "small divisors" | Public web | No direct collision found. |
| "asymptotic variance" "small divisor" | Public web | Adjacent variance/arithmetic literature. |
| "asymptotic variance" "Diophantine" "Gaussian" | Public web; arXiv | Located Lachièze-Rey's Gaussian-excursion results. |
| Exact title *Diophantine Gaussian excursions and random walks* | arXiv primary PDF | Full source retrieved; setting and main statements inspected. Arithmetic Gaussian variance effects are established prior context. |
| Exact title *A note on the asymptotic variance of drift accelerated diffusions* | Public web; HAL authors' version | Uniform-over-observable convergence criterion (their Theorems 2.4 and 2.9). Authors' version read in full on 4 November 2026 (HAL hal-02266338v1). |
| "Langevin" "asymptotic variance" "monotonicity" rotation | Public web, with recent-years filter | Located established overdamped theory; no direct full kinetic-ordering collision. |
| "underdamped" "variance" "monotonicity" | Public web | Repeated sampling-specific monotonicity check. |

Primary records:

- Lachièze-Rey (2021/2022): https://arxiv.org/abs/2104.07290 and https://arxiv.org/pdf/2104.07290
- Franke, Hwang, Ouled Said and Pai (2021): https://doi.org/10.1016/j.spl.2021.109128
- Duncan, Lelièvre and Pavliotis (2016): https://doi.org/10.1007/s10955-016-1491-2

**Consequence:** No exact kinetic rate collision found. Uniform variance convergence and arithmetic effects are not claimed as new general phenomena.

## 6. Coverage notes

| Source or corpus | What was done | Effect on conclusion |
|---|---|---|
| Maini, arXiv:2610.37113, *Spectral delocalization and central limit theorems for Fourier functionals of stationary Gaussian fields* | Whole paper read on 4 November 2026 (arXiv PDF). | Same convolution-power variance credited; no monotonicity, rotated family or sampler. No pre-emption (novelty report, Section 7.1). |
| Franke–Hwang–Ouled Said–Pai (2021) | Authors' version (HAL hal-02266338v1) read in full on 4 November 2026. | Overdamped uniform convergence and monotonicity with a self-adjoint base generator; no kinetic, threshold or rate content. No pre-emption (novelty report, Section 7.1). |
| Nüsken (2018) large thesis PDF | Complete PDF inspected. | The conjecture passage and surrounding thesis results were checked beyond the abstract. |
| Authenticated MathSciNet, zbMATH, Scopus and Web of Science | No comprehensive search performed. | Public indexing coverage is incomplete. |
| Non-English historical literature and unpublished notes | Not systematically searched. | Historical priority remains uncertain. |
| Author enquiries | None completed. | No direct confirmation from the originating authors or specialist community. |

The log records what was searched and what was found. Any new structural extension requires a fresh gate. See the [novelty report](../novelty_report.md) for the outcome by contribution unit and permitted claim language.
