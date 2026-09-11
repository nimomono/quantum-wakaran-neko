#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"


def main() -> None:
    scripts = sorted(TOOLS.glob("verify_*.py"))
    if not scripts:
        raise SystemExit("no verify_*.py scripts found")

    failures: list[str] = []
    for script in scripts:
        print(f"=== {script.name} ===", flush=True)
        completed = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if completed.returncode:
            failures.append(script.name)
            print(f"FAILED: {script.name} (exit {completed.returncode})", flush=True)
            break
        print(f"OK: {script.name}", flush=True)

    if failures:
        raise SystemExit(1)
    print(f"physics_checks_ok ({len(scripts)} scripts)")


if __name__ == "__main__":
    main()
