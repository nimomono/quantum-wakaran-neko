# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理で統合できるかを調べる現役研究候補である。現段階では論文正本へ昇格させず、`notes/` 内でR194A--R194E、R194H、R194Iを検討する。

現行Q3-2の達成根拠はM54空間状態構成、R161、R162、R185のままとし、R162を退役しない。M37とR191の責務も変更しない。本メモの更新は固定目標、達成判定、`sections/`、`paper.md`、`main.tex`、`paper.pdf` を変更しない。

M56の主線は、signal spin-waveから `rho,S` を得た後、位相と振幅を別々の物理チャネルへ渡す構成とする。

```text
spin signal
  |-- phase S --> weak pickup --> active LLGS regenerator --> wall current drift
  `-- density rho --> two-action entropy shell -----------> wall osmotic drift

thermal wall bath ----------------------------------------> Brownian noise / mobility
```

phase側は、signalとeasy-plane busを直接強結合してsignal amplitudeをcurrentのenergy sourceにするのではなく、weak pickup、外部driveを持つactive feed-forward、floating global phase servoを介して固定振幅spin currentへ変換する。relative-velocity magnon-drag、Doppler entrainment、`u_fast = j/rho` はM56主線へ戻さない。

## 2. 最小構成

基本実体は固定長古典spin、spin texture、熱浴、active feed-forwardを維持する外部driveである。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S` |
| phase regenerator | weak pickup + active easy-plane LLGS系 + floating global phase | signal phase gradientを固定振幅spin currentへ再生 |
| particle | biaxial easy-axis domain wall | 実在位置 `X`、必要なら内部角 `Phi` |
| entropy shell | 2 Brownian spinの非負作用 | `rho` に比例する状態数からosmotic forceを作る |
| thermal wall bath | stochastic LLGまたは同等の明示bath | mobility、Brownian noise、FDT |

R191の単磁区pointer spinをQ3粒子へ流用しない。Q3粒子はdomain-wall collective coordinateである。

## 3. R194A：spin signalの正準化と有限時間Schrödinger縮約

north-pole patchで固定spin長 `Sigma` に対し

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

と置く。この表示はspin長制約と

```math
\{Q_i,P_j\}=\delta_{ij}
```

を厳密に実現する。

```math
\psi_i
=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

とし、`U(1)` 対称な強磁性交換と局所縦磁場からなるsignal Hamiltonianを選ぶと

```math
i\mathcal J_0\dot\psi
=h_L\psi+N(\psi),
\qquad
h_L=\frac{\mathcal J_0^2}{2m}L_g+V
```

と書ける。総signal作用

```math
\mathcal A
=\mathcal J_0\|\psi\|_2^2
```

はglobal `U(1)` 対称性から厳密保存される。小振幅量

```math
\varepsilon_{\rm amp}
=\frac{\mathcal A}{\Sigma}
```

も保存され、固定時間窓 `0 <= t <= T` で線形Schrödinger解 `psi_L` に対し

```math
\sup_{0\le t\le T}
\frac{\|\psi(t)-\psi_L(t)\|_2}
{\|\psi(0)\|_2}
\le
C_{\rm sig}(T)\,\varepsilon_{\rm amp}
```

というDuhamel型評価を候補定理とする。

physical spin currentはSchrödinger currentへ収束し、1次元smooth long-wave、node-free領域では

```math
j_{\rm spin}
=\rho\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2).
```

R194Aの詳細計算は `m56_phase_bus_completion_derivations.md` に分離する。

## 4. R194B：domain-wall粒子とBrownian縮約

biaxial domain wallを

```math
\mathbf m(x,t)\simeq\mathbf m_{\rm DW}(x-X(t),\Phi(t))
```

とし、低角度作用を

```math
L_{\rm DW}
=
G\Phi\dot X
-
\frac{\kappa_\Phi}{2}\Phi^2
-
V_{\rm pin}(X)
```

とする。短時間のbare inertial massは

```math
M_{\rm DW}=\frac{G^2}{\kappa_\Phi}
```

である。一方、Q3-2で必要なのは長時間Smoluchowski極なので、`m = M_DW` は中心matchingから外し、追加のphysical consistency strengtheningとして扱う。

thermal wall bathの長時間縮約は

```math
dX_t
=
\mu_XF_X\,dt
+
\sqrt{2\nu}\,dW_t,
\qquad
\nu=\mu_Xk_BT
```

を狙う。内部角 `Phi`、finite wall width、memoryの有限誤差をR194Iのremainderへ渡す。

## 5. R194C：2-action entropy shellと初期位置準備

2個のBrownian spinの非負作用 `K_1,K_2` と

```math
A(X,t)=A_*\rho(X,t)
```

に対して

```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}{2}[K_1+K_2-A(X,t)]^2
```

を置く。strict shellでは

```math
\int_0^\infty dK_1
\int_0^\infty dK_2\,
\delta(A-K_1-K_2)
=A,
```

したがって `Omega_2(A) propto A` であり、条件付き自由エネルギーから

```math
F_{\rm osm}
=k_BT\,\partial_X\log\rho
```

を得る。mobility `mu_X` を用いれば

```math
w_{\rm osm}
=\mu_XF_{\rm osm}
=\nu\partial_X\log\rho.
```

finite shell stiffnessも静的には閉形式で評価できる。`c=kappa_sh/(2k_BT)` とすると

```math
Z_{\rm sh}(A)
=\frac{e^{-cA^2}}{2c}
+A\frac{\sqrt\pi}{2\sqrt c}
\left[1+\operatorname{erf}(\sqrt cA)\right].
```

そのlog微分は

```math
\partial_A\log Z_{\rm sh}(A)
=\frac{1}{A+\delta_A},
```

```math
\delta_A
=\frac{e^{-cA^2}}
{\sqrt{\pi c}\,[1+\operatorname{erf}(\sqrt cA)]}.
```

従って `A sqrt(c) >> 1` ではstrict-shell forceへの相対誤差は指数的に小さい。未解決として残すのはfinite mixing time、time-dependent `rho` へのadiabatic tracking、signalへのbackreactionである。

signalを準備時に固定すればwall平衡分布は

```math
p_0(X)\propto Z_{\rm sh}(A_*\rho_0(X))
```

となり、strict-shell極では `p_0 propto rho_0`、finite stiffnessでも制御誤差付きで同じ初期位置準備を狙える。

## 6. R194D'：active gradient regeneratorからmoving wallへの有限誤差bridge

旧R194Dでは、複素場 `B` のphenomenological open equationから固定振幅phase busを仮定し、

```math
J_b=-A_b\partial_x\phi,
\qquad
\dot X=c_{\rm ph}J_b+r_{\rm ph}
```

と置いていた。この模型は導出目標の整理には有用だったが、wallが実際に吸収するのは局所currentそのものではなくwall前後のcurrent jumpであり、両側で同じ `C^1` phase lockを課すとそのjumpが消える。従って旧 `B` 方程式は正式bridgeの主模型から降ろし、以下の明示的なactive spintronic chainへ置き換える。

```text
R194A signal spin
  -> weak phase pickup
  -> externally powered active feed-forward
  -> easy-plane LLGS gradient regenerator
  -> local spin current / finite healing layer
  -> easy-axis moving domain wall
```

regenerator phaseを `phi`、signal phaseを

```math
\theta=\frac{S}{\mathcal J_0}
```

とする。空間一様のfloating phase `chi(t)` を持たせ、

```math
\delta=\phi-\theta-\chi
```

を局所Adler lockする。`chi` は空間一様なのでspin current

```math
J_r=-\mathcal A_r\partial_x\phi
```

を変えず、wall内部角 `Phi` とのcoherent lockingだけを調整できる。

R194D'は次の4補題へ分解する。

- **R194D-a weak pickup / active feed-forward**：signal loadingを小さくしつつ、外部driveから有限locking torqueを供給する。
- **R194D-b floating-phase Adler locking**：`delta` に有限gapを持たせ、finite healing time `tau_h` とfinite healing length `ell_h` を得る。
- **R194D-c moving Brownian wall healing**：wallによる局所current破壊へregeneratorが追随し、wall前後のcurrent jumpをfar-field currentへ有限誤差で結びつける。
- **R194D-d collective coordinate / global phase servo**：easy-plane/easy-axis coupled LLGからwall current jumpを並進SDEへ写し、`chi(t)` で内部角のlocking条件を吸収する。

healing layer gainを `G_h` と書き、一般形を

```math
J_\Phi
=G_hJ_\infty+r_h,
\qquad
J_\infty
=-\frac{\mathcal A_r}{\mathcal J_0}\partial_xS+r_\infty
```

とする。対称な線形reaction-diffusion近似では `G_h=2+O(epsilon)` が候補だが、factor 2を普遍値として仮定しない。matchingは

```math
\frac{\sigma_{\rm DW}G_h\mathcal A_r}
{\Gamma_{\rm DW}\mathcal J_0}
=\frac1m
```

とする。

R194D'の目標は、node-free、subcriticalな停止時刻以前に

```math
dX_t
=\left[
\frac{\partial_xS(X_t,t)}{m}
+r_{194D'}(t)
\right]dt
+\sqrt{2\nu}\,dW_t
```

かつ

```math
\mathbb E\int_0^{T\wedge\tau_U}
|r_{194D'}(t)|^2dt
\le C_T\varepsilon^2
```

を同一parameter familyで示すことである。

候補scalingの一例は

```math
C_\varepsilon\sim\varepsilon^{-3},
\qquad
\Sigma_\varepsilon\sim\varepsilon^{-8},
\qquad
g_{p,\varepsilon}\sim\varepsilon,
```

```math
D_\varepsilon\sim\varepsilon^{-2},
\qquad
K_\varepsilon\sim\varepsilon^{-4},
```

```math
\ell_{h,\varepsilon}\sim\varepsilon,
\qquad
\tau_{h,\varepsilon}\sim\varepsilon^4,
\qquad
\lambda_\varepsilon\sim\varepsilon^2,
```

```math
K_{\chi,\varepsilon}\sim\varepsilon^{-4}.
```

Brownian wall追随では、瞬間速度ではなくhealing時間中のBrownian displacementを評価する必要があり、

```math
\frac{\sqrt{\nu\tau_h}}{\ell_h}
=\sqrt{\frac{\nu}{D_\varepsilon}}
```

が小さいことを要求する。従ってstrong lockingだけでは不十分で、`D_epsilon/nu -> infinity` が必要になる。

このscalingはmacroscopic carrier resourceを使う。従って「backreactionをゼロにしながら無料で有限currentを得る」とは主張せず、有限誤差装置族として扱う。詳細定理文と未証明点は `m56_phase_bus_completion_derivations.md` に置く。

## 7. R194H：temperature-independent diffusion plateau（強化候補）

R194HはQ3-2やR194Iの必須依存ではない。wall diffusion係数

```math
\nu(T)=\frac{k_BT}{\Gamma_X(T)}
```

について、thermal fast modesがwallへquadratic forceを与えるclassical harmonic windowを考える。force fluctuationが `O(k_BT)`、force correlationが `O((k_BT)^2)` ならGreen--Kuboの `beta=1/(k_BT)` により

```math
\Gamma_X(T)
=\Gamma_0+k_BT\,\mathcal G+\cdots
```

を得る候補がある。従って

```math
\nu(T)
=\frac{k_BT}
{\Gamma_0+k_BT\,\mathcal G+\cdots}.
```

温度窓

```math
k_BT\,\mathcal G\gg\Gamma_0
```

では

```math
\nu(T)
=\frac1{\mathcal G}
\left[
1+O\left(\frac{\Gamma_0}{k_BT\mathcal G}\right)
\right]
```

となり、有限温度範囲でtemperature-independent plateauを狙える。全温度で厳密一定とは主張しない。

同じ温度窓でcurrent-transfer coefficientが大きく崩れないことも別条件として管理する。

## 8. R194I：M56 collective-coordinate diffusion theorem候補

R194IはR194A--R194D'の物理部品を合成する結果候補である。node-free有限時間領域、R194D'、fast shell、長時間wall Brownian縮約、small backreaction、smooth signalを仮定し、

```math
dX_t
=\left[
\frac{\partial_xS}{m}
+\nu\partial_x\log\rho
\right](X_t,t)\,dt
+\sqrt{2\nu}\,dW_t
+dR_I(t)
```

を目標とする。

current branchのremainderは独立な `R_lock + R_absorb + R_back` とせず、

```math
R_{\rm current}=R_{194D'}
```

へまとめる。その内部台帳として

```text
pickup/readout,
signal loading,
Adler locking,
healing-layer gain,
Brownian wall tracking,
finite wall width,
wall leakage,
global-phase servo
```

を管理する。全体では

```math
R_I
=R_{\rm sig}
+R_{194D'}
+R_{\rm shell}
+R_{\rm mix}
+R_{\rm wall}
+R_{\rm mem}.
```

physical signalのexact continuityが使える場合はideal limitでFokker--Planck equivarianceを直接示す。Schrödinger型 `rho,S` との比較にはR194Aの `epsilon_amp` とlong-wave誤差を用いる。

R194Iの成立にはR194Hのtemperature plateauを必要としない。固定温度で

```math
\nu=\mu_Xk_BT
```

をsignal dispersionへmatchingできればよい。

## 9. R194E：同じpath lawからNelson Newton則

R194EはR194Iの後段に限定する。ideal R194Iで

```math
b_+
=v+w,
\qquad
v=\frac{\partial_xS}{m},
\qquad
w=\nu\partial_x\log\rho
```

とし、同じforward path lawの時間反転から

```math
b_-
=b_+-2\nu\partial_x\log\rho
=v-w
```

を得る。

```math
D_+X=v+w,
\qquad
D_-X=v-w.
```

Nelson対称加速度は

```math
a_N
=\partial_tv
+v\partial_xv
-w\partial_xw
-\nu\partial_x^2w.
```

signalがSchrödinger型方程式を満たし

```math
\mathcal J_0=2m\nu
```

ならMadelung恒等式から

```math
m a_N=-\partial_xV.
```

物理的なwall diffusionの構成はR194I、同じpath lawからの時間反転とNelson代数はR194E、と責務を分離する。

## 10. matching・誤差・昇格条件

中心matchingは

```math
\mathcal J_0=2m\nu,
\qquad
\nu=\mu_Xk_BT,
```

```math
\frac{\sigma_{\rm DW}G_h\mathcal A_r}
{\Gamma_{\rm DW}\mathcal J_0}
=\frac1m.
```

`m=M_DW` は必須ではなく、追加のconsistency strengtheningとする。

R194D'の時間・空間分離は

```text
tau_h << tau_signal,
lambda << ell_h << L_signal,
nu / D_reg << 1
```

を基本とする。誤差台帳は

```text
epsilon_sig,
epsilon_pickup,
epsilon_load,
epsilon_lock,
epsilon_heal,
epsilon_B,
epsilon_wall,
epsilon_servo,
epsilon_shell,
epsilon_mix,
epsilon_mem
```

を分離する。

| 候補ID | 内容 | 現在の導出状態 |
|---|---|---|
| R194A | exact spin Darboux chart、有限時間Schrödinger縮約、spin current | signal-only候補は明示計算済み、M56全体への埋込みは未完 |
| R194B | domain-wall粒子・Brownian縮約 | 既知collective-coordinate理論依存、finite-error縮約は未完 |
| R194C | 2-action shellからosmotic driftと初期位置準備 | strict state countとfinite-static stiffnessは明示計算済み、finite mixingは未完 |
| R194D' | active gradient regeneratorからmoving wallへのcurrent drift | 4補題＋合成定理と単一parameter familyを定式化、各finite-error証明は未完 |
| R194E | 同一path lawからNelson Newton則 | R194I成立後の代数は厳密 |
| R194H | wall diffusionのtemperature plateau | 強化候補、quadratic-bath Kubo縮約が未完 |
| R194I | M56 collective-coordinate diffusion theorem | R194D'をcurrent branchへ一本化した合成候補、shell/wallを含む統合証明は未完 |

R194F/Gはrelative-velocity検討で一時使用した履歴と衝突しないよう、現役候補番号として再利用しない。

M56が正本へ昇格する最低条件は、R194A/Cに加えてR194D-a--dを同一parameter familyで有限誤差証明し、R194Iでshell mixing、wall Brownian縮約、signal backreactionを統合し、固定温度で `J0=2m nu` を満たす非空なparameter regimeを示すことである。

R194Hのtemperature plateau、`m=M_DW`、完全受動phase bus、有限浴持上げは強化結果とする。R194D'を本メモへ定式化したこと自体は、M56の正本昇格や現行Q3-2達成根拠の変更を意味しない。
