@number: A5
@chapter: 付録
@title: 測定依存度、CHSH 四設定、postselection 監査
@status: 第II部の Bell 分類を定量化し、装置 posterior と表現論的最小値を区別する。

## E.1 Hall scale

setting-dependent hidden distribution に対する Hall の $L^1$ scale を

$$
M
=
\sup_{a,b,a',b'}
\int
\left|
\rho(\lambda\mid a,b)
-\rho(\lambda\mid a',b')
\right|
d\lambda
$$

とする。通常の total variation とは

$$
M=2D_{\rm TV}^{\max}
$$

の関係にある。

第7.6節の最小 two-mode posterior では、

$$
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
$$

なので、

$$
M_{\rm dev}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-\cos\Delta_{a'b'}
\right|.
$$

全角度を許せば

$$
M_{\rm dev}=2V_{\rm eff}.
$$

標準 CHSH の四 setting pair では cosine が $\pm1/\sqrt2$ なので、

$$
M_{\rm dev}^{(4)}
=
\sqrt2V_{\rm eff}.
$$

これは本文の具体的 device posterior が持つ値であり、同じ observable joint law を再現する全 local model の中で最小化した値ではない。

## E.2 ledger-only representation

hidden variable を

$$
\lambda_{\rm tab}
=
(A_*,B_*)
\in
\{\pm1\}^2
$$

とし、

$$
\mathscr A(a,\lambda_{\rm tab})=A_*,
\qquad
\mathscr B(b,\lambda_{\rm tab})=B_*,
$$

$$
\rho_{\rm tab}(A_*,B_*\mid a,b)
=
\frac14
\left[
1-A_*B_*V_{\rm eff}\cos\Delta_{ab}
\right]
$$

と置けば、local deterministic に目標 joint law を再現する。この representation は出力確率を hidden ledger に直接書き込んだものであり、物理的説明ではない。

Hall scale は

$$
M_{\rm tab}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-\cos\Delta_{a'b'}
\right|
$$

である。従って two-mode device posterior の coarse marginal と同じ値を持つ。この一致は装置構成の最適性を意味せず、両者が同じ support-length modulation を使っていることを示す。

## E.3 標準 CHSH 四設定の最小値

標準 CHSH 四設定に対し、目標 visibility $V_{\rm eff}$ を再現する local deterministic、operationally no-signalling representation 全体で Hall scale を最小化した値を $M_{\min}^{(4)}(V_{\rm eff})$ とする。

$V_{\rm eff}\leq1/\sqrt2$ では全 CHSH inequality が満たされる。Fine の定理により setting-independent joint hidden distribution が存在するので [38]、

$$
M_{\min}^{(4)}(V_{\rm eff})
=
0,
\qquad
0\leq V_{\rm eff}\leq\frac1{\sqrt2}.
$$

$V_{\rm eff}>1/\sqrt2$ では、Hall の relaxed CHSH bound

$$
|\mathcal S|
\leq
2+\min\{3M,2\}
$$

と

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}
$$

から

$$
M_{\min}^{(4)}(V_{\rm eff})
\geq
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
$$

を得る [9]。

この bound は、$V_{\rm eff}=1/\sqrt2$ の setting-independent Fine model と、$V_{\rm eff}=1$ で bound を saturate する Hall model を setting-independent flag で混合することで達成できる。従って

$$
M_{\min}^{(4)}(V_{\rm eff})
=
\max
\left\{
0,
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
\right\}.
$$

特に $V_{\rm eff}=1$ では

$$
M_{\min}^{(4)}
=
\frac{
2(\sqrt2-1)
}{3},
$$

一方、本文の device posterior は

$$
M_{\rm dev}^{(4)}=\sqrt2.
$$

従って明示 device は measurement-dependence resource について最適でない。

この最小値は四つの観測分布に対する representation-theoretic quantity である。finite Hamiltonian apparatus が同じ最小値を実現できることを意味しない。全角度の cosine family に対する device-constrained minimum も本論文では求めない。

## E.4 setting frequency と source posterior

controller prior を $P_S(a,b)$ とし、full boundary measure を controller まで含めて規格化すると、

$$
P_R(a,b)
=
\frac{
P_S(a,b)Z_{a,b}
}{
\sum_{a',b'}
P_S(a',b')Z_{a',b'}
}.
$$

本文の symmetric model では

$$
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
$$

が一定なので、

$$
P_R(a,b)=P_S(a,b).
$$

従って macroscopic setting frequency の自由と microscopic source posterior の setting dependence は両立する。これは measurement independence failure と、実験者が controller macrostate を変えられないという主張を区別する。

## E.5 launch count、record count、completion count

各 setting pair について次の三つの数を区別する。

1. external source が開始した launch count $N_{\rm launch}$。
2. 左右 pointer が definite result を持った record count $N_{\rm rec}$。
3. terminal apparatus が ready macroregion に入った completion count $N_R$。

boundary ontology `[R]` では、物理的に実現する trial 自体が terminal-compatible history であると解釈する。しかし laboratory implementation が単に

$$
N_R<N_{\rm rec}
$$

となる trial rejection を行うなら、observed sample は

$$
P_{\rm obs}(A,B\mid a,b)
=
\frac{
P_{\rm rec}(A,B\mid a,b)
\eta_{AB}(a,b)
}{
\sum_{A',B'}
P_{\rm rec}(A',B'\mid a,b)
\eta_{A'B'}(a,b)
}
$$

という detector-conditioned distribution になる。$\eta_{AB}$ は completion efficiency である。この場合、Bell violation は detection loophole で説明され得る。

従って physical boundary model と postselection を区別する最低条件は、

- 全 launch、record、completion count を setting ごとに報告する。
- outcome-dependent missing fraction を零または独立に有界化する。
- terminal device の calibration を Bell run より前に固定する。
- timeout を変えても、predicted finite-width correction 以外の joint-law drift がないことを確かめる。

である。

## E.6 biased preparation test

seed preparation apparatus を追加し、基準 sector weight $w_{AB}$ を操作する。本文模型が arbitrary preparation に対して operationally viable なら、次のいずれかが観測されなければならない。

1. $w_{AB}$ の操作が boundary compatibility によって自動的に相殺される。
2. biased macrostate が物理的に準備不能になる。
3. no-signalling residual が増大する。

no-signalling residual を

$$
\epsilon_{\rm NS}
=
\max_{a,b,b',A}
\left|
P_R(A\mid a,b)
-P_R(A\mid a,b')
\right|
$$

とする。ideal `[S]` ensemble では $\epsilon_{\rm NS}=0$ である。biased preparation に対し $\epsilon_{\rm NS}=O(1)$ が現れれば、equilibrium-only model の操作的限界が直接検出される。
