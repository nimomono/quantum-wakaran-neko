@number: A5
@chapter: 付録
@title: 2モード完全周期の正準構成と誤差上界
@status: M38の共通位相縮約、SU(2) 生成子、Rabi 解、2選択器トーラス、連続性障害、外部記録剪断、外部セル交換 reset、局所時計、完全周期写像を検算可能な形で与える。

## E.1 Hopf 写像の繊維

固定作用面では

```math
b
=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\qquad
|z_1|^2+|z_2|^2=1
```

である。Bloch 成分は

```math
r_x=2\operatorname{Re}(z_1^*z_2),
\qquad
r_y=2\operatorname{Im}(z_1^*z_2),
\qquad
r_z=|z_1|^2-|z_2|^2
```

となる。直接計算すると

```math
r_x^2+r_y^2+r_z^2
=
4|z_1|^2|z_2|^2
+
\left(|z_1|^2-|z_2|^2\right)^2
=1
```

を得る。

$r_z\neq-1$ なら、Bloch ベクトルから代表元を

```math
b(\boldsymbol r)
=
\begin{pmatrix}
\sqrt{(1+r_z)/2}\\
(r_x+ir_y)/\sqrt{2(1+r_z)}
\end{pmatrix}
```

と選べる。南極では $b=(0,1)^{\mathsf T}$ を選ぶ。同じ $\boldsymbol r$ を持つ別の規格化ベクトルはこの代表元の共通位相倍である。従ってHopf 写像の各繊維は $U(1)$ 軌道である。

## E.2 Bloch 成分のPoisson 代数

複素正準振幅は

```math
\{b_j,b_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

を満たす。Hermitian行列 $A,B$ に対し

```math
F_A=b^\dagger A b,
\qquad
F_B=b^\dagger B b
```

と置くと、

```math
\{F_A,F_B\}
=
-\frac{i}{\mathcal J_0}
b^\dagger[A,B]b
```

である。Pauli 行列の交換関係

```math
[\sigma_i,\sigma_j]
=
2i\epsilon_{ijk}\sigma_k
```

を代入すれば

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

が従う。

## E.3 SU(2) 生成子の正準流

$G_{Z,j}$ の時間 $\theta$ の流れは

```math
b_j
\longmapsto
e^{-i\theta}b_j
```

であり、他のモードを変えない。$G_X$ の時間 $\theta$ の流れは

```math
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix}
\longmapsto
e^{-i\theta\sigma_x}
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix}
```

である。相対位相回転

```math
e^{-i\theta\sigma_z/2}
```

は $G_{Z,1}$ と $G_{Z,2}$ に逆符号の半角パルスを加えて得る。従って $Z$--$X$--$Z$ のEuler 分解を各正準流へ置き換えれば、任意の $SU(2)$ を有限パルスで実装できる。

各生成子 $G$ は自身の流れで保存される。時計窓 $g(\tau)$ の面積が目標角に等しければ、パルス形状によらず同じ正準写像を得る。

## E.4 Rabi 回転座標

第4.4節の信号部分は

```math
i\dot b
=
\frac12
\left[
\omega_q\sigma_z
+
\Omega
\left(
\cos\tau_d\,\sigma_x
+
\sin\tau_d\,\sigma_y
\right)
\right]b
```

を与える。恒等式

```math
\cos\tau_d\,\sigma_x
+
\sin\tau_d\,\sigma_y
=
e^{-i\tau_d\sigma_z/2}
\sigma_x
e^{i\tau_d\sigma_z/2}
```

を使い、$b=e^{-i\tau_d\sigma_z/2}c$ と置く。$\dot\tau_d=\omega_d$ なので

```math
i\dot c
=
\frac12
\left[
(\omega_q-\omega_d)\sigma_z
+
\Omega\sigma_x
\right]c
```

となる。定生成子の指数関数

```math
e^{-it(\Delta\sigma_z+\Omega\sigma_x)/2}
=
\cos\frac{\Omega_Rt}{2}\,I
-
i\sin\frac{\Omega_Rt}{2}
\frac{\Delta\sigma_z+\Omega\sigma_x}{\Omega_R},
```

```math
\Omega_R
=
\sqrt{\Delta^2+\Omega^2}
```

を $e_1$ へ作用させれば、第4.4節の遷移公式を得る。

## E.5 任意軸の作用比

規格化信号のBloch 表示は

```math
bb^\dagger
=
\frac12
\left(
I+\boldsymbol r\cdot\boldsymbol\sigma
\right)
```

である。従って

```math
p_s(\boldsymbol n)
=
b^\dagger P_s(\boldsymbol n)b
=
\operatorname{tr}
\left[
bb^\dagger P_s(\boldsymbol n)
\right]
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
```

となる。第1結果 $s$ の後は $\boldsymbol r=s\boldsymbol n$ なので、別軸 $\boldsymbol m$ について

```math
p_t(\boldsymbol m\mid s)
=
\frac{1+st\boldsymbol n\cdot\boldsymbol m}{2}
```

が従う。同軸 $\boldsymbol m=\boldsymbol n$ では反対符号の作用区間長が零になる。

## E.6 2次元トーラスの一意エルゴード性

Poincaré 写像を

```math
R_{\boldsymbol\alpha}(\boldsymbol\vartheta)
=
\boldsymbol\vartheta+2\pi\boldsymbol\alpha
\pmod{2\pi},
\qquad
\boldsymbol\alpha=(\alpha_1,\alpha_2)
```

とする。整数ベクトル $k\in\mathbb Z^2\setminus\{0\}$ に対し

```math
k\cdot\boldsymbol\alpha
\notin
\mathbb Z
```

であることは、$1,\alpha_1,\alpha_2$ の有理数体上の1次独立性と同値である。Fourier 指標の軌道平均は

```math
\frac1N
\sum_{n=0}^{N-1}
e^{ik\cdot(\boldsymbol\vartheta+2\pi n\boldsymbol\alpha)}
\longrightarrow0
```

となる。三角多項式の稠密性から、連続関数の軌道平均はトーラスHaar 積分へ収束する。境界がHaar 零の結果集合についても指示関数近似により長期頻度が得られる。

第1結果集合のHaar 幅は $p_s(\boldsymbol n)$、その安全結果後の第2集合の条件付き幅は $p_t(\boldsymbol m\mid s)$ である。2角の積測度から

```math
P(s,t)
=
p_s(\boldsymbol n)
p_t(\boldsymbol m\mid s)
```

が従う。有限幅で理想結果が変わり得るのは、第1または第2の無反応集合に入る試行だけである。合併上界により

```math
D_{\rm TV}
\leq
P(\mathcal O_{\varnothing,1})
+
P(\mathcal O_{\varnothing,2})
\leq
\delta_1+\delta_2
```

となる。

## E.7 連続性障害

滑らかなHamiltonian $H$ の有限時間流 $\Phi_T$ は、解が存在する領域で微分同相写像である。信号部分への射影を $\pi_{\rm sig}$ とすれば

```math
F
=
\pi_{\rm sig}\circ\Phi_T
```

は連続である。連結集合 $X$ の連続像 $F(X)$ は連結である。相異なる2点だけからなり両点を含む像は非連結なので、全入力を2点だけへ送る滑らかな結果写像は存在しない。

M35とM38では、平坦な安全セクター間に滑らかな遷移領域を置き、その全体を無反応結果とする。従って信号像は遷移領域で連続につながり、定理と矛盾しない。

## E.8 2段写像と逆計算順序

第1測定段の前向き正準写像を $M_1$、第2段を $M_2$、外部記録剪断を $C_R$ とする。第1段のテンプレートを $t_1$、第2段を $t_2$ とし、両方を空準備する。前向き写像は

```math
M_2M_1
```

である。第1安全結果の後の信号を第2段が測定するため、順序を交換してはならない。

記録後の内部逆計算は

```math
M_1^{-1}M_2^{-1}
```

である。合成全体は

```math
\left(M_1^{-1}M_2^{-1}\right)
C_R
\left(M_2M_1\right).
```

記録セルの共役運動量が零なら、$C_R$ は内部変数を変えない。従って内部制限は恒等写像になり、記録座標だけが結果コード分だけ平行移動する。

無反応領域でも $M_1$ と $M_2$ は滑らかな正準写像として定義されているので、同じ逆計算が成立する。離散結果が定義されないことと、逆写像が存在しないことを混同しない。

## E.9 外部記録剪断の正準性

1つの記録セルについて

```math
G_{\rm rec}
=
P^R\Pi(z)
```

とする。Hamilton方程式は

```math
\dot Q^R=\Pi(z),
\qquad
\dot P^R=0,
```

```math
\dot z
=
P^R X_{\Pi}(z)
```

である。$P^R=0$ の理想入口では $z$ が固定され、$Q^R$ だけが移動する。これはHamiltonian 流なので正準性は自動的に成立する。

$|P^R|\leq\sigma_P$ なら、記録窓長を $T_R$、対象領域でのHamiltonian ベクトル場上界を $\|X_\Pi\|\leq K_\Pi$ として

```math
\|\Delta z\|
\leq
T_R\sigma_PK_\Pi
```

を得る。この量を $\varepsilon_{\rm rec}$ の状態誤差へ入れる。

## E.10 外部セル交換と収縮

1つの装置偏差 $a$ と外部偏差 $e$ について

```math
G
=
i\mathcal J_0
\left(a^*e-e^*a\right)
```

とする。交換角を流れ時間 $\phi$ とすれば

```math
\begin{pmatrix}
a^+\\
e^+
\end{pmatrix}
=
\begin{pmatrix}
\cos\phi&\sin\phi\\
-\sin\phi&\cos\phi
\end{pmatrix}
\begin{pmatrix}
a^-\\
e^-
\end{pmatrix}.
```

この行列は直交かつユニタリであり、実正準座標ではシンプレクティックである。$\phi=\pi/2$ では $a^+=e^-$、$e^+=-a^-$ となる。

内部周期後の加法残差を $\xi_n$ とし、

```math
a_{n+1}
=
c a_n+s e_n+\xi_n,
\qquad
c=\cos\phi,
\qquad
s=\sin\phi
```

と書く。$|c|<1$、$\|e_n\|\leq\sigma_E$、$\|\xi_n\|\leq\varepsilon_{\rm cyc}$ なら反復により

```math
\|a_n\|
\leq
|c|^n\|a_0\|
+
\frac{1-|c|^n}{1-|c|}
\left(
|s|\sigma_E+\varepsilon_{\rm cyc}
\right).
```

従って第4.10節の極限上界が従う。

## E.11 作用・角時計の帰還

1つの窓について

```math
H
=
\Omega_cJ_c
+
\Omega_cg(\tau_c)G(z)
```

とする。$\dot\tau_c=\Omega_c$ である。$G$ は自身のHamiltonian 流で保存されるので、窓中の $G$ は一定である。時計作用の変化は

```math
\Delta J_c
=
-\int
\Omega_cg'(\tau_c)G\,dt
=
-G\int g'(\tau_c)\,d\tau_c
=0
```

となる。支持が交わらない複数窓では同じ計算を順に適用できる。

窓が重なる場合、または窓中に別のHamiltonian が $G$ を変える場合はこの厳密帰還を使えない。有限誤差は

```math
|\Delta J_c|
\leq
\int
|g'(\tau_c)|
|G(\tau_c)-G_*|
\,d\tau_c
```

で評価し、時計誤差へ入れる。

## E.12 正準対数

$L=2$ のM35測定段の内訳は次である。

| 対象 | 正準対数 |
|---|---:|
| 信号 | 2 |
| テンプレート | 2 |
| 作用レジスター | 2 |
| 閾値 | 1 |
| 内部記録 | 1 |
| 選択器 | 1 |
| 時計 | 1 |
| 合計 | 10 |

2段では信号と時計だけを共有する。各段の固有部分はテンプレート2、作用2、閾値1、内部記録1、選択器1の7対なので、合計は17対である。

外部交換の14対は、共有信号2対と、各段のテンプレート2、作用2、閾値1、内部記録1を合計した12対からなる。選択器と時計は理想Poincaré 写像の一部なので交換しない。外部記録2対を加え、1周期当たり16対の外部セルを使う。

## E.13 完全周期の誤差合成

誤差を次の4層に分ける。

1. 正準状態誤差 $\varepsilon_z$。
2. 規格化信号方向誤差 $\varepsilon_{\rm dir}$。
3. 比較境界の入力換算移動量 $\Delta_{\rm cmp}$。
4. 結果分布の全変動距離 $\varepsilon_{\rm TV}$。

パルス、時計、記録反作用、逆計算、reset セル幅は最初に $\varepsilon_z$ へ評価する。信号作用が零から離れた領域で規格化写像のLipschitz上界を使い $\varepsilon_{\rm dir}$ へ移す。作用読出しと累積差の微分上界を使って $\Delta_{\rm cmp}$ へ移し、最後に境界近傍のHaar 質量へ変換する。

2段分布について、安全な和上界は

```math
\varepsilon_{\rm TV}
\leq
\delta_1+\delta_2
+
\varepsilon_{\rm op}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm inv}
+
\varepsilon_{\rm rst}
+
\varepsilon_{\rm port}
```

の形になる。右辺の各装置誤差は、前段の変換を通して全変動距離へ換算した後の無次元量を表す。

有限個のパルスと有限個の滑らかな写像だけを使うため、各誤差源を十分小さく選べば任意の $\epsilon>0$ に対して $\varepsilon_{\rm TV}<\epsilon$ と周期末偏差 $<\epsilon$ を同時に満たせる。有限幅を零、時計誤差を零、外部セル幅を零と置いた理想極限では、内部Poincaré 写像は2角の平行移動を除いて恒等写像である。

この証明は、固定プログラムごとに必要な窓数が有限であることを使う。可変プログラム全体、一般有限 $L$、無限記録容量、熱力学的最小コストへ一様な資源上界を与えるものではない。
