# 研究メモ一覧

`notes/` は、現行論文へ収録しないが再利用価値のある研究記録を置く。通常は旧章の複製でなく、不採用理由、移動理由、現行理論での位置づけ、再検討条件が分かる形へ整理する。M41の2文書だけはR107--R111、R121の式と証明を同じtreeで監査できるよう、draft-45Aの章・付録本文へ置換済み注記を加えて保存する。いずれも `paper.md`、`main.tex`、`paper.pdf` の生成対象には含めない。

draft-51以後の現行文書では、各試行で局在する物理変数を「粒子位置」と呼ぶ。変更記録と本フォルダーにある旧版メモの「実現配置」は、当時の用語と因果模型を追跡できるよう履歴として保持し、現行定義へ読み替えない。

| メモ | 元の版・移動元 | 現在の位置づけ | 移動理由 |
|---|---|---|---|
| `project_sources_key_results.md` | プロジェクト情報源からの統合前抽出 | 統合前メモ | 現行本文との整合性が未確認 |
| `superseded_terminal_function_model.md` | draft-11 第5〜8章、付録C | M11の不採用記録 | Bell 固有の終端統計入力を必要とし、共通作用殻モデルで置き換えた |
| `rejected_forward_weighting_models.md` | draft-10 第7.10節、第8.5節、第8.9節、付録C.11 | M12の不採用記録 | 順時間的共有浴と待ち時間は Bell 試行頻度を作らない |
| `complementary_terminal_halfspaces.md` | draft-10 第8.4節、付録C.4 | M12の不採用記録 | 相補半空間の等重み平均は余弦項を消す |
| `gaussian_nelson_examples.md` | draft-10 第2.6節、付録D | M3と補助計算 | 主定理と現行 Bell 論証を実質的に支えない |
| `measurement_dependence_comparisons.md` | draft-10 付録E.1〜E.3 | 表現論的比較 | Bell の前提監査は本文だけで完結し、最適化比較は中心論証に不要 |
| `rejected_bell_causal_alternatives.md` | draft-27 第7章、付録B.12〜B.16、付録D、およびM40設計検討 | M30、M33、M36、M40の不採用記録 | M41初期共通原因型と因果仮定が異なるため、旧論証を本文から分離した |
| `superseded_position_coupling_fisher_closure.md` | draft-13 第2〜4章 | M13の不採用記録 | 力密度閉鎖を、運動量結合から配置拡散へ進む直接経路で置き換えた |
| `superseded_three_mode_bell_shell.md` | draft-12〜draft-15 第6〜7章、付録C | M7〜M9の不採用記録 | 比較作用を直接読む2モード境界殻へ置き換えた |
| `superseded_two_component_induction_field.md` | draft-15〜draft-19 第2〜3章、付録A・D〜F | M14、M20〜M25の不採用記録 | 実在2成分誘導場を有限正準位相担体の相関行列力学へ置き換えた |
| `rejected_m44_capture_entropy_preparation.md` | draft-39・draft-40 第8.13節、付録H、R126 | M44の不採用記録 | 有限Hamiltonian候補から基準位置拡散、時間比例準備率、自律再生、周辺可逆性を同時導出できず、開放M45へ置換した |
| `rejected_m46_current_transducer.md` | draft-42 第8.14節、付録I、R130--R134 | M46の不採用記録。R130--R132は補助結果として一部保持 | 場からrateを作って実現配置を動かす因果律が、複素振幅を実現配置--浴共同統計として定義するM47と両立しない |
| `independent_m45_open_quasicritical_preparation.md` | draft-52までの第8.13節、付録H、R127--R129 | Q1--Q3と独立の開放準臨界準備研究線 | 固定入力時刻の有限枝読出しを与えず、現行Born型主線の準備問題と確率生成機構を分離するため |
| `superseded_m35_born_sampler.md` | draft-52までの付録A、R70--R72、R77、R78、R91、R165の一部 | M35旧Born型標本器の退役記録 | 確率生成をM50/R164/R170へ一本化し、M35を有限正準制御補助へ限定するため |
| `superseded_result_index.md` | draft-53で本文から外した結果ID | 旧結果IDと現行統合先の索引 | 統合後の本文と状態表へ旧IDを混在させず、追跡可能性を保つため |
| `superseded_m38_m42_q1.md` | draft-43以前の第3章、付録B、M38、R92--R100、R119 | 旧Q1操作・測定模型の置換記録。R97--R99は一般装置補題として一部保持 | Q1をW型2モード共同統計と傾斜測定を使うM47/R139--R144へ移行した |
| `superseded_m42_continuous_particle_position.md` | draft-51までの第2章、第6章、付録F、M42、R113--R118 | 旧全時刻等変粒子位置模型の退役記録 | Q3読出しをR167--R170の固定入力時刻M37--M50 instrumentへ移行し、確率起源と装置論をM50へ統一した |
| `frozen_q1_zeno.md` | draft-43以前の第3章、付録B、R101--R103 | Q1-4と旧有限Zeno構成の凍結記録 | M47測定へ接続する手順を今回構成せず、傾斜による離調固定をZeno効果と区別するため |
| `superseded_m41_bell_cycle.md` | draft-45A以前の第5章、M41、R107--R111、R121 | 旧初期共通原因型2端Bell周期の置換記録 | M48のpaired-Hopf receiver、2翼strong matching、切断後局所instrument、resetへ主線を移し、因果律の異なる旧周期を現行根拠から外した |
| `superseded_m41_cycle_proofs.md` | draft-45A以前の付録D | M41周期の旧証明記録 | R107--R111、R121を撤回せず保存する一方、現行Q2-2の証明依存から外すため |
| `superseded_m39_m48_handoff_claim.md` | draft-45BのR151、旧第4.9節・第5.3節・付録D.2・付録J.14 | 旧M39--M48 state handoff主張の置換記録 | 反対称filterが非零入力を同じsinglet射影へ潰し、等重み枝も内部fair seedで代替できるため、物理的なstate-carrying受渡しと分類できない |
| `superseded_m39_m42_q2_1.md` | draft-46以前の第4章、付録C、M39、R118・R120・R122のQ2-1適用 | 旧Q2-1模型の置換記録。R104--R106はM49内部へ再利用 | Q2-2へ必要な2端bath・配置registerを供給せず、付録Kの同一試行受渡し契約を満たさないため |

完全な旧原稿は版タグと公開版で保存し、ここには置かない。

不採用モデルの数値コード、設定、生出力は`notes/`へ複製しない。旧パス、最終収録版、対応コミット、主要結果を研究メモへ記録し、完全な実装はGit履歴から参照する。
