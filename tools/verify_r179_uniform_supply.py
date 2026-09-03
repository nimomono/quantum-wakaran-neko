#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


TOL = 2.0e-12


def main() -> None:
    rho = 0.63
    eta_cold = 2.0e-5
    initial = 4.7
    rounds = 31
    state = initial
    for index in range(rounds):
        cold = eta_cold * np.sin(0.7 * index)
        state = rho * state + np.sqrt(1.0 - rho * rho) * cold
    bound = rho**rounds * initial + eta_cold / (1.0 - rho)
    assert abs(state) <= bound + TOL

    for digits in range(1, 13):
        grid = (np.arange(2**digits) + 0.5) / 2**digits
        thresholds = np.linspace(0.0, 1.0, 4001)
        cdf = np.searchsorted(grid, thresholds, side="left") / len(grid)
        discrepancy = float(np.max(np.abs(cdf - thresholds)))
        assert discrepancy <= 2.0 ** (-digits) + TOL

    ideal = np.full(16, 1.0 / 16.0)
    bias = np.linspace(-1.0, 1.0, 16)
    actual = ideal + 1.0e-3 * bias
    actual /= np.sum(actual)
    input_tv = 0.5 * float(np.sum(np.abs(actual - ideal)))
    mapping = np.array([index.bit_count() % 3 for index in range(16)])
    output_ideal = np.array([np.sum(ideal[mapping == value]) for value in range(3)])
    output_actual = np.array([np.sum(actual[mapping == value]) for value in range(3)])
    output_tv = 0.5 * float(np.sum(np.abs(output_actual - output_ideal)))
    assert output_tv <= input_tv + TOL

    required = np.ceil(np.log(1.0e-9 / initial) / np.log(rho))
    assert required > 0

    print(f"partial-SWAP residual = {abs(state):.3e} <= {bound:.3e}")
    print(f"12-digit threshold discrepancy <= {2.0 ** -12:.3e}")
    print(f"data-processing TV = {output_tv:.3e} <= {input_tv:.3e}")
    print(f"rounds for 1e-9 residual = {int(required)}")


if __name__ == "__main__":
    main()
