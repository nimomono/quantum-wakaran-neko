@number: X
@chapter: 付録
@title: M61 単一Hamiltonian multiband媒体・複合mobile subsystem Q3親模型
@status: M60を置換せず、その下位に置くQ3の単一時間非依存Hamiltonian親模型。R200CでM37 signalとM60 chiral sectorを一つのmultiband媒体へ載せ、R200Aでmoving branch converterをHamiltonian化し、R200BでX-Yに結合する内部harmonic continuumからGLE/FDTを厳密に導く。R198Dの具体的core mixing、R199Aのcore--lead同時parameter witness、R200A/Bのtracking--thermal-load同時windowは強化目標A1の残件とする。

## X.1 M61の責務と物理的実体

M61はM60の別案ではなく、M60で別々の部品として書かれていた信号、chiral媒体、moving bath-frame、平衡bath、Duffing shellを一つの時間非依存Hamiltonianへ持ち上げる下位模型である。現行階層を

```math
H_{61}
\longrightarrow
M60
\longrightarrow
R161
\longrightarrow
R185
```

とする。

単一試行で物理的に存在するものは、固定された一つのmultiband Hamiltonian媒体と、一つの複合mobile subsystemである。固定媒体の各cellにはsignal mode族と二つのchiral mode族を置く。mobile subsystemにはtracer座標 $X$、wave pressureを受けるcollective coordinate $Y$、二つの実Duffing内部mode $(q_\sigma,p_\sigma)$、内部harmonic normal modes $(x_\ell,p_\ell)$ を置く。$X$ と $Y$ は同一剛体座標とは仮定せず、同じ複合mobile subsystemに属する二つのcollective coordinateとして扱う。

M61の正本Hamiltonianを

```math
H_{61}
=
H_s
+H_{\chi,\rm lin}
+H_{\chi,\rm nl}
+H_{XY}
+H_D
+H_{\rm th}
+H_{s\chi}
+H_{D\chi}
+H_{Y\chi}
```

とする。全ての項は実正準変数の時間非依存関数であり、複素振幅は実正準平面の略記だけである。

## X.2 signal bandとlab-frame変数

signal sectorにはM37をそのまま採用する。

```math
H_s
=
\sum_i
\left[
\frac{(p_i^s)^2}{2M_s}
+\frac{M_s\omega_0^2(q_i^s)^2}{2}
+\frac{\delta_i(q_i^s)^2}{2}
\right]
+
\frac12\sum_{\{i,j\}}
\kappa_{ij}(q_i^s-q_j^s)^2.
```

規格化正準座標からlab-frame振幅

```math
a_i
=
\frac{Q_i^s+iP_i^s}{\sqrt{2\mathcal J_0}}
```

を定める。M37の回転包絡は $Z_i(t)=e^{i\omega_0t}a_i(t)$ である。従って

```math
|a_i|^2=|Z_i|^2,
\qquad
a_i^*a_j=Z_i^*Z_j
```

であり、R195Aの作用和・差とsignal currentはlab-frame変数でも同じである。M61の時間非依存Hamiltonianには $Z_i$ を直接書き込まず、$a_i$ を使う。

## X.3 chiral physical fieldとM60 envelope

chiral mode族のphysical canonical amplitudeを

```math
\psi_{\sigma n}
=
\frac{Q_{\sigma n}+iP_{\sigma n}}{\sqrt{2\mathcal J_\chi}},
\qquad
\sigma=\pm
```

とし、

```math
H_{\chi,\rm lin}
=
\sum_{\sigma,n}
\Omega_\sigma|\psi_{\sigma n}|^2
-
J\sum_{\sigma,n}
\left(
\psi_{\sigma,n+1}^*\psi_{\sigma n}
+{\rm c.c.}
\right),
```

```math
H_{\chi,\rm nl}
=
\sum_n w_n
\left[
\frac{g_+}{2}|\psi_{+,n}|^4
+\frac{g_-}{2}|\psi_{-,n}|^4
+g_{+-}|\psi_{+,n}|^2|\psi_{-,n}|^2
\right]
```

とする。$w_n=1$ をnonlinear core、$w_n\simeq0$ をballistic leadとする。

固定carrier quasi-momentumを $K_\sigma=\sigma k_0$ とし、

```math
b_{\sigma n}
=
e^{iK_\sigma x_n}\psi_{\sigma n},
\qquad
k_0a=\frac{\pi}{2}
```

と定める。このsite-wise位相回転は時間非依存な正準変換である。

<!-- theorem-start:theorem -->
**定理（R200C：単一multiband媒体からM37 signal / M60 chiral sectorへの持上げ）**

上の変換の下で、physical nearest-neighbor hoppingは厳密に

```math
-iJ\sum_n
(b_{+,n+1}^*b_{+,n}-{\rm c.c.})
+
iJ\sum_n
(b_{-,n+1}^*b_{-,n}-{\rm c.c.})
```

へ移る。また

```math
|\psi_{\sigma n}|^2=|b_{\sigma n}|^2,
\qquad
Q_\sigma
=
\sum_{n\in\mathcal C}|\psi_{\sigma n}|^2
=
\sum_{n\in\mathcal C}|b_{\sigma n}|^2
```

であり、$H_{\chi,\rm nl}$、Liouville測度、閉じた基準coreの $(E,Q_+,Q_-)$ 状態密度は不変である。

signal edgeに対し

```math
C_{e,+}^{\rm lab}
=
\frac{a_i-ia_j}{\sqrt2},
\qquad
C_{e,-}^{\rm lab}
=
\frac{a_i+ia_j}{\sqrt2}
```

を置き、有限幅phase-matched port

```math
\mathcal P_{e\sigma}
=
\sum_n f_{e\sigma n}\psi_{\sigma n}
```

を固定係数で作る。相互作用

```math
H_{s\chi}
=
-\sum_{e,\sigma}\epsilon_{p,\sigma}
\left[
(C_{e,\sigma}^{\rm lab})^*\mathcal P_{e\sigma}
+{\rm c.c.}
\right]
```

は固定二次Hamiltonianである。共通carrier frameと狭帯域port極では現行M60の $H_{37\chi}$ へ有限port誤差で縮約する。bulk mode族が対称性でblock分離される理想模型では不要なsignal--chiral bulk mixingは零である。
<!-- theorem-end:theorem -->

R198B--R198Dの $Q_\pm$ 個別保存を維持するため、M61では $+$ と $-$ を一つのscalar bandの $\pm k_0$ packetへ同一視しない。同一物理媒体の別mode族として保持する。

## X.4 mobile coordinatesとDuffing shell

```math
H_{XY}
=
\frac{P_X^2}{2M_X}
+
\frac{P_Y^2}{2M_Y}
+
V_{\rm per}(X)
```

とする。Duffing sectorはM60 R198Aの実正準対を使い、

```math
H_D
=
\sum_{\sigma=\pm}
\left[
\frac{p_\sigma^2}{2m_\sigma}
+\frac12m_\sigma\omega_\sigma^2q_\sigma^2
\right]
+
\varepsilon V_D,
```

```math
V_D
=
\sum_\sigma\frac{\bar\alpha_\sigma}{4}q_\sigma^4
+\frac{\bar\beta}{2}q_+^2q_-^2
-A(X,a)\sum_\sigma\bar g_\sigma q_\sigma^2
+\frac{\kappa_{\rm sh}}2A(X,a)^2,
```

```math
A(X,a)
=
\bar\alpha
\sum_i\chi_i(X)
\left(
|a_i|^2+\delta q_i\bar S_{\rm ref}
\right)
```

とする。$|a_i|^2=|Z_i|^2$ なのでR198Aのcapacity辞書は変わらない。

線形Duffing正準対から作るharmonic amplitudeを $d_\sigma(q_\sigma,p_\sigma)$ とし、

```math
H_{D\chi}
=
-\sum_\sigma\lambda_\sigma
\left[
d_\sigma^*\mathcal B_\sigma^C(X)
+{\rm c.c.}
\right],
```

```math
\mathcal B_\sigma^C(X)
=
\sum_{n\in\mathcal C}\eta_{\sigma n}^C(X)\psi_{\sigma n}
```

とする。R198Aのnear-identity変換後にM60のaction-angle交換項へ移す際の残差はM61--M60持上げ誤差へ一度だけ入れる。

## X.5 R200A：moving branch converter

moving scatterer領域 $\mathcal S_Y$ をnonlinear coreとsignal portから分離し、

```math
\Psi_\sigma(Y)
=
\sum_{n\in\mathcal S_Y}
\eta_n^Y(Y)\psi_{\sigma n}
```

と置く。

```math
H_{Y\chi}
=
g_Y
\left[
\Psi_+^*(Y)\Psi_-(Y)
+
\Psi_-^*(Y)\Psi_+(Y)
\right]
```

は時間非依存なbranch-conversion Hamiltonianである。M60 envelope表示ではcarrier差により $e^{\pm2ik_0Y}$ が現れ、$-\partial_YH_{Y\chi}$ が波の運動量反作用を与える。

<!-- theorem-start:theorem -->
**定理（R200A：moving branch-converter HamiltonianからR196A bath-frame則への縮約）**

lead packetがcarrier近傍に狭帯域支持を持ち、$|U|/c\le\beta_*<1$、反射係数が1に近く、scatterer通過時間中の $I_\pm$ と $U=\dot Y$ の変化が遅いとする。return-free観測窓 $T<\tau_{\rm ret}$ では、$Y$ の波力は

```math
F_Y^{\rm wave}
=
\Lambda_Y
\left[
I_+\frac{1-\beta}{1+\beta}
-
I_-\frac{1+\beta}{1-\beta}
\right]
+
\delta F_{200A},
\qquad
\beta=\frac{U}{c},
```

へ縮約し、$\Lambda_Y>0$ は共通係数である。理想項の $|\beta|<1$ にある唯一安定な零点は

```math
\beta_*(r)
=
\frac{r}{1+\sqrt{1-r^2}},
\qquad
r=\frac{I_+-I_-}{I_++I_-}.
```

従ってsmooth sector $r=O(a)$ では

```math
U_*(r)=\frac c2r+O(ca^3).
```

$\delta F_{200A}$ は有限帯域、分散、有限反射率、adiabatic lag、返り波、非理想mode mixingを含む。
<!-- theorem-end:theorem -->

全M61では $H_{Y\chi}$ が $Q_+$ と $Q_-$ を交換するため個別保存はしない。R198B--R198Dが使う保存量は、$H_{s\chi}$、$H_{D\chi}$、$H_{Y\chi}$ を閉じた基準coreに限定する。

## X.6 R200B：内部harmonic continuum

mobile subsystemの内部normal modesを

```math
H_{\rm th}
=
\sum_\ell
\left[
\frac{p_\ell^2}{2m_\ell}
+
\frac{m_\ell\omega_\ell^2}{2}
\left(
x_\ell-
\frac{c_\ell}{m_\ell\omega_\ell^2}(X-Y)
\right)^2
\right]
```

で結合する。平方内の $(X-Y)^2$ 項はthermal couplingのcountertermであり、Duffing側の $A^2$ 項とは別の責務を持つ。

<!-- theorem-start:theorem -->
**定理（R200B：内部harmonic continuumからrelative-coordinate GLE/FDTへの厳密縮約）**

初期bathを $X(0)-Y(0)$ に条件づけた温度 $T$ のGibbs分布から準備する。内部modesを厳密に消去すると

```math
F_X^{\rm th}(t)
=
-\int_0^t
\Gamma(t-s)
[\dot X(s)-\dot Y(s)]\,ds
+
\xi(t),
```

```math
F_Y^{\rm th}(t)=-F_X^{\rm th}(t),
```

```math
\Gamma(t)
=
\sum_\ell
\frac{c_\ell^2}{m_\ell\omega_\ell^2}
\cos\omega_\ell t,
```

```math
\langle\xi(t)\rangle=0,
\qquad
\langle\xi(t)\xi(s)\rangle
=
k_BT\,\Gamma(|t-s|)
```

を得る。従ってthermal internal forceは $X$ と $Y$ の総運動量収支で相殺する。

Drude spectral densityを選ぶ場合は

```math
J_D(\omega)
=
\gamma_X\omega
\frac{\Lambda^2}{\omega^2+\Lambda^2},
\qquad
\Gamma_D(t)
=
\gamma_X\Lambda e^{-\Lambda t}.
```

有限cutoffのままR200Aと合成し、その後にMarkov極・overdamped極をR196Bで取る。
<!-- theorem-end:theorem -->

R200Bを含むと $Y$ にthermal fluctuationが作用するため、M61でのmoving-frame追従は決定論的pathwise誤差ではなく、有限cutoffにおける二乗平均または確率上界で管理する。

## X.7 support分離と誤差台帳

基本設計条件を

```math
\mathcal C\cap\mathcal P_\sigma=\varnothing,
\qquad
\mathcal C\cap\mathcal S_Y=\varnothing,
\qquad
\mathcal P_\sigma\cap\mathcal S_Y=\varnothing
```

とする。ここで $\mathcal C$ はnonlinear core、$\mathcal P_\sigma$ はsignal port、$\mathcal S_Y$ はmoving scatterer領域である。

M61からM60への追加誤差を

```math
\varepsilon_{61\to60}
=
\varepsilon_{\rm mb}
+\varepsilon_{\rm port}^{61}
+\varepsilon_{\rm sc}
+\varepsilon_{\rm ret}
+\varepsilon_{D\chi}
+\varepsilon_{\rm thload}
```

とする。$\varepsilon_{\rm mb}$ は非理想bulk band mixing、$\varepsilon_{\rm port}^{61}$ は有限幅port、$\varepsilon_{\rm sc}$ はR200A散乱縮約、$\varepsilon_{\rm ret}$ は返り波、$\varepsilon_{D\chi}$ はDuffing near-identity変換下の交換項残差、$\varepsilon_{\rm thload}$ はR200A/B合成時のthermal loadを表す。R200Bのexact GLE部分とR196BのMarkov/overdamped誤差を重複加算しない。

## X.8 R200：M61からM60への条件付き有限時間統合

<!-- theorem-start:theorem -->
**定理（R200：M61単一HamiltonianからM60共通縮約層への条件付き有限時間持上げ）**

R200A--R200C、R198A--R198D、R199Aのsafe-sector仮定を満たし、support分離、有限return-free window、共通carrier較正、有限cutoff thermal bathを取る。固定有限時間で、M61のsignal/chiral/shell/tracer周辺過程はM60の対応する縮約過程へ

```math
d_{\rm BL}
\left(
P_t^{61},P_t^{60}
\right)
\le
C_{61}(T)\varepsilon_{61\to60}
```

の形で接続されるとする。このときR197、R196A--R196C、R161、R185の既存下流評価を同じ誤差台帳へ合成できる。

R200はR198Dの具体的mixing/homogenization witness、R199Aの具体的core--lead同時parameter witness、R200A/Bのtracking--thermal-load同時parameter witnessを証明済みとは扱わない。これらが同じparameter familyで同時に閉じることはQ3-1-A1/Q3-2-A1の残件である。
<!-- theorem-end:theorem -->

## X.9 M60・M0との責務境界

M61はQ3内部の物理実体を統合するが、Q1/Q2のR191 pointer、projector router、記録、reset、共通clockまで一台へ統合しない。従ってM61はM0達成を意味しない。

M60は退役させない。M61がlab-frame単一Hamiltonian、M60がcarrier/envelope・core/lead・GLEへの縮約層、R161が位置経路法則、R185が時間反転・時間対称Newton則を担う。
