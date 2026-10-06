@number: AD
@chapter: 付録
@title: R215 compatible score と空間情報勾配自由エネルギー
@status: R215A--R215BをM67/R214 continuous-tracer lineのcandidate strengtheningとする。R214A/Bのrequired状態、Q3 fixed-goal達成、A1/A2、M37/R86、M64/R203、R161/R185の運用状態は変更しない。R215Cのmedium reversible closure、M68、Schrödinger再導出は本付録の主張に含めない。

## AD.1 目的と責務境界

付録AC/R214A--R214Bはgeneric nonnegative scalar port \(\varrho\) とflow port \(U\) を受け、node-safe weight
\[
w(x,t)=\varrho(x,t)+\varrho_T>0
\]
から
\[
dX_t=
\left[
U(X_t,t)+\nu\partial_x\log w(X_t,t)
\right]dt
+
\sqrt{2\nu}\circ dW_t,
\qquad
\nu=\frac{k_BT}{\gamma_X}
\]
というreference port diffusionを回収する。有限相関GLEからwhite-noise極限を取る物理的基本表現はStratonovichとし、constant-mobility leading sectorではnoiseが加法的なのでCartesian Itô表示と一致する。

本付録では、R214Aのcanonical potential of mean force
\[
F_{\rm db}(X)\simeq-k_BT\log w(X)
\]
と、R215Bで定義する
\[
\mathcal F_{\rm SI}[\pi]
\]
を区別する。前者はdumbbell内部phase volumeを消去した局所mean force、後者はR215Aのscoreに対応する空間情報の勾配functionalである。

またR215Bで使う \(M_X\) はR214 dumbbell重心の実慣性質量であり、M37/R185のSchrödinger表示に現れる設計質量 \(m\) と同一視しない。

## AD.2 projectively compatible density/flow port

固定有限時間 \(0\le t\le T\)、1次元周期領域
\[
\Omega=\mathbb T_\ell
\]
を考える。\(w\in C^{1,2}\) は
\[
w(x,t)\ge w_*>0
\]
を満たし、\(U\) はboundedかつ空間Lipschitzとする。

\[
Z(t)=\int_\Omega w(x,t)\,dx,
\qquad
\pi(x,t)=\frac{w(x,t)}{Z(t)}
\]
と定義する。

<!-- theorem-start:theorem -->
**補題（R215A-0：projective compatibility）**

ある時間だけのscalar \(\lambda(t)\) が存在して
\[
\partial_t w+\partial_x(wU)=\lambda(t)w
\]
が成立するとする。周期境界では
\[
\lambda(t)=\frac{\dot Z(t)}{Z(t)}
\]
であり、規格化densityは
\[
\boxed{
\partial_t\pi+\partial_x(\pi U)=0
}
\]
を満たす。

逆に、規格化density \(\pi\) がこのcontinuity lawを満たすなら、任意の正の \(Z(t)\) に対して \(w=Z(t)\pi\) はprojective compatibilityを満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215A-0）**

周期境界により
\[
\dot Z
=
\int_\Omega\partial_t w\,dx
=
\lambda Z.
\]
従って
\[
\partial_t\pi
=
\frac{\partial_t w}{Z}
-\frac{\dot Z}{Z}\pi
=
-\frac{\partial_x(wU)}{Z}
=
-\partial_x(\pi U).
\]
逆向きは \(w=Z\pi\) を直接微分すればよい。証明終。
<!-- theorem-end:proof -->

従って
\[
w\mapsto c(t)w,\qquad c(t)>0
\]
というglobal amplitudeの変更は同じ \(\pi\) と同じscore
\[
\partial_x\log w=\partial_x\log\pi
\]
を表す。

## AD.3 R215A：compatible-port equivariance / Bayes score

R214Bのreference port diffusionを
\[
dX_t
=
b_+(X_t,t)dt
+
\sqrt{2\nu}\circ dW_t,
\]
\[
b_+
=
U+\nu\partial_x\log w
=
U+\nu\partial_x\log\pi
\]
とする。noise amplitudeは定数なので、Fokker--PlanckとBayes条件付き率の計算だけItô表示へ移してもdrift補正は0である。

<!-- theorem-start:theorem -->
**定理（R215A：compatible-port equivariance / Bayes score）**

AD.2のprojective compatibility、\(w\ge w_*>0\)、bounded spatial-Lipschitz \(U\)、constant \(\nu>0\) を仮定する。上のR214 reference port diffusionを
\[
\mathcal L(X_0)=\pi_0
\]
から開始すると
\[
\boxed{
\mathcal L(X_t)=\pi_t
\qquad
(0\le t\le T)
}
\]
が成立する。

さらに同じ共同path lawのBayes backward mean drift \(b_-\) は
\[
\boxed{
b_-=U-\nu\partial_x\log\pi
}
\]
であり、
\[
\boxed{
b_\pm=U\pm u,
\qquad
u:=\nu\partial_x\log\pi
}
\]
を得る。従って
\[
\boxed{
\frac{b_++b_-}{2}=U,
\qquad
\frac{b_+-b_-}{2}=u.
}
\]

\(b_-\) は未来から作用する第二bathを表さず、同じ前向きpath lawをBayes条件付き確率で逆向きにfactorizeしたmean driftである。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215A）**

forward density \(p\) のFokker--Planck方程式は
\[
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
\]
\(p=\pi\) を代入すると
\[
-\nu\partial_x
\left(
\pi\partial_x\log\pi
\right)
+
\nu\partial_x^2\pi
=
0
\]
なので、AD.2の
\[
\partial_t\pi=-\partial_x(\pi U)
\]
と一致する。parabolic initial-value problemの一意性から \(p_t=\pi_t\)。

constant diffusion \(2\nu\) の同じpath lawについてBayes time reversalは
\[
b_-
=
b_+-2\nu\partial_x\log p.
\]
\(p=\pi\) とforward driftを代入すれば主張を得る。証明終。
<!-- theorem-end:proof -->

forward/backward generatorsを
\[
D_+
=
\partial_t
+
(U+u)\partial_x
+
\nu\partial_x^2,
\]
\[
D_-
=
\partial_t
+
(U-u)\partial_x
-
\nu\partial_x^2
\]
と書けば
\[
D_+X=U+u,
\qquad
D_-X=U-u.
\]
本付録では
\[
\frac12(D_+D_-+D_-D_+)X
\]
を力へ等置しない。時間対称Newton則はR185の責務である。

### AD.3.1 R214B finite-Hamiltonian corollary

R214Bはactual finite-bath dumbbell \(X_t^{\rm db}\) とreference port diffusion \(X_t^{\rm port}\) に
\[
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{\rm db}),
\mathcal L(X_t^{\rm port})
\right)
\le
\varepsilon_{214}^{\rm port}(T)
\]
を与える。

portがR215A compatibleで
\[
\mathcal L(X_0^{\rm port})=\pi_0
\]
なら
\[
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
\]

この \(W_1\) closenessだけから
\[
\nabla\log p_t
\simeq
\nabla\log\pi_t
\]
は従わない。従ってactual dumbbellのfinite-error backward score theoremは本結果に含めない。

### AD.3.2 current M37/M64 specialization

現行M64/R185 regularized density
\[
\rho_\delta
=
\frac{\rho+\delta q_0}{1+\delta},
\qquad
q_0=\frac1\ell
\]
を考える。正の定数 \(C\) に対してideal compatible portを
\[
\varrho^\circ=C\rho,
\qquad
\varrho_T=C\delta q_0,
\qquad
w^\circ=C(\rho+\delta q_0)
\]
と選べば
\[
\pi^\circ
=
\frac{w^\circ}{\int w^\circ dx}
=
\rho_\delta,
\]
\[
\partial_x\log w^\circ
=
\partial_x\log\rho_\delta.
\]
さらに
\[
U^\circ=v_\delta
\]
とすればM64 continuityからR215A compatibilityが成立し、
\[
b_\pm^\circ
=
v_\delta
\pm
\nu\partial_x\log\rho_\delta
\]
を得る。actual R214 scalar/flow portとの差は付録AC.7.2の
\[
\varepsilon_\varrho,\varepsilon_U
\]
とscore/drift stability ledgerへ渡す。

## AD.4 R215B：spatial-information free-energy identities

R215Aのcompatible density \(\pi\) とscore velocity
\[
u=\nu\partial_x\log\pi
\]
を使う。

<!-- theorem-start:theorem -->
**定理（R215B：spatial-information free-energy identities）**

R214 dumbbell重心の有限慣性質量を \(M_X>0\) とする。spatial-information gradient free energyを
\[
\boxed{
\mathcal F_{\rm SI}[\pi]
:=
\frac{M_X}{2}
\int_\Omega
\pi(x)|u(x)|^2dx
}
\]
と定義する。

Fisher information
\[
I_F[\pi]
:=
\int_\Omega
\pi|\partial_x\log\pi|^2dx
=
\int_\Omega
\frac{|\partial_x\pi|^2}{\pi}dx
\]
に対して
\[
\boxed{
\mathcal F_{\rm SI}
=
\frac{M_X\nu^2}{2}I_F[\pi]
=
2M_X\nu^2
\int_\Omega
|\partial_x\sqrt\pi|^2dx.
}
\]

さらに
\[
\tau_v:=\frac{M_X}{\gamma_X},
\qquad
\ell_v^2:=\nu\tau_v,
\qquad
\mathcal J_{\rm SI}:=2M_X\nu=2k_BT\tau_v
\]
と置けば
\[
\boxed{
\mathcal F_{\rm SI}
=
\frac{k_BT}{2}\ell_v^2I_F[\pi]
=
\frac{\mathcal J_{\rm SI}^2}{8M_X}I_F[\pi].
}
\]

未規格化port \(w=Z\pi\) では
\[
\boxed{
\mathcal F_{\rm SI}[w]
=
\frac{M_X\nu^2}{2Z}
\int_\Omega
\frac{|\partial_xw|^2}{w}dx,
}
\]
従って任意の \(c(t)>0\) に対して
\[
\mathcal F_{\rm SI}[cw]
=
\mathcal F_{\rm SI}[w].
\]
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R215B）**

\(u=\nu\partial_x\log\pi\) を定義へ代入すればFisher identityを得る。
\[
\frac{|\partial_x\pi|^2}{\pi}
=
4|\partial_x\sqrt\pi|^2
\]
でDirichlet表示が従う。FDT
\[
\nu=\frac{k_BT}{\gamma_X}
\]
と \(\tau_v=M_X/\gamma_X\) を使えば
\[
M_X\nu=k_BT\tau_v,
\qquad
\mathcal J_{\rm SI}=2M_X\nu
\]
なので残りの係数表示を得る。\(w=Z\pi\) では \(Z\) が空間一定なのでprojective invarianceも従う。証明終。
<!-- theorem-end:proof -->

\(\mathcal F_{\rm SI}\) は微視的瞬間運動エネルギー
\[
E\left[\frac{M_X}{2}V^2\mid X\right]
\]
と同一視しない。R215Aで現れるforward/backward scoreが担う空間識別情報へ、R214/FDTの同じ \(M_X,\gamma_X,T\) からエネルギー次元を与えるcandidate constitutive quantityである。

### AD.4.1 補助heat flowによるrelative-entropy dissipation

実時間 \(t\) とは別の補助parameter \(s\) に対して
\[
\partial_s\pi_s
=
\nu\partial_x^2\pi_s,
\qquad
\pi_{s=0}=\pi
\]
を考える。periodic uniform density \(q_0=1/\ell\) に対し
\[
\mathcal D[\pi_s]
=
D_{\rm KL}(\pi_s\Vert q_0)
=
\int\pi_s\log\frac{\pi_s}{q_0}dx
\]
とすると、積分部分積分から
\[
\boxed{
\frac{d}{ds}\mathcal D[\pi_s]
=
-\nu I_F[\pi_s].
}
\]
従って
\[
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
\]
これはR214実時間dynamicsに新しいentropy production lawを課す式ではなく、現在のdensity形状に付随するFisher functionalのheat-flow characterizationである。

### AD.4.2 score-ON / current-only path-space KL

同じ初期分布と同じconstant noiseを持つ二つのpath lawを
\[
P_{\rm score}:
\quad
dX_t=(U+u)dt+\sqrt{2\nu}\,dW_t,
\]
\[
P_{\rm cur}:
\quad
dX_t=Udt+\sqrt{2\nu}\,dW_t
\]
とする。Novikov条件が成立するsafe sectorではGirsanov公式から
\[
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
\]
R215Aのequivarianceを使えば
\[
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
\]
\(P_{\rm cur}\) 自身が \(\pi_t\) をmarginalとして持つことは要求しない。期待値は \(P_{\rm score}\) 側で評価する。

### AD.4.3 微小translation識別率

\[
\pi_\epsilon(x)=\pi(x-\epsilon)
\]
とすると、periodic smooth positive densityについて
\[
\boxed{
D_{\rm KL}(\pi\Vert\pi_\epsilon)
=
\frac{\epsilon^2}{2}I_F[\pi]
+
O(\epsilon^3).
}
\]
従ってFisher情報は空間translationに対するlocal statistical distinguishabilityの曲率である。

### AD.4.4 node-safe regularization

現行R185と同じ一様背景
\[
\pi_\delta
=
\frac{\rho+\delta q_0}{1+\delta},
\qquad
q_0=\frac1\ell
\]
について
\[
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
\]
node-safe offsetはFisher情報をregularizeする。node-free \(\rho\ge\rho_*>0\) のsmooth sectorでは
\[
I_F[\pi_\delta]
=
I_F[\rho]+O(\delta).
\]

### AD.4.5 port/score stabilityからfree-energy stability

二つのpositive normalized densities \(\pi,\pi^\circ\) に
\[
s=\partial_x\log\pi,
\qquad
s^\circ=\partial_x\log\pi^\circ
\]
と置く。単純な分解から
\[
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
\]
従って付録AC.7.2のport \(C^1\) stabilityからscore stabilityを経由して
\[
|\mathcal F_{\rm SI}[\pi]-\mathcal F_{\rm SI}[\pi^\circ]|
\]
を制御できる。

## AD.5 functional derivativeとR215C境界

規格化制約 \(\int\pi dx=1\) の下で
\[
\mathcal F_{\rm SI}
=
2M_X\nu^2
\int|\partial_x\sqrt\pi|^2dx
\]
を変分すると
\[
\boxed{
\frac{\delta\mathcal F_{\rm SI}}{\delta\pi}
=
-2M_X\nu^2
\frac{\partial_x^2\sqrt\pi}{\sqrt\pi}
+
C(t),
}
\]
ここで \(C(t)\) は規格化constraintによる空間一定項である。

本付録では
\[
-\pi\partial_x
\frac{\delta\mathcal F_{\rm SI}}{\delta\pi}
\]
をmediumのphysical reversible forceとして採用しない。このconstitutive closure、そのfinite-Hamiltonian parent、Madelung/Schrödinger再導出は後続R215C/M68の責務とする。

また
\[
\mathcal J_{\rm SI}=2M_X\nu
\]
をM37/R185の
\[
\mathcal J_0=2m\nu
\]
と同一視しない。固定 \(T,\gamma_X\) でstrict \(M_X\to0\) を取れば
\[
\tau_v,\mathcal J_{\rm SI},\mathcal F_{\rm SI}\to0
\]
なので、R215Bは
\[
\tau_{\rm bath}\ll\tau_v\ll\tau_{\rm slow}
\]
を満たす有限だが短い慣性時間を持つphysical ancestorのcandidate information free energyとして扱う。

## AD.6 status

- R215AはR214 generic portのうちprojectively compatibleなdensity/flow pairについて、equivarianceと同じpath lawのBayes score decompositionを与えるcandidate exact kinematic resultである。
- R215BはR215A scoreからspatial-information gradient free energyを定義し、Fisher、heat-flow relative entropy、path KL、translation distinguishabilityとの恒等式を与えるcandidate information-theoretic resultである。
- R214A/Bのrequired状態とcurrent M37/M64 specializationは変更しない。
- Q3-1/Q3-2 fixed-goal達成、Q3-1-A1/Q3-2-A1、A2、R161/R185の運用状態を変更しない。
- R215C、M68、medium reversible closure、Schrödinger再導出、M37退役は本付録に含めない。
