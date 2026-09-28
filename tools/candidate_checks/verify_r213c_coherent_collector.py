#!/usr/bin/env python3
from __future__ import annotations

import numpy as np

from verify_r213b_phase_tagged_gates import OMEGA, apply_statevector, path_terms


def sqrt_psd(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2)
    vals = np.maximum(vals, 0.0)
    return (vecs * np.sqrt(vals)) @ vecs.conj().T


def collector_matrix(n: int, terms: list[tuple[int, int]]) -> np.ndarray:
    m = len(terms)
    b = np.zeros((2**n, m), dtype=complex)
    for r, (q, _p) in enumerate(terms):
        b[q, r] = 1 / np.sqrt(m)
    return b


def main() -> None:
    rng = np.random.default_rng(21303)
    worst_unitarity = 0.0
    worst_amplitude = 0.0

    for n in (2, 3):
        gate_pool = [("H", j) for j in range(n)] + [("T", j) for j in range(n)]
        gate_pool += [("CX", c, t) for c in range(n) for t in range(n) if c != t]
        for _ in range(36):
            circuit = [
                gate_pool[int(rng.integers(len(gate_pool)))]
                for _ in range(int(rng.integers(1, 10)))
            ]
            terms = path_terms(n, circuit)
            m = len(terms)
            b = collector_matrix(n, terms)

            left = np.eye(2**n) - b @ b.conj().T
            right = np.eye(m) - b.conj().T @ b
            assert np.min(np.linalg.eigvalsh((left + left.conj().T) / 2)) > -1e-10
            assert np.min(np.linalg.eigvalsh((right + right.conj().T) / 2)) > -1e-10

            dl = sqrt_psd(left)
            dm = sqrt_psd(right)
            u = np.block([[b, dl], [dm, -b.conj().T]])
            defect = float(np.linalg.norm(u.conj().T @ u - np.eye(u.shape[0]), 2))
            worst_unitarity = max(worst_unitarity, defect)
            assert defect < 2e-10

            leaf = np.array([OMEGA**p for _q, p in terms], dtype=complex)
            collector = b @ leaf

            state = np.zeros(2**n, dtype=complex)
            state[0] = 1
            for gate in circuit:
                state = apply_statevector(state, gate, n)

            err = float(np.max(np.abs(collector - state)))
            worst_amplitude = max(worst_amplitude, err)
            assert err < 2e-12
            assert abs(np.sum(np.abs(collector) ** 2) - 1.0) < 2e-12

    print(
        "r213c_ok "
        f"max_unitarity_defect={worst_unitarity:.3e} "
        f"max_collector_error={worst_amplitude:.3e}"
    )


if __name__ == "__main__":
    main()
