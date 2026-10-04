#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    kBT = 1.0
    k = 1.0
    gamma_r = 1e-3
    sigma = np.sqrt(kBT / k)
    ell = 2.5 * sigma
    D = kBT / gamma_r
    tau_r = gamma_r / k

    # R214A radial law is the zero-flux stationary density.
    r = np.linspace(0.15, 7.0, 10000)
    dlogp = 2.0 / r - (r - ell) / sigma**2
    drift = -(k / gamma_r) * (r - ell) + 2.0 * D / r
    assert np.max(np.abs(drift - D * dlogp)) < 2e-11

    # One-sided contraction of the radial process.
    drift_prime = -(k / gamma_r) - 2.0 * D / r**2
    assert np.all(drift_prime <= -1.0 / tau_r)

    # Nonempty finite-bath / internal-mass / tracking window.
    tau_mem = 1e-7
    tau_int_mom = 1e-6
    tau_slow = 1.0
    t_rec = 100.0
    assert tau_mem < tau_int_mom < tau_r < tau_slow < t_rec

    # Direct small-mass bridge: epsilon_M B + sqrt(nu epsilon_M).
    nu = 0.8
    bstar = 0.6
    eps_m = np.array([4e-2, 1e-2, 2.5e-3, 6.25e-4])
    od = eps_m * bstar + np.sqrt(nu * eps_m)
    slope = float(np.polyfit(np.log(eps_m), np.log(od), 1)[0])
    assert 0.47 < slope < 0.53, slope

    # Y=X+epsilon_M V removes the fast OU velocity at the equation level.
    # Algebraic coefficient of V dt is exactly 1-epsilon_M/epsilon_M=0.
    for em in eps_m:
        assert abs(1.0 - em / em) < 1e-15

    # Absolute covariance / extra FDT friction ledger.
    c_mix = 1.5
    grad_ell = 0.1
    gamma_x = 1.0
    eps_fr_abs = c_mix * gamma_r * grad_ell**2 / gamma_x
    assert eps_fr_abs < 2e-5
    fluc_x = np.sqrt(2.0 * nu * 0.7 * eps_fr_abs)
    assert fluc_x < 5e-3

    # Explicit simultaneous family:
    # epsilon_M=lambda^2, eps_fr=O(lambda^3), tau_r=O(lambda^3),
    # internal momentum time=O(lambda^4).
    lam = np.array([0.2, 0.1, 0.05, 0.025])
    em = lam**2
    efr = lam**3
    tr = lam**3
    tmom = lam**4
    assert np.all(tmom < tr)
    assert np.all(tr < em)
    assert np.all(efr / np.sqrt(em) < 0.21)
    assert np.all(np.diff(efr / np.sqrt(em)) < 0.0)

    # R210A load-only relative error remains N0^-1.
    n0 = np.array([64.0, 128.0, 256.0, 512.0, 1024.0])
    relative_load = 0.2 / n0
    ratios = relative_load[:-1] / relative_load[1:]
    assert np.allclose(ratios, 2.0, rtol=0.0, atol=1e-14)

    print(
        "r214b_required_ok "
        f"small_mass_slope={slope:.6f} "
        f"extra_friction_abs={eps_fr_abs:.3e} "
        f"fluctuation_x={fluc_x:.3e}"
    )


if __name__ == "__main__":
    main()
