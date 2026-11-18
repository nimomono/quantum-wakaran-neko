# 第2期研究の生成・検算ツール

旧版の全verifierと移行検査は[固定した第1期研究](https://github.com/nimomono/quantum-wakaran-neko/tree/archive/pre-rewrite-2026-11-18)に保存した。新体系で採用済みの物理結果はまだなく、現行のrequired物理verifierはゼロ件である。

- `paper_source.py`：`sections/NN_*.md`を番号順に検査・収集する（固定章数なし）。
- `build_paper.py`：`paper.md`、`main.tex`、`paper.pdf`を生成。
- `check_source.py`：現行原稿の基本構造と旧理論ID混入を検査。
- `check_project_consistency.py`：主張台帳の空状態を機械的に検査。
- `run_physics_checks.py`：新体系の物理verifierを実行。ゼロ件ならその状態を明示。
- `check_generated.py`：生成物同期を検査。
- `check_latex_semantics.py`・`lint_typeset.py`：LaTeX異常・組版警告を分離。
- `test_validation_policy.py`：通常CIのread-only性と生成物同期の権限を検査。

```bash
python tools/check_source.py
python tools/check_project_consistency.py
python tools/run_physics_checks.py
python tools/build_paper.py
```

PRの生成物同期はdefault branchで管理される`.github/workflows/sync-paper.yml`を手動実行し、対象branchを指定する。旧版から残る`notes/`・`simulations/`は新体系での検算対象ではない。
