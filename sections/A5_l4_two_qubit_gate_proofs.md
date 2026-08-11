@number: E
@chapter: 付録
@title: M39の4モード操作代数、CNOT流、共同統計
@status: M39について、複素振幅と実正準座標の対応、局所操作代数の可換性、積状態の階数条件、差モード射影、厳密CNOT、面積誤差、一般制御誤差、資源上界を検算可能な形で証明する。

## E.1 複素振幅と実正準流

各複素振幅を

```math
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}}
```

とすると、$\{b_j,\overline b_k\}=-i\delta_{jk}/\mathcal J_0$ である。Hermitian行列 $K,L$ に対する2次Hamiltonian $F_K=\mathcal J_0b^\dagger Kb$ は

```math
\{F_K,F_L\}
=
-i\mathcal J_0b^\dagger[K,L]b,
\qquad
i\dot b
=
Kb
```

を満たす。従って有限流 $e^{-itK}$ はユニタリであり、実8次元表示では正準性と全作用 $\mathcal J_0b^\dagger b$ を保存する。以下の代数計算を実正準Hamiltonianへ移す根拠はこの対応である。

## E.2 2つの局所操作代数

基底順序を $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ とし、

```math
\mathcal A
=
M_2(\mathbb C)\otimes I_2,
\qquad
\mathcal B
=
I_2\otimes M_2(\mathbb C)
```

と置く。任意の $A,B\in M_2(\mathbb C)$ について $(A\otimes I_2)(I_2\otimes B)=A\otimes B$ なので、両代数は可換である。区画行列に対する行列単位との交換関係から、相互可換代数は $\mathcal A'=\mathcal B$、$\mathcal B'=\mathcal A$ となる。積 $A\otimes B$ の線形包は $M_4(\mathbb C)$ 全体であるため、この2代数が操作誘導テンソル積を定める。

<!-- theorem-start:proof -->
**証明（R104）**

G.1節の括弧公式へ $K=A\otimes I_2$、$L=I_2\otimes B$ を代入すると、対応するHamiltonianはPoisson可換である。G.3節の正方形配線が各代数のPauli生成子を実装し、G.4節の階数条件が局所操作による積状態保存を与える。
<!-- theorem-end:proof -->

## E.3 正方形配線

交換生成子 $G^X_{jk}=Q_jQ_k+P_jP_k$ とモード作用差を正方形の対辺へ同期配置すると、

```math
G_A^X
=
\mathcal J_0b^\dagger(X\otimes I_2)b,
\qquad
G_B^X
=
\mathcal J_0b^\dagger(I_2\otimes X)b,
```

```math
G_A^Z
=
\mathcal J_0b^\dagger(Z\otimes I_2)b,
\qquad
G_B^Z
=
\mathcal J_0b^\dagger(I_2\otimes Z)b
```

を得る。同じ部分系の $X,Z$ は $su(2)$ を生成し、異なる部分系の生成子は全て可換である。このため局所位相回転と $QQ+PP$ 交換の有限列が、両局所操作代数を実正準流として実装する。

## E.4 積状態の階数条件

4振幅を係数行列

```math
B(b)
=
\begin{pmatrix}
b_{00}&b_{01}\\
b_{10}&b_{11}
\end{pmatrix}
```

へ並べる。非零状態が積状態であることは、$B=uv^{\mathsf T}$、すなわち $\operatorname{rank}B=1$ または $\det B=0$ と同値である。局所操作では

```math
B
\longmapsto
U_ABU_B^{\mathsf T}
```

となるため、階数と $|\det B|$ は保存される。これはM39内部の論理因子化条件であり、2つの独立物理担体への分解ではない。

## E.5 差モード射影の正準表示

差モード $|d\rangle=(|10\rangle-|11\rangle)/\sqrt2$ への射影は

```math
\Pi_{\rm CX}
=
|d\rangle\langle d|
=
|1\rangle\langle1|_A
\otimes
\frac{I_2-X_B}{2}
```

である。対応する実2次生成子は

```math
G_{\rm CX}
=
\mathcal J_0b^\dagger\Pi_{\rm CX}b
=
\frac14
\left[
(Q_{10}-Q_{11})^2
+
(P_{10}-P_{11})^2
\right].
```

従って $b^\dagger b=1$ なら $0\leq G_{\rm CX}\leq\mathcal J_0$ であり、新しい相互作用次数を導入せず、下側1交換辺と2作用項で実装できる。

## E.6 射影指数と厳密CNOT

射影の冪は $\Pi_{\rm CX}^n=\Pi_{\rm CX}$ なので、

```math
e^{-iA\Pi_{\rm CX}}
=
I_4
+
\left(e^{-iA}-1\right)
\Pi_{\rm CX}
```

である。$A=\pi$ では制御値0部分空間に恒等写像、制御値1部分空間に $I_2-2(I_2-X)/2=X$ が作用する。従って全行列はCNOTに一致する。

<!-- theorem-start:proof -->
**証明（R105）**

$H_{\rm CX}=P_\tau+g(\tau)G_{\rm CX}$ では $\dot\tau=1$ で、信号生成子は全時刻で同じ射影の実数倍である。時間順序積は窓面積 $A$ の指数へ厳密に縮約し、$A=\pi$ で上のCNOTを得る。G.1節により流れは正準かつ作用保存である。G.7節の積入力を階数2へ写すため、局所操作の積には分解できない。
<!-- theorem-end:proof -->

## E.7 非因子化生成と相関

入力 $|+0\rangle$ の係数行列は

```math
B_{\rm in}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&0\\
1&0
\end{pmatrix}
```

であり、階数1である。CNOT後は

```math
B_{\rm out}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
```

となるため、階数2かつ $2|\det B_{\rm out}|=1$ である。

状態を $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$ と書く。Pauli 作用を基底へ直接適用すると、

```math
(X\otimes X)|\Phi^+\rangle
=
|\Phi^+\rangle,
```

```math
(Z\otimes Z)|\Phi^+\rangle
=
|\Phi^+\rangle,
```

```math
(Y\otimes Y)|\Phi^+\rangle
=
-|\Phi^+\rangle
```

となり、本文の3相関が従う。

## E.8 面積誤差の厳密評価

理想行列と実行列の相対行列は

```math
W(\delta A)
=
U_{\rm CX}^\dagger
U(\pi+\delta A)
=
e^{-i\delta A\Pi_{\rm CX}}.
```

固有値は1が3重、$e^{-i\delta A}$ が1重である。従って固定ゲージの作用素距離は

```math
\|W-I_4\|_{\rm op}
=
|e^{-i\delta A}-1|
=
2
\left|
\sin\frac{\delta A}{2}
\right|.
```

共通位相を最適化すると、単位円上の2固有値の中点位相が最適であり、$|\delta A|\leq\pi$ について

```math
\inf_\phi
\|W-e^{i\phi}I_4\|_{\rm op}
=
2\sin\frac{|\delta A|}{4}.
```

規格化入力について $p=\langle\psi|\Pi_{\rm CX}|\psi\rangle$ と置けば、目標出力との重なりは

```math
\langle\psi|W|\psi\rangle
=
1-p+pe^{-i\delta A}
```

なので、

```math
F_\psi
=
1
-
4p(1-p)
\sin^2\frac{\delta A}{2}.
```

$p=1/2$ で最小になり、最悪入力非忠実度は $\sin^2(\delta A/2)$ である。$|+0\rangle$ では $p=1/4$ なので、目標非忠実度は $3\sin^2(\delta A/2)/4$ となる。

4次元ユニタリの平均ゲート忠実度は

```math
F_{\rm avg}
=
\frac{|\operatorname{tr}W|^2+4}{20}.
```

$\operatorname{tr}W=3+e^{-i\delta A}$ を代入すると、

```math
F_{\rm avg}
=
1
-
\frac35
\sin^2\frac{\delta A}{2}
```

を得る。

面積誤差付き $|+0\rangle$ 出力の係数行列を直接計算すると、

```math
2|\det B|
=
\frac{|1+e^{-i\delta A}|}{2}
=
\left|
\cos\frac{\delta A}{2}
\right|.
```

真理値表について、制御値0の2基底は射影の核にあるため誤り0である。制御値1の各基底は対称・反対称標的成分を等重みで含むため、誤り確率は $\sin^2(\delta A/2)$ となる。

## E.9 一般Hermitian 誤差の上界

共通位相関数 $c(t)$ を1つ選び、

```math
\Delta K_c(t)
=
\Delta K(t)-c(t)I_4
```

と置く。対応する共通位相を実伝播行列から除いた後、理想伝播との相互作用表示を $V(t)$ とする。Duhamel 公式は

```math
V(T)-I_4
=
-i
\int_0^T
U_0(t)^\dagger
\Delta K_c(t)
\widetilde U_c(t)
\,\mathrm dt
```

を与える。両側の伝播行列はユニタリなので、

```math
\|V(T)-I_4\|_{\rm op}
\leq
\int_0^T
\|\Delta K_c(t)\|_{\rm op}
\,\mathrm dt.
```

$c(t)$ について下限を取ると本文の $\eta_{\rm g}$ 上界を得る。ユニタリ行列間の距離は最大2なので右辺を $\min\{2,\eta_{\rm g}\}$ とできる。

規格化ベクトル $x,y$ の共通位相最適化後の距離を $d$ とすると、

```math
1-|x^\dagger y|^2
\leq
d^2.
```

従って $1-F_\psi\leq\min\{1,\eta_{\rm g}^2\}$ である。$|\Phi^+\rangle$ と任意の積状態の重なり2乗はSchmidt 係数から最大 $1/2$ なので、$\eta_{\rm g}<1/\sqrt2$ なら実出力は積状態でない。

## E.10 有限時間と資源数

非負窓、$g\leq g_{\max}$、支持長 $T_{\rm g}$ なら、

```math
\pi
=
\int g(t)\,\mathrm dt
\leq
g_{\max}T_{\rm g}
```

から $T_{\rm g}\geq\pi/g_{\max}$ を得る。滑らかな有限支持関数は端に立上りと立下りを持つため、同じ最大値で任意の $T_{\rm g}>\pi/g_{\max}$ に面積 $\pi$ を調整できる。

信号には4正準対、窓の自律化には1時計正準対を使う。生成子は2つの単一モード作用項と1つの $QQ+PP$ 交換辺から成る。従ってゲート単体は5正準対で構成できる。

M35の $L=4$ 構成は、信号4対、テンプレート4対、作用レジスター4対、閾値1対、内部記録1対、選択器1対、時計1対を使う。合計は

```math
4+4+4+1+1+1+1
=16
```

である。ゲート信号と時計をM35側の信号と時計へ組み込む場合、固定設定の検算周期に追加の正準対は不要である。

## E.11 共同入力--出力統計の合成

固定ラベル $s$ のM35周期で、準備回路 $U_{{\rm prep},s}$ の後、基底回路 $W_s$ の前にM39の面積 $\pi$ のCNOT窓を挿入する。逆計算側では、対応する位置に逆CNOT窓を挿入する。全窓を重ならない時計区間へ置けるため、これは1本の有限自律Hamiltonian であり、周期末の内部Poincaré写像を変えない。第5章のM35定理を

```math
\chi
=
U_{\rm CX}\chi_s,
\qquad
W
=
W_s
```

へ適用すると、結果 $r$ の理想長期頻度は

```math
p_s^{\rm id}
\left(r\right)
=
\left|
\left[
W_sU_{\rm CX}\chi_s
\right]_r
\right|^2
```

となり、滑らかな比較で失われる質量は全て無反応へ入る。

実ゲートを $\widetilde U_s$ とし、ある共通位相 $\phi_s$ について

```math
\left\|
\widetilde U_s
-
e^{i\phi_s}U_{\rm CX}
\right\|_{\rm op}
\leq
\min
\left\{
2,\eta_{{\rm g},s}
\right\}
```

とする。任意の固定基底測定の全変動距離は純粋状態間の跡距離以下であり、その跡距離は共通位相最適化後のベクトル距離以下なので、ゲート誤差の寄与は $\min\{1,\eta_{{\rm g},s}\}$ 以下である。M35の無反応質量 $\delta_s$ を加えると、固定 $s$ の出力分布誤差は

```math
D_{\rm TV}
\left(
p_s^{\rm cyc},p_s^{\rm id}
\right)
\leq
\delta_s
+
\min
\left\{
1,\eta_{{\rm g},s}
\right\}.
```

有限入力集合の目標頻度 $\lambda_s$ を有理頻度 $n_s/N$ で近似し、合計 $N$ 個のラベル付きセルを直積する。$1$ と全選択器角増分を有理数体上で1次独立に選べば、直積回転は積Haar測度に関して一意エルゴード的である。従ってラベル付き共同分布の全変動距離は、入力頻度の近似誤差と各セルの出力誤差の加重和以下になる。$N$、比較増幅、角切断幅を有限値のまま順に選べば、任意の目標精度を得る。各セルは16正準対なので単純上界は $16N$ 正準対である。

<!-- theorem-start:proof -->
**証明（R106）**

G.5節から固定作用面上の相互作用エネルギー上界、G.10節から動作時間下界と5正準対上界を得る。G.8節が面積誤差の厳密式、G.9節が一般制御誤差の上界を与える。G.11節がM39とM35の正準合成、無反応込みの共同入力--出力分布、全変動距離上界、16正準対セルの有限直積構成を与える。これらを合わせるとR106が従う。
<!-- theorem-end:proof -->

## E.12 適用限界

本付録の証明は、4複素モードの直接符号化、固定作用面、Hermitian 2次制御、1つの論理分解に限定される。次は証明していない。

1. 4モード分解のミクロ物理的自然さまたは一意性。
2. 2つの独立物理担体への分解。
3. 空間的に離れた局所制御信号の有限速度配線。
4. Bell 共同頻度またはBell 前提監査。
5. 一般雑音過程の確率分布と長時間蓄積。
6. $2^n$ モード未満の多量子ビット符号化。
7. 資源上界の最小性。
8. 未知入力、未知装置の完全過程トモグラフィー、独立同分布型有限標本統計。
