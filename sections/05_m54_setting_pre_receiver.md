@number: 5
@chapter: 本文
@title: M54駆動逐次2端binary-selector受信機構とBell前提監査
@status: 固定一重項4モード信号をA設定で分解し、A端binary selectorの結果成分をprojector routerでB端へ直接渡し、B設定後のB端selectorと組み合わせる。R180A/R180Cをselector内部物理から独立化する。現行fixed-goal証人はA/B両端R191を維持する。

## 5.1 目的と模型の境界

Q2-2の固定目標は、Bell型共同統計を古典構成で再現し、その構成についてBell不等式の導出に用いられる前提の成立・不成立を監査することである。どのBell前提を破るかは固定目標側で指定しない。本節の現行証人は、固定一重項、固定有限設定族、非空間分離の逐次古典装置であり、二つの物理的な2値読出し端から量子一重項と同じ共同入出力統計を作る。現行証人について空間分離Bell局所模型またはloophole-free Bell実験の古典局所説明は主張しない。

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
4. A結果射影作用 $J_{A,\pm}$ を保持し、A端binary selectorを走らせて $r$ を固定・記録する。現行証人ではR191を使う。
5. R181Dと同じprojector routerで非規格化結果成分 $P_{A,r}^{x}Z$ をB端へ渡す。
6. B端で $I\otimes U_y^\dagger$ を作用し、B結果射影作用を保持する。
7. B端binary selectorを走らせて $s$ を固定・記録する。現行証人ではR191を使う。
8. 外部記録を残し、必要な能動部をR179のopen resetへ渡す。

A端とB端は別々のbinary selectorと記録を持つ。現行証人では各selectorをR191のBrownian macrospinで実装する。結果成分の物理転送があるため本装置は非空間分離である。

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

R180AのA端作用保持・binary selector・projector router、B設定gate、B端作用保持・binary selector、二つの局所記録、および反復時のR179 open resetが同じ有限時計割当と安全集合上で実行できるとする。理想極限の完全結果共同分布は

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

## 5.6 責務境界

R180Bのpaired-Hopf再準備、中央潜在結果を2翼へ複製する工程、切断後のA側再読出しは現行必須主線に使わない。これらは `notes/superseded_q2_2_paired_hopf_receiver.md` と退役付録へ保存する。

Q2-2で新たに使う確率源はない。共同確率はbinary selector contractとR181Dの逐次Lüders telescopingから得る。本draftのfixed-goal証人ではA端・B端ともR191を用い、M65への実装切替は行わない。Q2-2の条件付き達成ラベルは維持する。現行R180C証人が非空間分離であることと、Q2-2固定目標自体が特定のBell前提違反を指定しないことを区別する。空間隔離をどこまで強められるかは `Q2-2-S` の独立強化課題とする。
