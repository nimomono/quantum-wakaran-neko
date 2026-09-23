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
        raise AssertionError(f"{path}: missing draft-128 markers: {missing}")

def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    found = [token for token in tokens if token in text]
    if found:
        raise AssertionError(f"{path}: forbidden draft-128 markers remain: {found}")

def current_block(text: str) -> str:
    return text.split("### 現在地", 1)[1].split(
        "## 現行模型・物理実装層・手順の運用状態", 1
    )[0]

def row(text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|.*$", current_block(text), re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: missing row for {qid}")
    return m.group(0)

def main() -> None:
    a24 = "sections/A24_m66_common_phase_volume_readout.md"
    a26 = "sections/A26_m65_phase_volume_projective_instrument.md"

    require(
        a24,
        "@number: X",
        "@title: M66共通phase-volume reservoirとQ2多結果readout",
        "R205A：共通phase-volume identity",
        "R205B：matched capacity--conductance原理",
        "R205C--R205D：M64/M65との共通原理",
        "R206A：有限L結果common-hub sampler",
        "R206B：Q2-4用の一様受動channel構成",
        "R206C：finite-time / fabrication-error bound",
        "R206D：Q2-1、Q2-3、Q2-4 readout bridge",
        "R206E：Q2-4 uniform root preparation / refresh",
        "Q2-1/Q2-3/Q2-4のterminal multi-outcome readout正本",
    )
    forbid(a24, "R204A：", "R204D：", "R204F：", "Z.11")

    require(
        a26,
        "@number: Z",
        "@title: M65 binary selector",
        "R204A：M65 canonical open selector",
        "R204D：M65有限時間Born readout",
        "R204E：M65はbinary selector contractを満たす",
        "R204F：Q1 M65 interfaceと有限latency条件",
        "付録XのM66/R206",
    )
    forbid(
        a26,
        "## Z.11 M66共通phase-volume reservoirとQ2多結果readout",
        "定理（R205A：",
        "定理（R205B：",
        "定理（R206A：",
        "定理（R206B：",
        "定理（R206C：",
        "定理（R206D：",
        "定理（R206E：",
    )

    require(
        "sections/04_m54_q2_specializations.md",
        "付録XをM66/R206 terminal readout正本とし",
    )

    ps = read("PROJECT_STATUS.md")
    q1 = row(ps, "Q1-2")
    q21 = row(ps, "Q2-1")
    q22 = row(ps, "Q2-2")
    q23 = row(ps, "Q2-3")
    q24 = row(ps, "Q2-4")

    for token in ("R181D", "R204D--R204F"):
        if token not in q1:
            raise AssertionError(f"Q1-2 dependency changed: {q1}")
    for token in ("R181D", "R204D--R204E"):
        if token not in q22:
            raise AssertionError(f"Q2-2 dependency changed: {q22}")
    if "R206D" not in q21 or "R206D" not in q23:
        raise AssertionError("Q2-1/Q2-3 lost R206D")
    for token in ("R181C", "R186", "R206D", "R206E"):
        if token not in q24:
            raise AssertionError(f"Q2-4 dependency changed: {q24}")
    if "| Q2-4 | 条件付き達成 |" not in ps:
        raise AssertionError("Q2-4 status changed")

    for path in (
        "tools/verify_m66_common_phase_volume.py",
        "tools/verify_r206_multi_outcome_sampler.py",
        "tools/verify_r206_uniform_passive_scaling.py",
        "tools/verify_r206_q2_resource_scaling.py",
        "tools/verify_r206_root_preparation.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"required verifier missing: {path}")

    print("draft128_split_m66_appendix_ok")

if __name__ == "__main__":
    main()
