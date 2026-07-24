@number: 7
@chapter: 本文
@title: 終端整合測度と Bell 共同確率
@status: setting-blind terminal condition の Hamiltonian pullback と二モード位相体積から Bell compatibility weight を導く。

## 7.1 return comparator

return pointer を $(Y_R,\Pi_R)$ とし、滑らかな bounded function $F_R$ を

$$
F_R(0)=0,
\qquad
F_R'(0)=1
$$

となるよう選ぶ。例えば

$$
F_R(Y)
=
\delta_R
\tanh
\left(
\frac{Y}{\delta_R}
\right)
$$

を用いられる。comparator generator を

$$
K_R
=
F_R(Y_R)
\left[
h-\kappa I_-
\right]
$$

とする。ここで $\kappa>0$ は比較器 scale、$h=\omega_\ell J_s$ は二モード台帳の soft energy である。$E_*\geq0$ は comparator generator の定数項には入れず、相補的内部時計の初期相対運動量として置く。

comparator pointer の初期状態を

$$
Y_R=0,
\qquad
\Pi_R=E_*
$$

とする。$K_R$ は $\Pi_R$ に依存しないため、pulse 中

$$
\frac{dY_R}{d\tau}=0.
$$

従って $Y_R=0$ が保たれ、

$$
\frac{d\Pi_R}{d\tau}
=
-F_R'(0)
\left[
h-\kappa I_-
\right]
$$

から unit pulse 後に

$$
\Pi_R(T)
=
E_*+\kappa I_- -h
$$

を得る。

$F_R(0)=0$ なので、comparator pulse は読出し軌道上で messenger と ledger の canonical variables を動かさない。相対時計運動量へ $\Delta\Pi_R=\kappa I_- -h$ を加えるだけである。$E_*$ は時計向きが反転するまでの初期 momentum margin である。

## 7.2 固定 terminal condition

terminal macroregion を

$$
G_R(z_T)
=
\mathbf1_{\{\Pi_R(T)\geq0\}}
$$

とする。これは

$$
G_R=1
\quad\Longleftrightarrow\quad
h\leq E_*+\kappa I_-
$$

と等価である。

第5.9節の相補的内部時計実現では $P_c=0$ なので、

$$
\varrho_A(T)=\Pi_R(T),
\qquad
\varrho_B(T)=-\Pi_R(T).
$$

従って同じ terminal condition は、source で選んだ順序付き時計向き

$$
\varrho_A\geq0,
\qquad
\varrho_B\leq0
$$

が終端まで保たれた条件である。これは terminal half-space の正準力学的起源を与えるが、その半空間だけを物理的履歴集団として数える `[R]` の統計原理を置き換えない。

$G_R$ の関数形は $a,b,A,B$ も $\cos\Delta_{ab}$ も参照しない。setting と outcome への依存は、局所 Hamiltonian rotation を含む flow で $G_R$ を初期面へ pullback したときにのみ現れる。

全 source support で cutoff に当たらない working range

$$
0
\leq
E_*+\kappa I_-
\leq
E_\ell
$$

を仮定する。理想等振幅模型では十分条件として

$$
E_*+\kappa I_0(1+V)
\leq
E_\ell
$$

を用いられる。finite amplitude distribution を許す場合は、その support 上で同じ上界を課す。cutoff に当たる場合の補正は第8章と付録Cで扱う。

## 7.3 terminal compatibility の積分

outcome sector の基準質量を $w_{AB}$ とする。第6章の二モード定理により、sector 内の soft-energy density は $1/E_\ell$ である。source fluctuation を $\zeta$ とし、その基準分布を $d\nu(\zeta)$ と書くと、unnormalized terminal-compatible weight は

$$
W_{AB}(a,b)
=
w_{AB}
\int d\nu(\zeta)
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{
h\leq E_*+\kappa I_-^{AB}(\zeta)
\}}.
$$

working range の下で $h$ 積分は線形なので、

$$
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa
\overline I_-^{AB}
\right].
$$

第6.3節の visibility 表示を代入すると、

$$
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
\right].
$$

ここで

$$
\Delta_{ab}
=
\phi(a)-\phi(b)+\Delta_0
$$

であり、$\Delta_0$ は source phase offset を含む。

重要なのは、Bell compatibility weight の線形性が gate flux からではなく、固定総作用殻上の cumulative Liouville volume

$$
\int_0^x
\frac{dh}{E_\ell}
=
\frac{x}{E_\ell}
$$

から出ることである。

## 7.4 二モード台帳 Bell compatibility 定理

\begin{theorem}[二モード台帳を持つ時間対称 Bell compatibility]
次を仮定する。

1. `[H]`：第5章の有限 Hamiltonian 測定器と第7.1節の setting-blind comparator。
2. `[P]`：第6.3節の phase-locked source と visibility $0\leq V\leq1$。
3. `[S]`：四つの基準 outcome sector の独立符号反転対称性。
4. `[M]`：固定総作用 $E_\ell$ 上の二モード Liouville entrance measure。
5. `[R]`：第5.8節の時間対称境界統計原理。
6. working range：$0\leq E_*+\kappa I_-\leq E_\ell$ が source support 上で成立する。

このとき、規格化した terminal-compatible joint law は

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV_{\rm eff}\cos\Delta_{ab}
\right],
$$

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V.
$$

各履歴の局所 response は deterministic に因子化する。一方、Bell-complete source posterior は一般に setting-dependent である。
\end{theorem}

Proof. `[S]` から $w_{AB}=1/4$ である。第7.3節より

$$
W_{AB}
=
\frac1{4E_\ell}
\left[
E_*+\kappa I_0
-AB\kappa I_0V\cos\Delta_{ab}
\right].
$$

四 outcome を足すと

$$
Z_{a,b}
=
\sum_{A,B}W_{AB}
=
\frac{E_*+\kappa I_0}{E_\ell},
$$

なぜなら

$$
\sum_{A,B}AB=0
$$

だからである。$W_{AB}/Z_{a,b}$ を計算すれば主張の joint law を得る。

fixed complete microstate $\lambda$ では、

$$
A=\mathscr A(a,\lambda),
\qquad
B=\mathscr B(b,\lambda)
$$

であり、

$$
P(A,B\mid a,b,\lambda)
=
P(A\mid a,\lambda)
P(B\mid b,\lambda)
$$

と因子化する。しかし `[R]` 後の $\lambda$ 分布は第7.6節の通り setting-dependent である。

## 7.5 初期時計向き margin $E_*$ の役割

$E_*=0$ では

$$
V_{\rm eff}=V
$$

であり、理想 phase lock $V=1$ なら標準的な unit-visibility cosine law を得る。しかし $\Delta_{ab}=0$ かつ $AB=+1$ の channel では threshold が零になり、terminal-compatible volume も零になる。

$E_*>0$ は相補時計の正向き sector 内で向き反転までの初期運動量余裕を与える。同時に全 channel に正の compatibility floor を与え、

$$
E_*+\kappa I_-^{AB}\geq E_*
$$

とする。その代わり visibility は

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
<V
$$

へ低下する。従って $E_*$ は時計向きの頑健性および低 threshold の正則化と、Bell visibility の交換関係を与える。

## 7.6 microscopic posterior と measurement independence

理想化して、Bell-relevant hidden data を $(A,B,h)$ とする。他の source variables が setting-independently factorize する場合、`[R]` 後の密度は

$$
\rho_R(A,B,h\mid a,b)
=
\frac1{
4(E_*+\kappa I_0)
}
\mathbf1_{\{
0\leq h\leq x_{AB}(a,b)
\}},
$$

$$
x_{AB}(a,b)
=
E_*+\kappa I_0
\left[
1-ABV\cos\Delta_{ab}
\right].
$$

setting を変えると各 outcome sector の support ceiling が変わるため、

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda\mid a',b')
$$

が一般に成立する。

Bell--CHSH の標準導出では、四 setting pair に同じ $\rho(\lambda)$ を用いる。本構成で外れる仮定は measurement independence であり、fixed $\lambda$ における local response factorization ではない [9,10,24,25]。

二つの setting pair に対応する

$$
c=\cos\Delta_{ab},
\qquad
c'=\cos\Delta_{a'b'}
$$

の間の全変動距離は、上の最小 posterior について

$$
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
$$

である。追加 hidden variables が setting-independently factorize する場合、この値は full posterior に対しても正確である。一般の追加構造を許す場合は、$(A,B,h)$ marginal が与える識別可能性の下界になる。

## 7.7 setting frequency の保護

controller の基準分布を $P_S(a,b)$ とする。`[R]` を controller を含む全 ensemble へ適用すると、

$$
P_R(a,b)
\propto
P_S(a,b)Z_{a,b}.
$$

第7.4節で

$$
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
$$

は setting-independent である。従って

$$
P_R(a,b)=P_S(a,b).
$$

実験者は巨視的 controller frequency を変更できる。一方、その setting macrostate と terminal condition の両方に compatible な microscopic source posterior は変化する。この意味で本構成は future-input-dependent または time-symmetric boundary class に属する [7,8,21--23]。

## 7.8 no-signalling と相関

joint law の一側周辺は

$$
P_R(A\mid a,b)
=
\sum_{B=\pm1}
P_R(A,B\mid a,b)
=
\frac12,
$$

$$
P_R(B\mid a,b)
=
\frac12.
$$

従って `[S]` の対称 ensemble では operational no-signalling が成立する。これは microscopic measurement independence が回復したことを意味しない。遠隔 setting dependence は hidden posterior に残るが、outcome-sign symmetry により一側周辺で相殺される。

相関は

$$
E(a,b)
=
\sum_{A,B}
ABP_R(A,B\mid a,b)
=
-V_{\rm eff}\cos\Delta_{ab}.
$$

標準 CHSH angle

$$
\phi(a_0)=0,
\qquad
\phi(a_1)=\frac\pi2,
$$

$$
\phi(b_0)=\frac\pi4,
\qquad
\phi(b_1)=-\frac\pi4
$$

では

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}.
$$

従って

$$
V_{\rm eff}
>
\frac1{\sqrt2}
$$

なら CHSH 不等式を破る。

## 7.9 Bell 前提台帳

本構成の Bell 前提は次の通りである。

- outcome definiteness：満たす。各 Hamiltonian history は一つの anchor-pointer sector を持つ。
- local deterministic response：Bell-complete $\lambda$ 上で満たす。
- parameter independence at fixed $\lambda$：局所記録時刻について満たす。
- common measurement-independent distribution：満たさない。
- operational setting freedom：$Z_{a,b}$ が一定なので controller frequency を保つ。
- equilibrium no-signalling：`[S]` の下で満たす。
- arbitrary-preparation no-signalling：本論文では証明しない。
- absence of observed-data postselection：物理的実装条件として要求する。

従って本論文は Bell の定理を反駁しない。Bell 不等式を外れる共同確率と、外れた仮定を同じ模型の中で明示する。

## 7.10 流束、滞在時間、結果頻度

結果 $A,B$ が comparator 到達前に確定した順時間的 trial 列を考える。全 trial が有限時間で完了し、結果依存の除外がないなら、後段の reaction coordinate が持つ通過時間は、時刻を無作為に選んだときの occupancy を変えるが、trial number で数えた outcome ratio を変えない。

\begin{proposition}[後段時間による結果頻度不変]
$n$ 番目の trial の結果を $\kappa_n=(A_n,B_n)$、完了時間を $\tau_n<\infty$ とする。全 trial を結果に関係なく一度ずつ数えるなら、

$$
\frac1N
\sum_{n=1}^{N}
\mathbf1_{\{\kappa_n=(A,B)\}}
$$

は $\tau_n$ の値に依存しない。結果依存の timeout または非完了 trial の除外を導入した場合にのみ、観測された比率は再重みづけされる。
\end{proposition}

従って

- reaction gate の通過速度。
- 結果依存の待ち時間。
- 有限浴への順時間的 energy leakage。

は、それだけでは `[R]` の代わりにならない。本論文の $W_{AB}$ は gate capacity または completion flux ではなく、`[R]` が物理的集団とする terminal-compatible phase volume である。

## 7.11 本章の結論

setting-blind comparator は、相補時計の初期相対運動量 $\Pi_R(0)=E_*$ に $\kappa I_- -h$ を加えて

$$
\Pi_R(T)=E_*+\kappa I_- -h
$$

を作る。固定 terminal condition は順序付き時計向きの保存と同値であり、同時に $h$ の sublevel volume を測る。二モード台帳の一様密度と対称準備を用いると、Bell 型 cos 共同確率が通常の正の Liouville 積分として得られる。

確率の起源は `[R]` であり、時計相補性だけではない。cos dependence、linear threshold volume、terminal half-space の正準構造は Hamiltonian apparatus が計算する。Bell の前提違反は measurement independence に位置し、macroscopic setting frequency と equilibrium no-signalling は四 sector の対称性により保たれる。
