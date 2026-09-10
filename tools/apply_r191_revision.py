#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def replace_if_present(text: str, old: str, new: str) -> str:
    return text.replace(old, new) if old in text else text


def insert_after(text: str, marker: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f"{label}: marker not found")
    idx += len(marker)
    return text[:idx] + payload + text[idx:]


def insert_before(text: str, marker: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f"{label}: marker not found")
    return text[:idx] + payload + text[idx:]


R191_MAIN = r'''
### 2.8.2 R191：作用差駆動ブラウン巨視的スピン2結果射影読出し

Q1/Q2の2結果射影測定では、作用殻の多結果状態数を経由する経路とは別に、固定した2つの射影作用を既知のBrownian spin型開放磁化力学へ直接接続できる。非零信号 $Z$ と $P_++P_-=I$ に対して

```math
J_+
=\mathcal J_0Z^\dagger P_+Z,
\qquad
J_-
=\mathcal J_0Z^\dagger P_-Z,
```

```math
S=J_++J_->0,
\qquad
D=J_+-J_-
```

を固定する。transducer出力 $\widehat S,\widehat D$ は

```math
|\widehat S-S|\leq\varepsilon_\Sigma S,
\qquad
|\widehat D-D|\leq\varepsilon_\Delta S,
\qquad
0\leq\varepsilon_\Sigma<1
```

を満たすとする。指針変数を単磁区巨視的スピンの軸成分 $U=m_z\in[-1,1]$ とし、混合窓では等方回転拡散、decision窓では

```math
V_{\rm dec}(u)
=-\frac\chi2
\left(
\widehat S u^2+2\widehat D u
\right)
```

を作用させる。実吸引域境界は

```math
\widehat u_*
=-\frac{\widehat D}{\widehat S}
```

であり、理想境界 $u_*=-D/S$ との差は

```math
|\widehat u_*-u_*|
\leq
\varepsilon_u
:=
\frac{\varepsilon_\Delta+\varepsilon_\Sigma}
{1-\varepsilon_\Sigma}.
```

<!-- theorem-start:theorem -->
**定理（R191：作用差駆動ブラウン巨視的スピン2結果射影読出し）**

混合終了時の $U$ の法則が $U[-1,1]$ から全変動距離 $\varepsilon_{\rm mix}$ 以内にあり、通常読出し経路では両実推定重みが $\tau_{\rm cut}>0$ 以上、保護帯幅 $g$ と捕獲幅 $\zeta$ が $g+\zeta<2\tau_{\rm cut}$ を満たすとする。$|U-\widehat u_*|<g$ は正式な無反応へ送り、保護帯外では付録Tの軸対称stochastic LLGをdecision時間 $T$ だけ走らせ、$[1-\zeta,1]$ または $[-1,-1+\zeta]$ への初到達結果を吸収記録へ写す。

$S\geq S_{\min}>0$ とし、

```math
\Delta_{\min}
=
\frac{\chi(1-\varepsilon_\Sigma)S_{\min}}
{2k_{\rm B}T_{\rm dec}},
\qquad
m_\zeta=\zeta(2-\zeta)
```

と置く。付録Tで定める有限温度retreat上界 $q_{\rm ret}$ と有限時間未捕獲上界 $q_{\rm time}$ を使えば、通常経路の完全結果分布 $P_{191}$ と理想Born分布 $P_{\rm Born}=(J_+/S,J_-/S,0)$ は

```math
D_{\rm TV}(P_{191},P_{\rm Born})
\leq
\varepsilon_{\rm mix}
+g
+\frac{\varepsilon_u}{2}
+q_{\rm ret}
+q_{\rm time}
+\varepsilon_{\rm cap}
=: \varepsilon_{191}^{\rm int}
```

を満たす。$\min\{\widehat p_+,\widehat p_-\}<\tau_{\rm cut}$ では大きい側を決定論的経路へ送り、その偏差を

```math
\varepsilon_{191}^{\rm edge}
\leq
\tau_{\rm cut}
+\frac{\varepsilon_u}{2}
+\varepsilon_{\rm cap}
```

で抑える。従って1ノード誤差は

```math
\varepsilon_{191}
=
\max
\left\{
\varepsilon_{191}^{\rm int},
\varepsilon_{191}^{\rm edge}
\right\}.
```

理想混合・transducer・低温・長decision時間・完全捕獲極限では

```math
P(+)=\frac{J_+}{J_++J_-},
\qquad
P(-)=\frac{J_-}{J_++J_-}.
```

成功試行だけを再規格化しない。結果固定後の射影branch生成と次段受渡しは既存の共通射影選別機構/R181Dが担い、一般深さでbranch作用下限が必要な場合だけ方向を変えない振幅再調整を使う。R164/R190/R170は一般有限結果集合、作用殻型実現、独立な強化経路として残す。
<!-- theorem-end:theorem -->

混合評価、stochastic LLG、scale density、$q_{\rm ret}$、$q_{\rm time}$、端点dispatcher、熱力学、Q2-2で中央集約4結果samplerへ置換しない責務境界は付録Tに置く [56--58]。

'''


def patch_common() -> None:
    p = "sections/02_common_canonical_modules.md"
    t = read(p)
    t = replace_if_present(t, "### 2.8.1### 2.8.1 R190A--R190C", "### 2.8.1 R190A--R190C")
    t = insert_before(t, "## 2.9 R170：", R191_MAIN, "common R191 insertion")
    t = replace_if_present(t, "確率的な排他的選択と固定はR170が担う。", "2結果射影測定の排他的選択と固定はR191を主線とし、一般有限結果集合または作用殻型の代替経路はR170が担う。")
    t = replace_if_present(t, "R170を、Q1、Q2の段階的射影選別、R180Aの中央潜在選択、R180Cの局所読出し、Q3固定時刻診断で共有する静的選択・固定の正本とする。", "R170を、一般有限結果集合、作用殻型の代替経路、Q3固定時刻診断で共有する静的選択・固定の正本として残す。Q1/Q2の2結果射影ノードではR191を主読出しとし、R170と同じ誤差を二重計上しない。")
    t = replace_if_present(t, "上流は正の固定済み作用容量 $\\widehat A_i$ を保持し、R164/R190/R179が与える静的選択過程を有限時間走らせる。", "R170を用いる代替経路では、上流が正の固定済み作用容量 $\\widehat A_i$ を保持し、R164/R190/R179が与える静的選択過程を有限時間走らせる。")
    t = replace_if_present(t, "作用殻混合、再混合、リセット、散逸履歴はR190/R179の環境接続部へ置く。", "Q1/Q2の2結果読出しはR191のブラウン巨視的スピン接続部を主線とする。作用殻混合、再混合、リセット、散逸履歴を使うR190/R179は一般有限結果集合と代替実現へ残す。")
    old = "$\\bar\\varepsilon_j$ には第 $j$ 段のR170誤差、制御付き選別機構、方向を変えない振幅再調整、転送を各1回だけ含める。R170の $\\varepsilon_{\\rm sel}$ にはR179の流入誤差とR190の記憶・混合・作用開口誤差を含めるため、R179またはR190の同じ偏差を別項として再加算しない。R179の開放リセット誤差が次試行入口へ残る場合は、その次試行の $\\varepsilon_{\\rm in}$ へ含める。"
    new = "$\\bar\\varepsilon_j$ には第 $j$ 段のR191誤差、制御付き選別機構、必要な場合の方向を変えない振幅再調整、転送を各1回だけ含める。2結果主線ではR164/R190/R170の同じ選択偏差を重複加算しない。R179の開放リセット誤差が次試行入口へ残る場合は、その次試行の $\\varepsilon_{\\rm in}$ へ含める。一般有限結果集合または作用殻代替経路を選ぶ場合だけ、R170の $\\varepsilon_{\\rm sel}$ にR179/R190の選択偏差をまとめる。"
    t = replace_if_present(t, old, new)
    t = replace_if_present(t, "$\\eta_{\\rm gate}=O(\\epsilon/d)$ とし、$\\tau,\\gamma,\\delta,\\bar\\varepsilon_j$ はそれぞれ $O(\\epsilon/n)$ と選ぶ。R190作用開口の正則化制約により、最悪試行頻度は $O(\\delta^{-1/2})$ まで増大し得る。", "$\\eta_{\\rm gate}=O(\\epsilon/d)$ とし、$\\tau,\\gamma,\\bar\\varepsilon_j$ はそれぞれ $O(\\epsilon/n)$ と選ぶ。R191主線では $g,\\varepsilon_u,\\varepsilon_{\\rm cap}=O(\\epsilon/n)$ とし、$\\Delta_{\\min}g^2\\gtrsim\\log(n/\\epsilon)$ を十分条件に取る。R190作用殻の代替経路を選ぶ場合だけ、正則化 $\\delta$ と最悪試行頻度 $O(\\delta^{-1/2})$ をその経路の資源として数える。")
    t = replace_if_present(t, "従ってM54はQ2-4を条件付き達成へ進める。条件は、射影容量保持機構、R190/R179静的選択機構、R170吸収指針変数、制御付き選別機構、方向を変えない振幅再調整、開放リセット/供給接続部を同じ安全集合と制御規約で接続することである。", "従ってM54はQ2-4を条件付き達成へ進める。2結果主線の条件は、射影作用保持機構、R191ブラウン巨視的スピン読出し、制御付き選別機構、必要な方向を変えない振幅再調整、開放リセット/供給接続部を同じ安全集合と制御規約で接続することである。R164/R190/R170経路は一般有限結果集合と作用殻型の代替実現として残す。")
    t = replace_if_present(t, "R170は、容量結合、作用殻、信号保持、混合・衝突、選択機構、固定機構を有限能動部分系＋明示的Hamiltonian無限浴の1つの具体的ミクロ装置へ統合済みだと主張しない。", "R191は、transducer、ブラウン巨視的スピン、射影branch生成、記録、resetを単一閉鎖Hamiltonianへ統合済みだと主張しない。R170についても、容量結合、作用殻、信号保持、混合・衝突、選択機構、固定機構を1つの具体的装置へ統合済みだと主張しない。")
    write(p, t)


def patch_source_summaries() -> None:
    replacements = {
        "sections/01_scope_and_cycle.md": [("Q1/Q2はR164/R190/R179/R170の静的選択、Q3はR161/R162の移動過程へ特殊化する。", "Q1/Q2の2結果射影読出しはR191を主線とし、R164/R190/R179/R170を一般有限結果集合・作用殻型の代替経路へ残す。Q3はR161/R162の移動過程へ特殊化する。")],
        "sections/03_m47_controlled_w_instrument.md": [("R161は対応する静的平方根kernelを与え、R190/R179がその有限時間選択を物理実現する。選択終了後はR170が吸収指針変数へ結果を固定し、その後に局所記録を作る。", "Q1の2結果主線ではR191がブラウン巨視的スピンの吸引域測度から有限時間Born読出しと吸収記録を与える。R164/R161/R190/R179/R170は一般有限結果集合と作用殻型の代替実現として残す。"), ("次の測定面でのみ新しいR164--R190--R179--R170の整合を走らせる。", "次の測定面でのみ新しいR191読出しを走らせる。")],
        "sections/A2_m47_controlled_w_instrument_proofs.md": [("R164--R190--R179--R170の選択、固定、局所記録、保護帯、制御付き 選別機構、方向を変えない振幅再調整、転送を完全結果核としてまとめ", "R191の選択・固定・無反応、局所記録、制御付き選別機構、必要な方向を変えない振幅再調整、転送を完全結果核としてまとめ"), ("次の測定面でR164--R190--R179--R170を改めて走らせる。", "次の測定面でR191を改めて走らせる。")],
        "sections/04_m54_q2_specializations.md": [("2翼の局所M54静的/R170", "2翼の局所R191")],
        "sections/05_m54_setting_pre_receiver.md": [("2翼のR170を走らせて局所選択を固定し", "2翼のR191を走らせて局所選択を固定し"), ("その容量をR164--R190--R179の静的選択とR170 指針変数固定へ渡す。", "その2容量をR191の作用和・作用差駆動ブラウン巨視的スピン読出しへ渡す。")],
        "sections/A13_m54_template_port_preparation.md": [("Born結果成分、共通射影選別機構の単一装置統合、周期収支", "Born結果成分、R191を含む共通射影選別機構の単一装置統合、周期収支")],
        "sections/08_errors_resources_open_targets.md": [("R143は初期操作面のR170、W型分析器、分析器後のR181Dの深さ1 共通射影選別機構を合成する。", "R143は初期操作面のR191、W型分析器、分析器後のR181Dの深さ1 共通射影選別機構を合成する。")],
        "sections/09_conclusion.md": [("R181Dは深さ2の段階的射影選別を与える。", "R181DはR191の2結果読出しを使う深さ2の段階的射影選別を与える。")],
    }
    for path, reps in replacements.items():
        t = read(path)
        for old, new in reps:
            t = replace_if_present(t, old, new)
        write(path, t)
    p = "sections/08_errors_resources_open_targets.md"
    t = read(p)
    payload = r'''

### R191の2結果読出し誤差と資源

Q1/Q2の2結果主線では、1ノードの読出し誤差を

```math
\varepsilon_{191}
=\max\{\varepsilon_{191}^{\rm int},\varepsilon_{191}^{\rm edge}\}
```

として付録Tから受け取る。内部経路では混合誤差、保護帯、transducer境界誤差、有限温度retreat、有限時間未捕獲、捕獲記録を各1回だけ数え、R164/R190/R170代替経路の同じ選択偏差を重複加算しない。深さ $m$ では各ノード誤差を $O(\epsilon/m)$ とし、$g=O(\epsilon/m)$、$\Delta_{\min}g^2\gtrsim\log(m/\epsilon)$ を十分条件に取れば、R191のdecision障壁は $m,1/\epsilon$ の多項式で選べる。一般深さではbranch作用下限を保つ方向を変えない振幅再調整を残す。
'''
    if "### R191の2結果読出し誤差と資源" not in t:
        marker = "\n## "
        idx = t.find(marker)
        if idx < 0:
            t += payload
        else:
            t = t[:idx] + payload + t[idx:]
    write(p, t)


def patch_q2_receiver_more() -> None:
    p = "sections/05_m54_setting_pre_receiver.md"
    t = read(p)
    t = t.replace("局所R170", "局所R191")
    t = t.replace("2翼R170", "2翼R191")
    t = t.replace("R170局所読出し", "R191局所読出し")
    t = t.replace("R170の局所読出し", "R191の局所読出し")
    write(p, t)


def patch_r181d_appendix() -> None:
    p = "sections/A16_m54_projector_tree_receiver.md"
    t = read(p)
    t = t.replace("R164--R190--R179--R170", "R191")
    t = t.replace("R170の吸収指針変数", "R191の吸収記録")
    t = t.replace("R170誤差", "R191誤差")
    payload = r'''

### R191主読出しと非規格化branchの受渡し

2結果ノードではR191を主読出しとする。結果 $b$ が固定された後の可逆写像 $F_{k,b}$ は従来どおり $P_{k,b}Z$ と補branchを分け、active branchを物理的に規格化しない。次段R191はそのbranch自身の作用和を分母に持つ吸引域境界を作るため、理想条件付き確率は

```math
P(y_k=b\mid y_{<k})
=\frac{\|P_{k,b}Z_{k-1}\|^2}{\|Z_{k-1}\|^2}
```

となる。従って有限段の完全履歴は従来のLüders型telescopingを保つ。方向を変えない振幅再調整は固定小深度では省略できるが、Q2-4の一般深度では作用下限維持のため残す。
'''
    if "### R191主読出しと非規格化branchの受渡し" not in t:
        t += payload
    write(p, t)


def patch_r180_appendices() -> None:
    for p in ("sections/A4_m54_receiver_cycle_proofs.md", "sections/A9_m54_setting_pre_paired_hopf_receiver.md"):
        t = read(p)
        t = t.replace("R164--R190--R179--R170", "R191")
        t = t.replace("局所R170", "局所R191")
        t = t.replace("R170局所", "R191局所")
        write(p, t)


def patch_status() -> None:
    p = "PROJECT_STATUS.md"
    t = read(p)
    intro = "# 固定長期目標、現行モデル、現行結果\n"
    payload = """
## draft-88：R191ブラウン巨視的スピン2結果読出し

- Q1/Q2の2結果射影測定ではR191を主読出しとする。固定した2つの射影作用の和・差を一軸異方性と軸方向biasへ結合し、等方Brownian mixing後の吸引域測度からBorn型2値分布を得る。
- R191は有限混合時間、transducer誤差、保護帯、有限温度retreat、有限decision時間、端点dispatcher、無反応、吸収記録を一つの完全結果核として評価する。
- R164/R190/R170は削除せず、一般有限結果集合、作用殻型の明示実現、Q3固定時刻診断などの代替・強化経路へ残す。
- R181Dの可逆projector routerは維持し、固定小深度では非規格化branchを次段R191へ渡せる。Q2-4の一般深度では作用下限維持の方向を変えない振幅再調整を残す。
- 固定長期目標と達成ラベルは変更しない。

"""
    if "## draft-88：R191ブラウン巨視的スピン2結果読出し" not in t:
        t = replace_once(t, intro, intro + payload, "status intro")
    t = replace_if_present(t, "R170の容量結合、作用殻、信号保持、混合・衝突、収集、結果固定をQ1・Q2で共有する有限能動部分系＋Hamiltonian無限浴の単一ミクロ装置へ統合する。R190A--R190Cにより無限Drude浴を許す静的作用比分配bridgeは追加されたが、容量固定機構から浴、反復衝突のrenewal、収集、lockまでの単一装置統合は未解決である。", "R191の作用和・作用差transducer、Brownian mixing、decision、吸収記録、既存projector routerをQ1・Q2で共有する一つの能動装置へ統合し、有限帯域・有限温度・実素子較正を実験可能な範囲へ落とす。R164/R190/R170の作用殻型代替経路については単一装置統合を強化課題として残す。")
    write(p, t)


def patch_dependency_ledger() -> None:
    p = "tools/build_paper.py"
    t = read(p)
    t = replace_once(t, "    56: \"kubo_hashitsume1970\",\n}", "    56: \"kubo_hashitsume1970\",\n    57: \"brown1963\",\n    58: \"grinstein_koch2005\",\n}", "reference keys")
    t = replace_once(t, "    \"R170\": {\"R190C\", \"R179\"},\n", "    \"R170\": {\"R190C\", \"R179\"},\n    \"R191\": set(),\n", "R191 dependency")
    t = replace_once(t, "    \"R181D\": {\"R112\", \"R170\", \"R181A\"},", "    \"R181D\": {\"R112\", \"R191\", \"R181A\"},", "R181D deps")
    t = replace_once(t, "    \"R180A\": {\"R181C\", \"R170\"},", "    \"R180A\": {\"R181C\", \"R191\"},", "R180A deps")
    t = replace_once(t, "    \"R180C\": {\"R181B\", \"R170\", \"R180A\", \"R180B\"},", "    \"R180C\": {\"R181B\", \"R191\", \"R180A\", \"R180B\"},", "R180C deps")
    t = t.replace("\"SOURCE_DATE_EPOCH\": \"1788739200\"", "\"SOURCE_DATE_EPOCH\": \"1788998400\"")
    write(p, t)

    deps = {"R190A":{"R164"},"R190B":{"R190A"},"R190C":{"R161","R190B"},"R170":{"R190C","R179"},"R191":set(),"R181B":{"R112"},"R181C":{"R112","R181B"},"R181D":{"R112","R191","R181A"},"R177":{"R181B","R181C","R181D"},"R179":set(),"R186":{"R181C","R181D","R179"},"R180A":{"R181C","R191"},"R180B":{"R181A"},"R180C":{"R181B","R191","R180A","R180B"}}
    roots = {"Q2-1":{"R181B","R181C","R181D"},"Q2-2":{"R180C"},"Q2-3":{"R177"},"Q2-4":{"R179","R186"}}
    def closure(rs: set[str]) -> set[str]:
        out=set(rs); stack=list(rs)
        while stack:
            r=stack.pop()
            for d in deps.get(r,set()):
                if d not in out: out.add(d); stack.append(d)
        return out
    def key(r: str):
        m=re.fullmatch(r"R(\d+)([A-Z]?)",r); return (int(m.group(1)),m.group(2)) if m else (10**9,r)
    status=read("PROJECT_STATUS.md"); lines=status.splitlines()
    for i,line in enumerate(lines):
        if not any(line.startswith(f"| {goal} | 条件付き達成 |") for goal in roots): continue
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        goal=cells[0]
        if len(cells)<7: continue
        cells[5]="、".join(sorted(closure(roots[goal]),key=key))
        lines[i]="| "+" | ".join(cells)+" |"
    write("PROJECT_STATUS.md","\n".join(lines)+"\n")


def patch_references() -> None:
    p="sections/90_references.md"; t=read(p)
    if "- [57] W. F. Brown, Jr." not in t:
        t=t.rstrip()+"\n- [57] W. F. Brown, Jr., ``Thermal Fluctuations of a Single-Domain Particle,'' Physical Review 130, 1677--1686 (1963). <https://doi.org/10.1103/PhysRev.130.1677>\n- [58] G. Grinstein and R. H. Koch, ``Switching Probabilities for Single-Domain Magnetic Particles,'' Physical Review B 71, 184427 (2005). <https://doi.org/10.1103/PhysRevB.71.184427>\n"
    write(p,t)
    p="references.bib"; t=read(p)
    if "@article{brown1963," not in t:
        t=t.rstrip()+r'''

@article{brown1963,
  author = {Brown, William F., Jr.},
  title = {Thermal Fluctuations of a Single-Domain Particle},
  journal = {Physical Review},
  volume = {130},
  pages = {1677--1686},
  year = {1963},
  doi = {10.1103/PhysRev.130.1677}
}

@article{grinstein_koch2005,
  author = {Grinstein, G. and Koch, R. H.},
  title = {Switching Probabilities for Single-Domain Magnetic Particles},
  journal = {Physical Review B},
  volume = {71},
  pages = {184427},
  year = {2005},
  doi = {10.1103/PhysRevB.71.184427}
}
'''
    write(p,t)


def patch_version_and_docs() -> None:
    p="CITATION.cff"; t=read(p); t=t.replace('version: "draft-87"','version: "draft-88"'); t=re.sub(r"date-released: \d{4}-\d{2}-\d{2}","date-released: 2026-09-10",t); write(p,t)
    p="tools/template.tex"; t=read(p); t=t.replace("draft-87 改訂稿","draft-88 改訂稿"); write(p,t)
    p="README.md"; t=read(p); marker="量子、なんもわからん。\n"; payload="\n> **draft-88:** Q1/Q2の2結果射影読出しにR191ブラウン巨視的スピンinstrumentを追加した。射影作用の和・差を吸引域境界へ直接結合し、有限温度・有限時間・transducer誤差・無反応を含むBorn型2値読出しを共通化する。R164/R190/R170は一般有限結果集合と作用殻型の代替経路として残す。\n"; t=insert_after(t,marker,payload,"README summary"); write(p,t)
    for p,title,payload in [
        ("CHANGELOG.md","## draft-88：R191ブラウン巨視的スピン2結果読出し","\n## draft-88：R191ブラウン巨視的スピン2結果読出し\n\n- R191を追加し、Q1/Q2の2結果射影ノードの主読出しを、射影作用和・作用差で駆動するブラウン巨視的スピンの吸引域捕獲へ整理した。\n- 有限混合時間、transducer誤差、保護帯、有限温度retreat、有限decision時間、端点dispatcher、無反応、吸収記録を完全結果分布の明示誤差へまとめた。\n- R181Dの可逆projector routerを維持し、固定小深度では非規格化branchを次段へ直接渡す。Q2-4一般深度では方向を変えない振幅再調整を残す。\n- R164/R190/R170は削除せず、一般有限結果集合・作用殻型の代替実現として維持した。固定目標と達成ラベルは変更しない。\n- Brown 1963 と Grinstein--Koch 2005 を基礎文献として追加した。\n\n"),
        ("MANIFEST.md","## draft-88のR191読出し再編","\n## draft-88のR191読出し再編\n\n- 付録T `sections/A20_m54_brownian_macrospin_projective_instrument.md` を追加。\n- `tools/verify_r191_macrospin.py` を追加し、Born吸引域恒等式、transducer誤差、Itô変換、scale density、有限時間上界、端点dispatcher、Lüders telescopingを検算する。\n- Q1/Q2の2結果主線をR191へ接続し、R164/R190/R170を代替・強化経路として保持する。\n- draft-88の `paper.md`、`main.tex`、`paper.pdf` は `tools/build_paper.py` から再生成する。\n\n"),
        ("VALIDATION.md","## draft-88：R191ブラウン巨視的スピン読出し検証","\n## draft-88：R191ブラウン巨視的スピン読出し検証\n\n- `tools/verify_r191_macrospin.py` でBorn吸引域恒等式、作用和・作用差transducer誤差、`artanh` Itô変換、scale density、retreat/finite-time上界、端点dispatcher、逐次Lüders telescopingを独立に検算する。\n- R191定理は本文で1回だけ定義し、R164/R190/R170を削除しない。Q2-2は二つの物理測定端を維持し、中央集約4結果samplerへ変更しない。\n- Q2-4一般深度では方向を変えない振幅再調整を維持する。\n- `tools/build_paper.py` で統合Markdown、TeX、PDFを再生成し、通常の全 `verify_*.py`、生成物同期、TeX警告、PDF情報をCIで再確認する。\n\n")]:
        t=read(p)
        if title not in t:
            m=re.search(r"^# .*?\n",t,flags=re.M)
            if not m: raise RuntimeError(f"{p} heading missing")
            t=t[:m.end()]+payload+t[m.end():]
        write(p,t)


def patch_terminology() -> None:
    p="TERMINOLOGY.md"; t=read(p)
    payload="""

## draft-88で追加する測定語

| 標準表記 | 意味 |
|---|---|
| ブラウン巨視的スピン | 熱揺らぎと散逸を受ける固定長単磁区磁化を、R191の2結果指針変数として使うときの表記 |
| 確率的LLG方程式 | Landau--Lifshitz--Gilbert型磁化方程式へ熱揺らぎを加えた採用開放方程式 |
| 吸引域 | decision力学で最終的に同じ結果へ捕獲される初期指針状態の集合 |
| 吸引域境界 | 2つの吸引域を分ける不安定境界 |
| 保護帯 | 吸引域境界の近傍を有限幅で無反応へ送る安全領域 |
| 捕獲領域 | 結果を吸収記録へ写すために定める各極近傍の領域 |
"""
    if "## draft-88で追加する測定語" not in t: t += payload
    write(p,t)


def patch_workflow() -> None:
    p=".github/workflows/verify.yml"; t=read(p)
    t=t.replace('version: "draft-87"','version: "draft-88"').replace("draft-87 改訂稿","draft-88 改訂稿")
    if "sections/A20_m54_brownian_macrospin_projective_instrument.md" not in t:
        anchor="            sections/A19_m54_drude_action_shell_bridge.md \\\n"
        if anchor in t: t=t.replace(anchor,anchor+"            sections/A20_m54_brownian_macrospin_projective_instrument.md \\\n",1)
    if "test -f tools/verify_r191_macrospin.py" not in t:
        anchor="          test -f tools/verify_r190_drude_shell.py\n"
        t=t.replace(anchor,anchor+"          test -f tools/verify_r191_macrospin.py\n          test \"$(grep -Rho '定理（R191：' sections/*.md | wc -l)\" -eq 1\n",1)
    write(p,t)


def patch_build_validation_tokens() -> None:
    p="tools/build_paper.py"; t=read(p)
    anchor='    if "定理（R181D：M54段階的射影選別・測定後状態受渡し定理）" not in common_text:\n        raise ValueError("R181D新定理名がない")\n'
    extra='    if "定理（R191：作用差駆動ブラウン巨視的スピン2結果射影読出し）" not in common_text:\n        raise ValueError("R191主読出し定理がない")\n    if "R164/R190/R170は一般有限結果集合" not in common_text:\n        raise ValueError("R191と旧作用殻経路の責務境界がない")\n'
    if "R191主読出し定理がない" not in t and anchor in t: t=t.replace(anchor,anchor+extra,1)
    write(p,t)


def main() -> None:
    patch_common(); patch_source_summaries(); patch_q2_receiver_more(); patch_r181d_appendix(); patch_r180_appendices(); patch_status(); patch_dependency_ledger(); patch_references(); patch_version_and_docs(); patch_terminology(); patch_workflow(); patch_build_validation_tokens()
    print("R191 source revision applied")


if __name__ == "__main__":
    main()
