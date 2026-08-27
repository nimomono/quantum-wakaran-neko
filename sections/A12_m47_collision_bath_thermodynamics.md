@number: L
@chapter: 付録
@title: M47条件付きGibbs再平衡化と有限衝突熱浴
@status: R161--R163について、任意のM47階数1方向に対する有限W型配置再平衡化、有限衝突熱浴による局所詳細釣合い率、解析器quenchの経路ゆらぎ関係を証明し、Born型自由エネルギー地形の起源を未導出として分離する。

## L.1 目的、用語、主張範囲

本付録は、M47のmatchingを全時刻で保存することを要求しない。2モード信号bath座標をHamiltonian制御する仕事行程と、その座標を固定して実現配置を再平衡化する熱化行程を分離する。各操作面で条件付きGibbs分布へ戻せば、制御中に実現配置が瞬時の分布を追跡する必要はない。

記号 $z\in\mathbb C^2$ は各試行に存在する2モード信号bath座標、$X$ は有限W型配置グラフ上の実現配置である。$X$ を動かす有限セル列を衝突熱浴と呼ぶ。信号bathと衝突熱浴は別の物理部分系であり、単にbathとは書かない。

本付録が導くのは、単一試行の $z$ に条件付けた局所再平衡化機構である。集団共分散 $C$、統計振幅、全配置密度、確率流をcontrollerへ入力しない。一方、後で定義する配置エネルギーはBorn型対角から設計される。この構成をBorn測度の第一原理的起源とは呼ばない。有限衝突bathの微視的可逆性と熱化は既存の衝突模型の考え方を参照する [49]。

## L.2 条件付きGibbs族と自由エネルギー

有限連結無向グラフを $G_W=(\Omega_W,E_W)$ とし、$L=|\Omega_W|$ とする。W型最低2モードの配置埋込みを

```math
\Phi:\mathbb C^2\longrightarrow\mathbb C^L,
\qquad
\Phi^\dagger\Phi=I_2
```

とする。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定する。$z\neq0$ に対して

```math
w_i(z)
=
\frac{|(\Phi z)_i|^2}{z^\dagger z},
\qquad
\pi_i^\delta(z)
=
\frac{w_i(z)+\delta q_i}{1+\delta}
```

と置く。$\Phi^\dagger\Phi=I_2$ から $\sum_iw_i=1$ であり、$\pi^\delta$ は正の確率分布である。共通位相と全振幅に対して

```math
\pi^\delta(\alpha z)
=
\pi^\delta(z),
\qquad
\alpha\in\mathbb C\setminus\{0\}
```

なので、目標分布はbath rayだけに依存する。

熱作用尺度を $\Theta>0$、$\beta=\Theta^{-1}$ とし、条件付き配置エネルギーを

```math
E_i^\delta(z)
=
-\Theta\log\pi_i^\delta(z)
```

と定める。この規約では

```math
\sum_i
e^{-\beta E_i^\delta(z)}
=1
```

であり、平衡自由エネルギーの基準値は全ての $z$ で零である。

任意の配置分布 $p$ に対し、非平衡自由エネルギーを

```math
\mathcal F[p\mid z]
=
\sum_i p_iE_i^\delta(z)
+
\Theta\sum_i p_i\log p_i
```

と置けば

```math
\mathcal F[p\mid z]
-
\mathcal F[\pi^\delta\mid z]
=
\Theta
D_{\rm KL}
\left(
p\|\pi^\delta(z)
\right)
```

である。従って条件付き再平衡化は、固定した $z$ における相対エントロピーと非平衡自由エネルギーの緩和として解釈できる。

## L.3 R161：任意のbath方向への有限W型再平衡化

各無向辺 $\{i,j\}\in E_W$ に対称活動度 $a_{ij}=a_{ji}>0$ を置く。固定した $z\neq0$ に対して

```math
k_{i\to j}^\delta(z)
=
\kappa_Xa_{ij}
\sqrt{
\frac{\pi_j^\delta(z)}{\pi_i^\delta(z)}
}
```

とし、非隣接頂点間の率は零とする。生成子を

```math
(\mathcal L_z^\delta f)(i)
=
\sum_{j:j\sim i}
k_{i\to j}^\delta(z)
[f(j)-f(i)]
```

と書く。

基準分布の最小値、辺活動度の最小値を

```math
q_{\min}=\min_iq_i,
\qquad
a_{\min}=\min_{\{i,j\}\in E_W}a_{ij},
\qquad
m_\delta=\frac{\delta q_{\min}}{1+\delta}
```

とする。無重みグラフLaplacianの第1非零固有値を $\lambda_G>0$ とする。

<!-- theorem-start:theorem -->
**定理（R161：有限W型配置再平衡化）**

有限連結 $G_W$、$\delta>0$、任意の $z\neq0$ について、上の生成子は既約かつ可逆であり、唯一の定常分布は $\pi^\delta(z)$ である。$L^2(\pi^\delta)$ における第1非零固有値を $\lambda_\delta(z)$ とすれば

```math
\lambda_\delta(z)
\geq
\kappa_Xa_{\min}m_\delta\lambda_G
=:
\lambda_\delta
```

が全bath rayに一様に成り立つ。任意の初期配置分布 $p_0$ に対して

```math
D_{\rm TV}
\left(
p_T,
\pi^\delta(z)
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
\pi^\delta(z),
w(z)
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
\sum_{\{i,j\}\in E_W}
a_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
(f_i-f_j)^2
```

である。$\pi_i^\delta\geq m_\delta$ なので

```math
\mathcal E_z^\delta(f,f)
\geq
\kappa_Xa_{\min}m_\delta
\sum_{\{i,j\}\in E_W}
(f_i-f_j)^2.
```

一様平均を $\overline f=L^{-1}\sum_if_i$ とすれば、グラフPoincaré不等式と分散の最小化性から

```math
\sum_{\{i,j\}\in E_W}
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

### L.3.1 nodeにおける一様局所再平衡化の障害

<!-- theorem-start:proposition -->
**命題（零占有切断点に対する局所詳細釣合いno-go）**

$\delta=0$ とし、目標分布 $w$ の零頂点 $v$ が $G_W$ の切断点であるとする。隣接辺だけを使い、$w$ に関して詳細釣合いを満たす有限率生成子は、$G_W\setminus\{v\}$ の異なる連結成分間で確率質量を輸送できない。従って全初期分布から $w$ へ収束する既約な局所生成子は存在しない。
<!-- theorem-end:proposition -->

$w_v=0$ と $w_i>0$ に対し、詳細釣合いは

```math
w_i k_{i\to v}
=
w_vk_{v\to i}
=0
```

を強制するので $k_{i\to v}=0$ である。切断点を通る全経路が閉じるため、各成分の確率質量は独立に保存される。

この障害を避けるには、正の背景占有率、非局所辺、補助bridge状態の少なくとも一つが必要である。M47では $\delta>0$ を採用し、有限資源誤差として台帳に残す。

## L.4 R162：有限衝突熱浴による率の実現

固定した $z$ と辺 $\{i,j\}$ に対し、対称な基準障壁 $B_{ij}^0=B_{ji}^0$ を置く。制御された障壁を

```math
B_{ij}^\delta(z)
=
B_{ij}^0
-
\frac{\Theta}{2}
\log
\left[
\pi_i^\delta(z)
\pi_j^\delta(z)
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
B_{ij}^\delta(z)-E_i^\delta(z)
```

なら通過させ、通過後のセルエネルギーを

```math
\epsilon'
=
\epsilon
+
E_i^\delta(z)
-
E_j^\delta(z)
```

とする。閾値未満なら反射させる。通過時には

```math
\epsilon+E_i^\delta
=
\epsilon'+E_j^\delta
```

が成り立つ。さらに前向き閾値を満たすことと、出射状態が逆向き閾値を満たすことは同値である。

<!-- theorem-start:theorem -->
**定理（R162：M47局所詳細釣合い率の有限衝突熱浴実現）**

各辺の衝突試行流束を $\nu_{ij}=\nu_{ji}>0$ とする。上の流束分布、対称障壁、エネルギー保存散乱を採用すると、縮約された配置遷移率は

```math
k_{i\to j}^{\rm coll}(z)
=
\nu_{ij}
e^{-\beta B_{ij}^0}
\sqrt{
\frac{\pi_j^\delta(z)}{\pi_i^\delta(z)}
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
\sum_{\{i,j\}\in E_W}
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

指数流束分布の尾確率へ活性化エネルギーを代入すると表示した遷移率が得られる。対称障壁は正逆率比を配置エネルギー差だけにし、通過後エネルギー式は正逆散乱を一対一に対応させる。有限時間では到着数と最大エネルギーを切り、超過事象を完全結果集合へ残す。閾値比較、反射、通過、履歴保存を滑らかな有限幅散乱へ近似した誤差を加えれば有限セル上界が従う。証明終。
<!-- theorem-end:proof -->

## L.5 R163：解析器quenchと経路ゆらぎ関係

以下は、非平衡仕事関係と経路エントロピー生成の標準形 [46--48] をR161、R162の条件付き配置過程へ適用したものである。

bath方向を外部protocol $c_t$ とし、配置エネルギーを $E_i^\delta(c_t)$ とする。配置経路を

```math
\omega
=
(i_0,t_1,i_1,\ldots,t_N,i_N)
```

と書く。経路中の仕事と配置系へ入る熱を

```math
W[\omega]
=
\int_0^T
\dot E_{X_t}^\delta(c_t)
\,dt,
```

```math
Q[\omega]
=
\sum_{\ell=1}^N
\left[
E_{i_\ell}^\delta(c_{t_\ell})
-
E_{i_{\ell-1}}^\delta(c_{t_\ell})
\right]
```

と定義すれば、経路ごとに $\Delta E=W+Q$ である。

前向きprotocolを初期分布 $p_0$ から走らせ、その終端分布を $p_T$ とする。時間反転protocolは $p_T$ から開始する。両者の経路確率を $\mathcal P_F[\omega]$、$\mathcal P_R[\omega^\dagger]$ とする。全エントロピー生成を

```math
\Sigma[\omega]
=
\log\frac{p_0(i_0)}{p_T(i_N)}
+
\sum_{\ell=1}^N
\log
\frac{
k_{i_{\ell-1}\to i_\ell}^\delta(c_{t_\ell})
}{
k_{i_\ell\to i_{\ell-1}}^\delta(c_{t_\ell})
}
```

とする。

<!-- theorem-start:theorem -->
**定理（R163：M47解析器quench・配置再平衡化の経路ゆらぎ関係）**

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

初期方向 $c$ の平衡分布から方向 $c'$ へ瞬間quenchする場合、状態 $i$ に加えられる仕事は

```math
W_i
=
\Theta
\log
\frac{\pi_i^\delta(c)}
{\pi_i^\delta(c')}
```

であり、採用した自由エネルギー基準では

```math
\left\langle
e^{-\beta W}
\right\rangle
=1,
```

```math
\langle W\rangle
=
\Theta
D_{\rm KL}
\left(
\pi^\delta(c)
\|
\pi^\delta(c')
\right).
```

一般のエネルギー基準では $W$ を $W-\Delta F$ へ置き換える。
<!-- theorem-end:theorem -->

連続時間jump経路の待機因子は正逆比で相殺し、jump因子の比が局所詳細釣合い率の積になる。初期終端密度比を加えると経路確率比を得る。逆経路測度について和を取れば積分ゆらぎ関係、Jensen不等式から平均非負性が従う。

瞬間quenchでは配置は動かず、仕事はエネルギー差だけである。従って

```math
\begin{aligned}
\left\langle e^{-\beta W}\right\rangle
&=
\sum_i
\pi_i^\delta(c)
\frac{\pi_i^\delta(c')}{\pi_i^\delta(c)}\\
&=
1,
\end{aligned}
```

平均を取れば相対エントロピー式になる。

<!-- theorem-start:proof -->
**証明（R163）**

正逆経路の初期密度、jump率、待機因子を比べる。待機因子は反転protocolの対応区間と相殺し、残る率比と端点密度比が $e^\Sigma$ を与える。逆経路確率の総和は1なので積分ゆらぎ関係が従う。瞬間quench式は規格化されたGibbs分布へ直接代入して得る。証明終。
<!-- theorem-end:proof -->

## L.6 M47測定周期への接続

M47の1段測定を次の操作面へ分ける。

1. R145で信号bath方向を目標rayへ準備する。
2. 方向を保持し、R161/R162で実現配置を条件付きGibbs分布へ近づける。
3. 衝突熱浴を切り、R140の分析器操作を行う。この間の実現配置は瞬時分布を追跡しなくてよい。
4. 分析器終了後の方向を保持し、再びR161/R162を有限時間作用させる。
5. 入射セルを止めて辺ゲートを閉じ、R141の傾斜保持とR143の局所記録を行う。
6. 結果別テンプレート交換後、そのテンプレート方向に対して再平衡化し、次の逐次測定へ渡す。

1回の再平衡化誤差を

```math
\varepsilon_{\rm eq}
=
C_\delta e^{-\lambda_\delta T_X}
+
\frac{\delta}{1+\delta}
+
\varepsilon_{\rm coll}
+
\varepsilon_{\rm hold}
```

とする。2モード漏れと局所辺閉鎖誤差はそれぞれ $\varepsilon_{2m}$、$\varepsilon_{\rm res}$ として別に加える。この段階分離により、R137の全時刻matching保存をR143、R144の仮定に使わない。

## L.7 有限資源と正則化極限

$\pi_i^\delta\geq m_\delta$ から配置エネルギー幅は

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

が必要になり得る。従って $\delta\downarrow0$ では、エネルギー幅、衝突流束、混合時間の少なくとも一つが発散する。有限資源のまま厳密nodeを全方向で追跡するとは主張しない。

有限周期数 $N_{\rm cyc}$ に対するfresh cellと履歴セルは少なくとも衝突数と記録数に比例する。固定容量の閉鎖系による無期限の熱化、永久記録、resetは行わない。

## L.8 Born型地形の起源と非主張

R161は目的分布を初期配置測度へ直接置かず、有限時間の局所熱化から作る。R162はその率を微視的に可逆な衝突散乱へ持ち上げる。しかし

```math
E_i^\delta(z)
=
-\Theta\log\pi_i^\delta(z)
```

自体は設計されたcontroller地形である。従って本付録は次を主張しない。

1. Born型重みがW型装置の自然な状態数から自発的に発生すること。
2. 信号bath座標を有限反作用で保持するcontrollerを含む全装置の最小Hamiltonian。
3. R145のHopf方程式を同じ衝突熱浴から導いたこと。
4. 有限個のセルが無限時間のMarkov浴を厳密に再現すること。
5. 無反応またはoverflowを除外した後の条件付き統計。
6. $\delta=0$ で任意のnode方向を一様有限資源で再平衡化すること。
7. 解析器、Hopf pump、記録、template交換、resetまで含む周期全体の仕事・熱・エントロピー収支。

より深い未解決目標は、M47内部自由度の局所位相体積 $\Omega_i(z)$ から

```math
\Omega_i(z)
\propto
|(\Phi z)_i|^2
+
\delta q_i
```

を導き、$E_i^\delta$ を状態数の対数として得ることである。この位相体積起源が得られるまでは、R161--R163をBorn測度の第一原理的導出とは分類しない。
