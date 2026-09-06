@number: G
@chapter: 付録
@title: Q3-3A--Q3-3C・Q3-4A・Q3-4B・Q3-5の詳細形と証明
@status: 第7章で一度だけ宣言したR123--R125とR182について、井戸型・調和型・W型の低位束縛状態、純位相緩和、有限障壁、W型周期トンネル、最小2経路干渉の証明を与える。

## G.1 記法と証明範囲

本付録では、第7章の定理文を再掲するのではなく、その簡潔な定理文に対応する完全な仮定と結論を示してから証明する。Q3-3AとQ3-3Bでは1次元井戸型・調和型ポテンシャルの有限個の低位状態を扱い、R123の有限環境純位相部は任意の固定有限非縮退エネルギー列へ適用する。Q3-3CとQ3-4BではR182の対称W型を扱う。Q3-4Aでは3頂点鎖、Q3-5では2頂点再結合器を使い、位置読出しは第6.12--6.14節と付録NのM54 spatial/R161--R184へ全変動距離で接続する。

源、シャッター、幾何学的開口、散乱状態、吸収器、初回到達時刻、多画素スクリーン、永久記録、全検出器のHamiltonianは本付録の仮定にも結論にも入れない。

## G.2 R123の証明：束縛状態とエネルギー保存型純位相緩和

**証明で用いる設定と評価。**

正数 $\ell,m,\omega,\mathcal J_0$ と有限モード数 $K$ を固定する。

1. 区間 $(0,\ell)$ のDirichlet井戸を $N$ 個の内部格子点で離散化すると、生成子 $h_N^{\rm well}$ は単純固有値

```math
E_{k,N}^{\rm well}
=
\frac{2\mathcal J_0^2}{ma^2}
\sin^2
\left(
\frac{k\pi}{2(N+1)}
\right),
\qquad
a=\frac{\ell}{N+1},
\qquad
1\leq k\leq N
```

と規格化固有ベクトル

```math
u_{k,N}(j)
=
\sqrt{\frac{2}{N+1}}
\sin
\left(
\frac{k\pi j}{N+1}
\right)
```

を持つ。固定 $k$ について固有値、格子密度 $|u_{k,N}(j)|^2/a$、節の位置は連続Dirichlet井戸の値へ収束し、固有値誤差は $O(a^2)$ である。
2. 区間 $(-L,L)$ のDirichlet格子に調和型ポテンシャル $m\omega^2x^2/2$ を置いた生成子 $h_{N,L}^{\rm osc}$ は単純固有値を持ち、第 $k$ 固有ベクトルはちょうど $k$ 回符号を変える。固定 $k<K$ について、$a\to0$、$L\to\infty$ とすると

```math
E_{k,N,L}^{\rm osc}
\longrightarrow
\mathcal J_0\omega
\left(k+\frac12\right)
```

であり、密度と節位置も対応するHermite--Gauss状態へ収束する。適切な正数 $C_k,c_k$ により誤差は

```math
\left|
E_{k,N,L}^{\rm osc}
-
\mathcal J_0\omega
\left(k+\frac12\right)
\right|
\leq
C_k
\left(
a^2+e^{-c_kL^2}
\right)
```

と抑えられる。
3. 井戸型・調和型に限らず、任意の固定有限非縮退エネルギー列の先頭 $K$ モードの作用を $I_n=\mathcal J_0|b_n|^2$ とし、環境に $K$ 個の正準対 $(\theta_n,P_n)$ を置く。自律Hamiltonian

```math
H_{\rm deph}
=
\sum_{n=0}^{K-1}
\frac{E_n}{\mathcal J_0}I_n
+
\sum_{n=0}^{K-1}
\frac{P_n^2}{2M_n}
+
\frac{\lambda}{\mathcal J_0}
\sum_{n=0}^{K-1}
I_nP_n
```

を採用する。$\lambda>0$ とし、初期環境運動量を互いに独立な $P_n=\pm p_*$ の等重み集団で調製し、系の初期調製とは独立にする。環境を読まずに縮約した相関行列 $C_{nm}(t)$ は

```math
C_{nn}(t)=C_{nn}(0),
```

```math
C_{nm}(t)
=
C_{nm}(0)
\exp
\left[
-\frac{i(E_n-E_m)t}{\mathcal J_0}
\right]
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
\qquad n\neq m
```

を満たす。従って

```math
T_{\rm dec}
=
\frac{\pi\mathcal J_0}{2\lambda p_*}
```

で全ての非対角相関が厳密に零となり、対角占有率は全時刻で厳密に保存される。任意の $0<\delta<1$ に対し

```math
\mathcal W_\delta
=
\left[
T_{\rm dec}
-
\frac{\mathcal J_0}{\lambda p_*}
\arcsin\sqrt\delta,
\quad
T_{\rm dec}
+
\frac{\mathcal J_0}{\lambda p_*}
\arcsin\sqrt\delta
\right]
```

では非対角減衰因子が $\delta$ 以下である。最初の完全コヒーレンス回復時刻は

```math
T_{\rm rec}
=
\frac{\pi\mathcal J_0}{\lambda p_*}
=
2T_{\rm dec}
```

である。全Hamiltonianと注目系エネルギーはともに保存されるが、注目系は環境と相互作用し、環境を読まないため縮約記述では開放系である。

<!-- theorem-start:proof -->
**証明（R123）**

井戸型生成子を

```math
(h_N^{\rm well}u)_j
=
\frac{\mathcal J_0^2}{2ma^2}
\left(
2u_j-u_{j-1}-u_{j+1}
\right),
\qquad
u_0=u_{N+1}=0
```

とする。正弦加法公式を代入すれば定理の固有対を直接得る。$1\leq k\leq N$ で正弦の引数は厳密に増えるため固有値は単純で、第 $k$ ベクトルは $k-1$ 個の節区間を持つ。固定 $k$ で $\sin x=x+O(x^3)$ を使うと

```math
E_{k,N}^{\rm well}
=
\frac{\mathcal J_0^2\pi^2k^2}{2m\ell^2}
+O(a^2)
```

となる。$u_{k,N}/\sqrt a$ の区分線形補間は $\sqrt{2/\ell}\sin(k\pi x/\ell)$ へ一様に収束するので、密度は $L^1$ で、単純な内部零点は位置について収束する。

調和型生成子は

```math
(h_{N,L}^{\rm osc}u)_j
=
\frac{\mathcal J_0^2}{2ma^2}
\left(
2u_j-u_{j-1}-u_{j+1}
\right)
+
\frac12m\omega^2x_j^2u_j
```

である。これは全ての副対角成分が非零の実対称三重対角行列なので固有値は単純であり、離散Sturm振動定理により第 $k$ 固有ベクトルは $k$ 回符号を変える。

格子ベクトルの区分線形補間をDirichlet区間の関数とみなす。差分運動エネルギーは補間関数の微分二乗積分に一致し、ポテンシャル項はRiemann和として収束する。従って離散二次形式は連続区間の二次形式へ上からも下からも収束する。上からの評価には先頭 $k+1$ 個の連続固有関数の格子標本を、下からの評価にはエネルギー有界列の弱コンパクト性を使う。min--max原理により各固定低位固有値と固有空間が収束する。固有値が単純なので位相を選べば固有ベクトル自体が収束し、密度の $L^1$ 収束と単純零点の収束が従う。中心差分の局所切断誤差は滑らかな固有関数上で $O(a^2)$、区間外のHermite--Gauss尾部は $O(e^{-c_kL^2})$ なので、孤立固有値の摂動評価から表示した上界を得る。

次に純位相緩和を示す。$H_{\rm deph}$ はモード位相と環境角 $\theta_n$ に依存しないため、Hamilton方程式から

```math
\dot I_n=0,
\qquad
\dot P_n=0,
\qquad
i\mathcal J_0\dot b_n
=
(E_n+\lambda P_n)b_n
```

を得る。従って

```math
b_n(t)
=
b_n(0)
\exp
\left[
-\frac{i(E_n+\lambda P_n)t}{\mathcal J_0}
\right].
```

$n\neq m$ では独立な2個の二点運動量を平均するため

```math
\mathbb E
\exp
\left[
-\frac{i\lambda(P_n-P_m)t}{\mathcal J_0}
\right]
=
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
```

$n=m$ では因子は1である。これで縮約相関式が従う。$T_{\rm dec}$、$\mathcal W_\delta$、$T_{\rm rec}$ は余弦因子へ代入すればよい。

$I_n$ と $P_n$ が全て一定なので、$H_{\rm deph}$、注目系エネルギー $\sum_nE_nI_n/\mathcal J_0$、各占有率 $I_n/\sum_mI_m$ は厳密に保存される。一方、$\lambda\neq0$ では系の位相速度が読まない環境運動量に依存する。従って全系は有限自由度の閉じたHamiltonian系だが、その環境を縮約した注目系はエネルギー交換を伴わない開放系である。
<!-- theorem-end:proof -->

## G.3 R124の証明：3頂点有限障壁の障壁値未満確率移動

**証明で用いる設定と評価。**

正数 $\kappa,V$ に対し、頂点集合を障壁手前 $\{L\}$、障壁 $\{B\}$、障壁反対側 $\{R\}$ に分け、生成子を

```math
h_{\rm bar}
=
\begin{pmatrix}
0&-\kappa&0\\
-\kappa&V&-\kappa\\
0&-\kappa&0
\end{pmatrix}
```

とする。障壁値を $V$ とし、

```math
E_-
=
\frac{V-\sqrt{V^2+8\kappa^2}}{2},
\qquad
\alpha
=
\left(
1+\frac{E_-^2}{2\kappa^2}
\right)^{-1/2}
```

と置く。零固有ベクトル $a=(|L\rangle-|R\rangle)/\sqrt2$ と、$E_-$ の規格化固有ベクトル

```math
v_-
=
\frac{\alpha}{\sqrt2}
\left(
|L\rangle+|R\rangle
\right)
-
\frac{E_-\alpha}{\sqrt2\kappa}
|B\rangle
```

から

```math
b_0
=
\frac{a+v_-}{\sqrt2}
```

を調製する。この初期状態は

```math
\mathbf 1_{[V,\infty)}
(h_{\rm bar})b_0
=
0
```

を満たす。有限時刻

```math
T_{\rm bar}
=
\frac{\pi\mathcal J_0}{|E_-|}
```

では

```math
p_R(0)
=
\frac{(1-\alpha)^2}{4},
\qquad
p_R(T_{\rm bar})
=
\frac{(1+\alpha)^2}{4},
```

従って

```math
p_R(T_{\rm bar})-p_R(0)=\alpha>0
```

である。M54 spatial/R184の初期選択と終位置記録から得る分布 $q_t$ が $t=0,T_{\rm bar}$ の各理想位置分布から全変動距離 $\varepsilon_{184}$ 以内なら

```math
q_{T_{\rm bar}}(R)-q_0(R)
\geq
\alpha-2\varepsilon_{184}.
```

従って $\varepsilon_{184}<\alpha/2$ なら記録後にも正の増分が残る。

<!-- theorem-start:proof -->
**証明（R124）**

$s=(|L\rangle+|R\rangle)/\sqrt2$ とすると、$a$ は固有値0を持ち、$\{s,|B\rangle\}$ 上の行列は

```math
\begin{pmatrix}
0&-\sqrt2\kappa\\
-\sqrt2\kappa&V
\end{pmatrix}.
```

残る固有値は

```math
E_\pm
=
\frac{V\pm\sqrt{V^2+8\kappa^2}}{2}
```

である。$E_-<0<V<E_+$ なので、$b_0$ のスペクトル支持 $\{E_-,0\}$ は障壁値 $V$ より真に低い。表示した $v_-$ は直接代入により $E_-$ 固有ベクトルであり、$\alpha$ の定義により規格化されている。

$T_{\rm bar}$ では $a$ の位相は変わらず、$v_-$ の位相は $-1$ になる。従って

```math
b(T_{\rm bar})
=
\frac{a-v_-}{\sqrt2}.
```

$R$ 成分を取ると、初期振幅は $(\alpha-1)/2$、終期振幅は $-(1+\alpha)/2$ である。二乗差は $\alpha$ となる。初期の反対側裾を零と置かず、その厳密値を基準にしている。

全変動距離が $\epsilon$ 以下なら任意事象の確率差は $\epsilon$ 以下である。初期と終期の2回について三角不等式を使えば、読出し増分は理想増分から最大 $2\epsilon$ だけ減り得る。これで結論を得る。
<!-- theorem-end:proof -->

## G.4 R125の証明：2頂点再結合器のコヒーレンス差と位相差

**証明で用いる設定と評価。**

直交する2経路入力を有限グラフの頂点 $|L\rangle,|R\rangle$ とし、同一のSchrödinger型生成子

```math
h_{\rm int}
=
\kappa
\left(
|L\rangle\langle R|
+
|R\rangle\langle L|
\right),
\qquad
\kappa>0
```

を使う。コヒーレント入力と同じ経路重みの非干渉混合を

```math
|\psi_\phi\rangle
=
\frac{|L\rangle+e^{i\phi}|R\rangle}{\sqrt2},
\qquad
\rho_{\rm mix}
=
\frac12
\left(
|L\rangle\langle L|
+
|R\rangle\langle R|
\right)
```

とする。有限時刻

```math
T_{\rm int}
=
\frac{\pi\mathcal J_0}{4\kappa}
```

の位置分布は

```math
p_\phi
=
\left(
\frac{1+\sin\phi}{2},
\frac{1-\sin\phi}{2}
\right),
\qquad
p_{\rm mix}
=
\left(
\frac12,\frac12
\right).
```

特に

```math
D_{\rm TV}
\left(
p_{\pi/2},p_{\rm mix}
\right)
=
\frac12,
\qquad
D_{\rm TV}
\left(
p_{\pi/2},p_{-\pi/2}
\right)
=
1.
```

M54 spatial/R184が各入力の理想分布から全変動距離 $\varepsilon_{184}$ 以内なら、記録分布間の距離はそれぞれ $1/2-2\varepsilon_{184}$ 以上、$1-2\varepsilon_{184}$ 以上である。従って $\varepsilon_{184}<1/4$ なら、コヒーレント入力と混合の差、および相対位相変更による差がともに正に残る。

<!-- theorem-start:proof -->
**証明（R125）**

$\sigma_x=|L\rangle\langle R|+|R\rangle\langle L|$ と書けば、$\sigma_x^2=I$ なので

```math
U(T_{\rm int})
=
\exp
\left(
-\frac{i h_{\rm int}T_{\rm int}}{\mathcal J_0}
\right)
=
\frac{I-i\sigma_x}{\sqrt2}.
```

$|\psi_\phi\rangle$ へ作用させて各成分の絶対値を二乗すると表示した $p_\phi$ を得る。混合は $I/2$ であり、任意のユニタリ発展後も $I/2$ のままである。2点分布の全変動距離は第1成分差の絶対値に等しいため、一般に

```math
D_{\rm TV}
\left(
p_\phi,p_{\rm mix}
\right)
=
\frac{|\sin\phi|}{2},
```

```math
D_{\rm TV}
\left(
p_\phi,p_{\phi'}
\right)
=
\frac{|\sin\phi-\sin\phi'|}{2}.
```

$\phi=\pi/2$ と $-\pi/2$ を代入すれば理想距離を得る。各読出し分布に全変動距離 $\epsilon$ の誤差がある場合、三角不等式により2分布間距離は理想距離から最大 $2\epsilon$ だけ小さくなる。これで結論を得る。
<!-- theorem-end:proof -->

## G.5 達成範囲の切り分け

R123は、束縛固有状態の選択、冷却、射影収縮を導かない。有限環境の純位相緩和なので、コヒーレンスは $T_{\rm rec}$ で回復する。主張するのは $\mathcal W_\delta$ 内の有限時間減衰と、全時刻での対角占有率保存である。

R124は半無限散乱の透過率ではない。初期状態は厳密な低エネルギー部分空間に属し、初期右裾を含む基準値からの増分を示す。$V/\kappa$ が大きいと、初期右確率と障壁占有率は小さく、移動時刻は長くなる。

R125は固定目標で定めた最小2経路干渉である。幾何学的2開口装置または連続運転スクリーンへの拡張ではない。後2結果の粒子接続はM54 spatial/R161--R184を使い、M54、M54 spatial profile/M37 signal、初期作用殻、finite collision bath、記録までの単一Hamiltonian統合を条件に残す。

## G.6 R182の証明：W型低位スペクトル、障壁下二重項、M37分裂、空間周期

**証明で用いる設定。** 有限区間 $(-\ell,\ell)$、Dirichlet境界、$V_W\in C([-\ell,\ell])$ を満たす偶対称で下に有界なW型ポテンシャル $V_W$ を取り、

```math
H_W
=
-\frac{\mathcal J_0^2}{2m}
\frac{\mathrm d^2}{\mathrm dx^2}
+
V_W(x)
```

とする。中央障壁値を $V_b=V_W(0)$ とする。左右井戸内に互いに素な幅 $w$ の区間 $I_L,I_R$ があり、各区間で $V_W\leq V_b-\delta$ とする。$I_L,I_R$ 上のDirichlet基底正弦を規格化した試験関数 $u_L,u_R$ とする。

<!-- theorem-start:proof -->
**証明（R182）**

まず低位スペクトルの収束を示す。$H_W$ は有限区間の正則Sturm--Liouville作用素なので、Dirichlet固有値は単純で

```math
E_0<E_1<E_2<\cdots
```

となる。偶対称性から固有関数は偶または奇に選べ、基底状態は偶で節を持たず、第1励起は奇で中央に1節を持つ。一般に第 $n$ 状態は $n$ 個の内部節を持つ。

対称中心差分格子の二次形式を、格子ベクトルの区分線形補間へ移す。運動項は補間関数の微分二乗積分へ一致し、ポテンシャル項はRiemann和として連続二次形式へ収束する。固定 $K$ に対し、上からは先頭 $K$ 個の連続固有関数の格子標本、下からはエネルギー有界な補間列の弱コンパクト性を用いる。min--max原理により固定低位固有値と固有射影が収束する。固有値が単純なので符号を固定すれば固有関数自体が $L^2$ で収束し、1次元の正則性と単純零点を使って密度の $L^1$ 収束と節位置の収束が従う。対称格子では偶奇も保存される。

次に障壁値未満二重項を示す。各試験関数について

```math
\frac{
\langle u_{L/R},H_Wu_{L/R}\rangle
}{
\langle u_{L/R},u_{L/R}\rangle
}
\leq
V_b-\delta
+
\frac{\mathcal J_0^2\pi^2}{2mw^2}
<
V_b.
```

$u_L,u_R$ は支持が交わらないため、その2次元線形包の任意の非零ベクトルでもRayleigh商は両者の商の凸結合となり $V_b$ 未満である。Courant--Fischerのmin--max原理から

```math
E_1<V_b.
```

基底状態はさらに低いので $E_0<E_1<V_b$ である。1次元Dirichlet固有値の単純性から $G=E_2-E_1>0$。連続量

```math
\gamma_b=V_b-E_1>0,
\qquad
G>0
```

を固定すれば、格子収束により十分細かい格子で例えば $V_b-E_{1,N}>\gamma_b/2$、$E_{2,N}-E_{1,N}>G/2$ を選べる。

M37の静的正常モード生成子を考える。R86から

```math
h_{\rm ex}
=
\mathcal J_0\omega_0
\left[
\left(
I+
\frac{2h_W}{\mathcal J_0\omega_0}
\right)^{1/2}
-I
\right]
=
f_{\omega_0}(h_W).
```

有限格子のスペクトル定理により、$h_W\phi_n=E_n\phi_n$ なら

```math
h_{\rm ex}\phi_n
=
f_{\omega_0}(E_n)\phi_n.
```

従って固有ベクトル、parity、節、格子位置密度は厳密に共通である。さらに

```math
f_{\omega_0}'(E)
=
\left(
1+
\frac{2E}{\mathcal J_0\omega_0}
\right)^{-1/2}.
```

$\eta=2\|h_W\|/(\mathcal J_0\omega_0)<1$ なら全スペクトルで $1-\eta\leq1+2E/(\mathcal J_0\omega_0)\leq1+\eta$。平均値の定理を $E_0,E_1$ に適用して

```math
(1+\eta)^{-1/2}
\leq
\frac{
f(E_1)-f(E_0)
}{
E_1-E_0
}
\leq
(1-\eta)^{-1/2}
```

を得る。$E_1,E_2$ についても同じであり、正の第3gapはM37正常モードでも保たれる。

最後に完全位置分布を計算する。$\phi_0$ を正の偶関数、$\phi_1$ を左側で正となる奇関数に取る。最低二重項だけから作る

```math
\psi(x,t)
=
\frac{1}{\sqrt2}
\left[
e^{-iE_0t/\mathcal J_0}\phi_0(x)
+
e^{-iE_1t/\mathcal J_0}\phi_1(x)
\right]
```

の絶対値二乗を展開すれば第7章の $\rho(x,t)$ を得る。$C=[-c,c]$ 上では $\phi_0\phi_1$ が奇なので交差項の積分が零となり、$P_C$ は一定である。$P_L+P_C+P_R=1$ は規格化から従う。

$T_{1/2}=\pi\mathcal J_0/(E_1-E_0)$ では相対位相が $-1$ となり、

```math
\psi(x,T_{1/2})
=
e^{-iE_0T_{1/2}/\mathcal J_0}
\frac{\phi_0(x)-\phi_1(x)}{\sqrt2}.
```

偶奇性からその密度は $\rho(-x,0)$ である。一周期では相対位相が1へ戻り密度も初期へ戻る。第1励起は中央以外に節を持たず、符号を上のように選んだので左領域で $\phi_0\phi_1>0$、従って $B_c>0$ である。右領域の交差積は対称性により $-B_c$ なので、初期と半周期の差を取れば $P_R(T_{1/2})-P_R(0)=2B_c>0$ を得る。

厳密M37正常モードでは $E_n$ を $f(E_n)$ に置き換えるだけなので、$\Delta_{\rm ex}$ で定めた半周期・一周期に同じ鏡映と回帰が厳密に成り立つ。局所包絡との比較だけがR86の $\delta_{\rm loc}(\eta)$ を受ける。

R123の純位相Hamiltonianは、入力として有限非縮退エネルギー列と対応するモード作用だけを使う。従ってここで得たW型先頭 $K$ モードへそのまま適用でき、対角占有率を保存して有限時間に非対角相関を零にする。このdephasing系と上のコヒーレントトンネル系は別の運転である。同一運転でdephasingを有効にすると交差項を減衰させるため、Q3-4Bの理想周期証明には使わない。証明終。
<!-- theorem-end:proof -->