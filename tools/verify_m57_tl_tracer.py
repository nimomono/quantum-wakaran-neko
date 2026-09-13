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


def path_laplacian(n: int) -> np.ndarray:
    out = np.zeros((n, n), dtype=float)
    for i in range(n - 1):
        out[i, i] += 1.0
        out[i + 1, i + 1] += 1.0
        out[i, i + 1] -= 1.0
        out[i + 1, i] -= 1.0
    return out


def lyapunov_solution(a: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    op = np.kron(np.eye(n), a.T) + np.kron(a.T, np.eye(n))
    rhs = -np.eye(n).reshape(-1, order="F")
    p = np.linalg.solve(op, rhs).reshape((n, n), order="F")
    return 0.5 * (p + p.T)


def solve_beta_delta(gk: float) -> float:
    lo, hi = 0.0, 30.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        value = 1.0 / np.i0(0.5 * mid) ** 2
        if value > gk:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    rng = np.random.default_rng(20260913)

    # R195A chiral identities.
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

    # Explicit M57 dimensionless witness.
    a = 1.0
    n = 4
    inductance = 1.0 / 16.0
    capacitance = 1.0 / 16.0
    pin_inductance = 1.0
    boundary_resistance = 0.66834
    drude_cutoff = 8.0
    beta_anh = 0.05
    phi_star = 0.5
    gk = 5.0e-4
    nu = 2.0e-3

    omega0 = 1.0 / math.sqrt(inductance * capacitance)
    wave_speed = a / math.sqrt(inductance * capacitance)
    delta = path_laplacian(n)
    stiffness = np.eye(n) / pin_inductance + delta / inductance
    gamma_b = 1.0 / (boundary_resistance * capacitance)
    damping = np.zeros((n, n), dtype=float)
    damping[0, 0] = gamma_b
    damping[-1, -1] = gamma_b
    drift = np.block(
        [
            [np.zeros((n, n)), np.eye(n) / capacitance],
            [-stiffness, -damping],
        ]
    )

    eig = np.linalg.eigvals(drift)
    harmonic_gap = -float(np.max(np.real(eig)))
    check(harmonic_gap > 0.0, "M57 harmonic drift is Hurwitz")
    check(abs(harmonic_gap - 0.963010700731) < 5.0e-10, "M57 harmonic witness gap")

    drift_bar = drift / omega0
    p = lyapunov_solution(drift_bar)
    residual = np.max(np.abs(drift_bar.T @ p + p @ drift_bar + np.eye(2 * n)))
    check(residual < 2.0e-12, "M57 Lyapunov residual")
    check(np.min(np.linalg.eigvalsh(p)) > 0.0, "M57 Lyapunov matrix positive")

    pnorm = float(np.linalg.norm(p, 2))
    eta_nl = 3.0 * abs(beta_anh) * inductance * phi_star**2
    delta_anh = 4.0 * eta_nl
    margin = 1.0 - 2.0 * pnorm * delta_anh
    check(eta_nl < 0.01, "M57 weak anharmonic safe shell")
    check(margin > 0.0, "M57 finite nonlinear mixing margin")

    lambda_mix = omega0 * margin / (2.0 * pnorm)
    lambda_star = min(lambda_mix, drude_cutoff)
    tau_corr = 1.0 / lambda_star
    tau_mix_1pct = math.log(100.0) / lambda_mix
    check(lambda_mix > 0.15, "M57 conservative mixing rate")
    check(tau_corr < 7.0, "M57 finite force-correlation bound")
    check(tau_mix_1pct < 30.0, "M57 finite one-percent mixing time")

    # FDT/Kramers simultaneous matching.
    bare_diffusion = a * wave_speed / 4.0
    hopping_diffusion = gk * bare_diffusion
    check(abs(gk * wave_speed - 4.0 * nu / a) < TOL, "M57 gK-c-nu matching")
    check(abs(hopping_diffusion - nu) < TOL, "M57 hopping diffusion equals nu")

    beta_delta_u = solve_beta_delta(gk)
    recovered_gk = 1.0 / np.i0(0.5 * beta_delta_u) ** 2
    check(abs(recovered_gk - gk) < 2.0e-12, "M57 Lifson-Jackson periodic suppression")
    check(abs(beta_delta_u - 11.1025720156) < 2.0e-9, "M57 explicit barrier witness")

    edge_rate = nu / a**2
    residence_time = 1.0 / (2.0 * edge_rate)
    signal_time = a**2 / nu
    propagation_time = n * a / wave_speed
    drude_time = 1.0 / drude_cutoff
    check(drude_time < propagation_time < tau_corr, "M57 fast microscopic hierarchy")
    check(tau_corr < tau_mix_1pct < residence_time < signal_time, "M57 separated slow hierarchy")

    # Current drift uses the same matching as diffusion.
    for chirality in (0.01, 0.04, 0.08):
        bare_drift = 0.5 * wave_speed * chirality
        coarse_drift = gk * bare_drift
        target_drift = 2.0 * nu * chirality / a
        check(abs(coarse_drift - target_drift) < TOL, "M57 current drift matching")

    # Exact R161-form Kramers flux and O(a^2) native current correction.
    errors = []
    for r in (0.08, 0.04, 0.02):
        ratio = math.sinh(r) / r
        errors.append(abs(ratio - 1.0))
        traffic = 2.0 * math.cosh(r)
        current = 2.0 * math.sinh(r)
        qplus = 0.5 * (traffic + current)
        qminus = 0.5 * (traffic - current)
        check(abs(qplus - math.exp(r)) < TOL, "M57 R161 forward flux")
        check(abs(qminus - math.exp(-r)) < TOL, "M57 R161 reverse flux")
        check(traffic >= abs(current), "M57 R161 traffic positivity")
    check(errors[0] > errors[1] > errors[2], "M57 current correction monotonicity")
    check(errors[0] / errors[1] > 3.9 and errors[1] / errors[2] > 3.9, "M57 current correction is quadratic")

    print(f"checks={checks}")
    print(f"harmonic_gap={harmonic_gap:.12f}")
    print(f"lyapunov_norm={pnorm:.12f} margin={margin:.12f}")
    print(f"lambda_mix={lambda_mix:.12f}")
    print(f"tau_corr_bound={tau_corr:.12f}")
    print(f"tau_mix_1pct={tau_mix_1pct:.12f}")
    print(f"beta_delta_u={beta_delta_u:.12f}")
    print(f"residence_time={residence_time:.12f} signal_time={signal_time:.12f}")


if __name__ == "__main__":
    main()
