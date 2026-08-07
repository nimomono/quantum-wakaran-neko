@number: 2
@chapter: 本文
@title: 有限正準位相担体と階数1相関の準備
@status: 実正準対、複素振幅、保存全位相作用、相関行列、階数1の同値条件、共通源準備は有限次元で厳密である。一般集団の純化、源の反復可能な再初期化、非線形閉包は未完成である。

## 2.1 実正準対と複素振幅

有限モード $i=1,\ldots,L$ に実正準対

```math
\left(Q_i,P_i\right),
\qquad
\left\{Q_i,P_j\right\}
=
\delta_{ij}
```

を置く。固定作用尺度 $\mathcal J_0>0$ を用いて

```math
b_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

と定める。Poisson 括弧は

```math
\left\{
b_i,b_j^*
\right\}
=
-
\frac{i}{\mathcal J_0}
\delta_{ij}
```

である。$b_i$ は実2次元正準平面の表示であり、量子的な生成消滅演算子ではない。

各モードの作用と全位相作用を

```math
I_i
=
\frac12
\left(
Q_i^2+P_i^2
\right)
=
\mathcal J_0
\left|b_i\right|^2,
```

```math
I_{\rm ph}
=
\sum_iI_i
=
\mathcal J_0b^\dagger b
```

とする。$I_{\rm ph}$ は状態に依存する保存量、$\mathcal J_0$ は座標尺度である。

## 2.2 有限2次 Hamiltonian

有限 Hermitian 行列 $h(t)=h(t)^\dagger$ に対して

```math
H_{\rm ph}(t)
=
b^\dagger h(t)b
```

と置く。この量は実数であり、$Q_i,P_i$ だけからなる通常の2次 Hamiltonian である。

<!-- theorem-start:theorem -->
**定理（有限正準位相担体の発展）**
$H_{\rm ph}=b^\dagger hb$ の Hamilton 方程式は

```math
i\mathcal J_0\dot b
=
hb
```

である。$h$ が Hermitian なら $I_{\rm ph}$ は保存される。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
複素 Poisson 括弧から

```math
\dot b_i
=
\left\{b_i,H_{\rm ph}\right\}
=
-
\frac{i}{\mathcal J_0}
\frac{\partial H_{\rm ph}}{\partial b_i^*}
=
-
\frac{i}{\mathcal J_0}
\left(hb\right)_i
```

を得る。また

```math
\frac{d}{dt}
\left(b^\dagger b\right)
=
\frac{i}{\mathcal J_0}
b^\dagger hb
-
\frac{i}{\mathcal J_0}
b^\dagger hb
=
0
```

である。
<!-- theorem-end:proof -->

共通回転 $b\mapsto e^{i\beta}b$ は全位相作用 $I_{\rm ph}$ が生成する。観測可能な混合と干渉は絶対位相でなく、モード間の相対位相に依存する。

## 2.3 局所回転、分岐、再結合

実数 $\epsilon_i(t)$ による局所位相蓄積は

```math
H_{\rm phase}
=
\sum_i
\epsilon_i(t)
\left|b_i\right|^2
```

で実装できる。$i$ と $j$ の2モード混合は

```math
H_{ij}
=
g_{ij}(t)
\left(
b_i^*b_j+b_j^*b_i
\right)
```

または位相をずらした Hermitian 結合で実装できる。有限時間の流れはユニタリ行列 $U$ として

```math
b_{\rm out}
=
Ub_{\rm in},
\qquad
U^\dagger U=I
```

と書ける。ここでユニタリ性は量子仮説でなく、全位相作用を保存する線形正準写像の複素表示である。

経路モード $r$ が局所項 $\epsilon_r(t)|b_r|^2$ に従うなら、相対位相は

```math
\theta_r(t)-\theta_s(t)
=
\theta_r(0)-\theta_s(0)
-
\frac1{\mathcal J_0}
\int_0^t
\left[
\epsilon_r(u)-\epsilon_s(u)
\right]
\,du
```

となる。この式は位相担体が経路差の履歴を保持できることを示す。ただし、積分が粒子の古典作用差と一致することは別の導出を要する。

## 2.4 客観的相関行列

共通調製条件 $\mathcal P$ と観測プログラム $M$ を固定した集団測度を $\mu_{\mathcal P,M}$ とし、

```math
C_M(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
b_t b_t^\dagger
\right]
```

と定める。以下、条件を固定して混同がない場合は添字 $M$ と時刻 $t$ を省く。任意の $v\in\mathbb C^L$ に対して

```math
v^\dagger Cv
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
\left|v^\dagger b\right|^2
\right]
\geq0
```

なので $C$ は正半定値 Hermitian 行列である。対角成分 $C_{ii}$ は局所作用の集団平均、非対角成分 $C_{ij}$ は相対位相相関を保持する。

$C$ は調製条件とプログラムに依存するが、観測者の主観に依存するとは限らない。同じ源、 Hamiltonian 、集団測度を再現すれば同じ $C$ が得られるという意味で、温度や流体密度と同様の客観的な集団状態量として扱う。第4章の固定測定周期では $\mu_{\mathcal P,M}$ の1例を $\mu_{\chi,W}^{\rm cyc}$ として明示するが、一般の相関集団を全て同じ周期測度から生成したとはしない。

## 2.5 セル体積を含む規格化

空間セルの体積を $\Delta V$ とする。連続密度に対応する振幅 $a_i$ を使う場合は、セル体積を吸収した正準振幅

```math
b_i
=
\sqrt{\Delta V}\,a_i
```

を相関行列の定義に用いる。従って

```math
C_{ij}
=
\Delta V
\mathbb E_{\mu_{\mathcal P,M}}
\left[
a_i a_j^*
\right]
```

であり、正規化対角成分

```math
p_i
=
\frac{C_{ii}}{\operatorname{tr}C}
```

は既に規格化セル重みである。$p_i$ へさらに $\Delta V$ を掛けない。

階数1因子を $\chi$ とし、$\chi^\dagger\chi=1$ とする。連続密度表示を

```math
\psi_i
=
\frac{\chi_i}{\sqrt{\Delta V}}
```

と定めれば、

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V,
\qquad
\sum_i p_i=1
```

となる。

## 2.6 階数1条件の意味

<!-- theorem-start:theorem -->
**定理（階数1相関と試行振幅の同値条件）**
$C\neq0$ とする。次の2条件は同値である。

1. $C=\Lambda\chi\chi^\dagger$、$\Lambda>0$、$\chi^\dagger\chi=1$。
2. ある複素確率変数 $c^\omega$ が存在し、$b^\omega=c^\omega\chi$ がほとんど確実に成立する。

このとき $\Lambda=\mathbb E|c^\omega|^2$ である。
<!-- theorem-end:theorem -->

証明は付録Aに置く。この定理により、階数1は「平均すると1方向だけが残る」という弱い条件ではない。各試行の振幅ベクトルが共通射影方向 $\chi$ にあることを要求する。絶対位相と全振幅は試行ごとに異なってよいが、相対振幅と相対位相は共通でなければならない。

従って、旧2成分場模型の標本間コヒーレント集中を単に弱い条件へ置き換えたとは言えない。準備問題の位置を、実在連続場の集中から有限共通源の出力方向へ移したのである。

## 2.7 共通源による階数1準備

入力モードを $e_0$ とし、各試行で

```math
b_{\rm in}^\omega
=
e^{i\beta^\omega}e_0
```

を準備する。$\beta^\omega$ は試行ごとに任意でよい。有限正準準備回路 $U_{\rm prep}$ が

```math
U_{\rm prep}e_0
=
\chi_0,
\qquad
\chi_0^\dagger\chi_0=1
```

を満たすなら、

```math
b_{\rm out}^\omega
=
e^{i\beta^\omega}\chi_0
```

となる。

<!-- theorem-start:proposition -->
**命題（共通源による階数1相関）**
上の準備では、$\mathbb E[b_{\rm out}]=0$ であっても

```math
C_{\rm out}
=
\chi_0\chi_0^\dagger
```

が成立する。
<!-- theorem-end:proposition -->

共通絶対位相を固定する必要はない。必要なのは、1つの源から全モードの相対振幅と相対位相を同じ正準回路で作ることである。

## 2.8 準備回路の物理的範囲

任意の有限次元ユニタリ行列は、2モード混合と局所位相回転の有限列へ分解できる。従って、与えられた $\chi_0$ を準備する有限2次 Hamiltonian 回路は構成できる。

ただし、この事実は任意の量子状態が自然に生成されることを意味しない。$\chi_0$ を装置へ設計値として入れれば、その相対振幅を古典回路へ符号化しただけである。物理源、外部ポテンシャル、境界条件から特定の $\chi_0$ が選ばれる機構は別に示す必要がある。

また、反復運転には次が必要である。

1. 源モードの作用を毎試行同じ範囲へ戻す。
2. 前試行の相対位相情報を不要自由度へ移す。
3. 外部記録を保ったまま有限装置を再初期化する。
4. 源の失敗率を結果依存に除外しない。

本稿は理想準備写像を明示するが、この全再初期化周期を完成していない。

## 2.9 近似階数1

$C$ の固有値を $\lambda_1\geq\lambda_2\geq\cdots\geq0$ とし、主固有ベクトルを $\chi$ とする。階数欠陥を

```math
\varepsilon_{\rm rank}
=
1
-
\frac{\lambda_1}{\operatorname{tr}C}
```

と定める。すると

```math
C
=
\lambda_1\chi\chi^\dagger
+
E,
\qquad
E\geq0,
\qquad
\operatorname{tr}E
=
\varepsilon_{\rm rank}
\operatorname{tr}C
```

である。

純度欠陥

```math
\varepsilon_{\rm pur}
=
1
-
\frac{\operatorname{tr}C^2}{\left(\operatorname{tr}C\right)^2}
```

も使えるが、節の残留強度には $\varepsilon_{\rm rank}$ の方が直接的である。両者を同じ誤差として扱わない。

## 2.10 閉鎖線形発展では純化しない

第3章で示すように、閉鎖線形発展では

```math
C(t)
=
U(t)C(0)U(t)^\dagger
```

となる。従って固有値と $\varepsilon_{\rm rank}$ は保存される。

<!-- theorem-start:corollary -->
**系（閉鎖線形発展による純化の不可能性）**
$\operatorname{rank}C(0)>1$ なら、有限時間の閉鎖線形 Hamiltonian 発展だけで $C(t)$ を階数1にできない。
<!-- theorem-end:corollary -->

これは現行模型の否定的結果である。階数1準備には共通源による初期化、不要成分の補助系への交換、条件付け、弱い外部交換の少なくとも1つが必要になる。後段の厳密な交換子発展をもって、準備まで導出したとは書かない。

## 2.11 非線形項と閉包残差

各試行が

```math
i\mathcal J_0\dot b^\omega
=
h(t)b^\omega
+
r^\omega
```

に従う場合、相関行列は

```math
i\mathcal J_0\dot C
=
\left[h,C\right]
+
D_C,
```

```math
D_C
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
r b^\dagger
-
b r^\dagger
\right]
```

を満たす。Cauchy--Schwarz 不等式により

```math
\left\|D_C\right\|_{\rm op}
\leq
2
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|b\right\|^2
\right)^{1/2}
```

である。

4次以上の Hamiltonian では $r$ が $b$ に非線形に依存し、$D_C$ は一般に4次以上のモーメントを含む。$C$ だけの閉包は自動的に成立しない。本稿は2次模型を厳密な基準とし、準2次模型では有限観測時間内の $D_C$ を主要誤差として追跡する。

## 2.12 階数1条件と標本化の役割分担

階数1条件は、1つの統計振幅 $\chi$ とその Schrödinger 型発展を取り出すために必要である。一方、第4章の正準作用選択器は各試行の実際の作用分配を読むため、有限基底 Born 型標本化それ自体には階数1を要求しない。

従って、次の2つを分ける。

1. 階数1の $C$ から単一因子 $\chi$ を得て、干渉振幅として伝播させること。
2. 一般の正半定値 $C$ に対し、固定全作用と条件付き一様角の下で有限基底結果を標本化すること。

高階数相関行列は第1の目的には単一の $\chi$ を与えないが、第2の目的では正規化行列 $C/\operatorname{tr}C$ の対角要素を結果頻度として与え得る。
