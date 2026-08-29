@number: M
@chapter: 付録
@title: 有限信号作用と作用殻状態数の共通起源
@status: M50とR164について、一般有限信号作用から正則化枝容量を作り、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き分布とR161の有効自由エネルギーが得られることを条件付きで厳密に示す。Q1の2成分信号とQ2の4成分信号を同じ定理の特殊化として扱い、滑らかな有限幅拘束、枝流束、node、資源発散、表現の二重計数禁止を明示する。

## M.1 目的と主張範囲

付録Lは、正の条件付き分布 $\pi_i^\delta(v)$ に対して可逆な粒子位置jump過程と有限衝突熱浴を構成する。本付録はその上流をQ1、Q2、Q3に共通なM50「有限信号作用・作用殻・粒子位置熱化共通モジュール」として固定する。旧版では

```math
E_i^\delta(v)
=
-\Theta\log\pi_i^\delta(v)
```

を制御器へ設計した地形として置いていた。本付録ではBorn型確率を先に定義せず、同じ試行に存在する信号作用と、位置枝ごとの排他的な作用殻状態数から $\pi_i^\delta$ を導く。

旧R24の一般作用殻容量と2作用殻の線形性は、この目的に使える。ただし旧M15の位置入口模型、等方混合、標本化後の再埋込み、測定周期を復活させない。R164は、旧R24の状態数補題を一般有限信号、正則化、R161--R163の語義へ移植した条件付き結果である。M50は共通理論部品であり、Q1、Q2、Q3が同一ハードウェアを共有するという主張ではない。

本付録で区別する物理部分系は次の4つである。

1. $v\in\mathbb C^m$ を持つ有限信号担体。
2. 枝容量を数える作用殻fiber。
3. 粒子位置 $X=i$。
4. $X$ を再平衡化する付録Lの有限衝突熱浴。

作用殻fiberと衝突熱浴は同じものではない。前者は条件付き状態数を、後者はその状態数比と整合する粒子位置遷移を与える。

## M.2 階数1共分散の支持補題と単一試行信号

M50は各試行に存在する非零信号を入力とする。Q1のように複素振幅を集団共分散の階数1因子として定義する場合、その統計因子を単一試行信号と同一視せず、次の支持補題を介して接続する。

確率変数としての信号浴座標を $Z\in\mathbb C^m$ とし、

```math
0
<
\mathbb E[Z^\dagger Z]
<
\infty,
\qquad
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}
{\mathbb E[Z^\dagger Z]}
```

とする。$C_Z$ は正半定値、trace 1である。

ここでも $C_Z$ は非中心化された規格化第2モーメントを指す。$\mathbb E[Z]=0$ の場合にだけ通常の中心化共分散と比例して一致する。以下の支持補題へ中心化共分散の階数条件だけを代入してはならない。

<!-- theorem-start:lemma -->
**補題（階数1共分散の支持）**

単位ベクトル $c\in\mathbb C^m$ について

```math
C_Z
=
cc^\dagger
```

ならば、複素確率変数 $\alpha=c^\dagger Z$ を用いて

```math
Z
=
\alpha c
\qquad\text{a.s.}
```

と書ける。逆に $Z=\alpha c$ がほとんど確実に成り立ち、$\mathbb E|\alpha|^2>0$ なら $C_Z=cc^\dagger$ である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明（階数1共分散の支持）**

$P_c^\perp=I_m-cc^\dagger$ とする。このとき

```math
\frac{
\mathbb E\left\|P_c^\perp Z\right\|^2
}{
\mathbb E[Z^\dagger Z]
}
=
\operatorname{tr}
\left(
P_c^\perp C_Z
\right)
=
0.
```

非負確率変数の期待値が零なので $P_c^\perp Z=0$ がほとんど確実に成り立つ。従って $Z=(c^\dagger Z)c=\alpha c$ である。逆向きは共通因子 $\mathbb E|\alpha|^2$ が規格化で消えることから従う。証明終。
<!-- theorem-end:proof -->

近似階数1では、単一試行信号のray外平均作用比を

```math
\varepsilon_{\rm supp}(c)
:=
\operatorname{tr}
\left[
\left(I_m-cc^\dagger\right)C_Z
\right]
=
\frac{
\mathbb E
\left\|
\left(I_m-cc^\dagger\right)Z
\right\|^2
}{
\mathbb E[Z^\dagger Z]
}
```

と定める。これは平均二乗評価であり、各試行の相対方向誤差を一様には抑えない。M50へ渡す安全試行では $z=Z(\omega)$ に $z^\dagger z\geq r_*>0$ を課し、閾値未満と零信号を無反応へ送る。有限時間Hopf方向誤差から $\varepsilon_{\rm supp}$ を評価する場合は同じ偏差を二重に誤差加算しない。

Q1ではM50の仮引数を $v=z$ と特殊化する。厳密支持上では $z=\alpha c$ なので

```math
\pi_i^\delta(z)
=
\frac{
|\left(\Psi c\right)_i|^2
+
\delta q_i
}{1+\delta}
\qquad\text{a.s.}
```

となるが、物理制御器が入力するのは $c$ または $C_Z$ でなく単一試行の $z$ である。$c$ は集団を表示する統計的rayに留まる。

この補題は正半定値自己共分散 $\mathbb E[ZZ^\dagger]$ に対する結果である。Q2の交差モーメント $\mathbb E[z_Az_B^{\mathsf T}]$、そのベクトル化、またはそこから作る階数1射影へ適用して、積標本 $z_A\otimes z_B$ がsinglet ray上にあるとは結論しない。R146はそのような直接singlet支持が不可能であることを示す。M49中央殻にも本補題を適用せず、各試行に存在する物理program担体 $d_{\rm prog}$ を $v=d_{\rm prog}$ としてM50へ渡す。

Q3のR168は正半定値自己共分散の階数1支持をこのまま使う。高階数R169は本補題を使わず、各試行の全作用が固定されるときだけ、試行ごとのray規格化と集団共分散の規格化が可換になることを使う。可変全作用集団またはQ2の交差モーメントへR169を流用しない。

## M.3 M50の信号作用と正則化枝容量

有限な排他的枝集合を $\mathcal I$、枝数を $L$ とし、信号次元 $m\leq L$ の等長埋込みを

```math
\Psi:\mathbb C^m\longrightarrow\mathbb C^L,
\qquad
\Psi^\dagger\Psi=I_m
```

とする。作用単位 $\mathcal J_0>0$ に対して、単一試行信号の総作用と枝信号作用を

```math
J_{\rm sig}(v)
=
\mathcal J_0 v^\dagger v,
\qquad
J_i(v)
=
\mathcal J_0
\left| (\Psi v)_i \right|^2
```

と置く。等長性から

```math
\sum_iJ_i(v)
=
J_{\rm sig}(v)
```

である。正の固定基準分布 $q_i>0$、$\sum_iq_i=1$ と有限正則化 $\delta>0$ に対し、枝 $i$ の作用容量を

```math
A_i^\delta(v)
=
J_i(v)
+
\delta q_iJ_{\rm sig}(v)
```

とする。このとき

```math
\sum_iA_i^\delta(v)
=
(1+\delta)J_{\rm sig}(v),
\qquad
A_i^\delta(v)>0
```

が $v\neq0$ で成り立つ。$\delta q_iJ_{\rm sig}$ は確率の混合ではなく、背景作用を枝へ分けた有限装置容量として定義される。

容量式は共通位相に不変で、振幅拡大に対して2次の共変性を持つ。

```math
A_i^\delta(e^{i\alpha}v)
=
A_i^\delta(v),
\qquad
A_i^\delta(\gamma v)
=
|\gamma|^2A_i^\delta(v)
```

この全振幅依存性は、後で全枝状態数を規格化すると消える。

## M.4 排他的枝と単一母測度

位置枝に対応する作用殻を

```math
\Gamma^\delta(v)
=
\bigsqcup_{i\in\mathcal I}
\Gamma_i^\delta(v)
```

という非交和にする。1つの微視的状態は、同時に複数枝の状態として数えない。枝 $i$ には、活性作用 $K_i\geq0$ と1本の明反応作用 $I_i\geq0$、それぞれの角 $\theta_{K_i},\theta_{I_i}\in[0,2\pi)$ を置き、

```math
K_i+I_i=A_i^\delta(v)
```

を課す。作用基準 $J_{\rm ref}>0$ を使い、枝状態数を

```math
\Omega_i^\delta(v)
=
\frac{1}{J_{\rm ref}}
\int_{\Gamma_i}
\delta
\left(
A_i^\delta(v)-K_i-I_i
\right)
dK_i\,dI_i\,d\theta_{K_i}\,d\theta_{I_i}
```

と定める。全枝は同じLiouville規約、同じ角周期、同じ作用基準で数える。枝ごとに別々の規格化測度を置いてから比較するのではなく、非交和上の単一母測度を最後に一度だけ規格化する。

## M.5 一般作用殻容量

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

## M.6 R164：条件付き作用殻の状態数起源

<!-- theorem-start:theorem -->
**定理（R164：有限信号作用のBorn型殻状態数）**

$\Psi:\mathbb C^m\to\mathbb C^L$、$\Psi^\dagger\Psi=I_m$、$v\neq0$、$q_i>0$、$\sum_iq_i=1$、$\delta\geq0$ とする。$\delta=0$ では正容量を持つ活性支持だけを枝集合とする。枝容量を

```math
A_i^\delta(v)
=
\mathcal J_0
\left[
\left|(\Psi v)_i\right|^2
+
\delta q_i v^\dagger v
\right]
```

とし、各排他的枝を同じ2作用殻Liouville測度で数える。このとき

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}
A_i^\delta(v)
```

であり、非交和上の規格化枝重みは

```math
\begin{aligned}
P_i^\delta(v)
&=
\frac{\Omega_i^\delta(v)}
{\sum_j\Omega_j^\delta(v)}\\
&=
\frac{
| (\Psi v)_i |^2/(v^\dagger v)
+
\delta q_i
}{1+\delta}\\
&=
\pi_i^\delta(v).
\end{aligned}
```

従ってBorn型条件付き重みは、確率を枝容量へ書き込むことなく、有限信号作用の枝分解、背景作用容量、各排他的枝の2作用殻の状態数、単一母測度の規格化から得られる。ここで「2作用殻」は各枝の内部に非負作用が2本あるという意味であり、枝数が2であることを意味しない。Q1では典型的に $m=2$、Q2の中央共同読出しでは $m=L=4$ である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R164）**

一般作用殻容量の $n=2$ を各枝へ適用する。全枝に共通な $(2\pi)^2/J_{\rm ref}$ は規格化で消える。等長性と $\sum_iq_i=1$ から分母は $(1+\delta)\mathcal J_0v^\dagger v$ である。これを枝容量で割れば表示式を得る。証明終。
<!-- theorem-end:proof -->

R164は共通位相と全振幅に不変な枝確率を与える。一方、作用殻そのものの容量は全振幅に共変である。この区別により、信号のray情報と有限作用資源を混同しない。$\delta=0$ の零容量枝は状態数零であり、活性支持の外に置く。正の全枝混合率を必要とする粒子位置熱化では $\delta>0$ を使うが、中央の1回限りのQ2読出しでは活性支持上の直接標本化に $\delta=0$ を使える。

## M.7 有効自由エネルギーとR161への接続

作用殻fiberを消去した位置枝の有効自由エネルギーを

```math
F_i^{\rm sh}(v)
=
-\Theta\log\Omega_i^\delta(v)
```

とする。全枝状態数の基準を

```math
F_{\rm eq}^{\rm sh}(v)
=
-\Theta
\log
\sum_j\Omega_j^\delta(v)
```

と置けば、付録Lの地形は

```math
\begin{aligned}
E_i^\delta(v)
&=
F_i^{\rm sh}(v)-F_{\rm eq}^{\rm sh}(v)\\
&=
-\Theta\log\pi_i^\delta(v)
\end{aligned}
```

として得られる。従って $E_i^\delta$ は裸の配置エネルギーではなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。全系の平衡Hamiltonianと周辺化を別に与えた場合を除き、これを無条件に平均力Hamiltonianとは呼ばない。粗視化後の確率過程と微視的な仕事・熱を同一視するには追加条件が必要である [50,51]。

状態数を残す表示と、作用殻を消去した表示は同値だが、同じ縮約分配関数内で混ぜない。すなわち

```math
P_i^\delta
=
\frac{\Omega_i^\delta}{\sum_j\Omega_j^\delta}
```

を使う**作用殻明示表示**と、

```math
P_i^\delta
=
\frac{e^{-\beta E_i^\delta}}
{\sum_je^{-\beta E_j^\delta}}
```

を使う**作用殻消去表示**のどちらか一方を選ぶ。$\Omega_i^\delta e^{-\beta E_i^\delta}$ を同じ分配関数の枝重みとして掛けると状態数を2回数え、$\Omega_i^2$ に比例するため禁止する。

R161の平方根率は

```math
k_{i\to j}^\delta(v)
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

## M.8 直接作用分配次元の剛性

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

作用を直接受け取らず、全枝に同じ因子 $S(v)>0$ を掛けるspectator自由度は

```math
\widetilde\Omega_i^\delta(v)
=
S(v)\Omega_i^\delta(v)
```

として規格化で消える。枝依存spectator体積、異なる角周期、異なるcoarea Jacobianは消えず、枝対称性誤差に数える。

## M.9 入口流束と枝非対称誤差

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

## M.10 滑らかな有限幅作用容量

厳密デルタ殻は条件付き状態数の解析極限である。有限剛性の滑らかな実装候補として、枝 $i$ に

```math
H_{\kappa,i}
=
\frac{\kappa}{2}
\left(
K_i+I_i-A_i^\delta(v)
\right)^2,
\qquad
\kappa>0
```

を置く。角積分後の条件付き分配関数は

```math
Z_{\kappa,i}(v)
=
(2\pi)^2
\int_0^\infty
s
\exp
\left[
-\frac{\beta\kappa}{2}
\left(s-A_i^\delta(v)\right)^2
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

## M.11 node、零seed、有限資源

安全試行で

```math
v^\dagger v
\geq
r_*>0,
\qquad
q_{\min}
=
\min_iq_i
```

とすれば

```math
A_i^\delta(v)
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

を十分大きく保つ必要がある。$\delta\downarrow0$ で他の尺度を固定するなら、必要剛性は下界の次数として少なくとも

```math
\kappa
=
\Omega
\left(
\delta^{-2}
\right)
```

と増大する。$\kappa=\Theta(\delta^{-2})$ はこの下界を満たす代表的な選択であり、より大きい剛性を排除しない。これは付録Lの対数地形幅、衝突流束、混合時間に加わる独立な資源発散である。

$\delta=0$ で $A_i=0$ となるnodeは、厳密殻では状態数零である。一方、有限 $\kappa$ の滑らかな分配関数は $A_i=0$ でも正の端点寄与を持つため、厳密nodeを有限剛性で再現しない。零seed $v=0$ ではrayも規格化枝重みも定義せず、正式な無反応結果とする。安全閾値 $r_*$ 未満の試行、容量比較境界、枝選択失敗も完全結果集合へ残し、除外後の2値再規格化を行わない。

## M.12 R162、R163の熱力学語義

R164後の付録Lでは、$E_i^\delta$ を作用殻fiberの有効自由エネルギーとして読む。辺障壁は

```math
B_{ij}^\delta(v)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(v)+E_j^\delta(v)
\right]
```

と書ける。全ての $E_i^\delta$ を共通関数 $g(v)$ だけ移し、障壁も同じだけ移せば、活性化差 $B_{ij}^\delta-E_i^\delta$、衝突率、経路確率は不変である。

R163の正逆経路確率比と積分ゆらぎ関係は、粗視化された粒子位置跳躍過程について厳密である。作用殻明示表示での殻自由エネルギー仕事と、作用殻消去表示での相対有効仕事を

```math
W_i^{\rm sh}
=
\Delta F_i^{\rm sh},
\qquad
W_i^{\rm rel}
=
\Delta E_i
=
W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}
```

と区別する。全作用を保存するunitary操作では $F_{\rm eq}^{\rm sh}$ の共通項が一定になり得るが、pump、容量制御器、resetが作用を出し入れする一般の周期では一定とは限らない。従来のquench量

```math
W_i^{\rm rel}
=
E_i^\delta(v^+)-E_i^\delta(v^-)
```

と平均相対エントロピー恒等式も、相対有効仕事として厳密である。ただし、作用殻を実際に変形する有限時間過程、殻内平衡化、制御器反作用を含めなければ、$W^{\rm rel}$ を装置全体の機械仕事、跳躍時の有効自由エネルギー差を全微視的熱と同一視しない。ゆらぎの定理はR164で得た地形の下流整合性を検査するが、状態数の線形則を選び出す根拠ではない。

次元は全章で固定する。$J_{\rm sig},J_i,A_i,J_{\rm ref}$ は作用、$\Omega_i$ は無次元、$\Theta,E_i,F_i,B_{ij}$ と衝突セルエネルギーはエネルギー、$\beta$ はエネルギーの逆数、$\kappa$ はエネルギー毎作用2乗、跳躍率と衝突率は時間の逆数である。

## M.13 Q1・Q2・Q3への接続と非主張

M50をQ1、Q2、Q3の1回の作用殻準備と粒子位置再平衡化へ使うとき、共通誤差を

```math
\begin{aligned}
\varepsilon_{M50}
={}&
\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sym}
+\varepsilon_{\rm ad}\\
&+\varepsilon_\delta
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
\end{aligned}
```

と定める。$\varepsilon_{\rm cap}$ は有限容量結合、$\varepsilon_{\rm width}$ は有限剛性、$\varepsilon_{\rm sym}$ は枝非対称、$\varepsilon_{\rm ad}$ は殻内条件付き平衡化と有効地形切替、$\varepsilon_\delta$ は正則化、$\varepsilon_{\rm mix}$ は有限時間粒子位置混合、$\varepsilon_{\rm coll}$ は有限衝突近似、$\varepsilon_{\rm hold}$ は信号保持反作用である。$\varepsilon_{\rm supp}$ はM50内部誤差でなく、統計的rayから単一試行入力への上流受渡し誤差として別に記帳する。有限時間Hopf誤差から評価した同じ偏差を両方へ加えない。直接作用区間標本化だけを使うQ2-1では $\varepsilon_{\rm mix}$ と $\varepsilon_{\rm coll}$ を必須項にせず、実際に用いた項だけを台帳へ入れる。

R164の達成範囲は「条件付き厳密結果＋滑らかな有限幅近似」である。本付録は次を主張しない。

1. 枝容量 $A_i^\delta(v)$ を作る結合が任意のQ1、Q2、Q3信号状態から自動的に準備されること。
2. 作用殻Liouville測度が有限時間の局所力学で一様またはGibbs的に準備されること。
3. 枝対称な余面積因子と入口流束が信号担体だけから自動的に従うこと。
4. 作用殻とR162の衝突熱浴が同一の物理部分系であること。
5. 作用殻、信号保持制御器、衝突セルを含む全微視的仕事・熱収支がR163だけから従うこと。
6. $\delta=0$ のnodeを有限剛性、有限衝突流束、有限混合時間で一様に実現できること。
7. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。
8. 旧M15の入口標本化、殻等方混合、標本化後再埋込み、全測定周期が再び現行結果になること。

従ってQ1-2は部分達成のままである。Q2-1はR165の中央4枝直接標本化を追加しても達成判定を変えず、Q2-2はR166の切断後局所因子化を追加しても条件付き達成のままである。Q3のR168は階数1支持、R169は固定全作用集団を本付録の単一試行信号契約へ接続するが、R170の作用容量結合から局所記録までの統合を自動的に与えない。Q3-4、Q3-5は条件付き達成のままである。
