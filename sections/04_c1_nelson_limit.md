@number: 4
@chapter: 本文
@title: 繰り込み済み粗視化作用形式の Nelson 極限
@status: 線形 Gaussian・有限分解能・2次ポテンシャルの範囲で、定義した作用形式の定量的 $C^1$ 収束を示す。

## 4.1 粗視化作用

有限 $N$ の経路は微分可能であるが、$N\to\infty$ の拡散経路は微分不可能である。そのため、単純な運動エネルギー

$$
\frac m2\int_0^T|\dot X_N(t)|^2\dd t
$$

は極限で発散する。時間分解能 $h>0$ を固定し、有限差分

$$
D_hX_N(t)=\frac{X_N(t+h)-X_N(t)}{h}
$$

を用いる。拡散係数が $\nu$、空間次元が $d$ なら、雑音の普遍的発散は

$$
\frac m2\E|D_hX|^2
\sim
\frac{md\nu}{h}
$$

である。

差分商の運動項から軌道に依存しない発散定数を除き、有限な Guerra--Morato 項を残す原理自体は既知である [3,4]。本章の新規な主張は、有限 Fourier 切断、有限分解能の終端記録、滑らかな有限次元パラメータ族を同時に扱い、作用値とその第1偏微分へ共通の明示誤差評価を与える点にある。

ここで扱う粗視化作用は、有限 Hamiltonian 軌道の統計から定義する評価汎関数である。Hamilton 方程式そのものから、この汎関数を最小化または停留化する選択則が生じるとは仮定しない。本章の結論は作用形式の収束であり、有効運動方程式の動力学的選択まで含まない。

外部ポテンシャルを $U_\theta(x,t)$ と書き、条件付き経路法則に対する繰り込み済み作用を

$$
\mathcal A_{N,h}^{R,U}(\theta)
=
\E_{N,\theta}^{R}
\int_0^{T-h}
\left[
\frac m{2h^2}
|X_N(t+h)-X_N(t)|^2
-\frac{md\nu}{h}
-U_\theta(X_N(t),t)
\right]\dd t
$$

と定義する。差し引く項は結果や設定に依存せず、有限差分の Gaussian 自己揺らぎだけを除く。

## 4.2 許容するパラメータ族

パラメータ集合 $K\subset\R^p$ をコンパクトとする。次を仮定する。

1. $F_\theta(t)$、$f_\theta(t)$ は $(\theta,t)$ について $C^2$ であり、$K\times[0,T]$ 上で2階まで一様有界である。
2. 初期平均 $m_{0,\theta}$ と初期共分散 $P_{0,\theta}$ は $C^2$ で、$P_{0,\theta}\geq p_*I>0$ である。
3. 終端観測 $H_\theta$、$y_\theta$、$R_\theta$ は $C^2$ で、$R_\theta\geq r_*I>0$ である。
4. 外部ポテンシャルは

$$
U_\theta(x,t)
=
\frac12x^{\mathsf T}K_\theta(t)x
+\ell_\theta(t)^{\mathsf T}x
+c_\theta(t)
$$

の形で、係数は $C^2$ かつ一様有界である。
5. Fourier 切断数 $N$ と粗視化幅 $h=h_N$ は

$$
h_N\longrightarrow0,
\qquad
N\left(\frac{h_N}{T}\right)^2\longrightarrow\infty
$$

を満たす。

$C^1(K)$ は作用値と $\theta$ に関する全ての第1偏微分の一様ノルムを表す。この定理は、任意の非線形な経路変分についての無限次元 $C^1$ 定理ではなく、指定した線形 Gaussian パラメータ族上の定理である。

## 4.3 極限作用

極限の条件付き拡散の前進流れを $b_{+,\theta}^R$、時刻密度を $\rho_\theta^R$ とする。Guerra--Morato 型作用を

$$
\mathcal A_{\GM}^{R,U}(\theta)
=
\int_0^T\int_{\R^d}
\rho_\theta^R(x,t)
\left[
\frac m2|b_{+,\theta}^R(x,t)|^2
+m\nu\nabla\cdot b_{+,\theta}^R(x,t)
-U_\theta(x,t)
\right]
\dd x\dd t
$$

と定義する [4]。線形 Gaussian 系では $b_+^R$ は $x$ の1次式、$\rho^R$ は正の Gaussian 密度なので、全ての積分は有限である。

## 4.4 線形 Gaussian $C^1$ 収束定理

\begin{theorem}[線形 Gaussian $C^1$ 極限]
第4.2節の仮定を満たすとする。ある定数 $C_K<\infty$ が存在し、十分大きい $N$ と $0<h<T/4$ に対して

$$
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT
+
\frac{T^2}{Nh^2}
\right)
$$

が成立する。従って $h_N\to0$ かつ $N(h_N/T)^2\to\infty$ なら、次の収束が $C^1(K)$ で成り立つ。

$$
\mathcal A_{N,h_N}^{R,U}
\longrightarrow
\mathcal A_{\GM}^{R,U}.
$$

特に $h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。
\end{theorem}

この $N^{-1/3}$ は、共分散尾部を $O(N^{-1})$ と評価し、増分商の $h^{-2}$ と釣り合わせた現在の証明から得られる率である。下界または最適性は示していない。より滑らかな核、端点適合基底、相殺を用いれば改善される可能性があり、本質的な普遍指数とは主張しない。

証明の中心は、Fourier 切断による共分散誤差 $O(T^2/N)$ と、時間対角展開による粗視化誤差 $O(h/T)$ を分離することである。増分商には $h^{-2}$ が掛かるため、前者は作用上で $O(T^2/(Nh^2))$ になる。有限分解能記録による Schur 補完の安定性と、パラメータ第1微分を含む全評価は付録Bに示す。

## 4.5 Guerra--Morato 表示と Nelson 表示

前進・後退流れから

$$
v^R=\frac{b_+^R+b_-^R}{2},
\qquad
u^R=\frac{b_+^R-b_-^R}{2}
=\nu\nabla\log\rho^R
$$

を定義する。境界項が消える条件、例えば全空間での Gaussian 減衰、周期境界、または無流束境界を仮定する。

\begin{theorem}[Guerra--Morato 作用と Nelson 作用の一致]

$$
\mathcal A_{\GM}^{R,U}
=
\mathcal A_{\Nel}^{R,U},
$$

$$
\mathcal A_{\Nel}^{R,U}
=
\int_0^T\int_{\R^d}
\rho^R
\left[
\frac m2|v^R|^2
-\frac m2|u^R|^2
-U
\right]
\dd x\dd t.
$$
\end{theorem}

\begin{proof}
$b_+^R=v^R+u^R$ と $\nu\nabla\rho^R=\rho^Ru^R$ を用いる。空間部分積分により

$$
\int\rho^R m\nu\nabla\cdot b_+^R\dd x
=
-m\int\rho^R b_+^R\cdot u^R\dd x.
$$

従って

$$
\frac m2|b_+^R|^2
-m b_+^R\cdot u^R
=
\frac m2|v^R|^2
-\frac m2|u^R|^2.
$$

ポテンシャル項は共通なので結論を得る。
\end{proof}

この一致は近似ではない。$C^1$ 極限で得られた Guerra--Morato 作用は、正の Gaussian 密度領域では Nelson 作用そのものである [3--6]。Guerra--Morato 作用の臨界点と第2変分を扱う近年の研究もあるが [35]、本定理が扱う有限 Fourier 条件付き族の2尺度 $C^1$ 収束とは問題設定が異なる。

## 4.6 停留点について言えること

\begin{corollary}[収束する停留点]
$\theta_N\in\operatorname{int}K$ が

$$
D_\theta\mathcal A_{N,h_N}^{R,U}(\theta_N)=0,
\qquad
\theta_N\longrightarrow\theta_*
$$

を満たすなら、

$$
D_\theta\mathcal A_{\Nel}^{R,U}(\theta_*)=0
$$

である。
\end{corollary}

\begin{proof}
$C^1(K)$ 収束と $D\mathcal A_{N,h_N}(\theta_N)=0$ から

$$
\|D\mathcal A_{\Nel}(\theta_*)\|
\leq
\|D\mathcal A_{\Nel}(\theta_*)-D\mathcal A_{\Nel}(\theta_N)\|
+
\|D\mathcal A_{\Nel}(\theta_N)-D\mathcal A_{N,h_N}(\theta_N)\|
\longrightarrow0.
$$
\end{proof}

これは一方向の条件付き主張である。まず有限模型のパラメータ停留点列が存在し、その列が収束する場合に限って、極限点が Nelson 作用の停留点になる。任意の Nelson 停留点を有限浴の停留点列で近似するには、Hessian の非退化性と少なくとも局所 $C^2$ 収束が必要である。さらに、微視的 Hamiltonian 方程式が粗視化作用の停留点を力学的に選ぶことは、この系から従わない。

## 4.7 調和 Gaussian の物理像

1次元で

$$
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma(t)}
\exp\left[
-\frac{(x-q(t))^2}{2\sigma(t)^2}
\right]
$$

とし、連続の式を満たす速度を

$$
v(x,t)
=
\dot q(t)
+\frac{\dot\sigma(t)}{\sigma(t)}[x-q(t)]
$$

とする。浸透速度は

$$
u(x,t)
=
-\nu\frac{x-q(t)}{\sigma(t)^2}
$$

である。調和ポテンシャル $U=m\Omega^2x^2/2$ に対する Nelson 作用は

$$
\mathcal A_G[q,\sigma]
=
\frac m2
\int_0^T
\left[
\dot q^2+\dot\sigma^2
-\frac{\nu^2}{\sigma^2}
-\Omega^2(q^2+\sigma^2)
\right]\dd t.
$$

変分すると

$$
\ddot q+\Omega^2q=0,
$$

$$
\ddot\sigma+\Omega^2\sigma
-\frac{\nu^2}{\sigma^3}=0
$$

を得る。中心は古典的な調和運動を行い、幅は通常の拡散で単調に広がるのではなく、調和閉じ込めと密度勾配の項の釣り合いで振動する。定常幅は

$$
\sigma_*^2=\frac\nu\Omega
$$

である。これは Nelson 作用が、単なる熱拡散ではなく、確率流と密度勾配の前後対称な変分力学を表すことを示す。

## 4.8 定理の範囲

本章で証明したのは、線形 Gaussian 範囲における作用形式の $C^1$ 極限である。次は主定理に含まれない。

- 状態依存の非線形な流れ。
- 退化した点終端 $R=0$。
- 硬いしきい値条件による非滑らかな経路選択。
- 2次を超える一般ポテンシャルに対する一様第1変分評価。
- 密度の節を横切る大域位相。
- 全ての Nelson 変分を尽くす無限次元 $C^1$ 収束。
- 微視的 Hamiltonian 運動による粗視化作用の停留点選択。
- 一般の時間依存線形 Gaussian 表示を有限自律 Hamiltonian へ埋め込む定理。

したがって本章の結果を「Nelson 有効力学の動力学的出現」とは呼ばない。確立した内容は、明示した確率表示と粗視化規則に対する作用形式の収束である。
