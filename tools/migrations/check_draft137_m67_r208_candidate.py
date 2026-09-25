#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def read(p): return (ROOT/p).read_text(encoding="utf-8")
def req(t,s,w):
    if s not in t: raise AssertionError(f"{w}: missing {s}")
def main():
    a=read("sections/A27_m67_two_entity_structured_reservoir.md")
    for s in ("@number: AA","R208A：","R208B：","R208C：","R208D："): req(a,s,"A27")
    st=read("PROJECT_STATUS.md")
    for s in ("| M67 |","| R208A |","| R208B |","| R208C |","| R208D |"): req(st,s,"PROJECT_STATUS")
    req(st,"| Q3-2 | 達成 | M37 signal＋M64 continuous tracer","PROJECT_STATUS")
    req(st,"R86、R161、R185、R203A--R203D","PROJECT_STATUS")
    req(read("ENHANCEMENT_TARGETS.md"),"Q3-1-A2/Q3-2-A2は未監査","ENHANCEMENT_TARGETS")
    print("draft137_m67_r208_candidate_check_ok")
if __name__=="__main__": main()
