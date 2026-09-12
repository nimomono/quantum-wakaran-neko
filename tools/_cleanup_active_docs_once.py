#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, replacement: str, label: str) -> str:
    matches = list(re.finditer(pattern, text, flags=re.S))
    if len(matches) != 1:
        raise SystemExit(f"{label}: expected 1 match, found {len(matches)}")
    return re.sub(pattern, replacement, text, count=1, flags=re.S)


README = r'''# quantum-wakaran-neko

量子、なんもわからん。

## このプロジェクトは何を調べているか

古典的な粒子、振動子、熱浴、測定器を組み合わせたとき、量子力学に特徴的な構造がどこまで有効理論として現れるかを調べるプロジェクトです。

単にSchrödinger方程式と同じ形の方程式を古典振動子で作るだけでは、1回の実験で結果が一つに決まることや、Born則、測定後状態までは説明できません。そこで本プロジェクトでは、次の三つを同じ古典的な枠組みの中で調べています。

- 古典振動子から、量子状態に似た状態空間と可逆操作を作れるか。
- 1回ごとの排他的な測定結果と、振幅の二乗に比例する統計を古典過程から作れるか。
- その仕組みを、複合系、Bell型統計、量子回路型の処理、空間を動く粒子へ拡張できるか。

## この研究で「状態」は何を表すか

物理的な実体として扱うのは、実数の位置・運動量、粒子位置、熱浴、制御器、記録器です。論文中の複素信号 $Z$ は、実正準座標 $(Q,P)$ をまとめて書くための派生表示であり、独立した複素実体ではありません。

また、状態方向、第2モーメント、位置分布などは、多数回の試行をまとめた統計量として扱います。これらの統計量を、1回の試行の制御器が読み取って次の状態を書き込むことはしません。

論文では、こうした信号、配置、記録、時計自由度などをまとめた共通の有効状態構成をM54と呼びます。空間を伝わる信号については、局所的に結合した実振動子網M37からの物理的な実装も調べています。

## 現在の中心的な仕組み

### 1. 単一量子ビット型の操作と測定

弱く結合したW型振動子系の低い2モードを使うと、Bloch球に相当する2状態の有効空間と、任意の $SU(2)$ 操作、Rabi振動を作れます。M37の実振動子運動からこの2モード信号へ接続するのがR187、2モード上の操作がR140です。

測定では、測定軸に対応する二つの射影作用

```math
J_+=\mathcal J_0 Z^\dagger P_+Z,
\qquad
J_-=\mathcal J_0 Z^\dagger P_-Z
```

を作り、R191へ渡します。R191は古典的なブラウン巨視的スピンを使って、1回の試行ごとに $+,-$ のどちらか、または無反応を生成します。理想極限では

```math
P(\pm)=\frac{J_\pm}{J_++J_-}
```

となります。

結果が決まった後は、R181Dが可逆な射影成分の振り分けを行い、選ばれた非規格化成分 $P_rZ$ を同じ試行の次の操作へ渡します。

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{R191}}
r
\xrightarrow{\mathrm{R181D}}
P_rZ.
```

固定有限回の逐次測定では、各段で信号を物理的に規格化し直す必要はありません。一般に深いQ2-4の回路で作用が小さくなりすぎる場合だけ、状態方向を変えず作用の大きさだけを戻すR192を補助的に使います。

この経路で、Born型2結果分布、同じ軸の反復測定、異なる軸の逐次測定、有限回のRabi--Zeno比較まで構成しています。

### 2. 複合系とBell型統計

複合系では、R181Bが複数の入力からテンソル積型の多モード信号を作り、R181Cが同じ記憶部上で局所操作やCNOT型の結合操作を実行します。中間で状態を測定して作り直さず、同じ物理信号を次の操作へ渡します。

Bell型統計では、固定一重項型の4モード信号にA側の設定を作用し、A端のR191で結果を作ります。その結果に対応する非規格化射影成分をB端へ物理的に渡し、B側の設定と2つ目のR191を作用します。これにより一重項と同じ余弦共同統計、非信号性、CHSH/Tsirelson値を再現します。

ただし、A側の結果成分をB側へ物理的に渡す装置なので、空間分離されたBell局所模型ではありません。

一般回路については、$2^n$ 個の受動信号モードを許しつつ、外部から必要なプログラム、制御、時間、精度、読出しを多項式に抑えられるかをQ2-4で調べています。これは通常の意味で効率的な古典計算機シミュレーションや、量子計算機と同等の総物理資源を主張するものではありません。

### 3. 空間を動く粒子

空間側では、局所振動子網M37からSchrödinger型の包絡発展を導きます。さらに、開始時刻の粒子位置をR164で準備し、R161が信号の確率流と活動量から遷移率を作り、R162が開放Poisson跳躍過程として同じ粒子を時間発展させます。

```math
Z_{t_0}
\xrightarrow{\mathrm{R164}}
X_{t_0}
\xrightarrow{\mathrm{R161/R162}}
X_T.
```

R185では同じ前向き経路法則のBayes反転から前進・後退平均微分を構成し、有限格子・有限時間の範囲で時間対称Newton則へ接続します。

この位置過程は、Q1/Q2で測定結果を作るR191とは別の因果鎖です。

## 現在どこまでできているか

Q1では、2モード可逆操作、Born型2結果測定、同軸反復、異軸逐次測定、有限Rabi--Zeno証人まで構成しています。

Q2では、2量子ビット型結合操作、3部分系の二段ゲート合成、非空間分離Bell型統計、一般回路の出力標本化を条件付きで構成しています。主な残件は、読出し、射影成分の振り分け、作用安定化、リセットなどを一つの具体的な装置へ統合することと、一般回路での物理配線・較正・ノイズ条件を閉じることです。

Q3では、Schrödinger型有効力学、Nelson型の時間対称Newton則、井戸型・調和型・W型の束縛状態、トンネル効果、2経路干渉まで進んでいます。位相量子化は未達です。

正式な達成判定、根拠結果、残っている条件は [PROJECT_STATUS.md](PROJECT_STATUS.md) を正本とします。

## この研究が主張しないこと

- 量子力学全体を古典力学から導出したとは主張しません。
- 空間分離されたBell局所模型を構成したとは主張しません。
- 指数的な内部自由度を除去した、または通常の意味で効率的な古典計算を得たとは主張しません。
- Q1、Q2、Q3の全部品を一台の完成した物理装置へ統合したとは主張しません。

再現できた構造と、追加仮定が必要な構造、まだ未完成な構造を分けて記述することを重視しています。

## 読む順番

- [論文PDF](paper.pdf)
- [証明状態と理論の境界](PROJECT_STATUS.md)
- [プロジェクトの長期的方針](PROJECT_STANCE.md)
- [論文リポジトリの構成・執筆・更新規約](PROJECT_GUIDE.md)
- [論文用語と標準表記](TERMINOLOGY.md)
- [検算と品質確認](VALIDATION.md)
- [現行版のファイル一覧](MANIFEST.md)
- [論文外の研究メモ](notes/README.md)

論文本文の編集対象は `sections/` 以下です。`paper.md`、`main.tex`、`paper.pdf` は生成物として同期します。
'''


def patch_readme() -> None:
    path = ROOT / "README.md"
    path.write_text(README, encoding="utf-8")


def patch_project_status() -> None:
    path = ROOT / "PROJECT_STATUS.md"
    text = path.read_text(encoding="utf-8")

    current_models = r'''## 現行模型・物理実装層・手順の運用状態

### 共通有効模型族と物理実装層

| 識別 | 分類 | 運用状態 | 役割と限界 |
|---|---|---|---|
| M54 | 共通有効信号--配置状態構成族 | 現行Q1・Q2・Q3の共通有効層 | 準備済み古典入力境界、有限実正準信号、永続記憶部、作業領域、記録、時計自由度の共通型を与える。Q1/Q2ではR191の2結果読出しとR181Dの射影成分受渡し、Q2-4では必要な非終端段だけR192、Q3ではR164開始配置とR161/R162輸送へ接続する。R179は反復時の開放リセットと履歴排出を担う。全状態構成の単一装置統合を意味しない |
| M37 | 物理Hamiltonian実装層 | Q3の空間信号部分系、およびR187条件下のQ1 W2制御用信号系 | 局所位置結合された有限実古典振動子網からR86の空間包絡を導く。R187の弱結合W型族では最低2正常モードをM54のW2信号へ正準同定し、R140制御を任意精度で実装する。R191読出し、R181Dの振り分け、記録、リセットまでM37から導出したとはしない |

M50はM54の静的状態構成へ、M55はM54空間状態構成へ吸収した。旧R181Aの状態方向準備、旧R190/R170によるQ1/Q2二結果主線、旧R180Bの2端再準備は現行必須依存から外し、退役索引と研究メモへ保存する。

M54による統一は共通状態型、因果契約、接続規約の有効層の統一である。M37による実装は、そのうち空間信号部分系とQ1 W2制御信号の一部を局所Hamiltonian信号系から導く物理層の主張である。両者を同じ意味の「モデル統一」として数えない。

### 系列固有手順 / 受信機構

| 識別 | 使用する共通層 | 現行責務 |
|---|---|---|
| Q1 W型2モード手順（旧M47） | M54のW2静的状態構成＋R187のM37接続 | 準備済みW2入力、R187/R140による制御、射影作用保持、R191による2結果形成、R181Dによる非規格化射影成分受渡し、R143/R144、R189A--R189Cを接続する。R164/R190/R170の作用殻経路は現行Q1必須主線に使わない |
| R180 2端R191受信機構 | M54静的状態構成 | 固定一重項4モード信号にA設定を作用し、A端R191、R181D型の射影成分振り分け、B設定、B端R191を順に接続する非空間分離Q2-2手順。旧R180Bの2端再準備は使わない |

### 統合目標

| 識別 | 分類 | 運用状態 | 役割と限界 |
|---|---|---|---|
| M0 | 単一ミクロ装置統一目標 | 将来目標 | M54の状態構成、M37信号系、R191読出し、R181Dの射影成分振り分け、R192作用安定化、記録、R179開放リセットを、有限な能動部分系と明示的なHamiltonian無限浴からなる単一ミクロ装置と共通反復周期へ統合する。有限浴または有限閉鎖Hamiltonian全系への持上げは達成条件としない |

M54は共通の状態型と因果契約を与えるが、同じ物理接続部、永続記憶部、制御バス、読出し、記録、リセットを全状態構成・全規模で共有する単一ミクロ装置を意味しない。この強い統合はM0の未完成目標である。
'''
    text = sub_once(
        text,
        r"## 現行模型・物理実装層・手順の運用状態\n.*?(?=\n## 現行結果の導出状態)",
        current_models,
        "current model block",
    )

    text = replace_once(
        text,
        "R170は一般有限結果集合・作用殻型の代替経路へ残す。R180AはR181Dではなく共通射影作用保持補題とR191を使う兄弟特殊化である。",
        "R170は一般有限結果集合・作用殻型の代替経路へ残す。R180AはA端R191とR181D型の射影成分振り分けを組み合わせるQ2-2特殊化である。",
        "current-position R180A role",
    )

    text = text.replace(
        "有限衝突による移動分布の整合",
        "R161/R162による移動分布の整合",
    )

    text = sub_once(
        text,
        r"^- R190A--R190Cは、.*$",
        "- R190A--R190Cは、固定済み正作用容量を2作用LC殻へ渡して混合し、対称作用開口から静的平方根核へ接続する作用殻型の代替経路として保持する。現行Q1/Q2の2結果主線には使わず、Q3のR162開放Poisson跳躍過程も置き換えない。有限浴への持上げは独立の強化課題である。",
        "R190 interpretation",
    )
    text = sub_once(
        text,
        r"^- M54が準備する \\(C_Z.*$",
        "- M54が準備する $C_Z\\simeq cc^\\dagger$ は試行集団の統計状態である。各試行の実体は実正準信号、開放接続部、制御器、記録器と履歴であり、$c$ または $C_Z$ を単一試行制御器へ再注入しない。",
        "M54 ontology",
    )
    text = sub_once(
        text,
        r"^- Q3の単一試行では.*$",
        "- Q3の単一試行ではM54空間状態構成の実正準信号自由度、1個の粒子位置、R162の開放Poisson跳躍過程が物理過程を担う。複素信号は実正準状態の派生表示、状態方向と位置分布は集団統計であり、制御器へ集団統計を入力しない。M37は空間信号部分系の局所位置ばね物理実装層である。",
        "Q3 ontology",
    )
    text = replace_once(
        text,
        "$\\delta\\downarrow0$ では率感度と有限衝突資源が発散し得る。",
        "$\\delta\\downarrow0$ では率感度と率実装資源が発散し得る。",
        "delta resource wording",
    )
    text = sub_once(
        text,
        r"^- R170はQ1、Q2-1、Q2-3、Q2-4、R180A、R180Cで共通に使う.*$",
        "- R170は一般有限結果集合・作用殻型の代替経路とQ3固定時刻の代替診断に残す。現行Q1/Q2の2結果主線ではR191を用い、R170の選択・固定誤差を重複加算しない。",
        "R170 interpretation",
    )
    text = sub_once(
        text,
        r"^- R181Dでは未処理容量.*$",
        "- R181DはR191で固定された安全結果 $r$ に従い、可逆な射影成分の振り分けによって $P_rZ$ と補成分を分け、非規格化 $P_rZ$ を同じ試行の次段へ渡す。固定有限深さでは物理的な再規格化を行わない。一般深さQ2-4の非終端安全結果で次段R191の作用下限が必要な場合だけR192を使う。R170の作用殻型選択はこの主線の必須依存ではない。",
        "R181D interpretation",
    )

    unresolved = r'''## 未解決問題

未解決問題では、有限閉鎖Hamiltonian化そのものを共通到達点としない。M0本体では有限な能動部分系、共通接続部、明示的なHamiltonian無限浴、準備・測定・記録・リセットの因果接続を一つのミクロ装置と反復周期へ統合することを扱う。有限浴近似、有限再帰、有限総容量、全周期の微視的熱力学は、有限性自体に意味がある場合を除き別の強化課題とする。

1. R191の作用和・作用差変換器、ブラウン巨視的スピン、有限温度の決定過程、吸収記録、R181Dの射影成分振り分けを、Q1/Q2で共有できる一つの具体的な能動装置へ統合し、帯域、温度、較正誤差を実装模型から評価する。
2. R187のM37 W2信号系、射影作用保持、R191読出し、R181Dの射影成分振り分け、外部記録、必要なR179開放リセットを同じ具体装置と時計自由度で接続し、Q1測定部分系の単一装置統合と周期収支を閉じる。
3. Q2-2について、固定一重項4モード信号、A/B設定操作、二つのR191読出し端、R181D型の射影成分振り分け、記録、R179開放リセットを同じ非空間分離装置と時計割当へ統合する。
4. Q2-4について、M54の静的部分系配線、R191逐次読出し、R181D、非終端安全結果のR192、R179開放リセットを一つの一様装置族へ統合する。さらに製造ばらつきと運転中の揺らぎを実装模型から導き、R186の多項式精度条件を満たし、全自由度への加法的な揺らぎが生む指数障害を回避できる範囲を示す。
5. Q3の強化として、M37空間信号、R164開始配置、R161/R162輸送、時計自由度、終位置記録を同じ有限能動部分系＋Hamiltonian無限浴の装置へ統合する。あわせて、生M37局所包絡から時間対称Newton則へより直接に進む縮約、連続空間の一様極限、多粒子拡張を検討する。
6. Q3-6の位相量子化について、閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を同じ明示的な古典ミクロ構成で閉じる。

'''
    text = sub_once(
        text,
        r"## 未解決問題\n.*?(?=\n## 置換・退役結果)",
        unresolved.rstrip(),
        "unresolved block",
    )

    path.write_text(text, encoding="utf-8")


def patch_a3() -> None:
    path = ROOT / "sections" / "A3_m54_q2_specialization_proofs.md"
    text = path.read_text(encoding="utf-8")
    marker = "## C.8　容量固定機構"
    if text.count(marker) != 1:
        raise SystemExit(f"A3 C.8 marker count={text.count(marker)}")
    prefix = text.split(marker, 1)[0].rstrip()
    suffix = r'''

## C.8　現行末端読出しとの責務境界

本付録の正本はR181Bの有限次元テンソル積状態生成、R181Cの同一記憶部上の有限ゲート列、および逆演算診断までとする。

末端の2結果形成はR191、結果固定後の可逆な射影成分の振り分けと非規格化結果成分の次段受渡しはR181Dが担う。R181Dの一般定理と証明は第2章および付録Pを正本とし、本付録では再証明しない。Q2-1/Q2-3への有限次元特殊化は第4章を参照する。

したがって、旧C.8--C.10に置いていた作用容量固定、R170選択・固定、方向を変えない振幅再調整をR181Dの証明へ組み込む経路は現行主線に用いない。
'''
    path.write_text(prefix + suffix, encoding="utf-8")


def patch_r144() -> None:
    path = ROOT / "sections" / "03_m47_controlled_w_instrument.md"
    text = path.read_text(encoding="utf-8")
    old = "本定理はZeno効果そのものを示さず、測定中も零傾斜Rabi項を止めない対照との接続は別の未達課題である。"
    new = "本定理自体はZeno効果そのものを示さない。測定中も零傾斜Rabi項を止めない有限2回Zeno比較はR189A--R189Cで別に構成する。"
    text = replace_once(text, old, new, "R144 Zeno wording")
    path.write_text(text, encoding="utf-8")


def final_guards() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for forbidden in ("## 長期目標の現在地", "### 現行の模型・実装階層", "paired-Hopf", "2端Hopf受信機構"):
        if forbidden in readme:
            raise SystemExit(f"README stale token remains: {forbidden}")

    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    for forbidden in (
        "R181A--R181Cは準備・持ち上げ・gate",
        "R180設定先行2端Hopf受信機構",
        "R170はQ1、Q2-1、Q2-3、Q2-4、R180A、R180Cで共通に使う",
        "Q3-2固定範囲の有限衝突合成加速度はR162/R188で閉じた",
        "R181Aの供給源／ポンプ",
    ):
        if forbidden in status:
            raise SystemExit(f"PROJECT_STATUS stale token remains: {forbidden}")

    a3 = (ROOT / "sections" / "A3_m54_q2_specialization_proofs.md").read_text(encoding="utf-8")
    if "**証明（R181D）**" in a3 or "## C.9　末端誤差" in a3 or "## C.10　残る接続義務" in a3:
        raise SystemExit("old R181D proof remains in A3")

    q1 = (ROOT / "sections" / "03_m47_controlled_w_instrument.md").read_text(encoding="utf-8")
    if "対照との接続は別の未達課題" in q1:
        raise SystemExit("stale R144 Zeno wording remains")


if __name__ == "__main__":
    patch_readme()
    patch_project_status()
    patch_a3()
    patch_r144()
    final_guards()
    print("active_document_cleanup_ok")
