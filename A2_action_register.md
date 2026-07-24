@number: 7
@chapter: 第7章
@title: 物理的解釈、反証可能性、未解決問題
@status: 中心結果の範囲、循環論法、postselection、自然性、検証計画を整理。

## 7.1 到達した結果

本論文は、二側境界原理 `[R]` と equilibrium preparation `[E]` を明示的に分離した上で、次を一つの有限 Hamiltonian network に接続した。

1. setting を閉じた系内部の controller coordinate として表す。
2. 局所 analyzer が setting と definite outcome sign を canonical messenger へ書き込む。
3. 局所 pointer が記録時刻に一つの macroregion を通る。
4. messenger が記録後の共通未来で difference action を形成する。
5. physical comparator が difference action と soft-mode energy の差を terminal pointer へ記録する。
6. fixed setting-blind terminal condition が full-history measure を条件づける。
7. harmonic Liouville volume が difference action に線形なので standard cosine が得られる。
8. Bell-complete response は局所 deterministic のまま、microscopic measurement independence が破れる。
9. equilibrium ensemble では no-signalling と CHSH violation が両立する。

これは「古典 Hamiltonian が Bell の全前提を満たして不等式を破る」という結果ではない。Bell の前提違反が apparatus を含む microscopic measure のどこに現れるかを、有限 canonical coordinates 上で追跡した存在証明である。

## 7.2 何が Hamiltonian から導かれたか

次は明示 Hamiltonian の内部で厳密である。

- local rotation と outcome-dependent $\pi$ phase shift。
- pointer momentum への definite sign record。
- common-future quadratic action $I_-$。
- comparator pointer $\Pi_R=\kappa I_- -H_s$。
- one-pair sublevel volume および two-pair shell density の線形性。
- terminal compatibility、joint cosine law、visibility formula。
- equilibrium no-signalling、CHSH、measurement-dependence distance。

これに対して、次は Hamilton 方程式だけからは導かれていない。

- terminal condition を物理的全履歴 measure に用いる `[R]`。
- source が sign-symmetric equilibrium に限定される `[E]`。
- source phase lock `[P]` が自然な preparation から高 visibility で得られること。
- 理想 clock、frozen pointer、exact action shell の完全な mechanical regularization。

## 7.3 [R] の物理的地位

有限閉鎖 Hamiltonian は recurrence を持ち得る。また時間反転可能な方程式は final boundary condition を数学的には許す。しかし、これらは

$$
d\mu_R
\propto
\rho_iG_R\circ\Phi^T
$$

を物理的 probability law として一意に選ばない。`[R]` は依然として additional boundary-statistical principle である。

`[R]` を物理的に強めるには、少なくとも次を示す必要がある。

- terminal ready macroregion が実際の cyclic apparatus reset と一致する。
- terminal resolution と return time が Bell data fit より前に calibration される。
- 同一の terminal apparatus が全 setting と全 outcome に用いられる。
- apparatus を交換または terminal window を変えたときの deviation を事前予測できる。
- 実験後の trial rejection と異なる observable consequence を持つ。

## 7.4 循環論法の監査

目標 law を

$$
G_R
=
1-AB\cos\Delta
$$

のように terminal weight へ直接書けば、Bell correlation を説明したことにはならない。本論文の構成では順序を次に固定した。

1. $G_R=\mathbf1_{\{\Pi_R\geq0\}}$ または $\Pi_R=0$ を先に定義する。
2. setting-independent comparator Hamiltonian を定義する。
3. Hamilton 方程式から $\Pi_R=\kappa I_- -H_s$ を求める。
4. local rotations から $I_-$ の cosine cross term を求める。
5. soft-mode Liouville volume を積分する。
6. 最後に joint law と Fourier harmonic を計算する。

従って terminal rule 自体は cosine を参照しない。ただし comparator が $H_s$ と $I_-$ を比較するよう設計されている点は、物理的 engineering choice である。本模型はこの choice の単純さを示すが、generic recurrence が自動的に同じ comparator を生成することまでは証明しない。

## 7.5 標準 cosine の自然性

標準 cosine を選ぶ二つの構造は比較的明瞭である。

- cosine angle dependence は二次 Hamiltonian normal mode の inner product から生じる。
- linear probability dependence は最小 harmonic phase volume から生じる。

特に同じ apparatus が amplitude scale を変えても exact cosine を保つという要求は、scalar multiplicity を

$$
F(E)=CE
$$

に限定する。従って linear law は単なる一角度での curve fit より強く動機づけられる。

しかし「最小 canonical pair が自然界で必ず選ばれる」という結論は得ていない。追加 soft modes、anharmonicity、energy leakage があれば高調波または visibility loss が生じる。これらは模型の反証可能な deviation である。

## 7.6 postselection との経験的差

all-at-once boundary ontology と laboratory postselection は、同じ条件付き確率式を共有し得る。両者を区別するには言葉ではなく、実験 protocol が必要である。

本模型が物理的説明として成立するための最低条件は次である。

- Alice と Bob の全 pointer records が保存される。
- return apparatus の hidden state を理由に trial を削除しない。
- total trial rate と setting distribution を全設定で報告する。
- terminal device の calibration run を Bell run から独立に行う。
- terminal width、soft-mode energy、messenger amplitude を変更した予測を事前に固定する。

観測された subset に対してだけ CHSH violation が現れるなら、本模型の中心主張は成立しない。

## 7.7 preparability の課題

第6章の biased-subensemble example は、equilibrium no-signalling だけでは full physical theory に不十分であることを示す。任意 preparation における no-signalling を要求すると、最小模型はそのままでは失敗する。

この問題を単に「非 equilibrium は存在しない」と宣言して閉じるべきではない。必要なのは、source seed を操作する apparatus まで Hamiltonian boundary-value problem に含め、biased preparation を試みたときに何が起こるかを計算することである。可能性は次である。

1. preparation apparatus の terminal compatibility が bias を相殺する。
2. biased macrostate は `[R]` と両立する phase volume が零または極小になる。
3. biased preparation は可能で、模型は signalling prediction を持つ。

第三の場合、模型は実験的に排除される。第一または第二を有限 Hamiltonian から示せれば、`[E]` は独立公理でなく `[R]` の帰結へ近づく。

## 7.8 反証可能な量

同一 parameter set に対して、少なくとも次を同時に測る。

1. joint law の第一 harmonic visibility $V$。
2. second および higher harmonics。
3. no-signalling residual

$$
\epsilon_{\rm NS}
=
\max
\left|
P_R(A\mid a,b)-P_R(A\mid a,b')
\right|.
$$

4. setting normalization residual

$$
\epsilon_Z
=
\max_{a,b}
\left|
Z_{a,b}/\overline Z-1
\right|.
$$

5. measurement dependence $D_{\rm TV}$ と mutual information。
6. return-volume exponent

$$
\alpha_{\rm eff}
=
\frac{d\log\Omega_R}{d\log I_-}.
$$

7. pointer flip、missed outcome、terminal-width dependence。
8. biased preparation に対する signalling residual。

$|\mathcal S|>2$ だけを成功条件にしてはならない。

## 7.9 最小検証プログラム

旧稿の長い検証一覧は、次の六段階へ圧縮できる。

### 段階1：Hamiltonian map

全 canonical equations を積分し、local rotation、pointer shift、comparator shift が解析式と一致することを確認する。symplectic error と energy error を測る。

### 段階2：terminal compatibility

同じ $G_R$ を全 setting に用い、$h_{a,b}(\lambda)$ と $Z_{a,b}$ を直接計算する。measurement independence criterion を検査する。

### 段階3：phase volume

$I_-$ を変え、$\Omega_R(I_-)$ の exponent、cutoff、finite-width correction、高調波を測る。

### 段階4：Bell statistics

全 outcome joint law、marginals、CHSH、$D_{\rm TV}$ を同じ sample から計算する。

### 段階5：robustness

phase noise、amplitude mismatch、pulse overlap、anharmonicity、additional soft modes を変え、$V>1/\sqrt2$ の領域を求める。

### 段階6：preparation intervention

outcome-seed distribution を操作する apparatus を追加し、equilibrium symmetry が動的または境界的に回復するか、signalling が現れるかを判定する。

## 7.10 先行研究に対する位置

measurement-dependent singlet model [3--5] と time-symmetric boundary model [6--10] は、本論文の論理的可能性を既に示している。classical Hamiltonian measurement [14] と extended-phase-space autonomization [15,16] は、apparatus と clock を古典 Hamiltonian に含めること自体が障害でないことを示す。

本論文が追加するのは、それらを一つの有限 constructive network に接続し、setting-blind terminal function の pullback、physical comparator、linear Liouville volume、Bell assumption audit を同時に書いた点である。従って本模型の評価は、相関式が量子論と同じかだけでなく、`[R]` と `[E]` をどこまで独立な物理から正当化できるかによって決まる。

## 7.11 最終結論

有限古典 Hamiltonian mechanics と Bell violation の間に論理矛盾はない。Bell violation が生じるなら Bell の仮定のいずれかが失われており、本模型ではその位置を microscopic measurement independence に特定できる。

本論文は、局所で確定する記録を持つ有限 Hamilton 履歴、設定依存の二側測度、return-volume cosine 則、平衡 no-signalling、CHSH 違反を一つの明示模型として与えた。残る決定的課題は、物理的境界則 `[R]` と preparation equilibrium `[E]` を、追加の恣意的 selection rule ではなく、より大きな閉鎖 Hamilton 境界値問題から導けるかである。
