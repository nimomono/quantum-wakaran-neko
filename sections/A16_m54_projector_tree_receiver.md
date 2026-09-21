@number: P
@chapter: 付録
@title: M54段階的射影選別と測定後状態受渡し
@status: R181Dを上流binary selectorの物理実装から独立な共通projector-router定理として定式化する。R191は現行fixed-goal selector実装、M65は別の現行canonical selector modelとして同じ契約を満たす。一般深さの作用安定化はR192へ分離する。

## P.1 目的と節点状態

深さ $m$ の二分段階的射影選別を考える。節点 $u\in\{0,1\}^{k-1}$ の入力記憶部を $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

\[
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
\]

未処理射影作用を

\[
J_{u,b}
=
\mathcal J_0 Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma
=
J_{u,0}+J_{u,1}
=
\mathcal J_0Z_u^\dagger Z_u
\]

とし、

\[
p_{u,b}=\frac{J_{u,b}}{J_\Sigma}
\]

を理想条件付きBorn重みとする。

R181Dの責務は、上流binary selectorが固定した排他的結果を受け取り、projector routerで非規格化結果成分を次段へ渡すことである。selectorの内部物理、熱浴、rate、decision lawはR181Dの状態へ含めない。

## P.2 共通binary selector contract

節点 $u$ のselectorは完全結果

\[
Y_u\in\{0,1,\varnothing\}
\]

を返す。理想核を

\[
K_u(0)=p_{u,0},
\qquad
K_u(1)=p_{u,1},
\qquad
K_u(\varnothing)=0
\]

とし、実装核を $\widetilde K_u$ とする。

R181Dが要求する上流契約は次の5条件だけである。

1. 完全結果誤差
\[
D_{\rm TV}(\widetilde K_u,K_u)\leq\varepsilon_{{\rm sel},u}.
\]

2. 非空安全結果 $Y_u=b$ では
\[
p_{u,b}\geq\tau_{{\rm state},u}>0.
\]

3. $Y_u$ はprojector routerを開く前に固定される。

4. selectorはBorn確率表または振幅表を外部制御器へ要求しない。

5. $\varnothing$ を除いて成功試行だけを再規格化しない。

安全下限 $\tau_{{\rm state},u}$ をどう作るかはselector実装側の責務である。

### P.2.1 現行R191実装

R191を使う現行fixed-goal主線では、

\[
\varepsilon_{{\rm sel},u}
=
\varepsilon_{191,u},
\]

\[
\tau_{{\rm state},u}
=
\tau_{\rm cut}-\frac{\varepsilon_u}{2}>0
\]

と取れる。endpoint dispatcher、mixing、finite-temperature retreat、finite-time capture、吸収記録はR191側の誤差台帳に含める。

### P.2.2 M65実装

M65/R204D--R204Eを使う場合は、

\[
\varepsilon_{{\rm sel},u}
=
\varepsilon_{65,u},
\]

\[
\tau_{{\rm state},u}
=
\tau_{\rm cut}-\varepsilon_A>0
\]

と取れる。M65内部rateや無反応hub誤差はM65側の誤差台帳に含める。

本draftではQ1/Q2 fixed-goal witnessをR191からM65へ切り替えない。

## P.3 結果固定後の可逆projector router

selectorが有限decision時間後に $Y_u=b\in\{0,1\}$ を固定したときだけ、信号と未使用作業領域上の選別機構

\[
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
\]

を作用する。

直交射影子の関係から

\[
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I
\]

であり、

\[
F_{u,b}(Z_u,0)
=
(P_{u,b}Z_u,P_{u,1-b}Z_u).
\]

非選択成分を消去せず作業領域へ保持するので、router自体は可逆な実正準写像として実装できる。$Y_u=\varnothing$ の場合はどちらのrouterも作用させない。

## P.4 router誤差と条件付き状態方向

理想選択成分を

\[
v=P_{u,b}Z_u
\]

とし、実装後を $\widetilde v$ とする。router誤差が

\[
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|
\]

を満たすとする。

binary selector contractの安全下限から

\[
\|v\|
\geq
\sqrt{\tau_{{\rm state},u}}\|Z_u\|.
\]

従って

\[
\eta_F<\sqrt{\tau_{{\rm state},u}}
\]

なら、

\[
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{
2\eta_F
}{
\sqrt{\tau_{{\rm state},u}}-\eta_F
}
=:
\varepsilon_{{\rm proj},u}.
\]

この下限は物理的な状態依存除算ではない。selectorが保証した安全集合境界を解析に使うだけである。

## P.5 階数1射影子と測定後状態

階数1節点

\[
P_{u,b}=|b_u\rangle\langle b_u|
\]

では、

\[
v=P_{u,b}Z_u
=
\alpha_b|b_u\rangle,
\]

従って

\[
\frac{vv^\dagger}{v^\dagger v}
=
P_{u,b}.
\]

selectorの物理方式に依存せず、結果固定後のrouterそのものが選択後信号を射影子像へ送る。物理的な単位ノルム規格化は不要であり、非規格化成分を次段へそのまま渡す。

## P.6 Q2-4専用補助：R192作用安定化

一般深さQ2-4で選択後作用が次節点の感度下限を下回り得る場合だけ、router後の選択成分へR192を接続する。

\[
\dot Z
=
g(J_*-Z^\dagger Z)Z.
\]

R192は状態方向を変えず、Born重みや結果選択を作らない。必要な固定時間上界はselectorから受け取る $\tau_{\rm state}$ とR192自身のパラメータだけで評価する。

固定有限深さではR192を使わず、非規格化結果成分をそのまま次段へ渡せる。

## P.7 望遠鏡和と完全結果誤差

理想節点核を $K_k$、実装核を $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

\[
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(\cdot\mid h_{k-1}),
K_k(\cdot\mid h_{k-1})
\right)
\leq
\bar\varepsilon_k
\]

とする。

$\bar\varepsilon_k$ には、その節点で実際に使うselectorの完全結果誤差、局所記録誤差、router誤差、必要なR192誤差、転送誤差、前段状態方向誤差から次節点核へ伝播した偏差を各1回だけ含める。異なるselector実装の誤差を同一試行で重複加算しない。

Markov核の縮約性と望遠鏡和から、

\[
D_{\rm TV}
(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^{m}\bar\varepsilon_k.
\]

理想節点では

\[
\prod_{k=1}^{m}
p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z\|^2
}{
\|Z\|^2
}
\]

と望遠鏡型に縮約する。無反応を同じ完全履歴空間に保持し、成功履歴だけを再規格化しない。

<!-- theorem-start:theorem -->
**定理（R181D：binary selector後の段階的projector-routerと測定後状態受渡し）**

P.2のbinary selector contractを各節点で満たし、P.3のrouterを結果固定後にだけ作用し、必要な場合だけR192を使うとする。このとき理想極限ではLüders型逐次分布と非規格化測定後成分を得る。有限実装では

\[
D_{\rm TV}
(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^{m}\bar\varepsilon_k
\]

であり、安全結果の状態方向誤差はP.4の上界で抑えられる。

R181Dの結論はselectorの内部物理に依存しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R181D）**

P.2が完全結果核と安全作用下限、P.3が結果固定後の1対1な経路分解、P.4--P.5が条件付き状態方向、P.6が必要時だけの作用下限回復を与える。各段の完全結果核誤差を一度だけ $\bar\varepsilon_k$ に集約し、Markov核の縮約性と望遠鏡和を適用する。理想節点では未規格化作用比が連鎖的に相殺される。証明終。
<!-- theorem-end:proof -->

## P.8 一般深さの資源境界と反証条件

深さ $m=n$ の一般Q2-4では、各節点のselector、router、必要なR192、転送誤差を $O(\epsilon/n)$ に配分する。

現行R191 fixed-goal実装についてはA20/T節のR191資源条件を使う。M65を選ぶ場合はA26/Z節のR204F資源条件を使う。R181D自身はどちらのselectorにも追加の指数precisionを要求しない。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部制御器へ入力する。
2. selectorの結果固定前にrouterを開く。
3. endpoint判定に状態依存除算または指数precisionを要求する。
4. 非選択成分または作用安定化環境を同じ能動状態へ不可逆に消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 深さ $n$ のselector、router、転送誤差を多項式予算へ同時に収められない。
