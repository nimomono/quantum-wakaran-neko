# 現行モデルの数値シミュレーション

このフォルダーには、現行モデルと現行論文の主張を直接検査する数値プログラムを置く。不採用モデルと置換済みモデルのコードは保存せず、Git履歴から参照する。

## 強化目標A2との関係

`ENHANCEMENT_TARGETS.md` のA2は、A1で定めたミクロ方程式そのものの直接数値再現を要求する。A1で開放ODE/SDEを基本方程式として直接定める場合は、そのODE/SDE自体を直接積分または標本化する。理想白色雑音を用いるSDEも、Itô/Stratonovich規約と共分散を固定して直接標本化してよい。

Hamiltonian無限浴、連続伝送線その他の連続浴をA1とする場合は、有限帯域・有限モード切断を直接計算し、対象時間窓で切断依存性または収束性を調べる。有効Schrödinger方程式、Born分布、R161生成子など、導出後の有効模型だけを計算した結果はA2の直接再現とは数えない。

## 強化目標B3との関係

全ての固定目標のB3では、B1で定めた具体的な実験装置を装置レベルで直接計算する。Q1/Q2の回路実装ではSPICE、回路ODE/SDE、伝送線模型などを用いる。Q3の粒子・流体・機械・波動実装では、Brownian dynamics、流体方程式、粒子追跡模型、有限要素・有限体積その他の支配方程式を装置幾何と制御条件まで含めて直接計算する。A1で理想白色雑音を用いる場合も、B3では実装側の有限相関時間または有限帯域を入れ、有限Q、熱雑音、素子公差、寄生成分、壁面効果、有限粒径、検出誤差など対象装置に固有の非理想性とともに成立領域を監査する。

## `tools/` の短い検算との区別

`tools/verify_*.py` は恒等式、有限次元の数値診断、短い回帰検査を担う。これらはA2/B3の補助検算になり得るが、ミクロ方程式または具体回路の直接シミュレーションを行っていない限り、それだけでA2/B3達成とは数えない。

## 収録規約

モデル別または強化目標別フォルダーを追加するときは、完全IDを明示し、少なくとも次を自己完結して保持する。

1. 対象となるA1模型またはB1実験装置と、そのミクロ方程式または装置支配方程式
2. 数値積分法、確率積分規約、乱数種
3. 基準設定と自動検算用の短縮設定
4. 主要観測量、対照条件、収束検査
5. 集約済み基準結果と再生成命令
6. 数値的一致からは導けない主張の境界

大容量の生軌道や全標本は収録せず、人が差分を読める集約結果を保存する。




## M64 three-entity open-Q3 current model

`simulations/m64/` はM64/R203A--R203DのA2 direct simulation入口とする。continuous profileではM37 signal、initial preparation、mean-flow relaxation、canonical overdamped tracer SDEを同一parameter setで直接積分・標本化する。finite-graph profileではlocal $R_i^\delta,J_{ij},T_{ij}^\delta$ からjump lawを構成し、Q3-4A/Q3-5の経験位置分布を検査する。

required checksはpartition identity、initial preparation、finite-time tracking、current dictionary、finite-volume refinement、finite-graph R161/R124/R182/R125整合を扱うが、direct trajectory再現の代替にしない。Q3-1-A2/Q3-2-A2は未監査のままとする。



## M65 canonical open selector

draft-140以後のM65正本はtwo-result first-passage open selectorである。正本lawの解析・数値回帰はrequired verifierで行い、Poisson waiting-time lawそのものを将来のphysical parentへ要求しない。

旧R204B/R204C fixed-hub chamber simulation案は現行M65 strengtheningから退役した。draft-141でM67/R211A--R211Cが二重井戸markerからR204E-compatible complete-result kernelを回収するfinite-Hamiltonian liftを定めた。tools/verify_m67_q1_first_passage.py はrequired reduced-kernel regressionであり、full finite harmonic bath trajectoryを直接積分するQ1 A2 simulationは引き続き未監査である。

## M66 thermal open/effective layer

`simulations/m66/README.md` には、M67/R212から縮約されるopen/effective layerとしてR206 common-hub trajectory、R205E thermal Gibbs preparation、R205F passive separation、phase-volume scaling、finite-bandwidth correction、terminal backreaction、always-on couplingの将来A2計画を置く。R212 required checksと既存R205 checksは解析・短い数値回帰であり、R206 full apparatusや具体spatial reservoirの直接simulationを代替しない。

## M67 two-entity finite-Hamiltonian parent

`simulations/m67/` はM67/R208A--R212Cのsupporting direct-trajectory検証入口である。Q1 selectorについてはdraft-141のrequired verifierがdouble-well reduced diffusionと誤差予算を監査するが、full finite-bath Q1 trajectoryはA2 strengtheningとして別に残す。Q3側では `run_full_compatibility_witness.py` がfinite flow/drag bathを含むM67→M64 compatibilityを一つの有限Hamiltonian trajectoryで診断する。draft-139でM67をQ3 physical parentへ昇格し、draft-142でthermal sectorをR212A--R212Cまで拡張する。R212B rotor mixing witnessを含むsupporting simulationはA2 promotion testではなく、Q2-2/Q3のA2状態は既存判定を維持する。
