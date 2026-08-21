# 研究メモ一覧

`notes/` は、現行論文へ収録しないが再利用価値のある研究記録を置く。各メモは旧章の複製ではなく、不採用理由、移動理由、現行理論での位置づけ、再検討条件が分かる形へ整理する。`paper.md`、`main.tex`、`paper.pdf` の生成対象には含めない。

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

完全な旧原稿は版タグと公開版で保存し、ここには置かない。

不採用モデルの数値コード、設定、生出力は`notes/`へ複製しない。旧パス、最終収録版、対応コミット、主要結果を研究メモへ記録し、完全な実装はGit履歴から参照する。
