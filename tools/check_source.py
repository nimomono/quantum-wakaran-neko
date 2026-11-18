#!/usr/bin/env python3
"""第2期研究の原稿形式と公開本文の独立性を検査する。"""
from __future__ import annotations

import re
from pathlib import Path

from paper_source import ROOT, chapter_paths

LEGACY_ID = re.compile(r"(?<!\w)(?:M\d+|R\d+[A-Z]?|Q[123]-\d+[A-Z]?)(?!\w)")


def main() -> None:
    chapters = chapter_paths()
    errors: list[str] = []
    for path in chapters:
        text = path.read_text(encoding="utf-8")
        if LEGACY_ID.search(text):
            errors.append(f"{path}: legacy result/model identifier appears in new source")
        if text.count("```") % 2:
            errors.append(f"{path}: unclosed Markdown code fence")
    for name in ("rewrite/CLAIM_LEDGER.md", "PROJECT_STATUS.md", "PROJECT_GUIDE.md", "VALIDATION_POLICY.md"):
        if not (ROOT / name).is_file():
            errors.append(f"missing active management document: {name}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"source_check_ok chapters={len(chapters)}")


if __name__ == "__main__":
    main()
