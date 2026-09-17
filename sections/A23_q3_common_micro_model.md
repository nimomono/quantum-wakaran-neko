@number: W
@chapter: 付録
@title: M60 Duffing--統一二成分chiral媒体 Q3共通ミクロ模型
@status: Q3-1/Q3-2の共通ミクロ物理層。M59の実2-mode Duffing shellは維持し、独立していた二成分DNLS action reservoirとdual ballistic waveguideを同一の二成分非線形Hamiltonian媒体のnonlinear coreとballistic leadへ統合する。R198Dのcore mixing/homogenizationとR199Aのcore--lead同時parameter witnessはQ3-1-A1/Q3-2-A1の残件とする。

## W.1 M60の責務と実在自由度

Q3-1とQ3-2の共通親模型をM60とする。M60はM37をsignal subsystemとして同一試行上に含み、tracer $X$ に付随する2つの実Duffing内部自由度を、一つの二成分非線形chiral媒体へ局所結合する。M59で別の物理実体として置いていた二成分DNLS reservoirとdual ballistic waveguideは、M60では同じ媒体の異なる空間sector・時間尺度として扱う。

単一試行で物理的に存在する自由度は、M37の有限実振動子座標、tracerに付随する2つの実Duffing正準対 $(q_\sigma,p_\sigma)$、$\sigma=\pm$、二成分chiral媒体の実正準対、moving bath-frame carrier $Y_e$、その内部の平衡oscillator bath、1個のtracer位置 $X$、periodic/double-well potentialである。複素記号 $Z$、$a_\sigma$、$b_{\sigma n}$ は実正準平面をまとめる派生表示であり独立実体ではない。

M60では同じM37信号を開始時からDuffing shellとchiral媒体のsignal portへ弱く結合し、同じtracer $X_t$ を最後まで発展させる。signalを後段で再標本化しない。Brownian noiseとFDTはchiral媒体ではなく、$Y_e$ と共に並進する通常の平衡oscillator bathが担う。時計、終位置record、resetまで含む反復周期統合は本付録の責務に含めない。

全体系を概念的に

```math
H_{60}=H_{37}+H_X+H_{\rm D}+H_\chi+H_{\rm D\chi}+H_{37\chi}+H_{\rm eq}
```

と書く。$H_X=P_X^2/(2M_X)+V_{\rm per}(X)$、$H_{\rm eq}$ は付録Vの平衡oscillator bathである。M60の新規部分は $H_\chi$ がreservoirとballistic transportを兼ねる点にある。

## W.2 M37信号、current辞書、smooth capacity

1次元最近接格子でM37の目標生成子を

```math
h_L=\frac{\mathcal J_0^2}{2m}L_G+V_L
```

とし、最近接重みを $g_{i,i+1}=a^{-2}$ とする。Nelson matching

```math
\mathcal J_0=2m\nu
```

を採用する。M37局所実正準座標から得る $Z_i$ に対し、辺 $e=\{i,j\}$ ごとに

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。これは固定線形正準結合であり、state-dependent divisionや位相測定を必要としない。R195Aにより

```math
I_{e,+}+I_{e,-}=|Z_i|^2+|Z_j|^2,
```

```math
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j),
```

```math
J_{ij}^{\rm sig}=\frac{\nu}{a^2}(I_{e,+}-I_{e,-})
```

が厳密に成り立つ。

well中心 $x_i$ に対する周期的 $C^3$ partition of unity $\chi_i$ を取り、

```math
r^\delta(x,z)
=\sum_i\chi_i(x)
\left(|z_i|^2+\delta q_i\bar S_{\rm ref}\right)
```

とする。safe sectorで

```math
0<r_{\min}\le r^\delta(x,z)\le r_{\max}<\infty
```

を仮定し、

```math
A(x,z)=\bar\alpha r^\delta(x,z)
```

と置く。

## W.3 R198A：実2-mode Duffingから2-action shell

tracerに付随する実正準自由度を $(q_\sigma,p_\sigma)$、$\sigma=\pm$ とし、

```math
H_{\rm D}^{(\varepsilon)}=H_0+\varepsilon V
```

```math
H_0=\sum_{\sigma=\pm}
\left[\frac{p_\sigma^2}{2m_\sigma}+\frac12m_\sigma\omega_\sigma^2q_\sigma^2\right]
```

```math
V=\sum_{\sigma=\pm}\frac{\bar\alpha_\sigma}{4}q_\sigma^4
+\frac{\bar\beta}{2}q_+^2q_-^2
-A\sum_{\sigma=\pm}\bar g_\sigma q_\sigma^2
+\frac{\kappa_{\rm sh}}2A^2
```

とする。最後の $A^2$ は全Hamiltonianではsignal側countertermへ移しても等価である。線形振動子のaction-angle変数を $(K_\sigma,\theta_\sigma)$ とし、

```math
S=K_++K_-
```

と置く。

<!-- theorem-start:theorem -->
**定理（R198A：非共鳴2-mode Duffingから2-action shellへの有限時間縮約）**

safe sector $S\le S_*$、$A\in[A_{\min},A_{\max}]$ で必要な微分が有界とする。ある $\gamma>0$ に対し

```math
\omega_\sigma\ge\gamma,
\qquad
|\omega_+-\omega_-|\ge\gamma
```

を仮定する。また

```math
\frac{3\bar\alpha_\sigma}{8m_\sigma^2\omega_\sigma^2}=\frac{\kappa_{\rm sh}}2,
```

```math
\frac{\bar\beta}{2m_+m_-\omega_+\omega_-}=\kappa_{\rm sh},
\qquad
\frac{\bar g_\sigma}{m_\sigma\omega_\sigma}=\kappa_{\rm sh}
```

を理想係数条件とする。このときnear-identity canonical transformationが存在し、$0\le t\le T/\varepsilon$ で

```math
\widetilde H_{\rm D}^{(\varepsilon)}
=\omega_+K_++\omega_-K_-
+\varepsilon\frac{\kappa_{\rm sh}}2[S-A]^2
+\varepsilon^2R_A,
```

```math
\|R_A\|_{C^1}\le \frac{C_A}{\gamma}.
```

係数ずれを $\varepsilon_{\rm coef}$ とすれば

```math
H_{\rm slow}=\frac{\kappa_{\rm sh}}2(S-A)^2
+O(\varepsilon/\gamma)+O(\varepsilon_{\rm coef}).
```
<!-- theorem-end:theorem -->

R198AはM59から責務を変えない。M60初版では完全縮退CW/CCW pairを仮定せず、弱くsplitした2つの内部modeをchiral媒体の $\pm$ branchへ選択的に結合する。

## W.4 M60二成分chiral媒体

媒体の実正準対を複素略記 $b_{\sigma n}$、$\sigma=\pm$ で表す。有限core $\mathcal C$ と左右へ延びるlead $\mathcal L$ を同じ格子上に取り、

```math
H_\chi=H_{\rm lin}+H_{\rm nl}
```

```math
H_{\rm lin}
=\sum_{\sigma,n}\Omega_\sigma|b_{\sigma n}|^2
-iJ\sum_n(b_{+,n+1}^*b_{+,n}-b_{+,n}^*b_{+,n+1})
+iJ\sum_n(b_{-,n+1}^*b_{-,n}-b_{-,n}^*b_{-,n+1})
```

```math
H_{\rm nl}
=\sum_n w_n
\left[
\frac{g_+}{2}|b_{+,n}|^4
+\frac{g_-}{2}|b_{-,n}|^4
+g_{+-}|b_{+,n}|^2|b_{-,n}|^2
\right]
```

とする。$w_n=1$ をnonlinear core、$w_n\simeq0$ をballistic leadとする。$\Omega_\sigma>2|J|$ として線形周波数を正に保つ。leadでの線形分散は

```math
\omega_\pm(k)=\Omega_\pm\pm2J\sin k
```

なので、$k=0$ 近傍の狭帯域packetは

```math
v_{g,+}=+2Ja+O(k^2a),
\qquad
v_{g,-}=-2Ja+O(k^2a)
```

を持つ。従って

```math
c=2Ja
```

をM60 leadの中心伝播速度とする。

$H_{\rm nl}$ と $H_{\rm lin}$ は各成分の独立位相対称性を保ち、閉じたcore基準系では

```math
Q_\sigma=\sum_{n\in\mathcal C}|b_{\sigma n}|^2
```

を別々に保存する。

M37から媒体leadへのpassive portを

```math
H_{37\chi}
=-\epsilon_p\sum_{e,\sigma}
\left[C_{e,\sigma}^*b_{\sigma,n(e)}+{\rm c.c.}\right]
```

とする。shellとcoreの局所交換結合は、$a_\sigma=\sqrt{K_\sigma}e^{i\theta_\sigma}$ を用いて

```math
H_{\rm D\chi}
=-\sum_{\sigma=\pm}\lambda_\sigma
\left[a_\sigma^*B_\sigma(X)+a_\sigma B_\sigma(X)^*\right],
```

```math
B_\sigma(X)=\sum_{n\in\mathcal C}\eta_n(X)b_{\sigma n},
\qquad
\sum_n|\eta_n(X)|^2=1
```

とする。$\eta_n$ はtracer近傍を滑らかに選ぶlocal form factorである。

## W.5 R198B：M60 nonlinear coreからGibbs shellへの縮約

$\epsilon_p=0$、lead interfaceを閉じた基準coreの状態密度を $\Omega_N(E,Q_+,Q_-)$、entropy densityを

```math
\sigma_N(e,q_+,q_-)=\frac1N\log\Omega_N(Ne,Nq_+,Nq_-)
```

とする。

<!-- theorem-start:theorem -->
**定理（R198B：二保存action nonlinear coreからM60 Gibbs shellへの縮約）**

基準点で

```math
\beta_N=\partial_e\sigma_N>0,
\qquad
-\beta_N\mu_{\sigma,N}=\partial_{q_\sigma}\sigma_N
```

と定義する。safe sectorを含む近傍で $\sigma_N\in C^2$、$\|D^2\sigma_N\|_{\rm op}\le M_2$ とし、carrier matching

```math
\mu_{+,N}=\omega_+,
\qquad
\mu_{-,N}=\omega_-
```

を課す。このときzero-exchange microcanonical shell marginalと

```math
dP_A^{\rm G}
\propto
\exp\left[-\frac{\beta_N\kappa_{\rm sh}}2(S-A)^2\right]
1_{S\le S_*}
\,dK_+dK_-d\theta_+d\theta_-
```

の間に

```math
\|P_{N,A}^{\rm mc}-P_A^{\rm G}\|_{\rm TV}
\le\frac12\left(e^{2\delta_N}-1\right),
```

```math
\delta_N=\frac{M_2}{2N}(H_*^2+S_*^2)
```

が成り立つ。従って有限core誤差は $O(N^{-1})$ である。また

```math
dK_+dK_-=S\,dSdu,
\qquad
K_+=uS,
\qquad
K_-=(1-u)S
```

より

```math
\pi_A(S)\propto S\exp\left[-\frac{\beta_N\kappa_{\rm sh}}2(S-A)^2\right].
```
<!-- theorem-end:theorem -->

証明はM59 R198Bのentropy Taylor展開と同じであり、reservoirの成分ラベルをM60のchiral branchへ読み替える。

## W.6 R198C：shell--core有限交換結合

<!-- theorem-start:theorem -->
**定理（R198C：M60弱交換結合の偶数次mean-force補正）**

R198Bのregular sectorで、$B_\sigma(X)$ の4次までのmicrocanonical cumulantと必要なenergy derivativeが一様有界であり、finite-coupling shell marginalが $\lambda_\sigma=0$ の近傍で4次まで解析的とする。独立位相対称性により奇数次補正は消える。局所action

```math
m_{\sigma,N}(X)=\langle|B_\sigma(X)|^2\rangle_{\rm mc}
```

を用いると、二次carrier shiftはbare chemical potentialの再較正で吸収でき、残るstatic exchange誤差は

```math
\varepsilon_{\rm ex}
=O(\lambda^4)+O(\lambda^2/N)+\varepsilon_{\rm loc}
```

である。$\varepsilon_{\rm loc}$ は $X$ 依存form factorのslow variationが生む有限時間局所化誤差である。
<!-- theorem-end:theorem -->

R198Cの位相平均による奇数次消失と二次mean-force補正はM59から継承する。

## W.7 R198D：nonlinear coreの有限時間mixing

R198DはM60系列で具体的coreのmixingを仮定として残す。有限孤立Hamiltonian系はPoincare recurrenceを持つため、$t\to\infty$ の不可逆収束を主張せず、有限観測窓だけを扱う。

core境界observableを $B_\sigma(t)$、平衡相関を $C_{\sigma\tau}(t)$ とする。

<!-- theorem-start:theorem -->
**定理（R198D：M60 nonlinear coreによる有限時間thermalization）**

R198A--R198Cを仮定する。さらに選んだ正温度・非凝縮core sectorで境界observableの相関と必要な高次cumulantが一様に可積分で、例えば

```math
\int_0^\infty(1+t)|C_{\sigma\tau}(t)|dt<\infty
```

を満たすとする。$\lambda_\sigma=\lambda\bar\lambda_\sigma$、slow time $\tau=\lambda^2t$ を取る。有限kinetic intervalで真のHamiltonian shell marginalがreversible effective diffusionへ

```math
d_{\rm BL}(P_t^{\rm true},P_\tau^{\rm eff})
\le\varepsilon_{\rm hom}(\lambda,N,T)
```

で近づき、joint weak-coupling/large-core limitで $\varepsilon_{\rm hom}\to0$ と仮定する。effective generatorのM60 Gibbs measureに対するspectral gapが $g_A\ge g_*>0$ なら、frozen $A$ について

```math
d_{\rm BL}(P_t^{\rm true},P_A^{\rm G})
\le C_0e^{-g_*\lambda^2t}
+\varepsilon_{\rm hom}
+O(N^{-1})+\varepsilon_{\rm ex}.
```

時間依存 $A(t)$ ではさらに

```math
C_{\rm ad}\frac{\sup|\dot A|}{g_*\lambda^2}
```

を加える。
<!-- theorem-end:theorem -->

R198DはM60 nonlinear coreが全parameter領域でergodicであるとは主張しない。具体的mixing/homogenization witnessはQ3-1-A1/Q3-2-A1の残件である。

## W.8 R199A：同一chiral媒体のcore--ballistic lead接続

M60ではreservoirとtransportを同じ $b_{\pm n}$ 媒体が担うため、nonlinear coreを平衡reservoirとして使う時間窓とballistic leadをcurrent carrierとして使う時間窓が同時に非空であることを別に管理する。

<!-- theorem-start:theorem -->
**定理（R199A：M60 nonlinear-core / ballistic-lead有限時間分離）**

leadで $|w_n|\le w_{\rm L}\ll1$ とし、各 $\sigma$ のpacketが $k=0$ を中心とする幅 $\Delta k\ll1$ に支持されるとする。core--lead interfaceの反射振幅を $\varepsilon_{\rm int}$、lead非線形位相ずれを $\varepsilon_{\rm nl}$、signal port強度を $\epsilon_p$ とする。固定有限時間 $0\le t\le T$ で、port観測面のincident energy densityは

```math
e_{e,\sigma}(t)
=\kappa_p I_{e,\sigma}(t-\tau_p)
+\delta e_{e,\sigma}(t),
```

```math
\sup_{t\le T}|\delta e_{e,\sigma}(t)|
\le C_p I_*
\left[
(\Delta k)^2T
+\varepsilon_{\rm int}
+\varepsilon_{\rm nl}T
+\varepsilon_{\rm back}
\right],
```

```math
\varepsilon_{\rm back}=O(\epsilon_p^2T).
```

さらにcore容量を $N$ とし、固定時間内にleadへ流出入する総actionが $O(\epsilon_p^2TI_*)$ なら、core intensive variableのdriftは

```math
\varepsilon_{\rm drive}
\le C_{\rm drive}\frac{\epsilon_p^2TI_*}{N}.
```

従って

```math
\tau_R\ll\tau_{\rm therm}\ll\tau_A,
\qquad
\tau_p\ll T_{\rm sig},
```

かつ上の4誤差が同時に小さいparameter windowでは、同一M60媒体をR198B--R198DのreservoirとR196Aへのballistic inputに同時使用できる。
<!-- theorem-end:theorem -->

lead分散のTaylor展開、Duhamel評価、有限action fluxのextensive coreへの影響から上式を得る。R199Aは具体的core mixingそのものを証明せず、その責務はR198Dに残す。

## W.9 R199B：local Duffing pairのchiral response

R199BはM60の統合強化であり、Q3-2固定達成の必須依存にはしない。左右branchからshellへ入る弱いchiral biasが、同じ2-action pairにcurrent情報を保持できることを整理する。

```math
D=K_+-K_-,
\qquad
S=K_++K_-,
\qquad
r=\frac{I_+-I_-}{I_++I_-}.
```

<!-- theorem-start:theorem -->
**定理（R199B：交換対称local shellの奇偶応答）**

balanced point $I_+=I_-$ の近傍でshellのstationary familyが $r$ に解析的で、$+\leftrightarrow-$ 交換が $r\mapsto-r$ と同値であるとする。このとき

```math
F(r)=\left\langle\frac DS\right\rangle_r
```

は奇関数、任意の交換対称radial observableの平均は偶関数である。従って

```math
F(r)=\chi_1r+\chi_3r^3+O(r^5),
```

radial marginalのbalanced分布からの変化は $O(r^2)$ である。固定装置較正で $\chi_1=1$ とすれば

```math
\left\langle\frac DS\right\rangle
=r+O(r^3).
```

smooth sector $r=O(a)$ では、これをcurrent velocity $2\nu F(r)/a$ へ換算した誤差は $O(a^2)$、Born型state-countへのchiral補正はrelative $O(a^2)$ である。
<!-- theorem-end:theorem -->

R199Bは外部で $j/\rho$ を計算する機構を導入しない。入力は対応する二本のbranchへの固定Hamiltonian couplingだけであり、$r$ は解析上の応答変数としてのみ用いる。

## W.10 R197A：Gibbs shellの平均力

R198A--R198Dが到達するtarget Gibbs shell自体の積分恒等式はM59から独立なので維持する。

<!-- theorem-start:theorem -->
**定理（R197A：2-action Gibbs shellの平均力と有限幅誤差）**

```math
x(A)=\sqrt{\frac{\beta\kappa_{\rm sh}}2}A,
```

```math
\Delta(x)=\frac{e^{-x^2}}{e^{-x^2}+\sqrt\pi x[1+\operatorname{erf}(x)]}
```

と置く。target shell

```math
\pi_A(S)=\frac1{\mathcal Z_A}S\exp\left[-\frac{\beta\kappa_{\rm sh}}2(S-A)^2\right]
```

に対する $G_A(S)=\kappa_{\rm sh}(S-A)$ の平均は

```math
\bar G(A)=\frac{k_BT}{A}[1-\Delta(x(A))].
```

従って任意のslow座標 $y$ について

```math
\bar F_y^{\rm sh}
=k_BT[1-\Delta(x(A))]\partial_y\log r^\delta.
```

$x_{\min}=x(A_{\min})$、$\Delta_*=\Delta(x_{\min})$ とすると

```math
|\bar F_y^{\rm sh}-k_BT\partial_y\log r^\delta|
\le k_BT\Delta_*|\partial_y\log r^\delta|.
```

従って条件付き自由エネルギーは共通加法定数を除き

```math
F_{\rm sh}=-k_BT\log r^\delta+E_{\rm width}.
```
<!-- theorem-end:theorem -->

## W.11 R197C：M60負荷下のM37有限時間安定性

R198Dから得るcentered forceの有限相関積分を $C_G$ とする。shell平均力、有限相関fluctuation、M60 port backreaction、core--lead誤差をそれぞれ $\varepsilon_{\rm shell}$、$\varepsilon_{\rm fluc}$、$\varepsilon_{\rm back}$、$\varepsilon_{\rm lead}$ で評価する。

<!-- theorem-start:theorem -->
**定理（R197C：M60負荷下のM37有限時間安定性）**

R86、R196A--R196C、R198A--R198D、R199Aのsafe-sector仮定を同時に満たすとする。固定有限時間 $T$ で

```math
\varepsilon_{\rm sig}^{60}(T)
\le\varepsilon_{\rm car}(T)
+C_{\rm sig}(T)
\left(
\varepsilon_{\rm shell}
+\varepsilon_{\rm fluc}
+\varepsilon_{\rm back}
+\varepsilon_{\rm lead}
\right),
```

```math
\varepsilon_{\rm fluc}\le C_{\rm load}\sqrt{2TC_G}.
```

従ってR198Dのmixing windowとR199Aのcore--lead windowが同時に非空なら、M60 signal marginalはR86へ有限誤差で縮約する。
<!-- theorem-end:theorem -->

## W.12 共通誤差台帳とR161/R185への接続

M60 shell/core誤差を

```math
\varepsilon_{\rm shell}^{60}
=\varepsilon_{\rm av}
+\varepsilon_{\rm coef}
+\frac{C_N}{N}
+\varepsilon_{\rm ex}
+\varepsilon_{\rm hom}
+C_{\rm th}e^{-g_*\lambda^2t}
+C_{\rm ad}\frac{\sup|\dot A|}{g_*\lambda^2}
+\varepsilon_\mu
```

とし、transport側に

```math
\varepsilon_{\chi}
=\varepsilon_{\rm lead}
+\varepsilon_{\rm int}
+\varepsilon_{\rm nl}
+\varepsilon_{\rm drive}
+\varepsilon_{\rm back}
```

を加える。

<!-- theorem-start:theorem -->
**定理（R197：M60 Q3-1/Q3-2共通ミクロ模型の条件付き有限時間統合）**

R86、R195A、R196A--R196C、R198A--R198D、R199A、R197A、R197Cの仮定を同時に満たし、固定有限時間のsafe sectorで $r^\delta\ge r_{\min}>0$ とする。このとき同一のM60古典Hamiltonian/open-tracer過程について次が成り立つ。

1. signal marginalはR86のSchrodinger型空間信号へ誤差 $\varepsilon_{\rm sig}^{60}$ で縮約する。
2. shellを周辺化した平均力は $k_BT\partial_x\log r^\delta$ にR197Aのfinite-width誤差と $\varepsilon_{\rm shell}^{60}$ を加えた範囲で一致する。
3. 同じM60 chiral媒体のballistic leadをR196Aへ入力すると、R196A--R196Cを通じてwell-index生成子はR161へ有限誤差で一致する。
4. R161のcanonical path lawにはR185を適用でき、時間対称Newton則に残る誤差はM60からR161への持上げ誤差、R185の正則化残差、格子残差である。

従ってR198Dのmixing/homogenization仮定とR199Aのcore--lead同時windowが満たされる範囲で、Q3-1とQ3-2は同一M60過程の異なる周辺縮約として実現される。R199Bは同じDuffing pairへcurrent情報も保持できることを示す統合強化であり、本定理の必須依存には含めない。
<!-- theorem-end:theorem -->

## W.13 責務境界

R198Aは実Duffing自由度からaction shellを導く。R198BはM60 nonlinear coreの平衡周辺化、R198Cはshell--core有限交換結合、R198Dはcoreの有限時間thermalizationを担当する。R199Aは同一媒体をnonlinear reservoirとballistic carrierへ同時使用できる有限時間windowを担当し、R199Bはlocal 2-action pairのchiral responseを統合強化として整理する。R196A以降のmoving bath-frame、equilibrium bath、tracer GLE、R161/R185は付録V以降の既存経路を維持する。

固定目標Q3-1/Q3-2の既存達成ラベルは変更しない。Q3-1-A1/Q3-2-A1は部分達成のままとし、R198Dの具体的core mixing witnessとR199Aのcore--lead同時parameter witnessを残件とする。A2ではM60のDuffing＋統一chiral媒体＋moving bath-frame＋equilibrium bathを直接数値計算する。