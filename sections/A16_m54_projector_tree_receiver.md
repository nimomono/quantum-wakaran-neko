@number: P
@chapter: 付録
@title: M54のR170駆動projector-tree receiver
@status: R181Dのraw容量、正則化殻、selector lock、可逆filter、radial-only repump、完全結果誤差、資源境界を証明する。旧aperture samplerは現行因果鎖に使わない。

## P.1 目的とnode状態

深さ $m$ の二分projector-treeを考える。node $u\in\{0,1\}^{k-1}$ の入力registerを $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

```math
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
```

nodeの完全物理状態には、信号 $Z_u$、raw容量pointer $J_{u,b}$、作用殻容量 $A_{u,b}^\delta$、selector位置とlock、filter work、radial-port環境、R162 collision履歴、外部recordを含める。解析上の条件付き確率をcontrollerへ書き込まない。

## P.2 Raw容量と正則化殻

raw容量は

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

であり、$J_\Sigma=\mathcal J_0Z_u^\dagger Z_u$ である。固定 $q_b>0$、$q_0+q_1=1$ と $\delta>0$ に対し、R164/R170へ渡す容量を

```math
A_{u,b}^\delta
=J_{u,b}+\delta q_bJ_\Sigma
```

とする。従って理想R170 nodeの枝確率は

```math
\pi_{u,b}^\delta
=
\frac{A_{u,b}^\delta}{A_{u,0}^\delta+A_{u,1}^\delta}
=
\frac{p_{u,b}+\delta q_b}{1+\delta},
\qquad
p_{u,b}=\frac{J_{u,b}}{J_\Sigma}.
```

raw容量と正則化容量の役割を分ける。$A^\delta$ は作用殻を非退化にするためだけに使い、希少枝判定は $J$ に対して行う。これにより正則化で人工的に生じた小枝を安全枝と誤認しない。

## P.3 除算を使わないcutoff

安全閾値を $\tau>0$、guard幅を $\gamma>0$ とする。比較器は

```math
J_{u,b}-(\tau\pm\gamma)J_\Sigma
```

の符号だけを読む。$J_{u,b}\geq(\tau+\gamma)J_\Sigma$ をaccept plateau、$J_{u,b}\leq(\tau-\gamma)J_\Sigma$ をreject plateau、中間を無反応guardとする。$p_{u,b}$ の除算、浮動小数点評価、状態依存clockは要らない。

深さ $m$ の理想Born treeで、$p_{u,b}<\tau+\gamma$ のedgeを通る葉の総確率は高々 $2m(\tau+\gamma)$ である。各nodeには子edgeが高々2本あり、prefix確率との積を同じlevelの全nodeで足すと、prefix確率の総和は1以下なのでlevelごとの寄与は高々 $2(\tau+\gamma)$ となる。

## P.4 Selector lockと可逆filter

branch selectorはR164の殻状態数とR161/R162の有限混合により形成し、R170のcollection窓で $b$ のplateauへ固定する。lock前にfilterを開かない。異なる $b$ のplateauとguard領域を互いに素に取り、外部record、selector、guard flagを含む拡大状態で枝の和を1対1に保つ。

signalとblank work上のfilterを

```math
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
```

とする。直交性から

```math
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I,
```

かつ

```math
F_{u,b}(Z_u,0)
=(P_{u,b}Z_u,P_{u,1-b}Z_u)
```

である。非選択成分を消去せずworkへ保持するので、filter自体はunitaryな実正準写像である。selector plateauを保持したままcontrolled-$F_{u,b}$ を作用すれば、異なる枝の像はselector座標で分離される。

## P.5 Filter誤差と条件付きray

理想選択成分を $v=P_{u,b}Z_u$、実装後を $\widetilde v$ とし、

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|.
```

accept plateauでは $\|v\|\geq\sqrt\tau\|Z_u\|$ である。$\eta_F<\sqrt\tau$ なら三角不等式と規格化写像のLipschitz評価から

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{2\eta_F}{\sqrt\tau-\eta_F}.
```

この $\tau^{-1/2}$ は安全枝を条件付けた解析誤差であり、controllerが $p_{u,b}$ を読み出す費用ではない。

## P.6 Radial-only repump

filter後のselected信号だけにR181Aの $\kappa=0$ portを開く。

```math
\dot Z=g(J_*-Z^\dagger Z)Z.
```

方向 $Z/\|Z\|$ は一定で、作用 $r=Z^\dagger Z$ は

```math
\dot r=2gr(J_*-r)
```

に従う。accept plateauでは $r(0)\geq\tau r_{\rm in}$ である。入力作用を固定compact区間 $r_{\rm in}\in[J_-,J_+]$ に保てば、目標相対動径誤差 $\eta_R$ に必要な時間は

```math
T_R
=
O\!\left(
\frac1{gJ_*}
\log\frac{J_+}{\tau J_-\eta_R}
\right).
```

$T_R$ は $\tau$ と安全集合から試行前に固定できる。未知の $p_{u,b}^{-1/2}$ を実装する状態依存squeezeではない。これは採用開放法則であり、厳密なsymplectic resetまたは無履歴逆掃除とは呼ばない。環境へ移った動径情報はspent側に残す。

## P.7 Telescopingと完全結果誤差

理想node kernelを $K_k$、実装kernelを $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

```math
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(h_{k-1},\cdot),
K_k(h_{k-1},\cdot)
\right)
\leq\bar\varepsilon_k
```

と仮定する。$\bar\varepsilon_k$ はR170選択、lock、controlled filter、radial repump、routeを各1回だけ数える。Markov kernelの縮約性とtelescopingから、node実装誤差は $\sum_k\bar\varepsilon_k$ 以下である。

正則化は各nodeで高々 $\delta/(1+\delta)$、raw cutoffとguardは全体で高々 $2m(\tau+\gamma)$ の質量を無反応へ送る。入力分布誤差を $\varepsilon_{\rm in}$ とすると

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+\frac{m\delta}{1+\delta}
+2m(\tau+\gamma)
+\sum_{k=1}^m\bar\varepsilon_k.
```

ここで $P_{\rm out}$ は通常の葉と無反応を同じ結果空間に持つ。成功葉だけを再規格化しない。

<!-- theorem-start:proof -->
**証明（R181D）**

P.2がR170 nodeの正則化枝確率を与える。P.3が除去質量、P.4が枝別の1対1 filter、P.5がselected ray誤差、P.6が固定時間repump、P.7のkernel telescopingが深さ $m$ の完全結果誤差を与える。理想kernelの積は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2}{\|Z_0\|^2}
```

と望遠鏡型に縮約する。以上を足して本文の評価を得る。
<!-- theorem-end:proof -->

## P.8 資源と反証条件

$m=n$、$\delta,\tau,\gamma,\bar\varepsilon_k=O(\epsilon/n)$ と選ぶ。R170の保守的混合時間、collision精度、radial時間を合わせると、逐次読出し時間は

```math
O\!\left(
\frac{n^2}{\epsilon}\log\frac n\epsilon
\right)
```

で抑えられる。作用殻stiffnessは $O(n^2/\epsilon^2)$、collision fluxは $O(\sqrt{n/\epsilon})$、barrier rangeは $O(\log(n/\epsilon))$ で足りる。指数的なsignal、work、history、cold、spent容量と総熱はQ2-4の許容受動資源へ計上する。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部controllerへ入力する。
2. selector lock前にfilterを開き、枝像が重なる。
3. cutoffに状態依存除算または指数精度を要する。
4. 非選択成分、collision履歴、radial環境を消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 深さ $n$ のnode誤差を多項式予算へ同時に収められない。

旧fixed-volume apertureおよびdyadic threshold tapeはこの証明に使わない。
