#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def row(text: str, qid: str) -> str:
    block = text.split("### 現在地", 1)[1].split(
        "## 現行模型・物理実装層・手順の運用状態", 1
    )[0]
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|.*$", block, re.M)
    if not m:
        raise AssertionError(f"missing row {qid}")
    return m.group(0)


def main() -> None:
    a24 = read("sections/A24_m66_common_phase_volume_readout.md")
    for token in (
        "定理（R205C：phase-volume / mean-flow orthogonality）",
        "系（R205D：binary fixed-hub specialization）",
        "定理（R205E：common thermal Gibbs sampler）",
        "定理（R205F：passive separation principle）",
        "R206A：finite-$L$ common-hub sampler",
        "R206E：uniform root preparation / refresh",
    ):
        if token not in a24:
            raise AssertionError(f"A24 missing {token}")

    ps = read("PROJECT_STATUS.md")
    for token in ("| M66 | common thermal-reservoir parent model |", "| R205C |", "| R205D |", "| R205E |", "| R205F |"):
        if token not in ps:
            raise AssertionError(f"PROJECT_STATUS missing {token}")

    if "R206D" not in row(ps, "Q2-1") or "R206D" not in row(ps, "Q2-3"):
        raise AssertionError("Q2-1/Q2-3 dependency changed")
    if not all(t in row(ps, "Q2-4") for t in ("R181C", "R186", "R206D", "R206E")):
        raise AssertionError("Q2-4 dependency changed")
    if not all(t in row(ps, "Q2-2") for t in ("R181D", "R204D--R204E")):
        raise AssertionError("Q2-2 dependency changed")
    if not all(t in row(ps, "Q3-2") for t in ("R203A--R203D", "R161", "R185")):
        raise AssertionError("Q3-2 dependency changed")
    if "| Q2-4 | 条件付き達成 |" not in ps:
        raise AssertionError("Q2-4 status changed")

    active = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "sections").glob("*.md"))
    if "R207" in active:
        raise AssertionError("R207 introduced too early")

    for path in (
        "tools/verify_m66_common_phase_volume.py",
        "tools/verify_m66_thermal_gibbs_sampler.py",
        "tools/verify_m66_passive_separation.py",
        "tools/verify_r206_multi_outcome_sampler.py",
        "tools/verify_m64_reservoir_partition.py",
        "tools/verify_m65_open_selector.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"missing verifier {path}")

    print("draft129_m66_common_reservoir_parent_ok")


if __name__ == "__main__":
    main()
