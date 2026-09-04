@number: 9
@chapter: 本文
@title: 結論
@status: M54をQ1・Q2の共通親模型族として整理し、R181A--R181D、R178D、R179、R180 receiver、およびQ3のM37--M42二層模型を総括する。

## 9.1 確立したこと

M54は、一様有限正準register、物理source/template port、anti/work、raw・regularized容量、selector、cold/spent bank、記録、clockを持つQ1・Q2の共通親模型族である。R181Aは物理template準備、R181Bは固定2・3入力の可逆tensor-lift、R181Cは永続register上の局所gate列、R181DはR170駆動projector-tree Born instrumentを与える。各試行の複素信号は実正準座標の派生表示であり、解析上のrayや確率表をcontrollerへ書き戻さない。

Q1はM54の $n=1$ W型特殊化である。R181AのW型2モード系は独立結果IDを持たない。共通R135は階数1bath共分散のBloch球、R140は任意の $SU(2)$、零傾斜占有振動、離調Rabi式を与える。R181Dの深さ1とR143が有限コントラストの左右読出しと結果別状態更新を与える。R135、R140によりQ1-1を達成と判定した。

M50/R164は一般有限信号作用を枝容量へ写し、各排他的枝の2作用殻を単一Liouville母測度で数えるとBorn型条件付き状態数が得られることを示す。二乗形の状態依存性はM54が準備するrank-one第2モーメントに現れ、M50/R164は各試行の実担体信号から排他的結果の状態数を作る。この二段を二重の確率源として数えない。R161は条件付きGibbs再平衡化、R162は有限衝突熱浴を与え、その系として条件付き中間状態の正逆経路確率比と相対有効仕事が従う。作用殻明示表示と消去表示を同じ分配関数で二重計数せず、殻自由エネルギー仕事 $W^{\rm sh}$ と相対有効仕事 $W^{\rm rel}$ を区別する。

R143はHopf方向準備、操作面ごとの再平衡化、解析器、傾斜固定、辺閉鎖、M47粒子位置の局所記録、結果別テンプレート交換、測定後再平衡化を合成する有限誤差instrumentである。記録器は統計振幅、共分散、全密度、確率流、遷移率を入力にせず、各試行に存在する $X$ の局所位置だけを読む。R144は固定有限段について永久記録、内部逆計算、外部空セル交換を合成する。解析器中または周期間に配置--信号bath matchingを連続保存することは仮定しない。

Q2-1はM54の $n=2$ 特殊化である。受動的な4mode信号、anti-register、work、clock履歴をbathへ任せ、controllerはport、lift窓、gate種、対象、作用窓、末端読出しだけを指定する。R181Bは一般積入力の可逆tensor-lift、R181Cは同じ永続register上のCNOT、局所操作、逆演算を与える。R181Dは深さ2のprojector-treeを与える。末端の物理境界と一体化を条件としてQ2-1は条件付き達成である。

Q2-2にはM54駆動setting-pre paired-Hopf receiverを採用した。固定singlet源はM54の $|00\rangle\to H_A\to\mathrm{CX}_{A\to B}\to X_B\to Z_A$ で作り、R181C後の実際の1試行末端信号をcanonical SWAPで物理hold信号 $\widetilde V$ としてそのまま中央receiverへ渡す。$V=\widetilde V/\|\widetilde V\|$ は解析上のrayであり、SWAPが状態依存除算を行うわけではない。R180AはA設定basisで $\widetilde V$ を2つのblockへ分解し、物理容量比から枝重み、同じblock作用からB側templateを得る。固定singletでは各枝重みが $1/2$ となり、規格化templateは旧spin-flip fiberをglobal phaseまで回復する。

R180Bは選択したA側・B側templateをsourceとしてpaired-Hopf pump、paired差sink、直交sinkを駆動し、共役位相を持つ2翼rayへ有限時間で整列する。R180Cは中央切断後のfresh局所作用殻と局所応答が完全共通原因に条件付けて積因子化すること、Born共同分布、非信号性、CHSH差、fresh-cell帰還をまとめる。共通原因を平均した大域Bell対数を物理的な切断後ポテンシャルへ戻さない。M54の1試行信号 $\widetilde V$ を使い、集団交差momentまたはR181Cの生成子 $G_S$ を終端共役として再注入しない。

Q3ではM54/R181Aからrank-one初期集団を受け取り得る契約を上流に置き、M37の正確局所方程式、生成子誤差、有限時間Schrödinger型近似、作用比診断をR86へまとめる。その上に、各試行で1個の局在粒子位置、局所辺bath、clock、履歴を持つM42を置く。R172はM37有効辺流に沿う等変輸送と有限期待跳躍数、R173は節一様正則化と有限衝突Hamiltonian近似、R174はM54準備、1回の初期R164選択、M37担体、M42輸送、終位置記録の誤差台帳を与える。R123--R125の束縛状態、純位相緩和、障壁値未満確率移動、最小2経路干渉を維持し、後2者をM42へ接続する。終時刻に別のM50位置を再標本化しない。

## 9.2 条件付きで確立したこと

R143の結果分布と条件付き状態は、R181Aの信号bath方向準備、R164の作用殻準備、R161の有限時間再平衡化、R162の有限衝突近似と辺閉鎖、傾斜保持、局所記録、枝別テンプレート交換の誤差上界に条件付く。大域階数1共分散だけでは枝別測定後状態が生じないため、結果枝の非規格化共分散を独立に評価した。

Q1-2の測定統計部分は達成している。M54/R181Aがrank-one統計準備、R164がBorn型状態数と有効自由エネルギーの条件付き起源、R143とR144がBorn分布、同軸反復分布、異軸逐次分布を有限誤差で与える。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。有限局所Hamiltonian統合または有限閉鎖Hamiltonianへの持ち上げ、完全周期、永久記録、reset、周期全体の仕事・熱・エントロピー収支は、Q1-2の達成条件ではなく実装・熱力学的強化課題である。連続matching保存または周期間matching帰還も現行測定統計の必要条件ではない。

R180Aはblock代数と理想共同Born則を厳密に与える。R180Bは採用した開放方程式に対して吸引多様体、有限時間率、作用収支を厳密に与える。R180Cは、M54 holdからprojector latchまでの反作用、block source port、paired-Hopf pump・sink、中央切断、2翼R170、記録、fresh-cell帰還を1つの装置とclockで実現できることを条件に、完全結果誤差とBell監査を合成する。一方、切断面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。

固定目標Q2-2全体は条件付き達成である。範囲は固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則、プロトコル面matchingである。一般状態についてR180Aのblock代数とnode処理は与えるが、一般入力族の一様な高精度Bell receiverまでは主張しない。Q2-2の達成判定はQ2-1の達成状態に依存させないが、根拠模型は独立M48でなくM54の具体的singlet源と実信号を使う。

固定目標Q2-3は条件付き達成である。R181Bをgate列の前に2回使って8mode信号を作り、R181CのA--B、B--C二次生成子と逆演算を同じ永続registerへ作用させる。R177のGHZ--$T$--逆演算ではcoherent出力と完全dephasing出力の全変動距離が $1/(2\sqrt2)$ になる。末端ではM50/R164/R170を含むR181Dを8modeへ特殊化し、Q2-1と同じ末端接続条件が残る。

固定目標Q2-4は条件付き達成である。M54は $2^n$ 受動signal modeを許し、R181Cが局所gateをspectator sectorへ一様にbroadcastする。R181Dはraw容量、正則化作用殻、R170 selector、可逆filter、radial-only repumpを深さ $n$ で合成する。完全結果誤差は入力誤差、$n\delta/(1+\delta)$、$2n(\tau+\gamma)$、node誤差の和で抑える。R178Dは結果相関履歴をspentへ残す境界、R179はblank bank、collision cell、selector/filter work、spent bankを供給する。旧apertureとdyadic tapeは現行因果鎖に使わない。

Q2-4では総bath容量と総熱を多項式としない。signal、work、history、cold、spentの受動容量は指数的でもよい。その代わり、外部program、制御channel、精度、反復回数、総時間を多項式に抑え、指数個の個別address、確率表、回路別配線、稀な成功、事後選別を使わない。この限定は通常の効率的古典simulationではない。

## 9.3 確立していないこと

M54について未導出なのは、pump、transverse sink、template、clockを具体的な有限bath、仕事源、排熱先から導くこと、雑音付き有限時間誤差、揺らぎ散逸関係、準備portの総仕事・熱・エントロピー生成を閉じることである。R181Aは採用した縮約drift後の厳密結果であり、そのdriftの有限閉鎖Hamiltonian持上げではない。

M47について未導出なのは、M54/R181AのW型2モード系の開放portをW型装置へ統合すること、R164の作用容量結合・fiber内平衡化・枝対称性を有限局所Hamiltonianとして構成すること、R162の衝突散乱と信号bath保持controllerを同じ最小有限Hamiltonianへ統合すること、粗視化された有効仕事・熱を全微視的台帳へ持ち上げてpumpからresetまでの全周期ゆらぎ関係へ拡張することである。時間依存傾斜をM37のミクロ位置ばね網から一様誤差付きで導くこと、連続空間極限、多粒子も未完成である。

R180について未導出なのは、M54末端SWAP、projector作用latch、選択block source port、paired-Hopf pump・sink、R162の衝突粒子位置bath、中央切断、fresh cell流を同じ具体装置とclockへ統合することである。採用したR180B方程式を有限bathから導くこと、一般入力族でnode感度を一様に抑えること、総仕事、総熱、総エントロピー生成を閉じることも未完成である。A設定が中央準備へ入るため、空間的に分離した自由設定Bell実験を再現したとはいえない。

Q1-2のZeno部分は未達であり、同一の零傾斜Rabi対照と反復R143/R170測定を接続する必要がある。傾斜による離調固定、障壁増大、駆動停止、摩擦、事後選別をZeno効果とは呼ばない。Q3-2も未達だが、閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を統合する課題として再開する。

Q3-4とQ3-5は条件付き達成である。有限グラフ現象の代数部分はR124、R125で確立し、R181Aはrank-one初期集団の開放準備、R172--R174は局在トークンの有限時間輸送と記録への接続を与える。一方、M54準備port、M37担体、初期作用殻、M42局所辺bath、clock、終位置記録を同じ有限局所装置へ統合していない。最小率の一意なミクロ選択、正則化零極限の一様資源、同一ハードウェアと統一母測度を持つM0、独立同分布型有限標本統計も未完成である。

Q2-1はM54/M50とR112/R161/R162/R164/R170/R181A--R181D、Q2-2はM54/M50/R180 receiverとR112/R161/R162/R164/R170/R181A--R181D/R180A--R180C、Q2-3はM54/M50とR112/R161/R162/R164/R170/R177/R181A--R181D、Q2-4はM54とR112/R161/R162/R164/R170/R181A--R181D/R178D/R179を根拠とする。独立判定は他のQ2目標の達成ラベルを前提にしないという意味であり、同じ親模型と部品定理を共有できる。

Q2-1からQ2-4に共通する一様なハードウェア族は、判定外の実装努力目標として未完成である。同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceを全目標で共有する構成をまだ得ていないが、この未完成性をQ2-1またはQ2-2の達成状態へ遡及させない。

Q2-4で確立していないのは、M54の静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、局所誤差上界を同時に実現することである。cold bathを閉系から生成すること、有限bankで無期限運転すること、使用済みcellを履歴なしにblankへ戻すこと、指数受動容量または総熱を多項式へ削減することも主張しない。

## 9.4 次の決定的検査

Q1-2の次の決定的検査は、同じ総時間の零傾斜Rabi自由対照、測定中もRabi項を止めない有限回測定、flip・reflip・無反応の全履歴、tiltだけの対照を同じ明示的ミクロモデルで比較し、正のZeno抑制余裕が重なり・傾斜・自由発展・1段instrument誤差を上回るかを示すことである。反復回数に伴う時間、記録、fresh cell、エネルギーの増加も同じ台帳で評価する。

これとは別に、M54のpump、transverse sink、template、clockを有限bathへ持ち上げ、R164の作用容量結合、fiber内平衡化、枝対称性と同じW型装置へ統合すること、R162の有限衝突bath、信号bath保持controller、任意軸分析器、傾斜切替、局所記録、枝別テンプレート交換、resetを同じ有限時間Hamiltonian台帳へまとめること、粗視化経路熱力学を周期全体の微視的ゆらぎ関係へ拡張することは、実装・熱力学的強化課題として残る。$\delta\downarrow0$、深いW型、長いfiber準備・混合時間の精度--時間--エネルギー交換もこの強化課題で監査する。

Q2-1とQ2-3の次の検査は、R181Dのcanonical SWAP出口、容量pointer、R164/R170、selector lock、controlled filter、radial repump、recordを共通safe setと単一clock scheduleで閉じることである。Q2-2ではR180CのM54末端SWAP、setting-pre block latch、source port、paired-Hopf pump・sink、R162有限衝突bath、中央切断、2翼controllerを同じ装置とclockへ統合する。Q2-4ではsector漏れ、latch、R170 collision、filter、radial repump、cold floorを同じ安全集合上で同時に抑える。

Q3の次の検査は、M54切断面をM37初期面へ物理的に接続し、初期R164作用殻、M42の局所辺衝突bath、clock、履歴、終位置記録までを同じ有限局所装置へ統合して、誤差台帳と総収支を閉じることである。加えて、採用した最小率を選ぶ具体的装置理由と、節正則化を小さくしたときの資源発散を検査する。Q3-2では、頂点包絡から辺位相と閉路巻数を定義し、零点を避けるhomotopy不変性、エネルギー最小補間、R86細分化安定性、非整数seamの $a^{-1}$ エネルギー発散、節を介した位相すべりを一つの鎖で検査する。R180 receiverの空間分離拡張、R123の連続環境極限、R124・R125の散乱・吸収拡張は、それぞれ固定目標と区別して監査する。
