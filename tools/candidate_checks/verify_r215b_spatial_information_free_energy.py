#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def trap_periodic(f: np.ndarray, length: float) -> float:
    return float(np.mean(f) * length)


def main() -> None:
    length = 2.0 * math.pi
    n = 120000
    x = np.linspace(0.0, length, n, endpoint=False)

    amp = 0.31
    nu = 0.73
    gamma_x = 1.4
    mass_x = 0.18
    kbt = nu * gamma_x
    tau_v = mass_x / gamma_x
    j_si = 2.0 * mass_x * nu

    pi = (1.0 + amp * np.cos(x)) / length
    dpi = -amp * np.sin(x) / length
    score = dpi / pi
    u = nu * score

    fisher = trap_periodic(pi * score**2, length)
    f_si = 0.5 * mass_x * trap_periodic(pi * u**2, length)
    assert abs(f_si - 0.5 * mass_x * nu**2 * fisher) < 2e-12
    assert abs(f_si - (j_si**2 / (8.0 * mass_x)) * fisher) < 2e-12
    assert abs(j_si - 2.0 * kbt * tau_v) < 2e-15

    # Projective invariance w -> c w.
    z = 3.7
    w = z * pi
    dw = z * dpi
    fisher_w = trap_periodic((dw**2) / w, length) / z
    assert abs(fisher_w - fisher) < 2e-12

    # de Bruijn identity for the exactly heat-evolved cosine family:
    # amp(s)=amp exp(-nu s).
    def kl_uniform(s: float) -> float:
        a = amp * math.exp(-nu * s)
        p = (1.0 + a * np.cos(x)) / length
        return trap_periodic(p * np.log(p * length), length)

    h = 2e-6
    dkl = (kl_uniform(h) - kl_uniform(-h)) / (2.0 * h)
    assert abs(dkl + nu * fisher) < 2e-8
    assert abs(f_si + 0.5 * tau_v * kbt * dkl) < 2e-8

    # Path-KL rate identity (Girsanov coefficient).
    path_kl_rate = trap_periodic(pi * u**2, length) / (4.0 * nu)
    assert abs(f_si - j_si * path_kl_rate) < 2e-12

    # Translation KL curvature.
    def kl_shift(eps: float) -> float:
        p_shift = (1.0 + amp * np.cos(x - eps)) / length
        return trap_periodic(pi * np.log(pi / p_shift), length)

    eps = 2e-4
    curvature = (kl_shift(eps) + kl_shift(-eps)) / (eps * eps)
    assert abs(curvature - fisher) < 3e-7

    # Node-safe uniform regularization lowers Fisher information.
    delta = 0.2
    q0 = np.full_like(x, 1.0 / length)
    pi_delta = (pi + delta * q0) / (1.0 + delta)
    dpi_delta = dpi / (1.0 + delta)
    fisher_delta = trap_periodic(dpi_delta**2 / pi_delta, length)
    rhs_delta = (
        1.0
        / (1.0 + delta)
        * trap_periodic(dpi**2 / (pi + delta / length), length)
    )
    assert abs(fisher_delta - rhs_delta) < 2e-12
    assert fisher_delta <= fisher + 1e-14

    # Functional derivative check in a zero-mean direction.
    eta = np.cos(2.0 * x) / length
    deta = -2.0 * np.sin(2.0 * x) / length
    assert abs(trap_periodic(eta, length)) < 1e-14
    eps_fd = 2e-6

    def energy(p: np.ndarray, dp: np.ndarray) -> float:
        return 0.5 * mass_x * nu**2 * trap_periodic(dp**2 / p, length)

    e_plus = energy(pi + eps_fd * eta, dpi + eps_fd * deta)
    e_minus = energy(pi - eps_fd * eta, dpi - eps_fd * deta)
    fd = (e_plus - e_minus) / (2.0 * eps_fd)

    sqrt_pi = np.sqrt(pi)
    # periodic second derivative is analytic for checking via spectral-like centered FD
    dx = length / n
    lap_sqrt = (
        np.roll(sqrt_pi, -1) - 2.0 * sqrt_pi + np.roll(sqrt_pi, 1)
    ) / dx**2
    mu_si = -2.0 * mass_x * nu**2 * lap_sqrt / sqrt_pi
    pred = trap_periodic(mu_si * eta, length)
    assert abs(fd - pred) < 2e-6

    print(
        "r215b_candidate_ok "
        f"fisher={fisher:.6e} "
        f"F_SI={f_si:.6e} "
        f"path_kl_rate={path_kl_rate:.6e}"
    )


if __name__ == "__main__":
    main()
