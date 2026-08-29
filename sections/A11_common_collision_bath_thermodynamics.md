@number: K
@chapter: 付録
@title: 有限粒子位置再平衡化と有限衝突熱浴
@status: M50とR161--R163について、R164の有限信号作用殻状態数から得た条件付き中間状態有効自由エネルギーに対する有限粒子位置再平衡化、有限衝突熱浴による局所詳細釣合い率、制御切替の経路ゆらぎ関係を証明する。Q1・Q2・Q3に共通な熱化部品として扱い、粗視化された有効仕事・熱と全微視的収支を区別する。

## K.1 目的、用語、主張範囲

本付録は、M50を使うQ1、Q2、Q3の整合条件を全時刻で保存することを要求しない。有限信号座標をHamiltonian制御する仕事行程と、その座標を固定して粒子位置を再平衡化する熱化行程を分離する。各操作面または固定入力時刻で条件付きGibbs分布へ戻せば、制御中に粒子位置が瞬時の分布を追跡する必要はない。

記号 $v\in\mathbb C^m$ は各試行に存在する有限信号座標、$X$ は有限連結配置グラフ上の粒子位置である。$X$ を動かす有限セル列を衝突熱浴と呼ぶ。信号担体、作用殻、衝突熱浴は互いに別の物理部分系である。

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

## K.3 R161：任意の有限信号方向への粒子位置再平衡化

各無向辺 $\{i,j\}\in E_X$ に対称活動度 $a_{ij}=a_{ji}>0$ を置く。固定した $v\neq0$ に対して

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{
\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}
}
```

とし、非隣接頂点間の率は零とする。生成子を

```math
(\mathcal L_v^\delta f)(i)
=
\sum_{j:j\sim i}
k_{i\to j}^\delta(v)
[f(j)-f(i)]
```

と書く。

基準分布の最小値、辺活動度の最小値を

```math
q_{\min}=\min_iq_i,
\qquad
a_{\min}=\min_{\{i,j\}\in E_X}a_{ij},
\qquad
m_\delta=\frac{\delta q_{\min}}{1+\delta}
```

とする。無重みグラフLaplacianの第1非零固有値を $\lambda_G>0$ とする。

<!-- theorem-start:theorem -->
**定理（R161：任意の有限信号方向に対する粒子位置再平衡化）**

有限連結 $G_X$、$\delta>0$、任意の $v\neq0$ について、上の生成子は既約かつ可逆であり、唯一の定常分布は $\pi^\delta(v)$ である。$L^2(\pi^\delta)$ における第1非零固有値を $\lambda_\delta(v)$ とすれば

```math
\lambda_\delta(v)
\geq
\kappa_Xa_{\min}m_\delta\lambda_G
=:
\lambda_\delta
```

が全bath rayに一様に成り立つ。任意の初期粒子位置分布 $p_0$ に対して

```math
D_{\rm TV}
\left(
p_T,
\pi^\delta(v)
\right)
\leq
C_\delta e^{-\lambda_\delta T},
\qquad
C_\delta
=
\frac12
\sqrt{m_\delta^{-1}-1}
```

である。また

```math
D_{\rm TV}
\left(
\pi^\delta(v),
w(v)
\right)
\leq
\frac{\delta}{1+\delta}
```

であり、全有限時間誤差は混合誤差と正則化誤差に分かれる。
<!-- theorem-end:theorem -->

詳細釣合いは各辺で

```math
\pi_i^\delta k_{i\to j}^\delta
=
\kappa_Xa_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
=
\pi_j^\delta k_{j\to i}^\delta
```

となることから従う。Dirichlet形式は

```math
\mathcal E_z^\delta(f,f)
=
\kappa_X
\sum_{\{i,j\}\in E_X}
a_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
(f_i-f_j)^2
```

である。$\pi_i^\delta\geq m_\delta$ なので

```math
\mathcal E_z^\delta(f,f)
\geq
\kappa_Xa_{\min}m_\delta
\sum_{\{i,j\}\in E_X}
(f_i-f_j)^2.
```

一様平均を $\overline f=L^{-1}\sum_if_i$ とすれば、グラフPoincaré不等式と分散の最小化性から

```math
\sum_{\{i,j\}\in E_X}
(f_i-f_j)^2
\geq
\lambda_G
\sum_i(f_i-\overline f)^2
\geq
\lambda_G
\operatorname{Var}_{\pi^\delta}(f).
```

これがスペクトルギャップ下界を与える。有限可逆鎖の $L^2$ 収縮とCauchy--Schwarz不等式から

```math
D_{\rm TV}(p_T,\pi^\delta)
\leq
\frac12e^{-\lambda_\delta T}
\left\|
\frac{p_0}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}.
```

任意の $p_0$ について

```math
\left\|
\frac{p_0}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}^2
=
\sum_i\frac{p_{0,i}^2}{\pi_i^\delta}-1
\leq
m_\delta^{-1}-1
```

なので前因子も一様である。正則化誤差は

```math
D_{\rm TV}(\pi^\delta,w)
=
\frac{\delta}{2(1+\delta)}
\sum_i|q_i-w_i|
\leq
\frac{\delta}{1+\delta}
```

から従う。

<!-- theorem-start:proof -->
**証明（R161）**

正値性と連結性が既約性を、辺ごとの恒等式が可逆性と定常性を与える。Dirichlet形式を無重みグラフの形式で下から抑えると一様スペクトルギャップが得られる。可逆半群の $L^2$ 収縮、初期密度の一様上界、正則化分布と理想対角の全変動距離を順に適用すれば表示式が従う。証明終。
<!-- theorem-end:proof -->

### K.3.1 nodeにおける一様局所再平衡化の障害

<!-- theorem-start:proposition -->
**命題（零占有切断点に対する局所詳細釣合いno-go）**

$\delta=0$ とし、目標分布 $w$ の零頂点 $v$ が $G_X$ の切断点であるとする。隣接辺だけを使い、$w$ に関して詳細釣合いを満たす有限率生成子は、$G_X\setminus\{v\}$ の異なる連結成分間で確率質量を輸送できない。従って全初期分布から $w$ へ収束する既約な局所生成子は存在しない。
<!-- theorem-end:proposition -->

$w_v=0$ と $w_i>0$ に対し、詳細釣合いは

```math
w_i k_{i\to v}
=
w_vk_{v\to i}
=0
```

を強制するので $k_{i\to v}=0$ である。切断点を通る全経路が閉じるため、各成分の確率質量は独立に保存される。

この障害を避けるには、正の背景占有率、非局所辺、補助橋状態の少なくとも1つが必要である。粒子位置熱化を使うM50の特殊化では $\delta>0$ を採用し、有限資源誤差として台帳に残す。混合を使わずM50枝を粒子位置へ直接decodeする1回限りの運転は、このnode命題の対象外である。

## K.4 R162：有限衝突熱浴による率の実現

固定した $v$ と辺 $\{i,j\}$ に対し、対称な基準障壁 $B_{ij}^0=B_{ji}^0$ を置く。制御された障壁を

```math
B_{ij}^\delta(v)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(v)
+
E_j^\delta(v)
\right]
```

とする。$B_{ij}^0\geq(\Theta/2)\log(m_\delta^{-1})$ なら、両方向の活性化エネルギーは非負である。

入射セルは、到着断面を横切る流束について運動エネルギー分布

```math
f_{\rm in}(\epsilon)
=
\beta e^{-\beta\epsilon},
\qquad
\epsilon\geq0
```

を持つとする。これは静止した熱粒子を無条件に標本化する分布ではなく、衝突面へ実際に到着した粒子を数える流束分布である。入射位置、到着時刻、運動方向とその共役変数も完全状態へ含める。各辺には反応座標 $r_{ij}$ と共役運動量を置き、2つの井戸の底を $E_i^\delta,E_j^\delta$、鞍点を $B_{ij}^\delta$ に持つ滑らかなポテンシャルで散乱させる。理想的な閾値反射・通過則は、その障壁を狭くする有限幅極限として扱う。

$X=i$ のセルが辺 $i\to j$ へ到着したとき、

```math
\epsilon
\geq
B_{ij}^\delta(v)-E_i^\delta(v)
```

なら通過させ、通過後のセルエネルギーを

```math
\epsilon'
=
\epsilon
+
E_i^\delta(v)
-
E_j^\delta(v)
```

とする。閾値未満なら反射させる。通過時には

```math
\epsilon+E_i^\delta
=
\epsilon'+E_j^\delta
```

が成り立つ。ここで保存されるのは、作用殻fiberを消去した粒子位置有効自由エネルギーとセルエネルギーの粗視化和である。fiberを明示した全微視的Hamiltonianのエネルギー保存をこの式だけから主張しない。さらに前向き閾値を満たすことと、出射状態が逆向き閾値を満たすことは同値である。

<!-- theorem-start:theorem -->
**定理（R162：局所詳細釣合い率の有限衝突熱浴実現）**

各辺の衝突試行流束を $\nu_{ij}=\nu_{ji}>0$ とする。上の流束分布、対称障壁、粗視化有効自由エネルギー保存散乱を採用すると、縮約された配置遷移率は

```math
k_{i\to j}^{\rm coll}(v)
=
\nu_{ij}
e^{-\beta B_{ij}^0}
\sqrt{
\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}
}
```

である。従って

```math
\nu_{ij}e^{-\beta B_{ij}^0}
=
\kappa_Xa_{ij}
```

と校正すればR161の生成子に一致する。上の反応座標ポテンシャルに、入射位置、到着時計、運動方向、反射枝、出射エネルギー、履歴セルを含めれば、拡大散乱写像は一対一な時間反転対を持つ滑らかなHamiltonian散乱で任意精度に近似できる。

固定観測時間 $T$、各辺の有限セル数 $K_{ij}$、有限エネルギー切断 $E_{\max}$ では、理想生成子の経路測度との差を

```math
\varepsilon_{\rm coll}
\leq
\varepsilon_{\rm overflow}
+
\varepsilon_{\rm energy}
+
\varepsilon_{\rm smooth}
+
\varepsilon_{\rm clock}
```

と評価できる。信号bath座標の有限保持誤差 $\varepsilon_{\rm hold}$ はこれと別に加える。超過衝突、閾値平滑化帯、controller保持失敗は正式な無反応結果へ含め、除外後の再規格化を行わない。
<!-- theorem-end:theorem -->

有効自由エネルギーを全枝共通の $g(v)$ だけ移し、障壁も同じだけ移すgauge変換

```math
E_i^\delta
\longmapsto
E_i^\delta+g,
\qquad
B_{ij}^\delta
\longmapsto
B_{ij}^\delta+g
```

では、活性化差 $B_{ij}^\delta-E_i^\delta$ と全遷移率が不変である。従ってR162はR164の全枝状態数に含まれる共通因子へ依存しない。

活性化エネルギーは

```math
B_{ij}^\delta-E_i^\delta
=
B_{ij}^0
+
\frac{\Theta}{2}
\log
\frac{\pi_i^\delta}{\pi_j^\delta}
```

なので、指数分布の尾確率から

```math
\begin{aligned}
k_{i\to j}^{\rm coll}
&=
\nu_{ij}
\exp
\left[
-\beta(B_{ij}^\delta-E_i^\delta)
\right]\\
&=
\nu_{ij}e^{-\beta B_{ij}^0}
\sqrt{\frac{\pi_j^\delta}{\pi_i^\delta}}
\end{aligned}
```

を得る。正逆率比は

```math
\log
\frac{k_{i\to j}^{\rm coll}}
{k_{j\to i}^{\rm coll}}
=
-\beta
\left(
E_j^\delta-E_i^\delta
\right)
=
\log
\frac{\pi_j^\delta}{\pi_i^\delta}.
```

これは局所詳細釣合いである。

有限セルについて、辺 $\{i,j\}$ の理想到着数を平均 $\nu_{ij}T$ のPoisson変数 $N_{ij}$ で表すなら

```math
\varepsilon_{\rm overflow}
\leq
\sum_{\{i,j\}\in E_X}
P(N_{ij}>K_{ij}).
```

入射エネルギーを $E_{\max}$ で切る誤差は、衝突セル総数を $K_{\rm tot}$ として

```math
\varepsilon_{\rm energy}
\leq
K_{\rm tot}e^{-\beta E_{\max}}
```

で抑えられる。固定有限個のセルと時計を事前配置すれば、有限時間の離散衝突列は有限個の正準散乱窓からなる。無期限反復にはfresh cellの流入と使用済みセルの流出が必要である。

記録前には新規入射セルを止め、辺チャネルの入口ゲートを閉じる。エネルギー切断された安全セルは閉じた辺を越えない。有限障壁裾、平滑化帯、時計ずれによる離脱だけを $\varepsilon_{\rm res}$ として残せる。これによりR143が仮定していた記録中の経路滞在を、衝突窓の停止と局所辺閉鎖から評価できる。

<!-- theorem-start:proof -->
**証明（R162）**

指数流束分布の尾確率へ活性化エネルギーを代入すると表示した遷移率が得られる。対称障壁は正逆率比を粒子位置有効自由エネルギー差だけにし、通過後エネルギー式は正逆散乱を一対一に対応させる。有限時間では到着数と最大エネルギーを切り、超過事象を完全結果集合へ残す。閾値比較、反射、通過、履歴保存を滑らかな有限幅散乱へ近似した誤差を加えれば有限セル上界が従う。証明終。
<!-- theorem-end:proof -->

## K.5 R163：制御切替と経路ゆらぎ関係

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

<!-- theorem-start:theorem -->
**定理（R163：信号切替と粒子位置の経路ゆらぎ関係）**

R161の生成子またはR162の衝突熱浴を、正逆protocolで同じ熱作用尺度 $\Theta$ により駆動する。このとき

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
<!-- theorem-end:theorem -->

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
**証明（R163）**

正逆経路の初期密度、jump率、待機因子を比べる。待機因子は反転protocolの対応区間と相殺し、残る率比と端点密度比が $e^\Sigma$ を与える。逆経路確率の総和は1なので積分ゆらぎ関係が従う。瞬間quench式は規格化されたGibbs分布へ直接代入して得る。証明終。
<!-- theorem-end:proof -->

## K.6 R170：M50固定入力時刻有限枝instrumentの証明

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

M47の1段測定はM50のQ1特殊化として次の操作面へ分ける。

1. R145で信号bath方向を目標rayへ準備する。
2. 方向を保持し、R164の作用枝容量と条件付き作用殻fiberを準備する。
3. R161/R162で粒子位置を条件付きGibbs分布へ近づける。
4. 衝突熱浴を切り、R140の分析器操作を行う。この間の粒子位置は瞬時分布を追跡しなくてよい。
5. 分析器終了後の方向を保持し、作用殻fiberを更新してから再びR161/R162を有限時間作用させる。
6. 入射セルを止めて辺ゲートを閉じ、R141の傾斜保持とR143の局所記録を行う。
7. 結果別テンプレート交換後、そのテンプレート方向に対して作用殻準備と再平衡化を行い、次の逐次測定へ渡す。

1回の再平衡化誤差をM50の共通台帳

```math
\begin{aligned}
\varepsilon_{M50}
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

Q2-1の中央4枝はR164の作用殻を直接decodeする。M35作用区間を確率源として挟まない。Q2-2の切断後局所殻は各翼でR170を特殊化し、完全共通原因 $\Lambda$ に条件付けた積因子化誤差を別の $\varepsilon_{\rm prod}$ として加える。Q3は入力時刻 $t_\star$ のM37標本を保持してR170へ渡す。$t_{\rm out}>t_\star$ の局所記録までのQ3固有の上流誤差は付録Fで記帳する。

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
4. R145のHopf方程式を作用殻fiberまたは同じ衝突熱浴から導いたこと。
5. 有限個のセルが無限時間のMarkov浴を厳密に再現すること。
6. 無反応またはoverflowを除外した後の条件付き統計。
7. $\delta=0$ で任意のnode方向を一様有限資源で再平衡化すること。
8. 解析器、Hopf pump、fiber、記録、template交換、resetまで含む周期全体の微視的仕事・熱・エントロピー収支。
9. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。

残る最重要目標は、作用容量結合、殻内平衡化、枝対称性、信号保持反作用をQ1・Q2・Q3の各完全周期または固定入力instrumentの有限局所Hamiltonianとして統合することである。R161--R164を完全な有限装置による一般Born測度の第一原理導出とは分類しない。
