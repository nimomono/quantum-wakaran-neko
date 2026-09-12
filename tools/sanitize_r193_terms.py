#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = (
    "PROJECT_STATUS.md",
    "VALIDATION.md",
    "MANIFEST.md",
    "CHANGELOG.md",
    "sections/01_scope_and_cycle.md",
    "sections/02_common_canonical_modules.md",
    "sections/03_m47_controlled_w_instrument.md",
    "sections/08_errors_resources_open_targets.md",
    "sections/09_conclusion.md",
    "sections/A8_m47_w2_parameter_dictionary.md",
    "sections/A20_m54_brownian_macrospin_projective_instrument.md",
    "sections/A21_q1_r193_macrospin_bridge.md",
)

REPLACEMENTS = (
    ("fresh-latch", "未使用保持対"),
    ("fresh pair", "未使用保持対"),
    ("used latch", "使用済み保持対"),
    ("共通clock", "共通時計自由度"),
    ("```text", "```"),
)


def main() -> None:
    for rel in FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
    print("r193_terminology_sanitized")


if __name__ == "__main__":
    main()
