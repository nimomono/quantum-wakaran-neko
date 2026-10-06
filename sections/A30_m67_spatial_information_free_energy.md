@number: AD
@chapter: 付録
@title: R215 compatible score と空間情報勾配自由エネルギー
@status: R215A--R215BをM67/R214 continuous-tracer lineのcandidate strengtheningとする。R214A/Bのrequired状態、Q3 fixed-goal達成、A1/A2、M37/R86、M64/R203、R161/R185の運用状態は変更しない。R215Cのmedium reversible closure、M68、Schrödinger再導出は本付録の主張に含めない。

## AD.1 目的と責務境界

付録AC/R214A--R214Bは、generic nonnegative scalar port (arrho) とflow port (U) を受け、
node-safe weight
[
w(x,t)=arrho(x,t)+arrho_T>0
]
から
[
dX_t=
left[
U(X_t,t)+
upartial_xlog w(X_t,t)
ight]dt
+sqrt{2
u}circ dW_t,
qquad

u=rac{k_BT}{gamma_X}
]
というreference port diffusionを回収する。有限相関GLEからwhite-noise極限を取る物理的基本表現はStratonovichとし、constant-mobility leading sectorではnoiseが加法的なのでCartesian Itô表示と一致する。

本付録はこのgeneric R214出力に二段のcandidate strengtheningを加える。

- R215A：未規格化weight (w) とflow (U) が同じ規格化density/currentを表すcompatibility条件を置き、R214 diffusionのequivarianceと同じpath lawのBayes backward driftを導く。
- R215B：R215Aのscore
  [
  u=
upartial_xlogpi
  ]
  に対応する
  [
  mathcal F_{m SI}
  =
  rac{M_X}{2}intpi u^2dx
  ]
  をspatial-information gradient free energyとして定義し、Fisher情報、補助heat flowのrelative-entropy dissipation、path-space KL、微小translation識別率との恒等式を整理する。

R214Aのcanonical potential of mean force
[
F_{m db}(X)simeq-k_BTlog w(X)
]
と、R215Bのfunctional
[
mathcal F_{m SI}[pi]
]
は別の量である。前者はdumbbell内部phase volumeを消去した局所mean force、後者はそのscoreが保持する空間情報の勾配functionalとして本付録で新たに定義する。

また、R215Bで使う (M_X) はR214 dumbbell重心の実慣性質量である。M37/R185のSchrödinger表示に現れる設計質量 (m) と同一視しない。

## AD.2 projectively compatible density/flow port

固定有限時間 (0le tle T)、1次元周期領域
[
Omega=mathbb T_ell
]
を考える。(win C^{1,2}) は
[
w(x,t)ge w_*>0
]
を満たし、(U) はboundedかつ空間Lipschitzとする。

[
Z(t)=int_Omega w(x,t),dx,
qquad
pi(x,t)=rac{w(x,t)}{Z(t)}
]
と定義する。

<!-- theorem-start:theorem -->
**補題（R215A-0：projective compatibility）**

ある時間だけのscalar (lambda(t)) が存在して
[
partial_t w+partial_x(wU)=lambda(t)w
]
が成立するとする。周期境界では
[
lambda(t)=rac{dot Z(t)}{Z(t)}
]
であり、規格化densityは
[
oxed{
partial_tpi+partial_x(pi U)=0
}
]
を満たす。

逆に、正規化density (pi) が上のcontinuity equationを満たすなら、任意の正の (Z(t)) に対して (w=Z(t)pi) はprojective compatibilityを満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215A-0）**

periodic boundaryにより
[
dot Z
=
int_Omegapartial_t w,dx
=
lambda Z.
]
一方
[
partial_tpi
=
rac{partial_t w}{Z}
-rac{dot Z}{Z}pi
=
-rac{partial_x(wU)}{Z}
=
-partial_x(pi U).
]
逆向きは (w=Zpi) を直接微分すればよい。証明終。
<!-- theorem-end:proof -->

従って
[
wmapsto c(t)w,qquad c(t)>0
]
というglobal amplitudeの変更は同じ (pi) と同じscore
[
partial_xlog w=partial_xlogpi
]
を表す。

## AD.3 R215A：compatible-port equivariance / Bayes score theorem

R214Bのreference port diffusionを
[
dX_t
=
b_+(X_t,t)dt+sqrt{2
u}circ dW_t,
]
[
b_+
=
U+
upartial_xlog w
=
U+
upartial_xlogpi
]
とする。noise amplitudeは定数なので以下ではFokker--PlanckおよびBayes条件付き率の計算だけItô表示を使う。

<!-- theorem-start:theorem -->
**定理（R215A：compatible-port equivariance / Bayes score）**

AD.2のprojective compatibility、(wge w_*>0)、bounded spatial-Lipschitz (U)、constant (
u>0) を仮定する。上のR214 reference port diffusionを (mathcal L(X_0)=pi_0) から開始すると
[
oxed{
mathcal L(X_t)=pi_t
qquad
(0le tle T)
}
]
が成立する。

さらに同じ共同path lawのBayes backward mean drift (b_-) は
[
oxed{
b_-=U-
upartial_xlogpi
}
]
であり、
[
oxed{
b_pm=Upm u,
qquad
u:=
upartial_xlogpi
}
]
を得る。従って
[
oxed{
rac{b_++b_-}{2}=U,
qquad
rac{b_+-b_-}{2}=u.
}
]

(b_-) は未来から作用する第二bathを表さず、同じ前向きpath measureをBayes条件付き確率で逆向きにfactorizeしたmean driftである。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215A）**

加法noiseなのでStratonovichとItôのdriftは一致する。forward density (p) のFokker--Planck方程式は
[
partial_t p
=
-partial_x
left[
left(
U+
upartial_xlogpi
ight)p
ight]
+

upartial_x^2p.
]
(p=pi) を代入すると
[
-
upartial_x
left(
pipartial_xlogpi
ight)
+

upartial_x^2pi
=
-
upartial_x^2pi+
upartial_x^2pi
=0,
]
従ってAD.2のcontinuity equation
[
partial_tpi=-partial_x(pi U)
]
と一致する。parabolic initial-value problemの一意性から (p_t=pi_t)。

constant diffusion (2
u) の同じpath lawについてBayes time reversalは
[
b_-
=
b_+-2
upartial_xlog p.
]
(p=pi) とforward driftを代入すれば
[
b_-
=
U-
upartial_xlogpi.
]
証明終。
<!-- theorem-end:proof -->

R215Aのforward/backward generatorsを
[
D_+
=
partial_t
+
(U+u)partial_x
+

upartial_x^2,
]
[
D_-
=
partial_t
+
(U-u)partial_x
-

upartial_x^2
]
と書けば
[
D_+X=U+u,
qquad
D_-X=U-u.
]
本付録では (rac12(D_+D_-+D_-D_+)X) を力へ等置しない。時間対称Newton則はR185の責務である。

### AD.3.1 R214B finite-Hamiltonian corollary

R214Bはactual finite-bath dumbbell (X_t^{m db}) とreference port diffusion (X_t^{m port}) に
[
sup_{tle T}
W_1
left(
mathcal L(X_t^{m db}),
mathcal L(X_t^{m port})
ight)
le
arepsilon_{214}^{m port}(T)
]
を与える。

portがR215A compatibleで
[
mathcal L(X_0^{m port})=pi_0
]
なら
[
oxed{
sup_{tle T}
W_1
left(
mathcal L(X_t^{m db}),
pi_t
ight)
le
arepsilon_{214}^{m port}(T).
}
]

この(W_1) closenessだけから
[

ablalog p_t
simeq

ablalogpi_t
]
は従わない。従ってactual dumbbellのfinite-error backward score theoremは本結果に含めない。

### AD.3.2 current M37/M64 specialization

現行M64/R185 regularized density
[
ho_delta
=
rac{ho+delta q_0}{1+delta},
qquad
q_0=rac1ell
]
を考える。正の定数 (C) に対してideal compatible portを
[
arrho^circ=Cho,
qquad
arrho_T=Cdelta q_0,
qquad
w^circ=C(ho+delta q_0)
]
と選べば
[
pi^circ
=
rac{w^circ}{int w^circ dx}
=
ho_delta,
]
[
partial_xlog w^circ
=
partial_xlogho_delta.
]
さらに
[
U^circ=v_delta
]
とすればM64 continuityからR215A compatibilityが成立し、
[
b_pm^circ
=
v_delta
pm

upartial_xlogho_delta
]
を得る。actual R214 scalar/flow portとの差は付録AC.7.2の
(arepsilon_arrho,arepsilon_U) とscore/drift stability ledgerへ渡す。

## AD.4 R215B：spatial-information gradient free energy

R215Aのcompatible density (pi) とscore velocity
[
u=
upartial_xlogpi
]
を使う。

<!-- theorem-start:theorem -->
**定理（R215B：spatial-information free-energy identities）**

R214 dumbbell重心の有限慣性質量を (M_X>0) とする。spatial-information gradient free energyを
[
oxed{
mathcal F_{m SI}[pi]
:=
rac{M_X}{2}
int_Omega
pi(x)|u(x)|^2dx
}
]
と定義する。

Fisher information
[
I_F[pi]
:=
int_Omega
pi|partial_xlogpi|^2dx
=
int_Omega
rac{|partial_xpi|^2}{pi}dx
]
に対して
[
oxed{
mathcal F_{m SI}
=
rac{M_X
u^2}{2}I_F[pi]
=
2M_X
u^2
int_Omega
|partial_xsqrtpi|^2dx.
}
]

さらに
[
	au_v:=rac{M_X}{gamma_X},
qquad
ell_v^2:=
u	au_v,
qquad
mathcal J_{m SI}:=2M_X
u=2k_BT	au_v
]
と置けば
[
oxed{
mathcal F_{m SI}
=
rac{k_BT}{2}ell_v^2I_F[pi]
=
rac{mathcal J_{m SI}^2}{8M_X}I_F[pi].
}
]

未規格化port (w=Zpi) では
[
oxed{
mathcal F_{m SI}[w]
=
rac{M_X
u^2}{2Z}
int_Omega
rac{|partial_xw|^2}{w}dx,
}
]
従って任意の (c(t)>0) に対して
[
mathcal F_{m SI}[cw]
=
mathcal F_{m SI}[w].
]
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215B）**

(u=
upartial_xlogpi) を定義へ代入すれば最初のFisher identityを得る。
[
rac{|partial_xpi|^2}{pi}
=
4|partial_xsqrtpi|^2
]
でDirichlet表示が従う。FDT
[

u=rac{k_BT}{gamma_X}
]
と (	au_v=M_X/gamma_X) を使えば
[
M_X
u=k_BT	au_v,
qquad
mathcal J_{m SI}=2M_X
u
]
なので残りの係数表示を得る。(w=Zpi) では (Z) が空間一定であり
[
rac1Zrac{|partial_xw|^2}{w}
=
rac{|partial_xpi|^2}{pi},
]
従ってprojective invarianceが成立する。証明終。
<!-- theorem-end:proof -->

(mathcal F_{m SI}) は微視的瞬間運動エネルギー
[
Eleft[rac{M_X}{2}V^2mid Xight]
]
と同一視しない。R215Aで現れるforward/backward scoreが担う空間識別情報へR214/FDTの同じ (M_X,gamma_X,T) から自然なエネルギー次元を与えるcandidate constitutive quantityである。

### AD.4.1 補助heat flowによるrelative-entropy dissipation

(t) の実時間とは別の補助parameter (s) に対して
[
partial_spi_s
=

upartial_x^2pi_s,
qquad
pi_{s=0}=pi
]
を考える。periodic uniform density (q_0=1/ell) に対し
[
mathcal D[pi_s]
=
D_{m KL}(pi_sVert q_0)
=
intpi_slograc{pi_s}{q_0}dx
]
とすると、積分部分積分から
[
oxed{
rac{d}{ds}mathcal D[pi_s]
=
-
u I_F[pi_s].
}
]
従って
[
oxed{
mathcal F_{m SI}[pi]
=
-rac{	au_v}{2}
left.
rac{d}{ds}
left[
k_BT
D_{m KL}(pi_sVert q_0)
ight]
ight|_{s=0}.
}
]
これはR214実時間dynamicsに新しいentropy production lawを課す式ではなく、現在のdensity形状に付随するFisher functionalのheat-flow characterizationである。

### AD.4.2 score-ON / current-only path-space KL

同じ初期分布と同じconstant noiseを持つ二つのpath lawを
[
P_{m score}:
quad
dX_t=(U+u)dt+sqrt{2
u},dW_t,
]
[
P_{m cur}:
quad
dX_t=Udt+sqrt{2
u},dW_t
]
とする。Novikov条件が成立するsafe sectorではGirsanov公式から
[
D_{m KL}
left(
P_{m score}^{[0,T]}
Vert
P_{m cur}^{[0,T]}
ight)
=
rac1{4
u}
E_{P_{m score}}
int_0^T
|u(X_t,t)|^2dt.
]
R215Aのequivarianceを使えば
[
oxed{
int_0^T
mathcal F_{m SI}[pi_t]dt
=
mathcal J_{m SI}
D_{m KL}
left(
P_{m score}^{[0,T]}
Vert
P_{m cur}^{[0,T]}
ight).
}
]
(P_{m cur}) 自身が (pi_t) をmarginalとして持つことは要求しない。期待値は (P_{m score}) 側で評価する。

### AD.4.3 微小translation識別率

[
pi_epsilon(x)=pi(x-epsilon)
]
とすると、periodic smooth positive densityについて
[
oxed{
D_{m KL}(piVertpi_epsilon)
=
rac{epsilon^2}{2}I_F[pi]
+
O(epsilon^3).
}
]
従ってFisher情報は空間translationに対するlocal statistical distinguishabilityの曲率であり、(mathcal F_{m SI}) はその曲率にR214/FDTのエネルギー尺度を与えた量として読める。

### AD.4.4 node-safe regularization

現行R185と同じ一様背景
[
pi_delta
=
rac{ho+delta q_0}{1+delta},
qquad
q_0=rac1ell
]
について
[
oxed{
I_F[pi_delta]
=
rac1{1+delta}
int_Omega
rac{|partial_xho|^2}
{ho+delta q_0}dx
le
I_F[ho].
}
]
node-safe offsetはFisher情報をregularizeする。node-free (hogeho_*>0) のsmooth sectorでは
[
I_F[pi_delta]
=
I_F[ho]+O(delta).
]

### AD.4.5 port/score stabilityからfree-energy stability

二つのpositive normalized densities (pi,pi^circ) に
[
s=partial_xlogpi,
qquad
s^circ=partial_xlogpi^circ
]
と置く。単純な分解から
[
left|
I_F[pi]-I_F[pi^circ]
ight|
le
|pi-pi^circ|_{L^1}
|s|_infty^2
+
|s-s^circ|_infty
left(
|s|_infty+|s^circ|_infty
ight).
]
従って付録AC.7.2のport (C^1) stabilityからscore stabilityを経由して
[
|mathcal F_{m SI}[pi]-mathcal F_{m SI}[pi^circ]|
]
を明示的に制御できる。

## AD.5 functional derivativeとR215C境界

規格化制約 (intpi dx=1) の下で
[
mathcal F_{m SI}
=
2M_X
u^2
int|partial_xsqrtpi|^2dx
]
を変分すると
[
oxed{
rac{deltamathcal F_{m SI}}{deltapi}
=
-2M_X
u^2
rac{partial_x^2sqrtpi}{sqrtpi}
+
C(t),
}
]
ここで (C(t)) は規格化constraintによる空間一定項である。

本付録では
[
-pipartial_x
rac{deltamathcal F_{m SI}}{deltapi}
]
をmediumのphysical reversible forceとして採用しない。このconstitutive closure、その有限Hamiltonian parent、Madelung/Schrödinger再導出は後続R215C/M68の責務とする。

また
[
mathcal J_{m SI}=2M_X
u
]
をM37/R185の (mathcal J_0=2m
u) と同一視しない。固定 (T,gamma_X) でstrict (M_X	o0) を取れば
[
	au_v,mathcal J_{m SI},mathcal F_{m SI}	o0
]
なので、R215Bは
[
	au_{m bath}ll	au_vll	au_{m slow}
]
を満たす有限だが短い慣性時間を持つphysical ancestorのcandidate information free energyとして扱う。

## AD.6 status

- R215AはR214 generic portのうちprojectively compatibleなdensity/flow pairについて、equivarianceと同じpath lawのBayes score decompositionを与えるcandidate exact kinematic resultである。
- R215BはR215A scoreからspatial-information gradient free energyを定義し、Fisher、heat-flow relative entropy、path KL、translation distinguishabilityとの恒等式を与えるcandidate information-theoretic resultである。
- R214A/Bのrequired状態とcurrent M37/M64 specializationは変更しない。
- Q3-1/Q3-2 fixed-goal達成、Q3-1-A1/Q3-2-A1、A2、R161/R185の運用状態を変更しない。
- R215C、M68、medium reversible closure、Schrödinger再導出、M37退役は本付録に含めない。
