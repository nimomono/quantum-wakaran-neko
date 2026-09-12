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


def check_exact_darboux_chart() -> None:
    sigma = 5.0
    j0 = 0.73
    samples = [
        (0.3, -0.4),
        (1.1, 0.7),
        (-1.4, 0.2),
    ]
    for q, p in samples:
        r2 = q*q + p*p
        root = math.sqrt(sigma - r2/4.0)
        sx = q * root
        sy = p * root
        sz = sigma - r2/2.0
        assert_close(sx*sx + sy*sy + sz*sz, sigma*sigma, 1e-13,
                     f"darboux_spin_length_q={q:g}_p={p:g}")
        psi_abs2 = r2 / (2.0*j0)
        assert_close(sigma - sz, j0*psi_abs2, 1e-14,
                     f"darboux_action_identity_q={q:g}_p={p:g}")


def check_two_spin_shell() -> None:
    # ∫ dK1 dK2 δ(A-K1-K2) = ∫_0^A dK1 = A.
    for A in (0.2, 0.7, 1.4):
        grid = np.linspace(0.0, A, 20001)
        omega = np.trapezoid(np.ones_like(grid), grid)
        assert_close(omega / A, 1.0, 1e-12, f"shell_linearity_A={A:g}")


def shell_partition_closed(A: float, c: float) -> float:
    z = math.sqrt(c) * A
    return (
        math.exp(-c*A*A)/(2.0*c)
        + A*math.sqrt(math.pi)/(2.0*math.sqrt(c))*(1.0 + math.erf(z))
    )


def shell_partition_numeric(A: float, c: float) -> float:
    # S exp[-c(S-A)^2] is already negligible at this cutoff for tested values.
    upper = A + 12.0/math.sqrt(c)
    s = np.linspace(0.0, upper, 400001)
    return float(np.trapezoid(s*np.exp(-c*(s-A)**2), s))


def check_finite_shell_closed_form() -> None:
    for A, c in ((0.4, 2.0), (0.8, 5.0), (1.3, 7.0)):
        z_num = shell_partition_numeric(A, c)
        z_closed = shell_partition_closed(A, c)
        assert_close(z_num, z_closed, 2e-10,
                     f"finite_shell_partition_A={A:g}_c={c:g}")

        delta = math.exp(-c*A*A) / (
            math.sqrt(math.pi*c)*(1.0 + math.erf(math.sqrt(c)*A))
        )
        dlog_closed = 1.0/(A + delta)
        h = 1e-6
        dlog_num = (
            math.log(shell_partition_closed(A+h, c))
            - math.log(shell_partition_closed(A-h, c))
        )/(2.0*h)
        assert_close(dlog_num, dlog_closed, 2e-9,
                     f"finite_shell_log_derivative_A={A:g}_c={c:g}")


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


def check_r194d_prime_scaling() -> None:
    # 候補単一parameter familyの指数関係だけを確認する。
    # これはLLGS->Adlerやwall absorptionそのものを検証するものではない。
    nu = 0.37
    D0 = 2.4
    K0 = 1.6
    lam0 = 0.7
    for eps in (0.20, 0.10, 0.05):
        carrier = eps**-3
        sigma = eps**-8
        pickup = eps
        D = D0*eps**-2
        K = K0*eps**-4
        tau_h = 1.0/K
        ell_h = math.sqrt(D/K)
        lam = lam0*eps**2

        assert_close(carrier**2/sigma, eps**2, 1e-13,
                     f"r194d_amp_scaling_eps={eps:g}")
        assert_close(pickup**2, eps**2, 1e-15,
                     f"r194d_loading_scaling_eps={eps:g}")
        assert_close(pickup*carrier, eps**-2, 1e-12,
                     f"r194d_pickup_carrier_eps={eps:g}")
        assert_close(tau_h, eps**4/K0, 1e-15,
                     f"r194d_healing_time_eps={eps:g}")
        assert_close(ell_h, math.sqrt(D0/K0)*eps, 1e-14,
                     f"r194d_healing_length_eps={eps:g}")
        assert_close(math.sqrt(nu*tau_h)/ell_h,
                     math.sqrt(nu/D), 1e-15,
                     f"r194d_brownian_tracking_identity_eps={eps:g}")
        assert_close(lam/ell_h,
                     (lam0/math.sqrt(D0/K0))*eps, 1e-14,
                     f"r194d_wall_to_healing_eps={eps:g}")


def check_r194d_prime_matching() -> None:
    # J_Phi = G_h J_inf, J_inf = -A_r S_x/J0.
    # sigma_DW G_h A_r/(Gamma_DW J0)=1/m がdrift matching。
    m = 2.3
    j0 = 1.1
    gamma_dw = 1.7
    gain_h = 2.0
    sigma_dw = 1.0
    A_r = gamma_dw*j0/(sigma_dw*gain_h*m)
    coeff = sigma_dw*gain_h*A_r/(gamma_dw*j0)
    assert_close(coeff, 1/m, 1e-14, "r194d_prime_gain_matching")


def check_temperature_plateau_algebra() -> None:
    # Gamma(T)=Gamma0+kBT*G -> nu=kBT/Gamma.
    # Rewrite exactly as (1/G)/(1+Gamma0/(kBT*G)).
    gamma0 = 0.07
    G = 1.9
    for kbt in (0.5, 2.0, 8.0):
        gamma = gamma0 + kbt*G
        nu = kbt/gamma
        rewritten = (1.0/G)/(1.0 + gamma0/(kbt*G))
        assert_close(nu, rewritten, 1e-15,
                     f"temperature_plateau_identity_kBT={kbt:g}")

    kbt_hi = 20.0
    nu_hi = kbt_hi/(gamma0 + kbt_hi*G)
    rel = abs(nu_hi - 1.0/G)/(1.0/G)
    expected = gamma0/(gamma0 + kbt_hi*G)
    assert_close(rel, expected, 1e-15, "temperature_plateau_relative_error")


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
    check_exact_darboux_chart()
    check_two_spin_shell()
    check_finite_shell_closed_form()
    check_osmotic_drift()
    check_fokker_planck_equivariance()
    check_backward_drift()
    check_nelson_harmonic_ground_state()
    check_r194d_prime_scaling()
    check_r194d_prime_matching()
    check_temperature_plateau_algebra()
    check_wall_width_order()
    print("r194_brownian_spin_nelson_ok")


if __name__ == "__main__":
    main()
