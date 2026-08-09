@number: 4
@chapter: 本文
@title: 滑らかな局所有限基底測定周期
@status: 固定純粋準備・固定有限基底・有限次元について、局所位相回転、隣接2モード交換、滑らかな累積比較、無反応結果、条件付き測定後状態、内部記録、逆計算、無理数回転 Poincaré 写像を1本の有限自律 Hamiltonian 周期として構成する。Born 型長期頻度は任意精度で得られる。Q1の位置ばね網、局所時計配線、永久記録、弱開放 reset を同じ完全装置へ統合することは未完成である。

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

この定理は階数1を要求しない。固定作用下の高階数公式、全作用変動の共分散補正、相関行列との関係は付録Bにまとめる。本章の自律周期定理は、1本の軌道上の固定純粋準備に限定する。

## 4.2 固定純粋準備と必要自由度

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

である。作用レジスターのうち $Q_1,\ldots,Q_{L-1}$ は、読出し後に累積比較ポインターとして再利用する。これは最小数の主張ではない。

## 4.3 Q1包絡から Born 型分布への誤差伝播

第3章のミクロ局所包絡を測定時刻 $T$ で規格化し、

```math
\widehat b_{\rm mic}(T)
=
\frac{b(T)}{\left\|b(T)\right\|}
```

とする。目標有効状態を

```math
\chi_L(T)
=
\frac{b_L(T)}{\left\|b_L(T)\right\|}
```

とする。任意の有限基底変換 $W$ に対し、実際の作用比と目標 Born 型重みを

```math
p_k^{\rm mic}
=
\left|
\left(W\widehat b_{\rm mic}\right)_k
\right|^2,
\qquad
p_k^L
=
\left|
\left(W\chi_L\right)_k
\right|^2
```

と定める。

<!-- theorem-start:proposition -->
**命題（包絡方向誤差から測定分布誤差への伝播）**
任意のユニタリ $W$ について、全変動距離は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\left\langle
\widehat b_{\rm mic},
\chi_L
\right\rangle
\right|^2
}
\leq
\left\|
\widehat b_{\rm mic}-\chi_L
\right\|
```

を満たす。
<!-- theorem-end:proposition -->

最初の不等式は純粋状態間の距離が任意の射影成分分布の全変動距離を上から抑えること、2番目は単位ベクトルのノルム評価から従う。ここでは量子測定を仮定していない。左辺は古典作用比を同じ基底 $W$ で比較した量である。

第3章の有限時間上界と $\delta_{\rm loc}<1$ を使うと、

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\varepsilon_{\rm dist}(T),
```

```math
\varepsilon_{\rm dist}(T)
=
\min
\left\{
1,
\frac{
2\varepsilon_{\rm car}(T)
}{
1-\delta_{\rm loc}(\eta)
}
\right\}
```

を得る。$\varepsilon_{\rm dist}$ は包絡方向のずれが測定分布へ伝わる誤差であり、環境誤差ではない。

本章の自律周期は $I_{\rm ph}=\mathcal J_0$ の固定準備を使う。Q1から直接渡す単発入力で全局所作用が変動する場合は、測定時点の実際の $I_{\rm ph}(T)$ を読み、閾値も同じ値で規格化する必要がある。この受渡しを同じ局所反復装置へ組み込む問題はQ10に残す。

## 4.4 任意有限基底の局所正準回路

信号モードの実正準座標を $(Q_j^b,P_j^b)$ とする。単一モード位相回転と隣接2モード交換の生成子を

```math
G_{Z,j}
=
\frac{
\left(Q_j^b\right)^2
+
\left(P_j^b\right)^2
}{2},
```

```math
G_{X,j}
=
Q_j^bQ_{j+1}^b
+
P_j^bP_{j+1}^b
```

とする。複素振幅では $G_{Z,j}=\mathcal J_0|b_j|^2$、$G_{X,j}=\mathcal J_0(b_j^*b_{j+1}+b_{j+1}^*b_j)$ である。両者の流れは全作用を厳密に保存する。

$G_{Z,j}-G_{Z,j+1}$ と $G_{X,j}$ の交換子方向は、隣接モード間の虚交換生成子を与える。従って局所位相回転と実交換の有限列で任意の隣接 $U(2)$ 変換を作れる。

任意の $W\in U(L)$ には、隣接する2行だけに作用する Givens 変換を順に左から掛ける消去法を適用できる。下三角成分を下から消去すると、

```math
N_W
\leq
\frac{L(L-1)}2
```

個の隣接2モード変換と最後の対角位相へ分解できる [38,39]。固定状態だけを準備する $U_{\rm prep}e_1=\chi$ は $L-1$ 個以下の隣接2モード変換で足りる。逆変換は順序を逆にし、各回転角を反転すれば厳密に得られる。

この回路は、1次元鎖の $L-1$ 本の交換辺を時計順に再利用する。密な $W$ の情報は非局所結合本数ではなく、$O(L^2)$ 個の時計窓と回転角に保存される。互いに重ならない辺を並列化する Clements 型配置では、基底変換の直列深さを $O(L)$ に整理できる [39]。

ただし $G_{X,j}$ は位置間結合だけでなく運動量間結合を含む。これは明示的な有限古典 Hamiltonian だが、Q1の通常の位置ばね網と同じハードウェアではない。位置ばねだけに限定すると反回転項を伴う近似になるため、本章では採用しない。

## 4.5 作用読出しと累積比較ポインター

局所回路により $b=W\chi$ を作った後、各モード作用を

```math
I_k
=
\mathcal J_0|b_k|^2
```

とする。固定準備では $\sum_kI_k=\mathcal J_0$ である。読出し生成子を

```math
G_{\rm read}
=
\sum_{k=1}^L P_kI_k
+
P_U\mathcal J_0f(\vartheta)
```

とする。角の切断近傍を除き $f(\vartheta)=\vartheta/(2\pi)$ とする。全レジスター運動量を0から始めると、単位面積流の後に

```math
Q_k=I_k,
\qquad
Q_U=u
```

となり、入口信号と選択器への読出し反作用は零である。$P_UI_{\rm ph}f(\vartheta)$ を使わず、既知の $\mathcal J_0$ を使うため、固定準備周期では閾値レジスターを全信号モードへ結合しない。

次に局所剪断を

```math
G_{0}^{\rm cum}
=
-P_1Q_U,
```

```math
G_j^{\rm cum}
=
P_{j+1}Q_j,
\qquad
j=1,\ldots,L-2
```

の順に作用させる。すると

```math
Q_j
=
S_j-u
=:
d_j,
\qquad
j=1,\ldots,L-1
```

となる。作用が非負なので

```math
d_1
\leq
d_2
\leq
\cdots
\leq
d_{L-1}
```

である。入口で共役運動量が0なので、剪断は読出した値を壊さない。

有限保持窓の比較余裕を作るため、

```math
G_{\rm amp}
=
\Lambda
\sum_{j=1}^{L-1}Q_jP_j
```

を作用させる。流れは

```math
Q_j
\longmapsto
e^\Lambda d_j,
\qquad
P_j
\longmapsto
e^{-\Lambda}P_j
```

であり、符号と正準性を保存する。これは吸引的なラッチではなく、有限時間の双曲型増幅である。

## 4.6 滑らかな比較と完全結果集合

平坦部を持つ滑らかな段差関数を

```math
\rho(z)
=
\begin{cases}
0,&z\leq0,\\
e^{-1/z},&z>0,
\end{cases}
```

```math
\sigma(z)
=
\frac{
\rho(z+1)
}{
\rho(z+1)+\rho(1-z)
}
```

と定める。出力比較幅を $X>0$ とし、

```math
h_j
=
\sigma
\left(
\frac{Q_j}{X}
\right),
\qquad
h_0=0,
\qquad
h_L=1
```

とする。$Q_j$ の単調性から

```math
0
\leq
h_1
\leq
\cdots
\leq
h_{L-1}
\leq
1
```

となる。差

```math
c_k
=
h_k-h_{k-1}
```

は $c_k\geq0$、$\sum_kc_k=1$ を満たす。ただし遷移領域の $c_k$ を実結果または追加確率と解釈しない。

角の切断点を滑らかに接続する領域を $\mathcal C_{\rm cut}$ とする。結果 $k$ の安全セクターを

```math
\mathcal O_k
=
\left\{
\vartheta\notin\mathcal C_{\rm cut},
\qquad
Q_j\leq-X\quad(j<k),
\qquad
Q_j\geq X\quad(j\geq k)
\right\}
```

とする。各 $\mathcal O_k$ は互いに素で、内部では $h_j$ が厳密に0または1となる。残りを正式な無反応結果

```math
\mathcal O_{\varnothing}
=
\left(
\bigcup_{k=1}^L
\mathcal O_k
\right)^c
```

へ含める。従って結果集合は $\{1,\ldots,L,\varnothing\}$ で全入力を覆い、無反応試行を除いて再規格化しない。

入力換算半幅は

```math
w
=
Xe^{-\Lambda}
```

である。選択角の切断接続領域の Haar 質量を $\varepsilon_{\rm cut}$ とすると、

```math
P(\varnothing)
\leq
\min
\left\{
1,
2(L-1)
\frac{w}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
\right\}
```

を得る。安全セクター内部では、境界までの余裕より小さい有限変動に対して結果は変わらない。

## 4.7 隣接テンプレート経路と内部記録

隣接テンプレートモードの生成子を

```math
Y_{j,j+1}
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

とし、

```math
\ell_j
=
1-h_j
```

と置く。最初に $P_M$ の単位面積流で $Q_M=1$ とし、$j=1,\ldots,L-1$ の順に

```math
G_j^{\rm route}
=
\frac{\pi\mathcal J_0}{2}
\ell_j
t^\dagger Y_{j,j+1}t
+
P_M\ell_j
```

を作用させる。

安全な結果 $k$ では $\ell_j=1$ が $j<k$、$\ell_j=0$ が $j\geq k$ なので、

```math
t:
e_1
\longmapsto
e_2
\longmapsto
\cdots
\longmapsto
e_k,
```

```math
Q_M
=
1+
\sum_{j=1}^{L-1}\ell_j
=
k
```

となる。各経路流で $t^\dagger Y_{j,j+1}t=0$ が保存され、$P_M=0$ なので、比較ポインターの共役運動量への反作用は零である。

無反応領域ではテンプレートと $Q_M$ が中間値を取り得る。$Q_M$ が偶然整数になる遷移点もあるため、結果判定に $Q_M$ 単独を使わず、必ず $\mathcal O_k$ と組み合わせる。

## 4.8 正準 SWAP と測定後状態

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

とする。Hamiltonian $\pi\mathcal J_0G_{\rm sw}/2$ を単位面積だけ作用させると、

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

となる。安全な結果 $k$ では SWAP 直前に $b=W\chi$、$t=e_k$ なので、直後は

```math
b=e_k,
\qquad
t=-W\chi
```

である。信号へ局所回路として実装した $W^\dagger$ を作用させれば、

```math
b_{\rm post}
=
W^\dagger e_k
=
|u_k\rangle
```

となる。測定前情報は消えず、テンプレートへ退避している。無反応では基底状態を主張しない。

<!-- theorem-start:theorem -->
**定理（安全セクターの条件付き測定後状態）**
固定純粋準備 $\chi$、固定基底 $\{|u_k\rangle\}$、安全セクター $\mathcal O_k$ の下で、結果 $k$ の測定直後の信号相関行列は

```math
C_k^{\rm post}
=
|u_k\rangle
\langle u_k|
```

である。無反応を含む無条件相関行列には、無反応領域の中間状態が別項として残る。
<!-- theorem-end:theorem -->

これは全系の非可逆な射影ではない。全系では正準 SWAP であり、信号部分だけを縮約すると測定前情報がテンプレートへ移ったように見える。

## 4.9 反復可能性の範囲

安全な結果 $k$ の直後に同じ基底変換を施すと

```math
Wb_{\rm post}
=
e_k
```

なので、新しい空テンプレートを持つ第2装置では同じ結果が確率1で得られる。ただし現在の装置のテンプレートには $-W\chi$ が保持されている。同じ装置をその場で再使用するには、先に内部逆計算を完了するか、別の空テンプレートを用意する必要がある。

## 4.10 内部記録保持と完全逆計算

保持窓では、結果を比較ポインターセクター、信号、内部記録から読める。続いて次の順に逆操作する。

1. 信号へ局所回路 $W$ を作用させる。
2. 逆 SWAP を作用させる。
3. 隣接テンプレート経路を逆順・逆角で実行し、$Q_M$ の初期移動を逆にする。
4. 双曲型増幅を逆実行する。
5. 累積剪断を逆順に実行する。
6. 作用・閾値読出しを逆実行する。
7. 信号へ局所回路 $W^\dagger$、$U_{\rm prep}^\dagger$ を作用させる。

前向き写像全体の厳密な逆を使うため、この帰還は無反応領域を含む。周期末には信号、テンプレート、全レジスターとその共役運動量が準備値へ戻る。

この逆計算は永久記録を消しているのではない。途中で作った情報を元の信号・選択器状態へ戻している。周期を越えて保持する外部記録まで同じ有限閉鎖系内で結果非依存の同一点へ戻すことは要求しない。

## 4.11 1本の自律 Hamiltonian

時計を

```math
(\tau,P_\tau),
\qquad
\tau\in S^1,
\qquad
H_{\rm clk}=P_\tau
```

とする。互いに重ならない滑らかな時計窓 $g_r(\tau)$ と各局所生成子 $G_r$ を用いて、

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_{r=1}^{N_{\rm cyc}(L,W)}
g_r(\tau)G_r
```

という1本の有限自律 Hamiltonian にまとめられる。$W$ と $W^\dagger$ の4回の使用は同じ局所回路の順方向・逆方向であり、準備と逆準備も同様である。

最後の生成子を

```math
G_{\rm drift}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

とする。各窓の生成子はその窓内で保存され、窓端で $g_r=0$ なので、時計運動量 $P_\tau$ も1周期後に準備値へ戻る。1個の時計変数から各局所辺へ窓信号を物理的に配る配線は、本章の代数構成には含めずQ10に残す。

## 4.12 Poincaré 写像と不変測度

Poincaré 断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内で、信号、テンプレート、全レジスター、全共役運動量、選択器作用、時計運動量を準備値へ固定した集合を $\mathcal T_{\chi,W}$ とする。自由変数は $\vartheta$ だけである。

<!-- theorem-start:theorem -->
**定理（滑らかな固定有限基底周期の不変測度）**
$L<\infty$、$\chi^\dagger\chi=1$、固定基底変換 $W$、互いに重ならない単位面積時計窓、$\alpha\notin\mathbb Q$ を仮定する。前節までの滑らかな局所回路を合成すると、$\mathcal T_{\chi,W}$ 上の Poincaré 写像は

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

滑らか化後も前向き写像と逆向き写像が厳密に打ち消し合うため、不変性とエルゴード性は比較境界を除外せずに成立する。結果の離散性は、安全セクターと無反応セクターからなる粗視化で定義する。

## 4.13 無反応込みの Born 型長期頻度

理想分布を

```math
p^{\rm id}
=
\left(
p_1,\ldots,p_L,0
\right),
\qquad
p_k
=
\left|
\langle u_k|\chi\rangle
\right|^2
```

とする。滑らかな周期の長期結果分布を $p^{\rm cyc}$ とする。安全セクターでは理想累積区間と同じ結果になり、失われた作動質量は全て無反応成分へ入る。従って

```math
D_{\rm TV}
\left(
p^{\rm cyc},p^{\rm id}
\right)
=
p^{\rm cyc}_{\varnothing}
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

である。任意の $\epsilon>0$ に対し $\Lambda$ を十分大きくし、角切断幅を十分小さくすれば、右辺を $\epsilon$ 未満にできる。

<!-- theorem-start:theorem -->
**定理（局所滑らか測定周期による Born 型頻度）**
任意の有限 $L$、固定純粋準備 $\chi$、固定有限直交基底 $\{|u_k\rangle\}$、任意の $\epsilon>0$ に対し、$3L+4$ 正準対からなる有限自律 Hamiltonian 周期を構成できる。相互作用は、局所位相回転、隣接2モード交換、局所読出し、隣接剪断、双曲型増幅、隣接テンプレート経路、正準 SWAP からなる。結果集合は $\{1,\ldots,L,\varnothing\}$ であり、各試行の結果は一意である。安全な結果 $k$ では測定後信号が厳密に $|u_k\rangle$ となり、無反応領域を含む全内部変数が周期末に準備値へ戻る。長期結果分布は

```math
D_{\rm TV}
\left(
p^{\rm cyc},
\left(
|\langle u_1|\chi\rangle|^2,
\ldots,
|\langle u_L|\chi\rangle|^2,
0
\right)
\right)
<
\epsilon
```

を満たすように選べる。
<!-- theorem-end:theorem -->

無理数回転は混合的ではない。従って長期平均は Born 型重みに任意精度で一致するが、結果列は独立同分布でなく、二項分布型有限標本揺らぎを一般には再現しない。

Q1からの入力誤差と装置誤差を含めると、安全な和上界は

```math
D_{\rm TV}^{\rm obs}
\leq
\varepsilon_{\rm dist}
+
\varepsilon_{\rm prep}
+
\varepsilon_W
+
\varepsilon_{\rm read}
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm clk}
```

となる。理想局所正準回路では $\varepsilon_W=0$ であり、Q1の出力を直接入力する場合は周期内準備誤差 $\varepsilon_{\rm prep}$ を省ける。

## 4.14 空間セル基底と主張の範囲

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。ただし、これは位相担体の空間セル基底を標本化する式である。粒子座標がセル $i$ の局所検出器を作動させること、粒子と選択モードが同期すること、粒子が連続軌道を持つことは別の導出を要する。

本章によりQ2は、固定純粋準備、固定有限基底、有限次元、任意精度という範囲で達成と判定する。一般混合状態を1本の軌道から生成すること、混合的有限標本統計、粒子の局所検出、連続スペクトル、Q1位置ばね網と測定回路の同一ハードウェア化、局所時計配線、有限温度の永久記録、弱開放 reset はこの判定に含めない。
