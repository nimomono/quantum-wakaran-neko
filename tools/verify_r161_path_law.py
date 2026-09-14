#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def sample(t: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    eps = 0.04
    pi = np.array([
        1.0 / 3.0 + eps * math.sin(t),
        1.0 / 3.0 - eps * math.sin(t),
        1.0 / 3.0,
    ])
    dpi = np.array([eps * math.cos(t), -eps * math.cos(t), 0.0])

    # Convention: dot(pi_i) = sum_j j_{j i}.
    j = np.zeros((3, 3))
    j[1, 0] = eps * math.cos(t)
    j[0, 1] = -j[1, 0]

    activity = np.array([
        [0.0, 0.12, 0.08],
        [0.12, 0.0, 0.07],
        [0.08, 0.07, 0.0],
    ])
    kp = np.zeros((3, 3))
    km = np.zeros((3, 3))
    for i in range(3):
        for k in range(3):
            if i == k:
                continue
            kp[i, k] = (activity[i, k] + j[i, k]) / (2.0 * pi[i])
            km[i, k] = (activity[i, k] - j[i, k]) / (2.0 * pi[i])
    return pi, dpi, j, kp, km


def main() -> None:
    hazard_max = 0.0
    for t in np.linspace(0.0, 4.0, 401):
        pi, dpi, j, kp, km = sample(float(t))
        assert np.min(pi) > 0.0
        assert np.min(kp) >= -1e-14
        assert np.min(km) >= -1e-14

        forward = np.zeros(3)
        for i in range(3):
            forward[i] = sum(pi[k] * kp[k, i] - pi[i] * kp[i, k] for k in range(3) if k != i)
        assert np.max(np.abs(forward - dpi)) < 1e-12

        for i in range(3):
            for k in range(3):
                if i == k:
                    continue
                bayes = pi[k] * kp[k, i] / pi[i]
                assert abs(bayes - km[i, k]) < 1e-12

        hazard_max = max(hazard_max, float(np.max(np.sum(kp, axis=1))))

    assert math.isfinite(hazard_max) and hazard_max < 1.0
    print(f"r161_path_law_ok hazard_max={hazard_max:.6f}")


if __name__ == "__main__":
    main()
