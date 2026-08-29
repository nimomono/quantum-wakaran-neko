@number: C
@chapter: 付録
@title: M49共同bath CNOT供給模型の証明
@status: R104、R105の4モード担体、R157--R160の行分解bath--粒子位置matching、同期CNOT、固定有限共同統計、M48受渡しを証明する。

## C.1　4モード正準担体

$D_{\rm prog}\in\mathbb C^{2\times2}$ を行優先で

```math
 d_{\rm prog}=\operatorname{vec}_{\rm row}(D_{\rm prog})
 =((D_{\rm prog})_{00},(D_{\rm prog})_{01},(D_{\rm prog})_{10},(D_{\rm prog})_{11})^{\mathsf T}
 \tag{C.1}
```

と並べ、

```math
 (D_{\rm prog})_{ab}
 =\frac{Q_{ab}+iP_{ab}}{\sqrt{2\mathcal J_0}}
 \tag{C.2}
```

とする。Hermitian行列 $K$ に対する実2次Hamiltonian

```math
 F_K=\mathcal J_0d_{\rm prog}^\dagger Kd_{\rm prog}
 \tag{C.3}
```

は $i\dot d_{\rm prog}=Kd_{\rm prog}$ を与える。従ってunitaryは実正準流であり、$d_{\rm prog}^\dagger d_{\rm prog}$ を保存する。

局所代数

```math
 \mathcal A=M_2(\mathbb C)\otimes I_2,
 \qquad
 \mathcal B=I_2\otimes M_2(\mathbb C)
 \tag{C.4}
```

は相互に可換で、互いの可換代数に一致する。積 $A\otimes B$ の線形包は $M_4(\mathbb C)$ 全体なので、この二代数が操作誘導テンソル積を定める。局所unitaryは

```math
 D_{\rm prog}\longmapsto U_AD_{\rm prog}U_B^{\mathsf T}
 \tag{C.5}
```

と作用し、$\operatorname{rank}D_{\rm prog}$ と $|\det D_{\rm prog}|$ を保存する。

<!-- theorem-start:proof -->
**証明（R104）**

式(C.3)へ $K=A\otimes I_2$ と $L=I_2\otimes B$ を入れると、対応HamiltonianのPoisson括弧は行列交換子 $[K,L]=0$ に比例して零となる。正方形配線の対辺へ同じ $QQ+PP$ 交換と作用差を置けば、各局所Pauli生成子を有限2次Hamiltonianで実装できる。式(C.5)が積状態集合を保存する。証明終。
<!-- theorem-end:proof -->

## C.2　R105：CNOT担体と有限制御評価

差モード $|d\rangle=(|10\rangle-|11\rangle)/\sqrt2$ への射影は

```math
 \Pi_{\rm CX}
 =|d\rangle\langle d|
 =|1\rangle\langle1|_A
 \otimes\frac{I_2-\sigma_x}{2}.
 \tag{C.6}
```

対応する実2次生成子は

```math
 G_C
 =\mathcal J_0d_{\rm prog}^\dagger\Pi_{\rm CX}d_{\rm prog}
 =\frac14\left[(Q_{10}-Q_{11})^2+(P_{10}-P_{11})^2\right].
 \tag{C.7}
```

射影の冪は $\Pi_{\rm CX}^n=\Pi_{\rm CX}$ なので、

```math
 e^{-iA\Pi_{\rm CX}}
 =I_4+(e^{-iA}-1)\Pi_{\rm CX}.
 \tag{C.8}
```

$A=\pi$ では制御値0部分空間に恒等、制御値1部分空間に $\sigma_x$ が作用するためCNOTに一致する。

<!-- theorem-start:proof -->
**証明（R105）**

$H_C=P_\tau+g(\tau)G_C$ では $\dot\tau=1$ で、信号生成子は全時刻で同じ射影の実数倍である。時間順序積は窓面積 $A$ の式(C.8)へ厳密に縮約する。$A=\pi$ でCNOTを得て、式(C.3)により正準性と作用保存が従う。積入力 $|+0\rangle$ の出力係数行列は階数2なので、局所操作の積ではない。証明終。
<!-- theorem-end:proof -->

固定作用面では $0\leq G_C\leq\mathcal J_0$ である。$0\leq g\leq g_{max}$ の非負窓には

```math
 T_{\rm g}\geq\frac{\pi}{g_{max}}
 \tag{C.9}
```

が必要である。面積誤差を $\delta A\in[-\pi,\pi]$ とすると、相対行列は $e^{-i\delta A\Pi_{\rm CX}}$ であり、固有値は1が3重、$e^{-i\delta A}$ が1重である。このため

```math
 d_{\rm mat}
 =2\left|\sin\frac{\delta A}{2}\right|,
 \qquad
 d_{\rm proj}
 =2\sin\frac{|\delta A|}{4},
 \tag{C.10}
```

```math
 F_{\rm avg}
 =1-\frac35\sin^2\frac{\delta A}{2}.
 \tag{C.11}
```

一般Hermitian誤差 $\Delta K(t)$ には

```math
 \eta_C
 :=\inf_{q(t)\in\mathbb R}
 \int_0^{T_{\rm g}}
 \lVert\Delta K(t)-q(t)I_4\rVert_{\rm op},dt
 \tag{C.12}
```

を使う。共通位相を除いた相互作用表示のDuhamel式から

```math
 \inf_\phi
 \lVert\widetilde U-e^{i\phi}U_{\rm CX}\rVert_{\rm op}
 \leq\min{2,\eta_C}.
 \tag{C.13}
```

4信号正準対と1時計正準対で担体CNOTを実装できる。

**R105の有限制御節。**

式(C.9)は窓面積、式(C.10)、式(C.11)は射影の固有値、式(C.13)はDuhamel式から従う。生成子は4信号正準対上の2作用項と1交換辺で、時計に1正準対を要する。証明終。

## C.3　R157の理想行分解

R157の共同枝確率は、R164を $m=L=4$、$\Psi=I_4$、$\delta=0$ としたM50中央4枝作用殻の状態数 $\Omega_{ab}\propto|(D_{\rm prog})_{ab}|^2$ から直接得られる。以下の行分解は別の確率源ではなく、その共同母測度をA周辺とB条件付き分布へ分解した表示である。

非零行の集合を $I_D={a:\rho_a>0}$ とする。M50の排他的物理枝を $\gamma_{ab}$ と書けば、

```math
 P(\gamma_{ab})=|(D_{\rm prog})_{ab}|^2,
 \qquad
 P(X_A=a)=\rho_a.
 \tag{C.14}
```

safe branch $\gamma_{ab}$ から式(4.9)のone-hot粒子位置へcontrolled SWAPすると、

```math
 P(X_A=a,X_B=b)=|(D_{\rm prog})_{ab}|^2.
 \tag{C.15}
```

第 $a$ 行bath templateの1試行外積は

```math
 z_Az_B^{\mathsf T}
 =\rho_a^{-1}e_a(D_{\rm prog})_{a\bullet}.
 \tag{C.16}
```

従って

```math
 \mathbb E[z_Az_B^{\mathsf T}]
 =\sum_{a\in I_D}\rho_a
 \rho_a^{-1}e_a(D_{\rm prog})_{a\bullet}
 =D_{\rm prog}.
 \tag{C.17}
```

共通位相は外積から消える。$z_A$ は $e_a$ のray上にあり、$z_B$ の規格化成分比は $(D_{\rm prog})_{a\bullet}$ と同じなので、

```math
 \operatorname{Law}(X_A\mid z_A)=\pi_A^0(z_A),
 \qquad
 \operatorname{Law}(X_B=b\mid z_B)
 =\frac{|(D_{\rm prog})_{ab}|^2}{\rho_a}.
 \tag{C.18}
```

## C.4　R157の有限Hamiltonian準備

M50の排他的safe枝 $\gamma_{ab}$ をcontrolとして、freshなone-hot粒子位置registerへ有限列の2モード交換を作用させる。枝registerを使用済み履歴へ残すため、粒子位置への直接decodeを含む拡大写像は1対1である。独立な選択器角、作用区間pointer、比較器の逆計算は不要である。

固定program $s$ とactive行 $a$ ごとに、式(4.11)の4複素成分を持つtemplate cellを事前校正する。$X_A=a$ のsafe plateauをcontrolとするcanonical SWAPにより、templateをactive $z_A,z_B$ portへ移す。全窓を

```math
 H_{157}
 =P_\tau+\sum_{r=1}^{R_{157}}g_r(\tau)G_r
 \tag{C.19}
```

と書ける。$R_{157}$ は固定program族で有限、各 $G_r$ は有限個の作用差、$QQ+PP$ 交換、滑らかなplateau controlから成る。従って有限正準対と有限時間のHamiltonian準備である。templateの値は装置programであり、ensemble量を測定して再注入したものではない。

各非零branchのsurvival係数を $r_{ab}\in[1-\varepsilon_0,1]$ とする。安全事象上の非規格化粒子位置分布は $|(D_{\rm prog})_{ab}|^2r_{ab}$ であり、失敗質量を無反応へ置けば理想完全分布からの全変動距離は $\varepsilon_0$ 以下である。

式(C.16)のFrobeniusノルムは

```math
 \lVert z_Az_B^{\mathsf T}\rVert_F
 =\rho_a^{-1/2}
 \leq\rho_*^{-1/2}.
 \tag{C.20}
```

従って

```math
 \lVert M^G_{AB}-D_{\rm prog}\rVert_F
 \leq
 \sum_{a,b}|(D_{\rm prog})_{ab}|^2(1-r_{ab})\rho_a^{-1/2}
 \leq\frac{\varepsilon_0}{\sqrt{\rho_*}}.
 \tag{C.21}
```

$\delta=\varepsilon_0/\sqrt{\rho_*}<1$ と置く。$\lVert D_{\rm prog}\rVert_F=1$ と三角不等式から

```math
 \left\lVert
 \frac{M^G_{AB}}{\lVert M^G_{AB}\rVert_F}-D_{\rm prog}
 \right\rVert_F
 \leq2\delta.
 \tag{C.22}
```

単位ベクトルの距離は対応する階数1projectorのtrace距離を上から抑えるため式(4.16)が従う。

A粒子位置は全safe branchで行labelと一致する。B側では、行 $a$ の理想条件付き分布を $q_b=|(D_{\rm prog})_{ab}|^2/\rho_a$ とすると、安全条件付き分布は

```math
 q_b^G
 =\frac{q_br_{ab}}{\sum_jq_jr_{aj}}.
 \tag{C.23}
```

分母は $1-\varepsilon_0$ 以上なので

```math
 D_{\rm TV}(q^G,q)
 \leq\frac{\varepsilon_0}{1-\varepsilon_0}.
 \tag{C.24}
```

<!-- theorem-start:proof -->
**証明（R157）**

式(C.15)、式(C.17)、式(C.18)が理想matchingを与える。式(C.19)が有限Hamiltonian準備、式(C.21)--(C.24)が無反応込みの有限誤差上界を与える。証明終。
<!-- theorem-end:proof -->

## C.5　稀な行の資源下界

行 $a$ に条件付けた目標momentは

```math
 \mathbb E[z_Az_B^{\mathsf T}\mid a]
 =\frac{e_a(D_{\rm prog})_{a\bullet}}{\rho_a},
 \qquad
 \left\lVert
 \mathbb E[z_Az_B^{\mathsf T}\mid a]
 \right\rVert_F
 =\rho_a^{-1/2}.
 \tag{C.25}
```

Cauchy--Schwarzから

```math
 \mathbb E[\lVert z_A\rVert^2\mid a]
 \mathbb E[\lVert z_B\rVert^2\mid a]
 \geq\frac1{\rho_a}.
 \tag{C.26}
```

従って $\rho_a\to0$ を含むprogram族について両端bath作用を一様有界にはできない。式(4.11)では各端の作用が $\mathcal J_0/\sqrt{\rho_a}$、active pair全体が $2\mathcal J_0/\sqrt{\rho_a}$ である。行平均は

```math
 \sum_a\rho_a\frac{2\mathcal J_0}{\sqrt{\rho_a}}
 =2\mathcal J_0\sum_a\sqrt{\rho_a}
 \leq2\sqrt2\mathcal J_0.
 \tag{C.27}
```

この有限平均を全program一様の最大作用と混同しない。

## C.6　R158の点ごとの共変性

係数行列CNOTは行ごとに

```math
 (\mathcal C_{\rm CX}(D_{\rm prog}))_{0\bullet}=(D_{\rm prog})_{0\bullet},
\qquad
 (\mathcal C_{\rm CX}(D_{\rm prog}))_{1\bullet}=(D_{\rm prog})_{1\bullet}\sigma_x.
 \tag{C.28}
```

R157 branch $a$ で $z_B^+=\sigma_x^az_B$ とすると

```math
 \begin{aligned}
 \mathbb E[z_A^+(z_B^+)^{\mathsf T}]
 &=\sum_a\rho_a
 \rho_a^{-1}e_a(D_{\rm prog})_{a\bullet}\sigma_x^a\\
 &=\mathcal C_{\rm CX}(D_{\rm prog}).
 \end{aligned}
 \tag{C.29}
```

粒子位置は $b^+=b\oplus a$ なので

```math
 P(X_A^+=a,X_B^+=b)
 =|(D_{\rm prog})_{a,b\oplus a}|^2
 =|\mathcal C_{\rm CX}(D_{\rm prog})_{ab}|^2.
 \tag{C.30}
```

行重み $\rho_a$ は列交換で保存される。従って式(4.11)の各入力templateは、式(4.20)により出力programの対応templateへ点ごとに移る。

## C.7　三port CNOTのHamiltonian

3つのportへ同期するCNOTは、中央作用殻の枝labelにも $P_{\rm CX}(a,b)=(a,b\oplus a)$ を作用させる。$\Omega_{P_{\rm CX}(a,b)}(\mathcal C_{\rm CX}(D_{\rm prog}))=\Omega_{ab}(D_{\rm prog})$ なので状態数地形は共変だが、以下の有限時計Hamiltonianが行う機械仕事を零とはしない。

4モード担体には式(C.7)、B bathとB粒子位置には

```math
 G_z=\mathcal J_z\chi_1(x_A)z_B^\dagger\Pi_-z_B,
 \qquad
 G_X=\mathcal J_X\chi_1(x_A)x_B^\dagger\Pi_-x_B
 \tag{C.31}
```

を使う。$\chi_1$ はA粒子位置のsafe one-hot sectorで0または1のplateauを持ち、共役運動量へ依存しない。$G_C$ は担体、$G_z$ はB bath、$G_X$ はB粒子位置へ作用し、共有するA粒子位置についてはいずれも共役運動量を含まない。従って

```math
 {G_C,G_z}
 ={G_C,G_X}
 ={G_z,G_X}=0
 \tag{C.32}
```

である。一つの時計窓で各面積を $\pi$ にすれば、三流の積は順序に依存せず式(4.20)、式(4.21)になる。各流は自己逆であり、全active・使用済みregisterを含む拡大写像も1対1である。

有限bath unitaryを理想値から作用素距離 $\eta_z$ 以下とする。式(C.20)の重み付き平均から

```math
 \begin{aligned}
 \left\lVert
 \mathbb E[z_A(R_z-\sigma_x^{X_A})z_B^{\mathsf T}]
 \right\rVert_F
 &\leq
 \eta_z\sum_a\rho_a\rho_a^{-1/2}\\
 &\leq\sqrt2\eta_z.
 \end{aligned}
 \tag{C.33}
```

粒子位置XORの失敗質量を $\varepsilon_\oplus$ とすれば、全変動距離は同じ量以下だけ増える。担体誤差と時計誤差を別に加えると式(4.24)、式(4.25)を得る。

<!-- theorem-start:proof -->
**証明（R158）**

式(C.29)、式(C.30)が理想共変性、式(C.31)、式(C.32)が同一時計の有限Hamiltonian実装、式(C.33)が有限bath誤差を与える。証明終。
<!-- theorem-end:proof -->

## C.8　R159のfresh M50出力殻周期

入力源を

```math
 r_\lambda
 =(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_S})^{\mathsf T}
 \tag{C.34}
```

とする。外側scheduleはprogram label $S=s$ を頻度 $\lambda_s$ で提示する。これはbenchmarkの入力条件であり、出力確率源ではない。safe labelをfresh program registerへdecodeし、そのlabelで $D_{{\rm in},s}$ とR157 template bankをactive portへroutingする。入力粒子位置はM50物理枝から直接decodeする。

provider運転はR158後の $\Sigma_{\rm gate}$ で終わる。benchmark運転では同じ担体に $W_A^s\otimes W_B^s$ を作用させ、

```math
 D_{{\rm out},s}=W_A^s\mathcal C_{\rm CX}(D_{{\rm in},s})(W_B^s)^{\mathsf T}
 \tag{C.35}
```

を得る。実在する $D_{{\rm out},s}$ からfreshなM50出力殻を準備し、その物理枝を直接decodeするため、

```math
 P(Y_A=a,Y_B=b\mid S=s)=|(D_{{\rm out},s})_{ab}|^2.
 \tag{C.36}
```

出力safe branchをfresh結果registerへdecodeし、枝registerを履歴へ残す。CNOTを恒等窓へ置き換えると式(C.35)そのものが変わるため、出力器が理想CNOT表を固定的に返す構成ではない。

fresh殻条件が必要である。使用済み入力殻の同一微視的順位を、$S=0$ では条件付き出力重み $1/4$、$S=1$ では $3/4$ の出力殻へ再利用すると、四つの共同枝が全て $1/4$ になる場合がある。従って

```math
 P_{\rm shared}
 =\begin{pmatrix}1/4&1/4\\1/4&1/4\end{pmatrix},
 \qquad
 D_{\rm TV}(P_{\rm shared},P_{\rm id})=\frac14.
 \tag{C.37}
```

fresh出力殻を条件付きで準備すれば、そのM50枝周辺を平均して式(4.30)を得る。必要なのは別registerであり、独立なM35角ではない。

入力label誤差を含む結合を先に作り、各 $s$ でR157、担体unitary、fresh M50出力殻、直接decodeを順にcoupleする。全変動距離の縮小性と三角不等式から式(4.31)が従う。失敗は $\varnothing$ に送るので事後選別はない。各項は固定有限program族について、殻幅、時計幅、template精度を有限値で選んで任意に小さくできる。

<!-- theorem-start:proof -->
**証明（R159）**

式(C.34)--(C.36)が理想共同分布、逐次couplingが式(4.31)を与える。式(C.37)によりfresh出力殻は省略できない。証明終。
<!-- theorem-end:proof -->

## C.9　R160の固定singlet provider

式(4.33)の二行はともノルム2乗 $1/2$ である。CNOT後は

```math
 \mathcal C_{\rm CX}(D_{\rm in}^{\rm s})
 =\frac1{\sqrt2}
 \begin{pmatrix}0&-1\\1&0\end{pmatrix}
 =-\frac{\mathsf E}{\sqrt2}.
 \tag{C.38}
```

$r_*=2^{1/4}$ とすると、CNOT後の二枝は

```math
 \begin{array}{c|c|c|c}
 a&z_A&z_B&(X_A,X_B)\\ \hline
 0&r_*e^{i\theta}e_0&-r_*e^{-i\theta}e_1&(0,1)\\
 1&r_*e^{i\theta}e_1& r_*e^{-i\theta}e_0&(1,0)
 \end{array}.
 \tag{C.39}
```

付録Jの $\mathsf E$ について各枝で

```math
 z_B=\mathsf E\overline{z_A},
 \qquad
 \frac{z_A-\mathsf E\overline{z_B}}2=z_A,
 \qquad
 \frac{z_A+\mathsf E\overline{z_B}}2=0.
 \tag{C.40}
```

従ってM48のbright変数は $m=z_A$、dark変数は $d=0$ であり、cross momentと粒子位置分布は式(4.35)、式(4.36)に一致する。

$T_{\rm link}^{49\to48}$ はbath・粒子位置registerに恒等で、設定角は受渡し後に生成される。よって

```math
 \operatorname{Law}(\Gamma_{\Sigma_{\rm link}}\mid x,y)
 =\operatorname{Law}(\Gamma_{\Sigma_{\rm link}}).
 \tag{C.41}
```

有限port交換では元cellを使用済み側へ残すため、拡大写像は1対1である。

state-carrying感度には、link面族内の $D_0=e_0e_0^{\mathsf T}$ と $D_{\rm out}^{\rm s}$ を使う。対応する規格化row-majorベクトルは直交するので、cross projectorのtrace距離は1である。恒等portはこの距離を保存する。枝seed $S_0=(-1)^{X_A}$ は $P(X_A=0)=p$ をそのまま $P(S_0=+1)=p$ へ写すため、$p=0,1/4,1/2,3/4,1$ のbias監査を全て通る。履歴は受動的で、結果形成核へ入れない。

<!-- theorem-start:proof -->
**証明（R160）**

式(C.38)--(C.40)が固定singletのcross matchingと単一試行粒子位置matching、式(C.41)がsetting-free性を与える。同一registerの恒等搬送がprogram matchingを、canonical SWAP dilationが有限装置の1対1性を与える。state距離と枝biasも保存される。M48結果分布へ全変動距離の三角不等式を適用すると式(4.39)が従う。証明終。
<!-- theorem-end:proof -->

## C.10　資源と適用限界

一programのR157準備は、4モードprogram担体4対、active作用殻2対、2粒子位置register4対、active bath4対、2行template bank8対からなる単純上界22対を持つ。時計、外側program schedule、benchmark用fresh出力殻、履歴、記録は運転modeに応じて別に加える。template bankは固定有限族について $O(S)$、全装置も固定2論理部分系では有限である。

本付録は次を証明しない。

1. 未知入力を保持する一般量子channel。
2. 任意Q2-1出力に対する一般状態M48測定。
3. 独立同分布型有限標本統計。
4. 空間分離、準備後の自由設定変更、有限伝播円錐。
5. R162の有限衝突粒子位置bathとR153のrouting、paired-Hopf流、2翼controllerの閉鎖Hamiltonian統合。
6. $2^n$ モードを避ける多量子ビット拡張。

R104、R105はM49内部担体の有限正準結果として使う。これらの担体代数だけでは、R157--R160のbath、粒子位置、物理的受渡しは従わない。
