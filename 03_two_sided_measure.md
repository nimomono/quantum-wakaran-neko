@number: A
@chapter: 付録A
@title: Hamilton 方程式と symplectic network の詳細
@status: 第4章の有限 Hamiltonian map の直接計算。

## A.1 Poisson structure

canonical pair $(q_j,p_j)$ に対して

$$
\{F,G\}
=
\sum_j
\left(
\frac{\partial F}{\partial q_j}
\frac{\partial G}{\partial p_j}
-
\frac{\partial F}{\partial p_j}
\frac{\partial G}{\partial q_j}
\right)
$$

とする。Hamiltonian $K$ の pulse parameter $\tau$ に関する flow は

$$
\frac{dF}{d\tau}=\{F,K\}
$$

である。有限時間 flow は symplectic form と Liouville volume を保存する。

## A.2 messenger rotation

一 pair $(Q,P)$ と action

$$
I=\frac12(Q^2+P^2)
$$

に対して $K=-\theta I$ とする。このとき

$$
\dot Q=-\theta P,
\qquad
\dot P=\theta Q.
$$

従って unit flow は

$$
\begin{pmatrix}Q\\P\end{pmatrix}_{\rm out}
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}
\begin{pmatrix}Q\\P\end{pmatrix}_{\rm in}.
$$

$\theta=\phi(a)+\pi\chi_-(s)$ なら

$$
R[\theta]
=
\sigma(s)R[\phi(a)].
$$

この map は $I$ を保存する。

## A.3 pointer shift

$K_{\rm ptr}=-Y\sigma(s)$ に対して

$$
\dot Y=0,
\qquad
\dot\Pi=\sigma(s).
$$

unit flow は

$$
(Y,\Pi)
\longmapsto
(Y,\Pi+\sigma).
$$

Hamiltonian flow なので、phase-space volume を一つの pointer region へ圧縮しているのではない。異なる seed regions が異なる pointer regions へ一対一で移される。

## A.4 seed と controller の backreaction

局所 generator は $\pi_s$ と setting conjugate momentum $\alpha$ に依存しないため

$$
\dot s=0,
\qquad
\dot a=0.
$$

一方、

$$
\dot\pi_s
=
-\frac{\partial K}{\partial s},
\qquad
\dot\alpha
=
-\frac{\partial K}{\partial a}
$$

である。seed support を $\sigma'(s)=0$ の plateau に限定すれば、$\pi_s$ への backreaction も消える。setting controller の $\alpha$ は一般に impulse を受けるが、設定座標 $a$ は固定される。これは測定器が setting choice から仕事を受け取ることと整合する。

## A.5 source splitter

source mode $(Q_0,P_0)$ と ready auxiliary $(Q_v,P_v)$ に対して

$$
K_S
=
\frac\pi4
\left(
Q_0P_v-Q_vP_0
\right)
$$

を unit pulse とする。生成する mode rotation は

$$
u_0'
=
\frac{u_0-u_v}{\sqrt2},
\qquad
u_v'
=
\frac{u_0+u_v}{\sqrt2}.
$$

$u_v=0$、$u_0=\sqrt2\,r\,n(\Theta)$ なら二出力は固定符号または port convention を除いて共通 phase と amplitude $r$ を持つ。通常の time-reversal-even coupled-oscillator network でも、固定 phase offset を伴う同じ splitter を実装し、その offset を $\Phi_0$ へ吸収できる。

## A.6 difference mode

orthogonal mode transformation

$$
u_+
=
\frac{u_A+u_B}{\sqrt2},
\qquad
u_-
=
\frac{u_A-u_B}{\sqrt2}
$$

は $(Q_A,Q_B)$ と $(P_A,P_B)$ へ同じ直交行列を作用させるため symplectic である。対応する actions は

$$
I_+=\frac12\lVert u_+\rVert^2,
\qquad
I_-=\frac12\lVert u_-\rVert^2,
$$

$$
I_++I_-=I_A+I_B.
$$

従って common-future comparison は total messenger action を保存する passive network として実装できる。

## A.7 comparator flow

$D=H_s-\kappa I_-$ とし

$$
K_R=F_R(Y_R)D
$$

とする。$Y_R=0$ では

$$
\dot\Pi_R=-F_R'(0)D=-D.
$$

また $F_R(0)=0$ なので任意の soft または messenger observable $X$ に対し

$$
\dot X
=
F_R(0)\{X,D\}=0
$$

である。従って unit pulse 後に

$$
\Pi_R=\kappa I_- -H_s
$$

となり、比較対象自体は変化しない。

## A.8 boundedness on the working domain

$F_R(Y)=\delta\tanh(Y/\delta)$ なら $|F_R|\leq\delta$ である。また

$$
I_-
\leq
I_A+I_B
$$

なので、free messenger coefficient を十分大きく取れば comparator coupling を含む energy を working domain 上で下から有界にできる。ideal pointer に kinetic term を加えた正則化は付録Dで扱う。

## A.9 自由度数

Model A の Bell module は11 canonical pair、22-dimensional phase space である。source splitter を Hamiltonian 内に入れるなら source と auxiliary の二 pair を追加するが、その出力二 pairを messenger と同一視すれば実質的な増加は ready auxiliary 一 pairである。Model B は soft pair を一つ追加する。finite bath を $N$ pair で接続しても全次元は有限のままである。

## A.10 結論

local analyzer、pointer shift、source splitting、difference-mode formation、return comparison はすべて通常の canonical flow として書ける。確率則を担うのはこれらの map ではなく、同じ map の終端逆像へ `[R]` が与える measure である。
