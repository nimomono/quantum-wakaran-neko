# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理で統合できるかを調べる現役研究候補である。橋渡し結果候補をR194A--R194Eと呼ぶ。

現時点ではQ3-2の達成根拠を変更しない。現行主線はM54空間状態構成、R161、R162、R185であり、R162を退役しない。M37とR191の責務も変更しない。

M56が主線へ昇格する最低条件は、R194Dのphase-current bridgeを明示的なcoupled stochastic LLG模型から有限誤差付きで閉じ、R194B--R194Dの条件を同時に満たす非空なparameter regimeを示すことである。

## 2. 最小構成

基本実体は固定長古典spin、spin texture、熱浴である。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S` |
| phase bus | easy-plane spin系 | 位相勾配をspin supercurrentへ変換 |
| particle | biaxial easy-axis domain wall | 実在位置 `X`、内部角 `Phi` |
| entropy/bath | 2 Brownian spin＋stochastic LLG bath | osmotic driftとBrownian noise |

R191の単磁区pointer spinをQ3粒子へ流用しない。Q3粒子はdomain-wall collective coordinateである。

## 3. R194A--R194C

R194Aでは、古典spinのPoisson括弧
```math
\{S_i^a,S_j^b\}=\delta_{ij}\epsilon^{abc}S_i^c
```
を `z` 偏極近傍で線形化し、
```math
Q_i=\frac{S_i^x}{\sqrt S},
\qquad
P_i=\frac{S_i^y}{\sqrt S},
\qquad
\{Q_i,P_j\}=\delta_{ij}+O(\varepsilon_{\rm amp})
```
を得る。これは局所正準signalの候補だが、M37/R86を置換する有限時間spin縮約は未証明である。

R194Bではbiaxial domain wallを
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
から
```math
P=G\Phi,
\qquad
M_{\rm DW}=\frac{G^2}{\kappa_\Phi}
```
を得る。stochastic LLG bathとFDTから長時間に
```math
dX_t
=
\mu_XF_X\,dt
+
\sqrt{2\nu}\,dW_t,
\qquad
\nu=\mu_Xk_BT
```
というSmoluchowski極限を狙う。有限誤差Markov縮約は未証明である。

R194Cでは2個のBrownian spinの非負作用 `K_1,K_2` と
```math
A(X,t)=A_*\rho(X,t)
```
に対して
```math
H_{\rm sh}
=
\frac{\kappa}{2}[K_1+K_2-A(X,t)]^2
```
を置く。厳密2作用殻では
```math
\int_0^\infty dK_1
\int_0^\infty dK_2\,
\delta(A-K_1-K_2)
=
A,
```
したがって `Omega_2(A)` は `A` に比例する。

条件付き自由エネルギーから
```math
F_{\rm osm}
=
k_BT\,\partial_X\log\rho
```
が出る。osmotic velocityを `w_osm` と書けば
```math
w_{\rm osm}
=
\mu_XF_{\rm osm}
=
\nu\partial_X\log\rho.
```

Q3-2と同じnode-free領域 `rho >= rho_* > 0` では、R161/R162の正率化に用いた `delta` を導入せずこのdriftを直接狙う。2作用殻状態数は厳密だが、有限shell stiffnessと有限mixingの誤差は未評価である。

## 4. R194D：phase busからcurrent drift

Nelsonのcurrent velocityは
```math
v=\frac{\partial_xS}{m}.
```

easy-plane phase busをsignalへlockし、
```math
\phi
=
\frac{S}{\mathcal J_0}
+
O(\varepsilon_{\rm lock})
```
を狙う。spin supercurrent
```math
J_s=-A_b\partial_x\phi
```
の割合 `eta` をwallが吸収して
```math
\dot X_{\rm phase}
=
\frac{\eta J_s}{2s_w(1+\alpha_w^2)}
+
r_{\rm absorb}
```
と縮約できるなら、
```math
\frac{\eta A_b}
{2s_w(1+\alpha_w^2)\mathcal J_0}
=
\frac1m
```
というmatchingで
```math
\dot X_{\rm phase}
=
\frac{\partial_xS}{m}
+
O(\varepsilon_{\rm lock}+\varepsilon_{\rm absorb})
```
を得る。

thermal magnonの `beta` 型torqueは主経路に使わず、spin supercurrentの角運動量吸収を使う。R194Dが最大のneckであり、phase lock、吸収効率、同一ミクロ模型からの係数評価、backreactionが未証明である。

## 5. R194E：Nelson合成

R194C/Dの理想条件で
```math
v=\frac{\partial_xS}{m},
\qquad
w_{\rm osm}=\nu\partial_x\log\rho
```
とし、
```math
dX_t
=
(v+w_{\rm osm})(X_t,t)\,dt
+
\sqrt{2\nu}\,dW_t
```
とする。

Fokker--Planck方程式へ `p=rho` を代入すると
```math
w_{\rm osm}\rho
=
\nu\partial_x\rho
```
によりosmotic項と拡散項が相殺し、
```math
\partial_t\rho
=
-\partial_x(\rho v)
```
が残る。従ってSchrödinger型signalと同じ初期分布なら位置分布 `rho` が保存される。

同じforward path lawの時間反転から
```math
b_-
=
b_+
-
2\nu\partial_x\log\rho
=
v-w_{\rm osm},
```
従って
```math
D_+X=v+w_{\rm osm},
\qquad
D_-X=v-w_{\rm osm}.
```

Nelson加速度は
```math
a_N
=
\partial_tv
+
v\partial_xv
-
w_{\rm osm}\partial_xw_{\rm osm}
-
\nu\partial_x^2w_{\rm osm}.
```

signalがSchrödinger型方程式を満たし、
```math
\mathcal J_0=2m\nu
```
ならMadelung恒等式から
```math
m a_N=-\partial_xV.
```

R194C/Dを仮定した後のFokker--Planck整合、同経路時間反転、Nelson加速度代数は厳密だが、M56全体から仮定を導く部分は未解決である。

## 6. matching・誤差・昇格条件

中心matchingは
```math
\mathcal J_0=2m\nu,
\qquad
\nu=\mu_Xk_BT,
\qquad
m=M_{\rm DW},
```
```math
\eta A_b
=
4s_w(1+\alpha_w^2)\nu.
```

候補時間尺度は `tau_bath, tau_shell, tau_lock << tau_particle, tau_signal` とする。finite wall widthは滑らかなsignalに対して `O(lambda^2)` 補正として扱う。

誤差台帳は `epsilon_sig, epsilon_lock, epsilon_absorb, epsilon_shell, epsilon_wall, epsilon_od, epsilon_mem, epsilon_back` を分離し、将来forward driftと時間対称Newton則へ有限誤差を持ち上げる。

| 候補ID | 内容 | 現在の導出状態 |
|---|---|---|
| R194A | spin場から局所正準signal | 近似結果／実装候補 |
| R194B | domain-wall粒子・Brownian縮約 | 既知理論依存の近似結果 |
| R194C | 2-spin状態数からosmotic drift | shell状態数は厳密、有限mixingは近似 |
| R194D | phase busからcurrent drift | 予想・未解決 |
| R194E | Brownian diffusionからNelson Newton則 | R194C/D仮定後は厳密 |

R194A--R194Eはこのメモ内の候補番号であり、現行論文の達成根拠へまだ昇格させない。

次の決定的課題は `signal phase -> easy-plane phase lock -> J_s -> dot X` を同じcoupled spin Hamiltonian、Gilbert damping、thermal bathから有限誤差付きで導くことである。

## 7. 既知物理との接点

M56自体の成立を既知研究が証明するわけではないが、部品としてBrown/Kubo--HashitsumeのBrownian spin、Shibata--Takagi型のdomain-wall collective coordinate、Duine--Núñez--MacDonald型のstochastic domain-wall dynamics、Kim--Tserkovnyak型のthermomagnonic torque、Upadhyaya--Kim--Tserkovnyak型のspin-superfluid/domain-wall角運動量移送を参照する。

正式に論文本文へ昇格させる場合はbibliography情報を `references.bib` と `sections/90_references.md` へ同期する。
