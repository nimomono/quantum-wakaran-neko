@number: C
@chapter: 付録
@title: 可逆テンソル積状態の生成、永続ゲート、末端測定機構の証明
@status: R181B/R181Cを有限正準ハミルトニアン構成として証明し、R181Dの条件と誤差境界を分離する。

## C.1　実正準表示

$d$ 個の複素モードに共通作用尺度 $J_C>0$ を取り、

```math
 z_r=\frac{Q_r+iP_r}{\sqrt{2J_C}},
 \qquad
 \{Q_r,P_s\}=\delta_{rs}
 \tag{C.1}
```

とする。エルミート行列 $h=h^\dagger$ に対する実関数

```math
 H_h=z^\dagger hz
 \tag{C.2}
```

のHamilton方程式は

```math
 iJ_C\dot z=hz.
 \tag{C.3}
```

従って有限次元ユニタリ $U$ は、エルミート対数 $h$ と有限時間パルスを選ぶことで実正準流として実装できる。大域位相も実正準回転であり、末端Born比には影響しない。

## C.2　乗算パルス

供給源 $a_j,b_k$ と対象正準対 $(x,\pi^x)$、$(y,\pi^y)$ を考える。持ち上げ中のハミルトニアンを

```math
 H_{jk}
 =\chi(\tau)
 \left[
 \pi^x\sqrt2s_C\operatorname{Re}(a_jb_k)
 +\pi^y\sqrt2s_C\operatorname{Im}(a_jb_k)
 \right],
 \qquad
 s_C=\sqrt{2J_C}
 \tag{C.4}
```

とする。実部と虚部は供給源の実正準座標の2次多項式なので、式(C.4)は有限次数の実ハミルトニアンである。

対象を

```math
 x=y=\pi^x=\pi^y=0
 \tag{C.5}
```

から始め、$\int\chi(\tau)dt=1$ とする。$H_{jk}$ は $x,y$ に依存しないから $\pi^x,\pi^y$ は零のままである。そのため供給源に対するHamilton方程式の右辺も零となり、供給源は未使用多様体上で不変である。対象は

```math
 x=\sqrt2s_C\operatorname{Re}(a_jb_k),
 \qquad
 y=\sqrt2s_C\operatorname{Im}(a_jb_k)
 \tag{C.6}
```

へ移る。

$w^x=(x+i\pi^x)/s_C$、$w^y=(y+i\pi^y)/s_C$ とすると

```math
 w^x=\sqrt2\operatorname{Re}(a_jb_k),
 \qquad
 w^y=\sqrt2\operatorname{Im}(a_jb_k).
 \tag{C.7}
```

ここで本文式(4.11)は

```math
 S_0^{\mathsf T}JS_0=J,
 \qquad
 \det S_0=1
 \tag{C.8}
```

を満たす。対応する複素モードの変換は

```math
 \begin{pmatrix}Z_{jk}\\G_{jk}\end{pmatrix}
 =
 \frac1{\sqrt2}
 \begin{pmatrix}1&i\\1&-i\end{pmatrix}
 \begin{pmatrix}w^x\\w^y\end{pmatrix}.
 \tag{C.9}
```

式(C.7)を代入すれば

```math
 Z_{jk}=a_jb_k,
 \qquad
 G_{jk}=\overline{a_jb_k}.
 \tag{C.10}
```

を得る。$F^x=s_C\operatorname{Re}(a_jb_k)$、$F^y=s_C\operatorname{Im}(a_jb_k)$ と置くと $Z_{jk}=a_jb_k/\sqrt2$ となるため、式(C.4)の $\sqrt2$ を落としてはならない。

## C.3　可逆性と有限性

ハミルトニアン流は拡大位相空間上で1対1である。出力 $Z_S$ だけを残して供給源、$G_S$、作業領域、時計自由度履歴を捨てれば見かけ上の非可逆写像になるが、M54はそれらを浴内に保持する。逆順に $S_0^{-1}$ を作用させ、$\chi$ の符号を反転したパルスを通せば式(C.5)へ戻る。

多項式ハミルトニアンが大振幅で発散しないよう、安全コンパクト集合 $K$ の近傍で1となる滑らかなカットオフ $\eta_K$ を式(C.4)へ掛ける。有限入力次元、有限対象数、有限パルス時間では $K$ を通る理想軌道を覆う有限台を選べる。よって作用、時間、モード数は有限である。

実装ハミルトニアンベクトル場を理想場から一様に $\epsilon_X$ だけずらし、同じコンパクト集合上のLipschitz定数を $L_K$、時間を $T$ とする。Grönwall評価により

```math
 \|\widetilde\Gamma(T)-\Gamma(T)\|
 \leq
 \frac{e^{L_KT}-1}{L_K}\epsilon_X
 +e^{L_KT}\epsilon_{\rm blank}.
 \tag{C.11}
```

$L_K=0$ の場合は第1項を $T\epsilon_X$ と読む。

<!-- theorem-start:proof -->
**証明（R181B）**

式(C.4)--式(C.7)が各対象への積の書込みを与え、式(C.8)、式(C.9)がそれを $Z_{jk}=a_jb_k$ とanti-モードへ正準的に分ける。全 $(j,k)$ に同じ規則を並列適用すれば $Z_S=a\otimes b$ となる。ハミルトニアン流、$S_0$、パルスはすべて可逆であり、保持した供給源、逆演算用補助記憶部、作業領域、時計自由度履歴と逆順操作から逆写像を得る。有限性と誤差はカットオフ構成および式(C.11)から従う。証明終。
<!-- theorem-end:proof -->

## C.4　参照因子と反復持ち上げ

R181Bは未知の係数を外部で読み出すのでなく、入力モードと未使用対象の局所ハミルトニアン結合で積を生成する。従って制御器のプログラムは入力値に依存しない。

第三因子 $c$ に対しては、最初の出力を供給源として同じ乗算器へ入れ、

```math
 (a\otimes b)\otimes c
 =a\otimes b\otimes c
 \tag{C.12}
```

を得る。最初の持ち上げに属する逆演算用補助部／作業領域も捨てない。有限次元の参照因子 $R$ が存在しても、M54が $R$ に作用しなければ全写像は実正準流の恒等拡張となる。

ただし未知の一般状態を複製するとは主張しない。R181Bの入口契約は独立なQ1 接続端に与えられた積入力である。すでに非分離な入力は、前段と同じ永続記憶部内でゲートを継続し、再持ち上げしない。

## C.5　CNOT生成子

2成分部分空間で

```math
 |d_-\rangle=\frac{|10\rangle-|11\rangle}{\sqrt2},
 \qquad
 \Pi_-=|d_-\rangle\langle d_-|
 \tag{C.13}
```

とする。$\Pi_-^2=\Pi_-$ なので

```math
 e^{-i\pi\Pi_-}
 =I+(e^{-i\pi}-1)\Pi_-
 =I-2\Pi_-.
 \tag{C.14}
```

これは $|10\rangle$ と $|11\rangle$ を交換し、$|00\rangle,|01\rangle$ を固定する。よってCNOTに等しい。式(C.1)の正準座標へ展開すると、定数尺度を除いて本文式(4.17)の差モード振動子を得る。

3入力では $K_{AB}$ が各 $c$ 断面の $10c,11c$ を同時に交換し、$K_{BC}$ が各 $a$ 断面の $a10,a11$ を同時に交換する。外部プログラムは $c$ または $a$ を読まず、1つの二次ハミルトニアンを指定する。

## C.6　有限ゲート列の誤差

各ゲートについて大域位相を選び

```math
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \leq\varepsilon_r
 \tag{C.15}
```

とする。ユニタリの作用素ノルムが1であることと望遠鏡和 恒等式から

```math
 \left\|
 \prod_{r=L}^{1}\widetilde U_r
 -e^{i\sum_r\chi_r}
 \prod_{r=L}^{1}U_r
 \right\|_{\rm op}
 \leq\sum_{r=1}^{L}\varepsilon_r.
 \tag{C.16}
```

任意の参照次元について

```math
 \|(\widetilde U_r-e^{i\chi_r}U_r)\otimes I_R\|_{\rm op}
 =
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \tag{C.17}
```

なので同じ評価が成立する。モードまたは経路ごとの誤差を足さず、記憶部全体の作用素ノルムで評価する点が重要である。

式(4.20)の作用窓が交わらず、出口で $g_r=0$ なら、各窓の時間発展を順序積として分けられる。窓間は $H_{\rm hold}$ だけが作用する。状態を別浴へ渡さないので独立の受け渡し誤差はなく、保持、時計自由度、漏れとして一度だけ数える。

<!-- theorem-start:proof -->
**証明（R181C）**

式(C.3)により各有限エルミート生成子は同じ $Z_S$ 上の実正準ハミルトニアン流である。CNOTと3入力の二つのCNOTは式(C.13)、式(C.14)および断面和から従う。非重複時計自由度窓は有限ゲート列の順序積を与え、式(C.16)が合成誤差、式(C.17)が参照系安定性を与える。全期間にわたり $Z_S$ を保持するため、中間復号、選択、再準備はない。証明終。
<!-- theorem-end:proof -->

## C.7　逆演算診断

入力 $|+0\rangle$ にCNOTを作用させた後、2結果間の位相を保つ場合と完全位相緩和する場合を比較する。前者へ逆CNOTとA側Hadamardを作用させると結果は確定的に $|00\rangle$ へ戻る。後者は $|00\rangle$ と $|10\rangle$ を各 $1/2$ で与える。従って完全結果分布の全変動距離は

```math
 \frac12
 \left(
 \left|1-\frac12\right|
 +\left|0-\frac12\right|
 \right)
 =\frac12.
 \tag{C.18}
```

4モードの存在だけではこの干渉縞を保証しない。永続性、相対位相、逆ゲート、末端だけの読出しが必要である。

## C.8　容量固定機構

末端の実信号 $v$ をR112の正準SWAPで未使用保持記憶部 $V$ へ移す。SWAPは同次元の正準置換であり、係数の推定、結果選択、再準備を含まない。

未使用 指針変数 $(A_y,P_y^A)$ に本文式(4.25)を作用させると

```math
 \dot A_y=A_y^\delta(V),
 \qquad
 \dot P_y^A=0.
 \tag{C.19}
```

$P_y^A=0$ では $V$ の方程式に固定機構由来の反作用がない。単位パルス後に

```math
 A_y=J_0
 \left(
 |V_y|^2+\delta q_y\|V\|^2
 \right).
 \tag{C.20}
```

全容量で規格化すると

```math
 \pi_y^\delta(V)
 =\frac{|V_y|^2/\|V\|^2+\delta q_y}{1+\delta}.
 \tag{C.21}
```

よって

```math
 D_{\rm TV}(\pi^\delta(V),\pi^0(V))
 \leq\frac{\delta}{1+\delta}.
 \tag{C.22}
```

$V\mapsto re^{i\phi}V$ は式(C.21)を変えない。

## C.9　末端誤差

理想末端状態方向を $\widehat v$、実際を $\widehat V$ とし、位相を最適化したノルム誤差を

```math
 \inf_\phi\|\widehat V-e^{i\phi}\widehat v\|_2
 \leq\varepsilon_{\rm ray}
 \tag{C.23}
```

とする。純粋状態方向の計算基底分布に対するデータ処理評価から、その全変動距離は $\varepsilon_{\rm ray}$ 以下で抑えられる。正則化は式(C.22)、SWAP、固定機構、作用殻、混合、収集、固定、記録、時計自由度の有限誤差は合計 $\varepsilon_{170}^{\rm end}$ へ一度ずつ数える。無反応を $\varnothing$ として捨てずに含めれば本文R181Dの境界を得る。

<!-- theorem-start:proof -->
**証明（R181D）**

式(C.19)、式(C.20)が信号を壊さない容量固定機構を与え、式(C.21)、式(C.22)が正則化Born比とその誤差を与える。状態方向誤差、末端工程の合成誤差、無反応質量に三角不等式を適用すると本文R181Dの境界を得る。R164、R170の有限作用殻と排他的固定を接続できるという仮定の下で成立する条件付き証明である。証明終。
<!-- theorem-end:proof -->

## C.10　残る接続義務

R181Dを無条件の一体定理へ上げるには次を閉じる必要がある。

- 正準SWAP出口と容量指針変数入口の共通の安全集合
- 指針変数容量からR164作用殻への有限ハミルトニアン境界
- R161/R162の有限ファイバー混合が保つ結果成分間の対称性
- 収集、固定、記録までを含む単一時計自由度による時刻割当
- すべての失敗素子と無反応を含む完全結果空間

これらは一般入力持ち上げや中間のコヒーレント復号器の欠落ではない。R181BとR181Cにより、その二つはそれぞれ明示的持ち上げと同じ永続記憶部上のゲート列へ置き換わった。
