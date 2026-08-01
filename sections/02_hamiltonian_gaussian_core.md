@number: 2
@chapter: 本文
@title: 粒子、構造化誘導場、外部流路の Hamiltonian
@status: 有限誘導場と固定射影を現行モデルとして定義する。正準性と線形場の方程式は厳密である。欠陥成分だけの減衰と有効短記憶化は外部スペクトルに依存する近似候補である。

## 2.1 有限誘導場モデル

粒子座標を $X\in\mathbb R^d$、運動量を $P\in\mathbb R^d$ とする。有限誘導場は $M_N$ 個の実正準対

```math
(Q,\Pi)
\in
\mathbb R^{M_N}\times\mathbb R^{M_N}
```

で表す。質量行列を座標変換で単位行列へ移した表示を用い、有限部分を

```math
H_N^{\rm fin}
=
\frac{|P|^2}{2m}
+
V(X)
+
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}K_NQ
-
G_N(X)^{\mathsf T}B^{\mathsf T}Q
+
H_{N}^{\rm nl}
```

とする。$K_N=K_N^{\mathsf T}>0$ は場の線形部分、$G_N:\mathbb R^d\to\mathbb R^r$ は粒子から場への一般化力、$B:\mathbb R^r\to\mathbb R^{M_N}$ は固定した直接結合方向、$H_N^{\rm nl}$ は必要に応じて加える弱い非線形内部混合である。

粒子と場の Hamilton 方程式は

```math
\dot X
=
\frac Pm,
\qquad
\dot P
=
-\nabla V(X)
+
\left[\nabla G_N(X)\right]^{\mathsf T}B^{\mathsf T}Q
-
\nabla_XH_N^{\rm nl},
```

```math
\dot Q
=
\Pi,
\qquad
\dot\Pi
=
-K_NQ
+
BG_N(X)
-
\nabla_QH_N^{\rm nl}.
```

従って線形場の直接駆動方向は $BG_N(X)$ である。結合条件を場のポテンシャル行列へ曖昧に埋め込まず、$B$ として独立に表示する。

## 2.2 静的な明・暗モード分解

$B$ の像を直接明部分空間

```math
\mathcal B_{\rm dir}
=
\operatorname{Ran}B
```

とする。これを含む固定明部分空間 $\mathcal B_{\rm B}$ と、その直交補空間 $\mathcal B_{\rm D}$ を選び、射影を $P_{\rm B},P_{\rm D}$ と書く。直接結合が暗モードを駆動しないための条件は

```math
P_{\rm D}B=0
```

である。

これは

```math
P_{\rm D}K_NB=0
```

を要求しない。一般に $P_{\rm D}K_NP_{\rm B}\neq0$ であり、場の内部発展によって明モードから暗モードへ作用が移る。この間接伝播は、欠陥移送、局所セクター間の交差応答、有限記憶を生む候補である。

$\mathcal B_{\rm B}$ と $\mathcal B_{\rm D}$ に適合した直交行列 $O_N$ を固定し、

```math
\widetilde Q=O_NQ,
\qquad
\widetilde\Pi=O_N\Pi
```

と変換する。座標と運動量へ同じ直交行列を作用させるので、この変換は正準である。変換後の $O_NK_NO_N^{\mathsf T}$ は一般にブロック対角ではない。従って静的な明・暗分解の正準性と、動力学的な直和分離を混同しない。

## 2.3 位相整合成分と欠陥成分

Fisher 側では、場の中に長時間保たれる位相整合成分と、外部へ移送したい欠陥成分を区別する必要がある。固定射影を

```math
P_{\rm c},
\qquad
P_\perp=I-P_{\rm c}
```

と書く。

$P_{\rm c}$ は次のいずれか、またはその組合せから事前に定める。

- $K_N$ の指定したスペクトル帯。
- 直接結合方向 $B$ と、その有限回の $K_N$ 作用が張る Krylov 部分空間。
- 装置が保存する作用または位相基準に対応する固定正準部分空間。
- Bell 側の局所、共通境界、暗モードを定める装置固定基底。

得られた $\rho$、欲しい波動関数、または目標 Fisher 応力を見て $P_{\rm c}$ を選んではならない。そうすると、導出すべき構造を射影へ先に書き込むことになる。

場の射影と、粒子運動量分散の分解も同一ではない。後者には第3章で枝指標を導入し、条件付き全分散公式を用いる。

## 2.4 外部流路を含む拡大全系

外部自由度を $(Y,\Theta)$、仕事貯蔵自由度を $z_{\rm work}$ とし、

```math
H_N^{\rm all}
=
H_N^{\rm fin}(X,P,Q,\Pi)
+
H_{\rm ext}(Y,\Theta)
+
\varepsilon_{\rm ext}
H_{\rm link}(Q,\Pi,Y,\Theta)
+
H_{\rm work}(z_{\rm work})
+
H_{\rm ctrl}
```

とする。$H_{\rm ctrl}$ は自律時計を含む設定変更、記録、再準備の有限相互作用をまとめた記号である。

全 Hamiltonian に外からの陽な時間依存がなければ、拡大全エネルギーは保存される。有限部分のエネルギー変化は Poisson 括弧により

```math
\frac{\mathrm d}{\mathrm dt}H_N^{\rm fin}
=
\left\{
H_N^{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm ctrl}
\right\}
```

と書ける。従って弱開放性は、有限部分の基本方程式へ非 Hamiltonian な摩擦を直接加えることではなく、外部自由度を消去した後の有限部分の収支として現れる。

## 2.5 選択的な弱漏れの候補

欠陥成分へ強く、位相整合成分へ弱く結合する候補を

```math
H_{\rm link}
=
\left(P_\perp Q\right)^{\mathsf T}C_\perp Y
+
\epsilon_{\rm c}
\left(P_{\rm c}Q\right)^{\mathsf T}C_{\rm c}Y
+
H_{\rm link}^{(\Pi)}
```

と書く。$0\leq\epsilon_{\rm c}\ll1$ とする。$H_{\rm link}^{(\Pi)}$ は必要な運動量結合を表す。

外部相関時間が短く、スペクトル密度が対象周波数帯で十分滑らかなら、外部消去後の線形化した平均振幅は概念的に

```math
\frac{\mathrm d}{\mathrm dt}
\begin{pmatrix}
P_{\rm c}Q\\
P_\perp Q
\end{pmatrix}
=
\begin{pmatrix}
A_{\rm c} & C_{{\rm c}\perp}\\
C_{\perp{\rm c}} & A_\perp
\end{pmatrix}
\begin{pmatrix}
P_{\rm c}Q\\
P_\perp Q
\end{pmatrix}
+
\eta_{\rm eff}(t)
```

となる。$\eta_{\rm eff}$ は外部消去後の有効雑音である。$A_\perp$ の実部が負で、$A_{\rm c}$ の減衰率が十分小さければ、欠陥成分だけが速く除去される。

目標とする時間尺度は

```math
\tau_{\rm corr}
\ll
\gamma_\perp^{-1}
\ll
\tau_{\rm coh},
\qquad
\gamma_{\rm c}
\ll
\gamma_\perp.
```

ここで $\tau_{\rm corr}$ は外部相関時間、$\gamma_\perp$ は欠陥減衰率、$\tau_{\rm coh}$ は位相整合成分を利用する時間、$\gamma_{\rm c}$ は整合成分の漏れ率である。

特定の有限外部スペクトルについて

```math
\|P_\perp Q(t)\|
\leq
C e^{-\gamma_\perp t}
\|P_\perp Q(0)\|
+
R_{\rm in}(t)
```

を一様に証明してはいない。$R_{\rm in}$ は外部からの流入補正である。従って「欠陥成分だけの指数減衰」は、外部スペクトル、弱結合極限、Markov 近似に依存する近似結果候補である。

## 2.6 弱漏れが担わない役割

選択的な漏れが実現しても、次は自動的には従わない。

1. 粒子の配置空間で Markov 拡散が生じること。
2. 前進・後退過程が同じ拡散係数を持つこと。
3. ミクロ反作用が Fisher 応力へ閉じること。
4. Bell 側の3モード作用殻が $U(3)$ 等方になること。
5. 非零の総作用半径が定常に保たれること。

純粋漏れは欠陥と再帰を抑える候補である。配置空間の二側拡散には条件付き均質化が必要であり、作用殻の方向準備には Hamiltonian な接方向混合が必要であり、非零半径の維持には流入または仕事源が必要である。

## 2.7 局所測定窓と長時間準備の分離

局所測定窓 $T_{\rm meas}$ では

```math
\varepsilon_{\rm open}
\ll1,
\qquad
\gamma_\perp T_{\rm meas}
\ll1
```

を要求し、有限部分を近似閉鎖系として扱う。一方、試行間の準備時間 $T_{\rm prep}$ では

```math
\gamma_\perp T_{\rm prep}
\gtrsim1
```

を許し、欠陥除去と再帰抑制を利用する。

同じ結合を測定中だけ人工的に切るのではなく、常時存在する弱結合を異なる時間窓で異なる次数として扱う。測定窓と準備窓の両方を満たすには

```math
T_{\rm meas}
\ll
\gamma_\perp^{-1}
\lesssim
T_{\rm prep}
```

という時間尺度分離が必要である。

## 2.8 本章の結論

粒子と構造化誘導場の直接結合を $B$ で明示し、暗モードを直接駆動しない条件を $P_{\rm D}B=0$ とした。静的な明・暗分解は厳密な正準変換であるが、$K_N$ の内部結合による間接伝播は残る。

位相整合射影は Hamiltonian の固定構造から事前に定める。外部への選択的な弱漏れは欠陥除去と再帰抑制の候補だが、その指数減衰には外部スペクトルと短記憶近似が必要であり、Fisher 応力または作用殻等方性の導出ではない。
