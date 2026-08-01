@number: 3
@chapter: 本文
@title: 配置流束、誘導場の正確な消去、速度記憶核
@status: 運動量結合した有限誘導場について、正確な配置流束、速度モーメント式、自由速度揺らぎと反作用記憶項の分離を導く。Brown 極限と配置変数だけの Markov 性は近似または予想・未解決である。

## 3.1 拡大全系の Liouville 密度

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

## 3.2 配置密度と正確な配置流束

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

## 3.3 0次モーメント

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

## 3.4 正準運動量と配置速度の1次モーメント

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

## 3.5 質量規格化した線形誘導場

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

## 3.6 初期値問題での正確な消去

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

## 3.7 自由速度揺らぎの相関

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

## 3.8 配置変位の拡散極限

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

## 3.9 二側境界条件での消去

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

## 3.10 正確な結果と縮約課題

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

## 3.11 本章の結論

運動量結合した誘導場では、配置流束は $P/m+C_N\Pi$ であり、場の揺らぎは粒子速度へ直接入る。線形誘導場の正確な消去により、自由速度揺らぎと反作用速度記憶項を分離した。

この変更により、Fisher 項を有限 $N$ の力密度閉鎖から直接作る必要はなくなる。代わりに、自由配置変位の Brown 極限、反作用記憶の局所化、配置変数だけの Markov 性を示す必要がある。有限浴は厳密な OU 浴でないため、結果は再帰前の有限観測窓における制御された近似として扱う。
