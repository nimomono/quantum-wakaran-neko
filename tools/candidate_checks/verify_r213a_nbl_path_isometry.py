#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(21301)
    n = 5
    dim = 2**n

    # The abstract reference-product basis is orthonormal, so its Gram matrix is I.
    gram = np.eye(dim, dtype=complex)
    for _ in range(32):
        z = rng.normal(size=dim) + 1j * rng.normal(size=dim)
        w = rng.normal(size=dim) + 1j * rng.normal(size=dim)
        lhs = np.vdot(z, gram @ w)
        rhs = np.vdot(z, w)
        assert abs(lhs - rhs) < 1e-12

    # Finite time sampling: an empirical Gram matrix from m samples has rank <= m.
    m = dim // 2
    samples = rng.normal(size=(m, dim)) + 1j * rng.normal(size=(m, dim))
    empirical = samples.conj().T @ samples / m
    rank = np.linalg.matrix_rank(empirical, tol=1e-10)
    assert rank <= m < dim

    print(
        "r213a_ok "
        f"n={n} dim={dim} empirical_samples={m} empirical_rank={rank}"
    )


if __name__ == "__main__":
    main()
