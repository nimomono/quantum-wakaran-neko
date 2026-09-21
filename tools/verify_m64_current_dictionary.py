#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def exact_edge_identities() -> None:
    rng = np.random.default_rng(23)
    for _ in range(100):
        zi = rng.normal() + 1j * rng.normal()
        zj = rng.normal() + 1j * rng.normal()
        cp = (zi - 1j * zj) / np.sqrt(2.0)
        cm = (zi + 1j * zj) / np.sqrt(2.0)
        ip = abs(cp) ** 2
        im = abs(cm) ** 2
        assert abs((ip + im) - (abs(zi) ** 2 + abs(zj) ** 2)) < 2e-12
        assert abs((ip - im) - 2.0 * np.imag(np.conjugate(zi) * zj)) < 2e-12


def regularized_current_convergence() -> None:
    nu = 0.37
    amplitude2 = 1.4
    background = 0.9
    delta = 0.07
    wave_number = 0.63

    errors = []
    for n in (40, 80, 160, 320):
        a = 1.0 / n
        zi = np.sqrt(amplitude2)
        zj = np.sqrt(amplitude2) * np.exp(1j * wave_number * a)

        numerator = 2.0 * np.imag(np.conjugate(zi) * zj)
        denominator = 2.0 * (amplitude2 + delta * background)
        chirality = numerator / denominator
        c_j = 2.0 * nu / a
        observed = c_j * chirality

        target = 2.0 * nu * wave_number * amplitude2 / (amplitude2 + delta * background)
        errors.append(abs(observed - target))

    errors = np.asarray(errors)
    assert np.all(errors[1:] < 0.30 * errors[:-1])


def main() -> None:
    exact_edge_identities()
    regularized_current_convergence()
    print("M64 regularized current dictionary checks passed")


if __name__ == "__main__":
    main()
