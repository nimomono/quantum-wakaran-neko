@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、量子計算機をブラックボックスとして見たときと同種の回路入力を受け、量子回路の出力分布を再現し、そのための外部program、制御channel、時間、精度、試行回数を多項式に抑える古典装置を構成できるかである。内部の受動自由度数と外部から装置を使うための複雑度を区別し、内部の指数構造が外部interfaceへ指数costとして露出するかを判定する。

その物理的な基礎として、明示的な古典力学モデルから量子力学に似た可逆操作、Born型測定統計、結合ゲート、空間伝播、Bell型統計を構成できる範囲も調べる。有限閉鎖Hamiltonianモデルと開放古典モデルを区別し、採用方程式後の厳密結果と、その方程式自体のミクロ導出を分ける。

物理的な導出の主線を、M37の実振動子運動からW型の低2モードを経てQ1の制御運動へ進む経路とする。第6章の静的R86、第3章の射影内R140、両者を接続する条件付き系を区別する。Q1の既存正準実装の達成は維持し、制御された位置ばね実装の任意精度構成は追加の強化課題として管理する。準備・枝選択・記録とQ2の共同担体は、担体運動だけからは従わない。

M54をQ1・Q2・Q3の共通signal--configuration親模型族とする。完全状態は有限実正準register、source/template port、anti/work、raw・regularized容量、selector、collision cell、cold/spent bank、記録、clockを含む。R181Aは物理template準備、R181Bは固定入力tensor-lift、R181Cは永続register gate、R181DはR170駆動projector-treeを与える。複素信号は実担体の派生表示、rayと分布は解析上の統計量である。

各試行の有限正準signalからR164が共通条件付き分布 $\pi_i^\delta(v)$ を与え、R161がconfiguration matchingを、R162が有限collision実装を与える。Q1/Q2のstatic profileでは $j=0$ の再平衡化をR170でlock・記録し、Q3のspatial profileでは $j\neq0$ のmoving matchingとして同じ粒子を輸送する。二乗形の状態依存性はM54の第2モーメントに現れ、排他的結果または位置過程は同じ単一試行signalから作る。R112は有限正準制御、安全比較、SWAP、記録、逆計算を担うが、独立のBorn型枝生成には使わない。

Q1はM54 W2 static profileとQ1 W型2モードprotocolを使う。R187はM37の弱結合W型最低2正常modeをM54 W2 signal subsystemへcanonical同定し、R140の有限 $SU(2)$ 制御を任意精度で物理carrierへ持ち上げる。M54/R181AのW型2モード特殊化が入力rayを準備し、共通R135がBloch球型統計状態空間と集団輸送を与える。R140は射影内の任意 $SU(2)$ 操作、Rabi型占有振動、傾斜保持を与える。R143は共通R170へW型分析器、有限コントラスト、結果別テンプレート交換を加えた1段instrumentである。R144はR143を固定有限回合成し、無反応を含む完全履歴、同軸反復分布、異軸逐次分布と有限誤差和を与える。可逆操作と測定統計部分は導出済みである。Q1-2全体は、同一の零傾斜Rabi対照と有限回反復測定を接続するZeno部分が未達であるため部分達成とする。永久記録、補助逆計算、交換reset、周期総収支はR144の外に置く実装・熱力学的強化課題である。

Q2-1はM54の受動的な4mode信号、anti-register、work、clock履歴を同じ永続状態bathへ保持する。R181Bは一般積入力の可逆tensor-lift、R181Cは同一register上のCNOT、局所操作、逆演算、参照系安定な有限誤差合成、R181Dは末端Born型instrument接続を与える。R181Dの容量pointer--作用殻境界、有限fiber混合、記録までの一体化を条件としてQ2-1は条件付き達成である。Q2-2は独立の目標として、M54の実際の1試行末端信号をR180Aのsetting-pre block receiverへ渡し、R180Bのpaired-Hopf流で2翼templateへ有限時間整列させる。R180Cは、切断後の2つの局所R170、条件付き積因子化、Born共同分布、非信号性、CHSH不等式の破れ、Bell前提監査、fresh-cell帰還を、単一装置統合を条件としてまとめる。固定singlet、固定有限設定族、準備先行、非空間分離、採用開放法則の範囲でQ2-2は条件付き達成である。

Q2-3はR181Bをgate列の前に2回適用して8mode信号を作り、R181CのA--B、B--C二次生成子を同じ状態bathへ順に作用させる。R177はGHZ--$T$--逆演算のcoherent分布と完全dephasing分布が全変動距離 $1/(2\sqrt2)$ で分かれることを示す。R181Dと同じ末端一体化条件の下で条件付き達成である。

Q2-4はM54の一般 $n$ 特殊化である。R181Cは局所gateのsector一括作用、R181DはR170駆動の逐次projector-treeを与える。各nodeはraw容量、正則化作用殻、selector lock、可逆filter、radial-only repumpを使い、無反応を完全結果へ残す。R178Dはhistory掃除の限界、R179はblank bank、collision cell、spent bankの一様供給を与える。R186は、疎な静的製造誤差、独立mode phase noise、projector latchの相対係数誤差が指数sector数を直接加算せず抑えられる条件と、各modeへ独立に作用を注入するadditive noiseが指数noise suppressionを要求する障害条件を分離する。指数的な受動信号・work・history・cold・spent容量と総熱を許し、外部program、制御channel、精度、反復回数、総時間を多項式に抑えるblack-box operational規則の下で、Q2-4を条件付き達成とする。総物理資源が量子計算機と同程度であることは主張しない。

Q3はM54のspatial-moving profileである。共同測度 $\mu_t(dX\,dZ)$ 上で、R164と同じ条件付き位置分布を一般R161のmoving specializationが全時刻保存し、rank-one集団ではR135から正則化Born分布を得る。M37はR86によりM54 spatial signal sectorを局所位置ばねで有限時間近似する。R184はM37開始面の作用をlatchして正則化背景を固定し、rate・位置分布・R162 generic collision実装の誤差を与える。R185はR161の同一path-measure backward rateから $D_\pm$ を作り、1次元node-free sectorで時間対称Newton則を $O(a^2)+O(\delta)$ まで導く。finite collisionから対称加速度への誤差が残るためQ3-2は部分達成、Q3-6は未達である。Q3-3A--Q3-3Cは達成、Q3-4A・Q3-4B・Q3-5は単一装置統合を条件に達成である。

Q1・Q2・Q3は同じM54模型族の異なるprofileから派生する。M37はQ3 spatial signalに加えR187条件下のQ1 W2 control carrierも実装するが、pump、作用殻、collision bath、記録まで同一装置になったわけではない。全規模で同一の製造済みハードウェアまたは同一パラメータを使うところまでは主張しない。各固定目標は明記した根拠結果から独立に判定する。R180Cのreceiver内部統合、Q2共通ハードウェア族、Q1--Q3を1つの周期へ統合するM0はいずれも未完成である。