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
    a26 = read("sections/A26_m65_phase_volume_projective_instrument.md")
    status = read("PROJECT_STATUS.md")
    enh = read("ENHANCEMENT_TARGETS.md")
    a16 = read("sections/A16_m54_projector_tree_receiver.md")
    a24 = read("sections/A24_m66_common_phase_volume_readout.md")
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    lineage = read("notes/theory_lineage.md")
    retired = read("notes/superseded_m65_fixed_hub_physical_lift.md")

    for needle in (
        "two-result first-passage",
        "survival condition",
        "R204A：M65 canonical two-result first-passage selector",
        "R204D：M65有限時間Born readout",
        "R204E：M65はbinary selector contractを満たす",
        "R204F：Q1 M65 interfaceと有限latency条件",
        "e^{-\\kappa a_\\Sigma T}",
    ):
        req(a26, needle, "M65 first-passage core")

    for needle in (
        "k_{+\\to H}",
        "k_{H\\to +}",
        "3状態open selector",
        "R204B：",
        "R204C：",
    ):
        forbid(a26, needle, "active M65 appendix")

    req(status, "| M65 | Q1 binary canonical open selector |", "PROJECT_STATUS M65")
    req(status, "two-result first-passage open selector", "PROJECT_STATUS M65")
    q12 = next(line for line in status.splitlines() if line.startswith("| Q1-2 | 達成 |"))
    req(q12, "R204A", "Q1-2 direct evidence")
    req(q12, "R204D--R204F", "Q1-2 direct evidence")
    req(q12, "R181D", "Q1-2 direct evidence")
    q22 = next(line for line in status.splitlines() if line.startswith("| Q2-2 | 達成 |"))
    req(q22, "R207A--R207C", "Q2-2 direct evidence")
    forbid(q22, "M65", "Q2-2 direct evidence")
    forbid(q22, "R181D", "Q2-2 direct evidence")

    current_results = status.split("## 現行結果の導出状態", 1)[1].split("## 物理的解釈と境界", 1)[0]
    req(current_results, "| R204A |", "current R204 ledger")
    req(current_results, "| R204D |", "current R204 ledger")
    req(current_results, "| R204E |", "current R204 ledger")
    req(current_results, "| R204F |", "current R204 ledger")
    forbid(current_results, "| R204B |", "current R204 ledger")
    forbid(current_results, "| R204C |", "current R204 ledger")

    req(a16, "R181Dはfirst-passage waiting-time lawやselector内部状態数を仮定しない", "R181D boundary")
    req(a24, "binary fixed-hub corollary", "R205D boundary")
    req(a24, "現行M65 physical liftとは扱わない", "R205D boundary")
    req(enh, "| Q1-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |", "Q1-2 strengthening unchanged")
    req(enh, "finite-Hamiltonian/double-well lift", "M65 strengthening boundary")

    for name in (
        "verify_m65_phase_volume_partition.py",
        "verify_m65_matched_conductance.py",
        "verify_m65_brownian_reduction.py",
    ):
        if (ROOT / "tools" / "candidate_checks" / name).exists():
            raise AssertionError(f"retired M65 checker remains candidate: {name}")
        if not (ROOT / "notes" / "retired_verifiers" / name).is_file():
            raise AssertionError(f"retired M65 checker missing: {name}")

    for path in (
        "tools/verify_m65_open_selector.py",
        "tools/verify_q1_live_zeno.py",
        "tools/verify_r181d_projector_tree.py",
    ):
        if not (ROOT / path).is_file():
            raise AssertionError(f"required verifier missing: {path}")

    req(retired, "R204B", "retired fixed-hub note")
    req(retired, "R204C", "retired fixed-hub note")
    req(lineage, "two-result first-passage selector", "theory lineage")

    # PR3.5 must not pre-empt the later M67/R211 Q1 physical bridge.
    forbid(a27, "R211A", "M67 PR4 boundary")
    forbid(a27, "R211B", "M67 PR4 boundary")

    # Fixed-goal/enhancement boundaries outside Q1 remain untouched.
    req(status, "| Q2-4 | 条件付き達成 |", "Q2-4 unchanged")
    req(status, "| Q3-6 | 未達 |", "Q3-6 unchanged")
    req(status, "M0", "M0 boundary")
    print("draft140_m65_first_passage_selector_check_ok")


if __name__ == "__main__":
    main()
