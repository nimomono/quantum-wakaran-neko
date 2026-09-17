#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def langevin(x: float) -> float:
    if abs(x) < 1e-6:
        return x/3 - x**3/45 + 2*x**5/945
    return 1 / math.tanh(x) - 1 / x


def check_chiral_response_parity() -> None:
    rs = np.array([-0.08, -0.04, 0.04, 0.08])
    response = np.array([langevin(3*r) for r in rs])

    assert np.allclose(response[:2], -response[:1:-1], atol=1e-12)
    for r, value in zip(rs, response):
        assert abs(value - r) <= 0.7 * abs(r)**3

    radial_factor = np.sinh(3*rs) / (3*rs)
    assert np.allclose(radial_factor[:2], radial_factor[:1:-1], atol=1e-12)
    relative_change = radial_factor - 1.0
    assert np.all(relative_change >= 0)
    assert np.max(relative_change / (rs**2)) < 1.7


def main() -> None:
    check_chiral_response_parity()
    print("candidate_chiral_shell_response_ok")


if __name__ == "__main__":
    main()
