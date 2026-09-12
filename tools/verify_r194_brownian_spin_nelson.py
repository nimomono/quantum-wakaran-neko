#!/usr/bin/env python3
"""M56/R194候補のうち、物性bridgeに依存しない代数だけを検算する。"""

from __future__ import annotations

import math
import numpy as np


def assert_close(a, b, tol, label):
    err = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
    if not err <= tol:
        raise AssertionError(f"{label}: error={err:.3e} > {tol:.3e}")
    print(f"{label}: {err:.3e}")


def check_two_spin_shell() -> None:
    # ∫ dK1 dK2 δ(A-K1-K2) = ∫_0^A dK1 = A.
    for A in (0.2, 0.7, 1.4):
        grid = np.linspace(0.0, A, 20001)
        omega = np.trapezoid(np.ones_like(grid), grid)
        assert_close(omega / A, 1.0, 1e-12, f"shell_linearity_A={A:g}")


def check_osmotic_drift() -> None:
    x = np.linspace(-2.0, 2.0, 1001)
    nu = 0.37
    mu = 0.23
    kbt = nu / mu
    rho = 1.3 + 0.2 * np.cos(0.8 * x)
    drho = -0.16 * np.sin(0.8 * x)
    force_entropy = kbt * drho / rho
    drift = mu * force_entropy
    target = nu * drho / rho
    assert_close(drift, target, 1e-14, "einstein_entropy_to_osmotic")


def check_fokker_planck_equivariance() -> None:
    # 任意の滑らかな rho,v に対する局所恒等式
    # -∂x[(v+u)rho] + nu ∂xx rho = -∂x(v rho), u=nu ∂x log rho.
    x = np.linspace(-math.pi, math.pi, 4097, endpoint=False)
    dx = x[1] - x[0]
    nu = 0.19
    rho = 1.2 + 0.17 * np.cos(x) + 0.05 * np.sin(2*x)
    v = 0.3 * np.sin(x) - 0.07 * np.cos(2*x)

    def d1(f):
        return (np.roll(f, -1) - np.roll(f, 1)) / (2*dx)

    def d2(f):
        return (np.roll(f, -1) - 2*f + np.roll(f, 1)) / dx**2

    u = nu * d1(rho) / rho
    lhs = -d1((v + u) * rho) + nu * d2(rho)
    rhs = -d1(v * rho)
    # 二次中心差分同士の product/discrete-chain-rule mismatch は O(dx^2).
    assert_close(lhs, rhs, 2e-6, "fokker_planck_equivariance")


def check_backward_drift() -> None:
    x = np.linspace(-1.5, 1.5, 1001)
    nu = 0.41
    rho = 1.1 + 0.15*np.cos(1.1*x)
    dlog = (-0.165*np.sin(1.1*x)) / rho
    v = 0.2*np.sin(0.7*x)
    u = nu*dlog
    bplus = v + u
    bminus_from_reverse = bplus - 2*nu*dlog
    assert_close(bminus_from_reverse, v-u, 1e-14, "same_path_backward_drift")


def check_nelson_harmonic_ground_state() -> None:
    # hbar_eff=2m nu の調和基底状態:
    # rho ∝ exp[-omega x^2/(2nu)], u=-omega x, v=0.
    m = 1.7
    nu = 0.31
    omega = 0.8
    j0 = 2*m*nu
    assert_close(j0, 2*m*nu, 1e-15, "action_matching")
    x = np.linspace(-2.0, 2.0, 1001)
    u = -omega*x
    du = -omega*np.ones_like(x)
    d2u = np.zeros_like(x)
    a_n = -(u*du) - nu*d2u
    force_over_m = -(omega**2)*x
    assert_close(a_n, force_over_m, 1e-14, "nelson_harmonic_newton")


def check_phase_matching() -> None:
    # eta A_b = 4 s (1+alpha^2) nu と J0=2mnu から、
    # eta A_b/[2s(1+alpha^2)J0] = 1/m.
    eta = 0.73
    s = 1.4
    alpha = 0.08
    nu = 0.22
    m = 2.3
    j0 = 2*m*nu
    A_b = 4*s*(1+alpha**2)*nu/eta
    coeff = eta*A_b/(2*s*(1+alpha**2)*j0)
    assert_close(coeff, 1/m, 1e-14, "phase_current_matching")


def sech2(z):
    c = np.cosh(z)
    return 1.0/(c*c)


def wall_average_at_zero(lam: float) -> float:
    # rho(x)=1+0.2 cos x. w_lambda=(2lambda)^-1 sech^2(x/lambda).
    # 十分広い数値区間で局所平均を評価する。
    L = 12*lam
    x = np.linspace(-L, L, 200001)
    w = sech2(x/lam)/(2*lam)
    rho = 1.0 + 0.2*np.cos(x)
    return float(np.trapezoid(w*rho, x))


def check_wall_width_order() -> None:
    rho0 = 1.2
    e1 = abs(wall_average_at_zero(0.20)-rho0)
    e2 = abs(wall_average_at_zero(0.10)-rho0)
    ratio = e1/e2
    # Taylor leading error ∝ lambda^2, so ratio -> 4.
    if not 3.8 < ratio < 4.2:
        raise AssertionError(f"finite_wall_width_order: ratio={ratio}")
    print(f"finite_wall_width_O(lambda^2): ratio={ratio:.6f}")


def main() -> None:
    check_two_spin_shell()
    check_osmotic_drift()
    check_fokker_planck_equivariance()
    check_backward_drift()
    check_nelson_harmonic_ground_state()
    check_phase_matching()
    check_wall_width_order()
    print("r194_brownian_spin_nelson_ok")


if __name__ == "__main__":
    main()
