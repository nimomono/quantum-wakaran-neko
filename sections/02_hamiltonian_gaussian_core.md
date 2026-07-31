@number: 2
@chapter: 本文
@title: 有限 Hamiltonian 部分と線形 Gauss 型確率表示
@status: 弱開放な現行モデル、閉鎖調和補助モデル、証明用の線形 Gauss 型確率表示を分離する。

## 2.1 現行モデルと有限2次補助モデル

現行モデルでは、観測対象と装置を含む有限 Hamiltonian 部分 $z$ を、外部自由度 $y$ と弱く結合する。

```math
H_{\rm all}(z,y)
=
H_{\rm fin}(z)
+
H_{\rm ext}(y)
+
\varepsilon_{\rm ext}H_{\rm link}(z,y)
+
H_{\rm work}.
```

$H_{\rm fin}$ だけのエネルギーを $E_{\rm fin}=H_{\rm fin}$ とすると、

```math
\dot E_{\rm fin}
=
\varepsilon_{\rm ext}
\{H_{\rm fin},H_{\rm link}\}
+
P_{\rm ctrl}
```

である。第1項は外部との流入または流出、第2項は仕事貯蔵系と自律時計からの制御仕事である。従って、有限 Hamiltonian 部分は現行モデルの中で厳密な保存系ではない。

第I部の厳密計算では、観測窓 $0\leq t\leq T$ における

```math
\varepsilon_{\rm open}
=
\frac{
\sup_{0\leq t\leq T}
\left|
E_{\rm fin}(t)-E_{\rm fin}(0)
\right|
}{
E_{\rm ref}
}
\ll1
```

を仮定し、$\varepsilon_{\rm ext}=0$ とした閉鎖有限系を補助モデルとして用いる。この補助モデルへの置換は、中心的な作用または記録領域が変わる交換時間 $\tau_{\rm exch}$ に対して $T/\tau_{\rm exch}\ll1$ のときに限る。

さらに、作用収束定理は一般の弱開放ミクロモデルを直接扱わず、線形化後の Gauss 型経路法則を対象とする。従って本章では、次の3層を混同しない。

1. 有限 Hamiltonian 部分を持つ弱開放な現行モデル。
2. 1試行内で用いる閉鎖有限系の補助モデル。
3. 第4章の証明に用いる線形 Gauss 型確率表示。

閉鎖補助モデルの位相空間を $\mathbb{R}^{2M}$、正準座標を $Z=(Q,P)$ とし、

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

の形にできる。初期正準変数が中心 Gauss 分布を持つなら、任意の線形観測量

```math
X_N(t)=L e^{tJG_N}Z(0)+\mu_N(t)
```

は有限次元 Gauss 型過程である。従って、閉鎖調和補助モデルの線形観測座標は、平均と2時刻共分散だけで完全に記述できる。

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

であり、$\xi_N$ は浴初期座標の線形結合である。浴初期分布が Gauss 分布なら $\xi_N$ も有限 Gauss 型過程になる。有限 $N$ では記憶核も雑音も再帰的であり、白色雑音や散逸は閉鎖補助モデルの基本法則ではない。

本論文の $C^1$ 定理は、この一般化 Langevin 方程式を任意の非線形 $V$ について直接扱うものではない。調和領域または線形化領域で観測される Gauss 型経路法則を、次節の有限 Fourier 表示で計算する。従って、閉鎖調和系は微視的な可逆性を検査する補助モデル、線形 Gauss 型表示は観測法則を計算する補助モデルである。

弱開放な現行モデルからこの表示へ進むには、少なくとも弱結合、線形化、外部相関時間と観測時間の分離を要する。この縮約の一様誤差評価は本論文では完了していない。

## 2.3 完全な有限 Fourier 浴

時間区間を $[0,T]$、$\omega_n=2\pi n/T$ とする。独立な標準 Gauss 型ベクトル $Z_0,A_n,B_n\in\mathbb{R}^d$ を用いて

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

## 2.4 証明用の線形 Gauss 型確率表示

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

である。従って $X_N$ は有限個の Gauss 変数の線形像であり、平均 $\mu_N$ と共分散 $C_N$ を有限和として厳密に計算できる。

この方程式は、有限 $N$ の平均と共分散を計算するための補助的な確率表示である。$\widetilde\eta_N$ 自体は有限 Hamiltonian 正規モードの初期振幅から作れるが、任意の時間依存係数 $F_\theta(t)$、$f_\theta(t)$ を含む上式全体が、1つの有限自律 Hamiltonian の観測座標として実現されることまでは示さない。

従って、第4章の定理が直接扱うのはこの線形 Gauss 型確率表示のクラスである。特定の有限 Hamiltonian モデルと平均・共分散が一致する場合には同じ作用計算を移せるが、一般の時間依存線形系に対する Hamiltonian 埋め込みを定理の結論へ含めない。この区別により、「有限 Hamiltonian 部分を持つ現行モデル」と「証明用確率表示の Hamiltonian 実現」を混同しない。

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

## 2.6 本章の結論

現行モデルは、有限 Hamiltonian 部分を持つ弱開放系である。閉鎖調和系は1試行内の可逆性、正準構造、再帰を検査する補助モデルであり、第4章の証明にはさらに線形 Gauss 型確率表示を用いる。

厳密に確立したのは、補助表示内部の平均、共分散、有限 Fourier 近似である。弱開放ミクロモデルから一般の線形表示を導くこと、白色雑音近似と Markov 近似の誤差を現行モデルの尺度で閉じることは未解決である。終端条件は浴そのものではなく Gauss 型条件づけとして導入する。次章では、その数学的条件づけと、物理的試行測度の選択を分けて記述する。第II部の構造化浴と境界作用殻は別の補助構成であり、本章の線形表示から導かない。
