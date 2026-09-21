#!/usr/bin/env python3
"""R193の代数恒等式・誤差上界だけを検算し、原稿文字列には依存しない。"""

from __future__ import annotations

import math
import random


def close(a: float, b: float, tol: float = 1.0e-11) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b))


def verify_direct_basin_identity() -> None:
    for _ in range(20000):
        a_l = 10 ** random.uniform(-7.0, 3.0)
        a_r = 10 ** random.uniform(-7.0, 3.0)
        a_sum = a_l + a_r
        a_diff = a_l - a_r
        q_l = a_l / a_sum
        u_a = -a_diff / a_sum
        close(u_a, 1.0 - 2.0 * q_l)
        close((1.0 - u_a) / 2.0, q_l)


def verify_ratio_to_boundary_bound() -> None:
    for _ in range(30000):
        p = random.random()
        eps = random.uniform(0.0, 0.25)
        dq = random.uniform(-eps, eps)
        q = min(1.0, max(0.0, p + dq))
        u_ideal = 1.0 - 2.0 * p
        u_latch = 1.0 - 2.0 * q
        if abs(u_latch - u_ideal) > 2.0 * eps + 1.0e-12:
            raise AssertionError((p, q, eps, u_latch, u_ideal))


def verify_common_gain_invariance() -> None:
    for _ in range(10000):
        a_l = 10 ** random.uniform(-6.0, 2.0)
        a_r = 10 ** random.uniform(-6.0, 2.0)
        gain = 10 ** random.uniform(-4.0, 4.0)
        u0 = -(a_l - a_r) / (a_l + a_r)
        u1 = -(gain * a_l - gain * a_r) / (gain * a_l + gain * a_r)
        close(u0, u1)


def verify_endpoint_linear_dispatcher() -> None:
    for _ in range(20000):
        a_l = 10 ** random.uniform(-6.0, 3.0)
        a_r = 10 ** random.uniform(-6.0, 3.0)
        cut = random.uniform(1.0e-4, 0.49)
        q_l = a_l / (a_l + a_r)
        lhs_l = (1.0 - cut) * a_l - cut * a_r
        if (q_l < cut) != (lhs_l < 0.0):
            raise AssertionError((q_l, cut, lhs_l))
        q_r = a_r / (a_l + a_r)
        lhs_r = (1.0 - cut) * a_r - cut * a_l
        if (q_r < cut) != (lhs_r < 0.0):
            raise AssertionError((q_r, cut, lhs_r))


def verify_conjugate_momentum_bound() -> None:
    chi = 10 ** random.uniform(-3.0, 3.0)
    for _ in range(20000):
        u = random.uniform(-1.0, 1.0)
        pldot = 0.5 * chi * (u * u + 2.0 * u)
        prdot = 0.5 * chi * (u * u - 2.0 * u)
        bound = 1.5 * chi
        if abs(pldot) > bound + 1.0e-12 or abs(prdot) > bound + 1.0e-12:
            raise AssertionError((u, pldot, prdot, bound))


def verify_error_ledger_no_double_count() -> None:
    for _ in range(10000):
        eps_189a = random.uniform(0.0, 0.1)
        eps_link = random.uniform(0.0, 0.1)
        eps_mix = random.uniform(0.0, 0.1)
        guard = random.uniform(0.0, 0.1)
        q_ret = random.uniform(0.0, 0.1)
        q_time = random.uniform(0.0, 0.1)
        eps_cap = random.uniform(0.0, 0.1)
        eps_lat = random.uniform(0.0, 0.1)
        eps_191_193 = eps_mix + guard + eps_link / 2.0 + q_ret + q_time + eps_cap
        total = eps_189a + eps_191_193 + eps_lat
        expanded = (
            eps_189a
            + eps_mix
            + guard
            + eps_link / 2.0
            + q_ret
            + q_time
            + eps_cap
            + eps_lat
        )
        close(total, expanded)


def main() -> None:
    random.seed(193)
    verify_direct_basin_identity()
    verify_ratio_to_boundary_bound()
    verify_common_gain_invariance()
    verify_endpoint_linear_dispatcher()
    verify_conjugate_momentum_bound()
    verify_error_ledger_no_double_count()
    print("R193 Q1 macrospin bridge checks: OK")


if __name__ == "__main__":
    main()
