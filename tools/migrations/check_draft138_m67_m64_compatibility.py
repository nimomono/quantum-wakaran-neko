#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def read(path: str) -> str:
    return (ROOT/path).read_text(encoding="utf-8")

def req(text: str, needle: str, where: str) -> None:
    if needle not in text:
        raise AssertionError(f"{where}: missing {needle}")

def main() -> None:
    a27=read("sections/A27_m67_two_entity_structured_reservoir.md")
    for needle in (
        "R209A：",
        "R209B：",
        "R209C：",
        "M67からM64への有限時間process compatibility",
        "epsilon_{67\\to64}",
    ):
        req(a27,needle,"A27")

    status=read("PROJECT_STATUS.md")
    req(status,"| M67 | 二実体finite-Hamiltonian parent candidate |","PROJECT_STATUS")
    req(status,"| Q3-2 | 達成 | M37 signal＋M64 continuous tracer","PROJECT_STATUS")
    req(status,"R86、R161、R185、R203A--R203D","PROJECT_STATUS")
    for needle in ("| R209A |","| R209B |","| R209C |"):
        req(status,needle,"PROJECT_STATUS")

    for path in (
        "tools/candidate_checks/verify_r209a_local_flow_compatibility.py",
        "tools/candidate_checks/verify_r209b_finite_bath_markov_fdt.py",
        "tools/candidate_checks/verify_r209c_process_compatibility.py",
        "simulations/m67/run_full_compatibility_witness.py",
    ):
        if not (ROOT/path).exists():
            raise AssertionError(f"missing {path}")

    enh=read("ENHANCEMENT_TARGETS.md")
    req(enh,"Q3-1-A2/Q3-2-A2は未監査","ENHANCEMENT_TARGETS")

    # Promotion/retirement is explicitly deferred to the next PR.
    if "M67 | 二実体finite-Hamiltonian parent model |" in status:
        raise AssertionError("M67 promoted prematurely")
    if "M64 | Q3共通open model | 退役" in status:
        raise AssertionError("M64 retired prematurely")

    print("draft138_m67_m64_compatibility_check_ok")

if __name__=="__main__":
    main()
