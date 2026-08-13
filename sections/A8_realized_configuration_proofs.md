@number: A8
@chapter: 付録
@title: 有限配置グラフ上の実現配置過程
@status: R113--R118の局所流、最小跳躍率、Born型等変性、有界率no-go、節一様正則化、鋭い基準配置と任意初期場の準備、有限Hamiltonian実装、M37誤差伝播を証明する。Q1、Q2、Q3の共通理想過程、有限装置、Q3のミクロ複素振幅場を区別する。

## H.1 有限グラフの局所流

有限無向グラフを $G=(V,E)$、$|V|=L$ とし、Hermitian行列 $h$ はグラフ局所的、すなわち非対角成分について

```math
h_{ij}=0
\qquad
\left(
\{i,j\}\notin E
\right)
```

を満たすとする。理想複素振幅場を

```math
i\mathcal J_0\dot b
=
hb,
\qquad
b^\dagger b=1
```

で定め、頂点重みと有向辺流を

```math
p_i
=
|b_i|^2,
```

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
b_j^*h_{ji}b_i
\right)
```

とする。$J_{i\to j}$ の次元は時間の逆数である。

<!-- theorem-start:lemma -->
**補題（グラフ局所連続方程式）**
有向辺流は

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

を満たす。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明**
Hermitian性から反対称性が従う。また、

```math
\begin{aligned}
\dot p_i
&=
2\operatorname{Re}
\left(
b_i^*\dot b_i
\right)\\
&=
\frac{2}{\mathcal J_0}
\sum_j
\operatorname{Im}
\left(
b_i^*h_{ij}b_j
\right)\\
&=
\sum_jJ_{j\to i}
\end{aligned}
```

である。グラフ局所性により非隣接項は零になる。
<!-- theorem-end:proof -->

M37の局所包絡 $b_{\rm mic}$ は反回転項を含むため、この式を厳密なM37局所作用流として使わない。共通モデルが厳密な流として使うのは理想複素振幅場 $b_L$ の $J_{i\to j}$ である。$b_{\rm mic}$ から同じ式で計算する量は、目標流の局所推定値としてH.10節で誤差評価する。

## H.2 最小跳躍率、等変性、非爆発性

$p_i(t)>0$ のとき、最小跳躍率を

```math
\lambda_{i\to j}(t)
=
\frac{
[J_{i\to j}(t)]_+
}{
p_i(t)
},
\qquad
[z]_+
=
\max\{z,0\}
```

とする。$p_i=0$ では $J_{i\to j}=0$ であり、その頂点は等変分布の下で占有されない。従って率の値は到達不能状態上で任意に定めてよい。

<!-- theorem-start:theorem -->
**定理（最小跳躍過程のBorn型等変性）**
初期実現配置分布が

```math
P(X_0=i)
=
p_i(0)
```

なら、最小跳躍率を持つ理想過程は全存在時間で

```math
P(X_t=i)
=
p_i(t)
=
|b_i(t)|^2
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
分布を $\pi_i$ とするとmaster方程式は

```math
\dot\pi_i
=
\sum_j
\left(
\pi_j\lambda_{j\to i}
-
\pi_i\lambda_{i\to j}
\right)
```

である。$\pi_i=p_i$ を代入すれば、

```math
\begin{aligned}
\dot\pi_i
&=
\sum_j
\left(
[J_{j\to i}]_+
-
[J_{i\to j}]_+
\right)\\
&=
\sum_jJ_{j\to i}
=
\dot p_i
\end{aligned}
```

となる。全ての正成分が零から離れる開区間では率が有限であり、有限状態の線形master方程式の一意性から結論が従う。節へ近づく区間については、後述の期待跳躍数上界が有限時間非爆発性を与え、既知の大域存在定理 [45] により節をまたいで過程を延長できる。その延長でも上の無条件辺流が連続方程式を満たすため、等変分布 $p(t)$ が保たれる。
<!-- theorem-end:proof -->

この定理は初期分布を生成しない。初期分布を $p(0)$ として準備する物理過程はH.6節に分ける。また、連続方程式だけでは率は一意でない。任意の対称な非負辺流を両方向へ加えても同じ一時刻分布を保てる。上式は、余分な対称往復流を加えず、標準流を実現する率の中で期待跳躍頻度を最小にする選択である [44]。共通モデルはこの最小性を理想則の定義として採用する。

最大重み付き次数を

```math
h_1
=
\sup_{0\leq t\leq T}
\max_i
\sum_{j:j\sim i}
|h_{ij}(t)|
```

とする。$2\sqrt{p_ip_j}\leq p_i+p_j$ から、等変分布下の期待総跳躍率は

```math
\begin{aligned}
\mathbb E
\left[
\Lambda_{X_t}(t)
\right]
&=
\sum_{\{i,j\}\in E}
|J_{i\to j}(t)|\\
&\leq
\frac{h_1}{\mathcal J_0}.
\end{aligned}
```

従って有限時間 $T$ の跳躍数 $N_T$ は

```math
\mathbb E[N_T]
\leq
\frac{h_1T}{\mathcal J_0}
```

を満たし、有限時間爆発の確率は零である。節で特異な率を持つBell型過程の大域存在は既知であり [45]、有限状態・有界 $h$ はその十分条件の特別な場合である。本稿の新規結果はこの確率過程自体でなく、M37複素振幅場と有限Hamiltonian装置への接続にある。

## H.3 一様有界率による厳密節追跡のno-go

<!-- theorem-start:theorem -->
**定理（一様有界率Markov過程の有限時間厳密節追跡no-go）**
連続時間Markov跳躍過程の各頂点からの全脱出率が

```math
\Lambda_i(t)
\leq
\Lambda_{\max}
<
\infty
```

で一様に抑えられるとする。ある $s$ で $q_i(s)>0$ なら、全ての有限 $t>s$ について

```math
q_i(t)
\geq
q_i(s)
e^{-\Lambda_{\max}(t-s)}
>
0
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
流入項は非負なので

```math
\dot q_i
\geq
-\Lambda_iq_i
\geq
-\Lambda_{\max}q_i
```

である。Grönwall不等式を適用すれば結論を得る。
<!-- theorem-end:proof -->

この定理が禁止するのは、一様有界な脱出率を持つ連続時間Markov跳躍過程が、正の頂点占有を有限時間で厳密零へ送ることである。一般の決定論的Hamiltonian流、離散Poincaré写像、有限時間輸送写像を禁止する結果ではない。有限装置には厳密節追跡でなく、節占有を任意に小さくすることを要求する。

## H.4 節一様の滑らかな正則化

$\rho>0$ は無次元の重み正則化、$\sigma>0$ は時間の逆数を持つ流正則化とする。正部分の滑らかな近似を

```math
r_\sigma(z)
=
\frac12
\left(
z+
\sqrt{z^2+\sigma^2}
\right)
```

とし、

```math
\lambda_{i\to j}^{\rho,\sigma}(b)
=
\frac{
r_\sigma(J_{i\to j}(b))
}{
p_i(b)+\rho
}
```

を正則化率とする。$\sigma$ と $\rho$ を同一視しない。1パラメータ化する場合は、固定率尺度 $\Omega_*$ を使って $\sigma=\Omega_*\rho$ とする。

```math
0
\leq
r_\sigma(z)-[z]_+
\leq
\frac{\sigma}{2}
```

である。最大次数を $d_*$ とすると、

```math
\Lambda_*^{\rho,\sigma}
\leq
\frac{h_1}{\mathcal J_0\sqrt\rho}
+
\frac{d_*\sigma}{2\rho}
```

が全状態空間で成立する。固定した正の $\rho,\sigma$ では率は滑らかかつ一様有界である。

理想の無条件辺流と、Born型分布を正則化率へ入れた辺流を

```math
F_{i\to j}
=
[J_{i\to j}]_+,
```

```math
F_{i\to j}^{\rho,\sigma}
=
\frac{p_i}{p_i+\rho}
r_\sigma(J_{i\to j})
```

とする。このとき

```math
\left|
F_{i\to j}^{\rho,\sigma}
-
F_{i\to j}
\right|
\leq
\frac{\sigma}{2}
+
\frac{|h_{ij}|}{\mathcal J_0}
\sqrt\rho
```

である。右辺は $p_i$ の正の下限を含まず、節でも有限である。

時間依存生成子については、辺重み和も考えている有限時間区間での上限として

```math
H_E
=
\sup_{0\leq t\leq T}
\sum_{\{i,j\}\in E}
|h_{ij}(t)|
```

とし、正則化過程の分布を $q^{\rho,\sigma}(t)$ とする。

<!-- theorem-start:theorem -->
**定理（節一様の正則化分布誤差）**
$q^{\rho,\sigma}(0)=p(0)$ なら、任意の有限 $T$ について

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
\right].
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
各無向辺の両向き流差を足すと、$p(t)$ を正則化master方程式へ代入した残差の全変動ノルムは

```math
C_{\rho,\sigma}
\leq
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}
\sqrt\rho
```

である。Markov発展の全変動縮小性とDuhamel公式から

```math
D_{\rm TV}
\left(
q^{\rho,\sigma}(t),p(t)
\right)
\leq
\int_0^tC_{\rho,\sigma}\,ds
```

を得る。
<!-- theorem-end:proof -->

有限 $\rho,\sigma$ では逆向きの小さな対称跳躍も生じる。この過程は最小跳躍過程そのものではなく、$\rho,\sigma\to0$ でそれへ近づく有限率近似である。

## H.5 理想過程との軌道結合

理想過程と正則化過程を、同じ状態にいる間は各辺について両率の小さい方の跳躍を共有するよう結合する。初めて異なる跳躍が起きる時刻を $\tau_{\rm diff}$ とすると、H.4節の辺流差から

```math
P
\left(
\tau_{\rm diff}\leq T
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

を得る。従って有限時間の軌道分布も正則化極限で理想軌道分布へ近づく。ただし有限正則化では、理想重みが零となる時刻に実現配置がその頂点へ残る確率を厳密零にはできない。

## H.6 鋭い基準配置と任意初期場の準備

鋭い基準配置 $z_0$ から

```math
b(0)=e_{z_0},
\qquad
X_0=z_0
```

と開始すれば、等変性の初期条件は確率分布を別に与えず満たされる。固定準備回路 $U_{\rm prep}$ の各時計窓で、場と実現配置へ同じグラフプログラムを作用させる。R113から準備終了時に

```math
P(X=z)
=
\left|
(U_{\rm prep})_{zz_0}
\right|^2
=
|b_z|^2
```

を得る。これがR118であり、Q1、Q2の固定準備で使う。

任意の初期場 $b_0$ を準備履歴なしに直接与える場合は、初期実現配置を $|b_{0,i}|^2$ に従って別に準備する必要がある。

等変性を使うには、初期実現配置を $p_i(0)$ に従って準備する必要がある。初期作用を

```math
I_i(0)
=
\mathcal J_0|b_i(0)|^2,
\qquad
\sum_iI_i(0)
=
\mathcal J_0
```

とする。1個の初期選択器角 $\vartheta_0\in[0,2\pi)$ から一様閾値

```math
u_0
=
\frac{\mathcal J_0\vartheta_0}{2\pi}
\in
[0,\mathcal J_0)
```

を作り、作用区間

```math
\left[
\sum_{k<i}I_k(0),
\sum_{k\leq i}I_k(0)
\right)
```

へ分割し、選ばれたセル $i$ へ実現配置を運ぶ。作用読出しの共役運動量を入口で零に置けば、理想剪断は複素振幅場を変えない。比較境界を無反応結果とし、選択履歴を外部セルへ残せば、M35と同じ有限Hamiltonian機構で初期分布を任意精度に準備できる。

この準備は一般には全セル作用を集める大域過程であり、その後の局所実現配置運動と区別する。初期準備誤差を $\varepsilon_{\rm init}$ とすると、後段の等変性はこの誤差を増幅せず、最終全変動距離へ加算する。

## H.7 有限時間離散化

正則化生成子を $Q^{\rho,\sigma}(t)$ とする。刻み $\Delta=T/K$ を

```math
\Delta
\Lambda_*^{\rho,\sigma}
\leq
1-\kappa,
\qquad
0<\kappa<1
```

となるよう選べば、

```math
P_n(i,j)
=
\Delta
\lambda_{i\to j}^{\rho,\sigma}(t_n)
```

と

```math
P_n(i,i)
=
1-
\Delta
\sum_j
\lambda_{i\to j}^{\rho,\sigma}(t_n)
```

は確率核を成す。固定した $\rho,\sigma>0$ では $Q^{\rho,\sigma}(t)$ とその時間微分が有限時間区間で有界である。従って時間非一様master方程式のEuler近似について有限な定数 $C_{\rm disc}(\rho,\sigma,h,T)$ が存在し、

```math
\max_{n\leq K}
D_{\rm TV}
\left(
q_n^\Delta,
q^{\rho,\sigma}(t_n)
\right)
\leq
C_{\rm disc}
T\Delta
```

となる。$C_{\rm disc}$ は $\rho\to0$ で一様である必要はない。正則化を先に固定し、その後で $\Delta$ を選ぶ。

## H.8 局所選択器と1辺内Hamiltonian輸送

現在セルを $i$ とする。局所作用、正則化枝作用、待機作用を

```math
I_i^\rho
=
\mathcal J_0
\left(
p_i+\rho
\right),
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
\sum_{j:j\sim i}
A_{i\to j}
```

とする。H.7節の刻み条件により全て非負で、総和は $I_i^\rho$ である。従って1個の局所選択器角から一様閾値 $u_i\in[0,I_i^\rho)$ を作り、これらの作用区間へ入れれば、除算器を使わず

```math
P(i\to j)
=
\frac{A_{i\to j}}{I_i^\rho}
=
\Delta
\lambda_{i\to j}^{\rho,\sigma}
```

を得る。$\mathcal J_0\rho$ は固定校正作用として現在セルの選択器へ供給する。この可変全作用の選択はM41、排他的な滑らか比較と無反応はM35の機構と同じである。

局所読出しは模式的に

```math
G_{\rm read}
=
P_p|b_i|^2
+
\sum_{j:j\sim i}
P_{J,j}
J_{i\to j}(b)
```

と書ける。入口で $P_p=P_{J,j}=0$ なら、読出し座標は変化するが複素振幅場への理想反作用は零である。比較幅、角切断、有限読出し窓に由来する誤差は無反応を含む1step核の全変動距離として数える。

実現配置は新たな波動モードでなく、1個の古典局在自由度 $Z$ とする。有限グラフを互いに交わらない頂点領域と、端点以外では交わらない細い辺チャネルとして3次元空間へ埋め込み、その近傍を実現配置の配置空間とする。粗視化位置を

```math
X(Z)
\in
|G|
```

と書く。実現配置の正準位相空間は、この配置空間上の余接束であり、1個の位置 $Z$ とその共役運動量 $P_Z$ だけを持つ。各有向辺チャネル上で入口から出口へ向く滑らかなベクトル場を $v_{ij}(Z)$ とし、選択ラッチ $c_{i\to j}$ による輸送生成子を

```math
G_{i\to j}^{X}
=
c_{i\to j}
P_Z\mathbin{\cdot}v_{ij}(Z)
```

とする。これはベクトル場 $v_{ij}$ の余接持上げであり、正準流を生成する。時計窓と $v_{ij}$ の積分を選び、入口Poincaré断面から出口断面までを有限時間で運ぶ。安全枝では1個のラッチだけが作動するため、実現配置を担う1個の局在正準位相点は1頂点領域または選択された1辺チャネル上にあり、非隣接セルへ移らず、複数辺へ分裂しない。これは有限幅チャネル内の連続軌道を与えるが、格子細分化で得る連続空間極限や、実現配置の慣性質量を複素振幅場の有効質量 $m$ と同定することまでは主張しない。

各時刻層と各頂点へ選択器、読出し、枝ラッチ、履歴セルを事前配置すれば、固定 $K$ の全写像は有限個の滑らかな局所Hamiltonian窓へ埋め込める。使用済み履歴セルには旧位置、選択辺、待機、比較無反応の別を残す。同じ終点へ来る異なる履歴を消さないため、全写像の1対1性が保たれる。完全局所な単純資源上界は

```math
O
\left(
K
\left(
L+|E|
\right)
\right)
```

であり、有限次数グラフでは $O(KL)$ である。より小さい $O(L+K)$ 上界には、移動式制御器または明示的な局所通信路が別に必要なので、本稿では主張しない。無期限運転では新規の選択器・履歴セルを流入させ、使用済みセルを流出させる弱開放系とする。

M37複素振幅場は読出し、比較、輸送窓の間も発展する。理想的に停止した複素振幅場を仮定せず、窓内変化、読出し時刻と輸送完了時刻のずれ、時計窓との非可換性を $\varepsilon_{\rm win}$ として評価する。

## H.9 局所位置検出

頂点検出断面上で1となり、他の頂点と辺チャネル上で支持が交わらない滑らかな関数を $d_i(Z)$ とする。各局所検出器の正準読出し座標を $(D_i,P_{D_i})$ とし、

```math
G_{\rm det}
=
\sum_i
d_i(Z)
P_{D_i}
```

を使う。理想空入口 $P_{D_i}=0$ では実現配置への反作用なしに、実現配置を含む1個の頂点検出器だけが作動する。検出誤差と外部記録誤差を $\varepsilon_{\rm det}$ とすれば、予定されたPoincaré断面で

```math
P(D_i=1)
=
P(X=i)
```

を任意精度で実装できる。

これは固定時刻の局所位置読出しであり、初回到達、吸収、時間積分流束を与えない。これらはより強い検出模型として別に構成する必要がある。Q3-4とQ3-5の改訂後の固定判定にはこの読出しで十分だが、障壁値未満状態の確率増分と、2経路コヒーレント分布・非干渉混合・相対位相変更の間の正の分布差はまだ導いていない。

## H.10 M37包絡誤差の伝播

固定した $\rho,\sigma>0$ について、正則化生成子を複素振幅の関数

```math
b
\longmapsto
Q^{\rho,\sigma}(b)
```

とみなす。分母が $|b_i|^2+\rho$ で下から抑えられ、$r_\sigma$ が滑らかなので、任意の有界球 $\|b\|\leq R$ 上に有限なLipschitz定数 $L_{\rho,\sigma,h,R}$ が存在する。

```math
\left\|
Q^{\rho,\sigma}(b)
-
Q^{\rho,\sigma}(c)
\right\|_{1\to1}
\leq
L_{\rho,\sigma,h,R}
\|b-c\|_2
```

とする。R86により

```math
\sup_{0\leq t\leq T}
\|b_{\rm mic}(t)-b_L(t)\|_2
\leq
\varepsilon_{\rm car}(T)
\|\widetilde b(0)\|_2
```

なら、2つの時間非一様Markov発展のDuhamel評価から

```math
D_{\rm TV}
\left(
q_{\rm mic}^{\rho,\sigma}(t),
q_L^{\rho,\sigma}(t)
\right)
\leq
tL_{\rho,\sigma,h,R}
\varepsilon_{\rm car}(T)
\|\widetilde b(0)\|_2
```

を得る。固定した正則化の後では節で発散しない。$L_{\rho,\sigma,h,R}$ は $\rho,\sigma\to0$ で増大し得るため、M37弱結合量は正則化パラメータを固定した後に選ぶ。

## H.11 有限時間Hamiltonian実現配置近似

<!-- theorem-start:theorem -->
**定理（節を含む有限時間Hamiltonian実現配置近似）**
有限局所グラフ $G$、有限時間上で区分的に $C^1$ な有界Hermitian生成子 $h(t)$、有限時間 $T$、規格化初期複素振幅場 $b_0$、任意の $\epsilon>0$ を固定する。複素振幅場成分の正の下限は仮定しない。

初期作用比準備、正の $\rho,\sigma$、有限刻み $\Delta=T/K$、有限幅比較器、局所辺輸送、時計窓、検出器、および有限個の選択器・履歴セルを選び、全更新断面 $t_n\leq T$ で

```math
D_{\rm TV}
\left(
\mathcal L(X_n),
\{|b_i(t_n)|^2\}_{i=1}^L
\right)
<
\epsilon
```

となる有限Hamiltonian構成を得られる。固定 $K$ では全自由度を初めから含む有限閉鎖系へ埋め込める。無期限運転には新規の選択器・履歴セル流を持つ弱開放系が必要である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
全誤差を

```math
\begin{aligned}
\varepsilon_{X}
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
\varepsilon_{\rm det}
\end{aligned}
```

と分ける。まずH.4節により有限の $\rho,\sigma$ を選び、

```math
\varepsilon_{\rm reg}
=
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}
\sqrt\rho
\right]
```

を任意に小さくする。次にH.7節で有限の $K$ を選び、$\varepsilon_{\rm disc}$ を小さくする。最後に比較幅、角切断、読出し、輸送、時計、検出の有限精度を選び、残りの項を小さくする。全ての項を例えば $\epsilon/7$ 未満へ選べば結論が従う。
<!-- theorem-end:proof -->

Q3でM37ミクロ複素振幅場を使う場合は、上の台帳へ

```math
\varepsilon_{\rm car\to X}
\leq
TL_{\rho,\sigma,h,R}
\varepsilon_{\rm car}(T)
\|\widetilde b(0)\|_2
```

を加える。パラメータは

1. $\rho,\sigma$
2. M37弱結合量 $\eta$
3. $\Delta$ と $K$
4. 比較幅、角切断、輸送、時計、記録精度

の順に選ぶ。この順序で任意の固定精度に対する有限構成が得られる。

本定理は、初期Born型準備を任意の初期実現配置分布からの収束として導かない。実現配置が複素振幅場の全エネルギー、質量、電荷を運ぶとも、連続空間の点粒子軌道、多粒子過程、固定帯域の同じ装置による $\epsilon\to0$、2重スリット完全検出周期を構成したとも主張しない。
