#!/usr/bin/env python3
import re
from pathlib import Path

p = Path(__file__).resolve().parent / "check_source.py"
text = p.read_text(encoding="utf-8")
pattern = re.compile(r"def check_q3_common_model\(\) -> None:\n.*?\n(?=def check_enhancement_targets\(\) -> None:)", re.S)
replacement = '''def check_q3_common_model() -> None:
    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    q31 = next((line for line in status.splitlines() if line.startswith("| Q3-1 | 達成 |")), "")
    q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 | 達成 |")), "")
    if not q31 or not q32:
        raise AssertionError("Q3-1/Q3-2 fixed achievement rows are missing")

    appendix = (ROOT / "sections" / "A23_q3_common_micro_model.md").read_text(encoding="utf-8")
    for token in ("M59", "R198A", "R198B", "R198C", "R198D", "R197A", "R197C", "R197：M59"):
        if token not in appendix:
            raise AssertionError(f"A23 M59 marker missing: {token}")
    for forbidden in ("R197B：M58 shell", "mu_sh ="):
        if forbidden in appendix:
            raise AssertionError(f"retired M58 shell marker remains in A23: {forbidden}")

    enhancement = (ROOT / "ENHANCEMENT_TARGETS.md").read_text(encoding="utf-8")
    current = enhancement.split("## 強化目標の現在地表", 1)[1].split("## 既存の実装強化課題との関係", 1)[0]
    for qid in ("Q3-1", "Q3-2"):
        line = next((line for line in current.splitlines() if line.startswith(f"| {qid} |")), "")
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[1] != "部分達成" or cells[2] != "未監査":
            raise AssertionError(f"{qid}: expected A1=部分達成, A2=未監査")

'''
text, n = pattern.subn(lambda _: replacement, text)
if n != 1:
    raise SystemExit(f"expected one q3 check block, found {n}")
text = text.replace(
    'q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 | 達成 |") and "M58" in line), "")',
    'q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 | 達成 |") and "M59" in line), "")',
)
text = text.replace(
    'for token in ("R197", "R195A", "R196A--R196C", "R161", "R185"):',
    'for token in ("R197", "R198A--R198D", "R195A", "R196A--R196C", "R161", "R185"):',
)
p.write_text(text, encoding="utf-8")
print("draft102_source_contract_fix_ok")
