#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"
WORK = ROOT / "build" / "latex"
FMT_DIR = ROOT / "build" / "texfmt"
TEMPLATE = ROOT / "tools" / "template.tex"
PAPER_MD = ROOT / "paper.md"
MAIN_TEX = ROOT / "main.tex"
PDF = ROOT / "paper.pdf"

THEOREM_LABELS = {
    "theorem": "定理",
    "proposition": "命題",
    "lemma": "補題",
    "corollary": "系",
    "proof": "証明",
}

PART_TITLES: dict[int, str] = {}

REFERENCE_KEYS = {
    1: "bell1964",
    2: "chsh1969",
    3: "nelson1966",
    4: "guerra_morato1983",
    5: "yasue1981",
    6: "zambrini1986",
    7: "wharton2010",
    8: "wharton_argaman2020",
    9: "hall2010",
    10: "leifer_pusey2017",
    11: "wood_spekkens2015",
    12: "ford1965",
    13: "mori1965",
    14: "zwanzig1973",
    15: "jamison1974",
    16: "doob1957",
    17: "landauer1961",
    18: "bennett1982",
    19: "wallstrom1994",
    20: "price_wharton2023",
    21: "price_wharton2024",
    22: "argaman2010",
    23: "hossenfelder_palmer2020",
    24: "thooft2016",
    25: "leonard2014",
    26: "chen_georgiou_pavon2016",
    27: "rauch_tung_striebel1965",
    28: "fuchs_goldt_seifert2016",
    29: "evans_majumdar_schehr2020",
    30: "knorst_lopes2024",
    31: "wilson_et_al2021",
    32: "leonard_roelly_zambrini2014",
    33: "marchiori_deaguiar2011",
    34: "heslot1985",
    35: "briggs_eisfeld2012",
    36: "briggs_eisfeld2013",
    37: "skinner2013",
}


def parse_source(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    while lines and lines[0].startswith("@"):
        key, value = lines.pop(0)[1:].split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, lines


def citation_keys(spec: str) -> list[str]:
    numbers: list[int] = []
    for item in spec.split(","):
        if "--" in item:
            start, end = (int(value) for value in item.split("--", 1))
            numbers.extend(range(start, end + 1))
        else:
            numbers.append(int(item))
    return [REFERENCE_KEYS[number] for number in numbers]


def replace_citations(text: str) -> str:
    pattern = re.compile(r"\[((?:\d+)(?:(?:--|,)\d+)*)\]")

    def replacement(match: re.Match[str]) -> str:
        try:
            keys = citation_keys(match.group(1))
        except (KeyError, ValueError):
            return match.group(0)
        return r"\cite{" + ",".join(keys) + "}"

    return pattern.sub(replacement, text)



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
    errors = [
        name for name, pattern in forbidden.items()
        if re.search(pattern, text)
    ]
    for environment in THEOREM_LABELS:
        starts = text.count(f"<!-- theorem-start:{environment} -->")
        ends = text.count(f"<!-- theorem-end:{environment} -->")
        if starts != ends:
            errors.append(f"{environment} 境界の不一致")
    if errors:
        raise ValueError(f"{path}: " + "、".join(errors))


def preprocess(lines: list[str]) -> list[str]:
    lines = restore_markdown_source(lines)
    output: list[str] = []
    in_math = False
    for line in lines:
        stripped = line.strip()
        if not in_math and stripped in {"$$", "```math"}:
            in_math = True
            output.append(line)
            continue
        if in_math and stripped in {"$$", "```"}:
            in_math = False
            output.append(line)
            continue
        if in_math:
            output.append(line)
            continue
        heading = re.match(r"^(#{2,3})\s+(?:\d+|[A-Z])(?:\.\d+)*\s+(.*)$", line)
        if heading:
            line = f"{heading.group(1)} {heading.group(2)}"
        output.append(replace_citations(line))
    return output


def preprocess_public(lines: list[str]) -> list[str]:
    output: list[str] = []
    in_math = False
    for line in lines:
        stripped = line.strip()
        if not in_math and stripped == "```math":
            in_math = True
            output.append(line)
            continue
        if in_math and stripped == "```":
            in_math = False
            output.append(line)
            continue
        if not in_math:
            heading = re.match(r"^(#{2,3})\s+(?:\d+|[A-Z])(?:\.\d+)*\s+(.*)$", line)
            if heading:
                line = f"{heading.group(1)} {heading.group(2)}"
        output.append(line)
    if in_math:
        raise ValueError("unclosed math fence")
    return output


def markdown_for_pandoc(text: str) -> str:
    output: list[str] = []
    in_math = False
    for line in text.splitlines():
        stripped = line.strip()
        if not in_math and stripped == "```math":
            in_math = True
            output.append("$$")
            continue
        if in_math and stripped == "```":
            in_math = False
            output.append("$$")
            continue
        if not in_math and re.match(r"^#{1,6}\s+", line):
            for github_math, tex_math in (
                ("−1/<i>T</i>", "$-1/T$"),
                ("<i>C</i><sup>1</sup>", "$C^1$"),
                ("<i>E</i><sub>∗</sub>", "$E_*$"),
            ):
                line = line.replace(github_math, tex_math)
        output.append(line)
    if in_math:
        raise ValueError("unclosed math fence")
    pandoc_text = "\n".join(output) + "\n"
    return re.sub(
        r"(?m)^\$\$\n\n(\\end\{(?:theorem|proof)\})$",
        lambda match: "$$\n" + match.group(1),
        pandoc_text,
    )


def bibliography_tex() -> str:
    _, lines = parse_source(SECTIONS / "90_references.md")
    entries: dict[int, str] = {}
    for line in lines:
        match = re.match(r"^- \[(\d+)\]\s+(.*)$", line)
        if match:
            entry = re.sub(
                r"<(https?://[^ >]+)>",
                lambda url: r"\url{" + url.group(1) + "}",
                match.group(2),
            )
            entries[int(match.group(1))] = entry
    body = [r"\begin{thebibliography}{99}", r"\addcontentsline{toc}{chapter}{参考文献}"]
    for number in range(1, max(REFERENCE_KEYS) + 1):
        body.append(rf"\bibitem{{{REFERENCE_KEYS[number]}}} {entries[number]}")
    body.append(r"\end{thebibliography}")
    return "\n\n".join(body)


def pandoc_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        r"\chapter*{概要}",
        r"\addcontentsline{toc}{chapter}{概要}",
        "\n".join(preprocess(overview)),
    ])

    for number in range(1, 8):
        path = next(SECTIONS.glob(f"{number:02d}_*.md"))
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append(
                "\\begin{statusbox}\n"
                + "位置づけ：" + status + "\n"
                + "\\end{statusbox}"
            )
        chunks.append("\n".join(preprocess(lines)))

    appendix_paths = sorted(SECTIONS.glob("A?_*.md"))
    if appendix_paths:
        chunks.append(r"\appendix")
    for path in appendix_paths:
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append(
                "\\begin{statusbox}\n"
                + "位置づけ：" + status + "\n"
                + "\\end{statusbox}"
            )
        chunks.append("\n".join(preprocess(lines)))

    chunks.append(bibliography_tex())
    return "\n\n".join(chunks) + "\n"


def combined_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        "# 概要",
        "\n".join(preprocess_public(overview)),
    ])

    for number in range(1, 8):
        if number in PART_TITLES:
            chunks.append("# " + PART_TITLES[number])
        path = next(SECTIONS.glob(f"{number:02d}_*.md"))
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append("> **位置づけ：** " + status)
        chunks.append("\n".join(preprocess_public(lines)))

    appendix_paths = sorted(SECTIONS.glob("A?_*.md"))
    if appendix_paths:
        chunks.append("# 付録")
    for path in appendix_paths:
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append("> **位置づけ：** " + status)
        chunks.append("\n".join(preprocess_public(lines)))

    _, references = parse_source(SECTIONS / "90_references.md")
    chunks.extend([
        "# 参考文献",
        "\n".join(preprocess_public(references)),
    ])
    return "\n\n".join(chunks) + "\n"


def run_command(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=tex_environment(), check=True)


def tex_environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        "TEXINPUTS": "/usr/share/texlive/texmf-dist/tex//:",
        "TFMFONTS": "/usr/share/texlive/texmf-dist/fonts/tfm//:",
        "OPENTYPEFONTS": "/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:",
    })
    return env


def ensure_xelatex_format() -> Path:
    fmt = FMT_DIR / "xelatex.fmt"
    if fmt.exists():
        return fmt
    FMT_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["xetex", "-ini", "-etex", "xelatex.ini"],
        cwd=FMT_DIR,
        env=tex_environment(),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return fmt


def build() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    for source in sorted(SECTIONS.glob("*.md")):
        validate_github_markdown(source, source.read_text(encoding="utf-8"))

    paper_text = combined_markdown()
    validate_github_markdown(PAPER_MD, paper_text)
    PAPER_MD.write_text(paper_text, encoding="utf-8")

    pandoc_source = WORK / "paper.md"
    pandoc_source.write_text(
        markdown_for_pandoc(pandoc_markdown()),
        encoding="utf-8",
    )
    body = WORK / "body.tex"
    run_command([
        "pandoc",
        "--from=markdown+raw_tex",
        "--to=latex",
        "--top-level-division=chapter",
        "--wrap=none",
        "--output", str(body),
        str(pandoc_source),
    ])

    template = TEMPLATE.read_text(encoding="utf-8")
    MAIN_TEX.write_text(template.replace("$body$", body.read_text(encoding="utf-8")), encoding="utf-8")

    fmt = ensure_xelatex_format()
    for _ in range(3):
        run_command([
            "xetex",
            f"-fmt={fmt}",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={WORK}",
            str(MAIN_TEX),
        ], cwd=ROOT)

    built = WORK / "main.pdf"
    shutil.copy2(built, PDF)
    print(PAPER_MD)
    print(MAIN_TEX)
    print(PDF)


if __name__ == "__main__":
    build()
