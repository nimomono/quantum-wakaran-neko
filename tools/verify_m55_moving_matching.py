#!/usr/bin/env python3
from __future__ import annotations
import numpy as np

J0 = 1.0
TOL = 2.0e-10
checks = 0

def check(condition: bool, message: str) -> None:
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def hermitian_path(n: int) -> np.ndarray:
    h = np.diag(np.linspace(-0.13, 0.19, n)).astype(complex)
    for i, g in enumerate(np.linspace(0.27, 0.43, n - 1)):
        phase = 0.17 * (i + 1)
        value = -g * np.exp(1j * phase)
        h[i, i + 1] = value
        h[i + 1, i] = np.conj(value)
    return h

def current(z: np.ndarray, h: np.ndarray) -> np.ndarray:
    n = len(z)
    out = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            out[i, j] = 2.0 / J0 * np.imag(np.conj(z[j]) * h[j, i] * z[i])
    return out

def moving_rates(z: np.ndarray, h: np.ndarray, delta: float, q: np.ndarray):
    s = float(np.vdot(z, z).real)
    r = np.abs(z) ** 2 + delta * q * s
    j = current(z, h)
    n = len(z)
    t = np.zeros((n, n), dtype=float)
    kp = np.zeros((n, n), dtype=float)
    km = np.zeros((n, n), dtype=float)
    for i in range(n):
        for k in range(n):
            if i == k or abs(h[i, k]) == 0.0:
                continue
            t[i, k] = abs(h[i, k]) / J0 * (r[i] + r[k])
            kp[i, k] = (t[i, k] + j[i, k]) / (2.0 * r[i])
            km[i, k] = (t[i, k] - j[i, k]) / (2.0 * r[i])
    p = r / ((1.0 + delta) * s)
    return p, r, j, t, kp, km

def latched_rates(
    z: np.ndarray,
    h: np.ndarray,
    delta: float,
    q: np.ndarray,
    sref: float,
):
    r = np.abs(z) ** 2 + delta * q * sref
    j = current(z, h)
    n = len(z)
    t = np.zeros((n, n), dtype=float)
    kp = np.zeros((n, n), dtype=float)
    for i in range(n):
        for k in range(n):
            if i == k or abs(h[i, k]) == 0.0:
                continue
            t[i, k] = abs(h[i, k]) / J0 * (r[i] + r[k])
            kp[i, k] = (t[i, k] + j[i, k]) / (2.0 * r[i])
    return r, j, t, kp

def generator(rates: np.ndarray) -> np.ndarray:
    g = rates.copy()
    np.fill_diagonal(g, 0.0)
    g[np.diag_indices_from(g)] = -np.sum(g, axis=1)
    return g

def spectral_derivative(values: np.ndarray, order: int = 1) -> np.ndarray:
    n = len(values)
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.fft.ifft((1j * k) ** order * np.fft.fft(values)).real

def main() -> None:
    rng = np.random.default_rng(20260906)
    n = 7
    h = hermitian_path(n)
    z = rng.normal(size=n) + 1j * rng.normal(size=n)
    z /= np.linalg.norm(z)
    delta = 0.07
    q = np.linspace(1.0, 2.0, n)
    q /= q.sum()

    p, _, j, t, kp, km = moving_rates(z, h, delta, q)
    zdot = -1j * h @ z / J0
    pdot = 2.0 * np.real(np.conj(z) * zdot) / (1.0 + delta)
    master = p @ generator(kp)
    check(np.max(np.abs(j + j.T)) < TOL, "R183 current antisymmetry")
    check(np.min(t - np.abs(j)) > -TOL, "R183 traffic positivity")
    check(np.min(kp) > -TOL and np.min(km) > -TOL, "R183 rate positivity")
    check(np.max(np.abs(master - pdot)) < TOL, "R183 moving matching")

    bayes = np.zeros_like(km)
    for i in range(n):
        for k in range(n):
            if i != k:
                bayes[i, k] = p[k] * kp[k, i] / p[i]
    check(np.max(np.abs(bayes - km)) < TOL, "R185 same-measure time reversal")
    p2, *_ = moving_rates(2.3 * np.exp(0.7j) * z, h, delta, q)
    check(np.max(np.abs(p2 - p)) < TOL, "rank-one radial invariance")

    h_real = np.real(h)
    y = rng.normal(size=n) + 1j * rng.normal(size=n)
    y /= np.linalg.norm(y)
    Delta = 0.08
    eps_car = 2.0e-5
    direction = rng.normal(size=n) + 1j * rng.normal(size=n)
    direction /= np.linalg.norm(direction)
    x = y + eps_car / (1.0 - Delta) * direction
    qmin = float(np.min(q))
    h1 = max(float(np.sum(np.abs(h_real[i]))) - abs(h_real[i, i]) for i in range(n))
    Ldelta = h1 / (J0 * (1.0 - Delta) ** 2) * (
        np.sqrt(2.0) * (1.0 + np.sqrt(1.0 + Delta**2)) / (delta * qmin)
        + 2.0 * (1.0 + delta) / (delta**2 * qmin**2)
    )
    kx = latched_rates(x, h_real, delta, q, 1.0)[3]
    ky = moving_rates(y, h_real, delta, q)[4]
    kylat = latched_rates(y, h_real, delta, q, 1.0)[3]
    check(np.max(np.abs(kylat - ky)) < TOL, "R184 ideal latch equals M55")
    kinst = moving_rates(x, h_real, delta, q)[4]
    check(
        np.max(np.abs(kx - kinst)) > 1.0e-10,
        "R184 latch differs from instantaneous M37 action",
    )
    rowdiff = np.max(np.sum(np.abs(kx - ky), axis=1))
    check(
        rowdiff <= Ldelta * eps_car * (1.0 + 1.0e-9),
        "R184 latched Lipschitz bound",
    )

    N = 64
    a = 2.0 * np.pi / N
    nu = 0.31
    hring = np.zeros((N, N), dtype=complex)
    hop = -J0 * nu / a**2
    for i in range(N):
        ip = (i + 1) % N
        hring[i, ip] = hop
        hring[ip, i] = hop
    xx = a * np.arange(N)
    rho = 1.0 + 0.17 * np.cos(xx)
    phase = 0.23 * np.sin(xx)
    psi = np.sqrt(rho) * np.exp(1j * phase / J0)
    psi /= np.linalg.norm(psi)
    qu = np.full(N, 1.0 / N)
    pp, _, jj, _, kpf, kmf = moving_rates(psi, hring, delta, qu)
    spsi = float(np.vdot(psi, psi).real)
    dplus = np.zeros(N)
    dminus = np.zeros(N)
    vdisc = np.zeros(N)
    udisc = np.zeros(N)
    for i in range(N):
        ip = (i + 1) % N
        im = (i - 1) % N
        dplus[i] = a * kpf[i, ip] - a * kpf[i, im]
        dminus[i] = -a * kmf[i, ip] + a * kmf[i, im]
        jp = jj[i, ip] / ((1.0 + delta) * spsi)
        jm = jj[im, i] / ((1.0 + delta) * spsi)
        vdisc[i] = a * (jp + jm) / (2.0 * pp[i])
        udisc[i] = nu * (pp[ip] - pp[im]) / (2.0 * a * pp[i])
    check(np.max(np.abs(dplus - (vdisc + udisc))) < 5.0e-9, "R185 D+ decomposition")
    check(np.max(np.abs(dminus - (vdisc - udisc))) < 5.0e-9, "R185 D- decomposition")

    Nf = 1024
    xg = 2.0 * np.pi * np.arange(Nf) / Nf
    rh = 1.0 + 0.21 * np.cos(xg)
    u = nu * spectral_derivative(np.log(rh), 1)
    ux = spectral_derivative(u, 1)
    uxx = spectral_derivative(u, 2)
    force = u * ux + nu * uxx
    q0 = 1.0 / (2.0 * np.pi)
    A = rh / (rh + delta * q0)
    eps = 1.0 - A
    ud = A * u
    ad = -ud * spectral_derivative(ud, 1) - nu * spectral_derivative(ud, 2)
    residual = ad + force
    predicted = eps * (force - 2.0 * A * u * ux - (A * eps / nu) * u**3)
    check(np.max(np.abs(residual - predicted)) < 2.0e-8, "R185 delta residual")

    # General nonzero-current check of the full R_delta identity.
    rhg = 1.0 + 0.21 * np.cos(xg) + 0.07 * np.cos(2.0 * xg)
    vg = 0.18 * np.cos(xg) - 0.09 * np.sin(2.0 * xg)
    vtg = 0.05 * np.sin(xg) + 0.03 * np.cos(3.0 * xg)
    ug = nu * spectral_derivative(np.log(rhg), 1)
    vgx = spectral_derivative(vg, 1)
    ugx = spectral_derivative(ug, 1)
    ugxx = spectral_derivative(ug, 2)
    forceg = -(vtg + vg * vgx - ug * ugx - nu * ugxx)
    rhot = -spectral_derivative(rhg * vg, 1)
    Ag = rhg / (rhg + delta * q0)
    epsg = 1.0 - Ag
    Agt = delta * q0 / (rhg + delta * q0) ** 2 * rhot
    vdg = Ag * vg
    udg = Ag * ug
    vdgt = Agt * vg + Ag * vtg
    adg = (
        vdgt
        + vdg * spectral_derivative(vdg, 1)
        - udg * spectral_derivative(udg, 1)
        - nu * spectral_derivative(udg, 2)
    )
    residualg = adg + forceg
    predictedg = epsg * (
        forceg
        - 2.0 * Ag * (vg * vgx + ug * ugx)
        - (Ag * epsg / nu) * ug * (vg**2 + ug**2)
    )
    check(
        np.max(np.abs(residualg - predictedg)) < 8.0e-8,
        "R185 general-current delta residual",
    )

    residuals = []
    for d in (0.08, 0.04, 0.02):
        AA = rh / (rh + d * q0)
        udd = AA * u
        rr = -udd * spectral_derivative(udd, 1) - nu * spectral_derivative(udd, 2) + force
        residuals.append(float(np.max(np.abs(rr))))
    check(residuals[0] > residuals[1] > residuals[2], "R185 O(delta) monotonicity")
    check(residuals[0] / residuals[1] > 1.7 and residuals[1] / residuals[2] > 1.7, "R185 O(delta) scaling")

    print(f"checks={checks}")
    print(f"moving_master_residual={np.max(np.abs(master-pdot)):.3e}")
    print(f"time_reverse_residual={np.max(np.abs(bayes-km)):.3e}")
    print(f"r184_latched_rowdiff={rowdiff:.6e} bound={Ldelta*eps_car:.6e}")
    print(f"delta_residual_identity={np.max(np.abs(residual-predicted)):.3e}")
    print(
        "general_current_residual_identity="
        f"{np.max(np.abs(residualg-predictedg)):.3e}"
    )
    print("delta_residuals=" + ",".join(f"{v:.6e}" for v in residuals))

if __name__ == "__main__":
    main()