#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def req(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"{label}: stale {needle!r}")


def main() -> None:
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    a26 = read("sections/A26_m65_phase_volume_projective_instrument.md")
    a16 = read("sections/A16_m54_projector_tree_receiver.md")
    a24 = read("sections/A24_m66_common_phase_volume_readout.md")
    status = read("PROJECT_STATUS.md")
    enh = read("ENHANCEMENT_TARGETS.md")
    validation = read("VALIDATION.md")
    lineage = read("notes/theory_lineage.md")

    for needle in (
        "R211A：M67 Q1 double-well finite-Hamiltonian construction",
        "R211B：M67 Q1 double-well Born kernel / R204E compatibility",
        "R211C：M67 Q1 selector physical-lift composition",
        "中央に第三の安定pointer状態を持たない",
        "R211BはM65/R204Aの指数Poisson waiting-time law",
        "K_{67}^T",
        "\\varepsilon_{211B}",
    ):
        req(a27, needle, "R211 active appendix")

    req(a27, "Q2/NBL特殊化は将来候補", "M67 Q2/NBL boundary")
    forbid(a27, "Q1/Q2/NBL特殊化は将来候補", "stale M67 Q1 boundary")

    for needle in (
        "R204A：M65 canonical two-result first-passage selector",
        "R204D：M65有限時間Born readout",
        "R204E：M65はbinary selector contractを満たす",
        "R204F：Q1 M65 interfaceと有限latency条件",
    ):
        req(a26, needle, "M65 canonical path")

    for needle in ("R204B：", "R204C："):
        forbid(a26, needle, "retired R204B/C remain retired")

    req(a24, "binary fixed-hub corollary", "R205D boundary")
    req(a24, "現行M65 physical liftとは扱わない", "R205D boundary")
    req(a16, "M67/R211 finite-Hamiltonian physical lift", "R181D alternate selector")
    req(a16, "R181DはM65 Poisson waiting-time lawもM67 double-well dynamicsも仮定せず", "R181D independence")

    q12 = next(line for line in status.splitlines() if line.startswith("| Q1-2 | 達成 |"))
    req(q12, "R204A", "Q1-2 canonical evidence")
    req(q12, "R204D--R204F", "Q1-2 canonical evidence")
    req(q12, "R181D", "Q1-2 canonical evidence")
    forbid(q12, "R211A", "Q1-2 direct evidence unchanged")
    forbid(q12, "R211B", "Q1-2 direct evidence unchanged")

    for q in ("Q2-1", "Q2-2", "Q2-3", "Q2-4"):
        line = next(line for line in status.splitlines() if line.startswith(f"| {q} |"))
        forbid(line, "R211", f"{q} unchanged")
    req(status, "| Q2-4 | 条件付き達成 |", "Q2-4 unchanged")
    req(status, "| Q3-6 | 未達 |", "Q3-6 unchanged")
    req(status, "### M67 Q1 selector-lift結果", "R211 result ledger")
    for rid in ("R211A", "R211B", "R211C"):
        req(status, f"| {rid} |", "R211 result ledger")

    req(enh, "| Q1-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |", "Q1-2 strengthening unchanged")
    req(enh, "M67/R211A--R211C", "M67 Q1 strengthening")
    req(enh, "full direct trajectory", "A2 boundary")

    for path in (
        "tools/verify_r211a_m67_q1_hamiltonian.py",
        "tools/verify_m67_q1_first_passage.py",
        "tools/verify_q1_live_zeno.py",
        "tools/verify_m65_open_selector.py",
        "tools/verify_r181d_projector_tree.py",
    ):
        if not (ROOT / path).is_file():
            raise AssertionError(f"required verifier missing: {path}")

    req(validation, "draft-141：M67 Q1 selector physical-lift検算", "validation ledger")
    req(lineage, "draft-141でM67/R211 Q1 selector liftを追加", "theory lineage")

    print("draft141_m67_q1_selector_lift_check_ok")


if __name__ == "__main__":
    main()
