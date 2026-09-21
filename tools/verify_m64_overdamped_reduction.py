#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    n = 2048
    length = 2.0 * np.pi
    x = np.arange(n) * length / n
    dx = length / n
    nu = 0.7
    delta = 0.06

    rho = 1.0 + 0.22 * np.cos(x)
    rho /= rho.mean()
    q0 = np.ones_like(x)
    j = 0.28 * rho * np.sin(2.0 * x)

    rho_delta = (rho + delta * q0) / (1.0 + delta)
    j_delta = j / (1.0 + delta)
    v_delta = j_delta / rho_delta

    rho_x = (np.roll(rho_delta, -1) - np.roll(rho_delta, 1)) / (2.0 * dx)
    u_delta = nu * rho_x / rho_delta
    b_delta = v_delta + u_delta

    # The ideal regularized diffusion must reproduce the regularized current:
    # b rho_delta - nu d_x rho_delta = j_delta.
    fp_flux = b_delta * rho_delta - nu * rho_x
    assert np.max(np.abs(fp_flux - j_delta)) < 2e-12

    # The regularization keeps the density strictly positive.
    assert np.min(rho_delta) > 0.0

    print("M64 canonical overdamped regularized diffusion check passed")


if __name__ == "__main__":
    main()
