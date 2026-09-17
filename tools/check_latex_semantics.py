#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from latex_log import classify_latex_log


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("log", type=Path)
    args = parser.parse_args()

    if not args.log.is_file():
        raise SystemExit(f"LaTeX log missing: {args.log}")

    text = args.log.read_text(encoding="utf-8", errors="replace")
    hard, _ = classify_latex_log(text)

    if hard:
        print(f"latex_semantic_errors ({len(hard)} findings)")
        for finding in hard:
            print(f"ERROR [{finding.kind}] {finding.message}")
        raise SystemExit(1)

    print("latex_semantics_ok")


if __name__ == "__main__":
    main()
