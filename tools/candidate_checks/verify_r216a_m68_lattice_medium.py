#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def hamiltonian(p, s, a, mass, nu):
    edge = 0.5 * (p + np.roll(p, -1))
    ds = (np.roll(s, -1) - s) / a
    fisher = 2.0 * mass * nu**2 / a**2 * np.sum(
        (np.sqrt(np.roll(p, -1)) - np.sqrt(p)) ** 2
    )
    return float(np.sum(edge * ds**2 / (2.0 * mass)) + fisher)


def main() -> None:
    length = 2.0 * math.pi
    mass = 0.8
    nu = 0.35

    n = 96
    a = length / n
    x = np.arange(n) * a
    pi = (1.0 + 0.22 * np.cos(x) + 0.08 * np.cos(2.0 * x)) / length
    p = a * pi
    p /= np.sum(p)
    s = 0.17 * np.sin(x) - 0.04 * np.sin(2.0 * x)
    assert np.min(p) > 0.0
    assert abs(np.sum(p) - 1.0) < 1e-14

    edge = 0.5 * (p + np.roll(p, -1))
    ds = (np.roll(s, -1) - s) / a
    flux = edge * ds / (mass * a)
    grad_s = np.roll(flux, 1) - flux
    assert abs(np.sum(grad_s)) < 2e-14

    eps = 1e-7
    grad_p = np.empty_like(p)
    h0 = hamiltonian(p, s, a, mass, nu)
    for i in range(n):
        pp = p.copy()
        pm = p.copy()
        pp[i] += eps
        pm[i] -= eps
        grad_p[i] = (
            hamiltonian(pp, s, a, mass, nu)
            - hamiltonian(pm, s, a, mass, nu)
        ) / (2.0 * eps)
    energy_rate = float(np.dot(grad_p, grad_s) + np.dot(grad_s, -grad_p))
    assert abs(energy_rate) < 1e-12
    assert h0 > 0.0

    def continuum_fisher() -> float:
        xx = np.linspace(0.0, length, 400000, endpoint=False)
        pii = (1.0 + 0.22 * np.cos(xx) + 0.08 * np.cos(2.0 * xx)) / length
        pix = (-0.22 * np.sin(xx) - 0.16 * np.sin(2.0 * xx)) / length
        root_x = pix / (2.0 * np.sqrt(pii))
        return float(2.0 * mass * nu**2 * length * np.mean(root_x**2))

    target = continuum_fisher()
    ns = np.array([48, 96, 192, 384])
    errs = []
    for nn in ns:
        aa = length / nn
        xx = np.arange(nn) * aa
        pii = (1.0 + 0.22 * np.cos(xx) + 0.08 * np.cos(2.0 * xx)) / length
        pp = aa * pii
        pp /= np.sum(pp)
        disc = 2.0 * mass * nu**2 / aa**2 * np.sum(
            (np.sqrt(np.roll(pp, -1)) - np.sqrt(pp)) ** 2
        )
        errs.append(abs(float(disc) - target))
    errs = np.asarray(errs)
    slope = float(np.polyfit(np.log(length / ns), np.log(errs), 1)[0])
    assert 1.9 < slope < 2.1, slope

    print(
        "r216a_m68_lattice_ok "
        f"capacity_residual={abs(np.sum(grad_s)):.3e} "
        f"energy_rate={abs(energy_rate):.3e} "
        f"fisher_slope={slope:.6f}"
    )


if __name__ == "__main__":
    main()
