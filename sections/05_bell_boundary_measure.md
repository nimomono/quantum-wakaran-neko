@number: 5
@chapter: 本文
@title: Bell 対モード、比較器、共通境界測度
@status: 反対称源と局所回転からの余弦枝作用、理想比較転送、2モード殻容量は補助模型内部で厳密である。左右交差相関は単粒子側の正半定値相関行列と区別する。Bell 共同確率は共通境界測度に依存する条件付き結果であり、その測度を生成する完全周期は未完成である。

## 5.1 固定された左右位相担体モード

Bell 構成では、左右へ伝播する有限個の局在位相担体モードを基礎変数とする。2粒子配置空間上の場も、単粒子側の統計振幅 $\chi$ も局所 Hamiltonian へ追加しない。装置の組立時に固定した左右モードを

```math
z^A_{\mu r},
\qquad
z^B_{\nu r},
\qquad
\mu,\nu
\in
\left\{
+,-
\right\},
\qquad
r
\in
\left\{
1,2
\right\}
```

とする。$\mu,\nu$ は局所分析器の2出力、$r$ は2つの直交源チャンネルである。設定または結果ごとにモード基底を選び直さない。

左右モードの派生相関を

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

と定める。$\Xi$ は独立した場でも新しい正準変数でもない。左右の基礎位相担体から計算される階数2以下の交差相関行列である。単粒子側の

```math
C
=
\mathbb E
\left[
bb^\dagger
\right]
```

は正半定値 Hermitian 行列であるのに対し、$\Xi$ は一般に正半定値でも Hermitian でもない。両者を同一の相関行列として扱わない。実際の左右確率集団から作る場合は、より大きな正半定値共分散行列の左右非対角ブロックとして $\Xi$ を埋め込める。

共通内部回転

```math
z^A
\longmapsto
e^{i\beta}z^A,
\qquad
z^B
\longmapsto
e^{i\beta}z^B
```

に対して $\Xi$ は不変である。

## 5.2 反対称源と局所分析器

理想源が準備する相関行列を

```math
\Xi_0
=
\sqrt{
\frac{
\mathcal K
}{
2
}
}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。これは2つの階数1交差項へ分解できるため、2つの直交源チャンネルで構成できる。単粒子側の階数1条件とは異なり、Bell 源全体を階数1へ制限しない。有限 Hamiltonian 源が任意初期状態から $\Xi_0$ を準備することと、比較時刻まで相対位相を保つことは独立の準備問題である。

設定 $a,b$ に対応するモード角を $\alpha_a,\alpha_b$ とする。左右の局所分析器は各側の基礎位相担体モードだけを

```math
z^{A,(r)}
\longmapsto
R(\alpha_a)
z^{A,(r)},
\qquad
z^{B,(r)}
\longmapsto
R(\alpha_b)
z^{B,(r)}
```

と回転する。ここで

```math
R(\alpha)
=
\begin{pmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{pmatrix}
```

である。相関表示は

```math
\Xi(a,b)
=
R(\alpha_a)
\Xi_0
R(\alpha_b)^{\mathsf T}
```

となるが、物理的に回すのは左右の局所モードである。

局所正準座標 $(Q^A_{\mu r},P^A_{\mu r})$ に対する回転生成子を

```math
G_A
=
\sum_r
\left(
Q^A_{+r}P^A_{-r}
-
Q^A_{-r}P^A_{+r}
\right)
```

とすれば、$H_A=\dot\alpha_aG_A$ がA側だけを回転する。B側も同様であり、分析器 Hamiltonian は空間的に分離した局所和である。

## 5.3 余弦枝作用

結果 $A,B\in\{+1,-1\}$ に対応する基底を $e_A,e_B$ とし、

```math
\Xi_{AB}(a,b)
=
e_A^{\mathsf T}
\Xi(a,b)
e_B,
\qquad
K_{AB}
=
\left|
\Xi_{AB}
\right|^2
```

と定める。

<!-- theorem-start:theorem -->
**定理（反対称対モードの Bell 余弦枝作用）**
反対称源と左右の実回転の下で、

```math
K_{AB}
=
\frac{
\mathcal K
}{
4
}
\left[
1
-
AB
\cos
\Delta_{ab}
\right],
\qquad
\Delta_{ab}
=
2
\left(
\alpha_a-\alpha_b
\right)
```

が成立する。さらに、

```math
\sum_{A,B}
K_{AB}
=
\mathcal K,
\qquad
\sum_B
K_{AB}
=
\sum_A
K_{AB}
=
\frac{
\mathcal K
}{
2
}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$\delta=\alpha_a-\alpha_b$ とする。行列積を計算すると、

```math
K_{++}
=
K_{--}
=
\frac{
\mathcal K
}{
2
}
\sin^2\delta,
\qquad
K_{+-}
=
K_{-+}
=
\frac{
\mathcal K
}{
2
}
\cos^2\delta
```

となる。$\cos2\delta=\cos\Delta_{ab}$ を用いる。
<!-- theorem-end:proof -->

この定理は設定依存の枝作用を与えるが、結果頻度をまだ与えない。

光子偏光型では $\alpha_a=a$、$\alpha_b=b$ とすれば $\Delta_{ab}=2(a-b)$ となる。平面内スピン型では $\alpha_a=a/2$、$\alpha_b=b/2$ とすれば $\Delta_{ab}=a-b$ となる。モード角と装置表示角を区別する。

## 5.4 局所記録と共通未来

本稿の局所装置は、既に形成された2値結果セクターを出力ポートと指針へ写す最小符号化器である。連続したミクロ状態から安定な唯一結果を形成する一般測定器は構成していない。

左右の戻り信号は局所記録後に有限速度で伝播し、2測定事象の共通未来でだけ合流する。従って、$\Xi_{AB}$ を空間的に離れた測定時刻の瞬間的な局所力へ使わない。

比較振幅の実部と虚部を読む正準対を

```math
\left(
Q_{\rm R},
P_{\rm R}
\right),
\qquad
\left(
Q_{\rm I},
P_{\rm I}
\right)
```

とする。結果セクターを選ぶ滑らかな窓を $\chi_A$、$\chi_B$ とし、

```math
\Xi(s_A,s_B)
=
\sum_{A,B}
\chi_A(s_A)
\chi_B(s_B)
\Xi_{AB}
```

と書く。理想的な排他セクターでは $\Xi(s_A,s_B)=\Xi_{AB}$ である。

## 5.5 理想比較転送

比較読み出し Hamiltonian を

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}
\operatorname{Re}
\Xi(s_A,s_B)
+
P_{\rm I}
\operatorname{Im}
\Xi(s_A,s_B)
\right]
```

とする。$\vartheta$ は内部時計角である。比較窓の入口で

```math
Q_{\rm R}
=
P_{\rm R}
=
Q_{\rm I}
=
P_{\rm I}
=
0
```

とし、パルス面積を

```math
\Gamma
=
\int
g_{\rm read}(\vartheta(t))
\,dt
```

とする。

<!-- theorem-start:proposition -->
**命題（理想比較読み出し）**
比較窓で入力相関を一定とみなせる理想極限では、

```math
Q_{\rm R}^{\rm out}
=
\Gamma
\operatorname{Re}
\Xi_{AB},
\qquad
Q_{\rm I}^{\rm out}
=
\Gamma
\operatorname{Im}
\Xi_{AB}
```

となる。$P_{\rm R}=P_{\rm I}=0$ の理想入口では、読み出し Hamiltonian による入力モードへの反作用は零である。
<!-- theorem-end:proposition -->

比較2モードの作用を

```math
J_{\rm R}
=
\frac12
\left(
Q_{\rm R}^2+P_{\rm R}^2
\right),
\qquad
J_{\rm I}
=
\frac12
\left(
Q_{\rm I}^2+P_{\rm I}^2
\right)
```

とし、総比較作用を

```math
A_\partial
=
J_{\rm R}
+
J_{\rm I}
```

とする。

<!-- theorem-start:corollary -->
**系（枝作用の比較作用への転送）**
理想比較後の結果セクターでは、

```math
A_\partial^{AB}
=
\frac{
\Gamma^2
}{
2
}
K_{AB}
```

である。
<!-- theorem-end:corollary -->

## 5.6 比較2モード殻

複素比較モードを

```math
c_\nu
=
\frac{
Q_\nu+iP_\nu
}{
\sqrt2
},
\qquad
\nu
\in
\left\{
\mathrm R,
\mathrm I
\right\}
```

とすれば、

```math
A_\partial
=
\left|
c_{\rm R}
\right|^2
+
\left|
c_{\rm I}
\right|^2
```

である。第4章の一般作用殻容量から、

```math
\Omega_2
\left(
A_\partial^{AB}
\right)
=
\left(
2\pi
\right)^2
\frac{
\Gamma^2
}{
2
}
K_{AB}
```

を得る。

$U(2)$ 型の殻接混合は $A_\partial$ を保存し、比較殻上の角分布を変えられる。しかし、正規化された各結果セクターの総確率質量は Hamiltonian 写像で保存される。読み出しと殻内混合だけでは、セクター間の質量を $\Omega_2(A_\partial^{AB})$ に比例させられない。

Bell 頻度には、全結果セクターへ共通の未規格化境界密度または境界流束を置く条件が別に必要である。

## 5.7 境界位相空間

1試行の全正準変数を $z\in\Gamma_{\rm all}$ とする。比較境界面を結果ごとの排他的な和

```math
\Gamma_\partial
=
\bigsqcup_{A,B}
\Gamma_\partial^{AB}
```

とする。各 $\Gamma_\partial^{AB}$ では、局所記録は $(A,B)$ を持ち、時計は境界面を正方向に横切り、比較総作用は $A_\partial^{AB}$ である。

結果セクターの未規格化質量を

```math
\begin{aligned}
\widetilde W_{AB}(a,b)
={}&
w_{AB}
\int
\lambda_\partial^{AB}(z;a,b)
\\
&
\times
\delta
\left(
A_\partial^{AB}
-
J_{\rm R}
-
J_{\rm I}
\right)
d\Gamma_{\rm cmp}
d\Gamma_{\rm aux}
\end{aligned}
```

と定める。$d\Gamma_{\rm aux}$ は比較作用を直接分配しない自由度の測度である。

理想共通条件は次である。

1. 基準多重度 $w_{AB}$ が4結果で等しい。
2. 境界密度と時計流束が4結果で共通である。
3. 余面積 Jacobian、付随体積、解多重度が4結果で共通である。
4. 全結果を同じ境界分解能で数える。

共通因子は設定 $a,b$ に依存しても、4結果で同じなら規格化で相殺する。$w_{AB}$ は前向き初期集団の事前確率ではなく、境界 Liouville 要素へ置く共通基準多重度である。

## 5.8 主定理3

<!-- theorem-start:theorem -->
**定理（共通境界測度下の Bell 共同確率）**
次を仮定する。

1. 第5.3節の余弦枝作用。
2. 第5.5節の理想比較転送。
3. 第5.7節の共通境界条件。
4. 全結果セクターを無条件に数え、結果依存の失敗履歴を捨てない。

このとき、

```math
P
\left(
A,B
\mid
a,b
\right)
=
\frac{
\widetilde W_{AB}
}{
\sum_{A',B'}
\widetilde W_{A'B'}
}
=
\frac14
\left[
1
-
AB
\cos
\Delta_{ab}
\right]
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通境界因子を $\Lambda_\partial(a,b)>0$ とまとめる。2モード殻容量から

```math
\widetilde W_{AB}
\propto
A_\partial^{AB}
\propto
K_{AB}
```

である。$\sum_{A,B}K_{AB}=\mathcal K$ を用いて規格化する。
<!-- theorem-end:proof -->

これは共通境界条件を置いた後の厳密結果である。境界条件自体を通常の前向き初期分布から導いた結果ではない。

## 5.9 非信号周辺と CHSH 値

<!-- theorem-start:corollary -->
**系（対称共通境界測度下の非信号性）**
主定理3の条件の下で、

```math
\sum_B
P
\left(
A,B
\mid
a,b
\right)
=
\frac12,
\qquad
\sum_A
P
\left(
A,B
\mid
a,b
\right)
=
\frac12
```

である。
<!-- theorem-end:corollary -->

共同相関は

```math
E(a,b)
=
\sum_{A,B}
AB
P
\left(
A,B
\mid
a,b
\right)
=
-
\cos
\Delta_{ab}
```

となる。標準4設定では

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
```

を得る。これは平面内2出力の理想余弦則に対する値であり、一般的な Tsirelson 原理の導出ではない。

可視度 $V_{\rm Bell}$ により

```math
E(a,b)
=
-
V_{\rm Bell}
\cos
\Delta_{ab}
```

となる場合、標準角で $|S_{\rm CHSH}|=2\sqrt2V_{\rm Bell}$ である。CHSH不等式を超えるには $V_{\rm Bell}>1/\sqrt2$ が必要である。

## 5.10 有限誤差の測度

理想未規格化質量を $cK_{AB}$ とする。実際の未規格化質量 $W_{AB}$ に対し、

```math
\varepsilon_{\rm Bell}
=
\frac{
\sum_{A,B}
\left|
W_{AB}
-
cK_{AB}
\right|
}{
c\mathcal K
}
```

と定める。$\varepsilon_{\rm Bell}<1$ なら、規格化後の共同分布と理想分布の全変動距離は

```math
d_{\rm TV}
\leq
\frac{
\varepsilon_{\rm Bell}
}{
1-\varepsilon_{\rm Bell}
}
```

で抑えられる。この評価は、理想的に $K_{AB}=0$ となる端点でも相対誤差を使わずに済む。

周辺確率の非信号性偏差と各設定対の相関誤差も $O(\varepsilon_{\rm Bell})$ である。CHSH値の誤差は4設定の相関誤差の和で抑える。位相雑音、戻り損失、比較器初期作用、時計面積、結果窓、境界因子の非対称性を $\varepsilon_{\rm Bell}$ へ分解して監査する。

## 5.11 完全履歴測度と Bell 前提

設定 $a,b$ を固定した境界値問題の解空間を $\mathcal S_{a,b}$、境界位相点から完結履歴への解写像を

```math
\mathfrak S_{a,b}
:
\Gamma_\partial^{a,b}
\longrightarrow
\mathcal S_{a,b}
```

とする。完全履歴測度は、境界 Liouville 測度を解写像で押し出した

```math
\mu_{\rm hist}^{a,b}
=
\left(
\mathfrak S_{a,b}
\right)_*
\mu_\partial^{a,b}
```

である。

境界面から生成側準備面までの Hamiltonian flowを $\Phi_{T\leftarrow0}^{a,b}$ とすると、生成側へ引き戻した測度は

```math
\mu_{\rm prep}^{a,b}
=
\left(
\Phi_{T\leftarrow0}^{a,b}
\right)^*
\mu_\partial^{a,b}
```

である。境界作用制約が $a,b$ に依存するため、一般に

```math
\rho
\left(
\Lambda
\mid
a,b
\right)
\neq
\rho
\left(
\Lambda
\right)
```

となる。Bell の前提違反は測定設定独立性にある [1,2,7--11,20--23]。

理想局所装置では、

```math
A
=
A
\left(
a,
\Lambda_A
\right),
\qquad
B
=
B
\left(
b,
\Lambda_B
\right)
```

と書ける局所応答を維持する。Bell 違反は設定依存の完全履歴集団から生じる。Bell の定理を否定せず、遠隔設定による瞬間的な測定力も導入しない。

## 5.12 比較器の因果的役割

局所結果は戻り信号が比較器へ到達する前に記録できる。通常の前向き因果では、後の比較器は過去の記録を変更しない。本模型もそのような変更を主張しない。

比較器の役割は次の2つである。

1. 完結履歴の $K_{AB}$ を共通未来の局所相互作用として比較作用へ転送する。
2. 二側境界測度を定義する終端自由度を与える。

比較器は過去へ制御信号を送る装置ではなく、生成からリセットまでの全履歴に課す境界条件の物理的終端である。

## 5.13 記録、逆計算、未完成の周期

比較後、結果を空の外部記録へ可逆にコピーする。混合の制御履歴と暗モード状態を保持できる理想模型では、

1. 殻内混合を逆実行する。
2. 比較読み出しを逆実行する。
3. 戻り伝播を逆実行する。
4. 局所分析器を逆実行する。
5. 内部指針と比較器を基準状態へ戻す。

ことができる。

異なる結果を外部に残したまま、外部記録を含む全自由度を同じ1点へ戻すことはできない。Hamiltonian flowが1対1だからである [17,18]。反復には記録媒体、不要情報モード、仕事源、弱く結合した環境のいずれかが必要である。

主定理3の境界測度を事後選別なしに準備するには、さらに次が必要である。

1. 設定生成器を含む反復可能な全周期。
2. 一意結果形成と増幅。
3. 全開始数、局所記録数、比較完了数、リセット完了数の一致。
4. 結果依存の失敗試行または停止時間を捨てないこと。
5. 共通境界密度の有限 Hamiltonian・弱開放準備。

これは現模型の測定側で最大の未解決問題である。
