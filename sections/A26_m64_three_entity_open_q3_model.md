@number: Z
@chapter: 付録
@title: M64 三実体・最小古典開放系Q3共通模型
@status: M60/M61/M63をまだ置換しないactive replacement candidate。古典coherent signal、classical tracer、signal-driven moving thermal reservoirの三実体だけを正本候補とし、R203A--R203Dでsignal density/current、phase-volume free energy、moving Langevin縮約、R161 finite-volume接続を整理する。固定Q3-1/Q3-2達成判定、A1/A2判定、required主線は本付録追加だけでは変更しない。

## Z.1 責務と三実体

M64はQ3-1/Q3-2に必要な位置過程を、次の三つの古典的実体から構成する最小共通模型候補である。

1. classical coherent signal：M37型の実正準oscillator network。
2. classical tracer：一つの位置・運動量対 $(X,P_X)$。
3. signal-driven moving thermal reservoir：signal densityに応じて内部phase volumeが変わり、signal currentに応じたlocal mean flowを持ち、tracerへ摩擦と熱揺らぎを与える一つの古典環境。

複素包絡 $Z$、density $\rho$、current $j$、reservoir mean flow $U$、density scaling $\lambda_\alpha$ は、三実体から作る派生量またはcollective variableであり、独立した実体とはしない。

M64の因果鎖を

```text
M37 signal
   ↓
(ρ,j)
   ├─ ρ → reservoir phase volume → osmotic mean force
   └─ j/ρ → reservoir mean flow
                         ↓
                moving thermal reservoir
                         ↓
                     tracer X
                         ↓
                finite-volume R161
                         ↓
                      R185
```

とする。

M64は採用開放SDEを正本候補としてよい。single-field Hamiltonian化、finite-bath化、current transducerの完全Hamiltonian散乱導出はM64本体の成立条件に含めず、独立strengtheningとする。

## Z.2 signal、tracer、局所読出し量

signal sectorはM37/R86を再利用する。実正準signalから得る派生複素包絡を $Z_i$ とし、

```math
\rho_i=|Z_i|^2
```

とする。edge $e=(i,j)$ ごとに

```math
C_{e,+}
=
\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}
=
\frac{Z_i+iZ_j}{\sqrt2},
```

```math
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。

tracerは独立した古典粒子 $(X,P_X)$ とする。M64本体ではkink、domain wall、Duffing shell、PN wellをtracerの定義に要求しない。

tracer近傍を読む固定partition of unityを

```math
\chi_i(X)\ge0,
\qquad
\sum_i\chi_i(X)=1
```

とする。正則化signal densityを

```math
r_i^\delta
=
\delta q_i
+
\frac{|Z_i|^2}{N_0}
```

とし、

```math
r_X^\delta
=
r_*
\exp\left[
\sum_i
\chi_i(X)
\log\frac{r_i^\delta}{r_*}
\right]
```

をtracer-local densityとする。node-free smooth sectorでは

```math
\partial_X\log r_X^\delta
=
\partial_X\log\rho(X,t)
+
O(\varepsilon_{\rm width}+\delta)
```

を要求する。

## Z.3 R203A：signal density/current dictionary

<!-- theorem-start:theorem -->
**定理（R203A：M64 signal density/current dictionary）**

上のedge変換について厳密に

```math
I_{e,+}+I_{e,-}
=
|Z_i|^2+|Z_j|^2,
```

```math
I_{e,+}-I_{e,-}
=
2\operatorname{Im}(Z_i^*Z_j)
```

が成立する。局所chiralityを

```math
r_e
=
\frac{
I_{e,+}-I_{e,-}
}{
I_{e,+}+I_{e,-}+\delta I_0
}
```

とする。M37/R86のsafe narrow-band sectorと既存current dictionaryの下で、固定係数 $c_J$ を選ぶと

```math
c_Jr_e
=
\frac{j_e}{\rho_e}
+
O(
a^2
+
\delta
+
\varepsilon_{\rm env}
)
```

を得る。nearest-neighbor Schrödinger特殊化では $c_J=2\nu/a$ とできる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203A）**

和・差恒等式は $C_{e,\pm}$ の定義を直接展開すれば得られる。後半はR195A/R202E1で用いた同じ局所current identityをM64表記へ移したものであり、smooth narrow-band近似とdensity正則化の誤差だけを残す。証明終。
<!-- theorem-end:proof -->

R203Aは新しいcurrent機構を導入しない。M64ではcurrent情報をtracer位置で直接散乱して読むのでなく、reservoirのlocal collective flowへ渡す入力辞書として使う。

## Z.4 R203B：signal-driven moving phase-volume reservoir

reservoirの条件付き内部自由度を $(\zeta_\alpha,\Pi_\alpha)$ とし、固定signal、tracer位置、reservoir mean flowに対する内部Hamiltonianを

```math
H_{\rm res}
=
\sum_\alpha
\left[
\frac{
(\Pi_\alpha-m_\alpha U)^2
}{
2m_\alpha
}
+
\frac{
m_\alpha\omega_\alpha^2
}{2}
\left(
\lambda_\alpha\zeta_\alpha-d_\alpha R
\right)^2
\right]
```

とする。ここで $R$ はreservoir内部のrelative-coordinate shiftを許す補助量であり、partition identityにはその具体的担体を要求しない。

density scalingを

```math
\lambda_\alpha
=
\left(
\frac{r_X^\delta}{r_*}
\right)^{-w_\alpha},
\qquad
w_\alpha>0,
\qquad
\sum_\alpha w_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R203B：moving phase-volume reservoirの条件付きfree energy）**

固定 $r_X^\delta>0$、$U$、$R$ に対して上のreservoirをcanonicalに積分すると、

```math
Z_{\rm res}(r_X^\delta,U,R)
=
Z_{\rm res}^0
\frac{r_X^\delta}{r_*}
```

が厳密に成立する。従って条件付きinternal free energyは

```math
F_{\rm res}
=
-k_BT\log r_X^\delta+C_{\rm res},
```

```math
\partial_UF_{\rm res}
=
\partial_RF_{\rm res}
=
0
```

を満たし、tracerへの条件付きmean forceは

```math
F_X^{\rm osm}
=
k_BT\,\partial_X\log r_X^\delta
```

である。

mean flow $U$ は運動量分布の平行移動としてphase-volume Jacobianを変えず、density scalingだけが座標積分のJacobianを変える。従って同じreservoir内でdensity free-energy sectorとmean-flow sectorを分離できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203B）**

各modeで

```math
P_\alpha
=
\Pi_\alpha-m_\alpha U,
\qquad
Q_\alpha
=
\lambda_\alpha\zeta_\alpha-d_\alpha R
```

と変数変換する。運動量側は平行移動なので $d\Pi_\alpha=dP_\alpha$、座標側は

```math
d\zeta_\alpha
=
\lambda_\alpha^{-1}dQ_\alpha
```

である。従ってGaussian積分の $r_X^\delta,U,R$ 依存は

```math
\prod_\alpha\lambda_\alpha^{-1}
=
\left(
\frac{r_X^\delta}{r_*}
\right)^{\sum_\alpha w_\alpha}
=
\frac{r_X^\delta}{r_*}
```

だけである。free energyとmean forceは $-k_BT\log Z_{\rm res}$ を微分して得る。証明終。
<!-- theorem-end:proof -->

ここで $F_{\rm res}$ はreservoirの条件付きinternal free energyである。lab frameでのbulk flow energyはopen reservoirの資源収支として別に数え、上のinternal partition identityへ混ぜない。

同じreservoirのlocal mean flow $U_e(t)$ には、M64本体の採用開放constitutive lawとして

```math
\tau_U\dot U_e
=
-U_e
+
c_Jr_e
+
R_{U,e}
```

を置く。$U_e$ は別の物理実体ではなくreservoirのcollective flowである。理想極では

```math
U_e
=
\frac{j_e}{\rho_e}
+
O(\varepsilon_U).
```

tracer位置で

```math
U_X(t)
=
\sum_e
\chi_e^U(X_t)U_e(t),
\qquad
\sum_e\chi_e^U(X)=1
```

と補間する。

## Z.5 R203C：moving reservoirからM64 position processへ

M64正本では $T>0$ と低周波摩擦係数 $\gamma_X>0$ を定数とする。density scalingがphase volumeを変えても、採用open modelでは $\gamma_X$ をdensity依存にしない。これによりposition-dependent mobilityに伴う追加noise-induced driftを本体から除外する。

tracerのunderdamped Langevin equationを

```math
dX_t
=
V_t\,dt,
```

```math
M_XdV_t
=
\left[
k_BT\,\partial_X\log r_{X_t}^\delta
-
\gamma_X
\left(
V_t-U_X(X_t,t)
\right)
\right]dt
+
\sqrt{2\gamma_Xk_BT}\,dW_t
```

とする。

<!-- theorem-start:theorem -->
**定理（R203C：M64 moving-reservoir overdamped reduction）**

固定有限時間で $r_X^\delta\ge r_{\min}>0$ とし、$U_X$、$\partial_X\log r_X^\delta$ が有界Lipschitzであるとする。

```math
\nu
=
\frac{k_BT}{\gamma_X},
\qquad
\tau_v
=
\frac{M_X}{\gamma_X}
```

と置く。$\tau_v\to0$ のoverdamped極で、tracer位置過程は

```math
dX_t
=
\left[
U_X(X_t,t)
+
\nu\partial_X\log r_{X_t}^\delta
\right]dt
+
\sqrt{2\nu}\,dW_t
```

へ収束する。

R203A/Bのsafe sectorを合成すると

```math
dX_t
=
\left[
\frac{j}{\rho}
+
\nu\partial_X\log\rho
\right]dt
+
\sqrt{2\nu}\,dW_t
+
R_{64}(X_t,t)\,dt,
```

```math
|R_{64}|
\le
|\varepsilon_U|
+
\nu|\varepsilon_\rho|
+
\varepsilon_{\rm od}.
```

理想極でsignal continuity equation $\partial_t\rho+\partial_xj=0$ が成立するなら、このoverdamped SDEのFokker--Planck方程式は $p(x,t)=\rho(x,t)$ を解として持つ。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203C）**

```math
B(X,t)
=
U_X(X,t)
+
\nu\partial_X\log r_X^\delta
```

と置くと速度方程式は

```math
dV_t
=
-\tau_v^{-1}
[V_t-B(X_t,t)]dt
+
\tau_v^{-1}\sqrt{2\nu}\,dW_t
```

である。variation of constantsを $X_t=X_0+\int_0^tV_sds$ へ代入すると、初期velocity項と指数kernel項は固定有限時間で $\tau_v\to0$ に消え、noise積分は $\sqrt{2\nu}W_t$ へ収束する。よって表示したoverdamped SDEを得る。

そのFokker--Planck方程式へ $p=\rho$、$U=j/\rho$ を代入すると、

```math
-\partial_x
\left[
\left(
\frac{j}{\rho}
+
\nu\partial_x\log\rho
\right)
\rho
\right]
+
\nu\partial_x^2\rho
=
-\partial_xj
```

となり、signal continuity equationと一致する。証明終。
<!-- theorem-end:proof -->

## Z.6 R203D：smooth diffusionとR161 finite-volume chain

R203Cの正則化densityとcurrentを

```math
p_\delta(x,t)>0,
\qquad
J_\delta(x,t),
\qquad
\partial_tp_\delta+\partial_xJ_\delta=0
```

と書く。一様格子 $x_i=ia$ とcell

```math
C_i
=
[x_i-a/2,x_i+a/2]
```

を取り、

```math
\pi_i(t)
=
\int_{C_i}p_\delta(x,t)\,dx,
```

```math
j_{i+1/2}(t)
=
J_\delta(x_i+a/2,t)
```

とする。

R161が許す対称活動量として

```math
t_{i+1/2}
=
\frac{\nu}{a^2}
(\pi_i+\pi_{i+1})
```

を選ぶ。

<!-- theorem-start:theorem -->
**定理（R203D：M64 diffusion--R161 finite-volume connection）**

node-free smooth sectorで、十分小さい格子幅 $a$ に対して

```math
t_{i+1/2}\ge|j_{i+1/2}|
```

が成立するとする。R161 forward ratesを

```math
k^+_{i\to i+1}
=
\frac{
t_{i+1/2}+j_{i+1/2}
}{
2\pi_i
},
```

```math
k^+_{i\to i-1}
=
\frac{
t_{i-1/2}-j_{i-1/2}
}{
2\pi_i
}
```

と取るとrateは非負で、cell continuity equationはR161 master equationと厳密に一致する。

さらにR161 chainの前進・後退平均速度は

```math
D_+X_i
=
v_i^{(a)}
+
u_i^{(a)},
```

```math
D_-X_i
=
v_i^{(a)}
-
u_i^{(a)},
```

```math
v_i^{(a)}
=
\frac{a}{2\pi_i}
(j_{i+1/2}+j_{i-1/2}),
```

```math
u_i^{(a)}
=
\frac{\nu}{2a\pi_i}
(\pi_{i+1}-\pi_{i-1})
```

を厳密に満たす。

$p_\delta,J_\delta$ が十分滑らかなら

```math
v_i^{(a)}
=
\frac{J_\delta}{p_\delta}(x_i,t)
+
O(a^2),
```

```math
u_i^{(a)}
=
\nu\partial_x\log p_\delta(x_i,t)
+
O(a^2),
```

かつsmooth test function $f$ に対して

```math
L_af
=
L_{64}f
+
O(a^2)
```

である。従って $a\to0$、その後 $\delta\to0$ のsafe sectorで

```math
D_\pm X
=
\frac{j}{\rho}
\pm
\nu\partial_x\log\rho
+
O(a^2+\delta)
```

となり、その後のBayes後退率と時間対称Newton則はR161/R185を再利用できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203D）**

continuity equationを各cellへ積分すると

```math
\dot\pi_i
=
j_{i-1/2}
-
j_{i+1/2}
```

を得る。上のR161 rateは

```math
\pi_i k^+_{i\to i+1}
-
\pi_{i+1}k^+_{i+1\to i}
=
j_{i+1/2}
```

を厳密に満たすため、周辺master equationはcell continuityと一致する。

$D_+X_i$ へnearest-neighbor ratesを代入すると表示した $v^{(a)}+u^{(a)}$ が得られる。Bayes backward rateを用いる同じ計算で $D_-X_i=v^{(a)}-u^{(a)}$ となる。cell averageとedge currentを中心Taylor展開すれば $v^{(a)}$ と $u^{(a)}$ の誤差はともに $O(a^2)$ である。同様にjump generatorをTaylor展開すると一次momentは $v^{(a)}+u^{(a)}$、二次momentは $2\nu+O(a^2)$ となり、$L_a=L_{64}+O(a^2)$ を得る。証明終。
<!-- theorem-end:proof -->

M64では、連続軌道をcell labelへ単純に丸めた過程が厳密Markovであるとは主張しない。R203DはM64 smooth diffusionとR161 chainを、同じcontinuum generatorへ収束する連続・離散実現として接続する。

## Z.7 誤差責務と検証境界

M64の代表的な総誤差を

```math
\varepsilon_{64}
\le
C_{64}
\left(
\varepsilon_{\rm env}
+
\varepsilon_{\rm ch}
+
\varepsilon_{\rm width}
+
\delta
+
\varepsilon_U
+
\varepsilon_{\rm bath}
+
\varepsilon_{\rm od}
+
\varepsilon_{\rm fv}
\right)
```

と整理する。同じ上流偏差を複数段へ重複加算しない。

M60のDuffing shell/core mixing、ballistic lead、moving-reflector tracking、periodic homogenization、Eyring--Kramers hoppingに固有の誤差はM64へ引き継がない。M64ではcurrent mean-flow constitutive law自体の具体的Hamiltonian liftをrequired解析誤差とせず、direct open-model simulationまたは独立strengtheningで検査する。

解析核としてR203Aのcurrent identity、R203Bのpartition identity、R203Cのoverdamped reduction、R203Dのfinite-volume generator connectionを固定する。A2ではM37 signal equation、$U_e$ relaxation law、tracer Langevin SDEを同一parameter setで直接積分・標本化し、$U-j/\rho$、osmotic mean force、tracer drift/diffusion、位置密度、R161 generatorへの収束を検査する。

## Z.8 現行主線との責務境界

M64/R203A--R203Dは、M60/M61/M63を整理して置換することを狙うactive replacement candidateである。ただし本付録を追加する段階では、

- M61/R200--M60/R198/R199/R196を現行Q3固定達成主線として維持する。
- M63/R202をactive single-field strengthening candidateとして維持する。
- Q3-1/Q3-2の固定達成ラベルを変更しない。
- Q3-1-A1/Q3-2-A1の部分達成、Q3-1-A2/Q3-2-A2の未監査を変更しない。
- M61/M60 required verifierとM63 candidate verifierを削除・降格しない。

M64昇格と旧Q3主線の退役は、M64のdirect simulation、同一parameter set、文書・検算の整合性を別PRで監査した後に行う。
