@number: D
@chapter: 付録
@title: M54駆動設定先行2端R191受信機構の証明
@status: R180AをR191--R181DのA端特殊化として確認し、R180Cの共同Born分布、非信号性、CHSH値、有限全変動誤差、Bell前提監査を証明する。

## D.1 R180Aの特殊化確認

<!-- theorem-start:proof -->
**証明（R180A）**

$P_{A,+}^{x}+P_{A,-}^{x}=I$ なので

```math
J_{A,+}+J_{A,-}
=\mathcal J_0\|Z\|^2.
```

R191の理想2結果則を適用すると

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

A端保持・basis gate誤差を $\varepsilon_A^{\rm pre}$、A端R191を $\varepsilon_{191}^{A}$、routerを $\varepsilon_{\rm route}$、B端basis gateを $\varepsilon_B^{\rm basis}$、B端R191を $\varepsilon_{191}^{B}$、記録を $\varepsilon_{\rm rec}$ とする。同じ偏差を重複計上しなければkernel telescopingから

```math
\varepsilon_{180}
\leq
\varepsilon_A^{\rm pre}
+\varepsilon_{191}^{A}
+\varepsilon_{\rm route}
+\varepsilon_B^{\rm basis}
+\varepsilon_{191}^{B}
+\varepsilon_{\rm rec}.
```

完全結果分布の全変動距離が $\varepsilon_{180}$ 以下なら、任意の周辺事象の確率差も同じ上界以下である。また $rs\in[-1,1]$ なので各相関の差は $2\varepsilon_{180}$ 以下、4項CHSHの差は $8\varepsilon_{180}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

D.1のA端R191とrouter、D.2の条件付きB端R191を合成すると理想共同分布を得る。有限実装では各段をMarkov kernelとして同じ完全結果集合へ埋め込み、kernelの全変動距離の三角不等式を順に適用すれば上の $\varepsilon_{180}$ が得られる。非信号性、CHSH安定性はD.3と有界観測量の全変動安定性から従う。A結果結果成分がB端へ転送されるため、切断後局所性は結論にも仮定にも含めない。
<!-- theorem-end:proof -->
