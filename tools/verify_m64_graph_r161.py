#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def graph_r161_check(seed: int = 7) -> None:
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


def graph_preparation_check(seed: int = 11) -> None:
    rng = np.random.default_rng(seed)
    n = 6
    r = 0.2 + rng.random(n)
    pi = r / r.sum()

    kappa = np.zeros((n, n))
    for i in range(n - 1):
        value = 0.3 + rng.random()
        kappa[i, i + 1] = value
        kappa[i + 1, i] = value

    rates = kappa * r[None, :]
    for i in range(n):
        for j in range(n):
            if i != j:
                assert abs(pi[i] * rates[i, j] - pi[j] * rates[j, i]) < 1e-13

    generator = rates.copy()
    np.fill_diagonal(generator, -rates.sum(axis=1))
    assert np.max(np.abs(pi @ generator)) < 1e-13

    dt = 0.3 / np.max(rates.sum(axis=1))
    transition = np.eye(n) + dt * generator
    assert np.min(transition) >= -1e-14
    assert np.max(np.abs(transition.sum(axis=1) - 1.0)) < 1e-13

    p = rng.random(n)
    p /= p.sum()
    q0 = rng.random(n)
    q0 /= q0.sum()
    tv0 = 0.5 * np.abs(p - q0).sum()
    tv1 = 0.5 * np.abs(p @ transition - q0 @ transition).sum()
    assert tv1 <= tv0 + 1e-13


def regularized_readout_check() -> None:
    delta = 0.08

    # R124: a positive opposite-side increment is reduced only by 1/(1+delta).
    q3 = np.array([0.2, 0.3, 0.5])
    p0 = np.array([0.75, 0.20, 0.05])
    alpha = 0.40
    p1 = np.array([0.35, 0.20, 0.45])
    assert abs((p1[-1] - p0[-1]) - alpha) < 1e-14
    reg = lambda p, q: (p + delta * q) / (1.0 + delta)
    assert abs((reg(p1, q3)[-1] - reg(p0, q3)[-1]) - alpha / (1.0 + delta)) < 1e-13

    # R182: half-period transfer and exact one-period return.
    q_w = np.array([0.25, 0.50, 0.25])
    p_left = np.array([0.70, 0.20, 0.10])
    p_half = np.array([0.10, 0.20, 0.70])
    bc = 0.30
    assert abs((p_half[-1] - p_left[-1]) - 2.0 * bc) < 1e-14
    assert abs((reg(p_half, q_w)[-1] - reg(p_left, q_w)[-1]) - 2.0 * bc / (1.0 + delta)) < 1e-13
    assert np.max(np.abs(reg(p_left, q_w) - reg(p_left.copy(), q_w))) < 1e-14

    # R125: two-output distances scale by 1/(1+delta).
    q2 = np.array([0.5, 0.5])
    p_plus = np.array([1.0, 0.0])
    p_minus = np.array([0.0, 1.0])
    p_mix = q2.copy()
    tv = lambda p, r: 0.5 * np.abs(p - r).sum()

    assert abs(tv(reg(p_plus, q2), reg(p_mix, q2)) - 1.0 / (2.0 * (1.0 + delta))) < 1e-13
    assert abs(tv(reg(p_plus, q2), reg(p_minus, q2)) - 1.0 / (1.0 + delta)) < 1e-13


def main() -> None:
    graph_r161_check()
    graph_preparation_check()
    regularized_readout_check()
    print("M64 finite-graph R161 preparation and readout checks passed")


if __name__ == "__main__":
    main()
