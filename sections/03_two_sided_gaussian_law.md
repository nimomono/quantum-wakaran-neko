@number: 3
@chapter: 本文
@title: 縮約多様体、Madelung 作用、Schrödinger 型力学
@status: coherent縮約多様体に制限した Madelung 作用、変分、Schrödinger 型方程式、同期差保存は厳密結果である。確率過程を前提にしない。正定値2次場模型では高速法線成分の除去と局所縮約残差を条件付きで制御する。半正定値位相 Hessian、粒子-場を含む全 Hessian、coherent集中、密度同期、一様な特異極限、時間依存停留経路は未完成である。

## 3.1 縮約条件

第2章の有限セル系から連続表示へ進むため、次の条件を分けて置く。

1. **coherent集中**：非線形接続と正準項を共通の代表場 $(r,\theta)$ で評価できる。
2. **固定作用sector**：全位相作用 $\mathcal J_\phi\neq0$ を固定する。
3. **準備済み局所作用整合**：第2.6節の低速枝と第2.7節の準備窓により、

```math
j
=
\mathcal J_\phi r^2
+
O(\varepsilon_j).
```

4. **密度同期**：

```math
r^2
=
\rho
+
O(\varepsilon_\rho).
```

5. **接続極限**：節から離れた領域で

```math
\mathbf a_\varepsilon
=
\nabla\theta
+
O(\varepsilon_{\rm node}).
```

6. **単流束化**：条件付き速度分散による古典圧力を

```math
\varepsilon_{\rm press}
```

で抑える。
7. **準備済み動径低速化**：第2.6節の低速枝と振幅浴により、$p_r^2/(2M_r)$ と高速振幅モードの作用寄与を

```math
\varepsilon_{\rm radial}
```

で抑える。
8. **位相勾配の非重複**：粒子流速へ入れた位相運動エネルギーと、場側の $r^2|\nabla\theta|^2$ を二重に数えない。

これらは縮約多様体の定義と誤差条件である。第2章と付録Eは3と7の局所的な準備候補を与える。付録Fは、さらに正定値定数係数2次模型の高速法線成分を同型補助系へ完全に移す。しかし、1、4、6、半正定値位相 Hessian、節の制御を導かない。有限 Hamiltonian 時間発展が一般の初期状態から縮約多様体全体へ吸引するとは仮定しない。

### 3.1.1 有限特異パラメータの残差

セル表示では、第2.6節の正確な運動量消去により、理想縮約作用へ

```math
\Delta\mathcal A_{\epsilon_{\rm s}}
=
\int
\left[
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
+
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
\right)^2
\right]
dt
```

が加わる。有界な低速枝では $O(\epsilon_{\rm s})$ の作用補正である。準備浴の切断後には、さらに準備終了時の $P_i$、$\delta J_i$、記憶尾、有限温度雑音床を残差として加える。

この有限パラメータ表示は、局所作用整合と動径低速化を直接代入するより強い。しかし、有限エネルギーだけからの誤差は一般に $O(\sqrt{\epsilon_{\rm s}})$ であり、解と1次変分が観測時間に一様収束する定理はない。従って以下の Madelung 作用は、準備済み低速枝での形式的特異極限として扱う。

### 3.1.2 3種類の停留条件

本稿では、次の3つを区別する。

1. **場chartの局所2次縮約方程式**：付録Fの正定値2次模型で低速部分空間上の残差を $O(\epsilon_{\rm s})$ に抑える。
2. **coherent多様体上の Madelung 作用**：本章で制限作用を変分する。
3. **M0全体の粗視化停留力学**：粒子、場、密度、装置を含むミクロ時間発展から2を導く。

1は条件付きで部分達成したが、2の複数の解から特定解を選ばない。3は未解決である。従って「高速法線成分の除去」を「M0の停留点選択」と呼ばない。

## 3.2 物質微分結合

場の正準1形式は連続表示で

```math
\int
\left(
p_r\partial_tr
+
j\partial_t\theta
\right)
\,dx.
```

局所作用分配を用いると、位相部分は

```math
\mathcal J_\phi
\int
r^2\partial_t\theta
\,dx.
```

粒子の位相接続項は

```math
\mathcal J_\phi
\int
\rho
v\cdot\nabla\theta
\,dx.
```

密度同期 $r^2=\rho$ の理想極限では、両者の和は

```math
\mathcal J_\phi
\int
\rho
\left(
\partial_t\theta
+
v\cdot\nabla\theta
\right)
\,dx.
```

従って、位相は粒子流に沿う物質微分として作用へ入る。

Schrödinger 表示の位相を

```math
S
=
-\mathcal J_\phi\theta
```

と定める。すると上の項は

```math
-\int
\rho
\left(
\partial_tS
+
v\cdot\nabla S
\right)
\,dx
```

となる。

## 3.3 縮約作用

固定 $\mathcal J_\phi$ sectorで定数となる回転基底エネルギーを除き、動径慣性と交差誤差を無視した理想縮約作用を

```math
\mathcal A_{\rm red}
\left[
\rho,v,S
\right]
=
\int
\left[
\frac m2\rho|v|^2
-
\rho V
-
\rho
\left(
\partial_tS
+
v\cdot\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt
```

とする。

<!-- theorem-start:theorem -->
**定理（縮約多様体上の Madelung 作用）**
第3.1節の理想縮約条件が成立し、

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
```

なら、$\mathcal A_{\rm red}$ は有効作用定数

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|
```

を持つ Madelung 作用に一致する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
Madelung 作用の振幅勾配項は

```math
\frac m2
\int
\rho|u|^2
\,dx,
\qquad
u
=
\nu\nabla\log\rho.
```

と書ける。恒等式

```math
\rho
\left|
\nabla\log\rho
\right|^2
=
4
\left|
\nabla\sqrt\rho
\right|^2
```

より、

```math
\frac m2
\int
\rho|u|^2
\,dx
=
2m\nu^2
\int
\left|
\nabla\sqrt\rho
\right|^2
\,dx.
```

$\nu=|\mathcal J_\phi|/(2m)$ と置けば $2m\nu^2=\mathcal J_\phi^2/(2m)=\kappa$ である。これは Nelson の現在速度表示と同じ係数表示でもあるが、本定理は確率過程または配置拡散を仮定しない [3--6,30]。残りの項は連続の式を制約する標準的な Madelung 作用と一致する。
<!-- theorem-end:proof -->

この定理は作用を縮約多様体へ制限した後の一致を述べる。ミクロ運動がその制限作用の停留点を選ぶことは含まない。$\nu=|\mathcal J_\phi|/(2m)$ は係数の別表示であり、実在的な Markov 経路の存在を意味しない。

## 3.4 変分方程式

$S$、$v$、$\rho$ を独立に変分し、境界変分を零とする。

$S$ 変分から、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0.
```

$v$ 変分から、

```math
mv
=
\nabla S.
```

$\rho$ 変分から、

```math
\frac m2|v|^2
-
V
-
\partial_tS
-
v\cdot\nabla S
+
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0.
```

$mv=\nabla S$ を代入すると、

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
V
-
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0.
```

量子ポテンシャルに対応する項を

```math
Q[\rho]
=
-
\frac{\mathcal J_\phi^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

と書ける。

## 3.5 Schrödinger 型方程式

節を避ける単連結領域で

```math
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\hbar_{\rm eff}}
\right),
\qquad
\hbar_{\rm eff}
=
|\mathcal J_\phi|
```

とする。連続の式と Hamilton--Jacobi 式は

```math
i\hbar_{\rm eff}
\partial_t\psi
=
\left[
-
\frac{\hbar_{\rm eff}^2}{2m}
\Delta
+
V
\right]
\psi
```

に等価である。

活性場を

```math
\Psi_{\rm A}
=
re^{i\theta}
```

と書く。$S=-\mathcal J_\phi\theta$ なので、$\mathcal J_\phi>0$ sectorかつ $r^2=\rho$ では

```math
\psi
=
\Psi_{\rm A}^*.
```

活性場と Schrödinger 表示を同じ記号にしない。

## 3.6 係数不一致

場の振幅勾配係数が

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
+
\delta\kappa
```

なら、Hamilton--Jacobi 式には

```math
-\delta\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

が残る。$\hbar_{\rm eff}=|\mathcal J_\phi|$ で定義した $\psi$ に対して、これは標準 Schrödinger 方程式からの非線形残差になる。

従って

```math
\varepsilon_\kappa
=
\frac{
\left|
\delta\kappa
\right|
}{
\mathcal J_\phi^2/(2m)
}
```

を独立に管理する。$\kappa=\mathcal J_\phi^2/(2m)$ は内部回転対称性だけから従う定理ではなく、ミクロ係数の整合条件である。

## 3.7 密度同期差の保存

密度同期を作用へ代入する前の位相部分を

```math
\mathcal A_\theta
=
\int
\left[
j\partial_t\theta
+
\mathcal J_\phi
\rho v\cdot\nabla\theta
\right]
\,dx\,dt
```

とする。残余場 Hamiltonian を $H_{\rm residual}$ とし、理想縮約で必要な条件を

```math
\frac{
\delta H_{\rm residual}
}{
\delta\theta
}
=
0
```

とする。この条件の下で、$\theta$ 変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得る。

<!-- theorem-start:proposition -->
**命題（coherent多様体上の同期差保存）**
$\mathcal J_\phi\neq0$、$j=\mathcal J_\phi r^2$、粒子密度が連続の式を満たすなら、

```math
\partial_t
\left(
r^2-\rho
\right)
=
0.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$j=\mathcal J_\phi r^2$ を位相保存式へ代入して $\mathcal J_\phi$ で割ると、

```math
\partial_tr^2
+
\nabla\cdot(\rho v)
=
0.
```

粒子の連続の式との差を取る。
<!-- theorem-end:proof -->

これは同期差の中立的保存である。$r^2\neq\rho$ の状態を同期へ引き戻す復元力は含まない。共通位相の定数回転に対する不変性だけでは上の汎関数微分条件に足りず、相対位相または位相勾配に依存する残余項は追加流束を作り得る。入口で $r^2=\rho$ を作る作用殻流束を第4章で与える。

## 3.8 循環量子化

2成分場が閉曲線 $\gamma$ 上で非零かつ単価なら、位相写像の巻数 $n\in\mathbb Z$ により

```math
\oint_\gamma
\nabla\theta\cdot d\ell
=
2\pi n.
```

従って

```math
\oint_\gamma
\nabla S\cdot d\ell
=
-2\pi\mathcal J_\phi n
=
2\pi\hbar_{\rm eff}N,
\qquad
N\in\mathbb Z.
```

最後の整数 $N$ は $-\operatorname{sgn}(\mathcal J_\phi)n$ である。

この命題は、単価な2成分場と非零経路を仮定した条件付き循環量子化である。次は未完成である。

- $r=0$ の節近傍における接続と $j^2/r^2$ の同時正則化。
- 節の生成・消滅時における巻数変化。
- 密度同期が節を含む領域で維持される条件。
- 全ての物理的初期流れが単価な活性場から準備されること。

従って位相量子化は部分達成であり、Wallstrom 問題への全面的回答ではない [19]。

## 3.9 作用一致と力学導出の境界

本章で厳密なのは、縮約条件を満たす多様体に制限した作用の代数、変分、局所 Schrödinger 表示、同期差保存、条件付き循環量子化である。

未解決なのは、

1. 一般の有限 Hamiltonian 初期集団から coherent集中と密度同期を準備すること。
2. 現行の位相勾配非重複条件に適合する半正定値・零モード版の高速射影と交換定理を示すこと。
3. 有限 $\Lambda_N$ の規格化モードと、粒子-場を含む全 Hessian を扱うこと。
4. 時間依存基準経路で回転する低速・高速射影と、非線形高速再励起を制御すること。
5. 付録Eと付録Fの準備窓から観測窓まで、$\varepsilon_j$ と $\varepsilon_{\rm radial}$ の再成長を一様に抑えること。
6. 観測窓で $\varepsilon_{\rm coh}$、$\varepsilon_j$、$\varepsilon_\rho$、$\varepsilon_{\rm radial}$、$\varepsilon_{\rm press}$ を同時に小さくすること。
7. ミクロ運動の粗視化が $\mathcal A_{\rm red}$ の時間依存停留経路を支配すること。
8. 一般の節構造を含む領域で同じ縮約を制御すること。

実在的な前後 Markov 経路を構成する別候補は付録Dへ記録するが、本章の導出には使用しない。
