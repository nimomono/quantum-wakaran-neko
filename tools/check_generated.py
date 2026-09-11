#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN_LOG = re.compile(
    r"Citation .* undefined|Reference .* undefined|Overfull|Underfull|Fatal error|Missing character"
)


def command_output(args: list[str]) -> str:
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def pdf_text(path: Path) -> str:
    with tempfile.NamedTemporaryFile(suffix=".txt") as handle:
        subprocess.run(["pdftotext", "-layout", str(path), handle.name], check=True)
        return Path(handle.name).read_text(encoding="utf-8", errors="replace")


def pdfinfo_field(path: Path, field: str) -> str:
    info = command_output(["pdfinfo", str(path)])
    prefix = field + ":"
    for line in info.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    raise AssertionError(f"{path}: pdfinfo field {field!r} is missing")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", nargs="?", type=Path, default=ROOT / "build" / "ci")
    args = parser.parse_args()
    generated = args.output_dir.resolve()

    for name in ("paper.md", "main.tex", "paper.pdf"):
        if not (generated / name).is_file():
            raise AssertionError(f"generated artifact missing: {generated / name}")

    for name in ("paper.md", "main.tex"):
        committed = ROOT / name
        rebuilt = generated / name
        if committed.read_bytes() != rebuilt.read_bytes():
            raise AssertionError(f"generated {name} differs from committed {name}")

    committed_pdf = ROOT / "paper.pdf"
    rebuilt_pdf = generated / "paper.pdf"
    if pdf_text(committed_pdf) != pdf_text(rebuilt_pdf):
        raise AssertionError("regenerated PDF text differs from committed paper.pdf")
    for field in ("Pages", "Page size"):
        if pdfinfo_field(committed_pdf, field) != pdfinfo_field(rebuilt_pdf, field):
            raise AssertionError(f"regenerated PDF {field} differs from committed paper.pdf")

    log = generated / "latex" / "main.log"
    if not log.is_file():
        raise AssertionError(f"LaTeX log missing: {log}")
    log_text = log.read_text(encoding="utf-8", errors="replace")
    match = FORBIDDEN_LOG.search(log_text)
    if match:
        raise AssertionError(f"forbidden LaTeX warning remains: {match.group(0)}")

    print("generated_artifacts_check_ok")


if __name__ == "__main__":
    main()
