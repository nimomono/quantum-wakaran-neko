@number: C
@chapter: 付録
@title: 可逆tensor-lift、永続gate、末端instrumentの証明
@status: R181B/R181Cを有限正準Hamiltonian構成として証明し、R181Dの条件と誤差境界を分離する。

## C.1　実正準表示

$d$ 個の複素modeに共通作用尺度 $J_C>0$ を取り、

```math
 z_r=\frac{Q_r+iP_r}{\sqrt{2J_C}},
 \qquad
 \{Q_r,P_s\}=\delta_{rs}
 \tag{C.1}
```

とする。Hermitian行列 $h=h^\dagger$ に対する実関数

```math
 H_h=z^\dagger hz
 \tag{C.2}
```

のHamilton方程式は

```math
 iJ_C\dot z=hz.
 \tag{C.3}
```

従って有限次元unitary $U$ は、Hermitian対数 $h$ と有限時間pulseを選ぶことで実正準流として実装できる。global phaseも実正準回転であり、末端Born比には影響しない。

## C.2　乗算pulse

source $a_j,b_k$ とtarget正準対 $(x,\pi^x)$、$(y,\pi^y)$ を考える。lift中のHamiltonianを

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

とする。実部と虚部はsourceの実正準座標の2次多項式なので、式(C.4)は有限次数の実Hamiltonianである。

targetを

```math
 x=y=\pi^x=\pi^y=0
 \tag{C.5}
```

から始め、$\int\chi(\tau)dt=1$ とする。$H_{jk}$ は $x,y$ に依存しないから $\pi^x,\pi^y$ は零のままである。そのためsourceに対するHamilton方程式の右辺も零となり、sourceはblank manifold上で不変である。targetは

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

を満たす。対応する複素modeの変換は

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

Hamiltonian流は拡大位相空間上で1対1である。出力 $Z_S$ だけを残してsource、$G_S$、work、clock履歴を捨てれば見かけ上の非可逆写像になるが、M54はそれらをbath内に保持する。逆順に $S_0^{-1}$ を作用させ、$\chi$ の符号を反転したpulseを通せば式(C.5)へ戻る。

多項式Hamiltonianが大振幅で発散しないよう、安全compact集合 $K$ の近傍で1となる滑らかなcutoff $\eta_K$ を式(C.4)へ掛ける。有限入力次元、有限target数、有限pulse時間では $K$ を通る理想軌道を覆う有限supportを選べる。よって作用、時間、mode数は有限である。

実装Hamiltonian vector fieldを理想場から一様に $\epsilon_X$ だけずらし、同じcompact集合上のLipschitz定数を $L_K$、時間を $T$ とする。Grönwall評価により

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

式(C.4)--式(C.7)が各targetへの積の書込みを与え、式(C.8)、式(C.9)がそれを $Z_{jk}=a_jb_k$ とanti-modeへ正準的に分ける。全 $(j,k)$ に同じ規則を並列適用すれば $Z_S=a\otimes b$ となる。Hamiltonian流、$S_0$、pulseはすべて可逆であり、保持したsource、anti-register、work、clock履歴と逆順操作から逆写像を得る。有限性と誤差はcutoff構成および式(C.11)から従う。証明終。
<!-- theorem-end:proof -->

## C.4　参照因子と反復lift

R181Bは未知の係数を外部で読み出すのでなく、入力modeとblank targetの局所Hamiltonian couplingで積を生成する。従ってcontrollerのprogramは入力値に依存しない。

第三因子 $c$ に対しては、最初の出力をsourceとして同じ乗算器へ入れ、

```math
 (a\otimes b)\otimes c
 =a\otimes b\otimes c
 \tag{C.12}
```

を得る。最初のliftに属するanti/workも捨てない。有限次元の参照因子 $R$ が存在しても、M54が $R$ に作用しなければ全写像は実正準流の恒等拡張となる。

ただし未知の一般状態を複製するとは主張しない。R181Bの入口契約は独立なQ1 portに与えられた積入力である。すでに非分離な入力は、前段と同じ永続register内でゲートを継続し、再liftしない。

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

これは $|10\rangle$ と $|11\rangle$ を交換し、$|00\rangle,|01\rangle$ を固定する。よってCNOTに等しい。式(C.1)の正準座標へ展開すると、定数尺度を除いて本文式(4.17)の差mode oscillatorを得る。

3入力では $K_{AB}$ が各 $c$ sliceの $10c,11c$ を同時に交換し、$K_{BC}$ が各 $a$ sliceの $a10,a11$ を同時に交換する。外部programは $c$ または $a$ を読まず、1つの二次Hamiltonianを指定する。

## C.6　有限gate列の誤差

各gateについてglobal phaseを選び

```math
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \leq\varepsilon_r
 \tag{C.15}
```

とする。unitaryのoperator normが1であることとtelescoping identityから

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

なので同じ評価が成立する。modeまたは経路ごとの誤差を足さず、register全体のoperator normで評価する点が重要である。

式(4.20)の作用窓が交わらず、出口で $g_r=0$ なら、各窓の時間発展を順序積として分けられる。窓間は $H_{\rm hold}$ だけが作用する。状態を別bathへ渡さないので独立のhandoff誤差はなく、hold、clock、leakageとして一度だけ数える。

<!-- theorem-start:proof -->
**証明（R181C）**

式(C.3)により各有限Hermitian生成子は同じ $Z_S$ 上の実正準Hamiltonian流である。CNOTと3入力の二つのCNOTは式(C.13)、式(C.14)およびslice和から従う。非重複clock窓は有限gate列の順序積を与え、式(C.16)が合成誤差、式(C.17)が参照系安定性を与える。全期間にわたり $Z_S$ を保持するため、中間decode、選択、再準備はない。証明終。
<!-- theorem-end:proof -->

## C.7　逆演算診断

入力 $|+0\rangle$ にCNOTを作用させた後、2枝間の位相を保つ場合と完全dephaseする場合を比較する。前者へ逆CNOTとA側Hadamardを作用させると結果は確定的に $|00\rangle$ へ戻る。後者は $|00\rangle$ と $|10\rangle$ を各 $1/2$ で与える。従って完全結果分布の全変動距離は

```math
 \frac12
 \left(
 \left|1-\frac12\right|
 +\left|0-\frac12\right|
 \right)
 =\frac12.
 \tag{C.18}
```

4modeの存在だけではこのfringeを保証しない。永続性、相対位相、逆gate、末端だけの読出しが必要である。

## C.8　容量latch

末端の実信号 $v$ をR112のcanonical SWAPでblank hold-register $V$ へ移す。SWAPは同次元の正準置換であり、係数の推定、枝選択、再準備を含まない。

blank pointer $(A_y,P_y^A)$ に本文式(4.25)を作用させると

```math
 \dot A_y=A_y^\delta(V),
 \qquad
 \dot P_y^A=0.
 \tag{C.19}
```

$P_y^A=0$ では $V$ の方程式にlatch由来のback reactionがない。単位pulse後に

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

理想末端rayを $\widehat v$、実際を $\widehat V$ とし、位相を最適化したnorm誤差を

```math
 \inf_\phi\|\widehat V-e^{i\phi}\widehat v\|_2
 \leq\varepsilon_{\rm ray}
 \tag{C.23}
```

とする。純粋rayの計算基底分布に対するdata-processing評価から、その全変動距離は $\varepsilon_{\rm ray}$ 以下で抑えられる。正則化は式(C.22)、SWAP、latch、shell、mixing、collection、lock、record、clockの有限誤差は合計 $\varepsilon_{170}^{\rm end}$ へ一度ずつ数える。無反応を $\varnothing$ として捨てずに含めれば本文R181Dの境界を得る。

<!-- theorem-start:proof -->
**証明（R181D）**

式(C.19)、式(C.20)が信号を壊さない容量latchを与え、式(C.21)、式(C.22)が正則化Born比とその誤差を与える。ray誤差、末端工程の合成誤差、無反応massに三角不等式を適用すると本文R181Dの境界を得る。R164、R170の有限作用殻と排他的固定を接続できるという仮定の下で成立する条件付き証明である。証明終。
<!-- theorem-end:proof -->

## C.10　残る接続義務

R181Dを無条件の一体定理へ上げるには次を閉じる必要がある。

- canonical SWAP出口と容量pointer入口の共通safe set
- pointer容量からR164作用殻への有限Hamiltonian境界
- R161/R162の有限fiber混合が保つ枝対称性
- collection、lock、recordまでを含む単一clock schedule
- すべてのfailure cellと無反応を含む完全結果空間

これらは一般入力liftや中間coherent decoderの欠落ではない。R181BとR181Cにより、その二つはそれぞれ明示的liftと同じ永続register上のgate列へ置き換わった。
