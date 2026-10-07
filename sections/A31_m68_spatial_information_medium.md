@number: AE
@chapter: 付録
@title: M68 finite-capacity spatial-information medium
@status: M68/R216A--R216DをR215Cのfinite-lattice Hamiltonian realizationとR214 dumbbell feedbackを統合するcandidate strengtheningとする。R214A/B required、R215A--C candidate、M67現行physical parent、M37/R86・M64/R203・R161/R185 active状態、Q3 fixed-goal/A1/A2/M0、Q3-6未達を変更しない。Fisher/Dirichlet gradient potentialのよりprimitiveな起源、旧M37 parameter matching、M37退役は本付録の主張に含めない。

## AE.1 目的と責務境界

M68の目的は、R215Cでconstitutive assumptionとして置いたspatial-information gradient free energyを有限次元のreal canonical mediumへ明示実装し、R214 dumbbell tracerとfinite harmonic bathを同じjoint Hamiltonian candidateへ接続することにある。

M68は

~~~math
\text{intrinsic spatial-information medium}
+
\text{R214 dumbbell tracer}
+
\text{finite bath}
~~~

という三層を使う。R214 reciprocal loadの平均をR215C information stressと同一視しない。前者はtracer--medium interactionの作用反作用、後者はmedium自身のgradient self stressである。

Schrödinger fieldは一次的自由度に置かない。順序は

~~~math
(Q_i,S_i)
\longrightarrow
(p_i,U_i)
\longrightarrow
\text{R215C}
\longrightarrow
\Psi_{\rm SI}
~~~

とし、最後の複素表示はR215Cと同じderived representationである。

## AE.2 M68 finite lattice medium

1次元周期領域をL個のcellへ分け、格子幅をaとする。各cellにreal canonical pair

~~~math
(Q_i,S_i),
\qquad
\{Q_i,S_j\}=\delta_{ij},
\qquad
Q_i>0
~~~

を置く。medium総capacityとnormalized cell profileを

~~~math
C:=\sum_{i=1}^{L}Q_i,
\qquad
p_i:=\frac{Q_i}{C},
\qquad
\sum_i p_i=1
~~~

とする。candidate theoremでは固定有限時間上のnode-safe sector

~~~math
p_i\ge p_*>0
~~~

を仮定する。

edge量を

~~~math
\bar p_{i+1/2}
=
\frac{p_i+p_{i+1}}2,
\qquad
\nabla_aS_{i+1/2}
=
\frac{S_{i+1}-S_i}{a}
~~~

とする。medium一capacity単位のHamiltonianを

~~~math
h_{68}[p,S]
=
\sum_i
\frac{\bar p_{i+1/2}}{2M_X}
(\nabla_aS_{i+1/2})^2
+
\sum_iV_ip_i
+
\mathcal F_{{\rm SI},a}[p],
~~~

~~~math
\boxed{
\mathcal F_{{\rm SI},a}[p]
=
\frac{2M_X\nu^2}{a^2}
\sum_i
\left(
\sqrt{p_{i+1}}-\sqrt{p_i}
\right)^2
}
~~~

と置き、extensive medium Hamiltonianを

~~~math
\boxed{
H_{\rm med}^{68}
=
C\,h_{68}[p,S].
}
~~~

とする。

R214 dumbbellとfinite bathを同じsystemへ接続したfull candidateは概念的に

~~~math
\boxed{
H_{68}
=
H_{\rm med}^{68}
+
H_{\rm db}[p,X,\mathbf r,\mathbf p_r]
+
H_B.
}
~~~

である。R214のcanonical potential of mean force
\(F_{\rm db}\simeq-k_BT\log w\) は \(H_{\rm db}+H_B\) のfast variableを消去した後の量なので、H68へ独立に重ねて足さない。

### AE.2.1 R216A：finite-lattice spatial-information medium

<!-- theorem-start:theorem -->
**定理（R216A：M68 finite-lattice spatial-information medium）**

上のperiodic finite lattice Hamiltonianについて、global shift

~~~math
S_i\mapsto S_i+\theta
~~~

はexact symmetryである。従って

~~~math
\boxed{
\dot C=0.
}
~~~

またstatic \(V_i\) では

~~~math
\boxed{
\frac{dH_{\rm med}^{68}}{dt}=0.
}
~~~

Hamilton方程式からnormalized profileは

~~~math
\boxed{
\dot p_i
=
J_{i-1/2}-J_{i+1/2},
}
~~~

~~~math
J_{i+1/2}
=
\frac{\bar p_{i+1/2}}{M_Xa}
\nabla_aS_{i+1/2}
~~~

というdiscrete continuity lawを満たす。

smooth positive periodic fieldsに対し
\(p_i=a\pi(x_i)+O(a^3)\)、\(S_i=S(x_i)\) と標本化すると、

~~~math
h_{68}
=
\int
\left[
\frac{\pi(\partial_xS)^2}{2M_X}
+
V\pi
\right]dx
+
2M_X\nu^2
\int
|\partial_x\sqrt\pi|^2dx
+
O(a^2).
~~~

従ってnode-safe smooth sectorのlocal consistency limitはR215C field Hamiltonianである。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R216A）**

H68はSの差だけに依存するためglobal shift symmetryからNoether量Cが保存される。直接には
\(\dot C=\sum_i\partial H/\partial S_i\) がperiodic telescopingで0になる。static HamiltonianなのでHamilton方程式に沿うenergy derivativeはPoisson bracket \(\{H,H\}=0\)。

edge kinetic termをS_iで微分すると左右edge fluxの差だけが残るためdiscrete continuityを得る。Fisher termは
\(p_i=a\pi(x_i)\) に対し
\(\sqrt{p_i}=\sqrt a\,\sqrt{\pi(x_i)}\) なのでperiodic centered consistencyから
\(\mathcal F_{{\rm SI},a}
=
2M_X\nu^2\int|\partial_x\sqrt\pi|^2dx+O(a^2)\)。
kinetic/potential項も同じperiodic quadratureでR215Cへ収束する。証明終。
<!-- theorem-end:proof -->

R216Aはfinite-dimensional Hamiltonian realizationの存在を示すが、Fisher/Dirichlet potential自体をさらにprimitiveなspring/LC/local-bath Hamiltonianから導出したとは扱わない。

## AE.3 R216B：Nelson mass-matched closure

R215Aのsame-path forward/backward mean driftを

~~~math
b_\pm
=
U\pm u,
\qquad
u=\nu\partial_x\log\pi
~~~

とする。対応するmean derivativesを

~~~math
D_+
=
\partial_t+(U+u)\partial_x+\nu\partial_x^2,
~~~

~~~math
D_-
=
\partial_t+(U-u)\partial_x-\nu\partial_x^2
~~~

とする。

<!-- theorem-start:theorem -->
**定理（R216B：R215C + R215A Nelson closure）**

\(R=\sqrt\pi>0\) とすると

~~~math
\boxed{
u\partial_xu+\nu\partial_x^2u
=
2\nu^2
\partial_x
\left(
\frac{\partial_x^2R}{R}
\right).
}
~~~

medium equationを一般のinertial coefficient \(M_{\rm med}\) で

~~~math
M_{\rm med}
(\partial_tU+U\partial_xU)
=
-\partial_xV
+
2M_X\nu^2
\partial_x
\left(
\frac{\partial_x^2R}{R}
\right)
~~~

と書くと、Nelson time-symmetric mean accelerationは

~~~math
\frac12(D_+D_-+D_-D_+)X
=
-\frac{\partial_xV}{M_{\rm med}}
+
2\nu^2
\left(
\frac{M_X}{M_{\rm med}}-1
\right)
\partial_x
\left(
\frac{\partial_x^2R}{R}
\right).
~~~

従って

~~~math
\boxed{
M_{\rm med}=M_X
}
~~~

なら

~~~math
\boxed{
M_X
\frac12(D_+D_-+D_-D_+)X
=
-\partial_xV.
}
~~~

非自明なprofileで
\(\partial_x(R_{xx}/R)\not\equiv0\) なら、このmass matchingはgenericに必要である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R216B）**

\(u=2\nu R_x/R\) を二回微分して整理すればscore identityを得る。mean derivativeを直接展開すると

~~~math
\frac12(D_+D_-+D_-D_+)X
=
\partial_tU+U\partial_xU
-u\partial_xu-\nu\partial_x^2u.
~~~

medium equationとscore identityを代入すれば表示式を得る。証明終。
<!-- theorem-end:proof -->

ここで \(M_X\) はmedium全体の総質量ではなく、一capacity単位のinertial coefficientである。total medium inertiaはC倍される。M37/R185の設計質量mとはまだ同一視しない。

## AE.4 R216C：capacity scalingとreciprocal-load separation

M68ではdumbbell interactionはextensive amount Qではなくintensive profile \(p=Q/C\) を読む。interaction Hamiltonianを

~~~math
H_{\rm int}=h_{\rm int}(p,X,\ldots)
~~~

とする。

<!-- theorem-start:theorem -->
**定理（R216C：intensive score / reciprocal \(1/C\) scaling）**

\(C=\sum_iQ_i\)、\(p_i=Q_i/C\) なら

~~~math
\frac{\partial p_j}{\partial Q_i}
=
\frac{\delta_{ij}-p_j}{C}.
~~~

従って

~~~math
\boxed{
\frac{\partial H_{\rm int}}{\partial Q_i}
=
\frac1C
\left[
\frac{\partial h_{\rm int}}{\partial p_i}
-
\sum_jp_j
\frac{\partial h_{\rm int}}{\partial p_j}
\right].
}
~~~

safe compact sectorで \(h_{\rm int}\) のp微分がO(1)ならsingle-tracer reciprocal shape loadは

~~~math
\boxed{
F_{Q_i}^{\rm rec}=O(C^{-1}).
}
~~~

一方R214 score portが \(w(X;p)\) のようにintensive profileだけから作られるなら

~~~math
\boxed{
\partial_X\log w=O(1)
}
~~~

であり、tracerのosmotic/score effectはcapacityを大きくしても薄まらない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R216C capacity scaling）**

\(p_j=Q_j/\sum_kQ_k\) を直接微分しchain ruleを使えば表示式を得る。scoreはpを固定したuniform scaling \(Q\mapsto cQ\) に不変なのでC依存を持たない。証明終。
<!-- theorem-end:proof -->

### AE.4.1 reciprocal neutrality / Fisher variance

translation parameteraに対するideal R214 reciprocal forceを

~~~math
F_a^{\rm rec}
=
-k_BT\,\partial_x\log\pi(X)
~~~

とする。periodic normalized \(\pi\) と \(X\sim\pi\) なら

~~~math
\boxed{
E_\pi[F_a^{\rm rec}]=0,
}
~~~

~~~math
\boxed{
E_\pi[(F_a^{\rm rec})^2]
=
(k_BT)^2I_F[\pi].
}
~~~

さらに \(\nu=k_BT/\gamma_X\) なので

~~~math
\boxed{
\mathcal F_{\rm SI}
=
\frac{M_X}{2\gamma_X^2}
E_\pi[(F_a^{\rm rec})^2].
}
~~~

したがってinformation free energyはmean reciprocal loadではなく、同じscore couplingのtranslation-force varianceと結びつく。M68 medium forceは

~~~math
f_{\rm medium}
=
f_{\rm SI}
+
f_{\rm rec}
~~~

であり、intrinsic information stressとsingle-tracer reciprocal loadを別項として数える。

## AE.5 R216D：adapted feedback / finite-capacity equivariance

finite-dimensional medium stateをYとまとめる。actual dumbbell feedback系とcoarse port feedback系を

~~~math
\dot Y^{\rm db}
=
A(Y^{\rm db})
+
\frac1C
G_{\rm db}(Y^{\rm db},X^{\rm db},r),
~~~

~~~math
\dot Y^{\rm port}
=
A(Y^{\rm port})
+
\frac1C
G_{\rm port}(Y^{\rm port},X^{\rm port}),
~~~

~~~math
dX^{\rm port}
=
b(Y^{\rm port},X^{\rm port})dt
+
\sqrt{2\nu}\,dW_t
~~~

と書く。

固定有限時間Tで、node-safe compact sector上に次を仮定する。

- A、b、Gportは対応する変数について一様Lipschitz。
- bは一様boundedで、portはprogressively measurableかつnonanticipating。
- finite-bath初期状態はresolved initial dataに条件付けたshifted canonical preparation。
- R209B finite-bath Markovization errorとR214B small-mass/fast-dumbbell errorはこのfeedback-safe class上で一様に評価できる。
- microscopic/coarse feedback residual
  \(R_G=G_{\rm db}-G_{\rm port}\) は
  \(\mathcal R_G(T):=E\int_0^T|R_G(s)|ds<\infty\)
  を満たす。

<!-- theorem-start:theorem -->
**定理（R216D：adapted-feedback R214 stability）**

上の条件のもと、同じinitial dataと同じBrownian driverでcoupleできるactual finite-bath dumbbell feedback系とcoarse port feedback系について、有限な \(\Lambda_T,B_T\) が存在して

~~~math
\boxed{
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{\rm db,fb}),
\mathcal L(X_t^{\rm port,fb})
\right)
\le
\left[
\varepsilon_{214}^{\rm port}(T)
+
\frac{B_T}{C}
\right]
\exp
\left(
\frac{\Lambda_T}{C}
\right).
}
~~~

\(B_T\) は \(\mathcal R_G(T)\) に比例して取れる。特にmicroscopic feedbackとcoarse feedbackが一致して \(R_G=0\) なら

~~~math
\boxed{
\varepsilon_{\rm fb}
=
\left[
\exp(\Lambda_T/C)-1
\right]
\varepsilon_{214}^{\rm port}
=
O(C^{-1}\varepsilon_{214}^{\rm port}).
}
~~~

従ってadapted random portであること自体は独立なO(1) errorを作らない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R216D adapted feedback）**

まずactual medium path \(Y^{\rm db}\) を固定して読む補助port diffusion \(\widehat X\) を同じnoiseで駆動する。R214Bの変数
\(Y_X=X+(M_X/\gamma_X)V\) を使うsmall-mass synchronous couplingはdriftのdeterministic性を使わず、progressive measurability、一様bound、空間Lipschitz性だけを使う。exact harmonic-bath eliminationもfeedback trajectoryに対するDuhamel identityなので変わらない。feedback-safe classでR209B Markovizationを一様化すれば

~~~math
E\sup_{t\le T}
|X_t^{\rm db}-\widehat X_t|
\le
\varepsilon_{214}^{\rm port}(T)
~~~

を得る。

次に
\(D_X(t)=E\sup_{s\le t}|X_s^{\rm db}-X_s^{\rm port}|\)、
\(D_Y(t)=E\sup_{s\le t}\|Y_s^{\rm db}-Y_s^{\rm port}\|\)
と置く。same-noise couplingとbのLipschitz性から

~~~math
D_X(t)
\le
\varepsilon_{214}^{\rm port}
+
K_b
\int_0^tD_Y(s)ds.
~~~

medium equationの差とGportのLipschitz性から

~~~math
D_Y(t)
\le
K_A
\left[
\frac1C
\int_0^tD_X(s)ds
+
\frac{\mathcal R_G(t)}C
\right].
~~~

二式を代入しdouble integralをT倍のsingle integralで抑えてGronwallを適用すれば定理形を得る。証明終。
<!-- theorem-end:proof -->

### AE.5.1 finite-capacity annealed equivariance

feedbackなしreference medium \(Y^{(0)}\) とR215A port diffusion \(X^{(0)}\) は

~~~math
\mathcal L(X_t^{(0)})
=
\pi_t^{(0)}
~~~

をexactに満たす。finite-C port feedbackは

~~~math
\dot Y^{(C)}
=
A(Y^{(C)})
+
\frac1C
G(Y^{(C)},X^{(C)})
~~~

なので、same-noise/Gronwall stabilityから固定Tで

~~~math
\|Y_t^{(C)}-Y_t^{(0)}\|
=
O(C^{-1}),
~~~

~~~math
W_1(
\mathcal L(X_t^{(C)}),
\pi_t^{(0)}
)
=
O(C^{-1}).
~~~

random medium profileのensemble平均を

~~~math
\bar\pi_t^{(C)}
=
E[\pi(Y_t^{(C)})]
~~~

とすると、medium-to-density mapのLipschitz性から

~~~math
\boxed{
W_1
\left(
\mathcal L(X_t^{\rm port,fb}),
\bar\pi_t^{(C)}
\right)
\le
\frac{K_{\rm eq}(T,a,p_*)}{C}.
}
~~~

これをfinite-capacity annealed equivarianceと呼ぶ。feedback後の
\(\mathcal L(X_t\mid Y_t)=\pi(Y_t)\)
というconditional exact statementは一般に主張しない。

actual dumbbellまで合成すると

~~~math
\boxed{
W_1
\left(
\mathcal L(X_t^{\rm db,fb}),
\bar\pi_t^{(C)}
\right)
\le
\left[
\varepsilon_{214}^{\rm port}
+
\frac{B_T}{C}
\right]
e^{\Lambda_T/C}
+
\frac{K_{\rm eq}}{C}.
}
~~~

reciprocal neutralityによりmean medium biasがO(C^{-2})へ改善するsectorはあり得るが、medium--tracer correlationはgenericにO(C^{-1})なのでannealed equivariance全体はO(C^{-1})を標準次数とする。

## AE.6 external potentialとenergy bookkeeping

M68 leading constructionではexternal potentialVはmedium current equationへ入れる。R214 overdamped tracerへ独立な \(-\mu\nabla V\) driftを重ねない。R216Bによりtracerのtime-symmetric mean accelerationとして \(-\nabla V/M_X\) が既に回収されるためである。

full finite HamiltonianH68がtime independentならtotal energyはexact保存される。mediumだけを粗視化すればtracer/bathとのwork exchangeが残るため、R215C medium-only energy conservationはfeedbackを落としたleading sectorまたはlarge-C limitとして回収する。

## AE.7 誤差台帳とstatus

M68 candidateの固定finite-time error ledgerは

~~~math
\varepsilon_{68}
=
\varepsilon_{\rm lattice}
+
\varepsilon_{214}^{\rm port}
+
\varepsilon_{\rm fb}
+
\varepsilon_{\rm cap},
~~~

~~~math
\varepsilon_{\rm lattice}=O(a^2),
\qquad
\varepsilon_{\rm cap}=K_{\rm eq}/C.
~~~

R216A--Dが示すのは、R215C information mediumとR214 tracerをfinite-dimensional Hamiltonian candidateへ同居させ、Nelson closureとfinite-capacity feedback stabilityを同じparameter setで両立できることである。

本付録は次を主張しない。

- Fisher/Dirichlet gradient potentialのさらにprimitiveなspring/LC/local-bath origin
- \(a\to0\)、node regulator \(\to0\)、\(C\to\infty\) の同時一様極限
- variable mobilityを含むexact Schrödinger closure
- 多粒子M68
- \(M_X=m\) または \(\mathcal J_{\rm SI}=\mathcal J_0\) の旧模型間matching
- M37/R86の置換または退役
- Q3-6 circulation quantization
