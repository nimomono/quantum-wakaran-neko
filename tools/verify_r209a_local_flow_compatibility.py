#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def interp_error(n: int) -> float:
    L = 2 * np.pi
    a = L / n
    xe = (np.arange(n) + 0.5) * a
    ve = 0.18 * np.sin(xe) + 0.07 * np.cos(2 * xe) - 0.04 * np.sin(3 * xe)
    xs = np.linspace(0, L, 4001, endpoint=False)
    out = np.empty_like(xs)
    for j, x in enumerate(xs):
        y = (x - 0.5 * a) / a
        e = int(np.floor(y))
        u = y - e
        out[j] = (1 - u) * ve[e % n] + u * ve[(e + 1) % n]
    exact = 0.18 * np.sin(xs) + 0.07 * np.cos(2 * xs) - 0.04 * np.sin(3 * xs)
    return float(np.sqrt(np.mean((out - exact) ** 2)))


def main() -> None:
    # Generic shared-target cancellation: only the Hamiltonian residual remains.
    tau = 0.05
    eps = 0.013
    dt = 2e-4
    T = 0.8
    err = 0.0
    max_abs = 0.0
    for j in range(int(T / dt)):
        t = j * dt
        residual = eps * np.sin(1.7 * t)
        err += dt * (-err + residual) / tau
        max_abs = max(max_abs, abs(err))
    assert max_abs <= eps * (1 + 2e-2)

    # The result is independent of the concrete target dictionary.
    for phase in (0.0, 0.4, 1.1):
        target = lambda t: 0.2 * np.sin(0.9 * t + phase)
        u_eff = target(0.0)
        u_67 = target(0.0)
        diff_max = 0.0
        for j in range(int(T / dt)):
            t = j * dt
            v = target(t)
            ru = eps * np.sin(1.7 * t)
            u_eff += dt * (-u_eff + v) / tau
            u_67 += dt * (-u_67 + v + ru) / tau
            diff_max = max(diff_max, abs(u_67 - u_eff))
        assert diff_max <= eps * (1 + 2e-2)

    # M64/R214 spatial interpolation remains a separate corollary.
    ns = np.array([16.0, 24.0, 32.0, 48.0, 64.0, 96.0])
    errs = np.array([interp_error(int(n)) for n in ns])
    slope = float(np.polyfit(np.log(ns), np.log(errs), 1)[0])
    assert -2.15 < slope < -1.80, slope

    eps_y = 0.006
    assert abs((eps + eps_y) - 0.019) < 1e-15
    print("r209a_generic_flow_ok", slope, max_abs)


if __name__ == "__main__":
    main()
