@number: W
@chapter: 付録
@title: R207 projection phase-volume共同準備と局所二端読出し
@status: R207A--R207DをQ2-2 fixed-goalの現行Bell統計主線へ正式昇格する。M66/R205A・R205Eのphase-volume thermal preparationとR205Fのpassive separationを使い、一般Bloch方向の一重項共同統計、finite-thickness/finite-lock誤差、分離後local response、measurement-dependence監査を与える。R180A/R180Cは本draftではactive alternate witnessとして残し、退役は後続変更へ分離する。finite-speed spatial reservoir、direct SDE trajectory、実験装置はQ2-2-S/A2/Bの強化課題として残す。

## W.1 目的と因果境界

Q2-2の現行主線は、設定方向を含む近接時共同thermal preparation、受動分離、局所二値結果、局所記録の順で一試行を構成する。

\[
t_{\rm prep}<t_{\rm sep}<t_A^{\rm latch},t_B^{\rm latch}<t_A^{\rm out},t_B^{\rm out}.
\]

測定設定を表す単位ベクトルを
\[
\boldsymbol a,\boldsymbol b\in S^2
\]
とし、source側の実在古典方向自由度を
\[
\boldsymbol\lambda_A,\boldsymbol\lambda_B\in S^2
\]
とする。設定は局所制御器の物理状態として準備窓から存在してよい。後段のlocal latchはsource--setting相関を消さず、測定設定独立性を回復させない。

local thermal contactを確率生成のためだけにswitchしない。A/B間lockとreservoir cross-correlationは距離依存constitutive lawとして受動的に減衰させる。

## W.2 R207A：projection phase-volume共同準備

finite thicknessを表す
\[
f_\epsilon(t)=\sqrt{t^2+\epsilon^2(1-t^2)},\qquad 0<\epsilon<1
\]
を置き、
\[
w_A=f_\epsilon(\boldsymbol a\cdot\boldsymbol\lambda_A),\qquad
w_B=f_\epsilon(\boldsymbol b\cdot\boldsymbol\lambda_B)
\]
とする。$f_\epsilon$ は正で滑らかであり、$\epsilon\downarrow0$ で $|t|$ へ一様収束する。

phase-volumeは二つの等価な内部sector $J=A,B$ の和として実装する。$J=A$ sectorではR205A型fast canonical pairのJacobianを $w_A$、$J=B$ sectorでは $w_B$ とし、外部からsectorを選別せず両sectorを積分消去する。従って総phase-volume factorは
\[
w_\epsilon=w_A+w_B
\]
となる。これは結果確率表の外部注入ではなく、各setting方向に沿う有限厚みprojection railの局所phase volumeの和である。

near-contact lockを
\[
H_{\rm lock}^{(R)}=-K(R)\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B,\qquad
k=\beta K(R_{\rm prep})
\]
とする。R205Eへ $H_{\rm cfg}=H_{\rm lock}^{(R_{\rm prep})}$、$w=w_\epsilon$ を入れると
\[
\rho_{\epsilon,k}
(\boldsymbol\lambda_A,\boldsymbol\lambda_B\mid\boldsymbol a,\boldsymbol b)
=
\frac{
e^{k\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B}
\left[
f_\epsilon(\boldsymbol a\cdot\boldsymbol\lambda_A)
+
f_\epsilon(\boldsymbol b\cdot\boldsymbol\lambda_B)
\right]
}{Z_{\epsilon,k}}.
\]

\[
F_\epsilon=\int_{-1}^{1}f_\epsilon(t)\,dt,\qquad
G(k)=4\pi\frac{\sinh k}{k}
\]
とすると
\[
Z_{\epsilon,k}=4\pi F_\epsilon G(k)
\]
であり、$\boldsymbol a,\boldsymbol b$ に依存しない。

<!-- theorem-start:theorem -->
**定理（R207A：projection phase-volume共同準備とsetting marginal）**

任意の $\boldsymbol a,\boldsymbol b\in S^2$ に対してpartition functionは同じ $Z_{\epsilon,k}$ である。従ってsetting generatorを独立な基準分布 $p_A(\boldsymbol a)p_B(\boldsymbol b)$ で駆動したとき、thermal preparation後も
\[
P(\boldsymbol a,\boldsymbol b)=P(\boldsymbol a)P(\boldsymbol b)
\]
を保てる。

一方 $0<\epsilon<1$ では一般に
\[
\rho_{\epsilon,k}(\Lambda\mid\boldsymbol a,\boldsymbol b)\neq\rho_{\epsilon,k}(\Lambda)
\]
であり、source hidden stateはsetting-independentではない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R207A）**

固定 $\boldsymbol\lambda_A$ に対する $\boldsymbol\lambda_B$ 積分は回転対称性から $G(k)$、固定setting方向に対するsphere積分は $2\pi F_\epsilon$ である。$w_A,w_B$ の二項を足すと表示の $Z_{\epsilon,k}$ を得る。

measurement dependenceについて、同じhidden configuration $\boldsymbol\lambda_A=\boldsymbol\lambda_B=\hat{\boldsymbol z}$ を考える。$\boldsymbol a=\boldsymbol b=\hat{\boldsymbol z}$ ではphase-volume factorは $2$、$\boldsymbol a=\boldsymbol b=\hat{\boldsymbol x}$ では $2\epsilon$ である。partition functionはsetting-independentなので、$0<\epsilon<1$ では条件付きhidden-state densityがsettingに依存する。証明終。
<!-- theorem-end:proof -->

## W.3 R207B：一般Bloch方向の一重項共同統計

局所結果を
\[
r=\operatorname{sgn}(\boldsymbol a\cdot\boldsymbol\lambda_A),\qquad
s=-\operatorname{sgn}(\boldsymbol b\cdot\boldsymbol\lambda_B)
\]
とする。零集合はsphere measure zeroなので任意に割り当ててよい。

$\epsilon=0$ では
\[
|\boldsymbol a\cdot\boldsymbol\lambda_A|
\operatorname{sgn}(\boldsymbol a\cdot\boldsymbol\lambda_A)
=
\boldsymbol a\cdot\boldsymbol\lambda_A.
\]
von Mises--Fisher kernelの第一momentを
\[
L(k)=\coth k-\frac1k
\]
とすると
\[
\frac{\int e^{k\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B}
\boldsymbol\lambda_A\,d\Omega_A}
{\int e^{k\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B}d\Omega_A}
=L(k)\boldsymbol\lambda_B,
\]
また
\[
\int_{S^2}\boldsymbol\lambda\,
\operatorname{sgn}(\boldsymbol b\cdot\boldsymbol\lambda)\,d\Omega
=2\pi\boldsymbol b.
\]

<!-- theorem-start:theorem -->
**定理（R207B：finite-lock余弦則とfinite-thickness安定性）**

$\epsilon=0$ では任意の有限 $k>0$ と任意のBloch方向に対して
\[
E_{0,k}(\boldsymbol a,\boldsymbol b)
=
-L(k)\boldsymbol a\cdot\boldsymbol b.
\]
同時反転 $(\boldsymbol\lambda_A,\boldsymbol\lambda_B)\mapsto(-\boldsymbol\lambda_A,-\boldsymbol\lambda_B)$ はdensityを保ち $r,s$ をともに反転するため
\[
P(r=\pm1\mid\boldsymbol a,\boldsymbol b)
=
P(s=\pm1\mid\boldsymbol a,\boldsymbol b)
=
\frac12.
\]
従って
\[
P_{0,k}(r,s\mid\boldsymbol a,\boldsymbol b)
=
\frac14\left[1-rsL(k)\boldsymbol a\cdot\boldsymbol b\right].
\]

標準CHSH設定では
\[
|S_{0,k}|=2\sqrt2L(k),
\]
従って $k>3.387780776\ldots$ で $|S|>2$、$k\to\infty$ でTsirelson値 $2\sqrt2$ へ収束する。

finite thicknessでは
\[
0\le f_\epsilon(t)-|t|\le\epsilon
\]
から
\[
d_{\rm TV}(\rho_{\epsilon,k},\rho_{0,k})\le2\epsilon.
\]
従って
\[
d_{\rm TV}(P_{\epsilon,k},P_{\rm singlet})
\le
2\epsilon+\frac{1-L(k)}2
\]
が任意のsetting pairに一様に成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R207B）**

$w_A$ 項では第一moment恒等式を用いて $\boldsymbol\lambda_A$ を積分し、その後 $\boldsymbol\lambda_B$ の半球符号積分を行うと $-L(k)\boldsymbol a\cdot\boldsymbol b/2$ を得る。$w_B$ 項も同じ値を与える。単独周辺は同時反転対称性から零である。

finite thicknessでは $w_\epsilon-w_0$ は非負で各二項の増分が高々 $\epsilon$。規格化定数の変化を含めたdensityの全変動距離は高々 $2\epsilon$ であり、outcome写像で増えない。$\epsilon=0$ のfinite-lock lawとsinglet lawの全変動距離は $(1-L(k))|\boldsymbol a\cdot\boldsymbol b|/2$ 以下なので三角不等式で結論を得る。証明終。
<!-- theorem-end:proof -->

任意のtarget $\eta>0$ に対して
\[
\epsilon=\frac{\eta}{8},\qquad k=\frac2\eta
\]
とすれば統計核誤差は $\eta/2$ 未満になる。

## W.4 R207C：受動分離、一試行local interface、Bell前提監査

準備後に$R$を増やし、R205Fの距離依存lock $K(R)$ とreservoir cross block $C_{AB}(R)$ を受動的に小さくする。local thermal contactとlocal mobilityは切らない。

local rotational mobilityを $\mu_\lambda>0$、diffusion scaleを $D_\lambda=\mu_\lambda k_BT$ とする。$\mu_\lambda$ を小さくすると準備mixing時間は長くなるが有限のままであり、準備後の有限保持窓 $T_{\rm hold}=T_{\rm sep}+T_{\rm meas}$ におけるhidden-direction変化を小さくできる。準備終了時とlocal latch時のlawの全変動差を $\varepsilon_{\rm hold}^{207}$ とする。

R205Fの有限距離generator defectを $\varepsilon_{\rm sep}^{207}(R)$ とし、$R\to\infty$ で0へ行く。finite-speed causal isolationはここから推論せずQ2-2-Sへ残す。

各端では局所settingと局所hidden directionだけを比較する。ideal sign boundaryの有限幅 $\delta_{\rm lat}$ 近傍を正式な無反応安全帯として扱い、R112型比較・recordを用いる。finite $\epsilon>0$ のsmooth densityでは境界帯確率は $\delta_{\rm lat}\downarrow0$ で0へ行く。成功試行だけの再規格化は行わない。

<!-- theorem-start:theorem -->
**定理（R207C：一試行local二端合成とBell前提監査）**

R207Aの有限時間thermal preparation、有限保持、R205Fの有限距離passive separation、二つのlocal comparator/latch、R112型recordを同じ一試行に順序付ける。完全結果分布の実装誤差を
\[
\varepsilon_{207}
\le
\varepsilon_{\rm prep}^{207}
+
2\epsilon
+
\frac{1-L(k)}2
+
\varepsilon_{\rm hold}^{207}
+
\varepsilon_{\rm sep}^{207}
+
\varepsilon_{\rm latch}^{207}
+
\varepsilon_{\rm rec}^{207}
\]
とする。任意のtarget $\eta>0$ に対し、各parameterとrecord精度を有限に選び $\varepsilon_{207}<\eta$ とできる。

exact decoupling極では
\[
P(r,s\mid\Lambda,\boldsymbol a,\boldsymbol b)
=
P_A(r\mid\lambda_A,\boldsymbol a)
P_B(s\mid\lambda_B,\boldsymbol b)
\]
が成立する。一方R207Aにより
\[
\rho(\Lambda\mid\boldsymbol a,\boldsymbol b)\neq\rho(\Lambda).
\]
従って分離後local response factorizationとoperational non-signalingを保ちながらmeasurement independenceを満たさない。測定窓中のA結果からB結果へのresult communication、棄却試行のpostselection、結果確率表の外部注入は用いない。
<!-- theorem-end:theorem -->

finite最大伝播速度 $v_{\max}$ を持つ具体spatial reservoirとsetting確定後のcausal-isolation timingを同じ装置で閉じることはQ2-2-Sの独立強化課題である。

## W.5 R207D：Bell-local control

<!-- theorem-start:theorem -->
**定理（R207D：measurement-independent Bell-local control）**

同じ二値local responseについて
\[
\rho(\Lambda\mid\boldsymbol a,\boldsymbol b)=\rho(\Lambda)
\]
とlocal response factorizationを同時に課すなら、任意の4設定に対するCHSH量は
\[
|S|\le2
\]
を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R207D）**

固定 $\Lambda$ に対する二値local responseのCHSH integrandは絶対値2以下である。4 setting pairに共通なsetting-independent $\rho(\Lambda)$ で平均すれば表示の境界を得る。証明終。
<!-- theorem-end:proof -->

## W.6 Q2-2-Sとの境界

| 段階 | 現行R207との対応 | 状態 |
|---|---|---|
| S0 | R207A--R207Cのfixed-goal二端baseline | fixed-goal主線として確立 |
| S1 | 具体距離・transport geometryを持つ二端分離 | strengthening未監査 |
| S2 | setting確定後のfinite-speed causal isolation | finite-speed spatial reservoir未閉包 |
| S3 | S2を保ったsinglet統計とBell前提監査 | S2実装に条件付き |
| S4 | R207D Bell-local control | 解析controlあり |

R207のfixed-goal昇格だけからQ2-2-Sを達成または部分達成へ更新しない。direct SDE trajectory、finite-speed spatial reservoir、具体実験装置とparameter windowはA2/B/Q2-2-Sで別に監査する。
