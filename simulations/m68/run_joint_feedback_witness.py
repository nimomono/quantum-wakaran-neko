#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    t = 1.5
    capacities = np.array([8.0, 16.0, 32.0, 64.0, 128.0, 256.0])
    eps = 1.0 / capacities
    equivariance_defect = 2.0 * eps * (1.0 - np.exp(-t))
    medium_bias = 2.0 * eps**2 * (t - 1.0 + np.exp(-t))

    slope_eq = float(np.polyfit(np.log(capacities), np.log(equivariance_defect), 1)[0])
    slope_bias = float(np.polyfit(np.log(capacities), np.log(medium_bias), 1)[0])
    assert -1.01 < slope_eq < -0.99
    assert -2.01 < slope_bias < -1.99

    print("C equivariance_defect mean_medium_bias")
    for c, e, b in zip(capacities, equivariance_defect, medium_bias):
        print(f"{int(c):4d} {e:.8e} {b:.8e}")
    print(f"slopes equivariance={slope_eq:.6f} mean_bias={slope_bias:.6f}")


if __name__ == "__main__":
    main()
