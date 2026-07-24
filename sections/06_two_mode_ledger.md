@number: 6
@chapter: 本文
@title: 共通未来の比較器と二モード台帳
@status: cos 差動作用と sector 内の一様 soft-energy 密度を別々の位相空間幾何から導く。

## 6.1 phase-locked messenger

source が準備する二つの messenger を

$$
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
$$

$$
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
$$

とする。第5章の局所 pulse 後には

$$
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
$$

$$
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
$$

となる。$A,B$ は局所 anchor pointer にすでに記録されている。messenger はその符号と analyzer phase の写しを共通未来へ運ぶ。

相対角を

$$
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
$$

とする。setting が physical analyzer angle である場合、$\phi$ は装置表現に依存する。planar spin-like realization では $\phi(a)=a$、linear-polarization-like realization では double-angle map $\phi(a)=2a$ を用い得る。この写像は terminal rule ではなく、局所 analyzer の calibration に属する。

## 6.2 差動作用の cos 幾何

common-future difference mode の作用を

$$
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
$$

と定義する。直接展開すると

$$
I_-^{AB}
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right].
$$

\begin{proposition}[実二次元比較器の cos 恒等式]
等振幅 $r_A=r_B=r$、固定相対 source phase $\Theta_A-\Theta_B=\Phi_0$ の下で、

$$
I_-^{AB}
=
I_0
\left[
1-AB\cos
\left\{
\phi(a)-\phi(b)+\Phi_0
\right\}
\right],
$$

$$
I_0=\frac{r^2}{2}
$$

である。
\end{proposition}

Proof. 回転行列の内積

$$
n(\Theta_A)^{\mathsf T}
R[\phi(b)-\phi(a)]
n(\Theta_B)
=
\cos\Delta_{ab}
$$

を差ベクトルの二乗へ代入すればよい。

cos は複素確率振幅、Born rule、量子内積から導入されていない。二つの実 canonical vector の Euclidean inner product

$$
u_A\cdot u_B
=
ABr_Ar_B\cos\Delta_{ab}
$$

から出る。

## 6.3 amplitude mismatch と phase noise

source phase を

$$
\Theta_A-\Theta_B
=
\Phi_0+\delta
$$

とし、$r_A,r_B,\delta$ に setting と outcome sign から独立な準備分布を許す。terminal compatibility は $I_-$ に線形になるため、source variables を先に平均してよい。

$$
\overline I_-^{AB}
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle
-\frac{AB}{2}
\operatorname{Re}
\left[
e^{i\{\phi(a)-\phi(b)+\Phi_0\}}
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
\right].
$$

基準作用、visibility、phase offset を

$$
I_0
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle,
$$

$$
V
=
\frac{
2
\left|
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
\right|
}{
\left\langle
r_A^2+r_B^2
\right\rangle
},
$$

$$
\delta_0
=
\arg
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
$$

と置けば、

$$
\overline I_-^{AB}
=
I_0
\left[
1-ABV
\cos
\left\{
\phi(a)-\phi(b)+\Phi_0+\delta_0
\right\}
\right].
$$

Cauchy--Schwarz 不等式から

$$
0\leq V\leq1
$$

である。以下では phase offset を $\Delta_{ab}$ に吸収し、

$$
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
$$

と書く。

## 6.4 二モード台帳

比較器の未読変数として、一つの soft mode と一つの ledger mode を置く。

$$
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
\qquad
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right).
$$

両 mode の基準周波数を同じ $\omega_\ell>0$ とし、

$$
J_\ell
=
J_s+J_0,
$$

$$
E_\ell
=
\omega_\ell J_\ell
$$

を固定する。soft energy を

$$
h
=
\omega_\ell J_s
$$

とする。ledger mode は、soft mode に入っていない残余作用

$$
E_\ell-h
=
\omega_\ell J_0
$$

を保持する。

二つの action-angle 座標を

$$
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
\qquad
\nu=s,0
$$

と取れば、

$$
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
$$

固定総作用殻上の正規化 Liouville 測度を

$$
d\mu_\ell
=
\frac{
\delta\!\left(
E_\ell-\omega_\ell J_s-\omega_\ell J_0
\right)
dJ_s\,d\theta_s\,dJ_0\,d\theta_0
}{
\displaystyle
\int
\delta\!\left(
E_\ell-\omega_\ell J_s-\omega_\ell J_0
\right)
dJ_s\,d\theta_s\,dJ_0\,d\theta_0
}
$$

とする。

## 6.5 一様 soft-energy 周辺定理

\begin{theorem}[二モード台帳の一様周辺]
固定 $E_\ell>0$ の二モード作用殻上で、soft energy $h=\omega_\ell J_s$ の周辺密度は

$$
p_\ell(h)
=
\frac1{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}
$$

である。
\end{theorem}

Proof. 位相角を積分すると $(2\pi)^2$ を得る。$h=\omega_\ell J_s$ を固定した未規格化密度は

$$
\int_0^\infty
dJ_0\,
\delta
\left(
E_\ell-h-\omega_\ell J_0
\right)
\frac{dh}{\omega_\ell}
=
\frac{dh}{\omega_\ell^2}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

全質量は

$$
\int_0^{E_\ell}
\frac{dh}{\omega_\ell^2}
=
\frac{E_\ell}{\omega_\ell^2}.
$$

規格化すると $p_\ell(h)=1/E_\ell$ である。

この定理は、二つの一自由度 harmonic mode の density of states がともに定数であることの帰結である。結果 sector、setting、source phase は ledger shell の定義に現れないため、`[M]` の入口測度が各 sector で共通なら

$$
p
\left(
h\mid A,B,a,b
\right)
=
\frac1{E_\ell}
$$

となる。

## 6.6 有限非線形 mixer

固定総作用を保ったまま、soft mode と ledger mode の向きを攪拌する生成子を構成できる。次の二次量を定義する。

$$
J_x
=
q_sq_0+p_sp_0,
$$

$$
J_y
=
q_sp_0-p_sq_0,
$$

$$
J_z
=
J_s-J_0.
$$

直接計算から

$$
\{J_\ell,J_x\}
=
\{J_\ell,J_y\}
=
\{J_\ell,J_z\}
=
0
$$

である。有限個の非線形環境変数を $\chi=(X_\alpha,P_\alpha)$ とし、

$$
H_\chi
=
\sum_{\alpha=1}^{m}
\left[
\frac{P_\alpha^2}{2M_\alpha}
+\frac{M_\alpha\Omega_\alpha^2X_\alpha^2}{2}
+\lambda_\alpha X_\alpha^4
\right]
+
\sum_{\alpha<\beta}
c_{\alpha\beta}X_\alpha^2X_\beta^2
$$

を一例とする。mixer coupling を

$$
K_M
=
\epsilon
\left[
g_x(\chi)J_x
+g_y(\chi)J_y
+g_z(\chi)J_z
\right]
$$

とすれば、

$$
\{J_\ell,K_M\}=0.
$$

従って

$$
H_{\ell\chi}
=
\omega_\ell J_\ell
+H_\chi
+K_M
$$

は有限で滑らかであり、総 ledger action を厳密に保存しながら、二 mode 間の作用配分と相対位相を変化させる。

有限の非線形環境が少数自由度でも中心振動子の実効的エネルギー分散と熱化を起こし得ることは、具体的な古典模型で確認されている [40]。ただし本論文で必要なのは bath が ledger energy を吸収することではない。$J_\ell$ を保ったまま、固定作用殻の orientation を有限分解能で攪拌することである。

## 6.7 不変測度と動的混合の区別

二モード定理には二つの読み方がある。

1. **ensemble reading**：比較器入口を固定作用殻の正規化 Liouville 測度で準備する。この場合 $p_\ell(h)=1/E_\ell$ は厳密である。
2. **typical-time reading**：一つの初期 microstate を finite mixer で長時間発展させ、有限分解能の time histogram を入口測度として用いる。この場合は mixing と時間尺度分離が必要である。

Hamiltonian flow は fine-grained Liouville density を保存する。従って任意の初期密度が $L^1$ または pointwise に一様密度へ収束するとは言えない。mixing が与え得るのは、滑らかな coarse observable $F$ に対する

$$
\frac1{\tau_{\rm cmp}}
\int_0^{\tau_{\rm cmp}}
F[h(t)]dt
\approx
\int_0^{E_\ell}
F(h)\frac{dh}{E_\ell}
$$

という有限時間平均、または初期 cell を粗視化した弱い収束である。

必要な時間尺度は

$$
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}.
$$

$\tau_{\rm mix}$ は coarse histogram の緩和、$\tau_{\rm cmp}$ は comparator が ledger state を読み出す前の混合窓、$T_{\rm rec}$ は有限 mixer の再帰尺度である。本論文は一般の $K_M$ に対してこの不等式を証明しない。これは数値検証すべき `[M]` の動力学部分である。

## 6.8 通常の多モード浴が失敗する理由

soft mode が $N$ 個の通常 ledger mode と固定総エネルギーを自由に分け合うとする。各 mode が一つの harmonic canonical pair で、全 simplex

$$
h+\sum_{j=1}^{N}e_j=E_\ell,
\qquad
h,e_j\geq0
$$

上の一様 Liouville measure を用いる。$h$ を固定した残余 simplex の体積は $(E_\ell-h)^{N-1}$ に比例するので、

$$
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1},
\qquad
0\leq h\leq E_\ell.
$$

しきい値 $x$ 以下の累積重みは

$$
F_N(x)
=
\int_0^x p_N(h)dh
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
$$

$N=1$ のときだけ

$$
F_1(x)=\frac{x}{E_\ell}
$$

が線形である。$N>1$ では $x$ の二次以上の項が現れる。第7章のしきい値

$$
x_{AB}
=
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
$$

を代入すると、$\cos^2\Delta_{ab}$ 以上の高調波が一般に残る。

従って「大きな bath ほど Bell の cos 則に近づく」という主張は成立しない。純粋な線形 compatibility に必要なのは、

- 一つの soft canonical pair。
- 一つの ledger canonical pair。
- 総作用を保った orientation mixing。

という最小構造である。追加 bath は mixer の chaos を作る補助であり、threshold-dependent energy を自由に共有する ledger へしてはならない。

## 6.9 sector 質量の対称性

二モード定理が決めるのは各 outcome sector 内の条件付き密度であり、sector 自体の基準質量ではない。基準 preparation measure における四 sector を

$$
\Sigma_{AB}
=
\left\{
\sigma(s_A)=A,\,
\sigma(s_B)=B
\right\}
$$

とし、

$$
w_{AB}
=
\mu_S(\Sigma_{AB})
$$

と定義する。

preparation stage に二つの measure-preserving involution

$$
\mathcal S_A:
\Sigma_{AB}
\longrightarrow
\Sigma_{-A,B},
$$

$$
\mathcal S_B:
\Sigma_{AB}
\longrightarrow
\Sigma_{A,-B}
$$

があり、$H_{\rm prep}$、preparation macroregion、$\mu_S$ を保つとする。二つの変換が生成する群は四 sector に推移的に作用する。

\begin{proposition}[対称準備の sector 等体積]
上の独立符号反転対称性 `[S]` の下で、

$$
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14
$$

である。
\end{proposition}

Proof. $\mathcal S_A$ と $\mathcal S_B$ は measure-preserving bijection なので、任意の二 sector の測度は等しい。四 sector が全 preparation support を分割するため、規格化すると各質量は $1/4$ である。

Hamiltonian の符号対称性だけでは不十分である。同じ Hamiltonian に非対称な初期密度を置くことも可能だからである。`[S]` は「対称な preparation macrostate 上の不変基準測度を採用する」という統計条件を含む。

## 6.10 共通入口密度

第6.5節と第6.9節を組み合わせると、比較器入口での outcome sector と soft energy の基準密度は

$$
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

`[S]` の下では

$$
g_{AB}^{\rm ent}(h)
=
\frac1{4E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

この式で

- $1/E_\ell$ は二モード作用殻の幾何。
- $1/4$ は準備 sector の対称性。

から来る。二つを一つの「等基準因子」として仮定しないことが、本改訂の中心である。

## 6.11 本章の結論

Bell 型 cos 重みの角度依存性と線形確率変換は、異なる二つの幾何から生じる。cos は二つの実 messenger の差動作用、一様 threshold density は一つの soft pair と一つの ledger pair の固定総作用殻から生じる。

finite nonlinear bath は後者の不変測度を作る論理原理ではなく、その orientation を有限時間で典型化する候補機構である。sector mass はさらに preparation symmetry `[S]` を必要とする。次章では、setting-blind terminal coordinate へこの二つの結果を代入し、共同確率を導く。
