@number: 5
@chapter: 本文
@title: Bell型測定統計：projection phase-volume主線と空間隔離強化
@status: Q2-2 fixed-goalはM66/R205A・R205E・R205FとR207A--R207Cによるprojection phase-volume共同準備、受動分離、局所二端読出しで達成する。R207DはBell-local controlを与える。R180A/R180Cは本draftではactive alternate witnessとして残すがfixed-goal直接依存から外し、退役は後続PRへ分離する。Q2-2-Sはfinite-speed spatial isolationを独立に監査する。

## 5.1 目的と現行主線

Q2-2の固定目標は、二体系の共同内部状態を二つの物理的測定端へ接続し、一般余弦共同確率、CHSH不等式の破れ、Tsirelson限界、非信号性を整合的に導くこと、およびBell不等式の導出に用いられる前提の成立・不成立を物理的因果構造と確率因子化へ対応させることである。

現行主線R207は
\[
(\boldsymbol a,\boldsymbol b)
\longrightarrow
\rho_{\epsilon,k}(\boldsymbol\lambda_A,\boldsymbol\lambda_B\mid\boldsymbol a,\boldsymbol b)
\longrightarrow
\text{passive separation}
\longrightarrow
(r,s)
\longrightarrow
\text{local records}
\]
と進む。R180CのようなA結果成分からB端への逐次転送は現行主線では使わない。R180A/R180Cはactive alternate witnessとして5.8節に残し、このdraftでは結果IDを退役させない。

## 5.2 projection phase-volume共同準備

設定方向とhidden directionsを
\[
\boldsymbol a,\boldsymbol b,\boldsymbol\lambda_A,\boldsymbol\lambda_B\in S^2
\]
とする。finite thickness
\[
f_\epsilon(t)=\sqrt{t^2+\epsilon^2(1-t^2)}
\]
を用い、
\[
w_\epsilon
=
f_\epsilon(\boldsymbol a\cdot\boldsymbol\lambda_A)
+
f_\epsilon(\boldsymbol b\cdot\boldsymbol\lambda_B)
\]
とする。M66/R205Aのphase-volume sectorを二つの等価な内部branchへ特殊化すれば、この和は二本の局所projection railのphase volumeの加算として得られる。

near-contact lock
\[
H_{\rm lock}=-K\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B
\]
とR205Eを組み合わせると
\[
\rho_{\epsilon,k}
\propto
e^{k\boldsymbol\lambda_A\cdot\boldsymbol\lambda_B}
w_\epsilon,
\qquad
k=\beta K.
\]
R207Aによりpartition functionは設定方向に依存しない。従って外部setting generatorを独立に駆動できる一方、条件付きsource distributionはsetting-dependentでありmeasurement independenceは成立しない。

## 5.3 一般角度共同分布

局所結果を
\[
r=\operatorname{sgn}(\boldsymbol a\cdot\boldsymbol\lambda_A),
\qquad
s=-\operatorname{sgn}(\boldsymbol b\cdot\boldsymbol\lambda_B)
\]
とする。$\epsilon=0$ ではR207Bから
\[
E_{0,k}(\boldsymbol a,\boldsymbol b)
=
-L(k)\boldsymbol a\cdot\boldsymbol b,
\qquad
L(k)=\coth k-\frac1k,
\]
および
\[
P_{0,k}(r,s\mid\boldsymbol a,\boldsymbol b)
=
\frac14\left[
1-rsL(k)\boldsymbol a\cdot\boldsymbol b
\right]
\]
を得る。局所周辺は任意の有限$k$でexactに$1/2$である。

$k\to\infty$ では
\[
P_{\rm singlet}(r,s\mid\boldsymbol a,\boldsymbol b)
=
\frac14\left[
1-rs\boldsymbol a\cdot\boldsymbol b
\right]
\]
へ収束する。標準CHSH設定では
\[
|S|=2\sqrt2L(k)
\]
であり、有限$k>3.387780776\ldots$でCHSH境界を超え、任意精度でTsirelson値へ近づく。

## 5.4 finite-thickness / finite-lock誤差

finite thicknessでは
\[
d_{\rm TV}(\rho_{\epsilon,k},\rho_{0,k})\le2\epsilon
\]
である。従って
\[
d_{\rm TV}(P_{\epsilon,k},P_{\rm singlet})
\le
2\epsilon+\frac{1-L(k)}2.
\]

任意のtarget $\eta>0$ に対して
\[
\epsilon=\frac{\eta}{8},
\qquad
k=\frac2\eta
\]
のような有限選択で統計側誤差を$\eta/2$未満にできる。残る誤差予算をthermal mixing、hidden-direction保持、passive separation、local latch、recordへ割り当てる。

## 5.5 一試行の二端物理interface

共有projection phase-volume geometryには固定距離則 $chi_{m pv}(R)$ を置き、近接準備時に $chi_{m pv}=1$、分離時に $chi_{m pv}	o0$ とする。M66の共有weightを $w_epsilon^{chi_{m pv}(R)}$ とすれば、finite $epsilon>0$ で共有free-energy driftは距離とともに受動的に消える。

準備後に端間距離$R$を増やす。R205Fにより$K(R)$とreservoir cross-correlationを、同時にR207の $chi_{m pv}(R)$ を小さくし、分離後のideal generatorを
\[
\mathcal L=\mathcal L_A+\mathcal L_B
\]
へ近づける。

同じlocal mobilityを準備と保持に用い、準備時間を十分長く、分離から結果固定までの保持窓を十分短く選ぶことでhidden directionのlaw変化を$\varepsilon_{\rm hold}^{207}$以下へ抑える。各端のsign comparatorには有限安全帯を置き、R112型の局所recordへ結果を固定する。安全帯を無反応として完全結果集合へ含め、成功試行だけの再規格化は行わない。

R207Cの合成誤差は
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
\varepsilon_{\rm rec}^{207}.
\]
各項は有限parameterで任意に小さくできるため、固定目標達成規則に従いQ2-2は達成を維持する。

## 5.6 Bell前提監査

exact separation極では
\[
P(r,s\mid\Lambda,\boldsymbol a,\boldsymbol b)
=
P_A(r\mid\lambda_A,\boldsymbol a)
P_B(s\mid\lambda_B,\boldsymbol b)
\]
とlocal response factorizationする。一方、
\[
\rho(\Lambda\mid\boldsymbol a,\boldsymbol b)\neq\rho(\Lambda)
\]
でありmeasurement independenceは成立しない。

setting marginal自体は独立に保て、operational marginalは各端$1/2$で非信号である。A結果からB結果への測定窓内result communicationを用いず、無反応・棄却を事後除外しない。R207Dでmeasurement independenceとlocal response factorizationを同時に課すと$|S|\le2$へ戻る。

## 5.7 Q2-2-Sとの境界

Q2-2 fixed-goalは有限最大伝播速度に基づくspacelike separationを要求しない。R207A--R207Cは二つの物理端と一試行interfaceを閉じるが、R205Fのgenerator decouplingだけから有限最大伝播速度は従わない。

Q2-2-Sではさらに
\[
t_A^{\rm out}-t_B^{\rm set}<\frac{L}{v_{\max}},
\qquad
t_B^{\rm out}-t_A^{\rm set}<\frac{L}{v_{\max}}
\]
を同じphysical implementationで閉じる。finite-speed spatial reservoir、具体transport geometry、direct SDE trajectoryは未監査のままとする。

## 5.8 R180A/R180C active alternate witness

R180A/R180Cは本draftでは削除しない。設定前一重項4モードsignalを用い、A端の結果成分をprojector routerでB端へ渡す非空間分離逐次証人としてactive paperに残す。ただしQ2-2 fixed-goalの直接依存からは外し、後続PRで退役可否を独立に処理する。

### 5.8.1 固定一重項源と試行順序

固定ベンチマークではR181B/R181Cにより

```math
|00\rangle
\longrightarrow
\frac{|01\rangle-|10\rangle}{\sqrt2}
```

に対応する4モード信号を設定生成前に準備する。1周期の順序は次とする。

1. M54で固定一重項型末端信号 $Z$ を作る。
2. 設定生成器から $x,y$ を得る。
3. A側basis gate $U_x^\dagger\otimes I$ を同じ4モード信号へ作用する。
4. A結果射影作用 $J_{A,\pm}$ を保持し、A端M65を走らせて $r$ を固定・記録する。
5. R181Dと同じprojector routerで非規格化結果成分 $P_{A,r}^{x}Z$ をB端へ渡す。
6. B端で $I\otimes U_y^\dagger$ を作用し、B結果射影作用を保持する。
7. B端M65を走らせて $s$ を固定・記録する。
8. 外部記録を残し、必要な能動部をR179のopen resetへ渡す。

A端とB端は別々のM65 open selectorと有限recordを持つ。結果成分の物理転送があるため本装置は非空間分離である。

### 5.8.2 A端特殊化：binary selectorとR181Dから従うR180A

A設定 $x$ の固有基底を $u_{r,x}$、射影を

```math
P_{A,r}^{x}
=|u_{r,x}\rangle\langle u_{r,x}|\otimes I
```

とする。A端作用は

```math
J_{A,r}
=\mathcal J_0Z^\dagger P_{A,r}^{x}Z.
```

<!-- theorem-start:corollary -->
**系（R180A：binary selector--R181Dの設定先行A端特殊化）**

M54末端信号 $Z$ にA設定basis gateを作用し、直交射影子作用保持機構で $J_{A,+},J_{A,-}$ を保持してbinary selectorへ渡す。selectorの結果を $r$ とし、その固定記録で共通projector routerを制御する。理想極限では

```math
P(r\mid Z,x)
=\frac{J_{A,r}}{J_{A,+}+J_{A,-}}
=\frac{\|P_{A,r}^{x}Z\|^2}{\|Z\|^2},
```

かつB端へ渡る能動信号は非規格化結果成分

```math
Z_r=P_{A,r}^{x}Z
```

である。物理的な $Z_r/\|Z_r\|$ の生成を必要としない。作用保持、selector、routerの有限誤差は完全結果集合上で各1回だけ数える。
<!-- theorem-end:corollary -->

### 5.8.3 B端条件付き読出し

B設定 $y$ の射影を

```math
P_{B,s}^{y}
=I\otimes|u_{s,y}\rangle\langle u_{s,y}|
```

とする。A結果 $r$ 後のB端selector入力は

```math
J_{B,s\mid r}
=\mathcal J_0\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2,
```

```math
S_r
=\mathcal J_0\|P_{A,r}^{x}Z\|^2.
```

従ってbinary selector contractとR181Dの逐次受渡し則から

```math
P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|P_{A,r}^{x}Z\|^2}.
```

A端の確率と掛けると分母がtelescopingし、

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

### 5.8.4 R180C：2端合成とBell監査

<!-- theorem-start:theorem -->
**定理（R180C：M54駆動2端受信機構合成、有限誤差、局所性監査、帰還）**

R180AのA端作用保持・binary selector・projector router、B設定gate、B端作用保持・binary selector、二つの局所記録を、同じ一試行の有限な順序付き操作窓と安全集合上で実行できるとする。A端で固定した結果に対応する非規格化結果成分をprojector routerがB端へ物理的に渡した後にB端selectorを作用させる。反復試行で同じ能動補助部を再使用する場合のR179 open reset、永久記録、物理clock、次試行renewalは本定理の共同分布には用いずM0へ分離する。理想極限の完全結果共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

固定一重項型 $Z$ では

```math
P(r,s\mid x,y)
=
\frac14\left(1-rs\,\boldsymbol a_x\cdot\boldsymbol b_y\right),
```

```math
E(x,y)
=-\boldsymbol a_x\cdot\boldsymbol b_y.
```

従って標準CHSH設定で $|S|=2\sqrt2$ を得る。各翼の周辺は $1/2$ であり、理想共同分布は非信号性を満たす。

有限実装では、上流保持・basis gate、A端selector、router、B端basis gate、B端selector、記録の完全結果誤差を各1回加えた量を $\varepsilon_{180}$ とする。実共同分布は理想共同分布から全変動距離 $\varepsilon_{180}$ 以内にあり、周辺差とCHSH差はこの全変動誤差から従う標準安定性上界で抑えられる。

A端結果成分がB端へ物理的に渡るため、現行証人ではBell局所因子化を仮定しない。設定前の一重項源は $x,y$ に依存せず、現行証人のCHSH破れを測定設定独立性の破れへ帰属させない。一方、B端へ到達する内部状態はA設定とA結果に依存する。本結果は、この逐次因果伝播、完全結果集合、非信号周辺を同時に示すBell前提監査であり、空間分離局所模型を主張しない。
<!-- theorem-end:theorem -->
