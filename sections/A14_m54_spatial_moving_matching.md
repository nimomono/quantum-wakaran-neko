@number: N
@chapter: 付録
@title: M54空間移動状態構成とNelson型縮約
@status: M54共通親模型の空間移動状態構成を定義し、R161移動特殊化として旧R183の不変性を吸収する。R184のM37開始作用保持機構実装とR185のNelson型前後平均微分・時間対称Newton則を証明する。一般有限衝突は共通R162へ移す。

## N.1 M54空間移動状態構成と因果規約

有限グラフ $G=(V,E)$ 上でM54を $\Lambda=\mathcal I=V$、$\Psi=I$ へ特殊化する。Q3で直接使う1試行状態断面を

```math
\Gamma_t
=
(Q(t),P(t),X_t,S_{\rm ref})
```

とする。$Q_i,P_i$ は実正準信号自由度、$X_t\in V$ は1個の実在粒子位置である。位置jumpはR162の開放Poisson reservoirが担い、有限衝突素子とその微視的履歴を能動状態へ持たない。

```math
Z_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

は派生複素表示であり、独立した複素場ではない。$S_{\rm ref}$ はM37局所ばね実装を使う場合だけ開始面で固定する単一試行作用記憶部であり、理想M54空間信号部分系の発展則には入力しない。試行集団は $\mu_t(dX\,dZ)$ で記述し、

```math
C_Z(t)
=
\frac{\mathbb E[Z_tZ_t^\dagger]}
{\mathbb E[Z_t^\dagger Z_t]}
```

は集団統計に留める。$C_Z=cc^\dagger$ ならR135により $Z=\alpha c$ がほとんど確実に成り立つが、制御器は $c$、$C_Z$、全位置分布を入力しない。零信号 $Z=0$ はR164と同様に正規化結果重みを定義せず、開始面の正式な無反応結果へ送る。

## N.2 厳密信号部分系とR164型移動対象

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

とする。これはR164の $A_i^\delta/\mathcal J_0$ と同じ条件付き容量である。局所辺流と対称活動量を

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

である。

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



## N.4 R184の開始作用保持機構評価

M37局所包絡を $b(t)$、同じ初期値から進む理想M54空間信号を $b_L(t)$ とする。開始面で単一試行ごとに

```math
S_{\rm ref}
=
\|b(0)\|^2
```

を物理記憶部へ固定し、M37実装の背景容量は輸送中もこの値を使う。すなわち

```math
R_{i,37}^{\delta,\mathrm{lat}}(t)
=
|b_i(t)|^2+\delta q_iS_{\rm ref},
```

```math
T_{ij,37}^{\delta,\mathrm{lat}}(t)
=
\frac{|h_{ij}|}{\mathcal J_0}
\left(
R_{i,37}^{\delta,\mathrm{lat}}
+
R_{j,37}^{\delta,\mathrm{lat}}
\right),
```

```math
k_{i\to j}^{37,\mathrm{lat}}
=
\frac{
T_{ij,37}^{\delta,\mathrm{lat}}
+
J_{i\to j}(b)
}{
2R_{i,37}^{\delta,\mathrm{lat}}
}.
```

理想 $b_L$ は $\|b_L(t)\|^2=S_{\rm ref}$ を厳密保存するので、同じ固定機構表示はN.2の理想M54空間率と完全に一致する。M37局所包絡では $\|b(t)\|^2$ は厳密保存されないため、背景項を $\delta q_i\|b(t)\|^2$ へ毎時刻置き換えない。後者を採用する場合は局所作用変動に由来する追加率誤差が必要であり、R184の主張には含めない。

$\Delta=\delta_{\rm loc}(\eta)<1$ とする。規格化信号

```math
x=\frac{b}{\sqrt{S_{\rm ref}}},
\qquad
y=\frac{b_L}{\sqrt{S_{\rm ref}}}
```

は

```math
\|x-y\|
\leq
\frac{\varepsilon_{\rm car}(T)}{1-\Delta},
\qquad
\|x\|
\leq
\frac{1+\Delta}{1-\Delta},
\qquad
\|y\|=1.
```

保持背景容量を

```math
r_i^{\rm lat}(x)
=
|x_i|^2+\delta q_i
```

と置けば

```math
|r_i^{\rm lat}(x)-r_i^{\rm lat}(y)|
\leq
(R_\eta+1)|x_i-y_i|,
\qquad
R_\eta=\frac{1+\Delta}{1-\Delta}.
```

活動量差と確率流差は

```math
|t_{ij}^{\rm lat}(x)-t_{ij}^{\rm lat}(y)|
\leq
\frac{|h_{ij}|}{\mathcal J_0}
\sqrt2(R_\eta+1)\|x-y\|,
```

```math
|j_{ij}(x)-j_{ij}(y)|
\leq
\frac{2|h_{ij}|}{\mathcal J_0}
\sqrt{R_\eta^2+1}\|x-y\|.
```

$r_i^{\rm lat}\geq\delta q_{\min}$ を商へ使うと

```math
\max_i\sum_{j\ne i}
|k_{i\to j}^{37,\mathrm{lat}}-k_{i\to j}^{L}|
\leq
L_\delta(\eta)\varepsilon_{\rm car}(T)
```

で、

```math
L_\delta(\eta)
=
\frac{h_1}
{\mathcal J_0(1-\Delta)^2}
\left[
\frac{\sqrt2(1+\sqrt{1+\Delta^2})}{\delta q_{\min}}
+
\frac{2(1+\delta)}{\delta^2q_{\min}^2}
\right].
```

<!-- theorem-start:theorem -->
**定理（R184：M54空間 整合のM37開始作用保持機構実装）**

R86の仮定に加えて $\Delta<1$、$\delta>0$ とする。M37実装では開始面の $S_{\rm ref}=\|b(0)\|^2$ を固定して上の $k^{37,\mathrm{lat}}$ を使う。同じ初期位置分布から開始した理想M54空間過程とM37 保持背景過程は

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
P(X_t^{37,\mathrm{lat}}\in\cdot),
P(X_t^L\in\cdot)
\right)
\leq
T L_\delta(\eta)\varepsilon_{\rm car}(T)
```

を満たす。新R162の開放jump過程と終時刻記録を加えた完全結果誤差を

```math
\varepsilon_{184}
=
\varepsilon_{\rm init}
+
T L_\delta\varepsilon_{\rm car}
+
\varepsilon_{\rm rec}
```

とできる。厳密な $|\psi|^2$ と比較するときだけ $\delta/(1+\delta)$ を別項として加える。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R184）**

理想 $b_L$ では固定機構値が瞬間作用と一致するのでN.2のM54空間率そのものである。M37側では上の開始作用保持機構定義を使うため、規格化後の背景項は両過程で同じ $\delta q_i$ となり、表示した率差評価が各時刻に適用できる。有限Markov生成子のDuhamel公式と全変動距離の収縮性から、位置分布差は率行差の時間積分以下である。R162の開放jump生成子を適用する。有限衝突近似誤差は存在せず、終時刻記録の失敗だけを完全結果集合の無反応成分へ残して三角不等式で加える。証明終。
<!-- theorem-end:proof -->

## N.5 R161 後退率と前後平均微分

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

## N.6 有限格子の前後速度

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

## N.7 R185の時間対称Newton則と明示格子誤差

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

R185は理想M54空間信号部分系の結果である。R184の $L_\delta\varepsilon_{\rm car}$ は率と位置分布を制御するが、生M37の $2\omega_0$ マイクロモーションからNewton加速度までを率の時間微分付きで直接縮約した結果ではない。この直接縮約は強化課題として分離する。

## N.8 Q3-2の達成境界

R161/R162が定める同じ前向き開放経路法則からR185のBayes後退率を作るため、旧R188で必要だった有限衝突経路との比較は中心因果鎖に現れない。固定有限時間、1次元有限格子、node-free滑らかな部分系では

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
