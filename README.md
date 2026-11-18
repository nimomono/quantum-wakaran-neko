# quantum-wakaran-neko

量子、なんもわからん。

## 第2期研究（現行）

**研究再構築中。現在の原稿は研究目的と判定基準のみを収録し、量子力学の導出や個別現象の達成をまだ主張しない。**

古典的な微視的力学・準備・環境・観測・統計的縮約から、量子型構造の成立条件と限界を検証する。粒子、場、有限浴、開放系のどれを基礎とするかは、証拠を比較して決める。

- [現在の論文原稿](paper.md) / [組版PDF](paper.pdf)
- [本文の正本](sections/00_purpose_and_scope.md)
- [研究の目的と立場](PROJECT_STANCE.md)
- [現行の到達状況](PROJECT_STATUS.md)
- [主張と根拠の台帳](rewrite/CLAIM_LEDGER.md)
- [研究・執筆・検算の規約](PROJECT_GUIDE.md)
- [旧版からの移行記録](rewrite/MIGRATION_PLAN.md)

## 第1期研究（退役・保存済み）

2026年11月18日に、第1期研究の本文・付録・結果体系・達成判定を**現行の正本から全面退役**した。これは当時の個々の計算が誤りであることを意味しない。過去の証明、候補模型、数値実験、PDF、検算コードは固定したコミットから引き続き参照できる。

- [第1期研究の完全な保存ブランチ](https://github.com/nimomono/quantum-wakaran-neko/tree/archive/pre-rewrite-2026-11-18)
- [保存対象の固定コミット](https://github.com/nimomono/quantum-wakaran-neko/commit/5756e7e3aa3dfc1af177f15744b39b1676fad707)
- [第1期から第2期への移行記録](notes/rewrite_transition_2026-11-18.md)

第1期のM/R/Q番号、個別の達成判定、模型の依存関係は新体系へ自動継承しない。再採用する結果は条件・証明・実装を独立に検証してから台帳へ登録する。

## 開発・再生成

```bash
python tools/check_source.py
python tools/check_project_consistency.py
python tools/run_physics_checks.py
python tools/build_paper.py
```

`sections/`が原稿の正本で、`paper.md`・`main.tex`・`paper.pdf`は生成物。通常CIは検証のみ行い、生成物更新はPRブランチに対する手動「生成物同期」を使用する。
