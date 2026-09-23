#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def current_block(text: str) -> str:
    return text.split("### 現在地", 1)[1].split(
        "## 現行模型・物理実装層・手順の運用状態", 1
    )[0]


def row(text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|.*$", current_block(text), re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: missing row {qid}")
    return m.group(0)


def main() -> None:
    a23 = read("sections/A23_q2_2_spatial_preparation.md")
    for token in (
        "@number: W",
        "命題（R207A：対称thermal joint preparationと公平setting sector）",
        "命題（R207B：strong-lock CHSH witnessの存在）",
        "命題（R207C：passive separation後のlocal responseとBell前提監査）",
        "定理（R207D：Bell-local CHSH control）",
        "Q2-2-Sを達成または部分達成へ更新しない",
    ):
        if token not in a23:
            raise AssertionError(f"A23 missing {token}")

    ps = read("PROJECT_STATUS.md")
    for token in ("| R207A |", "| R207B |", "| R207C |", "| R207D |"):
        if token not in ps:
            raise AssertionError(f"PROJECT_STATUS missing {token}")

    q22 = row(ps, "Q2-2")
    for token in ("R112", "R180C", "R181D", "R204D--R204E"):
        if token not in q22:
            raise AssertionError(f"Q2-2 fixed-goal dependency changed: {q22}")
    if "| Q2-2 | 達成 |" not in ps:
        raise AssertionError("Q2-2 fixed-goal status changed")

    enh = read("ENHANCEMENT_TARGETS.md")
    if "| Q2-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |" not in enh:
        raise AssertionError("Q2-2 enhancement status changed")
    for token in ("R205E", "R205F", "R207A--R207D"):
        if token not in enh:
            raise AssertionError(f"Q2-2-S candidate mapping missing {token}")

    active = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "sections").glob("*.md"))
    if "M67" in active:
        raise AssertionError("draft-130 must not introduce M67")

    for path in (
        "tools/candidate_checks/verify_r207_gibbs_chsh.py",
        "tools/candidate_checks/verify_r207_separation_control.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"candidate verifier missing: {path}")

    print("draft130_r207_q2_2_s_candidate_ok")


if __name__ == "__main__":
    main()
