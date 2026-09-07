@number: D
@chapter: 付録
@title: M54駆動設定先行受信機構周期の証明
@status: R180Aの条件付きブロック代数、作用殻選択、節点切断、2翼整合、R180Cの局所応答・Bell監査・有限誤差・弱開放帰還を証明する。

## D.1 行優先ブロック分解

正準SWAP後の物理保持信号と解析上の規格化状態方向を、行優先で

```math
\widetilde V
=
\operatorname{vec}_{\rm row}(\widetilde D),
\qquad
r=\|\widetilde V\|>0,
\qquad
V
=
\operatorname{vec}_{\rm row}(D),
\qquad
D=\frac{\widetilde D}{r},
\qquad
D
=
\begin{pmatrix}
D_{00}&D_{01}\\
D_{10}&D_{11}
\end{pmatrix}
```

とする。$\widetilde V=v$ は同次元正準SWAPがそのまま移した物理信号であり、$V=\widetilde V/r$ は解析上だけ用いる。A 基底変換後の規格化成分は

```math
\left[
\left(
U_x^\dagger\otimes I_2
\right)V
\right]_{s,k}
=
\sum_j
\overline{(u_{s,x})_j}
D_{jk}.
```

右辺を $k$ 成分とする列ベクトルは

```math
w_{s,x}
=
D^{\mathsf T}
\overline{u_{s,x}}
```

である。物理ブロックは

```math
\widetilde w_{s,x}
=
\widetilde D^{\mathsf T}
\overline{u_{s,x}}
=
r w_{s,x}
```

であり、規格化ブロックについて

```math
\begin{aligned}
\|w_{s,x}\|^2
&=
u_{s,x}^\dagger
D^*D^{\mathsf T}
u_{s,x}\\
&=
V^\dagger
\left(
|u_{s,x}\rangle\langle u_{s,x}|
\otimes I_2
\right)V.
\end{aligned}
```

$u_{+,x},u_{-,x}$ の完全性から2つの射影子の和は $I_4$ であり、$\|V\|=1$ なら $p_{+|x}+p_{-|x}=1$ となる。

## D.2 R180Aの作用殻選択

第2.13節の直交射影子作用保持機構を物理保持信号 $\widetilde V$ と2つの直交射影子 $\Pi_s^x$ へ適用し、未使用指針変数へ

```math
A_s
=
\mathcal J_0\widetilde V^\dagger\Pi_s^x\widetilde V
=
\mathcal J_0r^2p_{s|x}(V)
```

を固定する。理想未使用 運動量が零なら信号への反作用は零である。有限未使用、選択機構 平坦域、時計自由度、カットオフによる偏差は $\varepsilon_{\rm latch}$ へ入れる。容量の生成は第2.13節の共通補題の役割であり、R170は次にR164/R161/R162を通して同じ容量から排他的選択を形成し、結果を固定する。

R164の作用殻状態数を

```math
\Omega_s(V,x)
=
C_{\rm sh}A_s
```

とし、結果成分対称な同じ比例定数 $C_{\rm sh}$ を使う。従って理想平衡結果成分比では共通大きさ方向因子 $\mathcal J_0r^2$ が消え、

```math
\frac{\Omega_s}{\Omega_++\Omega_-}
=
\frac{A_s}{A_++A_-}
=
p_{s|x}(V).
```

R170の内部でR161の平方根型率はこの比を一意定常分布とし、R162が固定有限時間上の有限衝突近似を与える。有限混合、衝突、あふれを無反応込みの $\varepsilon_{\rm latch}$ へ加える。R170で結果を固定した後に信号と作用殻を切り離し、同じ選択指針変数で第2.13節の対合選別機構を制御して対応する物理ブロック $\widetilde w_{s,x}$ を供給接続端へ渡す。入力係数または $r$ を外部制御器へ公開しない。

選択結果成分 $s$ について、局所B応答を

```math
P(B=b\mid s,V,x,y)
=
\frac{
|u_{b,y}^\dagger w_{s,x}|^2
}{
p_{s|x}(V)
}
```

とすれば

```math
\begin{aligned}
P(S=s,B=b\mid V,x,y)
&=
|u_{b,y}^\dagger w_{s,x}|^2\\
&=
\left|
\sum_{j,k}
\overline{(u_{s,x})_j}
\overline{(u_{b,y})_k}
D_{jk}
\right|^2\\
&=
\left|
\left(
u_{s,x}^\dagger
\otimes
u_{b,y}^\dagger
\right)V
\right|^2.
\end{aligned}
```

<!-- theorem-start:proof -->
**証明（R180A）**

D.1がブロックと射影子作用の等式を与える。第2.13節の容量固定補題とR170により理想内部結果重みは $p_{s|x}$ となり、R170内部のR161/R162が有限時間の物理的結果選択と固定を与える。選択結果成分の条件付きB応答へ $p_{s|x}$ を掛けると上のテンソル積Born重みになる。有限装置では各Markov核と有限正準写像の誤差を完全結果集合上で加える。証明終。
<!-- theorem-end:proof -->

## D.3 節点切断と方向安定性

$p_{s|x}<\tau$ の結果成分を無反応へ送ると、その総質量は

```math
\sum_{s:p_{s|x}<\tau}p_{s|x}
\leq
\sum_{s:p_{s|x}<\tau}\tau
\leq2\tau
```

である。これは事後選別率ではなく完全結果分布の無反応質量として数える。

非零ベクトルの規格化写像 $n(w)=w/\|w\|$ について、$\|w\|,\|w'\|\geq\sqrt\tau$ なら

```math
\left\|
n(w)-n(w')
\right\|
\leq
\frac{2}{\sqrt\tau}
\|w-w'\|.
```

従って保持、分離器、ブロック 経路選択の誤差は安全な結果成分で $C_\tau\varepsilon_{\rm block}$ へ移せる。一重項では全結果成分で $p_s=1/2$ なので、$\tau<1/2$ に固定すれば節点切断は生じず、規格化定数も一様である。

## D.4 一重項特殊化

```math
D_{\rm s}
=
\frac{\mathsf E}{\sqrt2},
\qquad
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathsf E^{\mathsf T}=-\mathsf E
```

なので

```math
w_{s,x}
=
D_{\rm s}^{\mathsf T}
\overline{u_{s,x}}
=
-\frac1{\sqrt2}
\mathsf E\overline{u_{s,x}}.
```

$\mathsf E$ はユニタリだから $\|w_{s,x}\|^2=1/2$ である。規格化B方向は $-\mathsf E\overline{u_{s,x}}$ となる。旧M48の $\mathsf E\overline{u_{s,x}}$ との差は全体符号だけであり、射影子、W型作用、局所応答を変えない。

## D.5 R180強整合ファイバー

局所ファイバー $\mathcal F_W^\delta(c)$ では

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)=\pi_i^\delta(z).
```

$\pi^\delta(e^{i\alpha}z)=\pi^\delta(z)$ なので共通位相は粒子位置分布を変えない。R180B終了後の2翼方向誤差は $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ 以下である。固定有限設定族と $p_s\geq\tau$ のコンパクト安全域では $z\mapsto\pi^\delta(z)$ と局所分析・記録核は射影距離に関して一様Lipschitzである。

2端Hopf終了後に $z_A,z_B$ を保持し、A、Bの粒子位置浴を条件付き独立に時間 $T_X$ だけ走らせる。R161から各翼の条件付き位置分布は $\pi^\delta$ から $C_Xe^{-\lambda_X^\delta T_X}$ 以内にある。正則化誤差は各翼で $\delta/(1+\delta)$ 以下である。

結果成分を最大結合し、連続信号を同じテンプレートと連動位相で結合し、離散位置を条件付き最大結合すれば、理想ファイバー $\nu_{V,x}^0$ からの結果前誤差は

```math
\begin{aligned}
d_{\rm fib}
\leq{}&
\varepsilon_{\rm latch}
+2\tau
+C_\tau\varepsilon_{\rm block}
+K_{180}e^{-\gamma_{180}T_{\rm PH}}\\
&+
\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}
+\varepsilon_{\rm cut}
\end{aligned}
```

となる。連続信号測度を理想状態方向支持測度と全変動距離で比較しない。

## D.6 局所応答と非信号性

切断後の完全共通原因 $\Lambda$ に条件付けて

```math
K_{\rm post}^{xy}
=
K_A^x\otimes K_B^y
```

とする。A分析器は $a_{s,x}=u_{s,x}$ を結果 $s$ の井戸へ写す。B分析器の理想応答は

```math
P(B=b\mid s,V,x,y)
=
|u_{b,y}^\dagger b_{s,x}(V)|^2.
```

各分析器終了後に局所信号を固定し、各翼のR170選択・固定を走らせ、その後R112局所記録を作用する。未使用作用殻、衝突素子、ノイズ初期種、記録素子が条件付き積なら、二つの局所測定機構も条件付き積になる。$\Lambda$ を切断面測度で平均すると相関は残るが、切断後の直接結合は生じない。

Bの未規格化周辺行列は

```math
\begin{aligned}
\sum_s
w_{s,x}w_{s,x}^\dagger
&=
D^{\mathsf T}
\left(
\sum_s
\overline{u_{s,x}}u_{s,x}^{\mathsf T}
\right)
\overline D\\
&=
D^{\mathsf T}\overline D.
\end{aligned}
```

従ってB周辺は $x$ に依存しない。A周辺は射影子作用 $p_{a|x}$ であり $y$ に依存しない。

一重項について $b_{s,x}$ のBlochベクトルは $-s\boldsymbol n_x$ だから

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
```

$P(s)=1/2$ と $A=s$ を使えば本文の余弦共同分布が従う。

## D.7 R180Cの有限誤差

実際の1周期を有限個の核 $K_1,\ldots,K_N$、理想核を $K_1^0,\ldots,K_N^0$ とする。各段の一様全変動誤差が $\epsilon_j$ 以下なら逐次結合とデータ処理から

```math
D_{\rm TV}
\left(
\nu_0K_1\cdots K_N,
\nu_0K_1^0\cdots K_N^0
\right)
\leq
\sum_j\epsilon_j.
```

連続方向誤差は局所応答核の一様Lipschitz定数で結果分布距離へ変換してから加える。$\|\widetilde V\|\geq r_{\min}$ の安全集合では規格化写像がLipschitzであるため、M54の供給源、ゲート、正準SWAP、保持が状態方向へ与える偏差を $\varepsilon_{\rm ray}^{54}$ にまとめられる。正準SWAP自体に除算は含めない。分離器、結果成分作用、中央R170、ブロック保持、2端Hopf、位置整合、切断、条件付き積偏差、局所R170、R112局所記録、時計自由度を各1回だけ数えると本文の $\varepsilon_{180}^{\rm cyc}$ になる。

周辺化は全変動距離を増やさない。同じ理想周辺から各設定で $\varepsilon_{180}^{\rm cyc}$ 以内なら、反対設定間の周辺差は三角不等式により $2\varepsilon_{180}^{\rm cyc}$ 以下である。

無反応を数値0として相関を定義する。各相関の被積分関数の絶対値は1以下なので、1設定対の相関差は $2\varepsilon_{180}^{\rm cyc}$ 以下、4項のCHSH差は $8\varepsilon_{180}^{\rm cyc}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

R180Aが結果成分重みと理想共同Born分布、R180Bが有限時間2翼テンプレート整合、D.5が局所粒子位置ファイバー、D.6が切断後の条件付き積測定機構を与える。各有限段を上の望遠鏡和境界で合成し、無反応を完全結果集合に残せば本文の全変動距離上界を得る。周辺とCHSHの境界はデータ処理と有界観測量評価から従う。未使用素子帰還はD.9の収縮条件を別に適用し、観測済み周期へ遡って加えない。証明終。
<!-- theorem-end:proof -->

## D.8 設定依存性の位置

M54の供給源と設定生成角の設定前測度を積に取るため、$V$ の準備法則は実際に生成される $x,y$ に依存しない。一方、$x$ は $U_x^\dagger\otimes I_2$、$\Pi_s^x$、$a_{s,x}$、$b_{s,x}(V)$ を決める。異なる非可換設定では理想ファイバー $\nu_{V,x}^0$ の支持と結果成分分解が異なるので

```math
\mu_{\rm cut}
\left(
d\Lambda\mid V,x,y
\right)
=
\mu_{V,x}(d\Lambda)
```

は一般に $x$ 依存である。従ってBellの測定設定独立性は成立しない。$y$ を中央準備核へ入れず、切断後にB局所核へだけ入れることと、理想B周辺が $x$ に依存しないことは両立する。

## D.9 未使用素子帰還

記録後の能動状態を $Y$、未使用基準状態を $Y_*$ とする。交換核が

```math
E
\left[
d_{\rm ret}(Y',Y_*)
\mid Y
\right]
\leq
r_{\rm ret}d_{\rm ret}(Y,Y_*)
+\epsilon_{\rm fresh},
\qquad
0\leq r_{\rm ret}<1
```

を満たすなら、反復により

```math
E
\left[
d_{\rm ret}(Y_n,Y_*)
\right]
\leq
r_{\rm ret}^n
d_{\rm ret}(Y_0,Y_*)
+
\frac{\epsilon_{\rm fresh}}{1-r_{\rm ret}}.
```

使用済みM54 保持、結果成分の固定機構、ポンプ、排出先、局所作用殻、衝突素子は使用済み履歴として残す。閉系から無履歴で未使用状態へ戻すとは主張しない。
