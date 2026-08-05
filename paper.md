# 概要


本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。目的は、量子力学をミクロ構成の入力に置かず、量子力学に特徴的な力学と確率構造が縮約された有効理論として現れ得るかを検証することである。

現行模型の力学的な主線は、物理空間上の有限2成分誘導場と粒子の位相接続である。配置拡散・Nelson 経路は補助理論として付録Dへ分離し、Schrödinger 型力学の前提には使わない。場の実2成分を複素表示

```math
\zeta^\omega
=
\Phi_1^\omega+i\Phi_2^\omega
```

へまとめる。標本 $\omega$ ごとの場が、共通内部位相を除いて代表場 $\bar\zeta$ の近傍へ Hamiltonian の2次形式ノルムで集中することを、コヒーレント集中と定義する。高速整合、コヒーレント集中、粒子密度・流束との同期は別条件として管理する。

保存全位相作用を $\mathcal J_\phi\neq0$ とし、

```math
\hbar_{\rm eff}
=
\left|
\mathcal J_\phi
\right|
```

と置く。係数整合と位相向きの変換後に得る有効場を $\psi$ とする。本稿の力学的な中心結果は、任意初期分布からの吸引定理ではない。有限観測時間 $[0,T]$ において、十分準備された初期集団、共通の実外部位置ポテンシャル、小さい双対残差とエネルギー残差、初期コヒーレント集中、粒子・場流束差の時間積分上界を仮定する。その下で、

```math
i\hbar_{\rm eff}
\partial_t\psi
=
\left[
-
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\Delta
+
V(x,t)
\right]
\psi
+
R_{\rm red}
```

が、節を含む全領域上の弱形式として成立し、$R_{\rm red}$、コヒーレント分散、粒子密度と場強度の差を有限時間で評価できる。大域方程式は複素場で記述し、Madelung 表示と量子ポテンシャルは節集合を除いた各節領域だけで用いる。

この結果は、各標本のミクロ時間発展から両残差上界が得られた場合の条件付き有限時間安定性定理である。現行稿が既に持つのは、コヒーレント縮約集合へ制限した作用の一致、正定値2次模型の局所低速残差、高速成分の理想交換である。半正定値方向、時間依存射影、非線形再励起、正則化した位相接続の節近傍極限を含めて、現行ミクロ模型から両残差上界そのものを導く部分は未完成である。

静的な実ポテンシャルでは、保存対称性部分空間の固有関数を条件付き定常解として含める。これは節を持つ励起状態を有効方程式が許容するという結果であり、任意初期状態からの励起状態選択、吸引、節の生成・消滅・再結合を意味しない。

第2の主結果は、排他的な位置入口チャンネルに置いた2モード作用殻である。総作用 $A_i$ の殻容量

```math
\Omega_2(A_i)
=
\left(
2\pi
\right)^2A_i
```

は $A_i$ に線形である。場強度に従う作用分配と、全チャンネルで共通の法線流束、障壁、余面積因子、付随自由度の体積を仮定すると、

```math
P_i
=
\left|
\bar\zeta_i
\right|^2
\Delta V
+
O
\left(
\varepsilon_{\rm meas}
\right)
```

を入口通過頻度として得る。これは位置入口標本化則であり、任意基底に対する一般 Born 則ではない。また、初期密度同期の分布部分を供給するが、初期流束同期と標本化後のコヒーレント場への再埋め込みは供給しない。

第3の主結果は、同じ2成分場の反対称対モード、左右の局所分析器、共通未来比較器、2モード境界作用殻を統合した条件付き Bell 統計である。比較器は相関振幅を結果枝作用へ転送するが、Hamiltonian 読み出しと殻内混合だけでは結果セクター間の確率質量を作らない。4結果セクターで共通の境界密度、時計流束、余面積因子、付随自由度の体積、解多重度を仮定したときに限り、

```math
P
\left(
A,B
\mid
a,b
\right)
=
\frac14
\left[
1
-
AB
\cos
\Delta_{ab}
\right]
+
O
\left(
\varepsilon_{\rm meas}
\right)
```

を得る。理想対称条件では非信号周辺と CHSH 値 $2\sqrt2$ が従う。境界測度を生成側へ引き戻した完全履歴集団は設定に依存するため、Bell の前提違反は測定設定独立性にある。Bell の定理を否定せず、局所記録を後から変更する機構も導入しない。

本文は6章から成る。第1章で模型と3主結果、第2章で有限2成分場と準備条件、第3章で有限時間弱縮約・節・励起状態、第4章で位置入口作用殻、第5章で Bell 対モードと共通境界測度、第6章で誤差、反証条件、未解決問題を扱う。長い正準計算、作用殻積分、装置 Hamiltonian、配置拡散補助理論、有限準備浴、低速・高速交換は付録へ置く。

最大の未解決問題は2つある。力学側では、節近傍を含む現行ミクロ時間発展から双対残差、エネルギー残差、粒子・場流束差の上界を導くことである。測定側では、共通境界測度を事後選別なしの反復可能な準備・設定生成・結果形成・記録・リセット周期として実現することである。

# 模型、適用範囲、主結果

> **位置づけ：** 3本の主結果を、条件付き有限時間弱縮約、位置入口作用殻、共通境界測度下の Bell 統計として分離する。現行ミクロ模型から弱縮約残差と共通境界測度を準備する部分は未完成である。


## 問題設定

本論文の目的は、明示的な古典 Hamiltonian 系から、量子力学に特徴的な確率構造が縮約された有効理論として出現し得るかを検証することである。量子力学をミクロ Hamiltonian の入力には使わず、縮約後の式と測定統計を比較するときだけ参照する。

現行稿は問題を次の3層へ分ける。

1. 有限2成分場と粒子の位相接続から、十分準備された有限時間発展に対する弱 Schrödinger 型縮約を記述する。
2. 2モード作用殻の Liouville 流束から、位置入口標本化の線形重みを得る。
3. 反対称対モード、局所分析器、共通未来比較器、共通境界測度から Bell 型共同統計を得る。

3層は同じ2成分場の固定モードを使うが、論理的には独立の追加条件を持つ。第1層の有効方程式だけから Born 型入口頻度または Bell 型境界頻度は従わない。第2層の位置入口標本化だけから初期流束同期は従わない。第3層の殻容量だけから共通境界測度の物理的準備は従わない。

## 拡大全系と時間窓

1試行内の有限部分を概略

```math
\begin{aligned}
H_{\rm fin}
={}&
H_{\rm particle}
+
H_{\rm field}
+
H_{\rm prep}
+
H_{\rm source}
+
H_{\rm analyzer}
\\
&
+
H_{\rm pointer}
+
H_{\rm return}
+
H_{\rm compare}
+
H_{\rm memory}
+
H_{\rm clk}
\end{aligned}
```

と書く。外部環境と仕事源を含む拡大全系は

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}
H_{\rm link}
+
H_{\rm work}
```

である。拡大全系は Hamiltonian とし、有限部分だけを見た収支は

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

と表す。

試行周期を次の窓へ分ける。

| 窓 | 主な役割 | 理論上の扱い |
|---|---|---|
| 準備窓 | 規格化、全位相作用の固定、局所作用欠陥と高速成分の低減 | 有限浴の短記憶近似または同型高速モード交換 |
| 観測窓 | 位相接続による粒子・場の発展 | 対象セクターをほぼ閉鎖し、有限時間残差を評価 |
| 測定窓 | 局所分析、結果記録、戻り伝播、共通未来比較 | 1試行内の有限 Hamiltonian 写像 |
| 再準備窓 | 外部記録の保持、不要情報の処理、浴と補助系の再初期化 | 弱い外部交換を許す |

閉鎖 Hamiltonian 流は位相体積を保存するため、広い初期集合を低次元のコヒーレント集合へ永久吸引するとは主張しない。必要なのは、準備窓で十分準備された集団を作り、観測窓の有限時間内で逸脱を制御することである。

## 同じ2成分場の固定モード

基本的な実在場は、物理空間上の1つの実2成分場

```math
\boldsymbol\Phi(x)
=
\begin{pmatrix}
\Phi_1(x)\\
\Phi_2(x)
\end{pmatrix}
```

とその正準運動量である。有限モード切断後の場空間を、装置の組立時に固定した直交部分空間

```math
\mathcal H_{\rm field}
=
\mathcal H_{\rm phase}
\oplus
\mathcal H_{\rm pair}^{A}
\oplus
\mathcal H_{\rm pair}^{B}
\oplus
\mathcal H_{\partial}^{\rm cmp}
\oplus
\mathcal H_{\rm dark}
```

へ分ける。

- $\mathcal H_{\rm phase}$ は粒子との位相接続を担う。
- $\mathcal H_{\rm pair}^{A}$ と $\mathcal H_{\rm pair}^{B}$ は、反対称源、左右分析器、戻り伝播を担う。
- $\mathcal H_{\partial}^{\rm cmp}$ は、共通未来の比較2モードを含む。
- $\mathcal H_{\rm dark}$ は、混合角、時計、位相保持、記録、不要情報を担う。

これらは別々の場ではない。設定、結果、目標密度を見て部分空間を選び直す構成も採用しない。固定モード間の交差応答は測定誤差へ含める。

## 3種類の準備条件

第2章以降では、次の3条件を混同しない。

| 条件 | 内容 | 現在の位置づけ |
|---|---|---|
| 高速整合 | 動径運動量、局所作用欠陥、正定値2次模型の高速スペクトル成分が小さい | 限定模型で部分的に準備可能 |
| コヒーレント集中 | 標本ごとの複素場が共通位相を除いて同じ代表場へエネルギーノルム集中する | 初期条件。有限時間安定性は残差仮定下で導出 |
| 密度・流束同期 | 粒子密度・流束が代表場の強度・流束に近い | 初期密度の分布部分だけを第4章で準備。流束差は独立条件 |

高速整合が成立しても、異なる標本が異なる固有モードへ分かれていればコヒーレント集中は成立しない。コヒーレント集中が成立しても、粒子分布がその場強度に従うとは限らない。連続の式だけから密度差は評価できるが、流束同期そのものは導けない。

## 主定理1の範囲

第3章の主定理1は、十分準備された集団に対する条件付き有限時間安定性定理である。仮定は次である。

1. 有限セル2成分場または共通2次形式領域を持つ連続極限。
2. 固定規格化と固定全位相作用。
3. 実数値で下から有界な外部位置ポテンシャル。
4. 初期高速整合と初期コヒーレント集中。
5. 各標本の有効複素場方程式に対する積分可能な双対残差上界とエネルギー残差上界。
6. 初期密度同期と、粒子・場流束差の時間積分上界。
7. 有限観測時間と一様エネルギー上界。
8. 振幅勾配係数と保存作用の係数整合。

結論は、代表有効場の残差付き弱 Schrödinger 型方程式、コヒーレント分散の有限時間評価、粒子密度と場強度の弱同期評価である。節を含む全領域では複素弱形式を使い、節外だけで Madelung 表示と循環量子化を用いる。

この定理は、現行 M0 のミクロ方程式から仮定5と6を無条件に導く定理ではない。正定値2次模型の局所残差は仮定5の一部を支えるが、半正定値方向、時間依存射影、非線形再励起、節近傍の重み付き接続誤差は未完成である。

## 主定理2の範囲

第4章の主定理2は位置入口標本化に限定する。排他的入口チャンネル $i$ に、場強度に比例する総作用

```math
A_i
=
A_{\rm tot}
\left|
\bar\zeta_i
\right|^2
\Delta V
```

を置く。2モード作用殻の容量は $A_i$ に線形である。入口面の法線速度、障壁、余面積因子、付随自由度の体積、解多重度が共通なら、正方向入口通過頻度は

```math
P_i
=
\left|
\bar\zeta_i
\right|^2
\Delta V
```

となる。

これは一般 Born 則ではなく、初期密度同期の分布部分を供給する候補である。粒子流束の方向、単流束化、標本化後の活性場の再埋め込みは別問題である。

## 主定理3の範囲

第5章の主定理3は、共通境界測度下の Bell 共同確率である。論理の順序は次である。

1. 2つの固定源チャンネルが反対称対モードを準備する。
2. 左右の局所分析器が局所モードだけを回転する。
3. 結果枝作用 $K_{AB}$ が余弦則を持つ。
4. 共通未来比較器が $K_{AB}$ を比較2モードの総作用へ転送する。
5. 2モード殻容量が比較作用に線形となる。
6. 4結果セクターで共通の境界測度を仮定する。
7. Bell 共同確率、非信号周辺、CHSH値を得る。
8. 境界測度を生成側へ引き戻し、測定設定独立性の破れを特定する。

比較器は過去の局所記録を変更しない。共通境界測度を通常の前向き試行周期が事後選別なしに生成することは、主定理3の仮定であって結論ではない。

## 導出状態

本論文の主要主張をまとめる。

| 主張 | 導出状態 | 主な制限 |
|---|---|---|
| 有限セル正準構造、固定作用平方分解 | 厳密結果 | 節では極座標を使わない |
| 正定値2次模型の低速・高速分離と理想交換 | 厳密結果 | 局所定数係数、正定値、精密調整 |
| コヒーレント縮約集合上の Madelung 作用 | 厳密結果 | 集合への準備と維持は別問題 |
| 弱残差仮定下の有限時間複素場縮約 | 近似結果・仮説依存 | ミクロ残差上界を仮定 |
| 節を含む複素弱形式 | 厳密な表現上の結果 | 位相接続からの節横断導出は未完成 |
| 対称性セクターの固有状態包含 | 条件付き結果 | 選択・吸引ではない |
| 位置入口2モード作用殻 | 厳密結果・仮説依存 | 共通流束因子が必要 |
| Bell余弦枝作用 | 厳密結果・仮説依存 | 反対称源と局所平面回転 |
| 共通境界測度下の Bell 統計 | 厳密結果・仮説依存 | 境界測度の物理的準備は未完成 |

## 本論文が主張しないこと

本論文は次を主張しない。

1. 任意初期分布からのコヒーレント集中。
2. 閉鎖 Hamiltonian 流による永久吸引。
3. 長時間一様な Schrödinger 型極限。
4. 一般の節生成、消滅、再結合。
5. 任意初期状態からの励起状態選択。
6. 任意基底に対する一般 Born 則。
7. 一般の複合状態または一般 Tsirelson 原理。
8. 共通境界測度を生成する完成した測定周期。
9. Bell の定理の否定。
10. 後の比較器が過去の記録を変更する逆因果制御。

配置拡散・Nelson 経路は付録Dに保存するが、現行力学の前提ではない。旧3モード Bell 作用殻と旧終端関数模型は研究メモに保存し、現行模型には使わない。

# 有限2成分場と準備済み低速領域

> **位置づけ：** 有限セルの正準構造、保存全位相作用、固定作用平方分解、厳密規格化下の局所座標 Hamiltonian は厳密結果である。高速整合は限定模型で部分的に準備できる。初期コヒーレント集中と粒子・場同期は独立の準備条件である。


## 大域変数と局所極座標

セル $i=1,\ldots,L$ に実2成分正準対

```math
\boldsymbol\Phi_i
=
\begin{pmatrix}
\Phi_{1,i}\\
\Phi_{2,i}
\end{pmatrix},
\qquad
\boldsymbol\Pi_i
=
\begin{pmatrix}
\Pi_{1,i}\\
\Pi_{2,i}
\end{pmatrix}
```

を置く。Poisson 括弧は

```math
\left\{
\Phi_{\alpha,i},
\Pi_{\beta,j}
\right\}
=
\delta_{\alpha\beta}
\delta_{ij}
```

である。節を含む大域変数は $\boldsymbol\Phi_i$ と $\boldsymbol\Pi_i$ であり、複素表示を

```math
\zeta_i
=
\Phi_{1,i}
+
i\Phi_{2,i}
```

とする。

$|\boldsymbol\Phi_i|>0$ の局所領域だけで、

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix}
```

と書く。動径運動量と局所位相作用を

```math
p_{r,i}
=
\boldsymbol\Pi_i
\cdot
\frac{
\boldsymbol\Phi_i
}{
r_i
},
\qquad
j_i
=
\Phi_{1,i}\Pi_{2,i}
-
\Phi_{2,i}\Pi_{1,i}
```

と定める。

<!-- theorem-start:proposition -->
**命題（有限セル極座標の正準1形式）**
$r_i>0$ の各セルで、

```math
\boldsymbol\Pi_i
\cdot
d\boldsymbol\Phi_i
=
p_{r,i}
\,dr_i
+
j_i
\,d\theta_i
```

が成立する。
<!-- theorem-end:proposition -->

この命題は局所座標の厳密な正準性を与えるが、節上で $\theta_i$ を定義しない。以後、大域的な集中と弱方程式は $\zeta$ で記述し、極座標は節外の計算に限定する。

## 規格化と保存全位相作用

セル体積を $\Delta V$ とし、場強度を

```math
\mathcal N_\Phi
=
\sum_i
\left|
\zeta_i
\right|^2
\Delta V
```

とする。主定理では

```math
\mathcal N_\Phi
=
1
```

をホロノミック制約として課す。有限ペナルティ

```math
H_{\rm norm}
=
\frac{
\lambda_{\rm norm}
}{
2
}
\left(
\mathcal N_\Phi-1
\right)^2
```

は別模型であり、厳密規格化と同じ不変セクターではない。

全セルを共通角だけ内部回転する対称性の生成子は

```math
\mathcal J_\phi
=
\sum_i
j_i
\Delta V
```

である。全 Hamiltonian がこの共通回転に不変なら、

```math
\left\{
\mathcal J_\phi,
H_{\rm all}
\right\}
=
0
```

となる。個々の $j_i$ はセル間を流れ得るが、$\mathcal J_\phi$ は保存される。本稿は $\mathcal J_\phi\neq0$ の固定セクターを取る。

## 固定作用下の平方分解

$r_i>0$、$\mathcal N_\Phi=1$ の局所座標で、回転エネルギーを

```math
E_{\rm rot}
=
\sum_i
\frac{
j_i^2
}{
2Ir_i^2
}
\Delta V
```

とする。

<!-- theorem-start:theorem -->
**定理（固定作用下の局所作用分配）**
固定 $\mathcal J_\phi$ の下で、

```math
E_{\rm rot}
=
\frac{
\mathcal J_\phi^2
}{
2I
}
+
\sum_i
\frac{
\left(
j_i-\mathcal J_\phi r_i^2
\right)^2
}{
2Ir_i^2
}
\Delta V
```

が成立する。従って、固定した振幅に対する一意な最小配置は

```math
j_i
=
\mathcal J_\phi r_i^2
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
平方項を展開し、

```math
\sum_i
j_i
\Delta V
=
\mathcal J_\phi,
\qquad
\sum_i
r_i^2
\Delta V
=
1
```

を代入する。交差項と定数項を整理すると $E_{\rm rot}$ が残る。
<!-- theorem-end:proof -->

これは固定振幅上のエネルギー最小化であって、閉鎖 Hamiltonian 流の吸引定理ではない。

## 高速整合

セル体積を正準変数へ吸収し、

```math
R_i
=
r_i
\sqrt{
\Delta V
},
\qquad
P_i
=
p_{r,i}
\sqrt{
\Delta V
},
\qquad
J_i
=
j_i
\Delta V
```

とする。規格化と全位相作用は

```math
N
=
\sum_iR_i^2,
\qquad
\mathcal J_\phi
=
\sum_iJ_i
```

である。局所作用欠陥を

```math
\delta J_i
=
J_i
-
\frac{
\mathcal J_\phi R_i^2
}{
N
}
```

と定めると、

```math
\sum_i
\frac{
\delta J_i^2
}{
R_i^2
}
=
\sum_i
\frac{
J_i^2
}{
R_i^2
}
-
\frac{
\mathcal J_\phi^2
}{
N
}
```

が厳密に成立する。

直交座標で同じ条件を見るため、内部回転行列を

```math
\mathbb J
=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
```

とする。規格化済みの単位系では、理想接線運動量は $\mathcal J_\phi\mathbb J\boldsymbol\Phi_i$ である。代数的高速欠陥を

```math
\boldsymbol D_i
=
\boldsymbol\Pi_i
-
\mathcal J_\phi
\mathbb J
\boldsymbol\Phi_i
```

と書ける。一般の慣性係数とセル重みを使う場合は対応する線形同型を挿入する。$\boldsymbol D_i=0$ は $p_{r,i}=0$ と $j_i=\mathcal J_\phi r_i^2$ に対応する。

ただし、$\boldsymbol D$ と正定値2次化の高速 Riesz 射影は一般には同じではない。前者は座標的な欠陥、後者は特定の2次 Hamiltonian のスペクトル部分空間である。付録Fの正定値条件下だけで両者の局所的な同値を使う。

本稿で高速整合とは、次の量が適用模型に応じて小さいことをいう。

```math
\varepsilon_{\rm fast}^2
=
\mathbb E_\omega
\left[
\sum_i
\left(
P_i^\omega
\right)^2
+
\sum_i
\frac{
\left(
\delta J_i^\omega
\right)^2
}{
\left(
R_i^\omega
\right)^2
}
+
\left\|
P_{\rm f}
z^\omega
\right\|^2
\right]
```

ここで $P_{\rm f}$ は、定義できる場合だけ用いる高速スペクトル射影である。

## 高速整合の準備機構

高速整合には2つの補助模型を使う。

1. 付録Eの有限振幅浴と有限作用交換浴。
2. 付録Fの正定値2次模型と同型高速モード交換補助系。

有限作用交換浴は位相差の余弦と正弦へ対称に結合する。共通内部回転に不変なので $\mathcal J_\phi$ を厳密に保存し、対となる逆項は位相固定ポテンシャルを作らない。固定振幅、短記憶、低温、有限浴再帰前の近似では、局所作用欠陥の2次量を減少させる。

同型交換は、正定値定数係数2次模型の高速 symplectic 部分空間に限定すれば厳密である。補助系が零状態から始まり交換角が $\pi/2$ なら、高速成分を補助系へ完全に移す。

2つの機構は同じ主張ではない。局所浴は局所的だが近似的であり、同型交換は2次模型内で厳密だが大域射影、同型複製、精密な交換角を必要とする。どちらも異なる標本を同じ場プロファイルへ集中させず、粒子密度と場強度も同期させない。

準備浴は観測中の相対位相運動を変え得るため、準備窓の後に切り離す。時間尺度は

```math
\tau_{\rm corr}
\ll
T_{\rm prep}
\ll
T_{\rm obs},
T_{\rm rec}
```

と分ける。有限温度、記憶尾、有限浴再帰、交換角誤差、補助初期エネルギー、観測中の高速再生成は第6章の準備誤差と縮約誤差へ含める。

## コヒーレント集中

各標本の複素場を $\zeta^\omega$ とする。連続模型では外部ポテンシャルを含む Hamiltonian の閉じた2次形式を $h_V$、共通形式領域を $\mathcal Q$ とする。定数 $c_V$ を十分大きく取り、

```math
\left\|
u
\right\|_{\mathcal E_V}^2
=
\left\|
u
\right\|_{L^2}^2
+
h_V
\left[
u
\right]
+
c_V
\left\|
u
\right\|_{L^2}^2
```

をエネルギーノルムとする。有限セルでは、同じ記号を離散勾配と実ポテンシャルを含む正定値2次形式に使う。

共通内部位相を物理的に同一視し、代表場 $\bar\zeta(t)$ に対する射影距離を

```math
\varepsilon_{\rm coh}^2(t)
=
\mathbb E_\omega
\inf_{
\alpha\in
\left[
0,2\pi
\right)
}
\left\|
\zeta^\omega(t)
-
e^{i\alpha}
\bar\zeta(t)
\right\|_{\mathcal E_V}^2
```

と定める。十分小さい分散と、基準場に対する非零重なりの下で、位相整合した射影重心を $\bar\zeta$ とする。

単純な標本平均を代表場にしてはならない。標本ごとの共通位相が異なると平均が相殺するからである。また、各時刻で独立に位相を最小化すると時間微分が不定になる。第3章では、初期代表場から連続に追跡する位相規約を使い、実数の共通位相項 $\lambda(t)$ を許す。

高速整合が成立しても、標本が異なる低速固有モードへ分かれていれば $\varepsilon_{\rm coh}$ は小さくない。従って、初期コヒーレント集中は独立の準備条件である。

## 場強度・場流束と粒子同期

代表場の強度を

```math
q
=
\left|
\bar\zeta
\right|^2
```

とする。位相向きを係数整合した有効場を $\psi$ とし、その場流束を

```math
\boldsymbol j_\psi
=
\frac{
\hbar_{\rm eff}
}{
m
}
\operatorname{Im}
\left(
\psi^*
\nabla\psi
\right)
```

とする。粒子側の密度と流束を $\rho$、$\boldsymbol J_{\rm p}$ とする。

密度・流束同期は

```math
\left\|
\rho-q
\right\|_{H^{-1}}
\ll1,
\qquad
\int_0^T
\left\|
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right\|
\,dt
\ll1
```

で評価する。節では $q=0$ となるため、$(\rho-q)/q$ のような相対誤差は使わない。

コヒーレント集中から、各標本場の強度と場流束が代表場へ集中することは積評価で従う。しかし、粒子密度と粒子流束との同期は従わない。第4章の位置入口作用殻は初期密度の分布部分を準備する候補だが、流束同期を準備しない。

## 位相接続

連続補間した2成分場に対し、正則化した接続を

```math
\boldsymbol a_\varepsilon
=
\frac{
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
}{
\left|
\boldsymbol\Phi
\right|^2
+
\varepsilon^2
}
```

とする。節外の極座標では

```math
\boldsymbol a_\varepsilon
=
\frac{
r^2
}{
r^2+\varepsilon^2
}
\nabla\theta
```

である。粒子正準対を $(X,P)$ とし、

```math
H_{\rm p}
=
\frac{
\left|
P
-
\mathcal J_\phi
\boldsymbol a_\varepsilon(X)
\right|^2
}{
2m
}
+
V(X,t)
```

とする。粒子運動量を消去すると、

```math
L_{\rm p}
=
\frac m2
\left|
\dot X
\right|^2
+
\mathcal J_\phi
\boldsymbol a_\varepsilon(X)
\cdot
\dot X
-
V(X,t)
```

を得る。

節外で $\varepsilon\to0$ とし、局所作用整合と密度同期を用いると、場の正準項と粒子接続項は位相の物質微分を作る。これは第3章の縮約作用を与える。しかし、$\rho-q$ が弱いノルムで小さいだけでは、節近傍で大きくなり得る $\boldsymbol a_\varepsilon$ との積を制御できない。節近傍の重み付き接続誤差は、ミクロ残差上界の独立成分として残す。

## 外部位置ポテンシャル

有限セル定理では、$V_i(t)$ を実数値とし、有限観測時間で一様有界、かつ対象軌道を有限エネルギー領域へ保つと仮定する。位置依存性を調和型または弱非線形へ限定しない。

連続極限では、次を仮定する。

1. $V(x,t)$ は実数値で下から有界である。
2. $H_V(t)$ は自己共役であるか、閉じた半有界2次形式を持つ。
3. 時間依存の場合は有限観測時間で共通形式領域 $\mathcal Q$ を持つ。
4. 対応する発展作用素がエネルギーノルムで有限時間安定である。
5. 境界条件を固定する。

$V(x,t)$ の位置依存の非線形性自体を小さい摂動とはしない。小さくするのは、高速・低速間の再励起、縮約集合からの逸脱、有限セル誤差、接続正則化誤差である。$V=V(|\psi|^2)$ のような状態依存ポテンシャルは扱わない。

## 準備済み初期集団

第3章で使う初期集団は、次を満たす。

1. 規格化と全位相作用のセクターが固定されている。
2. $\varepsilon_{\rm fast}(0)$ が小さい。
3. $\varepsilon_{\rm coh}(0)$ が小さい。
4. $\|\rho(0)-q(0)\|_{H^{-1}}$ が小さい。
5. 観測窓における粒子・場流束差の時間積分に上界がある。
6. 一様な場エネルギー上界がある。
7. 代表場の時間位相を連続に選べる非零重なりがある。

1から3を準備する完成した有限 Hamiltonian 装置はまだない。付録Eと付録Fは2の一部だけを扱い、第4章は4の分布部分だけを扱う。第3章の有限時間定理は、この不足を仮定として明示した上で、観測窓内の安定性を述べる。

# 有限時間弱 Schrödinger 型縮約、節、励起状態

> **位置づけ：** コヒーレント縮約集合上の Madelung 作用と、その変分は厳密結果である。各標本の弱縮約残差を仮定した有限時間安定性と弱密度同期は近似結果である。現行ミクロ模型から節近傍を含む残差上界を導く部分は未完成である。


## 有効複素場の位相向き

ミクロ複素場 $\zeta^\omega=\Phi_1^\omega+i\Phi_2^\omega$ と、その射影的代表場 $\bar\zeta$ を第2章で定めた。位相接続の縮約作用では

```math
S
=
-
\mathcal J_\phi
\theta
```

となるため、Schrödinger 表示の位相向きは保存作用の符号に依存する。そこで、有効場を

```math
\psi
=
\operatorname{Re}
\bar\zeta
-
i
\operatorname{sgn}
\left(
\mathcal J_\phi
\right)
\operatorname{Im}
\bar\zeta
```

と定める。$\mathcal J_\phi>0$ なら $\psi=\bar\zeta^*$、$\mathcal J_\phi<0$ なら $\psi=\bar\zeta$ である。従って

```math
q
=
\left|
\psi
\right|^2
=
\left|
\bar\zeta
\right|^2
```

である。

有効作用定数を

```math
\hbar_{\rm eff}
=
\left|
\mathcal J_\phi
\right|
```

とする。$\bar\zeta$ と $\psi$ を同じ記号にせず、ミクロ場、代表場、有効場の役割を分ける。

## コヒーレント縮約集合上の作用

節外の局所座標で、局所作用整合、密度同期、単流束化、動径低速化、接続極限を理想的に課す。場の正準項と粒子の接続項は

```math
-\int
\rho
\left(
\partial_tS
+
\boldsymbol v
\cdot
\nabla S
\right)
\,dx
```

を作る。固定作用セクターで定数となる回転基底エネルギーを除くと、制限作用は

```math
\mathcal A_{\rm red}
\left[
\rho,
\boldsymbol v,
S
\right]
=
\int
\left[
\frac m2
\rho
\left|
\boldsymbol v
\right|^2
-
\rho V
-
\rho
\left(
\partial_tS
+
\boldsymbol v
\cdot
\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt
```

となる。

<!-- theorem-start:theorem -->
**定理（縮約集合上の Madelung 作用）**
理想縮約条件と係数整合

```math
\kappa
=
\frac{
\mathcal J_\phi^2
}{
2m
}
```

の下で、$\mathcal A_{\rm red}$ は作用定数 $\hbar_{\rm eff}$ を持つ Madelung 作用に一致する。
<!-- theorem-end:theorem -->

この定理は、縮約集合へ制限した後の作用の代数的一致である。ミクロ流がその集合へ吸引されること、または制限作用の特定の停留経路を選ぶことは含まない。

$S$、$\boldsymbol v$、$\rho$ を独立に変分すると、

```math
\partial_t\rho
+
\nabla
\cdot
\left(
\rho\boldsymbol v
\right)
=
0,
\qquad
m\boldsymbol v
=
\nabla S
```

および

```math
\partial_tS
+
\frac{
\left|
\nabla S
\right|^2
}{
2m
}
+
V
-
\frac{
\mathcal J_\phi^2
}{
2m
}
\frac{
\Delta\sqrt\rho
}{
\sqrt\rho
}
=
0
```

を得る。後2式を節外で複素表示へまとめると理想 Schrödinger 型方程式になる。

## 弱縮約残差

一般の実外部位置ポテンシャルに対し、

```math
H_V(t)
=
-
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\Delta
+
V(x,t)
```

とする。共通2次形式領域を $\mathcal Q$、その双対を $\mathcal Q^*$ とする。

標本ごとの位相向きを整えた有効場を $\psi^\omega$ とする。第2章の連続位相整合を行った後、ミクロ時間発展が

```math
i\hbar_{\rm eff}
\partial_t
\psi^\omega
=
H_V(t)
\psi^\omega
+
R^\omega
```

を $\mathcal Q^*$ で満たすと仮定する。共通位相項がある場合は、標本ごとの連続位相変換へ吸収する。弱方程式を制御する残差を

```math
\varepsilon_{\rm mic}^{\rm wk}(T)
=
\int_0^T
\left(
\mathbb E_\omega
\left\|
R^\omega(t)
\right\|_{\mathcal Q^*}^2
\right)^{1/2}
\,dt
```

と定める。エネルギーノルムでのコヒーレント安定性には、これより強い

```math
\varepsilon_{\rm mic}^{\mathcal E}(T)
=
\int_0^T
\left(
\mathbb E_\omega
\left\|
R^\omega(t)
\right\|_{\mathcal E_V}^2
\right)^{1/2}
\,dt
```

も仮定する。$\mathcal E_V$ は連続埋め込みにより $\mathcal Q^*$ の残差としても読める。双対残差だけからエネルギーノルム集中は導かない。

$R^\omega$ は1つの物理誤差ではなく、次をまとめた監査量である。

1. 有限セルと連続極限の差。
2. 局所作用欠陥と動径欠陥。
3. 正定値2次模型から外れる半正定値方向。
4. 時間依存する低速・高速射影。
5. 非線形高速再励起。
6. 係数不一致。
7. 節近傍の正則化接続と密度差の重み付き積。

現行ミクロ模型から1から7を一様に評価する定理はない。粒子・場流束差は $R^\omega$ へ含めず、第3.6節の独立な同期誤差として扱う。付録Fの局所2次残差は3から5を除いた限定模型での部分結果である。

## 主定理1

<!-- theorem-start:theorem -->
**定理（準備済み集団の条件付き有限時間弱縮約）**
有限観測時間 $T>0$ を固定する。次を仮定する。

1. $H_V(t)$ が共通形式領域 $\mathcal Q$ 上で有限時間安定な発展作用素を生成する。
2. $\|\psi^\omega(t)\|_{\mathcal E_V}$ が $\omega$ と $0\leq t\leq T$ について一様に有界である。
3. 初期コヒーレント分散 $\varepsilon_{\rm coh}(0)$ が小さい。
4. 連続位相整合後の残差が $\varepsilon_{\rm mic}^{\rm wk}(T)$ と $\varepsilon_{\rm mic}^{\mathcal E}(T)$ の上界を満たす。
5. 位相整合平均が零にならず、代表場の連続位相規約を選べる。

このとき、規格化した代表有効場 $\psi$ と実数値関数 $\lambda(t)$ が存在し、

```math
i\hbar_{\rm eff}
\partial_t\psi
=
H_V(t)\psi
+
\lambda(t)\psi
+
R_{\rm red}
```

が $\mathcal Q^*$ で成立する。さらに、

```math
\left\|
R_{\rm red}
\right\|_{
L^1
\left(
0,T;
\mathcal Q^*
\right)
}
\leq
C_T
\varepsilon_{\rm mic}^{\rm wk}(T)
```

および

```math
\sup_{
0\leq t\leq T
}
\varepsilon_{\rm coh}(t)
\leq
C_T
\left[
\varepsilon_{\rm coh}(0)
+
\varepsilon_{\rm mic}^{\mathcal E}(T)
\right]
```

を得る。時間依存の共通位相変換により $\lambda(t)$ を除去できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
標本ごとの共通位相を初期代表場から連続に選び、位相整合した場を作る。共通線形発展を差し引くと、2標本の差は初期差と残差差の Duhamel 積分で表される。エネルギーノルムでの有限時間安定性と Minkowski 不等式により、$\varepsilon_{\rm mic}^{\mathcal E}$ を用いたコヒーレント分散の上界を得る。位相整合平均を規格化すると、平均残差と規格化微分の組合せが代表場の接空間に入る。その位相方向成分を実数の $\lambda(t)$ とし、残りを $R_{\rm red}$ とする。平均ノルムの正の下限により、両者は $\varepsilon_{\rm mic}^{\rm wk}$ で評価できる。詳細は付録Aに置く。
<!-- theorem-end:proof -->

この定理は、双対残差とエネルギー残差がともに小さいなら、コヒーレント集中が有限時間保たれ、代表場も小さい残差の弱方程式を満たすという安定性結果である。仮定4を現行 M0 から導くことは定理の外にある。従って「有限古典 Hamiltonian 系から節を含む Schrödinger 方程式を無条件に導出した」とは読まない。

## 場強度・場流束の集中

位相整合した標本場と代表場の差を $\delta\psi^\omega=\psi^\omega-\psi$ とする。$L^2$ と勾配の一様上界があれば、

```math
\left\|
\left|
\psi^\omega
\right|^2
-
\left|
\psi
\right|^2
\right\|_{L^1}
\leq
\left(
\left\|
\psi^\omega
\right\|_{L^2}
+
\left\|
\psi
\right\|_{L^2}
\right)
\left\|
\delta\psi^\omega
\right\|_{L^2}
```

である。また、

```math
\begin{aligned}
&
\left\|
\operatorname{Im}
\left[
\left(
\psi^\omega
\right)^*
\nabla\psi^\omega
-
\psi^*
\nabla\psi
\right]
\right\|_{L^1}
\\
&\qquad
\leq
\left\|
\delta\psi^\omega
\right\|_{L^2}
\left\|
\nabla\psi^\omega
\right\|_{L^2}
+
\left\|
\psi
\right\|_{L^2}
\left\|
\nabla\delta\psi^\omega
\right\|_{L^2}.
\end{aligned}
```

従ってエネルギーノルムでのコヒーレント集中は、標本場の強度と場流束の代表場への集中を与える。粒子密度・流束との同期はこの積評価からは従わない。

## 粒子密度との弱同期

粒子側と場側の連続の式の差を

```math
\partial_t
\left(
\rho-q
\right)
+
\nabla
\cdot
\left(
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right)
=
R_{\rm cont}
```

とする。ここで

```math
\boldsymbol j_\psi
=
\frac{
\hbar_{\rm eff}
}{
m
}
\operatorname{Im}
\left(
\psi^*
\nabla\psi
\right)
```

である。

<!-- theorem-start:proposition -->
**命題（弱密度同期評価）**
適切な境界条件の下で、

```math
\begin{aligned}
\left\|
\rho(t)-q(t)
\right\|_{H^{-1}}
\leq{}&
\left\|
\rho(0)-q(0)
\right\|_{H^{-1}}
\\
&
+
\int_0^t
\left\|
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right\|_{L^2}
\,ds
+
\int_0^t
\left\|
R_{\rm cont}
\right\|_{H^{-1}}
\,ds.
\end{aligned}
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
差の連続の式を時間積分し、発散作用素が $L^2$ から $H^{-1}$ へ有界であることを使う。
<!-- theorem-end:proof -->

この命題は密度同期の有限時間評価である。連続の式だけから流束同期の保存は導けない。粒子速度分散、接続追従、古典圧力を含む流束差の時間積分は独立の仮定である。

## 節を含む大域弱形式

時間依存の共通位相を除いた後、主定理1の式は

```math
i\hbar_{\rm eff}
\partial_t\psi
=
H_V(t)\psi
+
R_{\rm red}
```

となる。これは $\psi=0$ の点でも定義できる。試験関数 $\eta\in C_c^\infty$ に対し、

```math
\begin{aligned}
&
\int_0^T
\left[
-
i\hbar_{\rm eff}
\left\langle
\psi,
\partial_t\eta
\right\rangle
+
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\left\langle
\nabla\psi,
\nabla\eta
\right\rangle
+
\left\langle
V\psi,
\eta
\right\rangle
\right]
\,dt
\\
&\qquad
=
\int_0^T
\left\langle
R_{\rm red},
\eta
\right\rangle
\,dt
\end{aligned}
```

と書ける。端点項は試験関数の支持または初期値形式に応じて加える。

節集合を

```math
\mathcal Z_t
=
\left\{
x
\mid
\psi(x,t)=0
\right\}
```

とする。大域弱形式は $\mathcal Z_t$ を除外しない。一方、

```math
\psi
=
\sqrt q
\exp
\left(
\frac{
iS
}{
\hbar_{\rm eff}
}
\right)
```

という Madelung 表示は、$\mathcal Z_t$ を除いた各連結節領域 $\Omega_k(t)$ だけで用いる。量子ポテンシャルを節上で点ごとに評価しない。

複素弱形式を採用したことは、ミクロ位相接続から節をまたぐ導出が完成したことを意味しない。正則化接続

```math
\boldsymbol a_\varepsilon
=
\frac{
\operatorname{Im}
\left(
\zeta^*
\nabla\zeta
\right)
}{
\left|
\zeta
\right|^2
+
\varepsilon^2
}
```

と密度誤差の積を制御するには、節近傍の粒子質量上界、重み付き同期、正則化極限と有限セル極限の順序が必要である。これは $\varepsilon_{\rm mic}^{\rm wk}$ と $\varepsilon_{\rm mic}^{\mathcal E}$ の未導出成分である。

## 節外の Madelung 表示と循環量子化

$q>0$ の各節領域で、理想残差を零とすれば弱方程式は連続の式と Hamilton--Jacobi 型方程式へ分解できる。非零残差は両式の弱い源項へ分かれる。

2成分場が閉曲線 $\gamma$ 上で非零かつ単価なら、位相巻数 $n\in\mathbb Z$ により

```math
\oint_\gamma
\nabla\theta
\cdot
d\ell
=
2\pi n
```

である。従って

```math
\oint_\gamma
\nabla S
\cdot
d\ell
=
2\pi
\hbar_{\rm eff}
N,
\qquad
N\in\mathbb Z
```

を得る。

これは単価な基礎場と非零経路を仮定した条件付き循環量子化である。節の生成・消滅時の巻数変化、全ての物理的初期流れを単価場から準備すること、節近傍の接続極限は未完成である。従って Wallstrom 問題への全面的回答ではない [19]。

## 対称性セクターと励起状態

時間非依存の $H_V$ が離散固有値を持つとする。保存対称性で不変な閉部分空間 $\mathcal H_\sigma$ を取り、

```math
H_V
\varphi_n
=
E_n
\varphi_n,
\qquad
\varphi_n
\in
\mathcal H_\sigma
```

とする。

<!-- theorem-start:corollary -->
**系（対称性で保護された固有状態の条件付き包含）**
主定理1の残差が零で、初期代表場が $\varphi_n$ なら、

```math
\psi_n(t)
=
\exp
\left(
-
\frac{
iE_nt
}{
\hbar_{\rm eff}
}
\right)
\varphi_n
```

は大域弱方程式の定常解である。$\mathcal H_\sigma$ が発展で不変なら、その対称性が強制する節は保存される。
<!-- theorem-end:corollary -->

例えば奇パリティ部分空間の最低固有状態は、全空間では励起状態になり得る。この系は有効方程式が節を持つ固有状態を許容することを示すが、準備浴がその状態を選ぶことは示さない。

次は未解決である。

1. 任意初期状態からの励起状態選択。
2. 低速部分空間内のエネルギー緩和。
3. 一般の非対称ポテンシャルでの節固定。
4. 節の生成、消滅、再結合。
5. $H^1$ 型集中だけから節集合の形と個数を保存すること。

## Nelson 表示との関係

節外で

```math
\boldsymbol v
=
\frac{
\nabla S
}{
m
},
\qquad
\boldsymbol u
=
\frac{
\hbar_{\rm eff}
}{
2m
}
\nabla
\log\rho
```

と置けば、縮約作用は Nelson の現在速度・浸透速度表示と同じ係数構造を持つ [3--6,30]。これは有効作用の別表示であり、実在する前進・後退 Markov 過程の導出ではない。配置拡散から同じ構造を得る補助経路は付録Dに置く。

## 力学的到達点

本章で得たものは次である。

1. 制限作用上の Madelung 構造。
2. 双対残差とエネルギー残差を仮定した代表複素場とコヒーレント分散の有限時間評価。
3. 流束差上界を仮定した弱密度同期評価。
4. 節を含む大域複素弱形式と、節外の Madelung 表示・条件付き循環量子化。
5. 対称性で保護された固有状態の条件付き包含。

# 位置入口作用殻と Born 型標本化

> **位置づけ：** 一般作用殻容量、2モード殻の線形重み、作用分配次元の剛性は厳密結果である。位置入口頻度には共通流束因子を仮定する。一般 Born 則、初期流束同期、標本化後の再埋め込みは未完成である。


## 一般作用殻容量

$n$個の複素正準モードを

```math
a_k
=
\frac{
q_k+ip_k
}{
\sqrt2
},
\qquad
J_k
=
\left|
a_k
\right|^2
```

とする。固定総作用 $\sum_kJ_k=A$ の未規格化 Liouville 殻容量を

```math
\Omega_n(A)
=
\int
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n
dJ_k
\,d\theta_k
```

と定める。

<!-- theorem-start:theorem -->
**定理（一般作用殻容量）**
$A>0$ に対し、

```math
\Omega_n(A)
=
\frac{
\left(
2\pi
\right)^n
}{
\left(
n-1
\right)!
}
A^{n-1}
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数の積分が $(2\pi)^n$ を与える。残る作用変数は、$J_k\geq0$ と $\sum_kJ_k=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。
<!-- theorem-end:proof -->

位置入口と Bell 比較殻で線形重みを得るには $n=2$ が重要である。

## 排他的な位置入口

有限セルで代表場強度を

```math
q_i
=
\left|
\bar\zeta_i
\right|^2,
\qquad
\sum_i
q_i
\Delta V
=
1
```

とする。全入口作用 $A_{\rm tot}>0$ を

```math
A_i
=
A_{\rm tot}
q_i
\Delta V
```

とセルへ割り当てる。

入口反応面は排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とする。1つの履歴は1つの入口面だけを通過する。他セルの作用殻を同じ履歴について直積しない。

各入口セクターでは、選択された活性モードの作用を $K_i$、全チャンネルで共有する明反応座標の作用を $I$ とし、

```math
K_i+I
=
A_i
```

を課す。作用を直接分配する方向はこの2モードだけであり、残る自由度は付随因子として扱う。

## 正方向 Liouville 流束

$n=2$ の殻容量は

```math
\Omega_2(A_i)
=
\left(
2\pi
\right)^2
A_i
```

である。正方向入口流束を

```math
\mathscr F_i
=
\int_{
\Gamma_{\partial,i}
}
\left(
\dot s_i
\right)_+
d\mu_i
```

とする。$s_i$ は入口面の法線座標である。作用殻の線形容量以外を流束因子 $\lambda_i$ へまとめ、

```math
\mathscr F_i
=
\lambda_i
\Omega_2(A_i)
```

と書く。$\lambda_i$ は、法線速度、障壁透過、入口面の向き、余面積 Jacobian、付随自由度の体積、有限入口窓、解多重度を含む。

## 主定理2

<!-- theorem-start:theorem -->
**定理（2モード作用殻による位置入口標本化）**
次を仮定する。

1. 入口面が排他的な和である。
2. 各入口セクターで2モード総作用が $A_i=A_{\rm tot}q_i\Delta V$ である。
3. 全チャンネルで $\lambda_i=\lambda>0$ である。
4. 各開始履歴を正方向入口通過として1回だけ数える。
5. 結果または位置に応じて失敗履歴を捨てない。

このとき、

```math
P_i
=
\frac{
\mathscr F_i
}{
\sum_j
\mathscr F_j
}
=
q_i
\Delta V
=
\left|
\bar\zeta_i
\right|^2
\Delta V
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $\lambda$ と $\Omega_2(A_i)=(2\pi)^2A_i$ により、

```math
P_i
=
\frac{
A_i
}{
\sum_jA_j
}
```

である。$\sum_jA_j=A_{\rm tot}$ を代入する。
<!-- theorem-end:proof -->

この定理は場強度を確率と定義した結果ではない。入口反応面を横切る Liouville 流束の相対頻度である。

## 共通流束条件からのずれ

基準流束因子 $\lambda>0$ に対し、

```math
\frac{
\lambda_i
}{
\lambda
}
=
1+\delta_i
```

とする。一般には

```math
P_i
=
\frac{
q_i
\Delta V
\left(
1+\delta_i
\right)
}{
\sum_j
q_j
\Delta V
\left(
1+\delta_j
\right)
}
```

である。主要な標本化誤差を

```math
\varepsilon_{\rm sample}
=
\max_i
\left|
\delta_i
\right|
```

とすれば、

```math
P_i
=
q_i
\Delta V
+
O
\left(
\varepsilon_{\rm sample}
\right)
```

となる。位置依存の障壁と法線速度だけでなく、余面積 Jacobian、付随体積、入口分解能、解多重度も共通でなければならない。

## 作用分配次元の剛性

活性モードに加えて、作用を直接受け取る独立な明反応方向が $d_{\rm A}$ 個あるとする。固定総作用殻は $d_{\rm A}+1$ モードなので、

```math
\Omega_{
d_{\rm A}+1
}
(A_i)
\propto
A_i^{d_{\rm A}}
```

である。

<!-- theorem-start:proposition -->
**命題（直接作用分配次元の剛性）**
共通流束因子の下で、

```math
P_i
\propto
\left(
q_i
\Delta V
\right)^{d_{\rm A}}
```

となる。線形則には $d_{\rm A}=1$ が必要である。
<!-- theorem-end:proposition -->

追加自由度が時計、混合角、記録、不要情報だけを担い、総作用を直接分配しないなら、共通の付随因子として線形則を壊さない。

## 殻内混合とセクター質量

選択された2モードを $a_i$ とすると、総作用は $A_i=a_i^\dagger a_i$ である。$u(2)$ 生成子 $T_\alpha$ を用いた殻接混合

```math
H_{\rm mix}^{(i)}
=
\varepsilon_{\rm mix}
\chi_i(X)
\sum_\alpha
\xi_\alpha
a_i^\dagger
T_\alpha
a_i
```

は

```math
\left\{
A_i,
H_{\rm mix}^{(i)}
\right\}
=
0
```

を満たす。従って殻内角分布は変えられる。

しかし、正規化された初期集団を Hamiltonian 写像で押し出しても、入口セクターの総確率質量は保存される。殻内混合だけでは、セクター間の質量を $\Omega_2(A_i)$ に比例させられない。主定理2の共通未規格化流束条件は、殻内混合とは独立の仮定である。同じ制限は第5章の Bell 境界殻にも現れる。

## 初期密度同期との関係

主定理2は、入口直後の粒子位置頻度を $q_i\Delta V$ にできる。この意味で、第3章の初期密度同期

```math
\rho(0)
\approx
\left|
\psi(0)
\right|^2
```

の分布部分を供給する候補である。

ただし、次は供給しない。

1. 粒子流束と場流束の同期。
2. 粒子速度分散の小ささ。
3. 位相接続に沿う単流束化。
4. 標本化後の活性場を同じコヒーレント部分空間へ戻す写像。
5. 共有明反応座標と準備浴の反復可能な再初期化。

従って、主定理2が主定理1の全初期条件を準備するとは書かない。

## 一般 Born 則との区別

本章の結果は、次に限定される。

1. 位置入口チャンネルの通過頻度。
2. 1つの直接作用分配方向を持つ2モード殻。
3. チャンネル間で共通な未規格化流束。
4. 場強度に比例する入口前の作用分配。
5. 無条件に数えられる全開始履歴。

任意基底、一般射影測定、連続スペクトルの有限分解能、複合系の一般 Born 則は示していない。位置入口標本化は Born 則の部分達成であり、一般測定理論ではない。

# Bell 対モード、比較器、共通境界測度

> **位置づけ：** 反対称源と局所回転からの余弦枝作用、理想比較転送、2モード殻容量は補助模型内部で厳密である。Bell 共同確率は共通境界測度に依存する条件付き結果であり、その測度を生成する完全周期は未完成である。


## 固定された対モード

Bell 構成でも基本変数は物理空間上の同じ2成分場であり、2粒子配置空間上の独立な場を追加しない。第1章の固定モード分解から、左右へ進む局在モードを

```math
z^A_{\mu r},
\qquad
z^B_{\nu r},
\qquad
\mu,\nu
\in
\left\{
+,-
\right\},
\qquad
r
\in
\left\{
1,2
\right\}
```

とする。$\mu,\nu$ は局所分析器の2出力、$r$ は2つの直交源チャンネルである。設定または結果ごとにモード基底を選び直さない。

左右モードの派生相関を

```math
C_{\mu\nu}
=
\sum_{r=1}^2
\eta_r
z^A_{\mu r}
\left(
z^B_{\nu r}
\right)^*
```

と定める。$C$ は独立した場でも新しい正準変数でもない。基礎場モードから計算される階数2以下の行列である。共通内部回転

```math
z^A
\longmapsto
e^{i\beta}z^A,
\qquad
z^B
\longmapsto
e^{i\beta}z^B
```

に対して $C$ は不変である。

## 反対称源と局所分析器

理想源が準備する相関行列を

```math
C_0
=
\sqrt{
\frac{
\mathcal K
}{
2
}
}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。これは2つの階数1項へ分解できるため、2つの直交源チャンネルで構成できる。有限 Hamiltonian 源が任意初期状態から $C_0$ を準備することと、比較時刻まで相対位相を保つことは独立の準備問題である。

設定 $a,b$ に対応するモード角を $\alpha_a,\alpha_b$ とする。左右の局所分析器は基礎場モードだけを

```math
z^{A,(r)}
\longmapsto
R(\alpha_a)
z^{A,(r)},
\qquad
z^{B,(r)}
\longmapsto
R(\alpha_b)
z^{B,(r)}
```

と回転する。ここで

```math
R(\alpha)
=
\begin{pmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{pmatrix}
```

である。相関表示は

```math
C(a,b)
=
R(\alpha_a)
C_0
R(\alpha_b)^{\mathsf T}
```

となるが、物理的に回すのは左右の局所モードである。

局所正準座標 $(Q^A_{\mu r},P^A_{\mu r})$ に対する回転生成子を

```math
G_A
=
\sum_r
\left(
Q^A_{+r}P^A_{-r}
-
Q^A_{-r}P^A_{+r}
\right)
```

とすれば、$H_A=\dot\alpha_aG_A$ がA側だけを回転する。B側も同様であり、分析器 Hamiltonian は空間的に分離した局所和である。

## 余弦枝作用

結果 $A,B\in\{+1,-1\}$ に対応する基底を $e_A,e_B$ とし、

```math
C_{AB}(a,b)
=
e_A^{\mathsf T}
C(a,b)
e_B,
\qquad
K_{AB}
=
\left|
C_{AB}
\right|^2
```

と定める。

<!-- theorem-start:theorem -->
**定理（反対称対モードの Bell 余弦枝作用）**
反対称源と左右の実回転の下で、

```math
K_{AB}
=
\frac{
\mathcal K
}{
4
}
\left[
1
-
AB
\cos
\Delta_{ab}
\right],
\qquad
\Delta_{ab}
=
2
\left(
\alpha_a-\alpha_b
\right)
```

が成立する。さらに、

```math
\sum_{A,B}
K_{AB}
=
\mathcal K,
\qquad
\sum_B
K_{AB}
=
\sum_A
K_{AB}
=
\frac{
\mathcal K
}{
2
}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$\delta=\alpha_a-\alpha_b$ とする。行列積を計算すると、

```math
K_{++}
=
K_{--}
=
\frac{
\mathcal K
}{
2
}
\sin^2\delta,
\qquad
K_{+-}
=
K_{-+}
=
\frac{
\mathcal K
}{
2
}
\cos^2\delta
```

となる。$\cos2\delta=\cos\Delta_{ab}$ を用いる。
<!-- theorem-end:proof -->

この定理は設定依存の枝作用を与えるが、結果頻度をまだ与えない。

光子偏光型では $\alpha_a=a$、$\alpha_b=b$ とすれば $\Delta_{ab}=2(a-b)$ となる。平面内スピン型では $\alpha_a=a/2$、$\alpha_b=b/2$ とすれば $\Delta_{ab}=a-b$ となる。モード角と装置表示角を区別する。

## 局所記録と共通未来

本稿の局所装置は、既に形成された2値結果セクターを出力ポートと指針へ写す最小符号化器である。連続したミクロ状態から安定な唯一結果を形成する一般測定器は構成していない。

左右の戻り信号は局所記録後に有限速度で伝播し、2測定事象の共通未来でだけ合流する。従って、$C_{AB}$ を空間的に離れた測定時刻の瞬間的な局所力へ使わない。

比較振幅の実部と虚部を読む正準対を

```math
\left(
Q_{\rm R},
P_{\rm R}
\right),
\qquad
\left(
Q_{\rm I},
P_{\rm I}
\right)
```

とする。結果セクターを選ぶ滑らかな窓を $\chi_A$、$\chi_B$ とし、

```math
C(s_A,s_B)
=
\sum_{A,B}
\chi_A(s_A)
\chi_B(s_B)
C_{AB}
```

と書く。理想的な排他セクターでは $C(s_A,s_B)=C_{AB}$ である。

## 理想比較転送

比較読み出し Hamiltonian を

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}
\operatorname{Re}
C(s_A,s_B)
+
P_{\rm I}
\operatorname{Im}
C(s_A,s_B)
\right]
```

とする。$\vartheta$ は内部時計角である。比較窓の入口で

```math
Q_{\rm R}
=
P_{\rm R}
=
Q_{\rm I}
=
P_{\rm I}
=
0
```

とし、パルス面積を

```math
\Gamma
=
\int
g_{\rm read}(\vartheta(t))
\,dt
```

とする。

<!-- theorem-start:proposition -->
**命題（理想比較読み出し）**
比較窓で入力相関を一定とみなせる理想極限では、

```math
Q_{\rm R}^{\rm out}
=
\Gamma
\operatorname{Re}
C_{AB},
\qquad
Q_{\rm I}^{\rm out}
=
\Gamma
\operatorname{Im}
C_{AB}
```

となる。$P_{\rm R}=P_{\rm I}=0$ の理想入口では、読み出し Hamiltonian による入力モードへの反作用は零である。
<!-- theorem-end:proposition -->

比較2モードの作用を

```math
J_{\rm R}
=
\frac12
\left(
Q_{\rm R}^2+P_{\rm R}^2
\right),
\qquad
J_{\rm I}
=
\frac12
\left(
Q_{\rm I}^2+P_{\rm I}^2
\right)
```

とし、総比較作用を

```math
A_\partial
=
J_{\rm R}
+
J_{\rm I}
```

とする。

<!-- theorem-start:corollary -->
**系（枝作用の比較作用への転送）**
理想比較後の結果セクターでは、

```math
A_\partial^{AB}
=
\frac{
\Gamma^2
}{
2
}
K_{AB}
```

である。
<!-- theorem-end:corollary -->

## 比較2モード殻

複素比較モードを

```math
c_\nu
=
\frac{
Q_\nu+iP_\nu
}{
\sqrt2
},
\qquad
\nu
\in
\left\{
\mathrm R,
\mathrm I
\right\}
```

とすれば、

```math
A_\partial
=
\left|
c_{\rm R}
\right|^2
+
\left|
c_{\rm I}
\right|^2
```

である。第4章の一般作用殻容量から、

```math
\Omega_2
\left(
A_\partial^{AB}
\right)
=
\left(
2\pi
\right)^2
\frac{
\Gamma^2
}{
2
}
K_{AB}
```

を得る。

$U(2)$ 型の殻接混合は $A_\partial$ を保存し、比較殻上の角分布を変えられる。しかし、正規化された各結果セクターの総確率質量は Hamiltonian 写像で保存される。読み出しと殻内混合だけでは、セクター間の質量を $\Omega_2(A_\partial^{AB})$ に比例させられない。

Bell 頻度には、全結果セクターへ共通の未規格化境界密度または境界流束を置く条件が別に必要である。

## 境界位相空間

1試行の全正準変数を $z\in\Gamma_{\rm all}$ とする。比較境界面を結果ごとの排他的な和

```math
\Gamma_\partial
=
\bigsqcup_{A,B}
\Gamma_\partial^{AB}
```

とする。各 $\Gamma_\partial^{AB}$ では、局所記録は $(A,B)$ を持ち、時計は境界面を正方向に横切り、比較総作用は $A_\partial^{AB}$ である。

結果セクターの未規格化質量を

```math
\begin{aligned}
\widetilde W_{AB}(a,b)
={}&
w_{AB}
\int
\lambda_\partial^{AB}(z;a,b)
\\
&
\times
\delta
\left(
A_\partial^{AB}
-
J_{\rm R}
-
J_{\rm I}
\right)
d\Gamma_{\rm cmp}
d\Gamma_{\rm aux}
\end{aligned}
```

と定める。$d\Gamma_{\rm aux}$ は比較作用を直接分配しない自由度の測度である。

理想共通条件は次である。

1. 基準多重度 $w_{AB}$ が4結果で等しい。
2. 境界密度と時計流束が4結果で共通である。
3. 余面積 Jacobian、付随体積、解多重度が4結果で共通である。
4. 全結果を同じ境界分解能で数える。

共通因子は設定 $a,b$ に依存しても、4結果で同じなら規格化で相殺する。$w_{AB}$ は前向き初期集団の事前確率ではなく、境界 Liouville 要素へ置く共通基準多重度である。

## 主定理3

<!-- theorem-start:theorem -->
**定理（共通境界測度下の Bell 共同確率）**
次を仮定する。

1. 第5.3節の余弦枝作用。
2. 第5.5節の理想比較転送。
3. 第5.7節の共通境界条件。
4. 全結果セクターを無条件に数え、結果依存の失敗履歴を捨てない。

このとき、

```math
P
\left(
A,B
\mid
a,b
\right)
=
\frac{
\widetilde W_{AB}
}{
\sum_{A',B'}
\widetilde W_{A'B'}
}
=
\frac14
\left[
1
-
AB
\cos
\Delta_{ab}
\right]
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通境界因子を $\Lambda_\partial(a,b)>0$ とまとめる。2モード殻容量から

```math
\widetilde W_{AB}
\propto
A_\partial^{AB}
\propto
K_{AB}
```

である。$\sum_{A,B}K_{AB}=\mathcal K$ を用いて規格化する。
<!-- theorem-end:proof -->

これは共通境界条件を置いた後の厳密結果である。境界条件自体を通常の前向き初期分布から導いた結果ではない。

## 非信号周辺と CHSH 値

<!-- theorem-start:corollary -->
**系（対称共通境界測度下の非信号性）**
主定理3の条件の下で、

```math
\sum_B
P
\left(
A,B
\mid
a,b
\right)
=
\frac12,
\qquad
\sum_A
P
\left(
A,B
\mid
a,b
\right)
=
\frac12
```

である。
<!-- theorem-end:corollary -->

共同相関は

```math
E(a,b)
=
\sum_{A,B}
AB
P
\left(
A,B
\mid
a,b
\right)
=
-
\cos
\Delta_{ab}
```

となる。標準4設定では

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
```

を得る。これは平面内2出力の理想余弦則に対する値であり、一般的な Tsirelson 原理の導出ではない。

可視度 $V_{\rm Bell}$ により

```math
E(a,b)
=
-
V_{\rm Bell}
\cos
\Delta_{ab}
```

となる場合、標準角で $|S_{\rm CHSH}|=2\sqrt2V_{\rm Bell}$ である。CHSH不等式を超えるには $V_{\rm Bell}>1/\sqrt2$ が必要である。

## 有限誤差の測度

理想未規格化質量を $cK_{AB}$ とする。実際の未規格化質量 $W_{AB}$ に対し、

```math
\varepsilon_{\rm Bell}
=
\frac{
\sum_{A,B}
\left|
W_{AB}
-
cK_{AB}
\right|
}{
c\mathcal K
}
```

と定める。$\varepsilon_{\rm Bell}<1$ なら、規格化後の共同分布と理想分布の全変動距離は

```math
d_{\rm TV}
\leq
\frac{
\varepsilon_{\rm Bell}
}{
1-\varepsilon_{\rm Bell}
}
```

で抑えられる。この評価は、理想的に $K_{AB}=0$ となる端点でも相対誤差を使わずに済む。

周辺確率の非信号性偏差と各設定対の相関誤差も $O(\varepsilon_{\rm Bell})$ である。CHSH値の誤差は4設定の相関誤差の和で抑える。位相雑音、戻り損失、比較器初期作用、時計面積、結果窓、境界因子の非対称性を $\varepsilon_{\rm Bell}$ へ分解して監査する。

## 完全履歴測度と Bell 前提

設定 $a,b$ を固定した境界値問題の解空間を $\mathcal S_{a,b}$、境界位相点から完結履歴への解写像を

```math
\mathfrak S_{a,b}
:
\Gamma_\partial^{a,b}
\longrightarrow
\mathcal S_{a,b}
```

とする。完全履歴測度は、境界 Liouville 測度を解写像で押し出した

```math
\mu_{\rm hist}^{a,b}
=
\left(
\mathfrak S_{a,b}
\right)_*
\mu_\partial^{a,b}
```

である。

境界面から生成側準備面までの Hamiltonian flowを $\Phi_{T\leftarrow0}^{a,b}$ とすると、生成側へ引き戻した測度は

```math
\mu_{\rm prep}^{a,b}
=
\left(
\Phi_{T\leftarrow0}^{a,b}
\right)^*
\mu_\partial^{a,b}
```

である。境界作用制約が $a,b$ に依存するため、一般に

```math
\rho
\left(
\Lambda
\mid
a,b
\right)
\neq
\rho
\left(
\Lambda
\right)
```

となる。Bell の前提違反は測定設定独立性にある [1,2,7--11,20--23]。

理想局所装置では、

```math
A
=
A
\left(
a,
\Lambda_A
\right),
\qquad
B
=
B
\left(
b,
\Lambda_B
\right)
```

と書ける局所応答を維持する。Bell 違反は設定依存の完全履歴集団から生じる。Bell の定理を否定せず、遠隔設定による瞬間的な測定力も導入しない。

## 比較器の因果的役割

局所結果は戻り信号が比較器へ到達する前に記録できる。通常の前向き因果では、後の比較器は過去の記録を変更しない。本模型もそのような変更を主張しない。

比較器の役割は次の2つである。

1. 完結履歴の $K_{AB}$ を共通未来の局所相互作用として比較作用へ転送する。
2. 二側境界測度を定義する終端自由度を与える。

比較器は過去へ制御信号を送る装置ではなく、生成からリセットまでの全履歴に課す境界条件の物理的終端である。

## 記録、逆計算、未完成の周期

比較後、結果を空の外部記録へ可逆にコピーする。混合の制御履歴と暗モード状態を保持できる理想模型では、

1. 殻内混合を逆実行する。
2. 比較読み出しを逆実行する。
3. 戻り伝播を逆実行する。
4. 局所分析器を逆実行する。
5. 内部指針と比較器を基準状態へ戻す。

ことができる。

異なる結果を外部に残したまま、外部記録を含む全自由度を同じ1点へ戻すことはできない。Hamiltonian flowが1対1だからである [17,18]。反復には記録媒体、不要情報モード、仕事源、弱く結合した環境のいずれかが必要である。

主定理3の境界測度を事後選別なしに準備するには、さらに次が必要である。

1. 設定生成器を含む反復可能な全周期。
2. 一意結果形成と増幅。
3. 全開始数、局所記録数、比較完了数、リセット完了数の一致。
4. 結果依存の失敗試行または停止時間を捨てないこと。
5. 共通境界密度の有限 Hamiltonian・弱開放準備。

これは現模型の測定側で最大の未解決問題である。

# 誤差、反証条件、未解決問題

> **位置づけ：** 個別誤差を準備、縮約、測定、周期の4群へ整理し、主結果の成立範囲と反証条件を明示する。長時間一様評価、節近傍のミクロ縮約、共通境界測度の完全周期は未完成である。


## 4群の誤差

本文の誤差を

```math
\varepsilon_{\rm prep},
\qquad
\varepsilon_{\rm red},
\qquad
\varepsilon_{\rm meas},
\qquad
\varepsilon_{\rm cycle}
```

の4群へまとめる。

| 誤差群 | 主な内訳 | 影響する結論 |
|---|---|---|
| $\varepsilon_{\rm prep}$ | 初期高速欠陥、初期コヒーレント分散、初期密度差、源位相差 | 主定理1の初期条件、Bell 可視度 |
| $\varepsilon_{\rm red}$ | ミクロ弱残差、有限セル、係数不一致、時間依存射影、非線形再励起、流束差、節接続 | 弱 Schrödinger 型方程式、有限時間集中、密度同期 |
| $\varepsilon_{\rm meas}$ | 入口流束因子、分析器角、戻り損失、比較パルス、境界因子、結果窓 | 位置入口重み、Bell 共同分布、非信号性、CHSH値 |
| $\varepsilon_{\rm cycle}$ | 結果依存停止、記録脱落、再埋め込み、補助系再初期化、リセット失敗 | 無条件標本、反復可能性、境界測度の物理的意味 |

4群は単純に同じノルムで加える量ではない。各主定理の結論に対応するノルムまたは確率距離へ写してから評価する。

## 準備誤差

準備誤差の代表量を

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm fast}(0)
+
\varepsilon_{\rm coh}(0)
+
\left\|
\rho(0)-q(0)
\right\|_{H^{-1}}
+
\varepsilon_{\rm source}
```

とする。

局所作用欠陥と動径欠陥については、付録Eの準備近似と付録Fの正定値2次交換が部分的な上界を与える。初期コヒーレント集中、初期流束同期、反対称源の有限 Hamiltonian 準備は未完成である。

有限浴は再帰し、有限温度は欠陥の雑音床を作る。同型交換補助系は高速成分を消去せず移送するだけなので、反復には補助系の再初期化が必要である。準備窓を閉じた後の欠陥再成長も縮約誤差へ入る。

## 縮約誤差

主定理1に直接入る縮約誤差を

```math
\varepsilon_{\rm red}(T)
=
\varepsilon_{\rm mic}^{\rm wk}(T)
+
\varepsilon_{\rm mic}^{\mathcal E}(T)
+
\int_0^T
\left\|
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right\|_{L^2}
\,dt
+
\int_0^T
\left\|
R_{\rm cont}
\right\|_{H^{-1}}
\,dt
```

とする。$\varepsilon_{\rm mic}^{\rm wk}$ と $\varepsilon_{\rm mic}^{\mathcal E}$ の内部には、有限セル誤差、係数不一致、局所作用欠陥、動径欠陥、時間依存射影、非線形再励起を、それぞれのノルムで含める。粒子・場流束差は両残差へ重複計上しない。

節関係は1つの記号へ潰さず、次を分ける。

1. 有効複素弱方程式の形式領域での正則性。
2. 正則化接続 $\boldsymbol a_\varepsilon$ の極限。
3. 密度差と特異接続の重み付き積。
4. 節近傍の粒子質量。
5. 節集合の幾何学的安定性。

1は複素弱形式で扱える。2から5はミクロ位相接続の導出と励起状態の節安定性に必要であり、未完成である。

有限時間評価定数 $C_T$ は一般に $T$ とともに増える。残差の点ごとの小ささまたは全時間一様な局所2次残差だけでは、軌道位相差の長時間蓄積を排除しない。本稿は長時間一様極限を主張しない。

## 位置入口の測定誤差

位置入口では、理想流束因子からのずれを

```math
\frac{
\lambda_i
}{
\lambda
}
=
1+\delta_i
```

とし、

```math
\varepsilon_{\rm pos}
=
\max_i
\left|
\delta_i
\right|
```

で測る。法線速度、障壁、余面積 Jacobian、付随体積、有限窓、解多重度の位置依存が $\delta_i$ を作る。

入力作用分配自体が

```math
A_i
=
A_{\rm tot}
q_i
\Delta V
+
\Delta A_i
```

なら、$\Delta A_i/A_{\rm tot}$ も位置重みへ1次で入る。作用を直接分配する明方向が2つ以上あれば、誤差ではなくべき指数そのものが変わり、線形則は成立しない。

## Bell 測定誤差

Bell 側では、第5章の

```math
\varepsilon_{\rm Bell}
=
\frac{
\sum_{A,B}
\left|
W_{AB}
-
cK_{AB}
\right|
}{
c\mathcal K
}
```

を中心に使う。内訳は次である。

1. 反対称源の振幅・位相誤差。
2. 左右分析器角と局所性の誤差。
3. 戻りモードの損失、分散、交差混合。
4. 比較器初期作用とパルス面積。
5. 結果窓の重なり。
6. 境界密度、時計流束、余面積因子、解多重度の結果依存性。
7. 結果依存の比較失敗または停止時間。

6と7は非信号周辺を直接壊し得る。位相雑音だけが対称に可視度を下げる理想化では、

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
V_{\rm Bell}
```

であり、$V_{\rm Bell}>1/\sqrt2$ が Bell 違反の必要条件である。

## 周期誤差と全試行監査

開始数、局所記録数、比較完了数、外部記録数、リセット完了数をそれぞれ

```math
N_{\rm start},
\quad
N_{\rm local},
\quad
N_{\rm cmp},
\quad
N_{\rm mem},
\quad
N_{\rm reset}
```

とする。無条件な実験標本として境界測度を解釈するには、結果別に

```math
N_{\rm start}^{AB}
\simeq
N_{\rm local}^{AB}
\simeq
N_{\rm cmp}^{AB}
\simeq
N_{\rm mem}^{AB}
\simeq
N_{\rm reset}^{AB}
```

を監査しなければならない。

比較後に適合履歴だけを残す操作、結果依存の停止時間、記録脱落、リセット失敗を無視すると、共通境界測度の条件付き定理を実験的な無条件頻度と誤認する。$\varepsilon_{\rm cycle}$ は単なる装置効率ではなく、結果依存性を含めて評価する。

## 導出状態の一覧

| 対象 | 現在の導出状態 | 主要な未解決部分 |
|---|---|---|
| 有限セル極座標の正準性 | 厳密結果 | 節上では極座標を使わない |
| 固定作用平方分解 | 厳密結果 | 吸引を含まない |
| 有限特異 Hamiltonian の低速枝 | 厳密結果・成立条件 | 一般初期値の一様収束 |
| 準備浴の欠陥減衰 | 近似結果 | 動的振幅、有限温度、再帰、切断後 |
| 正定値2次模型の2帯分離と交換 | 厳密結果・成立条件 | 半正定値方向、大域射影、非線形 |
| 縮約集合上の Madelung 作用 | 厳密結果・仮説依存 | 集合の準備と維持 |
| 有限時間弱縮約 | 近似結果・仮説依存 | ミクロ残差上界 |
| 弱密度同期 | 厳密評価・仮説依存 | 流束差上界 |
| 節を含む複素弱形式 | 厳密な表現 | ミクロ接続の節横断極限 |
| 固有状態の条件付き包含 | 厳密な系 | 状態選択、節変形 |
| 位置入口作用殻 | 厳密結果・仮説依存 | 共通流束の準備、再埋め込み |
| Bell余弦枝作用と比較転送 | 厳密結果・仮説依存 | 反対称源、一般結果形成 |
| 共通境界測度下の Bell 統計 | 厳密結果・仮説依存 | 境界測度の物理的準備 |

## 否定的結果と適用限界

本論文から次が従う。

1. 高速整合だけではコヒーレント集中しない。
2. コヒーレント集中だけでは粒子・場同期しない。
3. 連続の式だけでは流束同期を保存できない。
4. 複素弱形式を使うだけでは、ミクロ位相接続の節横断導出は完成しない。
5. $H^1$ 型集中だけでは節集合の形と個数を保存できない。
6. 固有状態を解として含むことは、その状態を選択または吸引することではない。
7. $\kappa=\mathcal J_\phi^2/(2m)$ は内部回転対称性だけから従わない。
8. 位置入口作用殻は一般 Born 則ではない。
9. 正規化された殻内混合はセクター間の確率質量を作らない。
10. 低ランク相関と局所回転だけでは Bell 頻度を作らない。
11. 共通未来比較器は過去の記録を前向きに変更しない。
12. Bell 共同頻度には共通境界測度が必要である。
13. Bell 違反は測定設定独立性を満たさない完全履歴集団で生じる。
14. 異なる記録を残したまま全自由度を同じ位相点へ戻す完全リセットは Hamiltonian ではない。
15. 配置拡散・Nelson 経路は現行模型の前提ではない。

## 反証に使える観測量

力学側では次を測る。

1. $\varepsilon_{\rm coh}(t)$。
2. 高速欠陥ノルム。
3. $\|R_{\rm red}\|_{L^1(0,T;\mathcal Q^*)}$ と、コヒーレント安定性に用いるエネルギー残差。
4. $\|\rho-q\|_{H^{-1}}$。
5. $\|\boldsymbol J_{\rm p}-\boldsymbol j_\psi\|$ の時間積分。
6. 節近傍の重み付き接続誤差。
7. 有限セル幅、正則化幅、特異パラメータに対する収束。

調和井戸の基底状態だけでは節を検査できない。最初の節付き検証には、奇対称部分空間の第1励起状態が適している。続いて非調和井戸、対称2重井戸、非対称井戸、時間依存外力を比較する。

測定側では次を測る。

1. 位置入口流束因子の位置依存。
2. 4結果セクターの未規格化境界因子。
3. 全変動距離 $d_{\rm TV}$。
4. 一側周辺の遠隔設定依存。
5. 可視度と CHSH 値。
6. 結果別の開始、記録、比較、リセット完了率。

共通因子または全試行監査が破れれば、理想確率式は棄却される。

## 最重要の未解決問題

優先順位は次である。

1. 現行 M0 の有限時間発展から $\varepsilon_{\rm mic}^{\rm wk}(T)$ と $\varepsilon_{\rm mic}^{\mathcal E}(T)$ を導く。
2. 半正定値位相 Hessian と零モードを含む低速・高速分離を示す。
3. 時間依存射影と非線形高速再励起を制御する。
4. 粒子速度分散と接続追従から流束差上界を導く。
5. 節近傍の粒子質量、重み付き同期、正則化極限を制御する。
6. 初期コヒーレント集中を有限 Hamiltonian 準備で作る。
7. 位置入口標本化後の活性場をコヒーレント部分空間へ再埋め込みする。
8. 反対称対モード源と長時間位相保持を構成する。
9. 共通境界密度を事後選別なしに準備する。
10. 設定生成、結果形成、増幅、記録、比較、リセットを1周期へ統合する。

## 結論

本論文の力学的な前進は、節を避けた局所 Madelung 表示を中心にする構成から、複素場のエネルギー集中と大域弱形式を中心にする構成へ移したことである。これにより、節を持つ有効解と対称性で保護された励起状態を条件付きで含められる。

同時に、主張を強めすぎないよう、ミクロ弱残差と流束差を独立の仮定として明示した。現行稿は、残差が小さい場合の有限時間安定性を示すが、節近傍を含む現行 M0 から残差上界をまだ導いていない。

位置入口標本化と Bell 統計は、2モード作用殻の線形容量という共通の有限次元構造を使う。ただし、殻容量とセクター間の確率質量は同じではない。位置側では共通入口流束、Bell 側では共通境界測度が必要である。

従って現在の到達点は、古典 Hamiltonian 構成から量子力学に似た有効力学と確率構造を得るための、条件、誤差、否定的結果を監査可能な形で分離した段階である。無条件な完全導出ではない。

# 付録

# 有限セル正準変換と弱縮約評価の詳細

> **位置づけ：** 第2章と第3章の正準変換、固定作用最小化、縮約作用の変分、射影的代表場、有限時間安定性、弱密度同期を補足する。


## 極座標正準変換

各セルで

```math
\boldsymbol\Phi
=
r e_r,
\qquad
e_r
=
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix},
\qquad
e_\theta
=
\begin{pmatrix}
-\sin\theta\\
\cos\theta
\end{pmatrix}.
```

運動量を

```math
\boldsymbol\Pi
=
p_r e_r
+
\frac jr e_\theta
```

と分解する。すると

```math
d\boldsymbol\Phi
=
e_r\,dr
+
r e_\theta\,d\theta
```

なので、

```math
\boldsymbol\Pi\cdot d\boldsymbol\Phi
=
p_r\,dr
+
j\,d\theta.
```

従ってシンプレクティック2形式も

```math
d\boldsymbol\Pi\wedge d\boldsymbol\Phi
=
dp_r\wedge dr
+
dj\wedge d\theta
```

となる。$r=0$ では極座標が特異であるため、この変換を使う領域は $r>0$ に限定する。

## 固定作用最小化の Lagrange 乗数表示

固定振幅 $(r_i)$ の下で

```math
E_{\rm rot}
=
\sum_i
\frac{j_i^2}{2Ir_i^2}
\Delta V
```

を、制約

```math
\sum_i j_i\Delta V
=
\mathcal J_\phi
```

の下で最小化する。Lagrange 乗数を $\Lambda$ とすると、

```math
\frac{\partial}{\partial j_i}
\left[
E_{\rm rot}
-
\Lambda
\sum_kj_k\Delta V
\right]
=
\left(
\frac{j_i}{Ir_i^2}
-
\Lambda
\right)
\Delta V
=
0.
```

従って

```math
j_i
=
I\Lambda r_i^2.
```

規格化 $\sum_i r_i^2\Delta V=1$ と全作用制約から

```math
I\Lambda
=
\mathcal J_\phi.
```

よって $j_i=\mathcal J_\phi r_i^2$ を得る。Hessian は対角で

```math
\frac{\partial^2E_{\rm rot}}{\partial j_i\partial j_k}
=
\frac{\Delta V}{Ir_i^2}
\delta_{ik}
```

であり、$I>0$ と $r_i>0$ の下で正定値である。

## 連続極限と節正則化

連続表示の回転エネルギーは

```math
E_{\rm rot}
=
\int
\frac{j^2}{2Ir^2}
\,dx.
```

$r=0$ では特異なので、有限正則化では

```math
E_{\rm rot}^{(\varepsilon)}
=
\int
\frac{j^2}{2I(r^2+\varepsilon^2)}
\,dx
```

を使える。しかし、この正則化では最小配置が厳密な $j=\mathcal J_\phi r^2$ からずれる。接続だけを正則化して回転エネルギーの特異性を放置してはならない。

節から離れた領域

```math
r^2
\geq
c_{\rm node}
>
0
```

では、

```math
\left|
\frac{r^2}{r^2+\varepsilon^2}
-
1
\right|
\leq
\frac{\varepsilon^2}{c_{\rm node}}
```

なので、接続誤差は一様に制御できる。節を含む極限は別問題である。

## 位相接続の内部回転不変性

共通内部回転

```math
\boldsymbol\Phi
\mapsto
R(\alpha)\boldsymbol\Phi
```

の下で、行列式型の分子

```math
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
```

と分母 $|\boldsymbol\Phi|^2+\varepsilon^2$ は不変である。従って $\mathbf a_\varepsilon$ も不変である。

$\mathcal J_\phi$ はこの回転の生成子なので、全 Hamiltonian が共通回転不変なら Noether 量として保存される。固定 $\mathcal J_\phi$ sectorへの制限は、保存量の値を選ぶことであり、Hamiltonianへ外部パラメータを追加することではない。

## 粒子 Legendre 変換

```math
H_{\rm p}
=
\frac{
|P-\mathcal J_\phi\mathbf a|^2
}{
2m
}
+
V
```

から

```math
\dot X
=
\frac{
P-\mathcal J_\phi\mathbf a
}{
m
}
```

を得る。従って $P=m\dot X+\mathcal J_\phi\mathbf a$ であり、

```math
P\cdot\dot X
-
H_{\rm p}
=
\frac m2|\dot X|^2
+
\mathcal J_\phi\mathbf a\cdot\dot X
-
V.
```

接続項の符号は正である。$S=-\mathcal J_\phi\theta$ と定めることで、縮約作用の位相項は $-\rho(\partial_tS+v\cdot\nabla S)$ となる。

## 縮約作用の変分

作用密度を

```math
\mathcal L
=
\frac m2\rho|v|^2
-
\rho V
-
\rho\partial_tS
-
\rho v\cdot\nabla S
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
```

とする。

$S$ 変分では、

```math
\delta_S\mathcal A
=
\int
\left[
-\rho\partial_t\delta S
-
\rho v\cdot\nabla\delta S
\right]
\,dx\,dt
```

を部分積分し、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0
```

を得る。

$v$ 変分では、

```math
\delta_v\mathcal A
=
\int
\rho
\left(
mv-\nabla S
\right)
\cdot\delta v
\,dx\,dt,
```

従って $mv=\nabla S$ である。

$q=\sqrt\rho$ と置くと、

```math
\delta
\left[
-
\kappa
\int
|\nabla q|^2
\,dx
\right]
=
2\kappa
\int
\delta q\,\Delta q
\,dx.
```

$\delta\rho=2q\delta q$ から、$\rho$ に関する汎関数微分は

```math
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

この符号を使うと Hamilton--Jacobi 式の量子ポテンシャルは

```math
-\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

となる。

## 同期差保存の仮定

位相変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得るため、残余場 Hamiltonian $H_{\rm residual}$ に必要な条件は

```math
\frac{
\delta H_{\rm residual}
}{
\delta\theta
}
=
0
```

である。共通位相の定数回転に対する不変性だけではこの条件に足りない。$r^2|\nabla\theta|^2$ の独立な場エネルギーを残すと、位相流束が追加される。

従って第3章の理想同期差保存は、位相勾配エネルギーを粒子流速の運動エネルギーへ吸収し、残差を $\varepsilon_{\rm cross}$ または $\varepsilon_{\rm press}$ へ含めた縮約に限定される。この非重複条件では、付録Fの位相 Hessian $B$ が半正定値または零になり得るため、正定値2帯定理を直接適用できない。

## 変分縮約の限界

ミクロ作用を多様体へ制限してから変分する操作と、ミクロ方程式を解いてから粗視化する操作は一般に交換しない。必要なのは、少なくとも次のいずれかである。

1. 縮約多様体が近似不変であり、法線方向残差が小さい。
2. 高速法線モードを断熱消去し、有効作用の誤差を評価できる。
3. 弱開放縮約が法線方向だけを安定化し、接方向の Hamiltonian 構造を保つ。

付録Fは、正定値定数係数2次模型について2と3の一部を具体化し、高速法線成分を同型補助系へ移した後の局所縮約残差を $O(\epsilon_{\rm s})$ に抑える。ただし、現行作用に必要な半正定値位相 Hessian、粒子-場混合、時間依存射影、非線形再励起を含む一様誤差定理は与えない。

## 射影的代表場

複素 Hilbert 空間 $\mathcal Q$ の単位球面上で、共通位相を同一視した距離を

```math
d_{\rm pr}
\left(
u,v
\right)
=
\inf_{
\alpha\in
\left[
0,2\pi
\right)
}
\left\|
u-e^{i\alpha}v
\right\|_{\mathcal E_V}
```

とする。基準場 $v_0$ と各標本の重なりが零でなければ、

```math
\left\langle
v_0,
e^{-i\alpha_\omega}u^\omega
\right\rangle
>
0
```

となる位相 $\alpha_\omega$ を局所的かつ連続に選べる。位相整合平均を

```math
m
=
\mathbb E_\omega
\left[
e^{-i\alpha_\omega}
u^\omega
\right]
```

とする。$\|m\|_{L^2}>0$ なら、

```math
\bar u
=
\frac{
m
}{
\left\|
m
\right\|_{L^2}
}
```

を代表場にできる。分散が十分小さい範囲では、基準場の取り方を小さく変えても代表射影点の差は分散と同じ次数である。

各時刻で無関係に $\alpha_\omega$ を選ぶと時間微分が定まらない。初期位相から連続に追跡し、

```math
\left\langle
\bar u,
\partial_t\bar u
\right\rangle
\in
i\mathbb R
```

を許す。この純虚成分が第3章の実数共通位相項 $\lambda(t)$ に対応する。

## 共通線形発展に対する有限時間安定性

$U(t,s)$ を $H_V(t)$ が生成する発展作用素とし、

```math
\left\|
U(t,s)
\right\|_{
\mathcal E_V
\to
\mathcal E_V
}
\leq
C_T
```

を $0\leq s\leq t\leq T$ で仮定する。位相整合した2標本 $u^\omega$、$u^{\omega'}$ が

```math
i\hbar_{\rm eff}
\partial_tu^\omega
=
H_V(t)u^\omega
+
R^\omega
```

を満たすなら、Duhamel 公式から

```math
\begin{aligned}
u^\omega(t)-u^{\omega'}(t)
={}&
U(t,0)
\left[
u^\omega(0)-u^{\omega'}(0)
\right]
\\
&
-
\frac i{
\hbar_{\rm eff}
}
\int_0^t
U(t,s)
\left[
R^\omega(s)-R^{\omega'}(s)
\right]
\,ds.
\end{aligned}
```

従って

```math
\begin{aligned}
&
\left\|
u^\omega(t)-u^{\omega'}(t)
\right\|_{\mathcal E_V}
\\
&\qquad
\leq
C_T
\left\|
u^\omega(0)-u^{\omega'}(0)
\right\|_{\mathcal E_V}
+
\frac{
C_T
}{
\hbar_{\rm eff}
}
\int_0^t
\left[
\left\|
R^\omega(s)
\right\|_{\mathcal E_V}
+
\left\|
R^{\omega'}(s)
\right\|_{\mathcal E_V}
\right]
\,ds.
\end{aligned}
```

標本対について2乗平均を取り、Minkowski 不等式を使えば、第3章のコヒーレント分散評価を得る。ここでは残差のエネルギーノルム上界が必要であり、$\mathcal Q^*$ 上界だけでは足りない。

代表場の弱方程式は位相整合平均 $m$ を微分して得る。$\|m(t)\|_{L^2}\geq c_m>0$ を仮定すると、$\bar u=m/\|m\|_{L^2}$ の微分に現れる規格化項も平均残差の $\mathcal Q^*$ ノルムで評価できる。規格化後の全強制項は単位球面の接空間に入り、その $i\bar u$ 方向を実数共通位相項 $\lambda(t)\bar u$、残りを $R_{\rm red}$ と分ける。従って双対残差の上界は定数 $C_T$ に $c_m^{-1}$ を含む。規格化項だけを実数位相項と同一視しない。

この評価が使えるのは、各標本に対する共通線形主部と残差表示が既に得られた後である。ミクロ Hamiltonian から $R^\omega$ を小さくする部分を置き換えない。

## 強度と場流束の積評価

$u,v\in H^1$ とする。点ごとの恒等式

```math
\left|
u
\right|^2
-
\left|
v
\right|^2
=
\left(
u-v
\right)^*u
+
v^*
\left(
u-v
\right)
```

から、

```math
\left\|
\left|
u
\right|^2
-
\left|
v
\right|^2
\right\|_{L^1}
\leq
\left(
\left\|
u
\right\|_{L^2}
+
\left\|
v
\right\|_{L^2}
\right)
\left\|
u-v
\right\|_{L^2}
```

を得る。

場流束の差は

```math
u^*\nabla u
-
v^*\nabla v
=
\left(
u-v
\right)^*
\nabla u
+
v^*
\nabla
\left(
u-v
\right)
```

なので、

```math
\begin{aligned}
\left\|
\operatorname{Im}
\left(
u^*\nabla u
-
v^*\nabla v
\right)
\right\|_{L^1}
\leq{}&
\left\|
u-v
\right\|_{L^2}
\left\|
\nabla u
\right\|_{L^2}
\\
&
+
\left\|
v
\right\|_{L^2}
\left\|
\nabla
\left(
u-v
\right)
\right\|_{L^2}.
\end{aligned}
```

一様 $H^1$ 上界の下で、エネルギーノルム集中は強度と場流束の $L^1$ 集中を与える。

## 弱密度差評価

差の連続の式を

```math
\partial_t
\delta\rho
+
\nabla
\cdot
\delta\boldsymbol J
=
R_{\rm cont}
```

とする。時間積分すると、

```math
\delta\rho(t)
=
\delta\rho(0)
-
\int_0^t
\nabla
\cdot
\delta\boldsymbol J(s)
\,ds
+
\int_0^t
R_{\rm cont}(s)
\,ds.
```

発散作用素の有界性

```math
\left\|
\nabla
\cdot
\boldsymbol F
\right\|_{H^{-1}}
\leq
\left\|
\boldsymbol F
\right\|_{L^2}
```

を用いれば、

```math
\left\|
\delta\rho(t)
\right\|_{H^{-1}}
\leq
\left\|
\delta\rho(0)
\right\|_{H^{-1}}
+
\int_0^t
\left\|
\delta\boldsymbol J(s)
\right\|_{L^2}
\,ds
+
\int_0^t
\left\|
R_{\rm cont}(s)
\right\|_{H^{-1}}
\,ds.
```

これは流束差を入力とした密度差評価であり、流束差自体の発展方程式ではない。

## 節を含む弱形式と接続極限

$\psi\in L^2(0,T;\mathcal Q)$、$\partial_t\psi\in L^1(0,T;\mathcal Q^*)$ なら、Schrödinger 型方程式は節集合を除外せず弱形式で定義できる。運動エネルギーは

```math
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\int
\left|
\nabla\psi
\right|^2
\,dx
```

として有限であり、$\Delta\sqrt q/\sqrt q$ を節上で点ごとに評価する必要はない。

一方、ミクロ接続項には

```math
\rho
\frac{
\operatorname{Im}
\left(
\zeta^*
\nabla\zeta
\right)
}{
\left|
\zeta
\right|^2
+
\varepsilon^2
}
```

が現れる。$\rho=|\zeta|^2$ が厳密なら分母との相殺を使えるが、$\rho-|\zeta|^2$ が $H^{-1}$ または $L^1$ で小さいだけでは、節近傍の積を一様に抑えられない。必要なのは、例えば

```math
\int_0^T
\int
\frac{
\left|
\rho
-
\left|
\zeta
\right|^2
\right|
}{
\left|
\zeta
\right|^2
+
\varepsilon^2
}
\left|
\operatorname{Im}
\left(
\zeta^*
\nabla\zeta
\right)
\right|
\,dx\,dt
\longrightarrow
0
```

のような重み付き評価である。本稿はこの極限を仮定した弱残差へ含め、現行 M0 からの導出済み結果とはしない。

# 一般作用殻、余面積公式、入口流束の詳細

> **位置づけ：** 第4章と第5章で用いる2モード作用殻容量、排他的境界面、余面積 Jacobian、作用分配次元、殻接方向混合を補足し、正規化された混合集団と未規格化殻容量を区別する。


## 単体積分

作用殻容量を

```math
\Omega_n(A)
=
(2\pi)^n
\int_{J_k\geq0}
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n dJ_k
```

とする。$n=1$ では

```math
\Omega_1(A)
=
2\pi.
```

再帰関係

```math
\Omega_n(A)
=
2\pi
\int_0^A
\Omega_{n-1}(A-J_n)
\,dJ_n
```

を用いると、

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
A^{n-1}
```

が帰納的に従う。

## 排他的な和と直積の違い

位置チャンネルを排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とすれば、全入口流束は

```math
\mathscr F
=
\sum_i\mathscr F_i
```

であり、各 $\mathscr F_i$ に局所作用 $A_i$ の線形因子が残る。

一方、全セルに独立な2モード作用殻を同時に課す直積構成では、容量は

```math
\prod_i\Omega_2(A_i)
\propto
\prod_iA_i
```

となる。1つのチャンネル $i$ を選ぶ相対重みではなく、全セル作用の積が現れる。この構成は位置の Born 型入口頻度を与えない。

## coarea公式

全入口正準位相空間を $\Gamma$、基準体積を $d\Gamma$ とする。固定作用制約と反応面制約を

```math
F_1(z)
=
A_i-K_i-I,
```

```math
F_2(z)
=
s_i(z)
```

とする。正方向流束は記号的に

```math
\mathscr F_i
=
\int_\Gamma
\rho_0(z)
\delta(F_1)
\delta(F_2)
\left(
\dot s_i
\right)_+
d\Gamma.
```

一般の滑らかな写像 $F=(F_1,F_2)$ に対し、coarea公式は

```math
\int_\Gamma
g(z)
\delta(F(z))
d\Gamma
=
\int_{F^{-1}(0)}
\frac{g(z)}{J_F(z)}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

従って共通流束因子には、$\dot s_i$ だけでなく $J_F^{-1}$、初期密度、解多重度、spectator体積が含まれる。

## 2モード殻の明示積分

理想作用角座標では、

```math
\int_0^\infty dK
\int_0^\infty dI
\,
\delta(A-K-I)
=
\int_0^A dK
=
A.
```

角積分を加えると、

```math
\Omega_2(A)
=
(2\pi)^2A.
```

入口法線速度と spectator因子が作用分配座標 $(K,I)$ に依存しない理想模型では、流束はこの容量に比例する。

## 有限入口幅

デルタ関数の代わりに偶関数窓

```math
K_{\delta_A}(y)
=
\frac1{\delta_A}
K
\left(
\frac y{\delta_A}
\right),
```

```math
\int K(y)\,dy=1,
\qquad
\int yK(y)\,dy=0
```

を用いる。理想2モード容量は $A$ に線形なので、窓が $A=0$ の端へ触れず、他の因子が一定なら、対称な有限幅平均は線形重みを変えない。

一般の滑らかな流束因子 $g(A)$ を含むと、

```math
\mathscr F_i^{(\delta_A)}
=
\mathscr F_i^{(0)}
+
O
\left(
\delta_A^2
\sup
\left|
\partial_A^2
\left[
Ag(A)
\right]
\right|
\right).
```

殻端の切断、非対称窓、結果依存幅では1次誤差が現れ得る。

## 作用分配方向の数

活性モード $K$ と $q$ 個の明反応作用 $I_1,\ldots,I_q$ が

```math
K+\sum_{\alpha=1}^qI_\alpha
=
A
```

を分配すると、

```math
\int_{K,I_\alpha\geq0}
\delta
\left(
A-K-\sum_\alpha I_\alpha
\right)
dK
\prod_\alpha dI_\alpha
=
\frac{A^q}{q!}.
```

従って線形則には $q=1$ が必要である。$q>1$ の追加明モードを導入しながら線形 Born 型重みを保つには、それらを直接作用分配から外し、共通 spectator因子にしなければならない。

## 殻接方向 Hamiltonian

$n$モード複素ベクトル $a$ と Hermitian 行列 $T_\alpha$ に対し、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を生成子とする。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とすれば、

```math
\dot a
=
-iT_\alpha a,
```

```math
\left\{
a^\dagger a,
L_\alpha
\right\}
=
0.
```

従って

```math
H_{\rm mix}
=
\varepsilon
\sum_\alpha
\xi_\alpha(z_{\rm D})
L_\alpha
```

は総作用殻に接する Hamiltonian 混合を与える。

暗モードの相関が短く、生成子方向が等方なら、弱結合縮約は概念的に

```math
\mathcal L_{\rm eff}
=
D
\sum_\alpha
X_{L_\alpha}^2
```

となる。現行模型で用いる2モード全殻では $U(2)$ の Casimir型拡散に対応する。有限暗モードからこの生成子を一様誤差付きで導くことは未完成である。

## Born側とBell側の2モード殻

| 用途 | 全殻 | 比較する量 | 線形因子 |
|---|---|---|---|
| Born 型位置入口 | 活性＋共有明反応座標の2モード殻 | 位置sectorごとの全殻容量 | $A_i$ |
| Bell 型共同統計 | 実部＋虚部の比較2モード殻 | 結果sectorごとの全殻容量 | $A_\partial^{AB}$ |

両者は同じ2モード全殻の線形容量を使う。違いは、Born 側の総作用が局所場強度 $A_i=A_{\rm tot}r_i^2\Delta V$ で決まり、Bell 側の総作用が比較読み出し $A_\partial^{AB}=\Gamma^2K_{AB}/2$ で決まる点にある。

## 正規化された混合集団と殻容量

固定sector $\lambda$ の正規化測度を $\mu_\lambda$、正準写像を $\mathcal U_\lambda$ とする。押し出し測度は

```math
\mu_\lambda'
=
\left(
\mathcal U_\lambda
\right)_*
\mu_\lambda
```

である。

<!-- theorem-start:proposition -->
**命題（正準混合によるsector質量保存）**
正準写像がsector $\Gamma_\lambda$ を自身へ写すなら、

```math
\mu_\lambda'
\left(
\Gamma_\lambda
\right)
=
\mu_\lambda
\left(
\Gamma_\lambda
\right).
```

特に $\mu_\lambda$ が規格化されていれば、$U(2)$ 混合後もsector総質量は1であり、$\Omega_2(A_\lambda)$ には比例しない。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
押し出し測度の定義から、

```math
\mu_\lambda'
\left(
\Gamma_\lambda
\right)
=
\mu_\lambda
\left(
\mathcal U_\lambda^{-1}
\Gamma_\lambda
\right).
```

$\mathcal U_\lambda^{-1}\Gamma_\lambda=\Gamma_\lambda$ を用いる。
<!-- theorem-end:proof -->

一方、未規格化 Liouville 殻容量は

```math
\Omega_2(A_\lambda)
=
\int
\delta
\left(
A_\lambda-J_1-J_2
\right)
d\Gamma
```

であり、異なる半径の殻を同じ密度で数えるときの測度である。従って、容量比例頻度には、sectorごとに別々に規格化した集団ではなく、全sectorへ共通の境界密度または流束を置く必要がある。

## 流束規格化と全試行監査

位置入口または Bell 結果の確率を

```math
P_\lambda
=
\frac{\mathscr F_\lambda}{\sum_{\lambda'}\mathscr F_{\lambda'}}
```

と定義するには、分母が全開始試行の入口通過を数えなければならない。次を監査する。

1. 各開始試行は高々1つの排他的境界面を正方向に横切る。
2. 境界へ到達しない試行を無言で除外しない。
3. 複数回交差を1試行としてどう数えるかを固定する。
4. 結果別に異なる停止時間または滞在時間を頻度へ重複計上しない。
5. 記録失敗、再埋め込み失敗、再初期化失敗を結果依存に捨てない。
6. 局所記録数、比較完了数、外部記録数、reset完了数を結果別に監査する。
7. Bell 側では設定生成に失敗した周期も無言で除外しない。

これらを満たさなければ、作用殻容量が正しくても実験の無条件頻度にはならない。数学的な境界測度が全履歴を数えることと、実験準備がその測度を事後選別なしで生成することは別である。

## 再埋め込み写像に必要な保存量

標本化後の状態を $z_{\rm post}$、次試行の準備面を $\Gamma_{\rm prep}$ とする。理想的な再埋め込み写像

```math
\mathcal U_{\rm reset}:
z_{\rm post}
\longmapsto
z_{\rm next}\in\Gamma_{\rm prep}
```

は、拡大全系で正準かつ1対1でなければならない。結果情報を消去する場合、その情報とエントロピーは仕事源または外部自由度へ移す必要がある [17,18]。

有限装置部分だけで

```math
z_{\rm post}
\longmapsto
z_{\rm ref}
```

という多対1写像を置くことは Hamiltonian ではない。記録、garbage、外部仕事自由度を含む拡大全系で可逆に実装し、有限部分の復元だけを縮約として得る必要がある。

# 対モード、境界比較器、完全周期の Hamiltonian 詳細

> **位置づけ：** 同じ2成分場の固定モード射影、反対称源の階数2分解、局所回転、理想比較読み出し、2モード作用保存、殻容量、逆計算を有限正準変数で明示する。境界集団の準備と一般結果形成は未導出である。


## 拡大全系とエネルギー収支

1試行を担う有限部分を

```math
\begin{aligned}
H_{\rm fin}
={}&
H_{\rm particles}
+
H_{\rm field}
+
H_{\rm prep}
+
H_{\rm source}
+
H_{\rm analyzer}
+
H_{\rm pointer}\\
&
+
H_{\rm return}
+
H_{\rm read}
+
H_{\rm mix}
+
H_{\rm memory}
+
H_{\rm reset}
+
H_{\rm clk}
\end{aligned}
```

とする。外部自由度と仕事源を含め、

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

とする。$H_{\rm all}$ は自律 Hamiltonian であり、有限部分だけのエネルギーは

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

と変化し得る。

比較窓では $\varepsilon_{\rm ext}$ の効果を小さくし、有限閉鎖系の正準写像として計算する。$H_{\rm prep}$ は局所準備浴または同型高速モード交換補助系を含み、観測窓では切り離す。試行間では、外部記録、garbage移送、準備浴と交換補助系の再初期化に弱開放流路を用い得る。

## 固定モード射影の正準性

場の有限切断座標を $q\in\mathbb R^N$、運動量を $\pi\in\mathbb R^N$ とする。固定直交行列 $O$ で

```math
q'
=
Oq,
\qquad
\pi'
=
O\pi
```

と変換すると、

```math
\pi^{\mathsf T}dq
=
\left(
\pi'
\right)^{\mathsf T}
dq'.
```

従って変換は正準である。

$O$ の行を、位相活性、A側対モード、B側対モード、比較モード、暗モードの基底に選ぶ。射影は装置の設定、測定結果、目標密度に依存させない。

各2成分正準対 $(Q_{\mu r}^X,P_{\mu r}^X)$ から

```math
z_{\mu r}^X
=
\frac{
Q_{\mu r}^X+iP_{\mu r}^X
}{
\sqrt2
},
\qquad
X\in\{A,B\}
```

と定める。Poisson 括弧は

```math
\left\{
z_{\mu r}^X,
\left(
z_{\nu s}^Y
\right)^*
\right\}
=
-i
\delta_{XY}
\delta_{\mu\nu}
\delta_{rs}.
```

## 反対称源のランク2分解

基底ベクトルを

```math
e_+
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
e_-
=
\begin{pmatrix}
0\\
1
\end{pmatrix}
```

とする。理想反対称源は

```math
C_0
=
\sqrt{\frac{\mathcal K}{2}}
\left[
e_+e_-^{\mathsf T}
-
e_-e_+^{\mathsf T}
\right].
```

2つの直交源チャンネルを

```math
z^{A,(1)}
=
a_0e_+,
\qquad
z^{B,(1)}
=
b_0e_-,
```

```math
z^{A,(2)}
=
a_0e_-,
\qquad
z^{B,(2)}
=
-b_0e_+
```

と準備し、$\eta_r$ を

```math
\eta_1a_0b_0^*
=
\eta_2a_0b_0^*
=
\sqrt{\frac{\mathcal K}{2}}
```

に選べば、

```math
C
=
\sum_{r=1}^{2}
\eta_r
z^{A,(r)}
\left(
z^{B,(r)}
\right)^\dagger
=
C_0.
```

$a_0,b_0$ を実数に取る必要はない。共通位相は共役積で消え、相対位相だけが $C_0$ の符号と可視度を決める。

有限 Hamiltonian 源の候補は、時計窓で作動する2モード生成子の組合せとして書けるが、一般の初期集団から上の固定相対位相を偏りなく準備する収束定理はない。

## 局所分析器の生成子

A側の2出力モードに対し、

```math
G_A
=
\sum_r
\left(
Q^A_{+r}P^A_{-r}
-
Q^A_{-r}P^A_{+r}
\right).
```

Poisson 括弧から

```math
\dot z^{A,(r)}
=
\dot\alpha_a
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
z^{A,(r)}
```

を得るため、パルス積分後は

```math
z^{A,(r)}_{\rm out}
=
R(\alpha_a)
z^{A,(r)}_{\rm in}.
```

B側も同様である。$G_A$ と $G_B$ は空間的に離れた場モードへ作用し、

```math
\left\{
G_A,G_B
\right\}
=
0.
```

局所分析器は共通内部位相の生成子と可換である。出力モード添字を実回転するだけだからである。

## 戻り伝達核

局所出力から共通未来比較領域までの線形伝播を

```math
z_{{\rm ret},\mu r}^{X}(t)
=
\sum_{\nu,s}
\int
G_{\mu r,\nu s}^{X}(t-t')
z_{{\rm out},\nu s}^{X}(t')
\,dt'
```

と書く。局所有限伝播には

```math
G^{X}(t)
=
0
\qquad
t<\tau_X
```

が必要である。理想核は比較時刻で

```math
G^{X}
=
e^{i\varphi_X}I
```

となる。共通位相 $e^{i\varphi_X}$ は $C$ の全体位相または較正へ吸収できるが、源チャンネル依存位相は干渉可視度を低下させる。

交差応答の指標を

```math
\varepsilon_{\rm ret}
=
\left\|
G^X
-
e^{i\varphi_X}I
\right\|
```

とする。

## 相関選択関数

局所結果座標の滑らかな窓を $\chi_A(s_A)$、$\chi_B(s_B)$ とし、

```math
C(s_A,s_B)
=
\sum_{A,B}
\chi_A(s_A)
\chi_B(s_B)
\sum_r
\eta_r
z^A_{Ar}
\left(
z^B_{Br}
\right)^*
```

とする。理想的な排他的sectorでは

```math
\chi_A\chi_{A'}
=
0
\qquad
A\neq A',
```

```math
\sum_A\chi_A=1,
\qquad
\sum_B\chi_B=1
```

が結果領域で成立する。

窓の遷移域では複数sectorが重なり得る。遷移域の境界測度を零または制御された有限幅とする条件が必要である。一般的な唯一結果形成は、この窓の定義だけからは従わない。

## 比較 Hamiltonian の Poisson 計算

比較正準対に対し、

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}\operatorname{Re}C
+
P_{\rm I}\operatorname{Im}C
\right].
```

直接計算すると、

```math
\left\{
Q_{\rm R},
H_{\rm read}
\right\}
=
g_{\rm read}\operatorname{Re}C,
```

```math
\left\{
Q_{\rm I},
H_{\rm read}
\right\}
=
g_{\rm read}\operatorname{Im}C,
```

```math
\left\{
P_{\rm R},
H_{\rm read}
\right\}
=
\left\{
P_{\rm I},
H_{\rm read}
\right\}
=
0.
```

入力モード $z$ について、

```math
\left\{
z,H_{\rm read}
\right\}
=
g_{\rm read}
\left[
P_{\rm R}
\left\{
z,\operatorname{Re}C
\right\}
+
P_{\rm I}
\left\{
z,\operatorname{Im}C
\right\}
\right].
```

従って $P_{\rm R}=P_{\rm I}=0$ なら反作用は厳密に零である。比較中の他の Hamiltonian が $P_\nu$ を生成しないことが必要である。

## 比較作用と内部対称性

比較作用を

```math
A_\partial
=
\frac12
\left(
Q_{\rm R}^2
+
P_{\rm R}^2
+
Q_{\rm I}^2
+
P_{\rm I}^2
\right)
```

とする。理想読み出し後は

```math
A_\partial^{AB}
=
\frac{\Gamma^2}{2}
|C_{AB}|^2.
```

共通内部回転の生成子を $\mathcal J_\phi$ とする。$C$ は共通回転不変で、比較正準対を中性に取るため、

```math
\left\{
\mathcal J_\phi,
H_{\rm read}
\right\}
=
0.
```

局所分析器、時計、記録、reset各項も共通内部回転に不変に設計すれば、

```math
\left\{
\mathcal J_\phi,
H_{\rm cycle}
\right\}
=
0.
```

この条件は、位相接続の有効作用定数と Bell 比較構成を同じ場で共存させるために必要である。

## 作用保存型の比較混合

比較複素ベクトル

```math
c_\partial
=
\frac1{\sqrt2}
\begin{pmatrix}
Q_{\rm R}+iP_{\rm R}\\
Q_{\rm I}+iP_{\rm I}
\end{pmatrix}
```

に対し、

```math
A_\partial
=
c_\partial^\dagger c_\partial.
```

Hermitian 生成子 $T_\alpha$ を用い、

```math
H_{\rm mix}
=
g_{\rm mix}(\vartheta)
\sum_\alpha
\xi_\alpha(z_{\rm D})
c_\partial^\dagger T_\alpha c_\partial
```

とする。複素 Poisson 括弧から

```math
\dot c_\partial
=
-i
g_{\rm mix}
\sum_\alpha
\xi_\alpha
T_\alpha
c_\partial
```

であり、

```math
\frac{dA_\partial}{dt}
=
0.
```

従って暗モードは比較作用を直接受け取らず、$U(2)$ 回転の係数だけを供給する。

## 2モード殻積分

作用角座標で

```math
J_{\rm R}
=
|c_{\rm R}|^2,
\qquad
J_{\rm I}
=
|c_{\rm I}|^2
```

とする。固定比較作用 $A>0$ の未規格化殻容量は

```math
\begin{aligned}
\Omega_2(A)
&=
\int
\delta
\left(
A-J_{\rm R}-J_{\rm I}
\right)
dJ_{\rm R}\,d\theta_{\rm R}\,
dJ_{\rm I}\,d\theta_{\rm I}\\
&=
(2\pi)^2
\int_0^A
dJ_{\rm R}\\
&=
(2\pi)^2A.
\end{aligned}
```

従って $A=A_\partial^{AB}$ なら、

```math
\Omega_2^{AB}
=
(2\pi)^2
\frac{\Gamma^2}{2}
K_{AB}.
```

追加の比較作用モードを直接殻へ入れると、容量のべきが変わる。spectator自由度は、結果と設定に共通な因子としてだけ積分する。

## 共通境界流束と coarea

全境界位相空間上で作用制約を

```math
F_1(z)
=
A_\partial^{AB}
-
J_{\rm R}
-
J_{\rm I}
```

とし、時計面を

```math
F_2(z)
=
\vartheta-\vartheta_\partial
```

とする。結果sectorの正方向流束は

```math
\mathscr F_{AB}
=
w_{AB}
\int
\rho_\partial(z)
\delta(F_1)
\delta(F_2)
\left(
\dot\vartheta
\right)_+
d\Gamma.
```

coarea公式により、

```math
\mathscr F_{AB}
=
w_{AB}
\int_{F^{-1}(0)}
\frac{
\rho_\partial(z)
\left(
\dot\vartheta
\right)_+
}{
J_F(z)
}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

共通境界条件は、$\rho_\partial$、$\dot\vartheta$、$J_F^{-1}$、spectator体積、解多重度の積分後の因子が4結果で等しいことを要求する。殻容量以外の因子が結果依存なら、Bell 共同法則は修正される。

## 正規化された押し出しでは足りない

各結果sectorに規格化された初期測度 $\mu_{AB}$ を置き、読み出しと混合の正準写像を $\mathcal U_{AB}$ とする。すると、

```math
\left(
\mathcal U_{AB}
\right)_*
\mu_{AB}
\left(
\Gamma^{AB}
\right)
=
\mu_{AB}
\left(
\Gamma^{AB}
\right)
=
1.
```

従って、正規化された4集団を別々に比較しても $K_{AB}$ 重みは出ない。$K_{AB}$ 重みは、全sectorへ共通密度を置いた未規格化境界積分が、異なる殻容量を数えるときだけ現れる。

この事実は数値検算でも、sector質量保存と殻容量の線形性を別項目として確認する。

## 時計、記録、逆計算

時計項を

```math
H_{\rm clk}
=
\Omega I_\vartheta
```

とし、各相互作用を互いに分離した窓 $g_k(\vartheta)$ で作動させる。理想順序は、源準備、局所分析、局所記録、戻り伝播、比較、殻内混合、境界通過である。この順序に対応する Hamiltonian 窓として実装する。

境界通過後、結果を外部記録セルへ可逆にコピーし、

```math
\mathcal U_{\rm cycle}^{-1}
=
\mathcal U_{\rm source}^{-1}
\mathcal U_{\rm analyzer}^{-1}
\mathcal U_{\rm return}^{-1}
\mathcal U_{\rm read}^{-1}
\mathcal U_{\rm mix}^{-1}
```

を実際の逆順に適用する。記号上の積は作用順序に合わせて読む。比較読み出しの逆は同じ入力 $C_{AB}$ に対する $-H_{\rm read}$ である。

外部記録を含む全状態を同じ基準点へ戻すことはできない。異なる結果情報は外部記録、garbage、仕事源、環境のどこかへ残る必要がある。

## 有限幅誤差

有限パルス中の全 Hamiltonian を

```math
H
=
H_{\rm read}
+
H_0
```

とする。相互作用表示の Magnus 展開では、理想読み出しからの先頭補正は概略

```math
\delta\mathcal U
=
O
\left(
\tau_{\rm read}
\|H_0\|
\right)
+
O
\left(
\tau_{\rm read}^2
\left\|
[H_{\rm read},H_0]
\right\|
\right).
```

古典系では交換子を対応する Poisson 作用素の交換子として読む。初期比較運動量が $P_\nu^{\rm in}\neq0$ なら、入力モードへの反作用は1次で生じる。従って、

```math
\varepsilon_{\rm pulse}
\sim
\tau_{\rm read}\omega_{\rm free}
+
\frac{
|P_{\rm R}^{\rm in}|
+
|P_{\rm I}^{\rm in}|
}{
\Gamma|C_{AB}|+\epsilon_0
}
+
\varepsilon_{\rm ret}
```

を代表的な無次元誤差とできる。$\epsilon_0>0$ は作用零sectorでの規格化発散を避ける解析用定数である。

## 未導出事項

本付録の有限正準計算からは、次は導かれない。

1. 一般初期集団から反対称源 $C_0$ を準備すること。
2. 2源チャンネルの相対位相を全試行で保つこと。
3. 連続した局所状態から唯一結果sectorを形成すること。
4. 暗モード集団が比較殻上の Haar 分布を準備すること。
5. 異なる結果殻へ共通の未規格化境界密度を置くこと。
6. 設定生成器を含む境界測度を事後選別なしで実験的に実現すること。
7. 外部記録を保持し、準備浴と高速交換補助系を再初期化する長期反復reset。
8. 位相活性、対、比較部分空間の交差誤差を長時間一様に小さくすること。
9. 平面内2出力を超える一般測定器。
10. 一般的な Tsirelson 原理。

これらは補助模型内部の代数的厳密性とは別の、現行モデル M0 の準備、縮約、測定、反復の課題である。

# 現行模型に採用しない運動量結合配置拡散経路

> **位置づけ：** 本付録は現行モデル M0 に採用しない補助理論である。有限運動量結合、正確な場消去、二側配置拡散内部の Fisher 構造を保存するが、位相接続による Schrödinger 型力学の導出には使わない。


## この経路を残す理由

配置拡散経路は、実在的な確率軌道を構成する別の研究候補として記録する。現行モデル M0 の構成要素ではなく、第2章から第3章の位相接続縮約、第4章の Born 型入口標本化、第5章の Bell 型履歴測度のいずれにも使用しない。従って、次の係数一致は現行理論の成立条件ではない。

```math
\nu_{\rm bath}
=
\frac{|\mathcal J_\phi|}{2m}
```

この等式は、将来2経路を同一の有効理論として統合する場合だけ必要な比較条件である。

第3章は coherent縮約多様体上で Schrödinger 型PDEを閉じるが、粒子が実在的な前進・後退 Markov 経路を持つことは示さない。本章の運動量結合経路は、有限 Hamiltonian 誘導場の速度揺らぎから、その確率過程へ進む候補を与える。

両経路は役割を分ける。

- 位相接続経路：作用と有効PDEを与える。
- 運動量結合経路：配置軌道の拡散極限を与える候補である。
- 係数一致と同時実現：独立した未解決問題である。

## 運動量結合した有限誘導場

粒子正準対を $(X,P)$、誘導場正準対を $(Q,\Pi)$ とする。線形核を

```math
H_N^{\rm lin}
=
\frac12
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I_d & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}
+
V(X)
+
\frac12Q^{\mathsf T}K_NQ
```

とする。$M_N$ と $K_N$ は正定値実対称行列である。

<!-- theorem-start:proposition -->
**命題（運動量2次形式の成立条件）**
運動量2次形式が正定値であるための必要十分条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
左上ブロック $m^{-1}I_d$ は正定値である。ブロック行列の Schur 補条件を適用する。
<!-- theorem-end:proof -->

Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X),
```

```math
\dot Q
=
M_N^{-1}\Pi
+
C_N^{\mathsf T}P,
\qquad
\dot\Pi
=
-K_NQ.
```

従って配置速度は

```math
U_N
=
\frac Pm
+
Y_N,
\qquad
Y_N
=
C_N\Pi.
```

正準運動量 $P$ と機械的運動量 $m\dot X$ は一致しない。

## 時間反転と配置流束

標準時間反転

```math
(P,\Pi)
\mapsto
(-P,-\Pi)
```

の下で運動量2次形式は不変である。$V$ と場ポテンシャルが座標だけに依存すれば、有限閉鎖核は時間反転対称である。

全 Liouville 密度を $F_N(X,P,Q,\Pi,t)$、配置周辺密度を

```math
\rho_N(x,t)
=
\int
F_N
\,dP\,dQ\,d\Pi
```

とする。Liouville 方程式を内部変数で積分すると、

```math
\partial_t\rho_N
+
\nabla\cdot
\left(
\rho_Nv_N
\right)
=
0,
```

```math
v_N
=
\mathbb E_N
\left[
\frac Pm+C_N\Pi
\mid
X=x
\right].
```

$P/m$ だけを配置速度としてはならない。

## 線形誘導場の正確な消去

質量規格化した場座標で、正定値周波数行列を $\Omega_N$ とする。指定初期値問題の解を粒子運動量から独立な自由解と強制解へ分けると、

```math
Y_N(t)
=
Y_N^{\rm free}(t)
-
\int_0^t
C_N\Omega_N
\sin
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}P(s)
\,ds.
```

第1項は初期誘導場に由来する自由速度揺らぎ、第2項は粒子から場への反作用速度記憶である。

指定した Gauss 型初期集団で、場のエネルギー尺度を $\Theta_N$ とすると、

```math
R_N(t-s)
=
\mathbb E
\left[
Y_N^{\rm free}(t)
\otimes
Y_N^{\rm free}(s)
\right]
```

```math
=
\Theta_N
C_N
\cos
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}.
```

有限 $N$ では相関は余弦関数の有限和である。厳密な OU 相関や無限時間の Brown 運動ではない [12--14]。

二側境界条件を用いる場合、自己共役な境界値問題では Green 核が時間交換対称になる。しかし、自己共役 Green 核だけから Nelson の時間対称平均加速度は従わない。

## 再帰前の Brown 極限

目標とする観測窓は

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}.
```

多数モード、短記憶、適切なスペクトル包絡、弱い外部交換の下で、

```math
\int_0^t
Y_N^{\rm free}(s)
\,ds
\Longrightarrow
\sqrt{2\nu_{\rm bath}}\,W_t
```

を示す必要がある。

反作用記憶項も同時に、

```math
\int_0^t
K_N(t-s)P(s)
\,ds
=
\delta m\,\dot X(t)
+
B_{\rm loc}(X_t,P_t)
+
\mathcal R_{\rm mem}(t)
```

のように、質量繰り込み、局所ドリフト、制御可能な残差へ分けなければならない。有限再帰、異方性、非 Gauss 性、外部交換を同じ上界で制御する定理は未完成である。

## 位相空間極限と配置 Markov 閉鎖

最初の有効候補は

```math
dX_t
=
\frac{P_t}{m}\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t,
```

```math
dP_t
=
-\nabla V(X_t)\,dt
+
B_{\rm loc}(X_t,P_t)\,dt.
```

$(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。配置変数だけの前進・後退拡散

```math
dX_t
=
b_+(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^+,
```

```math
dX_t
=
b_-(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^-
```

を得るには、運動量緩和、条件付き速度分散、記憶残差を消去する追加の時間尺度分離が必要である。

## 二側配置拡散内部の Fisher 構造

共通の正の密度 $\rho$ と共通の等方拡散係数 $\nu_{\rm bath}$ を持つ前進・後退 Markov 拡散が得られたとする。現在速度 $v$ と浸透速度 $u$ を

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
```

と定める。前後 Fokker--Planck 方程式の差から、

```math
u
=
\nu_{\rm bath}
\nabla\log\rho.
```

従って、

```math
\frac m2
\int
\rho|u|^2
\,dx
=
\frac{
m\nu_{\rm bath}^2
}{
2
}
\int
\frac{
|\nabla\rho|^2
}{
\rho
}
\,dx
```

である。量子ポテンシャルに対応する項は

```math
Q_{\rm bath}[\rho]
=
-2m\nu_{\rm bath}^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

これは二側 Markov 拡散を仮定した補助模型内部の厳密結果である。

## 将来統合する場合の係数比較

第3章の作用係数は

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|.
```

本章の Fisher 係数が同じ量子ポテンシャルを与えるには、

```math
|\mathcal J_\phi|
=
2m\nu_{\rm bath}.
```

同値に、

```math
\nu_{\rm bath}
=
\frac{
|\mathcal J_\phi|
}{
2m
}.
```

この一致は、2経路を将来同じ有効理論として統合する場合の必要条件である。現行M0は配置拡散経路を採用しないため、現行理論の成立条件または反証条件ではない。補助模型を再採用する場合には、位相作用と浴拡散係数を独立に測り、上式が成立しなければ2経路は同じ有効理論を表さないと判定する。

## 時間対称 Newton 則との関係

配置拡散と Fisher 項だけから

```math
ma_{\rm ts}
=
-\nabla V
```

は従わない。時間対称 Green 応答、反作用記憶、条件付き変分からこの Newton 則へ進む問題は未解決である。

一方、第3章では、位相接続縮約作用の変分から同値な Madelung 動力学を得た。後者は、前者の確率過程導出を代替しない。

## 本章の結論

運動量結合した有限誘導場では、正定値条件、時間反転対称性、正確な配置流束、自由速度揺らぎと反作用記憶の分離を得る。二側配置 Markov 拡散が得られた後の浸透速度と Fisher 項も厳密である。

未解決なのは、有限誘導場からの Brown 極限、配置 $X$ だけの Markov 閉鎖、条件付き速度分散の抑制、時間対称 Newton 則、位相接続経路との係数一致と同時実現である。

# 局所作用整合と動径低速化の有限準備浴

> **位置づけ：** セルまたはグラフに局所的な有限調和浴の Hamiltonian、共通位相回転対称性、全位相作用の保存、対称な余弦・正弦結合による位相固定項の消去は厳密結果である。記憶摩擦、欠陥減衰、有限温度床、有限時間準備は明記した短記憶・固定振幅近似の下での結果である。付録Fの大域的な同型高速モード交換とは役割が異なる。


## 目的と時間窓

第2.6節の有限特異 Hamiltonian は、局所作用整合と動径低速化を低速枝として与えるが、一般初期値からその枝を準備しない。本付録では、対象場から高速欠陥エネルギーを有限浴へ移す Hamiltonian を明示する。

本付録の構成はセルまたは固定グラフ辺へ局所的に書ける一方、欠陥減衰に短記憶・固定振幅・低温近似を使う。付録Fの同型高速モード交換は、正定値定数係数2次模型では厳密だが、高速Riesz射影と精密調整された大域的補助系を使う。2つを置き換えず、局所的な近似準備機構と、大域的な可解基準機構として分ける。

準備に使う浴は観測中の位相運動を変え得るため、内部時計の準備窓だけ作動させる。時計正準対を $(\vartheta,J_\vartheta)$ とし、作動帯で滑らかな窓関数

```math
0
\leq
g_{\rm prep}(\vartheta)
\leq
1
```

を用いる。準備平坦部で $g_{\rm prep}=1$、観測窓で $g_{\rm prep}=0$ とする。時計を含む全 Hamiltonian は自律的である。

## 振幅座標の有限浴

セル $i$ の振幅座標 $R_i$ に有限個の調和振動子を結合する。浴正準対を $(Q_{i\alpha},\mathcal P_{i\alpha})$ とし、

```math
H_{R{\rm B}}
=
\sum_{i,\alpha}
\left[
\frac{
\mathcal P_{i\alpha}^2
}{
2m_\alpha
}
+
\frac{
m_\alpha\omega_\alpha^2
}{
2
}
\left(
Q_{i\alpha}
-
\frac{
c_\alpha g_{\rm prep}(\vartheta)R_i
}{
m_\alpha\omega_\alpha^2
}
\right)^2
\right]
```

とする。準備平坦部で浴を正確に消去すると、$P_i$ の式に

```math
-\int_0^t
K_R(t-s)
\dot R_i(s)
\,ds
+
\xi_i(t)
```

が加わる。記憶核は

```math
K_R(t)
=
\sum_\alpha
\frac{
c_\alpha^2
}{
m_\alpha\omega_\alpha^2
}
\cos
\left(
\omega_\alpha t
\right).
```

有限浴では $K_R$ は余弦関数の有限和であり、厳密な局所摩擦ではない。再帰前の短記憶領域で

```math
\int_0^t
K_R(t-s)
\dot R_i(s)
\,ds
\simeq
\eta_R\dot R_i
```

と近似できるとき、

```math
\dot P_i
\simeq
-
\frac{
\partial H_{\epsilon_{\rm s}}
}{
\partial R_i
}
-
\frac{
\eta_R
}{
\epsilon_{\rm s}M
}
P_i
+
\xi_i.
```

従って振幅浴は $P_i$ の高速成分を抑える。ただし、低速枝では $R_i$ 自体が動くため、目標は $P_i=0$ の永久固定ではなく、観測開始時に $P_i=O(\epsilon_{\rm s})$ となる準備である。

## 全作用を保存する作用交換浴

セルを結ぶ連結グラフを取り、辺 $e=(i,k)$ の向き付き接続ベクトルを $b_e=e_i-e_k$ とする。位相差と2つの周期関数を

```math
\phi_e
=
b_e^{\mathsf T}\boldsymbol\theta,
\qquad
F_{e,c}
=
\cos\phi_e,
\qquad
F_{e,s}
=
\sin\phi_e
```

と定める。作用交換浴の正準対を $(X_{e\sigma\alpha},\Pi_{e\sigma\alpha})$ とし、

```math
\begin{aligned}
H_{J{\rm B}}
=
\sum_{e,\sigma,\alpha}
\Bigg[
&
\frac{
\Pi_{e\sigma\alpha}^2
}{
2\mu_\alpha
}
\\
&+
\frac{
\mu_\alpha\Omega_\alpha^2
}{
2
}
\left(
X_{e\sigma\alpha}
-
\frac{
d_\alpha g_{\rm prep}(\vartheta)F_{e,\sigma}
}{
\mu_\alpha\Omega_\alpha^2
}
\right)^2
\Bigg],
\end{aligned}
```

```math
\sigma
\in
\{c,s\}
```

とする。同じ辺の余弦系列と正弦系列には同じ $(\mu_\alpha,\Omega_\alpha,d_\alpha)$ を用いる。

<!-- theorem-start:proposition -->
**命題（有限作用交換浴の全位相作用保存）**
$H_{J{\rm B}}$ は共通位相回転 $\theta_i\mapsto\theta_i+\beta$ に不変である。従って、

```math
\left\{
\mathcal J_\phi,
H_{\epsilon_{\rm s}}
+
H_{R{\rm B}}
+
H_{J{\rm B}}
+
H_{\rm clk}
\right\}
=
0.
```

時計窓の立ち上がりと立ち下がりを含め、$\mathcal J_\phi=\sum_iJ_i$ は厳密に保存される。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$H_{J{\rm B}}$ の位相依存性は全て $\theta_i-\theta_k$ を通じる。$H_{R{\rm B}}$ と $H_{\rm clk}$ は共通位相に依存しない。従って全 Hamiltonian は共通回転不変であり、その生成子 $\mathcal J_\phi$ との Poisson 括弧は零である。
<!-- theorem-end:proof -->

各辺の2系列から生じる逆項は

```math
\frac{
d_\alpha^2g_{\rm prep}^2
}{
2\mu_\alpha\Omega_\alpha^2
}
\left(
\cos^2\phi_e
+
\sin^2\phi_e
\right)
```

であり、位相差に依存しない。従って、浴は不要な位相固定ポテンシャルを作らない。2系列のスペクトルが一致しない場合は、この相殺が崩れるため誤差として管理する。

## 正確な記憶核と短記憶近似

準備平坦部で作用交換浴を消去すると、辺方向のトルクは

```math
\begin{aligned}
\tau_e(t)
=
{}&-
\int_0^t
K_J(t-s)
\cos
\left[
\phi_e(t)
-
\phi_e(s)
\right]
\dot\phi_e(s)
\,ds
\\
&+
\xi_e(t),
\end{aligned}
```

```math
K_J(t)
=
\sum_\alpha
\frac{
d_\alpha^2
}{
\mu_\alpha\Omega_\alpha^2
}
\cos
\left(
\Omega_\alpha t
\right)
```

となる。余弦因子は、2系列の積の和

```math
\sin\phi_e(t)
\sin\phi_e(s)
+
\cos\phi_e(t)
\cos\phi_e(s)
=
\cos
\left[
\phi_e(t)-\phi_e(s)
\right]
```

から生じる。

浴相関時間中の位相差変化が小さく、記憶核を局所化できるとき、接続行列を $B=(b_e)$、グラフ Laplacian を

```math
L_G
=
BB^{\mathsf T}
```

として、作用方程式の浴寄与は

```math
\dot{\boldsymbol J}
\simeq
-
\eta_JL_G
\dot{\boldsymbol\theta}
+
B\boldsymbol\xi.
```

これは絶対位相速度ではなく、辺に沿う相対位相速度だけへ作用する。しかし、観測中の物理的な相対位相運動も区別しないため、準備終了後には切り離す必要がある。

## 固定振幅準備近似での欠陥減衰

短い準備窓で $q_i=R_i^2$ を固定し、$D_q=\operatorname{diag}(q_i)$ とする。$H_0$ の位相力と浴雑音を無視した高速部分では、全体位相速度を除いて

```math
\dot{\boldsymbol\theta}
-
\bar\omega\boldsymbol 1
=
\frac{1}{\epsilon_{\rm s}I}
D_q^{-1}
\boldsymbol{\delta J}.
```

従って、

```math
\dot{\boldsymbol{\delta J}}
=
-
\frac{
\eta_J
}{
\epsilon_{\rm s}I
}
L_GD_q^{-1}
\boldsymbol{\delta J}.
```

欠陥エネルギーを

```math
E_{\delta J}
=
\frac{1}{2\epsilon_{\rm s}I}
\boldsymbol{\delta J}^{\mathsf T}
D_q^{-1}
\boldsymbol{\delta J}
```

とすると、

```math
\frac{
dE_{\delta J}
}{
dt
}
=
-
\frac{
\eta_J
}{
\epsilon_{\rm s}^2I^2
}
\left(
D_q^{-1}
\boldsymbol{\delta J}
\right)^{\mathsf T}
L_G
\left(
D_q^{-1}
\boldsymbol{\delta J}
\right)
\leq
0.
```

グラフが連結なら $L_G$ の零空間は $\boldsymbol 1$ が張る。等号なら $D_q^{-1}\boldsymbol{\delta J}=c\boldsymbol 1$ であるが、$\sum_i\delta J_i=0$ と $\sum_iq_i=1$ から $c=0$ となる。従って、この近似の範囲では $\boldsymbol{\delta J}=0$ だけが零減衰状態である。

一般の準備運動では、

```math
\dot{\boldsymbol{\delta J}}
=
\dot{\boldsymbol J}
-
\mathcal J_\phi
\dot{\boldsymbol q}
```

であり、$H_0$ の位相力、振幅運動、有限温度雑音、記憶残差が強制項になる。従って上の単調減衰は、固定振幅・短記憶・低温の準備近似に限定される。

## 有限浴、温度、切断の限界

有限 Hamiltonian 浴では永久的な不可逆減衰は起こらない。必要な観測窓は

```math
\tau_{\rm corr}
\ll
T_{\rm prep}
\ll
T_{\rm rec}.
```

$T_{\rm rec}$ より長い時間では、再位相整合とエネルギー再流入が起こり得る。反復運転では、試行後に浴を外部流路へ接続し、欠陥エネルギーを排出して浴を再初期化する必要がある。

有限温度では $\xi_i$ と $\xi_e$ が残り、欠陥は零ではなく温度依存の揺らぎ床を持つ。観測開始時の誤差には少なくとも、

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm mem}
+
\varepsilon_T
+
\varepsilon_q
+
\varepsilon_{cs}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm rec}
```

を含める。各項は、短記憶化、有限温度、準備中の振幅変化、余弦・正弦浴の不一致、時計窓の切断、有限浴再帰からの誤差である。

本付録は、局所作用欠陥と動径欠陥の準備を局所的な浴結合として部分的に具体化する。付録Fの厳密交換定理と異なり、一般の高速スペクトル部分空間を完全に零へ移す定理ではない。coherent集中、$r^2=\rho$ の密度同期、単流束化、節、入口標本化後の活性場再埋め込み、観測時間に一様な欠陥上界は導かない。

# 単体局所正準形、低速・高速分離、高速モード交換

> **位置づけ：** 厳密規格化・固定全位相作用の局所chart Hamiltonian、2つの慣性行列の逆恒等式、正定値2次模型の2帯分離、同型有限補助系への高速成分交換は、明記した条件の下で厳密結果である。半正定値位相 Hessian、有限規格化ペナルティ、時間依存基準経路、粒子-場を含む全 Hessian、非線形高速再励起は未完成である。


## 厳密制約模型と有限ペナルティ模型

第2.6節の規格化量を

```math
N
=
\sum_{i=1}^{L}R_i^2
```

とする。共通内部回転の生成子

```math
\mathcal J_\phi
=
\sum_{i=1}^{L}J_i
```

は対称性から保存される。従って、固定 $\mathcal J_\phi$ は Hamiltonian 流の不変sectorである。

一方、有限ペナルティ

```math
\frac{\Lambda_N}{2}
\left(
N-1
\right)^2
```

だけでは $N$ は一般に保存されない。本付録の厳密な局所縮約では、

```math
N=1
```

をホロノミック制約として課し、正の規格化単体

```math
\Sigma_{L-1}^{\circ}
=
\left\{
q\in\mathbb R^L:
q_i>0,
\quad
\boldsymbol 1^{\mathsf T}q=1
\right\}
```

の余接束を用いる。有限 $\Lambda_N$ の模型は別の Hamiltonian 系であり、規格化方向を追加モードとして含む。両者を同じ「固定規格化sector」と呼ばない。

固定 $\mathcal J_\phi$ を課した後、共通位相を商で除く。以下の局所chartは、節 $q_i=0$ から離れた単体内点だけを覆う。

## 単体と相対位相の局所座標

$n=L-1$ とし、

```math
E^{\mathsf T}E
=
I_n,
\qquad
E^{\mathsf T}\boldsymbol 1
=
0
```

を満たす $L\times n$ 行列 $E$ を固定する。単体内点 $q^*$ の近傍で、振幅偏差 $\xi\in\mathbb R^n$ と相対位相 $\varphi\in\mathbb R^n$ を

```math
q
=
q^*
+
E\xi,
qquad
\boldsymbol\theta
=
\Theta\boldsymbol 1
+
E\varphi
```

により定める。$\Theta$ は共通位相である。

位相正準項は

```math
\begin{aligned}
\mathcal J_\phi
q^{\mathsf T}
d\boldsymbol\theta
={}&
\mathcal J_\phi d\Theta
+
\mathcal J_\phi
\left(
E^{\mathsf T}q^*
+
\xi
\right)^{\mathsf T}
d\varphi.
\end{aligned}
```

$\mathcal J_\phi(E^{\mathsf T}q^*)^{\mathsf T}d\varphi$ は完全微分なので、局所運動方程式を変えずに除ける。固定 $\mathcal J_\phi$ と共通位相の商を取った後に残る磁気型1形式は

```math
\mathcal J_\phi
\xi^{\mathsf T}d\varphi
```

である。この項が、以下の最小結合型運動量シフトを作る。

## 正確な局所chart Hamiltonian

```math
D_q
=
\operatorname{diag}
\left(
q_1,\ldots,q_L
\right)
```

とし、2つの正定値行列を

```math
G_q(q)
=
E^{\mathsf T}
D_q^{-1}
E,
```

```math
G_\varphi(q)
=
E^{\mathsf T}
\left(
D_q
-
qq^{\mathsf T}
\right)
E
```

と定める。第2.6節の有限 $\epsilon_{\rm s}$ Lagrangian は、このchartで正確に

```math
\begin{aligned}
L_{\epsilon_{\rm s}}^{\rm chart}
={}&
\mathcal J_\phi
\xi^{\mathsf T}\dot\varphi
-
H_0(\xi,\varphi)
\\
&+
\frac{
\epsilon_{\rm s}M
}{
8
}
\dot\xi^{\mathsf T}
G_q(q)
\dot\xi
+
\frac{
\epsilon_{\rm s}I
}{
2
}
\dot\varphi^{\mathsf T}
G_\varphi(q)
\dot\varphi
\end{aligned}
```

となる。共役運動量は

```math
p_\xi
=
\frac{
\epsilon_{\rm s}M
}{
4
}
G_q(q)
\dot\xi,
```

```math
p_\varphi
=
\mathcal J_\phi\xi
+
\epsilon_{\rm s}I
G_\varphi(q)
\dot\varphi.
```

従って、局所chart Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{\rm chart}
={}&
H_0(\xi,\varphi)
+
\frac{
2
}{
\epsilon_{\rm s}M
}
p_\xi^{\mathsf T}
G_q(q)^{-1}
p_\xi
\\
&+
\frac{
1
}{
2\epsilon_{\rm s}I
}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right)^{\mathsf T}
G_\varphi(q)^{-1}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right).
\end{aligned}
```

<!-- theorem-start:proposition -->
**命題（厳密制約下の局所chart Hamiltonian）**
$q_i>0$、$N=1$、固定 $\mathcal J_\phi$ の下で、上の Hamiltonian は第2.6節の有限特異 Hamiltonian の局所正準表示である。$\epsilon_{\rm s}\to0$ を取らず、2次化も用いていない。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$\dot q=E\dot\xi$ を第2.6節の振幅慣性項へ代入すると $G_q$ を得る。相対位相速度から重み付き平均を除いた2次形式は

```math
\sum_i
q_i
\left(
\dot\theta_i
-
\sum_jq_j\dot\theta_j
\right)^2
=
\dot\varphi^{\mathsf T}
G_\varphi
\dot\varphi.
```

正準項から完全微分を除き、2つの運動量を Legendre 変換すればよい。
<!-- theorem-end:proof -->

## 振幅・位相慣性行列の逆恒等式

<!-- theorem-start:theorem -->
**定理（単体慣性行列の逆恒等式）**
$q\in\Sigma_{L-1}^{\circ}$ では、

```math
G_q(q)^{-1}
=
G_\varphi(q)
```

が厳密に成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
任意の $x\in\mathbb R^n$ に対し、$v=Ex$ と置く。$\boldsymbol1^{\mathsf T}v=0$ である。さらに

```math
w
=
\left(
D_q
-
qq^{\mathsf T}
\right)
v
```

と置くと、

```math
\boldsymbol1^{\mathsf T}w
=
q^{\mathsf T}v
-
\left(
\boldsymbol1^{\mathsf T}q
\right)
q^{\mathsf T}v
=
0.
```

従って $w=Ey$ を満たす一意な $y$ があり、

```math
y
=
E^{\mathsf T}w
=
G_\varphi x.
```

一方、

```math
D_q^{-1}w
=
v
-
\boldsymbol1
\left(
q^{\mathsf T}v
\right)
```

なので、

```math
G_qy
=
E^{\mathsf T}
D_q^{-1}
Ey
=
E^{\mathsf T}v
=
x.
```

従って $G_qG_\varphi=I_n$ である。
<!-- theorem-end:proof -->

この恒等式は、振幅方向の Fisher 型計量と、相対位相方向の重み付き共分散計量が同じ単体幾何の互いに逆な表示であることを示す。ただし、密度同期または Schrödinger 型力学を単独で導く結果ではない。

## 内点臨界点まわりの2次正準標準形

$H_0$ の内点臨界点を局所原点へ移し、

```math
\nabla H_0
\left(
0,0
\right)
=
0
```

とする。Hessianを

```math
K_{\xi\xi}
=
\partial_\xi^2H_0,
\qquad
K_{\xi\varphi}
=
\partial_\xi\partial_\varphi H_0,
\qquad
K_{\varphi\varphi}
=
\partial_\varphi^2H_0
```

とする。全て臨界点で評価する。

```math
G_*
=
G_\varphi(q^*)
```

を用い、線形正準変換を

```math
x
=
\frac{\sqrt M}{2}
G_*^{-1/2}
\xi,
\qquad
p_x
=
\frac{2}{\sqrt M}
G_*^{1/2}
p_\xi,
```

```math
y
=
\sqrt I
G_*^{1/2}
\varphi,
\qquad
p_y
=
\frac{1}{\sqrt I}
G_*^{-1/2}
p_\varphi
```

と定める。また、

```math
g_\phi
=
\frac{
2\mathcal J_\phi
}{
\sqrt{MI}
}
```

と置く。2次 Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{(2)}
={}&
\frac{1}{2\epsilon_{\rm s}}
\left[
p_x^{\mathsf T}p_x
+
\left(
p_y-g_\phi x
\right)^{\mathsf T}
\left(
p_y-g_\phi x
\right)
\right]
\\
&+
\frac12x^{\mathsf T}A x
+
x^{\mathsf T}C y
+
\frac12y^{\mathsf T}B y
\end{aligned}
```

となる。$A$、$B$ は実対称行列で、$C$ は一般には零でない。これらは元の Hessian を上の線形変換で移した行列である。

<!-- theorem-start:proposition -->
**命題（内点臨界点まわりの2次標準形）**
節から離れた内点臨界点の近傍で、正確なchart Hamiltonianの2次部分は上の最小結合型標準形へ正準変換できる。$G_\varphi(q)$ の位置依存性は、原点で運動量が零なら3次以上の項へ入る。
<!-- theorem-end:proposition -->

位相反転対称性

```math
H_0(\xi,\varphi)
=
H_0(\xi,-\varphi)
```

が臨界点近傍で成立し、臨界位相を $\varphi=0$ に取れるなら、

```math
C=0.
```

この対称性を仮定せずに混合 Hessian を捨ててはならない。

## 正定値2次模型の2帯分離

以下では、

```math
g_\phi\neq0,
\qquad
C=0,
\qquad
A>0,
\qquad
B>0
```

を仮定する。Hamilton方程式は

```math
\epsilon_{\rm s}\ddot x
-
g_\phi\dot y
+
Ax
=
0,
```

```math
\epsilon_{\rm s}\ddot y
+
g_\phi\dot x
+
By
=
0.
```

<!-- theorem-start:theorem -->
**定理（正定値2次模型の低速・高速分離）**
上の条件の下で、十分小さい $\epsilon_{\rm s}>0$ に対し、正の固有振動数は $n$ 個の低速帯と $n$ 個の高速帯へ分かれる。低速帯は $O(1)$ で、その2乗は重複度込みで

```math
\operatorname{spec}
\left[
\frac{
A^{1/2}BA^{1/2}
}{
g_\phi^2
}
\right]
```

へ収束する。高速帯は

```math
\omega_{{\rm f},k}
=
\frac{
|g_\phi|
}{
\epsilon_{\rm s}
}
+
O(1).
```

2帯の間には $\epsilon_{\rm s}\to0$ で発散するスペクトル間隙がある。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$e^{i\omega t}$ 型の解に対する固有値問題は

```math
\begin{pmatrix}
A-\epsilon_{\rm s}\omega^2I_n
&
-i g_\phi\omega I_n
\\
i g_\phi\omega I_n
&
B-\epsilon_{\rm s}\omega^2I_n
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
0.
```

$A>0$ と $B>0$ により2次 Hamiltonian は正定値であるため、線形 Hamiltonian 行列の非零固有値は半単純な純虚数対になる。$\omega=O(1)$ として $\epsilon_{\rm s}=0$ を代入し、$x$ を消去すると、

```math
B y
=
g_\phi^2\omega^2
A^{-1}y.
```

これは $A^{1/2}BA^{1/2}/g_\phi^2$ の正の固有値問題であり、$n$ 個の低速極限を与える。

残る $n$ 個について $\zeta=\epsilon_{\rm s}\omega$ を固定すると、最高次の行列束は $\zeta^2=g_\phi^2$ を与える。固有値の連続性と正定値 Hamiltonian 束の慣性指数を用いると、低速根と合わせて正の根は合計 $2n$ 個であり、残りの $n$ 個は $\zeta\to|g_\phi|$ となる。従って2帯の個数と漸近式を得る。
<!-- theorem-end:proof -->

この定理は正定値2次部分模型の結果である。現行の Madelung 縮約へ無条件に適用しない。

## 低速部分空間上の縮約残差

$\mathcal E_{\rm s}^{\epsilon}$ を前節の低速固有モードが張る実不変部分空間とする。正定値2次模型では、その上の解は全時間で有界であり、各時間微分も初期エネルギーにより一様に抑えられる。

形式的な1階縮約方程式は

```math
Ax
-
g_\phi\dot y
=
0,
```

```math
By
+
g_\phi\dot x
=
0.
```

完全2次方程式との差は

```math
\mathcal R_{\rm s}
=
\begin{pmatrix}
-\epsilon_{\rm s}\ddot x\\
-\epsilon_{\rm s}\ddot y
\end{pmatrix}.
```

<!-- theorem-start:proposition -->
**命題（低速部分空間上の全時間残差）**
初期状態を $\mathcal E_{\rm s}^{\epsilon}$ に置き、初期2次エネルギーを一定に抑えると、十分小さい $\epsilon_{\rm s}$ に対し、

```math
\sup_{t\in\mathbb R}
\left\|
\mathcal R_{\rm s}(t)
\right\|
\leq
C\epsilon_{\rm s}
```

となる。$C$ はそのエネルギー上界には依存するが、時刻と $\epsilon_{\rm s}$ には依存しない。
<!-- theorem-end:proposition -->

これは各時刻の方程式残差である。低速固有振動数の $O(\epsilon_{\rm s})$ 補正により、縮約軌道との位相差は一般に $O(\epsilon_{\rm s}t)$ と蓄積し得る。従って、軌道差が全時間で $O(\epsilon_{\rm s})$ とは結論しない。

また、この残差は局所2次化された場chartの1階方程式に対するものである。粒子密度、粒子流速、密度同期を含む完全な Madelung 作用の変分残差ではない。

## 高速Riesz射影

2次 Hamiltonian の線形生成子を $\mathscr L_{\epsilon}$ とする。十分小さい $\epsilon_{\rm s}$ では、低速固有値と高速固有値は分離している。高速固有値だけを囲む複素輪郭 $\gamma_{\rm f}$ を取り、

```math
\Pi_{\rm f}^{\epsilon}
=
\frac{1}{2\pi i}
\oint_{\gamma_{\rm f}}
\left(
z-\mathscr L_{\epsilon}
\right)^{-1}
\,dz
```

と定める。実高速部分空間は、共役な正負固有値の射影を合わせて得る。

<!-- theorem-start:proposition -->
**命題（高速スペクトル射影）**
正定値2次模型では、$\Pi_{\rm f}^{\epsilon}$ と

```math
\Pi_{\rm s}^{\epsilon}
=
I-\Pi_{\rm f}^{\epsilon}
```

は2次流と交換する。対応する実部分空間は不変かつsymplecticであり、2次 Hamiltonian は低速部分と高速部分の直和へ分かれる。
<!-- theorem-end:proposition -->

この射影は一般に全セルへ広がる。従って、固定グラフ辺だけへ結合する付録Eの局所作用交換浴と同じ局所機構ではない。

## 同型有限補助系による高速成分交換

高速部分空間を Williamson 正準座標で

```math
H_{\rm f}
=
\frac12
\sum_{k=1}^{n}
\omega_{{\rm f},k}
\left(
Q_k^2+P_k^2
\right)
```

と書く。同じ振動数を持つ補助正準対 $(\widetilde Q_k,\widetilde P_k)$ と

```math
\widetilde H_{\rm f}
=
\frac12
\sum_{k=1}^{n}
\omega_{{\rm f},k}
\left(
\widetilde Q_k^2
+
\widetilde P_k^2
\right)
```

を置く。交換生成子を

```math
H_{\rm ex}
=
\sum_{k=1}^{n}
\left(
Q_k\widetilde P_k
-
P_k\widetilde Q_k
\right)
```

とし、内部時計で制御された結合係数を $\chi_{\rm ex}(t)$ とする。

```math
\Theta_{\rm ex}
=
\int
\chi_{\rm ex}(t)
\,dt
```

を交換角と呼ぶ。$H_{\rm ex}$ は $H_{\rm f}+\widetilde H_{\rm f}$ と Poisson 可換なので、自由回転と交換回転を分離できる。

<!-- theorem-start:theorem -->
**定理（同型高速モードの完全交換）**
補助系が対象高速部分と同型で、交換窓の間に他の結合を無視できるとする。共通自由回転を除いた座標は

```math
\begin{pmatrix}
z_{\rm f}^{\rm out}\\
\widetilde z_{\rm f}^{\rm out}
\end{pmatrix}
=
\begin{pmatrix}
\cos\Theta_{\rm ex} & -\sin\Theta_{\rm ex}\\
\sin\Theta_{\rm ex} & \cos\Theta_{\rm ex}
\end{pmatrix}
\begin{pmatrix}
z_{\rm f}^{\rm in}\\
\widetilde z_{\rm f}^{\rm in}
\end{pmatrix}.
```

$\widetilde z_{\rm f}^{\rm in}=0$ と $\Theta_{\rm ex}=\pi/2$ の下で、

```math
z_{\rm f}^{\rm out}
=
0
```

となり、対象系の高速成分は補助系へ完全に移る。
<!-- theorem-end:theorem -->

この操作は散逸でなく、有限正準系間の可逆な状態交換である。交換後も全情報と高速エネルギーは補助系に残る。次試行までに補助系を零状態へ戻すには、外部記録または排熱を含む別の再初期化過程が必要である。

定理は厳密制約後の局所2次chart内部で成立する。交換結合を元の全場変数へ大域的に持ち上げ、節を越えて規格化と $\mathcal J_\phi$ を保存する構成は未完成である。

## 交換角と補助初期状態の誤差

高速2次エネルギーが定めるノルムを $\|\cdot\|_{H_{\rm f}}$ とする。前節の正確な同型模型では、

```math
\left\|
z_{\rm f}^{\rm out}
\right\|_{H_{\rm f}}
\leq
\left|
\cos\Theta_{\rm ex}
\right|
\left\|
z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
\left|
\sin\Theta_{\rm ex}
\right|
\left\|
\widetilde z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}.
```

$\Theta_{\rm ex}=\pi/2+\delta\Theta$ なら、

```math
\left\|
z_{\rm f}^{\rm out}
\right\|_{H_{\rm f}}
\leq
\left|
\delta\Theta
\right|
\left\|
z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
\left\|
\widetilde z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
O
\left(
|\delta\Theta|^2
\right).
```

従って、交換角誤差は振幅に1次、残留エネルギーに2次で入り、補助系の非零初期エネルギーはそのまま対象へ戻り得る。

補助 Hamiltonian の複製誤差、Riesz射影の実装誤差、交換窓中の非線形項は Duhamel 型積分として加わる。これらの一様な定数と連続極限での規模依存性は未評価である。

## 半正定値位相Hessianと零モード

現行の Madelung 縮約では、位相勾配エネルギーを粒子流速側へ整理し、場側で二重計数しない。この分割では $B$ は半正定値、極端には零になり得る。

1自由度で

```math
A>0,
\qquad
B=0,
\qquad
C=0
```

とすると、特性式は

```math
\omega^2
\left[
\epsilon_{\rm s}^2\omega^2
-
\epsilon_{\rm s}A
-
g_\phi^2
\right]
=
0.
```

高速振動数は

```math
\omega_{\rm f}
=
\frac{
\sqrt{
g_\phi^2
+
\epsilon_{\rm s}A
}
}{
\epsilon_{\rm s}
}
```

として残る。一方、低速側は正の振動数でなく零モードになる。一般初期値では零固有値の一般化固有空間に沿う線形成長が生じ得る。

この例は、高速帯の存在に $B>0$ が必須でないことを示す。しかし、一般の $B\geq0$、混合 Hessian、零固有値のJordan構造を含めて、

1. 高速帯だけを一様に分離すること。
2. 高速Riesz射影の正準性を保つこと。
3. 低速一般化部分空間の多項式成長を評価すること。
4. 高速交換後の残差を観測時間に一様に抑えること。

は未証明である。正定値定理を現行 M0 へ適用するために場側へ人工的な位相剛性を戻してはならない。

## 有限規格化ペナルティの中間帯

厳密制約を使わず、有限 $\Lambda_N$ で規格化方向を残すと、その局所偏差を $\eta_N=N-1$ として概略

```math
H_N^{(2)}
=
\frac{
p_N^2
}{
2\epsilon_{\rm s}M_N
}
+
\frac{
\Lambda_N
}{
2
}
\eta_N^2
```

が現れる。$\Lambda_N=O(1)$ なら、

```math
\omega_N
=
O
\left(
\epsilon_{\rm s}^{-1/2}
\right).
```

これは $O(1)$ の低速帯と $O(\epsilon_{\rm s}^{-1})$ の高速帯の間にある中間帯である。実際の係数と混合は $H_0$、規格化方向、相対位相方向の全 Hessian に依存する。

従って、厳密制約模型の2帯定理を有限 $\Lambda_N$ 模型へ直接移せない。有限ペナルティ模型には、少なくとも3帯を許す別のスペクトル解析が必要である。

## 非線形、時間依存、全M0への限界

本付録の厳密交換定理は、固定内点の定数係数2次模型に対する結果である。完全な局所 Hamiltonian では、

```math
G_q
=
G_q(q),
\qquad
G_\varphi
=
G_\varphi(q)
```

であり、$H_0$ は3次以上の項を持つ。これらは低速運動から高速成分を再生成し得る。適用には、初期振幅、観測時間、$\epsilon_{\rm s}$、スペクトル間隙に依存する再励起率の評価が必要である。

基準となる停留経路が時間依存なら、HessianとRiesz射影も時間に依存する。

```math
\dot\Pi_{\rm f}^{\epsilon}
\neq
0
```

であるため、射影の回転自体が低速成分と高速成分を混合する。断熱条件と幾何学的接続項を含む別の定理が必要になる。

さらに、現行 M0 には粒子座標、粒子運動量、密度、位相接続、装置、準備浴が含まれる。全系を2次化すると粒子-場混合 Hessian が現れる。本付録は場chart内部の高速法線成分を扱うが、M0全体の停留経路または特定の Schrödinger 解を選ばない。

従って、本付録が示すのは、

1. 厳密制約下の局所正準形。
2. 正定値2次模型での低速・高速分離。
3. 理想同型補助系への高速成分の可逆な完全交換。
4. 交換後の局所2次縮約方程式に対する $O(\epsilon_{\rm s})$ 残差。

までである。coherent集中、密度同期、単流束化、節、半正定値位相 Hessian、一般の時間依存停留経路は解決していない。

# 参考文献


- [1] J. S. Bell, ``On the Einstein Podolsky Rosen Paradox,'' Physics Physique Fizika 1, 195--200 (1964). <https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195>
- [2] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, ``Proposed Experiment to Test Local Hidden-Variable Theories,'' Physical Review Letters 23, 880--884 (1969). <https://doi.org/10.1103/PhysRevLett.23.880>
- [3] E. Nelson, ``Derivation of the Schrödinger Equation from Newtonian Mechanics,'' Physical Review 150, 1079--1085 (1966). <https://doi.org/10.1103/PhysRev.150.1079>
- [4] F. Guerra and L. M. Morato, ``Quantization of Dynamical Systems and Stochastic Control Theory,'' Physical Review D 27, 1774--1786 (1983). <https://doi.org/10.1103/PhysRevD.27.1774>
- [5] K. Yasue, ``Stochastic Calculus of Variations,'' Journal of Functional Analysis 41, 327--340 (1981). <https://doi.org/10.1016/0022-1236(81)90079-3>
- [6] J.-C. Zambrini, ``Stochastic Mechanics According to E. Schrödinger,'' Physical Review A 33, 1532--1548 (1986). <https://doi.org/10.1103/PhysRevA.33.1532>
- [7] K. B. Wharton, ``Time-Symmetric Boundary Conditions and Quantum Foundations,'' Symmetry 2, 272--283 (2010). <https://doi.org/10.3390/sym2010272>
- [8] K. B. Wharton and N. Argaman, ``Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics,'' Reviews of Modern Physics 92, 021002 (2020). <https://doi.org/10.1103/RevModPhys.92.021002>
- [9] M. J. W. Hall, ``Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence,'' Physical Review Letters 105, 250404 (2010). <https://doi.org/10.1103/PhysRevLett.105.250404>
- [10] M. S. Leifer and M. F. Pusey, ``Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?,'' Proceedings of the Royal Society A 473, 20160607 (2017). <https://doi.org/10.1098/rspa.2016.0607>
- [11] C. J. Wood and R. W. Spekkens, ``The Lesson of Causal Discovery Algorithms for Quantum Correlations,'' New Journal of Physics 17, 033002 (2015). <https://doi.org/10.1088/1367-2630/17/3/033002>
- [12] G. W. Ford, M. Kac, and P. Mazur, ``Statistical Mechanics of Assemblies of Coupled Oscillators,'' Journal of Mathematical Physics 6, 504--515 (1965). <https://doi.org/10.1063/1.1704304>
- [13] H. Mori, ``Transport, Collective Motion, and Brownian Motion,'' Progress of Theoretical Physics 33, 423--455 (1965). <https://doi.org/10.1143/PTP.33.423>
- [14] R. Zwanzig, ``Nonlinear Generalized Langevin Equations,'' Journal of Statistical Physics 9, 215--220 (1973). <https://doi.org/10.1007/BF01008729>
- [15] B. Jamison, ``Reciprocal Processes,'' Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 30, 65--86 (1974). <https://doi.org/10.1007/BF00532864>
- [16] J. L. Doob, ``Conditional Brownian Motion and the Boundary Limits of Harmonic Functions,'' Bulletin de la Société Mathématique de France 85, 431--458 (1957). <https://doi.org/10.24033/bsmf.1495>
- [17] R. Landauer, ``Irreversibility and Heat Generation in the Computing Process,'' IBM Journal of Research and Development 5, 183--191 (1961). <https://doi.org/10.1147/rd.53.0183>
- [18] C. H. Bennett, ``The Thermodynamics of Computation: A Review,'' International Journal of Theoretical Physics 21, 905--940 (1982). <https://doi.org/10.1007/BF02084158>
- [19] T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). <https://doi.org/10.1103/PhysRevA.49.1613>
- [20] H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). <https://arxiv.org/abs/2309.10969>
- [21] H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). <https://arxiv.org/abs/2406.04571>
- [22] N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). <https://doi.org/10.1119/1.3456564>
- [23] S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). <https://doi.org/10.3389/fphy.2020.00139>
- [24] G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). <https://doi.org/10.1007/978-3-319-41285-6>
- [25] C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). <https://doi.org/10.3934/dcds.2014.34.1533>
- [26] Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). <https://doi.org/10.1007/s10957-015-0803-z>
- [27] H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). <https://doi.org/10.2514/3.3166>
- [28] J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). <https://doi.org/10.1209/0295-5075/113/60009>
- [29] M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). <https://doi.org/10.1088/1751-8121/ab7cfe>
- [30] J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). <https://doi.org/10.1063/5.0207422>
- [31] J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). <https://jmlr.org/papers/v22/20-1260.html>
- [32] C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). <https://doi.org/10.1214/13-PS220>
- [33] M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). <https://doi.org/10.1103/PhysRevE.83.061112>
