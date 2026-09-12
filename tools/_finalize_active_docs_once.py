#!/usr/bin/env python3
from pathlib import Path

path = Path("PROJECT_STATUS.md")
text = path.read_text(encoding="utf-8")
old = "| 準備・測定・装置統合 | 零傾斜最低2正常モードをM54のW2信号へ正準同定するところまでR187で閉鎖。R181Aのポンプ／供給源、R164/R161/R162/R170の選択・固定機構、R143またはR112の記録、リセットとの単一装置統合とM0は未構成 |"
new = "| 準備・測定・装置統合 | 零傾斜最低2正常モードをM54のW2信号へ正準同定するところまでR187で閉鎖。準備済み入力境界、射影作用保持、R191読出し、R181Dの射影成分振り分け、外部記録、必要なR179開放リセットを同じ具体装置と時計自由度へ統合するM0は未構成 |"
if text.count(old) != 1:
    raise SystemExit(f"expected one stale integration row, found {text.count(old)}")
text = text.replace(old, new, 1)
for stale in (
    "R181Aのポンプ／供給源",
    "R180設定先行2端Hopf受信機構",
    "R170はQ1、Q2-1、Q2-3、Q2-4、R180A、R180Cで共通に使う",
    "Q3-2固定範囲の有限衝突合成加速度はR162/R188で閉じた",
):
    if stale in text:
        raise SystemExit(f"stale active-status wording remains: {stale}")
path.write_text(text, encoding="utf-8")
print("final_active_status_cleanup_ok")
