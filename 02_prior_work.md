@number: D
@chapter: 付録D
@title: autonomous clock、滑らかな pulse、機械的正則化
@status: 理想 scheduled Hamiltonian の有限自律化と、その物理的制約。

## D.1 extended phase-space suspension

時間依存 Hamiltonian $H(z,t)$ を考える。追加 canonical pair $(\vartheta,J_c)$ と定数 $\Omega>0$ を用いて

$$
H_{\rm ext}(z,\vartheta,J_c)
=
\Omega J_c+H(z,\vartheta/\Omega)
$$

とすれば

$$
\dot\vartheta=\Omega
$$

であり、$z$ は元の time-dependent Hamilton equations に従う。これは extended phase-space autonomization の標準構成である [15]。

本論文では periodic clock angle を使い

$$
H_{\rm ext}
=
\Omega J_c
+H_{\rm free}
+\Omega\sum_\nu f_\nu(\vartheta)K_\nu
$$

とした。profile の support を分離すれば各 operation の順序を固定できる。

## D.2 clock backreaction

clock momentum は

$$
\dot J_c
=
-\frac{\partial H_{\rm ext}}{\partial\vartheta}
$$

により変化する。従って clock は一方向に外部仕事を供給する無限 reservoir ではなく、有限 trial の間に apparatus との energy exchange を記録する。

$H_{\rm ext}$ が $J_c$ に線形なら $\dot\vartheta=\Omega$ は backreaction にかかわらず厳密である。ただし標準 cotangent cylinder で $J_c\in\mathbb R$ と取ると clock Hamiltonian は大域的には下から有界でない。

## D.3 working annulus

classical harmonic clock の action-angle coordinates を用い、$J_c>0$ の annulus に working domain を限定できる。十分大きい初期 action と有限 trial time を選び、pulse work より大きい margin を持たせれば $J_c$ は annulus 内に留まる。

angle-dependent profile は oscillator origin で滑らかでないが、working annulus の外で任意に smooth extension できる。従って有限 trial の accessible domain 上では、positive clock action と exact phase advance を両立できる。大域的に compact、全 energy shell 上で smooth、任意回数反復可能な clock の構成は別問題である。

rotor を内部 clock と work repository に用いる autonomous device の具体例は既存研究にもある [16]。

## D.4 smooth pulse profile

各 profile $f_\nu$ は compact support を持つ $C^\infty$ bump function として選べる。support 間隔を $\Delta\vartheta$、pulse width を $w$ とし

$$
w<\Delta\vartheta
$$

とすれば overlap はない。

有限 overlap を許す場合、time-ordered flow に Baker--Campbell--Hausdorff correction

$$
\epsilon_{\rm BCH}
\sim
\int dt\,dt'
f_\mu(t)f_\nu(t')
\{K_\mu,K_\nu\}
$$

が現れる。local A/B pulses は disjoint variables に作用するため Poisson commute するが、return pulse は local rotations 後に分離しておく必要がある。

## D.5 pointer kinetic regularization

理想 comparator は pulse 中に pointer kinetic term を持たない。有限 mass $M_R$ を導入して

$$
H_{R,0}
=
\frac{\Pi_R^2}{2M_R}+V_R(Y_R)
$$

とすると、comparator shift 後に $Y_R$ が動く。pulse duration を $\tau_R$ とすれば leading displacement は

$$
\Delta Y_R
\sim
\frac{\tau_R}{M_R}
(\kappa I_- -H_s).
$$

従って $M_R$ を大きくする、pulse を短くする、または clock により $H_{R,0}$ を interaction window で gate off することで理想 map へ近づける。有限誤差は terminal threshold を通じて joint law に影響するため、数値検証では直接測る。

## D.6 bounded comparator coupling

$F_R(Y)=\delta\tanh(Y/\delta)$ は bounded であり、

$$
|F_R(Y)|\leq\delta.
$$

soft energy coefficient と messenger free coefficient を十分大きく取れば、working domain 上で comparator coupling を含む total Hamiltonian を下から有界にできる。unbounded linear pointer coupling $Y_RD$ を用いる必要はない。

## D.7 時間反転

messenger action、soft energy、coordinate coupling $F_R(Y_R)D$ は標準 time reversal

$$
(Q,P,Y,\Pi)
\longmapsto
(Q,-P,Y,-\Pi)
$$

に対して even に選べる。局所 operation の時間順序は clock の初期 phase という boundary data により決まる。従って Hamiltonian の microscopic reversibility と、実験 protocol の時間非対称な preparation を区別する必要がある。

Model A の terminal half-space $\Pi_R\geq0$ は time-reversal invariant ではない。time-symmetric ready boundary を重視する場合は Model B の $\Pi_R=0$ または $|\Pi_R|\leq\varepsilon$ を用いる。

## D.8 結論

理想 pulse model は finite extended phase space 上で正確に自律化できる。通常の massive pointer、finite pulse、bounded energy、time-symmetric terminal cell へ置き換えると制御可能な correction が現れる。constructive theorem と完全に自然な mechanical apparatus を同一視してはならない。
