# PR2：第1期本文の全面退役と第2期の正本への切り替え

- 旧版の固定コミット: `5756e7e3aa3dfc1af177f15744b39b1676fad707`
- 保存先: https://github.com/nimomono/quantum-wakaran-neko/tree/archive/pre-rewrite-2026-11-18
- 第2期の正本: `sections/00_purpose_and_scope.md`

本PRでは以前の`sections/`の34ファイルすべてをactive treeから外し、旧版の専用物理verifierを現行CIから退役する。歴史的な`CHANGELOG.md`、`notes/`、`simulations/`は手を加えず、その時点の研究史として残す。

結果番号・模型番号・達成判定は新しい状態表へ転記しない。新体系にはまだ物理的な確定結果がなく、現行CIでrequired科学検算が0件と表示されることを意図している。

旧版の論文・付録・検算が無くなったのではなく、上記固定コミットから検証・復元できる。新しい原稿は過去の実装に拘束されない。

生成物はPRブランチで手動「生成物同期」を実施してからマージする。同期前に古いPDFが残っている状態を新しい公開状態とはみなさない。
