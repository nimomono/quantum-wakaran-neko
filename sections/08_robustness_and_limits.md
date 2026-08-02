@number: 8
@chapter: 本文
@title: 誤差、適用限界、反証条件、結論
@status: 3つの縮約経路について、厳密結果、近似条件、未解決接続、反証可能な残差を分離する。完成 Hamiltonian と完全周期は未完成である。

## 8.1 3経路の導出状態

| 経路 | 本論文で得た結果 | 未完成な接続 |
|---|---|---|
| 位相接続 | 有限セル正準構造、保存位相作用、固定作用下の局所分配、縮約作用、Madelung 方程式、局所 Schrödinger 型PDE、同期差保存、条件付き循環量子化 | coherent多様体の準備・維持、節、係数整合、停留点選択 |
| 配置拡散 | 正定値運動量結合、正確な配置流束、線形浴消去、自由速度相関、二側 Markov 拡散内部の Fisher 項 | Brown 極限、配置 Markov 閉鎖、古典圧力、時間対称 Newton 則 |
| 境界作用殻 | 一般殻容量、Born 型位置入口流束、作用分配次元の剛性、3モード残余ファイバー、Bell 型共同確率、Bell 前提監査 | 等方準備、一般測定器、再埋め込み、再初期化、偏った準備での非信号性 |

補助模型内部の厳密性と、現行の弱開放ミクロ模型から補助模型への接続を混同しない。

## 8.2 位相接続側の主要誤差

| 誤差 | 内容 | 理想条件 |
|---|---|---|
| $\varepsilon_{\rm coh}$ | coherent集中からのずれ | 非線形接続を代表場で閉じられる |
| $\varepsilon_\rho$ | $r^2-\rho$ | 入口同期と内部保存 |
| $\varepsilon_j$ | $j-\mathcal J_\phi r^2$ | 固定作用最小配置 |
| $\varepsilon_{\rm radial}$ | 動径慣性と高速振幅モード | 断熱的に小さい |
| $\varepsilon_{\rm press}$ | 条件付き速度分散 | 単流束化 |
| $\varepsilon_\kappa$ | $\kappa-\mathcal J_\phi^2/(2m)$ | Nelson係数一致 |
| $\varepsilon_{\rm node}$ | 節正則化と接続誤差 | 非零領域または制御された極限 |
| $\varepsilon_{\rm cross}$ | 位相活性場と配置拡散浴の交差作用 | 固定部分空間で小さい |

理想縮約方程式の残差を

```math
\mathcal R_{\rm phase}
=
\mathcal R_{\rm coh}
+
\mathcal R_\rho
+
\mathcal R_j
+
\mathcal R_{\rm radial}
+
\mathcal R_{\rm press}
+
\mathcal R_\kappa
+
\mathcal R_{\rm node}
+
\mathcal R_{\rm cross}
```

と分ける。各項を個別に小さくしても、長時間での位相誤差蓄積が小さいとは限らない。観測時間に一様な上界が必要である。

## 8.3 Born 型入口流束の誤差

理想重みは

```math
P_i^{(0)}
=
r_i^2\Delta V.
```

主要誤差は次である。

| 誤差 | 内容 |
|---|---|
| $\varepsilon_{\rm flux}$ | 法線速度、障壁、coarea Jacobian、解多重度のチャンネル差 |
| $\varepsilon_{\rm mix2}$ | 2モード殻準備の異方性と有限混合時間 |
| $\varepsilon_{\rm action}$ | $A_i-A_{\rm tot}r_i^2\Delta V$ |
| $\varepsilon_{\rm exclusive}$ | 複数入口チャンネルの同時開放 |
| $\varepsilon_{\rm reset}$ | 標本化後の活性場再埋め込みと明反応座標復元 |

直接作用分配方向が $q\neq1$ なら、これは小さい摂動ではなく構造的な変更であり、

```math
P_i
\propto
\left(
r_i^2\Delta V
\right)^q
```

となる。線形 Born 型重みは失われる。

## 8.4 配置拡散側の誤差

運動量結合経路の残差を

```math
\mathcal R_{\rm bath}
=
\mathcal R_{\rm spec}
+
\mathcal R_{\rm rec}
+
\mathcal R_{\rm mem}
+
\mathcal R_{\rm nonG}
+
\mathcal R_{\rm nonM}
+
\mathcal R_{\rm aniso}
+
\mathcal R_{\rm open}
```

と分ける。

- $\mathcal R_{\rm spec}$：有限スペクトル包絡と目標相関の差。
- $\mathcal R_{\rm rec}$：有限浴の再帰。
- $\mathcal R_{\rm mem}$：反作用記憶の非局所残差。
- $\mathcal R_{\rm nonG}$：高次 cumulant。
- $\mathcal R_{\rm nonM}$：配置射影の非 Markov 性。
- $\mathcal R_{\rm aniso}$：拡散係数の方向依存。
- $\mathcal R_{\rm open}$：外部流入・流出による補正。

さらに2経路の係数差を

```math
\varepsilon_\nu
=
\frac{
\left|
2m\nu_{\rm bath}
-
|\mathcal J_\phi|
\right|
}{
|\mathcal J_\phi|
}
```

とする。$\varepsilon_\nu$ が零へ近づかない模型では、配置拡散経路と位相接続経路は同じ有効理論へ収束しない。

## 8.5 Bell 側の誤差

第7章の理想共同法則を

```math
P_0(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}
AB\cos\Delta_{ab}
\right]
```

とする。主要誤差を

```math
\varepsilon_{\rm Bell}
\lesssim
C_{\rm loc}\varepsilon_{\rm loc}
+
C_{\rm aniso}\varepsilon_{\rm aniso}
+
C_{\rm mix}\varepsilon_{\rm mix3}
+
C_C\frac{\sigma_C}{C_0}
+
C_J\delta_J^2
+
C_{\rm jac}\varepsilon_{\rm jac}
+
C_{\rm sec}\varepsilon_{\rm sec}
+
C_{\rm mult}\varepsilon_{\rm mult}
```

と整理する。

- $\varepsilon_{\rm loc}$：左右局所測定窓の全交差応答。
- $\varepsilon_{\rm aniso}$：3モード殻接方向拡散の異方性。
- $\varepsilon_{\rm mix3}$：全殻混合不足。
- $\sigma_C/C_0$：総作用半径の幅。
- $\delta_J$：境界適合の有限分解能。
- $\varepsilon_{\rm jac}$：coarea Jacobian の結果・設定依存。
- $\varepsilon_{\rm sec}$：結果セクター基準質量の非対称。
- $\varepsilon_{\rm mult}$：解多重度と分岐の非共通性。

残余2モードの $U(2)$ 等方性は $\varepsilon_{\rm mix3}$ を制御しない。$J_+$ を含む全3モード殻の準備が必要である。

## 8.6 CHSH超過と可視度

余弦相関

```math
E(a,b)
=
-V_{\rm eff}\cos\Delta_{ab}
```

に対する標準角では

```math
|S_{\rm CHSH}|
=
2\sqrt2V_{\rm eff}.
```

理想模型が古典限界を超える条件は

```math
V_{\rm eff}
>
\frac1{\sqrt2}.
```

確率誤差が各設定で全変動距離 $\delta_{\rm TV}$ 以下なら、CHSH値のずれは粗く

```math
\left|
\delta S_{\rm CHSH}
\right|
\leq
8\delta_{\rm TV}.
```

従って十分条件は

```math
2\sqrt2V_{\rm eff}
-
8\delta_{\rm TV}
>
2.
```

Tsirelson 限界を一般原理から導いたわけではない。理想余弦則と $V_{\rm eff}\leq1$ の範囲では上限が $2\sqrt2$ になるだけである。

## 8.7 否定的結果と適用限界

1. 閉鎖 Hamiltonian 流は、一般に低次元の coherent多様体へ吸引しない。
2. 固定作用下のエネルギー最小配置は、その配置の動力学的準備を意味しない。
3. rank-one 2次モーメントだけでは非線形位相接続の標本平均を閉じない。
4. $\kappa=\mathcal J_\phi^2/(2m)$ は内部回転対称性だけから従わない。
5. 同期差保存は、同期多様体への復元力ではない。
6. 条件付き循環量子化は、節を含む Wallstrom 問題の全面解決ではない [19]。
7. 位置入口の Born 型流束は、任意基底の一般 Born 則ではない。
8. 直接作用分配方向が複数なら、入口重みは一般に $A_i$ の高いべきになる。
9. 暗モードへ作用を直接移す結合は、2モード保存則を壊す。
10. 運動量結合が速度揺らぎを作っても、その積分が Brown 運動へ収束するとは限らない。
11. $(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。
12. 二側配置拡散から Fisher 項が得られても、時間対称 Newton 則は自動的に従わない。
13. 残余2モードの $U(2)$ 等方性だけでは、Bell 結果ファイバー間の質量を決めない。
14. 固定正準接合部は Liouville 測度を保存するが、一様殻測度を単一状態から生成しない。
15. 純粋な一方向漏れは非零の定常作用殻を準備しない。
16. Bell 型余弦則は、Born 則、位相量子化、一般 Tsirelson 原理を単独では導かない。

## 8.8 反証に使える観測量

現行模型は次の量で反証または制約できる。

- coherent集中誤差と活性場2次モーメントの非 rank-one 成分。
- $j-\mathcal J_\phi r^2$ と $r^2-\rho$ の時間発展。
- $\kappa-\mathcal J_\phi^2/(2m)$。
- 巻数と粒子流速循環の不一致。
- チャンネル別の法線流束因子 $\lambda_i$。
- 入口頻度の $r_i^2\Delta V$ からのずれ。
- 標本化前後の活性場作用と $\varepsilon_{\rm reset}$。
- 浴拡散係数 $2m\nu_{\rm bath}$ と $|\mathcal J_\phi|$ の不一致。
- 配置変位の高次 cumulant、非 Markov残差、有限再帰。
- 3モード作用殻の異方性と混合時間。
- 設定別・結果別の coarea Jacobian、殻幅、解多重度。
- 開始数、入口数、記録数、完了数、再初期化数の不一致。

## 8.9 最重要の未解決問題

現在の最重要課題は次の順に整理できる。

1. 2モード入口作用殻を、場強度に対応する局所作用 $A_i$ と共通流束因子で偏りなく準備する。
2. 標本化後の結果情報を保存しつつ、活性場を coherent部分空間へ再埋め込みする。
3. 共有明反応座標、記録、garbage自由度を事後選別なしで復元し、次試行へ戻す。
4. coherent多様体上の縮約作用が、有限 Hamiltonian 粗視化運動を実際に支配することを示す。
5. 節を含む位相接続と循環量子化を制御する。
6. 運動量結合浴から Brown 極限と配置 Markov 閉鎖を導き、$2m\nu_{\rm bath}=|\mathcal J_\phi|$ を得る。
7. 同じ装置内で位相活性場、配置拡散浴、局所測定器、Bell 境界殻を同時に実現し、交差誤差を小さくする。
8. 任意基底と一般測定器へ Born 型流束を拡張する。
9. 偏った準備装置まで含めた非信号条件を示す。

中心的な未解決問題は、以前の「なぜ $r^2=\rho$ と置けるか」から、「入口でその同期を作用殻流束として作り、標本化後に同じ coherent場を復元する完全周期をどう構成するか」へ移った。

## 8.10 最終結論

有限2成分場の正準構造と位相接続を用いると、coherent縮約多様体上で Nelson--Madelung 作用、Madelung 方程式、局所 Schrödinger 型方程式を得る。保存位相作用は有効作用定数となり、単価な非零場は条件付き循環量子化を与える。

2モード作用殻の Liouville 流束は、共通流束因子と単一の直接作用分配方向の下で、位置の Born 型入口密度を与える。同じ一般作用殻幾何は、3モード境界殻の残余ファイバー体積を通じて Bell 型共同統計を与える。

運動量結合経路は、実在的な前後 Markov 拡散の候補として残る。位相接続経路との一致には

```math
2m\nu_{\rm bath}
=
|\mathcal J_\phi|
```

が必要である。

本論文は、Schrödinger 型力学、位置の Born 型重み、循環量子化候補、Bell 型統計を1つの構造化誘導場アーキテクチャへ整理した。しかし、coherent多様体の準備、2モード殻の等方化、標本化後の再埋め込み、一般測定器、完全な再初期化周期を1本の有限 Hamiltonian で完成していない。この境界を超えて主張しない。
