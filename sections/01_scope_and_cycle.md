@number: 1
@chapter: 本文
@title: 問題設定、現行模型、達成範囲
@status: M54をQ1・Q2・Q3の共通有効profile族、M37をQ3 spatial signalとR187条件下のQ1 W2 control carrierの物理backendとして区別し、系列固有protocolとsame-hardware統一目標を分離して現行因果鎖と未統合境界を示す。

## 1.1 研究上の問い

本論文の中心目的は、古典的な粒子、振動子、熱浴、制御器、記録器からなる装置が、量子計算機をブラックボックスとして見たときと同種の回路入力を受け、量子出力分布を指定誤差内で返し、そのための外部制御複雑度を多項式に抑えられるかを調べることである。量子力学は結果の比較基準に使うが、古典モデルの運動方程式や初期確率へ答えを直接入力しない。Q1とQ3は、このblack-box機能を支える量子型有効構造の古典物理的起源を独立に検査する。

有限次元Schrödinger方程式を実正準方程式へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、測定後状態、記録、resetは得られない。本稿は次を別々に要求する。

1. 実担体と開放portから階数1の試行集団統計を有限時間で準備する。
2. 可逆な信号操作を古典正準流として実装する。
3. 各試行の信号作用から排他的枝または初期粒子位置の状態数を作る。
4. Q1・Q2では粒子位置を枝分布へ再平衡化し、Q3では同じ局在粒子をM37担体に沿って輸送する。
5. 無反応を含む完全結果集合を局所記録する。
6. 系列固有の状態更新、ゲート、Bell監査、空間現象を共通読出しへ接続する。

### 1.1.1 ブラックボックスとしての比較基準

本稿は内部自由度の総数と、外部から装置を利用するための複雑度を区別する。量子ビットの有効2準位記述の背後にある微視的自由度数をblack-box interfaceから数え上げないのと同様に、M54内部の受動mode数だけをoperational complexityとは同一視しない。

| 分類 | Q2-4での扱い | 例 |
|---|---|---|
| operational resource | 多項式上界を要求 | 回路記述、compile、外部program、制御channel、address port、総時間、精度、制御energy/action、期待試行回数 |
| reported internal resource | 総量を報告するが、それだけでは不達としない | 受動mode、静的coupler、state capacity、cold/spent bank、装置体積、総bath容量、総熱 |

内部資源がmode別較正値、指数長の配線表、指数精度、指数時間、稀な成功として外部interfaceへ露出した場合はoperational resourceへ繰り上げて数える。したがって本稿がQ2-4で主張するのはblack-box operational equivalenceであり、通常の効率的古典simulationや量子計算機と同等の総物理資源効率ではない。

### 1.1.2 力学の導出と装置の運転順序

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

| 関係 | 進む順序 | 未導出の接続 |
|---|---|---|
| 担体の物理的導出 | M37、R86、W型低2モード、R140 | 全制御時間の包絡・状態誤差と資源 |
| 1試行の運転 | 初期実座標の準備、制御、作用殻選択、記録 | 準備・測定境界の同一装置化 |
| 複合系への拡張 | Q1入力、共同担体、結合操作、読出し | W型入力の抽出・転送の物理実装 |

M54による初期実座標の準備は、M37の運動法則をQ1から導くことではない。力学命題は指定された初期実座標を条件として始め、準備の構成は別に接続する。Q3全体の達成をQ1導出の前提にはしない。

本稿では「統一」を二層に分ける。M54は共通状態型、因果契約、port、matching/readout原理を共有する有効profile族であり、M37はそのspatial signal sectorを局所ばねHamiltonianから実装する物理backendである。共通profileを共有することは、同じ製造済みハードウェアを共有することを意味しない。全系列を同じ物理port、担体、bath、clock、反復周期へ統合する強い主張はM0に残す。

## 1.2 現行因果鎖

状態準備とBorn型読出しは

```math
\Gamma_0
\xrightarrow{\mathrm{M54/R181A}}
C_Z\simeq cc^\dagger,
\qquad
Z(\omega)
\xrightarrow{\mathrm{R164}}
\pi_i^\delta(v)
\xrightarrow{\mathrm{R161/R162}}
X=i
\xrightarrow{\mathrm{R170}}
D_i
```

の順に分ける。これはM54の $n=1$ または深さ1 nodeである。一般のQ2ではR181Bで固定入力をliftし、R181Cで同じregisterを操作し、R181Dで上のM54 static/R170 nodeをprojector-treeとして反復する。R112は有限基底制御、時計、比較、SWAP、記録、逆計算の共通定理である。

Q3だけは下流を

```math
\Gamma_0
\xrightarrow{\mathrm{M54/R181A}}
Z_{t_0}(\omega)
\xrightarrow{\mathrm{R164\ once}}
X_{t_0}
\xrightarrow{\mathrm{R161/R184}}
X_T
\xrightarrow{\mathrm{R112\ record}}
D_{X_T}
```

とする。終時刻に別のstatic-profile位置を作らない。

各試行の実体は実正準担体、粒子位置、bath、template、clock、記録・履歴である。M54の複素register $Z$ は実正準担体の派生表示、$c,C_Z$ は解析上の試行集団統計である。R164/R161/R170は同じ試行の物理signalから排他的結果を作る。これらを同一視しない。

| 系列 | 信号準備と操作 | 単一試行の下流入力 | 系列固有の下流結果 |
|---|---|---|---|
| Q1 | M54/R181A、Q1 W型2モードprotocol（旧M47）、R135、R140、R143--R144 | 単一試行のW型signal座標 | R181D深さ1のrank-one post-state handoffとR143のW型読出し特殊化 |
| Q2-1 | M54、R112、R181B--R181D | 1試行内の永続4mode信号とanti/work | 可逆tensor-lift、CNOT、逆演算、条件付き末端instrument |
| Q2-2 | M54、R180A--R180C | M54の1試行末端信号と切断後の各翼の局所信号 | setting-pre block抽出、paired-Hopf、2つのR170の条件付き局所合成、Bell監査、帰還 |
| Q2-3 | M54、R181B--R181D、R177 | 3部分系の永続8mode信号とanti/work | A--B、B--C、GHZ--$T$--逆演算、条件付き末端instrument |
| Q2-4 | M54、R112、R161、R162、R164、R170、R181A--R181D、R178D、R179 | $L=2^n$ の受動直接モード、逐次2枝filter、collision bank | 一般回路列と完全結果空間上の逐次出力。指数的な受動bankと総熱を許す |
| Q3 | M54 spatial profile、M37、R86、R135 | 準備終了面のM37標本と初期configuration | R161 moving、R184の粒子輸送、R123--R125への接続 |

集団の第2モーメント、交差モーメント、共同頻度を単一試行controllerへ書き戻さない。Q1・Q2は各試行の有限signalだけをM54 static profileへ渡す。Q3は各試行のM37実振動子、M54 spatial profileの現在位置、局所collision cellだけを進める。

## 1.3 現行模型と実装階層

| 識別 | 分類 | 役割 | 状態 |
|---|---|---|---|
| M54 | 共通有効signal--configuration profile族 | Q1/Q2のstatic profileとQ3のspatial-moving profileを同じ状態型、R164、R161、R162から派生する。R181A--R181Dは準備、lift、gate、projector-treeを与える | 現行有効層 |
| M37 | 物理Hamiltonian backend | M54 spatial signal sectorをR86/R184で実装し、R187条件下では弱結合W型最低2正常modeをM54 W2 static profileのQ1 control carrierへ接続する | 現行物理backend |
| M0 | same-hardware統一目標 | M54各profile、M37 backend、系列固有protocol、記録、外部流路を同じハードウェアと反復周期へ統合する | 未完成 |

系列固有のQ1 W型2モード制御・測定は、M54 W2 static profile上のprotocolとして扱う。R187はそのcontrol carrierをM37弱結合W型で物理実装するが、R181A準備やR170測定sectorまでM37へ吸収しない。旧版のモデルID M47は参照互換のため「旧M47」として残すが、現行模型表へ独立模型として二重計上しない。Q2-2のR180もM54 static profileに接続する系列固有receiverであり、M54とは別の親模型ではない。

置換済み模型と独立研究線は本文の模型地図へ並べない。最小索引は `notes/superseded_result_index.md`、詳細は各研究メモとGit履歴に置く。

## 1.4 達成判定

「達成」は、固定した範囲で基準を厳密に満たすか、任意の $\epsilon>0$ に対して誤差を $\epsilon$ 未満にする有限構成を選べることを指す。形式極限、構成のない収束仮定、無反応試行の事後除外は含めない。

| 目標 | 現在地 | 中心的な実現層 | 主な残件 |
|---|---|---|---|
| Q1-1 | 達成 | M54 W2 static profile上のQ1 W型2モード制御protocol | 固定目標上の残件なし。M37--W物理backend接続は強化課題 |
| Q1-2 | 部分達成 | 同じW2 profile上のQ1測定protocol | 測定統計は導出済み。Zeno抑制の有限誤差付き接続が残る |
| Q2-1 | 条件付き達成 | M54 static profileと永続register | 末端instrumentの単一装置統合 |
| Q2-2 | 条件付き達成 | M54 static profileとR180 receiver | R180Cの単一装置統合、自由設定、空間分離、一般状態 |
| Q2-3 | 条件付き達成 | M54三部分系static profile | 末端一体化。一般サイズ資源はQ2-4で判定 |
| Q2-4 | 条件付き達成 | M54一般static profileと受動bank | 一様装置族としての静的sector、collision、filter、bank、clock統合とR186の製造誤差・noise条件 |
| Q3-1 | 達成 | M37 | 固定目標上の残件なし |
| Q3-2 | 部分達成 | M54 spatial profile | finite collisionから時間対称加速度への明示誤差 |
| Q3-3A | 達成 | M37＋有限環境 | なし |
| Q3-3B | 達成 | M37＋有限環境 | なし |
| Q3-3C | 達成 | M37＋有限環境 | なし |
| Q3-4A | 条件付き達成 | M54 spatial profile＋M37 backend | 準備から終位置記録までの単一装置統合 |
| Q3-4B | 条件付き達成 | M54 spatial profile＋M37 W型backend | 半周期・一周期を含む単一装置統合 |
| Q3-5 | 条件付き達成 | M54 spatial profile＋M37 backend | 同上。幾何学的2開口と連続スクリーンは未構成 |
| Q3-6 | 未達 | 完結層なし | 節、巻数、位相すべり、細分化安定性、非整数モノドロミー排除の統合 |

固定目標の文言と達成判定、およびprofile・backend・protocolごとの完全な依存台帳は `PROJECT_STATUS.md` を正本とする。本文では完全なR番号表を複製しない。Q1-2はBorn分布、同軸反復分布、異軸逐次分布を導出済みとし、Zeno部分が未達であるため部分達成とする。Q2-1からQ2-4は、明記した根拠モデルと根拠結果から互いに独立に判定する。これは他のQ2目標の達成ラベルを前提にしないという意味であり、同じ模型または部品定理を複数の根拠行へ載せることは禁止しない。共通ハードウェア族への統合は固定目標とは別の実装努力目標である。Q2-3は3量子ビット型二段ゲート合成、Q2-4は指数的な受動自由度を許す多項式外部制御サンプリングである。置換または削除した旧固定目標は退役索引に保存する。

## 1.5 達成判定の独立性と模型間受渡し

Q2固定目標は、Q2-1のM54 static profile、Q2-2のM54/R180 receiver、Q2-3のM54三部分系static profile、Q2-4のM54一般profileをそれぞれの根拠として独立に判定する。Q2-1とQ2-2がM54を共有しても、一方の達成状態から他方を推論しない。規模ごとの一様な共通ハードウェア族へ統合することは、別の実装努力目標である。Q3-3A--Q3-3CとQ3-4A--Q3-4Bも接尾辞ごとに独立に判定し、系列名Q3-3、Q3-4へ独立した達成状態を置かない。

M54は同じ試行の $Z_S$、anti-register、work/historyをそのまま次のgate窓へ保持し、共同momentへの置換、fresh bathへの再準備を許さない。内部の有限modeは受動bath自由度であり、個別の外部初期化、較正、同期、address、読出し、resetを要求しない。Q2-3の完全な合成契約は付録Jを正本とする。Q2-2では実際の2入力末端信号をholdしてR180へ渡し、A設定による直交block分解後も同じ試行の選択blockをreceiver sourceとして使う。

## 1.6 非主張

本論文は次を主張しない。

1. Q1、Q2、Q3が同一の達成済み物理装置であること。
2. M54の採用driftを有限bath、仕事源、排熱先から導出済みであること。
3. R164の枝状態数だけで作用殻準備と熱化をミクロ導出したこと。
4. R170の全構成部品を1つの具体的有限局所Hamiltonianへ統合済みであること。
5. 長期頻度または有限熱化から独立同分布型有限標本揺らぎが従うこと。
6. R180 receiverが標準的な空間分離・自由設定Bell実験を再現すること。
7. Q3の有限格子moving-matching過程から連続空間の連続粒子軌道が一様に得られること。
8. Q2の一様な共通ハードウェア努力目標、R181Dの末端一体化、M54の全構成部品を単一の一様装置族へ統合済みであること。
9. 指数的な受動自由度を許すことが、指数時間、指数個の個別制御、指数的に細かい精度を許すこと。
10. Q2-4のblack-box operational equivalenceから、量子計算機と同等の装置体積、物質量、製造費、総bath容量、総熱が従うこと。
11. 連続空間、多粒子、一般有限POVMの一様構成。

## 1.7 論文の読み方

第2章はM54の完全状態型とR181A--R181D、第3章はM54の $n=1$ W型Q1特殊化、第4章は $n=2,3$ のQ2特殊化、第5章はM54駆動R180 Bell receiver、第6章と第7章はM54 spatial-moving profileとM37による局所ばねbackendを扱う。第8章は誤差、資源、反証条件をまとめ、第9章で結論を述べる。

付録AはR112、BはQ1 instrument、CはR181B/R181Cの有限次元特殊化、DはR180A/C、E--GはQ3、HはM54/R181A/R135/R140のW型2モード対応、IはR180B、JはQ2二段合成、K--LはR161/R162/R164/R170、MはR181A、NはM54 spatial moving matching、Oは一様register代数、PはR181D projector-tree、QはR179のbank供給を扱う。

導出主線を追う場合は、第6.2〜6.7節の実運動と静的縮約、第3.3〜3.5節のW型縮約、第3.5.1節の受渡し系を先に読む。その後に共通測定、第4章の共同担体、第7章の粒子位置現象へ進む。章番号と固定目標の段階番号は論理的な依存順を意味しない。