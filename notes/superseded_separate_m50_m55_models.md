# M50・M55独立モデルとR183の吸収記録

draft-73まで、Q1/Q2の固定時刻測定はM50、Q3の全時刻位置過程はM55として別のモデルIDを持っていた。draft-74では、両者が同じ単一試行signal、configuration変数、R164条件付き分布、finite collision部品を共有し、数学的な違いがmatching currentの有無に整理できることから、M54のprofileとして統合した。

## 1　旧M50

旧M50は、単一試行signalからR164の正則化作用容量を作り、R161の平方根型詳細釣合い率とR162のthermal collisionでconfigurationを再平衡化し、R170でlock・recordする共通instrument仕様であった。

draft-74ではこの内容をM54 static-instrument profileへ吸収した。R164、R161 static specialization、R162 thermal specialization、R168、R170は現行結果として保持する。M50というモデルIDだけを現行一覧から外し、再利用しない。

## 2　旧M55

旧M55は、実正準signal、1個の粒子位置、finite collision cell、clock、historyを持つQ3親模型であり、R183がR164と同じ条件付き分布をmoving matchingとして保存した。

draft-74では、M54を一般signal index集合 $\Lambda$ とconfiguration集合 $\mathcal I$ を持つ共通親模型へ拡張した。Q3は $\Lambda=\mathcal I=V$、$\Psi=I$ のspatial-moving profileとなる。M55の物理自由度はこのprofileへ保持され、M55という独立モデルIDだけを現行一覧から外す。

## 3　R183

R183の内容は撤回しない。一般化R161で

```math
k^+_{i\to j}
=
\frac{t_{ij}+j_{ij}}{2\pi_i},
\qquad
k^-_{i\to j}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
```

とし、M54 spatial profileのSchrödinger型signal currentと対称trafficを代入すると旧R183 rateとmoving-matching不変性を回収する。従ってR183は独立結果IDから外してR161の無番号spatial系へ吸収し、IDは再利用しない。

## 4　現行の区別

統合後もstaticとmovingを同一の物理運転とは扱わない。

- static profile: $j=0$。Q1/Q2の操作面・末端読出しでR161 static、R162 thermal、R170を使う。
- spatial profile: $j\neq0$。Q3でR161 moving、R162 generic、R184/R185を使う。
- M37: M54 spatial signal sectorの局所ばねbackendとして独立に残す。
- M0: 全profileを同じ製造済みハードウェアと反復周期へ統合する将来目標であり、M54の共通状態型だけでは達成しない。

この統合は固定長期目標と達成ラベルを変更しない。
