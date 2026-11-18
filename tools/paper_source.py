#!/usr/bin/env python3
"""第2期研究の原稿収集。旧版の章番号・結果IDに依存しない。"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
CHAPTER_RE = re.compile(r"(?P<number>\d{2})_[a-z0-9_]+\.md$")


def chapter_paths() -> list[Path]:
    chapters = sorted(SECTIONS.glob("*.md"))
    if not chapters:
        raise ValueError("sections/ is empty")
    numbers: set[int] = set()
    for path in chapters:
        match = CHAPTER_RE.fullmatch(path.name)
        if not match:
            raise ValueError(f"non-current source in sections/: {path.name}")
        number = int(match.group("number"))
        if number in numbers:
            raise ValueError(f"duplicate chapter number: {number}")
        numbers.add(number)
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            raise ValueError(f"{path}: first line must be a top-level heading")
        if "\x00" in text or "\r" in text:
            raise ValueError(f"{path}: disallowed control character")
    if 0 not in numbers:
        raise ValueError("sections/ requires a 00_ introduction")
    return chapters


def public_markdown() -> str:
    intro = (
        "# 第2期研究：古典力学から量子型構造の起源を調べる\n\n"
        "> **研究中。** この原稿は問題設定と判定基準のみを定める。"
        "量子力学の微視的導出・定理の達成は現段階では主張しない。\n"
    )
    return intro + "\n\n" + "\n\n".join(
        path.read_text(encoding="utf-8").strip()
        for path in chapter_paths()
    ) + "\n"


def pandoc_markdown() -> str:
    text = public_markdown()
    # 節番号はXeLaTeX側で付ける。公開Markdownには著者の見出しを残す。
    return re.sub(
        r"(?m)^(#{1,6})\s+(?:\d+(?:\.\d+)*\.?\s+)(.+)$",
        r"\1 \2",
        text,
    )
