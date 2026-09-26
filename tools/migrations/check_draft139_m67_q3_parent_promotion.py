#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def req(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def main() -> None:
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    status = read("PROJECT_STATUS.md")
    enh = read("ENHANCEMENT_TARGETS.md")
    lineage = read("notes/theory_lineage.md")

    for needle in (
        "R210A：M67 coherent-sector / R86 finite-time compatibility",
        "R210B：M67 bounded finite-dephasing embedding",
        "Q3共通二実体finite-Hamiltonian physical parent",
    ):
        req(a27 + status, needle, "M67 promotion")

    req(status, "| M67 | Q3共通二実体finite-Hamiltonian physical parent |", "PROJECT_STATUS")
    req(status, "| M64 | Q3 canonical open effective model |", "PROJECT_STATUS")
    req(status, "| M37 | active coherent-signal module |", "PROJECT_STATUS")
    for q in ("Q3-1", "Q3-2", "Q3-3A", "Q3-3B", "Q3-3C", "Q3-4A", "Q3-4B", "Q3-5"):
        line = next(x for x in status.splitlines() if x.startswith(f"| {q} | 達成 |"))
        req(line, "M67", q)
    req(status, "| Q3-6 | 未達 | M67 coherent sector |", "Q3-6")

    for name in (
        "verify_m67_two_entity_hamiltonian.py",
        "verify_r208_phase_volume_backreaction.py",
        "verify_r208_local_moving_bath.py",
        "verify_r208_m64_reduction.py",
        "verify_r209a_local_flow_compatibility.py",
        "verify_r209b_finite_bath_markov_fdt.py",
        "verify_r209c_process_compatibility.py",
        "verify_r210a_m67_coherent_compatibility.py",
        "verify_r210b_m67_bounded_dephasing.py",
    ):
        if not (ROOT / "tools" / name).is_file():
            raise AssertionError(f"required verifier missing: {name}")
        if (ROOT / "tools" / "candidate_checks" / name).exists():
            raise AssertionError(f"promoted verifier still candidate: {name}")

    req(enh, "| Q3-1 | 部分達成 | 未監査 |", "enhancement status")
    req(enh, "| Q3-2 | 部分達成 | 未監査 |", "enhancement status")
    req(enh, "Q3-1-A2/Q3-2-A2は未監査", "enhancement boundary")
    req(status, "| Q2-4 | 条件付き達成 |", "Q2-4 unchanged")
    req(status, "| M54 |", "M54 unchanged")
    req(status, "| M65 |", "M65 unchanged")
    req(status, "| M66 |", "M66 unchanged")
    req(status, "M0", "M0 boundary")
    req(lineage, "M67 common physical parent", "theory lineage")
    print("draft139_m67_q3_parent_promotion_check_ok")


if __name__ == "__main__":
    main()
