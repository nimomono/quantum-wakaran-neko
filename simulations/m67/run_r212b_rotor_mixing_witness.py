#!/usr/bin/env python3
"""R212B S^2 x S^2 rotor mixing witness for the R207 parameter point.

This is supporting numerical evidence, not a required fixed-goal proof. It
integrates the overdamped spherical R205E reduction at eta=1/4,
epsilon=eta/8, k=2/eta and compares the terminal law with exact equilibrium
samples from exp(k lambda_A.lambda_B) [w_A+w_B].
"""

import argparse
import json
import math
import numpy as np

ETA = 0.25
EPS = ETA / 8.0
K = 2.0 / ETA
D_ROT = 1.0


def f_eps(t):
    return np.sqrt(EPS * EPS + (1.0 - EPS * EPS) * t * t)


def setting_vectors(angle_deg):
    a = np.array([0.0, 0.0, 1.0])
    th = math.radians(angle_deg)
    b = np.array([math.sin(th), 0.0, math.cos(th)])
    return a, b


def tangent_grad_log_target(lam_a, lam_b, a, b):
    ta = lam_a @ a
    tb = lam_b @ b
    fa = f_eps(ta)
    fb = f_eps(tb)
    w = fa + fb
    fpa = (1.0 - EPS * EPS) * ta / fa
    fpb = (1.0 - EPS * EPS) * tb / fb
    ga = K * lam_b + (fpa / w)[:, None] * a
    gb = K * lam_a + (fpb / w)[:, None] * b
    ga -= np.sum(ga * lam_a, axis=1)[:, None] * lam_a
    gb -= np.sum(gb * lam_b, axis=1)[:, None] * lam_b
    return ga, gb


def spherical_diffusion(n, T, dt, angle_deg, seed):
    rng = np.random.default_rng(seed)
    a, b = setting_vectors(angle_deg)
    lam_a = np.tile(np.array([0.0, 0.0, 1.0]), (n, 1))
    lam_b = lam_a.copy()
    sqrt_noise = math.sqrt(2.0 * D_ROT * dt)
    steps = int(round(T / dt))
    for _ in range(steps):
        ga, gb = tangent_grad_log_target(lam_a, lam_b, a, b)
        za = rng.normal(size=lam_a.shape)
        zb = rng.normal(size=lam_b.shape)
        za -= np.sum(za * lam_a, axis=1)[:, None] * lam_a
        zb -= np.sum(zb * lam_b, axis=1)[:, None] * lam_b
        lam_a += D_ROT * ga * dt + sqrt_noise * za
        lam_b += D_ROT * gb * dt + sqrt_noise * zb
        lam_a /= np.linalg.norm(lam_a, axis=1)[:, None]
        lam_b /= np.linalg.norm(lam_b, axis=1)[:, None]
    return lam_a, lam_b, a, b


def random_sphere(rng, n):
    x = rng.normal(size=(n, 3))
    return x / np.linalg.norm(x, axis=1)[:, None]


def sample_vmf_about(mu, rng):
    n = len(mu)
    r = rng.random(n)
    em2 = math.exp(-2.0 * K)
    u = 1.0 + np.log(r + (1.0 - r) * em2) / K
    phi = 2.0 * math.pi * rng.random(n)
    helper = np.tile(np.array([0.0, 0.0, 1.0]), (n, 1))
    mask = np.abs(mu[:, 2]) > 0.9
    helper[mask] = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(helper, mu)
    e1 /= np.linalg.norm(e1, axis=1)[:, None]
    e2 = np.cross(mu, e1)
    s = np.sqrt(np.maximum(0.0, 1.0 - u * u))
    return u[:, None] * mu + s[:, None] * (
        np.cos(phi)[:, None] * e1 + np.sin(phi)[:, None] * e2
    )


def exact_target_samples(n, angle_deg, seed):
    rng = np.random.default_rng(seed)
    a, b = setting_vectors(angle_deg)
    aa = []
    bb = []
    got = 0
    while got < n:
        batch = max(1000, 3 * (n - got))
        la = random_sphere(rng, batch)
        lb = sample_vmf_about(la, rng)
        w = f_eps(la @ a) + f_eps(lb @ b)
        keep = rng.random(batch) < w / 2.0
        aa.append(la[keep])
        bb.append(lb[keep])
        got += int(np.count_nonzero(keep))
    return np.concatenate(aa)[:n], np.concatenate(bb)[:n], a, b


def features(la, lb, a, b):
    return np.column_stack(
        (np.sum(la * lb, axis=1), la @ a, lb @ b)
    )


def coarse_hist(la, lb, a, b, bins):
    edges = [np.linspace(-1.0, 1.0, bins + 1)] * 3
    h, _ = np.histogramdd(features(la, lb, a, b), bins=edges)
    return h / h.sum()


def coarse_tv(sample_a, sample_b, ref_a, ref_b, a, b, bins):
    return 0.5 * np.abs(
        coarse_hist(sample_a, sample_b, a, b, bins)
        - coarse_hist(ref_a, ref_b, a, b, bins)
    ).sum()


def run_one(angle_deg, n, T, dt, seed, bins=6, null_reps=40):
    la, lb, a, b = spherical_diffusion(
        n, T, dt, angle_deg, seed
    )
    ref_a, ref_b, _, _ = exact_target_samples(
        2 * n, angle_deg, seed + 1000
    )
    tv = float(
        coarse_tv(
            la,
            lb,
            ref_a[:n],
            ref_b[:n],
            a,
            b,
            bins,
        )
    )

    rng = np.random.default_rng(seed + 2000)
    null = []
    pool_n = len(ref_a)
    for _ in range(null_reps):
        i = rng.choice(pool_n, n, replace=False)
        j = rng.choice(pool_n, n, replace=False)
        null.append(
            coarse_tv(
                ref_a[i],
                ref_b[i],
                ref_a[j],
                ref_b[j],
                a,
                b,
                bins,
            )
        )
    null = np.asarray(null)

    mean_a = np.linalg.norm(np.mean(la, axis=0))
    mean_b = np.linalg.norm(np.mean(lb, axis=0))
    norm_err = max(
        float(
            np.max(
                np.abs(
                    np.linalg.norm(la, axis=1) - 1.0
                )
            )
        ),
        float(
            np.max(
                np.abs(
                    np.linalg.norm(lb, axis=1) - 1.0
                )
            )
        ),
    )
    return {
        "angle_deg": float(angle_deg),
        "trajectories": int(n),
        "T": float(T),
        "dt": float(dt),
        "coarse_bins_per_axis": int(bins),
        "coarse_tv_to_exact_equilibrium": tv,
        "equilibrium_sampling_tv_mean": float(
            np.mean(null)
        ),
        "equilibrium_sampling_tv_p95": float(
            np.quantile(null, 0.95)
        ),
        "terminal_mean_orientation_A": float(mean_a),
        "terminal_mean_orientation_B": float(mean_b),
        "sphere_norm_error_max": norm_err,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--angle-sweep", action="store_true")
    args = ap.parse_args()

    n = 6000 if args.full else 2500
    dt = 0.004 if args.full else 0.005
    T = 12.0
    angles = (
        [0.0, 45.0, 90.0, 135.0, 180.0]
        if args.angle_sweep
        else [45.0]
    )
    rows = [
        run_one(angle, n, T, dt, 21200 + i)
        for i, angle in enumerate(angles)
    ]

    for row in rows:
        assert row["sphere_norm_error_max"] < 1e-12, row
        assert (
            row["coarse_tv_to_exact_equilibrium"]
            <= row["equilibrium_sampling_tv_p95"] + 0.025
        ), row
        assert row["terminal_mean_orientation_A"] < 0.08, row
        assert row["terminal_mean_orientation_B"] < 0.08, row

    print(
        json.dumps(
            {
                "scope": (
                    "R212B S2xS2 overdamped mixing witness; "
                    "supporting evidence"
                ),
                "eta": ETA,
                "epsilon": EPS,
                "k": K,
                "D_rot": D_ROT,
                "rows": rows,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
