@number: Q
@chapter: 付録
@title: M54の一様開放供給・reset・renewal
@status: R179のopen reset、stationary incoming bath、outgoing履歴排出、R190反復時の履歴条件付きrenewalを証明する。旧partial-SWAP blank-bankは有限閉鎖実装の強化結果として本論から退役する。

## Q.1 目的

M54の一般 $n$ 特殊化では、信号記憶部そのものはR181Cの可逆ゲート中に保持する一方、節点ごとのpointer、選別機構用workspace、振幅再調整用接続端は反復使用する。現行模型はこれらを有限closed bankから供給せず、一様なopen reset interfaceへ接続する。結果相関情報、散逸履歴、使用済み環境自由度はoutgoing channelへ流し、能動系だけを未使用状態へ戻す。

Q1/Q2の静的選択ではR190の2作用LC殻へstationary incoming bath sectorを供給する。各attemptで過去と相互作用していないincoming sectorを使うことで、R190Bの初期shell方向に一様な混合評価を履歴条件付きrenewalへ持ち上げる。

## Q.2 一様open reset

補助能動状態の未使用分布を $\mu_{\rm blank}$ とする。reset半群 $P_t^{\rm reset}$ が安全集合上で

```math
D
\left(
\mu P_t^{\rm reset},
\mu_{\rm blank}
\right)
\leq
C_{\rm reset}e^{-\gamma_{\rm reset}t}
```

を満たすとする。従って

```math
T_{\rm reset}
\geq
\frac1{\gamma_{\rm reset}}
\log\frac{C_{\rm reset}}{\epsilon}
```

で要求精度 $\epsilon$ の未使用状態へ戻せる。結果相関情報を同じ能動自由度へ無履歴で消去することは主張せず、outgoing bathへ移す。

## Q.3 stationary incoming / outgoing reservoir

attempt $m$ の直前の完全過去履歴を $\mathcal H_m$ とする。incoming sector $B_m^{\rm in}$ は、過去に装置と相互作用していないstationary sectorから取り、

```math
\mathcal L
\left(
B_m^{\rm in}
\mid
\mathcal H_m
\right)
=
\mu_{\rm in}
```

を理想規約とする。有限相関または不完全なstationarityを許す場合、その条件付き距離を $\varepsilon_{{\rm in},m}$ とする。使用後のsectorは $B_m^{\rm out}$ としてoutgoing channelへ進み、同じattempt列へ再注入しない。

## Q.4 R190 renewal

shellのattempt前状態を $x$ とし、R190Bの混合kernelを $K_m(x,\cdot)$ とする。理想一様分布 $U[0,1]$ に対して

```math
\sup_x
D
\left(
K_m(x,\cdot),
U[0,1]
\right)
\leq
\varepsilon_{{\rm mix},m}
```

なら、任意の過去履歴に条件付けて

```math
D
\left(
\mathcal L(X_m\mid\mathcal H_m),
U[0,1]
\right)
\leq
\varepsilon_{{\rm in},m}
+
\varepsilon_{{\rm mix},m}.
```

R190Aの有限memory誤差を分離する場合は右辺へ $\varepsilon_{{\rm mem},m}$ を1回だけ加える。これがR190Cの反復平方根kernelに必要な履歴条件付きrenewalを与える。

## Q.5 Q2-4の資源境界

open bathを許しても外部運用資源を無制限にはしない。外部から個別に指定するbath port数、coupling family、reset時間、bandwidth、精度は $\operatorname{poly}(n,d,1/\epsilon)$ で抑える。内部の受動bath自由度、総bath容量、総熱は報告するが、それだけではQ2-4の失敗条件にしない。

浴が回路出力確率、振幅表、$2^n$ 個のmode別係数を外部入力として必要とする場合は失敗である。R186の全自由度に加わる加法noise障害もそのまま残り、open resetは計算中のsignal noiseを自動的に解消しない。

## Q.6 R179の証明と非主張

<!-- theorem-start:proof -->
**証明（R179）**

Q.2の指数収縮からreset時間上界が従う。Q.3のincoming sectorは過去履歴で条件付けても同じstationary法則を持ち、Q.4のkernel評価はshell初期状態に一様なので、条件付き法則の三角不等式からrenewal上界を得る。outgoing sectorを再利用しないため、結果相関情報を能動系へ戻す必要はない。証明終。
<!-- theorem-end:proof -->

R179は有限closed bank、partial-SWAP列、有限cold/spent cell数、無期限運転可能な有限bathを主張しない。これらは有限閉鎖実装そのものを調べる場合の強化問題である。
