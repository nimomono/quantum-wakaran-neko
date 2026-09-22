@number: N
@chapter: 付録
@title: R161空間参照過程とNelson型縮約
@status: R161が定める空間移動参照過程とcanonical Markov経路法則を定義し、Q1型局所正準信号とQ2型辺結合から得る $(\pi,j)$ をR161へ接続する。現行 $T_{ij}^\delta$ は許容される対称活動量の1選択として位置づけ、同じ前向き経路法則からR185のNelson型前後平均微分・時間対称Newton則を証明する。R162は同じR161 lawのoptional Poisson realizationであり、本付録の論理依存には置かない。

## N.1 R161空間参照過程と因果規約

有限グラフ $G=(V,E)$ 上でM54を $\Lambda=\mathcal I=V$、$\Psi=I$ へ特殊化する。この空間信号はQ1/Q2と別の正準代数ではなく、Q1型の局所実正準モードを頂点へ配置し、Q2で用いるのと同じ有限2体系エルミート結合族を辺へ反復した特殊化として読める。辺結合を切れば独立な局所モード列に戻り、空間確率流は消える。

R161/R185のideal参照過程で使う状態断面を

```math
\Gamma_t
=
(Q(t),P(t),X_t)
```

とする。$Q_i,P_i$ は実正準信号自由度、$X_t\in V$ はR161 canonical Markov経路法則に従う参照位置座標である。R162を用いなくてもこの経路法則はR161自身で存在・一意性・非爆発性まで定まる。

```math
Z_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

は派生複素表示であり、独立した複素場ではない。試行集団は $\mu_t(dX\,dZ)$ で記述し、

```math
C_Z(t)
=
\frac{\mathbb E[Z_tZ_t^\dagger]}
{\mathbb E[Z_t^\dagger Z_t]}
```

は集団統計に留める。$C_Z=cc^\dagger$ ならR135により $Z=\alpha c$ がほとんど確実に成り立つが、制御器は $c$、$C_Z$、全位置分布を入力しない。零信号 $Z=0$ では正規化位置重みを定義せず、開始面の正式な無反応結果へ送る。

## N.2 厳密信号部分系とR161移動特殊化

エルミート $h=A+iB$、$A^{\mathsf T}=A$、$B^{\mathsf T}=-B$ に対する

```math
H_{\rm sig}
=
\frac{Q^{\mathsf T}AQ+P^{\mathsf T}AP}{2\mathcal J_0}
+
\frac{P^{\mathsf T}BQ}{\mathcal J_0}
```

は厳密に

```math
i\mathcal J_0\dot Z=hZ
```

を与え、$S=Z^\dagger Z$ を保存する。

以下では非零信号 $S=Z^\dagger Z>0$ を扱う。$q_i>0$、$\sum_iq_i=1$、$\delta>0$ とし、

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
\pi_i^\delta
=
\frac{R_i^\delta}{(1+\delta)S}
```

とする。これはM64/R203で用いる正の背景を加えたregularized signal densityである。局所辺流と対称活動量を

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
Z_j^*h_{ji}Z_i
\right),
```

```math
T_{ij}^\delta
=
\frac{|h_{ij}|}{\mathcal J_0}
(R_i^\delta+R_j^\delta)
```

と定める。$2|Z_i||Z_j|\leq|Z_i|^2+|Z_j|^2$ から

```math
|J_{i\to j}|
\leq
T_{ij}^\delta
```

である。ここで $J_{i\to j}$ は信号Hamiltonianと局所連続方程式から固定されるが、$T_{ij}^\delta$ はR161が許す対称活動量の1選択であり、連続方程式だけから一意には定まらない。規格化した $t_{ij}=T_{ij}^\delta/[(1+\delta)S]$ を別のミクロ模型が同じ有向率まで再現する場合、その模型は第2章の意味で同じR161実現となる。異なる許容活動量を採る場合もR161の一般定理自体は変わらない。

## N.3 R161移動特殊化

前向き率を

```math
k^+_{i\to j}
=
\frac{T_{ij}^\delta+J_{i\to j}}{2R_i^\delta}
```

とする。

前向き率を

```math
k^+_{i\to j}
=
\frac{T_{ij}^\delta+J_{i\to j}}{2R_i^\delta}
```

とする。R161へ

```math
\pi_i=\pi_i^\delta,
\qquad
j_{ij}
=
\frac{J_{i\to j}}{(1+\delta)S},
\qquad
t_{ij}
=
\frac{T_{ij}^\delta}{(1+\delta)S}
```

を代入するとこの率が得られる。信号の連続方程式から

```math
\dot\pi_i^\delta
=
\frac{1}{(1+\delta)S}
\sum_jJ_{j\to i}
```

なので、R161により初期共同分布が $\mu_0^Z$-ほとんど全ての $z$ で

```math
\mu_0(X=i\mid Z=z)
=
\pi_i^\delta(z)
```

を満たせば、全有限時刻で $\mu_t^Z$-ほとんど全ての $z$ について

```math
\mu_t(X=i\mid Z=z)
=
\pi_i^\delta(z)
```

が成り立つ。

<!-- theorem-start:corollary -->
**系（R161のM54空間-移動特殊化）**

階数1 信号集団 $C_Z(t)=\psi_t\psi_t^\dagger$ ではR135の支持節から $Z=\alpha\psi$ がほとんど確実であり、

```math
P(X_t=i)
=
\frac{|\psi_i(t)|^2+\delta q_i}{1+\delta},
```

```math
D_{\rm TV}
\left(
P(X_t\in\cdot),|\psi_t|^2
\right)
\leq
\frac{\delta}{1+\delta}.
```

整合不変性自体には階数1仮定を要しない。これは旧R183の内容を一般R161へ吸収したものである。
<!-- theorem-end:corollary -->



## N.4 R161 後退率と前後平均微分

R161移動特殊化の共同経路分布を固定する。$p_i(t)=P(X_t=i\mid Z_t)$ は $\delta>0$ で正である。同じ経路分布のBayes反転から

```math
k^-_{i\to j}
=
\frac{p_jk^+_{j\to i}}{p_i}
=
\frac{T_{ij}^\delta-J_{i\to j}}{2R_i^\delta}
```

を得る。別の未来浴、後向き制御器、未来境界条件を物理入力として追加しない。

```math
D_+f_i
=
\partial_tf_i
+
\sum_jk^+_{i\to j}(f_j-f_i),
```

```math
D_-f_i
=
\partial_tf_i
+
\sum_jk^-_{i\to j}(f_i-f_j)
```

と定める。

## N.5 有限格子の前後速度

1次元最近接格子 $x_i=ia$ と

```math
h_{i,i+1}
=
-\frac{\mathcal J_0\nu}{a^2},
\qquad
\mathcal J_0=2m\nu
```

を考える。規格化辺流 $j_{i+1/2}=J_{i\to i+1}/[(1+\delta)S]$ に対し

```math
v_i^{(a,\delta)}
=
\frac{a}{2p_i}
(j_{i+1/2}+j_{i-1/2}),
```

```math
u_i^{(a,\delta)}
=
\frac{\nu}{2ap_i}
(p_{i+1}-p_{i-1})
```

と置くと有限格子上で厳密に

```math
D_+X=v^{(a,\delta)}+u^{(a,\delta)},
\qquad
D_-X=v^{(a,\delta)}-u^{(a,\delta)}
```

である。

Q3のR185では長さ $\ell=Na$ の1次元周期領域で一様背景 $q_i=1/N=a/\ell$ を採用する。連続密度を $\sum_i|\psi_i|^2=1$、$|\psi_i|^2=a\rho(x_i)+O(a^3)$ と規格化すると、背景の連続密度は

```math
q_0
=
\frac{q_i}{a}
=
\frac1\ell.
```

従って $\psi=\sqrt\rho e^{iS/\mathcal J_0}$、

```math
v=\frac{\partial_xS}{m},
\qquad
u=\nu\partial_x\log\rho
```

とし、

```math
A=\frac{\rho}{\rho+\delta q_0},
\qquad
\epsilon=1-A
```

と置くと

```math
v_\delta=Av,
\qquad
u_\delta=Au
```

であり、十分滑らかな節のない領域で $v^{(a,\delta)}=v_\delta+O(a^2)$、$u^{(a,\delta)}=u_\delta+O(a^2)$ である。

## N.6 R185の時間対称Newton則と明示格子誤差

```math
a_{N,\delta}
=
\frac12(D_+D_-+D_-D_+)X
```

とする。理想M54空間状態構成の有限格子実正準信号は、複素表示で

```math
i\mathcal J_0\dot\psi_i
=
-\frac{\mathcal J_0^2}{2m}
\Delta_a\psi_i
+
V_i\psi_i,
\qquad
\Delta_a f_i
=
\frac{f_{i+1}-2f_i+f_{i-1}}{a^2},
```

を満たす。これは独立な量子公理でなくN.2の実ハミルトニアンの表示である。滑らかな補間を $\psi=\sqrt\rho e^{iS/\mathcal J_0}$ とし、

```math
v=\frac{\partial_xS}{m},
\qquad
u=\nu\partial_x\log\rho,
\qquad
A=\frac{\rho}{\rho+\delta q_0},
\qquad
\epsilon=1-A
```

と置く。連続側の正則化速度は $v_\delta=Av$、$u_\delta=Au$ である。

有限格子信号から連続補間への差を明示するため

```math
c_\delta=\delta q_0,
\qquad
r=\rho+c_\delta,
\qquad
r_*=\rho_*+c_\delta
```

とし、

```math
R_k=\|\partial_x^k\rho\|_\infty,
\qquad
\Phi_k=\|\partial_x^k\psi\|_\infty,
\qquad
\Phi_{t,k}=\|\partial_t\partial_x^k\psi\|_\infty.
```

さらに

```math
H_0=\frac1{r_*},
\qquad
H_1=\frac{R_1}{r_*^2},
\qquad
H_2=
\frac{R_2}{r_*^2}
+
\frac{2R_1^2}{r_*^3},
\qquad
H_t=\frac{\|\partial_t\rho\|_\infty}{r_*^2}.
```

中心差分 $D_0^a$ と格子Laplacianについて

```math
\|D_0^af-\partial_xf\|_\infty
\leq
\frac{a^2}{6}\|\partial_x^3f\|_\infty,
```

```math
\|\Delta_af-\partial_x^2f\|_\infty
\leq
\frac{a^2}{12}\|\partial_x^4f\|_\infty.
```

格子速度と連続正則化速度の誤差係数を

```math
\beta_{u,0}
=
\frac{\nu}{6}H_0R_3,
\quad
\beta_{u,1}
=
\frac{\nu}{6}(H_1R_3+H_0R_4),
```

```math
\beta_{u,2}
=
\frac{\nu}{6}(H_2R_3+2H_1R_4+H_0R_5),
```

```math
\beta_{v,0}
=
\frac{\nu}{3}H_0\Phi_0\Phi_3,
```

```math
\beta_{v,1}
=
\frac{\nu}{3}
[
H_1\Phi_0\Phi_3
+
H_0\Phi_1\Phi_3
+
H_0\Phi_0\Phi_4
],
```

```math
\begin{aligned}
\beta_{v,2}
=
\frac{\nu}{3}
[
&
H_2\Phi_0\Phi_3
+
2H_1\Phi_1\Phi_3
+
2H_1\Phi_0\Phi_4
\\
&
+
H_0\Phi_2\Phi_3
+
2H_0\Phi_1\Phi_4
+
H_0\Phi_0\Phi_5
],
\end{aligned}
```

```math
\beta_{v,t}
=
\frac{\nu}{3}
\left[
H_t\Phi_0\Phi_3
+
H_0
(
\Phi_{t,0}\Phi_3
+
\Phi_0\Phi_{t,3}
)
\right]
```

とする。また

```math
\Gamma_{v,1}
=
\beta_{v,1}
+
\frac16\|\partial_x^3v_\delta\|_\infty,
\quad
\Gamma_{u,1}
=
\beta_{u,1}
+
\frac16\|\partial_x^3u_\delta\|_\infty,
```

```math
\Gamma_{u,2}
=
\beta_{u,2}
+
\frac1{12}\|\partial_x^4u_\delta\|_\infty.
```

固定した $a_0>0$ に対し

```math
\overline V_1
=
\|\partial_xv_\delta\|_\infty
+
a_0^2\Gamma_{v,1},
\quad
\overline U_1
=
\|\partial_xu_\delta\|_\infty
+
a_0^2\Gamma_{u,1},
```

```math
\overline V_2
=
\|\partial_x^2v_\delta\|_\infty
+
a_0^2\beta_{v,2},
\quad
\overline U_2
=
\|\partial_x^2u_\delta\|_\infty
+
a_0^2\beta_{u,2}.
```

有限格子の前後生成子を直接展開すると、滑らかなnode-free部分系での運動学的格子誤差は

```math
\|a_{N,\delta}^{(a)}-a_\delta\|_\infty
\leq
C_{\rm kin}a^2
```

で抑えられ、

```math
\begin{aligned}
C_{\rm kin}
={}&
\beta_{v,t}
+
\beta_{v,0}\overline V_1
+
\|v_\delta\|_\infty\Gamma_{v,1}
\\
&+
\beta_{u,0}\overline U_1
+
\|u_\delta\|_\infty\Gamma_{u,1}
+
\nu\Gamma_{u,2}
\\
&+
\frac{\|\partial_t\rho\|_\infty}{4r_*}
\overline V_2
+
\frac{\nu R_2}{4r_*}
\overline U_2 .
\end{aligned}
```

一方、有限格子Schrödinger表示と連続補間の残差は

```math
\mathscr R_a
=
\mathcal J_0\nu
(\partial_x^2-\Delta_a)\psi
```

であり、

```math
\|\mathscr R_a\|_\infty
\leq
\frac{\mathcal J_0\nu}{12}\Phi_4a^2,
\qquad
\|\partial_x\mathscr R_a\|_\infty
\leq
\frac{\mathcal J_0\nu}{12}\Phi_5a^2.
```

node-free条件 $|\psi|\geq\sqrt{\rho_*}$ と $\mathcal J_0=2m\nu$ から

```math
C_{\rm dyn}
=
\frac{\nu^2}{6}
\left[
\frac{\Phi_5}{\sqrt{\rho_*}}
+
\frac{\Phi_4\Phi_1}{\rho_*}
\right]
```

と取れ、

```math
C_{185,a}
=
C_{\rm kin}
+
C_{\rm dyn}
<\infty.
```

Madelung恒等式と正則化代数を合わせると

```math
a_{N,\delta}
=
-\frac{\partial_xV}{m}
+
R_\delta
+
E_a,
\qquad
\|E_a\|_\infty
\leq
C_{185,a}a^2,
```

```math
R_\delta
=
\epsilon
\left[
\frac{\partial_xV}{m}
-
2A(v\partial_xv+u\partial_xu)
-
\frac{A\epsilon}{\nu}u(v^2+u^2)
\right].
```

<!-- theorem-start:theorem -->
**定理（R185：共通の確率分布時間反転と時間対称Newton則）**

R161移動特殊化を長さ $\ell=Na$ の1次元一様格子へ特殊化し、$q_i=1/N$、連続背景密度 $q_0=1/\ell$、$\delta>0$、$\mathcal J_0=2m\nu$ とする。固定有限時間の節のない滑らかな部分系で $\rho\geq\rho_*>0$ を仮定し、上で用いた $\rho$、$\psi$、$v_\delta$、$u_\delta$ の有限個の空間・時間微分ノルムが有限とする。同じ共同経路分布から定まる $D_\pm$ は有限格子速度分解を厳密に満たし、

```math
\boxed{
\left\|
m a_{N,\delta}
+
\partial_xV
-
mR_\delta
\right\|_\infty
\leq
mC_{185,a}a^2 .
}
```

$F_0=\|\partial_xV/m\|_\infty$、$V_0=\|v\|_\infty$、$V_1=\|\partial_xv\|_\infty$、$U_0=\|u\|_\infty$、$U_1=\|\partial_xu\|_\infty$、

```math
\epsilon_*
=
\frac{\delta q_0}{\rho_*+\delta q_0}
```

とすれば

```math
\|R_\delta\|_\infty
\leq
\epsilon_*
\left[
F_0
+
2(V_0V_1+U_0U_1)
+
\frac{\epsilon_*}{\nu}U_0(V_0^2+U_0^2)
\right].
```

従って正則化残差は $O(\delta)$、格子残差は明示的に $C_{185,a}a^2$ である。
<!-- theorem-end:theorem -->

R185はR161が定める前向き経路法則と同じ分布のBayes時間反転から得る有限格子結果である。現行Q3ではM64/R203A--R203DがM37 signalからR161過程への物理接続を担う。生M37の $2\omega_0$ マイクロモーションからNewton加速度までを時間微分付きで直接縮約することは強化課題として分離する。

## N.7 Q3-2の達成境界

R161自身が定めるcanonical前向き経路法則からR185のBayes後退率を作るため、旧R188で必要だった有限衝突経路との比較は中心因果鎖に現れない。固定有限時間、1次元有限格子、node-free滑らかな部分系では

```math
\left\|
m
\frac12
\left(
D_+D_-+D_-D_+
\right)X
+
\partial_xV
\right\|_\infty
\leq
m\|R_\delta\|_\infty
+
mC_{185,a}a^2.
```

従って $\delta$ と格子幅 $a$ を順に小さくすることで時間対称Newton則へ任意有限誤差で近づける。未来から物理作用する第2浴は導入せず、後向き率は同じ前向き経路分布の条件付き確率である。

生M37局所包絡からNewton加速度までの直接時間微分付き縮約、連続空間の一様極限、多粒子配置空間、位相量子化は現行Q3-2の達成範囲に含めない。旧R162有限衝突経路および旧R188の安定性は有限閉鎖実装の強化結果として論文外メモへ保存する。
