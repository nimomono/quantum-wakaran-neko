#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    kbt = 1.0

    q = np.full(64, 1.0 / 64.0)
    k = np.linspace(0.7, 1.4, q.size)
    dlogw = 0.83
    second_moment = kbt / k
    mean_force = dlogw * float(np.sum(q * k * second_moment))
    assert abs(mean_force - kbt * dlogw) < 1e-14

    force_variance = (
        2.0 * kbt**2 * dlogw**2 * float(np.dot(q, q))
    )
    expected = 2.0 * kbt**2 * dlogw**2 / q.size
    assert abs(force_variance - expected) < 1e-14

    dt = 2.0e-4
    total = 1.5
    times = np.arange(0.0, total + 0.5 * dt, dt)

    def tracking_error(gamma_rho: float) -> float:
        var = kbt
        worst = 0.0
        for t in times[1:]:
            kval = 1.0 + 0.18 * math.sin(0.7 * t)
            target = kbt / kval
            var += dt * (
                -2.0 * kval / gamma_rho * var
                + 2.0 * kbt / gamma_rho
            )
            worst = max(worst, abs(var - target))
        return worst

    slow = tracking_error(0.20)
    medium = tracking_error(0.10)
    fast = tracking_error(0.05)
    assert fast < medium < slow

    mass = 0.03
    gamma = 1.7
    eps_m = mass / gamma
    velocity = -0.61
    force = 0.44
    dx_drift = velocity
    dv_drift = (force - gamma * velocity) / mass
    dy_drift = dx_drift + eps_m * dv_drift
    assert abs(dy_drift - force / gamma) < 1e-14

    tau_ratio = 2.0e-4
    n_rho = 40000
    nu = 1.0
    b_star = 2.0
    eps_mass = 1.0e-8
    eps_fh = 1.0e-5
    eps_init = 1.0e-5
    eps_pv = tau_ratio + 1.0 / math.sqrt(n_rho)
    eps_od = eps_mass * b_star + math.sqrt(nu * eps_mass)
    eps_x = eps_fh + eps_init + eps_pv + eps_od
    assert eps_x < 5.4e-3

    print(
        "r211b_q1_open_reduction_ok",
        slow,
        medium,
        fast,
        eps_x,
    )


if __name__ == "__main__":
    main()
