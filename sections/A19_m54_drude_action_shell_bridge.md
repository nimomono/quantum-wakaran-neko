@number: S
@chapter: 付録
@title: 2作用LC殻Drude混合と静的平方根衝突接続
@status: R190A--R190Cについて、無限古典Drude浴による作用保存型混合、有限時間作用分配一様化、対称作用開口からR161静的平方根核への単回接続と反復時のrenewal条件を証明する。

## S.1 目的、記号、主張範囲

R164は固定済み正作用容量 $\widehat A_i$ に対する2作用殻のLiouville状態数を線形に数えるが、R161静的特殊化の平方根分割そのものを一意には決めない。本付録では、2作用殻を2つの同周波数LCモードとして表し、無限自由度の等方Drude浴で作用分配を混合し、対称作用開口を通じてR161静的平方根核へ接続する一つの十分条件を与える。

本付録は無限古典調和浴を模型の一部として採用する。有限長・有限モード伝送線からの持ち上げ、容量生成から記録までの単一有限局所Hamiltonian装置、完全周期の仕事・熱・エントロピー収支は主張しない。R190が直接必要とするのは衝突に用いる作用比 $I/\widehat A$ の分布であり、2作用殻の全位相方向を有限時間で完全microcanonical化することではない。

## S.2 2作用LC殻と作用方向

2つの同周波数LCモードの複素正準振幅を $\zeta_K,\zeta_I$ とし、

\`\`\`math
K=\mathcal J_0|\zeta_K|^2,
\qquad
I=\mathcal J_0|\zeta_I|^2,
\qquad
K+I=\widehat A>0
\`\`\`

とする。Schwinger型作用生成子を

\`\`\`math
S_x=\frac{\mathcal J_0}{2}
(\zeta_K^*\zeta_I+\zeta_I^*\zeta_K),
\`\`\`

\`\`\`math
S_y=\frac{\mathcal J_0}{2i}
(\zeta_K^*\zeta_I-\zeta_I^*\zeta_K),
\qquad
S_z=\frac{K-I}{2}
\`\`\`

と置く。直接計算で

\`\`\`math
S_x^2+S_y^2+S_z^2=\frac{\widehat A^2}{4}
\`\`\`

である。従って

\`\`\`math
\boldsymbol n=\frac{2\boldsymbol S}{\widehat A}\in S^2,
\qquad
X=\frac{I}{\widehat A}=\frac{1-n_z}{2}.
\`\`\`

## S.3 無限調和Drude浴と作用保存

各 $\alpha=x,y,z$ に独立同型な調和浴を置き、counterterm込みの全Hamiltonianを

\`\`\`math
H_{\rm tot}
=
H_{\rm LC}(\widehat A)
+
\sum_{\alpha=x,y,z}
\int_0^\infty
\left[
\frac{p_\alpha(\omega)^2}{2m(\omega)}
+
\frac{m(\omega)\omega^2}{2}
\left(
q_\alpha(\omega)
-
\frac{c(\omega)}{m(\omega)\omega^2}S_\alpha
\right)^2
\right]
d\omega
\`\`\`

とする。$A=K+I$ は2モード全体の共通位相回転生成子であり、

\`\`\`math
\{A,S_\alpha\}=0
\`\`\`

だから $\{A,H_{\rm tot}\}=0$ である。従って全拡大Hamiltonian軌道で $A(t)=A(0)=\widehat A$ が厳密に成り立つ。

## S.4 調和浴の消去とDrude一般化Langevin方程式

調和浴自由度は線形なので、Zwanzig型の消去 [14] を適用できる。初期浴を固定した $\boldsymbol S(0)$ に条件付けたGaussian平衡状態から取ると、縮約運動は

\`\`\`math
\dot{\boldsymbol S}(t)
=
\boldsymbol S(t)\times
\left[
\boldsymbol\xi(t)
-
\int_0^t
\Gamma_{\rm D}(t-s)\dot{\boldsymbol S}(s)\,ds
\right]
\`\`\`

となる。等方Drude kernelを

\`\`\`math
\Gamma_{\rm D}(t)
=
\frac{g_{\rm D}}{\tau_{\rm D}}e^{-t/\tau_{\rm D}}
\`\`\`

とし、

\`\`\`math
E[\xi_\alpha(t)\xi_\beta(s)]
=
\Theta_{\rm D}\Gamma_{\rm D}(|t-s|)\delta_{\alpha\beta}
\`\`\`

とする。古典spin Brownian motionで摩擦と揺らぎを一体に扱うことはKubo--Hashitsume型の構造と整合する [56]。

指数kernelはreaction variableを加えて有限次元Markov系へ持ち上げられる。規格化後、

\`\`\`math
\dot{\boldsymbol n}=C_{\boldsymbol n}\boldsymbol y,
\qquad
C_{\boldsymbol n}\boldsymbol u=\boldsymbol n\times\boldsymbol u,
\`\`\`

\`\`\`math
\tau_{\rm D}d\boldsymbol y
=
-(I_3+g_{\rm D}C_{\boldsymbol n})\boldsymbol y\,dt
+
\sigma_{\rm D}d\boldsymbol W_t.
\`\`\`

回転拡散係数を

\`\`\`math
D_{\rm rot}
=
\frac{\sigma_{\rm D}^2}{2(1+g_{\rm D}^2)}
\`\`\`

と定める。

## S.5 固定作用上の平衡周辺分布

固定した $\boldsymbol S$ に対して浴座標を平行移動するとJacobianは1であり、浴分配関数は $\boldsymbol S$ の向きに依存しない。従って固定 $|\boldsymbol S|=\widehat A/2$ 上の平衡周辺分布は球面一様であり、$X=(1-n_z)/2$ の平衡分布は $U[0,1]$ である。

## S.6 無次元fast--slow系

$s=D_{\rm rot}t$、

\`\`\`math
\delta_{\rm D}
=
\sqrt{D_{\rm rot}\tau_{\rm D}},
\qquad
a_{\rm D}=1+g_{\rm D}^2
\`\`\`

とする。fast変数を平衡分散で規格化すると

\`\`\`math
d\boldsymbol n_s^\delta
=
\frac{\sqrt{a_{\rm D}}}{\delta_{\rm D}}
C_{\boldsymbol n_s^\delta}\boldsymbol v_s\,ds,
\`\`\`

\`\`\`math
d\boldsymbol v_s
=
-\frac1{\delta_{\rm D}^2}
(I_3+g_{\rm D}C_{\boldsymbol n_s^\delta})\boldsymbol v_s\,ds
+
\frac{\sqrt2}{\delta_{\rm D}}d\boldsymbol W_s.
\`\`\`

$C_{\boldsymbol n}^{\mathsf T}=-C_{\boldsymbol n}$ だからfast OU部分は $\boldsymbol n$ に一様な指数安定性を持つ。

## S.7 一次・二次corrector

極限球面拡散を

\`\`\`math
d\boldsymbol N_s
=
-2\boldsymbol N_s\,ds+B(\boldsymbol N_s)d\boldsymbol W_s
\`\`\`

と書く。ただし

\`\`\`math
P_{\boldsymbol n}=I_3-\boldsymbol n\boldsymbol n^{\mathsf T},
\`\`\`

\`\`\`math
B(\boldsymbol n)
=
\sqrt{\frac2{1+g_{\rm D}^2}}
(g_{\rm D}P_{\boldsymbol n}+C_{\boldsymbol n}).
\`\`\`

このとき $B(\boldsymbol n)B(\boldsymbol n)^{\mathsf T}=2P_{\boldsymbol n}$ である。

一次correctorを

\`\`\`math
\boldsymbol\chi
=
\frac{g_{\rm D}P_{\boldsymbol n}+C_{\boldsymbol n}}
{\sqrt{1+g_{\rm D}^2}}\boldsymbol v
\`\`\`

とする。$r=\boldsymbol n\cdot\boldsymbol v$、$\boldsymbol w=P_{\boldsymbol n}\boldsymbol v$ とし、

\`\`\`math
\boldsymbol\psi
=
\frac{r}{g_{\rm D}^2+4}
[(2-g_{\rm D}^2)P_{\boldsymbol n}-3g_{\rm D}C_{\boldsymbol n}]
\boldsymbol w
+
\boldsymbol n
\left(1-\frac{|\boldsymbol w|^2}{2}\right)
\`\`\`

とする。対応するPoisson方程式により、corrected variableの主項は極限球面拡散と一致する。

## S.8 同期couplingによる明示Wasserstein上界

\`\`\`math
\boldsymbol Y_s
=
\boldsymbol n_s^\delta
+
\delta_{\rm D}\boldsymbol\chi_s
+
\delta_{\rm D}^2\boldsymbol\psi_s
\`\`\`

とする。同期couplingでは

\`\`\`math
\|B(\boldsymbol n)-B(\boldsymbol m)\|_F^2
\leq4|\boldsymbol n-\boldsymbol m|^2
\`\`\`

であり、極限drift $-2\boldsymbol n$ と合わせた二乗距離の主項は非膨張である。

平衡fast初期条件でのGaussian momentを使い、

\`\`\`math
c_0=\sqrt3+\sqrt{\frac{13}{3}},
\qquad
c_G=\sqrt{18},
\`\`\`

\`\`\`math
c_R(g)=16.43\sqrt{1+g^2},
\`\`\`

\`\`\`math
A_{\rm str}(g)=4c_0+2c_R(g)+4c_G,
\`\`\`

\`\`\`math
B_{\rm str}=4c_0^2+4c_0c_G+c_G^2
\`\`\`

と置く。一つの保守的明示上界は

\`\`\`math
C_{\rm str}(g,S)
=
c_0
+
\frac{
A_{\rm str}(g)S
+
\sqrt{
A_{\rm str}(g)^2S^2
+
4(c_0^2+B_{\rm str}S)
}
}{2}.
\`\`\`

従って

\`\`\`math
W_1
(
\mathcal L(\boldsymbol n_T^{\tau_{\rm D}}),
\mathcal L(\boldsymbol N_T)
)
\leq
C_{\rm str}(g_{\rm D},D_{\rm rot}T)
\sqrt{D_{\rm rot}\tau_{\rm D}}.
\`\`\`

## S.9 作用比のJacobi縮約

$X=(1-N_z)/2$ とすると

\`\`\`math
\mathcal L_X
=
D_{\rm rot}
[
x(1-x)\partial_x^2+(1-2x)\partial_x
].
\`\`\`

固有値は $\lambda_\ell=D_{\rm rot}\ell(\ell+1)$ であり、スペクトルギャップは $2D_{\rm rot}$ である。

## S.10 有限時間一様化

Legendre展開から

\`\`\`math
D_{\rm TV}
(
\mathcal L(X_T),
U[0,1]
)
\leq
\min
\left\{
1,
\frac{\sqrt{q(3-q)}}{2(1-q)}
\right\},
\qquad
q=e^{-4D_{\rm rot}T}.
\`\`\`

R190AのWasserstein誤差と合わせてR190Bの $\eta_{190}$ を得る。

## S.11 Wasserstein誤差からCDF誤差への変換

1次元では

\`\`\`math
W_1(\mu,U)
=
\int_0^1|F_\mu(x)-x|\,dx.
\`\`\`

$F_\mu$ の単調性から

\`\`\`math
\sup_x|F_\mu(x)-x|
\leq
\sqrt{2W_1(\mu,U)}.
\`\`\`

## S.12 単回対称作用開口

$I_i=\widehat A_iX_i$ とし、

\`\`\`math
I_i^2
<
(c_{ij}^{\rm ap})^2\widehat A_i\widehat A_j
\`\`\`

を通過条件とする。これは

\`\`\`math
X_i
<
c_{ij}^{\rm ap}
\sqrt{\frac{\widehat A_j}{\widehat A_i}}
\`\`\`

と同値である。完全一様作用比では通過確率は右辺の閾値に等しい。

reaction coordinate $(x,p_x)$ と

\`\`\`math
D_{ij}^{\rm ap}
=
I_i^2-(c_{ij}^{\rm ap})^2\widehat A_i\widehat A_j
\`\`\`

を使い、

\`\`\`math
H_{ij}^{\rm ap}
=
\frac{p_x^2}{2M}
+
V_{\rm low}(x)
+
\Delta V(x)s_\epsilon(D_{ij}^{\rm ap})
\`\`\`

とすれば、低障壁と高障壁の間のincoming energy窓で有限Hamiltonian scattererを作れる。有限幅と有限散乱時間の誤差を $\varepsilon_{\rm sc}$ とする。

## S.13 反復衝突とrenewal条件

第 $m$ attempt直前の完全過去履歴を $\mathcal H_m$ とし、

\`\`\`math
\sup_x
\left|
P(X_m\leq x\mid\mathcal H_m)-x
\right|
\leq
\varepsilon_{{\rm ren},m}
\`\`\`

を仮定する。すると

\`\`\`math
\left|
P(i\to j\mid\mathcal H_m)
-
c_{ij}^{\rm ap}
\sqrt{\frac{\widehat A_j}{\widehat A_i}}
\right|
\leq
\varepsilon_{{\rm ren},m}
+\varepsilon_{{\rm sc},m}.
\`\`\`

有限attempt列では条件付き核誤差を加算して完全履歴TV誤差を抑えられる。R190A--R190Cだけから衝突後fast 浴の条件付き再平衡化または独立同分布性を主張しない。

## S.14 R161への校正、正則化資源、非主張

$\widehat\pi_i=\widehat A_i/\sum_k\widehat A_k$ とし、$\nu_{ij}c_{ij}^{\rm ap}=\kappa_Xa_{ij}$ と校正すれば、S.13のrenewal条件下でR161静的平方根率を条件付き核誤差内で回収する。

R164の正則化容量について一様な安全開口の十分条件は

\`\`\`math
c_{ij}^{\rm ap}
\leq
\sqrt{\frac{\delta q_{\min}}{1+\delta}}.
\`\`\`

従ってattempt frequencyは最悪 $O(\delta^{-1/2})$ まで増大し得る。これはK.8のR162熱的特殊化と同じ次数である。

R190A--R190Cは、無限Drude浴から有限浴を導くこと、容量 $\widehat A_i$ の生成機構、全2作用殻の完全microcanonical準備、反復衝突のrenewalを無条件に導くこと、R162の一般有向率を置き換えること、容量生成からlock、記録、選別、再調整までの単一装置統合、周期総収支を主張しない。
