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

    # These checks describe the source format, not any current theorem snapshot.
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
        fixed = text.split("### 固定目標一覧", 1)[1].split("### 現在地", 1)[0]
    except IndexError as exc:
        raise AssertionError("PROJECT_STATUS fixed-goal/current-position boundary is missing") from exc

    # Fixed goals should state physical targets without binding them to current M/R implementation IDs.
    hit = re.search(r"(?<![A-Za-z])[MR]\d+", fixed)
    if hit:
        raise AssertionError(f"fixed-goal block contains implementation/result ID: {hit.group(0)}")

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


def check_verifier_boundary() -> None:
    # Numerical/mathematical verifiers must not double as prose/file-layout guards.
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



def check_measurement_spine_residuals() -> None:
    checks = {
        "sections/A8_m47_hopf_preparation.md": ("R164/R190/R179/R170", "R170で選択機構"),
        "sections/A11_common_collision_bath_thermodynamics.md": ("Q1・Q2の静的測定",),
        "sections/08_errors_resources_open_targets.md": ("R164/R190/R179/R170の静的選択",),
        "sections/02_common_canonical_modules.md": ("Q1/Q2のR190反復再混合",),
    }
    for rel, forbidden in checks.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        hits = [token for token in forbidden if token in text]
        if hits:
            raise AssertionError(f"stale measurement-spine wording in {rel}: {hits}")


def main() -> None:
    check_sources()
    check_project_status()
    check_verifier_boundary()
    check_ci_read_only()
    check_measurement_spine_residuals()
    print("source_check_ok")


if __name__ == "__main__":
    main()
