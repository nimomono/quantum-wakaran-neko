# 置換・退役結果索引

この表は現行本文から外した結果への最小索引である。数式と証明は重複掲載せず、Git履歴と個別メモを正本とする。

## 退役した固定目標

| 旧目標 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| 旧Q2-3「有限回路の機能的再現」 | 任意の固定有限回路を $2^n$ 直接モード担体で有限合成し、末尾だけで読出す | 固定目標から削除。3量子ビット型二段ゲート合成を新Q2-3とし、直接モード構成はQ2-4の候補技術として資源監査を継続 | draft-60の本文、Git履歴、現行Q2-4 |
| 旧Q2-5「自律非平衡計算と平衡化運命の決定不能性」 | 白石--松本型の停止問題埋込みを局所古典開放系へ移す | 固定目標から削除し、量子出力サンプリングとは独立の研究線として保存。Q2-5のIDは再利用しない | draft-60の本文、Git履歴 |

退役は反証を意味しない。現在の固定目標と混同せず、必要な場合だけ独立研究線として再開する。

| 結果 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| R70--R72、R77、R78、R91 | M35作用区間によるBorn型長期頻度 | 確率源として退役。M50/R164へ一本化 | `superseded_m35_born_sampler.md` |
| R107--R111、R121 | M41 Bell周期 | M48/R151--R156、R166、R170へ置換 | `superseded_m41_bell_cycle.md` |
| R147、R153、R155 | 独立M48 setting-pre paired-Hopf Bell周期 | M52の実際の1試行末端信号を受けるR180A--R180Cへ置換 | `superseded_independent_m48_bell_protocol.md`、draft-65のGit履歴 |
| R113--R118 | 旧M42連続粒子位置閉包 | 旧結果は退役。現行Q3は再定義M42/R172--R174へ再編 | `superseded_m42_continuous_particle_position.md`、付録N |
| R127--R129 | M45開放準臨界準備 | Q1--Q3と独立の研究線 | `independent_m45_open_quasicritical_preparation.md` |
| R130--R132 | M46のcapacity・半減衰・主モード計算 | 現行本文から退役。再検討用の有限次元計算 | `rejected_m46_current_transducer.md` |
| R133、R134 | M46 current恒等式と条件付きNelson恒等式 | 現行因果鎖では不採用 | `rejected_m46_current_transducer.md` |
| R137、R138 | M47旧連続matching保存と逆設計 | R161/R162/R170の操作面再平衡化へ置換 | `superseded_m42_continuous_particle_position.md` |
| R150 | 抽象matching下のBell有限誤差系 | R155証明内の統計補題へ吸収 | Git履歴 |
| R152 | M48局所matching生成子 | R161の $m=2$、$\Psi=\Phi$ 特殊化へ吸収 | R161、R162 |
| R165 | M49中央4枝とM35作用区間の同値性 | M35側を退役し、M49中央4枝をR164の直接特殊化としてR159入力準備節に保持 | R159、R164 |
| R159 | M49の入力準備、同期CNOT、固定有限共同入力--出力統計 | 固定benchmarkの代数は撤回しないが、4モード共同担体を現行Q2-1に採用せず退役 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| R160 | M49固定singletからM48へのsetting-free同一register受渡し | M49の退役とともに現行模型間接続から外した。Q2-2はM48内部seedで独立に維持 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| R175 | draft-63 M52の有限coherent経路和代数 | R176Bのunitary診断展開へ吸収。経路限定設計と独立の物理分岐器を主結果鎖から外す | `superseded_m52_path_only_design.md`、draft-63のGit履歴 |
| R169 | 固定全作用高階数読出し | 安全事象を含む一般ray平均定理R168へ吸収 | R168 |
| R89 | 隣接2モード回路による有限unitary合成 | R112の有限合成節へ吸収 | R112、付録A |
| R90、R97--R99 | 有限時計、比較・無反応、結果別SWAP、記録・逆計算 | R112の制御・比較・記録回路へ吸収 | R112、付録A |
| R83--R85、R87、R88 | M37の局所包絡、生成子誤差、作用比診断 | R86の節と有限基底分布系へ吸収 | R86、付録E |
| R136、R141 | W型占有振動と傾斜保持 | W型2モード制御定理の節へ吸収 | R140、付録B・H |
| R139、R167 | 2次元Bloch縮約とM37第2モーメント持上げ | 共通信号集団の正確・有限誤差輸送へ吸収 | R135、付録F |
| R142 | W型有限コントラスト読出し | M47読出し・状態更新定理の補題へ吸収 | R143、付録B |
| R104、R105、R106 | 4モード担体の操作代数、CNOT流、有限時間安定性と資源 | R112の4モード/CNOT特殊化へ吸収 | R112、付録C |
| R157、R158 | M49入力準備と担体・bath・粒子位置の同期CNOT | R159の入力準備節・同期CNOT節へ吸収 | R159、付録C |
| R163 | 粗視化粒子位置過程の経路確率比、積分ゆらぎ関係、相対有効仕事 | R161・R162から従う無番号の粗視化経路熱力学系へ変更 | 第2章、付録K |
| R146 | 積bath標本の直接singlet支持の不可能性 | R147の必要性を示す番号なし否定命題 | 付録I.2 |
| R148、R151 | singlet交差モーメントと安全盆routing | M48設定前・切断面準備へ吸収 | R153、付録D・I |
| R149、R154、R156、R166 | 理想Bell応答、2翼局所合成、帰還、条件付き因子化 | 完全Bell周期の節と補題へ吸収 | R155、付録D・I・J |

## 吸収済みモデルID

| モデル | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| M43 | 固有モード作用結合型有限環境 | 独立モデルから外し、R123の有限環境純位相緩和構成へ吸収 | R123、付録G |
| M35 | 作用区間によるBorn型標本器と有限正準制御補助 | 確率生成部は退役し、非確率的な制御・比較・記録部はR112へ吸収 | `superseded_m35_born_sampler.md`、R112、付録A |

## 退役したモデルID

| モデル | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| M49 | 4モードprogram担体、行分解bath、二粒子位置によるQ2-1 CNOT供給 | 固定benchmarkは撤回せず退役。4mode自体でなく入力別template、外部routing、破壊的decode、閉じないinterfaceを不採用とし、Q2-1はM52/R176A--Cへ再構築 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| M48 | 独立setting-pre paired-Hopf Bell protocol | paired-Hopf機構とBell監査はR180へ継承し、独立fair seedと集団交差momentを現行sourceから外す。Q2-2はM52/R180 receiverへ置換 | `superseded_independent_m48_bell_protocol.md`、draft-65のGit履歴 |

結果番号は再利用しない。現行結果の番号を詰めず、履歴参照を安定させる。
