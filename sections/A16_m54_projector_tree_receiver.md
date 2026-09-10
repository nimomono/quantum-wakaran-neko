@number: P
@chapter: 付録
@title: M54段階的射影選別と測定後状態受渡し
@status: R181Dが共通射影作用保持機構、R191の2結果選択・吸収記録、可逆選別機構、必要な方向を変えない振幅再調整、階数1の測定後状態受渡しを段階的に合成し、完全結果誤差と資源境界を証明する。R164/R190/R170の作用殻型経路は代替実現として別に扱う。

## P.1 目的と節点状態

深さ $m$ の二分段階的射影選別を考える。節点 $u\in\{0,1\}^{k-1}$ の入力記憶部を $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

```math
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
```

未処理射影作用を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
=\mathcal J_0Z_u^\dagger Z_u
```

とする。節点の能動状態には信号 $Z_u$、2個の作用保持指針変数、R191のブラウン巨視的スピン、吸収記録 $Y$、選別機構用作業領域、必要なら方向を変えない振幅再調整接続端を含める。R191の混合・decision浴、R179の流出／リセット浴は環境接続部として別に扱い、解析上のBorn確率を制御器へ書き込まない。

R164/R190/R170の正則化作用殻は一般有限結果集合または独立な作用殻型代替実現にだけ用い、本節のR191主線と同じ試行で重複使用しない。

## P.2 R191節点契約と端点dispatcher

結果 $0$ をR191の $+$、結果 $1$ を $-$ に対応させ、

```math
S=J_{u,0}+J_{u,1},
\qquad
D=J_{u,0}-J_{u,1}
```

を作用和・作用差transducerへ渡す。実装値 $\widehat S,\widehat D$ から

```math
\widehat u_*=-\frac{\widehat D}{\widehat S},
\qquad
\widehat p_{u,0}=\frac{1-\widehat u_*}{2},
\qquad
\widehat p_{u,1}=\frac{1+\widehat u_*}{2}
```

を解析上定める。理想重み $p_{u,b}=J_{u,b}/J_\Sigma$ との偏差はR191の

```math
|\widehat u_*-u_*|\leq\varepsilon_u
```

から各成分で高々 $\varepsilon_u/2$ である。

固定閾値 $0<\tau_{\rm cut}\leq1/2$ を取り、$\min_b\widehat p_{u,b}<\tau_{\rm cut}$ なら大きい側を決定論的端点経路へ送り、それ以外はR191の混合--decision--捕獲を走らせる。保護帯、有限温度retreat、有限時間未捕獲はR191の完全結果誤差 $\varepsilon_{191,k}$ に含め、成功結果だけを再規格化しない。

```math
\tau_{\rm state}
:=
\tau_{\rm cut}-\frac{\varepsilon_u}{2}>0
```

を仮定すれば、無反応でない選択結果 $b$ の理想作用重みは

```math
p_{u,b}\geq\tau_{\rm state}
```

である。これは後段の射影選別機構に必要な状態方向Lipschitz下限をR191のdispatcherから直接供給する。

## P.3 R191吸収記録と可逆選別機構

R191が有限decision時間後に $Y=b\in\{0,1\}$ を吸収記録へ固定したときだけ、信号と未使用作業領域上の選別機構

```math
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
```

を開く。直交性から

```math
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I,
```

かつ

```math
F_{u,b}(Z_u,0)
=(P_{u,b}Z_u,P_{u,1-b}Z_u)
```

である。非選択成分を消去せず作業領域へ保持するので、選別機構自体はユニタリな実正準写像である。R191が無反応を返した場合は $F_{u,0},F_{u,1}$ のどちらも作用させない。

## P.4 選別機構誤差と条件付き状態方向

理想選択成分を $v=P_{u,b}Z_u$、実装後を $\widetilde v$ とし、

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|.
```

P.2から無反応でない安全結果では

```math
\|v\|
\geq
\sqrt{\tau_{\rm state}}\,\|Z_u\|.
```

$\eta_F<\sqrt{\tau_{\rm state}}$ なら規格化写像のLipschitz評価により

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{2\eta_F}
{\sqrt{\tau_{\rm state}}-\eta_F}
=:\varepsilon_{\rm proj}.
```

この下限は物理的な状態依存除算ではない。R191の固定dispatcherパラメータとtransducer誤差上界から解析的に得る安全集合境界である。

## P.5 階数1 射影子の測定後状態の受け渡し

階数1節点 $P_{u,b}=|b_u\rangle\langle b_u|$ では、安全結果について

```math
v=P_{u,b}Z_u
=\alpha_b|b_u\rangle,
\qquad
\frac{vv^\dagger}{v^\dagger v}=P_{u,b}.
```

従ってR191が結果を選んだ後、P.3の可逆選別機構そのものが選択後信号を射影子像へ物理的に移す。実装信号の規格化第2モーメント $C_{u,b}^{\rm out}$ は

```math
D_{\rm tr}
\left(
C_{u,b}^{\rm out},P_{u,b}
\right)
\leq
\varepsilon_{\rm proj}
```

を満たす。選択後成分を物理的に単位ノルムへ規格化する必要はなく、同じ未規格化成分を次段へ渡せる。

### P.5.1 階数1 射影子の測定後状態の受け渡し

前項の結論は、結果条件付き統計だけではなく、同一試行の実正準信号に対する物理的経路分解である。結果別固有状態テンプレートを別に準備せず、外部制御器が $\alpha_b$ または $p_{u,b}$ を読み出す必要もない。固定小深度では次段R191が新しい2作用の和と差を直接読むため、中間の振幅再調整を省略できる。

## P.6 方向を変えない振幅再調整

一般深さQ2-4で選択後作用が読出し下限を下回り得る場合だけ、選別機構後の選択後信号へR181Aの $\kappa=0$ 接続端を開く。

```math
\dot Z=g(J_*-Z^\dagger Z)Z.
```

方向 $Z/\|Z\|$ は一定で、作用 $r=Z^\dagger Z$ は

```math
\dot r=2gr(J_*-r)
```

に従う。P.2の下限 $r(0)\geq\tau_{\rm state}r_{\rm in}$ と固定入力作用区間から、目標相対動径誤差 $\eta_R$ に必要な時間を試行前に一様に選べる。固定小深度Q1/Q2-1/Q2-3では作用下限を直接保証できるなら本段を省略してよい。

## P.7 望遠鏡和と完全結果誤差

理想節点核を $K_k$、実装核を $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

```math
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(h_{k-1},\cdot),
K_k(h_{k-1},\cdot)
\right)
\leq\bar\varepsilon_k
```

とする。$\bar\varepsilon_k$ にはR191の完全結果誤差 $\varepsilon_{191,k}$、必要な局所記録誤差、制御付き選別機構誤差、必要な場合の振幅再調整誤差、転送誤差、および前段状態方向誤差からこの節点核へ伝播した偏差を各1回だけ含める。R191主線ではR164/R190/R170代替経路の正則化、混合、固定誤差を重複加算しない。

Markov核の縮約性と望遠鏡和から

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^m\bar\varepsilon_k.
```

理想核の積は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2}{\|Z_0\|^2}
```

と望遠鏡型に縮約する。無反応を同じ完全履歴空間に保持し、成功履歴だけを再規格化しない。

<!-- theorem-start:proof -->
**証明（R181D）**

P.1が射影作用保持、P.2がR191の2結果核と安全作用下限、P.3が結果固定後の1対1な経路分解、P.4--P.5.1が条件付き状態方向誤差、P.6が必要時だけの作用下限回復を与える。各段の完全結果核誤差を一度だけ $\bar\varepsilon_k$ に集約し、Markov核の縮約性と望遠鏡和を適用すれば上式を得る。理想節点では未規格化作用比が連鎖的に相殺され、Lüders型逐次分布に一致する。証明終。
<!-- theorem-end:proof -->

## P.8 資源と反証条件

$m=n$ の一般深さで各節点誤差を $O(\epsilon/n)$ に配分する。R191では

```math
\tau_{\rm cut},g,\varepsilon_u,\varepsilon_{\rm cap}
=O(\epsilon/n),
\qquad
\Delta_{\min}g^2
\gtrsim
\log(n/\epsilon)
```

を十分条件に選べるため、

```math
\Delta_{\min}
=O\!\left(
\frac{n^2}{\epsilon^2}
\log\frac n\epsilon
\right)
```

で足りる。$\tau_{\rm state}=O(\epsilon/n)$ なら状態方向誤差を $O(\epsilon/n)$ にする十分条件として $\eta_F=O((\epsilon/n)^{3/2})$ を取れ、依然として逆多項式精度である。一般深さではP.6の振幅再調整を残す。

R164/R190/R170の作用殻型代替経路を選ぶ場合、その正則化、混合、renewal、固定時間と資源は代替経路だけの台帳へ計上する。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部制御器へ入力する。
2. R191の結果固定前に選別機構を開き、結果成分像を混在させる。
3. 端点dispatcherに状態依存除算または指数精度を要する。
4. 非選択成分または振幅再調整環境を同じ能動状態へ不可逆に消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 深さ $n$ のR191、選別、転送誤差を多項式予算へ同時に収められない。
