@number: 5
@chapter: 本文
@title: Bell型測定統計：projection phase-volume主線と空間隔離強化
@status: Q2-2 fixed-goalはM66/R205A・R205E・R205FとR207A--R207Cによるprojection phase-volume共同準備、受動分離、局所二端読出しで達成する。R207DはBell-local controlを与える。Q2-2-Sはfinite-speed spatial isolationを独立に監査する。R180A/R180C逐次Bell witnessはdraft-135でactive paperから退役した。

## 5.1 目的と現行主線

Q2-2の固定目標は、二体系の共同内部状態を二つの物理的測定端へ接続し、一般余弦共同確率、CHSH不等式の破れ、Tsirelson限界、非信号性を整合的に導くこと、およびBell不等式の導出に用いられる前提の成立・不成立を物理的因果構造と確率因子化へ対応させることである。

現行主線R207は
```math
(\boldsymbol a,\boldsymbol b)
\longrightarrow
\rho_{\epsilon,k}(\boldsymbol\lambda_A,\boldsymbol\lambda_B\mid\boldsymbol a,\boldsymbol b)
\longrightarrow
\text{passive separation}
\longrightarrow
(r,s)
\longrightarrow
\text{local records}
```
と進む。測定窓中のA結果成分からB端への逐次転送は用いない。旧R180A/R180Cの非空間分離逐次witnessはdraft-135で退役し、履歴はnotesへ保存する。

## 5.2 projection phase-volume共同準備

設定方向とhidden directionsを
```math
\boldsymbol a,\boldsymbol b,\boldsymbol\lambda_A,\boldsymbol\lambda_B\in S^2
```
とする。finite thickness
```math
f_\epsilon(t)=\sqrt{t^2+\epsilon^2(1-t^2)}
```
を用い、
```math
w_\epsilon
=
f_\epsilon(\boldsymbol a\cdot\boldsymbol\lambda_A)
+
f_\epsilon(\boldsymbol b\cdot\boldsymbol\lambda_B)
```
とする。M66/R205Aのphase-volume sectorを二つの等価な内部branchへ特殊化すれば、この和は二本の局所projection railのphase volumeの加算として得られる。

near-contact lock
```math
H_{\rm lock}=-K\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B
```
とR205Eを組み合わせると
```math
\rho_{\epsilon,k}
\propto
e^{k\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B}
w_\epsilon,
\qquad
k=\beta K.
```
R207Aによりpartition functionは設定方向に依存しない。従って外部setting generatorを独立に駆動できる一方、条件付きsource distributionはsetting-dependentでありmeasurement independenceは成立しない。

## 5.3 一般角度共同分布

局所結果を
```math
r=\operatorname{sgn}(\boldsymbol a\cdot\boldsymbol\lambda_A),
\qquad
s=-\operatorname{sgn}(\boldsymbol b\cdot\boldsymbol\lambda_B)
```
とする。$\epsilon=0$ ではR207Bから
```math
E_{0,k}(\boldsymbol a,\boldsymbol b)
=
-L(k)\boldsymbol a\cdot\boldsymbol b,
\qquad
L(k)=\coth k-\frac1k,
```
および
```math
P_{0,k}(r,s\mid\boldsymbol a,\boldsymbol b)
=
\frac14\left[
1-rsL(k)\boldsymbol a\cdot\boldsymbol b
\right]
```
を得る。局所周辺は任意の有限$k$でexactに$1/2$である。

$k\to\infty$ では
```math
P_{\rm singlet}(r,s\mid\boldsymbol a,\boldsymbol b)
=
\frac14\left[
1-rs\boldsymbol a\cdot\boldsymbol b
\right]
```
へ収束する。標準CHSH設定では
```math
|S|=2\sqrt2L(k)
```
であり、有限$k>3.387780776\ldots$でCHSH境界を超え、任意精度でTsirelson値へ近づく。

## 5.4 finite-thickness / finite-lock誤差

finite thicknessでは
```math
d_{\rm TV}(\rho_{\epsilon,k},\rho_{0,k})\le2\epsilon
```
である。従って
```math
d_{\rm TV}(P_{\epsilon,k},P_{\rm singlet})
\le
2\epsilon+\frac{1-L(k)}2.
```

任意のtarget $\eta>0$ に対して
```math
\epsilon=\frac{\eta}{8},
\qquad
k=\frac2\eta
```
のような有限選択で統計側誤差を$\eta/2$未満にできる。残る誤差予算をthermal mixing、hidden-direction保持、passive separation、local latch、recordへ割り当てる。

## 5.5 一試行の二端物理interface

共有projection phase-volume geometryには固定距離則 $\chi_{\rm pv}(R)$ を置き、近接準備時に $\chi_{\rm pv}=1$、分離時に $\chi_{\rm pv}\to0$ とする。M66の共有weightを $w_\epsilon^{\chi_{\rm pv}(R)}$ とすれば、finite $\epsilon>0$ で共有free-energy driftは距離とともに受動的に消える。

準備後に端間距離$R$を増やす。R205Fにより$K(R)$とreservoir cross-correlationを、同時にR207の $\chi_{\rm pv}(R)$ を小さくし、分離後のideal generatorを
```math
\mathcal L=\mathcal L_A+\mathcal L_B
```
へ近づける。

同じlocal mobilityを準備と保持に用い、準備時間を十分長く、分離から結果固定までの保持窓を十分短く選ぶことでhidden directionのlaw変化を$\varepsilon_{\rm hold}^{207}$以下へ抑える。各端のsign comparatorには有限安全帯を置き、R112型の局所recordへ結果を固定する。安全帯を無反応として完全結果集合へ含め、成功試行だけの再規格化は行わない。

R207Cの合成誤差は
```math
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
\varepsilon_{\rm rec}^{207}.
```
各項は有限parameterで任意に小さくできるため、固定目標達成規則に従いQ2-2は達成を維持する。

## 5.6 Bell前提監査

exact separation極では
```math
P(r,s\mid\Lambda,\boldsymbol a,\boldsymbol b)
=
P_A(r\mid\lambda_A,\boldsymbol a)
P_B(s\mid\lambda_B,\boldsymbol b)
```
とlocal response factorizationする。一方、
```math
\rho(\Lambda\mid\boldsymbol a,\boldsymbol b)\neq\rho(\Lambda)
```
でありmeasurement independenceは成立しない。

setting marginal自体は独立に保て、operational marginalは各端$1/2$で非信号である。A結果からB結果への測定窓内result communicationを用いず、無反応・棄却を事後除外しない。R207Dでmeasurement independenceとlocal response factorizationを同時に課すと$|S|\le2$へ戻る。

## 5.7 Q2-2-Sとの境界

Q2-2 fixed-goalは有限最大伝播速度に基づくspacelike separationを要求しない。R207A--R207Cは二つの物理端と一試行interfaceを閉じるが、R205Fのgenerator decouplingだけから有限最大伝播速度は従わない。

Q2-2-Sではさらに
```math
t_A^{\rm out}-t_B^{\rm set}<\frac{L}{v_{\max}},
\qquad
t_B^{\rm out}-t_A^{\rm set}<\frac{L}{v_{\max}}
```
を同じphysical implementationで閉じる。finite-speed spatial reservoir、具体transport geometry、direct SDE trajectoryは未監査のままとする。
