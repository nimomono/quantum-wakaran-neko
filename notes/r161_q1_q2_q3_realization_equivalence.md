# R161を介したQ1--Q2--Q3実現同値の整理

## 1. 位置づけ

このメモは、Q1型局所自由度を空間に並べQ2型2体系相互作用を加える参照模型と、Q3の具体的な粒子・浴模型を、どの意味で「同じ」とみなすかを整理する。draft-112以後、論文正本のQ3物理実現はM37/R86 signalとM64三実体open modelとし、R161より後段の数学核は従来通り共通に保つ。M60/M61は旧Hamiltonian実現としてGit履歴に保存する。

現行Q3の数学的正本は

```text
signal dynamics
      ↓
   (π, j, t)
      ↓ R161
     k±
      ↓ R161 canonical path law
finite-state Markov path
      ↘ R162
optional Poisson realization
      ↓ R185
Nelson / time-symmetric Newton
```

である。R161より前段だけをミクロ実現依存とし、R162は基礎的実体でなくR161 lawのoptional stochastic referenceとして使う。

## 2. Q1/Q2から得る空間入力

各空間頂点にQ1型の局所実正準モードを置き、$R_i=|Z_i|^2$ とする。独立な局所モード列だけでは辺流がなく、空間伝播は生じない。

隣接頂点へQ2で用いるのと同じ有限2体系エルミート結合族を反復すると

```math
i\mathcal J_0\dot Z=hZ
```

となり、辺流

```math
J_{i\to j}
=\frac{2}{\mathcal J_0}
\operatorname{Im}(Z_j^*h_{ji}Z_i)
```

を得る。$S=\sum_iR_i$ が保存される区間では

```math
\pi_i=\frac{R_i}{S},
\qquad
j_{ij}=\frac{J_{i\to j}}{S},
\qquad
\dot\pi_i=\sum_jj_{ji}.
```

従ってQ1型局所作用が $\pi$、Q2型相互作用が空間伝播と反対称流 $j$ を供給する。ただし対称活動量 $t$ はこの代数だけから一意に決まらない。

## 3. 空間化Q1模型の役割

Q1のBorn型選択機構を各辺へ置き、Q2型の反対称流を局所的に重ねる模型は、適切な $(\pi,j,t)$ を作ればR161と同じ位置生成子を与える。これはQ1/Q2からQ3数学へ接続できることを露出した **参照実現** として有用である。

一方、この模型のpointer列やone-hot tokenを自然界の基礎的実体として採用する必要はない。現行物理実装はM37型coherent signal、一つのclassical tracer、一つのsignal-driven thermal reservoirからなるM64である。

## 4. R161実現同値

同じ信号履歴と同じ初期粒子位置分布に対し、2つの模型 $M_A,M_B$ が同じ $\pi_i(t)$ と同じ有向率 $k_{i\to j}(t)$ を与えるなら、R161実現として厳密同値とする。内部自由度、bath、pointer、粒子の具体的な担体が同じであることは要求しない。

固定有限時間 $T$ で

```math
\varepsilon_{\rm gen}
=\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}
|k^A_{i\to j}-k^B_{i\to j}|
```

なら

```math
\sup_{0\leq t\leq T}
D_{\rm TV}(p_t^A,p_t^B)
\leq T\varepsilon_{\rm gen}.
```

従って近似ミクロ模型も、生成子誤差を制御すれば同じR161/R162/R185下流へ接続できる。M64/R203Dはcontinuous profileとfinite-graph profileをこのinterfaceへ接続する。

## 5. 物理実現の比較規約

- M64 three-entity open model：現行Q3物理実現。M37 signalから $(\rho,j)$ を取り、signal-driven thermal reservoirのphase volumeとmean flowを介してcontinuous tracer diffusionを作る。finite graphではlocal $R_i^\delta,J_{ij},T_{ij}^\delta$ からR161 rateを直接構成する。
- M60/M61：旧Hamiltonian実現。Duffing shell、chiral-medium、ballistic lead、single-Hamiltonian parentを用いたより複雑な経路であり、draft-112で現行正本から退役した。反証扱いせずGit履歴へ保存する。
- R162 open Poisson jump：R161 lawのoptional stochastic reference。基礎的なQ3存在論とは扱わない。
- 空間化Q1＋Q2相互作用：Q1/Q2からR161へ到達できることを示す数学的参照実現。
- M56：spin-only実現を狙う代替研究線。現行Q3達成根拠には使わない。
- その他の粒子・浴模型：同じ $(\pi,j,t)$ または同じ有向率を導けるかで比較する。

今後のミクロ模型では、Nelson縮約全体を毎回導き直すのでなく、まず

```text
micro model -> (π, j, t) -> R161
```

を証明する。ここが閉じればR162/R185は共通結果を再利用する。

## 6. 非主張

- Q1型モードを空間に並べるだけでQ3が自動的に得られるとは主張しない。Q2型の辺結合が必要である。
- Q1/Q2のR191測定pointerをQ3粒子と同一視しない。
- $(\pi,j)$ だけから対称活動量 $t$ が一意に決まるとは主張しない。
- 異なるミクロ模型が同じ生成子を持つことから、それらの存在論や熱力学的資源まで同じとは結論しない。
- M64のcontinuous-space一様極限、多粒子、finite-bandwidth/Hamiltonian lift、全周期のsource--clock--record統合は別の強化課題である。
