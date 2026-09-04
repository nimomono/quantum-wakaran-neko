# 置換済み独立M48 Bell protocol

この文書はdraft-65まで現行Q2-2の根拠だった独立M48 Bell protocolの置換記録である。旧第5章、付録D、付録IとR147、R153、R155の完全な式・証明・検算器はGit履歴を正本とし、ここでは退役理由と再検討条件だけを管理する。

## 置換理由

独立M48は、内部の設定前等重みseedをA設定ごとの安全盆へroutingし、試行集団の交差momentからsinglet型paired fiberを特徴づけた。この構成は固定singlet Bell統計を条件付きで閉じたが、M52が同じ試行で保持する実際の4mode末端信号を受け取らなかった。このためQ2-1とQ2-2は根拠模型上も分離したままだった。

draft-66では主線をR180A--R180Cへ置換する。R180AはM52の実際の1試行末端信号をA設定basisでblock分解し、block作用を枝容量へ、同じ未規格化blockをB側templateへ渡す。R180Bは選択templateをsourceとするpaired-Hopf流を採用し、R180Cは中央切断後の2翼局所instrument、Bell監査、帰還を単一装置統合の条件付きで合成する。

## 保存する内容

- paired-Hopfで共役位相を持つ2翼rayを有限時間準備する考え方。
- setting-preでA設定を中央準備へ入力し、B設定を切断後のB局所分析器へだけ入力する因果順序。
- 完全共通原因に条件付けた切断後局所因子化、無反応込み誤差、非信号性、CHSH差の監査方法。
- 固定singletで現れるspin-flip fiber。R180Aのsinglet特殊化はこれをglobal phaseまで回復する。

## 現行根拠に使わない内容

- 独立fair seedと設定別safe-basin routing。
- 試行集団交差momentをreceiverの単一試行入力とみなすこと。
- R147、R153、R155を現行Q2-2の結果番号として引用すること。
- M52の実信号を介さずに独立M48だけでQ2-2を判定すること。

## 再検討条件

独立M48を再検討するのは、M52を使わないBell sourceが必要になり、その独立sourceの物理的価値、単一試行担体、仕事・熱・情報流がR180より明確に閉じる場合に限る。旧結果番号は再利用しない。
