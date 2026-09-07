@number: 3
@chapter: 本文
@title: Q1 W型2モード制御・測定protocol
@status: 旧M47で扱ったQ1系列をM54 W2 static profile上の系列固有protocolとして整理し、R187のM37物理carrier、R181A準備、R140操作、R181Dの深さ1読出し、R143状態更新へ接続する。測定統計は導出済み、Zeno効果はQ1-2の残件である。

## 3.1 Q1 W型2モードprotocolの主張範囲

物理的な導出の主線を、M37の実振動子運動から弱結合W型の低2正常modeを経てQ1の制御運動へ進む経路とする。第6章R187がM37 carrierからM54 W2 signalとR140制御への任意精度有限bridgeを与える。準備・枝選択・記録、R170 instrument、Q2の共同担体はR187から従わず、別sectorとして接続する。

W型とはまず信号担体の空間生成子に与える2重井戸構造であり、古典粒子1個を井戸へ置くだけで2準位信号が生じるという意味ではない。Q1 W型2モードprotocolの粒子位置と作用殻による結果選択は別の物理段階である。旧版のM47はこのprotocolの歴史的IDとしてのみ参照する。

本章は、旧M47で扱ったQ1系列をM54 W2 static profile上の統計力学的な操作・測定protocolとして記述する。基本状態は、W型ポテンシャル中で各試行に1つ存在する粒子位置 $X$ と、2モード信号bath座標 $Z$ を持つ共同測度

```math
\mu(dX\,dZ)
```

である。複素振幅を独立した実在場として先に置かず、規格化共分散

```math
C_Z
=
\frac{\mathbb E_\mu[ZZ^\dagger]}
{\mathbb E_\mu[Z^\dagger Z]}
```

が階数1の場合にだけ、その因子 $c$ を統計的rayとして使う。共通R135の階数1支持節により、単一試行の値 $z=Z(\omega)$ は $z=\alpha(\omega)c$ とほとんど確実に書ける。M54 static profileの局所制御器が入力するのは $c$ または $C_Z$ でなく、この単一試行の $z$ である。本章では粒子位置と信号方向の整合を全時刻では要求しない。Hamiltonian制御中は粒子位置が瞬時の信号bath方向から外れてよく、各操作面で付録Kの有限衝突熱浴を接続して条件付きGibbs分布へ戻す。

Q1の測定はR181Dの深さ1 nodeをW型分析器へ特殊化し、次の仕事行程、熱化行程、記録行程へ分ける。

1. R181AのW型2モード系で信号bath方向を準備する。
2. 信号bath方向を保持し、初期操作面のR164作用殻を準備する。
3. R161、R162、R170で初期粒子位置を準備する。この段階は出力選択ではない。
4. 衝突熱浴を切り、W型2モードの傾斜制御で測定軸の固有方向を左右局在方向へ写す。
5. 分析器終了後にR181Dのraw容量をlatchし、regularized作用殻を更新する。R161、R162、R170で出力selectorを形成してlockする。
6. 入射セルと辺遷移を止め、トンネル振動より速く、高モード間隔より遅く傾斜を立ち上げる。
7. 左右井戸の有効自由エネルギー差と閉じた辺ゲートで、既存の粒子位置を記録終了まで片側へ保持する。
8. 各井戸に置いた局所記録ポインターが、その場所にある $X$ だけを記録する。
9. 安全枝ではR181Dの可逆filterで選択成分と補成分を分け、radial-only portとR143の結果別templateで次段状態を作る。
10. 測定前情報と使用済み装置状態を外部セルへ残し、内部補助を逆計算と交換resetで戻す。

局所記録は、$C_Z$、統計振幅、全密度、確率流、遷移率を入力にしない。従って、物理的複素場のcurrentから全時刻位置率を作る

```math
b
\longrightarrow
q(b)
\longrightarrow
X
```

という因果律をQ1では使わない。Q3のM54 spatial/R161 moving specializationは、統計的rayを位置へ書き戻す旧M46型ではなく、各試行の実正準signal $Z(\omega)$ だけを局所rateへ入力してmoving matchingを構成する。従ってQ1の操作面再平衡化とQ3の連続matchingは、同じR164条件付き分布を異なる時間運用で使う。

共通M54/R181Aは、実正準担体のseed測度を雑音零の開放driftで押し出し、信号bath方向を目標位相円へ有限時間で吸引する。付録HのR181AのW型2モード系はそのW型2モード特殊化であり、別の準備機構ではない。共通R135は階数1共分散の統計因子を単一試行信号の支持へ接続し、R164は同じ試行の有限信号作用を正則化枝容量へ写し、各排他的枝の2作用殻状態数からBorn型条件付き重みと有効自由エネルギーを導く。第2章のR161は共通current--traffic matchingを与え、Q1ではそのstatic詳細釣合い特殊化が一様指数再平衡化を与える。R162はgeneric finite collisionとそのthermal特殊化を与え、続く粗視化経路熱力学系は制御切替と粒子位置経路の監査式を与える。R181A、R135、R164、R161を順に使えば、信号bath方向、条件付き状態数、粒子位置分布を同じ操作面へ有限誤差で準備できる。

第5章のR180Cは、R161を固定singlet型Bell装置の各翼へ適用する。R161は任意のQ1 W型2モードrayに対する平方根率を与え、R162は固定した単一試行信号bath座標に対する衝突熱浴実現を与える。R164は各翼の局所条件付き地形にも使えるが、M54からのblock latch、paired-Hopf準備、2翼周期全体を導かない。R161、R162、R164をQ1の共通根拠とする。

R164により、条件付き地形 $E_i^\delta=-\Theta\log\pi_i^\delta$ は確率から直接設計する量でなく、作用殻を消去した条件付き中間状態有効自由エネルギーとして得られる。作用殻明示表示の $\Omega_i^\delta$ と消去表示の $e^{-\beta E_i^\delta}$ を同じ分配関数で掛けず、状態数を二重計数しない。枝容量結合、殻内平衡化、枝対称性、信号bath保持反作用を同じ有限局所Hamiltonianへ統合しておらず、Hopf pump、記録、resetを含む周期全体の仕事・熱・エントロピー収支も未閉鎖である。ただし、これらは現行Q1 W型2モードprotocolを強める実装・熱力学的課題であり、再編後のQ1-2の達成条件には含めない。

## 3.2 階数1共分散とBloch球

Pauli行列を $\sigma_x,\sigma_y,\sigma_z$ とし、共分散のBloch成分を

```math
r_k
=
\operatorname{tr}(C_Z\sigma_k)
```

で定める。$C_Z$ はHermitian、正半定値、trace 1なので

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
i\mathcal J_0\dot C_Z
=
[G(t),C_Z]
```

に従う。

**R135の2次元系。**

trace 1の正半定値2次共分散について、階数1条件は $|\boldsymbol r|=1$ と同値である。階数1共分散の集合は共通位相を除いた $\mathbb{CP}^1\simeq S^2$ であり、$H_G$ の古典正準流はこの球面上の回転を与える。従ってQ1の純粋2モード統計状態は、独立した複素振幅場を仮定せずBloch球を持つ。
これはR135を時間依存2モード生成子へ特殊化したものである。共分散の回転は厳密だが、粒子位置周辺のmatching保存は別の条件である。

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

この式は、共鳴 $\varepsilon=0$ での完全振動、離調による振幅低下、振動数の変化を同じ担体で与える。

<!-- theorem-start:theorem -->
**定理（R140：W型2モードの制御、占有振動、傾斜保持）**

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はunitary共役であり、trace、正値性、階数を保存する。零傾斜では角周波数 $(E_1-E_0)/\mathcal J_0$ の左右占有振動を与え、一定傾斜では上の離調公式に従う。さらに射影内の左右占有変化は第3.7節の傾斜保持評価に従う。全W型系で $\varepsilon_{\rm lock}$ を用いる場合は、$J\ll|\varepsilon_m|\ll G$ と $\mathcal J_0/G\ll\tau_q\ll\mathcal J_0/J$ に加え、付録B.5の状態誤差条件を満たすことを仮定する。
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

は全て $\sqrt{J/G}$ の次数で零へ近づく。ただし、この $\tau_q$ は「高modeには遅く、トンネルには速い」という診断用の中間尺度であり、R187のsmooth switch誤差を小さくするための必須選択ではない。実際に $|\varepsilon_m|\tau_q/\mathcal J_0=O(1)$ なので、これだけから瞬時quenchとの差が小さいとはいえない。R187では小振幅のpiecewise-static controlを先に閉じ、必要なら短い $C^1$ rampを別誤差 $\varepsilon_{\rm sw}$ として評価する。

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

証明は付録B.17。固定基底では $\dot V=0$ として漏れ結合と有効位相を評価する。瞬間固有基底では基底移動項を落とさない。この系は一般の誤差接続道具として残す。ただし固定基底では傾斜結合が $O(F)$、hold時間が $O(F^{-1})$ となり得るため、積分残差が小さくならない場合がある。第6章R187は弱結合W型族のdressed低2clusterと静的正常mode較正を使い、この粗い障害を回避して任意精度の物理carrier族を構成する。

零傾斜完全移送時間は $T_X=\pi\mathcal J_0/(2J)$ である。一般のR86 Duhamel上界をこの長時間へ機械的に掛けると粗くなる。R187では各static segmentの厳密正常mode生成子 $f_{\omega_0}(h)$ が同じ固有ベクトルを共有することを使い、実際の低2分裂でhold時間を較正するため、carrier誤差をhold時間非依存の $\delta_{\rm loc}$ 型へ戻す。初期共通位相の異なる試行にも同じ全状態上界を適用し、R135の集団輸送へ接続する。Born型選択、粒子輸送、測定周期は本系とR187の結論に含めない。

### 3.5.2 R187からQ1制御誤差への受渡し

R187の零傾斜正常mode2pairをM54 W2 static profileのsignal subsystemと同定する。初期port誤差を含む全状態差を $\varepsilon_{187}$ とすると、低2modeへの射影後に成功枝だけを再規格化して誤差を小さく見せるのではなく、full stateのままR135/R168へ渡す。必要に応じて低2signalを規格化して比較する場合は、E.9の規格化写像を使い

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

R143の誤差台帳では、従来独立に置いていた全W型制御側の $\varepsilon_{\rm ctrl}+\varepsilon_{2m}$ を、R187を採用する運転では上のfull-state bridge誤差から一貫して評価する。同じM37偏差をcarrier誤差、ray誤差、Born分布誤差へ重複加算しない。R164/R161/R162/R170の作用殻・粒子位置・記録誤差は別sectorなのでR187へ吸収しない。

## 3.6 M54 static/R170のQ1二枝特殊化

Q1ではM54 static profileに
$v=z$、$\mathcal I=\{L,R\}$、$\Psi=\Phi$
を代入する。第2章のR164により

```math
\pi_i^\delta(z)
=
\frac{|(\Phi z)_i|^2/(z^\dagger z)+\delta q_i}{1+\delta}
```

が2作用殻の規格化状態数として得られ、R161はこの分布への有限時間再平衡化、R162はその有限衝突実現を与える。R170では再平衡化後に入射cellを止め、左右ゲートを閉じ、局所記録を作る。従ってQ1章で独立に必要なのは、W型signalの準備と分析器、左右固定、局所位置recordとの接続である。枝選択とrank-one post-state更新は第2章のcommon projective nodeへ共通化し、別の結果別state templateを置かない。

作用殻を消去した条件付き中間状態有効自由エネルギーは

```math
E_i^\delta(z)=-\Theta\log\pi_i^\delta(z)
```

である。第2章の粗視化経路熱力学系は、解析器quenchと粒子位置遷移の正逆経路比、積分ゆらぎ関係、相対有効散逸を監査する。ただしこれはHopf pump、作用殻準備、信号bath保持、記録、template交換、resetを含む全周期の機械仕事・微視的熱収支ではない。

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
R140が固定するのは信号bathの左右占有周辺であり、一般入力を左右固有状態へ収縮させる結果ではない。周辺固定だけから単一試行の粒子位置 $X$ の経路滞在は従わない。そこで再平衡化終了後にR162の入射セルを止め、辺ゲートを閉じる。記録時間中の離脱失敗率 $\varepsilon_{\rm res}$ は、有限障壁裾、エネルギー切断、閾値平滑化、時計ずれから評価する。どちらの枝にいるかは、ゲート閉鎖前から存在するM47粒子位置を局所的に読む。

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

分析器後の共分散は $C_Z'=A_{\boldsymbol n}CA_{\boldsymbol n}^\dagger$ である。分析器中は粒子位置周辺がこの共分散を追跡しなくてよい。終了後の信号bath方向を固定し、R161の再平衡化を時間 $T_X$ だけ作用させれば、左右井戸の粒子位置頻度が $p_s$ を有限コントラストと有限混合誤差で読む。

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


## 3.10 条件付けとprojective state updateの分離

測定記録を $R\in\{L,R,\varnothing\}$ とする。入力の大域共分散が階数1で
$C_Z=cc^\dagger$
なら、結果事象だけで条件付けても、filter前の各安全枝のsignal方向は一般に同じ $c$ のままである。したがって、Born型branchを選ぶことと、測定後固有stateを物理的に作ることは別の操作である。

Q1では分析器座標のrank-one projectorを

```math
P_s=|s\rangle\langle s|,
\qquad
s\in\{L,R\}
```

とする。R170と共通のselection--lock coreで安全枝 $s$ を固定した後、R181Dのcontrolled projector filterを作用させる。理想selected signalは

```math
Z_s^{\rm sel}
=
P_sZ
=
\langle s|Z\rangle |s\rangle
```

なので、安全枝では規格化方向が必ず $|s\rangle$ である。R181Dのradial-only repumpはこの方向を変えない。filter誤差を含む条件付きstate誤差は第2章の
$\varepsilon_{\rm node}^{\rm state}$
で評価する。

有限W型の左右コントラスト $\eta_W$ は「どの枝が記録されるか」という結果分布の偏差へ入るが、selector lock後にrank-one filterが作るsignal方向の誤差へ重ねて入れない。結果分布誤差とpost-state trace距離は別の量として管理する。

測定終了時に粒子位置 $X$ を新しいsignal方向へ再平衡化する必要はない。$X$ は局所recordが完了するまで安全井戸へ保持し、selected signalは同じ単一試行のまま次の制御区間へ渡す。次の測定面に到達した時点で、改めてR164、R161、R162を有限時間だけ作用させる。これにより全時刻の配置--signal matchingも、結果依存の外部state再準備も仮定しない。

## 3.11 粒子位置の局所記録

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

傾斜保持時間 $T_{\rm rec}$ は、局所ポインターが安全域を分離できる長さとする。R140により保持中の信号bath左右占有変化を $\varepsilon_{\rm lock}$ に抑える。R162により、再平衡化終了後の入射停止と辺ゲート閉鎖から、単一試行の経路滞在失敗を $\varepsilon_{\rm res}$ に抑える。分離面を通過中の試行、ゲート閉鎖失敗、有限閾値帯は無反応として記録し、除外後の2値再規格化を行わない。


## 3.12 共通projective nodeによる結果枝状態更新

分析器終了後、R164--R161--R162で形成したselectorをlockし、3.11の局所recordで安全枝 $s$ を記録する。signalとblank filter workに対し、第2章R181Dの

```math
F_s
=
\begin{pmatrix}
P_s&P_{1-s}\\
P_{1-s}&-P_s
\end{pmatrix}
```

をselector制御で作用させる。すると

```math
F_s(Z,0)
=
(P_sZ,P_{1-s}Z)
```

となり、selected componentはsignal側、rejected componentはwork/spent側へ残る。異なる入力を同じ出力へ消去する写像ではなく、拡大状態上の1対1 filterである。

rank-one $P_s=|s\rangle\langle s|$ では、安全枝のselected signalは位相とradial factorを除いて $|s\rangle$ そのものである。R181Aの $\kappa=0$ radial-only portをselected signalだけに開けば、作用を標準範囲へ戻してもrayは変わらない。R181Dのfilter実装誤差が $\eta_F<\sqrt\tau$ なら

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
\frac{2\eta_F}{\sqrt\tau-\eta_F}.
```

測定前の論理座標へ戻すと

```math
A_{\boldsymbol n}^\dagger
C_s^{\rm out}
A_{\boldsymbol n}
\simeq
\Pi_{\boldsymbol n,s}.
```

branchごとの固有state templateは使わない。測定前signalの非選択成分はfilter workへ、radial repumpで環境へ渡る情報はspent側へ残す。selected signalは同じ試行の次段へ直接渡し、次の測定面でのみ新しいR164--R161--R162 matchingを走らせる。


## 3.13 R143：Q1 W型2モード有限コントラスト読出しと共通projective-node受渡し

Q1の1段測定では、結果分布を作るM54 static selection--lock coreと、測定後signalを作るR181D rank-one filterを同じprojective nodeとして使う。R143が独自に担うのはW型signalの準備・分析器・有限コントラスト・傾斜固定・safe-well局所記録との接続であり、branch固有stateの再準備機構を別に置かない。

<!-- theorem-start:theorem -->
**定理（R143：Q1 W型2モード有限コントラスト読出しと共通projective-node受渡し）**

固定した入力純粋共分散、測定軸 $\boldsymbol n$、有限観測時間について、次を仮定する。

1. R181AのW型2モード特殊化でsignal方向を有限誤差 $\varepsilon_{\rm Hopf}$ 以内に準備し、初期操作面でR170を誤差 $\varepsilon_{170}^{\rm in}$ 以内に実行できる。
2. 衝突cell流を切った後、R140の傾斜列を2モード制御誤差 $\varepsilon_{\rm ctrl}$ 以下で実装し、分析器終了方向を保持できる。全W型高mode偏差を $\varepsilon_{2m}$ とする。
3. R140の尺度階層によりsignalの左右占有変化を $\varepsilon_{\rm lock}$ 以下にし、R162の入射停止と辺gate閉鎖により、局所record終了前に粒子位置 $X$ が安全井戸を離れる確率を $\varepsilon_{\rm res}$ 以下にできる。
4. 分析器後にR181Dの深さ1 common projective nodeを動かし、無反応を含む完全結果分布の実装誤差を $\varepsilon_{\rm node}^{\rm dist}$ 以下、各安全枝の条件付きpost-state trace距離を $\varepsilon_{\rm node}^{\rm state}$ 以下にできる。

このとき結果集合 $\{+1,-1,\varnothing\}$ を持つ有限正準・弱開放1段instrumentを構成でき、無反応質量を零とした理想Born分布との全変動距離は

```math
\varepsilon_{\rm inst}
\leq
\eta_W
+
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{170}^{\rm in}
+
\varepsilon_{\rm node}^{\rm dist}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
```

で抑えられる。安全結果 $s$ の条件付き出力共分散は、分析器座標で $|s\rangle\langle s|$ からtrace距離 $\varepsilon_{\rm node}^{\rm state}$ 以内である。有限コントラスト $\eta_W$ は結果頻度の誤差であり、このpost-state boundへ重複加算しない。記録は粒子位置 $X$ の局所関数だけを入力にし、全密度、確率流、統計振幅をcontrollerへ与えない。
<!-- theorem-end:theorem -->

R143の利用単位は1回の測定である。共通selection、lock、filter、radial repumpは第2章R181Dに置き、R143では再証明しない。複数回測定のjoint historyと段間state誤差合成はR144だけで扱う。旧連続matching保存は仮定しない。一方、作用容量結合とfiber内平衡化を含む最小Hamiltonian、signal保持controllerの完全な反作用、M37 carrierとprojective nodeの単一装置統合、Hopf準備からresetまでの総収支はR143から従わない。


## 3.14 同軸反復と異軸逐次測定

第1測定軸を $\boldsymbol n$ とし、安全結果 $s$ を得た後、R181Dのrank-one filter後の同じsignalは、分析器座標で $|s\rangle\langle s|$ からtrace距離 $\delta_{\rm state}$ 以内にある。同じ軸を再測定する場合、理想反対結果の確率は零であり、有限装置では段間state誤差と第2段instrument誤差で抑えられる。

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

段間ではselected signalをそのままR140制御へ渡す。分析器中に粒子位置がsignalへ追従することは要求せず、次の測定面でR164--R161--R162 matchingを新たに実行する。外部controllerがstate tomography、係数読出し、結果依存state再準備を行わない。

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

固定純粋入力、固定有限段数 $N$、固定した測定軸列 $\boldsymbol n_1,\ldots,\boldsymbol n_N$ を取る。各段でR143の4条件が成立し、段 $j$ のR181D selected signalを同じ試行の段 $j+1$ へ直接渡せるとする。段間にはR140で許された固定有限の正準制御列を挿入してよい。各段は有限個の記録cell、collision cell、selector/filter work、radial-port環境を使用し、無反応を含む履歴を列の終了まで保持する。

このとき完全履歴空間

```math
\mathcal H_N
=
\{+1,-1,\varnothing\}^N
```

上の有限正準・弱開放逐次instrumentを構成できる。理想逐次分布を $p_N^{\rm id}$、実分布を $p_N^{\rm obs}$ とし、段 $j$ の1段instrument誤差を $\varepsilon_{{\rm inst},j}$、安全出力共分散の理想射影からのtrace距離を $\delta_{{\rm state},j}$ とすれば、

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

ここでtrace距離は $D_{\rm tr}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1$ とする。任意の2値効果による確率差は $D_{\rm tr}$ 以下なので、段間state誤差の係数は1である。同軸列では理想反対結果の重みは零、異軸列では各安全条件付き核は

```math
\operatorname{tr}
\left(
\Pi_{\boldsymbol n_j,s_j}
\Pi_{\boldsymbol n_{j-1},s_{j-1}}
\right)
```

となる。固定有限 $N$ に必要な能動部と履歴cell数は有限であり、外部から量子状態を再準備しない。
<!-- theorem-end:theorem -->

R144はR143のsingle-stage instrumentを固定有限回だけ合成する定理であり、R181Dのpost-state handoffを段間interfaceとする。永久記録、内部逆計算、周期末resetを結論に含めない。全時刻のmatching保存または周期間matching帰還も仮定せず、各測定面でR164--R161--R162を有限時間だけ走らせる。本定理はZeno効果そのものを示さず、測定中も零傾斜Rabi項を止めない対照との接続は別の未達課題である。


## 3.16 実装強化：永久記録、補助逆計算、交換reset

R144の固定有限履歴を列終了後も保持し、補助controllerを次周期へ戻す場合の追加構成をここに分離する。この構成はQ1-2の達成条件ではない。

安全枝のselected signalはR181Dのpost-stateとして保持する。rejected componentはfilter work、radial情報はradial-port環境、selectorとcollisionの微視的履歴はspent側へ残す。局所recordを外部cellへ保持した後、結果とpost-stateを担わない時計、傾斜駆動器、比較補助だけを逆順に戻してよい。controlled projector filterをpost-state保持中に逆実行して測定前signalへ戻すこと、また採用開放radial repumpの環境履歴を消して逆転することは要求しない。

補助座標の周期末偏差 $\delta a$ を、流入する空cell $\eta_n$ と交換角 $\phi$ で回転すると

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta_n.
```

1周期の補助逆計算残差を $\varepsilon_{\rm cyc}$、空cell幅を $\|\eta_n\|\leq\sigma_E$ とすれば

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

**系（固定有限周期の補助逆計算・交換reset）。**

固定有限段のR144履歴とspent情報を保持し、結果相関を担わない補助自由度だけを逆順に戻し、各周期でfresh cellとの上記交換を行えるとする。このとき固定有限周期数 $K$ について拡大写像の1対1性を保ったまま補助偏差を上式で抑えられる。永久record、rejected filter work、collision履歴、radial-port履歴、使用済みcellは $O(K)$ 以上であり、固定容量閉鎖系で $K\to\infty$ を実現するとは主張しない。

この系はR144の根拠条件ではない。Hopf pump、作用殻、signal保持controller、collision cell、projective filter、radial repump、record、resetを含む総仕事、総熱、総エントロピー生成を一つの恒等式へ閉じる問題も引き続き未解決である。


## 3.17 誤差・熱力学・資源台帳

Q1の1段結果分布誤差は、R143の責務に合わせて

```math
\varepsilon_{Q1}^{\rm dist}
=
\varepsilon_{\rm prep}
+
\varepsilon_{170}^{\rm in}
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\eta_W
+
\varepsilon_{\rm node}^{\rm dist}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
```

と整理する。ここで $\varepsilon_{\rm node}^{\rm dist}$ は出力側common projective nodeのR164作用殻、R161混合、R162 collision、selector lock、局所record、guard、controlled filter、radial repump、routeの完全結果誤差を各1回だけ含む。同じ偏差をR170とR181Dへ重複加算しない。

安全枝のpost-stateは別量

```math
\varepsilon_{Q1}^{\rm state}
=
\varepsilon_{\rm node}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt\tau-\eta_F}
```

で管理する。$\eta_W$ は結果頻度の有限コントラスト誤差なので、このstate boundへ加えない。R144では各段の結果分布誤差と、次段へ伝わるtrace-distance state誤差を別々に有限和へ入れる。

準備誤差は

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm phase}
```

と分ける。R181Aはsignal ray準備を有限時間で抑え、零seedと位相基準の失敗は無反応を含む完全結果へ残す。R187を採用する運転ではcarrier側の $\varepsilon_{\rm ctrl}+\varepsilon_{2m}$ を同じM37 full-state bridge誤差から評価し、重複加算しない。

熱力学台帳では、分析器仕事 $W_{\rm ctrl}$、作用殻自由エネルギー仕事 $W_{\rm sh}$、作用殻消去表示の相対有効仕事 $W_{\rm q}^{\rm rel}$ と熱 $Q_X^{\rm rel}$、Hopf pump仕事、局所record、controlled filter、radial repump、resetを分ける。projector filterはrejected componentをworkへ残す可逆正準操作であり、それ自体を情報消去と呼ばない。radial-only repumpは採用開放流なので、失われたradial情報と散逸履歴をspent側へ数える。第2章の粗視化経路熱力学だけで、これらを含む全周期の微視的仕事・熱を同定しない。

1段の能動装置は、signal 2モード、条件付き作用殻fiber、容量controller、有限collision cell、辺gate、selector/lock、filter work、radial port、左右record cell、傾斜制御、clock、粒子位置の局所検出部からなる。結果別の左右state templateは不要である。R144の固定 $N$ 段では、record、collision、filter work、radial/spent cellとclock窓を粗く $O(N)$ で用意すれば列内資源は有限である。3.16の実装強化を $K$ 周期繰り返す場合だけ、永久recordとspent履歴がさらに $O(K)$ 以上増える。

$\delta\downarrow0$ では有効自由エネルギー幅が $O(\!\log\delta^{-1})$、必要collision流束が少なくとも $\Omega(\!\delta^{-1/2})$、R161の一般混合率下界は $O(\!\delta)$ まで低下し得る。R164の滑らかな有限幅作用殻を一様精度で保つ剛性には $\Omega(\!\delta^{-2})$ が必要で、$\Theta(\!\delta^{-2})$ は代表的な選択である。有限資源のまま厳密nodeを追跡するとは主張しない。

深いW型極限は測定コントラストと固定誤差を小さくする一方、トンネル分裂 $J$ を小さくする。零傾斜の $x$ 回転時間は $O(\mathcal J_0/J)$ なので、精度を高めるほど任意軸操作が遅くなる可能性がある。この精度--時間交換は資源台帳から除外しない。

## 3.18 Q1の達成判定とZeno統合課題

本章による現在地は次である。

| 目標 | 現在地 | 根拠 | 残る条件 |
|---|---|---|---|
| Q1-1 | 達成 | R135、R140 | 全W型制御は有限2モード誤差。精度--時間交換を持つ |
| Q1-2 | 部分達成 | R140、R143--R144、R161、R162、R164、R168、R170、R181A、R181D | Born分布、同軸反復分布、異軸逐次分布は導出済み。同一の零傾斜Rabi対照と反復測定を接続し、全履歴・無反応・tilt対照・有限誤差・資源を含む正のZeno抑制余裕を示すことが残る |

旧Q1-4のZeno効果はQ1-2へ統合した。旧M38の有限Zeno結果は、置換済み連続位置模型に依存する歴史的結果としてGit履歴と研究メモへ保存し、Q1 W型2モードprotocolの現行根拠へ戻さない。Q1の傾斜固定は測定保持の一部であり、反復測定間隔に応じたZeno抑制の導出ではない。傾斜でHamiltonianを離調させて遷移を抑える現象をZeno効果と呼ばない。旧Q1-3の完全周期は固定目標から削除し、3.16の無番号実装強化系と周期総収支を実装・熱力学的課題として保存する。

再開後の最初の検査では、総時間 $T$ と零傾斜Rabi周波数 $\Omega$ を共通に固定する。測定なし対照の理想目標を

```math
P_{\rm free}(T)
=
\frac{1+\cos(\Omega T)}{2},
```

等間隔に $N$ 回測る理想目標を

```math
P_N(T)
=
\frac{1+\cos^N(\Omega T/N)}{2}
```

と置く。ただし、これらは本版でQ1 W型2モードprotocolから導出したZeno結果ではなく、R144の有限段逐次instrumentへ零傾斜Rabi自由発展を接続するときの比較目標である。測定中も対象Rabi項を止めず、flip、reflip、無反応を含む全履歴を残す。測定と同じ傾斜操作だけを入れて記録しないtilt対照を必須とし、観測された差を離調固定から分離する。重なり、傾斜、自由発展、1段instrumentの誤差を別々に上界し、有限 $N$ で $P_N-P_{\rm free}$ の正の余裕が合成誤差を上回る場合だけ達成候補とする。反復回数に比例するrecord、selector/filter work、radial/spent cell、fresh cell、reset、時間、エネルギーも資源台帳へ含める。

## 3.19 非主張

本章は次を主張しない。

1. 大域階数1共分散だけから枝別測定後状態が自動的に生じること。
2. 具体的回路または有限bathからM54/R181AのW型2モード系の採用開放方程式を導出したこと。
3. R164の枝容量結合、作用殻fiber内平衡化、枝対称性がW型装置の有限局所Hamiltonianから自動的に発生すること。
4. 有効地形仕事・熱がfiberとcontrollerを含む全微視的仕事・熱に等しいこと。
5. 信号bath保持controllerへの反作用が厳密に零であること。
6. 全時刻の配置--信号bath matching保存。改訂後の周期はこれを必要としない。
7. 有限障壁の左右位置読出しが厳密射影になること。
8. 傾斜切替で高モード漏れが厳密に零になること。
9. 局所記録が統計振幅、共分散、確率流を測っていること。
10. 無反応なしの滑らかな厳密2値写像。
11. 固定容量の閉鎖系による無期限の衝突熱浴、永久記録、reset。
12. Hopf pumpからresetまでの総仕事、総熱、総エントロピー収支。
13. 2準位W型を越える一般Born則。
14. Zenoまたは反Zeno効果。
15. 置換済み連続位置模型の旧結果を現行Q1へ再導入すること。