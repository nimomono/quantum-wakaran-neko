@number: 2
@chapter: 第2章
@title: 先行研究との関係と本論文の新規性
@status: [K] 既知の Bell、measurement dependence、時間対称境界、古典 Hamiltonian measurement を整理。

## 2.1 measurement independence を緩めた Bell 模型

Bell--CHSH 導出に measurement independence が必要であること、およびそれを緩めれば局所 deterministic response と singlet correlation を両立できることは既知である。Brans は fully causal hidden-variable model を、Hall は singlet 相関を再現する局所 deterministic model を明示した [3,4]。従って

$$
P(A,B\mid a,b)
=
\frac14
\left[
1-AB\cos(a-b)
\right]
$$

という式を measurement-dependent distribution で再現すること自体は、本論文の新規性ではない。

Hall と Branciard は、hidden variable と setting の相互情報を用いて measurement dependence の cost を定量化し、causal、retrocausal、one-sided、superdeterministic model を比較した [5]。本論文も Bell 違反の報告だけでなく、二設定対間の全変動距離および設定 prior を指定した相互情報を報告対象とする。ここでの目的は cost の最適化ではなく、依存性を生む物理的 Hamilton operation を同定することである。

## 2.2 時間対称境界と future-input dependence

Wharton は量子基礎論における time-symmetric boundary condition を論じ、後には global constraint を持つ classical field model を具体化した [6,9]。Leifer と Pusey は operational time symmetry と retrocausality の関係を定理的に分析した [7]。Wharton と Argaman は Bell の前提を spacetime-local model の観点から整理し、future-input dependence を持つ locally mediated model を分類した [8]。

Schulman の special-state approach は、終端条件または稀な microscopic histories を用いて測定相関を説明する代表的な先行模型である [10]。したがって future boundary を用いること、または all-at-once に履歴を解くことも、それ自体は新規ではない。

本論文の `[R]` はこの系譜に属する。ただし、未知の過去変数へ設定依存分布を直接割り当てる代わりに、設定を物理的 controller state として Hamiltonian に入れ、固定 terminal macroregion の逆像を有限 flow で計算する点を構成上の焦点とする。

## 2.3 no-signalling、symmetry、fine-tuning

Wood と Spekkens は、Bell violation を causal model で説明しつつ no-signalling を保つには、causal parameter の fine-tuning が必要になることを指摘した [11]。Almada らは explicit retrocausal model を調べ、no-signalling が outcome-reflection symmetry により保護され得ることを示した [12]。

本論文でも no-signalling は

$$
W_{++}=W_{--},
\qquad
W_{+-}=W_{-+}
$$

という sign symmetry に依存する。この symmetry は joint law の周辺化を保護するが、任意の preparation における no-signalling を自動的に保証しない。

Bacciagaluppi、Hermens、Leegwater は measurement-dependent model において、特定の hidden-variable subensemble が準備可能なら signalling-in-principle が現れ得ることを示し、measurement independence を使わない拡張 Bell theorem の条件を論じた [13]。この結果は本模型に直接関係する。第6章では outcome-biased seed sector を準備した場合の signalling 例を明示し、equilibrium preparation `[E]` を独立な物理的条件として扱う。

## 2.4 古典 Hamiltonian measurement

物体と測定器を一つの Hamiltonian 系として扱い、system--apparatus coupling と Bayesian update を解析することにも先行研究がある。Theurel は有限温度 apparatus を含む古典 Hamiltonian measurement を構成し、測定精度と disturbance の関係を調べた [14]。従って classical pointer coupling 自体を量子論特有のものと見なす理由はない。

本論文の pointer は Theurel の measurement-quality 問題とは異なる役割を持つ。各履歴に definite sign を記録し、その sign と setting phase を common-future return sector へ運ぶ最小 canonical device である。本論文では非可逆増幅、decoherence、有限温度精度限界を扱わない。これらは現実的 apparatus の追加層になり得るが、measurement independence failure と cosine law の生成原因ではない。

## 2.5 自律 Hamiltonian と内部 clock

時間依存 Hamiltonian を extended phase space で自律系へ持ち上げる方法は標準的であり、Struckmeier は symplectic extended phase-space formalism を詳細に整理している [15]。有限 rotor を内部 clock と work reservoir に用いる具体的構成も autonomous engine の文脈で研究されている [16]。

本論文では、局所 analyzer と comparator の操作順を最初に pulse Hamiltonian として明示し、最後に clock pair $(\vartheta,J_c)$ を加えて

$$
H_{\rm aut}
=
\Omega J_c+H_{\rm sched}(\vartheta)
$$

とする。これは有限自由度の存在証明として用いる。clock backreaction、有限 pulse overlap、通常の正定値 kinetic term による正則化は付録Dで区別する。

## 2.6 有限 bath と Nelson 構造

調和 bath の厳密消去、generalized Langevin equation、射影法は Ford--Kac--Mazur、Zwanzig、Mori 以来の既知構造である [17--19]。Nelson、Yasue、Zambrini の stochastic mechanics は、実確率作用と Schrödinger 形の関係を与える [20--22]。局所 Madelung--Nelson 方程式から大域量子化条件が自動的に従わない問題は Wallstrom により指摘されている [23]。

旧稿はこれらを詳細に再導出していた。しかし本論文の Bell theorem は、OU/Nelson 極限の全証明を必要としない。必要なのは source が二つの phase-locked canonical messenger を準備できることである。この最小条件を本文 `[P]` とし、有限 Hamilton action を canonical phase へ記録する register と既存 bath への接続だけを付録Bに残す。

## 2.7 新規性の限定

本論文が新規性として主張しないものは次である。

- Bell theorem と CHSH 判定 [1,2]。
- measurement independence relaxation による singlet simulation [3--5]。
- time-symmetric または retrocausal boundary ontology [6--10]。
- symmetry-protected no-signalling の一般的考え [11,12]。
- classical Hamiltonian apparatus [14]。
- extended phase-space autonomization [15,16]。
- harmonic bath reduction と Nelson stochastic mechanics [17--23]。

今回確認した先行研究の範囲で、本論文の独自な組合せは次である。

1. setting を external parameter でなく finite controller coordinate とする。
2. outcome、setting、cosine を参照しない単一の terminal rule を用いる。
3. 局所 Hamiltonian pointer record を common-future messenger と分けて保持する。
4. antisymmetric canonical action を physical comparator で soft energy と比較する。
5. 通常の正の Liouville volume から joint cosine law を得る。
6. measurement independence failure がどの Hamilton operation と boundary conditioning の合成で生じるかを明示する。
7. equilibrium no-signalling と biased-subensemble signalling を同じ模型内で監査する。

従って適切な表現は「古典力学が Bell の定理を破る」ではなく、「二側 boundary measure の下で measurement-dependent Bell correlation を実現する有限 Hamiltonian existence theorem」である。
