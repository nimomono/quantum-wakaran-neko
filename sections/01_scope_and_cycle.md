@number: 1
@chapter: 本文
@title: 問題設定、現行模型、達成範囲
@status: M54をQ1・Q2・Q3の共通有効信号構成族、M37を物理信号実装層、M61をQ3単一Hamiltonian親層、M60をその共通縮約ミクロ層として区別する。M64/R203を三実体・採用開放系のactive replacement candidateとする。現行固定達成主線は置換しない。

## 1.1 研究上の問い

本稿は、古典的な粒子、実振動子、熱浴、制御器、記録器から、量子力学に特徴的な状態空間、可逆力学、Born型排他的結果、測定後状態、複合系相関、空間力学がどこまで有効構造として現れるかを調べる。有限次元Schrödinger方程式を古典正準座標へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、記録、resetは得られないため、信号力学と測定instrumentを分けて構成する。

古典振動子・古典波で有限次元Hilbert空間、unitary、量子gateを模擬できること自体は先行研究がある。本稿の物理課題は、各試行の実信号から排他的結果を形成し、その結果成分を同じ試行の次操作へ渡すこと、有限時間・有限温度・無反応・誤差を装置境界まで含めて明示することにある。

## 1.2 現行因果鎖

Q1/Q2の2結果測定では、射影作用を

```math
J_\pm=\mathcal J_0Z^\dagger P_\pm Z
```

として保持し、R191へ渡す。

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{R191}}
r
\xrightarrow{\mathrm{R181D}}
P_rZ.
```

R191が結果形成と吸収記録までを担い、R181Dは結果を生成せずprojector routerと測定後結果成分受渡しだけを担う。固定有限深さでは非規格化結果成分をそのまま次段R191へ渡す。一般深さで作用下限が不足する場合だけR192の方向不変作用安定化を補助的に使う。

Q1 W型2モード特殊化では、R189Aが保持した左右作用座標をR193の直接decision Hamiltonianへ渡し、R191のmacrospin energyを

```math
\widehat S=A_L+A_R,
\qquad
\widehat D=A_L-A_R
```

として物理的に実現する。従ってQ1では

```math
\mathrm{M37\ W2}
\xrightarrow{\mathrm{R189A}}
(A_L,A_R)
\xrightarrow{\mathrm{R193}}
\mathrm{R191}
\xrightarrow{\mathrm{R181D}}
P_rZ
```

が現行測定主線である。R193はQ1専用特殊化であり、Q2の一般R191 transducer契約は変更しない。

Q3の信号数学はQ1/Q2から切り離された別構造ではない。各頂点へQ1型の局所実正準モードを配置し、辺へQ2で用いるのと同じ有限2体系エルミート生成子の結合族を反復すると、$i\mathcal J_0\dot Z=hZ$ の空間信号を得る。辺結合を持たない独立Q1列では $j_{ij}=0$ で空間伝播しないが、差モード型結合 $\sum_{\{i,j\}}g_{ij}|Z_i-Z_j|^2$ を加えるとグラフLaplacianと局所連続方程式が生じる。局所作用を規格化した $\pi_i$ と辺の反対称確率流 $j_{ij}$ がR161への共通入力となる。

M61は、この空間信号からM60の全Q3部品までを一つの時間非依存Hamiltonianへ載せる現行最深親模型である。M60はM61をcarrier/envelope・core/lead・moving-bath表示へ縮約した共通ミクロ層である。tracerには2つの実Duffing内部振動が付随し、同じ二成分chiral Hamiltonian媒体へ局所結合する。媒体のnonlinear coreはR198B--R198Dのaction reservoir、弱非線形leadはR199Aの左右ballistic carrierを担う。辺 $e=\{i,j\}$ ごとに

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

を作る。R195Aにより局所密度、signal current、edge velocityはこのchiral作用から厳密に決まる。R199Aが同じ媒体のballistic leadをR196Aへ接続し、R196Aは左右wave pressureから唯一安定なmoving frame $U_{\rm bath}$ を作る。R196Bはそのframeで通常の平衡oscillator bathへ結合したtracerをGLE/FDTとperiodic homogenizationで縮約し、R196Cはmetastable well-index processをR161へ持ち上げる。

```math
Z
\xrightarrow{\mathrm{R195A}}
(R,I_+,I_-)
\xrightarrow{\mathrm{R199A/R196A}}
(R,U_{\rm bath})
\xrightarrow{\mathrm{R196B}}
X_t
\xrightarrow{\mathrm{R196C/R161}}
L_{\rm R161}
\xrightarrow{\mathrm{R185}}
\mathrm{Nelson\ /\ time\!\!\text{-}symmetric\ Newton}.
```

R162のopen Poisson-jump過程はM60の基礎的実体ではなく、R161 lawのoptional referenceとして残す。Q1/Q2の測定装置そのものをQ3粒子へ流用するとは主張しない。

## 1.3 現行模型と実装階層

| 識別 | 分類 | 現行責務 |
|---|---|---|
| M54 | 共通有効信号--配置状態構成族 | 有限実正準信号、準備済み入力境界、永続記憶部、作業領域、時計、記録の共通型。Q1型局所信号とQ2型2体系結合の空間特殊化がQ3 signalの $(\pi,j)$ を与える。M54中のQ3位置座標は有効interfaceであり、その現行ミクロ担体はM60 tracerである |
| M37 | 物理Hamiltonian信号実装層 | Q3空間信号を局所ばね網で実装し、R187条件下ではW型最低2正常モードをQ1 W2制御信号へ接続する |
| M61 | Q3単一Hamiltonian親層 | 一つのmultiband媒体と一つの複合mobile subsystemを $H_{61}$ へ統合し、R200Cでsignal/chiral、R200Aでmoving branch converter、R200Bで内部harmonic bathをM60へ持ち上げる |
| M60 | Q3共通縮約ミクロ層 | M61から得るM37 signal、実2-mode Duffing shell、二成分chiral媒体のnonlinear core/ballistic lead、moving bath-frame、平衡GLEをR198A--R198D・R199A・R195A・R196A--R196Cを介してR161へ接続する |
| M64 | Q3三実体・開放系置換候補 | M37型coherent signal、独立tracer、signal-driven moving thermal reservoirの三実体に責務を絞る。R203Aがdensity/current辞書、R203Bがphase-volume free energy、R203Cがmoving Langevin縮約、R203Dがsmooth diffusionからR161 finite-volume chainへの直接接続を担う。現行M61/M60主線はまだ置換しない |
| M0 | 単一ミクロ装置統一目標 | Q1ではR193によりW2作用保持からmacrospin decision energyまでを具体化済み。Q3ではM37 signalからM60粒子輸送までを具体化する。macrospin浴、router、record、reset、Q2一般transducer、Q3 clock/recordを共通接続端とHamiltonian無限浴へ統合する全周期目標は未完成 |

M54の複素信号 $Z$ は実正準対の派生表示であり、独立した複素実体ではない。状態方向、規格化共分散、位置分布は解析上の統計量であり、単一試行の制御器へ書き戻さない。

## 1.4 系列ごとの最小構成

| 系列 | 信号準備・操作 | 結果形成・受渡し |
|---|---|---|
| Q1 | 準備済みW2入力、R187、R135、R140、R189A | R193、R191、R181D、R143--R144、R189B--R189C |
| Q2-1 | R181B、R181C | R191を2段、R181D router |
| Q2-2 | 固定一重項4モード、A/B設定gate | A端R191、R181D型router、B端R191、R180A/R180C監査 |
| Q2-3 | R181Bを2回、R181C、R177 | R191逐次読出し、R181D router |
| Q2-4 | M54一般 $2^n$ 直接モード、R181C | R191逐次読出し、R181D、非終端安全結果のR192、R179 open reset、R186資源監査 |
| Q3 | M61単一Hamiltonian親模型、M60共通縮約模型、R200A--R200C/R200、R198A--R198D、R199A、R195A・R196A--R196C | R161/R162 ideal reference、R185時間対称Newton、R112終位置record |

旧R190A--R190C、R170、R180Bは固定Q1/Q2の必須依存から外す。R184は旧M37--M54空間率latchの補助結果として保持するがM60主線の必須依存から外す。旧構成の詳細は `notes/` とGit履歴に保存する。

## 1.5 達成範囲

固定目標と達成ラベルは `PROJECT_STATUS.md` を正本とする。Q1-1、Q1-2、Q3-1--Q3-3Cは達成、Q2-1--Q2-4、Q3-4A、Q3-4B、Q3-5は各文書に明記した条件付き達成、Q3-6は未達のままとする。Q3-1/Q3-2の最深ミクロ親模型はM61/R200、共通縮約層はM60/R197である。Q3-1のsignal marginalはM37/R86、Q3-2のparticle pathはM60/R199A/R196A--R196C/R161/R185で接続し、R198A--R198Dが同一試行の2-action shellを供給する。R198Dの具体的core mixing witnessとR199Aのcore--lead同時parameter witnessは強化目標A1の残件とする。

固定目標に付随する強化目標は `ENHANCEMENT_TARGETS.md` を正本とする。全固定目標にA1/A2、Q1/Q2にB1/B2/B3、Q2-2にQ2-2-Sを置き、固定目標の達成状態とは独立に管理する。A1では採用開放SDEと理想白色雑音を許し、A2はそのミクロ方程式自体の直接数値再現を要求する。回路強化Bでは有限帯域雑音を含む実験可能領域へ落とす。


付録YのM64/R203A--R203Dは、A1で採用開放SDEを許す現行方針を使ってQ3因果鎖を最小化するactive replacement candidateである。density port、current-frame collective flow、friction/noiseを一つのmoving thermal reservoirへ統合し、PN/Eyring--Kramers経路を必須にせずR161 finite-volume interfaceへ接続する。M64はまだreplacement candidateであり、A1/A2状態、固定達成判定、M61/M60 required verifierを変更しない。

## 1.6 非主張

本稿は、量子力学全体を古典力学へ還元したこと、空間分離Bell局所模型を得たこと、指数的な内部受動自由度を除去したこと、全系列を同一製造済み装置へ統合したことを主張しない。R193によりQ1のR189A保持座標からR191 decision energyまでの直接接続は具体化するが、R191のmacrospin浴、吸収記録、R181D router、未使用保持対/resetを含む全周期を単一閉鎖Hamiltonianへ統合したことまでは意味しない。Q2の一般transducerもR193の対象外である。M61/M60についてcore mixingの具体的witness、core--lead同時parameter witness、R200A/Bのtracking--thermal-load同時window、continuous-space一様極限、多粒子、signal sourceからclock/recordまでの完全単一周期統合は別の強化課題である。
