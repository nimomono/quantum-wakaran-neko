@number: AB
@chapter: 付録
@title: M67/NBL Q2 carrier candidateとcoherent Born-action reduction
@status: R213A--R213DをM67 structured reservoir内部のQ2 signal/register/gate置換候補として追加する。M54/R181B--R181C、R186、R206A--R206Eはactiveのまま維持し、Q2-4の条件付き達成、M0、A1/A2/B1--B3を変更しない。R213のrequired昇格、M54退役、R206 common-hub apparatus全体のfinite-Hamiltonian liftは後続課題とする。

## AB.1 目的と責務境界

本付録は、M54の一般direct-amplitude registerに代わる候補として、M67 structured reservoir内部にphase-tagged path carrierを置き、H/T/CNOT gate列を有限古典Hamiltonianで運び、終端でcoherent collector action

```math
J_y
=
J_*|A_y|^2
```

を生成するcandidate constructionを与える。

主要physical sectorは引き続き

```math
\mathcal R_{\rm str}
+
\mathcal X_{\rm marker}
```

である。path-memory、phase-tag、coherent leaf、collector、dark mode、phase-volume、finite bathはすべて単一structured reservoirの内部正準自由度であり、新しい第三実体を導入しない。

固定した有限qubit数 $n$ と有限gate列に対して全自由度は有限である。一方、Hadamard数を $h$ とすると素朴なpath populationは $M=2^h$、結果channel数は最大 $L=2^n$ であり、familyとして指数的な受動内部資源を許す。本付録は指数的な受動hardwareを除去したとは主張しない。狙いはR186で現れた指数local analog precisionを、有限状態path cellとcoherent energy-preserving reductionへ置換できるかを監査することである。

## AB.2 R213A：NBL/path state-space isometryとtime-sampling境界

各logical site $j$ に二つのreference function $R_{j0},R_{j1}$ を取り、

```math
\mathbb E[R_{jb}^*R_{kc}]
=
\delta_{jk}\delta_{bc}
```

とする。basis functionを

```math
\Phi_x
=
\prod_{j=1}^n R_{j,x_j},
\qquad
x\in\{0,1\}^n
```

と置き、

```math
\mathcal E_n(Z)
=
\Psi_Z
=
\sum_x Z_x\Phi_x
```

とする。

<!-- theorem-start:theorem -->
**定理（R213A：NBL/path isometryと有限time-sampling rank境界）**

上の独立reference familyでは

```math
\mathbb E[\Psi_Z^*\Psi_W]
=
Z^\dagger W,
\qquad
\mathbb E|\Psi_Z|^2
=
\sum_x|Z_x|^2
```

が成立し、tensor productはreference productへ写る。

一方、$m$ 個の有限time sampleだけから作るempirical Gram matrixのrankは高々 $m$ である。従って $2^n$ 次元basis全体について一様isometryをtime averagingだけで実現するには一般に $m\ge2^n$ が必要である。

この結果は、reference記述が小さいことから任意の $2^n$ amplitude vectorを $O(n)$ 個のtunable physical degreeで保持できるとは結論しない。R213B以後ではtime-sampled NBLを正本carrierにせず、有限Hamiltonian path populationを用いる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R213A）**

reference orthogonalityを積へ適用すると $\mathbb E[\Phi_x^*\Phi_y]=\delta_{xy}$ を得るのでisometryは直ちに従う。$m$ sampleで作るGram matrixは $m$ 本のsample vectorの積和なのでrankは高々 $m$ である。証明終。
<!-- theorem-end:proof -->

## AB.3 R213B：phase-tagged finite-Hamiltonian path carrier

回路中のHadamard数を $h$、path数を

```math
M=2^h
```

とする。path cell $r=1,\ldots,M$ にlogical rotors $(\theta_{rj},P_{rj})$、history rotors $(\eta_{rk},R_{rk})$、phase-tag rotor $(\phi_r,S_r)$ を置く。

hold potentialとして

```math
U_2(\theta)
=
K_2(1-\cos2\theta),
\qquad
U_8(\phi)
=
K_8(1-\cos8\phi)
```

を使い、logical wellsを $\theta=0,\pi$、phase wellsを

```math
\phi_r
=
\frac{\pi p_r}{4},
\qquad
p_r\in\mathbb Z_8
```

とする。smooth logical indicatorを

```math
b(\theta)
=
\frac{1-\cos\theta}{2}
```

とするとwell中心で $b=0,1$ かつ $b'=0$ である。

path-memory/phase hold Hamiltonianを

```math
H_{\rm mem}
=
\sum_{r,j}
\left[
\frac{P_{rj}^2}{2I_b}
+
U_2(\theta_{rj})
\right]
+
\sum_{r,k}
\left[
\frac{R_{rk}^2}{2I_b}
+
U_2(\eta_{rk})
\right],
```

```math
H_{\rm phase}
=
\sum_r
\left[
\frac{S_r^2}{2I_\phi}
+
U_8(\phi_r)
\right]
```

とする。gate window中は対象barrierをsmoothに下げ、conditional translationを作用させる。

T gate on $j$ には

```math
H_T(t)
=
v_T(t)
\sum_r
b(\theta_{rj})S_r,
\qquad
\int v_T(t)dt
=
\frac{\pi}{4}
```

を使う。CNOT $c\to t$ には

```math
H_{\rm CX}(t)
=
v_{\rm CX}(t)
\sum_r
b(\theta_{rc})P_{rt},
\qquad
\int v_{\rm CX}(t)dt
=
\pi
```

を使う。$k$ 番目Hadamardではfresh/history bit $\lambda_{rk}=b(\eta_{rk})$ に対し

```math
H_{H,\phi}(t)
=
v_{H,\phi}(t)
\sum_r
b(\theta_{rj})b(\eta_{rk})S_r,
\qquad
\int v_{H,\phi}(t)dt
=
\pi
```

でphaseを更新した後、三つのconditional translationで $(q_j,\lambda_k)$ をSWAPする。

<!-- theorem-start:theorem -->
**定理（R213B：H/T/CNOT phase-tagged path ruleの有限Hamiltonian lift）**

logical well中心、gate開始時の対象translation momentumを零とし、各windowでhold barrierを可逆に解除するideal logical manifoldでは、上のHamiltonian pulseは

```math
T:
\quad
p\mapsto p+q_j
\pmod 8,
```

```math
{\rm CNOT}:
\quad
q_t\mapsto q_t\oplus q_c,
```

```math
H:
\quad
(q_j,\lambda_k,p)
\mapsto
(\lambda_k,q_j,p+4q_j\lambda_k)
\pmod 8
```

を与える。Hadamard前の $q_j$ はhistory側へ保存されるため、この更新は可逆である。

control coordinateへの力は $b'(0)=b'(\pi)=0$ によりideal well中心で消え、finite-width defectはlogical leakage誤差へ分離できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R213B）**

例えばT gateでは $\dot\phi_r=S_r/I_\phi+v_Tb(\theta_{rj})$、$\dot S_r=0$ であり、$S_r=0$ とpulse areaから $\Delta\phi_r=(\pi/4)q_j$ を得る。CNOTも同様に $\Delta\theta_{rt}=\pi q_c$ を与える。Hadamardのphase pulseは $\Delta\phi_r=\pi q_j\lambda_k$ を与え、三CNOT型translationはSWAP恒等式を実現する。証明終。
<!-- theorem-end:proof -->

## AB.4 R213C：coherent terminal reductionとBorn-action port

回路終了時のpath cellにoutput label $Q_r\in\{0,1\}^n$ とphase tag $p_r\in\mathbb Z_8$ があるとする。量子path amplitudeを

```math
A_y
=
\frac1{\sqrt M}
\sum_{r:Q_r=y}
e^{i\pi p_r/4}
```

と定める。

各path cellに同一action $J_*$ のcoherent leaf oscillator $(I_r,\psi_r)$ を置く。固定carrier項を $\Omega_a I_r$ とし、8個のphase well上で

```math
f_8\left(\frac{k\pi}{4}\right)
=
\frac{k\pi}{4},
\qquad
f_8'\left(\frac{k\pi}{4}\right)
=
0,
\qquad
k=0,\ldots,7
```

を満たすsmooth periodic interpolation $f_8$ を一つ固定する。phase-copy windowを

```math
H_{\rm copy}(t)
=
g_{\rm copy}(t)
\sum_r
I_r f_8(\phi_r),
\qquad
\int g_{\rm copy}(t)dt=1
```

とする。Hamilton方程式は

```math
\dot\psi_r
=
\Omega_a
+
g_{\rm copy}(t)f_8(\phi_r),
\qquad
\dot I_r=0,
```

```math
\dot S_r
=
-
g_{\rm copy}(t)I_rf_8'(\phi_r)
```

である。従ってideal phase well中心では $f_8'=0$ によりtag側backreactionが消え、共通carrier phaseを除くleaf amplitudeは

```math
a_r
=
\sqrt{\frac{J_*}{\mathcal J_0}}
e^{i\pi p_r/4}
```

となる。output indicatorを

```math
\chi_y(Q_r)
=
\prod_{j=1}^n
\left[
y_jb(\theta_{rj})
+
(1-y_j)(1-b(\theta_{rj}))
\right]
```

とし、

```math
B_{yr}
=
\frac1{\sqrt M}\chi_y(Q_r)
```

と置く。

<!-- theorem-start:theorem -->
**定理（R213C：path-pair不要のcoherent Born-action reduction）**

ideal logical manifoldでは各pathはexactly one outputへ属するので

```math
BB^\dagger
=
{\rm diag}
\left(
\frac{m_y}{M}
\right)
\le I
```

であり、$B$ はcontractionである。従って有限unitary dilation $\mathcal U_B$ が存在し、有限Hermitian generator $K_B$ を

```math
\mathcal U_B
=
e^{-iK_B/\mathcal J_0}
```

と選べる。

path leavesと有限auxiliary/dark modesをまとめて $\mathbf z$ とし、

```math
H_{\rm coll}(t)
=
\mathbf z^\dagger
\left(
\mathcal J_0\Omega_c I
+
g_{\rm coll}(t)K_B
\right)
\mathbf z,
\qquad
\int g_{\rm coll}(t)dt=1
```

とする。$\Omega_c>\|K_B\|/\mathcal J_0$ と取ればcoherent quadratic sectorは下に有界である。

auxiliary inputを零とするとcollector outputは

```math
c_y
=
\frac1{\sqrt M}
\sum_{r:Q_r=y}a_r
=
\sqrt{\frac{J_*}{\mathcal J_0}}A_y
```

であり、そのactionは

```math
J_y
=
\mathcal J_0|c_y|^2
=
J_*|A_y|^2.
```

さらにunitary gate列に対応するpath ruleでは

```math
\sum_yJ_y
=
J_*.
```

従ってBorn weightは $4^h$ 個のpath-pair cellを用いず、coherent collector actionとして生成できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R213C）**

$BB^\dagger\le I$ なので例えばHalmos dilationにより有限unitary extensionが存在する。二次HamiltonianのHamilton方程式は rotating frame で $i\mathcal J_0\dot{\mathbf z}=g_{\rm coll}K_B\mathbf z$ となり、window終了時に $\mathbf z\mapsto\mathcal U_B\mathbf z$ を与える。上側blockが $B$ なので表示の $c_y$ を得る。action式は絶対値二乗から従う。証明終。
<!-- theorem-end:proof -->

collector actionを既存M66/R206へ渡すterminal local scaleは

```math
s_y
=
\delta
+
\frac{LJ_y}{J_*},
\qquad
L=2^n
```

とする。R212A型phase-volume portへは

```math
w_\delta(X,J)
=
\delta
+
\frac{L}{J_*}
\sum_y
\chi_y^X(X)J_y
```

として接続できる。readout Hamiltonianをcollector angle $\psi_y$ に依存させなければ

```math
\dot J_y
=
-\frac{\partial H_{\rm read}}{\partial\psi_y}
=
0
```

であり、terminal Born actionはQND型に保持される。

この接続はR212 thermal physical parentとR206 open/effective terminal samplerの既存責務を再利用する。R206 common-hub apparatus全体のfinite-Hamiltonian liftを本定理から推論しない。

## AB.5 R213D：robustness/resource auditとR186分離

<!-- theorem-start:proposition -->
**命題（R213D：analog signed collector obstructionとfinite-state/coherent carrierの資源境界）**

signed path contributionを

```math
F
=
g\sum_{r=1}^{N}X_r
```

というanalog busで集め、各cellに共通additive bias $b$ があるとする。真の平均を $m=N^{-1}\sum_rX_r$ とすると

```math
\frac{|\Delta F|}{|F|}
=
\frac{|b|}{|m|}
```

である。干渉により $|m|=2^{-O(d)}$ となるfamilyでは、一定relative accuracyのため $|b|\lesssim2^{-O(d)}$ が必要になり得る。従ってsigned analog summing busはcanonical R213 carrierとして採用しない。

一方、R213Bのlogical stateを有限well state、phase tagを $p\in\mathbb Z_8$ とし、R213Cのcollectorを有限depthのenergy-preserving unitary networkへ分解できる場合、各layerのoperator defectを $\epsilon_{\rm loc}$、network depthを $D$ とすれば標準telescoping boundから

```math
\|\widetilde U-U\|
\le
D\epsilon_{\rm loc}
+
O(D^2\epsilon_{\rm loc}^2).
```

従って $D={\rm poly}(n,d)$ なら $\epsilon_{\rm loc}^{-1}={\rm poly}(n,d,1/\epsilon)$ で十分であり、R186型の指数local precisionはこの誤差機構からは生じない。

代償として、素朴なrealizationでは

```math
N_{\rm path}
=
2^h,
\qquad
N_{\rm out}
=
2^n
```

までの受動内部cell/channel、ならびに指数的な装置体積、総coherent action、総bath容量、総static couplingを許す。これは現行Q2-4 resource contractで報告対象の内部受動資源であり、それだけではfixed-goal失敗としない。

strict 3D localityと有限伝播速度を追加要求すると、指数体積装置のdiameterによりcommunication timeが指数化する可能性があり、これは後続strengtheningとして残す。
<!-- theorem-end:proposition -->

## AB.6 一本のcandidate Hamiltonianと未閉包項

以上をまとめ、M67 Q2/NBL candidate profileを

```math
H_{67}^{\rm NBL}(t)
=
H_{\rm mem}
+
H_{\rm phase}
+
H_{\rm gate}(t)
+
H_{\rm copy}(t)
+
H_{\rm coll}(t)
+
H_{\rm read}
```

とする。$H_{\rm gate}=H_T+H_{\rm CX}+H_{H,\phi}+H_{H,\rm swap}$ であり、$H_{\rm read}$ はR212/M66 thermal-sector terminal specializationを用いる。

R213A--R213Dから本付録が閉じるのは、NBL/path state-space、H/T/CNOT path ruleのfinite-Hamiltonian candidate、path-pair不要のcoherent Born-action reduction、R186型local precision再発の監査までである。

未閉包項は次である。

- 抽象generator $K_B$ を固定50:50 combiner、controlled router、bounded-degree/local couplingだけからなる明示networkへ分解し、そのdepthと誤差をpolyに抑えること。
- R206 common-hub apparatus全体を有限Hamiltonianへ持ち上げ、$L=2^n$ に依存しないeffective mixing boundをphysical parentから回収すること。
- strict spatial localityと有限伝播速度まで要求した場合の指数装置径問題。
- 上記を閉じた後のM54/R181B--R181C退役、R186主線解除、Q2-4達成ラベル再判定。

従ってR213A--R213Dは本PRではpromotion-ready candidateとして扱い、Q2-4の現行fixed-goal直接依存を置換しない。
