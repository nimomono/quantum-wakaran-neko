#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


TOL = 2.0e-12


def main() -> None:
    capacities = np.array([0.37, 0.83])
    maximum = 1.0
    attempts = 29
    single = capacities / (2.0 * maximum)
    reject = 1.0 - float(np.sum(single))
    expected = capacities / float(np.sum(capacities)) * (1.0 - reject**attempts)
    geometric = np.array([sum(reject**index * value for index in range(attempts)) for value in single])
    assert np.max(np.abs(geometric - expected)) < TOL
    assert abs(float(np.sum(geometric)) + reject**attempts - 1.0) < TOL

    grid = np.linspace(-3.0, 3.0, 12001)
    base_derivative = np.where(np.abs(grid) <= 2.0, -grid, np.sign(-grid))
    rho_derivative = np.zeros_like(grid)
    shoulder = (np.abs(grid) > 0.8) & (np.abs(grid) < 1.6)
    phase = (np.abs(grid[shoulder]) - 0.8) / 0.8
    rho_derivative[shoulder] = -0.12 * np.sign(grid[shoulder]) * np.sin(np.pi * phase)
    coupling = 0.7
    aperture_maximum = 1.0
    support = np.abs(rho_derivative) > 2.0e-3
    safe = coupling * aperture_maximum * np.max(np.abs(rho_derivative))
    margin = np.min(np.abs(base_derivative[support]))
    assert safe < margin
    signs_base = np.sign(base_derivative[support])
    for offset in (-aperture_maximum, aperture_maximum):
        perturbed = base_derivative[support] + coupling * offset * rho_derivative[support]
        assert np.all(np.sign(perturbed) == signs_base)

    bit_count = 40
    epsilon = 1.0e-3
    tau = epsilon / (16.0 * bit_count)
    regularizer = epsilon / (16.0 * bit_count)
    stage = epsilon / (16.0 * bit_count)
    tape_attempts = int(np.ceil(2.0 * np.log(16.0 * bit_count / epsilon)))
    tape_reject = np.exp(-0.5 * tape_attempts)
    error = (
        2.0 * bit_count * tau
        + bit_count * regularizer / (1.0 + regularizer)
        + bit_count * stage
        + bit_count * tape_reject
        + epsilon / 8.0
    )
    assert error < epsilon

    print(f"finite-tape normalization error = {abs(float(np.sum(geometric)) + reject**attempts - 1.0):.3e}")
    print(f"aperture derivative safety = {safe:.3e} < {margin:.3e}")
    print(f"composed complete-outcome error budget = {error:.3e} < {epsilon:.3e}")


if __name__ == "__main__":
    main()
