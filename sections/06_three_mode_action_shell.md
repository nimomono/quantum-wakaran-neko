@number: 6
@chapter: 本文
@title: 3モード境界作用殻と誘導場内部混合による等方準備
@status: 和・差作用、U(2) の不足、U(3) 不変測度、共通殻の周辺密度、残余ファイバー体積は厳密結果である。同じ誘導場からの全殻等方拡散と半径安定化の導出は未解決である。

## 6.1 和・差作用の余弦幾何

生成源が準備する2つの伝達ベクトルを

```math
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
```

```math
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
```

とする。第5章の局所記録後には

```math
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
```

```math
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
```

となる。$A,B\in\{-1,+1\}$ は局所固定指針に記録済みである。

相対角を

```math
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
```

とする。和・差作用は

```math
I_+^{AB}
=
\frac14
\left\|
u_A+u_B
\right\|^2,
```

```math
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
```

である。直接展開すると、

```math
I_\pm^{AB}
=
\frac14
\left[
r_A^2+r_B^2
\pm
2ABr_Ar_B\cos\Delta_{ab}
\right].
```

<!-- theorem-start:proposition -->
**命題（和・差作用の余弦恒等式）**
等振幅 $r_A=r_B=r$、固定相対生成源位相の下で、

```math
I_\pm^{AB}
=
I_0
\left[
1
\pm
AB\cos\Delta_{ab}
\right],
\qquad
I_0=\frac{r^2}{2}.
```

さらに、

```math
I_+^{AB}+I_-^{AB}=2I_0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
2つのベクトルの内積は

```math
u_A\cdot u_B
=
ABr^2\cos\Delta_{ab}.
```

これを和ベクトルと差ベクトルの2乗へ代入すればよい。和と差を加えると内積項が消える。
<!-- theorem-end:proof -->

位相雑音 $\delta$ を許し、その分布が設定と結果符号に依存しないとする。重みが $I_\pm$ に線形であるため、位相を先に平均できる。可視度 $0\leq V\leq1$ と位相ずれを $\Delta_{ab}$ へ吸収すれば、

```math
\overline I_\pm^{AB}
=
I_0
\left[
1
\pm
ABV\cos\Delta_{ab}
\right].
```

総入力作用は平均後も $2I_0$ である。振幅揺らぎを許す場合は、各試行で $I_++I_-$ が固定される範囲に中心定理を限定する。総作用自体の揺らぎは第8章の殻幅誤差へ含める。

## 6.2 3モード共通作用殻

境界3モードを

```math
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
},
\qquad
J_\nu=|a_\nu|^2,
\qquad
\nu\in\{+,s,r\}
```

とする。作用角変数では

```math
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
```

```math
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
```

総作用を

```math
C
=
J_++J_s+J_r
```

とする。固定値 $C_0>0$ の共通作用殻上の Liouville 測度は

```math
d\mu_{C_0}
=
\frac{
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_{\nu}
dJ_\nu\,d\theta_\nu
}{
\Omega_3(C_0)
},
```

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

複素3成分ベクトル $a=(a_+,a_s,a_r)^{\mathsf T}$ で見れば、この殻は

```math
a^\dagger a=C_0
```

という5次元球面である。

局所記録と静的和・差変換が与える境界適合条件は

```math
J_+=I_+^{AB}(a,b).
```

従って結果セクター $(A,B)$ に残る作用は

```math
C_0-I_+^{AB}
=
J_s+J_r.
```

$C_0=J_*+2I_0$ とすれば、

```math
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```

この恒等式は作用保存だけから従う。相対確率を得るには、異なる $J_+$ のファイバーにどの測度を置くかを決めなければならない。

## 6.3 残余2モードの U(2) 等方性では不足する

固定 $J_+=x$ の下では、残余2モードは

```math
J_s+J_r=C_0-x
```

という3次元球面を作る。$(a_s,a_r)$ に $U(2)$ が作用すると、この球面上で推移的である。従って、固定 $x$ の内部では正規化された $U(2)$ 不変測度が一意になる。

この事実から、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac{
1
}{
C_0-x
},
\qquad
0\leq J_s\leq C_0-x
```

という一様作用分配が従う。しかし、これは各ファイバー内部の条件付き分布であり、異なる $x$ のファイバー間の相対質量を決めない。

<!-- theorem-start:proposition -->
**命題（U(2) 等方性の不足）**
任意の非負可積分関数 $f$ に対し、

```math
d\mu_f
\propto
f(J_+)
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_\nu dJ_\nu\,d\theta_\nu
```

は、残余2モード $(a_s,a_r)$ に関して $U(2)$ 不変である。しかし、$J_+=x$ のファイバー質量は

```math
W_f(x)
\propto
f(x)(C_0-x)
```

となる。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$f(J_+)$ は残余2モードの回転で変化しない。固定 $J_+=x$ で角変数を積分し、$J_r$ のデルタ関数積分を行うと、

```math
\int_0^{C_0-x}dJ_s
=
C_0-x
```

が残る。従って任意の $f(x)$ がファイバー間の相対質量へ残る。
<!-- theorem-end:proof -->

従って、残余2モードの等方性だけから Bell 重みを導くことはできない。必要なのは、$J_+$ を含む3モード共通殻全体の測度である。

## 6.4 U(3) 不変測度

$U(3)$ は $a^\dagger a=C_0$ の球面上へ推移的に作用する。従って、正規化された $U(3)$ 不変確率測度は一意であり、固定作用殻の Liouville 測度 $d\mu_{C_0}$ と一致する。

<!-- theorem-start:proposition -->
**命題（共通殻不変測度の一意性）**
$S_{C_0}^5=\{a\in\mathbb C^3:a^\dagger a=C_0\}$ とする。$S_{C_0}^5$ 上の正規化 Borel 測度が全ての $U(3)$ 変換に不変なら、その測度は $d\mu_{C_0}$ に等しい。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$U(3)$ は球面上で推移的であり、安定部分群は $U(2)$ である。従って球面は同次空間 $U(3)/U(2)$ と同一視できる。コンパクト群の正規化 Haar 測度を商空間へ押し出した測度は不変である。不変確率測度の平均作用を用いれば一意性が従う。作用角変数で書けば、その押し出しは $d\mu_{C_0}$ である。
<!-- theorem-end:proof -->

固定された損失のない3入力3出力接合部は $U(3)$ 変換を1つ実行するだけであり、単一の入力位相点を殻全体へ広げない。上の命題は不変測度の一意性を述べるのであって、Hamilton 方程式が確率測度を無から生成することを述べない。

## 6.5 誘導場内部混合による全殻等方拡散

境界3モードの準備窓で、構造化誘導場の多数の未読自由度と非線形内部混合を消去した縮約方程式を考える。理想的な殻接方向生成子を

```math
\mathcal L_{\rm iso}
=
D_\partial\Delta_{S^5},
\qquad
D_\partial>0
```

とする。$\Delta_{S^5}$ は固定作用殻の Laplace--Beltrami 作用素である。

この接方向生成子は、常時の外部漏れを直接拡散へ読み替えたものではない。Hamiltonian な内部混合が殻方向を探索し、弱い外部交換は欠陥除去、有限再帰の抑制、半径分布の維持を担う。2つの効果を同じ係数へまとめない。

<!-- theorem-start:theorem -->
**定理（等方殻拡散の定常測度）**
連結な固定作用殻 $S_{C_0}^5$ 上で

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

を考える。規格化された非負密度の定常解は定数だけであり、$d\mu_{C_0}$ が一意な定常確率測度である。初期密度が $L^2$ なら、

```math
\left\|
f_t-1
\right\|_{L^2(d\mu_{C_0})}
\leq
e^{-D_\partial\lambda_1t}
\left\|
f_0-1
\right\|_{L^2(d\mu_{C_0})},
```

ここで $\lambda_1>0$ は殻上 Laplacian の第1非零固有値である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
定常密度 $f$ に対し、部分積分から

```math
\int
f\Delta_{S^5}f\,d\mu_{C_0}
=
-
\int
\left|
\nabla_{S^5}f
\right|^2
d\mu_{C_0}.
```

左辺は0なので、連結性から $f$ は定数である。規格化により $f=1$ となる。時間発展については定数成分を除いた固有関数展開を用い、第1非零固有値で評価する。
<!-- theorem-end:proof -->

混合不足の尺度を

```math
\varepsilon_{\rm mix}
=
\exp
\left(
-D_\partial\lambda_1\tau_{\rm prep}
\right)
```

とする。$\varepsilon_{\rm mix}\ll1$ なら、滑らかな観測量について初期の方向偏りは小さくなる。

有限 Hamiltonian 浴からこの拡散を得る候補は、$U(3)$ の Hamiltonian 生成子を、等方な相関行列を持つ浴変数へ弱く結合することである。弱結合・短相関時間極限では、2次の縮約生成子が $U(3)$ の Casimir 作用素へ近づく。付録Cに具体形を示す。

ただし、有限閉鎖 Hamiltonian 流れは微細 Liouville 密度を保存し、一般には $L^1$ で一様密度へ収束しない。有限浴だけで主張できるのは、有限時間・有限分解能の混合または弱い観測量収束である。不可逆な一意定常分布を用いる場合は、常時の弱い外部交換まで含む縮約が必要である。

## 6.6 異方性と半径方向の弱開放補正

現行の縮約生成子を

```math
\mathcal L
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_{\rm aniso}
+
\mathcal L_C
```

と分ける。$\mathcal L_{\rm aniso}$ は殻接方向の異方成分、$\mathcal L_C$ は総作用 $C$ の半径方向変化を表す。

半径方向の有効式の候補を

```math
dC_t
=
-\gamma_C
\left(
C_t-C_0
\right)dt
+
\sqrt{2D_C}\,dW_t
```

とする。これは、外部への漏れと仕事貯蔵系または微小揺らぎからの流入が $C_0$ 付近で釣り合う線形化である。定常幅は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C},
\qquad
\varepsilon_C
=
\frac{\sigma_C}{C_0}.
```

$\varepsilon_C\ll1$ なら、固定殻計算を狭い準定常殻へ適用できる。純粋な漏れ

```math
\dot C=-\gamma_C C
```

だけでは、$C=0$ へ落ちるだけで $C_0>0$ の定常殻を作らない。

異方性と半径幅が小さく、境界ファイバーが殻端から離れていれば、滑らかな結果重みの補正を

```math
O
\left(
\varepsilon_{\rm aniso}
+
\varepsilon_{\rm mix}
+
\varepsilon_C
\right)
```

と整理できる。全係数を同じ有限浴の尺度から与える一様上界は未完成であるため、現行モデルへの接続は近似結果である。

## 6.7 共通殻の周辺密度

<!-- theorem-start:theorem -->
**定理（和モード作用の周辺密度）**
3モード固定作用殻の正規化 Liouville 測度について、$J_+=x$ の周辺密度は

```math
p_+(x)
=
\frac{
2(C_0-x)
}{
C_0^2
}
\mathbf1_{\{0\leq x\leq C_0\}}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数を積分すると $(2\pi)^3$ を得る。$J_+=x$ を固定した未規格化密度は

```math
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
=
(2\pi)^3(C_0-x).
```

これを

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}
```

で規格化すればよい。
<!-- theorem-end:proof -->

この線形密度が Bell 重みの起源になる。重要なのは、各 $x$ の残余2モード分布を別々に質量1へ規格化しないことである。4つの結果セクターを同じ3モード作用殻の切断として比較する。

## 6.8 残余ファイバー体積

結果セクター $(A,B)$ の理想境界条件を

```math
g_{AB}
=
J_+-I_+^{AB}(a,b)
=
0
```

とする。作用座標でこの制約を用いる場合、$|\partial g_{AB}/\partial J_+|=1$ であり、coarea Jacobian は全結果と全設定に共通である。

<!-- theorem-start:proposition -->
**命題（残余ファイバーの線形体積）**
$0<I_+^{AB}<C_0$ とする。固定作用殻と $g_{AB}=0$ の交わりに誘導される未規格化 Liouville 体積は

```math
\Omega_{AB}
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right)
```

に比例する。共通定数を除けば、

```math
W_{AB}
\propto
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$J_+=I_+^{AB}$ を固定し、$J_r$ のデルタ関数積分を行う。許される $J_s$ は

```math
0\leq J_s\leq C_0-I_+^{AB}
```

なので、その長さが残る。3つの角変数は共通因子 $(2\pi)^3$ を与える。
<!-- theorem-end:proof -->

一般の境界写像では、解集合自体を無条件にシンプレクティック多様体と呼ばない。全境界正準位相空間の Liouville 測度を、作用殻と境界適合写像で制限して得る誘導測度として定義する。複数解、分岐、caustic がある場合は、Jacobianと多重度を含める必要がある。

## 6.9 有限分解能

現実の境界適合条件には幅 $\delta_J>0$ がある。共通窓関数 $K_{\delta_J}$ を用い、

```math
K_{\delta_J}
\left(
J_+-I_+^{AB}
\right)
```

で制限する。$I_+^{AB}$ が殻端から $\delta_J$ より十分離れ、$K_{\delta_J}$ が全結果に共通なら、

```math
W_{AB}^{(\delta_J)}
=
c_{\delta_J}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
\frac{\delta_J^2}{C_0}
\right).
```

$c_{\delta_J}$ は全セクターに共通で規格化時に消える。窓幅または Jacobian が結果や設定に依存する場合は、余分な重みを直接導入するため認めない。

## 6.10 本章の結論

残余2モードの $U(2)$ 等方性は、固定 $J_+$ のファイバー内部を一様にするだけで、ファイバー間の質量を決めない。この不足は任意関数 $f(J_+)$ を用いた反例で厳密に示せる。

3モード全体の $U(3)$ 等方性は共通作用殻上の測度を一意に決める。縮約された等方拡散では、その測度が一意な定常分布になる。固定殻の $J_+$ 周辺は $C_0-J_+$ に比例し、境界条件 $J_+=I_+^{AB}$ を課した残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となる。

固定殻の幾何と縮約拡散の定常測度は、指定した補助モデル内で厳密である。一方、同じ構造化有限浴と常時の弱い外部交換から、非退化な $U(3)$ 等方生成子、混合時間、異方誤差、殻幅を導くことは未完成である。次章では、共通殻の誘導測度を履歴空間へ押し出し、Bell 型共同確率と前提違反を計算する。
