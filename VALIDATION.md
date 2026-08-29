# 検算と品質確認

この文書は draft-51 の再現計算、静的整合性、PDF 生成、および目視確認の記録である。検証日は 2026-08-28。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python tools/verify_envelope_reduction.py
python tools/verify_phase_correlation.py
python tools/verify_action_distribution.py
python tools/verify_m47_q1_instrument.py
python tools/verify_m47_hopf_preparation.py
python tools/verify_m47_collision_thermodynamics.py
python tools/verify_m47_action_shell_origin.py
python tools/verify_q2_action_shell_integration.py
python tools/verify_q2_1_gate.py
python tools/verify_m49_joint_bath_provider.py
python tools/verify_m48_paired_hopf.py
python tools/verify_m48_full_cycle.py
python tools/verify_m39_m48_ablation.py
python tools/verify_particle_position.py
python tools/verify_q3_completion.py
python simulations/m45_open_quasicritical/verify.py --quick
python tools/build_paper.py
```

## draft-51 理論監査

- R164より前に階数1共分散の支持補題を置いた。$C_Z=cc^\dagger$ から $Z=\alpha c$ がほとんど確実に従うこと、近似支持誤差 $\varepsilon_{\rm supp}$ は平均二乗評価であること、零または小信号を無反応へ送ることを監査した。Q1のM50入力は単一試行値 $z=Z(\omega)$ であり、統計量 $c,C_Z$ をcontrollerへ入れない。
- Q2の交差モーメントには支持補題を適用しない。R146は直接テンソル標本の自己共分散に補題を使う否定的結果、M49は各試行の物理program $D_{\rm prog},d_{\rm prog}$ を使う構成として分離した。交差統計は $B_{AB},\beta_{AB},C_G^\times$ に固定した。
- Pauli反転を $\sigma_x$、CNOT行作用を $\mathcal C_{\rm CX}$、枝置換を $P_{\rm CX}$ とし、粒子位置 $X$ との記号衝突を除いた。M37の局在正準座標も $(x,p_x)$、$X=\operatorname{cell}(x)$ へ分離した。
- 現行文書の旧称「実現配置」が0件であることを静的に検査した。変更記録と `notes/` の旧版用語は履歴として検査対象外に保った。

- M50をQ1・Q2共通モジュールとして導入した。任意の有限信号 $v\in\mathbb C^m$、等長埋込み $\Psi:\mathbb C^m\to\mathbb C^L$、枝容量 $A_i^\delta$、各枝2作用殻の単一Liouville母測度から、R164のBorn型状態数を導く。Q1は $m=2$、M49中央枝は $m=L=4$ の特殊化である。
- 「各枝に2作用があること」と「枝数が2であること」を区別した。2作用殻では状態数が容量に線形だが、直接作用分配次元を増やすと一般に容量の冪になる。共通spectator因子は規格化で消え、枝依存spectator体積、coarea因子、入口流束は枝対称性誤差として残る。
- 作用殻を明示する表示と作用殻を消去する表示を分離した。前者の状態数 $\Omega_i$ と後者の $\exp(-\beta E_i)$ を同時に掛けてBorn重みを二重計数しない。$E_i^\delta$ は条件付き中間状態の相対有効自由エネルギーであり、追加仮定なしに無条件のHamiltonian of mean forceとは呼ばない。
- R161--R163を任意の有限信号方向へ一般化した。R161は平方根型局所率、詳細釣合い、一意定常分布、全ray一様混合率を、R162は有限衝突bathによる粗視化実現を、R163は相対有効仕事 $W^{\rm rel}$ と経路ゆらぎ関係を与える。殻変形仕事 $W^{\rm sh}$ と全微視的仕事・熱は別台帳に置く。
- 有限幅殻の剛性は、$\delta\downarrow0$ で一様精度を保つため少なくとも $\Omega(\delta^{-2})$ が必要であり、$\Theta(\delta^{-2})$ は代表的選択と記した。Q1の有限正準制御と有限セル弱開放bathを同じ有限周期として扱い、強い意味の閉鎖Hamiltonian実現へ読み替えない。
- Q1-2は作用容量結合、殻内平衡化、枝対称性、信号bath反作用の有限局所Hamiltonian統合を残し、Q1-3はHopf pumpからresetまでの周期総収支を残すため、いずれも部分達成を維持した。
- R165はM49中央4枝の状態数 $\Omega_{ab}\propto|D_{ab}|^2$ とM35作用区間標本化を同じ母測度の押し出しとして同定した。M35は運用上の有限Hamiltonian標本器であって、殻の熱化証明ではない。直接標本化に配置混合誤差・衝突熱浴誤差を必須項として二重加算しない。
- CNOTは担体・bath・粒子位置だけでなく作用殻状態数と条件付き有効自由エネルギー地形も同じ枝置換で運ぶ。ただしこの共変性からCNOTパルスの機械仕事が零とは結論しない。入力枝と出力読出しには別のfresh作用殻を使い、同じ殻微視的状態を再利用しない。
- M49からM48へは $z_A,z_B,X_A,X_B$ をstate-carrying・branch-carrying成分として渡し、使用済み中央殻はprovenance-onlyとした。M48単独の等重みseedは対称2枝状態数から、M49接続時のseedは固定singlet中央状態数の非零2枝から得る。paired-Hopf rayは準備機構であり、Born重みの起源ではない。
- R166は完全共通原因 $\Lambda$ に条件付け、fresh局所殻、衝突セル、雑音seed、切断後生成子がA/B積へ分離することを仮定して、局所状態数の積、局所率の分離、経路エントロピー生成の加法性を示す。$\Lambda$ を積分した後の相関は許すが、$-\Theta\log P(a,b\mid x,y)$ を切断後の物理的大域Bellポテンシャルとして局所率へ戻さない。
- Q2-1はR165を追加しても達成、Q2-2はR166を追加しても固定singlet型・有限設定族・非空間分離・設定依存準備の意味で条件付き達成とし、Q2-3・Q3を含む全達成判定は変更していない。

## 数値・代数検証

`tools/verify_m48_full_cycle.py` は R151--R156 に対応する 88 項目を確認する。主な確認対象は、固定pairing tensor、等重みseed、安全盆routing、有限四頂点埋込み、正規化、詳細釣合い、定常残差、正のスペクトルギャップ、有限時間混合、余弦相関、無偏り周辺分布、CHSH 値、および reset である。

`tools/verify_m39_m48_ablation.py` は16項目を確認する。10,000件の一般入力に対する旧controller ray collapse、M39枝と内部fair seedのBell共同分布一致、枝bias sweep、provenance条件付き不変性、一般複素行列のrow/column permutationを検査する。

`tools/verify_m49_joint_bath_provider.py` は29項目を確認する。10,000件の一般複素programについて、R157のcross moment・粒子位置matching・稀な行の作用下界・有限失敗上界、R158の担体・bath・粒子位置CNOT共変性、R159の固定有限benchmarkと1角共有反例、R160のsinglet fiber・state感度・枝bias保存を検査する。

`tools/verify_m47_collision_thermodynamics.py` は29項目を確認する。R164の作用殻容量から作るR161標的の正規化、詳細釣合い、一様スペクトルギャップ下界、正則化誤差、位相・振幅不変性、node no-go、R162の衝突率、粗視化有効自由エネルギー保存、逆散乱、有限セルoverflow、有限エネルギー尾、R163のquench有効仕事、相対エントロピー、経路積分ゆらぎ関係を検査する。

`tools/verify_m47_action_shell_origin.py` は35項目を確認する。階数1自己共分散の因子、単一試行支持、近似支持恒等式、ray上のM50重み不変性に加え、R164の信号作用分解、正則化枝容量、一般作用殻公式、2作用殻の線形性、Born型規格化重み、有効自由エネルギー、作用分配次元の剛性、共通spectator因子の相殺、枝依存流束誤差、滑らかな有限幅殻、$\delta^{-2}$ 剛性増大、零seed、障壁gauge不変性、およびR161との詳細釣合い接続を検査する。

`tools/verify_q2_action_shell_integration.py` は33項目を確認する。M50の一般等長埋込み、M49中央4枝Born状態数、R165の行周辺・条件付き分布、CNOTの状態数・有効自由エネルギー共変性、状態数とBoltzmann因子の二重計数反例、fresh出力殻、固定singlet seed、R166の条件付き積因子化・局所詳細釣合い・経路エントロピー生成加法性、および平均後の大域対数非加法性を検査する。

- 最小 matching gap: `1.900700696128881`
- 例示するM48単独周期の誤差上界: `0.028`

既存検証を含む結果は次の通り。確認数は各スクリプト内のスカラーassertionまたは診断項目の数であり、独立な定理、独立な証明、または独立な物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| phase correlation | 15 |
| action distribution | 40 |
| M47 Q1 | 43 |
| M47 Hopf | 20 |
| M47 collision thermodynamics | 29 |
| M47 action-shell origin | 35 |
| Q2 action-shell integration | 33 |
| Q2-1 | 25 |
| M49 joint-bath provider | 29 |
| M48 paired-Hopf | 56 |
| M48 full cycle | 88 |
| M39--M48 ablation | 16 |
| particle-position cycle | 42 |
| Q3 pair model | 36 |
| M45 quick diagnostics | 23 |
| **合計** | **549** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 47、proposition 7、lemma 6、corollary 2、proof 45。
- `PROJECT_STATUS.md`、`README.md`、`CHANGELOG.md`、`MANIFEST.md`、本文、および付録の draft-51 表記と参照先を照合した。
- 現行検証から旧 M41 検証を外し、M48 full-cycle 検証へ置換した。
- Q2-3・Q3の達成判定、Q3本体、Q3付録の定理・証明ブロック、および M45 図版が基準コミットから不変であることを確認した。Q2-3資源台帳はM49の直接モード費用へ更新し、付録Fは冒頭の適用範囲だけを「Q2-3・Q3」に更新した。
- `git diff --check` に空白エラーはない。

## PDF 生成

- 出力: `paper.pdf`
- ページ数: 238
- 用紙: A4
- ファイルサイズ: 1,607,066 bytes
- SHA-256: `b23fc7f263637c6196a833e654fea196328ff64d89d190fb62f1f64a70dfd29d`
- `SOURCE_DATE_EPOCH` を固定した。現行TeX Liveの出力はPDF trailer IDを持たないが、連続2回の生成でPDFバイナリが一致した。
- 未解決の citation/reference、overfull/underfull box、fatal error、欠落文字、過大 float はない。
- Latin Modern Math の一部に bold fallback 警告があるが、文字欠落や配置崩れはない。

## PDF 目視確認

全 238 ページを10枚の低解像度コンタクトシートで通覧した。さらに、第3章の階数1共分散とQ1周期、第4章のQ2入力・出力統計、付録Kの受渡し契約、付録LのQ1・Q2接続、付録Mの支持補題と共通作用殻容量、付録Nの物理program・CNOT共変性・誤差台帳を144 dpiで重点監査した。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、および見出しの破綻は見つからなかった。

## CI

GitHub Actions は次を確認する。

- 上記 16 本の検証スクリプト
- 現行章・付録・検証器の存在と旧 M41 現行パスの不在
- status guide と本文の整合性
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- 238 ページであること
- LaTeX ログに重大警告がないこと
- `git diff --check`
