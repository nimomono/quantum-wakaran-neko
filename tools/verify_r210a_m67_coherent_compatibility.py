#!/usr/bin/env python3
import numpy as np


def main() -> None:
    # Flow-core square completion entering the R210A energy shell.
    K = np.array([4.0, 6.0, 9.0])
    M = np.array([0.8, 1.2, 1.5])
    assert np.all(K > M)
    rng = np.random.default_rng(210)
    for _ in range(200):
        U = rng.normal(size=3)
        v = rng.normal(scale=0.2, size=3)
        PY = rng.normal(size=3)
        lhs = PY**2 / (2 * M) + PY * U + 0.5 * K * (U - v) ** 2
        A = K - M
        c = K * M / (2 * A)
        rhs = (
            (PY + M * U) ** 2 / (2 * M)
            + 0.5 * A * (U - K / A * v) ** 2
            - c * v**2
        )
        assert np.max(np.abs(lhs - rhs)) < 2e-12

    # Phase-volume coefficient is controlled by the positive phase-volume energy.
    n_rho = 32
    wmax = 1.0 / n_rho
    q = rng.normal(size=n_rho)
    omega = np.linspace(0.8, 2.0, n_rho)
    h_rho = 0.5 * np.sum((omega * q) ** 2)
    a_rho = np.sum(wmax * (omega * q) ** 2)
    assert a_rho <= 2 * wmax * h_rho + 1e-14

    # Explicit finite-time excess-energy shell and N0^{-1} load scaling.
    eta = 0.12
    J0 = 1.0
    T = 0.7
    hnorm = 0.08
    c_rho = 1.4
    lv = 0.9
    vstar = np.array([0.25, 0.20, 0.18])
    gamma_k = np.max(K**2 / (K - M))
    gamma_v = np.sqrt(np.sum((K * M / (K - M) * vstar) ** 2))
    aa = 2 * c_rho * wmax
    bb = lv * np.sqrt(2 * gamma_k)
    cc = lv * gamma_v
    omega_h = 4 * hnorm / J0
    young_eps = 0.2
    Aeps = aa + young_eps
    Beps = cc + bb * bb / (4 * young_eps)
    e0 = 0.6
    estar = (e0 + Beps / Aeps) * np.exp(omega_h * Aeps * T) - Beps / Aeps
    assert estar >= e0
    c210 = aa * estar + bb * np.sqrt(estar) + cc
    assert np.isfinite(c210) and c210 > 0

    n0 = np.array([80.0, 160.0, 320.0, 640.0, 1280.0])
    load = 2 * T * c210 / (J0 * n0 * (1 - eta))
    slope = np.polyfit(np.log(n0), np.log(load), 1)[0]
    assert abs(slope + 1.0) < 1e-12

    n0_min = 4 * T * c210 / (J0 * (1 - eta) ** 1.5)
    assert n0[-1] > n0_min

    # Carrier-envelope and load ledgers are separate and combined only for Q3-1.
    kappa = (1 - eta) ** (-0.25)
    eps86 = 0.015
    q210 = kappa * eps86 + load[-1]
    assert q210 > load[-1]
    assert q210 < 1.0
    print("r210a_m67_coherent_compatibility_check_ok", slope, n0_min, q210)


if __name__ == "__main__":
    main()
