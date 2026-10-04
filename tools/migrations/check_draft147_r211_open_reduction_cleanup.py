#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def main() -> None:
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    a25 = read("sections/A25_m64_three_entity_open_q3_model.md")
    errors = read("sections/08_errors_resources_open_targets.md")
    status = read("PROJECT_STATUS.md")

    r211 = a27.split("## AA.18 R211A", 1)[1].split("## AA.20 R211C", 1)[0]
    for stale in (
        "R209B/C",
        "AA.6/R208D",
        "R208Bのcanonical mean-force",
        "R208C/R209B",
    ):
        require(stale not in r211, f"stale R211 dependency remains: {stale}")

    require(
        "R209B finite-window OU/Langevin realization corollary" in a27,
        "R209B finite-window realization corollary missing",
    )
    require(
        "d\\zeta_\\alpha" in r211 and "\\varepsilon_{\\rm FH}" in r211,
        "R211B open reduction / finite-Hamiltonian ledger missing",
    )
    require(
        "付録AC/R214B" in a25 and "退役したR209Cは現行bridgeに使わない" in a25,
        "A25 current M67->M64 bridge is not R214B",
    )
    early_q3 = errors.split("## 8.2", 1)[0]
    require("R209CのM67からM64 process compatibility" not in early_q3,
            "section 08 still uses R209C as current Q3 bridge")
    require("R208/R209の既存台帳" not in early_q3,
            "section 08 still uses legacy broad Q3 ledger")
    require("\\varepsilon_{214\\to64}" in early_q3,
            "section 08 current Q3 ledger lacks R214B error")
    require(
        "\\varepsilon_{\\rm FH}" in errors
        and "\\varepsilon_{\\rm pv}" in errors
        and "\\varepsilon_{\\rm od}" in errors,
        "Q1 R211 error ledger not synchronized",
    )

    require("| Q1-1 | 達成 |" in status, "Q1-1 status changed")
    require("| Q1-2 | 達成 |" in status, "Q1-2 status changed")
    require("| Q2-4 | 条件付き達成 |" in status, "Q2-4 status changed")
    require("| Q3-6 | 未達 |" in status, "Q3-6 status changed")
    require("R208B/R208C/R209Cには依存せず" in status,
            "R211B status boundary not synchronized")
    require((ROOT / "tools/verify_r211b_q1_open_reduction.py").is_file(),
            "new R211B required verifier missing")

    print("draft147_r211_open_reduction_cleanup_ok")


if __name__ == "__main__":
    main()
