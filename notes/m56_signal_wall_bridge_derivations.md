# M56 signal--wall bridge 技術メモ

## 1. 目的と状態区分

このメモは `brownian_spin_q1_q3_unification.md` の技術補助である。M56を正本へ昇格させる根拠にはまだ使わない。今回の議論で具体化したsignal縮約、domain-wall質量matching、Doppler係数、classical thermal-magnon scalingを式つきで保存し、未証明のfast-sector entrainmentを明確に分離する。

結果は次の3種類に分ける。

- **明示計算済み**：仮定した模型の下で代数または局所展開を最後まで実行したもの。
- **controlled asymptotic**：小振幅、長波長、有限時間、Markovなどの明示した極限で誤差を制御できるもの。
- **未証明候補**：M56全体へ必要だが、同一親模型からまだ導出していないもの。

## 2. signal-only classical spin model

有限無向グラフ `G=(V,E)`、固定spin長 `Sigma`、対称非負辺重み `g_ij` を考える。各頂点の古典spinは
```math
|\mathbf S_i|=\Sigma,
\qquad
\{S_i^a,S_j^b\}
=\delta_{ij}\epsilon^{abc}S_i^c.
```

signal-only Hamiltonianを
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
とする。

これは強磁性交換と局所縦磁場からなる `U(1)` 対称模型である。domain wallを同時に持つ最終M56親Hamiltonianではなく、R194Aのsignal-only検算用模型として使う。

## 3. exact Darboux chart

north-pole patchで
```math
S_i^x
=Q_i
\sqrt{\Sigma-\frac{Q_i^2+P_i^2}{4}},
```
```math
S_i^y
=P_i
\sqrt{\Sigma-\frac{Q_i^2+P_i^2}{4}},
```
```math
S_i^z
=\Sigma-\frac{Q_i^2+P_i^2}{2}
```
と置く。この表示は
```math
|\mathbf S_i|=\Sigma
```
を厳密に満たす。

`I_i=(Q_i^2+P_i^2)/2`、`Q_i=sqrt(2I_i) cos(theta_i)`、`P_i=sqrt(2I_i) sin(theta_i)` と書けば、標準正準構造 `\{I_i,theta_j\}=delta_ij` から
```math
\{Q_i,P_j\}=\delta_{ij}
```
およびspin Poisson bracketを厳密に再現する。

従って現行R194Aにあった
```math
\{Q_i,P_j\}
=\delta_{ij}+O(\varepsilon_{\rm amp})
```
という近似正準化は不要である。

複素signal座標を
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

## 4. exact Hamiltonian decomposition

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
とする。

一辺について
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
=\psi^\dagger h_L\psi
+R_{\rm nl},
```
```math
h_L
=\frac{\mathcal J_0^2}{2m}L_g+V,
```
```math
R_{\rm nl}
=
\frac{\mathcal J_0^2}{2m}
\sum_{\{i,j\}\in E}g_{ij}
\left[
2(1-A_{ij})x_{ij}
-\beta\rho_i\rho_j
\right].
```

局所potential項は
```math
\frac{V_i}{\mathcal J_0}(\Sigma-S_i^z)
=V_i|\psi_i|^2
```
なので非線形補正を生じない。

Hamilton方程式は
```math
i\mathcal J_0\dot\psi
=h_L\psi+N(\psi).
```
一辺からsite `i` へ来る非線形項は
```math
N_i^{(ij)}
=
\frac{\mathcal J_0^2g_{ij}}{2m}
\left[
(1-A_{ij})\psi_j
+\beta\frac{a_j}{2a_i}x_{ij}\psi_i
-\beta\rho_j\psi_i
\right].
```

## 5. exact action conservation and finite-time bound

総signal作用を
```math
\mathcal A
=\sum_i(\Sigma-S_i^z)
=\mathcal J_0\|\psi\|_2^2
```
とする。Hamiltonianはglobal `z` rotationに不変なので
```math
\frac{d\mathcal A}{dt}=0.
```

無次元小振幅量を
```math
\varepsilon_{\rm amp}
=\frac{\mathcal A}{\Sigma}
=\frac{\mathcal J_0\|\psi\|_2^2}{\Sigma}
```
とする。この量も厳密保存される。

`0<epsilon_amp<=epsilon_0<1` とし
```math
a_*
=\sqrt{1-\frac{\varepsilon_0}{2}}
```
と置く。辺ごとに
```math
1-A_{ij}
\le\frac{\varepsilon_{\rm amp}}{2},
```
```math
\beta\rho_i\le\varepsilon_{\rm amp},
\qquad
\beta|x_{ij}|
\le\frac{\varepsilon_{\rm amp}}{2}.
```

最大重み付き次数
```math
d_g
=\max_i\sum_jg_{ij}
```
を用いると
```math
\|N(\psi)\|_2
\le
\frac{\mathcal J_0^2}{2m}
 d_g
 C_N(\varepsilon_0)
 \varepsilon_{\rm amp}
 \|\psi\|_2,
```
```math
C_N(\varepsilon_0)
=\frac32+
\frac{1}{4\sqrt{1-\varepsilon_0/2}}.
```

目標Schrödinger解
```math
i\mathcal J_0\dot\psi_L
=h_L\psi_L,
\qquad
\psi_L(0)=\psi(0)
```
と比べ、Duhamel公式とunitarityから
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

一定 `d_g` で
```math
T=c_T\frac{2m}{\mathcal J_0d_g}
```
なら相対誤差は
```math
\le
C_N(\varepsilon_0)c_T\varepsilon_{\rm amp}.
```

これは固定有限時間における `O(epsilon_amp)` Schrödinger縮約である。小振幅量が厳密保存されるため、この評価にはGrönwall増幅を必要としない。

## 6. exact spin current

局所density `rho_i=|psi_i|^2` は厳密な離散連続の式
```math
\dot\rho_i
+\sum_jj_{ij}^{\rm spin}=0
```
を満たす。

exact edge currentは
```math
j_{ij}^{\rm spin}
=
\frac{\mathcal J_0}{m}
 g_{ij}A_{ij}
 \operatorname{Im}(\bar\psi_i\psi_j).
```

目標Schrödinger current
```math
j_{ij}^{\rm Sch}
=
\frac{\mathcal J_0}{m}
 g_{ij}
 \operatorname{Im}(\bar\psi_i\psi_j)
```
との差は
```math
|j_{ij}^{\rm spin}-j_{ij}^{\rm Sch}|
\le
\frac{\varepsilon_{\rm amp}}{2}
\frac{\mathcal J_0g_{ij}}{m}
|\psi_i||\psi_j|.
```

1次元格子 `g_{i,i+1}=1/a^2`、`psi_i=sqrt(a) phi(x_i)` としてsmooth long-wave limitを取ると
```math
j^{\rm spin}
=
\frac{\mathcal J_0}{m}
\operatorname{Im}(\bar\phi\partial_x\phi)
+O(\varepsilon_{\rm amp})
+O(a^2).
```

Madelung表示
```math
\phi
=\sqrt\rho\,e^{iS/\mathcal J_0}
```
では
```math
j^{\rm spin}
=\rho\frac{\partial_xS}{m}
+O(\varepsilon_{\rm amp})+O(a^2).
```
node-free領域で
```math
v_s=\frac{j}{\rho}
=\frac{\partial_xS}{m}
+O\!\left(\frac{\varepsilon_{\rm amp}+a^2}{\rho_*}\right).
```

## 7. biaxial wall mass and signal mass matching

整合性確認用に
```math
H
=\frac12\int dx\,
\left[
A|\partial_x\mathbf n|^2
+K_e(1-n_z^2)
+K_hn_y^2
\right]
```
を考える。

```math
\lambda=\sqrt{\frac{A}{K_e}},
\qquad
\kappa=\frac{K_h}{K_e}
```
とする。低角度wall作用は
```math
L_{\rm DW}
=2s\Phi\dot X
-K_h\lambda\Phi^2
-V(X)
```
なので
```math
G=2s,
\qquad
\kappa_\Phi=2K_h\lambda,
```
```math
M_{\rm DW}
=\frac{G^2}{\kappa_\Phi}
=\frac{2s^2}{K_h\lambda}.
```

一様偏極状態まわりのspin-wave dispersionは
```math
\omega(k)
=\frac1s
\sqrt{(Ak^2+K_e)(Ak^2+K_e+K_h)}.
```
長波長では
```math
\omega(k)
=\omega_0+D_{\rm sig}k^2+O(k^4),
```
```math
D_{\rm sig}
=\frac{A(2+\kappa)}{2s\sqrt{1+\kappa}}.
```

Schrödinger表示 `D_sig=J0/(2m_sig)` から
```math
m_{\rm sig}
=\frac{\mathcal J_0s\sqrt{1+\kappa}}
{A(2+\kappa)}.
```

`m_sig=M_DW` は
```math
\frac{\mathcal J_0}{s\lambda}
=\frac{2(2+\kappa)}
{\kappa\sqrt{1+\kappa}}
```
と同値である。右辺
```math
f(\kappa)
=\frac{2(2+\kappa)}
{\kappa\sqrt{1+\kappa}}
```
は `kappa>0` で単調減少し、`kappa->0+` で `infinity`、`kappa->infinity` で `0` へ向かう。従って任意の正の `J0/(s lambda)` に対し正のmatching `kappa` が一意に存在する。

これはmass equalityの非空性を示すだけであり、biaxial模型を最終M56親模型に確定するものではない。

## 8. U(1) signal background上のDoppler coefficient

`U(1)` 対称なcontinuum spinを
```math
\mathbf n
=(\sqrt{1-n^2}\cos\phi,
  \sqrt{1-n^2}\sin\phi,
  n)
```
とする。gradient energyは
```math
H_{\rm grad}
=\frac A2\int dx\,
\left[
\frac{(\partial_xn)^2}{1-n^2}
+(1-n^2)(\partial_x\phi)^2
\right].
```

一様背景
```math
n=n_0,
\qquad
\phi=qx
```
を取る。north-pole action densityとNoether currentを
```math
\rho=s(1-n_0),
```
```math
j=A(1-n_0^2)q
```
とすれば
```math
v_s=\frac{j}{\rho}
=\frac A s(1+n_0)q.
```

`n=n_0+delta n`、`phi=qx+delta phi` と展開する。gradient energyの二次項には
```math
H_2^{\rm cross}
=-2An_0q\int dx\,
\delta n\,\partial_x\delta\phi
```
が現れる。これはfast fluctuationのmomentumに比例するDoppler項であり、dispersion tiltは
```math
v_D
=\frac{2A}{s}n_0q.
```

従って
```math
\chi
=\frac{v_D}{v_s}
=\frac{2n_0}{1+n_0}.
```
`epsilon=1-n_0` と書けば
```math
|\chi-1|
=\frac{\varepsilon}{2-\varepsilon}.
```
したがって小振幅極 `epsilon->0` で
```math
v_D=v_s+O(\varepsilon v_s)
```
が制御できる。

この結果はDoppler generatorの係数を決めるものであり、thermal fast sectorの分布が速度 `v_s` のdrifting Gibbs stateになることを意味しない。

## 9. moving wall boost and the entrainment gap

wall frame `x'=x-X(t)` への変換ではfast magnon momentum `P_m` に
```math
H_{\rm move}\supset-\dot X P_m
```
が現れる。coherent backgroundのDoppler項と合わせると
```math
H_{\rm fast}^{(2)}
=H_0-(\dot X-v_D)P_m+\cdots.
```

しかし、ここから直接
```math
F_m=-\Gamma_m(\dot X-v_s)
```
とは結論しない。必要なのはthermal fast sectorの実際のnormal drift `u_fast` が
```math
u_{\rm fast}
=v_s+O(\varepsilon_{\rm ent})
```
となること、または条件付き分布が
```math
\mu_{\rm fast}(dY)
\propto
\exp[-\beta(H_{\rm fast}-v_sP_m)]dY
```
へ緩和することを示すことである。

Doppler shiftとthermal entrainmentは別問題である。一般のthermal magnon dragやwall torqueはcurrent `j` に比例し得るが、`j/rho` を自動的に読むわけではない。このgapをM56のR194F-b残件として固定する。

## 10. finite reflection and positive drag

bare continuum easy-axis wallは特殊なreflectionless scatteringを持つため、低周波Ohmic係数が消える場合がある。M56でMarkov Brownian wallを得るには、採用模型で
```math
R(k)\not\equiv0,
```
```math
\Gamma_m
=\lim_{\omega\to0}\operatorname{Re}\eta(\omega)>0,
```
```math
\tau_{\rm mem}<\infty
```
を示す必要がある。

候補は高次軸対称異方性、easy-cone wall、格子離散性、dipolar interaction、higher-gradient exchangeなどである。このメモでは特定候補をまだ固定しない。

## 11. harmonic classical bath and explicit temperature scaling

fast thermal sectorが
```math
H_f=\frac12Y^TKY
```
で、wallへ作用するcentered force `delta F(Y)` が `Y` の二次形式であるとする。canonical thermal stateで
```math
Y=\sqrt{k_BT}\,Z
```
と書くと `Z` の分布とharmonic dynamicsは明示的な `T` を含まず
```math
\delta F(Y)
=k_BT\,\delta f(Z).
```
従って
```math
\langle\delta F(t)\delta F(0)\rangle_T
=(k_BT)^2C_0(t).
```

classical Green--Kubo kernelは
```math
\eta_T(t)
=\frac1{k_BT}
\langle\delta F(t)\delta F(0)\rangle_T
=k_BT\,C_0(t).
```

```math
\mathcal G
=\int_0^\infty C_0(t)dt
```
が有限かつ正でMarkov縮約が許されるなら
```math
\Gamma_m(T)
=k_BT\,\mathcal G.
```
Einstein relationから
```math
\nu
=\frac{k_BT}{\Gamma_m}
=\frac1{\mathcal G}.
```

従ってclassical harmonic windowではFDT由来の明示的な `k_BT` は相殺される。ただしHamiltonian係数のthermal renormalizationや追加drag `Gamma_0` は別である。

追加dragがある場合
```math
\Gamma_{\rm tot}
=\Gamma_0+k_BT\mathcal G,
```
```math
\nu(T)
=\frac{k_BT}
{\Gamma_0+k_BT\mathcal G}.
```

## 12. diffusion--dispersion matching

signal dispersion係数を
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
と同値である。

harmonic bath result `nu=1/G` を用いると
```math
\mathcal G D_{\rm sig}=1
```
が必要十分なmatching equationになる。

従って今後の具体模型計算では、単に `Gamma_m>0` を示すだけでなく、同じ模型から `G` と `D_sig` を計算し、この無次元積が1に達するparameter pointまたはcontrolled windowを探す。

## 13. 今回閉じなかった項目

次は本メモでは未証明のまま残す。

1. signal theoremをdomain wallとthermal sectorを同時に持つ単一親Hamiltonianへ埋め込むこと。
2. coherent signal / fast thermal sectorの有限誤差分離。
3. fast-sector entrainment `u_fast=v_s+O(epsilon_ent)`。
4. 具体的reflection-breaking Hamiltonianでの `Gamma_m>0` と有限memory time。
5. 具体的同一模型での `G D_sig=1`。
6. entropy shellのfinite stiffness、mixing、初期 `p=rho`、backreaction。
7. 以上を同時に満たす非空parameter regime。

これらが閉じるまではM56を正本の主模型へ昇格させない。
