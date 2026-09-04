@number: 6
@chapter: 本文
@title: M37空間担体とM42局在トークン
@status: M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似をR86へ保ち、その下流に単一試行の局在粒子トークンM42を置く。M51準備、M37担体、R172--R174の等変輸送、有限衝突bath、終位置記録を二層模型として接続する。

## 6.1 Q3の二層基本模型とM37の範囲

Q3の単一試行系は、M37担体層とM42粒子層を区別する。

| 層 | 単一試行で物理的に存在するもの | 派生表示・集団記述 | 役割 |
|---|---|---|---|
| M37担体 | 有限個の実振動子座標 $(q_i,p_i)$ と局所ばね結合 | 局所複素包絡 $b_i$、統計ray、規格化第2モーメント | R86の有限時間Schrödinger型担体 |
| M42粒子 | 1個の局在位置 $X_t$、局所辺bath、clock、履歴、記録 | 位置分布 $P(X_t=i)$ | R172--R174の局所輸送と終位置記録 |

複素包絡は実振動子状態の派生座標であり、複素rayと位置分布は多数試行の統計である。一方、$X_t$ は各試行に1つ存在する粒子位置である。M37だけから粒子位置や最小率が必然的に出るとは主張せず、M42の局所率、bath cell、更新則を追加の採用ミクロ法則として明示する。

共通M51/R171は、M37へ入れる前の実正準seed集団を開放driftでrank-one rayへ準備する。準備後の同じ単一試行信号にM50/R164の作用殻選択を一度だけ適用してM42の初期位置 $X_0$ を作る。その後はM37とM42を同時に進め、終時刻には新しい位置を再標本化せず、既存の $X_T$ をR112の局所記録回路で読む。このためM51、初期R164選択、終位置記録を独立なBorn型確率源として数えない。

ミクロ振動子層から有効担体への移行はQ3-1の固定達成基準であり、R86が満たす。M42は粒子実体と下流現象を追加する強化であって、Q3-1の判定へ遡及的に要求しない。M51のport、M37局所ばね網、初期作用殻、M42衝突bath、記録を同じ有限局所装置へ統合したとも扱わない。

Q1はM47のW型2モード、Q2-2はM52駆動R180 paired-Hopf receiver、固定時刻の一般枝instrumentはM50/R170を使う。M42はQ3の空間セルだけに採用する。任意の装置用正準混合がM37の局所ばね網だけで実装できるとは仮定しない。M37がM47へ供給するのは、時間非依存の対称W型生成子、最低2固有モード、スペクトル間隔である。

振動子の個数を $L<\infty$、共通質量を $M_{\rm osc}>0$、搬送周波数を $\omega_0>0$ とする。$M_{\rm osc}$ はミクロ振動子の質量であり、第6.6節に現れる有効質量 $m$ と区別する。固定作用尺度 $\mathcal J_0>0$ は正準座標の規格化に使う。

有限次元 Schrödinger 方程式を古典正準座標または結合振動子へ写すこと自体は既知である [34--37]。特に、位置結合だけを用いる弱結合近似と、位置・運動量の両結合を用いる厳密写像は先行研究で区別されている [35--37]。

本稿は次を新規性として主張しない。

1. 複素ベクトルを2倍次元の実ベクトルで表すこと。
2. 任意の Hermitian 行列を設計済み2次 Hamiltonian へ埋め込むこと。
3. 結合振動子が Schrödinger 型運動を近似できること。

本稿で追加するのは、局所位置結合網について反回転項を落とさない厳密式、正常モード生成子との作用素誤差、有限時間状態誤差、局所包絡誤差から有限基底測定分布への伝播を同じ誤差台帳で接続することである。

## 6.2 ミクロHamiltonian

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

## 6.3 局所正準座標と回転包絡

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

## 6.4 反回転項を含む厳密局所方程式

**R86の厳密局所方程式。**
第6.2節のミクロ Hamiltonian に対し、局所回転包絡は厳密に

```math
i\mathcal J_0\dot b
=
h_0b
+
h_0e^{2i\omega_0t}\overline b
```

を満たす。
第2項は反回転項である。位置結合だけの実ばね網では、この項を厳密に消すことはできない。従って

```math
i\mathcal J_0\dot b
=
h_0b
```

をミクロ方程式として最初から置くのは正しくない。第6章で、反回転項の効果を正常モード変換と弱結合展開により有限時間で評価する。

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

この点は第2章との接続で重要である。測定器へ入る直前の $I_{\rm loc}$ を読み、その時点の作用比 $I_k/I_{\rm loc}$ を使う単発測定は定義できる。しかし、伝播中の局所作用を厳密保存量として扱ったり、準備から測定まで自動的に同じ規格化が保たれると主張したりしてはならない。

## 6.5 厳密正常モード包絡

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

とする。付録Eで正準変換を明示し、厳密に

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

## 6.6 目標グラフ演算子と弱結合量

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

第6.6節の係数対応により $h_0=h_L$ とする。このとき

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

## 6.7 生成子と状態の有限時間誤差

**R86の生成子誤差節。**
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
証明は付録E.6に置く。実対称 $h_L$ の固有値ごとにTaylor剰余を評価するだけであり、本文では上界と物理的な補正の意味を用いる。

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

であり、固定 $c_T$ に対して $O(\eta)$ である。誤差は時間に比例して蓄積するため、$T$ を無制限に伸ばせる定理ではない。Duhamel評価の詳細は付録E.7に示す。

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

とする。付録Eの Bogoliubov 型正準変換は

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

が成立する。$\delta_{\rm loc}=O(\eta)$ である。厳密だが非局所な包絡と、局所だが反回転項を持つ包絡の差を、この量で制御する。正準変換と上界は付録E.4、E.5に示す。

実際の局所初期値 $b(0)$ から始める目標解を

```math
b_L(t)
=
e^{-ih_Lt/\mathcal J_0}b(0)
```

とする。

<!-- theorem-start:theorem -->
**定理（R86：M37有限時間包絡線縮約）**

$h_L$ が時間独立な実対称行列で $\eta<1$ とする。第6.4節の反回転項を含む厳密局所方程式、第6.5節の厳密正常モード包絡、第6.7節の生成子誤差を同時に用いると、第6章のミクロ解から作る局所包絡 $b(t)$ は

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

である。厳密正常モード作用は保存され、局所作用の相対変動は第6.8節の $2\delta_{\rm loc}+\delta_{\rm loc}^2$ 以下である。規格化した包絡方向を任意の有限基底で比較した分布誤差は、第6.9節の $\varepsilon_{\rm dist}(T)$ 以下である。
<!-- theorem-end:theorem -->

証明は付録E.5--E.7に置く。局所包絡と正常モード包絡の両端の変換差、およびDuhamel評価による中央の生成子差を加える。

自然時間 $T=O(\mathcal J_0/\|h_L\|)$ では $\varepsilon_{\rm car}=O(\eta)$ である。本稿で「局所古典振動子網から Schrödinger 型発展を導く」とは、この有限時間近似定理を意味する。

## 6.8 局所作用の変動

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

である。従って局所作用は弱結合領域で $O(\eta)$ だけ振動し得る。局所作用を厳密保存量とする旧記述は、有効層内部の近似としてのみ維持する。詳細は付録E.8に示す。

## 6.9 干渉と有限基底作用比の診断

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

ミクロ局所包絡では、反回転項と正常モード補正により出力方向が $O(\eta)$ だけずれる。暗出力確率の誤差は振幅誤差の2乗だけとは限らない。規格化と任意有限基底測定を含む安全な上界は、第2章で全変動距離として与える。

第6章のミクロ局所包絡を測定時刻 $T$ で規格化し、

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

**R86の有限基底分布系。**
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
最初の不等式は純粋状態間の距離が任意の射影成分分布の全変動距離を上から抑えること、2番目は単位ベクトルのノルム評価から従う。ここでは量子測定を仮定していない。左辺は古典作用比を同じ基底 $W$ で比較した量である。

第6章の有限時間上界と $\delta_{\rm loc}<1$ を使うと、

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

本節の式は、派生複素包絡の作用比を任意有限基底で比較する診断であり、それだけでは単一試行の粒子を作らない。Q3では準備終了面で1回だけ初期M42位置を作り、空間セル基底の局所辺流に沿って同じ粒子を輸送する。任意の基底 $W$ で終時刻に新しい粒子位置を作るR170と、M42の連続位置過程を同じ運転へ重ねない。Q1のW型2モード測定は第3章で独立に扱う。

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。これは空間セル基底の目標位置分布である。R172は同じ分布をM42トークンの等変分布として全有限時刻へ運び、R173は節正則化と有限衝突Hamiltonian近似を与える。R86の作用比だけを粒子実体と同一視せず、粒子層の追加方程式と初期選択を必要とする。

## 6.10 M37標本集団と統計共分散

同じM37装置を反復する試行空間を $(\mathcal P,\mu)$ とし、局所包絡を複素確率変数

```math
Z_t(\omega):=b(t;\omega)\in\mathbb C^L
```

として扱う。有限で正の集団作用

```math
S_t=\mathbb E_\mu[Z_t^\dagger Z_t]
```

を仮定し、規格化自己共分散を

```math
C_Z(t)
=
\frac{\mathbb E_\mu[Z_tZ_t^\dagger]}{S_t}
```

と定める。$C_Z$ は正半定値、trace 1である。これは集団記述であり、単一試行で装置が読む変数ではない。各試行のM37包絡 $Z_t(\omega)$ は、準備終了面では初期M42位置選択へ、輸送中はM42の局所rate controllerへ渡す派生物理信号である。

本稿では $C_Z$ を「非中心化自己共分散」、すなわち規格化した第2モーメントとして使う。通常の中心化共分散を意味せず、$\mathbb E[Z_t]=0$ の場合にだけ中心化した量と比例して一致する。R168の支持結論はこの非中心化定義に対する主張であり、中心化共分散の階数1条件だけからは従わない。

初期集団をM51で準備する場合、設定前seed測度を $\mu_{\rm seed}$、準備切断面を $t_{\rm cut}$ とし、

```math
\mu_{\rm cut}^{c}
=
(\Phi_c^{t_{\rm cut}})_\#\mu_{\rm seed}
```

をM37初期面へ渡す。R171の安全事象外は無反応として残し、安全集団の第2モーメントだけが $cc^\dagger$ へ有限誤差で近づく。M37の初期分布へ $C_Z(0)=cc^\dagger$ を直接仮定する経路と、M51の押出し測度から得る経路を同じ準備状態と呼ばない。

## 6.11 共通R135のM37有限時間特殊化

理想有効発展を

```math
U_L(t)=\exp\left(-ih_Lt/\mathcal J_0\right)
```

とし、同じ初期標本から作る理想包絡を $\widetilde Z_t=U_L(t)\widetilde Z_0$ とする。$\widetilde S_0=\mathbb E\|\widetilde Z_0\|^2$ とし、実際の $S_t=\mathbb E\|Z_t\|^2$ に対して

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置く。

**R135のM37特殊化。**

全試行でR86の相対包絡誤差

```math
\|Z_t-\widetilde Z_t\|
\leq
\varepsilon_{\rm car}(T)\|\widetilde Z_0\|
```

が $0\leq t\leq T$ に一様に成り立つとする。このとき

```math
D_{\rm tr}
\left(
C_Z(t),
U_L(t)C_Z(0)U_L(t)^\dagger
\right)
\leq
\min\{1,r_T\},
```

```math
r_T
=
2\varepsilon_{\rm car}(T)\sqrt{\kappa_T}
+\varepsilon_{\rm car}(T)^2\kappa_T
```

が成り立つ。$S_0=\widetilde S_0$ で、R86の局所--正常モード比較から $S_t\geq(1-\delta_{\rm loc})^2S_0$、$\delta_{\rm loc}=(1-\eta)^{-1/4}-1<1$ を使う場合、$q_T=\varepsilon_{\rm car}/(1-\delta_{\rm loc})$ と置けば $r_T\leq2q_T+q_T^2$ としてよい。
証明は付録F.2に置く。同じM37包絡差を、担体誤差、共分散誤差、ray誤差へ別々に加算しない。どの段階で規格化したかを固定し、一つの上流誤差から必要な下流評価だけを選ぶ。

## 6.12 M42局在トークンとR172--R173

M42は、M37担体と別の実体として有限グラフ上に1個の粒子位置 $X_t$ を置く。理想有効包絡 $b_L$ の頂点重みと局所辺流を

```math
p_i(t)=|b_{L,i}(t)|^2,
\qquad
J_{i\to j}(t)
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left[
b_{L,j}^*h_{L,ji}b_{L,i}
\right]
```

とし、$p_i>0$ で

```math
\lambda_{i\to j}(t)
=
\frac{[J_{i\to j}(t)]_+}{p_i(t)}
```

を採用する。

<!-- theorem-start:theorem -->
**定理（R172：M37有効辺流に沿うM42局在トークンの等変輸送）**

有限グラフ上の時間連続な有界局所Hermitian生成子と上の最小率を仮定する。$P(X_0=i)=p_i(0)$ なら全有限時刻で $P(X_t=i)=p_i(t)$ が成り立つ。さらに $h_1=\sup_t\max_i\sum_{j:j\sim i}|h_{L,ij}(t)|$ とすれば、$\mathbb E[N_T]\leq h_1T/\mathcal J_0$ であり、有限時間爆発はない。
<!-- theorem-end:theorem -->

これは粒子位置が統計量だという意味ではない。各試行では $X_t$ が1頂点に局在し、上の分布は試行集団の記述である。

節で有限装置を保つため、正則化率を

```math
\lambda_{i\to j}^{\rho,\sigma}(b)
=
\frac{
\left[
J_{i\to j}(b)+
\sqrt{J_{i\to j}(b)^2+\sigma^2}
\right]/2
}{|b_i|^2+\rho}
```

とする。

<!-- theorem-start:theorem -->
**定理（R173：M42の節一様正則化と有限衝突Hamiltonian近似）**

正則化M42を理想分布と同じ初期分布から開始すると、固定有限時間 $T$ で理想分布との差は

```math
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]
```

以下である。さらに固定 $\rho,\sigma,T$ では、正則化生成子を有限時間窓ごとに凍結し、方向タグ、物理閾値座標、仕事register、履歴を持つ駆動衝突cellを辺ごとに配置した有限Hamiltonian散乱列が縮約経路測度を任意精度で近似する。一般のM42率は詳細釣合いを満たさないため、R162の平衡率公式をそのまま用いる主張ではない。
<!-- theorem-end:theorem -->

完全状態にはM37の実振動子、現在位置、入射bath cell、到着clock、運動方向、物理閾値座標、反射・通過、仕事register、出射エネルギー、使用済み履歴を含める。単一試行のpiecewise deterministic方程式、方向別衝突写像、正則化証明、資源発散は付録Nに置く。

### 固定時刻M50診断との区別

共通R168は、M37標本を任意の固定時刻にM50へ渡した場合の枝統計を診断する一般定理として引き続き成立する。ただし現行Q3の粒子経路では、終時刻R170による新しい位置の再標本化に使わない。次の式はM51準備、R135共分散、M42初期選択の整合を検査するために残す。

階数1の場合、$C_Z(t_\star)=c_\star c_\star^\dagger$ なら、付録Lの支持補題から

```math
Z_{t_\star}(\omega)
=
\alpha(\omega)c_\star
\qquad
\mu\text{-a.s.}
```

である。M50制御器が受け取るのは集団因子 $c_\star$ でなく、各試行の $Z_{t_\star}(\omega)$ である。

安全事象を

```math
G=\{Z_{t_\star}\neq0\}\cap G_{\rm hold}\cap G_{\rm guard}
```

とし、安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

と定める。これはtrace $P(G)$ の非規格化行列であり、失敗質量を捨てない。

**R168へのM37代入。**

$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ とする。各安全試行のM50枝分布を平均し、失敗を無反応へ送ると、完全結果分布は

```math
P(i)
=
\mathbb E
\left[
\mathbf1_G\pi_i^\delta(Z_{t_\star})
\right]
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
```

```math
P(\varnothing)=P(G^c)
```

である。さらに次が成り立つ。

1. $C_Z=c_\star c_\star^\dagger$ かつ $G$ 上で信号が非零なら、$Z=\alpha c_\star$ であり、$R_Z^G=P(G)c_\star c_\star^\dagger$ となる。
2. $Z^\dagger Z=s_*>0$ がほとんど確実で $P(G)=1$ なら、$R_Z^G=C_Z$ である。
3. 一般の可変作用集団では $R_Z^G$ が物理的な読出し対象であり、$C_Z$ への置換には半径方向補正と無反応質量の評価が必要である。

近似ray $\widehat Z$ が目標rayから純粋状態距離 $s$ 以内なら、対応する安全分布の全変動距離は $s/(1+\delta)$ 以下である。成功試行だけで再規格化しない。
$P(G)=1$ の可変作用集団では、$\overline S=\mathbb E[Z^\dagger Z]$ とすると

```math
D_{\rm tr}(R_Z^G,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{Z^\dagger Z}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}(Z^\dagger Z)}}{\overline S}.
```

この補正は一般には零でない。可変作用反例を付録Fに残す。R135の規格化方向誤差を使う場合、$q_T<1$ なら $\rho_T=q_T/(1-q_T)$ を安全なray誤差上界として選べる。

## 6.13 M51--M37--M42の開始面と終位置記録

準備切断時刻を $t_0$、終位置記録時刻を $T>t_0$ とする。M51/R171の切断面からM37初期面へ実正準担体を渡し、同じ試行の $Z_{t_0}(\omega)$ にM50/R164の作用殻選択を一度だけ適用して初期位置 $X_{t_0}$ を作る。統計因子 $c$、$C_Z$、全位置分布をcontrollerへ再注入せず、各試行の実信号と作用殻だけを使う。

$t_0<t<T$ では、M37実振動子とM42の現在位置、局所bath cell、clock、履歴を同時に進める。時刻 $T$ では別のM50位置を生成せず、R112の局所記録剪断で既存の $X_T$ を記録 $D_{X_T}$ へ写す。M50/R164は初期位置の物理化、R172/R173は同じ粒子の輸送、R112は終位置の記録を担う。

<!-- theorem-start:theorem -->
**定理（R174：M51--M37--M42の有限時間準備・輸送・記録受渡し）**

固定有限グラフと固定時間 $T$ について、M51/R171で担体集団を準備し、同じ試行の初期信号にM50/R164を一度だけ適用して $X_{t_0}$ を作り、M37と正則化M42を同時に進め、既存の $X_T$ をR112で記録する。完全結果分布と理想Born型位置分布の全変動距離は第6.14節の $\varepsilon_{174}(T)$ 以下である。安全事象外とcell overflowは無反応へ残し、成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

## 6.14 誤差、時間、資源、Q3-4・Q3-5への接続

R174の完全結果分布誤差を

```math
\begin{aligned}
\varepsilon_{174}(T)
\leq{}&
\varepsilon_{\rm prep}
+\varepsilon_{\rm init}
+\varepsilon_{\rm node}
+\varepsilon_{37\to42}
+\varepsilon_{\rm step}\\
&+\varepsilon_{\rm coll}
+\varepsilon_{\rm over}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm rec},
\end{aligned}
```

```math
\varepsilon_{\rm node}
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]
```

と分ける。$\varepsilon_{\rm prep}$ はM51のrank-one準備とseed無反応、$\varepsilon_{\rm init}$ は1回のM50/R164初期位置選択、$\varepsilon_{37\to42}$ はR86担体誤差から正則化M42生成子へのDuhamel誤差である。同じM37包絡差をR135診断、M42生成子、終位置記録へ重複加算しない。

固定 $\rho,\sigma>0$ では最大率が有限なので、時間窓数、方向別閾値分割、Hamiltonian平滑化、仕事register範囲、有限衝突cell数、clock精度を増やして $\varepsilon_{\rm step}$、$\varepsilon_{\rm coll}$、$\varepsilon_{\rm over}$、$\varepsilon_{\rm clk}$ を任意に小さくできる。ただし $\rho,\sigma\downarrow0$ では最大率、必要cell数、閾値・clock精度、仕事register範囲が発散し得る。1つの固定装置で厳密nodeを追跡するとは主張しない。

R124の理想増分を $\alpha$、R125の理想分布距離を $\Delta$ とする。比較する各M42運転の誤差が $\varepsilon_{174}$ 以下なら、観測差はそれぞれ $\alpha-2\varepsilon_{174}$、$\Delta-2\varepsilon_{174}$ 以上である。有限パラメータで正にできるが、M51準備、M37伝播、初期作用殻、M42衝突bath、clock、終位置記録の単一Hamiltonian統合が未完了なので、Q3-4とQ3-5は条件付き達成を維持する。

## 6.15 数値検算

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

M42/R172--R174については `tools/verify_m42_spatial_token.py` を用いる。局所連続方程式、最小率の等変性、期待跳躍率、節正則化、全変動上界、M37担体誤差のDuhamel受渡し、1回の初期作用殻選択、無反応質量、局所履歴を検算する。R135とR168は `tools/verify_common_signal_m50.py` の固定時刻統計診断として残す。数値検算は解析証明の代わりではなく、単一試行状態と集団統計、初期選択と終記録、同じ誤差の二重計数を監査する回帰検査である。

## 6.16 Q3-1の達成判定と限界

本稿の固定されたQ3-1達成基準は、局所位置結合振動子網から空間格子上の Schrödinger 型時間発展を、近似範囲と誤差を伴って導くことである。本章のM37部分は次を与えた。

1. 有限個の実古典振動子からなる局所位置結合 Hamiltonian 。
2. 反回転項を含む局所包絡の厳密方程式。
3. 厳密正常モード包絡と生成子 $h_{\rm ex}$。
4. 目標実対称 $h_L$ との係数対応。
5. 弱結合・弱離調・有限時間の作用素誤差と状態誤差。
6. 再現可能な数値検算。

従って、Q3-1はこの限定された有限実対称モデルについて達成と判定する。これは量子力学の必然的創発を示す結果ではなく、局所古典振動子網における制御された Schrödinger 型有効力学である。

Q3-1の固定基準自体はR86で満たされ、今回の改訂で後から基準を広げたわけではない。R171はM37初期集団に使える共通開放準備、R112は共通有限正準信号代数、R135はM37標本集団の共分散持上げ、R172はM42の理想等変輸送、R173は節正則化と有限衝突Hamiltonian近似、R174は準備から終位置記録までの誤差受渡しを追加する強化結果である。M51--M37--M42受渡しをQ3-1達成の根拠へ遡及的に加えない。

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

のような低速条件、または明示的な非共鳴条件が別に必要である。M47のQ1-1は、M37が供給する時間非依存W型生成子の最低2モードへ傾斜制御を追加する。R86は時間非依存結合の包絡近似なので、時間依存傾斜のミクロ実装を自動的には証明しない。第3章と付録Bでは、全W型制御をスペクトル間隔と切替時間の誤差として別に評価する。時間依存M37を同じハードウェアへ厳密統合する課題は第8章に残す。

次はQ3-1の固定達成基準を超える一般化であり、本章の結論に含めない。

1. $\mathcal J_0$ と有効質量 $m$ の普遍的な値の導出。
2. 一般の複素 Hermitian 演算子と磁場結合。
3. 時間依存駆動に対する一様な非共鳴定理。
4. 非線形ミクロ結合に対する閉包。
5. 一般連続極限と境界条件の一様誤差。
6. 格子細分化で得る連続空間の粒子軌道、位相量子化、多粒子位置。
7. 最小率がM37のミクロHamiltonianだけから一意に選ばれること。
8. 粒子位置の慣性質量、電荷、担体エネルギーとの同定。
9. 固定性能の同じ装置による正則化誤差零極限。
10. 1次元井戸型・調和型ポテンシャルの低位束縛スペクトルと、エネルギー保存型の有限時間デコヒーレンス。
11. M51、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所Hamiltonianへ統合すること。
12. 源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを扱う、固定目標より強い装置模型。

M47ではM37を、対称W型生成子 $h_W$、最低2モード $\phi_0,\phi_1$、モード分裂 $E_1-E_0$ を供給する層としてだけ使う。M42をQ1へ流用せず、M47の粒子位置はM50/R170の固定時刻instrumentに従う。M37のHamiltonianと反回転項の評価は変更しない。外部 $\lambda_{\rm prep}(t)$ による開放準備と閉鎖作用角伝播、matching受渡しの条件は第8章と付録Hに示す。

Q3の二乗統計はM51が準備するrank-one集団と、R164による1回の初期位置選択に由来する。M42は同じ粒子を輸送し、終時刻には再標本化せず記録する。状態数だけで初期選択の全ミクロ過程を説明したとはせず、有限衝突bathだけでM51準備や作用容量の起源を説明したとも扱わない。
