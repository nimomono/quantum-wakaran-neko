#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def projector(axis: np.ndarray, sign: int) -> np.ndarray:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma = axis[0] * sx + axis[1] * sy + axis[2] * sz
    return (np.eye(2) + sign * sigma) / 2


singlet = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
settings_a = [np.array([0.0, 0.0, 1.0]), np.array([1.0, 0.0, 0.0])]
settings_b = [
    np.array([1.0, 0.0, 1.0]) / math.sqrt(2),
    np.array([-1.0, 0.0, 1.0]) / math.sqrt(2),
]

corr = np.zeros((2, 2))
for ix, a in enumerate(settings_a):
    for iy, b in enumerate(settings_b):
        probs: dict[tuple[int, int], float] = {}
        for r in (-1, 1):
            pa = np.kron(projector(a, r), np.eye(2))
            branch = pa @ singlet
            p_r = float(np.vdot(branch, branch).real)
            assert p_r > 0
            cond_sum = 0.0
            for s in (-1, 1):
                pb = np.kron(np.eye(2), projector(b, s))
                joint_action = float(np.vdot(pb @ branch, pb @ branch).real)
                p_cond = joint_action / p_r
                probs[(r, s)] = p_r * p_cond
                cond_sum += p_cond
            assert abs(cond_sum - 1.0) < 2e-12
        assert abs(sum(probs.values()) - 1.0) < 2e-12
        marg_a = {r: sum(probs[(r, s)] for s in (-1, 1)) for r in (-1, 1)}
        marg_b = {s: sum(probs[(r, s)] for r in (-1, 1)) for s in (-1, 1)}
        assert max(abs(v - 0.5) for v in marg_a.values()) < 2e-12
        assert max(abs(v - 0.5) for v in marg_b.values()) < 2e-12
        corr[ix, iy] = sum(r * s * probs[(r, s)] for r in (-1, 1) for s in (-1, 1))
        assert abs(corr[ix, iy] + float(a @ b)) < 2e-12

chsh = corr[0, 0] + corr[0, 1] + corr[1, 0] - corr[1, 1]
assert abs(abs(chsh) - 2 * math.sqrt(2)) < 2e-12
print("R180 sequential two-end R191 checks passed")
