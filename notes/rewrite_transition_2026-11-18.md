# 第1期研究から第2期研究への移行記録（2026-11-18）

## 第1期研究の固定点

- repository: `nimomono/quantum-wakaran-neko`
- default branch at capture: `main`
- captured commit: `5756e7e3aa3dfc1af177f15744b39b1676fad707`
- archival branch: `archive/pre-rewrite-2026-11-18`
- archived browser URL: https://github.com/nimomono/quantum-wakaran-neko/tree/archive/pre-rewrite-2026-11-18

このスナップショットは、旧 `sections/` 全体、`paper.md`、`main.tex`、`paper.pdf`、`tools/`、`simulations/`、`notes/`、旧管理文書を含む元のGitツリーをそのまま参照する。退役は、旧版の各恒等式が誤りだったことを意味しない。

## 移行方針

新体系は [rewrite/README.md](../rewrite/README.md) を入口とし、旧M/R/Q番号、旧版の固定目標・達成状態、旧版の因果鎖・模型依存関係を前提にしない。旧版の成果を再利用する際は元の条件と証明を再検証してから新体系へ登録する。

第1段階では旧版の生成・検算環境をあえて変更せず、旧版の閲覧可能性を維持する。第2段階で旧原稿を現行から外し、公開本文・生成ツール・CIを新体系へ切り替える。

作業計画は [rewrite/MIGRATION_PLAN.md](../rewrite/MIGRATION_PLAN.md) を参照。
