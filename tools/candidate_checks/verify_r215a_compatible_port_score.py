#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    length = 2.0 * math.pi
    x = np.linspace(0.0, length, 20001, endpoint=False)
    dx = length / x.size

    nu = 0.7
    amp = 0.23
    c = 0.41
    t = 0.37
    z = 1.6 * math.exp(0.13 * t)
    phase = x - c * t

    pi = (1.0 + amp * np.cos(phase)) / length
    dpi = -amp * np.sin(phase) / length
    dt_pi = amp * c * np.sin(phase) / length
    u = nu * dpi / pi
    U = np.full_like(x, c)

    # Projective weight w=Z(t) pi: global amplitude must drop out of score.
    w = z * pi
    dw = z * dpi
    score_w = dw / w
    score_pi = dpi / pi
    assert np.max(np.abs(score_w - score_pi)) < 2e-14

    # Projective compatibility:
    # dt w + d_x(w U) = lambda w, lambda=dot Z/Z.
    lam = 0.13
    dt_w = lam * w + z * dt_pi
    d_wU = z * c * dpi
    assert np.max(np.abs(dt_w + d_wU - lam * w)) < 2e-14

    # Normalized continuity.
    assert np.max(np.abs(dt_pi + c * dpi)) < 2e-14

    # Fokker--Planck cancellation at p=pi.
    # -d_x[(U+u)pi] + nu d_xx pi = -d_x(U pi)
    ddpi = -amp * np.cos(phase) / length
    osm_current = u * pi
    # osm_current = nu dpi exactly
    assert np.max(np.abs(osm_current - nu * dpi)) < 2e-14
    fp_rhs = -c * dpi - nu * ddpi + nu * ddpi
    assert np.max(np.abs(fp_rhs + c * dpi)) < 2e-14
    assert np.max(np.abs(dt_pi - fp_rhs)) < 2e-14

    # Bayes forward/backward score decomposition.
    b_plus = U + u
    b_minus = b_plus - 2.0 * nu * score_pi
    assert np.max(np.abs(b_minus - (U - u))) < 2e-14
    assert np.max(np.abs(0.5 * (b_plus + b_minus) - U)) < 2e-14
    assert np.max(np.abs(0.5 * (b_plus - b_minus) - u)) < 2e-14

    # Normalization and positivity.
    assert abs(float(np.sum(pi) * dx) - 1.0) < 2e-13
    assert float(np.min(pi)) > 0.0

    print(
        "r215a_candidate_ok "
        f"min_pi={np.min(pi):.6e} "
        f"max_score={np.max(np.abs(score_pi)):.6e}"
    )


if __name__ == "__main__":
    main()
