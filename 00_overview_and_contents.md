@number: 3
@chapter: 第3章
@title: 二側 Hamilton 履歴測度と測定独立性
@status: [F|R] 有限 Hamilton flow の terminal compatibility と measurement-independence 判定。

## 3.1 全初期状態と setting controller

初期 hypersurface 上の全 microstate を

$$
z_i=(\lambda,\eta,\xi_A,\xi_B)
$$

とする。$\lambda$ は setting label を除く Bell-complete data、$\eta$ は後に積分される soft return mode、clock、未読 apparatus coordinate、$\xi_A,\xi_B$ は setting controller の microstate である。coarse map

$$
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
$$

により実験設定を定める。

基準初期 ensemble では、source と setting controller を統計的に独立に準備する。

$$
\rho_0(\lambda,\eta,\xi_A,\xi_B)
=
\rho_0(\lambda,\eta)
\rho_A(\xi_A)
\rho_B(\xi_B).
$$

これは `[R]` を適用する前の preparation statement である。controller macroregion $(a,b)$ に条件づけた後の有限 Hamilton flow を $\Phi_{a,b}^t$ と書く。実際には全設定で同じ Hamiltonian function を用い、controller の初期 macrostate だけを変える。下付き $a,b$ はこの条件付き flow を簡潔に表す記法である。

## 3.2 固定 terminal rule

終端時刻 $T$ における非負関数を

$$
G_R:\Gamma\longrightarrow[0,\infty)
$$

とする。中心的制約は、$G_R$ の関数形を全設定と全 outcome に共通に固定することである。従って

$$
G_R=G_R(z_T)
$$

であり、$G_R(a,b,A,B)$ のような label dependence を許さない。

`[R]` による二側履歴測度は

$$
d\mu_R^{a,b}(\lambda,\eta)
=
\frac{
\rho_0(\lambda,\eta)
G_R[\Phi_{a,b}^{T}(\lambda,\eta)]
}{Z_{a,b}}
d\lambda\,d\eta,
$$

$$
Z_{a,b}
=
\int
\rho_0(\lambda,\eta)
G_R[\Phi_{a,b}^{T}(\lambda,\eta)]
d\lambda\,d\eta
$$

である。これは有限次元の通常の正の条件付き測度である。未来から追加の非 Hamiltonian force を加えるのではなく、同じ Hamilton trajectories のどれに物理的 measure を置くかを両端条件で指定する。

## 3.3 terminal compatibility

$\lambda$ を固定したとき、未読変数 $\eta$ を積分した compatibility を

$$
h_{a,b}(\lambda)
=
\int
\rho_0(\eta\mid\lambda)
G_R[\Phi_{a,b}^{T}(\lambda,\eta)]
d\eta
$$

と定義する。このとき source hypersurface 上の posterior は

$$
\rho_R(\lambda\mid a,b)
=
\frac{
\rho_0(\lambda)
h_{a,b}(\lambda)
}{Z_{a,b}},
$$

$$
Z_{a,b}
=
\int
\rho_0(\lambda)
h_{a,b}(\lambda)
d\lambda
$$

となる。

$h_{a,b}$ は任意に置く hidden-variable distribution ではない。固定した $G_R$、具体的な Hamilton flow、未読 apparatus の基準密度から計算する量である。本論文の明示模型では、第4章の comparator と第5章の soft-mode 積分から直接求める。

## 3.4 測定独立性保存の必要十分条件

\begin{theorem}[terminal compatibility criterion]
全設定対に対して同一の posterior $\rho_R(\lambda)$ が存在するための必要十分条件は、ある非負関数 $h(\lambda)$ と正定数 $c_{a,b}$ が存在して

$$
h_{a,b}(\lambda)
=
c_{a,b}h(\lambda)
$$

がほとんど至る所で成立することである。
\end{theorem}

Proof. 上式が成立すれば $c_{a,b}$ は $Z_{a,b}$ による規格化で消え、posterior は全設定で同じになる。逆に posterior が全設定で同じなら

$$
\frac{h_{a,b}(\lambda)}{Z_{a,b}}
=
\frac{h_{a',b'}(\lambda)}{Z_{a',b'}}
$$

なので、$h_{a,b}$ は共通関数へ比例する。特に基準分布 $\rho_0(\lambda)$ 自体を保つには、$h_{a,b}(\lambda)$ が $\lambda$ に依存しないことが必要である。

従って、ある設定対について

$$
\frac{h_{a,b}(\lambda)}{h_{a',b'}(\lambda)}
$$

が $\lambda$ に依存すれば、measurement independence は破れている。

## 3.5 どの操作が依存性を生むか

一試行の操作を次に分ける。

- $S$：source preparation。
- $M_A(a),M_B(b)$：局所 analyzer。
- $D_A,D_B$：局所 pointer recording。
- $P$：messenger propagation。
- $C$：common-future comparison。
- $G_R$：fixed terminal condition。

$S$ の基準 measure は setting-independent に取る。局所 analyzer は軌道を setting-dependent にするが、前向き Liouville ensemble の source marginal を遡って変えない。pointer recording は軌道を disjoint outcome region へ写すが、それだけでは再重みづけを起こさない。common-future comparison は setting と outcome sign を terminal coordinate に集めるが、$G_R$ が定数なら $h_{a,b}=1$ である。

従って measurement independence failure を生む最小の合成は

$$
G_R\circ C\circ P\circ D_B\circ D_A
\circ M_B(b)\circ M_A(a)\circ S
$$

である。局所測定 pulse 単独ではなく、設定情報を terminal coordinate へ運ぶ Hamilton operation と、その coordinate に対する二側 conditioning の合成が本質である。

## 3.6 局所 deterministic response

$\lambda$ に source seed と局所 apparatus microstate をすべて含める。分離後の coupling graph が局所なら

$$
A=A_a(\lambda),
\qquad
B=B_b(\lambda)
$$

であり、fixed $\lambda$ における応答は

$$
P(A,B\mid a,b,\lambda)
=
\delta_{A,A_a(\lambda)}
\delta_{B,B_b(\lambda)}
$$

と因子化する。

Bell の導出が使えない理由は、この局所応答ではなく、平均に用いる分布が

$$
\rho_R(\lambda\mid a,b)
$$

と設定ごとに異なるためである。第4章の最小模型では全設定に共通 support を持たせるため、response の counterfactual definition 自体は維持できる。

## 3.7 setting の操作的自由

measurement dependence

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda)
$$

は、実験者が $P(a,b)$ を変更できないことを意味しない。実験者は局所 controller の macrostate 分布を変更できる。ただし `[R]` の下では、変更した controller macrostate と両立する full histories の microscopic source distribution が変化する。

全履歴を一つの block として解く記述では、設定は boundary-value problem の controllable input、source microstate はその入力に条件づけられた未知量である。この意味で本模型は future-input dependent または retrocausal class に属する [6--9]。時間を逆向きに流れる局所 force を仮定する必要はない。

## 3.8 setting frequency の保護

`[R]` を controller を含む全 ensemble へ適用すると、setting macrostate 自体の頻度は

$$
P_R(a,b)
\propto
P_0(a,b)Z_{a,b}
$$

となる。従って実験者が指定した setting distribution を保つには、理想的には

$$
Z_{a,b}=Z
$$

が全設定で成立する必要がある。

第5章の sign-symmetric 模型では

$$
\sum_{A,B}I_-(A,B;a,b)
$$

が設定に依存しないため、この条件が厳密に満たされる。microscopic source posterior は設定依存でも、macroscopic setting frequency は変化しない。

## 3.9 measurement dependence の量

二設定対間の全変動距離を

$$
D_{\rm TV}
\bigl[(a,b),(a',b')\bigr]
=
\frac12
\int
\left|
\rho_R(\lambda\mid a,b)
-
\rho_R(\lambda\mid a',b')
\right|d\lambda
$$

とする。setting prior が指定される場合は mutual information

$$
I_R(\lambda:a,b)
$$

も計算する [5]。明示模型における $D_{\rm TV}$ は第6章で解析的に求める。

## 3.10 postselection 監査

数式

$$
\rho_R\propto\rho_0G_R
$$

だけでは、物理的 boundary ensemble と実験後の rejection sampling を区別できない。区別は操作的構成に置かなければならない。本論文では次を要求する。

1. $G_R$ は trial の outcome を観測する前に、apparatus の terminal macroregion として固定される。
2. 全 setting と全 outcome に同じ terminal device と分解能を用いる。
3. 観測データから trial を除外せず、全 pointer record を共同確率へ含める。
4. terminal geometry を Bell data とは独立の calibration で決める。
5. setting-dependent acceptance rate が hidden detector loophole になっていないことを検査する。

これらを満たせない場合、模型は物理的 explanation ではなく、相関式を埋め込んだ postselection scheme に留まる。

## 3.11 本章の結論

固定 terminal function であっても、その Hamiltonian pullback は setting-dependent になり得る。測定独立性が保たれるのは terminal compatibility が全設定で共通関数へ比例する特殊な場合だけである。次章では、この一般構造を実現する全 canonical variables と Hamiltonian を書き下す。
