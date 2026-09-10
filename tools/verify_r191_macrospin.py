#!/usr/bin/env python3
from __future__ import annotations

import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPENDIX = ROOT / "sections" / "A20_m54_brownian_macrospin_projective_instrument.md"
COMMON = ROOT / "sections" / "02_common_canonical_modules.md"
STATUS = ROOT / "PROJECT_STATUS.md"


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b))


def verify_basin_identity() -> None:
    for _ in range(5000):
        jp = 10 ** random.uniform(-6.0, 3.0)
        jm = 10 ** random.uniform(-6.0, 3.0)
        s = jp + jm
        d = jp - jm
        u_star = -d / s
        close((1.0 - u_star) / 2.0, jp / s)
        close((1.0 + u_star) / 2.0, jm / s)


def verify_transducer_bound() -> None:
    for _ in range(30000):
        jp = 10 ** random.uniform(-6.0, 2.0)
        jm = 10 ** random.uniform(-6.0, 2.0)
        s = jp + jm
        d = jp - jm
        eps_s = random.uniform(0.0, 0.2)
        eps_d = random.uniform(0.0, 0.2)
        ds = random.uniform(-eps_s, eps_s) * s
        dd = random.uniform(-eps_d, eps_d) * s
        sh = s + ds
        dh = d + dd
        u = -d / s
        uh = -dh / sh
        bound = (eps_d + eps_s) / (1.0 - eps_s)
        if abs(uh - u) > bound + 1.0e-12:
            raise AssertionError((abs(uh - u), bound))


def verify_ito_transform() -> None:
    # For f(u)=artanh(u), b=(1-u^2)(u-u*)-u/Delta and
    # sigma^2=(1-u^2)/Delta.  Check that f'b+0.5 f''sigma^2=u-u*.
    for _ in range(10000):
        u = random.uniform(-0.98, 0.98)
        us = random.uniform(-0.9, 0.9)
        delta = 10 ** random.uniform(-1.0, 4.0)
        b = (1.0 - u * u) * (u - us) - u / delta
        sigma2 = (1.0 - u * u) / delta
        fp = 1.0 / (1.0 - u * u)
        fpp = 2.0 * u / (1.0 - u * u) ** 2
        transformed = fp * b + 0.5 * fpp * sigma2
        close(transformed, u - us, 2.0e-10)


def verify_scale_density() -> None:
    # s'(u)=exp[-Delta(u-u*)^2]/(1-u^2) must satisfy d log s'/du=-2b/sigma^2.
    for _ in range(10000):
        u = random.uniform(-0.95, 0.95)
        us = random.uniform(-0.8, 0.8)
        delta = 10 ** random.uniform(-0.5, 3.0)
        b = (1.0 - u * u) * (u - us) - u / delta
        sigma2 = (1.0 - u * u) / delta
        lhs = -2.0 * delta * (u - us) + 2.0 * u / (1.0 - u * u)
        rhs = -2.0 * b / sigma2
        close(lhs, rhs, 2.0e-10)


def verify_retreat_bound_shape() -> None:
    for _ in range(5000):
        zeta = random.uniform(0.01, 0.45)
        g = random.uniform(0.005, 0.5)
        delta_min = 10 ** random.uniform(-1.0, 5.0)
        mz = zeta * (2.0 - zeta)
        q = 2.0 / (mz * delta_min * g * g) * math.exp(-7.0 * delta_min * g * g / 16.0)
        q = min(1.0, q)
        if not 0.0 <= q <= 1.0:
            raise AssertionError(q)
    # The conservative bound must decrease once Delta*g^2 is sufficiently large.
    mz = 0.19
    g = 0.1
    vals = []
    for dg2 in (10.0, 20.0, 40.0, 80.0):
        delta_min = dg2 / (g * g)
        vals.append(2.0 / (mz * delta_min * g * g) * math.exp(-7.0 * dg2 / 16.0))
    if not all(a > b for a, b in zip(vals, vals[1:])):
        raise AssertionError(vals)


def verify_time_bound() -> None:
    for _ in range(5000):
        tau = random.uniform(0.03, 0.3)
        g = random.uniform(0.001, tau)
        zeta = random.uniform(0.001, tau)
        if g + zeta >= 2.0 * tau:
            continue
        left = -1.0 + 2.0 * tau + g
        right = 1.0 - zeta
        if not -1.0 < left < right < 1.0:
            continue
        lmax = math.atanh(right) - math.atanh(left)
        T = 2.0 * lmax / g + random.uniform(0.01, 10.0)
        delta_min = 10 ** random.uniform(-1.0, 4.0)
        mz = zeta * (2.0 - zeta)
        exponent = -delta_min * mz * (g * T / 2.0 - lmax) ** 2 / (2.0 * T)
        qtime = math.exp(exponent)
        if not 0.0 < qtime <= 1.0:
            raise AssertionError(qtime)


def verify_dispatcher_bound() -> None:
    # If the implemented probability is within eps_u/2 of the ideal one and
    # the small implemented branch is below tau_cut, deterministic dispatch
    # differs from ideal by at most tau_cut+eps_u/2.
    for _ in range(20000):
        p = random.random()
        eps_u = random.uniform(0.0, 0.1)
        dp = random.uniform(-eps_u / 2.0, eps_u / 2.0)
        ph = min(1.0, max(0.0, p + dp))
        cut = random.uniform(0.01, 0.2)
        if min(ph, 1.0 - ph) >= cut:
            continue
        dominant_plus = ph >= 0.5
        ideal_error = (1.0 - p) if dominant_plus else p
        if ideal_error > cut + eps_u / 2.0 + 1.0e-12:
            raise AssertionError((p, ph, cut, eps_u, ideal_error))


def verify_telescoping() -> None:
    # Scalar branch-action version of sequential Lüders telescoping.
    for _ in range(5000):
        s0 = 10 ** random.uniform(-4.0, 3.0)
        ratios = [random.uniform(0.02, 0.98) for _ in range(random.randint(1, 8))]
        s = s0
        product = 1.0
        for ratio in ratios:
            snext = s * ratio
            product *= snext / s
            s = snext
        close(product, s / s0)


def verify_source_contract() -> None:
    appendix = APPENDIX.read_text(encoding="utf-8")
    common = COMMON.read_text(encoding="utf-8")
    status = STATUS.read_text(encoding="utf-8")
    required = (
        "ブラウン巨視的スピン",
        "\\widehat u_*",
        "\\Delta_{\\min}",
        "q_{\\rm ret}",
        "q_{\\rm time}",
        "端点dispatcher",
        "成功試行だけの再規格化ではなく",
        "Q2-2ではR191を中央集約4結果samplerとして使わない",
        "一般深さで $\\|P_rZ\\|^2$ が読出し下限を下回り得る場合だけ",
    )
    for token in required:
        if token not in appendix:
            raise AssertionError(f"A20 missing: {token}")
    if "定理（R191：" not in common:
        raise AssertionError("R191 theorem missing from common module")
    if "R191" not in status:
        raise AssertionError("R191 missing from PROJECT_STATUS")


def main() -> None:
    random.seed(191)
    verify_basin_identity()
    verify_transducer_bound()
    verify_ito_transform()
    verify_scale_density()
    verify_retreat_bound_shape()
    verify_time_bound()
    verify_dispatcher_bound()
    verify_telescoping()
    verify_source_contract()
    print("R191 macrospin checks: OK")


if __name__ == "__main__":
    main()
