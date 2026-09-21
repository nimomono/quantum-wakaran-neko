#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def tracking_check() -> None:
    tau = 0.07
    omega = 0.6
    dt = 2.0e-4
    total = 8.0
    times = np.arange(0.0, total + dt, dt)
    q = 0.35 * np.sin(omega * times)
    qdot_bound = 0.35 * omega
    eps_a = 2.0e-3

    u = np.empty_like(times)
    u[0] = q[0] + eps_a
    for n in range(len(times) - 1):
        target = q[n] + eps_a * np.cos(0.7 * times[n])
        u[n + 1] = u[n] + dt * (-u[n] + target) / tau

    bound = eps_a + tau * qdot_bound + 5.0e-4
    assert np.max(np.abs(u - q)) < bound


def preparation_check() -> None:
    n = 400
    length = 2.0 * np.pi
    x = np.arange(n) * length / n
    rho = 1.0 + 0.25 * np.cos(x) + 0.1 * np.sin(2.0 * x)
    rho /= rho.sum()

    nu = 0.5
    dx = length / n
    k_right = nu / dx**2 * np.sqrt(np.roll(rho, -1) / rho)
    k_left = nu / dx**2 * np.sqrt(np.roll(rho, 1) / rho)

    flux_right = rho * k_right
    incoming_from_right = np.roll(rho * k_left, -1)
    assert np.max(np.abs(flux_right - incoming_from_right)) < 1e-12

    free_energy = -np.log(rho)
    gibbs = np.exp(-free_energy)
    gibbs /= gibbs.sum()
    assert np.max(np.abs(gibbs - rho)) < 1e-14


def main() -> None:
    preparation_check()
    tracking_check()
    print("M64 preparation and finite-time tracking checks passed")


if __name__ == "__main__":
    main()
