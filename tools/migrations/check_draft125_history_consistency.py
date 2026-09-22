#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(path: str, *tokens: str) -> None:
    text = read(path)
    missing = [token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-125 markers: {missing}")


def status(text: str, qid: str) -> str:
    m = re.search(
        rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|",
        text,
        re.M,
    )
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)


def main() -> None:
    require(
        "notes/theory_lineage.md",
        "現行の主要因果鎖",
        "M65 / R204",
        "M64 / R203A--R203D",
        "履歴メモの読み方",
    )
    require(
        "notes/README.md",
        "`theory_lineage.md`",
        "中間置換先が後に退役していても",
    )
    require(
        "notes/superseded_result_index.md",
        "`theory_lineage.md`",
        "退役行の第1列は退役した結果IDだけ",
    )
    for path in (
        "notes/superseded_a8_m47_hopf_preparation.md",
        "notes/superseded_r181a_template_port_preparation.md",
    ):
        require(path, "現行注記（draft-125）", "`theory_lineage.md`")
    require(
        "notes/brownian_spin_q1_q3_unification.md",
        "draft-120以後のQ1/Q2測定正本はM65/R181D",
        "`theory_lineage.md`",
    )

    require(
        "tools/check_project_consistency.py",
        "active_result_ids",
        "status_result_ids",
        "fixed_goal_dependency_ids",
        "retired_result_ids",
        "check_note_references",
    )
    require(
        ".github/workflows/verify.yml",
        "履歴・依存整合を検査",
        "python tools/check_project_consistency.py",
    )
    require(
        "tools/test_validation_policy.py",
        "test_structural_checkers_have_no_theory_snapshot_literals",
        "test_project_consistency_checker_is_called_by_ci",
    )
    require(
        "PROJECT_GUIDE.md",
        "`notes/theory_lineage.md`",
        "`tools/check_project_consistency.py`",
    )
    require(
        "VALIDATION_POLICY.md",
        "`check_project_consistency.py`",
        "active結果IDと退役索引の交差",
    )
    require(
        "PROJECT_STATUS.md",
        "draft-125：履歴メモと横断整合検査",
        "`notes/theory_lineage.md`",
    )

    ps = read("PROJECT_STATUS.md")
    expected = {
        "Q1-1": "達成",
        "Q1-2": "達成",
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
        "Q3-1": "達成",
        "Q3-2": "達成",
        "Q3-4A": "達成",
        "Q3-4B": "達成",
        "Q3-5": "達成",
        "Q3-6": "未達",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    print("draft125_history_consistency_ok")


if __name__ == "__main__":
    main()
