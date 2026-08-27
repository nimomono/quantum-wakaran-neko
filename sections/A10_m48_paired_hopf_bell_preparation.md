@number: J
@chapter: 付録
@title: M48設定依存paired-Hopf Bell準備
@status: 設定前共通基準測度から2翼bath対を準備する開放古典模型を定義し、R146--R150の否定的結果、吸引率、singlet交差共分散、抽象matching下の余弦則、有限誤差Bell監査を示す。完全周期は第5章と付録DのR151--R156で閉じる。

## J.1 目的、模型階層、主張範囲

本付録は、有限設定族について、設定前の共通基準測度から設定依存の2翼bath対を前向きに準備するM48を定義する。M48はM47を2翼へ拡張した**決定論的な開放古典有効模型**である。有限閉鎖Hamiltonian系への持ち上げは与えず、採用した開放方程式後の厳密計算と、その方程式自体のミクロ導出を区別する。

有限なA設定族とB設定族を

```math
\mathcal X
=
\{x_1,\ldots,x_M\},
\qquad
\mathcal Y
=
\{y_1,\ldots,y_N\}
```

とする。M48では設定生成後のA設定 $x$ が中央準備流へ入る。B設定 $y$ は中央結合の切断後にB局所分析器へだけ入る。従って、測定開始面の完全状態分布は一般に $x$ に依存するが、切断後の局所応答へ反対翼の設定を入れない。

本付録が厳密に示す範囲は次である。

1. 積bath標本の直接4次元共分散をsinglet階数1射影にできないという否定的結果R146。
2. M48の採用開放方程式に対する2枝paired-Hopf吸引多様体と有限時間収束率R147。
3. 1つの設定前基準測度から、全ての有限A設定について同じsinglet型交差共分散射影を準備するR148。
4. 2翼の完全なM47 matchingと局所instrumentを仮定した後の余弦共同分布R149。
5. 無反応を捨てない有限誤差、非信号性、CHSH値、Bell前提監査R150。

R146--R148が単独で厳密に吸引するのは2翼bath方向である。実現配置 $X_A,X_B$ の周辺、条件付きbath分布、切断後局所分析、記録、周期末resetは、第5章と付録Dの別の開放配置流・装置定理R151--R156がM48単独周期として閉じる。付録Jだけの結果を単一試行Bell周期またはQ2-1からの物理的受渡しと同一視しない。

## J.2 R146：積bath標本の直接共分散に対する否定的結果

各試行の2翼bathベクトルを $z_A,z_B\in\mathbb C^2$ とする。直接テンソル標本

```math
Z
=
z_A\otimes z_B
\in
\mathbb C^4
```

の規格化共分散を

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}
{\mathbb E[Z^\dagger Z]}
```

とする。既存M39の係数順序に合わせ、singlet代表を

```math
c_{\rm s}
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

と置く。

<!-- theorem-start:theorem -->
**定理（R146：積bath標本からの直接singlet階数1共分散の不可能性）**

$0<\mathbb E[Z^\dagger Z]<\infty$ とする。全ての標本が $Z=z_A\otimes z_B$ という積形なら、

```math
C_Z
=
c_{\rm s}c_{\rm s}^\dagger
```

とはならない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

等式が成り立つと仮定し、$P_\perp=I_4-c_{\rm s}c_{\rm s}^\dagger$ とする。このとき

```math
0
=
\operatorname{tr}
\left(
P_\perp C_Z
\right)
=
\frac{
\mathbb E
\left[
\left\|P_\perp Z\right\|^2
\right]
}{
\mathbb E[Z^\dagger Z]
}
```

なので、$Z$ はほとんど確実に $c_{\rm s}$ の1次元部分空間へ属する。一方、非零の積ベクトル $z_A\otimes z_B$ を $2\times2$ 係数行列へ戻すと階数1である。$c_{\rm s}$ の係数行列は

```math
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

で階数2なので、非零の積ベクトルはsinglet直線へ属さない。これは $\mathbb E[Z^\dagger Z]>0$ と矛盾する。証明終。
<!-- theorem-end:proof -->

従ってM48では、$z_A\otimes z_B$ の標本共分散をsingletへ直接吸引する構成を採らない。2翼bath間の交差共分散を先に作り、その規格化ベクトルが定める階数1射影をsinglet型統計状態とする。

## J.3 交差共分散と階数1射影

反対称行列を

```math
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathsf E^{\mathsf T}
=
-\mathsf E,
\qquad
\mathsf E^2
=
-I_2
```

とする。有限時間の安全事象を $G_x$ とし、無規格化交差共分散を

```math
M_{AB}^{G}
=
\mathbb E
\left[
\mathbf1_{G_x}
z_Az_B^{\mathsf T}
\right]
```

と定める。$M_{AB}^{G}\neq0$ のとき

```math
B_{AB}
=
\frac{M_{AB}^{G}}
{\left\|M_{AB}^{G}\right\|_{\rm F}}
```

とする。付録Kとの共通規約として行優先ベクトル化を

```math
\operatorname{vec}_{\rm row}
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
a&b&c&d
\end{pmatrix}^{\mathsf T}
```

と定め、

```math
\beta_{AB}
=
\operatorname{vec}_{\rm row}(B_{AB}),
\qquad
C_{AB}^{\times}
=
\beta_{AB}\beta_{AB}^\dagger
```

をM48の**交差共分散射影**と呼ぶ。階数1なのは $C_{AB}^{\times}$ であり、$2\times2$ 行列 $B_{AB}$ 自体ではない。また、$C_{AB}^{\times}$ はR146で退けた直接標本共分散 $C_Z$ ではない。

列優先記法との関係は、中央2成分を交換する $P_{23}$ により

```math
\operatorname{vec}_{\rm col}
\left(B\right)
=P_{23}\operatorname{vec}_{\rm row}\left(B\right)
```

である。M48で得る代表が $B_{AB}=-\mathsf E/\sqrt2$ なら

```math
\operatorname{vec}_{\rm row}
\left(
-\frac{\mathsf E}{\sqrt2}
\right)
=
-c_{\rm s}.
```

従ってM39の行優先singlet代表とはglobal phase $-1$ だけ異なり、同じ階数1射影

```math
C_{AB}^{\times}
=
c_{\rm s}c_{\rm s}^\dagger
```

を与える。singletでは $P_{23}$ がglobal signに退化するが、一般行列では退化しないため、row-majorとcolumn-majorを暗黙に交換しない。

## J.4 設定前共通基準測度と試行の順序

設定前開始面の状態を

```math
\Gamma_0
=
\left(
\xi_A,\xi_B,
m_0,d_0,
X_A,X_B,
\zeta,R
\right)
```

とする。$\xi_A,\xi_B$ は設定生成角、$m_0,d_0\in\mathbb C^2$ は中央paired-Hopf portの初期bright変数とdark変数、$X_A,X_B$ は2翼の実現配置、$\zeta$ はpump、時計、切断器、浴、履歴の補助変数、$R$ は空の外部記録である。基準測度を

```math
\nu_0(d\Gamma_0)
=
\frac{d\xi_A\,d\xi_B}{(2\pi)^2}
\otimes
\overline\nu_0(d\overline\Gamma_0),
```

```math
\overline\Gamma_0
=
\left(
m_0,d_0,X_A,X_B,\zeta,R
\right),
```

```math
\overline\nu_0(d\overline\Gamma_0)
=
\nu_m(dm_0)
\otimes
\nu_d(dd_0)
\otimes
\nu_{X\zeta R}
```

とする。有限設定を作る窓写像を $S_A(\xi_A)\in\mathcal X$、$S_B(\xi_B)\in\mathcal Y$ とする。積構造により、任意の非零設定窓について

```math
\nu_0
\left(
d\overline\Gamma_0
\mid
S_A(\xi_A)=x,
S_B(\xi_B)=y
\right)
=
\overline\nu_0(d\overline\Gamma_0).
```

従って設定前の物理seed測度 $\overline\nu_0$ は、実際に生成される設定値 $x,y$ に依存しない。

$m_0=r_0q_0$ と分け、方向 $q_0$ は $\mathbb C^2$ の単位球面上で共通位相を除いてHaar分布、動径とdark変数は

```math
0<r_-
\leq
r_0
\leq
r_+<\infty,
\qquad
\|d_0\|
\leq
d_+<\infty
```

を満たすとする。設定窓が $\xi_A,\xi_B$ から $x\in\mathcal X$、$y\in\mathcal Y$ を作った後、A設定 $x$ に対応する流を $\Phi_x^\tau$ と書く。明示的な設定レジスターを除いた準備状態を $\Lambda$ とし、その測度を

```math
\mu_x^\tau
=
\left(
\Phi_x^\tau
\right)_\#\overline\nu_0
```

と定める。測定開始面では

```math
\mu_{\rm meas}
\left(
d\Lambda
\mid
x,y
\right)
=
\mu_x^{\tau_{\rm p}}(d\Lambda)
```

となり、一般に $\mu_x^{\tau_{\rm p}}\neq\mu_{x'}^{\tau_{\rm p}}$ である。目的分布を設定依存初期測度へ直接書いたのではなく、同じ物理seed測度 $\overline\nu_0$ を設定生成後の明示流で押し出している。一方、B設定 $y$ はこの中央準備流へ入らない。

## J.5 bright変数とdark変数

中央portの2翼bath変数を $z_A,z_B\in\mathbb C^2$ とし、

```math
m
=
\frac{z_A-\mathsf E\overline{z_B}}{2},
\qquad
d
=
\frac{z_A+\mathsf E\overline{z_B}}{2}
```

と定める。逆変換は

```math
z_A
=
m+d,
\qquad
z_B
=
\mathsf E\overline{m-d}
```

である。$d=0$ なら2翼は位相共役した反対称対

```math
z_B
=
\mathsf E\overline{z_A}
```

になる。M48は設定方向へ $m$ を吸引し、$d$ を減衰させることでpaired fiberを準備する。

## J.6 M48のpaired-Hopf開放方程式

各設定 $x$ に単位Blochベクトル $n_x\in\mathbb R^3$ を対応させ、Pauli行列を $\boldsymbol\sigma$ と書く。設定作用素と方向変数を

```math
\Sigma_x
=
n_x\cdot\boldsymbol\sigma,
\qquad
\Sigma_x^2
=
I_2,
```

```math
h_x(m)
=
\frac{m^\dagger\Sigma_xm}{m^\dagger m}
```

とする。準備の有効時間を

```math
\tau(t)
=
\int_{t_{\rm in}}^t
\lambda_{\rm prep}(s)\,\mathrm{d}s
```

と定める。$m\neq0$ に対する決定論的開放流を

```math
\frac{dm}{d\tau}
=
F_x(m)
=
g(1-m^\dagger m)m
+
\kappa h_x(m)
\left(
\Sigma_x-h_x(m)I_2
\right)m,
```

```math
\frac{dd}{d\tau}
=
-\kappa_{\rm p}d
```

とする。$g,\kappa,\kappa_{\rm p}>0$ である。元の2翼変数では

```math
\dot z_A
=
\lambda_{\rm prep}(t)
\left[
F_x(m)-\kappa_{\rm p}d
\right],
```

```math
\dot z_B
=
\lambda_{\rm prep}(t)
\mathsf E
\overline{
F_x(m)+\kappa_{\rm p}d
}
```

である。$\lambda_{\rm prep}>0$ の準備窓が終わると中央portを切断する。以後は各翼のM47分析器、傾斜固定、局所記録だけを作動させる。

各項の物理的役割は次の通りである。

| 項 | 役割 | 外部収支 |
|---|---|---|
| $g(1-m^\dagger m)m$ | bright動径への能動供給と飽和 | pumpから作用を供給し、単位動径を越えるとlimiterへ戻す |
| $\kappa h_x(\Sigma_x-h_xI_2)m$ | 設定依存の異方的整列 | $m$ のノルムを変えず、設定controllerから方向情報を受け取る |
| $-\kappa_{\rm p}d$ | paired fiber外のdark成分の散逸 | dark作用をsinkへ排出する |
| $\lambda_{\rm prep}$ | 準備portの接続と切断 | 切替仕事、残留相関、時計情報を外部帳簿へ渡す |

局所的な作用様量

```math
N_{\rm pair}
=
m^\dagger m+d^\dagger d
```

は

```math
\frac{dN_{\rm pair}}{d\tau}
=
2g(1-m^\dagger m)m^\dagger m
-
2\kappa_{\rm p}d^\dagger d
```

を満たす。異方的整列項は $N_{\rm pair}$ を直接変えないが、設定controllerとの仕事と情報流を零と意味しない。位相体積の収縮とdark散逸に伴うエントロピーは外部sinkへ出る。M48はこの局所帳簿を明示するが、pump、controller、sink、切断器まで含む総エネルギー・総エントロピー収支を閉じていない。

開放模型としての8項目監査を次にまとめる。

| 監査項目 | M48で明示する内容と限界 |
|---|---|
| 状態、方程式、初期条件 | 状態は $(m,d)$、発展はJ.6節の2式、seedは $r_-\leq\|m_0\|\leq r_+$、$\|d_0\|\leq d_+$、有限時間一様評価では $|h_x(m_0)|\geq h_*$ とする |
| 雑音規約 | 確率微分項は零であり、Itô規約、Stratonovich規約、白色雑音極限を使わない。雑音付き定常測度へ読み替えない |
| drift、散逸、駆動 | bright pumpと飽和、設定依存整列、dark sink、外部 $\lambda_{\rm prep}$ による接続と切断を上の表の通り分離する |
| 熱、仕事、エントロピー、情報 | $N_{\rm pair}$ の局所流だけを計算する。bath温度と熱流 $\dot Q$ は定義せず、pump仕事、controller仕事、切替仕事、sinkのエントロピー生成、設定情報流の総収支は未閉鎖とする |
| 環境消去と時間尺度 | pump、controller、sink、切断器を外部portとして採用し、環境自由度の消去、Markov近似、時間尺度分離は導出しない。$\tau$ は有限準備窓の有効時間である |
| 測度、準備、試行 | J.4節の $\nu_0$ と共通物理seed周辺 $\overline\nu_0$、設定窓、押出し測度 $\mu_x^\tau$、J.12節の無反応を含む完全結果集合で試行を数える |
| 検証 | R147--R150の解析恒等式と有限誤差式を示し、`tools/verify_m48_paired_hopf.py` でbright/dark変換、吸引率、交差共分散、余弦則、CHSH誤差を回帰検算する |
| 各項の由来 | 全drift項は現象論的な採用開放方程式である。具体的な回路、流体、振動子浴、有限閉鎖Hamiltonian系から導出した項はない |

この改訂では白色雑音を加えない。雑音を加えると $h_x=0$ の盆境界を横切る枝遷移と定常測度を別に解析する必要がある。決定論的主定理を雑音付き定理へ読み替えない。

## J.7 R147：吸引多様体と有限時間収束率

$\Sigma_xu_{s,x}=s u_{s,x}$、$s\in\{+1,-1\}$ となる規格化固有ベクトルを選ぶ。M48の吸引集合を

```math
\mathcal A_x
=
\bigcup_{s=\pm1}
\left\{
\left(
e^{i\alpha}u_{s,x},
e^{-i\alpha}\mathsf E\overline{u_{s,x}}
\right):
\alpha\in[0,2\pi)
\right\}
```

とする。

<!-- theorem-start:theorem -->
**定理（R147：M48の2枝paired-Hopf吸引多様体と有限時間率）**

$m_0\neq0$、$h_0=h_x(m_0)\neq0$ とし、$s=\operatorname{sign}h_0$ とする。このときM48流は $\mathcal A_x$ の $s$ 枝へ収束する。具体的に

```math
\|m(\tau)\|^2
=
\frac{1}
{1+
\left(
\|m_0\|^{-2}-1
\right)e^{-2g\tau}},
```

```math
h_x(m(\tau))^2
=
\frac{1}
{1+
\left(
h_0^{-2}-1
\right)e^{-4\kappa\tau}},
```

```math
d(\tau)
=
e^{-\kappa_{\rm p}\tau}d_0
```

である。射影間のtrace距離を

```math
D_{\rm tr}(P,Q)
=
\frac12\|P-Q\|_1
```

とする。$|h_0|\geq h_*>0$ なら

```math
D_{\rm tr}
\left(
\frac{m(\tau)m(\tau)^\dagger}
{m(\tau)^\dagger m(\tau)},
u_{s,x}u_{s,x}^\dagger
\right)
\leq
\frac{e^{-2\kappa\tau}}
{\sqrt2h_*}.
```

さらに $r_-\leq\|m_0\|\leq r_+$、$\|d_0\|\leq d_+$ の有界seed集合で

```math
C_r
=
\max
\left\{
r_-^{-2}-1,
r_+^2-1,
0
\right\},
\qquad
\overline r
=
\max\{1,r_+\},
```

```math
K_{48}
=
\sqrt2
\left(
C_r
+
\frac{\overline r}{h_*}
+
d_+
\right)
```

と置けば

$\operatorname{dist}$ を $\mathbb C^2\times\mathbb C^2$ の標準積ノルムが定める距離として

```math
\operatorname{dist}
\left(
(z_A(\tau),z_B(\tau)),
\mathcal A_x
\right)
\leq
K_{48}
e^{-\gamma_{48}\tau},
```

```math
\gamma_{48}
=
\min
\left\{
2g,2\kappa,\kappa_{\rm p}
\right\}
```

を得る。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$r^2=m^\dagger m$ とする。$m^\dagger(\Sigma_x-h_xI_2)m=0$ なので

```math
\frac{dr^2}{d\tau}
=
2g(1-r^2)r^2.
```

これを解くと第1式を得る。$\Sigma_x^2=I_2$ を使うと

```math
\frac{dh_x}{d\tau}
=
2\kappa h_x
\left(
1-h_x^2
\right).
```

従って $h_x$ の符号は保存され、$h_x^2$ の方程式を解けば第2式を得る。$d$ の式は線形なので第3式が従う。

$P_m=mm^\dagger/(m^\dagger m)$ とする。2次元純粋射影のtrace距離は

```math
D_{\rm tr}(P_m,P_{s,x})
=
\sqrt{
\frac{1-|h_x|}{2}
}
\leq
\sqrt{
\frac{1-h_x^2}{2}
}.
```

$|h_0|\geq h_*$ と第2式から射影上界を得る。位相 $\alpha$ を最適に選ぶと、規格化brightベクトルの固有ベクトルからの距離は $\sqrt2D_{\rm tr}$ 以下である。また、動径の厳密解から

```math
\left|
\|m(\tau)\|-1
\right|
\leq
C_re^{-2g\tau}
```

であり、$\|m(\tau)\|\leq\overline r$ である。従って

```math
\min_\alpha
\left\|
m(\tau)-e^{i\alpha}u_{s,x}
\right\|
\leq
C_re^{-2g\tau}
+
\frac{\overline r}{h_*}e^{-2\kappa\tau}.
```

bright/dark逆変換に対して標準積ノルムを使うと、その距離の2乗はbright誤差とdark誤差の2倍の和である。$\|d(\tau)\|\leq d_+e^{-\kappa_{\rm p}\tau}$ を合わせれば、表示した $K_{48}$ と $\gamma_{48}$ が従う。証明終。
<!-- theorem-end:proof -->

$h_x=0$ は不変な盆境界であり、そこでは異方的整列項が零になる。この集合はHaar方向測度では零測度だが、有限時間の一様収束定数は $h_0\to0$ で発散する。従って有限時間装置では

```math
G_x
=
\left\{
|h_x(m_0)|\geq h_*
\right\}
```

を安全事象とし、補集合を無反応として記録する。Haar方向では $h_x$ は $[-1,1]$ 上の一様分布なので

```math
P(G_x^c)
=
h_*,
```

```math
P(h_x\geq h_*)
=
P(h_x\leq-h_*)
=
\frac{1-h_*}{2}.
```

無反応試行を除いて分母を付け替えない。

## J.8 交差共分散の有限時間上界

$P_{s,x}=u_{s,x}u_{s,x}^\dagger$ とする。bright/dark逆変換から各安全標本について

```math
z_Az_B^{\mathsf T}
=
-(m+d)(m^\dagger-d^\dagger)\mathsf E
```

である。従って

```math
\left\|
z_Az_B^{\mathsf T}
+
P_{s,x}\mathsf E
\right\|_{\rm F}
\leq
\left\|
mm^\dagger-P_{s,x}
\right\|_{\rm F}
+
2\|m\|\|d\|
+
\|d\|^2.
```

R147で定めた $C_r$、$\overline r$ を使うと

```math
\left\|
z_Az_B^{\mathsf T}
+
P_{s,x}\mathsf E
\right\|_{\rm F}
\leq
K_\times e^{-\gamma_{48}\tau},
```

```math
K_\times
=
C_r
+
h_*^{-1}
+
2\overline r d_+
+
d_+^2
```

を選べる。これは設定族の要素数に依存しない。依存するのは有限設定族で共通に選んだseed境界、盆余裕、3つの減衰率だけである。

## J.9 R148：共通基準測度からのsinglet交差共分散

吸引集合上の安全標本は

```math
z_A
=
e^{i\alpha}u_{s,x},
\qquad
z_B
=
e^{-i\alpha}
\mathsf E\overline{u_{s,x}}
```

となる。位相は積 $z_Az_B^{\mathsf T}$ で相殺する。また

```math
z_Az_B^{\mathsf T}
=
-P_{s,x}\mathsf E.
```

<!-- theorem-start:theorem -->
**定理（R148：設定前共通基準測度からのsinglet交差共分散準備）**

J.4節の設定前基準測度を取り、$q_0$ をHaar方向、有限設定族を $\mathcal X$ とする。各 $x\in\mathcal X$ について同じ物理seed周辺 $\overline\nu_0$ をM48流で押し出すと、安全2枝は等重みでR147の吸引集合へ収束し、

```math
M_{AB}^{G}(\infty\mid x)
=
-\frac{1-h_*}{2}\mathsf E
```

を満たす。従って

```math
B_{AB}(\infty\mid x)
=
-\frac{\mathsf E}{\sqrt2},
\qquad
C_{AB}^{\times}(\infty\mid x)
=
c_{\rm s}c_{\rm s}^\dagger
```

であり、右辺は $x$ に依存しない。

有限時間で交差共分散のずれを

```math
\delta_\times(\tau)
=
\left\|
M_{AB}^{G}(\tau\mid x)
+
\frac{1-h_*}{2}\mathsf E
\right\|_{\rm F}
```

とする。枝重みの非対称、切断残差を $\varepsilon_{\rm sym}$、$\varepsilon_{\rm cut}$ とすれば

```math
\delta_\times(\tau)
\leq
(1-h_*)K_\times e^{-\gamma_{48}\tau}
+
\varepsilon_{\rm sym}
+
\varepsilon_{\rm cut}.
```

$\delta_\times<(1-h_*)/(2\sqrt2)$ なら

```math
\left\|
B_{AB}(\tau\mid x)
+
\frac{\mathsf E}{\sqrt2}
\right\|_{\rm F}
\leq
\frac{2\sqrt2}{1-h_*}
\delta_\times(\tau).
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

Haar方向では安全な正負2枝の質量がそれぞれ $(1-h_*)/2$ である。$P_{+,x}+P_{-,x}=I_2$ なので

```math
M_{AB}^{G}(\infty\mid x)
=
-\frac{1-h_*}{2}
\left(
P_{+,x}+P_{-,x}
\right)\mathsf E
=
-\frac{1-h_*}{2}\mathsf E.
```

J.8節の標本ごとの上界を安全集合で平均すると有限時間式を得る。非零行列の規格化写像 $M\mapsto M/\|M\|_{\rm F}$ の局所Lipschitz上界を使えば最後の式が従う。証明終。
<!-- theorem-end:proof -->

R148が示すのはbath対の交差共分散射影である。各試行の2値結果、実現配置頻度、局所記録をこの集団量から直接読んではならない。

## J.10 完全matching fiberと証明済み射影の区別

枝 $s$、設定 $x$ に対する完全matching fiberを $\mathfrak M_{s,x}$ と書く。その最低条件は次の5つである。

1. bath対 $(z_A,z_B)$ がR147の $s$ 枝へ入る。
2. A実現配置 $X_A$ の周辺が $u_{s,x}$ のW型空間核と一致する。
3. B実現配置 $X_B$ の周辺が $\mathsf E\overline{u_{s,x}}$ のW型空間核と一致する。
4. 2翼の条件付きbath分布が、それぞれの未来のM47流と整合する。
5. 中央結合の切断後、局所分析器、傾斜固定、局所記録まで同じmatching関係を有限誤差で保存する。

R147、R148が単独で証明するのはbath射影

```math
\pi_z\mu_x^\tau
\longrightarrow
\pi_z\mathfrak M_x
```

だけであり、

```math
\mu_x^\tau
\longrightarrow
\mathfrak M_x
```

という完全共同測度の吸引ではない。交差共分散だけから単一試行頻度を作った扱いにすると、集団余弦重みだけを持ち単一試行周期を欠いた旧M30と同じ問題へ戻る。R149、R150はこの完全matchingと局所instrumentを抽象仮定にする。第5章のR151--R154は、固定singlet型Bell装置について、単一試行bath座標に条件付けた局所配置生成子、切断面の強いmatching fiber、切断後局所分析、再matching、固定、記録を構成し、この抽象仮定を有限誤差で充足する。Q2-1から同じ試行状態を渡す条件は付録Kで固定し、M49/R160が固定singlet供給プログラムについて満たす。

## J.11 R149：局所分析器からの条件付き余弦共同分布

spin-flip恒等式

```math
\mathsf E\overline{\Sigma_x}
=
-\Sigma_x\mathsf E
```

により、$u_{s,x}$ が $\Sigma_x$ の固有値 $s$ を持つなら

```math
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

は反対向きBlochベクトル $-s n_x$ を持つ。

<!-- theorem-start:theorem -->
**定理（R149：M48準備と局所M47分析器からの余弦共同分布）**

R148の各枝についてJ.10節の完全matchingが成立し、A局所分析器が $u_{s,x}$ を結果 $A=s$ の安全井戸へ写し、B局所分析器が $v_{s,x}$ を設定 $y$ で測ると仮定する。このとき理想安全枝では

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,n_x\cdot n_y
\right).
```

2枝が等重みなら

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left(
1-ab\,n_x\cdot n_y
\right),
```

```math
E(A\mid x,y)
=
E(B\mid x,y)
=
0,
\qquad
E(AB\mid x,y)
=
-n_x\cdot n_y.
```

平面設定では

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left[
1-ab\cos(x-y)
\right].
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$v_{s,x}$ のBlochベクトルは $-sn_x$ なので、B設定 $n_y$ の結果 $b$ の2値効果を作用させると条件付き確率式を得る。$P(s\mid x)=1/2$ を掛けて $s=a$ と置けば共同分布が従う。周辺と相関は2値和を取ればよい。証明終。
<!-- theorem-end:proof -->

R149はJ.10節の完全matchingを仮定した後の厳密結果である。R147、R148だけから結果頻度が出たとは分類しない。第5章のR153、R154を代入すると、固定Bell装置についてR149の仮定が充足され、R155の完全周期結果になる。

## J.12 無反応を含む有限時間分布

有限時間の一様率を使うときは $G_x^c$ を無反応 $\varnothing$ として残す。理想安全枝分布を $p_{xy}^{\rm safe}$ とすると、盆境界だけを有限化した完全結果分布は

```math
p_{xy}^{(h_*)}(a,b)
=
(1-h_*)p_{xy}^{\rm safe}(a,b),
```

```math
p_{xy}^{(h_*)}(\varnothing)
=
h_*.
```

無反応を持たない理想余弦分布を同じ拡大結果集合へ埋め込めば

```math
D_{\rm TV}
\left(
p_{xy}^{(h_*)},
p_{xy}^{\rm ideal}
\right)
=
h_*.
```

従って $h_*$ は事後選別率でなく、完全結果集合に残す有限時間誤差 $\varepsilon_{\rm basin}$ である。$h_*\downarrow0$ で無反応率は下がるが、R147の一様収束定数は増える。これは有限準備時間との交換である。R151のsetting-pre等重みseedを使う完全周期では、有限setting routingが最初から $|h_x|\geq h_*$ の安全盆へ入れる。そこではHaar盆境界質量 $h_*$ を固有の無反応率として加えず、seed biasとrouting失敗を $\varepsilon_{\rm seed}+\varepsilon_{\rm route}$ へ入れる。

## J.13 R150：有限誤差、非信号性、CHSH値、Bell監査

M48経路の1設定対当たりの前向き全変動誤差を

```math
\begin{aligned}
\varepsilon_{\rm Bell}^{48}
\leq{}&
\delta_{\rm set}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm route}
+
\varepsilon_{\rm PH}
+
\varepsilon_{\rm basin}
+
\varepsilon_{\rm fib}^{A}
+
\varepsilon_{\rm fib}^{B}\\
&+
\varepsilon_{\rm inst}^{A}
+
\varepsilon_{\rm inst}^{B}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}
\end{aligned}
```

と分ける。$\delta_{\rm set}$ は有限設定生成、$\varepsilon_{\rm seed}$ は等重みseed、$\varepsilon_{\rm route}$ は安全盆routing、$\varepsilon_{\rm PH}$ はR147、R148の有限時間吸引、$\varepsilon_{\rm basin}=h_*$ は無反応盆、$\varepsilon_{\rm fib}^{A,B}$ は完全matching、$\varepsilon_{\rm inst}^{A,B}$ は局所分析器・傾斜固定、$\varepsilon_{\rm cut}$ は中央切断、$\varepsilon_{\rm rec}$ は局所記録、$\varepsilon_{\rm clk}$ は時計窓である。帰還誤差は次周期へ渡し、同じ周期の観測済み分布へ遡って加えない。R153では連続bath方向を完全状態全変動距離でなくprojective fiber距離で評価し、R154の一様Lipschitz定数を通して結果全変動距離へ移す。

<!-- theorem-start:corollary -->
**系（R150：M48経路の有限誤差非信号性、CHSH破れ、Bell前提監査）**

各設定対の完全結果分布がR149の理想分布から全変動距離 $\varepsilon_{\rm Bell}^{48}$ 以下であるとする。このとき反対側設定を変えた一側周辺の差は $2\varepsilon_{\rm Bell}^{48}$ 以下である。無反応を数値0として相関を計算したCHSH値 $S_{48}$ は

```math
\left|
|S_{48}|-2\sqrt2
\right|
\leq
8\varepsilon_{\rm Bell}^{48}.
```

従って

```math
\varepsilon_{\rm Bell}^{48}
<
\frac{\sqrt2-1}{4}
```

なら有限誤差下でもCHSH不等式の破れが残る。
<!-- theorem-end:corollary -->

理想分布の一側周辺は反対側設定に依存しない。全変動距離の縮約性を各周辺へ使い、2つの設定分布を三角不等式で比較すると $2\varepsilon_{\rm Bell}^{48}$ を得る。絶対値1以下の相関量の期待値差は全変動距離の2倍以下なので、4相関のCHSH差は $8\varepsilon_{\rm Bell}^{48}$ 以下である。

Bell前提の監査は次の通りである。

| 監査項目 | M48経路 |
|---|---|
| 局所性 | 中央切断後は $P(A,B\mid\Lambda,x,y)=P_A(A\mid\Lambda_A,x)P_B(B\mid\Lambda_B,y)$ と因子化し、反対翼設定を局所方程式へ入れない |
| 測定設定独立性 | 測定開始面で $\mu_{\rm meas}(d\Lambda\mid x,y)=\mu_x(d\Lambda)$ なので成立しない。依存は設定前共通測度からのM48前向き流で生じる |
| 結果の一意性 | 安全枝では局所実現配置の井戸記録が1結果を与え、盆境界と有限装置遷移域は無反応へ送る |
| 事後選別 | 無反応を完全結果集合へ残し、採用試行だけで再規格化しない |
| 非信号性 | 理想周辺は $1/2$、有限誤差差はR150の上界を持つ |
| 試行測度 | 設定前基準測度 $\nu_0$、設定生成、M48押出し、切断、局所記録の順で定め、目的共同分布を初期測度へ直接置かない |

M48はBellの定理を否定しない。CHSH破れを可能にする位置は測定設定独立性であり、切断後の局所因子化とは別である。また、A設定が中央準備へ入るため、標準的な2側空間分離Bell実験を再現したとは主張しない。R150の抽象誤差項は、第5章のR153--R155でseed routing、強いmatching、局所記録を含む $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ へ具体化する。

## J.14 旧M39比較とM49の物理的受渡し

M39の行優先係数ベクトル $c=(c_{00},c_{01},c_{10},c_{11})^{\mathsf T}$ を係数行列へ戻す写像を

```math
\mathcal R(c)
=
\begin{pmatrix}
c_{00}&c_{01}\\
c_{10}&c_{11}
\end{pmatrix}
```

とする。既存singlet代表は

```math
\mathcal R(c_{\rm s})
=
\frac{\mathsf E}{\sqrt2}.
```

R148の $B_{AB}=-\mathsf E/\sqrt2$ はrow-majorで $-c_{\rm s}$ に対応し、同じ射影 $c_{\rm s}c_{\rm s}^\dagger$ を与える。従ってM39のsinglet出力とM48の交差共分散射影は代数的に一致する。

ただし、代数的射影一致は単一試行の物理的受渡しではない。旧R151の反対称filterは、非零な全入力をglobal phaseを除いて同じ $\mathsf E$ へ正規化するため、M39状態の違いをM48へ運ばない。等重み枝も内部fair seedで代替できる。旧主張の監査は `notes/superseded_m39_m48_handoff_claim.md` に残す。

M49/R160はこのfilterを使わない。設定前行分解共同bathへCNOTを同一試行で作用させ、得られた $z_A,z_B,X_A,X_B$ をsetting-free面で恒等搬送する。固定singlet供給プログラムでは、M49出力が式(4.35)、式(4.36)のpaired fiberへ厳密に入り、受渡し面のcross projector感度と枝bias感度も保存される。一般状態M48測定は依然として非主張である。

## J.15 M48単独周期で閉じた項目と残る非主張

setting-pre等重みseed、安全盆routing、2翼強matching、切断後局所分析、2翼記録、周期末帰還は、第5章と付録DのR151--R156で固定singlet型・固定有限設定族について閉じる。M49/R160はQ2-1の固定singlet出力を同じ試行registerでM48へ渡す。M41とM39単独模型は置換済み模型へ移す。

現稿で主張しない事項は次である。

1. M48開放方程式の具体的回路、流体、振動子浴からの導出。
2. M48の有限閉鎖Hamiltonian系への持ち上げ。
3. R152の配置応答率を具体的回路または有限閉鎖Hamiltonianから導出したこと。
4. 連続時間の全区間で強いmatching fiberが不変であること。
5. 任意のQ2-1出力を一般状態M48測定へ接続すること。
6. 準備後にA設定を自由変更する介入分布。
7. 空間的に隔たった2設定選択、有限伝播円錐、標準Bell実験。
8. 一般測定族を拘束するTsirelson原理。
9. 独立同分布型有限標本揺らぎ。
10. Q2-3の指数資源問題。
