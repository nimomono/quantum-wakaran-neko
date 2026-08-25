@number: 3
@chapter: 本文
@title: M47の傾斜制御W型2モード操作と測定
@status: Q1をM47へ移す。Q1-1は2モード制御で達成し、Q1-2とQ1-3は有限誤差の条件付き構成として部分達成、Q1-4は未達のまま凍結する。

## 3.1 Q1の模型移行と主張範囲

本章は、Q1の現行模型をM38/M42からM47へ移す。基本状態は、W型ポテンシャル中で各試行に1つ存在する実現配置 $X$ と、2モード浴変数 $Z$ を持つ共同測度

```math
\mu(dX\,dZ)
```

である。複素振幅を独立した実在場として先に置かず、規格化共分散

```math
C
=
\frac{\mathbb E_\mu[ZZ^\dagger]}
{\mathbb E_\mu[Z^\dagger Z]}
```

が階数1の場合にだけ、その因子 $c$ を統計状態として使う。実現配置の分布と共分散の空間核を一致させる条件は、付録IのM47 matching条件である。

Q1の測定は次の順序で行う。

1. W型2モードの傾斜制御で、測定軸の固有方向を左右の局在方向へ写す。
2. トンネル振動より速く、高モード間隔より遅く傾斜を立ち上げる。
3. 左右井戸のエネルギー差で遷移振幅を抑え、既存の実現配置を片側へ保持する。
4. 各井戸に置いた局所記録ポインターが、その場所にある $X$ だけを記録する。
5. 安全枝では、記録結果に対応する準備済み2モードテンプレートと信号浴を正準交換する。
6. 測定前情報と使用済み装置状態を外部セルへ残し、内部補助を逆計算と交換resetで戻す。

局所記録は、$C$、統計振幅、全密度、確率流、遷移率を入力にしない。従って、M42/R113の

```math
b
\longrightarrow
q(b)
\longrightarrow
X
```

という因果律を使わない。

付録IのR145は、雑音零の採用開放Hopf方程式についてbath方向を目標位相円へ吸引する厳密解と有限時間率を与える。一方、実現配置周辺と条件付きbath分布を含む完全matching準備と切断後保存は、この改訂だけでは解消しない。特に、時刻ごとの周辺分布が一致することと、結果枝ごとの条件付き浴状態が測定後固有状態になることは別である。このため本章は、可逆2モード制御とbath方向吸引を厳密結果、左右読出しを明示誤差付き結果、枝別状態更新と完全周期を条件付き結果として分ける。

第5章のR152--R154は、固定singlet型Bell装置の各プロトコル面でmatchingを回復するために設計した局所開放配置bathである。任意のQ1入力、測定後テンプレート交換、異軸逐次測定を一様に閉じないので、本章の未導出条件を置き換えず、Q1-2とQ1-3は部分達成のままとする。

## 3.2 階数1共分散とBloch球

Pauli行列を $\sigma_x,\sigma_y,\sigma_z$ とし、共分散のBloch成分を

```math
r_k
=
\operatorname{tr}(C\sigma_k)
```

で定める。$C$ はHermitian、正半定値、trace 1なので

```math
C
=
\frac12
\left(
I_2+\boldsymbol r\cdot\boldsymbol\sigma
\right),
\qquad
|\boldsymbol r|\leq1
```

である。階数1なら $C=cc^\dagger$、$c^\dagger c=1$ と書け、$|\boldsymbol r|=1$ である。$c$ と $e^{i\alpha}c$ は同じ $C$ を与えるため、共通位相は観測状態に含まれない。

一般のHermitian行列 $G(t)$ に対して、古典2モードHamiltonianを

```math
H_G(t)
=
Z^\dagger G(t)Z
```

とする。正準方程式は

```math
i\mathcal J_0\dot Z
=
G(t)Z
```

であり、規格化共分散は

```math
i\mathcal J_0\dot C
=
[G(t),C]
```

に従う。

<!-- theorem-start:proposition -->
**命題（R139：M47階数1共分散のBloch縮約）**

trace 1の正半定値2次共分散について、階数1条件は $|\boldsymbol r|=1$ と同値である。階数1共分散の集合は共通位相を除いた $\mathbb{CP}^1\simeq S^2$ であり、$H_G$ の古典正準流はこの球面上の回転を与える。従ってM47の純粋2モード統計状態は、独立した複素振幅場を仮定せずBloch球を持つ。
<!-- theorem-end:proposition -->

R139はR135を一般の時間依存2モード生成子へ拡張したものである。共分散の回転は厳密だが、実現配置周辺のmatching保存は別の条件である。

## 3.3 W型ポテンシャルと局在基底

対称W型生成子 $h_W(0)$ の最低2固有モードを、実偶関数 $\phi_0$ と実奇関数 $\phi_1$ とする。固有値を $E_0<E_1$、平均と半分裂を

```math
\overline E
=
\frac{E_0+E_1}{2},
\qquad
J
=
\frac{E_1-E_0}{2}
```

とする。位相規約を選び、左右局在基底を

```math
|L\rangle
=
\frac{\phi_0+\phi_1}{\sqrt2},
\qquad
|R\rangle
=
\frac{\phi_0-\phi_1}{\sqrt2}
```

と置く。左右の名称は $\langle L|x|L\rangle<\langle R|x|R\rangle$ となるように必要なら $\phi_1$ の符号を反転する。

制御可能な1次傾斜を

```math
h_W(F)
=
h_W(0)-F(t)x
```

とする。対称性から最低2モード内では対角位置要素が消え、局在基底での生成子は共通エネルギーを除いて

```math
G_F(t)
=
-J\sigma_x
+
\frac{\varepsilon(t)}{2}\sigma_z,
\qquad
\varepsilon(t)
=
2F(t)
\left|
\langle\phi_0|x|\phi_1\rangle
\right|
```

となる。$-J\sigma_x$ は左右トンネル振動、$\varepsilon\sigma_z/2$ は左右エネルギー差である。

## 3.4 傾斜制御による任意のSU(2)操作

傾斜を零にした区間は $\sigma_x$ 回転を与える。零でない一定傾斜は、$x$ 軸と平行でない $xz$ 平面内の軸回転を与える。2本の非平行回転軸の有限積は $SU(2)$ 全体を生成する。Lie代数では

```math
[\sigma_x,\sigma_z]
=
-2i\sigma_y
```

なので、$\sigma_x$ と $\sigma_z$ から3方向が閉じる。

一定傾斜 $\varepsilon$ で $|L\rangle$ から開始したとき、右井戸方向への2モード作用比は

```math
P_{L\to R}(t)
=
\frac{4J^2}{\varepsilon^2+4J^2}
\sin^2
\left(
\frac{\sqrt{\varepsilon^2+4J^2}}{2\mathcal J_0}t
\right).
```

この式は、共鳴 $\varepsilon=0$ での完全振動、離調による振幅低下、振動数の変化を同じ担体で与える。

<!-- theorem-start:theorem -->
**定理（R140：W型傾斜制御による2モード可制御性）**

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はunitary共役であり、trace、正値性、階数を保存する。一定傾斜の左右遷移は上の離調公式に従う。
<!-- theorem-end:theorem -->

R140は制御された2モード生成子についての厳密結果である。元の全W型系で同じ精度を得るには、高モード漏れと傾斜切替誤差を別に評価する。

## 3.5 2モード窓と傾斜切替の尺度階層

第3固有値を $E_2$ とし、最低2モードと高モードの間隔を

```math
G
=
E_2-E_1
```

とする。測定傾斜 $\varepsilon_m$ と切替時間 $\tau_q$ は

```math
J
\ll
|\varepsilon_m|
\ll
G,
```

```math
\frac{\mathcal J_0}{G}
\ll
\tau_q
\ll
\frac{\mathcal J_0}{J}
```

を満たすように選ぶ。時間尺度の右側 $\tau_q\ll\mathcal J_0/J$ はトンネル振動に対して急な切替、左側 $\mathcal J_0/G\ll\tau_q$ は高モードgapに対して遅い切替を表す。エネルギー尺度 $J\ll|\varepsilon_m|\ll G$ は、離調固定を強くしながら最低2モード窓を保つ条件である。

固定した有限格子W型族では、傾斜演算子の行列要素と時間微分が有界なら、2モード外漏れを

```math
\varepsilon_{2m}
\leq
C_W
\left[
\left(
\frac{|\varepsilon_m|}{G}
\right)^2
+
\left(
\frac{\mathcal J_0}{G\tau_q}
\right)^2
\right]
```

の形で抑えられる。$C_W$ は採用した有限W型族と切替形状に依存する。これは連続空間の一様上界ではない。

深いW型族で $J/G\to0$ なら、例えば

```math
|\varepsilon_m|
=
\sqrt{JG},
\qquad
\tau_q
=
\frac{\mathcal J_0}{\sqrt{JG}}
```

と選べる。このとき4つの比

```math
\frac{J}{|\varepsilon_m|},
\quad
\frac{|\varepsilon_m|}{G},
\quad
\frac{\mathcal J_0}{G\tau_q},
\quad
\frac{J\tau_q}{\mathcal J_0}
```

は全て $\sqrt{J/G}$ の次数で零へ近づく。

## 3.6 傾斜による左右分離固定

分析器操作を終えた直後に傾斜を立ち上げる。2モード射影内では、傾斜保持中の反対側遷移確率は全時刻で

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

を満たす。右から左も同じ上界である。

<!-- theorem-start:theorem -->
**定理（R141：傾斜による左右占有分布の固定）**

最低2モード内の任意の規格化共分散 $C$ について、一定傾斜 $\varepsilon_m$ の保持中の左占有率を $p_L(t)=\operatorname{tr}(|L\rangle\langle L|C(t))$ とする。このとき全時刻で

```math
|p_L(t)-p_L(0)|
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}.
```

特に切替開始時の共分散が $|L\rangle\langle L|$ または $|R\rangle\langle R|$ なら、反対井戸へ移る作用比は $4J^2/(\varepsilon_m^2+4J^2)$ 以下である。一般入力について、2モード内の占有変化と保持中の残留結合を合わせた周辺固定誤差を

```math
\varepsilon_{\rm lock}
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}
+
\varepsilon_{\rm hold}
```

で評価する。全W型系の固定中分布誤差は $\varepsilon_{2m}+\varepsilon_{\rm lock}$ 以下である。$J/G\to0$ の深いW型族では、前節の選択により両者を任意に小さくできる。
<!-- theorem-end:theorem -->

R141が固定するのは左右占有の周辺分布であり、一般入力を左右固有状態へ収縮させる結果ではない。また、周辺分布の固定だけでは、同じ単一試行の実現配置 $X$ が記録時間中ずっと同じ井戸へ滞在することを意味しない。R143では、この経路ごとの局所滞在失敗率を独立の $\varepsilon_{\rm res}$ として仮定する。どちらの枝にいるかは、傾斜前から存在するM47実現配置を局所的に読む。

## 3.7 任意軸分析器

測定軸を単位ベクトル $\boldsymbol n$、射影を

```math
\Pi_{\boldsymbol n,s}
=
\frac12
\left(
I_2+s\boldsymbol n\cdot\boldsymbol\sigma
\right),
\qquad
s\in\{+1,-1\}
```

とする。R140により、有限傾斜列 $A_{\boldsymbol n}$ を

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,+}
A_{\boldsymbol n}^\dagger
=
|L\rangle\langle L|,
```

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,-}
A_{\boldsymbol n}^\dagger
=
|R\rangle\langle R|
```

となるように選べる。入力共分散を $C$ とすると、理想射影重みは

```math
p_s
=
\operatorname{tr}
\left(
C\Pi_{\boldsymbol n,s}
\right).
```

分析器後の共分散は $C'=A_{\boldsymbol n}CA_{\boldsymbol n}^\dagger$ である。実現配置周辺がこの共分散の空間核とmatchingしていれば、左右井戸の実現配置頻度が $p_s$ を有限コントラストで読む。

## 3.8 左右空間読出しの有限コントラスト

左半空間への位置射影を $\Pi_L$ とし、

```math
B_W
=
\langle\phi_0|\Pi_L|\phi_1\rangle
```

と置く。位相規約で $B_W\geq0$ とする。最低2モード上の左読出し効果は、偶奇基底で

```math
E_L
=
\begin{pmatrix}
1/2&B_W\\
B_W&1/2
\end{pmatrix}
```

である。局在基底では

```math
E_L
=
(1-\eta_W)
|L\rangle\langle L|
+
\eta_W
|R\rangle\langle R|,
\qquad
\eta_W
=
\frac12-B_W.
```

従って $0\leq\eta_W\leq1/2$ である。理想分析器後の左占有率は

```math
P_L
=
\eta_W
+
(1-2\eta_W)p_+,
```

なので

```math
|P_L-p_+|
\leq
\eta_W.
```

<!-- theorem-start:proposition -->
**命題（R142：W型左右読出しのBorn型有限誤差）**

分析器終了時にM47の対角matchingが成立し、2モード外漏れを無視できるとする。左、右の実現配置読出しは、任意軸射影重み $p_+,p_-$ から各成分で高々 $\eta_W$ ずれた2値分布を持つ。有限の分析器、傾斜切替、固定、局所記録、境界無反応を加えた結果分布 $p^{\rm obs}$ は、無反応質量を零とした理想分布 $p^{\rm id}$ に対して

```math
D_{\rm TV}
\left(
p^{\rm obs},p^{\rm id}
\right)
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm match}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
```

を満たす。
<!-- theorem-end:proposition -->

有限障壁で $\eta_W$ は一般に零でない。従って生の左右位置読出しを有限パラメータで厳密な射影測定とは呼ばない。深いW型族で $\eta_W\to0$ となる場合に、任意精度極限を持つ非鋭い測定として扱う。

## 3.9 枝別matching

測定記録を $R\in\{L,R,\varnothing\}$ とする。安全枝 $s\in\{L,R\}$ の非規格化共分散を

```math
\widetilde C_s
=
\frac{
\mathbb E
\left[
\mathbf1_{R=s}ZZ^\dagger
\right]
}{
\mathbb E[Z^\dagger Z]
}
```

とする。$p_s=\operatorname{tr}\widetilde C_s>0$ なら条件付き共分散は

```math
C_s
=
\frac{\widetilde C_s}{p_s}
```

である。理想測定操作が必要とする枝別条件は

```math
\widetilde C_s^{\rm out}
\simeq
p_s|s\rangle\langle s|,
\qquad
C_s^{\rm out}
\simeq
|s\rangle\langle s|
```

である。

入力の大域共分散が階数1であることは、この枝別条件を意味しない。結果で条件付けるだけでは、同じ $C$ を2つの異なる射影へ変えられない。測定操作には、実現配置と浴を結果依存に相関させる物理段階が必要である。本章では、井戸ごとに置いた局所記録と準備済みテンプレートの正準交換をこの段階として使う。

## 3.10 実現配置の局所記録

左右井戸の内部に滑らかな検出関数 $\chi_L(X)$、$\chi_R(X)$ を置く。安全な左領域では $(\chi_L,\chi_R)=(1,0)$、安全な右領域では $(0,1)$ とし、分離面近傍を無反応領域とする。2つの記録セルを $(Q_s^R,P_s^R)$ とし、記録Hamiltonianを

```math
H_{\rm rec}(t)
=
g_{\rm rec}(t)
\sum_{s=L,R}
P_s^R\chi_s(X)
```

とする。単位面積パルスでは

```math
Q_s^R
\longmapsto
Q_s^R+\chi_s(X).
```

理想空セルで $P_s^R=0$ なら、記録中の $X$ への反作用は零である。有限準備幅は $\varepsilon_{\rm rec}$ に入れる。$\chi_s$ は各井戸の局所位置だけを読むため、記録装置は統計振幅、共分散、全密度、確率流を参照しない。

傾斜保持時間 $T_{\rm rec}$ は、局所ポインターが安全域を分離できる長さとする。R141により保持中の左右占有周辺変化を $\varepsilon_{\rm lock}$ に抑え、R143では単一試行の経路滞在失敗を別の $\varepsilon_{\rm res}$ に抑えると仮定する。分離面を通過中の試行は無反応として記録し、除外後の2値再規格化を行わない。

## 3.11 結果枝ごとの状態更新

左右井戸に、規格化共分散がそれぞれ

```math
C_L^{\rm tpl}
=
|L\rangle\langle L|,
\qquad
C_R^{\rm tpl}
=
|R\rangle\langle R|
```

となる2モードテンプレートを準備する。安全枝 $s$ では、$\chi_s(X)$ が開く局所交換結合により、信号浴 $Z$ と対応テンプレート $Z_s^{\rm tpl}$ を角 $\pi/2$ だけ正準回転する。測定前の $Z$ は使用済みテンプレートへ移り、写像全体は1対1のままである。

交換後の装置座標では $C_s^{\rm out}=|s\rangle\langle s|$ である。測定前の論理座標へ戻して表すと

```math
A_{\boldsymbol n}^\dagger
C_s^{\rm out}
A_{\boldsymbol n}
=
\Pi_{\boldsymbol n,s}
```

となる。R143の局所滞在条件の下で、実現配置 $X$ は記録終了まで同じ安全井戸へ保持される。有限障壁では局在テンプレートの反対井戸裾が $\eta_W$ あるため、枝別matchingも有限誤差である。

## 3.12 有限誤差instrument定理

<!-- theorem-start:theorem -->
**定理（R143：M47実現配置を傾斜で固定し局所記録する有限誤差instrument）**

固定した入力純粋共分散、測定軸 $\boldsymbol n$、有限観測時間について、次を仮定する。

1. 分析器開始時と終了時にM47の対角matching誤差が $\varepsilon_{\rm match}$ 以下である。
2. R140の傾斜列を2モード制御誤差 $\varepsilon_{\rm ctrl}$ 以下で実装できる。
3. R141の尺度階層により左右占有周辺の変化を $\varepsilon_{\rm lock}$ 以下にでき、さらに完全な局所古典流について、記録終了前に実現配置 $X$ が安全井戸を離れる確率を $\varepsilon_{\rm res}$ 以下にできる。
4. 安全枝で局所記録と結果別テンプレート交換を実行し、枝別交換誤差が $\varepsilon_{\rm br}$ 以下である。
5. 分離面近傍を正式な無反応結果とし、その全質量を $\varepsilon_{\rm guard}$ 以下にできる。

このとき結果集合 $\{+1,-1,\varnothing\}$ を持つ有限正準装置を構成でき、無反応質量を零とした理想Born分布との全変動距離は

```math
\varepsilon_{\rm inst}
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm match}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm br}
```

で抑えられる。安全結果 $s$ の条件付き出力共分散は、分析器座標で $|s\rangle\langle s|$ からtrace距離 $\varepsilon_{\rm br}+O(\eta_W)$ 以内である。記録は実現配置 $X$ の局所関数だけを入力にし、M42/R113またはcurrent transducerを使わない。
<!-- theorem-end:theorem -->

R143は、仮定1に含まれるM47の局所matching保存と、仮定3の経路ごとの局所滞在上界 $\varepsilon_{\rm res}$ を導出しない。従って測定操作の物理部品と誤差合成は明示したが、M47の自然な開放準備と完全な局所 $X$ 力学から全仮定を同時に得た完全定理ではない。

## 3.13 同軸反復と異軸逐次測定

第1測定軸を $\boldsymbol n$ とし、安全結果 $s$ を得た後、装置座標の出力共分散は $|s\rangle\langle s|$ に近い。同じ軸を再測定する場合は同じ左右基底を読むため、反対結果の確率は理想的には零で、有限装置では条件付き状態誤差と第2段誤差の和で抑えられる。

第2軸を $\boldsymbol m$ とする。第1分析器の出力座標から第2分析器へ進む制御を

```math
A_{\boldsymbol m}
A_{\boldsymbol n}^\dagger
```

とすれば、理想条件付き分布は

```math
P(t\mid s)
=
\operatorname{tr}
\left(
\Pi_{\boldsymbol m,t}
\Pi_{\boldsymbol n,s}
\right)
=
\frac12
\left(
1+st\boldsymbol n\cdot\boldsymbol m
\right).
```

2段の実分布と理想逐次分布の全変動距離は、逐次結合により各段の $\varepsilon_{\rm inst}$ と第1段条件付き状態誤差の和で抑えられる。各段は独立な記録セルとテンプレートを使う。無反応試行は結果空間に残す。

## 3.14 永久記録、逆計算、交換reset

外部記録セルは前節の局所剪断で結果を保持する。記録後、分析器時計、傾斜制御器、局所比較器の補助自由度を逆順に戻す。測定前浴情報は使用済みテンプレートにあり、外部記録は逆実行しないため、内部補助だけを戻しても正準可逆性は破れない。

周期末の装置偏差 $\delta a$ を、流入する空セル $\eta_n$ と交換角 $\phi$ で回転すると

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta_n.
```

1周期の逆計算残差を $\varepsilon_{\rm cyc}$、空セル幅を $\|\eta_n\|\leq\sigma_E$ とすれば

```math
\limsup_{n\to\infty}
\|\delta a_n\|
\leq
\frac{
\varepsilon_{\rm cyc}
+
|\sin\phi|\sigma_E
}{
1-|\cos\phi|
}
```

である。旧状態は使用済み外部セルへ移る。永久記録と旧状態を有限閉鎖系の固定容量へ無期限に蓄積するとは主張しない。

## 3.15 条件付き完全周期

<!-- theorem-start:theorem -->
**定理（R144：M47傾斜測定の固定有限弱開放周期）**

固定純粋入力、固定された有限個の傾斜制御、固定された2つの測定軸、任意の有限周期数について、R143の5仮定が各段と各周期で一様に成立するとする。準備、任意軸操作、傾斜分離固定、局所記録、枝別テンプレート交換、2段逐次測定、永久記録、内部逆計算、外部空セル交換からなる有限正準構成を選べる。無反応を含む結果分布誤差は各段の $\varepsilon_{\rm inst}$ の和、周期末偏差は逆計算とresetの上界で抑えられる。能動装置の自由度は固定有限であり、永久記録と使用済み状態のセル数は周期数に比例する。
<!-- theorem-end:theorem -->

R144は自然なmatching準備、切断後保存、周期間の条件付きbath fiber帰還を仮定している。このためQ1-3の完全達成定理ではなく、必要な仮定と装置部品を分離した条件付き構成である。

## 3.16 誤差台帳と資源

Q1測定の中心誤差を

```math
\varepsilon_{Q1}
=
\varepsilon_{\rm prep}
+
\varepsilon_{\rm match}
+
\varepsilon_{2m}
+
\varepsilon_{\rm ctrl}
+
\eta_W
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm br}
+
\varepsilon_{\rm ret}
```

とする。$\varepsilon_{\rm lock}$ は左右占有周辺の変化、$\varepsilon_{\rm res}$ は単一試行の経路滞在失敗であり、同じ量ではない。状態方向誤差、結果分布の全変動距離、記録ポインター誤差、周期末正準座標偏差は単位が異なるため、付録Bで対応するLipschitz定数を通してから合成する。

準備誤差はさらに

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm Xmatch}
+
\varepsilon_{\rm cond}
+
\varepsilon_{\rm cut}
```

と分ける。R145は $\varepsilon_{\rm Hopf}$ のbath方向部分を有限準備時間で抑える。$\varepsilon_{\rm Xmatch}$、$\varepsilon_{\rm cond}$、$\varepsilon_{\rm cut}$ はR145から従わず、Q1-2、Q1-3の残条件である。

1段の能動装置は、信号2モード、左右テンプレート、左右記録セル、傾斜制御、時計、実現配置の局所検出部からなる。固定段数では有限自由度である。正準対の最小数は評価しない。$K$ 周期の永久記録と使用済みテンプレート保存は $O(K)$、固定有限段の制御時間は傾斜パルス数に比例する。

深いW型極限は測定コントラストと固定誤差を小さくする一方、トンネル分裂 $J$ を小さくする。零傾斜の $x$ 回転時間は $O(\mathcal J_0/J)$ なので、精度を高めるほど任意軸操作が遅くなる可能性がある。この精度--時間交換は資源台帳から除外しない。

## 3.17 Q1の達成判定とZeno凍結

本章による現在地は次である。

| 目標 | 現在地 | 根拠 | 残る条件 |
|---|---|---|---|
| Q1-1 | 達成 | R139、R140 | 全W型制御は有限2モード誤差。精度--時間交換を持つ |
| Q1-2 | 部分達成 | R141--R143、R145 | 実現配置・条件付きbathを含む完全matching準備、経路ごとの局所滞在、枝別matchingの一様導出 |
| Q1-3 | 部分達成 | R143--R145 | 周期間matching帰還、切断後保存、総収支 |
| Q1-4 | 未達（凍結中） | — | 判定基準を保持し、反復測定の新規構成・証明・検証を凍結 |

Q1-4の固定目標は削除しない。旧M38の有限Zeno結果は、M42/R113に依存する置換済み模型内の結果としてGit履歴と研究メモへ保存する。M47の傾斜固定は測定保持の一部であり、反復測定間隔に応じたZeno抑制の導出ではない。傾斜でHamiltonianを離調させて遷移を抑える現象をZeno効果と呼ばない。

## 3.18 非主張

本章は次を主張しない。

1. 大域階数1共分散だけから枝別測定後状態が自動的に生じること。
2. M45または具体的回路からR145の採用方程式と完全M47 matching準備を導出したこと。
3. 切断後の局所古典流がmatching fiberを無条件に保存すること。
4. 有限障壁の左右位置読出しが厳密射影になること。
5. 傾斜切替で高モード漏れが厳密に零になること。
6. 局所記録が統計振幅、共分散、確率流を測っていること。
7. 無反応なしの滑らかな厳密2値写像。
8. 固定容量の閉鎖系による無期限の永久記録とreset。
9. Zenoまたは反Zeno効果。
10. M42/R113をQ2・Q3からも撤去したこと。
