# R208B/R208C/R209C Q3 continuous phase-volume bridgeの退役記録

## 位置づけ

R208B、R208C、R209Cはdraft-137--139で、M67の旧continuous phase-volume tracerをM64/R203へ接続するために導入した結果である。

draft-144でR214A--R214Bの三次元伸縮Brownian dumbbell profileを追加し、draft-145でR214A/BをQ3-2 continuous-tracerのrequired主線へ昇格した。同時にR209Aをgeneric flow lemma、R209Bをgeneric finite-bath/FDT lemma、R210Aをgeneric coherent-load theoremへ一般化し、R214B自身へsmall-mass $W_1$ bridgeを取り込んだ。

このためdraft-146で旧3結果をactive paperから退役する。退役は旧数式を反証したことを意味しない。結果ID R208B、R208C、R209Cは再利用しない。

## 旧責務と置換先

| 結果 | 旧責務 | 現行の置換先 |
|---|---|---|
| R208B | inverse-designed $H_\rho$ のphase-volume Jacobianからosmotic mean forceを作り、$N_\rho^{-1/2}$ fluctuationと $O(N_0^{-1})$ signal backreactionを評価 | continuous Q3ではR214Aのdumbbell partition/osmotic forceとR214Bのfinite-time fluctuation/load評価へ置換。一般phase-volume数学はR212A、M64 open/effective identityはR203Bへ残る |
| R208C | local tight-frame moving finite bathからrelative GLE/FDTとMarkov dragを導出 | profile-independentなR209B generic finite harmonic bath / Markov--FDT lemmaへ吸収 |
| R209C | finite-bath Markov化後のunderdamped tracerからM64 overdamped processへのsmall-mass $W_1$ compatibility | $Y=X+(M_X/\gamma_X)V$ couplingをR214Bへ直接取り込み、dumbbell固有drift・single-dumbbell fluctuationと同じ誤差台帳で閉じる |

## 現行Q3因果鎖

continuous Q3-2は

```text
M67 / R208A
  -> R214A / R214B
       uses R209A generic flow
       uses R209B generic finite bath/FDT
       uses R210A generic coherent-load bound
  -> M64 / R203C
  -> R161 / R185
```

とする。

finite-graph Q3-4A/Q3-4B/Q3-5はR214を要求せず、

```text
M67 finite-graph profile
  -> R212A phase-volume/mean-flow specialization
  -> R208D profile dispatch
  -> M64 / R203D
  -> R161 + R124/R182/R125
```

へ分離する。

## 退役する検算・supporting evidence

active required treeから次を外す。

- `tools/verify_r208_phase_volume_backreaction.py`
- `tools/verify_r208_local_moving_bath.py`
- `tools/verify_r209c_process_compatibility.py`
- `simulations/m67/run_full_compatibility_witness.py`

旧コードはnotesへ複製せずGit履歴を正本とする。現行required checksはR214A/B、R209A/B、R210A、R208D/R203Dの責務へ分割する。

## 履歴

- R208B/R208C初出: draft-137
- R209C初出: draft-138
- M67 Q3 parent昇格: draft-139
- R214 candidate追加: draft-144
- R214 required主線昇格: draft-145 / PR #191
- 退役直前active版: merge commit `59f05fac977b198998472074fb96c0edfa10a9cb`
- 完全な旧定理・証明・verifier・full compatibility witness: 上記commit以前のGit履歴

