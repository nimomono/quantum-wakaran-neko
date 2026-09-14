#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from paper_source import ROOT, SECTIONS, chapter_paths, ordered_appendix_paths, parse_source, result_declarations, validate_github_markdown

STATUS_VALUES = {"達成", "条件付き達成", "部分達成", "未達"}
Q_STATUS_ROW = re.compile(r"^\|\s*(Q[123]-\d+[A-Z]?)\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|")


def check_sources() -> None:
    sources = sorted(SECTIONS.glob("*.md"))
    if not sources:
        raise AssertionError("sections/*.md is empty")

    chapter_paths()
    ordered_appendix_paths()
    for path in sources:
        meta, _ = parse_source(path)
        validate_github_markdown(path, path.read_text(encoding="utf-8"))
        if path.name not in {"00_overview_and_contents.md", "90_references.md"}:
            if not meta.get("title"):
                raise AssertionError(f"{path}: @title is missing")

    declarations: dict[str, list[str]] = defaultdict(list)
    for path in sources:
        for result_id in result_declarations(path):
            declarations[result_id].append(path.relative_to(ROOT).as_posix())
    duplicates = {key: value for key, value in declarations.items() if len(value) != 1}
    if duplicates:
        details = "; ".join(f"{key}={','.join(value)}" for key, value in sorted(duplicates.items()))
        raise AssertionError("active result declarations are not unique: " + details)


def check_project_status() -> None:
    path = ROOT / "PROJECT_STATUS.md"
    text = path.read_text(encoding="utf-8")

    try:
        fixed = text.split("### 固定目標一覧", 1)[1].split("#### Q3-1からQ3-6の達成判定の補足", 1)[0]
    except IndexError as exc:
        raise AssertionError("PROJECT_STATUS fixed-goal definition boundary is missing") from exc

    hit = re.search(r"(?<![A-Za-z])[MR]\d+", fixed)
    if hit:
        raise AssertionError(f"fixed-goal definition contains implementation/result ID: {hit.group(0)}")

    rows: dict[str, list[str]] = defaultdict(list)
    for line in text.splitlines():
        match = Q_STATUS_ROW.match(line)
        if match:
            rows[match.group(1)].append(match.group(2))
    if not rows:
        raise AssertionError("PROJECT_STATUS current-position rows were not found")
    inconsistent = {key: values for key, values in rows.items() if len(set(values)) != 1}
    if inconsistent:
        raise AssertionError(f"conflicting Q status rows: {inconsistent}")
    invalid = {value for values in rows.values() for value in values if value not in STATUS_VALUES}
    if invalid:
        raise AssertionError(f"unsupported status values: {sorted(invalid)}")



def check_r161_path_boundary() -> None:
    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 | 達成 |")), "")
    if not q32:
        raise AssertionError("Q3-2 current-position row is missing")
    cells = [cell.strip() for cell in q32.strip().strip("|").split("|")]
    if len(cells) < 7:
        raise AssertionError("Q3-2 current-position row is malformed")
    evidence = cells[5]
    if "R162" in evidence:
        raise AssertionError("R162 must not be a Q3-2 evidence dependency")
    for token in ("R195A", "R196A--R196C", "R161", "R185"):
        if token not in evidence:
            raise AssertionError(f"Q3-2 evidence is missing {token}")

    common = (ROOT / "sections" / "02_common_canonical_modules.md").read_text(encoding="utf-8")
    required = (
        "R161：有限配置の確率流・活動量整合とMarkov経路存在",
        "M_T",
        "canonical Markov経路法則",
        "R162：R161経路法則の独立Poisson-jump実現",
    )
    missing = [token for token in required if token not in common]
    if missing:
        raise AssertionError(f"R161 path-law markers missing: {missing}")

    appendix = (ROOT / "sections" / "A14_m54_spatial_moving_matching.md").read_text(encoding="utf-8")
    if "R161が定める前向き経路法則（R162" in appendix:
        raise AssertionError("R185 still declares R162 as a path dependency")


def check_enhancement_targets() -> None:
    status_path = ROOT / "PROJECT_STATUS.md"
    status_text = status_path.read_text(encoding="utf-8")
    fixed_ids = {
        match.group(1)
        for match in re.finditer(r"^\|\s*(Q[123]-\d+[A-Z]?)\s*\|\s*[^|]+\|", status_text, re.MULTILINE)
    }
    # Remove current-position duplicates by set semantics; only actual fixed IDs remain.
    if not fixed_ids:
        raise AssertionError("fixed-goal IDs were not found")

    path = ROOT / "ENHANCEMENT_TARGETS.md"
    text = path.read_text(encoding="utf-8")
    try:
        current = text.split("## 強化目標の現在地表", 1)[1].split("## 既存の実装強化課題との関係", 1)[0]
    except IndexError as exc:
        raise AssertionError("enhancement current-position boundary is missing") from exc

    rows: dict[str, list[str]] = {}
    allowed = {"未監査", "未達", "部分達成", "達成", "—"}
    for line in current.splitlines():
        if not re.match(r"^\|\s*Q[123]-", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            raise AssertionError(f"malformed enhancement row: {line}")
        qid = cells[0]
        rows[qid] = cells[1:7]
        invalid = set(cells[1:7]) - allowed
        if invalid:
            raise AssertionError(f"unsupported enhancement status for {qid}: {sorted(invalid)}")

    if set(rows) != fixed_ids:
        raise AssertionError(
            f"enhancement target IDs differ from fixed goals: missing={sorted(fixed_ids-set(rows))}, extra={sorted(set(rows)-fixed_ids)}"
        )

    for qid, values in rows.items():
        a1, a2, b1, b2, b3, special = values
        if a1 == "—" or a2 == "—":
            raise AssertionError(f"{qid}: A1/A2 must apply")
        if qid.startswith(("Q1-", "Q2-")):
            if "—" in (b1, b2, b3):
                raise AssertionError(f"{qid}: B1/B2/B3 must apply")
        else:
            if any(value != "—" for value in (b1, b2, b3)):
                raise AssertionError(f"{qid}: B1/B2/B3 must not apply")
        if qid == "Q2-2":
            if special == "—":
                raise AssertionError("Q2-2-S must apply to Q2-2")
        elif special != "—":
            raise AssertionError(f"{qid}: unexpected goal-specific enhancement")

    required = (
        "採用開放ミクロ方程式",
        "理想白色雑音",
        "有限帯域雑音",
        "Q2-2-S",
        "Bell局所因子化",
        "未監査",
    )
    missing = [token for token in required if token not in text]
    if missing:
        raise AssertionError(f"enhancement policy markers missing: {missing}")

    fixed_section = status_text.split("### 固定目標一覧", 1)[1].split("#### Q3-1からQ3-6の達成判定の補足", 1)[0]
    q22 = next((line for line in fixed_section.splitlines() if line.startswith("| Q2-2 |")), "")
    if "測定設定独立性の破れ" in q22:
        raise AssertionError("Q2-2 fixed goal still requires measurement-setting dependence")
    if "Bell不等式の導出に用いられる前提" not in q22:
        raise AssertionError("Q2-2 fixed goal does not require neutral Bell-premise audit")

    stance = (ROOT / "PROJECT_STANCE.md").read_text(encoding="utf-8")
    if "どの前提を破るかを固定目標の側で先に指定しない" not in stance:
        raise AssertionError("Bell-neutral project stance is missing")

    receiver = (ROOT / "sections" / "05_m54_setting_pre_receiver.md").read_text(encoding="utf-8")
    for token in ("設定前の一重項源は $x,y$ に依存せず", "Bell局所因子化を仮定しない", "Q2-2-S"):
        if token not in receiver:
            raise AssertionError(f"Q2-2 receiver policy marker missing: {token}")

def check_verifier_boundary() -> None:
    forbidden_markers = (
        'ROOT / "sections"',
        "ROOT / 'sections'",
        'PROJECT_STATUS.md',
        'README.md',
        'TERMINOLOGY.md',
    )
    offenders: list[str] = []
    for path in sorted((ROOT / "tools").glob("verify_*.py")):
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in forbidden_markers):
            offenders.append(path.name)
    if offenders:
        raise AssertionError(
            "verify_*.py must contain only mathematical/numerical checks; source-contract checks found in: "
            + ", ".join(offenders)
        )


def check_ci_read_only() -> None:
    workflow = ROOT / ".github" / "workflows" / "verify.yml"
    text = workflow.read_text(encoding="utf-8")
    forbidden = ("git push", "git commit", "contents: write")
    hits = [token for token in forbidden if token in text]
    if hits:
        raise AssertionError("CI must be read-only; found: " + ", ".join(hits))


def main() -> None:
    check_sources()
    check_project_status()
    check_r161_path_boundary()
    check_enhancement_targets()
    check_verifier_boundary()
    check_ci_read_only()
    print("source_check_ok")


if __name__ == "__main__":
    main()
