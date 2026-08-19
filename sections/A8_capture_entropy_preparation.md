@number: H
@chapter: 付録
@title: 捕捉entropy型初期共通原因準備と定常Nelson流
@status: 第8.13節のM44とR126について、ミクロHamiltonian候補、ready位相体積比、転送作用素、形成・保持分解、Doob変換、定常Nelson則、誤差と未証明点を詳述する。

## H.1 目的、範囲、既存モデルとの関係

本付録は、物理ポテンシャル $V$ に依存する非Gauss初期共通原因測度を、求める固有関数そのものを初期分布へ書き込まずに準備する候補を定める。採用するM44は、一つの熱的入射場、一つの非線形準安定捕捉器、同じ伝送路の出射部から成る。外部clock、離散packet列、独立な第2浴、未来の観測境界を基本構成へ入れない。

M37、M42、M44の役割は異なる。M37は有限実振動子網から空間複素振幅場を供給する。M42は、既に準備された場と実現配置について、有限配置グラフ上のBorn型等変性と有限Hamiltonian近似を与える。M44は、正の定常基底状態に限り、M42が別途必要とする初期作用比分布を捕捉中の粒子位置分布として作る候補である。一般の複素場、非零の流れ速度、励起状態、時間依存状態を準備するものではなく、R118またはM35の一般準備を置き換えない。

本付録では1次元の有界連結領域 $D$ を中心に書く。境界条件は、自由核とSchrödinger型作用素に同じ自己共役境界条件を使う。非有界領域は第H.12節でtail近似として扱う。

## H.2 ミクロ自由度とHamiltonian候補

粒子の正準対を $(X,P)$、伝送路の正規モードを $(Q_k,\Pi_k)$、捕捉器の反応座標を $(s,p_s)$、内部モードを $(q_a,p_a)$ とする。全Hamiltonianの候補を

```math
H_{\rm M44}
=
H_{\rm p}
+H_{\rm line+match}
+H_{\rm cap}
+H_{\rm loc}
```

と分ける。粒子部分は

```math
H_{\rm p}
=
\frac{P^2}{2m_{\rm b}}
+V(X)
```

である。$m_{\rm b}$ は裸質量であり、低周波自己energyを含めた物理質量が $m$ になるように選ぶ。物理ポテンシャル $V(X)$ はここに一度だけ入れる。

伝送路と座標--運動量matchingは、概念的には

```math
H_{\rm line+match}
=
\sum_{k=1}^{N}
\left[
\frac{(\Pi_k-\eta_kP)^2}{2\mu_k}
+
\frac{\mu_k\omega_k^2}{2}
\left(
Q_k-
\frac{c_kX}{\mu_k\omega_k^2}
\right)^2
\right]
```

と書ける。座標側の平方完成は浴が作る静的2次potentialを相殺するcountertermを含み、運動量側の平方完成は裸質量調整を必要とする。$c_k$ と $\eta_k$ のmatchingは、基準縮約核の拡散係数を $\nu$ に固定し、時間反転対称な低速sectorへ不要な反応項が残らないように選ぶ。具体的な有限帯域列からこの性質を一様に導くことは、M44の未証明命題の一つである。有限調和浴から再帰前の有効記憶核を得る一般的な背景は[12--14]にある。

捕捉器は

```math
H_{\rm cap}
=
\frac{p_s^2}{2M_s}
+U_{\rm cap}(s)
+H_A(\boldsymbol q,\boldsymbol p)
+\varepsilon U_{\rm mix}(s,\boldsymbol q)
```

とする。内部作用reservoirの基準形を

```math
H_A
=
\sum_{a=1}^{R}
\left[
\frac{p_a^2}{2\mu_a}
+
\frac{\mu_a\Omega_a^2q_a^2}{2}
\right]
```

とする。$U_{\rm cap}$ は入口鞍点とその奥の井戸を持ち、$U_{\rm mix}$ は捕捉後のenergyを多数の内部モードへ混合する弱い非線形相互作用である。$H_{\rm loc}$ は、粒子、反応座標、伝送路端点を局所的に結ぶ。入口鞍点上の結合Jacobianと障壁高には、先頭次数で余分な $X$ 依存性を持たせない。そうでなければ、後で得る有効potentialへ捕捉器固有の位置依存項が混入する。

## H.3 入射場、出射場、初期共通原因測度

伝送路は長い調和鎖として実現できる。連続近似では接触部近傍の場を

```math
Q(z,t)
=
Q_{\rm in}(t+z/c)
+Q_{\rm out}(t-z/c)
```

と入射成分と出射成分へ分ける。$Q_{\rm in}$ の遠方初期条件を熱的Gauss測度から取ると、接触部には連続的な熱雑音が入る。$Q_{\rm out}$ は独立な平衡浴ではなく、捕捉失敗、反射、後の脱出、粒子反作用によって作られる出力である。

無限鎖では出射波は局所接触部へ戻らない。長さ $L_{\rm line}$ の有限鎖では、波速を $c$ として

```math
T_{\rm rec}
\simeq
\frac{2L_{\rm line}}{c}
```

より短い観測窓を使う。したがって有効な一方向放射は基本的な非相反性ではなく、長い伝送路、再帰前の時間窓、位相整合した入射echoを含まない初期macrostateから生じる。全Hamiltonianの時間反転解は存在するが、それは過去の出射波を精密に逆向きへ入射させる非典型な初期条件に対応する。

捕捉過程は観測開始と無関係に進行してよい。任意の観測開始時刻における共通原因測度を模式的に

```math
\mu_{\rm cc}
\propto
\mu_{\rm in,T}
\mu_{A,E_*}
\mu_{\rm loc}
1_{\mathcal R}
```

と書く。$\mathcal R$ は現在のready位相領域である。この式は、未来波形または目的固有関数を指定しない。現在の粒子、捕捉器、入射場、過去の出射波が共通の過去から相関していることを表す。有限閉鎖系ではこの準定常状態を永久には維持できず、有限観測窓または無限伝送路極限が必要である。

離散時間幅 $\delta$ は物理的に分離されたpacketの幅ではない。連続場と内部混合を粗視化する時間分解である。古い捕捉結果は出射波列の空間位置へ保存され、有限鎖は観測時間内の有限記録帯として働く。

## H.4 ready領域と位相空間境界

反応座標の入口鞍点を

```math
s=s^\ddagger,
\qquad
U_{\rm cap}(s^\ddagger)=B
```

とする。readyとdumpを分ける境界は粒子位置 $X$ 上の壁ではなく、この反応座標の分割面である。鞍点を内向きに越え、内部energyが多数モードへ混合された位相領域をreadyと呼ぶ。鞍点を越えられず反射された状態、または内部energyが再び反応座標へ集中して脱出した状態は、出射波を伴うdump側へ入る。

ready領域は全位相空間の真のattractorではない。有限Hamiltonian流はLiouville体積を保存する。局所変数だけを見ると捕捉に見えるのは、内部混合により逆脱出が遅くなり、失敗・脱出情報が遠方の出射自由度へ運ばれ、それらを縮約するからである。有限の混沌環境が局所系へ有効散逸を与え得ることとの比較は[33]にあるが、M44で必要な特定の捕捉核は別に証明しなければならない。

## H.5 ready位相体積比

```math
W(x)
=
V(x)-V_{\min}
\geq0
```

と置く。全energyを固定し、入口鞍点を越えた内部自由度へ使える基準energyを

```math
E_*
=
E_{\rm tot}-B-V_{\min}
```

とする。粒子が $X=x$ にあると、捕捉器側へ配分できるenergyは $E_*-W(x)$ へ減る。

<!-- theorem-start:lemma -->
**補題（ミクロカノニカル捕捉流束）**

$R$ 個の独立調和内部モードを持ち、入口分割面上の余分な $x$ 依存prefactorがないとする。内向きのミクロカノニカル流束は

```math
\Phi_R(x)
=
\int_{p_s>0}
\frac{p_s}{M_s}
\delta
\left(
E_{\rm tot}
-V(x)-B
-\frac{p_s^2}{2M_s}
-H_A
\right)
\,dp_s\,d\Gamma_A
```

であり、$E_*>W(x)$ の範囲で

```math
\Phi_R(x)
=
C_R
\left[E_*-W(x)\right]^R
```

となる。従って最低potential位置に対する流束比は

```math
a_R(x)
=
\frac{\Phi_R(x)}{\Phi_R(x_{\min})}
=
\left(
1-
\frac{W(x)}{E_*}
\right)^R
```

である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明**

$p_s$ 積分について

```math
\int_0^\infty
\frac{p_s}{M_s}
\delta
\left(
E-
\frac{p_s^2}{2M_s}
-H_A
\right)
dp_s
=
1_{\{H_A\leq E\}}
```

である。従って $\Phi_R(x)$ は $H_A\leq E_*-W(x)$ を満たす内部位相体積に等しい。1個の調和正準対の位相体積はenergyに比例し、$R$ 個の直積では累積位相体積が $C_RE^R$ となる。比を取れば $C_R$ は消える。
<!-- theorem-end:proof -->

捕捉entropyを

```math
\Delta S_R(x)
=
k_B\log a_R(x)
```

と定めれば、$a_R=\exp(\Delta S_R/k_B)$ である。これは全系の細粒化Gibbs entropyの減少ではない。readyへ条件付けた可視位相体積の減少と、内部相関・出射波へ移った情報を区別する。

<!-- theorem-start:lemma -->
**補題（指数捕捉則）**

```math
E_*
=
\frac{4m\nu R}{\delta}
```

とし、$\delta\|W\|_\infty<4m\nu R$ とする。このとき

```math
a_R(x)
=
\left(
1-
\frac{\delta W(x)}{4m\nu R}
\right)^R
```

であり、$R\to\infty$ で一様に

```math
a_R(x)
\longrightarrow
a_\delta(x)
=
\exp
\left[
-\frac{\delta W(x)}{4m\nu}
\right]
```

へ収束する。さらに

```math
\log a_R(x)
=
-\frac{\delta W(x)}{4m\nu}
-
\frac{\delta^2W(x)^2}{32m^2\nu^2R}
+
O
\left(
\frac{\delta^3\|W\|_\infty^3}{R^2(m\nu)^3}
\right)
```

である。
<!-- theorem-end:lemma -->

これは目的固有関数を装置へ入力せず、通常の $V(X)$ が全energy配分を減らすことだけから得られる。ただし $E_*$ と $\nu$ の係数一致は、現段階ではM44のscale-matching条件である。

## H.6 熱的入射場から自由拡散核への縮約条件

捕捉を外した基準系について、粗視化位置核を $K_{\delta,N}$ とする。M44が必要とする有限浴駆動条件は

```math
K_{\delta,N}
=
I+\delta\nu\partial_x^2
+R_{\delta,N},
\qquad
\|R_{\delta,N}\|
=
o(\delta)
```

である。核表示では

```math
K_\delta(x,y)
=
\frac{1}{\sqrt{4\pi\nu\delta}}
\exp
\left[
-\frac{(y-x)^2}{4\nu\delta}
\right]
```

が基準になる。有限相関時間の速度揺らぎ $Y_t$ をOU近似で表すなら、

```math
dY_t
=
-\frac{Y_t}{\tau}\,dt
+
\sqrt{\frac{2D}{\tau}}\,dW_t,
\qquad
\langle Y_tY_0\rangle
=
D e^{-|t|/\tau}
```

から

```math
\nu
=
\int_0^\infty
\langle Y_tY_0\rangle\,dt
=
D\tau
```

となる。

ここで必要なのはOU過程をミクロ法則として置くことではない。有限Hamiltonian浴の初期集団とmatching結合から、再帰前の有限時間に同じ位置核が出ることを示すことである。一般の非線形 $V$ の下では、直接力 $-V'(X)$、条件付き運動量分散、記憶核、反作用を同時に追跡し、一段階位置核に余分な $O(\delta)$ driftまたは位置依存拡散が残らないことを証明しなければならない。この有限浴縮約はR126の入力条件であり、M44からの完全導出ではない。

## H.7 時間反転対称なready転送作用素

$A_{\delta,R}$ を $a_R$ の乗算作用素とする。ready領域へ射影した一段階作用素の目標形を

```math
G_{\delta,N,R,V}
=
A_{\delta,R}
K_{\delta,N}
A_{\delta,R}
+R_{\rm mix}
```

とする。$R_{\rm mix}$ は内部混合、残留記憶、入口Jacobian、有限保持時間に由来する残差である。二つの $A_{\delta,R}$ は二つの捕捉器ではない。一つの時間区間の形成側と保持側、または同じ捕捉器の安定方向と不安定方向に対応する。

連続経路の時間対称重み

```math
\exp
\left[
-\int_t^{t+\delta}
\frac{W(X_s)}{2m\nu}
\,ds
\right]
```

を端点で対称に分けると、

```math
\exp
\left[
-\frac{\delta W(x)}{4m\nu}
\right]
\exp
\left[
-\frac{\delta W(y)}{4m\nu}
\right]
```

となる。この対称分割が $A_\delta K_\delta A_\delta$ の形を与える。

<!-- theorem-start:theorem -->
**定理（R126：捕捉entropy型準備作用素と定常Nelson則）**

$D$ を有界連結領域、$V\in C^3(D)$ を下に有界な実potentialとする。次を仮定する。

1. $K_{\delta,N}$ は正で対称な基準核であり、$N\to\infty$、$\delta\to0$ の指定極限で

```math
K_{\delta,N}
=
I+\delta\nu\partial_x^2+o(\delta)
```

となる。

2. M44の捕捉端点因子は

```math
\log a_{\delta,R}(x)
=
-\frac{\delta W(x)}{4m\nu}
+o(\delta)
```

を一様に満たす。

3. ready射影残差は

```math
\|R_{\rm mix}\|
=
o(\delta)
```

であり、$G_{\delta,N,R,V}$ は正で既約なcompact作用素になる。

このとき

```math
G_{\delta,N,R,V}
=
I-
\frac{\delta}{2m\nu}
\left(
H_V-V_{\min}
\right)
+o(\delta),
\qquad
H_V
=
-2m\nu^2\partial_x^2+V.
```

$h_{\delta,N,R}>0$ を $G_{\delta,N,R,V}$ の主固有関数とすると、指定極限で $h_{\delta,N,R}\to\phi_0$ である。ここで

```math
H_V\phi_0
=
E_0\phi_0,
\qquad
\phi_0>0.
```

形成枝と保持枝を同じ主sectorへ収束させて任意時刻のready占有を読むと、その位置密度は

```math
\rho_V(x)
=
\frac{\phi_0(x)^2}
{\int_D\phi_0(y)^2\,dy}
```

へ収束する。対応するDoob変換の連続極限は前後drift

```math
b_+(x)
=
2\nu\frac{\phi_0'(x)}{\phi_0(x)},
\qquad
b_-(x)
=
-2\nu\frac{\phi_0'(x)}{\phi_0(x)}
```

を持ち、そのNelson時間対称加速度は

```math
m a_N(x)
=
-V'(x)
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

```math
A_{\delta,R}
=
I-
\frac{\delta W}{4m\nu}
+o(\delta)
```

と基準核の展開を掛け合わせると、

```math
A_{\delta,R}
K_{\delta,N}
A_{\delta,R}
=
I+\delta\nu\partial_x^2
-
\frac{\delta W}{2m\nu}
+o(\delta).
```

右辺は

```math
I-
\frac{\delta}{2m\nu}
\left(
-2m\nu^2\partial_x^2+W
\right)
+o(\delta)
```

であるから、生成子の主固有関数は $H_V$ の正の基底固有関数へ収束する。正値性、既約性、compact性により主固有関数は単純で正である。

形成枝と保持枝の積、Doob変換、加速度の各結論は第H.8節から第H.11節で個別に示す。
<!-- theorem-end:proof -->

R126は、三つの縮約条件を仮定した後の結論をまとめた仮説依存の近似結果である。ミクロカノニカル流束と有限 $R$ 収束はM44内で明示計算できるが、同じ一つの滑らかな有限Hamiltonianから基準核、反復因子化、残差 $o(\delta)$ を同時に導く部分は未証明である。

## H.8 形成枝、保持枝、平方密度

現在位置 $x$ へ到達する形成重みを $L_M(x)$、現在から保持できる位相体積を $R_M(x)$ とする。端点関数 $\ell_0,r_0>0$ に対して

```math
L_M
=
(G^*)^M\ell_0,
\qquad
R_M
=
G^Mr_0
```

と書く。任意時刻にready領域を読む分布は

```math
\rho_M(x)
=
\frac{L_M(x)R_M(x)}
{\int_D L_M(y)R_M(y)\,dy}
```

となる。一般の非対称正作用素では、左主固有関数を $l$、右主固有関数を $r$ とすると長時間分布は $lr$ に比例する。時間反転整合したM44では $G$ が対称なので $l=r=h$ となり、

```math
\rho_M(x)
\longrightarrow
\frac{h(x)^2}{\int_Dh(y)^2\,dy}
```

を得る。これは正作用素のPerron--Frobenius型主sector選択である。

二枝は二つの浴でも二つの捕捉器でもない。形成枝は過去の入射揺らぎから現在のready領域へ到達できた位相体積、保持枝は現在の内部energy分配から長く滞在できる位相体積である。保持因子を未来条件として数学的に表すことはできるが、物理的準備が未来波形を参照するわけではない。定常占有が形成率と平均滞在時間の積で重み付けされることの作用素表示である。

正規化した一枝だけでは一般に $h$ が得られ、$h^2$ にはならない。M44では一つの準安定捕捉器の形成方向と保持方向の交差が平方密度を作る。

## H.9 経路捕捉重みと経験密度大偏差

離散経路 $x_0,\ldots,x_M$ のready重みは

```math
\prod_{j=1}^{M}
G_{\delta,V}(x_{j-1},x_j).
```

端点以外の $a_\delta(x_j)$ は左右の区間から二度現れるので、連続極限の基準Brown経路測度 $\mathbb P_0^T$ に対して

```math
\frac{d\mathbb P_V^T}{d\mathbb P_0^T}
\propto
\exp
\left[
-\int_0^T
\frac{W(X_t)}{2m\nu}
\,dt
\right]
```

となる。これは前進経路と時間反転経路で同じ値を取る。時間反転で符号が変わるentropy生成ではなく、ready経路の利用可能位相体積を表す時間対称重みである。正の前後因子とreciprocal過程の関係は[25,32]と比較できるが、M44は未来観測境界でなく、常時進行する捕捉過程の形成・保持分解を使う。

自由拡散の長時間経験密度を $\rho$ とすると、基準率関数は

```math
I_0[\rho]
=
\nu
\int_D
\left|
\partial_x\sqrt\rho
\right|^2
dx.
```

捕捉重みを加えた率関数は

```math
I_V[\rho]
=
\nu
\int_D
\left|
\partial_x\sqrt\rho
\right|^2
dx
+
\int_D
\frac{W(x)}{2m\nu}
\rho(x)
dx.
```

$2m\nu$ を掛けて $V_{\min}$ を戻すと、最小化すべき汎関数は

```math
\mathcal F_V[\rho]
=
\frac{m\nu^2}{2}
\int_D
\frac{(\rho')^2}{\rho}
dx
+
\int_D
V(x)\rho(x)
dx.
```

$\rho=\varphi^2$、$\int_D\varphi^2dx=1$ と置けば

```math
\mathcal F_V[\varphi^2]
=
2m\nu^2
\int_D(\varphi')^2dx
+
\int_DV\varphi^2dx.
```

従って停留条件は

```math
-2m\nu^2\varphi''
+V\varphi
=
E\varphi
```

であり、正の最小解は $\phi_0$ である。この汎関数はGuerra--Morato作用のFisher項との関係を持つ[30]が、ここで導いたのは定常経験密度の変分であり、一般の時間依存Nelson作用ではない。

## H.10 Doob変換と前後drift

主固有対を

```math
G_{\delta,V}h_\delta
=
\lambda_0h_\delta,
\qquad
h_\delta>0
```

とする。readyで長く生存することを条件付けた確率核を

```math
P_\delta(x,dy)
=
\frac{G_{\delta,V}(x,y)h_\delta(y)}
{\lambda_0h_\delta(x)}
dy
```

と定める。固有方程式により行和は1である。$G$ が対称なら

```math
h_\delta(x)^2P_\delta(x,dy)
=
\frac{h_\delta(x)G_{\delta,V}(x,y)h_\delta(y)}
{\lambda_0}
dx\,dy
```

は $x,y$ の交換で不変なので、$h_\delta^2$ は不変密度であり詳細釣り合いを満たす。これはDoob変換[16]である。

連続極限の前向き生成作用素は

```math
L_+f
=
\nu f''
+
2\nu
\frac{\phi_0'}{\phi_0}
f'.
```

従って

```math
b_+
=
2\nu
\frac{\phi_0'}{\phi_0}.
```

定常密度 $\rho=\phi_0^2$ に対する前後driftの関係

```math
b_-
=
b_+
-2\nu\partial_x\log\rho
```

から

```math
b_-
=
-2\nu
\frac{\phi_0'}{\phi_0}
```

となる。現在速度と浸透速度は

```math
v
=
\frac{b_++b_-}{2}
=
0,
\qquad
u
=
\frac{b_+-b_-}{2}
=
\nu\partial_x\log\rho.
```

全捕捉器では出射波と隠れた位相空間流束が存在しても、対称なready位置sectorは可逆になる。温度差を持つ二浴または基本的なchiral伝送を導入しない理由は、位置sectorへ余分な非対称driftを持ち込みやすいためである。

## H.11 定常Nelson加速度とNewton則

前向き微分と後向き微分を

```math
D_+
=
\partial_t+b_+\partial_x+\nu\partial_x^2,
\qquad
D_-
=
\partial_t+b_-\partial_x-\nu\partial_x^2
```

とする。Nelsonの時間対称加速度を

```math
a_N
=
\frac12
\left(
D_+D_-+D_-D_+
\right)X
```

と定める[3--6]。一般に

```math
a_N
=
\partial_tv
+vv'
-uu'
-\nu u''.
```

M44が準備する定常sectorでは $v=0$ なので

```math
a_N
=
-uu'-\nu u''.
```

一方、$\rho=\phi_0^2$ と基底固有方程式から

```math
Q[\rho]
=
-2m\nu^2
\frac{(\sqrt\rho)''}{\sqrt\rho}
=
-m
\left(
\frac{u^2}{2}
+\nu u'
\right)
```

および

```math
Q[\rho]+V
=
E_0
```

を得る。微分すると

```math
V'
=
m
\left(
uu'+\nu u''
\right)
```

である。従って

```math
m a_N
=
-V'.
```

このNewton則はR126の縮約条件の下で得た定常ready位置過程についての結論である。一般の時間依存密度と流れについて

```math
m
\left(
\partial_tv+vv'
\right)
=
-\partial_x
\left(
V+Q[\rho]
\right)
```

をミクロHamiltonianから導出したわけではない。M44単独から複素位相または一般のSchrödinger時間発展も従わない。

## H.12 有限誤差、時間尺度、非有界potential

M44で必要な時間尺度分離は

```math
\tau_{\rm bath},\tau_{\rm mix}
\ll
\delta
\ll
\tau_{\rm hold},T_{\rm rec}.
```

$\tau_{\rm bath}$ は入射場の相関時間、$\tau_{\rm mix}$ は内部energy混合時間、$\tau_{\rm hold}$ はready平均保持時間である。$T=M\delta$ の経路について、誤差を少なくとも次へ分ける。

1. $\varepsilon_K$：有限浴、有限帯域、Markov近似の一段階核誤差。
2. $\varepsilon_{\rm cap}$：有限 $R$ の捕捉entropy誤差。
3. $\varepsilon_{\rm split}$：対称作用素分割の誤差。
4. $\varepsilon_{\rm mix}$：一つの捕捉器を反復利用する際の残留内部記憶。
5. $\varepsilon_{\rm rec}$：有限伝送路の反射と再帰。
6. $\varepsilon_{\rm tail}$：有限capacityで扱えない高potential領域。
7. $\varepsilon_{\rm lift}$：Doob位置過程とミクロ条件付きHamilton軌道の時間対称加速度の差。

有限 $R$ 誤差は一段階で概ね

```math
\varepsilon_{\rm cap}^{(1)}
=
O
\left(
\frac{\delta^2\|W\|_\infty^2}
{R(m\nu)^2}
\right)
```

である。独立な一段階核誤差を単純加算するなら $M\varepsilon_K=T\varepsilon_K/\delta$ が現れる。対称分割は十分滑らかな有界作用素上で局所 $O(\delta^3)$、固定時間の大域 $O(T\delta^2)$ を目標とする。ただし非有界生成子については作用素domainを固定した別証明が必要である。

非有界 $V$ と有限 $E_*$ を同時に使う場合、全空間で $W<E_*$ を満たせない。energy sublevel

```math
D_{E_*}
=
\{x:W(x)<E_*\}
```

で定理を適用し、外側の目標質量

```math
\varepsilon_{\rm tail}
=
\int_{D_{E_*}^{\rm c}}
\phi_0(x)^2dx
```

をtail誤差として残す。有限capacity模型が非有界potentialの全空間基底状態を厳密に準備するとは主張しない。

## H.13 導出状態と未証明命題

M44とR126の導出状態を次のように分ける。

| 段階 | 導出状態 | 主な条件または残差 |
|---|---|---|
| 調和内部モードの捕捉流束 | 厳密結果 | 理想分割面、余分な $x$ 依存prefactorなし |
| 有限 $R$ から指数捕捉則 | 明示誤差付き近似結果 | capacity条件とscale matching |
| $G=A K A$ からSchrödinger型生成子 | 仮説後は厳密、極限は近似結果 | $R_{\delta,N}$、$R_{\rm mix}=o(\delta)$ |
| 形成・保持分解から $h^2$ | 仮説後は厳密結果 | 正値性、既約性、主固有値gap |
| Doob変換と定常Nelson則 | 仮説後は厳密結果 | 対称核、正の基底固有関数 |
| 一つの有限Hamiltonianから全縮約条件を同時導出 | 予想・未解決 | 有限帯域、内部混合、反作用、再帰 |
| 一般時間依存流と励起状態 | 未導出 | 位相、節、非零現在速度が必要 |

特に次が未証明である。

1. 具体的な少数種類の滑らかな局所結合が、一般の非線形 $V$ に対して基準拡散核と捕捉因子を同時に作ること。
2. 一つの準安定捕捉器がfresh cell列なしに十分速く混合し、一段階残差 $o(\delta)$ で反復因子化すること。
3. 入射場が決める $\nu$ と内部capacityが決める捕捉entropy係数を、同じ作用reservoirの保存量から固定すること。
4. 縮約Doob過程の時間対称加速度が、元のHamilton軌道の条件付き前後加速度へ有限誤差で持ち上がること。

これらを別の仮説へ移しただけで解決と呼ばない。M44は、この四点を一つの物理構成に対する検証課題へ集約した現行補助モデルである。

## H.14 旧経路との違いと非主張

M2--M5の二側配置拡散研究では、前向き因子と終端条件から後向き因子を作る経路を検討した。M44は未来の観測条件を使わず、常時進行する一つの捕捉器の形成位相体積と保持位相体積を現在のready占有で掛け合わせる。数式上の左右因子が似ていても、準備の因果構造は異なる。

不採用M13は、浴反作用と条件付き運動量流束をFisher応力へ閉じる構成則を必要とした。M44では、基準拡散経路の経験密度大偏差がFisher項を作る。従って旧Fisher力密度閉鎖を再採用しない。ただし基準拡散核とミクロ時間対称加速度への持ち上げは、依然として別々に証明する必要がある。

旧順時間重み模型では、求める頻度を作る物理的な試行数え上げが不足していた。M44は捕捉流束の位相体積比を明示するが、$G=A K A$ の反復縮約が未証明である限り、目的重みを完全にミクロ導出したとはいえない。

正で既約な $G$ の主固有関数は正であり、長時間には最低固有sectorが優勢になる。符号を変える励起固有関数を同じ正位相体積だけで安定選択できない。励起状態には、対称性で分離された不変sector、物理的節障壁、符号または位相を運ぶ別の縮約量が必要である。

従ってM44とR126は、定常基底状態の初期共通原因準備と、そのsectorにおけるNelson時間対称Newton則までを扱う。Born型測定則全体、任意のSchrödinger時間発展、励起状態、Wallstrom問題、Bell型統計をこの結果だけから導かない。
