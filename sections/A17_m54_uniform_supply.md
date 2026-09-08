@number: Q
@chapter: 付録
@title: M54の一様開放供給・reset・renewal
@status: R179のopen reset、stationary incoming bath、outgoing履歴排出、R190反復時の履歴条件付きrenewalを証明する。旧partial-SWAP blank-bankは有限閉鎖実装の強化結果として本論から退役する。

## Q.1 目的

M54の一般 $n$ 特殊化では、信号記憶部そのものはR181Cの可逆ゲート中に保持する一方、節点ごとの指針変数、選別機構用作業領域、振幅再調整用接続端は反復使用する。現行模型はこれらを有限閉鎖貯蔵部から供給せず、一様な開放リセット interfaceへ接続する。結果相関情報、散逸履歴、使用済み環境自由度は流出経路へ流し、能動系だけを未使用状態へ戻す。

Q1/Q2の静的選択ではR190の2作用LC殻へ定常流入浴部分系を供給する。各試行で過去と相互作用していない流入部分系を使うことで、R190Bの初期shell方向に一様な混合評価を履歴条件付きrenewalへ持ち上げる。

## Q.2 一様開放リセット

補助能動状態の未使用分布を $\mu_{\rm blank}$ とする。リセット半群 $P_t^{\rm reset}$ が安全集合上で

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

で要求精度 $\epsilon$ の未使用状態へ戻せる。結果相関情報を同じ能動自由度へ無履歴で消去することは主張せず、流出浴へ移す。

## Q.3 定常流入 / 流出 reservoir

試行 $m$ の直前の完全過去履歴を $\mathcal H_m$ とする。流入部分系 $B_m^{\rm in}$ は、過去に装置と相互作用していない定常 部分系から取り、

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

を理想規約とする。有限相関または不完全なstationarityを許す場合、その条件付き距離を $\varepsilon_{{\rm in},m}$ とする。使用後の部分系は $B_m^{\rm out}$ として流出経路へ進み、同じ試行列へ再注入しない。

## Q.4 R190 renewal

shellの試行前状態を $x$ とし、R190Bの混合kernelを $K_m(x,\cdot)$ とする。理想一様分布 $U[0,1]$ に対して

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

R190Aの有限記憶誤差を分離する場合は右辺へ $\varepsilon_{{\rm mem},m}$ を1回だけ加える。これがR190Cの反復平方根kernelに必要な履歴条件付きrenewalを与える。

## Q.5 Q2-4の資源境界

開放浴を許しても外部運用資源を無制限にはしない。外部から個別に指定する浴接続端数、coupling family、リセット時間、bandwidth、精度は $\operatorname{poly}(n,d,1/\epsilon)$ で抑える。内部の受動浴自由度、総浴容量、総熱は報告するが、それだけではQ2-4の失敗条件にしない。

浴が回路出力確率、振幅表、$2^n$ 個のモード別係数を外部入力として必要とする場合は失敗である。R186の全自由度に加わる加法ノイズ障害もそのまま残り、開放リセットは計算中の信号 ノイズを自動的に解消しない。

## Q.6 R179の証明と非主張

<!-- theorem-start:proof -->
**証明（R179）**

Q.2の指数収縮からリセット時間上界が従う。Q.3の流入部分系は過去履歴で条件付けても同じ定常法則を持ち、Q.4のkernel評価はshell初期状態に一様なので、条件付き法則の三角不等式からrenewal上界を得る。流出部分系を再利用しないため、結果相関情報を能動系へ戻す必要はない。証明終。
<!-- theorem-end:proof -->

R179は有限閉鎖貯蔵部、部分SWAP列、有限低温／使用済み素子数、無期限運転可能な有限浴を主張しない。これらは有限閉鎖実装そのものを調べる場合の強化問題である。
