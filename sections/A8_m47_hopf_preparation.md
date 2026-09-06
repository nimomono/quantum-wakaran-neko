@number: H
@chapter: 付録
@title: M54 W型2モード特殊化の対応表
@status: Q1 W型2モードprotocolで使うM54/R181A、R135、R140のパラメータ対応だけを示す。一般定理の証明は第2章、本文第3章、付録Mを正本とし、本付録では特殊化を再証明しない。

## H.1 目的と主張範囲

本付録は、対称W型ポテンシャルの最低2モードsectorをM54 W2 static profileへ対応させる辞書である。旧版でM47単一Hopf準備と呼んだ内容のうち、独立の物理機構ではないR181A、R135、R140の単なるパラメータ特殊化を一か所にまとめる。

粒子位置のBorn型分布、有限熱化、局所記録はR164、R161、R162、R170とR181Dの深さ1特殊化が操作面ごとに構成する。信号bathの統計核だけから単一試行粒子位置または連続位置rateを作る規則は使わない。

| 段階 | W型2モードでの指定 | 正本 |
|---|---|---|
| 開放準備 | $m=2$、生成子 $D_W$、目標ray $c_*(t)$ | R181A、付録M |
| 閉鎖伝播 | $G=D_W$ の2モード正準流 | R135、第2章 |
| W型制御・診断 | 偶奇二重項と左右局在基底。M37物理carrierはR187 | R140、第3章、第6章 |
| 排他的読出し | 2枝static matchingと局所記録 | R164、R161、R162、R170、R181D |
| 状態更新 | W型有限コントラストと結果別template | R143 |

## H.2 W型作用素と最低2モード

有限の対称1次元格子または有界区間上で、M37の古典振動子網から得る実対称包絡生成子を

```math
h_W
=
\frac{\mathcal J_0^2}{2m}L_W+V_W
```

とする。最低2モードの単純固有対を

```math
h_W\phi_0=E_0\phi_0,
\qquad
h_W\phi_1=E_1\phi_1,
\qquad
E_0<E_1
```

とし、$\phi_0$ を実偶、$\phi_1$ を実奇、両者を規格化直交とする。2モード埋込みは

```math
\Phi c=c_0\phi_0+c_1\phi_1,
\qquad
c\in\mathbb C^2
```

である。2モード対角生成子を

```math
D_W
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}
```

と置く。

左右局在基底は位相規約を固定して

```math
|L\rangle
=
\frac{\phi_0+\phi_1}{\sqrt2},
\qquad
|R\rangle
=
\frac{\phi_0-\phi_1}{\sqrt2}
```

とする。左井戸射影を $\Pi_L$ とし、

```math
\langle\phi_0,\Pi_L\phi_0\rangle
=
\langle\phi_1,\Pi_L\phi_1\rangle
=
\frac12,
\qquad
B_W=\langle\phi_0,\Pi_L\phi_1\rangle
```

を使う。

## H.3 R181Aへのパラメータ対応

目標規格化係数 $c_*$ の閉鎖回転軌道と射影を

```math
c_*(t)
=
\exp
\left[
-\frac{iD_W(t-t_*)}{\mathcal J_0}
\right]c_*,
\qquad
\Pi_*(t)=c_*(t)c_*(t)^\dagger
```

と置く。R181Aへ

```math
m=2,
\qquad
G=D_W,
\qquad
c(t)=c_*(t)
```

を代入する。準備portが開いた区間の採用有効方程式は

```math
\dot z
=
-\frac{i}{\mathcal J_0}D_Wz
+
\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-
\kappa(I_2-\Pi_*(t))z
\right]
```

となる。これは別の準備模型ではなくR181Aそのものである。ray方向収束、radial飽和、有界seed集合での有限時間誤差、rank-one第2モーメントへの受渡しは、付録MのR181A証明を $m=2$ に適用する。

各試行の実体は2個の実正準担体、template、pump、sink、clockであり、$z$ は実担体の派生複素座標である。$c_*$ と $c_*c_*^\dagger$ はtemplate設定と試行集団の統計記述であって追加の物理場ではない。直交seed、雑音付き定常測度、位相拡散、作用殻準備はR181Aの一般定理で主張していない範囲をそのまま引き継ぐ。

## H.4 R135とR140への対応

準備portを切った後は

```math
Z(t)
=
\exp
\left[
-\frac{iD_W(t-t_0)}{\mathcal J_0}
\right]Z(t_0)
```

である。従ってR135を $G=D_W$ へ特殊化すれば、

```math
i\mathcal J_0\dot C_Z=[D_W,C_Z]
```

となり、trace、正値性、rankの保存とrank-one因子の回転はR135から直接従う。本付録ではその証明を再掲しない。

R140の零傾斜W型診断では、rank-one因子を

```math
c(t_0)
=
\begin{pmatrix}
a_0e^{-i\theta_0(t_0)}\\
a_1e^{-i\theta_1(t_0)}
\end{pmatrix},
\qquad
a_0^2+a_1^2=1
```

とし、$\delta(t)=\theta_1(t)-\theta_0(t)$ と置く。統計核の左井戸積分は

```math
P_L^{\rm stat}(t)
=
\frac12+2a_0a_1B_W\cos\delta(t),
```

```math
\delta(t)
=
\delta(t_0)
+
\frac{E_1-E_0}{\mathcal J_0}(t-t_0)
```

であり、

```math
\Omega_W
=
\frac{E_1-E_0}{\mathcal J_0},
\qquad
T_W
=
\frac{2\pi\mathcal J_0}{E_1-E_0}
```

を得る。任意軸制御、離調Rabi式、有限2モード誤差は本文第3章のR140を正本とする。

## H.5 Q1 W型2モードprotocolへの接続

現行Q1は次の順序を使う。

1. R181AのW型2モード特殊化で単一試行signal方向を準備し、固定canonical portでR187のM37最低2正常modeへ渡す。
2. R187がM37局所ばねcarrier上でR140の有限正準操作を任意精度で実装し、R135へ統計輸送誤差を渡す。
3. 操作面でR164の2枝作用殻状態数を作り、R161 staticとR162 thermalを介してR170へ接続する。
4. R181Dの深さ1 nodeでselectorをlockし、無反応を含む完全結果を局所記録する。
5. R143でW型有限コントラストと結果別template交換を加える。
6. 固定有限段の逐次合成はR144を使う。

この因果鎖をQ1 W型2モードprotocolと呼ぶ。旧モデルID M47はGit履歴と旧版参照のため保持するが、M54とは別の現行親模型として数えない。

## H.6 限界

ここで得る $P_L^{\rm stat}$ は信号bath第2モーメントの空間核に対する診断量であり、それだけから単一試行粒子位置 $X$ の分布または経路は従わない。Q1の排他的位置結果はR164/R161/R162/R170で別に構成する。

Q3-4Bでは低2モードの作用比を粒子位置確率へ読み替えず、R182がW型固有関数から完全位置密度を構成し、R161/R184がM54 spatial profileの同じ粒子へ受け渡す。R187によりM37から制御されたW型2モードcarrierをQ1全制御時間へ任意精度で接続する問題はcarrier levelでは閉じた。一方、R181A pump/source、R164作用殻、R161/R162 collision、R170/R143記録まで同じ有限局所Hamiltonianへ統合したわけではない。
