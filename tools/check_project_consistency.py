#!/usr/bin/env python3
"""採用主張がない段階を明示的に許し、存在しない証明を装わない。"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "rewrite" / "CLAIM_LEDGER.md"


def main() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    if "## 採用済みの新体系の主張" not in text:
        raise SystemExit("missing claim-ledger section")
    current = text.split("## 採用済みの新体系の主張", 1)[1].split("\n## ", 1)[0]
    active = [
        line for line in current.splitlines()
        if re.match(r"^\|\s*[A-Za-z][A-Za-z0-9_-]+\s*\|", line)
    ]
    if active:
        raise SystemExit(
            "active claims require a dedicated formal ledger/verifier schema before registration"
        )
    if "なし。" not in current:
        raise SystemExit("declare explicitly that the new claim ledger is empty")
    print("project_consistency_ok active_claims=0 (no derived results claimed)")


if __name__ == "__main__":
    main()
