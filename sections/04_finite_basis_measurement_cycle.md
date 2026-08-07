@number: 4
@chapter: 本文
@title: 明示的な有限基底測定周期
@status: 固定純粋準備・固定有限基底では、作用読出し、唯一結果、条件付き測定後状態、内部記録、逆計算、無理数回転 Poincaré 写像を1本の自律 Hamiltonian 周期として構成する。理想離散結果は区分的に滑らかであり、滑らかな実装では境界近傍だけが近似になる。

## 4.1 一般作用区間公式

$L$ 個の位相担体モードを $b\in\mathbb C^L$ とする。測定する有限直交基底を $\{|u_k\rangle\}_{k=1}^L$ とし、これを標準基底へ移すユニタリ正準混合 $W$ を

```math
W|u_k\rangle
=
e_k
```

で定める。出力モードの作用と全位相作用は

```math
I_k
=
\mathcal J_0
\left|
\left(Wb\right)_k
\right|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^L I_k
```

である。累積作用を

```math
S_0=0,
\qquad
S_k
=
\sum_{j=1}^kI_j
```

とする。選択器角 $\vartheta\in[0,2\pi)$ から

```math
u
=
\frac{\vartheta}{2\pi}
I_{\rm ph}
```

を作り、$S_{k-1}\leq u<S_k$ を結果 $k$ とする。境界を除けば結果区間は互いに素で全区間を覆うため、各試行で結果は唯一である。

<!-- theorem-start:theorem -->
**定理（一般作用区間公式）**
選択器角が $(b,W,\mathcal P)$ の下で条件付き一様であり、比較失敗または記録失敗を結果依存に除外しないとする。このとき

```math
P(k\mid b,W)
=
\frac{I_k}{I_{\rm ph}}
```

であり、集団平均は

```math
P(k\mid W,\mathcal P)
=
\mathbb E
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
W,\mathcal P
\right]
```

となる。
<!-- theorem-end:theorem -->

この定理は階数1を要求しない。全作用が変動する場合、比の平均を平均の比へ置き換えてはならない。$r_k=I_k/I_{\rm ph}$ とすれば、

```math
P_k
-
\frac{\mathbb E[I_k]}{\mathbb E[I_{\rm ph}]}
=
-
\frac{
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
}{
\mathbb E[I_{\rm ph}]
}
```

である。固定全作用または無相関が、相関行列の対角比との一致条件になる。

## 4.2 固定作用と高階数相関行列

固定作用殻 $I_{\rm ph}=I_0>0$ 上の集団について

```math
C
=
\mathbb E
\left[
bb^\dagger
\middle|
\mathcal P
\right]
```

とする。調製集団が測定基底 $W$ に依存しなければ、一般作用区間公式から

```math
P(k\mid W,\mathcal P)
=
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
```

を得る。これは高階数の正半定値相関行列を含む。ただし、条件付き一様角を1本の軌道から作る力学と、高階数集団を同じ軌道上で生成する源力学は別問題である。

以下では、固定した純粋準備と固定基底に対象を絞る。この限定により、選択器角の Haar 測度と長期頻度を明示的な Poincaré 写像から導く。

## 4.3 固定純粋準備と必要自由度

準備状態を

```math
\chi\in\mathbb C^L,
\qquad
\chi^\dagger\chi=1
```

とし、全作用を $I_{\rm ph}=\mathcal J_0$ に固定する。信号 $b$ に加え、同じ $L$ モードのテンプレート $t$ を置く。周期開始時は

```math
b=e_1,
\qquad
t=e_1
```

とする。

作用読出し用に $L$ 個の正準対 $(Q_k,P_k)$、閾値用に $(Q_U,P_U)$、内部結果記録用に $(Q_M,P_M)$、選択器に $(\vartheta,J_{\rm sel})$、時計に $(\tau,P_\tau)$ を用いる。従って明示構成の正準対数は

```math
L+L+L+1+1+1+1
=
3L+4
```

である。これは最小数の主張ではない。直列累積比較なら作用レジスターを減らせる一方、二分木比較なら比較深さを減らす代わりに補助レジスターが増える。

## 4.4 準備、基底変換、作用読出し

任意の有限次元ユニタリ行列は Hermitian 生成子の指数として表せる。従って、互いに重ならない時計窓を使い、信号へ準備回路 $U_{\rm prep}$ と基底変換 $W$ を順に作用させられる。$U_{\rm prep}e_1=\chi$ なので、作用読出し直前には

```math
b
=
W\chi
```

となる。

作用読出し生成子を

```math
G_{\rm read}
=
\sum_{k=1}^L
P_kI_k
+
P_UI_{\rm ph}
f(\vartheta)
```

とする。理想模型では $f(\vartheta)=\vartheta/(2\pi)$ である。全レジスターを

```math
Q_k=P_k=Q_U=P_U=0
```

から始め、単位面積パルスを作用させると

```math
Q_k=I_k,
\qquad
Q_U
=
I_{\rm ph}f(\vartheta)
```

となる。共役運動量が零なので、理想入口では読出し中の信号と選択器への反作用は零である。

## 4.5 結果セクターとテンプレート

読出しレジスターから

```math
\xi_k
=
\mathbf1
\left[
\sum_{j=1}^{k-1}Q_j
\leq
Q_U
<
\sum_{j=1}^{k}Q_j
\right]
```

を定める。境界以外では $\xi_k\in\{0,1\}$ かつ $\sum_k\xi_k=1$ である。

$k>1$ に対し、$e_1$ と $e_k$ を回転する Hermitian 生成子を

```math
Y_{1k}
=
-i|1\rangle\langle k|
+
i|k\rangle\langle1|
```

とする。このとき

```math
\exp
\left(
-i\frac{\pi}{2}Y_{1k}
\right)e_1
=
e_k
```

である。条件付きテンプレート生成子を

```math
G_{\rm branch}
=
\frac{\pi\mathcal J_0}{2}
\sum_{k=2}^L
\xi_k
t^\dagger Y_{1k}t
+
P_M
\sum_{k=1}^L
k\xi_k
```

とする。単位面積パルス後に

```math
t=e_k,
\qquad
Q_M=k
```

となる。入口で $P_M=0$ であり、$t^\dagger Y_{1k}t=0$ は当該回転中に保存されるため、結果関数のレジスター依存性による共役運動量への反作用も理想不変集合では零である。

## 4.6 正準 SWAP と測定後状態

信号とテンプレートを交換する生成子を

```math
G_{\rm sw}
=
i
\left(
b^\dagger t
-
t^\dagger b
\right)
```

とする。 Hamiltonian $\pi\mathcal J_0G_{\rm sw}/2$ を単位面積だけ作用させると、

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

となる。 SWAP 直前は $b=W\chi$、$t=e_k$ なので、直後は

```math
b=e_k,
\qquad
t=-W\chi
```

である。信号だけに $W^\dagger$ を作用させれば、

```math
b_{\rm post}
=
W^\dagger e_k
=
|u_k\rangle
```

となる。測定前情報は消えず、テンプレートへ退避している。

<!-- theorem-start:theorem -->
**定理（条件付き測定後状態）**
固定純粋準備 $\chi$、固定基底 $\{|u_k\rangle\}$、理想結果セクターの下で、結果 $k$ の測定直後の信号相関行列は

```math
C_k^{\rm post}
=
|u_k\rangle
\langle u_k|
```

である。結果を無視した信号相関行列は

```math
C^{\rm post}
=
\sum_{k=1}^L
\left|
\langle u_k|\chi\rangle
\right|^2
|u_k\rangle
\langle u_k|
```

となる。
<!-- theorem-end:theorem -->

これは全系の非可逆な射影ではない。全系では正準 SWAP であり、信号部分だけを縮約すると非対角相関がテンプレートへ移ったように見える。

## 4.7 反復可能性の正確な範囲

結果 $k$ の直後に同じ基底変換を施すと

```math
Wb_{\rm post}
=
e_k,
```

```math
I_j
=
\mathcal J_0\delta_{jk}
```

となる。従って選択器角にかかわらず、累積区間は結果 $k$ を選ぶ。

ただし現在の装置のテンプレートには $-W\chi$ が保持されており、空状態ではない。従って厳密な主張は、測定直後の信号を新しい空テンプレートを持つ第2装置へ入れた場合に、同じ基底の結果が確率1で一致することである。同じ装置をその場で再使用するには、先に内部逆計算を完了するか、別の空テンプレートを用意する必要がある。

## 4.8 内部記録保持と逆計算

測定結果を読める保持窓では、

```math
b=|u_k\rangle,
\qquad
Q_M=k
```

を保つ。その後、次の順に逆操作する。

1. 信号へ $W$ を作用させる。
2. 逆 SWAP を作用させる。
3. 結果別テンプレート回転と内部記録を逆にする。
4. 作用・閾値読出しを逆にする。
5. 信号へ $W^\dagger$ を作用させる。
6. 準備回路 $U_{\rm prep}$ を逆にする。

順に追うと、逆 SWAP 後に $b=W\chi$、$t=e_k$、分岐逆計算後に $t=e_1$、$Q_M=0$、読出し逆計算後に $Q_k=Q_U=0$、最後に $b=e_1$ となる。理想不変集合では各共役運動量も零へ戻る。

この逆計算は内部記録を消去するのではなく、途中で作った情報を元の信号・選択器状態へ戻す操作である。周期を越えて永久保存する外部記録を同じ有限閉鎖系内で消し、全自由度を同じ点へ戻すことは要求しない。

## 4.9 1本の自律 Hamiltonian

時計を

```math
(\tau,P_\tau),
\qquad
\tau\in S^1,
\qquad
H_{\rm clk}=P_\tau
```

とする。$\dot\tau=1$ なので、互いに重ならない滑らかな時計窓 $g_r(\tau)$ と各生成子 $G_r$ を用いて

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_r
g_r(\tau)G_r
```

という1本の自律 Hamiltonian にまとめられる。時計窓の順序は、準備、$W$、読出し、分岐、 SWAP 、$W^\dagger$、保持、$W$、逆 SWAP 、逆分岐、逆読出し、$W^\dagger$、逆準備、選択器ドリフトである。

最後の生成子を

```math
G_{\rm drift}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

とする。各窓の生成子はその窓内で保存され、窓端で $g_r=0$ なので、時計運動量 $P_\tau$ も1周期後に準備値へ戻る。詳細な写像追跡は付録Cに示す。

## 4.10 Poincaré 写像と不変測度

Poincaré 断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内で、信号、テンプレート、全レジスター、全共役運動量、選択器作用、時計運動量を準備値へ固定した集合を $\mathcal T_{\chi,W}$ とする。自由変数は $\vartheta$ だけである。

<!-- theorem-start:theorem -->
**定理（固定有限基底周期の不変測度）**
$L<\infty$、$\chi^\dagger\chi=1$、固定基底変換 $W$、互いに重ならない単位面積時計窓、$\alpha\notin\mathbb Q$ を仮定する。理想比較境界を除く $\mathcal T_{\chi,W}$ 上で、 Poincaré 写像は

```math
\mathcal R_{\chi,W}:
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi}
```

であり、他の全内部変数を準備値へ戻す。従って

```math
d\mu_{\chi,W}^{\rm cyc}
=
\frac{d\vartheta}{2\pi}
\otimes
\delta_{\rm reset}
```

は不変であり、$\mathcal R_{\chi,W}$ はこの測度に関して一意エルゴード的である。
<!-- theorem-end:theorem -->

一意エルゴード性は付録Bで Fourier モードを用いて直接確認する。固定純粋準備と固定基底について、不変性とエルゴード性は仮定でなく計算結果である。

## 4.11 Born 型長期頻度

正規化重みと累積境界を

```math
p_k
=
\left|
\langle u_k|\chi\rangle
\right|^2,
\qquad
a_0=0,
\qquad
a_k
=
\sum_{j=1}^kp_j
```

とする。第 $n$ 試行の選択角は

```math
\vartheta_n
=
\vartheta_0+2\pi n\alpha
\pmod{2\pi}
```

であり、$a_{k-1}\leq\vartheta_n/(2\pi)<a_k$ のとき結果 $k$ になる。無理数回転の等分布性から

```math
\lim_{N\to\infty}
\frac{N_k(N)}{N}
=
a_k-a_{k-1}
=
\left|
\langle u_k|\chi\rangle
\right|^2
```

を得る。

無理数回転は混合的ではない。従って長期平均は Born 型重みに一致するが、結果列は独立同分布でなく、有限標本の分散を $Np_k(1-p_k)$ とする二項分布型揺らぎを一般には再現しない。有限標本統計を得るには、選択器写像を混合的なシンプレクティック写像へ強化する必要がある。

## 4.12 滑らかな有限幅模型

厳密な $\xi_k$ は不連続である。滑らかな有限時間 Hamiltonian 流は初期条件に連続なので、連結した初期領域を有限時間で厳密な離散基底状態だけへ写すことはできない。厳密2値化には、特異極限、分離面、無限時間極限、または粗視化が必要になる。

滑らかな比較関数を使い、各内部境界 $S_k$ の半幅 $w$ だけを遷移領域とする。選択変数が $[0,I_{\rm ph})$ 上で一様なので、内部境界近傍の和集合 $\mathcal B_w$ は

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\mathcal B_w
\right)
\leq
2(L-1)
\frac{w}{I_{\rm ph}}
```

を満たす。境界近傍が重なる場合、この和上界は過大評価になる。角の切断点を滑らかに接続する幅を $w_{\rm cut}$ とすれば、その誤差質量を別に加える。

遷移領域外では理想結果と条件付き測定後状態を保つ。遷移領域ではテンプレート回転角と記録が中間値になり、厳密な基底状態を失う。一方、前向き操作と同じ滑らかな関数を逆符号・逆順で作用させれば、遷移領域を含めて内部状態の逆計算は厳密であり、 Poincaré 写像の無理数回転部分は保たれる。

## 4.13 空間セル基底と主張の範囲

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、第2章の規格化から、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。ただし、これは位相担体の空間セル基底を標本化する式である。粒子座標がセル $i$ の局所検出器を作動させること、粒子と選択モードが同期すること、粒子が連続軌道を持つことは別の導出を要する。

本章で明示したものは、固定純粋準備・固定有限基底に対する内部測定周期、不変 Haar 測度、 Born 型長期頻度、条件付き測定後状態、内部記録、内部逆計算である。可変基底を含む単一のエルゴード周期、高階数源の軌道生成、混合的有限標本統計、永久外部記録、粒子検出、連続スペクトルは未解決である。
