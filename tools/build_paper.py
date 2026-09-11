#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from paper_source import (
    ROOT,
    SECTIONS,
    ordered_appendix_paths,
    parse_source,
    restore_markdown_source,
    validate_github_markdown,
)

TEMPLATE = ROOT / "tools" / "template.tex"

CHAPTER_NUMBERS = tuple(range(1, 10))
PART_TITLES: dict[int, str] = {
    1: "問題設定と共通言語",
    3: "単一量子ビット型操作と測定",
    4: "2論理部分系とBell型統計",
    6: "空間信号と粒子位置",
    8: "総合評価",
}
PART_NUMERALS = {1: "I", 3: "II", 4: "III", 6: "IV", 8: "V"}

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
    38: "reck_et_al1994",
    39: "clements_et_al2016",
    40: "misra_sudarshan1977",
    41: "itano_et_al1990",
    42: "ruseckas_kaulakys2001",
    43: "nielsen2002",
    44: "duerr_et_al2005",
    45: "georgii_tumulka2005",
    46: "jarzynski1997",
    47: "crooks1999",
    48: "seifert2005",
    49: "ehrich_et_al2020",
    50: "esposito2012",
    51: "jarzynski2004",
    52: "sun_et_al2022_classical_optical",
    53: "zhang_sun_zhang2025_qift",
    54: "zhang_sun_zhang2026_universal_analog",
    55: "chen_et_al2026_shor_optical",
    56: "kubo_hashitsume1970",
    57: "brown1963",
    58: "grinstein_koch2005",
}


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
    body = [
        r"\begingroup",
        r"\small",
        r"\begin{thebibliography}{99}",
        r"\addcontentsline{toc}{chapter}{参考文献}",
    ]
    for number in range(1, max(REFERENCE_KEYS) + 1):
        body.append(rf"\bibitem{{{REFERENCE_KEYS[number]}}} {entries[number]}")
    body.extend([r"\end{thebibliography}", r"\endgroup"])
    return "\n\n".join(body)


def pandoc_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        r"\chapter*{概要}",
        r"\addcontentsline{toc}{chapter}{概要}",
        "\n".join(preprocess(overview)),
    ])

    for number in CHAPTER_NUMBERS:
        if number in PART_TITLES:
            chunks.append(r"\part{" + PART_TITLES[number] + "}")
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

    appendix_paths = ordered_appendix_paths()
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
    chunks.extend(["# 概要", "\n".join(preprocess_public(overview))])

    for number in CHAPTER_NUMBERS:
        if number in PART_TITLES:
            chunks.append("# 第" + PART_NUMERALS[number] + "部　" + PART_TITLES[number])
        path = next(SECTIONS.glob(f"{number:02d}_*.md"))
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append("> **位置づけ：** " + status)
        chunks.append("\n".join(preprocess_public(lines)))

    appendix_paths = ordered_appendix_paths()
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
    chunks.extend(["# 参考文献", "\n".join(preprocess_public(references))])
    return "\n\n".join(chunks) + "\n"


def tex_environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        "SOURCE_DATE_EPOCH": "1788998400",
        "FORCE_SOURCE_DATE": "1",
        "TZ": "UTC",
        "TEXINPUTS": "/usr/share/texlive/texmf-dist/tex//:",
        "TFMFONTS": "/usr/share/texlive/texmf-dist/fonts/tfm//:",
        "OPENTYPEFONTS": "/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:",
    })
    return env


def run_command(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=tex_environment(), check=True)


def normalize_pdf_id(path: Path) -> None:
    data = path.read_bytes()
    pdf_string = rb"(?:<[0-9A-Fa-f]+>|\((?:\\.|[^\\)])*\))"
    pattern = re.compile(rb"/ID\[\s*" + pdf_string + rb"\s*" + pdf_string + rb"\s*\]")
    placeholder = b"/ID[<" + b"0" * 32 + b"><" + b"0" * 32 + b">]"
    normalized, count = pattern.subn(placeholder, data)
    if count == 0:
        return
    if count != 1:
        raise RuntimeError(f"expected at most one PDF trailer ID in {path}, found {count}")
    stable_id = hashlib.sha256(normalized).hexdigest()[:32].encode("ascii")
    stable = b"/ID[<" + stable_id + b"><" + stable_id + b">]"
    path.write_bytes(normalized.replace(placeholder, stable, 1))


def build(output_dir: Path) -> tuple[Path, Path, Path]:
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    work = (ROOT / "build" / "latex") if output_dir == ROOT else (output_dir / "latex")
    work.mkdir(parents=True, exist_ok=True)

    paper_md = output_dir / "paper.md"
    main_tex = output_dir / "main.tex"
    pdf = output_dir / "paper.pdf"

    for source in sorted(SECTIONS.glob("*.md")):
        validate_github_markdown(source, source.read_text(encoding="utf-8"))

    paper_text = combined_markdown()
    validate_github_markdown(paper_md, paper_text)
    paper_md.write_text(paper_text, encoding="utf-8")

    pandoc_source = work / "paper.md"
    pandoc_source.write_text(markdown_for_pandoc(pandoc_markdown()), encoding="utf-8")
    body = work / "body.tex"
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
    main_tex.write_text(template.replace("$body$", body.read_text(encoding="utf-8")), encoding="utf-8")

    latex_run = Path(tempfile.mkdtemp(prefix="quantum-wakaran-neko-latex-"))
    try:
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={latex_run}",
            str(main_tex),
        ]
        for _ in range(3):
            run_command(command, cwd=ROOT)
        shutil.copy2(latex_run / "main.pdf", work / "main.pdf")
        normalize_pdf_id(work / "main.pdf")
    finally:
        log = latex_run / "main.log"
        if log.exists():
            shutil.copy2(log, work / "main.log")
        shutil.rmtree(latex_run)

    shutil.copy2(work / "main.pdf", pdf)
    print(paper_md)
    print(main_tex)
    print(pdf)
    return paper_md, main_tex, pdf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate paper.md, main.tex and paper.pdf")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT,
        help="output directory (default: repository root)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build(args.output_dir)
