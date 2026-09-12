#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from latex_log import classify_latex_log

ROOT = Path(__file__).resolve().parent.parent


def annotation(message: str) -> str:
    return message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "log",
        nargs="?",
        type=Path,
        default=ROOT / "build" / "ci" / "latex" / "main.log",
    )
    args = parser.parse_args()
    log = args.log.resolve()
    if not log.is_file():
        raise AssertionError(f"LaTeX log missing: {log}")

    hard, style = classify_latex_log(log.read_text(encoding="utf-8", errors="replace"))
    for finding in style:
        location = f" source line {finding.source_line}" if finding.source_line else ""
        print(f"::warning title=LaTeX {finding.kind}::{annotation(finding.message + location)}")

    overfull_amounts = [f.amount_pt for f in style if f.kind == "overfull" and f.amount_pt is not None]
    maximum = max(overfull_amounts, default=0.0)
    print(
        "typeset_lint_ok "
        f"warnings={len(style)} overfull={sum(f.kind == 'overfull' for f in style)} "
        f"underfull={sum(f.kind == 'underfull' for f in style)} max_overfull_pt={maximum:.3f} "
        f"hard_findings_seen={len(hard)}"
    )


if __name__ == "__main__":
    main()
