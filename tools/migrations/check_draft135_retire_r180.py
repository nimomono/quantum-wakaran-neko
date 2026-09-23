#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    sections = ROOT / "sections"
    active_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(sections.glob("*.md"))
    )
    require("R180" not in active_text, "R180 remains in active paper sections")
    require(
        not (sections / "A4_m54_receiver_cycle_proofs.md").exists(),
        "R180 proof appendix D remains active",
    )

    ps = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    q22 = next(line for line in ps.splitlines() if line.startswith("| Q2-2 | 達成 |"))
    require("R207A--R207C" in q22, "Q2-2 direct evidence is not R207A--R207C")
    require("R180" not in q22 and "R181D" not in q22, "Q2-2 still depends on Theory A")
    q12 = next(line for line in ps.splitlines() if line.startswith("| Q1-2 | 達成 |"))
    require("R181D" in q12 and "R204D--R204F" in q12, "Q1 M65/R181D responsibility was lost")

    current_results = ps.split("## 現行結果の導出状態", 1)[1].split("## 物理的解釈と境界", 1)[0]
    require("| R180A |" not in current_results, "R180A remains in current result ledger")
    require("| R180C |" not in current_results, "R180C remains in current result ledger")
    require("| R181D |" in current_results, "R181D was retired accidentally")
    require("| R207A |" in current_results and "| R207D |" in current_results, "R207 mainline was damaged")

    require(not (ROOT / "tools/verify_r180_m54_receiver.py").exists(), "R180 receiver verifier remains required")
    require(not (ROOT / "tools/verify_r180c_locality.py").exists(), "R180 locality verifier remains required")
    require((ROOT / "notes/retired_verifiers/verify_r180_m54_receiver.py").exists(), "archived R180 receiver verifier missing")
    require((ROOT / "notes/retired_verifiers/verify_r180c_locality.py").exists(), "archived R180 locality verifier missing")
    require((ROOT / "notes/superseded_r180_sequential_q2_2_witness.md").exists(), "R180 retirement note missing")

    retired = (ROOT / "notes/superseded_result_index.md").read_text(encoding="utf-8")
    require("| R180A |" in retired and "| R180C |" in retired, "R180 results missing from retired index")

    enh = (ROOT / "ENHANCEMENT_TARGETS.md").read_text(encoding="utf-8")
    row = next(line for line in enh.splitlines() if line.startswith("| Q2-2 | 未監査 |"))
    require("R207A--R207D" in row and "R180" not in row, "Q2-2 strengthening candidate row is not R207-only")
    require("finite-speed" in enh and "未監査" in enh, "Q2-2-S strengthening boundary changed")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require("Q2-2" in readme and "R207" in readme, "README lost Q2-2 R207 mainline")
    require("R180" not in readme, "README still exposes R180 as current theory")

    manifest = (ROOT / "MANIFEST.md").read_text(encoding="utf-8")
    require("sections/A4_m54_receiver_cycle_proofs.md" not in manifest, "MANIFEST still lists appendix D")
    require("tools/verify_r180_m54_receiver.py" not in manifest, "MANIFEST still lists R180 receiver verifier")
    require("tools/verify_r180c_locality.py" not in manifest, "MANIFEST still lists R180 locality verifier")

    print("draft-135 R180 retirement migration checks passed")


if __name__ == "__main__":
    main()
