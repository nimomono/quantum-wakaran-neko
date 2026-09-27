#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np

BARRIER = 16.0
TAU_CUT = 0.07
ELL = 0.01
D_READ = 0.40
L_COMMIT = 0.78
T_DEC = 0.22
DELTA0 = 5.0e-4

XMAX = 1.60
H = 0.004
DT = 5.0e-4

EPS_X_LOOSE = 1.0e-3
EPS_X_STRONG = 1.0e-4

MAX_COLLAR = 4.8e-3
MAX_LAUNCH = 1.7e-3
MAX_SURVIVAL = 2.0e-5
MAX_RETURN = 5.0e-4
MAX_THRESHOLD_DENSITY = 1.0e-4
MAX_COARSE_STRONG = 8.0e-4
MAX_TOTAL_STRONG = 8.0e-3
MAX_TOTAL_LOOSE = 1.3e-2

def w0(x: np.ndarray | float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return BARRIER * (x * x - 1.0) ** 2

def w0_prime(x: np.ndarray | float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return 4.0 * BARRIER * x * (x * x - 1.0)

def w0_second(x: np.ndarray | float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return 4.0 * BARRIER * (3.0 * x * x - 1.0)

def smootherstep01(z: np.ndarray | float) -> np.ndarray:
    z = np.asarray(z, dtype=float)
    out = np.zeros_like(z)
    out[z >= 1.0] = 1.0
    mask = (z > 0.0) & (z < 1.0)
    u = z[mask]
    out[mask] = 6.0 * u**5 - 15.0 * u**4 + 10.0 * u**3
    return out

def smootherstep01_prime(z: np.ndarray | float) -> np.ndarray:
    z = np.asarray(z, dtype=float)
    out = np.zeros_like(z)
    mask = (z > 0.0) & (z < 1.0)
    u = z[mask]
    out[mask] = 30.0 * u**2 * (u - 1.0) ** 2
    return out

def smootherstep01_second(z: np.ndarray | float) -> np.ndarray:
    z = np.asarray(z, dtype=float)
    out = np.zeros_like(z)
    mask = (z > 0.0) & (z < 1.0)
    u = z[mask]
    out[mask] = 60.0 * u * (2.0 * u * u - 3.0 * u + 1.0)
    return out

def chi(x: np.ndarray | float) -> np.ndarray:
    return smootherstep01((np.asarray(x, dtype=float) + ELL) / (2.0 * ELL))

def chi_prime(x: np.ndarray | float) -> np.ndarray:
    z = (np.asarray(x, dtype=float) + ELL) / (2.0 * ELL)
    return smootherstep01_prime(z) / (2.0 * ELL)

def chi_second(x: np.ndarray | float) -> np.ndarray:
    z = (np.asarray(x, dtype=float) + ELL) / (2.0 * ELL)
    return smootherstep01_second(z) / (2.0 * ELL) ** 2

def free_energy(x: np.ndarray | float, p_plus: float) -> np.ndarray:
    if not (0.0 < p_plus < 1.0):
        raise ValueError("p_plus must lie strictly between 0 and 1")
    p_minus = 1.0 - p_plus
    logw = (
        (1.0 - chi(x)) * math.log(p_minus)
        + chi(x) * math.log(p_plus)
    )
    return w0(x) - logw

def free_energy_prime(x: np.ndarray | float, p_plus: float) -> np.ndarray:
    log_ratio = math.log(p_plus / (1.0 - p_plus))
    return w0_prime(x) - log_ratio * chi_prime(x)

def free_energy_second(x: np.ndarray | float, p_plus: float) -> np.ndarray:
    log_ratio = math.log(p_plus / (1.0 - p_plus))
    return w0_second(x) - log_ratio * chi_second(x)

def bisect_root(fn, a: float, b: float, iterations: int = 80) -> float:
    fa = float(fn(a))
    fb = float(fn(b))
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    if fa * fb > 0.0:
        raise AssertionError("bisection interval does not bracket a root")
    for _ in range(iterations):
        m = 0.5 * (a + b)
        fm = float(fn(m))
        if fm == 0.0:
            return m
        if fa * fm <= 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)

def central_roots(p_plus: float) -> list[float]:
    grid = np.linspace(-ELL, ELL, 20001)
    vals = free_energy_prime(grid, p_plus)
    roots: list[float] = []
    for i in range(grid.size - 1):
        left = float(vals[i])
        right = float(vals[i + 1])
        if abs(left) < 1.0e-12:
            r = float(grid[i])
            if not roots or abs(r - roots[-1]) > 1.0e-8:
                roots.append(r)
        if left * right < 0.0:
            r = bisect_root(
                lambda x: free_energy_prime(x, p_plus),
                float(grid[i]),
                float(grid[i + 1]),
            )
            if not roots or abs(r - roots[-1]) > 1.0e-8:
                roots.append(r)
    if abs(float(vals[-1])) < 1.0e-12:
        r = float(grid[-1])
        if not roots or abs(r - roots[-1]) > 1.0e-8:
            roots.append(r)
    return roots

def committor_and_launch(p_plus: float) -> tuple[float, float]:
    x = np.linspace(-L_COMMIT, L_COMMIT, 40001)
    scale_density = np.exp(free_energy(x, p_plus))
    denominator = float(np.trapezoid(scale_density, x))
    mid = x.size // 2
    q_plus = float(
        np.trapezoid(scale_density[: mid + 1], x[: mid + 1]) / denominator
    )
    launch_x = np.linspace(-DELTA0, DELTA0, 41)
    qprime = np.exp(free_energy(launch_x, p_plus)) / denominator
    return q_plus, float(np.max(qprime))

def generator_bands(
    x: np.ndarray, p_plus: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h = float(x[1] - x[0])
    f = free_energy(x, p_plus)
    upper = np.exp(-0.5 * (f[1:] - f[:-1])) / (h * h)
    lower = np.exp(-0.5 * (f[:-1] - f[1:])) / (h * h)
    diag = np.zeros(x.size)
    diag[:-1] -= upper
    diag[1:] -= lower
    return lower, diag, upper

def sub_bands(
    lower: np.ndarray,
    diag: np.ndarray,
    upper: np.ndarray,
    start: int,
    stop: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if stop <= start:
        raise ValueError("empty submatrix")
    return (
        lower[start : stop - 1].copy(),
        diag[start:stop].copy(),
        upper[start : stop - 1].copy(),
    )

def factor_tridiagonal(
    lower: np.ndarray, diag: np.ndarray, upper: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = diag.size
    if n == 0:
        raise ValueError("empty matrix")
    reduced_upper = np.empty(max(n - 1, 0))
    pivots = np.empty(n)
    pivots[0] = diag[0]
    if n > 1:
        reduced_upper[0] = upper[0] / pivots[0]
        for i in range(1, n - 1):
            pivots[i] = diag[i] - lower[i - 1] * reduced_upper[i - 1]
            reduced_upper[i] = upper[i] / pivots[i]
        pivots[-1] = diag[-1] - lower[-1] * reduced_upper[-1]
    if np.min(np.abs(pivots)) < 1.0e-14:
        raise AssertionError("near-singular tridiagonal solve")
    return lower.copy(), pivots, reduced_upper

def solve_factored(
    fact: tuple[np.ndarray, np.ndarray, np.ndarray], rhs: np.ndarray
) -> np.ndarray:
    lower, pivots, reduced_upper = fact
    n = pivots.size
    y = np.empty(n)
    y[0] = rhs[0] / pivots[0]
    for i in range(1, n):
        y[i] = (rhs[i] - lower[i - 1] * y[i - 1]) / pivots[i]
    out = np.empty(n)
    out[-1] = y[-1]
    for i in range(n - 2, -1, -1):
        out[i] = y[i] - reduced_upper[i] * out[i + 1]
    return out

def implicit_evolve(
    lower: np.ndarray,
    diag: np.ndarray,
    upper: np.ndarray,
    initial: np.ndarray,
    total_time: float,
    dt: float,
) -> np.ndarray:
    steps = int(round(total_time / dt))
    if steps < 1:
        raise ValueError("at least one time step is required")
    dt_eff = total_time / steps
    fact = factor_tridiagonal(
        -dt_eff * lower,
        1.0 - dt_eff * diag,
        -dt_eff * upper,
    )
    state = np.asarray(initial, dtype=float).copy()
    for _ in range(steps):
        state = solve_factored(fact, state)
    return state

def survival_probability(p_plus: float) -> float:
    n = int(round(2.0 * L_COMMIT / H)) + 1
    x = np.linspace(-L_COMMIT, L_COMMIT, n)
    lower, diag, upper = generator_bands(x, p_plus)
    sl, sd, su = sub_bands(lower, diag, upper, 1, n - 1)
    surv = implicit_evolve(sl, sd, su, np.ones(n - 2), T_DEC, DT)
    return float(np.interp(0.0, x[1:-1], surv))

def return_probability_right() -> float:
    n = int(round((XMAX - D_READ) / H)) + 1
    x = np.linspace(D_READ, XMAX, n)
    lower, diag, upper = generator_bands(x, 0.5)
    sl, sd, su = sub_bands(lower, diag, upper, 1, n)
    surv = implicit_evolve(sl, sd, su, np.ones(n - 1), T_DEC, DT)
    return float(1.0 - np.interp(L_COMMIT, x[1:], surv))

def return_probability_left() -> float:
    n = int(round((XMAX - D_READ) / H)) + 1
    x = np.linspace(-XMAX, -D_READ, n)
    lower, diag, upper = generator_bands(x, 0.5)
    sl, sd, su = sub_bands(lower, diag, upper, 0, n - 1)
    surv = implicit_evolve(sl, sd, su, np.ones(n - 1), T_DEC, DT)
    return float(1.0 - np.interp(-L_COMMIT, x[:-1], surv))

def terminal_distribution(p_plus: float) -> tuple[np.ndarray, np.ndarray]:
    n = int(round(2.0 * XMAX / H)) + 1
    x = np.linspace(-XMAX, XMAX, n)
    lower, diag, upper = generator_bands(x, p_plus)
    mass = np.zeros(n)
    mass[int(np.argmin(np.abs(x)))] = 1.0
    mass_t = implicit_evolve(
        upper.copy(), diag, lower.copy(), mass, T_DEC, DT
    )
    return x, mass_t

def coarse_graining_bound(
    terminal: dict[float, tuple[np.ndarray, np.ndarray]],
    epsilon_x: float,
) -> tuple[float, float, float]:
    best = (math.inf, math.nan, math.nan)
    for delta in np.linspace(0.02, 0.20, 91):
        omega = 0.0
        for x, mass in terminal.values():
            mask = np.abs(np.abs(x) - D_READ) <= delta + 1.0e-14
            omega = max(omega, float(np.sum(mass[mask])))
        value = epsilon_x / float(delta) + omega
        if value < best[0]:
            best = (value, float(delta), omega)
    return best

def main() -> None:
    structure_scan = np.linspace(TAU_CUT, 1.0 - TAU_CUT, 17)
    max_abs_saddle = 0.0
    least_negative_saddle_curvature = -math.inf
    for p_plus in structure_scan:
        roots = central_roots(float(p_plus))
        assert len(roots) == 1, (p_plus, roots)
        saddle = roots[0]
        saddle_curvature = float(free_energy_second(saddle, float(p_plus)))
        assert abs(saddle) < ELL
        assert saddle_curvature < -50.0
        assert abs(float(free_energy_prime(-1.0, float(p_plus)))) < 1.0e-10
        assert abs(float(free_energy_prime(+1.0, float(p_plus)))) < 1.0e-10
        assert float(free_energy_second(-1.0, float(p_plus))) > 100.0
        assert float(free_energy_second(+1.0, float(p_plus))) > 100.0
        max_abs_saddle = max(max_abs_saddle, abs(saddle))
        least_negative_saddle_curvature = max(
            least_negative_saddle_curvature, saddle_curvature
        )

    p_scan = np.linspace(TAU_CUT, 1.0 - TAU_CUT, 87)
    max_collar = 0.0
    max_launch_lipschitz = 0.0
    worst_collar_p = math.nan
    for p_plus in p_scan:
        q_plus, launch_lipschitz = committor_and_launch(float(p_plus))
        err = abs(q_plus - float(p_plus))
        if err > max_collar:
            max_collar = err
            worst_collar_p = float(p_plus)
        max_launch_lipschitz = max(max_launch_lipschitz, launch_lipschitz)
    launch_error = max_launch_lipschitz * DELTA0
    assert max_collar < MAX_COLLAR, max_collar
    assert launch_error < MAX_LAUNCH, launch_error

    dynamic_scan = np.linspace(TAU_CUT, 1.0 - TAU_CUT, 9)
    survival = {
        float(p): survival_probability(float(p)) for p in dynamic_scan
    }
    max_survival = max(survival.values())
    assert max_survival < MAX_SURVIVAL, max_survival

    return_right = return_probability_right()
    return_left = return_probability_left()
    max_return = max(return_right, return_left)
    assert max_return < MAX_RETURN, max_return

    terminal = {
        float(p): terminal_distribution(float(p)) for p in dynamic_scan
    }
    max_mass_error = 0.0
    max_threshold_density = 0.0
    density_window = 0.01
    for x, mass in terminal.values():
        max_mass_error = max(
            max_mass_error, abs(float(np.sum(mass)) - 1.0)
        )
        density = mass / H
        mask = np.abs(np.abs(x) - D_READ) <= density_window + 1.0e-14
        max_threshold_density = max(
            max_threshold_density, float(np.max(density[mask]))
        )
    assert max_mass_error < 2.0e-9, max_mass_error
    assert max_threshold_density < MAX_THRESHOLD_DENSITY, max_threshold_density

    coarse_strong, delta_strong, omega_strong = coarse_graining_bound(
        terminal, EPS_X_STRONG
    )
    coarse_loose, delta_loose, omega_loose = coarse_graining_bound(
        terminal, EPS_X_LOOSE
    )
    assert coarse_strong < MAX_COARSE_STRONG, coarse_strong

    total_strong = (
        max_collar + launch_error + max_survival + max_return + coarse_strong
    )
    total_loose = (
        max_collar + launch_error + max_survival + max_return + coarse_loose
    )
    assert total_strong < MAX_TOTAL_STRONG, total_strong
    assert total_loose < MAX_TOTAL_LOOSE, total_loose

    print("R211B / M67 Q1 first-passage numerical witness: OK")
    print(f"  W0(X) = {BARRIER:g} (X^2 - 1)^2")
    print(
        "  parameters:"
        f" tau_cut={TAU_CUT:g}, ell={ELL:g}, d={D_READ:g},"
        f" L={L_COMMIT:g}, T={T_DEC:g}, delta0={DELTA0:g}"
    )
    print(
        f"  topology: max |central saddle|={max_abs_saddle:.6g},"
        f" least-negative saddle curvature={least_negative_saddle_curvature:.6g}"
    )
    print(
        f"  collar: max={max_collar:.6g}"
        f" at p_plus~{worst_collar_p:.3f}"
    )
    print(
        f"  launch: L_q={max_launch_lipschitz:.6g},"
        f" error<={launch_error:.6g}"
    )
    print(f"  survival: max={max_survival:.6g}")
    print(
        f"  return: right={return_right:.6g},"
        f" left={return_left:.6g}"
    )
    print(
        f"  threshold density:"
        f" max rho_T near +/-d={max_threshold_density:.6g}"
    )
    print(
        f"  coarse transfer (epsilon_X={EPS_X_STRONG:g}):"
        f" {coarse_strong:.6g}"
        f" [delta={delta_strong:.3f}, omega={omega_strong:.6g}]"
    )
    print(
        f"  coarse transfer (epsilon_X={EPS_X_LOOSE:g}):"
        f" {coarse_loose:.6g}"
        f" [delta={delta_loose:.3f}, omega={omega_loose:.6g}]"
    )
    print(f"  total strong bound: {total_strong:.6g}")
    print(f"  total loose bound:  {total_loose:.6g}")

if __name__ == "__main__":
    main()
