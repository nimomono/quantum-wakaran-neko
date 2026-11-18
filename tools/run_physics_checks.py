#!/usr/bin/env python3
"""現行の主張に対応する検算だけを実行する。旧版verifierは保存ブランチにある。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "rewrite" / "CLAIM_LEDGER.md"


def main() -> None:
    required = sorted((ROOT / "tools").glob("verify_*.py"))
    current = LEDGER.read_text(encoding="utf-8").split(
        "## 採用済みの新体系の主張", 1
    )[-1].split("\n## ", 1)[0]
    if not required:
        if "なし。" not in current:
            raise SystemExit("physics checks absent but ledger is not explicitly empty")
        print("physics_checks_ok required=0: 新体系に採用済みの物理的主張なし")
        return

    failures: list[str] = []
    for script in required:
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode:
            failures.append(script.name)
    if failures:
        raise SystemExit("physics_checks_failed: " + ", ".join(failures))
    print(f"physics_checks_ok required={len(required)}")


if __name__ == "__main__":
    main()
