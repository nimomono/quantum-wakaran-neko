@number: 2
@chapter: 本文
@title: 可逆な調和 Hamiltonian 中核と有限 Gaussian 確率表示
@status: 微視的可逆性と、証明に用いる補助的な線形 Gaussian 確率表示の範囲を分離する。

## 2.1 有限2次 Hamiltonian

位相空間を $\mathbb{R}^{2M}$、正準座標を $Z=(Q,P)$ とし、

```math
H_N(Z)=\frac12 Z^{\mathsf T}G_N Z,
\qquad
G_N=G_N^{\mathsf T}>0
```

を考える。運動方程式は

```math
\dot Z=JG_NZ,
\qquad
Z(t)=e^{tJG_N}Z(0)
```

である。$G_N$ が運動量に関して偶であれば、標準時間反転 $\Theta(Q,P)=(Q,-P)$ に対して

```math
\Theta e^{tJG_N}\Theta=e^{-tJG_N}
```

が成立する。従って全微視軌道は時間反転対称であり、Liouville 体積を保存する。

正準変換で正規モードへ移れば、安定な部分は

```math
H_N
=
\sum_{n=1}^{N}
\frac12
\left(
P_n^2+\omega_n^2Q_n^2
\right)
```

の形にできる。初期正準変数が中心 Gaussian 分布を持つなら、任意の線形観測量

```math
X_N(t)=L e^{tJG_N}Z(0)+\mu_N(t)
```

は有限次元 Gaussian 過程である。従って、閉じた調和 Hamiltonian 系の観測座標は、平均と2時刻共分散だけで完全に記述できる。

## 2.2 反作用を含む標準的な調和浴

粒子座標 $q$ と調和浴を明示する代表例は

```math
H_{\rm core}
=
\frac{p^2}{2m}+V(q)
+
\sum_{n=1}^{N}
\left[
\frac{P_n^2}{2m_n}
+
\frac{m_n\omega_n^2}{2}
\left(
Q_n-\frac{c_nq}{m_n\omega_n^2}
\right)^2
\right]
```

である [12--14]。平方完成された結合は反作用と周波数補正を同時に含む。浴変数を厳密に消去すると、粒子は有限記憶核を持つ一般化 Langevin 方程式に従う。

```math
m\ddot q(t)
+V'(q(t))
+\int_0^t\Gamma_N(t-s)\dot q(s)\,\mathrm{d} s
=
\xi_N(t)+F_{\rm slip}(t).
```

ここで

```math
\Gamma_N(t)
=
\sum_{n=1}^{N}
\frac{c_n^2}{m_n\omega_n^2}
\cos\omega_nt
```

であり、$\xi_N$ は浴初期座標の線形結合である。浴初期分布が Gaussian なら $\xi_N$ も有限 Gaussian 過程になる。有限 $N$ では記憶核も雑音も再帰的であり、白色雑音や散逸は微視的な基本法則ではない。

本論文の $C^1$ 定理は、この一般化 Langevin 方程式を任意の非線形 $V$ について直接扱うものではない。調和領域または線形化領域で観測される Gaussian 経路法則を、次節の有限 Fourier 表示で計算する。したがって、閉じた Hamiltonian 中核は微視的な可逆性を支え、線形 Gaussian 模型はその観測法則を計算する簡略表示である。

## 2.3 完全な有限 Fourier 浴

時間区間を $[0,T]$、$\omega_n=2\pi n/T$ とする。独立な標準 Gaussian ベクトル $Z_0,A_n,B_n\in\mathbb{R}^d$ を用いて

```math
\widetilde\eta_N(t)
=
\sqrt{\frac{2\nu}{T}}Z_0
+
\sqrt{\frac{4\nu}{T}}
\sum_{n=1}^{N}
\left[
A_n\cos\omega_nt
+B_n\sin\omega_nt
\right]
```

と定義する。この過程は調和正規モードの初期振幅を読み出すことで実現できる。零周波数 $Z_0$ は保存された正準運動量または自由モードに対応する。

共分散は

```math
\mathbb{E}\left[
\widetilde\eta_N^i(t)
\widetilde\eta_N^j(s)
\right]
=
2\nu\,\delta^{ij}\delta_{T,N}(t-s),
```

```math
\delta_{T,N}(\tau)
=
\frac1T
+
\frac2T
\sum_{n=1}^{N}\cos\omega_n\tau
```

である。$\delta_{T,N}$ は周期 Dirichlet 核であり、滑らかな試験関数に対して周期デルタ分布へ収束する。

零周波数を最初から除いた

```math
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]
```

を普遍的な浴共分散とみなしてはならない。これは全ての線形系に共通な浴ではなく、自由増分の全期間積分を零にする条件を課したときに現れる特殊な条件付き共分散である。一般の線形な流れでは、終端条件による共分散修正は流れと観測行列に依存する Schur 補完になる。

## 2.4 証明用の線形 Gaussian 確率表示

実際の証明では、観測座標の確率法則を

```math
\dot X_N(t)
=
F_\theta(t)X_N(t)
+f_\theta(t)
+\widetilde\eta_N(t),
\qquad
X_N(0)\sim N(m_{0,\theta},P_{0,\theta})
```

で表す。$\theta$ は質量、周波数、外力、終端記録などをまとめた有限次元パラメータである。$F_\theta$ と $f_\theta$ は時間について十分滑らかとする。

基本行列 $\Phi_\theta(t,s)$ を

```math
\partial_t\Phi_\theta(t,s)
=
F_\theta(t)\Phi_\theta(t,s),
\qquad
\Phi_\theta(s,s)=I
```

で定めると、

```math
X_N(t)
=
\Phi_\theta(t,0)X_N(0)
+\int_0^t
\Phi_\theta(t,s)
\left[
f_\theta(s)+\widetilde\eta_N(s)
\right]
\,\mathrm{d} s
```

である。従って $X_N$ は有限個の Gaussian 変数の線形像であり、平均 $\mu_N$ と共分散 $C_N$ を有限和として厳密に計算できる。

この方程式は、有限 $N$ の平均と共分散を計算するための補助的な確率表示である。$\widetilde\eta_N$ 自体は有限 Hamiltonian 正規モードの初期振幅から作れるが、任意の時間依存係数 $F_\theta(t)$、$f_\theta(t)$ を含む上式全体が、1つの有限自律 Hamiltonian の観測座標として実現されることまでは示さない。

したがって、第4章の定理が直接扱うのはこの線形 Gaussian 確率表示のクラスである。特定の有限 Hamiltonian 模型と平均・共分散が一致する場合には同じ作用計算を移せるが、一般の時間依存線形系に対する Hamiltonian 埋め込みを定理の結論へ含めない。この区別により、「有限 Hamiltonian 中核の存在」と「証明に用いる全確率表示の Hamiltonian 実現」を混同しない。

## 2.5 極限拡散

$N\to\infty$ で積分雑音

```math
W_N(t)=\int_0^t\widetilde\eta_N(s)\,\mathrm{d} s
```

は、有限次元分布で共分散 $2\nu\min(s,t)$ を持つ Wiener 増分へ近づく。本論文の作用とパラメータ第1微分は2時刻の平均・共分散だけで評価するため、一般の経路空間位相における弱収束は主定理の仮定にも結論にも用いない。対応する線形拡散表示は

```math
\,\mathrm{d} X(t)
=
\left[
F_\theta(t)X(t)+f_\theta(t)
\right]\,\mathrm{d} t
+\sqrt{2\nu}\,\,\mathrm{d} W_t
```

である。有限 $N$ の各経路は微分可能であるが、極限経路は微分不可能である。粗視化作用に現れる発散は、この正則性の変化に由来する。

## 2.6 OU 模型と Stratonovich 表現

$F=-\lambda I+\Omega J$ と選べば、2次元の回転を伴う OU 位相模型が得られる。これは減衰する位相振幅を扱う便利な具体例である。しかし OU の摩擦は縮約後の有効係数であり、微視的 Hamiltonian 中核そのものが時間反転を破ることを意味しない。本論文では OU 模型を基礎仮定とせず、付録Dの例として用いる。

雑音係数が状態に依存しないため、Itô 表現と Stratonovich 表現の変換補正は零である。従って、どちらの記法を選んでも本論文の線形 Gaussian 定理は変わらない。Stratonovich 微分は中心論証に必要ないため、以後は Itô 表現に統一する。

## 2.7 本章の結論

有限調和 Hamiltonian 系は、微視的可逆性と有限 Gaussian 経路法則を同時に与える。実際の証明には補助的な線形 Gaussian 確率表示を用いるが、その一般形を有限自律 Hamiltonian へ埋め込んだとは主張しない。白色拡散は有限モードの特異極限であり、終端条件は浴そのものではなく Gaussian 条件づけとして導入する。次章では、その条件づけを有限 $N$ と極限拡散の双方で記述する。
