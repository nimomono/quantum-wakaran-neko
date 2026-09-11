#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"

THEOREM_LABELS = {
    "theorem": "定理",
    "proposition": "命題",
    "lemma": "補題",
    "corollary": "系",
    "proof": "証明",
}

APPENDIX_FILENAME = re.compile(r"A(\d+)_.*\.md")
RESULT_DECLARATION = re.compile(r"\*\*(?:定理|命題|補題|系)（(R\d+[A-Z]?)：")


def parse_source(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    while lines and lines[0].startswith("@"):
        if ":" not in lines[0]:
            raise ValueError(f"{path}: malformed metadata line: {lines[0]}")
        key, value = lines.pop(0)[1:].split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, lines


def chapter_paths() -> list[Path]:
    paths: list[Path] = []
    for number in range(1, 10):
        matches = sorted(SECTIONS.glob(f"{number:02d}_*.md"))
        if len(matches) != 1:
            raise ValueError(
                f"chapter {number:02d}: expected exactly one source, found {len(matches)}"
            )
        paths.append(matches[0])
    return paths


def ordered_appendix_paths() -> list[Path]:
    numbered: list[tuple[int, Path]] = []
    for path in SECTIONS.glob("A*_*.md"):
        match = APPENDIX_FILENAME.fullmatch(path.name)
        if match:
            numbered.append((int(match.group(1)), path))

    numbers = [number for number, _ in numbered]
    if len(numbers) != len(set(numbers)):
        raise ValueError("duplicate appendix number")

    ordered = sorted(numbered)
    for number, path in ordered:
        meta, _ = parse_source(path)
        if not 1 <= number <= 26:
            raise ValueError(f"unsupported appendix number: {path.name}")
        expected = chr(ord("A") + number - 1)
        if meta.get("number") != expected or meta.get("chapter") != "付録":
            raise ValueError(
                f"{path.name}: appendix metadata must be "
                f"@number: {expected} and @chapter: 付録"
            )
    return [path for _, path in ordered]


def restore_markdown_source(lines: list[str]) -> list[str]:
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        start = re.fullmatch(
            r"<!-- theorem-start:(theorem|proposition|lemma|corollary|proof) -->",
            line.strip(),
        )
        if start:
            environment = start.group(1)
            if index + 1 >= len(lines):
                raise ValueError(f"missing theorem label after {line}")
            visible = lines[index + 1].strip()
            label = THEOREM_LABELS[environment]
            plain = f"**{label}**"
            titled_prefix = f"**{label}（"
            if visible == plain:
                title = ""
            elif visible.startswith(titled_prefix) and visible.endswith("）**"):
                title = visible[len(titled_prefix):-3]
            else:
                raise ValueError(f"invalid theorem label: {visible}")
            begin = rf"\begin{{{environment}}}"
            if title:
                begin += f"[{title}]"
            output.append(begin)
            index += 2
            continue

        end = re.fullmatch(
            r"<!-- theorem-end:(theorem|proposition|lemma|corollary|proof) -->",
            line.strip(),
        )
        if end:
            output.append(rf"\end{{{end.group(1)}}}")
            index += 1
            continue

        output.append(line)
        index += 1
    return output


def validate_github_markdown(path: Path, text: str) -> None:
    if path.exists() and re.search(rb"[\x00-\x08\x0b\x0c\x0d\x0e-\x1f]", path.read_bytes()):
        raise ValueError(f"{path}: 規約外の制御文字を検出")
    forbidden = {
        "独自数式マクロ": r"\\(?:dd|E|R|Tr|GM|Nel)(?![A-Za-z])",
        "生の定理環境": (
            r"\\(?:begin|end)\{"
            r"(?:theorem|proposition|lemma|corollary|proof|statusbox|thebibliography)"
            r"\}"
        ),
        "数式外のTeX命令": (
            r"\\(?:chapter\*?|part|appendix|addcontentsline|cite|bibitem|url)\b"
        ),
        "規約外の数式区切り": r"\\\(|\\\[|\$\$",
        "数式命令内の日本語": (
            r"\\(?:text|mathrm|boxed)\{[^{}]*[ぁ-んァ-ヶ一-龠々〆ヵヶ][^{}]*\}"
        ),
    }
    errors = [name for name, pattern in forbidden.items() if re.search(pattern, text)]
    for environment in THEOREM_LABELS:
        starts = text.count(f"<!-- theorem-start:{environment} -->")
        ends = text.count(f"<!-- theorem-end:{environment} -->")
        if starts != ends:
            errors.append(f"{environment} 境界の不一致")
    if errors:
        raise ValueError(f"{path}: " + "、".join(errors))


def result_declarations(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return RESULT_DECLARATION.findall(text)
