@number: 4
@chapter: 本文
@title: 二側短記憶極限、Fisher 応力、中心閉鎖予想
@status: 二側 Markov 拡散を仮定した後の浸透速度と Fisher 応力は厳密結果である。ミクロ誘導場からその拡散と応力へ至る縮約は中心的な予想・未解決である。

## 4.1 二側条件付き過程と Markov 性

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

## 4.2 前進・後退流れ

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

## 4.3 時間対称平均加速度

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

## 4.4 Fisher 情報と応力

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

## 4.5 Fisher 閉鎖予想

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

## 4.6 無次元化した目標誤差

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

## 4.7 Gauss 幅における Routh–Fisher 一致

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

## 4.8 補助的な線形 Gauss 型作用定理

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

## 4.9 導出状態

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

## 4.10 本章の結論

二側 Markov 拡散が得られれば、浸透速度、Fisher 情報、Bohm–Fisher 応力、Nelson 作用の関係は厳密に整理できる。Gauss 幅族では、固定内部作用の Routh 縮約が Fisher 項と一致する。

未完成なのは、その構造をミクロ Hamiltonian から得る中央の縮約である。本論文は、正確なミクロ運動量収支と Fisher 応力の間を **Fisher 閉鎖予想** として明示し、自己共役性または弱漏れだけで解決済みとは扱わない。
