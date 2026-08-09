@number: A2
@chapter: 付録
@title: 相関行列、作用区間、無理数回転の補助結果
@status: 理想有効担体の相関行列を補助統計モデルとして整理し、本文第4章と第5章の確率式、不変測度、長期頻度、有限幅上界、Bell 基準体積を証明する。

## B.1 理想有効担体と相関行列

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

を置く。これは第2章の位置ばね網そのものではなく、測定回路を記述する理想正準制御層である。この層内部では

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

## B.2 相関行列の交換子発展

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

局所包絡 $b$ の厳密ミクロ発展には反回転項があるため、この交換子方程式を $b$ の厳密集団方程式として使わない。Q1のミクロ集団へ適用する場合は、第3章の包絡誤差を残す必要がある。

## B.3 階数1条件

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

とできる。この結果は理想有効層内部では厳密であるが、Q1のミクロ導出を置き換えない。

## B.4 近似階数1と閉包残差

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

## B.5 作用区間選択

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

## B.6 固定作用公式と共分散補正

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

## B.7 無理数円回転の不変性

正規化角 $r=\vartheta/(2\pi)\in\mathbb R/\mathbb Z$ を用い、

```math
R_\alpha(r)
=
r+\alpha
\pmod1,
\qquad
\alpha\notin\mathbb Q
```

とする。円周 Haar 測度 $m$ は平行移動不変なので、任意の可測集合 $A$ に対し

```math
m
\left(
R_\alpha^{-1}A
\right)
=
m(A)
```

である。従って $m$ は不変確率測度である。

一意性を Fourier 係数で示す。$R_\alpha$ の不変確率測度を $\nu$ とし、整数 $n$ に対する Fourier 係数を

```math
\widehat\nu(n)
=
\int_0^1
e^{-2\pi inr}
\,d\nu(r)
```

とする。不変性から

```math
\widehat\nu(n)
=
e^{-2\pi in\alpha}
\widehat\nu(n)
```

を得る。$n\neq0$ かつ $\alpha\notin\mathbb Q$ なら $e^{-2\pi in\alpha}\neq1$ なので、$\widehat\nu(n)=0$ である。$\widehat\nu(0)=1$ と合わせ、全 Fourier 係数が Haar 測度と一致する。三角多項式の一様稠密性により $\nu=m$ である。

## B.8 一意エルゴード性と区間頻度

連続関数 $f$ の時間平均を

```math
A_Nf(r)
=
\frac1N
\sum_{j=0}^{N-1}
f
\left(
r+j\alpha
\right)
```

とする。 Fourier モード $f_n(r)=e^{2\pi inr}$ に対し、$n\neq0$ なら

```math
A_Nf_n(r)
=
e^{2\pi inr}
\frac{
1-e^{2\pi inN\alpha}
}{
N
\left(
1-e^{2\pi in\alpha}
\right)
}
```

であり、$N\to\infty$ で $r$ に一様に零へ収束する。$n=0$ では1である。三角多項式近似により、任意の連続 $f$ について

```math
A_Nf(r)
\longrightarrow
\int_0^1f(s)\,ds
```

が一様に成立する。従って回転は一意エルゴード的である。

区間指示関数は端点で不連続だが、端点近傍を除いて上下から連続関数で挟める。よって任意の半開区間 $[a,b)$ について

```math
\lim_{N\to\infty}
\frac1N
\sum_{j=0}^{N-1}
\mathbf1_{[a,b)}
\left(
r+j\alpha
\right)
=
b-a
```

である。これを長さ $p_k$ の結果区間へ適用すると Born 型長期頻度を得る。

## B.9 無理数回転は混合的でない

Haar 空間上の非定数 Fourier モード $f_n$ に対し、

```math
f_n\circ R_\alpha^j
=
e^{2\pi inj\alpha}f_n
```

である。従って相関

```math
\int
f_n
\overline{f_n\circ R_\alpha^j}
\,dm
=
e^{-2\pi inj\alpha}
```

の絶対値は1のままで零へ収束しない。よって無理数回転は混合的でない。一意エルゴード性から長期平均は得られるが、独立同分布型の有限標本揺らぎは従わない。

## B.10 有限幅境界の測度上界

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

## B.11 高階数集団に必要な追加自由度

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

## B.12 4成分 Bell 重み

規格化反対称行列を

```math
\widehat\Xi_0
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

とする。$d=\alpha_x-\beta_y$ と置くと、回転の積を直接計算して

```math
R(\alpha_x)
\widehat\Xi_0
R(\beta_y)^{\mathsf T}
=
\frac1{\sqrt2}
\begin{pmatrix}
\sin d&\cos d\\
-\cos d&\sin d
\end{pmatrix}
```

を得る。成分の絶対値2乗は

```math
w_{++}=w_{--}
=
\frac12\sin^2d,
\qquad
w_{+-}=w_{-+}
=
\frac12\cos^2d
```

である。$\sin^2d=(1-\cos2d)/2$、$\cos^2d=(1+\cos2d)/2$ から

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos2d
\right]
```

が従う。また全成分の和は1である。

## B.13 局所 Haar 角の基準セクター

固定設定 $x$ に対し、$A_x(\phi_A)=\operatorname{sgn}\cos(\phi_A-2\alpha_x)$ の正負領域はそれぞれ長さ $\pi$ の半円である。従って

```math
P_0(A\mid x)
=
\frac12
```

である。B側も同様であり、$\phi_A,\phi_B$ の独立性から

```math
q_{AB}^{xy}
=
P_0(A,B\mid x,y)
=
\frac14
```

を得る。

未来角区間の長さが $w_{AB}^{xy}$ なので、積測度により

```math
\nu_{\rm B}^0
\left(
A,B,G
\mid
x,y
\right)
=
\frac14w_{AB}^{xy}
```

である。全結果の和と $\sum_{A,B}w_{AB}^{xy}=1$ から

```math
\nu_{\rm B}^0
\left(
G
\mid
x,y
\right)
=
\frac14
```

を得る。

## B.14 二側条件付けと設定分布保存

$d\mu_{\rm B}=4\mathbf1_G\,d\nu_{\rm B}^0$ とする。固定設定で

```math
P_{\mu_{\rm B}}(A,B\mid x,y)
=
\frac{
\nu_{\rm B}^0(A,B,G\mid x,y)
}{
\nu_{\rm B}^0(G\mid x,y)
}
=
w_{AB}^{xy}
```

である。また

```math
P_{\mu_{\rm B}}(x,y)
=
4\pi_x\pi_y
\nu_{\rm B}^0(G\mid x,y)
=
\pi_x\pi_y
```

なので、設定生成器の分布は保たれる。

## B.15 非信号周辺と測定設定独立性

余弦重みを一側で和を取ると、$B=\pm1$ の線形項が相殺して

```math
\sum_Bw_{AB}^{xy}
=
\frac12
```

となる。B側周辺も同様である。これは理想反対称源と共通基準密度に依存する。

一方、$d\mu_{\rm B}(\Lambda\mid x,y)=4\mathbf1_{G_{xy}}(\Lambda)d\nu_{\rm B}^0(\Lambda)$ であり、$G_{xy}$ は設定依存である。従って設定分布が保たれても、完全履歴の測定設定独立性は一般に成立しない。

## B.16 一般基準密度

付随自由度を含む基準測度が各結果セクター上で密度 $q_{AB}^{xy}$ を持つなら、

```math
\nu^0(A,B,G\mid x,y)
\propto
q_{AB}^{xy}K_{AB}^{xy}
```

である。条件付き規格化により

```math
P(A,B\mid x,y,G)
=
\frac{
q_{AB}^{xy}K_{AB}^{xy}
}{
\sum_{A',B'}
q_{A'B'}^{xy}K_{A'B'}^{xy}
}
```

を得る。$q_{AB}^{xy}$ が4結果で共通なら余弦則へ戻る。非共通補正は共同分布と周辺分布へ同時に入るため、完全模型では結果別密度を独立に検査する必要がある。
