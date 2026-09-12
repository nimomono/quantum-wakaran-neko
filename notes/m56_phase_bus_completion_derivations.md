# M56 phase-bus completion 技術メモ

## 1. 目的と状態区分

このメモは `brownian_spin_q1_q3_unification.md` の技術補助である。M56はまだ論文正本へ昇格させず、本メモも `notes/` に留める。

今回保存するのは、relative-velocity magnon-drag路線を復活させずにphase-bus版M56へ追加できる結果だけである。

- R194A：exact Darboux chart、有限時間Schrodinger縮約、spin current。
- R194C：finite shell stiffnessの閉形式、初期位置準備。
- R194D：active fixed-amplitude phase normalizerの最小open model。
- R194H：quadratic thermal bathによるtemperature-independent diffusion plateau候補。
- R194I：current drift、osmotic drift、Brownian noiseの有限誤差合成定理候補。

結果は、**明示計算済み**、**controlled asymptotic候補**、**未証明bridge**を区別する。

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
=
\sum_{\{i,j\}\in E}
\frac{\mathcal J_0g_{ij}}{4m\Sigma}
|\mathbf S_i-\mathbf S_j|^2
+
\sum_i
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
=
\frac{\mathcal J_0^2g_{ij}}{2m}
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

小振幅量が保存されるので、このsignal-only評価には非線形振幅の時間増大を仮定する必要がない。

### 2.4 exact spin current

局所density `rho_i=|psi_i|^2` はexact continuityを満たす。edge currentは

```math
j_{ij}^{\rm spin}
=
\frac{\mathcal J_0}{m}
 g_{ij}A_{ij}
 \operatorname{Im}(\bar\psi_i\psi_j).
```

目標Schrodinger currentとの差は `O(epsilon_amp)`。1次元smooth long-wave limitでは

```math
j^{\rm spin}
=
\frac{\mathcal J_0}{m}
\operatorname{Im}(\bar\phi\partial_x\phi)
+O(\varepsilon_{\rm amp})+O(a^2).
```

Madelung表示 `phi=sqrt(rho) exp(iS/J0)` では

```math
j^{\rm spin}
=
rho\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2).
```

R194Dは `j/rho` を直接読むのではなく、`S/J0` をphase normalizerへ渡す。

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
=
\frac{e^{-cA^2}}{2c}
+
A\frac{\sqrt\pi}{2\sqrt c}
[1+\operatorname{erf}(\sqrt cA)].
```

微分すると

```math
\frac{dZ_{\rm sh}}{dA}
=
\frac{\sqrt\pi}{2\sqrt c}
[1+\operatorname{erf}(\sqrt cA)],
```

従って

```math
\partial_A\log Z_{\rm sh}
=\frac1{A+\delta_A},
```

```math
\delta_A
=
\frac{e^{-cA^2}}
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

## 4. R194D：active fixed-amplitude phase normalizer

phase normalizerを

```math
B=Re^{i\phi}
```

とし、最小open equation候補を

```math
\partial_tB
=
\left[
\Gamma_b\left(1-\frac{|B|^2}{B_0^2}\right)
+i\omega_b
\right]B
+D_b\partial_x^2B
+\kappa_b\psi
+\xi_b.
```

`Gamma_b>0` は固定振幅limit cycleを維持する外部driveと散逸の組を表す。signalはphase referenceとして働く。

`rho>=rho_*>0` のnode-free領域で `delta=phi-S/J0` とすると、振幅が `B_0` 近傍へ縮約した後のphase dynamicsはAdler型

```math
\partial_t\delta
=\Delta
-K\sin\delta
+D_b\partial_x^2\delta
+\xi_\phi
+\cdots
```

となる候補が自然である。locking margin `K_* > |Delta| + spatial forcing + noise margin` の下で

```math
\|\delta\|
+L_{\rm sig}\|\partial_x\delta\|
\le C\varepsilon_{\rm lock}
```

を示すことがR194D-aの課題。

固定振幅carrierのspin current

```math
J_b=-A_b\partial_x\phi
```

がwallへ吸収され

```math
\dot X_{\rm ph}
=c_{\rm ph}J_b+r_{\rm absorb}
```

と縮約できるなら

```math
-c_{\rm ph}A_b=\frac{\mathcal J_0}{m}
```

により

```math
\dot X_{\rm ph}
=\frac{\partial_xS}{m}
+O(\varepsilon_{\rm lock}+\varepsilon_{\rm absorb}).
```

signalへのbackreactionを `R_back` として別管理する。active normalizerではcarrierのエネルギーを外部driveが供給するので、signal amplitudeをcurrent-drift energy sourceとみなさない。

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
\nu(T)
=\frac{k_BT}{\Gamma_X(T)}.
```

`k_BT G >> Gamma_0` で

```math
\nu(T)
=\frac1{\mathcal G}
\left[
1+O\left(\frac{\Gamma_0}{k_BT\mathcal G}\right)
\right].
```

これは有限温度windowのplateau候補であり、全温度での厳密定数性は主張しない。

R194Hはphase normalizerと役割が独立である。phase側はdeterministic current drift、thermal wall bath側はmobility/noiseを担当する。ただし同じ温度窓で

```math
c_{\rm ph}(T)
=c_{\rm ph}^{(0)}[1+O(\varepsilon_{\rm ph,T})]
```

を要求し、current-drift matchingが温度変化で崩れないことを監査する。

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

remainderは

```math
R_I
=R_{\rm sig}
+R_{\rm lock}
+R_{\rm absorb}
+R_{\rm shell}
+R_{\rm mix}
+R_{\rm wall}
+R_{\rm back}
+R_{\rm mem}.
```

各項の意味は次の通り。

- `R_sig`：R194Aのfinite amplitude、long-wave、phase derivative誤差。
- `R_lock`：phase normalizerの有限locking誤差。
- `R_absorb`：bus currentからwall並進へのcollective-coordinate誤差。
- `R_shell`：finite shell stiffnessのstatic誤差。
- `R_mix`：time-dependent shellの有限mixing誤差。
- `R_wall`：内部角、finite wall width、overdamped縮約誤差。
- `R_back`：signalへの有限backreaction。
- `R_mem`：wall bathのnon-Markov memory。

Lipschitz driftの下では同期couplingにより

```math
\mathbb E\sup_{s\le t}|X_s-\bar X_s|
\le
C_T\,\mathcal E_I
```

型のWasserstein-1 boundを狙う。`mathcal E_I` は上の誤差台帳の和とする。

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
-c_{\rm ph}A_b=\frac{\mathcal J_0}{m},
```

```math
\nu=\mu_Xk_BT.
```

`m=M_DW` は必須ではない。short-time inertial massとsignal dispersion massを一致させられること自体は強化結果として別に保持できる。

同様に、temperature-independent `nu`、完全受動phase bus、有限閉鎖Hamiltonian持上げは強化結果であり、M56の最低昇格条件へ入れない。

## 9. 次の決定的課題

1. node-free有限時間でactive phase normalizerの `C^1` locking boundを出す。
2. fixed-amplitude bus currentからwall並進へのcollective-coordinate係数と誤差を明示する。
3. finite shell mixingとtime-dependent `rho` trackingを定量化する。
4. wall Brownian縮約のmemory、内部角、finite widthをR194Iへ統合する。
5. quadratic wall-bath forceについて `Gamma_X(T)=Gamma_0+k_BT G+...` を具体的spin bathから導く。
6. R194AのL2有限時間boundをNelson accelerationへ十分なderivative normへ強化する。

これらが閉じるまではM56を正本のQ3-2達成根拠へ昇格させない。
