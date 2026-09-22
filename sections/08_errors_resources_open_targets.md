@number: 8
@chapter: 本文
@title: 誤差、資源、反証条件、未完成目標
@status: Q1/Q2のM65/R181D系と、Q3のM37/R86--M64/R203A--R203D--R161--R185階層を横断して誤差・資源・反証条件を整理する。M65ではfinite-time selector、record、endpoint、Q2-4資源を、M64ではprocess reduction、Newton residual、finite-graph readoutを責務別に管理する。


## 8.1 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168の状態方向誤差へ同時に加える。
2. M65主線で、M65内部に含めたfinite-time relaxation、hub無反応、endpoint comparator、record誤差を系列固有測定機構誤差へ重ねて入れる。退役した旧測定経路の偏差を現行台帳へ重ねて入れない。
3. R180Aの同じブロック保持偏差を $\varepsilon_{\rm split}$、$\varepsilon_{\rm latch}$、$C_\tau\varepsilon_{\rm block}$ へ重ねて入れる。
4. R180Cの積因子化誤差を各翼の局所M65誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。
6. 同じ準備済み入力偏差を $\varepsilon_{\rm in}$、R135の初期共分散誤差、系列固有の入力誤差へ重ねて入れる。
7. M64ではinitial preparation、current dictionary、mean-flow tracking、density interpolation、process reductionを導出箇所ごとに一度だけ数える。$\delta$ をcurrent-dictionary誤差とR185 regularizationへ二重に加算せず、process-law errorとNewton force residualを単純加算しない。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

### 共通ミクロ実装原則

本章の資源監査では、有限性を能動部分系、浴、拡大全系に分ける。有限閉鎖Hamiltonian実装は固定目標ではなく、有限な能動自由度と明示的なHamiltonian無限浴からなるミクロ模型を標準候補とする。開放方程式はHamiltonian無限浴からの縮約として得ても、基本的なミクロ方程式として直接定めてもよく、有限浴への持上げは有限性自体に物理的意味がある場合を除き強化課題とする。したがって、未使用素子列、有限再帰、有限総浴容量の評価は、中心結論に必要な場合だけ本体誤差へ入れる。

## 8.2 準備済み入力境界とR192の誤差・資源

Q1とQ3の状態方向、Q2-1--Q2-3の固定入力は、第2.4節の準備済み古典入力境界から受け取る。入力状態と目標状態の差は一つの $\varepsilon_{\rm in}$ として最初の下流誤差へ一度だけ加え、同じ偏差をR135、R168、系列固有誤差へ重複計上しない。一般の指定状態方向を共通seedから生成する旧R181Aの時間、ポンプ、排熱を現行固定目標の資源には数えない。具体的な入力準備装置を追加する場合、その費用は境界の上流実装として別途報告する。

R192は一般深さQ2-4だけで、R181Dが選別した非終端安全結果の絶対作用を次段binary selectorの感度下限へ戻す。理想流は

```math
\dot Z
=g_R(S_*-Z^\dagger Z)Z
```

で、状態方向を厳密に保存する。安全下限 $S_0\geq S_{\min}>0$ に対し、相対作用誤差を $\eta_R$ 以下にする固定接続時間は

```math
T_{192}
\geq
\frac{1}{2g_RS_*}
\log\!\left[
\frac{S_*/S_{\min}-1}{\eta_R}
\right].
```

R181Dのbinary selector contractから $S_{\min}/S_*=\operatorname{poly}^{-1}(n,1/\epsilon)$ を選び、$g_RS_*$ も逆多項式以上に保てば、各非終端段と全 $n-1$ 段のR192時間は多項式である。接続時間はこの事前下限から固定し、未知の条件付き確率や現在の振幅を読み取って適応変更しない。

有限実装の作用回復誤差を $\varepsilon_{192,k}$ とする場合、Q2-4では $\sum_{k=1}^{n-1}\varepsilon_{192,k}$ を一度だけ数える。R192は既存の横方向偏差を訂正しないので、静的結合誤差、位相雑音、全自由度への加法雑音はR186で監査する。$S_0=0$ または安全下限未満の希少結果をR192後に成功結果へ戻してはならない。

## 8.4 Q1の系列固有誤差

### M65とR189A--R189CのQ1誤差・資源

Q1 W2主線ではR189Aの保持済み二作用をM65へ直接入力する。R189Aで既に計上した作用比誤差をM65内部へ重複加算せず、走行中測定では

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+
\varepsilon_{65}^{\rm mid}
+
\varepsilon_{\rm lat}
```

とする。$\varepsilon_{65}^{\rm mid}$ はR204Dのcomplete-result誤差であり、finite-time relaxation、hub無反応、endpoint comparator、recordを内部で一度だけ数える。

R189A decisionに使った保持対は次回captureへ未処理のまま再接続しない。固定有限深さでは未使用保持対との正準SWAP、反復装置では使用済み保持対をR179へ流して未使用保持対を供給する。この未使用保持対/reset時間と有限SWAP誤差は次回captureの入力誤差へ一度だけ含める。

R143のM65主線では結果分布誤差と測定後状態誤差を分ける。

```math
\varepsilon_{143}^{\rm dist}
\leq
\varepsilon_{\rm in}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{65}
+\varepsilon_{\rm node}^{\rm dist}.
```

安全結果の測定後状態は

```math
\varepsilon_{143}^{\rm state}
\leq
\frac{2\eta_F}
{\sqrt{\tau_{\rm state}^{65}}-\eta_F}
```

で別に評価する。R144の固定 $N$ 段逐次測定では

```math
D_{\rm TV}(p_N^{\rm obs},p_N^{\rm id})
\leq
\sum_{j=1}^{N}\varepsilon_{{\rm inst},j}
+
\sum_{j=1}^{N-1}\delta_{{\rm state},j}
```

とする。固定有限列ではM65 pointer、record、選別機構用作業領域をR179の開放リセットで再使用し、結果相関履歴を流出浴へ流す。

R189CのQ1-2達成証人では中間R189Aで保持した2作用をM65へ直接入力し、中間R192を使わない。固定 $N=2$ の正の履歴重みには $p_*=0.10$ の安全下限を取れるため、M65 decision時間を有限に固定した後に $\Omega_\kappa\to0$ として時間ずれを小さくできる。空操作対照では同じM65 decisionとrecordを走らせ、R181D routerだけを開かない。旧作用殻型実現の偏差は現行M65主線へ重複加算しない。

### 8.4.1 R187のM37--W2 信号系誤差と資源

R187を使うQ1制御では、信号系側の誤差を

```math
\varepsilon_{187}
\leq
d_0
+
C_U\sqrt{r_\kappa}
+
\left(1+\varepsilon_{\rm stat}(\eta)\right)^{m_U}-1
+
\varepsilon_{\rm sw}
+
\varepsilon_{\rm cal}
```

と分ける。ここで $r_\kappa=J_\kappa/G_\kappa$、$d_0$ は準備済み入力境界または固定正準接続端からM37最低2正常モードへの投入誤差、$C_U\sqrt{r_\kappa}$ は傾斜時のスペクトル混成・モード群切替・結合後の生成子補正、$\varepsilon_{\rm stat}$ は局所包絡と較正済み厳密正常モードの時間一様差、$\varepsilon_{\rm sw}$ は滑らかなランプ近似、$\varepsilon_{\rm cal}$ は傾斜値と保持角の較正誤差である。

```math
\varepsilon_{\rm stat}(\eta)
=
\frac{2\delta_{\rm loc}(\eta)}
{1-\delta_{\rm loc}(\eta)},
\qquad
\delta_{\rm loc}(\eta)
=
(1-\eta)^{-1/4}-1.
```

各静的区間では厳密M37正常モード生成子 $f_{\omega_0}(h)$ と有効W型生成子が固有ベクトルを共有するため、実保持時間を厳密低2分裂で較正する。従って長いRabi時間へR86の $T\|h\|^2/\omega_0$ 型Duhamel上界をそのまま掛けず、信号系誤差は固定有限ゲート列の $\varepsilon_{\rm stat}$ で監査する。同じ偏差を $\varepsilon_{\rm ctrl}$、$\varepsilon_{2m}$、R135トレース誤差へ重複加算しない。

弱link $\kappa\downarrow0$ では

```math
J_\kappa=O(\kappa),
\qquad
G_\kappa\to g_*>0,
\qquad
T_U
=
O\!\left(
\frac{\mathcal J_0}{J_\kappa}
\right).
```

従って任意精度構成は有限だが、総時間は発散し得る。代表傾斜は $|F_\kappa|=O(\sqrt{J_\kappa G_\kappa})$、滑らかな化の一例では $\tau_{\rm sw}=O(r_\kappa^{1/4})$ の短いランプを使う。必要信号系周波数、弱結合設定精度、分裂・保持時間の相対較正精度、切替時刻分解能を別々に報告する。R187はQ1の信号系段階実装結果であり、Q2-4の多項式外部制御条件を満たすという主張には使わない。

R187のW2への正準接続端は全モード直交変換の先頭2正準対を使い、高モードを捨てない。具体的な準備済み入力装置の資源は境界の上流へ分離し、M65読出し、R181D router、R143局所記録の物理資源はQ1測定部分系として別に数える。

## 8.5 Q2-1の誤差と資源

M54ではテンソル積状態の生成、同じ永続記憶部の保持、時計自由度、各ゲート、外部浴への漏れ、末端状態方向、各末端2結果nodeを分ける。深さ $m=2$ のQ2-1末端読出しを含む長さ $L$ の回路誤差は

```math
\varepsilon_{\rm circ}
\leq
\varepsilon_{\rm lift}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm clock}
+\sum_{r=1}^{L}\varepsilon_r
+\varepsilon_{\rm leak}
+\varepsilon_{\rm ray}
+\sum_{k=1}^{m}\bar\varepsilon_k.
```

$\bar\varepsilon_k$ には第 $k$ nodeの射影作用保持、M65、R181D router、転送誤差を各1回だけ含める。固定深さQ2-1ではR192を必須にせず、退役した旧作用殻型測定経路の正則化・混合・固定誤差をM65主線へ加えない。無反応は完全結果集合に残し、成功試行だけを再規格化しない。

各ゲートはモード別誤差の粗い和でなく、状態浴全体の大域位相を除く作用素ノルムで抑える。実際の1試行末端信号をM65へ渡し、有限record/latch後にR181Dで結果成分を受け渡す物理interfaceは既存結果で閉じるため、Q2-1は達成である。$\varepsilon_{\rm clock}$ は有限操作列の切替・時刻割当誤差であり、自律的な物理clockや試行間resetを同じ装置へ統合したことを意味しない。それらの全周期統合はM0へ分離する。

## 8.6 Q2-2の誤差とBell監査

現行Q2-2はA端M65、projector router、B端M65の深さ2逐次instrumentである。完全結果誤差を

```math
\varepsilon_{180}
\leq
\varepsilon_A^{\rm pre}
+\varepsilon_{65}^{A}
+\varepsilon_{\rm route}
+\varepsilon_B^{\rm basis}
+\varepsilon_{65}^{B}
+\varepsilon_{\rm rec}
```

とする。M65内部のfinite-time relaxation、hub無反応、endpoint comparator、recordは各 $\varepsilon_{65}^{A,B}$ に1回だけ含める。旧R180Bの方向吸引誤差、中央結果複製誤差、切断後A側再読出し誤差は現行台帳から除く。

理想一重項共同分布との全変動距離が $\varepsilon_{180}$ 以下なら、各周辺事象の確率差は $\varepsilon_{180}$ 以下、各二値相関の差は $2\varepsilon_{180}$ 以下、CHSH値の差は $8\varepsilon_{180}$ 以下である。A結果成分をB端へ物理的に渡すため、Bell局所factorizationまたは空間分離を誤差ゼロ極限の主張へ追加しない。

## 8.7 Q3のM64--R161--R185誤差

Q3の現行particle/Nelson物理層はM64/R203A--R203Dである。continuous profileでは、initial preparation、regularized current dictionary、finite-time mean-flow tracking、density interpolationを経てcanonical overdamped tracerをideal regularized diffusionへ接続する。

initial preparationは

```math
\varepsilon_{\rm prep}
=
\frac12
C_{\rm init}
e^{-\lambda_{\rm prep}T_{\rm prep}}
+
\varepsilon_{\rho,0}
```

で管理する。current dictionaryとfinite-time flow trackingは

```math
\varepsilon_{\rm track}
=
\varepsilon_A
+
\tau_UM_q,
```

```math
\varepsilon_U
=
\varepsilon_{\rm track}
+
C_{\rm int}a^2
\|\partial_x^2v_\delta\|_\infty.
```

canonical overdamped M64からideal regularized diffusionへのdrift errorは

```math
\varepsilon_{\rm drift}^{64}
=
\varepsilon_U
+
\nu\varepsilon_{\rho,1},
```

有限時間process reductionは

```math
\varepsilon_{\rm red}^{64}(T)
=
e^{L_bT}\varepsilon_{\rm prep}^{W_1}
+
\frac{e^{L_bT}-1}{L_b}
\varepsilon_{\rm drift}^{64}
```

で評価する。$L_b=0$ の場合は第2項を $T\varepsilon_{\rm drift}^{64}$ と読む。

R203Dの1次元canonical R161 chainはR185と同じ $(\pi^\delta,j^\delta,t^\delta)$ を用いる。従ってeffective processの時間対称Newton残差は

```math
\varepsilon_{\rm Newt}^{185}
=
m\|R_\delta\|_\infty
+
mC_{185,a}a^2
```

であり、$\varepsilon_{\rm red}^{64}$ と単純加算しない。前者はprocess-law metric、後者は力の残差であり、次元と責務が異なる。

finite-graph profileではinitial preparation、generator実装、終位置recordを

```math
\varepsilon_{64,G}(T)
=
\varepsilon_{\rm prep,G}
+
T\varepsilon_{\rm gen,G}
+
\varepsilon_{\rm rec}
```

として一度ずつ数える。固定背景 $q_i$ に対するregularizationでは、R124の反対側増分、R182の半周期増分、R125の2経路分布距離がそれぞれ

```math
\frac{\alpha}{1+\delta},
\qquad
\frac{2B_c}{1+\delta},
\qquad
\frac{1}{2(1+\delta)}
```

の正の余裕を持つ。従って十分条件は

```math
2\varepsilon_{64,G}
<
\frac{\alpha}{1+\delta}
```

for Q3-4A、

```math
\varepsilon_{64,G}
<
\frac{B_c}{1+\delta}
```

for Q3-4B、

```math
\varepsilon_{64,G}
<
\frac{1}{4(1+\delta)}
```

for Q3-5である。R182のideal一周期回帰はregularization後も厳密に保たれ、観測分布の一周期回帰誤差は $2\varepsilon_{64,G}$ 以下である。

$\delta$ はR203Aの辞書誤差へ再加算せず、R185 regularizationとfinite-graph位置分布に一度だけ数える。M60/M61に固有だったDuffing shell、core mixing、ballistic lead、moving reflector、periodic homogenization、Eyring--Kramers、single-Hamiltonian liftの誤差は現行M64台帳へ移さない。finite-bandwidth/Hamiltonian lift、underdamped small-mass極、実M64 tracer自身の高階加速度安定性はstrengtheningへ分離する。

## 8.8 現行regularizationの資源境界

現行Q3で $\delta>0$ を使う目的は、M64/R203A--R203DとR161/R185のdensity・rateを節点近傍でも有限に保つことである。$\delta\downarrow0$ ではregularized densityの下限が小さくなり、drift・rate感度や必要な分解能が悪化し得るため、固定性能の同じ装置で極限を一様に取れるとは主張しない。

このregularizationはM64のphase-volume reservoir、continuous tracer、finite-graph generator、R185残差の誤差台帳で一度だけ数える。退役した旧作用殻測定経路の殻剛性、混合時間、作用開口frequencyは現行Q1/Q2/Q3の資源台帳へ移さない。

## 8.9 Q2の根拠モデル、共通ハードウェア努力目標、ブラックボックス資源分類## 8.9 Q2の根拠モデル、共通ハードウェア努力目標、ブラックボックス資源分類

Q2-1からQ2-4は、次の根拠モデルと根拠結果から互いに独立に判定する。独立とは他のQ2目標の達成ラベルを前提にしないという意味であり、同じ模型または部品定理を複数の目標で使うことは禁止しない。目標ごとに信号系、浴、時計自由度、準備・読出し原理が異なっても、それだけでは不達としない。ここで「根拠結果」は `PROJECT_STATUS.md` の固定目標表と同じく、達成判定で直接参照する結果だけを列挙し、個々の結果が内部で用いる推移的依存は重複列挙しない。

- Q2-1：M54静的状態構成を使う。根拠結果はR112、R181B、R181C、R181D、M65/R204D--R204E。
- Q2-2：M54静的状態構成と2端M65経路を使う。根拠結果はR112、R180C、R181D、M65/R204D--R204E。
- Q2-3：M54三部分系静的状態構成を使う。根拠結果はR112、R177、R181B、R181C、R181D、M65/R204D--R204E。
- Q2-4：M54一般静的状態構成を使う。根拠結果はR112、R179、R181C、R181D、R186、M65/R204F、R192。一般 $n$ の初期入力にはR181Bを反復しない。

規模 $N$ ごとの一様な共通ハードウェア族へ統合することは、固定目標の達成条件ではなく実装努力目標である。将来これを主張する場合は、同じ物理接続端、永続状態浴、相互作用区間族、時計自由度・制御バス、準備接続部、Born型読出し・記録接続部を共有する具体的な装置族を示す。共通の正準代数または測定機構契約だけでは同一装置とみなさない。

Q2-4ではブラックボックスとしての運用上の資源と報告対象の内部資源を分ける。外部から装置を利用するためのプログラム、制御、時間、精度、試行回数は前者として多項式上界を要求する。受動的な浴自由度、正準対、コヒーレント経路、静的結合、状態容量、受動並列度、装置体積、総浴容量、総熱は後者として規模を報告し、一様な有限規則から生成する限り指数的でもよい。ただし内部資源が外部接続部へ露出した次の操作は報告対象の内部資源には残さない。

1. 各モードを個別に初期化、設定、較正、同期、リセットする操作。
2. 指数個の係数、配線、時刻窓、結果成分を外部から指定すること。
3. 回路ごとの物理的な配線変更、全モード走査、全結果成分読出し。
4. 指数的に細かい精度、小さい成功率、長い準備・混合・実行時間。

この資源規約は内部コストを無視するためではなく、比較対象をブラックボックスとしての運用上の複雑度へ固定するためのものである。内部モード数、静的結合器数、装置体積、総浴容量、総熱は別の報告対象の内部資源として保持する。量子計算機と同等の総物理資源効率は主張しない一方、内部の指数構造がモード別較正、指数精度、指数時間、指数試行回数として外部へ露出する場合はQ2-4の失敗とする。

R186はこの露出のうち製造誤差とノイズの境界を定量化する。疎な局所製造誤差、独立位相ノイズ、射影結果の固定機構係数誤差は指数モード数をそのまま粗く加算せず評価できる。一方、空モードを含む全自由度に加わる加法ノイズが有限の下限を持つ場合は、現行M54直接振幅記憶部で横方向作用注入が指数的に増え得る。この障害を開放リセットだけで解消したとは扱わない。

信号作用 $S$ を指数的に増やせば、R186の加法ノイズ不等式だけから指数精度は直ちには従わない。この場合は、その大きな作用が外部制御のエネルギー・作用、準備、動的範囲、時刻精度、読出し分解能、期待試行回数へ指数コストとして露出しないことを同じ資源台帳で示す必要がある。従ってR186は、指数モード数を一律に失敗条件とするのでも、指数信号作用を無償の回避策として認めるのでもなく、内部の指数構造が外部運用資源へ露出する経路を分けて検査する。

Q1とQ2はM54の同じ完全状態型と外部接続部から派生する。ただし全規模で同じ製造済みハードウェアを共有するところまでは統合していない。この未完成性は個別達成判定を変更しない。R180CはM54末端から2翼記録までの受信機構内部統合をQ2-2自身の条件とする。

## 8.10 Q2-3の3量子ビット型二段ゲート合成

3つのQ1型、すなわち2状態の論理部分系を $A,B,C$ とし、2つの2量子ビット型結合ゲートを $A$--$B$、続いて $B$--$C$ へ作用させる。ここでQ1型とは論理状態空間を指し、3台のQ1 W型2モード手順装置またはQ1との共通ハードウェアを要求する語ではない。最小検査列の一つは

```math
|+\rangle_A|0\rangle_B|0\rangle_C
\longmapsto
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|111\rangle}{\sqrt2}.
```

R181Bをゲート列の前に2回作用させて $a\otimes b\otimes c$ を作り、第1ゲート後も同じM54永続状態浴を保持する。結果成分を測定せず、共同モーメントから新しい入力を再準備しない。さらにAへ $T=\operatorname{diag}(1,e^{i\pi/4})$ を作用させ、2つのゲートと最初のHadamardを逆順に戻す。R177の理想コヒーレント出力は

```math
P(000)=\cos^2\frac{\pi}{8},
\qquad
P(100)=\sin^2\frac{\pi}{8},
```

完全位相緩和出力は両者が $1/2$ であり、全変動距離は $1/(2\sqrt2)$ である。コヒーレント側と混合側の装置誤差の和がこの値未満なら正の識別余裕が残る。

R181Bは3入力の有限テンソル積状態の生成、R181Cは同じ8モード記憶部上の2つの二次ゲート領域と逆演算、R177は上の識別余裕を与える。第1ゲート後も同じ単一試行状態を保持して第2ゲートへ渡し、M65とR181Dが末端2結果読出しと結果成分受渡しを与えるため、固定3入力のQ2-3は達成である。8モードが受動的に存在すること自体は失敗条件ではない。失敗条件は中間で統計量へ縮約して再準備すること、または固定3入力の一試行に必要な各モードを外部から個別に初期化、較正、同期、個別指定することである。一般サイズの資源効率はQ2-4へ、物理clock・永久record・reset・renewalの全周期統合はM0へ分離する。

## 8.11 Q2-4多項式外部制御による量子出力サンプリング

Q2-4ではM54の $L=2^n$ 受動信号モードを使い、R179後の定数次元供給源から $0^n$ 根モードを作り、R181Cが局所ゲートを一括作用させる。各出力ビットでは射影作用をbinary selectorへ渡して結果を形成し、R181Dが非規格化射影成分を次段へ渡す。非終端の安全結果だけに事前固定時間のR192を作用させ、次段selectorの絶対作用下限を回復する。fixed-goal実装ではselectorにM65を使う。最終ビット後に別の作用感度を持つ読出しが無ければ終端R192は置かない。

R178Dの有限閉鎖リセット境界と旧R179の有限低温／使用済み貯蔵部は必須因果鎖から外す。結果相関情報や散逸履歴は流出浴へ流し、能動作業領域と指針変数だけをR179の開放リセットで再使用する。

外部プログラム、制御経路、準備・実行・リセット時間、結合強度・帯域幅・精度、外部から個別指定する浴接続端数を $\operatorname{poly}(n,d,1/\epsilon)$ に抑える。受動信号モード、浴自由度、装置体積、総浴容量、総熱は報告対象の内部資源とし、それだけでは失敗としない。浴がモード別初期化・較正、回路出力確率、振幅表、指数長係数表を外部入力として要求する場合は失敗である。R186の全自由度に加わる加法ノイズ障害も維持する。

Q2-4は条件付き達成を維持する。残る条件は、静的部分系配線、射影容量保持機構、M65 open selector、R181D制御付き選別機構、R192方向不変作用安定化、開放リセット/供給接続部を一つの一様装置族へ接続し、R186の許容ノイズ条件を満たすことである。

## 8.12 反証条件

現行主張は次の検査に失敗した場合に縮小または撤回する。

| 対象 | 反証条件 |
|---|---|
| M54/R192 | 状態方向が変化する、ロジスティック作用解または固定時間上界が破れる、安全作用下限未満の希少結果を成功へ救済する、未知の条件付き確率を読んで接続時間を変える、または横方向加法偏差を除去したと扱う |
| Q1 W型2モード手順/R143/R181D | 準備済み入力誤差を一度だけ数えられない、R140/R187の信号・分析器誤差、M65の完全結果誤差、またはR181Dの階数1射影選別・測定後状態受渡しが各境界を満たさない。第3.9節のW型空間profileコントラストはsignal診断であり、この主線の反証条件へ混ぜない |
| M54/R181B--R177 | テンソル積状態の生成の正規化または正準性が破れる、集団モーメントから再準備する、同じ記憶部を保持できない、参照系相関または逆演算干渉縞が壊れる、各モードの個別外部制御が必要、R181Dの完全結果誤差境界を満たさない |
| M54/R180A--R180C | 実際の末端信号でなく集団モーメントを再注入する、A端M65の結果とrouterが一致しない、B端へ非規格化結果成分を同じ試行のまま渡せない、B端読出しがA/B以外の設定を参照する、一試行内の有限順序付き操作窓と安全集合を構成できない、無反応込みでCHSH誤差上界を満たさない、または現行逐次構成で成立・不成立となるBell前提を因果構造と確率因子化に対応させて監査できない |
| M54/M65・R181C・R181D・R179・R186・R192 | M65結果固定前にrouterを開く、希少結果を事後除外する、R192で安全下限未満を救済する、状態依存除算を使う、開放浴へ回路出力確率やモード別係数を外部注入する、一様装置族へ統合できない、またはR186の加法ノイズ障害を回避できず指数精度を要求する |
| M37/R86・R135 | 有限時間包絡上界または第2モーメント持上げ上界を超える |
| R182 | W型固定低位スペクトル・密度・節が格子収束しない、Rayleigh十分条件から障壁下二重項が得られない、関数計算の共有固有空間または分裂相対上界を破る、中央障壁込み半周期鏡映・一周期回帰が成立しない |
| R161 path law | 固定有限時間で $M_T=\sup_{t\leq T}\max_i\sum_{j\ne i}k^+_{i\to j}(t)<\infty$ を満たさず、finite-state canonical Markov経路法則の非爆発性を保証できない |
| M64/R203A--R203D | signal density/current dictionaryが閉じない、phase-volume partitionまたはinitial preparationが成立しない、$U$ のfinite-time trackingを制御できない、canonical overdamped tracerをideal regularized diffusionへ有限時間で縮約できない、finite-graph ratesの非負性・current matching・初期準備が破れる、またはR161/R185・R124/R182/R125への誤差受渡しが閉じない |
| R161/R162 ideal reference | R161率の非負性またはmaster equation整合が破れる、あるいはR162 ideal open-jump生成子がR161率と一致しない |
| Q3-2 | 時間対称Newton則を縮約前に仮定する、M64からideal regularized process/R161へ有限時間で接続できない、同じ前向き経路法則からBayes後退率を構成できない、またはR185の $C_{185,a}a^2+O(\delta)$ 評価を破る |
| Q3-3C | W型低位スペクトルの格子・領域収束を示せない、または同じ固有基底で環境との弱結合を縮約した有限時間純位相緩和と対角占有率保存を閉じられない |
| Q3-4B | 2モード作用比を空間領域占有率へ同一視する、外部駆動・傾斜切替・障壁低下を使う、最低二重項の障壁値未満条件、第3状態との間隔、半周期移送、一周期回帰、M64位置読出しのいずれかを欠く |
| Q3-6 | 単価性または整数巻数を外部条件として置く、非整数モノドロミーを丸めて除く、節を介した位相すりと細分化安定性を同じ構成で扱えない |
| R168 | 可変作用集団で状態方向平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| Q2共通ハードウェア努力目標 | 同一装置を主張しながら目標ごとに信号系、浴、準備・読出し原理を交換する、または装置族を一様な有限規則で生成できない |
| Q2-3二段ゲート合成 | 第1ゲート後の単一試行状態を破壊せず第2区間へ渡せない、中間共同モーメントから再準備する、GHZ--$T$--逆演算の $1/(2\sqrt2)$ 余裕が全装置誤差を上回らない |
| Q2-4 | 受動モードごとの設定・較正・読出し、指数長の係数表、回路別配線、指数時間または指数精度が必要になる。総浴容量と総熱が指数的であることだけでは反証にならない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 8.13 固定目標の残件と実装強化課題

固定目標上の未完成事項は、Q3-6の位相量子化とQ2-4の一様装置族・資源条件である。Q2-4では静的部分系配線、M65 selector、R181D router、R192方向不変作用安定化、R179開放リセット/供給接続部を1つの一様装置族へ接続し、R186のノイズ条件と多項式外部運用資源を満たす必要がある。Q2-1/Q2-3は固定深さの一試行interface、Q2-2はA端結果成分をB端へ渡す非空間分離逐次interface、Q3-4A/Q3-4B/Q3-5はM64 finite-graph tracerの一試行位置読出しまでを既存結果で閉じている。これらの準備から永久記録、reset、物理clock、次試行renewalまでの全周期統合はM0へ分離する。

固定目標に付随する標準強化目標の定義、適用範囲、現在地は `ENHANCEMENT_TARGETS.md` を正本とする。全固定目標に具体的古典ミクロ模型A1と直接数値再現A2、Q1/Q2に具体回路B1、実験可能領域B2、回路直接数値再現B3を置く。Q2-2にはさらに、非空間分離の現行証人から物理的2端化、測定窓内因果隔離、隔離下のBell前提監査へ進むQ2-2-Sを置く。これらの強化状態は固定目標の達成状態と独立であり、導入時点では全て未監査とする。

A1ではHamiltonian無限浴だけでなく、規約と共分散を明示して直接定めたLangevin型SDEその他の開放ミクロ方程式を認め、理想白色雑音を許す。A2ではA1で定めたミクロODE/SDEそのものを直接計算する。理想白色雑音を使うQ1/Q2模型を回路へ移す場合、B2/B3では有限帯域雑音源と時間尺度分離を明示する。

従来からのQ1/Q2完全周期収支、R180Cを含むQ1/Q2の永久記録・reset・物理clock・次試行renewal統合、M64 common process--時計--終位置記録--reset--renewalの単一反復周期統合、連続空間一様極限、多粒子拡張、全周期の有限閉鎖Hamiltonian化は、M0、A/B/Sを横断する上位または系列固有の実装強化課題として保持する。R162を特定Hamiltonian浴から再導出することはM64主線の要件ではない。旧R162有限衝突経路、旧R188、旧R179部分SWAP貯蔵部、旧R178D有限閉鎖リセット境界は撤回せず、有限閉鎖実装を調べる強化結果として論文外メモへ保存する。

Q1-1、Q1-2、Q2-1、Q2-2、Q2-3、Q3-1、Q3-2、Q3-3A、Q3-3B、Q3-3C、Q3-4A、Q3-4B、Q3-5は達成、Q2-4は条件付き達成、Q3-6は未達である。

## 8.14 M37からQ1制御へ進む強化課題

新しい主線はM37、W型低2モード、Q1制御の順とする。固定目標の定義やQ2依存関係は変更しない。静的R86と射影内R140の既存達成に加え、第6.17節の区間合成と第3.5.1節の残差を同じ時間窓で閉じる必要がある。

| 誤差・資源 | 数える対象 |
|---|---|
| 包絡誤差 | 全定傾斜区間と有限切替。再準備で区間誤差を消さない |
| 低モード状態誤差 | 漏れ振幅と低モード内位相補正。漏れ確率の二乗評価と区別 |
| 制御誤差 | 合成角、時刻、切替幅、作用の変動、準備誤差 |
| 入力一様性 | 相対位相と初期共通位相を含む実線形写像のノルム |
| 資源 | 全Rabi時間、信号系周波数、間隔、結合強度、制御帯域、外部仕事 |

B.5の漏れ確率を全変動距離へ直接加える旧評価は採用しない。R143の誤差和では、実際の全状態または分布比較を満たす $\varepsilon_{2m}$ を使う。理想2準位信号系のQ1-1達成と、全W型・M37実装の任意精度強化は分ける。全W型測定の誤差予算もこの追加条件に依存する。

優先順は、物理係数の対応、静的Rabi、有限傾斜列、準備・読出し境界、共同信号系への接続、同一装置の統合である。ゲート列からの有効伝播は補助実装として研究メモで管理し、Q3全過程の独立導出とは呼ばない。

## M65 canonical open selector の誤差・資源台帳

M65の正本はR204Aの3状態open generatorである。通常経路では、安全運用域で $a_\Sigma\geq a_{\min}>0$ として

```math
\varepsilon_{65}^{\rm int}
\leq
\varepsilon_A
+
e^{-\Lambda T}
+
\frac{\Lambda}{\Lambda+\kappa a_{\min}}
+
T\varepsilon_{\rm rate}
+
\varepsilon_{\rm rec}.
```

canonical open lawそのものでは $\varepsilon_{\rm rate}=0$ とする。具体的chamber、有限帯域bath、Brownian liftを選んだ場合だけ実装generator誤差を追加する。

endpointは固定係数の線形比較器で判定でき、

```math
\varepsilon_{65}^{\rm edge}
\leq
\tau_{\rm cut}
+
\varepsilon_A
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm rec}.
```

従って

```math
\varepsilon_{65}
=
\max
\{
\varepsilon_{65}^{\rm int},
\varepsilon_{65}^{\rm edge}
\}.
```

二結果node数 $m$ について、

```math
T_{\rm node}
\geq
\frac1\Lambda
\log\frac{Cm}{\epsilon}
```

とし、

```math
\frac{\Lambda}{\kappa a_{\min}}
=
O\left(\frac{\epsilon}{m}\right)
```

および各局所誤差を $O(\epsilon/m)$ に配分すれば、$\Lambda^{-1},\kappa^{-1},a_{\min}^{-1},m$ が多項式範囲にある限り、

```math
T_{\rm read,total}
=
O\left(
\frac{m}{\Lambda}
\log\frac{m}{\epsilon}
\right)
```

は多項式である。小Born重み自体はM65のrelaxation rate $\Lambda$ を縮めない。

R204Bのphase-volume chamberとR204CのHamiltonian--Brownian liftを採用する場合、そのbath、overdamped、tube、lumping、calibration誤差はその実装だけの強化台帳へ加える。退役R191のmacrospin誤差を現行M65試行へ加算しない。

M65の正本化はR186の指数個signal modeへの加法noise/precision障害を解決しない。Q1/Q2 fixed-goal witnessにはM65を採用する。
