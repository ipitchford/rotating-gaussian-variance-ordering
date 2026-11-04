#!/usr/bin/env python3
"""Reproduce deterministic checks and figures for rotating Gaussian samplers.

This script is supporting verification, not a numerical proof of a theorem.
All calculations use fixed parameter grids; no random seeds or simulations are
needed. NumPy, SciPy and Matplotlib are required. SymPy is optional: add
--symbolic to compare the exact polynomial construction with a symbolic
Laplace-transform calculation.

Run from any directory:
    python verify.py
    python verify.py --symbolic  # requires an ordinary SymPy installation
"""

from __future__ import annotations

import argparse
import cmath
from fractions import Fraction
import json
import math
import os
from pathlib import Path
import platform
import sys
import tempfile

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm, solve_continuous_lyapunov

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "rotation-variance-mpl-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


ROOT = Path(__file__).resolve().parents[1]
CODE = Path(__file__).resolve().parent
FIGURES = ROOT / "figures"

# Non-standard, colour-blind-distinguishable print palette.
PLUM = "#70456F"
OCHRE = "#AD7C24"
TEAL = "#267A78"
TERRACOTTA = "#BD624B"
INK = "#2A2731"
MUTED = "#706B76"
GRID = "#E6E1E7"



def require(condition, description: str) -> None:
    """Explicit check that also runs under `python -O` (unlike assert)."""
    if not condition:
        raise RuntimeError("verification check failed: " + description)

def scalar_r(t: float, gamma: float) -> float:
    """Stationary scalar position autocorrelation, t >= 0."""
    if t < 0:
        t = -t
    a = gamma / 2.0
    if abs(gamma - 2.0) < 1e-12:
        return (1.0 + t) * math.exp(-t)
    if gamma < 2.0:
        w = math.sqrt(1.0 - a * a)
        return math.exp(-a * t) * (
            math.cos(w * t) + a * math.sin(w * t) / w
        )
    b = math.sqrt(a * a - 1.0)
    # Separate exponentials avoid overflow of cosh at large t.
    return ((a + b) * math.exp((-a + b) * t)
            - (a - b) * math.exp((-a - b) * t)) / (2.0 * b)


def scalar_r_power(t: float, n: int, gamma: float) -> float:
    if abs(gamma - 2.0) < 1e-12:
        # Stable in the large-n, small-t local-limit calculation.
        return math.exp(n * (math.log1p(abs(t)) - abs(t)))
    return scalar_r(t, gamma) ** n


def s1(omega, gamma: float):
    omega = np.asarray(omega)
    return 2.0 * gamma / (omega**4 + (gamma**2 - 2.0) * omega**2 + 1.0)


def spectrum_quad(n: int, omega: float, gamma: float) -> tuple[float, float]:
    """Fourier transform of r_gamma^n using independent quadrature."""
    f = lambda t: scalar_r_power(t, n, gamma)
    if abs(omega) < 1e-14:
        value, error = quad(f, 0.0, np.inf, epsabs=2e-12, epsrel=2e-12,
                            limit=400)
    else:
        value, error = quad(f, 0.0, np.inf, weight="cos", wvar=abs(omega),
                            epsabs=2e-12, limit=400, limlst=300)
    return 2.0 * value, 2.0 * error


def poly_add(a: list[int], b: list[int]) -> list[int]:
    result = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] += value
    for i, value in enumerate(b):
        result[i] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def exact_gamma2_polynomials(n: int) -> tuple[list[int], list[int]]:
    """Integer coefficients in x=omega^2, ascending powers.

    r_2(t)^n=(1+t)^n exp(-n t). Therefore
      S_n(omega)=2 Re sum_{k=0}^n binom(n,k) k!/(n-i omega)^(k+1).
    The common denominator is (n^2+x)^(n+1). This routine expands
    real numerators by integer arithmetic; it does not fit a rational function.
    """
    numerator = [0]
    for k in range(n + 1):
        real_part = [(-1) ** j * math.comb(k + 1, 2 * j)
                     * n ** (k + 1 - 2 * j)
                     for j in range((k + 1) // 2 + 1)]
        rest = [math.comb(n - k, j) * n ** (2 * (n - k - j))
                for j in range(n - k + 1)]
        factor = 2 * math.comb(n, k) * math.factorial(k)
        term = [factor * c for c in poly_mul(real_part, rest)]
        numerator = poly_add(numerator, term)
    denominator = [math.comb(n + 1, j) * n ** (2 * (n + 1 - j))
                   for j in range(n + 2)]
    return numerator, denominator


def exact_gamma2_value(n: int, omega: Fraction) -> Fraction:
    numerator, denominator = exact_gamma2_polynomials(n)
    x = omega * omega
    p = sum(Fraction(c) * x**j for j, c in enumerate(numerator))
    q = sum(Fraction(c) * x**j for j, c in enumerate(denominator))
    return p / q


def gamma2_spectrum(n: int, omega):
    numerator, _ = exact_gamma2_polynomials(n)
    x = np.asarray(omega, dtype=float) ** 2
    return np.polynomial.polynomial.polyval(x, numerator) / (n * n + x) ** (n + 1)


def exact_rational_checks(symbolic: bool) -> dict:
    rows = []
    max_error = 0.0
    grid = [0.0, 0.25, 1.0, 2.0, 6.0, 13.0]
    for n in range(1, 7):
        numerator, denominator = exact_gamma2_polynomials(n)
        errors = []
        for omega in grid:
            qvalue, qerror = spectrum_quad(n, omega, 2.0)
            exact_formula = float(gamma2_spectrum(n, omega))
            errors.append({"omega": omega, "rational_formula": exact_formula,
                           "quadrature": qvalue,
                           "quadrature_reported_abs_error": qerror,
                           "absolute_difference": abs(qvalue - exact_formula)})
            max_error = max(max_error, abs(qvalue - exact_formula))
        rows.append({"n": n, "variable": "x = omega^2",
                     "numerator_coefficients_ascending": numerator,
                     "denominator_coefficients_ascending": denominator,
                     "denominator_factored": f"({n*n}+x)^{n+1}",
                     "exact_values_omega_0_1_2": [str(exact_gamma2_value(n, Fraction(w)))
                                                   for w in [0, 1, 2]],
                     "quadrature_comparisons": errors})

    # Separate floating-point Laplace sum evaluates a different expression.
    max_laplace_error = 0.0
    for n in range(1, 7):
        for omega in grid:
            laplace = 2.0 * sum(math.comb(n, k) * math.factorial(k)
                                / complex(n, -omega) ** (k + 1)
                                for k in range(n + 1)).real
            max_laplace_error = max(max_laplace_error,
                                    abs(laplace - float(gamma2_spectrum(n, omega))))

    symbolic_result = {"requested": symbolic, "performed": False}
    if symbolic:
        import sympy as sp
        w = sp.symbols("w", real=True)
        checks = []
        for n in range(1, 7):
            numerator, _ = exact_gamma2_polynomials(n)
            proposed = sum(c * w ** (2 * j) for j, c in enumerate(numerator)) / (n*n + w*w)**(n+1)
            original = 2 * sp.re(sum(sp.binomial(n, k) * sp.factorial(k)
                                    / (n-sp.I*w)**(k+1) for k in range(n+1)))
            residual = sp.factor(sp.together(sp.expand_complex(original) - proposed))
            checks.append({"n": n, "symbolic_residual": str(residual),
                           "exact_identity": residual == 0})
        symbolic_result = {"requested": True, "performed": True,
                           "sympy_version": sp.__version__, "identities": checks}
        require(all(row["exact_identity"] for row in checks), 'all(row["exact_identity"] for row in checks)')
    require(max_error < 2e-10, 'max_error < 2e-10')
    require(max_laplace_error < 2e-10, 'max_laplace_error < 2e-10')
    return {"exact_integer_polynomial_construction": True, "orders": rows,
            "maximum_quadrature_difference": max_error,
            "maximum_laplace_sum_difference": max_laplace_error,
            "optional_symbolic_check": symbolic_result}


def drift_matrix(gamma: float, mu: float, j: np.ndarray) -> np.ndarray:
    d = len(j)
    eye = np.eye(d)
    return np.block([[-mu*j, eye], [-eye, -gamma*eye-mu*j]])


def covariance_and_lyapunov_checks() -> dict:
    j2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    j4 = np.zeros((4, 4))
    j4[:2, :2] = j2
    j4[2:, 2:] = 1.7 * j2
    covariance_error = 0.0
    invariant_error = 0.0
    number_covariance_checks = 0
    for gamma in [0.8, math.sqrt(2.0), 2.0, 3.3]:
        for mu in [0.0, 0.8, 5.2]:
            m = drift_matrix(gamma, mu, j4)
            q = np.diag([0.0]*4 + [2.0*gamma]*4)
            sigma = solve_continuous_lyapunov(m, -q)
            invariant_error = max(invariant_error,
                                  float(np.max(np.abs(sigma-np.eye(8)))))
            for t in [0.0, 0.1, 1.0, 3.7]:
                computed = (expm(m*t) @ sigma)[:4, :4]
                prediction = scalar_r(t, gamma) * expm(-mu*j4*t)
                covariance_error = max(covariance_error,
                                       float(np.max(np.abs(computed-prediction))))
                number_covariance_checks += 1

    # Linear Poisson-equation solve and an independent spectral calculation.
    b = np.array([0.8, -0.3, 0.5, 0.2, 0.0, 0.0, 0.0, 0.0])
    linear_rows = []
    for gamma in [0.8, math.sqrt(2.0), 2.0, 3.3]:
        for mu in [0.0, 0.3, 1.7, 5.0]:
            m = drift_matrix(gamma, mu, j4)
            h = np.linalg.solve(-m.T, b)
            poisson = float(2 * b @ h)
            spectral = float(np.sum(b[:2]**2)*s1(mu, gamma)
                             +np.sum(b[2:4]**2)*s1(1.7*mu, gamma))
            linear_rows.append({"gamma": gamma, "mu": mu,
                                "poisson_linear_solve": poisson,
                                "spectral": spectral,
                                "absolute_difference": abs(poisson-spectral)})

    # Quadratic Poisson solution is a continuous Lyapunov equation.
    k = np.array([[0.8, 0.3], [0.3, -0.2]])
    radial = np.trace(k)/2.0 * np.eye(2)
    traceless = k-radial
    c = np.zeros((4, 4))
    c[:2, :2] = k
    quadratic_rows = []
    for gamma in [0.8, math.sqrt(2.0), 2.0, 3.3]:
        for mu in [0.0, 0.3, 1.7, 5.0]:
            m = drift_matrix(gamma, mu, j2)
            h = solve_continuous_lyapunov(m.T, -c)
            lyapunov = float(4*np.trace(c@h))
            h0, _ = spectrum_quad(2, 0.0, gamma)
            hmu, _ = spectrum_quad(2, 2*mu, gamma)
            spectral = float(2*np.trace(radial@radial)*h0
                             +2*np.trace(traceless@traceless)*hmu)
            residual = float(np.max(np.abs(m.T@h+h@m+c)))
            quadratic_rows.append({"gamma": gamma, "mu": mu,
                                   "lyapunov": lyapunov,
                                   "spectral_quadrature": spectral,
                                   "absolute_difference": abs(lyapunov-spectral),
                                   "lyapunov_residual_max_abs": residual})
    max_linear = max(x["absolute_difference"] for x in linear_rows)
    max_quadratic = max(x["absolute_difference"] for x in quadratic_rows)
    require(covariance_error < 1e-11, 'covariance_error < 1e-11')
    require(invariant_error < 1e-11, 'invariant_error < 1e-11')
    require(max_linear < 1e-11, 'max_linear < 1e-11')
    require(max_quadratic < 5e-10, 'max_quadratic < 5e-10')
    return {"stationary_covariance_checks": number_covariance_checks,
            "maximum_covariance_factorisation_error": covariance_error,
            "maximum_stationary_covariance_error": invariant_error,
            "linear_observable_coefficients": b[:4].tolist(),
            "linear_checks": linear_rows,
            "maximum_linear_error": max_linear,
            "quadratic_observable_matrix": k.tolist(),
            "quadratic_checks": quadratic_rows,
            "maximum_quadratic_error": max_quadratic}


def finite_horizon(mu: float) -> float:
    z = complex(-1.0, mu)
    return 2.0 * (-1/z+2*cmath.exp(z)/z**2+2*(1-cmath.exp(z))/z**3).real


def skeleton(mu: float, delta: float = 1.0) -> float:
    z = cmath.exp(complex(-delta, mu*delta))
    return 1.0 + 2.0 * (z/(1-z) + delta*z/(1-z)**2).real


def boundary_checks() -> dict:
    mus = [0.0, 0.4, math.pi, 2*math.pi, 3*math.pi, 4*math.pi]
    finite_rows = []
    for mu in mus:
        exact_formula = finite_horizon(mu)
        qvalue, qerror = quad(lambda t: 2*(1-t*t)*math.exp(-t)*math.cos(mu*t),
                              0.0, 1.0, epsabs=1e-13, epsrel=1e-13)
        finite_rows.append({"mu": mu, "formula": exact_formula,
                            "quadrature": qvalue, "quadrature_error": qerror,
                            "absolute_difference": abs(exact_formula-qvalue)})

    upper_2pi = Fraction(1548, 50653)
    lower_3pi = Fraction(70456, 2260713)
    gap = lower_3pi-upper_2pi
    require(gap > 0, 'gap > 0')
    require(finite_horizon(2*math.pi) < float(upper_2pi), 'finite_horizon(2*math.pi) < float(upper_2pi)')
    require(finite_horizon(3*math.pi) > float(lower_3pi), 'finite_horizon(3*math.pi) > float(lower_3pi)')

    periodicity_rows = []
    maximum_periodicity_error = 0.0
    maximum_series_error = 0.0
    for delta in [0.25, 1.0, 2.0]:
        for mu in [0.0, 0.4, 1.7, 5.3]:
            formula = skeleton(mu, delta)
            repeated = skeleton(mu+2*math.pi/delta, delta)
            # 500 terms suffice for the minimum delta=0.25 used here.
            series = 1+2*sum((1+k*delta)*math.exp(-k*delta)
                              *math.cos(k*delta*mu) for k in range(1, 501))
            perr = abs(formula-repeated)
            serr = abs(formula-series)
            maximum_periodicity_error = max(maximum_periodicity_error, perr)
            maximum_series_error = max(maximum_series_error, serr)
            periodicity_rows.append({"delta": delta, "mu": mu,
                                     "formula": formula, "periodic_repeat": repeated,
                                     "500_term_series": series,
                                     "periodicity_error": perr,
                                     "series_difference": serr})

    # Independent gamma-arrival moments for the Poisson-sampling identity.
    # If T_k~Gamma(k,lambda), E[(1+T_k)e^{(-1+i mu)T_k}]
    # = (lambda/(lambda+1-i mu))^k [1+k/(lambda+1-i mu)].
    poisson_rows = []
    max_poisson_error = 0.0
    for rate in [0.5, 1.0, 3.0]:
        for mu in [0.0, 0.3, 1.7, 5.0]:
            denominator = complex(rate+1.0, -mu)
            z = rate/denominator
            arrival_sum = 1+2*sum((z**k*(1+k/denominator)).real
                                  for k in range(1, 501))
            identity = float(1+rate*s1(mu, 2.0))
            error = abs(arrival_sum-identity)
            max_poisson_error = max(max_poisson_error, error)
            poisson_rows.append({"rate": rate, "mu": mu,
                                 "500_gamma_arrival_terms": arrival_sum,
                                 "variance_identity": identity,
                                 "absolute_difference": error})
    require(maximum_periodicity_error < 2e-11, 'maximum_periodicity_error < 2e-11')
    require(maximum_series_error < 2e-11, 'maximum_series_error < 2e-11')
    require(max_poisson_error < 2e-11, 'max_poisson_error < 2e-11')
    return {"finite_horizon": finite_rows,
            "finite_horizon_exact_order_certificate": {
                "assumptions": "9 < pi^2 < 10 and 1/e > 1/3",
                "upper_bound_W_2pi": str(upper_2pi),
                "lower_bound_W_3pi": str(lower_3pi),
                "exact_positive_bound_gap": str(gap),
                "numerical_W_2pi": finite_horizon(2*math.pi),
                "numerical_W_3pi": finite_horizon(3*math.pi)},
            "skeleton": periodicity_rows,
            "maximum_skeleton_periodicity_error": maximum_periodicity_error,
            "maximum_skeleton_series_error": maximum_series_error,
            "poisson_observation": poisson_rows,
            "maximum_poisson_identity_error": max_poisson_error}


def local_limit_checks() -> dict:
    xgrid = [0.0, 0.5, 1.0, 2.0, 3.0]
    rows = []
    for gamma in [math.sqrt(2.0), 2.0, 3.0]:
        for n in [100, 1000, 10000]:
            rt = math.sqrt(n)
            kernel = lambda u: scalar_r_power(u/rt, n, gamma)
            spectra = []
            for x in xgrid:
                observed, err = quad(lambda u: 2*kernel(u)*math.cos(x*u),
                                      0.0, 30.0, epsabs=2e-11, epsrel=2e-11,
                                      limit=300)
                limit = math.sqrt(2*math.pi)*math.exp(-x*x/2)
                spectra.append({"scaled_frequency_x": x,
                                "sqrt_n_Sn_sqrt_n_x": observed,
                                "limiting_gaussian": limit,
                                "absolute_error": abs(observed-limit),
                                "quadrature_reported_error": err})
            curvature, cerr = quad(lambda u: u*u*kernel(u), 0.0, 30.0,
                                   epsabs=2e-11, epsrel=2e-11, limit=300)
            target = math.sqrt(math.pi/2)
            rows.append({"gamma": gamma, "n": n,
                         "spectral_grid": spectra,
                         "maximum_spectral_grid_error": max(v["absolute_error"] for v in spectra),
                         "n_to_three_halves_integral_t_squared_rn": curvature,
                         "curvature_limit": target,
                         "curvature_relative_error": curvature/target-1,
                         "quadrature_reported_error": cerr})
    observed_rates = []
    for gamma in [math.sqrt(2.0), 2.0, 3.0]:
        subset = [row for row in rows if row["gamma"] == gamma]
        for first, second in zip(subset[:-1], subset[1:]):
            rate = math.log(second["maximum_spectral_grid_error"]
                            /first["maximum_spectral_grid_error"]) / math.log(second["n"]/first["n"])
            observed_rates.append({"gamma": gamma, "from_n": first["n"],
                                   "to_n": second["n"],
                                   "observed_log_log_error_slope": rate})
    # A finite numerical grid cannot establish a uniform limit or a rate.
    require(all(row["maximum_spectral_grid_error"] < 0.3 for row in rows), 'all(row["maximum_spectral_grid_error"] < 0.3 for row in rows)')
    return {"interpretation": "Numerical consistency checks only; finite grids do not prove the local limit or its rate.",
            "integration_interval_in_rescaled_variable": [0.0, 30.0],
            "rows": rows, "observed_rates": observed_rates}


def make_figure(figures_dir: Path) -> list[str]:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.titlesize": 12, "axes.titleweight": "semibold",
        "axes.labelsize": 10, "axes.labelcolor": INK,
        "text.color": INK, "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.edgecolor": "#CFC8D1", "axes.spines.top": False,
        "axes.spines.right": False, "axes.linewidth": 0.7,
        "grid.color": GRID, "grid.linewidth": 0.6,
        "legend.frameon": False, "legend.fontsize": 9,
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "savefig.facecolor": "white",
    })
    fig, axes = plt.subplots(2, 2, figsize=(11.8, 8.35))
    fig.subplots_adjust(left=0.075, right=0.978, bottom=0.092, top=0.865,
                        hspace=0.49, wspace=0.30)
    fig.suptitle("Rotation and variance in a matched Gaussian sampler",
                 x=0.075, y=0.965, ha="left", fontsize=17, fontweight="semibold")
    fig.text(0.075, 0.922,
             "Exact formula curves · stationary initial distribution · dimensionless parameters",
             fontsize=10.5, color=MUTED)

    ax = axes[0, 0]
    mu = np.linspace(0, 3, 700)
    for gamma, colour, label in [(0.8, TERRACOTTA, r"$\gamma=0.8$"),
                                  (math.sqrt(2), PLUM, r"$\gamma=\sqrt{2}$"),
                                  (2.0, TEAL, r"$\gamma=2$"),
                                  (3.0, OCHRE, r"$\gamma=3$")]:
        ax.plot(mu, s1(mu, gamma)/(2*gamma), color=colour, lw=2.15, label=label)
    ax.axhline(1, color="#ABA4AE", lw=0.8, ls=(0, (3, 3)), zorder=0)
    ax.set(title="A  The friction threshold is sharp", xlabel=r"Rotation strength $\mu$",
           ylabel=r"$V_{q_1}(\mu)/V_{q_1}(0)$", xlim=(0, 3), ylim=(0, 2.03))
    ax.text(0.51, 1.92, "Initial increase below the threshold", color=TERRACOTTA,
            fontsize=8.7, ha="left", va="top")
    ax.legend(loc="upper right", bbox_to_anchor=(1.02, 0.79), ncol=1)
    ax.grid(axis="y")

    ax = axes[0, 1]
    mu = np.linspace(0, 2.5, 650)
    for n, colour in [(1, TEAL), (2, PLUM), (4, OCHRE), (6, TERRACOTTA)]:
        y = gamma2_spectrum(n, n*mu)/float(gamma2_spectrum(n, 0))
        ax.plot(mu, y, color=colour, lw=2.15, label=f"degree {n}")
    ax.set(title="B  Nonlinear angular modes also improve", xlabel=r"Rotation strength $\mu$",
           ylabel=r"$V_{\phi_n}(\mu)/V_{\phi_n}(0)$", xlim=(0, 2.5), ylim=(-0.025, 1.04))
    ax.text(0.98, 0.96, r"$\gamma=2$, angular frequency $n$", transform=ax.transAxes,
            ha="right", va="top", fontsize=9, color=MUTED)
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.83))
    ax.grid(axis="y")

    ax = axes[1, 0]
    mu = np.linspace(math.pi, 4*math.pi, 900)
    ax.plot(mu, [finite_horizon(float(x)) for x in mu], color=TERRACOTTA,
            lw=2.15, label=r"Finite horizon $T=1$")
    ax.plot(mu, s1(mu, 2.0), color=PLUM, lw=1.8, ls=(0, (4, 2)),
            label="Continuous-time asymptotic")
    ax.scatter([2*math.pi, 3*math.pi], [finite_horizon(2*math.pi), finite_horizon(3*math.pi)],
               color=TERRACOTTA, edgecolors="white", linewidths=1, s=44, zorder=4)
    ax.annotate("0.0193", (2*math.pi, finite_horizon(2*math.pi)),
                xytext=(-4, -19), textcoords="offset points", ha="center",
                fontsize=9, color=TERRACOTTA)
    ax.annotate("0.0403", (3*math.pi, finite_horizon(3*math.pi)),
                xytext=(0, 8), textcoords="offset points", ha="center",
                fontsize=9, color=TERRACOTTA)
    ax.set(title="C  A finite horizon can reverse the ordering",
           xlabel=r"Rotation strength $\mu$", ylabel="Variance (log scale)",
           xlim=(math.pi, 4*math.pi), ylim=(1.1e-4, 0.7), yscale="log")
    ax.set_xticks([k*math.pi for k in range(1, 5)],
                  [r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax.legend(loc="lower left", fontsize=8.6)
    ax.grid(axis="y", which="major")

    ax = axes[1, 1]
    mu = np.linspace(0, 4*math.pi, 1100)
    ax.plot(mu, [skeleton(float(x), 1.0) for x in mu], color=OCHRE, lw=2.15,
            label=r"Regular: interval $\Delta=1$")
    ax.plot(mu, 1+s1(mu, 2.0), color=TEAL, lw=2.15,
            label=r"Poisson: rate $\lambda=1$")
    ax.axhline(1, color=TEAL, lw=0.8, ls=(0, (2, 3)), alpha=0.6)
    for x in [2*math.pi, 4*math.pi]:
        ax.axvline(x, color=GRID, lw=0.8, zorder=0)
    ax.set(title="D  Observation schedules change the guarantee",
           xlabel=r"Rotation strength $\mu$", ylabel="Asymptotic variance per sample",
           xlim=(0, 4*math.pi), ylim=(-0.08, 5.25))
    ax.set_xticks([k*math.pi for k in range(5)],
                  ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax.yaxis.set_major_locator(MaxNLocator(6, integer=True))
    ax.legend(loc="upper right", fontsize=8.7)
    ax.grid(axis="y")

    fig.text(0.075, 0.025,
             r"C–D: $\gamma=2$, $f(q)=q_1$. Poisson observation preserves monotonicity with an added variance floor.",
             fontsize=9.2, color=MUTED)
    figures_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for suffix in ["pdf", "png"]:
        path = figures_dir / f"variance_landscape.{suffix}"
        fig.savefig(path, dpi=220 if suffix == "png" else None,
                    metadata={"Title": "Rotation and variance in a matched Gaussian sampler"})
        paths.append(path.name)
    plt.close(fig)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbolic", action="store_true",
                        help="also run exact SymPy identities; SymPy must be installed")
    parser.add_argument("--no-figures", action="store_true",
                        help="run checks without regenerating the publication figure")
    parser.add_argument("--output", type=Path, default=Path.cwd() / "verification_results.json",
                        help="JSON report path (default: verification_results.json in the current directory)")
    parser.add_argument("--figures-dir", type=Path, default=Path.cwd() / "figures",
                        help="directory for the regenerated figure (default: ./figures in the current directory)")
    args = parser.parse_args()
    results = {
        "purpose": "Reproducible deterministic consistency checks supporting, but not replacing, analytic proofs.",
        "date": "2026-11-01",
        "variance_convention": "V_f=lim_{T->infinity} T Var(T^{-1} integral_0^T f(q_t)dt)=2 integral_0^infinity Cov(f(q_t),f(q_0))dt",
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
        "exact_gamma2_spectra": exact_rational_checks(args.symbolic),
        "matrix_and_poisson_checks": covariance_and_lyapunov_checks(),
        "observation_boundaries": boundary_checks(),
        "local_gaussian_limits": local_limit_checks(),
    }
    results["figures"] = [] if args.no_figures else make_figure(args.figures_dir)
    results["status"] = "all stated deterministic checks passed"
    out = args.output
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps({
        "status": results["status"],
        "json": str(out),
        "figures": results["figures"],
        "max_spectral_quadrature_error": results["exact_gamma2_spectra"]["maximum_quadrature_difference"],
        "max_covariance_error": results["matrix_and_poisson_checks"]["maximum_covariance_factorisation_error"],
        "max_linear_error": results["matrix_and_poisson_checks"]["maximum_linear_error"],
        "max_quadratic_error": results["matrix_and_poisson_checks"]["maximum_quadratic_error"],
    }, indent=2))


if __name__ == "__main__":
    main()
