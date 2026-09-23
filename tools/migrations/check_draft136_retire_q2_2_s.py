#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    enh = (ROOT / "ENHANCEMENT_TARGETS.md").read_text(encoding="utf-8")
    require("Q2-2-S" not in enh, "Q2-2-S remains in active enhancement registry")
    require("固有強化" not in enh, "retired special-strengthening column remains")
    current = enh.split("## 強化目標の現在地表", 1)[1]
    q22_enh = next(line for line in current.splitlines() if line.startswith("| Q2-2 |"))
    cells = [c.strip() for c in q22_enh.strip().strip("|").split("|")]
    require(len(cells) == 7, "Q2-2 enhancement row is not A1/A2/B1/B2/B3 + candidate")
    require(cells[1:6] == ["未監査"] * 5, "Q2-2 A/B strengthening states changed")

    active_sections = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((ROOT / "sections").glob("*.md"))
    )
    require("Q2-2-S" not in active_sections, "Q2-2-S remains in active paper")
    require("v_{\\max}" not in active_sections, "finite-speed Bell timing remains an active paper target")

    for path in ("README.md", "PROJECT_STANCE.md", "PROJECT_GUIDE.md"):
        text = (ROOT / path).read_text(encoding="utf-8")
        require("Q2-2-S" not in text, f"Q2-2-S remains current in {path}")

    ps = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    q22 = next(line for line in ps.splitlines() if line.startswith("| Q2-2 | 達成 |"))
    require("R207A--R207C" in q22, "Q2-2 direct evidence changed")
    require("finite-speed" not in q22 and "Q2-2-S" not in q22, "Q2-2 row still carries spatial strengthening")
    require("| R207D |" in ps, "R207D Bell-local control was lost")
    require("measurement independence" in ps, "Bell measurement-independence audit missing")

    require((ROOT / "tools/verify_r207_projection_phase_volume.py").exists(), "R207 required verifier missing")
    require(
        not (ROOT / "tools/candidate_checks/verify_r207_separation_control.py").exists(),
        "retired Q2-2-S candidate checker remains active",
    )
    require(
        (ROOT / "notes/superseded_q2_2_s_spatial_strengthening.md").exists(),
        "Q2-2-S retirement note missing",
    )

    print("draft-136 Q2-2-S retirement migration checks passed")


if __name__ == "__main__":
    main()
