#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from paper_source import (
    ROOT,
    SECTIONS,
    chapter_paths,
    ordered_appendix_paths,
    parse_source,
    result_declarations,
    validate_github_markdown,
)

STATUS_VALUES = {"達成", "条件付き達成", "部分達成", "未達"}
ENHANCEMENT_STATUS_VALUES = STATUS_VALUES | {"未監査", "—"}
QID_PATTERN = r"Q[123]-\d+[A-Z]?"
Q_STATUS_ROW = re.compile(
    rf"^\|\s*(?P<qid>{QID_PATTERN})\s*\|\s*(?P<status>達成|条件付き達成|部分達成|未達)\s*\|"
)


def section_between(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError as exc:
        raise AssertionError(f"document boundary is missing: {start!r} .. {end!r}") from exc


def table_qids(text: str) -> set[str]:
    return {
        match.group(1)
        for match in re.finditer(rf"^\|\s*({QID_PATTERN})\s*\|", text, re.MULTILINE)
    }


def check_sources() -> None:
    sources = sorted(SECTIONS.glob("*.md"))
    if not sources:
        raise AssertionError("sections/*.md is empty")

    chapter_paths()
    ordered_appendix_paths()
    for path in sources:
        meta, _ = parse_source(path)
        validate_github_markdown(path, path.read_text(encoding="utf-8"))
        if path.name not in {"00_overview_and_contents.md", "90_references.md"} and not meta.get("title"):
            raise AssertionError(f"{path}: @title is missing")

    declarations: dict[str, list[str]] = defaultdict(list)
    for path in sources:
        for result_id in result_declarations(path):
            declarations[result_id].append(path.relative_to(ROOT).as_posix())
    duplicates = {key: value for key, value in declarations.items() if len(value) != 1}
    if duplicates:
        details = "; ".join(f"{key}={','.join(value)}" for key, value in sorted(duplicates.items()))
        raise AssertionError("active result declarations are not unique: " + details)


def check_project_status() -> set[str]:
    path = ROOT / "PROJECT_STATUS.md"
    text = path.read_text(encoding="utf-8")

    fixed = section_between(
        text,
        "### 固定目標一覧",
        "#### Q3-1からQ3-6の達成判定の補足",
    )
    fixed_ids = table_qids(fixed)
    if not fixed_ids:
        raise AssertionError("fixed-goal IDs were not found")

    implementation_id = re.search(r"(?<![A-Za-z])[MR]\d+", fixed)
    if implementation_id:
        raise AssertionError(
            "fixed-goal definition contains implementation/result ID: "
            + implementation_id.group(0)
        )

    rows: dict[str, list[str]] = defaultdict(list)
    for line in text.splitlines():
        match = Q_STATUS_ROW.match(line)
        if match:
            rows[match.group("qid")].append(match.group("status"))
    if not rows:
        raise AssertionError("PROJECT_STATUS status rows were not found")

    inconsistent = {key: values for key, values in rows.items() if len(set(values)) != 1}
    if inconsistent:
        raise AssertionError(f"conflicting Q status rows: {inconsistent}")

    unknown = set(rows) - fixed_ids
    if unknown:
        raise AssertionError(f"status rows contain unknown fixed-goal IDs: {sorted(unknown)}")

    return fixed_ids


def check_enhancement_targets(fixed_ids: set[str]) -> None:
    path = ROOT / "ENHANCEMENT_TARGETS.md"
    text = path.read_text(encoding="utf-8")
    current = section_between(
        text,
        "## 強化目標の現在地表",
        "## 既存の実装強化課題との関係",
    )

    rows: dict[str, list[str]] = {}
    for line in current.splitlines():
        if not re.match(rf"^\|\s*{QID_PATTERN}\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            raise AssertionError(f"malformed enhancement row: {line}")
        qid, values = cells[0], cells[1:]
        if qid in rows:
            raise AssertionError(f"duplicate enhancement row: {qid}")
        invalid = set(values) - ENHANCEMENT_STATUS_VALUES
        if invalid:
            raise AssertionError(
                f"unsupported enhancement status for {qid}: {sorted(invalid)}"
            )
        rows[qid] = values

    if set(rows) != fixed_ids:
        raise AssertionError(
            "enhancement target IDs differ from fixed goals: "
            f"missing={sorted(fixed_ids-set(rows))}, "
            f"extra={sorted(set(rows)-fixed_ids)}"
        )


def verifier_paths() -> list[Path]:
    required = sorted((ROOT / "tools").glob("verify_*.py"))
    candidate_root = ROOT / "tools" / "candidate_checks"
    candidate = sorted(candidate_root.glob("verify_*.py")) if candidate_root.is_dir() else []
    return required + candidate


def check_verifier_boundary() -> None:
    forbidden_markers = (
        'ROOT / "sections"',
        "ROOT / 'sections'",
        "PROJECT_STATUS.md",
        "ENHANCEMENT_TARGETS.md",
        "README.md",
        "TERMINOLOGY.md",
    )
    offenders: list[str] = []
    for path in verifier_paths():
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in forbidden_markers):
            offenders.append(path.relative_to(ROOT).as_posix())
    if offenders:
        raise AssertionError(
            "physics verifiers must contain only mathematical/numerical checks; "
            "source-contract checks found in: " + ", ".join(offenders)
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
    fixed_ids = check_project_status()
    check_enhancement_targets(fixed_ids)
    check_verifier_boundary()
    check_ci_read_only()
    print("source_check_ok")


if __name__ == "__main__":
    main()
