@number: E
@chapter: 付録
@title: M37正常モード変換と局所包絡誤差
@status: R86の正常モード変換と有限時間誤差に加え、R187の弱結合W型モード群、静的較正、有限切替、M54のW2正準状態の受け渡しを証明する。

## E.1 正常モード分解

第6章の剛性行列を

```math
K
=
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
```

とし、$K>0$ を仮定する。実直交行列 $O$ と正の固有周波数 $\omega_r$ により

```math
K
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1^2,\ldots,\omega_L^2
\right)
O
```

と書ける。行列平方根は

```math
\Omega
=
K^{1/2}
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1,\ldots,\omega_L
\right)
O
```

である。

正常座標を $x=Oq$、$\pi=Op$ とすれば、

```math
H_{\rm micro}
=
\sum_{r=1}^L
\left[
\frac{\pi_r^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_r^2x_r^2}{2}
\right]
```

となる。

## E.2 厳密正準振幅

行列表記で

```math
c
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}}\,
\Omega^{1/2}q
+
\frac{i}{\sqrt{M_{\rm osc}}}
\Omega^{-1/2}p
\right]
```

と定める。$\Omega$ は実対称正定値なので、

```math
\left\{c_r,c_s^*\right\}
=
-\frac{i}{\mathcal J_0}
\delta_{rs}
```

が成立する。従って $(c,c^*)$ は複素正準座標である。

逆変換は

```math
q
=
\sqrt{
\frac{\mathcal J_0}{2M_{\rm osc}}
}
\Omega^{-1/2}
\left(c+\overline c\right),
```

```math
p
=
-i
\sqrt{
\frac{M_{\rm osc}\mathcal J_0}{2}
}
\Omega^{1/2}
\left(c-\overline c\right)
```

である。ハミルトニアンは

```math
H_{\rm micro}
=
\mathcal J_0
c^\dagger\Omega c
```

となり、

```math
i\dot c
=
\Omega c
```

を得る。

## E.3 厳密回転包絡

搬送回転を除いた

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

を定めると、

```math
i\mathcal J_0
\dot{\widetilde b}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
\widetilde b
```

となる。従って

```math
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

である。また

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
=
\mathcal J_0c^\dagger c
```

は厳密保存量である。

## E.4 局所振幅との正準変換

局所振幅は

```math
a
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}\omega_0}\,q
+
\frac{i}{\sqrt{M_{\rm osc}\omega_0}}p
\right]
```

である。

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2},
\qquad
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

と置く。$q,p$ の表示を代入すると

```math
c
=
U_sa
+
V_s\overline a
```

を得る。$U_s^2-V_s^2=I$ なので逆変換は

```math
a
=
U_sc
-
V_s\overline c
```

である。回転包絡では

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)},
```

```math
b(t)
=
U_s\widetilde b(t)
-
V_se^{2i\omega_0t}
\overline{\widetilde b(t)}
```

となる。

## E.5 局所変換差の上界

$h_0=h_L$ なら

```math
s
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

である。$\eta=2\|h_L\|/(\mathcal J_0\omega_0)<1$ なので、$s$ の固有値は

```math
\left(1-\eta\right)^{1/4}
\leq
s_r
\leq
\left(1+\eta\right)^{1/4}
```

を満たす。

各正の実数 $s_r$ について

```math
\left|
\frac{s_r+s_r^{-1}}{2}-1
\right|
+
\left|
\frac{s_r-s_r^{-1}}{2}
\right|
=
\max
\left\{
s_r-1,
s_r^{-1}-1
\right\}
```

である。従って

$|\log s_r|$ が増えると上式の両項が同時に増え、許容区間では $s_r<1$ 側の最大偏差が $s_r>1$ 側の最大偏差以上である。このため $\|U_s-I\|$ と $\|V_s\|$ の上界を同じ端点で取ることができ、

```math
\left\|U_s-I\right\|
+
\left\|V_s\right\|
\leq
\left(1-\eta\right)^{-1/4}-1
=
\delta_{\rm loc}(\eta)
```

を得る。逆変換と $\|\overline v\|=\|v\|$ から

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}
\left\|\widetilde b(t)\right\|
```

である。$\|\widetilde b(t)\|$ は保存されるので本文の一様上界が従う。

## E.6 生成子の Taylor 上界

```math
X
=
\frac{2h_L}{\mathcal J_0\omega_0}
```

と置く。$h_L$ は実対称なので $X$ を直交対角化できる。各固有値 $x\in[-\eta,\eta]$ に対し Taylor の定理から

```math
\left|
\sqrt{1+x}-1-\frac{x}{2}
\right|
\leq
\frac{x^2}
{8\left(1-\eta\right)^{3/2}}
```

である。従って

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

となる。

## E.7 Duhamel 評価

エルミート 行列 $H_1,H_2$ に対し、

```math
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
=
-\frac{i}{\mathcal J_0}
\int_0^t
e^{-iH_1(t-s)/\mathcal J_0}
\left(H_1-H_2\right)
e^{-iH_2s/\mathcal J_0}
\,ds
```

である。両指数の作用素ノルムは1なので、

```math
\left\|
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
\right\|
\leq
\frac{t}{\mathcal J_0}
\left\|H_1-H_2\right\|
```

を得る。$H_1=h_{\rm ex}$、$H_2=h_L$ とすれば本文第6.7節の上界になる。

局所初期値 $b(0)$ を使う場合は、

```math
\begin{aligned}
\left\|b(t)-e^{-ih_Lt/\mathcal J_0}b(0)\right\|
\leq{}&
\left\|b(t)-\widetilde b(t)\right\|
\\
&+
\left\|
\widetilde b(t)
-e^{-ih_Lt/\mathcal J_0}\widetilde b(0)
\right\|
\\
&+
\left\|
e^{-ih_Lt/\mathcal J_0}
\left[
\widetilde b(0)-b(0)
\right]
\right\|
\end{aligned}
```

と分解し、両端の変換差と中央の生成子差を加える。

## E.8 局所作用変動

```math
e(t)
=
b(t)-\widetilde b(t)
```

と置くと、$\|e(t)\|\leq\delta_{\rm loc}\|\widetilde b(t)\|$ である。従って

```math
\begin{aligned}
\left|
\left\|b(t)\right\|^2
-
\left\|\widetilde b(t)\right\|^2
\right|
\leq{}&
2
\left\|\widetilde b(t)\right\|
\left\|e(t)\right\|
+
\left\|e(t)\right\|^2
\\
\leq{}&
\left(
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
\right)
\left\|\widetilde b(t)\right\|^2.
\end{aligned}
```

$\mathcal J_0$ を掛ければ本文第6.8節の局所作用上界を得る。

## E.9 規格化写像

非零ベクトル $x,y$ に対し、

```math
\left\|
\frac{x}{\left\|x\right\|}
-
\frac{y}{\left\|y\right\|}
\right\|
\leq
\frac{2\left\|x-y\right\|}
{\left\|y\right\|}
```

である。$x=b(T)$、$y=b_L(T)$ とし、

```math
\left\|b_L(T)\right\|
=
\left\|b(0)\right\|
\geq
\left(1-\delta_{\rm loc}\right)
\left\|\widetilde b(0)\right\|
```

を使えば、第6.9節の規格化状態誤差が従う。

## E.10 適用限界

本付録は有限次元、時間非依存、実対称 $h_L$ を扱う。$\eta<1$ は十分条件であり最適条件ではない。負の固有値を持つ $h_L$ も、全剛性が正定値であれば含む。

時間依存行列では各時刻の行列平方根が一般に可換でなく、正常モード基底の回転項が加わる。非線形結合では正常モード生成子自体が状態依存になる。これらへ本文の上界をそのまま適用しない。

## E.11 R86：局所回転包絡の厳密方程式の証明

<!-- theorem-start:proof -->
**証明**
規格化座標で ハミルトニアンは

```math
H_{\rm micro}
=
\frac{\omega_0}{2}
\left(P^{\mathsf T}P+Q^{\mathsf T}Q\right)
+
\frac{1}{2M_{\rm osc}\omega_0}
Q^{\mathsf T}AQ
```

となる。$Q=\sqrt{\mathcal J_0/2}(a+\overline a)$ を代入し、複素 Poisson 括弧を使うと

```math
i\mathcal J_0\dot a
=
\mathcal J_0\omega_0a
+
h_0
\left(a+\overline a\right)
```

を得る。$b=e^{i\omega_0t}a$ へ移れば結論が従う。
<!-- theorem-end:proof -->

## E.12 有限個の定傾斜区間の合成

区間の開始時刻を $t_r$ とする。R86の座標変換には $e^{2i\omega_0t_r}$ が入るが、ノルム上界は開始位相に依存しない。$k_r=(1-\eta_r)^{-1/4}$ とすると $\|\widetilde b(t_r)\|\leq k_r\|b(t_r)\|$。従って区間の実線形伝播を $S_r$、理想ユニタリ伝播を $U_r$ として

```math
\|(S_r-U_r)y\|\leq a_r\|y\|,\qquad
\|S_r\|\leq1+a_r
```

を全ての実初期座標yへ適用できる。ここで複素表示のノルムは実2L次元のユークリッドノルムであり、$S_r$ の複素線形性は仮定しない。

先行区間の相対誤差を $E_{r-1}$ とすると、同じ実状態を次区間へ渡す三角不等式は $E_r\leq(1+a_r)E_{r-1}+a_r$。$E_0=0$ から第6.17節の積上界を得る。途中で正常モードへ再準備する操作は含まない。局所作用と集団第2モーメントへの誤差伝播はR86とR135を参照し、同じ偏差を二重加算しない。

## E.13 滑らかな切替との比較

$Y=(Q,P)$ の実線形生成子を

```math
K_h(t)=\begin{pmatrix}0&\omega_0I\\
-\omega_0I-2h(t)/\mathcal J_0&0\end{pmatrix}
```

とする。区分一定の比較列を $\bar h$ とし、実伝播を $S_h,S_{\bar h}$ とする。対称部分の最大固有値は $\|h(t)\|/\mathcal J_0$ 以下なので、有限区間で

```math
\begin{aligned}
\|S_h(T,0)-S_{\bar h}(T,0)\|
&\leq D_{\rm ramp}(T),\\
D_{\rm ramp}(T)
&=\frac{2}{\mathcal J_0}
\exp\left(\frac1{\mathcal J_0}\int_0^T
\max\{\|h(t)\|,\|\bar h(t)\|\}\,dt\right)
\int_0^T\|h(t)-\bar h(t)\|\,dt .
\end{aligned}
```

これは実伝播のDuhamel公式と対数ノルム評価から従う。固定信号系の回転と正準規格化は同じなので、包絡相対誤差にも使える。滑らかな全W型の有効解を比較対象にする場合は、有効伝播間の差 $\mathcal J_0^{-1}\int\|h-\bar h\|dt$ も加える。

この指数上界は長時間に非常に粗くなり得る。有限切替幅を選べるという形式的事実だけから、現実的な制御帯域や多項式資源を結論しない。より鋭い駆動縮約、同時の高モード抑制、区間の安定性を別に検証する。


## E.14 弱結合W型族の低位モード群

左半井戸のHilbert空間を $\mathcal H_L$、右半井戸をその鏡映コピー $\mathcal H_R$ とする。$h_{\rm H}$ の規格化基底モードを $u_*$、固有値を $e_*$ とし、次固有値とのギャップを $g_*>0$ とする。中央端点ベクトルを $e_c$ とし

```math
a_*=\langle e_c,u_*\rangle\neq0
```

を仮定する。$\kappa=0$ の2重基底空間の基底を

```math
u_L=(u_*,0),
\qquad
u_R=(0,\mathcal Ru_*)
```

とする。中央結合作用素

```math
B
=
|e_L-e_R\rangle\langle e_L-e_R|
```

のこの2次元空間への圧縮は

```math
P_*BP_*
=
a_*^2
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
```

その固有値は $0$ と $2a_*^2$ で、固有ベクトルは偶・奇結合である。有限次元エルミート解析摂動論を孤立した2重固有値モード群へ適用すると、十分小さい $\kappa$ について最低2固有値は解析的に分岐し、

```math
E_0(\kappa)
=
e_*+O(\kappa^2),
\qquad
E_1(\kappa)
=
e_*+2a_*^2\kappa+O(\kappa^2).
```

従って

```math
J_\kappa
=
a_*^2\kappa+O(\kappa^2).
```

$\kappa=0$ の第3、第4固有値は半井戸の第1励起準位 $e_*+g_*$ にあるため、固有値の連続性から

```math
G_\kappa
=
E_2(\kappa)-E_1(\kappa)
=
g_*+O(\kappa).
```

特に $J_\kappa/G_\kappa\to0$ である。

鏡映に対して $\mathcal RX\mathcal R=-X$ とする。$\kappa\to0$ で偶奇モードは

```math
\phi_{0,\kappa}
\longrightarrow
\frac{\nu_L+\nu_R}{\sqrt2},
\qquad
\phi_{1,\kappa}
\longrightarrow
\frac{\nu_L-\nu_R}{\sqrt2}
```

と選べる。従って

```math
\langle\phi_{0,\kappa},X\phi_{1,\kappa}\rangle
\longrightarrow
\langle u_*,X_Lu_*\rangle.
```

右辺の絶対値を $\zeta_*>0$ と仮定したので、十分小さい $\kappa$ で $\zeta_\kappa\geq\zeta_*/2$ とできる。以上は有限局所ばね行列の固有値問題だけを使い、連続WKB分裂則を仮定しない。

## E.15 静的M37区間の長時間一様較正

時間独立な実対称 $h$ と $\eta=2\|h\|/(\mathcal J_0\omega_0)<1$ を取る。E.4の正準Bogoliubov変換を時刻 $t$ の局所包絡 $b(t)$ と厳密正常モード包絡 $\widetilde b(t)$ の間に使う。E.5から

```math
\|b(t)-\widetilde b(t)\|
\leq
\delta_{\rm loc}(\eta)\|\widetilde b(0)\|.
```

$t=0$ にも同じ式を使うと、$\delta_{\rm loc}<1$ の下で

```math
\|\widetilde b(0)\|
\leq
\frac{\|b(0)\|}{1-\delta_{\rm loc}}.
```

厳密正常モード伝播を

```math
U_{\rm ex}(t)
=
\exp\left[-\frac{i}{\mathcal J_0}f_{\omega_0}(h)t\right]
```

とする。$\widetilde b(t)=U_{\rm ex}(t)\widetilde b(0)$ とユニタリ性から

```math
\begin{aligned}
\|b(t)-U_{\rm ex}(t)b(0)\|
&\leq
\|b(t)-\widetilde b(t)\|
+
\|\widetilde b(0)-b(0)\|\\
&\leq
\frac{2\delta_{\rm loc}}{1-\delta_{\rm loc}}
\|b(0)\|.
\end{aligned}
```

これが本文の $\varepsilon_{\rm stat}$ である。重要なのは右辺が保持時間に依存しないことである。

$f_{\omega_0}$ は安定領域で単調増加し、$f_{\omega_0}(h)$ は $h$ の関数計算なので両者は固有射影を共有する。$h$ の孤立した2状態モード群の固有値を $\lambda_0<\lambda_1$ とすると、モード群内の回転軸は $h$ と $f(h)$ で同一で、射影型角速度だけが

```math
\frac{\lambda_1-\lambda_0}{\mathcal J_0}
\quad\longrightarrow\quad
\frac{f(\lambda_1)-f(\lambda_0)}{\mathcal J_0}
```

へ変わる。従って名目区間の射影型回転角を $\theta$ とすると、M37実区間を

```math
T_{\rm ex}
=
\frac{\mathcal J_0\theta}
{f(\lambda_1)-f(\lambda_0)}
```

だけ保持すれば、厳密正常モード群内では全体位相を除いて同じ回転角を得る。長いRabi時間にR86の全スペクトルDuhamel上界を掛ける必要はない。

## E.16 傾斜モード群、結合後の生成子と有限ゲート列

$P=P_\kappa$ を $h_\kappa$ の最低2状態射影、$Q=I-P$ とする。零傾斜モード群と残りのスペクトルの距離は $G_\kappa$ 以上である。摂動 $V_F=-FX$ に対して

```math
\rho_F
=
\frac{|F|\|X\|}{G_\kappa}
```

と置く。$\rho_F$ が十分小さければWeyl評価で最低2状態モード群は他のスペクトルから正距離を保ち、Riesz射影のレゾルベント積分またはDavis--Kahan評価から

```math
\|P_\kappa(F)-P\|
\leq
C_W\rho_F
```

を得る。$\kappa\to0$ で $G_\kappa\to g_*>0$、$\|X\|$ は固定なので、$C_W$ は十分小さい $\kappa$ に一様に取れる。

$P_\kappa(F)$ と $P$ の距離が1未満なら、極分解から恒等写像に近いユニタリ $W_F$ を選び

```math
W_FP W_F^\dagger=P_\kappa(F),
\qquad
\|W_F-I\|
\leq
C_W\rho_F
```

とできる。$W_F^\dagger h_\kappa(F)W_F$ はP--Q ブロック対角である。Feshbach展開の一次項は $Ph_\kappa(F)P$、Qを経由する項は2次以上なので

```math
\left\|
P W_F^\dagger h_\kappa(F)W_FP
-
P h_\kappa(F)P
\right\|
\leq
C_W
\frac{F^2\|X\|^2}{G_\kappa}.
```

偶奇基底から左右局在基底へ移ると、対称性により

```math
P h_\kappa(F)P
=
\overline E_\kappa I
-
J_\kappa\sigma_x
+
F\zeta_\kappa\sigma_z.
```

$F=F_\kappa=\sqrt{J_\kappa G_\kappa}/(2\zeta_\kappa)$ では $\rho_F=O(\sqrt{r_\kappa})$、結合後の ブロックの補正ノルムは $O(J_\kappa)$ である。傾斜区間の射影型角を固定すると保持時間は $O(\mathcal J_0/\sqrt{J_\kappa G_\kappa})$ なので、二次補正による角誤差は $O(\sqrt{r_\kappa})$ となる。切替時のモード群不一致も $\|P(F)-P\|=O(\sqrt{r_\kappa})$ である。

零傾斜の射影型回転軸は $x$ 軸、$F_\kappa$ の射影型回転軸は

```math
n_\kappa
\propto
\left(-J_\kappa,0,F_\kappa\zeta_\kappa\right)
```

であり、$n_\kappa\to z$。固定した任意の $U\in SU(2)$ について、$x$--$z$ Euler分解を非特異な有限語に選び、必要なら恒等的な追加回転を挿入して特異角を避ける。軸に関する連続性から、十分小さい $\kappa$ では $x$ と $n_\kappa$ の有限語で同じUを実現でき、区間数 $m_U$ と無次元回転角の総和を $\kappa$ に依存しない $C_U$ で抑えられる。

各傾斜区間を実際の全モード群で実行し、各切替で上の射影差を使う。有限個の三角不等式を合成すれば、厳密正常モード伝播とR140の理想2モード列の全状態差は

```math
\varepsilon_{\rm dress}
\leq
C_U\sqrt{r_\kappa}
```

となる。これは固定基底の $\int\|(I-P)h(F)P\|dt$ を使わないため、傾斜結合 $O(F)$ と保持時間 $O(F^{-1})$ の積が1程度になる粗い障害を回避する。

## E.17 局所M37伝播、有限切替とR187誤差

E.16の理想語を $m_U$ 個の静的M37区間として実行する。各区間ではE.15から局所包絡伝播と較正済み厳密正常モード伝播の作用素差を $\varepsilon_{\rm stat}(\eta)$ 以下にできる。各厳密正常モードの時間発展作用素はユニタリなので、区間ごとの実線形誤差を反復すると

```math
\varepsilon_{\rm car}^{(m_U)}
\leq
\left(1+\varepsilon_{\rm stat}(\eta)\right)^{m_U}-1.
```

初期モード投入誤差 $d_0$ とE.16の $\varepsilon_{\rm dress}$ を加えれば区分一定構成の主上界を得る。実際の傾斜値または保持角の較正誤差を射影型作用素ノルムで $\varepsilon_{\rm cal}$ と定義して別に加える。

跳躍時にはM37の $Q,P$ は連続であり、ハミルトニアン仕事だけが有限量変化する。跳躍列を滑らかにする場合、各跳躍時刻の幅 $\tau_j$ の小区間だけでE.13を使う。段階生成子 $\bar h$ と滑らかな生成子 $h$ の差がその区間外で零なら、局所ランプ誤差は

```math
D_j
\leq
\frac{2}{\mathcal J_0}
\exp\left[
\frac{\tau_j}{\mathcal J_0}
\max_{\rm ramp}\{\|h\|,\|\bar h\|\}
\right]
\int_{I_j}\|h(t)-\bar h(t)\|dt.
```

静的区間の安定な有限時間発展作用素と有限個のランプを合成し、全ランプ寄与を $\varepsilon_{\rm sw}$ とする。固定 $\kappa$、固定語では $\tau_j\downarrow0$ により任意に小さくできる。

さらに $H_\kappa=\sup_{|F|\leq F_\kappa}\|h_\kappa(F)\|$ が一様有界で、各ランプの振幅が $O(F_\kappa)$ のとき

```math
\tau_j
=
\frac{\mathcal J_0}{H_\kappa}r_\kappa^{1/4}
```

を選べば

```math
D_j
=
O\!\left(
\frac{|F_\kappa|\|X\|}{H_\kappa}
r_\kappa^{1/4}
\right)
=
O(r_\kappa^{3/4}).
```

これは断熱追随ではなく、小振幅クエンチを短い連続ランプで近似する評価である。

以上を合わせると

```math
\varepsilon_{187}
\leq
d_0
+C_U\sqrt{r_\kappa}
+\left(1+\varepsilon_{\rm stat}(\eta)\right)^{m_U}-1
+\varepsilon_{\rm sw}
+\varepsilon_{\rm cal}.
```

$\kappa\downarrow0$ で第2項を、$\omega_0\uparrow\infty$ で $\delta_{\rm loc}(\eta)$ と第3項を、ランプ幅と較正精度で残りを順に小さくできるので、任意の $\epsilon>0$ に対する有限構成が存在する。

零傾斜回転の時間は $O(\mathcal J_0/J_\kappa)$、傾斜回転は $O(\mathcal J_0/\sqrt{J_\kappa G_\kappa})$ なので有限語全体は

```math
T_U
\leq
C_U\frac{\mathcal J_0}{J_\kappa}
```

とできる。$J_\kappa=O(\kappa)$ なので精度を上げる族で時間は発散し得る。E.15の分裂較正を使うため、信号系 周波数へ長時間Duhamel誤差をそのまま移さないが、$\delta_{\rm loc}$ を目標精度へ下げる有限 $\omega_0$ と、長時間位相を保つ相対較正精度は必要である。

<!-- theorem-start:proof -->
**証明（R187）**

E.14で $r_\kappa\to0$ と $\zeta_\kappa\to\zeta_*>0$ を得る。E.16で $F_\kappa$ を選び、R140の任意の固定Uに対する有限語を結合後の全W型モード群へ $O(\sqrt{r_\kappa})$ で持ち上げる。各静的区間では関数計算 $f_{\omega_0}(h)$ が同じモード群固有ベクトルを保つため、E.15の分裂較正で射影型角を合わせる。局所M37包絡との差をE.15の時間一様上界で有限区間合成し、必要ならE.13を各短いランプだけへ適用する。初期接続端誤差と較正誤差を三角不等式で加えれば本文の上界を得る。各誤差項は順に有限パラメータで任意に小さくできる。証明終。
<!-- theorem-end:proof -->

## E.18 零傾斜正常モードとM54のW2正準接続端

$h_\kappa$ を実直交行列 $O_\kappa$ で対角化する。M37の全正準座標に同じOを作用させる

```math
Q'=O_\kappa^{\mathsf T}Q,
\qquad
P'=O_\kappa^{\mathsf T}P
```

は

```math
\sum_i dQ_i\wedge dP_i
=
\sum_i dQ'_i\wedge dP'_i
```

を保つので正準変換である。最低偶奇2モードに対応する先頭2正準対は全モード相空間の正準部分系をなす。左右局在座標はこの2対内の固定Hadamard変換であり、同じく正準である。

M54のW2静的状態構成の信号をこの2対と同定しても、高モードは残りの正準対として完全状態に保持される。従って「2モードを使う」ことは高モードを測定・廃棄・事後選別する操作ではない。

準備済み古典入力またはR112の正準SWAPをこの対へ接続するには、設計時に固定した線形正準接続端を用意すればよい。接続端が完全でない場合、その出力と所望低位モード初期状態の全状態差を $d_0$ に含める。接続端は入力係数、状態方向、共分散を実行時に読み取らず、規格化も行わない。

この同定はM37が初期状態方向の準備機構、作用殻、衝突浴、記録器を生成することを意味しない。R187の物理接続は信号系とQ1制御までで閉じ、測定・準備の単一装置統合はM0より弱い未解決課題として残す。
