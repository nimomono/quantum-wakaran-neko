@number: 2
@chapter: 本文
@title: 有限2成分誘導場と位相接続 Hamiltonian
@status: 有限セルの正準変換、内部回転対称性、保存位相作用、固定作用下の局所作用分配、厳密規格化下の局所chart Hamiltonian、慣性逆恒等式、粒子運動量消去は厳密結果である。正定値2次模型では低速・高速分離と同型補助系への高速成分交換を厳密に示す。半正定値位相 Hessian、有限規格化ペナルティ、非線形再励起、coherent集中、密度同期、単流束化は未完成である。

## 2.1 有限セルから始める理由

有限モード切断した場では、振幅 $r(x)$、位相 $\theta(x)$、局所作用 $j(x)$ は任意の独立関数ではない。切断された場多様体上の従属変数である。そこで、最初に有限個のセルを持つ正準系を定義し、連続表示はその後の近似として扱う。

セル $i=1,\ldots,L$ に2成分正準対

```math
\boldsymbol\Phi_i
=
\begin{pmatrix}
\Phi_{1,i}\\
\Phi_{2,i}
\end{pmatrix},
\qquad
\boldsymbol\Pi_i
=
\begin{pmatrix}
\Pi_{1,i}\\
\Pi_{2,i}
\end{pmatrix}
```

を置く。Poisson 括弧は

```math
\left\{
\Phi_{\alpha,i},
\Pi_{\beta,j}
\right\}
=
\delta_{\alpha\beta}\delta_{ij}.
```

$r_i>0$ の領域で

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix}
```

と書き、

```math
p_{r,i}
=
\boldsymbol\Pi_i\cdot
\frac{\boldsymbol\Phi_i}{r_i},
```

```math
j_i
=
\Phi_{1,i}\Pi_{2,i}
-
\Phi_{2,i}\Pi_{1,i}
```

と定める。

<!-- theorem-start:proposition -->
**命題（有限セル極座標の正準1形式）**
$r_i>0$ の各セルで、

```math
\boldsymbol\Pi_i\cdot d\boldsymbol\Phi_i
=
p_{r,i}\,dr_i
+
j_i\,d\theta_i
```

が成立する。従って $(r_i,p_{r,i})$ と $(\theta_i,j_i)$ は正準対である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
単位ベクトル

```math
e_{r,i}
=
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix},
\qquad
e_{\theta,i}
=
\begin{pmatrix}
-\sin\theta_i\\
\cos\theta_i
\end{pmatrix}
```

を用いると、

```math
d\boldsymbol\Phi_i
=
e_{r,i}\,dr_i
+
r_ie_{\theta,i}\,d\theta_i.
```

$p_{r,i}=\boldsymbol\Pi_i\cdot e_{r,i}$ と $j_i=r_i\boldsymbol\Pi_i\cdot e_{\theta,i}$ を代入すればよい。
<!-- theorem-end:proof -->

## 2.2 場 Hamiltonian と規格化

セル体積を $\Delta V$ とし、場強度を

```math
\mathcal N_\Phi
=
\sum_i r_i^2\Delta V
```

とする。理想縮約では $\mathcal N_\Phi=1$ を用いる。有限装置では、規格化逸脱を

```math
H_{\rm norm}
=
\frac{\lambda_{\rm norm}}{2}
\left(
\mathcal N_\Phi-1
\right)^2
```

でエネルギー的に抑えることができる。ただし $H_{\rm norm}$ は規格化を厳密に保存する制約ではない。厳密な固定規格化sectorを使うか、$\lambda_{\rm norm}$ が大きい観測窓で

```math
\left|
\mathcal N_\Phi-1
\right|
\ll1
```

を誤差として管理する。前者は厳密制約模型、後者は有限ペナルティ模型であり、同じ不変sectorではない。

回転不変な場 Hamiltonian の代表形を

```math
H_{\rm phase}
=
\sum_i
\left[
\frac{p_{r,i}^2}{2M_r}
+
\frac{j_i^2}{2Ir_i^2}
+
U(r_i)
\right]
\Delta V
+
H_{\rm grad}
+
H_{\rm norm}
```

とする。$H_{\rm grad}$ はセル差分に対して内部 $SO(2)$ 回転不変とし、連続極限で少なくとも

```math
H_{\rm grad}
\longrightarrow
\int
\left[
\kappa|\nabla r|^2
+
\kappa_\theta r^2|\nabla\theta|^2
\right]
\,dx
```

を含み得る。本論文の Madelung 縮約では、振幅勾配係数 $\kappa$ を保持し、位相勾配の運動エネルギーは粒子流速側へ整理する。二重計数を避ける係数条件は第3章で明記する。

## 2.3 内部回転対称性と保存作用

全セルを共通角 $\alpha$ だけ回す変換を

```math
\boldsymbol\Phi_i
\longmapsto
R(\alpha)\boldsymbol\Phi_i,
\qquad
\boldsymbol\Pi_i
\longmapsto
R(\alpha)\boldsymbol\Pi_i
```

とする。生成子は

```math
\mathcal J_\phi
=
\sum_i j_i\Delta V.
```

場 Hamiltonian、粒子との結合、外部結合がこの共通回転に不変なら、

```math
\left\{
\mathcal J_\phi,
H_{\rm all}
\right\}
=
0.
```

局所位相勾配があると各 $j_i$ はセル間を流れるため、個別には保存されない。保存されるのは全位相作用 $\mathcal J_\phi$ である。

## 2.4 固定作用下の局所作用分配

規格化 $\mathcal N_\Phi=1$ と全作用 $\mathcal J_\phi$ を固定する。回転エネルギーは

```math
E_{\rm rot}
=
\sum_i
\frac{j_i^2}{2Ir_i^2}
\Delta V.
```

<!-- theorem-start:theorem -->
**定理（固定作用下の局所作用分配）**
$r_i>0$、$\sum_i r_i^2\Delta V=1$、$\sum_i j_i\Delta V=\mathcal J_\phi$ の下で、

```math
E_{\rm rot}
=
\frac{\mathcal J_\phi^2}{2I}
+
\sum_i
\frac{
\left(
j_i-\mathcal J_\phi r_i^2
\right)^2
}{
2Ir_i^2
}
\Delta V.
```

従って固定 $(r_i)$ に対する一意な最小配置は

```math
j_i
=
\mathcal J_\phi r_i^2
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
右辺の平方項を展開すると、

```math
\sum_i
\frac{j_i^2}{2Ir_i^2}\Delta V
-
\frac{\mathcal J_\phi}{I}
\sum_i j_i\Delta V
+
\frac{\mathcal J_\phi^2}{2I}
\sum_i r_i^2\Delta V
+
\frac{\mathcal J_\phi^2}{2I}.
```

2つの制約を代入すると、最後の3項は相殺して $E_{\rm rot}$ が残る。平方項は非負であり、全て零のときだけ最小になる。
<!-- theorem-end:proof -->

この定理はエネルギー地形を定める。閉鎖 Hamiltonian 流が最小配置へ収束することは示さない。第2.5節から第2.7節では、同じ平方項を高速化した有限 Hamiltonian の低速枝と、準備窓だけ作動する有限浴を分けて導入する。

## 2.5 セル体積を吸収した正準変数

特異縮約ではセル体積を正準変数へ吸収する。各セルについて

```math
R_i
=
r_i\sqrt{\Delta V},
\qquad
P_i
=
p_{r,i}\sqrt{\Delta V},
\qquad
J_i
=
j_i\Delta V
```

と定める。このとき正準1形式は

```math
\sum_i
\left(
P_i\,dR_i
+
J_i\,d\theta_i
\right)
```

であり、規格化と全位相作用は

```math
N
=
\sum_iR_i^2,
\qquad
\mathcal J_\phi
=
\sum_iJ_i.
```

局所作用欠陥を

```math
\delta J_i
=
J_i
-
\frac{
\mathcal J_\phi R_i^2
}{
N
}
```

と定める。すると、正規化前にも恒等式

```math
\sum_i
\frac{
\delta J_i^2
}{
R_i^2
}
=
\sum_i
\frac{
J_i^2
}{
R_i^2
}
-
\frac{
\mathcal J_\phi^2
}{
N
}
```

が成立する。$N=1$ では、$\delta J_i=\Delta V(j_i-\mathcal J_\phi r_i^2)$ である。従って、この変数変更は第2.4節の局所作用分配と同じ条件を表し、別の作用を導入しない。

## 2.6 局所作用整合・動径低速 Hamiltonian

$H_0(R,\theta)$ を、位相接続に必要な遅い場エネルギーとする。小さい無次元量 $\epsilon_{\rm s}>0$ を用いて

```math
\begin{aligned}
H_{\epsilon_{\rm s}}
={}&
H_0(R,\theta)
+
\sum_i
\frac{
P_i^2
}{
2\epsilon_{\rm s}M
}
\\
&+
\frac{1}{2\epsilon_{\rm s}I}
\left[
\sum_i
\frac{
J_i^2
}{
R_i^2
}
-
\frac{
\mathcal J_\phi^2
}{
N
}
\right]
+
\frac{\Lambda_N}{2}
\left(
N-1
\right)^2
\end{aligned}
```

とする。固定 $\mathcal J_\phi$ sectorでは、$1/\epsilon_{\rm s}$ を持つ2項は動径運動量と局所作用欠陥に対して正定値である。ただし、$\Lambda_N$ 項は規格化逸脱をエネルギー的に抑えるだけである。以下の正確な消去は、$N=1$ をホロノミック制約として課した単体の局所座標上で行う。有限 $\Lambda_N$ の場合は規格化誤差を別に加える。$\mathcal J_\phi$ は保存量なので固定sectorを取れるが、$N=1$ は別途課した制約である。

```math
q_i
=
R_i^2,
\qquad
\pi_i
=
\frac{
P_i
}{
2R_i
},
\qquad
\sum_iq_i=1.
```

固定全作用の下で $\delta J_i=J_i-\mathcal J_\phi q_i$ と書く。単体の接空間条件 $\sum_i\delta J_i=0$ を課した有限 $\epsilon_{\rm s}$ の Legendre 変換から、

```math
\pi_i
=
\frac{
\epsilon_{\rm s}M
}{
4q_i
}
\dot q_i,
```

```math
\delta J_i
=
\epsilon_{\rm s}Iq_i
\left(
\dot\theta_i
-
\bar\omega
\right),
\qquad
\bar\omega
=
\sum_iq_i\dot\theta_i.
```

を得る。従って消去後の Lagrangian は

```math
\begin{aligned}
L_{\epsilon_{\rm s}}^{\rm red}
={}&
\mathcal J_\phi
\sum_i
q_i\dot\theta_i
-
H_0(q,\theta)
\\
&+
\frac{
\epsilon_{\rm s}M
}{
8
}
\sum_i
\frac{
\dot q_i^2
}{
q_i
}
\\
&+
\frac{
\epsilon_{\rm s}I
}{
2
}
\sum_i
q_i
\left(
\dot\theta_i
-
\bar\omega
\right)^2.
\end{aligned}
```

<!-- theorem-start:proposition -->
**命題（有限特異パラメータの正確な消去）**
$q_i>0$、$\sum_iq_i=1$、固定 $\mathcal J_\phi$ sectorで、上の運動量消去と $L_{\epsilon_{\rm s}}^{\rm red}$ は有限 $\epsilon_{\rm s}$ について正確である。$\dot q_i$ と $\dot\theta_i-\bar\omega$ が $\epsilon_{\rm s}$ に一様に有界な低速枝では、

```math
P_i
=
O
\left(
\epsilon_{\rm s}
\right),
\qquad
\delta J_i
=
O
\left(
\epsilon_{\rm s}
\right).
```
<!-- theorem-end:proposition -->

有限エネルギー上界だけから直接得られるのは、一般に $P_i=O(\sqrt{\epsilon_{\rm s}})$ と $\delta J_i=O(\sqrt{\epsilon_{\rm s}})$ である。$O(\epsilon_{\rm s})$ 評価には有界な低速を仮定する必要がある。また、一般初期値の解が $\epsilon_{\rm s}\to0$ で縮約解へ一様に収束する定理はまだない。

$\epsilon_{\rm s}\to0$ の形式極限では

```math
L_0
=
\mathcal J_\phi
\sum_i
q_i\dot\theta_i
-
H_0(q,\theta)
```

となる。これは局所作用整合と動径低速化を低速枝として説明するが、異なる標本の $(q,\theta)$ を共通代表場へ集中させない。この低速領域を

```math
\mathcal M_{\rm slow}
=
\left\{
P_i=0,
\quad
J_i=\mathcal J_\phi q_i
\right\}
```

と呼び、第2.11節の coherent集中と区別する。

### 2.6.1 単体局所chartと慣性逆恒等式

$n=L-1$ とし、$E^{\mathsf T}E=I_n$、$E^{\mathsf T}\boldsymbol1=0$ を満たす固定行列 $E$ を取る。単体内点 $q^*$ の近傍で

```math
q
=
q^*+E\xi,
\qquad
\boldsymbol\theta
=
\Theta\boldsymbol1+E\varphi
```

と置く。$\xi$ は振幅偏差、$\varphi$ は相対位相、$\Theta$ は共通位相である。共通位相を商で除き、固定 $\mathcal J_\phi$ を課すと、正確な局所 Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{\rm chart}
={}&
H_0(\xi,\varphi)
+
\frac{
2
}{
\epsilon_{\rm s}M
}
p_\xi^{\mathsf T}
G_q^{-1}
p_\xi
\\
&+
\frac{
1
}{
2\epsilon_{\rm s}I
}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right)^{\mathsf T}
G_\varphi^{-1}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right)
\end{aligned}
```

となる。ここで

```math
G_q
=
E^{\mathsf T}
D_q^{-1}
E,
\qquad
G_\varphi
=
E^{\mathsf T}
\left(
D_q-qq^{\mathsf T}
\right)
E,
\qquad
D_q
=
\operatorname{diag}(q)
```

である。単体内点では厳密に

```math
G_q^{-1}
=
G_\varphi
```

が成立する。導出と証明は付録F.1節からF.4節に置く。この結果は有限 $\epsilon_{\rm s}$ で正確だが、節 $q_i=0$ を含む大域chartではない。

### 2.6.2 内点臨界点まわりの2次標準形

```math
\nabla H_0(q^*,\varphi^*)
=
0
```

を満たす内点臨界点の近傍で、慣性行列を基準点に固定し、線形正準変換を行う。2次 Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{(2)}
={}&
\frac{1}{2\epsilon_{\rm s}}
\left[
p_x^{\mathsf T}p_x
+
\left(
p_y-g_\phi x
\right)^{\mathsf T}
\left(
p_y-g_\phi x
\right)
\right]
\\
&+
\frac12x^{\mathsf T}A x
+
x^{\mathsf T}C y
+
\frac12y^{\mathsf T}B y
\end{aligned}
```

となる。

```math
g_\phi
=
\frac{
2\mathcal J_\phi
}{
\sqrt{MI}
}
```

であり、$A$、$B$、$C$ は $H_0$ の振幅、位相、混合 Hessian を正準標準化した行列である。一般には $C\neq0$ である。臨界位相のまわりで

```math
H_0(x,y)
=
H_0(x,-y)
```

が成立するときだけ $C=0$ になる。

$C=0$、$A>0$、$B>0$ なら、十分小さい $\epsilon_{\rm s}$ に対し、$n$ 個の $O(1)$ 低速振動と $n$ 個の

```math
\omega_{{\rm f},k}
=
\frac{
|g_\phi|
}{
\epsilon_{\rm s}
}
+
O(1)
```

高速振動へ厳密に分かれる。低速部分空間上では、1階縮約方程式に対する残差が全時間で $O(\epsilon_{\rm s})$ になる。ただし、軌道の位相差は $O(\epsilon_{\rm s}t)$ と蓄積し得る。

現行の Madelung 縮約では、場側の位相勾配エネルギーを重複させないため、$B$ は半正定値、または零になり得る。従って、この正定値定理を現行 M0 へ無条件に適用しない。半正定値版、有限 $\Lambda_N$ の規格化モード、時間依存基準経路は付録Fで未解決事項として分ける。

### 2.6.3 高速部分空間の可逆交換

正定値2次模型では、高速固有値だけを囲む Riesz 射影により高速symplectic部分空間を定められる。その高速 Hamiltonian と同型の有限補助系を用意し、交換角を

```math
\Theta_{\rm ex}
=
\frac\pi2
```

にすると、補助系が零状態から始まる理想模型では、対象系の高速成分を補助系へ完全に移せる。これは散逸でなく有限正準系間の状態交換である。

この交換は、全セルへ広がる高速射影、同型補助 Hamiltonian、零初期状態、精密な交換角を必要とする。補助系へ移った情報とエネルギーは消えず、反復時には補助系の再初期化が必要である。また、元の全場変数への大域的な持ち上げ、半正定値 $B$、非線形再励起は未完成である。詳細は付録F.8節からF.13節に置く。

## 2.7 準備窓と観測窓の分離

閉鎖系では高速欠陥エネルギーは消えず、有限特異 Hamiltonian だけで一般初期値を $\mathcal M_{\rm slow}$ へ吸引できない。本稿では、役割の異なる2つの準備機構を分ける。

1. 付録Eの有限振幅浴と有限作用交換浴は、セル局所またはグラフ局所に書けるが、欠陥減衰に短記憶・固定振幅・低温近似を使う。
2. 付録Fの同型高速モード交換補助系は、正定値定数係数2次模型では高速成分を厳密に零にできるが、大域的な高速射影と精密調整を必要とする。

内部時計角 $\vartheta$ と滑らかな窓関数 $g_{\rm prep}(\vartheta)$ を使い、どちらも準備窓だけで作動させる。局所浴の全 Hamiltonian と正確な消去は付録E、同型交換の正準計算は付録Fに置く。

作用交換浴は $\theta_i-\theta_k$ の $\cos$ と $\sin$ へ対称に結合する。従って、

1. 全体位相回転に不変で、$\mathcal J_\phi$ を厳密に保存する。
2. 対となる逆項は $\cos^2+\sin^2=1$ により位相固定ポテンシャルを作らない。
3. 固定 $q_i>0$、連結グラフ、短記憶、低温の準備近似では、局所作用欠陥の Lyapunov量を減少させる。
4. 有限浴なので全 Hamiltonian は保存され、対象場から失われた欠陥エネルギーは浴へ移る。

一方、短記憶極限の作用交換浴は相対位相速度へ摩擦を与える。観測中も作動させると、必要な Schrödinger 型位相運動を変える。従って、時間尺度を

```math
\tau_{\rm corr}
\ll
T_{\rm prep}
\ll
T_{\rm slow},
T_{\rm rec}
```

と分離し、観測窓では

```math
g_{\rm prep}
=
0
```

とする。準備後の位相接続運動は $H_{\epsilon_{\rm s}}$ の低速領域で行う。有限温度雑音床、有限浴再帰、窓の切断誤差、観測中の欠陥再成長は第8章で管理する。

これらの機構が直接改善するのは、明記した近似または2次模型の範囲での局所作用欠陥

```math
\varepsilon_j
=
\left\|
j-\mathcal J_\phi r^2
\right\|
```

と動径欠陥 $\varepsilon_{\rm radial}$ である。coherent集中 $\varepsilon_{\rm coh}$、密度同期 $\varepsilon_\rho$、単流束化 $\varepsilon_{\rm press}$、節誤差 $\varepsilon_{\rm node}$ は独立に残る。

## 2.8 位相接続

連続補間した2成分場に対し、

```math
\mathbf a_\varepsilon
=
\frac{
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
}{
|\boldsymbol\Phi|^2+\varepsilon^2
}
```

と定める。極座標では

```math
\mathbf a_\varepsilon
=
\frac{r^2}{r^2+\varepsilon^2}
\nabla\theta.
```

$r>0$ かつ $\varepsilon\to0$ の領域では $\mathbf a_\varepsilon\to\nabla\theta$ である。$r=0$ の節では位相が定義できず、正則化誤差を別に管理する。

粒子の正準対を $(X,P)$ とし、

```math
H_{\rm p}
=
\frac{
\left|
P-\mathcal J_\phi\mathbf a_\varepsilon(X)
\right|^2
}{
2m
}
+
V(X)
```

とする。$\mathcal J_\phi$ は外から置く固定定数ではなく、場の共通内部回転の保存生成子である。固定 $\mathcal J_\phi$ sectorへ制限すると、有効結合定数として働く。

## 2.9 粒子運動量の消去

Hamilton 方程式から

```math
\dot X
=
\frac{
P-\mathcal J_\phi\mathbf a_\varepsilon(X)
}{
m
}
```

なので、

```math
P
=
m\dot X
+
\mathcal J_\phi\mathbf a_\varepsilon(X).
```

<!-- theorem-start:proposition -->
**命題（位相接続 Lagrangian）**
粒子正準運動量を消去すると、

```math
L_{\rm p}
=
\frac m2|\dot X|^2
+
\mathcal J_\phi
\mathbf a_\varepsilon(X)\cdot\dot X
-
V(X)
```

を得る。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$L_{\rm p}=P\cdot\dot X-H_{\rm p}$ へ上の $P$ を代入し、平方を整理する。
<!-- theorem-end:proof -->

節から離れた極限では接続項は

```math
\mathcal J_\phi
\nabla\theta(X)\cdot\dot X.
```

粒子集団の密度 $\rho$ と平均流速 $v$ へ粗視化すると、

```math
\mathcal J_\phi
\int
\rho
v\cdot\nabla\theta
\,dx
```

となる。場の正準項と合わせた物質微分構造は第3章で導く。

## 2.10 時間反転

標準時間反転を

```math
\mathsf T:
\quad
X\mapsto X,
\quad
P\mapsto-P,
\quad
\boldsymbol\Phi\mapsto\boldsymbol\Phi,
\quad
\boldsymbol\Pi\mapsto-\boldsymbol\Pi
```

とする。このとき

```math
\mathcal J_\phi\mapsto-\mathcal J_\phi,
\qquad
\mathbf a_\varepsilon\mapsto\mathbf a_\varepsilon.
```

従って

```math
P-\mathcal J_\phi\mathbf a_\varepsilon
\mapsto
-
\left(
P-\mathcal J_\phi\mathbf a_\varepsilon
\right),
```

であり、$H_{\rm p}$ は不変である。固定符号の $\mathcal J_\phi$ sectorだけを取り出すと時間反転は反対sectorへ写す。全理論は両sectorを含めて時間反転対称である。

## 2.11 coherent集中の意味

連続場の2次モーメントが rank-one に近いことだけでは、非線形比

```math
\frac{
\Phi_1\nabla\Phi_2-\Phi_2\nabla\Phi_1
}{
|\boldsymbol\Phi|^2+\varepsilon^2
}
```

の標本平均を閉じられない。本論文でいう coherent集中は、規格化された各標本が共通の $(r,\theta)$ 近傍に集中し、接続、正準項、勾配エネルギーの非線形平均を同じ代表場で評価できることを含む。

必要な誤差を

```math
\varepsilon_{\rm coh},
\qquad
\varepsilon_{\rm node},
\qquad
\varepsilon_{\rm radial}
```

とし、それぞれ coherent集中、節正則化、動径断熱化からのずれを表す。これらを有限 Hamiltonian 時間発展から一様に小さくする定理は未完成である。

## 2.12 同じ場の対モードと比較モード

複素場表示を

```math
\zeta(x)
=
\Phi_1(x)+i\Phi_2(x)
```

とする。同じ場の固定された直交モードから、Bell 構成に用いる有限個の係数を

```math
\zeta(x)
=
\sum_{\mu=\pm}
\sum_{r=1}^{2}
\left[
z^A_{\mu r}f^A_{\mu r}(x)
+
z^B_{\mu r}f^B_{\mu r}(x)
\right]
+
\sum_{\nu={\rm R},{\rm I}}
c_\nu f^\partial_\nu(x)
+
\zeta_\perp(x)
```

として切り出す。$f^A_{\mu r}$、$f^B_{\mu r}$、$f^\partial_\nu$ は装置の設定と結果に依存しない固定モードである。$\mu$ は局所分析器の2出力、$r$ は2つの直交源チャンネル、$\nu$ は比較振幅の実部と虚部を読む境界モードを表す。

共通内部回転では

```math
z^A_{\mu r}
\longmapsto
e^{i\beta}z^A_{\mu r},
\qquad
z^B_{\nu r}
\longmapsto
e^{i\beta}z^B_{\nu r}.
```

そこで低ランク相関を

```math
C_{\mu\nu}
=
\sum_{r=1}^{2}
\eta_r
z^A_{\mu r}
\left(
z^B_{\nu r}
\right)^*
```

と定める。$C$ は共通内部回転に不変である。従って、中性な比較正準対を用いる第6章の $H_{\rm read}$ は、位相活性部分と同じ保存作用 $\mathcal J_\phi$ を壊さない。

$C$ は独立した正準場ではない。時間発展は

```math
\dot C_{\mu\nu}
=
\sum_r
\eta_r
\left[
\dot z^A_{\mu r}
\left(
z^B_{\nu r}
\right)^*
+
z^A_{\mu r}
\left(
\dot z^B_{\nu r}
\right)^*
\right]
```

として基礎モードの Hamilton 方程式から従う。$C$ に独自の Poisson 括弧または独自の配置空間を与えない。

局所分析器は、共通内部位相 $\beta$ を回すのではなく、各側の出力添字 $\mu$ を実2次元回転する。位相活性モードへの漏出、対モードの損失、比較窓外の結合は独立な交差誤差として第8章で管理する。
