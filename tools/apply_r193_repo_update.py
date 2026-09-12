#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str, *, required: bool = True) -> str:
    count = text.count(old)
    if count == 0:
        if required:
            raise AssertionError(f"missing replacement marker: {label}")
        return text
    if count != 1:
        raise AssertionError(f"replacement marker not unique ({count}): {label}")
    return text.replace(old, new, 1)


def append_once(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n" + block.rstrip() + "\n"


def update_section_03() -> None:
    rel = "sections/03_m47_controlled_w_instrument.md"
    text = read(rel)
    text = text.replace(
        "R143--R144、R189A--R189Cの有限Rabi--Zeno比較へ接続する。",
        "R143--R144、R189A、R193、R189B--R189Cの有限Rabi--Zeno比較へ接続する。",
    )
    text = text.replace(
        "R189A終了後は固定済み左右作用 $\\bar J_L,\\bar J_R$ を走行中W2信号から切り離してR191へ渡し、",
        "R189A終了後は固定済み左右作用 $\\bar J_L,\\bar J_R$ を走行中W2信号から切り離し、付録UのR193でR191のdecision energyへ直接結合し、",
    )
    text = text.replace(
        "保持済み2作用をR191へ渡し、有限decision時間後に潜在結果",
        "保持済み2作用をR193でR191 decision energyへ直接結合し、有限decision時間後に潜在結果",
    )
    text = text.replace(
        "R135、R140、R187、R189A--R189C、R191",
        "R135、R140、R187、R189A、R193、R189B--R189C、R191",
    )
    text = text.replace(
        "R140、R143--R144、R168、R181D、R187、R189A--R189C、R191",
        "R140、R143--R144、R168、R181D、R187、R189A、R193、R189B--R189C、R191",
    )
    text = text.replace(
        "R189A--R189Cは",
        "R189A、R193、R189B--R189Cは",
    )
    text = text.replace(
        "R191 transducer、Brownian macrospin、R181D routerをM37",
        "R191 Brownian macrospin、R181D router、fresh-latch/resetをM37",
    )
    write(rel, text)


def update_r191_appendix() -> None:
    rel = "sections/A20_m54_brownian_macrospin_projective_instrument.md"
    text = read(rel)
    block = r'''## T.11 Q1のR193直接decision接続

R191本体はQ1/Q2で共有する一般instrumentなので、第T.2節のtransducer契約を維持する。Q1 W型2モード特殊化では、R189Aが保持した正準座標 $A_L,A_R$ を付録UのR193で直接decision energyへ結合し、

```math
\widehat S=A_L+A_R,
\qquad
\widehat D=A_L-A_R
```

を実現する。この特殊化ではR189Aで既に数えた作用比偏差をR191 transducer誤差へ重複加算せず、R193固有の接続偏差だけを $\varepsilon_{193}^{u}$ として数える。

また端点条件 $A_L/(A_L+A_R)<\tau_{\rm cut}$ は

```math
(1-\tau_{\rm cut})A_L
-\tau_{\rm cut}A_R
<0
```

と同値なので、Q1では状態依存除算を実行せず固定線形比較器でdispatcherを構成できる。decision後の使用済み保持対は共役運動量にmacrospin履歴を持つため、次回capture前にfresh pairへSWAPするかR179へ切り離す。

R193はQ1専用特殊化であり、Q2-1--Q2-4の一般R191 transducer契約を変更しない。
'''
    text = append_once(text, "## T.11 Q1のR193直接decision接続", block)
    write(rel, text)


def update_section_02() -> None:
    rel = "sections/02_common_canonical_modules.md"
    text = read(rel)
    old = "R191は、transducer、ブラウン巨視的スピン、射影成分生成、記録、resetを単一閉鎖Hamiltonianへ統合済みだと主張しない。"
    new = "R191は、ブラウン巨視的スピン、射影成分生成、記録、resetを単一閉鎖Hamiltonianへ統合済みだと主張しない。Q1 W2特殊化ではR189A保持座標からR193によりdecision energyまでを直接接続するが、Q2の一般transducerと全周期統合は未完成である。"
    if old in text:
        text = text.replace(old, new, 1)
    write(rel, text)


def update_section_08() -> None:
    rel = "sections/08_errors_resources_open_targets.md"
    text = read(rel)
    marker = "## 8.4 Q1の系列固有誤差\n"
    insert = r'''## 8.4 Q1の系列固有誤差

### R193の直接decision接続誤差とfresh-latch資源

Q1 W2主線ではR189Aの保持済み作用比をR193でR191 decision energyへ直接結合する。R189Aで既に計上した作用比誤差を一般R191 transducer誤差として重複計上しない。R193固有の有限gate、結合較正、時計偏差から生じる吸引域境界誤差を $\varepsilon_{193}^{u}$ とし、Q1特殊化したR191内部誤差を

```math
\varepsilon_{191|193}^{\rm int}
=
\varepsilon_{\rm mix}
+g
+\frac{\varepsilon_{193}^{u}}{2}
+q_{\rm ret}
+q_{\rm time}
+\varepsilon_{\rm cap}
```

とする。端点側は

```math
\varepsilon_{191|193}^{\rm edge}
=
\tau_{\rm cut}
+\frac{\varepsilon_{193}^{u}}{2}
+\varepsilon_{\rm cap}
```

でよい。従って走行中測定では

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+\varepsilon_{191|193}
+\varepsilon_{\rm lat}
```

とし、同じR189A偏差を2回加えない。

R193 decision中は保持座標 $A_L,A_R$ が固定される一方、共役運動量 $P_b^J$ には履歴が残る。固定有限深さでは未使用保持対との正準SWAPを用意すればよい。反復装置ではused latchをR179へ流してfresh pairを供給する。このfresh-latch/reset時間と有限SWAP誤差は次回captureの入力誤差へ一度だけ含める。

R191の等方mixingは保持作用を必要としないため、W2発展およびR189A captureと並行して実行してよい。R189Bのlatencyにはcapture中心時刻からR181D完了までの実時間差を入れ、事前mixing時間全体を機械的に加えない。
'''
    if "### R193の直接decision接続誤差とfresh-latch資源" not in text:
        text = replace_once(text, marker, insert, "section 8.4 heading")
    text = text.replace(
        "R189CのQ1-2達成証人では中間R189Aで保持した2作用をR191へ渡し、",
        "R189CのQ1-2達成証人では中間R189Aで保持した2作用をR193でR191 decision energyへ直接結合し、",
    )
    write(rel, text)


def update_overview_and_conclusion() -> None:
    for rel in ("sections/00_overview_and_contents.md", "sections/09_conclusion.md"):
        text = read(rel)
        text = text.replace("R189A--R189C", "R189A、R193、R189B--R189C")
        if rel.endswith("09_conclusion.md") and "R193はR189Aの保持座標" not in text:
            needle = "Born結果形成をW型粒子位置の再平衡化へ依存させない。"
            if needle in text:
                text = text.replace(
                    needle,
                    needle + " R193はR189Aの保持座標をR191 macrospinのdecision energyへ直接Hamiltonian結合し、Q1に残っていた抽象transducer接続を具体化する。",
                    1,
                )
        write(rel, text)


def update_project_status() -> None:
    rel = "PROJECT_STATUS.md"
    text = read(rel)
    draft = r'''## draft-91：R193 Q1作用保持--macrospin直接decision接続

- R193を追加し、R189Aが保持したQ1 W2左右作用座標をR191ブラウン巨視的スピンのdecision energyへ直接Hamiltonian結合する。
- decision中の保持座標不変、W2への直接反作用零、R189A作用比誤差から吸引域境界への $2\varepsilon_{189A}$ 評価、endpointの除算不要な線形比較を明示する。
- decision後の保持対共役運動量にmacrospin履歴が残るため、次回capture前のfresh-latch SWAPまたはR179 open resetを必須境界とする。
- R193はQ1専用特殊化であり、Q2の一般R191 transducer契約を変更しない。Q1-1/Q1-2の達成ラベルと固定目標は変更しない。
- M0全体は未達のまま。Q1ではW2作用保持からmacrospin decision energyまでが具体化し、残件はmacrospin浴、吸収記録、R181D router、fresh-latch/reset、共通clockの全周期統合へ縮約する。

'''
    if "## draft-91：R193 Q1作用保持--macrospin直接decision接続" not in text:
        text = replace_once(
            text,
            "# 固定長期目標、現行モデル、現行結果\n\n",
            "# 固定長期目標、現行モデル、現行結果\n\n" + draft,
            "PROJECT_STATUS title",
        )
    text = text.replace("R189A--R189C", "R189A、R193、R189B--R189C")
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("| Q1-2 |"):
            parts = line.split("|")
            if len(parts) >= 9:
                evidence = parts[6]
                if "R193" not in evidence:
                    evidence = evidence.replace("R189A", "R189A、R193")
                parts[6] = evidence
                parts[7] = " R193でR189A保持座標からmacrospin decision energyまでを直接接続。残る強化課題はmacrospin浴、吸収記録、R181D router、fresh-latch/reset、共通clockの一周期統合と全周期収支 "
                lines[idx] = "|".join(parts)
            break
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    old1 = "1. R191の作用和・作用差変換器、ブラウン巨視的スピン、有限温度の決定過程、吸収記録、R181Dの射影成分振り分けを、Q1/Q2で共有できる一つの具体的な能動装置へ統合し、帯域、温度、較正誤差を実装模型から評価する。"
    new1 = "1. Q1ではR193によりR189A作用保持座標からmacrospin decision energyまでを直接接続した。Q2では4、8、一般 $2^n$ モードからR191へ入る一般transducerを、各系列の永続記憶部と同じ具体的能動装置へ統合し、帯域、温度、較正誤差を実装模型から評価する。"
    text = text.replace(old1, new1)
    old2 = "2. R187のM37 W2信号系、射影作用保持、R191読出し、R181Dの射影成分振り分け、外部記録、必要なR179開放リセットを同じ具体装置と時計自由度で接続し、Q1測定部分系の単一装置統合と周期収支を閉じる。"
    new2 = "2. R187のM37 W2信号系、R189A作用保持、R193 decision接続、R191 macrospin浴・吸収記録、R181Dの射影成分振り分け、fresh-latch SWAP／R179 open resetを同じ具体装置と時計自由度で接続し、Q1測定部分系の単一装置統合と周期収支を閉じる。"
    text = text.replace(old2, new2)
    write(rel, text)


def update_validation_manifest_changelog() -> None:
    validation = read("VALIDATION.md")
    validation = append_once(
        validation,
        "## draft-91：R193直接decision接続の検算",
        r'''## draft-91：R193直接decision接続の検算

- `tools/verify_q1_r193_macrospin_bridge.py` で、保持座標からR191吸引域境界への恒等式、作用比誤差から境界誤差への係数2、共通gain不変性、endpoint dispatcherの線形比較同値性、decision後共役運動量の有限上界、R189A誤差の二重計数除去を独立に検算する。
- R193の正式宣言は付録Uに1回だけ置き、R191一般定理は変更しない。Q2の一般transducerはR193へ依存させない。
- Q1-1/Q1-2の達成ラベルと固定目標は変更しない。R193後もM0全体は未達とし、Q1全周期のmacrospin浴、記録、router、fresh-latch/reset統合を強化課題として残す。
- `paper.md`、`main.tex`、`paper.pdf` を章別原稿から再生成し、通常のsource/terminology/physics/generated-artifact検査を全て通す。
''',
    )
    write("VALIDATION.md", validation)

    manifest = read("MANIFEST.md")
    manifest = append_once(
        manifest,
        "## draft-91のR193 Q1直接decision接続",
        r'''## draft-91のR193 Q1直接decision接続

- 付録U `sections/A21_q1_r193_macrospin_bridge.md` を追加し、R189A保持座標からR191 macrospin decision energyへのQ1専用直接Hamiltonian接続R193を正本化。
- `tools/verify_q1_r193_macrospin_bridge.py` を追加し、吸引域境界、誤差係数、dispatcher、fresh-latch境界を検算。
- Q1主線を `M37 W2 -> R189A -> R193 -> R191 -> R181D` へ同期し、Q2の一般R191 transducer契約は維持。
- `paper.md`、`main.tex`、`paper.pdf` は章別原稿から再生成する。
''',
    )
    write("MANIFEST.md", manifest)

    changelog = read("CHANGELOG.md")
    if not changelog.startswith("## draft-91：R193"):
        block = r'''## draft-91：R193 Q1作用保持--macrospin直接decision接続

- R193を追加し、R189Aが保持した左右作用座標をR191ブラウン巨視的スピンのdecision energyへ直接Hamiltonian結合した。
- decision中の保持座標不変、W2への直接反作用零、吸引域境界誤差、endpoint線形dispatcher、decision後共役運動量のfresh-latch条件を明示した。
- Q1の誤差台帳ではR189A作用比誤差をR191 transducer誤差へ二重計上せず、R193固有の接続偏差だけを追加する。
- Q2の一般R191 transducer契約は変更せず、M0全体とQ1全周期統合は未完成の強化課題として維持する。
- 付録U、R193専用検算器、状態表、概要、誤差・資源台帳、結論、manifest、validation、統合原稿、TeX、PDFを同期する。

'''
        changelog = block + changelog
    write("CHANGELOG.md", changelog)


def main() -> None:
    update_section_03()
    update_r191_appendix()
    update_section_02()
    update_section_08()
    update_overview_and_conclusion()
    update_project_status()
    update_validation_manifest_changelog()
    print("r193_repository_update_ok")


if __name__ == "__main__":
    main()
