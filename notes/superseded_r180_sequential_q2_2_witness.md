# R180A/R180C sequential Q2-2 witness の退役

現行注記：draft-135でR180A/R180CとA→B逐次Bell経路をactive paperから退役した。Q2-2 fixed-goalはdraft-134で昇格したM66/R205--R207 projection phase-volume主線だけで維持する。R180A/R180Cの結果IDは再利用しない。

## 退役理由

R180A/R180Cは誤りとして撤回するのではない。設定前4モードsinglet、A端binary selector、R181D projector router、B端binary selectorを順次接続すれば、singlet共同分布、非信号周辺、CHSH/Tsirelsonを再現できる非空間分離逐次witnessとして成立する。

一方、R207A--R207Cはprojection phase-volume共同準備、passive separation、local outcome/recordから一般Bloch方向のsinglet共同統計を閉じ、測定窓中のA結果成分からB端へのresult-component transmissionを必要としない。Q2-2の現行主線を一本化するため、Theory A/R180系をactive paperから退役する。

M65/R204、R181D、R112、M54、R179自体は退役しない。M65/R181DはQ1逐次測定で引き続きactiveであり、R179は一般open reset/full-cycle strengthening側に残る。

## 最終active本文（draft-134）

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


## 最終active付録D（draft-134）

@number: D
@chapter: 付録
@title: M54駆動設定先行2端binary-selector受信機構の証明
@status: R180Aをbinary selector--R181DのA端特殊化として確認し、R180Cの共同Born分布、非信号性、CHSH値、有限全変動誤差、Bell前提監査をselector内部物理に依存せず証明する。現行fixed-goal実装はA/B両端M65を使う。

## D.1 R180Aの特殊化確認

<!-- theorem-start:proof -->
**証明（R180A）**

$P_{A,+}^{x}+P_{A,-}^{x}=I$ なので

```math
J_{A,+}+J_{A,-}
=\mathcal J_0\|Z\|^2.
```

binary selector contractの理想2結果則を適用すると

```math
P(r\mid Z,x)
=\frac{\|P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

結果固定後、共通対合router $F_{A,r}$ は未使用作業領域に対して

```math
F_{A,r}(Z,0)
=
(P_{A,r}^{x}Z,(I-P_{A,r}^{x})Z)
```

と作用する。従ってB端へ渡す結果成分は $P_{A,r}^{x}Z$ であり、状態依存規格化を物理操作として行わない。
<!-- theorem-end:proof -->

## D.2 逐次共同分布

B端の理想条件付き確率は

```math
P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|P_{A,r}^{x}Z\|^2}.
```

従って

```math
P(r,s\mid x,y)
=P(r\mid x)P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

これは付録Tの有限段Lüders telescopingの深さ2特殊化である。局所射影は異なるtensor因子へ作用するため可換であり、測定順序による理想共同分布の変更はない。

## D.3 一重項、非信号性、CHSH

固定一重項型信号ではPauli方向 $\boldsymbol a_x,\boldsymbol b_y$ に対し

```math
P(r,s\mid x,y)
=
\frac14\left(1-rs\,\boldsymbol a_x\cdot\boldsymbol b_y\right).
```

$s$ または$r$ を和すれば両周辺は $1/2$ であり、理想共同分布は非信号性を満たす。相関は

```math
E(x,y)
=-\boldsymbol a_x\cdot\boldsymbol b_y
```

であり、標準の4方向を取れば

```math
|S_{\rm CHSH}|=2\sqrt2.
```

これは非空間分離の共同装置の入出力統計であり、Bell局所factorizationから導いたものではない。

## D.4 有限誤差

A端保持・basis gate誤差を $\varepsilon_A^{\rm pre}$、A端selectorを $\varepsilon_{\rm sel}^{A}$、routerを $\varepsilon_{\rm route}$、B端basis gateを $\varepsilon_B^{\rm basis}$、B端selectorを $\varepsilon_{\rm sel}^{B}$、記録を $\varepsilon_{\rm rec}$ とする。現行M65実装では $\varepsilon_{\rm sel}^{A,B}=\varepsilon_{65}^{A,B}$ と置く。同じ偏差を重複計上しなければkernel telescopingから

```math
\varepsilon_{180}
\leq
\varepsilon_A^{\rm pre}
+\varepsilon_{\rm sel}^{A}
+\varepsilon_{\rm route}
+\varepsilon_B^{\rm basis}
+\varepsilon_{\rm sel}^{B}
+\varepsilon_{\rm rec}.
```

完全結果分布の全変動距離が $\varepsilon_{180}$ 以下なら、任意の周辺事象の確率差も同じ上界以下である。また $rs\in[-1,1]$ なので各相関の差は $2\varepsilon_{180}$ 以下、4項CHSHの差は $8\varepsilon_{180}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

D.1のA端selectorとrouter、D.2の条件付きB端selectorを合成すると理想共同分布を得る。有限実装では各段をMarkov kernelとして同じ完全結果集合へ埋め込み、kernelの全変動距離の三角不等式を順に適用すれば上の $\varepsilon_{180}$ が得られる。非信号性、CHSH安定性はD.3と有界観測量の全変動安定性から従う。A結果結果成分がB端へ転送されるため、切断後局所性は結論にも仮定にも含めない。
<!-- theorem-end:proof -->

