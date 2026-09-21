@number: 1
@chapter: 本文
@title: 問題設定、現行模型、達成範囲
@status: M54をQ1・Q2・Q3の共通有効信号構成族、M37を物理信号実装層、M64/R203A--R203DをQ3粒子・Nelsonの現行三実体open modelとして区別する。M60/M61の旧Hamiltonian実装は現行主線から退役する。

## 1.1 研究上の問い

本稿は、古典的な粒子、実振動子、熱浴、制御器、記録器から、量子力学に特徴的な状態空間、可逆力学、Born型排他的結果、測定後状態、複合系相関、空間力学がどこまで有効構造として現れるかを調べる。有限次元Schrödinger方程式を古典正準座標へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、記録、resetは得られないため、信号力学と測定instrumentを分けて構成する。

古典振動子・古典波で有限次元Hilbert空間、unitary、量子gateを模擬できること自体は先行研究がある。本稿の物理課題は、各試行の実信号から排他的結果を形成し、その結果成分を同じ試行の次操作へ渡すこと、有限時間・有限温度・無反応・誤差を装置境界まで含めて明示することにある。

## 1.2 現行因果鎖

Q1/Q2の2結果測定では、射影作用を

```math
J_\pm=\mathcal J_0Z^\dagger P_\pm Z
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

M65が結果形成、正式な無反応、有限recordまでを担い、R181Dは結果を生成せずprojector routerと測定後結果成分受渡しだけを担う。固定有限深さでは非規格化結果成分をそのまま次段M65へ渡す。一般深さで作用下限が不足する場合だけR192の方向不変作用安定化を補助的に使う。

Q1 W型2モード特殊化では、R189Aが保持した左右作用座標 $A_L,A_R$ をM65へ直接入力する。M65は各作用を固定scale $A_*$ で割った $a_r=A_r/A_*$ をhubから結果chamberへの線形rateへ使い、状態依存除算を外部制御器へ要求しない。従ってQ1では

```math
\mathrm{M37\ W2}
\xrightarrow{\mathrm{R189A}}
(A_L,A_R)
\xrightarrow{\mathrm{M65/R204D}}
Y
\xrightarrow{\mathrm{R181D}}
P_rZ
```

が現行測定主線である。decision終了時にはM65 generatorを閉じ、R112型recordへ $Y\in\{L,R,\varnothing\}$ を固定してからR181Dを開く。

Q3の信号数学はQ1/Q2から切り離された別構造ではない。各頂点へQ1型の局所実正準モードを配置し、辺へQ2で用いるのと同じ有限2体系エルミート生成子の結合族を反復すると、$i\mathcal J_0\dot Z=hZ$ の空間信号を得る。辺結合を持たない独立Q1列では $j_{ij}=0$ で空間伝播しないが、差モード型結合 $\sum_{\{i,j\}}g_{ij}|Z_i-Z_j|^2$ を加えるとグラフLaplacianと局所連続方程式が生じる。局所作用を規格化した $\pi_i$ と辺の反対称確率流 $j_{ij}$ がR161への共通入力となる。

M64は、この空間signalへ一つのclassical tracerと一つのsignal-driven thermal reservoirを接続する現行Q3 open modelである。辺 $e=\{i,j\}$ ごとに

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

を作る。R203Aは作用和・差をregularized density/currentへ接続する。R203Bはsignal densityに依存するreservoir phase volumeからosmotic free energyを導き、continuous/finite-graph initial preparationとfinite-time mean-flow trackingを与える。R203Cはcanonical overdamped tracerをideal regularized diffusionへ縮約し、R203Dは1次元でR161/R185、一般finite graphでR124/R182/R125へ接続する。

Q3-2の現行因果鎖は、M37/R86 signalからM64/R203A--R203Cへ進み、R203D/R161を介してR185のNelson型・時間対称Newton則へ接続する。

R162のopen Poisson-jump過程はM64の基礎的実体ではなく、R161 lawのoptional referenceとして残す。Q1/Q2の測定装置そのものをQ3粒子へ流用するとは主張しない。

## 1.3 現行模型と実装階層

| 識別 | 分類 | 現行責務 |
|---|---|---|
| M54 | 共通有効信号--配置状態構成族 | 有限実正準信号、準備済み入力境界、永続記憶部、作業領域、時計、記録の共通型。Q1型局所信号とQ2型2体系結合の空間特殊化がQ3 signalの $(\pi,j)$ を与え、Q3位置interfaceはM64 tracerへ接続する |
| M37 | 物理Hamiltonian信号実装層 | Q3空間signalを局所ばね網で実装し、R187条件下ではW型最低2正常モードをQ1 W2制御信号へ接続する |
| M64 | Q3三実体open model | M37型coherent signal、一つのclassical tracer、一つのsignal-driven thermal reservoirからなる。R203Aがregularized density/current、R203Bがphase-volume free energyと初期準備・flow tracking、R203Cがcanonical overdamped diffusion、R203DがR161/R185およびfinite-graph位置読出しを担う |
| M0 | 単一ミクロ装置統一目標 | Q1/Q2/Q3の主要自由度、共通接続端、準備、操作、測定、record、reset、clockを一つのjoint microscopic device/processと共通反復周期へ統合する。規約を満たす開放ミクロ方程式を基本方程式として直接定めることを許し、Hamiltonian無限浴への持上げは上位強化とする。現行部品の全周期統合は未完成 |

M54の複素信号 $Z$ は実正準対の派生表示であり、独立した複素実体ではない。状態方向、規格化共分散、位置分布は解析上の統計量であり、単一試行の制御器へ書き戻さない。

## 1.4 系列ごとの最小構成

| 系列 | 信号準備・操作 | 結果形成・受渡し |
|---|---|---|
| Q1 | 準備済みW2入力、R187、R135、R140、R189A | M65/R204D--R204F、R181D、R143--R144、R189B--R189C |
| Q2-1 | R181B、R181C | M65を2段、R181D router |
| Q2-2 | 固定一重項4モード、A/B設定gate | A端M65、R181D型router、B端M65、R180A/R180C監査 |
| Q2-3 | R181Bを2回、R181C、R177 | M65逐次読出し、R181D router |
| Q2-4 | M54一般 $2^n$ 直接モード、R181C | M65逐次読出し、R181D、非終端安全結果のR192、R179 open reset、R186資源監査 |
| Q3 | M37/R86 signal、M64/R203A--R203D | R161/R185、R124/R182/R125位置読出し、R112終位置record |

旧R190A--R190C、R170、R180Bは固定Q1/Q2の必須依存から外す。R184は旧M37--M54空間率latchの補助結果として保持するがM64主線の必須依存から外す。旧構成の詳細は `notes/` とGit履歴に保存する。

## 1.5 達成範囲

固定目標と達成ラベルは `PROJECT_STATUS.md` を正本とする。Q1-1、Q1-2、Q3-1--Q3-3Cは達成、Q2-1--Q2-4、Q3-4A、Q3-4B、Q3-5は各文書に明記した条件付き達成、Q3-6は未達のままとする。Q3-1はM37/R86を達成証人とし、Q3-2はM37/R86からM64/R203A--R203D、R161、R185へ接続する。Q3-4A、Q3-4B、Q3-5はそれぞれR124、R182、R125をM64 finite-graph tracerへ接続する。

固定目標に付随する強化目標は `ENHANCEMENT_TARGETS.md` を正本とする。全固定目標にA1/A2、Q1/Q2にB1/B2/B3、Q2-2にQ2-2-Sを置き、固定目標の達成状態とは独立に管理する。M64の正式昇格だけからQ3-1-A1/Q3-2-A1またはA2を自動的に上げない。A1では開放SDEを基本方程式として直接定めることと理想白色雑音を許し、A2はそのミクロ方程式自体の直接数値再現を要求する。

## 1.6 非主張

本稿は、量子力学全体を古典力学へ還元したこと、空間分離Bell局所模型を得たこと、指数的な内部受動自由度を除去したこと、全系列を同一製造済み装置へ統合したことを主張しない。M65はQ1/Q2のopen selectorを共通化するが、M65、R181D、記録、未使用保持対/resetを各信号装置と一つの製造済み装置へ統合したことまでは意味しない。M64についてdirect A2、finite-bandwidth/Hamiltonian lift、continuous-space一様極限、多粒子、signal sourceからclock/recordまでの完全単一周期統合は別の強化課題である。


## M65 canonical open selector とfixed-goal主線

M65/R204A--R204FはQ1/Q2二結果射影用のcanonical open selector modelとして正本化する。正本発展則は3状態open Markov過程であり、phase-volume chamberとHamiltonian--Brownian縮約は追加実現へ分離する。M64とM65は同一粒子を共有せず、M64はQ3 spatial tracer、M65はQ1/Q2 binary selectorという別の物理役割を持つ。

Q1/Q2 fixed-goalの現行結果形成にはM65を採用する。R181D、R192、R179、R180A/R180Cはbinary selector interfaceを通じてM65へ接続する。旧R191/R193はM65へ責務を吸収した退役研究線としてnotes/Git履歴へ保存する。
