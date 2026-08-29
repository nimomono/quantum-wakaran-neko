@number: 8
@chapter: 本文
@title: 誤差、資源、反証条件、未完成目標
@status: 現行のM47、M48、M49、M37、M50を横断比較し、共通R135、R168、R170の台帳、系列固有誤差、有限資源、反証条件、未完成目標を整理する。有限環境純位相緩和はR123の内部構成として扱う。

## 8.1 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168のray誤差へ同時に加える。
2. R164の有限幅・枝非対称誤差を、R170の作用殻誤差と系列固有instrument誤差へ重ねて入れる。
3. R153のpaired-Hopf方向誤差を $\varepsilon_{\rm PH}$ と $L_{\rm fib}\varepsilon_{\rm fib}$ の両方へ入れる。
4. R155の積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

## 8.2 共通R170誤差

M50固定入力時刻有限枝instrumentの共通台帳は

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

である。各項の意味は次の通りである。

| 項 | 物理的由来 |
|---|---|
| $\varepsilon_{\rm hold}$ | 入力時刻の信号SWAPと保持controller |
| $\varepsilon_{\rm cap}$ | 信号作用から枝容量への結合 |
| $\varepsilon_{\rm shell}$ | 作用殻有限幅、枝対称性、fiber準備 |
| $\varepsilon_{\rm mix}$ | R161の有限時間再平衡化 |
| $\varepsilon_{\rm coll}$ | R162の有限セル・有限エネルギー衝突近似 |
| $\varepsilon_{\rm lock}$ | 入射停止、辺閉鎖、枝固定 |
| $\varepsilon_{\rm rec}$ | 局所記録pointerの有限幅と時計窓 |
| $\varepsilon_{\rm clk}$ | 操作順序とパルス面積のずれ |
| $\varepsilon_{\varnothing}$ | 閾値、境界、overflowを含む無反応質量 |

混合項は

```math
\varepsilon_{\rm mix}
\leq
C_\delta e^{-\lambda_\delta\tau_X},
\qquad
\lambda_\delta
=
\kappa_Xa_{\min}
\frac{\delta q_{\min}}{1+\delta}
\lambda_G
```

で抑えられる。$\delta\downarrow0$ では一様混合率下界が $O(\delta)$ まで低下し得る。

## 8.3 Q1の系列固有誤差

R143は共通R170を初期操作面と分析器後操作面へ適用し、M47固有項を加える。

```math
\begin{aligned}
\varepsilon_{143}
\leq{}&
\varepsilon_{170}^{\rm in}
+\varepsilon_{170}^{\rm out}
+\varepsilon_{\rm Hopf}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}\\
&+
\eta_W
+\varepsilon_{\rm lock}^{W}
+\varepsilon_{\rm br}
+\varepsilon_{\rm post}.
\end{aligned}
```

$\varepsilon_{\rm Hopf}$ はR145の有限準備、$\varepsilon_{\rm ctrl}$ は傾斜制御、$\varepsilon_{2m}$ は高モード漏れ、$\eta_W$ は左右有限コントラスト、$\varepsilon_{\rm br}$ は結果別template交換、$\varepsilon_{\rm post}$ は条件付き状態更新である。

固定有限段の逐次測定では、各段の全変動距離誤差を和で抑えられる。永久記録と使用済みcellは段数に比例して増える。Q1-2、Q1-3の中心的未解決点は、作用容量、fiber、Hopf pump、controller、記録、resetを同じ有限局所Hamiltonian周期へ統合し、仕事・熱・エントロピー収支を閉じることである。

## 8.4 Q2-1の誤差と資源

M49はM50中央4枝を二粒子位置へ直接decodeする。別の作用区間標本器の誤差は加えない。固定program $s$ の誤差は

```math
\varepsilon_{49,s}
\leq
\varepsilon_{{\rm sh},s}
+\varepsilon_{{\rm dec},s}
+\eta_{C,s}
+\eta_{z,s}
+\varepsilon_{\oplus,s}
+\varepsilon_{{\rm clk},s}
```

で分ける。benchmark運転ではfresh出力殻の準備と出力decodeを追加する。使用済み入力殻の微視的状態を出力殻へ再利用すると共同分布が歪み得る。

一programのR159入力準備節に対する単純上界は次である。

| 部品 | 正準対 |
|---|---:|
| 4モードprogram担体 | 4 |
| active中央作用殻 | 2 |
| 二粒子位置register | 4 |
| active 2翼bath | 4 |
| 2行template bank | 8 |
| 合計 | 22 |

時計、外側program schedule、benchmark用fresh出力殻、履歴、永久記録は別に加える。これは存在上界であり最小性を主張しない。稀な行の重み $\rho_a\to0$ ではbath作用上界が増大し、全program一様上界はない。

## 8.5 Q2-2の誤差とBell監査

R155は2つのR170を条件付き積因子化の下で合成する。M48完全周期の設定対ごとの誤差を

```math
\begin{aligned}
\varepsilon_{155}
\leq{}&
\delta_{\rm set}
+\varepsilon_{\rm seed}
+\varepsilon_{\rm route}
+\varepsilon_{\rm PH}
+L_{\rm fib}\varepsilon_{\rm fib}\\
&+
\varepsilon_{170}^{A}
+\varepsilon_{170}^{B}
+\eta_W^A
+\eta_W^B
+\varepsilon_{\rm prod}
+\varepsilon_{\rm reset}.
\end{aligned}
```

とする。理想singlet分布からの全変動距離が $\varepsilon_{155}$ 以下なら、一側周辺の反対設定による差は $2\varepsilon_{155}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{155}$ 以下である。

```math
\varepsilon_{155}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。

| Bell前提 | M48での位置 |
|---|---|
| 切断後局所性 | R155により完全共通原因へ条件付けて局所因子化 |
| 測定設定独立性 | A設定が中央準備へ入るため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻で決まる |
| 事後選別 | 無反応を完全結果集合へ残す |
| 非信号性 | 理想対称性で成立し、有限差を上の誤差で抑える |

従ってBellの定理を否定しない。自由設定、空間分離、一般状態receiverは達成範囲に含まない。

## 8.6 Q3の誤差

R135の有限時間誤差節はM37標本包絡の偏差を非中心化第2モーメントへ持ち上げる。R168の物理読出し対象は安全ray平均

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

である。階数1では共通rayへ縮退し、固定全作用では $R_Z^G=C_Z$ となる。一般の可変作用集団では

```math
D_{\rm tr}(R_Z,C_Z)
\leq
\frac12
\frac{\sqrt{\operatorname{Var}(Z^\dagger Z)}}
{\mathbb E[Z^\dagger Z]}
```

という半径方向補正が必要である。安全事象外は $P(\varnothing)=P(G^c)$ として残す。

R124の理想トンネル型増分を $\alpha>0$、R125の理想干渉分布距離を $\Delta>0$ とする。比較する各R170読出しの誤差が $\varepsilon_{170}$ 以下なら観測差は

```math
\alpha-2\varepsilon_{170},
\qquad
\Delta-2\varepsilon_{170}
```

以上である。M37からR170の記録までの単一Hamiltonian統合が残るため、Q3-4とQ3-5は条件付き達成である。

## 8.7 M50の資源発散

正則化により $\pi_i^\delta\geq\delta q_{\min}/(1+\delta)$ なので、有効自由エネルギー幅は

```math
\max_iE_i^\delta-
\min_iE_i^\delta
\leq
\Theta
\log
\frac{1+\delta}{\delta q_{\min}}.
```

同時に次の資源交換がある。

| 極限 | 必要になり得る資源 |
|---|---|
| $\delta\downarrow0$ | 有効地形幅 $O(\!\log\delta^{-1})$ |
| $\delta\downarrow0$ | 混合時間 $\Omega(\delta^{-1})$ |
| $\delta\downarrow0$ | 衝突流束 $\Omega(\delta^{-1/2})$ |
| 一様有限幅殻 | 剛性 $\Omega(\delta^{-2})$ |
| 周期数 $N$ | fresh cellと永久記録が少なくとも $O(N)$ |

有限資源を固定したまま厳密node、無期限熱化、永久記録、resetを同時に達成したとは扱わない。

## 8.8 Q2-3多項式資源判定

Q2-3は、固定有限普遍ゲート集合から一様に生成される $n$ 量子ビット・深さ $d$ の回路族を対象にする。入力は計算基底、目標は最終計算基底出力分布である。古典装置の結果空間は

```math
\{0,1\}^n\cup\{\varnothing\}
```

とし、$\varnothing$ は無反応または失敗を表す。量子回路の目標分布にも零重みの $\varnothing$ を加え、同じ完全結果空間上の全変動距離を $\epsilon$ 以下にする。成功試行だけを再規格化しない。

達成には、次の各資源を個別に $\operatorname{poly}(n,d,1/\epsilon)$ で抑える一様な有限古典Hamiltonian装置族が必要である。

1. 正準対または物理自由度、相互作用項、補助装置、モード、枝。
2. 回路から装置を作るcompile時間、program長、係数表と初期条件のbit記述長。
3. 準備、初期化、実行、混合、測定、記録、resetの時間。
4. エネルギー、作用、結合強度、周波数、動的範囲。
5. 制御、初期化、時刻、読出しの精度と、それを指定するbit数。
6. fresh cell、履歴、永久記録、使用済みセル、廃熱先。
7. 無反応・失敗確率と、1つの出力記録を得る期待試行回数。

指数長の表を係数へhard-codeすること、$2^n$ 個のモードまたは枝を置くこと、指数時間、指数ハードウェア並列度、指数エネルギー・作用、指数的に細かい精度、指数的に小さいgap・basin・成功確率へコストを移すことは認めない。物理パラメータの大きさと、その指定に必要なbit長は別々に数える。

M49/M50の直接モード一般化は $L=2^n$ を要するため、この判定を満たさない。これは現行候補の否定的な資源監査であり、全ての有限古典Hamiltonian方式に対するno-go定理ではない。未知の任意量子入力、適応回路、誤り訂正、量子中間測定の逐次分布は、固定目標より強い拡張として分ける。

## 8.9 反証条件

現行主張は次の検査に失敗した場合に縮小または撤回する。

| 対象 | 反証条件 |
|---|---|
| M47/R143 | Hopf方向が有限時間で準備できない、R170特殊化後もBorn型枝と局所記録が一致しない、結果別状態更新が失敗する |
| M49/R159・R160 | M50中央枝の直接decodeが1対1でない、CNOTが担体・bath・粒子位置へ同期しない、fresh出力殻で共同分布が閉じない |
| M48/R155 | 条件付き積因子化が破れる、局所R170応答が反対翼設定を参照する、無反応込みでCHSH誤差上界を満たさない |
| M37/R86・R135 | 有限時間包絡上界または第2モーメント持上げ上界を超える |
| R168 | 可変作用集団でray平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| R170 | 混合上界、局所記録の排他性、履歴単射性、正の処理時間のいずれかを満たさない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 8.10 未完成目標の優先順位

1. R170の作用容量結合、作用殻fiber内平衡化、信号保持、衝突bath、枝固定、記録を1つの有限局所Hamiltonianへ統合する。
2. M47のHopf pumpから結果別状態更新、永久記録、resetまでの周期総収支を閉じる。
3. M48のpaired-Hopf準備、2翼局所R170、controller、fresh cell流を同じ具体装置へ統合する。
4. Q3でM37入力からR170出力までを同じ有限局所装置へ統合する。
5. Q1-4について、同じ零傾斜Rabi対照と反復R143/R170測定を接続し、全履歴、tilt対照、有限誤差、資源を含む正のZeno抑制余裕を示す。
6. Q3-2について、閉路巻数、homotopy不変性、節を介した位相すべり、R86細分化安定性、非整数seamのエネルギー発散を統合する。
7. Q2-3について、$2^n$ 直接モードを避け、全資源を $n,d,1/\epsilon$ の多項式で抑える一様な有限古典Hamiltonian装置族を得る。
8. 連続空間、多粒子を扱う。

Q1-1、Q2-1、Q3-1、Q3-3は達成、Q1-2とQ1-3は部分達成、Q2-2、Q3-4、Q3-5は条件付き達成、Q1-4、Q2-3、Q3-2は未達である。三課題の再開または固定目標変更は、新しい定理・模型・数値結果を追加したことを意味しない。
