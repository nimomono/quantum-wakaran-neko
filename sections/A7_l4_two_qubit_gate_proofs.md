@number: G
@chapter: 付録
@title: 4モード操作代数、CNOT流、忠実度上界
@status: M39について、複素振幅と実正準座標の対応、局所操作代数の可換性、積状態の階数条件、差モード射影、厳密CNOT、面積誤差、一般制御誤差、資源上界を検算可能な形で証明する。

## G.1 複素振幅の正準括弧

各モードについて

```math
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}},
\qquad
\overline b_j
=
\frac{Q_j-iP_j}{\sqrt{2\mathcal J_0}}
```

と置くと、

```math
\{b_j,\overline b_k\}
=
-\frac{i}{\mathcal J_0}\delta_{jk},
\qquad
\{b_j,b_k\}
=0
```

である。Hermitian 行列 $K,L$ に対して

```math
F_K
=
\mathcal J_0b^\dagger Kb,
\qquad
F_L
=
\mathcal J_0b^\dagger Lb
```

とすれば、直接計算により

```math
\{F_K,F_L\}
=
-i\mathcal J_0b^\dagger[K,L]b
```

を得る。また、

```math
\dot b_j
=
\{b_j,F_K\}
=
-i(Kb)_j
```

なので、$i\dot b=Kb$ である。$K$ がHermitian なら $e^{-itK}$ はユニタリであり、

```math
\frac{\mathrm d}{\mathrm dt}
b^\dagger b
=0
```

となる。複素ユニタリ写像の実表示は直交かつシンプレクティックなので、元の実8次元位相空間で正準性を保存する。

## G.2 2つの局所操作代数

基底順序を

```math
|00\rangle,
|01\rangle,
|10\rangle,
|11\rangle
```

とする。行列単位を $E_{ab}$ と書けば、

```math
\mathcal A
=
\operatorname{span}_{\mathbb C}
\left\{
E_{aa'}\otimes I_2
\right\},
```

```math
\mathcal B
=
\operatorname{span}_{\mathbb C}
\left\{
I_2\otimes E_{bb'}
\right\}
```

である。任意の要素について

```math
(A\otimes I_2)(I_2\otimes B)
=
A\otimes B
=
(I_2\otimes B)(A\otimes I_2)
```

なので両代数は可換である。

$X\in M_4(\mathbb C)$ が全ての $A\otimes I_2$ と可換すると仮定する。$X$ をA添字に関する $2\times2$ 区画行列へ分け、対角行列単位と非対角行列単位との交換関係を順に使うと、全対角区画が同じ行列 $B$、非対角区画が0になる。従って

```math
\mathcal A'
=
\mathcal B.
```

同様に $\mathcal B'=\mathcal A$ である。また積 $A\otimes B$ の線形包は $M_4(\mathbb C)$ 全体なので、2つの代数は4次元振幅空間を完全に分離する操作的な部分系構造を与える。

<!-- theorem-start:proof -->
**証明（R104）**

G.1節の括弧公式へ $K=A\otimes I_2$、$L=I_2\otimes B$ を代入すると、行列交換子が0なので対応するHamiltonian のPoisson 括弧も0である。Pauli 行列と恒等行列のHermitian 線形包は各 $M_2(\mathbb C)$ のHermitian 部分全体である。G.3節の正方形配線がその $X$ と $Z$ を実装し、交換子から $Y$ も生成する。相互可換代数と相互可換代数の計算から操作誘導テンソル積が定まる。積状態保存はG.4節で示す。
<!-- theorem-end:proof -->

## G.3 正方形配線の行列表現

交換生成子は

```math
G^X_{jk}
=
Q_jQ_k+P_jP_k
=
\mathcal J_0
b^\dagger
\left(
|j\rangle\langle k|
+
|k\rangle\langle j|
\right)b
```

である。従って

```math
G_A^X
=
\mathcal J_0b^\dagger(X\otimes I_2)b,
\qquad
G_B^X
=
\mathcal J_0b^\dagger(I_2\otimes X)b.
```

同様に作用差から

```math
G_A^Z
=
\mathcal J_0b^\dagger(Z\otimes I_2)b,
\qquad
G_B^Z
=
\mathcal J_0b^\dagger(I_2\otimes Z)b
```

を得る。各部分系の $X$ と $Z$ は $su(2)$ を生成する。異なる部分系の全生成子は可換であり、同一制御窓に入れても順序誤差を生じない。

## G.4 積状態の階数条件

状態 $b$ が積状態なら、ある非零ベクトル $u,v\in\mathbb C^2$ により $b_{ab}=u_av_b$ と書ける。従って

```math
B(b)
=
uv^{\mathsf T}
```

は階数1で、$\det B=0$ である。

逆に、規格化された非零 $2\times2$ 行列 $B$ が $\det B=0$ を満たすなら階数は1である。任意の非零列を $u$ とし、他方の列はその複素数倍として $v$ の成分へ吸収できるので、$B=uv^{\mathsf T}$ と因子化できる。

局所操作では

```math
B'
=
U_ABU_B^{\mathsf T}
```

である。$U_A,U_B$ は可逆なので、

```math
\operatorname{rank}B'
=
\operatorname{rank}B
```

となる。行列式は

```math
\det B'
=
(\det U_A)(\det U_B)\det B
```

なので、ユニタリ局所操作では $|\det B|$ も保存される。

## G.5 差モード射影の正準表示

差モード $|d\rangle=(|10\rangle-|11\rangle)/\sqrt2$ に対し、

```math
\Pi_{\rm CX}
=
|d\rangle\langle d|
```

は

```math
\Pi_{\rm CX}^2
=
\Pi_{\rm CX},
\qquad
\Pi_{\rm CX}^\dagger
=
\Pi_{\rm CX}
```

を満たす。制御値1の2次元部分空間では、反対称標的状態への射影が $(I_2-X)/2$ なので、

```math
\Pi_{\rm CX}
=
|1\rangle\langle1|_A
\otimes
\frac{I_2-X_B}{2}
```

である。

正準座標で生成関数を展開すると、

```math
\mathcal J_0
b^\dagger\Pi_{\rm CX}b
=
\frac{\mathcal J_0}{2}
|b_{10}-b_{11}|^2
```

```math
=
\frac14
\left[
(Q_{10}-Q_{11})^2
+
(P_{10}-P_{11})^2
\right].
```

これは非負であり、$b^\dagger b=1$ なら $0\leq G_{\rm CX}\leq\mathcal J_0$ である。

## G.6 射影指数と厳密CNOT

射影の冪は $\Pi_{m CX}^n=\Pi_{m CX}$ なので、指数級数から

```math
e^{-iA\Pi_{\rm CX}}
=
I_4
+
\left(e^{-iA}-1\right)
\Pi_{\rm CX}
```

を得る。$A=\pi$ では

```math
e^{-i\pi\Pi_{\rm CX}}
=
I_4-2\Pi_{\rm CX}.
```

制御値0の部分空間では $\Pi_{\rm CX}=0$ なので恒等写像である。制御値1の部分空間では

```math
I_2
-
2\frac{I_2-X}{2}
=
X
```

となるため、全行列はCNOTに一致する。

<!-- theorem-start:proof -->
**証明（R105）**

$H_{\rm CX}=P_\tau+g(\tau)G_{\rm CX}$ では $\dot\tau=1$ であり、信号生成子は全時刻で同じ射影の実数倍である。従って異なる時刻の生成子は可換で、時間順序積は面積 $A$ の指数へ厳密に縮約する。$A=\pi$ で上の計算からCNOTを得る。G.1節により流れは正準かつ作用保存である。G.7節の積入力を階数2へ写すため、局所操作の積には分解できない。
<!-- theorem-end:proof -->

## G.7 非因子化生成と相関

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

## G.8 面積誤差の厳密評価

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

## G.9 一般Hermitian 誤差の上界

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

## G.10 有限時間と資源数

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

<!-- theorem-start:proof -->
**証明（R106）**

G.5節から固定作用面上の相互作用エネルギー上界、G.10節から動作時間下界と5正準対上界を得る。G.8節が面積誤差の厳密式、G.9節が一般制御誤差の上界を与える。これらを合わせるとR106が従う。
<!-- theorem-end:proof -->

## G.11 適用限界

本付録の証明は、4複素モードの直接符号化、固定作用面、Hermitian 2次制御、1つの論理分解に限定される。次は証明していない。

1. 4モード分解のミクロ物理的自然さまたは一意性。
2. 2つの独立物理担体への分解。
3. 空間的に離れた局所制御信号の有限速度配線。
4. Bell 共同頻度またはBell 前提監査。
5. 一般雑音過程の確率分布と長時間蓄積。
6. $2^n$ モード未満の多量子ビット符号化。
7. 資源上界の最小性。
