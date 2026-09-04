# 退役したR178 aperture sampler

draft-67までのM53/Q2-4は、projector容量を次の別経路で排他的結果へ変えていた。

1. 二枝作用を容量pointerへlatchする。
2. branch labelとLiouville座標を持つfixed-volume cellを用意する。
3. 容量依存の滑らかな二channel apertureを通過または反射させる。
4. 複数cellをindex順に試し、最初のacceptを結果にする。
5. fair-bit源からdyadic threshold tapeを作る。

この経路の主な旧結果は、first-index選択の分布、有限tape失敗率、aperture境界幅、backreaction、離散threshold discrepancyであった。式と完全な証明はdraft-67のGit履歴を正本とする。

draft-68ではQ1とQ2の読出しをM54/R181DのR170駆動projector-treeへ統一した。R181Dはraw容量とregularized作用殻を分け、R164/R170がselectorを形成した後に可逆filterを開き、R181Aのradial-only portで選択rayを標準作用へ戻す。このため旧R178E/R178F、fresh aperture tape、dyadic thresholdは現行依存グラフから外した。

退役は反証を意味しない。次のいずれかが必要になれば、独立の代替receiverとして再検討できる。

- R170作用殻より強い完全Hamiltonian散乱実装が必要な場合
- fixed-volume entrance measureの物理起源を別に閉じられる場合
- aperture境界、arrival bias、backreactionを単一safe setで評価できる場合
- dyadic tapeを外部の指数精度へ費用移転せず供給できる場合

旧R178Dのhistory境界は、開放radial repumpを無履歴で逆掃除しない形へ改訂して現行結果に残す。
