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

    r = np.linspace(0.15, 7.0, 10000)
    dlogp = 2.0 / r - (r - ell) / sigma**2
    drift = -(k / gamma_r) * (r - ell) + 2.0 * D / r
    assert np.max(np.abs(drift - D * dlogp)) < 2e-11

    drift_prime = -(k / gamma_r) - 2.0 * D / r**2
    assert np.all(drift_prime <= -1.0 / tau_r)

    tau_mem = 1e-7
    tau_mom = 1e-6
    tau_slow = 1.0
    t_rec = 100.0
    assert tau_mem < tau_mom < tau_r < tau_slow < t_rec
    tracking_ratio = tau_r / tau_slow
    assert tracking_ratio <= 1e-3 + 1e-15

    c_mix = 1.5
    grad_ell = 0.1
    gamma_x = 1.0
    eps_fr = c_mix * gamma_r * grad_ell**2 / gamma_x
    assert eps_fr < 2e-5

    n0 = np.array([64.0, 128.0, 256.0, 512.0, 1024.0])
    relative_load = 0.2 / n0
    ratios = relative_load[:-1] / relative_load[1:]
    assert np.allclose(ratios, 2.0, rtol=0.0, atol=1e-14)

    print(
        "r214b_ok "
        f"tau_r={tau_r:.3e} "
        f"tracking_ratio={tracking_ratio:.3e} "
        f"extra_friction_ratio={eps_fr:.3e} "
        "relative_load_scaling=N0^-1"
    )


if __name__ == "__main__":
    main()
