# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理でどこまで統合できるかを調べる現役研究候補である。橋渡し結果候補をR194A--R194Hと呼ぶ。

現時点ではQ3-2の達成根拠を変更しない。現行主線はM54空間状態構成、R161、R162、R185であり、R162を退役しない。M37とR191の責務も変更しない。本メモと関連技術メモは `notes/` にとどめ、正本の結果番号、固定目標、達成判定へはまだ反映しない。

今回の検討で、signal自身から
```math
v_s=\frac{j}{\rho}
```
を定義し、coherent background上のfast fluctuationに現れるDoppler速度 `v_D` が小振幅極で `v_s` に一致するところまでは具体化した。一方、Doppler shiftだけからthermal fast sectorが速度 `v_s` で共流することは従わない。従って現行研究線は
```text
spin signal -> v_s=j/rho -> Doppler v_D~v_s
            -> fast-sector entrainment ?
            -> relative-velocity Kubo drag
```
と整理する。

旧R194Dのphase-bus経路は主候補から外したまま保持する。ただしrelative-velocity経路がfast-sector entrainmentで閉じない場合のfallback候補として再検討可能な形で残す。

## 2. 最小構成と未確定の親模型

基本実体は固定長古典spin、spin texture、熱浴である。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S`、局所流速 `v_s=j/rho` |
| particle | domain wall | 実在位置 `X`、必要なら内部角 `Phi` |
| entropy shell | 2 Brownian spinの作用自由度 | `rho` に比例する状態数からosmotic forceを作る |
| thermal spin bath | fast spin/magnon sector | friction、Brownian noise、FDT |

R191の単磁区pointer spinをQ3粒子へ流用しない。Q3粒子はdomain-wall collective coordinateである。

今回の検討では、domain-wall質量とsignal dispersionのmatching確認にbiaxial easy-axis/hard-axis模型を使い、signal Noether currentとDoppler係数の明示計算にはazimuthal `U(1)` 対称模型を使った。hard-axis項は一般に `U(1)` を壊すため、これらを現時点で同一Hamiltonianの結果として扱わない。

最終M56親模型は未固定であり、biaxial routeと `U(1)`-symmetric wall route（easy-cone、高次軸対称異方性などを含む）を比較する。

## 3. R194A：spin signalの有限時間Schrödinger縮約

有限spin graph上の `U(1)` 対称signal模型では、north-pole classical Holstein--Primakoff/Darboux chartにより局所正準対を厳密に取れる。spin長を `Sigma` として
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
=\Sigma-\frac{Q_i^2+P_i^2}{2},
\qquad
\{Q_i,P_j\}=\delta_{ij}.
```

```math
\psi_i=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```
とすると、適切な強磁性交換と局所縦磁場から
```math
i\mathcal J_0\dot\psi
=h_L\psi+N(\psi),
\qquad
h_L=\frac{\mathcal J_0^2}{2m}L_g+V
```
を得る。

小振幅量
```math
\varepsilon_{\rm amp}
=\frac{\mathcal J_0\|\psi\|_2^2}{\Sigma}
```
はglobal `U(1)` 対称性から厳密保存される。従って固定有限時間で目標Schrödinger解 `psi_L` に対し
```math
\sup_{0\le t\le T}
\frac{\|\psi(t)-\psi_L(t)\|_2}{\|\psi(0)\|_2}
\le
C_{\rm sig}(T)\,\varepsilon_{\rm amp}
```
というDuhamel評価を得る。

exact spin currentもSchrödinger currentへ `O(epsilon_amp)` で一致し、1次元長波長・node-free領域では
```math
v_s
=\frac{j}{\rho}
=\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2).
```

ここまでをsignal-only theorem候補とする。domain wall、thermal sector、reflection-breakingを同時に持つ最終M56親Hamiltonianへの埋込みは未完である。完全導出は `m56_signal_wall_bridge_derivations.md` に置く。

## 4. R194B：domain-wall質量とBrownian縮約

低角度wall作用
```math
L_{\rm DW}
=G\Phi\dot X
-\frac{\kappa_\Phi}{2}\Phi^2
-V_{\rm pin}(X)
```
から
```math
M_{\rm DW}=\frac{G^2}{\kappa_\Phi}
```
を得る。

整合性確認用biaxial模型
```math
H
=\frac12\int dx\,
\left[
A|\partial_x\mathbf n|^2
+K_e(1-n_z^2)
+K_hn_y^2
\right]
```
では
```math
\lambda=\sqrt{\frac{A}{K_e}},
\qquad
\kappa=\frac{K_h}{K_e},
```
```math
M_{\rm DW}=\frac{2s^2}{K_h\lambda}.
```

同じ模型の長波長spin-wave dispersionは
```math
\omega(k)=\omega_0+D_{\rm sig}k^2+O(k^4),
```
```math
D_{\rm sig}
=\frac{A(2+\kappa)}{2s\sqrt{1+\kappa}}.
```
`D_sig=J0/(2m_sig)` から
```math
m_{\rm sig}
=\frac{\mathcal J_0s\sqrt{1+\kappa}}{A(2+\kappa)}.
```
従って `m_sig=M_DW` は
```math
\frac{\mathcal J_0}{s\lambda}
=\frac{2(2+\kappa)}{\kappa\sqrt{1+\kappa}}
```
と同値である。右辺は `kappa>0` で `+infinity` から `0` へ単調減少するので、任意の正の `J0/(s lambda)` に対して正のmatching `kappa` が一意に存在する。従ってmass equality自体はno-goではない。

ただしこれはbiaxial route内の整合性確認であり、最終親Hamiltonianの選定を完了したものではない。

## 5. R194C：2-spin状態数からosmotic drift

2個のBrownian spinの非負作用 `K_1,K_2` と
```math
A(X,t)=A_*\rho(X,t)
```
に対し
```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}{2}[K_1+K_2-A(X,t)]^2
```
を置く。厳密2作用殻では
```math
\int_0^\infty dK_1\int_0^\infty dK_2\,
\delta(A-K_1-K_2)=A,
```
従って `Omega_2(A)` は `A` に比例する。

条件付き自由エネルギーから
```math
F_{\rm osm}=k_BT\,\partial_X\log\rho
```
が出る。mobilityを `mu_X` とすれば
```math
w_{\rm osm}
=\nu\partial_X\log\rho,
\qquad
\nu=\mu_Xk_BT.
```

有限shell stiffness、有限mixing time、初期 `p(X)=rho(X)` 準備、signalへのbackreactionは未評価である。

## 6. R194D：旧phase-bus経路

旧候補ではeasy-plane phase busをsignalへlockし、spin supercurrentをdomain wallへ渡して `partial_x S/m` を作る経路を検討した。signal自身から `v_s=j/rho` を構成できるため主候補からは降格したが、fast-sector entrainmentが閉じない場合のfallbackとして保持する。

通常のmagnon-current torqueだけではwall応答は一般にcurrent `j` に比例し、`j/rho` を直接読む機構にはならない。この注意は今回の検証でも維持された。

## 7. R194F：Doppler bridgeとfast-sector entrainment

### 7.1 R194F-a：Doppler coefficient

`U(1)` 対称1次元spin背景
```math
n=n_0,
\qquad
q=\partial_x\phi
```
に対し
```math
\rho=s(1-n_0),
\qquad
j=A(1-n_0^2)q,
```
なので
```math
v_s=\frac{j}{\rho}
=\frac{A}{s}(1+n_0)q.
```

同じ背景上でfast fluctuationを二次展開するとDoppler速度
```math
v_D=\frac{2A}{s}n_0q
```
を得る。従って
```math
\chi=\frac{v_D}{v_s}
=\frac{2n_0}{1+n_0}.
```
`epsilon=1-n_0` とすると
```math
|\chi-1|
=\frac{\varepsilon}{2-\varepsilon}.
```
従って小振幅極で
```math
v_D=v_s+O(\varepsilon_{\rm amp}v_s).
```

moving wall frameではfast magnon momentum `P_m` に `-dot X P_m` が入り、quadratic fast generatorは
```math
H_{\rm fast}^{(2)}
=H_0-(\dot X-v_D)P_m+\cdots
```
まで整理できる。

### 7.2 R194F-b：fast-sector entrainment problem

Doppler項だけからthermal fast sectorの実際のdrift velocityが `v_s` になることは従わない。relative-velocity Brownian化に必要なのはnormal-component drift
```math
u_{\rm fast}=v_s+O(\varepsilon_{\rm ent})
```
ではなく、以下で用いる速度記号
```math
u_{\rm fast}\equiv u_{\rm fast}
```
に対して
```math
u_{\rm fast}=v_s+O(\varepsilon_{\rm ent})
```
が成立すること、あるいは条件付きfast分布
```math
\mu_{\rm fast}(dY)
\propto
\exp[-\beta(H_{\rm fast}-v_sP_m)]\,dY
```
を導くことである。以後、本文ではこのnormal-component driftを `u_fast` と呼ぶ。

これが成立して初めてKubo/Mori縮約から
```math
F_m(t)
=-\int_0^\infty d\tau\,
\eta(\tau)
[\dot X(t-\tau)-v_s(t-\tau)]
+\xi(t)
```
を主張できる。

一般のthermal magnonsではnormal componentがlatticeに対してほぼ静止する可能性があり、その場合は `-Gamma_m dot X` が基本dragになる。既知のmagnon torque/dragも一般にはcurrent `j` に比例し、`j/rho` を自動的に読むわけではない。fast-sector entrainmentは現在のM56で最も重要な未解決点の一つである。

## 8. R194G：finite reflectionとpositive Markov drag

bare continuum easy-axis wallはmagnonに対してreflectionlessとなり、低周波Ohmic dragが消える場合がある。従って採用する最終模型にはreflectionless性を壊す機構が必要である。

R194Gの責務は具体模型で
```math
R(k)\not\equiv0,
\qquad
\Gamma_m>0,
\qquad
\tau_{\rm mem}<\infty,
```
```math
\eta(\omega)
=\Gamma_m+O(\omega\tau_{\rm mem})
```
を示すことに限定する。R194G単独からdragの相手側速度を `v_s` と決めない。その部分はR194F-bのentrainmentに依存する。

候補は高次軸対称異方性、easy-cone構造、格子離散性、dipolar interaction、higher-gradient exchangeなどである。

## 9. R194H：classical-magnon diffusion--dispersion matching候補

fast thermal sectorがharmonic classical field
```math
H_f=\frac12Y^TKY
```
として記述でき、wallへ作用するcentered forceがfast変数の二次形式であるとする。canonical thermal stateで
```math
Y=\sqrt{k_BT}\,Z
```
とrescaleすると
```math
\langle\delta F(t)\delta F(0)\rangle_T
=(k_BT)^2C_0(t).
```
従ってclassical Kubo kernelは
```math
\eta_T(t)=k_BT\,C_0(t).
```

```math
\mathcal G=\int_0^\infty C_0(t)dt
```
が有限かつ正ならMarkov極で
```math
\Gamma_m(T)=k_BT\,\mathcal G,
```
```math
\nu=\frac{k_BT}{\Gamma_m}=\frac1{\mathcal G}.
```
固定Hamiltonian係数のclassical harmonic windowでは、`nu` の明示的なbath-temperature因子は消える。

追加の温度非依存drag `Gamma_0` があれば
```math
\Gamma_{\rm tot}=\Gamma_0+k_BT\mathcal G,
```
```math
\nu(T)=\frac{k_BT}{\Gamma_0+k_BT\mathcal G},
```
なのでplateauには
```math
\Gamma_0\ll k_BT\mathcal G
```
が必要である。

signal dispersion
```math
D_{\rm sig}=\frac{\mathcal J_0}{2m}
```
を使えばNelson matching `J0=2m nu` は
```math
\nu=D_{\rm sig}
```
と同値である。従ってharmonic bath resultと合わせたmatching equationは
```math
\mathcal G D_{\rm sig}=1.
```

温度scalingの構造とmatching equationの同定までは進んだが、特定の単一Hamiltonianでこの数値条件を満たすことは未証明である。

## 10. R194E：Nelson合成

物理入力
```math
v=v_s=\frac{\partial_xS}{m},
```
```math
w_{\rm osm}=\nu\partial_x\log\rho,
```
```math
\nu=D_{\rm sig}=\frac{\mathcal J_0}{2m}
```
を仮定すると、forward SDE
```math
dX_t
=(v+w_{\rm osm})(X_t,t)dt
+\sqrt{2\nu}\,dW_t
```
のFokker--Planck方程式へ `p=rho` を代入したときosmotic項と拡散項が相殺し、Schrödinger continuity equationが残る。

同じforward path lawの時間反転から
```math
b_-=v-w_{\rm osm}
```
を得る。さらにNelson加速度に `J0=2m nu` を入れればMadelung恒等式から
```math
m a_N=-\partial_xV
```
が従う。

この数学的合成は物理入力を仮定した後は閉じている。未解決なのは、その入力を単一M56親模型から同時に導くことである。

## 11. error ledger

| 記号 | 内容 |
|---|---|
| `epsilon_sig` | finite-time spin signal -> Schrödinger縮約誤差 |
| `epsilon_amp` | north-pole小振幅量 |
| `epsilon_split` | coherent signal / fast thermal sector分離誤差 |
| `epsilon_Doppler` | `v_D` と `v_s` のずれ。`U(1)`模型では `<= epsilon_amp/(2-epsilon_amp)` |
| `epsilon_ent` | fast-sector drift `u_fast` と `v_s` のずれ |
| `epsilon_wall` | rigid-wall / low-angle collective-coordinate誤差 |
| `epsilon_Kubo` | linear-response / local-equilibrium誤差 |
| `epsilon_Markov` | finite memoryからMarkov dragへの誤差 |
| `epsilon_refl` | reflection/scattering模型の近似誤差 |
| `epsilon_shell` | finite shell stiffness / mixing誤差 |
| `epsilon_back` | signal, wall, shell間のbackreaction誤差 |
| `epsilon_H` | `nu=D_sig` matching誤差 |

B側では概念的に
```math
\varepsilon_B
\lesssim
\varepsilon_{\rm wall}
+\varepsilon_{\rm split}
+\varepsilon_{\rm Doppler}
+\varepsilon_{\rm ent}
+\varepsilon_{\rm Kubo}
+\varepsilon_{\rm Markov}.
```

## 12. 現在の達成状況

| 項目 | 状態 |
|---|---|
| signal-only exact Darboux chart | 明示計算済み |
| signal-only finite-time Schrödinger縮約 | 候補証明あり |
| exact spin current -> Schrödinger current | 候補証明あり |
| 最終親HamiltonianへのR194A埋込み | 未完 |
| wall mass `M_DW` | 既知縮約と整合 |
| biaxial routeでの `m_sig=M_DW` matching非空性 | 確認 |
| coherent-background Doppler coefficient | 明示計算済み |
| moving-wall `-dot X P_m` | 既知構造と整合 |
| fast-sector entrainment `u_fast~v_s` | 未証明・主ネック |
| positive Ohmic drag `Gamma_m>0` | 具体模型未固定 |
| harmonic classical bathの `Gamma_m` linear-in-`T` scaling | 条件付き導出 |
| `G D_sig=1` | matching条件を同定、実現未証明 |
| 2-spin shell状態数 | 厳密 |
| shell finite mixing / backreaction | 未証明 |
| Nelson代数 after assumptions | 閉じている |
| simultaneous nonempty parameter regime | 未証明 |

## 13. 正本昇格の最低条件

M56を主線へ置き換える前に、最低限次を同時に満たす必要がある。

1. single parent spin modelを固定する。
2. その模型上でfinite-time Schrödinger signal縮約を示す。
3. coherent signalとfast thermal sectorを有限誤差で分離する。
4. `v_D=v_s+O(epsilon_Doppler)` を示す。
5. `u_fast=v_s+O(epsilon_ent)` を示す。
6. `Gamma_m>0` と有限 `tau_mem` を示す。
7. Markov/Smoluchowski windowを示す。
8. entropy shellのfinite mixing、初期 `p=rho`、backreactionを制御する。
9. `nu=D_sig+O(epsilon_H)` を示す。
10. 以上を同時に満たす非空なparameter regimeを示す。

## 14. 現時点で主張しないこと

本メモの更新によって次を主張しない。

- M56がM54、M37、R161、R162、R185を置換した。
- R194Aが最終M56親Hamiltonian上で完全に証明された。
- thermal magnonsが自動的に `j/rho` で流れる。
- finite reflectionだけで `-Gamma_m(dot X-v_s)` が得られる。
- `Gamma_m` が温度に線形であることだけでNelson matchingが自動的に成立する。
- `nu=D_sig` が具体的な単一Hamiltonianで実現済みである。
- M56の全条件を同時に満たすparameter windowが存在すると証明済みである。

詳細計算は `notes/m56_signal_wall_bridge_derivations.md` に分離して保存する。
