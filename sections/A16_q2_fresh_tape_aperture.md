@number: P
@chapter: 付録
@title: M53のhistory処理と滑らかなaperture散乱
@status: R178D--R178Fの履歴逆掃除、reset境界、fixed-volume fresh tape、first-index選択、滑らかなaperture Hamiltonianと有限時間誤差を証明する。

## P.1 目的

本付録はR178Cが各出力bitで要求する2枝選択を物理化する。容量 $A_0,A_1$ に比例する可変体積の殻をblankから生成せず、固定体積のfresh cellを容量依存apertureへ通す。全cell、拒否履歴、容量pointerを含む拡大流は1対1に保ち、無反応を正式な結果とする。

## P.2 履歴の分類

$Y\in\{0,1\}^n$ をbit data記録、$F\in\{0,1\}$ を無反応flagとし、完全結果は $(Y,F)$ として保持する。$H(Y)\leq n\log2$ はdata記録だけの上界であり、flagと微視的履歴に必要な容量を除外しない。

1段の状態を

```math
\Gamma_k
=
(Z_k,W_k,R_k,A_k,C_k,D_k,H_k)
```

と書く。$W_k$ はfilter work、$R_k$ はrepump anti-register、$A_k$ は容量pointer、$C_k$ は使用したaperture cell、$D_k$ は出力記録、$H_k$ はclockとselector履歴である。

出力copy後に逆演算できるのは、出力値を条件として選ばずに完全な微視的入力が残る部分だけである。粗視化した結果、Markov遷移回数、平均容量だけから逆写像を作らない。

## P.3 R178Dの証明

<!-- theorem-start:proof -->
**証明（R178D）**

R112のclock、SWAP、比較、記録とR178Bのfilterは拡大正準空間上の1対1写像である。repumpもanti-registerを保持すればsymplecticである。従って出力を空recordへcopyした後、記録剪断を逆実行せず、出力と相関しないworkを逆順に戻せる。

一方、異なる完全結果 $(y,f)\neq(y',f')$ を持つ2入力が、同じ保持出力を残しながら装置とbathの同一点へ戻ると仮定すると、全写像の2入力が同じ全出力へ写り単射性に反する。従って結果と相関する自由度はspent側へ残る。spent状態から $Y$ を復号する誤り率を $p_{\rm e}$ とし、Fano補正を $\eta_{\rm F}=h_2(p_{\rm e})+p_{\rm e}\log(|\mathcal Y|-1)$ と置けば、nats単位で $C_{\rm spent}\geq H(Y)-\eta_{\rm F}$ である。$n$ bit dataでは別に $H(Y)\leq n\log2$ である。証明終。
<!-- theorem-end:proof -->

熱量への変換にはbath温度、準静的消去、仕事源を別に指定する必要がある。本定理は情報容量だけから総熱を同定しない。

## P.4 Fixed-volume cell

各cellの容量を $0\leq A_b\leq A_{\max}$ とし、入口位相領域を

```math
\Gamma_{\rm cell}
=
\{0,1\}\times[0,A_{\max}]\times\Gamma_{\rm aux}
```

と表示する。離散labelは実装ではP.8の連続selector井戸に持ち上げる。理想入口測度はlabelが等重み、$U$ が平坦、auxiliary測度が全branchで同じとする。

branch $b$ のaccept領域は

```math
\mathcal A_b
=
\{B=b,\ 0\leq U<A_b\}.
```

その入口測度は共通因子を除いて $A_b/(2A_{\max})$ である。R164の作用殻体積をさらに掛けない。

## P.5 First-index法

各cellをindex $j=1,\ldots,N$ の順に、同じ長さのclock窓で試す。最小indexのacceptを出力し、それ以前が全てrejectなら次cellへ進む。物理的な出口到着時刻で競争させない。

1 cellでbranch $b$ がacceptされる確率を $q_b$、rejectを $r$ とする。最初のacceptがbranch $b$ である確率は

```math
\sum_{j=1}^Nr^{j-1}q_b
=
q_b\frac{1-r^N}{1-r}
=
\frac{A_b}{A_0+A_1}(1-r^N).
```

全rejectは $r^N$ である。

## P.6 R178Eの証明

<!-- theorem-start:proof -->
**証明（R178E）**

P.4で $q_b=A_b/(2A_{\max})$、$1-r=q_0+q_1$。P.5の幾何和から定理の分布を得る。理想branch分布へ同じ総質量 $1-r^N$ を割り当て、残りを $\varnothing$ とすれば、理想Born出力だけを持つ分布との差は失敗質量 $r^N$ である。

$A_0+A_1\geq S_->0$ なら $r\leq1-S_-/(2A_{\max})<1$ なので、$nr^N\leq\epsilon$ を満たす $N$ は $O(\log(n/\epsilon))$ である。証明終。
<!-- theorem-end:proof -->

同じcell列を別試行で再利用すると、出力とcell microstateが相関しているため独立同分布性は従わない。有限試行数なら別のfresh列を用意し、無期限運転なら開放cell流を必要とする。

## P.7 Aperture Hamiltonian

反応座標 $(X,P_X)$ と基準barrier $V_0$ を置く。branch selectorの連続座標を $Q_B$、2つの安全井戸上で一定になる滑らかな関数を $\beta_b(Q_B)$ とし、$\beta_0+\beta_1=1$ とする。

```math
A(Q_B)
=
\beta_0(Q_B)A_0+\beta_1(Q_B)A_1.
```

相互作用は

```math
H_{\rm ap}
=
\frac{P_X^2}{2m}
+V_0(X)
+g\{U-A(Q_B)\}\rho(X)
+H_{\rm hold}.
```

$H_{\rm hold}$ はselector、容量pointer、$U$ の安全領域を保持する。$V_0(0)=E_0$、$\rho(0)=1$ なら頂上energyは $E_0+g(U-A_b)$。入口energy $E_0$ に対し $U<A_b$ で通過、$U>A_b$ で反射する。

## P.8 滑らかなlabelと境界失敗

抽象離散変数を滑らかなHamiltonianへ直接代入しない。selectorの左右安全井戸 $\mathcal W_0,\mathcal W_1$ では

```math
\beta_b=1,
\qquad
\beta_{1-b}=0.
```

井戸間の遷移帯はlabel failureへ送る。その入口質量を $\varepsilon_{\rm label}$ とする。R179のdyadic digitも同じplateau方式で $U_k(Q)$ として結合し、controllerがbit列を読み取らない。

## P.9 余分な極値の排除

相互作用窓の外縁では

```math
\partial_XH_{\rm ap}
=
V_0'(X)+g\{U-A(Q_B)\}\rho'(X).
```

$|U-A(Q_B)|\leq A_{\max}$ とし、

```math
gA_{\max}\|\rho'\|_\infty
<
\inf_{{\rm supp}\,\rho'}|V_0'|
```

なら、$\rho'$ のsupport上で摂動項は基準傾斜を反転できない。従って予定外の停留点を作らない。

## P.10 有限時間境界幅

barrier頂上近傍を逆調和近似すると、separatrixからenergy差 $|\Delta|$ の軌道が判定領域を出る時間は $\omega^{-1}\log(C/|\Delta|)$ で増える。energy幅、較正幅を加えると、時間 $T$ で未判定となる容量境界幅は

```math
\ell_{\rm eff}(T)
=
\frac{
\Delta_E+\Delta_{\rm cal}
+C_0e^{-\omega(T-t_0)}
}{g}.
```

従って $\ell_{\rm eff}=O(\epsilon/n)$ には $T=O(\log(n/\epsilon))$ で足りる。有限時間の滑らかな流でhard thresholdを正確に実装するとは主張しない。

## P.11 Backreaction

Hamilton方程式から

```math
\dot P_{A_b}
=
g\beta_b(Q_B)\rho(X),
\qquad
\dot P_U=-g\rho(X).
```

容量座標 $A_b$ と $U$ が変化しなくても共役momentumは散乱履歴を持つ。逆散乱しない運転ではpointerとcellをspent側へ送る。1標本で必要な容量pointerは $O(n)$ である。

## P.12 R178Fの証明

<!-- theorem-start:proof -->
**証明（R178F）**

P.7の頂上energy差が理想threshold、P.9が余分な極値の排除、P.10が有限時間境界幅を与える。容量を $\widetilde A_b$ として読み出した実効判定は $|\widetilde A_b-A_b|\leq\ell_{\rm eff}$ を満たす。$A_0+A_1\geq S_->2\ell_{\rm eff}$ なら、有限 $N$ tapeとの合成誤差は

```math
D_{\rm TV}
\leq
\left(
1-\frac{S_--2\ell_{\rm eff}}{2A_{\max}}
\right)^N
+\frac{2\ell_{\rm eff}}{S_--2\ell_{\rm eff}}
+\varepsilon_{\rm tape}
+\varepsilon_{\rm label}
+\varepsilon_{\rm clock}.
```

P.11よりpointerを無履歴で再利用しない。以上で定理を得る。証明終。
<!-- theorem-end:proof -->

## P.13 退役作用区間samplerおよびR170との境界

R178Eは正規化済み確率表または累積確率区間を装置へ入力しない。入力は局所的な非規格化容量 $A_0,A_1$ と、回路非依存のfixed-volume cellである。拒否と無反応を除外しないので、退役した作用区間samplerの事後規格化経路ではない。

M53は二枝apertureを使い、R170の有限混合を同じ段に加えない。R170はQ1、R180Cの2翼局所instrument、一般M50 instrumentの別実装として残る。
