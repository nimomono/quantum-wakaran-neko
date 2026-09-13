#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np

TOL = 2.0e-10
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def beta_star(r: float) -> float:
    return r / (1.0 + math.sqrt(1.0 - r * r))


def force(beta: float, ep: float, em: float) -> float:
    return 2.0 * ep * (1.0 - beta) / (1.0 + beta) - 2.0 * em * (1.0 + beta) / (1.0 - beta)


def dforce_du(beta: float, ep: float, em: float, c: float) -> float:
    return -(4.0 / c) * (ep / (1.0 + beta) ** 2 + em / (1.0 - beta) ** 2)


def solve_beta_delta(gk: float) -> float:
    lo, hi = 0.0, 30.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        value = 1.0 / np.i0(0.5 * mid) ** 2
        if value > gk:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def rk4_step(u: float, t: float, dt: float, rhs) -> float:
    k1 = rhs(t, u)
    k2 = rhs(t + 0.5 * dt, u + 0.5 * dt * k1)
    k3 = rhs(t + 0.5 * dt, u + 0.5 * dt * k2)
    k4 = rhs(t + dt, u + dt * k3)
    return u + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def main() -> None:
    rng = np.random.default_rng(20260914)

    # R195A: exact chiral identities.
    zi = rng.normal() + 1j * rng.normal()
    zj = rng.normal() + 1j * rng.normal()
    cp = (zi - 1j * zj) / np.sqrt(2.0)
    cm = (zi + 1j * zj) / np.sqrt(2.0)
    ip = abs(cp) ** 2
    im = abs(cm) ** 2
    ri = abs(zi) ** 2
    rj = abs(zj) ** 2
    check(abs((ip + im) - (ri + rj)) < TOL, "R195A chiral sum identity")
    check(abs((ip - im) - 2.0 * np.imag(np.conj(zi) * zj)) < TOL, "R195A chiral difference identity")

    # Central dimensionless Q3 witness.
    a = 1.0
    nu = 2.0e-3
    gk = 5.0e-4
    c = 16.0
    d0 = 4.0
    check(abs(gk * c - 4.0 * nu / a) < TOL, "M57 gK-c-nu matching")
    check(abs(d0 - nu / gk) < TOL, "M57 bare diffusion matching")

    # R196A: exact moving-reflector fixed point and stability.
    for r in (-0.7, -0.25, -0.04, 0.0, 0.04, 0.25, 0.7):
        total = 1.7
        ep = 0.5 * total * (1.0 + r)
        em = 0.5 * total * (1.0 - r)
        b = beta_star(r)
        check(abs(force(b, ep, em)) < 2.0e-12, "M57 moving-reflector fixed point")
        check(abs(b - (math.sqrt(ep) - math.sqrt(em)) / (math.sqrt(ep) + math.sqrt(em))) < TOL,
              "M57 square-root fixed-point form")
        check(dforce_du(b, ep, em, c) < 0.0, "M57 moving-reflector stability")
        check(-dforce_du(b, ep, em, c) >= total / c - TOL, "M57 force slope lower bound")

    # Exact cubic departure from c r / 2 and quadratic current correction.
    cubic_errors = []
    current_errors = []
    for r in (0.08, 0.04, 0.02):
        b = beta_star(r)
        exact_delta = b - 0.5 * r
        rhs_delta = r**3 / (2.0 * (1.0 + math.sqrt(1.0 - r * r)) ** 2)
        check(abs(exact_delta - rhs_delta) < 2.0e-13, "M57 beta-star cubic identity")
        cubic_errors.append(abs(exact_delta))

        ratio = math.sinh(2.0 * b) / r
        current_errors.append(abs(ratio - 1.0))
        approx = 1.0 + (5.0 / 12.0) * r * r
        check(abs(ratio - approx) < 1.2e-5, "M57 new R161 current expansion")
    check(cubic_errors[0] / cubic_errors[1] > 7.9 and cubic_errors[1] / cubic_errors[2] > 7.9,
          "M57 beta-star departure is cubic")
    check(current_errors[0] / current_errors[1] > 3.9 and current_errors[1] / current_errors[2] > 3.9,
          "M57 native current correction is quadratic")

    # R196A finite-time tracking witness with time-dependent chirality.
    eps = 2.0e-2
    kappa_bar = 1.0
    smin = 1.0
    mbar_e = 0.2
    tau_p = 0.25
    emin = eps**2 * kappa_bar * smin
    mass_e = eps**2 * mbar_e
    lambda_y = emin / (mass_e * c)
    tau_y = 1.0 / lambda_y
    check(abs(lambda_y - 0.3125) < TOL, "M57 explicit tracking rate")
    check(abs(tau_y - 3.2) < TOL, "M57 explicit tracking time")

    # Weak-tap scaling keeps lambda_Y fixed.
    for eps_test in (0.08, 0.04, 0.02, 0.01):
        e_test = eps_test**2 * kappa_bar * smin
        m_test = eps_test**2 * mbar_e
        lam_test = e_test / (m_test * c)
        check(abs(lam_test - lambda_y) < TOL, "M57 weak-tap finite tracking rate")

    # Direct numerical ODE check against a conservative Gronwall tracking bound.
    r0 = 0.04
    amp = 0.01
    omega = 1.0 / 80.0
    rstar = 0.06
    lstar = 1.0 / (math.sqrt(1.0 - rstar**2) * (1.0 + math.sqrt(1.0 - rstar**2)))
    rdot_sup = amp * omega
    bound_forcing = c * lstar * rdot_sup / lambda_y
    u = c * beta_star(r0) + 0.03
    initial_error = abs(u - c * beta_star(r0))

    def rhs(t: float, uval: float) -> float:
        r = r0 + amp * math.sin(omega * t)
        total = emin
        ep = 0.5 * total * (1.0 + r)
        em = 0.5 * total * (1.0 - r)
        return force(uval / c, ep, em) / mass_e

    dt = 0.01
    t = 0.0
    for _ in range(5000):
        u = rk4_step(u, t, dt, rhs)
        t += dt
    rt = r0 + amp * math.sin(omega * t)
    actual_error = abs(u - c * beta_star(rt))
    gronwall_bound = math.exp(-lambda_y * t) * initial_error + bound_forcing
    check(actual_error <= gronwall_bound * 1.02, "M57 finite-time tracking bound witness")

    # R196B weak-loading and overdamped scaling.
    gamma_bar = 0.1
    mbar_x = 0.1
    gamma_x = eps**4 * gamma_bar
    kbt = gamma_x * d0
    mass_x = eps**6 * mbar_x
    tau_x = mass_x / gamma_x
    load_scale = gamma_x / mass_e
    check(abs(gamma_x - 1.6e-8) < 1.0e-18, "M57 explicit equilibrium-bath friction")
    check(abs(kbt - 6.4e-8) < 1.0e-18, "M57 Einstein temperature scaling")
    check(abs(tau_x - 4.0e-4) < 1.0e-14, "M57 overdamped time scale")
    check(load_scale < 3.0e-4, "M57 tracer loading is weak")

    # Lifson-Jackson periodic suppression and time hierarchy.
    beta_delta_u = solve_beta_delta(gk)
    recovered_gk = 1.0 / np.i0(0.5 * beta_delta_u) ** 2
    check(abs(recovered_gk - gk) < 2.0e-12, "M57 Lifson-Jackson periodic suppression")
    check(abs(beta_delta_u - 11.1025720156) < 2.0e-9, "M57 explicit dimensionless barrier witness")
    signal_time = a * a / nu
    check(tau_x < tau_p < tau_y < signal_time, "M57 separated ballistic/Brownian hierarchy")

    # Signal current drift matching at leading order.
    for r in (0.01, 0.04, 0.08):
        coarse_leading = gk * 0.5 * c * r
        target = 2.0 * nu * r / a
        check(abs(coarse_leading - target) < TOL, "M57 current drift leading matching")

    # R196C ideal R161 traffic positivity with the new affinity A=4 beta_*(r).
    for r in (0.08, 0.04, 0.02, -0.04):
        affinity = 4.0 * beta_star(r)
        qplus = math.exp(0.5 * affinity)
        qminus = math.exp(-0.5 * affinity)
        traffic = qplus + qminus
        current = qplus - qminus
        check(traffic >= abs(current), "M57 R161 traffic positivity")
        check(qplus > 0.0 and qminus > 0.0, "M57 R161 positive fluxes")

    print(f"checks={checks}")
    print(f"lambda_y={lambda_y:.12f} tau_y={tau_y:.12f}")
    print(f"tau_p={tau_p:.12f} tau_x={tau_x:.12f} signal_time={signal_time:.12f}")
    print(f"load_scale={load_scale:.12e}")
    print(f"beta_delta_u={beta_delta_u:.12f}")
    print(f"tracking_error={actual_error:.12e} bound={gronwall_bound:.12e}")


if __name__ == "__main__":
    main()
