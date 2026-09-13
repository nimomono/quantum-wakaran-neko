# 旧Q3 open-Poissonミクロ存在論の退役記録

## 1. 退役対象

R162「局所有向率の開放Poisson-jump実現」そのものは退役しない。退役するのは、独立Poisson reservoirをQ3粒子輸送の基礎的ミクロ物理そのものと読む旧位置づけである。

## 2. 現行置換

draft-95以後、Q3の実在粒子輸送はM57 dual-TL tracer模型が担う。M37/M54実正準空間信号から、R195Aのchiral作用と2作用状態数、R195Bのdual open TL、R195CのFDT/Kramers縮約、R195DのR161生成子matchingを経て、局在tracerのcoarse-grained path lawを得る。

R162は

```text
M57 microscopic tracer
        ↓ R195D finite-error matching
R161 ideal generator
        ↓ R162
ideal open-jump reference path
        ↓ R185/R188
Nelson / time-symmetric Newton
```

という比較用の数学的・確率過程的参照実現へ責務を下げる。

## 3. 保持する結果

- R161の確率流・活動量整合は共通数学interfaceとして維持する。
- R162の非爆発性、生成子、有限骨格/履歴比較は維持する。
- R185の同一前向き経路法則からのBayes後退率と時間対称Newton則は維持する。
- R188のpath-TV誤差から合成加速度への有限時間安定性も維持する。

## 4. 退役理由

旧open-Poisson模型は有効jump過程として数学的に明瞭だったが、粒子・bathのミクロ自由度、signal currentからdriftが生じる物理機構、diffusion係数の起源が抽象的だった。M57は局在tracer、2作用状態数、左右独立open TL、FDT/Kramers縮約を明示し、同じR161核へ有限誤差で接続するため、Q3固定目標が要求する「明示的な古典ミクロモデル」の物理層をこちらへ移す。

## 5. 非主張

R162が誤っていた、または不要になったとは主張しない。M57の有限時間誤差評価とNelson数学核を分離するため、R162は今後もideal referenceとして使用する。

## 6. draft-95最終化検算

Actions run `34752813016` で、正本同期、全数式・数値検算、論文再生成、差分検査、`paper.md`・`main.tex`・`paper.pdf` の同期、最終化用一時workflow/scriptの削除まで成功した。通常のPR検算はこの最終生成コミットに対して別途read-onlyで確認する。
