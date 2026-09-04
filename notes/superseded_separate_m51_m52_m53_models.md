# 退役したM51・M52・M53の分離模型

draft-67までは、共通開放ray準備をM51、固定2・3入力の永続registerをM52、一般回路の直接mode samplerをM53として別模型に分けていた。draft-68では、これらを一様有限正準register・作用殻receiver模型族M54の特殊化へ吸収した。

| 旧識別 | 旧責務 | 現行の置換先 |
|---|---|---|
| M51 / R171 | 物理template、pump、transverse sinkによるray準備 | M54のtemplate port / R181A |
| M52 / R176A | 固定2・3入力のtensor-lift | M54 / R181B |
| M52 / R176B | 永続4・8mode register上のgate列 | M54 / R181C |
| M52 / R176C | 末端Born instrument接続 | M54 / R181Dの深さ2・3 |
| M53 / R178A | 一般 $n$ のsector-broadcast gate | M54 / R181C |
| M53 / R178B--R178C | projector latch、filter、逐次Born sampler | M54 / R181D |
| M53 / R178E--R178F | fixed-volume apertureとdyadic tape | 現行因果鎖から退役 |

吸収は旧結果の番号を別名で残すことではない。現行本文ではM54とR181A--R181Dだけを正本とし、旧番号はこの退役記録とGit履歴にだけ残す。

M54は共通の状態型とinterfaceを与える模型族であり、全規模で同一の製造済み装置または同一パラメータを使うことまでは主張しない。Q1--Q3を一つの反復周期へ統合するM0は引き続き未完成である。
