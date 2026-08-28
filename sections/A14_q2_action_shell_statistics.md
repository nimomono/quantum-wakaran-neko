@number: N
@chapter: 付録
@title: Q2中央4枝作用殻と切断後局所因子化
@status: M50をQ2へ特殊化し、R165でM49中央4枝作用殻とM35作用区間標本化の同値性、R166でM48切断後局所作用殻の完全共通原因に条件付けた積因子化を示す。中央殻、局所殻、履歴の役割を分離し、切断後の大域的Bell自由エネルギーを物理相互作用として導入しない。

## N.1 目的と段階分離

Q2では作用殻を2つの異なる段階で使う。

1. M49の中央4枝作用殻は、4成分の物理program信号 $(D_{\rm prog})_{ab}$ から共同枝 $(a,b)$ を1回だけ選ぶ。
2. M48の中央準備は、paired-Hopf流により2翼のrayと共通原因を準備する。
3. 中央切断後は、各翼がfreshな局所2枝作用殻と局所衝突熱浴を持つ。

第1段階の中央殻は共同Born重みを与える。第2段階のpaired-Hopf流は共有rayを準備するが、Born重みの状態数起源ではない。第3段階の局所殻は、完全共通原因に条件付けた局所応答を与える。これらを同じ作用殻微視的状態の連続運動として扱わない。

M50は共通理論部品であり、M49とM48に同一の殻ハードウェアを要求しない。中央殻の使用済み状態は受渡し面で履歴だけを残し、M48へ運ぶ物理量は $z_A,z_B,X_A,X_B$ とfreshな局所装置レジスタである。

## N.2 M49中央4枝の単一母測度

ある段階の規格化された物理program係数行列を $D_{\rm prog}\in\mathbb C^{2\times2}$ とし、行優先ベクトル化を

```math
d_{\rm prog}
=
\operatorname{vec}_{\rm row}(D_{\rm prog})
=
((D_{\rm prog})_{00},(D_{\rm prog})_{01},(D_{\rm prog})_{10},(D_{\rm prog})_{11})^{\mathsf T},
\qquad
d_{\rm prog}^\dagger d_{\rm prog}=1
```

とする。M50で $m=L=4$、$\Psi=I_4$、枝集合を

```math
\mathcal I_4
=
\{00,01,10,11\}
```

と選ぶ。中央信号作用と枝作用は

```math
J_{\rm sig}
=
\mathcal J_0d_{\rm prog}^\dagger d_{\rm prog}
=
\mathcal J_0,
\qquad
J_{ab}
=
\mathcal J_0|(D_{\rm prog})_{ab}|^2
```

である。M49の直接有限選択では $\delta=0$ とし、$J_{ab}>0$ の活性支持だけに枝を置く。零容量枝は状態数零であり、有限幅境界またはdecode失敗は無反応へ送る。

枝 $(a,b)$ ごとに2つの非負作用 $K_{ab},I_{ab}$ と2角を置き、

```math
K_{ab}+I_{ab}=J_{ab}
```

を課す。付録MのR164から

```math
\Omega_{ab}(D_{\rm prog})
=
\frac{(2\pi)^2}{J_{\rm ref}}J_{ab}
=
\frac{(2\pi)^2\mathcal J_0}{J_{\rm ref}}
|(D_{\rm prog})_{ab}|^2
```

となる。4枝を非交和として1回だけ規格化すれば

```math
P(a,b\mid D_{\rm prog})
=
\frac{\Omega_{ab}(D_{\rm prog})}
{\sum_{r,s}\Omega_{rs}(D_{\rm prog})}
=
|(D_{\rm prog})_{ab}|^2
\tag{N.1}
```

を得る。A周辺とAに条件付けたB分布は

```math
P(A=a\mid D_{\rm prog})
=
\rho_a,
\qquad
\rho_a
=
\sum_b|(D_{\rm prog})_{ab}|^2,
```

```math
P(B=b\mid A=a,D_{\rm prog})
=
\frac{|(D_{\rm prog})_{ab}|^2}{\rho_a}
\tag{N.2}
```

である。式(N.2)はR157の行templateが作る単一試行粒子位置matchingと一致する。

## N.3 M35作用区間への測度押し出し

M35の4作用区間は、規格化信号 $d_{\rm prog}$ の累積作用

```math
s_{ab}
=
\sum_{(r,s)\preceq(a,b)}|(D_{\rm prog})_{rs}|^2
```

から区間

```math
\mathcal O_{ab}
=
[s_{ab}^{-},s_{ab}^{+})
```

を作る。中央2作用殻の枝内で一様化した角座標を $u_X\in[0,1)$ とし、枝ラベル写像を

```math
\chi_{D_{\rm prog}}(u_X)
=
(a,b)
\quad\Longleftrightarrow\quad
u_X\in\mathcal O_{ab}
```

とする。$u_X$ は熱浴の混合時間を表す変数でなく、枝周辺を平坦化した作用殻座標である。M35の比較器、pointer、可逆decodeは、作用殻母測度を枝ラベルへ押し出す有限Hamiltonian標本器として使う。

<!-- theorem-start:theorem -->
**定理（R165：M49中央4枝作用殻とM35作用区間標本化の同値性）**

規格化された固定有限 $D_{\rm prog}$ 族について、各活性枝に同じ2作用殻Liouville規約を使い、$\delta=0$ とする。中央母測度を枝ラベルへ直接射影して得る分布と、枝内一様座標 $u_X$ をM35作用区間へ押し出して可逆decodeした分布は、ともに式(N.1)である。行周辺と行条件付き分布は式(N.2)となり、R157の行分解bath templateと整合する。

有限装置の全変動誤差を次の4項へ分ける。

有限幅誤差を $\varepsilon_{\rm width}^{49}$ とする。

殻の枝非対称誤差を $\varepsilon_{\rm sym}^{49}$ とする。

作用区間境界誤差を $\varepsilon_{\rm chart}^{49}$ とする。

decode誤差を $\varepsilon_{\rm dec}^{49}$ とする。

このとき無反応込み出力は

```math
D_{\rm TV}
\left(
P_{49}^{\rm obs},P_{D_{\rm prog}}
\right)
\leq
\varepsilon_{\rm cap}^{49}
+\varepsilon_{\rm width}^{49}
+\varepsilon_{\rm sym}^{49}
+\varepsilon_{\rm chart}^{49}
+\varepsilon_{\rm dec}^{49}
```

を満たす。粒子位置混合誤差と衝突熱浴誤差は、この直接標本化定理の必須項ではない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R165）**

R164の4枝特殊化から中央殻の枝測度は $|(D_{\rm prog})_{ab}|^2$ に比例する。M35区間のLebesgue長も $|(D_{\rm prog})_{ab}|^2$ であるため、平坦化座標の押し出しは同じ枝分布を与える。行で和を取り、正の行重みで割れば式(N.2)を得る。有限誤差は母測度、座標平坦化、境界、decodeの順に三角不等式で加える。証明終。
<!-- theorem-end:proof -->

R165はM35を作用殻の熱化証明とは分類しない。M35は固定有限Hamiltonian標本器であり、殻内一様性または条件付き平衡化はM50側の準備条件である。

## N.4 CNOT置換共変性と熱力学地形

CNOTが枝へ作用する置換を

```math
P_{\rm CX}(a,b)
=
(a,b\oplus a)
```

とする。係数行列への作用を $D_{\rm prog}\mapsto\mathcal C_{\rm CX}(D_{\rm prog})$ とすれば

```math
| (\mathcal C_{\rm CX}(D_{\rm prog}))_{P_{\rm CX}(a,b)} |^2
=
|(D_{\rm prog})_{ab}|^2
```

なので

```math
\Omega_{P_{\rm CX}(a,b)}(\mathcal C_{\rm CX}(D_{\rm prog}))
=
\Omega_{ab}(D_{\rm prog}).
\tag{N.3}
```

作用殻消去表示では

```math
E_{P_{\rm CX}(a,b)}(\mathcal C_{\rm CX}(D_{\rm prog}))
=
E_{ab}(D_{\rm prog})
```

であり、状態数と条件付き有効自由エネルギー地形は担体・bath・粒子位置と共に置換される。式(N.3)は分布地形の共変性であって、CNOTパルスの機械仕事が零であることを意味しない。全作用保存だけでは時計、制御器、作用殻変形の仕事を消去できない。

一般の積分析器 $W_A,W_B$ の後は

```math
D_{\rm out}
=
W_A\mathcal C_{\rm CX}(D_{\rm in})W_B^{\mathsf T}
```

に対するfreshな出力殻とfreshな結果レジスタ $Y_A,Y_B$ を使う。入力枝用の $u_X$ と出力枝用の $u_Y$ は、同じ試行に属しても異なる殻微視的状態を平坦化した座標である。1つの座標を入力と出力に再利用すると目標共同分布を壊し得るため、独立性の要請は「同じ殻微視的状態を再利用しない」という物理要請である。$u_S$ は入力program頻度を作る外側scheduleであり、作用殻の熱座標ではない。

## N.5 M49からM48への受渡し

M49の中央4枝殻はCNOT出力で1回使われる。固定singlet providerでは中央共同枝は $01,10$ の2枝に縮退し、同じ試行の $z_A,z_B,X_A,X_B$ をM48へ運ぶ。受渡し状態を

```math
\Gamma_{49\to48}
=
(z_A,z_B,X_A,X_B,H_{\rm prov},R_A^{\rm fresh},R_B^{\rm fresh})
```

とする。$H_{\rm prov}$ は使用済み中央殻の識別情報を保持するが、M48の結果形成へ入力しない。中央殻の $K_{ab},I_{ab}$ と角座標はM48の局所殻へ渡さない。局所作用殻レジスタ $R_A^{\rm fresh},R_B^{\rm fresh}$ は未使用状態から開始する。

この分離により、M49のstate-carrying部分は $z_A,z_B$ とcross projector感度、branch-carrying部分は $X_A,X_B$、使用済み中央殻はprovenance-onlyとなる。

## N.6 M48単独seedとM49接続seed

M48単独周期の等重みseedは、対称2枝作用殻

```math
J_+=J_-
=
\frac12J_{\rm seed}
```

から作れる。2枝に同じ2作用殻規約を使えば $\Omega_+=\Omega_-$ であり、$P(S_0=\pm1)=1/2$ となる。

M49接続周期ではseedを新しく標本化せず、固定singlet中央4枝状態数の非零枝 $01,10$ から

```math
S_0=(-1)^{X_A}
```

と読む。両枝の状態数が等しいため同じ等重みを持つ。paired-Hopf準備はこの $S_0$ と設定後の安全盆routingから共有rayを準備するが、$S_0$ のBorn重みを生成し直さない。

## N.7 切断後の局所作用殻

中央切断面の完全共通原因を

```math
\Lambda
=
(s,\alpha,z_A,z_B,X_A,X_B,H_{\rm prov},R_{\rm cut})
```

とする。履歴は結果形成へ入力しないが、条件付き独立性を監査する完全状態には含める。切断後の各翼 $w\in\{A,B\}$ にfreshな局所2枝作用殻

```math
\Gamma_{w,+}^{\delta_w}(z_w)
\sqcup
\Gamma_{w,-}^{\delta_w}(z_w)
```

を置き、局所枝状態数を

```math
\Omega_{w,r}^{\delta_w}(z_w)
=
\frac{(2\pi)^2}{J_{{\rm ref},w}}
A_{w,r}^{\delta_w}(z_w),
\qquad r\in\{+1,-1\}
```

とする。局所殻のLiouville測度、局所衝突セル、局所雑音seedは $\Lambda$ に条件付けてA、B間で独立に準備する。

<!-- theorem-start:theorem -->
**定理（R166：M48切断後局所作用殻の条件付き積因子化）**

切断後のHamiltonianまたは開放生成子が

```math
\mathcal L_{\rm post}^{xy}
=
\mathcal L_A^x
+
\mathcal L_B^y
```

と分離し、freshな局所作用殻、衝突セル、局所雑音seedが完全共通原因 $\Lambda$ に条件付けて積測度を持つとする。このとき切断後の作用殻測度は

```math
\mu_{\rm sh}^{AB}
(d\gamma_A,d\gamma_B\mid\Lambda,x,y)
=
\mu_{{\rm sh},A}^x
(d\gamma_A\mid\Lambda)
\otimes
\mu_{{\rm sh},B}^y
(d\gamma_B\mid\Lambda)
```

と因子化する。従って状態数と局所詳細釣合い率も

```math
\Omega_{rs}^{AB}(\Lambda,x,y)
=
\Omega_{A,r}^x(\Lambda)
\Omega_{B,s}^y(\Lambda),
```

```math
k_{(r,s)\to(r',s)}
=
k_{A,r\to r'}^x,
\qquad
k_{(r,s)\to(r,s')}
=
k_{B,s\to s'}^y
```

となる。経路エントロピー生成は

```math
\Sigma_{\rm post}
=
\Sigma_A+\Sigma_B
```

と加法的である。因子化からの全変動偏差を $\varepsilon_{\rm prod}$ とすれば、局所instrument誤差とは別にBell完全結果分布へ加算する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R166）**

初期条件付き測度が積で、切断後の半群が $e^{t\mathcal L_A^x}\otimes e^{t\mathcal L_B^y}$ と因子化するため、任意有限時刻で上の因子化式が保たれる。状態数は積測度の全質量なので積になり、局所跳躍率は反対翼の状態を含まない。正逆経路確率比の対数は積経路測度の対数比なので和になる。有限な残留結合、共通雑音、レジスタ取り違えによる偏差を $\varepsilon_{\rm prod}$ にまとめる。証明終。
<!-- theorem-end:proof -->

完全共通原因で条件付けず、$\Lambda$ を積分するとA、Bは一般に相関する。

```math
P(a,b\mid x,y)
=
\int
P_A(a\mid x,\Lambda)
P_B(b\mid y,\Lambda)
\,\mu_{\rm cut}^x(d\Lambda).
\tag{N.5}
```

M48では $\mu_{\rm cut}^x$ がA設定に依存し、式(N.5)が既存の余弦共同分布を与える。R166はこの相関を消さず、切断後に新しい非局所相互作用を加えないことを示す。

## N.8 大域的Bell自由エネルギーの禁止

切断後に

```math
E_{ab}^{\rm Bell}(x,y)
=
-\Theta\log P(a,b\mid x,y)
```

を物理的な大域ポテンシャルとして置くと、反対翼の設定を局所率へ再注入し、R166の生成子分離を壊す。従って式(N.5)から作った対数は、平均後の共同分布を要約する情報量としてだけ使い、切断後のHamiltonian、障壁、局所跳躍率には使わない。

条件付き局所有効自由エネルギーは

```math
E_{A,r}^x(\Lambda)
=
-\Theta_A\log\pi_{A,r}^x(\Lambda),
\qquad
E_{B,s}^y(\Lambda)
=
-\Theta_B\log\pi_{B,s}^y(\Lambda)
```

と定義でき、固定 $\Lambda$ では加法的である。$\Lambda$ を積分した後の対数は、一般にこれらの平均または和ではない。

## N.9 誤差と資源台帳

Q2-1の中央4枝殻では

```math
\varepsilon_{49}^{\rm sh}
=
\varepsilon_{\rm cap}^{49}
+\varepsilon_{\rm width}^{49}
+\varepsilon_{\rm sym}^{49}
+\varepsilon_{\rm chart}^{49}
+\varepsilon_{\rm dec}^{49}
```

を使う。R165は直接標本化定理なので、熱化時間、混合gap、衝突セル数を必要資源に数えない。M35の16正準対は有限Hamiltonian標本器の透明な上界であり、中央作用殻を実装する実際の平衡自由度数とは区別する。

Q2-2では各翼、各局所分析段階 $r$ について $\varepsilon_{M50}^{w,r}$ を持ち、

```math
\varepsilon_{48}^{\rm sh}
\leq
\sum_{w\in\{A,B\}}
\sum_r
\varepsilon_{M50}^{w,r}
+\varepsilon_{\rm prod}
```

とする。同じ物理偏差をR153のfiber誤差、R154の局所instrument誤差、R166の積因子化誤差へ重複して入れない。

次元は付録Mに従う。作用殻1枝あたり2作用・2角を必要とするが、中央4枝を同時に4つの活性装置へ複製する必要はない。非交和の枝registerと可逆routingで1枝だけを活性化できる。これは存在上界であり最小自由度を主張しない。

## N.10 非主張

本付録は次を主張しない。

1. M49の中央4枝作用殻とM48の各局所2枝作用殻が同一ハードウェアであること。
2. 中央殻の使用済み微視的状態を局所殻へ運び、同じ軌道として追跡したこと。
3. paired-Hopf準備がBorn重みの状態数起源であること。
4. M35の一意エルゴード角が殻内Gibbs熱化または独立同分布型標本を証明すること。
5. CNOT置換共変性からパルスの機械仕事が零と従うこと。
6. 切断後の大域的Bell有効自由エネルギーが物理相互作用として存在すること。
7. 一般Q2-1出力を一般状態Bell測定へ渡すこと。
8. paired-Hopf、局所作用殻、衝突熱浴、記録、resetを1つの有限閉鎖Hamiltonian周期へ統合したこと。

R165はQ2-1の達成判定を維持したままBorn型共同頻度の統計力学的起源を追加する。R166はQ2-2の条件付き達成を維持したまま、切断後局所性の統計力学的意味を強める。
