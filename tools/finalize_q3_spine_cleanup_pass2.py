#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def replace_required(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected cleanup fragment not found in {path}: {old!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# Remaining live references identified after the first pass.
replace_required(
    "sections/02_common_canonical_modules.md",
    "現行Q3の基礎的ミクロ存在論はM57/R195A--R195Dが担い",
    "現行Q3の基礎的ミクロ存在論はM57/R195A・R196A--R196Cが担い",
)
replace_required(
    "sections/02_common_canonical_modules.md",
    "現行Q3の物理主線はM57/R195A--R195Dであり",
    "現行Q3の物理主線はM57/R195A・R196A--R196Cであり",
)
replace_required(
    "sections/06_m37_spatial_envelope.md",
    "$\\delta>0$ のnode-free safe sectorでは、R195A・R196A--R196Cが有限TL mixing、FDT/Kramers縮約、生成子matchingを通じてR161率へ有限誤差で持ち上げる。",
    "$\\delta>0$ のnode-free safe sectorでは、R195A・R196A--R196Cがchiral作用/current恒等式、ballistic portとbath-frame追従、平衡GLE・periodic homogenization、生成子matchingを通じてR161率へ有限誤差で持ち上げる。",
)
replace_required(
    "sections/06_m37_spatial_envelope.md",
    "Q3-4AとQ3-5ではR124/R125の理想分布差をM57/R195Dの有限時間誤差 $\\varepsilon_{57}$ と比較する。",
    "Q3-4AとQ3-5ではR124/R125の理想分布差をM57/R196Cの有限時間誤差 $\\varepsilon_{57}$ と比較する。",
)

p = ROOT / "sections/07_q3_finite_graph_phenomena.md"
text = p.read_text(encoding="utf-8")
if "M57/R195D" not in text:
    raise SystemExit("expected remaining M57/R195D references were not found in section 07")
p.write_text(text.replace("M57/R195D", "M57/R196C"), encoding="utf-8")

replace_required(
    "sections/09_conclusion.md",
    "Q3のM57--R195--R161/R162--R185位置経路",
    "Q3のM57/R195A・R196A--R196C--R161--R185位置経路（R162はideal reference）",
)

# Current main chapters must not retain retired R195D or the broad old spine as live dependencies.
active_sections = sorted((ROOT / "sections").glob("0[0-9]_*.md"))
remaining: list[str] = []
for section in active_sections:
    s = section.read_text(encoding="utf-8")
    if "R195D" in s:
        remaining.append(section.name + ":R195D")
    if "M57--R195--R161/R162" in s:
        remaining.append(section.name + ":broad-old-spine")
if remaining:
    raise SystemExit("retired Q3 dependency remains in active chapters: " + ", ".join(remaining))

subprocess.run(["python", "tools/build_paper.py"], cwd=ROOT, check=True)

(ROOT / "tools/finalize_q3_spine_cleanup_pass2.py").unlink(missing_ok=True)
(ROOT / ".github/workflows/q3-spine-finalize-pass2.yml").unlink(missing_ok=True)
