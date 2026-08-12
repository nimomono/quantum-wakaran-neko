@number: 3
@chapter: 本文
@title: M38の2頂点操作・実現配置測定・帰還周期
@status: 共通モデルを2頂点へ特殊化し、複素振幅場上のBloch球、任意のSU(2)、自律Rabi振動と、実現配置を読む任意軸測定、逐次測定、永久外部記録、内部逆計算、外部セル交換resetを接続してQ1-1からQ1-3を達成する。M37との同一ハードウェア化は主張しない。

## 3.1 M38と主張範囲

本章では、第2章の有限配置グラフを $\Omega=\{0,1\}$ へ特殊化した単一量子ビット型装置M38を構成する。複素振幅場は2つの実正準対

```math
(Q_1,P_1),
\qquad
(Q_2,P_2)
```

であり、複素振幅場を

```math
b
=
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix},
\qquad
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}}
```

と定める。全位相作用は

```math
I_{\rm ph}
=
\frac12
\sum_{j=1}^2
\left(
Q_j^2+P_j^2
\right)
=
\mathcal J_0 b^\dagger b
```

である。本章では固定作用面

```math
I_{\rm ph}=\mathcal J_0
```

を使うので、$b^\dagger b=1$ である。各試行には実現配置 $X\in\{0,1\}$ があり、鋭い基準準備では

```math
b=e_0,
\qquad
X=0
```

から開始する。状態準備、Rabi駆動、任意の $SU(2)$、測定分析器の各窓で、$b$ は正準流に、$X$ は同じ辺流から作る第2章の実現配置過程に従う。

M38は次の4層からなる。

1. 同じ2頂点複素振幅場上の可逆操作層。
2. 同じグラフプログラムで発展する実現配置と、これを出口で読む逐次測定層。
3. 外部記録セル、外部 reset セル、局所作用・角時計を加えた弱開放周期層。
4. 単一測定コアと有限長の循環メモリー／reset セル列を使う有限反復Zeno層。

任意の操作、測定軸、初期純粋状態を1つの可変プログラム装置で切り替えるとは主張しない。固定した有限プログラムごとに有限Hamiltonian を構成する。M35の選択器角は実現配置の局所更新、条件付き場準備、無反応境界の有限実装に使い、測定結果を $X$ と別に生成しない。M38とM37は同じ有効モデルの特殊化だが、ミクロハードウェアは同じでない。

## 3.2 固定作用面とBloch 球

共通位相変換

```math
b
\longmapsto
e^{i\gamma}b
```

は $I_{\rm ph}$ が生成する正準変換である。本章で使う操作量 $b^\dagger A b$、出力作用 $|(Wb)_s|^2$、比較ポインターはこの変換に不変である。

Bloch ベクトルを

```math
\boldsymbol r
=
b^\dagger\boldsymbol\sigma b
```

と定める。実正準座標では

```math
r_x
=
\frac{Q_1Q_2+P_1P_2}{\mathcal J_0},
```

```math
r_y
=
\frac{Q_1P_2-P_1Q_2}{\mathcal J_0},
```

```math
r_z
=
\frac{
Q_1^2+P_1^2-Q_2^2-P_2^2
}{2\mathcal J_0}
```

となる。

<!-- theorem-start:proposition -->
**命題（固定作用面の共通位相縮約）**
固定作用面 $I_{\rm ph}=\mathcal J_0$ は $S^3$ である。写像 $b\mapsto\boldsymbol r$ は

```math
|\boldsymbol r|=1
```

を満たし、同じBloch ベクトルを持つ2点は共通位相だけ異なる。従って、採用する操作・測定代数に対する有効状態空間は

```math
S^3/U(1)
\simeq
\mathbb{CP}^1
\simeq
S^2
```

である。
<!-- theorem-end:proposition -->

正準Poisson 括弧から

```math
\{b_j,b_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

が従うので、Bloch 成分は

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

を満たす。この縮約は、古典位相空間で共通位相変数が存在しないという主張ではない。採用する操作量と測定量が共通位相を識別しないことを表す。

有限次元量子力学を実Hamiltonian 系として表示できること自体は既知である [34]。本章の追加内容は、この表示をM35型の滑らかな測定、逐次記録、逆計算、外部セル reset へ接続した点にある。

## 3.3 任意のSU(2) 操作

任意の実ベクトル $\boldsymbol\Omega$ に対し、信号Hamiltonian を

```math
H_{\boldsymbol\Omega}
=
\frac{\mathcal J_0}{2}
b^\dagger
\left(
\boldsymbol\Omega\cdot\boldsymbol\sigma
\right)b
```

と置く。Hamilton方程式は

```math
i\dot b
=
\frac12
\left(
\boldsymbol\Omega\cdot\boldsymbol\sigma
\right)b,
```

```math
\dot{\boldsymbol r}
=
\boldsymbol\Omega\times\boldsymbol r
```

となる。全位相作用は厳密に保存される。

M35で使う局所位相回転と2モード交換の生成子は

```math
G_{Z,j}
=
\frac{Q_j^2+P_j^2}{2},
```

```math
G_X
=
Q_1Q_2+P_1P_2
```

である。前者の相対位相回転と後者の交換回転を有限回合成すれば、Euler 分解

```math
U
=
e^{-i\alpha\sigma_z/2}
e^{-i\beta\sigma_x/2}
e^{-i\gamma\sigma_z/2}
```

により任意の $U\in SU(2)$ を同じ2頂点複素振幅場上で厳密に実装できる。

<!-- theorem-start:theorem -->
**定理（2モード正準担体上の任意のSU(2)）**
任意の $U\in SU(2)$ に対し、$G_{Z,1}$、$G_{Z,2}$、$G_X$ の有限パルス列が存在し、その信号部分の正準写像は $b\mapsto Ub$ と一致する。各パルスは $I_{\rm ph}$ を保存し、逆操作はパルス順序と符号を反転して得られる。
<!-- theorem-end:theorem -->

これは固定された操作ごとの構成である。全ての $U$ を1本のエルゴード周期が自動的に列挙すること、位置ばねだけで $G_X$ を厳密に実装することは含まない。

## 3.4 自律Rabi 振動

駆動用の作用・角変数を $(J_d,\tau_d)$ とし、次の自律Hamiltonian を置く。

```math
H_{\rm Rabi}
=
\omega_dJ_d
+
\frac{\omega_q}{4}
\left(
Q_1^2+P_1^2-Q_2^2-P_2^2
\right)
```

```math
\quad
+
\frac{\Omega}{2}
\left[
\cos\tau_d
\left(
Q_1Q_2+P_1P_2
\right)
+
\sin\tau_d
\left(
Q_1P_2-P_1Q_2
\right)
\right].
```

$H_{\rm Rabi}$ は時計を含む有限自由度の時間非依存Hamiltonian である。相互作用は $J_d$ に依存しないので

```math
\dot\tau_d=\omega_d
```

が厳密に成立する。$b=e^{-i\tau_d\sigma_z/2}c$ と置くと、回転座標では

```math
i\dot c
=
\frac12
\left(
\Delta\sigma_z+\Omega\sigma_x
\right)c,
\qquad
\Delta=\omega_q-\omega_d
```

となる。

<!-- theorem-start:proposition -->
**命題（自律2モードRabi 公式）**
初期状態を $b(0)=e_1$ とする。第2モードへの作用比は

```math
P_{1\to2}(t)
=
\frac{\Omega^2}{\Omega^2+\Delta^2}
\sin^2
\left(
\frac{\sqrt{\Omega^2+\Delta^2}}{2}t
\right)
```

である。従って共鳴時の完全振動、一般離調での振動数、駆動強度依存性、離調による振幅低下が同じ有限自律Hamiltonian から厳密に従う。
<!-- theorem-end:proposition -->

このRabi モデルはM38の $QQ+PP$ と交差位置・運動量結合を使う。M37の時間依存位置ばね近似、反回転補正、Bloch--Siegert型補正はQ1-1の達成条件に使わない。

## 3.5 任意の Bloch 軸の測定

測定軸を単位ベクトル $\boldsymbol n$、結果を $s\in\{+1,-1\}$ とする。射影成分を

```math
P_s(\boldsymbol n)
=
\frac{
I+s\boldsymbol n\cdot\boldsymbol\sigma
}{2}
```

と定める。$W_{\boldsymbol n}\in SU(2)$ を

```math
W_{\boldsymbol n}
|\boldsymbol n,s\rangle
=
e_s
```

となるように選ぶ。分析器 $W_{\boldsymbol n}$ を複素振幅場へ作用させる間、実現配置も同じ2頂点グラフ流に従わせる。分析器出口の作用比は

```math
p_s(\boldsymbol n)
=
\left|
\langle\boldsymbol n,s|b\rangle
\right|^2
=
\frac{
1+s\boldsymbol n\cdot\boldsymbol r
}{2}
```

となる。R113により、出口で実現配置を読むと

```math
P(X=s)
=
p_s(\boldsymbol n)
```

である。Born型重みを測定器が新しく生成するのではなく、分析器を通過した実現配置の分布として得る。

検出した $X=s$ を制御ラッチとして、測定前場と分析器履歴を空テンプレートへ退避し、信号場を $|\boldsymbol n,s\rangle$ へ準備する。実現配置も対応する出力チャネルへ固定する。有限Hamiltonian実装では、実現配置の正則化、時間離散化、局所更新、比較境界に誤差が生じる。作動結果 $+1$、$-1$ と無反応 $\varnothing$ を完全結果集合とし、測定段 $j$ の全前向き誤差を

```math
\delta_j
\leq
\varepsilon_{{\rm reg},j}
+
\varepsilon_{{\rm disc},j}
+
\varepsilon_{{\rm sel},j}
+
\varepsilon_{{\rm win},j}
+
2\frac{w_{{\rm eff},j}}{\mathcal J_0}
+
\varepsilon_{{\rm cut},j}
```

で抑える。安全結果 $s$ では条件付き正準写像後の信号場は厳密に $|\boldsymbol n,s\rangle$ となり、測定前情報はテンプレートへ退避する。無反応試行を除外して2値分布を再規格化しない。

## 3.6 滑らかな厳密2値測定の連続性障害

滑らかな有限時間Hamiltonian 流は初期値に連続に依存する。この事実は、有限幅比較器で無反応領域を残す理由を与える。

<!-- theorem-start:theorem -->
**定理（連結入力に対する厳密2値像の障害）**
連結な初期領域 $X$ と、滑らかな有限時間Hamiltonian 流から得る連続写像 $F:X\to Y$ を考える。出力信号が全入力について相異なる2点 $y_+$、$y_-$ のいずれかだけを取り、両方が実現されると仮定すると矛盾する。
<!-- theorem-end:theorem -->

連続像 $F(X)$ は連結であるが、$\{y_+,y_-\}$ の2点集合で両点を含む部分集合は連結でない。従って、次の4条件は同時には成立しない。

1. 滑らかな有限時間Hamiltonian 流。
2. 連結な選択器入力領域。
3. 無反応または遷移領域がないこと。
4. 全入力を2つの異なる固有状態だけへ写すこと。

M38は安全セクターで厳密な固有状態を作り、その間を正式な無反応結果とする。無反応率を任意に小さくできるが、有限資源で厳密に零とはしない。

## 3.7 同軸反復測定

第1測定の軸を $\boldsymbol n$ とし、安全結果 $X_1=s$ が得られたとする。複素振幅場は厳密に $|\boldsymbol n,s\rangle$ へ準備され、実現配置は対応する分析器出口にある。新しい空テンプレートと新しい実現配置更新セルを持つ第2測定段も同じ軸に設定すれば、理想分布は

```math
p_t
=
\delta_{ts}
```

となる。

有限幅でも、安全枝で反対符号の結果は生じない。第2段の結果は同じ符号または無反応であり、

```math
P_{\rm safe}(-s\mid s)=0,
\qquad
P(\varnothing\mid s)\leq\delta_2
```

である。ここでも無反応を除く条件付き確率だけを表示して反復性を主張しない。

## 3.8 異軸逐次測定

第1軸を $\boldsymbol n$、第2軸を $\boldsymbol m$ とする。第1段で実現配置 $X_1=s$ を読み、複素振幅場を $|\boldsymbol n,s\rangle$ へ条件付き準備する。第2分析器を通った実現配置 $X_2=t$ の理想条件付き分布は

```math
P(t\mid s)
=
\left|
\langle\boldsymbol m,t|\boldsymbol n,s\rangle
\right|^2
=
\frac{
1+st\boldsymbol n\cdot\boldsymbol m
}{2}.
```

従って理想共同分布は

```math
\pi_{st}
=
\frac{
1+s\boldsymbol n\cdot\boldsymbol r
}{2}
\frac{
1+st\boldsymbol n\cdot\boldsymbol m
}{2}.
```

有限Hamiltonian実装に使う2段の更新角を $(\vartheta_1,\vartheta_2)$ とし、周期末に

```math
(\vartheta_1,\vartheta_2)
\longmapsto
(\vartheta_1+2\pi\alpha_1,
\vartheta_2+2\pi\alpha_2)
\pmod{2\pi}
```

と進める。$1,\alpha_1,\alpha_2$ が有理数体上で1次独立なら、この平行移動は2次元トーラス上で一意エルゴード的であり、Haar 測度は積測度になる。

<!-- theorem-start:theorem -->
**定理（R119：実現配置による2頂点操作・逐次測定周期）**

鋭い基準配置から固定純粋入力を準備し、固定軸 $\boldsymbol n,\boldsymbol m$、独立な2組の実現配置更新セル、互いに重ならない時計窓を用いる。各分析器出口で読む結果を $(X_1,X_2)$ とする。理想共同分布は $\pi_{st}$ に一致する。有限装置では結果空間を $\{+1,-1,\varnothing\}^2$ とし、理想分布を無反応成分0で拡張すれば、実分布 $p^{(2)}$ は

```math
D_{\rm TV}
\left(
p^{(2)},\pi
\right)
\leq
\delta_1+\delta_2
```

を満たす。安全結果では、実現配置を制御ラッチとして場を対応固有状態へ準備するため、同軸反復性と異軸条件付き分布が同じ周期で成立する。
<!-- theorem-end:theorem -->

同じ更新角を2段で再利用すると、第1結果で条件付けた後の第2角の一様性が一般に失われるため採用しない。一意エルゴード性は有限Hamiltonian集団の長期頻度を与えるが、結果列の独立同分布性や二項分布型有限標本揺らぎは与えない。

## 3.9 外部記録への正準コピー

各測定段で、実現配置の正出力領域、負出力領域、辺輸送中または比較接続域を読む滑らかな結果コード $\Pi_j(X,z)$ を作る。$\Pi_j$ は安全な正出力で $+1$、安全な負出力で $-1$、無反応領域で $(-1,1)$ の値を取る。外部記録セル $(Q_j^R,P_j^R)$ への記録生成子を

```math
G_{\rm rec}
=
\sum_{j=1}^2
P_j^R\Pi_j(X,z)
```

とする。理想空記録セル $Q_j^R=P_j^R=0$ から単位面積パルスを作用させると

```math
Q_j^R
\longmapsto
Q_j^R+\Pi_j(z),
\qquad
P_j^R
\longmapsto
P_j^R
```

となる。$P_j^R=0$ なので、記録窓中の装置変数 $z$ への反作用は零である。有限な $P_j^R$ 準備誤差は記録反作用として誤差台帳へ入れる。

記録後は、$Q_j^R$ が正安全域、負安全域、中間域のどこにあるかをそれぞれ $+1$、$-1$、無反応として読む。不連続な抽象ラベルを直接コピーせず、有限幅の実現配置検出関数をコピーするため、前節の連続性障害を再導入しない。

## 3.10 内部逆計算と外部セル reset

第2測定、第1測定の順に前向き操作を逆実行する。装置内部状態を $z$、結果 $y$ の記録値を $R_y$ と略記すると、理想写像は

```math
(z_0,0_R)
\longmapsto
(z_y,0_R)
\longmapsto
(z_y,R_y)
\longmapsto
(z_0,R_y)
```

となる。装置は準備状態へ戻り、外部記録は残る。全写像は正準的で1対1であり、結果情報を消去せず外部セルへ移している。

有限誤差と長期運転のため、装置の準備値からの偏差モードを $\delta a_j$、毎周期流入する外部空モードを $\eta_{n,j}$ とする。固定並進後の複素正準座標で、交換生成子を

```math
G_{\rm rst}
=
i\mathcal J_0
\sum_j
\left(
\delta a_j^*\eta_{n,j}
-
\eta_{n,j}^*\delta a_j
\right)
```

とする。交換角を $\phi$ とすると

```math
\delta a_j^+
=
\cos\phi\,\delta a_j^-
+
\sin\phi\,\eta_{n,j},
```

```math
\eta_{n,j}^+
=
-\sin\phi\,\delta a_j^-
+
\cos\phi\,\eta_{n,j}
```

である。$\phi=\pi/2$ では完全交換、$0<|\cos\phi|<1$ では装置偏差の収縮になる。旧装置状態は使用済み外部モードへ移り、Hamiltonian 可逆性は失われない。

1周期の内部逆計算残差を $\varepsilon_{\rm cyc}$、流入セル幅を $\|\eta_n\|\leq\sigma_E$ とすると、

```math
\limsup_{n\to\infty}
\|\delta a_n\|
\leq
\frac{
\varepsilon_{\rm cyc}
+
|\sin\phi|\sigma_E
}{
1-|\cos\phi|
}
```

を得る。結合強度を $g$ とすれば交換時間は

```math
T_{\rm rst}
=
\frac{\phi}{g}
```

である。弱い結合でも接触時間を長くすれば完全交換へ到達できる。本稿で「弱開放」と呼ぶのは結合強度または単位時間当たり交換が弱いという意味であり、1周期のreset 効果が必ず微小という意味ではない。

## 3.11 局所時計と資源

全ての操作を1つの作用・角時計 $(J_c,\tau_c)$ で自律化する。互いに重ならない時計窓を $g_r(\tau_c)$、各局所生成子を $G_r$ とし、

```math
H_{\rm cyc}
=
\Omega_cJ_c
+
\Omega_c
\sum_r
g_r(\tau_c)G_r
```

と置く。各窓は

```math
\int g_r(\tau_c)\,d\tau_c=1
```

に規格化する。$\dot\tau_c=\Omega_c$ なので、各生成子の流れが単位パルス面積で実行される。窓が重ならず、各 $G_r$ が自身の流れで保存される理想構成では

```math
\Delta J_c
=
-\int g_r'(\tau_c)G_r\,d\tau_c
=0
```

であり、時計作用も各窓後に戻る。$J_c$ に十分な正の余裕を持たせれば、周期中も正作用領域に保てる。

M35の正準対数は $3L+4$ なので、$L=2$ の1段測定は10正準対である。2段装置で信号2対と時計1対だけを共有する単純上界は

```math
2+2\times7+1=17
```

正準対である。2つの外部記録セルは1周期当たり2対を使う。信号、テンプレート、作用・閾値・内部記録を全て外部空モードと交換する保守的上界は1周期当たり14対である。選択器2対は無理数平行移動を続け、時計1対は周期運動を続けるので、この14対には含めない。

$K$ 実験周期を完全な有限閉鎖Hamiltonian 系へ埋め込む単純上界は、輸送自由度を除いて

```math
17+16K
```

正準対である。能動装置の大きさは一定だが、永久記録と使用済みreset 状態の保存量は $O(K)$ で増える。無期限運転だけが外部からのセル供給と使用済みセルの流出を必要とする。

$L=2$ の能動装置は1つの局所セル内へ置けるため、一般有限 $L$ で残る長距離時計配線問題は生じない。有限なパルス面積誤差、時計窓の重なり、外部セルの有限準備幅は最終誤差へ加える。

## 3.12 完全周期定理と達成判定

2段測定の前向き順序は、鋭い基準配置、準備回路、任意の $SU(2)$ 操作、第1分析器と実現配置検出、条件付き場準備、第2分析器と実現配置検出、増幅、外部記録である。その後に第2測定、第1測定、準備回路を逆計算し、最後に外部空モード交換を行う。

<!-- theorem-start:theorem -->
**定理（2頂点複素振幅場・実現配置の弱開放完全周期）**

固定純粋入力、固定された有限 $SU(2)$ 操作列、固定された2つのBloch 軸、任意の $\epsilon>0$ に対し、有限個の正準自由度からなる能動装置と外部記録・resetセル流路を構成できる。各結果は分析器出口の実現配置を読む。安全結果の測定後複素振幅場は厳密な対応固有状態である。無反応を含む2段結果分布と理想逐次射影分布の全変動距離、記録誤差、周期末準備集合からの偏差を全て $\epsilon$ 未満に選べる。全系の写像は正準的で1対1であり、装置は次周期の準備集合へ戻り、結果履歴と旧装置偏差は外部流へ残る。
<!-- theorem-end:theorem -->

理想Poincaré 写像は

```math
(z_*,\vartheta_1,\vartheta_2)
\longmapsto
\left(
z_*,
\vartheta_1+2\pi\alpha_1,
\vartheta_2+2\pi\alpha_2
\right)
```

である。誤差は、正準状態誤差、状態方向誤差、比較境界移動量、結果分布の全変動距離の順に変換して評価する。異なる単位の誤差を直接加えない。

以上により、Q1-1は複素振幅場上のBloch球、共通位相不変性、任意の $SU(2)$、Rabi振動を厳密に満たす。Q1-2は分析器後の実現配置検出として、任意軸、排他的安全結果、測定後固有状態、同軸反復、異軸逐次測定を制御された任意精度で満たす。Q1-3は実現配置記録、内部逆計算、弱開放reset、次周期復帰を制御された任意精度で満たす。

Q1-1からQ1-3の達成は、M38内部の固定純粋入力・固定有限プログラムに限る。次は含まない。

1. M37とM38の同一ハードウェア化。
2. 一般有限 $L$ の2段完全周期。
3. 可変プログラム全体の統一エルゴード測度。
4. 独立同分布または二項分布型有限標本揺らぎ。
5. 有限閉鎖系の固定容量で永久記録を無期限に蓄積すること。
6. 無反応なしの厳密2値測定。
7. reset の熱力学的最小仕事または総エネルギー収支。

これらはQ1-1からQ1-3を別の未確立仮説へ移したものではない。M38の達成範囲を超える一般化、資源評価、M0への統合課題である。
