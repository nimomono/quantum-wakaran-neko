# 第2期研究の検算記録

## PR2：全面退役と生成・検算の再構築

- 対象：第1期の論文・付録・結果ID・達成判定の現行からの退役。
- 新正本：`sections/00_purpose_and_scope.md`。
- 物理結果：採用済みの主張0件。これを検算ゼロ件と明示し、旧版の計算結果を新体系へ移植しない。
- 構造検査：章数固定を撤去。第0章から必要な章だけを生成する。
- 検算系：旧版の物理検算を第1期保存ブランチへ移し、新体系の台帳と一致した検算に分離する。
- 組版：`paper.md`、`main.tex`、`paper.pdf`を新本文から再生成する。

GitHub Actionsの実行結果はPR2のChecksを根拠とする。初回の生成物同期が終わる前にPDF生成の完了を主張しない。

## 再現方法

```bash
python tools/check_source.py
python tools/check_project_consistency.py
python tools/run_physics_checks.py
python tools/build_paper.py --output-dir build/ci
python tools/check_generated.py build/ci
python tools/check_latex_semantics.py build/ci/latex/main.log
```

第1期の旧検算結果は[固定コミット](https://github.com/nimomono/quantum-wakaran-neko/commit/5756e7e3aa3dfc1af177f15744b39b1676fad707)で参照する。
