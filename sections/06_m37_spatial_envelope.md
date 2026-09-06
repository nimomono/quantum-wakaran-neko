@number: 6
@chapter: 本文
@title: M37空間担体、W型低2モードbridgeとM54 spatial-moving実装
@status: M37の正確局所方程式とR86を保ち、Q3 spatial signal sectorに加えて、R187で弱結合W型最低2モードをM54 W2 static profileのQ1制御担体へ有限誤差で接続する。測定・準備・M0統合は別課題とする。

## 6.1 Q3のM54 spatial profileとM37の範囲

Q3の親模型は第2章のM54 spatial-moving profileである。その1試行には、実正準signal自由度、その派生表示 $Z$、1個の粒子位置 $X_t$、finite collision bath、clock、履歴が含まれる。複素rayと位置分布は試行集団の統計であり、$C_Z$ またはそのrank-one因子を単一試行controllerへ書き戻さない。

M37はM54と並ぶ別の粒子親模型ではない。Q3ではM54 spatial signal sectorを局所位置ばねだけで有限時間近似する担体実現模型であり、Q1ではR187の弱結合W型族に限って最低2正常modeをM54 W2 static profileの物理signal subsystemとして使う。役割を次のように分ける。

| 対象 | 単一試行で物理的に存在するもの | 派生表示・集団記述 | 役割 |
|---|---|---|---|
| M54 spatial profile | 実正準signal、粒子位置 $X_t$、finite collision、clock、履歴 | $Z$、$C_Z$、rank-one ray、位置分布 | R161 moving matching、R185時間反転・Newton則 |
| M37実装 | 有限個の実振動子座標 $(q_i,p_i)$ と局所ばね結合 | 局所複素包絡 $b_i$、零傾斜正常mode座標 | R86によるM54 spatial signal sectorの有限時間近似、R184の受渡し。R187条件下ではQ1 W2 control carrierも実装 |

共通M54/R181Aでrank-one signal集団を準備する場合、安全な切断面から同じ試行のsignalをM54 spatial profileへ渡す。開始面ではR164とR161 static/R162 thermalを一度だけ用いて $X_0$ の条件付き分布を準備する。その後は再標本化せずR161 moving specializationが同じ粒子を輸送し、終時刻にはR112が既存の $X_T$ を記録する。

Q3-1の固定達成基準はM37から有効空間包絡への縮約であり、R86が満たす。M54 spatial profileの粒子位置とmoving matchingはQ3-2、Q3-4A、Q3-4B、Q3-5の下流構造であって、Q3-1へ遡及的に要求しない。M54のportとspatial profile、M37局所ばね網、作用殻、finite collision bath、記録器を単一の有限局所装置へ統合したとは扱わない。

Q1はQ1 W型2モードprotocol、Q2はM54の永続registerとreceiver、固定時刻の一般枝instrumentはM54 static/R170を使う。Q3の空間configurationはM54 spatial profileを使う。R187はM37の弱結合W型正常modeをQ1のcontrol carrierへ接続するが、M54 spatial profileの全時刻位置matchingをQ1へ流用しない。Q1の排他的粒子位置結果は引き続きR164/R161/R162/R170で作る。

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

本節の式は、派生複素包絡の作用比を任意有限基底で比較する診断であり、それだけでは単一試行の粒子を作らない。Q3では準備終了面で1回だけ初期M54 spatial profile位置を作り、空間セル基底の局所辺流に沿って同じ粒子を輸送する。任意の基底 $W$ で終時刻に新しい粒子位置を作るR170と、M54 spatial profileの連続位置過程を同じ運転へ重ねない。Q1のW型2モード測定は第3章で独立に扱う。

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。これは空間セル基底の目標位置分布である。R161 moving specializationは同じ条件付き分布をM54 spatial profileの実在粒子について全有限時刻へ運び、R184はM37とfinite collision実装の誤差を与える。R86の作用比だけを粒子実体と同一視せず、M54 spatial profileの位置更新則と初期matchingを必要とする。

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

と定める。$C_Z$ は正半定値、trace 1である。これは集団記述であり、単一試行で装置が読む変数ではない。各試行のM37包絡 $Z_t(\omega)$ は、準備終了面では初期M54 spatial profile位置選択へ、輸送中はM54 spatial profileの局所rate controllerへ渡す派生物理信号である。

本稿では $C_Z$ を「非中心化自己共分散」、すなわち規格化した第2モーメントとして使う。通常の中心化共分散を意味せず、$\mathbb E[Z_t]=0$ の場合にだけ中心化した量と比例して一致する。R168の支持結論はこの非中心化定義に対する主張であり、中心化共分散の階数1条件だけからは従わない。

初期集団をM54で準備する場合、設定前seed測度を $\mu_{\rm seed}$、準備切断面を $t_{\rm cut}$ とし、

```math
\mu_{\rm cut}^{c}
=
(\Phi_c^{t_{\rm cut}})_\#\mu_{\rm seed}
```

をM37初期面へ渡す。R181Aの安全事象外は無反応として残し、安全集団の第2モーメントだけが $cc^\dagger$ へ有限誤差で近づく。M37の初期分布へ $C_Z(0)=cc^\dagger$ を直接仮定する経路と、M54の押出し測度から得る経路を同じ準備状態と呼ばない。

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

## 6.12 M54 spatial profile moving matchingとR161 moving specialization

Q3の粒子位置はM54 spatial profileという独立二層模型へ置かず、第2章のM54 spatial profile共同測度模型で扱う。各試行にはM37または理想M54 spatial profile signalから得る単一試行の $Z_t(\omega)$ と、1個の粒子位置 $X_t$ が存在する。集団量 $C_Z$ またはそのrank-one因子 $\psi$ を位置controllerへ入力しない。

R164と同じ条件付き容量

```math
R_i^\delta(Z)
=
|Z_i|^2+\delta q_iZ^\dagger Z
```

から

```math
\pi_i^\delta(Z)
=
\frac{|Z_i|^2/(Z^\dagger Z)+\delta q_i}{1+\delta}
```

を定める。R161 moving specializationは局所辺流 $J_{i\to j}$ と対称traffic

```math
T_{ij}^\delta
=
\frac{|h_{ij}|}{\mathcal J_0}
(R_i^\delta+R_j^\delta)
```

から

```math
k^+_{i\to j}
=
\frac{T_{ij}^\delta+J_{i\to j}}{2R_i^\delta}
```

を作る。$T_{ij}^\delta\geq|J_{i\to j}|$ と $R_i^\delta\geq\delta q_iZ^\dagger Z$ によりnodeでも有限かつ非負である。初期共同測度が $\mu_0(X=i\mid Z=z)=\pi_i^\delta(z)$ を満たせば、同じ条件付き分布を全時刻で保存する。rank-one集団ではR135から $Z=\alpha\psi$ がほとんど確実に成り立ち、

```math
P(X_t=i)
=
\frac{|\psi_i(t)|^2+\delta q_i}{1+\delta}
```

となる。完全証明は付録Nに置く。

固定時刻に任意基底を読むR170とM54 spatial profileの連続位置過程を同じ終端標本器として重ねない。R170はQ1・Q2のinstrumentとQ3の代替固定時刻診断に残り、Q3-4A・Q3-4B・Q3-5では準備面で得た同じ $X_t$ をR161/R184で運ぶ。

## 6.13 M54 spatial profile--M37の開始面と終位置記録

M54/R181Aでrank-one signal集団を準備する場合、安全な切断面から同じ試行のsignalをM54 spatial profileへ渡す。開始面ではR164の作用殻状態数とR161/R162の有限再平衡化を1回だけ使い、

```math
P(X_{t_0}=i\mid Z_{t_0}=z)
\simeq
\pi_i^\delta(z)
```

を準備する。その後はR164による再抽選を行わず、R161 moving specializationのmoving matchingで同じ粒子を輸送する。

理想M54 spatial profile signal sectorでは $i\mathcal J_0\dot Z=h_LZ$ を実正準Hamiltonianとして厳密に持つ。局所位置ばね実装を要求するときだけM37へ置き換え、R86とR184の有限時間誤差を加える。終時刻には新しいstatic-profile位置を生成せず、R112の局所記録剪断が既存の $X_T$ を記録する。従ってM54準備、初期R164 matching、moving matching、終位置記録を独立な複数のBorn型確率源として数えない。

## 6.14 R184のM37・有限collision受渡しとQ3-4A・Q3-5

M37の実局所包絡を $b(t)$、同じ初期値から進む理想M54 spatial profile信号を $b_L(t)$ とする。開始面で $S_{\rm ref}=\|b(0)\|^2$ を単一試行registerへlatchする。M37実装では背景容量を

```math
R_{i,37}^{\delta,\mathrm{lat}}(t)
=
|b_i(t)|^2+\delta q_iS_{\rm ref}
```

と固定し、輸送中の非保存局所作用 $\|b(t)\|^2$ を背景項へ書き戻さない。理想 $b_L$ は $\|b_L(t)\|^2=S_{\rm ref}$ を保存するため、このlatch規約は理想M54 spatial profileの $R_i^\delta$ と一致する。$\Delta=\delta_{\rm loc}(\eta)<1$、$q_{\min}=\min_iq_i$、$h_1=\max_i\sum_{j\ne i}|h_{ij}|$ とすると、R184は

```math
\max_i
\sum_{j\ne i}
\left|
k_{i\to j}^{37,\mathrm{lat}}
-
k_{i\to j}^{L}
\right|
\leq
L_\delta(\eta)
\varepsilon_{\rm car}(T)
```

を与える。ここで

```math
L_\delta(\eta)
=
\frac{h_1}
{\mathcal J_0(1-\Delta)^2}
\left[
\frac{
\sqrt2(1+\sqrt{1+\Delta^2})
}{
\delta q_{\min}
}
+
\frac{
2(1+\delta)
}{
\delta^2q_{\min}^2
}
\right].
```

従って

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
P(X_t^{37,\mathrm{lat}}\in\cdot),
P(X_t^L\in\cdot)
\right)
\leq
T L_\delta(\eta)\varepsilon_{\rm car}(T).
```

$\delta>0$ ではrateは固定有限グラフ上で有界なので、共通R162のgeneric finite collision構成（付録K.4）により、有限threshold cell、clock、work register、historyを持つ有限駆動Hamiltonian散乱列へ任意精度で近似できる。旧R173または旧 $(\rho,\sigma)$ node正則化を現行証拠鎖へ戻さず、R164と共通の $\delta$ と開始作用latchだけを使う。

Q3-4AとQ3-5ではR124/R125の理想分布差をR184の完全結果誤差 $\varepsilon_{184}$ と比較する。Q3-4BではR182の同じ静的W型過程を三時刻で読み、同じM54 spatial profile粒子の半周期移送と一周期回帰へ持ち上げる。M54準備、M37実装、初期作用殻、finite collision bath、clock、終位置記録の単一装置統合は引き続き条件として残す。

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

M54 spatial/R161--R185については `tools/verify_m54_spatial_matching.py` を用いる。current反対称性、対称trafficの正値性、moving-matching master方程式、同一母測度の時間反転、有限格子の $D_\pm$ 分解、R184の開始作用latchとrate感度上界、R185の $O(\delta)$ 正則化残差を検算する。R185については零current例だけでなく非零current速度を持つ滑らかな周期例でも残差恒等式を検査する。R135とR168は `tools/verify_m54_static_instrument.py` の固定時刻統計診断として残す。数値検算は解析証明の代わりではなく、単一試行状態と集団統計、初期matchingと終記録、同じ誤差の二重計数を監査する回帰検査である。

## 6.16 Q3-1の達成判定と限界

本稿の固定されたQ3-1達成基準は、局所位置結合振動子網から空間格子上の Schrödinger 型時間発展を、近似範囲と誤差を伴って導くことである。本章のM37部分は次を与えた。

1. 有限個の実古典振動子からなる局所位置結合 Hamiltonian 。
2. 反回転項を含む局所包絡の厳密方程式。
3. 厳密正常モード包絡と生成子 $h_{\rm ex}$。
4. 目標実対称 $h_L$ との係数対応。
5. 弱結合・弱離調・有限時間の作用素誤差と状態誤差。
6. 再現可能な数値検算。

従って、Q3-1はこの限定された有限実対称モデルについて達成と判定する。これは量子力学の必然的創発を示す結果ではなく、局所古典振動子網における制御された Schrödinger 型有効力学である。

Q3-1の固定基準自体はR86で満たされ、今回の改訂で後から基準を広げたわけではない。R181AはM37初期集団に使える共通開放準備、R112は共通有限正準信号代数、R135はM37標本集団の共分散持上げ、R161 moving specializationはM54 spatial profileのmoving matching、R184はM37局所包絡とfinite collision実装への誤差受渡し、R185は同一母測度の時間反転と時間対称Newton則を追加する強化結果である。M54--M54 spatial profile--M37受渡しをQ3-1達成の根拠へ遡及的に加えない。

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

のような低速条件、または明示的な非共鳴条件が別に必要である。R86は一般の時間依存結合を自動的には証明しない。この一般的限界は維持する。一方、Q1 W型2モードprotocolについてはR187が別経路を使い、弱結合W型の有限個のpiecewise-static傾斜区間を各static正常mode分裂で較正し、必要なswitchだけを短いsmooth ramp比較として扱う。従って「任意の時間依存M37」は未解決のままだが、R187で指定した有限Q1 control familyは例外として物理bridgeが閉じる。

次はQ3-1の固定達成基準を超える一般化であり、本章の結論に含めない。

1. $\mathcal J_0$ と有効質量 $m$ の普遍的な値の導出。
2. 一般の複素 Hermitian 演算子と磁場結合。
3. 時間依存駆動に対する一様な非共鳴定理。
4. 非線形ミクロ結合に対する閉包。
5. 一般連続極限と境界条件の一様誤差。
6. 格子細分化で得る連続空間の粒子軌道、位相量子化、多粒子位置。
7. R161 moving specializationの対称往復trafficがM37の局所ばねHamiltonianだけから一意に選ばれること。
8. 粒子位置の慣性質量、電荷、担体エネルギーとの同定。
9. 固定性能の同じ装置による正則化誤差零極限。
10. 1次元井戸型・調和型ポテンシャルの低位束縛スペクトルと、エネルギー保存型の有限時間デコヒーレンス。
11. M54、M37、初期作用殻、M54 spatial profile衝突bath、clock、記録を同じ有限局所Hamiltonianへ統合すること。
12. 源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを扱う、固定目標より強い装置模型。

Q1 W型2モードprotocolの静的起源はM37の対称W型生成子と最低2モードにある。第6.17節と第3.5.1節の一般誤差道具に加え、第6.19節R187が弱結合W型carrierの任意精度有限制御を閉じる。M54 spatial profileをQ1へ流用せず、Q1 W型2モードprotocolの粒子位置はM54 static/R170の固定時刻instrumentに従う。M37のHamiltonianと反回転項の評価は変更しない。外部 $\lambda_{\rm prep}(t)$ による開放準備、作用殻、matching、記録の単一装置統合条件は第8章と付録Hに残す。

Q3の二乗統計はM54が準備するrank-one集団と、R164による1回の初期位置選択に由来する。M54 spatial profileは同じ粒子を輸送し、終時刻には再標本化せず記録する。状態数だけで初期選択の全ミクロ過程を説明したとはせず、有限衝突bathだけでM54準備や作用容量の起源を説明したとも扱わない。

## 6.17 W型制御への有限時間拡張

物理的主線では同じ実振動子へ傾斜を加え、その包絡からQ1制御を得る。有限格子上で $h_W(t)=h_W(0)-F(t)x$ とし、第6.6節の対応を

```math
A(t)=\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}h_W(t),\qquad
H(t)=\frac{\omega_0}{2}(P^{\mathsf T}P+Q^{\mathsf T}Q)
+\frac1{\mathcal J_0}Q^{\mathsf T}h_W(t)Q
```

へ拡張する。Fは有限時間の外部制御であり、自律時計や閉鎖仕事源を仮定しない。制御域で全剛性を正定値に保ち、位置ばねの非負重みと局所離調の対応を維持する。厳密に

```math
i\mathcal J_0\dot b=h_W(t)b+e^{2i\omega_0t}h_W(t)\overline b,
\qquad
\frac{dH}{dt}=\frac{\partial H}{\partial t}
=\frac1{\mathcal J_0}Q^{\mathsf T}\dot h_WQ
```

である。瞬時切替ではQ,Pは連続で、仕事は $Q^{\mathsf T}\Delta h_WQ/\mathcal J_0$。時刻ごとの正定値性だけでは駆動による増幅を防げない。

区分一定の区間rで生成子を $h_r$、長さを $\Delta t_r$、$\eta_r=2\|h_r\|/(\mathcal J_0\omega_0)<1$ とする。R86の係数を使い

```math
a_r=(1-\eta_r)^{-1/4}\varepsilon_{{\rm car},r}(\Delta t_r),
\qquad E_N=\prod_{r=1}^N(1+a_r)-1
```

と置く。付録E.12の合成評価により、同じ初期値の有効区分一定解との差は $E_N\|b(0)\|$ 以下である。区間内の時刻にも、その区間の経過時間で同じ式を適用する。区間ごとの再準備は使わない。滑らかな切替と区分一定列との差は付録E.13の実線形伝播差で評価し、静的R86に時間依存行列を代入しただけの主張にはしない。

この係数は保守的な上界である。Jが小さいとRabi時間が伸びるため、$J/G$、$\eta_r$、全時間、区間数、切替時間、状態残差を同時に監査する。低mode内に制限した周波数差の評価が全スペクトルノルムより鋭い場合もある。全操作の任意精度構成と資源上界は未完であり、静的Q3-1の達成範囲は変えない。

### 6.17.1 三段階の有限例照合

`tools/verify_m37_w_q1_bridge.py` は25点のW型格子で、同じ初期状態から実正準運動、全W型包絡、射影2モード運動を比較する。採用例は $J=0.02098$、$G=1.21391$、全時間122.513であり、3区間を再準備なしで接続する。搬送周波数を2000、20000、200000と増やすと、採用時刻での最大包絡誤差は0.02571、0.002585、0.0002584へ減る。一方、実運動と2モード運動の差は0.05221、0.04089、0.04030であり、搬送周波数だけでは消えない。これは包絡誤差と射影残差を分ける必要性を示す有限例であり、全パラメータ域の証明ではない。共通位相依存、rank-oneからのずれ、作用変動、滑らかな切替の仕事も別々に検算する。数値上界と再現条件は `VALIDATION.md` に記録する。

## 6.18 静的W型スペクトルと空間トンネルへのR182接続

時間に依存しないW型生成子 $h_W$ では、R86の厳密正常モード生成子は

```math
h_{\rm ex}
=
f_{\omega_0}(h_W),
\qquad
f_{\omega_0}(E)
=
\mathcal J_0\omega_0
\left[
\sqrt{
1+\frac{2E}{\mathcal J_0\omega_0}
}
-1
\right].
```

従って $h_{\rm ex}$ と $h_W$ は固有ベクトルを厳密に共有する。最低偶奇固有値の差を $\Delta=E_1-E_0$、厳密M37正常モードでの差を

```math
\Delta_{\rm ex}
=
f_{\omega_0}(E_1)-f_{\omega_0}(E_0)
```

とする。$\eta=2\|h_W\|/(\mathcal J_0\omega_0)<1$ なら平均値の定理から

```math
(1+\eta)^{-1/2}
\leq
\frac{\Delta_{\rm ex}}{\Delta}
\leq
(1-\eta)^{-1/2}.
```

同じ評価は $E_2-E_1$ にも成り立つ。この静的場合は、固有空間そのものの誤差を時間積分する必要がなく、厳密正常モードの半周期と一周期を $\Delta_{\rm ex}$ で較正すれば鏡映と回帰はその時刻で厳密である。局所包絡 $b$ と厳密正常モード包絡の差だけがR86の $\delta_{\rm loc}(\eta)$ で残る。

この評価は第6.17節の時間依存傾斜制御を置き換えない。Q1の有限傾斜列では一般の区間合成誤差と高モード残差を監査し、Q3-4Bの静的零傾斜W型ではR182の共有固有空間と分裂相対誤差を使う。これにより、トンネル分裂が小さく周期が長いことだけを理由に一般Duhamel上界を一周期へ機械的に適用しない。

## 6.19 R187：M37弱結合W型からQ1 W2制御への物理bridge

第3章3.5.1の残差系は、与えられた全W型制御列から2モード解への誤差を接続する一般道具である。しかし固定した零傾斜低2モード埋込みに傾斜項を作用させると、残差ノルムは $O(|F|)$、傾斜hold時間は $O(|F|^{-1})$ になり得るため、粗い積分上界だけでは任意精度族の存在を示せない。本節では、零傾斜で低2モードが孤立する明示的な局所W型族を作り、傾斜時のdressed低2モードを使ってこの障害を避ける。

### 6.19.1 弱結合W型族

固定した有限左半井戸の実対称局所生成子を $h_{\rm H}$ とする。最低固有値 $e_*$ は単純、次の固有値とのgapを $g_*>0$ とし、規格化ground mode $u_*$ の中央端点成分を $a_*\neq0$ とする。右半井戸は鏡映コピーとする。中央端点を結ぶ1本の局所ばねだけを強度 $\kappa\geq0$ で開き、

```math
h_\kappa
=
h_{\rm H}^{L}\oplus h_{\rm H}^{R}
+
\kappa
\left|e_L-e_R\right\rangle
\left\langle e_L-e_R\right|.
```

$\kappa=0$ では左右ground modeが2重縮退する。$\kappa>0$ の最低偶奇固有値を $E_0(\kappa)<E_1(\kappa)$、第3固有値を $E_2(\kappa)$ とし、

```math
J_\kappa
=
\frac{E_1-E_0}{2},
\qquad
G_\kappa
=
E_2-E_1,
\qquad
r_\kappa=\frac{J_\kappa}{G_\kappa}
```

と置く。付録E.14により

```math
J_\kappa
=
a_*^2\kappa+O(\kappa^2),
\qquad
G_\kappa
=
g_*+O(\kappa),
\qquad
r_\kappa\longrightarrow0.
```

零傾斜の最低偶奇modeを $\phi_{0,\kappa},\phi_{1,\kappa}$ とし、左右局在基底を第3章と同じ規約で作る。鏡映に対して奇な有限位置作用素 $X$ を固定し、半井戸ground modeの位置平均が零でないとする。このとき

```math
\zeta_\kappa
=
\left|
\langle\phi_{0,\kappa}|X|\phi_{1,\kappa}\rangle
\right|
\longrightarrow
\zeta_*>0.
```

従って低2モードの分裂を小さくしても、傾斜に対する左右lever armは消えない。

### 6.19.2 傾斜時のdressed低2モード

局所傾斜を

```math
h_\kappa(F)=h_\kappa-FX
```

とする。零傾斜低2モード射影を $P_\kappa$、$h_\kappa(F)$ の最低2状態cluster射影を $P_\kappa(F)$ とする。$|F|\|X\|/G_\kappa$ が十分小さいとき、有限次元spectral perturbationにより定数 $C_W$ を $\kappa$ に一様に選べて

```math
\|P_\kappa(F)-P_\kappa\|
\leq
C_W\frac{|F|\|X\|}{G_\kappa}.
```

さらに $P_\kappa(F)$ を $P_\kappa$ へ戻すnear-identity unitaryを選ぶと、共通エネルギーを除いたdressed 2モード生成子は

```math
g_{\kappa}^{\rm dr}(F)
=
-J_\kappa\sigma_x
+
F\zeta_\kappa\sigma_z
+
R_{\kappa}^{\rm dr}(F),
```

```math
\|R_{\kappa}^{\rm dr}(F)\|
\leq
C_W
\frac{F^2\|X\|^2}{G_\kappa}.
```

第3章の2モード傾斜は $\varepsilon=2F\zeta_\kappa$ なので、

```math
F_\kappa
=
\frac{\sqrt{J_\kappa G_\kappa}}{2\zeta_\kappa}
```

と選べば

```math
\frac{J_\kappa}{|\varepsilon_\kappa|},
\quad
\frac{|\varepsilon_\kappa|}{G_\kappa},
\quad
\frac{|F_\kappa|\|X\|}{G_\kappa}
=
O\!\left(\sqrt{r_\kappa}\right).
```

傾斜hold時間は $O(\mathcal J_0/\sqrt{J_\kappa G_\kappa})$ なので、dressed生成子の二次補正によるprojective角誤差も $O(\sqrt{r_\kappa})$ である。突然の有限傾斜切替では実ミクロ座標 $Q,P$ は連続で、切替前後の低2cluster不一致も $O(\sqrt{r_\kappa})$ に抑えられる。

### 6.19.3 静的M37正常modeによる長時間較正

各piecewise-constant区間ではM37の厳密正常mode生成子は

```math
h_{\rm ex}(F)
=
f_{\omega_0}\!\left(h_\kappa(F)\right),
\qquad
f_{\omega_0}(E)
=
\mathcal J_0\omega_0
\left[
\sqrt{1+\frac{2E}{\mathcal J_0\omega_0}}-1
\right].
```

従って $h_{\rm ex}(F)$ と $h_\kappa(F)$ は各静的区間で固有ベクトルを厳密に共有する。低2固有値を $\lambda_0(F)<\lambda_1(F)$ とし、

```math
\Delta_{\rm ex}(F)
=
f_{\omega_0}(\lambda_1(F))
-
f_{\omega_0}(\lambda_0(F))
```

と置く。R140で指定した同じ回転角を実M37区間で作るときは、名目時間を機械的に流用せず $\Delta_{\rm ex}(F)$ でhold時間を較正する。これにより、長い零傾斜Rabi区間でも $\|h_{\rm ex}-h\|T$ という粗いDuhamel誤差を使わず、低2cluster内のprojective回転角を一致させられる。

局所回転包絡 $b$ とこの厳密正常mode伝播との差は、$\delta_{\rm loc}(\eta)<1$ に対して付録E.15の一様な静的segment上界

```math
\varepsilon_{\rm stat}(\eta)
=
\frac{2\delta_{\rm loc}(\eta)}{1-\delta_{\rm loc}(\eta)}
```

以下であり、hold時間に比例しない。固定有限個 $m$ の区間では

```math
\varepsilon_{\rm car}^{(m)}
\leq
\left(1+\varepsilon_{\rm stat}(\eta)\right)^m-1.
```

### 6.19.4 R187物理bridge定理

<!-- theorem-start:theorem -->
**定理（R187：M37弱結合W型からQ1 W2制御への有限誤差物理bridge）**

上の有限弱結合W型族を取り、$\zeta_*>0$ とする。任意に固定した目標 $U\in SU(2)$ と誤差 $\epsilon>0$ に対し、十分小さい $\kappa>0$、十分大きい有限搬送周波数 $\omega_0$、有限個の傾斜値 $F\in\{0,\pm F_\kappa\}$ とpiecewise-constant hold列を選べる。各区間の時間はM37厳密正常modeの低2分裂 $\Delta_{\rm ex}(F)$ で較正する。

零傾斜最低2正常modeを全M37正準状態の中の2正準対として保持し、高modeを捨てない。初期の低2mode投入誤差を $d_0$、有限switchを滑らかに近似する場合の伝播誤差を $\varepsilon_{\rm sw}$、傾斜・時間較正のprojective角誤差を $\varepsilon_{\rm cal}$ とする。このとき固定目標 $U$ に依存する有限定数 $C_U$、有限区間数 $m_U$ と、入力に依存しない全体位相 $\alpha_U$ が存在し、全入力 $c\in\mathbb C^2$、$\|c\|=1$ についてM37局所包絡の終状態は

```math
\left\|
b_{\rm out}
-
e^{i\alpha_U}V_\kappa Uc
\right\|
\leq
\varepsilon_{187},
```

```math
\varepsilon_{187}
\leq
d_0
+
C_U\sqrt{r_\kappa}
+
\left(1+\varepsilon_{\rm stat}(\eta)\right)^{m_U}-1
+
\varepsilon_{\rm sw}
+
\varepsilon_{\rm cal}.
```

ここで $V_\kappa$ は零傾斜の左右局在2モードを全mode空間へ埋め込む等長写像である。従って各固定 $U$ と $\epsilon$ に対して $\varepsilon_{187}<\epsilon$ を満たす有限M37装置を選べる。総hold時間は

```math
T_U
\leq
C_U
\frac{\mathcal J_0}{J_\kappa}
```

の形で増大し得る。これは任意精度の有限構成の存在を示すが、精度に対する多項式時間、一定bandwidth、一定dynamic rangeを主張しない。
<!-- theorem-end:theorem -->

証明は付録E.14--E.18。R140の2軸compilationは、$F_\kappa$ の回転軸が $r_\kappa\to0$ で $z$ 軸へ近づき、零傾斜軸が $x$ 軸のままなので、固定した $U$ に対して有限Euler wordを $\kappa$ に一様な近傍で選べることを使う。一般の時間依存HamiltonianをR86へ無断で代入せず、static segment、spectral dressing、有限switchを別々に評価する。

### 6.19.5 M54 W2 static profileへのcanonical handoff

零傾斜 $h_\kappa$ を実直交行列 $O_\kappa$ で正常mode対角化する。全modeについて

```math
Q'=O_\kappa^{\mathsf T}Q,
\qquad
P'=O_\kappa^{\mathsf T}P
```

は正準変換である。先頭2正常modeの $(Q'_0,P'_0,Q'_1,P'_1)$ をM54 W2 static profileの物理signal subsystemと同定する。高modeは全状態に残し、2mode射影を物理的な消去操作として使わない。

R181AのW2 source/template portまたはR112の固定canonical SWAPをこの2正準対へ接続する場合、その固定port誤差をR187の $d_0$ へ加える。portは設計時に固定したcollective couplingであり、単一試行の係数読出し、tomography、状態依存規格化を行わない。R187が閉じるのはM37 carrierからM54 W2 signalとR140制御への受渡しまでであり、R181A pump、R164作用殻、R161/R162 collision、R170/R143測定、記録、resetをM37の局所ばねHamiltonianだけから導出するものではない。

### 6.19.6 有限switchと資源境界

R187本体は有限個のstatic quenchで閉じる。各jumpは $Q,P$ を連続に保ち、有限仕事 $Q^{\mathsf T}\Delta h\,Q/\mathcal J_0$ を持つ。連続制御が必要なら、各jumpを幅 $\tau_{\rm sw}$ の $C^1$ rampへ置き換え、付録E.17でjump列との差を評価する。有限個のrampなので任意の $\varepsilon_{\rm sw}>0$ を有限幅で選べる。代表的に $H_\kappa=\sup_{|F|\leq F_\kappa}\|h_\kappa(F)\|$ が一様有界なら

```math
\tau_{\rm sw}
=
\frac{\mathcal J_0}{H_\kappa}r_\kappa^{1/4}
```

とすることで、ramp区間だけの比較誤差を $O(r_\kappa^{3/4})$ にできる。このsmooth化は高modeに対する断熱切替を仮定せず、小振幅quenchの連続近似である。

精度を上げると $J_\kappa=O(\kappa)$ のため総時間は $O(\kappa^{-1})$ に増え、switch時刻分解能、weak-link設定、分裂較正の要求も厳しくなる。搬送周波数は $\delta_{\rm loc}(\eta)$ を小さくするため増やすが、各static区間を $\Delta_{\rm ex}(F)$ で較正するため、R86の粗い $T\|h\|^2/\omega_0$ 上界を長いRabi時間へそのまま掛けない。これらの資源発散をQ2-4の多項式資源主張へ流用しない。
