@number: 2
@chapter: 本文
@title: 有限2成分誘導場と位相接続 Hamiltonian
@status: 有限セルの正準変換、内部回転対称性、保存位相作用、固定作用下の局所作用分配、粒子運動量消去は厳密結果である。同じ場の位相・対・比較モード分解は固定射影として置く。coherent多様体の準備と交差応答の制御は未完成である。

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

を誤差として管理する。

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

この定理はエネルギー地形を定める。閉鎖 Hamiltonian 流が最小配置へ収束することは示さない。境界準備で最小配置を選ぶか、弱開放縮約でずれ

```math
\varepsilon_j
=
\left\|
j-\mathcal J_\phi r^2
\right\|
```

を小さく保つ必要がある。弱い漏れは準備済み配置の安定化候補であり、coherent配置の生成機構としては使わない。

## 2.5 位相接続

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

## 2.6 粒子運動量の消去

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

## 2.7 時間反転

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

## 2.8 coherent集中の意味

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

## 2.9 同じ場の対モードと比較モード

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
