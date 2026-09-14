#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def save(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(path: str, old: str, new: str, count: int = 1) -> None:
    text = load(path)
    if old not in text:
        raise SystemExit(f"{path}: required text not found: {old[:100]!r}")
    save(path, text.replace(old, new, count))


def replace_if_present(path: str, old: str, new: str) -> None:
    text = load(path)
    if old in text:
        save(path, text.replace(old, new))


def prepend_once(path: str, marker: str, block: str) -> None:
    text = load(path)
    if marker not in text:
        save(path, block.rstrip() + "\n\n" + text)


def replace_prefixed_line(path: str, prefix: str, newline: str) -> None:
    lines = load(path).splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        raise SystemExit(f"{path}: expected one line starting {prefix!r}, found {len(hits)}")
    lines[hits[0]] = newline
    save(path, "\n".join(lines) + "\n")


def main() -> None:
    prepend_once(
        "PROJECT_STATUS.md",
        "## draft-101：M58 Q3共通ミクロ模型",
        """## draft-101：M58 Q3共通ミクロ模型とR197統合

- M37 signal subsystem、thermostatted 2-action shell、M57 transport subsystemを同一試行上のM58へ統合し、R197A--R197CとR197を追加する。
- Q3-1はM58のsignal marginalからR86へ、Q3-2は同じM58のfull tracer marginalからR196A--R196C、R161、R185へ進む。固定目標の定義と達成ラベルは変更しない。
- A12の状態数自由エネルギーをR197A/Bの実際のGibbs周辺化へ接続し、A22で従来入力していた $-k_BT\\log R^\\delta$ を同じM58 shellの平均力として導出する。
- Q3-1-A1とQ3-2-A1をM58/R197により達成へ上げる。A2はM58採用SDE/PDEの直接数値再現が未実施なので未監査のまま保持する。""",
    )
    replace_prefixed_line(
        "PROJECT_STATUS.md",
        "| Q3-1 | 達成 |",
        "| Q3-1 | 達成 | M58共通Q3ミクロ模型のsignal marginal | M37実正準空間信号＋thermostatted shell/TL弱負荷 | Schrödinger型空間包絡 | R86、R197C、R197 | clock・終位置record・resetを含む反復周期、A2直接数値再現は強化課題 |",
    )
    replace_prefixed_line(
        "PROJECT_STATUS.md",
        "| Q3-2 | 達成 |",
        "| Q3-2 | 達成 | M58共通Q3ミクロ模型 | 同一試行のM37信号＋thermostatted 2-action shell＋M57 dual-ballistic-TL moving-bath tracer | Nelson型位置過程・時間対称Newton則 | R197、R195A、R196A--R196C、R161、R185 | R185の正則化・格子残差を分離。clock・record・reset反復周期、連続空間一様極限、多粒子は強化課題 |",
    )

    replace_required(
        "sections/06_m37_spatial_envelope.md",
        "Q3の親模型は第2章のM54空間信号構成とM57 dual-ballistic-TL moving-bath tracerである。",
        "Q3の共通親模型は付録WのM58であり、M37をsignal subsystem、M57をtransport subsystemとして同一試行上に結合する。",
    )
    replace_required(
        "sections/06_m37_spatial_envelope.md",
        "安全な開始面から同じ試行の信号をM57へ渡す。",
        "M58では開始時から同じ試行のM37信号、thermostatted shell、M57 transport、tracerが共存し、信号を後段へ再標本化して受け渡さない。",
    )
    replace_required(
        "sections/06_m37_spatial_envelope.md",
        "M54の接続端、M37局所ばね網、M57 dual-ballistic-TL moving-bath tracer、時計自由度、記録器を単一反復装置へ統合したとは扱わない。",
        "M37信号とM57 tracerの同一試行統合はR197で閉じる。時計、終位置記録、resetまで含む単一反復周期は別の強化課題として残す。",
    )
    replace_if_present(
        "sections/06_m37_spatial_envelope.md",
        "Q3-1の固定達成基準はM37から有効空間包絡への縮約であり、R86が満たす。",
        "Q3-1の固定達成基準はM58のsignal marginalから有効空間包絡への縮約であり、裸のM37についてR86、M58のshell/TL負荷を含む安定性についてR197C/R197が満たす。",
    )

    anchor = "粗視化後の確率過程と微視的な仕事・熱を同一視するには追加条件が必要である [50,51]。"
    text = load("sections/A12_common_action_shell_state_count.md")
    addition = anchor + "\n\nQ3のM58では付録WのR197A/Bがこの追加条件を具体化する。2-action shellを明示Langevin浴で熱化し、その条件付きGibbs分布を実際に周辺化するため、そこで初めて $-k_BT\\log R^\\delta$ をpotential of mean forceとして使用する。"
    if addition not in text:
        if anchor not in text:
            raise SystemExit("A12 mean-force caution anchor not found")
        save("sections/A12_common_action_shell_state_count.md", text.replace(anchor, addition, 1))

    replace_required(
        "sections/A22_m57_dual_tl_tracer_microphysics.md",
        "同じ状態数sectorのpotential of mean forceは $-k_BT\\log R^\\delta$ を与える。",
        "同じ状態数sectorの容量は $R^\\delta$ に比例する。これを実際のpotential of mean forceとして動力学的に実現するthermostatted shellと有限時間averagingは付録WのR197A/Bで与える。",
    )
    old = """slow potentialは

```math
V_{\\rm eff}(X,Z)
=V_{\\rm per}(X)-k_BT\\log R^\\delta(X,Z)
```

とする。Ohmic/Markov極とoverdamped極で"""
    new = """R197A/Bで同じ試行のthermostatted shellを消去すると、tracerへ作用する平均shell力は

```math
F_{\\rm sh}(X,Z)
=k_BT[1-\\Delta(x(A))]\\partial_X\\log R^\\delta(X,Z)
```

となり、finite-width誤差 $\\varepsilon_{\\rm width}$ とfast--slow averaging誤差 $\\varepsilon_{\\rm sh,av}$ が明示的に付く。strict-shell/fast-shell極では従来の $-k_BT\\log R^\\delta$ 表示へ一致する。Ohmic/Markov極とoverdamped極で"""
    replace_required("sections/A22_m57_dual_tl_tracer_microphysics.md", old, new)
    replace_if_present(
        "sections/A22_m57_dual_tl_tracer_microphysics.md",
        "M57はQ3の粒子位置輸送に対する現行ミクロ模型である。",
        "M57はM58内のQ3粒子位置輸送subsystemである。",
    )

    replace_if_present(
        "README.md",
        "Q3では、M37/M54空間信号からM57 dual-ballistic-TL moving-bath tracerへ接続し、R161が定めるcanonical Markov経路法則とR185を通してSchrödinger型有効力学、Nelson型の時間対称Newton則、井戸型・調和型・W型の束縛状態、トンネル効果、2経路干渉まで進んでいます。位相量子化は未達です。",
        "Q3では、M37局所古典振動子signal、thermostatted 2-action shell、M57 dual-ballistic-TL moving-bath tracerを同じM58古典開放模型へまとめています。signal marginalだけを見ればR86のSchrödinger型有効力学、同じ試行のtracerまで見ればR196A--R196C、R161、R185を通してNelson型の時間対称Newton則へ縮約します。井戸型・調和型・W型の束縛状態、トンネル効果、2経路干渉まで進んでおり、位相量子化は未達です。",
    )
    for path in ("sections/00_overview_and_contents.md", "sections/01_scope_and_cycle.md", "sections/09_conclusion.md"):
        replace_if_present(path, "M37/M54空間信号からM57 dual-ballistic-TL moving-bath tracerへ接続", "M58共通ミクロ模型のM37 signal subsystemとM57 transport subsystemを同一試行上で接続")
        replace_if_present(path, "M37/M54空間信号、M57 dual-ballistic-TL moving-bath tracer", "M58共通ミクロ模型（M37 signal＋thermostatted shell＋M57 transport）")
    replace_if_present(
        "sections/01_scope_and_cycle.md",
        "Q3-2の達成根拠はM57/R195A・R196A--R196Cの明示ballistic-TL/moving-bath/tracer縮約である。",
        "Q3-1/Q3-2の共通達成証人はM58/R197である。Q3-1は同じ模型のM37 signal marginal、Q3-2はthermostatted shellとM57 transportを含むfull tracer marginalからR161/R185へ進む。",
    )

    old_open = "M37信号源--M57 tracer--時計--終位置記録の単一反復周期統合"
    new_open = "M58 common process--時計--終位置記録--resetの単一反復周期統合"
    replace_if_present("sections/08_errors_resources_open_targets.md", old_open, new_open)
    replace_if_present("ENHANCEMENT_TARGETS.md", old_open, new_open)
    replace_if_present("sections/09_conclusion.md", old_open, new_open)

    path = "ENHANCEMENT_TARGETS.md"
    text = load(path)
    start = text.index("## 強化目標の現在地表")
    end = text.index("## 既存の実装強化課題との関係", start)
    head, current, tail = text[:start], text[start:end], text[end:]
    out: list[str] = []
    seen: set[str] = set()
    for line in current.splitlines():
        if line.startswith("| Q3-1 |") or line.startswith("| Q3-2 |"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            cells[1] = "達成"
            cells[2] = "未監査"
            line = "| " + " | ".join(cells) + " |"
            seen.add(cells[0])
        out.append(line)
    if seen != {"Q3-1", "Q3-2"}:
        raise SystemExit(f"enhancement current rows not found: {seen}")
    current = "\n".join(out) + "\n"
    note = "\nQ3-1-A1とQ3-2-A1は、M58/R197により同一の明示古典開放模型内で必要因果鎖が閉じたため達成とする。Q3-1-A2/Q3-2-A2は、採用したM58のODE/SDE/PDEそのものを直接数値発展する検証が未実施なので未監査のままとする。\n\n"
    if note.strip() not in current:
        current += note
    save(path, head + current + tail)

    path = "sections/08_errors_resources_open_targets.md"
    text = load(path)
    if "\\varepsilon_{\\rm sh,av}" not in text:
        insert = r"""

### M58共通模型の追加誤差台帳

Q3-1側のsignal誤差を

```math
\varepsilon_{\rm sig}^{58}
=\varepsilon_{86}
+\varepsilon_{\rm port\to sig}
+\varepsilon_{\rm sh\to sig}
```

とまとめる。Q3-2側では同じ上流誤差を二重計上せず、

```math
\begin{aligned}
\varepsilon_{58}
\leq C_{58}(&
\varepsilon_{\rm sig}^{58}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sh,av}
+\varepsilon_{\rm port}
+\varepsilon_{\rm prop}
+\varepsilon_{\rm track}\\
&+\varepsilon_{\rm load}
+\varepsilon_{\rm GLE}
+\varepsilon_{\rm od}
+\varepsilon_{\rm hom}
+\varepsilon_{\rm EK}
+a^2)
\end{aligned}
```

とする。R197により $D_{\rm TV}(p_t^{58},p_t^{161})\leq T\varepsilon_{58}$ であり、R185の $O(\delta)$ 正則化残差と $C_{185,a}a^2$ はその下流で別に数える。
"""
        save(path, text.rstrip() + insert + "\n")

    prepend_once(
        "MANIFEST.md",
        "## draft-101：M58 Q3共通ミクロ模型",
        """## draft-101：M58 Q3共通ミクロ模型とR197統合

- `sections/A23_q3_common_micro_model.md` を追加し、R197A--R197CとR197でQ3-1/Q3-2を同一M58過程の異なる周辺縮約として統合する。
- `tools/verify_q3_common_micro_model.py` を追加し、M37--M57辞書、shell分配関数・平均力・二乗平均、finite-width補正、共通weak scaling、時間尺度窓を検算する。
- A12/A22、第0・1・6・8・9章、README、PROJECT_STATUS、ENHANCEMENT_TARGETS、VALIDATION、CHANGELOGと生成物を同期する。""",
    )
    replace_required("MANIFEST.md", "- `sections/A22_m57_dual_tl_tracer_microphysics.md`", "- `sections/A22_m57_dual_tl_tracer_microphysics.md`\n- `sections/A23_q3_common_micro_model.md`")
    replace_required("MANIFEST.md", "- `tools/verify_m57_ballistic_tracer.py`", "- `tools/verify_m57_ballistic_tracer.py`\n- `tools/verify_q3_common_micro_model.py`")

    prepend_once(
        "CHANGELOG.md",
        "## draft-101：M58 Q3共通ミクロ模型",
        """## draft-101：M58 Q3共通ミクロ模型とR197統合

- M37 signal、thermostatted 2-action shell、M57 transportを同一試行M58へ統合し、R197A--R197Cと主定理R197を追加した。
- Q3-1/Q3-2の固定目標と達成ラベルは変更せず、達成証人をM58へ一本化した。Q3-1はsignal marginal、Q3-2はfull tracer marginalとして同じ模型から得る。
- A12の状態数自由エネルギーを実際のGibbs周辺化へ接続し、R196Bのosmotic forceへfinite-widthとfast--slow averaging誤差を追加した。
- Q3-1-A1/Q3-2-A1を達成へ更新し、A2は未監査のまま保持した。""",
    )
    prepend_once(
        "VALIDATION.md",
        "## draft-101：M58 Q3共通ミクロ模型",
        """## draft-101：M58 Q3共通ミクロ模型の検算

- `tools/verify_q3_common_micro_model.py` で $\mathcal J_0=2m\nu$ によるM37--M57辺結合一致、finite-width 2-action shellの分配関数、平均generalized force、二乗平均を数値積分と閉形式で照合する。
- $\Delta(x)$ の単調減少、$x=3$ での有限幅誤差、$\mu_{\rm sh}\propto\epsilon^{-4-\zeta}$ によるgenerator-level $O(\epsilon^\zeta)$ とstrong $O(\epsilon^{\zeta/2})$、M37平均shell反作用 $O(\epsilon^6)$ を検査する。
- witnessで $\lambda_{\rm sh}^{-1}\ll\tau_X\ll\tau_p\ll\tau_Y\ll T_{\rm sig}$ の非空時間尺度窓を確認する。
- `tools/check_source.py` でQ3-1/Q3-2のM58/R197依存、A22の旧無条件PMF文、旧M37--M57未統合表現の再混入を回帰検査する。""",
    )

    path = "tools/check_source.py"
    text = load(path)
    old = 'for token in ("R195A", "R196A--R196C", "R161", "R185"):'
    new = 'for token in ("R197", "R195A", "R196A--R196C", "R161", "R185"):'
    if old not in text:
        raise SystemExit("check_source evidence tuple not found")
    text = text.replace(old, new, 1)
    insertion_point = "\ndef check_enhancement_targets() -> None:\n"
    if "def check_q3_common_model()" not in text:
        common_check = r'''

def check_q3_common_model() -> None:
    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    q31 = next((line for line in status.splitlines() if line.startswith("| Q3-1 | 達成 |")), "")
    q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 | 達成 |")), "")
    for token in ("M58", "R86", "R197"):
        if token not in q31:
            raise AssertionError(f"Q3-1 common-model evidence is missing {token}")
    for token in ("M58", "R197", "R196A--R196C", "R161", "R185"):
        if token not in q32:
            raise AssertionError(f"Q3-2 common-model evidence is missing {token}")

    appendix = (ROOT / "sections" / "A23_q3_common_micro_model.md").read_text(encoding="utf-8")
    for token in ("M58", "R197A", "R197B", "R197C", "R197：Q3-1/Q3-2共通ミクロ模型"):
        if token not in appendix:
            raise AssertionError(f"A23 common-model marker missing: {token}")

    chapter6 = (ROOT / "sections" / "06_m37_spatial_envelope.md").read_text(encoding="utf-8")
    for forbidden in (
        "安全な開始面から同じ試行の信号をM57へ渡す",
        "単一反復装置へ統合したとは扱わない",
    ):
        if forbidden in chapter6:
            raise AssertionError(f"old M37--M57 handoff boundary remains: {forbidden}")

    m57 = (ROOT / "sections" / "A22_m57_dual_tl_tracer_microphysics.md").read_text(encoding="utf-8")
    if "同じ状態数sectorのpotential of mean forceは $-k_BT\\log R^\\delta$ を与える" in m57:
        raise AssertionError("A22 still asserts the shell PMF without R197 thermodynamic realization")

    enhancement = (ROOT / "ENHANCEMENT_TARGETS.md").read_text(encoding="utf-8")
    current = enhancement.split("## 強化目標の現在地表", 1)[1].split("## 既存の実装強化課題との関係", 1)[0]
    for qid in ("Q3-1", "Q3-2"):
        line = next((line for line in current.splitlines() if line.startswith(f"| {qid} |")), "")
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[1] != "達成" or cells[2] != "未監査":
            raise AssertionError(f"{qid}: expected A1=達成, A2=未監査")
'''
        if insertion_point not in text:
            raise SystemExit("check_source insertion point not found")
        text = text.replace(insertion_point, common_check + insertion_point, 1)
    call_anchor = "    check_r161_path_boundary()\n"
    if "    check_q3_common_model()\n" not in text:
        if call_anchor not in text:
            raise SystemExit("check_source main call anchor not found")
        text = text.replace(call_anchor, call_anchor + "    check_q3_common_model()\n", 1)
    save(path, text)

    print("draft101 source patch applied")


if __name__ == "__main__":
    main()
