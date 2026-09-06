@number: K
@chapter: 付録
@title: 共通matching生成子と有限衝突実装
@status: 一般化R161のcurrent--traffic matching、static詳細釣合い特殊化、一般化R162のbounded directed-rate finite collision実装とthermal特殊化を証明する。Q1・Q2のstatic instrumentとQ3のspatial moving processを同じmatching/collision原理から派生させる。

## K.1 目的、用語、主張範囲

本付録は、M54の有限configuration変数 (X) を動かす共通matching原理を扱う。Q1・Q2のstatic profileでは有限signalを固定して条件付き分布へ再平衡化し、制御中に (X) が瞬時分布を追跡することを要求しない。Q3のspatial profileでは同じR164条件付き分布が時間依存signalとともに動き、R161 moving specializationが全時刻matchingを保存する。

記号 $v\in\mathbb C^m$ は各試行に存在する有限signal座標、$X$ は有限configurationグラフ上の実在変数である。一般R162の有限cell列をcollision implementationと呼び、static detailed-balance特殊化だけを衝突熱浴と呼ぶ。signal担体、作用殻、collision cellは互いに別の物理部分系である。

本付録が導くのは、単一試行の $v$ に条件付けた局所再平衡化機構である。集団共分散 $C_Z$、統計振幅、全粒子位置密度、確率流を制御器へ入力しない。付録LのR164は、同じ試行の信号作用を枝容量へ写し、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き状態数が得られることを示す。本付録はその作用殻を消去した条件付き中間状態有効自由エネルギーを使う。有限衝突熱浴の微視的可逆性と熱化は既存の衝突模型を参照する [49]。粗視化熱力学と強結合での有効自由エネルギーの語義は [50,51] に従って区別する。

## K.2 R164状態数から得る条件付きGibbs族と有効自由エネルギー

有限連結無向グラフを $G_X=(\mathcal I,E_X)$ とし、$L=|\mathcal I|$ とする。信号次元 $m\leq L$ の等長埋込みを

```math
\Psi:\mathbb C^m\longrightarrow\mathbb C^L,
\qquad
\Psi^\dagger\Psi=I_m
```

とする。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定する。付録Lでは、単一試行の信号作用と枝容量を

```math
J_{\rm sig}(v)
=
\mathcal J_0v^\dagger v,
\qquad
A_i^\delta(v)
=
\mathcal J_0
\left[
|(\Psi v)_i|^2
+
\delta q_i v^\dagger v
\right]
```

と置き、排他的2作用殻の状態数が $\Omega_i^\delta\propto A_i^\delta$ となることをR164で示す。従って $v\neq0$ に対して

```math
w_i(v)
=
\frac{|(\Psi v)_i|^2}{v^\dagger v},
\qquad
\pi_i^\delta(v)
=
\frac{w_i(v)+\delta q_i}{1+\delta}
```

と置くと、R164から

```math
\pi_i^\delta(v)
=
\frac{\Omega_i^\delta(v)}
{\sum_j\Omega_j^\delta(v)}
```

である。$\Psi^\dagger\Psi=I_m$ から $\sum_iw_i=1$ であり、$\pi^\delta$ は正の確率分布である。共通位相と全振幅に対して

```math
\pi^\delta(\alpha v)
=
\pi^\delta(v),
\qquad
\alpha\in\mathbb C\setminus\{0\}
```

なので、目標分布はbath rayだけに依存する。

熱エネルギー尺度を $\Theta>0$、$\beta=\Theta^{-1}$ とする。作用殻の枝自由エネルギーと全枝基準を

```math
F_i^{\rm sh}(v)
=
-\Theta\log\Omega_i^\delta(v),
\qquad
F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\sum_j\Omega_j^\delta(v)
```

とし、gauge固定した条件付き粒子位置有効自由エネルギーを

```math
E_i^\delta(v)
=
F_i^{\rm sh}(v)-F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\pi_i^\delta(v)
```

と定める。$E_i^\delta$ は裸の配置エネルギーでなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。全系の平衡Hamiltonianと周辺化を別に与えた場合を除き、無条件に平均力Hamiltonianとは呼ばない。この規約では

```math
\sum_i
e^{-\beta E_i^\delta(v)}
=1
```

であり、平衡自由エネルギーの基準値は全ての $v$ で零である。作用殻明示表示の $\Omega_i^\delta$ と、作用殻消去表示の $e^{-\beta E_i^\delta}$ は同じ縮約を表すため、同じ分配関数内で積 $\Omega_i^\delta e^{-\beta E_i^\delta}$ を使わない。これは状態数の二重計数を避けるための表現規約である。

任意の粒子位置分布 $p$ に対し、非平衡自由エネルギーを

```math
\mathcal F[p\mid v]
=
\sum_i p_iE_i^\delta(v)
+
\Theta\sum_i p_i\log p_i
```

と置けば

```math
\mathcal F[p\mid v]
-
\mathcal F[\pi^\delta\mid v]
=
\Theta
D_{\rm KL}
\left(
p\|\pi^\delta(v)
\right)
```

である。従って条件付き再平衡化は、固定した $v$ における相対エントロピーと非平衡自由エネルギーの緩和として解釈できる。

## K.3 R161の証明：current--traffic matchingとstatic特殊化

有限configuration集合 \(\mathcal I\) 上の正の分布 \(\pi(t)\)、反対称current \(j_{ij}=-j_{ji}\)、対称traffic \(t_{ij}=t_{ji}\geq|j_{ij}|\) が

\`\`\`math
\dot\pi_i
=
\sum_jj_{ji}
\`\`\`

を満たすとする。第2章の定義

\`\`\`math
k^+_{i\to j}
=
\frac{t_{ij}+j_{ij}}{2\pi_i},
\qquad
k^-_{i\to j}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
\`\`\`

では非負性が直ちに従い、

\`\`\`math
\pi_i k^+_{i\to j}
-
\pi_j k^+_{j\to i}
=
j_{ij}.
\`\`\`

従って前向きmaster方程式は

\`\`\`math
\dot p_i
=
\sum_j
\left(
p_jk^+_{j\to i}
-
p_ik^+_{i\to j}
\right)
\`\`\`

であり、\(p=\pi\) を代入すると仮定したcontinuity equationに一致する。有限状態線形方程式の一意性から \(p(0)=\pi(0)\) なら \(p(t)=\pi(t)\) である。同じpath measureのBayes反転は

\`\`\`math
\frac{\pi_jk^+_{j\to i}}{\pi_i}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
=
k^-_{i\to j}
\`\`\`

となる。

### K.3.1 static detailed-balance特殊化

固定した非零signal \(v\) に対するR164分布 \(\pi^\delta(v)\) を取り、有限連結無向グラフの各辺に \(a_{ij}=a_{ji}>0\) を置く。

\`\`\`math
j_{ij}=0,
\qquad
t_{ij}
=
2\kappa_Xa_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
\`\`\`

とすれば

\`\`\`math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}}
\`\`\`

であり、従来のR161 static鎖を回収する。\(q_{\min}\)、\(a_{\min}\)、無重みgraph Laplacian gap \(\lambda_G\) と

\`\`\`math
m_\delta
=
\frac{\delta q_{\min}}{1+\delta}
\`\`\`

を用いると、Dirichlet形式は

\`\`\`math
\mathcal E^\delta(f,f)
=
\kappa_X
\sum_{\{i,j\}}
a_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
(f_i-f_j)^2
\`\`\`

である。従って

\`\`\`math
\lambda_\delta
\geq
\kappa_Xa_{\min}m_\delta\lambda_G
\`\`\`

となり、

\`\`\`math
D_{\rm TV}
\left(
p_T,\pi^\delta(v)
\right)
\leq
C_\delta e^{-\lambda_\delta T},
\qquad
C_\delta
=
\frac12\sqrt{m_\delta^{-1}-1}.
\`\`\`

R164の理想枝重み \(w\) との差は

\`\`\`math
D_{\rm TV}(\pi^\delta,w)
\leq
\frac{\delta}{1+\delta}.
\`\`\`

### K.3.2 nodeにおけるstatic再平衡化の障害

\(\delta=0\) とし、目標分布 \(w\) の零頂点 \(v\) がconfiguration graphの切断点であるとする。隣接辺だけを使い、\(w\) に関して詳細釣合いを満たす有限率生成子は、\(G_X\setminus\{v\}\) の異なる連結成分間で確率質量を輸送できない。詳細釣合いは

\`\`\`math
w_i k_{i\to v}
=
w_vk_{v\to i}
=0
\`\`\`

を強制するためである。この障害を避けるには正の背景、非局所辺、補助bridge stateの少なくとも1つが必要である。static profileでは \(\delta>0\) を採用し、spatial moving profileでも同じ正則化をnode回避に使う。

<!-- theorem-start:proof -->
**証明（R161）**

一般matching部分はcurrent恒等式と有限状態master方程式の一意性、backward rateはBayes反転から従う。static特殊化では \(j=0\) が詳細釣合いを与え、\(\pi_i^\delta\geq m_\delta\) によりDirichlet形式を無重みgraph形式で下から抑える。graph Poincare不等式、可逆半群の \(L^2\) 収縮、Cauchy--Schwarzを順に使うと一様mixing boundを得る。正則化誤差は \(\pi^\delta=(w+\delta q)/(1+\delta)\) から直接従う。証明終。
<!-- theorem-end:proof -->

## K.4 R162の証明：generic finite collisionとthermal特殊化

### K.4.1 一般有界有向rateのfinite collision持上げ

固定有限時間で区分連続な有向rate \(k_{i\to j}(t)\geq0\) と生成子 \(L(t)\) を取り、

\`\`\`math
M_*=
\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}k_{i\to j}(t)<\infty
\`\`\`

とする。有限分割 \(0=t_0<\cdots<t_M=T\) で各窓の生成子を \(\overline L_m\) へ凍結し、\(M_*\Delta t<1\) とすれば

\`\`\`math
P_m
=
I+\Delta t\,\overline L_m
\`\`\`

は確率行列である。時間順序指数とEuler積の差は

\`\`\`math
\varepsilon_{\rm step}
\leq
\int_0^T
\|L(t)-L_{\rm fr}(t)\|_{\rm row}\,dt
+
T M_*^2\Delta t\,e^{2M_*\Delta t}
\`\`\`

で抑えられる。

各stepへ一様Liouville threshold座標 \(u_m\in(0,1)\) とその共役座標、clock、空history、work registerを置く。現在configurationが \(i\) なら \((0,1)\) を長さ \(P_m(i,j)\) の区間へ分け、\(u_m\) が属する \(j\) へ移す。source、target、step番号、thresholdをhistoryへ残し、区間幅差を共役座標の逆伸縮を伴うcanonical squeezeで補う。有限個の平行移動・shear・squeezeを滑らかな有限時間Hamiltonian散乱へ近似すれば、指定読出し時刻の位置分布を対象Markov過程から

\`\`\`math
D_{\rm TV}
\leq
\varepsilon_{\rm step}
+
\varepsilon_{\rm coll}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm over}
\`\`\`

以内にできる。1-step-per-windowでは有限個のcellを事前配置できるため \(\varepsilon_{\rm over}=0\) と選べる。これは一般有向rateの実装であり、詳細釣合いまたは熱分布を仮定しない。

### K.4.2 thermal detailed-balance特殊化

R161 static profileの

\`\`\`math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}}
\`\`\`

については、条件付き有効自由エネルギー

\`\`\`math
E_i^\delta(v)
=
-\Theta\log\pi_i^\delta(v)
\`\`\`

と対称基準障壁 \(B_{ij}^0=B_{ji}^0\) を使う。制御障壁を

\`\`\`math
B_{ij}^\delta(v)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(v)+E_j^\delta(v)
\right]
\`\`\`

とし、到着断面の入射流束energyを

\`\`\`math
f_{\rm in}(\epsilon)
=
\beta e^{-\beta\epsilon}
\`\`\`

とする。通過条件 \(\epsilon\geq B_{ij}^\delta-E_i^\delta\) と通過後energy

\`\`\`math
\epsilon'
=
\epsilon+E_i^\delta-E_j^\delta
\`\`\`

により正逆散乱は1対1に対応する。縮約rateは

\`\`\`math
k_{i\to j}^{\rm coll}
=
\nu_{ij}e^{-\beta B_{ij}^0}
\sqrt{\frac{\pi_j^\delta}{\pi_i^\delta}},
\`\`\`

従って \(\nu_{ij}e^{-\beta B_{ij}^0}=\kappa_Xa_{ij}\) と校正すればR161 static rateに一致する。有限cell overflow、finite energy tail、boundary smoothing、clock、signal hold誤差を完全結果集合へ残し、成功試行だけを再規格化しない。

局所詳細釣合いは

\`\`\`math
\log
\frac{k_{i\to j}^{\rm coll}}
{k_{j\to i}^{\rm coll}}
=
-\beta(E_j^\delta-E_i^\delta)
=
\log\frac{\pi_j^\delta}{\pi_i^\delta}
\`\`\`

である。このthermal特殊化だけについてK.5の粗視化仕事・熱・entropy productionを定義する。

<!-- theorem-start:proof -->
**証明（R162）**

generic部分では、凍結生成子とEuler積の誤差を上の \(\varepsilon_{\rm step}\) で抑え、各有限確率行列を一様threshold座標の有限区間分割で実現する。historyを保存してcanonical squeeze、translation、shearを未使用sectorへ1対1に延長し、滑らかなHamiltonian散乱で近似すれば有限collision誤差が得られる。thermal特殊化では指数入射流束のtailへ活性化energyを代入して平方根型rateを得る。対称障壁と通過後energy式が正逆散乱と詳細釣合いを与える。証明終。
<!-- theorem-end:proof -->

## K.5 粗視化経路熱力学系の証明

以下は、非平衡仕事関係と経路エントロピー生成の標準形 [46--48] をR161、R162の条件付き粒子位置過程へ適用したものである。$E_i^\delta$ はR164の作用殻を消去した相対有効自由エネルギーなので、ここで定義する仕事と熱には上付き $\rm rel$ を付け、全微視的仕事・熱と区別する [50,51]。

単一試行信号 $v_t$ を外部制御写像により動かし、粒子位置有効自由エネルギーを $E_i^\delta(v_t)$ とする。粒子位置経路を

```math
\omega
=
(i_0,t_1,i_1,\ldots,t_N,i_N)
```

と書く。経路中の有効地形仕事と条件付き配置中間状態へ入る有効熱を

```math
W^{\rm rel}[\omega]
=
\int_0^T
\dot E_{X_t}^\delta(v_t)
\,dt,
```

```math
Q^{\rm rel}[\omega]
=
\sum_{\ell=1}^N
\left[
E_{i_\ell}^\delta(v_{t_\ell})
-
E_{i_{\ell-1}}^\delta(v_{t_\ell})
\right]
```

と定義すれば、粗視化された経路ごとに $\Delta E=W^{\rm rel}+Q^{\rm rel}$ である。

前向きprotocolを初期分布 $p_0$ から走らせ、その終端分布を $p_T$ とする。時間反転protocolは $p_T$ から開始する。両者の経路確率を $\mathcal P_F[\omega]$、$\mathcal P_R[\omega^\dagger]$ とする。全エントロピー生成を

```math
\Sigma[\omega]
=
\log\frac{p_0(i_0)}{p_T(i_N)}
+
\sum_{\ell=1}^N
\log
\frac{
k_{i_{\ell-1}\to i_\ell}^\delta(v_{t_\ell})
}{
k_{i_\ell\to i_{\ell-1}}^\delta(v_{t_\ell})
}
```

とする。

**第2章の粗視化経路熱力学系。**

R161 static specializationまたはR162 thermal specializationを、正逆protocolで同じ熱作用尺度 $\Theta$ により駆動する。このとき

```math
\frac{\mathcal P_F[\omega]}
{\mathcal P_R[\omega^\dagger]}
=
e^{\Sigma[\omega]},
```

```math
\left\langle
e^{-\Sigma}
\right\rangle_F
=1,
\qquad
\left\langle
\Sigma
\right\rangle_F
\geq0.
```

単一試行信号 $v^-$ の平衡分布から $v^+$ へ瞬間quenchする場合、状態 $i$ の有効地形仕事は

```math
W_i^{\rm rel}
=
\Theta
\log
\frac{\pi_i^\delta(v^-)}
{\pi_i^\delta(v^+)}
```

であり、採用した自由エネルギー基準では

```math
\left\langle
e^{-\beta W^{\rm rel}}
\right\rangle
=1,
```

```math
\langle W^{\rm rel}\rangle
=
\Theta
D_{\rm KL}
\left(
\pi^\delta(v^-)
\|
\pi^\delta(v^+)
\right).
```

作用殻明示表示では $W_i^{\rm sh}=\Delta F_i^{\rm sh}$ と書き、$W_i^{\rm rel}=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ である。全作用保存unitaryでは共通項が一定になり得るが、pumpまたはresetでは一定とは限らない。

連続時間jump経路の待機因子は正逆比で相殺し、jump因子の比が局所詳細釣合い率の積になる。初期終端密度比を加えると経路確率比を得る。逆経路測度について和を取れば積分ゆらぎ関係、Jensen不等式から平均非負性が従う。

瞬間quenchでは配置は動かず、有効地形仕事は有効自由エネルギー差だけである。従って

```math
\begin{aligned}
\left\langle e^{-\beta W^{\rm rel}}\right\rangle
&=
\sum_i
\pi_i^\delta(v^-)
\frac{\pi_i^\delta(v^+)}{\pi_i^\delta(v^-)}\\
&=
1,
\end{aligned}
```

平均を取れば相対エントロピー式になる。正逆経路確率比と積分ゆらぎ関係は粗視化跳躍過程について厳密である。一方、作用容量を変える過程、殻内平衡化、制御器反作用を含む完全Hamiltonianを構成しない限り、$W^{\rm rel}$ を全装置の機械仕事、$Q^{\rm rel}$ を全微視的熱と呼ばない。ゆらぎの定理はR164で得た地形の整合性を検査するが、作用殻状態数の線形則を導く定理ではない。

<!-- theorem-start:proof -->
**証明（粗視化経路熱力学系）**

正逆経路の初期密度、jump率、待機因子を比べる。待機因子は反転protocolの対応区間と相殺し、残る率比と端点密度比が $e^\Sigma$ を与える。逆経路確率の総和は1なので積分ゆらぎ関係が従う。瞬間quench式は規格化されたGibbs分布へ直接代入して得る。証明終。
<!-- theorem-end:proof -->

## K.6 R170：M54 static profile固定入力時刻instrumentの証明

入力時刻 $t_\star$ に非零信号 $v$ を空の保持registerへ正準SWAPする。SWAPは自己逆であり、交換前のregisterと時計面を履歴へ残せば拡大写像は1対1である。保持誤差または閾値失敗は無反応へ送る。

R164の単一Liouville母測度から、固定した $v$ に対する排他的枝分布は

```math
\pi_i^\delta(v)
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}{1+\delta}
```

となる。作用殻を消去した後は $E_i^\delta=-\Theta\log\pi_i^\delta$ だけを使うため、状態数を二重計数しない。

R161を時間 $\tau_X$ だけ作用させると、理想枝分布 $p_{\tau_X}$ は

```math
D_{\rm TV}
\left(
p_{\tau_X},
\pi^\delta(v)
\right)
\leq
C_\delta e^{-\lambda_\delta\tau_X}
=:
\varepsilon_{\rm mix}
```

を満たす。R162の有限衝突列でこの半群を近似する。衝突数超過、エネルギー切断、時計境界、滑らかな散乱近似の総偏差を $\varepsilon_{\rm coll}$ とすれば、データ処理不等式により粒子位置周辺の偏差も同じ量以下である。

熱化後に新規入射セルを止めて枝間ゲートを閉じる。枝 $i$ の安全領域内で1、他枝と通信路上で0となる滑らかな局所関数 $d_i(x)$ を選び、空の記録器へ

```math
G_{\rm rec}
=
\sum_i d_i(x)P_{D_i}
```

を作用させる。安全領域では1個の粒子位置枝だけが占有されるため、対応する1個の記録だけが動く。辺閉鎖、有限井戸幅、記録窓の偏差を $\varepsilon_{\rm lock}+\varepsilon_{\rm rec}$ とする。

各段階は確率核または無反応への写像であり、全変動距離を増加させない。作用容量、作用殻、混合、衝突、固定、記録、時計の有限偏差を順に合成すると

```math
\varepsilon_{170}
\leq
\varepsilon_{\rm hold}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
+\varepsilon_{\varnothing}
```

を得る。同じ物理偏差は最初に現れる項へだけ入れる。無反応を完全結果集合 $\mathcal I\cup\{\varnothing\}$ に残すため、成功試行の再規格化は不要である。

履歴には入力register、SWAP前後の時計、作用殻枝、衝突セル列、反射・透過ラベル、枝閉鎖状態、局所記録、無反応原因を残す。従って異なる入力または衝突履歴を同じ最終拡大状態へ潰さず、有限試行写像は単射である。全操作は有限時間なので $t_{\rm out}>t_\star$ を選べる。これでR170を得る。

この証明は、作用容量結合、作用殻fiber内平衡化、信号保持controller、衝突bath、記録器を1つの具体的Hamiltonianへ統合するものではない。R170は列挙した有限部品を指定誤差内で実行できることを前提にする条件付きinstrument定理である。

## K.7 Q1・Q2・Q3周期への接続

M47の1段測定はM54 static profileのQ1特殊化として次の操作面へ分ける。

1. R181AのW型2モード系で信号bath方向を目標rayへ準備する。
2. 方向を保持し、R164の作用枝容量と条件付き作用殻fiberを準備する。
3. R161/R162で粒子位置を条件付きGibbs分布へ近づける。
4. 衝突熱浴を切り、R140の分析器操作を行う。この間の粒子位置は瞬時分布を追跡しなくてよい。
5. 分析器終了後の方向を保持し、作用殻fiberを更新してから再びR161/R162を有限時間作用させる。
6. 入射セルを止めて辺ゲートを閉じ、R140の傾斜保持とR143の局所記録を行う。
7. 結果別テンプレート交換後、そのテンプレート方向に対して作用殻準備と再平衡化を行い、次の逐次測定へ渡す。

1回のstatic matching誤差を共通台帳

```math
\begin{aligned}
\varepsilon_{\rm match}
={}&\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sym}
+\varepsilon_{\rm ad}\\
&+\varepsilon_\delta
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
\end{aligned}
```

で記帳する。$\varepsilon_{\rm mix}=C_\delta e^{-\lambda_\delta T_X}$、$\varepsilon_\delta=\delta/(1+\delta)$ と選べる。Q1では2モード漏れと局所辺閉鎖誤差をそれぞれ $\varepsilon_{2m}$、$\varepsilon_{\rm res}$ として別に加える。この段階分離により、旧連続matching保存をR143、R144の仮定に使わない。

Q2-1はR181Dにより末端4mode信号を同次元hold-registerへSWAPし、容量latch後にR164/R170へ接続する。別の中間標本器を確率源として挟まない。Q2-2の切断後局所殻は各翼でR170を特殊化し、完全共通原因 $\Lambda$ に条件付けた積因子化誤差を別の $\varepsilon_{\rm prod}$ として加える。Q3はR164が与える同じ条件付き分布 $\pi^\delta(X\mid Z)$ を開始面でR161 static/R162 thermalにより準備し、その後は付録NのR161 moving specializationで同じ粒子を輸送する。spatial profileの一般有向率は局所詳細釣合いを仮定せず、R162 generic collisionをR184へ接続する。任意の固定時刻を診断する代替経路だけが付録FのR170を使う。

Q2-4のM54では、全gate後にR181Dが各bitの直交projector作用をraw容量へlatchする。R164はregularized容量比を排他的Born型状態数へ解釈し、R161/R162/R170がselectorを形成する。selector lock後に可逆filterとradial-only repumpを作用する。同じR170作用殻receiverを逐次nodeで使い、別のaperture標本器を重ねない。$L=2^n$ のsignal、work、history、cold、spent容量は受動資源として指数的でもよいが、個別の外部準備・較正・読出しには使わない。

## K.8 有限資源と正則化極限

$\pi_i^\delta\geq m_\delta$ から粒子位置有効自由エネルギー幅は

```math
\max_iE_i^\delta
-
\min_iE_i^\delta
\leq
\Theta\log(m_\delta^{-1}).
```

採用できる基準障壁も少なくとも同じ対数尺度を持つ。R161の一般下界は

```math
\lambda_\delta
=
O(\delta)
```

まで低下し得る。さらに $B_{ij}^0\geq(\Theta/2)\log(m_\delta^{-1})$ と率校正を同時に満たすには

```math
\nu_{ij}
\geq
\kappa_Xa_{ij}m_\delta^{-1/2}
```

が必要になり得る。さらにR164の有限幅作用殻を一様精度で保つ剛性は、他の尺度を固定すると下界の次数として

```math
\kappa
=
\Omega
\left(
\delta^{-2}
\right)
```

と増大する必要があり、$\kappa=\Theta(\delta^{-2})$ は代表的な選択である。従って $\delta\downarrow0$ では、有効地形幅、衝突流束、混合時間、作用殻剛性の少なくとも1つが発散する。有限資源のまま厳密nodeを全方向で追跡するとは主張しない。

有限周期数 $N_{\rm cyc}$ に対するfresh cellと履歴セルは少なくとも衝突数と記録数に比例する。固定容量の閉鎖系による無期限の熱化、永久記録、resetは行わない。

## K.9 R164で閉じた範囲と非主張

R164は単一試行信号作用から枝容量を作り、排他的2作用殻のLiouville状態数を単一母測度で規格化すると

```math
\Omega_i^\delta(v)
\propto
|(\Psi v)_i|^2
+
\delta q_i v^\dagger v
```

となり、$E_i^\delta=-\Theta\log\pi_i^\delta$ が作用殻を消去した条件付き中間状態有効自由エネルギーとして得られることを条件付きで厳密に示す。従って旧版の「Born型地形を確率から直接設計した」という未解決性は一段狭くなる。一方、本付録と付録Lは次を主張しない。

1. 枝容量結合 $A_i^\delta(v)$ と作用殻fiber内平衡化を同じ有限局所Hamiltonianから自動的に準備すること。
2. 枝対称な角周期、余面積因子、入口流束が信号担体だけから自動的に従うこと。
3. 信号bath座標を有限反作用で保持するcontrollerを含む全装置の最小Hamiltonian。
4. R181AのW型2モード系のHopf方程式を作用殻fiberまたは同じ衝突熱浴から導いたこと。
5. 有限個のセルが無限時間のMarkov浴を厳密に再現すること。
6. 無反応またはoverflowを除外した後の条件付き統計。
7. $\delta=0$ で任意のnode方向を一様有限資源で再平衡化すること。
8. 解析器、Hopf pump、fiber、記録、template交換、resetまで含む周期全体の微視的仕事・熱・エントロピー収支。
9. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。

残る最重要目標は、作用容量結合、殻内平衡化、枝対称性、信号保持反作用をQ1・Q2・Q3の各完全周期または固定入力instrumentの有限局所Hamiltonianとして統合することである。R161、R162、R164を完全な有限装置による一般Born測度の第一原理導出とは分類しない。