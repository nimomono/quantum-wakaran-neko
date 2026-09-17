@number: W
@chapter: 付録
@title: M59 Duffing--二保存action reservoir Q3共通ミクロ模型
@status: Q3-1/Q3-2の共通ミクロ物理層。旧M58のthermostatted 2-action shellを退役し、実2-mode Duffing内部自由度、二成分DNLS action reservoir、弱交換結合、有限時間mixingから同じGibbs shellを導く。R198Dの有限時間mixingは明示条件付き定理であり、Q3-1-A1/Q3-2-A1の残件とする。

## W.1 M59の責務と実在自由度

Q3-1とQ3-2の共通親模型候補をM59とする。M59はM37をsignal subsystem、M57をtransport subsystemとして同一試行上に含み、旧M58で直接仮定していたshell Langevin SDEを、Hamiltonian内部自由度とaction reservoirから導く。

単一試行で物理的に存在する自由度は、M37の有限実振動子座標、shellの2つの実Duffing正準対 $(q_r,p_r)$、二成分reservoirの実正準対、辺ごとの二本のballistic wave channel、moving bath-frame carrier $Y_e$、その内部の平衡oscillator bath、1個のtracer位置 $X$、periodic/double-well potentialである。複素記号 $Z$、$a_r$、$b_{rj}$ は実正準平面をまとめる派生表示であり独立実体ではない。

M59ではsignalをM37からM57へ後段で再標本化しない。開始時から同じM37信号がDuffing shellとballistic portへ弱く結合し、同じtracer $X_t$ が最後まで発展する。時計、終位置record、resetまで含む反復周期統合は本付録の責務に含めない。

旧M58で採用した $S$ への直接Langevin SDE、$u$ の反射Brownian motion、角の直接拡散、およびそれらに専用の旧R197Bは現行主線から退役する。旧M58のGibbs shellは、以下ではR198A--R198Dの有効周辺分布として再導出する。

## W.2 M37信号、M57 current辞書、smooth capacity

1次元最近接格子でM37の目標生成子を

```math
h_L=\frac{\mathcal J_0^2}{2m}L_G+V_L
```

とし、最近接重みを $g_{i,i+1}=a^{-2}$ とする。Nelson matching

```math
\mathcal J_0=2m\nu
```

を採用すると、M37の辺成分はM57のsignal current辞書と一致する。M37局所実正準座標から得る $Z_i$ に対し、

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2}
```

は固定線形正準結合であり、state-dependent divisionや位相測定を必要としない。

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

と置く。従って $A_{\min}=\bar\alpha r_{\min}>0$、$A_{\max}=\bar\alpha r_{\max}$ である。

## W.3 R198A：2-mode Duffingから2-action shell

shellの実正準自由度を $(q_r,p_r)$、$r=1,2$ とし、

```math
H_{\rm D}^{(\varepsilon)}=H_0+\varepsilon V
```

```math
H_0=\sum_{r=1}^2\left[\frac{p_r^2}{2m_r}+\frac12m_r\omega_r^2q_r^2\right]
```

```math
V=\frac{\bar\alpha_1}{4}q_1^4+\frac{\bar\alpha_2}{4}q_2^4
+\frac{\bar\beta}{2}q_1^2q_2^2
-A\left(\bar g_1q_1^2+\bar g_2q_2^2\right)
+\frac{\kappa_{\rm sh}}2A^2
```

とする。$A=A(\varepsilon t)$ はslow variableである。線形振動子のaction-angle変数を $(K_r,\theta_r)$ とし、$S=K_1+K_2$ と置く。

<!-- theorem-start:theorem -->
**定理（R198A：非共鳴2-mode Duffingから2-action shellへの有限時間縮約）**

safe sector $S\le S_*$、$A\in[A_{\min},A_{\max}]$ で必要な微分が有界とする。ある $\gamma>0$ に対し

```math
\omega_r\ge\gamma,
\qquad
|\omega_1-\omega_2|\ge\gamma
```

を仮定する。また

```math
\frac{3\bar\alpha_r}{8m_r^2\omega_r^2}=\frac{\kappa_{\rm sh}}2,
\qquad
\frac{\bar\beta}{2m_1m_2\omega_1\omega_2}=\kappa_{\rm sh},
```

```math
\frac{\bar g_r}{m_r\omega_r}=\kappa_{\rm sh}
```

を理想係数条件とする。このときnear-identity canonical transformationが存在し、$0\le t\le T/\varepsilon$ で

```math
\widetilde H_{\rm D}^{(\varepsilon)}
=\omega_1K_1+\omega_2K_2
+\varepsilon\frac{\kappa_{\rm sh}}2[S-A]^2
+\varepsilon^2R_A,
```

```math
\|R_A\|_{C^1}\le \frac{C_A}{\gamma}
```

と書ける。係数を理想値からずらした場合も、safe sector上の平均Hamiltonian誤差を $\varepsilon_{\rm coef}$ とすれば

```math
H_{\rm slow}
=\frac{\kappa_{\rm sh}}2(S-A)^2
+O(\varepsilon/\gamma)+O(\varepsilon_{\rm coef})
```

である。完全縮退 $\omega_1=\omega_2$ は仮定せず、1:1 resonant angle termは非共鳴条件で平均除去する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R198A）**

```math
q_r=\sqrt{\frac{2K_r}{m_r\omega_r}}\cos\theta_r
```

を用いると、角平均は

```math
\langle q_r^4\rangle=\frac{3K_r^2}{2m_r^2\omega_r^2},
\qquad
\langle q_1^2q_2^2\rangle=\frac{K_1K_2}{m_1m_2\omega_1\omega_2},
```

```math
\langle q_r^2\rangle=\frac{K_r}{m_r\omega_r}
```

である。理想係数条件を代入すれば一次平均は $\kappa_{\rm sh}(S-A)^2/2$ となる。非平均Fourier成分のsmall denominatorは非共鳴条件で $\gamma$ により下から抑えられるので、一次Lie transformと標準有限時間averagingで表示式を得る。証明終。
<!-- theorem-end:proof -->

## W.4 R198B：二保存action有限reservoir

reservoirを二成分DNLS型Hamiltonian

```math
H_R^{(N)}
=\sum_{r=1}^2\sum_{j=1}^N
\left[\Omega_r|b_{rj}|^2+\frac{g_r}{2}|b_{rj}|^4\right]
-\sum_{r=1}^2J_r\sum_j(b_{rj}^*b_{r,j+1}+{\rm c.c.})
+g_{12}\sum_j|b_{1j}|^2|b_{2j}|^2
```

とする。ここで複素振幅は実正準対の略記である。独立位相対称性により

```math
Q_r=\sum_j|b_{rj}|^2
```

が別々に保存される。成分間の線形mode-conversion項は置かない。

状態密度を $\Omega_N(E,Q_1,Q_2)$、entropy densityを

```math
\sigma_N(e,q_1,q_2)=\frac1N\log\Omega_N(Ne,Nq_1,Nq_2)
```

とする。

<!-- theorem-start:theorem -->
**定理（R198B：二保存action有限reservoirからM59 Gibbs shellへの縮約）**

基準点で

```math
\beta_N=\partial_e\sigma_N>0,
\qquad
-\beta_N\mu_{r,N}=\partial_{q_r}\sigma_N
```

と定義する。shellが取り得るsafe sectorを含む近傍で $\sigma_N\in C^2$、

```math
\|D^2\sigma_N\|_{\rm op}\le M_2
```

とする。$|H_{\rm sh}|\le H_*$、$S\le S_*$ とし、carrier matching

```math
\mu_{1,N}=\omega_1,
\qquad
\mu_{2,N}=\omega_2
```

を課す。このときzero-exchange microcanonical shell marginal $P_{N,A}^{\rm mc}$ と

```math
dP_A^{\rm G}
\propto
\exp\left[-\frac{\beta_N\kappa_{\rm sh}}2(S-A)^2\right]
1_{S\le S_*}
\,dK_1dK_2d\theta_1d\theta_2
```

の間に

```math
\|P_{N,A}^{\rm mc}-P_A^{\rm G}\|_{\rm TV}
\le\frac12\left(e^{2\delta_N}-1\right),
```

```math
\delta_N=\frac{M_2}{2N}(H_*^2+S_*^2)
```

が成り立つ。従って有限reservoir誤差は $O(N^{-1})$ である。target measureでは

```math
dK_1dK_2=S\,dSdu
```

より

```math
\pi_A(S)\propto S\exp\left[-\frac{\beta_N\kappa_{\rm sh}}2(S-A)^2\right].
```

有限 $N$ の真のmicrocanonical marginalでは $u$ の一様性は一般に $O(N^{-1})$ だけ歪む。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R198B）**

```math
N\sigma_N\left(e_0-\frac hN,q_{10}-\frac{k_1}N,q_{20}-\frac{k_2}N\right)
```

を基準点でTaylor展開すると、一次項は

```math
-\beta_Nh+\beta_N\mu_{1,N}k_1+\beta_N\mu_{2,N}k_2
```

である。R198Aのcarrier項とmatching条件が相殺し、残りは $-\beta_N\kappa_{\rm sh}(S-A)^2/2$ になる。二次剰余は $\delta_N$ 以下である。Radon--Nikodym比を上下から $e^{\pm2\delta_N}$ で挟めば表示式を得る。証明終。
<!-- theorem-end:proof -->

## W.5 R198C：有限交換結合とmean-force較正

shellの複素正準略記を $a_r=\sqrt{K_r}e^{i\theta_r}$ とし、reservoir境界modeへ

```math
H_{\rm ex}
=-\sum_{r=1}^2\lambda_r(a_r^*b_{r\ell_r}+a_rb_{r\ell_r}^*)
```

で接続する。この結合は独立位相対称性を保つため、全体系で

```math
\mathcal Q_r=K_r+Q_r
```

を厳密保存する。

<!-- theorem-start:theorem -->
**定理（R198C：弱交換結合の偶数次mean-force補正）**

R198Bのregular sectorで、境界modeの4次までのmicrocanonical cumulantと必要なenergy derivativeが一様有界であり、finite-coupling shell marginalが $\lambda_r=0$ の近傍で4次まで解析的とする。独立位相対称性により奇数次補正は消える。局所action

```math
m_{r,N}=\langle|b_{r\ell_r}|^2\rangle_{\rm mc}
```

を用いると、二次補正は

```math
\log\frac{dP_{N,\lambda}}{dP_{N,0}}
=\sum_r\beta_N^2\lambda_r^2m_{r,N}K_r
+R_C-\log Z_C,
```

```math
|R_C|\le
C_C\left[\frac{\lambda_1^2+\lambda_2^2}{N}S_*
+(\lambda_1^2+\lambda_2^2)^2S_*^2\right]
```

と評価できる。従ってbare chemical potentialを

```math
\mu_{r,N}^{\rm bare}
=\omega_r-\beta_N\lambda_r^2m_{r,N}
```

に再較正すれば、二次carrier shiftは吸収され、残るfinite-exchange誤差は $O(\lambda^4)+O(\lambda^2/N)$ である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R198C）**

交換observable $Y_r=a_r^*b_{r\ell_r}+a_rb_{r\ell_r}^*$ を用いてmicrocanonical energy constraintを $\lambda_r$ で展開する。位相対称性から $\langle Y_r\rangle=0$、異成分の一次cross termも零である。また

```math
\langle Y_r^2\rangle=2K_rm_{r,N}.
```

従って最初の非零項は二次であり、entropyのenergy derivativeを用いるとleading termは $\beta_N^2\lambda_r^2m_{r,N}K_r$ となる。仮定した4次cumulant boundとfinite-$N$ derivative boundが剰余評価を与える。証明終。
<!-- theorem-end:proof -->

## W.6 R198D：有限時間mixing

R198DはM59系列で唯一、具体的DNLS reservoirのmixingを仮定として残す。有限孤立Hamiltonian系はPoincare recurrenceを持つため、$t\to\infty$ の不可逆収束は主張せず、有限観測窓だけを扱う。

reservoir境界observableを $B_r(t)=b_{r\ell_r}(t)$、平衡相関を $C_{rs}(t)$ とする。

<!-- theorem-start:theorem -->
**定理（R198D：mixing二保存action reservoirによる有限時間thermalization）**

R198A--R198Cを仮定する。さらに選んだ正温度・非凝縮reservoir sectorで、境界observableの相関と必要な高次cumulantが一様に可積分で、例えば

```math
\int_0^\infty(1+t)|C_{rs}(t)|dt<\infty
```

を満たすとする。$\lambda_r=\lambda\bar\lambda_r$、slow time $\tau=\lambda^2t$ を取る。有限kinetic interval $0\le\tau\le T$ で真のHamiltonian shell marginal $P_t^{\rm true}$ がreversible effective diffusion $P_\tau^{\rm eff}$ へ

```math
d_{\rm BL}(P_t^{\rm true},P_\tau^{\rm eff})
\le\varepsilon_{\rm hom}(\lambda,N,T)
```

で近づき、joint weak-coupling/large-reservoir limitで $\varepsilon_{\rm hom}\to0$ と仮定する。effective generatorのM59 Gibbs measureに対するspectral gapが $g_A\ge g_*>0$ なら、frozen $A$ について

```math
d_{\rm BL}(P_t^{\rm true},P_A^{\rm G})
\le C_0e^{-g_*\lambda^2t}
+\varepsilon_{\rm hom}
+\varepsilon_{B+C},
```

時間依存 $A(t)$ ではさらに

```math
C_{\rm ad}\frac{\sup|\dot A|}{g_*\lambda^2}
```

を加える。ここで $\varepsilon_{B+C}=O(N^{-1})+O(\lambda^4)+O(\lambda^2/N)$ はR198B/Cの静的誤差である。
<!-- theorem-end:theorem -->

R198DはDNLSが全parameter領域でergodicであるとは主張しない。mixing相関条件とhomogenization boundはQ3-1-A1/Q3-2-A1の残件として明示し、A2では $C_{rr}(t)$、integrated autocorrelation time、shell relaxation、$u$ 分布、$\pi_A(S)$ を直接数値監査する。

## W.7 R197A：Gibbs shellの平均力

R198A--R198Dが到達するtarget Gibbs shell自体の積分恒等式は旧M58から独立なので維持する。

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
F_{\rm sh}=-k_BT\log r^\delta+E_{\rm width},
```

```math
|\partial_yE_{\rm width}|
\le k_BT\Delta_*|\partial_y\log r^\delta|.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R197A）**

$K_1=uS$、$K_2=(1-u)S$ により $dK_1dK_2=S\,dSdu$ である。Gaussian積分で $\mathcal Z_A$ を求め、$k_BT\partial_A\log\mathcal Z_A=\langle G_A\rangle$ を用いる。証明終。
<!-- theorem-end:proof -->

## W.8 M37/M57への有限誤差接続

R198Dから得るcentered forceの有限相関積分を

```math
C_G=\sup_A\int_0^\infty
|\operatorname{Cov}[G_A(S_t),G_A(S_0)]|dt
```

とする。M37へのshell couplingはW.2のcapacity scalingを通じて弱くし、ballistic portはA22のweak tapを用いる。

<!-- theorem-start:theorem -->
**定理（R197C：M59 shell・ballistic-port負荷下のM37有限時間安定性）**

R86、R196A--R196C、R198A--R198Dのsafe-sector仮定を同時に満たすとする。shellの平均力誤差、有限相関fluctuation、port backreactionをそれぞれ $\varepsilon_{\rm shell}$、$\varepsilon_{\rm fluc}$、$\varepsilon_{\rm port}$ で評価できるなら、固定有限時間 $T$ で

```math
\varepsilon_{\rm sig}^{59}(T)
\le\varepsilon_{\rm car}(T)
+C_{\rm sig}(T)
\left(\varepsilon_{\rm shell}+\varepsilon_{\rm fluc}+\varepsilon_{\rm port}\right).
```

特に

```math
\varepsilon_{\rm fluc}
\le C_{\rm load}\sqrt{2TC_G}
```

と取れる。従ってR198Dのmixing windowとM37 weak-loading windowが同時に非空なら、M59 signal marginalはR86へ有限誤差で縮約する。
<!-- theorem-end:theorem -->

## W.9 共通誤差台帳とR161/R185への接続

M59 shellの誤差を

```math
\varepsilon_{\rm shell}^{59}
=\varepsilon_{\rm av}
+\varepsilon_{\rm coef}
+\frac{C_N}{N}
+C_\lambda\lambda^4
+\varepsilon_{\rm hom}
+C_{\rm th}e^{-g_*\lambda^2t}
+C_{\rm ad}\frac{\sup|\dot A|}{g_*\lambda^2}
+\varepsilon_\mu
```

とまとめる。ここで $\varepsilon_\mu$ はrenormalized chemical-potential matchingの残差である。

旧M58の $\mu_{\rm sh}\to\infty$ scalingは用いない。M59で必要な時間尺度窓は

```math
\tau_R\ll\tau_{\rm therm}\sim(g_*\lambda^2)^{-1}\ll\tau_A
```

であり、さらにM57のtracer・moving-frame時間尺度窓と両立させる。$\lambda$ を小さくすると静的coupling誤差は減る一方thermalizationは遅くなるため、非空parameter windowはR198Dの具体的mixing witnessまたは数値監査で確認する。

<!-- theorem-start:theorem -->
**定理（R197：M59 Q3-1/Q3-2共通ミクロ模型の条件付き有限時間統合）**

R86、R195A、R196A--R196C、R198A--R198D、R197A、R197Cの仮定を同時に満たし、固定有限時間のsafe sectorで $r^\delta\ge r_{\min}>0$ とする。このとき同一のM59古典Hamiltonian/open-tracer過程について次が成り立つ。

1. signal marginalはR86のSchrodinger型空間信号へ誤差 $\varepsilon_{\rm sig}^{59}$ で縮約する。
2. shellを周辺化した平均力は $k_BT\partial_x\log r^\delta$ にR197Aのfinite-width誤差と $\varepsilon_{\rm shell}^{59}$ を加えた範囲で一致する。
3. 同じ試行のM57 transportを保持すると、R196A--R196Cを通じてwell-index生成子はR161へ有限誤差で一致する。
4. R161のcanonical path lawにはR185を適用でき、時間対称Newton則に残る誤差はM59からR161への持上げ誤差、R185の正則化残差、格子残差である。

従ってR198Dのmixing/homogenization仮定を満たすparameter witnessが与えられた範囲で、Q3-1とQ3-2は同一M59過程の異なる周辺縮約として実現される。
<!-- theorem-end:theorem -->

## W.10 責務境界

R198Aは実Duffing自由度からaction shellを導き、R198Bは有限二保存action reservoirの平衡周辺化、R198Cは有限交換結合のmean-force補正、R198Dは有限時間thermalizationを担当する。R198Dだけは具体的reservoir sectorのmixing/homogenization条件を仮定として残す。

従って固定目標Q3-1/Q3-2の既存達成ラベルは変更しないが、M59だけをA1の完全達成証人とはまだ扱わない。Q3-1-A1/Q3-2-A1は部分達成とし、R198Dのmixing条件を具体parameter witnessまたは直接数値計算で閉じることを残件とする。A2ではM59のDuffing＋DNLS＋exchange力学そのものを直接計算する。
