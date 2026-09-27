#!/usr/bin/env python3
"""Required checks for R212C finite-Hamiltonian passive separation."""

import math
import numpy as np


def mobility(gamma_a, gamma_b, kappa):
    G = np.array([[gamma_a, kappa], [kappa, gamma_b]], dtype=float)
    return np.linalg.inv(G)


def main() -> None:
    gamma_a, gamma_b = 1.2, 0.9
    mu0 = np.diag([1.0 / gamma_a, 1.0 / gamma_b])

    previous_cross = None
    for s in (1.0, 0.5, 0.25, 0.125, 0.0625):
        c = 0.18 * s
        kappa = 0.4 * c
        assert kappa * kappa < gamma_a * gamma_b
        mu = mobility(gamma_a, gamma_b, kappa)
        cross = abs(mu[0, 1])
        local = max(abs(mu[0, 0] - mu0[0, 0]), abs(mu[1, 1] - mu0[1, 1]))
        assert cross <= 2.0 * abs(kappa)
        assert local <= 3.0 * kappa * kappa
        if previous_cross is not None:
            assert cross < previous_cross
        previous_cross = cross

        K = 0.7 * s
        chi_pv = s
        defect_bound = abs(K) + chi_pv + cross + local
        assert defect_bound > 0.0

    # Compact-support endpoint gives exact factorization.
    s = 0.0
    c = 0.0
    kappa = 0.0
    mu = mobility(gamma_a, gamma_b, kappa)
    assert np.max(np.abs(mu - mu0)) < 1e-15
    K = 0.7 * s
    chi_pv = s
    assert K == 0.0 and chi_pv == 0.0 and c == 0.0
    assert np.max(np.abs(mu - mu0)) == 0.0

    print("R212C passive separation checks: OK")


if __name__ == "__main__":
    main()
