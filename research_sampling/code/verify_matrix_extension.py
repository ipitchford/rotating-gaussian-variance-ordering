#!/usr/bin/env python3
"""Deterministic checks for the matrix extension and mismatch certificate.

The finite checks test transfer-function, Lyapunov and tensor-convolution
calculations against one another. They do not establish the all-L2 theorem.
Run from any directory; the JSON is written beside this script by default.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.integrate import quad_vec
from scipy.linalg import block_diag, solve_continuous_lyapunov


J2 = np.array([[0.0, -1.0], [1.0, 0.0]])



def require(condition, description: str) -> None:
    """Explicit check that also runs under `python -O` (unlike assert)."""
    if not condition:
        raise RuntimeError("verification check failed: " + description)

def spectrum(k, friction, xi):
    inverse_friction = np.linalg.inv(friction)
    middle = friction - k @ inverse_friction - inverse_friction @ k
    pencil = k @ inverse_friction @ k + xi**2 * middle + xi**4 * inverse_friction
    return 2.0 * np.linalg.inv(pencil)


def transfer_spectrum(k, friction, xi):
    transfer = np.linalg.inv(k - xi**2 * np.eye(len(k)) + 1j * xi * friction)
    return transfer @ (2.0 * friction) @ transfer.conj().T


def drift(k, friction, j, mu):
    dimension = len(k)
    return np.block([[mu * j, -np.eye(dimension)], [k, friction + mu * j]])


def linear_variance(k, friction, j, mu, observable):
    covariance = block_diag(np.linalg.inv(k), np.eye(len(k)))
    linear = np.r_[observable, np.zeros(len(k))]
    return float(2.0 * linear @ np.linalg.solve(drift(k, friction, j, mu), covariance @ linear))


def quadratic_variance(k, friction, j, mu, observable):
    covariance = block_diag(np.linalg.inv(k), np.eye(len(k)))
    extended = block_diag(observable, np.zeros_like(k))
    poisson = solve_continuous_lyapunov(drift(k, friction, j, mu).T, extended)
    return float(4.0 * np.trace(extended @ covariance @ poisson @ covariance))


def checks():
    k0 = np.diag([1.0, 4.0])
    friction0 = np.array([[4.0, 1.0], [1.0, 4.0]])
    k, friction = np.kron(k0, np.eye(2)), np.kron(friction0, np.eye(2))
    j = np.kron(np.eye(2), J2)
    certificate = friction @ friction @ friction - friction @ k - k @ friction
    expected_certificate = np.kron(np.array([[68.0, 44.0], [44.0, 44.0]]), np.eye(2))
    require(np.array_equal(certificate, expected_certificate), 'np.array_equal(certificate, expected_certificate)')
    require(np.linalg.eigvalsh(certificate).min() > 0, 'np.linalg.eigvalsh(certificate).min() > 0')
    require(np.linalg.norm(k @ friction - friction @ k) > 0, 'np.linalg.norm(k @ friction - friction @ k) > 0')
    require(np.allclose(j @ k, k @ j), 'np.allclose(j @ k, k @ j)')
    require(np.allclose(j @ friction, friction @ j), 'np.allclose(j @ friction, friction @ j)')

    frequencies = [0.0, 0.05, 0.25, 0.7, 1.0, 2.0, 5.0, 12.0]
    transfer_error = max(np.max(np.abs(spectrum(k, friction, x) - transfer_spectrum(k, friction, x)))
                         for x in frequencies)
    loewner_minima = [float(np.linalg.eigvalsh(spectrum(k, friction, a) - spectrum(k, friction, b)).min())
                     for a, b in zip(frequencies[:-1], frequencies[1:])]
    require(min(loewner_minima) > 0, 'min(loewner_minima) > 0')
    linear = np.array([1.0, -0.4, 0.7, 0.3])
    linear_error = max(abs(linear_variance(k, friction, j, x, linear)
                           - linear @ spectrum(k, friction, x) @ linear)
                       for x in frequencies)

    # A pure angular-frequency-two quadratic in whitened coordinates.
    sqrt_k = np.diag(np.sqrt(np.diag(k)))
    seed = np.array([[1.0, 0.2, 0.4, 0.1], [0.2, -0.5, 0.3, 0.0],
                     [0.4, 0.3, 0.6, 0.2], [0.1, 0.0, 0.2, -0.2]])
    angular = (seed - j.T @ seed @ j) / 2.0
    angular /= np.sqrt(2.0 * np.trace(angular @ angular))
    observable = sqrt_k @ angular @ sqrt_k
    vector = angular.reshape(-1)

    def white_spectrum(x):
        return sqrt_k @ spectrum(k, friction, x) @ sqrt_k

    convolution_checks = []
    for mu in [0.0, 0.4, 1.3]:
        xi = 2.0 * mu
        integral, quadrature_error = quad_vec(
            lambda y: np.kron(white_spectrum(xi - y), white_spectrum(y)),
            -np.inf, np.inf, epsabs=1e-10, epsrel=1e-10,
        )
        chaos_variance = float(2.0 * vector @ integral @ vector / (2.0 * np.pi))
        poisson_variance = quadratic_variance(k, friction, j, mu, observable)
        convolution_checks.append({"mu": mu, "tensor_convolution": chaos_variance,
                                   "lyapunov": poisson_variance,
                                   "absolute_difference": abs(chaos_variance - poisson_variance),
                                   "quadrature_error_bound": float(quadrature_error)})
    require(max(row["absolute_difference"] for row in convolution_checks) < 1e-9, 'max(row["absolute_difference"] for row in convolution_checks) < 1e-9')

    # A natural squared-matrix threshold is insufficient without commutation.
    bad_k = np.kron(np.array([[0.25, -0.25], [-0.25, 1.75]]), np.eye(2))
    bad_friction = np.kron(np.diag([1.0, 2.0]), np.eye(2))
    squared_difference = bad_friction @ bad_friction - 2.0 * bad_k
    bad_certificate = bad_friction @ bad_friction @ bad_friction - bad_friction @ bad_k - bad_k @ bad_friction
    inverse_bad = np.linalg.inv(bad_friction)
    bad_middle = bad_friction - bad_k @ inverse_bad - inverse_bad @ bad_k
    eigenvalues, eigenvectors = np.linalg.eigh(bad_middle)
    bad_linear = bad_k @ inverse_bad @ bad_k @ eigenvectors[:, 0]
    bad_linear /= np.sqrt(bad_linear @ np.linalg.solve(bad_k, bad_linear))
    bad_v0 = linear_variance(bad_k, bad_friction, j, 0.0, bad_linear)
    bad_vsmall = linear_variance(bad_k, bad_friction, j, 0.001, bad_linear)
    require(np.linalg.eigvalsh(squared_difference).min() >= -1e-14, 'np.linalg.eigvalsh(squared_difference).min() >= -1e-14')
    require(np.linalg.eigvalsh(bad_certificate).min() < 0, 'np.linalg.eigvalsh(bad_certificate).min() < 0')
    require(bad_vsmall > bad_v0, 'bad_vsmall > bad_v0')

    # The least admissible friction, sqrt(2 K), has zero certificate.
    optimal_friction = np.diag(np.sqrt(2.0 * np.diag(k)))
    optimal_residual = np.max(np.abs(optimal_friction @ optimal_friction @ optimal_friction
                                     - optimal_friction @ k - k @ optimal_friction))
    require(optimal_residual < 1e-12, 'optimal_residual < 1e-12')

    mismatch = []
    for precision in [0.9, 1.0, 1.1]:
        for mu in [0.0, 1.0, 10.0, 100.0]:
            gamma = 2.0
            b = np.block([[mu * precision * J2, -np.eye(2)],
                          [precision * np.eye(2), gamma * np.eye(2) + mu * J2]])
            covariance = block_diag(np.eye(2) / precision, np.eye(2))
            extended = block_diag(precision * np.eye(2), np.zeros((2, 2)))
            poisson = solve_continuous_lyapunov(b.T, extended)
            numeric = float(4.0 * np.trace(extended @ covariance @ poisson @ covariance))
            exact_formula = 4.0 / gamma + 4.0 * gamma / precision + 4.0 * mu**2 * (1.0 - precision)**2 / (precision * gamma)
            mismatch.append({"precision": precision, "mu": mu, "lyapunov": numeric,
                             "formula": exact_formula, "absolute_difference": abs(numeric - exact_formula)})
    require(max(row["absolute_difference"] for row in mismatch) < 1e-8, 'max(row["absolute_difference"] for row in mismatch) < 1e-8')
    require(transfer_error < 1e-11 and linear_error < 1e-11, 'transfer_error < 1e-11 and linear_error < 1e-11')

    return {
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "noncommuting_example": {"K_block": k0.tolist(), "friction_block": friction0.tolist(),
                                 "certificate_block": expected_certificate[::2, ::2].tolist(),
                                 "certificate_eigenvalues": np.linalg.eigvalsh(certificate).tolist(),
                                 "commutator_norm": float(np.linalg.norm(k @ friction - friction @ k)),
                                 "transfer_max_abs_error": float(transfer_error),
                                 "linear_max_abs_error": float(linear_error),
                                 "loewner_grid_min_eigenvalues": loewner_minima,
                                 "quadratic_tensor_checks": convolution_checks},
        "insufficient_squared_criterion": {"squared_difference_eigenvalues": np.linalg.eigvalsh(squared_difference).tolist(),
                                           "exact_certificate_eigenvalues": np.linalg.eigvalsh(bad_certificate).tolist(),
                                           "linear_observable": bad_linear.tolist(),
                                           "variance_at_zero": bad_v0, "variance_at_0.001": bad_vsmall,
                                           "increase": bad_vsmall - bad_v0},
        "least_friction_residual": float(optimal_residual),
        "mismatch_checks": mismatch,
        "status": "All deterministic checks passed; finite checks do not replace the analytic proof.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path.cwd() / "matrix_extension_results.json",
                        help="JSON report path (default: matrix_extension_results.json in the current directory)")
    arguments = parser.parse_args()
    results = checks()
    arguments.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(results["status"])
    print(f"Results: {arguments.output}")
