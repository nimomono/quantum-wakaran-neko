@number: D
@chapter: 付録
@title: M48完全Bell周期の証明
@status: R151--R156のsetting-pre seed routing、局所matching生成子、切断面fiber、局所記録、Bell監査、弱開放帰還を証明する。

## D.1 記号と有限設定族

A、Bの有限設定族を $\mathcal X,\mathcal Y$ とする。A設定作用素を

```math
\Sigma_x
=
\boldsymbol n_x\cdot\boldsymbol\sigma
```

とし、固有ベクトルを

```math
\Sigma_xu_{s,x}
=
s u_{s,x},
\qquad
s\in\{+1,-1\}
```

とする。位相規約は任意でよい。$\mathsf E$ は

```math
\mathsf E
=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

であり、

```math
\mathsf E\Sigma_x^*
=
-\Sigma_x\mathsf E
```

を満たす。従って

```math
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

は $\Sigma_x$ の固有値 $-s$ の固有ベクトルである。

W型有限配置グラフの埋込み $\Phi$ は $\Phi^\dagger\Phi=I_2$ とする。従って $z\neq0$ について

```math
\sum_i
\frac{
|\left(\Phi z\right)_i|^2
}{
z^\dagger z
}
=1.
```

## D.2 R151の証明：setting-pre seedの安全盆routing

設定前の枝seedを $S_0\in\{+1,-1\}$ とし、

```math
P(S_0=+1)=P(S_0=-1)=\frac12
```

とする。M48単独運転では内部の設定非依存registerを使う。M49接続運転では、R160がsetting-free面へ渡した $X_A$ から $S_0=(-1)^{X_A}$ と読み、同じ $z_A,z_B$ registerをbright/dark変数へ接続する。pairing tensor $\mathsf E$ は固定装置定数である。許されたprovenance履歴 $H_{\rm prov}$ は同じ拡大状態に保存できるが、routing核、paired-Hopf流、局所分析器、記録核のいずれにも入力しない。

任意の $h_0\in[h_*,1)$ を固定し、$s=S_0$ と置く。各 $(s,x)$ について

```math
m_{s,x}
=
r_0
\left[
\sqrt{\frac{1+h_0}{2}}
u_{s,x}
+
\sqrt{\frac{1-h_0}{2}}
u_{-s,x}
\right]
```

と選べば

```math
\|m_{s,x}\|
=r_0,
\qquad
h_x(m_{s,x})
=s h_0.
```

有限設定族なので、設定registerと枝seedで選ぶ有限数のcontroller窓を事前配置できる。例えば各窓で

```math
\dot m
=
-\kappa_{\rm seed}
\left(
m-m_{s,x}
\right)
```

という採用開放整列を時間 $T_{\rm seed}$ だけ作用させれば、誤差は $e^{-\kappa_{\rm seed}T_{\rm seed}}$ の定数倍で減衰する。十分小さい誤差では $s h_x(m)\geq h_*$ を保てる。設定はこの前向き整列前に生成され、設定前測度へ $m_{s,x}$ を置いていない。

seed準備のbiasと欠損を $\varepsilon_{\rm seed}$、安全域外とrouting接続域の失敗質量を $\varepsilon_{\rm route}$ として無反応へ送る。M49接続ではbranch biasと同一register搬送の誤差を式(K.12)と式(4.24)で別に管理し、R151のrouting誤差と二重計上しない。

<!-- theorem-start:proof -->
**証明（R151）**

内部またはM49由来の等重みseedと明示seed $m_{s,x}$ が各設定の安全盆を与え、有限時間整列がそこへ指数的に近づける。全写像は設定前共通測度に設定依存分布を置かず、設定生成後の有限前向き操作である。M49接続でもbath・配置registerをensembleから再構成せず、そのまま前向きroutingへ使う。履歴を全結果形成核の入力から外しているため、履歴で条件付けた結果法則は周辺結果法則と一致する。seed誤差と安全域外を無反応へ含めれば定理が従う。証明終。
<!-- theorem-end:proof -->

## D.3 R152の証明：局所matching生成子

各翼の固定した単一試行bath座標 $z$ に対し、付録MのR164を局所適用する。信号作用 $J_{\rm sig}=\mathcal J_0z^\dagger z$、枝作用 $J_i=\mathcal J_0|(\Phi z)_i|^2$、正則化枝容量 $A_i^\delta=J_i+\delta q_iJ_{\rm sig}$ を排他的2作用殻で数えると

```math
\frac{\Omega_i^\delta(z)}
{\sum_j\Omega_j^\delta(z)}
=
\pi_i^\delta(z)
```

となる。従って以下の定常分布は、Born型確率を初期配置分布へ直接置いた量でなく、条件付き作用殻状態数から得た局所有効地形である。

$w_i(z)\geq0$ かつ $\sum_iw_i(z)=1$ なので

```math
\pi_i^\delta(z)
\geq
\frac{\delta q_i}{1+\delta}
>0,
\qquad
\sum_i\pi_i^\delta(z)=1.
```

従って全ての採用辺率は有限かつ正である。対称性 $a_{ij}=a_{ji}$ から

```math
\begin{aligned}
\pi_i^\delta k_{i\to j}^\delta
&=
\kappa_Xa_{ij}
\sqrt{
\pi_i^\delta\pi_j^\delta
}\\
&=
\pi_j^\delta k_{j\to i}^\delta
\end{aligned}
```

となる。有限連結グラフ上の連続時間鎖なので既約であり、$\pi^\delta$ は一意定常分布である。

$-\mathcal L_X^z$ を $L^2(\pi^\delta)$ で見ると自己共役非負である。固有値を

```math
0
=
\lambda_0
<
\lambda_1
\leq
\cdots
```

と並べ、$\lambda_X^\delta(z)=\lambda_1$ とする。既約性から $\lambda_1>0$ である。初期分布を $\rho_0$ とすれば、標準的な有限次元スペクトル分解から

```math
\left\|
\frac{\rho_T}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}
\leq
e^{-\lambda_X^\delta(z)T}
\left\|
\frac{\rho_0}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}.
```

Cauchy--Schwarz不等式により

```math
D_{\rm TV}
\left(
\rho_T,\pi^\delta
\right)
\leq
\frac12
\left\|
\frac{\rho_T}{\pi^\delta}-1
\right\|_{L^2(\pi^\delta)}.
```

$\pi_i^\delta\geq\delta q_{\min}/(1+\delta)$ なので、全初期分布に対する右辺前因子を有限定数 $C_X$ で一様に抑えられる。$z$ を規格化し、有限次元単位球面上の安全なcompact集合へ制限すると、生成子行列は $z$ に連続である。固有値の連続性と各点での正値性から、固定有限seed集合上で $\lambda_X^\delta(z)$ の正の一様下界を選べる。

共通位相に対し $w_i(e^{i\alpha}z)=w_i(z)$ なので $\pi^\delta$ も不変である。また

```math
\begin{aligned}
D_{\rm TV}
\left(
\pi^\delta,w
\right)
&=
\frac{\delta}{2(1+\delta)}
\sum_i
\left|q_i-w_i\right|\\
&\leq
\frac{\delta}{1+\delta}.
\end{aligned}
```

<!-- theorem-start:proof -->
**証明（R152）**

R164が各翼の条件付き状態数と正規化を与える。上の正値性、詳細釣合い、既約性が一意定常分布を与える。有限可逆生成子のスペクトル分解と正則化による一様正値性から指数全変動収束を得る。共通位相不変性と正則化誤差は表示式から直接従う。証明終。
<!-- theorem-end:proof -->

## D.4 強いfiberの基本性質

$\mu\in\mathcal F_W^\delta(c)$ とする。$z=e^{i\alpha}c$ かつ $\|c\|=1$ なので

```math
\frac{
E_\mu[zz^\dagger]
}{
E_\mu[z^\dagger z]
}
=
cc^\dagger.
```

また

```math
P_\mu(X=i)
=
E_\mu
\left[
\pi_i^\delta(z)
\right]
=
\pi_i^\delta(c).
```

従ってM47のrank-one bath条件を厳密に満たし、配置対角matchingを $\delta/(1+\delta)$ の誤差で満たす。さらに $X$ のbath条件付き分布を固定するため、周辺matchingだけより強い。

連続bath座標について、有限時間軌道は一般に目標rayそのものへは到達しない。従って切断面の完全状態測度を全変動距離で理想fiberと比較してはならない。第5.5節の $d_{\rm pair}$ は、同じ $\alpha$ をA側とB側へ反対符号で使うためpaired位相を保存し、動径誤差と2翼方向誤差を同時に測る。これに枝符号と2つの離散配置の不一致indicatorを加えて1で切った $d_\Omega$ は有界距離である。

このcostに関するWasserstein距離 $d_{\rm fib}$ では、bath対を同じ初期seedから理想吸引先へcoupleしたときの期待costをR147の有限時間ノルム上界で抑えられる。有限配置分布は最大couplingを使えば不一致確率が全変動距離に等しい。従って連続方向誤差と離散配置誤差を同じfiber距離へ加えられる。

## D.5 R153の証明：切断面2翼fiber

R151の理想枝seedでは、各 $s$ が確率 $1/2$ で選ばれ、$s h_x(m_0)\geq h_*$ である。R147から、paired-Hopf時間 $T_{\rm PH}$ 後にある同じ位相 $\alpha$ が存在して

```math
\left|
z_A-e^{i\alpha}u_{s,x}
\right|
+
\left|
z_B-e^{-i\alpha}v_{s,x}
\right|
\leq
K_{48}e^{-\gamma_{48}T_{\rm PH}}
```

となる。seed biasと安全盆routingの有限誤差は、それぞれ $\varepsilon_{\rm seed}$ と $\varepsilon_{\rm route}$ へ入れる。

R152の $\pi^\delta(z)$ は、$\|z\|$ が零から離れたcompact集合で $z$ の射影にLipschitzである。その定数をpaired-Hopf前因子へ吸収すれば、有限時間bath方向誤差から配置目標の誤差も $K_{48}e^{-\gamma_{48}T_{\rm PH}}$ の定数倍で抑えられる。

paired-Hopf終了時の $z_A,z_B$ をcontrollerで保持する。条件付き独立なA、B配置bathを時間 $T_X$ だけ作用させると、R152から各翼の条件付き配置分布は対応する $\pi^\delta$ から $C_Xe^{-\lambda_X^\delta T_X}$ 以内になる。最大couplingを各翼へ使うと配置不一致確率は各全変動誤差の和以下である。さらに $\pi^\delta$ と理想 $w$ の全変動距離は各翼で $\delta/(1+\delta)$ 以下なので、理想fiber $\mathcal F_W^0$ への正則化costは2翼で $2\delta/(1+\delta)$ 以下である。

理想安全枝の非規格化交差共分散は

```math
\begin{aligned}
M_{AB}
&=
\frac12
\sum_{s=\pm1}
u_{s,x}v_{s,x}^{\mathsf T}\\
&=
-\frac12\mathsf E
\end{aligned}
```

である。最後の等式は付録Jのspin-flip恒等式である。規格化ベクトル化射影はsinglet射影で、$x$ に依存しない。

枝分布を最大couplingし、bath対を同じseedとpaired位相でcoupleし、配置を条件付き最大couplingする。枝、bath対、配置正則化、有限混合、切断の期待costを加えると、理想fiber混合 $\nu_x^0$ に対するR153の $d_{\rm fib}\leq\varepsilon_{\rm fib}$ を得る。$\varepsilon_{\rm seed}$ と $\varepsilon_{\rm route}$ に含めた同じ源誤差を別の項へ重複して入れない。

<!-- theorem-start:proof -->
**証明（R153）**

R151が等重み安全枝、R147がpaired bath対の有限時間近接、R152が各bath座標に条件付けた配置分布の有限時間収束を与える。正則化誤差、積核誤差、切断誤差を上のcouplingで加えると、強い理想2翼fiberへのprojective fiber距離上界を得る。連続bath状態の全変動近接は使わない。交差共分散は枝和恒等式からsinglet射影になる。証明終。
<!-- theorem-end:proof -->

## D.6 R154の証明：局所分析と記録

局所分析に入る作用殻は中央殻の使用済み微視的状態でなく、各翼のfresh registerに準備する。切断後半群と初期条件付き測度の積因子化は付録NのR166で証明し、ここではその有限偏差 $\varepsilon_{\rm prod}$ を局所instrument誤差とは別に加える。

切断後、A、Bの正準変数、配置bath、noise seedを別々にする。共有する $s,\alpha$ は切断面に存在する共通過去であり、切断後の相互作用ではない。生成子の和に交差項がないため、その後の遷移核は完全状態に条件付けて

```math
K_{\rm post}^{xy}
=
K_A^x
\otimes
K_B^y
```

と因子化する。

A分析器を

```math
A_xu_{s,x}
=
|s\rangle
```

となるように選ぶ。B分析器について、局在出力 $|b\rangle$ の理想2モード重みは

```math
\begin{aligned}
p(b\mid s,x,y)
&=
\left|
\langle b|
A_yv_{s,x}
\rangle
\right|^2\\
&=
\left|
\langle b_y|
v_{s,x}
\rangle
\right|^2\\
&=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
\end{aligned}
```

最後の式は $v_{s,x}$ のBlochベクトルが $-s\boldsymbol n_x$ であることから従う。

各分析器終了後にbath方向を固定し、R152の局所配置bathを走らせる。従って記録直前の配置分布は分析器後bath座標のW型対角から有限混合誤差内にある。R142により左右空間効果と理想2モード射影の差は $\eta_W$ 以下である。固定有限設定族のguardから離れたcompact安全域では、分析器、$w(z)$、記録効果の合成応答核は $d_\Omega$ に関して一様Lipschitzである。その定数を $L_{\rm fib}$ とすれば、切断面fiber誤差が結果分布へ与える寄与は $L_{\rm fib}\varepsilon_{\rm fib}$ 以下である。

配置jump prefactorを零に切り替えた後、傾斜保持と局所記録剪断を作用させる。理想rate切断では記録窓中にjumpは起きない。有限切断残差、傾斜保持、分離面、記録cell幅をそれぞれ独立誤差へ入れる。

連続時間Markov鎖は、初期位置と各辺の局所jump clock列を固定すれば標本路がほとんど確実に一意である。clock列を完全状態のnoise seedに含めると、記録時刻の配置と結果は一意になる。無反応は正式な第3結果である。

<!-- theorem-start:proof -->
**証明（R154）**

局所2モード分析器が理想条件付き重みを与え、R152がそのbath座標に対応する配置分布を記録前に局所的に回復する。rate切断と傾斜保持後の局所剪断が配置だけを記録する。生成子とnoiseが切断後にA、Bへ分かれるため応答核は因子化する。有限制御、混合、W型コントラスト、固定、境界、記録の誤差を加えれば定理が従う。証明終。
<!-- theorem-end:proof -->

## D.7 R155の証明：共同分布と有限誤差

完全共通原因 $\Lambda$ に条件付けるとR166により局所作用殻と応答核は積になる。$\Lambda$ を $\mu_{\rm cut}^x$ で積分することで既存の余弦共同分布を回復するため、条件付き積因子化はBell相関を消去しない。有限誤差の三角不等式には $\varepsilon_{\rm prod}$ を1回だけ加える。

理想枝では $P(s)=1/2$、$a=s$ なので

```math
\begin{aligned}
P(a,b\mid x,y)
&=
\sum_s
\frac12
\mathbf1_{a=s}
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)\\
&=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right).
\end{aligned}
```

和を取れば両周辺は $1/2$、符号積を取れば

```math
E(x,y)
=
-\boldsymbol n_x\cdot\boldsymbol n_y
```

である。平面標準設定を代入すればCHSH絶対値は $2\sqrt2$ になる。

前向き周期を有限個のMarkov核 $K_1,\ldots,K_N$、理想核を $K_1^0,\ldots,K_N^0$ とする。各段の一様全変動誤差が $\epsilon_j$ 以下なら逐次結合から

```math
D_{\rm TV}
\left(
\nu_0K_1\cdots K_N,
\nu_0K_1^0\cdots K_N^0
\right)
\leq
\sum_j\epsilon_j.
```

状態方向またはcontroller誤差は、対応する有限設定核のLipschitz定数を通して結果分布距離へ換算してから加える。特にR153のprojective fiber誤差は $L_{\rm fib}\varepsilon_{\rm fib}$ として加える。この和が第5章の $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ である。

周辺化は全変動距離を増やさない。A周辺が同じ理想周辺から各設定で $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以内なら、三角不等式により反対設定間の差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

各相関関数の被積分関数は、無反応を数値0として絶対値1以下である。従って1設定対の相関差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下、4項のCHSH差は $8\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

設定前測度は同じ $\nu_0$ だが、R151のseed routingとR147の吸引先は $x$ に依存する。異なる非順序軸 $x,x'$ では2つの固有ray集合が異なるため、理想切断面測度の支持も異なる。従って一般に

```math
\mu_{\rm cut}^x
\neq
\mu_{\rm cut}^{x'}.
```

一方、D.6節の切断後核は局所因子化する。測定設定独立性は成立せず、局所応答因子化と理想非信号性は成立する。

<!-- theorem-start:proof -->
**証明（R155）**

等重み枝とB条件付き重みを合成するとsinglet共同分布を得る。逐次核の全変動上界が前向き誤差和を与え、周辺化、三角不等式、有界観測量の期待値差から非信号周辺差とCHSH差を得る。$2\sqrt2-8\varepsilon_{\rm Bell}^{48,{\rm cyc}}>2$ を解けば定理の破れ条件になる。切断面支持の設定依存性と切断後核の因子化がBell前提監査を与える。証明終。
<!-- theorem-end:proof -->

## D.8 R156の証明：fresh cell帰還

周期末偏差が

```math
\Delta_{n+1}
=
R_{\rm ret}\Delta_n
+
\eta_n,
\qquad
\|R_{\rm ret}\|
\leq
r_{\rm ret}
<1,
\qquad
\|\eta_n\|
\leq
\sigma_{\rm ret}
```

を満たすとする。反復すれば

```math
\|\Delta_n\|
\leq
r_{\rm ret}^n
\|\Delta_0\|
+
\sigma_{\rm ret}
\sum_{j=0}^{n-1}
r_{\rm ret}^j.
```

従って

```math
\limsup_{n\to\infty}
\|\Delta_n\|
\leq
\frac{
\sigma_{\rm ret}
}{
1-r_{\rm ret}
}.
```

controller残差が $\dot\Delta=-\lambda_{\rm ret}\Delta$ に従う時間窓では、有限時間残差は $C_{\rm ret}e^{-\lambda_{\rm ret}T_{\rm ret}}$ 以下である。これに有限SWAPとfresh seed幅を加えれば $\varepsilon_{\rm ret}$ の式を得る。

外部記録、使用済みsource、使用済みbathを逆実行しないため、全外部状態を同一点へ押しつぶさない。固定有限周期数なら必要な外部cell数も有限である。帰還は記録後に行うので、同じ周期の観測分布へ因果的に影響せず、次周期入口誤差へだけ渡す。

<!-- theorem-start:proof -->
**証明（R156）**

縮小写像の幾何級数評価が一様周期末上界を与える。有限時間減衰、SWAP、fresh seedの誤差を加えると1周期帰還誤差を得る。外部記録と使用済み状態を保持するため情報の不可逆消去を有限閉鎖系内で行ったとは主張せず、固定有限周期またはcell流を持つ弱開放周期として定理が従う。証明終。
<!-- theorem-end:proof -->

## D.9 任意精度の有限パラメータ選択

固定有限設定族と固定有限W型グラフについて、目標 $\epsilon>0$ を与える。まず十分小さい正則化 $\delta$ を選び、

```math
\frac{2\delta}{1+\delta}
<
\frac{\epsilon}{6}
```

とする。次に

```math
T_{\rm PH}
>
\frac1{\gamma_{48}}
\log
\frac{6K_{48}}{\epsilon},
```

```math
T_X
>
\frac1{\lambda_X^\delta}
\log
\frac{12C_X}{\epsilon}
```

を選ぶ。有限設定controller、W型深さ、記録幅、時計幅、reset時間を順に選び、残る有限個の誤差をそれぞれ $\epsilon$ の所定部分以下にする。従って形式的に時間を無限へ送るだけでなく、各 $\epsilon$ に対して有限時間・有限グラフ・有限設定controllerを選べる。

$\delta$ を小さくすると最小定常重みが小さくなり、$\lambda_X^\delta$ または最大rateが悪化し得る。W型を深くすると読出し誤差は下がるが、2モード操作時間が伸び得る。この構成は任意精度を同じ固定性能装置で得るとは主張しない。

## D.10 M41との置換境界

旧M41はM42/R113の場から配置への最小率と、A結果に条件付けた2担体準備を使った。M48は、内部のsetting-pre等重みseed、paired-Hopf bath対、単一試行bath座標に条件付けたR152の局所配置bath、切断後の局所再matchingから結果を作る。両者の因果律を同じ証明へ混ぜない。

M41のR107--R111、R121は置換済み模型内の結果として研究メモに保存する。R151--R156はM41の4モード条件付き2端準備もM39の4-mode状態受渡しも仮定せず、M42/R113をM48の実現配置頻度へ使わない。Q2-1からの共同bath受渡しは、M49/R160が付録Kの契約に従って固定singlet供給プログラムについて閉じる。一般Q2-1出力を扱う一般状態receiverは未完了である。

## D.11 証明範囲

本付録で厳密なのは、採用した有限次元paired-Hopf方程式、有限Markov生成子、有限設定controller、局所分析器、記録・帰還式の後段である。R152の局所状態数には付録MのR164、rate形には第3章R161、固定bath座標の有限衝突熱浴には付録LのR162を利用できる。一方、作用容量fiber、seed整列drift、paired-Hopf pump、信号bath保持、2翼controller、fresh cell流までを同じ具体的電子回路、流体装置、振動子浴、有限閉鎖Hamiltonianへ統合した結果ではない。Bell統計の条件付き達成範囲は変更しない。
