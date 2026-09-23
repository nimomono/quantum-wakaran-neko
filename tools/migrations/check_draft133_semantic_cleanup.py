#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(not (ROOT / "tools/verify_m47_action_shell_origin.py").exists(),
            "retired action-shell verifier remains required")
    require(not (ROOT / "tools/verify_r194_brownian_spin_nelson.py").exists(),
            "R194 candidate verifier remains required")
    require(not (ROOT / "tools/verify_q2_shell_and_locality.py").exists(),
            "mixed Q2 verifier remains required")
    require((ROOT / "notes/retired_verifiers/verify_m47_action_shell_origin.py").exists(),
            "retired action-shell verifier missing")
    require((ROOT / "tools/candidate_checks/verify_r194_brownian_spin_nelson.py").exists(),
            "R194 candidate verifier missing")
    require((ROOT / "tools/verify_m54_static_invariants.py").exists(),
            "M54 invariant verifier missing")
    require((ROOT / "tools/verify_r180c_locality.py").exists(),
            "R180C locality verifier missing")

    ps = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    result_block = ps.split("## 現行結果の導出状態", 1)[1].split("## 物理的解釈と境界", 1)[0]
    require("### M65 binary-selector結果" in result_block, "R204 classification missing")
    require("### M66 common thermal-reservoir結果" in result_block, "R205 classification missing")
    require("### R206 Q2 specialization結果" in result_block, "R206 classification missing")
    require("### Q2-2-S candidate結果" in result_block, "R207 classification missing")
    q3 = result_block.split("### Q3結果", 1)[1]
    for non_q3_prefix in ("| R204", "| R205", "| R206", "| R207"):
        require(non_q3_prefix not in q3, f"non-Q3 result remains under Q3: {non_q3_prefix}")
    for required_prefix in ("| R203A", "| R203B", "| R203C", "| R203D", "| R185"):
        require(required_prefix in q3, f"Q3 result missing from Q3 classification: {required_prefix}")

    current_docs = "\n".join(
        (ROOT / path).read_text(encoding="utf-8")
        for path in (
            "README.md",
            "PROJECT_STATUS.md",
            "ENHANCEMENT_TARGETS.md",
            "notes/theory_lineage.md",
        )
    )
    require(("M66 " + "terminal sampler") not in current_docs,
            "ambiguous M66 terminal sampler wording remains")
    require(("terminal M66/R206 " + "sampling") not in current_docs,
            "ambiguous terminal M66/R206 sampling wording remains")

    print("draft-133 semantic cleanup migration checks passed")


if __name__ == "__main__":
    main()
