@number: G
@chapter: 付録
@title: 正常モード正準変換と局所包絡誤差
@status: 有限実振動子網の正常モード包絡、局所包絡との Bogoliubov 型変換、作用素誤差、有限時間誤差、局所作用変動を有限次元の行列関数として証明する。

## G.1 正常モード分解

第9章の剛性行列を

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

## G.2 厳密正準振幅

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

である。Hamiltonian は

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

## G.3 厳密回転包絡

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

## G.4 局所振幅との正準変換

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

## G.5 局所変換差の上界

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

## G.6 生成子の Taylor 上界

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

## G.7 Duhamel 評価

Hermitian 行列 $H_1,H_2$ に対し、

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

を得る。$H_1=h_{\rm ex}$、$H_2=h_L$ とすれば本文第9.7節の上界になる。

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

## G.8 局所作用変動

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

$\mathcal J_0$ を掛ければ本文第9.8節の局所作用上界を得る。

## G.9 規格化写像

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

を使えば、第9.9節の規格化状態誤差が従う。

## G.10 適用限界

本付録は有限次元、時間非依存、実対称 $h_L$ を扱う。$\eta<1$ は十分条件であり最適条件ではない。負の固有値を持つ $h_L$ も、全剛性が正定値であれば含む。

時間依存行列では各時刻の行列平方根が一般に可換でなく、正常モード基底の回転項が加わる。非線形結合では正常モード生成子自体が状態依存になる。これらへ本文の上界をそのまま適用しない。
