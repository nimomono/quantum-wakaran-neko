#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def replace_section(rel: str, start: str, end: str, body: str) -> None:
    text = read(rel)
    i = text.find(start)
    if i < 0:
        raise RuntimeError(f"missing start {start!r} in {rel}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise RuntimeError(f"missing end {end!r} in {rel}")
    write(rel, text[:i] + body.rstrip() + "\n\n" + text[j:])


# ---------------------------------------------------------------------------
# Scope and core terminology.
# ---------------------------------------------------------------------------
rel = "sections/01_scope_and_cycle.md"
text = read(rel)
text = text.replace(
    "一般深さで作用下限が不足する場合だけ方向を変えない振幅再調整を補助的に使う。",
    "一般深さで作用下限が不足する場合だけR192の方向不変作用安定化を補助的に使う。",
)
write(rel, text)

rel = "sections/02_common_canonical_modules.md"
text = read(rel).replace("旧退役準備結果", "旧R181A")
write(rel, text)

# Rename the active appendix so the filename matches its new responsibility.
old = ROOT / "sections/A13_m54_template_port_preparation.md"
new = ROOT / "sections/A13_m54_radial_stabilizer.md"
if old.exists():
    if new.exists():
        new.unlink()
    shutil.move(str(old), str(new))

for rel in ("MANIFEST.md", "VALIDATION.md"):
    text = read(rel).replace(
        "A13_m54_template_port_preparation.md",
        "A13_m54_radial_stabilizer.md",
    )
    write(rel, text)


# ---------------------------------------------------------------------------
# Q2 chapter: make the active readout path R191 -> R181D; fixed depth uses no R192.
# ---------------------------------------------------------------------------
rel = "sections/04_m54_q2_specializations.md"
text = read(rel)
text = text.replace(
    "5. 排他的なBorn型結果は回路末尾だけでM54静的状態構成のR164/R190/R179/R170へ接続する。無反応も完全結果空間へ含める。",
    "5. 排他的なBorn型結果は回路末尾だけで共通R191へ接続し、R181Dで同じ試行の射影結果成分を受け渡す。無反応も完全結果空間へ含める。",
)
write(rel, text)

sec45 = r"""## 4.5　R191--R181Dの有限深さ段階的射影読出し

回路末尾の実際の1試行信号を

```math
v=Z_{\rm out}(\omega)
```

とする。これは理想係数の再構成値でも集団共分散でもない。第 $k$ 出力ビットに対する直交射影を $P_{k,0},P_{k,1}$ とし、現在の非零信号 $V_k$ から

```math
J_{k,b}
=J_0V_k^\dagger P_{k,b}V_k,
\qquad
S_k=J_{k,0}+J_{k,1}
```

を保持してR191へ渡す。R191が結果 $b_k\in\{0,1,\varnothing\}$ を形成・吸収記録し、安全な2値結果ではR181Dのprojector routerが

```math
V_{k+1}=P_{k,b_k}V_k
```

を同じ試行の次段へ渡す。物理的な $V_{k+1}/\|V_{k+1}\|$ は生成しない。

<!-- theorem-start:corollary -->
**系（R181Dの2入力・3入力計算基底読出し）**

R181Cの末端信号 $v$ が非零で、各段の作用保持、R191、projector router、記録が共通の安全集合と有限時計窓上で定義されるとする。2入力では $m=2$、3入力では $m=3$ とする。理想極限では逐次条件付き確率が望遠鏡積をなし、最終ビット列 $y$ に対して

```math
P(y)
=
\frac{\|P_yv\|^2}{\|v\|^2}
```

を得る。入力・ゲート列の末端状態方向誤差を $\varepsilon_{\rm ray}$、第 $k$ 段のR191とrouterを合わせた完全結果核誤差を $\bar\varepsilon_k$ とすれば、

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm ray}
+\sum_{k=1}^{m}\bar\varepsilon_k.
```

安全な結果成分の測定後状態誤差は付録B.10/P.5の規格化写像上界で別に評価する。固定 $m\in\{2,3\}$ では正の作用下限を有限回だけ追えばよく、R192による段間作用安定化を本系の必須依存にしない。
<!-- theorem-end:corollary -->

R164/R190/R170は一般有限結果集合・作用殻型の代替経路であり、このQ2-1/Q2-3主線へ誤差を重複加算しない。R192は一般深さQ2-4で次段R191の絶対作用下限を一様に保つ場合だけ使う。"""
replace_section(rel, "## 4.5", "## 4.6", sec45)

sec47 = r"""## 4.7　Q2-2の2端R191受信機構への末端接続

Q2-2の固定一重項源は、$|00\rangle$ のR181Bテンソル積状態の生成後にR181Cの固定有限ゲート列を作用させ、設定生成前に4モード信号として準備する。実際の末端信号 $Z$ を集団モーメントへ縮約せず、第5章の2端R191手順へそのまま渡す。

A設定後にA側射影作用をR191へ渡し、A結果でR181D型projector routerを制御して非規格化結果成分をB端へ送る。B設定後にB側射影作用を別のR191へ渡す。旧R180Bのpaired-Hopf再準備、結果別テンプレート吸引、中央潜在結果の2翼複製は現行主線に使わない。

R180AはA端のR191--R181D特殊化、R180CはA/B二端の逐次合成とBell前提監査として第5章で定義する。Q2-2はQ2-1の達成ラベルに依存せず、固定一重項・固定有限設定族・非空間分離という自身の境界で判定する。"""
replace_section(rel, "## 4.7", "## 4.8", sec47)

rel = "sections/04_m54_q2_specializations.md"
text = read(rel)
text = re.sub(
    r"```math\n \\varepsilon_\{\\rm circ\}.*?\\tag\{4\.32\}\n```",
    """```math
 \\varepsilon_{\\rm circ}
 \\leq
 \\varepsilon_{\\rm lift}
 +\\varepsilon_{\\rm hold}
 +\\varepsilon_{\\rm clock}
 +\\sum_{r=1}^{L}\\varepsilon_r
 +\\varepsilon_{\\rm leak}
 +\\varepsilon_{\\rm ray}
 +\\sum_{k=1}^{m}\\bar\\varepsilon_k.
 \\tag{4.32}
```""",
    text,
    count=1,
    flags=re.DOTALL,
)
text = text.replace(
    "R181Dは既存の末端浴部品へ接続する条件付き評価を与える。",
    "R181DはR191で固定した結果に対応する非規格化射影成分を同じ試行の次段へ渡す条件付き評価を与える。",
)
write(rel, text)


# ---------------------------------------------------------------------------
# Q3 bridge: remove stale Q1 action-shell mainline statements.
# ---------------------------------------------------------------------------
rel = "sections/06_m37_spatial_envelope.md"
text = read(rel)
text = text.replace(
    "共通M54/準備済み入力境界で階数1 信号集団を準備する場合、安全な切断面から同じ試行の信号をM54空間状態構成へ渡す。",
    "第2.4節の準備済み入力境界から階数1信号集団を受け取る場合、安全な開始面から同じ試行の信号をM54空間状態構成へ渡す。",
)
text = text.replace(
    "Q1の排他的結果はR164/R190/R179/R170の静的選択系で作る。",
    "Q1の排他的結果はR191で形成し、R181Dで同じ試行の射影結果成分を受け渡す。R164/R190/R170はQ1主線へ使わない。",
)
write(rel, text)


# ---------------------------------------------------------------------------
# Q1 proof appendix: remove stale R164/R190/R170 measurement spine.
# ---------------------------------------------------------------------------
rel = "sections/A2_m47_controlled_w_instrument_proofs.md"
text = read(rel)
text = text.replace(
    "この証明が抑えるのは各時刻の左右周辺占有率である。同じ試行の $X$ が有限記録時間中に安全井戸を離れないという経路事象は周辺分布だけから従わず、R143ではR170の吸収指針変数固定からその失敗率 $\\varepsilon_{\\rm res}$ を別に評価する。",
    "この証明が抑えるのはW型信号系の左右周辺占有率である。現行Q1の排他的結果は粒子位置の滞在事象から作らず、射影作用をR191へ渡して形成するため、この占有率評価からR170型の捕獲失敗率を追加しない。",
)
text = text.replace(
    "固定有限段数 $N$ について、各段の測定面整合、分析器、傾斜保持、辺閉鎖、局所記録、制御付き射影選別機構を共通時計の重ならない窓へ割り当てる。各段の浴接続部、記録素子、選択機構/選別機構用作業領域、流出浴自由度を有限個用意する。分析器中は粒子位置が信号へ追従する必要はなく、次の測定面でR164--R190--R179--R170を新たに走らせる。",
    "固定有限段数 $N$ について、各段のR140分析器、射影作用保持、R191読出し、R181D projector router、必要な局所記録を共通時計の重ならない窓へ割り当てる。各段のR191接続部、記録素子、選別機構用作業領域を有限個用意する。分析器中は粒子位置が信号へ追従する必要はなく、各測定面ではその時点のW2射影作用を新しいR191読出しへ渡す。",
)
text = text.replace(
    "R144は全時刻整合保存または周期間整合帰還を仮定しない。各測定面だけでR164--R190--R179--R170を有限時間作用させる。測定中も対象Rabi項を止めないZeno比較は本証明に含まれない。",
    "R144は全時刻の粒子位置整合または周期間整合帰還を仮定しない。各測定面では射影作用保持、R191、R181Dだけを有限時間作用させる。測定中も対象Rabi項を止めないZeno比較はR189A--R189Cで別に扱う。",
)
# Repair a malformed sentence introduced by the first migration.
text = text.replace(
    "制御付き 選別機構を逆実行して測定前信号を復元することの環境履歴を消して逆転することはここでは行わない。",
    "制御付き選別機構を逆実行して測定前信号を復元することや、結果相関を担う環境履歴を消して逆転することはここでは行わない。",
)
# Replace B.16 resource list and boundary paragraph.
start = text.find("## B.16 資源と適用範囲")
end = text.find("## B.17 M37有限時間制御受渡し系の証明", start)
if start < 0 or end < 0:
    raise RuntimeError("B.16 boundaries missing")
b16 = r"""## B.16 資源と適用範囲

現行Q1の1段測定は少なくとも、W2信号の2正準対、M37実装を使う場合の保持された高モード、R140傾斜制御と時計自由度、2つの射影作用保持指針、R191のmixing/decision浴とBrownian macrospin、吸収記録、R181Dの選別機構用作業領域を必要とする。固定有限段数 $N$ ではこれらを有限個用意でき、R192による段間作用安定化を必要条件にしない。

反復試行で能動補助部を再使用する場合だけR179のopen resetと流出浴を追加する。結果別状態テンプレート、R164作用殻、R190静的混合、R170吸収指針変数は現行Q1主線の資源に数えない。深いW型極限で $J$ が小さくなる場合、零傾斜回転時間 $\mathcal J_0/J$ が増大する事実は資源台帳に残す。

本付録は、R191 transducer、Brownian macrospin、R181D routerをM37の元の局所ばね座標と共通Hamiltonian無限浴から一つの単一ミクロ装置として導出しない。周期全体の微視的熱力学収支、無期限反復、$N\to\infty$ のZeno極限、有限浴化も強化課題である。"""
text = text[:start] + b16 + "\n\n" + text[end:]
write(rel, text)


# ---------------------------------------------------------------------------
# PROJECT_STATUS: align prose/result registry with draft-89 and R192 split.
# ---------------------------------------------------------------------------
rel = "PROJECT_STATUS.md"
text = read(rel)
text = text.replace(
    "R181Aは物理テンプレート準備、R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部ゲート、R191はQ1/Q2の2結果排他的選択・吸収記録、R181Dはその下流の可逆射影選別と測定後状態受渡しを与える。",
    "初期状態方向は第2.4節の準備済み古典入力境界に置く。R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部ゲート、R191はQ1/Q2の2結果排他的選択・吸収記録、R181Dはその下流の可逆射影選別と非規格化測定後状態受渡し、R192は一般深さQ2-4の方向不変作用安定化を与える。",
)
text = text.replace("既存選別機構、必要な再調整を一つの装置へ接続することを条件とする", "既存選別機構を一つの装置へ接続することを条件とする")
text = text.replace("M54準備、M37", "準備済み入力境界、M37")
text = text.replace(
    "R181AのW型2モード化は独立結果IDを持たない系として付録Hに置く。",
    "旧R181AのW型2モード準備対応は現行主線から退役し、notes/Git履歴へ保存する。付録HはR135/R140/R187/R191/R181DのW2対応表だけを置く。",
)
text = text.replace(
    "| R189B | 条件付き・明示誤差付き結果 | 固定済み作用容量からR170後半を走らせ、有限後段窓で零傾斜Rabi継続中の階数1制御付き選別機構を完了する。選択遅延と選別窓重なりを明示評価し、中間傾斜・記録・振幅再調整を使わない |",
    "| R189B | 条件付き・明示誤差付き結果 | R189Aで固定した2作用を走行中信号から切り離してR191へ渡し、有限後段窓で零傾斜Rabi継続中の階数1制御付き選別機構を完了する。選択遅延と選別窓重なりを明示評価し、中間傾斜・記録・R192を使わない |",
)
text = text.replace(
    "| R181D | 条件付き・明示誤差付き結果 | M54段階的射影選別・測定後状態受渡し。共通射影容量固定補題、R170選択・固定、必要な局所記録、可逆選別機構、方向を変えない振幅再調整、転送を合成し、階数1の安全な結果成分では測定後状態を同じ信号へ直接受け渡す |",
    "| R181D | 条件付き・明示誤差付き結果 | R191で固定された2値結果に従う可逆projector routerと非規格化測定後状態受渡し。階数1の安全結果では $Z\\mapsto P_bZ$ を同じ試行の次段へ直接渡し、結果形成や物理規格化を担わない |",
)
text = text.replace(
    "| R177 | 条件付き厳密結果 | R181B--R181Dを使うA--B、B--C二段合成とGHZ--$T$--逆演算証人。",
    "| R177 | 条件付き厳密結果 | R181B/R181CのA--B、B--C二段合成とR191/R181D末端読出しを使うGHZ--$T$--逆演算証人。",
)
# Remove retired R180B active row and rewrite R180A/C.
text = re.sub(r"^\| R180B \|.*\n", "", text, flags=re.MULTILINE)
text = re.sub(
    r"^\| R180A \|.*\n",
    "| R180A | 厳密結果・明示誤差付き結果 | M54の実際の1試行末端信号へA設定basis gateを作用し、A側射影作用をR191へ渡す。A結果でR181D型projector routerを制御し、非規格化結果成分をB端へ渡すQ2-2特殊化 |\n",
    text,
    flags=re.MULTILINE,
)
text = re.sub(
    r"^\| R180C \|.*\n",
    "| R180C | 条件付き・明示誤差付き結果 | A端R191、R181D型projector router、B設定gate、B端R191、二つの記録とR179 resetを合成し、固定一重項でBorn共同分布、非信号性、CHSH値、Bell前提監査を与える。非空間分離であり旧paired-Hopf再準備は使わない |\n",
    text,
    flags=re.MULTILINE,
)
text = text.replace(
    "- R164の作用殻結果別状態数はM54各状態構成が共有するBorn型条件付き重みの統計力学的起源である。容量結合と作用殻準備をミクロ導出済みとは扱わない。",
    "- R164の作用殻結果別状態数はQ3開始配置と一般有限結果集合・作用殻型代替経路に残す。現行Q1/Q2の2結果Born重みはR191が射影作用比から生成し、R164を必須依存にしない。容量結合と作用殻準備をミクロ導出済みとは扱わない。",
)
write(rel, text)


# ---------------------------------------------------------------------------
# Error/resource chapter: prepared-input boundary + R192; remove old shell spine.
# ---------------------------------------------------------------------------
rel = "sections/08_errors_resources_open_targets.md"
text = read(rel)
text = text.replace(
    "6. M54の同じ横方向偏差を退役退役準備結果の状態方向誤差、R135の初期共分散誤差、系列固有準備誤差へ重ねて入れる。",
    "6. 同じ準備済み入力偏差を $\\varepsilon_{\\rm in}$、R135の初期共分散誤差、系列固有の入力誤差へ重ねて入れる。",
)
write(rel, text)

sec82 = r"""## 8.2 準備済み入力境界とR192の誤差・資源

Q1とQ3の状態方向、Q2-1--Q2-3の固定入力は、第2.4節の準備済み古典入力境界から受け取る。入力状態と目標状態の差は一つの $\varepsilon_{\rm in}$ として最初の下流誤差へ一度だけ加え、同じ偏差をR135、R168、系列固有誤差へ重複計上しない。一般の指定状態方向を共通seedから生成する旧R181Aの時間、ポンプ、排熱を現行固定目標の資源には数えない。具体的な入力準備装置を追加する場合、その費用は境界の上流実装として別途報告する。

R192は一般深さQ2-4だけで、R181Dが選別した非終端安全結果の絶対作用を次段R191の読出し下限へ戻す。理想流は

```math
\dot Z
=g_R(S_*-Z^\dagger Z)Z
```

で、状態方向を厳密に保存する。安全下限 $S_0\geq S_{\min}>0$ に対し、相対作用誤差を $\eta_R$ 以下にする固定接続時間は

```math
T_{192}
\geq
\frac{1}{2g_RS_*}
\log\!\left[
\frac{S_*/S_{\min}-1}{\eta_R}
\right].
```

R191 dispatcherとR181Dから $S_{\min}/S_*=\operatorname{poly}^{-1}(n,1/\epsilon)$ を選び、$g_RS_*$ も逆多項式以上に保てば、各非終端段と全 $n-1$ 段のR192時間は多項式である。接続時間はこの事前下限から固定し、未知の条件付き確率や現在の振幅を読み取って適応変更しない。

有限実装の作用回復誤差を $\varepsilon_{192,k}$ とする場合、Q2-4では $\sum_{k=1}^{n-1}\varepsilon_{192,k}$ を一度だけ数える。R192は既存の横方向偏差を訂正しないので、静的結合誤差、位相雑音、全自由度への加法雑音はR186で監査する。$S_0=0$ または安全下限未満の希少結果をR192後に成功結果へ戻してはならない。"""
replace_section(rel, "## 8.2", "## 8.4", sec82)

rel = "sections/08_errors_resources_open_targets.md"
text = read(rel)
text = text.replace("\\varepsilon_{\\rm prep}", "\\varepsilon_{\\rm in}")
text = text.replace("中間振幅再調整を使わない", "中間R192を使わない")
text = text.replace("$d_0$ は退役退役準備結果の供給源または固定正準接続端から", "$d_0$ は準備済み入力境界または固定正準接続端から")
text = text.replace(
    "R187のW2への正準接続端は全モード直交変換の先頭2正準対を使い、高モードを捨てない。退役退役準備結果のポンプ／供給源、R191読出し、R181D router、R143局所記録の物理資源はこの台帳へ吸収せず、Q1測定部分系の別項として残す。",
    "R187のW2への正準接続端は全モード直交変換の先頭2正準対を使い、高モードを捨てない。具体的な準備済み入力装置の資源は境界の上流へ分離し、R191読出し、R181D router、R143局所記録の物理資源はQ1測定部分系として別に数える。",
)
# Q2-3 residuals should reflect R191/R181D rather than old shell endpoint.
text = text.replace(
    "R181Dが末端Born型測定機構への条件付き接続を与えるため、Q2-3は条件付き達成である。残る条件は容量指針変数--作用殻境界、有限ファイバー混合の結果成分間の対称性、SWAPから記録までの単一時計自由度統合である。",
    "R191とR181Dが末端2結果読出しと結果成分受渡しを与えるため、Q2-3は条件付き達成である。残る条件はR191 transducer、router、記録を永続8モード記憶部と同じ有限時計割当で統合することである。",
)
# Replace stale Q2-4 causal paragraph.
text = text.replace(
    "Q2-4ではM54の $L=2^n$ 受動信号モードを使い、R181Cが局所ゲートを一括作用させ、R181Dが出力ビットごとの未処理容量を保持する。各節点の静的選択は、容量保持機構 $\\to$ R164作用殻 $\\to$ R190のDrude混合・作用開口 $\\to$ R179の再混合 $\\to$ R170の吸収指針変数 $\\to$ 可逆選別機構 $\\to$ R192方向不変作用安定化、の順に行う。",
    "Q2-4ではM54の $L=2^n$ 受動信号モードを使い、R179後の定数次元供給源から $0^n$ 根モードを作り、R181Cが局所ゲートを一括作用させる。各出力ビットでは射影作用をR191へ渡して結果を形成し、R181Dが非規格化射影成分を次段へ渡す。非終端の安全結果だけに事前固定時間のR192を作用させ、次段R191の絶対作用下限を回復する。最終ビット後に別の作用感度を持つ読出しが無ければ終端R192は置かない。",
)
text = text.replace(
    "| M54/R180A--R180C | 実際の末端信号でなく集団モーメントを再注入する、ブロック作用と結果重みが一致しない、2端Hopf流が選択テンプレートへ吸引しない、R180Cの単一装置境界を満たさない、切断後因子化が破れる、局所R170応答が反対翼設定を参照する、無反応込みでCHSH誤差上界を満たさない |",
    "| M54/R180A--R180C | 実際の末端信号でなく集団モーメントを再注入する、A端R191の結果とrouterが一致しない、B端へ非規格化結果成分を同じ試行のまま渡せない、B端読出しがA/B以外の設定を参照する、R180Cの単一装置境界を満たさない、または無反応込みでCHSH誤差上界を満たさない |",
)
text = text.replace(
    "| M54/R181B--R181D・R179・R186 | 指針変数固定前に選別機構を開く、希少結果を事後除外する、状態依存除算を使う、開放浴へ回路出力確率やモード別係数を外部注入する、一様装置族へ統合できない、またはR186の全自由度に加わる加法ノイズ障害を回避できず指数精度を要求する |",
    "| M54/R181C・R181D・R179・R186・R191・R192 | R191結果固定前にrouterを開く、希少結果を事後除外する、R192で安全下限未満を救済する、状態依存除算を使う、開放浴へ回路出力確率やモード別係数を外部注入する、一様装置族へ統合できない、またはR186の加法ノイズ障害を回避できず指数精度を要求する |",
)
text = text.replace(
    "固定目標上の未完成事項は、Q3-6の位相量子化、Q2-1/Q2-3の末端開放浴接続、Q2-4の一様装置族統合である。Q2-4では静的部分系配線、射影容量保持機構、R190/R179静的選択機構、R170吸収指針変数、選別機構、R192方向不変作用安定化、開放リセット/供給接続部を一つの装置族へ接続し、R186のノイズ条件を満たす必要がある。",
    "固定目標上の未完成事項は、Q3-6の位相量子化、Q2-1/Q2-3の末端R191--R181D接続、Q2-4の一様装置族統合である。Q2-4では静的部分系配線、R191 transducerとBrownian macrospin、R181D router、R192方向不変作用安定化、R179開放リセット/供給接続部を一つの装置族へ接続し、R186のノイズ条件を満たす必要がある。",
)
# Historical R170 line remains valid only as alternative result; don't present it as Q1/Q2 mainline.
text = text.replace("退役退役準備結果", "旧R181A")
write(rel, text)


# ---------------------------------------------------------------------------
# Retired index: ensure R180B is explicitly historical.
# ---------------------------------------------------------------------------
rel = "notes/superseded_result_index.md"
text = read(rel)
if "| R180B |" not in text:
    marker = "| R181A |"
    row = "| R180B | Q2-2のpaired-Hopf二端再準備 | draft-89でA端R191→R181D型router→B端R191へ置換し、現行必須主線から退役 | `superseded_q2_2_paired_hopf_receiver.md`、第5章R180A/R180C |\n"
    idx = text.find(marker)
    if idx >= 0:
        text = text[:idx] + row + text[idx:]
write(rel, text)


# ---------------------------------------------------------------------------
# Validation prose and source checks.
# ---------------------------------------------------------------------------
rel = "VALIDATION.md"
text = read(rel).replace("退役退役準備結果", "旧R181A")
write(rel, text)

# No accidental machine-replacement wording may remain active.
for path in (ROOT / "sections").glob("*.md"):
    txt = path.read_text(encoding="utf-8")
    if "退役準備結果" in txt or "退役退役" in txt:
        raise RuntimeError(f"awkward retirement replacement remains in {path.name}")

print("r192_cleanup_complete")
