@number: AD
@chapter: 付録
@title: R215 compatible score と空間情報勾配自由エネルギー
@status: R215A--R215CをM67/R214 continuous-tracer lineのcandidate strengtheningとする。R215CはR215Bのspatial-information gradient free energyをmediumのreversible constitutive closureとして採用したときのenergy balance、local stress、Madelung closure、Schrödinger representationを与える。R214A/Bのrequired状態、Q3 fixed-goal達成、A1/A2、M37/R86、M64/R203、R161/R185の運用状態は変更しない。M68 finite-Hamiltonian parent、$M_X=m$ / $\mathcal J_{\rm SI}=\mathcal J_0$ matching、M37退役は本付録の主張に含めない。

## AD.1 目的と責務境界

付録AC/R214A--R214Bはgeneric nonnegative scalar port $\varrho$ とflow port $U$ を受け、node-safe weight
```math
w(x,t)=\varrho(x,t)+\varrho_T>0
```
から
```math
dX_t=
\left[
U(X_t,t)+\nu\partial_x\log w(X_t,t)
\right]dt
+
\sqrt{2\nu}\circ dW_t,
\qquad
\nu=\frac{k_BT}{\gamma_X}
```
というreference port diffusionを回収する。有限相関GLEからwhite-noise極限を取る物理的基本表現はStratonovichとし、constant-mobility leading sectorではnoiseが加法的なのでCartesian Itô表示と一致する。

本付録では、R214Aのcanonical potential of mean force
```math
F_{\rm db}(X)\simeq-k_BT\log w(X)
```
と、R215Bで定義する
```math
\mathcal F_{\rm SI}[\pi]
```
を区別する。前者はdumbbell内部phase volumeを消去した局所mean force、後者はR215Aのscoreに対応する空間情報の勾配functionalである。

またR215Bで使う $M_X$ はR214 dumbbell重心の実慣性質量であり、M37/R185のSchrödinger表示に現れる設計質量 $m$ と同一視しない。

## AD.2 projectively compatible density/flow port

固定有限時間 $0\le t\le T$、1次元周期領域
```math
\Omega=\mathbb T_\ell
```
を考える。$w\in C^{1,2}$ は
```math
w(x,t)\ge w_*>0
```
を満たし、$U$ はboundedかつ空間Lipschitzとする。

```math
Z(t)=\int_\Omega w(x,t)\,dx,
\qquad
\pi(x,t)=\frac{w(x,t)}{Z(t)}
```
と定義する。

<!-- theorem-start:lemma -->
**補題（projective compatibility）**

ある時間だけのscalar $\lambda(t)$ が存在して
```math
\partial_t w+\partial_x(wU)=\lambda(t)w
```
が成立するとする。周期境界では
```math
\lambda(t)=\frac{\dot Z(t)}{Z(t)}
```
であり、規格化densityは
```math
\boxed{
\partial_t\pi+\partial_x(\pi U)=0
}
```
を満たす。

逆に、規格化density $\pi$ がこのcontinuity lawを満たすなら、任意の正の $Z(t)$ に対して $w=Z(t)\pi$ はprojective compatibilityを満たす。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明（projective compatibility）**

周期境界により
```math
\dot Z
=
\int_\Omega\partial_t w\,dx
=
\lambda Z.
```
従って
```math
\partial_t\pi
=
\frac{\partial_t w}{Z}
-\frac{\dot Z}{Z}\pi
=
-\frac{\partial_x(wU)}{Z}
=
-\partial_x(\pi U).
```
逆向きは $w=Z\pi$ を直接微分すればよい。証明終。
<!-- theorem-end:proof -->

従って
```math
w\mapsto c(t)w,\qquad c(t)>0
```
というglobal amplitudeの変更は同じ $\pi$ と同じscore
```math
\partial_x\log w=\partial_x\log\pi
```
を表す。

## AD.3 R215A：compatible-port equivariance / Bayes score

R214Bのreference port diffusionを
```math
dX_t
=
b_+(X_t,t)dt
+
\sqrt{2\nu}\circ dW_t,
```
```math
b_+
=
U+\nu\partial_x\log w
=
U+\nu\partial_x\log\pi
```
とする。noise amplitudeは定数なので、Fokker--PlanckとBayes条件付き率の計算だけItô表示へ移してもdrift補正は0である。

<!-- theorem-start:theorem -->
**定理（R215A：compatible-port equivariance / Bayes score）**

AD.2のprojective compatibility、$w\ge w_*>0$、bounded spatial-Lipschitz $U$、constant $\nu>0$ を仮定する。上のR214 reference port diffusionを
```math
\mathcal L(X_0)=\pi_0
```
から開始すると
```math
\boxed{
\mathcal L(X_t)=\pi_t
\qquad
(0\le t\le T)
}
```
が成立する。

さらに同じ共同path lawのBayes backward mean drift $b_-$ は
```math
\boxed{
b_-=U-\nu\partial_x\log\pi
}
```
であり、
```math
\boxed{
b_\pm=U\pm u,
\qquad
u:=\nu\partial_x\log\pi
}
```
を得る。従って
```math
\boxed{
\frac{b_++b_-}{2}=U,
\qquad
\frac{b_+-b_-}{2}=u.
}
```

$b_-$ は未来から作用する第二bathを表さず、同じ前向きpath lawをBayes条件付き確率で逆向きにfactorizeしたmean driftである。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215A）**

forward density $p$ のFokker--Planck方程式は
```math
\partial_t p
=
-\partial_x
\left[
\left(
U+\nu\partial_x\log\pi
\right)p
\right]
+
\nu\partial_x^2p.
```
$p=\pi$ を代入すると
```math
-\nu\partial_x
\left(
\pi\partial_x\log\pi
\right)
+
\nu\partial_x^2\pi
=
0
```
なので、AD.2の
```math
\partial_t\pi=-\partial_x(\pi U)
```
と一致する。parabolic initial-value problemの一意性から $p_t=\pi_t$。

constant diffusion $2\nu$ の同じpath lawについてBayes time reversalは
```math
b_-
=
b_+-2\nu\partial_x\log p.
```
$p=\pi$ とforward driftを代入すれば主張を得る。証明終。
<!-- theorem-end:proof -->

forward/backward generatorsを
```math
D_+
=
\partial_t
+
(U+u)\partial_x
+
\nu\partial_x^2,
```
```math
D_-
=
\partial_t
+
(U-u)\partial_x
-
\nu\partial_x^2
```
と書けば
```math
D_+X=U+u,
\qquad
D_-X=U-u.
```
本付録では
```math
\frac12(D_+D_-+D_-D_+)X
```
を力へ等置しない。時間対称Newton則はR185の責務である。

### AD.3.1 R214B finite-Hamiltonian corollary

R214Bはactual finite-bath dumbbell $X_t^{\rm db}$ とreference port diffusion $X_t^{\rm port}$ に
```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{\rm db}),
\mathcal L(X_t^{\rm port})
\right)
\le
\varepsilon_{214}^{\rm port}(T)
```
を与える。

portがR215A compatibleで
```math
\mathcal L(X_0^{\rm port})=\pi_0
```
なら
```math
\boxed{
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{\rm db}),
\pi_t
\right)
\le
\varepsilon_{214}^{\rm port}(T).
}
```

この $W_1$ closenessだけから
```math
\nabla\log p_t
\simeq
\nabla\log\pi_t
```
は従わない。従ってactual dumbbellのfinite-error backward score theoremは本結果に含めない。

### AD.3.2 current M37/M64 specialization

現行M64/R185 regularized density
```math
\rho_\delta
=
\frac{\rho+\delta q_0}{1+\delta},
\qquad
q_0=\frac1\ell
```
を考える。正の定数 $C$ に対してideal compatible portを
```math
\varrho^\circ=C\rho,
\qquad
\varrho_T=C\delta q_0,
\qquad
w^\circ=C(\rho+\delta q_0)
```
と選べば
```math
\pi^\circ
=
\frac{w^\circ}{\int w^\circ dx}
=
\rho_\delta,
```
```math
\partial_x\log w^\circ
=
\partial_x\log\rho_\delta.
```
さらに
```math
U^\circ=v_\delta
```
とすればM64 continuityからR215A compatibilityが成立し、
```math
b_\pm^\circ
=
v_\delta
\pm
\nu\partial_x\log\rho_\delta
```
を得る。actual R214 scalar/flow portとの差は付録AC.7.2の
```math
\varepsilon_\varrho,\varepsilon_U
```
とscore/drift stability ledgerへ渡す。

## AD.4 R215B：spatial-information free-energy identities

R215Aのcompatible density $\pi$ とscore velocity
```math
u=\nu\partial_x\log\pi
```
を使う。

<!-- theorem-start:theorem -->
**定理（R215B：spatial-information free-energy identities）**

R214 dumbbell重心の有限慣性質量を $M_X>0$ とする。spatial-information gradient free energyを
```math
\boxed{
\mathcal F_{\rm SI}[\pi]
:=
\frac{M_X}{2}
\int_\Omega
\pi(x)|u(x)|^2dx
}
```
と定義する。

Fisher information
```math
I_F[\pi]
:=
\int_\Omega
\pi|\partial_x\log\pi|^2dx
=
\int_\Omega
\frac{|\partial_x\pi|^2}{\pi}dx
```
に対して
```math
\boxed{
\mathcal F_{\rm SI}
=
\frac{M_X\nu^2}{2}I_F[\pi]
=
2M_X\nu^2
\int_\Omega
|\partial_x\sqrt\pi|^2dx.
}
```

さらに
```math
\tau_v:=\frac{M_X}{\gamma_X},
\qquad
\ell_v^2:=\nu\tau_v,
\qquad
\mathcal J_{\rm SI}:=2M_X\nu=2k_BT\tau_v
```
と置けば
```math
\boxed{
\mathcal F_{\rm SI}
=
\frac{k_BT}{2}\ell_v^2I_F[\pi]
=
\frac{\mathcal J_{\rm SI}^2}{8M_X}I_F[\pi].
}
```

未規格化port $w=Z\pi$ では
```math
\boxed{
\mathcal F_{\rm SI}[w]
=
\frac{M_X\nu^2}{2Z}
\int_\Omega
\frac{|\partial_xw|^2}{w}dx,
}
```
従って任意の $c(t)>0$ に対して
```math
\mathcal F_{\rm SI}[cw]
=
\mathcal F_{\rm SI}[w].
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215B）**

$u=\nu\partial_x\log\pi$ を定義へ代入すればFisher identityを得る。
```math
\frac{|\partial_x\pi|^2}{\pi}
=
4|\partial_x\sqrt\pi|^2
```
でDirichlet表示が従う。FDT
```math
\nu=\frac{k_BT}{\gamma_X}
```
と $\tau_v=M_X/\gamma_X$ を使えば
```math
M_X\nu=k_BT\tau_v,
\qquad
\mathcal J_{\rm SI}=2M_X\nu
```
なので残りの係数表示を得る。$w=Z\pi$ では $Z$ が空間一定なのでprojective invarianceも従う。証明終。
<!-- theorem-end:proof -->

$\mathcal F_{\rm SI}$ は微視的瞬間運動エネルギー
```math
E\left[\frac{M_X}{2}V^2\mid X\right]
```
と同一視しない。R215Aで現れるforward/backward scoreが担う空間識別情報へ、R214/FDTの同じ $M_X,\gamma_X,T$ からエネルギー次元を与えるcandidate constitutive quantityである。

### AD.4.1 補助heat flowによるrelative-entropy dissipation

実時間 $t$ とは別の補助parameter $s$ に対して
```math
\partial_s\pi_s
=
\nu\partial_x^2\pi_s,
\qquad
\pi_{s=0}=\pi
```
を考える。periodic uniform density $q_0=1/\ell$ に対し
```math
\mathcal D[\pi_s]
=
D_{\rm KL}(\pi_s\Vert q_0)
=
\int\pi_s\log\frac{\pi_s}{q_0}dx
```
とすると、積分部分積分から
```math
\boxed{
\frac{d}{ds}\mathcal D[\pi_s]
=
-\nu I_F[\pi_s].
}
```
従って
```math
\boxed{
\mathcal F_{\rm SI}[\pi]
=
-\frac{\tau_v}{2}
\left.
\frac{d}{ds}
\left[
k_BT
D_{\rm KL}(\pi_s\Vert q_0)
\right]
\right|_{s=0}.
}
```
これはR214実時間dynamicsに新しいentropy production lawを課す式ではなく、現在のdensity形状に付随するFisher functionalのheat-flow characterizationである。

### AD.4.2 score-ON / current-only path-space KL

同じ初期分布と同じconstant noiseを持つ二つのpath lawを
```math
P_{\rm score}:
\quad
dX_t=(U+u)dt+\sqrt{2\nu}\,dW_t,
```
```math
P_{\rm cur}:
\quad
dX_t=Udt+\sqrt{2\nu}\,dW_t
```
とする。Novikov条件が成立するsafe sectorではGirsanov公式から
```math
D_{\rm KL}
\left(
P_{\rm score}^{[0,T]}
\Vert
P_{\rm cur}^{[0,T]}
\right)
=
\frac1{4\nu}
E_{P_{\rm score}}
\int_0^T
|u(X_t,t)|^2dt.
```
R215Aのequivarianceを使えば
```math
\boxed{
\int_0^T
\mathcal F_{\rm SI}[\pi_t]dt
=
\mathcal J_{\rm SI}
D_{\rm KL}
\left(
P_{\rm score}^{[0,T]}
\Vert
P_{\rm cur}^{[0,T]}
\right).
}
```
$P_{\rm cur}$ 自身が $\pi_t$ をmarginalとして持つことは要求しない。期待値は $P_{\rm score}$ 側で評価する。

### AD.4.3 微小translation識別率

```math
\pi_\epsilon(x)=\pi(x-\epsilon)
```
とすると、periodic smooth positive densityについて
```math
\boxed{
D_{\rm KL}(\pi\Vert\pi_\epsilon)
=
\frac{\epsilon^2}{2}I_F[\pi]
+
O(\epsilon^3).
}
```
従ってFisher情報は空間translationに対するlocal statistical distinguishabilityの曲率である。

### AD.4.4 node-safe regularization

現行R185と同じ一様背景
```math
\pi_\delta
=
\frac{\rho+\delta q_0}{1+\delta},
\qquad
q_0=\frac1\ell
```
について
```math
\boxed{
I_F[\pi_\delta]
=
\frac1{1+\delta}
\int_\Omega
\frac{|\partial_x\rho|^2}
{\rho+\delta q_0}dx
\le
I_F[\rho].
}
```
node-safe offsetはFisher情報をregularizeする。node-free $\rho\ge\rho_*>0$ のsmooth sectorでは
```math
I_F[\pi_\delta]
=
I_F[\rho]+O(\delta).
```

### AD.4.5 port/score stabilityからfree-energy stability

二つのpositive normalized densities $\pi,\pi^\circ$ に
```math
s=\partial_x\log\pi,
\qquad
s^\circ=\partial_x\log\pi^\circ
```
と置く。単純な分解から
```math
\left|
I_F[\pi]-I_F[\pi^\circ]
\right|
\le
\|\pi-\pi^\circ\|_{L^1}
\|s\|_\infty^2
+
\|s-s^\circ\|_\infty
\left(
\|s\|_\infty+\|s^\circ\|_\infty
\right).
```
従って付録AC.7.2のport $C^1$ stabilityからscore stabilityを経由して
```math
|\mathcal F_{\rm SI}[\pi]-\mathcal F_{\rm SI}[\pi^\circ]|
```
を制御できる。

## AD.5 functional derivativeとR215C入力

規格化制約 $\int\pi dx=1$ の下で
```math
\mathcal F_{\rm SI}
=
2M_X\nu^2
\int|\partial_x\sqrt\pi|^2dx
```
を変分すると
```math
\boxed{
\frac{\delta\mathcal F_{\rm SI}}{\delta\pi}
=
-2M_X\nu^2
\frac{\partial_x^2\sqrt\pi}{\sqrt\pi}
+
C(t),
}
```
ここで $C(t)$ は規格化constraintによる空間一定項である。

R215Cでは
```math
-\pi\partial_x
\frac{\delta\mathcal F_{\rm SI}}{\delta\pi}
```
をmediumのreversible constitutive force densityとして採用する。ただしこれはR215Bからの数学的恒等式ではなく、R215Cで新たに置くcandidate constitutive assumptionである。有限Hamiltonian coarse grainingがこのclosureを選ぶことのミクロ導出はM68へ残す。

また
```math
\mathcal J_{\rm SI}=2M_X\nu
```
をM37/R185の
```math
\mathcal J_0=2m\nu
```
と同一視しない。固定 $T,\gamma_X$ でstrict $M_X\to0$ を取れば
```math
\tau_v,\mathcal J_{\rm SI},\mathcal F_{\rm SI}\to0
```
なので、R215Bは
```math
\tau_{\rm bath}\ll\tau_v\ll\tau_{\rm slow}
```
を満たす有限だが短い慣性時間を持つphysical ancestorのcandidate information free energyとして扱う。

## AD.6 R215C：可逆information-free-energy closure

R215CではR215Bのspatial-information gradient free energyをmediumのreversible constitutive free energyとして採用する。ここで新しい物理自由度や独立係数は追加しない。

以下では
```math
\Omega=\mathbb T_\ell,
\qquad
\pi(x,t)>0,
\qquad
\int_\Omega\pi\,dx=1,
```
を仮定し、constant-mobility leading sector
```math
M_X>0,
\qquad
\nu=\frac{k_BT}{\gamma_X}>0
```
を固定する。pointwiseなlocal-stress表示まで使う節では
```math
R:=\sqrt\pi
```
が時間に1階、空間に3階まで滑らかであるsmooth positive sectorを仮定する。有限慣性ancestorの時間窓は
```math
\tau_{\rm bath}\ll\tau_v:=\frac{M_X}{\gamma_X}\ll\tau_{\rm slow}
```
とし、strict $M_X\to0$ は取らない。

R215Bのfunctional derivativeから空間一定のconstraint項を除いて
```math
\mu_{\rm SI}
:=
-2M_X\nu^2
\frac{\partial_x^2\sqrt\pi}{\sqrt\pi}
```
と置く。

R215Cのconstitutive assumptionは
```math
\boxed{
M_X
\left(
\partial_tU+U\partial_xU
\right)
=
-\partial_xV
-\partial_x\mu_{\rm SI}
}
```
である。$F_{\rm db}\simeq-k_BT\log w$ はR214 tracer側のscore portを作る局所potential of mean forceであり、medium energyへ重ねて加えない。

### AD.6.1 可逆closureとenergy balance

<!-- theorem-start:theorem -->
**定理（R215C：reversible information-free-energy closure）**

continuity
```math
\partial_t\pi+\partial_x(\pi U)=0
```
と上のconstitutive closureを満たすsmooth positive solutionについて
```math
\mathcal E_{\rm SI}
:=
\int_\Omega
\left[
\frac{M_X}{2}\pi U^2
+
V\pi
\right]dx
+
\mathcal F_{\rm SI}[\pi]
```
と置くと
```math
\boxed{
\frac{d\mathcal E_{\rm SI}}{dt}
=
\int_\Omega
\pi\,\partial_tV\,dx
}
```
が成立する。従ってstatic $V$ では
```math
\boxed{
\frac{d\mathcal E_{\rm SI}}{dt}=0.
}
```
またtime-evenなstatic $V$ のもとで
```math
t\mapsto-t,
\qquad
U\mapsto-U,
\qquad
\pi\mapsto\pi
```
に対してcontinuityとclosureは不変である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215C energy balance）**

continuityと周期境界から
```math
\frac{d}{dt}
\int_\Omega
\frac{M_X}{2}\pi U^2dx
=
\int_\Omega
\pi U
M_X
\left(
\partial_tU+U\partial_xU
\right)dx.
```
closureを代入して
```math
=
-\int_\Omega
\pi U
\left(
\partial_xV+\partial_x\mu_{\rm SI}
\right)dx.
```
一方
```math
\frac{d}{dt}
\int_\Omega V\pi dx
=
\int_\Omega
\pi U\,\partial_xV\,dx
+
\int_\Omega
\pi\,\partial_tV\,dx,
```
およびR215Bの変分公式から
```math
\frac{d\mathcal F_{\rm SI}}{dt}
=
\int_\Omega
\mu_{\rm SI}\partial_t\pi\,dx
=
\int_\Omega
\pi U\,\partial_x\mu_{\rm SI}\,dx.
```
三式を加えれば主張を得る。時間反転不変性は各項を直接変換すれば従う。証明終。
<!-- theorem-end:proof -->

### AD.6.2 局所information stress

<!-- theorem-start:lemma -->
**補題（R215C local information stress）**

```math
f_{\rm SI}
:=
-\pi\partial_x\mu_{\rm SI}
```
はlocal stressの発散
```math
\boxed{
f_{\rm SI}
=
\partial_x\sigma_{\rm SI}
}
```
と書ける。具体的に
```math
\boxed{
\sigma_{\rm SI}
=
2M_X\nu^2
\left[
R\partial_x^2R-(\partial_xR)^2
\right]
=
M_X\nu^2
\left[
\partial_x^2\pi
-
\frac{(\partial_x\pi)^2}{\pi}
\right].
}
```
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明（local information stress）**

```math
f_{\rm SI}
=
2M_X\nu^2
R^2
\partial_x
\left(
\frac{\partial_x^2R}{R}
\right)
=
2M_X\nu^2
\left(
R\partial_x^3R
-
\partial_xR\,\partial_x^2R
\right).
```
一方
```math
\partial_x
\left[
R\partial_x^2R-(\partial_xR)^2
\right]
=
R\partial_x^3R
-
\partial_xR\,\partial_x^2R.
```
従って第一表示を得る。$\pi=R^2$ を展開すれば第二表示を得る。証明終。
<!-- theorem-end:proof -->

したがってlocal momentum balanceは
```math
\boxed{
\partial_t(M_X\pi U)
+
\partial_x
\left(
M_X\pi U^2-\sigma_{\rm SI}
\right)
=
-\pi\partial_xV.
}
```

### AD.6.3 Madelung closure

zero-circulation sector
```math
\oint_\Omega U\,dx=0
```
では周期的なreal phase $S$ を
```math
\boxed{
\partial_xS=M_XU
}
```
で取れる。

<!-- theorem-start:theorem -->
**定理（R215C Madelung closure）**

zero-circulation smooth sectorではR215C closureは
```math
\boxed{
\partial_t\pi
+
\partial_x
\left(
\pi\frac{\partial_xS}{M_X}
\right)
=
0
}
```
と
```math
\boxed{
\partial_tS
+
\frac{(\partial_xS)^2}{2M_X}
+
V
-
2M_X\nu^2
\frac{\partial_x^2\sqrt\pi}{\sqrt\pi}
=
0
}
```
に同値である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（Madelung closure）**

$\partial_xS=M_XU$ をconstitutive closureへ入れると
```math
\partial_x
\left[
\partial_tS
+
\frac{(\partial_xS)^2}{2M_X}
+
V
+
\mu_{\rm SI}
\right]
=
0.
```
従って角括弧は空間一定の $C_S(t)$ に等しい。$S\mapsto S-\int^t C_S(s)ds$ というglobal time-dependent gaugeでこれを0へ吸収し、$\mu_{\rm SI}$ を代入すれば主張を得る。continuityは$\partial_xS=M_XU$ の直接代入である。証明終。
<!-- theorem-end:proof -->

同じ系はcoarse-grained field Hamiltonian
```math
\boxed{
\mathcal H_{215C}[\pi,S]
=
\int_\Omega
\left[
\frac{\pi(\partial_xS)^2}{2M_X}
+
V\pi
\right]dx
+
\mathcal F_{\rm SI}[\pi]
}
```
に対する
```math
\partial_t\pi
=
\frac{\delta\mathcal H_{215C}}{\delta S},
\qquad
\partial_tS
=
-\frac{\delta\mathcal H_{215C}}{\delta\pi}
```
としても書ける。これはmicroscopic finite-Hamiltonian parentの導出ではなく、R215C constitutive closureが可逆なHamiltonian field structureを持つという結果である。

### AD.6.4 Schrödinger representation

R215Bの
```math
\mathcal J_{\rm SI}=2M_X\nu
```
を使い
```math
\boxed{
\Psi_{\rm SI}
=
\sqrt\pi
\exp
\left(
\frac{iS}{\mathcal J_{\rm SI}}
\right)
}
```
と定義する。

<!-- theorem-start:theorem -->
**定理（R215C Schrödinger representation）**

AD.6.3のzero-circulation Madelung solutionは
```math
\boxed{
i\mathcal J_{\rm SI}
\partial_t\Psi_{\rm SI}
=
\left[
-\frac{\mathcal J_{\rm SI}^2}{2M_X}
\partial_x^2
+
V
\right]
\Psi_{\rm SI}
}
```
を満たす。逆にnode-freeなこのSchrödinger equationのsolutionから$\pi=|\Psi_{\rm SI}|^2$とphase $S$ を取ればAD.6.3を回収する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（Schrödinger representation）**

$R=\sqrt\pi$、$\mathcal J=\mathcal J_{\rm SI}$ と略記する。
```math
\partial_t\Psi
=
e^{iS/\mathcal J}
\left[
\partial_tR
+
\frac{i}{\mathcal J}R\partial_tS
\right],
```
```math
\partial_x^2\Psi
=
e^{iS/\mathcal J}
\left[
\partial_x^2R
+
\frac{2i}{\mathcal J}\partial_xR\,\partial_xS
+
\frac{i}{\mathcal J}R\partial_x^2S
-
\frac{1}{\mathcal J^2}R(\partial_xS)^2
\right].
```
Schrödinger equationの虚部はcontinuity、実部は
```math
\partial_tS
+
\frac{(\partial_xS)^2}{2M_X}
+
V
-
\frac{\mathcal J_{\rm SI}^2}{2M_X}
\frac{\partial_x^2R}{R}
=
0
```
である。$\mathcal J_{\rm SI}=2M_X\nu$ から
```math
\frac{\mathcal J_{\rm SI}^2}{2M_X}
=
2M_X\nu^2
```
なのでAD.6.3と一致する。逆向きも同じ計算を逆に読めばよい。証明終。
<!-- theorem-end:proof -->

### AD.6.5 torus circulation boundary

一般のperiodic velocity fieldでは
```math
\Delta S
:=
S(x+\ell)-S(x)
=
M_X\oint_\Omega U\,dx
```
が非零でもよい。このとき
```math
\Psi_{\rm SI}(x+\ell)
=
e^{i\Theta}
\Psi_{\rm SI}(x),
\qquad
\Theta
=
\frac{M_X}{\mathcal J_{\rm SI}}
\oint_\Omega U\,dx
```
というtwisted sectorを得る。static periodic $V$ とR215C closureでは
```math
\frac{d}{dt}
\oint_\Omega U\,dx=0
```
なのでcirculation sectorは保存される。

periodic single-valued $\Psi_{\rm SI}$ に必要な
```math
M_X\oint_\Omega U\,dx
=
2\pi n\mathcal J_{\rm SI}
```
はR215Cから導かない。この位相量子化はQ3-6の未達課題として維持する。

### AD.6.6 責務境界

R215Cが証明する因果鎖は、

R215B spatial-information free energy -> reversible constitutive closure（candidate assumption）-> energy balance / local stress -> Madelung closure -> Schrödinger representation

である。

以下はR215Cの主張に含めない。

- finite-Hamiltonian coarse grainingからconstitutive closure自体を導くこと
- variable mobility $\gamma_X+\zeta_{\rm db}(x)$ を含むexact Schrödinger representation
- $M_X=m$ のmatching
- $\mathcal J_{\rm SI}=\mathcal J_0$ のmatching
- M68 finite-Hamiltonian joint medium/tracer parent
- M37/R86の置換または退役
- Q3-6のcirculation quantization

## AD.7 status

- R215AはR214 generic portのうちprojectively compatibleなdensity/flow pairについて、equivarianceと同じpath lawのBayes score decompositionを与えるcandidate exact kinematic resultである。
- R215BはR215A scoreからspatial-information gradient free energyを定義し、Fisher、heat-flow relative entropy、path KL、translation distinguishabilityとの恒等式を与えるcandidate information-theoretic resultである。
- R215CはR215Bのfree energyをmediumのreversible constitutive free energyとして採用するcandidate closureであり、energy balance、local stress、zero-circulation Madelung closure、Schrödinger representationを厳密に与える。
- R214A/Bのrequired状態とcurrent M37/M64 specializationは変更しない。
- Q3-1/Q3-2 fixed-goal達成、Q3-1-A1/Q3-2-A1、A2、R161/R185の運用状態を変更しない。
- M68、finite-Hamiltonian closure origin、$M_X=m$ / $\mathcal J_{\rm SI}=\mathcal J_0$ matching、M37退役は本付録に含めない。
