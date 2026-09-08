@number: K
@chapter: 付録
@title: 共通整合生成子と開放jump実現
@status: R161の確率流・活動量整合と静的特殊化、新R162の有界有向率に対する開放Poisson-jump実現を証明する。Q1・Q2の静的平方根選択はR190/R179へ分離し、旧有限衝突Hamiltonian実装は強化結果として本論から退役する。

## K.1 目的、用語、主張範囲

本付録はM54の有限配置変数 $X$ を動かす共通整合原理を扱う。R161は目標分布、確率流、活動量から前向き・Bayes後向き率を定める。Q3では、その率を新R162の明示的な古典開放Poisson reservoirで直接実現する。Q1・Q2の静的測定では、R164の作用容量とR190の無限Drude浴・作用開口を用い、反復時のfreshnessをR179へ委ねる。

ここで「古典ミクロ模型」は有限閉鎖Hamiltonian系だけを意味しない。状態空間、局所率、確率入力、観測出力、適用時間を明示した開放jump方程式も採用ミクロ方程式として許す。有限衝突Hamiltonian列への持上げは固定目標の必要条件ではなく、旧R162/R188の強化結果として論文外メモへ保存する。

## K.2 ## K.2 R164状態数から得る条件付きGibbs族と有効自由エネルギー

有限連結無向グラフを $G_X=(\mathcal I,E_X)$ とし、$L=|\mathcal I|$ とする。信号次元 $m\leq L$ の等長埋込みを

```math
\Psi:\mathbb C^m\longrightarrow\mathbb C^L,
\qquad
\Psi^\dagger\Psi=I_m
```

とする。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定する。付録Lでは、単一試行の信号作用と結果成分容量を

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

なので、目標分布は浴 状態方向だけに依存する。

熱エネルギー尺度を $\Theta>0$、$\beta=\Theta^{-1}$ とする。作用殻の結果成分自由エネルギーと全結果成分基準を

```math
F_i^{\rm sh}(v)
=
-\Theta\log\Omega_i^\delta(v),
\qquad
F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\sum_j\Omega_j^\delta(v)
```

とし、ゲージ固定した条件付き粒子位置有効自由エネルギーを

```math
E_i^\delta(v)
=
F_i^{\rm sh}(v)-F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\pi_i^\delta(v)
```

と定める。$E_i^\delta$ は裸の配置エネルギーでなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。全系の平衡ハミルトニアンと周辺化を別に与えた場合を除き、無条件に平均力ハミルトニアンとは呼ばない。この規約では

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

## K.3 R161の証明：確率流・活動量整合と静的特殊化

有限配置集合 $\mathcal I$ 上の正の分布 $\pi(t)$、反対称確率流 $j_{ij}=-j_{ji}$、対称活動量 $t_{ij}=t_{ji}\geq|j_{ij}|$ が

```math
\dot\pi_i
=
\sum_jj_{ji}
```

を満たすとする。第2章の定義

```math
k^+_{i\to j}
=
\frac{t_{ij}+j_{ij}}{2\pi_i},
\qquad
k^-_{i\to j}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
```

では非負性が直ちに従い、

```math
\pi_i k^+_{i\to j}
-
\pi_j k^+_{j\to i}
=
j_{ij}.
```

従って前向きマスター方程式は

```math
\dot p_i
=
\sum_j
\left(
p_jk^+_{j\to i}
-
p_ik^+_{i\to j}
\right)
```

であり、$p=\pi$ を代入すると仮定した連続方程式に一致する。有限状態線形方程式の一意性から $p(0)=\pi(0)$ なら $p(t)=\pi(t)$ である。同じ経路分布のBayes反転は

```math
\frac{\pi_jk^+_{j\to i}}{\pi_i}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
=
k^-_{i\to j}
```

となる。

### K.3.1 静的 詳細釣り合い特殊化

固定した非零信号 $v$ に対するR164分布 $\pi^\delta(v)$ を取り、有限連結無向グラフの各辺に $a_{ij}=a_{ji}>0$ を置く。

```math
j_{ij}=0,
\qquad
t_{ij}
=
2\kappa_Xa_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
```

とすれば

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}}
```

であり、従来のR161静的鎖を回収する。$q_{\min}$、$a_{\min}$、無重みグラフLaplacian ギャップ $\lambda_G$ と

```math
m_\delta
=
\frac{\delta q_{\min}}{1+\delta}
```

を用いると、Dirichlet形式は

```math
\mathcal E^\delta(f,f)
=
\kappa_X
\sum_{\{i,j\}}
a_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
(f_i-f_j)^2
```

である。従って

```math
\lambda_\delta
\geq
\kappa_Xa_{\min}m_\delta\lambda_G
```

となり、

```math
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
```

R164の理想結果重み $w$ との差は

```math
D_{\rm TV}(\pi^\delta,w)
\leq
\frac{\delta}{1+\delta}.
```

R190A--R190Cは、この静的平方根率に対して作用殻明示表示の別の物理接続を与える。R190は固定済み正作用容量を2作用LC殻へ渡し、無限Drude浴で作用比を混合して対称作用開口で平方根kernelを得る十分条件であり、R161の一般整合定理そのものを変更しない。

### K.3.2 節点における静的再平衡化の障害

$\delta=0$ とし、目標分布 $w$ の零頂点 $v$ が配置 グラフの切断点であるとする。隣接辺だけを使い、$w$ に関して詳細釣合いを満たす有限率生成子は、$G_X\setminus\{v\}$ の異なる連結成分間で確率質量を輸送できない。詳細釣合いは

```math
w_i k_{i\to v}
=
w_vk_{v\to i}
=0
```

を強制するためである。この障害を避けるには正の背景、非局所辺、補助接続 状態の少なくとも1つが必要である。静的状態構成では $\delta>0$ を採用し、空間 移動 状態構成でも同じ正則化を節点回避に使う。

<!-- theorem-start:proof -->
**証明（R161）**

一般整合部分は確率流恒等式と有限状態マスター方程式の一意性、後退 率はBayes反転から従う。静的特殊化では $j=0$ が詳細釣合いを与え、$\pi_i^\delta\geq m_\delta$ によりDirichlet形式を無重みグラフ形式で下から抑える。グラフ Poincare不等式、可逆半群の $L^2$ 収縮、Cauchy--Schwarzを順に使うと一様混合上界を得る。正則化誤差は $\pi^\delta=(w+\delta q)/(1+\delta)$ から直接従う。証明終。
<!-- theorem-end:proof -->

## K.4 R162の証明：開放Poisson-jump実現

有限状態集合上の各有向辺 $(i,j)$ に独立なPoisson random measure $N_{ij}(dt\,du)$ を強度 $dt\,du$ で置く。配置が $i$ にある時刻 $t$ に、点 $(t,u)$ が $0<u<k_{i\to j}(t)$ を満たしたときだけ $i\to j$ を実行する。有限状態数と一様な総流出率上界 $M_*<\infty$ により、固定有限時間内のjump数は率 $M_*$ のPoisson過程で上から支配されるので非爆発である。

小時間 $dt$ では

```math
P(X_{t+dt}=j\mid X_t=i)
=
k_{i\to j}(t)dt+o(dt),
```

```math
P(X_{t+dt}=i\mid X_t=i)
=
1-dt\sum_{j\ne i}k_{i\to j}(t)+o(dt).
```

従って生成子は

```math
(L_tf)(i)
=
\sum_{j\ne i}
k_{i\to j}(t)[f(j)-f(i)]
```

であり、Kolmogorov前進方程式はR161のmaster equationに一致する。R161の整合条件から初期分布 $p(0)=\pi(0)$ なら $p(t)=\pi(t)$ である。同じ経路法則の2時刻条件付き確率にBayes則を適用すれば後向き率はR161の $k^-$ となる。物理的逆時間bathは追加しない。

旧有限衝突模型で必要だったEuler凍結、fresh threshold cell、比較境界帯、canonical latch、余接持上げ、時計誤差、有限骨格history TVは、この採用開放模型の中心証明には現れない。

<!-- theorem-start:proof -->
**証明（R162）**

上のPoisson構成の標準的なcompensator計算から生成子式を得る。有限総hazard上界が非爆発性を与え、有限状態のKolmogorov方程式の一意性からR161の周辺分布が従う。後退率は同じ前向き経路法則のBayes反転であり、別の確率源を必要としない。証明終。
<!-- theorem-end:proof -->

## K.5 R170吸収pointer固定の証明

選択終了時刻 $t_s$ 以降は $X$ を固定し、pointerを $Y=\varnothing$ から開始する。条件付きでcapture時刻は率 $\gamma$ の指数分布だから

```math
P(Y=\varnothing\mid X=i)
=
e^{-\gamma T_L},
```

```math
P(Y=i\mid X=i)
=
1-e^{-\gamma T_L}.
```

従って理想capture kernelは入力分布を係数 $1-e^{-\gamma T_L}$ で通常結果へ写し、残りを正式な無反応へ送る。Markov kernelの全変動縮約性と三角不等式から、上流選択誤差 $\varepsilon_{\rm sel}$ とpointer実装誤差 $\varepsilon_{\rm ptr}$ を加えてR170の上界を得る。吸収後の記録はデータ処理であり、結果重みを変更しない。

## K.6 境界と強化結果

新R162はQ3の移動過程に対する採用開放ミクロ方程式であり、有限閉鎖Hamiltonian実装を主張しない。Q1/Q2の静的平方根率の物理実現はR190の作用保存Drude混合と対称作用開口を正本とし、反復renewalはR179のstationary incoming bathを使う。

旧R162の有限衝突経路持上げ、局所詳細釣合いを持つ有限熱的scatterer、旧R188のpath-TVからNelson加速度への安定性は撤回せず、有限閉鎖実装を検査する強化結果として論文外メモへ保存する。有限浴化、完全周期の仕事・熱・エントロピー収支も中心定理の必要条件にしない。
