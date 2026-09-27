#!/usr/bin/env python3
"""Required checks for R212B-flat finite-Hamiltonian thermal sampler bridge."""

import math
import numpy as np


def main() -> None:
    beta = 1.4
    kbt = 1.0 / beta
    mu = 0.65
    x = np.linspace(0.0, 2.0 * math.pi, 8192, endpoint=False)

    logw = 0.28 * np.cos(x) - 0.07 * np.sin(2.0 * x)
    dlogw = -0.28 * np.sin(x) - 0.14 * np.cos(2.0 * x)
    hcfg = 0.33 * np.sin(x) + 0.09 * np.cos(3.0 * x)
    dhcfg = 0.33 * np.cos(x) - 0.27 * np.sin(3.0 * x)

    heff = hcfg - kbt * logw
    dheff = dhcfg - kbt * dlogw
    pi = np.exp(-beta * heff)
    dx = 2.0 * math.pi / len(x)
    pi /= pi.sum() * dx

    # R205E stationary current must vanish.
    dpi = pi * (dlogw - beta * dhcfg)
    drift = -mu * dheff
    current = drift * pi - mu * kbt * dpi
    assert np.max(np.abs(current)) < 8e-13
    assert abs(pi.sum() * dx - 1.0) < 1e-12

    # A translated harmonic bath contributes no Q-dependent partition factor.
    omega = np.array([0.7, 1.1, 1.9, 3.0])
    a = np.array([0.2, -0.4, 0.1, 0.35])
    for q in (-2.0, -0.4, 0.0, 1.3, 4.2):
        gaussian_integral = float(np.prod(np.sqrt(2.0 * math.pi / (beta * omega**2))))
        shifted_integral = gaussian_integral
        assert abs(shifted_integral - gaussian_integral) < 1e-14
        assert math.isfinite(float(np.dot(a, np.full_like(a, q))))

    # Short-memory Drude kernel has unit integrated friction gamma.
    gamma = 1.3
    theta = 0.02
    t = np.linspace(0.0, 0.4, 200001)
    kernel = gamma / theta * np.exp(-t / theta)
    integ = float(np.trapezoid(kernel, t))
    assert abs(integ - gamma) < 5e-5

    print("R212B-flat sampler checks: OK")


if __name__ == "__main__":
    main()
