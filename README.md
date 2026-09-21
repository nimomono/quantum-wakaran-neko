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

論文では、こうした信号、配置、記録、時計自由度などをまとめた共通の有効状態構成をM54と呼びます。空間を伝わる信号は局所的に結合した実振動子網M37/R86から実装します。Q3の現行粒子模型M64では、このclassical coherent signalに一つのclassical tracerと一つのsignal-driven thermal reservoirを接続し、signal density/currentから初期位置準備、current drift、osmotic drift、R161/R185位置過程を構成します。

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

Q3のsignal部分系はM37/R86で実装する。各空間点の局所実正準モードと隣接結合からSchrödinger型の空間包絡と局所currentを得る。M64はこのsignalへ一つのclassical tracerと一つのsignal-driven thermal reservoirを接続する現行Q3 open modelである。

各edge $e=\{i,j\}$ で

```math
C_{e,+}
=
\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}
=
\frac{Z_i+iZ_j}{\sqrt2},
```

と置くと、

```math
I_{e,+}+I_{e,-}
=
|Z_i|^2+|Z_j|^2,
\qquad
I_{e,+}-I_{e,-}
=
2\operatorname{Im}(Z_i^*Z_j)
```

が厳密に成り立つ。R203Aはこのlocal情報をregularized current velocity $v_\delta$ へ接続する。

signal densityはreservoir phase volumeを変え、R203Bから

```math
F_{\rm res}
=
-k_BT\log r_X^\delta
+
\mathrm{const}
```

を得る。同じreservoirのmean flowは

```math
\tau_U\dot U
=
-U+c_Jr
```

で $v_\delta$ を有限時間追跡する。initial preparationではflow-to-tracer couplingを切った同じopen dynamicsからregularized位置分布を有限時間で準備する。

continuous profileのcanonical tracerは

```math
dX_t
=
\left[
U_X
+
\nu\partial_X\log r_X^\delta
\right]dt
+
\sqrt{2\nu}\,dW_t.
```

R203Cはこれをideal regularized diffusionへ有限時間で縮約し、R203Dの1次元specializationはR185と同じR161 activityへ一致する。Q3-2の主線は

```text
M37 / R86 signal
        ↓
M64 / R203A--R203C
        ↓
R203D / R161
        ↓
R185
Nelson / time-symmetric Newton
```

である。

finite-graph profileではlocal $R_i^\delta,J_{ij},T_{ij}^\delta$ だけからR161 rateを構成する。初期位置もconnected graph上のreversible preparation lawから有限時間で準備できる。これによりR124の有限障壁、R182のW型トンネル振動、R125の2経路干渉を同じclassical tracerの位置読出しへ接続する。

M60/M61のDuffing shell、chiral-medium、ballistic lead、single-Hamiltonian parentは、より複雑な旧Hamiltonian実装として現行論文主線から退役する。Git履歴には残すが、固定目標の達成根拠やrequired検算には使わない。

### 4. Q3の現行物理正本と強化課題

Q3-1のSchrödinger型signalはM37/R86を達成証人とする。Q3-2以降の位置過程はM64/R203A--R203Dを現行正本とする。物理的実体はM37型classical coherent signal、一つのclassical tracer、一つのsignal-driven thermal reservoirの三つである。複素包絡 $Z$、密度、current、reservoir mean flowは派生量またはcollective variableである。

M64ではprocess-law reduction errorとR185のNewton force residualを別々に管理する。finite-graphではinitial preparation、generator実装、終位置recordを $\varepsilon_{64,G}$ に一度ずつ数える。

A1/A2は固定目標とは独立に監査する。M64の正式昇格だけからA1/A2を自動的に達成へ上げない。A2ではM37 signal、preparation、mean-flow relaxation、canonical tracer SDEまたはfinite-graph jump lawを同一parameter setで直接発展・標本化する。Hamiltonian lift、finite bath、finite-bandwidth noise、underdamped lift、continuous-space一様極限、多粒子拡張、clock・record・resetまでの単一反復装置統合は強化課題として残る。


### M65：3状態open射影読出し

M65は、二つの保持済み射影作用から排他的な二結果を作るcanonical open selectorである。最小模型は $+,H,-$ の3状態連続時間Markov過程で、保持作用はhubから各結果へのrateへ線形に入る。Born確率表や作用和による除算を外部制御器へ入力せず、有限時間で結果比をBorn作用比へ近づける。phase-volume chamberとHamiltonian--Brownian縮約はM65の追加実現候補であり、正本の成立条件ではない。

M65はexact endpoint $A_r=0$ を含む入力、有限decision終了時のR112型record/latch、R189AからM65を経てR181Dへ渡すQ1互換接続までを備える。本変更ではQ1/Q2 fixed-goalの現行証人を切り替えない。Q1/Q2の達成根拠は引き続きR191/R193を使い、実装切替とR191/R193退役は後続変更へ分離する。
