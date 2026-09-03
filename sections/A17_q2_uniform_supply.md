@number: Q
@chapter: 付録
@title: M53の一様blank-bankとfresh-cell供給
@status: R179の反復partial SWAP、有限温度誤差、root入力、fair-bit源、dyadic座標化、独立供給則と資源境界を証明する。

## Q.1 目的と資源境界

R178C--R178Fは、各出力bitに新しいwork、anti-register、容量pointer、aperture cell、selector digitを要求する。本付録では、それらを回路出力に応じて外部から逐次生成せず、初期時刻に用意した一様bankからclock順に供給する。

許すものは、回路と精度から計算できる多項式長の外部program、指数個でもよい受動cell、cold sourceとspent sinkを含む開放bathである。総bath容量、総熱、装置体積を多項式とする主張は置かない。

## Q.2 閉Hamiltonian系だけではblankを増やせない

同じ有限次元位相空間上のHamiltonian流は体積を保存する。異なる使用済みmicrostateを同じblank領域へ写し、他の自由度にも区別を残さない写像は単射でない。従ってblank供給は、使用済み状態をspent側へ移すか、より大きいbankの未使用領域と交換しなければならない。

この障害を隠さないため、M53のbankを

```math
\mathcal B
=
\mathcal B_{\rm cold}
\times
\mathcal B_{\rm active}
\times
\mathcal B_{\rm spent}
```

と分ける。collective resetはactive状態を消去せず、cold cellと交換して履歴をspent側へ移す。

## Q.3 一様bank index

cellは種類 $a$、出力段 $k$、試行index $j$、標本index $s$ で静的に並べる。clockは同じ有限状態遷移規則で次のcellを選ぶ。外部controllerはcellのmicrostate、Born重み、accept結果を読まない。

必要数が事前に

```math
N_{\rm cell}
=
O(SnN)
```

と決まる有限runでは、bank全体を初期状態の一部として用意する。ここで $S$ は標本数、$N$ は1 bit当たりのaperture試行数である。無期限運転には同じ局所規則を持つ開放cell流を仮定する。

## Q.4 反復partial SWAP

bank全体のactive vector $W_r$ と第 $r$ cold layer $E_r$ の対応mode間に、一定精度のpartial SWAPとして同じ2-mode回転を並列に作用させる。couplerは一様有限規則から作る同一の静的二次Hamiltonianとし、受動clockがroundを進める。指数個のcouplerを外部から個別に開閉しない。適切な位相規約でactive出力を

```math
W_{r+1}
=
C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1
```

と書く。pairごとの全変換は $(w',e')=(cw+se,-sw+ce)$、$c^2+s^2=1$ という回転であり、実正準かつ可逆である。cold側出力 $e'$ はspent側へ残す。$C_r,S_r$ は固定精度で実装され、各回に同じ上界 $\rho$ が使える。full SWAPを指数精度で1回実装する必要はない。

cold layerのaggregate blankずれを $\|E_r\|\leq\eta_{\rm cold}$ とし、$\|S_r\|\leq1$ を使えば

```math
\|W_R\|
\leq
\rho^R\|W_0\|
+\frac{\eta_{\rm cold}}{1-\rho}.
```

従って $\|W_0\|\leq R_{\rm in}$ に対し

```math
R
=
O\!\left(
\log R_{\rm in}
+\log\frac{1}{\varepsilon_{\rm blank}}
\right)
```

回の反復で、cold floorを除く残差を $\varepsilon_{\rm blank}$ 以下にできる。$R_{\rm in}$ が $2^{O(n)}d^{O(1)}$ 以下なら $R=O(n+\log d+\log(1/\varepsilon_{\rm blank}))$ である。

## Q.5 Cold floorとpassive容量

有限温度bathでは $\eta_{\rm cold}=0$ を仮定しない。実効blank誤差は

```math
\varepsilon_{\rm reset}
=
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho}
+\varepsilon_{\rm swap}
```

と評価する。$\varepsilon_{\rm swap}$ は反復実装誤差の合計である。要求精度を下げるにはcold sourceの品質または反復gate精度を上げる必要がある。外部精度を多項式に保つには、exact invariant blankを持つcold source、またはbank全体のaggregate誤差を一様contractで保証するsourceを仮定する。各modeに独立な定数thermal noiseが残るsourceは、bank次元とともにaggregate誤差が増えるためこの仮定を満たさない。

各反復で用いたcold cellはactive履歴と相関し得るため、再びcold cellとして数えない。有限runでは必要数を初期bankに積み、無期限runではcold流とspent sinkを仮定する。この容量は指数的でもよい受動資源であり、外部制御programの長さとは区別する。

## Q.6 Root入力の供給

R112のclockを開始するroot packetは、固定した1個のsource modeと最初のactive clock modeの間の定数次元SWAPで注入できる。sourceの絶対位相は、以後の判定が作用と相対位相だけに依存する限りglobal phaseとして消える。

標本ごとにroot packetを再利用するなら、source側の使用済み状態を保持するか、新しいsource cellへ進む。rootを閉系から無履歴で複製するとは主張しない。

## Q.7 一様fair-bit源

R161--R162の対称2状態collision bathを、selector digitのsourceとして使う。遷移核を

```math
K
=
\begin{pmatrix}
1-a&a\\
a&1-a
\end{pmatrix},
\qquad
0<a<1
```

とすれば定常分布は $(1/2,1/2)$ である。mixing後の1-bit lawのずれを $\varepsilon_{\rm bit}$、cell間相関の総寄与を $\varepsilon_{\rm corr}$ として追跡する。独立性を近似だけで済ませる場合、その誤差を $\varepsilon_{\rm tape}$ へ含める。

初期bath法則は、回路、入力signal、途中の出力から独立でなければならない。回路のBorn重みを初期digit分布へ埋め込まない。

## Q.8 Dyadic座標とthreshold discrepancy

$k$ 個のfair digit $C_1,\ldots,C_k\in\{0,1\}$ から

```math
J_k
=
\sum_{\ell=1}^k2^{k-\ell}C_\ell,
\qquad
U_k
=
A_{\max}\frac{J_k+1/2}{2^k}
```

を作る。$U_k$ は各dyadic区間の中点に一様に分布する。連続一様変数とのtotal variation距離は比較しない。両者は測度として互いに特異だからである。

代わりにthreshold classに対する累積分布差を使う。任意の $0\leq A\leq A_{\max}$ について

```math
\left|
\Pr[U_k<A]
-\frac{A}{A_{\max}}
\right|
\leq2^{-k}.
```

従って $nN$ 回のthreshold判定に対する合計discrepancyを $\epsilon$ 以下にするには $k=O(\log(nN/\epsilon))$ で足りる。

## Q.9 Data processingと供給独立性

理想product lawを $\mu^{\otimes L}$、実際のtape lawを $\widetilde\mu_L$ とする。回路とapertureの決定的な拡大正準流を $\Phi$ と書けば、任意の可測粗視化に対し

```math
D_{\rm TV}
\left(
\Phi_*\widetilde\mu_L,
\Phi_*\mu^{\otimes L}
\right)
\leq
D_{\rm TV}
\left(
\widetilde\mu_L,
\mu^{\otimes L}
\right).
```

従ってbit bias、有限mixing、cell間相関の誤差は、最終出力で増幅されず $\varepsilon_{\rm tape}$ として一度だけ加えられる。ただし回路依存の初期相関がある場合、この議論は使えない。

## Q.10 R179の証明

<!-- theorem-start:proof -->
**証明（R179）**

Q.3の静的indexとR112のclockにより、必要なcellを出力に依存しない順序で供給できる。Q.4--Q.5の反復partial SWAPはactive modeを所望のblank近傍へ移し、使用済みmicrostateをcold cellからspent側へ送る。同一静的couplerと受動clockを使うため、外部controllerのquench workをbank次元へ比例させない。Q.6がroot packet、Q.7--Q.8が回路非依存のdyadic selector tapeを与える。Q.9により供給法則のずれは最終出力誤差へ加法的に伝わる。

有限runでは初期bank容量を必要数だけ取ればよい。無期限runではcold inflowとspent outflowを仮定する。以上により、総bath容量を多項式と仮定せず、外部program、反復段数、1判定当たりdigit数を多項式に保つ一様供給が成立する。証明終。
<!-- theorem-end:proof -->

## Q.11 資源評価

1回のblank化に必要なpartial SWAP数は

```math
O\!\left(
n+\log d+\log\frac{1}{\varepsilon_{\rm blank}}
\right).
```

1 threshold当たりのdigit数は $O(\log(nN/\epsilon))$、R178Eのcell試行数は $N=O(\log(n/\epsilon))$ である。固定標本数 $S$ の外部clock長はこれらと $d,n,S$ の多項式である。

一方、signal、work、history、cold、spentを含む受動bank容量と総散逸は指数的でよい。この分離がQ2-4の現在の規則であり、通常の意味の効率的古典simulationや多項式総熱を意味しない。

## Q.12 反証条件と非主張

次のいずれかが必要ならR179は成立しない。

- cold cellが回路出力に応じて準備される。
- 使用済みcellを履歴なしにcold cellへ戻す。
- 1回のSWAPに指数小の較正誤差を要求する。
- dyadic tapeの離散lawと連続一様lawのtotal variation一致を要求する。
- bath容量または総熱を多項式に制限する。

R179は、cold bathを閉Hamiltonian dynamicsから生成すること、指数受動資源を削減すること、無期限運転を有限bankで行うことを主張しない。
