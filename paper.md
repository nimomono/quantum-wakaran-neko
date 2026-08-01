# 概要


本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。中心となる有限部分は、粒子または測定対象、構造化誘導場、測定器、記録器、境界3モードからなる。外部自由度と仕事源まで含む拡大全系を

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

となる。常時の弱い外部交換は、欠陥成分の除去、有限浴の再帰抑制、記録安定化、非零作用半径の維持に使う。Fisher 項や作用殻の方向一様性を外部漏れから直接仮定しない。

現行モデルの共通部分は、時間に依存しない明・暗モード分解を持つ構造化誘導場である。第I部では粒子と誘導場を運動量で結合し、配置速度揺らぎへ縮約する。第II部では同じ誘導場へ装置の座標結合を加え、2粒子、左右測定器、共通境界3モードの履歴測度へ縮約する。2種類の結合は役割が異なる。

第I部の有限 Hamiltonian を

```math
H_N^{\rm fin}
=
\frac12
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I_d & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}
+
V(X)
+
\frac12Q^{\mathsf T}K_NQ
+
H_N^{\rm nl}
```

とする。運動量2次形式の正定値条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。線形核の Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X)
```

を含む。従って誘導場速度

```math
Y_N
=
C_N\Pi
```

は配置流束へ直接入る。正準運動量 $P$ と機械的運動量 $m\dot X$ は一致しない。

質量規格化した線形誘導場を正確に消去すると、

```math
Y_N(t)
=
Y_N^{\rm free}(t)
-
\int_0^t
C_N\Omega_N
\sin
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}P(s)
\,\mathrm ds
```

を得る。第1項は初期場に由来する自由速度揺らぎ、第2項は粒子から場への反作用による速度記憶項である。有限浴の相関は余弦関数の有限和なので、厳密な OU 相関や無限時間の Brown 運動ではない。多数モード、短記憶、弱い外部交換を用い、

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}
```

という再帰前の窓で配置変位の拡散極限を調べる。

最初の有効候補は、配置雑音を持つ位相空間過程

```math
\mathrm dX_t
=
\frac{P_t}{m}
\,\mathrm dt
+
\sqrt{2\nu}
\,\mathrm dW_t,
\qquad
\mathrm dP_t
=
-\nabla V(X_t)
\,\mathrm dt
```

である。ただし $(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。配置変数だけの前進・後退 Markov 拡散と共通拡散係数 $\nu$ を得ることは追加の縮約課題である。

この配置 Markov 拡散が得られた有効モデル内部では、現在速度 $v$ と浸透速度 $u$ は

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

を満たす。従って

```math
\frac m2
\int
\rho|u|^2
\,\mathrm dx
=
\frac{m\nu^2}{2}
\int
\frac{|\nabla\rho|^2}{\rho}
\,\mathrm dx
```

となり、Fisher 項は二側配置拡散の運動学から直接現れる。量子ポテンシャルに対応する項は

```math
Q[\rho]
=
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho},
\qquad
\hbar_{\rm eff}
=
2m\nu
```

である。

ただし、配置拡散だけから時間対称 Newton 則

```math
ma_{\rm ts}
=
-\nabla V
```

は従わない。時間対称 Green 応答、反作用記憶、条件付き変分からこの動力学へ進む部分は独立した未解決問題である。従って旧稿の Fisher 力密度閉鎖は中心課題から外れるが、問題が全て解決したわけではない。

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
\frac hT
+
\frac{T^2}{Nh^2}
\right)
```

を保つ。これは二側配置拡散が得られた後の作用表示を制御する厳密な補助結果であり、ミクロな配置拡散極限や時間対称 Newton 則の証明ではない。

第II部では、同じ構造化誘導場の固定明部分空間が、$\operatorname{Ran}C_N^{\mathsf T}$ に加えて左右の装置結合方向と共通境界結合方向を含む。局所測定窓の左右交差応答には、座標–座標核だけでなく運動量–座標混合核も含め、全応答比 $\varepsilon_{\rm loc}\ll1$ を要求する。

境界3モードの作用を $J_+,J_s,J_r$ とし、共通総作用殻を

```math
J_+
+
J_s
+
J_r
=
C_0
```

とする。縮約された殻接方向混合が非退化な $U(3)$ 等方拡散なら、共通殻上の正規化 Liouville 測度が一意な定常分布になる。この縮約方程式内部の一意性は厳密だが、同じ誘導場からその生成子を導くことは未解決である。

局所記録後の2つの実2次元伝達ベクトルから、固定した和・差基底により

```math
I_+^{AB}
=
I_0
\left[
1
+
ABV\cos\Delta_{ab}
\right],
```

```math
I_-^{AB}
=
I_0
\left[
1
-
ABV\cos\Delta_{ab}
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

履歴測度は、全境界正準位相空間の Liouville 測度を作用保存と境界適合条件で制限し、Hamiltonian の解写像で許容履歴空間へ押し出す。境界適合ファイバーが設定 $a,b$ に依存するため、Bell の前提違反は測定設定独立性にある。対称セクターでは一側周辺が $1/2$ となる。

本論文の前進は、第I部の遠回りな Fisher 力密度閉鎖を、運動量結合から配置拡散へ進む経路へ置き換えたことである。残る中心課題は、有限 Hamiltonian 誘導場からの配置拡散極限、配置 Markov 閉鎖、時間対称動力学と、第II部の全殻準備、一般測定器、事後選別のない試行周期である。

# 問題設定、共通ミクロ構成、2つの縮約経路

> **位置づけ：** 第I部と第II部を1つの構造化誘導場を共有する2つの縮約として整理する。運動量結合による配置拡散と、装置の座標結合による境界作用殻を区別し、同時実現定理は未完成とする。


## 問題設定

本論文の目的は、明示的な古典 Hamiltonian 系から、量子力学に特徴的な確率構造が縮約された有効理論として出現し得るかを検証することである。量子力学を理論構成の入力に使わず、得られた有効式との比較にだけ用いる。

中心問題を次の2つに分ける。

1. 粒子と構造化誘導場を運動量で結合したとき、場の速度揺らぎから配置空間の二側拡散と Fisher 項が生じるか。
2. 同じ構造化誘導場を2粒子、左右測定器、共通境界モードへ拡張したとき、境界作用殻の測度から Bell 型共同確率が生じるか。

第1の問題では、運動量結合した有限浴の正確な消去と、二側配置拡散内部の Fisher 恒等式を示す。両者を結ぶ配置拡散極限、配置変数だけの Markov 性、時間対称 Newton 則は未完成である。

第2の問題では、共通作用殻を仮定した後の体積計算は厳密である。その殻測度、境界適合、事後選別のない試行周期を同じ有限誘導場から準備する部分は未完成である。

## 共通ミクロ構成

有限部分を

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

外部環境、常時の弱い結合、仕事源を加え、

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

構造化誘導場の基底は、時間、設定、結果に応じて切り替えない。運動量結合方向と装置の座標結合方向が張る明部分空間、その直交補空間である暗部分空間を装置の組立時に固定する。位相整合成分と欠陥成分も Hamiltonian の固定スペクトル部分空間または保存作用から定める。

## 2種類の直接結合

同じ誘導場を使うことは、全対象へ同じ型の結合を使うことを意味しない。本論文では次を区別する。

| 結合 | 主な対象 | 役割 |
|---|---|---|
| $P^{\mathsf T}C_N\Pi$ | 第I部の粒子と誘導場 | 配置速度へ $Y_N=C_N\Pi$ を加える |
| $x_Xc_X^{\mathsf T}Q$ | 第II部の局所装置と誘導場 | 局所応答、記録、境界モードへの伝達を作る |

前者は粒子の配置空間拡散へ進む経路、後者は測定器と境界作用殻へ進む経路である。明部分空間は $\operatorname{Ran}C_N^{\mathsf T}$ と全ての装置結合方向 $c_X$ を含む。

運動量–運動量結合と座標–座標結合が同じ誘導場に共存すると、座標–座標応答だけでなく運動量–座標の混合応答も生じ得る。第II部の局所交差応答は、これらを含む全応答作用素について評価する。

## 2つの縮約

第I部の縮約は次の順序で進む。

1. 運動量結合した粒子と構造化誘導場。
2. 誘導場の正確な消去と速度記憶核。
3. 再帰前の配置拡散極限。
4. 配置変数だけの二側 Markov 拡散。
5. Fisher 項と時間対称動力学。

第II部の縮約は次の順序で進む。

1. 2粒子、測定器、構造化誘導場。
2. 局所記録と共通境界3モード。
3. 作用殻準備と境界適合。
4. Bell 型共同確率。

両者は、構造化誘導場、固定射影、二側条件付け、弱い外部交換を共有する。配置空間の拡散係数 $\nu$ と境界作用殻の接方向拡散係数 $D_\partial$ は別の縮約係数である。同じ誘導場から両方が出ることや、同じパラメータ範囲で両方の近似誤差が小さいことは未証明である。

## 現行モデルと補助モデル

| モデル | 運用状態 | 役割と限界 |
|---|---|---|
| 粒子・装置・構造化誘導場・外部流路を持つ弱開放系 | 現行モデル | 2つの縮約の共通ミクロ構成。全周期と一様縮約定理は未完成 |
| 1試行内の有限閉鎖系 | 補助モデル | 正準写像、保存量、Liouville モーメント、作用殻体積を厳密に計算する |
| 運動量結合した線形誘導場 | 補助モデル | 自由速度揺らぎと反作用記憶項を正確に分ける |
| 配置雑音を持つ位相空間拡散 | 補助モデル | 最初の短記憶極限候補を整理する。$X$ 射影の Markov 性は含まない |
| 配置変数の二側 Markov 拡散 | 補助モデル | 前進・後退流れ、Fisher 項、時間対称平均加速度を整理する |
| 線形 Fourier–Gauss 型経路法則 | 補助モデル | 作用形式の $C^1$ 収束を検証する |
| Gauss 幅の Routh 縮約 | 補助モデル | 固定作用と Fisher 項の一致を1つの可解例で検証する |
| 最小結果符号化器 | 補助モデル | 既存の2値符号を固定指針へ写す。一般測定器ではない |
| 3モード固定作用殻 | 補助モデル | 境界適合ファイバーの体積を厳密に計算する |
| $U(3)$ 等方殻拡散 | 補助モデル | 共通作用殻の一意な定常測度を与える |

補助モデル内部の厳密結果を、そのまま弱開放な現行モデルからの厳密導出とは呼ばない。

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
\varepsilon_{\rm open}
\ll
1,
\qquad
T_{\rm meas}
\ll
\tau_{\rm exch}
```

を要求する。外部結合は長時間では欠陥除去、再帰抑制、記録保持、再準備に効くが、測定窓では小さい補正として扱う。

## 可逆誘導、内部混合、外部交換の役割

| 機構 | 主な役割 | それだけでは生じないもの |
|---|---|---|
| 運動量結合した可逆誘導場 | 配置速度揺らぎと反作用記憶 | Brown 極限、$X$ 射影の Markov 性、時間対称 Newton 則 |
| 装置の座標結合 | 局所反応と境界モードへの伝達 | Bell 結果重み、局所性 |
| Hamiltonian な殻接方向混合 | 境界3モードの方向準備 | 非零殻半径の維持 |
| 常時の弱い漏れ・流入・仕事 | 欠陥除去、再帰抑制、記録安定化、半径分布の維持 | Fisher 項、殻方向の一様性 |

純粋な一方向漏れはエネルギーまたは作用を減らすだけで、配置拡散も非零の一様作用殻も作らない。

## Fisher 側の縮約条件

### [H] 運動量結合 Hamiltonian

運動量2次形式を正定値に保ち、

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

を要求する。暗射影については

```math
P_{\rm D}C_N^{\mathsf T}
=
0
```

とする。ここまでの Hamilton 方程式と時間反転対称性は厳密結果である。

### [G] 誘導場の正確な消去

$Y_N=C_N\Pi$ を自由速度揺らぎと反作用記憶項へ分ける。初期値消去と、一意可解な二側境界条件の Green 消去は線形核内部の厳密結果である。

### [D] 配置拡散極限

多数モード、短記憶、再帰前の観測窓で、自由速度揺らぎの積分を Brown 運動へ近づける。反作用記憶、異方性、有限切断、弱開放補正を同時に評価する。この条件は未完成である。

### [X] 配置 Markov 閉鎖

位相空間の有効過程から、配置変数だけの前進・後退 Markov 拡散を得る。前後の2次変分が同じ $\nu$ を持ち、条件付き速度分散が余分な古典圧力を残さない範囲を示す。この条件は未完成である。

### [N] 時間対称動力学

時間対称 Green 応答と条件付き変分から

```math
ma_{\rm ts}
=
-\nabla V
```

を導く。配置拡散が得られただけでは従わない独立の動力学的課題である。

[X] が成立すれば Fisher 項は二側拡散の運動学から厳密に従う。[N] まで成立すれば、局所的な Schrödinger 表示へ進める。

## Bell 側の縮約条件

### [B1] 全交差応答の抑制

同じ誘導場の左右局所反応座標について、座標–座標核だけでなく、運動量–座標混合核を含む測定窓の交差応答比 $\varepsilon_{\rm loc}$ を小さくする。結合ベクトルの直交性だけでは十分でない。

### [B2] 位相同期した生成源

左右へ送る実2次元伝達ベクトル対は固定総入力作用を持ち、和・差作用は

```math
I_+^{AB}
+
I_-^{AB}
=
2I_0
```

を満たす。

### [B3] 対称な結果セクター

境界条件を課す前の基準 Liouville 測度、境界分解能、coarea Jacobian は、左右結果符号の反転で不変とする。

### [B4] 共通作用殻と境界適合

境界3モードは

```math
J_+
+
J_s
+
J_r
=
C_0
```

という1つの作用殻を持ち、全結果に共通の分解能で

```math
J_+
=
I_+^{AB}(a,b)
```

を課す。

### [B5] 全殻等方準備

殻接方向の縮約生成子を $D_\partial\Delta_{S^5}$ で近似する。縮約方程式内部の定常測度は厳密に決まるが、この生成子のミクロ導出は未完成である。

## 試行周期と測度

繰り返し試行を次の6段階に分ける。

1. **欠陥除去と入口準備**：前試行の記録と欠陥成分を除き、粒子、誘導場、装置を指定した入口巨視領域へ戻す。
2. **殻準備**：Bell 側の境界3モードの総作用を狭い分布へ置き、Hamiltonian な殻接方向混合で方向の偏りを緩和する。
3. **生成源と設定準備**：位相基準、伝達ベクトル対、左右設定制御器を準備する。
4. **局所発展と記録**：全交差応答が小さい窓で局所結果を形成し、指針へ記録する。
5. **境界適合**：記録済み伝達ベクトルを共通未来へ運び、共通作用殻の境界条件に適合する完結履歴を定める。
6. **消去と再初期化**：記録、局所反応座標、境界モードを次の試行へ戻し、必要な仕事と排熱を外部へ移す。

履歴確率は、解集合へ直接置いた Liouville 測度ではない。全境界正準位相空間の Liouville 測度を、保存作用、入口巨視領域、境界適合条件で条件づけ、Hamiltonian の解写像で許容履歴空間へ押し出す。

境界適合しない履歴を実験後に捨てる事後選別と、初めから2境界値問題として定義した履歴集団は数学的に異なる。ただし、後者を開始数と記録数を減らさない装置周期として実現することは未解決である。

## 本章の結論

第I部は運動量結合から配置拡散へ、第II部は装置の座標結合から境界作用殻へ進む。2つの結合型は同じ構造化誘導場と固定明・暗基底の中で共存するが、役割を混同しない。

第I部では旧稿の Fisher 力密度閉鎖を外し、配置拡散極限、$X$ 射影の Markov 性、時間対称 Newton 則を独立した未解決問題とする。第II部では作用殻体積の厳密計算を維持し、全殻準備、全交差応答、一般測定器、試行周期を未解決として残す。

# 第I部　運動量結合した構造化誘導場の配置拡散縮約

# 運動量結合した粒子、構造化誘導場、外部流路

> **位置づけ：** 粒子と有限誘導場の運動量2次形式、正定値条件、時間反転対称性、Hamilton 方程式は厳密結果である。配置速度揺らぎの短記憶極限と選択的な欠陥減衰は近似候補である。


## 運動量結合した有限誘導場

粒子座標を $X\in\mathbb R^d$、その正準運動量を $P\in\mathbb R^d$ とする。有限誘導場は $M_N$ 個の実正準対

```math
(Q,\Pi)
\in
\mathbb R^{M_N}\times\mathbb R^{M_N}
```

で表す。$M_N=M_N^{\mathsf T}>0$ を場の質量行列、$K_N=K_N^{\mathsf T}>0$ を場の剛性行列、$C_N\in\mathbb R^{d\times M_N}$ を固定した運動量結合行列とする。有限部分の中心 Hamiltonian を

```math
H_N^{\rm fin}
=
\frac12
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I_d & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}
+
V(X)
+
\frac12Q^{\mathsf T}K_NQ
+
H_N^{\rm nl}
```

とする。$H_N^{\rm nl}$ は必要に応じて加える弱い内部非線形項である。中心変更は、粒子と場の直接結合を座標の積でなく

```math
P^{\mathsf T}C_N\Pi
```

という運動量の積にしたことである。これにより、場は粒子へ直接の乱雑力を加えるのでなく、粒子の配置速度へ直接入る。

## 正定値条件

運動量2次形式が下に有界である条件を明示する。粒子側のブロック $m^{-1}I_d$ は正定値なので、Schur 補完により必要十分条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。同じことは平方完成

```math
\frac{|P|^2}{2m}
+
P^{\mathsf T}C_N\Pi
+
\frac12\Pi^{\mathsf T}M_N^{-1}\Pi
=
\frac1{2m}
\left|P+mC_N\Pi\right|^2
+
\frac12\Pi^{\mathsf T}
\left(
M_N^{-1}-mC_N^{\mathsf T}C_N
\right)
\Pi
```

からも分かる。従って結合強度は任意に大きくできない。本論文ではこの正定値条件を有限モデルの成立条件とする。

## Hamilton 方程式と配置速度

$H_N^{\rm nl}=0$ の線形核では、Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X),
```

```math
\dot Q
=
M_N^{-1}\Pi
+
C_N^{\mathsf T}P,
\qquad
\dot\Pi
=
-K_NQ
```

となる。場が配置速度へ加える成分を

```math
Y_N
=
C_N\Pi
```

と書く。この記号は第3章以降で固定する。

$P$ は正準運動量であり、機械的運動量 $m\dot X$ とは一致しない。

```math
m\dot X
=
P
+
mY_N
```

である。この区別を失うと、配置流束と運動量流束を取り違える。特に、配置密度の連続の式へ入る速度は $P/m$ だけでなく $Y_N$ を含む。

$H_N^{\rm nl}$ を残す場合は、$\dot X$ と $\dot Q$ にそれぞれ $\nabla_PH_N^{\rm nl}$ と $\nabla_\Pi H_N^{\rm nl}$、$\dot P$ と $\dot\Pi$ にそれぞれ $-\nabla_XH_N^{\rm nl}$ と $-\nabla_QH_N^{\rm nl}$ が加わる。本論文の正確な消去式は線形核について述べ、非線形項は混合と誤差の候補として分ける。

## 時間反転対称性

標準時間反転を

```math
\mathcal T:
(X,P,Q,\Pi,t)
\longmapsto
(X,-P,Q,-\Pi,-t)
```

とする。運動量結合項は

```math
(-P)^{\mathsf T}C_N(-\Pi)
=
P^{\mathsf T}C_N\Pi
```

なので時間反転で不変である。$H_N^{\rm nl}$ も全運動量の同時反転で偶関数なら、有限閉鎖核は時間反転対称である。

この対称性は、二側境界条件を置くことと両立する。しかし、時間反転対称な Hamiltonian だけから二側 Markov 拡散、共通拡散係数、Nelson の時間対称 Newton 則が自動的に従うわけではない。

## 静的な明・暗モード分解

運動量結合が場へ直接入る方向は

```math
\mathcal B_{\rm mom}
=
\operatorname{Ran}C_N^{\mathsf T}
```

である。第II部で使う装置の座標結合方向も含めた固定明部分空間を $\mathcal B_{\rm B}$、その直交補空間を $\mathcal B_{\rm D}$ とし、射影を $P_{\rm B},P_{\rm D}$ と書く。Fisher 側の運動量結合が暗モードを直接駆動しない条件は

```math
P_{\rm D}C_N^{\mathsf T}
=
0
```

である。

この条件は、$M_N^{-1}$ と $K_N$ が明・暗部分空間を保存することを意味しない。一般には

```math
P_{\rm D}K_NP_{\rm B}
\neq
0,
\qquad
P_{\rm D}M_N^{-1}P_{\rm B}
\neq
0
```

であり、内部発展による間接伝播が残る。この伝播は有限記憶、欠陥移送、Bell 側の局所セクター間交差応答の候補になる。

$\mathcal B_{\rm B}$ と $\mathcal B_{\rm D}$ に適合した直交行列 $O_N$ を固定し、

```math
\widetilde Q
=
O_NQ,
\qquad
\widetilde\Pi
=
O_N\Pi
```

と変換する。座標と共役運動量へ同じ直交行列を作用させるので、この変換は正準である。変換後の $O_NK_NO_N^{\mathsf T}$ と $O_NM_N^{-1}O_N^{\mathsf T}$ は一般にブロック対角ではない。静的な正準分類と動力学的な直和分離を混同しない。

## 位相整合成分と欠陥成分

長時間保つ位相整合成分と、外部へ移送する欠陥成分を分ける固定射影を

```math
P_{\rm c},
\qquad
P_\perp
=
I-P_{\rm c}
```

と書く。$P_{\rm c}$ は、$K_N$ と $M_N$ の固定スペクトル帯、$C_N^{\mathsf T}$ が生成する Krylov 部分空間、保存作用、装置構造から事前に定める。

得られた配置密度、目標量子状態、または欲しい Fisher 項を見て射影を選んではならない。正準な射影を定めたことは、その欠陥成分だけが不可逆に減衰することも、配置空間の Markov 性も意味しない。

## 外部流路を含む拡大全系

外部自由度を $(Z_{\rm ext},\Pi_{\rm ext})$、仕事貯蔵自由度を $z_{\rm work}$ とし、

```math
H_N^{\rm all}
=
H_N^{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
+
H_{\rm ctrl}
```

とする。$H_{\rm ctrl}$ は自律時計を含む設定変更、記録、再準備の有限相互作用をまとめた記号である。

全 Hamiltonian に外からの陽な時間依存がなければ、拡大全エネルギーは保存される。有限部分だけを見た収支は

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

となる。弱開放性は基礎方程式へ摩擦や白色雑音を直接追加することではなく、外部自由度を消去した後の有限部分の収支として現れる。

## 選択的な弱漏れと時間窓

欠陥成分へ強く、位相整合成分へ弱く結合する候補は、$P_\perp Q$、$P_\perp\Pi$ と外部自由度の結合として構成できる。外部相関時間が短く、対象周波数帯でスペクトル密度が滑らかなら、欠陥成分の有効減衰率を $\gamma_\perp$、整合成分の漏れ率を $\gamma_{\rm c}$ として

```math
\tau_{\rm corr}
\ll
\gamma_\perp^{-1}
\ll
\tau_{\rm coh},
\qquad
\gamma_{\rm c}
\ll
\gamma_\perp
```

を目標にできる。有限モデルから一様な指数減衰と流入補正を証明したわけではないため、これは近似候補である。

観測窓 $T_{\rm obs}$ と有限浴の再帰時間 $T_{\rm rec}$ には

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}
```

を要求する。測定窓では外部交換を小さい補正として扱い、試行間の準備窓では欠陥除去と再帰抑制を利用する。

## 弱漏れが担わない役割

選択的な弱漏れが実現しても、次は自動的には従わない。

1. $\int_0^tY_N(s)\,\mathrm ds$ が Brown 運動へ近づくこと。
2. 反作用記憶項が局所ドリフトまたは制御可能な残差へ縮約されること。
3. 配置変数 $X$ だけの射影が Markov 過程になること。
4. 二側条件付け後の前後過程が同じ拡散係数を持つこと。
5. Nelson の時間対称 Newton 則が成立すること。
6. Bell 側の3モード作用殻が $U(3)$ 等方になること。

弱漏れの主な役割は欠陥除去と再帰抑制である。配置拡散には多数モードの短記憶極限、Fisher 項には二側配置拡散の運動学、時間対称 Newton 則には独立した動力学的縮約、作用殻の方向準備には Hamiltonian な内部混合が必要である。

## 本章の結論

運動量結合 $P^{\mathsf T}C_N\Pi$ により、誘導場は粒子の配置速度へ $Y_N=C_N\Pi$ として直接入る。運動量2次形式の正定値条件、Hamilton 方程式、時間反転対称性、正準運動量と機械的運動量の差は有限モデル内部の厳密結果である。

固定明部分空間は $\operatorname{Ran}C_N^{\mathsf T}$ と第II部の装置結合方向を含む。外部流路は欠陥除去と有限再帰の抑制に使うが、配置拡散、$X$ 射影の Markov 性、時間対称 Newton 則をそれだけで導くものではない。

# 配置流束、誘導場の正確な消去、速度記憶核

> **位置づけ：** 運動量結合した有限誘導場について、正確な配置流束、速度モーメント式、自由速度揺らぎと反作用記憶項の分離を導く。Brown 極限と配置変数だけの Markov 性は近似または予想・未解決である。


## 拡大全系の Liouville 密度

外部自由度と仕事貯蔵自由度まで含む全位相点を $Z$ とし、全 Liouville 密度を $\varrho_N(Z,t)$ と書く。正規化は

```math
\int
\varrho_N(Z,t)
\,\mathrm dZ
=
1
```

である。第2章の全 Hamiltonian に対して

```math
\partial_t\varrho_N
+
\left\{
\varrho_N,
H_N^{\rm all}
\right\}
=
0
```

が成立する。有限部分を弱開放系として扱う場合も、外部変数まで含む拡大全系では Hamiltonian 流れと Liouville 体積保存を保つ。

## 配置密度と正確な配置流束

粒子の配置密度を

```math
\rho_N(x,t)
=
\int
\varrho_N(Z,t)
\,\mathrm dZ_{\widehat X}
```

とする。$\mathrm dZ_{\widehat X}$ は $X$ 以外の全変数についての積分を表す。$X=x$ を固定した条件付き平均を $\mathbb E_N[\cdot\mid X=x]$ と書く。

線形核におけるミクロな配置速度を

```math
U_N
=
\dot X
=
\frac Pm
+
Y_N,
\qquad
Y_N
=
C_N\Pi
```

と定める。配置流の平均速度は

```math
v_N(x,t)
=
\mathbb E_N
\left[
U_N
\mid
X=x
\right]
```

である。従って、旧位置結合モデルで用いた $\mathbb E_N[P\mid X=x]/m$ をそのまま配置速度と呼ぶことはできない。

## 0次モーメント

Liouville 方程式を $X$ 以外の全変数について積分し、境界項が消える減衰条件、周期境界、または無流束境界を仮定すると、

<!-- theorem-start:proposition -->
**命題（正確な配置連続の式）**

```math
\partial_t\rho_N
+
\nabla_x\cdot
\left(
\rho_Nv_N
\right)
=
0,
```

```math
v_N
=
\mathbb E_N
\left[
\frac Pm
+
C_N\Pi
\mathrel{\big|}
X=x
\right]
```

が成立する。

<!-- theorem-end:proposition -->

これは閉鎖近似を含まない。運動量結合による場の揺らぎは、力のモーメント式を経由せず、配置流束へ直接現れる。

## 正準運動量と配置速度の1次モーメント

$H_N^{\rm nl}=0$ とし、外部結合が粒子座標と正準運動量へ直接作用しない窓を考える。正準運動量は

```math
\dot P
=
-\nabla V(X)
```

に従う。Liouville 方程式へ $P_i$ を掛けて積分すると、

```math
\partial_t
\left(
\rho_N\overline P_{N,i}
\right)
+
\partial_{x_j}
\left[
\rho_N
\mathbb E_N
\left(
P_iU_{N,j}
\mid
X=x
\right)
\right]
=
-\rho_N\partial_{x_i}V
```

を得る。ここで $\overline P_N=\mathbb E_N[P\mid X=x]$ である。輸送速度が $P/m$ だけでないため、この式を旧稿の運動量 Euler 式へ変形してはならない。

配置速度自体の時間微分は

```math
\dot U_N
=
-\frac1m\nabla V(X)
-
C_NK_NQ
```

である。条件付き配置速度共分散を

```math
\Sigma_{U,N}
=
\mathbb E_N
\left[
\left(
U_N-v_N
\right)
\otimes
\left(
U_N-v_N
\right)
\mathrel{\big|}
X=x
\right]
```

とすると、同じ操作から

<!-- theorem-start:proposition -->
**命題（正確な配置速度収支）**

```math
m\rho_N
\left(
\partial_t
+
v_N\cdot\nabla
\right)
v_N
=
-\rho_N\nabla V
-
m\rho_N
\mathbb E_N
\left[
C_NK_NQ
\mid
X=x
\right]
-
m\nabla\cdot
\left(
\rho_N\Sigma_{U,N}
\right)
```

が成立する。

<!-- theorem-end:proposition -->

この有限 $N$ の恒等式は整合性検査には使えるが、本論文では右辺を Fisher 応力へ直接閉じる経路を中心課題にしない。白色極限では $U_N$ 自体が通常の有限分散速度として収束しないため、配置経路の2次変分を先に扱う必要がある。有限条件付き分散が余分な古典圧力として残らない条件は、独立した未解決問題である。

## 質量規格化した線形誘導場

正確な場消去を見通しよく書くため、正準な質量規格化により $M_N=I$ とした表示を用いる。規格化後の $K_N$ と $C_N$ に同じ記号を使い、

```math
\Omega_N
=
K_N^{1/2}
```

とする。場方程式は

```math
\dot Q
=
\Pi
+
C_N^{\mathsf T}P,
\qquad
\dot\Pi
=
-K_NQ
```

であり、$\Pi$ だけの2階方程式は

```math
\ddot\Pi
+
K_N\Pi
=
-K_NC_N^{\mathsf T}P
```

となる。

## 初期値問題での正確な消去

前節の2階方程式を初期値で解くと、

<!-- theorem-start:proposition -->
**命題（誘導場運動量の正確な初期値消去）**

```math
\Pi(t)
=
\cos
\left(
\Omega_Nt
\right)
\Pi(0)
-
\Omega_N
\sin
\left(
\Omega_Nt
\right)
Q(0)
```

```math
\quad
-
\int_0^t
\Omega_N
\sin
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}P(s)
\,\mathrm ds.
```

<!-- theorem-end:proposition -->

従って配置速度への場成分は

```math
Y_N(t)
=
Y_N^{\rm free}(t)
-
\int_0^t
\Gamma_N(t-s)P(s)
\,\mathrm ds,
```

```math
Y_N^{\rm free}(t)
=
C_N
\cos
\left(
\Omega_Nt
\right)
\Pi(0)
-
C_N\Omega_N
\sin
\left(
\Omega_Nt
\right)
Q(0),
```

```math
\Gamma_N(t)
=
C_N\Omega_N
\sin
\left(
\Omega_Nt
\right)
C_N^{\mathsf T}
```

と分かれる。$Y_N^{\rm free}$ は初期場から来る自由速度揺らぎ、畳み込み項は粒子から場への反作用が戻る速度記憶項である。

この分離により、自由浴を外から与えた雑音として扱う誤りを避けられる。配置拡散を導くには、自由成分の積分極限と反作用記憶項の縮約を別々に評価しなければならない。

## 自由速度揺らぎの相関

線形場の初期集団が中心化され、エネルギー尺度 $\Theta_N>0$ について

```math
\mathbb E_N
\left[
\Pi(0)\Pi(0)^{\mathsf T}
\right]
=
\Theta_NI,
```

```math
\mathbb E_N
\left[
Q(0)Q(0)^{\mathsf T}
\right]
=
\Theta_NK_N^{-1},
\qquad
\mathbb E_N
\left[
Q(0)\Pi(0)^{\mathsf T}
\right]
=
0
```

を満たすとする。このとき自由速度揺らぎの相関は厳密に

```math
R_N(t-s)
=
\mathbb E_N
\left[
Y_N^{\rm free}(t)
Y_N^{\rm free}(s)^{\mathsf T}
\right]
=
\Theta_NC_N
\cos
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}
```

となる。

有限 $N$ では、これは余弦関数の有限和であり、厳密には減衰相関でも OU 相関でもない。長時間極限を固定した有限浴の強収束として扱うことはできない。多数モード、滑らかなスペクトル包絡、弱い外部交換を用い、

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}
```

という再帰前の窓で粗視化する。

## 配置変位の拡散極限

自由速度揺らぎが作る配置変位を

```math
\Xi_N(t)
=
\int_0^t
Y_N^{\rm free}(s)
\,\mathrm ds
```

とする。相関包絡が積分可能で、異方性が小さい場合の目標は

```math
\Xi_N
\Longrightarrow
\sqrt{2\nu}\,W
```

という経路法則の収束である。等方拡散係数は、対応する連続スペクトル極限の相関 $R$ に対して

```math
\nu I_d
=
\int_0^\infty
R(s)
\,\mathrm ds
```

で決まる。

この Brown 極限は有限 Hamilton 方程式の厳密な等式ではない。多数モード極限、短記憶化、観測窓、初期集団、外部交換の順序を指定した近似結果として証明すべき対象である。

さらに、全配置速度には反作用記憶項がある。これが質量繰り込み、局所ドリフト、または小さい残差へ縮約されなければ、上の自由成分だけの Brown 極限から粒子の有効過程は得られない。

## 二側境界条件での消去

$\Pi$ の2階作用素へ、初期側と終端側の線形境界条件を課す。境界値問題が一意可解なら、

```math
\Pi(t)
=
\Pi_{\rm bd}(t)
-
\int_0^T
\mathcal G_{\Pi,N}(t,s)
K_NC_N^{\mathsf T}P(s)
\,\mathrm ds
```

と書ける。$\Pi_{\rm bd}$ は非同次境界データだけで決まる解、$\mathcal G_{\Pi,N}$ は指定した境界条件に対応する Green 核である。

境界条件が $\partial_t^2+K_N$ の自己共役領域を定めるなら、

```math
\mathcal G_{\Pi,N}(t,s)
=
\mathcal G_{\Pi,N}(s,t)^{\mathsf T}
```

となる。これは消去後の記憶作用が時間交換に対して対称になることを示す。しかし、自己共役性だけでは配置変数 $X$ の Markov 性も、Nelson の時間対称 Newton 則も導けない。

## 正確な結果と縮約課題

| 主張 | 導出状態 |
|---|---|
| 全 Liouville 方程式 | 定義した拡大全 Hamiltonian に対する厳密結果 |
| $U_N=P/m+C_N\Pi$ を含む配置連続の式 | 厳密結果 |
| 正準運動量と配置速度の1次モーメント式 | 線形核内部の厳密結果 |
| 誘導場運動量の初期値消去 | 指定初期値の下で厳密結果 |
| 自由速度揺らぎと反作用記憶項の分離 | 線形核内部の厳密結果 |
| 指定した Gauss 型初期集団での相関式 | 厳密結果 |
| 二側 Green 消去と時間交換対称性 | 一意可解な自己共役境界条件の下で厳密結果 |
| 自由配置変位の Brown 極限 | 近似結果として示すべき未完成課題 |
| 反作用記憶項の局所化と誤差評価 | 予想・未解決 |
| 配置変数だけの Markov 性 | 予想・未解決 |
| 二側条件付け後の共通拡散係数 | 予想・未解決 |
| 条件付き速度分散が余分な古典圧力を残さない条件 | 予想・未解決 |

## 本章の結論

運動量結合した誘導場では、配置流束は $P/m+C_N\Pi$ であり、場の揺らぎは粒子速度へ直接入る。線形誘導場の正確な消去により、自由速度揺らぎと反作用速度記憶項を分離した。

この変更により、Fisher 項を有限 $N$ の力密度閉鎖から直接作る必要はなくなる。代わりに、自由配置変位の Brown 極限、反作用記憶の局所化、配置変数だけの Markov 性を示す必要がある。有限浴は厳密な OU 浴でないため、結果は再帰前の有限観測窓における制御された近似として扱う。

# 二側配置拡散、Fisher 項、時間対称動力学

> **位置づけ：** 配置変数の二側 Markov 拡散を仮定した後の浸透速度、Fisher 情報、量子ポテンシャルは厳密結果である。運動量結合した有限誘導場からの配置拡散極限と時間対称 Newton 則は独立した未解決問題である。


## 配置雑音を持つ位相空間極限

第3章の自由速度揺らぎが短記憶化し、反作用記憶項が局所ドリフトまたは小さい残差へ縮約されるとき、最初の有効候補は

```math
\mathrm dX_t
=
\frac{P_t}{m}
\,\mathrm dt
+
\sqrt{2\nu}
\,\mathrm dW_t,
```

```math
\mathrm dP_t
=
-\nabla V(X_t)
\,\mathrm dt
```

である。$\nu>0$ は配置空間の等方拡散係数である。第2章の線形核では正準運動量が厳密に $\dot P=-\nabla V$ を満たすため、反作用記憶は $P$ の乱雑力でなく $X$ のドリフト側へ現れる。非線形項または外部自由度が $P$ へ直接結合する拡張では別の補正が加わるが、中心模型の式へ先に入れない。

この位相空間過程は $(X,P)$ について Markov でも、$X$ だけの射影は一般に Markov ではない。Fisher 項へ進むには、条件付き運動量が配置と時刻の局所関数へ閉じること、または $P$ を消去した配置経路法則が Markov 拡散へ近づくことが追加で必要である。

## 配置変数だけの二側 Markov 拡散

配置変数の極限過程が、共通の正の密度 $\rho(x,t)$ と同じ拡散係数 $\nu$ を持つ前進・後退表示を持つと仮定する。

```math
\mathrm dX_t
=
b_+(X_t,t)
\,\mathrm dt
+
\sqrt{2\nu}
\,\mathrm dW_t^+,
```

```math
\mathrm d_-X_t
=
b_-(X_t,t)
\,\mathrm dt
+
\sqrt{2\nu}
\,\mathrm d_-W_t^-.
```

境界条件付けは前後のドリフトを変えるが、1つの非退化拡散経路法則の条件付けとして構成できるなら、2次変分を決める主部は変えない。この理由により共通の $\nu$ は有効拡散モデル内部では自然である。ただし、有限 Hamiltonian 集団からその共通経路法則が得られることは未証明である。

前進と後退の Fokker--Planck 方程式は

```math
\partial_t\rho
=
-\nabla\cdot
\left(
\rho b_+
\right)
+
\nu\Delta\rho,
```

```math
\partial_t\rho
=
-\nabla\cdot
\left(
\rho b_-
\right)
-
\nu\Delta\rho
```

である。

## 現在速度と浸透速度

現在速度 $v$ と浸透速度 $u$ を

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
```

と定める。$u$ と拡散係数 $\nu$ は異なる量であり、以後この表記を固定する。

<!-- theorem-start:proposition -->
**命題（二側拡散の流れ分解）**

同じ正の密度と同じ等方拡散係数を持つ前進・後退表示では、

```math
\partial_t\rho
+
\nabla\cdot
\left(
\rho v
\right)
=
0,
```

```math
u
=
\nu\nabla\log\rho
```

が成立する。

<!-- theorem-end:proposition -->

これは配置 Markov 拡散モデル内部の厳密な運動学である。欲しい密度を見て $u$ を外から置くのではなく、同じ経路法則の前進・後退表示の差として得る。

## Fisher 情報と量子ポテンシャル

Fisher 情報を

```math
\mathcal I[\rho]
=
\int
\rho
\left|
\nabla\log\rho
\right|^2
\,\mathrm dx
```

とする。前節の恒等式から

```math
\frac m2
\int
\rho|u|^2
\,\mathrm dx
=
\frac{m\nu^2}{2}
\mathcal I[\rho]
```

が直ちに従う。従って Fisher 項は、旧位置結合経路の力密度閉鎖を経由せず、二側配置拡散の前後ドリフト差から直接現れる。

正規化制約と境界項が消える条件の下で、

```math
\frac{\delta\mathcal I}{\delta\rho}
=
-4
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

である。量子ポテンシャルに対応する密度汎関数を

```math
Q[\rho]
=
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

と定める。有効作用定数を

```math
\hbar_{\rm eff}
=
2m\nu
```

と置けば、

```math
Q[\rho]
=
-\frac{\hbar_{\rm eff}^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

となる。

Bohm–Fisher 応力を

```math
P_F[\rho]
=
-m\nu^2\rho
\,\nabla\nabla\log\rho
```

と定めると、

<!-- theorem-start:proposition -->
**命題（Fisher 応力恒等式）**

```math
-\nabla\cdot P_F[\rho]
=
2m\nu^2\rho
\,\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right)
=
-\rho\nabla Q[\rho]
```

が成立する。

<!-- theorem-end:proposition -->

## 時間対称 Newton 則は独立した主張である

前進・後退微分を $D_+,D_-$ とし、Nelson の時間対称平均加速度を

```math
a_{\rm ts}
=
\frac12
\left(
D_+D_-
+
D_-D_+
\right)X
```

と定義する。滑らかな $v,u$ について

```math
a_{\rm ts}
=
\partial_tv
+
\left(
v\cdot\nabla
\right)v
-
\left(
u\cdot\nabla
\right)u
-
\nu\Delta u
```

が成立する。$u=\nu\nabla\log\rho$ を使うと、

```math
\left(
u\cdot\nabla
\right)u
+
\nu\Delta u
=
2\nu^2
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right).
```

時間対称 Newton 則

```math
ma_{\rm ts}
=
-\nabla V
```

を追加で仮定または導出できれば、

```math
m
\left[
\partial_tv
+
\left(
v\cdot\nabla
\right)v
\right]
=
-\nabla V
-
\nabla Q[\rho]
```

を得る。

配置拡散の導出だけでは、この Newton 則は自動的に従わない。第3章の時間対称 Green 核、反作用記憶、境界条件付き変分を合わせ、非局所作用が上式へ収束することを別に示す必要がある。

## 局所的な Schrödinger 表示

節を含まない単連結領域で現在速度が

```math
v
=
\frac1m\nabla S
```

と書けるとする。連続の式と前節の Euler 型方程式を積分すると、時刻だけの関数を $S$ へ吸収した後、

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
V
+
Q[\rho]
=
0
```

を得る。そこで

```math
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\hbar_{\rm eff}}
\right)
```

と置けば、局所的には

```math
i\hbar_{\rm eff}
\partial_t\psi
=
\left(
-\frac{\hbar_{\rm eff}^2}{2m}\Delta
+
V
\right)
\psi
```

と同値である。

この局所変換は、節をまたぐ位相接続、循環量子化、単価な波動関数を保証しない。従って Wallstrom 問題は未解決である [19]。

## 配置拡散極限の誤差

旧稿の力密度閉鎖誤差に代えて、次の独立した誤差を管理する。

| 誤差 | 意味 |
|---|---|
| $\varepsilon_{\rm mem}=\tau_{\rm corr}/\tau_{\rm slow}$ | 自由速度相関の短記憶化 |
| $\varepsilon_{\rm fb}$ | 反作用記憶の局所化と質量繰り込みの残差 |
| $\varepsilon_{\rm BM}$ | 積分速度揺らぎと Brown 経路法則の差 |
| $\varepsilon_{\rm nM}$ | $X$ 射影の非 Markov 残差 |
| $\varepsilon_{\rm iso}$ | 配置拡散行列の異方性 |
| $\varepsilon_{\rm two}$ | 前後の2次変分と共通 $\nu$ からのずれ |
| $\varepsilon_{\rm press}$ | 条件付き速度分散が残す古典圧力 |
| $\varepsilon_{\rm dyn}$ | 時間対称 Newton 則からの動力学残差 |
| $\varepsilon_{\rm open}$ | 観測窓内の外部交換 |
| $\varepsilon_N$ | 有限モード切断、境界層、再帰 |

適用範囲は

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
\min
\left(
T_{\rm rec},
\tau_{\rm open}
\right)
```

である。中心結論を支えるには、有限 Hamiltonian 経路と有効過程を同じ入口・終端集団で比較し、短時間2次変分、3時刻条件付き分布、反作用記憶、作用残差を別々に測る必要がある。これらを1本の一様上界へまとめる定理はまだない。

## Gauss 幅における Routh–Fisher 一致

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

2次元内部座標を

```math
q
=
\sigma
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix}
```

とし、循環作用

```math
J
=
m\sigma^2\dot\theta
```

を固定して $\theta$ を Routh 縮約すると、内部 Routh 関数は

```math
R_{\rm int}
=
\frac m2\dot\sigma^2
-
\frac{J^2}{2m\sigma^2}
```

となる。$J=m\nu$ と置けば、

```math
-\frac{J^2}{2m\sigma^2}
=
-\frac{m\nu^2}{2}
\mathcal I[\rho_\sigma].
```

従って Gauss 幅族では、固定内部作用の Routh 項と二側配置拡散の負の Fisher 項が厳密に一致する。これは補助的な整合性検査であり、運動量結合した有限誘導場から配置拡散または時間対称 Newton 則を導くものではない。

## 補助的な線形 Gauss 型作用定理

配置 Markov 拡散が得られた後の作用表示を制御する補助結果を付録A、Bに残す。有限 Fourier–Gauss 型駆動、線形流れ、Gauss 初期分布、正定値の有限分解能終端記録、2次ポテンシャル、滑らかな有限次元パラメータ集合 $K$ を考える。

時間刻み $h$ の繰り込み済み粗視化作用を $\mathcal A_{N,h}^{R,U}$、極限の Guerra--Morato 作用を $\mathcal A_{\rm GM}^{R,U}$ とする。

<!-- theorem-start:theorem -->
**定理（線形 Gauss 型作用の <i>C</i><sup>1</sup> 極限）**

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
\,\mathrm dx
\,\mathrm dt
```

という Nelson 表示と厳密に一致する。

この定理は補助確率表示の作用値と有限次元パラメータ微分についての結果である。有限誘導場から配置拡散を導くこと、時間対称 Newton 則を導くこと、微視的時間発展が作用停留点を選ぶことは含まない。

## 導出状態

| 主張 | 導出状態 |
|---|---|
| 共通拡散係数を持つ二側 Markov 拡散での $u=\nu\nabla\log\rho$ | 有効拡散モデル内部の厳密結果 |
| Fisher 情報、量子ポテンシャル、Fisher 応力の恒等式 | 厳密結果 |
| 時間対称平均加速度の分解 | 有効拡散モデル内部の厳密結果 |
| Gauss 幅の Routh–Fisher 一致 | 指定した Gauss 変分モデル内部の厳密結果 |
| 線形 Gauss 型作用の $C^1$ 極限 | 補助モデル内部の厳密結果 |
| 有限誘導場から配置雑音を持つ位相空間過程への縮約 | 予想・未解決 |
| 配置変数だけの Markov 性と共通拡散係数 | 予想・未解決 |
| 反作用記憶、質量繰り込み、古典圧力の一様誤差評価 | 予想・未解決 |
| 時間対称 Green 応答から Newton 則への縮約 | 予想・未解決 |
| 微視的時間発展による Nelson 停留点選択 | 予想・未解決 |

## 本章の結論

運動量結合した誘導場は、配置速度揺らぎを直接生む。この揺らぎの積分が Brown 運動へ近づき、配置変数だけの二側 Markov 拡散が得られれば、$u=\nu\nabla\log\rho$、Fisher 項、量子ポテンシャルは運動学的に厳密に従う。

従って旧稿の Fisher 力密度閉鎖は中心課題から外れる。残る中心課題は、配置拡散極限、$X$ 射影の Markov 性、反作用記憶と古典圧力の制御、時間対称 Newton 則である。配置拡散を得たことと動力学まで得たことを分けて扱う。

# 第II部　同じ物理構成の境界作用殻縮約と Bell 型統計

# 構造化誘導場の2粒子・測定器拡張

> **位置づけ：** 第I部の運動量結合方向と同じ固定明部分空間に、左右局所装置と共通境界モードの座標結合方向を加える。全交差応答は近似条件、全殻拡散と一般測定器は予想・未解決である。


## 第II部の目的

第2章から第4章は、粒子と構造化誘導場の運動量結合、速度記憶核、配置拡散極限、二側 Markov 拡散を扱った。そこから Bell 型結果重みは出ない。第II部では、同じ誘導場へ装置の座標結合を加え、2粒子、左右測定器、共通境界モードへ拡張する。

1. 左右の局所記録と共通境界モードを、1つの構造化誘導場の中に置く。
2. 運動量結合方向と装置の座標結合方向から、時間に依存しない明・暗モード基底を定める。
3. 局所測定窓では、座標–座標核と運動量–座標混合核を含む左右交差応答が小さいことを条件にする。
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
\Pi
=
\begin{pmatrix}
\Pi_1&\cdots&\Pi_N
\end{pmatrix}^{\mathsf T}
```

とする。誘導場の Hamiltonian を

```math
H_{\rm med}
=
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

と書く。$K$ は正定値実対称行列、$V_{\rm nl}$ は有限時間混合を補助する滑らかな非線形項である。第2章の $K_N,M_N,H_N^{\rm nl}$ を質量規格化し、左右装置と境界モードを含む有限次元へ拡張した表示である。

第I部の粒子運動量結合は

```math
P^{\mathsf T}C_N\Pi
```

である。一方、第II部の左右局所装置は、局所応答座標 $x_A,x_B$ を用い、誘導場への結合を

```math
H_{\rm loc-link}
=
\epsilon_A x_A c_A^{\mathsf T}Q
+
\epsilon_B x_B c_B^{\mathsf T}Q
```

と結合する。$c_A,c_B$ は同じ $N$ 次元誘導場内の座標結合方向である。共通境界3モードへの座標結合方向も同じ場内に置く。これらを列に並べた行列を $B_q$ と書く。従って、第I部の $C_N^{\mathsf T}$ と第II部の $B_q$ は同じ明部分空間に属するが、結合型と物理的役割は異なる。

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

全ての直接結合方向が張る部分空間を

```math
\mathcal C
=
\operatorname{span}
\left\{
\operatorname{Ran}C_N^{\mathsf T},
c_A,c_B,c_{\partial,1},\ldots,c_{\partial,m}
\right\}
```

とする。$c_{\partial,\alpha}$ は境界3モードを混合する場方向である。この部分空間を第2章の $\mathcal B_{\rm B}$ に取り、暗射影 $P_{\rm D}$ に対して

```math
P_{\rm D}C_N^{\mathsf T}
=
0,
\qquad
P_{\rm D}B_q
=
0
```

とする。$\mathcal C$ の正規直交基底を先頭に並べる直交行列 $O$ を1つ固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde\Pi=O\Pi
```

とする。同じ $O$ を座標と運動量へ作用させるため、

```math
d\Pi^{\mathsf T}\wedge dQ
=
d\widetilde\Pi^{\mathsf T}\wedge d\widetilde Q
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

まず $\varepsilon_{\rm nl}=0$ の線形浴を考える。装置の座標結合だけを取り出して浴を消去すると、局所反応座標には自己応答と交差応答を含む記憶項が現れる [12--14]。単位質量表示では、座標–座標の代表核を

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

と書ける。第I部の運動量結合 $C_N$ が同じ場にある場合は、$Q$ と $\Pi$ の自由回転を通じて運動量–座標混合核も現れる。規格化や時間微分の位置は、どの装置変数へ結合するかにより変わる。

左右の全線形応答ブロックを $\mathcal R_{XY}(t)$ と書く。これは座標–座標、運動量–座標、必要なら運動量–運動量の各核をまとめた作用素である。局所性の誤差を

```math
\varepsilon_{\rm loc}
=
\frac{
\displaystyle
\sup_{0\leq t\leq T_{\rm meas}}
\max\left(
\|\mathcal R_{AB}(t)\|,
\|\mathcal R_{BA}(t)\|
\right)
}{
\displaystyle
\sup_{0\leq t\leq T_{\rm meas}}
\min\left(
\|\mathcal R_{AA}(t)\|,
\|\mathcal R_{BB}(t)\|
\right)
}
```

と定める。適用条件は

```math
\varepsilon_{\rm loc}\ll1.
```

$c_A^{\mathsf T}c_B=0$ だけでは、この条件は保証されない。$K$ が2方向を動力学的に混ぜる場合や、$C_N^{\mathsf T}$ を経由した混合応答がある場合は、有限時間後に交差応答が現れる。従って局所性は、結合ベクトルの直交性ではなく、全応答作用素または有限モデルの時間発展で検査する。

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

左右局所装置と共通境界モードを、複数の独立浴ではなく第I部と同じ固定射影を持つ1つの構造化誘導場として整理した。第I部の運動量結合方向 $\operatorname{Ran}C_N^{\mathsf T}$ と、第II部の座標結合方向 $\operatorname{Ran}B_q$ を同じ明部分空間へ含める。静的な明・暗モード分解は厳密な正準変換であるが、その後の Hamiltonian が完全な直和になるとは限らない。

局所性は、座標–座標応答だけでなく運動量–座標混合応答を含む全応答作用素について、測定窓内の $\varepsilon_{\rm loc}$ を実際に小さくする条件として置く。

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

> **位置づけ：** 配置拡散側と Bell 側の誤差を別々に管理する。配置拡散極限、配置 Markov 閉鎖、時間対称動力学、全殻拡散のミクロ導出は未完成であり、厳密な後段計算から遡って導出済みとは扱わない。


## 配置拡散側の誤差

第I部では、運動量結合した有限誘導場の正確な消去と、二側配置 Markov 拡散内部の Fisher 恒等式を得た。両者の間には、配置変位の Brown 極限、反作用記憶の局所化、$X$ 射影の Markov 性、時間対称 Newton 則という独立した段階がある。

| 誤差 | 物理的内容 | 検証方法 |
|---|---|---|
| $\varepsilon_{\rm mem}$ | 自由速度相関の短記憶化 | 相関包絡と粒子時間尺度を比較 |
| $\varepsilon_{\rm fb}$ | 反作用記憶と質量繰り込みの残差 | 正確な畳み込み項と局所近似を比較 |
| $\varepsilon_{\rm BM}$ | 積分速度揺らぎと Brown 経路法則の差 | 多時刻増分分布と2次変分を比較 |
| $\varepsilon_{\rm nM}$ | $X$ 射影の非 Markov 残差 | 3時刻条件付き分布と Chapman--Kolmogorov 残差 |
| $\varepsilon_{\rm iso}$ | 配置拡散行列の異方性 | 方向別の短時間2次変分 |
| $\varepsilon_{\rm two}$ | 前後の2次変分と共通 $\nu$ からのずれ | 同じ2境界集団の前進・後退推定を比較 |
| $\varepsilon_{\rm press}$ | 条件付き速度分散が残す古典圧力 | 正確な配置速度収支と有効 Euler 式を比較 |
| $\varepsilon_{\rm dyn}$ | 時間対称 Newton 則からの残差 | $ma_{\rm ts}+\nabla V$ を測る |
| $\varepsilon_{\rm proj}$ | 固定位相整合部分空間からの漏出 | $P_{\rm c},P_\perp$ 間の有限時間応答 |
| $\varepsilon_{\rm open}$ | 観測窓内の外部交換 | 拡大全系と閉鎖補助系を比較 |
| $\varepsilon_N$ | 有限場切断、境界層、再帰 | $N$、観測時間、外部結合を変えた収束 |

適用範囲は

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
\min
\left(
T_{\rm rec},
\tau_{\rm open}
\right)
```

である。全誤差を1本の一様上界へまとめる定理はまだない。

反証条件は段階ごとに異なる。積分速度揺らぎが拡散尺度を持たない、反作用記憶が局所化しない、$(X,P)$ は Markov でも $X$ 射影の非 Markov 残差が消えない、前後の2次変分が一致しない、または時間対称 Newton 残差が減少しない場合、対応する段階から先の主張は成立しない。

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

静的な明・暗モード基底の直交性は必要な構成要素だが、十分条件ではない。有限時間発展を支配する $K$、第I部の運動量結合 $C_N$、装置の座標結合、非線形項を含め、座標–座標核と運動量–座標混合核をまとめた $\mathcal R_{AB}(t)$ と $\mathcal R_{BA}(t)$ を評価する。

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
8. 運動量結合が配置速度揺らぎを作っても、その積分が Brown 運動へ収束するとは限らない。
9. $(X,P)$ の位相空間過程が Markov でも、$X$ だけの射影は一般に Markov ではない。
10. 二側配置拡散から Fisher 項が得られても、時間対称 Newton 則は自動的に従わない。

旧終端関数を削除したことを、確率測度のミクロな生成問題が解決したとは表現しない。問題は、結果依存終端重みの生成から、全3モード殻の等方準備と共通境界適合の実現へ移った。

## 反証に使える観測量

現行モデルは、少なくとも次の量で検査できる。

- 自由速度揺らぎ $Y_N^{\rm free}$ の相関包絡と積分変位の2次変分。
- 正確な反作用記憶項と局所ドリフトまたは質量繰り込み近似の残差。
- 前進・後退の短時間条件付き2次変分から得る拡散行列。
- 配置変数 $X$ の条件付き3時刻分布の非 Markov 残差。
- 条件付き速度分散が作る古典圧力と、時間対称 Newton 残差。
- 固定射影 $P_{\rm c},P_\perp$ 間の有限時間応答と欠陥減衰率。
- 局所測定窓の全交差応答作用素 $\mathcal R_{AB}(t),\mathcal R_{BA}(t)$。
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

1. 運動量結合した有限誘導場から、再帰前の観測窓で配置変位の Brown 極限を導く。
2. 反作用記憶を質量繰り込み、局所ドリフト、制御可能な残差へ分け、一様誤差を評価する。
3. 位相空間過程から配置変数だけの二側 Markov 拡散を導き、共通拡散係数と非 Markov 残差を評価する。
4. 条件付き速度分散が余分な古典圧力を残さない条件を示す。
5. 時間対称 Green 応答と条件付き変分から Nelson の時間対称 Newton 則を導く。
6. 固定位相整合射影と欠陥射影を保ったまま、欠陥成分だけの減衰と再帰抑制を外部スペクトルから導く。
7. 同じ誘導場の運動量–座標混合核を含む全交差応答を評価し、局所測定窓で抑える。
8. 誘導場の相関関数から $U(3)$ 等方な殻接方向生成子を導き、$\varepsilon_{\rm aniso}$ と混合時間を評価する。
9. 常時の弱い漏れと流入から、狭い総作用殻の定常幅とエネルギー収支を導く。
10. 設定、到来変数、装置微視状態から結果を形成する一般測定 Hamiltonian を構成する。
11. 境界適合、記録、消去、再初期化を1周期の明示モデルへ統合し、事後選別がないことを示す。
12. 偏った準備でも非信号性が回復する条件を判定する。
13. 微視的時間発展による Nelson 停留点選択を示す。
14. Born 則、Tsirelson 限界、Wallstrom 量子化へ進む追加構造を特定する。

## 最終結論

第I部では、粒子と構造化誘導場を運動量で結合し、正定値条件、時間反転対称性、正確な配置流束、自由速度揺らぎと反作用記憶項の分離を得た。配置変数の二側 Markov 拡散を仮定した後は、浸透速度、Fisher 項、量子ポテンシャルが運動学的に厳密に従う。

旧稿の Fisher 力密度閉鎖は中心課題から外した。しかし、有限誘導場からの配置拡散極限、$X$ 射影の Markov 性、反作用記憶と古典圧力の制御、時間対称 Newton 則は未証明である。補助的な線形 Gauss 型作用の $C^1$ 定理と Gauss 幅の Routh–Fisher 一致は後段の整合性検査であり、これらの縮約を証明しない。

第II部では、同じ物理構成を2粒子と測定器へ拡張し、1つの構造化誘導場を局所反応座標セクターと共通境界セクターへ静的に分けた。共通境界3モードの $U(3)$ 等方拡散は、縮約方程式の下で共通作用殻の一意な定常測度を与える。その作用殻を $J_+=I_+^{AB}$ で切ると、残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となり、対称セクターでは Bell 型余弦共同確率が厳密に従う。

Bell 固有の終端関数、中央比較器、相補時計は現行モデルから除いた。しかし、共通未来の境界適合と全殻測度は残る。現在の前進は、Fisher 項へ至る経路を力密度閉鎖から運動量結合による配置拡散へ置き換え、第I部と Bell 側を同じ構造化誘導場、固定射影、二側条件付け、弱い外部交換の下へ置いたことである。未完成の縮約は、配置拡散極限、配置 Markov 閉鎖、時間対称動力学、全殻準備として分けて管理する。

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

> **位置づけ：** 第2章の運動量結合方向と第II部の座標結合方向を含む固定射影について、静的基底、全交差応答、和・差変換、作用保存、固定殻体積、coarea 計算を補足する。誘導場から等方拡散への縮約は候補構成であり、未完成である。


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

浴座標を $Q,\Pi\in\mathbb R^N$ とし、

```math
H_{\rm med}
=
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

とする。$K$ は正定値実対称行列である。

第I部の粒子運動量結合方向を $\operatorname{Ran}C_N^{\mathsf T}$ とする。局所装置と境界装置が浴座標へ結合する方向を

```math
c_A,
\quad
c_B,
\quad
c_{\partial,1},
\ldots,
c_{\partial,m}
```

とする。$\operatorname{Ran}C_N^{\mathsf T}$ とこれらの座標結合方向が張る部分空間の正規直交基底を先頭に並べる直交行列 $O$ を固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde\Pi=O\Pi
```

と変換する。

<!-- theorem-start:proposition -->
**命題（直交浴基底変換の正準性）**
$O^{\mathsf T}O=I$ なら、$(Q,\Pi)\mapsto(\widetilde Q,\widetilde\Pi)$ は正準変換である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
正準1形式は

```math
\Pi^{\mathsf T}dQ
=
\widetilde\Pi^{\mathsf T}
O
O^{\mathsf T}
d\widetilde Q
=
\widetilde\Pi^{\mathsf T}d\widetilde Q
```

と保存される。従ってシンプレクティック2形式も保存される。
<!-- theorem-end:proof -->

変換後の2次形式は

```math
H_{\rm med}^{(2)}
=
\frac12\widetilde\Pi^{\mathsf T}\widetilde\Pi
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

結合方向に適合した基底を取っても、$\widetilde K$ は一般にブロック対角ではない。局所、境界、暗モード間の動的結合は $\widetilde K$ の非対角ブロックと $V_{\rm nl}$ に残る。運動量結合と座標結合が同じ明部分空間にあるため、自由回転後には両者の混合応答も一般に残る。

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

装置の座標結合だけに対する線形誘導場の運動方程式は

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
\right)\Pi(0)
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

同様に $\chi_{BA}$ を得る。従って、$c_A^{\mathsf T}c_B=0$ でも $\chi_{AB}(t)$ は一般に零ではない。$K$ が $c_A,c_B$ の張る部分空間を別々に不変にするときだけ、座標–座標の線形交差応答は厳密に消える。

第I部の $P^{\mathsf T}C_N\Pi$ を同時に含めると、$Q$ と $\Pi$ の自由回転を通じて運動量–座標混合核も生じる。局所性の判定には、各核をまとめた応答作用素 $\mathcal R_{XY}(t)$ を使う。

局所測定窓 $0\leq t\leq T_{\rm meas}$ で

```math
\varepsilon_{\rm loc}
=
\frac{
\sup_t
\max
\left(
\|\mathcal R_{AB}(t)\|,
\|\mathcal R_{BA}(t)\|
\right)
}{
\sup_t
\min
\left(
\|\mathcal R_{AA}(t)\|,
\|\mathcal R_{BB}(t)\|
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

- 運動量結合方向と座標結合方向を含む1つの有限誘導場に対する静的な直交正準基底。
- 装置の座標–座標交差応答核と、混合応答を含めた全応答作用素の定義。
- 最小結果符号化器の理想正準写像。
- 和・差変換の正準性と作用保存。
- $U(3)$ Hamiltonian 生成子が総作用を保存すること。
- 3モード固定作用殻の体積、周辺密度、残余ファイバー体積。
- 理想線形境界写像の共通 coarea Jacobian。

次は未導出である。

- 特定の有限非線形浴が必要な時間窓で等方な相関行列を持つこと。
- 有限誘導場と常時の外部交換から $D_\partial\Delta_{S^5}$ を一様誤差付きで得ること。
- 異方誤差、混合時間、再帰時間を同じパラメータから同時に閉じること。
- 運動量–座標混合核を含む左右全交差応答を、Bell 測定窓で一様に抑えること。
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
