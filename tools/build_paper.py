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
    19: "uhlenbeck_ornstein1930",
    20: "wallstrom1994",
    21: "price_wharton2023",
    22: "price_wharton2024",
    23: "argaman2010",
    24: "hossenfelder_palmer2020",
    25: "thooft2016",
    26: "leonard2014",
    27: "chen_georgiou_pavon2016",
    28: "rauch_tung_striebel1965",
    29: "waalkens_schubert_wiggins2008",
    30: "kramers1940",
    31: "chandler1978",
    32: "sigman_whitt2019",
    33: "fuchs_goldt_seifert2016",
    34: "evans_majumdar_schehr2020",
    35: "knorst_lopes2024",
    36: "wilson_et_al2021",
    37: "leonard_roelly_zambrini2014",
    38: "fine1982",
    39: "asmussen2003",
    40: "marchiori_deaguiar2011",
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


def preprocess(lines: list[str]) -> list[str]:
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
            entries[int(match.group(1))] = match.group(2)
    body = [r"\begin{thebibliography}{99}", r"\addcontentsline{toc}{chapter}{参考文献}"]
    for number in range(1, max(REFERENCE_KEYS) + 1):
        body.append(rf"\bibitem{{{REFERENCE_KEYS[number]}}} {entries[number]}")
    body.append(r"\end{thebibliography}")
    return "\n\n".join(body)


def combined_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        r"\chapter*{概要}",
        r"\addcontentsline{toc}{chapter}{概要}",
        "\n".join(preprocess(overview)),
    ])

    for number in range(1, 9):
        if number == 2:
            chunks.append(r"\part{有限調和 Gaussian 中核の Nelson 極限}")
        if number == 5:
            chunks.append(r"\part{2境界統計原理と2モード台帳による Bell 型統計}")
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
    PAPER_MD.write_text(combined_markdown(), encoding="utf-8")

    pandoc_source = WORK / "paper.md"
    pandoc_source.write_text(
        markdown_for_pandoc(PAPER_MD.read_text(encoding="utf-8")),
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
