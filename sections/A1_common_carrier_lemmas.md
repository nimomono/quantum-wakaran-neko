@number: A
@chapter: 付録
@title: 相関行列、作用区間、一意エルゴード性の共通補題
@status: 理想有効担体の相関行列を補助統計モデルとして整理し、本文第3章から第5章の確率式、不変測度、長期頻度、有限幅上界を証明する。旧Bell二側履歴モデルの基準体積と条件付けは不採用モデルの研究メモへ移した。

## A.1 理想有効担体と相関行列

この節だけでは、実正準対から

```math
d_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

を作り、設計済み有効 Hamiltonian

```math
H_{\rm eff}
=
d^\dagger h_Ld
```

を置く。これは第9章の位置ばね網そのものではなく、測定回路を記述する理想正準制御層である。この層内部では

```math
i\mathcal J_0\dot d
=
h_Ld,
\qquad
\mathcal J_0d^\dagger d
=
\operatorname{const}
```

が厳密に成立する。

調製条件 $\mathcal P$ とプログラム $M$ を固定した集団について

```math
C_M(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
d_t d_t^\dagger
\right]
```

と定める。$C_M$ は正半定値 Hermitian 行列であり、単一試行に追加する物質または正準変数ではない。

## A.2 相関行列の交換子発展

同じ集団の全試行が共通の $h_L(t)$ に従うなら、

```math
\begin{aligned}
i\mathcal J_0
\frac{d}{dt}
\left(dd^\dagger\right)
={}&
h_Ldd^\dagger
-
dd^\dagger h_L
\end{aligned}
```

なので、

```math
i\mathcal J_0\dot C_M
=
\left[h_L,C_M\right]
```

を得る。時間発展作用素を $U$ とすれば

```math
C_M(t)
=
U(t,t_0)
C_M(t_0)
U(t,t_0)^\dagger
```

である。従って跡、全固有値、階数、

```math
\mathcal P_C
=
\frac{\operatorname{tr}C^2}
{\left(\operatorname{tr}C\right)^2}
```

で定める純度が保存される。閉鎖線形発展だけでは高階数集団を階数1へ純化できない。

局所包絡 $b$ の厳密ミクロ発展には反回転項があるため、この交換子方程式を $b$ の厳密集団方程式として使わない。Q3-1のミクロ集団へ適用する場合は、第9章の包絡誤差を残す必要がある。

## A.3 階数1条件

$C=\Lambda\chi\chi^\dagger$、$\Lambda>0$、$\chi^\dagger\chi=1$ とする。$\chi$ と直交する任意の $v$ について

```math
0
=
v^\dagger Cv
=
\mathbb E
\left|
v^\dagger d
\right|^2
```

なので、$v^\dagger d=0$ がほとんど確実に成立する。有限次元直交補空間の基底を取れば、ある複素確率変数 $c^\omega$ が存在して

```math
d^\omega
=
c^\omega\chi
```

がほとんど確実に成立する。逆も明らかなので、階数1相関と共通射影方向は同値である。

交換子発展の下では、共通位相を選んで

```math
i\mathcal J_0\dot\chi
=
h_L\chi
```

とできる。この結果は理想有効層内部では厳密であるが、Q3-1のミクロ導出を置き換えない。

## A.4 近似階数1と閉包残差

$C$ の最大固有値を $\lambda_1$、主固有ベクトルを $\chi$ とし、

```math
C
=
\lambda_1\chi\chi^\dagger
+
E,
\qquad
E\geq0
```

とする。階数欠陥を

```math
\varepsilon_{\rm rank}
=
\frac{\operatorname{tr}E}
{\operatorname{tr}C}
```

とする。ユニタリ $W$ の出力 $k$ が理想因子に対して節を持つなら、

```math
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
\leq
\varepsilon_{\rm rank}
```

である。

残差付き有効式

```math
i\mathcal J_0\dot d
=
h_Ld+r
```

では

```math
i\mathcal J_0\dot C
=
\left[h_L,C\right]
+
D_C,
```

```math
D_C
=
\mathbb E
\left[
rd^\dagger-dr^\dagger
\right]
```

であり、

```math
\left\|D_C\right\|
\leq
2
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|d\right\|^2
\right)^{1/2}
```

を満たす。4次以上の Hamiltonian では $D_C$ が高次モーメントを含むため、$C$ だけの閉包は自動的に成立しない。

## A.5 作用区間選択

固定した $b,W$ に対し、$I_k\geq0$、$I_{\rm ph}=\sum_kI_k>0$ とする。$u$ が $[0,I_{\rm ph})$ 上で一様なら、結果事象

```math
E_k
=
\left\{
S_{k-1}\leq u<S_k
\right\}
```

の Lebesgue 長は $S_k-S_{k-1}=I_k$ である。従って

```math
P(E_k\mid b,W)
=
\frac{I_k}{I_{\rm ph}}
```

となる。境界集合 $\{u=S_k\}$ は有限集合なので零測度である。

選択器角 $\vartheta$ が $(b,W,\mathcal P)$ の下で条件付き Haar 分布なら、$u=I_{\rm ph}\vartheta/(2\pi)$ は条件付き一様である。条件付き期待値を取れば、

```math
P(k\mid W,\mathcal P)
=
\mathbb E
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
W,\mathcal P
\right]
```

を得る。

## A.6 固定作用公式と共分散補正

$I_{\rm ph}=I_0$ が集団で固定されるとする。$I_k=\mathcal J_0|(Wb)_k|^2$ なので、

```math
\mathbb E[I_k]
=
\mathcal J_0
\left(
WCW^\dagger
\right)_{kk},
```

```math
\mathbb E[I_{\rm ph}]
=
\mathcal J_0
\operatorname{tr}C
=
I_0
```

である。従って

```math
P_k
=
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
```

を得る。

全作用が変動する場合、$r_k=I_k/I_{\rm ph}$ と置けば $I_k=I_{\rm ph}r_k$ だから、

```math
\mathbb E[I_k]
=
\mathbb E[I_{\rm ph}]
\mathbb E[r_k]
+
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
```

である。$P_k=\mathbb E[r_k]$ を解けば本文の共分散恒等式を得る。

## A.7 無理数円回転の長期頻度と非混合性

正規化角 $r\in\mathbb R/\mathbb Z$ と無理数 $\alpha$ に対し、

```math
R_\alpha(r)
=
r+\alpha
\pmod1
```

とする。円周Haar測度は平行移動不変である。非零整数 $n$ に対するFourier指標の軌道平均は

```math
\frac1N
\sum_{j=0}^{N-1}
e^{2\pi in(r+j\alpha)}
=
e^{2\pi inr}
\frac{
1-e^{2\pi inN\alpha}
}{
N\left(1-e^{2\pi in\alpha}\right)
}
\longrightarrow
0
```

となる。三角多項式近似により回転は一意エルゴード的であり、境界がHaar零の半開区間 $[a,b)$ について、全初期角で訪問頻度が $b-a$ へ収束する。本文で使うBorn型長期頻度はこの区間頻度である。

一方、同じFourier指標の時間相関の絶対値は1のままなので、この回転は混合的でない。従って長期平均は得られるが、結果列の独立同分布性または二項分布型有限標本揺らぎは従わない。

## A.8 有限幅境界の測度上界

固定作用 $I_{\rm ph}$ の区間内に $L-1$ 個の内部境界 $S_1,\ldots,S_{L-1}$ がある。各境界の半幅 $w$ 近傍は長さ高々 $2w$ なので、一様測度と和集合上界から

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\min_{1\leq k<L}
|u-S_k|<w
\right)
\leq
2(L-1)
\frac{w}{I_{\rm ph}}
```

を得る。境界近傍が重なれば左辺はさらに小さい。

角の切断点近傍では、$f(\vartheta)=\vartheta/(2\pi)$ を円周上の滑らかな関数へ置き換える必要がある。その近傍の Haar 幅を $\varepsilon_{\rm cut}$ とすれば、無反応結果の全質量は右辺に $\varepsilon_{\rm cut}$ を加えて抑えられる。

## A.9 高階数集団に必要な追加自由度

固定作用殻上の源状態を $b^\omega$ とし、選択器角が $b^\omega$ の下で条件付き一様なら、

```math
P(k)
=
\mathbb E_\omega
\left[
\left|
\left(Wb^\omega\right)_k
\right|^2
\right]
=
\left(
WCW^\dagger
\right)_{kk}
```

である。ただし、本文の1次元不変トーラスでは $b^\omega=\chi$ が固定される。高階数 $C$ を単一軌道の時間平均として得るには、$b^\omega$ を動かす別の不変力学と、その力学に条件付けても選択器角が Haar 分布を保つ積構造または十分な結合条件が必要である。
