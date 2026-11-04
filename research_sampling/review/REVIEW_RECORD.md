# Review record for version 1.2

This file summarises the internal review of this manuscript and what changed in response. The reviews were AI-assisted: five simulated reviewers (editor, proof-checking, domain, cross-disciplinary and devil's advocate) and a separate adversarial mathematical audit by a different AI model, plus a clean replay of every script from a fresh extraction. **None of this is external human peer review.**

## Verdict on correctness

No reviewer or audit found a critical or major correctness error. The following were recomputed independently and matched the manuscript: the spectrum (8)–(9) and the endpoint $\gamma=\sqrt2$; the noncommuting failure witness (variance $118+12\mu^2+O(\mu^4)$); the admissible example (determinant 1056); the counterexample showing $\Gamma^2\succeq2K$ is not enough (determinant $-1/16$); the Section 9.2 rational certificate; the constant $\sqrt{2\pi/e}$; and the Proposition 6 constants (which converge slowly).

## Substantive objections and responses

| Objection | Response in version 1.2 |
|---|---|
| "Corrects their claim" overstates matters: DNP conjectured, not proved, the all-$L^2$ derivative statement. | Reworded throughout. The paper proves a global form of the conjecture, and says precisely where the literal second-derivative form needs qualification (invariant observables, which DNP's nondegeneracy conditions exclude, and rough observables). |
| The conjecture's location was misdescribed. | It follows DNP's parameter conditions, numbered (27) in the journal and (35a)–(35c) in arXiv v1; both are now given. DNP's own small-friction numerics are credited. |
| The headline theorem is close to immediate from classical tools. | Accepted in part. The classical ingredients are credited explicitly, and a plain-language box now states the mechanism in a paragraph. The contribution claimed is the exact criterion and threshold, and what follows from it. |
| The overdamped literature, where nonreversible perturbations improve every observable, is missing. | Added (Hwang–Normand–Wu 2015; Rey-Bellet–Spiliopoulos 2015a, 2015b, 2016) and contrasted: in the kinetic case improvement depends on friction. |
| A recent paper (Maini 2026) has the same convolution-power variance formula. | Cited next to Breuer–Major. It does not treat monotonicity or samplers. |
| The optimal-drift and friction-choice literature is not positioned. | Added (Hwang–Hwang-Ma–Sheu 1993; Lelièvre–Nier–Pavliotis 2013; Guillin–Monmarché 2016; Kaiser–Jack–Zimmer 2017), with Chak et al. (2023). |
| The practically used regime, friction below $\sqrt2$, is barely addressed. | New Theorem 4A: even observables improve at every rotation; only finitely many odd degrees can be hurt; one finite amplitude improves every observable. Table 1 gives computed crossing points. |
| $(2K)^{1/2}$ could be read as a recommended friction. | Stated explicitly that it is a safety boundary, not an optimum. |
| The abstract is over-packed and the paper hard to navigate. | Abstract shortened; Section 1 now has context, a plain-language box, a results table, a roadmap and a notation note. |
| Several steps were compressed (tensor-convolution monotonicity, Lemma 3's weak case, the Section 9.2 bound). | Lemma 10A now states and proves the tensor-convolution step, including compression to symmetric tensors; Lemma 3's weak case and the Section 9.2 grouping are written out. Lemma 3 now requires strictly positive integral, which excludes a null-set counterexample. |
| The scripts used `assert` (silently skipped under `python -O`) and wrote results into the bundle by default. | All checks now raise explicit errors; output paths default to the current directory. |

## Not done, and why

Exact discrete-time criteria for a splitting integrator, perturbative results for near-Gaussian targets, unmatched rotations, and a full comparison of rotation against friction retuning were suggested. They are larger projects and are listed as open in Section 10. A general stride-sampling rule was also suggested; Section 9.3 gives the exact aliasing mechanism but no general rule.

## Earlier versions

Versions 1.0 and 1.1 were reviewed internally before this round. The version 1.0 manuscript is preserved in `review/manuscript_v1.0.md`. The novelty reports in this folder record the bounded literature searches.
