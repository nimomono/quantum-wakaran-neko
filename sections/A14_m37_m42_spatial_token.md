@number: N
@chapter: 付録
@title: M37担体上のM42局在トークン
@status: M37の実振動子担体から局所辺流を作り、単一試行の局在粒子トークンを輸送するM42を定義する。R172の等変性、R173の節一様正則化と有限衝突Hamiltonian近似、R174のM51--M37--M42誤差受渡しを証明する。

## N.1 二層模型と単一試行の完全状態

Q3の現行基本模型は、M37担体層とM42粒子層からなる。M37は有限グラフ $G=(V,E)$ の各頂点に置いた実正準対 $(q_i,p_i)$ と局所ばね結合を持つ。M42は同じグラフ上の1個の局在粒子位置

```math
X_t\in V
```

を持つ。M42の粒子位置はM37の振動子座標でも、複素包絡の成分でもない。

1試行の完全状態には、少なくとも次を含める。

```math
\Gamma_t
=
\left(
q(t),p(t),X_t,n_t,s_t,
\{\xi_n,\zeta_n\}_{n=1}^{N_{\rm cell}},
D_t,H_t
\right).
```

$n_t$ は使用中bath cell、$s_t$ は累積hazard、$\xi_n,\zeta_n\in(0,1)$ は開始面で調製した有限bath cellの座標、$D_t$ は固定時刻の位置記録、$H_t$ は使用済みcellと向きの履歴である。複素包絡

```math
b_i(t)
=
e^{i\omega_0t}
\frac{Q_i(t)+iP_i(t)}{\sqrt{2\mathcal J_0}}
```

はM37の実正準状態の派生表示であり、追加の物理場ではない。量子状態に対応させるray、$|c_i|^2$、$C_Z$、粒子位置分布 $P(X_t=i)$ は試行集団の統計記述である。M42のcontrollerが読むのは各試行の局所M37座標、現在位置、局所bath cell、clock、履歴だけであり、$c$、$C_Z$、全粒子位置分布を単一試行へ書き戻さない。

M51の準備後にM42を開始するとき、同じ試行のM37入力信号にM50/R164の作用殻状態数を一度だけ適用し、初期位置 $X_0$ を生成する。この位置がM42の全輸送区間を通して存在する粒子トークンである。終時刻に別のM50位置を再標本化せず、R112の局所記録回路は既存の $X_T$ を読むだけである。

## N.2 M37有効担体の局所辺流

R86の目標有効包絡を、固定有限時間区間で

```math
i\mathcal J_0\dot b_L
=
h_Lb_L,
\qquad
b_L^\dagger b_L=1
```

とする。$h_L=h_L^\dagger$ は $G$ に局所的である。頂点重みと有向辺流を

```math
p_i(t)=|b_{L,i}(t)|^2,
```

```math
J_{i\to j}(t)
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left[
b_{L,j}(t)^*h_{L,ji}b_{L,i}(t)
\right]
```

と定める。Hermitian性と局所性から

```math
J_{i\to j}=-J_{j\to i},
\qquad
\dot p_i
=
\sum_{j:j\sim i}J_{j\to i}
```

が成り立つ。M37の厳密局所包絡 $b$ は反回転項を持つので、この連続方程式をそのまま厳密ミクロ流とは呼ばない。$b$ から計算した局所量はR86の誤差範囲で $b_L$ の流を近似するcontroller入力である。

$p_i(t)>0$ で最小率を

```math
\lambda_{i\to j}(t)
=
\frac{[J_{i\to j}(t)]_+}{p_i(t)},
\qquad
[x]_+=\max\{x,0\}
```

とする。零重み頂点は等変分布の下で占有されない。理想率は連続方程式と局所性だけから一意に強制されるのではなく、余分な対称往復流を加えない最小活動度の採用則である。

### N.2.1 R172の完全形

**R172の仮定と結論。**

有限グラフ、時間連続な有界局所Hermitian生成子、上の最小率を仮定する。$P(X_0=i)=|b_{L,i}(0)|^2$ なら、M42の理想位置過程は全ての有限時刻で

```math
P(X_t=i)=|b_{L,i}(t)|^2
```

を満たす。さらに $h_1=\sup_t\max_i\sum_{j:j\sim i}|h_{L,ij}(t)|$ とすれば、有限時間 $T$ の期待跳躍数は

```math
\mathbb E[N_T]
\leq
\frac{h_1T}{\mathcal J_0}
```

であり、有限時間爆発はない。

<!-- theorem-start:proof -->
**証明（R172）**

位置分布を $\pi_i$ とするとmaster方程式は

```math
\dot\pi_i
=
\sum_j
\left(
\pi_j\lambda_{j\to i}
-
\pi_i\lambda_{i\to j}
\right).
```

$\pi_i=p_i$ を代入すれば、各辺で正部分の差が元の反対称流に戻り、$\dot\pi_i=\sum_jJ_{j\to i}=\dot p_i$ となる。有限状態master方程式の一意性から等変性が従う。また $2\sqrt{p_ip_j}\leq p_i+p_j$ を各辺へ使うと、等変分布下の期待総脱出率は $h_1/\mathcal J_0$ 以下である。時間積分して期待跳躍数上界を得る。証明終。
<!-- theorem-end:proof -->

R172は初期分布を無償で仮定する定理ではない。現行因果鎖ではM51がM37担体のrank-one統計方向を準備し、M50/R164の1回の作用殻選択が初期M42位置を作る。R172はその同じ位置を輸送する。

## N.3 単一試行の明示開放方程式

理想M42は、有限bath tapeで切断したpiecewise deterministic open systemとして各試行を明示できる。現在位置を $i=X_t$ とし、全脱出率と条件付き辺重みを

```math
\Lambda_i(t)=\sum_{j:j\sim i}\lambda_{i\to j}(t),
\qquad
r_{i\to j}(t)=\frac{\lambda_{i\to j}(t)}{\Lambda_i(t)}
```

とする。$\Lambda_i=0$ では待機する。cell $n$ の閾値を $a_n=-\log\xi_n$ とし、跳躍の間は

```math
\dot q_i=\frac{\partial H_{37}}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H_{37}}{\partial q_i},
\qquad
\dot s=\Lambda_{X_t}(t),
\qquad
\dot X_t=0
```

で進める。$s=a_n$ に到達したとき、$\zeta_n$ が累積区間

```math
\sum_{k<j}r_{i\to k}(t)
\leq
\zeta_n
<
\sum_{k\leq j}r_{i\to k}(t)
```

に入る唯一の隣接頂点 $j$ へ $X:i\mapsto j$ と更新し、$(i,j,n,t)$ を $H_t$ へ記録し、$s\mapsto0$、$n\mapsto n+1$ とする。使用可能cellを超えた試行はoverflow無反応へ送る。$\xi_n,\zeta_n$ は時間ごとに外部乱数を注入する値でなく、開始面の有限bath状態である。

この開放表示は単一試行の状態と更新則を明示するが、節の近くで率が大きくなり得る。有限装置には次節の正則化率を使う。

## N.4 節一様正則化と有限Hamiltonian近似

無次元重み正則化 $\rho>0$ と率尺度 $\sigma>0$ を分け、

```math
r_\sigma(x)
=
\frac12
\left(
x+\sqrt{x^2+\sigma^2}
\right),
```

```math
\lambda_{i\to j}^{\rho,\sigma}(b)
=
\frac{r_\sigma(J_{i\to j}(b))}{|b_i|^2+\rho}
```

とする。$\sigma$ は時間の逆数を持ち、$\rho$ と同じ量ではない。最大次数を $d_*$ とすると、固定有限グラフで

```math
\Lambda_*^{\rho,\sigma}
\leq
\frac{h_1}{\mathcal J_0\sqrt\rho}
+
\frac{d_*\sigma}{2\rho}
```

であり、節でも有限である。$H_E=\sup_t\sum_{\{i,j\}\in E}|h_{L,ij}(t)|$ と置く。

### N.4.1 R173の完全形

**R173の仮定と結論。**

正則化M42を理想分布と同じ初期分布から開始する。任意の固定有限時間 $T$ について

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
P(X_t^{\rho,\sigma}\in\cdot),
|b_L(t)|^2
\right)
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right].
```

さらに固定した $\rho,\sigma,T$ について、時間を有限個の窓へ分け、各窓で率を凍結する。辺 $e=\{i,j\}$ と時間窓 $m$ ごとに

```math
\nu_{e,m}
\geq
\max\left\{
\lambda_{i\to j}^{\rho,\sigma},
\lambda_{j\to i}^{\rho,\sigma}
\right\}
```

となる有限試行率を選び、各入射cellに方向タグ $d_n$、物理的な一様閾値座標 $u_n\in(0,1)$、到着clock、共役変数、空の履歴sector、仕事registerを持たせる。$X=i$ から $j$ 向きに到着したcellは

```math
u_n
<
\frac{\lambda_{i\to j}^{\rho,\sigma}}{\nu_{e,m}}
```

なら通過し、それ以外は反射する。逆向きには別の物理閾値 $\lambda_{j\to i}^{\rho,\sigma}/\nu_{e,m}$ を使う。従って縮約通過率は各向きで正確に $\lambda^{\rho,\sigma}$ となる。

通過・反射後にもsource、target、窓、cell番号、未消去の $u_n$ を履歴sectorへ保持し、方向別controllerのエネルギー差を仕事registerへ移す。閾値で分けた各正準phase cellを同じLiouville体積の出射・履歴cellへ並進とshearで写し、未使用sector上まで有限置換として延長すれば、写像は一対一かつ正準にできる。閾値を有限有理分割で近似し、境界を滑らかなHamiltonian shearで置換すると、固定有限個のcellについて駆動Hamiltonian散乱列が得られる。cell overflow、閾値分割、境界平滑化、時間凍結、clock、仕事register切断の失敗は無反応へ残す。

これはR162と同じ有限衝突・履歴保存の設計様式を使うが、R162の詳細釣合い率を代入する構成ではない。一般のM42率は辺ごとの正逆率比が平衡ポテンシャル差から決まらないので、方向別controllerと仕事registerを持つ駆動衝突模型である。

<!-- theorem-start:proof -->
**証明（R173）**

$0\leq r_\sigma(x)-[x]_+\leq\sigma/2$ と $|J_{i\to j}|\leq2|h_{ij}|\sqrt{p_ip_j}/\mathcal J_0$ を使うと、理想辺流と正則化辺流の差は

```math
\left|
\frac{p_i}{p_i+\rho}r_\sigma(J_{i\to j})
-[J_{i\to j}]_+
\right|
\leq
\frac\sigma2
+
\frac{|h_{ij}|}{\mathcal J_0}\sqrt\rho
```

である。全辺を足し、Markov半群の全変動縮小性とDuhamel公式を使えば表示上界を得る。固定正則化では率が有界かつ滑らかなので、有限窓の凍結生成子列が時間順序指数へ収束する。各凍結率に上の方向別通過確率を持つ有限cellを置けば縮約率が一致する。履歴を消去しない正準phase-cell置換、有限分割、Hamiltonian平滑化の誤差を有限個の窓で加えれば、駆動Hamiltonian衝突列による任意精度の近似を得る。証明終。
<!-- theorem-end:proof -->

有限 $\rho,\sigma$ では小さな逆向き流が残る。$\rho,\sigma\downarrow0$ では必要最大率、衝突cell数、障壁精度が発散し得るため、1つの固定装置が厳密nodeを再現するとは主張しない。

## N.5 M37担体誤差からM42への受渡し

有限装置のcontrollerは理想 $b_L$ でなくM37局所包絡 $b$ を読む。安全領域

```math
\|b(t)\|\geq a_{\rm tok}>0,
\qquad
\|b(t)\|,\|b_L(t)\|\leq R_{\rm tok}
```

を固定する。正の $\rho,\sigma$ の下では、正則化生成子 $L^{\rho,\sigma}(b)$ はこのコンパクト安全領域でLipschitzであり、ある有限定数 $K_{\rho,\sigma,a,R}$ に対して

```math
\left\|
L^{\rho,\sigma}(b)
-L^{\rho,\sigma}(b_L)
\right\|_{\rm row}
\leq
K_{\rho,\sigma,a,R}
\|b-b_L\|
```

となる。ここで $\|A\|_{\rm row}=\max_i\sum_j|A_{ij}|$ は行確率ベクトルに作用する生成子の行和normである。R86の包絡誤差を使えば、担体からtoken分布への誤差を

```math
\varepsilon_{37\to42}(T)
\leq
\frac12
TK_{\rho,\sigma,a,R}
\varepsilon_{\rm car}(T)
\sup_\omega\|\widetilde b(0;\omega)\|
```

で抑えられる。安全領域外は無反応へ残し、成功試行だけを再規格化しない。

### N.5.1 R174の完全形

**R174の仮定と結論。**

固定有限グラフと固定時間 $T$ を取る。M51/R171でM37のrank-one初期担体集団を準備し、同じ試行の初期信号にM50/R164の作用殻選択を一度だけ適用して $X_0$ を作り、M37と正則化M42を同時に進め、終時刻に既存の $X_T$ をR112で局所記録する。完全結果集合に無反応を含めると、終位置の理想Born型分布との差は

```math
\begin{aligned}
\varepsilon_{174}(T)
\leq{}&
\varepsilon_{\rm prep}
+\varepsilon_{\rm init}
+T
\left[
|E|\sigma
+\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]\\
&+\varepsilon_{37\to42}
+\varepsilon_{\rm step}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm over}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm rec}.
\end{aligned}
```

ここで $\varepsilon_{\rm prep}$ はM51のray準備とseed無反応、$\varepsilon_{\rm init}$ は初期作用殻選択、$\varepsilon_{\rm step}$ は時間凍結、$\varepsilon_{\rm coll}$ は方向別閾値分割、Hamiltonian平滑化、仕事register切断を含む有限衝突近似、$\varepsilon_{\rm over}$ はbath cell不足、$\varepsilon_{\rm clk}$ は時計、$\varepsilon_{\rm rec}$ は局所記録である。同じM37包絡偏差を $\varepsilon_{\rm prep}$、$\varepsilon_{37\to42}$、$\varepsilon_{\rm rec}$ へ重複加算しない。

<!-- theorem-start:proof -->
**証明（R174）**

R171の準備切断面からM37初期面への誤差、R164による1回の初期位置分布、R172の理想等変性、R173の正則化誤差、M37--M42生成子のDuhamel誤差、有限衝突列と記録の縮約誤差を因果順に三角不等式で加える。無反応質量を完全結果分布の成分として保つため、事後規格化項は生じない。証明終。
<!-- theorem-end:proof -->

M51の二乗統計と初期M42位置は独立な2つのBorn型確率源ではない。M51は担体集団のrank-one方向を準備し、R164はその単一試行信号から1個の初期粒子位置を物理化し、R172は同じ粒子を輸送する。終時刻には再抽選せず、位置記録だけを行う。

## N.6 R123--R125への下流接続

R123の束縛スペクトルと有限環境純位相緩和は、M37有効生成子とその縮約統計に関する結果として維持する。M42を追加しても、固有状態選択、冷却、不可逆緩和は従わない。

R124では3頂点障壁の初期信号から $X_0$ を一度準備し、M42を $T_{\rm bar}$ まで輸送して反対側位置を読む。R125では2経路入力ごとに同じ初期選択・輸送・記録protocolを使う。各比較のM42読出し誤差が $\varepsilon_{174}$ 以下なら、観測される障壁反対側増分と干渉分布距離はそれぞれ

```math
\alpha-2\varepsilon_{174},
\qquad
\Delta-2\varepsilon_{174}
```

以上である。M51、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所装置へ統合していないため、Q3-4とQ3-5の条件付き達成判定は変えない。

## N.7 Q3-1への非遡及

Q3-1の固定基準は、局所位置結合振動子網から空間格子上のSchrödinger型時間発展を誤差付きで導くことであり、R86が満たす。M42は、粒子を実体として持つために追加する下流強化である。R172--R174をQ3-1達成の根拠へ遡及的に加えず、M42の正則化極限が失敗してもR86の包絡縮約定理自体は失われない。

## N.8 旧M42との差と非主張

旧M42の退役結果群は、任意に与えた物理的複素振幅場と位置過程を直接結び、Q1--Q3へ広く使う模型だった。現行M42はQ3だけに限定し、複素包絡をM37実正準状態の派生表示、rayを集団統計とする。初期二乗分布はM51準備と1回のR164選択に由来し、終時刻M50再標本化と併用しない。旧結果IDは再利用しない。

現行M42/R172--R174は次を主張しない。

1. 最小率がM37のHamiltonianだけから一意に強制されること。
2. M51、M37、作用殻、M42 bath、記録器の単一閉鎖Hamiltonian統合。
3. 1つの固定有限装置で $\rho=\sigma=0$ の厳密nodeを追跡すること。
4. 連続空間の連続粒子軌道、慣性質量、電荷、担体エネルギーの粒子への帰属。
5. 初回到達、吸収、散乱透過率、幾何学的2開口、連続運転スクリーン。
6. 多粒子、交換統計、一般複素hopping、外部磁場。
7. 独立同分布型の有限標本揺らぎ。

M42の採用により、Q3では「粒子が実在せず、終時刻にだけ位置が作られる」という読みに依存しない。一方、採用した局所率と有限衝突bathの物理的選択理由、全周期収支、連続極限は未完成課題として残る。
