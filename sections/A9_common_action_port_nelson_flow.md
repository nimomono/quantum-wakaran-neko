@number: I
@chapter: 付録
@title: 共通作用ポート型三角形capacity-current統合開放模型と時間依存Nelson流
@status: 第8.14節のM46とR130--R134について、phase-reduced開放方程式、指数capacity消去、半減衰、主共分散選択、局所current transducer、連続極限、時間対称Newton則を詳述する。

## I.1 この付録の目的と模型階層

M45は、周期反応座標、対数型捕捉エントロピー座標、熱雑音、受動散逸、負性抵抗型能動供給を持つ局所開放捕捉器である。R127とR128はその局所収支と指数位相体積を扱い、R129は局所エネルギー帳簿、時間比例切片則、周辺可逆性という3つの橋を仮定した後に定常基底密度と $v=0$ のNelson則を与える。M45の直接方程式から一般の時間依存流を得たわけではない。

M46は、この残る数学的鎖を閉じるために採用する**phase-reducedミクロ開放模型**である。M37のmatching Hamiltonian、M42の複素振幅場と実現配置、M45のlimit cycle、対数型capacity、準安定反応座標を再利用し、別の物理的latchまたは積分器を追加しない。追加するのは、消去後に仮定されていた三角形の開放結合を、採用方程式として明示することである。

M46の役割は次の4点である。

1. 対数型capacityの指数分布と局所loadingから、経路ごとのFeynman--Kac重みを導く。
2. 同じ作用ポートのphase-preserving散逸から、古典的生存率 $D$ に対する複素振幅の半減衰 $A=D^{1/2}$ を導く。
3. 複素slow covarianceの二成分を保持したまま主モードを選び、正の主固有関数だけを確率振幅の全情報と同一視しない。
4. matching Hamiltonianが作る相対位相を局所非負率へ符号化し、一般時間依存の $v$、$S$、前後drift、時間対称Newton則へ接続する。

ここで「ミクロ開放模型」と呼ぶのは、粒子位置、複素包絡、capacity、limit-cycle位相、入出力線を持つphase-reduced方程式を模型の最下位記述として採用するという意味である。この方程式を、さらに下位の有限閉鎖Hamiltonian回路から導出したとはしない。特に非相反な三角形結合、純散逸係数、独立出力雑音の抑制は、M46より下位に残る問題である。

## I.2 有限グラフ、作用尺度、ポテンシャル基準

有限連結グラフを

```math
\mathcal G=(\Lambda,E)
```

とし、正のグラフLaplacianを $L_{\mathcal G}\geq0$ とする。複素slow envelopeを $b\in\mathbb C^{|\Lambda|}$、実現配置を $X\in\Lambda$ とする。作用尺度を $\mathcal J_0>0$、拡散係数を $\nu>0$ とし、Nelson尺度整合を

```math
\mathcal J_0=2m\nu
```

と置く。有限グラフの空間Hamiltonianは

```math
H_V
=
\mathcal J_0\nu L_{\mathcal G}+V
=
\frac{\mathcal J_0^2}{2m}L_{\mathcal G}+V
```

である。連続極限で $L_{\mathcal G}\to-\Delta$ なら、運動項は $-\mathcal J_0^2\Delta/(2m)$ へ収束する。

capacity loadingに用いる非負ポテンシャルを

```math
W(x)=V(x)-V_{\rm ref}\geq0
```

とする。$V_{\rm ref}$ は定数であり、束縛問題では $V$ の下限以下に取る。定数シフトは実時間Schrödinger流には共通位相しか与えないが、開放capacityでは生存率の全体尺度を変えるため、準備規約の一部として固定する。

無選別の基準混合核を

```math
K_\delta
=
\exp
\left(
-\delta\nu L_{\mathcal G}
\right)
```

とする。有限連結グラフでは $K_\delta$ は対称Markov核であり、$\delta>0$ なら全成分が正である。

## I.3 共通limit cycleと内部mode記憶

負性抵抗発振器の安定limit cycleを $y_*(\varphi)$、位相を $\varphi$ とする。弱い局所結合の下で通常のphase reductionは

```math
\dot\varphi
=
\omega_c
+
\epsilon Z_\varphi(\varphi)\cdot F
+
O(\epsilon^2)
```

という形を持つ。M46では、この1周期をcapacity pulse、辺比較pulse、判定pulseの共通時間単位に使う。各pulseは別の時計ではなく、同じ $\varphi$ の異なる位相窓に支持を持つ滑らかな結合係数である。

M45の周期反応座標 $s$ は削除しない。$s$ の準安定領域と周期セルを使って、準備中と伝播中を区別する滑らかなgate

```math
\chi_{\rm prep}(s),
\qquad
\chi_{\rm prop}(s)
```

を定める。両者の主要な支持は重ならず、切替領域だけが有限幅を持つ。従ってmode記憶は既存の $s$ に内在し、別の二値latchを追加しない。

準備modeでは、capacity loading、phase-preserving散逸、辺混合、負性抵抗利得、入射雑音を作動させる。伝播modeではこれらの選別portを切り、M37のmatching HamiltonianとM42の実現配置更新を作動させる。伝播中にcapacity選別を残すと、非定常重ね合わせの相対振幅が減衰するため、mode分離は時間依存流に必要な構造である。

## I.4 三角形開放方程式

残りaction capacityを $I_t\geq0$ とする。準備modeで採用する理想loading則は

```math
\dot I_t
=
-W(X_t)
```

である。有限周期のphase reductionでは1周期 $\delta=2\pi/\omega_c$ ごとに

```math
I_{n+1}
=
I_n
-
\delta W(X_{n+1})
+
o(\delta)
```

となる。以下のR130--R134は $o(\delta)$ を除いた理想M46について厳密に述べ、元のlimit-cycle方程式へ戻すときは有限周期誤差を別に加える。

M46全体の因果依存をmodeをまたいで書けば

```math
b
\longrightarrow
q(b)
\longrightarrow
X
\longrightarrow
I
```

という三角形になる。ただし全ての矢印を同時に作動させるのではない。準備modeでは基準核 $K_\delta$ が $X$ を動かし、$X\to I$ のloadingと、同じ $W/\mathcal J_0$ を読む複素包絡の選別散逸を作動させる。伝播modeでは $b\to q^{\rm ct}(b)\to X$ を作動させ、$I$ を凍結する。いずれのmodeでも逆向きの $I\to X$、$X\to b$ を同じ時刻の運動方程式へ入れない。従ってcapacity loadingは位置方程式へ通常の保存力を追加せず、伝播中の実現配置はHamiltonian場へ反作用しない。

この一方向性は、閉鎖された受動Hamiltonian結合の一般的性質ではない。開放能動transducerでは、実際のloading energyを負性抵抗源が供給し、読み出し相関と過剰energyを出射線が運び去る。高input impedanceの弱いsensor結合と大きな能動gainの極限は三角形結合を近似し得るが、その具体的回路極限は本稿では証明しない。

## I.5 指数capacityと三係数整合

M45の対数型reservoirが作る残りenergyを $Z\geq0$ とし、理想指数分布を

```math
P(Z>z)
=
\exp
\left(
-\frac{z}{\Theta}
\right)
```

とする。limit-cycle周波数でenergyをactionへ移し、

```math
I=\frac{Z}{\omega_c}
```

と定義すると、

```math
P(I>i)
=
\exp
\left(
-\frac{i}{\mathcal J_0}
\right),
\qquad
\mathcal J_0
=
\frac{\Theta}{\omega_c}
```

となる。Nelson尺度と合わせれば

```math
\mathcal J_0
=
\frac{\Theta}{\omega_c}
=
2m\nu,
\qquad
\nu
=
\frac{\Theta}{2m\omega_c}.
```

$I$ のloading則をenergy表示へ戻すと

```math
\dot Z
=
-\omega_c W(X)
```

である。従って $\dot Z=-\alpha W(X)$ と書く規約では

```math
\alpha=\omega_c
```

となる。三つの係数を独立に調整するのでなく、指数escape尺度を作用へ換算する1回のmatchingが三係数関係を与える。

この関係はM46内部の予言である。M45の具体的Rayleigh係数、摩擦係数、伝送路impedanceから $\Theta$、$\omega_c$、$\alpha$ を独立に計算し、同じ関係を得たわけではない。

## I.6 R130：指数capacity消去

時刻 $n\delta$ までの消費actionを

```math
C_n
=
\delta
\sum_{k=1}^{n}
W(X_k)
```

とする。readyであり続ける条件は $I_0>C_n$ である。

<!-- theorem-start:theorem -->
**定理（R130：三角形capacity消去とFeynman--Kac重み）**

$I_0$ が平均 $\mathcal J_0$ の指数分布に従い、$I_{n+1}=I_n-\delta W(X_{n+1})$、$W\geq0$ とする。位置経路を固定したready生存確率は

```math
P
\left(
I_0>C_n
\mid
X_0,\ldots,X_n
\right)
=
\exp
\left[
-\frac{\delta}{\mathcal J_0}
\sum_{k=1}^{n}W(X_k)
\right].
```

さらに、ready条件下の残りcapacity $I_0-C_n$ は再び同じ指数分布に従う。従って内部capacityを消去した1周期の古典的非正規化位置核は

```math
\mathsf P_\delta
=
K_\delta D_\delta,
\qquad
D_\delta
=
\exp
\left(
-\frac{\delta W}{\mathcal J_0}
\right),
```

で閉じる。連続時間極限の経路重みは

```math
\exp
\left[
-\frac{1}{\mathcal J_0}
\int_0^tW(X_s)\,ds
\right]
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

指数分布の尾確率から直ちに

```math
P(I_0>C_n\mid X_0,\ldots,X_n)
=
\exp
\left(
-\frac{C_n}{\mathcal J_0}
\right)
```

を得る。また任意の $r\geq0$ について

```math
P
\left(
I_0-C_n>r
\mid
I_0>C_n
\right)
=
\frac{P(I_0>C_n+r)}{P(I_0>C_n)}
=
\exp
\left(
-\frac{r}{\mathcal J_0}
\right).
```

従ってready条件付き分布は各周期で統計的に再生する。位置が $x$ から $y$ へ $K_\delta(x,y)$ で移り、その後 $\delta W(y)$ を消費して残る確率が $D_\delta(y)$ なので、行核規約で $\mathsf P_\delta=K_\delta D_\delta$ となる。連続時間式はRiemann和の極限である。
<!-- theorem-end:proof -->

R130は物理的resetを毎周期行う定理ではない。実際のcapacityは過去の消費量を記憶するが、ready条件下の残量分布が指数分布へ戻るため、位置核だけを閉じられる。

## I.7 R131：生存率から複素振幅の半減衰へ

指数thresholdだけから $D^{1/2}$ は出ない。M46では同じ作用尺度を読むphase-preservingな線形散逸portを採用する。局所複素包絡の作用とenergyを

```math
J_x=\mathcal J_0|b_x|^2,
\qquad
E_x=\omega_cJ_x
```

とする。作用ポートが準備modeで

```math
\dot E_x
=
-\frac{W(x)}{\mathcal J_0}E_x
```

だけenergyを出射線へ渡し、同次数のfrequency shiftを残さないなら、

```math
\dot b_x
=
-\frac{W(x)}{2\mathcal J_0}b_x
```

となる。係数 $1/2$ は追加matchingでなく、作用が振幅の二乗であることから従う。

<!-- theorem-start:proposition -->
**命題（R131：共通作用ポートの半減衰と対称共分散核）**

R130のcapacity portと同じ $W/\mathcal J_0$ を持つphase-preserving線形散逸portを仮定する。1周期の古典的生存因子と複素振幅因子は

```math
D_\delta
=
\exp
\left(
-\frac{\delta W}{\mathcal J_0}
\right),
\qquad
A_\delta
=
\exp
\left(
-\frac{\delta W}{2\mathcal J_0}
\right)
=
D_\delta^{1/2}.
```

従って複素共分散の対称1周期核を

```math
\mathsf S_\delta
=
A_\delta K_\delta A_\delta
```

と取れる。古典的生存核 $\mathsf P_\delta=K_\delta D_\delta$ とは

```math
\mathsf S_\delta
=
A_\delta
\mathsf P_\delta
A_\delta^{-1}
```

の相似関係にある。さらに

```math
\mathsf S_\delta
=
I
-
\frac{\delta}{\mathcal J_0}
\left(
H_V-V_{\rm ref}
\right)
+
O(\delta^2).
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**

線形方程式を1周期積分すれば $A_\delta$ を得て、$|A_\delta b|^2=D_\delta|b|^2$ なので $A_\delta^2=D_\delta$ である。従って

```math
A_\delta
\mathsf P_\delta
A_\delta^{-1}
=
A_\delta K_\delta A_\delta^2A_\delta^{-1}
=
A_\delta K_\delta A_\delta.
```

また有限グラフ上で

```math
K_\delta
=
I-\delta\nu L_{\mathcal G}+O(\delta^2),
\qquad
A_\delta
=
I-\frac{\delta W}{2\mathcal J_0}+O(\delta^2).
```

これらを掛け合わせると

```math
\mathsf S_\delta
=
I
-\delta\nu L_{\mathcal G}
-\frac{\delta W}{\mathcal J_0}
+O(\delta^2).
```

$H_V-V_{\rm ref}=\mathcal J_0\nu L_{\mathcal G}+W$ を用いれば結論を得る。
<!-- theorem-end:proof -->

### I.7.1 二値threshold単独の限界

同じ指数capacityを二つの消費量 $c_x,c_y$ が共有し、両方を通過する条件だけを課すと、

```math
P(I>c_x,\ I>c_y)
=
\exp
\left[
-\frac{\max(c_x,c_y)}{\mathcal J_0}
\right]
```

となる。これは一般に

```math
\exp
\left[
-\frac{c_x+c_y}{2\mathcal J_0}
\right]
```

ではない。従って二方向のbinary ready条件を共有するだけでは、左右の幾何平均または複素振幅半減衰を導けない。R131に必要なのは、threshold survivorとは別に物理的自由度を増やすことではなく、既存複素包絡へ線形に作用する同じ出力portの散逸成分である。

R131は、phase-preserving純散逸portをM46の開放方程式として採用した後の厳密結果である。具体的負性抵抗回路から、$W$ 依存frequency pullingを $o(1)$ に抑えながらこの散逸係数だけを得る部分は未導出である。

## I.8 R132：主共分散選択と共通原因

$\mathsf S_\delta$ は実対称で成分が正なので、Perron--Frobenius固有対

```math
\mathsf S_\delta h_0
=
\lambda_0h_0,
\qquad
h_0>0
```

を持つ。準備modeの負性抵抗利得を $g$、1周期ごとの零平均入射雑音を $\eta_n$ とし、線形化したslow fieldを

```math
Y_{n+1}
=
g\mathsf S_\delta Y_n
+
\eta_n,
\qquad
E[\eta_n\eta_n^\dagger]=Q
```

とする。

<!-- theorem-start:theorem -->
**定理（R132：準臨界主共分散選択）**

$\mathsf S_\delta$ を有限次元の正で実対称な作用素とし、最大固有値 $\lambda_0$ が単純、$Q\geq0$、$\langle h_0,Qh_0\rangle>0$ とする。$g\lambda_0<1$ なら線形定常共分散は

```math
C_g
=
\sum_{k=0}^{\infty}
g^{2k}
\mathsf S_\delta^k
Q
\mathsf S_\delta^k.
```

$g\lambda_0\uparrow1$ の準臨界極限で

```math
\frac{C_g}{\operatorname{tr}C_g}
\longrightarrow
\frac{|h_0\rangle\langle h_0|}
{\langle h_0,h_0\rangle}.
```

従って非線形利得飽和が総作用 $\mathcal J_0\operatorname{tr}C$ を $\mathcal J_0$ に固定し、方向を変える残差が消える極限では

```math
C
\longrightarrow
\frac{|h_0\rangle\langle h_0|}
{\langle h_0,h_0\rangle},
\qquad
\rho_0(x)
=
\frac{h_0(x)^2}{\langle h_0,h_0\rangle}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$\mathsf S_\delta$ の正規直交固有基底を $h_a$、固有値を $\lambda_a$ とし、$\lambda_0>|\lambda_a|$ を $a>0$ について仮定する。固有基底でLyapunov級数を足すと

```math
\langle h_a,C_gh_b\rangle
=
\frac{\langle h_a,Qh_b\rangle}
{1-g^2\lambda_a\lambda_b}.
```

$(a,b)=(0,0)$ の成分だけが $g\lambda_0\uparrow1$ で発散し、他成分の分母は零から離れる。主成分の係数は仮定により正である。従ってtraceで規格化した極限は主固有射影となる。
<!-- theorem-end:proof -->

R132の線形共分散極限は厳密である。有限振幅のRayleigh飽和を含む非線形定常測度が、同じ精度でrank-oneへ集中することは別の摂動問題であり、spectral gap、利得飽和、雑音強度に依存する。

### I.8.1 一方向生存と平方密度の区別

行核 $\mathsf P_\delta=K_\delta D_\delta$ と対称作用素 $\mathsf S_\delta$ は相似である。$\mathsf S_\delta h_0=\lambda_0h_0$ なら、$\mathsf P_\delta$ の右・左固有関数は

```math
r=A_\delta^{-1}h_0,
\qquad
l=A_\delta h_0
```

であり、

```math
l(x)r(x)=h_0(x)^2
```

となる。しかし有限時刻の一方向生存だけで条件付けた終端分布は一般に左固有関数側へ近づき、$h_0^2$ そのものではない。$lr$ は長時間生存過程の内部時刻またはDoob変換後の不変密度に対応する。

M46は物理的な未来条件付けを導入しない。複素slow covarianceという現在の共通原因が、$|h_0\rangle\langle h_0|$ の二本の脚を同時に持ち、その対角が $h_0^2$ になる。過去と未来の二方向は、別々の二浴または未来probeでなく、同一時刻の共分散の左右成分として表現される。

## I.9 準備から伝播への受渡し

準備modeで選ばれたrank-one共分散を

```math
C_0
=
|\psi_0\rangle\langle\psi_0|,
\qquad
\langle\psi_0,\psi_0\rangle=1
```

とする。伝播modeへ入るとcapacity port、負性抵抗gain、選別散逸を切り、M37またはM42のHamiltonian流

```math
i\mathcal J_0\dot\psi_t
=
h(t)\psi_t
```

を作動させる。すると

```math
C_t
=
|\psi_t\rangle\langle\psi_t|
=
U_tC_0U_t^\dagger
```

であり、rankと総作用を保ったまま、slow covarianceの実部と虚部、すなわち振幅と相対位相を保持する。

M46の自律主モード選択だけから得られる $\psi_0=h_0$ は、静的 $V$ の基底固有状態なので時間発展は共通位相だけであり $v=0$ である。一般時間依存流には、基底状態に固定されないrank-one初期共分散が必要である。既存のM35/M42準備回路または明示的な外部操作で任意の $\psi_0$ を与えた後の伝播はR133とR134に含むが、任意複素状態の自律準備をM46が解いたとはしない。

## I.10 R133：局所current transducer

伝播Hamiltonianの辺成分を

```math
h_{ij}
=
|h_{ij}|e^{i\gamma_{ij}},
\qquad
\gamma_{ji}=-\gamma_{ij}
```

とする。第2.3節の辺流規約は

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
\psi_j^*h_{ji}\psi_i
\right).
```

M46の局所位相比較器は、$90$ 度ずらした二入力を重ねた非負強度を読む。$\rho_i=|\psi_i|^2>0$ 上でrateを

```math
q_{i\to j}^{\rm ct}
=
\frac{|h_{ij}|}
{2\mathcal J_0\rho_i}
\left|
\psi_i
+
i e^{i\gamma_{ij}}\psi_j
\right|^2
```

と定める。

<!-- theorem-start:theorem -->
**定理（R133：局所非負rateによる辺流と前後drift）**

有限HermitianグラフHamiltonianと、正の台上の上記rateを考える。全rateは非負であり、各辺で

```math
\rho_iq_{i\to j}^{\rm ct}
-
\rho_jq_{j\to i}^{\rm ct}
=
J_{i\to j}
```

が厳密に成り立つ。従って初期分布が $P(X_0=i)=\rho_i(0)$ なら、current-transducer過程は $P(X_t=i)=\rho_i(t)$ を保つ。

さらに1次元等間隔格子で

```math
h_{i,i+1}
=
-\frac{\mathcal J_0\nu}{a^2},
\qquad
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\mathcal J_0}
\right),
```

$\rho$ と $S$ が滑らかで $\rho$ が零から離れているなら、格子生成子は

```math
\mathcal L_af
=
(v+u)\partial_xf
+
\nu\partial_x^2f
+
O(a),
```

```math
v
=
\frac{\partial_xS}{m},
\qquad
u
=
\nu\partial_x\log\rho
```

へ収束する。時間反転driftは

```math
b_+=v+u,
\qquad
b_-=v-u
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$A=\psi_i^*e^{i\gamma_{ij}}\psi_j$ と置くと

```math
\rho_iq_{i\to j}^{\rm ct}
=
\frac{|h_{ij}|}{2\mathcal J_0}
\left(
\rho_i+\rho_j-2\operatorname{Im}A
\right),
```

```math
\rho_jq_{j\to i}^{\rm ct}
=
\frac{|h_{ij}|}{2\mathcal J_0}
\left(
\rho_i+\rho_j+2\operatorname{Im}A
\right).
```

差は $-2|h_{ij}|\operatorname{Im}A/\mathcal J_0$ である。一方、Hermitian性から $h_{ji}=|h_{ij}|e^{-i\gamma_{ij}}$ なので、これは $J_{i\to j}$ に一致する。master方程式の正味流がSchrödinger連続方程式と一致するため等変性が従う。

格子Laplacian辺では $\gamma_{i,i+1}=\pi$ であり、右左rateは

```math
q_\pm
=
\frac{\nu}{2a^2\rho(x)}
\left|
\psi(x)-i\psi(x\pm a)
\right|^2.
```

Taylor展開と $\mathcal J_0=2m\nu$ から

```math
q_\pm
=
\frac{\nu}{a^2}
\pm
\frac{v+u}{2a}
+
O(1).
```

従って

```math
q_+[f(x+a)-f(x)]
+
q_-[f(x-a)-f(x)]
=
(v+u)f'
+
\nu f''
+
O(a).
```

密度 $\rho$ を持つ拡散の時間反転公式 $b_-=b_+-2\nu\partial_x\log\rho$ を用いれば $b_-=v-u$ を得る。
<!-- theorem-end:proof -->

このrateはR113の最小率でない。両方向へ同じ次数の対称往復流を持つが、そのleading termが拡散係数 $\nu$ を作り、反対称差が量子currentを作る。従ってR133はR113を置換せず、共通作用ポートから動機づけられた物理的候補を追加する。

$\rho_i=0$ ではrate表示が特異である。厳密nodeを含む有限率装置には第2.5節の正則化、nodeで分離したsector、または有限幅遷移層が必要である。R133の連続極限は正の台のcompact部分に限る。

局所比較強度 $|\psi_i+i e^{i\gamma_{ij}}\psi_j|^2$ は、既存の二入力matching portへ四分の一周期の位相差を入れて読める。試行pulseの共通係数 $|h_{ij}|/(2\mathcal J_0)$ はR131と同じ作用尺度を使う。ただし具体的負性抵抗回路が、この正規化、有限帯域、node正則化を同時に実現することは未証明である。

## I.11 時間依存密度と作用位相

伝播modeの連続極限で

```math
i\mathcal J_0\partial_t\psi
=
\left[
-\frac{\mathcal J_0^2}{2m}\Delta
+
V
\right]\psi
```

とする。正の領域で

```math
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\mathcal J_0}
\right)
```

と分解する。実部と虚部は

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0,
\qquad
v
=
\frac{\nabla S}{m},
```

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
V
-
\frac{\mathcal J_0^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0
```

を与える。R129では $\psi=h_0$ を正実関数として固定したため $S$ は空間的に一定で $v=0$ だった。M46では伝播中に複素slow covarianceの二成分を消去せず、一般の $S(x,t)$ を保持する。

## I.12 R134：時間対称Newton則

前向き・後ろ向き微分を

```math
D_+
=
\partial_t
+
b_+\cdot\nabla
+
\nu\Delta,
```

```math
D_-
=
\partial_t
+
b_-\cdot\nabla
-
\nu\Delta
```

とする。時間対称加速度を

```math
a_N
=
\frac12
\left(
D_+D_-+D_-D_+
\right)X
```

と定義する。

<!-- theorem-start:theorem -->
**定理（R134：一般時間依存Nelson流の時間対称Newton則）**

$V$ を時間非依存の滑らかな実ポテンシャルとする。正で十分滑らかな $\rho$ を持つSchrödinger解 $\psi=\sqrt\rho\exp(iS/\mathcal J_0)$ が存在し、$\mathcal J_0=2m\nu$ とする。R133の連続極限で得る

```math
u=\nu\nabla\log\rho,
\qquad
v=\frac{\nabla S}{m},
\qquad
b_\pm=v\pm u
```

について

```math
a_N
=
\partial_tv
+
(v\cdot\nabla)v
-
(u\cdot\nabla)u
-
\nu\Delta u
```

であり、

```math
m a_N
=
-\nabla V
```

が成り立つ。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$D_+D_-X$ と $D_-D_+X$ を展開し、$b_\pm=v\pm u$ を代入すると交差項が消え、表示した $a_N$ を得る。$v$ は勾配場なのでHamilton--Jacobi式の勾配から

```math
\partial_tv
+
(v\cdot\nabla)v
=
-\frac{\nabla V}{m}
+
2\nu^2
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right).
```

一方、$u=\nu\nabla\log\rho$ について

```math
(u\cdot\nabla)u
+
\nu\Delta u
=
2\nu^2
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right).
```

両式を時間対称加速度へ代入すれば量子圧項が相殺し、$ma_N=-\nabla V$ を得る。
<!-- theorem-end:proof -->

R134は、M46が選ぶ開放準備sectorだけから任意の $\psi_0$ を自律生成する定理ではない。M37/M42のSchrödinger型伝播、R133の正の台上の連続極限、rank-one複素共分散の受渡しを仮定した後の解析的帰結である。静的二重井戸の片側局在状態のような非固有初期状態では、$\rho$ と $S$ が時間変化し、$v$ は一般に非零になる。この範囲でR129の定常式を時間依存へ拡張する。

時間依存 $V(x,t)$ に対しても同じ代数は $ma_N=-\nabla V(x,t)$ を与えるが、M37の現行ミクロ包絡定理は時間非依存結合に限る。時間依存駆動をM37へ持ち上げるには、第6.17節の低速または非共鳴条件が別に必要である。

## I.13 導出状態、誤差、反証条件

M46の結果を同じ確立度として扱ってはならない。

| 項目 | M46内の状態 | 下位模型への状態 |
|---|---|---|
| 指数capacityの無記憶消去 | 理想指数分布と三角形loadingの下で厳密 | M45は有限energyの近似指数分布を与える |
| $D\mapsto A=D^{1/2}$ | phase-preserving線形散逸portの下で厳密 | 具体的回路からの純散逸係数は未導出 |
| $\mathsf S_\delta=A_\delta K_\delta A_\delta$ | 有限グラフ上で厳密 | limit-cycle一周期へのphase reductionは $o(\delta)$ 誤差を持つ |
| 主共分散選択 | 線形準臨界極限で厳密 | 非線形飽和定常測度の集中誤差は未評価 |
| current rate恒等式 | 正の台上の有限グラフで厳密 | 具体的局所比較器とnode正則化は未完成 |
| 前後drift | 滑らかな正密度の格子極限で条件付き | 境界、node、一般グラフ細分化は未評価 |
| 時間対称Newton則 | Schrödinger流から解析的に厳密 | 一般初期複素状態の自律準備は未解決 |

次のいずれかが起きれば、M46の主張を対応する段階まで縮小する。

1. capacity loadingが位置方程式へ $O(1)$ の追加driftを返し、三角形極限が成立しない。
2. 出力portが $W$ と同次数の位相shiftを残し、$A_\delta$ が正実対角作用素にならない。
3. capacity thresholdに独立なdump-line雑音が加わり、指数無記憶則または共通gainが壊れる。
4. 準備modeと伝播modeの切替漏れが有限極限で残り、伝播中のcoherenceを減衰させる。
5. $g\lambda_0\uparrow1$ で非線形共分散が主固有射影へ集中しない。
6. current transducerの対称往復流が拡散係数 $\nu$ と一致しない、または反対称差が辺流と一致しない。
7. node正則化誤差が格子細分化で消えない。
8. graph-to-continuum極限で $b_+=v+u$ が一様に得られない。

M46は、共通limit cycle、既存capacity reservoir、既存反応座標、既存matching Hamiltonianを再利用するため、独立した第2reservoir、未来probe、外部clock、新しい積分器を要求しない。一方、同じ物理実体を再利用することは、必要な非相反応答が自動的に導出されたことを意味しない。残るミクロ課題は、共通作用ポートの純散逸gain、局所位相比較、capacity pulse、mode切替を、具体的な負性抵抗回路と一つの入出力線から誤差付きで同時に得ることである。
