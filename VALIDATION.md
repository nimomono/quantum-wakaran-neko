# 検算と品質確認

## 数式検算

実行コマンド：

```bash
python3 tools/verify_two_mode_ledger.py
```

固定 seed `20260724`、sample count `600000` で全項目が合格した。

| 項目 | 誤差 | 許容値 |
|---|---:|---:|
| two-mode uniform CDF の KS 誤差 | 0.00115444 | 0.003 |
| difference action の最大絶対誤差 | $1.33\times10^{-15}$ | $2.0\times10^{-14}$ |
| clock canonical one-form の最大絶対誤差 | $3.55\times10^{-15}$ | $2.0\times10^{-14}$ |
| terminal half-space と時計向き条件の不一致率 | 0 | 0 |
| orientation average no-go identity の誤差 | 0 | $1.0\times10^{-15}$ |
| Bell joint probability の最大誤差 | 0.00044900 | 0.0025 |
| no-signalling marginal error | 0 | 0.0025 |
| multi-mode CDF の最大誤差 | 0.00133542 | 0.0025 |
| CHSH identity error | 0 | $1.0\times10^{-14}$ |

## LaTeX

- XeLaTeX 3 pass：成功。
- undefined citation：なし。
- undefined reference：なし。
- overfull box：なし。
- PDF page count：88。
- page size：A4。

残る warning は Latin Modern Mono の bold shape fallback と、長い英語参考文献行の underfull box のみであり、内容欠落または clipping を生じない。

## PDF visual QA

88ページ全てを PNG へレンダリングし、contact sheet と主要ページの高解像度表示で確認した。

- title page：欠落なし。
- table of contents：全章と付録を収録。
- 本文の相補的内部時計による terminal half-space の正準実現：数式、命題、改ページに欠落なし。
- `[R]` の条件付き二境界 matching と orientation average no-go：数式、表、結論に欠落なし。
- 付録Cの clock Hamiltonian、canonical transformation、matching measure、no-go：数式切れなし。
- equations：clipping、black square、重なりなし。
- proof-status table：page width 内。
- bibliography：40件、URL 表示を確認。
- header、footer、page number：全ページで整合。

## 再現性

`paper.md` と `main.tex` は `sections/` から `tools/build_paper.py` で再生成される。`compiled_paper.pdf` と `output/pdf/nelson_boundary_bell_complementary_clock_revision.pdf` は同一内容である。
