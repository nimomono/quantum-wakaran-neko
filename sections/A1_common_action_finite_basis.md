@number: A
@chapter: 付録
@title: 共通作用、相関行列、M35有限基底補助
@status: 共通相関行列、作用区間、一意エルゴード性、M35の任意有限基底回路と完全正準構成をまとめる。

## A.1 理想有効担体と相関行列

この節だけでは、実正準対から

```math
d_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

を作り、設計済み有効 Hamiltonian

```math
H_{\rm eff}
=
d^\dagger h_Ld
```

を置く。これは第6章の位置ばね網そのものではなく、測定回路を記述する理想正準制御層である。この層内部では

```math
i\mathcal J_0\dot d
=
h_Ld,
\qquad
\mathcal J_0d^\dagger d
=
\operatorname{const}
```

が厳密に成立する。

調製条件 $\mathcal P$ とプログラム $M$ を固定した集団について

```math
C_M(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
d_t d_t^\dagger
\right]
```

と定める。$C_M$ は正半定値 Hermitian 行列であり、単一試行に追加する物質または正準変数ではない。

## A.2 相関行列の交換子発展

同じ集団の全試行が共通の $h_L(t)$ に従うなら、

```math
\begin{aligned}
i\mathcal J_0
\frac{d}{dt}
\left(dd^\dagger\right)
={}&
h_Ldd^\dagger
-
dd^\dagger h_L
\end{aligned}
```

なので、

```math
i\mathcal J_0\dot C_M
=
\left[h_L,C_M\right]
```

を得る。時間発展作用素を $U$ とすれば

```math
C_M(t)
=
U(t,t_0)
C_M(t_0)
U(t,t_0)^\dagger
```

である。従って跡、全固有値、階数、

```math
\mathcal P_C
=
\frac{\operatorname{tr}C^2}
{\left(\operatorname{tr}C\right)^2}
```

で定める純度が保存される。閉鎖線形発展だけでは高階数集団を階数1へ純化できない。

局所包絡 $b$ の厳密ミクロ発展には反回転項があるため、この交換子方程式を $b$ の厳密集団方程式として使わない。Q3-1のミクロ集団へ適用する場合は、第6章の包絡誤差を残す必要がある。

## A.3 階数1条件

$C=\Lambda\chi\chi^\dagger$、$\Lambda>0$、$\chi^\dagger\chi=1$ とする。$\chi$ と直交する任意の $v$ について

```math
0
=
v^\dagger Cv
=
\mathbb E
\left|
v^\dagger d
\right|^2
```

なので、$v^\dagger d=0$ がほとんど確実に成立する。有限次元直交補空間の基底を取れば、ある複素確率変数 $c^\omega$ が存在して

```math
d^\omega
=
c^\omega\chi
```

がほとんど確実に成立する。逆も明らかなので、階数1相関と共通射影方向は同値である。

交換子発展の下では、共通位相を選んで

```math
i\mathcal J_0\dot\chi
=
h_L\chi
```

とできる。この結果は理想有効層内部では厳密であるが、Q3-1のミクロ導出を置き換えない。

## A.4 近似階数1と閉包残差

$C$ の最大固有値を $\lambda_1$、主固有ベクトルを $\chi$ とし、

```math
C
=
\lambda_1\chi\chi^\dagger
+
E,
\qquad
E\geq0
```

とする。階数欠陥を

```math
\varepsilon_{\rm rank}
=
\frac{\operatorname{tr}E}
{\operatorname{tr}C}
```

とする。ユニタリ $W$ の出力 $k$ が理想因子に対して節を持つなら、

```math
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
\leq
\varepsilon_{\rm rank}
```

である。

残差付き有効式

```math
i\mathcal J_0\dot d
=
h_Ld+r
```

では

```math
i\mathcal J_0\dot C
=
\left[h_L,C\right]
+
D_C,
```

```math
D_C
=
\mathbb E
\left[
rd^\dagger-dr^\dagger
\right]
```

であり、

```math
\left\|D_C\right\|
\leq
2
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|d\right\|^2
\right)^{1/2}
```

を満たす。4次以上の Hamiltonian では $D_C$ が高次モーメントを含むため、$C$ だけの閉包は自動的に成立しない。

## A.5 作用区間選択

固定した $b,W$ に対し、$I_k\geq0$、$I_{\rm ph}=\sum_kI_k>0$ とする。$u$ が $[0,I_{\rm ph})$ 上で一様なら、結果事象

```math
E_k
=
\left\{
S_{k-1}\leq u<S_k
\right\}
```

の Lebesgue 長は $S_k-S_{k-1}=I_k$ である。従って

```math
P(E_k\mid b,W)
=
\frac{I_k}{I_{\rm ph}}
```

となる。境界集合 $\{u=S_k\}$ は有限集合なので零測度である。

選択器角 $\vartheta$ が $(b,W,\mathcal P)$ の下で条件付き Haar 分布なら、$u=I_{\rm ph}\vartheta/(2\pi)$ は条件付き一様である。条件付き期待値を取れば、

```math
P(k\mid W,\mathcal P)
=
\mathbb E
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
W,\mathcal P
\right]
```

を得る。

## A.6 固定作用公式と共分散補正

$I_{\rm ph}=I_0$ が集団で固定されるとする。$I_k=\mathcal J_0|(Wb)_k|^2$ なので、

```math
\mathbb E[I_k]
=
\mathcal J_0
\left(
WCW^\dagger
\right)_{kk},
```

```math
\mathbb E[I_{\rm ph}]
=
\mathcal J_0
\operatorname{tr}C
=
I_0
```

である。従って

```math
P_k
=
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
```

を得る。

全作用が変動する場合、$r_k=I_k/I_{\rm ph}$ と置けば $I_k=I_{\rm ph}r_k$ だから、

```math
\mathbb E[I_k]
=
\mathbb E[I_{\rm ph}]
\mathbb E[r_k]
+
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
```

である。$P_k=\mathbb E[r_k]$ を解けば本文の共分散恒等式を得る。

## A.7 無理数円回転の長期頻度と非混合性

正規化角 $r\in\mathbb R/\mathbb Z$ と無理数 $\alpha$ に対し、

```math
R_\alpha(r)
=
r+\alpha
\pmod1
```

とする。円周Haar測度は平行移動不変である。非零整数 $n$ に対するFourier指標の軌道平均は

```math
\frac1N
\sum_{j=0}^{N-1}
e^{2\pi in(r+j\alpha)}
=
e^{2\pi inr}
\frac{
1-e^{2\pi inN\alpha}
}{
N\left(1-e^{2\pi in\alpha}\right)
}
\longrightarrow
0
```

となる。三角多項式近似により回転は一意エルゴード的であり、境界がHaar零の半開区間 $[a,b)$ について、全初期角で訪問頻度が $b-a$ へ収束する。本文で使うBorn型長期頻度はこの区間頻度である。

一方、同じFourier指標の時間相関の絶対値は1のままなので、この回転は混合的でない。従って長期平均は得られるが、結果列の独立同分布性または二項分布型有限標本揺らぎは従わない。

## A.8 有限幅境界の測度上界

固定作用 $I_{\rm ph}$ の区間内に $L-1$ 個の内部境界 $S_1,\ldots,S_{L-1}$ がある。各境界の半幅 $w$ 近傍は長さ高々 $2w$ なので、一様測度と和集合上界から

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\min_{1\leq k<L}
|u-S_k|<w
\right)
\leq
2(L-1)
\frac{w}{I_{\rm ph}}
```

を得る。境界近傍が重なれば左辺はさらに小さい。

角の切断点近傍では、$f(\vartheta)=\vartheta/(2\pi)$ を円周上の滑らかな関数へ置き換える必要がある。その近傍の Haar 幅を $\varepsilon_{\rm cut}$ とすれば、無反応結果の全質量は右辺に $\varepsilon_{\rm cut}$ を加えて抑えられる。

## A.9 高階数集団に必要な追加自由度

固定作用殻上の源状態を $b^\omega$ とし、選択器角が $b^\omega$ の下で条件付き一様なら、

```math
P(k)
=
\mathbb E_\omega
\left[
\left|
\left(Wb^\omega\right)_k
\right|^2
\right]
=
\left(
WCW^\dagger
\right)_{kk}
```

である。ただし、本文の1次元不変トーラスでは $b^\omega=\chi$ が固定される。高階数 $C$ を単一軌道の時間平均として得るには、$b^\omega$ を動かす別の不変力学と、その力学に条件付けても選択器角が Haar 分布を保つ積構造または十分な結合条件が必要である。

## A.10 正準自由度

信号とテンプレートを

```math
b,t
\in
\mathbb C^L,
\qquad
b_j
=
\frac{Q_j^{b}+iP_j^{b}}{\sqrt{2\mathcal J_0}},
\qquad
t_j
=
\frac{Q_j^{t}+iP_j^{t}}{\sqrt{2\mathcal J_0}}
```

とする。作用レジスター、閾値、内部記録、選択器、時計は

```math
(Q_k,P_k)_{k=1}^L,
\quad
(Q_U,P_U),
\quad
(Q_M,P_M),
\quad
(\vartheta,J_{\rm sel}),
\quad
(\tau,P_\tau)
```

である。正準対数は $3L+4$ である。$L=2$ では10正準対になる。

周期開始値を

```math
b=t=e_1,
```

```math
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
```

```math
J_{\rm sel}=J_*>0,
\qquad
P_\tau=E
```

とする。選択器角 $\vartheta$ だけを自由にする。

## A.11 時計窓と自律化

$\tau\in S^1$ とし、

```math
H_{\rm clk}
=
P_\tau
```

と置く。各時計窓 $g_r(\tau)$ は滑らかで、逐次実行する窓の支持は互いに交わらず、

```math
\int_0^1g_r(\tau)\,d\tau
=
1
```

とする。互いに素な辺の生成子は同じ窓へまとめてもよい。全周期を

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_{r=1}^{N_{\rm cyc}(L,W)}
g_r(\tau)G_r
```

とする。$\dot\tau=1$ なので、これは時計を含む1本の有限自律 Hamiltonian である。旧来の固定14窓表示は、基底回路の長さが $L$ と $W$ に依存するため使わない。

## A.12 隣接2モード回路による任意ユニタリ

単一モード位相回転と隣接交換の実生成子を

```math
G_{Z,j}
=
\frac{
\left(Q_j^b\right)^2
+
\left(P_j^b\right)^2
}{2},
```

```math
G_{X,j}
=
Q_j^bQ_{j+1}^b
+
P_j^bP_{j+1}^b
```

とする。複素表示では

```math
G_{Z,j}
=
\mathcal J_0|b_j|^2,
```

```math
G_{X,j}
=
\mathcal J_0
\left(
b_j^*b_{j+1}
+
b_{j+1}^*b_j
\right)
```

である。$G_{Z,j}-G_{Z,j+1}$ と $G_{X,j}$ の Poisson 交換子は、行列表現で

```math
Y_j
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

の方向を生成する。従って $Z$、$X$、$Z$ の有限列で任意の隣接 $U(2)$ を実装できる。各流れはユニタリ正準変換であり、全作用を厳密に保存する。

構成的分解を確認する。複素数 $a,c$ に対し、

```math
G(a,c)
=
\frac1{\sqrt{|a|^2+|c|^2}}
\begin{pmatrix}
a^*&c^*\\
-c&a
\end{pmatrix}
```

とすれば、

```math
G(a,c)
\begin{pmatrix}
a\\
c
\end{pmatrix}
=
\begin{pmatrix}
\sqrt{|a|^2+|c|^2}\\
0
\end{pmatrix}
```

である。任意の $W\in U(L)$ に対し、列ごとに下から隣接2行へこの変換を掛けると、$L(L-1)/2$ 回以下で対角位相だけが残る。逆向きに並べ、残った対角位相を $D$ とすれば

```math
W
=
V_1V_2
\cdots
V_{N_W}D,
\qquad
N_W
\leq
\frac{L(L-1)}2
```

という隣接2モード変換と対角位相回転の積を得る。$D$ は $L$ 個以下の単一モード位相回転で実装する [38,39]。

逆回路は

```math
W^\dagger
=
D^\dagger
V_{N_W}^\dagger
\cdots
V_2^\dagger
V_1^\dagger
```

であり、同じ辺を逆順・逆角で使う。固定状態だけを作る $U_{\rm prep}e_1=\chi$ は、下成分を順に消去することで $L-1$ 個以下の2モード混合と位相調整に分解できる。

## A.13 準備回路と測定基底

第1の局所回路で

```math
b=e_1
\longmapsto
U_{\rm prep}e_1
=
\chi
```

とし、第2の局所回路で

```math
b
=
W\chi
```

とする。両回路はC.3節の生成子だけからなり、全位相作用を厳密に保存する。逆計算では同じ回路を逆順に使うため、密な一括生成子 $K_W$ を装置へ置かない。

信号鎖とテンプレート鎖を並べ、同じ番号の信号・テンプレートを SWAP 用の辺で結ぶ。作用レジスターは別の1次元鎖に置き、$Q_U$ を $Q_1$ の隣へ置く。基底変換、累積比較、テンプレート経路はこの有限次数グラフ上で局所になる。

## A.14 作用、閾値、累積差の読出し

読出し時のモード作用を

```math
I_k
=
\mathcal J_0|b_k|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^LI_k
=
\mathcal J_0
```

とする。角の切断接続領域を除いて $f(\vartheta)=\vartheta/(2\pi)$ とし、

```math
G_{\rm read}
=
\sum_{k=1}^L
P_kI_k
+
P_U\mathcal J_0f(\vartheta)
```

と置く。Hamilton 方程式は

```math
\dot Q_k=I_k,
\qquad
\dot Q_U=\mathcal J_0f(\vartheta),
\qquad
\dot P_k=\dot P_U=0
```

を与える。$P_k=P_U=0$ なので、信号と選択器の方程式へ入る読出し反作用は零である。単位面積流の後に

```math
Q_k=I_k,
\qquad
Q_U=u
```

となる。

続いて

```math
G_{0}^{\rm cum}
=
-P_1Q_U
```

を作用させ、次に

```math
G_j^{\rm cum}
=
P_{j+1}Q_j,
\qquad
j=1,\ldots,L-2
```

を番号順に作用させる。帰納的に

```math
Q_j
=
\sum_{r=1}^jI_r-u
=
S_j-u,
\qquad
j=1,\ldots,L-1
```

を得る。逆計算では $G_j^{\rm cum}$ を逆番号順・逆符号で使い、最後に $G_0^{\rm cum}$ を逆にする。

## A.15 双曲型増幅と滑らかな比較

累積差を

```math
G_{\rm amp}
=
\Lambda
\sum_{j=1}^{L-1}Q_jP_j
```

で増幅する。単位面積流は

```math
Q_j
\longmapsto
e^\Lambda Q_j,
\qquad
P_j
\longmapsto
e^{-\Lambda}P_j
```

である。$P_j=0$ は保たれ、逆流は $\Lambda\mapsto-\Lambda$ で得られる。

滑らかな関数を

```math
\rho(z)
=
\begin{cases}
0,&z\leq0,\\
e^{-1/z},&z>0,
\end{cases}
```

```math
\sigma(z)
=
\frac{\rho(z+1)}{\rho(z+1)+\rho(1-z)}
```

とし、

```math
h_j
=
\sigma
\left(
\frac{Q_j}{X}
\right),
\qquad
h_0=0,
\qquad
h_L=1
```

と置く。$Q_1\leq\cdots\leq Q_{L-1}$ なので $h_1\leq\cdots\leq h_{L-1}$ である。従って

```math
c_k
=
h_k-h_{k-1}
```

は非負で総和1となる。

角の切断接続領域を $\mathcal C_{\rm cut}$ とし、安全セクターを

```math
\mathcal O_k
=
\left\{
\vartheta\notin\mathcal C_{\rm cut},
\quad
Q_j\leq-X\quad(j<k),
\quad
Q_j\geq X\quad(j\geq k)
\right\}
```

とする。これらは互いに素である。補集合を $\mathcal O_\varnothing$ と定める。結果は比較ポインターセクターで判定し、後段の $Q_M$ だけでは判定しない。

入力換算幅は $w=Xe^{-\Lambda}$ である。$u$ が一様なので、

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\mathcal O_\varnothing
\right)
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

となる。境界近傍が重なれば右辺は過大評価になる。

## A.16 隣接テンプレート経路と記録

隣接生成子を

```math
Y_{j,j+1}
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

とし、$\ell_j=1-h_j$ とする。最初に

```math
G_M^{(0)}
=
P_M
```

を作用させ、$Q_M=1$ とする。続いて $j=1,\ldots,L-1$ の順に

```math
G_j^{\rm route}
=
\frac{\pi\mathcal J_0}{2}
\ell_j
t^\dagger Y_{j,j+1}t
+
P_M\ell_j
```

を作用させる。

$\mathcal O_k$ では

```math
\ell_j
=
\begin{cases}
1,&j<k,\\
0,&j\geq k,
\end{cases}
```

なので、$t=e_k$、$Q_M=k$ となる。初期テンプレートの成分は実で、各 $Y_{j,j+1}$ の流れも実回転として作用する。従って全経路で

```math
t^\dagger Y_{j,j+1}t
=
0
```

が保たれる。$P_M=0$ と合わせ、$\ell_j(Q)$ の座標依存性がポインター共役運動量へ与える反作用は零である。

$\mathcal O_\varnothing$ では複数の $\ell_j$ が中間値を取り得る。例えば $\sum_j\ell_j$ が整数でも、全 $h_j$ が平坦部にあるとは限らない。従って整数の $Q_M$ は必要な内部記録だが、十分な結果判定ではない。

## A.17 正準 SWAP 、測定後基底、保持

SWAP 生成子を

```math
G_{\rm sw}
=
i
\left(
b^\dagger t-t^\dagger b
\right)
```

とする。$\pi\mathcal J_0G_{\rm sw}/2$ の単位面積流は

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

を与える。$\mathcal O_k$ では SWAP 後に

```math
b=e_k,
\qquad
t=-W\chi
```

となる。信号へC.3節の逆局所回路 $W^\dagger$ を作用させると、

```math
b
=
W^\dagger e_k
=
|u_k\rangle
```

となる。次の時計窓は相互作用を置かない保持窓とし、比較ポインター、信号、$Q_M$ を読める状態に保つ。$\mathcal O_\varnothing$ では信号は一般に基底ベクトルではなく、結果は無反応である。

## A.18 全入力に対する逆計算

保持窓後に次を実行する。

1. 信号へ局所回路 $W$ を作用させる。
2. $-\pi\mathcal J_0G_{\rm sw}/2$ の流れで逆 SWAP する。
3. $G_j^{\rm route}$ を $j=L-1,\ldots,1$ の順に逆符号で作用させる。
4. $-G_M^{(0)}$ を作用させる。
5. $-G_{\rm amp}$ を作用させる。
6. $G_j^{\rm cum}$ を逆番号順・逆符号で作用させ、最後に $-G_0^{\rm cum}$ を作用させる。
7. $-G_{\rm read}$ を作用させる。
8. 信号へ $W^\dagger$ と $U_{\rm prep}^\dagger$ の局所回路を作用させる。

逆経路では読出しレジスターを消す前に、前向きと同じ $h_j$ と $\ell_j$ を再計算する。順序を入れ替えると逆写像にならない。

各操作は前向き流れの厳密な逆なので、安全セクターだけでなく $\mathcal O_\varnothing$ でも

```math
b=t=e_1,
```

```math
Q_k=P_k=Q_U=P_U=Q_M=P_M=0
```

へ戻る。滑らかな有限幅モデルでは、結果形成を無反応込みの粗視化で定義しながら、内部 Hamiltonian 写像そのものは全入力で厳密に可逆である。

## A.19 選択器ドリフトと時計運動量

最後に

```math
G_{\rm drift}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

を作用させる。Hamilton 方程式から

```math
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi},
\qquad
J_{\rm sel}
\longmapsto
J_{\rm sel}
```

となる。

各単独窓では $H=P_\tau+g_r(\tau)G_r$ である。$G_r$ は自分自身が生成する流れに沿って保存されるので、

```math
\Delta P_\tau
=
-\int
g_r'(\tau)G_r
\,d\tau
=
-G_r
\left[
g_r
\right]_{\rm in}^{\rm out}
=
0
```

である。窓は互いに重ならず、各窓端で $g_r=0$ なので、全周期後にも $P_\tau=E$ へ戻る。

## A.20 Poincaré 写像と長期分布

断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内の不変集合を

```math
\mathcal T_{\chi,W}
=
\left\{
b=t=e_1,
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
J_{\rm sel}=J_*,
P_\tau=E
\right\}
```

とする。自由なのは $\vartheta$ だけである。C.3節からC.10節までの写像を合成すると、

```math
\mathcal R_{\chi,W}
\left(
\vartheta
\right)
=
\vartheta+2\pi\alpha
\pmod{2\pi}
```

であり、他の全変数は定義値へ戻る。従って $\mathcal T_{\chi,W}$ は不変であり、Haar 測度の下で一意エルゴード的である。

理想累積区間の分布を

```math
p^{\rm id}
=
\left(
|\langle u_1|\chi\rangle|^2,
\ldots,
|\langle u_L|\chi\rangle|^2,
0
\right)
```

とする。実際の結果 $k$ は安全セクター $\mathcal O_k$、実際の無反応は $\mathcal O_\varnothing$ で定める。理想結果から失われた質量と無反応質量が一致するので、

```math
D_{\rm TV}
\left(
p^{\rm cyc},p^{\rm id}
\right)
=
p_{\varnothing}^{\rm cyc}
```

である。C.6節の上界により、有限 $\Lambda$ と有限切断幅で任意精度へ近づけられる。

## A.21 有限誤差に対する安全余裕

増幅前の累積差誤差を $\Delta_{\rm in}$、増幅後のポインター誤差を $\Delta_{\rm out}$ とする。入力換算された有効半幅は

```math
w_{\rm eff}
=
Xe^{-\Lambda}
+
\Delta_{\rm in}
+
e^{-\Lambda}\Delta_{\rm out}
```

である。従って

```math
\varepsilon_{\rm cmp}
\leq
\min
\left\{
1,
2(L-1)
\frac{w_{\rm eff}}{I_{\rm ph}}
\right\}
```

となる。増幅前の入力誤差は双曲型増幅で減らない。増幅後の固定出力誤差だけが入力換算で $e^{-\Lambda}$ 倍になる。

装置誤差が他にない場合、比較誤差を $\epsilon$ 以下にする十分条件は概ね

```math
\Lambda
\geq
\log
\frac{2(L-1)X}{\epsilon I_{\rm ph}}
```

である。精度を上げるほど必要な増幅率とポインター座標範囲が増える。有限温度での雑音床と長時間保持は本付録では評価しない。

## A.22 ゲート数と直列深さ

密な $W$ に対する資源上界は次である。

| 対象 | 隣接2モード混合回数 |
|---|---:|
| $W$ 1回 | $L(L-1)/2$ 以下 |
| 周期内の $W$、$W^\dagger$ 4回 | $2L(L-1)$ 以下 |
| 固定純粋準備 $U_{\rm prep}$ | $L-1$ 以下 |
| 準備と逆準備 | $2(L-1)$ 以下 |

比較剪断、テンプレート経路、逆実行はそれぞれ $O(L)$ 回である。信号モード数と物理交換辺数は増えず、1次元鎖の $L-1$ 辺を再利用する。

逐次 Givens 消去では基底回路の直列深さは $O(L^2)$ である。互いに素な辺を同じ時計層へ並列化する Clements 型配置では、基底回路の深さを $O(L)$ にできる [39]。ただし1個の時計自由度から空間的に離れた各辺へ窓信号を局所伝播させる配線自由度と遅延は、この数え上げに含めない。

## A.23 通常の位置ばねだけに限定した場合

正の位置ばね1本から得る有効2モード生成子は、対角離調を補正すれば交換方向へ近づけられる。しかし局所回転包絡は厳密には

```math
i\mathcal J_0\dot b
=
h(t)b
+
h(t)e^{2i\omega_0t}\overline b
```

を満たし、第2項が反回転項として残る。従って通常の位置ばねだけによる時間依存基底回路は、弱結合・非共鳴の近似である。

固定有限個のゲートでは、各ゲート誤差を $\delta_r$ とすれば

```math
\varepsilon_W^{\rm spr}
\leq
\sum_r\delta_r
```

と評価できる。しかし現行Q3-1定理は時間非依存 $h_L$ に限定され、順方向と逆方向の反回転誤差が無限反復で相殺されることも証明していない。古典振動子による一般複素状態の厳密表示に位置・運動量の双方の結合または符号調整が必要になることは、既存研究とも整合する [35--37]。

従って本付録では $QQ+PP$ 型の局所交換をQ2・Q3補助装置の現行構成とする。M37の位置ばね網、M47のQ1傾斜装置、本付録の交換回路を同一ハードウェアへ統合することは、M0またはM35の一般化として扱う別課題である。

## A.24 永久記録の限界

本周期の $Q_M$ と比較ポインターは内部記録であり、保持窓後に逆計算される。保持窓で結果を別の外部記録へコピーすれば、その外部自由度は結果情報を保持する。Hamiltonian 流の1対1性により、その外部記録まで結果に依存しない同一点へ戻すことはできない。

永久記録を伴う反復装置では、外部自由度を拡大するか、記録を循環履歴レジスターへ移すか、弱開放系として情報とエネルギーを外へ運ぶ必要がある。$L=2$ では付録BのM47/R144が、付録Lの操作面再平衡化を用いて外部記録セルとresetセル流を構成する。本付録の一般有限 $L$ のM35は、その外部過程を含まない。

## A.25 未導出事項

本付録の明示周期からは、次は導かれない。

1. 可変準備または可変基底を含む単一のエルゴード周期。
2. 高階数相関行列を1本の軌道から生成する源力学。
3. 混合性と二項分布型有限標本揺らぎ。
4. 一般有限 $L$ の複数段逐次測定、外部記録、弱開放 reset 、長距離時計配線。
5. 永久外部記録を含む有限閉鎖全系の同一点への完全帰還。
6. 無反応なしで連結入力領域全体を厳密な離散基底状態だけへ写す滑らかな有限時間流。
7. 作用区間ラベルと分析器出口の実現配置が各試行で同一であること。
8. 連続スペクトル極限。
9. M37の位置ばね網、M35またはM47の測定・記録回路を含むM0の完全統合。
