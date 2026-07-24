@number: 8
@chapter: 本文
@title: 頑健性、反証条件、証明台帳
@status: `[R]`、mixing、preparation symmetry の残る地位と、模型を区別する観測量を明示する。

## 8.1 到達した結果

第I部では、有限 Fourier--Gaussian bath から繰り込み済み作用の Nelson 極限を定量的に得た。第II部では、次の構造を一つの論理鎖にまとめた。

1. finite Hamiltonian local analyzer が definite anchor record を作る。
2. 二つの real messenger が common future で差動作用を形成する。
3. 差動作用は $1-ABV\cos\Delta_{ab}$ に比例する。
4. 一つの soft pair と一つの ledger pair の固定総作用殻が一様 threshold density を与える。
5. symmetric preparation が四 outcome sector の基準質量を $1/4$ にする。
6. return pair と center pair が、向きの相補的な二つの内部時計へ正準分解される。
7. setting-blind comparator が初期相対時計運動量 $E_*$ に $\kappa I_- -h$ を加え、$\Pi_R(T)=E_*+\kappa I_- -h$ を作る。
8. terminal half-space は順序付き時計向き保存条件として実現される。
9. `[R]` が terminal-compatible histories を物理的 ensemble とする。
10. 規格化後に Bell 型 joint law、no-signalling marginal、CHSH violation が得られる。
11. Bell の前提違反は measurement independence に現れる。

これは「閉じた Hamiltonian 方程式が forward evolution だけで Bell probability を生成した」という結果ではない。Hamiltonian dynamics、preparation measure、boundary ensemble の役割を分離した constructive compatibility theorem である。

## 8.2 `[R]` の物理的地位

有限閉鎖 Hamiltonian 系は recurrence を持ち得る。時間反転可能な方程式は final boundary condition を数学的に許す。しかし

$$
\text{finiteness}
+
\text{recurrence}
+
\text{time-reversal symmetry}
$$

だけから

$$
d\mu_R
\propto
\rho_S
G_R\circ\Phi^T
d\Gamma
$$

を物理的 probability law として一意に選ぶことはできない。`[R]` は本理論を標準的な初期値統計力学から区別する中心原理である。

従って `[R]` を削除するなら、少なくとも次のいずれかで同じ役割を置き換えなければならない。

- two-boundary condition。
- all-at-once history measure。
- setting-dependent source preparation。
- common-future consistency condition。
- action principle による complete-history selection。

名称を変えても、setting-dependent terminal compatibility を物理的履歴重みへ変換する構造は残る。何も置き換えずに通常の forward Liouville ensemble へ戻せば、Bell weight は得られない。

相補的内部時計はこの区別をさらに明確にする。$\Pi_R(T)\geq0$ は source で選んだ時計向きの順序が終端まで保存された条件として導ける。しかし $\Pi_R(T)<0$ の軌道も Hamiltonian 解であり、時計向きが交換されるだけである。従って時計相補性は $G_R$ の半空間を説明するが、$G_R$ を履歴確率へ変換しない。

各時計枝をそれぞれの clock-past 境界から準備し、同じ Hamiltonian 履歴として matching する規則を追加するなら、履歴空間上で

$$
d\nu
\propto
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
$$

と書ける。$z_f$ を積分すると

$$
d\nu_i
\propto
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i
$$

となり `[R]` の積形式を再現する。ただし、branch-wise boundary preparation と matching が追加の all-at-once 統計原理である。

さらに同じ scalar readout $\Pi_R(T)=x-h$ に対し、二つの相補的 half-space $\Pi_R(T)\geq0$ と $\Pi_R(T)\leq0$ を等重みで平均すると、

$$
F_+(x)
=
\frac{x}{E_\ell},
\qquad
F_-(x)
=
1-\frac{x}{E_\ell},
$$

$$
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12.
$$

従って Bell の cos 項は消える。単なる無向き相補性では足りず、順序付き sector、または時間反転した sector と comparator kick の符号を共変に結ぶ別の構造が必要である。

## 8.3 共有浴ノイズの順時間的漏れに関する否定結果

局所記録時刻 $t_m$ で、phase space を四つの disjoint record sector

$$
\Gamma_{AB}(t_m)
$$

に分ける。$t>t_m$ の共通浴を含む Hamiltonian flow を $\Phi^{t-t_m}$ とする。forward Liouville measure $\mu$ に対し、

$$
\mu
\left[
\Phi^{t-t_m}
\Gamma_{AB}(t_m)
\right]
=
\mu
\left[
\Gamma_{AB}(t_m)
\right]
$$

である。Hamiltonian flow は bijective かつ volume-preserving だからである。

従って、記録形成後に左右の copy を共通浴へ結合しても、全 trial を一度ずつ数える outcome-sector mass は変わらない。変わり得るのは

- bath state と record の相関。
- reaction time。
- 時刻占有率。
- finite timeout までの completion fraction。

である。

記録形成前に共通浴を左右へ結合すれば、相関を forward dynamics で作る余地はある。しかしその場合は spacelike-separated local response の coupling graph を改めて監査しなければならず、本論文の局所構成とは別模型になる。

従って本論文の Bell correlation は、共有浴ノイズの leakage ではない。共通未来の bath と mixer は、`[R]` の terminal compatibility を計算する装置部分である。

## 8.4 `[S]`、biased preparation、no-signalling

一般の基準 sector weight を $w_{AB}$ とすると、

$$
P_w(A,B\mid a,b,R)
=
\frac{
w_{AB}
\left[
C-ABKc
\right]
}{
\displaystyle
\sum_{A',B'}
w_{A'B'}
\left[
C-A'B'Kc
\right]
},
$$

$$
C=E_*+\kappa I_0,
\qquad
K=\kappa I_0V,
\qquad
c=\cos\Delta_{ab}.
$$

同時 sign flip symmetry

$$
w_{++}=w_{--},
\qquad
w_{+-}=w_{-+}
$$

があれば一側 outcome marginal は $1/2$ に保たれる。しかし parity sector の基準質量が異なると、全 compatibility は

$$
Z_{a,b}
=
C
-Kc
\sum_{A,B}ABw_{AB}
$$

となり、setting frequency が変化し得る。outcome marginal と controller frequency の両方を最も単純に保つ条件は

$$
w_{AB}=\frac14
$$

である。

例えば Bob seed を $B=+1$ に限定した基準 subensemble が操作的に準備可能なら、

$$
w_{++}=w_{-+}=\frac12,
\qquad
w_{+-}=w_{--}=0.
$$

このとき

$$
P_R(A=+1\mid a,b,B=+1)
=
\frac12
\left[
1-V_{\rm eff}\cos\Delta_{ab}
\right]
$$

となり、Alice の marginal は Bob の setting に依存する。従って `[S]` の equilibrium no-signalling は arbitrary-preparation no-signalling ではない。

full theory には次のいずれかが必要である。

1. biased preparation apparatus を含む boundary problem が symmetry を回復する。
2. biased seed macroregion の terminal-compatible volume が零または操作不能になる。
3. biased preparation が可能で、模型は signalling prediction を持つ。

第三の場合、本模型は実験的に排除される。`[S]` は反証不能な言葉で隠すのではなく、preparability test の対象にすべきである。

## 8.5 mixing の頑健性

二モード一様密度には三つの異なる誤差源がある。

1. **不完全 mixing**：finite observation window で $p(h)$ に residual structure が残る。
2. **action leakage**：$J_s+J_0$ が他 mode へ漏れ、fixed shell が崩れる。
3. **追加 ledger mode**：threshold-dependent energy を三つ以上の canonical pair が共有する。

入口密度を

$$
p(h)
=
\frac1{E_\ell}
\left[
1+\varepsilon r(h)
\right],
$$

$$
\int_0^{E_\ell}r(h)dh=0
$$

と書くと、compatibility weight は

$$
F(x)
=
\frac{x}{E_\ell}
+
\frac{\varepsilon}{E_\ell}
\int_0^x r(h)dh.
$$

$x=C-ABKc$ を代入したとき、第二項は一般に $c$ の非線形関数となる。従って不完全 mixing は visibility loss だけでなく、

$$
\cos2\Delta,
\qquad
\cos3\Delta,
\qquad
\ldots
$$

を生じ得る。

特に $N$ 個の通常 ledger mode に対する

$$
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N
$$

は、$N>1$ で明示的な高次調波を持つ。高調波の上限を測ることは、二モード縮約が実際に成立しているかを検査する直接的な方法である。

## 8.6 terminal width と cutoff

理想 terminal function

$$
G_R
=
\mathbf1_{\{\Pi_R\geq0\}}
$$

は sharp macroregion を用いる。有限分解能では、幅 $\epsilon_R$ の滑らかな response $g_{\epsilon_R}(\Pi_R)$ へ置き換える。compatibility は

$$
F_{\epsilon_R}(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
g_{\epsilon_R}(x-h)
$$

となる。

$x$ が両端 $0,E_\ell$ から $\epsilon_R$ より十分離れ、response kernel が translation-covariant なら、主要項は $x/E_\ell$ である。endpoint に近づくと clipping correction が入り、零 threshold channel は有限の background weight を持ち得る。

従って実験または数値検証では、

- $E_\ell$。
- $E_*$。
- $\kappa I_0$。
- terminal width $\epsilon_R$。

を独立に変え、first harmonic、higher harmonics、normalization residual を同時に測る必要がある。

## 8.7 reaction time と $E_*$ の交換関係

return pointer の後に、available energy

$$
x_{AB}
=
E_*+\kappa I_-^{AB}
$$

で自由 reaction coordinate を長さ $\ell_g$ だけ進ませるとする。質量を $M_g$ とすれば、理想自由飛行時間は

$$
\tau_g(x)
=
\ell_g
\sqrt{
\frac{M_g}{2x}
}.
$$

$E_*=0$ では $x\downarrow0$ の channel で時間が発散し得る。$E_*>0$ なら

$$
\tau_g(x_{AB})
\leq
\ell_g
\sqrt{
\frac{M_g}{2E_*}
}
$$

である。一方、Bell visibility は

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
$$

へ低下する。

従って $E_*$ を増やすと completion time は一様化するが、CHSH visibility は下がる。この同時変化は装置模型の反証可能な予測である。ただし $\tau_g$ は `[R]` で定まった weight を表示する後段時間であり、weight の起源ではない。

## 8.8 cos 則と Tsirelson 限界

本構成が直接与えるのは、実二次元の等振幅 messenger と quadratic difference comparator による

$$
I_-
\propto
1-AB\cos\Delta
$$

である。従って

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}
\leq
2\sqrt2
$$

は $0\leq V_{\rm eff}\leq1$ と comparator design の帰結である。

一般の非負 scalar comparator $F(I_-)$ を許せば、異なる correlation table を構成できる。本論文は、回転対称性、合成則、情報原理、Hamiltonian stability などから quadratic comparator を一意に選ぶ定理を持たない。従って $2\sqrt2$ を一般原理から導いたとは言えない。

## 8.9 Wallstrom 問題との関係

第I部の Nelson 表示から一般の Schrödinger theory を再構成するには、configuration space の閉路に沿う phase circulation を量子化する必要があり、Wallstrom 問題が残る [20]。

第II部で現れる cos は、

$$
u_A\cdot u_B
\propto
\cos\Delta_{ab}
$$

という comparator geometry である。これは Bell experiment の設定差に対する共同確率を与えるが、configuration-space phase $S(x)$ の閉路条件

$$
\oint\nabla S\cdot d\ell
\in
2\pi\hbar\mathbb Z
$$

を導かない。従って Bell 型 cos 共同確率が得られたことは、Wallstrom 問題の解決を意味しない。

ただし、同じ有限 Hamiltonian source の action-angle variable が、Bell messenger phase と Nelson phase の双方を拘束する追加機構を作れれば、両問題を結ぶ研究方向にはなり得る。その場合でも必要なのは単なる cos law ではなく、全許容閉路に対する整数 winding selection である。

## 8.10 検証プログラム

最小の検証を次の五段階に分ける。

### 段階1：local measurement

canonical equations を積分し、messenger rotation、bright shift、anchor shift、record holding time を測る。energy error、symplectic error、anchor flip rate を報告する。

### 段階2：two-mode ledger

固定 $J_\ell$ 上で $h/E_\ell$ の histogram、autocorrelation、mixing time、recurrence time を測る。Kolmogorov 距離または低次 moment だけでなく、threshold CDF の最大偏差

$$
\epsilon_F
=
\sup_{0\leq x\leq E_\ell}
\left|
F_{\rm emp}(x)-\frac{x}{E_\ell}
\right|
$$

を用いる。

### 段階3：terminal compatibility

全 setting と outcome に同じ $G_R$ を用い、$W_{AB}$ の $I_-$ に対する線形性、cutoff、terminal-width correction を直接測る。

### 段階4：Bell audit

joint law、marginal、CHSH、setting normalization、source posterior の全変動距離を同じ sample から計算する。observed trial の除外がないことを確認する。

### 段階5：robustness and preparation

phase noise、amplitude mismatch、additional ledger mode、action leakage、biased seed preparation、$E_*$、terminal width を変え、first harmonic、higher harmonics、no-signalling residual、completion time を同時に測る。

## 8.11 証明状態の台帳

| 主張 | 状態 |
|---|---|
| finite Fourier--Gaussian 表示 | 厳密 |
| 条件付き Gaussian law の Schur 補完 | 厳密 |
| 繰り込み作用のパラメータ $C^1$ Nelson 極限 | 指定した線形 Gaussian class で厳密 |
| local bright/anchor record | finite pulse Hamiltonian で明示 |
| cos 型差動作用 | 厳密な二次形式恒等式 |
| 固定総作用殻上の $p(h)=1/E_\ell$ | 正規化 Liouville measure について厳密 |
| 任意初期密度からの厳密な一様化 | 不成立。粗視化 mixing `[M]` のみ |
| $w_{AB}=1/4$ | symmetric preparation `[S]` の下で厳密 |
| setting-blind terminal coordinate | finite Hamiltonian pulse で明示 |
| terminal half-space の相補時計実現 | canonical transformation と向き保存条件として厳密 |
| branch-wise boundary matching から `[R]` の積形式 | matching rule を追加した条件付き定理 |
| 二つの相補的 half-space の等重み平均 | cos 項が消えるという厳密な no-go |
| Bell joint law | `[H,P,S,M,R]` と working range の下で厳密 |
| macroscopic setting normalization | `[S]` の下で厳密 |
| equilibrium no-signalling | `[S]` の下で厳密 |
| arbitrary-preparation no-signalling | 未証明 |
| `[R]` の物理的必然性 | 未導出 |
| cos comparator の一意性 | 未導出 |
| Tsirelson bound の独立導出 | 行っていない |
| Wallstrom phase quantization | 未解決 |

## 8.12 最終結論

本論文の確立した第I部の中心結果は、有限調和 Gaussian 条件付き作用の定量的パラメータ $C^1$ Nelson 極限である。第II部の中心結果は、有限 Hamiltonian 測定器、phase-locked source、symmetric preparation、固定総作用二モード台帳、setting-blind terminal condition、時間対称境界統計原理を組み合わせた Bell compatibility theorem である。

旧構成で一つの仮定にまとめていた共通入口密度は、

$$
\text{two-mode Liouville geometry}
+
\text{sector symmetry}
$$

へ分解された。これにより、soft-energy density の形は位相体積から導かれ、残る統計入力は準備対称性として明示された。

相補的内部時計により、return momentum、terminal half-space、$E_*$ はそれぞれ相対時計運動量、順序付き時計向き保存、向き反転までの初期余裕として解釈できるようになった。これは terminal device の任意性を減らす進展である。一方、`[R]` は消去されていない。時計向きが交換される Hamiltonian 軌道を物理的集団から除くには、二境界 matching または同等の all-at-once 統計原理がなお必要である。

従って `[R]` は欠陥を隠すための補助仮定ではなく、本理論が通常の初期値統計力学と異なる位置を明示する中心原理である。今後の決定的課題は、branch-wise boundary preparation と matching をより大きな物理的境界値問題から導くこと、順序付き sector の時間反転共変な完成形を構成すること、またはその実験的含意を postselection と区別することである。
