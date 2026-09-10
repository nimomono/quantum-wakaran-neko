@number: D
@chapter: 付録
@title: M54駆動設定先行受信機構周期の証明
@status: R180Aの条件付きブロック代数、中央R191選択、節点切断、2翼局所R191、R180Cの局所応答・Bell監査・有限誤差・弱開放帰還を証明する。

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

## D.2 R180Aの中央R191選択

第2.13節の直交射影子作用保持機構を物理保持信号 $\widetilde V$ と2つの直交射影子 $\Pi_s^x$ へ適用し、

```math
J_s
=\mathcal J_0\widetilde V^\dagger\Pi_s^x\widetilde V
=\mathcal J_0r^2p_{s|x}(V)
```

を固定する。理想未使用運動量が零なら保持機構から信号への反作用は零である。2作用 $J_+,J_-$ を中央R191へ渡すと、理想吸引域測度は

```math
P(S=s\mid\widetilde V,x)
=\frac{J_s}{J_++J_-}
=p_{s|x}(V).
```

中央R191の有限混合、transducer、保護帯、有限温度retreat、有限decision時間、吸収記録を $\varepsilon_{191}^{\rm cen}$ にまとめる。結果 $S=s$ を固定した後に第2.13節の対合選別機構を制御し、対応する未規格化ブロック $\widetilde w_{s,x}$ を供給接続端へ渡す。入力係数または $r$ を外部制御器へ公開しない。R164/R190/R170の作用殻型選択は代替経路としてのみ残す。

選択結果 $s$ に対する理想B応答を

```math
P(B=b\mid s,V,x,y)
=\frac{|u_{b,y}^\dagger w_{s,x}|^2}{p_{s|x}(V)}
```

とすれば

```math
P(S=s,B=b\mid V,x,y)
=\left|\left(u_{s,x}^\dagger\otimes u_{b,y}^\dagger\right)V\right|^2.
```

<!-- theorem-start:proof -->
**証明（R180A）**

D.1がブロックと射影作用の等式を与える。中央R191の理想2結果重みは保持作用比 $J_s/(J_++J_-)=p_{s|x}$ である。選択結果の条件付きB応答を掛ければテンソル積Born重みになる。有限装置では中央R191、保持、選別、接続端の偏差を完全結果集合上で各1回だけ加える。証明終。
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

## D.5 R180切断面と局所R191誤差

R180B終了後の2翼信号方向は、理想方向 $(a_{s,x},b_{s,x}(V))$ から有界距離 $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ 以内にある。固定有限設定族と中央結果成分の安全域では、局所分析器と局所射影作用保持はこの方向誤差に対して一様Lipschitzである。

中央R191結果 $s$ と連動位相を完全共通原因 $\Lambda$ に含め、切断後にはA翼・B翼それぞれに未使用のR191指針変数を置く。理想局所核を $K_{A,0}^x,K_{B,0}^y$、実装核を $K_A^x,K_B^y$ とし、

```math
D_{\rm TV}(K_A^x,K_{A,0}^x)\leq\varepsilon_{191}^{A},
\qquad
D_{\rm TV}(K_B^y,K_{B,0}^y)\leq\varepsilon_{191}^{B}
```

とする。切断後の環境初期化の積因子化偏差を $\varepsilon_{\rm prod}$ とすれば、結果形成前の偏差は粗く

```math
\varepsilon_{\rm fib}
\leq
\varepsilon_{191}^{\rm cen}
+C_{\rm safe}\varepsilon_{\rm block}
+L_{\rm fib}K_{180}e^{-\gamma_{180}T_{\rm PH}}
+\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{191}^{A}
+\varepsilon_{191}^{B}
```

で抑えられる。R191主線ではR164/R190/R170の正則化、混合、固定誤差をこの式へ同時に加えない。連続信号測度を理想状態方向支持測度と全変動距離で比較せず、結果核へ写した後の全変動距離だけを用いる。

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

各分析器終了後に局所2作用を保持し、各翼のR191を走らせ、その後R112局所記録を作用する。未使用ブラウン巨視的スピン、局所浴接続部、熱浴初期種、記録素子が条件付き積なら、二つの局所測定機構も条件付き積になる。$\Lambda$ を切断面測度で平均すると相関は残るが、切断後の直接結合は生じない。

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

連続方向誤差は局所応答核の一様Lipschitz定数で結果分布距離へ変換してから加える。$\|\widetilde V\|\geq r_{\min}$ の安全集合では規格化写像がLipschitzであるため、M54の供給源、ゲート、正準SWAP、保持が状態方向へ与える偏差を $\varepsilon_{\rm ray}^{54}$ にまとめられる。正準SWAP自体に除算は含めない。分離器、結果成分作用、中央R191、ブロック保持、2端Hopf、切断、条件付き積偏差、2個の局所R191、R112局所記録、時計自由度を各1回だけ数えると本文の $\varepsilon_{180}^{\rm cyc}$ になる。

周辺化は全変動距離を増やさない。同じ理想周辺から各設定で $\varepsilon_{180}^{\rm cyc}$ 以内なら、反対設定間の周辺差は三角不等式により $2\varepsilon_{180}^{\rm cyc}$ 以下である。

無反応を数値0として相関を定義する。各相関の被積分関数の絶対値は1以下なので、1設定対の相関差は $2\varepsilon_{180}^{\rm cyc}$ 以下、4項のCHSH差は $8\varepsilon_{180}^{\rm cyc}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

R180Aが結果成分重みと理想共同Born分布、R180Bが有限時間2翼テンプレート整合、D.5が中央・局所R191の有限誤差、D.6が切断後の条件付き積測定機構を与える。各有限段を上の望遠鏡和境界で合成し、無反応を完全結果集合に残せば本文の全変動距離上界を得る。周辺とCHSHの境界はデータ処理と有界観測量評価から従う。未使用素子帰還はD.9の収縮条件を別に適用し、観測済み周期へ遡って加えない。証明終。
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

結果相関情報、ポンプ・排出先・R191浴の環境履歴はR179の流出浴へ流す。能動補助部は開放リセットし、有限閉鎖系の無履歴リセットは主張しない。
