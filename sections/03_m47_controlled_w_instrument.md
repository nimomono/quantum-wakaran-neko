@number: 3
@chapter: 本文
@title: M47のHopf準備・条件付きGibbs再平衡化・傾斜測定
@status: Q1を、M50の2成分特殊化として2モード信号bath、条件付き作用殻、有限衝突熱浴、粒子位置の交互行程へ再編する。R164がBorn型状態数と条件付き中間状態有効自由エネルギーの起源を与える。達成判定は変更しない。

## 3.1 Q1の統計力学的再編と主張範囲

本章は、Q1のM47を統計力学的な操作周期として再編する。基本状態は、W型ポテンシャル中で各試行に1つ存在する粒子位置 $X$ と、2モード信号bath座標 $Z$ を持つ共同測度

```math
\mu(dX\,dZ)
```

である。複素振幅を独立した実在場として先に置かず、規格化共分散

```math
C_Z
=
\frac{\mathbb E_\mu[ZZ^\dagger]}
{\mathbb E_\mu[Z^\dagger Z]}
```

が階数1の場合にだけ、その因子 $c$ を統計的rayとして使う。付録M.2の階数1共分散の支持補題により、単一試行の実現値 $z=Z(\omega)$ は $z=\alpha(\omega)c$ とほとんど確実に書ける。M50と局所制御器が入力するのは $c$ または $C_Z$ でなく、この単一試行の $z$ である。粒子位置の分布と共分散の空間核を一致させる旧条件は、付録IのM47 matching条件である。本章ではmatchingを全時刻で保存しない。Hamiltonian制御中は粒子位置が瞬時の信号bath方向から外れてよく、各操作面で付録Lの有限衝突熱浴を接続して条件付きGibbs分布へ戻す。

Q1の測定は次の仕事行程、熱化行程、記録行程へ分ける。

1. R145のHopf駆動で2モード信号bath方向を準備する。
2. 信号bath方向を保持し、R164の作用枝容量と条件付き作用殻fiberを準備する。
3. R161、R162で粒子位置を条件付きGibbs分布へ近づける。
4. 衝突熱浴を切り、W型2モードの傾斜制御で測定軸の固有方向を左右局在方向へ写す。
5. 分析器終了後に作用殻fiberを更新し、再び衝突熱浴を有限時間だけ接続して新しい信号bath方向へ粒子位置を再平衡化する。
6. 入射セルと辺遷移を止め、トンネル振動より速く、高モード間隔より遅く傾斜を立ち上げる。
7. 左右井戸の有効自由エネルギー差と閉じた辺ゲートで、既存の粒子位置を記録終了まで片側へ保持する。
8. 各井戸に置いた局所記録ポインターが、その場所にある $X$ だけを記録する。
9. 安全枝では、記録結果に対応する準備済み2モードテンプレートと信号bathを正準交換し、交換後方向へ作用殻準備と粒子位置再平衡化を行う。
10. 測定前情報と使用済み装置状態を外部セルへ残し、内部補助を逆計算と交換resetで戻す。

局所記録は、$C_Z$、統計振幅、全密度、確率流、遷移率を入力にしない。従って、物理的複素場のcurrentから全時刻位置率を作る

```math
b
\longrightarrow
q(b)
\longrightarrow
X
```

という因果律を使わない。

付録IのR145は、雑音零の採用開放Hopf方程式について信号bath方向を目標位相円へ吸引する厳密解と有限時間率を与える。付録M.2は階数1共分散の統計因子を単一試行信号の支持へ接続し、M50/R164は同じ試行の有限信号作用を正則化枝容量へ写し、各排他的枝の2作用殻状態数からBorn型条件付き重みと有効自由エネルギーを導く。付録LのR161は任意有限信号方向に対する粒子位置の一様指数再平衡化、R162はその局所詳細釣合い率の有限衝突実現、R163は制御切替と粒子位置経路のゆらぎ関係を与える。R145、支持補題、R164、R161を順に使えば、信号bath方向、条件付き状態数、粒子位置分布を同じ操作面へ有限誤差で準備できる。

第5章のR152は、固定singlet型Bell装置に限って同じ平方根率を先に採用した結果である。R161はその数学的核を任意のM47 rayへ拡張し、R162は固定した単一試行信号bath座標に対する衝突熱浴実現を与える。R164は各翼の局所条件付き地形にも使えるが、paired-Hopf準備や2翼周期全体を導かない。R152を一般Q1定理として遡及的に読み替えず、R161--R164をQ1の新しい根拠とする。

R164により、条件付き地形 $E_i^\delta=-\Theta\log\pi_i^\delta$ は確率から直接設計する量でなく、作用殻を消去した条件付き中間状態有効自由エネルギーとして得られる。作用殻明示表示の $\Omega_i^\delta$ と消去表示の $e^{-\beta E_i^\delta}$ を同じ分配関数で掛けず、状態数を二重計数しない。ただし枝容量結合、殻内平衡化、枝対称性、信号bath保持反作用を同じ有限局所Hamiltonianへ統合しておらず、Hopf pump、記録、resetを含む周期全体の仕事・熱・エントロピー収支も未閉鎖である。このためQ1-2とQ1-3の判定は部分達成のまま維持する。

## 3.2 階数1共分散とBloch球

Pauli行列を $\sigma_x,\sigma_y,\sigma_z$ とし、共分散のBloch成分を

```math
r_k
=
\operatorname{tr}(C_Z\sigma_k)
```

で定める。$C_Z$ はHermitian、正半定値、trace 1なので

```math
C_Z
=
\frac12
\left(
I_2+\boldsymbol r\cdot\boldsymbol\sigma
\right),
\qquad
|\boldsymbol r|\leq1
```

である。階数1なら $C_Z=cc^\dagger$、$c^\dagger c=1$ と書け、$|\boldsymbol r|=1$ である。$c$ と $e^{i\alpha}c$ は同じ $C_Z$ を与えるため、共通位相は観測状態に含まれない。

一般のHermitian行列 $G(t)$ に対して、古典2モードHamiltonianを

```math
H_G(t)
=
Z^\dagger G(t)Z
```

とする。正準方程式は

```math
i\mathcal J_0\dot Z
=
G(t)Z
```

であり、規格化共分散は

```math
i\mathcal J_0\dot C_Z
=
[G(t),C_Z]
```

に従う。

<!-- theorem-start:proposition -->
**命題（R139：M47階数1共分散のBloch縮約）**

trace 1の正半定値2次共分散について、階数1条件は $|\boldsymbol r|=1$ と同値である。階数1共分散の集合は共通位相を除いた $\mathbb{CP}^1\simeq S^2$ であり、$H_G$ の古典正準流はこの球面上の回転を与える。従ってM47の純粋2モード統計状態は、独立した複素振幅場を仮定せずBloch球を持つ。
<!-- theorem-end:proposition -->

R139はR135を一般の時間依存2モード生成子へ拡張したものである。共分散の回転は厳密だが、粒子位置周辺のmatching保存は別の条件である。

## 3.3 W型ポテンシャルと局在基底

対称W型生成子 $h_W(0)$ の最低2固有モードを、実偶関数 $\phi_0$ と実奇関数 $\phi_1$ とする。固有値を $E_0<E_1$、平均と半分裂を

```math
\overline E
=
\frac{E_0+E_1}{2},
\qquad
J
=
\frac{E_1-E_0}{2}
```

とする。位相規約を選び、左右局在基底を

```math
|L\rangle
=
\frac{\phi_0+\phi_1}{\sqrt2},
\qquad
|R\rangle
=
\frac{\phi_0-\phi_1}{\sqrt2}
```

と置く。左右の名称は $\langle L|x|L\rangle<\langle R|x|R\rangle$ となるように必要なら $\phi_1$ の符号を反転する。

制御可能な1次傾斜を

```math
h_W(F)
=
h_W(0)-F(t)x
```

とする。対称性から最低2モード内では対角位置要素が消え、局在基底での生成子は共通エネルギーを除いて

```math
G_F(t)
=
-J\sigma_x
+
\frac{\varepsilon(t)}{2}\sigma_z,
\qquad
\varepsilon(t)
=
2F(t)
\left|
\langle\phi_0|x|\phi_1\rangle
\right|
```

となる。$-J\sigma_x$ は左右トンネル振動、$\varepsilon\sigma_z/2$ は左右エネルギー差である。

## 3.4 傾斜制御による任意のSU(2)操作

傾斜を零にした区間は $\sigma_x$ 回転を与える。零でない一定傾斜は、$x$ 軸と平行でない $xz$ 平面内の軸回転を与える。2本の非平行回転軸の有限積は $SU(2)$ 全体を生成する。Lie代数では

```math
[\sigma_x,\sigma_z]
=
-2i\sigma_y
```

なので、$\sigma_x$ と $\sigma_z$ から3方向が閉じる。

一定傾斜 $\varepsilon$ で $|L\rangle$ から開始したとき、右井戸方向への2モード作用比は

```math
P_{L\to R}(t)
=
\frac{4J^2}{\varepsilon^2+4J^2}
\sin^2
\left(
\frac{\sqrt{\varepsilon^2+4J^2}}{2\mathcal J_0}t
\right).
```

この式は、共鳴 $\varepsilon=0$ での完全振動、離調による振幅低下、振動数の変化を同じ担体で与える。

<!-- theorem-start:theorem -->
**定理（R140：W型傾斜制御による2モード可制御性）**

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はunitary共役であり、trace、正値性、階数を保存する。一定傾斜の左右遷移は上の離調公式に従う。
<!-- theorem-end:theorem -->

R140は制御された2モード生成子についての厳密結果である。元の全W型系で同じ精度を得るには、高モード漏れと傾斜切替誤差を別に評価する。

## 3.5 2モード窓と傾斜切替の尺度階層

第3固有値を $E_2$ とし、最低2モードと高モードの間隔を

```math
G
=
E_2-E_1
```

とする。測定傾斜 $\varepsilon_m$ と切替時間 $\tau_q$ は

```math
J
\ll
|\varepsilon_m|
\ll
G,
```

```math
\frac{\mathcal J_0}{G}
\ll
\tau_q
\ll
\frac{\mathcal J_0}{J}
```

を満たすように選ぶ。時間尺度の右側 $\tau_q\ll\mathcal J_0/J$ はトンネル振動に対して急な切替、左側 $\mathcal J_0/G\ll\tau_q$ は高モードgapに対して遅い切替を表す。エネルギー尺度 $J\ll|\varepsilon_m|\ll G$ は、離調固定を強くしながら最低2モード窓を保つ条件である。

固定した有限格子W型族では、傾斜演算子の行列要素と時間微分が有界なら、2モード外漏れを

```math
\varepsilon_{2m}
\leq
C_W
\left[
\left(
\frac{|\varepsilon_m|}{G}
\right)^2
+
\left(
\frac{\mathcal J_0}{G\tau_q}
\right)^2
\right]
```

の形で抑えられる。$C_W$ は採用した有限W型族と切替形状に依存する。これは連続空間の一様上界ではない。

深いW型族で $J/G\to0$ なら、例えば

```math
|\varepsilon_m|
=
\sqrt{JG},
\qquad
\tau_q
=
\frac{\mathcal J_0}{\sqrt{JG}}
```

と選べる。このとき4つの比

```math
\frac{J}{|\varepsilon_m|},
\quad
\frac{|\varepsilon_m|}{G},
\quad
\frac{\mathcal J_0}{G\tau_q},
\quad
\frac{J\tau_q}{\mathcal J_0}
```

は全て $\sqrt{J/G}$ の次数で零へ近づく。

## 3.6 条件付き作用殻、状態数、有効自由エネルギー

有限W型配置グラフを $G_W=(V_W,E_W)$、最低2モード埋込みを $\Phi$ とする。単一試行の信号bath座標 $z\neq0$ に対し、総信号作用、枝信号作用、正則化枝容量を

```math
J_{\rm sig}(z)
=
\mathcal J_0z^\dagger z,
\qquad
J_i(z)
=
\mathcal J_0|(\Phi z)_i|^2,
```

```math
A_i^\delta(z)
=
J_i(z)
+
\delta q_iJ_{\rm sig}(z)
```

とする。$q_i>0$、$\sum_iq_i=1$ は固定背景作用の枝配分、$\delta>0$ は有限装置の背景容量である。$\Phi^\dagger\Phi=I_2$ から

```math
\sum_iA_i^\delta(z)
=
(1+\delta)J_{\rm sig}(z)
```

となる。

各位置枝 $i$ に、非負作用 $K_i,I_i$ と2つの角を持つ排他的fiberを置き、$K_i+I_i=A_i^\delta(z)$ の作用殻を同じLiouville規約で数える。作用基準を $J_{\rm ref}$ とすれば、付録Mで

```math
\Omega_i^\delta(z)
=
\frac{(2\pi)^2}{J_{\rm ref}}
A_i^\delta(z)
```

を得る。

<!-- theorem-start:theorem -->
**定理（R164：有限信号作用のBorn型殻状態数）**

$\Phi^\dagger\Phi=I_2$、$z\neq0$、$q_i>0$、$\sum_iq_i=1$、$\delta>0$ とする。各排他的枝を同じ2作用殻Liouville母測度で数えると、規格化状態数は

```math
\begin{aligned}
\frac{\Omega_i^\delta(z)}
{\sum_j\Omega_j^\delta(z)}
&=
\frac{
|(\Phi z)_i|^2/(z^\dagger z)
+
\delta q_i
}{1+\delta}\\
&=:
\pi_i^\delta(z).
\end{aligned}
```

作用殻fiberの枝自由エネルギーを $F_i^{\rm sh}=-\Theta\log\Omega_i^\delta$、全枝基準を $F_{\rm eq}^{\rm sh}=-\Theta\log\sum_j\Omega_j^\delta$ とすれば

```math
E_i^\delta(z)
=
F_i^{\rm sh}(z)-F_{\rm eq}^{\rm sh}(z)
=
-\Theta\log\pi_i^\delta(z).
```

従ってBorn型条件付き重みとR161の有効自由エネルギーは、確率を枝容量へ書き込まず、信号作用のmode分解と2作用殻の状態数から得られる。
<!-- theorem-end:theorem -->

R164の証明、一般 $n$ 作用殻、作用分配次元の剛性、共通流束、有限幅拘束は付録Mに置く。直接作用を受け取る明反応方向が $q$ 本なら $\Omega\propto A^q$ なので、Born型線形則を全容量族で保つのは $q=1$ だけである。有限剛性 $\kappa$ の滑らかな作用殻は有限幅誤差を持ち、$\delta\downarrow0$ で一様精度を保つには必要条件として $\kappa=\Omega(\delta^{-2})$ であり、$\Theta(\delta^{-2})$ は代表的な選択である。

$E_i^\delta$ は裸の粒子位置エネルギーでなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。任意の粒子位置分布 $p$ に対して

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

となる。従ってrematchingを、抽象多様体への射影でなく有効自由エネルギーの緩和として扱える。ただしR164は作用容量結合、fiber内平衡化、枝対称性をM47周期の有限局所Hamiltonianから導かない。

## 3.7 任意の信号bath方向に対する粒子位置再平衡化

有限連結W型グラフの各辺 $i\sim j$ に $a_{ij}=a_{ji}>0$ を置き、

```math
k_{i\to j}^\delta(z)
=
\kappa_Xa_{ij}
\sqrt{
\frac{\pi_j^\delta(z)}{\pi_i^\delta(z)}
}
```

とする。これは単一試行の $z$ に条件付けた粒子位置応答であり、物理的複素場からcurrent rateを作る因果律ではない。

<!-- theorem-start:theorem -->
**定理（R161：任意の有限信号方向に対する粒子位置再平衡化）**

```math
q_{\min}=\min_iq_i,
\qquad
a_{\min}=\min_{i\sim j}a_{ij},
\qquad
m_\delta=\frac{\delta q_{\min}}{1+\delta}
```

とする。無重みW型グラフLaplacianの第1非零固有値を $\lambda_G$ とすれば、任意の $z\neq0$ に対して $\pi^\delta(z)$ は唯一の定常分布であり、全初期粒子位置分布から

```math
D_{\rm TV}
\left(
\operatorname{Law}(X_T\mid z),
\pi^\delta(z)
\right)
\leq
C_\delta e^{-\lambda_\delta T}
```

で収束する。ここで一様に

```math
\lambda_\delta
\geq
\kappa_Xa_{\min}m_\delta\lambda_G,
\qquad
C_\delta
=
\frac12\sqrt{m_\delta^{-1}-1}
```

と選べる。目標分布は共通位相と全振幅に不変であり、理想W型対角との差は

```math
D_{\rm TV}
\left(
\pi^\delta(z),
w(z)
\right)
\leq
\frac{\delta}{1+\delta}
```

である。
<!-- theorem-end:theorem -->

証明は付録Lに置く。R152は固定Bell装置の有限設定族について同じ平方根率を採用した先行結果である。R161は全M47 rayへ拡張し、$q_{\min}$、$a_{\min}$、$\lambda_G$ による明示的一様下界を与える。

$\delta=0$ で目標占有が零となる頂点がグラフの切断点なら、詳細釣合いは正占有頂点からそのnodeへの流入を零にする。従って局所隣接率だけで全初期状態を任意の理想rayへ一様再平衡化することはできない。有限M47では $\delta>0$ を採用し、正則化誤差と資源増大を台帳へ残す。

## 3.8 有限衝突熱浴と局所詳細釣合い

R164の粒子位置有効自由エネルギーに対して、辺の対称障壁を

```math
B_{ij}^\delta(z)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(z)+E_j^\delta(z)
\right]
```

とする。衝突面へ実際に到着するセルの運動エネルギー分布を

```math
f_{\rm in}(\epsilon)
=
\beta e^{-\beta\epsilon},
\qquad
\beta=\Theta^{-1}
```

とし、$\epsilon\geq B_{ij}^\delta-E_i^\delta$ の場合だけ辺を通す。通過後のセルエネルギーは

```math
\epsilon'
=
\epsilon
+
E_i^\delta
-
E_j^\delta
```

とするので、粗視化された粒子位置有効自由エネルギーとセルエネルギーの和は保存される。作用殻fiberを含む全微視的エネルギー保存は、fiberを明示したprotocolを構成するまで主張しない。

<!-- theorem-start:theorem -->
**定理（R162：局所詳細釣合い率の有限衝突熱浴実現）**

辺衝突流束を $\nu_{ij}=\nu_{ji}$ とする。入射位置、到着時計、運動方向、反射枝、出射エネルギー、履歴セルを完全状態へ含めると、正逆衝突を一対一に対応させる有限Hamiltonian散乱を構成できる。縮約粒子位置率は

```math
k_{i\to j}^{\rm coll}(z)
=
\nu_{ij}e^{-\beta B_{ij}^0}
\sqrt{
\frac{\pi_j^\delta(z)}{\pi_i^\delta(z)}
}
```

となる。$\nu_{ij}e^{-\beta B_{ij}^0}=\kappa_Xa_{ij}$ と校正すればR161に一致する。固定観測時間、各辺の有限セル数、有限エネルギー切断では、理想経路測度との差をoverflow、エネルギー尾部、閾値平滑化、時計、信号bath保持の誤差和で抑えられる。超過セルと比較境界は無反応結果へ含める。
<!-- theorem-end:theorem -->

記録前には入射セルを止め、辺ゲートを閉じる。これによりR143が仮定していた単一試行の局所滞在失敗率を、障壁裾、エネルギー尾部、時計ずれの和として評価できる。固定有限個のセルで無期限のMarkov浴を実現するとは主張せず、反復にはfresh cell流を使う。

## 3.9 解析器quenchとゆらぎ関係

単一試行信号 $z_t$ を外部制御写像により動かす。作用殻を消去した条件付き中間状態の相対有効仕事と相対有効熱を

```math
W^{\rm rel}
=
\int_0^T
\dot E_{X_t}^\delta(z_t)
\,dt,
```

```math
Q^{\rm rel}
=
\sum_{\ell}
\left[
E_{i_\ell}^\delta(z_{t_\ell})
-
E_{i_{\ell-1}}^\delta(z_{t_\ell})
\right]
```

とすれば、各粗視化経路で $\Delta E=W^{\rm rel}+Q^{\rm rel}$ である。

<!-- theorem-start:theorem -->
**定理（R163：信号切替と粒子位置の経路ゆらぎ関係）**

R161またはR162の正逆protocolについて、経路エントロピー生成 $\Sigma$ は

```math
\frac{\mathcal P_F[\omega]}
{\mathcal P_R[\omega^\dagger]}
=
e^{\Sigma[\omega]},
\qquad
\left\langle e^{-\Sigma}\right\rangle_F
=1,
\qquad
\langle\Sigma\rangle_F
\geq0
```

を満たす。単一試行信号 $z^-$ から $z^+$ への瞬間quenchでは

```math
W_i^{\rm eff}
=
\Theta
\log
\frac{\pi_i^\delta(z^-)}
{\pi_i^\delta(z^+)},
```

```math
\left\langle e^{-\beta W^{\rm rel}}\right\rangle
=1,
\qquad
\langle W^{\rm rel}\rangle
=
\Theta
D_{\rm KL}
\left(
\pi^\delta(z^-)
\|
\pi^\delta(z^+)
\right)
```

である。作用殻明示表示では $W_i^{\rm sh}=\Delta F_i^{\rm sh}$、作用殻消去表示では $W_i^{\rm rel}=\Delta E_i=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ と区別する。全作用保存unitaryでは共通項が一定になり得るが、pumpまたはresetでは一定とは限らない。
<!-- theorem-end:theorem -->

R163は、局所詳細釣合い率が単に目的分布を不変にするだけでなく、正逆経路確率比と相対有効散逸仕事を固定することを示す。経路確率比と積分ゆらぎ関係は粗視化跳躍過程で厳密だが、$W^{\rm rel}$ を全装置の機械仕事、$Q^{\rm rel}$ を全微視的熱と同一視しない。ゆらぎの定理はR164の地形の下流整合性を検査し、作用殻状態数の線形則を選び出すものではない。Hopf pump、作用殻準備、信号bath保持、傾斜回路、記録、template交換、resetを含む全周期の総収支は別に閉じる必要がある。

## 3.10 傾斜による左右分離固定

分析器操作を終えた直後に傾斜を立ち上げる。2モード射影内では、傾斜保持中の反対側遷移確率は全時刻で

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

を満たす。右から左も同じ上界である。

<!-- theorem-start:theorem -->
**定理（R141：傾斜による左右占有分布の固定）**

最低2モード内の任意の規格化共分散 $C_Z$ について、一定傾斜 $\varepsilon_m$ の保持中の左占有率を $p_L(t)=\operatorname{tr}(|L\rangle\langle L|C_Z(t))$ とする。このとき全時刻で

```math
|p_L(t)-p_L(0)|
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}.
```

特に切替開始時の共分散が $|L\rangle\langle L|$ または $|R\rangle\langle R|$ なら、反対井戸へ移る作用比は $4J^2/(\varepsilon_m^2+4J^2)$ 以下である。一般入力について、2モード内の占有変化と保持中の残留結合を合わせた周辺固定誤差を

```math
\varepsilon_{\rm lock}
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}
+
\varepsilon_{\rm hold}
```

で評価する。全W型系の固定中分布誤差は $\varepsilon_{2m}+\varepsilon_{\rm lock}$ 以下である。$J/G\to0$ の深いW型族では、前節の選択により両者を任意に小さくできる。
<!-- theorem-end:theorem -->

R141が固定するのは信号bathの左右占有周辺であり、一般入力を左右固有状態へ収縮させる結果ではない。周辺固定だけから単一試行の粒子位置 $X$ の経路滞在は従わない。そこで再平衡化終了後にR162の入射セルを止め、辺ゲートを閉じる。記録時間中の離脱失敗率 $\varepsilon_{\rm res}$ は、有限障壁裾、エネルギー切断、閾値平滑化、時計ずれから評価する。どちらの枝にいるかは、ゲート閉鎖前から存在するM47粒子位置を局所的に読む。

## 3.11 任意軸分析器

測定軸を単位ベクトル $\boldsymbol n$、射影を

```math
\Pi_{\boldsymbol n,s}
=
\frac12
\left(
I_2+s\boldsymbol n\cdot\boldsymbol\sigma
\right),
\qquad
s\in\{+1,-1\}
```

とする。R140により、有限傾斜列 $A_{\boldsymbol n}$ を

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,+}
A_{\boldsymbol n}^\dagger
=
|L\rangle\langle L|,
```

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,-}
A_{\boldsymbol n}^\dagger
=
|R\rangle\langle R|
```

となるように選べる。入力共分散を $C_Z$ とすると、理想射影重みは

```math
p_s
=
\operatorname{tr}
\left(
C_Z\Pi_{\boldsymbol n,s}
\right).
```

分析器後の共分散は $C_Z'=A_{\boldsymbol n}CA_{\boldsymbol n}^\dagger$ である。分析器中は粒子位置周辺がこの共分散を追跡しなくてよい。終了後の信号bath方向を固定し、R161の再平衡化を時間 $T_X$ だけ作用させれば、左右井戸の粒子位置頻度が $p_s$ を有限コントラストと有限混合誤差で読む。

## 3.12 左右空間読出しの有限コントラスト

左半空間への位置射影を $\Pi_L$ とし、

```math
B_W
=
\langle\phi_0|\Pi_L|\phi_1\rangle
```

と置く。位相規約で $B_W\geq0$ とする。最低2モード上の左読出し効果は、偶奇基底で

```math
E_L
=
\begin{pmatrix}
1/2&B_W\\
B_W&1/2
\end{pmatrix}
```

である。局在基底では

```math
E_L
=
(1-\eta_W)
|L\rangle\langle L|
+
\eta_W
|R\rangle\langle R|,
\qquad
\eta_W
=
\frac12-B_W.
```

従って $0\leq\eta_W\leq1/2$ である。理想分析器後の左占有率は

```math
P_L
=
\eta_W
+
(1-2\eta_W)p_+,
```

なので

```math
|P_L-p_+|
\leq
\eta_W.
```

<!-- theorem-start:proposition -->
**命題（R142：W型左右読出しのBorn型有限誤差）**

分析器終了後にR164の作用殻準備とR161、R162の粒子位置再平衡化を時間 $T_X$ だけ作用させ、その誤差を $\varepsilon_{\rm eq}$ とする。左、右の粒子位置読出しは、任意軸射影重み $p_+,p_-$ から各成分で高々 $\eta_W+\varepsilon_{\rm eq}$ ずれた2値分布を持つ。有限の分析器、傾斜切替、固定、局所記録、境界無反応を加えた結果分布 $p^{\rm obs}$ は、無反応質量を零とした理想分布 $p^{\rm id}$ に対して

```math
D_{\rm TV}
\left(
p^{\rm obs},p^{\rm id}
\right)
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm eq}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
```

を満たす。
<!-- theorem-end:proposition -->

有限障壁で $\eta_W$ は一般に零でない。従って生の左右位置読出しを有限パラメータで厳密な射影測定とは呼ばない。深いW型族で $\eta_W\to0$ となる場合に、任意精度極限を持つ非鋭い測定として扱う。

## 3.13 枝別条件付きGibbs整合

測定記録を $R\in\{L,R,\varnothing\}$ とする。安全枝 $s\in\{L,R\}$ の非規格化共分散を

```math
\widetilde C_s
=
\frac{
\mathbb E
\left[
\mathbf1_{R=s}ZZ^\dagger
\right]
}{
\mathbb E[Z^\dagger Z]
}
```

とする。$p_s=\operatorname{tr}\widetilde C_s>0$ なら条件付き共分散は

```math
C_s
=
\frac{\widetilde C_s}{p_s}
```

である。理想測定操作が必要とする枝別条件は

```math
\widetilde C_s^{\rm out}
\simeq
p_s|s\rangle\langle s|,
\qquad
C_s^{\rm out}
\simeq
|s\rangle\langle s|
```

である。

入力の大域共分散が階数1であることは、この枝別条件を意味しない。結果で条件付けるだけでは、同じ $C_Z$ を2つの異なる射影へ変えられない。測定操作には、粒子位置と信号bathを結果依存に相関させる物理段階が必要である。本章では、井戸ごとに置いた局所記録、準備済みテンプレートの正準交換、交換後方向に対するR161の再平衡化をこの段階として使う。

## 3.14 粒子位置の局所記録

左右井戸の内部に滑らかな検出関数 $\chi_L(X)$、$\chi_R(X)$ を置く。安全な左領域では $(\chi_L,\chi_R)=(1,0)$、安全な右領域では $(0,1)$ とし、分離面近傍を無反応領域とする。2つの記録セルを $(Q_s^R,P_s^R)$ とし、記録Hamiltonianを

```math
H_{\rm rec}(t)
=
g_{\rm rec}(t)
\sum_{s=L,R}
P_s^R\chi_s(X)
```

とする。単位面積パルスでは

```math
Q_s^R
\longmapsto
Q_s^R+\chi_s(X).
```

理想空セルで $P_s^R=0$ なら、記録中の $X$ への反作用は零である。有限準備幅は $\varepsilon_{\rm rec}$ に入れる。$\chi_s$ は各井戸の局所位置だけを読むため、記録装置は統計振幅、共分散、全密度、確率流を参照しない。

傾斜保持時間 $T_{\rm rec}$ は、局所ポインターが安全域を分離できる長さとする。R141により保持中の信号bath左右占有変化を $\varepsilon_{\rm lock}$ に抑える。R162により、再平衡化終了後の入射停止と辺ゲート閉鎖から、単一試行の経路滞在失敗を $\varepsilon_{\rm res}$ に抑える。分離面を通過中の試行、ゲート閉鎖失敗、有限閾値帯は無反応として記録し、除外後の2値再規格化を行わない。

## 3.15 結果枝ごとの状態更新と再平衡化

左右井戸に、規格化共分散がそれぞれ

```math
C_L^{\rm tpl}
=
|L\rangle\langle L|,
\qquad
C_R^{\rm tpl}
=
|R\rangle\langle R|
```

となる2モードテンプレートを準備する。安全枝 $s$ では、$\chi_s(X)$ が開く局所交換結合により、信号浴 $Z$ と対応テンプレート $Z_s^{\rm tpl}$ を角 $\pi/2$ だけ正準回転する。測定前の $Z$ は使用済みテンプレートへ移り、写像全体は1対1のままである。

交換後の装置座標では $C_s^{\rm out}=|s\rangle\langle s|$ である。測定前の論理座標へ戻して表すと

```math
A_{\boldsymbol n}^\dagger
C_s^{\rm out}
A_{\boldsymbol n}
=
\Pi_{\boldsymbol n,s}
```

となる。R162の辺閉鎖条件の下で、粒子位置 $X$ は記録終了まで同じ安全井戸へ保持される。記録後に辺を開き、交換後テンプレート方向を固定してR161を時間 $T_{X,\rm post}$ だけ作用させる。これにより条件付き出力配置は $\pi^\delta(s)$ へ戻り、枝別配置--信号bath整合誤差は有限混合誤差、正則化誤差、有限障壁の反対井戸裾 $\eta_W$ の和で評価できる。

## 3.16 有限誤差instrument定理

1回の粒子位置再平衡化誤差をM50の共通台帳として

```math
\begin{aligned}
\varepsilon_{\rm eq}
=\varepsilon_{M50}
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

とする。$\varepsilon_{\rm mix}=C_\delta e^{-\lambda_\delta T_X}$、$\varepsilon_\delta=\delta/(1+\delta)$ と選べる。各項は作用容量結合、有限幅拘束、枝対称性、殻内準備、正則化、有限混合、有限衝突実現、信号bath保持を表し、同じ偏差を2項へ重複して入れない。

<!-- theorem-start:theorem -->
**定理（R143：M47粒子位置を傾斜で固定し局所記録する有限誤差instrument）**

固定した入力純粋共分散、測定軸 $\boldsymbol n$、有限観測時間について、次を仮定する。

1. R145で信号bath方向を有限誤差 $\varepsilon_{\rm Hopf}$ 以内に準備し、R164の条件付き作用殻準備とR161、R162の初期再平衡化を $\varepsilon_{\rm eq}$ 以内で実行できる。
2. 衝突熱浴を切った後、R140の傾斜列を2モード制御誤差 $\varepsilon_{\rm ctrl}$ 以下で実装し、終了方向に対する再平衡化を同じ $\varepsilon_{\rm eq}$ 以内で実行できる。
3. R141の尺度階層により信号bath左右占有の変化を $\varepsilon_{\rm lock}$ 以下にでき、R162の入射停止と辺ゲート閉鎖により、記録終了前に粒子位置 $X$ が安全井戸を離れる確率を $\varepsilon_{\rm res}$ 以下にできる。
4. 安全枝で局所記録と結果別テンプレート交換を実行し、枝別交換誤差を $\varepsilon_{\rm br}$ 以下、交換後の条件付き再平衡化誤差を $\varepsilon_{\rm post}$ 以下にできる。
5. 分離面、閾値平滑化帯、セルoverflowを正式な無反応結果とし、その全質量を $\varepsilon_{\rm guard}$ 以下にできる。

このとき結果集合 $\{+1,-1,\varnothing\}$ を持つ、有限正準制御と有限セル弱開放粒子位置bathからなる装置を構成でき、無反応質量を零とした理想Born分布との全変動距離は

```math
\varepsilon_{\rm inst}
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm Hopf}
+
2\varepsilon_{\rm eq}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm br}
+
\varepsilon_{\rm post}
```

で抑えられる。安全結果 $s$ の条件付き出力共分散は、分析器座標で $|s\rangle\langle s|$ からtrace距離 $\varepsilon_{\rm br}+O(\eta_W)$ 以内であり、条件付き出力配置は $\pi^\delta(s)$ から $\varepsilon_{\rm post}$ 以内である。記録は粒子位置 $X$ の局所関数だけを入力にし、全密度、確率流、current transducerを使わない。
<!-- theorem-end:theorem -->

R143はR137の全時刻matching保存を仮定しない。分析器操作で配置--信号bath整合が崩れることを許し、操作面ごとにR164の作用殻準備とR161の再平衡化で回復する。記録中の経路滞在もR162の入射停止と辺ゲート閉鎖へ置き換えた。一方、作用容量結合とfiber内平衡化を含む最小Hamiltonian、信号bath保持controllerの完全な反作用、Hopf準備からresetまでの総収支はR143から従わない。

## 3.17 同軸反復と異軸逐次測定

第1測定軸を $\boldsymbol n$ とし、安全結果 $s$ を得た後、装置座標の出力共分散は $|s\rangle\langle s|$ に近い。同じ軸を再測定する場合は同じ左右基底を読むため、反対結果の確率は理想的には零で、有限装置では条件付き状態誤差と第2段誤差の和で抑えられる。

第2軸を $\boldsymbol m$ とする。第1分析器の出力座標から第2分析器へ進む制御を

```math
A_{\boldsymbol m}
A_{\boldsymbol n}^\dagger
```

とすれば、理想条件付き分布は

```math
P(t\mid s)
=
\operatorname{tr}
\left(
\Pi_{\boldsymbol m,t}
\Pi_{\boldsymbol n,s}
\right)
=
\frac12
\left(
1+st\boldsymbol n\cdot\boldsymbol m
\right).
```

2段の実分布と理想逐次分布の全変動距離は、逐次結合により各段の $\varepsilon_{\rm inst}$ と第1段条件付き状態誤差の和で抑えられる。各段は独立な記録セルとテンプレートを使う。無反応試行は結果空間に残す。

## 3.18 永久記録、逆計算、交換reset

外部記録セルは前節の局所剪断で結果を保持する。記録後、分析器時計、傾斜制御器、局所比較器の補助自由度を逆順に戻す。測定前浴情報は使用済みテンプレートにあり、外部記録は逆実行しないため、内部補助だけを戻しても正準可逆性は破れない。

周期末の装置偏差 $\delta a$ を、流入する空セル $\eta_n$ と交換角 $\phi$ で回転すると

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta_n.
```

1周期の逆計算残差を $\varepsilon_{\rm cyc}$、空セル幅を $\|\eta_n\|\leq\sigma_E$ とすれば

```math
\limsup_{n\to\infty}
\|\delta a_n\|
\leq
\frac{
\varepsilon_{\rm cyc}
+
|\sin\phi|\sigma_E
}{
1-|\cos\phi|
}
```

である。旧状態は使用済み外部セルへ移る。永久記録と旧状態を有限閉鎖系の固定容量へ無期限に蓄積するとは主張しない。

## 3.19 条件付き完全周期

<!-- theorem-start:theorem -->
**定理（R144：M47傾斜測定の固定有限弱開放周期）**

固定純粋入力、固定された有限個の傾斜制御、固定された2つの測定軸、任意の有限周期数について、R143の5条件が各段と各周期で一様に成立するとする。Hopf方向準備、条件付きGibbs再平衡化、任意軸操作、再平衡化、辺閉鎖、傾斜分離固定、局所記録、枝別テンプレート交換、測定後再平衡化、2段逐次測定、永久記録、内部逆計算、外部fresh-cell交換からなる有限正準・弱開放構成を選べる。無反応を含む結果分布誤差は各段の $\varepsilon_{\rm inst}$ の和、周期末偏差は逆計算とresetの上界で抑えられる。能動装置の自由度は固定有限であり、永久記録、衝突セル、使用済み状態のセル数は周期数に比例する。
<!-- theorem-end:theorem -->

R144は全時刻のmatching保存または周期間matching帰還を仮定しない。各操作面でR164の作用殻準備とR161、R162を有限時間だけ作用させる。一方、Hopf pump、作用殻fiber、信号bath保持controller、衝突セル準備、記録、template交換、resetを含む総仕事、総熱、総エントロピー生成を一つの恒等式へ閉じていない。このためQ1-3の完全達成定理ではない。

## 3.20 誤差・熱力学・資源台帳

Q1測定の中心誤差を

```math
\varepsilon_{Q1}
=
\varepsilon_{\rm prep}
+
2\varepsilon_{\rm eq}
+
\varepsilon_{2m}
+
\varepsilon_{\rm ctrl}
+
\eta_W
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm br}
+
\varepsilon_{\rm post}
+
\varepsilon_{\rm ret}
```

とする。$\varepsilon_{\rm eq}$ はR164の作用殻準備、有限時間混合、正則化、有限衝突セル、信号bath保持を含む。$\varepsilon_{\rm lock}$ は信号bath左右占有の変化、$\varepsilon_{\rm res}$ は辺ゲート閉鎖後の単一試行経路離脱であり、同じ量ではない。状態方向誤差、結果分布の全変動距離、記録ポインター誤差、周期末正準座標偏差は単位が異なるため、付録Bで対応するLipschitz定数を通してから合成する。

準備誤差はさらに

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm phase}
```

と分ける。R145は $\varepsilon_{\rm Hopf}$ の信号bath方向部分を有限準備時間で抑える。条件付き作用殻状態数、粒子位置周辺、条件付き粒子位置分布はR164、R161、R162の後段準備・再平衡化へ移し、R145単独の誤差へ入れない。零seedと位相基準の失敗は独立に完全結果集合へ残す。

熱力学台帳では、信号bath方向を変える解析器仕事 $W_{\rm ctrl}$、作用枝容量と作用殻拘束を切り替える殻自由エネルギー仕事 $W_{\rm sh}$、作用殻消去表示の相対有効仕事 $W_{\rm q}^{\rm rel}$、相対有効熱 $Q_X^{\rm rel}$、Hopf pump仕事 $W_{\rm Hopf}$、記録・template交換・reset仕事を分ける。R163は条件付き中間状態について

```math
\Delta E_X^{\rm rel}
=
W_{\rm q}^{\rm rel}
+
Q_X^{\rm rel}
```

と経路エントロピー生成を与える。$W_i^{\rm rel}=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ であり、全作用保存unitaryでは共通項が一定になり得るが、pumpとresetでは一定とは限らない。この式だけで $W_{\rm sh}$、殻内散逸、controller反作用を含む全微視的仕事・熱を同定しない。周期全体について

```math
\Delta E_{\rm total}
=0
```

となる外部セル込みの収支と、記録情報、使用済みセル、Hopf散逸を含む総エントロピー生成は未閉鎖である。

1段の能動装置は、信号2モード、条件付き作用殻fiber、容量controller、条件付き障壁controller、有限衝突セル、辺ゲート、左右テンプレート、左右記録セル、傾斜制御、時計、粒子位置の局所検出部からなる。固定段数と固定観測時間では有限自由度である。正準対の最小数は評価しない。$K$ 周期の永久記録、衝突履歴、使用済みテンプレート保存は $O(K)$ 以上、固定有限段の制御時間は傾斜パルス数、fiber準備時間、再平衡化時間に比例する。

$\delta\downarrow0$ では有効自由エネルギー幅が $O(\!\log\delta^{-1})$、必要衝突流束が少なくとも $\Omega(\!\delta^{-1/2})$、R161の一般混合率下界は $O(\!\delta)$ まで低下し得る。R164の滑らかな有限幅作用殻を一様精度で保つ剛性には $\Omega(\!\delta^{-2})$ が必要で、$\Theta(\!\delta^{-2})$ は代表的な選択である。有限資源のまま全bath方向の厳密nodeを追跡するとは主張しない。

深いW型極限は測定コントラストと固定誤差を小さくする一方、トンネル分裂 $J$ を小さくする。零傾斜の $x$ 回転時間は $O(\mathcal J_0/J)$ なので、精度を高めるほど任意軸操作が遅くなる可能性がある。この精度--時間交換は資源台帳から除外しない。

## 3.21 Q1の達成判定とZeno凍結

本章による現在地は次である。

| 目標 | 現在地 | 根拠 | 残る条件 |
|---|---|---|---|
| Q1-1 | 達成 | R139、R140 | 全W型制御は有限2モード誤差。精度--時間交換を持つ |
| Q1-2 | 部分達成 | R141--R145、R161--R164 | Born型状態数と有効自由エネルギーの条件付き起源を導出。作用容量結合、fiber内平衡化、枝対称性、信号bath反作用の有限局所Hamiltonian統合が残る |
| Q1-3 | 部分達成 | R143--R145、R161--R164 | 連続matching保存は不要化。Hopf pump、fiber、controller、記録、resetを含む周期総収支が残る |
| Q1-4 | 未達（凍結中） | — | 判定基準を保持し、反復測定の新規構成・証明・検証を凍結 |

Q1-4の固定目標は削除しない。旧M38の有限Zeno結果は、置換済み連続位置模型に依存する結果としてGit履歴と研究メモへ保存する。M47の傾斜固定は測定保持の一部であり、反復測定間隔に応じたZeno抑制の導出ではない。傾斜でHamiltonianを離調させて遷移を抑える現象をZeno効果と呼ばない。

## 3.22 非主張

本章は次を主張しない。

1. 大域階数1共分散だけから枝別測定後状態が自動的に生じること。
2. M45または具体的回路からR145の採用方程式を導出したこと。
3. R164の枝容量結合、作用殻fiber内平衡化、枝対称性がW型装置の有限局所Hamiltonianから自動的に発生すること。
4. 有効地形仕事・熱がfiberとcontrollerを含む全微視的仕事・熱に等しいこと。
5. 信号bath保持controllerへの反作用が厳密に零であること。
6. 全時刻の配置--信号bath matching保存。改訂後の周期はこれを必要としない。
7. 有限障壁の左右位置読出しが厳密射影になること。
8. 傾斜切替で高モード漏れが厳密に零になること。
9. 局所記録が統計振幅、共分散、確率流を測っていること。
10. 無反応なしの滑らかな厳密2値写像。
11. 固定容量の閉鎖系による無期限の衝突熱浴、永久記録、reset。
12. Hopf pumpからresetまでの総仕事、総熱、総エントロピー収支。
13. 2準位W型を越える一般Born則。
14. Zenoまたは反Zeno効果。
15. 置換済み連続位置模型の旧結果を現行Q1へ再導入すること。
