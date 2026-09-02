@number: 4
@chapter: 本文
@title: M52のQ1×Q1永続共同bath経路模型
@status: 1試行内のcoherent経路和に対するR175の代数を確立する。一般入力lift、有限Hamiltonian CNOT、逆演算、末端decoder、Born型読出しを同じ装置で閉じるR176は未解決であり、Q2-1を部分達成とする。

## 4.1　再構築の目的と判定境界

Q2-1の固定目標は、2量子ビット型結合ゲートと同一の共同入力--出力統計を生成し、2論理部分系のテンソル積構造に関して積入力を非分離な共同内部状態へ移し得る有限古典Hamiltonian過程を構成することである。二端Bell測定または多段ゲート合成はQ2-1単独の達成判定に含めない。

旧構成は、4つの論理係数を一つの4モードregisterへ直接保持し、固定programごとのbath templateと中央作用殻を用いた。この有限benchmarkの代数と数値検算は誤りと判定したわけではない。しかし、4モードregisterが共同状態そのものを担い、入力ごとのtemplate routingと破壊的枝decodeに依存するため、Q1出力を同じ形式の次段入力へcoherentに渡す模型として採用しない。旧模型と旧結果は現行章から外し、退役メモとGit履歴に保存する。

本章はM52「Q1×Q1永続共同bath経路模型」を候補として導入する。設計原則は次のとおりである。

1. 共同状態容量は、一つの4モード論理registerでなく、同じ試行に共存する有限個のbath経路が担う。
2. 経路を一つ選ばず、相対位相、pairing、経路ラベルをゲート終了後も保持する。
3. 各Q1 portは2成分の局所信号だけを操作し、共同係数行列を推定、再構成、参照しない。
4. 状態bathは計算終了まで永続し、時計、routing、記録に使う補助bathとは区別する。
5. Born型の排他的結果は回路末尾だけでM50/R164/R170へ渡し、中間では粒子位置または枝記録を作らない。

この設計は完成模型ではない。以下で厳密に示すのは有限経路和の代数であり、その代数を実在する有限古典Hamiltonian過程へ持ち上げることはR176の未解決条件である。

## 4.2　M52の1試行状態と存在論

有限経路集合を $\mathcal P_\Gamma$ とする。1試行の状態bath切断面を

```math
 \Xi_{AB}(\Gamma)
 =\{(\gamma_r,a_r,b_r,\ell_r):r\in\mathcal P_\Gamma\}
 \tag{4.1}
```

と書く。$a_r,b_r\in\mathbb C^2$ は各Q1 portに接続された実正準対の派生複素表示、$\gamma_r\in\mathbb C$ は同じ実正準bath sectorの作用と位相から得る派生係数、$\ell_r$ は物理的な経路・time-bin・sectorを識別する有限ラベルである。物理的実体は、これらを構成する実座標、実運動量、bath、時計、制御器、記録器である。

同じ試行内の診断行列を

```math
 D_\Gamma
 :=\sum_{r\in\mathcal P_\Gamma}
 \gamma_r a_r b_r^{\mathsf T}
 \in\mathbb C^{2\times2}
 \tag{4.2}
```

と定義する。$D_\Gamma$ は経路全体の状態を要約する派生量であり、独立の物理registerでもcontroller入力でもない。特にM48の集団交差モーメント

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf 1_Gz_Az_B^{\mathsf T}]
 \tag{4.3}
```

とは異なる。式(4.2)の和は一つの試行のbath sector間で保たれるcoherent和、式(4.3)の平均は異なる試行を集計した統計量である。後者から前者を各試行へ再準備してはならない。

M52の全状態は概念上

```math
 \Gamma_{52}
 =(\Gamma_{Q1,A},\Gamma_{Q1,B},\Xi_{AB},E_S,E_G,E_R,\tau,H,R)
 \tag{4.4}
```

と分ける。$E_S$ は永続状態bath、$E_G$ はゲート時計とinteraction zoneを作る補助bath、$E_R$ は末端読出しbathである。$H$ は履歴、$R$ は未使用・使用済みcellを保持する。$E_G$ と $E_R$ をfreshに交換してもよいが、$E_S$ をゲート間で交換、再標本化、初期化してはならない。

## 4.3　R175：有限経路和の局所共変性、CNOT、逆演算

局所unitary $U_A,U_B\in U(2)$ は各経路へ一様に

```math
 a_r\longmapsto U_Aa_r,
 \qquad
 b_r\longmapsto U_Bb_r
 \tag{4.5}
```

と作用する。このとき

```math
 D_\Gamma\longmapsto U_AD_\Gamma U_B^{\mathsf T}.
 \tag{4.6}
```

CNOTを経路ごとの分岐写像として定める。$P_j=|j\rangle\langle j|$ とし、各親経路 $r$ から子経路 $(r,0),(r,1)$ を

```math
 \begin{aligned}
 (\gamma_r,a_r,b_r,\ell_r)
 \longmapsto{}&
 (\gamma_r,P_0a_r,b_r,\ell_{r0}),\\
 &
 (\gamma_r,P_1a_r,Xb_r,\ell_{r1})
 \end{aligned}
 \tag{4.7}
```

として作る。零ベクトルの子経路は削除してよい。子経路を選択するのではなく、両方を同じ状態bath内に保持する。式(4.2)の行優先ベクトル化 $d_\Gamma=\operatorname{vec}_{\rm row}(D_\Gamma)$ に対して

```math
 d_\Gamma\longmapsto U_{\rm CX}d_\Gamma.
 \tag{4.8}
```

が成立する。

参照系 $R$ を持つ有限経路族

```math
 \Psi_\Gamma
 =\sum_r\gamma_r a_r\otimes b_r\otimes q_r
 \tag{4.9}
```

に同じ規則を作用させると、$q_r$ を読み出さず

```math
 \Psi_\Gamma
 \longmapsto
 (U_{\rm CX}\otimes I_R)\Psi_\Gamma
 \tag{4.10}
```

となる。CNOTは自己逆なので、式(4.7)のcoherentな子経路を再結合できる理想写像をもう一度作用させれば、派生状態は元へ戻る。

<!-- theorem-start:theorem -->
**定理（R175：1試行有限経路和の局所共変性、CNOT、参照系安定性、逆演算）**

有限経路族が式(4.1)、式(4.2)を満たし、経路間の複素係数を同じ試行内で線形に合成できるとする。このとき式(4.5)は式(4.6)、式(4.7)は式(4.8)を与える。任意の有限参照因子を追加しても式(4.10)が成立し、理想CNOTを2回作用させた派生状態は入力へ戻る。$|+\rangle_A|0\rangle_B$ のCNOT出力は

```math
 D_{\rm Bell}
 =\frac{1}{\sqrt2}
 \begin{pmatrix}
 1&0\\
 0&1
 \end{pmatrix},
 \qquad
 \det D_{\rm Bell}=\frac12
```

であり、局所積へ分解できない。
<!-- theorem-end:theorem -->

R175は有限次元線形代数の結果である。経路の分岐、位相保持、再結合を実行する有限Hamiltonian、一般入力を経路族へliftする装置、末端decoderは仮定している。従ってR175だけではQ2-1を達成しない。

## 4.4　一枝選択と集団交差モーメントが代用にならない理由

一つの経路だけを残すselectorを使うと、各試行の派生行列は

```math
 D_\Gamma^{(r)}=\gamma_ra_rb_r^{\mathsf T},
 \qquad
 \operatorname{rank}D_\Gamma^{(r)}\leq1.
 \tag{4.12}
```

となる。試行集団を平均して階数2の行列を回復できても、後から局所位相を加えて逆演算するfringeは回復しない。これは非分離状態をcoherentに受け渡したことではない。

同様に、式(4.3)を多数試行から推定し、新しいbathへ書き戻す操作は状態の輸送でなく再準備である。Q2-1とQ2-3では、次を不採用とする。

- ゲート間の経路選択または粒子位置decode
- 試行集団の交差モーメントからの再注入
- ゲートごとのfresh状態bathへの再準備
- 入力係数ごとに異なるtemplate bankまたは指数長program表
- 逆演算に必要なwhich-path情報の不可逆記録

状態bathが指数個の受動sectorを持つこと自体は排除しない。外部から個別に初期化、設定、較正、制御、同期、reset、読出しする必要がある場合だけQ2-4の資源条件に反する。

## 4.5　R176：Q1×Q1共同bath合成定理の未解決条件

一般のQ1入力を $u_A,u_B\in\mathbb C^2$ とする。入口liftは、入力係数を外部で展開せず、同じ有限規則により

```math
 \mathcal E_{AB}(u_A,u_B)
 \longmapsto\Xi_{AB},
 \qquad
 D_\Gamma=u_Au_B^{\mathsf T}
 \tag{4.13}
```

を実現しなければならない。すでに参照系と相関した入力には、積状態を仮定せず式(4.9)の各経路へ同じport写像を作用させる。

候補定理R176が要求する一周期は次である。

1. Q1形式の一般入力を永続状態bathへcoherentにliftする。
2. 固定されたinteraction zoneを有限時間だけ開き、全経路へ式(4.7)を一様に作用させる。
3. gate補助bathを入力状態からdecoupleし、状態bathだけを次段へ渡す。
4. 同じportで局所操作、別のQ1×Q1ゲート、または逆CNOTを受け付ける。
5. 回路末尾だけでcoherent decoderを作用させ、M50/R164/R170へ有限信号を渡す。
6. 無反応、漏れ、clock失敗、記録失敗を完全結果空間へ含める。

理想符号化と復号を $\mathcal E_2,\mathcal D_2$、M52の有限過程を $\Phi_{\rm CX}^{52}$ とする。参照系を含む一様条件は

```math
 \sup_{\rho_{ABR}}
 d_{\rm op}
 \left(
 (\mathcal D_2\otimes I_R)
 (\Phi_{\rm CX}^{52}\otimes I_R)
 (\mathcal E_2\otimes I_R)(\rho_{ABR}),
 (\mathcal U_{\rm CX}\otimes I_R)(\rho_{ABR})
 \right)
 \leq\varepsilon_{176}
 \tag{4.14}
```

と置く。$d_{\rm op}$ は古典ミクロ状態の符号化・復号後に定義する参照系安定な操作距離であり、量子channelを存在論として仮定する記号ではない。

**予想（R176：Q1×Q1共同bath合成定理）**

有限個のQ1 port、有限だが必要に応じて大きい永続状態bath、固定interaction zone、有限clock、末端M50 instrumentから、式(4.13)、式(4.14)を任意の正の目標誤差で満たす有限古典Hamiltonian過程を構成できる。入力係数またはbath sectorを個別に読み書きせず、CNOT、局所操作、逆演算、末端Born型読出しを同じinterfaceで合成できる。

現時点ではこの予想を証明していない。特に未完成なのは、一般入力lift、経路分岐と再結合の有限Hamiltonian、参照系に一様な誤差評価、gate補助bathのdecoupling、coherent末端decoderである。

## 4.6　有限誤差台帳

理想経路和と実際の出力の偏差を

```math
 \left\|
 D_{\rm out}-U_AD_{\rm in}U_B^{\mathsf T}
 \right\|_F
 \leq
 \varepsilon_{\rm lift}
 +\varepsilon_{\rm gate}
 +\varepsilon_{\rm pair}
 +\varepsilon_{\rm phase}
 +\varepsilon_{\rm leak}
 +\varepsilon_{\rm dec}
 \tag{4.15}
```

と整理する。右辺を $\varepsilon_D$ とする。Bell型基準行列の最小特異値は $1/\sqrt2$ なので、

```math
 \varepsilon_D<\frac{1}{\sqrt2}
 \tag{4.16}
```

ならWeyl評価により出力の階数2は保たれる。しかし式(4.16)だけでは経路coherenceを保証しない。bathに不可逆which-path記録がないことと、endpoint-onlyの逆演算fringeを別に検査する。

一般の長さ $L$ の合成には、各ゲートが同じ参照系安定距離を満たすなら

```math
 \varepsilon_{\rm circ}
 \leq\varepsilon_{\rm prep}
 +\sum_{j=1}^{L}\varepsilon_j
 +\sum_{j=1}^{L-1}\varepsilon_{{\rm hand},j}
 +\varepsilon_{\rm dec}
 +\varepsilon_{\rm Born}
 \tag{4.17}
```

という望ましい合成上界を置ける。M52についてこの一様上界を導くこともR176の一部である。

## 4.7　末端decoderとBorn型読出し

計算基底読出しでは、経路を途中で選ばず、末端decoderが式(4.2)の成分を一つの有限信号portへcoherentに集める必要がある。理想信号を

```math
 c_{ab}=(D_\Gamma)_{ab},
 \qquad
 \sum_{a,b}|c_{ab}|^2=1
 \tag{4.18}
```

とする。M50/R164を $m=L=4$、$\Psi=I_4$ へ特殊化すれば、正則化Born枝は

```math
 \pi_{ab}^{\delta}(c)
 =\frac{|c_{ab}|^2+\delta q_{ab}}{1+\delta},
 \qquad
 \sum_{a,b}q_{ab}=1
 \tag{4.19}
```

となる。理想分布からの全変動距離は高々 $\delta/(1+\delta)$ であり、有限混合、固定、記録誤差はR170へ加える。decoder失敗と無反応を捨てて成功試行だけを再規格化してはならない。

式(4.19)はdecoder入力が与えられた後の読出し結果であり、式(4.18)のcoherent decoderの存在を証明しない。R164を経路間coherenceの起源として逆向きに使ってはならない。

## 4.8　Q2-1の現在地

R175は、有限経路族を仮定すれば局所操作、CNOT、参照系を保つ拡張、逆演算、非分離性を同じ1試行内の代数として閉じる。R112は各有限unitaryの実正準実装部品、M50/R164/R170は末端信号が得られた後の排他的読出し部品として利用できる。

一方、M52全体を有限古典Hamiltonian過程として構成するR176は未解決である。従ってQ2-1は部分達成へ引き下げる。現在の達成内容はR175の経路代数と既存の有限制御・読出し部品であり、欠けているのは一般入力から末端読出しまでを同じ永続状態bath上で閉じる物理的合成定理である。

Q2-2はM48内部のsetting-pre等重みseedから独立に始まるため、この引下げで判定を変更しない。M52からM48への一般状態receiverも主張しない。Q2-3は同じM52状態bathへ二つのinteraction zoneを順に作用させる条件付き拡張として第8章と付録Jで整理する。
