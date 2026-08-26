@number: K
@chapter: 付録
@title: Q2共同bath--実現配置の受渡し契約
@status: 本文と同格の規約

## K.1　目的と適用範囲

本付録は、Q2-1の二体ゲート過程とQ2-2のBell周期を、将来同じ「共同bath--実現配置」体系へ接続するための共通契約を固定する。ここで固定するのは、共有する試行状態、matching条件、受渡し面、設定独立性、破壊的読出しに許す範囲である。Q2-1の既存構成やM48単独周期が、すでにこの接続を実現したと主張するものではない。

1試行の共通状態を

```math
 \Gamma_{\rm Q2}
 =\bigl(X_A,X_B,z_A,z_B,\eta,H,R\bigr)
 \tag{K.1}
```

とする。$X_A,X_B$ は両端の実現配置、$z_A,z_B$ は局所応答へ渡す有限次元状態、$\eta$ は同一試行で共有されるbath変数、$H$ は不変な履歴台帳、$R$ は未使用・使用済みを含む補助レジスタである。試行測度を $\mu$、安全事象を $G$ と書く。

## K.2　共同bathのcross momentと共通vectorization

安全事象上のcross momentを

```math
 M^G_{AB}
 :=\mathbb E_\mu\!\left[
   \mathbf 1_G z_Az_B^{\mathsf T}
 \right],
 \qquad
 B^G_{AB}:=
 \frac{M^G_{AB}}{\lVert M^G_{AB}\rVert_F}
 \tag{K.2}
```

で定める。ただし $M^G_{AB}\neq0$ をmatchingの定義域とする。状態ベクトル化は全章でrow-majorに統一し、

```math
 \beta^G_{AB}:=\operatorname{vec}_{\rm row}(B^G_{AB}),
 \qquad
 C^\times_G:=\beta^G_{AB}(\beta^G_{AB})^\dagger
 \tag{K.3}
```

とする。反対称行列とsinglet projectorは

```math
 \mathsf E=
 \begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 B_{\rm s}:=\frac{\mathsf E}{\sqrt2},
 \qquad
 c_{\rm s}:=\operatorname{vec}_{\rm row}(B_{\rm s}),
 \qquad
 C_{\rm s}:=c_{\rm s}c_{\rm s}^\dagger
 \tag{K.4}
```

で固定する。物理的matchingの対象はglobal phaseを除いた射影類

```math
 [B_{\rm s}]
 :=\left\{
 e^{i\alpha}\frac{\mathsf E}{\sqrt2}:\alpha\in\mathbb R
 \right\}
 \tag{K.5}
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
 \tag{K.6}
```

を必ず明示する。$B=B_{\rm s}$ ではこの交換がglobal signに退化するが、一般状態ではそうならないため、この偶然を規約の省略理由にしてはならない。

## K.3　matching条件

共同bathと実現配置のmatchingは、次の3条件を同一の安全事象 $G$ 上で満たすことをいう。

第一に、cross projectorの統計的matchingを

```math
 d_\times(C^\times_G,C_{\rm s})
 :=\frac12\lVert C^\times_G-C_{\rm s}\rVert_1
 \leq \varepsilon_{\rm cross}
 \tag{K.7}
```

とする。第二に、各端 $w\in\{A,B\}$ の単一試行配置matchingを

```math
 \mathbb E_\mu\!\left[
 D_{\rm TV}\!\left(
  \operatorname{Law}(X_w\mid z_w,G),
  \pi_w^\delta(z_w)
 \right)
 \middle|G
 \right]
 \leq \varepsilon_X^w
 \tag{K.8}
```

とする。第三に、program matchingとして、受渡し後の局所装置が同じ物理レジスタから局所設定 $x,y$ に応答することを要求する。$\pi_w$ を端 $w$ のレジスタ射影、$\tau_w$ を許された物理輸送またはdilationとすると、

```math
 \pi_w\circ T_{\rm link}=\tau_w\circ\pi_w,
 \quad w\in\{A,B\},
 \qquad
 K_{\rm post}^{xy}=K_A^x\otimes K_B^y
 \tag{K.9}
```

とする。第一式はensembleから新しい端状態を再標本化せず、受け取った $X_w,z_w,R_w$ を局所programへ渡すことを表す。第二式は中央切断後の因数分解を表す。

式(K.7)はensemble統計、式(K.8)は単一試行の条件付き配置法則であり、役割が異なる。$B^G_{AB}$ や $C^\times_G$ を各試行で利用できるcontrollerとして再注入してはならない。それを行う場合は、別の推定器、記憶、準備過程とその因果位置を明示する必要がある。

## K.4　設定前受渡し面

Q2-1とQ2-2の物理的接続は、局所設定の生成より前に置くsetting-free受渡し面 $\Sigma_{\rm link}$ で定義する。この面の状態は

```math
 \operatorname{Law}(\Gamma_{\Sigma_{\rm link}}\mid x,y)
 =\operatorname{Law}(\Gamma_{\Sigma_{\rm link}})
 \tag{K.10}
```

を満たさなければならない。Q2-2入口は、Q2-1の出力試行状態とfreshな装置レジスタ $e_0$ から

```math
 \Gamma_{\rm in}^{48}
 =T_{\rm link}\!\left(
  \Gamma_{\rm out}^{\rm Q2-1},e_0
 \right)
 \tag{K.11}
```

として構成する。ensemble平均からsinglet形を再構成して各試行へ配る操作は、式(K.11)の代用にならない。

受渡し誤差の予約記法を

```math
 \varepsilon_{\rm Q2-link}
 :=\varepsilon_{\rm cross}
  +\varepsilon_X^A+\varepsilon_X^B
  +\varepsilon_{\rm carry}
 \tag{K.12}
```

とする。$\varepsilon_{\rm carry}$ は、同じ物理レジスタを受渡し面からM48入口まで運ぶ際の状態劣化、取り違え、または設定依存をまとめた量である。現稿には式(K.11)を満たすproviderがないため、式(K.12)は将来の接続判定用であり、M48単独周期の誤差台帳へは算入しない。

## K.5　許される破壊的読出し

activeレジスタを消去する読出しは、環境を含む拡大系で

```math
 \mathcal D:\bigl(\Gamma^-,e_0\bigr)
 \longmapsto
 \bigl(\Gamma^+,e_{\rm used}\bigr)
 \tag{K.13}
```

が一対一になるdilationとして記述する。したがって、activeレジスタの初期化自体は許すが、試行を識別する情報は $e_{\rm used}$ または不変な履歴 $H$ に残らなければならない。履歴は結果形成へ再注入せず、監査とprovenance照合にのみ使う。

式(K.13)は、入力の物理状態を後段の結果形成へ伝えたことを自動的には意味しない。破壊的写像の役割は次の3種に分類する。

| 分類 | 後段へ残る入力依存性 | 必要な感度検査 |
|---|---|---|
| state-carrying | 入力状態の2つ以上の射影類に応じて出力法則が変わる | 入力状態族に対する出力距離 |
| branch-carrying | 単一試行の枝変数またはそのbiasが出力枝へ残る | 枝bias sweep |
| provenance-only | 履歴識別子だけが残り、出力法則は変わらない | 履歴条件付き不変性 |

## K.6　枝bias監査

枝搬送を主張する場合、入口枝 $S_0\in\{+1,-1\}$ に対して

```math
 \mathbb P(S_0=+1)=p
 \quad\Longrightarrow\quad
 \mathbb P(S_{\rm route}=+1)=p
 \tag{K.14}
```

を、少なくとも $p=0,1/4,1/2,3/4,1$ で検査する。入力biasにかかわらず常に $1/2$ を返す装置はbranch-carryingではなく、内部fair-seed生成器である。

provenance-only接続では、許された履歴値 $h$ ごとに

```math
 \operatorname{Law}(A,B\mid x,y,H=h)
 =\operatorname{Law}(A,B\mid x,y)
 \tag{K.15}
```

を要求する。これにより、履歴照合を残しつつ、履歴をBell結果の隠れた入力にしない。

## K.7　現稿への適用

M48単独周期は、固定された $\mathsf E$、設定前の等重み枝seed、局所設定後の安全basin routing、R152の開放応答則、局所閾値読出しによってBell統計を構成する。この構成はQ2-2側のreceiverとしては閉じるが、式(K.11)のproviderを含まない。

旧R151のM39反対称射影は

```math
 \mathcal P_-(B)
 =\frac{B_{01}-B_{10}}2\,\mathsf E
 \tag{K.16}
```

であり、非零出力を正規化すると常に $[B_{\rm s}]$ へ潰れる。したがって一般のM39状態情報を運ぶstate-carrying写像ではない。等重み枝だけを使う現在のM48に対しては、内部fair seedで置換してもBell分布が変わらない。M39枝値とbiasを保存するadapterならbranch-carrying、履歴識別子だけを残すadapterならprovenance-onlyと分類する。

## K.8　段階判定

現稿の段階判定は次で固定する。

| 対象 | 現在の判定 | 未完了条件 |
|---|---|---|
| Q2-1の既存二体ゲート過程 | 達成 | 本段階では変更しない |
| M48単独Bell周期 | 条件付き達成 | 固定設定族、固定singlet、採用した開放法則に依存 |
| Q2-1からM48への物理的接続 | 未達成 | 式(K.7)--(K.13)を同じ試行レジスタで構成する |
| 固定目標Q2-2全体 | 部分達成 | receiverに加えて共同bath providerと受渡し写像を閉じる |

この区別により、M48単独周期の成果を維持したまま、未構成のQ2-1--Q2-2接続を達成済みと数えない。
