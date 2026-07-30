@number: 6
@chapter: 本文
@title: 共通未来の比較器と2モード作用分配系
@status: 固定作用殻の余弦幾何と一様周辺は厳密結果、弱開放時の総作用漏れと動的準備は近似または未解決として分離する。

## 6.1 位相同期した伝達ベクトル

生成源が準備する2つの伝達ベクトルを

```math
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
```

```math
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
```

とする。第5章の局所パルス後には

```math
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
```

```math
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
```

となる。$A,B$ は局所固定指針にすでに記録されている。伝達ベクトルは、その符号と分析器位相の写しを共通未来へ運ぶ。

相対角を

```math
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
```

とする。測定設定が物理的な分析器角である場合、$\phi$ は装置表現に依存する。平面回転型では $\phi(a)=a$、直線偏光型では倍角写像 $\phi(a)=2a$ を用い得る。この写像は終端規則ではなく、局所分析器の較正に属する。

## 6.2 差動作用の余弦幾何

共通未来の差動モード作用を

```math
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
```

と定義する。直接展開すると

```math
I_-^{AB}
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right].
```

<!-- theorem-start:proposition -->
**命題（実2次元比較器の余弦恒等式）**
等振幅 $r_A=r_B=r$、固定相対生成源位相 $\Theta_A-\Theta_B=\Phi_0$ の下で、

```math
I_-^{AB}
=
I_0
\left[
1-AB\cos
\left\{
\phi(a)-\phi(b)+\Phi_0
\right\}
\right],
```

```math
I_0=\frac{r^2}{2}
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
回転行列の内積

```math
n(\Theta_A)^{\mathsf T}
R[\phi(b)-\phi(a)]
n(\Theta_B)
=
\cos\Delta_{ab}
```

を差ベクトルの2乗へ代入すればよい。
<!-- theorem-end:proof -->

余弦は複素確率振幅、Born 則、量子内積から導入されていない。2つの実正準ベクトルの Euclid 内積

```math
u_A\cdot u_B
=
ABr_Ar_B\cos\Delta_{ab}
```

から出る。

## 6.3 振幅不一致と位相雑音

生成源位相を

```math
\Theta_A-\Theta_B
=
\Phi_0+\delta
```

とし、$r_A,r_B,\delta$ に測定設定と結果符号から独立な準備分布を許す。終端整合重みは $I_-$ に線形になるため、生成源変数を先に平均してよい。

```math
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
```

基準作用、可視度、位相ずれを

```math
I_0
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle,
```

```math
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
```

```math
\delta_0
=
\arg
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
```

と置けば、

```math
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
```

Cauchy--Schwarz 不等式から

```math
0\leq V\leq1
```

である。以下では位相ずれを $\Delta_{ab}$ に吸収し、

```math
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
```

と書く。

## 6.4 2モード作用分配系

閉鎖補助モデルの未読変数として、1つのソフトモードと1つの残余作用モードを置く。

```math
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
```

両モードの基準周波数を同じ $\omega_\ell>0$ とし、

```math
J_\ell
=
J_s+J_0,
```

```math
E_\ell
=
\omega_\ell J_\ell
```

を固定する。ソフトモードのエネルギーを

```math
h
=
\omega_\ell J_s
```

とする。残余作用モードは、ソフトモードに入っていない残余作用

```math
E_\ell-h
=
\omega_\ell J_0
```

を保持する。

2つの作用・角変数を

```math
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
\qquad
\nu=s,0
```

と取れば、

```math
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
```

固定総作用殻上の正規化 Liouville 測度を

```math
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
```

とする。

固定総作用殻は Hamiltonian の式だけから自動的に準備されるわけではない。現行の弱開放モデルでは、試行前に仕事貯蔵系と外部環境を用いて $E_\ell$ の狭い入口分布を準備し、比較窓中には外部交換を小さく保つ必要がある。従って、殻上の幾何は厳密結果である一方、その殻を繰り返し準備する機構は `[M]` の物理的実現として別に監査する。

## 6.5 一様なソフトモードエネルギー周辺定理

<!-- theorem-start:theorem -->
**定理（2モード作用分配系の一様周辺）**
固定 $E_\ell>0$ の2モード作用殻上で、ソフトモードのエネルギー $h=\omega_\ell J_s$ の周辺密度は

```math
p_\ell(h)
=
\frac1{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
位相角を積分すると $(2\pi)^2$ を得る。$h=\omega_\ell J_s$ を固定した未規格化密度は

```math
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
```

全質量は

```math
\int_0^{E_\ell}
\frac{dh}{\omega_\ell^2}
=
\frac{E_\ell}{\omega_\ell^2}.
```

規格化すると $p_\ell(h)=1/E_\ell$ である。
<!-- theorem-end:proof -->

この定理は、2つの1自由度調和モードの状態密度がともに定数であることの帰結である。結果領域、測定設定、生成源位相は固定総作用殻の定義に現れないため、`[M]` の入口測度が各結果領域で共通なら

```math
p
\left(
h\mid A,B,a,b
\right)
=
\frac1{E_\ell}
```

となる。

## 6.6 有限非線形混合器

ソフトモードと残余作用モードの総作用 $J_\ell$ を保存したまま、2モード間の作用配分と相対位相を変える有限 Hamiltonian 生成子を構成できる。必要な生成子は

```math
\{J_\ell,K_M\}=0
```

を満たす。具体的には、2モードの双線形生成子と有限個の非線形環境変数を結合すればよい。全生成子、Poisson 括弧、保存則は付録C.8に示す。

この構成が保証するのは、固定総作用殻とその Liouville 測度が不変であることだけである。特定の有限混合器が必要な時間窓で十分に混合することは、生成子の存在からは従わない。混合速度、再帰時間、有限分解能での偏差は別に検証する必要がある。

## 6.7 不変測度と動的混合の区別

2モード定理には2つの読み方がある。

1. **集団としての準備**：比較器入口を固定作用殻の正規化 Liouville 測度で準備する。この場合 $p_\ell(h)=1/E_\ell$ は厳密である。
2. **時間典型性による準備**：1つの初期微視状態を有限混合器で長時間発展させ、有限分解能の時間頻度分布を入口測度として用いる。この場合は混合と時間尺度分離が必要である。

Hamiltonian 流れは微細 Liouville 密度を保存する。したがって任意の初期密度が $L^1$ または各点で一様密度へ収束するとは言えない。混合が与え得るのは、滑らかな粗視化観測量 $F$ に対する

```math
\frac1{\tau_{\rm cmp}}
\int_0^{\tau_{\rm cmp}}
F[h(t)]dt
\approx
\int_0^{E_\ell}
F(h)\frac{dh}{E_\ell}
```

という有限時間平均、または初期小領域を粗視化した弱い収束である。

必要な時間尺度は

```math
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}.
```

$\tau_{\rm mix}$ は粗視化頻度分布の緩和、$\tau_{\rm cmp}$ は比較器が作用分配系の状態を読み出す前の混合窓、$T_{\rm rec}$ は有限混合器の再帰尺度である。本論文は一般の $K_M$ に対してこの不等式を証明しない。これは数値検証すべき `[M]` の動力学部分である。

### 6.7.1 弱開放時の総作用漏れ

比較窓中の総作用エネルギーを

```math
E_\ell(t)
=
E_\ell+\Delta E_\ell(t)
```

とし、

```math
\varepsilon_\ell
=
\frac{
\sup_t
\left|
\Delta E_\ell(t)
\right|
}{
E_\ell
}
\ll1
```

を仮定する。しきい値 $x$ が殻の両端から、漏れ幅と終端分解能幅より十分離れているなら、各瞬間の一様殻に対する累積体積は

```math
\frac{x}{E_\ell+\Delta E_\ell}
=
\frac{x}{E_\ell}
+
O(\varepsilon_\ell)
```

である。さらに有限時間混合の粗視化誤差を $\varepsilon_{\rm mix}$ とすると、Bell 重みに入る累積分布の主要誤差は

```math
O
\left(
\varepsilon_\ell
+
\varepsilon_{\rm mix}
\right)
```

となる。

この評価が一様に使えるのは、$\Delta E_\ell$ と混合誤差が結果符号および測定設定に依存しない場合である。結果または設定に相関した漏れは、規格化で消えず、高次調波、設定頻度の変化、一側周辺の残差を生み得る。従って総作用漏れは単なる可視度補正とは限らず、中心結論を反証し得る観測量である。

固定殻の一様周辺は厳密結果である。上の弱開放補正は、$\varepsilon_\ell$ と $\varepsilon_{\rm mix}$ を測定し、元の有限モデルと比較する範囲でのみ近似結果として採用する。

## 6.8 多モード補助比較と2モード条件

ここでは、多数の残余作用モードを現行の Bell 重み生成器として採用せず、2モード条件の成立範囲を調べる補助比較モデルとして用いる。

ソフトモードが $N$ 個の残余作用モードと固定総エネルギーを自由に分け合うとする。各モードが1つの調和正準対で、全単体

```math
h+\sum_{j=1}^{N}e_j=E_\ell,
\qquad
h,e_j\geq0
```

上の一様 Liouville 測度を用いる。$h$ を固定した残余単体の体積は $(E_\ell-h)^{N-1}$ に比例するので、

```math
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1},
\qquad
0\leq h\leq E_\ell.
```

しきい値 $x$ 以下の累積重みは

```math
F_N(x)
=
\int_0^x p_N(h)dh
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
```

$N=1$ のときだけ

```math
F_1(x)=\frac{x}{E_\ell}
```

が線形である。$N>1$ では $x$ の二次以上の項が現れる。第7章のしきい値

```math
x_{AB}
=
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
```

を代入すると、$\cos^2\Delta_{ab}$ 以上の高調波が一般に残る。

したがって「大きな浴ほど Bell の余弦則に近づく」という主張は成立しない。この否定的結果は、中心モデルに必要な構造を次のように限定する。

- 1つのソフトモードの正準対。
- 1つの残余作用モードの正準対。
- 総作用を保つ向き混合。

という最小構造である。追加浴は混合器の複雑な運動を作る補助にできるが、しきい値依存エネルギーを自由に共有する作用分配自由度にしてはならない。多モード補助比較を残す理由は、この2モード条件を論証するためであり、多モード構成自体を現行モデルへ採用するためではない。

## 6.9 結果領域の質量対称性

2モード定理が決めるのは各結果領域内の条件付き密度であり、領域自体の基準質量ではない。基準準備測度における4領域を

```math
\Sigma_{AB}
=
\left\{
\sigma(s_A)=A,\,
\sigma(s_B)=B
\right\}
```

とし、

```math
w_{AB}
=
\mu_S(\Sigma_{AB})
```

と定義する。

準備段階に2つの測度保存対合

```math
\mathcal S_A:
\Sigma_{AB}
\longrightarrow
\Sigma_{-A,B},
```

```math
\mathcal S_B:
\Sigma_{AB}
\longrightarrow
\Sigma_{A,-B}
```

があり、$H_{\rm prep}$、準備巨視領域、$\mu_S$ を保つとする。2つの変換が生成する群は4領域に推移的に作用する。

<!-- theorem-start:proposition -->
**命題（対称準備の結果領域等体積）**
上の独立符号反転対称性 `[S]` の下で、

```math
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$\mathcal S_A$ と $\mathcal S_B$ は測度保存全単射なので、任意の2領域の測度は等しい。4領域が準備測度の全台を分割するため、規格化すると各質量は $1/4$ である。
<!-- theorem-end:proof -->

Hamiltonian の符号対称性だけでは不十分である。同じ Hamiltonian に非対称な初期密度を置くことも可能だからである。`[S]` は「対称な準備巨視状態上の不変基準測度を採用する」という統計条件を含む。

## 6.10 共通入口密度

第6.5節と第6.9節を組み合わせると、比較器入口での結果領域とソフトモードエネルギーの基準密度は

```math
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
```

`[S]` の下では

```math
g_{AB}^{\rm ent}(h)
=
\frac1{4E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
```

この式で

- $1/E_\ell$ は2モード作用殻の幾何。
- $1/4$ は準備領域の対称性。

から来る。2つを1つの仮定へまとめず、位相体積と準備対称性を分けて管理する。

## 6.11 本章の結論

Bell 型余弦重みの角度依存性と線形確率変換は、異なる2つの幾何から生じる。余弦は2つの実伝達ベクトルの差動作用、一様なしきい値密度は1つのソフトモードの正準対と1つの残余作用モードの正準対がつくる固定総作用殻から生じる。

有限非線形浴は後者の不変測度を作る論理原理ではなく、その向きを有限時間で典型化する候補機構である。結果領域の質量はさらに準備対称性 `[S]` を必要とする。

固定殻の閉鎖補助モデルでは一様周辺は厳密である。弱開放な現行モデルでは、総作用漏れ、有限時間混合、入口準備幅が主要誤差になる。次章ではまず閉鎖補助モデルの厳密な体積計算を行い、その物理的試行予測が `[R]` と弱開放近似へ依存することを分けて示す。
