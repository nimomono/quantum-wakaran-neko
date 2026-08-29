@number: 8
@chapter: 本文
@title: 誤差、資源、反証条件、未完成目標
@status: 各モデルの誤差、資源、反証条件、Q2-3、M48完全Bell周期、置換済み模型との境界、M0の未完成条件を横断整理する。

## 8.1 モデル間受渡しと共通有効代数

Q1ではM42の受渡しを使わない。M47傾斜測定の中心誤差を

```math
\begin{aligned}
\varepsilon_{Q1}
\leq{}&
\varepsilon_{\rm prep}
+2\varepsilon_{\rm eq}
+
\varepsilon_{2m}
+
\varepsilon_{\rm ctrl}
+
\eta_W\\
&+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm br}
+
\varepsilon_{\rm post}
+
\varepsilon_{\rm ret}
\end{aligned}
```

と分ける。$\varepsilon_{\rm prep}$ は信号bath方向、零seed、位相基準の準備、2つの $\varepsilon_{\rm eq}$ は解析器前後の条件付き作用殻準備とGibbs再平衡化、$\varepsilon_{2m}$ と $\varepsilon_{\rm ctrl}$ はW型制御、$\eta_W$ は左右空間効果の有限コントラスト、$\varepsilon_{\rm lock}$ は信号bath左右占有の傾斜保持、$\varepsilon_{\rm res}$ は辺閉鎖後に単一試行の粒子位置が安全井戸を離れる経路確率、$\varepsilon_{\rm rec}$ と $\varepsilon_{\rm br}$ は局所記録と枝別テンプレート交換、$\varepsilon_{\rm post}$ は交換後方向への再平衡化、$\varepsilon_{\rm ret}$ は次周期への帰還である。前向き分布誤差と帰還誤差は同じ観測へ二重に加えない。

R145を反映し、M47の準備誤差を

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm phase}
```

と分ける。雑音零の採用開放方程式では $\varepsilon_{\rm Hopf}$ の信号bath方向成分を有限時間指数率で抑えられる。作用殻fiberと条件付き粒子位置分布はR164、R161、R162の後段準備・再平衡化で作るため、Hopf準備誤差へ混ぜない。

R164、R161、R162の1回の作用殻準備・再平衡化誤差は

```math
\varepsilon_{\rm eq}
=
\varepsilon_{\rm sh}
+
C_\delta e^{-\lambda_\delta T_X}
+
\frac{\delta}{1+\delta}
+
\varepsilon_{\rm coll}
+
\varepsilon_{\rm hold}
```

とする。$\varepsilon_{\rm sh}=\varepsilon_{\rm cap}+\varepsilon_{\rm width}+\varepsilon_{\rm sym}+\varepsilon_{\rm ad}$ はR164の作用容量結合、有限幅拘束、枝対称性、fiber内準備、第2項は有限混合、第3項は正則化、第4項は有限セル数、有限エネルギー、閾値平滑化、時計の衝突近似、第5項は再平衡化中の信号bath保持である。fiber内準備と信号bath保持を二重に数えない。R161の一様下界 $\lambda_\delta\geq\kappa_Xa_{\min}m_\delta\lambda_G$ と $m_\delta=\delta q_{\min}/(1+\delta)$ を使い、$\delta$ を零と置いて一様率を主張しない。

M37の規格化局所包絡を $\widehat b_{\rm mic}$、目標状態を $\chi_L$ とすると、任意有限基底の分布誤差は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\langle\widehat b_{\rm mic},\chi_L\rangle
\right|^2
}
```

である。M35を実装する場合は、これに準備、基底回路、読出し、比較、角切断、時計のうち実際に評価した分だけを加える。一般有限 $L$ の物理的時計配線は未評価量として分ける。

このM37からM35への受渡しは、任意有限基底の作用標本化を検査する補助診断である。M42の基本位置読出しでは、M37包絡を正則化局所跳躍核へ渡し、粒子位置を時間発展させた後に局所検出器で読む。中心誤差は

```math
\begin{aligned}
\varepsilon_{\rm Q3}
\leq{}&
\varepsilon_{\rm init}
+
\varepsilon_{\rm reg}
+
\varepsilon_{\rm disc}
+
\varepsilon_{\rm sel}
+
\varepsilon_{\rm hop}\\
&+
\varepsilon_{\rm win}
+
\varepsilon_{\rm car\to X}
+
\varepsilon_{\rm det}
\end{aligned}
```

と分ける。正則化項とM37受渡し項は

```math
\varepsilon_{\rm reg}
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}
\sqrt\rho
\right],
```

```math
\varepsilon_{\rm car\to X}
\leq
TL_{\rho,\sigma,h,R}
\varepsilon_{\rm car}(T)
\|\widetilde b(0)\|
```

である。$\rho,\sigma$ を固定してからM37弱結合量を選ぶため、節で分母が発散する循環論法を避ける。

Q2-1の固定有限ベンチマークでは、入力program選択、R157のbath--配置準備、担体CNOTと固定積分析器、出力作用区間、decode、記録を分ける。第 $s$ programのR157失敗を $\varepsilon_{157,s}$、準備・CNOT・分析器の純粋状態距離を $\delta_{\rm state,s}$、出力作用区間とdecodeの誤差を $\varepsilon_{Y,s}$、$\varepsilon_{\rm dec,s}$ とすると、

```math
\begin{aligned}
D_{\rm TV}^{\rm Q2-1}
\leq{}&
\varepsilon_S
+\sum_s\lambda_s
\left(
\varepsilon_{157,s}
+\delta_{\rm state,s}
+\varepsilon_{Y,s}
+\varepsilon_{\rm dec,s}
\right)
+\varepsilon_{\rm rec}.
\end{aligned}
```

入力、R157の配置、出力読出しには独立な三つの選択器角を使う。共有角では入力labelと結果が相関し得る。理想M49では全項が0であり、有限装置の失敗は無反応へ送る。担体、bath、粒子位置が同じCNOTを表すかは別の $\varepsilon_{\rm sync}$ で監査し、共同分布誤差へ根拠なく吸収しない。ゲート単体、行分解matching、三選択器の検査は付録Cに置く。

## 8.2 誤差の比較規則

異なるモデルの誤差を機械的に足さない。各誤差は、まず次の4分類へ置く。

| 分類 | 対象 | 扱い |
|---|---|---|
| 前向き分布誤差 | 観測開始から外部記録まで | 同じ結果空間の全変動距離へ換算して加える |
| 帰還誤差 | 記録後の逆計算とreset | 次周期の準備誤差へ渡し、同じ周期の記録へ遡って加えない |
| 状態・操作誤差 | 包絡方向、ゲート作用素、正準状態 | 測定境界移動量または出力分布距離へ換算してから比較する |
| 未評価実装量 | 配線、輸送、長期雑音、総エネルギー | 既知の上界へ数値として混ぜず、必要な入力として分ける |

M47、M48、M49、置換済みM39、置換済みM41、M42の前向き分布は対象周期と因果律が異なる。M47のQ1誤差またはM48のBell誤差へM42の最小率誤差を混ぜない。M49は共同bath座標と粒子位置を同じ行枝から準備し、M42/R113をQ2-1へ使わない。M47のR161とM48のR152は同じ平方根型詳細釣合い核を共有し、R162の有限衝突実現を利用できるが、Q1とQ2を同一ハードウェアへ統合したことにはならない。M37からM35への接続は状態方向誤差から有限基底分布誤差への数学的受渡しであり、M42の局所粒子位置力学または同一ハードウェアの構成ではない。

## 8.3 中心誤差の横断表

| 対象 | 中心指標 | 主な制御量 | 詳細 |
|---|---|---|---|
| M47のQ1可逆制御 | 共分散の作用素距離と左右遷移確率 | 2モード漏れ、傾斜面積、切替時間、$J/G$ | 第3章、付録B |
| M47のQ1測定 | 無反応込み結果分布の全変動距離、条件付きGibbs分布距離、枝別共分散距離 | 有限混合、正則化、有限衝突セル、左右コントラスト、傾斜固定、辺閉鎖、局所記録、テンプレート交換 | 第3章、付録B、付録I、付録L |
| M37 | 局所包絡の状態ノルム誤差 | 弱結合量 $\eta$、観測時間 | 第6章、付録E |
| M37からM35 | 任意有限基底の出力全変動距離 | 包絡方向誤差とM35装置誤差 | 第6.9節 |
| M42共通過程 | 粒子位置分布の全変動距離 | 初期準備、$\rho,\sigma$、時間刻み、局所選択、辺輸送、時計、検出 | 第2章、付録F |
| M35 | 補助的な作用区間分布と条件付き場準備の誤差 | 比較増幅、角切断幅、無反応 | 第2章、付録A |
| M49 | 交差モーメント、bath--粒子位置matching、共通位相を除いた操作距離、固定有限出力分布 | 行分解近似、粒子位置matching、面積誤差、一般制御誤差、作用区間選択 | 第4章、付録C、付録A |
| M47の基礎閉包 | W型左右占有率、統計核、Hopf位相円の距離、配置自由エネルギー、経路エントロピー生成 | Hopf有限時間率、rank-oneずれ、Gibbs混合率、正則化、有限衝突誤差、浴記憶 | 第8.15節、付録I、付録L |
| M48 Bell周期 | bath対距離、singlet交差モーメント、strong matching、共同分布全変動距離、帰還偏差 | setting-pre seed、safe-basin routing、paired-Hopf時間、配置混合率、局所分析、切断、記録、fresh cell | 第5章、第8.16節、付録D、付録J |
| M49--M48受渡し | cross matching、単一試行粒子位置matching、同一レジスタ搬送、setting-free性 | singlet行分解、$T_{\rm link}$、state・branch・provenance感度 | 第4章、付録C、付録K |

## 8.4 前向き誤差と帰還誤差

M47のQ1測定では、分析器、2モード漏れ、左右コントラスト、傾斜固定、無反応、記録の誤差を結果分布の全変動距離へ換算して加える。枝別テンプレート交換は条件付き共分散のtrace距離で評価し、次段の確率誤差へ移すときにだけ効果作用素の上界を使う。逆計算と周期末resetは別の $\varepsilon_{\rm ret}^{\rm M47}$ とし、次周期の準備へ渡す。

2段測定では第 $j$ 段の一様前向き誤差を $\delta_j$、第1段の条件付き状態誤差を $\delta_{\rm post}$ とすると

```math
D_{\rm TV}
\left(
p_2^{\rm obs},p_2^{\rm id}
\right)
\leq
\delta_1
+
\delta_2
+
\frac12\delta_{\rm post}
```

である。Q1-4は未達・凍結であり、反復回数に依存するZeno履歴誤差を現行上界として掲げない。

置換済みM41の旧誤差分解と有限誤差Bell監査は研究メモに保存し、現行誤差台帳には重複掲載しない。M48単独の前向き誤差、非信号周辺差、CHSH値のずれは第8.16節の $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ で管理する。M49から接続してQ2-2全体を評価するときだけ $\varepsilon_{\rm Q2-link}$ を加え、M48単独周期へ二重に算入しない。

## 8.5 資源上界

以下は明示構成の上界であり、最小性を主張しない。

| 構成 | 上界 | 非算入資源 |
|---|---:|---|
| M47 Q1能動測定器 | 固定有限段・固定精度で有限 | 条件付き作用殻fiber、容量・障壁controller、fiber内混合器、辺ゲート、有限衝突セルの最小正準対数 |
| M47 Q1永久記録 | $K$ 周期で $O(K)$ | 最適共有、無期限セル供給 |
| M35 有限 $L$ 補助セル | $3L+4$ 対 | 粒子位置通信路、外部完全周期 |
| M49 CNOT担体 | 5対 | 行分解準備、読出し、永久記録 |
| M49固定有限選択器 | 16対／固定program | 最小性、独立同分布型標本 |
| M49共同bath--粒子位置register | 固定2量子ビットで有限 | 最小性、多項式規模拡張、一般状態Bell receiver |
| M48 Bell周期 | 固定設定族・固定W型グラフで有限、記録・使用済みcellは $O(K)$ | 最小自由度、設定数依存性、無期限cell供給 |
| M42 固定 $K$ 局所更新 | $O(K(L+|E|))$ 対 | 最小性、移動式制御器、連続空間極限 |

M35の密な基底回路は高々 $L(L-1)/2$ 個の隣接2モード変換を使う。M49が内部に保持する直接モード符号化を $n$ 論理量子ビットへ拡張すると、信号だけで $2^n$ モードを要する。従って現行値をQ2-3の多量子ビット資源評価へ外挿しない。

固定 $K$ 周期なら、永久記録と使用済みreset状態を含む有限閉鎖Hamiltonian系へ埋め込める。M42の上界は各時刻層・各頂点へ判定セルを事前配置する完全局所な単純構成であり、有限次数グラフでは $O(KL)$ である。$O(L+K)$ には移動式制御器または明示的な局所通信路が必要なので現行上界にしない。無期限運転では空セル流入と使用済みセル流出を持つ弱開放系として扱う。

M47の1段測定には、信号2モード、条件付き作用殻、容量制御器、殻内混合器、条件付き障壁制御器、各辺の有限衝突セル、辺ゲート、左右テンプレート、左右記録ポインター、傾斜制御、時計、粒子位置検出部、使用済み情報セルが必要である。固定段数、固定観測時間、固定精度では有限だが、最小正準対数は未評価である。誤差は付録Mの $\varepsilon_{M50}$ で記帳する。$\delta\downarrow0$ では有効自由エネルギー幅が $O(\!\log\delta^{-1})$、必要衝突流束が $\Omega(\!\delta^{-1/2})$、一様混合率下界は $O(\!\delta)$ まで低下し得る。有限幅作用殻の一様精度には剛性 $\Omega(\!\delta^{-2})$ が必要で、$\Theta(\!\delta^{-2})$ は代表的な選択である。Zeno用の反復セル数は現行資源表から外す。

## 8.6 動作時間、エネルギー、反復

パルス面積だけを固定し、最大結合強度を制限しなければ、絶対動作時間の主張にはならない。M49内部の非負CNOT窓は $T_{\rm g}\geq\pi/g_{\max}$、reset交換は接触角 $\phi$ と結合強度 $g$ に対して $T_{\rm rst}=\phi/g$ を満たす。弱結合化は接触時間を延ばす。

M47では、傾斜切替をトンネル振動より速く、高モード間隔より遅くする必要がある。$J/G\to0$ の深いW型族は左右読出しと固定を高精度化するが、零傾斜の $x$ 回転時間は $O(\mathcal J_0/J)$ へ増える。さらに正則化誤差を下げるとR164の作用殻剛性、R161の混合時間、R162の衝突資源が増える。精度、操作時間、傾斜帯域、有効自由エネルギー幅、fiber剛性を同時に固定した任意精度定理ではない。

R163は配置部分について、正逆経路確率比、積分ゆらぎ関係、quench仕事と相対エントロピーの恒等式を与える。これはHopf pump、傾斜controller、記録、template交換、resetを含む周期総収支ではない。配置部分の熱力学台帳を全周期の台帳として二重計数しない。

M37のミクロエネルギーと各理想正準流は保存的である。M42の固定有限更新も全補助自由度を含むHamiltonian流へ埋め込むが、これは粒子位置に独立の慣性質量や保存エネルギーを割り当てたことを意味しない。一方、準備装置、時計、記録媒体、外部セル輸送、低エントロピーセル供給まで含む総エネルギー収支は未評価である。Landauer原理だけを引用して具体的resetの熱・仕事収支の代わりにはしない [17,18]。

M42の正則化最大率は

```math
\Lambda_*^{\rho,\sigma}
\leq
\frac{h_1}{\mathcal J_0\sqrt\rho}
+
\frac{d_*\sigma}{2\rho}
```

で増大する。精度を上げると必要な更新速度と比較精度が増し得るため、任意精度は固定性能の同じ装置を意味しない。またM37担体は読出し・比較・輸送窓中も発展し続け、その窓誤差を零と仮定しない。

反復可能性は、測定後信号を同じ観測内の次段へ渡すこと、記録後に内部装置を戻すこと、reset後に次周期を始めること、外部履歴を含む全系を同一点へ戻すこと、の4つを区別する。M47のR144は操作面ごとの有限時間再平衡化を用いて前3者を構成する。M48のR156はBell記録後の能動部をfresh cell交換で次周期へ戻すが、測定後状態を次段へ渡すQ1 instrumentではない。第4者は要求しない。

## 8.7 未評価量と残る資源問題

既知の上界とは別に、次が未評価である。

1. 最大結合強度と帯域を固定した最小測定間隔。
2. 一般有限 $L$ の長距離時計配線、複数段外部記録、resetセル流。
3. M47、M49、M48の長期雑音耐性と誤差蓄積。
4. 準備・時計・輸送・記録を含む総エネルギー収支と資源下界。
5. M49の $2^n$ 直接符号化を避ける多量子ビット構成。
6. M49--M48接続を一般状態へ拡張するreceiver、M48の準備後設定変更、空間分離、独立同分布型有限標本統計。
7. M42の格子細分化に対する連続空間極限、多粒子拡張、粒子位置の質量・電荷・担体エネルギーとの関係。
8. M42の初期作用比準備を含む反復周期、局所通信路、最大率・帯域・総エネルギーの精度依存性。
9. M47のHopf pump、条件付き作用殻fiber、容量・障壁controller、有限衝突セル、傾斜切替、局所記録、枝別テンプレート交換、resetを含む総エネルギー・エントロピー収支。

これらは既存上界の未記入係数ではなく、追加の物理構成または別の定理を要する課題である。特に多量子ビットの規模依存性を扱うQ2-3は未着手である。

## 8.8 一般有限次元への拡張

M35はQ2・Q3について一般有限 $L$ の固定準備・固定基底、Born型長期頻度、条件付き場準備、内部逆計算を与える。これをM48の固定Bell周期を越える一般有限次元測定周期へ拡張するには、次が必要である。

1. 一般有限 $L$ の複数段異基底測定と独立選択器。
2. 外部記録セルへの結果非依存正準コピー。
3. 一般有限 $L$ の外部resetセル交換。
4. 空間的に離れた各辺への時計配線と遅延上界。
5. 自由度、時計窓、外部セルの規模依存性。

2モードの結果で記号 $L$ だけを置き換えたものは一般化と数えない。

## 8.9 量子ゲート型計算機の実装コスト（Q2-3）

Q2-3には、$n$ 論理量子ビット、回路深さ $d$、目標誤差 $\epsilon$ に対する少なくとも次の増加率が必要である。

1. 信号と補助装置の正準対数。
2. 局所結合数、最大並列度、時計窓数、動作時間。
3. 制御角、比較器、resetセルの必要精度。
4. 永久記録と使用済みセルの容量。
5. 隠れた指数コストの有無。

M49内部の直接モード符号化は信号だけで $2^n$ モードを要する。ゲート担体5対、固定program選択器16対という現行上界はQ2-3の達成ではなく、指数コストを監査する出発点である。

## 8.10 M49--M48受渡しと未達拡張

M41は置換済み模型であり、その旧条件付き達成評価を現行Q2-2根拠へ戻さない。R157はM49で共同状態とcross matchingと単一試行粒子位置matchingを同じ行枝から準備し、R158はその同じregisterへCNOTを点ごとに作用させる。R160は固定singlet入力について、設定生成前の面で同じ $(z_A,z_B,X_A,X_B)$ を恒等port $T_{\rm link}$ によりM48へ渡す。従って付録Kの固定singlet受渡し契約は構成済みである。

この結果を越えるには、準備後の自由な設定変更、空間的に隔たった設定選択、有限伝播速度を持つ長距離時計配線、一般状態を受けるBell receiver、独立同分布型有限標本統計を別々に扱う。これらを現行singlet型の誤差係数へ吸収してはならない。

state-carrying監査では、R160の受渡し面において2つ以上の射影類が区別可能に残ることを要求する。branch-carryingでは入力枝bias $p$ を保存し、provenance-onlyでは履歴条件付きでも結果法則を変えないことを検査する。M49の恒等portは3条件を満たすが、M48の結果法則を与える現行定理は固定singletに限る。旧R151の反対称filterは入力状態を固定 $\mathsf E$ へ潰し、等重み枝を内部fair seedで代替できたため、state-carrying条件を満たさなかった。

## 8.11 反証または範囲縮小の条件

個別の数値検査を再掲せず、主張を変更すべき条件を結果群ごとにまとめる。数値検算の個別項目は `VALIDATION.md` で管理する。

| 結果群 | 反証または範囲縮小が必要な条件 |
|---|---|
| M47 Q1可逆制御 | 階数1共分散がBloch球を与えない、傾斜生成子が $\mathfrak{su}(2)$ を張らない、離調Rabi式または共分散保存が解析式と一致しない |
| M47 Q1測定 | 左右効果がR142と一致しない、R164の作用分解・2作用殻線形容量・単一母測度規格化・有限幅上界が破れる、R161の定常分布・一様ギャップ上界・正則化誤差が破れる、R162の衝突率・粗視化有効エネルギー保存・有限セル誤差が破れる、辺閉鎖後の離脱率が $\varepsilon_{\rm res}$ を超える、局所記録が統計振幅や全密度を入力にする、枝別テンプレート交換後の条件付き共分散がR143上界を超える、無反応を事後除外する |
| M47 Q1周期 | 操作面ごとの作用殻準備と再平衡化を実行せず無条件完全周期と記す、R163の有効仕事・熱をfiberとcontrollerを含む全微視的収支と扱う、外部記録または使用済み状態を消して非可逆化する、作用殻・保持・帰還誤差を同じ周期の記録分布へ二重加算する |
| Q1-4 Zeno効果 | 凍結中に達成済みと記す、傾斜離調・障壁増大・駆動停止・摩擦・事後選別をZeno抑制と呼ぶ |
| M37包絡 | $\eta<1$ の範囲で生成子上界または有限時間状態上界が破れる、正常モード包絡を局所場として扱う |
| M42粒子位置 | 局所連続方程式または等変性が破れる、正則化誤差がR115の節一様上界を超える、非隣接跳躍または複数粒子位置分裂が生じる、履歴を消して非可逆化する、固定時刻検出を初回到達分布と同一視する |
| M35測定 | 完全結果集合が入力を覆わない、Born型長期分布が無反応上界を超える、測定後状態または逆計算が定理と一致しない |
| M49共同bath--粒子位置CNOT | 行分解の交差モーメントまたは粒子位置周辺が目標係数と一致しない、点ごとのCNOTがbathと粒子位置に同じ写像を与えない、局所代数が可換でない、面積 $\pi$ 流がCNOTでない、実流が正準性・作用保存を破る、固定有限出力分布がR159上界を超える |
| M49--M48受渡し | setting-free面より前に設定が入る、同じbath・粒子位置registerを運ばない、singlet fiberまたは枝biasを保存しない、provenance履歴が結果形成へ入る、R160の接続誤差上界を超える |
| M48 Bell周期 | R151の受渡しが破壊的単一portでない、R152が正規化・詳細釣合い・一意混合を失う、R153のfiber上界を超える、切断後に反対翼設定が局所生成子へ入る、無反応を再規格化する、R155またはR156の上界が破れる |
| Q3-2位相量子化 | 凍結中に達成済みと記す、再開時に補間が量子化条件を暗黙に仮定する、零点なしに巻数が変化する、非整数モノドロミーのエネルギーが細分化しても有界に残る |
| Q3-3束縛状態 | 非対角相関の減衰を外部乱数として直接仮定する、有限環境Hamiltonianまたは縮約を示さない、エネルギー占有率が許容値を超えて変化する、コヒーレンス回復を無視する |
| Q3-4トンネル効果 | 初期状態に障壁値以上のスペクトル成分が残る、反対側確率の増分が正でない、初期の反対側裾を無視する、位置読出しへの接続誤差が増分以上になる |
| Q3-5干渉 | コヒーレント入力と非干渉混合の位置分布が一致する、相対位相を変えても位置分布が変わらない、位置読出しへの接続誤差が分布差以上になる |
| M45開放準臨界準備 | 能動項を外しても同じ準備殻が現れる、位相すべり後の自律帰還が再現しない、捕捉位相体積比が指数則から大きく外れる、$W(X)$ の局所帳簿に二重計数が残る、時間切片則または位置核の周辺可逆性が成立しない、条件付き基底密度比較が格子細分化で収束しない |
| M47 W型共同統計 | 古典作用角からR135の共分散回転が出ない、W型交差項がR136の左右占有振動と一致しない、R145の信号bath方向吸引が破れる、R164の条件付き作用殻結果だけで作用容量結合・fiber内平衡化・枝対称性を自然発生と扱う、R161の零node no-goを無視して $\delta=0$ の一様局所混合を主張する、準備散逸・位相固定・浴記憶・2モード外漏れが観測時間で残る、大域階数1を枝別固有状態と同一視する |
| 文書上の範囲 | M37の時間非依存定理だけで時間依存傾斜をミクロ導出済みと扱う、M42/R113を現行Q1・Q2-1・M48へ使う、R162またはR164だけでHopf準備またはpaired-Hopf周期全体をミクロ導出済みと扱う、R163の有効仕事・熱を全微視的収支と扱う、M49相関またはM48を空間分離Bell統計と扱う、固定singlet接続から一般状態receiverを推論する、生成物と正本が食い違う |

目的共同分布を設定条件付き初期測度へ直接書き込み、R151--R153の前向き準備を省いた場合、M48の中心主張は成立しない。無反応試行を除外して共同分布またはCHSH値を再規格化した場合は事後選別となり、現行判定を使えない。

## 8.12 次の目標と統合課題

中心課題は次の6本である。

1. M47のQ1について、R164の作用容量結合、fiber内平衡化、枝対称性、信号bath保持反作用を有限局所Hamiltonianとして構成し、R145のHopf pump、R162の衝突熱浴、傾斜切替、局所記録、template交換、resetと同じ有限時間台帳へ統合する。Q1-4は判定基準を保ったまま凍結する。
2. Q2-3として、M49内部の $2^n$ 直接モードコストを監査し、多量子ビット回路の物理自由度、時間、精度、記録、resetの規模依存性を評価する。
3. Q3-2は判定基準を保持したまま凍結する。達成済みのQ3-3からQ3-5についてはR123--R125の有限モード・有限時間範囲を維持し、源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを独立した強い拡張として管理する。
4. R160の固定singlet接続を基点に、R164の各翼作用容量fiberとR162の衝突熱浴をpaired-Hopf準備・seed routing・2翼controllerへ統合し、準備後設定変更、空間分離、一般状態receiver、独立同分布型標本統計を検査する。
5. M45について、開放捕捉器の準臨界殻、位相すべり、自律帰還、捕捉エントロピー則の頑健性を検査し、$W(X)$ の局所帳簿、時間比例切片則、位置核の周辺可逆性という3つの橋を直接結合模型から導けるかを判定する。
6. Q2-1から外れたM42を全面退役させるため、Q3の固定時刻位置読出しをtransducerなしの共同統計から再導出する。

一般有限 $L$ への拡張はM35のQ2・Q3一般化課題として並行して管理する。M47、M48、M49、M37、M35、M42を1つのM0と統一母測度へまとめることは、その後の統合目標である。M39とM41は置換済み研究メモとして統合対象から外す。

## 8.13 M45開放自己組織化準臨界準備

M42のBorn型等変性には、開始時の粒子位置分布を複素振幅場の作用比へ合わせる準備が必要である。M45は、物理ポテンシャル $V(X)$ の正の定常基底状態に限り、目的固有関数を装置へ直接入力せずに、この分布を作れるかを調べる現行補助モデルである。

M45は、一つの熱的環境と非平衡自由エネルギー源へ接続された、一つの非線形準安定捕捉器を開放有効模型として採用する。局所状態は周期反応座標 $s$、対数型捕捉エントロピー座標 $r$、対応する運動量 $p_s,p_r$ である。ポテンシャルを

```math
U_C(s,r)
=
U_0(1-\cos s)
+
\frac{\Theta}{2}
\log
\left[
1+
\left(
\frac{r-c\sin s}{r_0}
\right)^2
\right]
```

とし、分離エネルギーを $E_{\rm sep}=2U_0$ とする。Itô規約の運動方程式は

```math
ds=v_s\,dt,
\qquad
dr=v_r\,dt,
```

```math
dp_s
=
\left[
-\partial_sU_C
-\gamma_sv_s
+
\alpha
\left(
1-\frac{v_s^2}{v_*^2}
\right)v_s
\right]dt
+
\sqrt{2\gamma_sT_b}\,dB_s,
```

```math
dp_r
=
\left[
-\partial_rU_C
-\gamma_rv_r
\right]dt
+
\sqrt{2\gamma_rT_b}\,dB_r
```

である。ここで $v_s=p_s/M_s$、$v_r=p_r/M_r$ である。Rayleigh型能動項は低速で注入、高速で抑制し、周期障壁、受動散逸、熱雑音との釣り合いで分離面近傍の有限幅殻を維持する。この意味だけで「自己組織化準臨界」と呼ぶ。厳密な相転移、熱力学極限、普遍的べき則、無調整の臨界到達は主張しない。

局所エネルギー

```math
E_C
=
\frac{p_s^2}{2M_s}
+
\frac{p_r^2}{2M_r}
+
U_C
```

は、R127の厳密なItô恒等式

```math
dE_C
=
\left[
F_A(v_s)v_s
-\gamma_sv_s^2
-\gamma_rv_r^2
+
\frac{\gamma_sT_b}{M_s}
+
\frac{\gamma_rT_b}{M_r}
\right]dt
+
\sqrt{2\gamma_sT_b}\,v_s\,dB_s
+
\sqrt{2\gamma_rT_b}\,v_r\,dB_r
```

を満たす。定常平均では能動仕事、受動散逸、Itô熱流入が釣り合う。能動項を維持するには熱浴と区別された自由エネルギー源が必要であり、M45はエネルギー無消費模型ではない。

位相すべり率またはリセット写像は運動方程式へ入れない。実数直線へ持ち上げた周期セル番号が変わるときに位相すべりを観測し、その後 $E_C<E_{\rm sep}$ が確認時間だけ続いたときを帰還と数える。直接積分で観測される帰還は連続軌道の自律帰還である。準備されるのは未来の雑音波形でなく、定常時刻に準備領域へある局所状態で条件付けた現在の共同測度である。

対数座標により、1周期セルのLiouville劣位相体積は高エネルギー側で

```math
\Omega_C(E)
=
C_C
\exp(E/\Theta)
\left[
1+o(1)
\right]
```

となる。R128は、接触時の利用可能内部エネルギーが

```math
W(X)
=
V(X)-V_{\min}
```

だけ減り、同次数の位置依存Jacobianがなければ、

```math
\frac{\Omega_C(E-W(X))}{\Omega_C(E)}
=
\exp
\left[
-\frac{W(X)}{\Theta}
\right]
\left[
1+o(1)
\right]
```

となることを与える。多数の調和内部モードを置かず、1個の対数座標で指数状態密度を作る。

ただしM45の直接方程式は粒子位置 $X$ をまだ含まない。次の3点は未導出の橋である。

1. $V$ を二重計数せず、$W(X)$ だけ内部利用可能エネルギーから差し引く局所結合
2. 1回の位相体積選別を、短時間 $\delta$ に比例する準備率へ変える弱接触切片則
3. 能動捕捉器を消去した位置周辺核の可逆性

総接触時間を $T$、切片数を $N$、$\delta=T/N$ とし、完全接触因子の $1/N$ 乗を各端点因子へ割り当てると仮定する。$\Theta=4m\nu/T$ の尺度整合の下で

```math
A_\delta(X)
=
\exp
\left[
-\frac{\delta W(X)}{4m\nu}
\right]
```

を得る。さらに無偏向基準位置核

```math
K_\delta
=
I+\delta\nu\partial_X^2+o(\delta)
```

と周辺可逆性を仮定し、

```math
G_{\delta,V}
=
A_\delta K_\delta A_\delta
+
o(\delta)
```

とすれば、R129は

```math
G_{\delta,V}
=
I
-
\frac{\delta}{2m\nu}
\left(
H_V-V_{\min}
\right)
+
o(\delta),
\qquad
H_V
=
-2m\nu^2\partial_X^2+V
```

を与える。対称作用素の左右主固有関数は同じ $h$ となり、形成方向と保持方向の積から準備密度は $h^2$ に比例する。連続極限で $h\to\phi_0$、$H_V\phi_0=E_0\phi_0$ なので、

```math
\rho_0(X)
=
\phi_0(X)^2
```

を得る。二方向は二つの浴でなく、一つの捕捉器の形成方向と保持方向であり、右因子だけでなく左右因子の積を作る役割を持つ。

主固有関数によるDoob変換[16]は

```math
b_+
=
2\nu\partial_X\log\phi_0,
\qquad
b_-
=
-2\nu\partial_X\log\phi_0
```

を与える。従って $v=0$、$u=\nu\partial_X\log\rho_0$ であり、Nelsonの時間対称加速度[3--6]は

```math
a_N
=
-uu'-\nu u'',
\qquad
ma_N
=
-V'
```

を満たす。これは3つの橋を仮定した後の定常基底sectorの条件付き結果であり、直接局所軌道の加速度から得た結果ではない。

現行数値コードは `simulations/m45_open_quasicritical/` に置く。直接Langevin検査では、分離面近傍率0.8275、3096離脱エピソード中2959件の有限時間帰還、平均収支残差 $3.45\times10^{-6}$ を得た。能動項を外した対照の分離面近傍率は0である。捕捉位相体積比の対数傾きは $-1.0673$、指数目標からの最大偏差は0.0220だった。これとは別に、3つの橋を入力した条件付き位置作用素監査では、量子基底密度との全変動距離が調和型0.00404、二重井戸型0.00882となった。後者を直接模型の量子基底状態再現とは呼ばない。

M45とR127--R129はM37、M47、M42、R118、M35を置換せず、M45単独でQ1--Q3の現行達成判定を変更しない。正の主固有関数を選ぶため一般の励起状態を準備せず、一般の時間依存Nelson流、複素位相、Schrödinger時間発展を導かない。完全な方程式、位相体積積分、数値事象定義、条件付き作用素、反証条件は付録Hに示す。

## 8.14 M46から保持する補助結果と不採用部分

旧M46は、物理的複素振幅場から局所current rateを作り、粒子位置を動かし、その粒子位置がcapacityを消費する三角形因果律を採用していた。M47では複素振幅を粒子位置--浴共同統計の後に定義するため、この因果律を同時に使うと循環する。従ってM46、R133、R134は現行因果模型から外し、完全な旧式、不採用理由、再検討条件を `notes/rejected_m46_current_transducer.md` で管理する。

一方、R130--R132の有限次元計算にはcurrent transducerと独立に再利用できる部分がある。本節ではその条件と限界だけを保持する。

作用尺度を

```math
\mathcal J_0
=
\frac{\Theta}{\omega_c}
=
2m\nu
```

とする。残りenergy $Z$ をaction capacity $I=Z/\omega_c$ へ換算すると、理想ready分布は

```math
P(I>i)
=
\exp
\left(
-\frac{i}{\mathcal J_0}
\right).
```

準備モードで採用する三角形loading則は

```math
\dot I_t
=
-W(X_t),
\qquad
W=V-V_{\rm ref}\geq0.
```

energy表示では $\dot Z=-\omega_cW(X)$ なので、$\dot Z=-\alpha W(X)$ の規約で

```math
\alpha=\omega_c,
\qquad
\nu
=
\frac{\Theta}{2m\omega_c}
```

となる。これは旧M46が置いた一回のaction matchingであり、M45の回路定数またはM47の共同統計から導出した普遍関係ではない。

R130は指数分布の無記憶性から、位置経路を固定したready生存率を

```math
D[X]
=
\exp
\left[
-\frac{1}{\mathcal J_0}
\int_0^tW(X_s)\,ds
\right]
```

とする。有限グラフの1周期では

```math
\mathsf P_\delta
=
K_\delta D_\delta,
\qquad
D_\delta
=
\exp
\left(
-\frac{\delta W}{\mathcal J_0}
\right),
```

である。$\mathsf P_\delta$ は古典的な非正規化生存核である。

古典thresholdだけでは複素振幅の平方根則は出ない。R131では、同じ係数を持つphase-preservingな線形散逸応答を条件として置き、

```math
\dot b_x
=
-\frac{W(x)}{2\mathcal J_0}b_x
```

を与えると採用する。R131により

```math
A_\delta
=
\exp
\left(
-\frac{\delta W}{2\mathcal J_0}
\right)
=
D_\delta^{1/2}
```

となる。複素共分散核は

```math
\mathsf S_\delta
=
A_\delta K_\delta A_\delta
```

であり、古典生存核とは

```math
\mathsf S_\delta
=
A_\delta
\mathsf P_\delta
A_\delta^{-1}
```

の相似関係にある。確率核と共分散核を同じ記号で呼ばない。

正のグラフLaplacian $L_{\mathcal G}$ について

```math
K_\delta
=
\exp
\left(
-\delta\nu L_{\mathcal G}
\right)
```

とすれば、

```math
\mathsf S_\delta
=
I
-
\frac{\delta}{\mathcal J_0}
\left(
H_V-V_{\rm ref}
\right)
+
O(\delta^2),
```

```math
H_V
=
\mathcal J_0\nu L_{\mathcal G}+V
=
\frac{\mathcal J_0^2}{2m}L_{\mathcal G}+V
```

を得る。

準備モードの線形化を

```math
Y_{n+1}
=
g\mathsf S_\delta Y_n
+
\eta_n
```

とする。$\mathsf S_\delta h_0=\lambda_0h_0$、$h_0>0$ とし、雑音が主モードへ非零成分を持つなら、R132は $g\lambda_0\uparrow1$ で規格化共分散が

```math
\frac{C_g}{\operatorname{tr}C_g}
\longrightarrow
\frac{|h_0\rangle\langle h_0|}
{\langle h_0,h_0\rangle}
```

へ収束することを与える。ただし、この線形共分散極限だけでは粒子位置周辺が $h_0^2$ になること、有限振幅Hopf定常測度がrank-oneへ集中すること、一般複素相対位相を準備すること、切断後にmatchingが保存されることは従わない。R130--R132の詳細な保持範囲は付録I.3に示す。

R133の有限グラフcurrent恒等式と、R134のSchrödinger--Madelung式を仮定した後のNelson恒等式は、旧M46内の解析結果として誤りとはしない。ただし新しい統計場解釈のミクロ因果律には使わず、現行本文の結果鎖から外す。R130--R132もM47のmatching準備を自動的に与えない。

## 8.15 M47 W型2モード Hopf共同統計模型

M47は対称W型ポテンシャルの最低2モードだけを対象とする。M37から得る実対称生成子を

```math
h_W
=
\frac{\mathcal J_0^2}{2m}L_W+V_W
```

とし、最低2モードの固有対を

```math
h_W\phi_0=E_0\phi_0,
\qquad
h_W\phi_1=E_1\phi_1,
\qquad
E_0<E_1
```

とする。$\phi_0$ は実偶モード、$\phi_1$ は実奇モードである。ここで $h_W$ は古典振動子網の包絡生成子であり、量子Hamiltonianを入力していない。

各試行の実在状態を

```math
\Gamma_t=(X_t,\xi_t)
```

とし、共同測度を $\mu_t(dX\,d\xi)$ とする。浴 $\xi$ に含まれる二作用角から $Z_0,Z_1$ を作り、規格化共分散を

```math
C_{mn}[\mu_t]
=
\frac{E_{\mu_t}[Z_mZ_n^*]}
{E_{\mu_t}[Z^\dagger Z]}
```

とする。空間核は

```math
K_W[\mu_t]
=
\Phi C[\mu_t]\Phi^\dagger,
\qquad
\Phi c=c_0\phi_0+c_1\phi_1
```

である。matching多様体を

```math
\mathcal M_W
=
\left\{
\mu:
\operatorname{rank}C[\mu]=1,
\quad
P_\mu(X=i)=K_{W,ii}[\mu]
\right\}
```

と定める。$\mu\in\mathcal M_W$ なら $C=cc^\dagger$ と因数分解でき、

```math
\psi_W^{\rm stat}[\mu]=\Phi c
```

を共通位相を除いて定義する。複素振幅は独立場でなく、粒子位置周辺とbath共分散が同じ共同測度上で一致した後の統計因子である。

準備と伝播は外部制御 $\lambda_{\rm prep}(t)$ で分ける。$\lambda_{\rm prep}>0$ の間はreservoir、能動供給、散逸、外部位相基準へ接続した開放Hopf系とし、所定の回転軌道近傍へ吸引する。$\lambda_{\rm prep}=0$ にすると準備portを切り、二作用角の閉鎖Hamiltonian

```math
H_{\rm rot}
=
\sum_{n=0}^1
\frac{E_n}{\mathcal J_0}I_n
```

だけを残す。内部latchまたは反応座標 $s$ を切替器に使わない。

R135はこの古典Hamiltonianから

```math
i\mathcal J_0\dot C=[D_W,C],
\qquad
D_W=\operatorname{diag}(E_0,E_1)
```

を厳密に導く。trace、正値性、rankは保存される。rank-one因子は

```math
c(t)
=
\exp
\left[
-\frac{iD_W(t-t_0)}{\mathcal J_0}
\right]c(t_0)
```

と回転する。

係数の大きさを $a_0,a_1$、bath相対角を $\delta=\theta_1-\theta_0$ とすると

```math
\delta(t)
=
\delta(t_0)
+
\frac{E_1-E_0}{\mathcal J_0}(t-t_0).
```

R136はmatching条件下の配置密度を

```math
\rho(x,t)
=
a_0^2\phi_0(x)^2
+
a_1^2\phi_1(x)^2
+
2a_0a_1\phi_0(x)\phi_1(x)\cos\delta(t)
```

と与える。左井戸射影 $\Pi_L$ と

```math
B_W=\langle\phi_0,\Pi_L\phi_1\rangle
```

を使えば

```math
P_L(t)
=
\frac12
+
2a_0a_1B_W\cos\delta(t).
```

等重みでは角周波数と周期が

```math
\Omega_W
=
\frac{E_1-E_0}{\mathcal J_0},
\qquad
T_W
=
\frac{2\pi\mathcal J_0}{E_1-E_0}
```

となる。基底または第1励起モード単独では交差項が消えて密度が定常だが、2モード重ね合わせでは左右分布が振動する。この解析式がM47の閉鎖伝播の中心検査である。

R137は、切断直後に $\mu_{t_0}\in\mathcal M_W$ であり、完全な閉鎖古典流が観測時間中に $\mathcal M_W$ を保存すると仮定した場合、$\psi_W^{\rm stat}$ の2モード生成子式と $P(X=i)=|\psi_{W,i}^{\rm stat}|^2$ が同時に保たれることを示す。matching保存は仮定であり、同じ局所Hopf--bath方程式から未導出である。

R138は一様な古典ラベルと逆累積分布を使い、任意のR135密度を各時刻の $X$ 周辺として実現できることを示す。これは量子力学を使わない決定論的古典存在構成だが、全密度を先に使う逆設計であり、自然な局所粒子位置軌道、有限伝播、bath反作用を与えない。

Q1では、一般2モードHamiltonian $H_G=Z^\dagger G(t)Z$ へ拡張する。R139は階数1共分散をBloch球へ縮約する。W型へ1次傾斜を加えると、局在基底の生成子は

```math
G_F(t)
=
-J\sigma_x
+
\frac{\varepsilon(t)}{2}\sigma_z
```

となる。R140はこの2方向が $\mathfrak{su}(2)$ を生成し、任意の $SU(2)$ と離調Rabi式を与えることを示す。R141は

```math
J
\ll
|\varepsilon_m|
\ll
G,
\qquad
\frac{\mathcal J_0}{G}
\ll
\tau_q
\ll
\frac{\mathcal J_0}{J}
```

の尺度階層で傾斜を立ち上げる。任意の2モード共分散について左右占有率の変化を $2|J|/\sqrt{\varepsilon_m^2+4J^2}$、局在射影からの反対井戸遷移をより強い $4J^2/(\varepsilon_m^2+4J^2)$ で抑え、全W型では2モード漏れを別に加える。これは各時刻の周辺分布上界であり、単一試行の $X$ が同じ井戸へ滞在する経路上界ではない。

左右空間射影は有限障壁では厳密な2値射影でない。$B_W=\langle\phi_0,\Pi_L\phi_1\rangle$、$\eta_W=1/2-B_W$ とすると、R142は左読出し効果を

```math
E_L
=
(1-\eta_W)|L\rangle\langle L|
+
\eta_W|R\rangle\langle R|
```

と与える。深いW型族で $\eta_W\to0$ の場合に、任意軸Born重みへ近づく。

R145は採用開放Hopf方程式により信号bath方向を階数1位相円へ準備する。R164は、その後の単一試行bath座標 $z$ の信号作用を枝容量

```math
A_i^\delta(z)
=
\mathcal J_0
\left[
|(\Phi z)_i|^2
+
\delta q_i z^\dagger z
\right]
```

へ写し、排他的2作用殻を単一Liouville母測度で数えると状態数 $\Omega_i^\delta\propto A_i^\delta$ が得られることを示す。規格化状態数は

```math
\pi_i^\delta(z)
=
\frac{|(\Phi z)_i|^2/(z^\dagger z)+\delta q_i}{1+\delta}
```

であり、R161はこれを条件付きGibbs分布として、平方根型局所率の詳細釣合い、一意定常分布、全ray一様の有限時間混合率を与える。$E_i^\delta=-\Theta\log\pi_i^\delta$ は作用殻fiberを消去した条件付き中間状態有効自由エネルギーである。R162は、到着粒子の運動エネルギーが指数分布を持つ有限衝突bathと粗視化された有効自由エネルギー保存散乱から同じ率を作り、有限セル、有限エネルギー、閾値平滑化、時計、保持の誤差を分ける。再平衡化後に入射を止めて辺ゲートを閉じることで、記録中の経路滞在失敗も有限誤差化する。

R143は、Hopf方向準備、初期再平衡化、解析器、分析後再平衡化、傾斜固定、辺閉鎖、左右井戸の局所記録、結果別2モードテンプレート交換、交換後再平衡化を順に合成する。記録相互作用は $X$ の局所関数だけを入力にし、統計振幅、共分散、全密度、確率流またはM42/R113を使わない。大域階数1共分散は枝別測定後状態を意味しないため、R143は枝別共分散を独立に評価する。

R144は固定有限段の記録、逆計算、外部空セル交換を合成する。各操作面でR164の作用殻準備とR161、R162を有限時間作用させるため、分析器中または周期間の連続matching保存を仮定しない。R163は条件付き配置中間状態の正逆経路確率比、積分ゆらぎ関係、有効quench仕事と相対エントロピーの恒等式を与える。ただし作用容量結合、fiber内平衡化、枝対称性、信号bath反作用の有限局所Hamiltonian統合と、周期総収支は閉じていない。

従ってM47の導出状態は次の通りである。

| 内容 | 状態 |
|---|---|
| 古典作用角からの共分散回転 | R135、厳密 |
| W型2モードの密度、current、左右占有振動 | R136、厳密 |
| matching保存後の統計振幅閉包 | R137、条件付き |
| 共同測度の古典的存在 | R138、逆設計存在構成 |
| 階数1共分散のBloch縮約 | R139、厳密 |
| 傾斜による任意の $SU(2)$ と離調Rabi式 | R140、2モード内で厳密 |
| 傾斜による左右占有周辺の固定 | R141、2モード内で厳密、全W型では明示誤差付き |
| 左右粒子位置のBorn型読出し | R142、有限コントラスト |
| 局所記録と枝別状態更新 | R143、有限再平衡化・辺閉鎖・無反応誤差付き |
| 固定有限弱開放周期 | R144、操作面ごとの再平衡化に条件付き |
| 採用開放Hopf方程式による信号bath方向準備 | R145、雑音零の方程式後に厳密 |
| 条件付き作用殻からのBorn型状態数と有効自由エネルギー | R164、条件付き厳密結果＋滑らかな有限幅近似 |
| 任意の階数1方向への条件付きGibbs再平衡化 | R161、正則化後に一様有限時間率 |
| 局所詳細釣合い率の有限衝突熱浴実現 | R162、有限セル・有限エネルギー誤差付き |
| 配置quenchと再平衡化のゆらぎ関係 | R163、粗視化配置過程と有効仕事で厳密 |
| 作用容量結合、fiber内平衡化、枝対称性、反作用の有限局所Hamiltonian | 未導出 |
| Hopf pumpからresetまでの周期総収支 | 未導出 |

この改訂でQ1-1は達成、Q1-2とQ1-3は部分達成、Q1-4は未達・凍結を維持する。Q1-2の残件は作用殻起源を有限局所Hamiltonian周期へ統合すること、Q1-3の残件はfiberを含む周期総収支であり、旧い連続matching保存問題ではない。M42/R113はQ2-3とQ3だけに残す。R139--R145、R161--R164の定義、証明、誤差目標は第3章、付録B、付録I、付録L、付録Mに示す。

## 8.16 M48設定依存paired-Hopf完全Bell周期

M48は設定前の共通基準測度 $\nu_0$ から、設定生成後のA設定 $x$ に依存する決定論的開放流で2翼bath対を準備する。bright変数とdark変数を

```math
m
=
\frac{z_A-\mathsf E\overline{z_B}}{2},
\qquad
d
=
\frac{z_A+\mathsf E\overline{z_B}}{2}
```

とし、

```math
\frac{dm}{d\tau}
=
g(1-m^\dagger m)m
+
\kappa h_x(m)
\left(
\Sigma_x-h_x(m)I_2
\right)m,
```

```math
\frac{dd}{d\tau}
=
-\kappa_{\rm p}d
```

を採用する。$h_x=m^\dagger\Sigma_xm/(m^\dagger m)$ である。動径供給・飽和、設定依存整列、dark散逸、外部切断を持つ開放古典模型であり、有限閉鎖Hamiltonian系から導出したとは呼ばない。

R146は積標本 $z_A\otimes z_B$ の直接4次元共分散をsinglet階数1射影へできないことを示す。M48は代わりに交差モーメント

```math
M_{AB}^{G}
=
\mathbb E
\left[
\mathbf1_{G_x}z_Az_B^{\mathsf T}
\right]
```

を使う。R147は $|h_x(m_0)|\geq h_*>0$ で2枝吸引多様体への有限時間率

```math
\gamma_{48}
=
\min
\left\{
2g,2\kappa,\kappa_{\rm p}
\right\}
```

を与える。Haar方向基準測度では盆無反応率は $h_*$、安全な2枝の質量はそれぞれ $(1-h_*)/2$ である。

R148は全ての有限A設定について

```math
M_{AB}^{G}(\infty\mid x)
=
-\frac{1-h_*}{2}\mathsf E,
\qquad
B_{AB}(\infty\mid x)
=
-\frac{\mathsf E}{\sqrt2}
```

を与える。規格化交差モーメントをベクトル化した階数1射影は $\beta_{\rm s}\beta_{\rm s}^\dagger$ であり、$x$ に依存しない。これは集団統計であり、単一試行の2値結果ではない。

R149は2翼の完全matchingと局所instrumentを抽象的に仮定した後に

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left(
1-ab\,n_x\cdot n_y
\right)
```

を与える。平面内では相関は $-\cos(x-y)$ である。有限時間の盆境界は無反応として完全結果集合へ残し、再規格化しない。

R151--R154は、この抽象仮定を固定singlet型Bell装置のreceiver側について閉じる。R151は、setting-pre等重みseed $S_0$ と固定pairing tensor $\mathsf E$ から始め、A設定生成後に各枝を安全なpaired-Hopf盆へ送る。provenance履歴を付けても結果形成へ入力しない。seedはM48内部でも準備でき、接続周期ではR160によりM49の二粒子位置 $01,10$ から $S_0=(-1)^{X_A}$ として同じ枝を受ける。

R152は単一試行bath座標 $z$ に対して

```math
\pi_i^\delta(z)
=
\frac{
|\left(\Phi z\right)_i|^2/(z^\dagger z)
+
\delta q_i
}{
1+\delta
}
```

を定め、有限W型配置グラフの局所率

```math
k_{i\to j}^\delta(z)
=
\kappa_Xa_{ij}
\sqrt{
\frac{
\pi_j^\delta(z)
}{
\pi_i^\delta(z)
}
}
```

が詳細釣合い、一意定常分布、有限時間全変動収束を持つことを示す。これはM42/R113の場からcurrent rateを作る因果律でなく、M48に採用する局所開放粒子位置応答則である。R152はR161のBell限定形であり、R161の一様ギャップ下界とR162の有限衝突熱浴実現を利用できる。

R153はpaired-Hopf時間 $T_{\rm PH}$ と配置混合時間 $T_X$ の後、中央切断面測度が2つの理想strong matching fiberの等重み混合から、連続bath対にはpaired位相を保つprojective cost、離散配置には最適coupling不一致確率を使うfiber距離で

```math
\begin{aligned}
\varepsilon_{\rm fib}
\leq{}&
\varepsilon_{\rm seed}
+
\varepsilon_{\rm route}
+
K_{48}e^{-\gamma_{48}T_{\rm PH}}\\
&+
\frac{2\delta}{1+\delta}
+
2C_Xe^{-\lambda_X^\delta T_X}
+
\varepsilon_{\rm cut}
\end{aligned}
```

以内にあることを示す。連続状態を完全状態全変動距離で理想rayへ近づけたとは呼ばない。R154は切断後の生成子をA、Bへ因子化し、局所分析器終了後の再matching、rate切断、傾斜固定、局所記録を閉じる。結果別テンプレート交換を必要としないBell結果専用instrumentであり、Q1の一般測定後状態を解かない。

R155で使うM48完全周期の前向き誤差を

```math
\begin{aligned}
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
\leq{}&
\delta_{\rm set}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm route}
+
\varepsilon_{\rm PH}
+
L_{\rm fib}\varepsilon_{\rm fib}\\
&+
\varepsilon_{\rm an}^{A}
+
\varepsilon_{\rm an}^{B}
+
\varepsilon_{\rm X,meas}^{A}
+
\varepsilon_{\rm X,meas}^{B}\\
&+
\varepsilon_{\rm lock}^{A}
+
\varepsilon_{\rm lock}^{B}
+
\eta_W^A
+
\eta_W^B\\
&+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}^{A}
+
\varepsilon_{\rm rec}^{B}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm prod}
\end{aligned}
```

と分ける。$L_{\rm fib}<\infty$ は固定有限設定族のguard安全域上でfiber距離を結果分布の全変動距離へ移す一様Lipschitz定数である。$\varepsilon_{\rm fib}$ をR153の右辺で展開するとき、同じpaired-Hopf誤差を $\varepsilon_{\rm PH}$ と二重に加えない。各設定対の結果全変動距離が $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下なら、R150、R155により一側周辺の設定差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下、CHSH値のずれは $8\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

```math
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
<
\frac{\sqrt2-1}{4}
```

なら有限誤差下でもCHSH不等式の破れが残る。

M48の状態、誤差、資源、反証条件は次の通りである。

| 項目 | 現行の状態 |
|---|---|
| 積bath直接共分散の否定的結果 | R146、厳密 |
| paired-Hopf吸引多様体と有限時間率 | R147、採用開放方程式後に厳密 |
| 共通基準測度からのsinglet交差モーメント | R148、有限設定族で厳密、有限時間誤差付き |
| setting-pre seedの安全盆routing | R151、等重みseedと履歴不活性、有限誤差付き |
| 単一試行bath条件付き粒子位置matching | R152、R161のBell限定形。各翼の条件付き状態数はR164、採用開放rate後に厳密、R162で有限衝突近似可能 |
| 切断面の2翼強matching | R153、連続bathのprojective costと離散配置couplingによる有限時間fiber距離上界 |
| 切断後の局所分析、再matching、固定、記録 | R154、有限誤差付き |
| 切断後fresh局所作用殻の条件付き積因子化 | R166、完全共通原因に条件付けて厳密、残留結合偏差 $\varepsilon_{\rm prod}$ 付き |
| 余弦共同分布、非信号性、CHSH破れ | R149、R150の抽象結果をR153、R154で充足し、R155でM48単独周期化 |
| 弱開放帰還 | R156、fresh cell交換と次周期誤差 |
| 開放資源 | fair-seed register、bright pump、設定controller、dark sink、2翼粒子位置bath、切断器、局所分析器、記録、fresh cell流 |
| M49接続資源 | 行分解共同原因、4モードCNOT担体、同じbath・粒子位置register、setting-free恒等port、受動履歴cell |
| 未評価資源 | R164の作用容量fiberとR162をpaired-Hopf・seed routing・2翼controllerへ統合する資源、一般状態Bell receiver、総エネルギー・総エントロピー収支、無期限cell供給、設定数に対する規模依存性 |
| 反証条件 | seed bias保存、履歴不活性、詳細釣合い、混合率、2翼fiber、局所条件付き確率、有限誤差上界、帰還上界のいずれかが破れること |

切断後は局所応答を

```math
P(A,B\mid\Lambda,x,y)
=
P_A(A\mid\Lambda_A,x)
P_B(B\mid\Lambda_B,y)
```

と因子化する。一方、測定開始面の $\Lambda$ の分布は $\mu_x$ なので測定設定独立性は成立しない。Bellの定理を否定せず、前提違反の位置を設定生成後の中央準備へ置く。

R151--R156とR166は、固定singlet型、固定有限設定族、準備先行、非空間分離、プロトコル面matchingという範囲でM48単独周期を局所記録、次周期入口まで閉じる。R157--R160とR165はM49で同じsinglet交差モーメントと粒子位置枝をCNOT出力として作り、setting-free面で同じregisterをM48へ渡す。従ってM48単独周期と固定目標Q2-2全体を、ともにこの範囲で条件付き達成とする。受渡し誤差は

```math
\varepsilon_{\rm Q2-link}
=
\varepsilon_\times
+\varepsilon_X^A
+\varepsilon_X^B
+\varepsilon_{\rm carry}
```

とし、接続周期では

```math
\varepsilon_{\rm Bell}^{49\to48}
\leq
\varepsilon_{\rm Q2-link}
+
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
```

と加える。M48単独周期へは二重に加えない。M41のR107--R111、R121は置換済み模型内の結果として研究メモへ移す。R162またはR164だけでpaired-Hopf準備、seed routing、2翼controller、信号bath保持を含むBell周期全体をミクロ導出したこと、連続時間の全区間でmatching fiberを保存すること、一般状態receiver、標準的な空間分離Bell実験は主張しない。

## 8.17 M50とQ1・Q2の共通状態数・熱力学台帳

M50の共通誤差を

```math
\begin{aligned}
\varepsilon_{M50}
={}&\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sym}
+\varepsilon_{\rm ad}\\
&+\varepsilon_\delta
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
\end{aligned}
```

とする。Q1は全項を使う。Q2-1の中央4枝直接標本化は $\varepsilon_{\rm cap}$、$\varepsilon_{\rm width}$、$\varepsilon_{\rm sym}$、作用区間座標誤差、decode誤差を使い、配置混合と衝突熱浴を確率の起源にしない。Q2-2は各翼・各局所段階のM50誤差に $\varepsilon_{\rm prod}$ を加える。

作用殻明示表示

```math
P_i=\Omega_i/\sum_j\Omega_j
```

と、作用殻消去表示

```math
E_i=-\Theta\log P_i
```

は同値な2表示であり、同じ縮約分配関数で $\Omega_i e^{-\beta E_i}$ を使わない。殻自由エネルギー仕事 $W_i^{\rm sh}=\Delta F_i^{\rm sh}$ と相対有効仕事 $W_i^{\rm rel}=\Delta E_i=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ を区別する。全作用保存unitaryでは共通項が一定になり得るが、pumpとresetでは一定とは限らない。

Q2-1のM35 16対は運用上の有限Hamiltonian標本器上界であり、中央作用殻の実際の平衡自由度数ではない。Q2-2ではM49の使用済み中央殻をprovenance-onlyとし、M48の各翼へfreshな局所殻を供給する。切断後に $-\Theta\log P(a,b\mid x,y)$ を物理的な大域ポテンシャルへ戻す構成はR166に反するため、現行模型に含めない。

$J,A,J_{\rm ref}$ は作用、$\Omega$ は無次元、$\Theta,E,F,B$ はエネルギー、$\beta$ はエネルギーの逆数、殻剛性はエネルギー毎作用2乗、率は時間の逆数である。有限幅を正則化極限で一様に保つ剛性には $\Omega(\delta^{-2})$ が必要で、$\Theta(\delta^{-2})$ は代表的な選択である。Q1-1達成、Q1-2・Q1-3部分達成、Q2-1達成、Q2-2条件付き達成、Q2-3未着手の判定は変えない。
