#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


TOL = 1.0e-11


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def hermitian_exponential(generator: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(generator)
    return vectors @ np.diag(np.exp(-1j * values)) @ vectors.conj().T


def spectral_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False)[0])


def check_rank_one_involution_and_running_pulse() -> None:
    p_l = np.diag([1.0, 0.0]).astype(complex)
    p_r = np.diag([0.0, 1.0]).astype(complex)
    f_l = np.block([[p_l, p_r], [p_r, -p_l]])
    identity = np.eye(4, dtype=complex)

    check(np.max(np.abs(f_l.conj().T @ f_l - identity)) < TOL, "R189B unitary involution")
    check(np.max(np.abs(f_l @ f_l - identity)) < TOL, "R189B square identity")

    tau_f = 0.23
    h_f = math.pi / (2.0 * tau_f) * (identity - f_l)
    u_f = hermitian_exponential(h_f * tau_f)
    check(np.max(np.abs(u_f - f_l)) < 2.0e-11, "R189B finite Hamiltonian pulse")

    omega = 0.07
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    h_r = -0.5 * omega * sigma_x
    h_ext = np.block([
        [h_r, np.zeros((2, 2), dtype=complex)],
        [np.zeros((2, 2), dtype=complex), np.zeros((2, 2), dtype=complex)],
    ])
    u_run = hermitian_exponential((h_ext + h_f) * tau_f)
    u_r = hermitian_exponential(h_ext * tau_f)
    error = spectral_norm(u_run - f_l @ u_r)
    check(error <= omega * tau_f + 5.0e-12, "R189B running-Rabi Duhamel bound")


def check_symmetric_capacity_window() -> None:
    omega = 0.13
    width = 0.41
    times = np.array([-width, 0.0, width])
    weights = np.array([0.25, 0.50, 0.25])
    d0 = 0.37
    y0 = -0.48

    d_values = d0 * np.cos(omega * times) + y0 * np.sin(omega * times)
    d_bar = float(weights @ d_values)
    c_chi = float(weights @ np.cos(omega * times))
    check(abs(d_bar - c_chi * d0) < TOL, "R189A even-window odd term cancellation")

    mu2 = float(weights @ (times * times))
    branch_error = abs(d_bar - d0) / 2.0
    bound = omega * omega * mu2 / 4.0
    check(branch_error <= bound + TOL, "R189A quadratic finite-window bound")


def check_two_step_zeno_witness() -> None:
    a = math.cos(math.pi / 8.0) ** 2
    q = math.sin(math.pi / 8.0) ** 2
    histories = {
        "++": a * a,
        "+-": a * q,
        "-+": q * q,
        "--": q * a,
    }

    check(abs(sum(histories.values()) - 1.0) < TOL, "R189C full history normalization")
    check(histories["-+"] > 0.0, "R189C positive reflip history")
    check(abs(histories["+-"] - 0.125) < TOL, "R189C +- weight")
    check(abs(histories["--"] - 0.125) < TOL, "R189C -- weight")

    measured_survival = histories["++"] + histories["-+"]
    free_survival = math.cos(math.pi / 4.0) ** 2
    gap = measured_survival - free_survival
    check(abs(measured_survival - 0.75) < TOL, "R189C measured survival")
    check(abs(free_survival - 0.50) < TOL, "R189C free survival")
    check(abs(gap - 0.25) < TOL, "R189C finite Zeno margin")
    check(q > 0.14 and q > 0.10, "R189C fixed safe probability floor")


def main() -> None:
    check_rank_one_involution_and_running_pulse()
    check_symmetric_capacity_window()
    check_two_step_zeno_witness()
    print("R189A--R189C live W2 Zeno checks: OK")


if __name__ == "__main__":
    main()
