@number: 5
@chapter: 本文
@title: Bell型測定統計：現行逐次証人と空間隔離強化
@status: Q2-2 fixed-goalはR180A/R180CとA/B両端M65、R181D projector routerによる非空間分離逐次証人で達成する。Q2-2-SはM66/R205Eのjoint thermal preparation、R205Fのpassive separation、R207A--R207Dを別の空間隔離candidateとして管理し、fixed-goal依存と混ぜない。

## 5.1 目的と模型の境界

Q2-2の固定目標は、Bell型共同統計を古典構成で再現し、その構成についてBell不等式の導出に用いられる前提の成立・不成立を物理的因果構造と確率因子化に対応させて監査することである。どのBell前提を破るかは固定目標側で先に指定しない。

現行Q2-2には、役割の異なる二つの経路を明確に分ける。

1. **fixed-goal witness**：固定一重項4モード信号へA設定を作用し、A端M65で結果を固定した後、R181D型projector routerで非規格化結果成分をB端へ物理的に渡し、B設定とB端M65を作用するR180C逐次装置。
2. **Q2-2-S candidate**：M66/R205Eでsourceとsetting precursorを共同準備し、R205FでA/B相互作用とreservoir cross-correlationを距離とともに受動的に落とし、分離後はlocal responseだけを使うR207A--R207D経路。

両者は同じCHSH型統計を扱うが、Bell前提監査の位置が異なる。R180Cでは測定窓中にA端結果成分をB端へ物理的に渡すため、Bell局所因子化を仮定しない。一方R207 candidateでは、分離後のconditional responseは

```math
P(r,s\mid\lambda_S,x,y)
=
P_A(r\mid\lambda_A,x)
P_B(s\mid\lambda_B,y)
```

と因子化する候補であるが、CHSH witnessでは

```math
\rho(\lambda_S\mid x,y)
\neq
\rho(\lambda_S)
```

となり、測定設定独立性が成立しない。したがってR207はR180Cを置換せず、Q2-2 fixed-goalの直接依存にも追加しない。Q2-2-Sの定義・公式状態・現在地は `ENHANCEMENT_TARGETS.md` を正本とする。

M54の実際の1試行末端信号を

```math
Z\in\mathbb C^4,
\qquad
Z\neq0
```

とする。解析上の規格化 $V=Z/\|Z\|$ は確率式を短く書くためだけに使い、物理制御器は状態依存除算を行わない。

## 5.2 固定一重項源と試行順序

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

## 5.3 A端特殊化：binary selectorとR181Dから従うR180A

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

## 5.4 B端条件付き読出し

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

## 5.5 R180C：2端合成とBell監査

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

## 5.6 fixed-goalとstrengtheningの責務境界

R180Bのpaired-Hopf再準備、中央潜在結果を2翼へ複製する工程、切断後のA側再読出しは現行必須主線に使わない。これらは `notes/superseded_q2_2_paired_hopf_receiver.md` と退役付録へ保存する。

Q2-2 fixed-goalで新たに使う確率源はない。共同確率はbinary selector contractとR181Dの逐次Lüders telescopingから得る。現行証人ではA端・B端ともM65を用い、A端結果成分をB端へ同じ試行のまま物理的に渡すため、固定一重項・固定有限設定族・非空間分離という固定範囲でQ2-2を達成する。

Q2-2-Sはこの達成証人を空間局所化したものではなく、別の強化経路である。R205E/FとR207A--R207Dの成立・不成立はQ2-2 fixed-goalの達成判定を自動的に変更せず、R180Cの成立もQ2-2-Sを自動的に達成させない。永久記録、試行間reset、物理clock、次試行renewalまでの全周期統合はM0の独立課題とする。

## 5.7 Q2-2-S：common preparationとpassive separationのcandidate

### 5.7.1 一試行の因果順序

付録W/R207では、near-contact joint thermal preparation、passive separation、local setting latch、local outcomesの順で一試行を構成する。particle--reservoir couplingは準備時と分離後でswitchせず、A/B間相互作用 $K(R)$ とreservoir cross-correlation $C_{AB}(R)$ だけを距離によって受動的に弱める。

setting precursor $q_A,q_B$ は準備窓から存在し、source anglesと相関し得る。分離後に

```math
x=\frac{1-\operatorname{sgn}q_A}{2},
\qquad
y=\frac{1-\operatorname{sgn}q_B}{2}
```

をlocal recordへlatchする。本稿のR207 candidateでは、このlocal latch時刻をQ2-2-Sのsetting確定時刻

```math
t_A^{\rm set}=t_A^{\rm latch},
\qquad
t_B^{\rm set}=t_B^{\rm latch}
```

として扱う。ただしsetting recordを分離後に固定することは、準備時に生じたsource--setting precursor相関を消さず、測定設定独立性を回復しない。

### 5.7.2 R180CとR207のBell前提監査

| 項目 | R180C fixed-goal witness | R207 Q2-2-S candidate |
|---|---|---|
| source / setting関係 | 設定前一重項sourceを設定非依存に準備 | common preparationでsourceとsetting precursorが相関 |
| 測定窓中の端間伝播 | A結果成分をB端へ物理的に渡す | R205F分離後は端間結果伝播を使わない |
| local response factorization | Bell-local modelとして仮定しない | R207Cの分離後candidateでは成立 |
| measurement independence | 設定前sourceについて維持可能 | R207B/C witnessでは不成立 |
| operational marginal | 一重項共同分布で非信号 | 4-setting witnessで各局所周辺 $1/2$ |
| Q2-2 fixed-goal | 達成証人 | 直接依存ではない |

従って両構成はBell前提の異なる箇所を使う。R207B/CのCHSH破れは、分離後local response factorizationと両立する一方、source hidden-state distributionのsetting dependenceを明示する。

### 5.7.3 S0--S4の現在地

Q2-2-Sの段階定義と公式状態は `ENHANCEMENT_TARGETS.md` を正本とし、本節はその現在地の本文要約である。

| 段階 | 現在の証拠 | 現在地 |
|---|---|---|
| S0 | R180C | 非空間分離の基準系として確立 |
| S1 | R207A | 二端joint preparation候補あり。具体spatial trajectoryは未監査 |
| S2 | R205F + R207C | generator-level分離候補あり。finite-speed physical isolationは未閉包 |
| S3 | R207B + R207C | CHSH witnessとBell前提監査候補あり。S2物理実装に条件付き |
| S4 | R207D | Bell-local analytical controlあり |

S2の主要残件は、有限最大伝播速度 $v_{\max}$ を持つ具体spatial reservoirとtiming closureである。本candidateでは

```math
t_A^{\rm out}-t_B^{\rm set}<\frac{L}{v_{\max}},
\qquad
t_B^{\rm out}-t_A^{\rm set}<\frac{L}{v_{\max}}
```

を同じphysical implementationで閉じる必要がある。R205Fのgenerator factorizationだけからこの条件は従わない。

S3については、どのBell前提を破るかをQ2-2-Sの定義で先に固定してはいないが、現R207 witnessを監査した結果としてmeasurement independenceが成立しない。S4が解析的に閉じていてもS2/S3のphysical isolationを閉じたことにはならない。従ってQ2-2-S全体の公式状態は未監査のままとする。

### 5.7.4 非主張と残件

R207A--R207Dから、次をまだ主張しない。

1. continuous $q_A,q_B$ を含むfull Langevin trajectoryでのdirect numerical reproduction。
2. 有限伝播速度を持つ具体spatial reservoirからの $C_{AB}(R)$ の導出。
3. separation、setting latch、local outcome fixationを一つのfinite-speed timing modelで閉じること。
4. 具体的実験装置、実験可能parameter window、direct apparatus simulation。

candidate誤差台帳とCHSH安定性は第8章8.6.1、数理詳細は付録W/R207A--R207Dを参照する。
