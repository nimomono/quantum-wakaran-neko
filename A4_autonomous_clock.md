@number: 6
@chapter: 第6章
@title: Bell 前提、no-signalling、CHSH、preparability
@status: [F|R|E|P] Bell audit。[O] equilibrium preparation の操作的閉鎖性。

## 6.1 joint law と相関

第5章の一般 visibility を含む law を

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV\cos\Delta_{a,b}
\right]
$$

と書く。phase offset は $\Delta_{a,b}$ に吸収した。相関は

$$
E(a,b)
=
\sum_{A,B}ABP_R(A,B\mid a,b)
=
-V\cos\Delta_{a,b}
$$

である。

## 6.2 equilibrium no-signalling

Alice の周辺確率は

$$
P_R(A\mid a,b)
=
\sum_{B=\pm1}
P_R(A,B\mid a,b)
=
\frac12.
$$

B 側も

$$
P_R(B\mid a,b)=\frac12
$$

である。従って指定した sign-symmetric equilibrium ensemble では

$$
P_R(A\mid a,b)
=
P_R(A\mid a,b'),
$$

$$
P_R(B\mid a,b)
=
P_R(B\mid a',b)
$$

が成立する。

これは microscopic measurement independence を回復することを意味しない。遠隔 setting dependence は full hidden distribution に残っているが、outcome-sign symmetry により一側周辺で相殺される。この種の symmetry protection は retrocausal model の先行解析とも整合する [11,12]。

## 6.3 CHSH

ideal phase map に対して

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

を選ぶ。すると三つの相関は $-V/\sqrt2$、残る一つは $+V/\sqrt2$ となり、

$$
|\mathcal S|
=
2\sqrt2V.
$$

従って

$$
V>\frac1{\sqrt2}
$$

なら CHSH 不等式を破り、$V=1$ なら Tsirelson value $2\sqrt2$ を得る。

## 6.4 Bell local response

最小模型の Bell-complete data に outcome seeds、local apparatus、messenger initial phase、soft return coordinate を含める。fixed microstate では

$$
A=\sigma(s_A),
\qquad
B=\sigma(s_B)
$$

であり、局所 outcome は遠隔 setting を引数に持たない。従って

$$
P(A,B\mid a,b,\lambda)
=
P(A\mid a,\lambda)
P(B\mid b,\lambda)
$$

が成立する。

common-future comparator は局所記録後にのみ作動し、一方向 evolution で過去の $A,B$ を変えない。Bell 上限を外すのは factorization failure ではなく、次節の measurement independence failure である。

## 6.5 microscopic posterior

ideal Model A では、hidden data の relevant part を $(A,B,E_s)$ と書ける。基準 energy density は $0\leq E_s\leq E_{\max}$ で一定である。`[R]` 後の条件付き density は

$$
\rho_R(A,B,E_s\mid a,b)
\propto
\mathbf1_{\{
0\leq E_s\leq
\kappa I_0(1-ABc_{a,b})
\}},
$$

$$
c_{a,b}=\cos\Delta_{a,b}.
$$

setting を変えると support の energy ceiling と outcome-sector volume が変わる。従って

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda\mid a',b')
$$

が明示的に成立する。

## 6.6 measurement dependence の全変動距離

二つの setting pair に対応する cosine を $c,c'$ とする。各 outcome sector における conditioned density の高さは共通で、support length だけが変化する。support の対称差を積分すると

$$
D_{\rm TV}(c,c')
=
\frac{|c-c'|}{2}
$$

を得る。

標準 CHSH に現れる $c=+1/\sqrt2$ と $c'=-1/\sqrt2$ の間では

$$
D_{\rm TV}
=
\frac1{\sqrt2}.
$$

これは本構成が measurement dependence の情報量について最適化されていないことを示す。setting prior を指定すれば mutual information も計算でき、Hall--Branciard の尺度と比較できる [5]。

## 6.7 setting normalization

ideal equal-sector preparation では

$$
Z_{a,b}
\propto
\sum_{A,B}
I_0(1-ABc_{a,b})
=
4I_0
$$

である。従って $Z_{a,b}$ は setting-independent で、二側 conditioning を controller を含む full ensemble に適用しても

$$
P_R(a,b)=P_0(a,b)
$$

が保たれる。実験者が controller の setting frequency を選べるという操作的事実と、microscopic source posterior の setting dependence は両立する。

## 6.8 一般 preparation

基準 outcome-sector weight を一般に $q_{AB}$ とする。linear return law の下では

$$
P_q(A,B\mid a,b,R)
=
\frac{
q_{AB}(1-ABc)
}{
\displaystyle
\sum_{A',B'}q_{A'B'}(1-A'B'c)
}.
$$

同時 sign flip symmetry

$$
q_{++}=q_{--},
\qquad
q_{+-}=q_{-+}
$$

があれば、一側周辺は $1/2$ に保たれる。ただし parity sectors の重みが異なる場合、全 compatibility $Z_{a,b}$ は $c$ に依存し得る。setting frequency まで基準分布のまま保つ最も単純な条件は

$$
q_{AB}=\frac14
$$

である。

## 6.9 biased subensemble の signalling

Bob の seed を $B=+1$ に限定した subensemble が準備可能だとする。

$$
q_{++}=q_{-+}=\frac12,
\qquad
q_{+-}=q_{--}=0.
$$

このとき

$$
P_q(A=+1\mid a,b,B=+1,R)
=
\frac{1-c}{2}.
$$

遠隔 setting の変更によって

$$
c=+\frac1{\sqrt2}
\quad\longrightarrow\quad
c=-\frac1{\sqrt2}
$$

とすれば、Alice の確率は

$$
0.1464\ldots
\quad\longrightarrow\quad
0.8536\ldots
$$

と変化する。従って最小模型は、任意の hidden-sector preparation に対して no-signalling なのではない。

この問題は measurement-dependent model に対する preparability-based Bell analysis [13] と同型である。full theory は、biased seed sector が操作的に準備できないこと、または準備操作自体を含む新しい boundary equilibrium が symmetry を回復することを示さなければならない。

## 6.10 equilibrium postulate [E]

以上から `[E]` は単なる計算上の便利ではなく、経験的 no-signalling を担保する物理的条件である。可能な完成方法は三つある。

1. `[R]` と source dynamics から sign-symmetric equilibrium measure が一意に選ばれることを証明する。
2. biased seed sector にアクセスするどの apparatus も、同時に terminal compatibility を変え、observable biased subensemble を作れないことを示す。
3. hidden-variable non-equilibrium を fundamental に禁止する preparation superselection rule を置く。

第一または第二が最も望ましい。第三を採る場合は `[E]` を `[R]` と独立な統計公理として明記しなければならない。

## 6.11 detector postselection ではないための条件

CHSH 分析では全 trial を含める。未検出 outcome または comparator failure を除外してはいけない。有限 apparatus で第三の pointer region $\varnothing$ が生じるなら、

$$
A\in\{+1,-1,\varnothing\}
$$

として full joint law を報告し、coincidence-conditioned CHSH を中心結果に用いない。

また、setting-dependent return rate が外部から観測可能な trial rate として現れる場合、それ自体が signal または detector loophole になる。理想模型で $Z_{a,b}$ が一定であることは、この監査の一部である。

## 6.12 Bell 前提台帳

- outcome definiteness：満たす。各 Hamilton history は一つの pointer sector を通る。
- local deterministic response：Bell-complete $\lambda$ 上で満たす。
- parameter independence at fixed $\lambda$：局所記録時刻について満たす。
- common measurement-independent distribution：満たさない。
- operational no-signalling：`[E]` の equilibrium ensemble では満たす。
- arbitrary-preparation no-signalling：最小模型では満たさない。
- freedom to vary setting-controller macrostate：許容する。
- absence of data postselection：模型の操作的実装条件として要求する。

## 6.13 本章の結論

本模型は Bell の定理をすり抜けるのではなく、measurement independence を定量的に破る。equilibrium source では sign symmetry により no-signalling と CHSH violation が両立するが、この no-signalling は arbitrary preparation へ自動的に拡張されない。`[E]` の物理的起源または biased subensemble の不可準備性が、`[R]` と並ぶ主要未解決問題である。
