# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理で統合できるかを調べる現役研究候補である。現段階では論文正本へ昇格させず、`notes/` 内でR194A--R194E、R194H、R194Iを検討する。

現行Q3-2の達成根拠はM54空間状態構成、R161、R162、R185のままとし、R162を退役しない。M37とR191の責務も変更しない。本メモの更新は固定目標、達成判定、`sections/`、`paper.md`、`main.tex`、`paper.pdf` を変更しない。

M56の主線は、signal spin-waveから `rho,S` を得た後、位相と振幅を別々の物理チャネルへ渡す構成とする。

```text
spin signal
  |-- phase S --> active fixed-amplitude phase normalizer --> wall current drift
  `-- density rho --> two-action entropy shell -----------> wall osmotic drift

thermal wall bath ----------------------------------------> Brownian noise / mobility
```

独立easy-plane phase busは「余計な量子状態sector」ではなく、signal phaseを固定振幅carrierへ写す古典的phase normalizerとして用いる。relative-velocity magnon-drag、Doppler entrainment、`u_fast = j/rho` はM56主線へ戻さない。

## 2. 最小構成

基本実体は固定長古典spin、spin texture、熱浴、必要ならphase normalizerを維持する外部driveである。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S` |
| phase normalizer | 固定振幅を保つeasy-plane / self-oscillating spin系 | signal phaseを有限振幅carrierへ写し、位相勾配をspin supercurrentへ変換 |
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

を厳密に実現する。従って旧版の「小振幅で近似的に正準化する」という記述は不要である。

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

も有限時間で保存され、固定時間窓 `0 <= t <= T` で線形Schrödinger解 `psi_L` に対し

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
=
\frac{e^{-cA^2}}{2c}
+
A\frac{\sqrt\pi}{2\sqrt c}
\left[1+\operatorname{erf}(\sqrt cA)\right].
```

そのlog微分は

```math
\partial_A\log Z_{\rm sh}(A)
=
\frac{1}{A+\delta_A},
```

```math
\delta_A
=
\frac{e^{-cA^2}}
{\sqrt{\pi c}\,[1+\operatorname{erf}(\sqrt cA)]}.
```

従って `A sqrt(c) >> 1` ではstrict-shell forceへの相対誤差は指数的に小さい。未解決として残すのはfinite mixing time、time-dependent `rho` へのadiabatic tracking、signalへのbackreactionである。

signalを準備時に固定すればwall平衡分布は

```math
p_0(X)\propto Z_{\rm sh}(A_*\rho_0(X))
```

となり、strict-shell極では `p_0 propto rho_0`、finite stiffnessでも制御誤差付きで同じ初期位置準備を狙える。

## 6. R194D：active phase normalizerからcurrent drift

Nelsonのcurrent velocityは

```math
v=\frac{\partial_xS}{m}.
```

phase normalizerの局所複素座標を

```math
B(x,t)=R(x,t)e^{i\phi(x,t)}
```

とし、候補open equationとして

```math
\partial_tB
=
\left[
\Gamma_b\left(1-\frac{|B|^2}{B_0^2}\right)
+i\omega_b
\right]B
+D_b\partial_x^2B
+\kappa_b\psi
+\xi_b
```

を置く。`Gamma_b>0` の外部自由エネルギー供給により `R approx B_0` を維持し、signalは主にphase referenceを与える。目的はnode-free有限時間領域で

```math
\phi
=\frac{S}{\mathcal J_0}
+O(\varepsilon_{\rm lock}),
\qquad
\partial_x\phi
=\frac{\partial_xS}{\mathcal J_0}
+O(\varepsilon_{\rm lock}).
```

を得ることだけである。phase busに `rho` の複製や `j/rho` の演算を要求しない。

fixed-amplitude easy-plane carrierのspin supercurrentを

```math
J_b=-A_b\partial_x\phi
```

とし、その一部がdomain wallへ吸収されるcollective-coordinate係数を `c_{\rm ph}` と書く。

```math
\dot X_{\rm ph}
=c_{\rm ph}J_b+r_{\rm ph}.
```

符号規約を含めて

```math
-c_{\rm ph}A_b
=\frac{\mathcal J_0}{m}
```

とmatchingすれば

```math
\dot X_{\rm ph}
=\frac{\partial_xS}{m}
+O(\varepsilon_{\rm lock}
+\varepsilon_{\rm absorb}
+\varepsilon_{\rm back}).
```

phase normalizerは受動Hamiltonian sectorである必要はない。採用open classical modelとして用いる場合は、外部drive、散逸、雑音、定常振幅、signalへの有限backreactionを明示する。完全受動phase busは上位の強化課題とする。

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

同じ温度窓でphase-transfer coefficientが大きく崩れないことも必要なので

```math
c_{\rm ph}(T)
=c_{\rm ph}^{(0)}
[1+O(\varepsilon_{\rm ph,T})]
```

を別条件として管理する。

## 8. R194I：M56 collective-coordinate diffusion theorem候補

R194IはR194A--R194Dの物理部品を合成する結果候補である。node-free有限時間領域、phase lock、fast shell、長時間wall Brownian縮約、small backreaction、smooth signalを仮定し、

```math
dX_t
=
\left[
\frac{\partial_xS}{m}
+\nu\partial_x\log\rho
\right](X_t,t)\,dt
+\sqrt{2\nu}\,dW_t
+dR_I(t)
```

を目標とする。

remainderは機構別に

```math
R_I
=R_{\rm sig}
+R_{\rm lock}
+R_{\rm absorb}
+R_{\rm shell}
+R_{\rm mix}
+R_{\rm wall}
+R_{\rm back}
```

と分離する。必要に応じ `R_mem`、finite wall width、内部角endpoint補正も加える。

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
-c_{\rm ph}A_b
=\frac{\mathcal J_0}{m}.
```

`m=M_DW` は必須ではなく、追加のconsistency strengtheningとする。

時間尺度は

```text
tau_bath, tau_shell, tau_lock << tau_particle, tau_signal
```

を基本とする。誤差台帳は

```text
epsilon_sig,
epsilon_lock,
epsilon_absorb,
epsilon_shell,
epsilon_mix,
epsilon_wall,
epsilon_od,
epsilon_mem,
epsilon_back,
epsilon_ph,T
```

を分離する。

| 候補ID | 内容 | 現在の導出状態 |
|---|---|---|
| R194A | exact spin Darboux chart、有限時間Schrödinger縮約、spin current | signal-only候補は明示計算済み、M56全体への埋込みは未完 |
| R194B | domain-wall粒子・Brownian縮約 | 既知collective-coordinate理論依存、finite-error縮約は未完 |
| R194C | 2-action shellからosmotic driftと初期位置準備 | strict state countとfinite-static stiffnessは明示計算済み、finite mixingは未完 |
| R194D | active phase normalizerからcurrent drift | open-model候補、finite lock/absorption/backreaction boundが未完 |
| R194E | 同一path lawからNelson Newton則 | R194I成立後の代数は厳密 |
| R194H | wall diffusionのtemperature plateau | 強化候補、quadratic-bath Kubo縮約が未完 |
| R194I | M56 collective-coordinate diffusion theorem | 合成候補、各finite-error boundの統合が未完 |

R194F/Gはrelative-velocity検討で一時使用した履歴と衝突しないよう、現役候補番号として再利用しない。

M56が正本へ昇格する最低条件は、R194A/C/D/Iの必要な有限誤差評価を同時に満たす非空なparameter regimeを示し、signalへのbackreactionを制御し、固定温度で `J0=2m nu` を満たすことである。R194Hのtemperature plateau、`m=M_DW`、完全受動phase bus、有限浴持上げは強化結果とする。

詳細計算と未解決条件は `m56_phase_bus_completion_derivations.md` に置く。

## 11. 既知物理との接点

M56自体の成立を既知研究が証明するわけではないが、部品としてBrown/Kubo--HashitsumeのBrownian spin、Shibata--Takagi型のdomain-wall collective coordinate、Duine--Nunez--MacDonald型のstochastic domain-wall dynamics、easy-plane spin superfluid、spin-superfluid/domain-wall角運動量移送、classical injection lockingを参照する。

正式に論文本文へ昇格させる場合に限ってbibliography情報を `references.bib` と `sections/90_references.md` へ同期する。
