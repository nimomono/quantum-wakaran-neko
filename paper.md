# 概要


本論文は、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、結合ゲート、空間伝播、Bell型統計を構成できる範囲を調べる。有限閉鎖Hamiltonianモデルと開放古典モデルを区別し、採用方程式後の厳密結果と、その方程式自体のミクロ導出を分ける。

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

M54をQ1・Q2の共通親模型族とする。完全状態は有限実正準register、source/template port、anti/work、raw・regularized容量、selector、collision cell、cold/spent bank、記録、clockを含む。R181Aは物理template準備、R181Bは固定入力tensor-lift、R181Cは永続register gate、R181DはR170駆動projector-treeを与える。複素信号は実担体の派生表示、rayと分布は解析上の統計量である。

準備後の各試行の有限正準信号 $v$ を共通instrument仕様M50へ渡し、R164の作用殻状態数から排他的枝重み $\pi_i^\delta(v)$ を得る。R161/R162で粒子位置を有限時間再平衡化し、R170で枝を固定して局所記録する。二乗形の状態依存性はM54の第2モーメントに現れ、排他的結果はM50/R170が作る。R112は有限正準制御、安全比較、SWAP、記録、逆計算を担うが、独立のBorn型枝生成には使わない。

Q1はM47のW型最低2モードと信号bathを使う。M54/R181AのW型2モード特殊化が入力rayを準備する。共通R135がBloch球型統計状態空間、R140が任意の $SU(2)$ 操作、Rabi型占有振動、傾斜保持を与える。R143は共通R170へW型分析器、有限コントラスト、結果別テンプレート交換を加えた特殊化である。可逆操作は達成し、Born分布、同軸反復分布、異軸逐次分布も有限誤差で導出している。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。完全周期と周期総収支は固定目標ではなく、実装・熱力学的強化課題として残す。

Q2-1はM54の受動的な4mode信号、anti-register、work、clock履歴を同じ永続状態bathへ保持する。R181Bは一般積入力の可逆tensor-lift、R181Cは同一register上のCNOT、局所操作、逆演算、参照系安定な有限誤差合成、R181Dは末端Born型instrument接続を与える。R181Dの容量pointer--作用殻境界、有限fiber混合、記録までの一体化を条件としてQ2-1は条件付き達成である。Q2-2は独立の目標として、M54の実際の1試行末端信号をR180Aのsetting-pre block receiverへ渡し、R180Bのpaired-Hopf流で2翼templateへ有限時間整列させる。R180Cは、切断後の2つの局所R170、条件付き積因子化、Born共同分布、非信号性、CHSH不等式の破れ、Bell前提監査、fresh-cell帰還を、単一装置統合を条件としてまとめる。固定singlet、固定有限設定族、準備先行、非空間分離、採用開放法則の範囲でQ2-2は条件付き達成である。

Q2-3はR181Bをgate列の前に2回適用して8mode信号を作り、R181CのA--B、B--C二次生成子を同じ状態bathへ順に作用させる。R177はGHZ--$T$--逆演算のcoherent分布と完全dephasing分布が全変動距離 $1/(2\sqrt2)$ で分かれることを示す。R181Dと同じ末端一体化条件の下で条件付き達成である。

Q2-4はM54の一般 $n$ 特殊化である。R181Cは局所gateのsector一括作用、R181DはR170駆動の逐次projector-treeを与える。各nodeはraw容量、正則化作用殻、selector lock、可逆filter、radial-only repumpを使い、無反応を完全結果へ残す。R178Dはhistory掃除の限界、R179はblank bank、collision cell、spent bankの一様供給を与える。指数的な受動信号・work・history・cold・spent容量と総熱を許し、外部program、制御channel、精度、反復回数、総時間だけを多項式に抑える現行規則の下で、Q2-4を条件付き達成とする。

Q3はM54で初期rank-one集団を準備し得る契約を上流に置き、M37の局所振動子網からR86の有限時間Schrödinger型担体を導く。その上に1個の局在粒子位置、局所辺bath、clock、履歴を持つM42を置く。R172はM37有効辺流に沿う位置分布の等変性、R173は節一様正則化と有限衝突Hamiltonian近似、R174はM54準備から終位置記録までの誤差受渡しを与える。初期位置は準備済み信号から一度だけ作り、終時刻に別の位置を再標本化しない。Q3-1と井戸型・調和型のQ3-3A・Q3-3Bは達成、有限障壁Q3-4AとQ3-5は単一装置統合を条件に達成、W型のQ3-3C・Q3-4Bは部分達成である。Nelson流の作用変分または時間対称Newton則を導くQ3-2と、位相量子化のQ3-6は未達であり、互いに独立に判定する。

Q1とQ2は同じM54模型族から派生するが、全規模で同一の製造済みハードウェアまたは同一パラメータを使うところまでは主張しない。各固定目標は明記した根拠結果から独立に判定する。R180Cのreceiver内部統合、Q2共通ハードウェア族、Q1--Q3を1つの周期へ統合するM0はいずれも未完成である。

# 第I部　問題設定と共通言語

# 問題設定、現行模型、達成範囲

> **位置づけ：** M54をQ1・Q2の共通親模型族とし、R181A--R181Dから各系列を派生させる現行因果鎖、Q3への準備port受渡し、未統合境界を示す。


## 研究上の問い

本論文の目的は、古典的な粒子、振動子、熱浴、制御器、記録器から、量子力学に特徴的な構造をどこまで明示的に再現できるかを調べることである。量子力学は結果の比較基準に使うが、古典モデルの運動方程式や初期確率へ答えを直接入力しない。

有限次元Schrödinger方程式を実正準方程式へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、測定後状態、記録、resetは得られない。本稿は次を別々に要求する。

1. 実担体と開放portから階数1の試行集団統計を有限時間で準備する。
2. 可逆な信号操作を古典正準流として実装する。
3. 各試行の信号作用から排他的枝または初期粒子位置の状態数を作る。
4. Q1・Q2では粒子位置を枝分布へ再平衡化し、Q3では同じ局在粒子をM37担体に沿って輸送する。
5. 無反応を含む完全結果集合を局所記録する。
6. 系列固有の状態更新、ゲート、Bell監査、空間現象を共通読出しへ接続する。

### 力学の導出と装置の運転順序

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

| 関係 | 進む順序 | 未導出の接続 |
|---|---|---|
| 担体の物理的導出 | M37、R86、W型低2モード、R140 | 全制御時間の包絡・状態誤差と資源 |
| 1試行の運転 | 初期実座標の準備、制御、作用殻選択、記録 | 準備・測定境界の同一装置化 |
| 複合系への拡張 | Q1入力、共同担体、結合操作、読出し | W型入力の抽出・転送の物理実装 |

M54による初期実座標の準備は、M37の運動法則をQ1から導くことではない。力学命題は指定された初期実座標を条件として始め、準備の構成は別に接続する。Q3全体の達成をQ1導出の前提にはしない。

## 現行因果鎖

状態準備とBorn型読出しは

```math
\Gamma_0
\xrightarrow{\mathrm{M54/R181A}}
C_Z\simeq cc^\dagger,
\qquad
Z(\omega)
\xrightarrow{\mathrm{M50/R164}}
\pi_i^\delta(v)
\xrightarrow{\mathrm{R161/R162}}
X=i
\xrightarrow{\mathrm{R170}}
D_i
```

の順に分ける。これはM54の $n=1$ または深さ1 nodeである。一般のQ2ではR181Bで固定入力をliftし、R181Cで同じregisterを操作し、R181Dで上のM50/R170 nodeをprojector-treeとして反復する。R112は有限基底制御、時計、比較、SWAP、記録、逆計算の共通定理である。

Q3だけは下流を

```math
\Gamma_0
\xrightarrow{\mathrm{M54/R181A}}
Z_{t_0}(\omega)
\xrightarrow{\mathrm{R164\ once}}
X_{t_0}
\xrightarrow{\mathrm{M37+M42/R172--R174}}
X_T
\xrightarrow{\mathrm{R112\ record}}
D_{X_T}
```

とする。終時刻に別のM50位置を作らない。

各試行の実体は実正準担体、粒子位置、bath、template、clock、記録・履歴である。M54の複素register $Z$ は実正準担体の派生表示、$c,C_Z$ は解析上の試行集団統計である。M50/R170は同じ試行の物理信号から排他的結果を作る。これらを同一視しない。

| 系列 | 信号準備と操作 | 単一試行の下流入力 | 系列固有の下流結果 |
|---|---|---|---|
| Q1 | M54/R181A、M47、R135、R140、R143--R144 | 単一試行のW型信号bath座標 | R181Dの深さ1とR143のW型状態更新 |
| Q2-1 | M54、R112、R181B--R181D | 1試行内の永続4mode信号とanti/work | 可逆tensor-lift、CNOT、逆演算、条件付き末端instrument |
| Q2-2 | M54、R180A--R180C | M54の1試行末端信号と切断後の各翼の局所信号 | setting-pre block抽出、paired-Hopf、2つのR170の条件付き局所合成、Bell監査、帰還 |
| Q2-3 | M54、R181B--R181D、R177 | 3部分系の永続8mode信号とanti/work | A--B、B--C、GHZ--$T$--逆演算、条件付き末端instrument |
| Q2-4 | M54、R112、R161、R162、R164、R170、R181A--R181D、R178D、R179 | $L=2^n$ の受動直接モード、逐次2枝filter、collision bank | 一般回路列と完全結果空間上の逐次出力。指数的な受動bankと総熱を許す |
| Q3 | M54/R181A、M37、R86、R135 | 準備終了面のM37標本と初期M42位置 | R172--R174の局在粒子輸送、R123--R125への接続 |

集団の第2モーメント、交差モーメント、共同頻度を単一試行controllerへ書き戻さない。Q1・Q2は各試行の有限信号だけをM50へ渡す。Q3は各試行のM37実振動子、M42現在位置、局所bath cellだけを進める。

## 現行模型

| 模型 | 役割 | 状態 |
|---|---|---|
| M0 | Q1--Q3を同一ハードウェアと反復周期へ統合する目標 | 未完成 |
| M54 | 一様有限正準register・作用殻receiver模型族 | Q1・Q2の共通親模型。R181A--R181Dが準備、lift、gate、projector-treeを与える。Q3は準備portだけを使用 |
| M37 | 局所振動子網からの空間包絡 | 現行基礎Hamiltonian模型 |
| M42 | M37担体上の局在1粒子トークン輸送 | 現行Q3粒子模型 |
| M47 | W型2モード信号bath・粒子位置の測定protocol | 現行Q1複合protocol |
| M50 | 有限信号作用、作用殻状態数、粒子位置再平衡化、R170 | Q1・Q2の共通instrument仕様。Q3では初期M42位置の1回選択だけに使用 |

置換済み模型と独立研究線は本文の模型地図へ並べない。最小索引は `notes/superseded_result_index.md`、詳細は各研究メモとGit履歴に置く。

## 達成判定

「達成」は、固定した範囲で基準を厳密に満たすか、任意の $\epsilon>0$ に対して誤差を $\epsilon$ 未満にする有限構成を選べることを指す。形式極限、構成のない収束仮定、無反応試行の事後除外は含めない。

| 目標 | 現在地 | 根拠モデル | 根拠結果 | 主な残件 |
|---|---|---|---|---|
| Q1-1 | 達成 | M47 | R135、R140 | なし |
| Q1-2 | 部分達成 | M47、M50、M54 | R140、R143--R144、R161、R162、R164、R168、R170、R181A、R181D | Born分布、同軸反復分布、異軸逐次分布は導出済み。零傾斜Rabi対照、反復測定、全履歴、tilt対照、有限誤差を含むZeno抑制余裕が残る |
| Q2-1 | 条件付き達成 | M54、M50末端読出し | R112、R161、R162、R164、R170、R181A--R181D | 容量pointerから作用殻、混合、固定、記録までの末端一体化 |
| Q2-2 | 条件付き達成 | M54＋setting-pre paired-Hopf receiver、M50局所instrument | R112、R161、R162、R164、R170、R181A--R181D、R180A--R180C | R180Cの単一装置統合、自由設定、空間分離、一般状態の完全装置化 |
| Q2-3 | 条件付き達成 | M54永続状態bathの三部分系特殊化、M50末端読出し | R112、R161、R162、R164、R170、R177、R181A--R181D | Q2-1と同じ末端一体化条件。一般サイズの資源効率はQ2-4に残る |
| Q2-4 | 条件付き達成 | M54 | R112、R161、R162、R164、R170、R181A--R181D、R178D、R179 | 静的sector配線、R170 collision、controlled filter、radial repump、cold/spent開放境界を一つの一様装置族へ統合する。受動bank容量と総熱は指数的でもよい |
| Q3-1 | 達成 | M37 | R86 | 一般複素hoppingと時間依存一様極限は範囲外 |
| Q3-2 | 未達 | 完結モデルなし | なし | 古典ミクロモデルの縮約からNelson流の作用変分または時間対称Newton則を導く |
| Q3-3A | 達成 | M37、R123有限環境 | R86、R123（井戸型） | なし |
| Q3-3B | 達成 | M37、R123有限環境 | R86、R123（調和型） | なし |
| Q3-3C | 部分達成 | M37、M47のW型2モード担体 | R86、R140 | 低位スペクトルの収束と有限環境純位相緩和 |
| Q3-4A | 条件付き達成 | M54、M37、M42、M50 | R86、R124、R181A、R172--R174 | M54準備、M37担体、初期作用殻、M42輸送、記録までの単一装置統合 |
| Q3-4B | 部分達成 | M37、M47のW型2モード担体 | R86、R140 | 全空間占有率、M42位置読出し、半周期移送と一周期回帰の誤差接続 |
| Q3-5 | 条件付き達成 | M54、M37、M42、M50 | R86、R125、R181A、R172--R174 | 同上。幾何学的2開口と連続スクリーンは未構成 |
| Q3-6 | 未達 | 完結モデルなし | なし | 節、巻数、位相すべり、細分化安定性、非整数モノドロミー排除の統合 |

固定目標の文言と達成判定の詳細は `PROJECT_STATUS.md` を正本とする。Q1-2はBorn分布、同軸反復分布、異軸逐次分布を導出済みとし、Zeno部分が未達であるため部分達成とする。Q2-1からQ2-4は、明記した根拠モデルと根拠結果から互いに独立に判定する。これは他のQ2目標の達成ラベルを前提にしないという意味であり、同じ模型または部品定理を複数の根拠行へ載せることは禁止しない。共通ハードウェア族への統合は固定目標とは別の実装努力目標である。Q2-3は3量子ビット型二段ゲート合成、Q2-4は指数的な受動自由度を許す多項式外部制御サンプリングである。置換または削除した旧固定目標は退役索引に保存する。

## 根拠モデルの独立性と模型間受渡し

Q2固定目標は、Q2-1のM54と末端M50、Q2-2のM54/R180 receiverと2翼M50、Q2-3のM54三部分系特殊化と末端M50、Q2-4のM54をそれぞれの根拠として独立に判定する。Q2-1とQ2-2がM54を共有しても、一方の達成状態から他方を推論しない。規模ごとの一様な共通ハードウェア族へ統合することは、別の実装努力目標である。Q3-3A--Q3-3CとQ3-4A--Q3-4Bも接尾辞ごとに独立に判定し、系列名Q3-3、Q3-4へ独立した達成状態を置かない。

M54は同じ試行の $Z_S$、anti-register、work/historyをそのまま次のgate窓へ保持し、共同momentへの置換、fresh bathへの再準備を許さない。内部の有限modeは受動bath自由度であり、個別の外部初期化、較正、同期、address、読出し、resetを要求しない。Q2-3の完全な合成契約は付録Jを正本とする。Q2-2では実際の2入力末端信号をholdしてR180へ渡し、A設定による直交block分解後も同じ試行の選択blockをreceiver sourceとして使う。

## 非主張

本論文は次を主張しない。

1. Q1、Q2、Q3が同一の達成済み物理装置であること。
2. M54の採用driftを有限bath、仕事源、排熱先から導出済みであること。
3. R164の枝状態数だけで作用殻準備と熱化をミクロ導出したこと。
4. R170の全構成部品を1つの具体的有限局所Hamiltonianへ統合済みであること。
5. 長期頻度または有限熱化から独立同分布型有限標本揺らぎが従うこと。
6. R180 receiverが標準的な空間分離・自由設定Bell実験を再現すること。
7. Q3の有限グラフトークンから連続空間の連続粒子軌道が一様に得られること。
8. Q2の一様な共通ハードウェア努力目標、R181Dの末端一体化、M54の全構成部品を単一の一様装置族へ統合済みであること。
9. 指数的な受動自由度を許すことが、指数時間、指数個の個別制御、指数的に細かい精度を許すこと。
10. 連続空間、多粒子、一般有限POVMの一様構成。

## 論文の読み方

第2章はM54の完全状態型とR181A--R181D、第3章はM54の $n=1$ W型Q1特殊化、第4章は $n=2,3$ のQ2特殊化、第5章はM54駆動R180 Bell receiver、第6章と第7章はM37--M42によるQ3を扱う。第8章は誤差、資源、反証条件をまとめ、第9章で結論を述べる。

付録AはR112、BはQ1 instrument、CはR181B/R181Cの有限次元特殊化、DはR180A/C、E--GはQ3、HはR181AのW型特殊化、IはR180B、JはQ2二段合成、K--LはR161/R162/R164/R170、MはR181A、NはM37--M42、Oは一様register代数、PはR181D projector-tree、QはR179のbank供給を扱う。

導出主線を追う場合は、第6.2〜6.7節の実運動と静的縮約、第3.3〜3.5節のW型縮約、第3.5.1節の受渡し系を先に読む。その後に共通測定、第4章の共同担体、第7章の粒子位置現象へ進む。章番号と固定目標の段階番号は論理的な依存順を意味しない。

# 有限モード担体と共通正準モジュール

> **位置づけ：** M54をQ1・Q2の共通親模型族として定義し、R181A--R181Dを準備、tensor-lift、永続gate、projector-tree読出しの正本として置く。Q3はM54の準備portだけを上流契約として使う。


## M54を親模型族とする範囲

M54は、有限個の実正準対から得る複素registerを、準備port、可逆gate、作用殻receiver、記録まで運ぶ模型族である。規模 $n$ の完全状態を

```math
\Gamma_{54}^{(n)}
=
(Z,S_{\rm port},G,W,J,A^\delta,X,C,
B_{\rm cold},B_{\rm spent},D,\tau)
```

と書く。$Z\in\mathbb C^{2^n}$ は物理的な実正準対の派生表示、$S_{\rm port}$ は有限次元source/template port、$G,W$ はanti-registerと可逆work、$J=(J_0,J_1)$ はraw作用容量、$A^\delta$ は作用殻容量、$X$ はselector、$C$ は有限衝突cellとその履歴、$B_{\rm cold},B_{\rm spent}$ は未使用・使用済みbank、$D$ は外部記録、$\tau$ は自律clockである。Q1では $n=1$、Q2-1・Q2-2では $n=2$、Q2-3では $n=3$、Q2-4では一般の $n$ を使う。

外部interfaceは、sourceまたは物理templateのload、固定有限gate名と対象bit、読出しbit、誤差予算、試行回数、clock開始だけに限る。振幅表、確率表、mode別較正値、試行中の状態依存制御を外部から与えない。lift、unitary gate、SWAP、latch、filter、記録は有限正準写像として扱う。template整列とradial repumpは採用開放方程式、R161/R162は有効率と有限衝突近似、R170を使う作用殻選択は条件付き構成、cold/spent供給は弱開放境界である。

```math
S_{\rm port}
\xrightarrow{\mathrm{R181A/R181B}}
Z
\xrightarrow{\mathrm{R181C}}
Z_{\rm out}
\xrightarrow{\mathrm{R181D}}
(D,B_{\rm spent}).
```

R181Aは物理templateに沿うray準備、R181Bは固定2・3入力の可逆tensor-lift、R181Cは同じregister上の局所gate列、R181DはR170で駆動する逐次projector-tree Born instrumentを与える。Q1とQ2はこの同じ状態型とport規約の特殊化であり、旧来の別模型を並置しない。ただし、全 $n$ を同じ製造済み装置で覆うことや、Q1とQ2の全パラメータを同一にすることは主張しない。Q1--Q3の単一反復装置M0は、M54より強い未完成の統合目標である。

| 系列 | M54の特殊化 | 準備 | 操作 | 排他的出力 |
|---|---|---|---|---|
| Q1 | $n=1$、W型2モード | R181A | R140 | R181Dの深さ1とR143 |
| Q2-1 | $n=2$ | R181B | R181C | R181Dの深さ2 |
| Q2-2 | $n=2$、固定singlet source | R181B/R181C | R180 setting-pre block | R181Dの局所nodeとR180C |
| Q2-3 | $n=3$ | R181Bを2回 | R181CとR177 | R181Dの深さ3 |
| Q2-4 | 一般 $n$、root input | R181Aのradial portとR179 | R181C | R181Dの深さ $n$ |
| Q3 | 有限空間セル | R181Aだけを上流契約として使用 | M37--M42 | 初期R164選択後は同じ粒子を記録 |

M54の $Z$ は各試行の物理的実状態から得る。解析上の $c$、$C_Z$、Born分布をcontrollerへ書き戻さない。Q3ではM54準備後の信号にR164を一度だけ適用してM42の初期位置を作り、終時刻に別の位置を再標本化しない。共通モデル族への整理は固定目標の文言や達成ラベルを変更しない。

M54は現行Q1・Q2の共通構成であるが、その全部品がM37から導出されたとはしない。M37主線はまずQ1の制御運動の物理的起源を強化する。W型入力の追加接続をR181B〜R181DやQ2各目標の必須前提へ加えず、M50/R170の入力仕様も変更しない。

## 有限正準信号の辺代数

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

<!-- theorem-start:theorem -->
**定理（R112：有限正準信号の制御・比較・記録回路）**

有限正準信号の可逆有効力学は、有限配置グラフ上の頂点作用項と差モード辺生成子の有限プログラムとして表せる。連結グラフでは隣接2モード交換と局所位相から $U(L)$ の任意の有限unitaryを有限積として合成できる。さらに、固定有限個の信号register、時計、比較対象、安全領域、記録枝、テンプレートについて、次を有限個の正準対と滑らかな有限時計窓で実装できる。

1. 指定した有限unitary列の自律化と有限制御誤差評価。
2. 互いに素な安全領域の滑らかな比較と、境界失敗を含む正式な無反応結果。
3. 空registerと使用済みregisterを区別した正準SWAPおよび結果別テンプレート交換。
4. 各枝だけに支持を持つ局所記録と、外部履歴を残した内部作業registerの逆計算。

全入力、時計、使用済みcell、無反応、外部記録を含む拡大写像は1対1に保てる。Q1、Q2、Q3の違いは、頂点集合、信号の物理的由来、係数、時計窓、排他的出力の実装にある。本定理だけから枝確率、Born型状態数、粒子位置分布、無期限resetは従わない。
<!-- theorem-end:theorem -->

## R112の役割境界

R112が現行主線へ供給するのは次の部品である。

1. 局所位相回転と隣接 $QQ+PP$ 交換による有限ユニタリ回路。
2. 時計窓の自律化と有限誤差制御。
3. 外部から与えた制御値に対する滑らかな比較器と正式な無反応領域。
4. 正準SWAP、局所記録、テンプレート交換、内部逆計算。

作用区間と一様選択器角から長期Born型頻度を得る旧経路は現行定理に使わない。R112は作用殻fiber内の平衡化も、結果列の独立同分布性も証明しない。旧正準標本器の確率生成経路は `notes/superseded_m35_born_sampler.md` に整理し、非確率的な制御・比較・記録内容はR112へ吸収する。

固定benchmarkのprogram順序を外部scheduleで作ることは許す。このscheduleは入力条件の提示であり、同じ試行のBorn型出力を生成する機構ではない。

## M54物理template-port準備

各試行の物理状態として $m$ 個の実正準対 $(Q,P)\in\mathbb R^{2m}$ を置き、その派生座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とする。$z$ は実担体の表示であって追加の実体ではない。目標templateも実装置の正準対 $(Q^w,P^w)$ で保持し、そこから得る非零派生座標 $w$ を直接couplerへ入れる。規格化方向 $c=w/\|w\|$ と射影 $\Pi_c=cc^\dagger$ は解析記号に限り、controllerが状態依存除算を行って作る物理registerではない。

Hermitian生成子 $G(t)$ とそのunitary $U(t)$ に対し $w(t)=U(t)w(0)$ とする。目標作用 $J_*>0$ を固定し、M54の雑音零の採用開放方程式を

```math
\dot z
=
-\frac{i}{\mathcal J_0}G(t)z
+\lambda_{\rm prep}(t)
\left[
g(J_*-z^\dagger z)z
-\kappa\{(w^\dagger w)z-w(w^\dagger z)\}
\right]
```

と定める。$g,\kappa>0$、$\lambda_{\rm prep}\geq0$ である。第1項は実正準Hamiltonian伝播、動径項はpumpと飽和、中括弧は非規格化templateだけで書いたtransverse sink、$\lambda_{\rm prep}$ は物理clockが開閉するportである。$\kappa=0$ はR181Dが使うradial-only repump portである。最小M54は決定論的であり、Langevin雑音を含まない。

準備有効時間を

```math
\tau(t)=\int_{t_0}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とする。相互作用表示で $\widetilde z=ac+p$、$c^\dagger p=0$ と分解すると

```math
\frac{da}{d\tau}=g(J_*-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(J_*-\|\widetilde z\|^2)-\kappa\|w\|^2\right]p,
```

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\|w\|^2\tau}
```

となる。初期seed測度 $\mu_0$ は目標階数1分布そのものとせず、固定 $a_*,R_*>0$ に対する安全事象

```math
G_*
=
\{|c^\dagger\widetilde z_0|\geq a_*\}
\cap
\{\|\widetilde z_0\|\leq R_*\}
```

を定める。$G_*^c$ はseed失敗として完全結果集合の無反応へ残す。目標依存の準備測度は、同じseed測度を上のdriftで押し出した $(\Phi_c^t)_\#\mu_0$ であり、階数1統計を初期測度へ直接置いたものではない。

<!-- theorem-start:theorem -->
**定理（R181A：物理template-port共通ray準備）**

$G_*$ 上で $q_*=(R_*^2-a_*^2)/a_*^2$ とする。M54の採用開放方程式では、各安全試行のray距離は

```math
D_{\rm pure}
\left(
\frac{zz^\dagger}{z^\dagger z},
\Pi_c(t)
\right)
\leq
\sqrt{q_*}e^{-\kappa\|w\|^2\tau(t)}.
```

安全試行の作用重み付き規格化第2モーメントを

```math
C_{Z,G_*}(t)
=
\frac{\mathbb E[\mathbf1_{G_*}Z_tZ_t^\dagger]}
{\mathbb E[\mathbf1_{G_*}Z_t^\dagger Z_t]}
```

とすれば

```math
D_{\rm tr}
\left(C_{Z,G_*}(t),\Pi_c(t)\right)
\leq
\sqrt{q_*}e^{-\kappa\|w\|^2\tau(t)}.
```

また、$a_0\neq0$ の各試行は $\tau\to\infty$ で作用 $J_*$ の位相円へ収束し、動径誤差を含む収束率は有界seed集合上で $\min\{2gJ_*,\kappa\|w\|^2\}$ により抑えられる。有限時刻 $t_{\rm cut}$ で $\lambda_{\rm prep}=0$ とした後は、各試行の実正準状態が $i\mathcal J_0\dot z=Gz$ に従い、R135の第2モーメント輸送が成り立つ。$G_*^c$ の確率は無反応質量として保持し、成功試行だけを結果分布として再規格化しない。物理couplerは $w$ だけを読み、$w/\|w\|$ を生成しない。
<!-- theorem-end:theorem -->

証明、複素式と等価な実変数方程式、pump・sink・template・clockの因果台帳は付録Mに置く。R181Aは採用開放方程式後の厳密結果である。pumpとsinkの環境自由度、仕事、熱、エントロピー生成を有限閉鎖系から導いた結果ではない。

## 有限信号集団の第2モーメント輸送

有限試行空間上の非零複素信号 $Z\in\mathbb C^m$ と、有限で正の集団作用

```math
S_Z=\mathbb E[Z^\dagger Z]
```

を考える。非中心化された規格化第2モーメントを

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{S_Z}
```

と定める。これは通常の中心化共分散ではなく、$\mathbb E[Z]=0$ の場合にだけ中心化した量と比例して一致する。

<!-- theorem-start:theorem -->
**定理（R135：有限信号集団の規格化第2モーメント輸送）**

各試行の信号が同じ有限次元unitary $U(t)$ により $Z(t)=U(t)Z(0)$ と発展するなら、

```math
C_Z(t)=U(t)C_Z(0)U(t)^\dagger
```

であり、trace、正値性、rankは保存される。$i\mathcal J_0\dot U=G(t)U$ なら

```math
i\mathcal J_0\dot C_Z=[G(t),C_Z]
```

である。

さらに、同じ初期標本から作る理想信号 $\widetilde Z_t=U(t)\widetilde Z_0$ に対し

```math
\|Z_t-\widetilde Z_t\|
\leq
\varepsilon(T)\|\widetilde Z_0\|
```

が全試行、$0\leq t\leq T$ で一様に成り立つとする。$\widetilde S_0=\mathbb E\|\widetilde Z_0\|^2$、$S_t=\mathbb E\|Z_t\|^2$、

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置けば、

```math
D_{\rm tr}
\left(
C_Z(t),
U(t)C_Z(0)U(t)^\dagger
\right)
\leq
\min
\left\{
1,
2\varepsilon(T)\sqrt{\kappa_T}
+\varepsilon(T)^2\kappa_T
\right\}.
```
<!-- theorem-end:theorem -->

階数1なら $C_Z=cc^\dagger$、$c^\dagger c=1$ と書け、非負量

```math
\mathbb E\|(I-cc^\dagger)Z\|^2
```

が零になるため、$Z=\alpha c$ がほとんど確実に成り立つ。$m=2$ では

```math
C_Z
=
\frac12
\left(I_2+\boldsymbol r\cdot\boldsymbol\sigma\right)
```

と書け、階数1条件は $|\boldsymbol r|=1$ と同値である。従ってBloch球はR135の2次元系であり、独立の結果を必要としない。正確輸送、有限時間誤差、階数1支持、2次元幾何を同じ第2モーメントの定理として使い、同じ上流偏差を複数の誤差項へ加算しない。証明は付録Fに置く。

## 一般ray平均からM50枝統計への受渡し

安全事象 $G$ 上の有限信号 $Z$ に対し、失敗質量を捨てない安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

とする。等長埋込み $\Psi$ と $M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ を固定する。

<!-- theorem-start:theorem -->
**定理（R168：一般ray平均からM50枝統計への受渡し）**

各安全試行にM50を適用し、安全事象外を無反応へ送ると、完全結果分布は

```math
P(i)
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
\qquad
P(\varnothing)=P(G^c)
```

である。さらに次が成り立つ。

1. $C_Z=cc^\dagger$ かつ $G$ 上で信号が非零なら、R135の支持節により $R_Z^G=P(G)cc^\dagger$ である。
2. $Z^\dagger Z=s_*>0$ がほとんど確実で $P(G)=1$ なら、$R_Z^G=C_Z$ である。
3. 一般の可変作用集団では $R_Z^G$ が読出し対象であり、$C_Z$ への置換には動径補正が必要である。
4. 安全な近似rayが目標rayから純粋状態距離 $s$ 以内なら、対応する枝分布の全変動距離は $s/(1+\delta)$ 以下である。

成功試行だけで再規格化しない。
<!-- theorem-end:theorem -->

$P(G)=1$、$\overline S=\mathbb E[Z^\dagger Z]$ の場合、動径補正は

```math
D_{\rm tr}(R_Z^G,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{Z^\dagger Z}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}(Z^\dagger Z)}}{\overline S}
```

で抑えられる。R168はM37を前提とせず、Q1・Q2が単一試行信号をM50へ渡すとき、およびQ3が初期M42位置または固定時刻代替診断へ信号を渡すときの共通統計写像である。証明と可変作用反例は付録Fに置く。

## M50の作用容量と枝状態数

非零有限信号 $v\in\mathbb C^m$、等長埋込み $\Psi:\mathbb C^m\to\mathbb C^L$、排他的枝 $i\in\mathcal I$ を考える。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定し、

```math
J_i(v)=\mathcal J_0|(\Psi v)_i|^2,
\qquad
A_i^\delta(v)=J_i(v)+\delta q_iJ_{\rm sig}(v)
```

と置く。各枝に2つの非負作用を持つ排他的作用殻を置く。

<!-- theorem-start:theorem -->
**定理（R164：有限信号作用のBorn型殻状態数）**

上の仮定の下で、全枝を同じLiouville母測度で数えると枝状態数は

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

となる。零信号、安全閾値未満、有限幅遷移域は無反応 $\varnothing$ へ送る。一般に各明反応枝が $q$ 個の独立な作用分配方向を持てば $\Omega_i\propto(A_i^\delta)^q$ であり、全容量族でBorn型線形則を保つのは $q=1$ に限る。
<!-- theorem-end:theorem -->

作用殻を消去する表示では

```math
E_i^\delta(v)=-\Theta\log\pi_i^\delta(v)
```

を条件付き中間状態有効自由エネルギーとして使う。状態数を残す表示と消去表示は同値であり、同じ縮約分配関数へ $\Omega_i^\delta e^{-E_i^\delta/\Theta}$ を入れて二重計数してはならない。

## R161/R162の有限再平衡化

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

と置く。

<!-- theorem-start:theorem -->
**定理（R161：任意の有限信号方向に対する粒子位置再平衡化）**

任意の非零入力 $v$ に対して $\pi^\delta(v)$ は上の連続時間跳躍過程の唯一の定常分布であり、任意の初期枝分布 $p_0$ から

```math
D_{\rm TV}(p_{\tau_X},\pi^\delta(v))
\leq
C_\delta e^{-\lambda_\delta\tau_X}
```

である。また理想枝重み $w_i(v)=|(\Psi v)_i|^2/(v^\dagger v)$ との差は $D_{\rm TV}(\pi^\delta,w)\leq\delta/(1+\delta)$ である。
<!-- theorem-end:theorem -->

<!-- theorem-start:theorem -->
**定理（R162：局所詳細釣合い率の有限衝突熱浴実現）**

各辺に対称障壁と有限個の入射cellを置き、入射位置、到着時計、運動方向、反射枝、出射エネルギー、履歴cellを完全状態へ含めれば、正逆衝突を1対1に対応させる有限Hamiltonian散乱でR161の率を任意精度で近似できる。固定観測時間での縮約経路測度誤差は、cell overflow、エネルギー尾部、閾値平滑化、時計、入力保持の誤差和で抑えられ、超過cellと比較境界は無反応へ送れる。
<!-- theorem-end:theorem -->

作用殻fiberは状態数を、衝突bathは粒子位置遷移を担い、同じ自由度ではない。

**系（粗視化経路熱力学）**

R161の局所詳細釣合い過程、またはR162の縮約過程の正逆protocolについて、粗視化経路エントロピー生成 $\Sigma$ は

```math
\frac{\mathcal P_F[\omega]}{\mathcal P_R[\omega^\dagger]}
=e^{\Sigma[\omega]},
\qquad
\left\langle e^{-\Sigma}\right\rangle_F=1,
\qquad
\langle\Sigma\rangle_F\geq0
```

を満たす。瞬間quench $v^-\to v^+$ では

```math
W_i^{\rm rel}
=\Theta\log\frac{\pi_i^\delta(v^-)}{\pi_i^\delta(v^+)},
\qquad
\left\langle e^{-\beta W^{\rm rel}}\right\rangle=1,
```

```math
\langle W^{\rm rel}\rangle
=\Theta D_{\rm KL}
\left(\pi^\delta(v^-)\|\pi^\delta(v^+)\right).
```

これは作用殻を消去した粒子位置跳躍過程の厳密な関係であり、全装置周期の機械仕事・微視的熱収支ではない。証明と表示間の仕事の換算は付録Kに置く。

## R170：M50固定入力時刻有限枝instrument

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

R170は有限枝instrumentの共通定理であり、M37を前提にしない。Q1のR143、Q2-2のR180C、Q3の固定時刻読出しはこの定理の特殊化または合成である。完全な証明と誤差台帳は付録Kに置く。

**系（共通instrumentの安定性）**

理想分布 $p,p'$ と実分布 $q,q'$ が

```math
D_{\rm TV}(q,p)\leq\varepsilon,
\qquad
D_{\rm TV}(q',p')\leq\varepsilon'
```

を満たせば

```math
D_{\rm TV}(q,q')
\geq
D_{\rm TV}(p,p')-\varepsilon-\varepsilon'.
```

任意の事象 $A$ について

```math
|q(A)-q'(A)|
\geq
|p(A)-p'(A)|-\varepsilon-\varepsilon'
```

であり、任意の有界観測量 $f$ について

```math
|\mathbb E_qf-\mathbb E_pf|
\leq
\operatorname{osc}(f)\varepsilon,
\qquad
\operatorname{osc}(f)=\sup f-\inf f.
```

従って理想分布間の分離が誤差和より大きければ、有限装置でも区別可能性が残る。この系をR124/R125の識別とR180CのBell監査へ共通に用いる。

## M54の一様register、port、bank

$n$ 量子ビット、深さ $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。M54では計算基底文字列 $x$ を受動信号モードへ直接対応させる。

```math
|x\rangle
\longleftrightarrow
Z_x,
\qquad
Z=(Z_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

M54はsignal、anti-register、filter work、rejected-history、radial repump、raw/regularized容量pointer、一様gate bus、collision cell、cold bank、spent bank、出力記録、clockを持つ。内部の受動自由度、静的結合、状態容量、受動並列度は $2^n\operatorname{poly}(n,d)$ まで許す。一方、外部programが指定するのはgate種、1個または2個の対象量子ビット、gate順序、現在読む出力bit、blanking round、cell index、clock窓だけである。$2^n$ モードの列挙、モード別初期化・較正・読出し、指数長の係数表、回路別配線、出力確率の事前計算を許さない。

M54はR181Bの反復tensor-liftを一般 $n$ へ延長しない。R179でbankをblank化した後、定数次元sourceを $0^n$ root modeへ接続して計算基底入力を作る。別の基底入力は回路先頭の $X$ gateで作る。gate列はR181C、末端bit列はR181D、結果相関履歴の境界はR178D、供給はR179が担う。

## R181B：Q1-port可逆tensor-lift

固定された2入力または3入力について、Q1型portの信号を $a,b$、blank共同registerを $Z$、anti-registerを $G$ とする。R112の三次乗算pulseを有限列 $S_0$ として使い、係数を測定または外部転記せず

```math
(a,b,0,0,W_0)
\longmapsto
(a,b,Z=a\otimes b,G=\overline{a\otimes b},W_1)
```

を作る。

<!-- theorem-start:theorem -->
**定理（R181B：非規格化Q1-port可逆tensor-lift）**

$a,b$ が固定安全集合にあり、共同registerとanti-registerが指定blank幅以内なら、有限個の実正準対、有限clock窓、R112型の可逆乗算pulseにより上の写像を任意の誤差 $\eta_{\rm lift}>0$ 以内で実装できる。拡大状態 $(a,b,Z,G,W)$ 上の写像は1対1で、逆clock列により入力とworkを回収できる。controllerは $a_j,b_k$ を読み出さず、積係数表を入力しない。3入力は同じliftを2回使って作る。本結果は入力数を固定したQ2-1--Q2-3の構成であり、一般 $n$ の多項式資源tensor-product準備を主張しない。
<!-- theorem-end:theorem -->

詳細なpulse列、参照位相、有限誤差は付録Cに置く。

## R181C：永続register上の一様局所gate合成

対象量子ビット集合 $S$ の大きさを $k\in\{1,2\}$ とし、$g$ を固定有限gate集合の $2^k$ 次元unitaryとする。spectator labelを $r\in\{0,1\}^{n-k}$ と書き、同じ局所生成子 $h_g$ を全sectorへ置く。

```math
H_{g,S}
=
\bigoplus_r h_g^{(r)},
\qquad
U_{g,S}=g_S\otimes I_{\bar S}.
```

<!-- theorem-start:theorem -->
**定理（R181C：永続register上の一様局所gate合成）**

各sector blockが同じ局所規則から生成され、実装block $\widetilde g_r$ が一様に $\|\widetilde g_r-g\|\leq\eta_g$ を満たし、異なるsector間の漏れの作用素normが $\eta_{\rm leak}$ 以下とする。このとき1個の共有clock窓で全spectator sectorへgateを作用でき、

```math
\|\widetilde U_{g,S}-U_{g,S}\|
\leq
\eta_g+\eta_{\rm leak}
```

である。block数による和は生じない。深さ $d$ のgate列では、全gateのglobal phaseを除いた誤差は各窓の作用素norm誤差の和以下である。固定gate集合なら、対象指定、制御channel、命令数は $n,d$ の多項式、静的sector結合は指数的でも一様有限規則から生成できる。
<!-- theorem-end:theorem -->

固定 $n=2,3$ では同じ定理がCNOT、局所操作、逆演算の有限列を与える。一般 $n$ では上のsector-broadcastを使う。いずれも中間測定、共同momentへの置換、再準備を行わず、同じ $Z$ を全gate窓で保持する。3次元Euclid空間への局所埋込み、指数個の静的結合の総製造費、全結合を個別に調整する方法は主張しない。

## R181Dで使うprojector latch・可逆filter補題

出力bit $k$ に対する計算基底射影を $P_{k,0},P_{k,1}$ とし、

```math
P_{k,0}+P_{k,1}=I,
\qquad
P_{k,0}P_{k,1}=0
```

とする。容量pointerへ保持する作用を

```math
J_{k,b}(Z)=\mathcal J_0Z^\dagger P_{k,b}Z
```

とする。signalとworkの2 bank上に

```math
F_{k,b}
=
\begin{pmatrix}
P_{k,b}&P_{k,1-b}\\
P_{k,1-b}&-P_{k,b}
\end{pmatrix}
```

を置く。

<!-- theorem-start:lemma -->
**補題（直交projector作用latchとinvolution filter）**

上の $F_{k,b}$ は

```math
F_{k,b}^\dagger F_{k,b}=I,
\qquad
F_{k,b}^2=I
```

を満たし、blank work bankに対して

```math
F_{k,b}(Z,0)
=
(P_{k,b}Z,P_{k,1-b}Z)
```

と作用する。容量latchを信号に対する制御剪断として実装すれば、blank容量momentum上で $J_{k,0},J_{k,1}$ をpointerへ保持し、理想信号 $Z$ を変更しない。計算基底bit projectorとfilterはbit labelだけから一様に生成され、$2^n$ 成分の列挙を必要としない。
<!-- theorem-end:lemma -->

この補題は確率的な枝選択を行わない。selectorの生成はR164/R170、選択後の信号更新はR181Dが担う。

## R181D：R170駆動projector-tree Born instrument

第 $k$ 段、履歴node $u$ の入力を $Z_u\neq0$ とし、直交射影 $P_{u,0},P_{u,1}$ に対するraw容量を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

とする。作用殻へ渡すregularized容量は、固定 $q_0,q_1>0$、$q_0+q_1=1$ に対し

```math
A_{u,b}^\delta=J_{u,b}+\delta q_bJ_\Sigma
```

である。R164/R170は $b$ を確率 $(p_{u,b}+\delta q_b)/(1+\delta)$ で選ぶ。cutoffは除算せず、raw比較 $J_{u,b}\gtrless\tau J_\Sigma$ を用いる。幅 $\gamma J_\Sigma$ のguard帯、selector plateau外、collision overflowは正式な無反応 $\varnothing$ へ送る。selectorをlockした後にfilter $F_{u,b}$ を作用し、非選択成分をwork/spentへ保持する。選択成分はR181Aの $\kappa=0$ radial-only port

```math
\dot Z=g(J_*-Z^\dagger Z)Z
```

で標準作用へ戻す。$J_{u,b}\geq\tau J_\Sigma$ の下限から固定repump時間を選び、未知の $p_{u,b}$ に依存するsqueezeをcontrollerへ入れない。

<!-- theorem-start:theorem -->
**定理（R181D：R170駆動projector-tree Born instrument）**

理想node instrumentを深さ $m$ まで合成すると、葉 $y=(y_1,\ldots,y_m)$ の確率は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2
}{
\|Z_0\|^2
}
```

となり、指定projector-treeのBorn分布に一致する。入力分布誤差を $\varepsilon_{\rm in}$、安全履歴上の第 $k$ node実装誤差を $\bar\varepsilon_k$ とすれば、無反応を含む完全結果分布は

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+\frac{m\delta}{1+\delta}
+2m(\tau+\gamma)
+\sum_{k=1}^m\bar\varepsilon_k.
```

$\bar\varepsilon_k$ にはR170選択、controlled filter、radial repump、routeを各1回だけ含める。filter作用素誤差が $\eta_F<\sqrt\tau$ なら、選択後の規格化ray誤差は $2\eta_F/(\sqrt\tau-\eta_F)$ 以下である。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

R181DはQ1の深さ1、Q2-1の深さ2、Q2-3の深さ3、Q2-4の深さ $n$ に同じnode機構を使う。最終分布を段ごとの規格化成功分布へ比較せず、実際の初期信号が持つBorn分布と完全結果分布を末端で一度だけ比較する。

## R178D：逐次history逆掃除・collective reset定理

$Y\in\{0,1\}^n$ をbit data記録、$F\in\{0,1\}$ を無反応flagとし、完全結果は $(Y,F)$ として保持する。以下の情報容量下界は $Y$ だけに対する弱い下界であり、flagと微視的履歴に必要な追加容量を除外しない。

<!-- theorem-start:theorem -->
**定理（R178D：逐次history逆掃除・collective reset定理）**

gate、latch、filter、clockの完全な微視的履歴を保持する。出力 $Y$ を別の記録へ可逆copyした後なら、出力記録と相関しないHamiltonian workを逆順に掃除できる。R181Aのradial repumpは採用開放流なので、その散逸履歴を含む無履歴の逆掃除は主張しない。

一方、$(Y,F)$ を保持したまま装置、bath、履歴の全てを同じ初期点へ戻す1対1写像は存在しない。結果と相関するselector、使用済みpointer、collision履歴、clock履歴はspent tapeへ送る必要がある。spent状態から $Y$ を復号する誤り率を $p_{\rm e}$ とし、Fano補正を $\eta_{\rm F}=h_2(p_{\rm e})+p_{\rm e}\log(|\mathcal Y|-1)$ と置く。natsで測ったspent側の情報容量 $C_{\rm spent}$ は

```math
C_{\rm spent}\geq H(Y)-\eta_{\rm F},
\qquad
H(Y)\leq n\log2
```

を満たす。熱的resetの仕事・熱下界は、bath温度と消去protocolを別に指定した場合だけ従う。
<!-- theorem-end:theorem -->

R170の粗視化Markov pathだけから微視的状態を逆算しない。逆転に使用できるのはR162の完全collision履歴、R181Dのselector/filter履歴、または開放portの環境履歴である。同じbath seedまたは同じ使用済みcellを再利用した試行列を独立同分布とは呼ばない。

旧fixed-volume aperture、first-index tape、dyadic threshold経路はR181Dへ統合せず退役させる。旧経路が誤りだと結論したのではなく、Q1とQ2で同じR170作用殻receiverを使うという今回の模型統一に不要だからである。式と旧誤差台帳は `notes/superseded_r178_aperture_sampler.md` とGit履歴に残す。

## R179：一様blank-bank・collision-cell・spent供給定理

全補助bankを $W\in\mathbb C^{D_{n,d}}$、$D_{n,d}\leq2^np(n,d)$ とまとめる。各blanking roundでbank modeとincoming cold modeの対応pairへ同じ形式のpartial SWAPを並列に作用させる。couplerは一様有限規則から作る同一の静的二次Hamiltonianとし、受動clockがroundを進める。指数個のcouplerを外部から個別に開閉せず、外部quench workをbank次元へ比例させない。

```math
W_{r+1}=C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1,
\qquad
\|E_r\|\leq\eta_{\rm cold}.
```

pairごとの全変換は2-mode回転で実正準かつ可逆であり、cold側出力はspent側へ保持する。active成分だけを捨てて非可逆化しない。R162/R170が使うcollision cell、selector pointer、filter work、radial-port環境の各bankは同じindex規則で供給する。

<!-- theorem-start:theorem -->
**定理（R179：一様blank-bank・collision-cell・spent供給定理）**

次の条件を仮定する。

1. bank初期normは $R_{\rm in}\leq\exp p_1(n,d)$ である。
2. cold layerのaggregate誤差は $\eta_{\rm cold}$ 以下である。
3. partial SWAPの残留係数は一様に $\rho<1$ である。
4. collision cellの初期lawは回路出力と独立で、同じ有限局所規則から生成される。

このとき

```math
\|W_R\|
\leq
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho},
```

```math
R
=
O\!\left(
n+\log d+\log(1/\varepsilon_{\rm blank})
\right)
```

で全bankを一様にblank化できる。続いて定数次元sourceをroot modeへSWAPし、R181Dの各nodeへ有限個のR162 collision cell、selector、filter workをclock順に供給できる。外部program長、準備時間、clock round、必要精度は $n,d,1/\epsilon$ の多項式である。静的couplerと受動clockが一括作用する限り、外部controllerの仕事をbank次元へ比例させない。cold bathとspent bathの受動自由度、状態容量、総作用移送、総熱は指数的でもよい。
<!-- theorem-end:theorem -->

R179は低作用bathを無から生成しない。供給測度は同じ局所lawを反復する回路非依存の規則であり、出力確率表を含まない。外部精度を多項式に保つには、exact invariant blankを持つcold source、またはbank全体のaggregate誤差を一様contractで保証するcold sourceが必要である。有限温度の独立noiseが各modeに定数作用を残す場合、aggregate blank誤差は $D_{n,d}$ とともに増大するためR179の仮定を満たさない。

## M54の合成誤差と資源

M54の完全結果分布を $P_{\rm M54}$、理想回路Born分布を $P_{\rm circ}$ とする。誤差を重複計上しなければ、

```math
D_{\rm TV}(P_{\rm M54},P_{\rm circ})
\leq
\varepsilon_{179}
+d\eta_{\rm gate}
+\varepsilon_{\rm leak}
+\frac{n\delta}{1+\delta}
+2n(\tau+\gamma)
+\sum_{j=1}^n\bar\varepsilon_j.
```

ここで

```math
\varepsilon_{179}
\leq
C_{\rm root}
(\varepsilon_{\rm blank}
+\varepsilon_{\rm src}
+\varepsilon_{\rm swap})
+\varepsilon_{\rm coll}.
```

$\bar\varepsilon_j$ は第 $j$ 段のR170選択、controlled filter、radial repump、route、clockだけを含む。R179へ入れたcold floorとcollision誤差を再び含めない。

$\eta_{\rm gate}=O(\epsilon/d)$ とし、$\tau,\gamma,\delta,\bar\varepsilon_j$ はそれぞれ $O(\epsilon/n)$ と選べる。

保守的な逐次読出し時間は

```math
O\!\left(
\frac{n^2}{\epsilon}\log\frac n\epsilon
\right)
```

である。必要な殻stiffnessは $O(n^2/\epsilon^2)$、collision fluxは $O(\sqrt{n/\epsilon})$、barrier rangeは $O(\log(n/\epsilon))$ で抑えられる。受動modeとcold bath容量は指数的だが、回路記述、外部命令、準備round、gate窓、読出し時間、必要精度は多項式である。

## Q2-4の判定と境界

R181Cは指数個の個別gate設定、R181Dは全 $2^n$ 葉の一括読出し、R179は指数個の個別blank初期化を避ける。従ってM54はQ2-4を条件付き達成へ進める。条件は、R170作用殻、R162 collision cell、controlled filter、radial repump、一様bank--bath結合を同じsafe setとclockで接続することである。

本構成は通常の計算量理論における多項式資源の古典simulationではない。指数個の受動自由度、静的結合、bath容量、総熱を許した上で、外部制御と総時間を多項式に抑える結果である。未知量子入力、適応中間測定、誤り訂正、固定容量bathによる無期限独立同分布標本は主張しない。M54はQ1・Q2の共通親模型族だが、同一の製造済み装置や同一パラメータを主張しない。

## 物理的意味と限界

熱化終了後の局所記録生成子は、枝 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、列挙した部品を1つの具体的有限局所Hamiltonianへ統合済みだと主張しない。現行の条件付き達成または部分達成は、この未統合部分を明示して判定する。一意エルゴードな外部scheduleまたは有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。

# 第II部　単一量子ビット型操作と測定

# M47のHopf準備・条件付きGibbs再平衡化・傾斜測定

> **位置づけ：** Q1をM54の $n=1$ 特殊化として、R181A準備、R140操作、R181Dの深さ1読出し、R143状態更新へ再編する。測定統計は導出済み、Zeno効果はQ1-2の残件である。


## Q1の統計力学的再編と主張範囲

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

W型とはまず信号担体の空間生成子に与える2重井戸構造であり、古典粒子1個を井戸へ置くだけで2準位信号が生じるという意味ではない。M47の粒子位置と作用殻による結果選択は別の物理段階である。

本章は、Q1のM47を統計力学的な操作周期として再編する。基本状態は、W型ポテンシャル中で各試行に1つ存在する粒子位置 $X$ と、2モード信号bath座標 $Z$ を持つ共同測度

```math
\mu(dX\,dZ)
```

である。複素振幅を独立した実在場として先に置かず、規格化共分散

```math
C_Z
=
\frac{\mathbb E_\mu[ZZ^\dagger]}
{\mathbb E_\mu[Z^\dagger Z]}
```

が階数1の場合にだけ、その因子 $c$ を統計的rayとして使う。共通R135の階数1支持節により、単一試行の値 $z=Z(\omega)$ は $z=\alpha(\omega)c$ とほとんど確実に書ける。M50と局所制御器が入力するのは $c$ または $C_Z$ でなく、この単一試行の $z$ である。本章では粒子位置と信号方向の整合を全時刻では要求しない。Hamiltonian制御中は粒子位置が瞬時の信号bath方向から外れてよく、各操作面で付録Kの有限衝突熱浴を接続して条件付きGibbs分布へ戻す。

Q1の測定はR181Dの深さ1 nodeをW型分析器へ特殊化し、次の仕事行程、熱化行程、記録行程へ分ける。

1. R181AのW型2モード系で信号bath方向を準備する。
2. 信号bath方向を保持し、初期操作面のR164作用殻を準備する。
3. R161、R162、R170で初期粒子位置を準備する。この段階は出力選択ではない。
4. 衝突熱浴を切り、W型2モードの傾斜制御で測定軸の固有方向を左右局在方向へ写す。
5. 分析器終了後にR181Dのraw容量をlatchし、regularized作用殻を更新する。R161、R162、R170で出力selectorを形成してlockする。
6. 入射セルと辺遷移を止め、トンネル振動より速く、高モード間隔より遅く傾斜を立ち上げる。
7. 左右井戸の有効自由エネルギー差と閉じた辺ゲートで、既存の粒子位置を記録終了まで片側へ保持する。
8. 各井戸に置いた局所記録ポインターが、その場所にある $X$ だけを記録する。
9. 安全枝ではR181Dの可逆filterで選択成分と補成分を分け、radial-only portとR143の結果別templateで次段状態を作る。
10. 測定前情報と使用済み装置状態を外部セルへ残し、内部補助を逆計算と交換resetで戻す。

局所記録は、$C_Z$、統計振幅、全密度、確率流、遷移率を入力にしない。従って、物理的複素場のcurrentから全時刻位置率を作る

```math
b
\longrightarrow
q(b)
\longrightarrow
X
```

という因果律を使わない。

共通M54/R181Aは、実正準担体のseed測度を雑音零の開放driftで押し出し、信号bath方向を目標位相円へ有限時間で吸引する。付録HのR181AのW型2モード系はそのW型2モード特殊化であり、別の準備機構ではない。共通R135は階数1共分散の統計因子を単一試行信号の支持へ接続し、M50/R164は同じ試行の有限信号作用を正則化枝容量へ写し、各排他的枝の2作用殻状態数からBorn型条件付き重みと有効自由エネルギーを導く。第2章のR161は任意有限信号方向に対する粒子位置の一様指数再平衡化、R162はその局所詳細釣合い率の有限衝突実現、続く粗視化経路熱力学系は制御切替と粒子位置経路の監査式を与える。R181A、R135、R164、R161を順に使えば、信号bath方向、条件付き状態数、粒子位置分布を同じ操作面へ有限誤差で準備できる。

第5章のR180Cは、R161を固定singlet型Bell装置の各翼へ適用する。R161は任意のM47 rayに対する平方根率を与え、R162は固定した単一試行信号bath座標に対する衝突熱浴実現を与える。R164は各翼の局所条件付き地形にも使えるが、M54からのblock latch、paired-Hopf準備、2翼周期全体を導かない。R161、R162、R164をQ1の共通根拠とする。

R164により、条件付き地形 $E_i^\delta=-\Theta\log\pi_i^\delta$ は確率から直接設計する量でなく、作用殻を消去した条件付き中間状態有効自由エネルギーとして得られる。作用殻明示表示の $\Omega_i^\delta$ と消去表示の $e^{-\beta E_i^\delta}$ を同じ分配関数で掛けず、状態数を二重計数しない。枝容量結合、殻内平衡化、枝対称性、信号bath保持反作用を同じ有限局所Hamiltonianへ統合しておらず、Hopf pump、記録、resetを含む周期全体の仕事・熱・エントロピー収支も未閉鎖である。ただし、これらは現行M47を強める実装・熱力学的課題であり、再編後のQ1-2の達成条件には含めない。

## 階数1共分散とBloch球

Pauli行列を $\sigma_x,\sigma_y,\sigma_z$ とし、共分散のBloch成分を

```math
r_k
=
\operatorname{tr}(C_Z\sigma_k)
```

で定める。$C_Z$ はHermitian、正半定値、trace 1なので

```math
C_Z
=
\frac12
\left(
I_2+\boldsymbol r\cdot\boldsymbol\sigma
\right),
\qquad
|\boldsymbol r|\leq1
```

である。階数1なら $C_Z=cc^\dagger$、$c^\dagger c=1$ と書け、$|\boldsymbol r|=1$ である。$c$ と $e^{i\alpha}c$ は同じ $C_Z$ を与えるため、共通位相は観測状態に含まれない。

一般のHermitian行列 $G(t)$ に対して、古典2モードHamiltonianを

```math
H_G(t)
=
Z^\dagger G(t)Z
```

とする。正準方程式は

```math
i\mathcal J_0\dot Z
=
G(t)Z
```

であり、規格化共分散は

```math
i\mathcal J_0\dot C_Z
=
[G(t),C_Z]
```

に従う。

**R135の2次元系。**

trace 1の正半定値2次共分散について、階数1条件は $|\boldsymbol r|=1$ と同値である。階数1共分散の集合は共通位相を除いた $\mathbb{CP}^1\simeq S^2$ であり、$H_G$ の古典正準流はこの球面上の回転を与える。従ってM47の純粋2モード統計状態は、独立した複素振幅場を仮定せずBloch球を持つ。
これはR135を時間依存2モード生成子へ特殊化したものである。共分散の回転は厳密だが、粒子位置周辺のmatching保存は別の条件である。

## W型ポテンシャルと局在基底

対称W型生成子 $h_W(0)$ の最低2固有モードを、実偶関数 $\phi_0$ と実奇関数 $\phi_1$ とする。固有値を $E_0<E_1$、平均と半分裂を

```math
\overline E
=
\frac{E_0+E_1}{2},
\qquad
J
=
\frac{E_1-E_0}{2}
```

とする。位相規約を選び、左右局在基底を

```math
|L\rangle
=
\frac{\phi_0+\phi_1}{\sqrt2},
\qquad
|R\rangle
=
\frac{\phi_0-\phi_1}{\sqrt2}
```

と置く。左右の名称は $x_L=\langle L|x|L\rangle<0<x_R=\langle R|x|R\rangle$ となるように $\phi_1$ の符号を固定する。従って $x_{01}=\langle\phi_0|x|\phi_1\rangle<0$ である。以下で $\sigma_z=\operatorname{diag}(1,-1)$ はL、Rの順とし、この規約を途中で変更しない。

制御可能な1次傾斜を

```math
h_W(F)
=
h_W(0)-F(t)x
```

とする。対称性から最低2モード内では対角位置要素が消え、局在基底での生成子は共通エネルギーを除いて

```math
G_F(t)
=
-J\sigma_x
+
\frac{\varepsilon(t)}{2}\sigma_z,
\qquad
\varepsilon(t)
=
2F(t)
\left|
\langle\phi_0|x|\phi_1\rangle
\right|
```

となる。$\varepsilon=F(x_R-x_L)$ はFの符号を保持する。$-J\sigma_x$ は左右トンネル振動、$\varepsilon\sigma_z/2$ は左右エネルギー差である。

## 傾斜制御による任意のSU(2)操作

傾斜を零にした区間は $\sigma_x$ 回転を与える。零でない一定傾斜は、$x$ 軸と平行でない $xz$ 平面内の軸回転を与える。2本の非平行回転軸の有限積は $SU(2)$ 全体を生成する。Lie代数では

```math
[\sigma_x,\sigma_z]
=
-2i\sigma_y
```

なので、$\sigma_x$ と $\sigma_z$ から3方向が閉じる。

一定傾斜 $\varepsilon$ で $|L\rangle$ から開始したとき、右井戸方向への2モード作用比は

```math
P_{L\to R}(t)
=
\frac{4J^2}{\varepsilon^2+4J^2}
\sin^2
\left(
\frac{\sqrt{\varepsilon^2+4J^2}}{2\mathcal J_0}t
\right).
```

この式は、共鳴 $\varepsilon=0$ での完全振動、離調による振幅低下、振動数の変化を同じ担体で与える。

<!-- theorem-start:theorem -->
**定理（R140：W型2モードの制御、占有振動、傾斜保持）**

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はunitary共役であり、trace、正値性、階数を保存する。零傾斜では角周波数 $(E_1-E_0)/\mathcal J_0$ の左右占有振動を与え、一定傾斜では上の離調公式に従う。さらに射影内の左右占有変化は第3.7節の傾斜保持評価に従う。全W型系で $\varepsilon_{\rm lock}$ を用いる場合は、$J\ll|\varepsilon_m|\ll G$ と $\mathcal J_0/G\ll\tau_q\ll\mathcal J_0/J$ に加え、付録B.5の状態誤差条件を満たすことを仮定する。
<!-- theorem-end:theorem -->

R140は制御された2モード生成子についての厳密結果である。元の全W型系で同じ精度を得るには、高モード漏れと傾斜切替誤差を別に評価する。

## 2モード窓と傾斜切替の尺度階層

第3固有値を $E_2$ とし、最低2モードと高モードの間隔を

```math
G
=
E_2-E_1
```

とする。測定傾斜 $\varepsilon_m$ と切替時間 $\tau_q$ は

```math
J
\ll
|\varepsilon_m|
\ll
G,
```

```math
\frac{\mathcal J_0}{G}
\ll
\tau_q
\ll
\frac{\mathcal J_0}{J}
```

を満たすように選ぶ。時間尺度の右側 $\tau_q\ll\mathcal J_0/J$ はトンネル振動に対して急な切替、左側 $\mathcal J_0/G\ll\tau_q$ は高モードgapに対して遅い切替を表す。エネルギー尺度 $J\ll|\varepsilon_m|\ll G$ は、離調固定を強くしながら最低2モード窓を保つ条件である。

固定した有限格子W型族では、制御中の高モード結合 $v=\sup_t\|(I-P_2)(-F(t)x)P_2\|$ と高モード間隔を別に測る。傾斜行列要素と切替形状を固定した断熱的評価で得る

```math
\ell_{2m}\lesssim C_W\left[(v/G)^2+(\mathcal J_0/(G\tau_q))^2\right]
```

は高モード漏れ確率の次数評価であり、全状態または左右測定分布の誤差ではない。$C_W$、初期準備、制御中の間隔、微分上界への依存を固定する必要があり、任意の駆動に対する一様定理とはしない。分布誤差台帳の $\varepsilon_{2m}$ は、付録B.5で定義する全状態差からの上界を使う。漏れが小さくても低モード内の位相補正は蓄積し得る。

深いW型族で $J/G\to0$ なら、例えば

```math
|\varepsilon_m|
=
\sqrt{JG},
\qquad
\tau_q
=
\frac{\mathcal J_0}{\sqrt{JG}}
```

と選べる。このとき4つの比

```math
\frac{J}{|\varepsilon_m|},
\quad
\frac{|\varepsilon_m|}{G},
\quad
\frac{\mathcal J_0}{G\tau_q},
\quad
\frac{J\tau_q}{\mathcal J_0}
```

は全て $\sqrt{J/G}$ の次数で零へ近づく。この尺度選択だけでは全制御時間の状態誤差は閉じず、第3.5.1節の残差も評価する。

### R140のM37実装に関する条件付き系

M37の有限W型制御を第6.17節で定義する。同じ初期実座標、同じ制御列、同じ時間区間で、実運動の包絡 $b$、全W型の有効解、2モード解を比較する。$V(t)^\dagger V(t)=I_2$ とし、$g(t)=g(t)^\dagger$ に対して $i\mathcal J_0\dot c=g(t)c$、$\|c(0)\|=1$ とする。共通位相を除く場合はその位相をVへ含める。

<!-- theorem-start:corollary -->
**系（R140のM37有限時間制御受渡し）**

実運動と同じ初期値から始めた全W型有効解との差が区間全体で $\varepsilon_{\rm env}$ 以下とする。等長埋込みVは連続かつ区分的に微分可能とし、残差を

```math
R(t)=h_W(t)V(t)-i\mathcal J_0\dot V(t)-V(t)g(t)
```

と定義する。初期差 $d_0=\|b(0)-V(0)c(0)\|$ に対し

```math
\|b(T)-V(T)c(T)\|
\leq\varepsilon_{\rm env}+d_0+
\frac1{\mathcal J_0}\int_0^T\|R(t)\|\,dt
```

が成立する。目標のSU(2)操作への合成誤差は別に加える。
<!-- theorem-end:corollary -->

証明は付録B.17。固定基底では $\dot V=0$ として漏れ結合と有効位相を評価する。瞬間固有基底では基底移動項を落とさない。この系は誤差を接続する厳密な道具であり、任意精度のW型制御族を構成したという結論ではない。

零傾斜完全移送時間は $T_X=\pi\mathcal J_0/(2J)$ である。深い井戸でJが減ると、静的R86の時間依存誤差もこの全時間で評価する必要がある。共通位相を除いた周波数差の較正で改善できる場合はあるが、反回転振動と駆動中の偏差は別に残る。初期共通位相の異なる試行に同じ上界を適用し、R135の集団輸送へ接続する。Born型選択、粒子輸送、測定周期は本系の結論に含めない。

## M50/R170のQ1二枝特殊化

Q1では共通仕様M50に
$v=z$、$\mathcal I=\{L,R\}$、$\Psi=\Phi$
を代入する。第2章のR164により

```math
\pi_i^\delta(z)
=
\frac{|(\Phi z)_i|^2/(z^\dagger z)+\delta q_i}{1+\delta}
```

が2作用殻の規格化状態数として得られ、R161はこの分布への有限時間再平衡化、R162はその有限衝突実現を与える。R170では再平衡化後に入射cellを止め、左右ゲートを閉じ、局所記録を作る。従ってQ1章で独立に必要なのは、W型信号の準備と分析器、左右固定、結果別テンプレート交換であり、共通定理を再宣言しない。

作用殻を消去した条件付き中間状態有効自由エネルギーは

```math
E_i^\delta(z)=-\Theta\log\pi_i^\delta(z)
```

である。第2章の粗視化経路熱力学系は、解析器quenchと粒子位置遷移の正逆経路比、積分ゆらぎ関係、相対有効散逸を監査する。ただしこれはHopf pump、作用殻準備、信号bath保持、記録、template交換、resetを含む全周期の機械仕事・微視的熱収支ではない。

## R140の傾斜保持節

分析器操作を終えた直後に傾斜を立ち上げる。2モード射影内では、傾斜保持中の反対側遷移確率は全時刻で

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

を満たす。右から左も同じ上界である。

**R140の傾斜保持評価。**

最低2モード内の任意の規格化共分散 $C_Z$ について、一定傾斜 $\varepsilon_m$ の保持中の左占有率を $p_L(t)=\operatorname{tr}(|L\rangle\langle L|C_Z(t))$ とする。このとき全時刻で

```math
|p_L(t)-p_L(0)|
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}.
```

特に切替開始時の共分散が $|L\rangle\langle L|$ または $|R\rangle\langle R|$ なら、反対井戸へ移る作用比は $4J^2/(\varepsilon_m^2+4J^2)$ 以下である。一般入力について、2モード内の占有変化と保持中の残留結合を合わせた周辺固定誤差を

```math
\varepsilon_{\rm lock}
\leq
\frac{2|J|}{\sqrt{\varepsilon_m^2+4J^2}}
+
\varepsilon_{\rm hold}
```

で評価する。全W型系の固定中分布誤差は $\varepsilon_{2m}+\varepsilon_{\rm lock}$ 以下である。$J/G\to0$ の深いW型族では、前節の選択により射影内の固定誤差を小さくできる。全W型系については同時に $\varepsilon_{2m}$ を小さくする条件が必要である。
R140が固定するのは信号bathの左右占有周辺であり、一般入力を左右固有状態へ収縮させる結果ではない。周辺固定だけから単一試行の粒子位置 $X$ の経路滞在は従わない。そこで再平衡化終了後にR162の入射セルを止め、辺ゲートを閉じる。記録時間中の離脱失敗率 $\varepsilon_{\rm res}$ は、有限障壁裾、エネルギー切断、閾値平滑化、時計ずれから評価する。どちらの枝にいるかは、ゲート閉鎖前から存在するM47粒子位置を局所的に読む。

## 任意軸分析器

測定軸を単位ベクトル $\boldsymbol n$、射影を

```math
\Pi_{\boldsymbol n,s}
=
\frac12
\left(
I_2+s\boldsymbol n\cdot\boldsymbol\sigma
\right),
\qquad
s\in\{+1,-1\}
```

とする。R140により、有限傾斜列 $A_{\boldsymbol n}$ を

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,+}
A_{\boldsymbol n}^\dagger
=
|L\rangle\langle L|,
```

```math
A_{\boldsymbol n}
\Pi_{\boldsymbol n,-}
A_{\boldsymbol n}^\dagger
=
|R\rangle\langle R|
```

となるように選べる。入力共分散を $C_Z$ とすると、理想射影重みは

```math
p_s
=
\operatorname{tr}
\left(
C_Z\Pi_{\boldsymbol n,s}
\right).
```

分析器後の共分散は $C_Z'=A_{\boldsymbol n}CA_{\boldsymbol n}^\dagger$ である。分析器中は粒子位置周辺がこの共分散を追跡しなくてよい。終了後の信号bath方向を固定し、R161の再平衡化を時間 $T_X$ だけ作用させれば、左右井戸の粒子位置頻度が $p_s$ を有限コントラストと有限混合誤差で読む。

## 左右空間読出しの有限コントラスト

左半空間への位置射影を $\Pi_L$ とし、

```math
B_W
=
\langle\phi_0|\Pi_L|\phi_1\rangle
```

と置く。位相規約で $B_W\geq0$ とする。最低2モード上の左読出し効果は、偶奇基底で

```math
E_L
=
\begin{pmatrix}
1/2&B_W\\
B_W&1/2
\end{pmatrix}
```

である。局在基底では

```math
E_L
=
(1-\eta_W)
|L\rangle\langle L|
+
\eta_W
|R\rangle\langle R|,
\qquad
\eta_W
=
\frac12-B_W.
```

従って $0\leq\eta_W\leq1/2$ である。理想分析器後の左占有率は

```math
P_L
=
\eta_W
+
(1-2\eta_W)p_+,
```

なので

```math
|P_L-p_+|
\leq
\eta_W.
```

**R143で使う有限コントラスト評価。**

分析器終了後にR164の作用殻準備とR161、R162の粒子位置再平衡化を時間 $T_X$ だけ作用させ、その誤差を $\varepsilon_{\rm eq}$ とする。左、右の粒子位置読出しは、任意軸射影重み $p_+,p_-$ から各成分で高々 $\eta_W+\varepsilon_{\rm eq}$ ずれた2値分布を持つ。有限の分析器、傾斜切替、固定、局所記録、境界無反応を加えた結果分布 $p^{\rm obs}$ は、無反応質量を零とした理想分布 $p^{\rm id}$ に対して

```math
D_{\rm TV}
\left(
p^{\rm obs},p^{\rm id}
\right)
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm eq}
+
\varepsilon_{\rm lock}
+
\varepsilon_{\rm res}
+
\varepsilon_{\rm guard}
+
\varepsilon_{\rm rec}
```

を満たす。

有限障壁で $\eta_W$ は一般に零でない。従って生の左右位置読出しを有限パラメータで厳密な射影測定とは呼ばない。深いW型族で $\eta_W\to0$ となる場合に、任意精度極限を持つ非鋭い測定として扱う。

## 枝別条件付きGibbs整合

測定記録を $R\in\{L,R,\varnothing\}$ とする。安全枝 $s\in\{L,R\}$ の非規格化共分散を

```math
\widetilde C_s
=
\frac{
\mathbb E
\left[
\mathbf1_{R=s}ZZ^\dagger
\right]
}{
\mathbb E[Z^\dagger Z]
}
```

とする。$p_s=\operatorname{tr}\widetilde C_s>0$ なら条件付き共分散は

```math
C_s
=
\frac{\widetilde C_s}{p_s}
```

である。理想測定操作が必要とする枝別条件は

```math
\widetilde C_s^{\rm out}
\simeq
p_s|s\rangle\langle s|,
\qquad
C_s^{\rm out}
\simeq
|s\rangle\langle s|
```

である。

入力の大域共分散が階数1であることは、この枝別条件を意味しない。結果で条件付けるだけでは、同じ $C_Z$ を2つの異なる射影へ変えられない。測定操作には、粒子位置と信号bathを結果依存に相関させる物理段階が必要である。本章では、井戸ごとに置いた局所記録、準備済みテンプレートの正準交換、交換後方向に対するR161の再平衡化をこの段階として使う。

## 粒子位置の局所記録

左右井戸の内部に滑らかな検出関数 $\chi_L(X)$、$\chi_R(X)$ を置く。安全な左領域では $(\chi_L,\chi_R)=(1,0)$、安全な右領域では $(0,1)$ とし、分離面近傍を無反応領域とする。2つの記録セルを $(Q_s^R,P_s^R)$ とし、記録Hamiltonianを

```math
H_{\rm rec}(t)
=
g_{\rm rec}(t)
\sum_{s=L,R}
P_s^R\chi_s(X)
```

とする。単位面積パルスでは

```math
Q_s^R
\longmapsto
Q_s^R+\chi_s(X).
```

理想空セルで $P_s^R=0$ なら、記録中の $X$ への反作用は零である。有限準備幅は $\varepsilon_{\rm rec}$ に入れる。$\chi_s$ は各井戸の局所位置だけを読むため、記録装置は統計振幅、共分散、全密度、確率流を参照しない。

傾斜保持時間 $T_{\rm rec}$ は、局所ポインターが安全域を分離できる長さとする。R140により保持中の信号bath左右占有変化を $\varepsilon_{\rm lock}$ に抑える。R162により、再平衡化終了後の入射停止と辺ゲート閉鎖から、単一試行の経路滞在失敗を $\varepsilon_{\rm res}$ に抑える。分離面を通過中の試行、ゲート閉鎖失敗、有限閾値帯は無反応として記録し、除外後の2値再規格化を行わない。

## 結果枝ごとの状態更新と再平衡化

左右井戸に、規格化共分散がそれぞれ

```math
C_L^{\rm tpl}
=
|L\rangle\langle L|,
\qquad
C_R^{\rm tpl}
=
|R\rangle\langle R|
```

となる2モードテンプレートを準備する。安全枝 $s$ では、$\chi_s(X)$ が開く局所交換結合により、信号浴 $Z$ と対応テンプレート $Z_s^{\rm tpl}$ を角 $\pi/2$ だけ正準回転する。測定前の $Z$ は使用済みテンプレートへ移り、写像全体は1対1のままである。

交換後の装置座標では $C_s^{\rm out}=|s\rangle\langle s|$ である。測定前の論理座標へ戻して表すと

```math
A_{\boldsymbol n}^\dagger
C_s^{\rm out}
A_{\boldsymbol n}
=
\Pi_{\boldsymbol n,s}
```

となる。R162の辺閉鎖条件の下で、粒子位置 $X$ は記録終了まで同じ安全井戸へ保持される。記録後に辺を開き、交換後テンプレート方向を固定してR161を時間 $T_{X,\rm post}$ だけ作用させる。これにより条件付き出力配置は $\pi^\delta(s)$ へ戻り、枝別配置--信号bath整合誤差は有限混合誤差、正則化誤差、有限障壁の反対井戸裾 $\eta_W$ の和で評価できる。

## R143：R170のM47特殊化と状態更新

1回の作用殻準備、有限熱化、辺閉鎖、局所記録に対する共通誤差は第2章R170の $\varepsilon_{170}$ を使う。M47固有のW型コントラスト、2モード制御、傾斜固定、結果別テンプレート交換だけをR143へ追加する。同じ容量、混合、衝突、記録偏差をR143で展開し直さない。

<!-- theorem-start:theorem -->
**定理（R143：M47有限コントラスト読出しと結果別状態更新）**

固定した入力純粋共分散、測定軸 $\boldsymbol n$、有限観測時間について、次を仮定する。

1. R181AのW型2モード特殊化で信号bath方向を有限誤差 $\varepsilon_{\rm Hopf}$ 以内に準備し、初期操作面でR170を誤差 $\varepsilon_{170}^{\rm in}$ 以内に実行できる。
2. 衝突熱浴を切った後、R140の傾斜列を2モード制御誤差 $\varepsilon_{\rm ctrl}$ 以下で実装し、終了方向に対してR170を誤差 $\varepsilon_{170}^{\rm out}$ 以内に実行できる。
3. R140の尺度階層により信号bath左右占有の変化を $\varepsilon_{\rm lock}$ 以下にでき、R162の入射停止と辺ゲート閉鎖により、記録終了前に粒子位置 $X$ が安全井戸を離れる確率を $\varepsilon_{\rm res}$ 以下にできる。
4. 安全枝で局所記録と結果別テンプレート交換を実行し、枝別交換誤差を $\varepsilon_{\rm br}$ 以下、交換後の条件付き再平衡化誤差を $\varepsilon_{\rm post}$ 以下にできる。
5. 分離面、閾値平滑化帯、セルoverflowを正式な無反応結果とし、その全質量を $\varepsilon_{\rm guard}$ 以下にできる。

このとき結果集合 $\{+1,-1,\varnothing\}$ を持つ、有限正準制御と有限セル弱開放粒子位置bathからなる装置を構成でき、無反応質量を零とした理想Born分布との全変動距離は

```math
\varepsilon_{\rm inst}
\leq
\eta_W
+
\varepsilon_{\rm ctrl}
+
\varepsilon_{2m}
+
\varepsilon_{\rm Hopf}
+
\varepsilon_{170}^{\rm in}
+
\varepsilon_{170}^{\rm out}
+
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
```

で抑えられる。安全結果 $s$ の条件付き出力共分散は、分析器座標で $|s\rangle\langle s|$ からtrace距離 $\varepsilon_{\rm br}+O(\eta_W)$ 以内であり、条件付き出力配置は $\pi^\delta(s)$ から $\varepsilon_{\rm post}$ 以内である。記録は粒子位置 $X$ の局所関数だけを入力にし、全密度、確率流、current transducerを使わない。
<!-- theorem-end:theorem -->

R143の共通instrument部分はR170に尽くされる。R143が追加するのはM47のW型分析器、有限コントラスト、傾斜固定、結果別テンプレート交換、条件付き状態更新である。旧連続matching保存は仮定しない。一方、作用容量結合とfiber内平衡化を含む最小Hamiltonian、信号bath保持controllerの完全な反作用、Hopf準備からresetまでの総収支はR143から従わない。

## 同軸反復と異軸逐次測定

第1測定軸を $\boldsymbol n$ とし、安全結果 $s$ を得た後、装置座標の出力共分散は $|s\rangle\langle s|$ に近い。同じ軸を再測定する場合は同じ左右基底を読むため、反対結果の確率は理想的には零で、有限装置では条件付き状態誤差と第2段誤差の和で抑えられる。

第2軸を $\boldsymbol m$ とする。第1分析器の出力座標から第2分析器へ進む制御を

```math
A_{\boldsymbol m}
A_{\boldsymbol n}^\dagger
```

とすれば、理想条件付き分布は

```math
P(t\mid s)
=
\operatorname{tr}
\left(
\Pi_{\boldsymbol m,t}
\Pi_{\boldsymbol n,s}
\right)
=
\frac12
\left(
1+st\boldsymbol n\cdot\boldsymbol m
\right).
```

2段の実分布と理想逐次分布の全変動距離は、逐次結合により各段の $\varepsilon_{\rm inst}$ と第1段条件付き状態誤差の和で抑えられる。各段は独立な記録セルとテンプレートを使う。無反応試行は結果空間に残す。

## 永久記録、逆計算、交換reset

外部記録セルは前節の局所剪断で結果を保持する。記録後、分析器時計、傾斜制御器、局所比較器の補助自由度を逆順に戻す。測定前浴情報は使用済みテンプレートにあり、外部記録は逆実行しないため、内部補助だけを戻しても正準可逆性は破れない。

周期末の装置偏差 $\delta a$ を、流入する空セル $\eta_n$ と交換角 $\phi$ で回転すると

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta_n.
```

1周期の逆計算残差を $\varepsilon_{\rm cyc}$、空セル幅を $\|\eta_n\|\leq\sigma_E$ とすれば

```math
\limsup_{n\to\infty}
\|\delta a_n\|
\leq
\frac{
\varepsilon_{\rm cyc}
+
|\sin\phi|\sigma_E
}{
1-|\cos\phi|
}
```

である。旧状態は使用済み外部セルへ移る。永久記録と旧状態を有限閉鎖系の固定容量へ無期限に蓄積するとは主張しない。

## 条件付き完全周期

<!-- theorem-start:theorem -->
**定理（R144：M47傾斜測定の固定有限弱開放周期）**

固定純粋入力、固定された有限個の傾斜制御、固定された2つの測定軸、任意の有限周期数について、R143の5条件が各段と各周期で一様に成立するとする。Hopf方向準備、条件付きGibbs再平衡化、任意軸操作、再平衡化、辺閉鎖、傾斜分離固定、局所記録、枝別テンプレート交換、測定後再平衡化、2段逐次測定、永久記録、内部逆計算、外部fresh-cell交換からなる有限正準・弱開放構成を選べる。無反応を含む結果分布誤差は各段の $\varepsilon_{\rm inst}$ の和、周期末偏差は逆計算とresetの上界で抑えられる。能動装置の自由度は固定有限であり、永久記録、衝突セル、使用済み状態のセル数は周期数に比例する。
<!-- theorem-end:theorem -->

R144は全時刻のmatching保存または周期間matching帰還を仮定しない。各操作面でR164の作用殻準備とR161、R162を有限時間だけ作用させる。一方、Hopf pump、作用殻fiber、信号bath保持controller、衝突セル準備、記録、template交換、resetを含む総仕事、総熱、総エントロピー生成を一つの恒等式へ閉じていない。従ってR144は完全周期の熱力学的閉鎖を与えないが、その閉鎖は再編後の固定目標Q1-2ではなく実装強化課題である。

## 誤差・熱力学・資源台帳

Q1測定の中心誤差を

```math
\varepsilon_{Q1}
=
\varepsilon_{\rm prep}
+
2\varepsilon_{\rm eq}
+
\varepsilon_{2m}
+
\varepsilon_{\rm ctrl}
+
\eta_W
+
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
```

とする。$\varepsilon_{\rm eq}$ はR164の作用殻準備、有限時間混合、正則化、有限衝突セル、信号bath保持を含む。$\varepsilon_{\rm lock}$ は信号bath左右占有の変化、$\varepsilon_{\rm res}$ は辺ゲート閉鎖後の単一試行経路離脱であり、同じ量ではない。状態方向誤差、結果分布の全変動距離、記録ポインター誤差、周期末正準座標偏差は単位が異なるため、付録Bで対応するLipschitz定数を通してから合成する。

準備誤差はさらに

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm phase}
```

と分ける。R181Aは $\varepsilon_{\rm Hopf}$ の信号bath方向部分を有限準備時間で抑える。条件付き作用殻状態数、粒子位置周辺、条件付き粒子位置分布はR164、R161、R162の後段準備・再平衡化へ移し、M54単独の誤差へ入れない。零seedと位相基準の失敗は独立に完全結果集合へ残す。

熱力学台帳では、信号bath方向を変える解析器仕事 $W_{\rm ctrl}$、作用枝容量と作用殻拘束を切り替える殻自由エネルギー仕事 $W_{\rm sh}$、作用殻消去表示の相対有効仕事 $W_{\rm q}^{\rm rel}$、相対有効熱 $Q_X^{\rm rel}$、Hopf pump仕事 $W_{\rm Hopf}$、記録・template交換・reset仕事を分ける。第2章の粗視化経路熱力学系は条件付き中間状態について

```math
\Delta E_X^{\rm rel}
=
W_{\rm q}^{\rm rel}
+
Q_X^{\rm rel}
```

と経路エントロピー生成を与える。$W_i^{\rm rel}=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ であり、全作用保存unitaryでは共通項が一定になり得るが、pumpとresetでは一定とは限らない。この式だけで $W_{\rm sh}$、殻内散逸、controller反作用を含む全微視的仕事・熱を同定しない。周期全体について

```math
\Delta E_{\rm total}
=0
```

となる外部セル込みの収支と、記録情報、使用済みセル、Hopf散逸を含む総エントロピー生成は未閉鎖である。

1段の能動装置は、信号2モード、条件付き作用殻fiber、容量controller、条件付き障壁controller、有限衝突セル、辺ゲート、左右テンプレート、左右記録セル、傾斜制御、時計、粒子位置の局所検出部からなる。固定段数と固定観測時間では有限自由度である。正準対の最小数は評価しない。$K$ 周期の永久記録、衝突履歴、使用済みテンプレート保存は $O(K)$ 以上、固定有限段の制御時間は傾斜パルス数、fiber準備時間、再平衡化時間に比例する。

$\delta\downarrow0$ では有効自由エネルギー幅が $O(\!\log\delta^{-1})$、必要衝突流束が少なくとも $\Omega(\!\delta^{-1/2})$、R161の一般混合率下界は $O(\!\delta)$ まで低下し得る。R164の滑らかな有限幅作用殻を一様精度で保つ剛性には $\Omega(\!\delta^{-2})$ が必要で、$\Theta(\!\delta^{-2})$ は代表的な選択である。有限資源のまま全bath方向の厳密nodeを追跡するとは主張しない。

深いW型極限は測定コントラストと固定誤差を小さくする一方、トンネル分裂 $J$ を小さくする。零傾斜の $x$ 回転時間は $O(\mathcal J_0/J)$ なので、精度を高めるほど任意軸操作が遅くなる可能性がある。この精度--時間交換は資源台帳から除外しない。

## Q1の達成判定とZeno統合課題

本章による現在地は次である。

| 目標 | 現在地 | 根拠 | 残る条件 |
|---|---|---|---|
| Q1-1 | 達成 | R135、R140 | 全W型制御は有限2モード誤差。精度--時間交換を持つ |
| Q1-2 | 部分達成 | R140、R143--R144、R161、R162、R164、R168、R170、R181A、R181D | Born分布、同軸反復分布、異軸逐次分布は導出済み。同一の零傾斜Rabi対照と反復測定を接続し、全履歴・無反応・tilt対照・有限誤差・資源を含む正のZeno抑制余裕を示すことが残る |

旧Q1-4のZeno効果はQ1-2へ統合した。旧M38の有限Zeno結果は、置換済み連続位置模型に依存する歴史的結果としてGit履歴と研究メモへ保存し、M47の現行根拠へ戻さない。M47の傾斜固定は測定保持の一部であり、反復測定間隔に応じたZeno抑制の導出ではない。傾斜でHamiltonianを離調させて遷移を抑える現象をZeno効果と呼ばない。旧Q1-3の完全周期は固定目標から削除し、本章のR144と周期総収支を実装・熱力学的強化として保存する。

再開後の最初の検査では、総時間 $T$ と零傾斜Rabi周波数 $\Omega$ を共通に固定する。測定なし対照の理想目標を

```math
P_{\rm free}(T)
=
\frac{1+\cos(\Omega T)}{2},
```

等間隔に $N$ 回測る理想目標を

```math
P_N(T)
=
\frac{1+\cos^N(\Omega T/N)}{2}
```

と置く。ただし、これらは本版でM47から導出した結果ではなく、有限幅R143/R170測定を反復合成するときの比較目標である。測定中も対象Rabi項を止めず、flip、reflip、無反応を含む全履歴を残す。測定と同じ傾斜操作だけを入れて記録しないtilt対照を必須とし、観測された差を離調固定から分離する。重なり、傾斜、自由発展、1段instrumentの誤差を別々に上界し、有限 $N$ で $P_N-P_{\rm free}$ の正の余裕が合成誤差を上回る場合だけ達成候補とする。反復回数に比例する記録、template、fresh cell、reset、時間、エネルギーも資源台帳へ含める。

## 非主張

本章は次を主張しない。

1. 大域階数1共分散だけから枝別測定後状態が自動的に生じること。
2. 具体的回路または有限bathからM54/R181AのW型2モード系の採用開放方程式を導出したこと。
3. R164の枝容量結合、作用殻fiber内平衡化、枝対称性がW型装置の有限局所Hamiltonianから自動的に発生すること。
4. 有効地形仕事・熱がfiberとcontrollerを含む全微視的仕事・熱に等しいこと。
5. 信号bath保持controllerへの反作用が厳密に零であること。
6. 全時刻の配置--信号bath matching保存。改訂後の周期はこれを必要としない。
7. 有限障壁の左右位置読出しが厳密射影になること。
8. 傾斜切替で高モード漏れが厳密に零になること。
9. 局所記録が統計振幅、共分散、確率流を測っていること。
10. 無反応なしの滑らかな厳密2値写像。
11. 固定容量の閉鎖系による無期限の衝突熱浴、永久記録、reset。
12. Hopf pumpからresetまでの総仕事、総熱、総エントロピー収支。
13. 2準位W型を越える一般Born則。
14. Zenoまたは反Zeno効果。
15. 置換済み連続位置模型の旧結果を現行Q1へ再導入すること。

# 第III部　2論理部分系とBell型統計

# M54のQ2有限次元特殊化

> **位置づけ：** 第2章のR181B--R181Dを2入力・3入力へ特殊化し、同一register上のCNOT、二段gate、末端projector-tree、およびR180 receiverへの分岐を明示する。Q2-1--Q2-3の達成ラベルは変更しない。


## 改訂した設計原則

Q2-1の固定目標は、2量子ビット型結合ゲートと同一の共同入力--出力統計を生成し、積入力を非分離な共同内部状態へ移し得る有限古典Hamiltonian過程を構成することである。M54は、この共同状態を経路だけに担わせる必要はない。4つまたはそれ以上の内部自由度が実在しても、それらが受動的なbath自由度であり、controllerが個別に扱う必要がなければ固定目標と両立する。

改訂後の設計原則は次のとおりである。

1. controllerが指定するのはQ1 port、lift窓、ゲート種、対象port、作用窓、末端読出しだけである。
2. 内部の4モードregister、8個の実正準座標、anti-register、work cell、clock履歴は許す。ただし各内部modeを外部から個別に初期化、較正、同期、address、読出し、resetしてはならない。
3. 一般入力から生じた同じ物理的状態bathを全ゲート間で保持し、中間で枝選択、粒子位置decode、tomography、集団moment推定、再準備をしない。
4. 可逆性に必要なanti-register、入力source、work、clock履歴を捨てない。
5. 排他的なBorn型結果は回路末尾だけでM50/R164/R170へ接続する。無反応も完全結果空間へ含める。

従って問題になるのは内部自由度の個数そのものではなく、外部interfaceが閉じているか、同一試行の状態が永続するか、余計な自由度をbathへ受動的に任せられるかである。旧path-only設計の「4モードregisterを使わず経路だけで担う」という制約は撤回する。

## M54の状態とinterface

2つのQ1入力を

```math
 a=(a_0,a_1)^{\mathsf T},
 \qquad
 b=(b_0,b_1)^{\mathsf T}
 \tag{4.1}
```

とする。lift後の状態bathに4成分の派生複素信号

```math
 Z_S=(Z_{00},Z_{01},Z_{10},Z_{11})^{\mathsf T}
 \in\mathbb C^4
 \tag{4.2}
```

を置く。これは1試行の実正準座標から得る物理的な派生信号であって、M54の解析上の統計量であるray因子 $c$ と規格化第2モーメント

```math
 C_Z=\frac{\mathbb E[zz^\dagger]}{\mathbb E[z^\dagger z]},
 \qquad
 C_Z=cc^\dagger
 \quad(\operatorname{rank}C_Z=1)
 \tag{4.3}
```

ではない。$Z_S$ と $c,C_Z$ は記号も用途も分ける。

可逆liftは同時にanti-register

```math
 G_S=\overline{a\otimes b}
 \tag{4.4}
```

を生成する。全状態を概念上

```math
 \Gamma_{54}^{(2)}
 =(\Gamma_{Q1,A},\Gamma_{Q1,B},Z_S,G_S,W_S,\tau,E_R,H,R)
 \tag{4.5}
```

と書く。これは第2章の完全状態型の $n=2$ 特殊化を用途別に束ねた略記であり、別模型ではない。$W_S$ はsource、work、lift clock、gate clockの可逆履歴を含む。$G_S,W_S$ は出力結果として読まず、逆写像を可能にするbath自由度として保持する。

外部interfaceは

```math
 \mathfrak I_{54}^{(2)}
 =(A,B;\,L_{AB};\,\{(g_r,S_r,t_r)\}_{r=1}^{L};\,M_{\rm end})
 \tag{4.6}
```

だけである。$L_{AB}$ はlift窓、$g_r$ は有限個のゲート種、$S_r$ は対象port集合、$t_r$ は作用窓、$M_{\rm end}$ は末端instrumentである。内部index $00,01,10,11$ をcontrollerの4本の独立命令として公開しない。

## R181B：可逆tensor-lift定理

各組 $(j,k)$ にblankな正準対

```math
 (x_{jk},\pi^x_{jk}),
 \qquad
 (y_{jk},\pi^y_{jk})
 \tag{4.7}
```

を用意し、$s_C=\sqrt{2J_C}$ として

```math
 w^x_{jk}=\frac{x_{jk}+i\pi^x_{jk}}{s_C},
 \qquad
 w^y_{jk}=\frac{y_{jk}+i\pi^y_{jk}}{s_C}
 \tag{4.8}
```

と置く。安全なcompact領域で1となる滑らかなcutoffを暗黙に掛け、lift Hamiltonianを

```math
 H_{\rm mult}
 =\chi(\tau)
 \sum_{j,k}
 \left(
 \pi^x_{jk}F^x_{jk}(a,b)
 +\pi^y_{jk}F^y_{jk}(a,b)
 \right)
 \tag{4.9}
```

とする。単位面積pulseに対して

```math
 F^x_{jk}=\sqrt2s_C\operatorname{Re}(a_jb_k),
 \qquad
 F^y_{jk}=\sqrt2s_C\operatorname{Im}(a_jb_k)
 \tag{4.10}
```

と選ぶ。係数 $\sqrt2$ は式(4.8)と後の正準混合の正規化に必要である。

各 $(j,k)$ で固定実正準行列

```math
 S_0=\frac1{\sqrt2}
 \begin{pmatrix}
 1&0&0&-1\\
 0&1&1&0\\
 1&0&0&1\\
 0&1&-1&0
 \end{pmatrix}
 \tag{4.11}
```

を $(x,\pi^x,y,\pi^y)$ に作用させる。出力の2つの派生複素modeは

```math
 Z_{jk}=a_jb_k,
 \qquad
 G_{jk}=\overline{a_jb_k}.
 \tag{4.12}
```

となる。

<!-- theorem-start:corollary -->
**系（R181Bの2入力特殊化）**

正規化された有限次元Q1入力 $a\in\mathbb C^m$、$b\in\mathbb C^n$ とblank targetを考える。式(4.9)--式(4.11)は安全compact領域上の有限時間Hamiltonian流として

```math
 (a,b,0)
 \longmapsto
 (a,b,Z_S=a\otimes b,G_S=\overline{a\otimes b},W_S)
```

を実現する。source、anti-register、work、clock履歴を保持すれば、$S_0^{-1}$ と逆pulseにより写像全体を反転できる。近似pulse、cutoff、blank誤差に対しては安全compact領域上のLipschitz定数による有限誤差評価を持つ。
<!-- theorem-end:corollary -->

積の非線形性は、式(4.9)がsourceとtargetを含む3次Hamiltonianであることに担わせる。blank manifold上ではtarget momentumが零のためsourceは理想的に動かず、targetだけが平行移動する。これは未知入力の係数をcontrollerが読み取って書き込む操作ではない。

R181Bは固定 $m,n$ に対する定理である。$m=n=2$ および3入力への2段liftには有限の受動modeしか要らない。一般の入力数 $N$ に対するtensor反復の一様性はR181Bから主張せず、Q2-4ではM54のroot-mode入力とR181Cのsector-broadcastを使う。

## R181C：永続状態bathゲート合成定理

lift後は同じ $Z_S$ を計算終了まで保持する。Hermitian行列 $h(t)$ に対して

```math
 H_h(t)=Z_S^\dagger h(t)Z_S,
 \qquad
 iJ_C\dot Z_S=h(t)Z_S
 \tag{4.14}
```

は有限mode上のunitaryを実正準Hamiltonian流として実装する。

Q2-1のCNOTはmode $10,11$ のswapである。差mode projectorを

```math
 \Pi_-^{10,11}
 =\frac12
 (|10\rangle-|11\rangle)
 (\langle10|-\langle11|)
 \tag{4.15}
```

とすれば

```math
 U_{\rm CX}=\exp(-i\pi\Pi_-^{10,11})
 \tag{4.16}
```

である。実正準座標では対応する生成子を

```math
 K_{A\to B}
 =\frac14
 \left[
 (Q_{10}-Q_{11})^2
 +(P_{10}-P_{11})^2
 \right]
 \tag{4.17}
```

と取れる。

3入力ではR181Bを2回使い、ゲート列の前に

```math
 Z_{ABC}=a\otimes b\otimes c
 \tag{4.18}
```

を作る。Q2-3の2つのCNOT生成子は

```math
 \begin{aligned}
 K_{AB}
 &=\frac14\sum_c
 \left[
 (Q_{10c}-Q_{11c})^2
 +(P_{10c}-P_{11c})^2
 \right],\\
 K_{BC}
 &=\frac14\sum_a
 \left[
 (Q_{a10}-Q_{a11})^2
 +(P_{a10}-P_{a11})^2
 \right].
 \end{aligned}
 \tag{4.19}
```

これはsectorごとの外部routingではなく、同じ有限二次形式を全該当modeへ受動的に作用させる1つのgate命令である。

gate clockを含む全Hamiltonianは

```math
 H_{\rm tot}
 =P_\tau+H_{\rm hold}
 +\sum_{r=1}^{L}g_r(\tau)K_r(Z_S)
 \tag{4.20}
```

とする。$g_r$ は互いに交わらないcompactな作用窓を持ち、出口では相互作用が零になる。clock momentumやworkは履歴を保持してよいが、$Z_S$ を交換または再準備しない。
本文式(4.17)、式(4.19)のCNOT窓では $\int g_r(t)dt=\pi$ とする。一般gateではこのpulse面積を対応するHermitian対数に置き換える。

<!-- theorem-start:corollary -->
**系（R181Cの2入力・3入力gate特殊化）**

R181Bで得た有限次元の同一状態bath $Z_S$ に、式(4.20)の有限個の非重複gate窓を作用させる。各理想gateを $U_r$、実装を $\widetilde U_r$ とし、

```math
 \inf_{\chi_r}
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \leq\varepsilon_r
```

とする。このとき任意の有限参照因子に恒等作用を追加しても同じ評価が成立し、

```math
 \inf_\chi
 \|\widetilde U_L\cdots\widetilde U_1
 -e^{i\chi}U_L\cdots U_1\|_{\rm op}
 \leq\sum_{r=1}^{L}\varepsilon_r
```

を得る。CNOT、局所unitary、逆演算、およびQ2-3の2段CNOTは、中間decodeや再準備なしに同じ $Z_S$ 上で合成できる。
<!-- theorem-end:corollary -->

以前の「handoff map」は不要である。同じregisterを保持するため、有限誤差はlift、hold、clock、gate、leakageへ一度ずつ数える。経路展開は式(4.16)、式(4.19)の代数的な診断表示として残せるが、独立のR175や物理的経路分岐器を主結果鎖に置かない。

## R181Dの有限深さprojector-tree特殊化

回路末尾の実際の1試行信号を

```math
 v=Z_{\rm out}(\omega)
 \tag{4.23}
```

とする。これは理想係数の再構成値でも集団共分散でもない。R112の同次元blank hold-registerへのcanonical SWAPで $V$ へ保持し、信号bathを計算registerから切り離す。

各node $u$ の2枝容量を

```math
 J_{u,b}(V)=J_0V^\dagger P_{u,b}V,
 \qquad
 J_\Sigma(V)=J_{u,0}(V)+J_{u,1}(V)
 \tag{4.24}
```

とし、raw容量のlatchと、作用殻へ渡す正則化容量を

```math
 H_{\rm latch}
 =\sum_bP_{u,b}^J J_{u,b}(V),
 \qquad
 A_{u,b}^\delta(V)=J_{u,b}(V)+\delta q_bJ_\Sigma(V)
 \tag{4.25}
```

で定める。blank容量momentumではpointerだけが移動し、理想的な $V$ は動かない。R170がselectorを固定した後、第2章のinvolution filterを作用し、選択rayをradial-only portでrepumpする。2入力は深さ2、3入力は深さ3である。

<!-- theorem-start:corollary -->
**系（R181Dの2入力・3入力計算基底読出し）**

R181Cの末端信号 $v$ が零でなく、canonical SWAP、容量latch、作用殻、有限混合、収集、固定、記録がそれぞれ安全compact領域上で定義されるとする。完全結果空間を

```math
 \Omega_{\rm out}=I_L\sqcup\{\varnothing\}
```

とする。正規化rayの実装誤差が $\varepsilon_{\rm ray}$、深さを $m\in\{2,3\}$、各node誤差を $\bar\varepsilon_k$ とすれば、

```math
 D_{\rm TV}(P_{\rm out},P_{\rm Born})
 \leq
 \varepsilon_{\rm ray}
 +\frac{m\delta}{1+\delta}
 +2m(\tau+\gamma)
 +\sum_{k=1}^m\bar\varepsilon_k.
```

理想的な共通radial因子とglobal phaseは式(4.24)の規格化で消える。
<!-- theorem-end:corollary -->

R181Dは条件付き定理である。R164、R170の既存部品に加え、容量pointer、selector lock、controlled filter、radial repump、記録を同じclockとsafe setで接続する必要がある。成功試行だけの再規格化は行わない。

## Q2-1とQ2-3の識別力

$|+0\rangle$ からCNOTを作用させると

```math
 Z_{\rm Bell}
 =\frac{|00\rangle+|11\rangle}{\sqrt2}.
 \tag{4.28}
```

中間で2枝をdephaseした模型は計算基底周辺を再現できても、逆CNOTとHadamardを通した末端分布を再現しない。coherent出力とdephase出力の全変動距離は

```math
 D_{\rm TV}=\frac12
 \tag{4.29}
```

である。従ってR181Cの逆演算試験は、単なる4結果確率表より強い。

Q2-3では $Z_{ABC}$ に式(4.19)を順に作用させる。R177のGHZ--位相--逆演算試験は、coherent模型と中間枝選択模型の間に

```math
 D_{\rm TV}=\frac1{2\sqrt2}
 \tag{4.30}
```

の識別gapを与える。同じtensor-lift、同じ永続register、同じ二次gate、同じ末端instrumentを使うため、Q2-1、Q2-3は同一機構の有限次元特殊化である。

## R180 setting-pre receiverへの末端interface

Q2-2の固定singlet sourceは、$|00\rangle$ のR181B tensor-lift後にR181Cの

```math
H_A,
\qquad
\operatorname{CX}_{A\to B},
\qquad
X_B,
\qquad
Z_A
```

を順に作用させて作る。理想末端信号は

```math
V_{\rm s}
=
\frac{|01\rangle-|10\rangle}{\sqrt2}.
\tag{4.31}
```

このgate列は設定生成前に終える。実際の末端信号 $v=Z_{\rm out}(\omega)$ をR112のcanonical SWAPで物理hold信号 $\widetilde V=v$ としてそのまま移し、第5章R180へ渡す。canonical SWAPは状態依存除算を含まない。R180では解析上だけ $V=\widetilde V/\|\widetilde V\|$ とし、A設定 $x$ が $\widetilde V$ の直交projector blockを選び、source-driven paired-Hopf receiverを通して2翼の局所M50/R170へ接続する。

このinterfaceはR181Dと役割が異なる。R181Dは末端計算基底分布を直接記録する。R180は同じ試行の4mode信号を記録前に2翼receiverへ渡す。1周期では選んだ一方だけを作動させる。

R180は $G_S$ を末端共役信号として使わない。R181B直後の $G_S=\overline{a\otimes b}$ はR181C後の $\overline{Z_{\rm out}}$ を意味しないからである。入力係数の外部読出し、試行集団momentへの縮約、fresh carrierへの再準備も行わない。

Q2-2がM54を根拠模型として共有しても、Q2-1の達成状態からQ2-2を推論しない。Q2-2はR180A--R180C固有のbranch作用、paired-Hopf、切断後局所性、完全結果誤差から独立に判定する。

## 誤差台帳と現在地

長さ $L$ の回路全体には

```math
 \varepsilon_{\rm circ}
 \leq
 \varepsilon_{\rm lift}
 +\varepsilon_{\rm hold}
 +\varepsilon_{\rm clock}
 +\sum_{r=1}^{L}\varepsilon_r
 +\varepsilon_{\rm leak}
 +\varepsilon_{\rm ray}
 +\frac{m\delta}{1+\delta}
 +2m(\tau+\gamma)
 +\sum_{k=1}^m\bar\varepsilon_k
 \tag{4.32}
```

と整理する。中間handoff、枝pairing、coherent decoderを独立項として二重計上しない。

R181Bは明示的な有限Hamiltonian構成、R181Cは同一有限register上の作用素norm合成を与える。R181Dは既存の末端bath部品へ接続する条件付き評価を与える。Q2-1は条件付き達成を維持し、残る条件は主としてR181Dの物理境界と全末端工程の一体化である。

Q2-3も同じ理由で条件付き達成を維持する。Q2-2は本章の実際の1試行末端信号を第5章のsetting-pre paired-Hopf receiverへ渡す別interfaceを使い、R180Cの単一装置統合を条件として条件付き達成を維持する。Q2-4は同じM54親模型の一般 $n$ 特殊化として、R181A--R181D、R178D、R179を根拠に条件付き達成を維持する。

M37由来のW型入力を接続する研究では、独立な2セルの並置と共同レジスタの構成を区別する。入力信号a,bだけで共同状態を $ab^{\mathsf T}$ と定義する限り積状態のままである。R181Bの写込み後は共同レジスタが独立な4成分を保持する。配置空間上のW型担体を別に置く案も、この共同自由度の物理的起源を追加しており、2台の実空間装置からの導出とは同一でない。この接続を既存Q2目標の必須依存にしない。

# M54駆動setting-pre paired-Hopf receiverとBell前提監査

> **位置づけ：** M54の実際の1試行末端信号をA設定で条件付きblockへ分け、source-driven paired-Hopf流、切断後fresh局所作用殻、2翼M50/R170へ接続する。R180A/Bは代数と採用開放流を閉じ、R180Cは単一装置統合を条件とする。Q2-2の条件付き達成を維持する。


## 目的と模型の境界

本章は、M54の実際の1試行末端信号を2つの物理的測定端へ渡すsetting-pre receiverを定義する。M54でgate列を終えた信号を

```math
v=Z_{\rm out}(\omega)\in\mathbb C^4,
\qquad
v\neq0
```

とし、R112のcanonical SWAPで同次元hold registerへ物理信号をそのまま

```math
\widetilde V=v
```

と保持する。canonical SWAPは同次元正準座標の交換だけを行い、状態依存除算を行わない。解析上の規格化rayを

```math
r=\|\widetilde V\|,
\qquad
V=\frac{\widetilde V}{r}
```

と定義する。$r\geq r_{\min}>0$ をsafe setに含め、零信号またはこの下限を外れる試行は無反応へ送る。$V$ はcontrollerが生成する物理registerではなく、枝容量比と誤差を記述する解析変数である。$\widetilde V$ は集団共分散、交差moment、理想係数の外部再構成値ではない。同じ試行の実正準座標から得る派生信号である。

M54のanti-register $G_S$ はR181B直後には $\overline{a\otimes b}$ だが、R181Cのgate列は一般に $Z_S$ だけを更新する。従って末端で $G_S=\overline{\widetilde V}$ とは仮定せず、本receiverはholdされた $\widetilde V$ だけを物理入力に使う。未知係数をcontrollerが読み出してtemplate表へ書き込むこと、試行集団momentを単一試行へ再注入することも認めない。

固定有限設定族を $\mathcal X,\mathcal Y$ とする。A設定 $x\in\mathcal X$ は中央receiverへ先行入力され、B設定 $y\in\mathcal Y$ は中央切断後にB局所分析器へだけ入る。設定前のM54 source、設定生成角、fresh cell、局所noise seedの共同測度は設定値に依存しないが、receiver準備後の切断面測度は一般に $x$ に依存する。

R180の物理状態を概念上

```math
\Gamma_{180}
=
\left(
\Gamma_{54}^{\rm hold},x,y,
A_+,A_-,S,
z_A,z_B,X_A,X_B,
\gamma_A,\gamma_B,
\tau,H,R
\right)
```

と書く。$A_\pm$ はbranch容量pointer、$S$ は内部枝、$z_A,z_B$ は2翼receiver信号、$X_A,X_B$ はW型有限位置グラフ上の粒子位置、$\gamma_A,\gamma_B$ はfresh局所作用殻と衝突cell、$H$ は使用済みsourceとclockの履歴、$R$ は外部記録である。$S$ は中央で形成される共通原因であり、この段階では外部結果として記録しない。

R180を三つに分ける。

1. R180AはM54信号のsetting-pre条件付きblock抽出、branch作用、Born共同代数を与える。
2. R180Bは選択blockを物理templateとして2翼carrierへ移すsource-driven paired-Hopf吸引を与える。
3. R180Cは中央切断、2翼M50/R170、局所記録、Bell監査、fresh-cell帰還を条件付きで合成する。

## M54の固定singlet sourceと試行順序

Q2-2の固定benchmarkでは、M54の2入力を $|00\rangle$ とし、R181Bのtensor-lift後にR181Cの局所gateとCNOTを

```math
|00\rangle
\xrightarrow{H_A}
\frac{|00\rangle+|10\rangle}{\sqrt2}
\xrightarrow{\operatorname{CX}_{A\to B}}
\frac{|00\rangle+|11\rangle}{\sqrt2}
\xrightarrow{X_B}
\frac{|01\rangle+|10\rangle}{\sqrt2}
\xrightarrow{Z_A}
\frac{|01\rangle-|10\rangle}{\sqrt2}
```

の順に作用させる。従って理想末端信号は

```math
\beta_{\rm s}
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

である。これは設定生成前に作る固定M54信号であり、$x,y$ をgate列へ入力しない。

1周期のclock順序を次とする。

1. M54で $v$ を作り、$\widetilde V=v$ をholdする。
2. 設定生成器から $x,y$ を得る。
3. $x$ を中央basis splitterとbranch latchへ入力する。
4. 選択blockをsource portへ保持し、R180Bを有限時間走らせる。
5. 中央couplerを切り、使用済みM54 sourceとbranch latchを結果形成から隔離する。
6. A、Bの局所分析器を作用させる。$y$ はこの段階でB側だけへ入る。
7. 2翼のR170を走らせ、局所結果または無反応を記録する。
8. 外部記録を残し、能動部をfresh cellへ交換する。

R181Dの直接計算基底instrumentとR180はM54の別々の末端interfaceである。同じ試行で両方を作動させず、Q2-1・Q2-3の判定は変更しない。

## R180A：setting-pre条件付きblock抽出

行優先規約で、物理hold信号と解析上の規格化rayを

```math
\widetilde V=\operatorname{vec}_{\rm row}(\widetilde D),
\qquad
V=\operatorname{vec}_{\rm row}(D),
\qquad
D=\frac{\widetilde D}{r},
\qquad
\|V\|=1
```

とする。A設定 $x$ の正規直交固有basisを

```math
U_x
=
\left(
u_{+,x},u_{-,x}
\right)
```

とする。物理hold信号 $\widetilde V$ へ有限4mode unitary $U_x^\dagger\otimes I_2$ を作用させる。枝 $s\in\{+1,-1\}$ の物理的なB側2成分blockと、その解析上の規格化表示は

```math
\widetilde w_{s,x}
=
\widetilde D^{\mathsf T}\overline{u_{s,x}}
=
r w_{s,x}(V),
\qquad
w_{s,x}(V)
=
D^{\mathsf T}\overline{u_{s,x}}
```

となる。直交projectorとbranch作用を

```math
\Pi_s^x
=
|u_{s,x}\rangle\langle u_{s,x}|\otimes I_2,
\qquad
p_{s|x}(V)
=
V^\dagger\Pi_s^xV
=
\|w_{s,x}(V)\|^2
```

と定める。物理容量は $\widetilde w_{s,x}$ からlatchし、確率比だけを規格化ray $V$ で表す。$\Pi_+^x+\Pi_-^x=I_4$ なので

```math
p_{+|x}(V)+p_{-|x}(V)=1.
```

安全枝 $p_{s|x}>0$ ではreceiver方向を

```math
a_{s,x}=u_{s,x},
\qquad
b_{s,x}(V)
=
\frac{w_{s,x}(V)}{\sqrt{p_{s|x}(V)}}
```

と書く。式は方向を表すための解析表示であり、controllerが $w_{s,x}$ を数値読出しして除算する操作ではない。物理receiverでは選択された未規格化block $\widetilde w_{s,x}$ をsource portへ渡し、R180Bのpumpが動径を整える。

<!-- theorem-start:theorem -->
**定理（R180A：M54末端信号のsetting-pre条件付きblock抽出定理）**

零でないM54末端信号をcanonical SWAPで $\widetilde V=v$ とholdし、解析上だけ $V=\widetilde V/\|\widetilde V\|$ とする。A設定 $x$ に応じた $U_x^\dagger\otimes I_2$、R181Dの直交projector作用latch、R164の2枝作用殻、R161/R162の有限再平衡化を順に作用させる。R181Dがlatchする物理branch容量を

```math
J_s(\widetilde V,x)
=
\mathcal J_0
\widetilde V^\dagger\Pi_s^x\widetilde V
=
\mathcal J_0r^2p_{s|x}(V)
```

とする。すると共通radial因子は全容量による規格化で消え、理想内部枝は

```math
P(S=s\mid \widetilde V,x)
=
\frac{J_s}{J_++J_-}
=
p_{s|x}(V)
```

を持つ。安全枝でA方向 $a_{s,x}$、B方向 $b_{s,x}(V)$ を2翼局所instrumentへ渡すと、任意のB設定basis $u_{b,y}$ について

```math
P(S=s,B=b\mid V,x,y)
=
\left|
\left(
u_{s,x}^\dagger\otimes u_{b,y}^\dagger
\right)V
\right|^2.
```

B側の規格化縮約行列は

```math
\rho_B(V)=D^{\mathsf T}\overline D
```

であり、

```math
\sum_s
w_{s,x}(V)w_{s,x}(V)^\dagger
=
\rho_B(V)
```

だからB周辺は $x$ に依存しない。代数部分は厳密である。有限装置ではhold、basis splitter、projector latch、作用殻、混合、衝突、block保持の誤差と無反応を完全結果集合上で加える。
<!-- theorem-end:theorem -->

R180AはR181Dの一般projector latchを特殊化して使い、同じ機構を独立に再証明しない。$S$ はA結果の前駆体だが、外部結果は中央で直接記録せず、切断後のA局所R170が一意な記録を作る。

## node切断とsinglet特殊化

一般の $V$ では $p_{s|x}$ が零または小さくなり得る。固定 $0<\tau<1/2$ に対し

```math
G_\tau(V,x,s)
=
\left\{
p_{s|x}(V)\geq\tau
\right\}
```

を安全事象とする。選択された枝が $G_\tau^c$ なら結果を無反応へ送り、成功試行だけを再規格化しない。二枝について切断質量は

```math
\sum_{s:p_{s|x}<\tau}p_{s|x}
\leq2\tau
```

である。$\|w\|\geq\sqrt\tau$ の安全域では $w\mapsto w/\|w\|$ のLipschitz定数を $C_\tau=O(\!\left(\tau^{-1/2}\right))$ で抑えられる。

singletでは係数行列を

```math
D_{\rm s}
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
=
\frac{\mathsf E}{\sqrt2}
```

と書ける。このとき

```math
w_{s,x}
=
-\frac1{\sqrt2}
\mathsf E\overline{u_{s,x}},
\qquad
p_{s|x}=\frac12,
\qquad
b_{s,x}
=
-\mathsf E\overline{u_{s,x}}.
```

最後のglobal signは局所rayと作用に影響しない。従って旧M48の等重みspin-flip fiberはR180Aのsinglet特殊化として回復される。$\tau<1/2$ ならsinglet枝にnode無反応はない。

## 2翼の局所matching

各翼のW型2モード埋込みを

```math
\Phi:
\mathbb C^2
\longrightarrow
\mathbb C^{|\Omega_W|},
\qquad
\Phi^\dagger\Phi=I_2
```

とする。単一試行の局所信号 $z\neq0$ に対して

```math
q_i(z)
=
\frac{|(\Phi z)_i|^2}{z^\dagger z},
\qquad
\pi_i^\delta(z)
=
\frac{q_i(z)+\delta r_i}{1+\delta},
\qquad
r_i>0,
\quad
\sum_ir_i=1
```

を置く。R164が作用殻状態数、R161が平方根型詳細釣合い率と有限混合、R162が固定信号に対する有限衝突近似を与える。ここで入力するのは各試行の $z_A,z_B$ であり、$V$ の集団平均ではない。

規格化方向 $c$ の強い局所fiber $\mathcal F_W^\delta(c)$ を

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)=\pi_i^\delta(z)
```

を満たす共同測度の族とする。R180の理想切断面fiberを

```math
\nu_{V,x}^0
=
\sum_{s=\pm1}
p_{s|x}(V)
\mathcal F_W^0(a_{s,x})
\mathbin{\widehat\otimes}
\mathcal F_W^0(b_{s,x}(V))
```

とする。$\widehat\otimes$ は枝 $s$ とpaired位相を共有し、局所粒子位置noiseは条件付き独立であることを表す。

連続bath座標は有限時間に目標rayへ厳密到達しないため、切断面の連続部分を全変動距離で比較しない。動径誤差、2翼の射影方向誤差、paired位相、枝不一致、離散粒子位置不一致を合わせた有界costのWasserstein距離 $d_{\rm fib}$ を使う。結果分布へ移すときだけ、固定有限設定族のcompact安全域上のLipschitz定数 $L_{\rm fib}$ を掛けて全変動誤差へ変換する。

## R180B：source-driven paired-Hopf吸引

安全枝のtemplateを $a=a_{s,x}$、$b=b_{s,x}(V)$ と固定する。標準source loadでは、branch pointerで既知のA templateを選び、選択された未規格化M54 blockをB portへそのまま注入して

```math
z_A(0)=a,
\qquad
z_B(0)=w_{s,x}=\sqrt{p_{s|x}}\,b
```

とする。従って $p_A(0)=p_B(0)=0$ かつ

```math
m_0
=
\frac{1+\sqrt{p_{s|x}}}{2}>0,
\qquad
d_0
=
\frac{1-\sqrt{p_{s|x}}}{2}.
```

安全域 $p_{s|x}\geq\tau$ では $m_0\geq(1+\sqrt\tau)/2$ であり、吸引定理の非零条件は自動的に満たされる。この表示はB template係数の外部読出しを要求せず、物理port上のblock方向を解析的に $b$ と呼んでいるだけである。

一般の有限入口偏差も含め、receiver信号を

```math
z_A=c_Aa+p_A,
\qquad
z_B=c_Bb+p_B,
\qquad
a^\dagger p_A=b^\dagger p_B=0
```

と分け、

```math
m=\frac{c_A+\overline{c_B}}2,
\qquad
d=\frac{c_A-\overline{c_B}}2
```

と置く。逆表示は

```math
z_A=(m+d)a+p_A,
\qquad
z_B=(\overline m-\overline d)b+p_B
```

である。準備有効時間 $T_{\rm PH}$ に対し、決定論的開放流を

```math
\dot m
=
g(1-|m|^2)m,
\qquad
\dot d
=
-\kappa_{\rm p}d,
```

```math
\dot p_A
=
-\kappa_\perp p_A,
\qquad
\dot p_B
=
-\kappa_\perp p_B
```

とする。

<!-- theorem-start:theorem -->
**定理（R180B：M54 source-driven paired-Hopf receiver吸引定理）**

$m_0\neq0$、$a,b$ が準備窓中に保持され、初期状態が有界安全集合にあるとする。上の採用開放流では $\alpha=\arg m_0$ が保存され、

```math
|m(T_{\rm PH})|^2
=
\frac1{
1+
\left(
|m_0|^{-2}-1
\right)e^{-2gT_{\rm PH}}
},
```

```math
d(T_{\rm PH})
=
e^{-\kappa_{\rm p}T_{\rm PH}}d_0,
\qquad
p_{A,B}(T_{\rm PH})
=
e^{-\kappa_\perp T_{\rm PH}}p_{A,B}(0).
```

従って有限定数 $K_{180}<\infty$ と

```math
\gamma_{180}
=
\min
\left\{
2g,\kappa_{\rm p},\kappa_\perp
\right\}
```

を選び、

```math
\left\|
z_A-e^{i\alpha}a
\right\|
+
\left\|
z_B-e^{-i\alpha}b
\right\|
\leq
K_{180}e^{-\gamma_{180}T_{\rm PH}}
```

とできる。これは採用した開放方程式後の厳密結果であり、pump、sink、template holdを含む有限閉鎖Hamiltonianへの持ち上げを主張しない。
<!-- theorem-end:theorem -->

作用様量

```math
N_{\rm rec}
=
|m|^2+|d|^2+
\|p_A\|^2+
\|p_B\|^2
```

は

```math
\dot N_{\rm rec}
=
2g(1-|m|^2)|m|^2
-2\kappa_{\rm p}|d|^2
-2\kappa_\perp
\left(
\|p_A\|^2+
\|p_B\|^2
\right)
```

を満たす。第1項はbright pumpと飽和、第2項はpaired phase外成分のsink、第3項はtemplate直交成分のsinkである。選択block source、pump、sink、clockの総仕事・総熱・総エントロピー収支は閉じていない。

## 中央切断と局所instrument

R180B終了後の完全共通原因を

```math
\Lambda
=
\left(
V,x,S,\alpha,
z_A,z_B,X_A,X_B,H
\right)
```

とする。中央coupler、M54 hold、branch latchを切り離し、切断後生成子を

```math
\mathcal L_{\rm post}^{xy}
=
\mathcal L_A^x
+
\mathcal L_B^y
```

とする。各翼には中央branch作用殻と異なるfresh局所2枝作用殻を置く。完全共通原因に条件付けて

```math
\mu_{\rm sh}^{AB}
\left(
d\gamma_A,d\gamma_B
\mid
\Lambda,x,y
\right)
=
\mu_{{\rm sh},A}^x
\left(
d\gamma_A
\mid
\Lambda
\right)
\otimes
\mu_{{\rm sh},B}^y
\left(
d\gamma_B
\mid
\Lambda
\right)
```

とする。有限偏差を $\varepsilon_{\rm prod}$ として誤差台帳へ残す。

A分析器は $a_{s,x}=u_{s,x}$ を結果 $A=s$ の安全井戸へ写す。B分析器は $b_{s,x}(V)$ をbasis $u_{b,y}$ で分析する。分析器終了後に各局所信号を固定し、R161/R162の局所粒子位置bathとR170の収集、固定、記録を走らせる。切断後のA核は $y$、B核は反対翼の結果形成変数を参照しない。

## 理想共同分布と非信号性

理想fiberでは $A=s$ であり、

```math
P(B=b\mid S=s,V,x,y)
=
\left|
u_{b,y}^\dagger b_{s,x}(V)
\right|^2.
```

R180Aから

```math
P(A=a,B=b\mid V,x,y)
=
\left|
\left(
u_{a,x}^\dagger
\otimes
u_{b,y}^\dagger
\right)V
\right|^2.
```

A周辺は $y$ に依存せず、B周辺は $\rho_B(V)=D^{\mathsf T}\overline D$ に対する局所Born重みであり $x$ に依存しない。非信号性はsinglet対称性だけでなく、任意の規格化M54純粋信号について成立する。

singletでは

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right),
```

```math
E(A\mid x,y)
=
E(B\mid x,y)
=
0,
\qquad
E(AB\mid x,y)
=
-\boldsymbol n_x\cdot\boldsymbol n_y.
```

平面標準設定ではCHSH絶対値は $2\sqrt2$ である。

## 前向き誤差とR180C

理想規格化末端rayを $V_*$ とし、R181B/R181C、canonical SWAP、holdの有限誤差を規格化後に一度だけ

```math
\varepsilon_{\rm ray}^{54}
=
\inf_\phi
\left\|
\frac{\widetilde V}{\|\widetilde V\|}
-e^{i\phi}V_*
\right\|_2
```

へまとめる。規格化写像のLipschitz評価は $r\geq r_{\min}$ のsafe set上だけで使い、その外は無反応に含める。1設定対の完全結果分布に対する前向き誤差を

```math
\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{\rm ray}^{54}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{\rm latch}
+2\tau\\
&+
C_\tau\varepsilon_{\rm block}
+L_{\rm fib}K_{180}
e^{-\gamma_{180}T_{\rm PH}}
+\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}\\
&+
\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{170,{\rm rest}}^{A}
+\varepsilon_{170,{\rm rest}}^{B}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
\end{aligned}
```

とする。$\varepsilon_{\rm ray}^{54}$ はR181B/R181Cのlift・gateとSWAP・holdが規格化rayへ与える誤差であり、状態依存除算を物理操作として数えない。radial偏差は $J_++J_-=\mathcal J_0\|\widetilde V\|^2$ を通じて必要な作用殻容量と混合時間を変えるが、枝容量比へは入らない。$\varepsilon_{\rm latch}$ は中央projector容量、作用殻、有限混合、衝突、内部枝固定、$\varepsilon_{\rm block}$ は選択block保持とtemplate portを表す。$\varepsilon_{170,{\rm rest}}^{A,B}$ は局所R170のうち、直前に明示した正則化、有限混合と、後ろに明示する記録・clockを除く作用殻、衝突、収集、固定の残差である。同じ有限段の誤差を二重に数えない。固定singletでは $p_s=1/2$ なので $\tau<1/2$ を選び、$2\tau$ のnode項を零にする。

<!-- theorem-start:theorem -->
**定理（R180C：M54駆動2端receiver合成、有限誤差、局所性監査、帰還）**

R180AのM54 signal hold、projector latch、branch作用殻、選択block port、R180Bのtemplate hold、pump、sink、2翼carrier、中央切断、および2つの局所R170が共通safe setと1つの有限clock schedule上で上式の各誤差以内に実行できるとする。完全結果集合を

```math
\Omega_{AB}
=
\left(
\{+1,-1\}\times\{+1,-1\}
\right)
\sqcup
\{\varnothing\}
```

とする。このとき実際の完全結果分布とR180Aの理想共同Born分布の全変動距離は $\varepsilon_{180}^{\rm cyc}$ 以下である。一側周辺の反対設定による差は高々 $2\varepsilon_{180}^{\rm cyc}$ である。singlet標準設定では

```math
\left|
|S_{180}|-2\sqrt2
\right|
\leq
8\varepsilon_{180}^{\rm cyc}.
```

従って

```math
\varepsilon_{180}^{\rm cyc}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。周期末に $r_{\rm ret}<1$ のfresh-cell交換を行えば、外部記録を保ったまま能動receiverを次周期入口の近傍へ戻せる。
<!-- theorem-end:theorem -->

R180Cは条件付き定理である。特に、M54 holdからprojector latchまでの反作用、branch pointerから未規格化block source portへの物理的routing、template portとpaired-Hopf pump・sinkの両立、中央切断後のfresh局所作用殻の積因子化、全窓を共有する単一clockは未統合である。有限閉鎖Hamiltonian liftはQ2-2の固定条件にしないが、上の開放装置境界を満たしたとはまだ主張しない。

## Bell前提監査

| 監査項目 | R180 receiverでの位置 |
|---|---|
| 設定前測度 | M54 source、設定生成角、fresh cell、noise seedの基準測度は $x,y$ に依存しない |
| 設定の中央入力 | A設定 $x$ はR180Aのbasis splitter、projector latch、R180B template選択へ入る |
| 測定開始面 | 一般に $\mu_{\rm cut}(d\Lambda\mid V,x,y)=\mu_{V,x}(d\Lambda)$ であり、$x$ に依存する |
| B設定 | $y$ は中央準備へ入らず、切断後のB局所分析器へだけ入る |
| 切断後局所性 | 完全共通原因 $\Lambda$ に条件付けてA、Bの生成子、作用殻、noise、記録核を因子化する |
| 非信号性 | R180Aのprojector完全性から理想周辺は反対設定に依存しない。有限差は $2\varepsilon_{180}^{\rm cyc}$ 以下 |
| 結果の一意性 | 初期粒子位置と局所jump clock列を完全状態へ含めれば、局所記録は各試行で一意 |
| 無反応 | node、safe set外、overflow、有限混合・固定失敗を $\varnothing$ に残し、成功試行だけを再規格化しない |
| Bell前提 | 成立しない前提は測定設定独立性である。標準的な空間分離・自由設定Bell実験ではない |

共通原因を平均した共同分布から

```math
-\Theta
\log
P(A=a,B=b\mid x,y)
```

を作り、切断後の物理的な大域ポテンシャルとして局所率へ戻してはならない。反対翼設定の再注入となり、R180Cの条件付き局所因子化を壊す。

## 開放模型の局所帳簿

| 項目 | 明示する内容と限界 |
|---|---|
| M54 source | R181B/R181Cの有限Hamiltonian liftとgate列、実際の末端信号 $\widetilde V$、同次元holdを使う。canonical SWAPに規格化を含めず、末端anti-registerを共役信号に使わない |
| branch形成 | $U_x^\dagger\otimes I_2$、R181Dのprojector作用容量latch、R164の容量比に対する作用殻状態数、有限再平衡化を使う |
| paired-Hopf | bright pump、paired差mode sink、template直交sinkの採用開放方程式を明示する |
| 局所測定 | 切断後に2つのR170を使い、fresh作用殻、有限衝突bath、固定、局所記録を分離する |
| 仕事と熱 | R180Bの $N_{\rm rec}$ 収支は示すが、source、controller、pump、sink、切断器、記録、fresh交換を含む総収支は閉じない |
| 環境消去 | paired-Hopf driftとMarkov型局所粒子位置bathの有限閉鎖環境からの導出は行わない |
| 試行の数え方 | 無反応を完全結果へ含め、設定対ごとの全試行を分母とする |
| 反証条件 | block Born恒等式、B周辺独立性、paired吸引、切断後因子化、完全結果誤差のいずれかが破れれば対応するR180結果は成立しない |

## 弱開放帰還

能動receiver状態を $Y_n$、次周期のfresh基準状態を $Y_*$ とする。記録後に使用済みhold、branch latch、pump、sink、局所作用殻、衝突cellをspent側へ移し、fresh cellとの交換核がある距離 $d_{\rm ret}$ について

```math
E
\left[
d_{\rm ret}(Y_{n+1},Y_*)
\mid
Y_n
\right]
\leq
r_{\rm ret}
d_{\rm ret}(Y_n,Y_*),
\qquad
0\leq r_{\rm ret}<1
```

を満たすとする。この交換は使用済みcellを履歴なしに初期化する操作ではない。有限runでは必要数を初期bankへ積み、無期限runではcold inflowとspent outflowを仮定する。帰還誤差は次周期入口へ渡し、既に記録した同じ周期の分布へ遡って加えない。

## 有限時間と資源

固定2入力、固定有限設定族について必要な能動信号mode数は定数である。外部controllerが扱うのは、M54 lift・gate列、設定値、basis splitter種、branch窓、paired-Hopf窓、切断、2つの局所分析器、記録窓だけであり、$\widetilde V$ の4係数、$r$、または $\widetilde w_s$ の2係数を個別に読み出さない。

精度を上げると、M54 gate時間、hold品質、projector latch精度、作用殻容量、mixing時間、衝突cell数、paired-Hopf時間、W型粒子位置混合時間、fresh bank容量が増える。一般状態で $\tau\downarrow0$ とするとnode質量は減るが $C_\tau$ が発散する。固定singletでは $p_s=1/2$ なので、この交換をQ2-2のCHSH benchmarkへ持ち込む必要はない。

## Q2-2判定と非主張

M54、setting-pre paired-Hopf receiver、M50と、R112、R161、R162、R164、R170、R181A--R181D、R180A--R180Cにより、固定singlet、固定有限設定族、準備先行、非空間分離、プロトコル面matching、無反応込み、採用開放法則、弱開放帰還という範囲で固定目標Q2-2を条件付き達成とする。

Q2-2の固定目標文言と独立判定規則は変更しない。現行の根拠構成がM54を共有するのであって、「Q2-1が達成ならQ2-2も達成」と推論しない。Q2-2はR180固有の条件と完全結果誤差から判定する。

本章は次を主張しない。

1. R180Cの全interfaceを1つの具体的開放装置または有限閉鎖Hamiltonianで統合したこと。
2. 準備終了後にA設定を自由に変更できること。
3. 標準的な空間分離・自由設定Bell実験を再現したこと。
4. 一般混合状態を単一試行信号と同一視したこと。
5. 任意のM54一般状態についてnodeなし・一様資源の完全2端装置を得たこと。
6. M54のanti-registerを末端共役信号として利用できること。
7. 総仕事、総熱、総エントロピー生成、無期限resetを閉じたこと。
8. Q2-3、M54/Q2-4、またはQ1--Q3のM0統合を同時に達成したこと。

# 第IV部　空間担体と粒子位置

# M37空間担体とM42局在トークン

> **位置づけ：** M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似をR86へ保ち、その下流に単一試行の局在粒子トークンM42を置く。M54準備、M37担体、R172--R174の等変輸送、有限衝突bath、終位置記録を二層模型として接続する。


## Q3の二層基本模型とM37の範囲

Q3の単一試行系は、M37担体層とM42粒子層を区別する。

| 層 | 単一試行で物理的に存在するもの | 派生表示・集団記述 | 役割 |
|---|---|---|---|
| M37担体 | 有限個の実振動子座標 $(q_i,p_i)$ と局所ばね結合 | 局所複素包絡 $b_i$、統計ray、規格化第2モーメント | R86の有限時間Schrödinger型担体 |
| M42粒子 | 1個の局在位置 $X_t$、局所辺bath、clock、履歴、記録 | 位置分布 $P(X_t=i)$ | R172--R174の局所輸送と終位置記録 |

複素包絡は実振動子状態の派生座標であり、複素rayと位置分布は多数試行の統計である。一方、$X_t$ は各試行に1つ存在する粒子位置である。M37だけから粒子位置や最小率が必然的に出るとは主張せず、M42の局所率、bath cell、更新則を追加の採用ミクロ法則として明示する。

共通M54/R181Aは、M37へ入れる前の実正準seed集団を開放driftでrank-one rayへ準備する。準備後の同じ単一試行信号にM50/R164の作用殻選択を一度だけ適用してM42の初期位置 $X_0$ を作る。その後はM37とM42を同時に進め、終時刻には新しい位置を再標本化せず、既存の $X_T$ をR112の局所記録回路で読む。このためM54、初期R164選択、終位置記録を独立なBorn型確率源として数えない。

ミクロ振動子層から有効担体への移行はQ3-1の固定達成基準であり、R86が満たす。M42は粒子実体と下流現象を追加する強化であって、Q3-1の判定へ遡及的に要求しない。M54のport、M37局所ばね網、初期作用殻、M42衝突bath、記録を同じ有限局所装置へ統合したとも扱わない。

Q1はM47のW型2モード、Q2-2はM54駆動R180 paired-Hopf receiver、固定時刻の一般枝instrumentはM50/R170を使う。M42はQ3の空間セルだけに採用する。任意の装置用正準混合がM37の局所ばね網だけで実装できるとは仮定しない。静的R86がM47へ供給するのは対称W型生成子、最低2固有モード、スペクトル間隔である。第6.17節と付録E.12では有限制御列への誤差接続を追加し、第3.5.1節の条件付き系へ渡す。

振動子の個数を $L<\infty$、共通質量を $M_{\rm osc}>0$、搬送周波数を $\omega_0>0$ とする。$M_{\rm osc}$ はミクロ振動子の質量であり、第6.6節に現れる有効質量 $m$ と区別する。固定作用尺度 $\mathcal J_0>0$ は正準座標の規格化に使う。

有限次元 Schrödinger 方程式を古典正準座標または結合振動子へ写すこと自体は既知である [34--37]。特に、位置結合だけを用いる弱結合近似と、位置・運動量の両結合を用いる厳密写像は先行研究で区別されている [35--37]。

本稿は次を新規性として主張しない。

1. 複素ベクトルを2倍次元の実ベクトルで表すこと。
2. 任意の Hermitian 行列を設計済み2次 Hamiltonian へ埋め込むこと。
3. 結合振動子が Schrödinger 型運動を近似できること。

本稿で追加するのは、局所位置結合網について反回転項を落とさない厳密式、正常モード生成子との作用素誤差、有限時間状態誤差、局所包絡誤差から有限基底測定分布への伝播を同じ誤差台帳で接続することである。

## ミクロHamiltonian

実正準対を

```math
\left\{q_i,p_j\right\}
=
\delta_{ij}
```

とし、時間非依存な有限振動子網を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

で定める。$A=A^{\mathsf T}$ は実対称である。局所グラフ $G=(V,E)$ 上では

```math
A
=
D_\delta+L_\kappa
```

とし、成分表示を

```math
H_{\rm micro}
=
\sum_i
\left[
\frac{p_i^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_0^2q_i^2}{2}
+
\frac{\delta_iq_i^2}{2}
\right]
+
\frac12
\sum_{\{i,j\}\in E}
\kappa_{ij}
\left(q_i-q_j\right)^2
```

と書ける。ここで $\kappa_{ij}=\kappa_{ji}\geq0$ である。$D_\delta$ は対角離調、$L_\kappa$ は重み付きグラフ Laplacian である。

安定条件は

```math
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
>
0
```

である。離調 $\delta_i$ は負でもよいが、全剛性行列は正定値でなければならない。本章では浴、散逸、環境残差を加えない。閉鎖有限振動子網だけでQ3-1の基準定理を構成する。

## 局所正準座標と回転包絡

各振動子に局所的な規格化座標

```math
Q
=
\sqrt{M_{\rm osc}\omega_0}\,q,
\qquad
P
=
\frac{p}{\sqrt{M_{\rm osc}\omega_0}}
```

を導入する。これは頂点ごとに独立な正準変換であり、$\{Q_i,P_j\}=\delta_{ij}$ を保つ。局所複素振幅と回転包絡を

```math
a
=
\frac{Q+iP}{\sqrt{2\mathcal J_0}},
\qquad
b(t)
=
e^{i\omega_0t}a(t)
```

と定める。複素数は実2次元正準平面の表示であり、量子的な生成消滅演算子ではない。

摂動行列に対応する有効演算子を

```math
h_0
=
\frac{\mathcal J_0}{2M_{\rm osc}\omega_0}A
```

とする。$A$ が局所疎行列なら $h_0$ も同じグラフ上で局所的である。

## 反回転項を含む厳密局所方程式

**R86の厳密局所方程式。**
第6.2節のミクロ Hamiltonian に対し、局所回転包絡は厳密に

```math
i\mathcal J_0\dot b
=
h_0b
+
h_0e^{2i\omega_0t}\overline b
```

を満たす。
第2項は反回転項である。位置結合だけの実ばね網では、この項を厳密に消すことはできない。従って

```math
i\mathcal J_0\dot b
=
h_0b
```

をミクロ方程式として最初から置くのは正しくない。第6章で、反回転項の効果を正常モード変換と弱結合展開により有限時間で評価する。

局所包絡から作る作用を

```math
I_{\rm loc}(t)
=
\mathcal J_0b(t)^\dagger b(t)
```

とする。厳密方程式から

```math
\frac{dI_{\rm loc}}{dt}
=
2
\operatorname{Im}
\left[
b^\dagger h_0
e^{2i\omega_0t}
\overline b
\right]
```

となり、一般には零でない。保存されるのはミクロエネルギーであり、局所回転包絡の作用ではない。

この点は第2章との接続で重要である。測定器へ入る直前の $I_{\rm loc}$ を読み、その時点の作用比 $I_k/I_{\rm loc}$ を使う単発測定は定義できる。しかし、伝播中の局所作用を厳密保存量として扱ったり、準備から測定まで自動的に同じ規格化が保たれると主張したりしてはならない。

## 厳密正常モード包絡

正定値行列

```math
\Omega
=
\left(
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
\right)^{1/2}
```

を定める。$\Omega$ を使って正常モード正準振幅 $c$ を作り、搬送回転を除いた厳密包絡を

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

とする。付録Eで正準変換を明示し、厳密に

```math
i\mathcal J_0\dot{\widetilde b}
=
h_{\rm ex}\widetilde b,
\qquad
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

が成立することを示す。

$\widetilde b$ は厳密に $\mathcal J_0\widetilde b^\dagger\widetilde b$ を保存する。ただし $\Omega$ の行列平方根を含むので、一般には各頂点だけで定義できる局所変数ではない。役割分担は次の通りである。

| 包絡 | 局所性 | 発展 | 作用保存 |
|---|---|---|---|
| $b$ | 頂点ごとに局所 | 反回転項を含めて厳密 | 一般には近似 |
| $\widetilde b$ | 一般には非局所 | $h_{\rm ex}$ で厳密 | 厳密 |
| 有効解 $b_L$ | 目標グラフ上で局所 | $h_L$ で近似 | 有効モデル内で厳密 |

## 目標グラフ演算子と弱結合量

有限空間グラフの重みを $g_{ij}=g_{ji}\geq0$ とし、

```math
\left(L_G\chi\right)_i
=
\sum_{j:\{i,j\}\in E}
g_{ij}
\left(\chi_i-\chi_j\right)
```

とする。目標とする実対称演算子を

```math
h_L
=
\frac{\mathcal J_0^2}{2m}L_G
+
V_L,
\qquad
V_L
=
\operatorname{diag}
\left(V_1,\ldots,V_L\right)
```

とする。古典パラメータを

```math
\kappa_{ij}
=
\frac{M_{\rm osc}\omega_0\mathcal J_0}{m}
g_{ij},
\qquad
\delta_i
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}
V_i
```

と選べば $h_0=h_L$ になる。従って、Laplacian の疎結合構造と局所ポテンシャルの形は、局所ばね結合と固有周波数離調から得られる。

一方、$m$ と $\mathcal J_0$ の値はこの対応式の設計パラメータである。特定の普遍定数または粒子質量がミクロ振動子網から必然的に選ばれることは示していない。

第6.6節の係数対応により $h_0=h_L$ とする。このとき

```math
A
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}h_L
```

であり、厳密正常モード生成子は

```math
h_{\rm ex}
=
\mathcal J_0\omega_0
\left[
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/2}
-I
\right]
```

となる。作用素ノルムによる無次元弱結合パラメータを

```math
\eta
=
\frac{\left\|A\right\|}
{M_{\rm osc}\omega_0^2}
=
\frac{2\left\|h_L\right\|}
{\mathcal J_0\omega_0}
```

とする。以下では $\eta<1$ を仮定する。この十分条件により

```math
I+
\frac{2h_L}{\mathcal J_0\omega_0}
>
0
```

が保証され、ミクロ剛性行列も正定値になる。

## 生成子と状態の有限時間誤差

**R86の生成子誤差節。**
$h_L=h_L^\dagger$、$\eta<1$ とする。このとき

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

が成立する。
証明は付録E.6に置く。実対称 $h_L$ の固有値ごとにTaylor剰余を評価するだけであり、本文では上界と物理的な補正の意味を用いる。

主項は

```math
h_{\rm ex}
=
h_L
-
\frac{h_L^2}{2\mathcal J_0\omega_0}
+
O
\left(
\frac{\left\|h_L\right\|^3}
{\mathcal J_0^2\omega_0^2}
\right)
```

である。補正 $h_L^2$ は一般に元のグラフより長距離の結合を含む。これは、厳密正常モード生成子が局所目標演算子と一致せず、局所性が弱結合近似として回復することを示す。

同じ初期値 $\widetilde b(0)$ から始める厳密解と目標有効解を

```math
\widetilde b(t)
=
e^{-ih_{\rm ex}t/\mathcal J_0}
\widetilde b(0),
```

```math
\widetilde b_L(t)
=
e^{-ih_Lt/\mathcal J_0}
\widetilde b(0)
```

とする。Duhamel 公式から

```math
\sup_{0\leq t\leq T}
\left\|
\widetilde b(t)-\widetilde b_L(t)
\right\|
\leq
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
\left\|\widetilde b(0)\right\|
```

を得る。自然な有効時間を

```math
T
=
c_T
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とすれば、相対誤差上界は

```math
\frac{c_T\eta}
{4\left(1-\eta\right)^{3/2}}
```

であり、固定 $c_T$ に対して $O(\eta)$ である。誤差は時間に比例して蓄積するため、$T$ を無制限に伸ばせる定理ではない。Duhamel評価の詳細は付録E.7に示す。

正定値行列

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2}
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

を定め、

```math
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

とする。付録Eの Bogoliubov 型正準変換は

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)}
```

である。逆変換も同じ $U_s,V_s$ を使う。

```math
\delta_{\rm loc}(\eta)
=
\left(1-\eta\right)^{-1/4}-1
```

と置くと、全時刻で

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}(\eta)
\left\|\widetilde b(0)\right\|
```

が成立する。$\delta_{\rm loc}=O(\eta)$ である。厳密だが非局所な包絡と、局所だが反回転項を持つ包絡の差を、この量で制御する。正準変換と上界は付録E.4、E.5に示す。

実際の局所初期値 $b(0)$ から始める目標解を

```math
b_L(t)
=
e^{-ih_Lt/\mathcal J_0}b(0)
```

とする。

<!-- theorem-start:theorem -->
**定理（R86：M37有限時間包絡線縮約）**

$h_L$ が時間独立な実対称行列で $\eta<1$ とする。第6.4節の反回転項を含む厳密局所方程式、第6.5節の厳密正常モード包絡、第6.7節の生成子誤差を同時に用いると、第6章のミクロ解から作る局所包絡 $b(t)$ は

```math
\sup_{0\leq t\leq T}
\left\|
b(t)-b_L(t)
\right\|
\leq
\varepsilon_{\rm car}(T)
\left\|\widetilde b(0)\right\|
```

を満たす。ここで

```math
\varepsilon_{\rm car}(T)
=
2\delta_{\rm loc}(\eta)
+
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
```

である。厳密正常モード作用は保存され、局所作用の相対変動は第6.8節の $2\delta_{\rm loc}+\delta_{\rm loc}^2$ 以下である。規格化した包絡方向を任意の有限基底で比較した分布誤差は、第6.9節の $\varepsilon_{\rm dist}(T)$ 以下である。
<!-- theorem-end:theorem -->

証明は付録E.5--E.7に置く。局所包絡と正常モード包絡の両端の変換差、およびDuhamel評価による中央の生成子差を加える。

自然時間 $T=O(\mathcal J_0/\|h_L\|)$ では $\varepsilon_{\rm car}=O(\eta)$ である。本稿で「局所古典振動子網から Schrödinger 型発展を導く」とは、この有限時間近似定理を意味する。

## 局所作用の変動

厳密包絡作用を

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
```

とする。これは保存される。局所作用との相対差は

```math
\left|
\frac{I_{\rm loc}(t)}{I_{\rm ex}}-1
\right|
\leq
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
```

である。従って局所作用は弱結合領域で $O(\eta)$ だけ振動し得る。局所作用を厳密保存量とする旧記述は、有効層内部の近似としてのみ維持する。詳細は付録E.8に示す。

## 干渉と有限基底作用比の診断

有効モデル内で入力1モードを等分岐し、2経路に位相 $\phi_1,\phi_2$ を蓄積して再結合すると

```math
\chi_+
=
\frac{e^{i\phi_1}+e^{i\phi_2}}{2},
\qquad
\chi_-
=
\frac{e^{i\phi_1}-e^{i\phi_2}}{2}
```

となり、

```math
p_+
=
\cos^2
\left(
\frac{\phi_1-\phi_2}{2}
\right),
\qquad
p_-
=
\sin^2
\left(
\frac{\phi_1-\phi_2}{2}
\right)
```

を得る。理想暗出力は $\phi_1-\phi_2=\pi$ で零になる。

ミクロ局所包絡では、反回転項と正常モード補正により出力方向が $O(\eta)$ だけずれる。暗出力確率の誤差は振幅誤差の2乗だけとは限らない。規格化と任意有限基底測定を含む安全な上界は、第2章で全変動距離として与える。

第6章のミクロ局所包絡を測定時刻 $T$ で規格化し、

```math
\widehat b_{\rm mic}(T)
=
\frac{b(T)}{\left\|b(T)\right\|}
```

とする。目標有効状態を

```math
\chi_L(T)
=
\frac{b_L(T)}{\left\|b_L(T)\right\|}
```

とする。任意の有限基底変換 $W$ に対し、実際の作用比と目標 Born 型重みを

```math
p_k^{\rm mic}
=
\left|
\left(W\widehat b_{\rm mic}\right)_k
\right|^2,
\qquad
p_k^L
=
\left|
\left(W\chi_L\right)_k
\right|^2
```

と定める。

**R86の有限基底分布系。**
任意のユニタリ $W$ について、全変動距離は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\left\langle
\widehat b_{\rm mic},
\chi_L
\right\rangle
\right|^2
}
\leq
\left\|
\widehat b_{\rm mic}-\chi_L
\right\|
```

を満たす。
最初の不等式は純粋状態間の距離が任意の射影成分分布の全変動距離を上から抑えること、2番目は単位ベクトルのノルム評価から従う。ここでは量子測定を仮定していない。左辺は古典作用比を同じ基底 $W$ で比較した量である。

第6章の有限時間上界と $\delta_{\rm loc}<1$ を使うと、

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\varepsilon_{\rm dist}(T),
```

```math
\varepsilon_{\rm dist}(T)
=
\min
\left\{
1,
\frac{
2\varepsilon_{\rm car}(T)
}{
1-\delta_{\rm loc}(\eta)
}
\right\}
```

を得る。$\varepsilon_{\rm dist}$ は包絡方向のずれが測定分布へ伝わる誤差であり、環境誤差ではない。

本節の式は、派生複素包絡の作用比を任意有限基底で比較する診断であり、それだけでは単一試行の粒子を作らない。Q3では準備終了面で1回だけ初期M42位置を作り、空間セル基底の局所辺流に沿って同じ粒子を輸送する。任意の基底 $W$ で終時刻に新しい粒子位置を作るR170と、M42の連続位置過程を同じ運転へ重ねない。Q1のW型2モード測定は第3章で独立に扱う。

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。これは空間セル基底の目標位置分布である。R172は同じ分布をM42トークンの等変分布として全有限時刻へ運び、R173は節正則化と有限衝突Hamiltonian近似を与える。R86の作用比だけを粒子実体と同一視せず、粒子層の追加方程式と初期選択を必要とする。

## M37標本集団と統計共分散

同じM37装置を反復する試行空間を $(\mathcal P,\mu)$ とし、局所包絡を複素確率変数

```math
Z_t(\omega):=b(t;\omega)\in\mathbb C^L
```

として扱う。有限で正の集団作用

```math
S_t=\mathbb E_\mu[Z_t^\dagger Z_t]
```

を仮定し、規格化自己共分散を

```math
C_Z(t)
=
\frac{\mathbb E_\mu[Z_tZ_t^\dagger]}{S_t}
```

と定める。$C_Z$ は正半定値、trace 1である。これは集団記述であり、単一試行で装置が読む変数ではない。各試行のM37包絡 $Z_t(\omega)$ は、準備終了面では初期M42位置選択へ、輸送中はM42の局所rate controllerへ渡す派生物理信号である。

本稿では $C_Z$ を「非中心化自己共分散」、すなわち規格化した第2モーメントとして使う。通常の中心化共分散を意味せず、$\mathbb E[Z_t]=0$ の場合にだけ中心化した量と比例して一致する。R168の支持結論はこの非中心化定義に対する主張であり、中心化共分散の階数1条件だけからは従わない。

初期集団をM54で準備する場合、設定前seed測度を $\mu_{\rm seed}$、準備切断面を $t_{\rm cut}$ とし、

```math
\mu_{\rm cut}^{c}
=
(\Phi_c^{t_{\rm cut}})_\#\mu_{\rm seed}
```

をM37初期面へ渡す。R181Aの安全事象外は無反応として残し、安全集団の第2モーメントだけが $cc^\dagger$ へ有限誤差で近づく。M37の初期分布へ $C_Z(0)=cc^\dagger$ を直接仮定する経路と、M54の押出し測度から得る経路を同じ準備状態と呼ばない。

## 共通R135のM37有限時間特殊化

理想有効発展を

```math
U_L(t)=\exp\left(-ih_Lt/\mathcal J_0\right)
```

とし、同じ初期標本から作る理想包絡を $\widetilde Z_t=U_L(t)\widetilde Z_0$ とする。$\widetilde S_0=\mathbb E\|\widetilde Z_0\|^2$ とし、実際の $S_t=\mathbb E\|Z_t\|^2$ に対して

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置く。

**R135のM37特殊化。**

全試行でR86の相対包絡誤差

```math
\|Z_t-\widetilde Z_t\|
\leq
\varepsilon_{\rm car}(T)\|\widetilde Z_0\|
```

が $0\leq t\leq T$ に一様に成り立つとする。このとき

```math
D_{\rm tr}
\left(
C_Z(t),
U_L(t)C_Z(0)U_L(t)^\dagger
\right)
\leq
\min\{1,r_T\},
```

```math
r_T
=
2\varepsilon_{\rm car}(T)\sqrt{\kappa_T}
+\varepsilon_{\rm car}(T)^2\kappa_T
```

が成り立つ。$S_0=\widetilde S_0$ で、R86の局所--正常モード比較から $S_t\geq(1-\delta_{\rm loc})^2S_0$、$\delta_{\rm loc}=(1-\eta)^{-1/4}-1<1$ を使う場合、$q_T=\varepsilon_{\rm car}/(1-\delta_{\rm loc})$ と置けば $r_T\leq2q_T+q_T^2$ としてよい。
証明は付録F.2に置く。同じM37包絡差を、担体誤差、共分散誤差、ray誤差へ別々に加算しない。どの段階で規格化したかを固定し、一つの上流誤差から必要な下流評価だけを選ぶ。

## M42局在トークンとR172--R173

M42は、M37担体と別の実体として有限グラフ上に1個の粒子位置 $X_t$ を置く。理想有効包絡 $b_L$ の頂点重みと局所辺流を

```math
p_i(t)=|b_{L,i}(t)|^2,
\qquad
J_{i\to j}(t)
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left[
b_{L,j}^*h_{L,ji}b_{L,i}
\right]
```

とし、$p_i>0$ で

```math
\lambda_{i\to j}(t)
=
\frac{[J_{i\to j}(t)]_+}{p_i(t)}
```

を採用する。

<!-- theorem-start:theorem -->
**定理（R172：M37有効辺流に沿うM42局在トークンの等変輸送）**

有限グラフ上の時間連続な有界局所Hermitian生成子と上の最小率を仮定する。$P(X_0=i)=p_i(0)$ なら全有限時刻で $P(X_t=i)=p_i(t)$ が成り立つ。さらに $h_1=\sup_t\max_i\sum_{j:j\sim i}|h_{L,ij}(t)|$ とすれば、$\mathbb E[N_T]\leq h_1T/\mathcal J_0$ であり、有限時間爆発はない。
<!-- theorem-end:theorem -->

これは粒子位置が統計量だという意味ではない。各試行では $X_t$ が1頂点に局在し、上の分布は試行集団の記述である。

節で有限装置を保つため、正則化率を

```math
\lambda_{i\to j}^{\rho,\sigma}(b)
=
\frac{
\left[
J_{i\to j}(b)+
\sqrt{J_{i\to j}(b)^2+\sigma^2}
\right]/2
}{|b_i|^2+\rho}
```

とする。

<!-- theorem-start:theorem -->
**定理（R173：M42の節一様正則化と有限衝突Hamiltonian近似）**

正則化M42を理想分布と同じ初期分布から開始すると、固定有限時間 $T$ で理想分布との差は

```math
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]
```

以下である。さらに固定 $\rho,\sigma,T$ では、正則化生成子を有限時間窓ごとに凍結し、方向タグ、物理閾値座標、仕事register、履歴を持つ駆動衝突cellを辺ごとに配置した有限Hamiltonian散乱列が縮約経路測度を任意精度で近似する。一般のM42率は詳細釣合いを満たさないため、R162の平衡率公式をそのまま用いる主張ではない。
<!-- theorem-end:theorem -->

完全状態にはM37の実振動子、現在位置、入射bath cell、到着clock、運動方向、物理閾値座標、反射・通過、仕事register、出射エネルギー、使用済み履歴を含める。単一試行のpiecewise deterministic方程式、方向別衝突写像、正則化証明、資源発散は付録Nに置く。

### 固定時刻M50診断との区別

共通R168は、M37標本を任意の固定時刻にM50へ渡した場合の枝統計を診断する一般定理として引き続き成立する。ただし現行Q3の粒子経路では、終時刻R170による新しい位置の再標本化に使わない。次の式はM54準備、R135共分散、M42初期選択の整合を検査するために残す。

階数1の場合、$C_Z(t_\star)=c_\star c_\star^\dagger$ なら、付録Lの支持補題から

```math
Z_{t_\star}(\omega)
=
\alpha(\omega)c_\star
\qquad
\mu\text{-a.s.}
```

である。M50制御器が受け取るのは集団因子 $c_\star$ でなく、各試行の $Z_{t_\star}(\omega)$ である。

安全事象を

```math
G=\{Z_{t_\star}\neq0\}\cap G_{\rm hold}\cap G_{\rm guard}
```

とし、安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

と定める。これはtrace $P(G)$ の非規格化行列であり、失敗質量を捨てない。

**R168へのM37代入。**

$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ とする。各安全試行のM50枝分布を平均し、失敗を無反応へ送ると、完全結果分布は

```math
P(i)
=
\mathbb E
\left[
\mathbf1_G\pi_i^\delta(Z_{t_\star})
\right]
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
```

```math
P(\varnothing)=P(G^c)
```

である。さらに次が成り立つ。

1. $C_Z=c_\star c_\star^\dagger$ かつ $G$ 上で信号が非零なら、$Z=\alpha c_\star$ であり、$R_Z^G=P(G)c_\star c_\star^\dagger$ となる。
2. $Z^\dagger Z=s_*>0$ がほとんど確実で $P(G)=1$ なら、$R_Z^G=C_Z$ である。
3. 一般の可変作用集団では $R_Z^G$ が物理的な読出し対象であり、$C_Z$ への置換には半径方向補正と無反応質量の評価が必要である。

近似ray $\widehat Z$ が目標rayから純粋状態距離 $s$ 以内なら、対応する安全分布の全変動距離は $s/(1+\delta)$ 以下である。成功試行だけで再規格化しない。
$P(G)=1$ の可変作用集団では、$\overline S=\mathbb E[Z^\dagger Z]$ とすると

```math
D_{\rm tr}(R_Z^G,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{Z^\dagger Z}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}(Z^\dagger Z)}}{\overline S}.
```

この補正は一般には零でない。可変作用反例を付録Fに残す。R135の規格化方向誤差を使う場合、$q_T<1$ なら $\rho_T=q_T/(1-q_T)$ を安全なray誤差上界として選べる。

## M54--M37--M42の開始面と終位置記録

準備切断時刻を $t_0$、終位置記録時刻を $T>t_0$ とする。M54/R181Aの切断面からM37初期面へ実正準担体を渡し、同じ試行の $Z_{t_0}(\omega)$ にM50/R164の作用殻選択を一度だけ適用して初期位置 $X_{t_0}$ を作る。統計因子 $c$、$C_Z$、全位置分布をcontrollerへ再注入せず、各試行の実信号と作用殻だけを使う。

$t_0<t<T$ では、M37実振動子とM42の現在位置、局所bath cell、clock、履歴を同時に進める。時刻 $T$ では別のM50位置を生成せず、R112の局所記録剪断で既存の $X_T$ を記録 $D_{X_T}$ へ写す。M50/R164は初期位置の物理化、R172/R173は同じ粒子の輸送、R112は終位置の記録を担う。

<!-- theorem-start:theorem -->
**定理（R174：M54--M37--M42の有限時間準備・輸送・記録受渡し）**

固定有限グラフと固定時間 $T$ について、M54/R181Aで担体集団を準備し、同じ試行の初期信号にM50/R164を一度だけ適用して $X_{t_0}$ を作り、M37と正則化M42を同時に進め、既存の $X_T$ をR112で記録する。完全結果分布と理想Born型位置分布の全変動距離は第6.14節の $\varepsilon_{174}(T)$ 以下である。安全事象外とcell overflowは無反応へ残し、成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

## 誤差、時間、資源、Q3-4A・Q3-5への接続

R174の完全結果分布誤差を

```math
\begin{aligned}
\varepsilon_{174}(T)
\leq{}&
\varepsilon_{\rm prep}
+\varepsilon_{\rm init}
+\varepsilon_{\rm node}
+\varepsilon_{37\to42}
+\varepsilon_{\rm step}\\
&+\varepsilon_{\rm coll}
+\varepsilon_{\rm over}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm rec},
\end{aligned}
```

```math
\varepsilon_{\rm node}
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right]
```

と分ける。$\varepsilon_{\rm prep}$ はM54のrank-one準備とseed無反応、$\varepsilon_{\rm init}$ は1回のM50/R164初期位置選択、$\varepsilon_{37\to42}$ はR86担体誤差から正則化M42生成子へのDuhamel誤差である。同じM37包絡差をR135診断、M42生成子、終位置記録へ重複加算しない。

固定 $\rho,\sigma>0$ では最大率が有限なので、時間窓数、方向別閾値分割、Hamiltonian平滑化、仕事register範囲、有限衝突cell数、clock精度を増やして $\varepsilon_{\rm step}$、$\varepsilon_{\rm coll}$、$\varepsilon_{\rm over}$、$\varepsilon_{\rm clk}$ を任意に小さくできる。ただし $\rho,\sigma\downarrow0$ では最大率、必要cell数、閾値・clock精度、仕事register範囲が発散し得る。1つの固定装置で厳密nodeを追跡するとは主張しない。

R124の理想増分を $\alpha$、R125の理想分布距離を $\Delta$ とする。比較する各M42運転の誤差が $\varepsilon_{174}$ 以下なら、観測差はそれぞれ $\alpha-2\varepsilon_{174}$、$\Delta-2\varepsilon_{174}$ 以上である。有限パラメータで正にできるが、M54準備、M37伝播、初期作用殻、M42衝突bath、clock、終位置記録の単一Hamiltonian統合が未完了なので、Q3-4AとQ3-5は条件付き達成を維持する。Q3-4Bには、同じ粒子のW型左右領域間の半周期移送と一周期回帰を中央障壁領域込みで接続する別の誤差台帳が必要であり、本節のR124接続からは従わない。

## 数値検算

8振動子の1次元鎖に弱い調和型離調を加え、固定目標 $h_L$ に対して $\omega_0$ を変えた。初期局所包絡は乱数種 `20260809` の複素ベクトルを規格化し、観測時刻を

```math
T
=
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とした。作用素誤差は $\|h_{\rm ex}-h_L\|$、局所状態誤差は $\|b(T)-b_L(T)\|$ である。

| $\omega_0$ | $\eta$ | 作用素誤差 | 局所状態誤差 | 規格化状態の距離 |
|---:|---:|---:|---:|---:|
| 20 | 0.1793 | 0.07391 | 0.03045 | 0.02890 |
| 40 | 0.08967 | 0.03849 | 0.01928 | 0.01690 |
| 80 | 0.04483 | 0.01966 | 0.01078 | 0.00959 |

全例で作用素上界、厳密包絡の状態上界、局所包絡の状態上界、局所作用変動上界を満たした。$\omega_0=40$ から80への倍増で作用素誤差は1.96分の1、局所状態誤差は1.79分の1になり、弱結合極限での $O(\eta)$ 収束と整合する。この表は `tools/verify_envelope_reduction.py` から再現できる。

M42/R172--R174については `tools/verify_m42_spatial_token.py` を用いる。局所連続方程式、最小率の等変性、期待跳躍率、節正則化、全変動上界、M37担体誤差のDuhamel受渡し、1回の初期作用殻選択、無反応質量、局所履歴を検算する。R135とR168は `tools/verify_common_signal_m50.py` の固定時刻統計診断として残す。数値検算は解析証明の代わりではなく、単一試行状態と集団統計、初期選択と終記録、同じ誤差の二重計数を監査する回帰検査である。

## Q3-1の達成判定と限界

本稿の固定されたQ3-1達成基準は、局所位置結合振動子網から空間格子上の Schrödinger 型時間発展を、近似範囲と誤差を伴って導くことである。本章のM37部分は次を与えた。

1. 有限個の実古典振動子からなる局所位置結合 Hamiltonian 。
2. 反回転項を含む局所包絡の厳密方程式。
3. 厳密正常モード包絡と生成子 $h_{\rm ex}$。
4. 目標実対称 $h_L$ との係数対応。
5. 弱結合・弱離調・有限時間の作用素誤差と状態誤差。
6. 再現可能な数値検算。

従って、Q3-1はこの限定された有限実対称モデルについて達成と判定する。これは量子力学の必然的創発を示す結果ではなく、局所古典振動子網における制御された Schrödinger 型有効力学である。

Q3-1の固定基準自体はR86で満たされ、今回の改訂で後から基準を広げたわけではない。R181AはM37初期集団に使える共通開放準備、R112は共通有限正準信号代数、R135はM37標本集団の共分散持上げ、R172はM42の理想等変輸送、R173は節正則化と有限衝突Hamiltonian近似、R174は準備から終位置記録までの誤差受渡しを追加する強化結果である。M54--M37--M42受渡しをQ3-1達成の根拠へ遡及的に加えない。

位置ばね結合から直接得られる $A$ と $h_L$ は実対称である。磁場に対応する Peierls 位相、一般の複素 hopping、運動量に比例する結合は本定理に含まれない。これらを厳密に実装するには、位置と運動量の両方を結ぶ追加の正準結合が必要になる。

本稿のQ3-1定理は時間非依存 $A$ に限定する。時間依存 $A(t)$ が有界であるだけでは不十分である。$2\omega_0$ 近傍の Fourier 成分が反回転項と共鳴し得るため、時間依存駆動には例えば

```math
\frac{\sup_t\left\|h_L(t)\right\|}
{\mathcal J_0\omega_0}
\ll1,
\qquad
\frac{\sup_t\left\|\dot h_L(t)\right\|}
{\mathcal J_0\omega_0^2}
\ll1
```

のような低速条件、または明示的な非共鳴条件が別に必要である。M47のQ1-1は、M37が供給する時間非依存W型生成子の最低2モードへ傾斜制御を追加する。R86は時間非依存結合の包絡近似なので、時間依存傾斜のミクロ実装を自動的には証明しない。第3章と付録Bでは、全W型制御をスペクトル間隔と切替時間の誤差として別に評価する。時間依存M37を同じハードウェアへ厳密統合する課題は第8章に残す。

次はQ3-1の固定達成基準を超える一般化であり、本章の結論に含めない。

1. $\mathcal J_0$ と有効質量 $m$ の普遍的な値の導出。
2. 一般の複素 Hermitian 演算子と磁場結合。
3. 時間依存駆動に対する一様な非共鳴定理。
4. 非線形ミクロ結合に対する閉包。
5. 一般連続極限と境界条件の一様誤差。
6. 格子細分化で得る連続空間の粒子軌道、位相量子化、多粒子位置。
7. 最小率がM37のミクロHamiltonianだけから一意に選ばれること。
8. 粒子位置の慣性質量、電荷、担体エネルギーとの同定。
9. 固定性能の同じ装置による正則化誤差零極限。
10. 1次元井戸型・調和型ポテンシャルの低位束縛スペクトルと、エネルギー保存型の有限時間デコヒーレンス。
11. M54、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所Hamiltonianへ統合すること。
12. 源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを扱う、固定目標より強い装置模型。

M47の静的起源はM37の対称W型生成子と最低2モードにある。制御されたM37実装への強化は第6.17節と第3.5.1節で管理する。M42をQ1へ流用せず、M47の粒子位置はM50/R170の固定時刻instrumentに従う。M37のHamiltonianと反回転項の評価は変更しない。外部 $\lambda_{\rm prep}(t)$ による開放準備と閉鎖作用角伝播、matching受渡しの条件は第8章と付録Hに示す。

Q3の二乗統計はM54が準備するrank-one集団と、R164による1回の初期位置選択に由来する。M42は同じ粒子を輸送し、終時刻には再標本化せず記録する。状態数だけで初期選択の全ミクロ過程を説明したとはせず、有限衝突bathだけでM54準備や作用容量の起源を説明したとも扱わない。

## W型制御への有限時間拡張

物理的主線では同じ実振動子へ傾斜を加え、その包絡からQ1制御を得る。有限格子上で $h_W(t)=h_W(0)-F(t)x$ とし、第6.6節の対応を

```math
A(t)=\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}h_W(t),\qquad
H(t)=\frac{\omega_0}{2}(P^{\mathsf T}P+Q^{\mathsf T}Q)
+\frac1{\mathcal J_0}Q^{\mathsf T}h_W(t)Q
```

へ拡張する。Fは有限時間の外部制御であり、自律時計や閉鎖仕事源を仮定しない。制御域で全剛性を正定値に保ち、位置ばねの非負重みと局所離調の対応を維持する。厳密に

```math
i\mathcal J_0\dot b=h_W(t)b+e^{2i\omega_0t}h_W(t)\overline b,
\qquad
\frac{dH}{dt}=\frac{\partial H}{\partial t}
=\frac1{\mathcal J_0}Q^{\mathsf T}\dot h_WQ
```

である。瞬時切替ではQ,Pは連続で、仕事は $Q^{\mathsf T}\Delta h_WQ/\mathcal J_0$。時刻ごとの正定値性だけでは駆動による増幅を防げない。

区分一定の区間rで生成子を $h_r$、長さを $\Delta t_r$、$\eta_r=2\|h_r\|/(\mathcal J_0\omega_0)<1$ とする。R86の係数を使い

```math
a_r=(1-\eta_r)^{-1/4}\varepsilon_{{\rm car},r}(\Delta t_r),
\qquad E_N=\prod_{r=1}^N(1+a_r)-1
```

と置く。付録E.12の合成評価により、同じ初期値の有効区分一定解との差は $E_N\|b(0)\|$ 以下である。区間内の時刻にも、その区間の経過時間で同じ式を適用する。区間ごとの再準備は使わない。滑らかな切替と区分一定列との差は付録E.13の実線形伝播差で評価し、静的R86に時間依存行列を代入しただけの主張にはしない。

この係数は保守的な上界である。Jが小さいとRabi時間が伸びるため、$J/G$、$\eta_r$、全時間、区間数、切替時間、状態残差を同時に監査する。低mode内に制限した周波数差の評価が全スペクトルノルムより鋭い場合もある。全操作の任意精度構成と資源上界は未完であり、静的Q3-1の達成範囲は変えない。

### 三段階の有限例照合

`tools/verify_m37_w_q1_bridge.py` は25点のW型格子で、同じ初期状態から実正準運動、全W型包絡、射影2モード運動を比較する。採用例は $J=0.02098$、$G=1.21391$、全時間122.513であり、3区間を再準備なしで接続する。搬送周波数を2000、20000、200000と増やすと、採用時刻での最大包絡誤差は0.02571、0.002585、0.0002584へ減る。一方、実運動と2モード運動の差は0.05221、0.04089、0.04030であり、搬送周波数だけでは消えない。これは包絡誤差と射影残差を分ける必要性を示す有限例であり、全パラメータ域の証明ではない。共通位相依存、rank-oneからのずれ、作用変動、滑らかな切替の仕事も別々に検算する。数値上界と再現条件は `VALIDATION.md` に記録する。

# Q3の確率力学、束縛状態、トンネル現象、2経路干渉、位相量子化

> **位置づけ：** 新Q3-2とQ3-6の未達課題、Q3-3A・Q3-3Bの達成、Q3-3C・Q3-4Bの部分達成、Q3-4A・Q3-5の条件付き達成を区別する。


本章は、Nelson流の作用変分または時間対称Newton則を古典ミクロモデルから導くQ3-2、R123によるQ3-3A・Q3-3B、M47/R140を部分根拠とするQ3-3C・Q3-4B、R124・R125とM42局在トークンを接続するQ3-4A・Q3-5、位相量子化のQ3-6を区別する。R123--R125の完全証明は付録F、G、M42輸送の証明は付録Nに置く。

## Nelson流の作用変分または時間対称Newton則（Q3-2）

**固定目標と達成判定。** Q3-2は、明示的な古典ミクロモデルの縮約から、Nelson型確率力学における作用の停留原理、または前進・後退平均加速度を対称に組み合わせたNewton則を導く。対象となる確率過程、前進・後退平均微分、力とポテンシャル、適用時間、近似範囲、誤差を明示する。作用変分経路では作用汎関数、許容変分、端点条件も必要である。二経路の少なくとも一方を満たせばよい。

**運用状態。** Q3-2は未達である。R86はM37の実振動子網から有限時間Schrödinger型包絡発展を導くが、粒子確率過程の前進・後退平均微分や時間対称平均加速度を導かない。R172は採用したM42跳躍率に対する等変輸送を与えるが、その率からNelson作用またはNewton則を逆導出しない。従って、既存の波動包絡と採用跳躍則を結合しただけでは達成としない。

**次の検証線。** M37担体、M42粒子、有限衝突bathを一つの開始分布と有限時間縮約へ置き、得られる位置過程について前進生成子と時間反転生成子を同じ母測度から定める必要がある。その上で、前進・後退drift、osmotic速度、current速度を誤差付きで同定し、古典ミクロ作用の縮約がNelson--Yasue型作用へ収束するか、または時間対称平均加速度が外力に一致するかを検査する。目標式を縮約前の仮定へ入れることや、外部から仮定したSchrödinger方程式を確率力学の記号へ書き換えることは認めない。

**非主張。** 本版はNelson作用、時間対称Newton則、量子ポテンシャルを導出したとは主張しない。確率過程を外部公理として置くこと、連続空間極限、多粒子配置空間もQ3-2の達成には含めていない。位相量子化の大域条件はQ3-6で独立に判定する。

## 束縛状態（Q3-3A--Q3-3C）

**固定目標と達成判定。** Q3-3A、Q3-3B、Q3-3Cは、井戸型、調和型、W型についてそれぞれ独立に、有限個の非縮退低位固有状態の固有値、密度、節構造を再現する。さらに、有限環境との弱結合を縮約したエネルギー固有基底で、非対角相関の有限時間減衰と対角占有率の安定性を導く。1試行ごとの状態選択、基底状態への緩和、射影的な収縮、独立したエネルギー測定器は要求しない。

<!-- theorem-start:theorem -->
**定理（R123：低位束縛状態と有限環境純位相緩和）**

1次元Dirichlet井戸と調和型ポテンシャルについて、任意に固定した有限個の低位固有値、密度、節位置は有限差分模型から連続模型へ収束し、低位固有値は非縮退である。先頭 $K$ モードを有限個の環境正準対へ純位相結合し、独立な二点環境運動量を読まずに縮約すると、注目系エネルギーと対角占有率を厳密に保存したまま全非対角相関が同じ有限時刻に零となり、有限の完全回復時刻を持つ。
<!-- theorem-end:theorem -->

**R123の束縛スペクトル。** 区間 $(0,\ell)$ のDirichlet井戸を $N$ 内部点、$a=\ell/(N+1)$ で離散化する。第 $k$ 固有値と固有ベクトルは

```math
E_{k,N}^{\rm well}
=
\frac{2\mathcal J_0^2}{ma^2}
\sin^2
\left(
\frac{k\pi}{2(N+1)}
\right),
\qquad
u_{k,N}(j)
=
\sqrt{\frac{2}{N+1}}
\sin
\left(
\frac{k\pi j}{N+1}
\right)
```

である。固有値は単純で、第 $k$ 状態は $k-1$ 個の節区間を持つ。固定低位モードについて固有値誤差は $O(a^2)$、格子密度と節位置も連続井戸へ収束する。

調和型では、有限区間のDirichlet差分生成子に $m\omega^2x^2/2$ を加える。実対称三重対角行列の固有値は単純で、第 $k$ 固有ベクトルは $k$ 回符号を変える。固定 $k$ について

```math
E_{k,N,L}^{\rm osc}
\longrightarrow
\mathcal J_0\omega
\left(k+\frac12\right),
\qquad
\left|
E_{k,N,L}^{\rm osc}
-
\mathcal J_0\omega
\left(k+\frac12\right)
\right|
\leq
C_k
\left(
a^2+e^{-c_kL^2}
\right)
```

であり、密度と節位置もHermite--Gauss状態へ収束する。離散Sturm振動、二次形式のmin--max収束、Gauss尾部評価を含む証明は付録G.2節に置く。

**R123の有限環境純位相緩和。** 先頭 $K$ モードの作用を $I_n=\mathcal J_0|b_n|^2$、有限環境を $K$ 個の正準対 $(\theta_n,P_n)$ とし、

```math
H_{\rm deph}
=
\sum_n
\frac{E_n}{\mathcal J_0}I_n
+
\sum_n
\frac{P_n^2}{2M_n}
+
\frac{\lambda}{\mathcal J_0}
\sum_n
I_nP_n
```

を採用する。初期環境運動量を独立な $P_n=\pm p_*$ の等重み集団で調製し、環境を読まずに縮約すると、

```math
C_{nn}(t)=C_{nn}(0),
```

```math
C_{nm}(t)
=
C_{nm}(0)
\exp
\left[
-\frac{i(E_n-E_m)t}{\mathcal J_0}
\right]
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
\qquad
n\neq m
```

となる。各 $I_n$ と $P_n$ が保存されるので、注目系のエネルギー占有率、注目系エネルギー、全Hamiltonianは厳密に保存される。それでも $\lambda\neq0$ では系の位相が読まない環境運動量と相関するため、縮約した注目系は開放系である。

全非対角相関は

```math
T_{\rm dec}
=
\frac{\pi\mathcal J_0}{2\lambda p_*}
```

で零となり、任意の $0<\delta<1$ に対してその周りの正の幅を持つ観測窓で減衰因子を $\delta$ 以下にできる。有限環境なので

```math
T_{\rm rec}
=
\frac{\pi\mathcal J_0}{\lambda p_*}
=
2T_{\rm dec}
```

で完全なコヒーレンス回復が起こる。主張する有効窓と回復時刻を同じ式で明示しており、不可逆な無限時間減衰とはしていない。

**達成判定。** R123は、井戸型・調和型の任意に固定した有限個の非縮退低位状態について、固有値、密度、節、格子・領域収束を与える。さらに有限自律Hamiltonian、初期調製、縮約、非対角相関の有限時間減衰、対角占有率の厳密保存、回復時間を与える。従ってQ3-3AとQ3-3Bは達成である。W型についてはM47/R140が最低偶・奇2モードとその制御を与えるが、任意に固定した有限個の低位状態の格子・領域収束と、同じ固有基底での有限環境純位相緩和をそろえていない。従ってQ3-3Cは部分達成である。

**非主張。** 状態選択、固有状態を吸引状態とする機構、基底状態への冷却、射影収縮、不可逆な熱浴極限は導かない。二点運動量集団は外部乱数位相を時間ごとに注入する処方ではなく、開始面で明示した有限Hamiltonian環境の調製分布である。

## 有限障壁のトンネル効果（Q3-4A）

**固定目標と達成判定。** Q3-4Aは、有限障壁を持つSchrödinger型発展で、障壁値より低いエネルギー成分だけからなる状態が障壁反対側へ位置確率を移すことを示し、その確率を位置読出しへ接続する。散乱装置全体や透過率曲線は要求しない。

<!-- theorem-start:theorem -->
**定理（R124：障壁値未満状態の反対側確率増加）**

3頂点有限障壁には、障壁値未満のスペクトル支持だけを持ち、有限時刻に障壁反対側の位置確率を正の幅 $\alpha$ だけ増加させる規格化初期状態が存在する。初期M42位置の準備と終位置記録を含む各運転のR174誤差が全変動距離 $\varepsilon_{174}$ 以下なら、観測増分は $\alpha-2\varepsilon_{174}$ 以上である。
<!-- theorem-end:theorem -->

**R124の最小有限障壁。** 頂点を障壁手前 $L$、障壁 $B$、反対側 $R$ とし、

```math
h_{\rm bar}
=
\begin{pmatrix}
0&-\kappa&0\\
-\kappa&V&-\kappa\\
0&-\kappa&0
\end{pmatrix},
\qquad
V>0,\quad \kappa>0
```

を使う。障壁値は $V$ である。低位固有値と係数を

```math
E_-
=
\frac{V-\sqrt{V^2+8\kappa^2}}{2},
\qquad
\alpha
=
\left(
1+\frac{E_-^2}{2\kappa^2}
\right)^{-1/2}
```

とする。零エネルギー反対称状態 $a$ と、$E_-$ の左右対称固有状態 $v_-$ の等重み重ね合わせ $b_0=(a+v_-)/\sqrt2$ を選ぶ。残る固有値 $E_+$ は $V$ より大きく、$b_0$ の支持は $\{E_-,0\}$ だけなので

```math
\mathbf 1_{[V,\infty)}
(h_{\rm bar})b_0
=
0.
```

有限時刻 $T_{\rm bar}=\pi\mathcal J_0/|E_-|$ では低位対称成分だけが符号反転し、

```math
p_R(0)
=
\frac{(1-\alpha)^2}{4},
\qquad
p_R(T_{\rm bar})
=
\frac{(1+\alpha)^2}{4},
```

```math
p_R(T_{\rm bar})-p_R(0)=\alpha>0
```

を得る。初期右裾を零とせず、その厳密値を基準にした増分である。$V/\kappa$ を大きくすると初期右裾と障壁占有率は小さくなる一方、移動時刻は長くなる。

第6.12--6.14節のM42/R174が初期選択から終位置記録までを全変動距離 $\varepsilon_{174}$ 以内で再現すれば、観測増分は $\alpha-2\varepsilon_{174}$ 以上である。$\varepsilon_{174}<\alpha/2$ を満たす有限パラメータを条件付きで選べるため、正の増分は記録後にも残る。完全な代数証明は付録F.7、G.3節、M42誤差証明は付録Nに置く。

**達成判定。** R124は有限グラフの3分割、生成子、障壁値、障壁値未満の厳密スペクトル支持、初期基準確率、有限時刻の正の増分を与える。R172--R174は1個の局在トークンを初期分布から反対側へ輸送して記録する誤差付き接続を与える。ただしM54、M37、初期作用殻、M42衝突bath、clock、記録の単一Hamiltonian統合を仮定に残す。従ってQ3-4Aは条件付き達成である。

**非主張。** 障壁高・幅・入射エネルギーに対する連続的な透過率曲線、半無限散乱極限、透過・反射・未確定を含む完全散乱装置、熱活性化との装置比較、初回通過、吸収器、到達時間分布は固定目標より強い拡張であり、本結果には含めない。

## W型のトンネル振動（Q3-4B）

**固定目標と達成判定。** Q3-4Bは、時間に依存しない対称W型ポテンシャルの障壁値未満にある最低偶・奇二重項から左右局在状態を構成し、外部駆動、傾斜切替、障壁低下を使わず、左右領域の占有率がトンネル分裂に従って半周期で移送され、一周期で戻ることを示す。第3状態との正の間隔、中央障壁領域を含む完全位置分布、有限時間誤差、単一試行の位置読出しへの接続も必要である。

**既存の部分根拠。** M47/R140の最低2モード射影では、零傾斜生成子の固有値差 $E_1-E_0=2J$ から角周波数 $2J/\mathcal J_0$ の左右2モード作用比振動が得られ、完全移送時間は $\pi\mathcal J_0/(2J)$ である。第6.17節の条件付き系は、M37の静的位置ばね網からこの有限時間2モード発展へ進む誤差境界を与える。従って、静的零傾斜、トンネル分裂、半周期の2モード交換という担体部分は得ている。

**残る接続。** R140の「左右占有」は最低2モード基底の作用比である。低2モードの作用比だけを空間領域占有率へ読み替えない。W型全生成子の最低二重項が障壁値未満で第3状態から分離されること、左右局在初期分布、中央を含む全空間分布、M42による同じ粒子の半周期移送と一周期回帰、終位置記録、全誤差を同じ運転で閉じる必要がある。従ってQ3-4Bは部分達成である。障壁高・幅に対する指数的分裂則は固定目標より強い拡張とする。

## 2重スリット干渉（Q3-5）

**固定目標と達成判定。** Q3-5は、有限空間グラフ上の2経路入力について、コヒーレント分布が非干渉混合と異なり、相対位相に応じて位置分布が変化することを示し、位置読出しへ接続する。固定目標名の「2重スリット」は、この最小の2経路干渉を指す。

<!-- theorem-start:theorem -->
**定理（R125：最小2経路干渉と位置読出し）**

2頂点再結合器へ同じ重みのコヒーレント入力と非干渉混合を入れると、有限時刻の位置分布の全変動距離は位相 $\pi/2$ で $1/2$ となる。相対位相 $\pi/2$ と $-\pi/2$ の位置分布距離は1である。各M42/R174運転誤差が $\epsilon$ 以下なら、対応する距離はそれぞれ $1/2-2\epsilon$、$1-2\epsilon$ 以上である。
<!-- theorem-end:theorem -->

**R125の最小2経路再結合器。** 直交入力 $|L\rangle,|R\rangle$ に同じ生成子

```math
h_{\rm int}
=
\kappa
\left(
|L\rangle\langle R|
+
|R\rangle\langle L|
\right)
```

を作用させる。コヒーレント入力と同じ経路重みの非干渉混合は

```math
|\psi_\phi\rangle
=
\frac{|L\rangle+e^{i\phi}|R\rangle}{\sqrt2},
\qquad
\rho_{\rm mix}
=
\frac12
\left(
|L\rangle\langle L|
+
|R\rangle\langle R|
\right).
```

$T_{\rm int}=\pi\mathcal J_0/(4\kappa)$ では

```math
p_\phi
=
\left(
\frac{1+\sin\phi}{2},
\frac{1-\sin\phi}{2}
\right),
\qquad
p_{\rm mix}
=
\left(
\frac12,\frac12
\right).
```

従って

```math
D_{\rm TV}
\left(
p_{\pi/2},p_{\rm mix}
\right)
=
\frac12,
\qquad
D_{\rm TV}
\left(
p_{\pi/2},p_{-\pi/2}
\right)
=
1.
```

第1式はコヒーレント交差項の有無を、第2式は相対位相変更の位置分布への効果を示す。同じSchrödinger型発展を全入力に使っており、入力後に結果依存の生成子を選んでいない。

M42/R174が各理想分布の初期選択から終位置記録までを全変動距離 $\varepsilon_{174}$ 以内で再現すれば、記録分布間の距離はそれぞれ $1/2-2\varepsilon_{174}$、$1-2\varepsilon_{174}$ 以上である。$\varepsilon_{174}<1/4$ を満たす有限パラメータを条件付きで選べるので両方の差が正に残る。完全な証明は付録F.7、G.4、N節に置く。

**達成判定。** R125は、有限グラフの直交2経路入力、同一発展、コヒーレント入力、同じ重みの混合、正のコヒーレンス差、正の相対位相差を与える。R174により、二つの理想分布間距離から各M42運転誤差を差し引いても正なら有限装置で識別できる。ただしM54、M37、初期作用殻、M42衝突bath、clock、記録の単一Hamiltonian統合を仮定に残す。従ってQ3-5は改訂後の固定範囲で条件付き達成である。

**非主張。** 幾何学的な開口、源、シャッター、多画素スクリーン、全検出器のHamiltonian、無検出を含む完全装置、初回到達、吸収、永久記録、反復resetは固定目標より強い拡張であり、本結果には含めない。

## 位相量子化（Q3-6）

**固定目標と達成判定。** Q3-6は、巻数、節、単価性、位相すべりを一貫して扱い、位相量子化の成立条件を示すことで、Wallstrom問題へ限定的に回答する。非零閉路での整数巻数、零点を通らない変形での不変性、節を介した位相すべり、格子細分化に対する安定性、非整数モノドロミーの力学的排除が必要である。

**運用状態。** Q3-6は未達の研究課題として再開している。本版では新しい定理、模型、数値結果を追加せず、達成へ進むための検証線を固定する。単価性を外から仮定する、閉路位相を整数へ丸める、整数巻数を許容条件として直接置く構成を達成としない。

**検証線。** まず、頂点の非零複素包絡から辺位相差を主値で定め、閉路和を整数巻数として読む。零点と反対向き端点を避ける変形に対するhomotopy不変性を示す。次に、区分線形補間または離散Laplacianのエネルギー最小補間を物理的補間として固定し、振幅の正の下界と一様に有界な離散Dirichletエネルギーから、R86の一様細分化で巻数が安定する条件を導く。非整数モノドロミーを許すseamでは、格子幅 $a$ に対して局所エネルギーが少なくとも $a^{-1}$ で発散することを検査し、節が生じる場合だけ位相すべりで巻数変更を許す。この鎖を同じ有限局所構成で閉じて初めて達成候補とする。

**非主張。** 密度と流れだけを基本変数とする一般的な確率力学への完全回答、節を横切る閉路の巻数、外部ゲージ場、多粒子配置空間を含む一般化は主張しない。Q3-2の作用変分または時間対称Newton則が達成されても、Q3-6の大域条件が自動的に従うとは扱わない。

## M47との境界

付録HのM47は、対称W型ポテンシャルの最低2モードについて、固有状態単独でなく重ね合わせの左右2モード作用比が時間振動することを解析的に扱うQ1側のモデルである。この結果はQ3-3CとQ3-4Bの部分根拠になるが、R123--R125の数値または有限グラフ証明をM47の証拠へ読み替えず、M47をQ3-4A、Q3-5の位置読出し根拠にも使わない。

今回の改訂では新しいW型数値解析を追加しない。共通R135とM47のR140は古典作用角と偶奇2モードから得る解析結果であり、M42をQ1へ流用しない。Q3-3CとQ3-4Bは部分達成、Q3-4AとQ3-5はM54--M37--M42の未統合仮定を反映して条件付き達成とする。

M37をQ1制御の物理的主線に用いても、本章の粒子位置現象は別の分岐である。M42の輸送をQ1へ再導入せず、有効信号の終端一致だけから粒子経路の一致を主張しない。

# 第V部　総合評価

# 誤差、資源、反証条件、未完成目標

> **位置づけ：** M54から派生するQ1・Q2、R180 receiver、M37--M42、M50を横断比較し、R181A--R181D、有限資源、反証条件、未完成目標を整理する。


## 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168のray誤差へ同時に加える。
2. R164の有限幅・枝非対称誤差を、R170の作用殻誤差と系列固有instrument誤差へ重ねて入れる。
3. R180Aの同じblock保持偏差を $\varepsilon_{\rm split}$、$\varepsilon_{\rm latch}$、$C_\tau\varepsilon_{\rm block}$ へ重ねて入れる。
4. R180Cの積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。
6. M54の同じtransverse偏差をR181Aのray誤差、R135の初期共分散誤差、系列固有準備誤差へ重ねて入れる。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

## M54/R181A共通開放準備の誤差と資源

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

## 共通R170誤差

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

## Q1の系列固有誤差

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

## Q2-1の誤差と資源

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

## Q2-2の誤差とBell監査

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

## Q3のM37--M42誤差

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

以上である。M54、M37、初期作用殻、M42局所辺bath、clock、終位置記録の単一Hamiltonian統合が残るため、Q3-4AとQ3-5は条件付き達成である。この誤差式をQ3-4Bの周期的W型移送へ流用せず、半周期と一周期の二時刻を含む別の誤差接続を要求する。

## M50の資源発散

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

## Q2の根拠モデル、共通ハードウェア努力目標、資源分類

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

## Q2-3の3量子ビット型二段ゲート合成

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

## Q2-4多項式外部制御による量子出力サンプリング

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

## 反証条件

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
| Q3-2 | 目標とする作用または時間対称Newton則を縮約前に仮定する、外部から仮定したSchrödinger方程式を書き換えるだけで済ませる、前進・後退平均微分と誤差を同じ確率過程上で定義できない |
| Q3-3C | W型低位スペクトルの格子・領域収束を示せない、または同じ固有基底の有限環境純位相緩和と対角占有率保存を閉じられない |
| Q3-4B | 2モード作用比を空間領域占有率へ同一視する、外部駆動・傾斜切替・障壁低下を使う、最低二重項の障壁値未満条件、第3状態との間隔、半周期移送、一周期回帰、位置読出しのいずれかを欠く |
| Q3-6 | 単価性または整数巻数を外部条件として置く、非整数モノドロミーを丸めて除く、節を介した位相すべりと細分化安定性を同じ構成で扱えない |
| R168 | 可変作用集団でray平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| R170 | 混合上界、局所記録の排他性、履歴単射性、正の処理時間のいずれかを満たさない |
| Q2共通ハードウェア努力目標 | 同一装置を主張しながら目標ごとに担体、浴、準備・読出し原理を交換する、または装置族を一様な有限規則で生成できない |
| Q2-3二段ゲート合成 | 第1ゲート後の単一試行状態を破壊せず第2区間へ渡せない、中間共同モーメントから再準備する、GHZ--$T$--逆演算の $1/(2\sqrt2)$ 余裕が全装置誤差を上回らない |
| Q2-4 | 受動モードごとの設定・較正・読出し、指数長の係数表、回路別配線、指数時間または指数精度が必要になる。総bath容量と総熱が指数的であることだけでは反証にならない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 固定目標の残件と実装強化課題

固定目標上の未完成事項は次である。

1. Q1-2について、同じ零傾斜Rabi対照と反復R143/R170測定を接続し、全履歴、tilt対照、有限誤差、資源を含む正のZeno抑制余裕を示す。
2. Q3-2について、M37--M42--有限衝突bathの縮約から、前進・後退平均微分を持つ同じ確率過程と、Nelson流の作用変分または時間対称Newton則を有限時間誤差付きで導く。
3. Q3-3Cについて、W型の有限個の低位固有値・密度・節の格子・領域収束と、同じ固有基底での有限環境純位相緩和をそろえる。
4. Q3-4Bについて、静的零傾斜W型の障壁値未満二重項、第三状態との間隔、全空間占有率、M42位置読出し、半周期移送、一周期回帰を同じ誤差台帳で閉じる。
5. Q3-6について、閉路巻数、homotopy不変性、節を介した位相すべり、R86細分化安定性、非整数seamのエネルギー発散を統合する。
6. Q2-1について、R181Dの容量pointer--作用殻境界、有限fiber混合、固定、記録を単一clock scheduleで閉じる。
7. Q2-3について、同じR181D末端条件を8mode特殊化で閉じ、R177の識別余裕より小さい全装置誤差を選ぶ。
8. Q2-4について、M54の静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、各局所誤差の独立な物理上界を与える。

次は固定目標の達成判定と分けて管理する実装・熱力学的強化課題である。

1. M54のpump、transverse sink、template、clockを有限bath、仕事源、排熱先へ持ち上げ、雑音と準備誤差と総収支を同じ模型で閉じる。
2. R170の作用容量結合、作用殻fiber内平衡化、信号保持、衝突bath、枝固定、記録をQ1・Q2の1つの有限局所Hamiltonianへ統合する。
3. M47のM54準備から結果別状態更新、永久記録、resetまでの周期総収支を閉じる。
4. R180CのM54末端SWAP、setting-pre block latch、paired-Hopf pump・sink、中央切断、2翼局所R170、controller、fresh cell流を同じ具体装置とclockへ統合する。
5. Q3-4A・Q3-5でM54切断面、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録までを同じ有限局所装置へ統合する。
6. 連続空間、多粒子を扱う。
7. Q2共通ハードウェア努力目標として、同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceをQ2-1からQ2-4で共有する一様な装置族を得る。

Q1-1、Q3-1、Q3-3A、Q3-3Bは達成、Q1-2、Q3-3C、Q3-4Bは部分達成、Q2-1、Q2-2、Q2-3、Q2-4、Q3-4A、Q3-5は条件付き達成、Q3-2、Q3-6は未達である。Q2-1とQ2-3の条件はR181Dの末端物理接続、Q2-2の条件はR180Cのreceiver内部単一装置統合、Q2-4の条件はM54部品の一様装置統合へ集約される。Q2共通ハードウェア族は判定外の努力目標として未完成であり、その成否を個別判定へ遡及させない。

## M37からQ1制御へ進む強化課題

新しい主線はM37、W型低2モード、Q1制御の順とする。固定目標の定義やQ2依存関係は変更しない。静的R86と射影内R140の既存達成に加え、第6.17節の区間合成と第3.5.1節の残差を同じ時間窓で閉じる必要がある。

| 誤差・資源 | 数える対象 |
|---|---|
| 包絡誤差 | 全定傾斜区間と有限切替。再準備で区間誤差を消さない |
| 低モード状態誤差 | 漏れ振幅と低モード内位相補正。漏れ確率の二乗評価と区別 |
| 制御誤差 | 合成角、時刻、切替幅、作用の変動、準備誤差 |
| 入力一様性 | 相対位相と初期共通位相を含む実線形写像のノルム |
| 資源 | 全Rabi時間、carrier周波数、間隔、結合強度、制御帯域、外部仕事 |

B.5の漏れ確率を全変動距離へ直接加える旧評価は採用しない。R143の誤差和では、実際の全状態または分布比較を満たす $\varepsilon_{2m}$ を使う。理想2準位担体のQ1-1達成と、全W型・M37実装の任意精度強化は分ける。全W型測定の誤差予算もこの追加条件に依存する。

優先順は、物理係数の対応、静的Rabi、有限傾斜列、準備・読出し境界、共同担体への接続、同一装置の統合である。ゲート列からの有効伝播は補助実装として研究メモで管理し、Q3全過程の独立導出とは呼ばない。

# 結論

> **位置づけ：** M54をQ1・Q2の共通親模型族として整理し、R181A--R181D、R178D、R179、R180 receiver、およびQ3のM37--M42二層模型を総括する。


## 確立したこと

M54は、一様有限正準register、物理source/template port、anti/work、raw・regularized容量、selector、cold/spent bank、記録、clockを持つQ1・Q2の共通親模型族である。R181Aは物理template準備、R181Bは固定2・3入力の可逆tensor-lift、R181Cは永続register上の局所gate列、R181DはR170駆動projector-tree Born instrumentを与える。各試行の複素信号は実正準座標の派生表示であり、解析上のrayや確率表をcontrollerへ書き戻さない。

Q1はM54の $n=1$ W型特殊化である。R181AのW型2モード系は独立結果IDを持たない。共通R135は階数1bath共分散のBloch球、R140は任意の $SU(2)$、零傾斜占有振動、離調Rabi式を与える。R181Dの深さ1とR143が有限コントラストの左右読出しと結果別状態更新を与える。R135、R140によりQ1-1を達成と判定した。

M50/R164は一般有限信号作用を枝容量へ写し、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き状態数が得られることを示す。二乗形の状態依存性はM54が準備するrank-one第2モーメントに現れ、M50/R164は各試行の実担体信号から排他的結果の状態数を作る。この二段を二重の確率源として数えない。R161は条件付きGibbs再平衡化、R162は有限衝突熱浴を与え、その系として条件付き中間状態の正逆経路確率比と相対有効仕事が従う。作用殻明示表示と消去表示を同じ分配関数で二重計数せず、殻自由エネルギー仕事 $W^{\rm sh}$ と相対有効仕事 $W^{\rm rel}$ を区別する。

R143はHopf方向準備、操作面ごとの再平衡化、解析器、傾斜固定、辺閉鎖、M47粒子位置の局所記録、結果別テンプレート交換、測定後再平衡化を合成する有限誤差instrumentである。記録器は統計振幅、共分散、全密度、確率流、遷移率を入力にせず、各試行に存在する $X$ の局所位置だけを読む。R144は固定有限段について永久記録、内部逆計算、外部空セル交換を合成する。解析器中または周期間に配置--信号bath matchingを連続保存することは仮定しない。

Q2-1はM54の $n=2$ 特殊化である。受動的な4mode信号、anti-register、work、clock履歴をbathへ任せ、controllerはport、lift窓、gate種、対象、作用窓、末端読出しだけを指定する。R181Bは一般積入力の可逆tensor-lift、R181Cは同じ永続register上のCNOT、局所操作、逆演算を与える。R181Dは深さ2のprojector-treeを与える。末端の物理境界と一体化を条件としてQ2-1は条件付き達成である。

Q2-2にはM54駆動setting-pre paired-Hopf receiverを採用した。固定singlet源はM54の $|00\rangle\to H_A\to\mathrm{CX}_{A\to B}\to X_B\to Z_A$ で作り、R181C後の実際の1試行末端信号をcanonical SWAPで物理hold信号 $\widetilde V$ としてそのまま中央receiverへ渡す。$V=\widetilde V/\|\widetilde V\|$ は解析上のrayであり、SWAPが状態依存除算を行うわけではない。R180AはA設定basisで $\widetilde V$ を2つのblockへ分解し、物理容量比から枝重み、同じblock作用からB側templateを得る。固定singletでは各枝重みが $1/2$ となり、規格化templateは旧spin-flip fiberをglobal phaseまで回復する。

R180Bは選択したA側・B側templateをsourceとしてpaired-Hopf pump、paired差sink、直交sinkを駆動し、共役位相を持つ2翼rayへ有限時間で整列する。R180Cは中央切断後のfresh局所作用殻と局所応答が完全共通原因に条件付けて積因子化すること、Born共同分布、非信号性、CHSH差、fresh-cell帰還をまとめる。共通原因を平均した大域Bell対数を物理的な切断後ポテンシャルへ戻さない。M54の1試行信号 $\widetilde V$ を使い、集団交差momentまたはR181Cの生成子 $G_S$ を終端共役として再注入しない。

Q3ではM54/R181Aからrank-one初期集団を受け取り得る契約を上流に置き、M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似、作用比診断をR86へまとめる。その上に、各試行で1個の局在粒子位置、局所辺bath、clock、履歴を持つM42を置く。R172はM37有効辺流に沿う等変輸送と有限期待跳躍数、R173は節一様正則化と有限衝突Hamiltonian近似、R174はM54準備、1回の初期R164選択、M37担体、M42輸送、終位置記録の誤差台帳を与える。R123は井戸型と調和型の束縛状態・純位相緩和を与え、Q3-3AとQ3-3Bを達成する。R124とR125は有限障壁の確率移動と最小2経路干渉をM42へ接続し、Q3-4AとQ3-5を条件付き達成とする。終時刻に別のM50位置を再標本化しない。

## 条件付きで確立したこと

R143の結果分布と条件付き状態は、R181Aの信号bath方向準備、R164の作用殻準備、R161の有限時間再平衡化、R162の有限衝突近似と辺閉鎖、傾斜保持、局所記録、枝別テンプレート交換の誤差上界に条件付く。大域階数1共分散だけでは枝別測定後状態が生じないため、結果枝の非規格化共分散を独立に評価した。

Q1-2の測定統計部分は達成している。M54/R181Aがrank-one統計準備、R164がBorn型状態数と有効自由エネルギーの条件付き起源、R143とR144がBorn分布、同軸反復分布、異軸逐次分布を有限誤差で与える。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。有限局所Hamiltonian統合または有限閉鎖Hamiltonianへの持ち上げ、完全周期、永久記録、reset、周期全体の仕事・熱・エントロピー収支は、Q1-2の達成条件ではなく実装・熱力学的強化課題である。連続matching保存または周期間matching帰還も現行測定統計の必要条件ではない。

R180Aはblock代数と理想共同Born則を厳密に与える。R180Bは採用した開放方程式に対して吸引多様体、有限時間率、作用収支を厳密に与える。R180Cは、M54 holdからprojector latchまでの反作用、block source port、paired-Hopf pump・sink、中央切断、2翼R170、記録、fresh-cell帰還を1つの装置とclockで実現できることを条件に、完全結果誤差とBell監査を合成する。一方、切断面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。

固定目標Q2-2全体は条件付き達成である。範囲は固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則、プロトコル面matchingである。一般状態についてR180Aのblock代数とnode処理は与えるが、一般入力族の一様な高精度Bell receiverまでは主張しない。Q2-2の達成判定はQ2-1の達成状態に依存させないが、根拠模型は独立M48でなくM54の具体的singlet源と実信号を使う。

固定目標Q2-3は条件付き達成である。R181Bをgate列の前に2回使って8mode信号を作り、R181CのA--B、B--C二次生成子と逆演算を同じ永続registerへ作用させる。R177のGHZ--$T$--逆演算ではcoherent出力と完全dephasing出力の全変動距離が $1/(2\sqrt2)$ になる。末端ではM50/R164/R170を含むR181Dを8modeへ特殊化し、Q2-1と同じ末端接続条件が残る。

固定目標Q2-4は条件付き達成である。M54は $2^n$ 受動signal modeを許し、R181Cが局所gateをspectator sectorへ一様にbroadcastする。R181Dはraw容量、正則化作用殻、R170 selector、可逆filter、radial-only repumpを深さ $n$ で合成する。完全結果誤差は入力誤差、$n\delta/(1+\delta)$、$2n(\tau+\gamma)$、node誤差の和で抑える。R178Dは結果相関履歴をspentへ残す境界、R179はblank bank、collision cell、selector/filter work、spent bankを供給する。旧apertureとdyadic tapeは現行因果鎖に使わない。

Q2-4では総bath容量と総熱を多項式としない。signal、work、history、cold、spentの受動容量は指数的でもよい。その代わり、外部program、制御channel、精度、反復回数、総時間を多項式に抑え、指数個の個別address、確率表、回路別配線、稀な成功、事後選別を使わない。この限定は通常の効率的古典simulationではない。

## 確立していないこと

M54について未導出なのは、pump、transverse sink、template、clockを具体的な有限bath、仕事源、排熱先から導くこと、雑音付き有限時間誤差、揺らぎ散逸関係、準備portの総仕事・熱・エントロピー生成を閉じることである。R181Aは採用した縮約drift後の厳密結果であり、そのdriftの有限閉鎖Hamiltonian持上げではない。

M47について未導出なのは、M54/R181AのW型2モード系の開放portをW型装置へ統合すること、R164の作用容量結合・fiber内平衡化・枝対称性を有限局所Hamiltonianとして構成すること、R162の衝突散乱と信号bath保持controllerを同じ最小有限Hamiltonianへ統合すること、粗視化された有効仕事・熱を全微視的台帳へ持ち上げてpumpからresetまでの全周期ゆらぎ関係へ拡張することである。時間依存傾斜をM37のミクロ位置ばね網から一様誤差付きで導くこと、連続空間極限、多粒子も未完成である。

R180について未導出なのは、M54末端SWAP、projector作用latch、選択block source port、paired-Hopf pump・sink、R162の衝突粒子位置bath、中央切断、fresh cell流を同じ具体装置とclockへ統合することである。採用したR180B方程式を有限bathから導くこと、一般入力族でnode感度を一様に抑えること、総仕事、総熱、総エントロピー生成を閉じることも未完成である。A設定が中央準備へ入るため、空間的に分離した自由設定Bell実験を再現したとはいえない。

Q1-2のZeno部分は未達であり、同一の零傾斜Rabi対照と反復R143/R170測定を接続する必要がある。傾斜による離調固定、障壁増大、駆動停止、摩擦、事後選別をZeno効果とは呼ばない。Q3-2も未達であり、M37--M42--有限衝突bathの縮約から前進・後退平均微分を持つ確率過程と、Nelson流の作用変分または時間対称Newton則を導く必要がある。目標則またはSchrödinger方程式を外部から仮定して書き換えるだけでは達成としない。Q3-6も未達であり、閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を統合する課題として維持する。

Q3-3CとQ3-4Bは部分達成である。M47/R140は対称W型の最低偶・奇2モード、零傾斜の分裂周波数、2モード作用比の半周期交換を与える。しかしQ3-3Cに必要な有限個の低位スペクトルの格子・領域収束と有限環境純位相緩和、Q3-4Bに必要な中央障壁領域を含む空間占有率、同じM42粒子の半周期移送と一周期回帰、位置読出しは閉じていない。2モード作用比を空間領域占有率へ読み替えない。

Q3-4AとQ3-5は条件付き達成である。有限グラフ現象の代数部分はR124、R125で確立し、R181Aはrank-one初期集団の開放準備、R172--R174は局在トークンの有限時間輸送と記録への接続を与える。一方、M54準備port、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録を同じ有限局所装置へ統合していない。最小率の一意なミクロ選択、正則化零極限の一様資源、同一ハードウェアと統一母測度を持つM0、独立同分布型有限標本統計も未完成である。

Q2-1はM54/M50とR112/R161/R162/R164/R170/R181A--R181D、Q2-2はM54/M50/R180 receiverとR112/R161/R162/R164/R170/R181A--R181D/R180A--R180C、Q2-3はM54/M50とR112/R161/R162/R164/R170/R177/R181A--R181D、Q2-4はM54とR112/R161/R162/R164/R170/R181A--R181D/R178D/R179を根拠とする。独立判定は他のQ2目標の達成ラベルを前提にしないという意味であり、同じ親模型と部品定理を共有できる。

Q2-1からQ2-4に共通する一様なハードウェア族は、判定外の実装努力目標として未完成である。同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceを全目標で共有する構成をまだ得ていないが、この未完成性をQ2-1またはQ2-2の達成状態へ遡及させない。

Q2-4で確立していないのは、M54の静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、局所誤差上界を同時に実現することである。cold bathを閉系から生成すること、有限bankで無期限運転すること、使用済みcellを履歴なしにblankへ戻すこと、指数受動容量または総熱を多項式へ削減することも主張しない。

## 次の決定的検査

Q1-2の次の決定的検査は、同じ総時間の零傾斜Rabi自由対照、測定中もRabi項を止めない有限回測定、flip・reflip・無反応の全履歴、tiltだけの対照を同じ明示的ミクロモデルで比較し、正のZeno抑制余裕が重なり・傾斜・自由発展・1段instrument誤差を上回るかを示すことである。反復回数に伴う時間、記録、fresh cell、エネルギーの増加も同じ台帳で評価する。

これとは別に、M54のpump、transverse sink、template、clockを有限bathへ持ち上げ、R164の作用容量結合、fiber内平衡化、枝対称性と同じW型装置へ統合すること、R162の有限衝突bath、信号bath保持controller、任意軸分析器、傾斜切替、局所記録、枝別テンプレート交換、resetを同じ有限時間Hamiltonian台帳へまとめること、粗視化経路熱力学を周期全体の微視的ゆらぎ関係へ拡張することは、実装・熱力学的強化課題として残る。$\delta\downarrow0$、深いW型、長いfiber準備・混合時間の精度--時間--エネルギー交換もこの強化課題で監査する。

Q2-1とQ2-3の次の検査は、R181Dのcanonical SWAP出口、容量pointer、R164/R170、selector lock、controlled filter、radial repump、recordを共通safe setと単一clock scheduleで閉じることである。Q2-2ではR180CのM54末端SWAP、setting-pre block latch、source port、paired-Hopf pump・sink、R162有限衝突bath、中央切断、2翼controllerを同じ装置とclockへ統合する。Q2-4ではsector漏れ、latch、R170 collision、filter、radial repump、cold floorを同じ安全集合上で同時に抑える。

Q3-2の次の検査は、M37担体、M42粒子、有限衝突bathを一つの開始分布と有限時間縮約へ置き、前進・後退生成子、osmotic速度、current速度を同じ母測度上で定義し、古典ミクロ作用からNelson--Yasue型作用へ進むか、時間対称平均加速度が外力へ一致するかを誤差付きで判定することである。

Q3-3Cでは、W型の低位固有値・密度・節の格子・領域収束と有限環境純位相緩和を追加する。Q3-4Bでは、静的零傾斜W型について最低二重項の障壁値未満条件、第3状態との間隔、中央障壁を含む全空間分布、M42の半周期移送と一周期回帰、位置記録を一つの誤差台帳へまとめる。Q3-4AとQ3-5では、M54切断面をM37初期面へ物理的に接続し、初期R164作用殻、M42の局所辺衝突bath、clock、履歴、終位置記録までを同じ有限局所装置へ統合して総収支を閉じる。

Q3-6では、頂点包絡から辺位相と閉路巻数を定義し、零点を避けるhomotopy不変性、エネルギー最小補間、R86細分化安定性、非整数seamの $a^{-1}$ エネルギー発散、節を介した位相すべりを一つの鎖で検査する。採用した最小率の具体的装置理由と節正則化の資源発散、R180 receiverの空間分離拡張、R123の連続環境極限、R124・R125の散乱・吸収拡張は、それぞれ固定目標と区別して監査する。

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

追加した区間合成と残差受渡しは厳密な誤差接続であるが、全制御族の任意精度構成は未完である。漏れ確率だけによる分布誤差評価を撤回し、全状態差と位相補正を分けた。M0の共通記述、同一装置、全外部流路の閉鎖系化を同じ達成として数えない。

# 付録

# R112有限正準制御・比較・記録の証明

> **位置づけ：** R112の有限ユニタリ回路、時計、滑らかな比較、正準SWAP、記録、逆計算を一つの証明として整理する。Born型枝生成はM50/R164へ分離する。


## 目的と役割境界

R112は有限次元複素信号を実正準座標で制御する共通定理である。証明は次の4節に分かれる。

1. 局所位相回転と隣接2モード交換から有限ユニタリを合成する。
2. 有限時計窓で制御を自律化する。
3. 外部から与えた制御値を滑らかに比較し、遷移帯を無反応へ送る。
4. 正準SWAP、局所記録、テンプレート交換、内部逆計算を行う。

一様選択器角の作用区間長をBorn型頻度と同一視する旧経路は使わない。旧数式、非混合性、再利用反例、退役結果IDは `notes/superseded_m35_born_sampler.md` に置く。R112はM50の作用容量、枝状態数、作用殻fiber内平衡化、粒子位置熱化を代替しない。

## 有限正準信号

$L$ 個の実正準対 $(Q_j,P_j)$ から

```math
d_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}},
\qquad
d=(d_1,\ldots,d_L)^{\mathsf T}
```

を作る。全作用は

```math
J_{\rm sig}=\mathcal J_0d^\dagger d
```

である。Hermitian行列 $h(t)$ に対する2次Hamiltonian

```math
H_h(t)=d^\dagger h(t)d
```

は

```math
i\mathcal J_0\dot d=h(t)d
```

を与え、全作用とLiouville体積を保存する。集団の非中心化第2モーメント

```math
C_d
=
\frac{\mathbb E[dd^\dagger]}{\mathbb E[d^\dagger d]}
```

は $d\mapsto Ud$ の下で $C_d\mapsto UC_dU^\dagger$ と変換する。$C_d$ は集団量であり、R112の単一試行controllerへ入力しない。

## R112の有限unitary合成節

モード $j,k$ の位相回転と交換を

```math
R_j(\varphi)
=
\exp(-i\varphi|j\rangle\langle j|),
```

```math
G_{jk}(\theta,\varphi)
=
\exp
\left[
-i\theta
\left(
e^{i\varphi}|j\rangle\langle k|
+e^{-i\varphi}|k\rangle\langle j|
\right)
\right]
```

とする。対応する実Hamiltonianは $Q_jQ_k+P_jP_k$ 型交換と局所作用項の有限和である。

**R112の有限合成節。**

任意の $U\in U(L)$ は、隣接2モード交換と局所位相回転の有限積として表せる。完全結合を仮定した分解を1次元隣接線へ移す場合も、有限個の隣接SWAPを挿入すればよい。ゲート数は一般の密な $U$ について $O(L^2)$、直列深さは単純構成で $O(L^2)$ である。

各2モードブロックはユニタリなので、対応する実写像はシンプレクティックで全作用を保存する。逆回路はゲート順を反転し、各角を反転して得る。

## R112の有限時計節

時計正準対 $(\tau,P_\tau)$ とcompact支持の窓 $g_r(\tau)$ を使い、

```math
H_{\rm clk}
=
P_\tau
+\sum_{r=1}^R g_r(\tau)G_r
```

とする。$\dot\tau=1$ なので、窓を通過するたびに $G_r$ が有限面積だけ作用する。窓の重なりを避ければ指定順のPoincaré写像を得る。有限幅、面積ずれ、時計初期値ずれは制御誤差へ入れる。

**有限時計による正準回路の自律化。**

固定有限個の2次正準ゲートと滑らかなcontrol gateは、有限個の時計窓を持つ自律Hamiltonianへ埋め込める。初期時計面と使用済み窓を履歴へ残せば、境界失敗を含む拡大写像は1対1である。

## R112の滑らかな比較・無反応節

外部から指定された有限個の互いに素な安全領域 $O_i$ を考える。各領域内部で1、他の安全領域と境界帯で0となる滑らかなplateau関数 $\chi_i(u)$ を選ぶ。安全領域外を正式な無反応 $\varnothing$ とする。

空pointer正準対 $(T_i,P_{T_i})$ に

```math
G_{\rm cmp}
=
\sum_i\chi_i(u)P_{T_i}
```

を作用させれば、安全領域では該当pointerだけが動く。$u$ はprogram番号、枝register、時計面など外部ですでに定まった制御値である。振幅作用から結果確率を作る目的には使わない。

**有限幅比較と完全結果集合。**

有限個の互いに素な安全領域に対し、上の滑らかな比較器を有限Hamiltonian窓として実装できる。異なる安全結果は排他的であり、境界帯、時計ずれ、pointer準備失敗を $\varnothing$ へ送ると結果集合は完全になる。無反応を除いて再規格化してはならない。

## R112の正準SWAP・テンプレート交換節

同じ次元の2つの複素正準register $d,e$ に対し、

```math
G_{\rm sw}
=
\mathcal J_0
\left(
d^\dagger e+e^\dagger d
\right)
```

を面積 $\pi/2$ だけ作用させると、位相規約を除いて2つのregisterを交換できる。空registerへ値を移し、元registerと使用済みcellを履歴へ残すことで情報を消去せず転送する。

結果枝 $i$ に対して事前校正テンプレート $e_i^{\rm tpl}$ を用意し、$\chi_i$ をcontrolとして対応SWAPだけを開けば、結果別状態更新を実装できる。template値は固定装置programであり、集団共分散を測定して単一試行へ書き戻したものではない。

**結果別テンプレート交換。**

固定有限枝と固定有限テンプレートbankについて、排他的safe branchをcontrolとする正準SWAPを有限回路で構成できる。入力情報は使用済みtemplate側に残るため、枝別交換を含む拡大写像は1対1である。

## R112の局所記録・逆計算節

物理枝 $i$ だけに支持を持つ局所関数 $d_i(x)$ と空の記録器 $(D_i,P_{D_i})$ に

```math
G_{\rm rec}
=
\sum_i d_i(x)P_{D_i}
```

を作用させる。理想空pointerで $P_{D_i}=0$ なら、記録中の被測定系への反作用は零である。有限pointer幅と境界帯を記録誤差または無反応へ入れる。

**記録を残した内部逆計算。**

有限回路が入力、時計、pointer、template、使用済みcellを含む拡大系で1対1なら、外部記録を固定したまま、記録前の補助操作を逆順に作用させて内部作業registerを準備集合へ戻せる。ただし入力情報または使用済み状態は外部履歴へ残り、永久記録を有限閉鎖自由度から消去できない。

## 資源と限界

一般の密な $L$ モードunitaryには $L$ 信号正準対、$O(L^2)$ 個の校正ゲート窓、時計、pointer、template、履歴が必要である。固定有限 $L$、固定有限回路、固定精度では全て有限である。永久記録と使用済みcellは試行数に少なくとも比例する。

本付録から次は従わない。

1. 振幅2乗に比例する枝状態数または結果頻度。
2. 作用殻fiber内のGibbs平衡化。
3. 有限熱化した粒子位置の独立同分布性。
4. 未知入力用の自己校正template bank。
5. 無期限反復と永久記録を持つ有限閉鎖装置。
6. R112単独から最終Born型出力が従うこと。Q2-3ではM50/R164/R170を回路末尾に別途接続する。
7. 一般有限 $L$ の合成が量子ビット数に対して多項式外部制御であること。$L=2^n$ の受動モードは許されるが、指数個の個別設定、較正、読出し、指数時間を要するならQ2-4を満たさない。

Born型枝生成はM50/R164、有限再平衡化と記録はR161/R162/R170を正本とする。

# M47傾斜制御測定の証明と誤差評価

> **位置づけ：** R135、R140、R143、R144について、2次元共分散、W型2モード制御、傾斜保持、有限コントラスト、局所記録、枝別状態更新、条件付き周期を証明する。


## 規格化共分散の正準発展

複素2モード正準変数を $Z=(Z_0,Z_1)^{\mathsf T}$ とし、Poisson括弧を

```math
\{Z_j,Z_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

とする。Hermitian行列 $G(t)$ に対するHamiltonian $H_G=Z^\dagger GZ$ は

```math
i\mathcal J_0\dot Z
=
GZ
```

を与える。伝播行列 $U(t,t_0)$ は

```math
i\mathcal J_0\partial_tU
=
G(t)U,
\qquad
U(t_0,t_0)=I_2
```

を満たし、Hermitian性からunitaryである。各試行で $Z(t)=U(t,t_0)Z(t_0)$ なので

```math
\mathbb E[Z(t)Z(t)^\dagger]
=
U
\mathbb E[Z(t_0)Z(t_0)^\dagger]
U^\dagger.
```

分母 $\mathbb E[Z^\dagger Z]$ は保存される。従って

```math
C_Z(t)
=
U(t,t_0)C_Z(t_0)U(t,t_0)^\dagger
```

であり、微分すると $i\mathcal J_0\dot C_Z=[G,C_Z]$ を得る。

## R135の2次元系

2次Hermitian行列はPauli基底で

```math
C_Z
=
\frac12
\left(
\operatorname{tr}C_Z\,I_2
+
\sum_{k=x,y,z}
\operatorname{tr}(C_Z\sigma_k)\sigma_k
\right)
```

と展開できる。$\operatorname{tr}C_Z=1$ なので本文の表示を得る。固有値は

```math
\lambda_\pm
=
\frac12(1\pm|\boldsymbol r|)
```

である。正半定値性は $|\boldsymbol r|\leq1$、階数1は固有値集合が $\{1,0\}$ であることと同値なので $|\boldsymbol r|=1$ である。

階数1なら $C_Z=cc^\dagger$ と因数分解できる。同じ $C_Z$ を与える規格化因子 $d$ は、$C_Z$ の1次元像を張るので $d=e^{i\alpha}c$ である。従って因子空間は $S^3/U(1)=\mathbb{CP}^1$ である。

<!-- theorem-start:proof -->
**証明（R135の2次元系）**

上の固有値計算により階数1条件と単位Bloch球面が同値である。B.1のunitary共役は階数1を保存し、共通位相を変えても $C_Z$ を変えない。従ってM47階数1共分散の有効状態空間はBloch球面であり、古典正準流がその回転を与える。証明終。
<!-- theorem-end:proof -->

## 傾斜W型の2モード行列

偶奇基底で、対称生成子の最低2モード射影は

```math
P_2h_W(0)P_2
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}.
```

$x$ は奇なので

```math
\langle\phi_0|x|\phi_0\rangle
=
\langle\phi_1|x|\phi_1\rangle
=
0.
```

$x_{01}=\langle\phi_0|x|\phi_1\rangle<0$ と本文の左右規約で固定すれば

```math
P_2xP_2
=
x_{01}\sigma_x
```

である。偶奇基底から局在基底へのHadamard変換を $H$ とすると

```math
H\sigma_zH
=
\sigma_x,
\qquad
H\sigma_xH
=
\sigma_z.
```

従って共通項 $\overline E I_2$ を除き

```math
H P_2h_W(F)P_2 H
-
\overline E I_2
=
-J\sigma_x
-
Fx_{01}\sigma_z.
```

従って $\varepsilon=-2Fx_{01}=2F|x_{01}|=F(x_R-x_L)$ であり、本文と同じ符号である。

## R140の可制御性

共通エネルギーは共通位相しか生成しないため除く。傾斜零の反Hermitian生成子を

```math
X_0
=
\frac{iJ}{\mathcal J_0}\sigma_x
```

とし、傾斜差から得る制御方向を

```math
X_1
=
-\frac{i}{2\mathcal J_0}\sigma_z
```

とする。交換子は

```math
[X_0,X_1]
=
-\frac{iJ}{\mathcal J_0^2}\sigma_y
```

である。$J>0$ なら $X_0,X_1,[X_0,X_1]$ は $\mathfrak{su}(2)$ を張る。$SU(2)$ はコンパクトで連結なので、正負の傾斜を含む区分一定制御の到達集合は $SU(2)$ 全体である。固定目標操作ごとに有限積を選ぶ。

一定傾斜では

```math
G
=
-J\sigma_x
+
\frac{\varepsilon}{2}\sigma_z,
\qquad
G^2
=
\left(
J^2+\frac{\varepsilon^2}{4}
\right)I_2.
```

$\Omega_E=\sqrt{J^2+\varepsilon^2/4}$ とすると

```math
e^{-iGt/\mathcal J_0}
=
\cos
\left(
\frac{\Omega_Et}{\mathcal J_0}
\right)I_2
-
i\frac{G}{\Omega_E}
\sin
\left(
\frac{\Omega_Et}{\mathcal J_0}
\right).
```

$|L\rangle=(1,0)^{\mathsf T}$、$|R\rangle=(0,1)^{\mathsf T}$ とすれば、遷移振幅の絶対値2乗は本文の式になる。

<!-- theorem-start:proof -->
**証明（R140）**

Lie代数階数条件から任意の $SU(2)$ 操作が有限傾斜列で到達できる。B.1から各区間は共分散のunitary共役である。一定傾斜の指数行列を展開して左右遷移成分を取れば、Rabi振幅、振動数、離調依存式を得る。証明終。
<!-- theorem-end:proof -->

## 漏れ確率と全状態誤差の分離

$V_2=(\phi_L,\phi_R)$、$P_2=V_2V_2^\dagger$ とし、規格化有効解 $\psi(t)$ と射影生成子 $g_2=V_2^\dagger h_WV_2$ の規格化解 $c(t)$ を比較する。高モード漏れは $\ell_{2m}=\|(I-P_2)\psi\|^2$、全状態差は $d_{2m}=\|\psi-V_2c\|$ であり、同じ量ではない。

固定基底の残差は $B=(I-P_2)h_WV_2$ である。Duhamel公式から、全ての有限時間に

```math
d_{2m}(T)\leq d_{2m}(0)+\frac1{\mathcal J_0}\int_0^T\|B(t)\|\,dt
```

を得る。これは振動相殺を使わない保守的上界である。任意の同じ完全測定への作用比を比較する全変動距離には

```math
\varepsilon_{2m}(T)=\min\{1,d_{2m}(0)+\mathcal J_0^{-1}\int_0^T\|B(t)\|\,dt\}
```

を使える。共分散の場合も、同じ入力集団に一様な状態誤差がある場合に平均して適用する。低モード射影後に成功部分だけを再規格化しない。

静的な間隔と滑らかな切替による $\ell_{2m}=O((v/G)^2+(\mathcal J_0/(G\tau_q))^2)$ は、初期準備・微分・間隔の条件を指定した漏れの次数評価としてのみ使う。一般観測量は低・高モード間の交差項を持ち、誤差が $O(\sqrt{\ell_{2m}})$ になり得る。さらに仮想遷移による低モードの位相差は漏れだけから抑えられない。より鋭い状態評価には補正生成子と残差の評価を必要とする。

## R140の傾斜保持節と尺度選択

一定傾斜の生成子を

```math
G_m
=
-J\sigma_x
+
\frac{\varepsilon_m}{2}\sigma_z,
\qquad
\Omega_m
=
\sqrt{\varepsilon_m^2+4J^2}
```

とする。Bloch球上では、時間発展は単位軸 $\boldsymbol n=(-2J,0,\varepsilon_m)/\Omega_m$ のまわりの回転である。$\Pi_L=(I_2+\sigma_z)/2$ とすると

```math
\left\|
U(t)^\dagger\Pi_LU(t)-\Pi_L
\right\|_\infty
\leq
\frac{2|J|}{\Omega_m}.
```

実際、$z$ 軸の $\boldsymbol n$ に直交する成分の長さは $2|J|/\Omega_m$ であり、回転によるその成分の変化は高々2倍、射影のBloch係数は $1/2$ だからである。従って任意の規格化共分散について左占有率の変化は $2|J|/\Omega_m$ 以下である。

初期共分散が局在射影の場合は、R140の遷移式で正弦2乗は1以下なので、さらに強い上界

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

である。右から左も同じである。保持中の残留散逸、制御揺らぎ、matching driftを $\varepsilon_{\rm hold}$ とすれば、一般入力の2モード内周辺固定誤差は本文の $\varepsilon_{\rm lock}$ で抑えられる。全W型発展と2モード近似の分布距離 $\varepsilon_{2m}$ はこれと別に加え、全W型系の固定中分布誤差を $\varepsilon_{2m}+\varepsilon_{\rm lock}$ とする。

深いW型族で $r=J/G\to0$ とする。$|\varepsilon_m|=G\sqrt r$、$\tau_q=\mathcal J_0/(G\sqrt r)$ を選ぶと

```math
\frac{J}{|\varepsilon_m|}
=
\frac{|\varepsilon_m|}{G}
=
\frac{\mathcal J_0}{G\tau_q}
=
\frac{J\tau_q}{\mathcal J_0}
=
\sqrt r.
```

一般入力の周辺固定項は $2\sqrt r/\sqrt{1+4r}$ 以下、局在射影からの反対井戸遷移は $4r/(1+4r)$ 以下、漏れの次数評価は $O(r)$ であるが、全状態誤差の零収束を意味しない。

<!-- theorem-start:proof -->
**証明（R140の傾斜保持節）**

2モード内の一般入力上界は射影の作用素ノルム評価、局在入力の強い上界はR140の遷移式から従う。B.5の漏れと保持残差を全変動距離の三角不等式で加える。上の尺度選択は射影内の固定誤差を零へ送る。全W型の主張にはB.5の状態誤差を別途小さくする構成を条件とする。証明終。
<!-- theorem-end:proof -->

この証明が抑えるのは各時刻の左右周辺占有率である。同じ試行の $X$ が有限記録時間中に安全井戸を離れないという経路事象は周辺分布だけから従わず、R143ではR162の入射停止と辺ゲート閉鎖からその失敗率 $\varepsilon_{\rm res}$ を別に評価する。

## R143の有限コントラスト補題

対称性により

```math
\langle\phi_0|\Pi_L|\phi_0\rangle
=
\langle\phi_1|\Pi_L|\phi_1\rangle
=
\frac12.
```

従って偶奇基底の効果は本文の $E_L$ である。Hadamard変換で対角化すると固有値は $1/2\pm B_W$ である。$B_W\geq0$ とし、$\eta_W=1/2-B_W$ と置けば

```math
E_L
=
\begin{pmatrix}
1-\eta_W&0\\
0&\eta_W
\end{pmatrix}_{L,R}.
```

分析器後の局在基底対角を $(p_+,p_-)=(p_+,1-p_+)$ とすると

```math
P_L
=
(1-\eta_W)p_+
+
\eta_W(1-p_+)
=
\eta_W+(1-2\eta_W)p_+.
```

差は $\eta_W|1-2p_+|\leq\eta_W$ である。

<!-- theorem-start:proof -->
**証明（R143の有限コントラスト補題）**

上の2次行列計算が理想2モードの有限コントラスト式を与える。分析器、漏れ、matching、固定、無反応、記録による各実分布を中間分布として挿入し、全変動距離の三角不等式を順に使えば本文の誤差和を得る。無反応成分は理想分布側に質量0で追加するため、事後再規格化はない。証明終。
<!-- theorem-end:proof -->

## 大域階数1と枝別共分散の違い

入力共分散が $C_Z=cc^\dagger$ なら、付録L.2の階数1共分散の支持補題により $Z=\alpha c$ がほとんど確実に成り立つ。結果事象 $R=s$ で条件付けても、交換前の $Z$ の方向は $c$ のままである。一般の $c$ は同時に $|L\rangle$ と $|R\rangle$ に平行ではないため、条件付けだけでは2つの測定後固有状態を作れない。

結果別テンプレート交換は、この不足を物理写像として補う。交換前の信号浴を捨てず使用済みテンプレートへ移すので、異なる入力を同じ出力へ不可逆に押しつぶさない。

## 局所記録剪断の正準性

1個の記録セルについて

```math
H_{\rm rec}
=
g(t)P^R\chi(X)
```

とする。単位面積パルスのHamilton方程式は

```math
Q^R_+
=
Q^R_-+\chi(X_-),
\qquad
P^R_+
=
P^R_-,
```

```math
P_{X,+}
=
P_{X,-}
-
P^R_-\nabla\chi(X_-),
\qquad
X_+=X_-.
```

である。これはHamiltonian流なので正準的である。$P^R_-=0$ なら $X$ への反作用は零である。$|P^R_-|\leq\delta_R$ なら反作用は $\delta_R\|\nabla\chi\|$ 以下であり、記録誤差台帳へ入る。

左右の $\chi_s$ は空間的に分離した支持を持つ。安全領域では片方だけが1である。支持が重なる分離面近傍を無反応領域とするため、1試行に2つの排他的安全記録が同時に立つことはない。

## 結果別テンプレート交換

信号浴と枝 $s$ のテンプレートを $Z$、$T_s$ と書く。交換生成子を

```math
G_s
=
i\mathcal J_0
\left(
Z^\dagger T_s
-
T_s^\dagger Z
\right)
```

とする。その角 $\theta$ の流れは

```math
Z_+
=
\cos\theta\,Z_-
+
\sin\theta\,T_{s,-},
```

```math
T_{s,+}
=
-\sin\theta\,Z_-
+
\cos\theta\,T_{s,-}.
```

$\theta=\pi/2$ で完全交換となる。安全枝では局所因子 $\chi_s(X)=1$ がこの結合だけを開き、他枝では零にする。無反応領域では完全固有状態を主張しない。

テンプレート共分散が $|s\rangle\langle s|$ なら、完全交換後の信号共分散も同じである。角誤差 $|\delta\theta|$、テンプレート誤差 $\delta_{\rm tpl}$、分岐漏れ $\delta_{\rm gate}$ がある場合、固定作用殻上でtrace距離は

```math
\varepsilon_{\rm br}
\leq
2|\delta\theta|
+
\delta_{\rm tpl}
+
\delta_{\rm gate}
```

と評価できる。係数2はunitary回転の作用素ノルム評価から取った保守的上界である。

## R143の証明

初期操作面と分析器後操作面へ共通R170を適用する。対応する理想分布を $p^{\rm in}$、$p^{\rm out}$ とし、実分布を $\widetilde p^{\rm in}$、$\widetilde p^{\rm out}$ とすれば

```math
D_{\rm TV}
\left(
\widetilde p^{\rm in},p^{\rm in}
\right)
\leq
\varepsilon_{170}^{\rm in},
\qquad
D_{\rm TV}
\left(
\widetilde p^{\rm out},p^{\rm out}
\right)
\leq
\varepsilon_{170}^{\rm out}.
```

この2項は付録K.6の容量、作用殻、混合、衝突、辺閉鎖、局所記録、無反応を既に含む。B.11ではW型に固有なHopf方向、分析器、2モード漏れ、有限コントラスト、傾斜固定、結果別テンプレート交換だけを追加する。全変動距離の縮小性と三角不等式から

```math
D_{\rm TV}
\left(
p^{\rm obs},p^{\rm id}
\right)
\leq
\varepsilon_{170}^{\rm in}
+\varepsilon_{170}^{\rm out}
+\varepsilon_{\rm Hopf}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\eta_W
+\varepsilon_{\rm lock}
+\varepsilon_{\rm res}
+\varepsilon_{\rm guard}
+\varepsilon_{\rm br}
+\varepsilon_{\rm post}.
```

安全枝ではB.10により信号共分散が $|s\rangle\langle s|$ へ近づく。記録後にR161をtemplate方向へ作用させると、条件付き粒子位置分布は $\pi^\delta(s)$ から $\varepsilon_{\rm post}$ 以内になる。従って枝別共同状態の条件付きGibbs整合誤差は $\varepsilon_{\rm br}+\varepsilon_{\rm post}+O(\eta_W)$ である。

<!-- theorem-start:proof -->
**証明（R143）**

R181AのW型2モード系で信号bath方向を準備し、R170で初期粒子位置枝を作る。衝突熱浴を切ってR140で任意軸を左右基底へ写し、分析器終了後の信号へR170を再適用する。R140の保持節で傾斜保持、R143の補題でW型有限コントラストを評価する。B.9の局所剪断で既存の $X$ を記録し、B.10の結果別正準交換で安全枝の条件付き共分散を作る。最後にtemplate方向へ再平衡化する。共通instrument誤差はR170、M47固有誤差は上の三角不等式、条件付き状態誤差は交換と局在裾の評価で抑えられる。証明終。
<!-- theorem-end:proof -->

この証明は旧連続matching保存を使わない。付録Lの条件付き状態数、付録Kの有限混合率、有限衝突誤差、辺閉鎖誤差を使う。一方、作用容量結合、fiber内平衡化、枝対称性を含む有限局所Hamiltonianと、信号bath保持controllerの完全な反作用は別の未導出事項である。

## 逐次測定誤差

理想2段核を $K_1,K_2$、実核を $\widetilde K_1,\widetilde K_2$ とする。各入力安全状態について

```math
\sup_z
D_{\rm TV}
\left(
\widetilde K_j(z,\cdot),
K_j(z,\cdot)
\right)
\leq
\delta_j
```

なら、核の縮約性から

```math
D_{\rm TV}
\left(
\mu\widetilde K_1\widetilde K_2,
\mu K_1K_2
\right)
\leq
\delta_1+\delta_2.
```

第1段条件付き状態が理想射影からtrace距離 $\delta_{\rm post}$ だけずれる場合、2値効果に対する確率差は $\delta_{\rm post}/2$ 以下である。従って2段誤差は

```math
\delta_1
+
\delta_2
+
\frac12\delta_{\rm post}
```

で抑えられる。同軸では理想反対結果が零であるため、実反対結果は同じ上界以下である。

## 記録後の逆計算とreset

装置内部を $z$、測定前情報を受け取る使用済みセルを $w_s$、外部記録を $R_s$ とする。安全枝の理想写像は概念的に

```math
(z_0,w_0,0_R)
\longmapsto
(z_s,w_s,0_R)
\longmapsto
(z_s,w_s,R_s)
\longmapsto
(z_0,w_s,R_s)
```

である。最後の逆計算は記録剪断と信号テンプレート交換を逆実行せず、時計、傾斜駆動器、比較補助だけを戻す。測定前情報は $w_s$、結果は $R_s$ に残るため、写像は1対1である。

交換resetの漸化式

```math
d_{n+1}
\leq
a d_n+b,
\qquad
a=|\cos\phi|<1,
\qquad
b=\varepsilon_{\rm cyc}+|\sin\phi|\sigma_E
```

を反復すると

```math
d_n
\leq
a^nd_0
+
\frac{1-a^n}{1-a}b
```

となり、本文の上極限を得る。

## R144の証明

固定有限段数 $N$ について、各段の初期再平衡化、分析器、分析器後再平衡化、辺閉鎖、傾斜切替、記録、テンプレート交換、測定後再平衡化を共通時計の重ならない窓へ割り当てる。各段の衝突セル、使用済みテンプレート、記録セルを別に用意すれば、前向き写像は有限個の正準流と有限セル散乱の合成である。観測後、内部補助を逆順に戻し、周期末にfresh-cell交換を行う。

結果分布についてはB.12を反復し

```math
D_{\rm TV}
\left(
p_N^{\rm obs},p_N^{\rm id}
\right)
\leq
\sum_{j=1}^N
\left(
\varepsilon_{{\rm inst},j}
+
\frac12\delta_{{\rm post},j}
\right)
```

を得る。周期末偏差はB.13の上界に従う。固定 $N$ と固定周期数 $K$ なら、必要な記録セルと使用済みセルも有限である。$K\to\infty$ を固定容量で実現するとはしない。

<!-- theorem-start:proof -->
**証明（R144）**

各測定段にR143を適用し、独立な衝突セル、テンプレート、記録セルを割り当てる。有限個の拡大正準流の合成は正準的であり、B.12が前向き分布誤差、B.13が内部帰還誤差を与える。永久記録と使用済み状態を外部セルへ保持するため、内部補助だけを準備集合へ戻せる。証明終。
<!-- theorem-end:proof -->

R144は各段でR164の作用殻準備とR161の有限時間再平衡化を明示的に走らせるため、周期間のmatching保存を仮定しない。ただしfiberとcontrollerを含む周期全体の熱力学収支は本証明に含まれない。

## 連続性障害と無反応

連結な初期領域から滑らかな有限時間Hamiltonian流で得る写像は連続であり、その像は連結である。2つの異なる離散固有状態だけを両方含む像は連結でない。従って、安全な左右結果の間には、遷移領域または無反応領域が必要である。

この一般事実はR112の安全比較・無反応節を使う。M47の局所記録では、分離面近傍、傾斜切替中、高モード漏れが大きい領域を無反応へ含める。無反応率を有限パラメータで厳密零にせず、理想2値分布側へ質量0の第3結果を追加して全変動距離を評価する。

## 資源と適用範囲

1段の装置は少なくとも次を必要とする。

1. 信号浴の2正準対。
2. 左右テンプレートの4正準対。
3. 左右記録ポインターの2正準対。
4. 傾斜制御と共通時計の有限正準対。
5. 粒子位置の局所位置と共役運動量。
6. 条件付き作用殻fiber、容量controller、fiber内混合器。
7. 条件付き障壁controller、辺ゲート、有限衝突セル。
8. 使用済み信号、衝突履歴、制御履歴を保持する外部セル。

これは下界でも最適構成でもない。能動部は固定有限段数と固定観測時間に対して有限、永久記録と使用済み状態は実験周期数 $K$ に対して $O(K)$ 以上である。深いW型極限で $J$ が指数的に小さくなる場合、零傾斜回転時間 $\mathcal J_0/J$ は増大する。$\delta\downarrow0$ では付録Kの有効自由エネルギー幅、衝突流束、混合時間に加え、付録Lの作用殻剛性も増大する。誤差だけを零へ送り、時間、エネルギー、セル数、制御帯域を固定したとは扱わない。

本付録は、W型2モード外の一様連続極限、R164の作用容量結合とfiber内平衡化を含む有限局所Hamiltonian、信号bath保持controllerの完全な反作用、周期全体の微視的熱力学収支、無期限反復、Zeno効果を証明しない。全時刻matching保存は証明対象から外し、操作面ごとの作用殻準備と再平衡化へ置き換えた。

## M37有限時間制御受渡し系の証明

全W型のunitary伝播をUとする。$w=Vc$ は $i\mathcal J_0\dot w=h_Ww-Rc$ を満たすので、同じ初期値からの全W型解 $\psi$ と比較し

```math
\psi(T)-w(T)=U(T,0)(\psi(0)-w(0))
-\frac{i}{\mathcal J_0}\int_0^TU(T,t)R(t)c(t)\,dt
```

を得る。Uのunitarityと $\|c(t)\|=1$ から初期差と残差積分の和で抑え、$\|b-\psi\|\leq\varepsilon_{\rm env}$ を加える。連続な区分微分可能Vでは区間境界の項は相殺する。不連続な基底交換を使う場合は交換写像または跳躍残差を追加し、本式へ無断で含めない。

全modeの実直交変換OをQ,Pへ同時に作用させる写像は正準的であるが、先頭2modeだけへの射影は正準同型ではない。高modeは完全状態に保持する。また座標の定義だけでは別の物理入力端への抽出装置は得られず、M54への転送には相互作用と誤差の追加構成を要する。

# 可逆tensor-lift、永続gate、末端instrumentの証明

> **位置づけ：** R181B/R181Cを有限正準Hamiltonian構成として証明し、R181Dの条件と誤差境界を分離する。


## 実正準表示

$d$ 個の複素modeに共通作用尺度 $J_C>0$ を取り、

```math
 z_r=\frac{Q_r+iP_r}{\sqrt{2J_C}},
 \qquad
 \{Q_r,P_s\}=\delta_{rs}
 \tag{C.1}
```

とする。Hermitian行列 $h=h^\dagger$ に対する実関数

```math
 H_h=z^\dagger hz
 \tag{C.2}
```

のHamilton方程式は

```math
 iJ_C\dot z=hz.
 \tag{C.3}
```

従って有限次元unitary $U$ は、Hermitian対数 $h$ と有限時間pulseを選ぶことで実正準流として実装できる。global phaseも実正準回転であり、末端Born比には影響しない。

## 乗算pulse

source $a_j,b_k$ とtarget正準対 $(x,\pi^x)$、$(y,\pi^y)$ を考える。lift中のHamiltonianを

```math
 H_{jk}
 =\chi(\tau)
 \left[
 \pi^x\sqrt2s_C\operatorname{Re}(a_jb_k)
 +\pi^y\sqrt2s_C\operatorname{Im}(a_jb_k)
 \right],
 \qquad
 s_C=\sqrt{2J_C}
 \tag{C.4}
```

とする。実部と虚部はsourceの実正準座標の2次多項式なので、式(C.4)は有限次数の実Hamiltonianである。

targetを

```math
 x=y=\pi^x=\pi^y=0
 \tag{C.5}
```

から始め、$\int\chi(\tau)dt=1$ とする。$H_{jk}$ は $x,y$ に依存しないから $\pi^x,\pi^y$ は零のままである。そのためsourceに対するHamilton方程式の右辺も零となり、sourceはblank manifold上で不変である。targetは

```math
 x=\sqrt2s_C\operatorname{Re}(a_jb_k),
 \qquad
 y=\sqrt2s_C\operatorname{Im}(a_jb_k)
 \tag{C.6}
```

へ移る。

$w^x=(x+i\pi^x)/s_C$、$w^y=(y+i\pi^y)/s_C$ とすると

```math
 w^x=\sqrt2\operatorname{Re}(a_jb_k),
 \qquad
 w^y=\sqrt2\operatorname{Im}(a_jb_k).
 \tag{C.7}
```

ここで本文式(4.11)は

```math
 S_0^{\mathsf T}JS_0=J,
 \qquad
 \det S_0=1
 \tag{C.8}
```

を満たす。対応する複素modeの変換は

```math
 \begin{pmatrix}Z_{jk}\\G_{jk}\end{pmatrix}
 =
 \frac1{\sqrt2}
 \begin{pmatrix}1&i\\1&-i\end{pmatrix}
 \begin{pmatrix}w^x\\w^y\end{pmatrix}.
 \tag{C.9}
```

式(C.7)を代入すれば

```math
 Z_{jk}=a_jb_k,
 \qquad
 G_{jk}=\overline{a_jb_k}.
 \tag{C.10}
```

を得る。$F^x=s_C\operatorname{Re}(a_jb_k)$、$F^y=s_C\operatorname{Im}(a_jb_k)$ と置くと $Z_{jk}=a_jb_k/\sqrt2$ となるため、式(C.4)の $\sqrt2$ を落としてはならない。

## 可逆性と有限性

Hamiltonian流は拡大位相空間上で1対1である。出力 $Z_S$ だけを残してsource、$G_S$、work、clock履歴を捨てれば見かけ上の非可逆写像になるが、M54はそれらをbath内に保持する。逆順に $S_0^{-1}$ を作用させ、$\chi$ の符号を反転したpulseを通せば式(C.5)へ戻る。

多項式Hamiltonianが大振幅で発散しないよう、安全compact集合 $K$ の近傍で1となる滑らかなcutoff $\eta_K$ を式(C.4)へ掛ける。有限入力次元、有限target数、有限pulse時間では $K$ を通る理想軌道を覆う有限supportを選べる。よって作用、時間、mode数は有限である。

実装Hamiltonian vector fieldを理想場から一様に $\epsilon_X$ だけずらし、同じcompact集合上のLipschitz定数を $L_K$、時間を $T$ とする。Grönwall評価により

```math
 \|\widetilde\Gamma(T)-\Gamma(T)\|
 \leq
 \frac{e^{L_KT}-1}{L_K}\epsilon_X
 +e^{L_KT}\epsilon_{\rm blank}.
 \tag{C.11}
```

$L_K=0$ の場合は第1項を $T\epsilon_X$ と読む。

<!-- theorem-start:proof -->
**証明（R181B）**

式(C.4)--式(C.7)が各targetへの積の書込みを与え、式(C.8)、式(C.9)がそれを $Z_{jk}=a_jb_k$ とanti-modeへ正準的に分ける。全 $(j,k)$ に同じ規則を並列適用すれば $Z_S=a\otimes b$ となる。Hamiltonian流、$S_0$、pulseはすべて可逆であり、保持したsource、anti-register、work、clock履歴と逆順操作から逆写像を得る。有限性と誤差はcutoff構成および式(C.11)から従う。証明終。
<!-- theorem-end:proof -->

## 参照因子と反復lift

R181Bは未知の係数を外部で読み出すのでなく、入力modeとblank targetの局所Hamiltonian couplingで積を生成する。従ってcontrollerのprogramは入力値に依存しない。

第三因子 $c$ に対しては、最初の出力をsourceとして同じ乗算器へ入れ、

```math
 (a\otimes b)\otimes c
 =a\otimes b\otimes c
 \tag{C.12}
```

を得る。最初のliftに属するanti/workも捨てない。有限次元の参照因子 $R$ が存在しても、M54が $R$ に作用しなければ全写像は実正準流の恒等拡張となる。

ただし未知の一般状態を複製するとは主張しない。R181Bの入口契約は独立なQ1 portに与えられた積入力である。すでに非分離な入力は、前段と同じ永続register内でゲートを継続し、再liftしない。

## CNOT生成子

2成分部分空間で

```math
 |d_-\rangle=\frac{|10\rangle-|11\rangle}{\sqrt2},
 \qquad
 \Pi_-=|d_-\rangle\langle d_-|
 \tag{C.13}
```

とする。$\Pi_-^2=\Pi_-$ なので

```math
 e^{-i\pi\Pi_-}
 =I+(e^{-i\pi}-1)\Pi_-
 =I-2\Pi_-.
 \tag{C.14}
```

これは $|10\rangle$ と $|11\rangle$ を交換し、$|00\rangle,|01\rangle$ を固定する。よってCNOTに等しい。式(C.1)の正準座標へ展開すると、定数尺度を除いて本文式(4.17)の差mode oscillatorを得る。

3入力では $K_{AB}$ が各 $c$ sliceの $10c,11c$ を同時に交換し、$K_{BC}$ が各 $a$ sliceの $a10,a11$ を同時に交換する。外部programは $c$ または $a$ を読まず、1つの二次Hamiltonianを指定する。

## 有限gate列の誤差

各gateについてglobal phaseを選び

```math
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \leq\varepsilon_r
 \tag{C.15}
```

とする。unitaryのoperator normが1であることとtelescoping identityから

```math
 \left\|
 \prod_{r=L}^{1}\widetilde U_r
 -e^{i\sum_r\chi_r}
 \prod_{r=L}^{1}U_r
 \right\|_{\rm op}
 \leq\sum_{r=1}^{L}\varepsilon_r.
 \tag{C.16}
```

任意の参照次元について

```math
 \|(\widetilde U_r-e^{i\chi_r}U_r)\otimes I_R\|_{\rm op}
 =
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \tag{C.17}
```

なので同じ評価が成立する。modeまたは経路ごとの誤差を足さず、register全体のoperator normで評価する点が重要である。

式(4.20)の作用窓が交わらず、出口で $g_r=0$ なら、各窓の時間発展を順序積として分けられる。窓間は $H_{\rm hold}$ だけが作用する。状態を別bathへ渡さないので独立のhandoff誤差はなく、hold、clock、leakageとして一度だけ数える。

<!-- theorem-start:proof -->
**証明（R181C）**

式(C.3)により各有限Hermitian生成子は同じ $Z_S$ 上の実正準Hamiltonian流である。CNOTと3入力の二つのCNOTは式(C.13)、式(C.14)およびslice和から従う。非重複clock窓は有限gate列の順序積を与え、式(C.16)が合成誤差、式(C.17)が参照系安定性を与える。全期間にわたり $Z_S$ を保持するため、中間decode、選択、再準備はない。証明終。
<!-- theorem-end:proof -->

## 逆演算診断

入力 $|+0\rangle$ にCNOTを作用させた後、2枝間の位相を保つ場合と完全dephaseする場合を比較する。前者へ逆CNOTとA側Hadamardを作用させると結果は確定的に $|00\rangle$ へ戻る。後者は $|00\rangle$ と $|10\rangle$ を各 $1/2$ で与える。従って完全結果分布の全変動距離は

```math
 \frac12
 \left(
 \left|1-\frac12\right|
 +\left|0-\frac12\right|
 \right)
 =\frac12.
 \tag{C.18}
```

4modeの存在だけではこのfringeを保証しない。永続性、相対位相、逆gate、末端だけの読出しが必要である。

## 容量latch

末端の実信号 $v$ をR112のcanonical SWAPでblank hold-register $V$ へ移す。SWAPは同次元の正準置換であり、係数の推定、枝選択、再準備を含まない。

blank pointer $(A_y,P_y^A)$ に本文式(4.25)を作用させると

```math
 \dot A_y=A_y^\delta(V),
 \qquad
 \dot P_y^A=0.
 \tag{C.19}
```

$P_y^A=0$ では $V$ の方程式にlatch由来のback reactionがない。単位pulse後に

```math
 A_y=J_0
 \left(
 |V_y|^2+\delta q_y\|V\|^2
 \right).
 \tag{C.20}
```

全容量で規格化すると

```math
 \pi_y^\delta(V)
 =\frac{|V_y|^2/\|V\|^2+\delta q_y}{1+\delta}.
 \tag{C.21}
```

よって

```math
 D_{\rm TV}(\pi^\delta(V),\pi^0(V))
 \leq\frac{\delta}{1+\delta}.
 \tag{C.22}
```

$V\mapsto re^{i\phi}V$ は式(C.21)を変えない。

## 末端誤差

理想末端rayを $\widehat v$、実際を $\widehat V$ とし、位相を最適化したnorm誤差を

```math
 \inf_\phi\|\widehat V-e^{i\phi}\widehat v\|_2
 \leq\varepsilon_{\rm ray}
 \tag{C.23}
```

とする。純粋rayの計算基底分布に対するdata-processing評価から、その全変動距離は $\varepsilon_{\rm ray}$ 以下で抑えられる。正則化は式(C.22)、SWAP、latch、shell、mixing、collection、lock、record、clockの有限誤差は合計 $\varepsilon_{170}^{\rm end}$ へ一度ずつ数える。無反応を $\varnothing$ として捨てずに含めれば本文R181Dの境界を得る。

<!-- theorem-start:proof -->
**証明（R181D）**

式(C.19)、式(C.20)が信号を壊さない容量latchを与え、式(C.21)、式(C.22)が正則化Born比とその誤差を与える。ray誤差、末端工程の合成誤差、無反応massに三角不等式を適用すると本文R181Dの境界を得る。R164、R170の有限作用殻と排他的固定を接続できるという仮定の下で成立する条件付き証明である。証明終。
<!-- theorem-end:proof -->

## 残る接続義務

R181Dを無条件の一体定理へ上げるには次を閉じる必要がある。

- canonical SWAP出口と容量pointer入口の共通safe set
- pointer容量からR164作用殻への有限Hamiltonian境界
- R161/R162の有限fiber混合が保つ枝対称性
- collection、lock、recordまでを含む単一clock schedule
- すべてのfailure cellと無反応を含む完全結果空間

これらは一般入力liftや中間coherent decoderの欠落ではない。R181BとR181Cにより、その二つはそれぞれ明示的liftと同じ永続register上のgate列へ置き換わった。

# M54駆動setting-pre receiver周期の証明

> **位置づけ：** R180Aの条件付きblock代数、作用殻選択、node切断、2翼matching、R180Cの局所応答・Bell監査・有限誤差・弱開放帰還を証明する。


## 行優先block分解

canonical SWAP後の物理hold信号と解析上の規格化rayを、行優先で

```math
\widetilde V
=
\operatorname{vec}_{\rm row}(\widetilde D),
\qquad
r=\|\widetilde V\|>0,
\qquad
V
=
\operatorname{vec}_{\rm row}(D),
\qquad
D=\frac{\widetilde D}{r},
\qquad
D
=
\begin{pmatrix}
D_{00}&D_{01}\\
D_{10}&D_{11}
\end{pmatrix}
```

とする。$\widetilde V=v$ は同次元正準SWAPがそのまま移した物理信号であり、$V=\widetilde V/r$ は解析上だけ用いる。A basis変換後の規格化成分は

```math
\left[
\left(
U_x^\dagger\otimes I_2
\right)V
\right]_{s,k}
=
\sum_j
\overline{(u_{s,x})_j}
D_{jk}.
```

右辺を $k$ 成分とする列ベクトルは

```math
w_{s,x}
=
D^{\mathsf T}
\overline{u_{s,x}}
```

である。物理blockは

```math
\widetilde w_{s,x}
=
\widetilde D^{\mathsf T}
\overline{u_{s,x}}
=
r w_{s,x}
```

であり、規格化blockについて

```math
\begin{aligned}
\|w_{s,x}\|^2
&=
u_{s,x}^\dagger
D^*D^{\mathsf T}
u_{s,x}\\
&=
V^\dagger
\left(
|u_{s,x}\rangle\langle u_{s,x}|
\otimes I_2
\right)V.
\end{aligned}
```

$u_{+,x},u_{-,x}$ の完全性から2つのprojectorの和は $I_4$ であり、$\|V\|=1$ なら $p_{+|x}+p_{-|x}=1$ となる。

## R180Aの作用殻選択

R181Dを物理hold信号 $\widetilde V$ と2つの直交projector $\Pi_s^x$ へ適用し、blank pointerへ

```math
A_s
=
\mathcal J_0\widetilde V^\dagger\Pi_s^x\widetilde V
=
\mathcal J_0r^2p_{s|x}(V)
```

をlatchする。理想blank momentumが零なら信号への反作用は零である。有限blank、selector plateau、clock、cutoffによる偏差は $\varepsilon_{\rm latch}$ へ入れる。容量の生成はR181Dの役割であり、R164は次に同じ容量を排他的な作用殻状態数へ写す。

R164の作用殻状態数を

```math
\Omega_s(V,x)
=
C_{\rm sh}A_s
```

とし、枝対称な同じ比例定数 $C_{\rm sh}$ を使う。従って理想平衡枝比では共通radial因子 $\mathcal J_0r^2$ が消え、

```math
\frac{\Omega_s}{\Omega_++\Omega_-}
=
\frac{A_s}{A_++A_-}
=
p_{s|x}(V).
```

R161の平方根型率はこの比を一意定常分布とし、R162が固定有限時間上の有限衝突近似を与える。有限mixing、collision、overflowを無反応込みの $\varepsilon_{\rm latch}$ へ加える。枝選択後に信号と作用殻をdecoupleし、選択pointerだけで対応する物理block $\widetilde w_{s,x}$ をsource portへroutingする。入力係数または $r$ を外部controllerへ公開しない。

選択枝 $s$ について、局所B応答を

```math
P(B=b\mid s,V,x,y)
=
\frac{
|u_{b,y}^\dagger w_{s,x}|^2
}{
p_{s|x}(V)
}
```

とすれば

```math
\begin{aligned}
P(S=s,B=b\mid V,x,y)
&=
|u_{b,y}^\dagger w_{s,x}|^2\\
&=
\left|
\sum_{j,k}
\overline{(u_{s,x})_j}
\overline{(u_{b,y})_k}
D_{jk}
\right|^2\\
&=
\left|
\left(
u_{s,x}^\dagger
\otimes
u_{b,y}^\dagger
\right)V
\right|^2.
\end{aligned}
```

<!-- theorem-start:proof -->
**証明（R180A）**

D.1がblockとprojector作用の等式を与える。R181DのlatchとR164の線形状態数により理想内部枝重みは $p_{s|x}$ となり、R161/R162が有限時間の物理的枝選択を与える。選択枝の条件付きB応答へ $p_{s|x}$ を掛けると上のテンソル積Born重みになる。有限装置では各Markov核と有限正準写像の誤差を完全結果集合上で加える。証明終。
<!-- theorem-end:proof -->

## node切断と方向安定性

$p_{s|x}<\tau$ の枝を無反応へ送ると、その総質量は

```math
\sum_{s:p_{s|x}<\tau}p_{s|x}
\leq
\sum_{s:p_{s|x}<\tau}\tau
\leq2\tau
```

である。これは事後選別率ではなく完全結果分布の無反応質量として数える。

非零ベクトルの規格化写像 $n(w)=w/\|w\|$ について、$\|w\|,\|w'\|\geq\sqrt\tau$ なら

```math
\left\|
n(w)-n(w')
\right\|
\leq
\frac{2}{\sqrt\tau}
\|w-w'\|.
```

従ってhold、splitter、block routingの誤差は安全枝で $C_\tau\varepsilon_{\rm block}$ へ移せる。singletでは全枝で $p_s=1/2$ なので、$\tau<1/2$ に固定すればnode切断は生じず、規格化定数も一様である。

## singlet特殊化

```math
D_{\rm s}
=
\frac{\mathsf E}{\sqrt2},
\qquad
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathsf E^{\mathsf T}=-\mathsf E
```

なので

```math
w_{s,x}
=
D_{\rm s}^{\mathsf T}
\overline{u_{s,x}}
=
-\frac1{\sqrt2}
\mathsf E\overline{u_{s,x}}.
```

$\mathsf E$ はunitaryだから $\|w_{s,x}\|^2=1/2$ である。規格化B方向は $-\mathsf E\overline{u_{s,x}}$ となる。旧M48の $\mathsf E\overline{u_{s,x}}$ との差はglobal signだけであり、projector、W型作用、局所応答を変えない。

## R180 strong fiber

局所fiber $\mathcal F_W^\delta(c)$ では

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)=\pi_i^\delta(z).
```

$\pi^\delta(e^{i\alpha}z)=\pi^\delta(z)$ なので共通位相は粒子位置分布を変えない。R180B終了後の2翼方向誤差は $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ 以下である。固定有限設定族と $p_s\geq\tau$ のcompact安全域では $z\mapsto\pi^\delta(z)$ と局所分析・記録核は射影距離に関して一様Lipschitzである。

paired-Hopf終了後に $z_A,z_B$ を保持し、A、Bの粒子位置bathを条件付き独立に時間 $T_X$ だけ走らせる。R161から各翼の条件付き位置分布は $\pi^\delta$ から $C_Xe^{-\lambda_X^\delta T_X}$ 以内にある。正則化誤差は各翼で $\delta/(1+\delta)$ 以下である。

枝を最大couplingし、連続信号を同じtemplateとpaired位相でcoupleし、離散位置を条件付き最大couplingすれば、理想fiber $\nu_{V,x}^0$ からの結果前誤差は

```math
\begin{aligned}
d_{\rm fib}
\leq{}&
\varepsilon_{\rm latch}
+2\tau
+C_\tau\varepsilon_{\rm block}
+K_{180}e^{-\gamma_{180}T_{\rm PH}}\\
&+
\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}
+\varepsilon_{\rm cut}
\end{aligned}
```

となる。連続信号測度を理想ray支持測度と全変動距離で比較しない。

## 局所応答と非信号性

切断後の完全共通原因 $\Lambda$ に条件付けて

```math
K_{\rm post}^{xy}
=
K_A^x\otimes K_B^y
```

とする。A分析器は $a_{s,x}=u_{s,x}$ を結果 $s$ の井戸へ写す。B分析器の理想応答は

```math
P(B=b\mid s,V,x,y)
=
|u_{b,y}^\dagger b_{s,x}(V)|^2.
```

各分析器終了後に局所信号を固定し、各翼のR170を走らせる。fresh作用殻、衝突cell、noise seed、記録cellが条件付き積なら、二つの局所instrumentも条件付き積になる。$\Lambda$ を切断面測度で平均すると相関は残るが、切断後の直接結合は生じない。

Bの未規格化周辺行列は

```math
\begin{aligned}
\sum_s
w_{s,x}w_{s,x}^\dagger
&=
D^{\mathsf T}
\left(
\sum_s
\overline{u_{s,x}}u_{s,x}^{\mathsf T}
\right)
\overline D\\
&=
D^{\mathsf T}\overline D.
\end{aligned}
```

従ってB周辺は $x$ に依存しない。A周辺はprojector作用 $p_{a|x}$ であり $y$ に依存しない。

singletについて $b_{s,x}$ のBlochベクトルは $-s\boldsymbol n_x$ だから

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
```

$P(s)=1/2$ と $A=s$ を使えば本文の余弦共同分布が従う。

## R180Cの有限誤差

実際の1周期を有限個の核 $K_1,\ldots,K_N$、理想核を $K_1^0,\ldots,K_N^0$ とする。各段の一様全変動誤差が $\epsilon_j$ 以下なら逐次couplingとdata processingから

```math
D_{\rm TV}
\left(
\nu_0K_1\cdots K_N,
\nu_0K_1^0\cdots K_N^0
\right)
\leq
\sum_j\epsilon_j.
```

連続方向誤差は局所応答核の一様Lipschitz定数で結果分布距離へ変換してから加える。$\|\widetilde V\|\geq r_{\min}$ のsafe setでは規格化写像がLipschitzであるため、M54 source、gate、canonical SWAP、holdがrayへ与える偏差を $\varepsilon_{\rm ray}^{54}$ にまとめられる。canonical SWAP自体に除算は含めない。splitter、branch作用、node、block保持、paired-Hopf、位置matching、切断、条件付き積偏差、局所R170、記録、clockを各1回だけ数えると本文の $\varepsilon_{180}^{\rm cyc}$ になる。

周辺化は全変動距離を増やさない。同じ理想周辺から各設定で $\varepsilon_{180}^{\rm cyc}$ 以内なら、反対設定間の周辺差は三角不等式により $2\varepsilon_{180}^{\rm cyc}$ 以下である。

無反応を数値0として相関を定義する。各相関の被積分関数の絶対値は1以下なので、1設定対の相関差は $2\varepsilon_{180}^{\rm cyc}$ 以下、4項のCHSH差は $8\varepsilon_{180}^{\rm cyc}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

R180Aがbranch重みと理想共同Born分布、R180Bが有限時間2翼template matching、D.5が局所粒子位置fiber、D.6が切断後の条件付き積instrumentを与える。各有限段を上のtelescoping境界で合成し、無反応を完全結果集合に残せば本文の全変動距離上界を得る。周辺とCHSHの境界はdata processingと有界観測量評価から従う。fresh-cell帰還はD.9のcontractを別に適用し、観測済み周期へ遡って加えない。証明終。
<!-- theorem-end:proof -->

## 設定依存性の位置

M54 sourceと設定生成角の設定前測度を積に取るため、$V$ の準備法則は実際に生成される $x,y$ に依存しない。一方、$x$ は $U_x^\dagger\otimes I_2$、$\Pi_s^x$、$a_{s,x}$、$b_{s,x}(V)$ を決める。異なる非可換設定では理想fiber $\nu_{V,x}^0$ の支持とbranch分解が異なるので

```math
\mu_{\rm cut}
\left(
d\Lambda\mid V,x,y
\right)
=
\mu_{V,x}(d\Lambda)
```

は一般に $x$ 依存である。従ってBellの測定設定独立性は成立しない。$y$ を中央準備核へ入れず、切断後にB局所核へだけ入れることと、理想B周辺が $x$ に依存しないことは両立する。

## fresh-cell帰還

記録後の能動状態を $Y$、fresh基準状態を $Y_*$ とする。交換核が

```math
E
\left[
d_{\rm ret}(Y',Y_*)
\mid Y
\right]
\leq
r_{\rm ret}d_{\rm ret}(Y,Y_*)
+\epsilon_{\rm fresh},
\qquad
0\leq r_{\rm ret}<1
```

を満たすなら、反復により

```math
E
\left[
d_{\rm ret}(Y_n,Y_*)
\right]
\leq
r_{\rm ret}^n
d_{\rm ret}(Y_0,Y_*)
+
\frac{\epsilon_{\rm fresh}}{1-r_{\rm ret}}.
```

使用済みM54 hold、branch latch、pump、sink、局所作用殻、衝突cellはspent履歴として残す。閉系から無履歴でfresh状態へ戻すとは主張しない。

# M37正常モード変換と局所包絡誤差

> **位置づけ：** R86の正常モード変換、反回転項、作用素誤差、有限時間誤差、作用比診断を証明する。


## 正常モード分解

第6章の剛性行列を

```math
K
=
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
```

とし、$K>0$ を仮定する。実直交行列 $O$ と正の固有周波数 $\omega_r$ により

```math
K
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1^2,\ldots,\omega_L^2
\right)
O
```

と書ける。行列平方根は

```math
\Omega
=
K^{1/2}
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1,\ldots,\omega_L
\right)
O
```

である。

正常座標を $x=Oq$、$\pi=Op$ とすれば、

```math
H_{\rm micro}
=
\sum_{r=1}^L
\left[
\frac{\pi_r^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_r^2x_r^2}{2}
\right]
```

となる。

## 厳密正準振幅

行列表記で

```math
c
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}}\,
\Omega^{1/2}q
+
\frac{i}{\sqrt{M_{\rm osc}}}
\Omega^{-1/2}p
\right]
```

と定める。$\Omega$ は実対称正定値なので、

```math
\left\{c_r,c_s^*\right\}
=
-\frac{i}{\mathcal J_0}
\delta_{rs}
```

が成立する。従って $(c,c^*)$ は複素正準座標である。

逆変換は

```math
q
=
\sqrt{
\frac{\mathcal J_0}{2M_{\rm osc}}
}
\Omega^{-1/2}
\left(c+\overline c\right),
```

```math
p
=
-i
\sqrt{
\frac{M_{\rm osc}\mathcal J_0}{2}
}
\Omega^{1/2}
\left(c-\overline c\right)
```

である。Hamiltonian は

```math
H_{\rm micro}
=
\mathcal J_0
c^\dagger\Omega c
```

となり、

```math
i\dot c
=
\Omega c
```

を得る。

## 厳密回転包絡

搬送回転を除いた

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

を定めると、

```math
i\mathcal J_0
\dot{\widetilde b}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
\widetilde b
```

となる。従って

```math
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

である。また

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
=
\mathcal J_0c^\dagger c
```

は厳密保存量である。

## 局所振幅との正準変換

局所振幅は

```math
a
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}\omega_0}\,q
+
\frac{i}{\sqrt{M_{\rm osc}\omega_0}}p
\right]
```

である。

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2},
\qquad
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

と置く。$q,p$ の表示を代入すると

```math
c
=
U_sa
+
V_s\overline a
```

を得る。$U_s^2-V_s^2=I$ なので逆変換は

```math
a
=
U_sc
-
V_s\overline c
```

である。回転包絡では

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)},
```

```math
b(t)
=
U_s\widetilde b(t)
-
V_se^{2i\omega_0t}
\overline{\widetilde b(t)}
```

となる。

## 局所変換差の上界

$h_0=h_L$ なら

```math
s
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

である。$\eta=2\|h_L\|/(\mathcal J_0\omega_0)<1$ なので、$s$ の固有値は

```math
\left(1-\eta\right)^{1/4}
\leq
s_r
\leq
\left(1+\eta\right)^{1/4}
```

を満たす。

各正の実数 $s_r$ について

```math
\left|
\frac{s_r+s_r^{-1}}{2}-1
\right|
+
\left|
\frac{s_r-s_r^{-1}}{2}
\right|
=
\max
\left\{
s_r-1,
s_r^{-1}-1
\right\}
```

である。従って

$|\log s_r|$ が増えると上式の両項が同時に増え、許容区間では $s_r<1$ 側の最大偏差が $s_r>1$ 側の最大偏差以上である。このため $\|U_s-I\|$ と $\|V_s\|$ の上界を同じ端点で取ることができ、

```math
\left\|U_s-I\right\|
+
\left\|V_s\right\|
\leq
\left(1-\eta\right)^{-1/4}-1
=
\delta_{\rm loc}(\eta)
```

を得る。逆変換と $\|\overline v\|=\|v\|$ から

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}
\left\|\widetilde b(t)\right\|
```

である。$\|\widetilde b(t)\|$ は保存されるので本文の一様上界が従う。

## 生成子の Taylor 上界

```math
X
=
\frac{2h_L}{\mathcal J_0\omega_0}
```

と置く。$h_L$ は実対称なので $X$ を直交対角化できる。各固有値 $x\in[-\eta,\eta]$ に対し Taylor の定理から

```math
\left|
\sqrt{1+x}-1-\frac{x}{2}
\right|
\leq
\frac{x^2}
{8\left(1-\eta\right)^{3/2}}
```

である。従って

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

となる。

## Duhamel 評価

Hermitian 行列 $H_1,H_2$ に対し、

```math
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
=
-\frac{i}{\mathcal J_0}
\int_0^t
e^{-iH_1(t-s)/\mathcal J_0}
\left(H_1-H_2\right)
e^{-iH_2s/\mathcal J_0}
\,ds
```

である。両指数の作用素ノルムは1なので、

```math
\left\|
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
\right\|
\leq
\frac{t}{\mathcal J_0}
\left\|H_1-H_2\right\|
```

を得る。$H_1=h_{\rm ex}$、$H_2=h_L$ とすれば本文第6.7節の上界になる。

局所初期値 $b(0)$ を使う場合は、

```math
\begin{aligned}
\left\|b(t)-e^{-ih_Lt/\mathcal J_0}b(0)\right\|
\leq{}&
\left\|b(t)-\widetilde b(t)\right\|
\\
&+
\left\|
\widetilde b(t)
-e^{-ih_Lt/\mathcal J_0}\widetilde b(0)
\right\|
\\
&+
\left\|
e^{-ih_Lt/\mathcal J_0}
\left[
\widetilde b(0)-b(0)
\right]
\right\|
\end{aligned}
```

と分解し、両端の変換差と中央の生成子差を加える。

## 局所作用変動

```math
e(t)
=
b(t)-\widetilde b(t)
```

と置くと、$\|e(t)\|\leq\delta_{\rm loc}\|\widetilde b(t)\|$ である。従って

```math
\begin{aligned}
\left|
\left\|b(t)\right\|^2
-
\left\|\widetilde b(t)\right\|^2
\right|
\leq{}&
2
\left\|\widetilde b(t)\right\|
\left\|e(t)\right\|
+
\left\|e(t)\right\|^2
\\
\leq{}&
\left(
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
\right)
\left\|\widetilde b(t)\right\|^2.
\end{aligned}
```

$\mathcal J_0$ を掛ければ本文第6.8節の局所作用上界を得る。

## 規格化写像

非零ベクトル $x,y$ に対し、

```math
\left\|
\frac{x}{\left\|x\right\|}
-
\frac{y}{\left\|y\right\|}
\right\|
\leq
\frac{2\left\|x-y\right\|}
{\left\|y\right\|}
```

である。$x=b(T)$、$y=b_L(T)$ とし、

```math
\left\|b_L(T)\right\|
=
\left\|b(0)\right\|
\geq
\left(1-\delta_{\rm loc}\right)
\left\|\widetilde b(0)\right\|
```

を使えば、第6.9節の規格化状態誤差が従う。

## 適用限界

本付録は有限次元、時間非依存、実対称 $h_L$ を扱う。$\eta<1$ は十分条件であり最適条件ではない。負の固有値を持つ $h_L$ も、全剛性が正定値であれば含む。

時間依存行列では各時刻の行列平方根が一般に可換でなく、正常モード基底の回転項が加わる。非線形結合では正常モード生成子自体が状態依存になる。これらへ本文の上界をそのまま適用しない。

## R86：局所回転包絡の厳密方程式の証明

<!-- theorem-start:proof -->
**証明**
規格化座標で Hamiltonian は

```math
H_{\rm micro}
=
\frac{\omega_0}{2}
\left(P^{\mathsf T}P+Q^{\mathsf T}Q\right)
+
\frac{1}{2M_{\rm osc}\omega_0}
Q^{\mathsf T}AQ
```

となる。$Q=\sqrt{\mathcal J_0/2}(a+\overline a)$ を代入し、複素 Poisson 括弧を使うと

```math
i\mathcal J_0\dot a
=
\mathcal J_0\omega_0a
+
h_0
\left(a+\overline a\right)
```

を得る。$b=e^{i\omega_0t}a$ へ移れば結論が従う。
<!-- theorem-end:proof -->

## 有限個の定傾斜区間の合成

区間の開始時刻を $t_r$ とする。R86の座標変換には $e^{2i\omega_0t_r}$ が入るが、ノルム上界は開始位相に依存しない。$k_r=(1-\eta_r)^{-1/4}$ とすると $\|\widetilde b(t_r)\|\leq k_r\|b(t_r)\|$。従って区間の実線形伝播を $S_r$、理想unitary伝播を $U_r$ として

```math
\|(S_r-U_r)y\|\leq a_r\|y\|,\qquad
\|S_r\|\leq1+a_r
```

を全ての実初期座標yへ適用できる。ここで複素表示のノルムは実2L次元のEuclidノルムであり、$S_r$ の複素線形性は仮定しない。

先行区間の相対誤差を $E_{r-1}$ とすると、同じ実状態を次区間へ渡す三角不等式は $E_r\leq(1+a_r)E_{r-1}+a_r$。$E_0=0$ から第6.17節の積上界を得る。途中で正常モードへ再準備する操作は含まない。局所作用と集団第2モーメントへの誤差伝播はR86とR135を参照し、同じ偏差を二重加算しない。

## 滑らかな切替との比較

$Y=(Q,P)$ の実線形生成子を

```math
K_h(t)=\begin{pmatrix}0&\omega_0I\\
-\omega_0I-2h(t)/\mathcal J_0&0\end{pmatrix}
```

とする。区分一定の比較列を $\bar h$ とし、実伝播を $S_h,S_{\bar h}$ とする。対称部分の最大固有値は $\|h(t)\|/\mathcal J_0$ 以下なので、有限区間で

```math
\begin{aligned}
\|S_h(T,0)-S_{\bar h}(T,0)\|
&\leq D_{\rm ramp}(T),\\
D_{\rm ramp}(T)
&=\frac{2}{\mathcal J_0}
\exp\left(\frac1{\mathcal J_0}\int_0^T
\max\{\|h(t)\|,\|\bar h(t)\|\}\,dt\right)
\int_0^T\|h(t)-\bar h(t)\|\,dt .
\end{aligned}
```

これは実伝播のDuhamel公式と対数ノルム評価から従う。固定carrierの回転と正準規格化は同じなので、包絡相対誤差にも使える。滑らかな全W型の有効解を比較対象にする場合は、有効伝播間の差 $\mathcal J_0^{-1}\int\|h-\bar h\|dt$ も加える。

この指数上界は長時間に非常に粗くなり得る。有限切替幅を選べるという形式的事実だけから、現実的な制御帯域や多項式資源を結論しない。より鋭い駆動縮約、同時の高mode抑制、区間の安定性を別に検証する。

# 共通信号集団とM50 ray平均の証明

> **位置づけ：** 共通R135の正確輸送、有限時間誤差、階数1支持と、一般ray平均定理R168を証明する。Q3ではM37包絡誤差をR135へ代入する統計診断として扱い、R168/R170の固定時刻instrumentをM42連続粒子経路と区別する。


## 共通信号集団と受渡し契約

有限試行空間を $(\mathcal P,\mu)$、M37局所包絡を

```math
Z_t(\omega)=b(t;\omega)\in\mathbb C^L
```

とする。全ての期待値は $\mu$ に関して取る。有限で正の集団作用

```math
S_t=\mathbb E[Z_t^\dagger Z_t]
```

を仮定し、

```math
C_Z(t)
=
\frac{\mathbb E[Z_tZ_t^\dagger]}{S_t}
```

と置く。$C_Z$ は集団の自己共分散であり、M50へ直接入力する物理変数ではない。M50へ渡すのは、入力標本時刻 $t_\star$ に各試行が持つ $Z_{t_\star}(\omega)$ またはその正準コピーである。

ここで自己共分散は非中心化された規格化第2モーメントを指す。$\mathbb E[Z_t]=0$ を追加した場合にだけ、通常の中心化共分散と比例して一致する。以下の支持証明に中心化共分散だけを代入してはならない。

R170の完全結果集合は

```math
\mathcal Y=\mathcal I\cup\{\varnothing\}
```

である。$\varnothing$ は零信号、信号閾値未満、比較境界、作用殻準備失敗、衝突数超過、保持失敗、枝固定失敗、記録失敗を含む。無反応を除いて再規格化しない。

入力時刻と出力時刻を

```math
t_\star<t_{\rm out}
```

と固定する。$t_\star$ はM37包絡を採取する時刻、$t_{\rm out}$ はM50熱化、ラッチ、局所記録を終えた時刻である。R170は両者の間に有限の処理時間を必要とする。

## R135の有限時間誤差節の証明

理想有効発展を

```math
U_L(t)=\exp\left(-ih_Lt/\mathcal J_0\right),
\qquad
\widetilde Z_t=U_L(t)\widetilde Z_0
```

とする。$U_L$ はユニタリなので

```math
\widetilde S_0
=
\mathbb E\|\widetilde Z_t\|^2
=
\mathbb E\|\widetilde Z_0\|^2
```

は時間に依存しない。誤差標本を

```math
D_t=Z_t-\widetilde Z_t
```

と書く。R86の一様包絡評価から

```math
d_t
:=
\mathbb E\|D_t\|^2
\leq
\varepsilon_{\rm car}(T)^2\widetilde S_0
```

である。

任意の $x,y\in\mathbb C^L$ について、$d=x-y$ と書けば

```math
xx^\dagger-yy^\dagger
=
xd^\dagger+dx^\dagger-dd^\dagger
```

である。階数1作用素のtrace normが

```math
\|uv^\dagger\|_1=\|u\|\|v\|
```

であることから

```math
\|xx^\dagger-yy^\dagger\|_1
\leq
2\|x\|\|d\|+\|d\|^2
```

を得る。$x=Z_t$、$y=\widetilde Z_t$ とし、Cauchy--Schwarz不等式を使うと、非規格化第2モーメント

```math
A_t=\mathbb E[Z_tZ_t^\dagger],
\qquad
B_t=\mathbb E[\widetilde Z_t\widetilde Z_t^\dagger]
```

について

```math
\|A_t-B_t\|_1
\leq
2\sqrt{S_td_t}+d_t
```

である。

正半定値作用素 $A,B$、$a=\operatorname{tr}A>0$、$b=\operatorname{tr}B>0$ について

```math
\frac12
\left\|
\frac{A}{a}-\frac{B}{b}
\right\|_1
\leq
\frac{\|A-B\|_1}{a}
```

が成り立つ。実際、三角不等式と

```math
|a-b|
\leq
\|A-B\|_1
```

を使えばよい。従って

```math
D_{\rm tr}
\left(
C_Z(t),
\frac{B_t}{\widetilde S_0}
\right)
\leq
2\sqrt{\frac{d_t}{S_t}}
+\frac{d_t}{S_t}.
```

$B_t/\widetilde S_0=U_L(t)C_{\widetilde Z}(0)U_L(t)^\dagger$ である。同じ初期集団を使い $C_{\widetilde Z}(0)=C_Z(0)$ とし、

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置けば

```math
D_{\rm tr}
\left(
C_Z(t),
U_L(t)C_Z(0)U_L(t)^\dagger
\right)
\leq
2\varepsilon_{\rm car}(T)\sqrt{\kappa_T}
+\varepsilon_{\rm car}(T)^2\kappa_T.
```

trace距離は1以下なので右辺を1で切ってよい。$S_0=\widetilde S_0$ かつ局所--正常モード変換が

```math
\|Z_t\|
\geq
(1-\delta_{\rm loc})\|\widetilde Z_t\|
```

を与えるなら $\kappa_T\leq(1-\delta_{\rm loc})^{-2}$ である。従って

```math
q_T
=
\frac{\varepsilon_{\rm car}(T)}{1-\delta_{\rm loc}},
\qquad
r_T\leq2q_T+q_T^2
```

となる。これでR135の有限時間誤差節を得る。正確なunitary輸送は $Z_t=U(t)Z_0$ を第2モーメントへ代入して直ちに従う。

## R168の階数1節の証明

$C_Z(t_\star)=c_\star c_\star^\dagger$、$\|c_\star\|=1$ とする。直交射影 $P_\star^\perp=I-c_\star c_\star^\dagger$ に対して

```math
\frac{\mathbb E\|P_\star^\perp Z_{t_\star}\|^2}{S_{t_\star}}
=
\operatorname{tr}
\left(P_\star^\perp C_Z(t_\star)\right)
=0
```

である。非負確率変数の期待値が零なので

```math
Z_{t_\star}(\omega)
=
\alpha(\omega)c_\star
```

がほとんど確実に成り立つ。安全試行では $\alpha\neq0$ なので、M50のray重みは

```math
w_i\left(Z_{t_\star}\right)
=
\frac{|(\Psi Z_{t_\star})_i|^2}{Z_{t_\star}^\dagger Z_{t_\star}}
=
|(\Psi c_\star)_i|^2
```

である。従って

```math
\pi_i^\delta\left(Z_{t_\star}\right)
=
\frac{|(\Psi c_\star)_i|^2+\delta q_i}{1+\delta}
```

となる。

近似rayを単位ベクトル $\widehat z$、目標rayを $c$ とする。純粋状態trace距離を

```math
s
=
D_{\rm tr}
\left(
\widehat z\widehat z^\dagger,
cc^\dagger
\right)
```

と置く。$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ は1つの有限結果測定を定めるため、trace距離の縮約性から

```math
D_{\rm TV}
\left(w(\widehat z),w(c)\right)
\leq s.
```

正則化は両分布へ同じ $q$ を混ぜるので

```math
D_{\rm TV}
\left(
\pi^\delta(\widehat z),
\pi^\delta(c)
\right)
=
\frac{1}{1+\delta}
D_{\rm TV}
\left(w(\widehat z),w(c)\right)
\leq
\frac{s}{1+\delta}.
```

R135のベクトル誤差から直接ray誤差を作る場合、目標rayを $c$ とし、適切な同位相・同尺度の代表に対して $\|z-c\|\leq q_T<1$ なら

```math
\frac{\|(I-cc^\dagger)z\|}{\|z\|}
\leq
\frac{q_T}{1-q_T}
```

である。左辺は $z$ と $c$ の純粋状態trace距離なので、$\rho_T=q_T/(1-q_T)$ を使える。同じ $q_T$ をR135のtrace誤差とR168のray誤差の双方へ加算してはならない。これでR168を得る。

## R168の一般ray平均、固定作用節、可変作用反例

安全事象 $G$ を固定し、安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

と置く。M50の枝平均は線形性から

```math
P(i)
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
\qquad
P(\varnothing)=P(G^c)
```

である。次に $P(G)=1$ かつ $S(\omega)=Z_{t_\star}(\omega)^\dagger Z_{t_\star}(\omega)=s_*$ がほとんど確実に成り立つとする。$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ に対し

```math
\mathbb E[w_i(Z)]
=
\mathbb E
\left[
\frac{Z^\dagger M_iZ}{s_*}
\right]
=
\operatorname{tr}
\left(
M_i
\frac{\mathbb E[ZZ^\dagger]}{s_*}
\right)
=
\operatorname{tr}(M_iC_Z).
```

正則化項を加えると

```math
\mathbb E[\pi_i^\delta(Z)]
=
\frac{\operatorname{tr}(M_iC_Z)+\delta q_i}{1+\delta}.
```

これは固定作用面で $R_Z^G=C_Z$ となること、従って各試行でray規格化してから平均する操作と、集団第2モーメントを規格化してから枝射影を取る操作が可換であることを示す。

固定作用を外すと一般には可換しない。2次元で、確率 $1/2$ ずつ

```math
Z=\sqrt3e_1,
\qquad
Z=e_2
```

を取る集団を考える。試行ごとのray平均は

```math
R_Z
=
\mathbb E
\left[
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
=
\begin{pmatrix}
1/2&0\\
0&1/2
\end{pmatrix},
```

一方、規格化共分散は

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{\mathbb E[Z^\dagger Z]}
=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}
```

である。従って高階数公式を可変作用集団へ無条件に拡張できない。

一般の正の作用変数 $S=Z^\dagger Z$ と $\overline S=\mathbb E[S]$ について

```math
R_Z-C_Z
=
\mathbb E
\left[
\left(
\frac1S-\frac1{\overline S}
\right)
ZZ^\dagger
\right].
```

$\|ZZ^\dagger\|_1=S$ なので

```math
D_{\rm tr}(R_Z,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{S}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}S}}{\overline S}.
```

最後はCauchy--Schwarz不等式である。枝射影とM50正則化を通した全変動距離は

```math
D_{\rm TV}
\leq
\frac{1}{1+\delta}
D_{\rm tr}(R_Z,C_Z)
```

で抑えられる。これでR168の固定作用節、可変作用反例、半径方向補正を得る。階数1ならF.3により $R_Z^G=P(G)c_\star c_\star^\dagger$ である。

## 入力標本化、保持、作用殻消去表示

M37信号registerを $Z$、同じ次元の空registerを $V$ とする。対応する全ての実正準対を交換する写像

```math
(Z,V)\longmapsto(V,Z)
```

は正準であり、自己逆である。入力面で $V=0$ なら、交換後は $V=Z_{t_\star}$ を保持し、M37側registerは空になる。交換前の値、時計面、保持controllerの状態を履歴へ残せば、閾値判定と保持失敗を含めても拡大写像は1対1にできる。

保持した $V\neq0$ に対し、付録LのM50容量は

```math
A_i^\delta(V)
=
\mathcal J_0
\left[
|(\Psi V)_i|^2
+\delta q_iV^\dagger V
\right]
```

である。2作用殻のLiouville状態数を1回だけ規格化して $\pi_i^\delta(V)$ を得る。R161/R162へ渡すときは殻を消去し、

```math
E_i^\delta(V)=-\Theta\log\pi_i^\delta(V)
```

だけを使う。同じ分配関数内で $\Omega_i^\delta e^{-\beta E_i^\delta}$ を使わない。

作用容量結合、殻内平衡化、枝対称性、保持controller反作用を一つの有限局所Hamiltonianへ統合した定理はまだない。R170は、これらを指定誤差で実行できるという条件付きinstrument定理である。

## 共通R170のQ3固定時刻診断

有限熱化、衝突近似、辺閉鎖、局所記録、履歴単射性の共通証明は付録K.6のR170へ集約する。Q3信号を任意の固定時刻に診断する代替instrumentでは、F.5のSWAPにより $v=V=Z_{t_\star}(\omega)$ を固定し、集団理想分布をR168で評価する。安全事象外は全て $\varnothing$ へ送り、$t_{\rm out}>t_\star$ を保つ。現行Q3の物理経路はM42を初期化して同じ粒子を輸送するため、終時刻R170と同じ運転へ併用しない。

各段階の全変動誤差を合成すると

```math
\begin{aligned}
\varepsilon_{170}
\leq{}&
\varepsilon_{\rm nr}
+\varepsilon_{37\to50}
+\varepsilon_{\rm reg}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm flux}\\
&+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
\end{aligned}
```

を得る。ここで

```math
\varepsilon_{\rm mix}
\leq
C_\delta e^{-\lambda_\delta\tau_X}.
```

$\varepsilon_{37\to50}$ にはR168の階数1ray評価、固定作用等式、半径方向補正の必要なものだけを入れる。同じM37標本偏差を $\varepsilon_{\rm reg}$、$\varepsilon_{\rm cap}$ へ再び入れない。

R168の理想分布は既に $P(\varnothing)=P(G^c)$ を含む。R170固有の実装失敗だけを追加し、上流の無反応質量を再加算しない。これにより成功試行の再規格化なしにQ3特殊化を得る。

## R124とR125に対する固定時刻代替診断

R124の初期読出し分布を $p_0$、終期読出し分布を $p_1$、障壁反対側の理想増分を

```math
p_1(R)-p_0(R)=\alpha>0
```

とする。各読出しのR170誤差が $\varepsilon_{170}$ 以下なら

```math
p_1^{\rm out}(R)-p_0^{\rm out}(R)
\geq
\alpha-2\varepsilon_{170}.
```

従って $\varepsilon_{170}<\alpha/2$ なら正の増分が残る。

R125の2つの理想分布を $p,q$ とし、理想全変動距離を $\Delta$ とする。各R170読出しが誤差 $\varepsilon_{170}$ 以下なら三角不等式から

```math
D_{\rm TV}
\left(p^{\rm out},q^{\rm out}\right)
\geq
\Delta-2\varepsilon_{170}.
```

コヒーレント入力と非干渉混合では $\Delta=1/2$、2つの相対位相入力では $\Delta=1$ なので、$\varepsilon_{170}<1/4$ で両方の差が正に残る。

これらは固定入力時刻の分布を後刻に読む代替instrument接続である。現行Q3のQ3-4A・Q3-5判定は付録NのM42/R174接続を使い、この節のR170を第2の終位置標本器として重ねない。Q3-4BはW型の半周期移送と一周期回帰を同じM42粒子へ接続する別の構成を要求する。いずれの経路も、障壁散乱の初回到達率、吸収率、幾何学的2開口、連続運転スクリーンを構成しない。

## 物理的限界と反証条件

R135、R168とR170の固定時刻診断だけから次は従わない。第3項の有限グラフ版はM42/R172--R174が別の追加模型として扱う。

1. 集団共分散 $C_Z$ を単一試行制御器が直接読むこと。
2. 可変全作用集団で $\mathbb E[ZZ^\dagger]/\mathbb E[Z^\dagger Z]$ と $\mathbb E[ZZ^\dagger/(Z^\dagger Z)]$ が一致すること。
3. 粒子位置が入力時刻以前からM37作用比を追跡すること。
4. M50熱化中の枝軌道がSchrödinger型確率流または物理空間の連続軌道であること。
5. 粒子位置がM37振動子網の全エネルギー、慣性質量、電荷を運ぶこと。
6. 初回到達、吸収、時間積分流束、多粒子位置、連続空間極限。
7. 固定有限精度の同じ装置で $\delta\downarrow0$ を取れること。
8. 作用殻fiber、衝突bath、信号保持、局所記録、resetの総仕事・総熱収支が閉じること。

固定作用公式が可変作用反例で破れない、入力時刻と出力時刻を同一視しない、作用殻状態数を二重計数しない、無反応を除いて再規格化しない、同じM37誤差を複数回加算しないことが本付録の監査条件である。

## 制御されたM37の共通位相と階数1診断

M37の局所包絡は共役成分を含む実線形発展である。一般には $b(t;e^{i\alpha}b_0)=e^{i\alpha}b(t;b_0)$ は厳密には成り立たない。従って初期 $Z_0=\alpha c$ の階数1集団に対して、局所包絡の第2モーメントが厳密に階数1を保つとは主張しない。

第6.17節の入力一様な相対誤差をF.2の二乗平均誤差へ代入すれば、有効unitary輸送からの偏差をR135で抑えられる。別の方法として安全作用下で試行ごとの方向誤差をR168へ直接渡してよい。同じ偏差を両経路の和として数えない。局所作用は実際の読出し入口で評価し、射影後の成功試行だけを再規格化しない。M37の共通位相依存は制御精度の検査対象であり、新しい確率源ではない。

# Q3-3A・Q3-3B・Q3-4A・Q3-5の詳細形と証明

> **位置づけ：** 第7章で一度だけ宣言したR123--R125について、井戸型・調和型の低位束縛状態、純位相緩和、有限障壁の確率移動、最小2経路干渉の証明を与える。


## 記法と証明範囲

本付録では、第7章の定理文を再掲するのではなく、その簡潔な定理文に対応する完全な仮定と結論を示してから証明する。Q3-3AとQ3-3Bでは1次元井戸型・調和型ポテンシャルの有限個の低位状態と、有限個の環境正準対を読まない純位相緩和を構成する。Q3-4Aでは3頂点鎖、Q3-5では2頂点再結合器を使う。後2者については第6.12--6.14節と付録NのM42/R174へ全変動距離で接続する。Q3-3CとQ3-4Bの未完成部分は本付録のR123--R125から補わない。

源、シャッター、幾何学的開口、散乱状態、吸収器、初回到達時刻、多画素スクリーン、永久記録、全検出器のHamiltonianは本付録の仮定にも結論にも入れない。

## R123の証明：束縛状態とエネルギー保存型純位相緩和

**証明で用いる設定と評価。**

正数 $\ell,m,\omega,\mathcal J_0$ と有限モード数 $K$ を固定する。

1. 区間 $(0,\ell)$ のDirichlet井戸を $N$ 個の内部格子点で離散化すると、生成子 $h_N^{\rm well}$ は単純固有値

```math
E_{k,N}^{\rm well}
=
\frac{2\mathcal J_0^2}{ma^2}
\sin^2
\left(
\frac{k\pi}{2(N+1)}
\right),
\qquad
a=\frac{\ell}{N+1},
\qquad
1\leq k\leq N
```

と規格化固有ベクトル

```math
u_{k,N}(j)
=
\sqrt{\frac{2}{N+1}}
\sin
\left(
\frac{k\pi j}{N+1}
\right)
```

を持つ。固定 $k$ について固有値、格子密度 $|u_{k,N}(j)|^2/a$、節の位置は連続Dirichlet井戸の値へ収束し、固有値誤差は $O(a^2)$ である。
2. 区間 $(-L,L)$ のDirichlet格子に調和型ポテンシャル $m\omega^2x^2/2$ を置いた生成子 $h_{N,L}^{\rm osc}$ は単純固有値を持ち、第 $k$ 固有ベクトルはちょうど $k$ 回符号を変える。固定 $k<K$ について、$a\to0$、$L\to\infty$ とすると

```math
E_{k,N,L}^{\rm osc}
\longrightarrow
\mathcal J_0\omega
\left(k+\frac12\right)
```

であり、密度と節位置も対応するHermite--Gauss状態へ収束する。適切な正数 $C_k,c_k$ により誤差は

```math
\left|
E_{k,N,L}^{\rm osc}
-
\mathcal J_0\omega
\left(k+\frac12\right)
\right|
\leq
C_k
\left(
a^2+e^{-c_kL^2}
\right)
```

と抑えられる。
3. いずれかの模型の先頭 $K$ モードの作用を $I_n=\mathcal J_0|b_n|^2$ とし、環境に $K$ 個の正準対 $(\theta_n,P_n)$ を置く。自律Hamiltonian

```math
H_{\rm deph}
=
\sum_{n=0}^{K-1}
\frac{E_n}{\mathcal J_0}I_n
+
\sum_{n=0}^{K-1}
\frac{P_n^2}{2M_n}
+
\frac{\lambda}{\mathcal J_0}
\sum_{n=0}^{K-1}
I_nP_n
```

を採用する。$\lambda>0$ とし、初期環境運動量を互いに独立な $P_n=\pm p_*$ の等重み集団で調製し、系の初期調製とは独立にする。環境を読まずに縮約した相関行列 $C_{nm}(t)$ は

```math
C_{nn}(t)=C_{nn}(0),
```

```math
C_{nm}(t)
=
C_{nm}(0)
\exp
\left[
-\frac{i(E_n-E_m)t}{\mathcal J_0}
\right]
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
\qquad n\neq m
```

を満たす。従って

```math
T_{\rm dec}
=
\frac{\pi\mathcal J_0}{2\lambda p_*}
```

で全ての非対角相関が厳密に零となり、対角占有率は全時刻で厳密に保存される。任意の $0<\delta<1$ に対し

```math
\mathcal W_\delta
=
\left[
T_{\rm dec}
-
\frac{\mathcal J_0}{\lambda p_*}
\arcsin\sqrt\delta,
\quad
T_{\rm dec}
+
\frac{\mathcal J_0}{\lambda p_*}
\arcsin\sqrt\delta
\right]
```

では非対角減衰因子が $\delta$ 以下である。最初の完全コヒーレンス回復時刻は

```math
T_{\rm rec}
=
\frac{\pi\mathcal J_0}{\lambda p_*}
=
2T_{\rm dec}
```

である。全Hamiltonianと注目系エネルギーはともに保存されるが、注目系は環境と相互作用し、環境を読まないため縮約記述では開放系である。

<!-- theorem-start:proof -->
**証明（R123）**

井戸型生成子を

```math
(h_N^{\rm well}u)_j
=
\frac{\mathcal J_0^2}{2ma^2}
\left(
2u_j-u_{j-1}-u_{j+1}
\right),
\qquad
u_0=u_{N+1}=0
```

とする。正弦加法公式を代入すれば定理の固有対を直接得る。$1\leq k\leq N$ で正弦の引数は厳密に増えるため固有値は単純で、第 $k$ ベクトルは $k-1$ 個の節区間を持つ。固定 $k$ で $\sin x=x+O(x^3)$ を使うと

```math
E_{k,N}^{\rm well}
=
\frac{\mathcal J_0^2\pi^2k^2}{2m\ell^2}
+O(a^2)
```

となる。$u_{k,N}/\sqrt a$ の区分線形補間は $\sqrt{2/\ell}\sin(k\pi x/\ell)$ へ一様に収束するので、密度は $L^1$ で、単純な内部零点は位置について収束する。

調和型生成子は

```math
(h_{N,L}^{\rm osc}u)_j
=
\frac{\mathcal J_0^2}{2ma^2}
\left(
2u_j-u_{j-1}-u_{j+1}
\right)
+
\frac12m\omega^2x_j^2u_j
```

である。これは全ての副対角成分が非零の実対称三重対角行列なので固有値は単純であり、離散Sturm振動定理により第 $k$ 固有ベクトルは $k$ 回符号を変える。

格子ベクトルの区分線形補間をDirichlet区間の関数とみなす。差分運動エネルギーは補間関数の微分二乗積分に一致し、ポテンシャル項はRiemann和として収束する。従って離散二次形式は連続区間の二次形式へ上からも下からも収束する。上からの評価には先頭 $k+1$ 個の連続固有関数の格子標本を、下からの評価にはエネルギー有界列の弱コンパクト性を使う。min--max原理により各固定低位固有値と固有空間が収束する。固有値が単純なので位相を選べば固有ベクトル自体が収束し、密度の $L^1$ 収束と単純零点の収束が従う。中心差分の局所切断誤差は滑らかな固有関数上で $O(a^2)$、区間外のHermite--Gauss尾部は $O(e^{-c_kL^2})$ なので、孤立固有値の摂動評価から表示した上界を得る。

次に純位相緩和を示す。$H_{\rm deph}$ はモード位相と環境角 $\theta_n$ に依存しないため、Hamilton方程式から

```math
\dot I_n=0,
\qquad
\dot P_n=0,
\qquad
i\mathcal J_0\dot b_n
=
(E_n+\lambda P_n)b_n
```

を得る。従って

```math
b_n(t)
=
b_n(0)
\exp
\left[
-\frac{i(E_n+\lambda P_n)t}{\mathcal J_0}
\right].
```

$n\neq m$ では独立な2個の二点運動量を平均するため

```math
\mathbb E
\exp
\left[
-\frac{i\lambda(P_n-P_m)t}{\mathcal J_0}
\right]
=
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
```

$n=m$ では因子は1である。これで縮約相関式が従う。$T_{\rm dec}$、$\mathcal W_\delta$、$T_{\rm rec}$ は余弦因子へ代入すればよい。

$I_n$ と $P_n$ が全て一定なので、$H_{\rm deph}$、注目系エネルギー $\sum_nE_nI_n/\mathcal J_0$、各占有率 $I_n/\sum_mI_m$ は厳密に保存される。一方、$\lambda\neq0$ では系の位相速度が読まない環境運動量に依存する。従って全系は有限自由度の閉じたHamiltonian系だが、その環境を縮約した注目系はエネルギー交換を伴わない開放系である。
<!-- theorem-end:proof -->

## R124の証明：3頂点有限障壁の障壁値未満確率移動

**証明で用いる設定と評価。**

正数 $\kappa,V$ に対し、頂点集合を障壁手前 $\{L\}$、障壁 $\{B\}$、障壁反対側 $\{R\}$ に分け、生成子を

```math
h_{\rm bar}
=
\begin{pmatrix}
0&-\kappa&0\\
-\kappa&V&-\kappa\\
0&-\kappa&0
\end{pmatrix}
```

とする。障壁値を $V$ とし、

```math
E_-
=
\frac{V-\sqrt{V^2+8\kappa^2}}{2},
\qquad
\alpha
=
\left(
1+\frac{E_-^2}{2\kappa^2}
\right)^{-1/2}
```

と置く。零固有ベクトル $a=(|L\rangle-|R\rangle)/\sqrt2$ と、$E_-$ の規格化固有ベクトル

```math
v_-
=
\frac{\alpha}{\sqrt2}
\left(
|L\rangle+|R\rangle
\right)
-
\frac{E_-\alpha}{\sqrt2\kappa}
|B\rangle
```

から

```math
b_0
=
\frac{a+v_-}{\sqrt2}
```

を調製する。この初期状態は

```math
\mathbf 1_{[V,\infty)}
(h_{\rm bar})b_0
=
0
```

を満たす。有限時刻

```math
T_{\rm bar}
=
\frac{\pi\mathcal J_0}{|E_-|}
```

では

```math
p_R(0)
=
\frac{(1-\alpha)^2}{4},
\qquad
p_R(T_{\rm bar})
=
\frac{(1+\alpha)^2}{4},
```

従って

```math
p_R(T_{\rm bar})-p_R(0)=\alpha>0
```

である。M42/R174の初期選択と終位置記録から得る分布 $q_t$ が $t=0,T_{\rm bar}$ の各理想位置分布から全変動距離 $\varepsilon_{174}$ 以内なら

```math
q_{T_{\rm bar}}(R)-q_0(R)
\geq
\alpha-2\varepsilon_{174}.
```

従って $\varepsilon_{174}<\alpha/2$ なら記録後にも正の増分が残る。

<!-- theorem-start:proof -->
**証明（R124）**

$s=(|L\rangle+|R\rangle)/\sqrt2$ とすると、$a$ は固有値0を持ち、$\{s,|B\rangle\}$ 上の行列は

```math
\begin{pmatrix}
0&-\sqrt2\kappa\\
-\sqrt2\kappa&V
\end{pmatrix}.
```

残る固有値は

```math
E_\pm
=
\frac{V\pm\sqrt{V^2+8\kappa^2}}{2}
```

である。$E_-<0<V<E_+$ なので、$b_0$ のスペクトル支持 $\{E_-,0\}$ は障壁値 $V$ より真に低い。表示した $v_-$ は直接代入により $E_-$ 固有ベクトルであり、$\alpha$ の定義により規格化されている。

$T_{\rm bar}$ では $a$ の位相は変わらず、$v_-$ の位相は $-1$ になる。従って

```math
b(T_{\rm bar})
=
\frac{a-v_-}{\sqrt2}.
```

$R$ 成分を取ると、初期振幅は $(\alpha-1)/2$、終期振幅は $-(1+\alpha)/2$ である。二乗差は $\alpha$ となる。初期の反対側裾を零と置かず、その厳密値を基準にしている。

全変動距離が $\epsilon$ 以下なら任意事象の確率差は $\epsilon$ 以下である。初期と終期の2回について三角不等式を使えば、読出し増分は理想増分から最大 $2\epsilon$ だけ減り得る。これで結論を得る。
<!-- theorem-end:proof -->

## R125の証明：2頂点再結合器のコヒーレンス差と位相差

**証明で用いる設定と評価。**

直交する2経路入力を有限グラフの頂点 $|L\rangle,|R\rangle$ とし、同一のSchrödinger型生成子

```math
h_{\rm int}
=
\kappa
\left(
|L\rangle\langle R|
+
|R\rangle\langle L|
\right),
\qquad
\kappa>0
```

を使う。コヒーレント入力と同じ経路重みの非干渉混合を

```math
|\psi_\phi\rangle
=
\frac{|L\rangle+e^{i\phi}|R\rangle}{\sqrt2},
\qquad
\rho_{\rm mix}
=
\frac12
\left(
|L\rangle\langle L|
+
|R\rangle\langle R|
\right)
```

とする。有限時刻

```math
T_{\rm int}
=
\frac{\pi\mathcal J_0}{4\kappa}
```

の位置分布は

```math
p_\phi
=
\left(
\frac{1+\sin\phi}{2},
\frac{1-\sin\phi}{2}
\right),
\qquad
p_{\rm mix}
=
\left(
\frac12,\frac12
\right).
```

特に

```math
D_{\rm TV}
\left(
p_{\pi/2},p_{\rm mix}
\right)
=
\frac12,
\qquad
D_{\rm TV}
\left(
p_{\pi/2},p_{-\pi/2}
\right)
=
1.
```

M42/R174が各入力の理想分布から全変動距離 $\varepsilon_{174}$ 以内なら、記録分布間の距離はそれぞれ $1/2-2\varepsilon_{174}$ 以上、$1-2\varepsilon_{174}$ 以上である。従って $\varepsilon_{174}<1/4$ なら、コヒーレント入力と混合の差、および相対位相変更による差がともに正に残る。

<!-- theorem-start:proof -->
**証明（R125）**

$\sigma_x=|L\rangle\langle R|+|R\rangle\langle L|$ と書けば、$\sigma_x^2=I$ なので

```math
U(T_{\rm int})
=
\exp
\left(
-\frac{i h_{\rm int}T_{\rm int}}{\mathcal J_0}
\right)
=
\frac{I-i\sigma_x}{\sqrt2}.
```

$|\psi_\phi\rangle$ へ作用させて各成分の絶対値を二乗すると表示した $p_\phi$ を得る。混合は $I/2$ であり、任意のユニタリ発展後も $I/2$ のままである。2点分布の全変動距離は第1成分差の絶対値に等しいため、一般に

```math
D_{\rm TV}
\left(
p_\phi,p_{\rm mix}
\right)
=
\frac{|\sin\phi|}{2},
```

```math
D_{\rm TV}
\left(
p_\phi,p_{\phi'}
\right)
=
\frac{|\sin\phi-\sin\phi'|}{2}.
```

$\phi=\pi/2$ と $-\pi/2$ を代入すれば理想距離を得る。各読出し分布に全変動距離 $\epsilon$ の誤差がある場合、三角不等式により2分布間距離は理想距離から最大 $2\epsilon$ だけ小さくなる。これで結論を得る。
<!-- theorem-end:proof -->

## 達成範囲の切り分け

R123は、束縛固有状態の選択、冷却、射影収縮を導かない。有限環境の純位相緩和なので、コヒーレンスは $T_{\rm rec}$ で回復する。主張するのは $\mathcal W_\delta$ 内の有限時間減衰と、全時刻での対角占有率保存である。

R124は半無限散乱の透過率ではない。初期状態は厳密な低エネルギー部分空間に属し、初期右裾を含む基準値からの増分を示す。$V/\kappa$ が大きいと、初期右確率と障壁占有率は小さく、移動時刻は長くなる。

R125は固定目標で定めた最小2経路干渉である。幾何学的2開口装置または連続運転スクリーンへの拡張ではない。後2結果の粒子接続はM42/R174を使い、M54、M37、初期作用殻、M42 bath、記録までの単一Hamiltonian統合を条件に残す。

# M47単一Hopf準備

> **位置づけ：** M47の単一Hopf準備をM54/R181AのW型2モード特殊化として示す。閉鎖信号集団の第2モーメント輸送と2次元幾何は共通R135、W型占有振動はR140の特殊化として付録Fと本文第3章へ集約する。


## 目的と主張範囲

本付録は、対称なW型ポテンシャルの最低2モードsectorで、単一試行信号bath $Z\in\mathbb C^2$ を準備し、閉鎖正準流で回転させる部分だけを扱う。粒子位置のBorn型分布、有限熱化、局所記録はM50/R170が操作面ごとに構成する。信号bathの統計核から連続粒子位置rateを作る規則は使わない。

| 段階 | 内容 | 結果 |
|---|---|---|
| 開放準備 | M54による目標rayの位相円への有限時間吸引 | R181AのW型2モード系 |
| 閉鎖伝播 | 2作用角の共分散回転 | R135 |
| W型診断 | 統計核対角の左右占有振動 | R140の零傾斜特殊化 |

本筋から外した計算と旧連続matching線は、論文外の研究メモとGit履歴に保存する。いずれも現行R143またはR170の仮定に使わない。

## W型作用素と最低2モード

有限の対称1次元格子または有界区間上で、M37の古典振動子網から得る実対称包絡生成子を

```math
h_W
=
\frac{\mathcal J_0^2}{2m}L_W+V_W
```

とする。最低2モードの単純固有対を

```math
h_W\phi_0=E_0\phi_0,
\qquad
h_W\phi_1=E_1\phi_1,
\qquad
E_0<E_1
```

とし、$\phi_0$ を実偶、$\phi_1$ を実奇、両者を規格化直交とする。2モード埋込みは

```math
\Phi c=c_0\phi_0+c_1\phi_1,
\qquad
c\in\mathbb C^2
```

である。左井戸射影を $\Pi_L$ とし、対称分割で

```math
\langle\phi_0,\Pi_L\phi_0\rangle
=
\langle\phi_1,\Pi_L\phi_1\rangle
=
\frac12,
\qquad
B_W=\langle\phi_0,\Pi_L\phi_1\rangle
```

と置く。

## R181AのW型2モード特殊化

2モード対角行列を

```math
D_W
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}
```

とする。目標規格化係数 $c_*$ の閉鎖回転軌道と射影を

```math
c_*(t)
=
\exp
\left[
-\frac{iD_W(t-t_*)}{\mathcal J_0}
\right]c_*,
\qquad
\Pi_*(t)=c_*(t)c_*(t)^\dagger
```

と置く。共通M54へ $m=2$、$G=D_W$、$c(t)=c_*(t)$ を代入すると、準備portが開いた区間の採用有効方程式は

```math
\dot z
=
-\frac{i}{\mathcal J_0}D_Wz
+
\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-
\kappa(I_2-\Pi_*(t))z
\right]
```

である。$g>0$ は動径供給と飽和、$\kappa>0$ は目標rayから外れた成分の散逸である。各試行の実体は2個の実正準担体、template、pump、sink、clockである。$z$ は実担体の派生複素座標、$c_*$ と $c_*c_*^\dagger$ はtemplate設定および試行集団の統計記述であり、追加の物理場ではない。

有効準備時間を

```math
\tau(t)=\int_{t_*}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とし、回転座標を $\widetilde z=ac_*+p$、$c_*^\dagger p=0$ と分解する。雑音零では

```math
\frac{da}{d\tau}
=
g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p.
```

$a_0\neq0$、$q_0=\|p_0\|^2/|a_0|^2$、$y=|a|^{-2}$ と置くと

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\tau}
```

であり、$\kappa\neq g$ では

```math
y(\tau)
=
1
+(y_0-1)e^{-2g\tau}
+\frac{gq_0}{g-\kappa}
\left(e^{-2\kappa\tau}-e^{-2g\tau}\right).
```

$\kappa=g$ では最後の項を $2gq_0\tau e^{-2g\tau}$ に置き換える。

<!-- theorem-start:corollary -->
**系（R181AのM47 W型2モード特殊化）**

$g,\kappa>0$、$a_0\neq0$ とする。上の雑音零の採用開放方程式では

```math
\widetilde z(\tau)
\longrightarrow
e^{i\arg a_0}c_*.
```

$|a_0|\geq a_*>0$、$\|\widetilde z_0\|\leq R_*<\infty$ の有界seed集合では有限定数 $K_{47}$ が存在し、

```math
\operatorname{dist}
\left(
\widetilde z(\tau),
\{e^{i\alpha}c_*:\alpha\in[0,2\pi)\}
\right)
\leq
K_{47}e^{-\gamma_{47}\tau},
\qquad
\gamma_{47}=\min\{2g,\kappa\}.
```

同じseed境界を持つ集団の規格化bath第2モーメント $C_z(\tau)$ についても、有限定数 $K_C$ を選び、

```math
\|C_z(\tau)-c_*c_*^\dagger\|_1
\leq
K_Ce^{-\gamma_{47}\tau}
```

とできる。
<!-- theorem-end:corollary -->

<!-- theorem-start:proof -->
**証明**

$a$ と $p$ の方程式を割ると $p/a=(p_0/a_0)e^{-\kappa\tau}$ を得る。$y$ の線形方程式を積分すると上の厳密解が従い、$y\to1$、$p/a\to0$ となる。有界seed集合では係数を一様に抑えられる。外積の収束を平均し、分母が十分大きい $\tau$ で零から離れることを使えば第2モーメント上界を得る。証明終。
<!-- theorem-end:proof -->

この証明は付録MのR181A証明を $m=2$ へ制限したものである。R181AのW型2モード系をM54とは別の準備機構として数えず、共通のpump、transverse sink、port切断のW型特殊化として扱う。

$a_0=0$ の直交超平面は不変である。その質量はseed失敗または無反応として残す。R181AのW型2モード系は雑音付き定常測度、位相拡散、粒子位置周辺、作用殻準備を導かない。

## 共通R135のM47特殊化

準備portを切った後の古典Hamiltonianを

```math
H_{\rm rot}
=
\sum_{n=0}^1\frac{E_n}{\mathcal J_0}I_n
```

とする。正準関係から $\dot I_n=0$、$\dot\theta_n=E_n/\mathcal J_0$ であり、各試行で

```math
Z_n(t)
=
e^{-iE_n(t-t_0)/\mathcal J_0}Z_n(t_0)
```

となる。

**R135の2モード特殊化。**

$\mathbb E[Z^\dagger Z]>0$ とし、非中心化された規格化第2モーメントを

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{\mathbb E[Z^\dagger Z]}
```

とする。このとき

```math
i\mathcal J_0\dot C_Z=[D_W,C_Z]
```

であり、trace、正値性、rankは保存される。$C_Z(t_0)=c_0c_0^\dagger$ なら

```math
C_Z(t)=c(t)c(t)^\dagger,
\qquad
c(t)
=
\exp
\left[-\frac{iD_W(t-t_0)}{\mathcal J_0}\right]c_0.
```
<!-- theorem-start:proof -->
**証明（R135の2モード特殊化）**

各試行で $Z(t)=U(t)Z(t_0)$ であり、$U$ はユニタリである。従って分母は一定、$C_Z(t)=U(t)C_Z(t_0)U(t)^\dagger$ である。微分すればcommutator式を得る。証明終。
<!-- theorem-end:proof -->

## R140の零傾斜W型占有振動

rank-one因子を

```math
c(t_0)
=
\begin{pmatrix}
a_0e^{-i\theta_0(t_0)}\\
a_1e^{-i\theta_1(t_0)}
\end{pmatrix},
\qquad
a_0^2+a_1^2=1
```

とし、$\delta(t)=\theta_1(t)-\theta_0(t)$ と置く。

**R140の零傾斜特殊化。**

R135のrank-one因子に対する統計核の対角は

```math
\rho_{\rm stat}(x,t)
=
a_0^2\phi_0(x)^2
+a_1^2\phi_1(x)^2
+2a_0a_1\phi_0(x)\phi_1(x)\cos\delta(t)
```

である。左井戸への積分は

```math
P_L^{\rm stat}(t)
=
\frac12+2a_0a_1B_W\cos\delta(t),
```

```math
\delta(t)
=
\delta(t_0)
+\frac{E_1-E_0}{\mathcal J_0}(t-t_0)
```

となる。従って角周波数と周期は

```math
\Omega_W=\frac{E_1-E_0}{\mathcal J_0},
\qquad
T_W=\frac{2\pi\mathcal J_0}{E_1-E_0}.
```
<!-- theorem-start:proof -->
**証明（R140の零傾斜特殊化）**

$\Phi c(t)$ の絶対値2乗を展開し、対称井戸の対角積分と $B_W$ を代入すれば従う。証明終。
<!-- theorem-end:proof -->

この $\rho_{\rm stat}$ は信号bath第2モーメントの空間核であり、それだけから単一試行粒子位置 $X$ の分布または経路は従わない。R143は各操作面でM50/R170を適用し、実在する粒子位置を別に準備して記録する。

## 現行Q1への接続と限界

現行Q1は次の順序を使う。

1. R181AのW型2モード系で単一試行信号bathの方向を準備する。
2. R135とR140で有限正準操作を行う。
3. 各操作面でR170を適用し、M50枝状態数から粒子位置を再平衡化して局所記録する。
4. R143でW型有限コントラスト、傾斜固定、結果別テンプレート交換を合成する。

従って全時刻の粒子位置--信号bath matching保存は不要である。本付録からは、採用Hopf方程式の具体的回路導出、作用容量結合、作用殻fiber内平衡化、信号保持反作用、周期総収支、独立同分布型結果列は従わない。

# M54 source-driven setting-pre paired-Hopf receiver

> **位置づけ：** M54の選択blockを単一試行sourceとして使う決定論的開放receiverを定義し、R180Bのpaired位相、template方向、有限時間吸引率、作用収支を証明する。有限閉鎖Hamiltonian liftとR180Cの装置統合は主張しない。


## 目的と旧M48からの変更

旧M48は設定前の内部等重みseedをA設定に応じた2枝へroutingし、固定spin-flip tensorからsinglet型2翼rayを作った。現行receiverではこの独立sourceを使わない。M54の実際の1試行末端信号を物理hold信号 $\widetilde V$ としてA設定basisでblock分解し、R180Aが選んだblockを物理sourceとしてpaired-Hopf流へ渡す。$V=\widetilde V/\|\widetilde V\|$ は解析上のrayであり、canonical SWAPに状態依存除算を含めない。

従って本付録では、試行集団の交差moment

```math
\mathbb E
\left[
z_Az_B^{\mathsf T}
\right]
```

を計算して単一試行templateへ書き戻さない。旧M48で必要だったHaar seed、等重みcell、安全盆 $h_x=0$、設定別seed tableも現行主線から外れる。branch重みはM54信号のprojector作用 $p_{s|x}(V)$ から生じる。

M54のhold signal、branch pointer、選択block port、receiver carrier、pump、sink、clockは別の物理自由度として数える。解析上の方向 $b=w/\|w\|$ は、controllerが未知係数を測って書き込む命令ではない。選択された未規格化block $w$ を固定portから注入し、Hopf飽和が動径を標準化する。

## template分解

安全枝について規格化templateを

```math
a,b\in\mathbb C^2,
\qquad
a^\dagger a=b^\dagger b=1
```

とする。2翼receiver信号 $z_A,z_B\in\mathbb C^2$ を

```math
c_A=a^\dagger z_A,
\qquad
p_A=(I_2-aa^\dagger)z_A,
```

```math
c_B=b^\dagger z_B,
\qquad
p_B=(I_2-bb^\dagger)z_B
```

と分ける。従って

```math
z_A=c_Aa+p_A,
\qquad
z_B=c_Bb+p_B,
\qquad
a^\dagger p_A=b^\dagger p_B=0.
```

paired scalarを

```math
m
=
\frac{c_A+\overline{c_B}}2,
\qquad
d
=
\frac{c_A-\overline{c_B}}2
```

と置く。逆変換は

```math
c_A=m+d,
\qquad
c_B=\overline m-\overline d
```

である。$d=0$ かつ $p_A=p_B=0$ なら

```math
z_A=ma,
\qquad
z_B=\overline m b.
```

$|m|=1$ では2翼が同じ位相を反対符号で持つpaired fiberになる。

標準source loadでは、branch pointerが既知の $a=u_{s,x}$ をA carrierへ送り、M54の選択blockを係数読出しなしにB carrierへ注入する。

```math
z_A(0)=a,
\qquad
z_B(0)=w_{s,x}=\sqrt{p_{s|x}}\,b.
```

このとき

```math
p_A(0)=p_B(0)=0,
\qquad
m_0=\frac{1+\sqrt{p_{s|x}}}{2},
\qquad
d_0=\frac{1-\sqrt{p_{s|x}}}{2}.
```

$p_{s|x}\geq\tau$ なら $m_0\geq(1+\sqrt\tau)/2>0$ であり、下の吸引に必要な非零bright seedを独立に仮定する必要はない。一般入口状態に対する定理は有限source-load偏差も許す。

## 採用開放方程式

準備portの窓関数を $\lambda_{\rm PH}(t)\geq0$ とし、有効時間を

```math
\tau_{\rm PH}(t)
=
\int_{t_{\rm in}}^t
\lambda_{\rm PH}(s)\,ds
```

とする。以下ではdotを $\tau_{\rm PH}$ 微分とする。

```math
\dot m
=
g(1-|m|^2)m,
\qquad
\dot d
=
-\kappa_{\rm p}d,
```

```math
\dot p_A
=
-\kappa_\perp p_A,
\qquad
\dot p_B
=
-\kappa_\perp p_B,
\qquad
g,\kappa_{\rm p},\kappa_\perp>0.
```

元のreceiver信号では

```math
\dot z_A
=
\left[
g(1-|m|^2)m
-\kappa_{\rm p}d
\right]a
-\kappa_\perp p_A,
```

```math
\dot z_B
=
\overline{
\left[
g(1-|m|^2)m
+\kappa_{\rm p}d
\right]
}b
-\kappa_\perp p_B.
```

準備窓中は $a,b$ をtemplate holdで固定する。窓終了後に $\lambda_{\rm PH}$ を零へし、$z_A,z_B$ を局所holdへ移して中央couplerを切る。有限hold誤差と切替反作用はR180Cの条件へ残す。

各項の役割は次の通りである。

| 項 | 役割 | 外部境界 |
|---|---|---|
| $g(1-|m|^2)m$ | paired bright modeへのpumpと単位動径飽和 | pump sourceとlimiterを必要とする |
| $-\kappa_{\rm p}d$ | 2翼のpaired位相差を減衰 | dark sinkへ作用を送る |
| $-\kappa_\perp p_A$ | A template直交成分を減衰 | A transverse sinkを必要とする |
| $-\kappa_\perp p_B$ | B template直交成分を減衰 | B transverse sinkを必要とする |
| $\lambda_{\rm PH}$ | source port、pump、sinkの接続と切断 | clock、切替仕事、残留相関を外部帳簿へ残す |

## exact solutionと有限時間率

$R=|m|^2$ とすると

```math
\dot R
=
2g(1-R)R.
```

$m_0\neq0$ なら

```math
R(\tau)
=
\frac1{
1+
\left(
R_0^{-1}-1
\right)e^{-2g\tau}
}.
```

$\dot m/m$ は実数なので $m$ の位相は保存される。$\alpha=\arg m_0$ とすれば

```math
m(\tau)
=
e^{i\alpha}\sqrt{R(\tau)}.
```

他の成分は

```math
d(\tau)
=
e^{-\kappa_{\rm p}\tau}d_0,
```

```math
p_A(\tau)
=
e^{-\kappa_\perp\tau}p_A(0),
\qquad
p_B(\tau)
=
e^{-\kappa_\perp\tau}p_B(0)
```

である。

有界初期集合

```math
0<r_-
\leq
|m_0|
\leq
r_+<\infty,
```

```math
|d_0|
\leq
d_+,
\qquad
\|p_A(0)\|
\leq
p_+,
\qquad
\|p_B(0)\|
\leq
p_+
```

を固定する。logistic解から有限定数 $C_r$ を選んで

```math
\left|
\sqrt{R(\tau)}-1
\right|
\leq
C_re^{-2g\tau}
```

とできる。従って

```math
\begin{aligned}
\left\|
z_A-e^{i\alpha}a
\right\|
&\leq
C_re^{-2g\tau}
+d_+e^{-\kappa_{\rm p}\tau}
+p_+e^{-\kappa_\perp\tau},\\
\left\|
z_B-e^{-i\alpha}b
\right\|
&\leq
C_re^{-2g\tau}
+d_+e^{-\kappa_{\rm p}\tau}
+p_+e^{-\kappa_\perp\tau}.
\end{aligned}
```

本文の $K_{180}$ と $\gamma_{180}$ は例えば

```math
K_{180}
=
2C_r+2d_++2p_+,
\qquad
\gamma_{180}
=
\min
\left\{
2g,\kappa_{\rm p},\kappa_\perp
\right\}
```

と選べる。

<!-- theorem-start:proof -->
**証明（R180B）**

$R=|m|^2$ のlogistic方程式、$m$ の位相保存、$d,p_A,p_B$ の線形減衰を上の通り解く。template分解の逆変換へ代入し、三角不等式と有界初期集合を使えば2翼の有限時間吸引上界を得る。証明終。
<!-- theorem-end:proof -->

## 作用様量と開放収支

```math
N_{\rm rec}
=
|m|^2+|d|^2+
\|p_A\|^2+
\|p_B\|^2
```

と置く。採用流から

```math
\dot N_{\rm rec}
=
2g(1-|m|^2)|m|^2
-2\kappa_{\rm p}|d|^2
-2\kappa_\perp
\left(
\|p_A\|^2+
\|p_B\|^2
\right)
```

を得る。$|m|<1$ ではpumpからbright作用が入り、$|m|>1$ ではlimiter側へ戻る。paired差と直交成分はsinkへ流れる。この式はreceiver内部の局所作用収支であり、M54 source、branch latch、template hold、clock、切断器、局所測定、記録、fresh交換を含む総エネルギー保存式ではない。

位相体積の収縮、sink entropy、設定情報流、切替仕事を零とはしない。温度、熱流、微視的環境Hamiltonianを指定していないため、熱力学量の総和を閉じない。

## singletと旧paired fiber

singletではR180Aから

```math
a=u_{s,x},
\qquad
b=-\mathsf E\overline{u_{s,x}},
\qquad
p_{s|x}=\frac12
```

を得る。R180Bの吸引先は

```math
z_A
=
e^{i\alpha}u_{s,x},
\qquad
z_B
=
-e^{-i\alpha}
\mathsf E\overline{u_{s,x}}.
```

B側のglobal signを位相 $\alpha\mapsto\alpha+\pi$ またはtemplate位相へ吸収すれば、旧M48のspin-flip paired fiberと同じ局所ray、作用、Born応答になる。

ただし生成機構は異なる。旧M48は内部fair seedと設定別安全盆routingから枝を作った。R180ではM54信号のprojector作用が枝重みを作り、選択block自体がB templateを運ぶ。従って旧交差momentを現行M54信号と同一視しない。

## 開放模型監査

| 監査項目 | R180Bで明示する内容と限界 |
|---|---|
| 状態 | $m,d,p_A,p_B$ と物理template hold $a,b$ |
| 初期条件 | $m_0$ は零から離れ、全成分を有限compact集合に制限する |
| 雑音 | paired-Hopf流自体は決定論的。白色雑音、Itô規約、定常確率測度を使わない |
| 駆動と散逸 | bright pump、paired差sink、2つのtransverse sink、準備窓を分ける |
| source | M54の選択された未規格化blockを物理portから受ける。係数表を外部入力しない |
| 有限時間 | $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ で評価する |
| 切断 | template hold、pump、sinkを切り、2翼局所holdへ渡す。反作用評価はR180Cの条件 |
| 熱力学 | $N_{\rm rec}$ の局所収支だけを計算し、総仕事・総熱・総entropyは未閉鎖 |
| ミクロ由来 | 全driftは現象論的に採用する。具体的流体、回路、振動子bath、有限閉鎖Hamiltonianからは未導出 |

## 反証条件と非主張

次のいずれかが必要ならR180Bの物理的receiver解釈は成立しない。

- M54の未知block係数を外部で測定してからtemplateを書き込む。
- 選択blockを集団momentへ縮約し、別試行のcarrierを再準備する。
- template holdの反作用が有限時間誤差内に抑えられない。
- $m_0=0$ を有限時間で自発的に非零へすることを上の方程式だけから要求する。
- node枝を捨てて成功試行だけを再規格化する。
- R180B単独から切断後局所性、Born branch状態数、記録、reset、総熱力学を結論する。

R180Bはsource-driven paired-Hopf吸引だけを閉じる。M54 hold、projector latch、source port、pump、sink、2翼R170を同じ装置へ統合する条件はR180Cに残す。

# Q2永続共同bathの合成契約

> **位置づけ：** R181Bの反復tensor-lift、R181Cの同一8mode状態bath、R181Dの末端instrument、R177のGHZ--T--逆演算証人を統合し、2入力M54信号をR180 receiverへ渡す境界を区別する。


## 目的と適用範囲

本付録はQ2-1とQ2-3を同じ機構で動かす契約を定める。三つのQ1型port $A,B,C$ から、R181Bをgate列の前に2回作用させて

```math
 Z_{ABC}=a\otimes b\otimes c\in\mathbb C^8
 \tag{J.1}
```

を作る。その後はR181Cにより同じ物理的状態bathへA--B、B--C、局所gate、逆gateを順に作用させ、R181Dにより末端だけを読む。

ここで「同じ機構」とは、mode数が常に4であることではない。固定された有限入力数に対応する受動的な内部modeをbathに任せ、外部controllerはport、gate種、対象、作用窓だけを指定することを意味する。

## 1試行状態と集団momentの分離

$Z_{ABC}$ は同じ試行の実正準座標から得る8成分信号である。2入力の $Z_{AB}$ と、第5章R180がholdする $V=Z_{\rm out}/\|Z_{\rm out}\|$ も同じ種類の1試行信号である。Q2-2では $V$ をA設定basisで物理的にblock分解し、選択blockを同じ試行のreceiver sourceとして渡す。

一方、試行集団の交差moment

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]
 \tag{J.2}
```

を推定して $Z_{AB}$、$Z_{ABC}$ またはR180のtemplateへ戻す操作は再準備である。Q2-1、Q2-2、Q2-3の状態受渡しには使わない。旧M48のBell周期は式(J.2)からsinglet型射影を作ったが、現行Q2-2の根拠から退役し、R180は実際のM54信号を直接受ける。

3入力liftの拡大状態は概念上

```math
 \Gamma_{ABC}
 =(Z_{ABC},G_{AB},G_{ABC},W_{AB},W_{ABC},\tau,H,R)
 \tag{J.3}
```

と書く。anti-registerとwork/historyは読出し対象ではないが、可逆性のため保持する。

## 内部modeと外部interface

| 区分 | 役割 | 外部制御 |
|---|---|---|
| $Z_{ABC}$ | 8modeの永続状態bath | 個別modeをaddressしない |
| $G,W,H$ | anti、source、work、clock履歴 | 読出し・resetしない |
| gate窓 | 固定二次Hamiltonianを開閉 | gate種、対象port、時間だけ |
| 末端bath | hold、容量、作用殻、固定、記録 | 回路末尾だけ接続 |

内部に8つの複素modeがあることは、それ自体では指数長の外部registerを意味しない。Q2-3は入力数が固定された有限benchmarkである。一般の $N$ 入力でmode数が $2^N$ になるtensor-lift反復の一様性はここでは主張しない。Q2-4は同じM54親模型のroot-mode・sector-broadcast特殊化で扱う。

## 二つのgate zone

R181Cの生成子を

```math
 \begin{aligned}
 K_{AB}
 &=\frac14\sum_c
 \left[
 (Q_{10c}-Q_{11c})^2
 +(P_{10c}-P_{11c})^2
 \right],\\
 K_{BC}
 &=\frac14\sum_a
 \left[
 (Q_{a10}-Q_{a11})^2
 +(P_{a10}-P_{a11})^2
 \right]
 \end{aligned}
 \tag{J.4}
```

とする。第1式はC因子を読まずにA--B CNOTを、第2式はA因子を読まずにB--C CNOTを実装する。clock Hamiltonian

```math
 H_{\rm tot}
 =P_\tau+H_{\rm hold}
 +g_{AB}(\tau)K_{AB}
 +g_{BC}(\tau)K_{BC}
 \tag{J.5}
```

で2つのcompact作用窓を交わらないようにする。B portは第1gateの出力と第2gateの入力を兼ねるが、中間handoff mapは存在しない。

## GHZ--T--逆演算証人

初期状態を $|000\rangle$ とし、AへHadamardを作用させる。前向き列は

```math
 |+00\rangle
 \xrightarrow{\operatorname{CX}_{A\to B}}
 \frac{|000\rangle+|110\rangle}{\sqrt2}
 \xrightarrow{\operatorname{CX}_{B\to C}}
 \frac{|000\rangle+|111\rangle}{\sqrt2}.
 \tag{J.6}
```

Aへ

```math
 T=\operatorname{diag}(1,e^{i\pi/4})
 \tag{J.7}
```

を作用させ、二つのCNOTと最初のHadamardを逆順に戻す。理想coherent出力は

```math
 \frac{1+e^{i\pi/4}}2|000\rangle
 +\frac{1-e^{i\pi/4}}2|100\rangle.
 \tag{J.8}
```

従って

```math
 P_{\rm coh}(000)=\cos^2\frac\pi8,
 \qquad
 P_{\rm coh}(100)=\sin^2\frac\pi8.
 \tag{J.9}
```

中間で完全dephaseした模型は

```math
 P_{\rm mix}(000)=P_{\rm mix}(100)=\frac12
 \tag{J.10}
```

を与え、両分布の全変動距離は

```math
 g_{\rm coh}
 =D_{\rm TV}(P_{\rm coh},P_{\rm mix})
 =\frac1{2\sqrt2}.
 \tag{J.11}
```

<!-- theorem-start:proposition -->
**命題（R177：二段共同bath合成のGHZ--T--逆演算証人）**

R181Bによる3入力lift、R181CによるA--B、B--C、局所 $T$、逆gate、およびR181Dによる末端instrumentが同じ永続状態bath上で合成されるとする。観測coherent分布と式(J.9)の距離を $\varepsilon_{\rm coh}$、任意の完全dephase模型の観測分布と式(J.10)の距離を $\varepsilon_{\rm mix}$ とする。このとき

```math
 \varepsilon_{\rm coh}+\varepsilon_{\rm mix}
 <\frac1{2\sqrt2}
```

なら両模型は正の有限余裕で識別できる。
<!-- theorem-end:proposition -->

## R177の証明

式(J.6)へ式(J.7)を作用させると $(|000\rangle+e^{i\pi/4}|111\rangle)/\sqrt2$ となる。逆CNOTをB--C、A--Bの順に作用させると $(|000\rangle+e^{i\pi/4}|100\rangle)/\sqrt2$ であり、AへのHadamardから式(J.8)、絶対値の二乗から式(J.9)を得る。

dephasingは $|000\rangle\langle111|$ とその随伴を消す。逆列は二つの対角成分を等重みのA結果へ移すので式(J.10)を得る。式(J.9)と式(J.10)の全変動距離は式(J.11)である。三角不等式から命題の識別条件が従う。証明終。

## 有限誤差台帳

R177周期の誤差は

```math
 \begin{aligned}
 \varepsilon_{\rm coh}\leq{}&
 \varepsilon_{\rm lift}^{AB}
 +\varepsilon_{\rm lift}^{ABC}
 +\varepsilon_{\rm hold}
 +\varepsilon_{\rm clock}
 +\varepsilon_{AB}
 +\varepsilon_{BC}
 +\varepsilon_T\\
 &+\varepsilon_{BC}^{-1}
 +\varepsilon_{AB}^{-1}
 +\varepsilon_H
 +\varepsilon_{\rm leak}
 +\varepsilon_{\rm ray}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}
 +f_\varnothing.
 \end{aligned}
 \tag{J.12}
```

handoff、branch pairing、decoderを独立項として加えない。同じregisterを保持し、末端で同次元SWAPと容量latchを使うためである。各gateはmode数に依存する枝別和でなく

```math
 \inf_\chi
 \|\widetilde U-e^{i\chi}U\|_{\rm op}
 \leq\varepsilon
 \tag{J.13}
```

で評価する。無反応は最初のfailure cellで排他的に数え、成功試行だけを再規格化しない。

## 末端instrument

R181Dを $L=8$ に特殊化する。実際の末端信号 $v=Z_{\rm out}(\omega)$ をcanonical SWAPでholdし、

```math
 \pi_{abc}^{\delta}(v)
 =\frac{|v_{abc}|^2/\|v\|^2+\delta q_{abc}}{1+\delta},
 \qquad
 \sum_{a,b,c}q_{abc}=1
 \tag{J.14}
```

を容量比として作用殻へ渡す。これはcoherent decoderを仮定しない。計算中にすでに存在する8mode信号を同次元blank registerへ可逆に保持し、その二乗容量を末端だけでlatchする。

末端のunresolved条件は、容量pointerとR164作用殻の境界、有限fiber混合の枝対称性、およびR170までの一体化である。これらはR181Dの条件へ集約する。

## R180の条件付き局所因子化との境界

2入力M54の末端には二つの異なるinterfaceがある。R181Dは末端計算基底分布を直接記録する。R180は実際の4mode信号をholdし、A設定で2つの直交blockへ分け、source-driven paired-Hopf流を通して2翼局所instrumentへ渡す。どちらも1試行信号を集団momentへ置換しない。

切断面で完全共通原因を $\Lambda$ とし、切断後の状態と生成子が

```math
 \mu_{AB}^{x,y}(d\gamma_A,d\gamma_B\mid\Lambda)
 =\mu_A^x(d\gamma_A\mid\Lambda)
 \mu_B^y(d\gamma_B\mid\Lambda),
 \tag{J.15}
```

```math
 L_{AB}^{x,y}(\Lambda)
 =L_A^x(\Lambda)\otimes I_B
 +I_A\otimes L_B^y(\Lambda)
 \tag{J.16}
```

と因子化すれば有限時間核も因子化する。これはR180Cの局所性監査に使う。$\Lambda$ にはM54信号、A設定、内部枝、paired位相、切断面の2翼状態、使用済みsource履歴を含めてよいが、切断後のA核へ $y$、B核へ反対翼の結果形成変数を入れない。

M54の1試行信号を式(J.2)へ置換したり、式(J.2)をM54またはR180へ再注入したりしない。R180Cで未解決なのは、hold、projector latch、選択block port、paired-Hopf pump・sink、中央切断、fresh局所作用殻、2翼R170を共通safe setと単一clockで統合する物理境界である。

## Q2-3の現在地と反証条件

R181B/R181Cにより3入力の有限tensor-liftと2つの有限Hamiltonian gate zoneは明示された。R177は同じregisterのcoherenceを検査する有限gapを与える。R181Dの物理境界と一体化が条件として残るため、Q2-3は条件付き達成である。

次のいずれかが必要なら現行候補は反証される。

- 第1gate後に枝またはmodeを一つ選ぶ。
- 第2gate前に集団momentを推定してfresh bathへ再準備する。
- B--C gateがA側係数または最終分布を外部から読み取る。
- 逆演算のために内部mode別の外部履歴回収が必要になる。
- 固定3入力でも各modeの個別較正、同期、address、resetが必要になる。
- 誤差上界が内部modeごとの粗い和にしかならない。

一般の $N$ に対するQ2-4はM54の直接モードsector-broadcastと逐次2枝標本化で扱う。これはR181B/R181Cのtensor-lift反復から自動的に従う結果ではない。

# 有限粒子位置再平衡化と有限衝突熱浴

> **位置づけ：** M50、R161、R162について、R164の有限信号作用殻状態数から得た条件付き中間状態有効自由エネルギーに対する有限粒子位置再平衡化、有限衝突熱浴による局所詳細釣合い率、粗視化経路熱力学系を証明する。Q1・Q2・Q3に共通な熱化部品として扱い、粗視化された有効仕事・熱と全微視的収支を区別する。


## 目的、用語、主張範囲

本付録は、M50を使うQ1、Q2、Q3の整合条件を全時刻で保存することを要求しない。有限信号座標をHamiltonian制御する仕事行程と、その座標を固定して粒子位置を再平衡化する熱化行程を分離する。各操作面または固定入力時刻で条件付きGibbs分布へ戻せば、制御中に粒子位置が瞬時の分布を追跡する必要はない。

記号 $v\in\mathbb C^m$ は各試行に存在する有限信号座標、$X$ は有限連結配置グラフ上の粒子位置である。$X$ を動かす有限セル列を衝突熱浴と呼ぶ。信号担体、作用殻、衝突熱浴は互いに別の物理部分系である。

本付録が導くのは、単一試行の $v$ に条件付けた局所再平衡化機構である。集団共分散 $C_Z$、統計振幅、全粒子位置密度、確率流を制御器へ入力しない。付録LのR164は、同じ試行の信号作用を枝容量へ写し、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き状態数が得られることを示す。本付録はその作用殻を消去した条件付き中間状態有効自由エネルギーを使う。有限衝突熱浴の微視的可逆性と熱化は既存の衝突模型を参照する [49]。粗視化熱力学と強結合での有効自由エネルギーの語義は [50,51] に従って区別する。

## R164状態数から得る条件付きGibbs族と有効自由エネルギー

有限連結無向グラフを $G_X=(\mathcal I,E_X)$ とし、$L=|\mathcal I|$ とする。信号次元 $m\leq L$ の等長埋込みを

```math
\Psi:\mathbb C^m\longrightarrow\mathbb C^L,
\qquad
\Psi^\dagger\Psi=I_m
```

とする。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定する。付録Lでは、単一試行の信号作用と枝容量を

```math
J_{\rm sig}(v)
=
\mathcal J_0v^\dagger v,
\qquad
A_i^\delta(v)
=
\mathcal J_0
\left[
|(\Psi v)_i|^2
+
\delta q_i v^\dagger v
\right]
```

と置き、排他的2作用殻の状態数が $\Omega_i^\delta\propto A_i^\delta$ となることをR164で示す。従って $v\neq0$ に対して

```math
w_i(v)
=
\frac{|(\Psi v)_i|^2}{v^\dagger v},
\qquad
\pi_i^\delta(v)
=
\frac{w_i(v)+\delta q_i}{1+\delta}
```

と置くと、R164から

```math
\pi_i^\delta(v)
=
\frac{\Omega_i^\delta(v)}
{\sum_j\Omega_j^\delta(v)}
```

である。$\Psi^\dagger\Psi=I_m$ から $\sum_iw_i=1$ であり、$\pi^\delta$ は正の確率分布である。共通位相と全振幅に対して

```math
\pi^\delta(\alpha v)
=
\pi^\delta(v),
\qquad
\alpha\in\mathbb C\setminus\{0\}
```

なので、目標分布はbath rayだけに依存する。

熱エネルギー尺度を $\Theta>0$、$\beta=\Theta^{-1}$ とする。作用殻の枝自由エネルギーと全枝基準を

```math
F_i^{\rm sh}(v)
=
-\Theta\log\Omega_i^\delta(v),
\qquad
F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\sum_j\Omega_j^\delta(v)
```

とし、gauge固定した条件付き粒子位置有効自由エネルギーを

```math
E_i^\delta(v)
=
F_i^{\rm sh}(v)-F_{\rm eq}^{\rm sh}(v)
=
-\Theta\log\pi_i^\delta(v)
```

と定める。$E_i^\delta$ は裸の配置エネルギーでなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。全系の平衡Hamiltonianと周辺化を別に与えた場合を除き、無条件に平均力Hamiltonianとは呼ばない。この規約では

```math
\sum_i
e^{-\beta E_i^\delta(v)}
=1
```

であり、平衡自由エネルギーの基準値は全ての $v$ で零である。作用殻明示表示の $\Omega_i^\delta$ と、作用殻消去表示の $e^{-\beta E_i^\delta}$ は同じ縮約を表すため、同じ分配関数内で積 $\Omega_i^\delta e^{-\beta E_i^\delta}$ を使わない。これは状態数の二重計数を避けるための表現規約である。

任意の粒子位置分布 $p$ に対し、非平衡自由エネルギーを

```math
\mathcal F[p\mid v]
=
\sum_i p_iE_i^\delta(v)
+
\Theta\sum_i p_i\log p_i
```

と置けば

```math
\mathcal F[p\mid v]
-
\mathcal F[\pi^\delta\mid v]
=
\Theta
D_{\rm KL}
\left(
p\|\pi^\delta(v)
\right)
```

である。従って条件付き再平衡化は、固定した $v$ における相対エントロピーと非平衡自由エネルギーの緩和として解釈できる。

## R161の証明：任意の有限信号方向への粒子位置再平衡化

各無向辺 $\{i,j\}\in E_X$ に対称活動度 $a_{ij}=a_{ji}>0$ を置く。固定した $v\neq0$ に対して

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{
\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}
}
```

とし、非隣接頂点間の率は零とする。生成子を

```math
(\mathcal L_v^\delta f)(i)
=
\sum_{j:j\sim i}
k_{i\to j}^\delta(v)
[f(j)-f(i)]
```

と書く。

基準分布の最小値、辺活動度の最小値を

```math
q_{\min}=\min_iq_i,
\qquad
a_{\min}=\min_{\{i,j\}\in E_X}a_{ij},
\qquad
m_\delta=\frac{\delta q_{\min}}{1+\delta}
```

とする。無重みグラフLaplacianの第1非零固有値を $\lambda_G>0$ とする。

**第2章R161で用いる一様評価。**

有限連結 $G_X$、$\delta>0$、任意の $v\neq0$ について、上の生成子は既約かつ可逆であり、唯一の定常分布は $\pi^\delta(v)$ である。$L^2(\pi^\delta)$ における第1非零固有値を $\lambda_\delta(v)$ とすれば

```math
\lambda_\delta(v)
\geq
\kappa_Xa_{\min}m_\delta\lambda_G
=:
\lambda_\delta
```

が全bath rayに一様に成り立つ。任意の初期粒子位置分布 $p_0$ に対して

```math
D_{\rm TV}
\left(
p_T,
\pi^\delta(v)
\right)
\leq
C_\delta e^{-\lambda_\delta T},
\qquad
C_\delta
=
\frac12
\sqrt{m_\delta^{-1}-1}
```

である。また

```math
D_{\rm TV}
\left(
\pi^\delta(v),
w(v)
\right)
\leq
\frac{\delta}{1+\delta}
```

であり、全有限時間誤差は混合誤差と正則化誤差に分かれる。

詳細釣合いは各辺で

```math
\pi_i^\delta k_{i\to j}^\delta
=
\kappa_Xa_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
=
\pi_j^\delta k_{j\to i}^\delta
```

となることから従う。Dirichlet形式は

```math
\mathcal E_z^\delta(f,f)
=
\kappa_X
\sum_{\{i,j\}\in E_X}
a_{ij}
\sqrt{\pi_i^\delta\pi_j^\delta}
(f_i-f_j)^2
```

である。$\pi_i^\delta\geq m_\delta$ なので

```math
\mathcal E_z^\delta(f,f)
\geq
\kappa_Xa_{\min}m_\delta
\sum_{\{i,j\}\in E_X}
(f_i-f_j)^2.
```

一様平均を $\overline f=L^{-1}\sum_if_i$ とすれば、グラフPoincaré不等式と分散の最小化性から

```math
\sum_{\{i,j\}\in E_X}
(f_i-f_j)^2
\geq
\lambda_G
\sum_i(f_i-\overline f)^2
\geq
\lambda_G
\operatorname{Var}_{\pi^\delta}(f).
```

これがスペクトルギャップ下界を与える。有限可逆鎖の $L^2$ 収縮とCauchy--Schwarz不等式から

```math
D_{\rm TV}(p_T,\pi^\delta)
\leq
\frac12e^{-\lambda_\delta T}
\left\|
\frac{p_0}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}.
```

任意の $p_0$ について

```math
\left\|
\frac{p_0}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}^2
=
\sum_i\frac{p_{0,i}^2}{\pi_i^\delta}-1
\leq
m_\delta^{-1}-1
```

なので前因子も一様である。正則化誤差は

```math
D_{\rm TV}(\pi^\delta,w)
=
\frac{\delta}{2(1+\delta)}
\sum_i|q_i-w_i|
\leq
\frac{\delta}{1+\delta}
```

から従う。

<!-- theorem-start:proof -->
**証明（R161）**

正値性と連結性が既約性を、辺ごとの恒等式が可逆性と定常性を与える。Dirichlet形式を無重みグラフの形式で下から抑えると一様スペクトルギャップが得られる。可逆半群の $L^2$ 収縮、初期密度の一様上界、正則化分布と理想対角の全変動距離を順に適用すれば表示式が従う。証明終。
<!-- theorem-end:proof -->

### nodeにおける一様局所再平衡化の障害

<!-- theorem-start:proposition -->
**命題（零占有切断点に対する局所詳細釣合いno-go）**

$\delta=0$ とし、目標分布 $w$ の零頂点 $v$ が $G_X$ の切断点であるとする。隣接辺だけを使い、$w$ に関して詳細釣合いを満たす有限率生成子は、$G_X\setminus\{v\}$ の異なる連結成分間で確率質量を輸送できない。従って全初期分布から $w$ へ収束する既約な局所生成子は存在しない。
<!-- theorem-end:proposition -->

$w_v=0$ と $w_i>0$ に対し、詳細釣合いは

```math
w_i k_{i\to v}
=
w_vk_{v\to i}
=0
```

を強制するので $k_{i\to v}=0$ である。切断点を通る全経路が閉じるため、各成分の確率質量は独立に保存される。

この障害を避けるには、正の背景占有率、非局所辺、補助橋状態の少なくとも1つが必要である。粒子位置熱化を使うM50の特殊化では $\delta>0$ を採用し、有限資源誤差として台帳に残す。信号から容量pointerだけを作るR181Dのlatch段階は、このnode命題の対象外である。その後に有限混合を使う場合は本命題の条件を再び受ける。

## R162の証明：有限衝突熱浴による率の実現

固定した $v$ と辺 $\{i,j\}$ に対し、対称な基準障壁 $B_{ij}^0=B_{ji}^0$ を置く。制御された障壁を

```math
B_{ij}^\delta(v)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(v)
+
E_j^\delta(v)
\right]
```

とする。$B_{ij}^0\geq(\Theta/2)\log(m_\delta^{-1})$ なら、両方向の活性化エネルギーは非負である。

入射セルは、到着断面を横切る流束について運動エネルギー分布

```math
f_{\rm in}(\epsilon)
=
\beta e^{-\beta\epsilon},
\qquad
\epsilon\geq0
```

を持つとする。これは静止した熱粒子を無条件に標本化する分布ではなく、衝突面へ実際に到着した粒子を数える流束分布である。入射位置、到着時刻、運動方向とその共役変数も完全状態へ含める。各辺には反応座標 $r_{ij}$ と共役運動量を置き、2つの井戸の底を $E_i^\delta,E_j^\delta$、鞍点を $B_{ij}^\delta$ に持つ滑らかなポテンシャルで散乱させる。理想的な閾値反射・通過則は、その障壁を狭くする有限幅極限として扱う。

$X=i$ のセルが辺 $i\to j$ へ到着したとき、

```math
\epsilon
\geq
B_{ij}^\delta(v)-E_i^\delta(v)
```

なら通過させ、通過後のセルエネルギーを

```math
\epsilon'
=
\epsilon
+
E_i^\delta(v)
-
E_j^\delta(v)
```

とする。閾値未満なら反射させる。通過時には

```math
\epsilon+E_i^\delta
=
\epsilon'+E_j^\delta
```

が成り立つ。ここで保存されるのは、作用殻fiberを消去した粒子位置有効自由エネルギーとセルエネルギーの粗視化和である。fiberを明示した全微視的Hamiltonianのエネルギー保存をこの式だけから主張しない。さらに前向き閾値を満たすことと、出射状態が逆向き閾値を満たすことは同値である。

**第2章R162で用いる有限衝突評価。**

各辺の衝突試行流束を $\nu_{ij}=\nu_{ji}>0$ とする。上の流束分布、対称障壁、粗視化有効自由エネルギー保存散乱を採用すると、縮約された配置遷移率は

```math
k_{i\to j}^{\rm coll}(v)
=
\nu_{ij}
e^{-\beta B_{ij}^0}
\sqrt{
\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}
}
```

である。従って

```math
\nu_{ij}e^{-\beta B_{ij}^0}
=
\kappa_Xa_{ij}
```

と校正すればR161の生成子に一致する。上の反応座標ポテンシャルに、入射位置、到着時計、運動方向、反射枝、出射エネルギー、履歴セルを含めれば、拡大散乱写像は一対一な時間反転対を持つ滑らかなHamiltonian散乱で任意精度に近似できる。

固定観測時間 $T$、各辺の有限セル数 $K_{ij}$、有限エネルギー切断 $E_{\max}$ では、理想生成子の経路測度との差を

```math
\varepsilon_{\rm coll}
\leq
\varepsilon_{\rm overflow}
+
\varepsilon_{\rm energy}
+
\varepsilon_{\rm smooth}
+
\varepsilon_{\rm clock}
```

と評価できる。信号bath座標の有限保持誤差 $\varepsilon_{\rm hold}$ はこれと別に加える。超過衝突、閾値平滑化帯、controller保持失敗は正式な無反応結果へ含め、除外後の再規格化を行わない。

有効自由エネルギーを全枝共通の $g(v)$ だけ移し、障壁も同じだけ移すgauge変換

```math
E_i^\delta
\longmapsto
E_i^\delta+g,
\qquad
B_{ij}^\delta
\longmapsto
B_{ij}^\delta+g
```

では、活性化差 $B_{ij}^\delta-E_i^\delta$ と全遷移率が不変である。従ってR162はR164の全枝状態数に含まれる共通因子へ依存しない。

活性化エネルギーは

```math
B_{ij}^\delta-E_i^\delta
=
B_{ij}^0
+
\frac{\Theta}{2}
\log
\frac{\pi_i^\delta}{\pi_j^\delta}
```

なので、指数分布の尾確率から

```math
\begin{aligned}
k_{i\to j}^{\rm coll}
&=
\nu_{ij}
\exp
\left[
-\beta(B_{ij}^\delta-E_i^\delta)
\right]\\
&=
\nu_{ij}e^{-\beta B_{ij}^0}
\sqrt{\frac{\pi_j^\delta}{\pi_i^\delta}}
\end{aligned}
```

を得る。正逆率比は

```math
\log
\frac{k_{i\to j}^{\rm coll}}
{k_{j\to i}^{\rm coll}}
=
-\beta
\left(
E_j^\delta-E_i^\delta
\right)
=
\log
\frac{\pi_j^\delta}{\pi_i^\delta}.
```

これは局所詳細釣合いである。

有限セルについて、辺 $\{i,j\}$ の理想到着数を平均 $\nu_{ij}T$ のPoisson変数 $N_{ij}$ で表すなら

```math
\varepsilon_{\rm overflow}
\leq
\sum_{\{i,j\}\in E_X}
P(N_{ij}>K_{ij}).
```

入射エネルギーを $E_{\max}$ で切る誤差は、衝突セル総数を $K_{\rm tot}$ として

```math
\varepsilon_{\rm energy}
\leq
K_{\rm tot}e^{-\beta E_{\max}}
```

で抑えられる。固定有限個のセルと時計を事前配置すれば、有限時間の離散衝突列は有限個の正準散乱窓からなる。無期限反復にはfresh cellの流入と使用済みセルの流出が必要である。

記録前には新規入射セルを止め、辺チャネルの入口ゲートを閉じる。エネルギー切断された安全セルは閉じた辺を越えない。有限障壁裾、平滑化帯、時計ずれによる離脱だけを $\varepsilon_{\rm res}$ として残せる。これによりR143が仮定していた記録中の経路滞在を、衝突窓の停止と局所辺閉鎖から評価できる。

<!-- theorem-start:proof -->
**証明（R162）**

指数流束分布の尾確率へ活性化エネルギーを代入すると表示した遷移率が得られる。対称障壁は正逆率比を粒子位置有効自由エネルギー差だけにし、通過後エネルギー式は正逆散乱を一対一に対応させる。有限時間では到着数と最大エネルギーを切り、超過事象を完全結果集合へ残す。閾値比較、反射、通過、履歴保存を滑らかな有限幅散乱へ近似した誤差を加えれば有限セル上界が従う。証明終。
<!-- theorem-end:proof -->

## 粗視化経路熱力学系の証明

以下は、非平衡仕事関係と経路エントロピー生成の標準形 [46--48] をR161、R162の条件付き粒子位置過程へ適用したものである。$E_i^\delta$ はR164の作用殻を消去した相対有効自由エネルギーなので、ここで定義する仕事と熱には上付き $\rm rel$ を付け、全微視的仕事・熱と区別する [50,51]。

単一試行信号 $v_t$ を外部制御写像により動かし、粒子位置有効自由エネルギーを $E_i^\delta(v_t)$ とする。粒子位置経路を

```math
\omega
=
(i_0,t_1,i_1,\ldots,t_N,i_N)
```

と書く。経路中の有効地形仕事と条件付き配置中間状態へ入る有効熱を

```math
W^{\rm rel}[\omega]
=
\int_0^T
\dot E_{X_t}^\delta(v_t)
\,dt,
```

```math
Q^{\rm rel}[\omega]
=
\sum_{\ell=1}^N
\left[
E_{i_\ell}^\delta(v_{t_\ell})
-
E_{i_{\ell-1}}^\delta(v_{t_\ell})
\right]
```

と定義すれば、粗視化された経路ごとに $\Delta E=W^{\rm rel}+Q^{\rm rel}$ である。

前向きprotocolを初期分布 $p_0$ から走らせ、その終端分布を $p_T$ とする。時間反転protocolは $p_T$ から開始する。両者の経路確率を $\mathcal P_F[\omega]$、$\mathcal P_R[\omega^\dagger]$ とする。全エントロピー生成を

```math
\Sigma[\omega]
=
\log\frac{p_0(i_0)}{p_T(i_N)}
+
\sum_{\ell=1}^N
\log
\frac{
k_{i_{\ell-1}\to i_\ell}^\delta(v_{t_\ell})
}{
k_{i_\ell\to i_{\ell-1}}^\delta(v_{t_\ell})
}
```

とする。

**第2章の粗視化経路熱力学系。**

R161の生成子またはR162の衝突熱浴を、正逆protocolで同じ熱作用尺度 $\Theta$ により駆動する。このとき

```math
\frac{\mathcal P_F[\omega]}
{\mathcal P_R[\omega^\dagger]}
=
e^{\Sigma[\omega]},
```

```math
\left\langle
e^{-\Sigma}
\right\rangle_F
=1,
\qquad
\left\langle
\Sigma
\right\rangle_F
\geq0.
```

単一試行信号 $v^-$ の平衡分布から $v^+$ へ瞬間quenchする場合、状態 $i$ の有効地形仕事は

```math
W_i^{\rm rel}
=
\Theta
\log
\frac{\pi_i^\delta(v^-)}
{\pi_i^\delta(v^+)}
```

であり、採用した自由エネルギー基準では

```math
\left\langle
e^{-\beta W^{\rm rel}}
\right\rangle
=1,
```

```math
\langle W^{\rm rel}\rangle
=
\Theta
D_{\rm KL}
\left(
\pi^\delta(v^-)
\|
\pi^\delta(v^+)
\right).
```

作用殻明示表示では $W_i^{\rm sh}=\Delta F_i^{\rm sh}$ と書き、$W_i^{\rm rel}=W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}$ である。全作用保存unitaryでは共通項が一定になり得るが、pumpまたはresetでは一定とは限らない。

連続時間jump経路の待機因子は正逆比で相殺し、jump因子の比が局所詳細釣合い率の積になる。初期終端密度比を加えると経路確率比を得る。逆経路測度について和を取れば積分ゆらぎ関係、Jensen不等式から平均非負性が従う。

瞬間quenchでは配置は動かず、有効地形仕事は有効自由エネルギー差だけである。従って

```math
\begin{aligned}
\left\langle e^{-\beta W^{\rm rel}}\right\rangle
&=
\sum_i
\pi_i^\delta(v^-)
\frac{\pi_i^\delta(v^+)}{\pi_i^\delta(v^-)}\\
&=
1,
\end{aligned}
```

平均を取れば相対エントロピー式になる。正逆経路確率比と積分ゆらぎ関係は粗視化跳躍過程について厳密である。一方、作用容量を変える過程、殻内平衡化、制御器反作用を含む完全Hamiltonianを構成しない限り、$W^{\rm rel}$ を全装置の機械仕事、$Q^{\rm rel}$ を全微視的熱と呼ばない。ゆらぎの定理はR164で得た地形の整合性を検査するが、作用殻状態数の線形則を導く定理ではない。

<!-- theorem-start:proof -->
**証明（粗視化経路熱力学系）**

正逆経路の初期密度、jump率、待機因子を比べる。待機因子は反転protocolの対応区間と相殺し、残る率比と端点密度比が $e^\Sigma$ を与える。逆経路確率の総和は1なので積分ゆらぎ関係が従う。瞬間quench式は規格化されたGibbs分布へ直接代入して得る。証明終。
<!-- theorem-end:proof -->

## R170：M50固定入力時刻有限枝instrumentの証明

入力時刻 $t_\star$ に非零信号 $v$ を空の保持registerへ正準SWAPする。SWAPは自己逆であり、交換前のregisterと時計面を履歴へ残せば拡大写像は1対1である。保持誤差または閾値失敗は無反応へ送る。

R164の単一Liouville母測度から、固定した $v$ に対する排他的枝分布は

```math
\pi_i^\delta(v)
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}{1+\delta}
```

となる。作用殻を消去した後は $E_i^\delta=-\Theta\log\pi_i^\delta$ だけを使うため、状態数を二重計数しない。

R161を時間 $\tau_X$ だけ作用させると、理想枝分布 $p_{\tau_X}$ は

```math
D_{\rm TV}
\left(
p_{\tau_X},
\pi^\delta(v)
\right)
\leq
C_\delta e^{-\lambda_\delta\tau_X}
=:
\varepsilon_{\rm mix}
```

を満たす。R162の有限衝突列でこの半群を近似する。衝突数超過、エネルギー切断、時計境界、滑らかな散乱近似の総偏差を $\varepsilon_{\rm coll}$ とすれば、データ処理不等式により粒子位置周辺の偏差も同じ量以下である。

熱化後に新規入射セルを止めて枝間ゲートを閉じる。枝 $i$ の安全領域内で1、他枝と通信路上で0となる滑らかな局所関数 $d_i(x)$ を選び、空の記録器へ

```math
G_{\rm rec}
=
\sum_i d_i(x)P_{D_i}
```

を作用させる。安全領域では1個の粒子位置枝だけが占有されるため、対応する1個の記録だけが動く。辺閉鎖、有限井戸幅、記録窓の偏差を $\varepsilon_{\rm lock}+\varepsilon_{\rm rec}$ とする。

各段階は確率核または無反応への写像であり、全変動距離を増加させない。作用容量、作用殻、混合、衝突、固定、記録、時計の有限偏差を順に合成すると

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

を得る。同じ物理偏差は最初に現れる項へだけ入れる。無反応を完全結果集合 $\mathcal I\cup\{\varnothing\}$ に残すため、成功試行の再規格化は不要である。

履歴には入力register、SWAP前後の時計、作用殻枝、衝突セル列、反射・透過ラベル、枝閉鎖状態、局所記録、無反応原因を残す。従って異なる入力または衝突履歴を同じ最終拡大状態へ潰さず、有限試行写像は単射である。全操作は有限時間なので $t_{\rm out}>t_\star$ を選べる。これでR170を得る。

この証明は、作用容量結合、作用殻fiber内平衡化、信号保持controller、衝突bath、記録器を1つの具体的Hamiltonianへ統合するものではない。R170は列挙した有限部品を指定誤差内で実行できることを前提にする条件付きinstrument定理である。

## Q1・Q2・Q3周期への接続

M47の1段測定はM50のQ1特殊化として次の操作面へ分ける。

1. R181AのW型2モード系で信号bath方向を目標rayへ準備する。
2. 方向を保持し、R164の作用枝容量と条件付き作用殻fiberを準備する。
3. R161/R162で粒子位置を条件付きGibbs分布へ近づける。
4. 衝突熱浴を切り、R140の分析器操作を行う。この間の粒子位置は瞬時分布を追跡しなくてよい。
5. 分析器終了後の方向を保持し、作用殻fiberを更新してから再びR161/R162を有限時間作用させる。
6. 入射セルを止めて辺ゲートを閉じ、R140の傾斜保持とR143の局所記録を行う。
7. 結果別テンプレート交換後、そのテンプレート方向に対して作用殻準備と再平衡化を行い、次の逐次測定へ渡す。

1回の再平衡化誤差をM50の共通台帳

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

で記帳する。$\varepsilon_{\rm mix}=C_\delta e^{-\lambda_\delta T_X}$、$\varepsilon_\delta=\delta/(1+\delta)$ と選べる。Q1では2モード漏れと局所辺閉鎖誤差をそれぞれ $\varepsilon_{2m}$、$\varepsilon_{\rm res}$ として別に加える。この段階分離により、旧連続matching保存をR143、R144の仮定に使わない。

Q2-1はR181Dにより末端4mode信号を同次元hold-registerへSWAPし、容量latch後にR164/R170へ接続する。別の中間標本器を確率源として挟まない。Q2-2の切断後局所殻は各翼でR170を特殊化し、完全共通原因 $\Lambda$ に条件付けた積因子化誤差を別の $\varepsilon_{\rm prod}$ として加える。Q3は準備終了面のM37標本へR164を一度だけ適用して初期M42位置を作り、その後は付録Nの局所辺衝突bathで同じ粒子を輸送する。M42の一般有向率は局所詳細釣合いを満たさないので、R162の平衡率公式をそのまま用いず、方向別controllerと仕事registerを持つ駆動衝突cellへ拡張する。任意の固定時刻を診断する代替経路だけが付録FのR170を使う。

Q2-4のM54では、全gate後にR181Dが各bitの直交projector作用をraw容量へlatchする。R164はregularized容量比を排他的Born型状態数へ解釈し、R161/R162/R170がselectorを形成する。selector lock後に可逆filterとradial-only repumpを作用する。同じR170作用殻receiverを逐次nodeで使い、別のaperture標本器を重ねない。$L=2^n$ のsignal、work、history、cold、spent容量は受動資源として指数的でもよいが、個別の外部準備・較正・読出しには使わない。

## 有限資源と正則化極限

$\pi_i^\delta\geq m_\delta$ から粒子位置有効自由エネルギー幅は

```math
\max_iE_i^\delta
-
\min_iE_i^\delta
\leq
\Theta\log(m_\delta^{-1}).
```

採用できる基準障壁も少なくとも同じ対数尺度を持つ。R161の一般下界は

```math
\lambda_\delta
=
O(\delta)
```

まで低下し得る。さらに $B_{ij}^0\geq(\Theta/2)\log(m_\delta^{-1})$ と率校正を同時に満たすには

```math
\nu_{ij}
\geq
\kappa_Xa_{ij}m_\delta^{-1/2}
```

が必要になり得る。さらにR164の有限幅作用殻を一様精度で保つ剛性は、他の尺度を固定すると下界の次数として

```math
\kappa
=
\Omega
\left(
\delta^{-2}
\right)
```

と増大する必要があり、$\kappa=\Theta(\delta^{-2})$ は代表的な選択である。従って $\delta\downarrow0$ では、有効地形幅、衝突流束、混合時間、作用殻剛性の少なくとも1つが発散する。有限資源のまま厳密nodeを全方向で追跡するとは主張しない。

有限周期数 $N_{\rm cyc}$ に対するfresh cellと履歴セルは少なくとも衝突数と記録数に比例する。固定容量の閉鎖系による無期限の熱化、永久記録、resetは行わない。

## R164で閉じた範囲と非主張

R164は単一試行信号作用から枝容量を作り、排他的2作用殻のLiouville状態数を単一母測度で規格化すると

```math
\Omega_i^\delta(v)
\propto
|(\Psi v)_i|^2
+
\delta q_i v^\dagger v
```

となり、$E_i^\delta=-\Theta\log\pi_i^\delta$ が作用殻を消去した条件付き中間状態有効自由エネルギーとして得られることを条件付きで厳密に示す。従って旧版の「Born型地形を確率から直接設計した」という未解決性は一段狭くなる。一方、本付録と付録Lは次を主張しない。

1. 枝容量結合 $A_i^\delta(v)$ と作用殻fiber内平衡化を同じ有限局所Hamiltonianから自動的に準備すること。
2. 枝対称な角周期、余面積因子、入口流束が信号担体だけから自動的に従うこと。
3. 信号bath座標を有限反作用で保持するcontrollerを含む全装置の最小Hamiltonian。
4. R181AのW型2モード系のHopf方程式を作用殻fiberまたは同じ衝突熱浴から導いたこと。
5. 有限個のセルが無限時間のMarkov浴を厳密に再現すること。
6. 無反応またはoverflowを除外した後の条件付き統計。
7. $\delta=0$ で任意のnode方向を一様有限資源で再平衡化すること。
8. 解析器、Hopf pump、fiber、記録、template交換、resetまで含む周期全体の微視的仕事・熱・エントロピー収支。
9. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。

残る最重要目標は、作用容量結合、殻内平衡化、枝対称性、信号保持反作用をQ1・Q2・Q3の各完全周期または固定入力instrumentの有限局所Hamiltonianとして統合することである。R161、R162、R164を完全な有限装置による一般Born測度の第一原理導出とは分類しない。

# 有限信号作用と作用殻状態数の共通起源

> **位置づけ：** M50とR164について、一般有限信号作用から正則化枝容量を作り、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き分布とR161の有効自由エネルギーが得られることを条件付きで厳密に示す。Q1の2成分信号とQ2の4成分信号を同じ定理の特殊化として扱い、滑らかな有限幅拘束、枝流束、node、資源発散、表現の二重計数禁止を明示する。


## 目的と主張範囲

付録Kは、正の条件付き分布 $\pi_i^\delta(v)$ に対して可逆な粒子位置jump過程と有限衝突熱浴を構成する。本付録はその上流をQ1、Q2、Q3に共通なM50「有限信号作用・作用殻・粒子位置熱化共通モジュール」として固定する。旧版では

```math
E_i^\delta(v)
=
-\Theta\log\pi_i^\delta(v)
```

を制御器へ設計した地形として置いていた。本付録ではBorn型確率を先に定義せず、同じ試行に存在する信号作用と、位置枝ごとの排他的な作用殻状態数から $\pi_i^\delta$ を導く。

旧R24の一般作用殻容量と2作用殻の線形性は、この目的に使える。ただし旧M15の位置入口模型、等方混合、標本化後の再埋込み、測定周期を復活させない。R164は、旧R24の状態数補題を一般有限信号、正則化、R161・R162と粗視化経路熱力学の語義へ移植した条件付き結果である。M50は共通instrument仕様であり、それ自体を完成したHamiltonian模型とは呼ばない。

本付録で区別する物理部分系は次の4つである。

1. $v\in\mathbb C^m$ を持つ有限信号担体。
2. 枝容量を数える作用殻fiber。
3. 粒子位置 $X=i$。
4. $X$ を再平衡化する付録Kの有限衝突熱浴。

作用殻fiberと衝突熱浴は同じものではない。前者は条件付き状態数を、後者はその状態数比と整合する粒子位置遷移を与える。

## 共通R135の階数1支持とM50入力

M50は各試行に存在する非零信号を入力とする。Q1のように複素振幅を集団共分散の階数1因子として定義する場合、その統計因子を単一試行信号と同一視せず、次の支持補題を介して接続する。

確率変数としての信号浴座標を $Z\in\mathbb C^m$ とし、

```math
0
<
\mathbb E[Z^\dagger Z]
<
\infty,
\qquad
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}
{\mathbb E[Z^\dagger Z]}
```

とする。$C_Z$ は正半定値、trace 1である。

ここでも $C_Z$ は非中心化された規格化第2モーメントを指す。$\mathbb E[Z]=0$ の場合にだけ通常の中心化共分散と比例して一致する。以下の支持補題へ中心化共分散の階数条件だけを代入してはならない。

**R135の階数1支持節。**

単位ベクトル $c\in\mathbb C^m$ について

```math
C_Z
=
cc^\dagger
```

ならば、複素確率変数 $\alpha=c^\dagger Z$ を用いて

```math
Z
=
\alpha c
\qquad\text{a.s.}
```

と書ける。逆に $Z=\alpha c$ がほとんど確実に成り立ち、$\mathbb E|\alpha|^2>0$ なら $C_Z=cc^\dagger$ である。
**M50記号での確認。**

$P_c^\perp=I_m-cc^\dagger$ とする。このとき

```math
\frac{
\mathbb E\left\|P_c^\perp Z\right\|^2
}{
\mathbb E[Z^\dagger Z]
}
=
\operatorname{tr}
\left(
P_c^\perp C_Z
\right)
=
0.
```

非負確率変数の期待値が零なので $P_c^\perp Z=0$ がほとんど確実に成り立つ。従って $Z=(c^\dagger Z)c=\alpha c$ である。逆向きは共通因子 $\mathbb E|\alpha|^2$ が規格化で消えることから従う。証明終。

近似階数1では、単一試行信号のray外平均作用比を

```math
\varepsilon_{\rm supp}(c)
:=
\operatorname{tr}
\left[
\left(I_m-cc^\dagger\right)C_Z
\right]
=
\frac{
\mathbb E
\left\|
\left(I_m-cc^\dagger\right)Z
\right\|^2
}{
\mathbb E[Z^\dagger Z]
}
```

と定める。これは平均二乗評価であり、各試行の相対方向誤差を一様には抑えない。M50へ渡す安全試行では $z=Z(\omega)$ に $z^\dagger z\geq r_*>0$ を課し、閾値未満と零信号を無反応へ送る。有限時間Hopf方向誤差から $\varepsilon_{\rm supp}$ を評価する場合は同じ偏差を二重に誤差加算しない。

Q1ではM50の仮引数を $v=z$ と特殊化する。厳密支持上では $z=\alpha c$ なので

```math
\pi_i^\delta(z)
=
\frac{
|\left(\Psi c\right)_i|^2
+
\delta q_i
}{1+\delta}
\qquad\text{a.s.}
```

となるが、物理制御器が入力するのは $c$ または $C_Z$ でなく単一試行の $z$ である。$c$ は集団を表示する統計的rayに留まる。

この補題は正半定値自己共分散 $\mathbb E[ZZ^\dagger]$ に対する結果である。Q2の交差モーメント $\mathbb E[z_Az_B^{\mathsf T}]$、そのベクトル化、またはそこから作る階数1射影へ適用して、積標本 $z_A\otimes z_B$ がsinglet ray上にあるとは結論しない。付録Iの否定命題はそのような直接singlet支持が不可能であることを示す。M54ではR181Bが1試行の積入力から実際の $Z_S=a\otimes b$ をHamiltonian liftで作るので、集団共分散を準備機構として流用しない。

Q3のR168は、この階数1支持に加えて一般の安全事象上のray平均を扱う。高階数の固定作用節では、各試行の全作用が一定のときだけ、試行ごとのray規格化と集団第2モーメントの規格化が可換になる。可変全作用集団ではradial補正が必要であり、Q2の交差モーメントへこの節を流用しない。

## M50の信号作用と正則化枝容量

有限な排他的枝集合を $\mathcal I$、枝数を $L$ とし、信号次元 $m\leq L$ の等長埋込みを

```math
\Psi:\mathbb C^m\longrightarrow\mathbb C^L,
\qquad
\Psi^\dagger\Psi=I_m
```

とする。作用単位 $\mathcal J_0>0$ に対して、単一試行信号の総作用と枝信号作用を

```math
J_{\rm sig}(v)
=
\mathcal J_0 v^\dagger v,
\qquad
J_i(v)
=
\mathcal J_0
\left| (\Psi v)_i \right|^2
```

と置く。等長性から

```math
\sum_iJ_i(v)
=
J_{\rm sig}(v)
```

である。正の固定基準分布 $q_i>0$、$\sum_iq_i=1$ と有限正則化 $\delta>0$ に対し、枝 $i$ の作用容量を

```math
A_i^\delta(v)
=
J_i(v)
+
\delta q_iJ_{\rm sig}(v)
```

とする。このとき

```math
\sum_iA_i^\delta(v)
=
(1+\delta)J_{\rm sig}(v),
\qquad
A_i^\delta(v)>0
```

が $v\neq0$ で成り立つ。$\delta q_iJ_{\rm sig}$ は確率の混合ではなく、背景作用を枝へ分けた有限装置容量として定義される。

容量式は共通位相に不変で、振幅拡大に対して2次の共変性を持つ。

```math
A_i^\delta(e^{i\alpha}v)
=
A_i^\delta(v),
\qquad
A_i^\delta(\gamma v)
=
|\gamma|^2A_i^\delta(v)
```

この全振幅依存性は、後で全枝状態数を規格化すると消える。

## 排他的枝と単一母測度

位置枝に対応する作用殻を

```math
\Gamma^\delta(v)
=
\bigsqcup_{i\in\mathcal I}
\Gamma_i^\delta(v)
```

という非交和にする。1つの微視的状態は、同時に複数枝の状態として数えない。枝 $i$ には、活性作用 $K_i\geq0$ と1本の明反応作用 $I_i\geq0$、それぞれの角 $\theta_{K_i},\theta_{I_i}\in[0,2\pi)$ を置き、

```math
K_i+I_i=A_i^\delta(v)
```

を課す。作用基準 $J_{\rm ref}>0$ を使い、枝状態数を

```math
\Omega_i^\delta(v)
=
\frac{1}{J_{\rm ref}}
\int_{\Gamma_i}
\delta
\left(
A_i^\delta(v)-K_i-I_i
\right)
dK_i\,dI_i\,d\theta_{K_i}\,d\theta_{I_i}
```

と定める。全枝は同じLiouville規約、同じ角周期、同じ作用基準で数える。枝ごとに別々の規格化測度を置いてから比較するのではなく、非交和上の単一母測度を最後に一度だけ規格化する。

## 一般作用殻容量

$n$ 本の非負作用 $J_1,\ldots,J_n$ と角 $\theta_1,\ldots,\theta_n$ に対し、無次元状態数を

```math
\Omega_n(A)
=
\frac{1}{J_{\rm ref}^{n-1}}
\int
\delta
\left(
A-\sum_{r=1}^nJ_r
\right)
\prod_{r=1}^n
dJ_r\,d\theta_r
```

と置く。

<!-- theorem-start:lemma -->
**補題（一般作用殻容量）**

$A>0$ に対して

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
\left(
\frac{A}{J_{\rm ref}}
\right)^{n-1}
```

である。特に2作用殻は

```math
\Omega_2(A)
=
\frac{(2\pi)^2}{J_{\rm ref}}A
```

と容量に線形である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明（一般作用殻容量）**

角積分は $(2\pi)^n$ を与える。作用積分は $J_r\geq0$、$\sum_rJ_r=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。作用基準で無次元化すれば表示式を得る。証明終。
<!-- theorem-end:proof -->

## R164の証明：条件付き作用殻の状態数起源

**第2章R164で用いる状態数評価。**

$\Psi:\mathbb C^m\to\mathbb C^L$、$\Psi^\dagger\Psi=I_m$、$v\neq0$、$q_i>0$、$\sum_iq_i=1$、$\delta\geq0$ とする。$\delta=0$ では正容量を持つ活性支持だけを枝集合とする。枝容量を

```math
A_i^\delta(v)
=
\mathcal J_0
\left[
\left|(\Psi v)_i\right|^2
+
\delta q_i v^\dagger v
\right]
```

とし、各排他的枝を同じ2作用殻Liouville測度で数える。このとき

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}
A_i^\delta(v)
```

であり、非交和上の規格化枝重みは

```math
\begin{aligned}
P_i^\delta(v)
&=
\frac{\Omega_i^\delta(v)}
{\sum_j\Omega_j^\delta(v)}\\
&=
\frac{
| (\Psi v)_i |^2/(v^\dagger v)
+
\delta q_i
}{1+\delta}\\
&=
\pi_i^\delta(v).
\end{aligned}
```

従ってBorn型条件付き重みは、確率を枝容量へ書き込むことなく、有限信号作用の枝分解、背景作用容量、各排他的枝の2作用殻の状態数、単一母測度の規格化から得られる。ここで「2作用殻」は各枝の内部に非負作用が2本あるという意味であり、枝数が2であることを意味しない。Q1では典型的に $m=2$、Q2の中央共同読出しでは $m=L=4$ である。

<!-- theorem-start:proof -->
**証明（R164）**

一般作用殻容量の $n=2$ を各枝へ適用する。全枝に共通な $(2\pi)^2/J_{\rm ref}$ は規格化で消える。等長性と $\sum_iq_i=1$ から分母は $(1+\delta)\mathcal J_0v^\dagger v$ である。これを枝容量で割れば表示式を得る。証明終。
<!-- theorem-end:proof -->

R164は共通位相と全振幅に不変な枝確率を与える。一方、作用殻そのものの容量は全振幅に共変である。この区別により、信号のray情報と有限作用資源を混同しない。$\delta=0$ の零容量枝は状態数零であり、活性支持の外に置く。正の全枝混合率を必要とする粒子位置熱化では $\delta>0$ を使うが、中央の1回限りのQ2読出しでは活性支持上の直接標本化に $\delta=0$ を使える。

## 有効自由エネルギーとR161への接続

作用殻fiberを消去した位置枝の有効自由エネルギーを

```math
F_i^{\rm sh}(v)
=
-\Theta\log\Omega_i^\delta(v)
```

とする。全枝状態数の基準を

```math
F_{\rm eq}^{\rm sh}(v)
=
-\Theta
\log
\sum_j\Omega_j^\delta(v)
```

と置けば、付録Kの地形は

```math
\begin{aligned}
E_i^\delta(v)
&=
F_i^{\rm sh}(v)-F_{\rm eq}^{\rm sh}(v)\\
&=
-\Theta\log\pi_i^\delta(v)
\end{aligned}
```

として得られる。従って $E_i^\delta$ は裸の配置エネルギーではなく、作用殻を消去した条件付き中間状態有効自由エネルギーである。全系の平衡Hamiltonianと周辺化を別に与えた場合を除き、これを無条件に平均力Hamiltonianとは呼ばない。粗視化後の確率過程と微視的な仕事・熱を同一視するには追加条件が必要である [50,51]。

状態数を残す表示と、作用殻を消去した表示は同値だが、同じ縮約分配関数内で混ぜない。すなわち

```math
P_i^\delta
=
\frac{\Omega_i^\delta}{\sum_j\Omega_j^\delta}
```

を使う**作用殻明示表示**と、

```math
P_i^\delta
=
\frac{e^{-\beta E_i^\delta}}
{\sum_je^{-\beta E_j^\delta}}
```

を使う**作用殻消去表示**のどちらか一方を選ぶ。$\Omega_i^\delta e^{-\beta E_i^\delta}$ を同じ分配関数の枝重みとして掛けると状態数を2回数え、$\Omega_i^2$ に比例するため禁止する。

R161の平方根率は

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\exp
\left[
-\frac{\beta}{2}
\left(
E_j^\delta-E_i^\delta
\right)
\right]
```

と書ける。R164は定常重みと有効自由エネルギーの起源を与えるが、対称活動度 $a_{ij}$ の大きさや平方根分割そのものを作用殻から一意に導かない。R161はその有効地形に整合する局所再平衡化定理として独立に必要である。

## 直接作用分配次元の剛性

活性作用に加えて、枝容量を直接分配する明反応作用が $q$ 本ある場合、固定作用殻は $q+1$ 作用からなる。一般容量公式により

```math
\Omega_{q+1}(A_i)
\propto
A_i^q
```

となる。

<!-- theorem-start:proposition -->
**命題（作用分配次元の剛性）**

枝間で共通なLiouville規約の下で、正規化状態数は

```math
P_i^{(q)}
=
\frac{(A_i^\delta)^q}
{\sum_j(A_j^\delta)^q}
```

である。全ての正容量族に対してR164の線形重みを保つのは $q=1$、すなわち2作用殻だけである。
<!-- theorem-end:proposition -->

作用を直接受け取らず、全枝に同じ因子 $S(v)>0$ を掛けるspectator自由度は

```math
\widetilde\Omega_i^\delta(v)
=
S(v)\Omega_i^\delta(v)
```

として規格化で消える。枝依存spectator体積、異なる角周期、異なるcoarea Jacobianは消えず、枝対称性誤差に数える。

## 入口流束と枝非対称誤差

作用殻状態を配置遷移入口として数える場合、正方向流束を

```math
\mathscr F_i
=
\lambda_i\Omega_i^\delta
```

と書く。$\lambda_i$ は法線速度、反応面の向き、透過率、coarea因子、入口窓、直接分配しないspectator体積を含む。$\lambda_i=\lambda>0$ が全枝で共通なら、流束頻度もR164の $\pi_i^\delta$ に一致する。

一般に $\lambda_i=\lambda(1+\eta_i)$、$|\eta_i|\leq\varepsilon_{\rm sym}<1$ とする。流束分布を $P^{\rm flux}$ とすれば

```math
D_{\rm TV}
\left(
P^{\rm flux},
\pi^\delta
\right)
\leq
\frac{\varepsilon_{\rm sym}}
{1-\varepsilon_{\rm sym}}.
```

この誤差は、R161の混合誤差またはR162の衝突bath誤差へ隠さず、作用殻準備の枝対称性誤差として別に記帳する。

## 滑らかな有限幅作用容量

厳密デルタ殻は条件付き状態数の解析極限である。有限剛性の滑らかな実装候補として、枝 $i$ に

```math
H_{\kappa,i}
=
\frac{\kappa}{2}
\left(
K_i+I_i-A_i^\delta(v)
\right)^2,
\qquad
\kappa>0
```

を置く。角積分後の条件付き分配関数は

```math
Z_{\kappa,i}(v)
=
(2\pi)^2
\int_0^\infty
s
\exp
\left[
-\frac{\beta\kappa}{2}
\left(s-A_i^\delta(v)\right)^2
\right]
ds.
```

$a=\beta\kappa/2$、$x_i=\sqrt a A_i^\delta$ とすれば、積分は厳密に

```math
Z_{\kappa,i}
=
(2\pi)^2
\left[
\frac{e^{-x_i^2}}{2a}
+
\frac{A_i^\delta\sqrt\pi}{2\sqrt a}
\left(
1+\operatorname{erf}x_i
\right)
\right]
```

である。$C_\kappa=(2\pi)^2\sqrt{\pi/a}$ と置くと

```math
Z_{\kappa,i}
=
C_\kappa A_i^\delta
\left(
1+r_i
\right),
```

```math
0
\leq
r_i
\leq
\frac{e^{-x_i^2}}
{2\sqrt\pi x_i}
```

が $x_i>0$ で成り立つ。$\widehat\pi_i^\delta=Z_{\kappa,i}/\sum_jZ_{\kappa,j}$、$\rho=\max_ir_i$ とすれば

```math
D_{\rm TV}
\left(
\widehat\pi^\delta,
\pi^\delta
\right)
\leq
\frac{\rho}{2}.
```

これを有限幅誤差 $\varepsilon_{\rm width}$ とする。

## node、零seed、有限資源

安全試行で

```math
v^\dagger v
\geq
r_*>0,
\qquad
q_{\min}
=
\min_iq_i
```

とすれば

```math
A_i^\delta(v)
\geq
\mathcal J_0\delta q_{\min}r_*.
```

従って滑らかな有限幅誤差を全bath rayで一様に小さくするには

```math
x_{\min}
=
\sqrt{\frac{\beta\kappa}{2}}
\mathcal J_0\delta q_{\min}r_*
```

を十分大きく保つ必要がある。$\delta\downarrow0$ で他の尺度を固定するなら、必要剛性は下界の次数として少なくとも

```math
\kappa
=
\Omega
\left(
\delta^{-2}
\right)
```

と増大する。$\kappa=\Theta(\delta^{-2})$ はこの下界を満たす代表的な選択であり、より大きい剛性を排除しない。これは付録Kの対数地形幅、衝突流束、混合時間に加わる独立な資源発散である。

$\delta=0$ で $A_i=0$ となるnodeは、厳密殻では状態数零である。一方、有限 $\kappa$ の滑らかな分配関数は $A_i=0$ でも正の端点寄与を持つため、厳密nodeを有限剛性で再現しない。零seed $v=0$ ではrayも規格化枝重みも定義せず、正式な無反応結果とする。安全閾値 $r_*$ 未満の試行、容量比較境界、枝選択失敗も完全結果集合へ残し、除外後の2値再規格化を行わない。

## R162と粗視化経路熱力学の語義

R164後の付録Kでは、$E_i^\delta$ を作用殻fiberの有効自由エネルギーとして読む。辺障壁は

```math
B_{ij}^\delta(v)
=
B_{ij}^0
+
\frac12
\left[
E_i^\delta(v)+E_j^\delta(v)
\right]
```

と書ける。全ての $E_i^\delta$ を共通関数 $g(v)$ だけ移し、障壁も同じだけ移せば、活性化差 $B_{ij}^\delta-E_i^\delta$、衝突率、経路確率は不変である。

第2章の正逆経路確率比と積分ゆらぎ関係は、粗視化された粒子位置跳躍過程について厳密である。作用殻明示表示での殻自由エネルギー仕事と、作用殻消去表示での相対有効仕事を

```math
W_i^{\rm sh}
=
\Delta F_i^{\rm sh},
\qquad
W_i^{\rm rel}
=
\Delta E_i
=
W_i^{\rm sh}-\Delta F_{\rm eq}^{\rm sh}
```

と区別する。全作用を保存するunitary操作では $F_{\rm eq}^{\rm sh}$ の共通項が一定になり得るが、pump、容量制御器、resetが作用を出し入れする一般の周期では一定とは限らない。従来のquench量

```math
W_i^{\rm rel}
=
E_i^\delta(v^+)-E_i^\delta(v^-)
```

と平均相対エントロピー恒等式も、相対有効仕事として厳密である。ただし、作用殻を実際に変形する有限時間過程、殻内平衡化、制御器反作用を含めなければ、$W^{\rm rel}$ を装置全体の機械仕事、跳躍時の有効自由エネルギー差を全微視的熱と同一視しない。ゆらぎの定理はR164で得た地形の下流整合性を検査するが、状態数の線形則を選び出す根拠ではない。

次元は全章で固定する。$J_{\rm sig},J_i,A_i,J_{\rm ref}$ は作用、$\Omega_i$ は無次元、$\Theta,E_i,F_i,B_{ij}$ と衝突セルエネルギーはエネルギー、$\beta$ はエネルギーの逆数、$\kappa$ はエネルギー毎作用2乗、跳躍率と衝突率は時間の逆数である。

## Q1・Q2・Q3への接続と非主張

M50をQ1、Q2、Q3の1回の作用殻準備と粒子位置再平衡化へ使うとき、共通誤差を

```math
\begin{aligned}
\varepsilon_{M50}
={}&
\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm sym}
+\varepsilon_{\rm ad}\\
&+\varepsilon_\delta
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
\end{aligned}
```

と定める。$\varepsilon_{\rm cap}$ は有限容量結合、$\varepsilon_{\rm width}$ は有限剛性、$\varepsilon_{\rm sym}$ は枝非対称、$\varepsilon_{\rm ad}$ は殻内条件付き平衡化と有効地形切替、$\varepsilon_\delta$ は正則化、$\varepsilon_{\rm mix}$ は有限時間粒子位置混合、$\varepsilon_{\rm coll}$ は有限衝突近似、$\varepsilon_{\rm hold}$ は信号保持反作用である。$\varepsilon_{\rm supp}$ はM50内部誤差でなく、統計的rayから単一試行入力への上流受渡し誤差として別に記帳する。有限時間Hopf誤差から評価した同じ偏差を両方へ加えない。R181DではSWAP、容量latch、shell、mixing、collection、lock、record、clockを $\varepsilon_{170}^{\rm end}$ へ各1回だけ数える。

R164の達成範囲は「条件付き厳密結果＋滑らかな有限幅近似」である。本付録は次を主張しない。

1. 枝容量 $A_i^\delta(v)$ を作る結合が任意のQ1、Q2、Q3信号状態から自動的に準備されること。
2. 作用殻Liouville測度が有限時間の局所力学で一様またはGibbs的に準備されること。
3. 枝対称な余面積因子と入口流束が信号担体だけから自動的に従うこと。
4. 作用殻とR162の衝突熱浴が同一の物理部分系であること。
5. 作用殻、信号保持制御器、衝突セルを含む全微視的仕事・熱収支が粗視化経路熱力学だけから従うこと。
6. $\delta=0$ のnodeを有限剛性、有限衝突流束、有限混合時間で一様に実現できること。
7. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。
8. 旧M15の入口標本化、殻等方混合、標本化後再埋込み、全測定周期が再び現行結果になること。

R164をR143、R144へ接続すると、Q1-2のBorn分布、同軸反復分布、異軸逐次分布を支える。Q1-2全体はZeno部分が未達であるため部分達成のままであり、R164の有限局所Hamiltonian統合や完全周期は達成条件に含めない。Q2-1ではR181DがM54の実際の末端4mode信号をcanonical SWAPと容量latchでR164へ接続する。R181B/R181Cはlift、CNOT、逆演算を与えるが、容量pointer--作用殻境界と全末端工程の一体化は条件として残るためQ2-1は条件付き達成である。Q2-2ではR180Aが同じ実信号から枝作用と2翼templateを作り、R180Cが切断後局所因子化を追加するが、単一装置統合を条件とするため条件付き達成のままである。Q3ではR164を準備終了面で一度だけ使って初期M42位置を作り、R172--R174が同じ粒子を輸送する。作用容量結合、M42 bath、clock、記録の統合を自動的に与えないため、Q3-4A、Q3-5は条件付き達成のままである。Q3-4BにはW型全空間分布と周期回帰を結ぶ追加構成が必要である。

現行Q2-3ではR181Bの反復liftが作る8mode信号を同じ永続状態bathでR181Cの二段gateへ通す。末端だけでR181Dを $m=L=8$、$\Psi=I_8$ へ特殊化する。規格化出力信号を $Z_{\rm out}$ とすればR164の枝比は $(|(Z_{\rm out})_y|^2+\delta q_y)/(1+\delta)$ となり、正則化誤差は高々 $\delta/(1+\delta)$ である。残る末端一体化条件はQ2-1と共通である。

Q2-4のM54では、R181Dが各bitの信号作用をraw容量 $J_{u,0},J_{u,1}$ へlatchし、regularized容量 $A_{u,b}^\delta$ だけをR164/R170作用殻へ渡す。raw容量はcutoff比較に残し、selectorをlockした後に可逆filterを作用する。$L=2^n$ のsignal modeは受動資源として計上し、局所gateとprojectorをR181C/R181Dの一様規則で作用させる。

# M54物理template-port準備

> **位置づけ：** 非規格化物理templateだけをcouplerへ入れるR181Aの採用開放方程式、seed測度の押出し、有限時間率、radial-only特殊化、切断後輸送を証明する。


## 目的と存在論

本付録は、量子状態に対応させる階数1統計を初期分布へ直接置かず、有限次元の実古典担体を開放driftで有限時間準備するM54のtemplate portを定義する。Q1とQ2は同じ模型族の特殊化である。Q3は準備portの入出力契約だけを上流に使う。

M54の記述階層は次の通りである。

| 階層 | M54での対象 | 因果的役割 |
|---|---|---|
| 単一試行の物理状態 | 実正準担体 $(Q,P)$、template正準対 $(Q^w,P^w)$、clock、port履歴 | 開放driftが直接作用し、切断面で下流へ渡る |
| 単一試行の派生座標 | $z=(Q+iP)/\sqrt{2\mathcal J_0}$、$w=(Q^w+iP^w)/\sqrt{2\mathcal J_0}$ | 実方程式を簡潔に表示する。追加の物理場ではない |
| 外部制御 | $g$、$\kappa$、$\lambda_{\rm prep}$、template設定 | pump、sink、port開閉を指定する |
| 集団統計 | $C_Z=\mathbb E[ZZ^\dagger]/\mathbb E[Z^\dagger Z]$、$c$、$\Pi_c$ | 準備結果を記述する。単一試行controllerへ書き戻さない |
| 下流の物理入力 | 各試行の $z(\omega)$ またはその正準SWAP先 | M50が作用容量を作る |
| 観測結果 | M54単独では存在しない | M50/R170が粒子位置と外部記録を作る |

templateの規格化方向 $c=w/\|w\|$ は解析記号である。物理装置は $w$ とその二次形式だけをcouplerへ入れ、$w/\|w\|$ を作る除算器を持たない。開放流の押出し後に解析上 $C_Z\simeq cc^\dagger$ と評価する。

## 実正準担体と可逆生成子

$m$ 個の実正準対を列ベクトル $Q,P\in\mathbb R^m$ とする。派生複素座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

と定める。Hermitian行列を

```math
G=A+iB,
\qquad
A^{\mathsf T}=A,
\qquad
B^{\mathsf T}=-B
```

と分解する。実Hamiltonian

```math
H_G
=
\frac{1}{2\mathcal J_0}
\left(Q^{\mathsf T}AQ+P^{\mathsf T}AP\right)
+\frac{1}{\mathcal J_0}P^{\mathsf T}BQ
```

は

```math
\dot Q
=
\frac{AP+BQ}{\mathcal J_0},
\qquad
\dot P
=
\frac{-AQ+BP}{\mathcal J_0}
```

を与え、複素表示では

```math
i\mathcal J_0\dot z=Gz
```

となる。従って有限次元の複素線形伝播は実正準担体の可逆運動として厳密に表せる。ただし、この代数的実現だけから、状態準備、Born型結果、粒子位置、局所性、熱力学的自然さは従わない。

$B=0$ なら $Q$ と $P$ の同じ実対称結合だけでよい。M37の位置ばね網は、さらに結合の局所性と正値性を課し、回転包絡に対して有限時間近似を与える制限された物理実現である。M54の一般 $H_G$ をM37の局所位置結合から導出済みとは扱わない。

## M54の開放方程式を実変数で書く

物理template作用を $\alpha=w^\dagger w>0$、解析上の目標射影を

```math
\Pi_c=C+iD,
\qquad
C^{\mathsf T}=C,
\qquad
D^{\mathsf T}=-D
```

と書き、担体作用比を

```math
r
=
z^\dagger z
=
\frac{Q^{\mathsf T}Q+P^{\mathsf T}P}{2\mathcal J_0}
```

とする。第2章のM54方程式と等価な実方程式は

```math
\dot Q
=
\frac{AP+BQ}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(J_*-r)Q
-\kappa\alpha\{(I-C)Q+DP\}
\right],
```

```math
\dot P
=
\frac{-AQ+BP}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(J_*-r)P
-\kappa\alpha\{(I-C)P-DQ\}
\right].
```

これがM54の縮約ミクロ方程式である。$Q$ と $P$ が各試行の状態であり、右辺はそれらの有限次元driftとして完全に指定される。最小模型では確率微分項を置かない。

| 要素 | 方程式上の項 | 物理的分類 |
|---|---|---|
| 可逆担体 | $G$ または $A,B$ | Hamiltonian流 |
| 動径pump | $g(J_*-r)(Q,P)$ | action供給と飽和を表す開放drift |
| transverse sink | $-\kappa\{(w^\dagger w)z-w(w^\dagger z)\}$ | 非規格化templateで直交成分を外部portへ捨てる開放drift |
| clock・切断器 | $\lambda_{\rm prep}$ | 準備portの接続時間を指定する外部制御 |
| template | $(Q^w,P^w)$ | 目標rayを物理的に保持する装置自由度 |

M54はpumpとsinkの背後にある有限bath自由度、衝突則、仕事源、排熱先を消去した基礎開放モデルである。従って上の式からの結論は厳密でも、この式を有限閉鎖Hamiltonianから導出したとは呼ばない。有限bath持上げ、雑音、揺らぎ散逸関係、総仕事・熱・エントロピー生成は後続課題である。

## seed測度、押出し測度、無反応

試行開始面で、実状態と空の履歴registerに基準測度

```math
\mu_0(dQ\,dP\,dH_{\rm port})
```

を置く。$\mu_0$ は目標射影そのものを階数1共分散として埋め込まない。template設定 $c$ に対するM54流を $\Phi_c^t$ と書けば、準備時刻の測度は

```math
\mu_c^t=(\Phi_c^t)_\#\mu_0
```

である。目標依存性は初期分布へ隠さず、template設定後のdriftに現れる。

相互作用表示の初期値を $\widetilde z_0=a_0c+p_0$、$c^\dagger p_0=0$ と分ける。安全事象を

```math
G_*
=
\{|a_0|\geq a_*\}
\cap
\{\|\widetilde z_0\|\leq R_*\}
```

とする。$a_0=0$ の直交超平面はM54で不変であり、そこから目標rayは生成されない。有限 $a_*$ を採ることで有限時間の一様上界を得る。$G_*^c$ を捨てず、下流の完全結果集合で無反応へ送る。

連続なseed測度では直交超平面の測度が零でも、$|a_0|$ が小さい近傍の質量は有限時間資源に影響する。$a_*\downarrow0$ とすると無反応質量は減らせるが、$q_*=(R_*^2-a_*^2)/a_*^2$ と必要準備時間が増える。この交換を無限時間極限で隠さない。

## R181Aの証明

M54のunitary $U(t)$ で回る相互作用表示を使う。$c$ を固定し、$\widetilde z=ac+p$、$c^\dagger p=0$ と置けば

```math
\frac{da}{d\tau}
=
g(J_*-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(J_*-\|\widetilde z\|^2)-\kappa\alpha\right]p.
```

$a\neq0$ では両式の共通動径項が消え、

```math
\frac{d}{d\tau}\left(\frac{p}{a}\right)
=
-\kappa\alpha\frac{p}{a},
\qquad
\frac{p(\tau)}{a(\tau)}
=
\frac{p_0}{a_0}e^{-\kappa\alpha\tau}
```

を得る。$G_*$ 上では

```math
\frac{\|p_0\|^2}{|a_0|^2}
\leq
\frac{R_*^2-a_*^2}{a_*^2}
=q_*.
```

純粋ray距離は

```math
D_{\rm pure}
\left(
\frac{\widetilde z\widetilde z^\dagger}
{\widetilde z^\dagger\widetilde z},
cc^\dagger
\right)
=
\frac{\|p\|}{\sqrt{|a|^2+\|p\|^2}}
\leq
\frac{\|p\|}{|a|}
\leq
\sqrt{q_*}e^{-\kappa\alpha\tau}.
```

unitary変換はこの距離を保存するので第2章の時刻 $t$ の上界が従う。

作用重み付き第2モーメントに対し、全安全試行で $\|p\|^2\leq q_*e^{-2\kappa\alpha\tau}|a|^2$ だから

```math
1-\operatorname{tr}(\Pi_cC_{Z,G_*})
\leq
\frac{q_*e^{-2\kappa\alpha\tau}}
{1+q_*e^{-2\kappa\alpha\tau}}.
```

純粋射影とのtrace距離に対する上界を使えば

```math
D_{\rm tr}(C_{Z,G_*},\Pi_c)
\leq
\sqrt{q_*}e^{-\kappa\alpha\tau}
```

となる。

動径収束も確認する。$r=\|\widetilde z\|^2$ とすると、transverse sinkの寄与は非正であり、$p/a$ は率 $\kappa\alpha$ で減衰する。十分大きい有限時刻以後は $r$ の上下比較方程式を目標 $J_*$ のlogistic方程式で挟める。従って $|a|^2\to J_*$、$p\to0$ であり、有界seed集合上の全ベクトル収束は $\min\{2gJ_*,\kappa\alpha\}$ の指数率で抑えられる。$\kappa=0$ なら方向を固定したまま $\dot r=2gr(J_*-r)$ となり、R181Dのradial-only repumpを得る。

準備終了後に $\lambda_{\rm prep}=0$ とすれば、開放項は消えて $i\mathcal J_0\dot z=Gz$ だけが残る。各試行の実正準状態は可逆に発展し、R135により第2モーメントはunitary共役で輸送される。以上でR181Aを得る。

## M50への受渡しと二乗則の位置

M54切断面の各安全試行について、M50へ渡すのは $c$ または $C_Z$ ではなく、実正準担体から得た $z(\omega)$ である。等長埋込み $\Psi$ に対するM50の理想ray重みは

```math
w_i(z)
=
\frac{|(\Psi z)_i|^2}{z^\dagger z}.
```

M54のray上界とR168により、無反応を含む実分布を、

```math
p_c^{\rm id}(i)
=
P(G_*)
\frac{|(\Psi c)_i|^2+\delta q_i}{1+\delta},
\qquad
p_c^{\rm id}(\varnothing)=P(G_*^c)
```

へ比較できる。M54由来のray誤差だけなら

```math
D_{\rm TV}(p^{\rm M54\to M50},p_c^{\rm id})
\leq
\frac{P(G_*)\sqrt{q_*}e^{-\kappa\alpha\tau}}
{1+\delta}
```

である。実際のR170では、これに容量、作用殻、混合、衝突、保持、固定、記録の誤差を別に加える。

ここで $|(\Psi c)_i|^2$ は、M54が作った階数1第2モーメントの対角である。同じ式をM50側では各試行の作用比として読む。従って二乗形の状態依存性は準備済み統計に由来し、排他的な単一結果はM50の作用殻状態数と粒子位置熱化に由来する。M54だけで結果頻度が生じるとも、M50が目標rayを無から準備するとも解釈しない。

## 現行系列への特殊化と非主張

| 系列 | M54から供給できるもの | M54から従わないもの |
|---|---|---|
| Q1 | $m=2$、W型生成子、目標Bloch ray | W型粒子位置、Born枝、測定後template交換、周期収支 |
| Q2-1 | 指定した局所rayの試行集団準備 | R181Bの1試行tensor-lift、R181CのCNOT・逆演算、R181Dの末端接続 |
| Q2-3 | 指定した3部分系初期rayの試行集団準備 | R181B/R181Cの反復lift・二段gate、R177、R181Dの末端接続 |
| Q2-4 | root sourceのradial整形と各nodeのradial-only repump | R181Cのgate合成、R170のselector形成、R181Dのfilter、R179のbank供給 |
| Q2-2 | setting-free局所seedまたは有限ray template | singlet交差モーメント、paired-Hopf強matching、Bell因果構造 |
| Q3 | M37へ渡すrank-one初期標本集団とM42初期位置用の単一試行信号 | M37--M42との同一局所Hamiltonian統合、空間伝播、終位置記録 |

M54のR181A portは状態準備の共通開放模型を与えるが、次を主張しない。

1. pump、sink、template、clockを含む有限閉鎖Hamiltonian実現。
2. 雑音付き定常測度、揺らぎ散逸関係、有限bathによる誤差上界。
3. M54とM37、M42、M47、M50、R180 receiverが同じ物理装置であること。
4. M54単独で粒子位置、Born型排他的結果、測定後状態を生成すること。
5. template設定から独立に任意の未知入力状態を自己準備すること。
6. 試行列の独立同分布性または二項型有限標本揺らぎ。

これらを追加するときは、M54の開放portを構成する有限bath、仕事源、排熱、情報履歴を完全状態へ加え、準備前測度から切断面測度までの因果鎖を再監査する。

# M37担体上のM42局在トークン

> **位置づけ：** M37の実振動子担体から局所辺流を作り、単一試行の局在粒子トークンを輸送するM42を定義する。R172の等変性、R173の節一様正則化と有限衝突Hamiltonian近似、R174のM54--M37--M42誤差受渡しを証明する。


## 二層模型と単一試行の完全状態

Q3の現行基本模型は、M37担体層とM42粒子層からなる。M37は有限グラフ $G=(V,E)$ の各頂点に置いた実正準対 $(q_i,p_i)$ と局所ばね結合を持つ。M42は同じグラフ上の1個の局在粒子位置

```math
X_t\in V
```

を持つ。M42の粒子位置はM37の振動子座標でも、複素包絡の成分でもない。

1試行の完全状態には、少なくとも次を含める。

```math
\Gamma_t
=
\left(
q(t),p(t),X_t,n_t,s_t,
\{\xi_n,\zeta_n\}_{n=1}^{N_{\rm cell}},
D_t,H_t
\right).
```

$n_t$ は使用中bath cell、$s_t$ は累積hazard、$\xi_n,\zeta_n\in(0,1)$ は開始面で調製した有限bath cellの座標、$D_t$ は固定時刻の位置記録、$H_t$ は使用済みcellと向きの履歴である。複素包絡

```math
b_i(t)
=
e^{i\omega_0t}
\frac{Q_i(t)+iP_i(t)}{\sqrt{2\mathcal J_0}}
```

はM37の実正準状態の派生表示であり、追加の物理場ではない。量子状態に対応させるray、$|c_i|^2$、$C_Z$、粒子位置分布 $P(X_t=i)$ は試行集団の統計記述である。M42のcontrollerが読むのは各試行の局所M37座標、現在位置、局所bath cell、clock、履歴だけであり、$c$、$C_Z$、全粒子位置分布を単一試行へ書き戻さない。

M54の準備後にM42を開始するとき、同じ試行のM37入力信号にM50/R164の作用殻状態数を一度だけ適用し、初期位置 $X_0$ を生成する。この位置がM42の全輸送区間を通して存在する粒子トークンである。終時刻に別のM50位置を再標本化せず、R112の局所記録回路は既存の $X_T$ を読むだけである。

## M37有効担体の局所辺流

R86の目標有効包絡を、固定有限時間区間で

```math
i\mathcal J_0\dot b_L
=
h_Lb_L,
\qquad
b_L^\dagger b_L=1
```

とする。$h_L=h_L^\dagger$ は $G$ に局所的である。頂点重みと有向辺流を

```math
p_i(t)=|b_{L,i}(t)|^2,
```

```math
J_{i\to j}(t)
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left[
b_{L,j}(t)^*h_{L,ji}b_{L,i}(t)
\right]
```

と定める。Hermitian性と局所性から

```math
J_{i\to j}=-J_{j\to i},
\qquad
\dot p_i
=
\sum_{j:j\sim i}J_{j\to i}
```

が成り立つ。M37の厳密局所包絡 $b$ は反回転項を持つので、この連続方程式をそのまま厳密ミクロ流とは呼ばない。$b$ から計算した局所量はR86の誤差範囲で $b_L$ の流を近似するcontroller入力である。

$p_i(t)>0$ で最小率を

```math
\lambda_{i\to j}(t)
=
\frac{[J_{i\to j}(t)]_+}{p_i(t)},
\qquad
[x]_+=\max\{x,0\}
```

とする。零重み頂点は等変分布の下で占有されない。理想率は連続方程式と局所性だけから一意に強制されるのではなく、余分な対称往復流を加えない最小活動度の採用則である。

### R172の完全形

**R172の仮定と結論。**

有限グラフ、時間連続な有界局所Hermitian生成子、上の最小率を仮定する。$P(X_0=i)=|b_{L,i}(0)|^2$ なら、M42の理想位置過程は全ての有限時刻で

```math
P(X_t=i)=|b_{L,i}(t)|^2
```

を満たす。さらに $h_1=\sup_t\max_i\sum_{j:j\sim i}|h_{L,ij}(t)|$ とすれば、有限時間 $T$ の期待跳躍数は

```math
\mathbb E[N_T]
\leq
\frac{h_1T}{\mathcal J_0}
```

であり、有限時間爆発はない。

<!-- theorem-start:proof -->
**証明（R172）**

位置分布を $\pi_i$ とするとmaster方程式は

```math
\dot\pi_i
=
\sum_j
\left(
\pi_j\lambda_{j\to i}
-
\pi_i\lambda_{i\to j}
\right).
```

$\pi_i=p_i$ を代入すれば、各辺で正部分の差が元の反対称流に戻り、$\dot\pi_i=\sum_jJ_{j\to i}=\dot p_i$ となる。有限状態master方程式の一意性から等変性が従う。また $2\sqrt{p_ip_j}\leq p_i+p_j$ を各辺へ使うと、等変分布下の期待総脱出率は $h_1/\mathcal J_0$ 以下である。時間積分して期待跳躍数上界を得る。証明終。
<!-- theorem-end:proof -->

R172は初期分布を無償で仮定する定理ではない。現行因果鎖ではM54がM37担体のrank-one統計方向を準備し、M50/R164の1回の作用殻選択が初期M42位置を作る。R172はその同じ位置を輸送する。

## 単一試行の明示開放方程式

理想M42は、有限bath tapeで切断したpiecewise deterministic open systemとして各試行を明示できる。現在位置を $i=X_t$ とし、全脱出率と条件付き辺重みを

```math
\Lambda_i(t)=\sum_{j:j\sim i}\lambda_{i\to j}(t),
\qquad
r_{i\to j}(t)=\frac{\lambda_{i\to j}(t)}{\Lambda_i(t)}
```

とする。$\Lambda_i=0$ では待機する。cell $n$ の閾値を $a_n=-\log\xi_n$ とし、跳躍の間は

```math
\dot q_i=\frac{\partial H_{37}}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H_{37}}{\partial q_i},
\qquad
\dot s=\Lambda_{X_t}(t),
\qquad
\dot X_t=0
```

で進める。$s=a_n$ に到達したとき、$\zeta_n$ が累積区間

```math
\sum_{k<j}r_{i\to k}(t)
\leq
\zeta_n
<
\sum_{k\leq j}r_{i\to k}(t)
```

に入る唯一の隣接頂点 $j$ へ $X:i\mapsto j$ と更新し、$(i,j,n,t)$ を $H_t$ へ記録し、$s\mapsto0$、$n\mapsto n+1$ とする。使用可能cellを超えた試行はoverflow無反応へ送る。$\xi_n,\zeta_n$ は時間ごとに外部乱数を注入する値でなく、開始面の有限bath状態である。

この開放表示は単一試行の状態と更新則を明示するが、節の近くで率が大きくなり得る。有限装置には次節の正則化率を使う。

## 節一様正則化と有限Hamiltonian近似

無次元重み正則化 $\rho>0$ と率尺度 $\sigma>0$ を分け、

```math
r_\sigma(x)
=
\frac12
\left(
x+\sqrt{x^2+\sigma^2}
\right),
```

```math
\lambda_{i\to j}^{\rho,\sigma}(b)
=
\frac{r_\sigma(J_{i\to j}(b))}{|b_i|^2+\rho}
```

とする。$\sigma$ は時間の逆数を持ち、$\rho$ と同じ量ではない。最大次数を $d_*$ とすると、固定有限グラフで

```math
\Lambda_*^{\rho,\sigma}
\leq
\frac{h_1}{\mathcal J_0\sqrt\rho}
+
\frac{d_*\sigma}{2\rho}
```

であり、節でも有限である。$H_E=\sup_t\sum_{\{i,j\}\in E}|h_{L,ij}(t)|$ と置く。

### R173の完全形

**R173の仮定と結論。**

正則化M42を理想分布と同じ初期分布から開始する。任意の固定有限時間 $T$ について

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
P(X_t^{\rho,\sigma}\in\cdot),
|b_L(t)|^2
\right)
\leq
T
\left[
|E|\sigma
+
\frac{2H_E}{\mathcal J_0}\sqrt\rho
\right].
```

さらに固定した $\rho,\sigma,T$ について、時間を有限個の窓へ分け、各窓で率を凍結する。辺 $e=\{i,j\}$ と時間窓 $m$ ごとに

```math
\nu_{e,m}
\geq
\max\left\{
\lambda_{i\to j}^{\rho,\sigma},
\lambda_{j\to i}^{\rho,\sigma}
\right\}
```

となる有限試行率を選び、各入射cellに方向タグ $d_n$、物理的な一様閾値座標 $u_n\in(0,1)$、到着clock、共役変数、空の履歴sector、仕事registerを持たせる。$X=i$ から $j$ 向きに到着したcellは

```math
u_n
<
\frac{\lambda_{i\to j}^{\rho,\sigma}}{\nu_{e,m}}
```

なら通過し、それ以外は反射する。逆向きには別の物理閾値 $\lambda_{j\to i}^{\rho,\sigma}/\nu_{e,m}$ を使う。従って縮約通過率は各向きで正確に $\lambda^{\rho,\sigma}$ となる。

通過・反射後にもsource、target、窓、cell番号、未消去の $u_n$ を履歴sectorへ保持し、方向別controllerのエネルギー差を仕事registerへ移す。閾値で分けた各正準phase cellを同じLiouville体積の出射・履歴cellへ並進とshearで写し、未使用sector上まで有限置換として延長すれば、写像は一対一かつ正準にできる。閾値を有限有理分割で近似し、境界を滑らかなHamiltonian shearで置換すると、固定有限個のcellについて駆動Hamiltonian散乱列が得られる。cell overflow、閾値分割、境界平滑化、時間凍結、clock、仕事register切断の失敗は無反応へ残す。

これはR162と同じ有限衝突・履歴保存の設計様式を使うが、R162の詳細釣合い率を代入する構成ではない。一般のM42率は辺ごとの正逆率比が平衡ポテンシャル差から決まらないので、方向別controllerと仕事registerを持つ駆動衝突模型である。

<!-- theorem-start:proof -->
**証明（R173）**

$0\leq r_\sigma(x)-[x]_+\leq\sigma/2$ と $|J_{i\to j}|\leq2|h_{ij}|\sqrt{p_ip_j}/\mathcal J_0$ を使うと、理想辺流と正則化辺流の差は

```math
\left|
\frac{p_i}{p_i+\rho}r_\sigma(J_{i\to j})
-[J_{i\to j}]_+
\right|
\leq
\frac\sigma2
+
\frac{|h_{ij}|}{\mathcal J_0}\sqrt\rho
```

である。全辺を足し、Markov半群の全変動縮小性とDuhamel公式を使えば表示上界を得る。固定正則化では率が有界かつ滑らかなので、有限窓の凍結生成子列が時間順序指数へ収束する。各凍結率に上の方向別通過確率を持つ有限cellを置けば縮約率が一致する。履歴を消去しない正準phase-cell置換、有限分割、Hamiltonian平滑化の誤差を有限個の窓で加えれば、駆動Hamiltonian衝突列による任意精度の近似を得る。証明終。
<!-- theorem-end:proof -->

有限 $\rho,\sigma$ では小さな逆向き流が残る。$\rho,\sigma\downarrow0$ では必要最大率、衝突cell数、障壁精度が発散し得るため、1つの固定装置が厳密nodeを再現するとは主張しない。

## M37担体誤差からM42への受渡し

有限装置のcontrollerは理想 $b_L$ でなくM37局所包絡 $b$ を読む。安全領域

```math
\|b(t)\|\geq a_{\rm tok}>0,
\qquad
\|b(t)\|,\|b_L(t)\|\leq R_{\rm tok}
```

を固定する。正の $\rho,\sigma$ の下では、正則化生成子 $L^{\rho,\sigma}(b)$ はこのコンパクト安全領域でLipschitzであり、ある有限定数 $K_{\rho,\sigma,a,R}$ に対して

```math
\left\|
L^{\rho,\sigma}(b)
-L^{\rho,\sigma}(b_L)
\right\|_{\rm row}
\leq
K_{\rho,\sigma,a,R}
\|b-b_L\|
```

となる。ここで $\|A\|_{\rm row}=\max_i\sum_j|A_{ij}|$ は行確率ベクトルに作用する生成子の行和normである。R86の包絡誤差を使えば、担体からtoken分布への誤差を

```math
\varepsilon_{37\to42}(T)
\leq
\frac12
TK_{\rho,\sigma,a,R}
\varepsilon_{\rm car}(T)
\sup_\omega\|\widetilde b(0;\omega)\|
```

で抑えられる。安全領域外は無反応へ残し、成功試行だけを再規格化しない。

### R174の完全形

**R174の仮定と結論。**

固定有限グラフと固定時間 $T$ を取る。M54/R181AでM37のrank-one初期担体集団を準備し、同じ試行の初期信号にM50/R164の作用殻選択を一度だけ適用して $X_0$ を作り、M37と正則化M42を同時に進め、終時刻に既存の $X_T$ をR112で局所記録する。完全結果集合に無反応を含めると、終位置の理想Born型分布との差は

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
+\varepsilon_{\rm rec}.
\end{aligned}
```

ここで $\varepsilon_{\rm prep}$ はM54のray準備とseed無反応、$\varepsilon_{\rm init}$ は初期作用殻選択、$\varepsilon_{\rm step}$ は時間凍結、$\varepsilon_{\rm coll}$ は方向別閾値分割、Hamiltonian平滑化、仕事register切断を含む有限衝突近似、$\varepsilon_{\rm over}$ はbath cell不足、$\varepsilon_{\rm clk}$ は時計、$\varepsilon_{\rm rec}$ は局所記録である。同じM37包絡偏差を $\varepsilon_{\rm prep}$、$\varepsilon_{37\to42}$、$\varepsilon_{\rm rec}$ へ重複加算しない。

<!-- theorem-start:proof -->
**証明（R174）**

R181Aの準備切断面からM37初期面への誤差、R164による1回の初期位置分布、R172の理想等変性、R173の正則化誤差、M37--M42生成子のDuhamel誤差、有限衝突列と記録の縮約誤差を因果順に三角不等式で加える。無反応質量を完全結果分布の成分として保つため、事後規格化項は生じない。証明終。
<!-- theorem-end:proof -->

M54の二乗統計と初期M42位置は独立な2つのBorn型確率源ではない。M54は担体集団のrank-one方向を準備し、R164はその単一試行信号から1個の初期粒子位置を物理化し、R172は同じ粒子を輸送する。終時刻には再抽選せず、位置記録だけを行う。

## R123--R125への下流接続

R123の束縛スペクトルと有限環境純位相緩和は、M37有効生成子とその縮約統計に関する結果として維持する。M42を追加しても、固有状態選択、冷却、不可逆緩和は従わない。

R124では3頂点障壁の初期信号から $X_0$ を一度準備し、M42を $T_{\rm bar}$ まで輸送して反対側位置を読む。R125では2経路入力ごとに同じ初期選択・輸送・記録protocolを使う。各比較のM42読出し誤差が $\varepsilon_{174}$ 以下なら、観測される障壁反対側増分と干渉分布距離はそれぞれ

```math
\alpha-2\varepsilon_{174},
\qquad
\Delta-2\varepsilon_{174}
```

以上である。M54、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所装置へ統合していないため、Q3-4AとQ3-5の条件付き達成判定は変えない。Q3-4Bの周期的W型移送は本付録の結論に含めない。

## Q3-1への非遡及

Q3-1の固定基準は、局所位置結合振動子網から空間格子上のSchrödinger型時間発展を誤差付きで導くことであり、R86が満たす。M42は、粒子を実体として持つために追加する下流強化である。R172--R174をQ3-1達成の根拠へ遡及的に加えず、M42の正則化極限が失敗してもR86の包絡縮約定理自体は失われない。

## 旧M42との差と非主張

旧M42の退役結果群は、任意に与えた物理的複素振幅場と位置過程を直接結び、Q1--Q3へ広く使う模型だった。現行M42はQ3だけに限定し、複素包絡をM37実正準状態の派生表示、rayを集団統計とする。初期二乗分布はM54準備と1回のR164選択に由来し、終時刻M50再標本化と併用しない。旧結果IDは再利用しない。

現行M42/R172--R174は次を主張しない。

1. 最小率がM37のHamiltonianだけから一意に強制されること。
2. M54、M37、作用殻、M42 bath、記録器の単一閉鎖Hamiltonian統合。
3. 1つの固定有限装置で $\rho=\sigma=0$ の厳密nodeを追跡すること。
4. 連続空間の連続粒子軌道、慣性質量、電荷、担体エネルギーの粒子への帰属。
5. 初回到達、吸収、散乱透過率、幾何学的2開口、連続運転スクリーン。
6. 多粒子、交換統計、一般複素hopping、外部磁場。
7. 独立同分布型の有限標本揺らぎ。

M42の採用により、Q3では「粒子が実在せず、終時刻にだけ位置が作られる」という読みに依存しない。一方、採用した局所率と有限衝突bathの物理的選択理由、全周期収支、連続極限は未完成課題として残る。

# M54の一様registerとprojector-tree代数

> **位置づけ：** R181Cの一様gate作用と、R181Dで使うlatch、可逆2枝filter、Born確率のtelescoping、raw cutoff、radial-only repumpを検算する。


## 目的と記号

$n$ bit文字列の集合を $\Omega_n=\{0,1\}^n$、信号空間を $\mathcal H_n=\mathbb C^{\Omega_n}$ とする。複素信号 $Z$ は実正準対の派生表示であり、量子状態を別の実体として追加しない。M54は $\dim\mathcal H_n=2^n$ を受動状態容量として許すが、外部controllerに $2^n$ 個の係数またはaddressを渡さない。

固定有限gate集合を $\mathcal G$ とする。programは $(g,S,t)$ の有限列で、$g\in\mathcal G$、$|S|\leq2$、$t$ はclock窓である。最終確率表はprogramに含めない。

## 一様sector生成子

$S$ に属さないbit列を $r$ とする。基底を $(s,r)$ の順へ並べれば、局所gateの理想作用は

```math
U_{g,S}
=
\bigoplus_{r\in\{0,1\}^{n-|S|}}g.
```

対応する実正準Hamiltonianは第2.2節と同じく

```math
H_{g,S}(t)=Z^\dagger h_{g,S}(t)Z,
\qquad
h_{g,S}(t)=\bigoplus_r h_g(t)
```

である。blockごとの項は異なる正準pairへ作用するため、同じclock係数を共有できる。静的辺は、対象bitだけが異なりspectator bitが一致する文字列pair、という有限規則で生成される。

## R181Cの証明

<!-- theorem-start:proof -->
**証明（R181C）**

sector間漏れがない場合、

```math
\widetilde U_{g,S}-U_{g,S}
=
\bigoplus_r(\widetilde g_r-g)
```

だから、直和の作用素normにより

```math
\|\widetilde U_{g,S}-U_{g,S}\|
=
\max_r\|\widetilde g_r-g\|
\leq\eta_g.
```

漏れ作用を $E_{\rm leak}$ とすれば三角不等式で $\eta_g+\eta_{\rm leak}$ を得る。gate列 $U_d\cdots U_1$ と $\widetilde U_d\cdots\widetilde U_1$ の差はtelescopingし、各因子のnormが1なら各窓誤差の和以下である。

1 bit gateはbit indexを指定する $O(n)$ 本以下、2 bit gateは素朴にはpairを指定する $O(n^2)$ 本以下の共有busで足りる。外部命令はgate数 $d$ に比例する。静的block数は指数的でも、blockを列挙する外部表は不要である。証明終。
<!-- theorem-end:proof -->

共有係数 $\chi(t)$ で $H(t)=\chi(t)H_{g,S}$ を開閉する場合、固定作用殻上の制御仕事は

```math
|W_{\rm ctrl}|
\leq
\int|\dot\chi(t)|\,\|h_g\|\,\|Z(t)\|^2\,dt
```

で抑えられる。この評価はoccupied signal作用を数え、空sector数を足し上げない。ただし結合器の製造費と受動体積は指数的でもよい資源として別に記録する。

## 2枝容量latch

計算基底bit $k$ の射影は

```math
P_{k,b}
=
\sum_{x:x_k=b}|x\rangle\langle x|.
```

容量pointer $(Q^A_{k,b},P^A_{k,b})$ と滑らかなclock窓 $\lambda_k$ に対し、理想latch生成子を

```math
H_{{\rm lat},k}
=
\lambda_k(t)
\sum_{b=0}^1
\mathcal J_0Z^\dagger P_{k,b}Z\,P^A_{k,b}
```

とする。$P^A_{k,b}=0$ のblank面ではsignal方程式への反作用が消え、pointer位置だけが容量に比例して移る。有限pointer幅、clock overlap、blank momentum誤差は $\varepsilon_{{\rm lat},k}$ へ入れる。

## 可逆filter代数

$P=P_{k,b}$、$Q=I-P=P_{k,1-b}$ と略記する。$PQ=QP=0$、$P^2=P$、$Q^2=Q$ だから、

```math
F^2
=
\begin{pmatrix}
P^2+Q^2&PQ-QP\\
QP-PQ&Q^2+P^2
\end{pmatrix}
=I.
```

$F=F^\dagger$ なので $F^\dagger F=I$ でもある。複素unitaryは実正準座標上のsymplectic直交変換を与える。

## R181Dの証明

<!-- theorem-start:proof -->
**証明（R181D）**

O.5より $F_{k,b}$ はunitaryかつinvolutionである。blank workを代入すると第1出力は $P_{k,b}Z$、第2出力は $P_{k,1-b}Z$ になる。O.4のlatchはblank momentum面で信号を変えない。射影はbit labelだけで決まるため、signal成分の列挙を必要としない。証明終。
<!-- theorem-end:proof -->

## 逐次Born確率

履歴 $y_{<k}$ のprojectorを

```math
P_{y_{<k}}
=
P_{k-1,y_{k-1}}\cdots P_{1,y_1}
```

とする。非零履歴上の条件付き確率は

```math
p_{k,b|y_{<k}}
=
\frac{
\|P_{k,b}P_{y_{<k}}Z_0\|^2
}{
\|P_{y_{<k}}Z_0\|^2
}.
```

分母と次段分子が相殺するので、全履歴確率は

```math
\prod_{k=1}^np_{k,y_k|y_{<k}}
=
\frac{\|P_yZ_0\|^2}{\|Z_0\|^2}.
```

## 希少枝切断

第 $k$ 段で条件付き確率が $\tau$ 未満の子枝を全て数える。各親履歴の下には高々2個の子があるため、その親から切られる条件付き質量は $2\tau$ 以下である。親履歴の確率を掛けて全親について和を取ると、第 $k$ 段の切断質量は $2\tau$ 以下。段の和により

```math
P_{\rm cut}\leq2n(\tau+\gamma).
```

切断枝は $\varnothing$ として残すので、これは事後選別ではない。

## Radial repump

selected signal $W$ にR181Aの $\kappa=0$ radial-only portを作用させる。

```math
\dot W=g(J_*-W^\dagger W)W.
```

この流れはrayを変えない。accept plateauでは初期作用に $\tau$ から決まる正の下限があるので、目標作用への相対誤差を $\eta_R$ 以下にする時間は $O(\log(1/(\tau\eta_R)))$ である。時間は試行前に固定でき、未知の条件付き確率を読み取るsqueezeを使わない。開放環境はradial履歴を保持し、使用後にblankとみなさない。

## R181Dの証明と誤差

<!-- theorem-start:proof -->
**証明（R181D）**

理想確率はO.7のtelescopingによりBorn分布へ一致する。O.8が切断・guard質量、O.9が固定時間repumpを与える。正則化を各段で最大 $\delta/(1+\delta)$、各段の実装channel誤差を $\bar\varepsilon_k$ とすればMarkov kernelのtelescopingにより

```math
D_{\rm TV}
\leq
2n(\tau+\gamma)
+\frac{n\delta}{1+\delta}
+\sum_{k=1}^n\bar\varepsilon_k
```

を得る。初期signalまたはgate列の誤差は、実際の末端signalのBorn分布と理想回路分布の距離として先頭に一度だけ加える。証明終。
<!-- theorem-end:proof -->

## 資源と非主張

各段のactive subspaceを物理的に圧縮しない保守的実装では、signal、anti、work、historyは $O(n2^n)$ modeを使う。縮小subspaceを詰めれば $O(2^n)$ まで減らせる可能性があるが、本結果に不要である。外部gate命令は $O(d)$、逐次出力段は $n$、nodeごとのcollision・repump資源は付録Pで評価する。

本付録は未知量子入力、適応中間測定、誤り訂正、空間局所Hamiltonian、指数受動資源の削減を主張しない。

# M54のR170駆動projector-tree receiver

> **位置づけ：** R181Dのraw容量、正則化殻、selector lock、可逆filter、radial-only repump、完全結果誤差、資源境界を証明する。旧aperture samplerは現行因果鎖に使わない。


## 目的とnode状態

深さ $m$ の二分projector-treeを考える。node $u\in\{0,1\}^{k-1}$ の入力registerを $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

```math
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
```

nodeの完全物理状態には、信号 $Z_u$、raw容量pointer $J_{u,b}$、作用殻容量 $A_{u,b}^\delta$、selector位置とlock、filter work、radial-port環境、R162 collision履歴、外部recordを含める。解析上の条件付き確率をcontrollerへ書き込まない。

## Raw容量と正則化殻

raw容量は

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

であり、$J_\Sigma=\mathcal J_0Z_u^\dagger Z_u$ である。固定 $q_b>0$、$q_0+q_1=1$ と $\delta>0$ に対し、R164/R170へ渡す容量を

```math
A_{u,b}^\delta
=J_{u,b}+\delta q_bJ_\Sigma
```

とする。従って理想R170 nodeの枝確率は

```math
\pi_{u,b}^\delta
=
\frac{A_{u,b}^\delta}{A_{u,0}^\delta+A_{u,1}^\delta}
=
\frac{p_{u,b}+\delta q_b}{1+\delta},
\qquad
p_{u,b}=\frac{J_{u,b}}{J_\Sigma}.
```

raw容量と正則化容量の役割を分ける。$A^\delta$ は作用殻を非退化にするためだけに使い、希少枝判定は $J$ に対して行う。これにより正則化で人工的に生じた小枝を安全枝と誤認しない。

## 除算を使わないcutoff

安全閾値を $\tau>0$、guard幅を $\gamma>0$ とする。比較器は

```math
J_{u,b}-(\tau\pm\gamma)J_\Sigma
```

の符号だけを読む。$J_{u,b}\geq(\tau+\gamma)J_\Sigma$ をaccept plateau、$J_{u,b}\leq(\tau-\gamma)J_\Sigma$ をreject plateau、中間を無反応guardとする。$p_{u,b}$ の除算、浮動小数点評価、状態依存clockは要らない。

深さ $m$ の理想Born treeで、$p_{u,b}<\tau+\gamma$ のedgeを通る葉の総確率は高々 $2m(\tau+\gamma)$ である。各nodeには子edgeが高々2本あり、prefix確率との積を同じlevelの全nodeで足すと、prefix確率の総和は1以下なのでlevelごとの寄与は高々 $2(\tau+\gamma)$ となる。

## Selector lockと可逆filter

branch selectorはR164の殻状態数とR161/R162の有限混合により形成し、R170のcollection窓で $b$ のplateauへ固定する。lock前にfilterを開かない。異なる $b$ のplateauとguard領域を互いに素に取り、外部record、selector、guard flagを含む拡大状態で枝の和を1対1に保つ。

signalとblank work上のfilterを

```math
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
```

とする。直交性から

```math
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I,
```

かつ

```math
F_{u,b}(Z_u,0)
=(P_{u,b}Z_u,P_{u,1-b}Z_u)
```

である。非選択成分を消去せずworkへ保持するので、filter自体はunitaryな実正準写像である。selector plateauを保持したままcontrolled-$F_{u,b}$ を作用すれば、異なる枝の像はselector座標で分離される。

## Filter誤差と条件付きray

理想選択成分を $v=P_{u,b}Z_u$、実装後を $\widetilde v$ とし、

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|.
```

accept plateauでは $\|v\|\geq\sqrt\tau\|Z_u\|$ である。$\eta_F<\sqrt\tau$ なら三角不等式と規格化写像のLipschitz評価から

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{2\eta_F}{\sqrt\tau-\eta_F}.
```

この $\tau^{-1/2}$ は安全枝を条件付けた解析誤差であり、controllerが $p_{u,b}$ を読み出す費用ではない。

## Radial-only repump

filter後のselected信号だけにR181Aの $\kappa=0$ portを開く。

```math
\dot Z=g(J_*-Z^\dagger Z)Z.
```

方向 $Z/\|Z\|$ は一定で、作用 $r=Z^\dagger Z$ は

```math
\dot r=2gr(J_*-r)
```

に従う。accept plateauでは $r(0)\geq\tau r_{\rm in}$ である。入力作用を固定compact区間 $r_{\rm in}\in[J_-,J_+]$ に保てば、目標相対動径誤差 $\eta_R$ に必要な時間は

```math
T_R
=
O\!\left(
\frac1{gJ_*}
\log\frac{J_+}{\tau J_-\eta_R}
\right).
```

$T_R$ は $\tau$ と安全集合から試行前に固定できる。未知の $p_{u,b}^{-1/2}$ を実装する状態依存squeezeではない。これは採用開放法則であり、厳密なsymplectic resetまたは無履歴逆掃除とは呼ばない。環境へ移った動径情報はspent側に残す。

## Telescopingと完全結果誤差

理想node kernelを $K_k$、実装kernelを $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

```math
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(h_{k-1},\cdot),
K_k(h_{k-1},\cdot)
\right)
\leq\bar\varepsilon_k
```

と仮定する。$\bar\varepsilon_k$ はR170選択、lock、controlled filter、radial repump、routeを各1回だけ数える。Markov kernelの縮約性とtelescopingから、node実装誤差は $\sum_k\bar\varepsilon_k$ 以下である。

正則化は各nodeで高々 $\delta/(1+\delta)$、raw cutoffとguardは全体で高々 $2m(\tau+\gamma)$ の質量を無反応へ送る。入力分布誤差を $\varepsilon_{\rm in}$ とすると

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+\frac{m\delta}{1+\delta}
+2m(\tau+\gamma)
+\sum_{k=1}^m\bar\varepsilon_k.
```

ここで $P_{\rm out}$ は通常の葉と無反応を同じ結果空間に持つ。成功葉だけを再規格化しない。

<!-- theorem-start:proof -->
**証明（R181D）**

P.2がR170 nodeの正則化枝確率を与える。P.3が除去質量、P.4が枝別の1対1 filter、P.5がselected ray誤差、P.6が固定時間repump、P.7のkernel telescopingが深さ $m$ の完全結果誤差を与える。理想kernelの積は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2}{\|Z_0\|^2}
```

と望遠鏡型に縮約する。以上を足して本文の評価を得る。
<!-- theorem-end:proof -->

## 資源と反証条件

$m=n$、$\delta,\tau,\gamma,\bar\varepsilon_k=O(\epsilon/n)$ と選ぶ。R170の保守的混合時間、collision精度、radial時間を合わせると、逐次読出し時間は

```math
O\!\left(
\frac{n^2}{\epsilon}\log\frac n\epsilon
\right)
```

で抑えられる。作用殻stiffnessは $O(n^2/\epsilon^2)$、collision fluxは $O(\sqrt{n/\epsilon})$、barrier rangeは $O(\log(n/\epsilon))$ で足りる。指数的なsignal、work、history、cold、spent容量と総熱はQ2-4の許容受動資源へ計上する。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部controllerへ入力する。
2. selector lock前にfilterを開き、枝像が重なる。
3. cutoffに状態依存除算または指数精度を要する。
4. 非選択成分、collision履歴、radial環境を消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 深さ $n$ のnode誤差を多項式予算へ同時に収められない。

旧fixed-volume apertureおよびdyadic threshold tapeはこの証明に使わない。

# M54の一様blank-bank・collision-cell・spent供給

> **位置づけ：** R179の反復partial SWAP、aggregate cold誤差、root入力、R162 collision cell、selector/filter work、spent履歴の供給則と資源境界を証明する。


## 目的と供給対象

M54の一般 $n$ 特殊化は、$2^n$ signal mode、gate work、R181Dのraw/regularized容量pointer、selector、filter work、radial-port環境、R162 collision cell、外部recordを使う。これらを回路出力に応じて外部生成せず、試行開始前に用意したbankからclock順に供給する。

有限runでは必要bank全体を初期状態に含める。無期限runでは同じ局所規則を持つcold inflowとspent outflowを仮定する。有限閉Hamiltonian系が低作用blankを無制限に増やすとは主張しない。

## 一様bank index

bank modeのindexは

```math
(\mathrm{kind},k,r,j)
```

とする。$\mathrm{kind}$ はsignal、pointer、selector、filter、collision、radial、recordの有限種類、$k$ は回路または読出し段、$r$ はblanking round、$j$ はsector indexである。隣接indexへ同じ形のcouplerを置く有限生成規則を使い、外部programは個々の $j$ を列挙しない。

## 反復partial SWAP

active bankを $W_r$、incoming cold layerを $E_r$ とする。対応pairへ、一様有限規則から作る同一の静的二次Hamiltonianによる同じ2-mode rotationを一括作用させると

```math
W_{r+1}=C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1.
```

各pairの全変換は実正準かつ可逆で、cold側出力をspentへ保持する。active成分だけを捨てない。$\|E_r\|\leq\eta_{\rm cold}$ なら

```math
\|W_R\|
\leq
\rho^R\|W_0\|
+\eta_{\rm cold}\sum_{j=0}^{R-1}\rho^j
\leq
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho}.
```

## Aggregate cold条件

Q2-4で必要なのはmodeごとの温度上界ではなく、bank全体のaggregate norm上界である。独立な各modeが定数noise floorを持てば、$2^n$ modeのaggregate誤差は一般に増大する。この場合R179の多項式精度条件を満たさない。

許される供給は、exact invariant blank、またはbank全体で $\eta_{\rm cold}=O(\epsilon/\operatorname{poly}(n,d))$ を保証する一様contractである。cold sourceの受動容量、装置体積、総作用移送、総熱は指数的でもよいが、外部controllerがmodeごとに較正してはならない。

## Root入力

一般 $n$ 入力はR181Bの反復tensor-liftで作らない。定数次元source packet $s$ を一様tree couplerへ入れ、$0^n$ root modeとblank bankの間でpartial SWAPする。理想的には

```math
Z_{0^n}=s,
\qquad
Z_x=0\quad(x\neq0^n).
```

他の計算基底入力は回路先頭のR181C $X$ gateで作る。未知振幅表のloadはR179のinterfaceに含めない。

## Collision cellとselector供給

R181Dの各nodeはR161率を有限時間近似するR162 collision cellを使う。cellの初期lawは回路出力、raw容量、将来のselector値と独立に取り、branchに依存しない同じ有限局所分布から供給する。容量依存性はR170の局所相互作用にだけ入る。

selectorとfilter workはblank幅以内へpartial SWAPで準備する。使用後は、selector結果、filterに退避した非選択信号、collision履歴、radial-port履歴をspentへ送る。結果を保持したまま全てを同じblank点へ戻さない。

## R179の証明

<!-- theorem-start:proof -->
**証明（R179）**

Q.3の幾何級数評価により、$R_{\rm in}\leq\exp p_1(n,d)$ なら

```math
R
=
O\!\left(
n+\log d+\log(1/\varepsilon_{\rm blank})
\right)
```

回の一様partial SWAPでactive bankを所望のblank幅へ入れられる。Q.2のindex規則により外部命令はbank次元でなくround数に比例する。Q.5がroot入力、Q.6がcollision、selector、filter、spent供給を与える。各供給kernelの全変動距離またはsafe-set失敗率を足せば

```math
\varepsilon_{179}
\leq
C_{\rm root}
(\varepsilon_{\rm blank}+\varepsilon_{\rm src}+\varepsilon_{\rm swap})
+\varepsilon_{\rm coll}
+\varepsilon_{\rm selector}
+\varepsilon_{\rm clock}.
```

供給法則は回路出力確率を含まず、deterministicな下流写像は全変動距離を増やさない。以上で本文のR179を得る。
<!-- theorem-end:proof -->

## 資源境界と非主張

外部program長、blanking round、clock精度、collision精度は $n,d,1/\epsilon$ の多項式である。signal、work、history、cold、spentの受動自由度と状態容量、総作用移送、総熱は $2^n\operatorname{poly}(n,d,1/\epsilon)$ まで許す。これは通常の効率的古典simulationではない。

R179は次を主張しない。

1. cold bathを有限閉Hamiltonian系から無制限に生成すること。
2. 有限bankを無期限運転し、使用済みcellを履歴なしにblankへ戻すこと。
3. 指数的な受動容量、装置体積、総熱を多項式へ削減すること。
4. 結果確率、振幅表、mode別較正値を外部から供給すること。
5. 旧fair-bit、dyadic threshold、aperture tapeをR181Dに必要とすること。

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
- [34] A. Heslot, ``Quantum Mechanics as a Classical Theory,'' Physical Review D 31, 1341--1348 (1985). <https://doi.org/10.1103/PhysRevD.31.1341>
- [35] J. S. Briggs and A. Eisfeld, ``Coherent Quantum States from Classical Oscillator Amplitudes,'' Physical Review A 85, 052111 (2012). <https://doi.org/10.1103/PhysRevA.85.052111>
- [36] J. S. Briggs and A. Eisfeld, ``Quantum Dynamics Simulation with Classical Oscillators,'' Physical Review A 88, 062104 (2013). <https://doi.org/10.1103/PhysRevA.88.062104>
- [37] T. E. Skinner, ``Exact Mapping of the Quantum States in Arbitrary N-Level Systems to the Positions of Classical Coupled Oscillators,'' Physical Review A 88, 012110 (2013). <https://doi.org/10.1103/PhysRevA.88.012110>
- [38] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, ``Experimental Realization of Any Discrete Unitary Operator,'' Physical Review Letters 73, 58--61 (1994). <https://doi.org/10.1103/PhysRevLett.73.58>
- [39] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, ``Optimal Design for Universal Multiport Interferometers,'' Optica 3, 1460--1465 (2016). <https://doi.org/10.1364/OPTICA.3.001460>
- [40] B. Misra and E. C. G. Sudarshan, ``The Zeno's Paradox in Quantum Theory,'' Journal of Mathematical Physics 18, 756--763 (1977). <https://doi.org/10.1063/1.523304>
- [41] W. M. Itano, D. J. Heinzen, J. J. Bollinger, and D. J. Wineland, ``Quantum Zeno Effect,'' Physical Review A 41, 2295--2300 (1990). <https://doi.org/10.1103/PhysRevA.41.2295>
- [42] J. Ruseckas and B. Kaulakys, ``Real Measurements and the Quantum Zeno Effect,'' Physical Review A 63, 062103 (2001). <https://doi.org/10.1103/PhysRevA.63.062103>
- [43] M. A. Nielsen, ``A Simple Formula for the Average Gate Fidelity of a Quantum Dynamical Operation,'' Physics Letters A 303, 249--252 (2002). <https://doi.org/10.1016/S0375-9601(02)01272-0>
- [44] D. Dürr, S. Goldstein, R. Tumulka, and N. Zanghì, ``Quantum Hamiltonians and Stochastic Jumps,'' Communications in Mathematical Physics 254, 129--166 (2005). <https://doi.org/10.1007/s00220-004-1242-0>
- [45] H.-O. Georgii and R. Tumulka, ``Global Existence of Bell's Time-Inhomogeneous Jump Process for Lattice Quantum Field Theory,'' Markov Processes and Related Fields 11, 1--18 (2005). <https://arxiv.org/abs/math/0312294>
- [46] C. Jarzynski, ``Nonequilibrium Equality for Free Energy Differences,'' Physical Review Letters 78, 2690--2693 (1997). <https://doi.org/10.1103/PhysRevLett.78.2690>
- [47] G. E. Crooks, ``Entropy Production Fluctuation Theorem and the Nonequilibrium Work Relation for Free Energy Differences,'' Physical Review E 60, 2721--2726 (1999). <https://doi.org/10.1103/PhysRevE.60.2721>
- [48] U. Seifert, ``Entropy Production along a Stochastic Trajectory and an Integral Fluctuation Theorem,'' Physical Review Letters 95, 040602 (2005). <https://doi.org/10.1103/PhysRevLett.95.040602>
- [49] J. Ehrich, M. Esposito, F. Barra, and J. M. R. Parrondo, ``Micro-Reversibility and Thermalization with Collisional Baths,'' Physica A: Statistical Mechanics and its Applications 552, 122108 (2020). <https://doi.org/10.1016/j.physa.2019.122108>
- [50] M. Esposito, ``Stochastic Thermodynamics under Coarse Graining,'' Physical Review E 85, 041125 (2012). <https://doi.org/10.1103/PhysRevE.85.041125>
- [51] C. Jarzynski, ``Nonequilibrium Work Theorem for a System Strongly Coupled to a Thermal Environment,'' Journal of Statistical Mechanics: Theory and Experiment 2004, P09005 (2004). <https://doi.org/10.1088/1742-5468/2004/09/P09005>
