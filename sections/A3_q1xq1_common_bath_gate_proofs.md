@number: C
@chapter: 付録
@title: Q1×Q1共同bath経路代数と合成条件
@status: R175を証明し、R176に必要なHamiltonian、参照系安定性、decoder、誤差条件を分離する。

## C.1　有限経路表示の規約

1試行の有限経路族を

```math
 \Xi_{AB}=\{(\gamma_r,a_r,b_r,\ell_r):r\in\mathcal P\}
 \tag{C.1}
```

とする。零係数または零局所ベクトルを持つ項は削除し、同じ物理sectorへ合流した項は係数をcoherentに加える。経路表示は一意でなく、経路の置換、非零複素数 $s_r$ による

```math
 (\gamma_r,a_r,b_r)
 \longmapsto
 (\gamma_r/s_r,s_ra_r,b_r)
 \tag{C.2}
```

およびA、B間での同様の再配分は同じ派生行列を与える。物理模型ではこの表示冗長性を実座標のcanonical gaugeと区別しなければならない。

行優先ベクトル化について

```math
 \operatorname{vec}_{\rm row}(ab^{\mathsf T})=a\otimes b
 \tag{C.3}
```

なので、

```math
 d_\Gamma
 :=\operatorname{vec}_{\rm row}(D_\Gamma)
 =\sum_r\gamma_ra_r\otimes b_r.
 \tag{C.4}
```

有限次元では任意の $D\in\mathbb C^{2\times2}$ は高々2本の階数1項へ分解できる。例えば特異値分解 $D=\sum_{k=1}^{R}s_ku_kv_k^\dagger$ に対し、$a_k=u_k$、$b_k=\overline{v_k}$、$\gamma_k=s_k$ とすればよい。ただしこの存在証明は、未知入力から物理経路を生成する装置を与えない。

## C.2　局所共変性

式(C.4)へ $U_A\otimes U_B$ を作用させると

```math
 (U_A\otimes U_B)d_\Gamma
 =\sum_r\gamma_r(U_Aa_r)\otimes(U_Bb_r).
 \tag{C.5}
```

ベクトル化を戻せば

```math
 D_\Gamma'
 =U_AD_\Gamma U_B^{\mathsf T}.
 \tag{C.6}
```

従って局所操作は経路数を増やさず、同じ一様な2成分操作を全sectorへ作用させればよい。$U_A,U_B$ がunitaryならFrobenius norm、rank、特異値を保存し、特殊unitaryなら $|\det D_\Gamma|$ も保存する。

経路ラベルの置換 $r\mapsto\pi(r)$ と全経路共通位相 $\gamma_r\mapsto e^{i\chi}\gamma_r$ は

```math
 D_\Gamma\longmapsto e^{i\chi}D_\Gamma
 \tag{C.7}
```

しか生じない。経路ごとに異なる位相誤差 $e^{i\delta_r}$ は一般に相殺せず、後述の位相誤差へ数える。

## C.3　CNOTの経路展開

CNOTは

```math
 U_{\rm CX}=P_0\otimes I_2+P_1\otimes X
 \tag{C.8}
```

である。式(C.4)へ作用させると

```math
 U_{\rm CX}d_\Gamma
 =\sum_r\gamma_r
 \left(P_0a_r\otimes b_r+P_1a_r\otimes Xb_r\right).
 \tag{C.9}
```

右辺を子経路 $(r,0),(r,1)$ と解釈すれば本文式(4.7)を得る。$P_0P_1=0$ なので二つの子はA側で直交するが、これは一方を排他的に選ぶことを意味しない。

同じ演算をもう一度作用させると

```math
 U_{\rm CX}^2
 =(P_0\otimes I_2+P_1\otimes X)^2
 =P_0\otimes I_2+P_1\otimes I_2
 =I_4.
 \tag{C.10}
```

従って派生和は入力へ戻る。物理的には、1回目の分岐で生じた両sectorを同じ相対位相で2回目のinteraction zoneへ入れ、同じ出力sectorへ到着した寄与をcoherentに加える必要がある。sectorを測定または履歴へ不可逆記録した場合、式(C.10)の代数が正しくても物理的な逆演算にはならない。

## C.4　非分離性と一枝selectorの失敗

入力を

```math
 a=\frac{e_0+e_1}{\sqrt2},
 \qquad
 b=e_0
 \tag{C.11}
```

とする。CNOT後は

```math
 d_{\rm Bell}
 =\frac{e_0\otimes e_0+e_1\otimes e_1}{\sqrt2},
 \qquad
 D_{\rm Bell}=\frac{I_2}{\sqrt2}.
 \tag{C.12}
```

$\det D_{\rm Bell}=1/2$ なので階数2である。一方、任意の一枝だけを残した行列は外積であり行列式が零である。

位相を持つBell型経路

```math
 d_\theta
 =\frac{e_0\otimes e_0+e^{i\theta}e_1\otimes e_1}{\sqrt2}
 \tag{C.13}
```

へ逆CNOTとA側Hadamardを作用させると、計算基底のA周辺は

```math
 P_A(0)=\cos^2\frac{\theta}{2},
 \qquad
 P_A(1)=\sin^2\frac{\theta}{2}.
 \tag{C.14}
```

which-path記録により2枝間の交差項を消すと両者は $1/2$ になる。従って枝周辺確率だけを保存しても、位相と逆演算を保存したことにはならない。

## C.5　参照系安定性

有限参照因子 $q_r\in\mathbb C^{m}$ を付け、

```math
 \Psi_\Gamma=\sum_r\gamma_ra_r\otimes b_r\otimes q_r
 \tag{C.15}
```

とする。CNOT経路展開は $q_r$ に作用しないため

```math
 \begin{aligned}
 \Psi_\Gamma'
 &=\sum_r\gamma_r
 \left(P_0a_r\otimes b_r\otimes q_r
 +P_1a_r\otimes Xb_r\otimes q_r\right)\\
 &=(U_{\rm CX}\otimes I_m)\Psi_\Gamma.
 \end{aligned}
 \tag{C.16}
```

これはAまたはBが既に第三部分系と非分離な場合にも必要な整合条件である。第2ゲートが参照因子を読み取って個別routingする必要はない。

<!-- theorem-start:proof -->
**証明（R175）**

局所共変性は式(C.3)--式(C.6)、CNOTは式(C.8)、式(C.9)、自己逆性は式(C.10)から従う。参照因子は各項へ恒等作用を追加するだけなので式(C.16)を得る。式(C.12)の行列式は非零であり非分離性が従う。すべて有限和の恒等式である。証明終。
<!-- theorem-end:proof -->

## C.6　一般入力liftの条件

Q1 portの実正準座標から派生した入力を $u_A,u_B$ とする。許されるliftは次を同時に満たす必要がある。

1. 外部制御はport、ゲート種、作用時間だけを指定し、$u_A,u_B$ の複素係数を読み取らない。
2. bathは固定された単純基準状態から始まり、入力との局所相互作用で経路を自律的に形成する。
3. lift後に入力portを破壊的測定せず、参照系との相関を保つ。
4. 出力経路族の派生和が $u_Au_B^{\mathsf T}$ となる。
5. lift補助bathは状態bathから有限誤差でdecoupleする。

特異値分解による存在証明、入力係数ごとのtemplate選択、tomography後の再準備は第1条件から第3条件を満たさない。M51/R171は指定rayの試行集団を準備する結果であり、未知の単一試行Q1入力を参照系安定に複製またはliftする結果ではない。

## C.7　有限Hamiltonian分岐器に必要な構造

候補分岐器は、各親sectorに同じ局所Hamiltonian密度を作用させ、Aの $P_0$ 成分を直進sector、$P_1$ 成分を交差sectorへ送る必要がある。概念的には

```math
 H_{\rm split}(t)
 =H_A(t)\otimes I_B
 +P_1\otimes H_{X,B}(t)
 +H_{\rm route}(t)
 \tag{C.17}
```

と書けるが、$P_1$ は派生複素信号上の記号である。実座標、実運動量、有限bath couplingだけから式(C.17)と等価な1対1流を構成しなければならない。

有限閉鎖Hamiltonian流は位相空間体積を保存するため、空の子sector、clock、使用済み補助cellを含む拡大系で写像を1対1にする。分岐後のsectorラベルを履歴に残す場合も、逆演算の制御へ不可逆なwhich-path記録として作用させてはならない。履歴が必要なら、逆演算前にuncomputeするか、両経路で同じ状態へ戻す。

## C.8　誤差伝播

理想項を $x_r=\gamma_ra_rb_r^{\mathsf T}$、実際の項を

```math
 \widetilde x_r
 =(\gamma_r+\delta\gamma_r)
 (a_r+\delta a_r)
 (b_r+\delta b_r)^{\mathsf T}
 \tag{C.18}
```

とする。2次以上の項を含む直接評価は

```math
 \begin{aligned}
 \|\widetilde x_r-x_r\|_F
 \leq{}&
 |\delta\gamma_r|\|a_r\|\|b_r\|\\
 &+(|\gamma_r|+|\delta\gamma_r|)
 \left(
 \|\delta a_r\|\|b_r\|
 +\|a_r\|\|\delta b_r\|
 +\|\delta a_r\|\|\delta b_r\|
 \right).
 \end{aligned}
 \tag{C.19}
```

である。経路の欠損集合を $\mathcal F$ とし、pairing誤りと位相誤りを別に加えれば

```math
 \|\widetilde D-D\|_F
 \leq
 \sum_{r\notin\mathcal F}\|\widetilde x_r-x_r\|_F
 +\sum_{r\in\mathcal F}\|x_r\|_F
 +\varepsilon_{\rm pair}
 +\varepsilon_{\rm phase}.
 \tag{C.20}
```

ただし経路数が指数的な場合、式(C.20)を各経路誤差の粗い和として使うと指数精度を要求し得る。R176には、正規化状態bath全体に対する一様作用素評価

```math
 \inf_\chi
 \|\widetilde U-e^{i\chi}U\|_{\rm op}
 \leq\varepsilon_{\rm gate}
 \tag{C.21}
```

を要求する。これなら任意の経路数に対する状態誤差は $\varepsilon_{\rm gate}$ 以下である。

Bell型基準行列 $D_{\rm Bell}$ についてWeyl不等式は

```math
 \sigma_{\min}(\widetilde D)
 \geq\frac1{\sqrt2}-\|\widetilde D-D_{\rm Bell}\|_2
 \tag{C.22}
```

を与える。右辺が正なら階数2は残る。ただしdephasing後の混合でも対角周辺は一致し得るため、階数診断に加えて逆演算fringeを要求する。

## C.9　末端decoder契約

末端decoderは経路族を計算基底信号へ写し、

```math
 c_y=\sum_r\gamma_r
 \langle y_A|a_r\rangle
 \langle y_B|b_r\rangle
 \tag{C.23}
```

を同じ試行の有限信号として得る必要がある。各経路を先に測定して $|\gamma_r|^2$ を足してはならない。前者は干渉項を含む $|\sum_r\cdots|^2$、後者は $\sum_r|\cdots|^2$ であり一般に異なる。

decoder後はM50/R164/R170を使える。正則化 $\delta$、decoder誤差 $\varepsilon_{\rm dec}$、R170誤差 $\varepsilon_{170}$、無反応率 $f_\varnothing$ を完全結果空間へ含め、

```math
 D_{\rm TV}(P_{\rm obs},P_{\rm Born})
 \leq
 \varepsilon_{\rm dec}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}
 +f_\varnothing
 \tag{C.24}
```

を目標とする。式(C.24)は入力信号に対する条件付き評価であり、decoderの構成は未解決である。

## C.10　R176の証明義務

R176を結果へ昇格するには、少なくとも次を同一模型で閉じる必要がある。

- 一般Q1入力と参照系に安定な入口lift
- 1試行内の有限coherent sectorを持つ実正準状態bath
- 固定interaction zoneによる一様CNOTと局所操作
- 経路数に依存しない作用素誤差
- 状態bathとgate補助bathのdecoupling
- 同じ形式の出力portと次段入力port
- CNOTの逆演算と位相fringe
- coherent末端decoderとM50/R164/R170
- 失敗、無反応、漏れ、clock、記録を含む完全結果空間
- 全操作について有限時間、有限作用、有限bath

R175はこのうち経路代数だけを与える。R112は有限unitaryを実正準担体へ実装する一般部品、R164/R170は末端信号の読出し部品であるが、両者の間をM52として物理的に接続する定理はまだない。
