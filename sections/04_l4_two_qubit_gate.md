@number: 4
@chapter: 本文
@title: M49の共同bath CNOT供給模型と共同入力--出力統計
@status: M49の中央4枝作用殻から粒子位置への直接decode、行分解bath--粒子位置matching、担体・bath・粒子位置・作用殻地形へ同期するCNOT、fresh出力殻を使う固定有限ベンチマーク、M48へのsetting-free受渡しを構成する。Q2-1の達成判定は維持する。

## 4.1　目的、試行状態、二つの終了面

Q2-1の固定目標は、2量子ビット型結合ゲートと同一の共同入力--出力統計を生成する有限古典Hamiltonian過程を構成することである。本章ではM49「行分解共同bath--粒子位置CNOT供給模型」を採用し、4モード担体、M50中央4枝、粒子位置、行分解bathを同じ試行で接続する。

固定有限program族を $s=1,\ldots,S$ とし、1試行状態を

```math
 \Gamma_{49}
 =\bigl(S,D_{\rm prog},u_S,\Gamma_X,\Gamma_Y,X_A,X_B,Y_A,Y_B,z_A,z_B,\tau,H,R\bigr)
 \tag{4.1}
```

とする。$S$ はprogram番号、$D_{\rm prog}\in\mathbb C^{2\times2}$ はFrobenius規格化された4モード正準担体である。$u_S$ は外部から指定されたprogram頻度を作るscheduleであり、Born型出力の確率源ではない。$\Gamma_X$ と $\Gamma_Y$ は入力と出力の相異なるM50作用殻、$X_A,X_B$ は2端の粒子位置、$Y_A,Y_B$ はbenchmark専用のfresh出力register、$z_A,z_B\in\mathbb C^2$ は2端へ継続するbath座標、$\tau$ は共有時計、$H$ は不変な履歴、$R$ は未使用・使用済みcellを含む補助レジスタである。provider運転では $\Gamma_Y,Y_A,Y_B$ を空のまま保つ。$D_{\rm prog}$ は各試行に存在する物理担体であり、交差モーメントを推定して試行へ書き戻す集団制御器ではない。

M49は次の4層を同じ固定programで閉じる。

1. 4モード担体からM50中央4枝作用殻を作り、物理枝 $(a,b)$ を空の二粒子位置register $X_A=a,X_B=b$ へ直接かつ可逆にdecodeする。
2. $X_A=a$ が指定する有限bath templateをactive port $z_A,z_B$ へroutingし、交差モーメントと単一試行粒子位置matchingを同時に作る。
3. $D_{\rm prog}$、$z_A,z_B$、$X_A,X_B$ と中央作用殻の枝地形へ同じCNOT置換を同一時計窓で作用させる。
4. provider運転ではCNOT直後に停止し、benchmark運転では固定積分析器とfreshな出力作用殻を追加する。

CNOT直後かつ積分析器前の面を $\Sigma_{\rm gate}$、固定積分析器と出力読出し後の面を $\Sigma_{\rm bench}$ とする。$\Sigma_{\rm gate}$ はM48へ状態を渡すprovider面、$\Sigma_{\rm bench}$ はQ2-1の共同統計を監査する面である。同じ試行で先にbenchmark読出しを行い、その後にprovider状態を渡したとは扱わない。

R104、R105はM49内部の4モード担体に対する有限正準代数として使う。この代数だけからM50中央枝、bath、粒子位置は従わない。

## 4.2　4モード担体とCNOT代数

行優先ベクトル化を

```math
 d_{\rm prog}
 :=\operatorname{vec}_{\rm row}(D_{\rm prog})
 =((D_{\rm prog})_{00},(D_{\rm prog})_{01},(D_{\rm prog})_{10},(D_{\rm prog})_{11})^{\mathsf T}
 \tag{4.2}
```

とする。局所操作代数は

```math
 \mathcal A=M_2(\mathbb C)\otimes I_2,
 \qquad
 \mathcal B=I_2\otimes M_2(\mathbb C)
 \tag{4.3}
```

であり、局所unitaryは

```math
 D_{\rm prog}\longmapsto U_AD_{\rm prog}U_B^{\mathsf T}
 \tag{4.4}
```

と作用する。両代数は相互に可換で、積状態条件 $\det D_{\rm prog}=0$ を保存する。

<!-- theorem-start:lemma -->
**補題（R104：M49有限program担体の操作誘導テンソル積）**

固定作用4モード正準担体上に、式(4.3)の二つの局所操作代数を有限2次Hamiltonian流として実装できる。両代数は互いの可換代数に一致し、4次元担体へ操作誘導テンソル積を定める。これは一つの物理担体内の論理分解であり、2物理端への分配ではない。
<!-- theorem-end:lemma -->

CNOT射影を

```math
 \Pi_{\rm CX}
 =|1\rangle\langle1|_A
 \otimes\frac{I_2-\sigma_x}{2}
 \tag{4.5}
```

とする。対応する実2次生成子と時計Hamiltonianは

```math
 G_C
 =\frac14\left[(Q_{10}-Q_{11})^2+(P_{10}-P_{11})^2\right],
 \qquad
 H_C=P_\tau+g(\tau)G_C.
 \tag{4.6}
```

窓面積が $\pi$ なら、$e^{-i\pi\Pi_{\rm CX}}=U_{\rm CX}$ である。

<!-- theorem-start:lemma -->
**補題（R105：M49 program担体の厳密CNOT流と有限制御評価）**

面積 $\pi$ の有限時計窓は、4モードprogram担体上でCNOTと厳密に一致し、全作用と正準性を保存する。積入力 $|+0\rangle$ を $(|00\rangle+|11\rangle)/\sqrt2$ へ写すため、局所操作の積へは分解できない。4信号正準対と1時計正準対で実装でき、面積誤差と一般制御誤差は式(4.7)および直後の作用素距離で評価される。bath、粒子位置、選択器、記録を含むM49全体の資源は別に加える。
<!-- theorem-end:lemma -->

固定作用面で $0\leq G_C\leq\mathcal J_0$ である。$0\leq g\leq g_{max}$ なら動作時間は $T_{\rm g}\geq\pi/g_{max}$、面積誤差 $\delta A\in[-\pi,\pi]$ には

```math
 F_{\rm avg}
 =1-\frac35\sin^2\frac{\delta A}{2},
 \qquad
 d_{\rm proj}
 =2\sin\frac{|\delta A|}{4}
 \tag{4.7}
```

が成立する。一般Hermitian制御誤差を共通位相を除いた積分作用素ノルム $\eta_C$ で評価すると、実行unitaryはCNOTから作用素距離 $\min{2,\eta_C}$ 以下にある。

これらはR105の有限制御節であり、正確CNOTと別の結果を構成しない。

## 4.3　R157：行分解bath--粒子位置matching

規格化program $D_{\rm prog}$ の行重みを

```math
 \rho_a
 :=\sum_{b=0}^1|(D_{\rm prog})_{ab}|^2,
 \qquad
 \rho_0+\rho_1=1
 \tag{4.8}
```

とする。$\rho_a=0$ の行は活性枝から除く。M50で $v=d_{\rm prog}\in\mathbb C^4$、$\Psi=I_4$、$\delta=0$ とし、中央枝 $ab$ の作用と状態数を

```math
J_{ab}(D_{\rm prog})
=
\mathcal J_0|(D_{\rm prog})_{ab}|^2,
\qquad
\Omega_{ab}(D_{\rm prog})
=
\frac{(2\pi)^2}{J_{\rm ref}}J_{ab}(D_{\rm prog})
```

とする。従って活性支持上の単一母測度は $P(ab)=|(D_{\rm prog})_{ab}|^2$ を持つ。零容量枝は中央殻に存在せず、有限幅境界とdecode失敗は無反応とする。中央殻の排他的物理枝を $\gamma_{ab}$ と書く。安全枝ではfreshな2端粒子位置registerへ

```math
 (\gamma_{ab},x_A=e_0,x_B=e_0)
 \longmapsto
 (\gamma_{ab},x_A=e_a,x_B=e_b)
 \tag{4.9}
```

をcontrolled SWAPで直接decodeする。ここで $x_A,x_B$ は $X_A,X_B$ を担う2モードone-hot正準registerである。物理枝 $\gamma_{ab}$ を使用済み履歴へ残すため、decodeは拡大系で1対1である。M35の作用区間、一様選択器角、一時pointerを挟まない。

共通位相 $\theta$ を設定と独立に選び、第 $a$ 行用の事前校正bath templateを

```math
 z_A^{(a)}
 =\rho_a^{-1/4}e^{i\theta}e_a,
 \qquad
 z_B^{(a)}
 =\rho_a^{-3/4}e^{-i\theta}(D_{\rm prog})_{a\bullet}^{\mathsf T}
 \tag{4.10}
```

とする。$X_A=a$ のsafe plateauをcontrolとして、有限template bankからactive $z_A,z_B$ portへcanonical SWAPする。これにより

```math
 \mathbb E[z_Az_B^{\mathsf T}]=D_{\rm prog},
\qquad
 P(X_A=a,X_B=b)=|(D_{\rm prog})_{ab}|^2
 \tag{4.11}
```

が同じ試行族で厳密に成立する。さらに付録Jの局所核 $\pi_w^0$ に対して

```math
 \operatorname{Law}(X_A\mid z_A)=\pi_A^0(z_A),
 \qquad
 \operatorname{Law}(X_B\mid z_B)=\pi_B^0(z_B).
 \tag{4.12}
```

式(4.11)の第1式は集団上の交差モーメント、式(4.12)は単一試行bathに条件付けた粒子位置法則であり、役割を混同しない。共同Born型枝はR164の $m=L=4$、$\Psi=I_4$、$\delta=0$ 特殊化だけから得る。

安全事象を $G$ とする。各固定programの各非零branchで、比較境界、decode、template routingの失敗率が一様に $\varepsilon_0$ 以下になるよう有限装置を選ぶ。失敗は全て無反応へ送る。固定有限program族について

```math
 \rho_*
 :=\min_{s,a:\rho_a(D_{{\rm in},s})>0}\rho_a(D_{{\rm in},s})>0
 \tag{4.14}
```

と置けば、safe cross moment $M^G_{AB}=\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]$ は

```math
 P(G^c)\leq\varepsilon_0,
 \qquad
 \lVert M^G_{AB}-D_{\rm prog}\rVert_F
 \leq\frac{\varepsilon_0}{\sqrt{\rho_*}}
 \tag{4.15}
```

を満たす。$\varepsilon_0<\sqrt{\rho_*}$ なら、規格化cross projectorについて

```math
 d_\times(C_G^\times,d_{\rm prog}d_{\rm prog}^\dagger)
 \leq
 \min\left\{1,\frac{2\varepsilon_0}{\sqrt{\rho_*}}\right\},
 \qquad
 d_{\rm prog}=\operatorname{vec}_{\rm row}(D_{\rm prog})
 \tag{4.16}
```

である。A側matchingはsafe branch上で厳密、B側は

```math
 \varepsilon_X^A=0,
 \qquad
 \varepsilon_X^B
 \leq\frac{\varepsilon_0}{1-\varepsilon_0}
 \tag{4.17}
```

と評価できる。

<!-- theorem-start:theorem -->
**定理（R157：M49中央4枝状態数の有限Hamiltonian準備）**

任意の固定有限規格化program族について、M50中央4枝作用殻から二粒子位置を直接かつ可逆にdecodeし、行配置から事前校正bath templateをactive portへcanonical routingする有限Hamiltonian装置を構成できる。理想層では共同Born状態数、行周辺、式(4.11)、式(4.12)が厳密に整合し、有限装置では無反応を除外せず式(4.15)--(4.17)で誤差を抑えられる。交差モーメントまたは共同頻度を単一試行制御器へ書き戻さない。
<!-- theorem-end:theorem -->

「有限Hamiltonian準備」は、固定program用に校正済みの有限template bankからactive portへ可逆routingする意味である。未知入力の自然な自己分解ではない。また稀な行に一様資源上界はない。行 $a$ の条件付きcross momentを作る任意分解にはCauchy--Schwarzから

```math
 \mathbb E[\lVert z_A\rVert^2\mid a]
 \mathbb E[\lVert z_B\rVert^2\mid a]
 \geq\frac1{\rho_a}
 \tag{4.18}
```

が必要である。従って固定有限program族では有限だが、$\rho_a\to0$ を含む全program一様上界は主張しない。

## 4.4　R158：担体・bath・粒子位置へ同期するCNOT

係数行列上のCNOTを

```math
 \mathcal C_{\rm CX}(D_{\rm prog})
 :=P_0D_{\rm prog}+P_1D_{\rm prog}\sigma_x,
 \qquad
 P_a=|a\rangle\langle a|
 \tag{4.19}
```

とする。row-majorで $\operatorname{vec}_{\rm row}(\mathcal C_{\rm CX}(D_{\rm prog}))=U_{\rm CX}d_{\rm prog}$ である。R157の各試行へ

```math
 D_{\rm prog}^+=\mathcal C_{\rm CX}(D_{\rm prog}^-),
 \qquad
 z_A^+=z_A^-,
 \qquad
 z_B^+=\sigma_x^{X_A}z_B^-,
 \tag{4.20}
```

```math
 X_A^+=X_A^-,
 \qquad
 X_B^+=X_B^-\oplus X_A
 \tag{4.21}
```

を作用させる。A粒子位置registerのsafe value 1でだけ値1となり、境界では滑らかに0へ落ちるplateau関数を $\chi_1(x_A)$ とする。B側反対称射影 $\Pi_-=(I_2-\sigma_x)/2$ を用い、同じ時計窓に

```math
 G_C=\mathcal J_Cd_{\rm prog}^\dagger\Pi_{\rm CX}d_{\rm prog},
 \qquad
 G_z=\mathcal J_z\chi_1(x_A)z_B^\dagger\Pi_-z_B,
 \qquad
 G_X=\mathcal J_X\chi_1(x_A)x_B^\dagger\Pi_-x_B
 \tag{4.22}
```

を置く。三生成子はsafe sector上で異なるtarget registerに作用し、共有control $x_A$ の共役運動量を使わないためPoisson可換である。各面積を $\pi$ に合わせれば式(4.20)、式(4.21)を同時に得る。境界は無反応へ送り、反作用は使用済みcellへ残す。

理想層では行重みが保存され、各R157 branchは出力program $\mathcal C_{\rm CX}(D_{\rm prog})$ の対応branchへ点ごとに写る。従って

```math
 M_{AB}^+=\mathcal C_{\rm CX}(M_{AB}^-),
 \qquad
 P(X_A^+=a,X_B^+=b)
 =|\mathcal C_{\rm CX}(D_{\rm prog})_{ab}|^2.
 \tag{4.23}
```

CNOT枝置換を $P_{\rm CX}(a,b)=(a,b\oplus a)$ とすると、中央作用殻は

```math
\Omega_{P_{\rm CX}(a,b)}
\left(
\mathcal C_{\rm CX}(D_{\rm prog})
\right)
=
\Omega_{ab}(D_{\rm prog})
```

を満たす。作用殻消去表示の条件付き有効自由エネルギーも同じ置換で共変である。従って担体、bath、粒子位置だけでなく、Born型状態数と熱力学的地形も同じ出力programへ移る。この共変性は分布地形についての主張であり、時計パルス、制御器反作用、作用殻変形を含むCNOTの機械仕事が零であることを意味しない。

<!-- theorem-start:theorem -->
**定理（R158：担体・bath・粒子位置へ同期する同一試行CNOT）**

R157の各safe試行について、4モード担体、B bath、B粒子位置へ式(4.20)、式(4.21)の同じCNOTを1つの有限時計窓で作用させられる。理想写像は自己逆、正準、作用保存であり、交差モーメント、二粒子位置、中央作用殻の状態数地形を式(4.23)と上の置換共変式へ同時に写す。別標本化または集団制御器を使用しない。
<!-- theorem-end:theorem -->

有限bath反転誤差を $\eta_z$、粒子位置XOR誤差を $\varepsilon_\oplus$、担体誤差を $\eta_C$、時計同期誤差を $\varepsilon_{\rm clk}^{49}$ とする。例えば

```math
 \lVert M_{AB}^+-\mathcal C_{\rm CX}(D_{\rm prog})\rVert_F
 \leq
 \frac{\varepsilon_0}{\sqrt{\rho_*}}
 +\sqrt2\eta_z
 +\varepsilon_{\rm clk}^{49},
 \tag{4.24}
```

```math
 D_{\rm TV}(P_{\rm CX}^+,P_{\mathcal C_{\rm CX}(D_{\rm prog})})
 \leq\varepsilon_0+\varepsilon_\oplus,
 \qquad
 \varepsilon_{\rm sync}
 \leq\eta_C+\eta_z+\varepsilon_\oplus+\varepsilon_{\rm clk}^{49}.
 \tag{4.25}
```

と分ける。$\varepsilon_{\rm sync}$ は担体、bath、粒子位置が同じprogram出力を表すかの監査量であり、Q2-1共同分布誤差と同じ記号に吸収しない。

## 4.5　R159：固定有限共同入力--出力統計

固定有限benchmarkを

```math
 \mathcal B
 ={(D_{{\rm in},s},W_A^s,W_B^s,\lambda_s)}_{s=1}^S,
 \qquad
 \sum_s\lambda_s=1
 \tag{4.26}
```

とする。CNOT後と固定積分析器後の係数行列を

```math
 D_{{\rm gate},s}=\mathcal C_{\rm CX}(D_{{\rm in},s}),
\qquad
 D_{{\rm out},s}=W_A^sD_{{\rm gate},s}(W_B^s)^{\mathsf T}
 \tag{4.27}
```

とし、理想共同分布を

```math
 P_{\rm CX}^{\rm id}(s,a,b)
 =\lambda_s|(D_{{\rm out},s})_{ab}|^2,
 \qquad
 P_{\rm CX}^{\rm id}(s,\varnothing)=0
 \tag{4.28}
```

とする。

入力program頻度は、固定源 $r_\lambda=(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_S})$ に対する外側schedule $u_S$ から作る。これはbenchmark入力条件の提示であり、Born型出力の確率源ではない。選ばれた物理register $S=s$ により、program担体 $D_{{\rm in},s}$ と対応するR157 template bankをactive portへroutingする。R157の入力結果は中央M50殻の物理枝から直接decodeする。R158後、provider運転は $\Sigma_{\rm gate}$ で停止する。

benchmark運転だけは、同じ担体 $D_{{\rm gate},s}$ へ固定局所分析器を作用させて $D_{{\rm out},s}$ を得る。$D_{{\rm out},s}$ からfreshな中央4枝M50出力殻 $\Gamma_Y$ を準備し、その物理枝 $(a,b)$ をfresh結果register $Y_A=e_a,Y_B=e_b$ へ直接かつ可逆にdecodeする。入力殻 $\Gamma_X$ と出力殻 $\Gamma_Y$ は異なる物理registerであり、分析器前の担体を複製せず、出力表を装置へ直接書き込まない。

入力殻と出力殻で同じ微視的座標を再利用してはならない。例えば $\lambda_0=\lambda_1=1/2$、$P(Y=1\mid S=0)=1/4$、$P(Y=1\mid S=1)=3/4$ の目標分布は

```math
 P_{\rm id}(S,Y)
 =\begin{pmatrix}3/8&1/8\\1/8&3/8\end{pmatrix}.
 \tag{4.30}
```

$S=0$ と $S=1$ の入力枝を作った使用済み殻状態を、そのまま条件付き出力殻として再利用すると、入力枝との相関が残り得る。上の目標に対し、再利用した同一微視的順位が4共同枝を全て $1/4$ にする場合、式(4.30)からの全変動距離は $1/4$ である。この反例は、M50を使っても使用済み入力殻の微視的状態をfresh出力殻へ再利用してはならないことを示す。

入力選択誤差を $\varepsilon_S$、R157失敗を $\varepsilon_{157,s}$、準備・CNOT・分析器の純粋状態距離を $\delta_{\rm state,s}$、fresh出力殻の準備誤差を $\varepsilon_{{\rm sh},s}$、直接decode誤差を $\varepsilon_{\rm dec,s}$、記録誤差を $\varepsilon_{\rm rec}$ とする。無反応込みの実分布は

```math
 D_{\rm TV}(P_{\rm obs},P_{\rm CX}^{\rm id})
 \leq
 \varepsilon_S
 +\sum_s\lambda_s
 \left(
 \varepsilon_{157,s}
 +\delta_{\rm state,s}
 +\varepsilon_{{\rm sh},s}
 +\varepsilon_{\rm dec,s}
 \right)
 +\varepsilon_{\rm rec}.
 \tag{4.31}
```

<!-- theorem-start:theorem -->
**定理（R159：固定有限入力、入力頻度、固定積出力基底の共同入力--出力統計）**

任意の固定有限純粋入力、入力頻度、固定積出力基底、任意の $\epsilon>0$ に対し、program schedule、M49の中央入力殻・行分解準備、同期CNOT、固定積分析器、fresh中央M50出力殻、無反応込みの直接枝decodeからなる有限Hamiltonian benchmarkを構成できる。入力labelと2粒子位置出力の長期共同分布は式(4.28)から全変動距離 $\epsilon$ 未満にできる。
<!-- theorem-end:theorem -->

共同分布全体の精度に最小入力頻度は不要である。ただし各入力に条件付けた誤差を一様に主張する場合は

```math
 \lambda_*
 :=\min_{s:\lambda_s>0}\lambda_s
 \tag{4.32}
```

に対する条件付け誤差の増幅を別に評価する。R159は未知入力、完全過程tomography、独立同分布型有限標本、一般測定後状態を与えない。

## 4.6　R160：M49からM48への受渡し

M48へ渡す固定積入力を

```math
 D_{\rm in}^{\rm s}
 =\frac1{\sqrt2}
 \begin{pmatrix}0&-1\\0&1\end{pmatrix}
 \tag{4.33}
```

とする。R158後には

```math
 \mathcal C_{\rm CX}(D_{\rm in}^{\rm s})
=-\frac{\mathsf E}{\sqrt2}
 =:D_{\rm out}^{\rm s}
 \tag{4.34}
```

となる。$\rho_0=\rho_1=1/2$ なので、R157の二枝はCNOT後に

```math
 z_B=\mathsf E\overline{z_A},
 \qquad
 P(X_A,X_B)
 =\tfrac12\delta_{01}+\tfrac12\delta_{10},
 \tag{4.35}
```

```math
 \mathbb E[z_Az_B^{\mathsf T}]
 =-\frac{\mathsf E}{\sqrt2}
 \tag{4.36}
```

を満たす。これはM48の固定singlet fiberと同じbath・粒子位置matchingである。

$\Sigma_{\rm gate}$ を局所設定生成前の $\Sigma_{\rm link}$ とする。受渡し写像 $T_{\rm link}^{49\to48}$ は、active $z_A,z_B,X_A,X_B$ の恒等搬送、または元portを使用済みcellへ残すcanonical SWAPとする。$D_{\rm prog}$、program label、履歴は受動registerに保持し、M48の結果形成へ入力しない。使用済み中央作用殻の作用・角座標はM48へ渡さず、履歴識別子だけをprovenance-onlyで残す。M48の各局所作用殻はfreshな空registerから準備する。M48のseedは

```math
 S_0=(-1)^{X_A}
 \tag{4.37}
```

と定める。固定singlet programでは等重みであり、branch biasを変えた監査では同じbiasを保存する。

理想singlet接続では $\varepsilon_{\rm Q2-link}=0$ である。有限装置では

```math
 \varepsilon_{\rm Q2-link}
 =\varepsilon_\times
 +\varepsilon_X^A+\varepsilon_X^B
 +\varepsilon_{\rm carry}
 \tag{4.38}
```

とし、M48単独周期の誤差を $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ とすると

```math
 \varepsilon_{\rm Bell}^{49\to48}
 \leq
 \varepsilon_{\rm Q2-link}
 +\varepsilon_{\rm Bell}^{48,{\rm cyc}}.
 \tag{4.39}
```
<!-- theorem-start:theorem -->
**定理（R160：M49固定singlet providerからM48へのsetting-free同一register受渡し）**

$T_{\rm link}^{49\to48}$ はM49のlink面族全体でbath・粒子位置registerを変えず、付録Jのprogram matching、setting-free性、拡大系での1対1性を満たす。異なる二つのcross projector間距離と枝biasを保存するため、受渡し面ではstate-carryingかつbranch-carryingである。M48 Bell周期へ接続する現行結論は式(4.33)の固定singlet programに限る。理想singlet接続では式(4.38)が零となり、有限装置では式(4.39)の接続Bell誤差上界を持つ。
<!-- theorem-end:theorem -->

右辺が $(\sqrt2-1)/4$ 未満なら、R155のCHSH不等式の破れが接続周期でも残る。一般Q2-1出力を一般状態Bell receiverへ渡す定理ではない。

## 4.7　資源、達成判定、非主張

一つの固定programに対するR157準備の透明な単純上界は次である。

| 部品 | 正準対 |
|---|---:|
| 4モードprogram担体 | 4 |
| 中央2作用殻のactive枝 | 2 |
| $X_A,X_B$ one-hot粒子位置register | 4 |
| active $z_A,z_B$ | 4 |
| 2行分bath template bank | 8 |
| 合計 | 22 |

この22対は、program担体、1つのactive作用殻、粒子位置、active bath、固定2行templateを明示した単純上界である。CNOT時計、外側program schedule、fresh出力benchmark殻、履歴、永久記録は運転方式に応じて別に加える。これは存在上界であり最小性を主張しない。active bath作用は

```math
 \mathcal J_{\rm bath}^{max}
 \leq\frac{2\mathcal J_0}{\sqrt{\rho_*}},
 \qquad
 \mathbb E[\mathcal J_{\rm bath}^{\rm active}]
 \leq2\sqrt2\mathcal J_0.
 \tag{4.40}
```

R157--R159と共通R164により、Q2-1は固定有限benchmark、無反応込み、制御された任意精度の範囲で引き続き達成である。根拠はR104、R105、R157--R159、R164となり、M50枝からの直接decodeを明示しても判定語は変えない。R160により、固定singlet programは付録Jの契約を満たしてM48へ物理的に接続される。Q2-2全体はR155の条件付き局所因子化を加えても、固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則という範囲の条件付き達成を維持する。

次は含まない。

1. 未知入力に対する一般量子channel。
2. 任意Q2-1出力を処理する一般状態Bell receiver。
3. 独立同分布型有限標本統計。
4. 空間的に分離した自由設定Bell実験。
5. R162の有限衝突粒子位置bathとR153のrouting、paired-Hopf流、2翼controllerの同一ミクロHamiltonianへの統合。
6. $2^n$ モードを避ける多量子ビット拡張。

4モード担体の有限正準代数は再利用するが、担体近似だけをbath・粒子位置まで同期するM49の根拠にはしない。
