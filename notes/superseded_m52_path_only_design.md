# M52経路限定設計の退役記録

## 1　由来

draft-63のM52は、共同状態容量を4mode registerでなく、同じ試行に共存する有限個のcoherent経路だけへ担わせた。R175は経路和

$$
D_\Gamma=\sum_r\gamma_ra_rb_r^{\mathsf T}
$$

の局所共変性、CNOT展開、参照系安定性、理想逆演算、非分離性を有限代数として示した。旧R176は、一般入力lift、有限Hamiltonian分岐・再結合、末端coherent decoderを閉じる未解決予想だった。

## 2　改訂理由

共同状態に4つの自由度が実在しても、外部controllerがそれらを個別に扱わず、余計な自由度をbathへ受動的に任せられるなら固定目標と矛盾しない。経路限定設計は、この許容される場合まで排除していた。

改訂後はmode数でなく外部interfaceを判定する。許されるのは、入力非依存の有限Hamiltonian規則が内部mode、anti-register、work、clock履歴を自律的に作り、同じ試行の状態をgate間で保持する構成である。許されないのは、内部modeごとの個別初期化、設定、較正、同期、address、読出し、reset、入力別係数表、回路別配線、中間decode、集団momentからの再準備である。

## 3　現行系列への対応

| draft-63の要素 | draft-64以後の扱い |
|---|---|
| 共同状態は経路だけが担う | 撤回。受動的な有限modeをbath自由度として許す |
| R175の経路和代数 | R176Bのunitary作用に対する診断展開へ吸収。結果IDは現行主結果鎖から退役 |
| 一般入力lift | R176Aの可逆tensor-liftで明示構成 |
| Hamiltonian CNOT | R176Bの差mode二次生成子で明示構成 |
| gate間handoff | 同じ永続registerを保持するため独立写像を置かない |
| coherent末端decoder | R176Cの同次元canonical SWAPと容量latchへ置換 |
| 経路pairing誤差 | register全体のoperator norm、hold、clock、leakageへ整理 |

## 4　保存する知見

R175の有限経路展開は、unitaryが各テンソル因子へどう作用するかを確認する代数的表示として有用である。一枝選択、完全dephasing、集団momentからの再準備が逆演算fringeを失うという診断も維持する。ただし物理的な経路分岐器や経路decoderの存在を独立に要求しない。

Q2-1のcoherent/dephase逆演算gap $1/2$ と、Q2-3のR177 gap $1/(2\sqrt2)$ は現行の永続mode構成でも同じ診断として使う。

## 5　再検討条件

経路限定設計を再び主線へ戻すのは、直接mode liftより単純な有限Hamiltonian構成を与え、経路数に依存しないoperator-norm誤差、可逆な分岐・再結合、末端instrument接続、外部制御資源の優位性を同時に示せる場合に限る。
