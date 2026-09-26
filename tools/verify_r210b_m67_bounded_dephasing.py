#!/usr/bin/env python3
import itertools
import numpy as np


def main() -> None:
    J0 = 1.0
    pstar = 0.7
    lam = 0.18
    omega = np.array([1.6, 1.9, 2.3])
    mass = np.array([1.0, 1.2, 0.8])

    def f(p):
        return pstar * np.sin(np.pi * p / (2 * pstar))

    grid = np.linspace(-8 * pstar, 8 * pstar, 20001)
    assert np.max(np.abs(f(grid))) <= pstar + 2e-15
    assert abs(f(pstar) - pstar) < 1e-14
    assert abs(f(-pstar) + pstar) < 1e-14

    margin = omega.min() - abs(lam) * pstar / J0
    assert margin > 0.0

    # Global lower bound on the full action--bath block.
    rng = np.random.default_rng(2100)
    for _ in range(1000):
        action = rng.exponential(size=3)
        momentum = rng.normal(scale=4 * pstar, size=3)
        h = np.sum(
            omega * action
            + momentum**2 / (2 * mass)
            + (lam / J0) * action * f(momentum)
        )
        lower = np.sum(
            (omega - abs(lam) * pstar / J0) * action
            + momentum**2 / (2 * mass)
        )
        assert h + 1e-12 >= lower
        assert lower >= 0.0

    # Independent prepared P_n=±p* recovers the R123 cos^2 factor exactly.
    signs = list(itertools.product((-1.0, 1.0), repeat=2))
    for t in np.linspace(0.0, 7.0, 51):
        vals = []
        for s0, s1 in signs:
            p0, p1 = s0 * pstar, s1 * pstar
            vals.append(np.exp(-1j * (lam / J0) * (f(p0) - f(p1)) * t))
        avg = sum(vals) / len(vals)
        target = np.cos(lam * pstar * t / J0) ** 2
        assert abs(avg - target) < 3e-14

    tdec = np.pi * J0 / (2 * abs(lam) * pstar)
    trec = np.pi * J0 / (abs(lam) * pstar)
    assert abs(trec - 2 * tdec) < 1e-14
    assert abs(np.cos(lam * pstar * tdec / J0) ** 2) < 1e-30
    assert abs(np.cos(lam * pstar * trec / J0) ** 2 - 1.0) < 1e-14
    print("r210b_m67_bounded_dephasing_check_ok", margin, tdec, trec)


if __name__ == "__main__":
    main()
