@number: Q
@chapter: 付録
@title: M54の一様blank-bank・collision-cell・spent供給
@status: R179の反復partial SWAP、aggregate cold誤差、root入力、R162 collision cell、selector/filter work、spent履歴の供給則と資源境界を証明する。

## Q.1 目的と供給対象

M54の一般 $n$ 特殊化は、$2^n$ signal mode、gate work、R181Dのraw/regularized容量pointer、selector、filter work、radial-port環境、R162 collision cell、外部recordを使う。これらを回路出力に応じて外部生成せず、試行開始前に用意したbankからclock順に供給する。

有限runでは必要bank全体を初期状態に含める。無期限runでは同じ局所規則を持つcold inflowとspent outflowを仮定する。有限閉Hamiltonian系が低作用blankを無制限に増やすとは主張しない。

## Q.2 一様bank index

bank modeのindexは

```math
(\mathrm{kind},k,r,j)
```

とする。$\mathrm{kind}$ はsignal、pointer、selector、filter、collision、radial、recordの有限種類、$k$ は回路または読出し段、$r$ はblanking round、$j$ はsector indexである。隣接indexへ同じ形のcouplerを置く有限生成規則を使い、外部programは個々の $j$ を列挙しない。

## Q.3 反復partial SWAP

active bankを $W_r$、incoming cold layerを $E_r$ とする。対応pairへ、一様有限規則から作る同一の静的二次Hamiltonianによる同じ2-mode rotationを一括作用させると

```math
W_{r+1}=C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1.
```

各pairの全変換は実正準かつ可逆で、cold側出力をspentへ保持する。active成分だけを捨てない。$\|E_r\|\leq\eta_{\rm cold}$ なら

```math
\|W_R\|
\leq
\rho^R\|W_0\|
+\eta_{\rm cold}\sum_{j=0}^{R-1}\rho^j
\leq
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho}.
```

## Q.4 Aggregate cold条件

Q2-4で必要なのはmodeごとの温度上界ではなく、bank全体のaggregate norm上界である。独立な各modeが定数noise floorを持てば、$2^n$ modeのaggregate誤差は一般に増大する。この場合R179の多項式精度条件を満たさない。

許される供給は、exact invariant blank、またはbank全体で $\eta_{\rm cold}=O(\epsilon/\operatorname{poly}(n,d))$ を保証する一様contractである。cold sourceの受動容量、装置体積、総作用移送、総熱は指数的でもよいが、外部controllerがmodeごとに較正してはならない。

## Q.5 Root入力

一般 $n$ 入力はR181Bの反復tensor-liftで作らない。定数次元source packet $s$ を一様tree couplerへ入れ、$0^n$ root modeとblank bankの間でpartial SWAPする。理想的には

```math
Z_{0^n}=s,
\qquad
Z_x=0\quad(x\neq0^n).
```

他の計算基底入力は回路先頭のR181C $X$ gateで作る。未知振幅表のloadはR179のinterfaceに含めない。

## Q.6 Collision cellとselector供給

R181Dの各nodeはR161率を有限時間近似するR162 collision cellを使う。cellの初期lawは回路出力、raw容量、将来のselector値と独立に取り、branchに依存しない同じ有限局所分布から供給する。容量依存性はR170の局所相互作用にだけ入る。

selectorとfilter workはblank幅以内へpartial SWAPで準備する。使用後は、selector結果、filterに退避した非選択信号、collision履歴、radial-port履歴をspentへ送る。結果を保持したまま全てを同じblank点へ戻さない。

## Q.7 R179の証明

<!-- theorem-start:proof -->
**証明（R179）**

Q.3の幾何級数評価により、$R_{\rm in}\leq\exp p_1(n,d)$ なら

```math
R
=
O\!\left(
n+\log d+\log(1/\varepsilon_{\rm blank})
\right)
```

回の一様partial SWAPでactive bankを所望のblank幅へ入れられる。Q.2のindex規則により外部命令はbank次元でなくround数に比例する。Q.5がroot入力、Q.6がcollision、selector、filter、spent供給を与える。各供給kernelの全変動距離またはsafe-set失敗率を足せば

```math
\varepsilon_{179}
\leq
C_{\rm root}
(\varepsilon_{\rm blank}+\varepsilon_{\rm src}+\varepsilon_{\rm swap})
+\varepsilon_{\rm coll}
+\varepsilon_{\rm selector}
+\varepsilon_{\rm clock}.
```

供給法則は回路出力確率を含まず、deterministicな下流写像は全変動距離を増やさない。以上で本文のR179を得る。
<!-- theorem-end:proof -->

## Q.8 資源境界と非主張

外部program長、blanking round、clock精度、collision精度は $n,d,1/\epsilon$ の多項式である。signal、work、history、cold、spentの受動自由度と状態容量、総作用移送、総熱は $2^n\operatorname{poly}(n,d,1/\epsilon)$ まで許す。これは通常の効率的古典simulationではない。

R179は次を主張しない。

1. cold bathを有限閉Hamiltonian系から無制限に生成すること。
2. 有限bankを無期限運転し、使用済みcellを履歴なしにblankへ戻すこと。
3. 指数的な受動容量、装置体積、総熱を多項式へ削減すること。
4. 結果確率、振幅表、mode別較正値を外部から供給すること。
5. 旧fair-bit、dyadic threshold、aperture tapeをR181Dに必要とすること。
