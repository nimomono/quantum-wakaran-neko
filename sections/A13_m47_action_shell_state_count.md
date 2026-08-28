@number: M
@chapter: 付録
@title: M47条件付き作用殻の状態数起源
@status: R164について、M47の単一試行信号作用から正則化枝容量を作り、排他的な2作用殻のLiouville状態数を単一母測度で数えるとBorn型条件付き分布とR161の有効自由エネルギーが得られることを条件付きで厳密に示す。滑らかな有限幅拘束、枝流束、node、資源発散を明示し、作用容量結合と殻内平衡化を含む有限局所Hamiltonian周期は未導出として残す。

## M.1 目的と主張範囲

付録Lは、正の条件付き分布 $\pi_i^\delta(z)$ に対して可逆な配置jump過程と有限衝突熱浴を構成した。しかし旧版では

```math
E_i^\delta(z)
=
-\Theta\log\pi_i^\delta(z)
```

をcontrollerへ設計した地形として置いていた。本付録はその上流を一段だけ閉じる。Born型確率を先に定義せず、同じ試行に存在する信号作用と、配置枝ごとの排他的な作用殻状態数から $\pi_i^\delta$ を導く。

旧R24の一般作用殻容量と2作用殻の線形性は、この目的に使える。ただし旧M15の位置入口模型、等方混合、標本化後の再埋込み、測定周期を復活させない。R164は、旧R24の状態数補題を現行M47の信号bath、W型mode埋込み、正則化、R161--R163の語義へ移植した新しい条件付き結果である。

本付録で区別する物理部分系は次の4つである。

1. $z\in\mathbb C^2$ を持つ2モード信号bath。
2. 枝容量を数える作用殻fiber。
3. 実現配置 $X=i$。
4. $X$ を再平衡化する付録Lの有限衝突熱浴。

作用殻fiberと衝突熱浴は同じものではない。前者は条件付き状態数を、後者はその状態数比と整合する配置遷移を与える。

## M.2 信号作用と正則化枝容量

有限W型配置グラフの頂点集合を $\Omega_W$、頂点数を $L$ とし、最低2モードの等長埋込みを

```math
\Phi:\mathbb C^2\longrightarrow\mathbb C^L,
\qquad
\Phi^\dagger\Phi=I_2
```

とする。作用単位 $\mathcal J_0>0$ に対して、単一試行信号の総作用と枝信号作用を

```math
J_{\rm sig}(z)
=
\mathcal J_0 z^\dagger z,
\qquad
J_i(z)
=
\mathcal J_0
\left| (\Phi z)_i \right|^2
```

と置く。等長性から

```math
\sum_iJ_i(z)
=
J_{\rm sig}(z)
```

である。正の固定基準分布 $q_i>0$、$\sum_iq_i=1$ と有限正則化 $\delta>0$ に対し、枝 $i$ の作用容量を

```math
A_i^\delta(z)
=
J_i(z)
+
\delta q_iJ_{\rm sig}(z)
```

とする。このとき

```math
\sum_iA_i^\delta(z)
=
(1+\delta)J_{\rm sig}(z),
\qquad
A_i^\delta(z)>0
```

が $z\neq0$ で成り立つ。$\delta q_iJ_{\rm sig}$ は確率の混合ではなく、背景作用を枝へ分けた有限装置容量として定義される。

容量式は共通位相に不変で、振幅拡大に対して2次の共変性を持つ。

```math
A_i^\delta(e^{i\alpha}z)
=
A_i^\delta(z),
\qquad
A_i^\delta(\gamma z)
=
|\gamma|^2A_i^\delta(z)
```

この全振幅依存性は、後で全枝状態数を規格化すると消える。

## M.3 排他的枝と単一母測度

配置枝に対応する作用殻を

```math
\Gamma^\delta(z)
=
\bigsqcup_{i\in\Omega_W}
\Gamma_i^\delta(z)
```

という非交和にする。1つの微視的状態は、同時に複数枝の状態として数えない。枝 $i$ には、活性作用 $K_i\geq0$ と1本の明反応作用 $I_i\geq0$、それぞれの角 $\theta_{K_i},\theta_{I_i}\in[0,2\pi)$ を置き、

```math
K_i+I_i=A_i^\delta(z)
```

を課す。作用基準 $J_{\rm ref}>0$ を使い、枝状態数を

```math
\Omega_i^\delta(z)
=
\frac{1}{J_{\rm ref}}
\int_{\Gamma_i}
\delta
\left(
A_i^\delta(z)-K_i-I_i
\right)
dK_i\,dI_i\,d\theta_{K_i}\,d\theta_{I_i}
```

と定める。全枝は同じLiouville規約、同じ角周期、同じ作用基準で数える。枝ごとに別々の規格化測度を置いてから比較するのではなく、非交和上の単一母測度を最後に一度だけ規格化する。

## M.4 一般作用殻容量

$n$ 本の非負作用 $J_1,\ldots,J_n$ と角 $\theta_1,\ldots,\theta_n$ に対し、無次元状態数を

```math
\Omega_n(A)
=
\frac{1}{J_{\rm ref}^{n-1}}
\int
\delta
\left(
A-\sum_{r=1}^nJ_r
\right)
\prod_{r=1}^n
dJ_r\,d\theta_r
```

と置く。

<!-- theorem-start:lemma -->
**補題（一般作用殻容量）**

$A>0$ に対して

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
\left(
\frac{A}{J_{\rm ref}}
\right)^{n-1}
```

である。特に2作用殻は

```math
\Omega_2(A)
=
\frac{(2\pi)^2}{J_{\rm ref}}A
```

と容量に線形である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明（一般作用殻容量）**

角積分は $(2\pi)^n$ を与える。作用積分は $J_r\geq0$、$\sum_rJ_r=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。作用基準で無次元化すれば表示式を得る。証明終。
<!-- theorem-end:proof -->

## M.5 R164：条件付き作用殻の状態数起源

<!-- theorem-start:theorem -->
**定理（R164：M47条件付き作用殻の状態数起源）**

$\Phi^\dagger\Phi=I_2$、$z\neq0$、$q_i>0$、$\sum_iq_i=1$、$\delta>0$ とする。枝容量を

```math
A_i^\delta(z)
=
\mathcal J_0
\left[
\left|(\Phi z)_i\right|^2
+
\delta q_i z^\dagger z
\right]
```

とし、各排他的枝を同じ2作用殻Liouville測度で数える。このとき

```math
\Omega_i^\delta(z)
=
\frac{(2\pi)^2}{J_{\rm ref}}
A_i^\delta(z)
```

であり、非交和上の規格化枝重みは

```math
\begin{aligned}
P_i^\delta(z)
&=
\frac{\Omega_i^\delta(z)}
{\sum_j\Omega_j^\delta(z)}\\
&=
\frac{
| (\Phi z)_i |^2/(z^\dagger z)
+
\delta q_i
}{1+\delta}\\
&=
\pi_i^\delta(z).
\end{aligned}
```

従ってBorn型条件付き重みは、確率を枝容量へ書き込むことなく、信号作用のW型mode分解、背景作用容量、排他的2作用殻の状態数、単一母測度の規格化から得られる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R164）**

一般作用殻容量の $n=2$ を各枝へ適用する。全枝に共通な $(2\pi)^2/J_{\rm ref}$ は規格化で消える。等長性と $\sum_iq_i=1$ から分母は $(1+\delta)\mathcal J_0z^\dagger z$ である。これを枝容量で割れば表示式を得る。証明終。
<!-- theorem-end:proof -->

R164は共通位相と全振幅に不変な枝確率を与える。一方、作用殻そのものの容量は全振幅に共変である。この区別により、信号のray情報と有限作用資源を混同しない。

## M.6 有効自由エネルギーとR161への接続

作用殻fiberを消去した配置枝の有効自由エネルギーを

```math
F_i^{\rm sh}(z)
=
-\Theta\log\Omega_i^\delta(z)
```

とする。全枝状態数の基準を

```math
F_{\rm eq}^{\rm sh}(z)
=
-\Theta
\log
\sum_j\Omega_j^\delta(z)
```

と置けば、付録Lの地形は

```math
\begin{aligned}
E_i^\delta(z)
&=
F_i^{\rm sh}(z)-F_{\rm eq}^{\rm sh}(z)\\
&=
-\Theta\log\pi_i^\delta(z)
\end{aligned}
```

として得られる。従って $E_i^\delta$ は裸の配置エネルギーではなく、条件付き作用殻fiberを消去したmesostate有効自由エネルギー、すなわちこの模型におけるHamiltonian of mean forceである。粗視化後の確率過程と微視的な仕事・熱を同一視するには追加条件が必要である [50,51]。

R161の平方根率は

```math
k_{i\to j}^\delta(z)
=
\kappa_Xa_{ij}
\exp
\left[
-\frac{\beta}{2}
\left(
E_j^\delta-E_i^\delta
\right)
\right]
```

と書ける。R164は定常重みと有効自由エネルギーの起源を与えるが、対称活動度 $a_{ij}$ の大きさや平方根分割そのものを作用殻から一意に導かない。R161はその有効地形に整合する局所再平衡化定理として独立に必要である。

## M.7 直接作用分配次元の剛性

活性作用に加えて、枝容量を直接分配する明反応作用が $q$ 本ある場合、固定作用殻は $q+1$ 作用からなる。一般容量公式により

```math
\Omega_{q+1}(A_i)
\propto
A_i^q
```

となる。

<!-- theorem-start:proposition -->
**命題（作用分配次元の剛性）**

枝間で共通なLiouville規約の下で、正規化状態数は

```math
P_i^{(q)}
=
\frac{(A_i^\delta)^q}
{\sum_j(A_j^\delta)^q}
```

である。全ての正容量族に対してR164の線形重みを保つのは $q=1$、すなわち2作用殻だけである。
<!-- theorem-end:proposition -->

作用を直接受け取らず、全枝に同じ因子 $S(z)>0$ を掛けるspectator自由度は

```math
\widetilde\Omega_i^delta(z)
=
S(z)\Omega_i^\delta(z)
```

として規格化で消える。枝依存spectator体積、異なる角周期、異なるcoarea Jacobianは消えず、枝対称性誤差に数える。

## M.8 入口流束と枝非対称誤差

作用殻状態を配置遷移入口として数える場合、正方向流束を

```math
\mathscr F_i
=
\lambda_i\Omega_i^\delta
```

と書く。$\lambda_i$ は法線速度、反応面の向き、透過率、coarea因子、入口窓、直接分配しないspectator体積を含む。$\lambda_i=\lambda>0$ が全枝で共通なら、流束頻度もR164の $\pi_i^\delta$ に一致する。

一般に $\lambda_i=\lambda(1+\eta_i)$、$|\eta_i|\leq\varepsilon_{\rm sym}<1$ とする。流束分布を $P^{\rm flux}$ とすれば

```math
D_{\rm TV}
\left(
P^{\rm flux},
\pi^\delta
\right)
\leq
\frac{\varepsilon_{\rm sym}}
{1-\varepsilon_{\rm sym}}.
```

この誤差は、R161の混合誤差またはR162の衝突bath誤差へ隠さず、作用殻準備の枝対称性誤差として別に記帳する。

## M.9 滑らかな有限幅作用容量

厳密デルタ殻は条件付き状態数の解析極限である。有限剛性の滑らかな実装候補として、枝 $i$ に

```math
H_{\kappa,i}
=
\frac{\kappa}{2}
\left(
K_i+I_i-A_i^\delta(z)
\right)^2,
\qquad
\kappa>0
```

を置く。角積分後の条件付き分配関数は

```math
Z_{\kappa,i}(z)
=
(2\pi)^2
\int_0^\infty
s
\exp
\left[
-\frac{\beta\kappa}{2}
\left(s-A_i^\delta(z)\right)^2
\right]
ds.
```

$a=\beta\kappa/2$、$x_i=\sqrt a A_i^\delta$ とすれば、積分は厳密に

```math
Z_{\kappa,i}
=
(2\pi)^2
\left[
\frac{e^{-x_i^2}}{2a}
+
\frac{A_i^\delta\sqrt\pi}{2\sqrt a}
\left(
1+\operatorname{erf}x_i
\right)
\right]
```

である。$C_\kappa=(2\pi)^2\sqrt{\pi/a}$ と置くと

```math
Z_{\kappa,i}
=
C_\kappa A_i^\delta
\left(
1+r_i
\right),
```

```math
0
\leq
r_i
\leq
\frac{e^{-x_i^2}}
{2\sqrt\pi x_i}
```

が $x_i>0$ で成り立つ。$\widehat\pi_i^\delta=Z_{\kappa,i}/\sum_jZ_{\kappa,j}$、$\rho=\max_ir_i$ とすれば

```math
D_{\rm TV}
\left(
\widehat\pi^\delta,
\pi^\delta
\right)
\leq
\frac{\rho}{2}.
```

これを有限幅誤差 $\varepsilon_{\rm width}$ とする。

## M.10 node、零seed、有限資源

安全試行で

```math
z^\dagger z
\geq
r_*>0,
\qquad
q_{\min}
=
\min_iq_i
```

とすれば

```math
A_i^\delta(z)
\geq
\mathcal J_0\delta q_{\min}r_*.
```

従って滑らかな有限幅誤差を全bath rayで一様に小さくするには

```math
x_{\min}
=
\sqrt{\frac{\beta\kappa}{2}}
\mathcal J_0\delta q_{\min}r_*
```

を十分大きく保つ必要がある。$\delta\downarrow0$ で他の尺度を固定するなら、必要剛性は少なくとも

```math
\kappa
=
O
\left(
\delta^{-2}
\right)
```

まで増え得る。これは付録Lの対数地形幅、衝突流束、混合時間に加わる独立な資源発散である。

$\delta=0$ で $A_i=0$ となるnodeは、厳密殻では状態数零である。一方、有限 $\kappa$ の滑らかな分配関数は $A_i=0$ でも正の端点寄与を持つため、厳密nodeを有限剛性で再現しない。零seed $z=0$ ではrayも規格化枝重みも定義せず、正式な無反応結果とする。安全閾値 $r_*$ 未満の試行、容量比較境界、枝選択失敗も完全結果集合へ残し、除外後の2値再規格化を行わない。

## M.11 R162、R163の熱力学語義

R164後の付録Lでは、$E_i^\delta$ を作用殻fiberの有効自由エネルギーとして読む。辺障壁は

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

と書ける。全ての $E_i^\delta$ を共通関数 $g(z)$ だけ移し、障壁も同じだけ移せば、活性化差 $B_{ij}^\delta-E_i^\delta$、衝突率、経路確率は不変である。

R163の正逆経路確率比と積分ゆらぎ関係は、粗視化された配置jump過程について厳密である。quench量

```math
W_i^{\rm eff}
=
E_i^\delta(c')-E_i^\delta(c)
```

と平均相対エントロピー恒等式も、有効地形仕事として厳密である。ただし、作用殻fiberを実際に変形する有限時間protocol、fiber内平衡化、controller反作用を含めなければ、$W^{\rm eff}$ を装置全体の機械仕事、jump時の有効自由エネルギー差を全微視的熱と同一視しない。ゆらぎの定理はR164で得た地形の下流整合性を検査するが、状態数の線形則を選び出す根拠ではない。

## M.12 M47周期への接続と非主張

R164をM47周期へ使うとき、1回の配置再平衡化誤差へ

```math
\varepsilon_{\rm sh}
=
\varepsilon_{\rm cap}
+
\varepsilon_{\rm width}
+
\varepsilon_{\rm sym}
+
\varepsilon_{\rm ad}
```

を加える。$\varepsilon_{\rm cap}$ は有限容量結合、$\varepsilon_{\rm width}$ は有限剛性、$\varepsilon_{\rm sym}$ は枝非対称、$\varepsilon_{\rm ad}$ はfiber内条件付き平衡化と有効地形切替の有限時間誤差である。R161の混合、R162の衝突近似、信号bath保持とは別の誤差なので二重計上しない。

R164の達成範囲は「条件付き厳密結果＋滑らかな有限幅近似」である。本付録は次を主張しない。

1. 枝容量 $A_i^\delta(z)$ を作る結合が任意のM47信号状態から自動的に準備されること。
2. 作用殻Liouville測度が有限時間の局所力学で一様またはGibbs的に準備されること。
3. 枝対称なcoarea因子と入口流束がW型装置だけから自動的に従うこと。
4. 作用殻fiberとR162の衝突熱浴が同一の物理部分系であること。
5. fiber、信号bath保持controller、衝突セルを含む全微視的仕事・熱収支がR163だけから従うこと。
6. $\delta=0$ のnodeを有限剛性、有限衝突流束、有限混合時間で一様に実現できること。
7. 2準位W型を越える任意次元、任意POVM、連続スペクトルの一般Born則。
8. 旧M15の入口標本化、殻等方混合、標本化後再埋込み、全測定周期が再び現行結果になること。

従ってQ1-2は部分達成のままである。Born型状態数と有効自由エネルギーの条件付き起源はR164で得たが、作用容量結合、fiber内平衡化、枝対称性、信号bath反作用をM47測定周期の有限局所Hamiltonianとして統合する問題が残る。Q1-3には、さらにHopf pump、記録、template交換、resetを含む周期総収支が残る。
