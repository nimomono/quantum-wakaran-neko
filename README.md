# quantum-wakaran-neko

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

論文では、こうした信号、配置、記録、時計自由度などをまとめた共通の有効状態構成をM54と呼びます。空間を伝わる信号については、局所的に結合した実振動子網M37からの物理的な実装も調べています。Q3の現行ミクロ模型M60では、1個のtracer $X$ に2つの実Duffing内部振動を付随させ、それらを一つの二成分非線形chiral媒体へ局所結合します。同じ媒体のnonlinear coreがaction reservoir、弱非線形leadが左右ballistic carrierとして働き、Brownian noiseとFDTは別の通常の平衡oscillator bathが担います。

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

この経路で、Born型2結果分布、同軸反復、異軸逐次測定、有限回のRabi--Zeno比較まで構成しています。

### 2. 複合系とBell型統計

複合系では、R181Bが複数の入力からテンソル積型の多モード信号を作り、R181Cが同じ記憶部上で局所操作やCNOT型の結合操作を実行します。中間で状態を測定して作り直さず、同じ物理信号を次の操作へ渡します。

Bell型統計では、固定一重項型の4モード信号にA側の設定を作用し、A端のR191で結果を作ります。その結果に対応する非規格化射影成分をB端へ物理的に渡し、B側の設定と2つ目のR191を作用します。これにより一重項と同じ余弦共同統計、非信号性、CHSH/Tsirelson値を再現します。

ただし、現行証人はA側の結果成分をB側へ物理的に渡す装置なので、Bell局所因子化を満たす空間分離模型ではありません。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査します。測定窓内の因果隔離をどこまで強められるかはQ2-2-Sで別に調べます。

一般回路については、$2^n$ 個の受動信号モードを許しつつ、外部から必要なプログラム、制御、時間、精度、読出しを多項式に抑えられるかをQ2-4で調べています。これは通常の意味で効率的な古典計算機シミュレーションや、量子計算機と同等の総物理資源を主張するものではありません。

### 3. 空間を動く粒子

Q3の信号部分系はQ1/Q2と無関係な別の数理を導入するものではありません。Q1で使うものと同じ局所実正準モードを空間の各点へ並べ、Q2で用いるのと同型の2体系エルミート結合を隣接点の間へ入れると、グラフLaplacian型のSchrödinger伝播と局所確率流が生じます。

各edge $e=\{i,j\}$ で

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

と置くと、

```math
I_{e,+}+I_{e,-}=|Z_i|^2+|Z_j|^2,
\qquad
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j)
```

が厳密に成り立ちます。Nelson関係 $\mathcal J_0=2m\nu$ の下では

```math
J_{ij}^{\rm sig}=\frac{\nu}{a^2}(I_+-I_-),
\qquad
u_{ij}^{\rm sig}=\frac{2\nu}{a}\frac{I_+-I_-}{I_++I_-}
```

となるため、signal currentを位相測定や外部除算で計算する必要はありません。

M60では、M37から得る $+$ と $-$ のchiral成分を一つの二成分Hamiltonian媒体へ受動的に結合します。この媒体は同じ $b_{\pm n}$ 自由度を持ち、tracer近傍のnonlinear coreではDuffing shellを熱化するaction reservoirとして、leadでは $+$ が右向き、$-$ が左向きのballistic carrierとして働きます。reservoirとwaveguideを別々の物理装置として置きません。

leadから来る左右のenergy densityを局所bath cellの可動COM $Y_e$ の左右へ入射させると、wave pressureの釣合いは

```math
\frac{U_e}{c}
=\beta_*(r)
=\frac{r}{1+\sqrt{1-r^2}},
\qquad
r=\frac{I_+-I_-}{I_++I_-}
```

という唯一安定なbath-frame速度を作ります。chiral媒体そのものへ非平衡FDTを課すことはしません。

実在tracer $X$ は、この $Y_e$ と共に並進する通常の平衡oscillator bathへ結合します。tracerのBrownian noiseとFDTはこの平衡bathが担います。一方、osmotic driftを与える2作用Gibbs shellは、tracerに付随する実2-mode Duffing内部自由度をM60のnonlinear coreへ弱結合し、そのmicrocanonical周辺化とfinite-time mixingから導きます。periodic potentialのhomogenizationに

```math
D_0=\frac{\nu}{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

を課すと、coarse-grained diffusionは $\nu$、current driftは $j/\rho+O(a^2)$、osmotic driftは $\nu\partial_x\log\rho$ となります。

構造としては

```text
M37/M54の空間信号 Z
        ↓ R195A
   chiral I±
        ↓ M60 passive port
統一chiral媒体 ─ nonlinear core → Duffing 2-action shell
        │
        └ ballistic lead → R196A → moving bath frame U
                                      ↓ R196B
                          equilibrium Brownian bath → tracer X_t
                                      ↓ R196C / R161
                              ideal Q3位置生成子
                                      ↓ R185
                         Nelson / time-symmetric Newton
```

となります。R161は共通数学interfaceであり、有限状態のcanonical Markov経路法則まで自身で定めます。R162はその法則を独立Poisson random measuresで具体化したoptional stochastic referenceとして残し、Q3-2の達成根拠やM60の基礎的物理実体とは扱いません。

### 4. Q3のミクロ物理正本と代替研究線

Q3の現行ミクロ物理正本はM60です。R198Aがtracerに付随する実2-mode Duffingから2-action shellを導き、R198B--R198Dが同じ二成分chiral媒体のnonlinear coreを有限reservoirとして接続します。R199Aは、その同じ媒体をballistic leadとして同時に使える有限時間windowを管理します。R195A/R196A--R196CはM60のtransport reductionとして、signal currentからmoving bath-frame、平衡GLE/FDT、R161位置生成子までを接続します。

R199Bでは、同じDuffing pairの作用和 $S=K_++K_-$ にstate count、作用差 $D=K_+-K_-$ にchiral current情報を持たせられることも調べます。ただし、これはM60の統合強化であり、Q3-2固定達成の必須依存にはしていません。

M56 Brownian-spin模型はspin-onlyの別実現を探る代替研究線としてnotesに残します。

## 現在どこまでできているか

Q1では、2モード可逆操作、Born型2結果測定、同軸反復、異軸逐次測定、有限Rabi--Zeno証人まで構成しています。

Q2では、2量子ビット型結合操作、3部分系の二段ゲート合成、非空間分離Bell型統計、一般回路の出力標本化を条件付きで構成しています。主な残件は、読出し、射影成分の振り分け、作用安定化、リセットなどを一つの具体的な装置へ統合することと、一般回路での物理配線・較正・揺らぎ条件を閉じることです。

Q3では、M37局所古典振動子signal、tracerに付随する実2-mode Duffing shell、nonlinear coreとballistic leadを兼ねる一つの二成分chiral媒体、moving bath-frame、平衡oscillator bathをM60共通模型へまとめています。R198A--R198CでDuffingから2-action Gibbs shellまでの静的Hamiltonian持上げを構成し、R198Dでfinite-time core mixing条件、R199Aでcore--lead同時使用条件を明示します。signal marginalはR86のSchrödinger型有効力学、tracerまで含めるとR196A--R196C、R161、R185を通してNelson型の時間対称Newton則へ縮約します。R198Dの具体的mixing witnessとR199Aの具体的同時parameter witnessは強化目標A1の残件です。

正式な達成判定、根拠結果、残っている条件は [PROJECT_STATUS.md](PROJECT_STATUS.md) を正本とします。

固定目標とは別に、全Q1--Q3について具体的古典ミクロ模型とその直接数値再現、Q1/Q2についてアナログ回路・実験可能パラメータ領域・回路直接シミュレーション、Q2-2について空間隔離を強める研究軸を [ENHANCEMENT_TARGETS.md](ENHANCEMENT_TARGETS.md) で管理しています。これらは固定目標の達成ラベルと独立です。理論側では規約を明示した採用開放SDEと理想白色雑音を認め、回路実装では有限帯域雑音へ落とします。

## この研究が主張しないこと

- 量子力学全体を古典力学から導出したとは主張しません。
- 空間分離されたBell局所模型を構成したとは主張しません。
- 指数的な内部自由度を除去した、または通常の意味で効率的な古典計算を得たとは主張しません。
- Q1、Q2、Q3の全部品を一台の完成した物理装置へ統合したとは主張しません。
- M60について連続空間の一様極限、多粒子、全周期のsource--clock--record統合、具体的core mixing witnessまで閉じたとは主張しません。

再現できた構造と、追加仮定が必要な構造、まだ未完成な構造を分けて記述することを重視しています。

## 読む順番

- [論文PDF](paper.pdf)
- [証明状態と理論の境界](PROJECT_STATUS.md)
- [固定目標に付随する強化目標](ENHANCEMENT_TARGETS.md)
- [プロジェクトの長期的方針](PROJECT_STANCE.md)
- [論文リポジトリの構成・執筆・更新規約](PROJECT_GUIDE.md)
- [論文用語と標準表記](TERMINOLOGY.md)
- [検算と品質確認](VALIDATION.md)
- [現行版のファイル一覧](MANIFEST.md)
- [論文外の研究メモ](notes/README.md)

論文本文の編集対象は `sections/` 以下です。`paper.md`、`main.tex`、`paper.pdf` は生成物として同期します。
