# M56 Brownian-spin Q1/Q3統合候補

## 1. 位置づけ

M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理でどこまで統合できるかを調べる現役研究候補である。橋渡し結果候補をR194A--R194Hと呼ぶ。

現時点ではQ3-2の達成根拠を変更しない。現行主線はM54空間状態構成、R161、R162、R185であり、R162を退役しない。M37とR191の責務も変更しない。本メモと関連する技術メモは `notes/` にとどめ、正本の結果番号、固定目標、達成判定へはまだ反映しない。

今回の検討で、signal自身から
```math
v_s=\frac{j}{\rho}
```
を定義し、coherent background上のfast fluctuationに現れるDoppler速度 `v_D` が小振幅極で `v_s` に一致するところまでは具体化した。一方、Doppler shiftだけからthermal fast sectorが速度 `v_s` で共流することは従わない。従って現行の研究線は
```text
spin signal -> v_s=j/rho -> Doppler v_D~v_s
            -> fast-sector entrainment ?
            -> relative-velocity Kubo drag
```
と整理する。

旧R194Dのphase-bus経路は主候補から外したまま保持する。ただしrelative-velocity経路がfast-sector entrainmentで閉じない場合のfallback候補として再検討可能な形で残す。

M56が主線へ昇格するには、単一の親spin模型上でsignal縮約、coherent/thermal分離、Doppler、fast-sector entrainment、正の低周波drag、entropy shell、wall Brownian縮約、diffusion--dispersion matchingを同時に満たす非空なparameter regimeを示す必要がある。

## 2. 最小構成

基本実体は固定長古典spin、spin texture、熱浴である。複素振幅は独立実体ではなく実spin自由度の派生表示とする。

| sector | 物理自由度 | 役割 |
|---|---|---|
| signal | 偏極spinの小振幅横mode | Schrödinger型signal、密度 `rho`、位相 `S`、局所流速 `v_s=j/rho` |
| particle | domain wall | 実在位置 `X`、必要なら内部角 `Phi` |
| entropy shell | 2 Brownian spinの作用自由度 | `rho` に比例する状態数からosmotic forceを作る |
| thermal spin bath | fast spin/magnon sector | friction、Brownian noise、FDT |

R191の単磁区pointer spinをQ3粒子へ流用しない。Q3粒子はdomain-wall collective coordinateである。

## 3. 最終親Hamiltonianは未固定

今回の検討では、異なる目的に二つのspin模型族を用いた。

1. domain-wall質量とsignal dispersionのmatching確認には、biaxial easy-axis/hard-axis模型
```math
H_{\rm biax}
=\frac12\int dx\,
\left[
A|\partial_x\mathbf n|^2
+K_e(1-n_z^2)
+K_hn_y^2
\right]
```
を用いた。
2. signal Noether currentとDoppler係数の明示計算には、azimuthal angleに対する `U(1)` 対称性を持つ模型を用いた。

`K_h n_y^2` は一般に `U(1)` を壊すため、現時点ではこれらを同一Hamiltonianの結果として扱わない。最終M56親模型は未固定であり、biaxial routeと `U(1)`-symmetric wall route（easy-cone、高次軸対称異方性などを含む）を比較する。

## 4. R194A：spin signalの有限時間Schrödinger縮約

### 4.1 signal-onlyで閉じる部分

有限spin graph上の `U(1)` 対称signal模型について、north-pole classical Holstein--Primakoff/Darboux chartを使えば、局所正準対を近似ではなく厳密に取れる。spin長を `Sigma` として
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
\{Q_i,P_j\}=\delta_{ij}
```
と書ける。

複素signalを
```math
\psi_i=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```
とすると、適切な強磁性交換と局所縦磁場から
```math
i\mathcal J_0\dot\psi
=h_L\psi+N(\psi),
```
```math
h_L
=\frac{\mathcal J_0^2}{2m}L_g+V
```
を得る。非線形項は小振幅量
```math
\varepsilon_{\rm amp}
=\frac{\mathcal J_0\|\psi\|_2^2}{\Sigma}
```
に対して `N=O(epsilon_amp)` であり、総signal作用
```math
\mathcal A
=\mathcal J_0\|\psi\|_2^2
```
は `U(1)` 対称性から厳密保存される。

従って固定有限時間で目標Schrödinger解 `psi_L` に対し
```math
\sup_{0\le t\le T}
\frac{\|\psi(t)-\psi_L(t)\|_2}{\|\psi(0)\|_2}
\le
C_{\rm sig}(T)\,\varepsilon_{\rm amp}
```
というDuhamel評価が得られる。詳細は `m56_signal_wall_bridge_derivations.md` に保存する。

またexact spin currentはSchrödinger currentへ `O(epsilon_amp)` で一致し、1次元長波長・node-free領域では
```math
v_s
=\frac{j}{\rho}
=\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2)
```
となる。

### 4.2 未完部分

上記はsignal-only theoremである。domain wall、thermal sector、reflection-breakingを同時に持つ最終M56親Hamiltonianへこの有限時間縮約を埋め込むことは未完である。

## 5. R194B：domain-wall粒子、質量、Brownian縮約

biaxial domain wallを
```math
\mathbf n(x,t)
\simeq
\mathbf n_{\rm DW}(x-X(t),\Phi(t))
```
とし、低角度作用
```math
L_{\rm DW}
=G\Phi\dot X
-\frac{\kappa_\Phi}{2}\Phi^2
-V_{\rm pin}(X)
```
から
```math
P=G\Phi,
\qquad
M_{\rm DW}=\frac{G^2}{\kappa_\Phi}
```
を得る。

biaxial模型
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
として
```math
M_{\rm DW}
=\frac{2s^2}{K_h\lambda}
```
が得られる。同じ模型の長波長spin-wave dispersion
```math
\omega(k)
=\omega_0+D_{\rm sig}k^2+O(k^4)
```
は
```math
D_{\rm sig}
=\frac{A(2+\kappa)}{2s\sqrt{1+\kappa}}.
```
Schrödinger表示 `D_sig=J0/(2m)` を使うと
```math
m_{\rm sig}
=\frac{\mathcal J_0s\sqrt{1+\kappa}}{A(2+\kappa)}.
```
従って `m_sig=M_DW` は
```math
\frac{\mathcal J_0}{s\lambda}
=\frac{2(2+\kappa)}{\kappa\sqrt{1+\kappa}}
```
という1本のmatching条件になる。右辺は `kappa>0` で正かつ `infinity` から `0` へ単調に下がるので、任意の正の `J0/(s lambda)` に対して正の解が一意に存在する。従ってmass equality自体はno-goではない。

ただし、この確認はbiaxial route内の整合性確認であり、最終親Hamiltonianの選定を完了したものではない。

wall collective coordinateとBrownian縮約そのものには既知理論があるが、M56で必要なのはsignal driftと同じbathを使ったrelative-velocity Brownian化であり、これはR194F/Gに依存する。

## 6. R194C：2-spin状態数からosmotic drift

2個のBrownian spinの非負作用 `K_1,K_2` と
```math
A(X,t)=A_*\rho(X,t)
```
に対し
```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}{2}
[K_1+K_2-A(X,t)]^2
```
を置く。厳密2作用殻では
```math
\int_0^\infty dK_1\int_0^\infty dK_2\,
\delta(A-K_1-K_2)
=A,
```
従って `Omega_2(A)` は `A` に比例する。

条件付き自由エネルギーから
```math
F_{\rm osm}
=k_BT\,\partial_X\log\rho
```
が出る。mobilityを `mu_X` とすれば
```math
w_{\rm osm}
=\mu_XF_{\rm osm}
=\nu\partial_X\log\rho,
\qquad
\nu=\mu_Xk_BT.
```

ここで厳密なのは2作用殻の状態数である。有限shell stiffness、有限mixing time、初期 `p(X)=rho(X)` 準備、signalへのbackreactionは未評価である。

## 7. R194D：旧phase-bus経路

旧候補ではeasy-plane phase busをsignalへlockし、spin supercurrentをdomain wallへ渡して
```math
v=\frac{\partial_xS}{m}
```
を作る経路を検討した。

signal自身から `v_s=j/rho` を構成できるため主候補からは降格したが、relative-velocity経路のfast-sector entrainmentが閉じない場合のfallbackとして保持する。旧matching、phase lock、吸収効率は現時点の主線昇格条件には含めない。

通常のmagnon-current torqueだけではwall応答は一般にcurrent `j` に比例し、`j/rho` を直接読む機構にはならない。この点は今回の検証でも維持された。

## 8. R194F：Doppler bridgeとfast-sector entrainment

### 8.1 R194F-a：coherent-background Doppler

`U(1)` 対称な1次元spin模型を
```math
\mathbf n
=(\sqrt{1-n^2}\cos\phi,
  \sqrt{1-n^2}\sin\phi,
  n)
```
で書き、背景
```math
n=n_0,
\qquad
q=\partial_x\phi
```
を考える。signal action densityとNoether currentを
```math
\rho=s(1-n_0),
```
```math
j=A(1-n_0^2)q
```
とすると
```math
v_s=\frac{j}{\rho}
=\frac{A}{s}(1+n_0)q.
```

同じ背景上でfast fluctuationを二次展開すると、cross termからDoppler速度
```math
v_D
=\frac{2A}{s}n_0q
```
が得られる。従って
```math
\chi
=\frac{v_D}{v_s}
=\frac{2n_0}{1+n_0}.
```
`epsilon=1-n_0` とすると
```math
|\chi-1|
=\frac{\varepsilon}{2-\varepsilon}.
```
従ってnorth-pole小振幅極で
```math
v_D
=v_s+O(\varepsilon_{\rm amp}v_s)
```
が制御できる。

moving wall frameではfast magnon momentum `P_m` に
```math
-\dot X\,P_m
```
が入るため、quadratic fast generatorは
```math
H_{\rm fast}^{(2)}
=H_0-(\dot X-v_D)P_m+\cdots
```
まで整理できる。

### 8.2 R194F-b：fast-sector entrainment problem

上のDoppler項だけから、thermal fast sectorの実際のdrift velocityが `v_s` になることは従わない。Doppler generatorとdrifting thermal stateを区別する必要がある。

relative-velocity Brownian化に必要なのは、例えば
```math
u_{\rm fast}
=v_s+O(\varepsilon_{\rm ent})
```
または条件付きfast分布
```math
\mu_{\rm fast}(dY)
\propto
\exp[-\beta(H_{\rm fast}-v_sP_m)]\,dY
```
を導くことである。

これが成立して初めてKubo/Mori縮約から
```math
F_m(t)
=-\int_0^\infty d\tau\,
\eta(\tau)
[\dot X(t-\tau)-v_s(t-\tau)]
+\xi(t)
```
を主張できる。

一般のthermal magnonsではnormal componentがlatticeに対してほぼ静止する可能性があり、その場合は `-Gamma_m dot X` が基本dragになる。既知のmagnon torque/dragも一般にはcurrent `j` に比例し、`j/rho` を自動的に読むわけではない。従ってfast-sector entrainmentは現在のM56で最も重要な未解決点の一つである。

## 9. R194G：finite reflectionとpositive Markov drag

最も単純な連続easy-axis wallはmagnonに対してreflectionlessとなり、低周波Ohmic dragが消える場合がある。このbare continuum模型では
```math
\Gamma_m
=\lim_{\omega\to0}\operatorname{Re}\eta(\omega)
=0
```
となり得る。

従って採用する最終模型にはreflectionless性を壊す機構が必要である。候補は高次軸対称異方性、easy-cone構造、格子離散性、dipolar interaction、higher-gradient exchangeなどである。

R194Gの責務は
```math
R(k)\not\equiv0,
\qquad
\Gamma_m>0,
\qquad
\tau_{\rm mem}<\infty,
```
および
```math
\eta(\omega)
=\Gamma_m+O(\omega\tau_{\rm mem})
```
を具体模型で示すことに限定する。R194G単独からdragの相手側速度を `v_s` と決めない。その部分はR194F-bのentrainmentに依存する。

## 10. R194H：classical-magnon diffusion--dispersion matching候補

### 10.1 harmonic classical bathの温度scaling

fast thermal sectorがharmonic classical field
```math
H_f=\frac12Y^TKY
```
として記述でき、wallへ作用するfluctuating forceがfast変数の二次形式であるとする。canonical thermal stateで
```math
Y=\sqrt{k_BT}\,Z
```
とrescaleすると、connected force correlationは
```math
\langle\delta F(t)\delta F(0)\rangle_T
=(k_BT)^2 C_0(t)
```
とscaleする。classical Kubo kernelは
```math
\eta_T(t)
=\frac{1}{k_BT}
\langle\delta F(t)\delta F(0)\rangle_T
=k_BT\,C_0(t).
```
従って
```math
\mathcal G
=\int_0^\infty C_0(t)dt
```
が有限かつ正なら、Markov極で
```math
\Gamma_m(T)
=k_BT\,\mathcal G,
```
```math
\nu
=\frac{k_BT}{\Gamma_m}
=\frac{1}{\mathcal G}.
```
固定Hamiltonian係数のclassical harmonic windowでは、`nu` の明示的なbath-temperature因子は消える。

これは全温度域で `nu` が厳密一定という主張ではない。低温の量子占有、高温での秩序崩壊、Hamiltonian係数のthermal renormalization、bare Gilbert dragなどは別に評価する必要がある。例えば温度非依存drag `Gamma_0` があれば
```math
\Gamma_{\rm tot}
=\Gamma_0+k_BT\mathcal G,
```
```math
\nu(T)
=\frac{k_BT}{\Gamma_0+k_BT\mathcal G}.
```
plateauには `Gamma_0 << k_B T G` が必要である。

### 10.2 diffusion--dispersion matching

signal dispersionを
```math
\omega(k)
=\omega_0+D_{\rm sig}k^2+O(k^4)
```
とし、Schrödinger表示で
```math
D_{\rm sig}
=\frac{\mathcal J_0}{2m}
```
とする。Nelson matching
```math
\mathcal J_0=2m\nu
```
は
```math
\nu=D_{\rm sig}
```
と同値である。上の `nu=1/G` を使えば必要条件は
```math
\mathcal G D_{\rm sig}=1.
```
従ってR194Hの中心課題は、具体的な最終親Hamiltonianで `G>0` を計算し、`G D_sig=1` を満たすparameter pointまたはcontrolled windowを示すことである。

現時点では、温度scalingの構造とmatching equationの同定までは進んだが、特定の単一Hamiltonianで数値条件を満たすことは未証明である。

## 11. R194E：Nelson合成

以下を仮定する。
```math
v=v_s=\frac{\partial_xS}{m},
```
```math
w_{\rm osm}
=\nu\partial_x\log\rho,
```
```math
\nu=D_{\rm sig}
=\frac{\mathcal J_0}{2m}.
```
forward SDEを
```math
dX_t
=(v+w_{\rm osm})(X_t,t)dt
+\sqrt{2\nu}\,dW_t
```
とする。

Fokker--Planck方程式へ `p=rho` を代入すると
```math
w_{\rm osm}\rho
=\nu\partial_x\rho
```
によりosmotic項と拡散項が相殺し
```math
\partial_t\rho
=-\partial_x(\rho v)
```
が残る。同じforward path lawの時間反転から
```math
b_-
=b_+-2\nu\partial_x\log\rho
=v-w_{\rm osm}
```
を得る。

Nelson加速度
```math
a_N
=\partial_tv
+v\partial_xv
-w_{\rm osm}\partial_xw_{\rm osm}
-\nu\partial_x^2w_{\rm osm}
```
に対し、signalがSchrödinger型方程式を満たし `J0=2m nu` ならMadelung恒等式から
```math
m a_N=-\partial_xV
```
を得る。

ここでのFokker--Planck整合、同経路時間反転、Nelson加速度代数は、物理入力を仮定した後は閉じている。未解決なのは、その物理入力を単一M56親模型から同時に導くことである。

## 12. error ledger

現時点の主要誤差候補を次のように分離する。

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

B側の概念的error budgetは
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

## 13. 現在の達成状況

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
| harmonic classical bathの `Gamma_m proportional T` scaling | 条件付き導出 |
| `G D_sig=1` | matching条件を同定、実現未証明 |
| 2-spin shell状態数 | 厳密 |
| shell finite mixing / backreaction | 未証明 |
| Nelson代数 after assumptions | 閉じている |
| simultaneous nonempty parameter regime | 未証明 |

## 14. 正本昇格の最低条件

M56をM54/M37/R161/R162/R185の主線へ置き換える前に、最低限次を同時に満たす必要がある。

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

## 15. 現時点で主張しないこと

本メモの更新によって次を主張しない。

- M56がM54、M37、R161、R162、R185を置換した。
- R194Aが最終M56親Hamiltonian上で完全に証明された。
- thermal magnonsが自動的に `j/rho` で流れる。
- finite reflectionだけで `-Gamma_m(dot X-v_s)` が得られる。
- `Gamma_m proportional T` だけでNelson matchingが自動的に成立する。
- `nu=D_sig` が具体的な単一Hamiltonianで実現済みである。
- M56の全条件を同時に満たすparameter windowが存在すると証明済みである。

詳細計算は `notes/m56_signal_wall_bridge_derivations.md` に分離して保存する。
