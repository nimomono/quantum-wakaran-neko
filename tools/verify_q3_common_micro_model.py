#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def check_r198a() -> None:
    m1, m2 = 1.3, 0.9
    w1, w2 = 2.0, 2.7
    kappa = 0.4
    alpha1 = (4.0 / 3.0) * kappa * m1**2 * w1**2
    alpha2 = (4.0 / 3.0) * kappa * m2**2 * w2**2
    beta = 2.0 * kappa * m1 * m2 * w1 * w2
    g1, g2 = kappa * m1 * w1, kappa * m2 * w2
    c1 = 3 * alpha1 / (8 * m1**2 * w1**2)
    c2 = 3 * alpha2 / (8 * m2**2 * w2**2)
    c12 = beta / (2 * m1 * m2 * w1 * w2)
    d1, d2 = g1 / (m1 * w1), g2 / (m2 * w2)
    assert np.allclose([c1, c2, c12, d1, d2], [kappa / 2, kappa / 2, kappa, kappa, kappa])
    k1, k2, A = 0.7, 1.1, 1.2
    avg = c1*k1*k1 + c2*k2*k2 + c12*k1*k2 - A*(d1*k1+d2*k2) + 0.5*kappa*A*A
    target = 0.5*kappa*(k1+k2-A)**2
    assert math.isclose(avg, target, rel_tol=1e-12, abs_tol=1e-12)


def check_r198b() -> None:
    # Hessian remainder bound and the 1/N law.
    M2, Hs, Ss = 1.7, 2.2, 1.8
    Ns = np.array([50.0, 100.0, 200.0, 400.0])
    delta = M2 * (Hs**2 + Ss**2) / (2 * Ns)
    assert np.allclose(delta[:-1] / delta[1:], 2.0)
    tv = 0.5 * (np.exp(2 * delta) - 1)
    assert np.all(np.diff(tv) < 0)
    # Target Liouville Jacobian gives the S factor.
    S, u = 1.7, 0.31
    J = abs(np.linalg.det(np.array([[u, S], [1-u, -S]], dtype=float)))
    assert math.isclose(J, S, rel_tol=1e-12)


def check_r198c() -> None:
    # Phase averaging removes odd exchange terms and leaves <Y^2>=2 K m.
    K, m, lam, beta = 1.2, 0.8, 0.05, 3.0
    phases = np.linspace(0.0, 2*np.pi, 20000, endpoint=False)
    Y = 2 * math.sqrt(K*m) * np.cos(phases)
    assert abs(float(np.mean(Y))) < 1e-12
    assert math.isclose(float(np.mean(Y**2)), 2*K*m, rel_tol=1e-10)
    shift = beta * lam**2 * m
    mu_bare, omega = 2.4 - shift, 2.4
    assert math.isclose(mu_bare + shift, omega, rel_tol=1e-12)


def check_r198d_window() -> None:
    # A nonempty weak-exchange window exists for sufficiently slow A.
    eps = 1e-2
    g = 1.0
    Adot = 1e-7
    lower = Adot / (g * eps)
    upper = math.sqrt(eps)
    assert lower < upper
    lam2 = math.sqrt(lower * upper)
    lam = math.sqrt(lam2)
    assert Adot / (g * lam**2) < eps
    assert lam**4 < eps


def check_mean_force() -> None:
    beta, kappa, A = 4.0, 3.0, 1.1
    x = math.sqrt(beta*kappa/2.0) * A
    Delta = math.exp(-x*x) / (math.exp(-x*x) + math.sqrt(math.pi)*x*(1+math.erf(x)))
    mean = (1/beta)/A * (1-Delta)
    assert 0 < mean < (1/beta)/A


def main() -> None:
    check_r198a()
    check_r198b()
    check_r198c()
    check_r198d_window()
    check_mean_force()
    print("q3_common_micro_model_m59_ok")


if __name__ == "__main__":
    main()
