@number: 1
@chapter: 本文
@title: 問題設定、統一構造、達成範囲
@status: M54を共通実正準signal・状態構成層、M37をsignal物理実装層、M66/R205を共通thermal-reservoir interfaceとする。M64、M65、R206、R207は用途別の模型・特殊化として責務を分け、M0のjoint device/process統合とは区別する。

## 1.1 研究上の問い

本稿は、古典的な粒子、実振動子、熱浴、制御器、記録器から、量子力学に特徴的な状態空間、可逆力学、Born型排他的結果、測定後状態、複合系相関、空間力学がどこまで有効構造として現れるかを調べる。有限次元Schrödinger方程式を古典正準座標へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、記録、resetは得られないため、signal dynamicsとresult formationを分けて構成する。

各試行の物理状態、そこから作る派生座標、試行集団の統計量、外部制御、観測記録を区別する。複素信号 $Z$、密度、current、状態方向、規格化第2モーメントを単一試行の独立実体として仮定せず、必要な物理interfaceなしに統計量を各試行へ再注入しない。

## 1.2 現行の統一構造

現行理論は、共通signal層、共通thermal-reservoir層、用途別specialization、全周期統合目標の4層に分ける。

| 層 | 識別 | 責務 |
|---|---|---|
| 共通有効signal・状態構成 | M54 | 有限実正準信号、準備済み入力境界、永続記憶部、作業領域、時計、記録、接続規約 |
| signal物理実装 | M37/R86 | 局所結合古典振動子網から空間signalを実装。R187条件下ではW型最低2正常モードをQ1へ接続 |
| 共通thermal-reservoir interface | M66/R205A--R205F | phase-volume、mean-flow、thermal sampling、matched capacity--conductance、passive separation |
| 用途別模型・特殊化 | M64、M65、R206、R207 | Q3 tracer/Nelson、Q1逐次2値測定、Q2終端多結果読出し、Q2-2 projection phase-volume二端模型 |
| 全周期統合目標 | M0 | 準備、操作、測定、永久記録、reset、clock、renewalを1つのjoint device/processへ統合 |

M54とM66は異なる責務を持つ共通層である。M54はどのsignal・状態・接続端を使うかを整理し、M66はresolved classical degreeとthermal reservoirの間の物理原理を整理する。M66がM54を置換するわけでも、M54からM66が従うわけでもない。

M66の共通入力は正のphase-volume weight $w(Q,t)$、通常のenergy landscape $H_{\rm cfg}(Q,t)$、mean-flow port $U(Q,t)$ である。R205A/R205Cは

```math
F_{\rm res}(w)
=
-k_BT\log w+C
```

とmean-flow shiftの両立を与え、R205Eは

```math
p_{\rm eq}(Q)
\propto
w(Q)e^{-\beta H_{\rm cfg}(Q)}
```

のthermal samplingを与える。R205Fは距離依存相互作用とreservoir cross-correlationが消えるときのgenerator分離条件を与える。

ただし、この共通化はwhole-model derivationではない。M64ではR203Bのpartition/free-energyとmean-flow sectorだけがR205Cへ埋め込まれ、current dictionary、initial preparationの具体則、tracer、R203C/R203DはM64固有である。M65ではR204Bのphase-volume chamber実現だけがR205Dへ埋め込まれ、canonical 3状態open Markov lawはM65自身の定義である。R206はM66のQ2終端多結果特殊化であり、R207はR205A/R205E/R205FをQ2-2 projection phase-volume主線へ適用する。

## 1.3 系列ごとの現行因果鎖

Q1の逐次2結果測定では、射影作用を

```math
J_\pm
=
\mathcal J_0Z^\dagger P_\pm Z
```

として保持し、M65へ渡す。

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{M65/R204D}}
r
\xrightarrow{\mathrm{R181D}}
P_rZ.
```

M65が完全結果形成、正式な無反応、有限recordまでを担い、R181Dは結果を生成せずprojector routerと測定後結果成分受渡しだけを担う。固定有限深さでは非規格化結果成分をそのまま次段M65へ渡す。

Q1 W型2モード特殊化では

```math
\mathrm{M37\ W2}
\xrightarrow{\mathrm{R187/R189A}}
(A_L,A_R)
\xrightarrow{\mathrm{M65/R204D}}
Y
\xrightarrow{\mathrm{R181D}}
P_rZ
```

が現行測定主線である。

Q2-1/Q2-3/Q2-4はterminal readout後に結果成分を次のgateへ渡さないため、M65/R181D treeを使わない。

```math
Z_{\rm out}
\longrightarrow
\{J_y=\mathcal J_0|Z_y|^2\}
\xrightarrow{\mathrm{R206}}
Y.
```

Q2-1は $L=4$、Q2-3は $L=8$、Q2-4は $L=2^n$ とする。Q2-4ではR206Eの一様root preparation、R181C gate列、R206D terminal samplingを使う。

Q2-2 fixed-goalはM66/R205A・R205Eによるprojection phase-volume共同準備、near-contact hidden-direction lock、R205F passive separation、R207 local sign latch/recordを一試行で接続する。一般Bloch方向のsinglet共同統計を任意精度で再現し、分離後local response factorizationとmeasurement independenceの不成立を監査する。

Q3のsignal数学はQ1/Q2の局所実正準信号と2体系結合の空間特殊化である。M37/R86 signalへM64のclassical tracerとsignal-driven thermal reservoirを接続し、

```math
\mathrm{M37/R86}
\longrightarrow
\mathrm{M64/R203A--R203C}
\longrightarrow
\mathrm{R203D/R161}
\longrightarrow
\mathrm{R185}
```

と進む。R162はR161 canonical Markov lawのoptional Poisson realizationであり、Q3の基礎的存在論やQ3-2の直接依存には入れない。

## 1.4 系列ごとの最小構成

| 系列 | signal準備・操作 | 結果形成・受渡し |
|---|---|---|
| Q1 | 準備済みW2入力、M37/R187、R135、R140、R189A | M65/R204D--R204F、R181D、R143--R144、R189B--R189C |
| Q2-1 | R181B、R181C | M66/R206Dの4結果terminal sampler |
| Q2-2 | M66/R205 projection phase-volume共同準備、near-contact lock | R207 passive separation、local sign latch、R112型record、R207A--R207D監査 |
| Q2-3 | R181Bを2回、R181C、R177 | M66/R206Dの8結果terminal sampler |
| Q2-4 | R206E root preparation、M54一般 $2^n$ 直接モード、R181C | M66/R206Dの $2^n$ 結果terminal sampler、R186資源監査 |
| Q3 | M37/R86 signal、M64/R203A--R203D | R161/R185、R124/R182/R125位置読出し、R112終位置record |

## 1.5 達成範囲と判定階層

固定目標と達成ラベルは PROJECT_STATUS.md を正本とする。Q1-1、Q1-2、Q2-1、Q2-2、Q2-3、Q3-1--Q3-5は達成、Q2-4は条件付き達成、Q3-6は未達とする。

個別固定目標は、その目標が要求する現象を1試行内で明示的な物理interfaceを介して合成できることを共通最低条件とする。永久記録、試行間reset、物理clock、次試行renewalまでの全周期統合は、目標自身が要求しない限りM0へ分離する。Q2-4は資源効率・反復回数・総時間を目標自身が要求するため例外である。

固定目標に付随するA1/A2/B1--B3は ENHANCEMENT_TARGETS.md を正本とし、fixed-goal達成状態とは独立に管理する。A1は主要因果鎖を1つの具体的古典物理模型として閉じること、A2はそのミクロ方程式自体を直接計算することを要求する。

M0はさらに強く、複数系列にまたがる主要自由度、物理接続端、準備、操作、測定、永久記録、reset、clock、renewalを1つのjoint microscopic device/processと共通反復周期へ統合することを要求する。M0の強さはHamiltonian性ではなく統合範囲にある。

## 1.6 非主張

本稿は、量子力学全体を古典力学へ還元したこと、自由設定を保った空間分離Bell局所模型を得たこと、指数的な受動内部自由度を除去したこと、全系列を同一製造済み装置へ統合したことを主張しない。

M66はM64/M65/R206/R207に現れるreservoir原理を共通化するが、M64のQ3 tracer/Nelson model、M65のcanonical binary instrument、R207のQ2-2 specializationまでを1つの模型から導出したことを意味しない。また、共通thermal-reservoir interfaceを得たことは、全系列が同じ単一bathまたは同じ製造済みreservoirを共有することを意味しない。

Q2-2ではR207A--R207Cがfixed-goal core、R207DがBell-local controlとして確立している。Q2-4ではR206がreader側の逐次branch問題を避けても、R186のdirect-amplitude register additive-noise障害を解消しない。Q3ではM64のdirect A2、finite-bandwidth/Hamiltonian lift、continuous-space一様極限、多粒子化、全周期統合が強化課題として残る。

置換済みの旧作用殻型Q1/Q2測定経路、旧paired-Hopf受信機構、旧Q3率latch、M60/M61旧Hamiltonian実装は現行主線へ重ねず、研究メモとGit履歴へ保存する。
