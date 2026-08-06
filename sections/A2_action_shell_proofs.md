@number: A2
@chapter: 付録
@title: 母測度、作用選択器、履歴区間の証明
@status: 本文第1章、第4章、第5章で用いる母測度の条件付け、エルゴード頻度、作用区間選択、固定作用公式、共分散補正、任意有限基底、Bell履歴区間と基準セクター密度を補足する。不変母測度の力学的生成は仮定である。

## B.1 条件付き母測度

試行開始面を $(\Sigma_0,\mathcal B)$、母測度を $\mu_*$ とする。調製条件、プログラム、基底、Bell設定は全て $\mathcal B$ 可測な開始点の関数またはレジスター領域として扱う。

条件事象 $D\in\mathcal B$、$\mu_*(D)>0$ に対し、

```math
\mu_*^D(E)
=
\frac{
\mu_*(E\cap D)
}{
\mu_*(D)
}
```

とする。本文の $\mathbb E_{\mu_*}[\cdot\mid\mathcal P,M,U]$ は、連続レジスターでは正則条件付き分布、離散レジスターでは上の条件事象による期待値を表す。

相関行列は

```math
C_D(t)
=
\int_{\Sigma_0}
b_t(z)b_t(z)^\dagger
\,d\mu_*^D(z)
```

である。有限基底結果とBell結果も同じ $\mu_*^D$ の事象確率であるため、3つに独立な基礎測度を置かない。

## B.2 不変性とエルゴード頻度

周期写像 $\mathcal R$ が

```math
\mathcal R_*\mu_*
=
\mu_*
```

を満たし、$\mu_*$ に関してエルゴード的であると仮定する。Birkhoffのエルゴード定理により、$f\in L^1(\mu_*)$ に対して

```math
\frac1N
\sum_{n=0}^{N-1}
f\left(
\mathcal R^nz
\right)
\longrightarrow
\int f\,d\mu_*
```

が $\mu_*$ に関してほとんど確実に成立する。

事象 $E$ の指示関数を取れば

```math
\frac1N
\sum_{n=0}^{N-1}
\mathbf 1_E
\left(
\mathcal R^nz
\right)
\longrightarrow
\mu_*(E)
```

となる。条件事象 $D$ が正の測度を持ち、その出現回数が無限に増えるなら、比エルゴード定理または分子と分母への上式の適用により

```math
\frac{
\sum_{n=0}^{N-1}
\mathbf 1_{E\cap D}
\left(
\mathcal R^nz
\right)
}{
\sum_{n=0}^{N-1}
\mathbf 1_D
\left(
\mathcal R^nz
\right)
}
\longrightarrow
\mu_*(E\mid D)
```

を得る。これは設定対ごとのBell相対頻度に用いる。エルゴード性は本稿の仮定であり、以下の有限次元積分からは導かれない。

## B.3 作用区間選択

$I_k\geq0$、$I_{\rm ph}=\sum_kI_k>0$ とする。$\vartheta$ が $(I_1,\ldots,I_L)$ の下で $[0,2\pi)$ 上に条件付き一様であるとする。

```math
u
=
\frac{\vartheta}{2\pi}
I_{\rm ph},
\qquad
S_k
=
\sum_{j=1}^kI_j
```

とし、$E_k=\{S_{k-1}\leq u<S_k\}$ とする。

<!-- theorem-start:lemma -->
**補題（作用区間の条件付き確率）**

```math
P(E_k\mid I_1,\ldots,I_L)
=
\frac{I_k}{I_{\rm ph}}
```

が成立する。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明**
$u$ の条件付き密度は $1/I_{\rm ph}$ である。区間 $[S_{k-1},S_k)$ の長さが $I_k$ なので、積分は $I_k/I_{\rm ph}$ となる。
<!-- theorem-end:proof -->

$I_k=0$ の区間は空であり、正の確率を持たない。境界 $u=S_k$ の集合は、条件付き一様分布では零測度である。半開区間の選び方は確率を変えない。

## B.4 正準基底混合と固定作用公式

$b\in\mathbb C^L$、$U^\dagger U=I$ とし、

```math
I_k
=
\mathcal J_0
\left|
\left(Ub\right)_k
\right|^2,
\qquad
I_{\rm ph}
=
\mathcal J_0b^\dagger b
```

とする。ユニタリ性により $\sum_kI_k=I_{\rm ph}$ である。

条件付き相関行列を

```math
C_U
=
\mathbb E
\left[
bb^\dagger
\mid
U,\mathcal P,M=\mathsf{basis}
\right]
```

とする。$I_{\rm ph}=I_0$ がほとんど確実なら、

```math
\begin{aligned}
P_k
&=
\mathbb E
\left[
\frac{I_k}{I_0}
\right]
\\
&=
\frac{
\mathcal J_0
\mathbb E
\left|
\left(Ub\right)_k
\right|^2
}{
I_0
}
\\
&=
\frac{
\left(
UC_UU^\dagger
\right)_{kk}
}{
\operatorname{tr}C_U
}.
\end{aligned}
```

この導出は $C_U$ の階数を使わない。

## B.5 全作用変動の共分散恒等式

```math
r_k
=
\frac{I_k}{I_{\rm ph}}
```

とする。$I_k=I_{\rm ph}r_k$ なので、

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

である。従って、

```math
\mathbb E[r_k]
-
\frac{
\mathbb E[I_k]
}{
\mathbb E[I_{\rm ph}]
}
=
-
\frac{
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
}{
\mathbb E[I_{\rm ph}]
}
```

となる。固定作用は共分散を零にする十分条件である。独立性までは不要で、無相関でもよい。

## B.6 測定基底に依存しない調製

異なる $U$ に対する条件付き相関を $C_U$ とする。$C_U=C$ が全ての許容基底で成立するとき、固定作用公式は

```math
P_k(U)
=
\frac{
\left(
UCU^\dagger
\right)_{kk}
}{
\operatorname{tr}C
}
```

となる。

$C_U\neq C$ なら同じ代数は

```math
P_k(U)
=
\frac{
\left(
UC_UU^\dagger
\right)_{kk}
}{
\operatorname{tr}C_U
}
```

を与えるだけである。これは基底依存の調製集団に対する式であり、1つの状態 $C$ の測定基底を変えた結果とは呼べない。

## B.7 条件付き一様性からのずれ

理想条件付き角分布を $m(d\vartheta)=d\vartheta/(2\pi)$、実分布を $\rho_{b,U}(d\vartheta)$ とする。任意の区間事象 $E_k$ に対して、全変動距離の定義から

```math
\left|
\rho_{b,U}(E_k)
-
m(E_k)
\right|
\leq
d_{\rm TV}
\left(
\rho_{b,U},m
\right)
```

である。母測度で平均すれば、

```math
\left|
P_k^{\rm real}
-
P_k^{\rm ideal}
\right|
\leq
\mathbb E
\left[
d_{\rm TV}
\left(
\rho_{b,U},m
\right)
\right]
```

を得る。周辺角分布の全変動距離ではなく、$(b,U,\mathcal P)$ で条件付けた距離を使う必要がある。

## B.8 有限幅比較器

理想境界集合を

```math
\mathcal D
=
\bigcup_{k=1}^{L-1}
\{u=S_k\}
```

とする。有限幅比較器が理想結果と異なり得る領域を

```math
\mathcal D_w
=
\left\{
\min_k
\left|u-S_k\right|
\leq w
\right\}
```

へ限定できるなら、結合不等式により理想分布と実分布の全変動距離は

```math
d_{\rm TV}
\leq
\mu_*(\mathcal D_w)
```

で抑えられる。

条件付き $u$ 密度が $M_u$ 以下なら、粗い上界として

```math
\mu_*(\mathcal D_w)
\leq
2(L-1)M_uw
```

を得る。ただし、境界が接近または重複する場合は過大評価である。有限装置では二重ラッチ、無結果、比較順序依存も別に測る。

## B.9 Bell枝区間

固定設定 $(x,y)$ で、4つの非負枝作用 $K_{AB}^{xy}$ が

```math
\sum_{A,B}
K_{AB}^{xy}
=
\mathcal K
```

を満たすとする。$u_{\rm B}$ を $[0,\mathcal K)$ 上の一様変数とし、区間 $\mathcal I_{AB}^{xy}$ の長さを $K_{AB}^{xy}$ とする。

Bell側では $(A,B)$ が先に局所記録されるため、区間は結果生成に使わない。候補完結履歴の結果セクターを固定した後、

```math
G_{AB}^{xy}
=
\left\{
u_{\rm B}
\in
\mathcal I_{AB}^{xy}
\right\}
```

を整合条件とする。

## B.10 基準セクター密度を含む Bell公式

選択器座標を除く候補履歴変数を $\zeta$ とする。固定設定と結果セクターで、候補 Liouville 基準要素が

```math
d\nu_{AB}^{xy}
=
q_{AB}^{xy}
d\bar\nu_{AB}^{xy}(\zeta)
\frac{du_{\rm B}}{\mathcal K},
\qquad
\int
d\bar\nu_{AB}^{xy}
=
1
```

と分解できるとする。$q_{AB}^{xy}$ は選択器以外の密度と体積を全て含む。

整合事象の基準質量は

```math
\nu_{AB}^{xy}
\left(
G_{AB}^{xy}
\right)
=
q_{AB}^{xy}
\frac{K_{AB}^{xy}}{\mathcal K}
```

である。全4セクターを合わせて規格化すると、

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

を得る。

<!-- theorem-start:corollary -->
**系（共通基準密度）**
$q_{AB}^{xy}=q^{xy}$ が4結果で共通なら、

```math
P(A,B\mid x,y,G)
=
\frac{K_{AB}^{xy}}{\mathcal K}
```

である。
<!-- theorem-end:corollary -->

この系は共通性を導くものではない。$q_{AB}^{xy}$ が不均等なら、一様なBell境界角だけでは余弦共同確率を得られない。

## B.11 全試行監査と再初期化

母測度確率を実験頻度と比較するには、次を監査する。

1. 各開始点がほとんど確実に有限時間で次の開始面へ戻る。
2. 1周期で結果レジスターが高々1回だけ確定する。
3. 比較境界への複数回交差を重複計数しない。
4. 基底、設定、結果に応じて失敗周期を捨てない。
5. 開始数、設定生成数、局所記録数、比較完了数、外部記録数、再帰数を照合する。
6. Bell側で整合しない周期を観測後に捨てない。
7. 外部記録と不要情報を含む拡大全系の写像を1対1に保つ。

異なる結果履歴を外部記録ごと同じ点へ押しつぶす多対1写像は Hamiltonian ではない。結果情報は外部記録、不要情報モード、仕事源、環境のいずれかへ残す必要がある [17,18]。
