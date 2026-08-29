@number: 2
@chapter: 本文
@title: 有限正準信号、M50枝状態数、共通有限枝instrument
@status: R112、R161--R164、R170をQ1・Q2・Q3の共通主線として整理する。M35は有限正準制御、比較、記録の補助部品に限定し、Born型枝生成はM50へ一本化する。

## 2.1 共通主線と統一M0の違い

本稿のBorn型読出しは次の1本の因果鎖を使う。

```math
v
\longrightarrow
\Omega_i^\delta(v)
\longrightarrow
\pi_i^\delta(v)
\longrightarrow
X=i
\longrightarrow
D_i.
```

有限正準信号 $v$ をM50の作用容量へ渡し、R164で排他的枝の状態数を数え、R161/R162で粒子位置を有限時間再平衡化し、R170で枝を固定して局所記録する。Q1、Q2、Q3の特殊性は信号の準備、枝グラフ、局所分析器、記録後状態にある。確率源は共通にM50であり、M35の選択器角を第2のBorn型機構として併用しない。

| 系列 | M50へ渡す単一試行信号 | 排他的出力 | 系列固有部分 |
|---|---|---|---|
| Q1 | M47の信号bath座標 $Z(\omega)$ | 左右井戸 | W型制御、有限コントラスト、結果別テンプレート |
| Q2-1 | M49のprogram担体 $d_{\rm prog}(\omega)$ | 4中央枝、2粒子位置 | 行分解bath、CNOT、直接枝decode |
| Q2-2 | M48切断後の各翼の局所信号 | 各翼2枝 | paired-Hopf準備、2翼局所合成、Bell監査 |
| Q3 | M37標本包絡 $Z_{t_\star}(\omega)$ | 有限空間セル | R167とR168による一般ray平均受渡し |

この共有は同一ハードウェアを意味しない。全系列の信号準備、容量結合、作用殻、衝突bath、時計、記録、resetを1つの有限局所Hamiltonian周期へまとめるM0は未完成である。

## 2.2 有限正準信号の辺代数

有限グラフ $\mathcal G=(\Omega,E)$ の各頂点 $z$ に実正準対 $(Q_z,P_z)$ と複素信号

```math
d_z=\frac{Q_z+iP_z}{\sqrt{2\mathcal J_0}}
```

を置く。全信号作用は $J_{\rm sig}=\mathcal J_0d^\dagger d$ である。時間依存Hermitian行列 $h(t)$ に対するHamiltonian

```math
H_h(t)=d^\dagger h(t)d
```

は $i\mathcal J_0\dot d=h(t)d$ を与える。無向辺 $e=\{u,v\}$ の差モード射影と辺生成子を

```math
\Pi_e
=
\frac12
(|u\rangle-|v\rangle)
(\langle u|-\langle v|),
```

```math
G_e
=
\mathcal J_0d^\dagger\Pi_ed
=
\frac14
\left[(Q_u-Q_v)^2+(P_u-P_v)^2\right]
```

とする。

<!-- theorem-start:lemma -->
**補題（R112：有限正準信号担体の共通辺代数）**

有限正準信号の可逆有効力学は、有限配置グラフ上の頂点作用項と差モード辺生成子の有限プログラムとして表せる。Q1、Q2、Q3の違いは、頂点集合、信号の物理的由来、係数、時計窓、排他的出力の実装にある。この代数だけから枝確率、粒子位置、記録、resetは従わない。
<!-- theorem-end:lemma -->

## 2.3 M35の限定された役割

M35から現行主線に残すのは次の部品である。

1. 局所位相回転と隣接 $QQ+PP$ 交換による有限ユニタリ回路。
2. 時計窓の自律化と有限誤差制御。
3. 外部から与えた制御値に対する滑らかな比較器と正式な無反応領域。
4. 正準SWAP、局所記録、テンプレート交換、内部逆計算。

M35の作用区間と一様選択器角から長期Born型頻度を得る旧経路は現行定理に使わない。M35は作用殻fiber内の平衡化も、結果列の独立同分布性も証明しない。旧経路の数式と結果IDは `notes/superseded_m35_born_sampler.md` に整理する。

固定benchmarkのprogram順序を外部scheduleで作ることは許す。このscheduleは入力条件の提示であり、同じ試行のBorn型出力を生成する機構ではない。

## 2.4 M50の作用容量と枝状態数

非零有限信号 $v\in\mathbb C^m$、等長埋込み $\Psi:\mathbb C^m\to\mathbb C^L$、排他的枝 $i\in\mathcal I$ を考える。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定し、

```math
J_i(v)=\mathcal J_0|(\Psi v)_i|^2,
\qquad
A_i^\delta(v)=J_i(v)+\delta q_iJ_{\rm sig}(v)
```

と置く。各枝に2つの非負作用を持つ排他的作用殻を置けば、R164の状態数は

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}A_i^\delta(v)
```

であり、単一Liouville母測度を1回だけ規格化すると

```math
\pi_i^\delta(v)
=
\frac{\Omega_i^\delta(v)}{\sum_j\Omega_j^\delta(v)}
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}{1+\delta}
```

を得る。零信号、安全閾値未満、有限幅遷移域は無反応 $\varnothing$ へ送る。

作用殻を消去する表示では

```math
E_i^\delta(v)=-\Theta\log\pi_i^\delta(v)
```

を条件付き中間状態有効自由エネルギーとして使う。状態数を残す表示と消去表示は同値であり、同じ縮約分配関数へ $\Omega_i^\delta e^{-E_i^\delta/\Theta}$ を入れて二重計数してはならない。

## 2.5 R161/R162の有限再平衡化

有限連結枝グラフ $G_X=(\mathcal I,E_X)$ で

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}}
```

を採用する。$q_{\min}=\min_iq_i$、$a_{\min}$ を正の最小辺重み、$\lambda_G$ を無重みグラフLaplacianの第1非零固有値とし、

```math
m_\delta=\frac{\delta q_{\min}}{1+\delta},
\qquad
\lambda_\delta=\kappa_Xa_{\min}m_\delta\lambda_G,
\qquad
C_\delta=\frac12\sqrt{m_\delta^{-1}-1}
```

と置く。R161により任意の初期枝分布 $p_0$ から

```math
D_{\rm TV}(p_{\tau_X},\pi^\delta(v))
\leq
C_\delta e^{-\lambda_\delta\tau_X}
```

である。R162はこの率を有限衝突熱浴と履歴セルを持つ局所Hamiltonian散乱へ任意精度で近似する。作用殻fiberは状態数を、衝突bathは粒子位置遷移を担い、同じ自由度ではない。

## 2.6 R170：M50固定入力時刻有限枝instrument

<!-- theorem-start:theorem -->
**定理（R170：M50固定入力時刻有限枝instrument）**

非零入力 $v\in\mathbb C^m$、有限枝グラフ $G_X$、等長埋込み $\Psi$、$\delta>0$、入力時刻 $t_\star$ を固定する。次を指定誤差内で実行できると仮定する。

1. $t_\star$ の信号を空の有限正準registerへSWAPし、処理中に保持する。
2. R164の作用容量と排他的作用殻を準備する。
3. R161の有限再平衡化を行い、R162の有限衝突実現で近似する。
4. 入射セルを止め、枝間ゲートを閉じて粒子位置を固定する。
5. 各枝だけに支持を持つ局所関数で空の記録セルを動かす。
6. 無反応、時計、使用済み衝突セル、旧信号、記録を含む拡大履歴を1対1に保つ。

このとき有限の $t_{\rm out}>t_\star$ と完全結果集合 $\mathcal I\cup\{\varnothing\}$ を持つinstrumentを選べる。理想分布を

```math
p_v^{\rm id}(i)=\pi_i^\delta(v),
\qquad
p_v^{\rm id}(\varnothing)=0
```

とすると、実分布は

```math
D_{\rm TV}(p_v^{\rm out},p_v^{\rm id})
\leq
\varepsilon_{170}
```

を満たす。ただし

```math
\varepsilon_{170}
\leq
\varepsilon_{\rm hold}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
+\varepsilon_{\varnothing}
```

であり、同じ物理偏差を複数項へ入れない。無反応を除いて再規格化しない。
<!-- theorem-end:theorem -->

R170は有限枝instrumentの共通定理であり、M37を前提にしない。Q1のR143、Q2-2のR154、Q3の固定時刻読出しはこの定理の特殊化または合成である。完全な証明と誤差台帳は付録Kに置く。

## 2.7 物理的意味と限界

熱化終了後の局所記録生成子は、枝 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、列挙した部品を1つの具体的有限局所Hamiltonianへ統合済みだと主張しない。現行の条件付き達成または部分達成は、この未統合部分を明示して判定する。一意エルゴードな外部scheduleまたは有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。
