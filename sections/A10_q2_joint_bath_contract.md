@number: J
@chapter: 付録
@title: Q2共同bath--二粒子位置の受渡し契約
@status: 本文と同格の規約

## J.1　目的と適用範囲

本付録は、Q2-1の二体ゲート過程とQ2-2のBell周期を同じ「共同bath--粒子位置」体系へ接続する共通契約を固定する。共有する試行状態、matching条件、受渡し面、設定独立性、破壊的読出しに許す範囲を定め、第4章のM49とR160が固定singlet供給プログラムについてこの契約を満たすことを監査する。一般Q2-1出力または一般状態Bell測定への拡張を含めない。

1試行の共通状態を

```math
 \Gamma_{\rm Q2}
 =\bigl(X_A,X_B,z_A,z_B,\eta,H,R\bigr)
 \tag{J.1}
```

とする。$X_A,X_B$ は両端の粒子位置、$z_A,z_B$ は局所応答へ渡す有限次元状態、$\eta$ は同一試行で共有されるbath変数、$H$ は不変な履歴台帳、$R$ は未使用・使用済みを含む補助レジスタである。試行測度を $\mu$、安全事象を $G$ と書く。

## J.2　共同bathのcross momentと共通vectorization

安全事象上のcross momentを

```math
 M^G_{AB}
 :=\mathbb E_\mu\!\left[
   \mathbf 1_G z_Az_B^{\mathsf T}
 \right],
 \qquad
 B^G_{AB}:=
 \frac{M^G_{AB}}{\lVert M^G_{AB}\rVert_F}
 \tag{J.2}
```

で定める。ただし $M^G_{AB}\neq0$ をmatchingの定義域とする。状態ベクトル化は全章でrow-majorに統一し、

```math
 \beta^G_{AB}:=\operatorname{vec}_{\rm row}(B^G_{AB}),
 \qquad
 C_G^\times:=\beta^G_{AB}(\beta^G_{AB})^\dagger
 \tag{J.3}
```

とする。反対称行列とsinglet projectorは

```math
 \mathsf E=
 \begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 B_{\rm s}:=\frac{\mathsf E}{\sqrt2},
 \qquad
 \beta_{\rm s}:=\operatorname{vec}_{\rm row}(B_{\rm s}),
\qquad
 C_{\rm s}^\times:=\beta_{\rm s}\beta_{\rm s}^\dagger
 \tag{J.4}
```

で固定する。物理的matchingの対象はglobal phaseを除いた射影類

```math
 [B_{\rm s}]
 :=\left\{
 e^{i\alpha}\frac{\mathsf E}{\sqrt2}:\alpha\in\mathbb R
 \right\}
 \tag{J.5}
```

である。

column-major記法を使う場合は、中央2成分を交換する置換

```math
 P_{23}=
 \begin{pmatrix}
 1&0&0&0\\
 0&0&1&0\\
 0&1&0&0\\
 0&0&0&1
 \end{pmatrix},
 \qquad
 \operatorname{vec}_{\rm col}(B)
 =P_{23}\operatorname{vec}_{\rm row}(B)
 \tag{J.6}
```

を必ず明示する。$B=B_{\rm s}$ ではこの交換がglobal signに退化するが、一般状態ではそうならないため、この偶然を規約の省略理由にしてはならない。

## J.3　matching条件

共同bathと粒子位置のmatchingは、次の3条件を同一の安全事象 $G$ 上で満たすことをいう。

第一に、cross projectorの統計的matchingを

```math
 d_\times(C_G^\times,C_{\rm s}^\times)
 :=\frac12\lVert C_G^\times-C_{\rm s}^\times\rVert_1
 \leq \varepsilon_\times
 \tag{J.7}
```

とする。第二に、各端 $w\in\{A,B\}$ の単一試行粒子位置matchingを

```math
 \mathbb E_\mu\!\left[
 D_{\rm TV}\!\left(
  \operatorname{Law}(X_w\mid z_w,G),
  \pi_w^\delta(z_w)
 \right)
 \middle|G
 \right]
 \leq \varepsilon_X^w
 \tag{J.8}
```

とする。第三に、program matchingとして、受渡し後の局所装置が同じ物理レジスタから局所設定 $x,y$ に応答することを要求する。$\pi_w$ を端 $w$ のレジスタ射影、$\tau_w$ を許された物理輸送またはdilationとすると、

```math
 \pi_w\circ T_{\rm link}=\tau_w\circ\pi_w,
 \quad w\in\{A,B\},
 \qquad
 K_{\rm post}^{xy}=K_A^x\otimes K_B^y
 \tag{J.9}
```

とする。第一式はensembleから新しい端状態を再標本化せず、受け取った $X_w,z_w,R_w$ を局所programへ渡すことを表す。第二式は中央切断後の因数分解を表す。

式(J.7)はensemble統計、式(J.8)は単一試行の条件付き粒子位置法則であり、役割が異なる。$B^G_{AB}$ や $C_G^\times$ を各試行で利用できるcontrollerとして再注入してはならない。それを行う場合は、別の推定器、記憶、準備過程とその因果位置を明示する必要がある。付録L.2の階数1共分散の支持補題は自己共分散 $\mathbb E[ZZ^\dagger]$ に対する結果であり、交差モーメント $\mathbb E[z_Az_B^{\mathsf T}]$ または $C_G^\times$ から積標本 $z_A\otimes z_B$ の支持を導くためには使えない。

## J.4　設定前受渡し面

Q2-1とQ2-2の物理的接続は、局所設定の生成より前に置くsetting-free受渡し面 $\Sigma_{\rm link}$ で定義する。この面の状態は

```math
 \operatorname{Law}(\Gamma_{\Sigma_{\rm link}}\mid x,y)
 =\operatorname{Law}(\Gamma_{\Sigma_{\rm link}})
 \tag{J.10}
```

を満たさなければならない。Q2-2入口は、Q2-1の出力試行状態とfreshな装置レジスタ $e_0$ から

```math
 \Gamma_{\rm in}^{48}
 =T_{\rm link}\!\left(
  \Gamma_{\rm out}^{\rm Q2-1},e_0
 \right)
 \tag{J.11}
```

として構成する。ensemble平均からsinglet形を再構成して各試行へ配る操作は、式(J.11)の代用にならない。

受渡し誤差の予約記法を

```math
 \varepsilon_{\rm Q2-link}
 :=\varepsilon_\times
  +\varepsilon_X^A+\varepsilon_X^B
  +\varepsilon_{\rm carry}
 \tag{J.12}
```

とする。$\varepsilon_{\rm carry}$ は、同じ物理レジスタを受渡し面からM48入口まで運ぶ際の状態劣化、取り違え、または設定依存をまとめた量である。M49のR160は式(J.11)を満たす。式(J.12)は接続周期の誤差として式(4.38)へ算入するが、M48だけを単独運転するときの誤差台帳へは算入しない。

## J.5　許される破壊的読出し

activeレジスタを消去する読出しは、環境を含む拡大系で

```math
 \mathcal D:\bigl(\Gamma^-,e_0\bigr)
 \longmapsto
 \bigl(\Gamma^+,e_{\rm used}\bigr)
 \tag{J.13}
```

が一対一になるdilationとして記述する。したがって、activeレジスタの初期化自体は許すが、試行を識別する情報は $e_{\rm used}$ または不変な履歴 $H$ に残らなければならない。履歴は結果形成へ再注入せず、監査とprovenance照合にのみ使う。

式(J.13)は、入力の物理状態を後段の結果形成へ伝えたことを自動的には意味しない。破壊的写像の役割は次の3種に分類する。

| 分類 | 後段へ残る入力依存性 | 必要な感度検査 |
|---|---|---|
| state-carrying | 入力状態の2つ以上の射影類に応じて後段入口または出力法則が変わる | 入力状態族に対する入口・出力距離 |
| branch-carrying | 単一試行の枝変数またはそのbiasが出力枝へ残る | 枝bias sweep |
| provenance-only | 履歴識別子だけが残り、出力法則は変わらない | 履歴条件付き不変性 |

## J.6　枝bias監査

枝搬送を主張する場合、入口枝 $S_0\in\{+1,-1\}$ に対して

```math
 \mathbb P(S_0=+1)=p
 \quad\Longrightarrow\quad
 \mathbb P(S_{\rm route}=+1)=p
 \tag{J.14}
```

を、少なくとも $p=0,1/4,1/2,3/4,1$ で検査する。入力biasにかかわらず常に $1/2$ を返す装置はbranch-carryingではなく、内部fair-seed生成器である。

provenance-only接続では、許された履歴値 $h$ ごとに

```math
 \operatorname{Law}(A,B\mid x,y,H=h)
 =\operatorname{Law}(A,B\mid x,y)
 \tag{J.15}
```

を要求する。これにより、履歴照合を残しつつ、履歴をBell結果の隠れた入力にしない。

## J.7　M49とM48への適用

M48単独周期は、固定された $\mathsf E$、設定前の等重み枝seed、局所設定後の安全basin routing、R161のM48特殊化の開放応答則、局所閾値読出しによってBell統計を構成する。M49は固定singlet供給プログラムに対し、CNOT後の同じ試行registerを式(J.11)でM48へ渡す。

M49は4モード担体からM50/R164の中央4枝を作って粒子位置へ直接decodeし、行templateをactive bathへroutingした後、担体、bath、粒子位置へCNOTを点ごとに作用させる。R160の $T_{\rm link}^{49\to48}$ はbath・粒子位置registerの恒等搬送であり、M49 link面族の少なくとも2つのcross projector間距離を保存するため、受渡し面に対してstate-carryingである。Bell結果まで閉じる現行定理は固定singletに限る。$S_0=(-1)^{X_A}$ は枝biasも保存し、履歴は結果形成へ入れない。

## J.8　段階判定

現稿の段階判定は次で固定する。

| 対象 | 現在の判定 | 未完了条件 |
|---|---|---|
| Q2-1のM49二体ゲート過程 | 達成 | 固定有限ベンチマーク、無反応込み、任意精度 |
| M48単独Bell周期 | 条件付き達成 | 固定設定族、固定singlet、採用した開放法則に依存 |
| M49からM48への物理的接続 | 固定singletについて達成 | 一般Q2-1出力と一般状態Bell測定は含まない |
| 固定目標Q2-2全体 | 条件付き達成 | 固定singlet、固定有限設定族、準備先行、非空間分離、採用開放法則に限定 |

この区別により、M48単独周期とM49--M48接続周期を別々に誤差評価し、固定singletの接続達成を一般状態受渡しへ拡張しない。

## J.9　作用殻registerの役割契約

Q2で使う作用殻registerを次の3種類へ分ける。

| 役割 | 物理的内容 | 受渡し |
|---|---|---|
| state-carrying | $z_A,z_B$ とcross projector感度を保持するbath・粒子位置register | M49からM48へ同じ物理registerを運ぶ |
| branch-carrying | 中央4枝状態数から選ばれた $X_A,X_B$ と固定singlet枝bias | M48の $S_0=(-1)^{X_A}$ へ渡す |
| provenance-only shell | 使用済み中央殻の作用・角座標を退避した履歴 | 履歴識別子だけを残し、結果形成へ再注入しない |

中央作用殻の使用済み微視的状態はM48へ渡さない。各翼はfreshな局所作用殻、局所衝突セル、局所雑音seedから開始する。完全共通原因 $\Lambda$ に条件付けた切断後契約を

```math
\mu_{\rm sh}^{AB}
(d\gamma_A,d\gamma_B\mid\Lambda,x,y)
=
\mu_{{\rm sh},A}^x
(d\gamma_A\mid\Lambda)
\otimes
\mu_{{\rm sh},B}^y
(d\gamma_B\mid\Lambda)
```

とする。有限偏差は $\varepsilon_{\rm prod}$ として接続誤差、局所instrument誤差、paired-Hopf誤差と分けて監査する。

切断後に $-\Theta\log P(a,b\mid x,y)$ を物理的な大域自由エネルギーとして局所率へ入力することを禁止する。これは式(J.9)の局所因子化に反する。条件付き局所有効自由エネルギーは各翼で使えるが、$\Lambda$ を平均した後の共同分布の対数は情報的要約に限る。
