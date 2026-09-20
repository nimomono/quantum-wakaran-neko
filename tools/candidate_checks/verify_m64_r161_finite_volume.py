#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def errors(n: int, nu: float = 0.7) -> tuple[float, float]:
    length = 2.0 * np.pi
    a = length / n
    x = np.arange(n) * a
    rho = 1.0 + 0.3 * np.cos(x)
    current = 0.4 * rho * np.sin(2.0 * x)

    # Midpoint cell representation on a periodic grid.
    pi = a * rho
    x_edge = x + 0.5 * a
    rho_edge = 1.0 + 0.3 * np.cos(x_edge)
    j_edge = 0.4 * rho_edge * np.sin(2.0 * x_edge)

    traffic = nu * (pi + np.roll(pi, -1)) / a**2
    assert np.min(traffic - np.abs(j_edge)) > 0.0

    k_plus = (traffic + j_edge) / (2.0 * pi)
    traffic_left = np.roll(traffic, 1)
    j_left = np.roll(j_edge, 1)
    k_minus = (traffic_left - j_left) / (2.0 * pi)
    assert np.min(k_plus) >= 0.0
    assert np.min(k_minus) >= 0.0

    # Exact R161 current reconstruction.
    reconstructed = pi * k_plus - np.roll(pi * k_minus, -1)
    assert np.max(np.abs(reconstructed - j_edge)) < 1e-11

    dplus = a * (k_plus - k_minus)
    v = current / rho
    rho_x = -0.3 * np.sin(x)
    u = nu * rho_x / rho
    drift_error = np.max(np.abs(dplus - (v + u)))

    # Generator on a smooth periodic test function.
    f = np.sin(x) + 0.2 * np.cos(2.0 * x)
    la = k_plus * (np.roll(f, -1) - f) + k_minus * (np.roll(f, 1) - f)
    fx = np.cos(x) - 0.4 * np.sin(2.0 * x)
    fxx = -np.sin(x) - 0.8 * np.cos(2.0 * x)
    l_cont = (v + u) * fx + nu * fxx
    gen_error = np.max(np.abs(la - l_cont))
    return drift_error, gen_error


def main() -> None:
    ns = [40, 80, 160, 320]
    values = [errors(n) for n in ns]
    drift = np.array([value[0] for value in values])
    generator = np.array([value[1] for value in values])

    # Second-order convergence: halving a should reduce errors by approximately 4.
    assert np.all(drift[1:] < 0.35 * drift[:-1])
    assert np.all(generator[1:] < 0.35 * generator[:-1])

    print("M64 R203D finite-volume checks passed")
    for n, (ed, eg) in zip(ns, values):
        print(f"N={n:4d} drift_error={ed:.6e} generator_error={eg:.6e}")


if __name__ == "__main__":
    main()
