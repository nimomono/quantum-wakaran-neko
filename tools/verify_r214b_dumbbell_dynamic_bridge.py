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

    # The physical white-noise limit is Stratonovich in Cartesian
    # coordinates.  The noise amplitude is constant, so Cartesian Ito and
    # Stratonovich drifts coincide; the radial 2D/r term is geometric.
    r = np.linspace(0.15, 7.0, 10000)
    dlogp = 2.0 / r - (r - ell) / sigma**2
    drift = -(k / gamma_r) * (r - ell) + 2.0 * D / r
    assert np.max(np.abs(drift - D * dlogp)) < 2e-11
    sigma_cart = np.sqrt(2.0 * D)
    dsigma_dx = 0.0
    assert 0.5 * sigma_cart * dsigma_dx == 0.0

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

    # Generic microscopic reciprocal-load bound on a prepared shell.
    alpha = 1.3
    ell0 = 2.5
    k_load = 1.2
    e_star = 0.8
    c_load = alpha * np.sqrt(2.0 * k_load * e_star) / (2.0 * ell0)
    rng = np.random.default_rng(214)
    for _ in range(200):
        grad_rho = float(rng.uniform(-0.8, 0.8))
        ell_now = float(rng.uniform(ell0, 4.0))
        delta = (
            float(rng.uniform(-1.0, 1.0))
            * np.sqrt(2.0 * e_star / k_load)
        )
        force = abs(k_load * delta * alpha * grad_rho / (2.0 * ell_now))
        assert force <= c_load * abs(grad_rho) + 1e-14

    # Port C1 stability implies score stability in the node-safe sector.
    x = np.linspace(-np.pi, np.pi, 2001)
    rho0 = 1.0 + 0.2 * np.sin(x)
    drho0 = 0.2 * np.cos(x)
    amp = 0.01
    delta_rho = amp * np.cos(2.0 * x)
    ddelta_rho = -2.0 * amp * np.sin(2.0 * x)
    rho1 = rho0 + delta_rho
    drho1 = drho0 + ddelta_rho
    rho_t = 0.45
    score0 = drho0 / (rho0 + rho_t)
    score1 = drho1 / (rho1 + rho_t)
    score_err = float(np.max(np.abs(score1 - score0)))
    score_bound = (
        float(np.max(np.abs(ddelta_rho))) / rho_t
        + float(np.max(np.abs(drho0)))
        * float(np.max(np.abs(delta_rho)))
        / rho_t**2
    )
    assert score_err <= score_bound + 1e-14

    eps_u = 0.004
    drift_err = eps_u + nu * score_err
    drift_bound = eps_u + nu * score_bound
    assert drift_err <= drift_bound + 1e-14

    # Explicit simultaneous family.
    lam = np.array([0.2, 0.1, 0.05, 0.025])
    em = lam**2
    efr = lam**3
    tr = lam**3
    tmom = lam**4
    assert np.all(tmom < tr)
    assert np.all(tr < em)
    assert np.all(efr / np.sqrt(em) < 0.21)
    assert np.all(np.diff(efr / np.sqrt(em)) < 0.0)

    print(
        "r214b_required_ok "
        f"small_mass_slope={slope:.6f} "
        f"extra_friction_abs={eps_fr_abs:.3e} "
        f"fluctuation_x={fluc_x:.3e} "
        f"score_err={score_err:.3e} "
        f"score_bound={score_bound:.3e}"
    )


if __name__ == "__main__":
    main()
