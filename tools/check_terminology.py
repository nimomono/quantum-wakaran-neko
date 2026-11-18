#!/usr/bin/env python3
"""旧理論の識別子が新しい本文へ無意識に混入していないかを確認する。"""
from __future__ import annotations

import re
from paper_source import chapter_paths

PATTERN = re.compile(r"(?<!\w)(?:M\d+|R\d+[A-Z]?|Q[123]-\d+[A-Z]?)(?!\w)")


def main() -> None:
    offenders = [path.name for path in chapter_paths() if PATTERN.search(path.read_text(encoding="utf-8"))]
    if offenders:
        raise SystemExit("legacy identifiers in active source: " + ", ".join(offenders))
    print("terminology_lint_ok")


if __name__ == "__main__":
    main()
