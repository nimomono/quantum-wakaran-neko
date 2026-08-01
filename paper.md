# 概要


本論文は、有限自由度の古典 Hamiltonian 系を基礎としながら、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。中心となる有限部分は、粒子または測定対象、構造化誘導場、測定器、記録器、境界3モードからなる。外部自由度と仕事源まで含む拡大全系を

```math
H_{\rm all}
=
H_{\rm fin}(z)
+
H_{\rm ext}(y)
+
\varepsilon_{\rm ext}H_{\rm link}(z,y)
+
H_{\rm work}
```

と書く。全系は Hamiltonian とし、有限部分の収支だけが

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

となる。外部への常時のごく弱い漏れは、Fisher 応力や作用殻の等方性を直接生む入力ではない。主な役割は、欠陥成分の除去、有限浴の再帰抑制、記録安定化である。非零の準定常作用を保つには、流入または仕事源も必要になる。

現行モデルの共通部分は、時間に依存しない明・暗モード分解を持つ構造化誘導場である。第I部では、この誘導場を粒子の有効力学へ縮約する。第II部では、同じ物理構成を2粒子、左右測定器、共通境界3モードへ拡張し、境界作用殻の履歴測度へ縮約する。2つの縮約が同じ具体的な有限パラメータ集合から同時に成立することは未証明なので、1本の完成定理とは呼ばない。

第I部の有限誘導場を、粒子座標 $X$、運動量 $P$、場座標 $Q$、共役運動量 $\Pi$ により

```math
H_N
=
\frac{|P|^2}{2m}
+
V(X)
+
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}K_NQ
-
G_N(X)^{\mathsf T}B^{\mathsf T}Q
+
H_{\rm leak,N}
```

と書く。直接駆動方向 $B$ は、装置構造だけから固定した明部分空間に属し、暗射影 $P_{\rm D}$ に対して

```math
P_{\rm D}B=0
```

を満たす。ただし $K_N$ の非対角部分による明モードから暗モードへの間接伝播は許す。位相整合成分と欠陥成分を分ける射影も、得られた密度や目標量子状態から逆算せず、$K_N$、$B$、保存作用、装置の固定スペクトル窓から事前に定める。

外部自由度を含む全 Liouville 密度を場、浴、外部変数について積分すると、粒子の配置密度 $\rho_N$ と平均速度 $v_N$ は正確に

```math
\partial_t\rho_N
+
\nabla\cdot(\rho_Nv_N)
=0,
```

```math
m\rho_N
\left(
\partial_t+v_N\cdot\nabla
\right)v_N
=
-\rho_N\nabla V
+
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
```

を満たす。$\overline F_{{\rm G},N}$ は誘導場の条件付き平均反作用、$\Sigma_{p,N}$ は位置を固定した運動量共分散である。これは近似でなく、Liouville 方程式の0次と1次のモーメント式である。

線形誘導場は、指定した初期条件または二側境界条件の下で Green 作用素により正確に消去できる。自己共役な二側 Green 核は時間対称な記憶作用を与えるが、それだけで Markov 拡散や Nelson の平均加速度は導かれない。短記憶化、条件付き均質化、前進・後退で共通な拡散係数、非 Markov 残差の抑制を別々の縮約条件として置く。

二側 Markov 拡散が得られた有効モデル内部では、前進・後退流れ $b_+,b_-$ から

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
=
\nu\nabla\log\rho
```

が厳密に従う。このとき Bohm–Fisher 応力を

```math
P_F[\rho]
=
-m\nu^2\rho\,\nabla\nabla\log\rho
```

と定めれば、

```math
-\nabla\cdot P_F[\rho]
=
2m\nu^2\rho\,
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right)
```

となる。

第I部の中心課題は、ミクロ反作用と運動量流束がこの応力へ閉じること、すなわち

```math
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
\longrightarrow
-\nabla\cdot P_F[\rho]
```

を一様な誤差評価とともに示すことである。本論文はこれを **Fisher 閉鎖予想** と呼ぶ。左辺の正確なモーメント式、右辺の二側拡散内部での代数、両者が一致するための目標式は得るが、中央の収束はまだ証明しない。

補助結果として、有限 Fourier–Gauss 型経路法則の繰り込み済み粗視化作用について

```math
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\rm GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+
\frac{T^2}{Nh^2}
\right)
```

を付録で保つ。これは二側拡散が得られた後の作用表示を制御する厳密結果であり、Fisher 閉鎖予想の証明ではない。$h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。

第II部では、同じ構造化誘導場を、左右の局所反応座標、暗モード、共通境界3モードへ静的に分ける。局所測定窓の左右交差応答を $\varepsilon_{\rm loc}\ll1$ に抑え、共同重みは局所相互作用でなく、共通未来の境界適合ファイバーから得る。

境界3モードの作用を $J_+,J_s,J_r$ とし、共通総作用殻を

```math
J_++J_s+J_r=C_0
```

とする。縮約された殻接方向混合が非退化な $U(3)$ 等方拡散なら、共通殻上の正規化 Liouville 測度が一意な定常分布になる。この縮約方程式内部の一意性は厳密だが、同じ誘導場からその生成子を導くことは未解決である。

局所記録後の2つの実2次元伝達ベクトルから、固定した和・差基底により

```math
I_+^{AB}
=
I_0
\left[
1+ABV\cos\Delta_{ab}
\right],
\qquad
I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
```

を得る。共通作用殻を境界条件 $J_+=I_+^{AB}$ で切ると、残余ファイバー体積は

```math
W_{AB}
\propto
C_0-I_+^{AB}
=
J_*+I_-^{AB}
```

となる。対称な結果セクター、共通分解能、共通 coarea Jacobian の下で、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}AB\cos\Delta_{ab}
\right],
\qquad
V_{\rm eff}
=
\frac{I_0}{J_*+I_0}V
```

を得る。これは共通殻などの仮説の下での厳密な体積計算である。

履歴測度は、解空間へ直接 Liouville 測度を置くものではない。全境界正準位相空間の Liouville 測度を作用保存と境界適合条件で制限し、Hamiltonian の解写像で許容履歴空間へ押し出す。境界適合ファイバーが $a,b$ に依存するため、Bell の前提違反は測定設定独立性にある。対称セクターでは一側周辺が $1/2$ となる。

本論文が統合したのは、Fisher 側と Bell 側の完成導出ではなく、両者を同じ構造化誘導場、固定射影、二側条件付け、弱い外部交換という物理構成の下へ置き、どの縮約定理が未完成かを明示したことである。

# 問題設定、共通ミクロ構成、2つの縮約経路

> **位置づけ：** 第I部と第II部を論理的に無関係な2問題とは扱わず、1つの構造化誘導場を共有する2つの縮約として整理する。ただし同時実現定理は未完成である。


## 問題設定

本論文の目的は、明示的な古典 Hamiltonian 系から、量子力学に特徴的な確率構造が縮約された有効理論として出現し得るかを検証することである。量子力学を理論構成の入力に使わず、得られた有効式との比較にだけ用いる。

中心問題を次の2つに分ける。

1. 構造化誘導場を消去した粒子の正確な Liouville モーメント式が、二側短記憶極限で Fisher 応力を持つ Nelson 型有効力学へ閉じるか。
2. 同じ物理構成を2粒子、左右測定器、共通境界モードへ拡張したとき、境界作用殻の測度から Bell 型共同確率が生じるか。

第1の問題では、ミクロ反作用と運動量流束の和を Fisher 応力へ同定するところが未完成である。第2の問題では、共通作用殻を仮定した後の体積計算は厳密だが、その殻測度と境界適合を同じ有限誘導場から準備するところが未完成である。

従って、2つの問題の後半だけを厳密に計算して、前半のミクロ導出まで完了したとは呼ばない。

## 共通ミクロ構成

共通する有限部分を

```math
H_{\rm fin}
=
H_{\rm obj}
+
H_{\rm med}
+
H_{\rm dev}
+
H_\partial
+
H_{\rm fin-link}
```

と書く。各項の役割は次である。

| 項 | 役割 |
|---|---|
| $H_{\rm obj}$ | 粒子、生成源、または測定対象の Hamiltonian |
| $H_{\rm med}$ | 局所反応、位相整合、暗モードを含む構造化誘導場 |
| $H_{\rm dev}$ | 設定制御器、局所分析器、指針、記録器 |
| $H_\partial$ | Bell 側で用いる共通境界3モード |
| $H_{\rm fin-link}$ | 対象、誘導場、測定器、境界モード間の固定結合 |

外部環境 $H_{\rm ext}$、常時の弱い結合 $\varepsilon_{\rm ext}H_{\rm link}$、仕事源 $H_{\rm work}$ を加え、

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

とする。拡大全系の Hamiltonian 流れは Liouville 体積を保存する。有限部分だけを見れば、外部への流出、外部からの流入、制御仕事がある。

構造化誘導場の基底は時間、設定、結果に応じて切り替えない。直接結合方向が張る明部分空間と、その直交補空間である暗部分空間を装置の組立時に固定する。さらに位相整合成分と欠陥成分を分ける場合も、Hamiltonian の固定スペクトル部分空間または保存作用から定める。

## 2つの縮約

第I部の縮約は、次の順序で進む。

1. 粒子と構造化誘導場。
2. Liouville モーメント式。
3. 二側短記憶極限。
4. Fisher 応力を持つ有効力学。

第II部の縮約は、次の順序で進む。

1. 2粒子、測定器、構造化誘導場。
2. 局所記録と共通境界3モード。
3. 作用殻準備と境界適合。
4. Bell 型共同確率。

両者は、構造化誘導場、固定射影、二側条件付け、弱い外部交換を共有する。配置空間の拡散係数 $\nu$ と、境界作用殻の接方向拡散係数 $D_\partial$ は別の縮約係数である。同じ浴から両方が出ることや、同じパラメータ範囲で両方の近似誤差が小さいことは未証明である。

## 現行モデルと補助モデル

| モデル | 運用状態 | 役割と限界 |
|---|---|---|
| 粒子・装置・構造化誘導場・外部流路を持つ弱開放系 | 現行モデル | 2つの縮約の共通ミクロ構成。全周期と一様縮約定理は未完成 |
| 1試行内の有限閉鎖系 | 補助モデル | 正準写像、保存量、Liouville モーメント、作用殻体積を厳密に計算する |
| 線形誘導場 | 補助モデル | Green 作用素による場の消去を厳密に行う |
| 二側 Markov 拡散 | 補助モデル | 前進・後退流れと Fisher 応力を厳密に整理する |
| 線形 Fourier–Gauss 型経路法則 | 補助モデル | 作用形式の $C^1$ 収束を検証する |
| Gauss 幅の Routh 縮約 | 補助モデル | 固定作用と Fisher 項の一致を1つの可解例で検証する |
| 最小結果符号化器 | 補助モデル | 既存の2値符号を固定指針へ写す。一般測定器ではない |
| 3モード固定作用殻 | 補助モデル | 境界適合ファイバーの体積を厳密に計算する |
| $U(3)$ 等方殻拡散 | 補助モデル | 共通作用殻の一意な定常測度を与える |

閉鎖補助モデルまたは縮約方程式の内部で厳密な結果を、そのまま弱開放な現行モデルの厳密結果と呼ばない。

## 1試行内の近似閉鎖窓

局所測定窓では、有限部分の位相点を $z$、標準シンプレクティック行列を $J$ として

```math
\dot z
=
J\nabla H_{\rm fin}(z)
```

を0次近似に用いる。外部交換の小さい量を

```math
\varepsilon_{\rm open}
=
\frac{
\displaystyle
\sup_{0\leq t\leq T_{\rm meas}}
\left|
E_{\rm fin}(t)-E_{\rm fin}(0)
\right|
}{E_{\rm ref}}
```

とし、

```math
\varepsilon_{\rm open}\ll1,
\qquad
T_{\rm meas}\ll\tau_{\rm exch}
```

を要求する。$\tau_{\rm exch}$ は外部交換により中心作用または記録領域が変化する時間尺度である。

この近似は、常時の弱い外部結合を物理モデルから削除するものではない。外部結合は長時間では欠陥除去、再帰抑制、記録保持、再準備に効く。測定窓ではその効果を小さい補正として扱う。

## 可逆誘導、内部混合、外部交換の役割

3つの機構を混同しない。

| 機構 | 主な役割 | それだけでは生じないもの |
|---|---|---|
| 可逆な位相整合誘導場 | 条件付き反作用、枝間運動量流束、Fisher 応力の候補 | Markov 性、欠陥の不可逆減衰 |
| Hamiltonian な殻接方向混合 | 境界3モードの方向準備 | 非零殻半径の維持 |
| 常時の弱い漏れ・流入・仕事 | 欠陥除去、再帰抑制、記録安定化、半径分布の維持 | Fisher 応力、殻方向の一様性 |

純粋な一方向漏れはエネルギーまたは作用を減らすだけで、Fisher 応力も非零の一様作用殻も作らない。等方準備には殻接方向の混合、準定常半径には流入または仕事源との釣り合いが必要である。

## Fisher 側の縮約条件

第I部で必要な条件を次に分ける。

### [H] 明示的な誘導場 Hamiltonian

粒子と有限誘導場の直接結合方向を $B$ で指定し、暗射影 $P_{\rm D}$ に対して

```math
P_{\rm D}B=0
```

を要求する。場の内部行列 $K_N$ による明・暗間の間接伝播は別に評価する。

### [L] 正確な Liouville 縮約

外部自由度まで含む全密度から、配置密度、平均運動量、運動量共分散、誘導場反作用を定義し、0次・1次モーメント式を得る。ここまでは厳密結果である。

### [G] 二側 Green 応答

指定した初期条件または二側境界条件の下で線形場を消去する。二側条件では自己共役 Green 核を用いる。自己共役性は時間対称な記憶作用を与えるが、Nelson 加速度を直接意味しない。

### [M] 二側短記憶極限

条件付き均質化の結果として、前進・後退過程が共通の拡散係数 $\nu$ を持つ Markov 拡散へ近づくことを要求する。短相関時間、弱結合、観測時間、非 Markov 残差を明示する。この条件は未導出である。

### [F] Fisher 閉鎖

ミクロ反作用と運動量流束の和が $-\nabla\cdot P_F[\rho]$ へ収束することを要求する。本論文の中心予想であり、未証明である。

## Bell 側の縮約条件

第II部では、次を用いる。

### [B1] 局所交差応答の抑制

同じ誘導場の左右局所反応座標について、測定窓の交差応答比 $\varepsilon_{\rm loc}$ を小さくする。結合ベクトルの直交性だけでは十分でない。

### [B2] 位相同期した生成源

左右へ送る実2次元伝達ベクトル対は固定総入力作用を持ち、和・差作用は

```math
I_+^{AB}+I_-^{AB}=2I_0
```

を満たす。

### [B3] 対称な結果セクター

境界条件を課す前の基準 Liouville 測度、境界分解能、coarea Jacobian は、左右結果符号の反転で不変とする。

### [B4] 共通作用殻と境界適合

境界3モードは

```math
J_++J_s+J_r=C_0
```

という1つの作用殻を持ち、全結果に共通の分解能で

```math
J_+=I_+^{AB}(a,b)
```

を課す。

### [B5] 全殻等方準備

殻接方向の縮約生成子を $D_\partial\Delta_{S^5}$ で近似する。縮約方程式内部の定常測度は厳密に決まるが、この生成子のミクロ導出は未完成である。

## 試行周期と測度

繰り返し試行を次の6段階に分ける。

1. **欠陥除去と入口準備**：外部交換を用いて前試行の記録と欠陥成分を除き、粒子、誘導場、装置を指定した入口巨視領域へ戻す。
2. **殻準備**：Bell 側では境界3モードの総作用を狭い分布へ置き、Hamiltonian な殻接方向混合で方向の偏りを緩和する。
3. **生成源と設定準備**：位相基準、伝達ベクトル対、左右設定制御器を準備する。
4. **局所発展と記録**：左右交差応答が小さい窓で局所結果を形成し、指針へ記録する。
5. **境界適合**：記録済み伝達ベクトルを共通未来へ運び、共通作用殻の境界条件に適合する完結履歴を定める。
6. **消去と再初期化**：記録、局所反応座標、境界モードを次の試行へ戻し、必要な仕事と排熱を外部へ移す。

履歴確率は、解集合へ直接置いた Liouville 測度ではない。全境界正準位相空間の Liouville 測度を、保存作用、入口巨視領域、境界適合条件で条件づけ、Hamiltonian の解写像で許容履歴空間へ押し出す。

境界適合しない履歴を実験後に捨てる事後選別と、初めから2境界値問題として定義された履歴集団は数学的には異なる。ただし、後者を開始数と記録数を減らさない装置周期として実現することは未解決であり、Bell 監査では開始数、記録数、完了数、棄却数を別々に数える必要がある。

## 本章の結論

本論文の2部は、もはや「補助 Gauss 型作用」と「Bell 作用殻」という無関係な2問題ではない。構造化誘導場を共通ミクロ構成として、粒子の有効応力と境界履歴測度へ進む2つの縮約である。

一方、共通の物理構成を示したことと、同じ有限 Hamiltonian の同じパラメータ領域で両方の縮約を証明したことは異なる。第I部の Fisher 閉鎖、第II部の全殻準備と試行周期は、独立した中心未解決問題として残す。

# 第I部　構造化誘導場の縮約と Fisher 応力

# 粒子、構造化誘導場、外部流路の Hamiltonian

> **位置づけ：** 有限誘導場と固定射影を現行モデルとして定義する。正準性と線形場の方程式は厳密である。欠陥成分だけの減衰と有効短記憶化は外部スペクトルに依存する近似候補である。


## 有限誘導場モデル

粒子座標を $X\in\mathbb R^d$、運動量を $P\in\mathbb R^d$ とする。有限誘導場は $M_N$ 個の実正準対

```math
(Q,\Pi)
\in
\mathbb R^{M_N}\times\mathbb R^{M_N}
```

で表す。質量行列を座標変換で単位行列へ移した表示を用い、有限部分を

```math
H_N^{\rm fin}
=
\frac{|P|^2}{2m}
+
V(X)
+
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}K_NQ
-
G_N(X)^{\mathsf T}B^{\mathsf T}Q
+
H_{N}^{\rm nl}
```

とする。$K_N=K_N^{\mathsf T}>0$ は場の線形部分、$G_N:\mathbb R^d\to\mathbb R^r$ は粒子から場への一般化力、$B:\mathbb R^r\to\mathbb R^{M_N}$ は固定した直接結合方向、$H_N^{\rm nl}$ は必要に応じて加える弱い非線形内部混合である。

粒子と場の Hamilton 方程式は

```math
\dot X
=
\frac Pm,
\qquad
\dot P
=
-\nabla V(X)
+
\left[\nabla G_N(X)\right]^{\mathsf T}B^{\mathsf T}Q
-
\nabla_XH_N^{\rm nl},
```

```math
\dot Q
=
\Pi,
\qquad
\dot\Pi
=
-K_NQ
+
BG_N(X)
-
\nabla_QH_N^{\rm nl}.
```

従って線形場の直接駆動方向は $BG_N(X)$ である。結合条件を場のポテンシャル行列へ曖昧に埋め込まず、$B$ として独立に表示する。

## 静的な明・暗モード分解

$B$ の像を直接明部分空間

```math
\mathcal B_{\rm dir}
=
\operatorname{Ran}B
```

とする。これを含む固定明部分空間 $\mathcal B_{\rm B}$ と、その直交補空間 $\mathcal B_{\rm D}$ を選び、射影を $P_{\rm B},P_{\rm D}$ と書く。直接結合が暗モードを駆動しないための条件は

```math
P_{\rm D}B=0
```

である。

これは

```math
P_{\rm D}K_NB=0
```

を要求しない。一般に $P_{\rm D}K_NP_{\rm B}\neq0$ であり、場の内部発展によって明モードから暗モードへ作用が移る。この間接伝播は、欠陥移送、局所セクター間の交差応答、有限記憶を生む候補である。

$\mathcal B_{\rm B}$ と $\mathcal B_{\rm D}$ に適合した直交行列 $O_N$ を固定し、

```math
\widetilde Q=O_NQ,
\qquad
\widetilde\Pi=O_N\Pi
```

と変換する。座標と運動量へ同じ直交行列を作用させるので、この変換は正準である。変換後の $O_NK_NO_N^{\mathsf T}$ は一般にブロック対角ではない。従って静的な明・暗分解の正準性と、動力学的な直和分離を混同しない。

## 位相整合成分と欠陥成分

Fisher 側では、場の中に長時間保たれる位相整合成分と、外部へ移送したい欠陥成分を区別する必要がある。固定射影を

```math
P_{\rm c},
\qquad
P_\perp=I-P_{\rm c}
```

と書く。

$P_{\rm c}$ は次のいずれか、またはその組合せから事前に定める。

- $K_N$ の指定したスペクトル帯。
- 直接結合方向 $B$ と、その有限回の $K_N$ 作用が張る Krylov 部分空間。
- 装置が保存する作用または位相基準に対応する固定正準部分空間。
- Bell 側の局所、共通境界、暗モードを定める装置固定基底。

得られた $\rho$、欲しい波動関数、または目標 Fisher 応力を見て $P_{\rm c}$ を選んではならない。そうすると、導出すべき構造を射影へ先に書き込むことになる。

場の射影と、粒子運動量分散の分解も同一ではない。後者には第3章で枝指標を導入し、条件付き全分散公式を用いる。

## 外部流路を含む拡大全系

外部自由度を $(Y,\Theta)$、仕事貯蔵自由度を $z_{\rm work}$ とし、

```math
H_N^{\rm all}
=
H_N^{\rm fin}(X,P,Q,\Pi)
+
H_{\rm ext}(Y,\Theta)
+
\varepsilon_{\rm ext}
H_{\rm link}(Q,\Pi,Y,\Theta)
+
H_{\rm work}(z_{\rm work})
+
H_{\rm ctrl}
```

とする。$H_{\rm ctrl}$ は自律時計を含む設定変更、記録、再準備の有限相互作用をまとめた記号である。

全 Hamiltonian に外からの陽な時間依存がなければ、拡大全エネルギーは保存される。有限部分のエネルギー変化は Poisson 括弧により

```math
\frac{\mathrm d}{\mathrm dt}H_N^{\rm fin}
=
\left\{
H_N^{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm ctrl}
\right\}
```

と書ける。従って弱開放性は、有限部分の基本方程式へ非 Hamiltonian な摩擦を直接加えることではなく、外部自由度を消去した後の有限部分の収支として現れる。

## 選択的な弱漏れの候補

欠陥成分へ強く、位相整合成分へ弱く結合する候補を

```math
H_{\rm link}
=
\left(P_\perp Q\right)^{\mathsf T}C_\perp Y
+
\epsilon_{\rm c}
\left(P_{\rm c}Q\right)^{\mathsf T}C_{\rm c}Y
+
H_{\rm link}^{(\Pi)}
```

と書く。$0\leq\epsilon_{\rm c}\ll1$ とする。$H_{\rm link}^{(\Pi)}$ は必要な運動量結合を表す。

外部相関時間が短く、スペクトル密度が対象周波数帯で十分滑らかなら、外部消去後の線形化した平均振幅は概念的に

```math
\frac{\mathrm d}{\mathrm dt}
\begin{pmatrix}
P_{\rm c}Q\\
P_\perp Q
\end{pmatrix}
=
\begin{pmatrix}
A_{\rm c} & C_{{\rm c}\perp}\\
C_{\perp{\rm c}} & A_\perp
\end{pmatrix}
\begin{pmatrix}
P_{\rm c}Q\\
P_\perp Q
\end{pmatrix}
+
\eta_{\rm eff}(t)
```

となる。$\eta_{\rm eff}$ は外部消去後の有効雑音である。$A_\perp$ の実部が負で、$A_{\rm c}$ の減衰率が十分小さければ、欠陥成分だけが速く除去される。

目標とする時間尺度は

```math
\tau_{\rm corr}
\ll
\gamma_\perp^{-1}
\ll
\tau_{\rm coh},
\qquad
\gamma_{\rm c}
\ll
\gamma_\perp.
```

ここで $\tau_{\rm corr}$ は外部相関時間、$\gamma_\perp$ は欠陥減衰率、$\tau_{\rm coh}$ は位相整合成分を利用する時間、$\gamma_{\rm c}$ は整合成分の漏れ率である。

特定の有限外部スペクトルについて

```math
\|P_\perp Q(t)\|
\leq
C e^{-\gamma_\perp t}
\|P_\perp Q(0)\|
+
R_{\rm in}(t)
```

を一様に証明してはいない。$R_{\rm in}$ は外部からの流入補正である。従って「欠陥成分だけの指数減衰」は、外部スペクトル、弱結合極限、Markov 近似に依存する近似結果候補である。

## 弱漏れが担わない役割

選択的な漏れが実現しても、次は自動的には従わない。

1. 粒子の配置空間で Markov 拡散が生じること。
2. 前進・後退過程が同じ拡散係数を持つこと。
3. ミクロ反作用が Fisher 応力へ閉じること。
4. Bell 側の3モード作用殻が $U(3)$ 等方になること。
5. 非零の総作用半径が定常に保たれること。

純粋漏れは欠陥と再帰を抑える候補である。配置空間の二側拡散には条件付き均質化が必要であり、作用殻の方向準備には Hamiltonian な接方向混合が必要であり、非零半径の維持には流入または仕事源が必要である。

## 局所測定窓と長時間準備の分離

局所測定窓 $T_{\rm meas}$ では

```math
\varepsilon_{\rm open}
\ll1,
\qquad
\gamma_\perp T_{\rm meas}
\ll1
```

を要求し、有限部分を近似閉鎖系として扱う。一方、試行間の準備時間 $T_{\rm prep}$ では

```math
\gamma_\perp T_{\rm prep}
\gtrsim1
```

を許し、欠陥除去と再帰抑制を利用する。

同じ結合を測定中だけ人工的に切るのではなく、常時存在する弱結合を異なる時間窓で異なる次数として扱う。測定窓と準備窓の両方を満たすには

```math
T_{\rm meas}
\ll
\gamma_\perp^{-1}
\lesssim
T_{\rm prep}
```

という時間尺度分離が必要である。

## 本章の結論

粒子と構造化誘導場の直接結合を $B$ で明示し、暗モードを直接駆動しない条件を $P_{\rm D}B=0$ とした。静的な明・暗分解は厳密な正準変換であるが、$K_N$ の内部結合による間接伝播は残る。

位相整合射影は Hamiltonian の固定構造から事前に定める。外部への選択的な弱漏れは欠陥除去と再帰抑制の候補だが、その指数減衰には外部スペクトルと短記憶近似が必要であり、Fisher 応力または作用殻等方性の導出ではない。

# Liouville モーメント式と誘導場の消去

> **位置づけ：** 拡大全系の Liouville 方程式から連続の式と運動量収支を厳密に導き、線形誘導場を指定した境界条件の下で Green 作用素により消去する。Fisher 応力への閉鎖はまだ置かない。


## 拡大全系の Liouville 密度

外部自由度と仕事貯蔵自由度まで含む全位相点を

```math
Z
=
(X,P,Q,\Pi,Y,\Theta,z_{\rm work})
```

とする。全 Liouville 密度を $\varrho_N(Z,t)$ と書く。正規化を

```math
\int \varrho_N(Z,t)\,\mathrm dZ=1
```

とする。

全 Hamiltonian $H_N^{\rm all}$ に対して

```math
\partial_t\varrho_N
+
\{\varrho_N,H_N^{\rm all}\}
=0
```

が成立する。弱漏れの外部振動子を含める場合も、密度はそれらの座標を含む全位相空間上で定義する。有限部分の変数だけに摩擦付き Liouville 方程式を置くことは、外部消去後の別の近似である。

## 配置密度と条件付き平均

粒子の配置密度を

```math
\rho_N(x,t)
=
\int
\varrho_N(Z,t)
\,\mathrm dP\,\mathrm dQ\,\mathrm d\Pi
\,\mathrm dY\,\mathrm d\Theta\,\mathrm dz_{\rm work}
```

とする。$X=x$ を固定した条件付き平均を

```math
\mathbb E_N[A\mid X=x]
=
\frac1{\rho_N(x,t)}
\int
A(Z)
\varrho_N(Z,t)
\,\mathrm dP\,\mathrm dQ\,\mathrm d\Pi
\,\mathrm dY\,\mathrm d\Theta\,\mathrm dz_{\rm work}
```

と定義する。$\rho_N=0$ の点では局所式を用いない。

平均運動量と平均速度を

```math
\overline P_N(x,t)
=
\mathbb E_N[P\mid X=x],
\qquad
v_N(x,t)
=
\frac{\overline P_N(x,t)}m
```

とする。運動量共分散は

```math
\Sigma_{p,N}(x,t)
=
\mathbb E_N
\left[
(P-mv_N)
\otimes
(P-mv_N)
\mid X=x
\right].
```

誘導場の粒子への反作用を

```math
F_{{\rm G},N}(Z)
=
\left[\nabla G_N(X)\right]^{\mathsf T}
B^{\mathsf T}Q
-
\nabla_XH_N^{\rm nl}
```

とし、条件付き平均を

```math
\overline F_{{\rm G},N}(x,t)
=
\mathbb E_N
\left[
F_{{\rm G},N}
\mid X=x
\right]
```

とする。

## 0次モーメント

Liouville 方程式を粒子運動量と全内部変数について積分する。境界項が消える減衰条件、周期境界、または無流束境界を仮定すると、

```math
\partial_t\rho_N
+
\nabla_x\cdot
\left(
\frac1m
\rho_N\overline P_N
\right)
=0
```

を得る。従って

```math
\partial_t\rho_N
+
\nabla_x\cdot(\rho_Nv_N)
=0.
```

これは外部交換を含む拡大全系でも正確である。外部交換は条件付き平均 $v_N$ の時間発展へ入るが、粒子数を作成・消滅しない限り連続の式の形を変えない。

## 1次モーメント

Liouville 方程式へ $P_i$ を掛けて積分すると、

```math
\partial_t
\left(
\rho_N\overline P_{N,i}
\right)
+
\partial_{x_j}
\left[
\frac{\rho_N}{m}
\mathbb E_N
\left(
P_iP_j\mid X=x
\right)
\right]
=
-\rho_N\partial_{x_i}V
+
\rho_N\overline F_{{\rm G},N,i}
```

を得る。添字 $j$ について和を取る。

2次モーメントを

```math
\mathbb E_N
\left[
P\otimes P\mid X=x
\right]
=
m^2v_N\otimes v_N
+
\Sigma_{p,N}
```

と分解し、連続の式を使うと、

<!-- theorem-start:proposition -->
**命題（正確な粒子運動量収支）**

```math
m\rho_N
\left(
\partial_t+v_N\cdot\nabla
\right)v_N
=
-\rho_N\nabla V
+
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right).
```

<!-- theorem-end:proposition -->

この式は閉鎖近似を含まない。誘導場反作用と粒子運動量流束を分けて保持することが重要である。どちらか一方だけを Fisher 応力と同定してはならない。

## 枝内部幅と枝間流束

場の射影 $P_{\rm c},P_\perp$ は、粒子運動量共分散を自動的に分解しない。位相整合した局所枝を表す離散または連続指標を $\alpha$ とし、条件付き全分散公式を使う。

<!-- theorem-start:proposition -->
**命題（条件付き全分散分解）**

```math
\Sigma_{p,N}(x,t)
=
\mathbb E_N
\left[
\operatorname{Var}_N(P\mid X=x,\alpha)
\mid X=x
\right]
+
\operatorname{Var}_N
\left(
\mathbb E_N[P\mid X=x,\alpha]
\mid X=x
\right).
```

<!-- theorem-end:proposition -->

第1項は枝内部の運動量幅、第2項は枝中心間の流束である。どちらを欠陥、どちらを位相整合成分と呼べるかは、$\alpha$ のミクロな定義と時間尺度に依存する。

第2項を単に捨てると、枝間の位相整合運動量流束まで失う。第1項を常に零と置くと、有限温度、有限分解能、局所非線形性の影響を隠す。Fisher 閉鎖では、両項と誘導場反作用を合わせて評価する。

## 線形誘導場の初期値消去

$H_N^{\rm nl}=0$ とする。場方程式は

```math
\ddot Q(t)
+
K_NQ(t)
=
BG_N(X(t))
+
F_{\rm ext}(t)
```

である。$F_{\rm ext}$ は外部自由度を明示したままなら決定論的な Hamiltonian 力であり、外部集団について条件付けまたは平均した後には有効雑音として現れ得る。

$\Omega_N=K_N^{1/2}$ とすると、初期値問題の解は

```math
Q(t)
=
\cos(\Omega_Nt)Q(0)
+
\Omega_N^{-1}
\sin(\Omega_Nt)\Pi(0)
+
\int_0^t
\Omega_N^{-1}
\sin
\left[
\Omega_N(t-s)
\right]
\left[
BG_N(X(s))+F_{\rm ext}(s)
\right]
\,\mathrm ds.
```

これを $F_{{\rm G},N}$ へ代入すると、粒子は

1. 初期場に由来する自由反作用、
2. 自己履歴に依存する有限記憶項、
3. 外部流路から伝わる駆動、

を受ける。有限 $N$ では記憶核は準周期的であり、長時間には再帰を持つ。

## 二側境界条件での消去

場の境界条件を線形作用素 $\mathcal C_0Q(0)+\mathcal D_0\dot Q(0)=q_0$ と $\mathcal C_TQ(T)+\mathcal D_T\dot Q(T)=q_T$ で指定する。境界値問題が一意可解なら、

```math
Q(t)
=
Q_{\rm bd}(t)
+
\int_0^T
\mathcal G_N(t,s)
\left[
BG_N(X(s))+F_{\rm ext}(s)
\right]
\,\mathrm ds
```

と書ける。$\mathcal G_N$ は指定した境界条件に対応する Green 核、$Q_{\rm bd}$ は非同次境界データだけで決まる解である。

境界条件が場作用素の自己共役領域を定めるなら、

```math
\mathcal G_N(t,s)
=
\mathcal G_N(s,t)^{\mathsf T}
```

となる。従って消去後の履歴作用は時間交換に対して対称になる。

しかし、Green 核の自己共役性だけから

```math
\frac12
\left(
D_+D_-+D_-D_+
\right)X
```

という Nelson の平均加速度は導けない。一般には、非局所記憶、質量繰り込み、境界層、外部交換による反対称部分が残る。

## 条件付き平均反作用

二側消去式を使うと、条件付き平均反作用は概念的に

```math
\overline F_{{\rm G},N}(x,t)
=
F_{{\rm bd},N}(x,t)
+
\int_0^T
\mathbb E_N
\left[
\mathcal K_N
\left(
x,t;X(s),s
\right)
\mid X(t)=x
\right]
\,\mathrm ds
+
F_{{\rm ext},N}(x,t)
```

と書ける。$\mathcal K_N$ は $\nabla G_N$、$B$、$\mathcal G_N$ から決まる記憶核である。

この式は、反作用が一般に現在密度 $\rho_N(x,t)$ だけの局所汎関数ではないことを示す。Fisher 応力のような局所密度汎関数へ閉じるには、短記憶化、条件付き局所平衡、枝分解、外部交換の誤差評価が必要である。

## 正確な式と縮約仮説の境界

| 主張 | 導出状態 |
|---|---|
| 全 Liouville 方程式 | 定義した全 Hamiltonian に対する厳密結果 |
| 連続の式 | 厳密結果 |
| 運動量モーメント式 | 厳密結果 |
| 条件付き全分散分解 | 厳密結果 |
| 線形場の初期値消去 | 指定した初期条件の下で厳密結果 |
| 線形場の二側 Green 消去 | 一意可解な指定境界条件の下で厳密結果 |
| 自己共役 Green 核の時間交換対称性 | 自己共役境界条件の下で厳密結果 |
| 記憶核の Markov 化 | 予想・未解決 |
| 二側条件付き過程の共通拡散係数 | 予想・未解決 |
| 反作用と運動量流束の Fisher 閉鎖 | 中心的な予想・未解決 |

## 本章の結論

誘導場と外部流路を含む全 Liouville 密度から、粒子の連続の式と運動量収支を正確に得た。粒子が受ける有効応力の候補は、誘導場の条件付き平均反作用と運動量共分散の発散の組合せである。

線形誘導場は Green 作用素で消去できるが、一般には非局所記憶が残る。時間対称な Green 核は二側縮約の必要な構造を与えるが、Nelson の Markov 拡散または Fisher 応力を単独では強制しない。

# 二側短記憶極限、Fisher 応力、中心閉鎖予想

> **位置づけ：** 二側 Markov 拡散を仮定した後の浸透速度と Fisher 応力は厳密結果である。ミクロ誘導場からその拡散と応力へ至る縮約は中心的な予想・未解決である。


## 二側条件付き過程と Markov 性

第3章の有限 Hamiltonian 集団へ初期側と終端側の条件を課しても、粒子の縮約過程が自動的に Markov 過程になるわけではない。有限誘導場を消去すると、一般には履歴依存の記憶核が残る。

本章では、次の縮約が成立する場合の有効式を先に整理する。

1. 誘導場相関時間 $\tau_{\rm corr}$ が粒子の遅い時間 $\tau_{\rm slow}$ より十分短い。
2. 条件付き均質化により、有限次元分布が前進・後退 Markov 拡散へ収束する。
3. 前進と後退の2次変分が同じ正定値拡散行列へ収束する。
4. 非 Markov 残差、境界層、有限再帰、外部交換が観測窓で一様に小さい。

等方な場合の有効前進過程を

```math
\mathrm dX_t
=
b_+(X_t,t)\,\mathrm dt
+
\sqrt{2\nu}\,\mathrm dW_t^+
```

とし、後退過程を

```math
\mathrm d_-X_t
=
b_-(X_t,t)\,\mathrm dt
+
\sqrt{2\nu}\,\mathrm d_-W_t^-
```

と書く。$\nu>0$ は配置空間の拡散係数である。境界作用殻の係数 $D_\partial$ とは区別する。

## 前進・後退流れ

共通の正の時刻密度を $\rho(x,t)$ とする。前進と後退の Fokker--Planck 方程式は

```math
\partial_t\rho
=
-\nabla\cdot(\rho b_+)
+
\nu\Delta\rho,
```

```math
\partial_t\rho
=
-\nabla\cdot(\rho b_-)
-
\nu\Delta\rho
```

である。両式を加減し、

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
```

と置く。

<!-- theorem-start:proposition -->
**命題（二側拡散の流れ分解）**

共通の正の密度と共通の拡散係数 $\nu$ を持つなら、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=0,
```

```math
u
=
\nu\nabla\log\rho
```

が成立する。

<!-- theorem-end:proposition -->

これは二側 Markov 拡散モデル内部の厳密結果である。有限 Hamiltonian 集団からこのモデルが得られることの証明ではない。

## 時間対称平均加速度

前進・後退微分を $D_+,D_-$ とする。Nelson の時間対称平均加速度を

```math
a_{\rm ts}
=
\frac12
\left(
D_+D_-+D_-D_+
\right)X
```

と定義する。滑らかな $v,u$ について

```math
a_{\rm ts}
=
\partial_tv
+
(v\cdot\nabla)v
-
(u\cdot\nabla)u
-
\nu\Delta u
```

が成立する。

$u=\nu\nabla\log\rho$ を使うと、

```math
(u\cdot\nabla)u
+
\nu\Delta u
=
2\nu^2
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right).
```

従って時間対称 Newton 式

```math
ma_{\rm ts}
=
-\nabla V
```

は

```math
m
\left[
\partial_tv
+
(v\cdot\nabla)v
\right]
=
-\nabla V
+
2m\nu^2
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right)
```

と同値である。

自己共役 Green 核を得ただけでは、この時間対称 Newton 式は従わない。Green 消去後の非局所作用が、Markov 極限と条件付き変分を通じて上式へ収束することを示す必要がある。

## Fisher 情報と応力

Fisher 情報を

```math
\mathcal I[\rho]
=
\int
\rho
|\nabla\log\rho|^2
\,\mathrm dx
```

とする。浸透速度の2乗平均は

```math
\int\rho|u|^2\,\mathrm dx
=
\nu^2\mathcal I[\rho]
```

である。正規化制約と境界項が消える条件の下で、

```math
\frac{\delta\mathcal I}{\delta\rho}
=
-4
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

となる。

Bohm–Fisher 応力を

```math
P_F[\rho]
=
-m\nu^2\rho\,
\nabla\nabla\log\rho
```

と定義する。

<!-- theorem-start:proposition -->
**命題（Fisher 応力恒等式）**

十分滑らかな正の密度について、

```math
-\nabla\cdot P_F[\rho]
=
2m\nu^2\rho\,
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right)
```

が成立する。

<!-- theorem-end:proposition -->

従って二側 Markov 拡散の時間対称 Newton 式は、連続の式と

```math
m\rho
\left(
\partial_t+v\cdot\nabla
\right)v
=
-\rho\nabla V
-
\nabla\cdot P_F[\rho]
```

という Euler 型運動量式で書ける。

## Fisher 閉鎖予想

第3章の正確なミクロ運動量式は

```math
m\rho_N
\left(
\partial_t+v_N\cdot\nabla
\right)v_N
=
-\rho_N\nabla V
+
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right).
```

二側拡散側の目標式と比較すると、必要な中心閉鎖は次である。

**予想（Fisher 閉鎖）**

適切な有限誘導場列、固定射影、二側境界集団、短記憶尺度、弱外部交換の下で、

```math
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
\longrightarrow
-\nabla\cdot P_F[\rho]
```

が指定した時空間ノルムで成立する。

この予想は現在の定理ではない。特に、$\overline F_{{\rm G},N}$ だけ、または $\Sigma_{p,N}$ だけを右辺へ同定するものではない。誘導場反作用、枝内部幅、枝間流束、外部補正を合わせた収束である。

## 無次元化した目標誤差

力密度の比較ノルムを $\|\cdot\|_{\mathcal X}$ とし、代表力密度を $\mathcal F_*>0$ とする。例えば、対象時間窓での $\|-\nabla\cdot P_F[\rho]\|_{L^2_tH^{-1}_x}$ の上界を $\mathcal F_*$ に選ぶ。

閉鎖誤差を

```math
\varepsilon_F^{(N)}
=
\frac1{\mathcal F_*}
\left\|
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
+
\nabla\cdot P_F[\rho]
\right\|_{\mathcal X}
```

とする。目標評価は

```math
\varepsilon_F^{(N)}
\leq
C
\left(
\varepsilon_{\rm mem}
+
\varepsilon_{\rm nM}
+
\varepsilon_{\rm diff}
+
\varepsilon_{\rm proj}
+
\varepsilon_{\rm defect}
+
\varepsilon_{\rm open}
+
\varepsilon_N
\right)
```

の形である。右辺は全て無次元量とする。

| 誤差 | 意味 |
|---|---|
| $\varepsilon_{\rm mem}=\tau_{\rm corr}/\tau_{\rm slow}$ | 短記憶化 |
| $\varepsilon_{\rm nM}$ | 条件付き過程の非 Markov 残差 |
| $\varepsilon_{\rm diff}$ | 前進・後退の拡散行列の不一致と異方性 |
| $\varepsilon_{\rm proj}$ | 固定位相整合部分空間からの漏出 |
| $\varepsilon_{\rm defect}$ | 枝内部欠陥と未除去成分 |
| $\varepsilon_{\rm open}$ | 測定窓内の外部交換 |
| $\varepsilon_N$ | 有限誘導場切断と再帰 |

この式は次元を揃えた目標評価であり、現時点では証明済みの上界ではない。

## Gauss 幅における Routh–Fisher 一致

一般の Fisher 閉鎖は未証明だが、1つの可解な幅モデルでは、固定作用の Routh 縮約と Fisher 項が一致する。

1次元の正規分布を

```math
\rho_\sigma(x)
=
\frac1{\sqrt{2\pi}\sigma}
\exp
\left(
-\frac{x^2}{2\sigma^2}
\right)
```

とすると、

```math
\mathcal I[\rho_\sigma]
=
\frac1{\sigma^2}.
```

一方、2次元内部座標を

```math
q
=
\sigma
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix}
```

とし、運動項を

```math
L_{\rm int}
=
\frac m2
\left(
\dot\sigma^2
+
\sigma^2\dot\theta^2
\right)
```

とする。循環作用

```math
J
=
m\sigma^2\dot\theta
```

を固定して $\theta$ を Routh 縮約すると、

```math
R_{\rm int}
=
\frac m2\dot\sigma^2
-
\frac{J^2}{2m\sigma^2}.
```

$J=m\nu$ と置けば、

```math
-\frac{J^2}{2m\sigma^2}
=
-\frac{m\nu^2}{2}
\mathcal I[\rho_\sigma].
```

従って Gauss 幅族では、固定内部作用の Routh 項と Nelson 作用の負の Fisher 項が厳密に一致する。

これは重要な整合性検査だが、一般密度の Fisher 閉鎖を証明しない。$J=m\nu$ の選択、Gauss 幅以外の形状自由度、位相整合部分空間の力学的準備が別に必要である。

## 補助的な線形 Gauss 型作用定理

二側 Markov 拡散が得られた後の作用表示を制御する補助結果を付録A、Bに残す。有限 Fourier–Gauss 型駆動、線形流れ、Gauss 初期分布、正定値の有限分解能終端記録、2次ポテンシャル、滑らかな有限次元パラメータ集合 $K$ を考える。

時間刻み $h$ の繰り込み済み粗視化作用を $\mathcal A_{N,h}^{R,U}$、極限の Guerra--Morato 作用を $\mathcal A_{\rm GM}^{R,U}$ とする。

<!-- theorem-start:theorem -->
**定理（線形 Gauss 型作用の $C^1$ 極限）**

ある $C_K<\infty$ が存在し、

```math
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\rm GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT
+
\frac{T^2}{Nh^2}
\right)
```

が成立する。$h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。

<!-- theorem-end:theorem -->

正の密度と境界項が消える条件の下で、

```math
\mathcal A_{\rm GM}^{R,U}
=
\int
\rho
\left[
\frac m2|v|^2
-
\frac m2|u|^2
-
U
\right]
\,\mathrm dx\,\mathrm dt
```

という Nelson 表示と厳密に一致する。

この定理は、定義した補助確率表示の作用値と有限次元パラメータ微分についての結果である。ミクロ誘導場から二側 Markov 拡散を導くこと、微視的時間発展が作用停留点を選ぶこと、Fisher 閉鎖を示すことは含まれない。

## 導出状態

| 主張 | 導出状態 |
|---|---|
| 共通拡散係数を持つ二側 Markov 拡散での $u=\nu\nabla\log\rho$ | 有効拡散モデル内部の厳密結果 |
| 時間対称平均加速度の分解 | 有効拡散モデル内部の厳密結果 |
| Fisher 応力恒等式 | 厳密結果 |
| Gauss 幅の Routh–Fisher 一致 | 指定した Gauss 変分モデル内部の厳密結果 |
| 線形 Gauss 型作用の $C^1$ 極限 | 補助モデルの厳密結果 |
| ミクロ誘導場から二側 Markov 拡散への縮約 | 予想・未解決 |
| 自己共役 Green 応答から Nelson 平均加速度への収束 | 予想・未解決 |
| ミクロ反作用と運動量流束の Fisher 閉鎖 | 中心的な予想・未解決 |
| 微視的時間発展による Nelson 停留点選択 | 予想・未解決 |

## 本章の結論

二側 Markov 拡散が得られれば、浸透速度、Fisher 情報、Bohm–Fisher 応力、Nelson 作用の関係は厳密に整理できる。Gauss 幅族では、固定内部作用の Routh 縮約が Fisher 項と一致する。

未完成なのは、その構造をミクロ Hamiltonian から得る中央の縮約である。本論文は、正確なミクロ運動量収支と Fisher 応力の間を **Fisher 閉鎖予想** として明示し、自己共役性または弱漏れだけで解決済みとは扱わない。

# 第II部　同じ物理構成の境界作用殻縮約と Bell 型統計

# 構造化誘導場の2粒子・測定器拡張

> **位置づけ：** 第I部と同じ固定射影を持つ誘導場を、左右局所反応座標と共通境界セクターへ拡張する。局所交差応答は近似条件、全殻拡散と一般測定器は予想・未解決である。


## 第II部の目的

第2章から第4章は、粒子と構造化誘導場の Liouville 縮約、二側短記憶極限、Fisher 閉鎖予想を扱った。そこから Bell 型結果重みは出ない。第II部では、同じ物理構成を2粒子、左右測定器、共通境界モードへ拡張する。

1. 左右の局所記録と共通境界モードを、1つの構造化誘導場の中に置く。
2. 第2章と同様に、直接結合ベクトルから時間に依存しない明・暗モード基底を定める。
3. 局所測定窓では、左右反応座標間の交差応答が小さいことを条件にする。
4. 局所記録後の伝達ベクトルを、共通未来で静的な和・差基底へ写す。
5. 共通境界3モードの作用殻と境界適合条件から、結果ごとの残余ファイバーを定める。

旧構成の中央比較器、相補時計、結果重みを直接与える終端関数は用いない。Bell 重みは第6章と第7章で、誘導場の殻接方向混合が準備する共通作用殻の残余体積として求める。常時の弱漏れだけに等方準備を担わせない。

本章で完全に構成するのは、一般測定器の全過程ではない。既存の結果符号を固定指針へ写す最小結果符号化器、静的な浴基底、局所交差応答の評価量、共通未来へ運ぶ伝達ベクトルを明示する。設定、到来変数、装置微視状態から結果を形成する一般測定相互作用は未構成である。

## 1つの構造化誘導場

質量で規格化した誘導場の正準座標を

```math
Q
=
\begin{pmatrix}
Q_1&\cdots&Q_N
\end{pmatrix}^{\mathsf T},
\qquad
P
=
\begin{pmatrix}
P_1&\cdots&P_N
\end{pmatrix}^{\mathsf T}
```

とする。誘導場の Hamiltonian を

```math
H_{\rm med}
=
\frac12P^{\mathsf T}P
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

と書く。$K$ は正定値実対称行列、$V_{\rm nl}$ は有限時間混合を補助する滑らかな非線形項である。第2章の $K_N,B,H_N^{\rm nl}$ を、左右装置と境界モードを含む有限次元へ拡張した表示である。

左右の局所応答座標を $x_A,x_B$ とし、誘導場への結合を

```math
H_{\rm loc-link}
=
\epsilon_A x_A c_A^{\mathsf T}Q
+
\epsilon_B x_B c_B^{\mathsf T}Q
```

とする。$c_A,c_B$ は同じ $N$ 次元誘導場内の直接結合ベクトルである。共通境界3モードへの結合ベクトルも同じ場内に置く。これらを列に並べた行列が第2章の $B$ に対応する。従って左右局所浴と境界浴を別々の独立系として追加するのではない。

有限装置部分は概念的に

```math
H_{\rm fin}
=
H_{\rm src}
+
H_{\rm set}
+
H_{\rm meas,A}
+
H_{\rm meas,B}
+
H_{\rm ptr}
+
H_{\rm med}
+
H_{\partial}
+
H_{\rm fin-link}
```

と書ける。$H_\partial$ は第6章の境界3モード、$H_{\rm fin-link}$ は局所反応座標、境界モード、誘導場暗モードの結合を含む。この式は部品表であり、全操作を1本の自律有限幅 Hamiltonian で実行する完成モデルではない。

現行の拡大全系は

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}(z_{\rm ext})
+
H_{\rm work}(z_{\rm work})
+
\varepsilon_{\rm ext}H_{\rm link}
```

である。$\varepsilon_{\rm ext}H_{\rm link}$ は常時存在し、局所セクターと境界セクターから外部へのごく弱い漏れと、逆向きの微小な流入の双方を許す。選択的な漏れは欠陥除去と再帰抑制を担い、殻方向の等方化は $V_{\rm nl}$ と固定内部結合による Hamiltonian 混合へ分ける。

## 静的な明・暗モード分解

結合ベクトル

```math
\mathcal C
=
\operatorname{span}
\left\{
c_A,c_B,c_{\partial,1},\ldots,c_{\partial,m}
\right\}
```

を誘導場の明部分空間とする。$c_{\partial,\alpha}$ は境界3モードを混合する場方向である。この明部分空間を第2章の $\mathcal B_{\rm B}$ に取り、暗射影 $P_{\rm D}$ に対して $P_{\rm D}B=0$ とする。$\mathcal C$ の正規直交基底を先頭に並べる直交行列 $O$ を1つ固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde P=OP
```

とする。同じ $O$ を座標と運動量へ作用させるため、

```math
dP^{\mathsf T}\wedge dQ
=
d\widetilde P^{\mathsf T}\wedge d\widetilde Q
```

が成り立つ。従ってこれは正準変換である。

変換後の先頭成分には、左右の局所反応座標と共通境界反応座標を取る。残りは外部装置と直接結合しない暗モードである。記号上、

```math
\mathcal B
\simeq
\mathcal B_A^{\rm loc}
\oplus
\mathcal B_B^{\rm loc}
\oplus
\mathcal B_\partial^{\rm glob}
\oplus
\mathcal B^{\rm dark}
```

と書く。

この直和は、一般には Hamiltonian の厳密な直和ではない。$O K O^{\mathsf T}$ と非線形項は各部分空間を弱く結び得る。従って変換後の誘導場 Hamiltonian を

```math
H_{\rm med}
=
H_A^{\rm loc}
+
H_B^{\rm loc}
+
H_\partial^{\rm glob}
+
H^{\rm dark}
+
\varepsilon_{\rm cross}H_{\rm cross}
```

と整理する。$\varepsilon_{\rm cross}$ は単一の結合定数ではなく、対象時間窓で測る交差応答の代表尺度である。

明・暗モード分解は測定設定や結果に応じて切り替えない。$O$ は装置を組み立てた時点で固定され、全試行に同じ基底を用いる。局所、共通、和、差という名称は、同じ正準位相空間内の異なる固定部分空間を表す。

## 局所交差応答

まず $\varepsilon_{\rm nl}=0$ の線形浴を考える。浴を消去すると、局所反応座標には自己応答と交差応答を含む記憶項が現れる [12--14]。単位質量表示では、代表的な応答核を

```math
\chi_{XY}(t)
=
c_X^{\mathsf T}
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)
c_Y,
\qquad
X,Y\in\{A,B\}
```

と書ける。規格化や時間微分の位置は、どの局所変数へ結合するかにより変わる。本論文で必要なのは、対角核と非対角核の比である。

局所性の誤差を

```math
\varepsilon_{\rm loc}
=
\frac{
\displaystyle
\sup_{0\leq t\leq T_{\rm meas}}
\max\left(
|\chi_{AB}(t)|,
|\chi_{BA}(t)|
\right)
}{
\displaystyle
\sup_{0\leq t\leq T_{\rm meas}}
\min\left(
|\chi_{AA}(t)|,
|\chi_{BB}(t)|
\right)
}
```

と定める。適用条件は

```math
\varepsilon_{\rm loc}\ll1.
```

$c_A^{\mathsf T}c_B=0$ だけでは、この条件は保証されない。$K$ が2方向を動力学的に混ぜれば、有限時間後に交差応答が現れる。従って局所性は、結合ベクトルの直交性ではなく、実際の応答核または有限モデルの時間発展で検査する。

非線形浴と弱開放補正を含む場合は、同じ初期小摂動に対する線形化応答、または条件付き相関を用いて $\varepsilon_{\rm loc}$ を定義する。第7章の厳密な Bell 代数は $\varepsilon_{\rm loc}=0$ の補助モデルで行い、現行モデルへの接続では $O(\varepsilon_{\rm loc})$ の局所誤差として扱う。

## 局所分析器と最小結果符号化器

結果種を表す円周座標を $s_A,s_B$ とし、平坦領域上で

```math
A=\sigma(s_A)\in\{-1,+1\},
\qquad
B=\sigma(s_B)\in\{-1,+1\}
```

とする。生成源が左右へ送る実2次元伝達ベクトルを

```math
u_X
=
\begin{pmatrix}
Q_X\\
P_X
\end{pmatrix},
\qquad
X=A,B
```

とする。

局所分析器の理想正準写像は

```math
u_A^{\rm out}
=
A R[\phi(a)]u_A^{\rm in},
\qquad
u_B^{\rm out}
=
B R[\phi(b)]u_B^{\rm in}
```

である。$R[\phi]$ は実2次元回転行列、$\phi(a),\phi(b)$ は装置の設定較正である。この写像は、結果符号と設定位相を伝達ベクトルへ記録する。

応答モードの運動量を $p_X$、固定指針の運動量を $\Pi_X$ とする。短時間の局所 Hamiltonian パルスにより

```math
p_A^{\rm out}=A,
\qquad
p_B^{\rm out}=B,
```

```math
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B
```

を得る補助構成を用いる。有限幅パルスと浴交差応答を含めると、

```math
\Pi_X^{\rm out}
=
X
+
O(\varepsilon_{\rm pulse})
+
O(\varepsilon_{\rm loc})
```

となる。右辺の $X$ は $A$ または $B$ を表す。補正が指針の2つの巨視領域の間隔より小さければ、記録符号は変わらない。

この構成は、既存の2値符号を記録する最小結果符号化器である。設定、到来変数、装置微視状態から結果そのものを形成する一般の局所 Hamiltonian は与えていない。従って、結果の形成は現行モデルの未解決部分であり、後段の厳密な体積計算によって解決済みにはならない。

## 常時の弱い漏れと記録安定性

局所反応座標と暗モードを外部環境へ弱く結合する。結合は測定窓だけ切るのではなく常時存在する。第2章の $P_{\rm c},P_\perp$ を用い、欠陥射影 $P_\perp$ の漏れ率を位相整合射影 $P_{\rm c}$ より大きくする候補を採る。局所有限部分の収支を

```math
\dot E_X^{\rm loc}
=
P_X^{\rm ctrl}
+
J_X^{\rm in}
-
J_X^{\rm out}
+
J_X^{\rm cross}
```

と分ける。$J_X^{\rm cross}$ は同じ誘導場内の他セクターとの交換である。

局所記録に必要な時間尺度条件は

```math
\tau_{\rm form}
\ll
\tau_{\rm leak},
\qquad
\tau_{\rm record}
\ll
T_{\rm rec},
```

```math
\tau_{\rm mix}^{\rm dark}
\lesssim
\tau_{\rm record}
```

である。$\tau_{\rm form}$ は記録形成、$\tau_{\rm leak}$ は記録を担う明モードの作用が外部交換で変わる尺度、$\tau_{\rm mix}^{\rm dark}$ は一時情報が暗モードへ分散する尺度である。

漏れが強すぎれば記録形成を壊し、弱すぎれば有限誘導場の再帰を抑えられない。外部揺らぎの流入も指針領域をまたがない強さでなければならない。本論文は、具体的な外部スペクトルについてこの安定域を一様に証明しない。弱開放記録の安定性と欠陥成分だけの指数減衰は予想・未解決である。

## 共通未来の静的な和・差基底

局所記録時刻を $t_A,t_B$、両伝達ベクトルが同じ境界領域へ到達できる時刻を $t_C$ とし、

```math
t_A,t_B<t_C
```

とする。$t_C$ より前には、A側の局所 Hamiltonian はB側の設定と結果を含まず、B側も同様である。左右交差応答は $O(\varepsilon_{\rm loc})$ に抑える。

$t_C$ 以後、伝達ベクトルを静的な和・差基底へ写す。

```math
u_+
=
\frac{
u_A+u_B
}{
\sqrt2
},
\qquad
u_-
=
\frac{
u_A-u_B
}{
\sqrt2
}.
```

この変換は直交変換であり、対応する座標と運動量へ同じ行列を作用させれば正準である。和・差作用は

```math
I_+
=
\frac12\|u_+\|^2
=
\frac14\|u_A+u_B\|^2,
```

```math
I_-
=
\frac12\|u_-\|^2
=
\frac14\|u_A-u_B\|^2.
```

和・差基底は、測定後に結果に応じて選ぶ比較規則ではない。装置の固定された線形正常モードである。固定された損失のない接合部は位相体積を保存するが、共通作用殻上の一様測度を生成しない。この区別は第6章で用いる。

## 共通境界3モード

共通境界セクターに、和モード $a_+$、ソフトモード $a_s$、残余モード $a_r$ を置く。

```math
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
},
\qquad
J_\nu
=
|a_\nu|^2,
\qquad
\nu\in\{+,s,r\}.
```

$a_+$ は静的和モード $u_+$ の複素正準表示であり、

```math
J_+=I_+.
```

差モードの作用 $I_-$ と準備時の基準作用 $J_*$ は、境界接合部の損失のない正準写像により $a_s,a_r$ の総作用へ入る。

```math
J_s+J_r
=
J_*+I_-.
```

従って、

```math
C
=
J_++J_s+J_r
=
J_*+I_++I_-.
```

生成源が固定総入力作用 $I_++I_-=2I_0$ を持つなら、

```math
C=C_0,
\qquad
C_0=J_*+2I_0.
```

この関係は作用保存を表す。どの結果が何倍起こるかはまだ決めない。結果重みを得るには、3モード共通殻上の準備測度と、各結果セクターを切る共通分解能が必要である。

## 共通未来を残す理由

左右局所セクターを同じ有限誘導場の中に置いても、共通未来の境界構造は不要にならない。同じ場を共有するだけで Bell 重みが出るなら、その重みは共通過去の場変数、局所窓の交差応答、または非局所相互作用に書き込まれていなければならない。本モデルはその経路を採らない。

局所測定窓では左右交差応答を小さく保ち、共同重みは共通未来の作用殻を切る残余体積から得る。従って、局所 Hamilton 方程式の因果伝播と、完結履歴へ置く境界条件付けを分ける。

旧構成の Bell 固有な終端関数を除くことは、2境界値問題そのものを初期値問題へ置き換えることではない。本モデルに残るのは、

- 全結果に共通な作用保存則。
- 設定名を直接参照しない静的和・差基底。
- 3モード共通殻。
- 同じ分解能で課す境界適合条件。

である。

## 本章の結論

左右局所装置と共通境界モードを、複数の独立浴ではなく第I部と同じ固定射影を持つ1つの構造化誘導場として整理した。静的な明・暗モード分解は厳密な正準変換であるが、その後の Hamiltonian が完全な直和になるとは限らない。局所性は、測定窓内の交差応答 $\varepsilon_{\rm loc}$ を実際に小さくする条件として置く。

局所装置について明示したのは最小結果符号化器であり、一般測定器ではない。常時の弱い漏れは欠陥除去と有限誘導場の再帰抑制を担う候補だが、漏れだけでは境界作用殻を一様化しない。

共通未来では、固定された和・差正準基底から $I_+$ と $I_-$ を得る。境界3モードの総作用は $C_0=J_*+I_++I_-$ である。次章では、3モード全体の等方拡散が共通殻測度をどう準備し、その測度が残余ファイバー体積をどう決めるかを示す。

# 3モード境界作用殻と誘導場内部混合による等方準備

> **位置づけ：** 和・差作用、U(2) の不足、U(3) 不変測度、共通殻の周辺密度、残余ファイバー体積は厳密結果である。同じ誘導場からの全殻等方拡散と半径安定化の導出は未解決である。


## 和・差作用の余弦幾何

生成源が準備する2つの伝達ベクトルを

```math
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
```

```math
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
```

とする。第5章の局所記録後には

```math
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
```

```math
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
```

となる。$A,B\in\{-1,+1\}$ は局所固定指針に記録済みである。

相対角を

```math
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
```

とする。和・差作用は

```math
I_+^{AB}
=
\frac14
\left\|
u_A+u_B
\right\|^2,
```

```math
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
```

である。直接展開すると、

```math
I_\pm^{AB}
=
\frac14
\left[
r_A^2+r_B^2
\pm
2ABr_Ar_B\cos\Delta_{ab}
\right].
```

<!-- theorem-start:proposition -->
**命題（和・差作用の余弦恒等式）**
等振幅 $r_A=r_B=r$、固定相対生成源位相の下で、

```math
I_\pm^{AB}
=
I_0
\left[
1
\pm
AB\cos\Delta_{ab}
\right],
\qquad
I_0=\frac{r^2}{2}.
```

さらに、

```math
I_+^{AB}+I_-^{AB}=2I_0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
2つのベクトルの内積は

```math
u_A\cdot u_B
=
ABr^2\cos\Delta_{ab}.
```

これを和ベクトルと差ベクトルの2乗へ代入すればよい。和と差を加えると内積項が消える。
<!-- theorem-end:proof -->

位相雑音 $\delta$ を許し、その分布が設定と結果符号に依存しないとする。重みが $I_\pm$ に線形であるため、位相を先に平均できる。可視度 $0\leq V\leq1$ と位相ずれを $\Delta_{ab}$ へ吸収すれば、

```math
\overline I_\pm^{AB}
=
I_0
\left[
1
\pm
ABV\cos\Delta_{ab}
\right].
```

総入力作用は平均後も $2I_0$ である。振幅揺らぎを許す場合は、各試行で $I_++I_-$ が固定される範囲に中心定理を限定する。総作用自体の揺らぎは第8章の殻幅誤差へ含める。

## 3モード共通作用殻

境界3モードを

```math
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
},
\qquad
J_\nu=|a_\nu|^2,
\qquad
\nu\in\{+,s,r\}
```

とする。作用角変数では

```math
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
```

```math
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
```

総作用を

```math
C
=
J_++J_s+J_r
```

とする。固定値 $C_0>0$ の共通作用殻上の Liouville 測度は

```math
d\mu_{C_0}
=
\frac{
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_{\nu}
dJ_\nu\,d\theta_\nu
}{
\Omega_3(C_0)
},
```

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

複素3成分ベクトル $a=(a_+,a_s,a_r)^{\mathsf T}$ で見れば、この殻は

```math
a^\dagger a=C_0
```

という5次元球面である。

局所記録と静的和・差変換が与える境界適合条件は

```math
J_+=I_+^{AB}(a,b).
```

従って結果セクター $(A,B)$ に残る作用は

```math
C_0-I_+^{AB}
=
J_s+J_r.
```

$C_0=J_*+2I_0$ とすれば、

```math
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```

この恒等式は作用保存だけから従う。相対確率を得るには、異なる $J_+$ のファイバーにどの測度を置くかを決めなければならない。

## 残余2モードの U(2) 等方性では不足する

固定 $J_+=x$ の下では、残余2モードは

```math
J_s+J_r=C_0-x
```

という3次元球面を作る。$(a_s,a_r)$ に $U(2)$ が作用すると、この球面上で推移的である。従って、固定 $x$ の内部では正規化された $U(2)$ 不変測度が一意になる。

この事実から、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac{
1
}{
C_0-x
},
\qquad
0\leq J_s\leq C_0-x
```

という一様作用分配が従う。しかし、これは各ファイバー内部の条件付き分布であり、異なる $x$ のファイバー間の相対質量を決めない。

<!-- theorem-start:proposition -->
**命題（U(2) 等方性の不足）**
任意の非負可積分関数 $f$ に対し、

```math
d\mu_f
\propto
f(J_+)
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_\nu dJ_\nu\,d\theta_\nu
```

は、残余2モード $(a_s,a_r)$ に関して $U(2)$ 不変である。しかし、$J_+=x$ のファイバー質量は

```math
W_f(x)
\propto
f(x)(C_0-x)
```

となる。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$f(J_+)$ は残余2モードの回転で変化しない。固定 $J_+=x$ で角変数を積分し、$J_r$ のデルタ関数積分を行うと、

```math
\int_0^{C_0-x}dJ_s
=
C_0-x
```

が残る。従って任意の $f(x)$ がファイバー間の相対質量へ残る。
<!-- theorem-end:proof -->

従って、残余2モードの等方性だけから Bell 重みを導くことはできない。必要なのは、$J_+$ を含む3モード共通殻全体の測度である。

## U(3) 不変測度

$U(3)$ は $a^\dagger a=C_0$ の球面上へ推移的に作用する。従って、正規化された $U(3)$ 不変確率測度は一意であり、固定作用殻の Liouville 測度 $d\mu_{C_0}$ と一致する。

<!-- theorem-start:proposition -->
**命題（共通殻不変測度の一意性）**
$S_{C_0}^5=\{a\in\mathbb C^3:a^\dagger a=C_0\}$ とする。$S_{C_0}^5$ 上の正規化 Borel 測度が全ての $U(3)$ 変換に不変なら、その測度は $d\mu_{C_0}$ に等しい。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$U(3)$ は球面上で推移的であり、安定部分群は $U(2)$ である。従って球面は同次空間 $U(3)/U(2)$ と同一視できる。コンパクト群の正規化 Haar 測度を商空間へ押し出した測度は不変である。不変確率測度の平均作用を用いれば一意性が従う。作用角変数で書けば、その押し出しは $d\mu_{C_0}$ である。
<!-- theorem-end:proof -->

固定された損失のない3入力3出力接合部は $U(3)$ 変換を1つ実行するだけであり、単一の入力位相点を殻全体へ広げない。上の命題は不変測度の一意性を述べるのであって、Hamilton 方程式が確率測度を無から生成することを述べない。

## 誘導場内部混合による全殻等方拡散

境界3モードの準備窓で、構造化誘導場の多数の未読自由度と非線形内部混合を消去した縮約方程式を考える。理想的な殻接方向生成子を

```math
\mathcal L_{\rm iso}
=
D_\partial\Delta_{S^5},
\qquad
D_\partial>0
```

とする。$\Delta_{S^5}$ は固定作用殻の Laplace--Beltrami 作用素である。

この接方向生成子は、常時の外部漏れを直接拡散へ読み替えたものではない。Hamiltonian な内部混合が殻方向を探索し、弱い外部交換は欠陥除去、有限再帰の抑制、半径分布の維持を担う。2つの効果を同じ係数へまとめない。

<!-- theorem-start:theorem -->
**定理（等方殻拡散の定常測度）**
連結な固定作用殻 $S_{C_0}^5$ 上で

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

を考える。規格化された非負密度の定常解は定数だけであり、$d\mu_{C_0}$ が一意な定常確率測度である。初期密度が $L^2$ なら、

```math
\left\|
f_t-1
\right\|_{L^2(d\mu_{C_0})}
\leq
e^{-D_\partial\lambda_1t}
\left\|
f_0-1
\right\|_{L^2(d\mu_{C_0})},
```

ここで $\lambda_1>0$ は殻上 Laplacian の第1非零固有値である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
定常密度 $f$ に対し、部分積分から

```math
\int
f\Delta_{S^5}f\,d\mu_{C_0}
=
-
\int
\left|
\nabla_{S^5}f
\right|^2
d\mu_{C_0}.
```

左辺は0なので、連結性から $f$ は定数である。規格化により $f=1$ となる。時間発展については定数成分を除いた固有関数展開を用い、第1非零固有値で評価する。
<!-- theorem-end:proof -->

混合不足の尺度を

```math
\varepsilon_{\rm mix}
=
\exp
\left(
-D_\partial\lambda_1\tau_{\rm prep}
\right)
```

とする。$\varepsilon_{\rm mix}\ll1$ なら、滑らかな観測量について初期の方向偏りは小さくなる。

有限 Hamiltonian 浴からこの拡散を得る候補は、$U(3)$ の Hamiltonian 生成子を、等方な相関行列を持つ浴変数へ弱く結合することである。弱結合・短相関時間極限では、2次の縮約生成子が $U(3)$ の Casimir 作用素へ近づく。付録Cに具体形を示す。

ただし、有限閉鎖 Hamiltonian 流れは微細 Liouville 密度を保存し、一般には $L^1$ で一様密度へ収束しない。有限浴だけで主張できるのは、有限時間・有限分解能の混合または弱い観測量収束である。不可逆な一意定常分布を用いる場合は、常時の弱い外部交換まで含む縮約が必要である。

## 異方性と半径方向の弱開放補正

現行の縮約生成子を

```math
\mathcal L
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_{\rm aniso}
+
\mathcal L_C
```

と分ける。$\mathcal L_{\rm aniso}$ は殻接方向の異方成分、$\mathcal L_C$ は総作用 $C$ の半径方向変化を表す。

半径方向の有効式の候補を

```math
dC_t
=
-\gamma_C
\left(
C_t-C_0
\right)dt
+
\sqrt{2D_C}\,dW_t
```

とする。これは、外部への漏れと仕事貯蔵系または微小揺らぎからの流入が $C_0$ 付近で釣り合う線形化である。定常幅は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C},
\qquad
\varepsilon_C
=
\frac{\sigma_C}{C_0}.
```

$\varepsilon_C\ll1$ なら、固定殻計算を狭い準定常殻へ適用できる。純粋な漏れ

```math
\dot C=-\gamma_C C
```

だけでは、$C=0$ へ落ちるだけで $C_0>0$ の定常殻を作らない。

異方性と半径幅が小さく、境界ファイバーが殻端から離れていれば、滑らかな結果重みの補正を

```math
O
\left(
\varepsilon_{\rm aniso}
+
\varepsilon_{\rm mix}
+
\varepsilon_C
\right)
```

と整理できる。全係数を同じ有限浴の尺度から与える一様上界は未完成であるため、現行モデルへの接続は近似結果である。

## 共通殻の周辺密度

<!-- theorem-start:theorem -->
**定理（和モード作用の周辺密度）**
3モード固定作用殻の正規化 Liouville 測度について、$J_+=x$ の周辺密度は

```math
p_+(x)
=
\frac{
2(C_0-x)
}{
C_0^2
}
\mathbf1_{\{0\leq x\leq C_0\}}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数を積分すると $(2\pi)^3$ を得る。$J_+=x$ を固定した未規格化密度は

```math
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
=
(2\pi)^3(C_0-x).
```

これを

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}
```

で規格化すればよい。
<!-- theorem-end:proof -->

この線形密度が Bell 重みの起源になる。重要なのは、各 $x$ の残余2モード分布を別々に質量1へ規格化しないことである。4つの結果セクターを同じ3モード作用殻の切断として比較する。

## 残余ファイバー体積

結果セクター $(A,B)$ の理想境界条件を

```math
g_{AB}
=
J_+-I_+^{AB}(a,b)
=
0
```

とする。作用座標でこの制約を用いる場合、$|\partial g_{AB}/\partial J_+|=1$ であり、coarea Jacobian は全結果と全設定に共通である。

<!-- theorem-start:proposition -->
**命題（残余ファイバーの線形体積）**
$0<I_+^{AB}<C_0$ とする。固定作用殻と $g_{AB}=0$ の交わりに誘導される未規格化 Liouville 体積は

```math
\Omega_{AB}
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right)
```

に比例する。共通定数を除けば、

```math
W_{AB}
\propto
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$J_+=I_+^{AB}$ を固定し、$J_r$ のデルタ関数積分を行う。許される $J_s$ は

```math
0\leq J_s\leq C_0-I_+^{AB}
```

なので、その長さが残る。3つの角変数は共通因子 $(2\pi)^3$ を与える。
<!-- theorem-end:proof -->

一般の境界写像では、解集合自体を無条件にシンプレクティック多様体と呼ばない。全境界正準位相空間の Liouville 測度を、作用殻と境界適合写像で制限して得る誘導測度として定義する。複数解、分岐、caustic がある場合は、Jacobianと多重度を含める必要がある。

## 有限分解能

現実の境界適合条件には幅 $\delta_J>0$ がある。共通窓関数 $K_{\delta_J}$ を用い、

```math
K_{\delta_J}
\left(
J_+-I_+^{AB}
\right)
```

で制限する。$I_+^{AB}$ が殻端から $\delta_J$ より十分離れ、$K_{\delta_J}$ が全結果に共通なら、

```math
W_{AB}^{(\delta_J)}
=
c_{\delta_J}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
\frac{\delta_J^2}{C_0}
\right).
```

$c_{\delta_J}$ は全セクターに共通で規格化時に消える。窓幅または Jacobian が結果や設定に依存する場合は、余分な重みを直接導入するため認めない。

## 本章の結論

残余2モードの $U(2)$ 等方性は、固定 $J_+$ のファイバー内部を一様にするだけで、ファイバー間の質量を決めない。この不足は任意関数 $f(J_+)$ を用いた反例で厳密に示せる。

3モード全体の $U(3)$ 等方性は共通作用殻上の測度を一意に決める。縮約された等方拡散では、その測度が一意な定常分布になる。固定殻の $J_+$ 周辺は $C_0-J_+$ に比例し、境界条件 $J_+=I_+^{AB}$ を課した残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となる。

固定殻の幾何と縮約拡散の定常測度は、指定した補助モデル内で厳密である。一方、同じ構造化有限浴と常時の弱い外部交換から、非退化な $U(3)$ 等方生成子、混合時間、異方誤差、殻幅を導くことは未完成である。次章では、共通殻の誘導測度を履歴空間へ押し出し、Bell 型共同確率と前提違反を計算する。

# 境界作用殻測度からの Bell 型共同法則

> **位置づけ：** 全境界正準位相空間の Liouville 測度を共通殻と境界適合で条件づけた後の共同確率は厳密結果である。全殻測度のミクロな準備、境界適合の装置実現、一般測定器は予想・未解決である。


## 履歴測度の定義

第6章で得た Liouville 測度は、境界3モードの正準位相空間上にある。Bell 実験の結果確率として用いるには、その測度を完結履歴の空間へ移す必要がある。

初期側の生成源、設定制御器、局所装置、指針、誘導場暗モードをまとめて $\lambda$ とし、境界3モードを $\eta=(a_+,a_s,a_r)$ とする。設定制御器の巨視領域が $a,b$ を定め、局所 Hamiltonian 流れが結果 $A,B$ と伝達ベクトル $u_A,u_B$ を定める。

全境界正準位相空間の基準測度を

```math
d\mu_0
=
\rho_{\rm prep}(\lambda)
d\lambda\,
d\mu_{C_0}(\eta)
```

とする。ここで $d\mu_{C_0}$ は3モード共通作用殻の正規化 Liouville 測度である。結果セクターを

```math
\Sigma_{AB}
=
\left\{
\lambda:
A(\lambda,a)=A,\,
B(\lambda,b)=B
\right\}
```

とする。

境界適合写像を

```math
g_{AB}^{a,b}(\lambda,\eta)
=
J_+(\eta)
-
I_+^{AB}(a,b;\lambda)
```

とする。理想境界条件は $g_{AB}^{a,b}=0$ である。有限分解能では、全セクターに共通な窓関数 $K_{\delta_J}$ を用いる。

設定 $(a,b)$ の履歴測度は、$d\mu_0$ を $\Sigma_{AB}$ と境界適合窓で制限し、Hamiltonian の解写像

```math
\mathcal F_{a,b}:
(\lambda,\eta)
\longmapsto
\gamma_{a,b}
```

により履歴空間へ押し出して定める。記号的には、

```math
d\mu_{\rm hist}^{a,b}
\propto
\left(
\mathcal F_{a,b}
\right)_\#
\left[
\rho_{\rm prep}(\lambda)
K_{\delta_J}
\left(
g_{AB}^{a,b}
\right)
d\lambda\,
d\mu_{C_0}(\eta)
\right].
```

この定義で数えるのは、解集合そのものに無条件で置いた Liouville 体積ではない。全境界正準位相空間の Liouville 測度を、作用保存と境界適合条件で制限し、解写像で履歴空間へ押し出した測度である。

## 結果セクターの基準対称性

共通作用殻が決めるのは、各境界適合ファイバーの作用体積である。局所結果セクター自体の基準質量は、準備対称性から別に決める。

境界条件を課す前の質量を

```math
w_{AB}
=
\int_{\Sigma_{AB}}
\rho_{\rm prep}(\lambda)\,d\lambda
```

とする。左右の結果符号を独立に反転する測度保存対合を

```math
\mathcal S_A:
\Sigma_{AB}
\longrightarrow
\Sigma_{-A,B},
```

```math
\mathcal S_B:
\Sigma_{AB}
\longrightarrow
\Sigma_{A,-B}
```

とする。$\mathcal S_A,\mathcal S_B$ が準備 Hamiltonian、準備巨視領域、$\rho_{\rm prep}d\lambda$ を保つなら、

```math
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14.
```

Hamiltonian の形式が符号反転対称なだけでは不十分である。同じ Hamiltonian に非対称な準備密度を置けるため、準備巨視領域と基準測度まで対称でなければならない。

## 結果の未規格化質量

理想境界条件と共通 Jacobian の下で、結果 $(A,B)$ の未規格化質量は

```math
\widetilde W_{AB}
=
w_{AB}
\int
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\delta
\left(
J_+-I_+^{AB}
\right)
\prod_\nu dJ_\nu\,d\theta_\nu.
```

第6.8節の計算から、

```math
\widetilde W_{AB}
\propto
w_{AB}
\left(
C_0-I_+^{AB}
\right).
```

$C_0=J_*+2I_0$ と $I_++I_-=2I_0$ を用いれば、

```math
\widetilde W_{AB}
\propto
w_{AB}
\left(
J_*+I_-^{AB}
\right).
```

ここで $J_*$ は結果と設定に依存しない基準作用である。$J_*$ は、境界ファイバーが全結果で正の幅を持つための余裕でもある。$J_*$ が大きいほど角度依存の可視度は低下する。

有限分解能では、

```math
\widetilde W_{AB}^{(\delta_J)}
=
c_{\delta_J}
w_{AB}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
w_{AB}
\frac{\delta_J^2}{C_0}
\right).
```

$c_{\delta_J}$ が全結果と全設定に共通なら規格化で消える。結果ごとに異なる窓幅を用いると、欲しい重みを装置分解能へ直接書き込むことになる。

## Bell 型共同確率

位相雑音を平均した差作用を

```math
\overline I_-^{AB}
=
I_0
\left[
1
-
ABV\cos\Delta_{ab}
\right]
```

とする。$[S]$ の対称準備により $w_{AB}=1/4$ とする。

<!-- theorem-start:theorem -->
**定理（境界作用殻からの Bell 型共同法則）**
次を仮定する。

1. 境界3モードは1つの共通作用殻 $C_0=J_*+2I_0$ 上の Liouville 測度を持つ。
2. 4つの結果セクターの基準質量は等しい。
3. 境界条件は $J_+=I_+^{AB}$ であり、分解能と coarea Jacobian は全結果・全設定に共通である。
4. 生成源は固定総入力作用と可視度 $V$ を持つ。

このとき、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}
AB\cos\Delta_{ab}
\right],
```

```math
V_{\rm eff}
=
\frac{
I_0
}{
J_*+I_0
}V.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
未規格化質量は

```math
\widetilde W_{AB}
\propto
\frac14
\left[
J_*+I_0
-
AB I_0V\cos\Delta_{ab}
\right].
```

4セクターについて和を取ると、$AB$ に奇な項が消え、

```math
\sum_{A,B}
\widetilde W_{AB}
\propto
J_*+I_0.
```

従って各質量を総和で割れば主張を得る。
<!-- theorem-end:proof -->

$J_*=0$ かつ $V=1$ なら、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
AB\cos\Delta_{ab}
\right].
```

$J_*>0$ または $V<1$ なら、同じ余弦形で可視度が低下する。

## CHSH 値

相関関数は

```math
E(a,b)
=
\sum_{A,B}
AB
P(A,B\mid a,b)
=
-V_{\rm eff}\cos\Delta_{ab}.
```

標準的な4設定を選ぶと、

```math
|S_{\rm CHSH}|
=
2\sqrt2\,V_{\rm eff}.
```

従って CHSH 超過の条件は

```math
V_{\rm eff}
>
\frac1{\sqrt2}.
```

小さい補正 $\varepsilon_{\rm Bell}$ が相関へ一様に加わる場合、十分な超過余裕を持つには

```math
2\sqrt2\,V_{\rm eff}
-
2
\gg
O(\varepsilon_{\rm Bell})
```

が必要である。誤差の内訳は第8章で整理する。

## 非信号性

対称な共同確率をBについて和を取ると、

```math
\sum_B
P(A,B\mid a,b)
=
\frac12.
```

同様に、

```math
\sum_A
P(A,B\mid a,b)
=
\frac12.
```

従って一側周辺は反対側の設定に依存しない。この非信号性は、次の条件に依存する。

- $w_{AB}=1/4$。
- 共通の境界分解能。
- 共通の coarea Jacobian。
- $J_*$ と総入力作用が結果・設定に依存しない。
- 位相雑音と殻幅の分布が左右符号反転に不変。

これらが崩れる場合、一側周辺に残差が現れ得る。任意の偏った準備に対して非信号性が動的に回復することは示していない。

## 測定設定独立性

Bell の測定設定独立性は、完全な隠れた変数または履歴変数 $\Lambda$ の分布が

```math
\rho
\left(
\Lambda\mid a,b
\right)
=
\rho(\Lambda)
```

を満たすことを要求する。本モデルでは境界適合条件が

```math
J_+
=
I_+^{AB}(a,b)
```

であり、許容される残余ファイバーが設定によって変わる。従って、

```math
\rho_{\rm hist}
\left(
\Lambda\mid a,b
\right)
\neq
\rho_{\rm hist}(\Lambda)
```

が一般に成り立つ。

測定設定依存性は、初期密度へ結果式を直接書き込むことからではなく、同じ共通作用殻を設定依存の境界適合面で切ることから生じる。局所結果形成時に反対側の設定が Hamilton 方程式へ入ることを意味しない。

この構成は Bell の定理を否定しない。Bell 不等式を超えるために必要な前提違反を、完結履歴の測定設定独立性の破れとして明示する。

## 事後選別との区別

境界条件に適合しない軌道は、本理論上は実験後に捨てた記録済み試行ではなく、最初から指定した2境界値問題の解ではない。しかし、数学上の定義だけでは、実験装置が事後選別なしにその履歴集団を実現することを保証しない。

操作上は、少なくとも次を結果別・設定別に監査する。

1. 外部から与えた開始信号数。
2. 左右の局所指針が形成した記録数。
3. 境界段階まで完了した試行数。
4. 次試行へ再初期化できた回数。
5. 記録形成、殻準備、消去に要した時間と交換エネルギー。
6. 境界分解能と作用殻幅。

観測済み試行の一部を結果または設定に依存して除外しなければ Bell 値が出ない場合、本構成は検出事後選別へ退化する。開始数、記録数、完了数が共通係数だけで異なるなら、共同確率の規格化には影響しない。

## Bell 前提の一覧

| 前提または条件 | 本モデルでの地位 |
|---|---|
| 局所 Hamiltonian 応答 | 局所測定窓で $O(\varepsilon_{\rm loc})$ まで成立 |
| 結果の一意性 | 最小結果符号化器では成立。一般測定器は未構成 |
| 測定設定独立性 | 境界適合ファイバーの設定依存性により成立しない |
| 非信号性 | 対称準備と共通分解能の下で厳密 |
| 事後選別の不在 | 理論上は2境界解集合。装置実現では開始・記録・完了数の監査が必要 |
| 共通試行測度 | 全殻等方拡散の定常測度として縮約レベルで導出 |
| 全殻拡散のミクロ生成 | 予想・未解決 |

局所性と測定設定独立性を同じ条件として扱わない。局所 Hamilton 方程式の交差応答が小さくても、完結履歴の条件付き測度は設定に依存し得る。

## 旧終端関数との置換関係

旧構成では、基準初期密度へ終端関数を引き戻して

```math
\rho_{\rm old}
\propto
\rho_S
G_R\circ\Phi_{a,b}^{T}
```

とし、終端半空間の体積を Bell 重みへ変換していた。この構成では、Bell 固有の終端統計原理を独立入力として必要とした。

現構成では、

```math
d\mu_{C_0}
\longrightarrow
J_+=I_+^{AB}
\longrightarrow
W_{AB}
\propto
C_0-I_+^{AB}
```

という1つの共通作用殻の切断を用いる。設定名、結果名、目標相関を引数に持つ終端関数はない。中央比較器と相補時計も用いない。

ただし、これは境界条件付けを消したのではない。共通未来で $J_+=I_+^{AB}$ を要求し、許容履歴の測度を数える点で2境界構造は残る。未解決問題は、Bell 固有の終端関数の生成から、同じ構造化浴による全殻等方準備と共通境界適合の物理的実現へ移った。

## 本章の結論

3モード共通作用殻の Liouville 測度を、結果セクターと境界適合条件で制限し、履歴空間へ押し出す測度を定義した。対称な結果セクター、共通分解能、共通 Jacobian の下で、残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となり、Bell 型余弦共同確率が厳密に従う。

完全な余弦則には $J_*=0$ と $V=1$、CHSH 超過には $V_{\rm eff}>1/\sqrt2$ が必要である。対称準備では非信号性が成り立つ一方、完全履歴分布は設定に依存する。Bell の前提違反は測定設定独立性にある。

旧来の Bell 固有な終端関数と中央比較器は除いたが、共通未来を含む境界値問題は残る。全殻測度を同じ有限浴から準備すること、一般測定器を構成すること、事後選別なしの試行周期として実装することは未解決である。

# 2つの縮約の誤差、適用限界、反証条件

> **位置づけ：** Fisher 側と Bell 側の誤差を別々に管理する。Fisher 閉鎖と全殻拡散のミクロ導出は未完成であり、厳密な後段計算から遡って導出済みとは扱わない。


## Fisher 側の誤差

第I部では、正確な Liouville 運動量収支と、二側 Markov 拡散内部の Fisher 応力恒等式が得られている。両者を結ぶ Fisher 閉鎖は予想である。力密度の比較ノルム $\|\cdot\|_{\mathcal X}$ と代表力密度 $\mathcal F_*$ を用い、

```math
\varepsilon_F^{(N)}
=
\frac1{\mathcal F_*}
\left\|
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
+
\nabla\cdot P_F[\rho]
\right\|_{\mathcal X}
```

とする。中心結論には、少なくとも次の無次元誤差が入る。

| 誤差 | 物理的内容 | 検証方法 |
|---|---|---|
| $\varepsilon_{\rm mem}$ | 誘導場相関時間と遅い時間の比 | 記憶核の幅と粒子時間尺度を比較 |
| $\varepsilon_{\rm nM}$ | 二側条件付き過程の非 Markov 残差 | 3時刻条件付き分布と Chapman--Kolmogorov 残差 |
| $\varepsilon_{\rm diff}$ | 前進・後退の拡散係数不一致と異方性 | 短時間条件付き2次変分を前後で比較 |
| $\varepsilon_{\rm proj}$ | 固定位相整合部分空間からの漏出 | $P_{\rm c},P_\perp$ 間の有限時間応答 |
| $\varepsilon_{\rm defect}$ | 枝内部幅と未除去欠陥 | 条件付き全分散の2項を別々に測る |
| $\varepsilon_{\rm open}$ | 観測窓内の外部交換 | 拡大全系と閉鎖補助系の比較 |
| $\varepsilon_N$ | 有限場切断、再帰、境界層 | $N$、観測時間、外部結合を変えた収束 |

右辺の各誤差が小さくても、$\varepsilon_F^{(N)}$ の上界はまだ証明されていない。特に、自己共役 Green 核、選択的漏れ、Gauss Routh 一致のいずれも、単独では一般密度の Fisher 閉鎖を保証しない。

反証条件は明確である。短記憶化しても前進・後退の拡散行列が一致しない、固定射影からの漏出が消えない、または $\varepsilon_F^{(N)}$ が $N$ と時間尺度分離に対して減少しないなら、現在の中心縮約は成立しない。

## Bell 側の誤差分解

第7章の Bell 型共同確率は、理想化した共通作用殻、対称セクター、共通境界分解能の下で厳密である。弱開放な現行モデルへ接続するときの主要誤差を

```math
\varepsilon_{\rm Bell}
=
\varepsilon_{\rm loc}
+
\varepsilon_{\rm pulse}
+
\varepsilon_{\rm aniso}
+
\varepsilon_{\rm mix}
+
\varepsilon_C
+
\varepsilon_{\rm res}
+
\varepsilon_J
+
\varepsilon_S
```

と整理する。

| 記号 | 物理的意味 | 主な検証 |
|---|---|---|
| $\varepsilon_{\rm loc}$ | 局所測定窓の左右交差応答 | 有限浴の応答核、局所摂動実験 |
| $\varepsilon_{\rm pulse}$ | 局所正準写像の有限幅補正 | パルス幅を変えた収束 |
| $\varepsilon_{\rm aniso}$ | 殻接方向拡散の $U(3)$ 異方性 | 生成子の固有値、方向別相関 |
| $\varepsilon_{\rm mix}$ | 準備時間が有限であることによる初期偏り | 準備時間を変えた収束 |
| $\varepsilon_C$ | 総作用の半径方向幅 | $C$ の定常分布 |
| $\varepsilon_{\rm res}$ | 境界適合の有限分解能 | 窓幅を変えた収束 |
| $\varepsilon_J$ | coarea Jacobian と解多重度の変動 | 境界写像の微分、分岐監査 |
| $\varepsilon_S$ | 結果セクター基準質量の非対称 | 設定前の結果符号反転試験 |

各誤差が結果と設定に一様であり、境界ファイバーが殻端から離れていれば、

```math
P_{\rm phys}(A,B\mid a,b)
=
P_{\rm shell}(A,B\mid a,b)
+
O(\varepsilon_{\rm Bell})
```

と整理できる。全係数を同じ有限 Hamiltonian 浴から与える一様上界は未完成であるため、この接続は近似結果である。

## 局所交差応答

同じ有限浴の中で左右の局所セクターを定める以上、厳密な独立性を自動的には持たない。中心条件は

```math
\varepsilon_{\rm loc}\ll1
```

である。

交差応答が結果形成前に大きければ、B側の設定がA側の局所結果へ順時間的に影響する経路が生じる。この場合、測定設定独立性だけでなく局所性の監査も失敗する。交差応答が小さいが零でない場合は、一側周辺、設定頻度、相関関数へ現れる残差を同時に測る。

静的な明・暗モード基底の直交性は必要な構成要素だが、十分条件ではない。有限時間発展を支配する $K$ と非線形項を含めて、$\chi_{AB}(t)$ と $\chi_{BA}(t)$ を評価する。

## 全殻混合と U(2) の限界

残余2モードだけの $U(2)$ 等方性では、

```math
d\mu_f
\propto
f(J_+)
\delta
\left(
C_0-J_+-J_s-J_r
\right)
d\Gamma
```

という任意の $f(J_+)$ が残る。従って Bell 重みを決めるには、$J_+$ を含む全3モード殻の測度が必要である。

縮約生成子が

```math
\mathcal L
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_{\rm aniso}
```

なら、異方成分は定常密度を変形する。第1近似では、

```math
f_{\rm stat}
=
1
+
O(\varepsilon_{\rm aniso})
```

となるが、異方生成子の零モード近傍に小さい固有値がある場合は補正係数が大きくなり得る。単に結合定数が小さいことではなく、等方生成子のスペクトルギャップに対する相対量を評価する必要がある。

準備時間が有限なら、

```math
\varepsilon_{\rm mix}
\lesssim
\exp
\left(
-D_\partial\lambda_1\tau_{\rm prep}
\right)
```

で初期偏りを評価する。有限 Hamiltonian 浴だけを用いる場合は、この指数収束を微細密度へ主張せず、有限分解能観測量の混合誤差として測る。

## 常時の漏れと殻幅

外部へのごく弱い漏れは、有限浴の再帰抑制と記録安定化に役立ち得る。しかし、純粋な減衰は作用殻を一様化しない。半径方向に

```math
\dot C=-\gamma_C C
```

だけが働けば、定常状態は $C=0$ である。

$C_0>0$ の狭い準定常殻には、外部からの流入または仕事貯蔵系による復元が必要である。線形化した定常幅を

```math
\varepsilon_C
=
\frac1{C_0}
\sqrt{
\frac{D_C}{\gamma_C}
}
```

とする。結果ファイバーが殻端から

```math
\min_{A,B,a,b}
\left(
C_0-I_+^{AB}
\right)
\gg
\sigma_C+\delta_J
```

だけ離れている範囲で、固定殻の線形体積を安定に用いる。

総作用の平均または幅が結果や設定に依存する場合、規格化で消えない余分な重みが生じる。これは単なる可視度低下ではなく、非信号性残差や高次調波を生み得る。

## 境界分解能、Jacobian、複数解

理想線形制約

```math
g_{AB}=J_+-I_+^{AB}=0
```

では、作用座標に関する Jacobian は1である。現実の境界写像を $g_{AB}^{\rm phys}$ とすると、coarea 公式は

```math
W_{AB}
\propto
\int_{
\left(
g_{AB}^{\rm phys}
\right)^{-1}(0)
}
\frac{
\rho_\partial
}{
\left|
\nabla g_{AB}^{\rm phys}
\right|
}
d\Sigma
```

を与える。

次の場合は単純な線形体積則を再検討する。

- $|\nabla g_{AB}^{\rm phys}|$ が結果または設定に依存する。
- 1つの境界データに複数の解が対応する。
- caustic で解の多重度が変わる。
- 境界面が殻端へ接する。
- 分解能窓が非対称または結果依存である。

これらの効果をまとめて $\varepsilon_J+\varepsilon_{\rm res}$ とする。共通分解能を較正するだけでなく、境界写像の微分と解多重度を検査しなければならない。

## CHSH 超過の安定条件

理想相関は

```math
E(a,b)
=
-V_{\rm eff}\cos\Delta_{ab},
\qquad
V_{\rm eff}
=
\frac{I_0}{J_*+I_0}V.
```

誤差が4つの相関値それぞれに最大 $\delta_E$ 入るなら、

```math
\left|
\delta S_{\rm CHSH}
\right|
\leq
4\delta_E.
```

従って、CHSH 超過を誤差込みで主張する安全条件は

```math
2\sqrt2\,V_{\rm eff}
-
4\delta_E
>
2.
```

$\delta_E$ は相関関数の誤差であり、確率表の最大絶対誤差と同じとは限らない。数値検算では共同確率、相関、周辺確率を別々に報告する。

## 否定的結果と適用限界

現時点で確立している否定的結果をまとめる。

1. 残余2モードの $U(2)$ 等方性だけでは、異なる $J_+$ のファイバー間質量を決められない。
2. 固定された損失のない接合部は Liouville 測度を保存するが、単一状態から一様測度を生成しない。
3. 純粋な一方向漏れは $C_0>0$ の一様作用殻を準備しない。
4. 有限閉鎖 Hamiltonian 流れは微細 Liouville 密度を一般に強収束させない。
5. 左右を同じ誘導場へ入れただけでは、共通未来の境界条件は不要にならない。
6. Bell 型余弦則は配置空間位相の循環量子化を含意せず、Wallstrom 問題を解かない [19]。
7. 余弦相関が得られても、Tsirelson 限界を一般原理から選んだことにはならない。

旧終端関数を削除したことを、確率測度のミクロな生成問題が解決したとは表現しない。問題は、結果依存終端重みの生成から、全3モード殻の等方準備と共通境界適合の実現へ移った。

## 反証に使える観測量

現行モデルは、少なくとも次の量で検査できる。

- 正確なミクロ力密度と Fisher 応力の残差 $\varepsilon_F^{(N)}$。
- 前進・後退の短時間条件付き2次変分から得る拡散行列。
- 条件付き3時刻分布の非 Markov 残差。
- 固定射影 $P_{\rm c},P_\perp$ 間の有限時間応答と欠陥減衰率。
- 局所測定窓の交差応答核 $\chi_{AB}(t),\chi_{BA}(t)$。
- 境界3モードの $J_+$ 周辺が $2(C_0-J_+)/C_0^2$ に従うか。
- 準備時間に対する初期方向偏りの減衰。
- 作用殻幅 $\sigma_C/C_0$ と結果別・設定別の平均作用。
- 境界分解能を変えたときの共同確率の収束。
- 高次調波 $\cos(2\Delta)$、$\cos(3\Delta)$ の残差。
- 一側周辺の反対側設定依存性。
- 開始数、記録数、完了数、再初期化数の結果別・設定別差。
- $J_*$ を変えたときの可視度 $I_0V/(J_*+I_0)$。

$J_+$ 周辺が線形でない、Jacobianが結果依存、開始後の棄却率が設定依存、局所交差応答が無視できない、といういずれかが確認されれば、中心導出の適用条件は破れる。

## 残る課題

中心的な未解決問題は次である。

1. 明示的な構造化誘導場から二側 Markov 拡散を導き、前進・後退の拡散係数と非 Markov 残差を評価する。
2. 誘導場反作用と運動量流束の Fisher 閉鎖を、次元の揃った一様誤差評価として証明する。
3. 固定位相整合射影と欠陥射影を保ったまま、欠陥成分だけの減衰と再帰抑制を外部スペクトルから導く。
4. 同じ誘導場から局所反応座標と境界3モードの双方を導き、局所交差応答を評価する。
5. 誘導場の相関関数から $U(3)$ 等方な殻接方向生成子を導き、$\varepsilon_{\rm aniso}$ と混合時間を評価する。
6. 常時の弱い漏れと流入から、狭い総作用殻の定常幅とエネルギー収支を導く。
7. 設定、到来変数、装置微視状態から結果を形成する一般測定 Hamiltonian を構成する。
8. 境界適合、記録、消去、再初期化を1周期の明示モデルへ統合し、事後選別がないことを示す。
9. 偏った準備でも非信号性が回復する条件を判定する。
10. 微視的時間発展による Nelson 停留点選択を示す。
11. Born 則、Tsirelson 限界、Wallstrom 量子化へ進む追加構造を特定する。

## 最終結論

第I部では、粒子と構造化誘導場を含む全 Liouville 方程式から、連続の式と運動量収支を厳密に得た。線形誘導場は指定境界条件の下で Green 作用素により厳密に消去できる。二側 Markov 拡散を仮定した後の浸透速度と Fisher 応力も厳密に整理できる。

しかし、ミクロ反作用と運動量流束が Fisher 応力へ収束することは未証明である。補助的な線形 Gauss 型作用の $C^1$ 定理と Gauss 幅の Routh–Fisher 一致は整合性検査であり、この閉鎖を一般に証明しない。

第II部では、同じ物理構成を2粒子と測定器へ拡張し、1つの構造化誘導場を局所反応座標セクターと共通境界セクターへ静的に分けた。共通境界3モードの $U(3)$ 等方拡散は、縮約方程式の下で共通作用殻の一意な定常測度を与える。その作用殻を $J_+=I_+^{AB}$ で切ると、残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となり、対称セクターでは Bell 型余弦共同確率が厳密に従う。

Bell 固有の終端関数、中央比較器、相補時計は現行モデルから除いた。しかし、共通未来の境界適合と全殻測度は残る。現在の前進は、Fisher 側と Bell 側を同じ構造化誘導場、固定射影、二側条件付け、弱い外部交換の下へ置き、未完成の縮約を Fisher 閉鎖と全殻準備へ絞ったことである。

# 付録

# 線形 Fourier–Gauss 型補助表示と Schur 補完

> **位置づけ：** 二側拡散が得られた後の制御された補助検証として、有限モード表示、有限分解能条件づけ、共分散収束を厳密に補足する。現行誘導場からの縮約ではない。


## 補助表示の定義

時間区間を $[0,T]$、$\omega_n=2\pi n/T$ とする。独立な標準 Gauss 型ベクトル $Z_0,A_n,B_n\in\mathbb R^d$ を用いて

```math
\widetilde\eta_N(t)
=
\sqrt{\frac{2\nu}{T}}Z_0
+
\sqrt{\frac{4\nu}{T}}
\sum_{n=1}^{N}
\left[
A_n\cos\omega_nt
+
B_n\sin\omega_nt
\right]
```

と定義する。この有限過程は調和正規モードの初期振幅の線形読出しとして実現できる。共分散は

```math
\mathbb E
\left[
\widetilde\eta_N^i(t)
\widetilde\eta_N^j(s)
\right]
=
2\nu\delta^{ij}\delta_{T,N}(t-s),
```

```math
\delta_{T,N}(\tau)
=
\frac1T
+
\frac2T
\sum_{n=1}^{N}\cos\omega_n\tau.
```

証明対象の線形 Gauss 型経路法則を

```math
\dot X_N(t)
=
F_\theta(t)X_N(t)
+
f_\theta(t)
+
\widetilde\eta_N(t),
\qquad
X_N(0)
\sim
N(m_{0,\theta},P_{0,\theta})
```

とする。基本行列を

```math
\partial_t\Phi_\theta(t,s)
=
F_\theta(t)\Phi_\theta(t,s),
\qquad
\Phi_\theta(s,s)=I
```

で定めれば、

```math
X_N(t)
=
\Phi_\theta(t,0)X_N(0)
+
\int_0^t
\Phi_\theta(t,s)
\left[
f_\theta(s)
+
\widetilde\eta_N(s)
\right]
\,\mathrm ds.
```

終端記録を

```math
Y
=
H_\theta X_N(T)
+
\epsilon,
\qquad
\epsilon\sim N(0,R_\theta),
\qquad
R_\theta\geq r_*I>0
```

とする。記録値 $Y=y_\theta$ で条件づける。

無条件平均と共分散を $\mu_N,C_N$ とし、

```math
S_N
=
H_\theta C_N(T,T)H_\theta^{\mathsf T}
+
R_\theta
```

と置く。Gauss 型 Schur 補完により、条件付き平均と共分散は

```math
\mu_N^R(t)
=
\mu_N(t)
+
C_N(t,T)H_\theta^{\mathsf T}S_N^{-1}
\left[
y_\theta-H_\theta\mu_N(T)
\right],
```

```math
C_N^R(s,t)
=
C_N(s,t)
-
C_N(s,T)H_\theta^{\mathsf T}S_N^{-1}
H_\theta C_N(T,t)
```

である。

極限の線形拡散は

```math
\mathrm dX_t
=
\left[
F_\theta(t)X_t
+
f_\theta(t)
\right]\mathrm dt
+
\sqrt{2\nu}\,\mathrm dW_t
```

である。終端尤度を $h_R(x,t)$ とすると、条件付き前進流れは

```math
b_+^R(x,t)
=
F_\theta(t)x
+
f_\theta(t)
+
2\nu\nabla\log h_R(x,t).
```

この付録の有限 Fourier 表示は、第2章の現行誘導場 Hamiltonian から一般に導出したものではない。二側拡散の作用形式と有限切断誤差を検査する補助モデルである。

## 基本核の Fourier 係数

線形方程式の雑音応答核を

```math
G_\theta(t,s)
=
\mathbf 1_{0\leq s\leq t}
\Phi_\theta(t,s)
```

とする。$s=t$ に跳びがあるため、$s$ に関する Fourier 係数は一般に $O(n^{-1})$ である。

<!-- theorem-start:lemma -->
**補題（一様 Fourier 尾部）**
$F_\theta$ が第4.8節の仮定を満たすなら、ある $C_K$ が存在して

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|},
```

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|D_\theta\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|}
```

が成立する。従って共分散尾部は

```math
\sup_{\theta,s,t}
\left(
\|C_N(s,t)-C(s,t)\|
+\|D_\theta C_N(s,t)-D_\theta C(s,t)\|
\right)
\leq
\frac{C_KT^2}{N}
```

である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明**
$n\neq0$ に対して $e^{-i\omega_ns}$ を部分積分する。区間端と $s=t$ の跳びから $1/\omega_n$ の境界項が生じ、区間内部では $\partial_s\Phi(t,s)=-\Phi(t,s)F(s)$ が一様有界である。従って $|\widehat G_n|\leq C/|\omega_n|$ を得る。

$\theta$ 微分については

```math
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\,\mathrm{d} r
```

を使う。$D\Phi$ とその $s$ 微分も一様有界なので同じ部分積分評価が成立する。共分散は Fourier 係数の積の和であり、

```math
\sum_{|n|>N}\frac1{n^2}\leq\frac{C}{N}
```

から結論を得る。
<!-- theorem-end:proof -->

## 平均の収束

本論文では $F_\theta$、$f_\theta$、初期平均は $N$ に依存しないため、無条件平均は $\mu_N=\mu$ である。浴切断に依存する補正平均を許す場合でも、Fourier 尾部が中心化されていれば平均差は零であり、非零の決定論的尾部を加えた場合はその $L^1$ ノルムで直接評価できる。

条件付き平均は $C_N(t,T)$ と $C_N(T,T)$ に依存するため、共分散尾部から $O(1/N)$ の差を持つ。

## Schur 補完の安定性

$S_N=HC_N(T,T)H^{\mathsf T}+R$、$S=HC(T,T)H^{\mathsf T}+R$ とする。$R\geq r_*I$ なので

```math
\|S_N^{-1}\|\leq r_*^{-1},
\qquad
\|S^{-1}\|\leq r_*^{-1}.
```

逆行列恒等式

```math
S_N^{-1}-S^{-1}
=
S_N^{-1}(S-S_N)S^{-1}
```

から

```math
\|S_N^{-1}-S^{-1}\|
\leq
r_*^{-2}\|S_N-S\|
```

を得る。従って条件付き共分散について

```math
\sup_{s,t,\theta}
\|C_N^R(s,t)-C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

である。

第1微分では

```math
D(S^{-1})=-S^{-1}(DS)S^{-1}
```

を用いる。$S_N^{-1}$、$DS_N$ が一様有界なので、積の各因子を1つずつ差し替えることで

```math
\sup_{s,t,\theta}
\|D C_N^R(s,t)-D C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

を得る。条件付き平均も同様である。

## 有限分解能の役割

$R>0$ は、観測値 $y$ の周囲に有限幅の終端領域を持たせる。これにより、条件付き共分散は $T$ で完全には消えず、条件付き流れの係数は閉区間 $[0,T]$ 上で有界に保たれる。

$R\downarrow0$ とすると、完全観測された方向の終端共分散は零へ近づく。自由拡散では前進条件付き流れに

```math
\frac{y-x}{T-t}
```

型の項が現れる。点終端での定理を得るには、$t=T$ の境界層を除いた区間で先に $N\to\infty$、$h\to0$ を取り、その後に境界層と $R\downarrow0$ を別に評価する必要がある。

## 自由終端固定と零周波数

自由系では

```math
X_N(T)-X_N(0)
=
\int_0^T\widetilde\eta_N(t)\,\mathrm{d} t
=
\sqrt{2\nu T}\,Z_0.
```

従って $X_N(T)=X_N(0)$ は $Z_0=0$ と同値である。非零モードは終端条件と独立なので、条件付き共分散から零モードの寄与 $2\nu/T$ だけが除かれる。この計算は、旧来の $-1/T$ が浴の基本性質ではなく、自由終端固定の結果であることを最も直接に示す。

## 一般線形系では全モードが条件づけられる

$F\neq0$ では

```math
X_N(T)
=
\Phi(T,0)X_N(0)
+\sum_\alpha K_{N,\alpha}(T)\zeta_\alpha
+d_N(T)
```

である。ここで $d_N(T)$ は決定論項であり、一般に $K_{N,\alpha}(T)\neq0$ である。終端記録は零周波数だけでなく全ての Fourier 係数の線形結合を拘束する。そのため条件付き雑音共分散の修正は階数有限の Schur 項となり、流れ $F$、観測 $H$、分解能 $R$ に依存する。

# 粗視化作用の <i>C</i><sup>1</sup> 評価

> **位置づけ：** 補助的な線形 Gauss 型表示について、時間粗視化誤差と Fourier 切断誤差を分離し、厳密な主定理を補足する。


## 作用とパラメータ族

コンパクトな有限次元パラメータ集合を $K$ とする。$F_\theta,f_\theta,m_{0,\theta},P_{0,\theta},H_\theta,y_\theta,R_\theta$ は $\theta\in K$ について $C^2$ で一様有界、$P_{0,\theta}\geq p_*I>0$、$R_\theta\geq r_*I>0$ とする。外部ポテンシャルは

```math
U_\theta(x,t)
=
\frac12x^{\mathsf T}K_\theta(t)x
+
\ell_\theta(t)^{\mathsf T}x
+
c_\theta(t)
```

とする。

有限分解能で条件づけた付録Aの経路法則に対し、繰り込み済み粗視化作用を

```math
\mathcal A_{N,h}^{R,U}(\theta)
=
\mathbb E_{N,\theta}^{R}
\int_0^{T-h}
\left[
\frac m{2h^2}
|X_N(t+h)-X_N(t)|^2
-
\frac{md\nu}{h}
-
U_\theta(X_N(t),t)
\right]
\,\mathrm dt
```

と定義する。極限の Guerra--Morato 作用を

```math
\mathcal A_{\rm GM}^{R,U}(\theta)
=
\int_0^T\int_{\mathbb R^d}
\rho_\theta^R
\left[
\frac m2|b_{+,\theta}^R|^2
+
m\nu\nabla\cdot b_{+,\theta}^R
-
U_\theta
\right]
\,\mathrm dx\,\mathrm dt
```

とする。$C^1(K)$ は作用値と $\theta$ に関する全ての第1偏微分の一様ノルムを表す。

## Gauss 型増分の正確な表示

条件付き Gauss 型過程の増分 $\Delta_hX(t)=X(t+h)-X(t)$ に対して

```math
\mathbb{E}^R|\Delta_hX(t)|^2
=
|\mu^R(t+h)-\mu^R(t)|^2
+\operatorname{tr}\left[
C^R(t+h,t+h)+C^R(t,t)-2C^R(t+h,t)
\right]
```

が厳密に成立する。従って粗視化作用の運動項は、条件付き平均と共分散だけで計算できる。

有限 $N$ でも同じ式が成立する。$C_N^R-C^R=O(1/N)$ なので、増分2乗の有限モード誤差は粗い評価で $O(1/N)$、$h^{-2}$ を掛けた作用誤差は $O(1/(Nh^2))$ となる。

## 時間対角の展開

極限拡散について、$X_t=x$ を固定した短時間増分は

```math
\Delta_hX
=
b_+^R(x,t)h
+\sqrt{2\nu}\Delta_hW
+O_{L^2}(h^{3/2})
```

である。流れの空間依存と雑音の相関による交差項まで含めて平均すると

```math
\mathbb{E}^R
\left[
|\Delta_hX|^2\mid X_t=x
\right]
=
2d\nu h
+h^2
\left[
|b_+^R(x,t)|^2
+2\nu\nabla\cdot b_+^R(x,t)
\right]
+O(h^3).
```

線形流れでは3階剰余を平均・微分した量も一様に有界である。$m/(2h^2)$ を掛けると

```math
\frac m{2h^2}\mathbb{E}^R|\Delta_hX|^2
-\frac{md\nu}{h}
=
\mathbb{E}^R
\left[
\frac m2|b_+^R|^2
+m\nu\nabla\cdot b_+^R
\right]
+O(h).
```

積分上端を $T-h$ で止めたことによる欠落も $O(h)$ である。

## なぜ発散項が残るか

雑音の主要項 $2d\nu h$ だけを差し引いても、流れと短時間雑音の交差効果は $h^2$ の有限項として残る。それが

```math
m\nu\nabla\cdot b_+^R
```

である。この項を落とすと、極限は正しい Guerra--Morato 作用にならず、Nelson 表示の負の Fisher 項も得られない。

## Fourier 切断誤差

付録Aの評価から

```math
\|C_N^R-C^R\|_{C^1(K;C([0,T]^2))}
\leq
\frac{C_KT^2}{N}
```

である。増分共分散は4つの共分散値の線形結合なので、

```math
\left|
\mathbb{E}_N^R|\Delta_hX_N|^2
-
\mathbb{E}^R|\Delta_hX|^2
\right|_{C^1(K)}
\leq
\frac{C_KT^2}{N}.
```

従って運動項の差は

```math
\frac{C_KT^2}{Nh^2}
```

で抑えられる。この評価は最適とは限らないが、$N(h/T)^2\to\infty$ という単純な対角極限を与える。

## 2次ポテンシャル

$U(x,t)=x^{\mathsf T}K(t)x/2+\ell(t)^{\mathsf T}x+c(t)$ なら

```math
\mathbb{E}^R[U(X_t,t)]
=
\frac12\mu^R(t)^{\mathsf T}K(t)\mu^R(t)
+\frac12\operatorname{tr}[K(t)C^R(t,t)]
+\ell(t)^{\mathsf T}\mu^R(t)
+c(t).
```

従ってポテンシャル期待値とそのパラメータ第1微分は、$\mu_N^R$ と $C_N^R$ の $O(1/N)$ 収束から直接従う。これは運動項の $O(1/(Nh^2))$ より小さく、主定理の右辺へ吸収できる。

一般の滑らかな非2次ポテンシャルでは、Gauss 型モーメント展開または一様可積分性を用いて同様の結果を拡張できる可能性がある。しかし第1微分には解写像の応答と $\nabla U$ の積が現れるため、本論文では証明が閉じる2次範囲に限定する。

## パラメータ第1微分

作用を $\theta_j$ で微分すると、平均、共分散、条件付き Schur 項、ポテンシャル係数の微分が現れる。基本行列の微分公式と $R\geq r_*I$ により、全ての係数は $K$ 上で一様有界である。

時間対角展開を微分した剰余も $O(h)$、Fourier 尾部を微分した誤差も $O(T^2/(Nh^2))$ である。有限個の $\theta_j$ について最大を取れば

```math
\|\mathcal A_{N,h}^{R,U}-\mathcal A_{\mathrm{GM}}^{R,U}\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+\frac{T^2}{Nh^2}
\right)
```

を得る。

## 対角尺度の選択

$h/T=N^{-\alpha}$ と置くと、2つの誤差は

```math
N^{-\alpha},
\qquad
N^{2\alpha-1}
```

である。両者を同じ次数にするには $\alpha=1/3$ とすればよい。従って

```math
h_N=TN^{-1/3},
\qquad
\varepsilon_N=O(N^{-1/3})
```

となる。ここで $\varepsilon_N$ は全評価誤差を表す。

この選択は、粗視化窓を短くしすぎると未解像の Fourier 尾部が増幅され、長くしすぎると局所 Nelson 作用から外れる、という物理的な釣り合いを表す。

# 構造化誘導場、U(3) 殻拡散、境界ファイバー体積

> **位置づけ：** 第2章と共通の固定射影を持つ誘導場について、静的基底、和・差変換、作用保存、固定殻体積、coarea 計算を補足する。誘導場から等方拡散への縮約は候補構成であり、未完成である。


## 拡大全系とエネルギー収支

第II部の拡大全系を

```math
H_{\rm all}
=
H_{\rm src}
+
H_{\rm set}
+
H_{\rm loc}
+
H_{\rm ptr}
+
H_{\rm med}
+
H_\partial
+
H_{\rm fin-link}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

と書く。各項の役割は次である。

| 項 | 役割 |
|---|---|
| $H_{\rm src}$ | 固定総入力作用と位相基準を持つ伝達ベクトル対の準備 |
| $H_{\rm set}$ | 左右の設定制御器 |
| $H_{\rm loc}$ | 局所結果形成または最小結果符号化 |
| $H_{\rm ptr}$ | 固定指針への記録 |
| $H_{\rm med}$ | 左右局所反応座標、共通境界反応座標、暗モードを含む1つの構造化誘導場 |
| $H_\partial$ | 境界3モードの自由運動と弱い混合 |
| $H_{\rm fin-link}$ | 有限装置部分内の結合 |
| $H_{\rm ext}$ | 外部環境 |
| $\varepsilon_{\rm ext}H_{\rm link}$ | 常時のごく弱い漏れと流入 |
| $H_{\rm work}$ | 設定変更、記録消去、再初期化の仕事源 |

全 Hamiltonian に明示的な時間依存性がなければ、拡大全エネルギーは保存される。一方、有限装置部分

```math
H_{\rm fin}
=
H_{\rm all}
-
H_{\rm ext}
-
H_{\rm work}
```

の収支は

```math
\frac{dH_{\rm fin}}{dt}
=
\left\{
H_{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
\right\}.
```

実験室の記号では、

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}.
```

閉鎖補助モデルは $\varepsilon_{\rm ext}=0$ とし、仕事源を有限装置へ含めた短時間窓で用いる。現行モデルでは $\varepsilon_{\rm ext}$ を常時零にせず、測定窓内の相対エネルギー変化を小さい量として評価する。

## 静的誘導場基底の正準性

浴座標を $Q,P\in\mathbb R^N$ とし、

```math
H_{\rm med}
=
\frac12P^{\mathsf T}P
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

とする。$K$ は正定値実対称行列である。

局所装置と境界装置が浴へ結合する方向を

```math
c_A,
\quad
c_B,
\quad
c_{\partial,1},
\ldots,
c_{\partial,m}
```

とする。その張る部分空間の正規直交基底を先頭に並べる直交行列 $O$ を固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde P=OP
```

と変換する。

<!-- theorem-start:proposition -->
**命題（直交浴基底変換の正準性）**
$O^{\mathsf T}O=I$ なら、$(Q,P)\mapsto(\widetilde Q,\widetilde P)$ は正準変換である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
正準1形式は

```math
P^{\mathsf T}dQ
=
\widetilde P^{\mathsf T}
O
O^{\mathsf T}
d\widetilde Q
=
\widetilde P^{\mathsf T}d\widetilde Q
```

と保存される。従ってシンプレクティック2形式も保存される。
<!-- theorem-end:proof -->

変換後の2次形式は

```math
H_{\rm med}^{(2)}
=
\frac12\widetilde P^{\mathsf T}\widetilde P
+
\frac12
\widetilde Q^{\mathsf T}
\widetilde K
\widetilde Q,
\qquad
\widetilde K
=
OKO^{\mathsf T}.
```

結合ベクトルに適合した基底を取っても、$\widetilde K$ は一般にブロック対角ではない。局所、境界、暗モード間の動的結合は $\widetilde K$ の非対角ブロックと $V_{\rm nl}$ に残る。

従って、

```math
H_{\rm med}
=
H_A^{\rm loc}
+
H_B^{\rm loc}
+
H_\partial^{\rm glob}
+
H^{\rm dark}
+
H_{\rm cross}
```

という分解は、正準座標の厳密な分類と、動力学的な近似直和を分けて読む必要がある。

## 線形応答核

線形誘導場の運動方程式は

```math
\ddot Q+KQ
=
-\epsilon_Ac_Ax_A
-\epsilon_Bc_Bx_B
-\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

ここで $F_\alpha$ は境界モードから浴へ加わる一般化力である。初期値解は

```math
Q(t)
=
\cos
\left(
K^{1/2}t
\right)Q(0)
+
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)P(0)
```

```math
\quad
-
\int_0^t
K^{-1/2}
\sin
\left[
K^{1/2}(t-s)
\right]
F_{\rm dev}(s)\,ds,
```

```math
F_{\rm dev}
=
\epsilon_Ac_Ax_A
+
\epsilon_Bc_Bx_B
+
\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

A側の一般化力 $c_A^{\mathsf T}Q(t)$ にB側の $x_B$ が与える寄与は

```math
-\epsilon_B
\int_0^t
\chi_{AB}(t-s)x_B(s)\,ds,
```

```math
\chi_{AB}(t)
=
c_A^{\mathsf T}
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)
c_B.
```

同様に $\chi_{BA}$ を得る。従って、$c_A^{\mathsf T}c_B=0$ でも $\chi_{AB}(t)$ は一般に零ではない。$K$ が $c_A,c_B$ の張る部分空間を別々に不変にするときだけ、線形交差応答は厳密に消える。

局所測定窓 $0\leq t\leq T_{\rm meas}$ で

```math
\varepsilon_{\rm loc}
=
\frac{
\sup_t
\max
\left(
|\chi_{AB}(t)|,
|\chi_{BA}(t)|
\right)
}{
\sup_t
\min
\left(
|\chi_{AA}(t)|,
|\chi_{BB}(t)|
\right)
}
```

を用いる理由はここにある。非線形補正については、指定した準備領域のまわりで変分方程式を解き、同じ比を定義する。

## 局所結果符号化の生成子

結果種座標を $s_X$、伝達ベクトルを $(Q_X,P_X)$、応答モードを $(x_X,p_X)$ とする。平坦結果領域上で $\sigma(s_X)=X\in\{-1,+1\}$ とする。

局所分析の生成子を

```math
K_X^{\rm an}
=
-
\left[
\phi(a_X)
+
\pi\chi_-(s_X)
\right]
I_X
-
x_X\sigma(s_X),
```

```math
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
\chi_-(s)
=
\frac{
1-\sigma(s)
}{
2
}
```

とする。生成子の単位流れで、

```math
u_X^{\rm out}
=
X R[\phi(a_X)]u_X^{\rm in},
\qquad
p_X^{\rm out}
=
p_X^{\rm in}+X.
```

$p_X^{\rm in}=0$ なら $p_X^{\rm out}=X$ である。

固定指針対を $(Y_X,\Pi_X)$ とし、平坦関数 $\zeta(p_X)$ が $p_X=\pm1$ の近傍で $\pm1$ を取るとする。転写生成子

```math
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
```

の単位流れは

```math
\Pi_X^{\rm out}
=
\Pi_X^{\rm in}
+
\zeta(p_X).
```

$\Pi_X^{\rm in}=0$ なら $\Pi_X^{\rm out}=X$ となる。

自由 Hamiltonian と幅 $\tau_{\rm pulse}$ のパルスが同時に働く場合、理想単位流れとの差は、有界な適用領域で

```math
O(\varepsilon_{\rm pulse}),
\qquad
\varepsilon_{\rm pulse}
=
\tau_{\rm pulse}
\sup_{\mathcal K}
\left\|
X_{H_0}
\right\|
```

と評価する。局所誘導場の交差応答も加えると、指針の誤差は

```math
O
\left(
\varepsilon_{\rm pulse}
+
\varepsilon_{\rm loc}
+
\varepsilon_{\rm open}
\right).
```

この補助装置は既存の結果種を記録するだけであり、一般測定器ではない。

## 和・差基底の正準性

左右伝達ベクトルを正準対 $(Q_A,P_A)$、$(Q_B,P_B)$ とする。和・差座標を

```math
Q_\pm
=
\frac{
Q_A\pm Q_B
}{
\sqrt2
},
\qquad
P_\pm
=
\frac{
P_A\pm P_B
}{
\sqrt2
}
```

と定める。

<!-- theorem-start:proposition -->
**命題（和・差変換の正準性）**
上の変換は正準であり、

```math
P_A\,dQ_A
+
P_B\,dQ_B
=
P_+\,dQ_+
+
P_-\,dQ_-.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
変換行列

```math
U
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
```

は直交行列である。座標と運動量へ同じ $U$ を作用させるため、C.1節と同じ計算で正準1形式が保存される。
<!-- theorem-end:proof -->

和・差作用は

```math
I_\pm
=
\frac12
\left(
Q_\pm^2+P_\pm^2
\right)
=
\frac14
\left\|
u_A\pm u_B
\right\|^2.
```

直交性から、

```math
I_++I_-
=
I_A+I_B.
```

設定と結果は $I_+-I_-$ に入るが、総入力作用には入らない。

固定された $U$ は1つの正準写像であり、測度を生成しない。入力集団が Liouville 測度を持てば保存するが、単一入力を一様集団へ変えない。

## 3モード作用と U(3) 生成子

境界3モードを複素正準変数

```math
a
=
\begin{pmatrix}
a_+\\
a_s\\
a_r
\end{pmatrix},
\qquad
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
}
```

で表す。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とする。総作用は

```math
C
=
a^\dagger a.
```

$T_\alpha$ を $u(3)$ の Hermitian 基底とし、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を Hamiltonian 生成子とする。$L_\alpha$ の流れは

```math
\dot a
=
-iT_\alpha a
```

であり、

```math
\left\{
C,L_\alpha
\right\}
=
0.
```

従って全ての $U(3)$ 生成子は総作用殻に接する。

構造化誘導場の未読変数 $\xi_\alpha(z_{\mathcal B})$ と弱く結合する候補 Hamiltonian を

```math
H_{\rm iso-link}
=
\epsilon_{\rm iso}
\sum_{\alpha=1}^{9}
\xi_\alpha(z_{\mathcal B})
L_\alpha(a)
```

とする。各瞬間の全 Hamiltonian 流れは $C$ を保存する。

浴相関が準備窓で

```math
\left\langle
\xi_\alpha(t)
\xi_\beta(0)
\right\rangle
\simeq
\delta_{\alpha\beta}
\kappa(t)
```

となり、相関時間が境界モードの緩和時間より短いとする。弱結合・長時間尺度での2次縮約生成子は概念的に

```math
\mathcal L_{\rm eff}
=
D_\partial
\sum_{\alpha=1}^{9}
X_{L_\alpha}^2
```

となる。同次空間 $U(3)/U(2)$ 上では、この Casimir 作用素は規格化を除いて $\Delta_{S^5}$ に一致する。

この縮約には、少なくとも次の近似が必要である。

1. $\epsilon_{\rm iso}\ll1$ の弱結合。
2. 浴相関時間と準備時間の分離。
3. 9方向の相関行列の等方性。
4. 有限誘導場の再帰時間より短い準備窓。
5. 外部交換による長時間再位相化の抑制。

本論文は、特定の有限 $V_{\rm nl}$ と外部結合について、これらの条件から $\mathcal L_{\rm eff}$ への一様誤差上界を証明しない。従ってこれはミクロ実現候補であり、導出済みの定理ではない。

## 等方拡散の定常測度

固定殻 $S_{C_0}^5$ 上の密度 $f$ が

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

に従うとする。定常解は

```math
\Delta_{S^5}f=0
```

を満たす。部分積分により、

```math
0
=
\int
f\Delta_{S^5}f\,d\mu_{C_0}
=
-
\int
\left|
\nabla_{S^5}f
\right|^2
d\mu_{C_0}.
```

従って $f$ は定数であり、規格化すれば $f=1$ である。

異方摂動を

```math
\mathcal L_\varepsilon
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_1
```

とする。$\mathcal L_1$ が質量を保存し、等方生成子のスペクトルギャップに対して相対有界なら、定常密度の形式展開は

```math
f_\varepsilon
=
1
-
\frac{
\varepsilon_{\rm aniso}
}{
D_\partial
}
\left(
\Delta_{S^5}
\right)^{-1}_{0}
\mathcal L_1^*1
+
O
\left(
\varepsilon_{\rm aniso}^2
\right)
```

となる。逆作用素の添字0は平均零部分空間への制限である。この式は、異方性の影響が結合定数だけでなくスペクトルギャップに依存することを示す。

## 固定殻体積と周辺密度

作用角変数で、3モード固定殻の未規格化体積は

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^\infty dJ_+
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-J_+-J_s-J_r
\right).
```

$J_r$ を積分すると、$J_+,J_s\geq0$ かつ $J_++J_s\leq C_0$ の三角形が残る。従って、

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^{C_0}dJ_+
\int_0^{C_0-J_+}dJ_s
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

$J_+=x$ の未規格化周辺は

```math
\omega_+(x)
=
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
```

```math
=
(2\pi)^3
\left(
C_0-x
\right)
\mathbf1_{\{0\leq x\leq C_0\}}.
```

従って、

```math
p_+(x)
=
\frac{
\omega_+(x)
}{
\Omega_3(C_0)
}
=
\frac{
2(C_0-x)
}{
C_0^2
}.
```

固定 $x$ の条件付き分布では、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac1{C_0-x}
```

である。条件付き密度の $1/(C_0-x)$ と、ファイバー総質量の $C_0-x$ を混同してはならない。

## coarea と境界ファイバー

一般の境界正準位相空間を $\Gamma_\partial$、基準体積を $d\Gamma_\partial$ とする。2つの制約を

```math
F_1
=
C_0-J_+-J_s-J_r,
```

```math
F_2
=
J_+-I_+^{AB}
```

とする。理想線形モデルでは、

```math
W_{AB}
\propto
\int_{\Gamma_\partial}
\delta(F_1)
\delta(F_2)
d\Gamma_\partial.
```

作用角座標に変換すると、変換 Jacobian は1である。$J_+$ と $J_r$ のデルタ関数積分を行えば、

```math
W_{AB}
\propto
(2\pi)^3
\int_0^{C_0-I_+^{AB}}dJ_s
```

```math
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right).
```

一般の滑らかな境界写像 $F=(F_1,F_2)$ では coarea 公式により、

```math
\int_{\Gamma_\partial}
\rho(z)
\delta
\left(
F(z)
\right)
d\Gamma_\partial
=
\int_{F^{-1}(0)}
\frac{
\rho(z)
}{
J_F(z)
}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

理想作用座標では $J_F$ が結果と設定に共通な定数へなる。非線形境界写像、分岐、caustic、解多重度がある場合は、この単純化を使えない。同じ巨視的結果へ対応する複数の解は、その局所 Jacobian と多重度を含めて数える。

## 有限分解能の展開

偶関数 $K$ を

```math
\int_{\mathbb R}K(y)\,dy=1,
\qquad
\int_{\mathbb R}yK(y)\,dy=0
```

と規格化し、

```math
K_{\delta_J}(y)
=
\frac1{\delta_J}
K
\left(
\frac y{\delta_J}
\right)
```

とする。$J_+$ 周辺密度 $p_+(x)$ は殻内部で線形なので、窓が殻端に触れない限り、

```math
\int
p_+(x)
K_{\delta_J}(x-I_+)\,dx
=
p_+(I_+)
```

が偶対称窓では厳密に成り立つ。一般の滑らかな Jacobian または殻幅分布を含めると、

```math
W_{AB}^{(\delta_J)}
=
c_{\delta_J}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
\delta_J^2
\sup
\left|
\partial_{J_+}^2
\frac{\rho}{J_F}
\right|
\right).
```

従って、理想線形作用殻では有限分解能自体が1次の角度誤差を生まない。主要な分解能誤差は、殻端の切断、非線形 Jacobian、結果依存窓、総作用幅との重なりから生じる。

## 半径方向の弱開放力学

総作用 $C$ の縮約式を

```math
dC_t
=
-\gamma_C
\left(
C_t-C_0
\right)dt
+
\sqrt{2D_C}\,dW_t
```

とする。定常密度は

```math
\rho_C(C)
\propto
\exp
\left[
-
\frac{
\gamma_C
}{
2D_C
}
\left(
C-C_0
\right)^2
\right],
```

その分散は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C}
```

である。

この式は、外部への漏れと流入を線形化した縮約候補である。基礎 Hamiltonian の総エネルギーが確率的に失われると仮定したものではない。外部環境と仕事源を消去した有限部分の有効式として読む。

角方向と半径方向が近似的に分離する条件を

```math
\tau_{\rm corr}
\ll
\tau_{\rm mix}
\ll
\tau_C,
\qquad
\tau_C=\gamma_C^{-1}
```

とする。$\tau_{\rm corr}$ は浴相関時間、$\tau_{\rm mix}$ は殻接方向混合、$\tau_C$ は半径変化である。$\tau_{\rm mix}\ll\tau_C$ なら、各半径で方向分布が先に等方化する。

純粋漏れでは

```math
dC_t=-\gamma_CC_t\,dt
```

となり、非零の定常殻は存在しない。流入または仕事源を含む復元項は、作用殻準備に不可欠である。

## ミクロ構成から未導出の事項

本付録で厳密に示したのは次である。

- 1つの有限誘導場に対する静的な直交正準基底。
- 線形誘導場の交差応答核。
- 最小結果符号化器の理想正準写像。
- 和・差変換の正準性と作用保存。
- $U(3)$ Hamiltonian 生成子が総作用を保存すること。
- 3モード固定作用殻の体積、周辺密度、残余ファイバー体積。
- 理想線形境界写像の共通 coarea Jacobian。

次は未導出である。

- 特定の有限非線形浴が必要な時間窓で等方な相関行列を持つこと。
- 有限誘導場と常時の外部交換から $D_\partial\Delta_{S^5}$ を一様誤差付きで得ること。
- 異方誤差、混合時間、再帰時間を同じパラメータから同時に閉じること。
- 半径方向の復元式とエネルギー収支を明示的な外部 Hamiltonian から導くこと。
- 一般測定器、境界適合、記録、消去、再初期化を1本の有限幅 Hamiltonian へ統合すること。

従って、作用殻の幾何計算は厳密結果、全殻拡散と半径安定化は縮約候補、現行の弱開放モデルへの接続は近似または予想・未解決として扱う。

# 参考文献


- [1] J. S. Bell, ``On the Einstein Podolsky Rosen Paradox,'' Physics Physique Fizika 1, 195--200 (1964). <https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195>
- [2] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, ``Proposed Experiment to Test Local Hidden-Variable Theories,'' Physical Review Letters 23, 880--884 (1969). <https://doi.org/10.1103/PhysRevLett.23.880>
- [3] E. Nelson, ``Derivation of the Schrödinger Equation from Newtonian Mechanics,'' Physical Review 150, 1079--1085 (1966). <https://doi.org/10.1103/PhysRev.150.1079>
- [4] F. Guerra and L. M. Morato, ``Quantization of Dynamical Systems and Stochastic Control Theory,'' Physical Review D 27, 1774--1786 (1983). <https://doi.org/10.1103/PhysRevD.27.1774>
- [5] K. Yasue, ``Stochastic Calculus of Variations,'' Journal of Functional Analysis 41, 327--340 (1981). <https://doi.org/10.1016/0022-1236(81)90079-3>
- [6] J.-C. Zambrini, ``Stochastic Mechanics According to E. Schrödinger,'' Physical Review A 33, 1532--1548 (1986). <https://doi.org/10.1103/PhysRevA.33.1532>
- [7] K. B. Wharton, ``Time-Symmetric Boundary Conditions and Quantum Foundations,'' Symmetry 2, 272--283 (2010). <https://doi.org/10.3390/sym2010272>
- [8] K. B. Wharton and N. Argaman, ``Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics,'' Reviews of Modern Physics 92, 021002 (2020). <https://doi.org/10.1103/RevModPhys.92.021002>
- [9] M. J. W. Hall, ``Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence,'' Physical Review Letters 105, 250404 (2010). <https://doi.org/10.1103/PhysRevLett.105.250404>
- [10] M. S. Leifer and M. F. Pusey, ``Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?,'' Proceedings of the Royal Society A 473, 20160607 (2017). <https://doi.org/10.1098/rspa.2016.0607>
- [11] C. J. Wood and R. W. Spekkens, ``The Lesson of Causal Discovery Algorithms for Quantum Correlations,'' New Journal of Physics 17, 033002 (2015). <https://doi.org/10.1088/1367-2630/17/3/033002>
- [12] G. W. Ford, M. Kac, and P. Mazur, ``Statistical Mechanics of Assemblies of Coupled Oscillators,'' Journal of Mathematical Physics 6, 504--515 (1965). <https://doi.org/10.1063/1.1704304>
- [13] H. Mori, ``Transport, Collective Motion, and Brownian Motion,'' Progress of Theoretical Physics 33, 423--455 (1965). <https://doi.org/10.1143/PTP.33.423>
- [14] R. Zwanzig, ``Nonlinear Generalized Langevin Equations,'' Journal of Statistical Physics 9, 215--220 (1973). <https://doi.org/10.1007/BF01008729>
- [15] B. Jamison, ``Reciprocal Processes,'' Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 30, 65--86 (1974). <https://doi.org/10.1007/BF00532864>
- [16] J. L. Doob, ``Conditional Brownian Motion and the Boundary Limits of Harmonic Functions,'' Bulletin de la Société Mathématique de France 85, 431--458 (1957). <https://doi.org/10.24033/bsmf.1495>
- [17] R. Landauer, ``Irreversibility and Heat Generation in the Computing Process,'' IBM Journal of Research and Development 5, 183--191 (1961). <https://doi.org/10.1147/rd.53.0183>
- [18] C. H. Bennett, ``The Thermodynamics of Computation: A Review,'' International Journal of Theoretical Physics 21, 905--940 (1982). <https://doi.org/10.1007/BF02084158>
- [19] T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). <https://doi.org/10.1103/PhysRevA.49.1613>
- [20] H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). <https://arxiv.org/abs/2309.10969>
- [21] H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). <https://arxiv.org/abs/2406.04571>
- [22] N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). <https://doi.org/10.1119/1.3456564>
- [23] S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). <https://doi.org/10.3389/fphy.2020.00139>
- [24] G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). <https://doi.org/10.1007/978-3-319-41285-6>
- [25] C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). <https://doi.org/10.3934/dcds.2014.34.1533>
- [26] Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). <https://doi.org/10.1007/s10957-015-0803-z>
- [27] H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). <https://doi.org/10.2514/3.3166>
- [28] J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). <https://doi.org/10.1209/0295-5075/113/60009>
- [29] M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). <https://doi.org/10.1088/1751-8121/ab7cfe>
- [30] J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). <https://doi.org/10.1063/5.0207422>
- [31] J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). <https://jmlr.org/papers/v22/20-1260.html>
- [32] C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). <https://doi.org/10.1214/13-PS220>
- [33] M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). <https://doi.org/10.1103/PhysRevE.83.061112>
