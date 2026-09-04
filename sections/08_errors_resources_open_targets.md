@number: 8
@chapter: 本文
@title: 誤差、資源、反証条件、未完成目標
@status: M54から派生するQ1・Q2、R180 receiver、M37--M42、M50を横断比較し、R181A--R181D、有限資源、反証条件、未完成目標を整理する。

## 8.1 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168のray誤差へ同時に加える。
2. R164の有限幅・枝非対称誤差を、R170の作用殻誤差と系列固有instrument誤差へ重ねて入れる。
3. R180Aの同じblock保持偏差を $\varepsilon_{\rm split}$、$\varepsilon_{\rm latch}$、$C_\tau\varepsilon_{\rm block}$ へ重ねて入れる。
4. R180Cの積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。
6. M54の同じtransverse偏差をR181Aのray誤差、R135の初期共分散誤差、系列固有準備誤差へ重ねて入れる。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

## 8.2 M54/R181A共通開放準備の誤差と資源

M54の安全事象を $G_*$、$q_*=(R_*^2-a_*^2)/a_*^2$ とする。準備切断面の上流誤差を

```math
\varepsilon_{54}
\leq
\varepsilon_{\rm seed}
+\varepsilon_{\rm ray}
+\varepsilon_{\rm cut},
```

```math
\varepsilon_{\rm seed}=P(G_*^c),
\qquad
\varepsilon_{\rm ray}
\leq
\sqrt{q_*}e^{-\kappa\tau_{\rm prep}}
```

と分ける。$\varepsilon_{\rm seed}$ は完全結果集合の無反応質量、$\varepsilon_{\rm ray}$ は安全試行の方向誤差、$\varepsilon_{\rm cut}$ はport切断とM54から下流registerへの受渡し誤差である。M54の最小方程式は雑音零なので、有限bath雑音を仮定した誤差項をここへ暗黙に入れない。

目標ray誤差 $\epsilon_{\rm p}>0$ に対し、

```math
\tau_{\rm prep}
\geq
\frac{1}{\kappa}
\log\frac{\sqrt{q_*}}{\epsilon_{\rm p}}
```

を選べる。$a_*\downarrow0$ ではseed無反応質量を減らせる場合があるが $q_*$ が増え、準備時間、動的範囲、pump作用が増える。$\kappa\to\infty$ で時間だけを縮める場合も、sink結合強度と排熱率の資源を別に数える。

R181Aが定量化するのは縮約drift後の有限時間収束である。pump仕事、sink熱、template保持、clock切替、port履歴、有限bath交換の総収支は未導出であり、$\varepsilon_{54}$ が小さいことから熱力学的コストが小さいとは結論しない。M54のray誤差をR135で伝播した後、同じ偏差をR168または系列固有誤差へ再加算しない。

## 8.3 共通R170誤差

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

## 8.4 Q1の系列固有誤差

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

$\varepsilon_{\rm Hopf}$ はR181AのW型2モード系の有限準備、$\varepsilon_{\rm ctrl}$ は傾斜制御、$\varepsilon_{2m}$ は高モード漏れ、$\eta_W$ は左右有限コントラスト、$\varepsilon_{\rm br}$ は結果別template交換、$\varepsilon_{\rm post}$ は条件付き状態更新である。

固定有限段の逐次測定では、各段の全変動距離誤差を和で抑えられる。永久記録と使用済みcellは段数に比例して増える。作用容量、fiber、Hopf pump、controller、記録、resetを同じ有限局所Hamiltonian周期へ統合し、仕事・熱・エントロピー収支を閉じることは、M47を強める実装・熱力学的課題として残るが、Q1-2の達成条件には含めない。Q1-2の固定目標上の残件は、同じ明示的ミクロモデルで零傾斜Rabi対照と有限回反復測定を接続し、全履歴と対照を保ったZeno抑制を有限誤差で示すことである。

## 8.5 Q2-1の誤差と資源

M54ではtensor-lift、同じ永続registerのhold、clock、各gate、外部bathへの漏れ、末端ray、Born型instrumentを分ける。長さ $L$ の回路誤差は

```math
\varepsilon_{\rm circ}
\leq
\varepsilon_{\rm lift}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm clock}
+\sum_{r=1}^{L}\varepsilon_r
+\varepsilon_{\rm leak}
+\varepsilon_{\rm ray}
+\frac{\delta}{1+\delta}
+\varepsilon_{170}^{\rm end}
+f_\varnothing
```

とする。中間handoff、経路pairing、coherent decoderを独立項として加えない。$Z_S$ は同じregisterに留まり、R181Dは末端で同次元canonical SWAPと容量latchを使うためである。$f_\varnothing$ は最初の失敗段階ごとに排他的に数え、成功試行だけを再規格化しない。各gateはmode別誤差の粗い和でなく、状態bath全体のglobal phaseを除くoperator normで抑える。R181Dの未統合境界は $\varepsilon_{170}^{\rm end}$ の構成条件として残す。

## 8.6 Q2-2の誤差とBell監査

R180CはM54の実際の末端信号、R180Aのsetting-pre block receiver、R180Bのpaired-Hopf流、2つの局所R170を条件付き積因子化の下で合成する。設定対ごとの完全周期誤差を

```math
\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{54}^{\rm src}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{\rm latch}
+2\tau\\
&+
C_\tau\varepsilon_{\rm block}
+L_{\rm fib}K_{180}e^{-\gamma_{180}T_{\rm PH}}
+\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}\\
&+
\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}\\
&+
\varepsilon_{170,{\rm rest}}^{A}
+\varepsilon_{170,{\rm rest}}^{B}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}.
\end{aligned}
```

ここで $2\tau$ は一般状態の小作用blockを無反応へ送る切断質量、$C_\tau=O(\!\left(\tau^{-1/2}\right))$ は安全域の規格化感度である。$\varepsilon_{170,{\rm rest}}^{A,B}$ は、明示済みの正則化・有限混合と、別項の記録・clockを除いた局所R170残差であり、同じ段を二重に数えない。固定singletでは各枝作用が $1/2$ なので、$\tau<1/2$ ならnode項は零にする。理想singlet分布からの全変動距離が $\varepsilon_{180}^{\rm cyc}$ 以下なら、一側周辺の反対設定による差は $2\varepsilon_{180}^{\rm cyc}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{180}^{\rm cyc}$ 以下である。

```math
\varepsilon_{180}^{\rm cyc}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。

| Bell前提 | R180 receiverでの位置 |
|---|---|
| 切断後局所性 | R180Cの装置統合条件の下で完全共通原因へ条件付けて局所因子化 |
| 測定設定独立性 | A設定が中央準備へ入るため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻で決まる |
| 事後選別 | 無反応を完全結果集合へ残す |
| 非信号性 | 理想対称性で成立し、有限差を上の誤差で抑える |

従ってBellの定理を否定しない。自由設定、空間分離、一般状態receiverは達成範囲に含まない。

## 8.7 Q3のM37--M42誤差

Q3ではR135をM37担体集団の統計診断に使い、単一試行の粒子輸送はR172--R174へ分ける。完全結果分布の中心誤差を

```math
\begin{aligned}
\varepsilon_{174}(T)
\leq{}&
\varepsilon_{\rm prep}
+\varepsilon_{\rm init}
+T
\left[
|E|\sigma
+\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]\\
&+\varepsilon_{37\to42}
+\varepsilon_{\rm step}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm over}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm rec}
\end{aligned}
```

とする。M54の同じtransverse偏差を $\varepsilon_{\rm prep}$ と $\varepsilon_{37\to42}$ へ重ねず、R86の同じ包絡偏差をR135診断とM42生成子誤差へ二重加算しない。安全事象外とcell overflowは無反応として残す。

正則化誤差を小さくすると最大率は概ね $\rho^{-1/2}+\sigma/\rho$ で増え、有限衝突cell数、clock分解能、障壁精度も増える。任意の固定 $T$ と目標誤差に有限構成を選べるが、同じ固定装置でnode正則化を零にする一様資源上界はない。

R124の理想トンネル型増分を $\alpha>0$、R125の理想干渉分布距離を $\Delta>0$ とする。比較する各M42運転の誤差が $\varepsilon_{174}$ 以下なら観測差は

```math
\alpha-2\varepsilon_{174},
\qquad
\Delta-2\varepsilon_{174}
```

以上である。M54、M37、初期作用殻、M42局所辺bath、clock、終位置記録の単一Hamiltonian統合が残るため、Q3-4とQ3-5は条件付き達成である。

## 8.8 M50の資源発散

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

## 8.9 Q2の根拠モデル、共通ハードウェア努力目標、資源分類

Q2-1からQ2-4は、次の根拠モデルと根拠結果から互いに独立に判定する。独立とは他のQ2目標の達成ラベルを前提にしないという意味であり、同じ模型または部品定理を複数の目標で使うことは禁止しない。目標ごとに担体、浴、clock、準備・読出し原理が異なっても、それだけでは不達としない。

- Q2-1：M54とM50末端読出しを使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D。
- Q2-2：M54、M50、R180 receiverを使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D、R180A--R180C。
- Q2-3：M54永続状態bathの三部分系特殊化とM50末端読出しを使う。R112、R161、R162、R164、R170、R177、R181A--R181Dを根拠とする。
- Q2-4：M54を使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D、R178D、R179。

規模 $N$ ごとの一様な共通ハードウェア族へ統合することは、固定目標の達成条件ではなく実装努力目標である。将来これを主張する場合は、同じ物理port、永続状態浴、相互作用区間族、clock・制御bus、準備interface、Born型読出し・記録interfaceを共有する具体的な装置族を示す。共通の正準代数またはinstrument契約だけでは同一装置とみなさない。

受動資源と能動資源を分ける。受動的な浴自由度、正準対、coherent経路、静的結合、状態容量、受動並列度は指数的でもよい。ただし規模を報告し、一様な有限規則から生成する。次は受動資源とはみなさない。

1. 各モードを個別に初期化、設定、較正、同期、リセットする操作。
2. 指数個の係数、配線、時刻窓、結果枝を外部から指定すること。
3. 回路ごとの物理的な配線変更、全モード走査、全枝読出し。
4. 指数的に細かい精度、小さい成功率、長い準備・混合・実行時間。

Q1とQ2はM54の同じ完全状態型と外部interfaceから派生する。ただし全規模で同じ製造済みハードウェアを共有するところまでは統合していない。この未完成性は個別達成判定を変更しない。R180CはM54末端から2翼記録までのreceiver内部統合をQ2-2自身の条件とする。

## 8.10 Q2-3の3量子ビット型二段ゲート合成

3つのQ1型、すなわち2状態の論理部分系を $A,B,C$ とし、2つの2量子ビット型結合ゲートを $A$--$B$、続いて $B$--$C$ へ作用させる。ここでQ1型とは論理状態空間を指し、3台のM47装置またはQ1との共通ハードウェアを要求する語ではない。最小検査列の一つは

```math
|+\rangle_A|0\rangle_B|0\rangle_C
\longmapsto
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|111\rangle}{\sqrt2}.
```

R181Bをgate列の前に2回作用させて $a\otimes b\otimes c$ を作り、第1ゲート後も同じM54永続状態bathを保持する。枝を測定せず、共同momentから新しい入力を再準備しない。さらにAへ $T=\operatorname{diag}(1,e^{i\pi/4})$ を作用させ、2つのゲートと最初のHadamardを逆順に戻す。R177の理想coherent出力は

```math
P(000)=\cos^2\frac{\pi}{8},
\qquad
P(100)=\sin^2\frac{\pi}{8},
```

完全dephasing出力は両者が $1/2$ であり、全変動距離は $1/(2\sqrt2)$ である。coherent側と混合側の装置誤差の和がこの値未満なら正の識別余裕が残る。

R181Bは3入力の有限tensor-lift、R181Cは同じ8mode register上の2つの二次gate zoneと逆演算、R177は上の識別余裕を与える。R181Dが末端Born型instrumentへの条件付き接続を与えるため、Q2-3は条件付き達成である。残る条件は容量pointer--作用殻境界、有限fiber混合の枝対称性、SWAPから記録までの単一clock統合である。8modeが受動的に存在すること自体は失敗条件ではない。失敗条件は中間で統計量へ縮約して再準備すること、または各modeを外部から個別に初期化、較正、同期、address、読出し、resetすることである。

## 8.11 Q2-4多項式外部制御による量子出力サンプリング

Q2-4では、固定有限普遍ゲート集合から与えられる $n$ 量子ビット・深さ $d$ の回路について、全gateを終えた回路末尾から1つの出力標本を生成する。古典装置の結果空間は

```math
\{0,1\}^n\cup\{\varnothing\}
```

とし、$\varnothing$ は無反応または失敗を表す。量子回路の目標分布にも零重みの $\varnothing$ を加え、同じ完全結果空間上の全変動距離を $\epsilon$ 以下にする。成功試行だけを再規格化しない。

次を個別に $\operatorname{poly}(n,d,1/\epsilon)$ で抑える。

1. 回路記述、コンパイル時間、外部プログラム、外部指定係数の個数とbit記述長。
2. 外部制御channel数、ゲート命令数、制御列長、addressするport数。
3. 準備、初期化、実行、混合、測定、記録、必要な場合のリセットを含む総時間。
4. 外部制御のエネルギー、作用、結合強度、周波数、動的範囲。
5. 制御、初期化、時刻、読出しの精度と、それを指定するbit数。
6. 外部から個別にaddress、設定、較正、回収するcell、履歴、記録、仕事、排熱portの個数。受動bank内部のcell総数と総熱はここへ含めない。
7. 無反応・失敗確率と期待試行回数。

一方、signal、anti-register、work、history、cold、spentを含む指数的な受動自由度と受動状態容量を許す。装置体積、総bath容量、総熱は指数的でもよい。これは通常の意味の効率的古典simulationを主張する基準ではない。

M54は $L=2^n$ 個のsignal modeを使うが、R181Cにより固定有限局所gateをspectator sectorへ同じ係数でbroadcastし、作用素norm誤差をsector数の和ではなく最大値で抑える。R181Dは各bitでraw容量 $J_{u,b}$ とregularized容量 $A_{u,b}^\delta$ を分け、R164/R170でselectorを形成してから可逆filterを開く。確率 $\tau$ 未満の枝とguardを $\varnothing$ に残すため、切断誤差は $2n(\tau+\gamma)$ 以下であり、事後選別を使わない。

選択成分はR181Aのradial-only portで標準作用へ戻す。未知の条件付き確率を読み出すsqueezeではなく、$\tau$ の下限から固定repump時間を選ぶ。深さ $n$ の完全結果誤差は入力誤差、$n\delta/(1+\delta)$、$2n(\tau+\gamma)$、各node実装誤差の和で抑える。R178DはHamiltonian workだけの逆掃除と、結果・開放散逸履歴をspent側へ残す境界を与える。

R179は同一静的couplerと受動clockによるpartial SWAPを反復し、active残差を幾何的にaggregate cold floorまで縮める。root source、R162 collision cell、selector、filter workをbankから供給し、使用済み状態をspentへ送る。旧fair-bit、dyadic threshold、aperture tapeは現行因果鎖に使わない。

以上は各構成部品と合成誤差・資源の定理を与える。ただし、静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合する物理境界が残る。この条件の下でQ2-4を条件付き達成とする。

## 8.12 反証条件

現行主張は次の検査に失敗した場合に縮小または撤回する。

| 対象 | 反証条件 |
|---|---|
| M54/R181A | 実変数driftと複素式が一致しない、安全seed上のray距離が指数上界を破る、無反応質量を落とさずM50分布へ接続できない |
| M47/R143 | Hopf方向が有限時間で準備できない、R170特殊化後もBorn型枝と局所記録が一致しない、結果別状態更新が失敗する |
| M54/R181B--R177 | tensor-liftの正規化または正準性が破れる、集団momentから再準備する、同じregisterを保持できない、参照系相関または逆演算fringeが壊れる、各modeの個別外部制御が必要、R181Dの完全結果誤差境界を満たさない |
| M54/R180A--R180C | 実際の末端信号でなく集団momentを再注入する、block作用と枝重みが一致しない、paired-Hopf流が選択templateへ吸引しない、R180Cの単一装置境界を満たさない、切断後因子化が破れる、局所R170応答が反対翼設定を参照する、無反応込みでCHSH誤差上界を満たさない |
| M54/R181A--R181D・R178D・R179 | sectorごとの誤差を指数個加算する、selector lock前にfilterを開く、projector filterが正準でない、希少枝を事後除外する、状態依存除算または確率依存squeezeを使う、使用済みcellを履歴なしにblankへ戻す、または単一の一様装置族へ統合できない |
| M37/R86・R135 | 有限時間包絡上界または第2モーメント持上げ上界を超える |
| M42/R172--R174 | 局所master方程式がM37辺流を再現しない、正則化全変動上界を破る、有限衝突近似が安全領域で収束しない、終時刻に同じ粒子を記録できない |
| R168 | 可変作用集団でray平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| R170 | 混合上界、局所記録の排他性、履歴単射性、正の処理時間のいずれかを満たさない |
| Q2共通ハードウェア努力目標 | 同一装置を主張しながら目標ごとに担体、浴、準備・読出し原理を交換する、または装置族を一様な有限規則で生成できない |
| Q2-3二段ゲート合成 | 第1ゲート後の単一試行状態を破壊せず第2区間へ渡せない、中間共同モーメントから再準備する、GHZ--$T$--逆演算の $1/(2\sqrt2)$ 余裕が全装置誤差を上回らない |
| Q2-4 | 受動モードごとの設定・較正・読出し、指数長の係数表、回路別配線、指数時間または指数精度が必要になる。総bath容量と総熱が指数的であることだけでは反証にならない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 8.13 固定目標の残件と実装強化課題

固定目標上の未完成事項は次である。

1. Q1-2について、同じ零傾斜Rabi対照と反復R143/R170測定を接続し、全履歴、tilt対照、有限誤差、資源を含む正のZeno抑制余裕を示す。
2. Q3-2について、閉路巻数、homotopy不変性、節を介した位相すべり、R86細分化安定性、非整数seamのエネルギー発散を統合する。
3. Q2-1について、R181Dの容量pointer--作用殻境界、有限fiber混合、固定、記録を単一clock scheduleで閉じる。
4. Q2-3について、同じR181D末端条件を8mode特殊化で閉じ、R177の識別余裕より小さい全装置誤差を選ぶ。
5. Q2-4について、M54の静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、各局所誤差の独立な物理上界を与える。

次は固定目標の達成判定と分けて管理する実装・熱力学的強化課題である。

1. M54のpump、transverse sink、template、clockを有限bath、仕事源、排熱先へ持ち上げ、雑音と準備誤差と総収支を同じ模型で閉じる。
2. R170の作用容量結合、作用殻fiber内平衡化、信号保持、衝突bath、枝固定、記録をQ1・Q2の1つの有限局所Hamiltonianへ統合する。
3. M47のM54準備から結果別状態更新、永久記録、resetまでの周期総収支を閉じる。
4. R180CのM54末端SWAP、setting-pre block latch、paired-Hopf pump・sink、中央切断、2翼局所R170、controller、fresh cell流を同じ具体装置とclockへ統合する。
5. Q3でM54切断面、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録までを同じ有限局所装置へ統合する。
6. 連続空間、多粒子を扱う。
7. Q2共通ハードウェア努力目標として、同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceをQ2-1からQ2-4で共有する一様な装置族を得る。

Q1-1、Q3-1、Q3-3は個別機能として達成、Q1-2は部分達成、Q2-1、Q2-2、Q2-3、Q2-4、Q3-4、Q3-5は条件付き達成、Q3-2は未達である。Q2-1とQ2-3の条件はR181Dの末端物理接続、Q2-2の条件はR180Cのreceiver内部単一装置統合、Q2-4の条件はM54部品の一様装置統合へ集約される。Q2共通ハードウェア族は判定外の努力目標として未完成であり、その成否を個別判定へ遡及させない。
