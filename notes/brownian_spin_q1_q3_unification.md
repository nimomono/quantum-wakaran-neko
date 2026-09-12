# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理で統合できるかを調べる現役研究候補である。橋渡し結果候補をR194A--R194Hと呼ぶ。

現時点ではQ3-2の達成根拠を変更しない。現行主線はM54空間状態構成、R161、R162、R185であり、R162を退役しない。M37とR191の責務も変更しない。

M56の現行主候補は、独立easy-plane phase busを置かず、signal spin-wave自身の局所流速 `j/rho` をdomain-wall relative-velocity frictionへ渡す経路である。旧R194Dのphase-bus経路は代替案として降格し、結果番号は再利用しない。

M56が主線へ昇格する最低条件は、同一stochastic spin field内でcoherent signalとfast thermal magnonsを有限誤差付きで分離し、signal phaseから局所driftを作るDoppler縮約、有限低周波drag、entropy shell、wall Brownian縮約を同時に満たす非空なparameter regimeを示すことである。

## 2. 最小構成

基本実体は固定長古典spin、spin texture、熱浴である。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S`、局所流速 `v=j/rho` |
| particle | biaxial easy-axis domain wall | 実在位置 `X`、内部角 `Phi` |
| entropy shell | 2 Brownian spinの作用自由度 | `rho` に比例する状態数からosmotic forceを作る |
| thermal spin bath | stochastic LLGのfast spin/magnon sector | relative-velocity friction、Brownian noise、FDT |

R191の単磁区pointer spinをQ3粒子へ流用しない。Q3粒子はdomain-wall collective coordinateである。

## 3. R194A：spin signalと局所流速

古典spinのPoisson括弧
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

長波長の有効signalを
```math
\psi(x,t)=\sqrt{\rho(x,t)}\,e^{iS(x,t)/\mathcal J_0}
```
とし、Schrödinger型kinetic termを持つ場合、局所currentは
```math
j
=\frac{\mathcal J_0}{m}\operatorname{Im}(\psi^*\partial_x\psi)
=\rho\frac{\partial_xS}{m}.
```
したがってnode-free領域 `rho >= rho_* > 0` では
```math
v_s
=\frac{j}{\rho}
=\frac{\partial_xS}{m}.
```
この `v_s` を独立phase busへ複製せず、signal自身のhydrodynamic velocityとして使う。

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
から
```math
P=G\Phi,
\qquad
M_{\rm DW}=\frac{G^2}{\kappa_\Phi}
```
を得る。

一般のstochastic LLG bathとFDTから、十分長い時間で
```math
dX_t
=
\mu_XF_X\,dt
+
\sqrt{2\nu}\,dW_t,
\qquad
\nu=\mu_Xk_BT
```
というSmoluchowski型縮約を狙う。wall collective coordinateとBrownian縮約自体には既知理論があるが、M56の同一signal/bath模型に対する有限誤差Markov縮約は未証明である。

## 5. R194C：2-spin状態数からosmotic drift

2個のBrownian spinの非負作用 `K_1,K_2` と
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
が出る。mobilityを `mu_X` とすれば
```math
w_{\rm osm}
=
\mu_XF_{\rm osm}
=
\nu\partial_X\log\rho,
\qquad
\nu=\mu_Xk_BT.
```

Q3-2と同じnode-free領域では、R161/R162の正率化に用いた `delta` を導入せずこのdriftを直接狙う。2作用殻状態数は厳密だが、有限shell stiffness、有限mixing、signalへのbackreactionは未評価である。

## 6. R194D：旧phase-bus経路の降格

旧候補ではeasy-plane phase busをsignalへlockし、spin supercurrentをdomain wallへ吸収させて
```math
v=\frac{\partial_xS}{m}
```
を作る経路を検討した。

この経路自体を反証したわけではないが、signal自身に
```math
v_s=\frac{j}{\rho}=\frac{\partial_xS}{m}
```
が存在し、R194Fのrelative-velocity couplingで直接利用できる見込みが立ったため、独立phase busはM56の主候補から外す。旧matching、phase lock、吸収効率は主線の昇格条件に含めない。

通常のmagnon-current torqueだけでは `dot X` は一般に `j=rho v` に比例し、`j/rho` を直接読む機構にはならないので、旧経路の代わりに単純なcurrent吸収を採用するわけではない。

## 7. R194F：relative-velocity Kubo bridge

moving wallのcollective-coordinate縮約では、fast magnon momentum `P_m` に対して
```math
H_{\rm wall-mag}\supset-\dot X\,P_m
```
型の結合が現れる。

一方、coherent signal background
```math
\psi=\sqrt\rho\,e^{iS/\mathcal J_0}
```
の周りでfast fluctuationを展開すると、局所phase gradientはDoppler項
```math
H_{\rm signal-fast}\supset+v_sP_m,
\qquad
v_s=\frac{\partial_xS}{m}
```
として入る候補になる。

従ってfast sectorが見る速度依存部分は
```math
-(\dot X-v_s)P_m.
```
Kubo/Mori縮約の一般形は
```math
F_m(t)
=
-\int_0^\infty d\tau\,
\eta(\tau)
[\dot X(t-\tau)-v_s(t-\tau)].
```
ここで重要なのは、同じresponse kernelが `dot X` と `v_s` の差に掛かることである。R194Fではこのrelative-velocity構造を主張候補とし、まだMarkov近似を仮定しない。

未解決なのは、同一stochastic spin field内でcoherent signalとfast thermal sectorを有限誤差付きで分離し、上のDoppler項とKubo kernelを同時に導くことである。

## 8. R194G：finite reflectionとMarkov drag

最も単純な連続easy-axis domain wallはmagnonに対してreflectionlessになる特殊な構造を持ち、低周波Ohmic frictionが消える場合がある。このbare continuum模型では
```math
\Gamma_m
=\lim_{\omega\to0}\operatorname{Re}\eta(\omega)
=0
```
となり、単純な
```math
-\Gamma_m(\dot X-v_s)
```
を主張できない。

したがってM56の主候補では、wall scatteringのreflectionless性を弱く壊す具体的な古典spin Hamiltonianを必要条件とする。候補は高次異方性、格子離散性、dipolar interaction、higher-gradient exchangeなどであり、このメモではまだ一つに固定しない。

採用模型で有限reflection
```math
R(k)>0
```
が生じ、low-frequency responseが
```math
\eta(\omega)=\Gamma_m+O(\omega\tau_{\rm mem}),
\qquad
\Gamma_m>0
```
を持てば、slow limitで
```math
F_m
=
-\Gamma_m(\dot X-v_s)
+O(\Omega_{\rm slow}\tau_{\rm mem}).
```
ここまで閉じて初めてcurrent driftをMarkov Brownian SDEへ組み込む。

## 9. R194H：thermal-magnon FDTと温度plateau

classical high-occupancy magnon領域では、弾性散乱から生じるdragがthermal occupationに線形なら
```math
\Gamma_m(T)=k_BT\,\mathcal G
```
と書ける。`mathcal G` はHamiltonian parameterとscattering dataから決まり、明示的な `T` を含まない。

同じbathにFDTを適用すると
```math
\nu
=\frac{k_BT}{\Gamma_m}
=\frac{1}{\mathcal G}.
```
したがって、古典magnon plateauでは `nu` の明示的なbath-temperature依存が消える。

これは全温度域で `nu` が厳密一定という主張ではない。低温のBose占有、spin秩序の高温崩壊、`A(T),K(T),s(T),R(k,T)` などHamiltonian parameterのthermal renormalizationは残る。正確な主張は、同一thermal magnon bathがnoiseとdragを同時に作る領域でFDT由来の明示的な `k_BT` が相殺される、というものである。

`m=M_DW` も同じ温度窓でほぼ一定なら
```math
\mathcal J_0=2m\nu
```
の明示的なbath-temperature依存も消える候補になる。

## 10. R194E：Nelson合成

R194A/B/C/F/Gの理想条件で
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

R194A/B/C/F/Gを仮定した後のFokker--Planck整合、同経路時間反転、Nelson加速度代数は厳密だが、M56全体から仮定を導く部分は未解決である。

## 11. 誤差台帳と昇格条件

新主線では旧phase-bus用の `epsilon_lock, epsilon_absorb` を使わず、候補誤差を

- `epsilon_sig`：spin signalからSchrödinger型包絡への誤差
- `epsilon_split`：coherent signalとfast thermal sectorの分離誤差
- `epsilon_Doppler`：signal phaseから `v_s P_m` への縮約誤差
- `epsilon_Kubo`：線形応答縮約誤差
- `epsilon_Markov`：memory kernelの局所化誤差
- `epsilon_refl`：採用scattering模型とlow-frequency `Gamma_m` の差
- `epsilon_shell`：有限shell stiffness・mixing誤差
- `epsilon_wall`：finite wall width・collective-coordinate誤差
- `epsilon_od`：overdamped縮約誤差
- `epsilon_back`：signalへのbath/shell backreaction

に分ける。

M56昇格には少なくとも、次を同時に満たす非空parameter regimeが必要である。

1. node-free signalで `v_s=j/rho` が有限誤差付きで定義できる。
2. coherent signalとfast thermal magnonsを同一spin模型内で分離できる。
3. `-(dot X-v_s)P_m` のrelative-velocity couplingを有限誤差付きで導ける。
4. 採用Hamiltonianで `Gamma_m>0` と `tau_mem << T_signal` を示せる。
5. lab-frameの不要drag、pinning、signal dampingを主drag以下へ抑えられる。
6. entropy shell、Brownian FDT、Nelson matching `J0=2m nu` を同時に満たせる。

候補時間尺度は `tau_fast, tau_shell, tau_mem << tau_particle, tau_signal` とする。finite wall widthは滑らかなsignalに対して `O(lambda^2)` 補正として扱う候補である。

## 12. 現在採用しない経路

- 通常のmagnon-current torqueだけで `v=j/rho` を作る経路：一般には `dot X` が `j=rho v` に比例する。
- 独立easy-plane phase busをM56の必須sectorとする経路：signal自身のlocal velocityを直接使うR194Fを優先する。
- thermal magnonの `beta` 型torqueをcurrent driftの主機構にする経路：補助効果としては許すが主bridgeに使わない。
- bare reflectionless continuum wallだけでMarkov dragを得る経路：low-frequency `Gamma_m` が消える場合がある。
- strict 1D quadratic dispersionで4-magnon scatteringだけをfast-sector thermalizationの根拠にする経路：十分なmomentum mixingを自動的には与えない。

## 13. 候補番号の状態

| 候補ID | 内容 | 現在の導出状態 |
|---|---|---|
| R194A | spin signal、局所正準構造、`v=j/rho` | 長波長有効記述／M37からの直接有限時間縮約は未証明 |
| R194B | domain-wall粒子・Brownian縮約 | 既知理論依存の近似結果 |
| R194C | 2-spin状態数からosmotic drift | shell状態数は厳密、有限mixingは近似 |
| R194D | 独立phase busからcurrent drift | 旧代替案へ降格 |
| R194E | Brownian diffusionからNelson Newton則 | 前段仮定後は厳密 |
| R194F | signal phaseからrelative-velocity Kubo kernel | 構造候補、同一spin模型からの有限誤差導出が未完 |
| R194G | finite reflectionからOhmic/Markov drag | 条件付き候補、具体Hamiltonian未固定 |
| R194H | classical thermal-magnon dragでの `nu` 温度plateau | FDT/equipartition構造、材料parameterの温度依存は残る |

R194A--R194Hはこのメモ内の候補番号であり、現行論文の達成根拠へまだ昇格させない。

## 14. 既知物理との接点

M56自体の成立を既知研究が証明するわけではないが、部品としてBrown/Kubo--HashitsumeのBrownian spin、domain-wall collective coordinate、stochastic domain-wall dynamics、domain-wall--magnon friction、spin hydrodynamics、thermomagnonic torqueを参照する。

正式に論文本文へ昇格させる場合は、採用する具体的なscattering Hamiltonianを固定したうえでbibliography情報を `references.bib` と `sections/90_references.md` へ同期する。
