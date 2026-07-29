@number: A3
@chapter: 付録
@title: Hamiltonian 装置部品、2モード位相体積、補正項
@status: 第II部の理想正準写像、有限幅誤差、厳密な比較窓、作用殻測度、多モード補正を計算する。

本付録が与えるのは、装置を構成する有限 Hamiltonian 部品と、その正準計算である。生成源、設定制御器、全自由発展を含む1本の完全な実験 Hamiltonian が、全ての理想写像を有限時間で誤差なく実行するとは主張しない。一般の局所パルスは短時間極限で理想写像へ近づき、第7.1節の比較読出しだけは、保存量との交換関係により有限幅でも厳密である。

## C.1 Poisson 構造

各正準対 $(q_j,p_j)$ に

```math
\{q_j,p_k\}
=
\delta_{jk}
```

を置く。伝達ベクトル $u=(Q,P)^{\mathsf T}$ と作用

```math
I=\frac12(Q^2+P^2)
```

に対し、生成子

```math
K_{\rm rot}
=
-\theta I
```

の単位流れは

```math
\dot Q=-\theta P,
\qquad
\dot P=\theta Q
```

なので

```math
u(1)
=
R(\theta)u(0).
```

$\theta=\phi(a)+\pi\chi_-(s)$ とし、結果種の平坦領域上で $A=\sigma(s)$ とすれば

```math
R
\left[
\phi(a)+\pi\chi_-(s)
\right]
=
A R[\phi(a)].
```

したがって結果符号を伝達ベクトル位相の $\pi$ 移動として正準的に記録できる。

## C.2 応答モードと固定指針の移動

応答モード対 $(x,p)$ に対する生成子

```math
K_{\rm br}
=
-x\sigma(s)
```

は

```math
\dot p
=
-\frac{\partial K_{\rm br}}{\partial x}
=
\sigma(s),
```

```math
\dot x
=
\frac{\partial K_{\rm br}}{\partial p}
=
0
```

を与える。$p(0)=0$ なら $p(1)=A$ である。

固定指針対 $(Y,\Pi)$ に対する

```math
K_{\rm lock}
=
-Y\zeta(p)
```

は

```math
\dot\Pi
=
-\frac{\partial K_{\rm lock}}{\partial Y}
=
\zeta(p),
```

```math
\dot Y=0,
\qquad
\dot p=0
```

を与える。$\zeta(\pm1)=\pm1$ の平坦領域で $\Pi(0)=0$ なら、

```math
\Pi(1)=A.
```

2つの写像は Hamiltonian 流れなので位相体積を保存する。応答モードの情報を局所浴へ分散した後も、固定指針対を切り離せば比較窓の記録符号は保たれる。

## C.3 自律順序時計と有限幅誤差

時計対 $(\vartheta,J_c)$ と、互いに重ならないパルス形 $f_{\nu,\epsilon}(\vartheta)$ を用い、

```math
H
=
\Omega J_c
+H_0
+\Omega
\sum_\nu
f_{\nu,\epsilon}(\vartheta)K_\nu
```

とする。$K_\nu$ と $H_0$ が $J_c$ に依存しないとき、

```math
\dot\vartheta=\Omega.
```

$f_{\nu,\epsilon}$ を

```math
\int_{\operatorname{supp}f_{\nu,\epsilon}}
f_{\nu,\epsilon}(\vartheta)d\vartheta=1
```

と規格化すれば、対応する時間区間で

```math
\int
\Omega f_{\nu,\epsilon}[\vartheta(t)]dt=1.
```

自由 Hamiltonian $H_0$ を無視すれば、この積分は $K_\nu$ の単位正準写像を与える。しかし全 Hamiltonian では $H_0$ も同時に働く。相互作用表示で Duhamel 展開を用いると、パルスの時間幅を $\epsilon_\nu$ として、有界な適用領域 $\mathcal K$ 上で

```math
\sup_{z\in\mathcal K}
\left\|
\Phi_{\rm full}^{(\nu)}(z)
-
e^{X_{K_\nu}}z
\right\|
\leq
C_{\mathcal K}\epsilon_\nu
```

となる。定数 $C_{\mathcal K}$ は、$\mathcal K$ 上の $X_{H_0}$、$X_{K_\nu}$、それらの第1微分の上界で決まる。したがって、本文の局所分析器と指針固定は短時間パルス極限の理想写像であり、有限幅では $O(\epsilon_\nu)$ の補正を持つ。

パルス形の台が重なる場合には、さらに Poisson 括弧 $\{K_\mu,K_\nu\}$ に比例する補正が生じる。本論文では台を分離し、この補正を使わない。第7.1節の比較読出しは、読出し対象の作用が全比較窓 Hamiltonian と交換するため、この一般誤差評価より強い厳密式を持つ。

## C.4 相補的内部時計、2境界照合、向き平均の否定結果

まず、時計運動量を $\pm\varrho_0$ の極小へ固定するだけの Hamiltonian

```math
H_{\rm stop}
=
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
+
\frac{\lambda_c}{4}
\sum_{X=A,B}
\left(
\varrho_X^2-\varrho_0^2
\right)^2
```

は用いない。極小

```math
\left(
\varrho_A,\varrho_B
\right)
=
\left(
+\varrho_0,-\varrho_0
\right)
```

では

```math
\dot\tau_X
=
\frac{\partial H_{\rm stop}}{\partial\varrho_X}
=
0
```

となり、向きは区別できても時計が進まないからである。

実際に相補的な時計運動を作る最小の二次 Hamiltonian として

```math
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
```

を用いる。中心・相対変数を

```math
\bar\tau
=
\frac{\tau_A+\tau_B}{2},
\qquad
Y_R
=
\tau_A-\tau_B,
```

```math
P_c
=
\varrho_A+\varrho_B,
\qquad
\Pi_R
=
\frac{\varrho_A-\varrho_B}{2}
```

と定めると、

```math
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R.
```

したがって変換は正準であり、

```math
H_{\rm or}
=
\frac{\Pi_R^2}{M_\tau}
+
\left(
\frac{1}{4M_\tau}
+
\frac{\kappa_c}{2}
\right)
P_c^2.
```

$P_c=0$ 上では

```math
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
```

```math
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
```

比較パルス直前に $\Pi_R=E_*>0$ を準備し、終端比較生成子を

```math
K_R
=
Y_R
\left(
h-\kappa I_-
\right)
```

とする。$K_R$ は $\bar\tau$ に依存しないので $P_c=0$ は保たれる。さらに

```math
\{h,K_R\}
=
\{I_-,K_R\}
=
0
```

なので、比較パルス中も $h$ と $I_-$ は保存される。相補時計の自由運動により

```math
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}
```

であり、$Y_R$ は一般に動く。一方、規格化したパルス係数を $g_R(t)$ とすれば

```math
\dot\Pi_R
=
g_R(t)
\left(
\kappa I_- -h
\right),
\qquad
\int g_R(t)dt=1
```

である。したがって有限幅パルスでも厳密に

```math
\Delta\Pi_R
=
\kappa I_- -h,
```

```math
\Pi_R(T)
=
E_*+\kappa I_- -h.
```

したがって

```math
\Pi_R(T)\geq0
\quad\Longleftrightarrow\quad
\varrho_A(T)\geq0
\quad\land\quad
\varrho_B(T)\leq0.
```

終端半空間は、初期に選んだ時計向きの順序を保存した履歴の集合として得られる。一方、$\Pi_R(T)<0$ の軌道も正則な Hamiltonian 軌道であり、時計向きが交換されるだけである。

この半空間から `[R]` の積形式を得るには、さらに2境界の統計的照合を置く必要がある。初期境界の密度を $\rho_S(z_i)$、逆向き時計の時計過去に対応する終端関数を $G_{\rm or}(z_f)$ とし、両枝が同じ Hamiltonian 履歴を表す条件を

```math
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
```

で課す。履歴空間上の測度を

```math
d\nu
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
```

とすれば、$z_f$ 積分により

```math
d\nu_i
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i.
```

これは `[R]` と同じ積形式である。Hamiltonian 流れの Jacobian が1であるため、逆向きに積分しても余分な密度因子は出ない。ただし2つの境界密度を掛けて照合する規則は、Hamilton 方程式とは別の全履歴統計原理である。

最後に、向きの順序を指定しない素朴な平均を考える。同じスカラー読出し

```math
\Pi_R(T)
=
x-h,
\qquad
x
=
E_*+\kappa I_-,
```

に対して正向き半空間を $\Pi_R(T)\geq0$、相補的半空間を $\Pi_R(T)\leq0$ とし、$0\leq x\leq E_\ell$ で一様な $h$ を積分すると、

```math
F_+(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\leq x\}}
=
\frac{x}{E_\ell},
```

```math
F_-(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\geq x\}}
=
1-\frac{x}{E_\ell}.
```

両者を等重みで足せば

```math
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12
```

となり、$I_-$ の余弦依存性は消える。したがって $\varrho_A=-\varrho_B$ という無向きの相補性だけでは Bell 重みを保てない。順序付き境界領域を採るか、時間反転した領域では比較パルスの符号も反転する共変な追加構造が必要である。

## C.5 差動モード作用

2つの伝達ベクトルを

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

とする。シンプレクティック分岐器

```math
u_+
=
\frac{u_A+u_B}{\sqrt2},
\qquad
u_-
=
\frac{u_A-u_B}{\sqrt2}
```

は総作用を保存する。

```math
\frac12\|u_A\|^2
+\frac12\|u_B\|^2
=
\frac12\|u_+\|^2
+\frac12\|u_-\|^2.
```

反対称出力の作用は

```math
\frac12\|u_-\|^2
=
\frac14\|u_A-u_B\|^2
=
I_-.
```

内積を展開して

```math
I_-
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right]
```

を得る。この物理的な分岐写像を実行してから反対称出力の作用を比較器へ結合してもよく、同じ2次観測量へ直接結合してもよい。

## C.6 有限幅の終端比較読出し

比較窓 Hamiltonian を

```math
H_{\rm win}
=
H_{\rm or}
+
\omega_-I_-
+
\omega_\ell(J_s+J_0)
+
\Omega J_c
+
\Omega f_R(\vartheta)
Y_R
\left(
h-\kappa I_-
\right)
```

とする。$f_R$ の台は他のパルスと交わらず、

```math
\int f_R(\vartheta)d\vartheta=1
```

と規格化する。$H_{\rm win}$ は $J_c$ へ線形なので

```math
\dot\vartheta=\Omega
```

である。差動作用とソフトモードのエネルギーについて、

```math
\dot I_-
=
\{I_-,H_{\rm win}\}
=
0,
```

```math
\dot h
=
\{h,H_{\rm win}\}
=
0
```

が厳密に成り立つ。比較パルスは対応する角変数を移動させるが、2つの作用を変えない。

終端比較対については

```math
\dot\Pi_R
=
\Omega f_R(\vartheta)
\left(
\kappa I_- -h
\right),
```

```math
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}.
```

したがって $Y_R$ は一般にパルス中も動く。旧生成子 $F_R(Y_R)(h-\kappa I_-)$ に対して $Y_R=0$ を仮定する方法は、$H_{\rm or}$ との同時発展を無視していた。

修正後の線形生成子では $\dot\Pi_R$ が $Y_R$ に依存しない。$I_-$ と $h$ も定数なので、

```math
\Pi_R(T)-\Pi_R(t_R^-)
=
\left(
\kappa I_- -h
\right)
\int_{t_R^-}^{t_R^+}
\Omega f_R[\vartheta(t)]dt
=
\kappa I_- -h.
```

したがって $\Pi_R(t_R^-)=E_*$ なら

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

が有限幅パルスで厳密に成り立つ。比較器は $I_-$ と $h$ を非破壊的に読み出すが、それらの角変数を不変に保つとは主張しない。

## C.7 2モード作用殻の正規化

2つの作用・角変数対に対し、

```math
\mathcal N(E_\ell)
=
\int_0^\infty
dJ_s
\int_0^{2\pi}
d\theta_s
\int_0^\infty
dJ_0
\int_0^{2\pi}
d\theta_0
\delta
\left[
E_\ell-\omega_\ell(J_s+J_0)
\right].
```

$J_0$ を積分すると

```math
\mathcal N(E_\ell)
=
\frac{(2\pi)^2}{\omega_\ell}
\int_0^{E_\ell/\omega_\ell}
dJ_s
=
\frac{(2\pi)^2E_\ell}{\omega_\ell^2}.
```

$h=\omega_\ell J_s$ の区間 $[h,h+dh]$ に入る作用殻測度は

```math
d\mathcal N_h
=
\frac{(2\pi)^2}{\omega_\ell^2}dh.
```

従って

```math
p_\ell(h)dh
=
\frac{d\mathcal N_h}{\mathcal N(E_\ell)}
=
\frac{dh}{E_\ell}.
```

同じ結果は、尺度を変えた Descartes 座標

```math
\frac1{\sqrt{2J_\ell}}
\left(
q_s,p_s,q_0,p_0
\right)
```

が3次元球面 $S^3$ 上にあることからも分かる。

```math
\frac{J_s}{J_\ell}
=
\frac{q_s^2+p_s^2}{
q_s^2+p_s^2+q_0^2+p_0^2
}
```

は Beta$(1,1)$、すなわち $[0,1]$ 上の一様分布である。

## C.8 混合器生成子

次を定義する。

```math
J_x=q_sq_0+p_sp_0,
```

```math
J_y=q_sp_0-p_sq_0,
```

```math
J_z=\frac12
\left(
q_s^2+p_s^2-q_0^2-p_0^2
\right),
```

```math
J_\ell
=
\frac12
\left(
q_s^2+p_s^2+q_0^2+p_0^2
\right).
```

Poisson 括弧を直接計算すると、

```math
\{J_\ell,J_i\}=0,
\qquad
i=x,y,z.
```

また、規格化の取り方に応じた定数因子を除き、$J_x,J_y,J_z$ は $\mathfrak{su}(2)$ 型の閉じた括弧を持つ。したがって

```math
K_M
=
a_x(t)J_x+a_y(t)J_y+a_z(t)J_z
```

の各流れは $S^3$ 上の測度保存向き写像である。係数 $a_i(t)$ を有限非線形環境と自律時計から生成すれば、全系を Hamiltonian に保ったまま複雑な向き運動を作れる。

この事実は $p(h)$ の不変基準測度を保証するが、特定の決定論的係数列が混合を起こすことを自動的には保証しない。混合率は、相関減衰または転送作用素のスペクトルで別に検証する必要がある。

## C.9 多モード単体の周辺分布

ソフトモードエネルギー $h$ と $N$ 個の残余作用エネルギー $e_1,\ldots,e_N$ が

```math
h+\sum_{j=1}^{N}e_j=E_\ell
```

を満たすとする。各調和対の位相角を積分すると定数になる。$h$ を固定した残余単体

```math
\sum_{j=1}^{N}e_j=E_\ell-h,
\qquad
e_j\geq0
```

の面上の重複度は

```math
\frac{(E_\ell-h)^{N-1}}{(N-1)!}
```

に比例する。規格化から

```math
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1}.
```

累積分布は

```math
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
```

$N=1$ でのみ線形である。$x=C-ABKc$ と書けば、

```math
F_N(C-ABKc)
=
1-
\sum_{m=0}^{N}
\binom Nm
\left(
1-\frac C{E_\ell}
\right)^{N-m}
\left(
\frac{ABKc}{E_\ell}
\right)^m.
```

偶数 $m$ は結果の偶奇に依存しない規格化補正、奇数 $m\geq3$ は $c^3,c^5,\ldots$ を通じて高次角度調波を生む。したがって追加の残余作用モードは単なる可視度の再規格化ではない。

## C.10 有限終端幅

鋭い指示関数を単調応答 $g_\epsilon$ へ置き換える。

```math
G_{R,\epsilon}
=
g_\epsilon
\left(
E_*+\kappa I_- -h
\right).
```

一様なソフトモードエネルギー密度に対する整合重みは

```math
F_\epsilon(x)
=
\frac1{E_\ell}
\int_0^{E_\ell}
g_\epsilon(x-h)dh.
```

$g_\epsilon$ が Heaviside 関数と対称平滑化核の畳み込みなら、

```math
\frac{dF_\epsilon}{dx}
=
\frac1{E_\ell}
\left[
g_\epsilon(x)-g_\epsilon(x-E_\ell)
\right].
```

内部領域

```math
\epsilon\ll x\ll E_\ell-\epsilon
```

では $g_\epsilon(x)\approx1$、$g_\epsilon(x-E_\ell)\approx0$ なので、

```math
\frac{dF_\epsilon}{dx}
\approx
\frac1{E_\ell}.
```

両端近傍でのみ傾きと切片が変わる。したがって $E_*$ は零しきい値領域を境界層から離す一方、可視度を低下させる。

## C.11 順時間的共有浴と待ち時間の否定結果

記録形成後の4領域を $\Gamma_{AB}$ とし、共有浴を含む後段流れを $\Psi^t$ とする。Liouville 測度に関して

```math
\mu(\Psi^t\Gamma_{AB})
=
\int_{\Psi^t\Gamma_{AB}}d\Gamma
=
\int_{\Gamma_{AB}}
\left|
\det D\Psi^t
\right|
d\Gamma.
```

Hamiltonian 流れでは

```math
\det D\Psi^t=1
```

なので

```math
\mu(\Psi^t\Gamma_{AB})
=
\mu(\Gamma_{AB}).
```

したがって共通未来の浴結合は、順時間的集団の結果領域質量を変えない。終端条件づけを加えると

```math
\mu_R(\Gamma_{AB})
\propto
\int_{\Gamma_{AB}}
G_R(\Psi^T z)
d\mu(z)
```

となり、結果領域質量は変わり得る。しかし変化を生むのは浴雑音の漏れそのものではなく、共通未来の流れと $G_R$ を組み合わせた境界再重みづけである。

同じ結論は後段の待ち時間にも成り立つ。$n$ 番目の試行の結果を $\kappa_n$、有限完了時間を $\tau_n$ とする。全試行を結果に関係なく1回ずつ数えるなら、

```math
\frac1N
\sum_{n=1}^{N}
\mathbf1_{\{\kappa_n=(A,B)\}}
```

は $\tau_n$ に依存しない。待ち時間は時刻占有率を変えるが、試行番号で数えた結果頻度を変えない。結果に依存する未完了試行または時間切れ試行を除外したときだけ観測頻度が変わり、その場合は事後選別である。

## C.12 代数的整合性検査

実装の最小検査は次である。

1. 無作為な角と符号について、直接計算した $\|u_A-u_B\|^2/4$ と解析式 $I_-$ を比較する。
2. $S^3$ 上の等方 Gaussian ベクトルを規格化し、$J_s/J_\ell$ の経験累積分布と一様累積分布を比較する。
3. $Y_R$ を自由運動させた有限幅比較パルスを積分し、$I_-$ と $h$ の保存および $\Delta\Pi_R=\kappa I_- -h$ を検査する。
4. 終端半空間と相補時計の向き保存条件を検査する。
5. $h\leq E_*+\kappa I_-$ の指示関数を Monte Carlo 積分し、解析的な $W_{AB}$ と比較する。
6. 4つの結果を規格化し、一側周辺残差と CHSH 値を計算する。
7. $F_+(x)+F_-(x)=1$ を検査し、等重み向き平均で余弦項が消えることを確認する。
8. 追加の残余作用モードを加え、予測される $F_N(x)$ と高次調波を比較する。

これらは Hamiltonian 混合の証明ではない。幾何、規格化、標本化実装に循環または符号誤りがないことを確認する代数的検証である。
