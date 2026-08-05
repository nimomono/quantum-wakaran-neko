@number: A2
@chapter: 付録
@title: 一般作用殻、余面積公式、入口流束の詳細
@status: 第4章と第5章で用いる2モード作用殻容量、排他的境界面、余面積 Jacobian、作用分配次元、殻接方向混合を補足し、正規化された混合集団と未規格化殻容量を区別する。

## B.1 単体積分

作用殻容量を

```math
\Omega_n(A)
=
(2\pi)^n
\int_{J_k\geq0}
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n dJ_k
```

とする。$n=1$ では

```math
\Omega_1(A)
=
2\pi.
```

再帰関係

```math
\Omega_n(A)
=
2\pi
\int_0^A
\Omega_{n-1}(A-J_n)
\,dJ_n
```

を用いると、

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
A^{n-1}
```

が帰納的に従う。

## B.2 排他的な和と直積の違い

位置チャンネルを排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とすれば、全入口流束は

```math
\mathscr F
=
\sum_i\mathscr F_i
```

であり、各 $\mathscr F_i$ に局所作用 $A_i$ の線形因子が残る。

一方、全セルに独立な2モード作用殻を同時に課す直積構成では、容量は

```math
\prod_i\Omega_2(A_i)
\propto
\prod_iA_i
```

となる。1つのチャンネル $i$ を選ぶ相対重みではなく、全セル作用の積が現れる。この構成は位置の Born 型入口頻度を与えない。

## B.3 coarea公式

全入口正準位相空間を $\Gamma$、基準体積を $d\Gamma$ とする。固定作用制約と反応面制約を

```math
F_1(z)
=
A_i-K_i-I,
```

```math
F_2(z)
=
s_i(z)
```

とする。正方向流束は記号的に

```math
\mathscr F_i
=
\int_\Gamma
\rho_0(z)
\delta(F_1)
\delta(F_2)
\left(
\dot s_i
\right)_+
d\Gamma.
```

一般の滑らかな写像 $F=(F_1,F_2)$ に対し、coarea公式は

```math
\int_\Gamma
g(z)
\delta(F(z))
d\Gamma
=
\int_{F^{-1}(0)}
\frac{g(z)}{J_F(z)}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

従って共通流束因子には、$\dot s_i$ だけでなく $J_F^{-1}$、初期密度、解多重度、spectator体積が含まれる。

## B.4 2モード殻の明示積分

理想作用角座標では、

```math
\int_0^\infty dK
\int_0^\infty dI
\,
\delta(A-K-I)
=
\int_0^A dK
=
A.
```

角積分を加えると、

```math
\Omega_2(A)
=
(2\pi)^2A.
```

入口法線速度と spectator因子が作用分配座標 $(K,I)$ に依存しない理想模型では、流束はこの容量に比例する。

## B.5 有限入口幅

デルタ関数の代わりに偶関数窓

```math
K_{\delta_A}(y)
=
\frac1{\delta_A}
K
\left(
\frac y{\delta_A}
\right),
```

```math
\int K(y)\,dy=1,
\qquad
\int yK(y)\,dy=0
```

を用いる。理想2モード容量は $A$ に線形なので、窓が $A=0$ の端へ触れず、他の因子が一定なら、対称な有限幅平均は線形重みを変えない。

一般の滑らかな流束因子 $g(A)$ を含むと、

```math
\mathscr F_i^{(\delta_A)}
=
\mathscr F_i^{(0)}
+
O
\left(
\delta_A^2
\sup
\left|
\partial_A^2
\left[
Ag(A)
\right]
\right|
\right).
```

殻端の切断、非対称窓、結果依存幅では1次誤差が現れ得る。

## B.6 作用分配方向の数

活性モード $K$ と $q$ 個の明反応作用 $I_1,\ldots,I_q$ が

```math
K+\sum_{\alpha=1}^qI_\alpha
=
A
```

を分配すると、

```math
\int_{K,I_\alpha\geq0}
\delta
\left(
A-K-\sum_\alpha I_\alpha
\right)
dK
\prod_\alpha dI_\alpha
=
\frac{A^q}{q!}.
```

従って線形則には $q=1$ が必要である。$q>1$ の追加明モードを導入しながら線形 Born 型重みを保つには、それらを直接作用分配から外し、共通 spectator因子にしなければならない。

## B.7 殻接方向 Hamiltonian

$n$モード複素ベクトル $a$ と Hermitian 行列 $T_\alpha$ に対し、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を生成子とする。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とすれば、

```math
\dot a
=
-iT_\alpha a,
```

```math
\left\{
a^\dagger a,
L_\alpha
\right\}
=
0.
```

従って

```math
H_{\rm mix}
=
\varepsilon
\sum_\alpha
\xi_\alpha(z_{\rm D})
L_\alpha
```

は総作用殻に接する Hamiltonian 混合を与える。

暗モードの相関が短く、生成子方向が等方なら、弱結合縮約は概念的に

```math
\mathcal L_{\rm eff}
=
D
\sum_\alpha
X_{L_\alpha}^2
```

となる。現行模型で用いる2モード全殻では $U(2)$ の Casimir型拡散に対応する。有限暗モードからこの生成子を一様誤差付きで導くことは未完成である。

## B.8 Born側とBell側の2モード殻

| 用途 | 全殻 | 比較する量 | 線形因子 |
|---|---|---|---|
| Born 型位置入口 | 活性＋共有明反応座標の2モード殻 | 位置sectorごとの全殻容量 | $A_i$ |
| Bell 型共同統計 | 実部＋虚部の比較2モード殻 | 結果sectorごとの全殻容量 | $A_\partial^{AB}$ |

両者は同じ2モード全殻の線形容量を使う。違いは、Born 側の総作用が局所場強度 $A_i=A_{\rm tot}r_i^2\Delta V$ で決まり、Bell 側の総作用が比較読み出し $A_\partial^{AB}=\Gamma^2K_{AB}/2$ で決まる点にある。

## B.9 正規化された混合集団と殻容量

固定sector $\lambda$ の正規化測度を $\mu_\lambda$、正準写像を $\mathcal U_\lambda$ とする。押し出し測度は

```math
\mu_\lambda'
=
\left(
\mathcal U_\lambda
\right)_*
\mu_\lambda
```

である。

<!-- theorem-start:proposition -->
**命題（正準混合によるsector質量保存）**
正準写像がsector $\Gamma_\lambda$ を自身へ写すなら、

```math
\mu_\lambda'
\left(
\Gamma_\lambda
\right)
=
\mu_\lambda
\left(
\Gamma_\lambda
\right).
```

特に $\mu_\lambda$ が規格化されていれば、$U(2)$ 混合後もsector総質量は1であり、$\Omega_2(A_\lambda)$ には比例しない。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
押し出し測度の定義から、

```math
\mu_\lambda'
\left(
\Gamma_\lambda
\right)
=
\mu_\lambda
\left(
\mathcal U_\lambda^{-1}
\Gamma_\lambda
\right).
```

$\mathcal U_\lambda^{-1}\Gamma_\lambda=\Gamma_\lambda$ を用いる。
<!-- theorem-end:proof -->

一方、未規格化 Liouville 殻容量は

```math
\Omega_2(A_\lambda)
=
\int
\delta
\left(
A_\lambda-J_1-J_2
\right)
d\Gamma
```

であり、異なる半径の殻を同じ密度で数えるときの測度である。従って、容量比例頻度には、sectorごとに別々に規格化した集団ではなく、全sectorへ共通の境界密度または流束を置く必要がある。

## B.10 流束規格化と全試行監査

位置入口または Bell 結果の確率を

```math
P_\lambda
=
\frac{\mathscr F_\lambda}{\sum_{\lambda'}\mathscr F_{\lambda'}}
```

と定義するには、分母が全開始試行の入口通過を数えなければならない。次を監査する。

1. 各開始試行は高々1つの排他的境界面を正方向に横切る。
2. 境界へ到達しない試行を無言で除外しない。
3. 複数回交差を1試行としてどう数えるかを固定する。
4. 結果別に異なる停止時間または滞在時間を頻度へ重複計上しない。
5. 記録失敗、再埋め込み失敗、再初期化失敗を結果依存に捨てない。
6. 局所記録数、比較完了数、外部記録数、reset完了数を結果別に監査する。
7. Bell 側では設定生成に失敗した周期も無言で除外しない。

これらを満たさなければ、作用殻容量が正しくても実験の無条件頻度にはならない。数学的な境界測度が全履歴を数えることと、実験準備がその測度を事後選別なしで生成することは別である。

## B.11 再埋め込み写像に必要な保存量

標本化後の状態を $z_{\rm post}$、次試行の準備面を $\Gamma_{\rm prep}$ とする。理想的な再埋め込み写像

```math
\mathcal U_{\rm reset}:
z_{\rm post}
\longmapsto
z_{\rm next}\in\Gamma_{\rm prep}
```

は、拡大全系で正準かつ1対1でなければならない。結果情報を消去する場合、その情報とエントロピーは仕事源または外部自由度へ移す必要がある [17,18]。

有限装置部分だけで

```math
z_{\rm post}
\longmapsto
z_{\rm ref}
```

という多対1写像を置くことは Hamiltonian ではない。記録、garbage、外部仕事自由度を含む拡大全系で可逆に実装し、有限部分の復元だけを縮約として得る必要がある。
