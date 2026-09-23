# quantum-wakaran-neko

量子、なんもわからん。

## 1. このプロジェクトの目標

明示的な古典力学モデルから、量子力学に特徴的な可逆操作、Born型測定統計、測定後状態、複合系相関、量子回路型処理、空間粒子力学が、縮約された有効構造としてどこまで現れるかを調べる。

単にSchrödinger方程式と同型の式を古典振動子へ書き写すことは目標ではない。1回の試行で排他的結果が生じる物理過程、結果を次の操作へ渡すinterface、熱浴・雑音・境界条件から確率が生じる場所まで追跡する。

単一試行の物理的実体として扱うのは実正準自由度、粒子位置、熱浴または開放浴との接続、制御器、時計、記録器である。複素信号 $Z$、状態方向、密度、current、確率分布は派生量または試行集団の統計量として区別する。

現在の理論は次の構造に整理している。

```text
共通signal・状態構成
M54
  ↑
M37：古典振動子によるsignal実装

        ↓

共通thermal-reservoir interface
M66 / R205

用途別接続
Q1逐次測定            M65 → R181D
Q2-1/Q2-3/Q2-4読出し R206A--R206D
Q2-4準備              R206E
Q2-2 Bell統計         M66/R205 → R207
Q3粒子/Nelson         M64 → R161 → R185
Q2-2-S因果隔離強化    R207 + finite-speed reservoir
```

M54はsignal・状態・接続規約を共通化し、M66/R205はphase-volume、mean-flow、thermal sampling、passive separationというreservoir原理を共通化する。R206A--R206DはこのinterfaceをQ2終端多結果読出しへ特殊化し、R206EはQ2-4準備を担う。M66はM64やM65の全模型を置換せず、共通するreservoir sectorだけを抽出する。

## 2. 長期目標の現在地

固定目標の定義と厳密な根拠は [PROJECT_STATUS.md](PROJECT_STATUS.md)、A1/A2/B1--B3およびQ2-2-Sの状態は [ENHANCEMENT_TARGETS.md](ENHANCEMENT_TARGETS.md) を正本とする。

### 第1段階：単一量子ビット型装置

| ID | 目標 | 達成判定の中心 | 現在地 |
|---|---|---|---|
| Q1-1 | 単一量子ビット型可逆力学 | Bloch球型状態空間、任意の $SU(2)$ 操作、Rabi振動 | 達成 |
| Q1-2 | 射影測定統計とZeno効果 | Born型2結果、逐次測定、有限回Zeno型抑制 | 達成 |

### 第2段階：複合系・量子計算

| ID | 目標 | 達成判定の中心 | 現在地 |
|---|---|---|---|
| Q2-1 | 2量子ビット型結合ゲート | 結合ゲート型の共同入力--出力統計 | 達成 |
| Q2-2 | Bell型測定統計 | 余弦共同確率、CHSH、Tsirelson限界、非信号性、Bell前提監査 | 達成 |
| Q2-3 | 3量子ビット型二段ゲート合成 | 第1ゲート後状態を保持した二段合成と8結果分布 | 達成 |
| Q2-4 | 多項式外部制御による量子出力サンプリング | 一様装置族で外部制御・時間・精度を多項式に抑えた1標本生成 | 条件付き達成 |

Q2-4の条件はM54 direct-amplitude registerに対するR186の加法ノイズ・精度障害である。R206により末端reader側の逐次探索問題は外れている。

Q2-2-SはQ2-2のR207主線へfinite-speed causal isolationを追加する空間隔離強化である。fixed-goalの一般余弦共同統計とlocal responseはR207A--R207Cへ昇格したが、finite-speed spatial reservoirとsetting確定後のtiming closureが未閉包なので、Q2-2-S全体状態は未監査である。

### 第3段階：空間量子力学

| ID | 目標 | 達成判定の中心 | 現在地 |
|---|---|---|---|
| Q3-1 | 空間Schrödinger型有効力学 | 古典局所自由度からSchrödinger型空間signalを導出 | 達成 |
| Q3-2 | Nelson流または時間対称Newton則 | 古典ミクロ模型から粒子確率過程と時間対称Newton則へ接続 | 達成 |
| Q3-3A | 井戸型束縛状態 | 低位固有状態と純位相緩和 | 達成 |
| Q3-3B | 調和型束縛状態 | 低位固有状態と純位相緩和 | 達成 |
| Q3-3C | W型束縛状態 | W型低位固有状態と純位相緩和 | 達成 |
| Q3-4A | 有限障壁のトンネル効果 | 障壁反対側への正の位置確率移動と位置読出し | 達成 |
| Q3-4B | W型トンネル振動 | 静的W型のトンネル分裂による左右占有交換 | 達成 |
| Q3-5 | 2重スリット干渉 | 2経路の位相依存位置分布と粒子位置読出し | 達成 |
| Q3-6 | 位相量子化 | 閉路巻数、節、位相すべり、非整数モノドロミー排除 | 未達 |

## 3. 運用文書

- [PROJECT_STANCE.md](PROJECT_STANCE.md)：長期的な研究方針と解釈上の立場
- [PROJECT_STATUS.md](PROJECT_STATUS.md)：固定目標、現行模型、現行結果、達成状態の正本
- [ENHANCEMENT_TARGETS.md](ENHANCEMENT_TARGETS.md)：A1/A2/B1--B3、Q2-2-Sの定義と現在地
- [PROJECT_GUIDE.md](PROJECT_GUIDE.md)：論文・リポジトリの更新規約
- [TERMINOLOGY.md](TERMINOLOGY.md)：論文用語と標準表記
- [VALIDATION.md](VALIDATION.md)：数式・数値・生成物・組版の検算記録
- [VALIDATION_POLICY.md](VALIDATION_POLICY.md)：自動検算の責務とrequired/candidateの区別
- [MANIFEST.md](MANIFEST.md)：現行収録物と研究メモの一覧
- [CHANGELOG.md](CHANGELOG.md)：変更履歴
- [notes/theory_lineage.md](notes/theory_lineage.md)：退役研究線から現行正本への入口

## 4. 論文の概要

論文ではまず、有限個の実正準自由度から量子状態に似たsignal空間と可逆操作を作る。M54が共通の有効状態構成を与え、M37/R86が空間signalを古典振動子網として実装する。

測定と粒子輸送にはthermal reservoirを使う。M66/R205は、局所phase-volume weight $w$ から

```math
F_{\rm res}
=
-k_BT\log w+C
```

を得る共通原理、mean-flow port、thermal sampling、passive separationをまとめる。

Q1の逐次2値測定では、保持した2つの射影作用をM65の3状態open selectorへ渡し、結果固定後にR181Dで対応する非規格化射影成分を次段へ渡す。Q2-1/Q2-3/Q2-4の回路末端ではR206が4結果、8結果、または $2^n$ 結果を一回で標本化する。Q2-2はM66/R205のthermal phase-volumeをR207へ特殊化して二端Bell統計を作る。

Q2-2 fixed-goalのBell型統計はR207 projection phase-volume二端模型で再現する。一般Bloch方向の余弦共同分布へ任意精度で近づき、局所周辺は非信号、分離後responseはlocalに因子化する。一方source hidden stateはsetting-dependentでありmeasurement independenceは成立しない。有限伝播速度を持つ具体reservoirはQ2-2-Sでまだ閉じていない。

Q3ではM37/R86 signalへM64のclassical tracerとsignal-driven thermal reservoirを接続し、signal density/currentからosmotic driftとcurrent driftを作る。R203D/R161/R185を介してNelson型の前進・後退平均微分と時間対称Newton則へ接続し、finite graphでは有限障壁、W型トンネル振動、2経路干渉を同じtracerの位置読出しへつなぐ。

この共通化は、全系列を1台の装置へ統合したことを意味しない。準備、操作、測定、永久記録、reset、clock、renewalを1つのjoint microscopic device/processへまとめることはM0で別に要求する。

閲覧用の統合原稿は [paper.md](paper.md)、組版済みPDFは [paper.pdf](paper.pdf) である。再生成は

```bash
python tools/build_paper.py
```

を基本とし、詳細な検査方法は VALIDATION.md と tools/README.md を参照する。
