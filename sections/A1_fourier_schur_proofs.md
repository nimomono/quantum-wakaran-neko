@number: A
@chapter: 付録
@title: Fourier--Gaussian 近似と Schur 補完の評価
@status: 第3章と第4章で用いた有限モード収束と条件づけの安定性を補足する。

## A.1 基本核の Fourier 係数

線形方程式の雑音応答核を

```math
G_\theta(t,s)
=
\mathbf 1_{0\leq s\leq t}
\Phi_\theta(t,s)
```

とする。$s=t$ に跳びがあるため、$s$ に関する Fourier 係数は一般に $O(n^{-1})$ である。

\begin{lemma}[一様 Fourier 尾部]
$F_\theta$ が第4.2節の仮定を満たすなら、ある $C_K$ が存在して

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|},
```

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|D_\theta\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|}
```

が成立する。従って共分散尾部は

```math
\sup_{\theta,s,t}
\left(
\|C_N(s,t)-C(s,t)\|
+\|D_\theta C_N(s,t)-D_\theta C(s,t)\|
\right)
\leq
\frac{C_KT^2}{N}
```

である。
\end{lemma}

\begin{proof}
$n\neq0$ に対して $e^{-i\omega_ns}$ を部分積分する。区間端と $s=t$ の跳びから $1/\omega_n$ の境界項が生じ、区間内部では $\partial_s\Phi(t,s)=-\Phi(t,s)F(s)$ が一様有界である。従って $|\widehat G_n|\leq C/|\omega_n|$ を得る。

$\theta$ 微分については

```math
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\dd r
```

を使う。$D\Phi$ とその $s$ 微分も一様有界なので同じ部分積分評価が成立する。共分散は Fourier 係数の積の和であり、

```math
\sum_{|n|>N}\frac1{n^2}\leq\frac{C}{N}
```

から結論を得る。
\end{proof}

## A.2 平均の収束

本論文では $F_\theta$、$f_\theta$、初期平均は $N$ に依存しないため、無条件平均は $\mu_N=\mu$ である。浴切断に依存する補正平均を許す場合でも、Fourier 尾部が中心化されていれば平均差は零であり、非零の決定論的尾部を加えた場合はその $L^1$ ノルムで直接評価できる。

条件付き平均は $C_N(t,T)$ と $C_N(T,T)$ に依存するため、共分散尾部から $O(1/N)$ の差を持つ。

## A.3 Schur 補完の安定性

$S_N=HC_N(T,T)H^{\mathsf T}+R$、$S=HC(T,T)H^{\mathsf T}+R$ とする。$R\geq r_*I$ なので

```math
\|S_N^{-1}\|\leq r_*^{-1},
\qquad
\|S^{-1}\|\leq r_*^{-1}.
```

逆行列恒等式

```math
S_N^{-1}-S^{-1}
=
S_N^{-1}(S-S_N)S^{-1}
```

から

```math
\|S_N^{-1}-S^{-1}\|
\leq
r_*^{-2}\|S_N-S\|
```

を得る。従って条件付き共分散について

```math
\sup_{s,t,\theta}
\|C_N^R(s,t)-C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

である。

第1微分では

```math
D(S^{-1})=-S^{-1}(DS)S^{-1}
```

を用いる。$S_N^{-1}$、$DS_N$ が一様有界なので、積の各因子を1つずつ差し替えることで

```math
\sup_{s,t,\theta}
\|D C_N^R(s,t)-D C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

を得る。条件付き平均も同様である。

## A.4 有限分解能の役割

$R>0$ は、観測値 $y$ の周囲に有限幅の終端領域を持たせる。これにより、条件付き共分散は $T$ で完全には消えず、条件付き流れの係数は閉区間 $[0,T]$ 上で有界に保たれる。

$R\downarrow0$ とすると、完全観測された方向の終端共分散は零へ近づく。自由拡散では前進条件付き流れに

```math
\frac{y-x}{T-t}
```

型の項が現れる。点終端での定理を得るには、$t=T$ の境界層を除いた区間で先に $N\to\infty$、$h\to0$ を取り、その後に境界層と $R\downarrow0$ を別に評価する必要がある。

## A.5 自由終端固定と零周波数

自由系では

```math
X_N(T)-X_N(0)
=
\int_0^T\widetilde\eta_N(t)\dd t
=
\sqrt{2\nu T}\,Z_0.
```

従って $X_N(T)=X_N(0)$ は $Z_0=0$ と同値である。非零モードは終端条件と独立なので、条件付き共分散から零モードの寄与 $2\nu/T$ だけが除かれる。この計算は、旧来の $-1/T$ が浴の基本性質ではなく、自由終端固定の結果であることを最も直接に示す。

## A.6 一般線形系では全モードが条件づけられる

$F\neq0$ では

```math
X_N(T)
=
\Phi(T,0)X_N(0)
+\sum_\alpha K_{N,\alpha}(T)\zeta_\alpha
+d_N(T)
```

である。ここで $d_N(T)$ は決定論項であり、一般に $K_{N,\alpha}(T)\neq0$ である。終端記録は零周波数だけでなく全ての Fourier 係数の線形結合を拘束する。そのため条件付き雑音共分散の修正は階数有限の Schur 項となり、流れ $F$、観測 $H$、分解能 $R$ に依存する。
