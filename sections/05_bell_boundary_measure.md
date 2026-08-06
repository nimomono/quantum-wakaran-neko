@number: 5
@chapter: 本文
@title: Bell 余弦枝作用と設定条件付き履歴測度
@status: 反対称左右交差相関と局所回転からの余弦枝作用は補助模型内部で厳密である。Bell共同確率は、同じ不変母測度の設定条件付き完結履歴として定義する。余弦頻度には二側履歴整合、条件付き一様な境界角、4結果で共通な基準セクター密度が必要であり、その物理的生成は未完成である。

## 5.1 固定された左右位相担体モード

Bell 構成では、左右へ伝播する有限個の局在位相担体モードを基礎変数とする。2粒子配置空間上の場も、単粒子側の統計振幅 $\chi$ も局所 Hamiltonian へ追加しない。装置の組立時に固定した左右モードを

```math
z^A_{\mu r},
\qquad
z^B_{\nu r},
\qquad
\mu,\nu\in\{+,-\},
\qquad
r\in\{1,2\}
```

とする。$\mu,\nu$ は局所分析器の2出力、$r$ は2つの直交源チャンネルである。設定または結果ごとにモード基底を選び直さない。

左右モードの派生交差相関を

```math
\Xi_{\mu\nu}
=
\sum_{r=1}^2
\eta_r
z^A_{\mu r}
\left(
z^B_{\nu r}
\right)^*
```

と定める。$\Xi$ は独立した場でも新しい正準変数でもない。左右の基礎位相担体から計算される階数2以下の交差相関である。単粒子側の $C$ は正半定値 Hermitian 行列であるのに対し、$\Xi$ は一般に正半定値でも Hermitian でもない。両者を同じ相関行列として扱わない。

## 5.2 反対称源と局所分析器

理想源が準備する交差相関を

```math
\Xi_0
=
\sqrt{
\frac{\mathcal K}{2}
}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。これは2つの階数1交差項へ分解できるため、2つの直交源チャンネルで構成できる。有限 Hamiltonian 源が任意初期状態から $\Xi_0$ を反復準備することと、比較時刻まで相対位相を保つことは独立の準備問題である。

Bell設定を $x,y$、対応する局所モード角を $\alpha_x,\beta_y$ とする。左右の局所分析器は各側の基礎位相担体だけを

```math
z^{A,(r)}
\longmapsto
R(\alpha_x)
z^{A,(r)},
\qquad
z^{B,(r)}
\longmapsto
R(\beta_y)
z^{B,(r)}
```

と回転する。ここで

```math
R(\theta)
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}
```

である。交差相関表示は

```math
\Xi(x,y)
=
R(\alpha_x)
\Xi_0
R(\beta_y)^{\mathsf T}
```

となるが、物理的に回すのは空間的に分離した左右の局所モードである。

## 5.3 余弦枝作用

結果 $A,B\in\{+1,-1\}$ に対応する基底を $e_A,e_B$ とし、

```math
\Xi_{AB}^{xy}
=
e_A^{\mathsf T}
\Xi(x,y)
e_B,
\qquad
K_{AB}^{xy}
=
\left|
\Xi_{AB}^{xy}
\right|^2
```

と定める。

<!-- theorem-start:theorem -->
**定理（反対称対モードの Bell 余弦枝作用）**
反対称源と左右の実回転の下で、

```math
K_{AB}^{xy}
=
\frac{\mathcal K}{4}
\left[
1
-
AB\cos\Delta_{xy}
\right],
\qquad
\Delta_{xy}
=
2
\left(
\alpha_x-\beta_y
\right)
```

が成立する。さらに、

```math
\sum_{A,B}
K_{AB}^{xy}
=
\mathcal K,
\qquad
\sum_B
K_{AB}^{xy}
=
\sum_A
K_{AB}^{xy}
=
\frac{\mathcal K}{2}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$\delta=\alpha_x-\beta_y$ とする。行列積から

```math
K_{++}^{xy}
=
K_{--}^{xy}
=
\frac{\mathcal K}{2}
\sin^2\delta,
\qquad
K_{+-}^{xy}
=
K_{-+}^{xy}
=
\frac{\mathcal K}{2}
\cos^2\delta
```

を得る。$\cos2\delta=\cos\Delta_{xy}$ を用いる。
<!-- theorem-end:proof -->

この定理は設定依存の非負枝作用を与えるが、結果頻度をまだ与えない。

## 5.4 同じ母測度上の完全履歴事象

第1章の母測度 $\mu_*$ は、設定生成器、局所装置、比較器、記録、外部自由度まで含む開始面 $\Sigma_0$ 上に置かれる。Bellプログラムの完結履歴事象を

```math
F_{AB}^{xy}
=
\left\{
z\in\Sigma_0:
x(z)=x,
y(z)=y,
A(z)=A,
B(z)=B,
M(z)=\mathsf{Bell}
\right\}
```

とする。Bell共同確率は新しいBell専用測度でなく、

```math
P(A,B\mid x,y)
=
\mu_*
\left(
F_{AB}^{xy}
\mid
x,y,M=\mathsf{Bell}
\right)
```

である。第1章で仮定した不変性とエルゴード性により、設定対 $(x,y)$ が出現する部分列の長期相対頻度をこの条件付き確率と結び付ける。各設定対の母測度が正であることを仮定する。

## 5.5 局所記録と共通未来

本稿の局所装置は、既に形成された2値結果セクターを出力ポートと指針へ写す最小符号化器である。連続したミクロ状態から安定な唯一結果を形成する一般測定器は構成していない。

左右の局所結果は、戻り信号が共通未来へ到達する前に記録される。理想局所応答は

```math
A
=
A(x,\Lambda_A),
\qquad
B
=
B(y,\Lambda_B)
```

と書ける。ここで $\Lambda_A,\Lambda_B$ は各側へ到達するミクロ変数である。後の比較器は過去の記録を変更しない。

従って、共通未来で $K_{AB}^{xy}$ を計算してから $(A,B)$ を前向きに選ぶ模型は採用しない。共通未来の役割は、既に局所記録された結果と未来境界変数が整合する完結履歴を定めることである。

## 5.6 Bell 境界角と整合事象

共通未来に固定作用の選択器振動子を置き、その角を $\vartheta_{\rm B}$ とする。枝作用の総和は $\mathcal K$ なので、

```math
u_{\rm B}
=
\frac{\vartheta_{\rm B}}{2\pi}
\mathcal K,
\qquad
0\leq u_{\rm B}<\mathcal K
```

とする。4結果を固定した順に並べ、累積枝作用を

```math
T_0^{xy}=0,
\qquad
T_m^{xy}
=
\sum_{n=1}^m
K_n^{xy}
```

とする。結果対 $(A,B)$ に対応する区間 $\mathcal I_{AB}^{xy}$ の長さは

```math
\left|
\mathcal I_{AB}^{xy}
\right|
=
K_{AB}^{xy}
```

である。

完結履歴の整合事象を

```math
G
=
\left\{
u_{\rm B}
\in
\mathcal I_{A(z)B(z)}^{x(z)y(z)}
\right\}
```

とする。物理的母測度には

```math
\mu_*
\left(
G
\mid
M=\mathsf{Bell}
\right)
=
1
```

を要求する。実験で $G$ を満たさない周期を後から捨てるなら事後選別であり、本稿の模型ではない。必要なのは、不整合周期が物理的解空間で零測度になることである。

## 5.7 基準セクター密度

整合条件を課す前の候補完結履歴に対する Liouville 基準要素を $\nu_*^{xy}$ とする。これは別の観測統計ではなく、$\mu_*$ のBell条件付き部分を構成するための境界位相体積である。結果セクター $(A,B)$ で、選択器座標以外を積分した基準密度を $q_{AB}^{xy}>0$ とする。

選択器角が候補履歴の残る変数に対して条件付き一様で、整合条件以外の因子を $q_{AB}^{xy}$ へ含めると、整合履歴の未規格化質量は

```math
W_{AB}^{xy}
=
q_{AB}^{xy}
K_{AB}^{xy}
```

となる。従って一般式は

```math
P(A,B\mid x,y,G)
=
\frac{
q_{AB}^{xy}
K_{AB}^{xy}
}{
\sum_{A',B'}
q_{A'B'}^{xy}
K_{A'B'}^{xy}
}
```

である。

$q_{AB}^{xy}$ は、局所結果形成後のセクター密度、時計流束、余面積 Jacobian、付随自由度の体積、解多重度、有限境界幅を含む。正準角を追加しただけでは $q_{AB}^{xy}$ の共通性は従わない。これは旧共通境界測度の課題を別名で消したものではなく、その残存条件を1つの因子として明示した式である。

## 5.8 主定理3

<!-- theorem-start:theorem -->
**定理（共通基準密度下の Bell 完全履歴統計）**
次を仮定する。

1. 第5.3節の余弦枝作用が成立する。
2. 局所結果が共通未来より前に形成され、左右の局所応答が保たれる。
3. Bell境界角が候補履歴の残る変数の下で条件付き一様である。
4. 物理的母測度が整合事象 $G$ に支持を持つ。
5. 各設定対で $q_{AB}^{xy}=q^{xy}>0$ が4結果に共通である。
6. 結果依存の失敗周期を捨てない。

このとき、同じ母測度の設定条件付き共同確率は

```math
P(A,B\mid x,y)
=
\frac14
\left[
1
-
AB\cos\Delta_{xy}
\right]
```

となる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $q^{xy}$ は規格化で相殺する。第5.3節の $\sum_{A,B}K_{AB}^{xy}=\mathcal K$ を用いれば、$P(A,B\mid x,y)=K_{AB}^{xy}/\mathcal K$ となる。
<!-- theorem-end:proof -->

定理は、整合支持条件と共通基準密度を置いた後の厳密結果である。具体的な周期写像がこの母測度を生成することは示していない。

## 5.9 非信号周辺と CHSH 値

<!-- theorem-start:corollary -->
**系（対称履歴測度下の非信号性）**
主定理3の条件の下で、

```math
\sum_B
P(A,B\mid x,y)
=
\frac12,
\qquad
\sum_A
P(A,B\mid x,y)
=
\frac12
```

である。
<!-- theorem-end:corollary -->

共同相関は

```math
E(x,y)
=
\sum_{A,B}
AB
P(A,B\mid x,y)
=
-\cos\Delta_{xy}
```

となる。標準4設定では

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
```

を得る。これは平面内2出力の理想余弦則に対する値であり、一般 Tsirelson 原理の導出ではない。

## 5.10 測定設定独立性と設定介入

設定生成器も $\Sigma_0$ の正準自由度に含まれる。完全な隠れ変数を $\Lambda$ とすると、整合支持が設定に依存するため一般に

```math
\mu_*
\left(
d\Lambda
\mid
x,y,M=\mathsf{Bell}
\right)
\neq
\mu_*
\left(
d\Lambda
\mid
M=\mathsf{Bell}
\right)
```

となる。Bell の前提違反は測定設定独立性にある [1,2,7--11,20--23]。局所応答、結果の一意性、理想非信号周辺は維持する。Bell の定理を否定しない。

本稿が求めるのは観測条件付き確率 $P(A,B\mid x,y)$ である。周期内部の設定生成器を外部から差し替え、設定だけを介入変更した場合に同じ分布が保たれるとは示していない。二側境界模型を、前周期記憶が源と設定の共通原因になる前向き模型と同一視もしない。

## 5.11 基準密度と有限幅の誤差

基準密度を

```math
q_{AB}^{xy}
=
q^{xy}
\left(
1+\delta_{AB}^{xy}
\right)
```

とし、

```math
\varepsilon_{\rm base}
=
\max_{A,B,x,y}
\left|
\delta_{AB}^{xy}
\right|
```

とする。$\varepsilon_{\rm base}<1$ なら規格化共同分布の理想余弦則からの偏差は $O(\varepsilon_{\rm base})$ である。

枝作用、境界角、整合判定を含む実際の未規格化質量を $W_{AB}^{xy}$ とし、理想共通密度を $c^{xy}K_{AB}^{xy}$ とする。設定対ごとの総偏差を

```math
\varepsilon_{\rm Bell}^{xy}
=
\frac{
\sum_{A,B}
\left|
W_{AB}^{xy}
-
c^{xy}K_{AB}^{xy}
\right|
}{
c^{xy}\mathcal K
}
```

と定める。$\varepsilon_{\rm Bell}^{xy}<1$ なら、規格化後の共同分布と理想分布の全変動距離は

```math
d_{\rm TV}^{xy}
\leq
\frac{
\varepsilon_{\rm Bell}^{xy}
}{
1-
\varepsilon_{\rm Bell}^{xy}
}
```

で抑えられる。位相雑音、戻り損失、枝作用計算誤差、境界角の非一様性、有限比較幅、基準密度非対称性を分けて監査する。

## 5.12 比較器、記録、逆計算

共通未来比較器は、設定と戻りモードから $K_{AB}^{xy}$ と4区間の境界を可逆に計算する。比較器は過去へ制御信号を送らず、局所記録を変更しない。二側境界問題の終端自由度と整合レジスターを与える。

結果を空の外部記録へ可逆にコピーした後、区間計算、枝作用計算、戻り伝播、局所分析器を逆実行できる。異なる結果を外部記録ごと同じ位相点へ戻すことは Hamiltonian flowの1対1性に反する [17,18]。反復には外部記録、不要情報モード、仕事源、弱く結合した環境が必要である。

## 5.13 主張の範囲

本章で得たものは次である。

1. 固定左右位相担体と反対称源からの余弦枝作用。
2. Bell共同確率を同じ母測度の設定条件付き履歴事象として定義する統一形式。
3. 任意の基準密度 $q_{AB}^{xy}$ を含む一般共同確率式。
4. 共通基準密度下の余弦共同確率、非信号周辺、CHSH値。
5. Bell の測定設定独立性が成立しないことの明示。

一方、次は示していない。

1. 一般初期集団から反対称源を反復準備すること。
2. 連続した局所状態から安定な唯一結果を形成すること。
3. 整合しない周期を事後選別せず零測度にする Hamiltonian 境界値問題。
4. 4結果の基準密度を共通にする物理的準備。
5. 目的のBell条件付き部分を持つ不変母測度の具体的な生成。
6. 外部設定介入に対する統計の安定性。
7. 一般複合状態、一般測定、一般 Tsirelson 原理。
