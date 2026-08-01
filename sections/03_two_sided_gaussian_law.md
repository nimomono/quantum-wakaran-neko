@number: 3
@chapter: 本文
@title: Liouville モーメント式と誘導場の消去
@status: 拡大全系の Liouville 方程式から連続の式と運動量収支を厳密に導き、線形誘導場を指定した境界条件の下で Green 作用素により消去する。Fisher 応力への閉鎖はまだ置かない。

## 3.1 拡大全系の Liouville 密度

外部自由度と仕事貯蔵自由度まで含む全位相点を

```math
Z
=
(X,P,Q,\Pi,Y,\Theta,z_{\rm work})
```

とする。全 Liouville 密度を $\varrho_N(Z,t)$ と書く。正規化を

```math
\int \varrho_N(Z,t)\,\mathrm dZ=1
```

とする。

全 Hamiltonian $H_N^{\rm all}$ に対して

```math
\partial_t\varrho_N
+
\{\varrho_N,H_N^{\rm all}\}
=0
```

が成立する。弱漏れの外部振動子を含める場合も、密度はそれらの座標を含む全位相空間上で定義する。有限部分の変数だけに摩擦付き Liouville 方程式を置くことは、外部消去後の別の近似である。

## 3.2 配置密度と条件付き平均

粒子の配置密度を

```math
\rho_N(x,t)
=
\int
\varrho_N(Z,t)
\,\mathrm dP\,\mathrm dQ\,\mathrm d\Pi
\,\mathrm dY\,\mathrm d\Theta\,\mathrm dz_{\rm work}
```

とする。$X=x$ を固定した条件付き平均を

```math
\mathbb E_N[A\mid X=x]
=
\frac1{\rho_N(x,t)}
\int
A(Z)
\varrho_N(Z,t)
\,\mathrm dP\,\mathrm dQ\,\mathrm d\Pi
\,\mathrm dY\,\mathrm d\Theta\,\mathrm dz_{\rm work}
```

と定義する。$\rho_N=0$ の点では局所式を用いない。

平均運動量と平均速度を

```math
\overline P_N(x,t)
=
\mathbb E_N[P\mid X=x],
\qquad
v_N(x,t)
=
\frac{\overline P_N(x,t)}m
```

とする。運動量共分散は

```math
\Sigma_{p,N}(x,t)
=
\mathbb E_N
\left[
(P-mv_N)
\otimes
(P-mv_N)
\mid X=x
\right].
```

誘導場の粒子への反作用を

```math
F_{{\rm G},N}(Z)
=
\left[\nabla G_N(X)\right]^{\mathsf T}
B^{\mathsf T}Q
-
\nabla_XH_N^{\rm nl}
```

とし、条件付き平均を

```math
\overline F_{{\rm G},N}(x,t)
=
\mathbb E_N
\left[
F_{{\rm G},N}
\mid X=x
\right]
```

とする。

## 3.3 0次モーメント

Liouville 方程式を粒子運動量と全内部変数について積分する。境界項が消える減衰条件、周期境界、または無流束境界を仮定すると、

```math
\partial_t\rho_N
+
\nabla_x\cdot
\left(
\frac1m
\rho_N\overline P_N
\right)
=0
```

を得る。従って

```math
\partial_t\rho_N
+
\nabla_x\cdot(\rho_Nv_N)
=0.
```

これは外部交換を含む拡大全系でも正確である。外部交換は条件付き平均 $v_N$ の時間発展へ入るが、粒子数を作成・消滅しない限り連続の式の形を変えない。

## 3.4 1次モーメント

Liouville 方程式へ $P_i$ を掛けて積分すると、

```math
\partial_t
\left(
\rho_N\overline P_{N,i}
\right)
+
\partial_{x_j}
\left[
\frac{\rho_N}{m}
\mathbb E_N
\left(
P_iP_j\mid X=x
\right)
\right]
=
-\rho_N\partial_{x_i}V
+
\rho_N\overline F_{{\rm G},N,i}
```

を得る。添字 $j$ について和を取る。

2次モーメントを

```math
\mathbb E_N
\left[
P\otimes P\mid X=x
\right]
=
m^2v_N\otimes v_N
+
\Sigma_{p,N}
```

と分解し、連続の式を使うと、

<!-- theorem-start:proposition -->
**命題（正確な粒子運動量収支）**

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

<!-- theorem-end:proposition -->

この式は閉鎖近似を含まない。誘導場反作用と粒子運動量流束を分けて保持することが重要である。どちらか一方だけを Fisher 応力と同定してはならない。

## 3.5 枝内部幅と枝間流束

場の射影 $P_{\rm c},P_\perp$ は、粒子運動量共分散を自動的に分解しない。位相整合した局所枝を表す離散または連続指標を $\alpha$ とし、条件付き全分散公式を使う。

<!-- theorem-start:proposition -->
**命題（条件付き全分散分解）**

```math
\Sigma_{p,N}(x,t)
=
\mathbb E_N
\left[
\operatorname{Var}_N(P\mid X=x,\alpha)
\mid X=x
\right]
+
\operatorname{Var}_N
\left(
\mathbb E_N[P\mid X=x,\alpha]
\mid X=x
\right).
```

<!-- theorem-end:proposition -->

第1項は枝内部の運動量幅、第2項は枝中心間の流束である。どちらを欠陥、どちらを位相整合成分と呼べるかは、$\alpha$ のミクロな定義と時間尺度に依存する。

第2項を単に捨てると、枝間の位相整合運動量流束まで失う。第1項を常に零と置くと、有限温度、有限分解能、局所非線形性の影響を隠す。Fisher 閉鎖では、両項と誘導場反作用を合わせて評価する。

## 3.6 線形誘導場の初期値消去

$H_N^{\rm nl}=0$ とする。場方程式は

```math
\ddot Q(t)
+
K_NQ(t)
=
BG_N(X(t))
+
F_{\rm ext}(t)
```

である。$F_{\rm ext}$ は外部自由度を明示したままなら決定論的な Hamiltonian 力であり、外部集団について条件付けまたは平均した後には有効雑音として現れ得る。

$\Omega_N=K_N^{1/2}$ とすると、初期値問題の解は

```math
Q(t)
=
\cos(\Omega_Nt)Q(0)
+
\Omega_N^{-1}
\sin(\Omega_Nt)\Pi(0)
+
\int_0^t
\Omega_N^{-1}
\sin
\left[
\Omega_N(t-s)
\right]
\left[
BG_N(X(s))+F_{\rm ext}(s)
\right]
\,\mathrm ds.
```

これを $F_{{\rm G},N}$ へ代入すると、粒子は

1. 初期場に由来する自由反作用、
2. 自己履歴に依存する有限記憶項、
3. 外部流路から伝わる駆動、

を受ける。有限 $N$ では記憶核は準周期的であり、長時間には再帰を持つ。

## 3.7 二側境界条件での消去

場の境界条件を線形作用素 $\mathcal C_0Q(0)+\mathcal D_0\dot Q(0)=q_0$ と $\mathcal C_TQ(T)+\mathcal D_T\dot Q(T)=q_T$ で指定する。境界値問題が一意可解なら、

```math
Q(t)
=
Q_{\rm bd}(t)
+
\int_0^T
\mathcal G_N(t,s)
\left[
BG_N(X(s))+F_{\rm ext}(s)
\right]
\,\mathrm ds
```

と書ける。$\mathcal G_N$ は指定した境界条件に対応する Green 核、$Q_{\rm bd}$ は非同次境界データだけで決まる解である。

境界条件が場作用素の自己共役領域を定めるなら、

```math
\mathcal G_N(t,s)
=
\mathcal G_N(s,t)^{\mathsf T}
```

となる。従って消去後の履歴作用は時間交換に対して対称になる。

しかし、Green 核の自己共役性だけから

```math
\frac12
\left(
D_+D_-+D_-D_+
\right)X
```

という Nelson の平均加速度は導けない。一般には、非局所記憶、質量繰り込み、境界層、外部交換による反対称部分が残る。

## 3.8 条件付き平均反作用

二側消去式を使うと、条件付き平均反作用は概念的に

```math
\overline F_{{\rm G},N}(x,t)
=
F_{{\rm bd},N}(x,t)
+
\int_0^T
\mathbb E_N
\left[
\mathcal K_N
\left(
x,t;X(s),s
\right)
\mid X(t)=x
\right]
\,\mathrm ds
+
F_{{\rm ext},N}(x,t)
```

と書ける。$\mathcal K_N$ は $\nabla G_N$、$B$、$\mathcal G_N$ から決まる記憶核である。

この式は、反作用が一般に現在密度 $\rho_N(x,t)$ だけの局所汎関数ではないことを示す。Fisher 応力のような局所密度汎関数へ閉じるには、短記憶化、条件付き局所平衡、枝分解、外部交換の誤差評価が必要である。

## 3.9 正確な式と縮約仮説の境界

| 主張 | 導出状態 |
|---|---|
| 全 Liouville 方程式 | 定義した全 Hamiltonian に対する厳密結果 |
| 連続の式 | 厳密結果 |
| 運動量モーメント式 | 厳密結果 |
| 条件付き全分散分解 | 厳密結果 |
| 線形場の初期値消去 | 指定した初期条件の下で厳密結果 |
| 線形場の二側 Green 消去 | 一意可解な指定境界条件の下で厳密結果 |
| 自己共役 Green 核の時間交換対称性 | 自己共役境界条件の下で厳密結果 |
| 記憶核の Markov 化 | 予想・未解決 |
| 二側条件付き過程の共通拡散係数 | 予想・未解決 |
| 反作用と運動量流束の Fisher 閉鎖 | 中心的な予想・未解決 |

## 3.10 本章の結論

誘導場と外部流路を含む全 Liouville 密度から、粒子の連続の式と運動量収支を正確に得た。粒子が受ける有効応力の候補は、誘導場の条件付き平均反作用と運動量共分散の発散の組合せである。

線形誘導場は Green 作用素で消去できるが、一般には非局所記憶が残る。時間対称な Green 核は二側縮約の必要な構造を与えるが、Nelson の Markov 拡散または Fisher 応力を単独では強制しない。
