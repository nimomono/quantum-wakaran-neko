@number: B
@chapter: 付録
@title: M47傾斜制御測定の証明と誤差評価
@status: R135、R140、R143、R144について、2次元共分散、W型2モード制御、傾斜保持、有限コントラスト、局所記録、枝別状態更新、条件付き周期を証明する。

## B.1 規格化共分散の正準発展

複素2モード正準変数を $Z=(Z_0,Z_1)^{\mathsf T}$ とし、Poisson括弧を

```math
\{Z_j,Z_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

とする。Hermitian行列 $G(t)$ に対するHamiltonian $H_G=Z^\dagger GZ$ は

```math
i\mathcal J_0\dot Z
=
GZ
```

を与える。伝播行列 $U(t,t_0)$ は

```math
i\mathcal J_0\partial_tU
=
G(t)U,
\qquad
U(t_0,t_0)=I_2
```

を満たし、Hermitian性からunitaryである。各試行で $Z(t)=U(t,t_0)Z(t_0)$ なので

```math
\mathbb E[Z(t)Z(t)^\dagger]
=
U
\mathbb E[Z(t_0)Z(t_0)^\dagger]
U^\dagger.
```

分母 $\mathbb E[Z^\dagger Z]$ は保存される。従って

```math
C_Z(t)
=
U(t,t_0)C_Z(t_0)U(t,t_0)^\dagger
```

であり、微分すると $i\mathcal J_0\dot C_Z=[G,C_Z]$ を得る。

## B.2 R135の2次元系

2次Hermitian行列はPauli基底で

```math
C_Z
=
\frac12
\left(
\operatorname{tr}C_Z\,I_2
+
\sum_{k=x,y,z}
\operatorname{tr}(C_Z\sigma_k)\sigma_k
\right)
```

と展開できる。$\operatorname{tr}C_Z=1$ なので本文の表示を得る。固有値は

```math
\lambda_\pm
=
\frac12(1\pm|\boldsymbol r|)
```

である。正半定値性は $|\boldsymbol r|\leq1$、階数1は固有値集合が $\{1,0\}$ であることと同値なので $|\boldsymbol r|=1$ である。

階数1なら $C_Z=cc^\dagger$ と因数分解できる。同じ $C_Z$ を与える規格化因子 $d$ は、$C_Z$ の1次元像を張るので $d=e^{i\alpha}c$ である。従って因子空間は $S^3/U(1)=\mathbb{CP}^1$ である。

<!-- theorem-start:proof -->
**証明（R135の2次元系）**

上の固有値計算により階数1条件と単位Bloch球面が同値である。B.1のunitary共役は階数1を保存し、共通位相を変えても $C_Z$ を変えない。従ってM47階数1共分散の有効状態空間はBloch球面であり、古典正準流がその回転を与える。証明終。
<!-- theorem-end:proof -->

## B.3 傾斜W型の2モード行列

偶奇基底で、対称生成子の最低2モード射影は

```math
P_2h_W(0)P_2
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}.
```

$x$ は奇なので

```math
\langle\phi_0|x|\phi_0\rangle
=
\langle\phi_1|x|\phi_1\rangle
=
0.
```

$x_{01}=\langle\phi_0|x|\phi_1\rangle$ を実非負に選べば

```math
P_2xP_2
=
x_{01}\sigma_x
```

である。偶奇基底から局在基底へのHadamard変換を $H$ とすると

```math
H\sigma_zH
=
\sigma_x,
\qquad
H\sigma_xH
=
\sigma_z.
```

従って共通項 $\overline E I_2$ を除き

```math
H P_2h_W(F)P_2 H
-
\overline E I_2
=
-J\sigma_x
-
Fx_{01}\sigma_z.
```

左右の名称または傾斜符号を選び直せば本文の $\varepsilon=2F|x_{01}|$ の形になる。

## B.4 R140の可制御性

共通エネルギーは共通位相しか生成しないため除く。傾斜零の反Hermitian生成子を

```math
X_0
=
\frac{iJ}{\mathcal J_0}\sigma_x
```

とし、傾斜差から得る制御方向を

```math
X_1
=
-\frac{i}{2\mathcal J_0}\sigma_z
```

とする。交換子は

```math
[X_0,X_1]
=
-\frac{iJ}{\mathcal J_0^2}\sigma_y
```

である。$J>0$ なら $X_0,X_1,[X_0,X_1]$ は $\mathfrak{su}(2)$ を張る。$SU(2)$ はコンパクトで連結なので、正負の傾斜を含む区分一定制御の到達集合は $SU(2)$ 全体である。固定目標操作ごとに有限積を選ぶ。

一定傾斜では

```math
G
=
-J\sigma_x
+
\frac{\varepsilon}{2}\sigma_z,
\qquad
G^2
=
\left(
J^2+\frac{\varepsilon^2}{4}
\right)I_2.
```

$\Omega_E=\sqrt{J^2+\varepsilon^2/4}$ とすると

```math
e^{-iGt/\mathcal J_0}
=
\cos
\left(
\frac{\Omega_Et}{\mathcal J_0}
\right)I_2
-
i\frac{G}{\Omega_E}
\sin
\left(
\frac{\Omega_Et}{\mathcal J_0}
\right).
```

$|L\rangle=(1,0)^{\mathsf T}$、$|R\rangle=(0,1)^{\mathsf T}$ とすれば、遷移振幅の絶対値2乗は本文の式になる。

<!-- theorem-start:proof -->
**証明（R140）**

Lie代数階数条件から任意の $SU(2)$ 操作が有限傾斜列で到達できる。B.1から各区間は共分散のunitary共役である。一定傾斜の指数行列を展開して左右遷移成分を取れば、Rabi振幅、振動数、離調依存式を得る。証明終。
<!-- theorem-end:proof -->

## B.5 2モード漏れの有限次元評価

有限格子上の全生成子を、最低2モード射影 $P$ と補空間 $Q=I-P$ に分ける。傾斜摂動を $V(t)=-F(t)x$ とし、観測区間で

```math
\|PVQ\|
\leq
v,
\qquad
\operatorname{dist}
\left(
\operatorname{spec}(PhP),
\operatorname{spec}(QhQ)
\right)
\geq
G
```

とする。$v/G<1/2$ なら、スペクトル射影の静的回転は $O(v/G)$、確率漏れは $O((v/G)^2)$ である。滑らかな切替では、瞬時射影の時間微分に由来する振幅が $O(\mathcal J_0/(G\tau_q))$ である。有限次元かつ固定切替形状なので、両者をまとめる定数 $C_W<\infty$ が存在し

```math
\varepsilon_{2m}
\leq
C_W
\left[
\left(
\frac{v}{G}
\right)^2
+
\left(
\frac{\mathcal J_0}{G\tau_q}
\right)^2
\right]
```

となる。本文では $v$ を $|\varepsilon_m|$ と同じ次数へ吸収した。この評価は固定有限格子族の作用素ノルム上界を使う。格子幅を零へ送るときに $C_W$ が一様とは主張しない。

## B.6 R140の傾斜保持節と尺度選択

一定傾斜の生成子を

```math
G_m
=
-J\sigma_x
+
\frac{\varepsilon_m}{2}\sigma_z,
\qquad
\Omega_m
=
\sqrt{\varepsilon_m^2+4J^2}
```

とする。Bloch球上では、時間発展は単位軸 $\boldsymbol n=(-2J,0,\varepsilon_m)/\Omega_m$ のまわりの回転である。$\Pi_L=(I_2+\sigma_z)/2$ とすると

```math
\left\|
U(t)^\dagger\Pi_LU(t)-\Pi_L
\right\|_\infty
\leq
\frac{2|J|}{\Omega_m}.
```

実際、$z$ 軸の $\boldsymbol n$ に直交する成分の長さは $2|J|/\Omega_m$ であり、回転によるその成分の変化は高々2倍、射影のBloch係数は $1/2$ だからである。従って任意の規格化共分散について左占有率の変化は $2|J|/\Omega_m$ 以下である。

初期共分散が局在射影の場合は、R140の遷移式で正弦2乗は1以下なので、さらに強い上界

```math
P_{L\to R}(t)
\leq
\frac{4J^2}{\varepsilon_m^2+4J^2}
```

である。右から左も同じである。保持中の残留散逸、制御揺らぎ、matching driftを $\varepsilon_{\rm hold}$ とすれば、一般入力の2モード内周辺固定誤差は本文の $\varepsilon_{\rm lock}$ で抑えられる。全W型発展と2モード近似の分布距離 $\varepsilon_{2m}$ はこれと別に加え、全W型系の固定中分布誤差を $\varepsilon_{2m}+\varepsilon_{\rm lock}$ とする。

深いW型族で $r=J/G\to0$ とする。$|\varepsilon_m|=G\sqrt r$、$\tau_q=\mathcal J_0/(G\sqrt r)$ を選ぶと

```math
\frac{J}{|\varepsilon_m|}
=
\frac{|\varepsilon_m|}{G}
=
\frac{\mathcal J_0}{G\tau_q}
=
\frac{J\tau_q}{\mathcal J_0}
=
\sqrt r.
```

一般入力の周辺固定項は $2\sqrt r/\sqrt{1+4r}$ 以下、局在射影からの反対井戸遷移は $4r/(1+4r)$ 以下、2モード漏れは $O(r)$ である。

<!-- theorem-start:proof -->
**証明（R140の傾斜保持節）**

2モード内の一般入力上界は射影の作用素ノルム評価、局在入力の強い上界はR140の遷移式から従う。B.5の漏れと保持残差を全変動距離の三角不等式で加える。上の尺度選択は高速切替と高モード抑制を同時に満たし、$r\to0$ で誤差を零へ送る。証明終。
<!-- theorem-end:proof -->

この証明が抑えるのは各時刻の左右周辺占有率である。同じ試行の $X$ が有限記録時間中に安全井戸を離れないという経路事象は周辺分布だけから従わず、R143ではR162の入射停止と辺ゲート閉鎖からその失敗率 $\varepsilon_{\rm res}$ を別に評価する。

## B.7 R143の有限コントラスト補題

対称性により

```math
\langle\phi_0|\Pi_L|\phi_0\rangle
=
\langle\phi_1|\Pi_L|\phi_1\rangle
=
\frac12.
```

従って偶奇基底の効果は本文の $E_L$ である。Hadamard変換で対角化すると固有値は $1/2\pm B_W$ である。$B_W\geq0$ とし、$\eta_W=1/2-B_W$ と置けば

```math
E_L
=
\begin{pmatrix}
1-\eta_W&0\\
0&\eta_W
\end{pmatrix}_{L,R}.
```

分析器後の局在基底対角を $(p_+,p_-)=(p_+,1-p_+)$ とすると

```math
P_L
=
(1-\eta_W)p_+
+
\eta_W(1-p_+)
=
\eta_W+(1-2\eta_W)p_+.
```

差は $\eta_W|1-2p_+|\leq\eta_W$ である。

<!-- theorem-start:proof -->
**証明（R143の有限コントラスト補題）**

上の2次行列計算が理想2モードの有限コントラスト式を与える。分析器、漏れ、matching、固定、無反応、記録による各実分布を中間分布として挿入し、全変動距離の三角不等式を順に使えば本文の誤差和を得る。無反応成分は理想分布側に質量0で追加するため、事後再規格化はない。証明終。
<!-- theorem-end:proof -->

## B.8 大域階数1と枝別共分散の違い

入力共分散が $C_Z=cc^\dagger$ なら、付録L.2の階数1共分散の支持補題により $Z=\alpha c$ がほとんど確実に成り立つ。結果事象 $R=s$ で条件付けても、交換前の $Z$ の方向は $c$ のままである。一般の $c$ は同時に $|L\rangle$ と $|R\rangle$ に平行ではないため、条件付けだけでは2つの測定後固有状態を作れない。

結果別テンプレート交換は、この不足を物理写像として補う。交換前の信号浴を捨てず使用済みテンプレートへ移すので、異なる入力を同じ出力へ不可逆に押しつぶさない。

## B.9 局所記録剪断の正準性

1個の記録セルについて

```math
H_{\rm rec}
=
g(t)P^R\chi(X)
```

とする。単位面積パルスのHamilton方程式は

```math
Q^R_+
=
Q^R_-+\chi(X_-),
\qquad
P^R_+
=
P^R_-,
```

```math
P_{X,+}
=
P_{X,-}
-
P^R_-\nabla\chi(X_-),
\qquad
X_+=X_-.
```

である。これはHamiltonian流なので正準的である。$P^R_-=0$ なら $X$ への反作用は零である。$|P^R_-|\leq\delta_R$ なら反作用は $\delta_R\|\nabla\chi\|$ 以下であり、記録誤差台帳へ入る。

左右の $\chi_s$ は空間的に分離した支持を持つ。安全領域では片方だけが1である。支持が重なる分離面近傍を無反応領域とするため、1試行に2つの排他的安全記録が同時に立つことはない。

## B.10 結果別テンプレート交換

信号浴と枝 $s$ のテンプレートを $Z$、$T_s$ と書く。交換生成子を

```math
G_s
=
i\mathcal J_0
\left(
Z^\dagger T_s
-
T_s^\dagger Z
\right)
```

とする。その角 $\theta$ の流れは

```math
Z_+
=
\cos\theta\,Z_-
+
\sin\theta\,T_{s,-},
```

```math
T_{s,+}
=
-\sin\theta\,Z_-
+
\cos\theta\,T_{s,-}.
```

$\theta=\pi/2$ で完全交換となる。安全枝では局所因子 $\chi_s(X)=1$ がこの結合だけを開き、他枝では零にする。無反応領域では完全固有状態を主張しない。

テンプレート共分散が $|s\rangle\langle s|$ なら、完全交換後の信号共分散も同じである。角誤差 $|\delta\theta|$、テンプレート誤差 $\delta_{\rm tpl}$、分岐漏れ $\delta_{\rm gate}$ がある場合、固定作用殻上でtrace距離は

```math
\varepsilon_{\rm br}
\leq
2|\delta\theta|
+
\delta_{\rm tpl}
+
\delta_{\rm gate}
```

と評価できる。係数2はunitary回転の作用素ノルム評価から取った保守的上界である。

## B.11 R143の証明

初期操作面と分析器後操作面へ共通R170を適用する。対応する理想分布を $p^{\rm in}$、$p^{\rm out}$ とし、実分布を $\widetilde p^{\rm in}$、$\widetilde p^{\rm out}$ とすれば

```math
D_{\rm TV}
\left(
\widetilde p^{\rm in},p^{\rm in}
\right)
\leq
\varepsilon_{170}^{\rm in},
\qquad
D_{\rm TV}
\left(
\widetilde p^{\rm out},p^{\rm out}
\right)
\leq
\varepsilon_{170}^{\rm out}.
```

この2項は付録K.6の容量、作用殻、混合、衝突、辺閉鎖、局所記録、無反応を既に含む。B.11ではW型に固有なHopf方向、分析器、2モード漏れ、有限コントラスト、傾斜固定、結果別テンプレート交換だけを追加する。全変動距離の縮小性と三角不等式から

```math
D_{\rm TV}
\left(
p^{\rm obs},p^{\rm id}
\right)
\leq
\varepsilon_{170}^{\rm in}
+\varepsilon_{170}^{\rm out}
+\varepsilon_{\rm Hopf}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\eta_W
+\varepsilon_{\rm lock}
+\varepsilon_{\rm res}
+\varepsilon_{\rm guard}
+\varepsilon_{\rm br}
+\varepsilon_{\rm post}.
```

安全枝ではB.10により信号共分散が $|s\rangle\langle s|$ へ近づく。記録後にR161をtemplate方向へ作用させると、条件付き粒子位置分布は $\pi^\delta(s)$ から $\varepsilon_{\rm post}$ 以内になる。従って枝別共同状態の条件付きGibbs整合誤差は $\varepsilon_{\rm br}+\varepsilon_{\rm post}+O(\eta_W)$ である。

<!-- theorem-start:proof -->
**証明（R143）**

R181AのW型2モード系で信号bath方向を準備し、R170で初期粒子位置枝を作る。衝突熱浴を切ってR140で任意軸を左右基底へ写し、分析器終了後の信号へR170を再適用する。R140の保持節で傾斜保持、R143の補題でW型有限コントラストを評価する。B.9の局所剪断で既存の $X$ を記録し、B.10の結果別正準交換で安全枝の条件付き共分散を作る。最後にtemplate方向へ再平衡化する。共通instrument誤差はR170、M47固有誤差は上の三角不等式、条件付き状態誤差は交換と局在裾の評価で抑えられる。証明終。
<!-- theorem-end:proof -->

この証明は旧連続matching保存を使わない。付録Lの条件付き状態数、付録Kの有限混合率、有限衝突誤差、辺閉鎖誤差を使う。一方、作用容量結合、fiber内平衡化、枝対称性を含む有限局所Hamiltonianと、信号bath保持controllerの完全な反作用は別の未導出事項である。

## B.12 逐次測定誤差

理想2段核を $K_1,K_2$、実核を $\widetilde K_1,\widetilde K_2$ とする。各入力安全状態について

```math
\sup_z
D_{\rm TV}
\left(
\widetilde K_j(z,\cdot),
K_j(z,\cdot)
\right)
\leq
\delta_j
```

なら、核の縮約性から

```math
D_{\rm TV}
\left(
\mu\widetilde K_1\widetilde K_2,
\mu K_1K_2
\right)
\leq
\delta_1+\delta_2.
```

第1段条件付き状態が理想射影からtrace距離 $\delta_{\rm post}$ だけずれる場合、2値効果に対する確率差は $\delta_{\rm post}/2$ 以下である。従って2段誤差は

```math
\delta_1
+
\delta_2
+
\frac12\delta_{\rm post}
```

で抑えられる。同軸では理想反対結果が零であるため、実反対結果は同じ上界以下である。

## B.13 記録後の逆計算とreset

装置内部を $z$、測定前情報を受け取る使用済みセルを $w_s$、外部記録を $R_s$ とする。安全枝の理想写像は概念的に

```math
(z_0,w_0,0_R)
\longmapsto
(z_s,w_s,0_R)
\longmapsto
(z_s,w_s,R_s)
\longmapsto
(z_0,w_s,R_s)
```

である。最後の逆計算は記録剪断と信号テンプレート交換を逆実行せず、時計、傾斜駆動器、比較補助だけを戻す。測定前情報は $w_s$、結果は $R_s$ に残るため、写像は1対1である。

交換resetの漸化式

```math
d_{n+1}
\leq
a d_n+b,
\qquad
a=|\cos\phi|<1,
\qquad
b=\varepsilon_{\rm cyc}+|\sin\phi|\sigma_E
```

を反復すると

```math
d_n
\leq
a^nd_0
+
\frac{1-a^n}{1-a}b
```

となり、本文の上極限を得る。

## B.14 R144の証明

固定有限段数 $N$ について、各段の初期再平衡化、分析器、分析器後再平衡化、辺閉鎖、傾斜切替、記録、テンプレート交換、測定後再平衡化を共通時計の重ならない窓へ割り当てる。各段の衝突セル、使用済みテンプレート、記録セルを別に用意すれば、前向き写像は有限個の正準流と有限セル散乱の合成である。観測後、内部補助を逆順に戻し、周期末にfresh-cell交換を行う。

結果分布についてはB.12を反復し

```math
D_{\rm TV}
\left(
p_N^{\rm obs},p_N^{\rm id}
\right)
\leq
\sum_{j=1}^N
\left(
\varepsilon_{{\rm inst},j}
+
\frac12\delta_{{\rm post},j}
\right)
```

を得る。周期末偏差はB.13の上界に従う。固定 $N$ と固定周期数 $K$ なら、必要な記録セルと使用済みセルも有限である。$K\to\infty$ を固定容量で実現するとはしない。

<!-- theorem-start:proof -->
**証明（R144）**

各測定段にR143を適用し、独立な衝突セル、テンプレート、記録セルを割り当てる。有限個の拡大正準流の合成は正準的であり、B.12が前向き分布誤差、B.13が内部帰還誤差を与える。永久記録と使用済み状態を外部セルへ保持するため、内部補助だけを準備集合へ戻せる。証明終。
<!-- theorem-end:proof -->

R144は各段でR164の作用殻準備とR161の有限時間再平衡化を明示的に走らせるため、周期間のmatching保存を仮定しない。ただしfiberとcontrollerを含む周期全体の熱力学収支は本証明に含まれない。

## B.15 連続性障害と無反応

連結な初期領域から滑らかな有限時間Hamiltonian流で得る写像は連続であり、その像は連結である。2つの異なる離散固有状態だけを両方含む像は連結でない。従って、安全な左右結果の間には、遷移領域または無反応領域が必要である。

この一般事実はR112の安全比較・無反応節を使う。M47の局所記録では、分離面近傍、傾斜切替中、高モード漏れが大きい領域を無反応へ含める。無反応率を有限パラメータで厳密零にせず、理想2値分布側へ質量0の第3結果を追加して全変動距離を評価する。

## B.16 資源と適用範囲

1段の装置は少なくとも次を必要とする。

1. 信号浴の2正準対。
2. 左右テンプレートの4正準対。
3. 左右記録ポインターの2正準対。
4. 傾斜制御と共通時計の有限正準対。
5. 粒子位置の局所位置と共役運動量。
6. 条件付き作用殻fiber、容量controller、fiber内混合器。
7. 条件付き障壁controller、辺ゲート、有限衝突セル。
8. 使用済み信号、衝突履歴、制御履歴を保持する外部セル。

これは下界でも最適構成でもない。能動部は固定有限段数と固定観測時間に対して有限、永久記録と使用済み状態は実験周期数 $K$ に対して $O(K)$ 以上である。深いW型極限で $J$ が指数的に小さくなる場合、零傾斜回転時間 $\mathcal J_0/J$ は増大する。$\delta\downarrow0$ では付録Kの有効自由エネルギー幅、衝突流束、混合時間に加え、付録Lの作用殻剛性も増大する。誤差だけを零へ送り、時間、エネルギー、セル数、制御帯域を固定したとは扱わない。

本付録は、W型2モード外の一様連続極限、R164の作用容量結合とfiber内平衡化を含む有限局所Hamiltonian、信号bath保持controllerの完全な反作用、周期全体の微視的熱力学収支、無期限反復、Zeno効果を証明しない。全時刻matching保存は証明対象から外し、操作面ごとの作用殻準備と再平衡化へ置き換えた。
