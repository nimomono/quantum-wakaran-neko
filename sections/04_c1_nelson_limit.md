@number: 4
@chapter: 本文
@title: 二側配置拡散、Fisher 項、時間対称動力学
@status: 配置変数の二側 Markov 拡散を仮定した後の浸透速度、Fisher 情報、量子ポテンシャルは厳密結果である。運動量結合した有限誘導場からの配置拡散極限と時間対称 Newton 則は独立した未解決問題である。

## 4.1 配置雑音を持つ位相空間極限

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

## 4.2 配置変数だけの二側 Markov 拡散

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

## 4.3 現在速度と浸透速度

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

## 4.4 Fisher 情報と量子ポテンシャル

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

## 4.5 時間対称 Newton 則は独立した主張である

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

## 4.6 局所的な Schrödinger 表示

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

## 4.7 配置拡散極限の誤差

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

## 4.8 Gauss 幅における Routh–Fisher 一致

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

## 4.9 補助的な線形 Gauss 型作用定理

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

## 4.10 導出状態

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

## 4.11 本章の結論

運動量結合した誘導場は、配置速度揺らぎを直接生む。この揺らぎの積分が Brown 運動へ近づき、配置変数だけの二側 Markov 拡散が得られれば、$u=\nu\nabla\log\rho$、Fisher 項、量子ポテンシャルは運動学的に厳密に従う。

従って旧稿の Fisher 力密度閉鎖は中心課題から外れる。残る中心課題は、配置拡散極限、$X$ 射影の Markov 性、反作用記憶と古典圧力の制御、時間対称 Newton 則である。配置拡散を得たことと動力学まで得たことを分けて扱う。
