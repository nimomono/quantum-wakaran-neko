#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    ps = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    sec5 = (ROOT / "sections/05_m54_setting_pre_receiver.md").read_text(encoding="utf-8")
    a23 = (ROOT / "sections/A23_q2_2_spatial_preparation.md").read_text(encoding="utf-8")
    enh = (ROOT / "ENHANCEMENT_TARGETS.md").read_text(encoding="utf-8")

    q2row = next(line for line in ps.splitlines() if line.startswith("| Q2-2 | 達成 |"))
    require("R207A--R207C" in q2row, "Q2-2 direct evidence was not switched to R207")
    require("R180C" not in q2row, "R180C remains a Q2-2 direct dependency")
    require("projection phase-volume" in sec5, "chapter 5 not switched")
    require("R207A" in a23 and "R207D" in a23, "R207 theorem block missing")
    require((ROOT / "tools/verify_r207_projection_phase_volume.py").exists(), "required verifier missing")
    require(not (ROOT / "tools/candidate_checks/verify_r207_gibbs_chsh.py").exists(), "old Gibbs checker still active")
    require((ROOT / "notes/retired_verifiers/verify_r207_gibbs_chsh.py").exists(), "retired checker missing")
    require((ROOT / "notes/superseded_r207_four_setting_gibbs_candidate.md").exists(), "old candidate note missing")
    require("R180C" in sec5, "R180C retired prematurely")
    require((ROOT / "tools/verify_r180c_locality.py").exists(), "R180C verifier retired prematurely")
    require("未監査" in enh and "finite-speed" in enh, "Q2-2-S boundary changed incorrectly")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require("Q2-2 Bell統計" in readme and "R207" in readme, "README not switched")
    require("Q1逐次測定" in readme and "M65" in readme, "Q1 M65 responsibility lost")
    print("draft-134 R207 promotion migration checks passed")


if __name__ == "__main__":
    main()
