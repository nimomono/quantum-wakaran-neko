#!/usr/bin/env python3
"""Required checks for M66/R205A-R205D common-reservoir identities."""

import math


def main() -> None:
    q = [0.2, 0.3, 0.5]
    for w in (0.01, 0.2, 1.0, 3.0, 100.0):
        jac = math.prod(w ** qi for qi in q)
        assert abs(jac - w) <= 1e-12 * max(1.0, abs(w))
        for U in (-7.0, -0.3, 0.0, 2.5, 11.0):
            for R in (-5.0, 0.0, 4.0):
                total = jac * 1.0 * 1.0
                assert abs(total - w) <= 1e-12 * max(1.0, abs(w))
                assert math.isfinite(U + R)

    V0, G0, VH0 = 2.0, 3.0, 5.0
    Lambda = G0 / V0
    kappa = G0 / VH0
    for a_plus, a_minus in ((0.1, 0.9), (1.0, 1.0), (3.0, 0.25)):
        for a in (a_plus, a_minus):
            V = V0 * a
            G = G0 * a
            assert abs(G / V - Lambda) < 1e-14
            assert abs(G / VH0 - kappa * a) < 1e-14

    print("M66/R205A-R205D common-reservoir checks: OK")


if __name__ == "__main__":
    main()
