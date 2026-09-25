@number: AA
@chapter: 付録
@title: M67 二実体・構造化熱浴Hamiltonian統合候補
@status: M67/R208A--R208Dは、構造化熱浴と古典マーカーの二つの物理sectorだけからM64型Q3有効力学を回収する有限Hamiltonian candidateである。現行Q3正本M37/R86→M64/R203A--R203D→R161/R185は変更せず、M67はその上位parent候補として扱う。Q1/Q2/NBLへの拡張、M64/M66の退役、M0達成は本付録では主張しない。

## AA.1 目的、二実体、責務境界

M67は、M64で別実体としていたclassical coherent signalとsignal-driven thermal reservoirを一つの構造化熱浴へまとめる。単一試行の主要物理sectorは

```math
\mathcal R_{\rm str}
+
\mathcal X,
\qquad
\mathcal X=(X,P_X)
```

だけとする。$\mathcal R_{\rm str}$ は有限個の古典正準自由度からなる一つのHamiltonian媒体であり、内部にcoherent、phase-volume、flow、dragの各sectorを持つ。これらは別々の物理実体ではなく、同じ媒体の正準部分系またはreaction coordinateである。Q3では $\mathcal X$ をclassical tracerとして読む。

本付録の責務はM67からM64/R203A--R203Dのcontinuous Q3 lawへ有限時間で接続することである。R161/R185は既存の下流数学結果として再利用し、本付録では再証明しない。Q1のM65/R181D、Q2のM54/R181B--R181C、M66/R205--R207、NBL型registerは本付録の直接主張に含めない。

## AA.2 全Hamiltonianとcoherent sector

M67の有限Hamiltonianを

```math
H_{67}
=
H_{\rm coh}
+
H_{\rho}
+
H_U
+
H_{\rm drag}
+
H_X,
\qquad
H_X
=
\frac{P_X^2}{2M_X}
+
V_{\rm ext}(X)
```

とする。coherent sectorにはM37/R86の有限局所振動子網を使う。

```math
H_{\rm coh}
=
\sum_i
\left[
\frac{p_i^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_0^2q_i^2}{2}
+
\frac{\delta_iq_i^2}{2}
\right]
+
\frac12
\sum_{\{i,j\}}
\kappa_{ij}(q_i-q_j)^2.
```

回転包絡 $Z_i$ は $(q_i,p_i)$ の派生表示であり、safe narrow-band sectorでは

```math
i\mathcal J_0\dot Z
=
hZ
+
R_{\rm env},
\qquad
\|R_{\rm env}\|
\le
\varepsilon_{\rm env}.
```

regularized density/currentはR203Aと同じ

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
S=\sum_i|Z_i|^2,
```

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
Z_j^*h_{ji}Z_i
\right)
```

を使う。

## AA.3 phase-volume sectorとsignal backreaction

M64/Y.2と同じcompact interpolationから正のlocal scale $r_X^\delta$ を作る。

```math
H_\rho
=
\sum_{\alpha=1}^{N_\rho}
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\lambda_\alpha(Z,X)^2\zeta_\alpha^2
\right],
```

```math
\lambda_\alpha
=
\left(
\frac{r_X^\delta}{r_*}
\right)^{-w_\alpha},
\qquad
w_\alpha>0,
\qquad
\sum_\alpha w_\alpha=1.
```

固定 $Z,X$ のcanonical積分は

```math
Z_\rho(Z,X)
=
Z_\rho^0
\frac{r_X^\delta}{r_*},
\qquad
F_\rho
=
-k_BT\log r_X^\delta+C_\rho
```

を与え、

```math
\left\langle
-\partial_XH_\rho
\right\rangle
=
k_BT\partial_X\log r_X^\delta.
```

equal weights $w_\alpha=1/N_\rho$ ならphase-volume force fluctuationは $O(N_\rho^{-1/2})$ で自己平均化する。

完全Hamiltonianではsignalへの反作用を消せない。$Z_i=\sqrt{N_0}z_i$ とすると、$r_X^\delta$ が $Z$ の二次量であることから

```math
\frac{\partial\log r_X^\delta}{\partial Z_i^*}
=
O(N_0^{-1/2}),
```

一方 $hZ=O(N_0^{1/2})$ なので、固定有限時間のrelative state-direction backreactionは

```math
\varepsilon_{\rm back}^{\rho}
=
O(N_0^{-1})
```

となる。

## AA.4 local flow reaction coordinate

各edge $e$ にR203Aのlocal current/densityからtarget velocity

```math
v_e[Z]
=
v_{\delta,e}
+
\Delta_{A,e},
\qquad
|\Delta_{A,e}|
\le
\varepsilon_A
```

を定め、flow reaction coordinate $(U_e,P_{U,e})$ とmoving material-frame coordinate $(Y_e,P_{Y,e})$ を置く。

```math
H_U
=
\sum_e
\left[
\frac{P_{U,e}^2}{2I_e}
+
\frac{K_e}{2}
(U_e-v_e[Z])^2
+
\frac{P_{Y,e}^2}{2M_e}
+
P_{Y,e}U_e
\right]
+
H_{U{\rm bath}}.
```

$K_e>M_e$ とbounded $v_e$ のsafe sectorでは、平方完成によりquadratic sectorを下に有界に取れる。Hamilton方程式から

```math
\dot Y_e
=
U_e+\frac{P_{Y,e}}{M_e}.
```

finite harmonic flow bathを消去し、短memory・small-inertia極を取ると

```math
\tau_U\dot U_e
=
-U_e+v_e+R_{U,e}
```

となる。

## AA.5 local tight-frame moving bath

$U(X)$ をHamiltonianへ直接momentum shiftとして書かず、tracerとlocal material frameの相対座標だけを結合する。compact-supportのpartition

```math
\chi_e(X)\ge0,
\qquad
\sum_e\chi_e(X)=1
```

を取り、advective channel $g_e=\chi_e$ と、重なるpair $e<f$ のstationary compensator

```math
g_{ef}
=
\sqrt{2\chi_e\chi_f}
```

を置く。すると

```math
\sum_e g_e^2+\sum_{e<f}g_{ef}^2=1.
```

各channel $c$ に $s_c'(X)=g_c(X)$ を取り、advective channelでは $\eta_e=Y_e$、compensatorでは $\eta_{ef}=0$ とする。

```math
H_{\rm drag}
=
\sum_{c,\mu}
\left[
\frac{p_{c\mu}^2}{2m_{c\mu}}
+
\frac{m_{c\mu}\omega_{c\mu}^2}{2}
\left[
q_{c\mu}
-
a_{c\mu}
\left(
s_c(X)-\eta_c
\right)
\right]^2
\right].
```

finite harmonic variablesを厳密に消去すると

```math
F_{\rm drag}^{(N)}(t)
=
\sum_cg_c(X_t)\xi_c^{(N)}(t)
-
\sum_cg_c(X_t)
\int_0^t
\Gamma_{c,N}(t-s)
\left[
g_c(X_s)V_s-\dot\eta_c(s)
\right]ds
+
R_{\rm slip}
```

を得る。条件付きcanonical preparationでは

```math
\left\langle
\xi_c^{(N)}(t)\xi_d^{(N)}(s)
\right\rangle
=
\delta_{cd}k_BT\Gamma_{c,N}(t-s).
```

short-memory、flow tracking、small recoilの極では

```math
F_{\rm drag}
=
-\gamma(V-U_X)+\xi_X+R_C,
\qquad
U_X=\sum_e\chi_eU_e,
```

```math
\left\langle
\xi_X(t)\xi_X(t')
\right\rangle
=
2\gamma k_BT\delta(t-t')
```

となる。

## AA.6 finite-time window

finite bathの代表memory timeを $\tau_{\rm mem}$、recurrence timeを $T_{\rm rec}$ とする。M67の基本動作窓は

```math
\max
\left(
\tau_{\rm mem},
\tau_U,
M_X/\gamma,
\tau_{\rho,\rm mix}
\right)
\ll
T_{\rm obs}
\ll
\min
\left(
T_{\rm rec},
T_{\rm back}
\right).
```

永久不可逆性は要求せず、固定有限観測時間のprethermal Hamiltonian windowを使う。

## AA.7 R208A：二実体finite-Hamiltonian parent

<!-- theorem-start:theorem -->
**定理（R208A：M67二実体finite-Hamiltonian parent）**

M37/R86 safe coherent sector、$K_e>M_e$、正の有限harmonic-bath parameterを取り、$r_X^\delta$ と $v_e$ が固定観測窓で有界とする。このときM67の全自由度は

```math
\mathcal R_{\rm str}
+
(X,P_X)
```

の二つの主要物理sectorへ分類でき、$H_{67}$ は有限古典Hamiltonianとして構成できる。$Z,\rho,j,U,\xi$ はすべてM67正準自由度から作る派生量であり、新しい独立実体を必要としない。
<!-- theorem-end:theorem -->

## AA.8 R208B：osmotic forceと有限backreaction

<!-- theorem-start:theorem -->
**定理（R208B：phase-volume osmotic forceと有限backreaction）**

M67 phase-volume sectorについて

```math
Z_\rho
=
Z_\rho^0
\frac{r_X^\delta}{r_*},
\qquad
F_\rho
=
-k_BT\log r_X^\delta+C_\rho,
```

従って

```math
\left\langle F_X^\rho\right\rangle
=
k_BT\partial_X\log r_X^\delta.
```

equal weightsではphase-volume force fluctuationは $O(N_\rho^{-1/2})$、coherent action $Z=\sqrt{N_0}z$ に対する固定有限時間のrelative state-direction backreactionは $O(N_0^{-1})$ である。
<!-- theorem-end:theorem -->

## AA.9 R208C：local moving finite bath

<!-- theorem-start:theorem -->
**定理（R208C：local finite bathのrelative Langevin縮約）**

AA.5のlocal tight frameと条件付きcanonical finite bath preparationを用いると、finite harmonic variablesの消去からmemory forceとfinite-bath FDTを厳密に得る。short-memory、flow tracking、small moving-frame recoilの極では

```math
F_{\rm drag}
=
-\gamma(V-U_X)+\xi_X+R_C,
```

```math
\left\langle
\xi_X(t)\xi_X(t')
\right\rangle
=
2\gamma k_BT\delta(t-t')
```

となる。smooth sectorでは

```math
U_X
=
v_\delta(X,t)
+
O(
\varepsilon_A+
\varepsilon_U+
\varepsilon_{\rm int}+
\varepsilon_Y
).
```

finite-memory error、finite-spectrum error、recurrenceはAA.6の時間窓で別々に管理する。
<!-- theorem-end:theorem -->

## AA.10 R208D：M64への有限時間縮約

<!-- theorem-start:theorem -->
**定理（R208D：M67からM64 Q3 lawへの有限時間縮約）**

R208A--R208Cの条件に加え、$\rho_\delta\ge\rho_{\delta,*}>0$、必要な微分の有界性、AA.6の時間尺度分離を仮定する。M67 tracerをfast reservoir sectorについて縮約し、$M_X/\gamma\to0$ のoverdamped極を取ると、

```math
dX_t
=
\left[
\frac{J_\delta}{\rho_\delta}
+
\nu\partial_X\log\rho_\delta
\right]dt
+
\sqrt{2\nu}\,dW_t
+
R_{208}(t),
\qquad
\nu=\frac{k_BT}{\gamma}
```

を得る。総残差はcoherent envelope、density interpolation、$O(N_\rho^{-1/2})$ force fluctuation、flow tracking、moving-frame recoil、finite-memory、finite-spectrum、overdamped、$O(N_0^{-1})$ signal backreactionを別々に管理する。

ideal limitではM64/R203Cを回収し、同じ $\rho_\delta,J_\delta$ をR203Dへ渡せるため、R161/R185およびR124/R182/R125接続は既存結果を再利用できる。
<!-- theorem-end:theorem -->

## AA.11 数値検証契約と未主張範囲

M67 candidateではHamiltonian drift、M37 ideal signalとの状態方向誤差、$U_X-v_\delta$、phase-volume mean force、finite-bath memory、tracer分布を同じparameter setで監査する。$N_0$、$N_\rho$、$K_U$、$\tau_U$、$\tau_{\rm mem}$、bath mode数、格子幅を独立に振り、一つの改善を複数誤差へ二重計数しない。

M67/R208を追加しただけではM64、M65、M66、M54を退役させない。Q3 fixed-goalの直接依存、A1/A2/B1--B3、M0の判定も変更しない。Q1/Q2/NBL特殊化は将来候補であり、H/T/CNOTの一般実装、NBL Born sampling、mixing/resource boundを本付録から推論しない。
