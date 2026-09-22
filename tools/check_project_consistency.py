#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from paper_source import ROOT, SECTIONS, result_declarations

RESULT_ID = re.compile(r"(?<![A-Za-z0-9_])R\d+[A-Z]?(?![A-Za-z0-9_])")
RESULT_RANGE = re.compile(
    r"R(?P<n1>\d+)(?P<s1>[A-Z]?)--R(?P<n2>\d+)(?P<s2>[A-Z]?)"
)
GOAL_ID = re.compile(r"Q[123]-\d+[A-Z]?")


def between(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError as exc:
        raise AssertionError(f"required document boundary is missing: {start!r} -> {end!r}") from exc


def table_cells(line: str) -> list[str]:
    if not line.lstrip().startswith("|"):
        return []
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def expand_result_ids(text: str) -> set[str]:
    ids: set[str] = set()
    ranges: list[tuple[int, int]] = []

    for match in RESULT_RANGE.finditer(text):
        ranges.append(match.span())
        n1, n2 = int(match.group("n1")), int(match.group("n2"))
        s1, s2 = match.group("s1"), match.group("s2")
        if n1 == n2 and s1 and s2 and ord(s1) <= ord(s2):
            ids.update(f"R{n1}{chr(code)}" for code in range(ord(s1), ord(s2) + 1))
        elif not s1 and not s2 and n1 <= n2 and n2 - n1 <= 100:
            ids.update(f"R{number}" for number in range(n1, n2 + 1))
        else:
            ids.add(f"R{n1}{s1}")
            ids.add(f"R{n2}{s2}")

    masked = list(text)
    for start, end in ranges:
        masked[start:end] = " " * (end - start)
    ids.update(RESULT_ID.findall("".join(masked)))
    return ids


def active_result_ids() -> set[str]:
    paths: dict[str, list[str]] = defaultdict(list)
    for path in sorted(SECTIONS.glob("*.md")):
        for result_id in result_declarations(path):
            paths[result_id].append(path.relative_to(ROOT).as_posix())
    duplicates = {key: value for key, value in paths.items() if len(value) != 1}
    if duplicates:
        raise AssertionError(f"active result declarations are not unique: {duplicates}")
    return set(paths)


def status_result_ids(text: str) -> set[str]:
    block = between(text, "## 現行結果の導出状態", "## 物理的解釈と境界")
    rows: dict[str, int] = defaultdict(int)
    for line in block.splitlines():
        cells = table_cells(line)
        if not cells or not re.fullmatch(r"R\d+[A-Z]?", cells[0]):
            continue
        rows[cells[0]] += 1
    duplicates = sorted(key for key, count in rows.items() if count != 1)
    if duplicates:
        raise AssertionError(f"PROJECT_STATUS current-result rows are not unique: {duplicates}")
    return set(rows)


def fixed_goal_dependency_ids(text: str) -> set[str]:
    block = between(
        text,
        "### 現在地",
        "## 現行模型・物理実装層・手順の運用状態",
    )
    dependencies: set[str] = set()
    for line in block.splitlines():
        cells = table_cells(line)
        if not cells or not GOAL_ID.fullmatch(cells[0]):
            continue
        dependencies.update(expand_result_ids(line))
    return dependencies


def retired_result_ids(text: str) -> set[str]:
    retired: set[str] = set()
    for line in text.splitlines():
        cells = table_cells(line)
        if not cells:
            continue
        first = cells[0]
        if not RESULT_ID.search(first) and not RESULT_RANGE.search(first):
            continue
        retired.update(expand_result_ids(first))
    return retired


def markdown_note_paths(text: str) -> set[Path]:
    paths: set[Path] = set()
    for token in re.findall(r"`([^`]+\.md)`", text):
        candidate = Path(token)
        if candidate.is_absolute():
            continue
        if candidate.parts and candidate.parts[0] in {"notes", "sections"}:
            paths.add(ROOT / candidate)
        elif len(candidate.parts) == 1:
            paths.add(ROOT / "notes" / candidate)
    return paths


def check_note_references() -> None:
    index_text = (ROOT / "notes" / "superseded_result_index.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "notes" / "README.md").read_text(encoding="utf-8")
    missing = sorted(
        str(path.relative_to(ROOT))
        for path in markdown_note_paths(index_text) | markdown_note_paths(readme_text)
        if not path.exists()
    )
    if missing:
        raise AssertionError("historical note references point to missing files: " + ", ".join(missing))


def main() -> None:
    project_status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    retired_index = (ROOT / "notes" / "superseded_result_index.md").read_text(encoding="utf-8")

    declared = active_result_ids()
    listed = status_result_ids(project_status)
    if declared != listed:
        raise AssertionError(
            "active theorem declarations and PROJECT_STATUS current-result rows differ: "
            f"missing_in_status={sorted(declared-listed)}, "
            f"missing_in_sections={sorted(listed-declared)}"
        )

    dependencies = fixed_goal_dependency_ids(project_status)
    unknown_dependencies = dependencies - declared
    if unknown_dependencies:
        raise AssertionError(
            "fixed-goal current-position rows reference non-active results: "
            + ", ".join(sorted(unknown_dependencies))
        )

    retired = retired_result_ids(retired_index)
    reused = declared & retired
    if reused:
        raise AssertionError(
            "result IDs occur in both active declarations and retired index: "
            + ", ".join(sorted(reused))
        )

    check_note_references()
    print(
        "project_consistency_ok "
        f"active={len(declared)} dependencies={len(dependencies)} retired={len(retired)}"
    )


if __name__ == "__main__":
    main()
