#!/usr/bin/env python3
"""現行原稿へ旧英語説明語が再混入していないか検査する。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"

TARGETS = [
    ROOT / "README.md",
    ROOT / "PROJECT_STATUS.md",
    ROOT / "PROJECT_STANCE.md",
    *sorted(path for path in SECTIONS.glob("*.md") if path.name != "90_references.md"),
]

FORBIDDEN_WORDS = (
    "profile", "carrier", "register", "cell", "latch", "branch",
    "sector", "backend", "handoff", "protocol", "bank", "mode",
    "signal", "bath", "clock", "collision", "filter", "ray",
    "matching", "port", "source", "repump", "receiver", "controller",
    "noise", "blank", "fresh", "spent", "raw", "cold", "specialization",
    "schedule", "criterion", "broadcast", "norm", "blanking", "latent",
    "copy", "tail", "isotropic", "selection", "collection", "support",
    "fringe", "limiter", "yield",
)

FORBIDDEN_PHRASES = (
    "projective-node", "projector-tree", "tensor-lift", "setting-pre",
    "radial-only", "finite collision", "canonical handoff",
    "functional calculus", "continuity equation", "data-processing",
    "interaction picture", "fault-tolerant", "hard defect",
)

INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
INLINE_MATH_RE = re.compile(r"\$[^$\n]*\$")
URL_RE = re.compile(r"https?://\S+")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def strip_protected(text: str) -> str:
    text = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    out: list[str] = []
    in_fence = False
    in_display_math = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        if stripped in {"$$", r"\["}:
            in_display_math = True
            out.append("")
            continue
        if stripped in {"$$", r"\]"} and in_display_math:
            in_display_math = False
            out.append("")
            continue
        if in_display_math:
            out.append("")
            continue
        if stripped.startswith("@"):
            out.append("")
            continue
        line = INLINE_CODE_RE.sub(" ", line)
        line = INLINE_MATH_RE.sub(" ", line)
        line = URL_RE.sub(" ", line)
        out.append(line)
    return "\n".join(out)


def main() -> None:
    errors: list[str] = []
    word_patterns = {
        word: re.compile(
            rf"(?<![A-Za-z0-9_]){re.escape(word)}(?![A-Za-z0-9_])",
            re.IGNORECASE,
        )
        for word in FORBIDDEN_WORDS
    }
    phrase_patterns = {
        phrase: re.compile(re.escape(phrase), re.IGNORECASE)
        for phrase in FORBIDDEN_PHRASES
    }

    for path in TARGETS:
        text = strip_protected(path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for token, pattern in word_patterns.items():
                if pattern.search(line):
                    errors.append(f"{rel}:{line_number}: 旧説明語 {token!r}: {line.strip()}")
            for token, pattern in phrase_patterns.items():
                if pattern.search(line):
                    errors.append(f"{rel}:{line_number}: 旧複合語 {token!r}: {line.strip()}")

    if errors:
        print("用語規約違反:")
        print("\n".join(errors))
        raise SystemExit(1)
    print("terminology_check_ok")


if __name__ == "__main__":
    main()
