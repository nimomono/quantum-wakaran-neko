# プロジェクト情報源から抽出した主要結果

> **統合前メモ。** 本文書は、プロジェクト情報源にある重要な定理と条件付き命題を抽出したものである。既存本文との整合性は未確認であり、`sections/` 以下の正本文書を置き換えるものではない。情報源にない接続は補わず、未確定部分は「未導出事項」として残す。

## 第I部　二側縮約とNelson作用

### 1. 有限線形Gaussian系の二側条件づけ定理

有限Fourier–Gaussian表示から得られる線形過程を $X_N(t)$ とする。初期側の記録を条件づけたGaussian初期分布に含め、終端側で有限分解能の記録

```math
Y=HX_N(T)+\varepsilon,\qquad
\varepsilon\sim N(0,R),\qquad R\ge r_*I>0
```

を与える。無条件平均と共分散を $\mu_N(t)$、$C_N(s,t)$ とし、

```math
S_N=HC_N(T,T)H^{\mathsf T}+R
```

と置く。

**定理。** $Y=y$ の下で $X_N$ はGaussian過程のままであり、条件付き平均と共分散は

```math
\mu_N^R(t)
=\mu_N(t)+C_N(t,T)H^{\mathsf T}S_N^{-1}
\left[y-H\mu_N(T)\right],
```

```math
C_N^R(s,t)
=C_N(s,t)-C_N(s,T)H^{\mathsf T}
S_N^{-1}HC_N(T,t)
```

で与えられる。

これは結合Gaussian分布のSchur補完である。終端記録による共分散の減少は統計的更新であり、終端装置から過去へ作用する力ではない。$R>0$ により逆行列とそのパラメータ微分が一様に制御される。点終端 $R=0$ と、一般の非線形Hamiltonian系への拡張は未導出事項である。

### 2. 前向き因子・後向き因子の分解定理

Markov拡散極限において、初期準備から伝播した前向き因子を $\alpha(x,t)$、終端記録の後向き尤度を $\beta(x,t)$ とすると、二側条件付き密度は

```math
\rho(x,t)
=\frac{\alpha(x,t)\beta(x,t)}
{\int \alpha(x,t)\beta(x,t)\,dx}
```

と書ける。基準となる前進流れを $b_+^0$ とすれば、終端条件づけ後の前進流れはDoob変換

```math
b_+=b_+^0+2\nu\nabla\log\beta
```

で与えられる。前進・後退流れの間には

```math
b_--b_+=-2\nu\nabla\log\rho
```

が成り立つため、

```math
v=\frac{b_++b_-}{2},\qquad
u=\frac{b_+-b_-}{2}
=\nu\nabla\log\rho
```

を、それぞれ流れ速度と浸透速度として得る。

この分解が与えるのは、同じ基準過程に対する二側条件づけとNelson型の速度分解である。位置だけの積 $\alpha\beta$ から位相や干渉項が自動的に生じるわけではない。また、一般の縮約Fokker–Planck方程式の解全体がNelson流に一致するという主張は未導出事項である。

### 3. 繰り込み粗視化作用の収束定理

有限差分

```math
D_hX_N(t)=\frac{X_N(t+h)-X_N(t)}{h}
```

を用い、拡散経路で普遍的に発散する項を差し引いた作用を

```math
\mathcal A_{N,h}^{R,U}(\theta)
=\mathbb E_{N,\theta}^{R}
\int_0^{T-h}
\left[
\frac{m}{2h^2}|X_N(t+h)-X_N(t)|^2
-\frac{md\nu}{h}
-U_\theta(X_N(t),t)
\right]dt
```

とする。差し引く項は結果や設定に依存しない。

**定理。** 線形Gaussian系、有限分解能記録、2次ポテンシャル、滑らかな有限次元パラメータ族という仮定の下で、

```math
\left\|
\mathcal A_{N,h}^{R,U}
-\mathcal A_{\mathrm{GM}}^{R,U}
\right\|_{C^1(K)}
\le C_K
\left(
\frac{h}{T}+\frac{T^2}{Nh^2}
\right)
```

が成り立つ。特に $h_N=TN^{-1/3}$ とすれば、作用値と指定したパラメータ方向の第1変分は誤差 $O(N^{-1/3})$ でGuerra–Morato作用へ収束する。

境界項が消える条件の下では、

```math
\mathcal A_{\mathrm{GM}}^{R,U}
=\int \rho
\left[
\frac m2|v|^2-\frac m2|u|^2-U
\right]dx\,dt
=\mathcal A_{\mathrm{Nel}}^{R,U}
```

であり、極限作用はNelson作用に一致する。

$C^1$ 収束から、収束する有限模型の停留点列の極限がNelson作用の停留点であることは従う。逆に、任意のNelson停留点が有限模型から得られること、無限次元の全変分、一般の非線形Hamiltonian系、収束率の最適性は未導出事項である。

### 4. 作用差と干渉の条件付き命題

2経路の繰り込み済みHamilton作用差を

```math
\Delta\theta
=\frac{S_L^{\mathrm{ren}}-S_R^{\mathrm{ren}}}
{\hbar_{\mathrm{eff}}}
```

とする。前向き分布と後向きチャンネル尤度が、同じ円周位相変数を持ち、その第1Fourier成分がこの作用差に固定されるなら、位相変数を積分した重みは

```math
W
=w_L+w_R
+2\sqrt{w_Lw_R}\,
V_{LR}\cos(\Delta\theta+\delta),
\qquad 0\le V_{LR}\le1
```

の形になる。

**条件付き命題。** 正の二側確率の積からcos項を得ることはできるが、そのためには、作用差と共通のコサイクルに結び付いた位相変数と、それに感応する後向き尤度が必要である。位置密度だけの二側条件づけでは不十分である。

一般の複素振幅加算則、この位相構造の単一Hamiltonianからの生成、Wallstromの循環量子化は未導出事項である。

## 第II部　固有状態と測定

### 5. 有限閉鎖Hamiltonian系の非吸引定理

**定理。** 有限次元の閉じたHamiltonian流はLiouville体積を保存する。そのため、正の体積を持つ初期集合を、より低次元の固有状態集合や指針領域へ不可逆に収縮させる真の吸引子を持たない。運動が有界なら再帰も避けられない。

したがって、可逆な前測定は系と指針を相関させるが、単一結果を選ばない。有限環境によるデコヒーレンスは干渉を有限時間抑制できるが、真正混合や永久記録を与えない。固有状態は停留状態または周期状態にはなり得ても、有限閉鎖力学だけで確率的吸収状態にはならない。

### 6. 有効選択法則の収束定理

離散スペクトル

```math
M=\sum_r m_r\Pi_r,\qquad [H,M]=0
```

を持つ観測量に対し、次の規格化確率過程を追加する。

```math
d\psi_t
=\left[
-\frac{i}{\hbar_{\mathrm{eff}}}H
-\frac{\kappa}{2}(M-\bar M_t)^2
\right]\psi_t\,dt
+\sqrt{\kappa}(M-\bar M_t)\psi_t\,dW_t,
```

```math
\bar M_t=\langle\psi_t,M\psi_t\rangle.
```

この法則はノルムを保存し、平均密度行列は

```math
\partial_t\varrho_t
=-\frac{i}{\hbar_{\mathrm{eff}}}[H,\varrho_t]
-\frac{\kappa}{2}[M,[M,\varrho_t]]
```

に従う。スペクトル重み

```math
p_r(t)=\langle\psi_t,\Pi_r\psi_t\rangle
```

は

```math
dp_r
=2\sqrt{\kappa}(m_r-\bar M_t)p_r\,dW_t
```

を満たす有界マルチンゲールである。また

```math
V_t=\langle\psi_t,(M-\bar M_t)^2\psi_t\rangle
```

について

```math
\frac{d}{dt}\mathbb E[V_t]
=-4\kappa\,\mathbb E[V_t^2]\le0
```

となり、$V_t\to0$ がほとんど確実に成り立つ。

**定理。** 有限離散スペクトルと $[H,M]=0$ の下で、過程は1つの固有空間へほとんど確実に収束し、

```math
\mathbb P(R_\infty=r)
=p_r(0)
=\|\Pi_r\psi_0\|^2
```

となる。Born到達確率は、この有効選択法則を置いた後ではマルチンゲール性から厳密に従う。

ただし、この法則のWiener雑音、係数 $\kappa$、指針・記録環境からのMarkov極限を有限Hamiltonian系から導くことは未導出事項である。$[H,M]\ne0$ の一般の場合も、この単純な定理の範囲外である。

### 7. 測定法則の導出範囲

- **位置。** 位置表現では $P(X_t\in dx)=\rho(x,t)\,dx$ であり、波動関数表示が成立する範囲では $\rho=|\psi|^2$ である。
- **運動量。** Nelson流の運動量分布は、瞬間的な標本速度の分布ではない。適切な自由飛行極限では、飛行後の漸近速度から運動量分布を操作的に読み出す。
- **一般測定。** 解析器による基底選択、指針との可逆な前測定、デコヒーレンス、前節の有効選択法則を別段階として扱う。選択法則を仮定した後の到達確率は証明済みだが、一般測定の $P_n=|c_n|^2$ を有限Hamiltonian中核だけから導くことは未導出事項である。

## 第III部　Bell型統計

### 8. 境界作用殻とBell共同確率

#### 8.1 全Hamiltonianと浴による比較器

情報源の最新版では、測定窓全体を、概略

```math
H_{\rm tot}
=
H_{\rm src}
+H_{\rm ctrl}
+H_{\rm msg}
+H_A^{\rm loc}
+H_B^{\rm loc}
+H_{AB}^{\rm shared}
+H_\ell
+H_{\rm clk}
+\epsilon H_{\rm leak}
```

という一つのHamiltonianとして整理する。$H_{\rm clk}$ は互いに重ならない結合窓を自律的に進行させ、$\epsilon H_{\rm leak}$ は長時間で外部との微小なエネルギー交換を許す項である。有限の測定窓では $\epsilon=0$ の閉鎖系を基準とする。

局所部分は

```math
H_X^{\rm loc}
=
H_X^{\rm sys}
+H_{X,L}
+H_{X,I}
+H_{X-L},
\qquad X=A,B
```

と分ける。局所浴 $\mathcal B_X^{\rm loc}=\mathcal B_{X,L}\oplus\mathcal B_{X,I}$ のうち、$L$ sectorは局所記録とbright transientの分散、$I$ sectorは記録とmessengerの正準な写しを共通未来へ渡すinterfaceを担う。$t<t_C$ では左右の局所部分を分離し、$t\ge t_C$ でinterface modeだけを共有sector $\mathcal B_{AB}^{\rm shared}$ に結合する。したがって共有浴は、記録形成前に左右へ共通ノイズを与える浴ではない。

従来 $H_{\rm cmp}$ と $H_{\rm mix}$ に分けていた後段の操作は、$H_{AB}^{\rm shared}$ 内の静的な2入力・2出力junctionとして数える。このjunctionは共通の $U(1)$ actionを保存し、浴の二つのinterface vectorを正準な和・差modeへ組み替える。

```math
I_-=\frac14\|u_A-u_B\|^2,
\qquad
I_+=\frac14\|u_A+u_B\|^2.
```

左右の基準作用が等しいとき、

```math
I_-^{AB}
=
I_0\left[1-ABV\cos\Delta_{ab}\right],
\qquad
I_+^{AB}
=
I_0\left[1+ABV\cos\Delta_{ab}\right],
```

```math
I_++I_-=2I_0
```

が成り立つ。差modeが不一致量を表し、和modeと残りのbath modeが比較のためのreservoirを構成する。この意味で比較器は独立した外付け装置ではなく、共通未来の浴をreaction coordinateとdark modeへ分解したものとして実装できる。

soft energyを $h$、未読のreturn-reservoir energyを $e_R\ge0$ とし、境界sectorの固定作用殻を

```math
e_R+h+\kappa I_+
=
E_*+2\kappa I_0
```

と取る。上の恒等式から

```math
e_R
=
E_*+\kappa I_- -h
```

であり、bath energyの非負性だけで

```math
h\le E_*+\kappa I_-
```

を得る。これは旧模型でreturn comparatorへ明示的に書き込んでいたterminal compatibilityと同じ支持条件である。比較演算は、浴modeの正準変換、全作用の保存、reservoir energyの非負性でまかなわれる。

ここで厳密なのは、和・差modeへの正準変換、$I_++I_-=2I_0$、固定殻から上の支持条件が出る代数である。一方、一般の有限浴が境界microcanonical測度 $[M_\partial]$ を動力学的に準備すること、$\epsilon H_{\rm leak}$ がその測度を一意に選ぶこと、局所測定から境界準備までの全結合を一本の明示式で完成することは未導出事項である。したがって、この整理は独立比較器を浴へ吸収する重要なHamiltonian構成案だが、$[R]$ の完全な力学的除去を証明するものではない。

#### 8.2 比較器と二モード台帳

左右の記録を共通未来で比較する実2次元比較器について、

```math
I_-^{AB}
=\frac14\|u_A-u_B\|^2
=I_0\left[
1-ABV\cos\Delta_{ab}
\right]
```

とする。$A,B\in\{-1,+1\}$、$0\le V\le1$ である。cos依存はNelson極限から自動的に出るものではなく、この差動比較器の幾何に含まれる。

軟モードと台帳モードの作用を $J_s,J_0$ とし、

```math
J_s+J_0=\frac{E_\ell}{\omega_\ell}
```

という固定総作用殻上でLiouville測度を取ると、軟モードエネルギー $h=\omega_\ell J_s$ は $[0,E_\ell]$ 上で一様になる。結果領域の基準質量 $w_{AB}=1/4$ は、Hamiltonianの形ではなく対称な準備測度から従う。

旧境界原理 $[R]$ では、設定と結果を明示的な引数に持たない終端条件が

```math
h\le E_*+\kappa I_-^{AB}
```

と等価になる。全結果領域でしきい値が台帳の適用範囲内にあるとき、適合体積は

```math
W_{AB}
=\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa I_0
\left(1-ABV\cos\Delta_{ab}\right)
\right]
```

となる。対称準備で規格化すると、

```math
P(A,B\mid a,b)
=\frac14
\left[
1-ABV_{\mathrm{eff}}\cos\Delta_{ab}
\right],
```

```math
V_{\mathrm{eff}}
=\frac{\kappa I_0}{E_*+\kappa I_0}\,V
```

を得る。

#### 8.3 最新の固定作用殻候補

後発の候補では、終端フィルター $[R]$ を独立に置く代わりに、軟モード作用 $J_s$、帰還作用 $J_r$、比較器の差動作用 $\widetilde I_-$ から

```math
Q
=\omega_\ell(J_s+J_r)-\kappa\widetilde I_-
```

という保存量を構成し、固定作用殻 $Q=E_*$ 上の境界Liouville測度を $[M_\partial]$ とする。この殻の境界体積が $E_*+\kappa I_-^{AB}$ に線形なら、旧 $[R]$ と同じBell型共同確率を再現する。

これは最新版の主候補である。ただし、固定殻の準備自体が設定依存の境界条件なら、$[R]$ を力学的に導いたのではなく、境界測度として再表現しただけになる。$[M_\partial]$ が因子化された初期集団と順方向Hamiltonian流だけから得られることは未導出事項である。

### 9. Bell前提と模型の未決着点

完全な微視状態を $\lambda$ とすれば、固定した $\lambda$ における左右の局所応答は局所的に因子化できる。一方、境界条件づけ後の集団は

```math
\rho(A,B,h\mid a,b)
=\frac{1}{4(E_*+\kappa I_0)}
\mathbf 1_{
0\le h\le
E_*+\kappa I_0[1-ABV\cos\Delta_{ab}]
}
```

のように設定 $a,b$ に依存する。したがって、この模型で外れるBell前提は測定設定独立性である。

対称準備では

```math
P(A\mid a,b)=P(B\mid a,b)=\frac12,
\qquad
E(a,b)=-V_{\mathrm{eff}}\cos\Delta_{ab}
```

となり、規格化因子も設定に依存しないため非信号性を保つ。CHSH値の最大は

```math
S_{\max}=2\sqrt2\,V_{\mathrm{eff}}
```

であり、$V_{\mathrm{eff}}>1/\sqrt2$ ならBell不等式を破る。

次は未導出事項である。

- $[M_\partial]$ が旧 $[R]$ を真に除去し、単なる言い換えではないこと。
- 偏った準備を含む任意の初期集団に対する非信号性。
- cos比較器とTsirelson限界が、他の正の比較器から一意に選ばれること。
- 相補的な内部時計だけから物理的履歴測度が選ばれること。
- Nelsonの二側測度、測定の選択法則、Bellの境界測度を単一原理から導くこと。
- 一般の局所測定過程と境界測度の準備まで含め、全構成を単一の有限自律Hamiltonianとして完成すること。

現段階では、Nelson部分には有限線形Gaussian系の $C^1$ 収束定理、測定部分には追加選択法則の下での収束定理、Bell部分には $[M_\partial]$ を最新版候補として採用する。旧 $[R]$ は、Bell共同確率が厳密に得られる比較対象として残す。

## 参照したプロジェクト情報源

- `nelson_reset_bell_final_revision.md`
- `closed_hamiltonian_bell_measurement_latex.pdf`
- `nelson_boundary_bell_complementary_clock_revision.tex`
- $[Q]$ および $[M_\partial]$ の固定作用殻案を扱うプロジェクト内記事
