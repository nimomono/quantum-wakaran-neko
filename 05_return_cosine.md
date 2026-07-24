@number: B
@chapter: 付録B
@title: Hamilton 作用位相 register と有限 bath への接続
@status: 旧稿の OU/Nelson・作用 cocycle 部分を、Bell 本文に必要な最小 bridge へ圧縮。

## B.1 目的

Bell module 自体は phase-locked source `[P]` から始められる。しかし元の finite Hamilton theory との接続では、ある軌道 segment の Hamilton action

$$
S[z]
=
\int
\left(
\sum_i p_i\dot q_i-H_N(z)
\right)dt
$$

を actual canonical phase として保存できるかが問題になる。本付録では、その有限 realization を与える。

## B.2 on-shell Lagrangian

有限次元 Hamiltonian $H_N(q,p)$ に対し

$$
\mathcal L_N(q,p)
=
\sum_i
p_i\frac{\partial H_N}{\partial p_i}
-H_N(q,p)
$$

を定義する。Hamilton 軌道上では $\dot q_i=\partial H_N/\partial p_i$ なので

$$
\mathcal L_N
=
\sum_i p_i\dot q_i-H_N
$$

である。

## B.3 action register Hamiltonian

追加 canonical pair $(\Theta,I)$ と滑らかな関数 $F(I)$ を取り、

$$
F(I_0)=0,
\qquad
F'(I_0)=1
$$

とする。extended Hamiltonian を

$$
H_{\rm reg}
=
H_N(q,p)
-
\frac{F(I)}{\hbar_{\rm eff}}
\mathcal L_N(q,p)
$$

と定義する。

\begin{lemma}[action-register lemma]
初期条件 $I=I_0$ の invariant shell 上で、元の variables $(q,p)$ は未摂動 Hamiltonian $H_N$ に従う。canonical angle は

$$
\Theta(t)-\Theta(t_0)
=
-\frac{S[z]}{\hbar_{\rm eff}}
$$

を満たし、下で定義する messenger の polar phase $\vartheta_m=-\Theta$ は $S[z]/\hbar_{\rm eff}$ を満たす。
\end{lemma}

Proof. $H_{\rm reg}$ は $\Theta$ に依存しないため $\dot I=0$。$I=I_0$ では $F(I_0)=0$ なので $(q,p)$ に対する追加 Hamilton vector field は消え、元の $H_N$ trajectory が保たれる。一方

$$
\dot\Theta
=
\frac{\partial H_{\rm reg}}{\partial I}
=
-\frac{F'(I_0)}{\hbar_{\rm eff}}
\mathcal L_N
=
-\frac{\mathcal L_N}{\hbar_{\rm eff}}.
$$

時間積分すれば結論を得る。

## B.4 Cartesian messenger への変換

action-angle pair を working annulus 上で

$$
Q=\sqrt{2I}\cos\Theta,
\qquad
P=-\sqrt{2I}\sin\Theta
$$

と Cartesian canonical pair に写す。この符号を含めると $\{Q,P\}_{\Theta,I}=1$ である。$I=I_0$ 上では radius が一定で、Cartesian polar phase

$$
\vartheta_m
=
\arg(Q+iP)
=
-\Theta
$$

が $S/\hbar_{\rm eff}$ を運ぶ。本文の source phase $\Theta_A,\Theta_B$ はこの $\vartheta_m$ と同定する。付録Aの splitter を用いれば、この一つの source register から共通 phase を持つ二 messenger を作れる。

## B.5 有限 bath との接続

粒子と $N$ 個の oscillator を含む finite Hamiltonian を $H_N$ とすれば、上の補題は任意の有限 $N$ でそのまま成立する。bath を消去して generalized Langevin equation または effective action を得る標準手順は既知である [17--19]。OU/Nelson limit を取る場合、mode spectrum、tightness、counterterm、極限順序を別途制御する必要がある [20--23]。

本論文の Bell theorem はこの極限を必要としない。必要なのは、finite source segment の renormalized action または選んだ canonical phase を messenger へ記録できることである。旧稿で扱った次の内容は独立の foundational paper に属する。

- 単一温度 Gibbs ensemble と OU cusp の no-go。
- non-Gibbs mode spectrum による finite-periodic OU approximation。
- two-sided Gaussian bridge と Doob drift。
- renormalized action と Nelson variational principle。
- Wallstrom quantization condition。
- two-history cross kernel と complex moment compression。

これらの成否は phase source の自然性を左右するが、本稿の finite Bell realization の代数的正しさを左右しない。

## B.6 physical naturalness

action-register lemma は existence proof であり、自然界が $\mathcal L_NF(I)$ coupling を自発的に供給することを示さない。さらに $I$ の有限幅があると $F(I)\neq0$ となり、元の trajectory へ backreaction が生じる。

従って検証すべき量は

$$
\epsilon_{\rm reg}
=
\sup_{0\leq t\leq T}
\lVert z_{\rm reg}(t)-z_N(t)\rVert
$$

および phase error

$$
\epsilon_\Theta
=
\left|
\vartheta_m(T)-\vartheta_m(0)-S[z]/\hbar_{\rm eff}
\right|.
$$

Bell violation には、これらの誤差が visibility を $1/\sqrt2$ 以下へ落とさないことが必要である。

## B.7 Koopman 表現との違い

古典 Hamiltonian flow を Hilbert space 上へ表すこと自体は Koopman 以来知られている [24]。しかし本補題で重要なのは複素記法ではなく、phase が actual finite canonical pair $(Q,P)$ に保存され、局所 analyzer と return comparator がその pair に物理的に結合できることである。

## B.8 結論

作用積分から messenger phase への写像は、有限 extended Hamiltonian の invariant action shell 上で明示できる。これにより旧稿の action-to-mode gap は数学的には閉じる。ただし register coupling の自然性、finite-width stability、OU/Nelson source からの高 visibility preparation は未解決であり、Bell 主本文とは分離して扱う。
