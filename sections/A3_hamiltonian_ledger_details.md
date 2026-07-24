@number: A3
@chapter: 付録
@title: 明示 Hamiltonian、二モード位相体積、補正項
@status: 第II部で用いた canonical map、作用殻測度、多モード補正を詳細に計算する。

## C.1 Poisson structure

各 canonical pair $(q_j,p_j)$ に

$$
\{q_j,p_k\}
=
\delta_{jk}
$$

を置く。messenger vector $u=(Q,P)^{\mathsf T}$ と action

$$
I=\frac12(Q^2+P^2)
$$

に対し、生成子

$$
K_{\rm rot}
=
-\theta I
$$

の unit flow は

$$
\dot Q=-\theta P,
\qquad
\dot P=\theta Q
$$

なので

$$
u(1)
=
R(\theta)u(0).
$$

$\theta=\phi(a)+\pi\chi_-(s)$ とし、seed plateau 上で $A=\sigma(s)$ とすれば

$$
R
\left[
\phi(a)+\pi\chi_-(s)
\right]
=
A R[\phi(a)].
$$

従って outcome sign を messenger phase の $\pi$ shift として canonical に記録できる。

## C.2 bright shift と anchor shift

bright pair $(x,p)$ に対する生成子

$$
K_{\rm br}
=
-x\sigma(s)
$$

は

$$
\dot p
=
-\frac{\partial K_{\rm br}}{\partial x}
=
\sigma(s),
$$

$$
\dot x
=
\frac{\partial K_{\rm br}}{\partial p}
=
0
$$

を与える。$p(0)=0$ なら $p(1)=A$ である。

anchor pair $(Y,\Pi)$ に対する

$$
K_{\rm lock}
=
-Y\zeta(p)
$$

は

$$
\dot\Pi
=
-\frac{\partial K_{\rm lock}}{\partial Y}
=
\zeta(p),
$$

$$
\dot Y=0,
\qquad
\dot p=0
$$

を与える。$\zeta(\pm1)=\pm1$ の plateau で $\Pi(0)=0$ なら、

$$
\Pi(1)=A.
$$

二つの map は Hamiltonian flow なので phase volume を保存する。bright information を local bath へ分散した後も、anchor pair を decouple すれば comparator window 中の record sign は保たれる。

## C.3 autonomous clock

clock pair $(\vartheta,J_c)$ と mutually disjoint pulse profile $f_\nu(\vartheta)$ を用い、

$$
H
=
\Omega J_c
+H_0
+\Omega
\sum_\nu
f_\nu(\vartheta)K_\nu
$$

とする。$K_\nu$ と $H_0$ が $J_c$ に依存しないとき、

$$
\dot\vartheta=\Omega.
$$

$f_\nu$ を

$$
\int_{\operatorname{supp}f_\nu}
f_\nu(\vartheta)d\vartheta=1
$$

と規格化すれば、対応する time interval で

$$
\int
\Omega f_\nu[\vartheta(t)]dt=1.
$$

従って idealized nonoverlapping limit で $K_\nu$ の unit canonical map が得られる。有限 pulse overlap は Baker--Campbell--Hausdorff expansion に従う commutator correction を生む。operator norm が有界な working region では、overlap duration を $\delta_t$ として leading error は $O(\delta_t\| \{K_\mu,K_\nu\}\|)$ で評価できる。

## C.4 相補的内部時計、二境界 matching、向き平均 no-go

まず、時計運動量を $\pm\varrho_0$ の極小へ固定するだけの Hamiltonian

$$
H_{\rm stop}
=
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
+
\frac{\lambda_c}{4}
\sum_{X=A,B}
\left(
\varrho_X^2-\varrho_0^2
\right)^2
$$

は用いない。極小

$$
\left(
\varrho_A,\varrho_B
\right)
=
\left(
+\varrho_0,-\varrho_0
\right)
$$

では

$$
\dot\tau_X
=
\frac{\partial H_{\rm stop}}{\partial\varrho_X}
=
0
$$

となり、向きは区別できても時計が進まないからである。

実際に相補的な時計運動を作る最小の二次 Hamiltonian として

$$
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
$$

を用いる。center--relative variables を

$$
\bar\tau
=
\frac{\tau_A+\tau_B}{2},
\qquad
Y_R
=
\tau_A-\tau_B,
$$

$$
P_c
=
\varrho_A+\varrho_B,
\qquad
\Pi_R
=
\frac{\varrho_A-\varrho_B}{2}
$$

と定めると、

$$
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R.
$$

従って変換は正準であり、

$$
H_{\rm or}
=
\frac{\Pi_R^2}{M_\tau}
+
\left(
\frac{1}{4M_\tau}
+
\frac{\kappa_c}{2}
\right)
P_c^2.
$$

$P_c=0$ 上では

$$
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
$$

$$
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
$$

source で $\Pi_R(0)=E_*>0$ を準備し、return generator を

$$
K_R
=
F_R(Y_R)
\left(
h-\kappa I_-
\right)
$$

とする。$K_R$ は $\bar\tau$ に依存しないので $P_c=0$ は保たれる。また $Y_R=0$、$F_R'(0)=1$ の readout orbit 上で

$$
\Delta\Pi_R
=
\kappa I_- -h,
$$

$$
\Pi_R(T)
=
E_*+\kappa I_- -h.
$$

従って

$$
\Pi_R(T)\geq0
\quad\Longleftrightarrow\quad
\varrho_A(T)\geq0
\ \hbox{and}\
\varrho_B(T)\leq0.
$$

terminal half-space は、source で選んだ時計向きの順序を保存した履歴の集合として得られる。一方、$\Pi_R(T)<0$ の軌道も正則な Hamiltonian 軌道であり、時計向きが交換されるだけである。

この half-space から `[R]` の積形式を得るには、さらに二境界の statistical matching を置く必要がある。初期境界の密度を $\rho_S(z_i)$、逆向き時計の clock-past に対応する終端関数を $G_{\rm or}(z_f)$ とし、両枝が同じ Hamiltonian 履歴を表す条件を

$$
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
$$

で課す。履歴空間上の測度を

$$
d\nu
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
$$

とすれば、$z_f$ 積分により

$$
d\nu_i
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i.
$$

これは `[R]` と同じ積形式である。Hamiltonian flow の Jacobian が1であるため、逆向きに積分しても余分な密度因子は出ない。ただし二つの境界密度を掛け、matching する規則は Hamilton 方程式とは別の all-at-once 統計原理である。

最後に、向きの順序を指定しない素朴な平均を考える。同じ scalar readout

$$
\Pi_R(T)
=
x-h,
\qquad
x
=
E_*+\kappa I_-,
$$

に対して正向き half-space を $\Pi_R(T)\geq0$、相補的 half-space を $\Pi_R(T)\leq0$ とし、$0\leq x\leq E_\ell$ で一様な $h$ を積分すると、

$$
F_+(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\leq x\}}
=
\frac{x}{E_\ell},
$$

$$
F_-(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\geq x\}}
=
1-\frac{x}{E_\ell}.
$$

両者を等重みで足せば

$$
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12
$$

となり、$I_-$ の cos dependence は消える。従って $\varrho_A=-\varrho_B$ という無向きの相補性だけでは Bell weight を保てない。順序付き boundary sector を採るか、時間反転した sector では comparator kick の符号も反転する共変な追加構造が必要である。

## C.5 difference-mode action

二つの messenger を

$$
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
$$

$$
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
$$

とする。symplectic beam splitter

$$
u_+
=
\frac{u_A+u_B}{\sqrt2},
\qquad
u_-
=
\frac{u_A-u_B}{\sqrt2}
$$

は total action を保存する。

$$
\frac12\|u_A\|^2
+\frac12\|u_B\|^2
=
\frac12\|u_+\|^2
+\frac12\|u_-\|^2.
$$

antisymmetric port の action は

$$
\frac12\|u_-\|^2
=
\frac14\|u_A-u_B\|^2
=
I_-.
$$

内積を展開して

$$
I_-
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right]
$$

を得る。この物理的 beam-splitter map を実行してから antisymmetric port の action を comparator へ結合してもよく、同じ quadratic observable へ直接結合してもよい。

## C.6 return-pointer shift

return generator

$$
K_R
=
F_R(Y_R)
\left[
h-\kappa I_-
\right]
$$

に対して

$$
\dot Y_R
=
\frac{\partial K_R}{\partial\Pi_R}
=
0.
$$

$Y_R(0)=0$ なら $Y_R(\tau)=0$ である。$F_R(0)=0$ から、readout orbit 上で

$$
\dot q_s
=
\frac{\partial K_R}{\partial p_s}
=
0,
\qquad
\dot p_s
=
-\frac{\partial K_R}{\partial q_s}
=
0
$$

となり、messenger variables も同様に動かない。一方、

$$
\dot\Pi_R
=
-F_R'(0)
\left[
h-\kappa I_-
\right].
$$

$F_R'(0)=1$、$\Pi_R(0)=E_*$ なら

$$
\Pi_R(1)
=
E_*+\kappa I_- -h.
$$

従って comparator は $I_-$ と $h$ を破壊せずに差だけを pointer へ記録する。

## C.7 二モード作用殻の正規化

二つの action-angle pair に対し、

$$
\mathcal N(E_\ell)
=
\int_0^\infty
dJ_s
\int_0^{2\pi}
d\theta_s
\int_0^\infty
dJ_0
\int_0^{2\pi}
d\theta_0
\delta
\left[
E_\ell-\omega_\ell(J_s+J_0)
\right].
$$

$J_0$ を積分すると

$$
\mathcal N(E_\ell)
=
\frac{(2\pi)^2}{\omega_\ell}
\int_0^{E_\ell/\omega_\ell}
dJ_s
=
\frac{(2\pi)^2E_\ell}{\omega_\ell^2}.
$$

$h=\omega_\ell J_s$ の interval $[h,h+dh]$ に入る shell measure は

$$
d\mathcal N_h
=
\frac{(2\pi)^2}{\omega_\ell^2}dh.
$$

従って

$$
p_\ell(h)dh
=
\frac{d\mathcal N_h}{\mathcal N(E_\ell)}
=
\frac{dh}{E_\ell}.
$$

equivalently、rescaled Cartesian coordinate

$$
\frac1{\sqrt{2J_\ell}}
\left(
q_s,p_s,q_0,p_0
\right)
$$

は3-sphere $S^3$ 上にあり、

$$
\frac{J_s}{J_\ell}
=
\frac{q_s^2+p_s^2}{
q_s^2+p_s^2+q_0^2+p_0^2
}
$$

は Beta$(1,1)$、すなわち $[0,1]$ 上の一様分布である。

## C.8 mixer generators

次を定義する。

$$
J_x=q_sq_0+p_sp_0,
$$

$$
J_y=q_sp_0-p_sq_0,
$$

$$
J_z=\frac12
\left(
q_s^2+p_s^2-q_0^2-p_0^2
\right),
$$

$$
J_\ell
=
\frac12
\left(
q_s^2+p_s^2+q_0^2+p_0^2
\right).
$$

Poisson bracket を直接計算すると、

$$
\{J_\ell,J_i\}=0,
\qquad
i=x,y,z.
$$

また、規格化の取り方に応じた定数因子を除き、$J_x,J_y,J_z$ は $\mathfrak{su}(2)$ 型の閉じた bracket を持つ。従って

$$
K_M
=
a_x(t)J_x+a_y(t)J_y+a_z(t)J_z
$$

の各 flow は $S^3$ 上の measure-preserving orientation map である。係数 $a_i(t)$ を有限 nonlinear environment と autonomous clock から生成すれば、全系を Hamiltonian に保ったまま複雑な orientation dynamics を作れる。

この事実は $p(h)$ の invariant reference measure を保証するが、特定の deterministic coefficient sequence が mixing であることを自動的には保証しない。mixing rate は別途 correlation decay または transfer-operator spectrum で検証する必要がある。

## C.9 多モード simplex marginal

soft energy $h$ と $N$ 個の ledger energy $e_1,\ldots,e_N$ が

$$
h+\sum_{j=1}^{N}e_j=E_\ell
$$

を満たすとする。各 harmonic pair の phase angle を積分すると定数になる。$h$ を固定した残余 simplex

$$
\sum_{j=1}^{N}e_j=E_\ell-h,
\qquad
e_j\geq0
$$

の surface multiplicity は

$$
\frac{(E_\ell-h)^{N-1}}{(N-1)!}
$$

に比例する。規格化から

$$
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1}.
$$

cumulative distribution は

$$
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
$$

$N=1$ でのみ linear である。$x=C-ABKc$ と書けば、

$$
F_N(C-ABKc)
=
1-
\sum_{m=0}^{N}
\binom Nm
\left(
1-\frac C{E_\ell}
\right)^{N-m}
\left(
\frac{ABKc}{E_\ell}
\right)^m.
$$

偶数 $m$ は outcome parity に依存しない normalization correction、奇数 $m\geq3$ は $c^3,c^5,\ldots$ を通じて higher angular harmonics を生む。従って extra ledger modes は単なる visibility renormalization ではない。

## C.10 finite terminal width

sharp indicator を monotone response $g_\epsilon$ へ置き換える。

$$
G_{R,\epsilon}
=
g_\epsilon
\left(
E_*+\kappa I_- -h
\right).
$$

一様 soft density に対する compatibility は

$$
F_\epsilon(x)
=
\frac1{E_\ell}
\int_0^{E_\ell}
g_\epsilon(x-h)dh.
$$

$g_\epsilon$ が Heaviside function と symmetric smoothing kernel の convolution なら、

$$
\frac{dF_\epsilon}{dx}
=
\frac1{E_\ell}
\left[
g_\epsilon(x)-g_\epsilon(x-E_\ell)
\right].
$$

内部領域

$$
\epsilon\ll x\ll E_\ell-\epsilon
$$

では $g_\epsilon(x)\approx1$、$g_\epsilon(x-E_\ell)\approx0$ なので、

$$
\frac{dF_\epsilon}{dx}
\approx
\frac1{E_\ell}.
$$

endpoint 近傍でのみ slope と offset が変わる。従って $E_*$ は zero channel を boundary layer から離す一方、visibility を低下させる。

## C.11 forward-bath no-go

記録形成後の四 sector を $\Gamma_{AB}$ とし、共通浴を含む後段 flow を $\Psi^t$ とする。Liouville measure に関して

$$
\mu(\Psi^t\Gamma_{AB})
=
\int_{\Psi^t\Gamma_{AB}}d\Gamma
=
\int_{\Gamma_{AB}}
\left|
\det D\Psi^t
\right|
d\Gamma.
$$

Hamiltonian flow では

$$
\det D\Psi^t=1
$$

なので

$$
\mu(\Psi^t\Gamma_{AB})
=
\mu(\Gamma_{AB}).
$$

従って future bath coupling は forward ensemble の sector mass を変えない。terminal conditioning を加えると

$$
\mu_R(\Gamma_{AB})
\propto
\int_{\Gamma_{AB}}
G_R(\Psi^T z)
d\mu(z)
$$

となり、sector mass は変わり得る。しかし変化を生むのは bath noise の leakage そのものではなく、future flow と $G_R$ を組み合わせた boundary reweighting である。

## C.12 algebraic consistency checks

実装の最小 check は次である。

1. random angle と sign について、直接計算した $\|u_A-u_B\|^2/4$ と analytic $I_-$ を比較する。
2. $S^3$ 上の isotropic Gaussian vector を規格化し、$J_s/J_\ell$ の empirical CDF と uniform CDF を比較する。
3. $\Pi_R(0)=E_*$ と $\Delta\Pi_R=\kappa I_- -h$ から、相補時計の終端向き条件を検算する。
4. $h\leq E_*+\kappa I_-$ の indicator を Monte Carlo 積分し、analytic $W_{AB}$ と比較する。
5. 四 outcome を規格化し、marginal residual と CHSH を計算する。
6. $F_+(x)+F_-(x)=1$ を検算し、等重み orientation average で cos 項が消えることを確認する。
7. extra ledger modes を追加し、predicted $F_N(x)$ と higher harmonics を比較する。

これらは Hamiltonian mixing の証明ではない。幾何、normalization、sampling implementation に循環または符号誤りがないことを確認する代数的検証である。
