@number: Z
@chapter: 付録
@title: M63 topological reservoir一成分Hamiltonian lattice Q3統合候補
@status: M62/R201を置き換えるactive single-field strengthening candidate。一組の実格子正準変数からkink、Schrödinger型signal、局所reservoirを構成し、2-action shellを介さずreservoir phase-space Jacobianからosmotic free energyを得る。R202Cのpartition identityは解析核として閉じる一方、R202Bのfull envelope、R202Dのmicroscopic backreaction bound、R202Eのcurrent port・GLE/FDT、R202FのPN hopping--R161有限時間合成は未閉鎖とする。M61/M60の現行固定達成主線は置換しない。

## Z.1 M63の責務と存在論

M63は一格子点あたり一組の実正準変数

```math
(\phi_n,\pi_n),
\qquad
n\in\mathbb Z
```

だけを基本自由度とする時間非依存古典Hamiltonian latticeである。複素signal、kink中心、reservoir modeは独立した実体ではなく、同じ $(\phi_n,\pi_n)$ の固定線形またはcollective representationである。

M63の目標は、同じ一成分場からkink位置、signal density/current、local reservoirを取り出し、signalの局所規格化密度 $r$ に対する条件付きreservoir自由エネルギーから

```math
F_X^{\rm osm}
=
k_BT\,\partial_X\log r
```

を得ることである。M63では2-action shell、weighted-shell normal form、shell chemical potential、shell--reservoir exchangeを用いない。

## Z.2 2-site local canonical filter bank

隣接2サイトを一つのcellとして

```math
u_m
=
\frac{\phi_{2m}+\phi_{2m+1}}{\sqrt2},
\qquad
v_m
=
\frac{\phi_{2m}-\phi_{2m+1}}{\sqrt2},
```

```math
p_m
=
\frac{\pi_{2m}+\pi_{2m+1}}{\sqrt2},
\qquad
q_m
=
\frac{\pi_{2m}-\pi_{2m+1}}{\sqrt2}
```

と定める。これは固定線形正準変換であり、

```math
\{u_m,p_n\}=\delta_{mn},
\qquad
\{v_m,q_n\}=\delta_{mn}
```

を満たす。また

```math
\frac12(p_m^2+q_m^2)
=
\frac12(\pi_{2m}^2+\pi_{2m+1}^2)
```

である。$u$、$v$ は二つの物理場ではなく、一成分格子の局所canonical coordinatesである。$u$-branchをkinkとsignalに、$v$-branchをreservoirに用いる。

## Z.3 kink・signal branch

最小候補として

```math
H_A
=
\sum_m
\left[
\frac{p_m^2}{2}
+
U_K(u_m)
\right]
+
\frac{\kappa_A}{2}
\sum_m
(u_{m+1}-u_m)^2
```

とし、

```math
U_K(u)
=
\frac{\Omega_K^2}{8u_0^2}
(u^2-u_0^2)^2
```

のようなdouble wellを取る。真空 $u=\pm u_0$ を結ぶ離散kink $u_m^K(X)$ のcollective centerを粒子位置 $X$ とする。

真空まわりの線形branchは

```math
\omega_A^2(k)
=
\Omega_K^2
+
4\kappa_A\sin^2\frac{k}{2}
```

を持つ。このcontinuumの狭帯域packetをsignalとして用いる。

kink抽出用の固定low-passを $\bar u=F_Ku$、signal carrier抽出用の固定band-passを $Q^s=F_su$、$P^s=F_sp$ とする。存在証人では有限range FIR filterを許す。一サイト並進対称性を求める強化版では格子作用素の滑らかな関数または有限次数多項式近似を用いてよい。

<!-- theorem-start:theorem -->
**定理（R202A：一成分local filter-bankによるkink・signal・reservoir branch構成）**

適切な正のparameterと固定filterを選び、同一の一成分実格子上にstable kink sector、$u$-branch continuum内の狭帯域signal sector、$v$-branch reservoir sectorを同時に構成する。signalのkink low-passへの漏れを $\varepsilon_{KS}$、signal/reservoir branch混成を $\varepsilon_{SR}$ とし、固定有限時間safe sectorで所定値以下にできるparameter familyをR202Aの目標とする。
<!-- theorem-end:theorem -->

R202Aでは旧M62の2 shell modeや $3\omega_2<\omega_{\min}^{\rm cont}$ を要求しない。余分なkink shape modeがある場合はsignal/reservoir時間窓との共鳴を誤差として管理する。

## Z.4 same-field signal envelopeと規格化密度

carrier波数 $k_s$ の周囲で

```math
\omega_A(k)
=
\omega_s
+
v_g(k-k_s)
+
\frac12\omega_s''(k-k_s)^2
+
\cdots
```

と展開する。carrier phaseとgroup translationを除いたslow envelopeを $Z$ とする。

局所signal actionを

```math
\rho_m^s
=
\frac{
(P_m^s)^2+\omega_s^2(Q_m^s)^2
}{
2\omega_s
}
```

とする。準備境界から固定physical action scale $N_0>0$ を受け取り、Hamiltonian内部で現在の総作用を測って割らない。平滑kernel $K_r$ と正則化背景 $\delta\varpi_m>0$ を使い、

```math
r_m^\delta
=
\delta\varpi_m
+
\frac1{N_0}
\sum_\ell
K_r(m-\ell)\rho_\ell^s
```

とする。safe sectorで $0<r_{\min}\le r_m^\delta\le r_{\max}<\infty$ を仮定する。

<!-- theorem-start:theorem -->
**定理（R202B：same-field Schrödinger signal envelope・density/current）**

R202Aの狭帯域signal sectorについて、固定有限時間で

```math
i\mathcal J_0\partial_tZ
=
-\frac{\mathcal J_0^2}{2m_{\rm eff}}
\partial_x^2Z
+
V_{\rm eff}Z
+
R_{\rm env}
```

へ縮約し、

```math
\|Z_{\rm micro}(t)-Z_{\rm Sch}(t)\|
\le
\varepsilon_{\rm env}(T)
```

を得る。同じsignalから密度 $\rho$ とcurrent $j$ を導き、$\partial_t\rho+\partial_xj=O(\varepsilon_{\rm env})$ を満たす。prepared actionについて

```math
\left|
\frac{N_s(t)}{N_0}-1
\right|
\le
\varepsilon_N
```

を有限時間で要求する。Nelson matchingは $\mathcal J_0=2m_{\rm eff}\nu$ とする。
<!-- theorem-end:theorem -->

## Z.5 topological kink weight

左真空で0、右真空で1となる滑らかな単調関数 $s$ を固定し、$s(-u_0)=0$、$s(u_0)=1$ とする。kink weightを

```math
\boxed{
\gamma_m
=
s(\bar u_{m+1})
-
s(\bar u_m)
}
```

と定める。異種境界条件 $\bar u_{-\infty}=-u_0$、$\bar u_{+\infty}=u_0$ のtopological sectorではtelescopingにより

```math
\boxed{
\sum_m\gamma_m=1
}
```

が成り立つ。理想単調kinkでは $\gamma_m\ge0$ であり、kink core近傍に局在する。外部からkink中心を測ってwindowを動かす必要はない。

## Z.6 reservoir Hamiltonianとtopological scaling

基準reservoirを

```math
\mathcal H_R^0(c,q)
=
\sum_m
\left[
\frac{q_m^2}{2}
+
\frac{\Omega_R^2}{2}c_m^2
+
\frac{\beta_R}{4}c_m^4
\right]
+
\frac{\kappa_R}{2}
\sum_m
(c_{m+1}-c_m)^2
```

とする。$\Omega_R^2,\beta_R,\kappa_R>0$ とし、quartic termはreservoir内部mixingを得るための正の安定化非線形性として用いる。

reference density $r_*>0$ を固定し、

```math
\boxed{
\lambda_m
=
\left(
\frac{r_m^\delta}{r_*}
\right)^{-\gamma_m}
}
```

と置く。実reservoir Hamiltonianを

```math
\boxed{
H_R
=
\mathcal H_R^0(
c_m=\lambda_mv_m,
q_m
)
}
```

とする。具体的には

```math
\begin{aligned}
H_R
={}&
\sum_m\frac{q_m^2}{2}
+
\sum_m
\left[
\frac{\Omega_R^2}{2}(\lambda_mv_m)^2
+
\frac{\beta_R}{4}(\lambda_mv_m)^4
\right]
\\
&+
\frac{\kappa_R}{2}
\sum_m
(
\lambda_{m+1}v_{m+1}
-
\lambda_mv_m
)^2 .
\end{aligned}
```

$u,v,p,q,r^\delta,\gamma,\lambda$ はすべて固定式で $(\phi,\pi)$ から定まるので、$H_{63}^{\rm core}=H_A+H_R=H_{63}^{\rm core}(\phi,\pi)$ であり、独立自由度を追加しない。

## Z.7 R202C：topological reservoir-scaling partition identity

固定signal/kink configurationに対するreservoir partition functionを

```math
Z_R[r,\gamma]
=
\int
e^{-\beta H_R}
\prod_mdv_m\,dq_m
```

とする。$c_m=\lambda_mv_m$ と変数変換すると $dv_m=\lambda_m^{-1}dc_m$ なので、$Z_R=Z_R^0\prod_m\lambda_m^{-1}$ となる。

<!-- theorem-start:theorem -->
**定理（R202C：topological reservoir phase-volume identity）**

R202Aのsafe kink sectorで $\sum_m\gamma_m=1$ とする。このとき

```math
\boxed{
Z_R[r,\gamma]
=
Z_R^0
\exp
\left[
\sum_m\gamma_m
\log\frac{r_m^\delta}{r_*}
\right]
}
```

が厳密に成立し、条件付きreservoir自由エネルギーは

```math
\boxed{
F_R[r,\gamma]
=
-k_BT
\sum_m\gamma_m\log r_m^\delta
+
C_R
}
```

となる。
<!-- theorem-end:theorem -->

この恒等式はweak quartic expansion、normal form、chemical potential、wave-action prethermal conservationを必要としない。基準reservoir内部に安定なmode couplingを追加しても $H_R=\mathcal H_R^0(\lambda v,q)$ の形を保つ限り同じJacobian identityが成立する。

## Z.8 R202D：osmotic forceとsignal backreaction

kink weightの中心と二次幅を

```math
X_\gamma
=
\sum_mx_m\gamma_m,
\qquad
\sigma_K^2
=
\sum_m
(x_m-X_\gamma)^2\gamma_m
```

とする。signalがkink幅より滑らかなら、

```math
\sum_m
\gamma_m\log r_m^\delta
=
\log r^\delta(X_\gamma)
+
\frac{\sigma_K^2}{2}
\partial_x^2\log r^\delta(X_\gamma)
+
\cdots .
```

<!-- theorem-start:theorem -->
**定理（R202D：topological osmotic force・small-backreaction）**

R202A--R202Cのsafe sectorで $r^\delta\ge r_{\min}>0$ とし、signal densityがkink幅より滑らかであるとする。このときconditional-equilibrium mean forceは

```math
\boxed{
F_X^{\rm osm}
=
k_BT\partial_X\log r^\delta
+
O(
\varepsilon_{\rm width}
+
\varepsilon_{\rm filt}
+
\varepsilon_{\rm top}
)
}
```

となる。

また $r^\delta$ がprepared physical action $N_0$ で規格化されるため、reservoir scalingからsignalへ返るshape-changing variationは固定有限時間で

```math
\varepsilon_{\rm back}
\le
C_{\rm back}
\frac{k_BT T}{
\mathcal J_0N_0r_{\min}
}
+
O(N_0^{-1}M^{-1/2})
```

型に抑えることを目標とする。
<!-- theorem-end:theorem -->

physical signal振幅を $O(\sqrt{N_0})$、bare lattice nonlinear scaleを $v_0$ とすると $\sqrt{N_0}/v_0\ll1$ を要求する。例えば $v_0=N_0^{3/4}$ とすれば $N_0^{-1}\to0$ と $\sqrt{N_0}/v_0\to0$ を同時に取れる。これは存在parameter familyのscale witnessであり、full trajectory boundではない。

## Z.9 signal current port

R202C--R202Dはdensityからosmotic forceを生成する。Nelson current velocityには同じsignalから

```math
V^\delta
=
\frac{j}{
\rho+\delta N_0q
}
```

を得る必要がある。kinkが読む局所current velocityを $V_K=\sum_m\gamma_mV_m^\delta$ とする。smooth sectorでは $V_K=j/\rho+O(\varepsilon_{\rm width}+\varepsilon_{\rm env})$ となる。

$V_K$ を実際のkink transportへ渡すbounded same-field Hamiltonian couplingをcurrent portと呼ぶ。$V_K$ またはLagrangian frameを解析上定義するだけではcurrent portを構成したことにしない。

## Z.10 R202E：reservoir dynamics・GLE/FDT

R202Cはfixed conditional configurationのstatic partition identityである。実時間trajectoryがこの自由エネルギーを追従するにはreservoir mixingとslow-variable separationが必要である。

<!-- theorem-start:theorem -->
**定理（R202E：same-field current port・local reservoir GLE/FDT）**

同じM63 reservoirが有限mixing時間 $\tau_{\rm mix}$ と有限memory時間 $\tau_{\rm mem}$ を持ち、current portが

```math
V_K
=
\frac j\rho
+
O(\varepsilon_{\rm cur})
```

をkink transportへ渡すとする。このときkink collective coordinateを

```math
\begin{aligned}
M_X\ddot X
={}&
-\partial_XU_{\rm PN}
+
k_BT\partial_X\log r^\delta
\\
&-
\int_0^t
\Gamma(t-s)
[
\dot X(s)-V_K(s)
]ds
+
\xi(t)
+
R_{202E}
\end{aligned}
```

型のGLEへ有限時間縮約することをR202Eの目標とする。条件付き平衡下で

```math
\langle\xi(t)\rangle=0,
\qquad
\langle\xi(t)\xi(s)\rangle
=
k_BT\Gamma(|t-s|)
```

を要求する。
<!-- theorem-end:theorem -->

$\tau_{\rm mem}$ がslow時間より十分短ければlocal frictionへ縮約し、Einstein relation $\nu=k_BT/\gamma_X$ とoverdamped極から

```math
dX_t
=
\left[
\frac j\rho
+
\nu\partial_X\log r^\delta
\right]dt
+
\sqrt{2\nu}\,dW_t
+
O(\varepsilon_{\rm od})
```

を得る。正則化極で $r^\delta\to\rho/N_0$ ならosmotic termは $\nu\partial_X\log\rho$ へ収束する。

R202Eは現時点で未閉鎖であり、current portを具体Hamiltonianとして固定し、full reservoir trajectoryからmixing、memory、FDTを検証する必要がある。

## Z.11 R202F：PN hoppingからR161/R185への合成

離散kink中心は自然なPeierls--Nabarro周期ポテンシャル $U_{\rm PN}(X)$ を持つ。そのminimaを $x_i$ とし、intra-well relaxationがescapeより速いregimeでwell index過程へ粗視化する。

<!-- theorem-start:theorem -->
**定理（R202F：M63からR161位置経路・R185への有限時間合成）**

R202A--R202Eを同じparameter familyで満たし、

```math
\tau_{\rm mix},
\tau_{\rm mem},
\tau_{\rm well}
\ll
\tau_{\rm hop},
\tau_r,
\qquad
T_{\rm obs}<T_{\rm env}
```

となる非空の観測時間窓を取れるとする。PN well-index過程のgenerator $k_{i\to j}^{63}$ について

```math
\sup_{t\le T}
\max_i
\sum_{j\ne i}
\left|
k_{i\to j}^{63}(t)
-
k_{i\to j}^{161}(t)
\right|
\le
\varepsilon_{\rm tr}^{63}
```

を満たすparameter familyを構成することをR202Fの目標とする。この接続が閉じれば、同じ前向き経路法則のBayes反転から後退率、$D_\pm$、時間対称Newton則を得る既存R185を再利用する。
<!-- theorem-end:theorem -->

## Z.12 誤差責務と現行主線との境界

M63候補の誤差は

```math
\begin{aligned}
\varepsilon_{\rm tr}^{63}
\le C_{63}(&
\varepsilon_{\rm env}
+\varepsilon_{KS}
+\varepsilon_{SR}
+\varepsilon_{\rm filt}
+\varepsilon_N
+\varepsilon_{\rm top}
\\
&
+\varepsilon_{\rm width}
+\varepsilon_{\rm back}
+\varepsilon_{\rm eq}
+\varepsilon_{\rm cur}
+\varepsilon_{\rm mem}
\\
&
+\varepsilon_{\rm od}
+\varepsilon_{\rm PN}
+\varepsilon_{\rm EK}
+a_X^2)
\end{aligned}
```

と整理する。同じ上流偏差を複数項へ重複加算しない。旧M62のnormal-form remainder、shell--reservoir exchange時間、prethermal shell-action lifetimeはM63へ持ち込まない。

M63/R202はM62/R201をactive single-field candidateとして置き換えるが、M61/R200--M60/R198/R199/R196の現行固定達成主線はまだ置換しない。固定Q3-1/Q3-2の達成ラベル、Q3-1-A1/Q3-2-A1の部分達成、Q3-1-A2/Q3-2-A2の未監査は変更しない。

M63を現行Q3ミクロ主線へ昇格させるには、少なくともR202A/R202Bの同一parameter branch witness、R202Dのfull trajectory osmotic forceと $N_0^{-1}$ backreaction scaling、R202Eのbounded current port・reservoir mixing・memory・FDT、R202FのPN hopping--R161有限誤差接続、およびそれらを同時に満たす共通時間窓を閉じる必要がある。R202Cのpartition identityはこの動的closureとは独立した解析核として保持する。
