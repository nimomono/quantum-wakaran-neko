@number: O
@chapter: 付録
@title: M54の一様registerとprojector-tree代数
@status: R181Cの一様gate作用と、R181Dで使うlatch、可逆2枝filter、Born確率のtelescoping、raw cutoff、radial-only repumpを検算する。

## O.1 目的と記号

$n$ bit文字列の集合を $\Omega_n=\{0,1\}^n$、信号空間を $\mathcal H_n=\mathbb C^{\Omega_n}$ とする。複素信号 $Z$ は実正準対の派生表示であり、量子状態を別の実体として追加しない。M54は $\dim\mathcal H_n=2^n$ を受動状態容量として許すが、外部controllerに $2^n$ 個の係数またはaddressを渡さない。

固定有限gate集合を $\mathcal G$ とする。programは $(g,S,t)$ の有限列で、$g\in\mathcal G$、$|S|\leq2$、$t$ はclock窓である。最終確率表はprogramに含めない。

## O.2 一様sector生成子

$S$ に属さないbit列を $r$ とする。基底を $(s,r)$ の順へ並べれば、局所gateの理想作用は

```math
U_{g,S}
=
\bigoplus_{r\in\{0,1\}^{n-|S|}}g.
```

対応する実正準Hamiltonianは第2.2節と同じく

```math
H_{g,S}(t)=Z^\dagger h_{g,S}(t)Z,
\qquad
h_{g,S}(t)=\bigoplus_r h_g(t)
```

である。blockごとの項は異なる正準pairへ作用するため、同じclock係数を共有できる。静的辺は、対象bitだけが異なりspectator bitが一致する文字列pair、という有限規則で生成される。

## O.3 R181Cの証明

<!-- theorem-start:proof -->
**証明（R181C）**

sector間漏れがない場合、

```math
\widetilde U_{g,S}-U_{g,S}
=
\bigoplus_r(\widetilde g_r-g)
```

だから、直和の作用素normにより

```math
\|\widetilde U_{g,S}-U_{g,S}\|
=
\max_r\|\widetilde g_r-g\|
\leq\eta_g.
```

漏れ作用を $E_{\rm leak}$ とすれば三角不等式で $\eta_g+\eta_{\rm leak}$ を得る。gate列 $U_d\cdots U_1$ と $\widetilde U_d\cdots\widetilde U_1$ の差はtelescopingし、各因子のnormが1なら各窓誤差の和以下である。

1 bit gateはbit indexを指定する $O(n)$ 本以下、2 bit gateは素朴にはpairを指定する $O(n^2)$ 本以下の共有busで足りる。外部命令はgate数 $d$ に比例する。静的block数は指数的でも、blockを列挙する外部表は不要である。証明終。
<!-- theorem-end:proof -->

共有係数 $\chi(t)$ で $H(t)=\chi(t)H_{g,S}$ を開閉する場合、固定作用殻上の制御仕事は

```math
|W_{\rm ctrl}|
\leq
\int|\dot\chi(t)|\,\|h_g\|\,\|Z(t)\|^2\,dt
```

で抑えられる。この評価はoccupied signal作用を数え、空sector数を足し上げない。ただし結合器の製造費と受動体積は指数的でもよい資源として別に記録する。

## O.4 2枝容量latch

計算基底bit $k$ の射影は

```math
P_{k,b}
=
\sum_{x:x_k=b}|x\rangle\langle x|.
```

容量pointer $(Q^A_{k,b},P^A_{k,b})$ と滑らかなclock窓 $\lambda_k$ に対し、理想latch生成子を

```math
H_{{\rm lat},k}
=
\lambda_k(t)
\sum_{b=0}^1
\mathcal J_0Z^\dagger P_{k,b}Z\,P^A_{k,b}
```

とする。$P^A_{k,b}=0$ のblank面ではsignal方程式への反作用が消え、pointer位置だけが容量に比例して移る。有限pointer幅、clock overlap、blank momentum誤差は $\varepsilon_{{\rm lat},k}$ へ入れる。

## O.5 可逆filter代数

$P=P_{k,b}$、$Q=I-P=P_{k,1-b}$ と略記する。$PQ=QP=0$、$P^2=P$、$Q^2=Q$ だから、

```math
F^2
=
\begin{pmatrix}
P^2+Q^2&PQ-QP\\
QP-PQ&Q^2+P^2
\end{pmatrix}
=I.
```

$F=F^\dagger$ なので $F^\dagger F=I$ でもある。複素unitaryは実正準座標上のsymplectic直交変換を与える。

## O.6 R181Dの証明

<!-- theorem-start:proof -->
**証明（R181D）**

O.5より $F_{k,b}$ はunitaryかつinvolutionである。blank workを代入すると第1出力は $P_{k,b}Z$、第2出力は $P_{k,1-b}Z$ になる。O.4のlatchはblank momentum面で信号を変えない。射影はbit labelだけで決まるため、signal成分の列挙を必要としない。証明終。
<!-- theorem-end:proof -->

## O.7 逐次Born確率

履歴 $y_{<k}$ のprojectorを

```math
P_{y_{<k}}
=
P_{k-1,y_{k-1}}\cdots P_{1,y_1}
```

とする。非零履歴上の条件付き確率は

```math
p_{k,b|y_{<k}}
=
\frac{
\|P_{k,b}P_{y_{<k}}Z_0\|^2
}{
\|P_{y_{<k}}Z_0\|^2
}.
```

分母と次段分子が相殺するので、全履歴確率は

```math
\prod_{k=1}^np_{k,y_k|y_{<k}}
=
\frac{\|P_yZ_0\|^2}{\|Z_0\|^2}.
```

## O.8 希少枝切断

第 $k$ 段で条件付き確率が $\tau$ 未満の子枝を全て数える。各親履歴の下には高々2個の子があるため、その親から切られる条件付き質量は $2\tau$ 以下である。親履歴の確率を掛けて全親について和を取ると、第 $k$ 段の切断質量は $2\tau$ 以下。段の和により

```math
P_{\rm cut}\leq2n(\tau+\gamma).
```

切断枝は $\varnothing$ として残すので、これは事後選別ではない。

## O.9 Radial repump

selected signal $W$ にR181Aの $\kappa=0$ radial-only portを作用させる。

```math
\dot W=g(J_*-W^\dagger W)W.
```

この流れはrayを変えない。accept plateauでは初期作用に $\tau$ から決まる正の下限があるので、目標作用への相対誤差を $\eta_R$ 以下にする時間は $O(\log(1/(\tau\eta_R)))$ である。時間は試行前に固定でき、未知の条件付き確率を読み取るsqueezeを使わない。開放環境はradial履歴を保持し、使用後にblankとみなさない。

## O.10 R181Dの証明と誤差

<!-- theorem-start:proof -->
**証明（R181D）**

理想確率はO.7のtelescopingによりBorn分布へ一致する。O.8が切断・guard質量、O.9が固定時間repumpを与える。正則化を各段で最大 $\delta/(1+\delta)$、各段の実装channel誤差を $\bar\varepsilon_k$ とすればMarkov kernelのtelescopingにより

```math
D_{\rm TV}
\leq
2n(\tau+\gamma)
+\frac{n\delta}{1+\delta}
+\sum_{k=1}^n\bar\varepsilon_k
```

を得る。初期signalまたはgate列の誤差は、実際の末端signalのBorn分布と理想回路分布の距離として先頭に一度だけ加える。証明終。
<!-- theorem-end:proof -->

## O.11 資源と非主張

各段のactive subspaceを物理的に圧縮しない保守的実装では、signal、anti、work、historyは $O(n2^n)$ modeを使う。縮小subspaceを詰めれば $O(2^n)$ まで減らせる可能性があるが、本結果に不要である。外部gate命令は $O(d)$、逐次出力段は $n$、nodeごとのcollision・repump資源は付録Pで評価する。

本付録は未知量子入力、適応中間測定、誤り訂正、空間局所Hamiltonian、指数受動資源の削減を主張しない。
