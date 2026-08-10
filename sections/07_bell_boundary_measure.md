@number: 7
@chapter: 本文
@title: 4成分 Bell 重みと二側履歴測度
@status: 反対称な集団交差相関の4成分重みを一般有限基底作用重みと代数的に比較する。独立な局所 Haar 角から基準セクター密度1/4を導き、二側整合条件の下で Bell 余弦共同確率、設定分布保存、非信号性を得る。M39の単一担体内論理相関とは分離し、2物理担体、分離局所測定翼、試行ごとの余弦区間生成、整合支持条件を未完成課題とする。

## 7.1 左右位相担体と反対称交差相関

左右に2モードずつを置き、単一試行の局所モード振幅を $z^{A,\omega},z^{B,\omega}\in\mathbb C^2$ とする。調製条件と Bell プログラムを固定した集団平均として

```math
\Xi
=
\mathbb E
\left[
z^{A,\omega}
\left(z^{B,\omega}\right)^{\mathsf T}
\right]
\in
\mathbb C^{2\times2}
```

を定める。$\Xi$ は集団統計量であり、単一試行の正準変数ではない。反対称源条件を

```math
\Xi_0
=
\sqrt{\frac{\mathcal K}{2}}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。$\mathcal K=\operatorname{tr}(\Xi_0\Xi_0^\dagger)$ は集団交差相関の規格化量である。単一試行ごとの保存作用と同一視しない。反対称源集団の反復可能な物理準備は本章の入力条件であり、結論ではない。

行優先ベクトル化を

```math
\operatorname{rvec}\Xi
=
\begin{pmatrix}
\Xi_{++}\\
\Xi_{+-}\\
\Xi_{-+}\\
\Xi_{--}
\end{pmatrix}
```

と定め、規格化4成分ベクトルを

```math
\chi_{\rm B}
=
\frac{\operatorname{rvec}\Xi_0}{\sqrt{\mathcal K}}
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\
1\\
-1\\
0
\end{pmatrix}
```

とする。$\chi_{\rm B}$ は左右の局所担体集団から作る派生交差相関の4次元表示である。独立した非局所実在場または単一試行の4モード粒子状態として追加しない。

## 7.2 局所分析器とテンソル積表示

設定 $x,y$ に対応する局所分析器角を $\alpha_x,\beta_y$ とする。平面回転を

```math
R(\gamma)
=
\begin{pmatrix}
\cos\gamma&-\sin\gamma\\
\sin\gamma&\cos\gamma
\end{pmatrix}
```

とする。左右の分析器は

```math
z^A
\longmapsto
R(\alpha_x)z^A,
\qquad
z^B
\longmapsto
R(\beta_y)z^B
```

と局所的に作用する。左右の正準変数は分離しているので、生成子 $G_A,G_B$ は $\{G_A,G_B\}=0$ を満たし、分析器 Hamiltonian は局所和として書ける。

交差相関と4成分表示は

```math
\Xi_{xy}
=
R(\alpha_x)
\Xi_0
R(\beta_y)^{\mathsf T},
```

```math
\chi_{xy}
=
\left[
R(\alpha_x)
\otimes
R(\beta_y)
\right]
\chi_{\rm B}
```

となる。テンソル積表示は、左右の局所正準回転の交差相関への作用をまとめたものである。

## 7.3 4成分作用重み

結果対 $A,B\in\{+1,-1\}$ に対応する規格化重みを

```math
w_{AB}^{xy}
=
\left|
\left(\chi_{xy}\right)_{AB}
\right|^2
=
\frac{
\left|
\left(\Xi_{xy}\right)_{AB}
\right|^2
}{
\mathcal K
}
```

とする。直接計算すると

```math
w_{++}^{xy}
=
w_{--}^{xy}
=
\frac12
\sin^2
\left(
\alpha_x-\beta_y
\right),
```

```math
w_{+-}^{xy}
=
w_{-+}^{xy}
=
\frac12
\cos^2
\left(
\alpha_x-\beta_y
\right)
```

である。$\Delta_{xy}=2(\alpha_x-\beta_y)$ とすれば、

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

となる。規格化前の集団重みを

```math
K_{AB}^{xy}
=
\mathcal K
w_{AB}^{xy}
```

とする。

<!-- theorem-start:proposition -->
**命題（Bell 集団重みと4成分作用重みの代数的同型）**
反対称な集団交差相関と左右局所回転の下で、規格化重み $K_{AB}^{xy}/\mathcal K$ は、4成分ベクトル $\chi_{\rm B}$ に局所テンソル積回転を施した成分の絶対値2乗に一致する。従ってBell 余弦集団重みは、第5章の有限基底作用重みと同じ代数構造を持つ。
<!-- theorem-end:proposition -->

この同値は線形代数上の同型であり、単粒子側のテンプレート SWAP 測定器を Bell 装置へ適用したことを意味しない。$\chi_{\rm B}$ と $w_{AB}^{xy}$ は集団相関から計算した量であり、単一試行の Hamiltonian が直接読み取れる正準レジスターではない。Bell では左右の結果が共通未来へ情報が届く前に局所的に形成される必要がある。

## 7.4 局所結果生成

A側とB側に固定作用の正準角

```math
\phi_A,\phi_B
\in
[0,2\pi)
```

を置く。理想局所結果を

```math
A_x(\phi_A)
=
\operatorname{sgn}
\cos
\left(
\phi_A-2\alpha_x
\right),
```

```math
B_y(\phi_B)
=
\operatorname{sgn}
\cos
\left(
\phi_B-2\beta_y
\right)
```

とする。零点は零測度境界である。各応答は同じ翼の設定と局所角だけを参照する。A側の式に $y$ はなく、B側の式に $x$ はない。

実装では符号関数を滑らかな有限幅比較へ置き換える。結果の厳密2値化に関する連続性の制限は第4章と同じであり、境界近傍だけを誤差領域とする。

## 7.5 制約前基準測度

設定生成器のマクロセクター確率を $\pi_x,\pi_y$ とする。局所結果角と共通未来角 $\theta_F$ を独立な Haar 角とし、制約前基準測度を

```math
d\nu_{\rm B}^0
=
\pi_x\pi_y
\frac{d\phi_A}{2\pi}
\frac{d\phi_B}{2\pi}
\frac{d\theta_F}{2\pi}
```

とする。各局所応答は円周を等しい2つの半円へ分けるので、

```math
\nu_{\rm B}^0
\left(
A
\mid
x
\right)
=
\frac12,
\qquad
\nu_{\rm B}^0
\left(
B
\mid
y
\right)
=
\frac12
```

である。独立性から

```math
q_{AB}^{xy}
:=
\nu_{\rm B}^0
\left(
A,B
\mid
x,y
\right)
=
\frac14
```

を全設定・全結果について得る。最小模型では、基準セクター密度の共通性は仮定でなく局所 Haar 角と半円分割の帰結である。

## 7.6 共通未来区間と整合事象

固定した反対称源プログラムについて、4結果を $++,+-,-+,--$ の順に並べ、累積重みを

```math
T_0=0,
\qquad
T_1=w_{++}^{xy},
```

```math
T_2
=
w_{++}^{xy}+w_{+-}^{xy},
\qquad
T_3
=
T_2+w_{-+}^{xy},
\qquad
T_4=1
```

とする。$r_F=\theta_F/(2\pi)$ とし、各結果対の区間 $\mathcal I_{AB}^{xy}\subset[0,1)$ を対応する累積区間とする。その長さは

```math
\left|
\mathcal I_{AB}^{xy}
\right|
=
w_{AB}^{xy}
```

である。区間境界は、反対称源条件と設定角から計算される Bell プログラムのパラメータである。単一試行の $z^{A,\omega},z^{B,\omega}$ から集団相関 $\Xi$ を推定して区間を作るとはしない。

左右で既に記録された結果を $A_x(\phi_A),B_y(\phi_B)$ とする。二側整合事象を

```math
G
=
\left\{
r_F
\in
\mathcal I_{A_x(\phi_A),B_y(\phi_B)}^{xy}
\right\}
```

と定める。未来角は結果を作らない。局所結果を持つ履歴と、プログラムされた集団余弦区間が整合するかだけを制約する。この区間法則をミクロ源と局所装置から試行ごとに生成する機構は未完成である。

## 7.7 整合体積と設定分布

固定した $x,y,A,B$ について、局所角の結果セクター体積は $1/4$、未来角区間の体積は $w_{AB}^{xy}$ である。従って

```math
\nu_{\rm B}^0
\left(
A,B,G
\mid
x,y
\right)
=
\frac14
w_{AB}^{xy}
```

となる。全結果について和を取ると、

```math
\nu_{\rm B}^0
\left(
G
\mid
x,y
\right)
=
\frac14
\sum_{A,B}
w_{AB}^{xy}
=
\frac14
```

である。整合事象の総基準体積は設定に依存しない。

## 7.8 二側履歴測度と共同確率

物理的履歴を、初期側の準備条件と終端側の整合条件 $G$ の双方を満たす Hamiltonian 軌道として定める。二側履歴測度を

```math
d\mu_{\rm B}
=
4\mathbf1_G
\,d\nu_{\rm B}^0
```

とする。$\nu_{\rm B}^0(G)=1/4$ なので規格化されている。

<!-- theorem-start:theorem -->
**定理（最小 Bell 二側履歴測度）**
反対称源、左右局所回転、独立局所 Haar 角、独立未来 Haar 角、整合支持条件 $G$ を仮定する。このとき

```math
P_{\mu_{\rm B}}
\left(
A,B
\mid
x,y
\right)
=
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

であり、設定分布は

```math
P_{\mu_{\rm B}}(x,y)
=
\pi_x\pi_y
```

のまま保たれる。
<!-- theorem-end:theorem -->

この定理では、局所結果セクター体積 $1/4$ と、集団反対称源から代数的に得た未来区間長 $w_{AB}^{xy}$ の積を二側条件で規格化している。ただし区間長を物理的境界法則として採用するため、共同確率を完全なミクロ装置から無条件に導出した結果ではない。

## 7.9 一般基準密度との関係

完全装置では、時計流束、境界面の Jacobian 、付随自由度、解多重度、記録失敗率が結果対に依存する可能性がある。これらをまとめた一般基準密度を $q_{AB}^{xy}$ とすれば、共同確率は

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

となる。最小模型の $q_{AB}^{xy}=1/4$ を完全模型へ拡張するには、少なくとも次が必要である。

1. 付随測度が局所結果セクターから独立である。
2. 境界面の Jacobian が4結果で共通である。
3. 各結果に対応する Hamiltonian 解の多重度が共通である。
4. 戻り伝播、比較、記録の失敗率が結果依存でない。

従って本章は、最小因子化模型での基準密度を導出するが、一般完全模型での共通性を無条件には主張しない。

## 7.10 非信号性と CHSH 値

余弦重みを一側について和を取ると、

```math
\sum_B
w_{AB}^{xy}
=
\frac12,
\qquad
\sum_A
w_{AB}^{xy}
=
\frac12
```

である。従って

```math
P(A\mid x,y)
=
P(A\mid x)
=
\frac12,
```

```math
P(B\mid x,y)
=
P(B\mid y)
=
\frac12
```

となる。測定設定独立性は破れるが、理想対称模型の観測周辺は非信号である。

相関は

```math
E(x,y)
=
-\cos
2
\left(
\alpha_x-\beta_y
\right)
```

である。標準角

```math
\alpha_0=0,
\qquad
\alpha_1=\frac{\pi}{4},
\qquad
\beta_0=\frac{\pi}{8},
\qquad
\beta_1=-\frac{\pi}{8}
```

に対し、

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
```

を得る。これは反対称4成分状態と平面内2出力に対する値であり、一般 Tsirelson 原理の導出ではない。

## 7.11 測定設定独立性

完全ミクロ履歴を

```math
\Lambda
=
\left(
\phi_A,
\phi_B,
\theta_F,
\Lambda_{\rm src},
\ldots
\right)
```

とする。物理測度では

```math
d\mu_{\rm B}
\left(
\Lambda
\mid
x,y
\right)
=
4
\mathbf1_{G_{xy}}(\Lambda)
d\nu_{\rm B}^0(\Lambda)
```

であり、$G_{xy}$ は設定を通じて余弦区間に依存する。従って一般に

```math
\mu_{\rm B}
\left(
d\Lambda
\mid
x,y
\right)
\neq
\mu_{\rm B}
\left(
d\Lambda
\right)
```

である。 Bell の前提違反は測定設定独立性にある。局所応答は $A=A(x,\phi_A)$、$B=B(y,\phi_B)$ のままであり、反対側の設定を引数に持たない。 Bell の定理は正しく、本模型はその前提を満たさない。

設定分布保存は、完全ミクロ履歴の設定独立性を回復しない。観測される $P(x,y)$ が制約前と同じことと、$P(\Lambda\mid x,y)=P(\Lambda)$ は別の条件である。

## 7.12 二側境界値問題としての意味

物理順序として確立している部分は、局所分析器、局所結果形成、局所記録、有限速度の情報伝送までである。共通未来では、固定プログラムが設定 $x,y$ に対応する区間 $\mathcal I_{AB}^{xy}$ を参照し、記録済み結果との整合性を判定する条件付き模型を考える。

時刻 $t_0$ の準備面と時刻 $t_F$ の終端面

```math
\mathcal B_F
=
\left\{
r_F
\in
\mathcal I_{AB}^{xy}
\right\}
```

の両方を満たす軌道を解集合とする。Hamiltonian 流を $\Phi_T$ とすれば、許される初期状態は $\Phi_T^{-1}(\mathcal B_F)$ である。最小因子化模型では、Liouville 体積保存と未来角の独立 Haar 密度により、固定結果セクターでの引戻し体積は終端区間体積に比例する。完全模型では、付随測度、境界 Jacobian、解多重度の結果非依存性が別に必要である。

これは終端から過去へ制御力を送る機構ではない。初期条件だけでなく終端条件も満たす全履歴を物理的解とする二側境界値問題である。一方、$G$ を物理法則として課さず、制約前候補を全て前向き生成して $G^c$ を実験後に捨てれば、25%だけを残す事後選別になる。その解釈は採用しない。

重要な未完成点は、$\Xi$ が集団量であるため、単一試行の装置が $\Xi$ を読み取って4区間を作ることはできない点である。本章では反対称源プログラムから解析的な余弦区間を指定する。単一試行の源変数と局所相互作用から同じ区間多重度が自然に生じる有限 Hamiltonian は構成していない。

## 7.13 主張の範囲

本章で得たものは次である。

1. Bell 余弦重みと有限 $L=4$ 作用重みの代数的同値。
2. 左右の局所 Hamiltonian によるテンソル積回転。
3. 独立局所 Haar 角と半円分割からの基準セクター密度 $1/4$。
4. 整合事象の総基準体積 $1/4$ と設定独立性。
5. 二側履歴測度の下での Bell 共同確率と設定分布保存。
6. 理想対称条件での非信号性、 CHSH 値、 Bell 前提監査。

第6章のM39は、1つの4モード装置内に操作誘導テンソル積とCNOTを構成する。M39のA、Bは論理部分系であり、本章が必要とする空間的に分離した2物理担体または2測定翼ではない。M39の $XX$、$YY$、$ZZ$ 相関をBell 共同頻度として使わない。

一方、次は示していない。

1. 反対称源の反復可能な物理準備。
2. 集団相関 $\Xi$ を使わず、単一試行変数から余弦区間多重度を生成すること。
3. 二側整合支持条件 $G$ の物理的必然性。
4. $\mu_{\rm B}$ を通常の前向き自律 Hamiltonian の Poincaré 不変測度として生成すること。
5. 付随自由度と境界 Jacobian を含む完全模型での基準密度因子化。
6. 外部設定介入に対する統計安定性。
7. 非対称準備または有限比較幅の下での一般非信号条件。
8. 平面内2出力を超える一般複合測定と一般 Tsirelson 原理。
9. 共通源からの2物理担体の生成と空間分離。
10. 測定中のA--B直接結合を使わない局所Hamiltonian 測定翼。
11. 各翼の不可逆な局所結果記録と、記録後だけに行う照合。
