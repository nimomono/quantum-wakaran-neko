@number: P
@chapter: 付録
@title: M54段階的射影選別と測定後状態受渡し
@status: R181Dを上流binary selectorの物理実装から独立な共通projector-router定理として定式化する。現行fixed-goalではQ1逐次測定とQ2-2 A端--B端handoffに用い、Q2-1/Q2-3/Q2-4のterminal readoutはM66/R206へ移す。

## P.1 目的と節点状態

深さ $m$ の二分段階的射影選別を考える。節点 $u\in\{0,1\}^{k-1}$ の入力記憶部を $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

```math
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
```

未処理射影作用を

```math
J_{u,b}
=
\mathcal J_0 Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma
=
J_{u,0}+J_{u,1}
=
\mathcal J_0Z_u^\dagger Z_u
```

とし、

```math
p_{u,b}=\frac{J_{u,b}}{J_\Sigma}
```

を理想条件付きBorn重みとする。

R181Dの責務は、上流binary selectorが固定した排他的結果を受け取り、projector routerで非規格化結果成分を次段へ渡すことである。selectorの内部物理、熱浴、rate、decision lawはR181Dの状態へ含めない。

## P.2 共通binary selector contract

節点 $u$ のselectorは完全結果

```math
Y_u\in\{0,1,\varnothing\}
```

を返す。理想核を

```math
K_u(0)=p_{u,0},
\qquad
K_u(1)=p_{u,1},
\qquad
K_u(\varnothing)=0
```

とし、実装核を $\widetilde K_u$ とする。

R181Dが要求する上流契約は次の5条件だけである。

1. 完全結果誤差
```math
D_{\rm TV}(\widetilde K_u,K_u)\leq\varepsilon_{{\rm sel},u}.
```

2. 非空安全結果 $Y_u=b$ では
```math
p_{u,b}\geq\tau_{{\rm state},u}>0.
```

3. $Y_u$ はprojector routerを開く前に固定される。

4. selectorはBorn確率表または振幅表を外部制御器へ要求しない。

5. $\varnothing$ を除いて成功試行だけを再規格化しない。

安全下限 $\tau_{{\rm state},u}$ をどう作るかはselector実装側の責務である。

### P.2.1 現行M65実装

M65/R204D--R204Eを使う場合は、

```math
\varepsilon_{{\rm sel},u}
=
\varepsilon_{65,u},
```

```math
\tau_{{\rm state},u}
=
\tau_{\rm cut}-\varepsilon_A>0
```

と取れる。M65内部rateや無反応hub誤差はM65側の誤差台帳に含める。

Q1およびQ2-2 fixed-goal witnessにはM65を使う。

## P.3 結果固定後の可逆projector router

selectorが有限decision時間後に $Y_u=b\in\{0,1\}$ を固定したときだけ、信号と未使用作業領域上の選別機構

```math
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
```

を作用する。

直交射影子の関係から

```math
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I
```

であり、

```math
F_{u,b}(Z_u,0)
=
(P_{u,b}Z_u,P_{u,1-b}Z_u).
```

非選択成分を消去せず作業領域へ保持するので、router自体は可逆な実正準写像として実装できる。$Y_u=\varnothing$ の場合はどちらのrouterも作用させない。

## P.4 router誤差と条件付き状態方向

理想選択成分を

```math
v=P_{u,b}Z_u
```

とし、実装後を $\widetilde v$ とする。router誤差が

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|
```

を満たすとする。

binary selector contractの安全下限から

```math
\|v\|
\geq
\sqrt{\tau_{{\rm state},u}}\|Z_u\|.
```

従って

```math
\eta_F<\sqrt{\tau_{{\rm state},u}}
```

なら、

```math
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
```

この下限は物理的な状態依存除算ではない。selectorが保証した安全集合境界を解析に使うだけである。

## P.5 階数1射影子と測定後状態

階数1節点

```math
P_{u,b}=|b_u\rangle\langle b_u|
```

では、

```math
v=P_{u,b}Z_u
=
\alpha_b|b_u\rangle,
```

従って

```math
\frac{vv^\dagger}{v^\dagger v}
=
P_{u,b}.
```

selectorの物理方式に依存せず、結果固定後のrouterそのものが選択後信号を射影子像へ送る。物理的な単位ノルム規格化は不要であり、非規格化成分を次段へそのまま渡す。

## P.6 望遠鏡和と完全結果誤差

理想節点核を $K_k$、実装核を $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

```math
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(\cdot\mid h_{k-1}),
K_k(\cdot\mid h_{k-1})
\right)
\leq
\bar\varepsilon_k
```

とする。

$\bar\varepsilon_k$ には、その節点で実際に使うselectorの完全結果誤差、局所記録誤差、router誤差、転送誤差、前段状態方向誤差から次節点核へ伝播した偏差を各1回だけ含める。異なるselector実装の誤差を同一試行で重複加算しない。

Markov核の縮約性と望遠鏡和から、

```math
D_{\rm TV}
(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^{m}\bar\varepsilon_k.
```

理想節点では

```math
\prod_{k=1}^{m}
p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z\|^2
}{
\|Z\|^2
}
```

と望遠鏡型に縮約する。無反応を同じ完全履歴空間に保持し、成功履歴だけを再規格化しない。

**定理再掲（R181D：binary selector後の段階的projector-routerと測定後状態受渡し）**

P.2のbinary selector contractを各節点で満たし、P.3のrouterを結果固定後にだけ作用するとする。このとき理想極限ではLüders型逐次分布と非規格化測定後成分を得る。有限実装では

```math
D_{\rm TV}
(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^{m}\bar\varepsilon_k
```

であり、安全結果の状態方向誤差はP.4の上界で抑えられる。

R181Dの結論はselectorの内部物理に依存しない。


<!-- theorem-start:proof -->
**証明（R181D）**

P.2が完全結果核と安全作用下限、P.3が結果固定後の1対1な経路分解、P.4--P.5が条件付き状態方向を与える。各段の完全結果核誤差を一度だけ $\bar\varepsilon_k$ に集約し、Markov核の縮約性と望遠鏡和を適用する。理想節点では未規格化作用比が連鎖的に相殺される。証明終。
<!-- theorem-end:proof -->

## P.7 適用境界と反証条件

R181Dは、結果固定後に非規格化射影成分を同じ試行の次操作へ渡す必要がある場合だけ使う。現行fixed-goalではQ1逐次測定とQ2-2のA端--B端handoffがこれに当たる。Q2-1/Q2-3/Q2-4はterminal M66/R206 samplerへ移行し、R181Dを結果標本化の一般treeとして使わない。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部制御器へ入力する。
2. selectorの結果固定前にrouterを開く。
3. endpoint判定に状態依存除算または指数precisionを要求する。
4. 非選択成分を同じ能動状態へ不可逆に消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 固定有限深さのselector、router、転送誤差を有限誤差予算へ収められない。
