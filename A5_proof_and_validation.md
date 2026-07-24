@number: 1
@chapter: 第1章
@title: 問題設定、中心定理、適用範囲
@status: [D] Bell 前提と物理的仮定を固定。[F|R|E|P] 中心定理の正確な主張。

## 1.1 Bell 定理に対する立場

Bell の定理と CHSH 不等式は、その仮定の下で正しい [1,2]。局所 hidden-variable 表現

$$
P(A,B\mid a,b)
=
\int d\lambda\,
\rho(\lambda)
P(A\mid a,\lambda)
P(B\mid b,\lambda)
$$

において、同一の設定非依存分布 $\rho(\lambda)$ を四設定対に用いるなら、CHSH 量

$$
\mathcal S
=
E(a_0,b_0)
+E(a_0,b_1)
+E(a_1,b_0)
-E(a_1,b_1)
$$

は

$$
|\mathcal S|\leq2
$$

を満たす。本論文はこの定理を否定しない。

本論文の問いは、測定装置を外部の瞬間的 operation とせず、setting controller、analyzer、pointer、messenger、return device を含む閉じた Hamilton 系として追跡したとき、Bell の仮定のどこが失われるか、というものである。結論は、各履歴の局所応答ではなく、その履歴へ与える二側条件付き measure に measurement independence failure が現れる、というものである。

## 1.2 一試行の古典 ontology

全 phase space を $\Gamma$ とし、初期時刻 $t_i$ の一点を $z_i\in\Gamma$ とする。同じ Hamiltonian function $H_{\mathrm{tot}}$ が全 trial に用いられ、設定は phase space 内の controller sector によって

$$
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
$$

と決まる。一つの $z_i$ は一つの Hamilton 軌道

$$
z(t)=\Phi^t(z_i)
$$

を与える。

局所 pointer の二つの disjoint macroregion を $\Gamma_A^+$、$\Gamma_A^-$ とし、B 側も同様に定める。記録時刻 $t_A,t_B$ に

$$
A(z_i)=
\begin{cases}
+1,&z(t_A)\in\Gamma_A^+,\\
-1,&z(t_A)\in\Gamma_A^-,
\end{cases}
$$

と定義する。各履歴の outcome は一意であり、独立の stochastic collapse または selection trajectory を必要としない。確率は異なる definite histories に与えられた measure から生じる。

## 1.3 四つの明示仮定

本論文では仮定を次の四つに分ける。

### [H] 有限 Hamiltonian 仮定

source、局所装置、clock、return sector を含む全系は有限個の canonical pair と滑らかな Hamiltonian で記述される。理想 pulse 表現は有限時間の Hamilton flow として自律化できる。

### [R] 二側 return 測度

基準初期密度 $\rho_i(z_i)$ と固定 terminal function $G_R(z_T)\geq0$ に対し、物理的履歴測度を

$$
d\mu_R^{a,b}(z_i)
=
\frac{
\rho_i(z_i)
G_R[\Phi_{a,b}^{T}(z_i)]
}{Z_{a,b}},dz_i
$$

とする。$G_R$ は setting label、outcome label、目標 cosine を引数に持たない。この `[R]` は Hamilton 方程式からの帰結ではなく、物理的 ensemble を指定する境界原理である。

### [E] equilibrium preparation

基準 ensemble における四つの outcome-seed sector は等体積である。より一般には、同時 sign flip

$$
(A,B)\longmapsto(-A,-B)
$$

に対する preparation symmetry を要求する。第6章で、この条件を外すと no-signalling が一般には保証されないことを示す。

### [P] phase-locked source

二つの messenger pair は等しい action と共通 phase を持つ source macrostate から出る。相対 phase noise を許す場合は第一 circular moment を visibility に含める。作用積分を canonical phase へ記録する有限 Hamiltonian register は付録Bで構成する。

## 1.4 中心定理

\begin{theorem}[有限 Hamiltonian Bell realization]
仮定 `[H]`、`[R]`、`[E]`、`[P]` の下で、setting controller、局所 outcome seed、局所 pointer、二つの canonical messenger、soft return mode、common-future comparator、autonomous clock からなる有限 Hamiltonian が存在し、その二側条件付き共同確率は

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV\cos\{\phi(a)-\phi(b)+\Phi_0\}
\right]
$$

となる。各履歴の局所応答は deterministic に因子化するが、Bell-complete microscopic distribution は一般に

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda)
$$

である。$0\leq V\leq1$ なら共同確率は非負であり、equilibrium preparation の全 outcome 周辺は $1/2$、最大 CHSH 値は $2\sqrt2V$ である。
\end{theorem}

定理の Hamiltonian は第4章、phase-volume 計算は第5章、Bell 前提監査は第6章に与える。この定理は `[R]` および `[E]` の物理的必然性を主張しない。

## 1.5 導出の主鎖

導出は次の順序で進む。

1. 基準 ensemble では source と setting controller を独立に準備する。
2. 局所 analyzer が setting と outcome sign を messenger phase に書き込む。
3. 局所 pointer が $A,B$ を記録する。
4. 二つの messenger が局所記録後の共通未来で比較される。
5. comparator が antisymmetric action と soft-mode energy の差を return pointer に記録する。
6. setting-independent terminal condition を全履歴へ課す。
7. terminal condition の Hamiltonian pullback が source-level measure を設定依存にする。
8. harmonic soft-mode の Liouville volume が antisymmetric action に線形なので cosine law が得られる。

この順序は、目標確率を terminal weight に書き込む循環構成を排除するためにも重要である。

## 1.6 何を主張しないか

本論文は次を主張しない。

- Bell の全仮定を保った古典模型による Bell 違反。
- quantum theory の内部機構または wave-function collapse の説明。
- 非可逆項や decoherence による outcome selection。
- 有限再帰または時間反転対称性から `[R]` が一意に従うこと。
- 任意の preparation における no-signalling。
- return geometry が自然界で一意に選ばれること。
- 本模型が measurement-dependent model の情報量について最適であること。

従って本論文の成果は、完全理論の主張ではなく、明示的かつ反証可能な constructive existence theorem である。

## 1.7 postselection との区別

実験終了後に観測者が一部の trial を捨てる通常の postselection では、採否と設定・結果の相関を操作的に検査できる。本論文の `[R]` は、観測された trial 列の部分集合を選ぶ規則ではなく、最初から物理的に実現する全履歴 ensemble を定める境界条件として置かれる。

しかし数式だけを見れば両者は同じ条件付き確率に見える。このため模型が経験的説明になるには、terminal apparatus が各 trial の観測後にデータを捨てていないこと、設定ごとに異なる acceptance window を使っていないこと、全 outcome が確率の規格化に含まれることを独立に示さなければならない。この監査を第7章で行う。

## 1.8 論文の構成

第2章では本論文の各構成要素に対する先行研究を整理し、新規性の範囲を限定する。第3章では二側測度と measurement independence の関係を一般の有限 Hamilton flow に対して証明する。第4章と第5章が本論文の構成的中核である。第6章では Bell 分類と preparability を調べ、第7章では物理的解釈と未解決点をまとめる。

## 1.9 本章の結論

本模型の Bell 違反は、局所 Hamiltonian trajectory の非局所性または確率的 collapse から生じない。固定 terminal condition を設定依存 Hamilton flow で pullback したとき、source hypersurface 上の microscopic measure が設定依存になることから生じる。以下ではこの主張を抽象的説明に留めず、一つの有限 Hamiltonian として実現する。
