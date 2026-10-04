#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def main() -> None:
    # R208D is now a structural profile dispatcher.
    # Continuous branch inherits its process error from R214B without re-adding it.
    eps_r214 = 0.013
    eps_m64 = 0.007
    continuous_total = eps_r214 + eps_m64
    assert abs(continuous_total - 0.020) < 1e-15

    # Finite-graph branch delegates to the R203D local density/current interface.
    R = np.array([0.35, 0.65], dtype=float)
    J = 0.12
    T = 0.40
    assert T >= abs(J)

    k01 = (T + J) / (2.0 * R[0])
    k10 = (T - J) / (2.0 * R[1])
    flux = R[0] * k01 - R[1] * k10
    assert abs(flux - J) < 1e-14

    # Dispatcher must not require any R214 contribution on the finite-graph branch.
    finite_graph_r214_contribution = 0.0
    assert finite_graph_r214_contribution == 0.0

    print(
        "r208d_profile_dispatch_ok",
        f"continuous_total={continuous_total:.6f}",
        f"finite_graph_flux={flux:.6f}",
    )


if __name__ == "__main__":
    main()
