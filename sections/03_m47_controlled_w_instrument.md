@number: 3
@chapter: 本文
@title: Q1 W型2モード制御・測定手順
@status: 旧M47で扱ったQ1系列をM54のW2静的状態構成上の系列固有手順として整理し、R187のM37物理信号系準備、R140操作、R191読出し、R181D 結果成分受渡し、R143--R144、R189A--R189Cの有限Rabi--Zeno比較へ接続する。

## 3.1 Q1 W型2モード手順の主張範囲

物理的な導出の主線は、M37の実振動子運動から弱結合W型の最低2正常モードを経て、M54のW2信号とR140制御へ進む。R187がこの有限時間接続を与える。準備、結果形成、記録は別部分系として接続する。

Q1の1段測定は次の最小手順で行う。

1. 準備済み入力境界で2モード信号方向を準備する。
2. R140/R143の分析器で測定軸の固有方向を左右射影成分へ写す。
3. 共通射影作用保持機構で $J_+,J_-$ を保持する。
4. R191を有限時間走らせ、結果 $r\in\{+,-,\varnothing\}$ を吸収記録へ固定する。
5. 安全な結果ではR181Dのprojector routerで $(P_rZ,(I-P_r)Z)$ を分け、非規格化 $P_rZ$ を次のR140区間へ直接渡す。
6. R143またはR112が必要な外部記録を作る。

固定有限深さでは、次段R191が残った作用和を分母として条件付き確率を読むので、選択結果成分を物理的に規格化し直さない。R144の同軸・異軸逐次分布はこの結果成分受渡しを有限回合成する。R189CのZeno証人では中間R189Aが保持した2作用をR191へ渡し、中間記録や振幅再調整を挟まず走行中信号へ結果成分を返す。

W型ポテンシャル中の粒子位置は信号系の物理実装・空間診断として現れるが、Q1のBorn結果を粒子位置の再平衡化で生成する因果鎖は使わない。Q3の実在粒子位置はR164--R161/R162の別経路で扱う。従ってQ1測定の誤差台帳へR164、R190、R170の選択誤差を加えない。

## 3.2 階数1共分散とBloch球

Pauli行列を $\sigma_x,\sigma_y,\sigma_z$ とし、共分散のBloch成分を

```math
r_k
=
\operatorname{tr}(C_Z\sigma_k)
```

で定める。$C_Z$ はエルミート、正半定値、トレース 1なので

```math
C_Z
=
\frac12
\left(
I_2+\boldsymbol r\cdot\boldsymbol\sigma
\right),
\qquad
|\boldsymbol r|\leq1
```

である。階数1なら $C_Z=cc^\dagger$、$c^\dagger c=1$ と書け、$|\boldsymbol r|=1$ である。$c$ と $e^{i\alpha}c$ は同じ $C_Z$ を与えるため、共通位相は観測状態に含まれない。

一般のエルミート行列 $G(t)$ に対して、古典2モードハミルトニアンを

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
i\mathcal J_0\dot C_Z
=
[G(t),C_Z]
```

に従う。

**R135の2次元系。**

トレース 1の正半定値2次共分散について、階数1条件は $|\boldsymbol r|=1$ と同値である。階数1共分散の集合は共通位相を除いた $\mathbb{CP}^1\simeq S^2$ であり、$H_G$ の古典正準流はこの球面上の回転を与える。従ってQ1の純粋2モード統計状態は、独立した複素振幅場を仮定せずBloch球を持つ。
これはR135を時間依存2モード生成子へ特殊化したものである。共分散の回転は厳密だが、粒子位置周辺の整合保存は別の条件である。

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

と置く。左右の名称は $x_L=\langle L|x|L\rangle<0<x_R=\langle R|x|R\rangle$ となるように $\phi_1$ の符号を固定する。従って $x_{01}=\langle\phi_0|x|\phi_1\rangle<0$ である。以下で $\sigma_z=\operatorname{diag}(1,-1)$ はL、Rの順とし、この規約を途中で変更しない。

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

となる。$\varepsilon=F(x_R-x_L)$ はFの符号を保持する。$-J\sigma_x$ は左右トンネル振動、$\varepsilon\sigma_z/2$ は左右エネルギー差である。

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

この式は、共鳴 $\varepsilon=0$ での完全振動、離調による振幅低下、振動数の変化を同じ信号系で与える。

<!-- theorem-start:theorem -->
**定理（R140：W型2モードの制御、占有振動、傾斜保持）**

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はユニタリ共役であり、トレース、正値性、階数を保存する。零傾斜では角周波数 $(E_1-E_0)/\mathcal J_0$ の左右占有振動を与え、一定傾斜では上の離調公式に従う。さらに射影内の左右占有変化は第3.7節の傾斜保持評価に従う。全W型系で $\varepsilon_{\rm lock}$ を用いる場合は、$J\ll|\varepsilon_m|\ll G$ と $\mathcal J_0/G\ll\tau_q\ll\mathcal J_0/J$ に加え、付録B.5の状態誤差条件を満たすことを仮定する。
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

を満たすように選ぶ。時間尺度の右側 $\tau_q\ll\mathcal J_0/J$ はトンネル振動に対して急な切替、左側 $\mathcal J_0/G\ll\tau_q$ は高モードギャップに対して遅い切替を表す。エネルギー尺度 $J\ll|\varepsilon_m|\ll G$ は、離調固定を強くしながら最低2モード窓を保つ条件である。

固定した有限格子W型族では、制御中の高モード結合 $v=\sup_t\|(I-P_2)(-F(t)x)P_2\|$ と高モード間隔を別に測る。傾斜行列要素と切替形状を固定した断熱的評価で得る

```math
\ell_{2m}\lesssim C_W\left[(v/G)^2+(\mathcal J_0/(G\tau_q))^2\right]
```

は高モード漏れ確率の次数評価であり、全状態または左右測定分布の誤差ではない。$C_W$、初期準備、制御中の間隔、微分上界への依存を固定する必要があり、任意の駆動に対する一様定理とはしない。分布誤差台帳の $\varepsilon_{2m}$ は、付録B.5で定義する全状態差からの上界を使う。漏れが小さくても低モード内の位相補正は蓄積し得る。

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

は全て $\sqrt{J/G}$ の次数で零へ近づく。ただし、この $\tau_q$ は「高モードには遅く、トンネルには速い」という診断用の中間尺度であり、R187の滑らかな 切替誤差を小さくするための必須選択ではない。実際に $|\varepsilon_m|\tau_q/\mathcal J_0=O(1)$ なので、これだけから瞬時クエンチとの差が小さいとはいえない。R187では小振幅の区分一定 制御を先に閉じ、必要なら短い $C^1$ ランプを別誤差 $\varepsilon_{\rm sw}$ として評価する。

### 3.5.1 R140のM37実装に関する条件付き系

M37の有限W型制御を第6.17節で定義する。同じ初期実座標、同じ制御列、同じ時間区間で、実運動の包絡 $b$、全W型の有効解、2モード解を比較する。$V(t)^\dagger V(t)=I_2$ とし、$g(t)=g(t)^\dagger$ に対して $i\mathcal J_0\dot c=g(t)c$、$\|c(0)\|=1$ とする。共通位相を除く場合はその位相をVへ含める。

<!-- theorem-start:corollary -->
**系（R140のM37有限時間制御受渡し）**

実運動と同じ初期値から始めた全W型有効解との差が区間全体で $\varepsilon_{\rm env}$ 以下とする。等長埋込みVは連続かつ区分的に微分可能とし、残差を

```math
R(t)=h_W(t)V(t)-i\mathcal J_0\dot V(t)-V(t)g(t)
```

と定義する。初期差 $d_0=\|b(0)-V(0)c(0)\|$ に対し

```math
\|b(T)-V(T)c(T)\|
\leq\varepsilon_{\rm env}+d_0+
\frac1{\mathcal J_0}\int_0^T\|R(t)\|\,dt
```

が成立する。目標のSU(2)操作への合成誤差は別に加える。
<!-- theorem-end:corollary -->

証明は付録B.17。固定基底では $\dot V=0$ として漏れ結合と有効位相を評価する。瞬間固有基底では基底移動項を落とさない。この系は一般の誤差接続道具として残す。ただし固定基底では傾斜結合が $O(F)$、保持時間が $O(F^{-1})$ となり得るため、積分残差が小さくならない場合がある。第6章R187は弱結合W型族の結合後の低2モード部分空間と静的正常モード較正を使い、この粗い障害を回避して任意精度の物理信号系族を構成する。

零傾斜完全移送時間は $T_X=\pi\mathcal J_0/(2J)$ である。一般のR86 Duhamel上界をこの長時間へ機械的に掛けると粗くなる。R187では各静的 区間の厳密正常モード生成子 $f_{\omega_0}(h)$ が同じ固有ベクトルを共有することを使い、実際の低2分裂で保持時間を較正するため、信号系誤差を保持時間非依存の $\delta_{\rm loc}$ 型へ戻す。初期共通位相の異なる試行にも同じ全状態上界を適用し、R135の集団輸送へ接続する。Born型選択、粒子輸送、測定周期は本系とR187の結論に含めない。

### 3.5.2 R187からQ1制御誤差への受渡し

R187の零傾斜最低2正常モードをM54のW2静的状態構成の信号部分系と同定する。初期接続端誤差を含む全状態差を $\varepsilon_{187}$ とすると、低2モードへの射影後に成功結果成分だけを再規格化して誤差を小さく見せるのではなく、full 状態のままR135/R168へ渡す。必要に応じて低2signalを規格化して比較する場合は、E.9の規格化写像を使い

```math
\left\|
\widehat Z_{W2}^{\rm phys}
-
e^{i\alpha}Uc
\right\|
\leq
\frac{2\varepsilon_{187}}
{1-\varepsilon_{187}}
```

と評価する。

R143の誤差台帳では、従来独立に置いていた全W型制御側の $\varepsilon_{\rm ctrl}+\varepsilon_{2m}$ を、R187を採用する運転では上の全状態 接続誤差から一貫して評価する。同じM37偏差を信号系誤差、状態方向誤差、Born分布誤差へ重複加算しない。R191の読出し・吸収記録誤差は別部分系なのでR187へ吸収しない。R164/R190/R170の作用殻型代替経路を選ぶ場合もその誤差をR187へ吸収しない。

## 3.6 M54静的/R191のQ1二結果成分特殊化

Q1ではM54静的状態構成に
$v=z$、$\mathcal I=\{L,R\}$、$\Psi=\Phi$
を代入する。第2章のR164により

```math
\pi_i^\delta(z)
=
\frac{|(\Phi z)_i|^2/(z^\dagger z)+\delta q_i}{1+\delta}
```

が2作用殻の規格化状態数として得られる。Q1の2結果主線ではR191がブラウン巨視的スピンの吸引域測度から有限時間Born読出しと吸収記録を与える。R164/R161/R190/R179/R170は一般有限結果集合と作用殻型の代替実現として残す。従ってQ1章で独立に必要なのは、W型信号の準備と分析器、左右固定、局所位置記録との接続である。結果選択と階数1 測定後状態更新は第2章の共通射影選別機構へ共通化し、別の結果別状態テンプレートを置かない。

作用殻を消去した条件付き中間状態有効自由エネルギーは

```math
E_i^\delta(z)=-\Theta\log\pi_i^\delta(z)
```

である。第2章の粗視化経路熱力学系は、解析器クエンチと粒子位置遷移の正逆経路比、積分ゆらぎ関係、相対有効散逸を監査する。ただしこれはHopf ポンプ、作用殻準備、信号浴保持、記録、テンプレート交換、リセットを含む全周期の機械仕事・微視的熱収支ではない。

## 3.7 R140の傾斜保持節

分析器操作を終えた直後に傾斜を立ち上げる。2モード射影内では、傾斜保持中の反対側遷移確率は全時刻で

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

を満たす。右から左も同じ上界である。

**R140の傾斜保持評価。**

最低2モード内の任意の規格化共分散 $C_Z$ について、一定傾斜 $\varepsilon_m$ の保持中の左占有率を $p_L(t)=\operatorname{tr}(|L\rangle\langle L|C_Z(t))$ とする。このとき全時刻で

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

で評価する。全W型系の固定中分布誤差は $\varepsilon_{2m}+\varepsilon_{\rm lock}$ 以下である。$J/G\to0$ の深いW型族では、前節の選択により射影内の固定誤差を小さくできる。全W型系については同時に $\varepsilon_{2m}$ を小さくする条件が必要である。
R140が固定するのは信号浴の左右占有周辺であり、一般入力を左右固有状態へ収縮させる結果ではない。周辺固定だけから単一試行の粒子位置 $X$ の経路滞在は従わない。そこで静的選択終了後に選択浴を切り、R170の吸収指針変数へ固定する。記録時間中の離脱失敗率 $\varepsilon_{\rm res}$ は、有限障壁裾、エネルギー切断、閾値平滑化、時計ずれから評価する。どちらの結果成分にいるかは、ゲート閉鎖前から存在するM47粒子位置を局所的に読む。

## 3.8 任意軸分析器

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

となるように選べる。入力共分散を $C_Z$ とすると、理想射影重みは

```math
p_s
=
\operatorname{tr}
\left(
C_Z\Pi_{\boldsymbol n,s}
\right).
```

分析器後の共分散は $C_Z'=A_{\boldsymbol n}CA_{\boldsymbol n}^\dagger$ である。分析器中は粒子位置周辺がこの共分散を追跡しなくてよい。終了後の信号浴方向を固定し、R161の再平衡化を時間 $T_X$ だけ作用させれば、左右井戸の粒子位置頻度が $p_s$ を有限コントラストと有限混合誤差で読む。

## 3.9 左右空間読出しの有限コントラスト

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

**R143で使う有限コントラスト評価。**

分析器終了後にR164の作用殻準備とR161、R162の粒子位置再平衡化を時間 $T_X$ だけ作用させ、その誤差を $\varepsilon_{\rm eq}$ とする。左、右の粒子位置読出しは、任意軸射影重み $p_+,p_-$ から各成分で高々 $\eta_W+\varepsilon_{\rm eq}$ ずれた2値分布を持つ。有限の分析器、傾斜切替、固定、局所記録、境界無反応を加えた結果分布 $p^{\rm obs}$ は、無反応質量を零とした理想分布 $p^{\rm id}$ に対して

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
\varepsilon_{\rm eq}
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

有限障壁で $\eta_W$ は一般に零でない。従って生の左右位置読出しを有限パラメータで厳密な射影測定とは呼ばない。深いW型族で $\eta_W\to0$ となる場合に、任意精度極限を持つ非鋭い測定として扱う。


## 3.10 結果条件付けと測定後状態の物理的受け渡しの分離

測定記録を $R\in\{L,R,\varnothing\}$ とする。入力の大域共分散が階数1で
$C_Z=cc^\dagger$
なら、結果事象だけで条件付けても、選別機構前の各安全な結果成分の信号方向は一般に同じ $c$ のままである。したがって、Born型結果成分を選ぶことと、測定後固有状態を物理的に作ることは別の操作である。

Q1では分析器座標の階数1 射影子を

```math
P_s=|s\rangle\langle s|,
\qquad
s\in\{L,R\}
```

とする。R191で安全な結果成分 $s$ を吸収記録へ固定した後、R181Dの制御付き射影選別機構を作用させる。理想選択後信号は

```math
Z_s^{\rm sel}
=
P_sZ
=
\langle s|Z\rangle |s\rangle
```

なので、安全な結果成分では規格化方向が必ず $|s\rangle$ である。R181Dの方向を変えない振幅再調整はこの方向を変えない。選別機構誤差を含む条件付き状態誤差は第2章の
$\varepsilon_{\rm node}^{\rm state}$
で評価する。

有限W型の左右コントラスト $\eta_W$ は「どの結果成分が記録されるか」という結果分布の偏差へ入るが、選択結果の固定後に階数1の選別機構が作る信号方向の誤差へ重ねて入れない。結果分布誤差と測定後状態 トレース距離は別の量として管理する。

測定終了時に粒子位置 $X$ を新しい信号方向へ再平衡化する必要はない。$X$ は局所記録が完了するまで安全井戸へ保持し、選択後信号は同じ単一試行のまま次の制御区間へ渡す。次の測定面に到達した時点で、改めてR191を有限時間だけ作用させる。これにより全時刻の配置--信号整合も、結果依存の外部状態再準備も仮定しない。

## 3.11 粒子位置の局所記録

左右井戸の内部に滑らかな検出関数 $\chi_L(X)$、$\chi_R(X)$ を置く。安全な左領域では $(\chi_L,\chi_R)=(1,0)$、安全な右領域では $(0,1)$ とし、分離面近傍を無反応領域とする。2つの記録素子を $(Q_s^R,P_s^R)$ とし、記録ハミルトニアンを

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

理想空素子で $P_s^R=0$ なら、記録中の $X$ への反作用は零である。有限準備幅は $\varepsilon_{\rm rec}$ に入れる。$\chi_s$ は各井戸の局所位置だけを読むため、記録装置は統計振幅、共分散、全密度、確率流を参照しない。

傾斜保持時間 $T_{\rm rec}$ は、局所ポインターが安全域を分離できる長さとする。R140により保持中の信号浴左右占有変化を $\varepsilon_{\rm lock}$ に抑える。R170により、静的選択終了後の指針変数未捕獲または有限漏れを $\varepsilon_{\rm res}$ に抑える。分離面を通過中の試行、ゲート閉鎖失敗、有限閾値帯は無反応として記録し、除外後の2値再規格化を行わない。


## 3.12 共通射影選別機構による測定後状態の受け渡し

分析器終了後、R191で安全な結果成分 $s$ を吸収記録へ固定し、必要なら3.11の局所記録へ結果を写す。信号と未使用 選別機構用作業領域に対し、第2章R181Dの

```math
F_s
=
\begin{pmatrix}
P_s&P_{1-s}\\
P_{1-s}&-P_s
\end{pmatrix}
```

を選択機構制御で作用させる。すると

```math
F_s(Z,0)
=
(P_sZ,P_{1-s}Z)
```

となり、選択成分は信号側、除外成分は作業領域/R179の流出浴へ残る。異なる入力を同じ出力へ消去する写像ではなく、拡大状態上の1対1の選別機構である。

階数1 $P_s=|s\rangle\langle s|$ では、安全な結果成分の選択後信号は位相と振幅因子を除いて $|s\rangle$ そのものである。準備済み入力境界の $\kappa=0$ 方向を変えない振幅再調整用接続端を選択後信号だけに開けば、作用を標準範囲へ戻しても状態方向は変わらない。R181Dの選別機構実装誤差が $\eta_F<\sqrt{\tau_{\rm state}}$ なら

```math
D_{\rm tr}
\left(
C_s^{\rm out},
|s\rangle\langle s|
\right)
\leq
\varepsilon_{\rm node}^{\rm state},
\qquad
\varepsilon_{\rm node}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}.
```

測定前の論理座標へ戻すと

```math
A_{\boldsymbol n}^\dagger
C_s^{\rm out}
A_{\boldsymbol n}
\simeq
\Pi_{\boldsymbol n,s}.
```

結果成分ごとの固有状態テンプレートは使わない。測定前信号の非選択成分は選別機構用作業領域へ、方向を変えない振幅再調整で環境へ渡る情報はR179の流出浴へ残す。選択後信号は同じ試行の次段へ直接渡し、次の測定面でのみ新しいR191読出しを走らせる。


## 3.13 R143：Q1 W型2モード読出しと射影選別機構受渡し

Q1の1段測定では、R140の分析器後に左右2作用を保持し、R191で排他的結果を選択・吸収記録する。R181Dの階数1選別機構が同一試行信号を対応する射影子像へ移し、必要なら局所記録へ結果を写す。有限W型の左右空間コントラストによる位置読出しは独立な代替・診断であり、R191主線のBorn重み生成には使わない。

<!-- theorem-start:theorem -->
**定理（R143：Q1 W型2モード読出しと射影選別機構受渡し）**

固定純粋入力、測定軸 $\boldsymbol n$、有限観測時間について/R187の信号準備、R140分析器、左右射影作用保持、R191、R181Dの階数1選別機構を同じ安全集合で実行できるとする。準備誤差を $\varepsilon_{\rm prep}$、分析器とW2接続誤差を $\varepsilon_{\rm ctrl}+\varepsilon_{2m}$、R191完全結果誤差を $\varepsilon_{191}$、選別・転送を含む節点誤差を $\varepsilon_{\rm node}^{\rm dist}$ とする。このとき

```math
\varepsilon_{\rm inst}
\leq
\varepsilon_{\rm prep}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{191}
+\varepsilon_{\rm node}^{\rm dist}
```

で理想2結果Born分布との差を抑えられる。無反応を同じ完全結果集合に残す。

R191のdispatcherから得る $\tau_{\rm state}>0$ と選別機構誤差 $\eta_F<\sqrt{\tau_{\rm state}}$ に対し、安全結果 $s$ の条件付き出力共分散は

```math
D_{\rm tr}
\left(C_s^{\rm out},|s\rangle\langle s|\right)
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}
=:\varepsilon_{\rm node}^{\rm state}.
```

結果別固有状態テンプレート、外部トモグラフィー、成功試行の再規格化は使わない。
<!-- theorem-end:theorem -->

R143の利用単位は1回の測定であり、複数回履歴はR144で合成する。左右空間位置を直接読む旧有限コントラスト経路はW型固有の代替検証として3.9--3.11に残し、その $\eta_W$ や再平衡化誤差をR191主線へ重複加算しない。

## 3.14 同軸反復と異軸逐次測定

第1測定軸を $\boldsymbol n$ とし、安全結果 $s$ を得た後、R181Dの階数1の選別機構後の同じ信号は、分析器座標で $|s\rangle\langle s|$ からトレース距離 $\delta_{\rm state}$ 以内にある。同じ軸を再測定する場合、理想反対結果の確率は零であり、有限装置では段間状態誤差と第2段測定機構誤差で抑えられる。

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

段間では選択後信号をそのままR140制御へ渡す。分析器中に粒子位置が信号へ追従することは要求せず、次の測定面でR164--R190--R179--R170の整合を新たに実行する。外部制御器が状態トモグラフィー、係数読出し、結果依存状態再準備を行わない。

固定有限段では結果履歴を

```math
h=(r_1,\ldots,r_N),
\qquad
r_j\in\{+1,-1,\varnothing\}
```

とする。安全履歴 $s_1,\ldots,s_N$ の理想分布は

```math
P_{\rm id}(s_1,\ldots,s_N)
=
\operatorname{tr}
\left(
\Pi_{\boldsymbol n_1,s_1}C_{\rm in}
\right)
\prod_{j=2}^N
\operatorname{tr}
\left(
\Pi_{\boldsymbol n_j,s_j}
\Pi_{\boldsymbol n_{j-1},s_{j-1}}
\right).
```

無反応を含む履歴は捨てず、理想側に零質量の履歴を追加した同じ完全結果空間で比較する。


## 3.15 R144：固定有限段逐次測定合成

<!-- theorem-start:theorem -->
**定理（R144：Q1 W型2モード固定有限段逐次測定合成）**

固定純粋入力、固定有限段数 $N$、固定した測定軸列 $\boldsymbol n_1,\ldots,\boldsymbol n_N$ を取る。各段でR143の4条件が成立し、段 $j$ のR181Dの選択後信号を同じ試行の段 $j+1$ へ直接渡せるとする。段間にはR140で許された固定有限の正準制御列を挿入してよい。各段は有限個の記録素子、浴接続部、選択機構/選別機構用作業領域、振幅再調整用接続端の環境を使用し、無反応を含む履歴を列の終了まで保持する。

このとき完全履歴空間

```math
\mathcal H_N
=
\{+1,-1,\varnothing\}^N
```

上の有限正準・弱開放逐次測定機構を構成できる。理想逐次分布を $p_N^{\rm id}$、実分布を $p_N^{\rm obs}$ とし、段 $j$ の1段測定機構誤差を $\varepsilon_{{\rm inst},j}$、安全出力共分散の理想射影からのトレース距離を $\delta_{{\rm state},j}$ とすれば、

```math
D_{\rm TV}
\left(
p_N^{\rm obs},p_N^{\rm id}
\right)
\leq
\sum_{j=1}^{N}
\varepsilon_{{\rm inst},j}
+
\sum_{j=1}^{N-1}
\delta_{{\rm state},j}.
```

ここでトレース距離は $D_{\rm tr}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1$ とする。任意の2値効果による確率差は $D_{\rm tr}$ 以下なので、段間状態誤差の係数は1である。同軸列では理想反対結果の重みは零、異軸列では各安全条件付き核は

```math
\operatorname{tr}
\left(
\Pi_{\boldsymbol n_j,s_j}
\Pi_{\boldsymbol n_{j-1},s_{j-1}}
\right)
```

となる。固定有限 $N$ に必要な能動部と履歴素子数は有限であり、外部から量子状態を再準備しない。
<!-- theorem-end:theorem -->

R144はR143の1段測定機構を固定有限回だけ合成する定理であり、R181Dの測定後状態の受け渡しを段間接続部とする。永久記録、内部逆計算、周期末リセットを結論に含めない。全時刻の整合保存または周期間整合帰還も仮定せず、各測定面でR191を有限時間だけ走らせる。本定理はZeno効果そのものを示さず、測定中も零傾斜Rabi項を止めない対照との接続は別の未達課題である。


## 3.16 実装強化：永久記録、補助逆計算、交換リセット

R144の固定有限履歴を列終了後も保持し、補助制御器を次周期へ戻す場合の追加構成をここに分離する。この構成はQ1-2の達成条件ではない。

安全な結果成分の選択後信号はR181Dの測定後状態として保持する。除外成分は選別機構用作業領域、振幅情報は振幅再調整用接続端の環境、結果相関環境履歴はR179の流出浴へ流す。局所記録を外部素子へ保持した後、結果と測定後状態を担わない時計、傾斜駆動器、比較補助だけを逆順に戻してよい。制御付き射影選別機構を測定後状態保持中に逆実行して測定前信号へ戻すこと、また採用開放方向を変えない振幅再調整の環境履歴を消して逆転することは要求しない。

補助座標の周期末偏差 $\delta a$ を、流入する空素子 $\eta_n$ と交換角 $\phi$ で回転すると

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta_n.
```

1周期の補助逆計算残差を $\varepsilon_{\rm cyc}$、空素子幅を $\|\eta_n\|\leq\sigma_E$ とすれば

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
}.
```

**系（固定有限周期の補助逆計算・交換リセット）。**

固定有限段の結果を外部記録へ写し、結果相関情報と散逸履歴をR179の流出浴へ流した後、結果を担わない補助自由度だけを逆順に戻して開放リセットする。有限浴容量で無期限運転することは主張せず、その問題は有限閉鎖実装の強化課題へ分離する。

この系はR144の根拠条件ではない。Hopf ポンプ、作用殻、信号保持制御器、浴接続部、射影型 選別機構、方向を変えない振幅再調整、記録、リセットを含む総仕事、総熱、総エントロピー生成を一つの恒等式へ閉じる問題も引き続き未解決である。


## 3.17 誤差・熱力学・資源台帳

Q1のR191主線では1段結果分布誤差を

```math
\varepsilon_{Q1}^{\rm dist}
=
\varepsilon_{\rm prep}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{191}
+\varepsilon_{\rm node}^{\rm dist}
```

と整理し、R191内部の混合、transducer、保護帯、有限温度retreat、有限decision時間、吸収記録を別項として二重加算しない。安全結果の測定後状態誤差は

```math
\varepsilon_{Q1}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}
```

で別管理する。R144では各段の結果分布誤差と次段へ伝わる状態方向誤差を有限和へ入れる。

熱力学台帳では分析器仕事、R191のmixing/decision浴、吸収記録、可逆選別機構、必要な振幅再調整、リセットを分ける。R164/R190/R170の作用殻型代替経路を選ぶ場合、その作用殻仕事・混合・renewal・固定資源は代替経路だけへ計上する。有限閉鎖Hamiltonian全系への統合は固定目標ではない。

1段のR191主線の能動装置は、2モード信号、作用保持指針変数、ブラウン巨視的スピン、吸収記録、選別機構用作業領域、必要な記録素子と傾斜制御からなる。固定有限段では未規格化選択成分を次段へ直接渡し、一般深さで作用下限が必要な場合だけ方向を変えない振幅再調整を使う。

## 3.18 W2走行中作用容量の有限正準保持

Q1-2のZeno比較では、中間測定のために零傾斜Rabiを停止しない。R187の零傾斜W2信号を $Z_\kappa(t)$ とし、厳密な低2モード分裂から

```math
\Omega_\kappa
=
\frac{\Delta_{\rm ex}(0)}{\mathcal J_0}
```

を定める。左右射影子 $P_L,P_R$ に対する未処理作用を

```math
J_b(Z)=\mathcal J_0 Z^\dagger P_b Z,
\qquad
b\in\{L,R\}
```

とする。第2.13節の直交射影子作用保持機構を、停止した信号ではなく走行中W2へ有限時計窓で作用させる。

<!-- theorem-start:lemma -->
**補題（R189A：W2走行中作用容量有限正準保持）**

時刻 $t_\ell$ を中心とする非負で偶な滑らかな有限支持関数 $\chi_\ell$ を取り、

```math
\chi_\ell(s)=\chi_\ell(-s),
\qquad
\int \chi_\ell(s)\,ds=1
```

とする。2個の未使用正準指針変数対 $(A_b,P_b^J)$ を用意し、

```math
H_{\rm cap}(t)
=
\chi_\ell(t-t_\ell)
\sum_{b=L,R}P_b^J J_b(Z)
```

を零傾斜Rabi Hamiltonianへ加える。理想未使用条件 $P_L^J=P_R^J=0$ から開始すれば、全保持窓で $P_b^J=0$ が保たれ、保持機構からW2信号への追加Hamiltonian項は零である。従って理想W2信号は同じ区間の自由零傾斜Rabi信号と厳密に一致する。

指針変数増分を $\bar J_b$ と書くと

```math
\bar J_b
=
\int \chi_\ell(s)J_b(t_\ell+s)\,ds,
\qquad
\bar J_L+\bar J_R=J_\Sigma
```

である。$D=J_L-J_R$ に対して

```math
\bar D
=
c_\chi D(t_\ell),
\qquad
c_\chi
=
\int \chi_\ell(s)\cos(\Omega_\kappa s)\,ds
```

が成り立つ。第2モーメント $\mu_2=\int s^2\chi_\ell(s)\,ds$ とすると、固定較正による逆補正を使わない場合でも規格化左右作用比の各成分誤差は

```math
\varepsilon_{\rm avg}
\leq
\frac{\Omega_\kappa^2\mu_2}{4}
```

で抑えられる。$c_\chi\neq0$ なら、固定正準スケーリングにより理想W2の中心時刻作用を厳密に復元してもよい。

有限未使用運動量、W2接続端、時計自由度、較正の偏差をそれぞれ $\varepsilon_P,\varepsilon_{\rm port},\varepsilon_{\rm clk},\varepsilon_{\rm cal}$ とすると、保持済み作用比の全変動距離誤差を

```math
\varepsilon_{189A}
\leq
\varepsilon_{\rm avg}
+\varepsilon_P
+\varepsilon_{\rm port}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm cal}
```

とできる。高モードへ恒等作用する正確なR187 W2接続端では保持機構自身による高モード励起は生じない。
<!-- theorem-end:lemma -->

R189Aは完全QND測定を主張しない。$J_L,J_R$ は零傾斜Rabi自身により時間変化する。主張するのは、作用保持相互作用自身の反作用が理想未使用指針変数上で零であり、有限窓平均を明示評価できることである。

## 3.19 W2走行中階数1射影選別の有限時間接続

R189A終了後は固定済み左右作用 $\bar J_L,\bar J_R$ を走行中W2信号から切り離してR191へ渡し、その吸収記録 $S_{\rm lock}\in\{L,R,\varnothing\}$ が固定された後に制御付き選別機構を開く。中間測定では傾斜、局所外部記録、方向を変えない振幅再調整を使わない。

<!-- theorem-start:theorem -->
**定理（R189B：W2走行中階数1射影選別有限時間接続）**

R189Aの保持中心時刻を $t_\ell$ とする。保持済み2作用をR191へ渡し、有限decision時間後に潜在結果 $S_{\rm lock}$ を固定する。安全結果 $b$ ではR181Dの階数1対合選別機構 $F_b$ を有限時間 $\tau_F$ だけ作用し、その完了時刻を実効測定時刻 $t_m$ と定める。全操作中で零傾斜Rabi項を停止しない。

選別機構単独の理想作用を $F_b$、有限実装・接続端・時計偏差を含む誤差を $\eta_F^{\rm run}$ とすれば

```math
\eta_F^{\rm run}
\leq
\eta_F
+\Omega_\kappa\tau_F
+\varepsilon_{\rm port,F}
+\varepsilon_{\rm clk,F}.
```

また

```math
|p_b(t_m)-p_b(t_\ell)|
\leq
\varepsilon_{\rm lat},
\qquad
\varepsilon_{\rm lat}
=\frac{\Omega_\kappa}{2}(t_m-t_\ell).
```

従って実効測定時刻のBorn分布との全変動距離は

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+\varepsilon_{191}^{\rm mid}
+\varepsilon_{\rm lat}
```

で抑えられる。R191の無反応は完全結果へ残す。選別時刻で $p_b(t_m)\geq p_*>0$ かつ $\eta_F^{\rm run}<\sqrt{p_*}$ なら

```math
\varepsilon_{189B}^{\rm state}
\leq
\frac{2\eta_F^{\rm run}}{\sqrt{p_*}-\eta_F^{\rm run}}.
```

無反応では $F_L,F_R$ のどちらも作用させず、W2信号は零傾斜Rabiを継続する。
<!-- theorem-end:theorem -->

固定有限回のZeno証人では各安全結果に固定正下限を取れるため、中間振幅再調整を省ける。

## 3.20 R189C：有限2回Rabi--Zeno比較

一般の有限 $N$ について理想射影核を合成すれば

```math
P_N(T)
=
\frac{1+\cos^N(\Omega_\kappa T/N)}{2}
```

となるが、Q1-2の達成証人には一般 $N$ や $N\to\infty$ を必要としない。本章では最大誤差余裕を明瞭にするため $N=2$ を固定する。

<!-- theorem-start:theorem -->
**定理（R189C：M37 W2有限2回Rabi--Zeno比較）**

R187の同じ零傾斜M37 W2信号系を使い、初期状態を $P_L$、総物理時間 $T$ を

```math
\Omega_\kappa T
=
\frac{\pi}{2}
```

で固定する。測定なし自由対照では終端 $L$ 確率は

```math
P_{\rm free}^{\rm id}
=
\frac12
```

である。

測定運転では、実効時刻 $t_m=T/2$ にR189AとR189Bによる1回の走行中階数1射影選別を完了し、その後も $T$ まで同じ零傾斜Rabiを作用する。終端だけを全対照に共通のR143/R181D読出しで測る。理想終端 $L$ 確率は

```math
P_{\rm meas}^{\rm id}
=
\frac34
```

であり、理想Zeno余裕は

```math
\Delta_Z
=
P_{\rm meas}^{\rm id}-P_{\rm free}^{\rm id}
=
\frac14
```

である。

中間区間の

```math
a=\cos^2\frac{\pi}{8}
=
\frac{2+\sqrt2}{4},
\qquad
q=\sin^2\frac{\pi}{8}
=
\frac{2-\sqrt2}{4}
```

を用いると、無反応を除く理想完全履歴は

```math
P(++ )=a^2,
\qquad
P(+-)=aq=\frac18,
\qquad
P(-+)=q^2,
\qquad
P(--)=qa=\frac18
```

であり、反転後の再反転履歴 $-+$ も正の重みを持つ。実装では同じ履歴空間へ無反応を加え、事後選別しない。

空操作対照では、測定運転と同じR189A、R191読出し、吸収記録、時計自由度、待ち時間を用いるが、走行中W2へ $F_b$ を作用させない。理想未使用指針変数と切断条件では、この対照のW2信号は全時間で自由Rabi信号と一致する。

実測定、空操作、自由対照の終端確率が

```math
\left|P_{\rm meas}^{\rm obs}-\frac34\right|
\leq
\varepsilon_{\rm meas},
\qquad
\left|P_{\rm empty}^{\rm obs}-\frac12\right|
\leq
\varepsilon_{\rm empty},
\qquad
\left|P_{\rm free}^{\rm obs}-\frac12\right|
\leq
\varepsilon_{\rm free}
```

を満たすなら

```math
P_{\rm meas}^{\rm obs}
-P_{\rm empty}^{\rm obs}
\geq
\frac14
-\varepsilon_{\rm meas}
-\varepsilon_{\rm empty}
```

である。従って

```math
\varepsilon_{\rm meas}+\varepsilon_{\rm empty}
<
\frac14
```

を満たす有限パラメータ選択では正のZeno型遷移抑制余裕が残る。また

```math
|P_{\rm empty}^{\rm obs}-P_{\rm free}^{\rm obs}|
\leq
\varepsilon_{\rm empty}+\varepsilon_{\rm free}
```

なので、作用保持、R191のmixing/decision、吸収記録、待ち時間だけによる抑制を別に監査できる。

R187の弱結合極限では $\Omega_\kappa\to0$ であり、固定精度のR191 decision時間と有限選別時間を保ったまま $\varepsilon_{\rm lat}$ と $\Omega_\kappa\tau_F$ を任意に小さくできる。R189Aの有限幅誤差も $O(\!\Omega_\kappa^2)$ である。R191/R181DについてQ1測定統計で採用する指定誤差条件の下で、各有限誤差を順に十分小さく選べるため、上の $1/4$ 条件を満たす有限構成が存在する。
<!-- theorem-end:theorem -->

中間測定では傾斜を一切使わない。従って傾斜離調、障壁増大、Hamiltonian停止、摩擦、方向を変えない振幅再調整、事後選別はR189Cの抑制機構ではない。終端読出しに用いる傾斜固定は $t=T$ より後で全対照に共通に置く。

## 3.21 誤差・資源台帳とQ1の達成判定

R189Cの測定運転誤差は、同じ物理偏差を一度だけ数えて粗く

```math
\varepsilon_{\rm meas}
\leq
\varepsilon_{\rm car}
+\varepsilon_{189A}
+\varepsilon_{191}^{\rm mid}
+\varepsilon_{\rm lat}
+\varepsilon_{189B}^{\rm state}
+\varepsilon_{\rm term}
```

と整理できる。空操作対照には $\varepsilon_{189B}^{\rm state}$ を入れず、作用保持系の反作用、固定済み容量処理の残留結合、終端読出しを数える。中間傾斜誤差、中間局所記録誤差、中間振幅再調整誤差は零と選ぶ。

固定 $N=2$ では最小理想条件付き結果確率は

```math
q
=
\frac{2-\sqrt2}{4}
>0.14
```

なので、例えば固定 $p_*=0.10$ と $\tau_{\rm state}<p_*$ を選べる。R189Aと時間ずれ誤差を $q-p_*$ 未満にすれば全理想安全結果が選別時刻でも安全平坦域に残り、一般R181Dの小確率結果に対する粗い除去質量評価を使う必要がない。

新たに必要な能動資源は1個の中間作用容量指針変数対群、固定済み2作用からのR191ブラウン巨視的スピン読出し部分系、選別機構用未使用作業領域、時計自由度、完全履歴であり、すべて有限である。中間局所記録、方向を変えない振幅再調整、周期末リセットはQ1-2達成証人に使わない。R187側では $T=O(\!\mathcal J_0/J_\kappa)$ まで長くなり得るが、Q1-2は多項式時間を要求しない。

本章による現在地は次である。

| 目標 | 現在地 | 根拠 | 残る条件 |
|---|---|---|---|
| Q1-1 | 達成 | R135、R140、R187 | 固定目標上の残件なし |
| Q1-2 | 達成 | R140、R143--R144、R168、R181D、R187、R189A--R189C、R191 | Born分布、同軸反復分布、異軸逐次分布に加え、同一零傾斜M37 W2信号系で有限2回Zeno証人を構成。有限能動部分系＋Hamiltonian無限浴の単一ミクロ装置への全統合は強化課題。有限浴化は追加強化 |

R189A--R189CはR144の通常測定をそのまま中間へ挿入した結果ではない。R144で使った有限履歴核の望遠鏡和とトレース距離による段間安定性を再利用しつつ、中間測定を零傾斜・走行中信号専用に構成した結果である。

## 3.22 非主張

本章は次を主張しない。

1. 大域階数1共分散だけから結果成分別測定後状態が自動的に生じること。
2. 明示的なHamiltonian浴からM54/準備済み入力境界のW型2モード系の採用開放方程式を縮約導出したこと。有限浴化は別の強化課題である。
3. R164の結果成分容量結合、作用殻ファイバー内平衡化、結果成分間の対称性がW型有限能動部分系と共通Hamiltonian浴から自動的に発生すること。
4. 有効地形仕事・熱がファイバーと制御器を含む全微視的仕事・熱に等しいこと。
5. 有限未使用指針変数誤差を含めても作用容量保持の反作用が厳密に零であること。
6. 全時刻の配置--信号浴整合保存。
7. 有限障壁の左右位置読出しが厳密射影になること。
8. 一般時間依存M37または高モードを含む任意の測定相互作用をR189A--R189Cが扱うこと。
9. 局所記録が統計振幅、共分散、確率流を測っていること。
10. 無反応なしの滑らかな厳密2値写像。
11. 固定容量の閉鎖系による無期限の衝突熱浴、永久記録、リセット。
12. Hopf ポンプからリセットまでの総仕事、総熱、総エントロピー収支。
13. 2準位W型を越える一般Born則。
14. $N\to\infty$ のZeno極限、任意高速測定、一定時間・一定資源での任意精度Zeno測定。
15. M37の元の局所ばね座標だけでR189A作用保持機構とR189B選別機構を局所実装したこと。
16. 置換済み連続位置模型の旧結果を現行Q1へ再導入すること。
