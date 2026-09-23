#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def current_block(text: str) -> str:
    return text.split("### 現在地", 1)[1].split(
        "## 現行模型・物理実装層・手順の運用状態", 1
    )[0]


def row(text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|.*$", current_block(text), re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: missing row {qid}")
    return m.group(0)


def main() -> None:
    chapter5 = read("sections/05_m54_setting_pre_receiver.md")
    if "@title: Bell型測定統計：現行逐次証人と空間隔離強化" not in chapter5:
        raise AssertionError("chapter 5 title not synchronized")
    for token in (
        "R180C fixed-goal witness",
        "R207 Q2-2-S candidate",
        "### 5.7.3 S0--S4の現在地",
        "| S0 | R180C |",
        "| S1 | R207A |",
        "| S2 | R205F + R207C |",
        "| S3 | R207B + R207C |",
        "| S4 | R207D |",
        "finite-speed physical isolationは未閉包",
        "t_A^{\\rm set}=t_A^{\\rm latch}",
    ):
        if token not in chapter5:
            raise AssertionError(f"chapter 5 missing sync token: {token}")

    enh = read("ENHANCEMENT_TARGETS.md")
    for token in (
        "### Q2-2-Sの現在地監査",
        "| S0 | 非空間分離基準系 | R180C",
        "| S1 | 実在する二端と分離protocol | R207A",
        "| S2 | setting確定後に他端から到達可能な信号を使わない | R205F + R207C",
        "| S3 | S2を保ったBell型統計と前提監査 | R207B/C",
        "| S4 | Bell局所CHSH対照系 | R207D",
        "finite-speed spatial reservoir",
        "Q2-2-S全体の公式状態は `未監査`",
    ):
        if token not in enh:
            raise AssertionError(f"ENHANCEMENT_TARGETS missing sync token: {token}")
    if "| Q2-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |" not in enh:
        raise AssertionError("Q2-2-S overall status changed")

    ps = read("PROJECT_STATUS.md")
    q22 = row(ps, "Q2-2")
    for token in ("R112", "R180C", "R181D", "R204D--R204E"):
        if token not in q22:
            raise AssertionError(f"Q2-2 fixed-goal dependency changed: {q22}")
    for token in ("R207A", "R207B", "R207C", "R207D"):
        if token in q22:
            raise AssertionError(f"R207 leaked into Q2-2 fixed-goal dependency: {q22}")
        if f"| {token} |" not in ps:
            raise AssertionError(f"PROJECT_STATUS missing active candidate result: {token}")
    if "| Q2-2 | 達成 |" not in ps:
        raise AssertionError("Q2-2 fixed-goal status changed")

    section1 = read("sections/01_scope_and_cycle.md")
    if "R205Fの空間分離原理をBell型共同統計へ適用することはQ2-2-Sの後続強化" in section1:
        raise AssertionError("pre-R207 current-form text remains in section 1")

    a24 = read("sections/A24_m66_common_phase_volume_readout.md")
    if "具体的適用は付録W/R207A--R207D" not in a24:
        raise AssertionError("R205F current cross-reference not synchronized")

    for path in (
        "tools/candidate_checks/verify_r207_gibbs_chsh.py",
        "tools/candidate_checks/verify_r207_separation_control.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"R207 candidate verifier missing: {path}")

    print("draft131_q2_2_s_management_sync_ok")


if __name__ == "__main__":
    main()
