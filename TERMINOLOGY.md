# 論文用語・標準表記

## 1. この文書の目的

この文書は、論文で繰り返し使う専門用語とプロジェクト固有語の標準表記を定める。

本文では、英単語をそのまま説明語として使わない。一般的な日本語の専門用語がある場合はそれを使い、定着したカタカナ語が自然な場合はカタカナで書く。単純な直訳が日本語として不自然になる場合は、英語との1対1対応よりも、物理的または数学的な意味が読者に伝わる表現を優先する。

同じ英単語でも文脈によって意味が異なる場合は、無理に1つの訳語へ統一しない。

この文書は `PROJECT_GUIDE.md` の使用言語規約を具体化する標準表記の正本である。両者が食い違う場合は `PROJECT_GUIDE.md` を優先する。モデルまたは結果に固有の数学的定義は、それを定義する `sections/*.md` を正本とし、この文書は定義そのものを変更しない。

人名、数式記号、略号、モデルID、結果ID、プログラム上の識別子、文献原題は別扱いとし、`PROJECT_GUIDE.md` の規約に従う。

---

## 2. 数学・量子力学

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| ray | 状態方向 | 全体位相または全体倍率を除いて状態の向きだけを指す場合。「射線」は原則使わない |
| state | 状態 | |
| state space | 状態空間 | |
| configuration space | 配置空間 | 数学的な状態空間を指す場合 |
| basis | 基底 | |
| norm | ノルム | |
| trace | トレース | 日本の物理で一般的な表記を優先する |
| rank-one | 階数1 | |
| unitary | ユニタリ | |
| projective | 射影型 | |
| projector | 射影子 | 数学的作用素そのものを指す場合 |
| projector-tree | 段階的射影選別 | 木構造そのものを議論する場合だけ「射影選別木」としてよい |
| tensor product | テンソル積 | |
| tensor-lift | テンソル積状態の生成 | 必要なら「テンソル積空間への写像」とする |
| eigenvalue | 固有値 | |
| eigenmode | 固有モード | |
| low modes | 低位モード | |
| low-2 modes | 最低2モード | |
| cluster | モード群／準位群／部分空間 | 対象に応じて使い分ける |
| dressed | 結合後の／相互作用を取り込んだ | 「ドレスト」を説明なしに多用しない |
| dressed low-2 cluster | 結合後の低2モード部分空間 | 「ドレスト低2準位群」は使わない |
| gap | ギャップ | エネルギー差そのものなら「準位間隔」でもよい |
| spectral gap | スペクトルギャップ | |
| coherent | コヒーレント | 説明文では「位相関係を保った」と書いてもよい |
| coherence | コヒーレンス | |
| dephasing | 位相緩和 | |
| phase | 位相 | |
| current | 確率流／流れ | 確率過程では「確率流」を優先する |
| flux | 流束 | |
| node | 節 | 波動関数や固有モードの場合 |
| graph node | 頂点 | グラフの場合 |
| path | 経路 | |
| branch | 結果成分／結果経路 | 「枝」だけでは書かない |
| branch probability | 結果確率 | |
| branch state | 結果別状態 | |

---

## 3. 確率・測度・統計

`measure` と `measurement` は区別する。`measure` を「測定」と訳してはならない。

ただし、数学的に確率測度を扱っていて、測度論そのものが論点でない場合は、「測度」という抽象語をできるだけ「確率分布」に言い換える。

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| measurement | 測定 | 物理的な観測過程 |
| measure | 測度 | 測度論上の性質そのものが必要な場合 |
| probability measure | 確率分布 | 厳密な測度論が必要な箇所では「確率測度」 |
| distribution | 確率分布／分布 | |
| reference measure | 基準分布 | 一般の測度である必要がある場合だけ「基準測度」 |
| common measure | 共通の確率分布 | 必要なら「共通基準分布」 |
| mother measure | 共通の基準分布 | 「母測度」は原則使わない |
| pushforward measure | 写像後の分布 | 証明で測度論を明示するときだけ「押し出し測度」 |
| conditional measure | 条件付き分布 | |
| conditional probability | 条件付き確率 | |
| ensemble | 試行集団 | |
| moment | モーメント | |
| second moment | 第2モーメント | |
| cross moment | 交差モーメント | |
| sampling | 標本化 | |
| sample | 標本 | |
| seed | 初期状態／初期種 | 乱数そのものなら「乱数種」 |
| seed distribution | 初期分布 | |

たとえば、

- 「同一母測度の前進・後退率」→「共通の確率分布に基づく前進・後退率」
- 「seed測度」→「初期分布」
- 「ray平均」→「状態方向の平均」

のように書く。

---

## 4. 物理系と自由度

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| mode | モード | 日本の物理で定着しているためカタカナでよい |
| signal | 信号 | |
| signal mode | 信号モード | |
| carrier | 信号系／信号自由度 | 「担体」は原則使わない |
| control carrier | 制御用信号系 | |
| spatial carrier | 空間信号系 | |
| bath | 浴 | 必要に応じて「環境自由度」と説明する |
| thermal bath | 熱浴 | |
| finite bath | 有限浴 | |
| Drude bath | Drude浴 | 指数memory kernelを持つ古典調和浴 |
| memory time | 記憶時間 | Drude浴では $\tau_{\rm D}$ |
| rotational diffusion | 回転拡散 | 作用方向の $S^2$ 上拡散 |
| action-partition cell | 作用分配セル | 2作用LC殻を物理セルとして説明するとき |
| action aperture | 作用開口 | collisionの作用しきい値領域 |
| renewal | 再混合／再熱化 | 作用比だけなら「再混合」、浴を含む条件付き平衡なら「再熱化」 |
| environment | 環境 | |
| sector | 部分系／部分空間／領域 | 「セクター」は原則避ける |
| signal sector | 信号部分系 | |
| collision sector | 衝突部分系 | |
| work sector | 作業部分系 | |
| spectator sector | 非作用部分 | ゲートの作用を受けない部分を指す場合 |
| profile | 状態構成 | M54の分類語として使う場合 |
| static profile | 静的状態構成 | |
| spatial-moving profile | 空間移動状態構成 | |
| configuration | 配置 | 数学的または組合せ的な意味に限る |
| configuration profile | 配置状態構成 | 必要なら文脈に応じて簡略化する |
| backend | 物理実装層 | |
| physical backend | 物理実装層 | |
| interface | 接続部／外部接続 | |
| port | 接続端 | |
| canonical port | 正準接続端 | |
| canonical handoff | 正準状態の受け渡し | 「正準受け渡し」は使わない |
| handoff | 受け渡し | 必ず何を受け渡すか明示する |

---

## 5. 装置・記憶・制御

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| register | 記憶部 | 必要なら「状態記憶部」 |
| anti-register | 逆演算用補助記憶部 | 実際の役割に応じて「補助記憶部」と簡略化してよい |
| history register | 履歴記憶部 | |
| cell | 素子 | 「記憶素子」「衝突素子」のように機能を付ける |
| blank cell | 未使用素子 | |
| fresh cell | 未使用素子 | |
| spent cell | 使用済み素子 | |
| bank | 貯蔵部／素子群 | 内容に応じて使い分ける |
| blank bank | 未使用素子群 | |
| cold bank | 低温貯蔵部 | 実際に低温を意味する場合 |
| spent bank | 使用済み貯蔵部 | |
| work | 作業領域 | 計算用自由度の場合 |
| thermodynamic work | 仕事 | 熱力学的仕事の場合 |
| history | 履歴 | |
| latch | 固定機構／保持機構 | 一時保持なら「保持」、結果確定なら「固定」 |
| projector latch | 射影結果の固定機構 | |
| pointer | 指針変数 | 測定器の結果を保持する変数 |
| hold | 保持 | |
| lock | 固定 | |
| selector | 選択機構 | |
| selector lock | 選択結果の固定 | |
| filter | 選別機構 | 光学フィルタ等を実際に指す場合だけ「フィルタ」 |
| controlled filter | 制御付き選別機構 | |
| controller | 制御器 | |
| control channel | 制御経路 | |
| address | 指定先／指定番号 | 内部モードを直接指定する意味なら「個別指定」も使う |
| clock | 時計自由度 | 単なる時刻指定なら「時刻」 |
| schedule | 動作順序／時刻割当 | |
| protocol | 手順 | 「プロトコル」は原則使わない |

---

## 6. 開放系・非平衡過程

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| noise | ノイズ | 「雑音」には統一しない |
| additive noise | 加法ノイズ | |
| phase noise | 位相ノイズ | |
| drift | ドリフト | 確率過程で定着しているためカタカナでよい |
| collision | 衝突 | |
| finite collision | 有限衝突 | |
| collision rate | 衝突率 | |
| transition rate | 遷移率 | |
| matching | 整合 | 単独では意味が弱いため、なるべく対象を付ける |
| rate matching | 遷移率の整合 | |
| distribution matching | 分布の整合 | |
| moving matching | 移動分布の整合 | |
| static matching | 静的分布の整合 | |
| pump | ポンプ | エネルギー供給そのものを強調する場合は「駆動源」 |
| source | 供給源 | |
| sink | 排出先 | |
| repump | 再励起／再調整 | 物理的意味に応じて使い分ける |
| radial | 大きさ方向／動径方向 | 抽象状態空間なら「大きさ方向」の方が分かりやすい |
| radial-only repump | 方向を変えない振幅再調整 | 「動径専用再充填」は使わない |
| transverse | 横方向 | |
| thermal | 熱的 | |
| relaxation | 緩和 | |
| equilibrium | 平衡 | |
| nonequilibrium | 非平衡 | |
| detailed balance | 詳細釣り合い | |

---

## 7. 量子計算・回路

| 原語・旧表記 | 本文の標準表記 | 使い分け |
|---|---|---|
| gate | ゲート | 日本語として定着している |
| gate sequence | ゲート列 | |
| control | 制御 | |
| control pulse | 制御パルス | |
| switch | 切替 | |
| ramp | 緩やかな切替／ランプ | 技術的定義が必要な場合だけ「ランプ」 |
| bit | ビット | |
| qubit | 量子ビット | |
| input | 入力 | |
| output | 出力 | |
| readout | 読出し | |
| reset | リセット | |
| program | プログラム | |
| compile | コンパイル | |
| compiler | コンパイラ | |
| resource | 資源 | |
| operational resource | 外部運用資源 | |
| internal resource | 内部資源 | |
| black-box | ブラックボックス | |
| black-box operational equivalence | ブラックボックスとしての運用上の同等性 | 初出で定義した後は「運用上の同等性」と略してよい |
| sampling | 標本化 | |
| postselection | 事後選別 | |

CNOT、CHSH、SWAP、SU(2)など、分野で定着した略号はそのまま使う。

---

## 8. プロジェクト固有の複合語

英語をハイフンで連結したプロジェクト固有語は、原則として本文では使わない。

| 旧表記 | 標準表記 |
|---|---|
| static profile | 静的状態構成 |
| spatial-moving profile | 空間移動状態構成 |
| tensor-lift | テンソル積状態の生成 |
| projective-node | 共通射影選別機構 |
| projector-tree | 段階的射影選別 |
| canonical handoff | 正準状態の受け渡し |
| finite collision | 有限衝突 |
| finite switch | 有限時間切替 |
| dressed low-2 cluster | 結合後の低2モード部分空間 |
| control carrier | 制御用信号系 |
| spatial carrier | 空間信号系 |
| physical backend | 物理実装層 |
| fresh-cell | 未使用素子 |
| blank bank | 未使用素子群 |
| spent bank | 使用済み貯蔵部 |
| selector lock | 選択結果の固定 |
| controlled filter | 制御付き選別機構 |
| radial-only repump | 方向を変えない振幅再調整 |
| additive noise | 加法ノイズ |
| extensive additive noise | 全自由度に加わる加法ノイズ |
| setting-pre | 設定先行 |
| setting-pre receiver | 設定先行受信機構 |
| paired-Hopf receiver | 2端Hopf受信機構 |
| setting-pre paired-Hopf receiver | 設定先行2端Hopf受信機構 |
| moving specialization | 移動型への特殊化 |
| static specialization | 静的型への特殊化 |

`paired-Hopf` のようにプロジェクト固有の物理機構を指す名称は、定義を失わない範囲で本文の説明に合わせてさらに改名してよい。

---

## 9. 直訳を避ける語

次の訳語は意味は通じても、日本語本文では分かりにくいため原則使わない。

| 避ける表記 | 代わりに使う表記 |
|---|---|
| 射線 | 状態方向 |
| 担体 | 信号系／信号自由度 |
| 枝 | 結果成分／結果経路 |
| 射影子木 | 段階的射影選別 |
| 正準受け渡し | 正準状態の受け渡し |
| ドレスト低2準位群 | 結合後の低2モード部分空間 |
| 母測度 | 共通の確率分布／共通基準分布 |
| ラッチ | 固定機構／保持機構 |
| レジスタ | 記憶部 |
| セル | 素子 |
| セクター | 部分系／部分空間／領域 |
| プロトコル | 手順 |
| バックエンド | 物理実装層 |
| キャリア | 信号系／信号自由度 |

---

## 10. 人名と略号

人名に由来する語は `PROJECT_GUIDE.md` の規約に従う。

たとえば、

- Bell の定理
- Born 則
- Bloch 球
- Rabi 振動
- Zeno 効果
- Nelson 流
- Newton 則
- Tsirelson 限界
- Wallstrom 問題

のように、人名部分を固有名として扱う。

CNOT、CHSH、SWAP、SU(2)、Q1、Q2、Q3、M37、M54、R164などの略号・識別子は原表記を保つ。

---

## 11. 運用原則

新しい英語表現を本文へ導入するときは、次の順で表記を決める。

1. 日本の物理・数学で一般的な日本語訳があるなら、それを使う。
2. 定着したカタカナ語なら、カタカナを使う。
3. 直訳すると意味が分かりにくい場合は、対象の物理的役割を日本語で説明する。
4. プロジェクト固有語は、英語の形を保存することより、何をするものか分かる名前を優先する。
5. 同じ英単語でも異なる物理的役割を持つ場合は、文脈ごとに訳し分ける。
6. 数学的厳密性を失わない範囲では、「測度」より「確率分布」、「担体」より「信号系」のように、学部生が読んで意味を取りやすい語を優先する。
7. 訳語を変更した場合は、本文、付録、README、PROJECT_STATUS、検算器の文字列を同時に確認する。
