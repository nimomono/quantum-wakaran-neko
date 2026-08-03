@number: 0
@chapter: 概要
@title: 概要

本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。目的は、量子力学をミクロ構成の入力に置かず、量子力学に特徴的な力学と確率構造が縮約された有効理論として現れ得るかを検証することである。

現行模型の力学的な主線は、有限2成分誘導場の位相接続経路である。運動量結合による配置拡散経路は、実在的な確率軌道を構成する別の候補として付録Dへ移し、現行模型から外す。従って、本論文は配置 Markov 過程または Nelson 確率過程の実在を、Schrödinger 型力学の前提にしない。

有限セル $i$ の2成分場を

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix},
\qquad
j_i
=
\Phi_{1,i}\Pi_{2,i}
-
\Phi_{2,i}\Pi_{1,i}
```

とする。正準1形式は有限次元で厳密に

```math
\sum_i
\boldsymbol\Pi_i\cdot d\boldsymbol\Phi_i
=
\sum_i
\left(
p_{r,i}\,dr_i+j_i\,d\theta_i
\right)
```

となる。規格化 $\sum_i r_i^2\Delta V=1$ と固定全位相作用

```math
\mathcal J_\phi
=
\sum_i j_i\Delta V
```

の下で、回転エネルギーは

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
\Delta V
```

と分解できる。従ってエネルギー最小配置は $j_i=\mathcal J_\phi r_i^2$ である。これは固定作用sector内の厳密な最小化結果であり、閉鎖 Hamiltonian 流がこの配置へ吸引されることを意味しない。

セル体積を吸収した振幅 $R_i$ と局所作用 $J_i$ を用い、局所作用欠陥を

```math
\delta J_i
=
J_i
-
\frac{
\mathcal J_\phi R_i^2
}{
\sum_kR_k^2
}
```

とする。本稿は、動径運動量と $\delta J_i$ の正定値エネルギーを $1/\epsilon_{\rm s}$ で高速化した有限 Hamiltonian を追加する。有限 $\epsilon_{\rm s}$ の正確な Legendre 変換により、有界な低速枝では

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
\right)
```

を得る。さらに、準備窓だけ有限振幅浴と位相差に結合した有限作用交換浴を作動させる。作用交換浴は共通位相回転に不変なので $\mathcal J_\phi$ を厳密に保存し、余弦・正弦結合の対は位相固定項を作らない。固定振幅・短記憶・低温の準備近似では局所作用欠陥を減衰させる。ただし、観測中の相対位相運動を変えないよう、準備後は浴を切り離す。

この構成が部分的に具体化するのは、局所作用整合と動径低速化である。異なる標本を共通の $(r,\theta)$ へ集中させる coherent集中、$r^2=\rho$ の密度同期、単流束化、節の制御は導かない。

正則化した位相接続を

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

とし、粒子 Hamiltonian を

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

とする。coherent集中、局所作用分配、密度同期、単流束化、動径断熱化、節から離れた極限の下で、場の正準項と粒子の接続項は物質微分結合を与える。$S=-\mathcal J_\phi\theta$ と定めると、縮約作用は

```math
\mathcal A_{\rm red}
=
\int
\left[
\frac m2\rho|v|^2
-
\rho V
-
\rho
\left(
\partial_tS+v\cdot\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt
```

となる。係数整合

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
```

の下で、変分は Madelung 方程式を与える。従って

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|,
\qquad
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\hbar_{\rm eff}}
\right)
```

は節を避ける局所領域で Schrödinger 型方程式を満たす。これは位相接続縮約作用からの直接結果であり、配置拡散経路を使用しない。Nelson の現在速度表示との一致は、同じ作用の別表示としてのみ用いる。

単価な2成分場では

```math
\oint
\nabla\theta\cdot d\ell
=
2\pi n
```

であるため、条件付き循環量子化を得る。節の生成・消滅、正則化極限、全ての物理的流れが単価な場から準備されることは未解決であり、Wallstrom 問題を全面的に解いたとは主張しない。

位置の Born 型入口重みは2モード作用殻から得る。局所作用を

```math
A_i
=
A_{\rm tot}r_i^2\Delta V
```

とし、選択された活性モードと1つの共有明反応座標が $K_i+I=A_i$ を分配すると、

```math
\Omega_2(A_i)
=
(2\pi)^2A_i
```

である。排他的な入口チャンネルの法線速度、障壁、coarea Jacobian、spectator因子が共通なら、正方向 Liouville 流束は $A_i$ に比例し、

```math
P_i
=
r_i^2\Delta V,
\qquad
\rho_{{\rm in},i}
=
r_i^2
```

を得る。これは位置入口分布に限定された Born 型結果であり、任意基底の一般測定則ではない。

Bell 側でも、新しい配置空間場は導入しない。同じ2成分場の固定された直交モード部分空間から、左右へ進む2出力モードを切り出す。左右モード間の低ランク相関を

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

と定義する。$C$ は独立した正準場ではなく、基礎モードから作る派生量である。共役を含むため、共通内部位相回転に対して不変である。

2つの直交源チャンネルが反対称源

```math
C_0
=
\sqrt{\frac{\mathcal K}{2}}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

を準備し、左右の局所分析器が出力モードを $R(\alpha_a)$、$R(\alpha_b)$ で回すと、結果枝作用は

```math
K_{AB}
=
\left|
e_A^{\mathsf T}
R(\alpha_a)
C_0
R(\alpha_b)^{\mathsf T}
e_B
\right|^2
=
\frac{\mathcal K}{4}
\left[
1-AB\cos\Delta_{ab}
\right],
```

```math
\Delta_{ab}
=
2
\left(
\alpha_a-\alpha_b
\right)
```

となる。局所分析器は場の共通内部位相を回すのではなく、固定された2出力モード添字を局所的に回す。

左右の記録後、戻りモードは有限速度で共通未来の比較領域へ伝播する。そこに同じ誘導場の2つの境界比較モード

```math
(Q_{\rm R},P_{\rm R}),
\qquad
(Q_{\rm I},P_{\rm I})
```

を置き、理想比較パルスを

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}\operatorname{Re}C
+
P_{\rm I}\operatorname{Im}C
\right]
```

とする。比較運動量が零で、他の自由発展を無視できるなら、入力モードを乱さず

```math
Q_{\rm R}^{\rm out}
=
\Gamma\operatorname{Re}C_{AB},
\qquad
Q_{\rm I}^{\rm out}
=
\Gamma\operatorname{Im}C_{AB}
```

を得る。従って比較2モードの総作用は

```math
A_\partial^{AB}
=
\frac{\Gamma^2}{2}K_{AB}.
```

2モード殻容量は線形なので、

```math
\Omega_2
\left(
A_\partial^{AB}
\right)
=
(2\pi)^2A_\partial^{AB}
\propto
K_{AB}.
```

ただし、読み出し写像、殻上の等方混合、結果頻度を区別しなければならない。Hamiltonian 読み出しは空の比較器を殻上の1点へ移し、$U(2)$ 混合は準備された集団を殻上で混ぜるが、正規化済みの結果セクター総質量を殻容量倍にはしない。Bell 重みを得るには、各比較殻へ共通密度または共通流束を置く二側境界準備条件が別に必要である。

結果セクターの基準質量が $w_{AB}=1/4$、境界密度、時計速度、coarea因子、spectator体積が全結果で共通なら、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1-AB\cos\Delta_{ab}
\right]
```

を得る。対称性により一側周辺は $1/2$ である。境界測度を生成側へ Hamiltonian flow で引き戻すと一般に

```math
\rho(\Lambda\mid a,b)
\neq
\rho(\Lambda)
```

となる。従って Bell の前提違反は測定設定独立性にある。共通未来比較器が前向き因果として過去の局所記録を変更するわけではない。

本改訂の中心的な前進は、位相接続による Schrödinger 型力学を支える局所作用整合と動径低速化を、有限特異 Hamiltonian の低速枝と時計制御された有限準備浴として部分的に具体化したことである。位置の Born 型入口標本化、同じ2成分場の低ランク対モードから得る Bell 余弦作用、共通未来比較器による2モード作用転送は維持した。最大の未解決問題は、殻容量に比例する共通境界測度を、結果別の事後選別を用いない実験周期として準備し、coherent集中、密度同期、記録、逆計算、再初期化まで統合することである。
