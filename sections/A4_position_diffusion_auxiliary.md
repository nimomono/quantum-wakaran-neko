@number: A4
@chapter: 本文
@title: 現行模型に採用しない運動量結合配置拡散経路
@status: 本付録は現行モデル M0 に採用しない補助理論である。有限運動量結合、正確な場消去、二側配置拡散内部の Fisher 構造を保存するが、位相接続による Schrödinger 型力学の導出には使わない。

## D.1 この経路を残す理由

配置拡散経路は、実在的な確率軌道を構成する別の研究候補として記録する。現行モデル M0 の構成要素ではなく、第2章から第3章の位相接続縮約、第4章の Born 型入口標本化、第5章の Bell 型履歴測度のいずれにも使用しない。従って、次の係数一致は現行理論の成立条件ではない。

```math
\nu_{\rm bath}
=
\frac{|\mathcal J_\phi|}{2m}
```

この等式は、将来2経路を同一の有効理論として統合する場合だけ必要な比較条件である。

第3章は coherent縮約多様体上で Schrödinger 型PDEを閉じるが、粒子が実在的な前進・後退 Markov 経路を持つことは示さない。本章の運動量結合経路は、有限 Hamiltonian 誘導場の速度揺らぎから、その確率過程へ進む候補を与える。

両経路は役割を分ける。

- 位相接続経路：作用と有効PDEを与える。
- 運動量結合経路：配置軌道の拡散極限を与える候補である。
- 係数一致と同時実現：独立した未解決問題である。

## D.2 運動量結合した有限誘導場

粒子正準対を $(X,P)$、誘導場正準対を $(Q,\Pi)$ とする。線形核を

```math
H_N^{\rm lin}
=
\frac12
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I_d & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}
+
V(X)
+
\frac12Q^{\mathsf T}K_NQ
```

とする。$M_N$ と $K_N$ は正定値実対称行列である。

<!-- theorem-start:proposition -->
**命題（運動量2次形式の成立条件）**
運動量2次形式が正定値であるための必要十分条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
左上ブロック $m^{-1}I_d$ は正定値である。ブロック行列の Schur 補条件を適用する。
<!-- theorem-end:proof -->

Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X),
```

```math
\dot Q
=
M_N^{-1}\Pi
+
C_N^{\mathsf T}P,
\qquad
\dot\Pi
=
-K_NQ.
```

従って配置速度は

```math
U_N
=
\frac Pm
+
Y_N,
\qquad
Y_N
=
C_N\Pi.
```

正準運動量 $P$ と機械的運動量 $m\dot X$ は一致しない。

## D.3 時間反転と配置流束

標準時間反転

```math
(P,\Pi)
\mapsto
(-P,-\Pi)
```

の下で運動量2次形式は不変である。$V$ と場ポテンシャルが座標だけに依存すれば、有限閉鎖核は時間反転対称である。

全 Liouville 密度を $F_N(X,P,Q,\Pi,t)$、配置周辺密度を

```math
\rho_N(x,t)
=
\int
F_N
\,dP\,dQ\,d\Pi
```

とする。Liouville 方程式を内部変数で積分すると、

```math
\partial_t\rho_N
+
\nabla\cdot
\left(
\rho_Nv_N
\right)
=
0,
```

```math
v_N
=
\mathbb E_N
\left[
\frac Pm+C_N\Pi
\mid
X=x
\right].
```

$P/m$ だけを配置速度としてはならない。

## D.4 線形誘導場の正確な消去

質量規格化した場座標で、正定値周波数行列を $\Omega_N$ とする。指定初期値問題の解を粒子運動量から独立な自由解と強制解へ分けると、

```math
Y_N(t)
=
Y_N^{\rm free}(t)
-
\int_0^t
C_N\Omega_N
\sin
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}P(s)
\,ds.
```

第1項は初期誘導場に由来する自由速度揺らぎ、第2項は粒子から場への反作用速度記憶である。

指定した Gauss 型初期集団で、場のエネルギー尺度を $\Theta_N$ とすると、

```math
R_N(t-s)
=
\mathbb E
\left[
Y_N^{\rm free}(t)
\otimes
Y_N^{\rm free}(s)
\right]
```

```math
=
\Theta_N
C_N
\cos
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}.
```

有限 $N$ では相関は余弦関数の有限和である。厳密な OU 相関や無限時間の Brown 運動ではない [12--14]。

二側境界条件を用いる場合、自己共役な境界値問題では Green 核が時間交換対称になる。しかし、自己共役 Green 核だけから Nelson の時間対称平均加速度は従わない。

## D.5 再帰前の Brown 極限

目標とする観測窓は

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}.
```

多数モード、短記憶、適切なスペクトル包絡、弱い外部交換の下で、

```math
\int_0^t
Y_N^{\rm free}(s)
\,ds
\Longrightarrow
\sqrt{2\nu_{\rm bath}}\,W_t
```

を示す必要がある。

反作用記憶項も同時に、

```math
\int_0^t
K_N(t-s)P(s)
\,ds
=
\delta m\,\dot X(t)
+
B_{\rm loc}(X_t,P_t)
+
\mathcal R_{\rm mem}(t)
```

のように、質量繰り込み、局所ドリフト、制御可能な残差へ分けなければならない。有限再帰、異方性、非 Gauss 性、外部交換を同じ上界で制御する定理は未完成である。

## D.6 位相空間極限と配置 Markov 閉鎖

最初の有効候補は

```math
dX_t
=
\frac{P_t}{m}\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t,
```

```math
dP_t
=
-\nabla V(X_t)\,dt
+
B_{\rm loc}(X_t,P_t)\,dt.
```

$(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。配置変数だけの前進・後退拡散

```math
dX_t
=
b_+(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^+,
```

```math
dX_t
=
b_-(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^-
```

を得るには、運動量緩和、条件付き速度分散、記憶残差を消去する追加の時間尺度分離が必要である。

## D.7 二側配置拡散内部の Fisher 構造

共通の正の密度 $\rho$ と共通の等方拡散係数 $\nu_{\rm bath}$ を持つ前進・後退 Markov 拡散が得られたとする。現在速度 $v$ と浸透速度 $u$ を

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
```

と定める。前後 Fokker--Planck 方程式の差から、

```math
u
=
\nu_{\rm bath}
\nabla\log\rho.
```

従って、

```math
\frac m2
\int
\rho|u|^2
\,dx
=
\frac{
m\nu_{\rm bath}^2
}{
2
}
\int
\frac{
|\nabla\rho|^2
}{
\rho
}
\,dx
```

である。量子ポテンシャルに対応する項は

```math
Q_{\rm bath}[\rho]
=
-2m\nu_{\rm bath}^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

これは二側 Markov 拡散を仮定した補助模型内部の厳密結果である。

## D.8 将来統合する場合の係数比較

第3章の作用係数は

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|.
```

本章の Fisher 係数が同じ量子ポテンシャルを与えるには、

```math
|\mathcal J_\phi|
=
2m\nu_{\rm bath}.
```

同値に、

```math
\nu_{\rm bath}
=
\frac{
|\mathcal J_\phi|
}{
2m
}.
```

この一致は、2経路を将来同じ有効理論として統合する場合の必要条件である。現行M0は配置拡散経路を採用しないため、現行理論の成立条件または反証条件ではない。補助模型を再採用する場合には、位相作用と浴拡散係数を独立に測り、上式が成立しなければ2経路は同じ有効理論を表さないと判定する。

## D.9 時間対称 Newton 則との関係

配置拡散と Fisher 項だけから

```math
ma_{\rm ts}
=
-\nabla V
```

は従わない。時間対称 Green 応答、反作用記憶、条件付き変分からこの Newton 則へ進む問題は未解決である。

一方、第3章では、位相接続縮約作用の変分から同値な Madelung 動力学を得た。後者は、前者の確率過程導出を代替しない。

## D.10 本章の結論

運動量結合した有限誘導場では、正定値条件、時間反転対称性、正確な配置流束、自由速度揺らぎと反作用記憶の分離を得る。二側配置 Markov 拡散が得られた後の浸透速度と Fisher 項も厳密である。

未解決なのは、有限誘導場からの Brown 極限、配置 $X$ だけの Markov 閉鎖、条件付き速度分散の抑制、時間対称 Newton 則、位相接続経路との係数一致と同時実現である。
