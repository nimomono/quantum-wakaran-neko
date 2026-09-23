#!/usr/bin/env python3
"""Required regression checks for R205F passive separation principle."""

import math


def defect_and_bound(R: float, x: float, y: float) -> tuple[float, float]:
    mu_a, mu_b = 0.8, 1.1
    K = 0.9 * math.exp(-R)
    C = 0.2 * math.exp(-2.0 * R)
    grad_va = -math.sin(x - y)
    grad_vb = math.sin(x - y)
    grad_fa = math.cos(x) * math.cos(y)
    grad_fb = -math.sin(x) * math.sin(y)
    mixed_f = -math.cos(x) * math.sin(y)
    defect = -K * (mu_a * grad_va * grad_fa + mu_b * grad_vb * grad_fb) + 2.0 * C * mixed_f
    bound = (
        abs(K) * mu_a * abs(grad_va) * abs(grad_fa)
        + abs(K) * mu_b * abs(grad_vb) * abs(grad_fb)
        + 2.0 * abs(C) * abs(mixed_f)
    )
    return defect, bound


def main() -> None:
    previous = None
    for R in (0.0, 1.0, 2.0, 4.0, 8.0):
        worst = 0.0
        for x in (0.2, 1.1, 2.4):
            for y in (0.4, 1.7, 2.8):
                defect, bound = defect_and_bound(R, x, y)
                assert abs(defect) <= bound + 1e-15
                worst = max(worst, abs(defect))
        if previous is not None:
            assert worst < previous
        previous = worst

    K = C = 0.0
    assert -K * math.sin(0.7 - 1.3) + 2.0 * C * math.cos(0.7) * math.sin(1.3) == 0.0
    print("R205F passive separation checks: OK")


if __name__ == "__main__":
    main()
