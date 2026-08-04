@number: 6
@chapter: 本文
@title: 共通未来比較器と2モード境界作用殻
@status: 理想比較パルスによる相関振幅の非反作用読み出し、比較総作用と Bell 枝作用の比例、2モード殻容量、比較器の理想逆計算は補助模型内部で厳密である。等方な境界集団と共通境界密度の物理的準備は未完成である。

## 6.1 共通未来の境界比較モード

左右の戻り信号が局所的な有限伝播で合流できる領域は、両測定事象の共通未来にある。比較器は空間全体に瞬間的に共有された自由度ではなく、共通未来のreset領域へ局在した、同じ2成分誘導場の境界集団モードとする。

比較振幅の実部と虚部を読む2つの正準対を

```math
(Q_{\rm R},P_{\rm R}),
\qquad
(Q_{\rm I},P_{\rm I})
```

とする。これらは局所測定中には暗く、比較窓だけ戻りモードへ結合する。

局所結果座標を $s_A,s_B$ とし、結果sectorで1となる滑らかな窓を $\chi_A(s_A)$、$\chi_B(s_B)$ とする。選択された戻り相関振幅を

```math
C(s_A,s_B)
=
\sum_{A,B}
\chi_A(s_A)
\chi_B(s_B)
C_{AB}
```

と定める。排他的な理想sectorでは、1つの履歴について $C(s_A,s_B)=C_{AB}$ である。

## 6.2 理想比較 Hamiltonian

比較読み出しを

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}\operatorname{Re}C(s_A,s_B)
+
P_{\rm I}\operatorname{Im}C(s_A,s_B)
\right]
```

とする。$\vartheta$ は試行周期を制御する時計角である。比較窓の入口条件を

```math
Q_{\rm R}
=
P_{\rm R}
=
Q_{\rm I}
=
P_{\rm I}
=
0
```

とする。

Hamilton 方程式は

```math
\dot Q_{\rm R}
=
g_{\rm read}(\vartheta)
\operatorname{Re}C,
\qquad
\dot Q_{\rm I}
=
g_{\rm read}(\vartheta)
\operatorname{Im}C,
```

```math
\dot P_{\rm R}
=
\dot P_{\rm I}
=
0.
```

入力戻りモード $z$ への反作用は

```math
\dot z\big|_{\rm read}
=
\left\{
z,H_{\rm read}
\right\}
```

であり、右辺は $P_{\rm R}$ または $P_{\rm I}$ に比例する。両運動量は初期に零で、そのまま零なので、理想パルス中の入力モードは変化しない。

<!-- theorem-start:theorem -->
**定理（理想比較読み出し）**
比較窓で他の自由発展を無視でき、$C=C_{AB}$ が一定なら、

```math
\Gamma
=
\int_{\rm read}
g_{\rm read}(t)\,dt
```

に対して

```math
Q_{\rm R}^{\rm out}
=
\Gamma\operatorname{Re}C_{AB},
\qquad
Q_{\rm I}^{\rm out}
=
\Gamma\operatorname{Im}C_{AB},
```

```math
P_{\rm R}^{\rm out}
=
P_{\rm I}^{\rm out}
=
0
```

が厳密に成立する。理想パルス中、入力戻りモードは変化しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$P_{\rm R}=P_{\rm I}=0$ は Hamilton 方程式により保存されるため、入力モードへの反作用は零である。従って $C$ は比較結合によって変化しない。$Q_{\rm R}$ と $Q_{\rm I}$ の方程式を比較窓で積分する。
<!-- theorem-end:proof -->

$C$ は共通内部回転に不変なので、中性な比較正準対を用いた $H_{\rm read}$ も共通内部回転に不変である。従って理想比較は保存位相作用 $\mathcal J_\phi$ を壊さない。

## 6.3 比較総作用

比較2モードの作用を

```math
J_{\rm R}
=
\frac12
\left(
Q_{\rm R}^2+P_{\rm R}^2
\right),
\qquad
J_{\rm I}
=
\frac12
\left(
Q_{\rm I}^2+P_{\rm I}^2
\right)
```

とし、総作用を

```math
A_\partial
=
J_{\rm R}+J_{\rm I}
```

とする。

<!-- theorem-start:corollary -->
**系（比較作用への転送）**
理想比較読み出し後の結果sector $(A,B)$ では、

```math
A_\partial^{AB}
=
\frac{\Gamma^2}{2}
|C_{AB}|^2
=
\frac{\Gamma^2}{2}K_{AB}.
```
<!-- theorem-end:corollary -->

第5章の余弦作用を代入すると、

```math
A_\partial^{AB}
=
\frac{\Gamma^2\mathcal K}{8}
\left[
1-AB\cos\Delta_{ab}
\right].
```

旧3モード模型の基準作用 $J_*$ は現れない。結果依存作用を比較2モードの総作用へ直接転送するからである。

## 6.4 2モード内部の作用保存混合

複素比較モードを

```math
c_\partial
=
\begin{pmatrix}
c_{\rm R}\\
c_{\rm I}
\end{pmatrix},
\qquad
c_\nu
=
\frac{
Q_\nu+iP_\nu
}{
\sqrt2
}
```

とする。$A_\partial=c_\partial^\dagger c_\partial$ である。

同じ誘導場の未読暗モード $z_{\rm D}$ が混合角を供給する候補 Hamiltonian を

```math
H_{\rm mix}
=
g_{\rm mix}(\vartheta)
\sum_\alpha
\xi_\alpha(z_{\rm D})
c_\partial^\dagger
T_\alpha
c_\partial
```

とする。$T_\alpha$ は $u(2)$ の Hermitian 生成子である。

<!-- theorem-start:proposition -->
**命題（比較総作用の保存）**
暗モード変数が比較正準対と独立なら、

```math
\left\{
A_\partial,
H_{\rm mix}
\right\}
=
0.
```
<!-- theorem-end:proposition -->

従って混合は比較2モード殻に接し、$A_\partial^{AB}$ を変えない。

暗モードの初期角度集団と制御された $U(2)$ 変換の押し出しが Haar 分布を与えるなら、各固定 $A_\partial^{AB}$ 殻上で一様な角分布を準備できる。ただし、単一位相点の決定論的 Hamiltonian 発展が確率分布を無から生成するわけではない。必要なのは暗モードを含む初期集団の準備である。

## 6.5 2モード殻容量

一般作用殻定理の $n=2$ の場合から、

```math
\Omega_2(A)
=
(2\pi)^2A,
\qquad
A>0.
```

従って、

```math
\Omega_2
\left(
A_\partial^{AB}
\right)
=
(2\pi)^2
\frac{\Gamma^2}{2}
K_{AB}.
```

<!-- theorem-start:corollary -->
**系（Bell 比較殻の線形容量）**
理想比較模型では、

```math
\Omega_2^{AB}
\propto
K_{AB}.
```
<!-- theorem-end:corollary -->

比較に直接参加する作用分配方向は、実部と虚部を受ける2モードだけでなければならない。追加暗モードが $A_\partial^{AB}$ を直接分配すると、$n>2$ の一般式により容量は $K_{AB}$ の高いべきとなる。追加自由度は混合角、時計、位相保持、記録、garbageだけを担う。

## 6.6 読み出し写像、混合、境界測度の区別

3つの操作を区別する。

1. $H_{\rm read}$ は、空の比較器を固定殻上の1点へ移す。
2. $H_{\rm mix}$ は、準備された集団を同じ殻上で混ぜる。
3. 境界測度は、異なる結果sectorと異なる殻の間に未規格化質量を置く。

1と2は Hamiltonian 写像である。正規化された各sectorの集団 $\mu_{AB}$ に対し、

```math
\mu_{AB}
\longmapsto
\left(
\mathcal U_{AB}
\right)_*
\mu_{AB}
```

としても、

```math
\left(
\mathcal U_{AB}
\right)_*
\mu_{AB}
\left(
\Gamma^{AB}
\right)
=
\mu_{AB}
\left(
\Gamma^{AB}
\right)
```

である。従って、読み出しと $U(2)$ 混合だけでは、sector総質量を $\Omega_2(A_\partial^{AB})$ に比例させられない。

Bell 重みには、比較殻上へ全sector共通の未規格化密度または流束を置く境界準備条件が別に必要である。この条件を第7章で明示する。殻容量と頻度を同一視しないことが、本改訂の中心的な制限である。

## 6.7 有限パルスと初期条件の誤差

理想読み出しからの主なずれは次である。

- 比較器の初期座標 $Q_\nu^{\rm in}$。
- 比較器の初期運動量 $P_\nu^{\rm in}$。
- 比較中の入力モード自由発展。
- 比較モード自身の自由発展。
- 有限幅の結果窓 $\chi_A,\chi_B$。
- 戻りモードの損失、分散、交差混合。
- 時計パルス面積 $\Gamma$ の試行差。

相対誤差を $\varepsilon_{\rm pulse}$ とまとめると、

```math
A_\partial^{AB}
=
\frac{\Gamma^2}{2}
K_{AB}
\left[
1+O(\varepsilon_{\rm pulse})
\right]
+
A_{\rm bg}^{AB}.
```

$A_{\rm bg}^{AB}$ は初期比較振幅と非理想自由発展から生じる背景作用である。結果依存の背景は余弦可視度だけでなく周辺対称性も壊し得る。

理想式で $K_{AB}=0$ となるsectorは殻の端にある。有限分解能、初期比較幅、読み出し雑音があると零作用の点に有限背景が生じるため、端点近傍は独立に評価する。

## 6.8 時計と1回の比較窓

時計正準対を $(\vartheta,I_\vartheta)$ とし、

```math
H_{\rm clk}
=
\Omega I_\vartheta
```

とする。すると $\dot\vartheta=\Omega$ である。各相互作用を時計角の互いに重ならない窓関数 $g_k(\vartheta)$ で作動させる。

比較反応面を

```math
\Gamma_\partial
=
\left\{
\vartheta=\vartheta_\partial,
\quad
\dot\vartheta>0
\right\}
```

とする。1周期に時計角が1度だけこの面を横切る構成なら、比較イベントの重複計数を防げる。ただし、全初期履歴がこの面へ到達することと、結果別に失敗履歴を捨てないことは別に監査する必要がある。

## 6.9 局所記録と比較の順序

左右の指針を $(Y_A,\Pi_A)$、$(Y_B,\Pi_B)$ とする。局所記録 Hamiltonian の代表形を

```math
H_{\rm rec}
=
-g_A(\vartheta)Y_A\sigma_A(s_A)
-
g_B(\vartheta)Y_B\sigma_B(s_B)
```

とする。パルス面積を1に規格化すれば、理想sectorで

```math
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B
```

を得る。

この記録は、戻り信号が共通未来比較器へ到達する前に局所的に作れる。比較器は記録内容を前向きに変更しない。共同頻度に比較作用を使うには、試行全体へ置く二側境界測度として解釈しなければならない。

## 6.10 可逆な比較器逆計算

境界通過後、結果を空の外部記録セル $(M_A,M_B)$ へ可逆にコピーする。その後、

1. $U(2)$ 混合を逆実行する。
2. 比較読み出しを $-H_{\rm read}$ で逆実行する。
3. 戻り伝達を逆実行する。
4. 局所分析器を逆実行する。
5. 内部指針と結果座標を基準状態へ戻す。

混合の制御履歴と暗モード状態を保持し、正確な逆変換を実行できる理想模型では、読み出し前の

```math
Q_{\rm R}
=
Q_{\rm I}
=
P_{\rm R}
=
P_{\rm I}
=
0
```

へ戻る。入力戻りモードは理想読み出しで乱されていないため、比較器の逆計算は有限 Hamiltonian で構成できる。

ただし、異なる結果を外部に残したまま、外部記録も含む全自由度を同じ1点へ戻すことはできない。Hamiltonian flowは1対1だからである。反復には、大きな記録テープ、garbageモード、仕事源、弱く結合した環境のいずれかが必要である [17,18]。

## 6.11 自律的な全 Hamiltonian

試行周期の有限部分は概略

```math
\begin{aligned}
H_{\rm cycle}
={}&
H_{\rm particles}
+
H_{\rm field}
+
H_{\rm prep}
+
H_{\rm source}
+
H_{\rm analyzer}
+
H_{\rm pointer}\\
&
+
H_{\rm return}
+
H_{\rm read}
+
H_{\rm mix}
+
H_{\rm memory}
+
H_{\rm reset}
+
H_{\rm clk}
\end{aligned}
```

と書ける。外部時間依存を時計角依存 $g_k(\vartheta)$ へ置換し、時計と仕事源を全系に含めれば、自律的な有限 Hamiltonian として表現できる。

$H_{\rm prep}$ は、付録Eの有限振幅浴・作用交換浴と、付録Fの高速部分・同型補助部分・交換結合を含み得る。観測窓ではこれらを切り離す。高速交換補助系へ移った情報とエネルギーは、比較器の理想逆計算では消えないため、試行間の再初期化対象に含める。

本章は各項の理想部分と順序を与えるが、全ての窓を同時に滑らかで有限幅にし、交差誤差、記録安定性、境界測度準備、長期resetを一様に制御する完成模型は与えない。

## 6.12 本章の結論

共通未来の2つの境界比較モードは、Bell 相関振幅の実部と虚部を、入力戻りモードを理想的には乱さず比較総作用へ転送する。その2モード殻容量は $K_{AB}$ に線形であり、旧3モード模型の基準作用を必要としない。

一方、Hamiltonian 読み出しと殻内混合は、結果sector間の確率質量を作らない。Bell 頻度には共通境界測度の準備が別に必要である。
