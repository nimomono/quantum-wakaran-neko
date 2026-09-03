# 概要


本論文は、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、結合ゲート、空間伝播、Bell型統計を構成できる範囲を調べる。有限閉鎖Hamiltonianモデルと開放古典モデルを区別し、採用方程式後の厳密結果と、その方程式自体のミクロ導出を分ける。

状態準備とBorn型読出しを分ける。M51は実正準担体、物理template、pump、transverse sink、clockを持つ基礎開放模型であり、R171は設定前seed測度を有限時間押し出してrank-one第2モーメントを準備する。各試行の実体は実担体と装置自由度、複素信号は実担体の派生表示である。M51のrayは試行集団の統計因子だが、M52の $Z_S$ は1試行の実正準状態から得る派生信号である。

準備後の各試行の有限正準信号 $v$ を共通instrument仕様M50へ渡し、R164の作用殻状態数から排他的枝重み $\pi_i^\delta(v)$ を得る。R161/R162で粒子位置を有限時間再平衡化し、R170で枝を固定して局所記録する。二乗形の状態依存性はM51の第2モーメントに現れ、排他的結果はM50/R170が作る。R112は有限正準制御、安全比較、SWAP、記録、逆計算を担うが、独立のBorn型枝生成には使わない。

Q1はM47のW型最低2モードと信号bathを使う。R145はM51/R171の2モード特殊化として入力rayを準備する。共通R135がBloch球型統計状態空間、R140が任意の $SU(2)$ 操作、Rabi型占有振動、傾斜保持を与える。R143は共通R170へW型分析器、有限コントラスト、結果別テンプレート交換を加えた特殊化である。可逆操作は達成し、Born分布、同軸反復分布、異軸逐次分布も有限誤差で導出している。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。完全周期と周期総収支は固定目標ではなく、実装・熱力学的強化課題として残す。

Q2-1はM52の受動的な4mode信号、anti-register、work、clock履歴を同じ永続状態bathへ保持する。R176Aは一般積入力の可逆tensor-lift、R176Bは同一register上のCNOT、局所操作、逆演算、参照系安定な有限誤差合成、R176Cは末端Born型instrument接続を与える。R176Cの容量pointer--作用殻境界、有限fiber混合、記録までの一体化を条件としてQ2-1は条件付き達成である。Q2-2は独立の目標として、R147のpaired-Hopf準備後、R153で設定前routingと2翼strong matchingを作り、R155で2つの局所R170、条件付き積因子化、余弦共同分布、非信号性、CHSH不等式の破れ、Bell前提監査、fresh-cell帰還をまとめる。Bell型統計は固定singlet、固定有限設定族、準備先行、非空間分離、採用開放法則の範囲で条件付き達成である。

Q2-3はR176Aをgate列の前に2回適用して8mode信号を作り、R176BのA--B、B--C二次生成子を同じ状態bathへ順に作用させる。R177はGHZ--$T$--逆演算のcoherent分布と完全dephasing分布が全変動距離 $1/(2\sqrt2)$ で分かれることを示す。R176Cと同じ末端一体化条件の下で条件付き達成である。

Q2-4には一様直接モード・逐次2枝標本化模型M53を置く。R178A--R178Cは局所gateのsector一括作用、可逆filter、希少枝切断付き逐次Born標本化を与え、R178D--R178Fは履歴逆掃除の限界、fixed-volume fresh tape、滑らかな二channel aperture散乱を与える。R179は一定精度partial SWAPの反復、回路非依存のfair-bit源、dyadic threshold tapeによりblank-bankとfresh cellを供給する。指数的な受動信号・work・history・cold・spent容量と総熱を許し、外部program、制御channel、精度、反復回数、総時間だけを多項式に抑える現行規則の下で、Q2-4を条件付き達成とする。条件はM53の静的sector配線、滑らかなaperture、cold/spent開放境界を単一の一様装置族へ統合することである。

Q3はM51で初期rank-one集団を準備し得る契約を上流に置き、M37の局所振動子網からR86の有限時間Schrödinger型担体を導く。その上に1個の局在粒子位置、局所辺bath、clock、履歴を持つM42を置く。R172はM37有効辺流に沿う位置分布の等変性、R173は節一様正則化と有限衝突Hamiltonian近似、R174はM51準備から終位置記録までの誤差受渡しを与える。初期位置は準備済み信号から一度だけ作り、終時刻に別の位置を再標本化しない。空間Schrödinger型力学と束縛状態は達成、トンネル効果と最小2経路干渉は単一装置統合を条件に達成である。位相量子化は未達だが、巻数、節、位相すべり、細分化安定性を統合する研究課題として再開する。

Q1、Q2、Q3は同じハードウェアではなく、Q2内部でもM52、M48、M53は別の構成である。各固定目標は明記した根拠モデルと根拠結果から独立に判定する。Q2共通ハードウェア族と、信号準備、作用容量結合、作用殻fiber、衝突bath、時計、記録、resetを1つの有限局所Hamiltonian周期へ統合するM0は、判定外の実装努力目標として未完成である。連続空間・多粒子への一様拡張も得ていない。

# 第I部　問題設定と共通言語

# 問題設定、現行模型、達成範囲

> **位置づけ：** 共通M51開放準備からQ1のM47、Q2-1・Q2-3のM52、Q2-2のM48、Q2-4のM53、Q3のM37--M42へ進む現行因果鎖と未統合境界を示す。


## 研究上の問い

本論文の目的は、古典的な粒子、振動子、熱浴、制御器、記録器から、量子力学に特徴的な構造をどこまで明示的に再現できるかを調べることである。量子力学は結果の比較基準に使うが、古典モデルの運動方程式や初期確率へ答えを直接入力しない。

有限次元Schrödinger方程式を実正準方程式へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、測定後状態、記録、resetは得られない。本稿は次を別々に要求する。

1. 実担体と開放portから階数1の試行集団統計を有限時間で準備する。
2. 可逆な信号操作を古典正準流として実装する。
3. 各試行の信号作用から排他的枝または初期粒子位置の状態数を作る。
4. Q1・Q2では粒子位置を枝分布へ再平衡化し、Q3では同じ局在粒子をM37担体に沿って輸送する。
5. 無反応を含む完全結果集合を局所記録する。
6. 系列固有の状態更新、ゲート、Bell監査、空間現象を共通読出しへ接続する。

## 現行因果鎖

状態準備とBorn型読出しは

```math
\Gamma_0
\xrightarrow{\mathrm{M51/R171}}
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

の順に分ける。M51は採用driftを持つ基礎開放模型、M50は共通instrument仕様であり、どちらも単独では完成した測定周期ではない。R112は有限基底制御、時計、比較、SWAP、記録、逆計算の共通定理であり、作用区間の一様角から別のBorn型結果を作らない。

Q3だけは下流を

```math
\Gamma_0
\xrightarrow{\mathrm{M51/R171}}
Z_{t_0}(\omega)
\xrightarrow{\mathrm{R164\ once}}
X_{t_0}
\xrightarrow{\mathrm{M37+M42/R172--R174}}
X_T
\xrightarrow{\mathrm{R112\ record}}
D_{X_T}
```

とする。終時刻に別のM50位置を作らない。

各試行の実体は実正準担体、粒子位置、bath、template、clock、記録・履歴である。複素信号は実正準担体の派生表示である。M51の $c,C_Z$ は試行集団の統計量だが、M52の $Z_S$ は1試行の実正準状態から得る。M50は同じ試行の物理信号から排他的結果を作る。これらを同一視しない。

| 系列 | 信号準備と操作 | 単一試行の下流入力 | 系列固有の下流結果 |
|---|---|---|---|
| Q1 | M51/R171、M47、R135、R140、R143--R145 | 単一試行のW型信号bath座標 | R143のW型分析器と結果別状態更新 |
| Q2-1 | M52、R112、R176A--R176C | 1試行内の永続4mode信号とanti/work | 可逆tensor-lift、CNOT、逆演算、条件付き末端instrument |
| Q2-2 | M48、R147、R153、R155 | 切断後の各翼の局所信号 | 2つのR170の条件付き局所合成とBell監査、帰還 |
| Q2-3 | M52、R176A--R176C、R177 | 3部分系の永続8mode信号とanti/work | A--B、B--C、GHZ--$T$--逆演算、条件付き末端instrument |
| Q2-4 | M53、R112、R161、R162、R164、R178A--R178F、R179 | $L=2^n$ の受動直接モード、逐次2枝filter、fresh tape | 一般回路列と完全結果空間上の逐次出力。指数的な受動bankと総熱を許す |
| Q3 | M51/R171、M37、R86、R135 | 準備終了面のM37標本と初期M42位置 | R172--R174の局在粒子輸送、R123--R125への接続 |

集団の第2モーメント、交差モーメント、共同頻度を単一試行controllerへ書き戻さない。Q1・Q2は各試行の有限信号だけをM50へ渡す。Q3は各試行のM37実振動子、M42現在位置、局所bath cellだけを進める。

## 現行模型

| 模型 | 役割 | 状態 |
|---|---|---|
| M0 | Q1--Q3を同一ハードウェアと反復周期へ統合する目標 | 未完成 |
| M51 | 有限実正準担体からrank-one統計rayを作る共通開放準備 | 現行基礎開放模型 |
| M37 | 局所振動子網からの空間包絡 | 現行基礎Hamiltonian模型 |
| M42 | M37担体上の局在1粒子トークン輸送 | 現行Q3粒子模型 |
| M47 | W型2モード信号bath・粒子位置の測定protocol | 現行Q1複合protocol |
| M48 | 設定依存paired-Hopf Bell周期 | 現行Q2-2開放複合protocol |
| M52 | Q1×Q1可逆tensor-lift永続状態bath模型 | 現行Q2-1・Q2-3模型。R176A/Bは厳密、R176Cは条件付き |
| M53 | 一様直接モード・逐次2枝標本化模型 | 現行Q2-4模型。R178A--R178FとR179を単一装置族へ統合することを条件とする |
| M50 | 有限信号作用、作用殻状態数、粒子位置再平衡化、R170 | Q1・Q2の共通instrument仕様。Q3では初期M42位置の1回選択だけに使用 |

置換済み模型と独立研究線は本文の模型地図へ並べない。最小索引は `notes/superseded_result_index.md`、詳細は各研究メモとGit履歴に置く。

## 達成判定

「達成」は、固定した範囲で基準を厳密に満たすか、任意の $\epsilon>0$ に対して誤差を $\epsilon$ 未満にする有限構成を選べることを指す。形式極限、構成のない収束仮定、無反応試行の事後除外は含めない。

| 目標 | 現在地 | 根拠モデル | 根拠結果 | 主な残件 |
|---|---|---|---|---|
| Q1-1 | 達成 | M47 | R135、R140 | なし |
| Q1-2 | 部分達成 | M47、M50、M51 | R140、R143--R145、R161、R162、R164、R168、R170、R171 | Born分布、同軸反復分布、異軸逐次分布は導出済み。零傾斜Rabi対照、反復測定、全履歴、tilt対照、有限誤差を含むZeno抑制余裕が残る |
| Q2-1 | 条件付き達成 | M52、M50末端読出し | R112、R164、R170、R176A--R176C | 容量pointerから作用殻、混合、固定、記録までの末端一体化 |
| Q2-2 | 条件付き達成 | M48、M50 | R147、R153、R155、R164、R168、R170 | 自由設定、空間分離、一般状態 |
| Q2-3 | 条件付き達成 | M52永続状態bathの三部分系特殊化 | R112、R176A--R176C、R177 | Q2-1と同じ末端一体化条件。一般サイズの資源効率はQ2-4に残る |
| Q2-4 | 条件付き達成 | M53 | R112、R161、R162、R164、R178A--R178F、R179 | 静的sector配線、滑らかなaperture、cold/spent開放境界を一つの一様装置族へ統合する。受動bank容量と総熱は指数的でもよい |
| Q3-1 | 達成 | M37 | R86 | 一般複素hoppingと時間依存一様極限は範囲外 |
| Q3-2 | 未達 | 完結モデルなし | なし | 節、巻数、位相すべり、細分化安定性、非整数モノドロミー排除の統合 |
| Q3-3 | 達成 | M37、R123有限環境 | R86、R123 | 一般連続空間・多粒子は範囲外 |
| Q3-4 | 条件付き達成 | M51、M37、M42、M50 | R86、R124、R171--R174 | M51準備、M37担体、初期作用殻、M42輸送、記録までの単一装置統合 |
| Q3-5 | 条件付き達成 | M51、M37、M42、M50 | R86、R125、R171--R174 | 同上。幾何学的2開口と連続スクリーンは未構成 |

固定目標の文言と達成判定の詳細は `PROJECT_STATUS.md` を正本とする。Q1-2はBorn分布、同軸反復分布、異軸逐次分布を導出済みとし、Zeno部分が未達であるため部分達成とする。Q2-1からQ2-4は、明記した根拠モデルと根拠結果から互いに独立に判定する。共通ハードウェア族への統合は固定目標とは別の実装努力目標である。Q2-3は3量子ビット型二段ゲート合成、Q2-4は指数的な受動自由度を許す多項式外部制御サンプリングである。置換または削除した旧固定目標は退役索引に保存する。

## 根拠モデルの独立性と模型間受渡し

Q2固定目標は、Q2-1のM52と末端M50、Q2-2のM48/M50、Q2-3のM52三部分系特殊化、Q2-4のM53をそれぞれの根拠として独立に判定する。これらが同じ物理装置でないことは個別判定を変更しない。規模ごとの一様な共通ハードウェア族へ統合することは、別の実装努力目標である。

M52は同じ試行の $Z_S$、anti-register、work/historyをそのまま次のgate窓へ保持し、mode選択、共同momentへの置換、fresh bathへの再準備を許さない。内部の有限modeは受動bath自由度であり、個別の外部初期化、較正、同期、address、読出し、resetを要求しない。Q2-3の完全な合成契約は付録Jを正本とする。M48は内部seedから独立に開始し、M52からの入力受渡しを現行結果として主張しない。

## 非主張

本論文は次を主張しない。

1. Q1、Q2、Q3が同一の達成済み物理装置であること。
2. M51の採用driftを有限bath、仕事源、排熱先から導出済みであること。
3. R164の枝状態数だけで作用殻準備と熱化をミクロ導出したこと。
4. R170の全構成部品を1つの具体的有限局所Hamiltonianへ統合済みであること。
5. 長期頻度または有限熱化から独立同分布型有限標本揺らぎが従うこと。
6. M48が標準的な空間分離・自由設定Bell実験を再現すること。
7. Q3の有限グラフトークンから連続空間の連続粒子軌道が一様に得られること。
8. Q2の一様な共通ハードウェア努力目標、R176Cの末端一体化、M53の全構成部品を単一の一様装置族へ統合済みであること。
9. 指数的な受動自由度を許すことが、指数時間、指数個の個別制御、指数的に細かい精度を許すこと。
10. 連続空間、多粒子、一般有限POVMの一様構成。

## 論文の読み方

第2章は有限モード担体、M51/R171の共通開放準備、M50/R170の共通読出し、M53の一様直接モード・逐次2枝標本化、第3章はM47によるQ1、第4章はM52のQ1×Q1共同bath候補、第5章は独立のM48 Bell周期、第6章と第7章はM37--M42によるQ3を扱う。第8章は現行主線の誤差と資源に加え、固定目標ごとの根拠モデル、Q2共通ハードウェア努力目標、Q2-3、Q2-4の境界、反証条件、未完成目標をまとめ、第9章で結論を述べる。

付録AはR112の制御・比較・記録証明、BはM47測定特殊化、CはM52の経路代数とR176の証明義務、DはM48、EはM37包絡、Fは共通R135/R168とR170の固定時刻診断、GはQ3現象の証明、HはR171のM47特殊化、IはM48 paired-Hopf準備、JはQ2永続共同bathの二段合成とM48条件付き因子化、KはR161、R162、粗視化経路熱力学、R170の証明、LはR164の証明、MはM51/R171の共通開放準備、NはM37--M42の局在トークン輸送、O--QはM53の一様gate、逐次Born標本化、history処理、滑らかなaperture、blank-bank供給を扱う。

# 有限モード担体と共通正準モジュール

> **位置づけ：** Q1の2モード、M52の有限永続mode、Q2末端信号、Q3の有限空間セル担体に共通するR112、R171、R135、R164と、固定時刻枝instrumentのR161、R162、R168、R170を整理する。


## 共通主線と統一M0の違い

共通の階数1状態準備と固定時刻Born型instrumentは次の因果鎖を使う。

```math
\Gamma_0
\xrightarrow{\mathrm{M51/R171}}
C_Z\simeq cc^\dagger,
\qquad
Z(\omega)
\longrightarrow
\Omega_i^\delta(v)
\longrightarrow
\pi_i^\delta(v)
\longrightarrow
X=i
\longrightarrow
D_i.
```

M51は実正準担体と開放portのseed測度を有限時間押し出し、単一試行の派生信号 $Z(\omega)$ の集団第2モーメントを階数1射影へ近づける。統計因子 $c$ または $C_Z$ を単一試行controllerへ書き戻さず、各試行に実在する正準担体から得た $v=Z(\omega)$ だけをM50の作用容量へ渡す。Q1とQ2、および任意の固定時刻instrumentでは、R164で排他的枝の状態数を数え、R161/R162で粒子位置を有限時間再平衡化し、R170で枝を固定して局所記録する。

Q3の空間位置では、M51準備後の単一試行信号にR164を一度だけ適用してM42の初期粒子位置を作る。その後はM37担体の局所辺流とM42 bathが同じ粒子を輸送し、終時刻にはR112で既存位置を記録する。終時刻R170で別の位置を再標本化しない。

二乗形はM51が作る第2モーメントの対角とR164が数える単一試行作用の両方に現れるが、同じ因果段階ではない。M51はrayを準備し、R164はその方向を1個の排他的位置または枝へ物理化する。M51単独をBorn型標本器と呼ばず、初期M42選択と終時刻M50選択を2つの確率源として併用しない。

| 系列 | 有限担体の大きさ | 単一試行の実体 | 共通モジュール | 系列固有装置 |
|---|---:|---|---|---|
| Q1 | $L=2$ | 2モード実担体、粒子位置、bath、記録 | M51、R112、M50 | M47 W型分析器 |
| Q2 | 目的ごとに有限 | M52永続modeまたはM48局所信号、末端読出し、記録 | R112、M50 | M52、M48 |
| Q3 | 空間セル数 $L$ | M37実振動子、M42局在粒子、局所辺bath、記録 | M51、R112、R135、初期R164 | M37--M42二層模型 |

同じ $L$ 次元正準代数を使うことは、担体のミクロHamiltonian、bath、粒子輸送則、時計、記録器が同じことを意味しない。

| 系列 | M51の役割 | M50へ渡す単一試行信号 | 排他的出力 | 系列固有部分 |
|---|---|---|---|---|
| Q1 | M51の2モード特殊化でW型rayを準備 | M47の信号bath座標 $Z(\omega)$ | 左右井戸 | W型制御、有限コントラスト、結果別テンプレート |
| Q2-1 | R176Aが積入力を可逆lift | M52の実際の末端信号 $Z_{\rm out}(\omega)$ | 4計算基底枝 | 永続4mode、anti/work、CNOT、逆演算、容量latch |
| Q2-2 | M51は局所seedに使用可能。singlet交差統計はM48が別に準備 | M48切断後の各翼の局所信号 | 各翼2枝 | paired-Hopf準備、2翼局所合成、Bell監査 |
| Q3 | M51で初期rank-one集団を準備し、M37へ受渡し可能 | 準備終了面のM37標本包絡 $Z_{t_0}(\omega)$ | 初期M42位置。終時刻は同じ粒子を記録 | R172--R174の局所辺流、節正則化、有限衝突bath |

この表の共有は、M52とM48が同一ハードウェアであることを意味しない。Q2固定目標はそれぞれの根拠モデルと根拠結果から独立に判定し、同一装置への統合を要求しない。M52の $Z_S$ は1試行の派生信号であり、M51の試行集団rayまたはM48の集団交差momentと同一視しない。M52の内部mode、anti-register、work、clock履歴は受動bath自由度として許すが、外部から個別に初期化、較正、同期、address、読出し、resetしない。現行の有限担体と共通モジュールは将来の共通ハードウェア候補部品だが、統合結果ではない。M51は採用したdriftを持つ基礎開放モデル、M50は共通instrument仕様、M42はQ3だけの局在粒子輸送模型であり、いずれも単独では全周期装置ではない。M51のpump、sink、template、切断器を有限閉鎖Hamiltonianへ持ち上げたとは主張しない。全系列の信号準備、容量結合、作用殻、衝突bath、時計、記録、resetを1つの有限局所Hamiltonian周期へまとめるM0も、判定外の実装努力目標として未完成である。

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

## M51有限実正準担体の共通開放ray準備

各試行の物理状態として $m$ 個の実正準対 $(Q,P)\in\mathbb R^{2m}$ を置き、その派生座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とする。$z$ は実担体の表示であって追加の実体ではない。目標templateも実装置の正準対 $(Q^w,P^w)$ で保持し、そこから得る非零派生座標 $w$、規格化方向 $c=w/\|w\|$、射影 $\Pi_c=cc^\dagger$ を使う。$c$ と $\Pi_c$ はtemplate設定および準備後集団統計の記述であり、各試行へ別に加える物理場ではない。

Hermitian生成子 $G(t)$ とそのunitary $U(t)$ に対し $c(t)=U(t)c(0)$、$\Pi_c(t)=c(t)c(t)^\dagger$ とする。M51の雑音零の採用開放方程式を

```math
\dot z
=
-\frac{i}{\mathcal J_0}G(t)z
+\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-\kappa(I-\Pi_c(t))z
\right]
```

と定める。$g,\kappa>0$、$\lambda_{\rm prep}\geq0$ である。第1項は実正準Hamiltonian伝播、動径項はpumpと飽和、射影直交項はtransverse sink、$\lambda_{\rm prep}$ は物理clockが開閉するportである。最小M51は決定論的であり、Langevin雑音を含まない。雑音付き拡張は別のモデルであり、R171の結論へ暗黙に含めない。

準備有効時間を

```math
\tau(t)=\int_{t_0}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とする。相互作用表示で $\widetilde z=ac+p$、$c^\dagger p=0$ と分解すると

```math
\frac{da}{d\tau}=g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p,
```

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\tau}
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
**定理（R171：M51共通開放ray準備の有限時間率と切断後輸送）**

$G_*$ 上で $q_*=(R_*^2-a_*^2)/a_*^2$ とする。M51の採用開放方程式では、各安全試行のray距離は

```math
D_{\rm pure}
\left(
\frac{zz^\dagger}{z^\dagger z},
\Pi_c(t)
\right)
\leq
\sqrt{q_*}e^{-\kappa\tau(t)}.
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
\sqrt{q_*}e^{-\kappa\tau(t)}.
```

また、$a_0\neq0$ の各試行は $\tau\to\infty$ で位相円へ収束し、動径誤差を含む収束率は有界seed集合上で $\min\{2g,\kappa\}$ により抑えられる。有限時刻 $t_{\rm cut}$ で $\lambda_{\rm prep}=0$ とした後は、各試行の実正準状態が $i\mathcal J_0\dot z=Gz$ に従い、R135の第2モーメント輸送が成り立つ。$G_*^c$ の確率は無反応質量として保持し、成功試行だけを結果分布として再規格化しない。
<!-- theorem-end:theorem -->

証明、複素式と等価な実変数方程式、pump・sink・template・clockの因果台帳は付録Mに置く。R171は採用開放方程式後の厳密結果である。pumpとsinkの環境自由度、仕事、熱、エントロピー生成を有限閉鎖系から導いた結果ではない。

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

R170は有限枝instrumentの共通定理であり、M37を前提にしない。Q1のR143、Q2-2のR155、Q3の固定時刻読出しはこの定理の特殊化または合成である。完全な証明と誤差台帳は付録Kに置く。

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

従って理想分布間の分離が誤差和より大きければ、有限装置でも区別可能性が残る。この系をR124/R125の識別とR155のBell監査へ共通に用いる。

## M53一様直接モード・逐次2枝標本化模型

$n$ 量子ビット、深さ $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。M53では計算基底文字列 $x$ を受動信号モードへ直接対応させる。

```math
|x\rangle
\longleftrightarrow
Z_x,
\qquad
Z=(Z_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

M53はsignal、anti-register、filter work、rejected-history、repump、容量pointer、一様gate bus、cold bath layer、fresh tape、spent tape、出力記録、clockを持つ。内部の受動自由度、静的結合、状態容量、受動並列度は $2^n\operatorname{poly}(n,d)$ まで許す。一方、外部programが指定するのはgate種、1個または2個の対象量子ビット、gate順序、現在読む出力bit、blanking round、tape index、clock窓だけである。$2^n$ モードの列挙、モード別初期化・較正・読出し、指数長の係数表、回路別配線、出力確率の事前計算を許さない。

M53はR176Aの反復tensor-liftを一般 $n$ へ延長しない。R179で全bankをblank化した後、定数次元sourceを $0^n$ root modeへ接続して計算基底入力を作る。別の基底入力は回路先頭の $X$ gateで作る。gate列はR178A、末端bit列はR178B--R178F、準備資源はR179が担う。

## R178A：局所gateの一様sector-broadcast定理

対象量子ビット集合 $S$ の大きさを $k\in\{1,2\}$ とし、$g$ を固定有限gate集合の $2^k$ 次元unitaryとする。spectator labelを $r\in\{0,1\}^{n-k}$ と書き、同じ局所生成子 $h_g$ を全sectorへ置く。

```math
H_{g,S}
=
\bigoplus_r h_g^{(r)},
\qquad
U_{g,S}=g_S\otimes I_{\bar S}.
```

<!-- theorem-start:theorem -->
**定理（R178A：局所gateの一様sector-broadcast定理）**

各sector blockが同じ局所規則から生成され、実装block $\widetilde g_r$ が一様に $\|\widetilde g_r-g\|\leq\eta_g$ を満たし、異なるsector間の漏れの作用素normが $\eta_{\rm leak}$ 以下とする。このとき1個の共有clock窓で全spectator sectorへgateを作用でき、

```math
\|\widetilde U_{g,S}-U_{g,S}\|
\leq
\eta_g+\eta_{\rm leak}
```

である。block数による和は生じない。深さ $d$ のgate列では、全gateのglobal phaseを除いた誤差は各窓の作用素norm誤差の和以下である。固定gate集合なら、対象指定、制御channel、命令数は $n,d$ の多項式、静的sector結合は指数的でも一様有限規則から生成できる。
<!-- theorem-end:theorem -->

3次元Euclid空間への局所埋込み、指数個の静的結合の総製造費、全結合を個別に調整する方法は主張しない。外部制御仕事は空sector数ではなく占有信号の総作用と共有係数の変化で評価し、指数個の独立駆動器を隠さない。

## R178B：直交projector作用latch・可逆filter定理

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

<!-- theorem-start:theorem -->
**定理（R178B：直交projector作用latch・可逆filter定理）**

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
<!-- theorem-end:theorem -->

R178Bは確率的な枝選択を行わない。容量比を排他的結果へ変える工程はR178E/R178Fが担う。

## R178C：希少枝切断付き逐次Born sampler定理

第 $k$ 段の入力を $Z_{k-1}\neq0$ とし、条件付きBorn重みを

```math
p_{k,b}
=
\frac{\|P_{k,b}Z_{k-1}\|^2}{\|Z_{k-1}\|^2}
```

とする。R178E/R178Fが $b$ を選び、R178Bがselected componentを分離する。$p_{k,b}\geq\tau$ の安全枝ではrepumpがselected rayを変えず標準作用へ戻し、radial情報をanti/historyへ移す。$p_{k,b}<\tau$ の枝は失敗結果 $\varnothing$ へ送る。

<!-- theorem-start:theorem -->
**定理（R178C：希少枝切断付き逐次Born sampler定理）**

理想2枝instrumentを $n$ 段合成すると、文字列 $y=(y_1,\ldots,y_n)$ の確率は

```math
\prod_{k=1}^n p_{k,y_k}
=
\frac{
\|P_{n,y_n}\cdots P_{1,y_1}Z_0\|^2
}{
\|Z_0\|^2
}
```

となり、計算基底Born分布に一致する。各段で条件付き確率が $\tau$ 未満の枝を $\varnothing$ へ送る場合、除去される全確率質量は高々 $2n\tau$ である。selected枝の必要repump利得は $\tau^{-1/2}$ 以下、2-mode squeeze強度は $O(\log(1/\tau))$ である。成功試行だけを再規格化せず、無反応と切断枝を完全結果空間に残す。
<!-- theorem-end:theorem -->

最終分布を段ごとの条件付き状態へ逐次比較せず、実際の初期信号が持つBorn分布と理想回路分布を末端で一度だけ比較する。これにより小確率枝ごとの不必要な $1/\tau$ 誤差増幅を避ける。

## R178D：逐次history逆掃除・collective reset定理

$Y\in\{0,1\}^n$ をbit data記録、$F\in\{0,1\}$ を無反応flagとし、完全結果は $(Y,F)$ として保持する。以下の情報容量下界は $Y$ だけに対する弱い下界であり、flagと微視的履歴に必要な追加容量を除外しない。

<!-- theorem-start:theorem -->
**定理（R178D：逐次history逆掃除・collective reset定理）**

gate、latch、filter、repump、clockの完全な微視的履歴を保持する。出力 $Y$ を別の記録へ可逆copyした後なら、出力記録と相関しない内部workを逆順に掃除できる。

一方、$(Y,F)$ を保持したまま装置、bath、履歴の全てを同じ初期点へ戻す1対1写像は存在しない。結果と相関するselector、使用済みpointer、collision履歴、clock履歴はspent tapeへ送る必要がある。spent状態から $Y$ を復号する誤り率を $p_{\rm e}$ とし、Fano補正を $\eta_{\rm F}=h_2(p_{\rm e})+p_{\rm e}\log(|\mathcal Y|-1)$ と置く。natsで測ったspent側の情報容量 $C_{\rm spent}$ は

```math
C_{\rm spent}\geq H(Y)-\eta_{\rm F},
\qquad
H(Y)\leq n\log2
```

を満たす。熱的resetの仕事・熱下界は、bath温度と消去protocolを別に指定した場合だけ従う。
<!-- theorem-end:theorem -->

R170の粗視化Markov pathだけから微視的状態を逆算しない。逆転に使用できるのはR162の完全collision履歴またはR178E/Fの全cell履歴である。同じbath seedまたは同じ使用済みcellを再利用した試行列を独立同分布とは呼ばない。

## R178E：二枝作用殻interface・fresh-tape周期定理

各fresh cellはbranch label $B\in\{0,1\}$ とLiouville座標 $U\in[0,A_{\max}]$ を持つ。容量は $0\leq A_b\leq A_{\max}$ とする。理想入口測度では $B$ は等重み、$U$ は平坦で相互に独立とする。$B=b$ かつ $U<A_b$ のcellだけをacceptし、物理的な最速到達ではなく最小tape indexのacceptを結果とする。

```math
q_b=\frac{A_b}{2A_{\max}},
\qquad
r=1-\frac{A_0+A_1}{2A_{\max}}.
```

<!-- theorem-start:theorem -->
**定理（R178E：二枝作用殻interface・fresh-tape周期定理）**

$N$ 個の独立cellをindex順に固定時間窓で試すと、

```math
P_N(b)
=
\frac{A_b}{A_0+A_1}(1-r^N),
\qquad
P_N(\varnothing)=r^N.
```

理想容量比分布に無反応を加えた完全結果分布との全変動距離は $r^N$ である。各段の容量latch時に

```math
0<S_-\leq A_0+A_1\leq S_+
```

が一様に成立し、$S_-/A_{\max}$ が正の定数以下へ落ちないなら、$n$ bit全体の無反応を目標誤差以下にするcell数は各bitで $N=O(\log(n/\epsilon))$ で足りる。
<!-- theorem-end:theorem -->

R164の作用殻状態数とR178Eの通過体積を同じ枝重みへ二重に掛けない。M53ではR164が与える線形capacityをR178Eのapertureが一度だけ物理化する。拒否cellもspent tapeへ残す。

## R178F：滑らかな二channel aperture散乱の一様canonical実装定理

反応座標 $(X,P_X)$、cell座標 $U$、branch selector $Q_B$、滑らかなplateau $\beta_b(Q_B)$ を置き、

```math
A(Q_B)=\beta_0(Q_B)A_0+\beta_1(Q_B)A_1
```

とする。aperture Hamiltonianを

```math
H_{\rm ap}
=
\frac{P_X^2}{2m}
+V_0(X)
+g\{U-A(Q_B)\}\rho(X)
```

とする。$V_0(0)=E_0$、$V_0''(0)=-m\omega^2$、$\rho(0)=1$ とする。

<!-- theorem-start:theorem -->
**定理（R178F：滑らかな二channel aperture散乱の一様canonical実装定理）**

入口energyが $E_0$ で、selectorがbranch $b$ の安全plateauにあるとする。$U<A_b$ では頂上障壁が入射energyより低く、$U>A_b$ では高いので、それぞれ通過と反射になる。また

```math
gA_{\max}\|\rho'\|_\infty
<
\inf_{{\rm supp}\,\rho'}|V_0'|
```

なら相互作用窓に余分な極値を作らない。energy幅 $\Delta_E$、較正幅 $\Delta_{\rm cal}$、判定時間 $T$ に対する未解決境界幅は

```math
\ell_{\rm eff}(T)
=
\frac{
\Delta_E+\Delta_{\rm cal}
+C_0e^{-\omega(T-t_0)}
}{g}
```

で抑えられる。$A_b$ と $U$ は理想相互作用で保存されるが、その共役momentumはbackreactionを保持するため、capacity pointerとcellを逆散乱しない限りblankとして再利用しない。
<!-- theorem-end:theorem -->

cellを物理的到着順で競争させず、indexごとに長さ $T$ の窓を順番に開く。従って散乱時間が $|U-A_b|$ に依存しても容量比へarrival biasを入れない。

## R179：一様blank-bank・fresh-cell供給定理

全補助bankを $W\in\mathbb C^{D_{n,d}}$、$D_{n,d}\leq2^np(n,d)$ とまとめる。各blanking roundでbank modeとincoming cold modeの対応pairへ同じ形式のpartial SWAPを並列に作用させる。couplerは一様有限規則から作る同一の静的二次Hamiltonianとし、受動clockがroundを進める。指数個のcouplerを外部から個別に開閉せず、外部quench workをbank次元へ比例させない。

```math
W_{r+1}=C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1,
\qquad
\|E_r\|\leq\eta_{\rm cold}.
```

pairごとの全変換は2-mode回転で実正準かつ可逆であり、cold側出力はspent側へ保持する。active成分だけを捨てて非可逆化しない。

fresh aperture cellはlabel bit $B$ と $k$ 個のdigit bit $C_1,\ldots,C_k$ を持ち、

```math
J=\sum_{\ell=1}^k2^{k-\ell}C_\ell,
\qquad
U_k=A_{\max}\frac{J+1/2}{2^k}
```

をR178Fへ直接結合する。

<!-- theorem-start:theorem -->
**定理（R179：一様blank-bank・fresh-cell供給定理）**

次の条件を仮定する。

1. bank初期normは $R_{\rm in}\leq\exp p_1(n,d)$ である。
2. cold layerのaggregate誤差は $\eta_{\rm cold}$ 以下である。
3. partial SWAPの残留係数は一様に $\rho<1$ である。
4. fresh cellの2状態自由度は、回路と容量から独立な対称collision bathで並列公平化される。

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

で全bankを一様にblank化できる。続いて定数次元sourceをroot modeへSWAPし、$M=nN$ 個のaperture cellを $R_{\rm bit}=M(k+1)$ 個の公平bitから作れる。dyadic tapeの全threshold誤差は $M2^{-k}$ 以下であり、$k=O(\log(M/\epsilon))$ で足りる。外部program長、準備時間、clock round、必要精度は $n,d,1/\epsilon$ の多項式である。静的couplerと受動clockが一括作用する限り、外部controllerの仕事をbank次元へ比例させない。cold bathとspent bathの受動自由度、状態容量、総作用移送、総熱は指数的でもよい。
<!-- theorem-end:theorem -->

R179は低作用bathを無から生成しない。供給測度は同じ局所lawを反復する回路非依存の積規則であり、出力確率表を含まない。外部精度を多項式に保つには、exact invariant blankを持つcold source、またはbank全体のaggregate誤差を一様contractで保証するcold sourceが必要である。有限温度の独立noiseが各modeに定数作用を残す場合、aggregate blank誤差は $D_{n,d}$ とともに増大するためR179の仮定を満たさない。

## M53の合成誤差と資源

M53の完全結果分布を $P_{\rm M53}$、理想回路Born分布を $P_{\rm circ}$ とする。誤差を重複計上しなければ、

```math
D_{\rm TV}(P_{\rm M53},P_{\rm circ})
\leq
\varepsilon_{179}
+d\eta_{\rm gate}
+\varepsilon_{\rm leak}
+2n\tau
+\frac{n\delta}{1+\delta}
+\sum_{j=1}^n\varepsilon_{{\rm stage},j}
+\sum_{j=1}^nr_j^N.
```

ここで

```math
\varepsilon_{179}
\leq
C_{\rm root}
(\varepsilon_{\rm blank}
+\varepsilon_{\rm src}
+\varepsilon_{\rm swap})
+\varepsilon_{\rm fair}
+M2^{-k}
+\varepsilon_{\rm guard}
+\varepsilon_{\rm coll}.
```

$\varepsilon_{{\rm stage},j}$ は第 $j$ 段のlatch、filter、repump、aperture境界、label、clockだけを含む。R179へ入れたtape bias、fair-bit mixing、cold floorと、別に書いた $r_j^N$ を再び含めない。

$\eta_{\rm gate}=O(\epsilon/d)$、$\tau,\delta,\varepsilon_{{\rm stage},j}=O(\epsilon/n)$、$N=O(\log(n/\epsilon))$、$k=O(\log(M/\epsilon))$ と選べる。保守的な逐次読出し時間は $O(n\log^2(n/\epsilon))$ である。受動modeとcold bath容量は指数的だが、回路記述、外部命令、準備round、gate窓、読出し時間、必要精度は多項式である。

## Q2-4の判定と境界

R178Aは指数個の個別gate設定、R178B--R178Fは全 $2^n$ 枝の読出し、R179は指数個の個別blank初期化を避ける。従ってM53はQ2-4を条件付き達成へ進める。条件は、R179のaggregate-cold port、回路非依存なfair-cell積測度、一様bank--bath結合、R178Fの滑らかなdyadic接続、およびgateからspent tapeまでの単一clock safe setである。

本構成は通常の計算量理論における多項式資源の古典simulationではない。指数個の受動自由度、静的結合、bath容量、総熱を許した上で、外部制御と総時間を多項式に抑える結果である。未知量子入力、適応中間測定、誤り訂正、固定容量bathによる無期限独立同分布標本は主張しない。M53はM52、M48と別の模型であり、Q2-1--Q2-4の共通ハードウェアを達成条件にしない。

## 物理的意味と限界

熱化終了後の局所記録生成子は、枝 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、列挙した部品を1つの具体的有限局所Hamiltonianへ統合済みだと主張しない。現行の条件付き達成または部分達成は、この未統合部分を明示して判定する。一意エルゴードな外部scheduleまたは有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。

# 第II部　単一量子ビット型操作と測定

# M47のHopf準備・条件付きGibbs再平衡化・傾斜測定

> **位置づけ：** Q1を、M50の2成分特殊化として2モード信号bath、条件付き作用殻、有限衝突熱浴、粒子位置の交互行程へ再編する。R164がBorn型状態数と条件付き中間状態有効自由エネルギーの起源を与える。Born分布、同軸反復分布、異軸逐次分布を導出済み部分とし、Zeno効果をQ1-2の残件として統合する。


## Q1の統計力学的再編と主張範囲

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

Q1の測定は次の仕事行程、熱化行程、記録行程へ分ける。

1. R145のHopf駆動で2モード信号bath方向を準備する。
2. 信号bath方向を保持し、R164の作用枝容量と条件付き作用殻fiberを準備する。
3. R161、R162で粒子位置を条件付きGibbs分布へ近づける。
4. 衝突熱浴を切り、W型2モードの傾斜制御で測定軸の固有方向を左右局在方向へ写す。
5. 分析器終了後に作用殻fiberを更新し、再び衝突熱浴を有限時間だけ接続して新しい信号bath方向へ粒子位置を再平衡化する。
6. 入射セルと辺遷移を止め、トンネル振動より速く、高モード間隔より遅く傾斜を立ち上げる。
7. 左右井戸の有効自由エネルギー差と閉じた辺ゲートで、既存の粒子位置を記録終了まで片側へ保持する。
8. 各井戸に置いた局所記録ポインターが、その場所にある $X$ だけを記録する。
9. 安全枝では、記録結果に対応する準備済み2モードテンプレートと信号bathを正準交換し、交換後方向へ作用殻準備と粒子位置再平衡化を行う。
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

共通M51/R171は、実正準担体のseed測度を雑音零の開放driftで押し出し、信号bath方向を目標位相円へ有限時間で吸引する。付録HのR145はそのW型2モード特殊化であり、別の準備機構ではない。共通R135は階数1共分散の統計因子を単一試行信号の支持へ接続し、M50/R164は同じ試行の有限信号作用を正則化枝容量へ写し、各排他的枝の2作用殻状態数からBorn型条件付き重みと有効自由エネルギーを導く。第2章のR161は任意有限信号方向に対する粒子位置の一様指数再平衡化、R162はその局所詳細釣合い率の有限衝突実現、続く粗視化経路熱力学系は制御切替と粒子位置経路の監査式を与える。R171/R145、R135、R164、R161を順に使えば、信号bath方向、条件付き状態数、粒子位置分布を同じ操作面へ有限誤差で準備できる。

第5章のR161のM48特殊化は、固定singlet型Bell装置に限って同じ平方根率を先に採用した結果である。R161はその数学的核を任意のM47 rayへ拡張し、R162は固定した単一試行信号bath座標に対する衝突熱浴実現を与える。R164は各翼の局所条件付き地形にも使えるが、paired-Hopf準備や2翼周期全体を導かない。R161、R162、R164をQ1の共通根拠とする。

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

と置く。左右の名称は $\langle L|x|L\rangle<\langle R|x|R\rangle$ となるように必要なら $\phi_1$ の符号を反転する。

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

となる。$-J\sigma_x$ は左右トンネル振動、$\varepsilon\sigma_z/2$ は左右エネルギー差である。

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

$J>0$ とし、傾斜 $\varepsilon(t)$ を正負の2値以上へ区分的に設定できるとする。最低2モード射影内では、有限個の定傾斜区間からなる制御列で任意の $U\in SU(2)$ を実現できる。各区間の共分散流はunitary共役であり、trace、正値性、階数を保存する。零傾斜では角周波数 $(E_1-E_0)/\mathcal J_0$ の左右占有振動を与え、一定傾斜では上の離調公式に従う。さらに $J\ll|\varepsilon_m|\ll G$ と $\mathcal J_0/G\ll\tau_q\ll\mathcal J_0/J$ の尺度階層では、高モード漏れを抑えながら左右占有変化を第3.7節の $\varepsilon_{\rm lock}$ で一様に抑えられる。
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

固定した有限格子W型族では、傾斜演算子の行列要素と時間微分が有界なら、2モード外漏れを

```math
\varepsilon_{2m}
\leq
C_W
\left[
\left(
\frac{|\varepsilon_m|}{G}
\right)^2
+
\left(
\frac{\mathcal J_0}{G\tau_q}
\right)^2
\right]
```

の形で抑えられる。$C_W$ は採用した有限W型族と切替形状に依存する。これは連続空間の一様上界ではない。

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

は全て $\sqrt{J/G}$ の次数で零へ近づく。

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

で評価する。全W型系の固定中分布誤差は $\varepsilon_{2m}+\varepsilon_{\rm lock}$ 以下である。$J/G\to0$ の深いW型族では、前節の選択により両者を任意に小さくできる。
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

1. R171のM47特殊化R145で信号bath方向を有限誤差 $\varepsilon_{\rm Hopf}$ 以内に準備し、初期操作面でR170を誤差 $\varepsilon_{170}^{\rm in}$ 以内に実行できる。
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

と分ける。R171/R145は $\varepsilon_{\rm Hopf}$ の信号bath方向部分を有限準備時間で抑える。条件付き作用殻状態数、粒子位置周辺、条件付き粒子位置分布はR164、R161、R162の後段準備・再平衡化へ移し、M51単独の誤差へ入れない。零seedと位相基準の失敗は独立に完全結果集合へ残す。

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
| Q1-2 | 部分達成 | R140、R143--R145、R161、R162、R164、R168、R170、R171 | Born分布、同軸反復分布、異軸逐次分布は導出済み。同一の零傾斜Rabi対照と反復測定を接続し、全履歴・無反応・tilt対照・有限誤差・資源を含む正のZeno抑制余裕を示すことが残る |

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
2. 具体的回路または有限bathからM51/R145の採用開放方程式を導出したこと。
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

# M52のQ1×Q1可逆tensor-lift永続状態bath模型

> **位置づけ：** R176A/B/Cを条件付き定理として分離する。一般積入力の可逆tensor-lift、同一永続状態上の有限ゲート列、末端Born型instrument接続を明示し、Q2-1を条件付き達成とする。


## 改訂した設計原則

Q2-1の固定目標は、2量子ビット型結合ゲートと同一の共同入力--出力統計を生成し、積入力を非分離な共同内部状態へ移し得る有限古典Hamiltonian過程を構成することである。M52は、この共同状態を経路だけに担わせる必要はない。4つまたはそれ以上の内部自由度が実在しても、それらが受動的なbath自由度であり、controllerが個別に扱う必要がなければ固定目標と両立する。

改訂後の設計原則は次のとおりである。

1. controllerが指定するのはQ1 port、lift窓、ゲート種、対象port、作用窓、末端読出しだけである。
2. 内部の4モードregister、8個の実正準座標、anti-register、work cell、clock履歴は許す。ただし各内部modeを外部から個別に初期化、較正、同期、address、読出し、resetしてはならない。
3. 一般入力から生じた同じ物理的状態bathを全ゲート間で保持し、中間で枝選択、粒子位置decode、tomography、集団moment推定、再準備をしない。
4. 可逆性に必要なanti-register、入力source、work、clock履歴を捨てない。
5. 排他的なBorn型結果は回路末尾だけでM50/R164/R170へ接続する。無反応も完全結果空間へ含める。

従って問題になるのは内部自由度の個数そのものではなく、外部interfaceが閉じているか、同一試行の状態が永続するか、余計な自由度をbathへ受動的に任せられるかである。旧M52の「4モードregisterを使わず経路だけで担う」という制約は撤回する。

## M52の状態とinterface

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

を置く。これは1試行の実正準座標から得る物理的な派生信号であって、M51の集団統計量

```math
 c=\mathbb E[z],
 \qquad
 C_Z=\mathbb E[zz^\dagger]
 \tag{4.3}
```

ではない。記号も用途も分ける。

可逆liftは同時にanti-register

```math
 G_S=\overline{a\otimes b}
 \tag{4.4}
```

を生成する。全状態を概念上

```math
 \Gamma_{52}
 =(\Gamma_{Q1,A},\Gamma_{Q1,B},Z_S,G_S,W_S,\tau,E_R,H,R)
 \tag{4.5}
```

と書く。$W_S$ はsource、work、lift clock、gate clockの可逆履歴を含む。$G_S,W_S$ は出力結果として読まず、逆写像を可能にするbath自由度として保持する。

外部interfaceは

```math
 \mathfrak I_{52}
 =(A,B;\,L_{AB};\,\{(g_r,S_r,t_r)\}_{r=1}^{L};\,M_{\rm end})
 \tag{4.6}
```

だけである。$L_{AB}$ はlift窓、$g_r$ は有限個のゲート種、$S_r$ は対象port集合、$t_r$ は作用窓、$M_{\rm end}$ は末端instrumentである。内部index $00,01,10,11$ をcontrollerの4本の独立命令として公開しない。

## R176A：可逆tensor-lift定理

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

<!-- theorem-start:theorem -->
**定理（R176A：可逆tensor-lift定理）**

正規化された有限次元Q1入力 $a\in\mathbb C^m$、$b\in\mathbb C^n$ とblank targetを考える。式(4.9)--式(4.11)は安全compact領域上の有限時間Hamiltonian流として

```math
 (a,b,0)
 \longmapsto
 (a,b,Z_S=a\otimes b,G_S=\overline{a\otimes b},W_S)
```

を実現する。source、anti-register、work、clock履歴を保持すれば、$S_0^{-1}$ と逆pulseにより写像全体を反転できる。近似pulse、cutoff、blank誤差に対しては安全compact領域上のLipschitz定数による有限誤差評価を持つ。
<!-- theorem-end:theorem -->

積の非線形性は、式(4.9)がsourceとtargetを含む3次Hamiltonianであることに担わせる。blank manifold上ではtarget momentumが零のためsourceは理想的に動かず、targetだけが平行移動する。これは未知入力の係数をcontrollerが読み取って書き込む操作ではない。

R176Aは固定 $m,n$ に対する定理である。$m=n=2$ および3入力への2段liftには有限の受動modeしか要らない。一般の入力数 $N$ に対するtensor反復の一様性はR176Aから主張せず、Q2-4では別模型M53の直接モードsector-broadcastを使う。

## R176B：永続状態bathゲート合成定理

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

3入力ではR176Aを2回使い、ゲート列の前に

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

<!-- theorem-start:theorem -->
**定理（R176B：永続状態bathゲート合成定理）**

R176Aで得た有限次元の同一状態bath $Z_S$ に、式(4.20)の有限個の非重複gate窓を作用させる。各理想gateを $U_r$、実装を $\widetilde U_r$ とし、

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
<!-- theorem-end:theorem -->

以前の「handoff map」は不要である。同じregisterを保持するため、有限誤差はlift、hold、clock、gate、leakageへ一度ずつ数える。経路展開は式(4.16)、式(4.19)の代数的な診断表示として残せるが、独立のR175や物理的経路分岐器を主結果鎖に置かない。

## R176C：末端Born型instrument接続定理

回路末尾の実際の1試行信号を

```math
 v=Z_{\rm out}(\omega)
 \tag{4.23}
```

とする。これは理想係数の再構成値でも集団共分散でもない。R112の同次元blank hold-registerへのcanonical SWAPで $V$ へ保持し、信号bathを計算registerから切り離す。

各結果 $y$ の容量を

```math
 J_y(V)=J_0|V_y|^2,
 \qquad
 J_\Sigma(V)=\sum_yJ_y(V)
 \tag{4.24}
```

とし、正則化容量とlatchを

```math
 A_y^\delta(V)=J_y(V)+\delta q_yJ_\Sigma(V),
 \qquad
 H_{\rm latch}
 =\sum_yP_y^A A_y^\delta(V)
 \tag{4.25}
```

で定める。blank容量momentum $P_y^A=0$ ではpointerだけが移動し、理想的な $V$ は動かない。latch後に信号をdecoupleしてからR164の作用殻、R161/R162の有限混合、R170の衝突・固定・記録へ渡す。

<!-- theorem-start:theorem -->
**定理（R176C：末端Born型instrument接続定理）**

R176Bの末端信号 $v$ が零でなく、canonical SWAP、容量latch、作用殻、有限混合、収集、固定、記録がそれぞれ安全compact領域上で定義されるとする。完全結果空間を

```math
 \Omega_{\rm out}=I_L\sqcup\{\varnothing\}
```

とする。正規化rayの実装誤差が $\varepsilon_{\rm ray}$、無反応率が $f_\varnothing$、末端各段を一度ずつ合計した誤差が $\varepsilon_{170}^{\rm end}$ なら、

```math
 D_{\rm TV}(P_{\rm out},P_{\rm Born})
 \leq
 f_\varnothing
 +\varepsilon_{\rm ray}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}.
```

理想的な共通radial因子とglobal phaseは式(4.24)の規格化で消える。
<!-- theorem-end:theorem -->

R176Cは条件付き定理である。R164、R170の既存部品に加え、容量pointerから作用殻への境界、有限fiber混合の枝対称性、SWAPから記録までの一体化を同じ有限Hamiltonian実装で満たす必要がある。成功試行だけの再規格化は行わない。

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

である。従ってR176Bの逆演算試験は、単なる4結果確率表より強い。

Q2-3では $Z_{ABC}$ に式(4.19)を順に作用させる。R177のGHZ--位相--逆演算試験は、coherent模型と中間枝選択模型の間に

```math
 D_{\rm TV}=\frac1{2\sqrt2}
 \tag{4.30}
```

の識別gapを与える。同じtensor-lift、同じ永続register、同じ二次gate、同じ末端instrumentを使うため、Q2-1、Q2-3は同一機構の有限次元特殊化である。

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
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}
 +f_\varnothing
 \tag{4.31}
```

と整理する。中間handoff、枝pairing、coherent decoderを独立項として二重計上しない。

R176Aは明示的な有限Hamiltonian構成、R176Bは同一有限register上の作用素norm合成を与える。R176Cは既存の末端bath部品へ接続する条件付き評価を与える。このためQ2-1は「部分達成」から「条件付き達成」へ更新する。残る条件は主としてR176Cの物理境界と全末端工程の一体化である。

Q2-3も同じ理由で条件付き達成とする。Q2-2はM48のsetting-pre等重みseedに基づく別経路であり条件付き達成のままである。Q2-4はM52の一般化ではなく、M53とR178A--R178F、R179を根拠に別途条件付き達成とする。

# M48の2端Bell測定周期と前提監査

> **位置づけ：** 固定singlet型・固定有限設定族について、M48内部の対称2枝作用殻に由来する等重みseed、paired-Hopf共有ray準備、切断後fresh局所作用殻の条件付き積因子化、局所分析、記録、弱開放帰還を閉じる。条件付き達成の判定は維持する。


## 目的と模型の境界

本章は、付録IのM48 paired-Hopf準備を、setting-freeな等重みseedから2つの物理的測定端、局所記録、次周期入口まで閉じる。M48の各試行で実在する信号変数は、2翼のbath作用角表示 $z_A,z_B$、W型有限配置グラフ上の粒子位置 $X_A,X_B$、freshな局所作用殻、設定、時計、局所雑音seed、記録・履歴・resetセルである。交差モーメント射影は集団統計であり、単一試行の制御器または結果変数ではない。

M48単独周期は次の5項目を順に閉じる。

1. 設定前の等重みseedを履歴から独立に保持し、A設定生成後に安全盆へ送る。
2. paired-Hopf流の各安全枝について、bath対と2翼粒子位置を強いmatching fiberへ準備する。
3. 中央結合を切った後は、A端とB端の生成子を因子化する。
4. 各局所分析器の終了後にmatchingを局所的に回復し、傾斜固定した粒子位置だけを記録する。
5. 外部記録を残したまま、能動部をfresh cell交換で次周期入口へ戻す。

全時刻でmatching多様体が厳密不変であるとは主張しない。切断面、局所分析器終了面、記録面というプロトコル面ごとにmatching誤差を評価する。M48内部のBell結果頻度に必要な橋はR147、R153、R155で閉じる。R161のM48特殊化はM50/R161と同じ平方根型核を持ち、各翼の局所条件付き地形にはR164の作用殻状態数、固定bath座標の局所遷移にはR162の有限衝突実現を利用できる。切断後局所殻の因子化はR155の局所性条件として扱う。ただしQ1とQ2を同一ハードウェアへ統合したことにはならない。

M48は採用開放古典模型である。paired-Hopf pump、設定controller、配置交換bath、傾斜固定、記録cell、fresh cell流を明示するが、全系を有限閉鎖Hamiltonianへ持ち上げたとは呼ばない。

共通M51/R171は各翼の有限ray seedを準備する局所部品として使えるが、M48のsinglet型交差モーメントや2翼strong matchingを準備しない。交差統計を単一試行のM51 templateへ書き戻す経路は採用しない。従ってM48のpaired-Hopf準備とM51を同じ結果として統合せず、共通なのは実担体、開放port、切断後の統計輸送という記述契約だけである。

## 設定前開始面と等重みseed

固定した有限A設定族を $\mathcal X$、有限B設定族を $\mathcal Y$ とする。設定前開始面では、設定生成角、固定pairing tensor $\mathsf E$、等重み枝seed $S_0\in\{+1,-1\}$、2翼の空W型配置、局所雑音seed、記録・履歴・resetセルを設定非依存測度 $\nu_0$ に置く。

```math
P(S_0=+1)=P(S_0=-1)=\frac12,
\qquad
\operatorname{Law}(S_0\mid x,y)=\operatorname{Law}(S_0).
```

$S_0$ は測定結果ではなく、設定生成前に存在する共通原因seedである。$J_+=J_-=J_{\rm seed}/2$ の対称2枝作用殻を単一母測度で数え、$\Omega_+=\Omega_-$ からM48内部の等重みcellを作る。使用済みseed殻は履歴識別子 $H_{\rm prov}$ だけを残し、設定と結果形成へ入力しない。paired-Hopfは共有rayを準備するが、この等重みの状態数起源ではない。

## setting-pre seedの履歴付き安全盆routing

A設定 $x$ の生成後、有限controllerはbright seed $m$ を

```math
S_0h_x(m)
\geq
h_*,
\qquad
h_x(m)
=
\frac{m^\dagger\Sigma_xm}{m^\dagger m}
```

となる安全盆へ有限時間で送る。有限設定族なので、各 $(S_0,x)$ に1つずつ安全seedと有限routingを用意できる。目的の測定開始分布を開始面へ直接置くのではなく、設定生成後の前向き開放写像として実行する。

**R153で使う安全盆routing構成。**

有限設定族 $\mathcal X$ と $h_*>0$ を固定する。設定前の等重みseed $S_0\in\{+1,-1\}$ と固定tensor $\mathsf E$ から開始し、各 $(S_0,x)$ について $S_0h_x(m)\geq h_*$ となるbright seedへ送る有限前向きroutingを構成できる。$S_0$ はM48内部cellから供給し、設定生成前に存在する。有限装置ではseed bias誤差を $\varepsilon_{\rm seed}$、盆外・routing失敗質量を $\varepsilon_{\rm route}$ として無反応へ送る。任意の許された履歴値 $h$ について

```math
\operatorname{Law}(A,B\mid x,y,H_{\rm prov}=h)
=
\operatorname{Law}(A,B\mid x,y)
```

とし、履歴はprovenance監査にだけ残す。この構成はR153の設定生成後準備節であり、一般状態Bell測定またはM52状態bathの受信を主張しない。

## R161/R170のM48局所特殊化

各翼のW型2モード埋込みを

```math
\Phi:
\mathbb C^2
\longrightarrow
\mathbb C^{|\Omega_W|}
```

とし、$\Phi^\dagger\Phi=I_2$ とする。$\Omega_W$ は有限連結配置グラフである。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と、正則化 $\delta>0$ を固定する。

単一試行のbath座標 $z\neq0$ に対して

```math
w_i(z)
=
\frac{
|\left(\Phi z\right)_i|^2
}{
z^\dagger z
},
```

```math
\pi_i^\delta(z)
=
\frac{
w_i(z)+\delta q_i
}{
1+\delta
}
```

と置く。$w_i$ は集団共分散または統計振幅を入力にせず、その試行に存在する2作用角と固定W型mode係数から作る局所controller信号である。

無向辺 $i\sim j$ に対し $a_{ij}=a_{ji}>0$ とし、粒子位置jump率を

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

とする。生成子は

```math
\left(
\mathcal L_X^zf
\right)(i)
=
\sum_{j\sim i}
k_{i\to j}^\delta(z)
\left[
f(j)-f(i)
\right]
```

である。これはR161で $m=2$、$\Psi=\Phi$ とした特殊化であり、物理的複素場からcurrent rateを作る規則ではない。付録LのR164は各翼の単一試行信号作用から $\pi^\delta$ の局所状態数起源を与え、付録KのR162は固定した単一試行bath座標に対する有限衝突熱浴実現を与える。

R161を直接適用すると、$z\neq0$ を固定した上のjump率は有限かつ非負で、隣接辺ごとに

```math
\pi_i^\delta(z)
k_{i\to j}^\delta(z)
=
\pi_j^\delta(z)
k_{j\to i}^\delta(z)
```

を満たす。従って $\pi^\delta(z)$ は一意定常分布である。$\lambda_X^\delta(z)>0$ を可逆生成子の第1非零固有値とすれば、固定有限seed集合上で有限定数 $C_X$ と一様下界 $\lambda_X^\delta>0$ を選べ、

```math
D_{\rm TV}
\left(
\operatorname{Law}(X_T\mid z),
\pi^\delta(z)
\right)
\leq
C_Xe^{-\lambda_X^\delta T}
```

となる。$\pi^\delta(e^{i\alpha}z)=\pi^\delta(z)$ であり、理想Born型対角 $w(z)$ との差は全変動距離で高々 $\delta/(1+\delta)$ である。正値性、詳細釣合い、有限時間収束は共通R161の内容であり、M48固有の独立定理番号を付けない。M48固有の記号対応とLipschitz評価は付録Dに置く。

各翼の局所分析後には共通R170を2枝グラフへ特殊化する。ただし作用容量fiberをpaired-Hopf準備、seed routing、2翼controller、信号bath保持へ統合した同一最小Hamiltonianを導いたことにはならない。

## 強いmatching fiber

規格化 $c\in\mathbb C^2$ に対し、強い正則化matching fiber $\mathcal F_W^\delta(c)$ を、次を満たす共同測度の族とする。

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)
=
\pi_i^\delta(z).
```

共通位相 $\alpha$ の分布は任意でよい。このfiberではbath共分散は $cc^\dagger$ であり、粒子位置周辺は $|\Phi c|^2$ から高々 $\delta/(1+\delta)$ だけずれる。M47のmatching条件より強く、単一試行bath座標に条件付けた粒子位置分布まで指定する。

$\delta=0$ の理想fiberを $\mathcal F_W^0(c)$ と書く。連続bath座標の有限時間近接を全変動距離で測ると、異なるrayに支持された測度間の距離が1になり得るため、切断面には次のprojective fiber距離を使う。規格化した目標対 $(u,v)$ に対して

```math
\begin{aligned}
d_{\rm pair}
\left(
(z_A,z_B),(u,v)
\right)
={}&
\left|\|z_A\|-1\right|
+
\left|\|z_B\|-1\right|\\
&+
\inf_{\alpha\in\mathbb R}
\left[
\left\|
\frac{z_A}{\|z_A\|}-e^{i\alpha}u
\right\|
+
\left\|
\frac{z_B}{\|z_B\|}-e^{-i\alpha}v
\right\|
\right].
\end{aligned}
```

枝符号の不一致、$X_A$、$X_B$ の不一致、および $d_{\rm pair}$ の和を1で切ったcostを $d_\Omega$ とする。切断面測度と理想fiber混合の間の $d_\Omega$-Wasserstein距離を $d_{\rm fib}$ と書く。離散配置部分では最適couplingの不一致確率が全変動距離に等しく、連続bath部分ではpaired位相を保った方向誤差を測る。この距離を完全状態の全変動距離と呼ばない。

paired-Hopf準備終了後、controllerを保持して $z_A,z_B$ を固定し、A、Bの粒子位置jumpを独立に有限時間走らせる。安全枝 $s$ の理想目標を

```math
u_{s,x},
\qquad
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

とする。

<!-- theorem-start:theorem -->
**定理（R153：M48中央切断面の2翼強matching準備）**

R147の有界seed条件、本章の安全盆routing、R161のM48特殊化の有限配置グラフを仮定する。paired-Hopf時間を $T_{\rm PH}$、配置混合時間を $T_X$ とする。理想切断面fiber混合を

```math
\nu_x^0
=
\frac12
\sum_{s=\pm1}
\mathcal F_W^0(u_{s,x})
\mathbin{\widehat\otimes}
\mathcal F_W^0(v_{s,x})
```

とする。中央切断面の完全状態測度 $\mu_{\rm cut}^x$ は、無反応部分を含めてprojective fiber距離

```math
\begin{aligned}
d_{\rm fib}
\left(
\mu_{\rm cut}^x,\nu_x^0
\right)
\leq
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

以内にある。$\widehat\otimes$ は枝符号とpaired位相を共有し、粒子位置jump noiseは条件付き独立であることを表す。この測度の交差モーメント射影は付録Iの交差モーメント補題のsinglet射影に有限時間誤差で一致し、同時に各翼の粒子位置周辺と条件付きbath分布がmatchingされる。
<!-- theorem-end:theorem -->

## 中央切断と局所分析器

切断後の状態を

```math
\Lambda
=
(\Lambda_A,\Lambda_B,s,\alpha,\mathcal H)
```

と書く。$\mathcal H$ は中央の使用済みsourceと受渡し履歴であり、局所結果形成には入らない。切断後の生成子を

```math
\mathcal L_{\rm post}^{xy}
=
\mathcal L_A^x
+
\mathcal L_B^y
```

とする。A、Bの局所雑音seedは $s,\alpha$ に条件付けて独立である。A設定 $x$ は中央準備ですでに使われている。B設定 $y$ は中央切断後にB局所controllerへだけ入る。

各翼には中央作用殻から独立なfresh局所2枝作用殻を置く。完全共通原因を $\Lambda$ とすると、付録Jの条件付き因子化補題は

```math
\mu_{\rm sh}^{AB}
(d\gamma_A,d\gamma_B\mid\Lambda,x,y)
=
\mu_{{\rm sh},A}^x
(d\gamma_A\mid\Lambda)
\otimes
\mu_{{\rm sh},B}^y
(d\gamma_B\mid\Lambda)
```

を与える。従って局所状態数、局所詳細釣合い率、切断後の経路エントロピー生成は条件付きで積または和に分かれる。$\Lambda$ を積分した後の結果は相関してよく、既存の余弦共同分布と矛盾しない。有限な残留結合、共通雑音、局所殻registerの取り違えによる偏差を $\varepsilon_{\rm prod}$ とする。

A端はR140の分析器 $A_x$ で $u_{s,x}$ を左右局在方向へ写す。B端は $A_y$ で $v_{s,x}$ をB測定基底へ写す。局所2モード操作中に粒子位置matchingが一時的に崩れることを許すが、操作終了後にbath方向を固定し、R161のM48特殊化の局所粒子位置流を時間 $T_{X,\rm meas}$ だけ走らせる。

その後、粒子位置jump prefactorを零へ切り替え、R140の傾斜固定を保ったまま記録する。従って記録窓中の経路滞在失敗は、rate切断残差と傾斜保持誤差へ明示的に分けられる。

## 局所記録と結果の一意性

各翼の左右安全領域に局所検出関数 $\chi_{w,+}(X_w)$、$\chi_{w,-}(X_w)$ を置く。分離面近傍は無反応とする。外部記録cellへの生成子を

```math
G_{\rm rec}
=
P_A^R
\left(
\chi_{A,+}-\chi_{A,-}
\right)
+
P_B^R
\left(
\chi_{B,+}-\chi_{B,-}
\right)
```

とする。理想空cellでは記録中の能動部への反作用は零である。結果集合は

```math
\{+1,-1,\varnothing\}^2
```

であり、無反応試行を除外して再規格化しない。

Markov jumpの局所noise seedを完全状態へ含めれば、記録時刻の $X_A,X_B$ と記録結果は各試行で一意に決まる。確率応答は外から結果重みとして与えるのでなく、R161のM48特殊化の開放粒子位置bathと設定前noise seedから生じる。

**R155の局所応答補題。**

R153の切断面から開始し、各翼へ共通R170の2枝特殊化を適用する。固定有限設定族について局所2モード制御誤差、2モード外漏れ、W型左右コントラストを有限とし、guardから離れたcompact安全域上の局所応答核は $d_\Omega$ に関して一様Lipschitzとする。付録Jの条件付き積因子化の下で、切断後にA、Bの直接結合を使わず、各翼のbath座標、粒子位置、設定、局所noiseだけから一意な局所記録を作れる。安全枝 $s$ についてA結果は $s$ から有限誤差内にあり、B条件付き結果は

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)
```

から局所instrument誤差内にある。切断後の応答核は完全状態に条件付けてA、Bに因子化する。
この補題の共通熱化、固定、記録部分はR170、2翼の局所分離は付録Jの因子化補題に尽くされる。R155へ追加するのはM48のpaired-Hopf切断面、2つの局所分析器、spin-flip関係から得る条件付きBell応答である。結果別2モードテンプレート交換、逐次測定後状態、Q1の一般射影instrumentは主張しない。

## 余弦共同分布、非信号性、CHSH値

枝seedは等重みであり、A記録は理想的に $a=s$ である。従って上の局所応答補題から

```math
P(a,b\mid x,y)
=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)
```

を得る。平面角では $\boldsymbol n_x\cdot\boldsymbol n_y=\cos(x-y)$ である。両周辺は

```math
P(A=a\mid x,y)
=
P(B=b\mid x,y)
=
\frac12
```

であり、相関は $E(x,y)=-\cos(x-y)$ となる。標準CHSH設定では $|S|=2\sqrt2$ である。これは固定singlet型平面2出力族の値であり、一般測定族を拘束するTsirelson原理の導出ではない。

## 前向き有限誤差

M48完全周期の前向き誤差を

```math
\begin{aligned}
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
\leq{}&
\delta_{\rm set}
+\varepsilon_{\rm seed}
+\varepsilon_{\rm route}
+\varepsilon_{\rm PH}
+L_{\rm fib}\varepsilon_{\rm fib}\\
&+
\varepsilon_{\rm an}^A
+\varepsilon_{\rm an}^B
+\varepsilon_{\rm X,meas}^A
+\varepsilon_{\rm X,meas}^B\\
&+
\varepsilon_{\rm lock}^A
+\varepsilon_{\rm lock}^B
+\eta_W^A
+\eta_W^B\\
&+
\varepsilon_{\rm guard}
+\varepsilon_{\rm rec}^A
+\varepsilon_{\rm rec}^B
+\varepsilon_{\rm clk}
+\varepsilon_{\rm prod}
\end{aligned}
```

とする。$L_{\rm fib}<\infty$ は固定有限設定族の安全域上で局所応答核を結果全変動距離へ移す一様Lipschitz定数である。R153の展開を使う場合、$\varepsilon_{\rm PH}$ と $\varepsilon_{\rm fib}$ の中の同じpaired-Hopf項を二重に数えない。

<!-- theorem-start:theorem -->
**定理（R155：M48完全Bell周期、有限誤差、局所性監査、帰還）**

各設定対について、M48の無反応を含む完全結果分布 $P_{\rm Bell}^{48,{\rm cyc}}$ と理想singlet分布の全変動距離は $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。従って一側周辺の反対設定による差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

```math
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。設定前測度 $\nu_0$ は設定に依存しないが、R153の前向きroutingとR147の準備後の切断面測度 $\mu_{\rm cut}^x$ はA設定に依存する。切断後の応答は完全共通原因に条件付けて局所因子化し、理想周辺は非信号的である。周期末に $r_{\rm ret}<1$ のfresh cell交換を行えば、第5.11節の上界で次周期入口へ戻せる。従ってBellの定理を否定せず、成立しない前提は測定設定独立性である。本定理はM48のreceiver側を記録と帰還まで閉じるが、付録Jの $T_{\rm link}$ を構成しない。
<!-- theorem-end:theorem -->

付録Iの理想局所応答補題は完全matchingを抽象的に仮定する。R153と本章の局所応答補題は固定Bell装置についてその仮定を有限誤差で充足する。第2章R170の安定性系を有界相関観測量へ適用して周辺差とCHSH差を抑え、R155の完全周期の結論を得る。

## Bell前提監査

| 監査項目 | M48完全周期での位置 |
|---|---|
| 局所性 | 切断後の生成子は $\mathcal L_A^x+\mathcal L_B^y$。fresh局所作用殻は完全共通原因に条件付けて積因子化し、反対翼の設定、結果、noiseを入力にしない |
| 測定設定独立性 | 設定前は共通測度。A設定生成後のseed routingとpaired-Hopf準備により $\mu_{\rm cut}^x$ が $x$ に依存するため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻を固定すれば、各翼の粒子位置と記録は一意 |
| 事後選別 | seed失敗、盆失敗、時計境界を $\varnothing$ として分母へ残す |
| 非信号性 | 理想singlet対称性から両周辺は $1/2$。有限装置では反対設定差を $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ で抑える |
| 試行測度 | 枝重みはsetting-pre等重みseed、粒子位置頻度はR161のM48特殊化の有限時間開放流から作り、測定開始面へ目的分布を直接置かない |
| provenance | 履歴は監査にだけ使い、許された履歴値で条件付けても結果法則を変えない |

$x$ と $x'$ が同じ非順序軸を表さない場合、理想切断面の2枝支持

```math
\left\{
u_{+,x},u_{-,x}
\right\}
```

と

```math
\left\{
u_{+,x'},u_{-,x'}
\right\}
```

は異なる。従って交差モーメント射影が両設定で同じでも、完全切断面測度は同じではない。設定依存性を2次交差モーメントだけで監査してはならない。

## 弱開放帰還

paired-Hopf準備と配置混合は散逸を含むため、前向き流を逆実行して開始点へ戻すとはしない。外部記録を保持した後、各翼の使用済みbath、配置seed、controller残差を流出cellへ交換し、設定非依存のfresh cellを次周期入口へ入れる。

能動部偏差 $\Delta_n$ の1周期写像を

```math
\Delta_{n+1}
=
R_{\rm ret}\Delta_n
+
\eta_n
```

とし、$\|R_{\rm ret}\|\leq r_{\rm ret}<1$、$\|\eta_n\|\leq\sigma_{\rm ret}$ とする。この交換は外部記録と使用済み状態を同一点へ戻さない。固定有限周期では有限個の外部cell、無期限運転ではcell流を持つ弱開放系として扱う。

**R155のfresh-cell帰還節。**

R147、R153、R155の固定有限設定周期について、$r_{\rm ret}<1$ のfresh cell交換を各周期末に行うと、

```math
\limsup_{n\to\infty}
\|\Delta_n\|
\leq
\frac{
\sigma_{\rm ret}
}{
1-r_{\rm ret}
}
```

である。有限時間のcontroller減衰を明示する場合は

```math
\varepsilon_{\rm ret}
\leq
C_{\rm ret}e^{-\lambda_{\rm ret}T_{\rm ret}}
+
\varepsilon_{\rm swap}
+
\varepsilon_{\rm seed}
```

とできる。$\varepsilon_{\rm ret}$ は同じ周期の記録分布へ遡って加えず、次周期の $\varepsilon_{\rm seed}+\varepsilon_{\rm route}$ へ渡す。固定有限周期数について、永久記録、使用済み状態、fresh cellを含む有限装置を選べる。

## 開放模型の局所帳簿

| 段階 | 外部作用 | 散逸先・情報流 |
|---|---|---|
| seed routing | setting-pre seedの読出しと安全盆routingの仕事 | seed履歴を使用済みcellへ移し、結果形成へ再注入しない |
| paired-Hopf準備 | bright pump、設定controller | dark sinkと振幅飽和bathへ熱・位相情報を渡す |
| 粒子位置matching | $z$ 依存局所有効ポテンシャルの制御仕事 | 各翼の配置交換bathへjump熱を渡す |
| 中央切断 | pairing、共通clock、中央粒子位置bathとの結合を停止する仕事 | 切断残差を $\varepsilon_{\rm cut}$ へ入れる |
| 局所分析 | A、B別々の2モード制御仕事 | 各局所controllerと粒子位置bathだけを使う |
| 固定・記録 | rate切断、傾斜、空記録cell | 記録情報を外部cellへ移す |
| 帰還 | fresh cell供給と使用済みcell排出 | 使用済みbath、配置seed、controller情報を外部へ流す |

粒子位置jumpについて

```math
U_i^\delta(z)
=
-\Theta
\log
\pi_i^\delta(z)
```

と置けば、rate比は

```math
\frac{
k_{i\to j}^\delta
}{
k_{j\to i}^\delta
}
=
\exp
\left[
-\frac{
U_j^\delta-U_i^\delta
}{
\Theta
}
\right]
```

となる。固定 $z$ でのjump熱は局所有効ポテンシャル差、$z$ またはsettingを変える間のポテンシャル変化はcontroller仕事である。第2章の粗視化経路熱力学系は各翼の粒子位置応答にも適用できる。一方、paired-Hopf pump、中央controller、2翼記録、resetまで含む総仕事、総熱、総エントロピー生成を閉じてはいない。

切断後に共同分布から

```math
E_{ab}^{\rm Bell}(x,y)
=
-\Theta\log P(a,b\mid x,y)
```

を作って物理的な大域ポテンシャルとして局所率へ戻してはならない。それは反対翼の設定を局所制御器へ再注入し、R155の条件付き局所因子化を壊す。完全共通原因に条件付けた局所有効自由エネルギーは加法的に使えるが、共通原因を平均した後の大域対数は共同分布を要約する情報量に限る。

## 有限時間と精度--資源交換

目標誤差を正に固定すれば、少なくとも

```math
T_{\rm PH}
\geq
\frac1{\gamma_{48}}
\log
\frac{K_{48}}{\epsilon_{\rm PH}},
```

```math
T_X
\geq
\frac1{\lambda_X^\delta}
\log
\frac{C_X}{\epsilon_X},
```

```math
T_{\rm ret}
\geq
\frac1{\lambda_{\rm ret}}
\log
\frac{C_{\rm ret}}{\epsilon_{\rm ret}}
```

と選べる。$\delta\to0$ では率比と混合時間が悪化し得る。深いW型で $\eta_W\to0$ とするとR140の操作時間が増え得る。設定族は固定有限とする。設定数、論理量子ビット数、回路深さ、逆誤差に対する全資源の多項式上界はQ2-4へ送り、本章の固定規模評価からは導かない。

## Q2-2判定と非主張

M48/M50とR147、R153、R155、R164、R168、R170により、固定singlet型、固定有限設定族、準備先行、非空間分離、プロトコル面matching、無反応込み、採用開放法則、弱開放帰還という解釈で、固定目標Q2-2を条件付き達成とする。この判定はQ2-1の特定実装またはM52からの受渡しに依存しない。

本章は次を主張しない。

1. 任意のQ2-1出力を一般状態Bell測定へ渡すこと。
2. 標準的な空間分離Bell実験または準備後の自由設定変更。
3. 一般測定族に対するTsirelson原理。
4. 独立同分布型有限標本揺らぎ。
5. R153のseed routingとpaired-Hopf準備を具体的回路または有限閉鎖Hamiltonianから導出したこと。
6. 連続時間の全区間で強いmatching fiberが不変であること。
7. R161--R164を用いただけでpaired-Hopf、seed routing、2翼controller、一般状態M48 receiver、測定後状態、逐次測定を解いたこと。
8. 全系の総エネルギー・総エントロピー収支を閉じたこと。
9. Q2-4の多項式外部制御による量子出力サンプリングを構成したこと。

# 第IV部　空間複素振幅場と粒子位置

# M37空間担体とM42局在トークン

> **位置づけ：** M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似をR86へ保ち、その下流に単一試行の局在粒子トークンM42を置く。M51準備、M37担体、R172--R174の等変輸送、有限衝突bath、終位置記録を二層模型として接続する。


## Q3の二層基本模型とM37の範囲

Q3の単一試行系は、M37担体層とM42粒子層を区別する。

| 層 | 単一試行で物理的に存在するもの | 派生表示・集団記述 | 役割 |
|---|---|---|---|
| M37担体 | 有限個の実振動子座標 $(q_i,p_i)$ と局所ばね結合 | 局所複素包絡 $b_i$、統計ray、規格化第2モーメント | R86の有限時間Schrödinger型担体 |
| M42粒子 | 1個の局在位置 $X_t$、局所辺bath、clock、履歴、記録 | 位置分布 $P(X_t=i)$ | R172--R174の局所輸送と終位置記録 |

複素包絡は実振動子状態の派生座標であり、複素rayと位置分布は多数試行の統計である。一方、$X_t$ は各試行に1つ存在する粒子位置である。M37だけから粒子位置や最小率が必然的に出るとは主張せず、M42の局所率、bath cell、更新則を追加の採用ミクロ法則として明示する。

共通M51/R171は、M37へ入れる前の実正準seed集団を開放driftでrank-one rayへ準備する。準備後の同じ単一試行信号にM50/R164の作用殻選択を一度だけ適用してM42の初期位置 $X_0$ を作る。その後はM37とM42を同時に進め、終時刻には新しい位置を再標本化せず、既存の $X_T$ をR112の局所記録回路で読む。このためM51、初期R164選択、終位置記録を独立なBorn型確率源として数えない。

ミクロ振動子層から有効担体への移行はQ3-1の固定達成基準であり、R86が満たす。M42は粒子実体と下流現象を追加する強化であって、Q3-1の判定へ遡及的に要求しない。M51のport、M37局所ばね網、初期作用殻、M42衝突bath、記録を同じ有限局所装置へ統合したとも扱わない。

Q1はM47のW型2モード、Q2-2はM48のpaired-Hopf周期、固定時刻の一般枝instrumentはM50/R170を使う。M42はQ3の空間セルだけに採用する。任意の装置用正準混合がM37の局所ばね網だけで実装できるとは仮定しない。M37がM47へ供給するのは、時間非依存の対称W型生成子、最低2固有モード、スペクトル間隔である。

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

初期集団をM51で準備する場合、設定前seed測度を $\mu_{\rm seed}$、準備切断面を $t_{\rm cut}$ とし、

```math
\mu_{\rm cut}^{c}
=
(\Phi_c^{t_{\rm cut}})_\#\mu_{\rm seed}
```

をM37初期面へ渡す。R171の安全事象外は無反応として残し、安全集団の第2モーメントだけが $cc^\dagger$ へ有限誤差で近づく。M37の初期分布へ $C_Z(0)=cc^\dagger$ を直接仮定する経路と、M51の押出し測度から得る経路を同じ準備状態と呼ばない。

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

共通R168は、M37標本を任意の固定時刻にM50へ渡した場合の枝統計を診断する一般定理として引き続き成立する。ただし現行Q3の粒子経路では、終時刻R170による新しい位置の再標本化に使わない。次の式はM51準備、R135共分散、M42初期選択の整合を検査するために残す。

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

## M51--M37--M42の開始面と終位置記録

準備切断時刻を $t_0$、終位置記録時刻を $T>t_0$ とする。M51/R171の切断面からM37初期面へ実正準担体を渡し、同じ試行の $Z_{t_0}(\omega)$ にM50/R164の作用殻選択を一度だけ適用して初期位置 $X_{t_0}$ を作る。統計因子 $c$、$C_Z$、全位置分布をcontrollerへ再注入せず、各試行の実信号と作用殻だけを使う。

$t_0<t<T$ では、M37実振動子とM42の現在位置、局所bath cell、clock、履歴を同時に進める。時刻 $T$ では別のM50位置を生成せず、R112の局所記録剪断で既存の $X_T$ を記録 $D_{X_T}$ へ写す。M50/R164は初期位置の物理化、R172/R173は同じ粒子の輸送、R112は終位置の記録を担う。

<!-- theorem-start:theorem -->
**定理（R174：M51--M37--M42の有限時間準備・輸送・記録受渡し）**

固定有限グラフと固定時間 $T$ について、M51/R171で担体集団を準備し、同じ試行の初期信号にM50/R164を一度だけ適用して $X_{t_0}$ を作り、M37と正則化M42を同時に進め、既存の $X_T$ をR112で記録する。完全結果分布と理想Born型位置分布の全変動距離は第6.14節の $\varepsilon_{174}(T)$ 以下である。安全事象外とcell overflowは無反応へ残し、成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

## 誤差、時間、資源、Q3-4・Q3-5への接続

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

と分ける。$\varepsilon_{\rm prep}$ はM51のrank-one準備とseed無反応、$\varepsilon_{\rm init}$ は1回のM50/R164初期位置選択、$\varepsilon_{37\to42}$ はR86担体誤差から正則化M42生成子へのDuhamel誤差である。同じM37包絡差をR135診断、M42生成子、終位置記録へ重複加算しない。

固定 $\rho,\sigma>0$ では最大率が有限なので、時間窓数、方向別閾値分割、Hamiltonian平滑化、仕事register範囲、有限衝突cell数、clock精度を増やして $\varepsilon_{\rm step}$、$\varepsilon_{\rm coll}$、$\varepsilon_{\rm over}$、$\varepsilon_{\rm clk}$ を任意に小さくできる。ただし $\rho,\sigma\downarrow0$ では最大率、必要cell数、閾値・clock精度、仕事register範囲が発散し得る。1つの固定装置で厳密nodeを追跡するとは主張しない。

R124の理想増分を $\alpha$、R125の理想分布距離を $\Delta$ とする。比較する各M42運転の誤差が $\varepsilon_{174}$ 以下なら、観測差はそれぞれ $\alpha-2\varepsilon_{174}$、$\Delta-2\varepsilon_{174}$ 以上である。有限パラメータで正にできるが、M51準備、M37伝播、初期作用殻、M42衝突bath、clock、終位置記録の単一Hamiltonian統合が未完了なので、Q3-4とQ3-5は条件付き達成を維持する。

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

Q3-1の固定基準自体はR86で満たされ、今回の改訂で後から基準を広げたわけではない。R171はM37初期集団に使える共通開放準備、R112は共通有限正準信号代数、R135はM37標本集団の共分散持上げ、R172はM42の理想等変輸送、R173は節正則化と有限衝突Hamiltonian近似、R174は準備から終位置記録までの誤差受渡しを追加する強化結果である。M51--M37--M42受渡しをQ3-1達成の根拠へ遡及的に加えない。

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
11. M51、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所Hamiltonianへ統合すること。
12. 源、シャッター、全検出器、散乱極限、初回到達、吸収、時間積分流束、連続運転スクリーンを扱う、固定目標より強い装置模型。

M47ではM37を、対称W型生成子 $h_W$、最低2モード $\phi_0,\phi_1$、モード分裂 $E_1-E_0$ を供給する層としてだけ使う。M42をQ1へ流用せず、M47の粒子位置はM50/R170の固定時刻instrumentに従う。M37のHamiltonianと反回転項の評価は変更しない。外部 $\lambda_{\rm prep}(t)$ による開放準備と閉鎖作用角伝播、matching受渡しの条件は第8章と付録Hに示す。

Q3の二乗統計はM51が準備するrank-one集団と、R164による1回の初期位置選択に由来する。M42は同じ粒子を輸送し、終時刻には再標本化せず記録する。状態数だけで初期選択の全ミクロ過程を説明したとはせず、有限衝突bathだけでM51準備や作用容量の起源を説明したとも扱わない。

# Q3の束縛状態、純位相緩和、障壁、2経路干渉

> **位置づけ：** Q3-2の再開課題、R123によるQ3-3の達成、R124・R125とM42/R174によるQ3-4・Q3-5の条件付き達成範囲をまとめる。


本章は、Q3-2の再開後の検証線、R123によるQ3-3の達成範囲、R124・R125による有限グラフ現象とM42局在トークンの条件付き接続をまとめる。有限グラフ現象の完全証明は付録F、G、M42輸送の証明は付録Nに置く。

## 位相量子化（Q3-2）

**固定目標と達成判定。** Q3-2は、巻数、節、単価性、位相すべりを一貫して扱い、位相量子化の成立条件を示すことで、Wallstrom 問題へ限定的に回答する。非零閉路での整数巻数、零点を通らない変形での不変性、節を介した位相すべり、格子細分化に対する安定性、非整数モノドロミーの力学的排除が必要である。

**運用状態。** Q3-2は未達の研究課題として再開する。本版では新しい定理、模型、数値結果を追加せず、達成へ進むための検証線を固定する。単価性を外から仮定する、閉路位相を整数へ丸める、整数巻数を許容条件として直接置く構成を達成としないという制限は維持する。

**再開後の検証線。** まず、頂点の非零複素包絡から辺位相差を主値で定め、閉路和を整数巻数として読む。零点と反対向き端点を避ける変形に対するhomotopy不変性を示す。次に、区分線形補間または離散Laplacianのエネルギー最小補間を物理的補間として固定し、振幅の正の下界と一様に有界な離散Dirichletエネルギーから、R86の一様細分化で巻数が安定する条件を導く。非整数モノドロミーを許すseamでは、格子幅 $a$ に対して局所エネルギーが少なくとも $a^{-1}$ で発散することを検査し、節が生じる場合だけ位相すべりで巻数変更を許す。この鎖を同じ有限局所構成で閉じて初めて達成候補とする。

**非主張。** 密度と流れだけを基本変数とする一般的な確率力学への完全回答、節を横切る閉路の巻数、外部ゲージ場、多粒子配置空間を含む一般化は主張しない。再開は新しい結果の宣言でも、達成判定の緩和でもない。

## 束縛状態（Q3-3）

**固定目標と達成判定。** Q3-3は、1次元の井戸型・調和型ポテンシャルについて有限個の非縮退低位固有状態の固有値、密度、節構造を再現する。さらに、有限環境との弱結合を縮約したエネルギー固有基底で、非対角相関の有限時間減衰と対角占有率の安定性を導く。1試行ごとの状態選択、基底状態への緩和、射影的な収縮、独立したエネルギー測定器は要求しない。

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

**達成判定。** R123は、井戸型・調和型の任意に固定した有限個の非縮退低位状態について、固有値、密度、節、格子・領域収束を与える。さらに有限自律Hamiltonian、初期調製、縮約、非対角相関の有限時間減衰、対角占有率の厳密保存、回復時間を与える。従ってQ3-3は改訂後の固定範囲で達成である。

**非主張。** 状態選択、固有状態を吸引状態とする機構、基底状態への冷却、射影収縮、不可逆な熱浴極限は導かない。二点運動量集団は外部乱数位相を時間ごとに注入する処方ではなく、開始面で明示した有限Hamiltonian環境の調製分布である。

## トンネル効果（Q3-4）

**固定目標と達成判定。** Q3-4は、有限障壁を持つSchrödinger型発展で、障壁値より低いエネルギー成分だけからなる状態が障壁反対側へ位置確率を移すことを示し、その確率を位置読出しへ接続する。散乱装置全体や透過率曲線は要求しない。

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

**達成判定。** R124は有限グラフの3分割、生成子、障壁値、障壁値未満の厳密スペクトル支持、初期基準確率、有限時刻の正の増分を与える。R172--R174は1個の局在トークンを初期分布から反対側へ輸送して記録する誤差付き接続を与える。ただしM51、M37、初期作用殻、M42衝突bath、clock、記録の単一Hamiltonian統合を仮定に残す。従ってQ3-4は改訂後の固定範囲で条件付き達成である。

**非主張。** 障壁高・幅・入射エネルギーに対する連続的な透過率曲線、半無限散乱極限、透過・反射・未確定を含む完全散乱装置、熱活性化との装置比較、初回通過、吸収器、到達時間分布は固定目標より強い拡張であり、本結果には含めない。

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

**達成判定。** R125は、有限グラフの直交2経路入力、同一発展、コヒーレント入力、同じ重みの混合、正のコヒーレンス差、正の相対位相差を与える。R174により、二つの理想分布間距離から各M42運転誤差を差し引いても正なら有限装置で識別できる。ただしM51、M37、初期作用殻、M42衝突bath、clock、記録の単一Hamiltonian統合を仮定に残す。従ってQ3-5は改訂後の固定範囲で条件付き達成である。

**非主張。** 幾何学的な開口、源、シャッター、多画素スクリーン、全検出器のHamiltonian、無検出を含む完全装置、初回到達、吸収、永久記録、反復resetは固定目標より強い拡張であり、本結果には含めない。

## M47との境界

付録HのM47は、対称W型ポテンシャルの最低2モードについて、固有状態単独でなく重ね合わせの左右占有分布が時間振動することを解析的に扱うQ1側のモデルである。R123--R125の数値または有限グラフ証明をM47の証拠へ読み替えず、M47をQ3-4、Q3-5の位置読出し根拠にも使わない。

今回の改訂では新しいW型数値解析を追加しない。共通R135とM47のR140は古典作用角と偶奇2モードから得る解析結果であり、M42をQ1へ流用しない。Q3-3の判定は維持し、Q3-4とQ3-5はM51--M37--M42の未統合仮定を反映して条件付き達成を維持する。

# 第V部　総合評価

# 誤差、資源、反証条件、未完成目標

> **位置づけ：** 現行のM51、M47、M52、M48、M37、M42、M50を横断比較し、共通R171、R135、R168、R170、Q2のR176A--R177、Q3固有R172--R174の台帳、有限資源、反証条件、未完成目標を整理する。


## 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168のray誤差へ同時に加える。
2. R164の有限幅・枝非対称誤差を、R170の作用殻誤差と系列固有instrument誤差へ重ねて入れる。
3. R153のpaired-Hopf方向誤差を $\varepsilon_{\rm PH}$ と $L_{\rm fib}\varepsilon_{\rm fib}$ の両方へ入れる。
4. R155の積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。
6. M51の同じtransverse偏差をR171のray誤差、R135の初期共分散誤差、系列固有準備誤差へ重ねて入れる。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

## M51/R171共通開放準備の誤差と資源

M51の安全事象を $G_*$、$q_*=(R_*^2-a_*^2)/a_*^2$ とする。準備切断面の上流誤差を

```math
\varepsilon_{51}
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

と分ける。$\varepsilon_{\rm seed}$ は完全結果集合の無反応質量、$\varepsilon_{\rm ray}$ は安全試行の方向誤差、$\varepsilon_{\rm cut}$ はport切断とM51から下流registerへの受渡し誤差である。M51の最小方程式は雑音零なので、有限bath雑音を仮定した誤差項をここへ暗黙に入れない。

目標ray誤差 $\epsilon_{\rm p}>0$ に対し、

```math
\tau_{\rm prep}
\geq
\frac{1}{\kappa}
\log\frac{\sqrt{q_*}}{\epsilon_{\rm p}}
```

を選べる。$a_*\downarrow0$ ではseed無反応質量を減らせる場合があるが $q_*$ が増え、準備時間、動的範囲、pump作用が増える。$\kappa\to\infty$ で時間だけを縮める場合も、sink結合強度と排熱率の資源を別に数える。

R171が定量化するのは縮約drift後の有限時間収束である。pump仕事、sink熱、template保持、clock切替、port履歴、有限bath交換の総収支は未導出であり、$\varepsilon_{51}$ が小さいことから熱力学的コストが小さいとは結論しない。M51のray誤差をR135で伝播した後、同じ偏差をR168または系列固有誤差へ再加算しない。

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

$\varepsilon_{\rm Hopf}$ はR145の有限準備、$\varepsilon_{\rm ctrl}$ は傾斜制御、$\varepsilon_{2m}$ は高モード漏れ、$\eta_W$ は左右有限コントラスト、$\varepsilon_{\rm br}$ は結果別template交換、$\varepsilon_{\rm post}$ は条件付き状態更新である。

固定有限段の逐次測定では、各段の全変動距離誤差を和で抑えられる。永久記録と使用済みcellは段数に比例して増える。作用容量、fiber、Hopf pump、controller、記録、resetを同じ有限局所Hamiltonian周期へ統合し、仕事・熱・エントロピー収支を閉じることは、M47を強める実装・熱力学的課題として残るが、Q1-2の達成条件には含めない。Q1-2の固定目標上の残件は、同じ明示的ミクロモデルで零傾斜Rabi対照と有限回反復測定を接続し、全履歴と対照を保ったZeno抑制を有限誤差で示すことである。

## Q2-1の誤差と資源

M52ではtensor-lift、同じ永続registerのhold、clock、各gate、外部bathへの漏れ、末端ray、Born型instrumentを分ける。長さ $L$ の回路誤差は

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

とする。中間handoff、経路pairing、coherent decoderを独立項として加えない。$Z_S$ は同じregisterに留まり、R176Cは末端で同次元canonical SWAPと容量latchを使うためである。$f_\varnothing$ は最初の失敗段階ごとに排他的に数え、成功試行だけを再規格化しない。各gateはmode別誤差の粗い和でなく、状態bath全体のglobal phaseを除くoperator normで抑える。R176Cの未統合境界は $\varepsilon_{170}^{\rm end}$ の構成条件として残す。

## Q2-2の誤差とBell監査

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

とする。M51の同じtransverse偏差を $\varepsilon_{\rm prep}$ と $\varepsilon_{37\to42}$ へ重ねず、R86の同じ包絡偏差をR135診断とM42生成子誤差へ二重加算しない。安全事象外とcell overflowは無反応として残す。

正則化誤差を小さくすると最大率は概ね $\rho^{-1/2}+\sigma/\rho$ で増え、有限衝突cell数、clock分解能、障壁精度も増える。任意の固定 $T$ と目標誤差に有限構成を選べるが、同じ固定装置でnode正則化を零にする一様資源上界はない。

R124の理想トンネル型増分を $\alpha>0$、R125の理想干渉分布距離を $\Delta>0$ とする。比較する各M42運転の誤差が $\varepsilon_{174}$ 以下なら観測差は

```math
\alpha-2\varepsilon_{174},
\qquad
\Delta-2\varepsilon_{174}
```

以上である。M51、M37、初期作用殻、M42局所辺bath、clock、終位置記録の単一Hamiltonian統合が残るため、Q3-4とQ3-5は条件付き達成である。

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

Q2-1からQ2-4は、次の根拠モデルと根拠結果から互いに独立に判定する。目標ごとに担体、浴、clock、準備・読出し原理が異なっても、それだけでは不達としない。

- Q2-1：M52とM50末端読出しを使う。根拠結果はR112、R164、R170、R176A--R176C。
- Q2-2：根拠モデルM48、M50。根拠結果R147、R153、R155、R164、R168、R170。
- Q2-3：M52永続状態bathの三部分系特殊化を使う。R112、R176A--R176C、R177を根拠とする。
- Q2-4：M53を使う。根拠結果はR112、R161、R162、R164、R178A--R178F、R179。

規模 $N$ ごとの一様な共通ハードウェア族へ統合することは、固定目標の達成条件ではなく実装努力目標である。将来これを主張する場合は、同じ物理port、永続状態浴、相互作用区間族、clock・制御bus、準備interface、Born型読出し・記録interfaceを共有する具体的な装置族を示す。共通の正準代数またはinstrument契約だけでは同一装置とみなさない。

受動資源と能動資源を分ける。受動的な浴自由度、正準対、coherent経路、静的結合、状態容量、受動並列度は指数的でもよい。ただし規模を報告し、一様な有限規則から生成する。次は受動資源とはみなさない。

1. 各モードを個別に初期化、設定、較正、同期、リセットする操作。
2. 指数個の係数、配線、時刻窓、結果枝を外部から指定すること。
3. 回路ごとの物理的な配線変更、全モード走査、全枝読出し。
4. 指数的に細かい精度、小さい成功率、長い準備・混合・実行時間。

現行M52、M48、M53は同じ共通ハードウェア族へ統合されていない。この未完成性は、各目標の根拠モデルによる個別達成判定を変更しない。一方、Q2-4自身の固定条件として、受動資源と外部制御資源を区別する上の台帳は維持する。

## Q2-3の3量子ビット型二段ゲート合成

3つのQ1型、すなわち2状態の論理部分系を $A,B,C$ とし、2つの2量子ビット型結合ゲートを $A$--$B$、続いて $B$--$C$ へ作用させる。ここでQ1型とは論理状態空間を指し、3台のM47装置またはQ1との共通ハードウェアを要求する語ではない。最小検査列の一つは

```math
|+\rangle_A|0\rangle_B|0\rangle_C
\longmapsto
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|111\rangle}{\sqrt2}.
```

R176Aをgate列の前に2回作用させて $a\otimes b\otimes c$ を作り、第1ゲート後も同じM52永続状態bathを保持する。枝を測定せず、共同momentから新しい入力を再準備しない。さらにAへ $T=\operatorname{diag}(1,e^{i\pi/4})$ を作用させ、2つのゲートと最初のHadamardを逆順に戻す。R177の理想coherent出力は

```math
P(000)=\cos^2\frac{\pi}{8},
\qquad
P(100)=\sin^2\frac{\pi}{8},
```

完全dephasing出力は両者が $1/2$ であり、全変動距離は $1/(2\sqrt2)$ である。coherent側と混合側の装置誤差の和がこの値未満なら正の識別余裕が残る。

R176Aは3入力の有限tensor-lift、R176Bは同じ8mode register上の2つの二次gate zoneと逆演算、R177は上の識別余裕を与える。R176Cが末端Born型instrumentへの条件付き接続を与えるため、Q2-3は条件付き達成である。残る条件は容量pointer--作用殻境界、有限fiber混合の枝対称性、SWAPから記録までの単一clock統合である。8modeが受動的に存在すること自体は失敗条件ではない。失敗条件は中間で統計量へ縮約して再準備すること、または各modeを外部から個別に初期化、較正、同期、address、読出し、resetすることである。

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

M53は $L=2^n$ 個のsignal modeを使うが、R178Aにより固定有限局所gateをspectator sectorへ同じ係数でbroadcastし、作用素norm誤差をsector数の和ではなく最大値で抑える。R178B--R178Cは各bitを直交projectorで可逆にfilterし、条件付きBorn確率を逐次標本化する。確率 $\tau$ 未満の枝を切断して $\varnothing$ に残すため、切断誤差は $2n\tau$ 以下であり、事後選別を使わない。

R178Dは出力と相関しないworkだけを逆掃除でき、結果情報はspent側に残ることを示す。R178E--R178Fは容量に比例する可変体積を生成せず、固定体積cell、最小indexのaccept、滑らかな二channel apertureを使う。1 bit当たり $N=O(\log(n/\epsilon))$ 個のcellと $O(\log(n/\epsilon))$ の散乱時間で有限誤差を得る。R164の作用容量 $A_b$ とaperture入口体積は同じ重みの二重計数ではない。

R179は同一静的couplerと受動clockによる一定精度のpartial SWAPを反復し、active残差を幾何的にcold floorまで縮める。外部controllerのquench workをbank次元へ比例させない。回路非依存の対称2状態bathからfair digitを取り、$k$ digitのdyadic中点 $U_k$ を作る。離散lawと連続一様lawのtotal variation距離は用いず、threshold discrepancy $2^{-k}$ を用いる。有限runではblank-bankを初期状態に積み、無期限runではcold inflowとspent outflowを仮定する。

以上は各構成部品と合成誤差・資源の定理を与える。ただし、静的sector配線、projector latch、repump、history掃除、smooth aperture、blank-bank、clockを一つの具体的な一様装置族へ統合する物理境界が残る。この条件の下でQ2-4を条件付き達成とする。

## 反証条件

現行主張は次の検査に失敗した場合に縮小または撤回する。

| 対象 | 反証条件 |
|---|---|
| M51/R171 | 実変数driftと複素式が一致しない、安全seed上のray距離が指数上界を破る、無反応質量を落とさずM50分布へ接続できない |
| M47/R143 | Hopf方向が有限時間で準備できない、R170特殊化後もBorn型枝と局所記録が一致しない、結果別状態更新が失敗する |
| M52/R176A--R177 | tensor-liftの正規化または正準性が破れる、集団momentから再準備する、同じregisterを保持できない、参照系相関または逆演算fringeが壊れる、各modeの個別外部制御が必要、R176Cの完全結果誤差境界を満たさない |
| M48/R155 | 条件付き積因子化が破れる、局所R170応答が反対翼設定を参照する、無反応込みでCHSH誤差上界を満たさない |
| M53/R178A--R179 | sectorごとの誤差を指数個加算する、projector filterが正準でない、希少枝を事後除外する、first-index以外の到着競争を使う、aperture backreactionを消す、使用済みcellを履歴なしにblankへ戻す、回路依存のtape法則を入れる、または単一の一様装置族へ統合できない |
| M37/R86・R135 | 有限時間包絡上界または第2モーメント持上げ上界を超える |
| M42/R172--R174 | 局所master方程式がM37辺流を再現しない、正則化全変動上界を破る、有限衝突近似が安全領域で収束しない、終時刻に同じ粒子を記録できない |
| R168 | 可変作用集団でray平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| R170 | 混合上界、局所記録の排他性、履歴単射性、正の処理時間のいずれかを満たさない |
| Q2共通ハードウェア努力目標 | 同一装置を主張しながら目標ごとに担体、浴、準備・読出し原理を交換する、または装置族を一様な有限規則で生成できない |
| Q2-3二段ゲート合成 | 第1ゲート後の単一試行状態を破壊せず第2区間へ渡せない、中間共同モーメントから再準備する、GHZ--$T$--逆演算の $1/(2\sqrt2)$ 余裕が全装置誤差を上回らない |
| Q2-4 | 受動モードごとの設定・較正・読出し、指数長の係数表、回路別配線、指数時間または指数精度が必要になる。総bath容量と総熱が指数的であることだけでは反証にならない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 固定目標の残件と実装強化課題

固定目標上の未完成事項は次である。

1. Q1-2について、同じ零傾斜Rabi対照と反復R143/R170測定を接続し、全履歴、tilt対照、有限誤差、資源を含む正のZeno抑制余裕を示す。
2. Q3-2について、閉路巻数、homotopy不変性、節を介した位相すべり、R86細分化安定性、非整数seamのエネルギー発散を統合する。
3. Q2-1について、R176Cの容量pointer--作用殻境界、有限fiber混合、固定、記録を単一clock scheduleで閉じる。
4. Q2-3について、同じR176C末端条件を8mode特殊化で閉じ、R177の識別余裕より小さい全装置誤差を選ぶ。
5. Q2-4について、M53の静的sector配線、projector latch、repump、history掃除、smooth aperture、blank-bank、clockを一つの具体的な一様装置族へ統合し、各局所誤差の独立な物理上界を与える。

次は固定目標の達成判定と分けて管理する実装・熱力学的強化課題である。

1. M51のpump、transverse sink、template、clockを有限bath、仕事源、排熱先へ持ち上げ、雑音と準備誤差と総収支を同じ模型で閉じる。
2. R170の作用容量結合、作用殻fiber内平衡化、信号保持、衝突bath、枝固定、記録をQ1・Q2の1つの有限局所Hamiltonianへ統合する。
3. M47のM51準備から結果別状態更新、永久記録、resetまでの周期総収支を閉じる。
4. M48のpaired-Hopf準備、2翼局所R170、controller、fresh cell流を同じ具体装置へ統合する。
5. Q3でM51切断面、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録までを同じ有限局所装置へ統合する。
6. 連続空間、多粒子を扱う。
7. Q2共通ハードウェア努力目標として、同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceをQ2-1からQ2-4で共有する一様な装置族を得る。

Q1-1、Q3-1、Q3-3は個別機能として達成、Q1-2は部分達成、Q2-1、Q2-2、Q2-3、Q2-4、Q3-4、Q3-5は条件付き達成、Q3-2は未達である。Q2-1とQ2-3の条件はR176Cの末端物理接続、Q2-4の条件はM53部品の一様装置統合へ集約される。Q2共通ハードウェア族は判定外の努力目標として未完成であり、その成否を個別判定へ遡及させない。

# 結論

> **位置づけ：** M51のrank-one開放準備、M50のBorn型instrument、Q1のM47、Q2-1・Q2-3のM52/R176A--C、Q2-2のM48、Q2-4のM53/R178A--R179、Q3のM37--M42二層模型を総括する。


## 確立したこと

M51は、有限個の実正準担体、物理template、動径pump、transverse sink、clockを持つ共通基礎開放模型である。採用した雑音零driftに対し、R171は設定前seed測度の押出し、目標rayへの有限時間指数収束、rank-one第2モーメント、準備port切断後の実正準伝播とR135輸送を与える。各試行の実体は実担体と装置自由度、複素信号は派生座標、量子状態に対応するrayは試行集団の統計因子である。

Q1をM47のW型2モード共同統計へ移した。R145はR171のW型2モード特殊化であり、独立の準備機構ではない。共通R135は階数1bath共分散のBloch球、R140は1次傾斜制御による任意の $SU(2)$、零傾斜占有振動、離調Rabi式、左右エネルギー差による占有周辺固定を与える。R143は有限コントラストの左右読出しと結果別状態更新を共通R170へ追加する。2モード射影内の共分散制御と遷移式は厳密であり、全W型系では高モード間隔、切替時間、左右重なりを明示誤差として分けた。R135、R140によりQ1-1を再構成し、達成と判定した。

M50/R164は一般有限信号作用を枝容量へ写し、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き状態数が得られることを示す。二乗形の状態依存性はM51が準備するrank-one第2モーメントに現れ、M50/R164は各試行の実担体信号から排他的結果の状態数を作る。この二段を二重の確率源として数えない。R161は条件付きGibbs再平衡化、R162は有限衝突熱浴を与え、その系として条件付き中間状態の正逆経路確率比と相対有効仕事が従う。作用殻明示表示と消去表示を同じ分配関数で二重計数せず、殻自由エネルギー仕事 $W^{\rm sh}$ と相対有効仕事 $W^{\rm rel}$ を区別する。

R143はHopf方向準備、操作面ごとの再平衡化、解析器、傾斜固定、辺閉鎖、M47粒子位置の局所記録、結果別テンプレート交換、測定後再平衡化を合成する有限誤差instrumentである。記録器は統計振幅、共分散、全密度、確率流、遷移率を入力にせず、各試行に存在する $X$ の局所位置だけを読む。R144は固定有限段について永久記録、内部逆計算、外部空セル交換を合成する。解析器中または周期間に配置--信号bath matchingを連続保存することは仮定しない。

Q2-1には改訂M52を置いた。受動的な4mode信号、anti-register、work、clock履歴をbathへ任せ、controllerはport、lift窓、gate種、対象、作用窓、末端読出しだけを指定する。R176Aは一般積入力の可逆tensor-lift、R176Bは同じ永続register上のCNOT、局所操作、逆演算と参照系安定な有限誤差合成を与える。R176Cはcanonical SWAP、容量latch、M50/R164/R170への条件付き末端接続を与える。末端の物理境界と一体化を条件としてQ2-1は条件付き達成である。

Q2-2にはM48を採用した。付録Iの否定命題は積bath標本の直接4次元共分散をsinglet階数1射影へできないことを示し、R147は設定依存paired-Hopf流の2枝吸引多様体と有限時間率を与える。singlet交差モーメントはR153の準備補題、完全matching下の余弦共同分布はR155の理想応答補題として管理する。

R153はM48内部の対称2枝作用殻に由来する等重みseedをpaired-Hopf安全盆へ送り、切断面の2翼strong matchingまでを扱う。paired-Hopfは共有rayを準備するが、Born重みの状態数起源ではない。R155は切断後のfresh局所作用殻と局所応答が完全共通原因に条件付けて積因子化し、経路エントロピー生成が加法的になること、余弦共同分布、非信号性、CHSH差、fresh-cell帰還をまとめる。共通原因を平均した大域Bell対数を物理的な切断後ポテンシャルへ戻さない。M52の1試行信号 $Z_S$ とM48の試行集団交差momentは別の概念であり、相互に再注入しない。

Q3ではM51/R171からrank-one初期集団を受け取り得る契約を上流に置き、M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似、作用比診断をR86へまとめる。その上に、各試行で1個の局在粒子位置、局所辺bath、clock、履歴を持つM42を置く。R172はM37有効辺流に沿う等変輸送と有限期待跳躍数、R173は節一様正則化と有限衝突Hamiltonian近似、R174はM51準備、1回の初期R164選択、M37担体、M42輸送、終位置記録の誤差台帳を与える。R123--R125の束縛状態、純位相緩和、障壁値未満確率移動、最小2経路干渉を維持し、後2者をM42へ接続する。終時刻に別のM50位置を再標本化しない。

## 条件付きで確立したこと

R143の結果分布と条件付き状態は、R171/R145の信号bath方向準備、R164の作用殻準備、R161の有限時間再平衡化、R162の有限衝突近似と辺閉鎖、傾斜保持、局所記録、枝別テンプレート交換の誤差上界に条件付く。大域階数1共分散だけでは枝別測定後状態が生じないため、結果枝の非規格化共分散を独立に評価した。

Q1-2の測定統計部分は達成している。M51/R171がrank-one統計準備、R164がBorn型状態数と有効自由エネルギーの条件付き起源、R143とR144がBorn分布、同軸反復分布、異軸逐次分布を有限誤差で与える。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。有限局所Hamiltonian統合または有限閉鎖Hamiltonianへの持ち上げ、完全周期、永久記録、reset、周期全体の仕事・熱・エントロピー収支は、Q1-2の達成条件ではなく実装・熱力学的強化課題である。連続matching保存または周期間matching帰還も現行測定統計の必要条件ではない。

R155の理想局所応答補題は、2翼完全matchingを抽象仮定にする。R153とR155の装置構成は固定Bell装置について、その仮定、R170の2翼局所特殊化、切断後局所作用殻の積因子化を有限誤差で充足する。一方、切断面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。

M48単独周期は条件付き達成である。条件は、固定singlet型、固定有限設定族、準備先行、非空間分離、プロトコル面matchingである。交差モーメントを単一試行頻度と同一視せず、R161のM48特殊化の局所粒子位置bathを明示した。R162はこの粒子位置応答を有限衝突bathで近似実現するが、paired-Hopf準備、seed routing、2翼controllerを同じミクロ回路へ統合したことを条件付き達成へ含めない。

固定目標Q2-2全体は条件付き達成である。M48単独の条件は固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則、プロトコル面matchingである。Q2-2の達成判定は特定のQ2-1実装に依存させない。M52出力を受け取る一般状態M48 receiverは現行結果に含めない。

固定目標Q2-3は条件付き達成である。R176Aをgate列の前に2回使って8mode信号を作り、R176BのA--B、B--C二次生成子と逆演算を同じ永続registerへ作用させる。R177のGHZ--$T$--逆演算ではcoherent出力と完全dephasing出力の全変動距離が $1/(2\sqrt2)$ になる。Q2-1と同じR176Cの末端接続条件が残る。

固定目標Q2-4は条件付き達成である。M53は $2^n$ 受動signal modeを許し、R178Aが局所gateをspectator sectorへ一様にbroadcastする。R178B--R178Cは可逆2枝filter、条件付き確率のtelescoping、希少枝切断、有限利得repumpを与える。R178D--R178Fは逆掃除可能なhistoryの範囲、fixed-volume fresh tape、最小index選択、滑らかなaperture散乱とbackreactionを与える。R179は一定精度partial SWAPの反復、fair-bit源、dyadic threshold tape、cold/spent bankを与える。残る条件はこれらを単一の一様装置族へ統合することである。

Q2-4では総bath容量と総熱を多項式としない。signal、work、history、cold、spentの受動容量は指数的でもよい。その代わり、外部program、制御channel、精度、反復回数、総時間を多項式に抑え、指数個の個別address、確率表、回路別配線、稀な成功、事後選別を使わない。この限定は通常の効率的古典simulationではない。

## 確立していないこと

M51について未導出なのは、pump、transverse sink、template、clockを具体的な有限bath、仕事源、排熱先から導くこと、雑音付き有限時間誤差、揺らぎ散逸関係、準備portの総仕事・熱・エントロピー生成を閉じることである。R171は採用した縮約drift後の厳密結果であり、そのdriftの有限閉鎖Hamiltonian持上げではない。

M47について未導出なのは、M51/R145の開放portをW型装置へ統合すること、R164の作用容量結合・fiber内平衡化・枝対称性を有限局所Hamiltonianとして構成すること、R162の衝突散乱と信号bath保持controllerを同じ最小有限Hamiltonianへ統合すること、粗視化された有効仕事・熱を全微視的台帳へ持ち上げてpumpからresetまでの全周期ゆらぎ関係へ拡張することである。時間依存傾斜をM37のミクロ位置ばね網から一様誤差付きで導くこと、連続空間極限、多粒子も未完成である。

M48について未導出なのは、具体的な回路または振動子bathからpaired-Hopf方程式とR153のseed整列を導き、R162の衝突粒子位置bath、fresh cell流まで統合すること、連続時間の全区間で強いmatching fiberを不変にすること、一般Q2-1出力を一般状態Bell測定へ接続することである。A設定が中央準備へ入るため、空間的に分離した自由設定Bell実験を再現したとはいえない。総仕事、総熱、総エントロピー生成も閉じていない。

Q1-2のZeno部分は未達であり、同一の零傾斜Rabi対照と反復R143/R170測定を接続する必要がある。傾斜による離調固定、障壁増大、駆動停止、摩擦、事後選別をZeno効果とは呼ばない。Q3-2も未達だが、閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を統合する課題として再開する。

Q3-4とQ3-5は条件付き達成である。有限グラフ現象の代数部分はR124、R125で確立し、R171はrank-one初期集団の開放準備、R172--R174は局在トークンの有限時間輸送と記録への接続を与える。一方、M51準備port、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録を同じ有限局所装置へ統合していない。最小率の一意なミクロ選択、正則化零極限の一様資源、同一ハードウェアと統一母測度を持つM0、独立同分布型有限標本統計も未完成である。

Q2-1はM52、M50末端読出しとR112/R164/R170/R176A--C、Q2-2はM48/M50とR147/R153/R155/R164/R168/R170を根拠として独立に判定する。Q2-3はM52三部分系特殊化とR112/R176A--C/R177、Q2-4はM53とR112/R161/R162/R164/R178A--R178F/R179を根拠とする。目標ごとに異なる担体、bath、読出し原理を使うことは個別判定を変更しない。

Q2-1からQ2-4に共通する一様なハードウェア族は、判定外の実装努力目標として未完成である。同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceを全目標で共有する構成をまだ得ていないが、この未完成性をQ2-1またはQ2-2の達成状態へ遡及させない。

Q2-4で確立していないのは、M53の静的sector配線、projector latch、repump、history掃除、smooth aperture、blank-bank、clockを一つの具体的な一様装置族へ統合し、局所誤差上界を同時に実現することである。cold bathを閉系から生成すること、有限bankで無期限運転すること、使用済みcellを履歴なしにblankへ戻すこと、指数受動容量または総熱を多項式へ削減することも主張しない。

## 次の決定的検査

Q1-2の次の決定的検査は、同じ総時間の零傾斜Rabi自由対照、測定中もRabi項を止めない有限回測定、flip・reflip・無反応の全履歴、tiltだけの対照を同じ明示的ミクロモデルで比較し、正のZeno抑制余裕が重なり・傾斜・自由発展・1段instrument誤差を上回るかを示すことである。反復回数に伴う時間、記録、fresh cell、エネルギーの増加も同じ台帳で評価する。

これとは別に、M51のpump、transverse sink、template、clockを有限bathへ持ち上げ、R164の作用容量結合、fiber内平衡化、枝対称性と同じW型装置へ統合すること、R162の有限衝突bath、信号bath保持controller、任意軸分析器、傾斜切替、局所記録、枝別テンプレート交換、resetを同じ有限時間Hamiltonian台帳へまとめること、粗視化経路熱力学を周期全体の微視的ゆらぎ関係へ拡張することは、実装・熱力学的強化課題として残る。$\delta\downarrow0$、深いW型、長いfiber準備・混合時間の精度--時間--エネルギー交換もこの強化課題で監査する。

Q2-1とQ2-3の次の検査は、R176Cのcanonical SWAP出口、容量pointer、R164作用殻、有限fiber混合、collection、lock、recordを共通safe setと単一clock scheduleで閉じ、完全結果誤差を逆演算gapより小さくすることである。Q2-2ではR162の有限衝突bathをR153の安全盆routing、paired-Hopf pump、2翼controllerへ統合し、熱・仕事・情報流を同じミクロ模型で閉じる。Q2-4ではM53の全区間を一つのclockへ接続し、sector漏れ、latch、repump、aperture境界、tape bias、cold floorの誤差を同じ安全集合上で同時に抑える。

Q3の次の検査は、M51切断面をM37初期面へ物理的に接続し、初期R164作用殻、M42の局所辺衝突bath、clock、履歴、終位置記録までを同じ有限局所装置へ統合して、誤差台帳と総収支を閉じることである。加えて、採用した最小率を選ぶ具体的装置理由と、節正則化を小さくしたときの資源発散を検査する。Q3-2では、頂点包絡から辺位相と閉路巻数を定義し、零点を避けるhomotopy不変性、エネルギー最小補間、R86細分化安定性、非整数seamの $a^{-1}$ エネルギー発散、節を介した位相すべりを一つの鎖で検査する。M48の空間分離拡張、R123の連続環境極限、R124・R125の散乱・吸収拡張は、それぞれ固定目標と区別して監査する。

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

$x_{01}=\langle\phi_0|x|\phi_1\rangle$ を実非負に選べば

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

左右の名称または傾斜符号を選び直せば本文の $\varepsilon=2F|x_{01}|$ の形になる。

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

## 2モード漏れの有限次元評価

有限格子上の全生成子を、最低2モード射影 $P$ と補空間 $Q=I-P$ に分ける。傾斜摂動を $V(t)=-F(t)x$ とし、観測区間で

```math
\|PVQ\|
\leq
v,
\qquad
\operatorname{dist}
\left(
\operatorname{spec}(PhP),
\operatorname{spec}(QhQ)
\right)
\geq
G
```

とする。$v/G<1/2$ なら、スペクトル射影の静的回転は $O(v/G)$、確率漏れは $O((v/G)^2)$ である。滑らかな切替では、瞬時射影の時間微分に由来する振幅が $O(\mathcal J_0/(G\tau_q))$ である。有限次元かつ固定切替形状なので、両者をまとめる定数 $C_W<\infty$ が存在し

```math
\varepsilon_{2m}
\leq
C_W
\left[
\left(
\frac{v}{G}
\right)^2
+
\left(
\frac{\mathcal J_0}{G\tau_q}
\right)^2
\right]
```

となる。本文では $v$ を $|\varepsilon_m|$ と同じ次数へ吸収した。この評価は固定有限格子族の作用素ノルム上界を使う。格子幅を零へ送るときに $C_W$ が一様とは主張しない。

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

一般入力の周辺固定項は $2\sqrt r/\sqrt{1+4r}$ 以下、局在射影からの反対井戸遷移は $4r/(1+4r)$ 以下、2モード漏れは $O(r)$ である。

<!-- theorem-start:proof -->
**証明（R140の傾斜保持節）**

2モード内の一般入力上界は射影の作用素ノルム評価、局在入力の強い上界はR140の遷移式から従う。B.5の漏れと保持残差を全変動距離の三角不等式で加える。上の尺度選択は高速切替と高モード抑制を同時に満たし、$r\to0$ で誤差を零へ送る。証明終。
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

R145で信号bath方向を準備し、R170で初期粒子位置枝を作る。衝突熱浴を切ってR140で任意軸を左右基底へ写し、分析器終了後の信号へR170を再適用する。R140の保持節で傾斜保持、R143の補題でW型有限コントラストを評価する。B.9の局所剪断で既存の $X$ を記録し、B.10の結果別正準交換で安全枝の条件付き共分散を作る。最後にtemplate方向へ再平衡化する。共通instrument誤差はR170、M47固有誤差は上の三角不等式、条件付き状態誤差は交換と局在裾の評価で抑えられる。証明終。
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

# 可逆tensor-lift、永続gate、末端instrumentの証明

> **位置づけ：** R176A/Bを有限正準Hamiltonian構成として証明し、R176Cの条件と誤差境界を分離する。


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

Hamiltonian流は拡大位相空間上で1対1である。出力 $Z_S$ だけを残してsource、$G_S$、work、clock履歴を捨てれば見かけ上の非可逆写像になるが、M52はそれらをbath内に保持する。逆順に $S_0^{-1}$ を作用させ、$\chi$ の符号を反転したpulseを通せば式(C.5)へ戻る。

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
**証明（R176A）**

式(C.4)--式(C.7)が各targetへの積の書込みを与え、式(C.8)、式(C.9)がそれを $Z_{jk}=a_jb_k$ とanti-modeへ正準的に分ける。全 $(j,k)$ に同じ規則を並列適用すれば $Z_S=a\otimes b$ となる。Hamiltonian流、$S_0$、pulseはすべて可逆であり、保持したsource、anti-register、work、clock履歴と逆順操作から逆写像を得る。有限性と誤差はcutoff構成および式(C.11)から従う。証明終。
<!-- theorem-end:proof -->

## 参照因子と反復lift

R176Aは未知の係数を外部で読み出すのでなく、入力modeとblank targetの局所Hamiltonian couplingで積を生成する。従ってcontrollerのprogramは入力値に依存しない。

第三因子 $c$ に対しては、最初の出力をsourceとして同じ乗算器へ入れ、

```math
 (a\otimes b)\otimes c
 =a\otimes b\otimes c
 \tag{C.12}
```

を得る。最初のliftに属するanti/workも捨てない。有限次元の参照因子 $R$ が存在しても、M52が $R$ に作用しなければ全写像は実正準流の恒等拡張となる。

ただし未知の一般状態を複製するとは主張しない。R176Aの入口契約は独立なQ1 portに与えられた積入力である。すでに非分離な入力は、前段と同じ永続register内でゲートを継続し、再liftしない。

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
**証明（R176B）**

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

とする。純粋rayの計算基底分布に対するdata-processing評価から、その全変動距離は $\varepsilon_{\rm ray}$ 以下で抑えられる。正則化は式(C.22)、SWAP、latch、shell、mixing、collection、lock、record、clockの有限誤差は合計 $\varepsilon_{170}^{\rm end}$ へ一度ずつ数える。無反応を $\varnothing$ として捨てずに含めれば本文R176Cの境界を得る。

<!-- theorem-start:proof -->
**証明（R176C）**

式(C.19)、式(C.20)が信号を壊さない容量latchを与え、式(C.21)、式(C.22)が正則化Born比とその誤差を与える。ray誤差、末端工程の合成誤差、無反応massに三角不等式を適用すると本文R176Cの境界を得る。R164、R170の有限作用殻と排他的固定を接続できるという仮定の下で成立する条件付き証明である。証明終。
<!-- theorem-end:proof -->

## 残る接続義務

R176Cを無条件の一体定理へ上げるには次を閉じる必要がある。

- canonical SWAP出口と容量pointer入口の共通safe set
- pointer容量からR164作用殻への有限Hamiltonian境界
- R161/R162の有限fiber混合が保つ枝対称性
- collection、lock、recordまでを含む単一clock schedule
- すべてのfailure cellと無反応を含む完全結果空間

これらは一般入力liftや中間coherent decoderの欠落ではない。R176AとR176Bにより、その二つはそれぞれ明示的liftと同じ永続register上のgate列へ置き換わった。

# M48完全Bell周期の証明

> **位置づけ：** R147、R153、R155のsetting-pre seed routing、paired-Hopf準備、切断面fiber、局所記録、Bell監査、条件付き因子化、弱開放帰還を証明する。


## 記号と有限設定族

A、Bの有限設定族を $\mathcal X,\mathcal Y$ とする。A設定作用素を

```math
\Sigma_x
=
\boldsymbol n_x\cdot\boldsymbol\sigma
```

とし、固有ベクトルを

```math
\Sigma_xu_{s,x}
=
s u_{s,x},
\qquad
s\in\{+1,-1\}
```

とする。位相規約は任意でよい。$\mathsf E$ は

```math
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

であり、

```math
\mathsf E\Sigma_x^*
=
-\Sigma_x\mathsf E
```

を満たす。従って

```math
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

は $\Sigma_x$ の固有値 $-s$ の固有ベクトルである。

W型有限配置グラフの埋込み $\Phi$ は $\Phi^\dagger\Phi=I_2$ とする。従って $z\neq0$ について

```math
\sum_i
\frac{
|\left(\Phi z\right)_i|^2
}{
z^\dagger z
}
=1.
```

## R153の準備節：setting-pre seedの安全盆routing

設定前の枝seedを $S_0\in\{+1,-1\}$ とし、

```math
P(S_0=+1)=P(S_0=-1)=\frac12
```

とする。M48内部の設定非依存registerを使う。pairing tensor $\mathsf E$ は固定装置定数である。許されたprovenance履歴 $H_{\rm prov}$ は同じ拡大状態に保存できるが、routing核、paired-Hopf流、局所分析器、記録核のいずれにも入力しない。

任意の $h_0\in[h_*,1)$ を固定し、$s=S_0$ と置く。各 $(s,x)$ について

```math
m_{s,x}
=
r_0
\left[
\sqrt{\frac{1+h_0}{2}}
u_{s,x}
+
\sqrt{\frac{1-h_0}{2}}
u_{-s,x}
\right]
```

と選べば

```math
\|m_{s,x}\|
=r_0,
\qquad
h_x(m_{s,x})
=s h_0.
```

有限設定族なので、設定registerと枝seedで選ぶ有限数のcontroller窓を事前配置できる。例えば各窓で

```math
\dot m
=
-\kappa_{\rm seed}
\left(
m-m_{s,x}
\right)
```

という採用開放整列を時間 $T_{\rm seed}$ だけ作用させれば、誤差は $e^{-\kappa_{\rm seed}T_{\rm seed}}$ の定数倍で減衰する。十分小さい誤差では $s h_x(m)\geq h_*$ を保てる。設定はこの前向き整列前に生成され、設定前測度へ $m_{s,x}$ を置いていない。

seed準備のbiasと欠損を $\varepsilon_{\rm seed}$、安全域外とrouting接続域の失敗質量を $\varepsilon_{\rm route}$ として無反応へ送る。

<!-- theorem-start:proof -->
**証明（R153のrouting節）**

内部等重みseedと明示seed $m_{s,x}$ が各設定の安全盆を与え、有限時間整列がそこへ指数的に近づける。全写像は設定前共通測度に設定依存分布を置かず、設定生成後の有限前向き操作である。履歴を全結果形成核の入力から外しているため、履歴で条件付けた結果法則は周辺結果法則と一致する。seed誤差と安全域外を無反応へ含めれば定理が従う。証明終。
<!-- theorem-end:proof -->

## R161/R170のM48局所特殊化

各翼の固定した単一試行bath座標 $z$ に対し、R164とR161へ

```math
m=2,
\qquad
\Psi=\Phi,
\qquad
v=z
```

を代入する。従って条件付き状態数は

```math
\frac{\Omega_i^\delta(z)}
{\sum_j\Omega_j^\delta(z)}
=
\pi_i^\delta(z),
```

R161の一様混合評価は

```math
D_{\rm TV}
\left(
\operatorname{Law}(X_T\mid z),
\pi^\delta(z)
\right)
\leq
C_\delta e^{-\lambda_\delta T}
```

となる。詳細釣合い、正値性、一意定常分布、有限衝突実現は共通R161/R162の証明を使い、ここで重複証明しない。

M48固有に必要なのは、paired-Hopfが作る有限設定族の安全ray集合上で $z\mapsto\pi^\delta(z)$ が射影距離に関して一様Lipschitzであることだけである。$\|z\|$ が零から離れ、有限次元のcompact集合に制限されるため、分母 $z^\dagger z$ は正の下界を持ち、微分は有界である。この定数を $L_{48}$ とすれば、bath方向誤差 $d_{\rm ray}$ は粒子位置目標分布へ高々 $L_{48}d_{\rm ray}$ だけ伝播する。

局所分析後は、共通R170を各翼の2枝グラフへ適用する。fresh局所作用殻、局所衝突セル、辺閉鎖、局所記録を使い、無反応を完全結果集合へ残す。この対応はM48固有の独立定理ではない。

## 強いfiberの基本性質

$\mu\in\mathcal F_W^\delta(c)$ とする。$z=e^{i\alpha}c$ かつ $\|c\|=1$ なので

```math
\frac{
E_\mu[zz^\dagger]
}{
E_\mu[z^\dagger z]
}
=
cc^\dagger.
```

また

```math
P_\mu(X=i)
=
E_\mu
\left[
\pi_i^\delta(z)
\right]
=
\pi_i^\delta(c).
```

従ってM47のrank-one bath条件を厳密に満たし、配置対角matchingを $\delta/(1+\delta)$ の誤差で満たす。さらに $X$ のbath条件付き分布を固定するため、周辺matchingだけより強い。

連続bath座標について、有限時間軌道は一般に目標rayそのものへは到達しない。従って切断面の完全状態測度を全変動距離で理想fiberと比較してはならない。第5.5節の $d_{\rm pair}$ は、同じ $\alpha$ をA側とB側へ反対符号で使うためpaired位相を保存し、動径誤差と2翼方向誤差を同時に測る。これに枝符号と2つの離散配置の不一致indicatorを加えて1で切った $d_\Omega$ は有界距離である。

このcostに関するWasserstein距離 $d_{\rm fib}$ では、bath対を同じ初期seedから理想吸引先へcoupleしたときの期待costをR147の有限時間ノルム上界で抑えられる。有限粒子位置分布は最大couplingを使えば不一致確率が全変動距離に等しい。従って連続方向誤差と離散配置誤差を同じfiber距離へ加えられる。

## R153の証明：切断面2翼fiber

R153の理想枝seedでは、各 $s$ が確率 $1/2$ で選ばれ、$s h_x(m_0)\geq h_*$ である。R147から、paired-Hopf時間 $T_{\rm PH}$ 後にある同じ位相 $\alpha$ が存在して

```math
\left|
z_A-e^{i\alpha}u_{s,x}
\right|
+
\left|
z_B-e^{-i\alpha}v_{s,x}
\right|
\leq
K_{48}e^{-\gamma_{48}T_{\rm PH}}
```

となる。seed biasと安全盆routingの有限誤差は、それぞれ $\varepsilon_{\rm seed}$ と $\varepsilon_{\rm route}$ へ入れる。

R161のM48特殊化の $\pi^\delta(z)$ は、$\|z\|$ が零から離れたcompact集合で $z$ の射影にLipschitzである。その定数をpaired-Hopf前因子へ吸収すれば、有限時間bath方向誤差から配置目標の誤差も $K_{48}e^{-\gamma_{48}T_{\rm PH}}$ の定数倍で抑えられる。

paired-Hopf終了時の $z_A,z_B$ をcontrollerで保持する。条件付き独立なA、B粒子位置bathを時間 $T_X$ だけ作用させると、R161のM48特殊化から各翼の条件付き粒子位置分布は対応する $\pi^\delta$ から $C_Xe^{-\lambda_X^\delta T_X}$ 以内になる。最大couplingを各翼へ使うと配置不一致確率は各全変動誤差の和以下である。さらに $\pi^\delta$ と理想 $w$ の全変動距離は各翼で $\delta/(1+\delta)$ 以下なので、理想fiber $\mathcal F_W^0$ への正則化costは2翼で $2\delta/(1+\delta)$ 以下である。

理想安全枝の非規格化交差モーメントは

```math
\begin{aligned}
M_{AB}
&=
\frac12
\sum_{s=\pm1}
u_{s,x}v_{s,x}^{\mathsf T}\\
&=
-\frac12\mathsf E
\end{aligned}
```

である。最後の等式は付録Iのspin-flip恒等式である。規格化ベクトル化射影はsinglet射影で、$x$ に依存しない。

枝分布を最大couplingし、bath対を同じseedとpaired位相でcoupleし、粒子位置を条件付き最大couplingする。枝、bath対、配置正則化、有限混合、切断の期待costを加えると、理想fiber混合 $\nu_x^0$ に対するR153の $d_{\rm fib}\leq\varepsilon_{\rm fib}$ を得る。$\varepsilon_{\rm seed}$ と $\varepsilon_{\rm route}$ に含めた同じ源誤差を別の項へ重複して入れない。

<!-- theorem-start:proof -->
**証明（R153）**

R153のrouting節が等重み安全枝、R147がpaired bath対の有限時間近接、R161のM48特殊化が各bath座標に条件付けた粒子位置分布の有限時間収束を与える。正則化誤差、積核誤差、切断誤差を上のcouplingで加えると、強い理想2翼fiberへのprojective fiber距離上界を得る。連続bath状態の全変動近接は使わない。交差モーメントは枝和恒等式からsinglet射影になる。証明終。
<!-- theorem-end:proof -->

## R155の局所応答節：R170の2翼合成

局所分析に入る作用殻は中央殻の使用済み微視的状態でなく、各翼のfresh registerに準備する。切断後半群と初期条件付き測度の積因子化は付録Jで証明し、ここではその有限偏差 $\varepsilon_{\rm prod}$ を局所instrument誤差とは別に加える。

切断後、A、Bの正準変数、粒子位置bath、noise seedを別々にする。共有する $s,\alpha$ は切断面に存在する共通過去であり、切断後の相互作用ではない。生成子の和に交差項がないため、その後の遷移核は完全状態に条件付けて

```math
K_{\rm post}^{xy}
=
K_A^x
\otimes
K_B^y
```

と因子化する。

A分析器を

```math
A_xu_{s,x}
=
|s\rangle
```

となるように選ぶ。B分析器について、局在出力 $|b\rangle$ の理想2モード重みは

```math
\begin{aligned}
p(b\mid s,x,y)
&=
\left|
\langle b|
A_yv_{s,x}
\rangle
\right|^2\\
&=
\left|
\langle b_y|
v_{s,x}
\rangle
\right|^2\\
&=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
\end{aligned}
```

最後の式は $v_{s,x}$ のBlochベクトルが $-s\boldsymbol n_x$ であることから従う。

各分析器終了後にbath方向を固定し、R161のM48特殊化の局所粒子位置bathを走らせる。従って記録直前の粒子位置分布は分析器後bath座標のW型対角から有限混合誤差内にある。R143の有限コントラスト補題により左右空間効果と理想2モード射影の差は $\eta_W$ 以下である。固定有限設定族のguardから離れたcompact安全域では、分析器、$w(z)$、記録効果の合成応答核は $d_\Omega$ に関して一様Lipschitzである。その定数を $L_{\rm fib}$ とすれば、切断面fiber誤差が結果分布へ与える寄与は $L_{\rm fib}\varepsilon_{\rm fib}$ 以下である。

粒子位置jump prefactorを零に切り替えた後、傾斜保持と局所記録剪断を作用させる。理想rate切断では記録窓中にjumpは起きない。有限切断残差、傾斜保持、分離面、記録cell幅をそれぞれ独立誤差へ入れる。

連続時間Markov鎖は、初期位置と各辺の局所jump clock列を固定すれば標本路がほとんど確実に一意である。clock列を完全状態のnoise seedに含めると、記録時刻の配置と結果は一意になる。無反応は正式な第3結果である。

<!-- theorem-start:proof -->
**証明（R155の局所応答節）**

局所2モード分析器が理想条件付き重みを与え、各翼のR170がそのbath座標に対応する粒子位置分布を回復して局所記録する。付録Jの因子化補題により生成子、作用殻、noiseは完全共通原因に条件付けてA、Bへ分かれる。従って2つのR170応答核は条件付きで積になる。spin-flip恒等式がB側の条件付き余弦応答を与える。共通容量、混合、固定、記録誤差は各 $\varepsilon_{170}^{A,B}$ へ1回だけ入れ、M48固有の分析器、W型コントラスト、fiber誤差と合成すれば定理が従う。証明終。
<!-- theorem-end:proof -->

## R155の証明：共同分布と有限誤差

完全共通原因 $\Lambda$ に条件付けると付録Jの補題により局所作用殻と応答核は積になる。$\Lambda$ を $\mu_{\rm cut}^x$ で積分することで既存の余弦共同分布を回復するため、条件付き積因子化はBell相関を消去しない。有限誤差の三角不等式には $\varepsilon_{\rm prod}$ を1回だけ加える。

理想枝では $P(s)=1/2$、$a=s$ なので

```math
\begin{aligned}
P(a,b\mid x,y)
&=
\sum_s
\frac12
\mathbf1_{a=s}
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)\\
&=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
\end{aligned}
```

和を取れば両周辺は $1/2$、符号積を取れば

```math
E(x,y)
=
-\boldsymbol n_x\cdot\boldsymbol n_y
```

である。平面標準設定を代入すればCHSH絶対値は $2\sqrt2$ になる。

前向き周期を有限個のMarkov核 $K_1,\ldots,K_N$、理想核を $K_1^0,\ldots,K_N^0$ とする。各段の一様全変動誤差が $\epsilon_j$ 以下なら逐次結合から

```math
D_{\rm TV}
\left(
\nu_0K_1\cdots K_N,
\nu_0K_1^0\cdots K_N^0
\right)
\leq
\sum_j\epsilon_j.
```

状態方向またはcontroller誤差は、対応する有限設定核のLipschitz定数を通して結果分布距離へ換算してから加える。特にR153のprojective fiber誤差は $L_{\rm fib}\varepsilon_{\rm fib}$ として加える。この和が第5章の $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ である。

周辺化は全変動距離を増やさない。A周辺が同じ理想周辺から各設定で $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以内なら、三角不等式により反対設定間の差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

各相関関数の被積分関数は、無反応を数値0として絶対値1以下である。従って1設定対の相関差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下、4項のCHSH差は $8\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

設定前測度は同じ $\nu_0$ だが、R153のseed routingとR147の吸引先は $x$ に依存する。異なる非順序軸 $x,x'$ では2つの固有ray集合が異なるため、理想切断面測度の支持も異なる。従って一般に

```math
\mu_{\rm cut}^x
\neq
\mu_{\rm cut}^{x'}.
```

一方、D.6節の切断後核は局所因子化する。測定設定独立性は成立せず、局所応答因子化と理想非信号性は成立する。

<!-- theorem-start:proof -->
**証明（R155）**

等重み枝とB条件付き重みを合成するとsinglet共同分布を得る。逐次核の全変動上界が前向き誤差和を与え、周辺化、三角不等式、有界観測量の期待値差から非信号周辺差とCHSH差を得る。$2\sqrt2-8\varepsilon_{\rm Bell}^{48,{\rm cyc}}>2$ を解けば定理の破れ条件になる。切断面支持の設定依存性と切断後核の因子化がBell前提監査を与える。証明終。
<!-- theorem-end:proof -->

## R155のfresh-cell帰還節

周期末偏差が

```math
\Delta_{n+1}
=
R_{\rm ret}\Delta_n
+
\eta_n,
\qquad
\|R_{\rm ret}\|
\leq
r_{\rm ret}
<1,
\qquad
\|\eta_n\|
\leq
\sigma_{\rm ret}
```

を満たすとする。反復すれば

```math
\|\Delta_n\|
\leq
r_{\rm ret}^n
\|\Delta_0\|
+
\sigma_{\rm ret}
\sum_{j=0}^{n-1}
r_{\rm ret}^j.
```

従って

```math
\limsup_{n\to\infty}
\|\Delta_n\|
\leq
\frac{
\sigma_{\rm ret}
}{
1-r_{\rm ret}
}.
```

controller残差が $\dot\Delta=-\lambda_{\rm ret}\Delta$ に従う時間窓では、有限時間残差は $C_{\rm ret}e^{-\lambda_{\rm ret}T_{\rm ret}}$ 以下である。これに有限SWAPとfresh seed幅を加えれば $\varepsilon_{\rm ret}$ の式を得る。

外部記録、使用済みsource、使用済みbathを逆実行しないため、全外部状態を同一点へ押しつぶさない。固定有限周期数なら必要な外部cell数も有限である。帰還は記録後に行うので、同じ周期の観測分布へ因果的に影響せず、次周期入口誤差へだけ渡す。

<!-- theorem-start:proof -->
**証明（R155のfresh-cell帰還節）**

縮小写像の幾何級数評価が一様周期末上界を与える。有限時間減衰、SWAP、fresh seedの誤差を加えると1周期帰還誤差を得る。外部記録と使用済み状態を保持するため情報の不可逆消去を有限閉鎖系内で行ったとは主張せず、固定有限周期またはcell流を持つ弱開放周期として定理が従う。証明終。
<!-- theorem-end:proof -->

## 任意精度の有限パラメータ選択

固定有限設定族と固定有限W型グラフについて、目標 $\epsilon>0$ を与える。まず十分小さい正則化 $\delta$ を選び、

```math
\frac{2\delta}{1+\delta}
<
\frac{\epsilon}{6}
```

とする。次に

```math
T_{\rm PH}
>
\frac1{\gamma_{48}}
\log
\frac{6K_{48}}{\epsilon},
```

```math
T_X
>
\frac1{\lambda_X^\delta}
\log
\frac{12C_X}{\epsilon}
```

を選ぶ。有限設定controller、W型深さ、記録幅、時計幅、reset時間を順に選び、残る有限個の誤差をそれぞれ $\epsilon$ の所定部分以下にする。従って形式的に時間を無限へ送るだけでなく、各 $\epsilon$ に対して有限時間・有限グラフ・有限設定controllerを選べる。

$\delta$ を小さくすると最小定常重みが小さくなり、$\lambda_X^\delta$ または最大rateが悪化し得る。W型を深くすると読出し誤差は下がるが、2モード操作時間が伸び得る。この構成は任意精度を同じ固定性能装置で得るとは主張しない。

## M52との境界

M48は、内部のsetting-pre等重みseed、paired-Hopf bath対、単一試行bath座標に条件付けたR161のM48特殊化、切断後の局所再平衡化から結果を作る。M52の1試行coherent経路和はM48の集団交差モーメントと同一でなく、現行M48はM52出力を受け取る一般状態receiverを持たない。Q2-1とQ2-2は独立に判定する。

## 証明範囲

本付録で厳密なのは、採用した有限次元paired-Hopf方程式、有限Markov生成子、有限設定controller、局所分析器、記録・帰還式の後段である。R161のM48特殊化の局所状態数には付録LのR164、rate形には第3章R161、固定bath座標の有限衝突熱浴には付録KのR162を利用できる。一方、作用容量fiber、seed整列drift、paired-Hopf pump、信号bath保持、2翼controller、fresh cell流までを同じ具体的電子回路、流体装置、振動子浴、有限閉鎖Hamiltonianへ統合した結果ではない。Bell統計の条件付き達成範囲は変更しない。

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

これらは固定入力時刻の分布を後刻に読む代替instrument接続である。現行Q3のQ3-4・Q3-5判定は付録NのM42/R174接続を使い、この節のR170を第2の終位置標本器として重ねない。どちらの経路も、障壁散乱の初回到達率、吸収率、幾何学的2開口、連続運転スクリーンを構成しない。

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

# Q3-3からQ3-5の詳細形と証明

> **位置づけ：** 第7章で一度だけ宣言したR123--R125について、低位束縛状態、純位相緩和、障壁値未満確率移動、最小2経路干渉の証明を与える。


## 記法と証明範囲

本付録では、第7章の定理文を再掲するのではなく、その簡潔な定理文に対応する完全な仮定と結論を示してから証明する。Q3-3では1次元井戸型・調和型ポテンシャルの有限個の低位状態と、有限個の環境正準対を読まない純位相緩和を構成する。Q3-4では3頂点鎖、Q3-5では2頂点再結合器を使う。後2者については第6.12--6.14節と付録NのM42/R174へ全変動距離で接続する。

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

R125は固定目標で定めた最小2経路干渉である。幾何学的2開口装置または連続運転スクリーンへの拡張ではない。後2結果の粒子接続はM42/R174を使い、M51、M37、初期作用殻、M42 bath、記録までの単一Hamiltonian統合を条件に残す。

# M47単一Hopf準備

> **位置づけ：** M47の単一Hopf準備R145を共通M51/R171の2モード特殊化として示す。閉鎖信号集団の第2モーメント輸送と2次元幾何は共通R135、W型占有振動はR140の特殊化として付録Fと本文第3章へ集約する。


## 目的と主張範囲

本付録は、対称なW型ポテンシャルの最低2モードsectorで、単一試行信号bath $Z\in\mathbb C^2$ を準備し、閉鎖正準流で回転させる部分だけを扱う。粒子位置のBorn型分布、有限熱化、局所記録はM50/R170が操作面ごとに構成する。信号bathの統計核から連続粒子位置rateを作る規則は使わない。

| 段階 | 内容 | 結果 |
|---|---|---|
| 開放準備 | M51による目標rayの位相円への有限時間吸引 | R171、R145 |
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

## R145：M51/R171のW型2モード特殊化

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

と置く。共通M51へ $m=2$、$G=D_W$、$c(t)=c_*(t)$ を代入すると、準備portが開いた区間の採用有効方程式は

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

<!-- theorem-start:theorem -->
**定理（R145：M51共通開放準備のM47特殊化）**

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
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$a$ と $p$ の方程式を割ると $p/a=(p_0/a_0)e^{-\kappa\tau}$ を得る。$y$ の線形方程式を積分すると上の厳密解が従い、$y\to1$、$p/a\to0$ となる。有界seed集合では係数を一様に抑えられる。外積の収束を平均し、分母が十分大きい $\tau$ で零から離れることを使えば第2モーメント上界を得る。証明終。
<!-- theorem-end:proof -->

この証明は付録MのR171証明を $m=2$ へ制限したものである。R145をM51とは別の準備機構として数えず、共通のpump、transverse sink、port切断のW型特殊化として扱う。

$a_0=0$ の直交超平面は不変である。その質量はseed失敗または無反応として残す。R145は雑音付き定常測度、位相拡散、粒子位置周辺、作用殻準備を導かない。

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

1. R145で単一試行信号bathの方向を準備する。
2. R135とR140で有限正準操作を行う。
3. 各操作面でR170を適用し、M50枝状態数から粒子位置を再平衡化して局所記録する。
4. R143でW型有限コントラスト、傾斜固定、結果別テンプレート交換を合成する。

従って全時刻の粒子位置--信号bath matching保存は不要である。本付録からは、採用Hopf方程式の具体的回路導出、作用容量結合、作用殻fiber内平衡化、信号保持反作用、周期総収支、独立同分布型結果列は従わない。

# M48設定依存paired-Hopf Bell準備

> **位置づけ：** 設定前共通基準測度から2翼bath対を準備する開放古典模型を定義し、R147の吸引率を主定理、直接singlet支持の不可能性と交差モーメントを補助命題として示す。局所応答と有限誤差Bell監査はR153、R155へ集約する。


## 目的、模型階層、主張範囲

paired-Hopf流の役割は、設定生成後の共有rayと共通原因を有限時間で準備することに限る。M48の等重みseedは内部の対称2枝作用殻から得る。paired-Hopf流自体をBorn重みの状態数起源とはしない。

本付録は、有限設定族について、設定前の共通基準測度から設定依存の2翼bath対を前向きに準備するM48を定義する。M48はM47を2翼へ拡張した**決定論的な開放古典有効模型**である。有限閉鎖Hamiltonian系への持ち上げは与えず、採用した開放方程式後の厳密計算と、その方程式自体のミクロ導出を区別する。

M51/R171は1つの有限担体rayをrank-one自己第2モーメントへ準備する共通模型である。M48が必要とするのは2翼間の交差モーメントと設定依存paired fiberであり、M51を2台並べただけでは得られない。M51は局所seed準備へ使えても、M48の交差統計を単一試行templateへ変換する機構としては使わない。

有限なA設定族とB設定族を

```math
\mathcal X
=
\{x_1,\ldots,x_M\},
\qquad
\mathcal Y
=
\{y_1,\ldots,y_N\}
```

とする。M48では設定生成後のA設定 $x$ が中央準備流へ入る。B設定 $y$ は中央結合の切断後にB局所分析器へだけ入る。従って、測定開始面の完全状態分布は一般に $x$ に依存するが、切断後の局所応答へ反対翼の設定を入れない。

本付録が厳密に示す範囲は次である。

1. 積bath標本の直接4次元共分散をsinglet階数1射影にできないという否定命題。
2. M48の採用開放方程式に対する2枝paired-Hopf吸引多様体と有限時間収束率R147。
3. 1つの設定前基準測度から、全ての有限A設定について同じsinglet型交差モーメント射影を準備するR153の補題。
4. 2翼の完全なM47 matchingと局所instrumentを仮定した後のR155理想応答補題。
5. 無反応を捨てない有限誤差、非信号性、CHSH値、Bell前提監査をR155へ渡す統計距離補題。

R147と補助命題が扱うのは2翼bath方向である。粒子位置 $X_A,X_B$ の周辺、条件付きbath分布、切断後局所分析、記録、周期末resetは、第5章と付録DのR153、R155がM48単独周期として閉じる。付録Iだけの結果を単一試行Bell周期またはQ2-1からの物理的受渡しと同一視しない。

## 積bath標本の直接共分散に対する否定命題

各試行の2翼bathベクトルを $z_A,z_B\in\mathbb C^2$ とする。直接テンソル標本

```math
Z
=
z_A\otimes z_B
\in
\mathbb C^4
```

の規格化共分散を

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}
{\mathbb E[Z^\dagger Z]}
```

とする。行優先の係数順序を使い、singlet代表を

```math
\beta_{\rm s}
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

と置く。

**否定命題（積bath標本からの直接singlet階数1共分散の不可能性）。**

$0<\mathbb E[Z^\dagger Z]<\infty$ とする。全ての標本が $Z=z_A\otimes z_B$ という積形なら、

```math
C_Z
=
\beta_{\rm s}\beta_{\rm s}^\dagger
```

とはならない。

<!-- theorem-start:proof -->
**証明**

等式が成り立つと仮定する。付録L.2の階数1共分散の支持補題を直接テンソル標本 $Z$ へ適用すると、$Z=\alpha\beta_{\rm s}$ がほとんど確実に成り立つ。一方、非零の積ベクトル $z_A\otimes z_B$ を $2\times2$ 係数行列へ戻すと階数1である。$\beta_{\rm s}$ の係数行列は

```math
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

で階数2なので、非零の積ベクトルはsinglet直線へ属さない。従って $\alpha=0$ がほとんど確実となり、$\mathbb E[Z^\dagger Z]>0$ と矛盾する。証明終。
<!-- theorem-end:proof -->

従ってM48では、$z_A\otimes z_B$ の標本共分散をsingletへ直接吸引する構成を採らない。2翼bath間の交差モーメントを先に作り、その規格化ベクトルが定める階数1射影をsinglet型統計状態とする。

## 交差モーメントと階数1射影

反対称行列を

```math
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathsf E^{\mathsf T}
=
-\mathsf E,
\qquad
\mathsf E^2
=
-I_2
```

とする。有限時間の安全事象を $G_x$ とし、無規格化交差モーメントを

```math
M_{AB}^{G}
=
\mathbb E
\left[
\mathbf1_{G_x}
z_Az_B^{\mathsf T}
\right]
```

と定める。$M_{AB}^{G}\neq0$ のとき

```math
B_{AB}
=
\frac{M_{AB}^{G}}
{\left\|M_{AB}^{G}\right\|_{\rm F}}
```

とする。付録Jとの共通規約として行優先ベクトル化を

```math
\operatorname{vec}_{\rm row}
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
a&b&c&d
\end{pmatrix}^{\mathsf T}
```

と定め、

```math
\beta_{AB}
=
\operatorname{vec}_{\rm row}(B_{AB}),
\qquad
C_{AB}^{\times}
=
\beta_{AB}\beta_{AB}^\dagger
```

をM48の**交差モーメント射影**と呼ぶ。階数1なのは $C_{AB}^{\times}$ であり、$2\times2$ 行列 $B_{AB}$ 自体ではない。また、$C_{AB}^{\times}$ はI.2で退けた直接標本共分散 $C_Z$ ではない。

列優先記法との関係は、中央2成分を交換する $P_{23}$ により

```math
\operatorname{vec}_{\rm col}
\left(B\right)
=P_{23}\operatorname{vec}_{\rm row}\left(B\right)
```

である。M48で得る代表が $B_{AB}=-\mathsf E/\sqrt2$ なら

```math
\operatorname{vec}_{\rm row}
\left(
-\frac{\mathsf E}{\sqrt2}
\right)
=
-\beta_{\rm s}.
```

このrow-major代表はglobal phaseを除いて同じ階数1射影

```math
C_{AB}^{\times}
=
\beta_{\rm s}\beta_{\rm s}^\dagger
```

を与える。singletでは $P_{23}$ がglobal signに退化するが、一般行列では退化しないため、row-majorとcolumn-majorを暗黙に交換しない。

## 設定前共通基準測度と試行の順序

設定前開始面の状態を

```math
\Gamma_0
=
\left(
\xi_A,\xi_B,
m_0,d_0,
X_A,X_B,
\zeta,R
\right)
```

とする。$\xi_A,\xi_B$ は設定生成角、$m_0,d_0\in\mathbb C^2$ は中央paired-Hopf portの初期bright変数とdark変数、$X_A,X_B$ は2翼の粒子位置、$\zeta$ はpump、時計、切断器、浴、履歴の補助変数、$R$ は空の外部記録である。基準測度を

```math
\nu_0(d\Gamma_0)
=
\frac{d\xi_A\,d\xi_B}{(2\pi)^2}
\otimes
\overline\nu_0(d\overline\Gamma_0),
```

```math
\overline\Gamma_0
=
\left(
m_0,d_0,X_A,X_B,\zeta,R
\right),
```

```math
\overline\nu_0(d\overline\Gamma_0)
=
\nu_m(dm_0)
\otimes
\nu_d(dd_0)
\otimes
\nu_{X\zeta R}
```

とする。有限設定を作る窓写像を $S_A(\xi_A)\in\mathcal X$、$S_B(\xi_B)\in\mathcal Y$ とする。積構造により、任意の非零設定窓について

```math
\nu_0
\left(
d\overline\Gamma_0
\mid
S_A(\xi_A)=x,
S_B(\xi_B)=y
\right)
=
\overline\nu_0(d\overline\Gamma_0).
```

従って設定前の物理seed測度 $\overline\nu_0$ は、実際に生成される設定値 $x,y$ に依存しない。

$m_0=r_0q_0$ と分け、方向 $q_0$ は $\mathbb C^2$ の単位球面上で共通位相を除いてHaar分布、動径とdark変数は

```math
0<r_-
\leq
r_0
\leq
r_+<\infty,
\qquad
\|d_0\|
\leq
d_+<\infty
```

を満たすとする。設定窓が $\xi_A,\xi_B$ から $x\in\mathcal X$、$y\in\mathcal Y$ を作った後、A設定 $x$ に対応する流を $\Phi_x^\tau$ と書く。明示的な設定レジスターを除いた準備状態を $\Lambda$ とし、その測度を

```math
\mu_x^\tau
=
\left(
\Phi_x^\tau
\right)_\#\overline\nu_0
```

と定める。測定開始面では

```math
\mu_{\rm meas}
\left(
d\Lambda
\mid
x,y
\right)
=
\mu_x^{\tau_{\rm p}}(d\Lambda)
```

となり、一般に $\mu_x^{\tau_{\rm p}}\neq\mu_{x'}^{\tau_{\rm p}}$ である。目的分布を設定依存初期測度へ直接書いたのではなく、同じ物理seed測度 $\overline\nu_0$ を設定生成後の明示流で押し出している。一方、B設定 $y$ はこの中央準備流へ入らない。

## bright変数とdark変数

中央portの2翼bath変数を $z_A,z_B\in\mathbb C^2$ とし、

```math
m
=
\frac{z_A-\mathsf E\overline{z_B}}{2},
\qquad
d
=
\frac{z_A+\mathsf E\overline{z_B}}{2}
```

と定める。逆変換は

```math
z_A
=
m+d,
\qquad
z_B
=
\mathsf E\overline{m-d}
```

である。$d=0$ なら2翼は位相共役した反対称対

```math
z_B
=
\mathsf E\overline{z_A}
```

になる。M48は設定方向へ $m$ を吸引し、$d$ を減衰させることでpaired fiberを準備する。

## M48のpaired-Hopf開放方程式

各設定 $x$ に単位Blochベクトル $n_x\in\mathbb R^3$ を対応させ、Pauli行列を $\boldsymbol\sigma$ と書く。設定作用素と方向変数を

```math
\Sigma_x
=
n_x\cdot\boldsymbol\sigma,
\qquad
\Sigma_x^2
=
I_2,
```

```math
h_x(m)
=
\frac{m^\dagger\Sigma_xm}{m^\dagger m}
```

とする。準備の有効時間を

```math
\tau(t)
=
\int_{t_{\rm in}}^t
\lambda_{\rm prep}(s)\,\mathrm{d}s
```

と定める。$m\neq0$ に対する決定論的開放流を

```math
\frac{dm}{d\tau}
=
F_x(m)
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

とする。$g,\kappa,\kappa_{\rm p}>0$ である。元の2翼変数では

```math
\dot z_A
=
\lambda_{\rm prep}(t)
\left[
F_x(m)-\kappa_{\rm p}d
\right],
```

```math
\dot z_B
=
\lambda_{\rm prep}(t)
\mathsf E
\overline{
F_x(m)+\kappa_{\rm p}d
}
```

である。$\lambda_{\rm prep}>0$ の準備窓が終わると中央portを切断する。以後は各翼のM47分析器、傾斜固定、局所記録だけを作動させる。

各項の物理的役割は次の通りである。

| 項 | 役割 | 外部収支 |
|---|---|---|
| $g(1-m^\dagger m)m$ | bright動径への能動供給と飽和 | pumpから作用を供給し、単位動径を越えるとlimiterへ戻す |
| $\kappa h_x(\Sigma_x-h_xI_2)m$ | 設定依存の異方的整列 | $m$ のノルムを変えず、設定controllerから方向情報を受け取る |
| $-\kappa_{\rm p}d$ | paired fiber外のdark成分の散逸 | dark作用をsinkへ排出する |
| $\lambda_{\rm prep}$ | 準備portの接続と切断 | 切替仕事、残留相関、時計情報を外部帳簿へ渡す |

局所的な作用様量

```math
N_{\rm pair}
=
m^\dagger m+d^\dagger d
```

は

```math
\frac{dN_{\rm pair}}{d\tau}
=
2g(1-m^\dagger m)m^\dagger m
-
2\kappa_{\rm p}d^\dagger d
```

を満たす。異方的整列項は $N_{\rm pair}$ を直接変えないが、設定controllerとの仕事と情報流を零と意味しない。位相体積の収縮とdark散逸に伴うエントロピーは外部sinkへ出る。M48はこの局所帳簿を明示するが、pump、controller、sink、切断器まで含む総エネルギー・総エントロピー収支を閉じていない。

開放模型としての8項目監査を次にまとめる。

| 監査項目 | M48で明示する内容と限界 |
|---|---|
| 状態、方程式、初期条件 | 状態は $(m,d)$、発展はJ.6節の2式、seedは $r_-\leq\|m_0\|\leq r_+$、$\|d_0\|\leq d_+$、有限時間一様評価では $|h_x(m_0)|\geq h_*$ とする |
| 雑音規約 | 確率微分項は零であり、Itô規約、Stratonovich規約、白色雑音極限を使わない。雑音付き定常測度へ読み替えない |
| drift、散逸、駆動 | bright pumpと飽和、設定依存整列、dark sink、外部 $\lambda_{\rm prep}$ による接続と切断を上の表の通り分離する |
| 熱、仕事、エントロピー、情報 | $N_{\rm pair}$ の局所流だけを計算する。bath温度と熱流 $\dot Q$ は定義せず、pump仕事、controller仕事、切替仕事、sinkのエントロピー生成、設定情報流の総収支は未閉鎖とする |
| 環境消去と時間尺度 | pump、controller、sink、切断器を外部portとして採用し、環境自由度の消去、Markov近似、時間尺度分離は導出しない。$\tau$ は有限準備窓の有効時間である |
| 測度、準備、試行 | J.4節の $\nu_0$ と共通物理seed周辺 $\overline\nu_0$、設定窓、押出し測度 $\mu_x^\tau$、J.12節の無反応を含む完全結果集合で試行を数える |
| 検証 | R147、R153、R155で使う解析恒等式と有限誤差式を示し、`tools/verify_m48_paired_hopf.py` でbright/dark変換、吸引率、交差モーメント、余弦則、CHSH誤差を回帰検算する |
| 各項の由来 | 全drift項は現象論的な採用開放方程式である。具体的な回路、流体、振動子浴、有限閉鎖Hamiltonian系から導出した項はない |

この改訂では白色雑音を加えない。雑音を加えると $h_x=0$ の盆境界を横切る枝遷移と定常測度を別に解析する必要がある。決定論的主定理を雑音付き定理へ読み替えない。

## R147：吸引多様体と有限時間収束率

$\Sigma_xu_{s,x}=s u_{s,x}$、$s\in\{+1,-1\}$ となる規格化固有ベクトルを選ぶ。M48の吸引集合を

```math
\mathcal A_x
=
\bigcup_{s=\pm1}
\left\{
\left(
e^{i\alpha}u_{s,x},
e^{-i\alpha}\mathsf E\overline{u_{s,x}}
\right):
\alpha\in[0,2\pi)
\right\}
```

とする。

<!-- theorem-start:theorem -->
**定理（R147：M48の2枝paired-Hopf吸引多様体と有限時間率）**

$m_0\neq0$、$h_0=h_x(m_0)\neq0$ とし、$s=\operatorname{sign}h_0$ とする。このときM48流は $\mathcal A_x$ の $s$ 枝へ収束する。具体的に

```math
\|m(\tau)\|^2
=
\frac{1}
{1+
\left(
\|m_0\|^{-2}-1
\right)e^{-2g\tau}},
```

```math
h_x(m(\tau))^2
=
\frac{1}
{1+
\left(
h_0^{-2}-1
\right)e^{-4\kappa\tau}},
```

```math
d(\tau)
=
e^{-\kappa_{\rm p}\tau}d_0
```

である。射影間のtrace距離を

```math
D_{\rm tr}(P,Q)
=
\frac12\|P-Q\|_1
```

とする。$|h_0|\geq h_*>0$ なら

```math
D_{\rm tr}
\left(
\frac{m(\tau)m(\tau)^\dagger}
{m(\tau)^\dagger m(\tau)},
u_{s,x}u_{s,x}^\dagger
\right)
\leq
\frac{e^{-2\kappa\tau}}
{\sqrt2h_*}.
```

さらに $r_-\leq\|m_0\|\leq r_+$、$\|d_0\|\leq d_+$ の有界seed集合で

```math
C_r
=
\max
\left\{
r_-^{-2}-1,
r_+^2-1,
0
\right\},
\qquad
\overline r
=
\max\{1,r_+\},
```

```math
K_{48}
=
\sqrt2
\left(
C_r
+
\frac{\overline r}{h_*}
+
d_+
\right)
```

と置けば

$\operatorname{dist}$ を $\mathbb C^2\times\mathbb C^2$ の標準積ノルムが定める距離として

```math
\operatorname{dist}
\left(
(z_A(\tau),z_B(\tau)),
\mathcal A_x
\right)
\leq
K_{48}
e^{-\gamma_{48}\tau},
```

```math
\gamma_{48}
=
\min
\left\{
2g,2\kappa,\kappa_{\rm p}
\right\}
```

を得る。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$r^2=m^\dagger m$ とする。$m^\dagger(\Sigma_x-h_xI_2)m=0$ なので

```math
\frac{dr^2}{d\tau}
=
2g(1-r^2)r^2.
```

これを解くと第1式を得る。$\Sigma_x^2=I_2$ を使うと

```math
\frac{dh_x}{d\tau}
=
2\kappa h_x
\left(
1-h_x^2
\right).
```

従って $h_x$ の符号は保存され、$h_x^2$ の方程式を解けば第2式を得る。$d$ の式は線形なので第3式が従う。

$P_m=mm^\dagger/(m^\dagger m)$ とする。2次元純粋射影のtrace距離は

```math
D_{\rm tr}(P_m,P_{s,x})
=
\sqrt{
\frac{1-|h_x|}{2}
}
\leq
\sqrt{
\frac{1-h_x^2}{2}
}.
```

$|h_0|\geq h_*$ と第2式から射影上界を得る。位相 $\alpha$ を最適に選ぶと、規格化brightベクトルの固有ベクトルからの距離は $\sqrt2D_{\rm tr}$ 以下である。また、動径の厳密解から

```math
\left|
\|m(\tau)\|-1
\right|
\leq
C_re^{-2g\tau}
```

であり、$\|m(\tau)\|\leq\overline r$ である。従って

```math
\min_\alpha
\left\|
m(\tau)-e^{i\alpha}u_{s,x}
\right\|
\leq
C_re^{-2g\tau}
+
\frac{\overline r}{h_*}e^{-2\kappa\tau}.
```

bright/dark逆変換に対して標準積ノルムを使うと、その距離の2乗はbright誤差とdark誤差の2倍の和である。$\|d(\tau)\|\leq d_+e^{-\kappa_{\rm p}\tau}$ を合わせれば、表示した $K_{48}$ と $\gamma_{48}$ が従う。証明終。
<!-- theorem-end:proof -->

$h_x=0$ は不変な盆境界であり、そこでは異方的整列項が零になる。この集合はHaar方向測度では零測度だが、有限時間の一様収束定数は $h_0\to0$ で発散する。従って有限時間装置では

```math
G_x
=
\left\{
|h_x(m_0)|\geq h_*
\right\}
```

を安全事象とし、補集合を無反応として記録する。Haar方向では $h_x$ は $[-1,1]$ 上の一様分布なので

```math
P(G_x^c)
=
h_*,
```

```math
P(h_x\geq h_*)
=
P(h_x\leq-h_*)
=
\frac{1-h_*}{2}.
```

無反応試行を除いて分母を付け替えない。

## 交差モーメントの有限時間上界

$P_{s,x}=u_{s,x}u_{s,x}^\dagger$ とする。bright/dark逆変換から各安全標本について

```math
z_Az_B^{\mathsf T}
=
-(m+d)(m^\dagger-d^\dagger)\mathsf E
```

である。従って

```math
\left\|
z_Az_B^{\mathsf T}
+
P_{s,x}\mathsf E
\right\|_{\rm F}
\leq
\left\|
mm^\dagger-P_{s,x}
\right\|_{\rm F}
+
2\|m\|\|d\|
+
\|d\|^2.
```

R147で定めた $C_r$、$\overline r$ を使うと

```math
\left\|
z_Az_B^{\mathsf T}
+
P_{s,x}\mathsf E
\right\|_{\rm F}
\leq
K_\times e^{-\gamma_{48}\tau},
```

```math
K_\times
=
C_r
+
h_*^{-1}
+
2\overline r d_+
+
d_+^2
```

を選べる。これは設定族の要素数に依存しない。依存するのは有限設定族で共通に選んだseed境界、盆余裕、3つの減衰率だけである。

## R153の交差モーメント補題

吸引集合上の安全標本は

```math
z_A
=
e^{i\alpha}u_{s,x},
\qquad
z_B
=
e^{-i\alpha}
\mathsf E\overline{u_{s,x}}
```

となる。位相は積 $z_Az_B^{\mathsf T}$ で相殺する。また

```math
z_Az_B^{\mathsf T}
=
-P_{s,x}\mathsf E.
```

**R153の交差モーメント補題。**

J.4節の設定前基準測度を取り、$q_0$ をHaar方向、有限設定族を $\mathcal X$ とする。各 $x\in\mathcal X$ について同じ物理seed周辺 $\overline\nu_0$ をM48流で押し出すと、安全2枝は等重みでR147の吸引集合へ収束し、

```math
M_{AB}^{G}(\infty\mid x)
=
-\frac{1-h_*}{2}\mathsf E
```

を満たす。従って

```math
B_{AB}(\infty\mid x)
=
-\frac{\mathsf E}{\sqrt2},
\qquad
C_{AB}^{\times}(\infty\mid x)
=
\beta_{\rm s}\beta_{\rm s}^\dagger
```

であり、右辺は $x$ に依存しない。

有限時間で交差モーメントのずれを

```math
\delta_\times(\tau)
=
\left\|
M_{AB}^{G}(\tau\mid x)
+
\frac{1-h_*}{2}\mathsf E
\right\|_{\rm F}
```

とする。枝重みの非対称、切断残差を $\varepsilon_{\rm sym}$、$\varepsilon_{\rm cut}$ とすれば

```math
\delta_\times(\tau)
\leq
(1-h_*)K_\times e^{-\gamma_{48}\tau}
+
\varepsilon_{\rm sym}
+
\varepsilon_{\rm cut}.
```

$\delta_\times<(1-h_*)/(2\sqrt2)$ なら

```math
\left\|
B_{AB}(\tau\mid x)
+
\frac{\mathsf E}{\sqrt2}
\right\|_{\rm F}
\leq
\frac{2\sqrt2}{1-h_*}
\delta_\times(\tau).
```

<!-- theorem-start:proof -->
**証明**

Haar方向では安全な正負2枝の質量がそれぞれ $(1-h_*)/2$ である。$P_{+,x}+P_{-,x}=I_2$ なので

```math
M_{AB}^{G}(\infty\mid x)
=
-\frac{1-h_*}{2}
\left(
P_{+,x}+P_{-,x}
\right)\mathsf E
=
-\frac{1-h_*}{2}\mathsf E.
```

J.8節の標本ごとの上界を安全集合で平均すると有限時間式を得る。非零行列の規格化写像 $M\mapsto M/\|M\|_{\rm F}$ の局所Lipschitz上界を使えば最後の式が従う。証明終。
<!-- theorem-end:proof -->

この補題が示すのはbath対の交差モーメント射影である。各試行の2値結果、粒子位置頻度、局所記録をこの集団量から直接読んではならない。

## 完全matching fiberと証明済み射影の区別

枝 $s$、設定 $x$ に対する完全matching fiberを $\mathfrak M_{s,x}$ と書く。その最低条件は次の5つである。

1. bath対 $(z_A,z_B)$ がR147の $s$ 枝へ入る。
2. A粒子位置 $X_A$ の周辺が $u_{s,x}$ のW型空間核と一致する。
3. B粒子位置 $X_B$ の周辺が $\mathsf E\overline{u_{s,x}}$ のW型空間核と一致する。
4. 2翼の条件付きbath分布が、それぞれの未来のM47流と整合する。
5. 中央結合の切断後、局所分析器、傾斜固定、局所記録まで同じmatching関係を有限誤差で保存する。

R147と交差モーメント補題が単独で証明するのはbath射影

```math
\pi_z\mu_x^\tau
\longrightarrow
\pi_z\mathfrak M_x
```

だけであり、

```math
\mu_x^\tau
\longrightarrow
\mathfrak M_x
```

という完全共同測度の吸引ではない。交差モーメントだけから単一試行頻度を作った扱いにすると、集団余弦重みだけを持ち単一試行周期を欠いた旧M30と同じ問題へ戻る。次節の理想応答補題はこの完全matchingと局所instrumentを抽象仮定にする。第5章のR153、R155は、固定singlet型Bell装置について、単一試行bath座標に条件付けた局所粒子位置生成子、切断面の強いmatching fiber、切断後局所分析、再matching、固定、記録を構成し、この抽象仮定を有限誤差で充足する。Q2-1のM52経路状態をM48の交差モーメントへ置換してはならない。

## R155の理想局所応答補題

spin-flip恒等式

```math
\mathsf E\overline{\Sigma_x}
=
-\Sigma_x\mathsf E
```

により、$u_{s,x}$ が $\Sigma_x$ の固有値 $s$ を持つなら

```math
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

は反対向きBlochベクトル $-s n_x$ を持つ。

**R155の理想局所応答補題。**

R153の交差モーメント補題の各枝についてJ.10節の完全matchingが成立し、A局所分析器が $u_{s,x}$ を結果 $A=s$ の安全井戸へ写し、B局所分析器が $v_{s,x}$ を設定 $y$ で測ると仮定する。このとき理想安全枝では

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,n_x\cdot n_y
\right).
```

2枝が等重みなら

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left(
1-ab\,n_x\cdot n_y
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
-n_x\cdot n_y.
```

平面設定では

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left[
1-ab\cos(x-y)
\right].
```

<!-- theorem-start:proof -->
**証明**

$v_{s,x}$ のBlochベクトルは $-sn_x$ なので、B設定 $n_y$ の結果 $b$ の2値効果を作用させると条件付き確率式を得る。$P(s\mid x)=1/2$ を掛けて $s=a$ と置けば共同分布が従う。周辺と相関は2値和を取ればよい。証明終。
<!-- theorem-end:proof -->

この補題はJ.10節の完全matchingを仮定した後の厳密結果である。R147と交差モーメント補題だけから結果頻度が出たとは分類しない。第5章のR153と局所応答構成を代入すると、固定Bell装置について仮定が充足され、R155の完全周期結果になる。

## 無反応を含む有限時間分布

有限時間の一様率を使うときは $G_x^c$ を無反応 $\varnothing$ として残す。理想安全枝分布を $p_{xy}^{\rm safe}$ とすると、盆境界だけを有限化した完全結果分布は

```math
p_{xy}^{(h_*)}(a,b)
=
(1-h_*)p_{xy}^{\rm safe}(a,b),
```

```math
p_{xy}^{(h_*)}(\varnothing)
=
h_*.
```

無反応を持たない理想余弦分布を同じ拡大結果集合へ埋め込めば

```math
D_{\rm TV}
\left(
p_{xy}^{(h_*)},
p_{xy}^{\rm ideal}
\right)
=
h_*.
```

従って $h_*$ は事後選別率でなく、完全結果集合に残す有限時間誤差 $\varepsilon_{\rm basin}$ である。$h_*\downarrow0$ で無反応率は下がるが、R147の一様収束定数は増える。これは有限準備時間との交換である。R153のsetting-pre等重みseedを使う完全周期では、有限setting routingが最初から $|h_x|\geq h_*$ の安全盆へ入れる。そこではHaar盆境界質量 $h_*$ を固有の無反応率として加えず、seed biasとrouting失敗を $\varepsilon_{\rm seed}+\varepsilon_{\rm route}$ へ入れる。

## R155で使う統計距離補題

M48経路の1設定対当たりの前向き全変動誤差を

```math
\begin{aligned}
\varepsilon_{\rm Bell}^{48}
\leq{}&
\delta_{\rm set}
+
\varepsilon_{\rm seed}
+
\varepsilon_{\rm route}
+
\varepsilon_{\rm PH}
+
\varepsilon_{\rm basin}
+
\varepsilon_{\rm fib}^{A}
+
\varepsilon_{\rm fib}^{B}\\
&+
\varepsilon_{\rm inst}^{A}
+
\varepsilon_{\rm inst}^{B}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}
\end{aligned}
```

と分ける。$\delta_{\rm set}$ は有限設定生成、$\varepsilon_{\rm seed}$ は等重みseed、$\varepsilon_{\rm route}$ は安全盆routing、$\varepsilon_{\rm PH}$ はR147と交差モーメント補題の有限時間吸引、$\varepsilon_{\rm basin}=h_*$ は無反応盆、$\varepsilon_{\rm fib}^{A,B}$ は完全matching、$\varepsilon_{\rm inst}^{A,B}$ は局所分析器・傾斜固定、$\varepsilon_{\rm cut}$ は中央切断、$\varepsilon_{\rm rec}$ は局所記録、$\varepsilon_{\rm clk}$ は時計窓である。帰還誤差は次周期へ渡し、同じ周期の観測済み分布へ遡って加えない。R153では連続bath方向を完全状態全変動距離でなくprojective fiber距離で評価し、R155の一様Lipschitz定数を通して結果全変動距離へ移す。

**統計距離補題。**

各設定対の完全結果分布がR155の理想分布から全変動距離 $\varepsilon_{\rm Bell}^{48}$ 以下であるとする。このとき反対側設定を変えた一側周辺の差は $2\varepsilon_{\rm Bell}^{48}$ 以下である。無反応を数値0として相関を計算したCHSH値 $S_{48}$ は

```math
\left|
|S_{48}|-2\sqrt2
\right|
\leq
8\varepsilon_{\rm Bell}^{48}.
```

従って

```math
\varepsilon_{\rm Bell}^{48}
<
\frac{\sqrt2-1}{4}
```

なら有限誤差下でもCHSH不等式の破れが残る。
理想分布の一側周辺は反対側設定に依存しない。全変動距離の縮約性を各周辺へ使い、2つの設定分布を三角不等式で比較すると $2\varepsilon_{\rm Bell}^{48}$ を得る。絶対値1以下の相関量の期待値差は全変動距離の2倍以下なので、4相関のCHSH差は $8\varepsilon_{\rm Bell}^{48}$ 以下である。

Bell前提の監査は次の通りである。

| 監査項目 | M48経路 |
|---|---|
| 局所性 | 中央切断後は $P(A,B\mid\Lambda,x,y)=P_A(A\mid\Lambda_A,x)P_B(B\mid\Lambda_B,y)$ と因子化し、反対翼設定を局所方程式へ入れない |
| 測定設定独立性 | 測定開始面で $\mu_{\rm meas}(d\Lambda\mid x,y)=\mu_x(d\Lambda)$ なので成立しない。依存は設定前共通測度からのM48前向き流で生じる |
| 結果の一意性 | 安全枝では局所粒子位置の井戸記録が1結果を与え、盆境界と有限装置遷移域は無反応へ送る |
| 事後選別 | 無反応を完全結果集合へ残し、採用試行だけで再規格化しない |
| 非信号性 | 理想周辺は $1/2$、有限誤差差は上の統計距離補題の上界を持つ |
| 試行測度 | 設定前基準測度 $\nu_0$、設定生成、M48押出し、切断、局所記録の順で定め、目的共同分布を初期測度へ直接置かない |

M48はBellの定理を否定しない。CHSH破れを可能にする位置は測定設定独立性であり、切断後の局所因子化とは別である。また、A設定が中央準備へ入るため、標準的な2側空間分離Bell実験を再現したとは主張しない。この補題の抽象誤差項は、第5章のR155証明内でseed routing、強いmatching、局所記録を含む $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ へ具体化する。

## M52との状態概念の境界

R153の $B_{AB}=-\mathsf E/\sqrt2$ はM48試行集団の交差モーメントである。M52の $D_\Gamma=\sum_r\gamma_ra_rb_r^{\mathsf T}$ は一つの試行内に共存するcoherent経路の派生和であり、平均の位置が異なる。両者の行列表現が一致しても物理的受渡しは従わない。

M48は内部の設定前等重みseedから開始する。M52出力を一般状態Bell測定へ接続するreceiverは現行模型に含めず、交差モーメントからM52経路を再準備する操作も採用しない。

## M48単独周期で閉じた項目と残る非主張

setting-pre等重みseed、安全盆routing、2翼強matching、切断後局所分析、2翼記録、周期末帰還は、第5章と付録DのR153、R155で固定singlet型・固定有限設定族について閉じる。各翼の固定単一試行bath座標に対するR161のM48特殊化の局所状態数には、付録LのR164を利用できる。

現稿で主張しない事項は次である。

1. M48開放方程式の具体的回路、流体、振動子浴からの導出。
2. M48の有限閉鎖Hamiltonian系への持ち上げ。
3. R164の作用容量fiberとR162の衝突熱浴を、paired-Hopf pump、seed routing、2翼controller、信号bath保持へ同じ具体的回路または有限閉鎖Hamiltonianとして統合したこと。
4. 連続時間の全区間で強いmatching fiberが不変であること。
5. 任意のQ2-1出力を一般状態M48測定へ接続すること。
6. 準備後にA設定を自由変更する介入分布。
7. 空間的に隔たった2設定選択、有限伝播円錐、標準Bell実験。
8. 一般測定族を拘束するTsirelson原理。
9. 独立同分布型有限標本揺らぎ。
10. Q2-4の多項式外部制御による量子出力サンプリング。

# Q2永続共同bathの合成契約

> **位置づけ：** R176Aの反復tensor-lift、R176Bの同一8mode状態bath、R176Cの末端instrument、およびR177のGHZ--T--逆演算証人を統合する。


## 目的と適用範囲

本付録はQ2-1とQ2-3を同じ機構で動かす契約を定める。三つのQ1型port $A,B,C$ から、R176Aをgate列の前に2回作用させて

```math
 Z_{ABC}=a\otimes b\otimes c\in\mathbb C^8
 \tag{J.1}
```

を作る。その後はR176Bにより同じ物理的状態bathへA--B、B--C、局所gate、逆gateを順に作用させ、R176Cにより末端だけを読む。

ここで「同じ機構」とは、mode数が常に4であることではない。固定された有限入力数に対応する受動的な内部modeをbathに任せ、外部controllerはport、gate種、対象、作用窓だけを指定することを意味する。

## 1試行状態と集団momentの分離

$Z_{ABC}$ は同じ試行の実正準座標から得る8成分信号である。一方、M48で使う

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]
 \tag{J.2}
```

は試行集団の交差momentである。式(J.2)を推定して $Z_{ABC}$ へ戻す操作は再準備であり、Q2-1またはQ2-3の状態受渡しには使わない。M48のBell周期は独立な固定目標Q2-2に属し、setting-pre等重みseedから始まる。

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

内部に8つの複素modeがあることは、それ自体では指数長の外部registerを意味しない。Q2-3は入力数が固定された有限benchmarkである。一般の $N$ 入力でmode数が $2^N$ になるM52反復の一様性はここでは主張しない。Q2-4は別模型M53で扱う。

## 二つのgate zone

R176Bの生成子を

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

R176Aによる3入力lift、R176BによるA--B、B--C、局所 $T$、逆gate、およびR176Cによる末端instrumentが同じ永続状態bath上で合成されるとする。観測coherent分布と式(J.9)の距離を $\varepsilon_{\rm coh}$、任意の完全dephase模型の観測分布と式(J.10)の距離を $\varepsilon_{\rm mix}$ とする。このとき

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

R176Cを $L=8$ に特殊化する。実際の末端信号 $v=Z_{\rm out}(\omega)$ をcanonical SWAPでholdし、

```math
 \pi_{abc}^{\delta}(v)
 =\frac{|v_{abc}|^2/\|v\|^2+\delta q_{abc}}{1+\delta},
 \qquad
 \sum_{a,b,c}q_{abc}=1
 \tag{J.14}
```

を容量比として作用殻へ渡す。これはcoherent decoderを仮定しない。計算中にすでに存在する8mode信号を同次元blank registerへ可逆に保持し、その二乗容量を末端だけでlatchする。

末端のunresolved条件は、容量pointerとR164作用殻の境界、有限fiber混合の枝対称性、およびR170までの一体化である。これらはR176Cの条件へ集約する。

## M48の条件付き局所因子化との境界

M48の固定singlet型Bell周期はM52を入力providerとして要求しない。M48内部の設定前等重みseed、paired-Hopf準備、2翼strong matching、切断後局所instrumentから始まる。

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

と因子化すれば有限時間核も因子化する。これはM48/R155の局所性監査に使う。M52の1試行信号を式(J.2)へ置換したり、式(J.2)をM52へ再注入したりしない。

## Q2-3の現在地と反証条件

R176A/Bにより3入力の有限tensor-liftと2つの有限Hamiltonian gate zoneは明示された。R177は同じregisterのcoherenceを検査する有限gapを与える。R176Cの物理境界と一体化が条件として残るため、Q2-3は条件付き達成である。

次のいずれかが必要なら現行候補は反証される。

- 第1gate後に枝またはmodeを一つ選ぶ。
- 第2gate前に集団momentを推定してfresh bathへ再準備する。
- B--C gateがA側係数または最終分布を外部から読み取る。
- 逆演算のために内部mode別の外部履歴回収が必要になる。
- 固定3入力でも各modeの個別較正、同期、address、resetが必要になる。
- 誤差上界が内部modeごとの粗い和にしかならない。

一般の $N$ に対するQ2-4はM53の直接モードsector-broadcastと逐次2枝標本化で扱う。これはR176A/Bのtensor-lift反復から自動的に従う結果ではない。

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

この障害を避けるには、正の背景占有率、非局所辺、補助橋状態の少なくとも1つが必要である。粒子位置熱化を使うM50の特殊化では $\delta>0$ を採用し、有限資源誤差として台帳に残す。信号から容量pointerだけを作るR176Cのlatch段階は、このnode命題の対象外である。その後に有限混合を使う場合は本命題の条件を再び受ける。

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

1. R145で信号bath方向を目標rayへ準備する。
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

Q2-1はR176Cにより末端4mode信号を同次元hold-registerへSWAPし、容量latch後にR164/R170へ接続する。別の中間標本器を確率源として挟まない。Q2-2の切断後局所殻は各翼でR170を特殊化し、完全共通原因 $\Lambda$ に条件付けた積因子化誤差を別の $\varepsilon_{\rm prod}$ として加える。Q3は準備終了面のM37標本へR164を一度だけ適用して初期M42位置を作り、その後は付録Nの局所辺衝突bathで同じ粒子を輸送する。M42の一般有向率は局所詳細釣合いを満たさないので、R162の平衡率公式をそのまま用いず、方向別controllerと仕事registerを持つ駆動衝突cellへ拡張する。任意の固定時刻を診断する代替経路だけが付録FのR170を使う。

Q2-4のM53では、計算中にR164の作用容量を作らず、全ゲート後に各bitの直交projector作用だけをlatchする。R161/R162の対称2状態collision bathはR179のfair-bit sourceへ特殊化して使うが、M50/R170の有限枝熱化を逐次段へ重ねない。従って同じ二乗重みを作用殻体積とaperture入口体積で二重計数しない。$L=2^n$ のsignal、work、history、cold、spent容量は受動資源として指数的でもよいが、個別の外部準備・較正・読出しには使わない。

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
4. R145のHopf方程式を作用殻fiberまたは同じ衝突熱浴から導いたこと。
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

この補題は正半定値自己共分散 $\mathbb E[ZZ^\dagger]$ に対する結果である。Q2の交差モーメント $\mathbb E[z_Az_B^{\mathsf T}]$、そのベクトル化、またはそこから作る階数1射影へ適用して、積標本 $z_A\otimes z_B$ がsinglet ray上にあるとは結論しない。付録Iの否定命題はそのような直接singlet支持が不可能であることを示す。M52ではR176Aが1試行の積入力から実際の $Z_S=a\otimes b$ をHamiltonian liftで作るので、集団共分散を準備機構として流用しない。

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

と定める。$\varepsilon_{\rm cap}$ は有限容量結合、$\varepsilon_{\rm width}$ は有限剛性、$\varepsilon_{\rm sym}$ は枝非対称、$\varepsilon_{\rm ad}$ は殻内条件付き平衡化と有効地形切替、$\varepsilon_\delta$ は正則化、$\varepsilon_{\rm mix}$ は有限時間粒子位置混合、$\varepsilon_{\rm coll}$ は有限衝突近似、$\varepsilon_{\rm hold}$ は信号保持反作用である。$\varepsilon_{\rm supp}$ はM50内部誤差でなく、統計的rayから単一試行入力への上流受渡し誤差として別に記帳する。有限時間Hopf誤差から評価した同じ偏差を両方へ加えない。R176CではSWAP、容量latch、shell、mixing、collection、lock、record、clockを $\varepsilon_{170}^{\rm end}$ へ各1回だけ数える。

R164の達成範囲は「条件付き厳密結果＋滑らかな有限幅近似」である。本付録は次を主張しない。

1. 枝容量 $A_i^\delta(v)$ を作る結合が任意のQ1、Q2、Q3信号状態から自動的に準備されること。
2. 作用殻Liouville測度が有限時間の局所力学で一様またはGibbs的に準備されること。
3. 枝対称な余面積因子と入口流束が信号担体だけから自動的に従うこと。
4. 作用殻とR162の衝突熱浴が同一の物理部分系であること。
5. 作用殻、信号保持制御器、衝突セルを含む全微視的仕事・熱収支が粗視化経路熱力学だけから従うこと。
6. $\delta=0$ のnodeを有限剛性、有限衝突流束、有限混合時間で一様に実現できること。
7. 有限信号次元を越える任意POVM、連続スペクトルの一般Born則。
8. 旧M15の入口標本化、殻等方混合、標本化後再埋込み、全測定周期が再び現行結果になること。

R164をR143、R144へ接続すると、Q1-2のBorn分布、同軸反復分布、異軸逐次分布を支える。Q1-2全体はZeno部分が未達であるため部分達成のままであり、R164の有限局所Hamiltonian統合や完全周期は達成条件に含めない。Q2-1ではR176CがM52の実際の末端4mode信号をcanonical SWAPと容量latchでR164へ接続する。R176A/Bはlift、CNOT、逆演算を与えるが、容量pointer--作用殻境界と全末端工程の一体化は条件として残るためQ2-1は条件付き達成である。Q2-2はR155の切断後局所因子化を追加しても条件付き達成のままである。Q3ではR164を準備終了面で一度だけ使って初期M42位置を作り、R172--R174が同じ粒子を輸送する。作用容量結合、M42 bath、clock、記録の統合を自動的に与えないため、Q3-4、Q3-5は条件付き達成のままである。

現行Q2-3ではR176Aの反復liftが作る8mode信号を同じ永続状態bathでR176Bの二段gateへ通す。末端だけでR176Cを $m=L=8$、$\Psi=I_8$ へ特殊化する。規格化出力信号を $Z_{\rm out}$ とすればR164の枝比は $(|(Z_{\rm out})_y|^2+\delta q_y)/(1+\delta)$ となり、正則化誤差は高々 $\delta/(1+\delta)$ である。残る末端一体化条件はQ2-1と共通である。

Q2-4のM53では、R164の線形容量則を各bitの二枝容量 $A_0,A_1$ に使う。R178Eのfixed-volume cellはこの容量をthresholdとして読み、入口体積を新しいBorn因子として掛けない。$L=2^n$ のsignal modeは受動資源として計上し、局所gateとprojectorをR178A/Bの一様規則で作用させる。

# M51有限実正準担体の共通開放ray準備

> **位置づけ：** M51の単一試行実変数、採用開放方程式、seed測度の押出し、R171の有限時間率、切断後のR135輸送、M50への受渡し境界を証明する。


## 目的と存在論

本付録は、量子状態に対応させる階数1統計を初期分布へ直接置かず、有限次元の実古典担体を開放driftで有限時間準備する共通模型M51を定義する。M51はQ1、Q2、Q3の同一ハードウェアを主張する模型ではない。各系列が同じ入出力契約を使えることだけを示す。

M51の記述階層は次の通りである。

| 階層 | M51での対象 | 因果的役割 |
|---|---|---|
| 単一試行の物理状態 | 実正準担体 $(Q,P)$、template正準対 $(Q^w,P^w)$、clock、port履歴 | 開放driftが直接作用し、切断面で下流へ渡る |
| 単一試行の派生座標 | $z=(Q+iP)/\sqrt{2\mathcal J_0}$、$w=(Q^w+iP^w)/\sqrt{2\mathcal J_0}$ | 実方程式を簡潔に表示する。追加の物理場ではない |
| 外部制御 | $g$、$\kappa$、$\lambda_{\rm prep}$、template設定 | pump、sink、port開閉を指定する |
| 集団統計 | $C_Z=\mathbb E[ZZ^\dagger]/\mathbb E[Z^\dagger Z]$、$c$、$\Pi_c$ | 準備結果を記述する。単一試行controllerへ書き戻さない |
| 下流の物理入力 | 各試行の $z(\omega)$ またはその正準SWAP先 | M50が作用容量を作る |
| 観測結果 | M51単独では存在しない | M50/R170が粒子位置と外部記録を作る |

templateの規格化方向 $c=w/\|w\|$ は、装置設定を表すと同時に準備後の統計因子をラベルする。同じ記号を使うのは両者を因果的に同一視するためではない。物理templateを設定し、その実変数から $c$ を計算し、開放流の押出し後に $C_Z\simeq cc^\dagger$ となる順序である。

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

$B=0$ なら $Q$ と $P$ の同じ実対称結合だけでよい。M37の位置ばね網は、さらに結合の局所性と正値性を課し、回転包絡に対して有限時間近似を与える制限された物理実現である。M51の一般 $H_G$ をM37の局所位置結合から導出済みとは扱わない。

## M51の開放方程式を実変数で書く

目標射影を

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

とする。第2章のM51方程式と等価な実方程式は

```math
\dot Q
=
\frac{AP+BQ}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(1-r)Q
-\kappa\{(I-C)Q+DP\}
\right],
```

```math
\dot P
=
\frac{-AQ+BP}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(1-r)P
-\kappa\{(I-C)P-DQ\}
\right].
```

これがM51の縮約ミクロ方程式である。$Q$ と $P$ が各試行の状態であり、右辺はそれらの有限次元driftとして完全に指定される。最小模型では確率微分項を置かない。

| 要素 | 方程式上の項 | 物理的分類 |
|---|---|---|
| 可逆担体 | $G$ または $A,B$ | Hamiltonian流 |
| 動径pump | $g(1-r)(Q,P)$ | action供給と飽和を表す開放drift |
| transverse sink | $-\kappa(I-\Pi_c)z$ | template直交成分を外部portへ捨てる開放drift |
| clock・切断器 | $\lambda_{\rm prep}$ | 準備portの接続時間を指定する外部制御 |
| template | $(Q^w,P^w)$ | 目標rayを物理的に保持する装置自由度 |

M51はpumpとsinkの背後にある有限bath自由度、衝突則、仕事源、排熱先を消去した基礎開放モデルである。従って上の式からの結論は厳密でも、この式を有限閉鎖Hamiltonianから導出したとは呼ばない。有限bath持上げ、雑音、揺らぎ散逸関係、総仕事・熱・エントロピー生成は後続課題である。

## seed測度、押出し測度、無反応

試行開始面で、実状態と空の履歴registerに基準測度

```math
\mu_0(dQ\,dP\,dH_{\rm port})
```

を置く。$\mu_0$ は目標射影そのものを階数1共分散として埋め込まない。template設定 $c$ に対するM51流を $\Phi_c^t$ と書けば、準備時刻の測度は

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

とする。$a_0=0$ の直交超平面はM51で不変であり、そこから目標rayは生成されない。有限 $a_*$ を採ることで有限時間の一様上界を得る。$G_*^c$ を捨てず、下流の完全結果集合で無反応へ送る。

連続なseed測度では直交超平面の測度が零でも、$|a_0|$ が小さい近傍の質量は有限時間資源に影響する。$a_*\downarrow0$ とすると無反応質量は減らせるが、$q_*=(R_*^2-a_*^2)/a_*^2$ と必要準備時間が増える。この交換を無限時間極限で隠さない。

## R171の証明

M51のunitary $U(t)$ で回る相互作用表示を使う。$c$ を固定し、$\widetilde z=ac+p$、$c^\dagger p=0$ と置けば

```math
\frac{da}{d\tau}
=
g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p.
```

$a\neq0$ では両式の共通動径項が消え、

```math
\frac{d}{d\tau}\left(\frac{p}{a}\right)
=
-\kappa\frac{p}{a},
\qquad
\frac{p(\tau)}{a(\tau)}
=
\frac{p_0}{a_0}e^{-\kappa\tau}
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
\sqrt{q_*}e^{-\kappa\tau}.
```

unitary変換はこの距離を保存するので第2章の時刻 $t$ の上界が従う。

作用重み付き第2モーメントに対し、全安全試行で $\|p\|^2\leq q_*e^{-2\kappa\tau}|a|^2$ だから

```math
1-\operatorname{tr}(\Pi_cC_{Z,G_*})
\leq
\frac{q_*e^{-2\kappa\tau}}
{1+q_*e^{-2\kappa\tau}}.
```

純粋射影とのtrace距離に対する上界を使えば

```math
D_{\rm tr}(C_{Z,G_*},\Pi_c)
\leq
\sqrt{q_*}e^{-\kappa\tau}
```

となる。

動径収束も確認する。$q_0=\|p_0\|^2/|a_0|^2$、$y=|a|^{-2}$ と置けば、$\kappa\neq g$ で

```math
y(\tau)
=
1+(y_0-1)e^{-2g\tau}
+\frac{gq_0}{g-\kappa}
\left(e^{-2\kappa\tau}-e^{-2g\tau}\right).
```

$\kappa=g$ では最後の項を $2gq_0\tau e^{-2g\tau}$ に置き換える。従って $|a|\to1$、$p\to0$ であり、有界seed集合上の全ベクトル収束は $\min\{2g,\kappa\}$ で抑えられる。

準備終了後に $\lambda_{\rm prep}=0$ とすれば、開放項は消えて $i\mathcal J_0\dot z=Gz$ だけが残る。各試行の実正準状態は可逆に発展し、R135により第2モーメントはunitary共役で輸送される。以上でR171を得る。

## M50への受渡しと二乗則の位置

M51切断面の各安全試行について、M50へ渡すのは $c$ または $C_Z$ ではなく、実正準担体から得た $z(\omega)$ である。等長埋込み $\Psi$ に対するM50の理想ray重みは

```math
w_i(z)
=
\frac{|(\Psi z)_i|^2}{z^\dagger z}.
```

M51のray上界とR168により、無反応を含む実分布を、

```math
p_c^{\rm id}(i)
=
P(G_*)
\frac{|(\Psi c)_i|^2+\delta q_i}{1+\delta},
\qquad
p_c^{\rm id}(\varnothing)=P(G_*^c)
```

へ比較できる。M51由来のray誤差だけなら

```math
D_{\rm TV}(p^{\rm M51\to M50},p_c^{\rm id})
\leq
\frac{P(G_*)\sqrt{q_*}e^{-\kappa\tau}}
{1+\delta}
```

である。実際のR170では、これに容量、作用殻、混合、衝突、保持、固定、記録の誤差を別に加える。

ここで $|(\Psi c)_i|^2$ は、M51が作った階数1第2モーメントの対角である。同じ式をM50側では各試行の作用比として読む。従って二乗形の状態依存性は準備済み統計に由来し、排他的な単一結果はM50の作用殻状態数と粒子位置熱化に由来する。M51だけで結果頻度が生じるとも、M50が目標rayを無から準備するとも解釈しない。

## 現行系列への特殊化と非主張

| 系列 | M51から供給できるもの | M51から従わないもの |
|---|---|---|
| Q1 | $m=2$、W型生成子、目標Bloch ray。R145はこの特殊化 | W型粒子位置、Born枝、測定後template交換、周期収支 |
| Q2-1 | 指定した局所rayの試行集団準備 | R176Aの1試行tensor-lift、R176BのCNOT・逆演算、R176Cの末端接続 |
| Q2-3 | 指定した3部分系初期rayの試行集団準備 | R176A/Bの反復lift・二段gate、R177、R176Cの末端接続 |
| Q2-4 | 指定した一般回路入力rayの試行集団準備候補 | M53の1試行signal準備、R178のgate・逐次標本化、R179のblank-bank供給。M51を標準M53入力とはしない |
| Q2-2 | setting-free局所seedまたは有限ray template | singlet交差モーメント、paired-Hopf強matching、Bell因果構造 |
| Q3 | M37へ渡すrank-one初期標本集団とM42初期位置用の単一試行信号 | M37--M42との同一局所Hamiltonian統合、空間伝播、終位置記録 |

M51/R171は状態準備の共通開放模型を与えるが、次を主張しない。

1. pump、sink、template、clockを含む有限閉鎖Hamiltonian実現。
2. 雑音付き定常測度、揺らぎ散逸関係、有限bathによる誤差上界。
3. M51とM37、M42、M47、M48、M50、M52、M53が同じ物理装置であること。
4. M51単独で粒子位置、Born型排他的結果、測定後状態を生成すること。
5. template設定から独立に任意の未知入力状態を自己準備すること。
6. 試行列の独立同分布性または二項型有限標本揺らぎ。

これらを追加するときは、M51の開放portを構成する有限bath、仕事源、排熱、情報履歴を完全状態へ加え、準備前測度から切断面測度までの因果鎖を再監査する。

# M37担体上のM42局在トークン

> **位置づけ：** M37の実振動子担体から局所辺流を作り、単一試行の局在粒子トークンを輸送するM42を定義する。R172の等変性、R173の節一様正則化と有限衝突Hamiltonian近似、R174のM51--M37--M42誤差受渡しを証明する。


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

M51の準備後にM42を開始するとき、同じ試行のM37入力信号にM50/R164の作用殻状態数を一度だけ適用し、初期位置 $X_0$ を生成する。この位置がM42の全輸送区間を通して存在する粒子トークンである。終時刻に別のM50位置を再標本化せず、R112の局所記録回路は既存の $X_T$ を読むだけである。

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

R172は初期分布を無償で仮定する定理ではない。現行因果鎖ではM51がM37担体のrank-one統計方向を準備し、M50/R164の1回の作用殻選択が初期M42位置を作る。R172はその同じ位置を輸送する。

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

固定有限グラフと固定時間 $T$ を取る。M51/R171でM37のrank-one初期担体集団を準備し、同じ試行の初期信号にM50/R164の作用殻選択を一度だけ適用して $X_0$ を作り、M37と正則化M42を同時に進め、終時刻に既存の $X_T$ をR112で局所記録する。完全結果集合に無反応を含めると、終位置の理想Born型分布との差は

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

ここで $\varepsilon_{\rm prep}$ はM51のray準備とseed無反応、$\varepsilon_{\rm init}$ は初期作用殻選択、$\varepsilon_{\rm step}$ は時間凍結、$\varepsilon_{\rm coll}$ は方向別閾値分割、Hamiltonian平滑化、仕事register切断を含む有限衝突近似、$\varepsilon_{\rm over}$ はbath cell不足、$\varepsilon_{\rm clk}$ は時計、$\varepsilon_{\rm rec}$ は局所記録である。同じM37包絡偏差を $\varepsilon_{\rm prep}$、$\varepsilon_{37\to42}$、$\varepsilon_{\rm rec}$ へ重複加算しない。

<!-- theorem-start:proof -->
**証明（R174）**

R171の準備切断面からM37初期面への誤差、R164による1回の初期位置分布、R172の理想等変性、R173の正則化誤差、M37--M42生成子のDuhamel誤差、有限衝突列と記録の縮約誤差を因果順に三角不等式で加える。無反応質量を完全結果分布の成分として保つため、事後規格化項は生じない。証明終。
<!-- theorem-end:proof -->

M51の二乗統計と初期M42位置は独立な2つのBorn型確率源ではない。M51は担体集団のrank-one方向を準備し、R164はその単一試行信号から1個の初期粒子位置を物理化し、R172は同じ粒子を輸送する。終時刻には再抽選せず、位置記録だけを行う。

## R123--R125への下流接続

R123の束縛スペクトルと有限環境純位相緩和は、M37有効生成子とその縮約統計に関する結果として維持する。M42を追加しても、固有状態選択、冷却、不可逆緩和は従わない。

R124では3頂点障壁の初期信号から $X_0$ を一度準備し、M42を $T_{\rm bar}$ まで輸送して反対側位置を読む。R125では2経路入力ごとに同じ初期選択・輸送・記録protocolを使う。各比較のM42読出し誤差が $\varepsilon_{174}$ 以下なら、観測される障壁反対側増分と干渉分布距離はそれぞれ

```math
\alpha-2\varepsilon_{174},
\qquad
\Delta-2\varepsilon_{174}
```

以上である。M51、M37、初期作用殻、M42衝突bath、clock、記録を同じ有限局所装置へ統合していないため、Q3-4とQ3-5の条件付き達成判定は変えない。

## Q3-1への非遡及

Q3-1の固定基準は、局所位置結合振動子網から空間格子上のSchrödinger型時間発展を誤差付きで導くことであり、R86が満たす。M42は、粒子を実体として持つために追加する下流強化である。R172--R174をQ3-1達成の根拠へ遡及的に加えず、M42の正則化極限が失敗してもR86の包絡縮約定理自体は失われない。

## 旧M42との差と非主張

旧M42の退役結果群は、任意に与えた物理的複素振幅場と位置過程を直接結び、Q1--Q3へ広く使う模型だった。現行M42はQ3だけに限定し、複素包絡をM37実正準状態の派生表示、rayを集団統計とする。初期二乗分布はM51準備と1回のR164選択に由来し、終時刻M50再標本化と併用しない。旧結果IDは再利用しない。

現行M42/R172--R174は次を主張しない。

1. 最小率がM37のHamiltonianだけから一意に強制されること。
2. M51、M37、作用殻、M42 bath、記録器の単一閉鎖Hamiltonian統合。
3. 1つの固定有限装置で $\rho=\sigma=0$ の厳密nodeを追跡すること。
4. 連続空間の連続粒子軌道、慣性質量、電荷、担体エネルギーの粒子への帰属。
5. 初回到達、吸収、散乱透過率、幾何学的2開口、連続運転スクリーン。
6. 多粒子、交換統計、一般複素hopping、外部磁場。
7. 独立同分布型の有限標本揺らぎ。

M42の採用により、Q3では「粒子が実在せず、終時刻にだけ位置が作られる」という読みに依存しない。一方、採用した局所率と有限衝突bathの物理的選択理由、全周期収支、連続極限は未完成課題として残る。

# M53の一様sector操作と逐次Born標本化

> **位置づけ：** R178A--R178Cの一様gate作用、可逆2枝filter、希少枝切断付き逐次Born標本化、repump、有限誤差と資源を証明する。


## 目的と記号

$n$ bit文字列の集合を $\Omega_n=\{0,1\}^n$、信号空間を $\mathcal H_n=\mathbb C^{\Omega_n}$ とする。複素信号 $Z$ は実正準対の派生表示であり、量子状態を別の実体として追加しない。M53は $\dim\mathcal H_n=2^n$ を受動状態容量として許すが、外部controllerに $2^n$ 個の係数またはaddressを渡さない。

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

## R178Aの証明

<!-- theorem-start:proof -->
**証明（R178A）**

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

## R178Bの証明

<!-- theorem-start:proof -->
**証明（R178B）**

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
P_{\rm cut}\leq2n\tau.
```

切断枝は $\varnothing$ として残すので、これは事後選別ではない。

## Radial repump

selected signal $W$ とblank anti-register $R$ の各mode pairへ同じ2-mode squeezeを作用させる。複素表示の線形正準変換を

```math
\begin{pmatrix}
W'\\
\overline R'
\end{pmatrix}
=
\begin{pmatrix}
\cosh s&\sinh s\\
\sinh s&\cosh s
\end{pmatrix}
\begin{pmatrix}
W\\
\overline R
\end{pmatrix}
```

とする。$R=0$ なら $W'=(\cosh s)W$ でありrayを変えない。選択前の作用を1へ規格化しておけば、条件付き確率が $p\geq\tau$ の枝を標準作用へ戻す利得は $p^{-1/2}\leq\tau^{-1/2}$。従って $s=O(\log(1/\tau))$ である。anti-registerはradial履歴を保持し、使用後にblankとみなさない。

## R178Cの証明と誤差

<!-- theorem-start:proof -->
**証明（R178C）**

理想確率はO.7のtelescopingによりBorn分布へ一致する。O.8が切断質量、O.9が有限repump利得を与える。正則化を各段で最大 $\delta/(1+\delta)$、各段の実装channel誤差を $\varepsilon_{{\rm stage},k}$ とすればMarkov kernelのtelescopingにより

```math
D_{\rm TV}
\leq
2n\tau
+\frac{n\delta}{1+\delta}
+\sum_{k=1}^n\varepsilon_{{\rm stage},k}
```

を得る。初期signalまたはgate列の誤差は、実際の末端signalのBorn分布と理想回路分布の距離として先頭に一度だけ加える。証明終。
<!-- theorem-end:proof -->

## 資源と非主張

各段のactive subspaceを物理的に圧縮しない保守的実装では、signal、anti、work、historyは $O(n2^n)$ modeを使う。縮小subspaceを詰めれば $O(2^n)$ まで減らせる可能性があるが、本結果に不要である。外部gate命令は $O(d)$、逐次出力段は $n$、各bitのtape cell数は付録Pの $O(\log(n/\epsilon))$ である。

本付録は未知量子入力、適応中間測定、誤り訂正、空間局所Hamiltonian、指数受動資源の削減を主張しない。

# M53のhistory処理と滑らかなaperture散乱

> **位置づけ：** R178D--R178Fの履歴逆掃除、reset境界、fixed-volume fresh tape、first-index選択、滑らかなaperture Hamiltonianと有限時間誤差を証明する。


## 目的

本付録はR178Cが各出力bitで要求する2枝選択を物理化する。容量 $A_0,A_1$ に比例する可変体積の殻をblankから生成せず、固定体積のfresh cellを容量依存apertureへ通す。全cell、拒否履歴、容量pointerを含む拡大流は1対1に保ち、無反応を正式な結果とする。

## 履歴の分類

$Y\in\{0,1\}^n$ をbit data記録、$F\in\{0,1\}$ を無反応flagとし、完全結果は $(Y,F)$ として保持する。$H(Y)\leq n\log2$ はdata記録だけの上界であり、flagと微視的履歴に必要な容量を除外しない。

1段の状態を

```math
\Gamma_k
=
(Z_k,W_k,R_k,A_k,C_k,D_k,H_k)
```

と書く。$W_k$ はfilter work、$R_k$ はrepump anti-register、$A_k$ は容量pointer、$C_k$ は使用したaperture cell、$D_k$ は出力記録、$H_k$ はclockとselector履歴である。

出力copy後に逆演算できるのは、出力値を条件として選ばずに完全な微視的入力が残る部分だけである。粗視化した結果、Markov遷移回数、平均容量だけから逆写像を作らない。

## R178Dの証明

<!-- theorem-start:proof -->
**証明（R178D）**

R112のclock、SWAP、比較、記録とR178Bのfilterは拡大正準空間上の1対1写像である。repumpもanti-registerを保持すればsymplecticである。従って出力を空recordへcopyした後、記録剪断を逆実行せず、出力と相関しないworkを逆順に戻せる。

一方、異なる完全結果 $(y,f)\neq(y',f')$ を持つ2入力が、同じ保持出力を残しながら装置とbathの同一点へ戻ると仮定すると、全写像の2入力が同じ全出力へ写り単射性に反する。従って結果と相関する自由度はspent側へ残る。spent状態から $Y$ を復号する誤り率を $p_{\rm e}$ とし、Fano補正を $\eta_{\rm F}=h_2(p_{\rm e})+p_{\rm e}\log(|\mathcal Y|-1)$ と置けば、nats単位で $C_{\rm spent}\geq H(Y)-\eta_{\rm F}$ である。$n$ bit dataでは別に $H(Y)\leq n\log2$ である。証明終。
<!-- theorem-end:proof -->

熱量への変換にはbath温度、準静的消去、仕事源を別に指定する必要がある。本定理は情報容量だけから総熱を同定しない。

## Fixed-volume cell

各cellの容量を $0\leq A_b\leq A_{\max}$ とし、入口位相領域を

```math
\Gamma_{\rm cell}
=
\{0,1\}\times[0,A_{\max}]\times\Gamma_{\rm aux}
```

と表示する。離散labelは実装ではP.8の連続selector井戸に持ち上げる。理想入口測度はlabelが等重み、$U$ が平坦、auxiliary測度が全branchで同じとする。

branch $b$ のaccept領域は

```math
\mathcal A_b
=
\{B=b,\ 0\leq U<A_b\}.
```

その入口測度は共通因子を除いて $A_b/(2A_{\max})$ である。R164の作用殻体積をさらに掛けない。

## First-index法

各cellをindex $j=1,\ldots,N$ の順に、同じ長さのclock窓で試す。最小indexのacceptを出力し、それ以前が全てrejectなら次cellへ進む。物理的な出口到着時刻で競争させない。

1 cellでbranch $b$ がacceptされる確率を $q_b$、rejectを $r$ とする。最初のacceptがbranch $b$ である確率は

```math
\sum_{j=1}^Nr^{j-1}q_b
=
q_b\frac{1-r^N}{1-r}
=
\frac{A_b}{A_0+A_1}(1-r^N).
```

全rejectは $r^N$ である。

## R178Eの証明

<!-- theorem-start:proof -->
**証明（R178E）**

P.4で $q_b=A_b/(2A_{\max})$、$1-r=q_0+q_1$。P.5の幾何和から定理の分布を得る。理想branch分布へ同じ総質量 $1-r^N$ を割り当て、残りを $\varnothing$ とすれば、理想Born出力だけを持つ分布との差は失敗質量 $r^N$ である。

$A_0+A_1\geq S_->0$ なら $r\leq1-S_-/(2A_{\max})<1$ なので、$nr^N\leq\epsilon$ を満たす $N$ は $O(\log(n/\epsilon))$ である。証明終。
<!-- theorem-end:proof -->

同じcell列を別試行で再利用すると、出力とcell microstateが相関しているため独立同分布性は従わない。有限試行数なら別のfresh列を用意し、無期限運転なら開放cell流を必要とする。

## Aperture Hamiltonian

反応座標 $(X,P_X)$ と基準barrier $V_0$ を置く。branch selectorの連続座標を $Q_B$、2つの安全井戸上で一定になる滑らかな関数を $\beta_b(Q_B)$ とし、$\beta_0+\beta_1=1$ とする。

```math
A(Q_B)
=
\beta_0(Q_B)A_0+\beta_1(Q_B)A_1.
```

相互作用は

```math
H_{\rm ap}
=
\frac{P_X^2}{2m}
+V_0(X)
+g\{U-A(Q_B)\}\rho(X)
+H_{\rm hold}.
```

$H_{\rm hold}$ はselector、容量pointer、$U$ の安全領域を保持する。$V_0(0)=E_0$、$\rho(0)=1$ なら頂上energyは $E_0+g(U-A_b)$。入口energy $E_0$ に対し $U<A_b$ で通過、$U>A_b$ で反射する。

## 滑らかなlabelと境界失敗

抽象離散変数を滑らかなHamiltonianへ直接代入しない。selectorの左右安全井戸 $\mathcal W_0,\mathcal W_1$ では

```math
\beta_b=1,
\qquad
\beta_{1-b}=0.
```

井戸間の遷移帯はlabel failureへ送る。その入口質量を $\varepsilon_{\rm label}$ とする。R179のdyadic digitも同じplateau方式で $U_k(Q)$ として結合し、controllerがbit列を読み取らない。

## 余分な極値の排除

相互作用窓の外縁では

```math
\partial_XH_{\rm ap}
=
V_0'(X)+g\{U-A(Q_B)\}\rho'(X).
```

$|U-A(Q_B)|\leq A_{\max}$ とし、

```math
gA_{\max}\|\rho'\|_\infty
<
\inf_{{\rm supp}\,\rho'}|V_0'|
```

なら、$\rho'$ のsupport上で摂動項は基準傾斜を反転できない。従って予定外の停留点を作らない。

## 有限時間境界幅

barrier頂上近傍を逆調和近似すると、separatrixからenergy差 $|\Delta|$ の軌道が判定領域を出る時間は $\omega^{-1}\log(C/|\Delta|)$ で増える。energy幅、較正幅を加えると、時間 $T$ で未判定となる容量境界幅は

```math
\ell_{\rm eff}(T)
=
\frac{
\Delta_E+\Delta_{\rm cal}
+C_0e^{-\omega(T-t_0)}
}{g}.
```

従って $\ell_{\rm eff}=O(\epsilon/n)$ には $T=O(\log(n/\epsilon))$ で足りる。有限時間の滑らかな流でhard thresholdを正確に実装するとは主張しない。

## Backreaction

Hamilton方程式から

```math
\dot P_{A_b}
=
g\beta_b(Q_B)\rho(X),
\qquad
\dot P_U=-g\rho(X).
```

容量座標 $A_b$ と $U$ が変化しなくても共役momentumは散乱履歴を持つ。逆散乱しない運転ではpointerとcellをspent側へ送る。1標本で必要な容量pointerは $O(n)$ である。

## R178Fの証明

<!-- theorem-start:proof -->
**証明（R178F）**

P.7の頂上energy差が理想threshold、P.9が余分な極値の排除、P.10が有限時間境界幅を与える。容量を $\widetilde A_b$ として読み出した実効判定は $|\widetilde A_b-A_b|\leq\ell_{\rm eff}$ を満たす。$A_0+A_1\geq S_->2\ell_{\rm eff}$ なら、有限 $N$ tapeとの合成誤差は

```math
D_{\rm TV}
\leq
\left(
1-\frac{S_--2\ell_{\rm eff}}{2A_{\max}}
\right)^N
+\frac{2\ell_{\rm eff}}{S_--2\ell_{\rm eff}}
+\varepsilon_{\rm tape}
+\varepsilon_{\rm label}
+\varepsilon_{\rm clock}.
```

P.11よりpointerを無履歴で再利用しない。以上で定理を得る。証明終。
<!-- theorem-end:proof -->

## 退役作用区間samplerおよびR170との境界

R178Eは正規化済み確率表または累積確率区間を装置へ入力しない。入力は局所的な非規格化容量 $A_0,A_1$ と、回路非依存のfixed-volume cellである。拒否と無反応を除外しないので、退役した作用区間samplerの事後規格化経路ではない。

M53は二枝apertureを使い、R170の有限混合を同じ段に加えない。R170はQ1、M48、一般M50 instrumentの別実装として残る。

# M53の一様blank-bankとfresh-cell供給

> **位置づけ：** R179の反復partial SWAP、有限温度誤差、root入力、fair-bit源、dyadic座標化、独立供給則と資源境界を証明する。


## 目的と資源境界

R178C--R178Fは、各出力bitに新しいwork、anti-register、容量pointer、aperture cell、selector digitを要求する。本付録では、それらを回路出力に応じて外部から逐次生成せず、初期時刻に用意した一様bankからclock順に供給する。

許すものは、回路と精度から計算できる多項式長の外部program、指数個でもよい受動cell、cold sourceとspent sinkを含む開放bathである。総bath容量、総熱、装置体積を多項式とする主張は置かない。

## 閉Hamiltonian系だけではblankを増やせない

同じ有限次元位相空間上のHamiltonian流は体積を保存する。異なる使用済みmicrostateを同じblank領域へ写し、他の自由度にも区別を残さない写像は単射でない。従ってblank供給は、使用済み状態をspent側へ移すか、より大きいbankの未使用領域と交換しなければならない。

この障害を隠さないため、M53のbankを

```math
\mathcal B
=
\mathcal B_{\rm cold}
\times
\mathcal B_{\rm active}
\times
\mathcal B_{\rm spent}
```

と分ける。collective resetはactive状態を消去せず、cold cellと交換して履歴をspent側へ移す。

## 一様bank index

cellは種類 $a$、出力段 $k$、試行index $j$、標本index $s$ で静的に並べる。clockは同じ有限状態遷移規則で次のcellを選ぶ。外部controllerはcellのmicrostate、Born重み、accept結果を読まない。

必要数が事前に

```math
N_{\rm cell}
=
O(SnN)
```

と決まる有限runでは、bank全体を初期状態の一部として用意する。ここで $S$ は標本数、$N$ は1 bit当たりのaperture試行数である。無期限運転には同じ局所規則を持つ開放cell流を仮定する。

## 反復partial SWAP

bank全体のactive vector $W_r$ と第 $r$ cold layer $E_r$ の対応mode間に、一定精度のpartial SWAPとして同じ2-mode回転を並列に作用させる。couplerは一様有限規則から作る同一の静的二次Hamiltonianとし、受動clockがroundを進める。指数個のcouplerを外部から個別に開閉しない。適切な位相規約でactive出力を

```math
W_{r+1}
=
C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1
```

と書く。pairごとの全変換は $(w',e')=(cw+se,-sw+ce)$、$c^2+s^2=1$ という回転であり、実正準かつ可逆である。cold側出力 $e'$ はspent側へ残す。$C_r,S_r$ は固定精度で実装され、各回に同じ上界 $\rho$ が使える。full SWAPを指数精度で1回実装する必要はない。

cold layerのaggregate blankずれを $\|E_r\|\leq\eta_{\rm cold}$ とし、$\|S_r\|\leq1$ を使えば

```math
\|W_R\|
\leq
\rho^R\|W_0\|
+\frac{\eta_{\rm cold}}{1-\rho}.
```

従って $\|W_0\|\leq R_{\rm in}$ に対し

```math
R
=
O\!\left(
\log R_{\rm in}
+\log\frac{1}{\varepsilon_{\rm blank}}
\right)
```

回の反復で、cold floorを除く残差を $\varepsilon_{\rm blank}$ 以下にできる。$R_{\rm in}$ が $2^{O(n)}d^{O(1)}$ 以下なら $R=O(n+\log d+\log(1/\varepsilon_{\rm blank}))$ である。

## Cold floorとpassive容量

有限温度bathでは $\eta_{\rm cold}=0$ を仮定しない。実効blank誤差は

```math
\varepsilon_{\rm reset}
=
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho}
+\varepsilon_{\rm swap}
```

と評価する。$\varepsilon_{\rm swap}$ は反復実装誤差の合計である。要求精度を下げるにはcold sourceの品質または反復gate精度を上げる必要がある。外部精度を多項式に保つには、exact invariant blankを持つcold source、またはbank全体のaggregate誤差を一様contractで保証するsourceを仮定する。各modeに独立な定数thermal noiseが残るsourceは、bank次元とともにaggregate誤差が増えるためこの仮定を満たさない。

各反復で用いたcold cellはactive履歴と相関し得るため、再びcold cellとして数えない。有限runでは必要数を初期bankに積み、無期限runではcold流とspent sinkを仮定する。この容量は指数的でもよい受動資源であり、外部制御programの長さとは区別する。

## Root入力の供給

R112のclockを開始するroot packetは、固定した1個のsource modeと最初のactive clock modeの間の定数次元SWAPで注入できる。sourceの絶対位相は、以後の判定が作用と相対位相だけに依存する限りglobal phaseとして消える。

標本ごとにroot packetを再利用するなら、source側の使用済み状態を保持するか、新しいsource cellへ進む。rootを閉系から無履歴で複製するとは主張しない。

## 一様fair-bit源

R161--R162の対称2状態collision bathを、selector digitのsourceとして使う。遷移核を

```math
K
=
\begin{pmatrix}
1-a&a\\
a&1-a
\end{pmatrix},
\qquad
0<a<1
```

とすれば定常分布は $(1/2,1/2)$ である。mixing後の1-bit lawのずれを $\varepsilon_{\rm bit}$、cell間相関の総寄与を $\varepsilon_{\rm corr}$ として追跡する。独立性を近似だけで済ませる場合、その誤差を $\varepsilon_{\rm tape}$ へ含める。

初期bath法則は、回路、入力signal、途中の出力から独立でなければならない。回路のBorn重みを初期digit分布へ埋め込まない。

## Dyadic座標とthreshold discrepancy

$k$ 個のfair digit $C_1,\ldots,C_k\in\{0,1\}$ から

```math
J_k
=
\sum_{\ell=1}^k2^{k-\ell}C_\ell,
\qquad
U_k
=
A_{\max}\frac{J_k+1/2}{2^k}
```

を作る。$U_k$ は各dyadic区間の中点に一様に分布する。連続一様変数とのtotal variation距離は比較しない。両者は測度として互いに特異だからである。

代わりにthreshold classに対する累積分布差を使う。任意の $0\leq A\leq A_{\max}$ について

```math
\left|
\Pr[U_k<A]
-\frac{A}{A_{\max}}
\right|
\leq2^{-k}.
```

従って $nN$ 回のthreshold判定に対する合計discrepancyを $\epsilon$ 以下にするには $k=O(\log(nN/\epsilon))$ で足りる。

## Data processingと供給独立性

理想product lawを $\mu^{\otimes L}$、実際のtape lawを $\widetilde\mu_L$ とする。回路とapertureの決定的な拡大正準流を $\Phi$ と書けば、任意の可測粗視化に対し

```math
D_{\rm TV}
\left(
\Phi_*\widetilde\mu_L,
\Phi_*\mu^{\otimes L}
\right)
\leq
D_{\rm TV}
\left(
\widetilde\mu_L,
\mu^{\otimes L}
\right).
```

従ってbit bias、有限mixing、cell間相関の誤差は、最終出力で増幅されず $\varepsilon_{\rm tape}$ として一度だけ加えられる。ただし回路依存の初期相関がある場合、この議論は使えない。

## R179の証明

<!-- theorem-start:proof -->
**証明（R179）**

Q.3の静的indexとR112のclockにより、必要なcellを出力に依存しない順序で供給できる。Q.4--Q.5の反復partial SWAPはactive modeを所望のblank近傍へ移し、使用済みmicrostateをcold cellからspent側へ送る。同一静的couplerと受動clockを使うため、外部controllerのquench workをbank次元へ比例させない。Q.6がroot packet、Q.7--Q.8が回路非依存のdyadic selector tapeを与える。Q.9により供給法則のずれは最終出力誤差へ加法的に伝わる。

有限runでは初期bank容量を必要数だけ取ればよい。無期限runではcold inflowとspent outflowを仮定する。以上により、総bath容量を多項式と仮定せず、外部program、反復段数、1判定当たりdigit数を多項式に保つ一様供給が成立する。証明終。
<!-- theorem-end:proof -->

## 資源評価

1回のblank化に必要なpartial SWAP数は

```math
O\!\left(
n+\log d+\log\frac{1}{\varepsilon_{\rm blank}}
\right).
```

1 threshold当たりのdigit数は $O(\log(nN/\epsilon))$、R178Eのcell試行数は $N=O(\log(n/\epsilon))$ である。固定標本数 $S$ の外部clock長はこれらと $d,n,S$ の多項式である。

一方、signal、work、history、cold、spentを含む受動bank容量と総散逸は指数的でよい。この分離がQ2-4の現在の規則であり、通常の意味の効率的古典simulationや多項式総熱を意味しない。

## 反証条件と非主張

次のいずれかが必要ならR179は成立しない。

- cold cellが回路出力に応じて準備される。
- 使用済みcellを履歴なしにcold cellへ戻す。
- 1回のSWAPに指数小の較正誤差を要求する。
- dyadic tapeの離散lawと連続一様lawのtotal variation一致を要求する。
- bath容量または総熱を多項式に制限する。

R179は、cold bathを閉Hamiltonian dynamicsから生成すること、指数受動資源を削減すること、無期限運転を有限bankで行うことを主張しない。

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
