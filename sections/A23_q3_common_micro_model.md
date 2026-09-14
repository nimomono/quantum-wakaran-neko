@number: W
@chapter: 付録
@title: M58 Q3共通ミクロ模型とR197有限時間統合
@status: Q3-1/Q3-2の共通ミクロ物理層。M37局所振動子信号、thermostatted 2-action shell、M57 dual-ballistic-TL moving-bath tracerを同一試行上で結合し、signal marginalではR86、full tracer marginalではR196A--R196CからR161/R185へ有限誤差で接続する。

## W.1 M58の責務と実在自由度

Q3-1とQ3-2の共通親模型をM58とする。M58はM37をsignal subsystem、M57をtransport subsystemとして同一試行上に含む古典開放模型であり、Q3-1はそのsignal marginal、Q3-2は同じ試行のsignalとtracerを含むfull marginalとして読む。

単一試行で物理的に存在する自由度は、M37の有限実振動子座標 $(q_i,p_i)$、2-action shellの作用・角自由度 $(K_1,K_2,\theta_1,\theta_2)$、辺ごとの二本のballistic wave channel、moving bath-frame carrier $Y_e$、その内部の平衡oscillator bath、1個のtracer位置 $X$、periodic/double-well potentialである。複素信号 $Z$ はM37実正準平面の派生表示であり独立実体ではない。

M58ではsignalをM37からM57へ後段で再標本化して受け渡さない。開始時から同じM37信号がthermostatted shellとballistic portへ弱く結合し、同じtracer $X_t$ が最後まで発展する。時計、終位置記録、resetまで含む反復周期統合は本付録の責務に含めない。

## W.2 M37信号とM57 current辞書の一致

1次元最近接格子でM37の目標生成子を

```math
h_L
=
\frac{\mathcal J_0^2}{2m}L_G+V_L
```

とし、最近接重みを $g_{i,i+1}=a^{-2}$ とする。R195A/R196Cと同じ

```math
\mathcal J_0=2m\nu
```

を採用すると、M37の辺成分は

```math
h_{i,i+1}
=-\frac{\mathcal J_0^2}{2ma^2}
=-\frac{\mathcal J_0\nu}{a^2}
```

となり、M57のsignal current辞書と厳密に一致する。従ってM37からR195Aへ移るための追加の結合再較正は不要である。

M37局所実正準座標から

```math
Z_i
=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

と置けば、M57のchiral変数

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2}
```

は隣接する実quadratureの固定線形正準結合である。従ってstate-dependent divisionや位相測定を必要とせず、固定passive portで物理的に結合できる。

## W.3 大作用carrierとsmooth shell容量

小パラメータ $0<\epsilon\leq\epsilon_0$ を取り、M37信号を

```math
Z^{(\epsilon)}
=\epsilon^{-1}z,
\qquad
S_{\rm ref}^{(\epsilon)}
=\epsilon^{-2}\bar S_{\rm ref}
```

とする。$z$ は規格化されたslow signalである。

well中心 $x_i$ に対する周期的 $C^3$ partition of unity $\chi_i(x)$ を

```math
\chi_i\geq0,
\qquad
\sum_i\chi_i=1,
\qquad
\chi_i(x_j)=\delta_{ij}
```

となるよう取る。正則化密度を

```math
r^\delta(x,z)
=
\sum_i\chi_i(x)
\left(
|z_i|^2+\delta q_i\bar S_{\rm ref}
\right)
```

とする。固定有限時間のsafe sectorで

```math
0<r_{\min}
\leq r^\delta(x,z)
\leq r_{\max}<\infty
```

を仮定し、以下で使う $x,z$ 微分ノルムが有限とする。

物理信号に対するshell容量係数を

```math
\alpha_\epsilon
=\epsilon^2\bar\alpha
```

とし、

```math
A(x,Z^{(\epsilon)})
=
\alpha_\epsilon
\sum_i\chi_i(x)
\left(
|Z_i^{(\epsilon)}|^2
+\delta q_iS_{\rm ref}^{(\epsilon)}
\right)
```

と置く。このとき

```math
A(x,Z^{(\epsilon)})
=\bar\alpha r^\delta(x,z)
=:A(x,z)
```

であり、

```math
A_{\min}=\bar\alpha r_{\min}>0,
\qquad
A_{\max}=\bar\alpha r_{\max}
```

は $\epsilon$ に依存しない。

## W.4 thermostatted 2-action shell

2本の作用を $K_1,K_2\geq0$、総作用を

```math
S=K_1+K_2>0
```

とし、shell Hamiltonianを

```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}2
[S-A(X,z)]^2
```

とする。作用比 $u=K_1/S\in[0,1]$ と角 $\theta_1,\theta_2$ を加え、総作用には採用開放SDE

```math
dS_t
=-\mu_{\rm sh}
\left[
\kappa_{\rm sh}(S_t-A_t)
-\frac{k_BT}{S_t}
\right]dt
+\sqrt{2\mu_{\rm sh}k_BT}\,dB_t,
```

```math
A_t=A(X_t,z_t)
```

を用いる。$u$ は $[0,1]$ 上の反射Brownian motion、角は円周上の拡散として熱化させる。$k_BT/S$ は2-action Liouville測度

```math
dK_1dK_2=S\,dSdu
```

のJacobianに対応するentropic driftである。

固定した $A>0$ に対する不変密度は

```math
\pi_A(S)
=\frac1{\mathcal Z_A}
S\exp\left[-\frac{\beta\kappa_{\rm sh}}2(S-A)^2\right],
\qquad
\beta=(k_BT)^{-1}.
```

有効potential

```math
\Phi_A(S)
=\frac{\kappa_{\rm sh}}2(S-A)^2-k_BT\log S
```

は

```math
\Phi_A''(S)
=\kappa_{\rm sh}+\frac{k_BT}{S^2}
\geq\kappa_{\rm sh}
```

を満たす。従ってfrozen shellの収縮rateを

```math
\lambda_{\rm sh}
=\mu_{\rm sh}\kappa_{\rm sh}
```

と取れる。

<!-- theorem-start:theorem -->
**定理（R197A：thermostatted 2-action shellの平均力と有限幅誤差）**

上のshellについて

```math
x(A)
=\sqrt{\frac{\beta\kappa_{\rm sh}}2}A,
```

```math
\Delta(x)
=\frac{e^{-x^2}}
{e^{-x^2}+\sqrt\pi x[1+\operatorname{erf}(x)]}
```

と置く。分配関数は

```math
\mathcal Z_A
=C
\left[
\frac{e^{-x(A)^2}}{\beta\kappa_{\rm sh}}
+A\sqrt{\frac{\pi}{2\beta\kappa_{\rm sh}}}
\left(1+\operatorname{erf}x(A)\right)
\right]
```

である。generalized force

```math
G_A(S)=\kappa_{\rm sh}(S-A)
```

の条件付き平均は厳密に

```math
\bar G(A)
=\frac{k_BT}{A}[1-\Delta(x(A))]
```

を満たす。従って任意のslow座標 $y$ に対して

```math
\bar F_y^{\rm sh}
=\bar G(A)\partial_yA
=k_BT[1-\Delta(x(A))]\partial_y\log r^\delta.
```

$x_{\min}=x(A_{\min})$、$\Delta_*=\Delta(x_{\min})$ とすれば

```math
\left|
\bar F_y^{\rm sh}
-k_BT\partial_y\log r^\delta
\right|
\leq
k_BT\Delta_*
|\partial_y\log r^\delta|.
```

従ってshellを実際に周辺化した条件付き自由エネルギーは、共通加法定数を除き

```math
F_{\rm sh}
=-k_BT\log r^\delta+E_{\rm width},
```

```math
|\partial_yE_{\rm width}|
\leq
k_BT\Delta_*|\partial_y\log r^\delta|
```

である。また二乗平均は

```math
\int G_A(S)^2\pi_A(dS)
=\kappa_{\rm sh}k_BT[1+\Delta(x(A))]
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R197A）**

$K_1=uS$、$K_2=(1-u)S$ と変数変換すると $dK_1dK_2=S\,dSdu$ である。角と $u$ を積分して上の不変密度を得る。$a=\beta\kappa_{\rm sh}/2$ とすると

```math
\int_0^\infty
S e^{-a(S-A)^2}dS
=
\frac{e^{-aA^2}}{2a}
+\frac{A\sqrt\pi}{2\sqrt a}
[1+\operatorname{erf}(\sqrt a A)].
```

これを $A$ で微分し、$k_BT\partial_A\log\mathcal Z_A=\langle G_A\rangle$ を用いれば平均力式を得る。二乗平均は同じGaussian積分を2階まで行えば表示式となる。証明終。
<!-- theorem-end:proof -->

## W.5 Brownian tracerと時間発展信号に対するfast--slow averaging

slow変数を

```math
Y=(X,\operatorname{Re}z,\operatorname{Im}z)
```

とまとめる。shell平均を除いたslow driftを $b_0(t,Y)$、shell generalized forceの結合係数を $c(Y)$、slow Brownian diffusion matrixを $\Sigma$ とし、$\Sigma$ は $S$ に依存しないとする。

```math
dY_t
=\left[
b_0(t,Y_t)+c(Y_t)G_{A(Y_t)}(S_t)
\right]dt+\Sigma dW_t.
```

frozen-shell generatorからmobilityを除いた作用素を

```math
L_A
=k_BT\partial_S^2
-\left[
\kappa_{\rm sh}(S-A)-\frac{k_BT}{S}
\right]\partial_S
```

とし、centered forceを

```math
h_A(S)=G_A(S)-\bar G(A)
```

とする。

<!-- theorem-start:theorem -->
**定理（R197B：M58 shellの有限時間fast--slow averaging）**

$A\in[A_{\min},A_{\max}]$、$b_0,c,A$ がsafe compact sectorで必要な2階微分まで有界Lipschitz、slow diffusion $\Sigma$ がshell変数に依存せず、shellを条件付き平衡 $S_0\sim\pi_{A(Y_0)}$ から開始するとする。平均零Poisson方程式

```math
-L_A\phi_A=h_A,
\qquad
\int\phi_A\,d\pi_A=0
```

は一意解を持ち、

```math
\partial_S\phi_A(S)
=-\frac{
\int_0^S h_A(u)\pi_A(u)du
}{k_BT\pi_A(S)},
```

```math
|\partial_S\phi_A|\leq1
```

を満たす。

```math
K_0
=\sup_Y\|c(Y)\phi_{A(Y)}\|_{L^2(\pi_A)},
```

```math
K_B
=\sup_Y
\|\Sigma^{\mathsf T}\nabla_Y[c(Y)\phi_{A(Y)}]\|_{L^2(\pi_A)},
```

```math
K_L
=\sup_Y
\|\mathcal L_{\rm slow}[c(Y)\phi_{A(Y)}]\|_{L^2(\pi_A)},
```

```math
C_c=\sup_Y\|c(Y)\|
```

とする。これらはsafe compact sectorで有限である。shell forceを条件付き平均 $\bar G(A)$ へ置換したaveraged processを $\bar Y_t$ とし、そのdriftのLipschitz定数を $L_{\rm av}$ とすれば、同じslow Brownian motionによるcouplingで

```math
\begin{aligned}
&\left[
\mathbb E\sup_{0\leq t\leq T}
|Y_t-\bar Y_t|^2
\right]^{1/2}
\\
&\leq
e^{L_{\rm av}T}
\left[
2C_c\sqrt{\frac{2k_BTT}{\mu_{\rm sh}}}
+\frac{2K_0+TK_L+2\sqrt T K_B}{\mu_{\rm sh}}
\right].
\end{aligned}
```

従って固定有限時間でstrong averaging誤差は $O(\mu_{\rm sh}^{-1/2})$ である。

さらにshell fluctuationのGreen--Kubo積分は

```math
\int_0^\infty
|\operatorname{Cov}_{\pi_A}[h_A(S_t),h_A(S_0)]|dt
\leq
\frac{k_BT[1+\Delta_*]}{\mu_{\rm sh}}.
```

tracer mobilityを $\mu_X=1/\gamma_X$ とすると、shell fluctuationがtracerへ加える拡散は

```math
D_{\rm sh}^{\rm add}
\leq
\frac{
\mu_X^2\|\partial_XA\|_\infty^2
k_BT(1+\Delta_*)
}{\mu_{\rm sh}},
```

従って $D_0=\mu_Xk_BT$ に対する相対誤差は

```math
\varepsilon_{\rm sh,av}
:=\frac{D_{\rm sh}^{\rm add}}{D_0}
\leq
\frac{
\mu_X\|\partial_XA\|_\infty^2(1+\Delta_*)
}{\mu_{\rm sh}}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R197B）**

$\Phi_A''\geq\kappa_{\rm sh}$ からfrozen shellはrate $\mu_{\rm sh}\kappa_{\rm sh}$ 以上で指数収縮する。1次元reversible diffusionの積分表示からPoisson解を得る。centered forceのLipschitz定数と強凸定数がともに $\kappa_{\rm sh}$ なので $|\partial_S\phi_A|\leq1$ である。$c(Y)\phi_{A(Y)}(S)$ にItô公式を適用し、Poisson方程式を代入するとcentered forceの時間積分はendpoint項、slow drift項、slow Brownian martingale、shell Brownian martingaleへ分解される。前3者をCauchy--Schwarz、最後をDoob--BDGで評価し、Gronwall不等式を適用して表示式を得る。covarianceにはspectral-gap収縮とR197Aの二乗平均を用いる。証明終。
<!-- theorem-end:proof -->

## W.6 loaded M37の安定性

shell HamiltonianのM37信号への反作用は、格子点 $i$ では局所onsite perturbationとして

```math
i\mathcal J_0\dot z_i\big|_{\rm sh}
=-\alpha_\epsilon
G_A(S)\chi_i(X)z_i
```

と書ける。ballistic portはA22のbilinear weak tapを同じM37 quadratureへ結合する。

<!-- theorem-start:theorem -->
**定理（R197C：shell・ballistic-port負荷下のM37有限時間安定性）**

R86の仮定に加え、W.3のsafe sectorとR197A/Bのshell条件を仮定する。ballistic-port couplingを $\epsilon_{\rm port}=\epsilon$ とし、physical signal作用を $O(\epsilon^{-2})$ とする。このときport incident energyは有限非零のscaleに保てる一方、M37へのrelative port backreactionは

```math
\varepsilon_{\rm port\to sig}(T)
\leq C_{\rm back}(T)\epsilon^2
```

である。

shell平均反作用は一般に

```math
\varepsilon_{\rm sh,mean}^{37}(T)
\leq
\frac{Tk_BT}{\mathcal J_0r_{\min}}\epsilon^2,
```

centered shell fluctuationは

```math
\varepsilon_{\rm sh,fluc}^{37}(T)
\leq
\frac{2\bar\alpha\epsilon^2}{\mathcal J_0}
\sqrt{\frac{2k_BTT}{\mu_{\rm sh}}}
+O\left(\frac{\epsilon^2}{\mu_{\rm sh}}\right).
```

従ってM58 signal marginalとR86理想信号の有限時間誤差は

```math
\begin{aligned}
\varepsilon_{\rm sig}^{58}(T)
\leq{}&
\varepsilon_{\rm car}(T)
+C_{\rm back}(T)\epsilon^2
\\
&+\frac{Tk_BT}{\mathcal J_0r_{\min}}\epsilon^2
+\frac{2\bar\alpha\epsilon^2}{\mathcal J_0}
\sqrt{\frac{2k_BTT}{\mu_{\rm sh}}}
+O\left(\frac{\epsilon^2}{\mu_{\rm sh}}\right).
\end{aligned}
```

したがってM57を同時に接続した同一試行上でもQ3-1のR86縮約は保持される。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R197C）**

shell平均項とcentered項を分離する。平均項はR197Aと $r^\delta\geq r_{\min}$ を使い、centered項はR197BのPoisson-corrector評価をM37のDuhamel公式へ代入する。ballistic portはA22の有限時間backreaction評価を用いる。三角不等式でR86の裸carrier誤差へ加えれば表示式を得る。証明終。
<!-- theorem-end:proof -->

## W.7 共通weak familyと時間尺度窓

R196A--R196Bと共通の小パラメータ $\epsilon$ を用い、

```math
\kappa_p=\epsilon^2\bar\kappa_p,
\qquad
M_e=\epsilon^2\bar M_e,
```

```math
\gamma_X=\epsilon^4\bar\gamma,
\qquad
k_BT=\epsilon^4\bar\gamma D_0,
```

```math
M_X=\epsilon^6\bar M_X,
\qquad
V_{\rm per}=k_BT\bar V_{\rm per}
```

とする。さらに任意の $\zeta>0$ に対し

```math
\mu_{\rm sh}
=\bar\mu_{\rm sh}\epsilon^{-4-\zeta}
```

とする。$\kappa_{\rm sh},A_{\min},D_0$ は固定する。

このとき

```math
\lambda_{\rm sh}^{-1}
=O(\epsilon^{4+\zeta}),
\qquad
\tau_X=\frac{M_X}{\gamma_X}=O(\epsilon^2),
```

かつ

```math
x_{\min}^2
=\frac{\kappa_{\rm sh}A_{\min}^2}{2k_BT}
=O(\epsilon^{-4}).
```

従ってfinite-width誤差は指数的に消え、

```math
\varepsilon_{\rm sh,av}=O(\epsilon^\zeta),
```

strong shell averagingは $O(\epsilon^{\zeta/2})$、M37への平均shell反作用は $O(\epsilon^6)$、port backreactionとmoving-frame loadingは $O(\epsilon^2)$ となる。特に $\zeta=2$ ならgenerator-level shell誤差を既存M57 weak familyと同じ $O(\epsilon^2)$ へ揃えられる。

十分小さい有限 $\epsilon$ では

```math
\lambda_{\rm sh}^{-1}
\ll\tau_X
\ll\tau_p
\ll\lambda_Y^{-1}
\ll T_{\rm sig}
```

を満たす非空なparameter windowを取れる。

## W.8 R196B/R196Cへの接続

R197A/Bでshellを消去したoverdamped tracer driftは

```math
\begin{aligned}
dX_t
={}&U_e(t)dt
+D_0[1-\Delta(x(A_t))]
\partial_x\log r^\delta(X_t,z_t)dt
\\
&-\mu_XV_{\rm per}'(X_t)dt
+\sqrt{2D_0}\,dW_t+dR_t.
\end{aligned}
```

$R_t$ はR196B既存のGLE、overdamped、homogenization残差にR197のfinite-width・averaging残差を加えたものである。中心matching

```math
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

の下で、R196A--R196Cのcurrent drift、diffusion、well-index reductionはそのまま適用できる。

M58からR161への生成子誤差を

```math
\begin{aligned}
\varepsilon_{58}
\leq C_{58}(&
\varepsilon_{\rm sig}^{58}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sh,av}
+\varepsilon_{\rm port}
+\varepsilon_{\rm prop}
+\varepsilon_{\rm track}
\\
&+\varepsilon_{\rm load}
+\varepsilon_{\rm GLE}
+\varepsilon_{\rm od}
+\varepsilon_{\rm hom}
+\varepsilon_{\rm EK}
+a^2)
\end{aligned}
```

とする。同じ上流誤差は一度だけ数える。

<!-- theorem-start:theorem -->
**定理（R197：Q3-1/Q3-2共通ミクロ模型の有限時間統合）**

R86、R195A、R196A--R196C、R197A--R197Cの仮定を同時に満たし、固定有限時間 $[0,T]$ のsafe sectorで $r^\delta\geq r_{\min}>0$ とする。このとき単一のM58古典開放過程について次が同時に成り立つ。

1. signal marginalだけを見ると、M37規格化包絡はR86のSchrödinger型空間信号へ誤差 $\varepsilon_{\rm sig}^{58}(T)$ で縮約する。従ってM58はQ3-1の明示ミクロ証人である。
2. 同じ試行のsignal、shell、ballistic channels、moving bath frame、平衡bath、tracerを保持すると、そのwell-index過程の生成子はR161生成子へ誤差 $\varepsilon_{58}$ で一致する。同じ初期位置分布から開始した経路周辺分布は

```math
\sup_{0\leq t\leq T}
D_{\rm TV}(p_t^{58},p_t^{161})
\leq T\varepsilon_{58}
```

を満たす。
3. $-k_BT\log r^\delta$ は外部から挿入するポテンシャルではなく、同じM58内のthermostatted 2-action shellを条件付きGibbs分布で消去したpotential of mean forceとして得られる。
4. R161極限過程にはR185をそのまま適用できる。従ってQ3-2の時間対称Newton則に残る独立残差はM58からR161への持上げ誤差、R185の正則化残差 $O(\delta)$、格子残差 $C_{185,a}a^2$ である。

共通weak familyで $\zeta=2$ とし、R86の弱carrier極、$\epsilon\to0$、格子極・正則化極をsafe-sector条件を保つ順序で取れば

```math
\varepsilon_{\rm sig}^{58}\to0,
\qquad
\varepsilon_{58}\to0.
```

従ってQ3-1とQ3-2は別々のミクロ模型ではなく、同一M58過程の異なる周辺縮約として同時に実現される。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R197）**

signal sectorにはR86とR197Cを適用する。shell sectorにはR197A/Bを適用し、R196Bで従来入力していたosmotic forceを同じ試行のthermostatted shellの平均力で置き換える。current情報はR195AからR196Aのballistic moving frameへ伝わり、R196Bの平衡bathとperiodic homogenizationを経てR196Cのwell-index生成子へ縮約する。各近似の上流残差を一度だけ合成して $\varepsilon_{58}$ を得る。有限状態Markov生成子のDuhamel公式と全変動距離の収縮性から $D_{\rm TV}\leq T\varepsilon_{58}$ を得る。最後にR161のcanonical path lawへR185を適用する。証明終。
<!-- theorem-end:proof -->

## W.9 責務境界

R197はM37信号源とM57 tracerを同一試行の古典開放模型へ統合する結果である。有限閉鎖Hamiltonian全系への持上げは要求しない。Q3-1/Q3-2のA1では本M58を共通証人として使える。

一方、A2はM58の採用SDE/PDEを直接数値発展して主要観測量を再現することを別途要求する。また、clock、終位置record、resetを含む反復周期、連続空間一様極限、多粒子拡張はR197の結論に含めない。
