# R164作用殻状態数結果の退役記録

## 位置づけ

R164はdraft-49で導入した、単一試行signalの結果成分作用から排他的2作用殻のLiouville状態数を数え、Born型の線形重みを得る結果である。後にQ1/Q2の静的測定経路とQ3開始配置の統計力学的説明へ使った。

Q1/Q2の結果形成はM65/R204へ、Q3の位置重み・initial preparation・tracer輸送はM64/R203A--R203Dへ置換された。draft-123で旧Q3 rate-latchも退役し、R164を直接参照するfixed-goal因果鎖がなくなったため、draft-124でactive paperから退役する。

退役は状態数計算の反証を意味しない。結果番号R164は再利用しない。

## 旧主張の核

非零signal $v$ と排他的結果成分 $i$ に対し、

```math
J_i(v)
=
\mathcal J_0 |(\Psi v)_i|^2,
\qquad
A_i^\delta(v)
=
J_i(v)+\delta q_iJ_{\rm sig}(v)
```

と置く。各結果成分に2つの非負作用を持つ排他的作用殻を置き、同じLiouville基準分布で数えると

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}A_i^\delta(v)
```

となり、

```math
\frac{\Omega_i^\delta}
{\sum_j\Omega_j^\delta}
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}
{1+\delta}.
```

一般に各結果成分が $q$ 個の独立な作用分配方向を持つと $\Omega_i\propto(A_i^\delta)^q$ となり、全容量族で線形則を保つのは $q=1$ に限る、という剛性も旧付録Lで扱った。

## 現行置換

Q1/Q2では保持済み二射影作用をM65の3状態open selectorへ直接入力する。Q3ではM64/R203Aがregularized density/currentを、R203B/R203Dがinitial preparationを、R203C/R203Dがtracer輸送を担う。したがって作用殻状態数を中間の確率源として置く必要がない。

現行Q3で使う

```math
R_i^\delta=|Z_i|^2+\delta q_iS,
\qquad
\pi_i^\delta=\frac{R_i^\delta}{(1+\delta)S}
```

はM64/R203のregularized signal densityとして定義し、作用殻のLiouville状態数を物理的に追加しない。

## 履歴

- 初出: draft-49
- 主定理追加: commit `ce33c7e1722011261d87018790cf81893af03852`
- draft-49 merge: commit `df8342f79ab00764db3436647256f1d3845513cf`
- active paper退役直前: commit `951740f1af8fcb38fc37337dc2748b560d8544b1`
- 旧定理本文: 退役直前の `sections/02_common_canonical_modules.md`
- 完全証明・剛性・有限幅評価: 退役直前の `sections/A12_common_action_shell_state_count.md`

完全な旧証明はGit履歴を正本とし、このメモへ複製しない。
