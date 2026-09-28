#!/usr/bin/env python3
from __future__ import annotations

import numpy as np

OMEGA = np.exp(1j * np.pi / 4)


def apply_sv(state: np.ndarray, gate: tuple, n: int) -> np.ndarray:
    kind = gate[0]
    if kind == "T":
        out = state.copy()
        j = gate[1]
        for x in range(2**n):
            if (x >> j) & 1:
                out[x] *= OMEGA
        return out
    if kind == "CX":
        c, t = gate[1], gate[2]
        out = np.zeros_like(state)
        for x, amp in enumerate(state):
            y = x ^ (1 << t) if ((x >> c) & 1) else x
            out[y] += amp
        return out
    if kind == "H":
        j = gate[1]
        out = np.zeros_like(state)
        for x, amp in enumerate(state):
            bit = (x >> j) & 1
            base = x & ~(1 << j)
            out[base] += amp / np.sqrt(2)
            out[base | (1 << j)] += ((-1) ** bit) * amp / np.sqrt(2)
        return out
    raise ValueError(gate)


def path_terms(n: int, circuit: list[tuple]) -> list[tuple[int, int]]:
    terms = [(0, 0)]
    for gate in circuit:
        kind = gate[0]
        if kind == "T":
            j = gate[1]
            terms = [(q, (p + ((q >> j) & 1)) % 8) for q, p in terms]
        elif kind == "CX":
            c, t = gate[1], gate[2]
            nxt = []
            for q, p in terms:
                nxt.append((q ^ (1 << t) if ((q >> c) & 1) else q, p))
            terms = nxt
        elif kind == "H":
            j = gate[1]
            nxt = []
            for q, p in terms:
                x = (q >> j) & 1
                base = q & ~(1 << j)
                for y in (0, 1):
                    nxt.append((base | (y << j), (p + 4 * x * y) % 8))
            terms = nxt
        else:
            raise ValueError(gate)
    return terms


def collector(n: int, terms: list[tuple[int, int]]) -> np.ndarray:
    m = len(terms)
    out = np.zeros(2**n, dtype=complex)
    for q, p in terms:
        out[q] += OMEGA**p / np.sqrt(m)
    return out


def run_case(n: int, circuit: list[tuple]) -> tuple[float, float]:
    state = np.zeros(2**n, dtype=complex)
    state[0] = 1
    for gate in circuit:
        state = apply_sv(state, gate, n)
    col = collector(n, path_terms(n, circuit))
    amp = float(np.max(np.abs(state - col)))
    born = float(np.max(np.abs(np.abs(state) ** 2 - np.abs(col) ** 2)))
    return amp, born


def main() -> None:
    rng = np.random.default_rng(21304)
    max_amp = 0.0
    max_born = 0.0
    cases = 0

    for n in (2, 3, 4):
        pool = [("H", j) for j in range(n)] + [("T", j) for j in range(n)]
        pool += [("CX", c, t) for c in range(n) for t in range(n) if c != t]
        for depth in (4, 8, 12):
            for _ in range(20):
                circuit = [pool[int(rng.integers(len(pool)))] for _ in range(depth)]
                amp, born = run_case(n, circuit)
                max_amp = max(max_amp, amp)
                max_born = max(max_born, born)
                cases += 1

    # Exact destructive-interference witness: H-Z-H with Z = T^4 maps |0> to |1>.
    hzh = [("H", 0)] + [("T", 0)] * 4 + [("H", 0)]
    amp, born = run_case(1, hzh)
    max_amp = max(max_amp, amp)
    max_born = max(max_born, born)

    assert max_amp < 3e-12
    assert max_born < 3e-12
    print(
        "r213_nbl_q2_witness_ok "
        f"cases={cases + 1} max_amp={max_amp:.3e} max_born={max_born:.3e}"
    )


if __name__ == "__main__":
    main()
