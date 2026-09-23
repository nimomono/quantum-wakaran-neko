# Q2-2-S spatial strengthening の退役

現行注記：draft-136でQ2-2-Sを独立strengthening IDとして退役し、Q2-2のBell模型とBell前提監査をM66/R205--R207へ一本化した。Q2-2-SのIDは再利用しない。

## 導入から退役まで

Q2-2-Sは、Q2-2 fixed-goalがR180A/R180Cの非空間分離逐次witnessだった時期に、別模型R207を用いて物理的二端化と空間隔離を調べるstrengtheningとして導入した。

draft-134でR207A--R207CがQ2-2 fixed-goal本体へ昇格し、draft-135でR180A/R180Cがactive paperから退役した。この時点でQ2-2とQ2-2-Sは同じR207模型を共有し、Q2-2-Sに固有に残った責務はfinite-speed spatial reservoir、最大伝播速度、setting確定後causal-isolation timingだけになった。

draft-136では、これらを正式なfixed-goalまたはstrengtheningの必須条件として要求しない方針を採る。Q2-2のBell監査は、setting marginal independence、分離後local response factorization、operational non-signalingを保つ一方で

[
ho(Lambdamidoldsymbol a,oldsymbol b)

eq
ho(Lambda)
]

となりmeasurement independenceを満たさないことを明示すれば閉じる。完全なmeasurement independenceとlocal response factorizationを同時に課した対照系はR207DとしてQ2-2本体に残る。

## 退役した管理内容

旧Q2-2-SはS0--S4で管理していた。

- S0：R207 fixed-goal baseline
- S1：具体spatial geometry
- S2：finite-speed causal isolation
- S3：隔離下のBell統計と前提監査
- S4：Bell-local CHSH control

S0はQ2-2本体そのものになり、S4はR207Dへ吸収済みである。S1--S3のfinite-speed/spacelike実装条件は正式目標から外し、A1/A2/B1--B3へ移し替えない。

## 旧candidate checker

Q2-2-S専用diagnosticとして `tools/candidate_checks/verify_r207_separation_control.py` を使用していた。最終active版はmain commit `d76da8bb7b289a3fe5e251f441478644dfaded70` 以前のGit履歴から参照する。

このcheckerはR205F型cross-generator defectの距離減衰と、例示的なfinite-speed timing inequalityを検査していた。R205F passive separation自体は現行R207の一部として残り、R207 fixed-goalのrequired検算は `tools/verify_r207_projection_phase_volume.py` および既存R205系required checksで維持する。

完全な旧コードはnotesへ複製せずGit履歴から参照する。
