#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    t = 1.2
    capacities = np.array([8.0, 16.0, 32.0, 64.0, 128.0, 256.0])
    eps = 1.0 / capacities

    equivariance_defect = 2.0 * eps * (1.0 - np.exp(-t))
    mean_medium_bias = 2.0 * eps**2 * (t - 1.0 + np.exp(-t))
    slope_eq = float(np.polyfit(np.log(capacities), np.log(equivariance_defect), 1)[0])
    slope_bias = float(np.polyfit(np.log(capacities), np.log(mean_medium_bias), 1)[0])
    assert -1.01 < slope_eq < -0.99, slope_eq
    assert -2.01 < slope_bias < -1.99, slope_bias

    eps214 = 2.5e-2
    lam = 1.7
    b = 0.31
    total = (eps214 + b / capacities) * np.exp(lam / capacities)
    adapt = total - eps214
    slope_adapt = float(np.polyfit(np.log(capacities[-4:]), np.log(adapt[-4:]), 1)[0])
    assert -1.08 < slope_adapt < -0.92, slope_adapt
    assert np.all(total > eps214)
    assert total[-1] < total[0]

    print(
        "r216d_feedback_ok "
        f"equivariance_slope={slope_eq:.6f} "
        f"mean_bias_slope={slope_bias:.6f} "
        f"adapt_slope={slope_adapt:.6f}"
    )


if __name__ == "__main__":
    main()
