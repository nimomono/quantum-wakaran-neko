#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import numpy as np


def target_density(r: np.ndarray, ell: float, sigma: float) -> np.ndarray:
    w = r * r * np.exp(-0.5 * ((r - ell) / sigma) ** 2)
    return w / np.trapz(w, r)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trajectories", type=int, default=12000)
    ap.add_argument("--steps", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=21402)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    kBT = 1.0
    k = 1.0
    gamma = 0.02
    D = kBT / gamma
    sigma = math.sqrt(kBT / k)
    ell = 2.5 * sigma
    dt = 2e-5

    x = np.zeros((args.trajectories, 3), dtype=float)
    x[:, 0] = ell

    for _ in range(args.steps):
        r = np.linalg.norm(x, axis=1)
        safe = np.maximum(r, 1e-12)
        force = -k * ((r - ell) / safe)[:, None] * x
        x += (force / gamma) * dt
        x += math.sqrt(2.0 * D * dt) * rng.normal(size=x.shape)

    radii = np.linalg.norm(x, axis=1)
    edges = np.linspace(0.0, ell + 5.0 * sigma, 90)
    hist, _ = np.histogram(radii, bins=edges, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    target = target_density(centers, ell, sigma)
    widths = np.diff(edges)
    tv = 0.5 * float(np.sum(np.abs(hist - target) * widths))

    mean_emp = float(np.mean(radii))
    mean_target = float(np.sum(centers * target * widths))

    assert np.isfinite(tv)
    assert tv < 0.16
    assert abs(mean_emp - mean_target) < 0.18

    print(
        "r214_dumbbell_q3_witness_ok "
        f"trajectories={args.trajectories} steps={args.steps} "
        f"tv={tv:.4f} mean_emp={mean_emp:.4f} mean_target={mean_target:.4f}"
    )


if __name__ == "__main__":
    main()
