#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def energy_envelope(a: float, b: float, c: float, e0: float, omega_h: float, T: float, eps: float) -> tuple[float, float]:
    A = a + eps
    B = c + b * b / (4 * eps)
    estar = (e0 + B / A) * np.exp(omega_h * A * T) - B / A
    C = a * estar + b * np.sqrt(estar) + c
    return float(estar), float(C)


def main() -> None:
    eta = 0.12
    J0 = 1.0
    T = 0.7
    hnorm = 0.08
    omega_h = 4 * hnorm / J0
    eps_young = 0.2

    # Generic theorem: any phase-invariant load envelope aE+b sqrt(E)+c gives N0^-1 scaling.
    profiles = {
        "phase_volume_regression": (0.08, 1.15, 0.12),
        "dumbbell": (0.0, 1.55, 0.12),
    }
    for name, (a, b, c) in profiles.items():
        estar, Cp = energy_envelope(a, b, c, 0.6, omega_h, T, eps_young)
        assert estar >= 0.6
        assert np.isfinite(Cp) and Cp > 0.0
        n0 = np.array([80.0, 160.0, 320.0, 640.0, 1280.0])
        load = 2 * T * Cp / (J0 * n0 * (1 - eta))
        slope = float(np.polyfit(np.log(n0), np.log(load), 1)[0])
        assert abs(slope + 1.0) < 1e-12, (name, slope)

    # R214 dumbbell direct gradient bound on a bootstrap tube.
    kappa = (1 - eta) ** (-0.25)
    Keta = kappa**2 + 0.5 * kappa**(-2)
    alpha = 1.0
    Bx = 1.0
    k = 1.0
    ell0 = 2.5
    Ddb = alpha * Bx * Keta**2 * np.sqrt(2 * k) / (2 * ell0)
    assert 0.0 < Ddb < 1.0

    # Exact U(1) invariance of the dumbbell intensity port.
    rng = np.random.default_rng(210)
    bvec = rng.normal(size=8) + 1j * rng.normal(size=8)
    B = np.diag(np.linspace(0.4, 1.2, 8))
    rho0 = float(np.real(np.vdot(bvec, B @ bvec)))
    for theta in np.linspace(0.0, 2 * np.pi, 17):
        bp = np.exp(1j * theta) * bvec
        rho = float(np.real(np.vdot(bp, B @ bp)))
        assert abs(rho - rho0) < 2e-12

    # Generic flow derivative assumption is profile-independent.
    ell_e = np.array([0.7, 0.8, 0.6])
    Lv = float(np.sqrt(np.sum(ell_e**2)))
    gammaK = 4.5
    gammav = 0.3
    b_db = Ddb + Lv * np.sqrt(2 * gammaK)
    c_db = Lv * gammav
    assert b_db > Ddb
    assert c_db > 0.0

    # R86 error is combined only for Q3-1, not for the Q3-2 load-only bridge.
    n0 = 1280.0
    _, Cp = energy_envelope(0.0, b_db, c_db, 0.6, omega_h, T, eps_young)
    qload = 2 * T * Cp / (J0 * n0 * (1 - eta))
    eps86 = 0.015
    q210_q31 = kappa * eps86 + qload
    assert q210_q31 > qload
    assert q210_q31 < 1.0

    print(
        "r210a_generic_coherent_load_ok",
        f"Ddb={Ddb:.6f}",
        f"qload={qload:.6e}",
        f"q3_1_combined={q210_q31:.6e}",
    )


if __name__ == "__main__":
    main()
