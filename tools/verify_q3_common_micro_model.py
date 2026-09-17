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
    M2, Hs, Ss = 1.7, 2.2, 1.8
    Ns = np.array([50.0, 100.0, 200.0, 400.0])
    delta = M2 * (Hs**2 + Ss**2) / (2 * Ns)
    assert np.allclose(delta[:-1] / delta[1:], 2.0)
    tv = 0.5 * (np.exp(2 * delta) - 1)
    assert np.all(np.diff(tv) < 0)
    S, u = 1.7, 0.31
    jac = abs(np.linalg.det(np.array([[u, S], [1-u, -S]], dtype=float)))
    assert math.isclose(jac, S, rel_tol=1e-12)


def check_r198c() -> None:
    K, m, lam, beta = 1.2, 0.8, 0.05, 3.0
    phases = np.linspace(0.0, 2*np.pi, 20000, endpoint=False)
    Y = 2 * math.sqrt(K*m) * np.cos(phases)
    assert abs(float(np.mean(Y))) < 1e-12
    assert math.isclose(float(np.mean(Y**2)), 2*K*m, rel_tol=1e-10)
    shift = beta * lam**2 * m
    mu_bare, omega = 2.4 - shift, 2.4
    assert math.isclose(mu_bare + shift, omega, rel_tol=1e-12)


def check_r198d_window() -> None:
    eps = 1e-2
    g = 1.0
    Adot = 1e-7
    lower = Adot / (g * eps)
    upper = math.sqrt(eps)
    assert lower < upper
    lam2 = math.sqrt(lower * upper)
    assert Adot / (g * lam2) < eps
    assert lam2**2 < eps


def check_r199a_dispersion() -> None:
    J, a, Omega = 0.7, 0.05, 2.0
    assert Omega > 2 * abs(J)
    k = np.array([-1e-4, 0.0, 1e-4])
    wp = Omega + 2 * J * np.sin(k)
    wm = Omega - 2 * J * np.sin(k)
    vg_p = (wp[2] - wp[0]) / (k[2] - k[0]) * a
    vg_m = (wm[2] - wm[0]) / (k[2] - k[0]) * a
    c = 2 * J * a
    assert math.isclose(vg_p, c, rel_tol=1e-8)
    assert math.isclose(vg_m, -c, rel_tol=1e-8)


def check_r199a_window() -> None:
    dk = 0.01
    T = 20.0
    eps_int = 2e-3
    eps_nl = 2e-5
    eps_port = 5e-3
    N = 400.0
    Istar = 1.0
    lead_error = dk**2 * T + eps_int + eps_nl * T + eps_port**2 * T
    core_drive = eps_port**2 * T * Istar / N
    assert lead_error < 1e-2
    assert core_drive < 1e-4
    tau_R, tau_therm, tau_A, tau_p, T_sig = 0.2, 2.0, 50.0, 0.1, 20.0
    assert tau_R < tau_therm < tau_A
    assert tau_p < T_sig


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
    check_r199a_dispersion()
    check_r199a_window()
    check_mean_force()
    print("q3_common_micro_model_m60_required_ok")


if __name__ == "__main__":
    main()
