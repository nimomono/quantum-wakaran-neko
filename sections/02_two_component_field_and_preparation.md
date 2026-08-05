@number: 2
@chapter: 本文
@title: 有限2成分場と準備済み低速領域
@status: 有限セルの正準構造、保存全位相作用、固定作用平方分解、厳密規格化下の局所座標 Hamiltonian は厳密結果である。高速整合は限定模型で部分的に準備できる。初期コヒーレント集中と粒子・場同期は独立の準備条件である。

## 2.1 大域変数と局所極座標

セル $i=1,\ldots,L$ に実2成分正準対

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
\delta_{\alpha\beta}
\delta_{ij}
```

である。節を含む大域変数は $\boldsymbol\Phi_i$ と $\boldsymbol\Pi_i$ であり、複素表示を

```math
\zeta_i
=
\Phi_{1,i}
+
i\Phi_{2,i}
```

とする。

$|\boldsymbol\Phi_i|>0$ の局所領域だけで、

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix}
```

と書く。動径運動量と局所位相作用を

```math
p_{r,i}
=
\boldsymbol\Pi_i
\cdot
\frac{
\boldsymbol\Phi_i
}{
r_i
},
\qquad
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
\boldsymbol\Pi_i
\cdot
d\boldsymbol\Phi_i
=
p_{r,i}
\,dr_i
+
j_i
\,d\theta_i
```

が成立する。
<!-- theorem-end:proposition -->

この命題は局所座標の厳密な正準性を与えるが、節上で $\theta_i$ を定義しない。以後、大域的な集中と弱方程式は $\zeta$ で記述し、極座標は節外の計算に限定する。

## 2.2 規格化と保存全位相作用

セル体積を $\Delta V$ とし、場強度を

```math
\mathcal N_\Phi
=
\sum_i
\left|
\zeta_i
\right|^2
\Delta V
```

とする。主定理では

```math
\mathcal N_\Phi
=
1
```

をホロノミック制約として課す。有限ペナルティ

```math
H_{\rm norm}
=
\frac{
\lambda_{\rm norm}
}{
2
}
\left(
\mathcal N_\Phi-1
\right)^2
```

は別模型であり、厳密規格化と同じ不変セクターではない。

全セルを共通角だけ内部回転する対称性の生成子は

```math
\mathcal J_\phi
=
\sum_i
j_i
\Delta V
```

である。全 Hamiltonian がこの共通回転に不変なら、

```math
\left\{
\mathcal J_\phi,
H_{\rm all}
\right\}
=
0
```

となる。個々の $j_i$ はセル間を流れ得るが、$\mathcal J_\phi$ は保存される。本稿は $\mathcal J_\phi\neq0$ の固定セクターを取る。

## 2.3 固定作用下の平方分解

$r_i>0$、$\mathcal N_\Phi=1$ の局所座標で、回転エネルギーを

```math
E_{\rm rot}
=
\sum_i
\frac{
j_i^2
}{
2Ir_i^2
}
\Delta V
```

とする。

<!-- theorem-start:theorem -->
**定理（固定作用下の局所作用分配）**
固定 $\mathcal J_\phi$ の下で、

```math
E_{\rm rot}
=
\frac{
\mathcal J_\phi^2
}{
2I
}
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

が成立する。従って、固定した振幅に対する一意な最小配置は

```math
j_i
=
\mathcal J_\phi r_i^2
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
平方項を展開し、

```math
\sum_i
j_i
\Delta V
=
\mathcal J_\phi,
\qquad
\sum_i
r_i^2
\Delta V
=
1
```

を代入する。交差項と定数項を整理すると $E_{\rm rot}$ が残る。
<!-- theorem-end:proof -->

これは固定振幅上のエネルギー最小化であって、閉鎖 Hamiltonian 流の吸引定理ではない。

## 2.4 高速整合

セル体積を正準変数へ吸収し、

```math
R_i
=
r_i
\sqrt{
\Delta V
},
\qquad
P_i
=
p_{r,i}
\sqrt{
\Delta V
},
\qquad
J_i
=
j_i
\Delta V
```

とする。規格化と全位相作用は

```math
N
=
\sum_iR_i^2,
\qquad
\mathcal J_\phi
=
\sum_iJ_i
```

である。局所作用欠陥を

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

と定めると、

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

が厳密に成立する。

直交座標で同じ条件を見るため、内部回転行列を

```math
\mathbb J
=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
```

とする。規格化済みの単位系では、理想接線運動量は $\mathcal J_\phi\mathbb J\boldsymbol\Phi_i$ である。代数的高速欠陥を

```math
\boldsymbol D_i
=
\boldsymbol\Pi_i
-
\mathcal J_\phi
\mathbb J
\boldsymbol\Phi_i
```

と書ける。一般の慣性係数とセル重みを使う場合は対応する線形同型を挿入する。$\boldsymbol D_i=0$ は $p_{r,i}=0$ と $j_i=\mathcal J_\phi r_i^2$ に対応する。

ただし、$\boldsymbol D$ と正定値2次化の高速 Riesz 射影は一般には同じではない。前者は座標的な欠陥、後者は特定の2次 Hamiltonian のスペクトル部分空間である。付録Fの正定値条件下だけで両者の局所的な同値を使う。

本稿で高速整合とは、次の量が適用模型に応じて小さいことをいう。

```math
\varepsilon_{\rm fast}^2
=
\mathbb E_\omega
\left[
\sum_i
\left(
P_i^\omega
\right)^2
+
\sum_i
\frac{
\left(
\delta J_i^\omega
\right)^2
}{
\left(
R_i^\omega
\right)^2
}
+
\left\|
P_{\rm f}
z^\omega
\right\|^2
\right]
```

ここで $P_{\rm f}$ は、定義できる場合だけ用いる高速スペクトル射影である。

## 2.5 高速整合の準備機構

高速整合には2つの補助模型を使う。

1. 付録Eの有限振幅浴と有限作用交換浴。
2. 付録Fの正定値2次模型と同型高速モード交換補助系。

有限作用交換浴は位相差の余弦と正弦へ対称に結合する。共通内部回転に不変なので $\mathcal J_\phi$ を厳密に保存し、対となる逆項は位相固定ポテンシャルを作らない。固定振幅、短記憶、低温、有限浴再帰前の近似では、局所作用欠陥の2次量を減少させる。

同型交換は、正定値定数係数2次模型の高速 symplectic 部分空間に限定すれば厳密である。補助系が零状態から始まり交換角が $\pi/2$ なら、高速成分を補助系へ完全に移す。

2つの機構は同じ主張ではない。局所浴は局所的だが近似的であり、同型交換は2次模型内で厳密だが大域射影、同型複製、精密な交換角を必要とする。どちらも異なる標本を同じ場プロファイルへ集中させず、粒子密度と場強度も同期させない。

準備浴は観測中の相対位相運動を変え得るため、準備窓の後に切り離す。時間尺度は

```math
\tau_{\rm corr}
\ll
T_{\rm prep}
\ll
T_{\rm obs},
T_{\rm rec}
```

と分ける。有限温度、記憶尾、有限浴再帰、交換角誤差、補助初期エネルギー、観測中の高速再生成は第6章の準備誤差と縮約誤差へ含める。

## 2.6 コヒーレント集中

各標本の複素場を $\zeta^\omega$ とする。連続模型では外部ポテンシャルを含む Hamiltonian の閉じた2次形式を $h_V$、共通形式領域を $\mathcal Q$ とする。定数 $c_V$ を十分大きく取り、

```math
\left\|
u
\right\|_{\mathcal E_V}^2
=
\left\|
u
\right\|_{L^2}^2
+
h_V
\left[
u
\right]
+
c_V
\left\|
u
\right\|_{L^2}^2
```

をエネルギーノルムとする。有限セルでは、同じ記号を離散勾配と実ポテンシャルを含む正定値2次形式に使う。

共通内部位相を物理的に同一視し、代表場 $\bar\zeta(t)$ に対する射影距離を

```math
\varepsilon_{\rm coh}^2(t)
=
\mathbb E_\omega
\inf_{
\alpha\in
\left[
0,2\pi
\right)
}
\left\|
\zeta^\omega(t)
-
e^{i\alpha}
\bar\zeta(t)
\right\|_{\mathcal E_V}^2
```

と定める。十分小さい分散と、基準場に対する非零重なりの下で、位相整合した射影重心を $\bar\zeta$ とする。

単純な標本平均を代表場にしてはならない。標本ごとの共通位相が異なると平均が相殺するからである。また、各時刻で独立に位相を最小化すると時間微分が不定になる。第3章では、初期代表場から連続に追跡する位相規約を使い、実数の共通位相項 $\lambda(t)$ を許す。

高速整合が成立しても、標本が異なる低速固有モードへ分かれていれば $\varepsilon_{\rm coh}$ は小さくない。従って、初期コヒーレント集中は独立の準備条件である。

## 2.7 場強度・場流束と粒子同期

代表場の強度を

```math
q
=
\left|
\bar\zeta
\right|^2
```

とする。位相向きを係数整合した有効場を $\psi$ とし、その場流束を

```math
\boldsymbol j_\psi
=
\frac{
\hbar_{\rm eff}
}{
m
}
\operatorname{Im}
\left(
\psi^*
\nabla\psi
\right)
```

とする。粒子側の密度と流束を $\rho$、$\boldsymbol J_{\rm p}$ とする。

密度・流束同期は

```math
\left\|
\rho-q
\right\|_{H^{-1}}
\ll1,
\qquad
\int_0^T
\left\|
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right\|
\,dt
\ll1
```

で評価する。節では $q=0$ となるため、$(\rho-q)/q$ のような相対誤差は使わない。

コヒーレント集中から、各標本場の強度と場流束が代表場へ集中することは積評価で従う。しかし、粒子密度と粒子流束との同期は従わない。第4章の位置入口作用殻は初期密度の分布部分を準備する候補だが、流束同期を準備しない。

## 2.8 位相接続

連続補間した2成分場に対し、正則化した接続を

```math
\boldsymbol a_\varepsilon
=
\frac{
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
}{
\left|
\boldsymbol\Phi
\right|^2
+
\varepsilon^2
}
```

とする。節外の極座標では

```math
\boldsymbol a_\varepsilon
=
\frac{
r^2
}{
r^2+\varepsilon^2
}
\nabla\theta
```

である。粒子正準対を $(X,P)$ とし、

```math
H_{\rm p}
=
\frac{
\left|
P
-
\mathcal J_\phi
\boldsymbol a_\varepsilon(X)
\right|^2
}{
2m
}
+
V(X,t)
```

とする。粒子運動量を消去すると、

```math
L_{\rm p}
=
\frac m2
\left|
\dot X
\right|^2
+
\mathcal J_\phi
\boldsymbol a_\varepsilon(X)
\cdot
\dot X
-
V(X,t)
```

を得る。

節外で $\varepsilon\to0$ とし、局所作用整合と密度同期を用いると、場の正準項と粒子接続項は位相の物質微分を作る。これは第3章の縮約作用を与える。しかし、$\rho-q$ が弱いノルムで小さいだけでは、節近傍で大きくなり得る $\boldsymbol a_\varepsilon$ との積を制御できない。節近傍の重み付き接続誤差は、ミクロ残差上界の独立成分として残す。

## 2.9 外部位置ポテンシャル

有限セル定理では、$V_i(t)$ を実数値とし、有限観測時間で一様有界、かつ対象軌道を有限エネルギー領域へ保つと仮定する。位置依存性を調和型または弱非線形へ限定しない。

連続極限では、次を仮定する。

1. $V(x,t)$ は実数値で下から有界である。
2. $H_V(t)$ は自己共役であるか、閉じた半有界2次形式を持つ。
3. 時間依存の場合は有限観測時間で共通形式領域 $\mathcal Q$ を持つ。
4. 対応する発展作用素がエネルギーノルムで有限時間安定である。
5. 境界条件を固定する。

$V(x,t)$ の位置依存の非線形性自体を小さい摂動とはしない。小さくするのは、高速・低速間の再励起、縮約集合からの逸脱、有限セル誤差、接続正則化誤差である。$V=V(|\psi|^2)$ のような状態依存ポテンシャルは扱わない。

## 2.10 準備済み初期集団

第3章で使う初期集団は、次を満たす。

1. 規格化と全位相作用のセクターが固定されている。
2. $\varepsilon_{\rm fast}(0)$ が小さい。
3. $\varepsilon_{\rm coh}(0)$ が小さい。
4. $\|\rho(0)-q(0)\|_{H^{-1}}$ が小さい。
5. 観測窓における粒子・場流束差の時間積分に上界がある。
6. 一様な場エネルギー上界がある。
7. 代表場の時間位相を連続に選べる非零重なりがある。

1から3を準備する完成した有限 Hamiltonian 装置はまだない。付録Eと付録Fは2の一部だけを扱い、第4章は4の分布部分だけを扱う。第3章の有限時間定理は、この不足を仮定として明示した上で、観測窓内の安定性を述べる。
