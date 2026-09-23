#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def require(path: str, *tokens: str) -> None:
    text = read(path)
    missing = [token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-127 markers: {missing}")

def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    found = [token for token in tokens if token in text]
    if found:
        raise AssertionError(f"{path}: forbidden draft-127 markers remain: {found}")

def current_block(text: str) -> str:
    try:
        return text.split("### 現在地", 1)[1].split("## 現行模型・物理実装層・手順の運用状態", 1)[0]
    except IndexError as exc:
        raise AssertionError("PROJECT_STATUS.md: current-position block missing") from exc

def status_row(text: str, qid: str) -> str:
    block = current_block(text)
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|.*$", block, re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: current row missing for {qid}")
    return m.group(0)

def status(text: str, qid: str) -> str:
    row = status_row(text, qid)
    m = re.match(rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|", row)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status missing for {qid}")
    return m.group(1)

def must_have(row: str, *tokens: str) -> None:
    missing = [x for x in tokens if x not in row]
    if missing:
        raise AssertionError(f"row missing: {missing}\n{row}")

def must_not_have(row: str, *tokens: str) -> None:
    found = [x for x in tokens if x in row]
    if found:
        raise AssertionError(f"row still contains retired dependency: {found}\n{row}")

def main() -> None:
    ps = read("PROJECT_STATUS.md")
    expected = {
        "Q1-2": "達成",
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    q1 = status_row(ps, "Q1-2")
    q21 = status_row(ps, "Q2-1")
    q22 = status_row(ps, "Q2-2")
    q23 = status_row(ps, "Q2-3")
    q24 = status_row(ps, "Q2-4")

    must_have(q1, "R181D", "R204D--R204F")
    must_have(q22, "R181D", "R204D--R204E")
    must_have(q21, "R206D")
    must_have(q23, "R177", "R206D")
    must_have(q24, "R181C", "R186", "R206D", "R206E")

    must_not_have(q21, "R181D", "R204D", "R204E", "R179", "R192")
    must_not_have(q23, "R181D", "R204D", "R204E", "R179", "R192")
    must_not_have(q24, "R179", "R181D", "R192", "R204F", "M65")

    require(
        "sections/A26_m65_phase_volume_projective_instrument.md",
        "R206C：finite-time / fabrication-error bound",
        "R206E：uniform root preparation / refresh",
        "Q2-1/Q2-3/Q2-4のterminal multi-outcome readout正本",
    )
    require(
        "sections/A16_m54_projector_tree_receiver.md",
        "Q1逐次測定とQ2-2",
        "Q2-1/Q2-3/Q2-4はterminal M66/R206 sampler",
    )
    require(
        "sections/A17_m54_uniform_supply.md",
        "Q2-4のroot preparation/refreshはR206E",
    )

    if (ROOT / "sections/A13_m54_radial_stabilizer.md").exists():
        raise AssertionError("R192 active appendix still exists")
    if (ROOT / "tools/verify_r192_radial_stabilizer.py").exists():
        raise AssertionError("R192 required verifier still exists")

    for path in (
        "tools/verify_m66_common_phase_volume.py",
        "tools/verify_r206_multi_outcome_sampler.py",
        "tools/verify_r206_uniform_passive_scaling.py",
        "tools/verify_r206_q2_resource_scaling.py",
        "tools/verify_r206_root_preparation.py",
        "notes/superseded_r192_radial_stabilizer.md",
        "notes/superseded_q2_sequential_terminal_readout.md",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"missing draft-127 file: {path}")

    require(
        "PROJECT_STATUS.md",
        "| M66 | Q2 terminal multi-outcome common-reservoir readout | Q2-1/Q2-3/Q2-4現行fixed-goal正本 |",
        "| R206C |",
        "| R206E |",
        "draft-127ではQ2-1/Q2-3/Q2-4のterminal readoutをM66/R206へ置換",
    )
    forbid(
        "PROJECT_STATUS.md",
        "| R192 | 直接定めた開放方程式に対する厳密結果",
    )

    print("draft127_promote_m66_r206_ok")

if __name__ == "__main__":
    main()
