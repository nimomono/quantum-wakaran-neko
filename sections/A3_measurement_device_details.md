@number: A3
@chapter: 付録
@title: 有限基底測定周期の完全正準構成
@status: 固定純粋準備・固定有限基底について、信号、テンプレート、レジスター、選択器、時計の全写像を追跡する。理想比較は区分的に滑らかであり、滑らかな比較では結果形成だけが近似になる。

## C.1 正準自由度

信号とテンプレートを

```math
b,t
\in
\mathbb C^L,
\qquad
b_j
=
\frac{Q_j^{b}+iP_j^{b}}{\sqrt{2\mathcal J_0}},
\qquad
t_j
=
\frac{Q_j^{t}+iP_j^{t}}{\sqrt{2\mathcal J_0}}
```

とする。作用レジスター、閾値、内部記録、選択器、時計は

```math
(Q_k,P_k)_{k=1}^L,
\quad
(Q_U,P_U),
\quad
(Q_M,P_M),
\quad
(\vartheta,J_{\rm sel}),
\quad
(\tau,P_\tau)
```

である。正準対数は $3L+4$ である。$L=2$ では9正準対になる。

周期開始値を

```math
b=t=e_1,
```

```math
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
```

```math
J_{\rm sel}=J_*>0,
\qquad
P_\tau=E
```

とする。選択器角 $\vartheta$ だけを自由にする。

## C.2 時計窓と自律化

$\tau\in S^1$ とし、

```math
H_{\rm clk}
=
P_\tau
```

と置く。各時計窓 $g_r(\tau)$ は滑らかで、支持が互いに交わらず、

```math
\int_0^1g_r(\tau)\,d\tau
=
1
```

とする。各窓で生成子 $G_r$ を作用させ、

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_{r=1}^{14}
g_r(\tau)G_r
```

とする。$\dot\tau=1$ なので、これは時間依存制御を正準時計で自律化した有限 Hamiltonian である。

## C.3 準備回路と測定基底

$U_{\rm prep}e_1=\chi$ を満たすユニタリ行列を選ぶ。 Hermitian 行列 $K_{\rm prep},K_W$ を

```math
U_{\rm prep}
=
e^{-iK_{\rm prep}},
\qquad
W
=
e^{-iK_W}
```

で選べる。複素正準 Hamiltonian

```math
G_1
=
\mathcal J_0
b^\dagger K_{\rm prep}b,
\qquad
G_2
=
\mathcal J_0
b^\dagger K_Wb
```

の単位面積流は、それぞれ $b\mapsto U_{\rm prep}b$、$b\mapsto Wb$ を生成する。第2窓後には

```math
b
=
W\chi
```

である。全位相作用は各ユニタリ正準写像で保存される。

## C.4 作用と閾値の読出し

読出し時のモード作用を

```math
I_k
=
\mathcal J_0|b_k|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^LI_k
=
\mathcal J_0
```

とする。理想角関数を $f(\vartheta)=\vartheta/(2\pi)$ とし、

```math
G_3
=
G_{\rm read}
=
\sum_{k=1}^L
P_kI_k
+
P_UI_{\rm ph}f(\vartheta)
```

と置く。Hamilton方程式は

```math
\dot Q_k=I_k,
\qquad
\dot Q_U=I_{\rm ph}f(\vartheta),
\qquad
\dot P_k=\dot P_U=0
```

を与える。$P_k=P_U=0$ なので、$b$ と $\vartheta$ の方程式へ入る読出し反作用は零である。従って第3窓後に

```math
Q_k=I_k,
\qquad
Q_U
=
I_{\rm ph}f(\vartheta)
```

となる。

## C.5 結果指示関数

レジスター座標から

```math
\xi_k(Q,Q_U)
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

を定める。境界を除いて

```math
\xi_k\in\{0,1\},
\qquad
\sum_{k=1}^L\xi_k=1
```

である。理想指示関数を含む $H_{\chi,W}^{\rm cyc}$ は比較境界で不連続な区分的 Hamiltonian である。境界は Haar 測度零なので、ほとんど全ての初期角で写像が一意に定まる。

## C.6 条件付きテンプレートと内部記録

$k>1$ に対し

```math
Y_{1k}
=
-i|1\rangle\langle k|
+
i|k\rangle\langle1|
```

とする。分岐生成子を

```math
G_4
=
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

とする。唯一の $\xi_k$ だけが1なので、

```math
t
\longmapsto
e_k,
\qquad
Q_M
\longmapsto
k
```

となる。

レジスター依存の $\xi_k$ は、一般には $P_j,P_U$ の方程式へ反作用を生む。しかし理想不変集合では、当該分岐中に

```math
t^\dagger Y_{1k}t=0,
\qquad
P_M=0
```

が保たれる。従って $\partial G_{\rm branch}/\partial Q_j$ と $\partial G_{\rm branch}/\partial Q_U$ に掛かる係数は零であり、$P_j=P_U=0$ のままである。

## C.7 正準 SWAP

SWAP 生成子を

```math
G_{\rm sw}
=
i
\left(
b^\dagger t-t^\dagger b
\right)
```

とする。第5窓の生成子を

```math
G_5
=
\frac{\pi\mathcal J_0}{2}
G_{\rm sw}
```

と置く。流れのパラメータを $s$ とすれば、

```math
\frac{db}{ds}
=
\frac{\pi}{2}t,
\qquad
\frac{dt}{ds}
=
-\frac{\pi}{2}b
```

である。$s=1$ で

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

となる。従って第5窓後は

```math
b=e_k,
\qquad
t=-W\chi
```

である。

## C.8 測定後基底と保持窓

第6窓で

```math
G_6
=
-\mathcal J_0
b^\dagger K_Wb
```

を作用させる。これは $W^\dagger$ を生成し、

```math
b
=
W^\dagger e_k
=
|u_k\rangle
```

となる。第7窓は相互作用を置かない保持窓とし、信号と内部記録を読める状態に保つ。

## C.9 逆計算

第8窓から第13窓を

```math
G_8
=
\mathcal J_0b^\dagger K_Wb,
```

```math
G_9
=
-\frac{\pi\mathcal J_0}{2}G_{\rm sw},
```

```math
G_{10}
=
-G_{\rm branch},
\qquad
G_{11}
=
-G_{\rm read},
```

```math
G_{12}
=
-\mathcal J_0b^\dagger K_Wb,
\qquad
G_{13}
=
-\mathcal J_0b^\dagger K_{\rm prep}b
```

とする。第8窓後に $b=e_k$、第9窓の逆 SWAP 後に $b=W\chi$、$t=e_k$ となる。第10窓後に $t=e_1$、$Q_M=0$、第11窓後に $Q_k=Q_U=0$ となる。第12窓後に $b=\chi$、第13窓後に $b=e_1$ となる。

逆分岐では、前向き分岐と同じレジスター値から同じ $\xi_k$ を計算する。逆読出しより先に逆分岐を行う必要がある。順序を入れ替えると結果指示関数を再現できない。

## C.10 選択器ドリフト

第14窓で

```math
G_{14}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

を作用させる。Hamilton方程式から

```math
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi},
\qquad
J_{\rm sel}
\longmapsto
J_{\rm sel}
```

となる。

## C.11 時計運動量の帰還

各単独窓では $H=P_\tau+g_r(\tau)G_r$ である。$G_r$ は自分自身が生成する流れに沿って保存されるので、

```math
\Delta P_\tau
=
-
\int
g_r'(\tau)G_r
\,d\tau
=
-G_r
\left[
g_r
\right]_{\rm in}^{\rm out}
=
0
```

である。窓は互いに重ならず、各窓端で $g_r=0$ なので、全周期後にも $P_\tau=E$ へ戻る。

## C.12 Poincaré 写像

断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内の不変集合を

```math
\mathcal T_{\chi,W}
=
\left\{
b=t=e_1,
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
J_{\rm sel}=J_*,
P_\tau=E
\right\}
```

とする。自由なのは $\vartheta$ だけである。C.3節からC.11節までの写像を合成すると、

```math
\mathcal R_{\chi,W}
\left(
\vartheta
\right)
=
\vartheta+2\pi\alpha
\pmod{2\pi}
```

であり、他の全変数は定義値へ戻る。従って $\mathcal T_{\chi,W}$ は不変である。

## C.13 2次元具体例

$L=2$、実準備状態

```math
\chi_a
=
\begin{pmatrix}
\cos a\\
\sin a
\end{pmatrix},
\qquad
0<a<\frac{\pi}{2}
```

を考える。標準基底測定では

```math
I_1
=
\mathcal J_0\cos^2a,
\qquad
I_2
=
\mathcal J_0\sin^2a
```

である。差

```math
D
=
Q_1-Q_U
=
\mathcal J_0
\left(
\cos^2a
-
\frac{\vartheta}{2\pi}
\right)
```

の符号が結果を定める。結果1の区間長は $\cos^2a$、結果2の区間長は $\sin^2a$ である。テンプレートの条件付き回転は2モード回転1個で足り、正準対数は9となる。

## C.14 滑らかな比較関数

各理想 $\xi_k$ を、境界から距離 $w$ 以上では0または1の平坦部を持つ滑らかな関数 $\xi_{k,w}$ へ置き換える。全生成子で同じ $\xi_{k,w}$ を使い、逆分岐に $-G_{\rm branch,w}$ を用いる。

遷移領域では複数の $\xi_{k,w}$ が中間値を取り得る。テンプレートは一般に基底ベクトルでなくなり、$Q_M$ も整数にならない。従って結果形成は近似である。一方、 Hamiltonian 流は滑らかで可逆であり、前向き写像の厳密な逆を逆順に作用させるので、内部状態は遷移領域を含めて準備値へ戻る。

理想角関数 $f(\vartheta)=\vartheta/(2\pi)$ も円周切断点で不連続である。切断点近傍だけを滑らかに接続し、結果誤差を比較境界誤差と分けて評価する。

## C.15 永久記録の限界

本周期の $Q_M$ は内部記録であり、第7窓後に逆計算される。保持窓で結果を別の外部記録へコピーすれば、その外部自由度は結果情報を保持する。 Hamiltonian 流の1対1性により、その外部記録まで結果に依存しない同一点へ戻すことはできない。

永久記録を伴う反復装置では、外部自由度を拡大するか、記録を循環履歴レジスターへ移すか、弱開放系として情報とエネルギーを外へ運ぶ必要がある。本付録の閉鎖内部周期は、その外部過程を構成しない。

## C.16 未導出事項

本付録の明示周期からは、次は導かれない。

1. 可変準備または可変基底を含む単一のエルゴード周期。
2. 高階数相関行列を1本の軌道から生成する源力学。
3. 混合性と二項分布型有限標本揺らぎ。
4. 同じ装置を内部逆計算前に再使用する反復測定。
5. 永久外部記録を含む閉鎖全系の完全帰還。
6. 滑らかな有限時間 Hamiltonian による厳密離散射影。
7. 位相担体結果と粒子局所検出の同一性。
