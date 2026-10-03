#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def phi(a: float) -> float:
    return math.exp(-0.5 * a * a) / math.sqrt(2.0 * math.pi)


def Phi(a: float) -> float:
    return 0.5 * (1.0 + math.erf(a / math.sqrt(2.0)))


def G(a: float) -> float:
    return Phi(a) + a * phi(a) / (1.0 + a * a)


def eps_force(a: float) -> float:
    return phi(a) / (a * (1.0 + a * a) * G(a))


def exact_I(ell: float, sigma: float) -> float:
    a = ell / sigma
    return sigma * math.sqrt(2.0 * math.pi) * (ell * ell + sigma * sigma) * G(a)


def numerical_I(ell: float, sigma: float) -> float:
    rmax = ell + 10.0 * sigma
    r = np.linspace(0.0, rmax, 250001)
    f = r * r * np.exp(-0.5 * ((r - ell) / sigma) ** 2)
    return float(np.trapz(f, r))


def main() -> None:
    sigma = 1.0
    for a in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
        ell = a * sigma
        num = numerical_I(ell, sigma)
        ana = exact_I(ell, sigma)
        assert abs(num - ana) / ana < 3e-7

    for a in np.linspace(0.2, 5.0, 40):
        h = 1e-6
        numeric = (G(float(a + h)) - G(float(a - h))) / (2.0 * h)
        analytic = 2.0 * phi(float(a)) / (1.0 + float(a) ** 2) ** 2
        assert abs(numeric - analytic) < 2e-8

    grid = np.linspace(0.1, 6.0, 300)
    eps = np.array([eps_force(float(a)) for a in grid])
    assert np.all(np.diff(eps) < 0.0)

    assert eps_force(1e-3) > 700.0
    assert eps_force(2e-3) < eps_force(1e-3)

    e25 = eps_force(2.5)
    e30 = eps_force(3.0)
    assert e25 < 9.7e-4
    assert e30 < 1.5e-4

    ac = 0.02
    ell0 = 2.5
    core_scale = ac * ac / (ell0 * ell0 + sigma * sigma)
    assert core_scale < 6e-5

    print(
        "r214a_ok "
        f"eps_force_2p5={e25:.6e} "
        f"eps_force_3={e30:.6e} "
        f"core_scale={core_scale:.6e}"
    )


if __name__ == "__main__":
    main()
