@number: 3
@chapter: 本文
@title: 前後両側から条件づけた線形 Gaussian 経路法則
@status: 有限分解能の終端記録を Gaussian Schur 補完として厳密に定義する。

## 3.1 なぜ有限分解能を用いるか

前章の $X_N$ に対し、初期側では Gaussian 準備分布を与え、終端側では測定装置が残す有限分解能の記録を条件として用いる。終端位置をデルタ関数で厳密固定すると、極限拡散の終端近傍で流れが特異になり、$C^1$ 評価に不要な境界層が生じる。実在する測定記録は有限分解能を持つため、本論文では正定値の読み出し雑音を含む条件づけを主定理に採用する。

時刻 $T$ の記録を

```math
Y=HX_N(T)+\varepsilon,
\qquad
\varepsilon\sim N(0,R),
\qquad
R\geq r_*I>0
```

とする。実際に得られた記録値を $y$ とする。この条件は、尤度

```math
L_R(x)
=
\exp\left[
-\frac12(Hx-y)^{\mathsf T}R^{-1}(Hx-y)
\right]
```

で経路を重みづけすることと同値である。

## 3.2 無条件 Gaussian 法則

有限 $N$ の平均と2時刻共分散を

```math
\mu_N(t)=\mathbb{E}[X_N(t)],
```

```math
C_N(s,t)
=
\mathbb{E}\left[
(X_N(s)-\mu_N(s))
(X_N(t)-\mu_N(t))^{\mathsf T}
\right]
```

とする。基本行列を使えば、平均は

```math
\mu_N(t)
=
\Phi(t,0)m_0
+\int_0^t\Phi(t,r)f(r)\,\mathrm{d} r
```

であり、共分散は初期共分散と有限 Fourier モードの寄与の和として書ける。

雑音を基底関数 $e_\alpha(t)$ と独立 Gaussian 係数 $\zeta_\alpha$ で

```math
\widetilde\eta_N(t)
=
\sum_{\alpha=0}^{2N}e_\alpha(t)\zeta_\alpha
```

と書けば、

```math
K_{N,\alpha}(t)
=
\int_0^t\Phi(t,r)e_\alpha(r)\,\mathrm{d} r
```

により

```math
C_N(s,t)
=
\Phi(s,0)P_0\Phi(t,0)^{\mathsf T}
+\sum_{\alpha=0}^{2N}
K_{N,\alpha}(s)K_{N,\alpha}(t)^{\mathsf T}
```

となる。この表示は、条件づけとパラメータ微分を有限行列計算へ帰着させる。

## 3.3 Schur 補完による条件付き平均と共分散

記録共分散を

```math
S_N
=
HC_N(T,T)H^{\mathsf T}+R
```

とする。$R\geq r_*I$ なので $S_N$ は一様に可逆である。

<!-- theorem-start:proposition -->
**命題（有限 Gaussian 条件づけ）**
条件 $Y=y$ の下で $X_N$ は Gaussian 過程のままであり、その平均と共分散は

```math
\mu_N^R(t)
=
\mu_N(t)
+C_N(t,T)H^{\mathsf T}S_N^{-1}
\left[y-H\mu_N(T)\right],
```

```math
C_N^R(s,t)
=
C_N(s,t)
-C_N(s,T)H^{\mathsf T}S_N^{-1}HC_N(T,t)
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
有限個の時刻 $t_1,\ldots,t_k$ を固定すると、$(X_N(t_1),\ldots,X_N(t_k),Y)$ は結合 Gaussian ベクトルである。結合共分散行列の $Y$ 成分に関する Schur 補完を取れば上式を得る。任意の有限時刻集合で整合するため、条件付き過程全体が定まる。
<!-- theorem-end:proof -->

条件付き共分散の第2項は、終端記録により減少した不確かさを表す。これは力ではない。ある経路が終端記録とどれだけ整合するかという統計的更新である。

この計算は、新しい種類の Gaussian 条件づけではない。有限次元の状態を拡大して Fourier 係数まで含めれば、固定区間の線形 Gaussian 平滑化と同じ Schur 補完になる [28]。経路測度の立場では相反過程および Schrödinger 橋の線形 Gaussian 部分に属し [15,26,27,37]、経路単位の Gaussian 条件づけとしても標準的に表せる [36]。本論文で必要なのは、この既知の条件づけを有限 Fourier 切断数 $N$ とパラメータ $\theta$ について一様に微分し、第4章の定量的 $C^1$ 評価へ接続することである。

## 3.4 パラメータ微分

$F_\theta$ の変分 $\delta F$ に対して基本行列の第1変分は

```math
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\,\mathrm{d} r
```

である。逆行列の微分

```math
D(S^{-1})[\delta S]
=
-S^{-1}(\delta S)S^{-1}
```

と合わせると、$\mu_N^R$、$C_N^R$ のパラメータ第1微分を明示できる。$S_N\geq r_*I$ により、条件づけの微分は $N$ に依存しない定数で制御される。

有限分解能 $R>0$ は、物理的に自然であるだけでなく、数学的にも重要である。$R=0$ で $H$ が全座標を固定すると、終端に近づくにつれて条件付き流れが $(T-t)^{-1}$ 型に発散し得る。点終端は $R\downarrow0$ の別極限として扱うべきであり、主定理には含めない。

## 3.5 極限拡散の条件付き流れ

$N\to\infty$ の無条件拡散を

```math
\,\mathrm{d} X_t=b(X_t,t)\,\mathrm{d} t+\sqrt{2\nu}\,\,\mathrm{d} W_t,
\qquad
b(x,t)=F(t)x+f(t)
```

とする。終端尤度の後方伝播を

```math
h_R(x,t)
=
\mathbb{E}\left[L_R(X_T)\mid X_t=x\right]
```

と置く。線形 Gaussian 系では $h_R$ は指数2次関数で正である。条件付き前進流れは Doob 変換により

```math
b_+^R(x,t)
=
b(x,t)+2\nu\nabla\log h_R(x,t)
```

となる [15,16]。$\nabla\log h_R$ は $x$ の1次式であるため、条件付き過程も線形 Gaussian である。

条件付き時刻密度を $\rho^R(x,t)$ とすると、後退流れは

```math
b_-^R(x,t)
=
b_+^R(x,t)-2\nu\nabla\log\rho^R(x,t)
```

である。そこで

```math
v^R
=
\frac{b_+^R+b_-^R}{2},
\qquad
u^R
=
\frac{b_+^R-b_-^R}{2}
=
\nu\nabla\log\rho^R
```

と定義する。$v^R$ は確率流の速度、$u^R$ は密度勾配に伴う浸透速度である。

## 3.6 自由系で現れる −1/<i>T</i>

$F=0$、$f=0$、$X_N(0)=x_0$ とし、終端を厳密に $X_N(T)=x_0$ へ固定する特殊な場合を考える。非零 Fourier モードは1周期積分すると零になるため、全期間変位を担うのは零周波数 $Z_0$ だけである。終端条件は $Z_0=0$ を意味する。従って条件付き雑音共分散は

```math
\mathbb{E}\left[
\widetilde\eta_N(t)
\widetilde\eta_N(s)^{\mathsf T}
\mid X_N(T)=x_0
\right]
=
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]I.
```

ここで初めて $-1/T$ が現れる。一般の $F\neq0$ では終端値は全 Fourier モードの線形結合に依存するため、条件付き修正は

```math
-\operatorname{Cov}(\widetilde\eta_N,Y)
\operatorname{Cov}(Y,Y)^{-1}
\operatorname{Cov}(Y,\widetilde\eta_N)
```

という流れ依存の Schur 補完であり、単純な $-1/T$ ではない。

## 3.7 前後両側条件づけの物理的意味

初期準備と終端記録の双方を知った後に、途中経路の統計を求めることは、通常の条件付き確率である。終端記録が途中経路の条件付き平均を変えることは、終端装置が過去へ力を送ることを意味しない。

ただし、条件付き経路分布を物理的試行頻度として採用するには、どの完結履歴へ確率を置くかという追加の物理原理が必要である。Gaussian Schur 補完は、記録を与えた後の条件付き法則を計算するが、その法則が実験の無条件頻度として選ばれることまでは証明しない。第II部ではこの役割を2境界統計原理 `[R]` として明示し、第4章の Nelson 作用極限からは導かない。

## 3.8 本章の結論

有限分解能の終端記録を用いれば、前後両側から条件づけた経路法則は通常の Gaussian Schur 補完として完全に定義できる。条件付き平均、共分散、そのパラメータ微分は一様に制御される。次章では、この安定性を用いて、有限浴の繰り込み済み作用とその第1変分を Nelson 極限へ移す。
