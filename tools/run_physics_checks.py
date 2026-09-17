#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"


@dataclass(frozen=True)
class CheckResult:
    label: str
    path: Path
    returncode: int


def discover(include_candidate: bool) -> list[tuple[str, Path]]:
    checks: list[tuple[str, Path]] = [
        ("required", path) for path in sorted(TOOLS.glob("verify_*.py"))
    ]
    if include_candidate:
        candidate_dir = TOOLS / "candidate_checks"
        checks.extend(
            ("candidate", path)
            for path in sorted(candidate_dir.glob("verify_*.py"))
        )
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-candidate",
        action="store_true",
        help="also run tools/candidate_checks/verify_*.py",
    )
    args = parser.parse_args()

    checks = discover(args.include_candidate)
    required_count = sum(label == "required" for label, _ in checks)
    if required_count == 0:
        raise SystemExit("no required verify_*.py scripts found")

    results: list[CheckResult] = []
    for label, script in checks:
        rel = script.relative_to(ROOT).as_posix()
        print(f"=== [{label}] {rel} ===", flush=True)
        completed = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        result = CheckResult(label, script, completed.returncode)
        results.append(result)
        state = "OK" if completed.returncode == 0 else f"FAILED (exit {completed.returncode})"
        print(f"{state}: {rel}", flush=True)

    print("\n=== physics check summary ===", flush=True)
    for result in results:
        rel = result.path.relative_to(ROOT).as_posix()
        state = "PASS" if result.returncode == 0 else "FAIL"
        print(f"{state:4} [{result.label}] {rel}", flush=True)

    failures = [result for result in results if result.returncode != 0]
    if failures:
        print(
            f"physics_checks_failed ({len(failures)}/{len(results)} scripts)",
            flush=True,
        )
        raise SystemExit(1)

    print(f"physics_checks_ok ({len(results)} scripts)", flush=True)


if __name__ == "__main__":
    main()
