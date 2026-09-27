# 旧M65 fixed-hub physical lift（R204B/R204C）

draft-140でM65の正本を3状態往復Markov pointerからtwo-result first-passage selectorへ簡素化したため、旧R204B/R204Cのfixed-hub physical liftをactive paperから退役した。

この退役は数式の反証ではない。R204Bのmatched capacity--conductance恒等式とR204Cの有限時間generator比較は、旧

```text
+ <-> H <-> -
```

という3状態M65を物理化するためのstrengtheningだった。現行M65では第三の安定pointer状態を置かず、未決定はfirst event前のsurvival conditionとして扱うため、旧fixed-hub liftは現行正本の推奨physical realizationではなくなった。

結果ID R204B/R204Cは履歴追跡のため再利用しない。R205Dのfixed-hub capacity--conductance数学はM66側の一般結果として残るが、現行M65のphysical liftとは扱わない。現行M65のfinite-Hamiltonian liftはdraft-141のM67/R211A--R211C double-well経路で別に構成し、R204E contractへ接続する。

## 最終active内容

## Z.4 R204B：fixed-hub phase-volume実現候補

R204Aはopen lawそのものを正本とする。この節は同じlawを受動phase-volume構造から作る追加実現候補であり、M65の定義には使わない。

固定された左右chamber $C_\pm$、neck $N_\pm$、hub $H$ を取り、局所phase-volume factorを概念的に

```math
\Phi_A(Q)
=
\begin{cases}
a_+\phi_C(Q),&Q\in C_+,\\
a_+\phi_N(Q),&Q\in N_+,\\
\phi_H(Q),&Q\in H,\\
a_-\phi_N(Q),&Q\in N_-,\\
a_-\phi_C(Q),&Q\in C_-,
\end{cases}
```

とする。hubのphase volumeは作用に依存させない。

R203Bと同じ調和自由度のcanonical積分を使えば、局所Gibbs容量はphase-volume factorへ比例する。左右共通の基準量 $V_C^0,G_0,V_H^0>0$ に対して

```math
V_r=a_rV_C^0,
\qquad
G_r=a_rG_0,
\qquad
V_H=V_H^0
```

を得る場合、

```math
\frac{G_r}{V_r}
=
\frac{G_0}{V_C^0}
=:\Lambda,
\qquad
\frac{G_r}{V_H}
=
\frac{G_0}{V_H^0}a_r
=:\kappa a_r.
```

<!-- theorem-start:theorem -->
**定理（R204B：fixed-hub matched capacity--conductance realization）**

上記capacity/conductance relationsを満たすwell-mixed chamber reductionでは、左右chamberとhubのcoarse generatorはR204Aのcanonical open generatorと一致する。従ってphase-volume構造は、Born比を外部計算せずR204Aを実装する一つの物理候補を与える。
<!-- theorem-end:theorem -->

R204BはM65正本の必須依存ではない。capacity--conductance部分は付録XのM66/R205Dでbinary fixed-hub specializationとしてcommon parentへ埋め込む。

## Z.5 R204C：Hamiltonian--Brownian lift strengthening

R204Bの固定幾何を明示Hamiltonian、有限帯域bath、Brownian/Smoluchowski過程から導く場合だけこの結果を使う。対象時間窓 $0\leq t\leq T$ で、

```math
\varepsilon_{\rm bath},
\quad
\varepsilon_{\rm od},
\quad
\varepsilon_{\rm pv},
\quad
\varepsilon_{\rm tube},
\quad
\varepsilon_{\rm lump},
\quad
\varepsilon_{\rm cal}
```

を、それぞれbath、overdamped、phase-volume tracking、tube reduction、well-mixed lumping、capacity/conductance較正の誤差とする。

```math
\varepsilon_{\rm gen}
=
\varepsilon_{\rm bath}
+\varepsilon_{\rm od}
+\varepsilon_{\rm pv}
+\varepsilon_{\rm tube}
+\varepsilon_{\rm lump}
+\varepsilon_{\rm cal}.
```

<!-- theorem-start:theorem -->
**定理（R204C：Hamiltonian--Brownian liftの有限時間誤差）**

具体実装のcoarse lawを $\widetilde\nu_t$、R204Aのcanonical lawを $\nu_t$ とする。初期lumping誤差を $\varepsilon_{\rm init}$ とし、対象時間窓でgenerator差の全変動作用normが一様に $\varepsilon_{\rm gen}$ 以下なら、

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
(
\widetilde\nu_t,\nu_t
)
\leq
\varepsilon_{\rm init}
+
T\varepsilon_{\rm gen}
=:
\varepsilon_{204C}(T).
```

これはR204AのHamiltonian/Brownian実現を評価する強化結果であり、R204A/R204D/R204E/R204Fの成立条件ではない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204C）**

Markov半群の全変動縮約性とDuhamel展開を使い、generator差を時間積分する。証明終。
<!-- theorem-end:proof -->


## 旧candidate verifier

draft-140で次のM65専用candidate checksを `notes/retired_verifiers/` へ移した。

- `verify_m65_phase_volume_partition.py`
- `verify_m65_matched_conductance.py`
- `verify_m65_brownian_reduction.py`

phase-volume identity自体はM66/R205側のrequired verifierで現行検算を続ける。fixed-hub matched conductanceとthree-state Brownian reductionは旧R204B/R204Cの履歴検算としてのみ保存する。
