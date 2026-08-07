@number: A1
@chapter: 付録
@title: 正準位相担体、相関行列、階数1因子の証明
@status: 本文第2章と第3章で用いる複素正準表示、相関行列発展、相関スペクトル保存、階数1の同値条件、共通源準備、階数1因子、近似階数1の節上界を有限次元で証明する。

## A.1 複素正準座標

実正準対 $(Q_i,P_i)$ と固定作用尺度 $\mathcal J_0>0$ に対し、

```math
b_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}},
\qquad
b_i^*
=
\frac{Q_i-iP_i}{\sqrt{2\mathcal J_0}}
```

とする。直接計算により

```math
\left\{b_i,b_j\right\}
=
0,
\qquad
\left\{b_i^*,b_j^*\right\}
=
0,
```

```math
\left\{b_i,b_j^*\right\}
=
-
\frac{i}{\mathcal J_0}
\delta_{ij}
```

を得る。

実関数 $H(b,b^*)$ に対する Hamilton 方程式は

```math
\dot b_i
=
-
\frac{i}{\mathcal J_0}
\frac{\partial H}{\partial b_i^*}
```

である。$H=b^\dagger hb$ なら $\partial H/\partial b^*=hb$ なので、

```math
i\mathcal J_0\dot b
=
hb
```

となる。

## A.2 実2次 Hamiltonian の表示

$h=A+iB$ と分ける。 Hermitian 条件から

```math
A^{\mathsf T}=A,
\qquad
B^{\mathsf T}=-B
```

である。$Q=(Q_1,\ldots,Q_L)^{\mathsf T}$、$P=(P_1,\ldots,P_L)^{\mathsf T}$ とすると、

```math
b^\dagger hb
=
\frac1{2\mathcal J_0}
\left[
Q^{\mathsf T}AQ
+
P^{\mathsf T}AP
-
2Q^{\mathsf T}BP
\right]
```

である。右辺は実正準変数の通常の2次 Hamiltonian である。$h$ が実対称なら $B=0$ で、$Q$ と $P$ に同じ2次形式が作用する。

## A.3 共通回転と全位相作用

全位相作用を

```math
I_{\rm ph}
=
\frac12
\left(
Q^{\mathsf T}Q
+
P^{\mathsf T}P
\right)
=
\mathcal J_0b^\dagger b
```

とする。Poisson 括弧は

```math
\left\{b_i,I_{\rm ph}\right\}
=
-ib_i
```

なので、$I_{\rm ph}$ は共通位相回転を生成する。

$H=b^\dagger hb$ に対し、

```math
\left\{I_{\rm ph},H\right\}
=
0
```

である。従って、時間依存 $h(t)$ であっても共通回転対称性が保たれる限り $I_{\rm ph}$ は保存される。

## A.4 相関行列方程式

各試行で

```math
i\mathcal J_0\dot b^\omega
=
h(t)b^\omega
```

とする。積を微分すると、

```math
\begin{aligned}
i\mathcal J_0
\frac{d}{dt}
\left(
b^\omega
\left(b^\omega\right)^\dagger
\right)
={}&
h
b^\omega
\left(b^\omega\right)^\dagger
\\
&-
b^\omega
\left(b^\omega\right)^\dagger
h
\end{aligned}
```

となる。調製条件 $\mathcal P$ と観測プログラム $M$ を固定した集団測度を $\mu_{\mathcal P,M}$ とする。同じ集団の全試行が共通の $h(t)$ に従い、条件が観測窓で固定され、微分と平均を交換できるなら、

```math
i\mathcal J_0\dot C
=
\left[h,C\right]
```

を得る。ここで

```math
C(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
b_t b_t^\dagger
\right]
```

である。周期測度の不変性またはエルゴード性は、この有限時間微分の代数には不要である。第4章では固定プログラムについて周期測度を明示するが、一般の相関集団を同じ周期へ統合したとはしない。

## A.5 相関スペクトルの保存

時間発展作用素 $U$ は

```math
i\mathcal J_0\dot U
=
hU,
\qquad
U(t_0)=I
```

を満たす。$h=h^\dagger$ なら

```math
\frac{d}{dt}
\left(U^\dagger U\right)
=
0
```

なので $U$ はユニタリである。相関行列は

```math
C(t)
=
U(t,t_0)
C(t_0)
U(t,t_0)^\dagger
```

となる。

従って、任意の正整数 $n$ に対し

```math
\operatorname{tr}C(t)^n
=
\operatorname{tr}C(t_0)^n
```

である。有限次元では固有値の全対称多項式が保存されるため、固有値の多重集合、階数、純度が保存される。

## A.6 階数1相関なら共通射影方向

$C=\Lambda\chi\chi^\dagger$、$\Lambda>0$、$\chi^\dagger\chi=1$ とする。$\chi$ と直交する任意の $v$ に対し、

```math
0
=
v^\dagger Cv
=
\mathbb E
\left[
\left|v^\dagger b\right|^2
\right]
```

である。非負確率変数の平均が零なので、

```math
v^\dagger b^\omega
=
0
```

がほとんど確実に成立する。

有限次元直交補空間の正規直交基底 $v_2,\ldots,v_L$ を取ると、全てについて同時に上式が成立する確率1の集合を取れる。従って

```math
b^\omega
=
c^\omega\chi
```

がほとんど確実に成立する。ここで $c^\omega=\chi^\dagger b^\omega$ である。さらに

```math
C
=
\mathbb E
\left|c^\omega\right|^2
\chi\chi^\dagger
```

なので $\Lambda=\mathbb E|c^\omega|^2$ である。

逆に $b^\omega=c^\omega\chi$ がほとんど確実なら、上式から $C$ は階数1である。これで本文第2.6節の同値条件が従う。

## A.7 共通源準備

入力が

```math
b_{\rm in}^\omega
=
c^\omega e_0
```

であり、準備回路 $U_{\rm prep}$ が $U_{\rm prep}e_0=\chi_0$ を満たすとする。線形性により

```math
b_{\rm out}^\omega
=
c^\omega\chi_0
```

である。従って

```math
C_{\rm out}
=
\mathbb E
\left|c^\omega\right|^2
\chi_0\chi_0^\dagger
```

となる。

$c^\omega=e^{i\beta^\omega}$ で $\beta^\omega$ が一様なら、

```math
\mathbb E
\left[b_{\rm out}^\omega\right]
=
0
```

であっても、

```math
C_{\rm out}
=
\chi_0\chi_0^\dagger
```

である。1次平均でなく2次相関を状態量に選ぶ理由がここにある。

## A.8 階数1因子の発展

$C=\Lambda\chi\chi^\dagger$、$\chi^\dagger\chi=1$ とし、$\Lambda$ は一定とする。交換子方程式へ代入すると、

```math
i\mathcal J_0
\left(
\dot\chi\chi^\dagger
+
\chi\dot\chi^\dagger
\right)
=
h\chi\chi^\dagger
-
\chi\chi^\dagger h
```

である。

左から $I-\chi\chi^\dagger$、右から $\chi$ を掛けると、

```math
\left(
I-\chi\chi^\dagger
\right)
\left(
i\mathcal J_0\dot\chi-h\chi
\right)
=
0
```

を得る。従って

```math
i\mathcal J_0\dot\chi
-
h\chi
=
\lambda(t)\chi
```

である。規格化を微分し、$h$ が Hermitian であることを用いると $\lambda(t)$ は実数となる。

位相変換

```math
\widetilde\chi(t)
=
\exp
\left[
\frac{i}{\mathcal J_0}
\int_{t_0}^t
\lambda(s)\,ds
\right]
\chi(t)
```

により、

```math
i\mathcal J_0
\dot{\widetilde\chi}
=
h\widetilde\chi
```

となる。

## A.9 近似階数1と節上界

$C$ の最大固有値を $\lambda_1$、単位主固有ベクトルを $\chi$ とする。スペクトル分解から

```math
C
=
\lambda_1\chi\chi^\dagger
+
E,
\qquad
E\geq0,
\qquad
E\chi=0
```

である。$\operatorname{tr}E=\operatorname{tr}C-\lambda_1$ なので、

```math
\varepsilon_{\rm rank}
=
\frac{\operatorname{tr}E}{\operatorname{tr}C}
```

となる。

任意のユニタリ $U$ と出力基底ベクトル $e_k$ に対し、$(U\chi)_k=0$ なら

```math
\begin{aligned}
p_k
&=
\frac{
e_k^\dagger UCU^\dagger e_k
}{
\operatorname{tr}C
}
\\
&=
\frac{
e_k^\dagger UEU^\dagger e_k
}{
\operatorname{tr}C
}
\\
&\leq
\frac{\left\|E\right\|_{\rm op}}{\operatorname{tr}C}
\leq
\frac{\operatorname{tr}E}{\operatorname{tr}C}
=
\varepsilon_{\rm rank}.
\end{aligned}
```

正半定値性が最後の不等式に必要である。

## A.10 閉包残差の上界

残差付き試行方程式

```math
i\mathcal J_0\dot b
=
hb+r
```

から

```math
D_C
=
\mathbb E
\left[
rb^\dagger-br^\dagger
\right]
```

を得る。任意の単位ベクトル $u,v$ に対し、

```math
\left|
u^\dagger
\mathbb E
\left[rb^\dagger\right]
v
\right|
\leq
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|b\right\|^2
\right)^{1/2}
```

なので、2項を合わせて

```math
\left\|D_C\right\|_{\rm op}
\leq
2
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|b\right\|^2
\right)^{1/2}
```

となる。これは残差の起源を導く式ではなく、試行残差から相関閉包誤差への伝播上界である。
