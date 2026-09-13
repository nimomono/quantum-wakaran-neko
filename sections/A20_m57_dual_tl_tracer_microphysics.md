@number: T
@chapter: 付録
@title: M57 dual-TL tracerミクロ模型とR161有限誤差持上げ
@status: Q3の現行ミクロ物理層。M37/M54実正準空間信号を、2作用状態数、左右独立open TL、局在tracerへ接続し、R195A--R195DでR161生成子へ有限誤差で持ち上げる。R161/R162/R185の数学核は変更しない。

## T.1 M57の責務と実在自由度

M57はQ3の粒子位置輸送に対する現行ミクロ模型である。M54の実正準信号とM37の空間信号実装は残し、従来R162のopen Poisson reservoirへ直接委ねていた粒子輸送のミクロ物理を、局在tracerと明示bathへ置き換える。単一試行で物理的に存在する自由度は、実正準信号、1個のtracer座標 $X$、2作用状態数sector、左右独立の有限transmission-line channel、open terminationである。複素信号 $Z$ は実正準平面の派生表示であり独立実体ではない。

有限格子の辺 $e=\{i,j\}$ ごとに

```math
R_i=|Z_i|^2,
\qquad
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
```

```math
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。左右channelは同一1次元鎖の運動量符号ではなく、独立な2本の物理channelとする。これにより各channel内部へweak pinningとopen terminationを入れても、current情報はchannel energy差として保持できる。

## T.2 R195A：chiral作用と2作用状態数

直接計算から

```math
I_{e,+}+I_{e,-}=R_i+R_j,
```

```math
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j)
```

が厳密に成り立つ。nearest-neighbor Schrödinger特殊化で $\mathcal J_0=2m\nu$ とし、辺結合を $h_{ij}=-\mathcal J_0\nu/a^2$ と取る向き規約では、信号辺流は

```math
J_{ij}^{\rm sig}
=\frac{\nu}{a^2}(I_{e,+}-I_{e,-}).
```

tracer位置に付随する2作用sector $(K_1,\theta_1),(K_2,\theta_2)$ に

```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}2
[K_1+K_2-A^\delta(X,Z)]^2,
```

```math
A_i^\delta
=\alpha\,[R_i+\delta q_iS_{\rm ref}]
```

を置く。strict-shell極では

```math
\int_0^\infty dK_1\int_0^\infty dK_2\,
\delta(A-K_1-K_2)=A
```

なので、条件付きLiouville状態数は

```math
\Omega_i^\delta\propto R_i^\delta,
\qquad
R_i^\delta=R_i+\delta q_iS_{\rm ref}.
```

従って開始位置重みはR164と同じ

```math
\pi_i^\delta
=\frac{R_i^\delta}{\sum_kR_k^\delta}
```

であり、運動中のpotential of mean forceは $-k_BT\log R^\delta$ を与える。毎時刻Born再標本化を行うのではなく、同じtracerがこの自由エネルギーとTL bathの下で移動する。

<!-- theorem-start:theorem -->
**定理（R195A：M57 chiral作用・状態数恒等式）**

上の定義の下で、chiral作用の和・差恒等式は全信号振幅について厳密である。strict 2-action shellでは条件付きLiouville状態数は $A_i^\delta$ に比例し、規格化位置重みは $\pi_i^\delta$ となる。有限shell stiffnessでは付録A12の有限殻補正をそのまま適用できる。
<!-- theorem-end:theorem -->

## T.3 dual open TL

各 $\sigma=\pm$ channelを $N$ cellのpinned weakly-anharmonic LC chainとして

```math
H_{{\rm TL},\sigma}
=
\sum_{n=1}^N\frac{Q_{\sigma n}^2}{2C}
+
\sum_n\frac{(\Phi_{\sigma,n+1}-\Phi_{\sigma n})^2}{2L}
+
\sum_n\frac{\Phi_{\sigma n}^2}{2L_0}
+
\frac{\beta}{4}\sum_n(\Phi_{\sigma,n+1}-\Phi_{\sigma n})^4.
```

遠端はDrude/Langevin terminationへ接続する。線形速度尺度とDrude memoryを

```math
c=\frac{a}{\sqrt{LC}},
\qquad
\tau_D=\Omega_D^{-1}
```

とする。signal chiral modeとのlocal portは、normal-mode表示で

```math
H_{\rm port}
=\epsilon\sum_{\sigma=\pm}\int dk\,
[g_kC_{e,\sigma}^*b_{\sigma k}+\mathrm{c.c.}]
```

と書く。portは状態依存除算を行わず、左右のsignal actionを対応channelへ線形に注入する。

harmonic driftを $Y=(\Phi,Q)$ について

```math
\dot Y=A_NY+\text{boundary noise},
```

```math
A_N=
\begin{pmatrix}
0&C^{-1}I\\
-K_N&-\Gamma_N
\end{pmatrix},
\qquad
K_N=L_0^{-1}I+L^{-1}\Delta_N
```

とする。$A_N$ がHurwitzで、無次元化したLyapunov方程式

```math
\bar A_N^{\mathsf T}P_N+P_N\bar A_N=-I,
\qquad
\bar A_N=A_N/\omega_0,
\qquad
\omega_0=(LC)^{-1/2}
```

の正定値解が存在するとする。固定safe shellでanharmonic Jacobian perturbationを $\|\Delta\bar A\|\le\delta_{\rm anh}$ と評価し、

```math
2\|P_N\|\delta_{\rm anh}<1
```

を仮定する。

このとき保守的なstate-contraction rateとして

```math
\lambda_{\rm mix}
=\omega_0
\frac{1-2\|P_N\|\delta_{\rm anh}}{2\|P_N\|}>0
```

を用いる。Drude側を含めた最遅rateを

```math
\lambda_*=\min\{\lambda_{\rm mix},\Omega_D\}
```

とする。

## T.4 R195B：port slaving・有限mixing・force correlation

signal variation timeを $T_{\rm sig}$ とし、directivity、dispersion、backreactionをそれぞれ $\varepsilon_{\rm dir},\varepsilon_{\rm disp},\varepsilon_{\rm back}$ で評価する。linear port responseとexponential relaxationを合成したM57の採用仮定は

```math
|e_{e,\sigma}(t)-C_pI_{e,\sigma}(t)|
\le
C_pI_*
\left[
C_0e^{-\lambda_{\rm mix}t}
+\frac{1}{\lambda_{\rm mix}T_{\rm sig}}
+\varepsilon_{\rm dir}
+\varepsilon_{\rm disp}
+\varepsilon_{\rm back}
\right].
```

またtracer force observableについてconnected correlationが

```math
|\langle\delta F(t)\delta F(0)\rangle|
\le C_Fe^{-\lambda_*t}
```

を満たすsectorを用いる。規格化積分相関時間には

```math
\tau_{\rm corr}\le A_F/\lambda_*
```

を得る。mixing tolerance $\varepsilon$ までの十分時間は

```math
\tau_{\rm mix}(\varepsilon)
\le
\lambda_{\rm mix}^{-1}\log(C_0/\varepsilon).
```

<!-- theorem-start:theorem -->
**定理（R195B：M57 finite-time bath slaving）**

上のHurwitz条件、safe-shell perturbation条件、有限band port response条件の下で、TL energy densityのchiral作用への追従誤差、mixing time、force-correlation timeは上式で有限に評価できる。閉じたmomentum-conserving 1D FPUT鎖は本定理の対象に含めない。
<!-- theorem-end:theorem -->

## T.5 R195C：Green--Kubo/FDT、tracer mobility、Kramers matching

局所drifting-Gibbs近似が有効な弱current sectorで、tracerに働くTL forceを

```math
F_{\rm TL}
=-\Gamma(\dot X-u_{\rm TL})+\xi+r_{\rm GK}
```

と縮約する。完全反射に近い1次元scattererの低速度極では

```math
\Gamma
=\frac{4(e_++e_-)}{c}+O(\varepsilon_{\rm GK}),
```

```math
u_{\rm TL}
=\frac c2\frac{e_+-e_-}{e_++e_-}
+O(\varepsilon_{\rm GK}).
```

FDTは

```math
D_0=\frac{k_BT}{\Gamma}
```

を与える。classical TLの採用band/cutoffで $e_++e_-=k_BT/a$ と規格化すると

```math
D_0=\frac{ac}{4}.
```

tracerのperiodic potentialによる長時間mobility/diffusion suppressionを $g_K\in(0,1]$ とし、

```math
D_{\rm hop}=g_KD_0.
```

Q3 diffusivity $\nu$ との中心matchingを

```math
\boxed{
g_Kc=\frac{4\nu}{a}
}
```

と置けば

```math
D_{\rm hop}=\nu
```

となる。port slavingを使ったdriftも同じmatchingから

```math
u_{\rm hop}
=\frac{2\nu}{a}
\frac{I_+-I_-}{I_++I_-}
+O(\varepsilon_{\rm phys})
```

を得る。状態数sectorは独立に $\nu\partial_x\log\rho$ のosmotic driftを供給する。

<!-- theorem-start:theorem -->
**定理（R195C：M57 FDT--Kramers matching）**

R195Bのfast-bath条件、弱current drifting-Gibbs条件、完全反射近似、overdamped periodic-tracer縮約の下で、$g_Kc=4\nu/a$ は長時間diffusion $D_{\rm hop}=\nu$ とsignal-current drift係数を同時に一致させる。FDT/Kramers近似誤差は $\varepsilon_{\rm phys}$ へまとめる。
<!-- theorem-end:theorem -->

## T.6 R195D：R161生成子への有限誤差持上げ

edge chiralityを

```math
r_{ij}
=\frac{I_+-I_-}{I_++I_-}
```

とする。symmetric barrier interpolation $R_b=(R_i^\delta+R_j^\delta)/2$ と中心matching後のKramers fluxを

```math
q_{ij}^+
=\frac{\nu R_b}{a^2}e^{r_{ij}},
\qquad
q_{ij}^-
=\frac{\nu R_b}{a^2}e^{-r_{ij}}
```

と書けば、

```math
T_{ij}^{57}=q_{ij}^++q_{ij}^-
=\frac{2\nu R_b}{a^2}\cosh r_{ij},
```

```math
J_{ij}^{57}=q_{ij}^+-q_{ij}^-
=\frac{2\nu R_b}{a^2}\sinh r_{ij}.
```

従って

```math
k_{i\to j}^{57}
=\frac{T_{ij}^{57}+J_{ij}^{57}}{2R_i^\delta}
```

はR161の形式を厳密に持つ。$\delta=0$ かつsmooth nearest-neighbor sectorでは

```math
J_{ij}^{57}
=J_{ij}^{\rm sig}\frac{\sinh r_{ij}}{r_{ij}}
=J_{ij}^{\rm sig}[1+O(a^2)].
```

有限時間 $0\le t\le T$ の生成子差を

```math
\varepsilon_{57}
=
\sup_{t\le T}\max_i\sum_{j\ne i}
|k_{i\to j}^{57}-k_{i\to j}^{161}|
```

とする。node-free safe sectorでは

```math
\varepsilon_{57}
\le
C_{57}
\left(
\varepsilon_{86}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm port}
+\varepsilon_{\rm mix}
+\varepsilon_{\rm corr}
+\varepsilon_{\rm FDT}
+\varepsilon_K
+\varepsilon_{\rm back}
+a^2
\right).
```

R161実現同値の有限時間比較から、同じ初期位置分布について

```math
\sup_{t\le T}
D_{\rm TV}(p_t^{57},p_t^{161})
\le T\varepsilon_{57}.
```

<!-- theorem-start:theorem -->
**定理（R195D：M57からR161への有限時間持上げ）**

R195A--R195Cの仮定とnode-free smooth sectorを仮定する。M57 tracerのcoarse-grained well-index processはR161形式の有向率を持ち、signal-currentを使う理想R161生成子との差は上の $\varepsilon_{57}$ で有限時間制御できる。R162はこの理想jump lawの参照実現、R185は同じR161前向き経路法則からの時間反転・時間対称Newton縮約として再利用できる。
<!-- theorem-end:theorem -->

## T.7 明示parameter witness

仮定集合が空でないことを確認するdimensionless witnessとして

```math
a=1,
\quad N=4,
\quad L=C=\frac1{16},
\quad L_0=1,
```

```math
R_b=0.66834,
\quad\Omega_D=8,
\quad\beta=0.05,
\quad\Phi_*=0.5,
```

```math
g_K=5.0\times10^{-4},
\quad c=16,
\quad\nu=2.0\times10^{-3}
```

を取る。`tools/verify_m57_tl_tracer.py` は、この値についてharmonic driftの最遅減衰率、Lyapunov margin、$\lambda_{\rm mix}$、$\tau_{\rm corr}$、$\tau_{\rm mix}$、$g_Kc=4\nu/a$、$D_{\rm hop}=\nu$、drift matching、$\sinh r/r$ の二次補正を独立に再計算する。現在のwitnessでは

```math
\lambda_H\simeq0.9630,
\qquad
\lambda_{\rm mix}\simeq0.15768,
```

```math
\tau_{\rm corr}\lesssim6.342,
\qquad
\tau_{\rm mix}(1\%)\lesssim29.21,
```

```math
T_{\rm res}=250,
\qquad
T_{\rm sig}=500
```

となり、fast-bath hierarchyは非空である。

## T.8 責務境界

1. M57はQ3粒子輸送の現行ミクロ物理層であり、Q1/Q2のR191測定器を置き換えない。
2. R161は共通数学interfaceとして維持し、M57固有にしない。
3. R162のPoisson reservoirはM57の基礎的実体ではなく、R195Dが比較するideal jump referenceである。
4. R184は旧M37--M54空間率latchの補助結果として保持するが、M57主線の必須依存にはしない。
5. R185の時間反転率は同じ前向き経路法則からBayes構成し、物理的な逆時間bathを導入しない。
6. closed momentum-conserving 1D FPUT chain、外部servo、状態依存除算器、毎時刻のBorn再標本化をM57へ導入しない。
7. continuous-space一様極限、多粒子、全周期のsource--clock--record統合は別の強化課題である。
