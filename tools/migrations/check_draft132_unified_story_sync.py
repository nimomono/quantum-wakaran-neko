#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def current_goal_row(project_status: str, goal: str) -> str:
    block = project_status.split("### 現在地", 1)[1].split(
        "## 現行模型・物理実装層・手順の運用状態", 1
    )[0]
    match = re.search(rf"^\|\s*{re.escape(goal)}\s*\|.*$", block, re.M)
    if not match:
        raise AssertionError(f"missing current goal row: {goal}")
    return match.group(0)


def main() -> None:
    overview = read("sections/00_overview_and_contents.md")
    chapter1 = read("sections/01_scope_and_cycle.md")
    chapter2 = read("sections/02_common_canonical_modules.md")
    chapter8 = read("sections/08_errors_resources_open_targets.md")
    chapter9 = read("sections/09_conclusion.md")
    readme = read("README.md")
    status = read("PROJECT_STATUS.md")
    enhancement = read("ENHANCEMENT_TARGETS.md")

    for text, name in (
        (overview, "overview"),
        (chapter1, "chapter1"),
        (chapter2, "chapter2"),
        (chapter9, "chapter9"),
        (readme, "README"),
    ):
        for token in ("M54", "M66", "M64", "M65", "R206"):
            if token not in text:
                raise AssertionError(f"{name} missing unified-story token: {token}")

    if "## 2.8 R161の共通整合・Markov経路法則とM64/R162の物理・参照実現##" in chapter2:
        raise AssertionError("chapter 2 duplicate heading remains")
    if "## 8.9 Q2の根拠モデル、共通ハードウェア努力目標、ブラックボックス資源分類##" in chapter8:
        raise AssertionError("chapter 8 duplicate heading remains")

    stale_q23 = "M65とR181Dが末端2結果読出しと結果成分受渡しを与えるため"
    if stale_q23 in chapter8:
        raise AssertionError("stale Q2-3 M65/R181D terminal reader remains")
    for token in ("Q2-3", "M66/R206D", "8結果"):
        if token not in chapter8:
            raise AssertionError(f"chapter 8 missing Q2-3 terminal sync token: {token}")

    stale_r205f = (
        "R205FをQ2-2-Sの空間分離Bell構成へ適用する作業は後続強化へ残す"
    )
    if stale_r205f in chapter9:
        raise AssertionError("chapter 9 pre-R207 R205F text remains")
    if "候補主線へまだ接続しない" in enhancement:
        raise AssertionError("ENHANCEMENT_TARGETS pre-R207 current text remains")

    q22 = current_goal_row(status, "Q2-2")
    if "| Q2-2 | 達成 |" not in q22:
        raise AssertionError("Q2-2 fixed-goal status changed")
    for token in ("R180C", "R181D", "R204D--R204E"):
        if token not in q22:
            raise AssertionError(f"Q2-2 fixed-goal dependency changed: {token}")
    if "R207" in q22:
        raise AssertionError("R207 leaked into Q2-2 fixed-goal row")

    q23 = current_goal_row(status, "Q2-3")
    if "R206D" not in q23 or "R204" in q23:
        raise AssertionError("Q2-3 current row is not terminal R206 path")

    if "| Q2-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |" not in enhancement:
        raise AssertionError("Q2-2-S overall strengthening status changed")
    for token in ("R205F + R207C", "R207B/C", "finite-speed spatial reservoir"):
        if token not in enhancement:
            raise AssertionError(f"Q2-2-S management token missing: {token}")

    if "M66共通化からwhole-model derivation" not in status:
        raise AssertionError("draft-132 non-overclaim boundary missing")

    print("draft132_unified_story_sync_ok")


if __name__ == "__main__":
    main()
