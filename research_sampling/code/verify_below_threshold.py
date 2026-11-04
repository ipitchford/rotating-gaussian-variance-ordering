#!/usr/bin/env python3
"""Below-threshold comparison with the unrotated sampler (Section 7A of the manuscript).

For friction 0 < gamma < 2 the normalised oscillator covariance is
    r(t) = c e^{lambda t} + conj(c) e^{conj(lambda) t},  t >= 0,
with lambda = -gamma/2 + i w, w = sqrt(1 - gamma^2/4), c = (1 - i gamma/(2 w))/2.
Expanding r^n binomially gives the exact closed form
    S_n(xi) = 2 Re sum_k binom(n,k) c^k conj(c)^(n-k) / (i xi - k lambda - (n-k) conj(lambda)),
so no quadrature is involved.

The script computes, for odd n, the crossing point
    Xi_n(gamma) = sup{ xi > 0 : S_n(xi) > S_n(0) }   (0 if the set is empty),
checks the closed form against direct quadrature at sample points, checks the
linear case Xi_1 = sqrt(2 - gamma^2), checks that even n never exceed S_n(0), and
records the largest odd degree with a crossing among n <= N_SCAN.

These are finite numerical computations. They illustrate Theorem 13; they do not
prove the statement about every degree, which is proved analytically.
Checks raise RuntimeError on failure, so they also run under `python -O`.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np
from scipy import integrate

GAMMAS = [0.1, 0.3, 0.5, 0.8, 1.0, 1.2]
N_SCAN = 121


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError("check failed: " + msg)


def params(g: float):
    w = math.sqrt(1.0 - g * g / 4.0)
    lam = complex(-g / 2.0, w)
    c = complex(0.5, -g / (4.0 * w))
    return w, lam, c


def spectrum(n: int, g: float, xi: np.ndarray) -> np.ndarray:
    """Exact binomial form when its cancellation bound (2|c|)^n is small, otherwise
    trapezoidal quadrature of r^n on a fine grid (the binomial sum then loses digits)."""
    w, lam, c = params(g)
    if (2 * abs(c)) ** n > 1e3:
        return spectrum_grid(n, g, xi)
    k = np.arange(n + 1)
    logb = np.array([math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) for j in k])
    coef = np.exp(logb) * c ** k * np.conj(c) ** (n - k)
    rate = k * lam + (n - k) * np.conj(lam)
    den = 1j * xi[:, None] - rate[None, :]
    return 2.0 * np.real((coef[None, :] / den).sum(axis=1))


def spectrum_grid(n: int, g: float, xi: np.ndarray) -> np.ndarray:
    w, _, _ = params(g)
    upper = 80.0 / (n * g / 2.0) + 10.0
    dt = min(0.005, 0.25 / (float(np.max(xi)) + 1.0))
    t = np.arange(0.0, upper + dt, dt)
    rt = np.exp(-g * t / 2.0) * (np.cos(w * t) + g / (2.0 * w) * np.sin(w * t))
    y = rt ** n
    wts = np.full(t.size, dt)
    wts[0] = wts[-1] = dt / 2
    yw = y * wts
    out = np.empty(xi.size)
    for i in range(0, xi.size, 400):
        out[i:i + 400] = 2.0 * (np.cos(np.outer(xi[i:i + 400], t)) @ yw)
    return out


def r_fun(g: float, t: float) -> float:
    w = math.sqrt(1.0 - g * g / 4.0)
    return math.exp(-g * t / 2.0) * (math.cos(w * t) + g / (2.0 * w) * math.sin(w * t))


def quad_spectrum(n: int, g: float, xi: float) -> float:
    upper = 60.0 / (n * g / 2.0)
    val, _ = integrate.quad(lambda t: r_fun(g, t) ** n * math.cos(xi * t), 0.0, upper,
                            limit=4000, epsabs=1e-13, epsrel=1e-11)
    return 2.0 * val


def crossing(n: int, g: float) -> tuple[float, float]:
    w, _, _ = params(g)
    # S_n(xi) <= 2 * integral |r|^n, and its spectral mass sits within a few
    # multiples of sqrt(n) of the origin; the scan window covers both resonances
    # (odd multiples of w) and the Gaussian bulk.
    xmax = min(n * w + 12.0, 8.0 * math.sqrt(n) + 12.0)
    xi = np.linspace(0.0, xmax, int(xmax / 0.001) + 1)
    s = spectrum(n, g, xi)
    s0 = s[0]
    excess = s[1:] - s0
    rel = float(excess.max() / s0)
    idx = np.where(excess > 1e-9 * abs(s0))[0]
    if idx.size == 0:
        return 0.0, rel
    j = idx[-1] + 1  # last grid point above S_n(0)
    lo, hi = xi[j], xi[min(j + 1, xi.size - 1)]
    f = lambda x: spectrum(n, g, np.array([x]))[0] - s0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), rel


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=Path.cwd() / "below_threshold_results.json",
                    help="report path (default: below_threshold_results.json in the current directory)")
    args = ap.parse_args()

    report = {"description": "Below-threshold crossing points Xi_n(gamma) for odd Hermite degrees",
              "n_scan": N_SCAN, "gammas": {}}
    # 1. closed form against quadrature
    qerr = 0.0
    for g in (0.3, 1.0):
        for n in (1, 2, 3, 5):
            for x in (0.0, 0.7, 1.9, 3.1):
                a = spectrum(n, g, np.array([x]))[0]
                b = quad_spectrum(n, g, x)
                qerr = max(qerr, abs(a - b))
    check(qerr < 1e-8, f"closed form vs quadrature {qerr}")
    report["closed_form_vs_quadrature_max_abs_error"] = qerr
    # 2. linear case matches equation (8)
    for g in (0.3, 1.0):
        x = np.linspace(0, 5, 11)
        exact = 2 * g / (x ** 4 + (g * g - 2) * x ** 2 + 1)
        check(np.max(np.abs(spectrum(1, g, x) - exact)) < 1e-12, "n=1 matches (8)")

    for g in GAMMAS:
        rows = []
        last = 0
        for n in range(1, N_SCAN + 1, 2):
            X, rel = crossing(n, g)
            rows.append({"n": n, "Xi": X, "max_relative_excess": rel})
            if X > 0:
                last = n
        x1 = rows[0]["Xi"]
        check(abs(x1 - math.sqrt(2 - g * g)) < 1e-6, f"Xi_1 = sqrt(2-gamma^2) at gamma={g}")
        # even degrees: S_n(0) is the maximum (r^n >= 0)
        for n in (2, 4, 6, 10):
            w, _, _ = params(g)
            xi = np.linspace(1e-3, n * w + 12, 20001)
            s = spectrum(n, g, xi)
            s0 = spectrum(n, g, np.array([0.0]))[0]
            check(np.all(s < s0), f"even degree {n} below S_n(0) at gamma={g}")
        report["gammas"][str(g)] = {
            "last_odd_degree_with_crossing_up_to_n_scan": last,
            "Xi_max_over_odd_degrees": max(r["Xi"] for r in rows),
            "rows_with_crossing": [r for r in rows if r["Xi"] > 0],
        }
        print(f"gamma={g}: last crossing degree {last}; max Xi {report['gammas'][str(g)]['Xi_max_over_odd_degrees']:.4f}")

    report["environment"] = {"python": platform.python_version(), "numpy": np.__version__,
                             "scipy": __import__("scipy").__version__}
    args.output.write_text(json.dumps(report, indent=2))
    print("All checks passed; finite computations do not replace the analytic proof.")
    print("Results:", args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
