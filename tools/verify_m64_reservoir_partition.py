#!/usr/bin/env python3
from __future__ import annotations

import math


def main() -> None:
    r = 1.37
    r_star = 0.91
    weights = [0.2, 0.3, 0.5]
    lambdas = [(r / r_star) ** (-w) for w in weights]
    jacobian = math.prod(1.0 / value for value in lambdas)
    target = r / r_star
    assert abs(sum(weights) - 1.0) < 1e-14
    assert abs(jacobian - target) < 1e-13

    # Mean-flow and relative-coordinate shifts are translations and have unit Jacobian.
    m = 2.3
    u = -0.41
    pi = 0.73
    p = pi - m * u
    assert abs((p + m * u) - pi) < 1e-14

    lam = lambdas[0]
    zeta = -0.28
    d = 0.17
    rel = 0.62
    q = lam * zeta - d * rel
    assert abs((q + d * rel) / lam - zeta) < 1e-14

    free_energy_difference = -math.log(jacobian)
    target_difference = -math.log(target)
    assert abs(free_energy_difference - target_difference) < 1e-13

    print("M64 R203B reservoir partition checks passed")


if __name__ == "__main__":
    main()
