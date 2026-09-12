#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class LatexFinding:
    severity: str
    kind: str
    message: str
    source_line: int | None = None
    amount_pt: float | None = None


HARD_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("undefined-citation", re.compile(r"Citation .* undefined", re.IGNORECASE)),
    ("undefined-reference", re.compile(r"Reference .* undefined", re.IGNORECASE)),
    ("undefined-references-summary", re.compile(r"There were undefined references", re.IGNORECASE)),
    ("missing-character", re.compile(r"Missing character:", re.IGNORECASE)),
    ("fatal-error", re.compile(r"Fatal error", re.IGNORECASE)),
    ("emergency-stop", re.compile(r"Emergency stop", re.IGNORECASE)),
)

OVERFULL_RE = re.compile(
    r"Overfull \\hbox \((?P<amount>[0-9.]+)pt too wide\)(?: in paragraph)? at lines? (?P<start>\d+)(?:--(?P<end>\d+))?",
    re.IGNORECASE,
)
UNDERFULL_RE = re.compile(
    r"Underfull \\hbox .*?(?: at lines? (?P<start>\d+)(?:--(?P<end>\d+))?)?$",
    re.IGNORECASE,
)


def classify_latex_log(text: str) -> tuple[list[LatexFinding], list[LatexFinding]]:
    hard: list[LatexFinding] = []
    style: list[LatexFinding] = []

    for line in text.splitlines():
        for kind, pattern in HARD_PATTERNS:
            if pattern.search(line):
                hard.append(LatexFinding("error", kind, line.strip()))
                break

        overfull = OVERFULL_RE.search(line)
        if overfull:
            style.append(
                LatexFinding(
                    "warning",
                    "overfull",
                    line.strip(),
                    source_line=int(overfull.group("start")),
                    amount_pt=float(overfull.group("amount")),
                )
            )
            continue

        underfull = UNDERFULL_RE.search(line)
        if underfull:
            source_line = underfull.group("start")
            style.append(
                LatexFinding(
                    "warning",
                    "underfull",
                    line.strip(),
                    source_line=int(source_line) if source_line else None,
                )
            )

    return hard, style
