@number: Y
@chapter: 付録
@title: M62 一成分Hamiltonian lattice Q3単一場統合候補
@status: M61/M60の現行固定達成主線を置換しないQ3強化候補。一組の実格子正準変数からkink位置、2 shell mode、signal continuum、prethermal reservoir、reaction-coordinate frameを同時に得ることを狙う。R201A--R201Eには解析構造とcandidate numerical witnessがあるが、full normal-form remainder、validated shell--reservoir exchange、prethermal lifetime、finite-memory Markov誤差、同一parameter setでのR201F合成は未閉鎖とする。

## Y.1 M62の責務と基本Hamiltonian

M62は、一格子点あたり一組の実正準変数

```math
(\phi_n,\pi_n),\qquad n\in\mathbb Z
```

だけを基本自由度とする一成分古典Hamiltonian latticeである。M62は「場が究極的実体である」ことを仮定しない。ここでの格子変数は、より下位の粒子系や連続体から得るcollective displacement/order parameterであってもよい。

正本候補Hamiltonianを

```math
H_{62}
=
\sum_n
\left[
\frac{\pi_n^2}{2}
+
U_v(\phi_n)
+
\frac14 B_v(\phi_n)\pi_n^4
\right]
+
\frac12
\sum_n\sum_{r\ge1}
\kappa_r
(\phi_{n+r}-\phi_n)^2
```

とする。field-amplitude scaleを

```math
U_v(\phi)=v^2U_*(\phi/v),
\qquad
B_v(\phi)=B_*(\phi/v),
\qquad
B_*(u)\ge0
```

とする。$v$ を増やすと線形kink spectrumを保ったまま $U^{(3)}=O(v^{-1})$、$U^{(4)}=O(v^{-2})$、$U^{(5)}=O(v^{-3})$ とできる。

代表的な正の長距離結合として、格子幅 $a=0.1$ の規格化で

```math
\kappa_r
=
\frac{200}{9}\,3^{1-r}
```

を用いる。このとき真空まわりのdispersionは

```math
\omega^2(q)
=
16+
\frac{400(1-\cos q)}{5-3\cos q}
```

であり、continuum下端は $4$、上端は $\sqrt{116}$ である。

M62でkink位置、shell、signal、reservoir、reaction-coordinate frameは別々の場ではなく、同じ $(\phi_n,\pi_n)$ の異なるcollective sectorとして定義する。

## Y.2 R201A：kink・低位spectrum・continuum

$U_*$ は二つの安定真空を持ち、それらを結ぶ単調kink $\phi_n^K(X)$ を持つように選ぶ。kinkまわりの線形化作用素は、continuum下にPeierls--Nabarro/translation modeと2個のshell modeだけを持つことを要求する。

<!-- theorem-start:theorem -->
**定理（R201A：kink・2-shell・continuum構成）**

あるM62 parameter familyで

```math
0<\omega_{\rm PN}
<
\omega_1
<
\omega_2
<
\omega_{\min}^{\rm cont}
```

かつ

```math
3\omega_2<\omega_{\min}^{\rm cont}
```

を満たし、PN/translation modeと2 shell mode以外の局在modeをcontinuum下に持たない構成を取れる。
<!-- theorem-end:theorem -->

最終格子再較正のcandidate witnessでは、stability-well parameterを

```math
A_0\simeq37.5782,
\qquad
A_{\rm side}\simeq35.4820,
\qquad
d\simeq1.45
```

とした有限格子計算で

```math
\omega_{\rm PN}\simeq0.28284,
\qquad
\omega_1\simeq1.19599,
\qquad
\omega_2\simeq1.21700,
\qquad
\omega_3\simeq4.00659
```

を得ている。これらは解析証明ではなくparameter-design witnessとして扱う。

## Y.3 R201B：same-field signal sector

continuumのうち狭帯域wave packet sectorをsignalとして選び、その包絡を $Z(x,t)$ と書く。$Z$ は独立した複素実体ではなく、実格子場の狭帯域正準振幅の派生表示である。signalのwave-action density/currentを $\rho_{\rm sig}$、$j_{\rm sig}$ とし、局所capacityを

```math
A[X,Z]
=
\int K_A(x-X)\rho_{\rm sig}(x,t)\,dx
```

のような局所汎関数で定義する。

<!-- theorem-start:theorem -->
**定理（R201B：same-field signal/carrier縮約）**

M62 continuumに狭帯域・弱分散sectorを選ぶと、固定有限時間で有効Schrödinger型signal envelope、対応する局所wave-action density/current、kink coreが読むcapacity $A[X,Z]$ へ縮約できる。signal sector、right/left carrier sector、reservoir sectorは同じcontinuum上の異なるwave-packet sectorであり、別の物理場を導入しない。
<!-- theorem-end:theorem -->

R201Bの有限時間包絡誤差と、現行M37/R86に対応する有効質量・作用尺度の完全なparameter辞書は未閉鎖である。従って現行Q3-1達成証人をM62へ差し替えない。

## Y.4 R201C：weighted-shell normal form

2つのshell modeのactionを $(K_1,K_2)$ とし、

```math
S_w=a_1K_1+a_2K_2,
\qquad
a_1,a_2>0,
\qquad
a_1+a_2=2
```

をweighted shell actionとする。$K_1=S_wu/a_1$、$K_2=S_w(1-u)/a_2$ と置けば

```math
dK_1dK_2
=
\frac{S_w}{a_1a_2}\,dS_w\,du
```

なので、2-action shellのradial state-count factor $S_w$ を保ったままshell frequencyの非縮退を許容できる。

$B_*$ は一つの非負関数として設計するが、責務を見やすくするため

```math
B_*=B_{\rm bulk}+B_{\rm shell}+B_{\rm ex}
```

と分解してよい。この分解は別の物理自由度を追加するものではない。

<!-- theorem-start:theorem -->
**定理（R201C：weighted-shell normal form）**

R201Aのspectral conditionの下でnear-identity canonical transformationを取り、

```math
H_{\rm sh}^{\rm NF}
=
\omega_1K_1+\omega_2K_2
+
\frac{\kappa_{\rm sh}}2
\left[
S_w-A[X,Z]
\right]^2
+
R_{\rm NF}
```

とする。quartic coefficientは

```math
C_{11}=\frac{\kappa_{\rm sh}a_1^2}{2},
\qquad
C_{22}=\frac{\kappa_{\rm sh}a_2^2}{2},
\qquad
C_{12}=\kappa_{\rm sh}a_1a_2
```

へ合わせ、angle-dependent quartic項はnormal formで除去する。5次以上のremainderについて

```math
|\dot S_w|
\le
D_5 S_w^{5/2}+O(S_w^3)
```

型の有限時間上界を目標とする。
<!-- theorem-end:theorem -->

現在の探索的な安全側設計値は概ね

```math
D_5^{\rm safe}\sim\frac{10^3}{v}
```

である。例えば $v=5\times10^5$、$S_w=0.08$ では10% driftまでの目安は $T_{\rm NF}\sim2.2\times10^3$ となる。continuum virtual modeまで含むfull Lie-transform boundは未証明であり、この数値をrequired boundとして扱わない。

## Y.5 R201D：prethermal reservoirとshell交換

far-field continuumの4-wave mixingをreservoirとする。M62ではshellのradial coordinate $S_w$ と、prethermalに近似保存される全wave action

```math
\mathcal N=K_1+K_2+Q_{\rm res}
```

を区別する。reservoir chemical potentialを $\mu$ とし、

```math
\frac{\omega_1-\mu}{a_1}
=
\frac{\omega_2-\mu}{a_2}
=
\lambda
```

を満たすweightsを取ると、$A_{\rm eff}=A-\lambda/\kappa_{\rm sh}$ へ線形項を吸収できる。

<!-- theorem-start:theorem -->
**定理（R201D：prethermal reservoir・weighted-shell Gibbs marginal）**

continuum 4-wave mixingがshell交換より速く局所混合し、観測時間中に $\mathcal N$ のnumber-changing過程が遅いprethermal regimeを取る。このときshell marginalは

```math
\pi_A(S_w)
\propto
S_w
\exp\left[
-\frac{\beta\kappa_{\rm sh}}2
(S_w-A_{\rm eff})^2
\right]
```

へ近づく。
<!-- theorem-end:theorem -->

shell--continuum交換を増強するcandidateとして、kink座標上で

```math
B_{\rm ex}(\phi_K(x))
=
A_L e^{-(x+1.8)^2/[2(0.12)^2]}
+
A_R e^{-(x-1.8)^2/[2(0.12)^2]},
\qquad
A_L\simeq340,
\quad
A_R\simeq445
```

というtail-localized bumpを用いた。単調kink上では一価な $B(\phi)$ に対応する。

有限箱の実scattering eigenmodeを用いた探索的FGRでは

```math
\Gamma_1^{\rm ex}\simeq(6.6\pm0.8)\times10^{-3},
\qquad
\Gamma_2^{\rm ex}\simeq(5.8\pm0.7)\times10^{-3}
```

すなわち $\tau_{\rm ex}\sim150$--$180$ を得た。直接非線形trajectoryでも $O(10^2)$ のaction再配分を観測した。harmonic wave-action diagnosticは少なくとも $t=800$ まで数%程度の変化に留まり、$\tau_{\mathcal N}>800$ という探索的lower boundを得ている。finite-box、energy broadening、sampling、長時間外挿を含むvalidated boundは未完である。

## Y.6 R201E：reaction-coordinate frameとGLE/FDT

$Y$ は独立したミクロ正準自由度として追加しない。同じcontinuumのsignal wave-action flowから、kink近傍の局所Lagrangian frameとして

```math
\rho_Y=\int K_Y(x-Y)\rho_{\rm sig}(x)\,dx,
\qquad
j_Y=\int K_Y(x-Y)j_{\rm sig}(x)\,dx,
\qquad
\dot Y=\frac{j_Y}{\rho_Y}
```

と定義する。

<!-- theorem-start:theorem -->
**定理（R201E：same-field reaction coordinate・GLE/FDT）**

M62 reservoirを消去すると、kink位置 $X$ について

```math
M_X\ddot X
=
F_{\rm eff}
-
\int_0^t
\Gamma(t-s)
[\dot X(s)-\dot Y(s)]\,ds
+
\xi(t)
```

を得て、平衡条件下で

```math
\langle\xi(t)\rangle=0,
\qquad
\langle\xi(t)\xi(s)\rangle
=
k_BT\,\Gamma(|t-s|)
```

を満たす。memoryが観測時間より短い場合、local-friction GLEへ有限誤差で縮約する。
<!-- theorem-end:theorem -->

同じnonlinear Hamiltonianのorthogonal-dynamics探索ではmemory kernelの主成分は $t\sim10$--$20$ で減衰し、弱いoscillatory tailを安全側に含めると $\tau_{\rm mem}^{\rm safe}\sim40$--$50$ 程度である。完全なdelta-memory極は仮定せず、convolutionとlocal frictionの差を有限時間誤差として評価することをR201Eの残件とする。

## Y.7 R201F：同一parameter setでの有限時間合成

<!-- theorem-start:theorem -->
**定理（R201F：M62からQ3共通有効過程への有限時間合成）**

R201A--R201Eを同じM62 parameter setで満たし、

```math
\max(
\tau_{\rm mix},
\tau_{\rm ex},
\tau_{\rm mem}
)
\ll
T_{\rm obs}
\ll
\min(
T_{\rm NF},
\tau_{\mathcal N}
)
```

となる非空の観測時間窓を取れるなら、M62のsignal/shell/kink周辺過程をR161の位置経路interfaceへ有限誤差で接続し、その後のR185時間反転・時間対称Newton則を既存の共通数学核として再利用できる。
<!-- theorem-end:theorem -->

現時点のcandidate witnessは概ね

```math
\tau_{\rm mem}\sim10\text{--}50,
\qquad
\tau_{\rm ex}\sim150\text{--}200,
\qquad
\tau_{\mathcal N}>800,
\qquad
T_{\rm NF}\sim2\times10^3
```

であり、$T_{\rm obs}\sim500$ のstrict inequality自体は満たし得る。ただし両側で十分強い $\ll$ separationをvalidated boundとして確立したわけではない。従ってR201Fは未閉鎖とする。

## Y.8 現行主線との責務境界

M62/R201は現時点でM61/R200--M60/R198/R199/R196主線を置換しない。固定目標Q3-1/Q3-2の達成ラベル、Q3-1-A1/Q3-2-A1の部分達成、Q3-1-A2/Q3-2-A2の未監査は変更しない。

M62を現行Q3ミクロ主線へ昇格させる条件は、少なくとも次の4点である。

1. continuum virtual modeを含むR201C full remainder boundを閉じる。
2. R201Dのshell--reservoir交換率とprethermal $\tau_{\mathcal N}$ をfinite-size/sampling依存込みで検証する。
3. R201Eのmemory convolutionをlocal frictionへ置く有限時間誤差を評価する。
4. R201Fの共通parameter setで十分なmarginを持つ時間窓を示す。

それまではM62の数値結果をcandidate witnessとして管理し、現行required verifierへ昇格させない。
