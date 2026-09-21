#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def graph_check(seed: int = 7) -> None:
    rng = np.random.default_rng(seed)
    n = 7
    j0 = 1.3
    delta = 0.04
    q = np.full(n, 1.0 / n)

    z = rng.normal(size=n) + 1j * rng.normal(size=n)
    h = np.zeros((n, n), dtype=np.complex128)
    for i in range(n - 1):
        amp = 0.4 + 0.2 * rng.random()
        phase = 0.5 * rng.normal()
        value = amp * np.exp(1j * phase)
        h[i, i + 1] = value
        h[i + 1, i] = np.conjugate(value)

    s = float(np.vdot(z, z).real)
    r = np.abs(z) ** 2 + delta * q * s
    pi = r / ((1.0 + delta) * s)

    dpi = np.zeros(n)
    master = np.zeros(n)
    for i in range(n):
        for k in range(i + 1, n):
            if h[i, k] == 0:
                continue
            current = (2.0 / j0) * np.imag(np.conjugate(z[k]) * h[k, i] * z[i])
            activity = abs(h[i, k]) / j0 * (r[i] + r[k])
            assert activity + 1e-13 >= abs(current)

            k_ik = (activity + current) / (2.0 * r[i])
            k_ki = (activity - current) / (2.0 * r[k])
            assert k_ik >= -1e-13
            assert k_ki >= -1e-13

            normalized_current = current / ((1.0 + delta) * s)
            dpi[i] -= normalized_current
            dpi[k] += normalized_current

            master[i] += pi[k] * k_ki - pi[i] * k_ik
            master[k] += pi[i] * k_ik - pi[k] * k_ki

    assert np.max(np.abs(master - dpi)) < 1e-12


def r125_regularization_check() -> None:
    delta = 0.08
    q = np.array([0.5, 0.5])
    p_plus = np.array([1.0, 0.0])
    p_minus = np.array([0.0, 1.0])
    p_mix = q.copy()

    reg = lambda p: (p + delta * q) / (1.0 + delta)
    tv = lambda p, r: 0.5 * np.abs(p - r).sum()

    assert abs(tv(reg(p_plus), reg(p_mix)) - 1.0 / (2.0 * (1.0 + delta))) < 1e-13
    assert abs(tv(reg(p_plus), reg(p_minus)) - 1.0 / (1.0 + delta)) < 1e-13


def main() -> None:
    graph_check()
    r125_regularization_check()
    print("M64 finite-graph R161 and R125 checks passed")


if __name__ == "__main__":
    main()
