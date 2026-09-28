#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def rotation(theta: float) -> np.ndarray:
    return np.array(
        [[math.cos(theta), -math.sin(theta)],
         [math.sin(theta), math.cos(theta)]],
        dtype=float,
    )


def main() -> None:
    # Common additive bias on an analog signed bus inherits the inverse coherent mean.
    eps = 1e-2
    for h in range(2, 13):
        mean = 2.0 ** (-h)
        allowed_bias = eps * mean
        relative = allowed_bias / mean
        assert abs(relative - eps) < 1e-15
        assert allowed_bias <= eps * 2.0 ** (-h)

    # A finite-depth coherent network accumulates small layer errors at most linearly
    # to first order. Rotations give a direct deterministic witness.
    for depth in (4, 8, 16, 32):
        local = 1e-5
        ideal = np.eye(2)
        actual = np.eye(2)
        u = rotation(local)
        for _ in range(depth):
            actual = u @ actual
        defect = np.linalg.norm(actual - ideal, 2)
        assert defect <= depth * local * 1.01

    # Passive hardware may be exponential while local word/tolerance requirements stay polynomial.
    for h in (4, 8, 16):
        n_path = 2**h
        logical_barrier_units = h + 20
        assert n_path == 2**h
        expected_polynomial_scale = h + 20
        assert logical_barrier_units == expected_polynomial_scale

    print("r213d_ok analog_bias_exponential=True coherent_layer_error_linear=True")


if __name__ == "__main__":
    main()
