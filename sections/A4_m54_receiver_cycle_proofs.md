@number: D
@chapter: 付録
@title: M54駆動setting-pre receiver周期の証明
@status: R180Aの条件付きblock代数、作用殻選択、node切断、2翼matching、R180Cの局所応答・Bell監査・有限誤差・弱開放帰還を証明する。

## D.1 行優先block分解

canonical SWAP後の物理hold信号と解析上の規格化rayを、行優先で

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

とする。$\widetilde V=v$ は同次元正準SWAPがそのまま移した物理信号であり、$V=\widetilde V/r$ は解析上だけ用いる。A basis変換後の規格化成分は

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

である。物理blockは

```math
\widetilde w_{s,x}
=
\widetilde D^{\mathsf T}
\overline{u_{s,x}}
=
r w_{s,x}
```

であり、規格化blockについて

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

$u_{+,x},u_{-,x}$ の完全性から2つのprojectorの和は $I_4$ であり、$\|V\|=1$ なら $p_{+|x}+p_{-|x}=1$ となる。

## D.2 R180Aの作用殻選択

R181Dを物理hold信号 $\widetilde V$ と2つの直交projector $\Pi_s^x$ へ適用し、blank pointerへ

```math
A_s
=
\mathcal J_0\widetilde V^\dagger\Pi_s^x\widetilde V
=
\mathcal J_0r^2p_{s|x}(V)
```

をlatchする。理想blank momentumが零なら信号への反作用は零である。有限blank、selector plateau、clock、cutoffによる偏差は $\varepsilon_{\rm latch}$ へ入れる。容量の生成はR181Dの役割であり、R164は次に同じ容量を排他的な作用殻状態数へ写す。

R164の作用殻状態数を

```math
\Omega_s(V,x)
=
C_{\rm sh}A_s
```

とし、枝対称な同じ比例定数 $C_{\rm sh}$ を使う。従って理想平衡枝比では共通radial因子 $\mathcal J_0r^2$ が消え、

```math
\frac{\Omega_s}{\Omega_++\Omega_-}
=
\frac{A_s}{A_++A_-}
=
p_{s|x}(V).
```

R161の平方根型率はこの比を一意定常分布とし、R162が固定有限時間上の有限衝突近似を与える。有限mixing、collision、overflowを無反応込みの $\varepsilon_{\rm latch}$ へ加える。枝選択後に信号と作用殻をdecoupleし、選択pointerだけで対応する物理block $\widetilde w_{s,x}$ をsource portへroutingする。入力係数または $r$ を外部controllerへ公開しない。

選択枝 $s$ について、局所B応答を

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

D.1がblockとprojector作用の等式を与える。R181DのlatchとR164の線形状態数により理想内部枝重みは $p_{s|x}$ となり、R161/R162が有限時間の物理的枝選択を与える。選択枝の条件付きB応答へ $p_{s|x}$ を掛けると上のテンソル積Born重みになる。有限装置では各Markov核と有限正準写像の誤差を完全結果集合上で加える。証明終。
<!-- theorem-end:proof -->

## D.3 node切断と方向安定性

$p_{s|x}<\tau$ の枝を無反応へ送ると、その総質量は

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

従ってhold、splitter、block routingの誤差は安全枝で $C_\tau\varepsilon_{\rm block}$ へ移せる。singletでは全枝で $p_s=1/2$ なので、$\tau<1/2$ に固定すればnode切断は生じず、規格化定数も一様である。

## D.4 singlet特殊化

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

$\mathsf E$ はunitaryだから $\|w_{s,x}\|^2=1/2$ である。規格化B方向は $-\mathsf E\overline{u_{s,x}}$ となる。旧M48の $\mathsf E\overline{u_{s,x}}$ との差はglobal signだけであり、projector、W型作用、局所応答を変えない。

## D.5 R180 strong fiber

局所fiber $\mathcal F_W^\delta(c)$ では

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)=\pi_i^\delta(z).
```

$\pi^\delta(e^{i\alpha}z)=\pi^\delta(z)$ なので共通位相は粒子位置分布を変えない。R180B終了後の2翼方向誤差は $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ 以下である。固定有限設定族と $p_s\geq\tau$ のcompact安全域では $z\mapsto\pi^\delta(z)$ と局所分析・記録核は射影距離に関して一様Lipschitzである。

paired-Hopf終了後に $z_A,z_B$ を保持し、A、Bの粒子位置bathを条件付き独立に時間 $T_X$ だけ走らせる。R161から各翼の条件付き位置分布は $\pi^\delta$ から $C_Xe^{-\lambda_X^\delta T_X}$ 以内にある。正則化誤差は各翼で $\delta/(1+\delta)$ 以下である。

枝を最大couplingし、連続信号を同じtemplateとpaired位相でcoupleし、離散位置を条件付き最大couplingすれば、理想fiber $\nu_{V,x}^0$ からの結果前誤差は

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

となる。連続信号測度を理想ray支持測度と全変動距離で比較しない。

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

各分析器終了後に局所信号を固定し、各翼のR170を走らせる。fresh作用殻、衝突cell、noise seed、記録cellが条件付き積なら、二つの局所instrumentも条件付き積になる。$\Lambda$ を切断面測度で平均すると相関は残るが、切断後の直接結合は生じない。

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

従ってB周辺は $x$ に依存しない。A周辺はprojector作用 $p_{a|x}$ であり $y$ に依存しない。

singletについて $b_{s,x}$ のBlochベクトルは $-s\boldsymbol n_x$ だから

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

実際の1周期を有限個の核 $K_1,\ldots,K_N$、理想核を $K_1^0,\ldots,K_N^0$ とする。各段の一様全変動誤差が $\epsilon_j$ 以下なら逐次couplingとdata processingから

```math
D_{\rm TV}
\left(
\nu_0K_1\cdots K_N,
\nu_0K_1^0\cdots K_N^0
\right)
\leq
\sum_j\epsilon_j.
```

連続方向誤差は局所応答核の一様Lipschitz定数で結果分布距離へ変換してから加える。$\|\widetilde V\|\geq r_{\min}$ のsafe setでは規格化写像がLipschitzであるため、M54 source、gate、canonical SWAP、holdがrayへ与える偏差を $\varepsilon_{\rm ray}^{54}$ にまとめられる。canonical SWAP自体に除算は含めない。splitter、branch作用、node、block保持、paired-Hopf、位置matching、切断、条件付き積偏差、局所R170、記録、clockを各1回だけ数えると本文の $\varepsilon_{180}^{\rm cyc}$ になる。

周辺化は全変動距離を増やさない。同じ理想周辺から各設定で $\varepsilon_{180}^{\rm cyc}$ 以内なら、反対設定間の周辺差は三角不等式により $2\varepsilon_{180}^{\rm cyc}$ 以下である。

無反応を数値0として相関を定義する。各相関の被積分関数の絶対値は1以下なので、1設定対の相関差は $2\varepsilon_{180}^{\rm cyc}$ 以下、4項のCHSH差は $8\varepsilon_{180}^{\rm cyc}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

R180Aがbranch重みと理想共同Born分布、R180Bが有限時間2翼template matching、D.5が局所粒子位置fiber、D.6が切断後の条件付き積instrumentを与える。各有限段を上のtelescoping境界で合成し、無反応を完全結果集合に残せば本文の全変動距離上界を得る。周辺とCHSHの境界はdata processingと有界観測量評価から従う。fresh-cell帰還はD.9のcontractを別に適用し、観測済み周期へ遡って加えない。証明終。
<!-- theorem-end:proof -->

## D.8 設定依存性の位置

M54 sourceと設定生成角の設定前測度を積に取るため、$V$ の準備法則は実際に生成される $x,y$ に依存しない。一方、$x$ は $U_x^\dagger\otimes I_2$、$\Pi_s^x$、$a_{s,x}$、$b_{s,x}(V)$ を決める。異なる非可換設定では理想fiber $\nu_{V,x}^0$ の支持とbranch分解が異なるので

```math
\mu_{\rm cut}
\left(
d\Lambda\mid V,x,y
\right)
=
\mu_{V,x}(d\Lambda)
```

は一般に $x$ 依存である。従ってBellの測定設定独立性は成立しない。$y$ を中央準備核へ入れず、切断後にB局所核へだけ入れることと、理想B周辺が $x$ に依存しないことは両立する。

## D.9 fresh-cell帰還

記録後の能動状態を $Y$、fresh基準状態を $Y_*$ とする。交換核が

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

使用済みM54 hold、branch latch、pump、sink、局所作用殻、衝突cellはspent履歴として残す。閉系から無履歴でfresh状態へ戻すとは主張しない。
