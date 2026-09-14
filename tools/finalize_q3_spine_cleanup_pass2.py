#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

p = ROOT / "sections/07_q3_finite_graph_phenomena.md"
text = p.read_text(encoding="utf-8")
if "M57/R195D" not in text:
    raise SystemExit("expected remaining M57/R195D references were not found")
text = text.replace("M57/R195D", "M57/R196C")
p.write_text(text, encoding="utf-8")

# Current main chapters must not retain the retired R195D as a live dependency.
active_sections = sorted((ROOT / "sections").glob("0[0-9]_*.md"))
remaining: list[str] = []
for section in active_sections:
    s = section.read_text(encoding="utf-8")
    if "R195D" in s:
        remaining.append(section.name)
    if "M57--R195--R161/R162" in s:
        remaining.append(section.name + ":broad-old-spine")
if remaining:
    raise SystemExit("retired Q3 dependency remains in active chapters: " + ", ".join(remaining))

subprocess.run(["python", "tools/build_paper.py"], cwd=ROOT, check=True)

(ROOT / "tools/finalize_q3_spine_cleanup_pass2.py").unlink(missing_ok=True)
(ROOT / ".github/workflows/q3-spine-finalize-pass2.yml").unlink(missing_ok=True)
