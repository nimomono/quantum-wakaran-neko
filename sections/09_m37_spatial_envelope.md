@number: 9
@chapter: 本文
@title: 空間複素振幅場と1個の空間実現配置
@status: M37の有限局所実振動子網からSchrödinger型複素振幅場を有限時間誤差付きで導き、第2章の共通実現配置則を空間グラフへ特殊化する。初期準備、Born型等変性、節一様正則化、局所Hamiltonian更新、固定時刻位置検出を与え、Q3-1の固定基準を維持する。

## 9.1 Q3の4層構造とM37の範囲

本稿のQ3側は、次の4層を区別する。

1. ミクロ層は、実位置 $q_i$ と実運動量 $p_i$ を持つ有限個の古典振動子である。
2. 有効場層は、搬送振動を除いた局所複素包絡 $b_i$ である。
3. 実現配置層は、共通モデルが複素振幅場と別に置く1個の局在正準自由度 $(Z,P_Z)$ と、その粗視化セル位置 $X=X(Z)$ である。
4. 装置層は、初期準備、局所辺選択、実現配置輸送、履歴保存、位置検出を行う有限正準制御系である。

ミクロ層から有効場層への移行はQ3-1の固定達成基準である。M37は共通モデルへ空間複素振幅場を供給する役割を持つ。完全状態は模式的に $(b,Z,P_Z,\mathcal R,\mathcal C)$ と書き、$\mathcal R$ は選択・履歴セル、$\mathcal C$ は時計・局所制御自由度を表す。理想Markov記述では粗視化した $X_t\in V$ を使う。M37だけから実現配置または最小跳躍則が必然的に出るとは主張しない。

M38はQ1-1からQ1-4を扱い、M35は一般有限 $L$ の作用選択器を与える。M42はM35の比較機構、M38の有限履歴選択器、M41の可変全作用選択を局所更新部品として再利用する。任意の装置用正準混合がM37の局所ばね網だけで実装できるとは仮定せず、M37とM38の同一ハードウェア化も主張しない。

振動子の個数を $L<\infty$、共通質量を $M_{\rm osc}>0$、搬送周波数を $\omega_0>0$ とする。$M_{\rm osc}$ はミクロ振動子の質量であり、第9.6節に現れる有効質量 $m$ と区別する。固定作用尺度 $\mathcal J_0>0$ は正準座標の規格化に使う。

有限次元 Schrödinger 方程式を古典正準座標または結合振動子へ写すこと自体は既知である [34--37]。特に、位置結合だけを用いる弱結合近似と、位置・運動量の両結合を用いる厳密写像は先行研究で区別されている [35--37]。

本稿は次を新規性として主張しない。

1. 複素ベクトルを2倍次元の実ベクトルで表すこと。
2. 任意の Hermitian 行列を設計済み2次 Hamiltonian へ埋め込むこと。
3. 結合振動子が Schrödinger 型運動を近似できること。

本稿で追加するのは、局所位置結合網について反回転項を落とさない厳密式、正常モード生成子との作用素誤差、有限時間状態誤差、局所包絡誤差から有限基底測定分布への伝播を同じ誤差台帳で接続することである。

## 9.2 ミクロHamiltonian

実正準対を

```math
\left\{q_i,p_j\right\}
=
\delta_{ij}
```

とし、時間非依存な有限振動子網を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

で定める。$A=A^{\mathsf T}$ は実対称である。局所グラフ $G=(V,E)$ 上では

```math
A
=
D_\delta+L_\kappa
```

とし、成分表示を

```math
H_{\rm micro}
=
\sum_i
\left[
\frac{p_i^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_0^2q_i^2}{2}
+
\frac{\delta_iq_i^2}{2}
\right]
+
\frac12
\sum_{\{i,j\}\in E}
\kappa_{ij}
\left(q_i-q_j\right)^2
```

と書ける。ここで $\kappa_{ij}=\kappa_{ji}\geq0$ である。$D_\delta$ は対角離調、$L_\kappa$ は重み付きグラフ Laplacian である。

安定条件は

```math
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
>
0
```

である。離調 $\delta_i$ は負でもよいが、全剛性行列は正定値でなければならない。本章では浴、散逸、環境残差を加えない。閉鎖有限振動子網だけでQ3-1の基準定理を構成する。

## 9.3 局所正準座標と回転包絡

各振動子に局所的な規格化座標

```math
Q
=
\sqrt{M_{\rm osc}\omega_0}\,q,
\qquad
P
=
\frac{p}{\sqrt{M_{\rm osc}\omega_0}}
```

を導入する。これは頂点ごとに独立な正準変換であり、$\{Q_i,P_j\}=\delta_{ij}$ を保つ。局所複素振幅と回転包絡を

```math
a
=
\frac{Q+iP}{\sqrt{2\mathcal J_0}},
\qquad
b(t)
=
e^{i\omega_0t}a(t)
```

と定める。複素数は実2次元正準平面の表示であり、量子的な生成消滅演算子ではない。

摂動行列に対応する有効演算子を

```math
h_0
=
\frac{\mathcal J_0}{2M_{\rm osc}\omega_0}A
```

とする。$A$ が局所疎行列なら $h_0$ も同じグラフ上で局所的である。

## 9.4 反回転項を含む厳密局所方程式

<!-- theorem-start:theorem -->
**定理（局所回転包絡の厳密方程式）**
第9.2節のミクロ Hamiltonian に対し、局所回転包絡は厳密に

```math
i\mathcal J_0\dot b
=
h_0b
+
h_0e^{2i\omega_0t}\overline b
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
規格化座標で Hamiltonian は

```math
H_{\rm micro}
=
\frac{\omega_0}{2}
\left(P^{\mathsf T}P+Q^{\mathsf T}Q\right)
+
\frac{1}{2M_{\rm osc}\omega_0}
Q^{\mathsf T}AQ
```

となる。$Q=\sqrt{\mathcal J_0/2}(a+\overline a)$ を代入し、複素 Poisson 括弧を使うと

```math
i\mathcal J_0\dot a
=
\mathcal J_0\omega_0a
+
h_0
\left(a+\overline a\right)
```

を得る。$b=e^{i\omega_0t}a$ へ移れば結論が従う。
<!-- theorem-end:proof -->

第2項は反回転項である。位置結合だけの実ばね網では、この項を厳密に消すことはできない。従って

```math
i\mathcal J_0\dot b
=
h_0b
```

をミクロ方程式として最初から置くのは正しくない。第9章で、反回転項の効果を正常モード変換と弱結合展開により有限時間で評価する。

局所包絡から作る作用を

```math
I_{\rm loc}(t)
=
\mathcal J_0b(t)^\dagger b(t)
```

とする。厳密方程式から

```math
\frac{dI_{\rm loc}}{dt}
=
2
\operatorname{Im}
\left[
b^\dagger h_0
e^{2i\omega_0t}
\overline b
\right]
```

となり、一般には零でない。保存されるのはミクロエネルギーであり、局所回転包絡の作用ではない。

この点は第5章との接続で重要である。測定器へ入る直前の $I_{\rm loc}$ を読み、その時点の作用比 $I_k/I_{\rm loc}$ を使う単発測定は定義できる。しかし、伝播中の局所作用を厳密保存量として扱ったり、準備から測定まで自動的に同じ規格化が保たれると主張したりしてはならない。

## 9.5 厳密正常モード包絡

正定値行列

```math
\Omega
=
\left(
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
\right)^{1/2}
```

を定める。$\Omega$ を使って正常モード正準振幅 $c$ を作り、搬送回転を除いた厳密包絡を

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

とする。付録Gで正準変換を明示し、厳密に

```math
i\mathcal J_0\dot{\widetilde b}
=
h_{\rm ex}\widetilde b,
\qquad
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

が成立することを示す。

$\widetilde b$ は厳密に $\mathcal J_0\widetilde b^\dagger\widetilde b$ を保存する。ただし $\Omega$ の行列平方根を含むので、一般には各頂点だけで定義できる局所変数ではない。役割分担は次の通りである。

| 包絡 | 局所性 | 発展 | 作用保存 |
|---|---|---|---|
| $b$ | 頂点ごとに局所 | 反回転項を含めて厳密 | 一般には近似 |
| $\widetilde b$ | 一般には非局所 | $h_{\rm ex}$ で厳密 | 厳密 |
| 有効解 $b_L$ | 目標グラフ上で局所 | $h_L$ で近似 | 有効モデル内で厳密 |

## 9.6 目標グラフ演算子と弱結合量

有限空間グラフの重みを $g_{ij}=g_{ji}\geq0$ とし、

```math
\left(L_G\chi\right)_i
=
\sum_{j:\{i,j\}\in E}
g_{ij}
\left(\chi_i-\chi_j\right)
```

とする。目標とする実対称演算子を

```math
h_L
=
\frac{\mathcal J_0^2}{2m}L_G
+
V_L,
\qquad
V_L
=
\operatorname{diag}
\left(V_1,\ldots,V_L\right)
```

とする。古典パラメータを

```math
\kappa_{ij}
=
\frac{M_{\rm osc}\omega_0\mathcal J_0}{m}
g_{ij},
\qquad
\delta_i
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}
V_i
```

と選べば $h_0=h_L$ になる。従って、Laplacian の疎結合構造と局所ポテンシャルの形は、局所ばね結合と固有周波数離調から得られる。

一方、$m$ と $\mathcal J_0$ の値はこの対応式の設計パラメータである。特定の普遍定数または粒子質量がミクロ振動子網から必然的に選ばれることは示していない。

第9.6節の係数対応により $h_0=h_L$ とする。このとき

```math
A
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}h_L
```

であり、厳密正常モード生成子は

```math
h_{\rm ex}
=
\mathcal J_0\omega_0
\left[
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/2}
-I
\right]
```

となる。作用素ノルムによる無次元弱結合パラメータを

```math
\eta
=
\frac{\left\|A\right\|}
{M_{\rm osc}\omega_0^2}
=
\frac{2\left\|h_L\right\|}
{\mathcal J_0\omega_0}
```

とする。以下では $\eta<1$ を仮定する。この十分条件により

```math
I+
\frac{2h_L}{\mathcal J_0\omega_0}
>
0
```

が保証され、ミクロ剛性行列も正定値になる。

## 9.7 生成子と状態の有限時間誤差

<!-- theorem-start:theorem -->
**定理（正常モード生成子の誤差上界）**
$h_L=h_L^\dagger$、$\eta<1$ とする。このとき

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

が成立する。
<!-- theorem-end:theorem -->

証明は付録G.6に置く。実対称 $h_L$ の固有値ごとにTaylor剰余を評価するだけであり、本文では上界と物理的な補正の意味を用いる。

主項は

```math
h_{\rm ex}
=
h_L
-
\frac{h_L^2}{2\mathcal J_0\omega_0}
+
O
\left(
\frac{\left\|h_L\right\|^3}
{\mathcal J_0^2\omega_0^2}
\right)
```

である。補正 $h_L^2$ は一般に元のグラフより長距離の結合を含む。これは、厳密正常モード生成子が局所目標演算子と一致せず、局所性が弱結合近似として回復することを示す。

同じ初期値 $\widetilde b(0)$ から始める厳密解と目標有効解を

```math
\widetilde b(t)
=
e^{-ih_{\rm ex}t/\mathcal J_0}
\widetilde b(0),
```

```math
\widetilde b_L(t)
=
e^{-ih_Lt/\mathcal J_0}
\widetilde b(0)
```

とする。Duhamel 公式から

```math
\sup_{0\leq t\leq T}
\left\|
\widetilde b(t)-\widetilde b_L(t)
\right\|
\leq
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
\left\|\widetilde b(0)\right\|
```

を得る。自然な有効時間を

```math
T
=
c_T
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とすれば、相対誤差上界は

```math
\frac{c_T\eta}
{4\left(1-\eta\right)^{3/2}}
```

であり、固定 $c_T$ に対して $O(\eta)$ である。誤差は時間に比例して蓄積するため、$T$ を無制限に伸ばせる定理ではない。Duhamel評価の詳細は付録G.7に示す。

正定値行列

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2}
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

を定め、

```math
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

とする。付録Gの Bogoliubov 型正準変換は

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)}
```

である。逆変換も同じ $U_s,V_s$ を使う。

```math
\delta_{\rm loc}(\eta)
=
\left(1-\eta\right)^{-1/4}-1
```

と置くと、全時刻で

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}(\eta)
\left\|\widetilde b(0)\right\|
```

が成立する。$\delta_{\rm loc}=O(\eta)$ である。厳密だが非局所な包絡と、局所だが反回転項を持つ包絡の差を、この量で制御する。正準変換と上界は付録G.4、G.5に示す。

実際の局所初期値 $b(0)$ から始める目標解を

```math
b_L(t)
=
e^{-ih_Lt/\mathcal J_0}b(0)
```

とする。

<!-- theorem-start:theorem -->
**定理（局所包絡の有限時間近似）**
$\eta<1$ とする。第9章のミクロ解から作る局所包絡 $b(t)$ は

```math
\sup_{0\leq t\leq T}
\left\|
b(t)-b_L(t)
\right\|
\leq
\varepsilon_{\rm car}(T)
\left\|\widetilde b(0)\right\|
```

を満たす。ここで

```math
\varepsilon_{\rm car}(T)
=
2\delta_{\rm loc}(\eta)
+
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
```

である。
<!-- theorem-end:theorem -->

証明は付録G.5--G.7に置く。局所包絡と正常モード包絡の両端の変換差、およびDuhamel評価による中央の生成子差を加える。

自然時間 $T=O(\mathcal J_0/\|h_L\|)$ では $\varepsilon_{\rm car}=O(\eta)$ である。本稿で「局所古典振動子網から Schrödinger 型発展を導く」とは、この有限時間近似定理を意味する。

## 9.8 局所作用の変動

厳密包絡作用を

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
```

とする。これは保存される。局所作用との相対差は

```math
\left|
\frac{I_{\rm loc}(t)}{I_{\rm ex}}-1
\right|
\leq
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
```

である。従って局所作用は弱結合領域で $O(\eta)$ だけ振動し得る。局所作用を厳密保存量とする旧記述は、有効層内部の近似としてのみ維持する。詳細は付録G.8に示す。

## 9.9 干渉と補助的なM35受渡し

有効モデル内で入力1モードを等分岐し、2経路に位相 $\phi_1,\phi_2$ を蓄積して再結合すると

```math
\chi_+
=
\frac{e^{i\phi_1}+e^{i\phi_2}}{2},
\qquad
\chi_-
=
\frac{e^{i\phi_1}-e^{i\phi_2}}{2}
```

となり、

```math
p_+
=
\cos^2
\left(
\frac{\phi_1-\phi_2}{2}
\right),
\qquad
p_-
=
\sin^2
\left(
\frac{\phi_1-\phi_2}{2}
\right)
```

を得る。理想暗出力は $\phi_1-\phi_2=\pi$ で零になる。

ミクロ局所包絡では、反回転項と正常モード補正により出力方向が $O(\eta)$ だけずれる。暗出力確率の誤差は振幅誤差の2乗だけとは限らない。規格化と任意有限基底測定を含む安全な上界は、第5章で全変動距離として与える。

第9章のミクロ局所包絡を測定時刻 $T$ で規格化し、

```math
\widehat b_{\rm mic}(T)
=
\frac{b(T)}{\left\|b(T)\right\|}
```

とする。目標有効状態を

```math
\chi_L(T)
=
\frac{b_L(T)}{\left\|b_L(T)\right\|}
```

とする。任意の有限基底変換 $W$ に対し、実際の作用比と目標 Born 型重みを

```math
p_k^{\rm mic}
=
\left|
\left(W\widehat b_{\rm mic}\right)_k
\right|^2,
\qquad
p_k^L
=
\left|
\left(W\chi_L\right)_k
\right|^2
```

と定める。

<!-- theorem-start:proposition -->
**命題（包絡方向誤差から測定分布誤差への伝播）**
任意のユニタリ $W$ について、全変動距離は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\left\langle
\widehat b_{\rm mic},
\chi_L
\right\rangle
\right|^2
}
\leq
\left\|
\widehat b_{\rm mic}-\chi_L
\right\|
```

を満たす。
<!-- theorem-end:proposition -->

最初の不等式は純粋状態間の距離が任意の射影成分分布の全変動距離を上から抑えること、2番目は単位ベクトルのノルム評価から従う。ここでは量子測定を仮定していない。左辺は古典作用比を同じ基底 $W$ で比較した量である。

第9章の有限時間上界と $\delta_{\rm loc}<1$ を使うと、

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\varepsilon_{\rm dist}(T),
```

```math
\varepsilon_{\rm dist}(T)
=
\min
\left\{
1,
\frac{
2\varepsilon_{\rm car}(T)
}{
1-\delta_{\rm loc}(\eta)
}
\right\}
```

を得る。$\varepsilon_{\rm dist}$ は包絡方向のずれが測定分布へ伝わる誤差であり、環境誤差ではない。

本節の受渡しは、複素振幅場の作用比を任意有限基底で標本化する補助診断として残す。M42の基本位置測定は、M35が測定時にセルを選ぶ方式ではなく、既に局在している実現配置を第9.16節の局所検出器が読む方式である。2モードの完全周期は第3章のM38で独立に扱う。

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。M35だけを使う場合、これは複素振幅場の空間セル基底を標本化する式に留まる。M42は独立変数 $X$ とその等変力学を追加し、固定時刻の局所位置検出を別に構成する。従ってR87は削除せず、M42の初期準備と検算に使える補助的な作用標本化結果へ位置づける。

## 9.10 共通モデルの空間実現配置

R62が示すとおり、相関行列、階数1因子、複素振幅場の作用比だけでは1試行の位置、等変流、局所位置検出は決まらない。共通モデルはこの不足を解釈で埋めず、独立の正準変数 $(Z,P_Z)$ を置き、その粗視化セル位置を $X=X(Z)$ とする。

複素振幅場 $b$ はM37の全空間振動子網へ広がり、相対振幅、相対位相、局所辺流を担う。実現配置 $(Z,P_Z)$ は1個の古典局在自由度であり、頂点断面では $X(Z)$ が1個のセルを、輸送窓中は $Z$ が選択された1本の隣接辺チャネル上の位置を表す。$|b_i|^2$ は場の局所作用比であると同時に、適切に準備された実現配置集団の粗視化位置分布になる。場の作用が複数の粒子断片を表すとは解釈しない。

実現配置が複素振幅場の全エネルギー、慣性質量、電荷を運ぶことは示していない。有限幅辺チャネル内の軌道は構成するが、格子細分化で得る連続空間極限は本稿の範囲外である。

## 9.11 局所辺流と理想最小跳躍過程

規格化した理想担体を

```math
i\mathcal J_0\dot b_L
=
h_Lb_L,
\qquad
p_i
=
|b_{L,i}|^2
```

とし、有向辺流を

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
b_{L,j}^*h_{L,ji}b_{L,i}
\right)
```

とする。Hermitian性とグラフ局所性から

```math
J_{i\to j}
=
-J_{j\to i},
\qquad
\dot p_i
=
\sum_{j:j\sim i}
J_{j\to i}
```

が厳密に成立する。M37の局所包絡 $b_{\rm mic}$ から同じ式で計算する量は、反回転項のため厳密なM37作用流でなく、目標流の局所推定値である。

$p_i>0$ での最小跳躍率を

```math
\lambda_{i\to j}
=
\frac{[J_{i\to j}]_+}{p_i}
```

と定義する。これは標準流を実現する既知のBell型最小率である [44]。連続方程式だけでは率は一意でなく、対称な往復流を加えられる。M42は余分な対称流を持たない最小率をモデル定義として採用する。

<!-- theorem-start:theorem -->
**定理（理想実現配置のBorn型等変性）**
初期分布が

```math
P(X_0=i)
=
|b_{L,i}(0)|^2
```

なら、全ての有限時刻で

```math
P(X_t=i)
=
|b_{L,i}(t)|^2
```

が成立する。さらに最大重み付き次数を $h_1=\max_i\sum_{j:j\sim i}|h_{L,ij}|$ とすると、有限時間の期待跳躍数は

```math
\mathbb E[N_T]
\leq
\frac{h_1T}{\mathcal J_0}
```

であり、有限時間爆発は起こらない。
<!-- theorem-end:theorem -->

証明は付録H.1、H.2に置く。節で率が特異でも等変分布下の無条件流は有限であり、有限状態・有界生成子は既知の大域存在定理 [45] の範囲に入る。R113はこの有限グラフへの適用、等変性、期待跳躍数評価を整理する。理想跳躍則そのものを本稿の新規結果とはしない。

## 9.12 初期作用比準備と有限履歴測度

等変性は初期Born型分布を生成しない。初期実現配置を任意の分布から $p(0)$ へ収束させる定理も得ていない。M42では、M35の作用区間選択器を使う初期準備を別の物理過程として置く。

初期作用

```math
I_i(0)
=
\mathcal J_0
|b_{L,i}(0)|^2
```

を全セルから読み、1個の初期選択器角を累積作用区間へ入れ、選択されたセルへ実現配置を運ぶ。選択履歴を外部セルへ残し、理想空読出し入口では担体を変えない。これは一般には大域準備である。準備後の辺流読出し、隣接移動、位置検出は局所的に行う。

固定有限時間を $K$ 回の更新へ分ける場合、初期角と更新角

```math
(\vartheta_0,\vartheta_1,\ldots,\vartheta_K)
\in
\mathbb T^{K+1}
```

へ積Haar測度を置く。これは固定有限個の選択器を最初から含む有限閉鎖Hamiltonian集団である。無理数平行移動で長期頻度として実現する場合も、一意エルゴード性だけを使い、混合性または独立同分布型有限標本揺らぎを主張しない。無期限Markov記述には新規の選択器セル流が別に必要である。

## 9.13 有界率no-goと節一様正則化

一様有界な全脱出率 $\Lambda_i(t)\leq\Lambda_{\max}$ を持つ連続時間Markov跳躍過程では、$q_i(s)>0$ なら

```math
q_i(t)
\geq
q_i(s)
e^{-\Lambda_{\max}(t-s)}
>
0
```

である。従って正の占有を有限時間で厳密零へ送ることはできない。R114はこの対象を一様有界率Markov過程に限定した否定的結果であり、一般のHamiltonian流や離散Poincaré写像を禁止しない。

有限装置では、流の正部分と分母を

```math
r_\sigma(z)
=
\frac12
\left(
z+\sqrt{z^2+\sigma^2}
\right),
```

```math
\lambda_{i\to j}^{\rho,\sigma}
=
\frac{
r_\sigma(J_{i\to j})
}{
p_i+\rho
}
```

と正則化する。$\rho>0$ は無次元、$\sigma>0$ は時間の逆数を持つ。従って次元の異なる $\rho$ と $\sigma$ を等置しない。1パラメータ化する場合は率尺度 $\Omega_*$ を使い、$\sigma=\Omega_*\rho$ とする。

最大次数を $d_*$、辺重み和を $H_E=\sum_{\{i,j\}\in E}|h_{L,ij}|$ とすると、

```math
\Lambda_*^{\rho,\sigma}
\leq
\frac{h_1}{\mathcal J_0\sqrt\rho}
+
\frac{d_*\sigma}{2\rho}
```

であり、正則化過程の分布 $q^{\rho,\sigma}$ は初期分布を $p(0)$ に合わせれば

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
q^{\rho,\sigma}(t),p(t)
\right)
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}
\sqrt\rho
\right]
```

を満たす。これがR115である。証明と理想軌道分布への結合は付録H.3--H.5に置く。有限 $\rho,\sigma$ では小さな逆向き跳躍を含み、理想最小過程そのものではない。有限装置が保証するのは節占有確率を任意に小さくできることであり、厳密零ではない。

## 9.14 局所Hamiltonian更新と履歴保存

刻み $\Delta=T/K$ を $\Delta\Lambda_*^{\rho,\sigma}\leq1-\kappa$ となるよう選ぶ。現在セル $i$ で

```math
I_i^\rho
=
\mathcal J_0
(p_i+\rho),
```

```math
A_{i\to j}
=
\mathcal J_0\Delta
r_\sigma(J_{i\to j}),
```

```math
A_{i\to0}
=
I_i^\rho
-
\sum_jA_{i\to j}
```

と置く。全て非負で総和は $I_i^\rho$ なので、M35型選択器は除算せずに待機または隣接辺を排他的に選ぶ。比較境界は無反応結果とし、無反応試行を捨てない。

実現配置は、グラフを頂点領域と細い辺チャネルで実現した配置空間上の1個の正準位置 $Z$ である。安全枝では選択された1本の辺の余接持上げだけを起動し、入口頂点断面から出口頂点断面へ有限時間で運ぶ。従ってPoincaré断面では $X(Z)$ が厳密に1セルを指し、輸送中も $Z$ は1本の辺チャネルにだけ存在する。単一占有の波動モードをSWAPする模型としては定義しない。

異なる旧位置や選択辺が同じ終点へ到達しても、使用済み履歴セルに旧位置、枝、待機、比較無反応の別を残す。これにより全Hamiltonian写像の1対1性を保つ。各時刻層・各頂点へ局所判定セルを事前配置する単純上界は

```math
O
\left(
K
\left(
L+|E|
\right)
\right)
```

であり、有限次数グラフでは $O(KL)$ である。$O(L+K)$ を主張するには移動式制御器または明示的な局所通信路が別に必要である。

M37は読出し、比較、輸送中にも発展する。複素振幅場を都合よく停止せず、窓内変化、読出し時刻と輸送完了時刻のずれ、時計窓との非可換性を $\varepsilon_{\rm win}$ として数える。R116は固定 $K$ の局所更新、履歴保存、有限閉鎖埋込、無期限時の弱開放セル流、固定時刻検出をまとめる。

## 9.15 M37から実現配置分布への誤差伝播

固定した $\rho,\sigma>0$ では、担体振幅から正則化生成子への写像は有界球上で滑らかである。Lipschitz定数を $L_{\rho,\sigma,h,R}$ とし、R86の包絡誤差を使うと、M37入力と理想担体入力による実現配置分布の差は

```math
\varepsilon_{\rm car\to X}
\leq
T
L_{\rho,\sigma,h,R}
\varepsilon_{\rm car}(T)
\|\widetilde b(0)\|
```

で抑えられる。正則化を固定した後では節で発散しない。これはR117であり、詳細は付録H.10、H.11に置く。

M42の固定時間における誤差台帳は

```math
\begin{aligned}
\varepsilon_{\rm Q3}
\leq{}&
\varepsilon_{\rm init}
+
\varepsilon_{\rm reg}
+
\varepsilon_{\rm disc}
+
\varepsilon_{\rm sel}\\
&+
\varepsilon_{\rm hop}
+
\varepsilon_{\rm win}
+
\varepsilon_{\rm car\to X}
+
\varepsilon_{\rm det}
\end{aligned}
```

である。パラメータは、まず $\rho,\sigma$、次にM37弱結合量 $\eta$、次に $\Delta,K$、最後に比較幅、角切断、輸送、時計、記録精度の順で選ぶ。従って任意の $\epsilon>0$ に対し、全更新時刻で

```math
D_{\rm TV}
\left(
\mathcal L(X_n),
\{|b_{L,i}(t_n)|^2\}_{i=1}^L
\right)
<
\epsilon
```

となる有限自由度・有限パラメータ構成を選べる。ただし精度を上げても固定帯域・固定最大結合の同じ装置で済むとは主張しない。

## 9.16 固定時刻の局所位置検出

頂点 $i$ の検出断面上で1となり、他の頂点領域と辺チャネル上では支持が交わらない滑らかな局所関数を $d_i(Z)$ とし、局所検出器の正準読出しを $(D_i,P_{D_i})$ とする。

```math
G_{\rm det}
=
\sum_i
d_i(Z)
P_{D_i}
```

を使えば、理想空入口 $P_{D_i}=0$ で実現配置への反作用なしに、該当する1個の検出器だけを作動できる。従って

```math
P(D_i=1)
=
P(X=i)
\simeq
|b_{L,i}|^2
```

となる。Born型位置重みを検出器が測定時に新しく生成するのではない。初期作用比準備で与えた分布を実現配置力学が等変に保ち、検出器はそれを局所的に読む。

これは予定時刻の局所読出しであり、Q3-4とQ3-5の改訂後の固定判定へ接続できる。Q3-4では障壁反対側の頂点集合、Q3-5では全頂点の位置分布を読むだけでよく、源、シャッター、全検出器のHamiltonianを同時に構成する必要はない。初回到達、吸収条件、時間積分流束、散乱極限、連続運転スクリーンを主張するには別の装置構成が必要だが、これらは固定達成条件より強い拡張である。Q3-4とQ3-5の最小有限例と正式な確率差の導出は次段階に残る。

## 9.17 数値検算

8振動子の1次元鎖に弱い調和型離調を加え、固定目標 $h_L$ に対して $\omega_0$ を変えた。初期局所包絡は乱数種 `20260809` の複素ベクトルを規格化し、観測時刻を

```math
T
=
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とした。作用素誤差は $\|h_{\rm ex}-h_L\|$、局所状態誤差は $\|b(T)-b_L(T)\|$ である。

| $\omega_0$ | $\eta$ | 作用素誤差 | 局所状態誤差 | 規格化状態の距離 |
|---:|---:|---:|---:|---:|
| 20 | 0.1793 | 0.07391 | 0.03045 | 0.02890 |
| 40 | 0.08967 | 0.03849 | 0.01928 | 0.01690 |
| 80 | 0.04483 | 0.01966 | 0.01078 | 0.00959 |

全例で作用素上界、厳密包絡の状態上界、局所包絡の状態上界、局所作用変動上界を満たした。$\omega_0=40$ から80への倍増で作用素誤差は1.96分の1、局所状態誤差は1.79分の1になり、弱結合極限での $O(\eta)$ 収束と整合する。この表は `tools/verify_envelope_reduction.py` から再現できる。

M42については、乱数種 `20260812` の6頂点鎖、厳密節を持つ2頂点模型、複素Hermitian 3頂点模型、4頂点CNOT辺を使って42件を検査した。中心値は次のとおりである。

| 検査 | 実測値 | 解析上界または許容値 |
|---|---:|---:|
| 連続方程式誤差 | $3.469\times10^{-17}$ | $\leq2\times10^{-11}$ |
| 最小率master誤差 | $5.551\times10^{-17}$ | $\leq2\times10^{-11}$ |
| 2頂点厳密節占有 | $3.749\times10^{-33}$ | $\leq2\times10^{-30}$ |
| 正則化最大脱出率 | $2.227$ | $\leq10.8$ |
| 正則化全変動距離 | $1.696\times10^{-2}$ | $\leq5.40\times10^{-1}$ |
| Euler最小誤差比 | $2.001$ | $\geq1.85$ |
| 初期作用比頻度誤差 | $2.538\times10^{-6}$ | $\leq5\times10^{-6}$ |
| 場摂動全変動距離 | $1.359\times10^{-5}$ | $\leq2.401\times10^{-4}$ |

非隣接率が零であること、確率保存、非負性、待機作用、履歴セルの単射性に加え、複素Hermitian流の等変性、1辺射影のCNOT行列、共同実現配置の真理値表、R122の位置ばね誤差上界も合格した。この表は `tools/verify_realized_configuration.py` から再現できる。数値検算は解析証明の代わりではなく、添字、符号、係数、離散化を監査する回帰検査である。

## 9.18 Q3-1の達成判定と限界

本稿の固定されたQ3-1達成基準は、局所位置結合振動子網から空間格子上の Schrödinger 型時間発展を、近似範囲と誤差を伴って導くことである。本章のM37部分は次を与えた。

1. 有限個の実古典振動子からなる局所位置結合 Hamiltonian 。
2. 反回転項を含む局所包絡の厳密方程式。
3. 厳密正常モード包絡と生成子 $h_{\rm ex}$。
4. 目標実対称 $h_L$ との係数対応。
5. 弱結合・弱離調・有限時間の作用素誤差と状態誤差。
6. 再現可能な数値検算。

従って、Q3-1はこの限定された有限実対称モデルについて達成と判定する。これは量子力学の必然的創発を示す結果ではなく、局所古典振動子網における制御された Schrödinger 型有効力学である。

Q3-1の固定基準自体はR83--R88で満たされ、今回の改訂で後から基準を広げたわけではない。R112--R117は、共通有限モード代数、独立実現配置、初期作用比準備、Born型等変性、節を含む有限率近似、局所Hamiltonian更新、固定時刻検出を追加する強化結果である。

位置ばね結合から直接得られる $A$ と $h_L$ は実対称である。磁場に対応する Peierls 位相、一般の複素 hopping、運動量に比例する結合は本定理に含まれない。これらを厳密に実装するには、位置と運動量の両方を結ぶ追加の正準結合が必要になる。

本稿のQ3-1定理は時間非依存 $A$ に限定する。時間依存 $A(t)$ が有界であるだけでは不十分である。$2\omega_0$ 近傍の Fourier 成分が反回転項と共鳴し得るため、時間依存駆動には例えば

```math
\frac{\sup_t\left\|h_L(t)\right\|}
{\mathcal J_0\omega_0}
\ll1,
\qquad
\frac{\sup_t\left\|\dot h_L(t)\right\|}
{\mathcal J_0\omega_0^2}
\ll1
```

のような低速条件、または明示的な非共鳴条件が別に必要である。M38のQ1-1はこの位置ばね近似を使わず厳密に閉じる。時間依存M37を同じハードウェアへ統合する課題は、Q3-1を超える一般化として第10章に残す。

次はQ3-1の固定達成基準を超える一般化であり、本章の結論に含めない。

1. $\mathcal J_0$ と有効質量 $m$ の普遍的な値の導出。
2. 一般の複素 Hermitian 演算子と磁場結合。
3. 時間依存駆動に対する一様な非共鳴定理。
4. 非線形ミクロ結合に対する閉包。
5. 一般連続極限と境界条件の一様誤差。
6. 格子細分化で得る連続空間の粒子軌道、位相量子化、多実現配置。
7. 任意の初期実現配置分布からBorn型分布への収束、初期作用比準備を不要にする機構。
8. 実現配置の慣性質量、電荷、担体エネルギーとの同定。
9. 有限帯域装置による厳密節追跡、固定性能の同じ装置による誤差零極限。
10. 1次元井戸型・調和型ポテンシャルの低位束縛スペクトルと、エネルギー保存型の有限時間デコヒーレンス。
11. 障壁値未満状態の障壁反対側への位置確率移動、および有限グラフ2経路入力のコヒーレント分布と非干渉混合の差を、固定時刻位置読出しへ接続する最小例。
12. 源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを扱う、固定目標より強い装置模型。

M42はBorn型位置分布を「初期作用比準備と等変保存」に分ける。等変性だけで初期分布の起源を説明したとはしない。M35による直接セル標本化は補助診断として残し、M42の固定時刻位置検出とは混同しない。
