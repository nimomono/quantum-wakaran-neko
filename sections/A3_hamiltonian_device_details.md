@number: A3
@chapter: 付録
@title: 構造化誘導場、U(3) 殻拡散、境界ファイバー体積
@status: 配置拡散浴の運動量結合方向と測定器の座標結合方向を含む固定射影について、静的基底、全交差応答、和・差変換、作用保存、固定殻体積、coarea 計算を補足する。誘導場から等方拡散への縮約は候補構成であり、未完成である。

## C.0 拡大全系とエネルギー収支

測定器と境界作用殻を含む拡大全系を

```math
H_{\rm all}
=
H_{\rm src}
+
H_{\rm set}
+
H_{\rm loc}
+
H_{\rm ptr}
+
H_{\rm med}
+
H_\partial
+
H_{\rm fin-link}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

と書く。各項の役割は次である。

| 項 | 役割 |
|---|---|
| $H_{\rm src}$ | 固定総入力作用と位相基準を持つ伝達ベクトル対の準備 |
| $H_{\rm set}$ | 左右の設定制御器 |
| $H_{\rm loc}$ | 局所結果形成または最小結果符号化 |
| $H_{\rm ptr}$ | 固定指針への記録 |
| $H_{\rm med}$ | 左右局所反応座標、共通境界反応座標、暗モードを含む1つの構造化誘導場 |
| $H_\partial$ | 境界3モードの自由運動と弱い混合 |
| $H_{\rm fin-link}$ | 有限装置部分内の結合 |
| $H_{\rm ext}$ | 外部環境 |
| $\varepsilon_{\rm ext}H_{\rm link}$ | 常時のごく弱い漏れと流入 |
| $H_{\rm work}$ | 設定変更、記録消去、再初期化の仕事源 |

全 Hamiltonian に明示的な時間依存性がなければ、拡大全エネルギーは保存される。一方、有限装置部分

```math
H_{\rm fin}
=
H_{\rm all}
-
H_{\rm ext}
-
H_{\rm work}
```

の収支は

```math
\frac{dH_{\rm fin}}{dt}
=
\left\{
H_{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
\right\}.
```

実験室の記号では、

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}.
```

閉鎖補助モデルは $\varepsilon_{\rm ext}=0$ とし、仕事源を有限装置へ含めた短時間窓で用いる。現行モデルでは $\varepsilon_{\rm ext}$ を常時零にせず、測定窓内の相対エネルギー変化を小さい量として評価する。

## C.1 静的誘導場基底の正準性

浴座標を $Q,\Pi\in\mathbb R^N$ とし、

```math
H_{\rm med}
=
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

とする。$K$ は正定値実対称行列である。

第5章の粒子運動量結合方向を $\operatorname{Ran}C_N^{\mathsf T}$ とする。局所装置と境界装置が浴座標へ結合する方向を

```math
c_A,
\quad
c_B,
\quad
c_{\partial,1},
\ldots,
c_{\partial,m}
```

とする。$\operatorname{Ran}C_N^{\mathsf T}$ とこれらの座標結合方向が張る部分空間の正規直交基底を先頭に並べる直交行列 $O$ を固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde\Pi=O\Pi
```

と変換する。

<!-- theorem-start:proposition -->
**命題（直交浴基底変換の正準性）**
$O^{\mathsf T}O=I$ なら、$(Q,\Pi)\mapsto(\widetilde Q,\widetilde\Pi)$ は正準変換である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
正準1形式は

```math
\Pi^{\mathsf T}dQ
=
\widetilde\Pi^{\mathsf T}
O
O^{\mathsf T}
d\widetilde Q
=
\widetilde\Pi^{\mathsf T}d\widetilde Q
```

と保存される。従ってシンプレクティック2形式も保存される。
<!-- theorem-end:proof -->

変換後の2次形式は

```math
H_{\rm med}^{(2)}
=
\frac12\widetilde\Pi^{\mathsf T}\widetilde\Pi
+
\frac12
\widetilde Q^{\mathsf T}
\widetilde K
\widetilde Q,
\qquad
\widetilde K
=
OKO^{\mathsf T}.
```

結合方向に適合した基底を取っても、$\widetilde K$ は一般にブロック対角ではない。局所、境界、暗モード間の動的結合は $\widetilde K$ の非対角ブロックと $V_{\rm nl}$ に残る。運動量結合と座標結合が同じ明部分空間にあるため、自由回転後には両者の混合応答も一般に残る。

従って、

```math
H_{\rm med}
=
H_A^{\rm loc}
+
H_B^{\rm loc}
+
H_\partial^{\rm glob}
+
H^{\rm dark}
+
H_{\rm cross}
```

という分解は、正準座標の厳密な分類と、動力学的な近似直和を分けて読む必要がある。

## C.2 線形応答核

装置の座標結合だけに対する線形誘導場の運動方程式は

```math
\ddot Q+KQ
=
-\epsilon_Ac_Ax_A
-\epsilon_Bc_Bx_B
-\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

ここで $F_\alpha$ は境界モードから浴へ加わる一般化力である。初期値解は

```math
Q(t)
=
\cos
\left(
K^{1/2}t
\right)Q(0)
+
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)\Pi(0)
```

```math
\quad
-
\int_0^t
K^{-1/2}
\sin
\left[
K^{1/2}(t-s)
\right]
F_{\rm dev}(s)\,ds,
```

```math
F_{\rm dev}
=
\epsilon_Ac_Ax_A
+
\epsilon_Bc_Bx_B
+
\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

A側の一般化力 $c_A^{\mathsf T}Q(t)$ にB側の $x_B$ が与える寄与は

```math
-\epsilon_B
\int_0^t
\chi_{AB}(t-s)x_B(s)\,ds,
```

```math
\chi_{AB}(t)
=
c_A^{\mathsf T}
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)
c_B.
```

同様に $\chi_{BA}$ を得る。従って、$c_A^{\mathsf T}c_B=0$ でも $\chi_{AB}(t)$ は一般に零ではない。$K$ が $c_A,c_B$ の張る部分空間を別々に不変にするときだけ、座標–座標の線形交差応答は厳密に消える。

第5章の $P^{\mathsf T}C_N\Pi$ を同時に含めると、$Q$ と $\Pi$ の自由回転を通じて運動量–座標混合核も生じる。局所性の判定には、各核をまとめた応答作用素 $\mathcal R_{XY}(t)$ を使う。

局所測定窓 $0\leq t\leq T_{\rm meas}$ で

```math
\varepsilon_{\rm loc}
=
\frac{
\sup_t
\max
\left(
\|\mathcal R_{AB}(t)\|,
\|\mathcal R_{BA}(t)\|
\right)
}{
\sup_t
\min
\left(
\|\mathcal R_{AA}(t)\|,
\|\mathcal R_{BB}(t)\|
\right)
}
```

を用いる理由はここにある。非線形補正については、指定した準備領域のまわりで変分方程式を解き、同じ比を定義する。

## C.3 局所結果符号化の生成子

結果種座標を $s_X$、伝達ベクトルを $(Q_X,P_X)$、応答モードを $(x_X,p_X)$ とする。平坦結果領域上で $\sigma(s_X)=X\in\{-1,+1\}$ とする。

局所分析の生成子を

```math
K_X^{\rm an}
=
-
\left[
\phi(a_X)
+
\pi\chi_-(s_X)
\right]
I_X
-
x_X\sigma(s_X),
```

```math
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
\chi_-(s)
=
\frac{
1-\sigma(s)
}{
2
}
```

とする。生成子の単位流れで、

```math
u_X^{\rm out}
=
X R[\phi(a_X)]u_X^{\rm in},
\qquad
p_X^{\rm out}
=
p_X^{\rm in}+X.
```

$p_X^{\rm in}=0$ なら $p_X^{\rm out}=X$ である。

固定指針対を $(Y_X,\Pi_X)$ とし、平坦関数 $\zeta(p_X)$ が $p_X=\pm1$ の近傍で $\pm1$ を取るとする。転写生成子

```math
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
```

の単位流れは

```math
\Pi_X^{\rm out}
=
\Pi_X^{\rm in}
+
\zeta(p_X).
```

$\Pi_X^{\rm in}=0$ なら $\Pi_X^{\rm out}=X$ となる。

自由 Hamiltonian と幅 $\tau_{\rm pulse}$ のパルスが同時に働く場合、理想単位流れとの差は、有界な適用領域で

```math
O(\varepsilon_{\rm pulse}),
\qquad
\varepsilon_{\rm pulse}
=
\tau_{\rm pulse}
\sup_{\mathcal K}
\left\|
X_{H_0}
\right\|
```

と評価する。局所誘導場の交差応答も加えると、指針の誤差は

```math
O
\left(
\varepsilon_{\rm pulse}
+
\varepsilon_{\rm loc}
+
\varepsilon_{\rm open}
\right).
```

この補助装置は既存の結果種を記録するだけであり、一般測定器ではない。

## C.4 和・差基底の正準性

左右伝達ベクトルを正準対 $(Q_A,P_A)$、$(Q_B,P_B)$ とする。和・差座標を

```math
Q_\pm
=
\frac{
Q_A\pm Q_B
}{
\sqrt2
},
\qquad
P_\pm
=
\frac{
P_A\pm P_B
}{
\sqrt2
}
```

と定める。

<!-- theorem-start:proposition -->
**命題（和・差変換の正準性）**
上の変換は正準であり、

```math
P_A\,dQ_A
+
P_B\,dQ_B
=
P_+\,dQ_+
+
P_-\,dQ_-.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
変換行列

```math
U
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
```

は直交行列である。座標と運動量へ同じ $U$ を作用させるため、C.1節と同じ計算で正準1形式が保存される。
<!-- theorem-end:proof -->

和・差作用は

```math
I_\pm
=
\frac12
\left(
Q_\pm^2+P_\pm^2
\right)
=
\frac14
\left\|
u_A\pm u_B
\right\|^2.
```

直交性から、

```math
I_++I_-
=
I_A+I_B.
```

設定と結果は $I_+-I_-$ に入るが、総入力作用には入らない。

固定された $U$ は1つの正準写像であり、測度を生成しない。入力集団が Liouville 測度を持てば保存するが、単一入力を一様集団へ変えない。

## C.5 3モード作用と U(3) 生成子

境界3モードを複素正準変数

```math
a
=
\begin{pmatrix}
a_+\\
a_s\\
a_r
\end{pmatrix},
\qquad
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
}
```

で表す。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とする。総作用は

```math
C
=
a^\dagger a.
```

$T_\alpha$ を $u(3)$ の Hermitian 基底とし、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を Hamiltonian 生成子とする。$L_\alpha$ の流れは

```math
\dot a
=
-iT_\alpha a
```

であり、

```math
\left\{
C,L_\alpha
\right\}
=
0.
```

従って全ての $U(3)$ 生成子は総作用殻に接する。

構造化誘導場の未読変数 $\xi_\alpha(z_{\mathcal B})$ と弱く結合する候補 Hamiltonian を

```math
H_{\rm iso-link}
=
\epsilon_{\rm iso}
\sum_{\alpha=1}^{9}
\xi_\alpha(z_{\mathcal B})
L_\alpha(a)
```

とする。各瞬間の全 Hamiltonian 流れは $C$ を保存する。

浴相関が準備窓で

```math
\left\langle
\xi_\alpha(t)
\xi_\beta(0)
\right\rangle
\simeq
\delta_{\alpha\beta}
\kappa(t)
```

となり、相関時間が境界モードの緩和時間より短いとする。弱結合・長時間尺度での2次縮約生成子は概念的に

```math
\mathcal L_{\rm eff}
=
D_\partial
\sum_{\alpha=1}^{9}
X_{L_\alpha}^2
```

となる。同次空間 $U(3)/U(2)$ 上では、この Casimir 作用素は規格化を除いて $\Delta_{S^5}$ に一致する。

この縮約には、少なくとも次の近似が必要である。

1. $\epsilon_{\rm iso}\ll1$ の弱結合。
2. 浴相関時間と準備時間の分離。
3. 9方向の相関行列の等方性。
4. 有限誘導場の再帰時間より短い準備窓。
5. 外部交換による長時間再位相化の抑制。

本論文は、特定の有限 $V_{\rm nl}$ と外部結合について、これらの条件から $\mathcal L_{\rm eff}$ への一様誤差上界を証明しない。従ってこれはミクロ実現候補であり、導出済みの定理ではない。

## C.6 等方拡散の定常測度

固定殻 $S_{C_0}^5$ 上の密度 $f$ が

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

に従うとする。定常解は

```math
\Delta_{S^5}f=0
```

を満たす。部分積分により、

```math
0
=
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

従って $f$ は定数であり、規格化すれば $f=1$ である。

異方摂動を

```math
\mathcal L_\varepsilon
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_1
```

とする。$\mathcal L_1$ が質量を保存し、等方生成子のスペクトルギャップに対して相対有界なら、定常密度の形式展開は

```math
f_\varepsilon
=
1
-
\frac{
\varepsilon_{\rm aniso}
}{
D_\partial
}
\left(
\Delta_{S^5}
\right)^{-1}_{0}
\mathcal L_1^*1
+
O
\left(
\varepsilon_{\rm aniso}^2
\right)
```

となる。逆作用素の添字0は平均零部分空間への制限である。この式は、異方性の影響が結合定数だけでなくスペクトルギャップに依存することを示す。

## C.7 固定殻体積と周辺密度

作用角変数で、3モード固定殻の未規格化体積は

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^\infty dJ_+
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-J_+-J_s-J_r
\right).
```

$J_r$ を積分すると、$J_+,J_s\geq0$ かつ $J_++J_s\leq C_0$ の三角形が残る。従って、

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^{C_0}dJ_+
\int_0^{C_0-J_+}dJ_s
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

$J_+=x$ の未規格化周辺は

```math
\omega_+(x)
=
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
```

```math
=
(2\pi)^3
\left(
C_0-x
\right)
\mathbf1_{\{0\leq x\leq C_0\}}.
```

従って、

```math
p_+(x)
=
\frac{
\omega_+(x)
}{
\Omega_3(C_0)
}
=
\frac{
2(C_0-x)
}{
C_0^2
}.
```

固定 $x$ の条件付き分布では、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac1{C_0-x}
```

である。条件付き密度の $1/(C_0-x)$ と、ファイバー総質量の $C_0-x$ を混同してはならない。

## C.8 coarea と境界ファイバー

一般の境界正準位相空間を $\Gamma_\partial$、基準体積を $d\Gamma_\partial$ とする。2つの制約を

```math
F_1
=
C_0-J_+-J_s-J_r,
```

```math
F_2
=
J_+-I_+^{AB}
```

とする。理想線形モデルでは、

```math
W_{AB}
\propto
\int_{\Gamma_\partial}
\delta(F_1)
\delta(F_2)
d\Gamma_\partial.
```

作用角座標に変換すると、変換 Jacobian は1である。$J_+$ と $J_r$ のデルタ関数積分を行えば、

```math
W_{AB}
\propto
(2\pi)^3
\int_0^{C_0-I_+^{AB}}dJ_s
```

```math
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right).
```

一般の滑らかな境界写像 $F=(F_1,F_2)$ では coarea 公式により、

```math
\int_{\Gamma_\partial}
\rho(z)
\delta
\left(
F(z)
\right)
d\Gamma_\partial
=
\int_{F^{-1}(0)}
\frac{
\rho(z)
}{
J_F(z)
}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

理想作用座標では $J_F$ が結果と設定に共通な定数へなる。非線形境界写像、分岐、caustic、解多重度がある場合は、この単純化を使えない。同じ巨視的結果へ対応する複数の解は、その局所 Jacobian と多重度を含めて数える。

## C.9 有限分解能の展開

偶関数 $K$ を

```math
\int_{\mathbb R}K(y)\,dy=1,
\qquad
\int_{\mathbb R}yK(y)\,dy=0
```

と規格化し、

```math
K_{\delta_J}(y)
=
\frac1{\delta_J}
K
\left(
\frac y{\delta_J}
\right)
```

とする。$J_+$ 周辺密度 $p_+(x)$ は殻内部で線形なので、窓が殻端に触れない限り、

```math
\int
p_+(x)
K_{\delta_J}(x-I_+)\,dx
=
p_+(I_+)
```

が偶対称窓では厳密に成り立つ。一般の滑らかな Jacobian または殻幅分布を含めると、

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
\delta_J^2
\sup
\left|
\partial_{J_+}^2
\frac{\rho}{J_F}
\right|
\right).
```

従って、理想線形作用殻では有限分解能自体が1次の角度誤差を生まない。主要な分解能誤差は、殻端の切断、非線形 Jacobian、結果依存窓、総作用幅との重なりから生じる。

## C.10 半径方向の弱開放力学

総作用 $C$ の縮約式を

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

とする。定常密度は

```math
\rho_C(C)
\propto
\exp
\left[
-
\frac{
\gamma_C
}{
2D_C
}
\left(
C-C_0
\right)^2
\right],
```

その分散は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C}
```

である。

この式は、外部への漏れと流入を線形化した縮約候補である。基礎 Hamiltonian の総エネルギーが確率的に失われると仮定したものではない。外部環境と仕事源を消去した有限部分の有効式として読む。

角方向と半径方向が近似的に分離する条件を

```math
\tau_{\rm corr}
\ll
\tau_{\rm mix}
\ll
\tau_C,
\qquad
\tau_C=\gamma_C^{-1}
```

とする。$\tau_{\rm corr}$ は浴相関時間、$\tau_{\rm mix}$ は殻接方向混合、$\tau_C$ は半径変化である。$\tau_{\rm mix}\ll\tau_C$ なら、各半径で方向分布が先に等方化する。

純粋漏れでは

```math
dC_t=-\gamma_CC_t\,dt
```

となり、非零の定常殻は存在しない。流入または仕事源を含む復元項は、作用殻準備に不可欠である。

## C.11 ミクロ構成から未導出の事項

本付録で厳密に示したのは次である。

- 運動量結合方向と座標結合方向を含む1つの有限誘導場に対する静的な直交正準基底。
- 装置の座標–座標交差応答核と、混合応答を含めた全応答作用素の定義。
- 最小結果符号化器の理想正準写像。
- 和・差変換の正準性と作用保存。
- $U(3)$ Hamiltonian 生成子が総作用を保存すること。
- 3モード固定作用殻の体積、周辺密度、残余ファイバー体積。
- 理想線形境界写像の共通 coarea Jacobian。

次は未導出である。

- 特定の有限非線形浴が必要な時間窓で等方な相関行列を持つこと。
- 有限誘導場と常時の外部交換から $D_\partial\Delta_{S^5}$ を一様誤差付きで得ること。
- 異方誤差、混合時間、再帰時間を同じパラメータから同時に閉じること。
- 運動量–座標混合核を含む左右全交差応答を、Bell 測定窓で一様に抑えること。
- 半径方向の復元式とエネルギー収支を明示的な外部 Hamiltonian から導くこと。
- 一般測定器、境界適合、記録、消去、再初期化を1本の有限幅 Hamiltonian へ統合すること。

従って、作用殻の幾何計算は厳密結果、全殻拡散と半径安定化は縮約候補、現行の弱開放モデルへの接続は近似または予想・未解決として扱う。
