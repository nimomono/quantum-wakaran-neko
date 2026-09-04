# 検算と品質確認

この文書はdraft-66のM52駆動R180 setting-pre paired-Hopf receiver、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-09-04。過去版の検証記録は後半に保存する。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python -m py_compile tools/*.py
for script in tools/verify_*.py; do python "$script"; done
python tools/build_paper.py
```

主要検算器を個別に実行するときは次を使う。

```bash
python tools/verify_common_canonical_control.py
python tools/verify_common_collision_thermodynamics.py
python tools/verify_m51_common_open_preparation.py
python tools/verify_m42_spatial_token.py
python tools/verify_q1xq1_common_bath.py
python tools/verify_q2_shell_and_locality.py
python tools/verify_r180_m52_receiver.py
python tools/verify_r180_bell_cycle.py
python tools/verify_common_signal_m50.py
python tools/verify_r178_uniform_sampler.py
python tools/verify_r179_uniform_supply.py
python tools/verify_q2_m53_composition.py
```

## draft-66方針監査

- Q2-2の根拠模型を独立M48からM52、M50、R180 receiverへ置換した。固定目標の文言と条件付き達成判定は維持し、R180Cのreceiver内部単一装置統合を条件として明記した。
- M52の固定singlet gate列を設定生成前に完了し、R176B後の実際の1試行末端信号 $V$ をR180へ渡す。試行集団交差momentまたは $G_S$ を終端共役信号へ再利用しないことを本文、付録、CIで固定した。
- R180Aの行優先block $w_{s,x}=D^{\mathsf T}\overline{u_{s,x}}$ がprojector作用、枝重み、B縮約状態、共同Born則を同時に与えることを検査した。一般状態の小作用blockは無反応に残し、固定singletでは枝作用 $1/2$ によりnode切断がない。
- R180Bの標準source loadを $z_A(0)=a$、$z_B(0)=w_{s,x}$ とし、安全枝では $m_0\geq(1+\sqrt\tau)/2>0$ が従うようにした。paired-Hopf吸引の非零bright seedを独立仮定にしない。
- R180Cの誤差台帳では中央branch形成、block保持、paired-Hopf整列、局所正則化・混合、R170残差、記録、clockを1回ずつ数える。CHSH閾値と非信号周辺差を無反応込みの完全結果空間で評価する。
- 旧M48、R147、R153、R155は現行結果鎖から退役し、paired-Hopf機構とBell監査だけをR180へ継承した。旧ファイル、旧検算器、現行表への旧根拠列が残らないことをCIで検査した。

## draft-66再現計算

- Python構文検査と18本の `tools/verify_*.py` を実行し、すべて正常終了した。
- `verify_r180_m52_receiver.py` の12項目で、M52 singlet gate列、行優先block、projector作用、枝完全性、B縮約状態、共同Born則、node上界、規格化感度、singlet spin-flip特殊化を検算した。
- `verify_r180_bell_cycle.py` の15項目で、R180Bの厳密流と作用収支、singlet余弦共同分布、非信号性、Tsirelson値、有限全変動誤差下の周辺差・CHSH差、無反応保持を検算した。
- `verify_q2_shell_and_locality.py` の17項目をR180C表記へ同期し、切断後条件付き積、局所詳細釣合い、経路entropy加法性、共通原因平均後の非加法性を再検算した。
- CIの理論階層統合blockをローカルで実行し、R180A--R180Cの定理宣言一意性、R180Cの条件付き表記、現行根拠表、新旧ファイル境界、用語を含む全検査を通した。

## draft-66 PDF生成・目視確認

- 出力はA4、201ページ、1,247,201 byte、SHA-256 `0f544ed27b8318a69a636b00abe773cf54f1c246cd4743f327dd45bd20851927` である。`SOURCE_DATE_EPOCH` は2026-09-04 00:00:00 UTCとした。
- `paper.md`、`main.tex`、`paper.pdf` を連続生成し、再生成差分がないことを確認した。LaTeX logに未定義citation/reference、overfull、underfull、fatal error、欠落文字はない。
- 物理PDFページ1、58--66、90--91、98--99、119--122、147--150を120--144 dpiでrenderした。draft-66表紙、第5章R180A--R180C、第8章の誤差・Bell前提監査、第9章の判定、付録Dのblock・誤差証明、付録Iのsource-driven paired-Hopf流を確認し、数式、表、見出し、頁番号に切れ、重なり、欠落glyph、意図しない空白は見つからなかった。

## draft-65方針監査

- M53をQ2-4の現行模型として追加した。R178A--R178FとR179を根拠に、Q2-4を未達から条件付き達成へ更新した。Q2-1、Q2-2、Q2-3の条件付き達成と他の固定目標判定は変更していない。
- 総bath容量、装置体積、cold/spent cell総数、総熱は指数的でもよい。一方、外部program、制御channel、精度、反復回数、総時間は多項式に抑え、個別mode設定、指数長の係数表、回路別配線、稀な成功、事後選別を禁止する。通常の意味の効率的古典simulationは主張しない。
- R178Aのsector-broadcastは直和のoperator normを最大block誤差で評価し、sector数を加算しない。R178B/Cはinvolution型filter、条件付きBorn積、希少枝切断、有限利得repumpを使う。
- R178Dはdata記録と無反応flagを分け、Fano補正付きspent情報容量下界を置いた。情報容量だけから総熱を同定しない。
- R178E/Fはfixed-volume cell、最小index規則、滑らかな二channel aperture、有限時間境界幅、backreactionを明示する。R164の容量とaperture入口体積を二重計数しない。
- R179は同一静的couplerと受動clockで一定精度partial SWAPを反復し、使用済み状態をspent側へ残す。回路非依存fair-bit源のdyadic tapeは連続一様lawとのtotal variationでなくthreshold discrepancyで評価する。exact invariant blankまたはaggregate cold誤差の一様contractを条件とし、独立な定数thermal noiseではこの条件が破れることを明記した。
- M53ではR170をQ2-4の根拠に使わない。R161/R162はfair-bit source、R164は各逐次段の二枝容量だけに使う。

## draft-65再現計算

- Python構文検査と18本の tools/verify_*.py を実行し、すべて正常終了した。
- R178検算でsector直和誤差 $1.0\times10^{-7}$ が最大block誤差と一致し、filter involution誤差は0、逐次Born誤差は $2.78\times10^{-17}$、希少枝切断質量は上界内だった。
- R179検算で31回partial SWAP後の残差 $2.64\times10^{-5}$ が上界 $5.69\times10^{-5}$ 以下、12 digit threshold discrepancyが $2^{-12}$ 以下、粗視化後の全変動距離が入力tape距離以下だった。
- M53合成検算でfinite-tape正規化誤差は $2.22\times10^{-16}$、aperture傾斜安全量は $8.40\times10^{-2}<8.05\times10^{-1}$、完全結果誤差予算は $4.30\times10^{-4}<10^{-3}$ だった。
- CIの理論階層統合blockをローカルで実行し、M53/R178A--R179の存在、定理宣言の一意性、Q2-4条件付き達成、資源境界、退役ID、用語を含む全検査を通した。
- paper.md、main.tex、paper.pdfを連続生成し、3ファイルのSHA-256が再生成前後で一致した。git diff --checkとLaTeX logの未定義参照、overfull、underfull、missing glyph検査も通過した。

## draft-65 PDF目視確認

完成PDFはA4、207ページ、1,289,585 byteである。全207物理ページを72 dpiでrenderし、16ページずつの13枚のcontact sheetで全体を確認した。さらにM53本文と付録O--Qを144 dpiで確認した。見出し、定理、数式、表、頁番号に切れ、重なり、空白崩れ、欠落glyphは見つからなかった。

## draft-64方針監査

- 内部4modeの存在自体を禁止せず、個別の外部初期化、較正、同期、address、読出し、resetを必要としない受動bath自由度なら許す設計原則へM52を改訂した。
- R176Aの乗算pulseでは $F_{jk},G_{jk}$ に $\sqrt2s_C$ を用い、固定正準行列 $S_0$ の後に $Z_{jk}=a_jb_k$ が係数まで一致することを解析と数値の両方で確認した。
- R176BのCNOTを差mode projectorの指数として実装し、同じ永続register上で局所gate、逆gate、3入力のA--B/B--C gateを合成した。参照因子を加えたoperator normは変わらない。
- R176Cのcanonical SWAP、容量latch、正則化Born比、完全結果空間上の無反応massを検算した。作用殻、有限fiber混合、固定、記録までの一体化は条件として明記した。
- Q2-1のcoherent/dephase逆演算gap $1/2$ と、Q2-3のR177 gap $1/(2\sqrt2)$ を同じ検算器で確認した。
- Q2-1とQ2-3を条件付き達成へ更新し、Q2-2の条件付き達成とQ2-4の未達を維持した。固定目標の文言は変更していない。
- R175と経路限定M52は現行主結果鎖から外し、退役索引と `notes/superseded_m52_path_only_design.md` へ履歴を保存した。

## draft-64再現計算

- `python -m py_compile tools/*.py` と15本の `tools/verify_*.py` を実行し、すべて正常終了した。
- `verify_q1xq1_common_bath.py` の29項目はすべて通過した。最大tensor-lift正規化誤差は $1.40\times10^{-16}$ 未満、$S_0$ の正準誤差は $4.47\times10^{-16}$ 未満だった。
- Q2-1のcoherent/dephase逆演算gapは $1/2$、Q2-3のGHZ--$T$--逆演算gapは $1/(2\sqrt2)$ と数値丸めの範囲で一致した。
- CIの理論階層統合blockをローカルで実行し、R176A/B/Cの宣言一意性、現在地表、退役ID、資源語彙の全検査を通した。
- `python tools/build_paper.py` を連続して再実行し、`paper.md`、`main.tex`、`paper.pdf` のSHA-256が一致することを確認した。`git diff --check` とLaTeX logの未定義参照、overfull、underfull、missing glyph検査も通過した。

## draft-64 PDF目視確認

完成PDFはA4、188ページ、1,203,145 byteである。物理PDFページ1、9、43--48、103--107、151--154、188を110 dpiでrenderし、表紙、目次、第4章R176A/B/C、付録C、付録J、参考文献を確認した。見出し、定理枠、数式、表、頁番号に切れ、重なり、欠落glyphは見つからなかった。

## draft-63方針監査

- Q2-1の4モード担体を現行構成から退役し、達成判定を「部分達成」へ引き下げた。旧M49、R159、R160は現行本文・付録・README・現在地表から除き、履歴メモと退役索引にだけ保存した。
- 新しい候補M52を、1試行内のQ1×Q1共同bath path族として導入した。共同二体量は各試行のpath和 $D_\Gamma=\sum_r\gamma_r a_rb_r^{\mathsf T}$ として定義し、M48の試行集団交差モーメント $\mathbb E[\mathbf 1_Gz_Az_B^{\mathsf T}]$ と区別した。
- R175で局所共変性、pathwise CNOT、任意の外部参照系に対する代数的一致、逆演算、非分離性の保存を示した。path選択やselectorによる試行集団への置換は、coherent handoffの代用にならないことを明記した。
- R176「Q1×Q1共同bath合成定理」は未解決予想として配置した。一般入力lift、有限局所Hamiltonian、bath次元に依存しない参照系安定誤差、同じ符号化への復号、逆演算、M50 Born読出しまでを単一の証明義務とした。
- Q2-3には、三台のQ1と永続状態bathに二つのinteraction zoneを順次作用させる最小合成試験を追加した。条件付き命題R177は $\mathrm{CX}_{A\to B}$、$\mathrm{CX}_{B\to C}$、$T_A$、全逆演算のcoherent予測とdephased予測の全変動距離差 $1/(2\sqrt2)$ を与える。
- 指数個の受動bath自由度は許容する一方、指数個の個別制御、振幅表、mode走査、指数時間、指数精度、稀な成功、事後選別は引き続き不許可とした。誤差評価はbath次元に依存しない作用素または参照系安定ノルムで行う。
- M48はQ2-2のBell型統計生成器として維持したが、Q2-1のcoherent gate carrierまたはM52へのconnectorとしては使わない。M50もR176が復号を与えた後の終端Born読出しに限定した。
- 固定長期目標の文言は変更せず、`PROJECT_STATUS.md`、README、本文、付録、研究メモ、CI、生成器をこの再構築へ同期した。

## draft-62方針監査

- Q2共通ハードウェア族を固定目標の横断条件から外し、判定外の実装努力目標へ移した。各固定目標は、明記した根拠モデルと根拠結果から独立に判定する。
- Q1-1からQ3-5までの現在地表とREADMEへ根拠モデル・根拠結果の対応を追加した。共通の正準代数またはinstrument契約を共有することと、同じ物理装置を使うことを区別した。
- Q2-1はM49/M50とR112/R159/R164、Q2-2はM48/M50とR147/R153/R155/R164/R168/R170を固有の根拠とした。R160はM49からM48への追加接続であり、固定目標の依存条件に含めていない。
- Q2-3は完結モデルなしの8モード正準担体候補とR112、Q2-4は完結モデルなしの直接モード候補とR112/R164/R170を根拠として明記した。共通ハードウェアの未完成性はこれらの判定理由へ混ぜていない。
- Q2-3の「Q1型」を2状態論理部分系の意味に限定し、M47装置の物理的な再利用を要求しないことを明記した。
- Q2-4自身の受動自由度と能動的外部制御の資源区分は維持した。指数的な受動自由度を許しても、指数個の個別制御、指数表、指数時間、指数精度、稀な成功、事後選別は許可していない。
- 付録Cの旧Q2-3直接モード記述を現Q2-4候補へ修正し、付録Lで現Q2-3の $L=8$ と一般の $L=2^n$ を分離した。
- `PROJECT_STATUS.md`、`PROJECT_STANCE.md`、`PROJECT_GUIDE.md`、`README.md`、本文、付録、CI、生成器をこの規約へ同期した。

## draft-61方針監査

- Q2-1とQ2-2の固定目標から依存順序を外し、それぞれを独立に判定する規約へ変更した。R160のM49からM48への接続は、固定目標の依存関係ではなく任意のmodel-to-model接続として保存した。
- Q2系に共通ハードウェア規約を追加した。同型のQ1 port、永続状態浴、interaction zone族、clock/control bus、準備interface、Born読出し・記録部を共有し、目標ごとの担体・浴・読出し装置の交換を禁止した。
- 旧Q2-3を削除し、3個のQ1型部分系に対してA--B gateとB--C gateを順に作用させる「3量子ビット型二段ゲート合成」へ置き換えた。R112は8モード代数を与えるが、永続浴・2 interaction zone・共通interface・coherent handoffの有限誤差統合が未証明なので、現在地を部分達成とした。
- Q2-4を「多項式外部制御による量子出力サンプリング」へ整理した。指数個の受動bath mode、path、静的結合、状態容量は許す一方、回路記述、compile、外部制御係数、制御channel、addressed port、準備から読出しまでの総時間、精度、反復時間を多項式に制限した。
- modeごとの初期化・校正・同期・reset・読出し、指数長の係数表・配線表・lookup table、回路ごとの再配線、全mode走査、出力分布の事前計算、指数精度、指数的な成功時間またはpostselectionを不許可とした。
- 旧Q2-5を現行固定目標・本文・参考文献から削除し、白石--松本型の議論は退役索引だけに履歴として保存した。旧IDは再利用していない。
- 個別機能の達成判定と共通ハードウェアへの横断統合を分離した。Q2-1は個別機能達成、Q2-2は条件付き個別達成だが、両者とも共通ハードウェア統合は未達である。
- `PROJECT_STATUS.md`、`PROJECT_STANCE.md`、`PROJECT_GUIDE.md`、`README.md`、本文、付録、退役索引、参考文献、CI、生成器をこの規約へ同期した。

## draft-60方針監査

- Q2-1の本文と付録へ、4モードCNOTが積入力を2論理部分系に関して非分離な共同内部状態へ写すことを明記した。その状態を2つの物理的測定端へ接続して検査する課題はQ2-2に残した。
- Q2-3を、$L=2^n$ の同一直接モード担体上でR112の有限ゲート列を作用させ、途中で枝選択せず、回路末尾だけでM50/R164/R170を計算基底読出しへ特殊化する構成として本文へ追加した。最終分布の事前計算・直接埋込みを使わず、任意の固定有限回路と正の誤差について有限であることを確認した。
- Q2-3は有限部品と開放instrument契約の単一運転への接続を条件として条件付き達成へ更新した。独立の新定理または新しいミクロ模型を追加したものではない。
- Q2-4はQ2-3から分離し、$2^n$ モードと枝を含む指数資源を避ける一標本資源台帳として未達を維持した。resetは採用時だけ数え、無反応・失敗は完全結果空間上の全変動距離へ含める。
- Q2-5へ白石--松本型の量子熱化決定不能性を構成原理として追加し、既知の孤立量子系結果と本稿の未達な局所古典開放系目標を区別した。有限時間の非停止判定、超計算、量子出力サンプリングの高速化は非主張とした。
- `PROJECT_STATUS.md`、`README.md`、本文、付録、参考文献、CI、生成器の固定目標検査をQ2-3条件付き達成、Q2-4・Q2-5未達へ同期した。

## draft-59方針監査

- 旧Q1-4のZeno効果をQ1-2へ統合し、Q1-2を「射影測定統計とZeno効果」へ変更した。固定基準に2値Born分布、同軸反復分布、異軸逐次分布、有限回反復測定によるZeno型抑制を含めた。
- 旧Q1-3「完全操作・測定周期」を固定目標と現在地表から削除した。旧Q1-3と旧Q1-4のIDを再利用せず、完全周期、永久記録、内部逆計算、reset、周期総収支を実装・熱力学的強化課題へ移した。
- R143とR144の本文および付録B.12を照合し、Born分布、同軸反復分布、異軸逐次分布をQ1-2の導出済み部分とした。測定後固有状態は独立の固定条件から外し、これらの分布を支える現行実現機構として残した。
- Q1-2の現在地は部分達成を維持した。残件を、零傾斜Rabi対照、継続Rabi駆動下の有限回測定、flip・reflip・無反応を含む全履歴、tilt対照、有限誤差、資源台帳を備えた正のZeno抑制余裕に限定した。
- `PROJECT_STANCE.md` と `PROJECT_GUIDE.md` に、固定目標が明記しない有限局所Hamiltonian実装、有限閉鎖Hamiltonian持ち上げ、完全周期、周期総収支を達成条件から分離する規約を追加した。明示的な開放ミクロモデルも達成候補とする一方、要求された入出力または逐次過程の接続自体は必要とした。
- M51、R170、M47の有限局所Hamiltonian統合と周期総収支を未解決問題として保存したが、Q1-2の達成判定から外した。Q2とQ3の固定目標、現在地、達成判定には変更を加えていない。
- `notes/q1_zeno_revival.md` を `notes/q1_2_zeno_integration.md` へ改名し、旧結果の保存と現行Q1-2のZeno検証線を分けた。新しいモデルID、結果ID、定理、証明、数値結果は追加していない。

## 数値・代数検証

`tools/verify_common_signal_m50.py` はR135、R168、R170に対応する31項目を確認した。主な数値は次の通り。

- R135 trace距離: `0.0003785985871776989`
- R135上界: `0.036319466370298495`
- R168可変作用反例のtrace距離: `0.24999999999999997`
- R170有限時間混合誤差: `1.6705734018351848e-13`
- R170混合予算: `0.003999999999999999`
- 例示誤差台帳: `epsilon_170 = 0.033`

`tools/verify_m42_spatial_token.py` はR172--R174に対応する26項目を確認した。主な残差は次の通り。

- M37作用保存誤差: `8.881784e-16`
- 辺流の反対称性誤差: `3.469447e-18`
- 局所連続方程式誤差: `6.938894e-18`
- R172 master方程式誤差: `3.469447e-18`
- 正逆方向の駆動衝突率が各物理閾値から再現されること
- 初期作用殻選択の最大頻度誤差: `3.989125e-06`（上限 `5.000000e-06`）
- 完全結果分布の規格化誤差: `3.552714e-15`

確認数は各スクリプト内のスカラー検査または診断項目の数であり、独立な定理、証明、物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| common canonical control | 29 |
| M47 action-shell origin | 35 |
| common collision thermodynamics | 29 |
| M51 common open preparation | 25 |
| M47 Hopf preparation | 20 |
| M47 Q1 instrument | 43 |
| M48 full cycle | 88 |
| M48 paired-Hopf | 56 |
| common signal and M50 | 31 |
| phase correlation | 15 |
| Q1×Q1 common bath | 20 |
| Q2 shell and locality | 17 |
| Q3 finite-graph phenomena | 36 |
| M42 spatial token | 26 |
| **合計** | **489** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 23、proposition 3、lemma 1、corollary 0、proof 31。
- 付録はA--Nの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録、研究メモ、CIをdraft-63へ同期した。固定目標を定める `PROJECT_STANCE.md` と `PROJECT_GUIDE.md` は変更していない。
- 現行本文・付録・README・現在地表にM49、R159、R160が残っておらず、旧構成の記録が `notes/` にだけ残ることを確認した。
- 新しい本文・付録・検算器のパスと、M52、R175、R176、R177の必須語を生成器とCIで検査した。R175の定理宣言とR177の命題宣言は各1回である。
- Q2-1は全表で「部分達成」、Q2-2は「条件付き達成」、Q2-3は「部分達成」、Q2-4とQ3-2は「未達」で一致した。
- R175のpathwise CNOT、外部参照系の不変性、逆演算、rank-2 witnessと、R177のGHZ--$T$--全逆演算、dephased対照、全変動距離差を数値検算した。
- M48の試行集団交差モーメントとM52の1試行内path和を別概念として扱い、M48をcoherent handoffの根拠に使う記述がないことを確認した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- 生成対象MarkdownにC0制御文字が含まれないことを検査した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 188
- 用紙: A4
- ファイルサイズ: 1,205,399 bytes
- SHA-256: `7b70f22dbfda6b58cced6b9b76fbefc59239046636f54d994dff09ec8e40f196`
- `SOURCE_DATE_EPOCH` は2026-09-01 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全188ページを30 dpiでレンダリングし、20ページずつ10枚のコンタクトシートで通覧した。さらに物理PDFページ1、8、15--16、43--48、82、87、150--154、188を重点確認した。対象にはdraft-63表紙、目次、現在地表、M52とR175/R176の本文、M48との境界、Q2-3の資源規約、付録Cの証明義務、付録Jの二段合成とR177、参考文献を含む。

初回確認で表紙の副題に旧「有限配置ゲート」が残っているのを検出したため、「共同bathゲート」へ同期して再生成した。最終版にクリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表・見出しの破綻はない。最終ログでもoverfull、underfull、未定義参照、欠落文字はなく、ヘッダー、フッター、ページ番号、章・付録の切替は正常である。

## CI

GitHub Actionsは次を確認する。

- 現行15本の検証スクリプトによる489項目とPython構文検査
- 付録A--N、新しいQ1×Q1共同bath原稿・検算器、退役索引の存在と、旧M49原稿・検算器パスの不在
- R112、R171--R174、R135、R161、R162、R164、R168、R170の共通層、R86、R123--R125、R140、R143、R145、R147、R153、R155、R175--R177の集約条件
- M52とR175--R177の必須語、R175定理宣言とR177命題宣言の一意性、Q1×Q1検算器の20項目
- 現行本文・付録・README・現在地表におけるM49、R159、R160の不在
- 固定長期目標の全達成判定語、Q1-2の統合基準、旧Q1-3・旧Q1-4行の不在
- Q2-1の「部分達成」、Q2-2の「条件付き達成」、Q2-3の「部分達成」、Q2-4・Q3-2の「未達」判定
- M52の1試行内path和とM48の試行集団交差モーメントの分離、M50の終端Born読出しへの限定、指数的受動bath自由度と多項式外部制御の区別
- Q2-5現行行の不在、Q2-3--Q2-4とQ3-2を凍結中と扱う旧記述の不在
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- 生成対象MarkdownにおけるC0制御文字の不在
- `paper.md`、`main.tex` の再生成差分と、`paper.pdf` のテキスト層・ページ数・用紙寸法の一致。TeX Liveなどの環境差によるPDFバイナリ差は失敗条件にしない
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
