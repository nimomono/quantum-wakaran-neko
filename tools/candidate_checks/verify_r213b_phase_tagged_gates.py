#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


OMEGA = np.exp(1j * np.pi / 4)


def apply_statevector(state: np.ndarray, gate: tuple, n: int) -> np.ndarray:
    out = state.copy()
    kind = gate[0]
    if kind == "T":
        j = gate[1]
        for x in range(2**n):
            if (x >> j) & 1:
                out[x] *= OMEGA
        return out
    if kind == "CX":
        c, t = gate[1], gate[2]
        nxt = np.zeros_like(out)
        for x, amp in enumerate(out):
            y = x ^ (1 << t) if ((x >> c) & 1) else x
            nxt[y] += amp
        return nxt
    if kind == "H":
        j = gate[1]
        nxt = np.zeros_like(out)
        s = 1 / np.sqrt(2)
        for x, amp in enumerate(out):
            bit = (x >> j) & 1
            y0 = x & ~(1 << j)
            y1 = y0 | (1 << j)
            nxt[y0] += s * amp
            nxt[y1] += s * ((-1) ** bit) * amp
        return nxt
    raise ValueError(gate)


def path_terms(n: int, circuit: list[tuple]) -> list[tuple[int, int]]:
    # Each entry is (current computational label, p in Z_8).
    terms = [(0, 0)]
    for gate in circuit:
        kind = gate[0]
        if kind == "T":
            j = gate[1]
            terms = [
                (q, (p + ((q >> j) & 1)) % 8)
                for q, p in terms
            ]
        elif kind == "CX":
            c, t = gate[1], gate[2]
            nxt = []
            for q, p in terms:
                if (q >> c) & 1:
                    q ^= 1 << t
                nxt.append((q, p))
            terms = nxt
        elif kind == "H":
            j = gate[1]
            nxt = []
            for q, p in terms:
                x = (q >> j) & 1
                base = q & ~(1 << j)
                for y in (0, 1):
                    q2 = base | (y << j)
                    p2 = (p + 4 * x * y) % 8
                    nxt.append((q2, p2))
            terms = nxt
        else:
            raise ValueError(gate)
    return terms


def amplitudes_from_paths(n: int, circuit: list[tuple]) -> np.ndarray:
    terms = path_terms(n, circuit)
    h = sum(g[0] == "H" for g in circuit)
    out = np.zeros(2**n, dtype=complex)
    scale = 2 ** (-h / 2)
    for q, p in terms:
        out[q] += scale * OMEGA**p
    return out


def main() -> None:
    rng = np.random.default_rng(21302)
    max_err = 0.0
    for n in (2, 3, 4):
        gates = [("H", j) for j in range(n)] + [("T", j) for j in range(n)]
        gates += [("CX", c, t) for c in range(n) for t in range(n) if c != t]
        for _ in range(80):
            depth = int(rng.integers(1, 14))
            circuit = [gates[int(rng.integers(len(gates)))] for _ in range(depth)]
            state = np.zeros(2**n, dtype=complex)
            state[0] = 1
            for gate in circuit:
                state = apply_statevector(state, gate, n)
            path = amplitudes_from_paths(n, circuit)
            err = float(np.max(np.abs(state - path)))
            max_err = max(max_err, err)
            assert err < 2e-12
    print(f"r213b_ok max_amplitude_error={max_err:.3e}")


if __name__ == "__main__":
    main()
