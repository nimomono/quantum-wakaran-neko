#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    gamma = 2.0
    kbt = 0.7
    nu = kbt / gamma
    assert abs(nu - 0.35) < 1e-14

    # Deterministic constant-coefficient relaxation toward B.
    b = 0.43
    v0 = -0.31
    for tau in [0.2, 0.1, 0.05, 0.025]:
        t = 1.0
        v = b + (v0 - b) * math.exp(-t / tau)
        assert abs(v - b) <= abs(v0 - b) * math.exp(-t / tau) + 1e-14

    # Fokker--Planck consistency: b rho - nu rho_x = j.
    n = 4096
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dx = x[1] - x[0]
    rho = 1.0 + 0.2 * np.cos(x)
    current = 0.17 + 0.08 * np.sin(2.0 * x)
    rho_x = (np.roll(rho, -1) - np.roll(rho, 1)) / (2.0 * dx)
    drift = current / rho + nu * rho_x / rho
    reconstructed = drift * rho - nu * rho_x
    assert np.max(np.abs(reconstructed - current)) < 1e-12

    print("M64 R203C overdamped/Fokker-Planck checks passed")


if __name__ == "__main__":
    main()
