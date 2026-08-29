@number: G
@chapter: 付録
@title: Q3-3からQ3-5の詳細形と証明
@status: 第7章で一度だけ宣言したR123--R125について、低位束縛状態、純位相緩和、障壁値未満確率移動、最小2経路干渉の証明を与える。

## G.1 記法と証明範囲

本付録では、第7章の定理文を再掲するのではなく、その簡潔な定理文に対応する完全な仮定と結論を示してから証明する。Q3-3では1次元井戸型・調和型ポテンシャルの有限個の低位状態と、有限個の環境正準対を読まない純位相緩和を構成する。Q3-4では3頂点鎖、Q3-5では2頂点再結合器を使う。後2者については第6.14、6.15節と付録FのR170固定入力時刻位置instrumentへ全変動距離で接続する。

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
3. いずれかの模型の先頭 $K$ モードの作用を $I_n=\mathcal J_0|b_n|^2$ とし、環境に $K$ 個の正準対 $(\theta_n,P_n)$ を置く。自律Hamiltonian

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

である。各入力時刻に対するR170の出力分布 $q_t$ が $t=0,T_{\rm bar}$ の各理想位置分布から全変動距離 $\varepsilon_{170}$ 以内なら

```math
q_{T_{\rm bar}}(R)-q_0(R)
\geq
\alpha-2\varepsilon_{170}.
```

従って $\varepsilon_{170}<\alpha/2$ なら読出し後にも正の増分が残る。

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

R170固定入力時刻位置instrumentが各入力の理想分布から全変動距離 $\varepsilon_{170}$ 以内なら、読出し分布間の距離はそれぞれ $1/2-2\varepsilon_{170}$ 以上、$1-2\varepsilon_{170}$ 以上である。従って $\varepsilon_{170}<1/4$ なら、コヒーレント入力と混合の差、および相対位相変更による差がともに正に残る。

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

R125は固定目標で定めた最小2経路干渉である。幾何学的2開口装置または連続運転スクリーンへの拡張ではない。後2結果の読出し接続はR170を使い、作用容量結合から局所記録までの単一Hamiltonian統合を条件に残す。
