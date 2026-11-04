# Reproduce the mathematical checks and figure

Use Python 3.10 or later. From this `code` directory, run:

```bash
python -m pip install numpy scipy matplotlib
python verify.py --output /tmp/verification_results.json --figures-dir /tmp/figures
python verify_matrix_extension.py --output /tmp/matrix_extension_results.json
python verify_below_threshold.py --output /tmp/below_threshold_results.json
```

Reports and figures go to the paths given (defaults: the current directory). Checks raise `RuntimeError` on failure and do not rely on `assert`, so they also run under `python -O`.

All three scripts can be invoked by absolute path from any working directory. From the bundle root, prefix their names with `code/`. No script uses network access, simulation, external data or a random seed.

The shipped reports in `code/` and the figure in `figures/` were produced with `--output` and `--figures-dir` pointing at those locations. For a further symbolic identity check in the base script:

```bash
python -m pip install sympy
python verify.py --symbolic
```

The optional SymPy installation is not required for the default checks. Exact rational polynomial coefficients are constructed with Python integer arithmetic and `fractions.Fraction`, independently of SymPy. Use `python verify.py --no-figures` to skip figure regeneration. The matrix script requires only NumPy and SciPy; Matplotlib is needed by the base script even when figure generation is skipped.

The supplied reports record successful runs with Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and, for the base script, Matplotlib 3.10.8. Each report records its own package versions and check results; the source files do not require those exact versions.

## Base script: `verify.py`

The script checks:

1. Exact rational spectral fingerprints for the first six Hermite orders when the friction is 2, including their values at angular frequencies 0, 1 and 2. It compares the rational expressions with direct cosine quadrature and a separate complex Laplace sum. With `--symbolic`, SymPy also simplifies six rational-expression differences exactly to zero.
2. The stationary covariance and its rotating scalar factorisation against matrix exponentials and a continuous Lyapunov equation on a four-dimensional position space.
3. Linear-observable asymptotic variances against an independent Poisson-equation linear solve; quadratic-observable variances against an independent continuous Lyapunov solve.
4. The finite-horizon counterexample by exact formula, direct quadrature, and an exact positive rational bound separating the two specified variances.
5. Fixed-step periodicity against direct covariance sums and the Poisson-observation identity against summed Gamma waiting-time moments.
6. The large-Hermite-order spectral and curvature limits at orders 100, 1,000 and 10,000, for three friction values. The report includes observed error slopes, without treating them as proof of an asymptotic rate.

The four-panel figure shows the sharp friction threshold, higher angular modes, the finite-horizon reversal, and the contrast between regular and independent Poisson observation. All curves use analytic formulas. The local-limit calculations use a finite rescaled integration interval [0, 30]; the analytic manuscript, rather than this quadrature, supplies the tail justification.

## Matrix extension: `verify_matrix_extension.py`

The extension checks the unit-mass model

\[
dq=(p-\mu Jq)\,dt,\qquad
dp=(-Kq-\Gamma p-\mu Jp)\,dt+\sqrt{2\Gamma}\,dW,
\]

where \(K,\Gamma\succ0\), \(J^T=-J\), and \(J\) commutes with both matrices. The example deliberately has \(K\Gamma\ne\Gamma K\). The analytic ordering condition is \(\Gamma^3-\Gamma K-K\Gamma\succeq0\).

The script checks:

1. The noncommuting example's exact matrix certificate and commuting-rotation identities, and the inverse-polynomial spectrum against an independent complex transfer-function calculation.
2. Positive Loewner differences on a fixed frequency grid and linear-observable variances against a separate Poisson-equation solve.
3. A pure angular-frequency-two quadratic: its matrix tensor-convolution spectrum, evaluated by quadrature, agrees with an independent continuous Lyapunov calculation at three amplitudes.
4. A counterexample showing that the weaker inequality \(\Gamma^2\succeq2K\) is insufficient without commutation: the exact certificate is indefinite and a selected linear variance increases at a small positive amplitude.
5. The zero-certificate identity at the least admissible friction \(\Gamma=\sqrt{2K}\).
6. An explicit precision-mismatch quadratic variance formula against Lyapunov calculations at several precisions and amplitudes. This illustrates a known failure mechanism outside the matched rotation assumptions; it is not a claim of a new replica construction.

`matrix_extension_results.json` contains the matrices, eigenvalues, comparison errors, quadrature error estimates and environment versions. The matrix script generates no figure. Its finite checks do not prove the tensor-convolution lemma, all-\(L^2\) ordering, the least-friction theorem, regularity or operator-rate results; those are analytic arguments in the manuscript and extension notes.

## Below threshold: `verify_below_threshold.py`

For friction values 0.1, 0.3, 0.5, 0.8, 1.0 and 1.2, it computes the crossing points of Table 1 for odd Hermite degrees up to 121. It uses an exact exponential-sum formula for the spectra (falling back to fine-grid quadrature where that sum would lose digits), cross-checks against adaptive quadrature, confirms the linear crossing point equals the square root of (2 minus the friction squared), and confirms that even degrees never exceed their zero-frequency value. These are finite computations; Theorem 4A is proved analytically.

## Interpretation and conventions

The variance convention is

\[
V_f=\lim_{T\to\infty}T\operatorname{Var}\!\left(T^{-1}\int_0^T f(q_t)\,dt\right)
=2\int_0^\infty\operatorname{Cov}(f(q_t),f(q_0))\,dt.
\]

This is twice the quantity called `sigma_f^2` in Duncan, Nüsken and Pavliotis (2017). All checks use stationary initial distributions and position-only observables. Parameters in the figures are dimensionless.

Finite grids and floating-point agreement do not prove monotonicity for all parameters, establish a central limit theorem, validate an arbitrary numerical integrator, or settle novelty. The analytic proofs make the universal claims. The exact rational bound in the finite-horizon check certifies only that explicit counterexample.
