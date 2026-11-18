#!/usr/bin/env python3
"""第2期研究のsections/から公開Markdown・TeX・PDFを生成する。"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from paper_source import ROOT, pandoc_markdown, public_markdown

TEMPLATE = ROOT / "tools" / "template.tex"


def environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        "SOURCE_DATE_EPOCH": "1794960000",
        "FORCE_SOURCE_DATE": "1",
        "TZ": "UTC",
    })
    return env


def run(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=environment(), check=True)


def normalize_pdf_id(path: Path) -> None:
    data = path.read_bytes()
    pdf_string = rb"(?:<[0-9A-Fa-f]+>|\((?:\\.|[^\\)])*\))"
    pattern = re.compile(rb"/ID\[\s*" + pdf_string + rb"\s*" + pdf_string + rb"\s*\]")
    zero = b"/ID[<" + b"0" * 32 + b"><" + b"0" * 32 + b">]"
    normalized, count = pattern.subn(zero, data)
    if count > 1:
        raise RuntimeError("ambiguous PDF ID")
    if count == 1:
        stable_id = hashlib.sha256(normalized).hexdigest()[:32].encode("ascii")
        final = b"/ID[<" + stable_id + b"><" + stable_id + b">]"
        path.write_bytes(normalized.replace(zero, final, 1))


def build(output_dir: Path) -> tuple[Path, Path, Path]:
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    work = ROOT / "build" / "latex" if output_dir == ROOT else output_dir / "latex"
    work.mkdir(parents=True, exist_ok=True)

    md = output_dir / "paper.md"
    tex = output_dir / "main.tex"
    pdf = output_dir / "paper.pdf"
    md.write_text(public_markdown(), encoding="utf-8")

    intermediate = work / "source.md"
    intermediate.write_text(pandoc_markdown(), encoding="utf-8")
    body = work / "body.tex"
    run([
        "pandoc", "--from=markdown+raw_tex", "--to=latex",
        "--top-level-division=chapter", "--wrap=none",
        "--output", str(body), str(intermediate),
    ])
    content = body.read_text(encoding="utf-8")
    # 00_から始める場合、第0章として番号を揃える。
    content = r"\setcounter{chapter}{-1}" + "\n" + content
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count("$body$") != 1:
        raise ValueError("expected exactly one $body$ placeholder")
    tex.write_text(template.replace("$body$", content), encoding="utf-8")

    temporary = Path(tempfile.mkdtemp(prefix="quantum-rewrite-xelatex-"))
    try:
        command = [
            "xelatex", "-interaction=nonstopmode", "-halt-on-error",
            f"-output-directory={temporary}", str(tex),
        ]
        for _ in range(3):
            run(command, cwd=ROOT)
        output_pdf = temporary / "main.pdf"
        shutil.copyfile(output_pdf, work / "main.pdf")
        normalize_pdf_id(work / "main.pdf")
    finally:
        if (temporary / "main.log").exists():
            shutil.copy2(temporary / "main.log", work / "main.log")
        shutil.rmtree(temporary)

    shutil.copyfile(work / "main.pdf", pdf)
    for result in (md, tex, pdf):
        print(result)
    return md, tex, pdf


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()
