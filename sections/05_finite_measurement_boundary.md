@number: 5
@chapter: 本文
@title: 有限 Hamiltonian 測定器と時間対称境界集団
@status: 局所 definite record と全履歴測度を分離し、`[R]` を第II部の確率原理として明示する。

## 5.1 第II部の目的

第2章から第4章は、観測座標の線形 Gaussian 経路法則と Nelson 作用を扱った。そこから Bell 型結果重みは出ない。Bell 実験を記述するには、少なくとも次の構造が必要である。

1. 左右の setting controller。
2. 局所的に確定する2値 record。
3. 設定と結果符号を共通未来へ運ぶ messenger。
4. 二つの messenger を比較する setting-blind な二次形式。
5. 比較結果と未読台帳変数を照合する terminal coordinate。
6. terminal-compatible histories を物理的集団とする境界統計原理。

本章では1、2、3、5、6を有限 Hamiltonian 系として定式化する。比較器の cos 幾何と二モード台帳は第6章、共同確率は第7章で扱う。

## 5.2 正準変数

一試行の第II部に必要な正準変数を次のように取る。

- messenger pairs：$(Q_A,P_A)$、$(Q_B,P_B)$。
- outcome-seed pairs：$(s_A,\pi_A)$、$(s_B,\pi_B)$。
- setting-controller pairs：$(a,\alpha)$、$(b,\beta)$。
- bright response pairs：$(x_A,p_A)$、$(x_B,p_B)$。
- anchor-pointer pairs：$(Y_A,\Pi_A)$、$(Y_B,\Pi_B)$。
- local finite-bath pairs：$(r_{Xj},\varpi_{Xj})$、$X=A,B$、$1\leq j\leq n_X$。
- ledger pairs：$(q_s,p_s)$、$(q_0,p_0)$。
- return-comparator pair：$(Y_R,\Pi_R)$。
- complementary-clock center pair：$(\bar\tau,P_c)$。
- autonomous-clock pair：$(\vartheta,J_c)$。

messenger action を

$$
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
X=A,B
$$

とする。ledger の二つの作用は

$$
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
$$

$$
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right)
$$

である。全 Hamiltonian の構造は

$$
H_{\rm tot}
=
H_{\rm src}
+H_{\rm ctrl}
+H_{\rm msg}
+H_{\rm seed}
+H_{\rm ptr}
+H_{\rm bath}
+H_\ell
+H_{\rm mix}
+H_{\rm cmp}
+H_{\rm or}
+H_{\rm clk}.
$$

各項の具体形は付録Cにまとめる。本章では各操作を有限時間の canonical map として明示する。

## 5.3 outcome seed と設定 controller

$s_X$ を circle coordinate とし、互いに等しい Liouville 体積を持つ二つの plateau region $\Sigma_X^+$、$\Sigma_X^-$ を取る。滑らかな周期関数 $\sigma$ を

$$
\sigma(s)
=
+1
\qquad
\left(
s\in\Sigma^+
\right),
$$

$$
\sigma(s)
=
-1
\qquad
\left(
s\in\Sigma^-
\right)
$$

とし、二領域の間だけで滑らかに補間する。基準 preparation は補間領域に support を持たない。従って実際の support 上で

$$
\sigma'(s)=0.
$$

局所結果を

$$
A=\sigma(s_A),
\qquad
B=\sigma(s_B)
$$

とする。負符号 sector の indicator は

$$
\chi_-(s)
=
\frac{1-\sigma(s)}2
$$

である。

setting は controller coordinate の初期 macroregion で決まる。全試行に同じ Hamiltonian function を用い、

$$
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
$$

という coarse map で設定を読み出す。以下では controller coordinate 自体を簡単に $a,b$ と書く。

この最小模型では outcome seed を明示的に置く。より一般の局所決定論 response

$$
A=\mathscr A(a,\lambda_A),
\qquad
B=\mathscr B(b,\lambda_B)
$$

も、局所 canonical preprocessing の後に同じ plateau record へ写せる。Bell 監査に必要なのは、fixed complete microstate における左の response が右の setting を参照せず、右も同様であることだけである。

## 5.4 autonomous pulse Hamiltonian

clock angle $\vartheta$ 上に、互いに重ならない滑らかな profile $f_\nu(\vartheta)$ を置き、

$$
\int f_\nu(\vartheta)d\vartheta=1
$$

と規格化する。全 Hamiltonian に

$$
H_{\rm clk}
=
\Omega J_c
$$

と pulse 項

$$
H_{\rm pulse}
=
\Omega
\sum_\nu
f_\nu(\vartheta)K_\nu
$$

を加える。各 $K_\nu$ は $J_c$ に依存しないため、

$$
\dot\vartheta
=
\frac{\partial H_{\rm tot}}{\partial J_c}
=
\Omega
$$

が厳密に成立する。従って各 profile は生成子 $K_\nu$ の unit flow を実行する。clock action $J_c$ が pulse の backreaction を吸収し、拡張した全 Hamiltonian energy は保存される。

この自律化は、外部から setting ごとに異なる Hamiltonian を挿入する操作ではない。setting は phase space 内の controller state、操作順序は同じ clock orbit 上の異なる区間である。$(\vartheta,J_c)$ は pulse scheduler であり、第5.9節で導入する相補的内部時計ではない。両者を同一視すると、内部時計を逆向きに動かす Hamiltonian へ替えたときに pulse の単調な順序づけが失われるため、独立な canonical pair として保持する。

## 5.5 局所 analyzer と bright response

A 側の analyzer generator を

$$
K_A^{\rm an}
=
-\left[
\phi(a)
+\pi\chi_-(s_A)
\right]I_A
-x_A\sigma(s_A)
$$

とし、B 側も同様に

$$
K_B^{\rm an}
=
-\left[
\phi(b)
+\pi\chi_-(s_B)
\right]I_B
-x_B\sigma(s_B)
$$

とする。

$K_A^{\rm an}$ の unit flow parameter を $\tau$ とすると、seed plateau 上で

$$
\frac{dQ_A}{d\tau}
=
-\theta_A P_A,
\qquad
\frac{dP_A}{d\tau}
=
\theta_A Q_A,
$$

$$
\theta_A
=
\phi(a)+\pi\chi_-(s_A),
$$

および

$$
\frac{dp_A}{d\tau}
=
\sigma(s_A)=A,
\qquad
\frac{dx_A}{d\tau}=0
$$

を得る。bright momentum を $p_A^{\rm in}=0$ に準備すれば、

$$
p_A^{\rm out}=A.
$$

messenger は

$$
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm out}
=
R[\theta_A]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
=
A R[\phi(a)]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
$$

となる。B 側も

$$
p_B^{\rm out}=B,
$$

$$
u_B^{\rm out}
=
B R[\phi(b)]u_B^{\rm in}
$$

を満たす。

bright mode は setting pulse と local seed に強く応答する一時変数である。outcome probability を生成する浴ではない。各 trajectory の $A,B$ は seed と局所 Hamiltonian flow で一意に決まる。

## 5.6 anchor pointer への記録固定

滑らかな plateau function $\zeta(p)$ を

$$
\zeta(p)=+1
\quad
\left(
|p-1|<\delta_p
\right),
$$

$$
\zeta(p)=-1
\quad
\left(
|p+1|<\delta_p
\right)
$$

となるよう取る。anchor transfer generator を

$$
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
$$

とする。unit flow では

$$
\frac{d\Pi_X}{d\tau}
=
\zeta(p_X),
\qquad
\frac{dY_X}{d\tau}=0,
\qquad
\frac{dp_X}{d\tau}=0.
$$

従って $\Pi_X^{\rm in}=0$ なら

$$
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B.
$$

二つの disjoint macroregion

$$
\Gamma_X^+
=
\left\{
\Pi_X>\frac12
\right\},
\qquad
\Gamma_X^-
=
\left\{
\Pi_X<-\frac12
\right\}
$$

を pointer record とする。anchor pair はこの後の common-future comparator から decouple される。従って comparison stage は過去の pointer sign を変更しない。

bright mode には、記録後に有限局所浴

$$
H_{{\rm bath},X}
=
\sum_{j=1}^{n_X}
\left[
\frac{\varpi_{Xj}^2}{2m_{Xj}}
+\frac{m_{Xj}\omega_{Xj}^2r_{Xj}^2}{2}
\right]
+\epsilon_X x_X
\sum_{j=1}^{n_X}
c_{Xj}r_{Xj}
$$

を結合できる。これは bright transient と位相情報を複数自由度へ分散し、有限観測窓での再読出し誤差を小さくする。ただし有限閉鎖浴は真の散逸を与えず、十分長時間では recurrence を持つ。record の主張は

$$
\tau_{\rm lock}
\ll
\tau_{\rm cmp}
\ll
T_{{\rm rec},X}
$$

の範囲に限る。

## 5.7 common-future propagation

局所記録時刻を $t_A,t_B$、両 messenger が同じ時空領域へ到達できる時刻を $t_C$、terminal time を $T$ とし、

$$
t_A,t_B<t_C<T
$$

とする。$t_C$ より前の coupling graph は

$$
(u_A,s_A,a,x_A,Y_A,\Gamma_{{\rm bath},A})
$$

と

$$
(u_B,s_B,b,x_B,Y_B,\Gamma_{{\rm bath},B})
$$

に分離する。A 側の Hamiltonian は B 側の setting、seed、pointer を含まず、B 側も同様である。

$t_C$ 以後に二つの messenger を同じ comparator へ入れる。これは局所記録後の timelike common future における通常の相互作用であり、spacelike separated な記録形成へ遠隔 force を導入しない。第7章で現れる setting dependence は、common-future interaction 自体が過去を変更するためではなく、その interaction を含む全軌道に terminal boundary measure `[R]` を適用するためである。

## 5.8 terminal function と履歴測度

初期 hypersurface 上の全 microstate を

$$
z_i=(\lambda,\eta,\xi_A,\xi_B)
$$

とする。$\lambda$ は outcome response を完結させる source と局所装置の変数、$\eta$ は後に積分する ledger、mixer、return pointer などの未読変数、$\xi_A,\xi_B$ は setting controller である。基準準備では

$$
\rho_S(\lambda,\eta,\xi_A,\xi_B)
=
\rho_S(\lambda,\eta)
\rho_A(\xi_A)
\rho_B(\xi_B)
$$

とする。

終端時刻 $T$ に、全設定と全 outcome に共通な非負関数

$$
G_R:\Gamma\longrightarrow[0,\infty)
$$

を固定する。`[R]` による条件付き履歴測度は

$$
d\mu_R^{a,b}(\lambda,\eta)
=
\frac{
\rho_S(\lambda,\eta)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
}{
Z_{a,b}
}
d\lambda\,d\eta.
$$

$\lambda$ を固定して未読変数を積分した terminal compatibility を

$$
h_{a,b}(\lambda)
=
\int
\rho_S(\eta\mid\lambda)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
d\eta
$$

と定義すると、source hypersurface 上の posterior は

$$
\rho_R(\lambda\mid a,b)
=
\frac{
\rho_S(\lambda)h_{a,b}(\lambda)
}{
Z_{a,b}
}
$$

となる。

\begin{proposition}[terminal compatibility criterion]
全 setting pair に対して同一の posterior $\rho_R(\lambda)$ が存在するための必要十分条件は、ある非負関数 $h(\lambda)$ と正定数 $c_{a,b}$ が存在して

$$
h_{a,b}(\lambda)
=
c_{a,b}h(\lambda)
$$

がほとんど至る所で成立することである。
\end{proposition}

Proof. 上式が成立すれば $c_{a,b}$ は規格化で消える。逆に posterior が全 setting で同じなら、

$$
\frac{h_{a,b}(\lambda)}{Z_{a,b}}
=
\frac{h_{a',b'}(\lambda)}{Z_{a',b'}}
$$

なので、各 compatibility は共通関数へ比例する。

従って固定した $G_R$ であっても、その Hamiltonian pullback

$$
G_R\circ\Phi_{a,b}^{T}
$$

が source variable を setting-dependent に再重みづけし得る。

## 5.9 相補的内部時計による terminal half-space の正準実現

return pair $(Y_R,\Pi_R)$ に center pair $(\bar\tau,P_c)$ を加え、二つの内部時計対を

$$
\tau_A
=
\bar\tau+\frac{Y_R}{2},
\qquad
\tau_B
=
\bar\tau-\frac{Y_R}{2},
$$

$$
\varrho_A
=
\frac{P_c}{2}+\Pi_R,
\qquad
\varrho_B
=
\frac{P_c}{2}-\Pi_R
$$

で定める。実際、

$$
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R
$$

なので、これは正準変換である。

内部時計の自由 Hamiltonian を

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

とする。center--relative 変数では

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

相補的 sector

$$
P_c=0
$$

は自由運動と、$\bar\tau$ に依存しない comparator pulse の双方で保存される。この sector では

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

従って $\Pi_R>0$ は A 時計が正向き、B 時計が負向きの順序付き相補性を表す。これは二粒子が実験室時刻に対して逆向きに伝播するという意味ではない。左右の粒子と messenger は通常どおり source から局所測定器、共通未来へ進み、反対になるのは内部時計または境界情報の向きである。

\begin{proposition}[terminal half-space の相補時計実現]
$P_c=0$、$\Pi_R(0)=E_*>0$ とし、comparator pulse が

$$
\Delta\Pi_R
=
\kappa I_- -h
$$

を与えるとする。このとき

$$
\Pi_R(T)
=
E_*+\kappa I_- -h.
$$

順序付き時計向きが終端まで保存される条件

$$
\varrho_A(T)\geq0,
\qquad
\varrho_B(T)\leq0
$$

は

$$
\Pi_R(T)\geq0
$$

と必要十分である。
\end{proposition}

これにより $\Pi_R$ は任意の return momentum ではなく二時計の相対運動量、$E_*$ は時計向きが反転するまでの初期 momentum margin、$G_R=\mathbf1_{\{\Pi_R(T)\geq0\}}$ は順序付き向き保存条件と読める。

ただし Hamilton 方程式は $\Pi_R(T)<0$ の軌道を禁止しない。この軌道では

$$
\varrho_A(T)<0,
\qquad
\varrho_B(T)>0
$$

となり、時計向きが交換されるだけである。従って相補的時計は terminal half-space の形を導くが、その半空間に入る履歴だけを物理的 ensemble とする `[R]` までは導かない。

## 5.10 `[R]` と postselection

数式上、

$$
\rho_R
\propto
\rho_S G_R\circ\Phi^T
$$

は、実験後の rejection sampling と同じ条件付き確率に見える。本論文が `[R]` を境界 ontology として用いるためには、少なくとも次を要求する。

1. $G_R$ は Bell data を見る前に apparatus の terminal macroregion として固定する。
2. 全 setting と全 outcome に同じ terminal device と分解能を用いる。
3. 実現した pointer record を後から除外しない。
4. terminal width、ledger energy、comparator scale を独立 calibration で決める。
5. external launch count、pointer record count、terminal completion count の関係を報告する。

これらを満たせず、観測済み trial の一部を捨てて初めて Bell 値が出るなら、本構成は detector postselection に退化する。`[R]` を公理として書くだけではこの操作的区別は自動的に保証されない。

## 5.11 本章の結論

局所 analyzer、bright response、anchor record、有限局所浴、setting messenger、common-future propagation、terminal boundary measure を有限正準系の中に配置した。各履歴の outcome は局所 Hamiltonian flow で definite であり、common-future apparatus は記録後にのみ作動する。さらに return pair を相補的内部時計の相対 pair として正準実現し、terminal half-space を順序付き時計向き保存条件として解釈した。

一方、結果頻度を定める原理は局所浴の散逸、pointer の保持時間、comparison の速度、または時計相補性だけではない。物理的 ensemble を定める `[R]` と、次章で導く terminal compatibility の位相体積である。
