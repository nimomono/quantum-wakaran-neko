# M56 phase-bus completion 技術メモ

## 1. 目的と状態区分

このメモは `brownian_spin_q1_q3_unification.md` の技術補助である。M56はまだ論文正本へ昇格させず、本メモも `notes/` に留める。

今回保存するのは、relative-velocity magnon-drag路線を復活させずにphase-bus版M56へ追加できる結果だけである。

- R194A：exact Darboux chart、有限時間Schrodinger縮約、spin current。
- R194C：finite shell stiffnessの閉形式、初期位置準備。
- R194D'：weak pickup + active LLGS gradient regenerator + moving domain wallの4補題と有限誤差合成定理候補。
- R194H：quadratic thermal bathによるtemperature-independent diffusion plateau候補。
- R194I：current drift、osmotic drift、Brownian noiseの有限誤差合成定理候補。

結果は、**明示計算済み**、**controlled asymptotic候補**、**未証明bridge**を区別する。R194D'を定理形へ書き下したことはM56の正本昇格を意味しない。

## 2. R194A：signal-only classical spin model

有限無向グラフ `G=(V,E)`、固定spin長 `Sigma`、対称非負辺重み `g_ij` を考える。各siteで

```math
|\mathbf S_i|=\Sigma,
\qquad
\{S_i^a,S_j^b\}
=\delta_{ij}\epsilon^{abc}S_i^c.
```

signal-only Hamiltonian候補を

```math
H_{\rm sig}
=\sum_{\{i,j\}\in E}
\frac{\mathcal J_0g_{ij}}{4m\Sigma}
|\mathbf S_i-\mathbf S_j|^2
+\sum_i
\frac{V_i}{\mathcal J_0}
(\Sigma-S_i^z)
```

とする。これは強磁性交換と局所縦磁場からなる `U(1)` 対称模型である。

### 2.1 exact Darboux chart

north-pole patchで

```math
S_i^x
=Q_i\sqrt{\Sigma-\frac{Q_i^2+P_i^2}{4}},
```
```math
S_i^y
=P_i\sqrt{\Sigma-\frac{Q_i^2+P_i^2}{4}},
```
```math
S_i^z
=\Sigma-\frac{Q_i^2+P_i^2}{2}
```

と置くと、spin長制約を厳密に満たし、標準正準構造

```math
\{Q_i,P_j\}=\delta_{ij}
```

からspin Poisson bracketを厳密に再現する。

```math
\psi_i
=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

とすると

```math
\{\psi_i,\bar\psi_j\}
=-\frac{i}{\mathcal J_0}\delta_{ij},
```

```math
\Sigma-S_i^z
=\mathcal J_0|\psi_i|^2.
```

### 2.2 exact Hamiltonian decomposition

```math
\beta=\frac{\mathcal J_0}{\Sigma},
\qquad
\rho_i=|\psi_i|^2,
```

```math
a_i
=\sqrt{1-\frac{\beta\rho_i}{2}},
\qquad
A_{ij}=a_ia_j,
```

```math
x_{ij}=\operatorname{Re}(\bar\psi_i\psi_j)
```

とする。一辺のHamiltonianは

```math
H_{ij}
=\frac{\mathcal J_0^2g_{ij}}{2m}
\left[
\rho_i+\rho_j
-2A_{ij}x_{ij}
-\beta\rho_i\rho_j
\right].
```

従って

```math
H_{\rm sig}
=\psi^\dagger h_L\psi+R_{\rm nl},
```

```math
h_L
=\frac{\mathcal J_0^2}{2m}L_g+V.
```

Hamilton方程式は

```math
i\mathcal J_0\dot\psi
=h_L\psi+N(\psi).
```

### 2.3 action conservationと有限時間bound

総signal作用

```math
\mathcal A
=\sum_i(\Sigma-S_i^z)
=\mathcal J_0\|\psi\|_2^2
```

はglobal `U(1)` 対称性から厳密保存される。

```math
\varepsilon_{\rm amp}
=\frac{\mathcal A}{\Sigma}
=\frac{\mathcal J_0\|\psi\|_2^2}{\Sigma}
```

も厳密保存される。`0<epsilon_amp<=epsilon_0<1` とし、最大重み付き次数を

```math
d_g=\max_i\sum_jg_{ij}
```

とする。非線形項に

```math
\|N(\psi)\|_2
\le
\frac{\mathcal J_0^2}{2m}
 d_g
 C_N(\varepsilon_0)
 \varepsilon_{\rm amp}
 \|\psi\|_2
```

というboundを置けば、同初期値の線形解 `psi_L` に対しDuhamel公式から

```math
\sup_{0\le t\le T}
\frac{\|\psi(t)-\psi_L(t)\|_2}
{\|\psi(0)\|_2}
\le
\frac{\mathcal J_0}{2m}
 C_N(\varepsilon_0)
 \varepsilon_{\rm amp}
 \int_0^T d_g(s)ds.
```

### 2.4 exact spin current

局所density `rho_i=|psi_i|^2` はexact continuityを満たす。edge currentは

```math
j_{ij}^{\rm spin}
=\frac{\mathcal J_0}{m}
 g_{ij}A_{ij}
 \operatorname{Im}(\bar\psi_i\psi_j).
```

目標Schrodinger currentとの差は `O(epsilon_amp)`。1次元smooth long-wave limitでは

```math
j^{\rm spin}
=\frac{\mathcal J_0}{m}
\operatorname{Im}(\bar\phi\partial_x\phi)
+O(\varepsilon_{\rm amp})+O(a^2).
```

Madelung表示 `phi=sqrt(rho) exp(iS/J0)` では

```math
j^{\rm spin}
=\rho\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2).
```

R194D'は `j/rho` を直接演算せず、signal transverse phaseをweak pickupで読む。

## 3. R194C：finite shell stiffness

```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}{2}(K_1+K_2-A)^2,
\qquad
K_1,K_2\ge0
```

とする。`S=K_1+K_2` に変数変換すると、固定 `S` の線分長が `S` なので

```math
Z_{\rm sh}(A)
=\int_0^\infty
S\exp[-c(S-A)^2]dS,
```

```math
c=\frac{\kappa_{\rm sh}}{2k_BT}.
```

積分は

```math
Z_{\rm sh}(A)
=\frac{e^{-cA^2}}{2c}
+A\frac{\sqrt\pi}{2\sqrt c}
[1+\operatorname{erf}(\sqrt cA)].
```

微分すると

```math
\frac{dZ_{\rm sh}}{dA}
=\frac{\sqrt\pi}{2\sqrt c}
[1+\operatorname{erf}(\sqrt cA)],
```

従って

```math
\partial_A\log Z_{\rm sh}
=\frac1{A+\delta_A},
```

```math
\delta_A
=\frac{e^{-cA^2}}
{\sqrt{\pi c}[1+\operatorname{erf}(\sqrt cA)]}.
```

`z=A sqrt(c)` とすると `z>>1` で

```math
\frac{\delta_A}{A}
\lesssim
\frac{e^{-z^2}}{\sqrt\pi z}.
```

よってfinite stiffnessの**静的**誤差は指数的に小さい。time-dependent `rho` では別にshell mixing time `tau_sh` を評価する必要がある。

### 3.1 初期位置準備

準備中にsignalを固定し、wallがshellとの有効自由エネルギーで平衡化するなら

```math
p_{\rm eq}(X)
\propto
Z_{\rm sh}(A_*\rho_0(X)).
```

strict-shell極では `Z_sh propto A propto rho_0` なので

```math
p_0(X)\propto\rho_0(X).
```

finite stiffnessでは上の `delta_A` により初期分布誤差を制御する。

## 4. R194D'：active gradient regenerator--moving-wall finite-error bridge

### 4.0 旧R194Dからの変更

旧R194Dでは

```math
\partial_tB
=\left[
\Gamma_b\left(1-\frac{|B|^2}{B_0^2}\right)
+i\omega_b
\right]B
+D_b\partial_x^2B
+\kappa_b\psi
+\xi_b
```

という抽象open equationを用いていた。これはphase normalizationの役割を整理するphenomenological surrogateとしてのみ残す。

formal bridgeでは、signalとbusの両側 `C^1` lockを直接仮定しない。wallが吸収するspin currentはcurrent jumpであり、wall両側で同じsignal gradientへ完全lockするとjumpが消えるためである。

採用候補は次の物理chainである。

```text
R194A signal spin
  -> weak pickup
  -> active feed-forward / external power
  -> easy-plane LLGS regenerator
  -> finite healing layer
  -> easy-axis moving domain wall
```

### 4.1 共通設定

有限時間区間 `0 <= t <= T` と一次元領域 `U` を固定する。R194A signal phaseを

```math
\theta(x,t)=\frac{S(x,t)}{\mathcal J_0}
```

とする。node-free smooth-signal領域で

```math
R_s(x,t)\ge R_*>0
```

および `theta` の必要な空間・時間微分に有限上界を仮定する。

regenerator spinを単位vector field `n_epsilon(x,t)`、そのeasy-plane phaseを `phi_epsilon(x,t)` とする。空間一様のfloating phaseを `chi_epsilon(t)` とし、

```math
\delta_\varepsilon
=\phi_\varepsilon-\theta-\chi_\varepsilon
```

をlocking variableとする。

easy-axis wallのcollective coordinatesを

```math
X_\varepsilon(t),
\qquad
\Phi_\varepsilon(t)
```

とする。wall thermal translationにはtarget Brownian term `sqrt(2 nu) dW` を残す。

停止時刻を

```math
\tau_\varepsilon
=\inf\left\{
t>0:
X_\varepsilon(t)\notin U
\text{ or node-free/subcritical condition fails}
\right\}
```

とする。

### 4.2 補題 R194D-a：weak pickup / active feed-forward / loading

signal physical carrier amplitudeを `C_epsilon`、spin長を `Sigma_epsilon`、pickup strengthを `g_p,epsilon` とする。pickup phasorを

```math
V_\varepsilon(x,t)
=g_{p,\varepsilon}C_\varepsilon
A_s(x,t)e^{i\theta(x,t)}
+N_\varepsilon(x,t)
```

とする。active feed-forwardは外部DC powerからregeneratorへの有限phase-sensitive torqueを生成する。

候補scalingとして

```math
C_\varepsilon=\varepsilon^{-3},
\qquad
\Sigma_\varepsilon=\varepsilon^{-8},
\qquad
g_{p,\varepsilon}=\varepsilon
```

を取る。

**R194D-aの証明目標。** 適切なactive gain familyと有限noise仮定の下で

```math
K_{{\rm in},\varepsilon}
=K_0+r_{K,\varepsilon}
```

かつ

```math
\|r_{K,\varepsilon}\|_{L^2}
\le C_T\varepsilon
```

を得る。同時にsignal loadingについて

```math
\sup_{0\le t\le T}
\|\psi_\varepsilon(t)-\psi_0(t)\|_{\mathcal H}
\le C_T\varepsilon
```

を示す。

このscalingでは

```math
\frac{C_\varepsilon^2}{\Sigma_\varepsilon}
=\varepsilon^2,
```

```math
g_{p,\varepsilon}^2=\varepsilon^2,
```

```math
g_{p,\varepsilon}C_\varepsilon
=\varepsilon^{-2}.
```

従ってsmall-amplitude errorとdeterministic loadingを小さくしつつ、pickup carrier amplitudeを小さくしないparameter familyに代数的矛盾はない。ただしfinite-temperature input noiseに対する具体的SNR/loading boundは実回路で別途証明する。

### 4.3 補題 R194D-b：floating-phase Adler locking / finite healing

regenerator LLGSのphase-amplitude reduction後、停止時刻以前に

```math
\partial_t\delta_\varepsilon
=D_\varepsilon\partial_x^2\delta_\varepsilon
-K_\varepsilon\sin\delta_\varepsilon
+F_\varepsilon
+\xi_\varepsilon
```

を得ることを証明対象とする。

候補scalingを

```math
D_\varepsilon=D_0\varepsilon^{-2},
\qquad
K_\varepsilon=K_0\varepsilon^{-4}
```

とする。stable Adler branchで十分なlocking marginを仮定する。

定義

```math
\tau_{h,\varepsilon}=K_\varepsilon^{-1},
```

```math
\ell_{h,\varepsilon}
=\sqrt{\frac{D_\varepsilon}{K_\varepsilon}}
```

から

```math
\tau_{h,\varepsilon}=O(\varepsilon^4),
\qquad
\ell_{h,\varepsilon}=O(\varepsilon).
```

**R194D-bの証明目標。** finite-time stochastic stability estimateとして

```math
\mathbb E
\|\delta_\varepsilon\|_{H^1(U)}^2
\le C_T\varepsilon^2
```

を示し、従って

```math
\phi_{\varepsilon,x}
=\frac{S_x}{\mathcal J_0}
+r_{{\rm grad},\varepsilon}
```

および

```math
\mathbb E
\|r_{{\rm grad},\varepsilon}\|_{L^2(U)}^2
\le C_T\varepsilon^2
```

を得る。

`chi_epsilon(t)` は空間一様なので

```math
\partial_x\chi_\varepsilon=0.
```

従ってglobal phase zero modeを残しながらlocal errorだけに有限gapを持たせる。

### 4.4 補題 R194D-c：moving Brownian wall / healing-layer gain

regenerator spin currentを

```math
J_\varepsilon(x,t)
=-\mathcal A_\varepsilon
\phi_{\varepsilon,x}(x,t)
```

とし、wall current jumpを

```math
J_{\Phi,\varepsilon}
=J_\varepsilon(X_\varepsilon^-,t)
-J_\varepsilon(X_\varepsilon^+,t)
```

とする。

wall translationは

```math
dX_\varepsilon
=V_\varepsilon dt
+\sqrt{2\nu}\,dW_t
```

を満たすとする。

候補scalingとして

```math
\lambda_\varepsilon=\lambda_0\varepsilon^2
```

を置き、

```math
\frac{\lambda_\varepsilon}{\ell_{h,\varepsilon}}
=O(\varepsilon)
```

とする。

Brownian wallでは瞬間速度を用いた追随条件を置かない。healing時間中のBrownian displacementから

```math
\varepsilon_B
=\frac{\sqrt{\nu\tau_{h,\varepsilon}}}
{\ell_{h,\varepsilon}}
=\sqrt{\frac{\nu}{D_\varepsilon}}
```

を定義する。上のscalingなら

```math
\varepsilon_B=O(\varepsilon).
```

この恒等式から、strong locking `K_epsilon -> infinity` だけではBrownian追随性は改善せず、`D_epsilon/nu -> infinity` が必要だと分かる。

far-field currentを

```math
J_{\infty,\varepsilon}
=-\frac{\mathcal A_\varepsilon}{\mathcal J_0}S_x
+r_{\infty,\varepsilon}
```

とする。

**R194D-cの証明目標。** wall周辺のstochastic moving-boundary-layer problemから、あるfinite healing gain `G_h,epsilon` に対して

```math
J_{\Phi,\varepsilon}
=G_{h,\varepsilon}
J_{\infty,\varepsilon}(X_\varepsilon,t)
+r_{{\rm heal},\varepsilon}
```

および

```math
\mathbb E\int_0^{T\wedge\tau_\varepsilon}
|r_{{\rm heal},\varepsilon}(t)|^2dt
\le C_T\varepsilon^2
```

を示す。

**factor 2の扱い。** 対称な線形reaction-diffusion modelで、wall直後currentをzeroへ落として両側へ指数healingさせる場合は

```math
G_{h,\varepsilon}=2+O(\varepsilon)
```

となる候補がある。ただし `2` を普遍値としてR194D'の仮定へ入れない。full LLGS/feed-forward sourceを固定した後に `G_h` を導出し、その値をmatchingへ使う。

### 4.5 補題 R194D-d：collective coordinate / floating-phase servo

subcritical easy-plane/easy-axis coupled LLGから

```math
J_{\Phi,\varepsilon}
=J_{c,\varepsilon}
\sin\left(
\phi_\varepsilon(X_\varepsilon,t)
-\Phi_\varepsilon
\right)
+r_{{\rm core},\varepsilon}
```

を得るとする。

wall translationのcollective-coordinate reductionを

```math
\Gamma_{{\rm DW},\varepsilon}
dX_\varepsilon
=\sigma_{\rm DW}
J_{\Phi,\varepsilon}dt
+\Gamma_{{\rm DW},\varepsilon}
\sqrt{2\nu}\,dW_t
+dR_{{\rm cc},\varepsilon}
```

とする。`sigma_DW` はwall polarityの符号である。

wall内部角とregeneratorのcoherent lockingに必要な位相条件は、空間一様の `chi_epsilon(t)` で吸収する。servo rateを

```math
K_{\chi,\varepsilon}
=K_{\chi,0}\varepsilon^{-4}
```

とする。

**R194D-dの証明目標。** stable subcritical branchで

```math
\phi_\varepsilon(X_\varepsilon,t)-\Phi_\varepsilon
=\Delta_*+r_{\Delta,\varepsilon}
```

かつ

```math
\mathbb E\int_0^{T\wedge\tau_\varepsilon}
|r_{\Delta,\varepsilon}|^2dt
\le C_T\varepsilon^2
```

を示す。同時にfinite wall width、internal-angle elimination、wall-profile deformation、memoryのうちR194D'へ含める項について

```math
\mathbb E\int_0^{T\wedge\tau_\varepsilon}
|r_{{\rm cc},\varepsilon}(t)|^2dt
\le C_T\varepsilon^2
```

を狙う。

### 4.6 定理 R194D'：active gradient regenerator--moving-wall finite-error bridge

R194D-a--dが同じparameter familyで成立し、

```math
G_{h,\varepsilon}\to G_h>0,
\qquad
\Gamma_{{\rm DW},\varepsilon}
\to\Gamma_{\rm DW}>0
```

とする。

matching conditionを

```math
\frac{\sigma_{\rm DW}G_h\mathcal A_*}
{\Gamma_{\rm DW}\mathcal J_0}
=\frac1m
```

とする。ここで `A_*` はfar-field regenerator stiffnessの極限である。

このとき停止時刻以前に

```math
dX_\varepsilon(t)
=\left[
\frac{S_x(X_\varepsilon(t),t)}m
+r_{194D',\varepsilon}(t)
\right]dt
+\sqrt{2\nu}\,dW_t
```

を得て、総drift誤差について

```math
\mathbb E\int_0^{T\wedge\tau_\varepsilon}
|r_{194D',\varepsilon}(t)|^2dt
\le C_T\varepsilon^2
```

を示すことをR194D'の正式な証明目標とする。

同時にsignal loadingについて

```math
\sup_{0\le t\le T}
\|\psi_\varepsilon(t)-\psi_0(t)\|_{\mathcal H}
\le C_T\varepsilon
```

を要求する。

regenerator由来の追加wall diffusionは

```math
\nu_{{\rm reg},\varepsilon}=o(1)
```

とし、target `nu` を極限で変えないことも含める。

### 4.7 単一parameter familyと誤差台帳

一例として

| quantity | scaling |
|---|---:|
| signal carrier `C_epsilon` | `epsilon^-3` |
| signal spin length `Sigma_epsilon` | `epsilon^-8` |
| pickup coupling `g_p,epsilon` | `epsilon` |
| regenerator phase diffusivity `D_epsilon` | `epsilon^-2` |
| Adler locking rate `K_epsilon` | `epsilon^-4` |
| healing length `ell_h,epsilon` | `epsilon` |
| healing time `tau_h,epsilon` | `epsilon^4` |
| wall width `lambda_epsilon` | `epsilon^2` |
| global-phase servo rate `K_chi,epsilon` | `epsilon^-4` |

を取る。

このとき候補orderは

| error source | target order |
|---|---:|
| R194A nonlinear carrier | `O(epsilon^2)` |
| deterministic signal loading | `O(epsilon)` 以下 |
| pickup phase/readout | `O(epsilon)` 以下 |
| LLGS phase/amplitude reduction | `O(epsilon)` |
| gradient locking | `O(epsilon)` |
| signal variation across healing layer | `O(epsilon)` |
| deterministic wall displacement during healing | `O(epsilon^3)` |
| Brownian wall displacement / healing length | `O(epsilon)` |
| finite wall width / healing length | `O(epsilon)` |
| floating-phase servo | `O(epsilon)` |
| regenerator extra diffusion | `o(1)` |

を狙える。

これは「全誤差が既に証明済み」という表ではなく、**同時に小さくするparameter familyへ代数的矛盾がないことを固定する設計表**である。

### 4.8 R194D'でまだ証明していないもの

R194D'を証明済みに上げるには少なくとも次の4項が必要である。

1. stochastic LLGSからR194D-bのAdler reaction-diffusion equationへの、このscalingで一様なphase-amplitude reduction。
2. Brownian moving sinkを持つreaction-diffusion equationについてR194D-cのhealing-layer estimateと `G_h` の導出。
3. finite-width coupled easy-plane/easy-axis LLGSからR194D-dのcollective-coordinate error bound。
4. 一つの具体的pickup/amplifier circuitについてR194D-aのloading--noise inequalityを定数付きで示すこと。

従って現在のR194D'は、模型の責務と証明対象を4補題へ切り分けた**未証明合成定理候補**である。

## 5. R194H：temperature-independent diffusion plateau

wall bathのeffective frictionをGreen--Kuboで

```math
\Gamma_X(T)
=\beta\int_0^\infty
\langle\delta F_X(t)\delta F_X(0)\rangle_Tdt
```

と書く。

fast thermal coordinates `y_a` がclassical harmonic regimeにあり、centered wall forceの最低次がquadratic

```math
\delta F_X
=\sum_{ab}C_{ab}
[y_ay_b-\langle y_ay_b\rangle]
```

ならequipartitionから `y=O(sqrt(k_BT))`、従って

```math
\delta F_X=O(k_BT),
```

```math
\langle\delta F_X(t)\delta F_X(0)\rangle
=O((k_BT)^2).
```

相関時間と無次元shapeが温度に弱くしか依存しない窓では

```math
\Gamma_X(T)
=k_BT\,\mathcal G+o(T).
```

温度非依存の追加drag `Gamma_0` を含め

```math
\Gamma_X(T)
=\Gamma_0+k_BT\mathcal G+\cdots
```

とすれば

```math
\nu(T)=\frac{k_BT}{\Gamma_X(T)}.
```

`k_BT G >> Gamma_0` で

```math
\nu(T)
=\frac1{\mathcal G}
\left[
1+O\left(\frac{\Gamma_0}{k_BT\mathcal G}\right)
\right].
```

これは有限温度windowのplateau候補であり、全温度での厳密定数性は主張しない。R194HはR194D'やR194Iの必須条件ではない。

## 6. R194I：collective-coordinate diffusion theorem候補

ideal targetは

```math
d\bar X_t
=\left[
\frac{\partial_xS}{m}
+\nu\partial_x\log\rho
\right](\bar X_t,t)dt
+\sqrt{2\nu}\,dW_t.
```

physical wall中心 `X_t` について

```math
X_t
=X_0
+\int_0^t
\left[
\frac{\partial_xS}{m}
+\nu\partial_x\log\rho
\right](X_s,s)ds
+\sqrt{2\nu}W_t
+R_I(t)
```

を目標とする。

R194D'成立後はcurrent branchを

```math
R_{\rm current}=R_{194D'}
```

へ一本化する。`R194D'` の内部でpickup/readout、loading、locking、healing gain、Brownian wall tracking、finite width、leakage、servoを管理する。

R194I全体のremainderは

```math
R_I
=R_{\rm sig}
+R_{194D'}
+R_{\rm shell}
+R_{\rm mix}
+R_{\rm wall}
+R_{\rm mem}.
```

`R_sig` はR194Aのfinite amplitude、long-wave、phase derivative誤差、`R_shell` はfinite shell stiffness、`R_mix` はtime-dependent shell mixing、`R_wall` と `R_mem` はR194D'の範囲外に残したwall Brownian bathの誤差を表す。

Lipschitz driftの下では同期couplingにより

```math
\mathbb E\sup_{s\le t}|X_s-\bar X_s|
\le
C_T\,\mathcal E_I
```

型のWasserstein-1 boundを狙う。

### 6.1 equivariance

ideal SDEのFokker--Planck方程式に `p=rho` を代入すると

```math
-\partial_x
\left[
\left(v+\nu\partial_x\log\rho\right)\rho
\right]
+\nu\partial_x^2\rho
=-\partial_x(v\rho).
```

従ってsignal continuity

```math
\partial_t\rho+\partial_x(v\rho)=0
```

が成り立つなら `p_0=rho_0` から `p_t=rho_t` が保存される。

R194Aのphysical spin currentを用いる場合はexact spin continuityを先に使い、その後Schrodinger型 `rho,S` への比較誤差を評価する方が論理順序として安全である。

## 7. R194Eとの責務分離

R194Iがphysical forward diffusionを構成し、R194Eはその**同じpath law**のBayes時間反転とNelson対称加速度だけを扱う。

```math
b_+=v+w,
\qquad
w=\nu\partial_x\log\rho,
```

```math
b_-=b_+-2\nu\partial_x\log\rho=v-w.
```

`J0=2mnu` とSchrodinger/Madelung方程式から

```math
m a_N=-\partial_xV
```

を得る。

R194Hのtemperature plateauはこの論理閉路の必須条件ではない。固定温度で `nu=D_sig=J0/(2m)` を満たせばQ3-2相当のNelson matchingには足りる。

## 8. 中心matchingと強化結果

M56正本昇格候補に必要な中心matchingは

```math
\mathcal J_0=2m\nu,
```

```math
\frac{\sigma_{\rm DW}G_h\mathcal A_*}
{\Gamma_{\rm DW}\mathcal J_0}
=\frac1m,
```

```math
\nu=\mu_Xk_BT.
```

`m=M_DW` は必須ではない。short-time inertial massとsignal dispersion massを一致させられること自体は強化結果として別に保持できる。

同様に、temperature-independent `nu`、完全受動phase bus、有限閉鎖Hamiltonian持上げは強化結果であり、M56の最低昇格条件へ入れない。

## 9. 次の決定的課題

1. R194D-a：具体pickup/amplifier circuitでloading--noise boundを定数付き化する。
2. R194D-b：full stochastic LLGSからfloating-phase Adler equationと `H^1` finite-time boundを導く。
3. R194D-c：Brownian moving sinkのhealing-layer estimateを証明し、full source modelから `G_h` を決める。
4. R194D-d：coupled easy-plane/easy-axis LLGSからwall collective-coordinate finite-error boundとglobal servo stabilityを導く。
5. R194C：finite shell mixingとtime-dependent `rho` trackingを定量化する。
6. R194I：R194D'、shell、wall bath memoryを同一parameter familyで合成する。
7. R194A：L2有限時間boundをNelson accelerationへ十分なderivative normへ強化する。
8. R194H：必要ならquadratic wall-bath forceからtemperature plateauを導く。これは強化課題である。

これらが閉じるまではM56を正本のQ3-2達成根拠へ昇格させない。
