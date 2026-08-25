# 組版用フォント

このディレクトリの4ファイルは、PDFを再現可能に組版するために収録したNoto JP書体である。ファイル名はTeXテンプレート上の役割を表し、フォント内部のface名とは一致しない。

| ファイル | フォント内部のface名 | SHA-256 | 著作権表示 |
|---|---|---|---|
| `NotoSansJP-Regular.ttf` | Noto Sans JP Thin Regular | `750256672b6ec3d3748ac2c0c6c9b71012b28e7435a6a55577df991acbfad0ff` | Copyright 2014--2021 Adobe, Reserved Font Name “Source” |
| `NotoSansJP-Bold.ttf` | Noto Sans JP Thin Bold | `23e2b749f7402901b3ae2b392bc28f8c05e2c140a3d1741fa982f6c27b34825d` | Copyright 2014--2021 Adobe, Reserved Font Name “Source” |
| `NotoSerifJP-Regular.ttf` | Noto Serif JP ExtraLight Regular | `66cd911fbda31ef7cdd520b1aaf509ee276f4e1c0a73426696715435fc2da218` | Copyright 2017--2024 Adobe |
| `NotoSerifJP-Bold.ttf` | Noto Serif JP ExtraLight Bold | `7094d02f08b72da2c473e0add1f0e166a70b06d2c5b5ab545d2868d4720b58b1` | Copyright 2017--2024 Adobe |

各ファイルはSIL Open Font License Version 1.1で配布される。ライセンス全文は [`OFL.txt`](OFL.txt) を参照する。元の書体情報は[Noto CJK](https://github.com/notofonts/noto-cjk)、配布時のライセンス情報はGoogle Fontsの[Noto Sans JP](https://github.com/google/fonts/tree/main/ofl/notosansjp)と[Noto Serif JP](https://github.com/google/fonts/tree/main/ofl/notoserifjp)で確認できる。

収録ファイルは改変せず、内部メタデータをそのまま保持している。差し替える場合は、face名、著作権表示、ライセンス、ファイル検査値、およびPDFの改ページを再確認する。
