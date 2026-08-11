@number: D
@chapter: 付録
@title: M35一般有限基底測定の完全正準構成
@status: M35の一般有限L構成について、局所2モード回路、累積比較ポインター、無反応を含む結果集合、信号、テンプレート、レジスター、選択器、時計の全写像を追跡する。L=2の2段測定、外部記録、弱開放 reset は付録Bで扱う。

## D.1 正準自由度

信号とテンプレートを

```math
b,t
\in
\mathbb C^L,
\qquad
b_j
=
\frac{Q_j^{b}+iP_j^{b}}{\sqrt{2\mathcal J_0}},
\qquad
t_j
=
\frac{Q_j^{t}+iP_j^{t}}{\sqrt{2\mathcal J_0}}
```

とする。作用レジスター、閾値、内部記録、選択器、時計は

```math
(Q_k,P_k)_{k=1}^L,
\quad
(Q_U,P_U),
\quad
(Q_M,P_M),
\quad
(\vartheta,J_{\rm sel}),
\quad
(\tau,P_\tau)
```

である。正準対数は $3L+4$ である。$L=2$ では10正準対になる。

周期開始値を

```math
b=t=e_1,
```

```math
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
```

```math
J_{\rm sel}=J_*>0,
\qquad
P_\tau=E
```

とする。選択器角 $\vartheta$ だけを自由にする。

## D.2 時計窓と自律化

$\tau\in S^1$ とし、

```math
H_{\rm clk}
=
P_\tau
```

と置く。各時計窓 $g_r(\tau)$ は滑らかで、逐次実行する窓の支持は互いに交わらず、

```math
\int_0^1g_r(\tau)\,d\tau
=
1
```

とする。互いに素な辺の生成子は同じ窓へまとめてもよい。全周期を

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_{r=1}^{N_{\rm cyc}(L,W)}
g_r(\tau)G_r
```

とする。$\dot\tau=1$ なので、これは時計を含む1本の有限自律 Hamiltonian である。旧来の固定14窓表示は、基底回路の長さが $L$ と $W$ に依存するため使わない。

## D.3 隣接2モード回路による任意ユニタリ

単一モード位相回転と隣接交換の実生成子を

```math
G_{Z,j}
=
\frac{
\left(Q_j^b\right)^2
+
\left(P_j^b\right)^2
}{2},
```

```math
G_{X,j}
=
Q_j^bQ_{j+1}^b
+
P_j^bP_{j+1}^b
```

とする。複素表示では

```math
G_{Z,j}
=
\mathcal J_0|b_j|^2,
```

```math
G_{X,j}
=
\mathcal J_0
\left(
b_j^*b_{j+1}
+
b_{j+1}^*b_j
\right)
```

である。$G_{Z,j}-G_{Z,j+1}$ と $G_{X,j}$ の Poisson 交換子は、行列表現で

```math
Y_j
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

の方向を生成する。従って $Z$、$X$、$Z$ の有限列で任意の隣接 $U(2)$ を実装できる。各流れはユニタリ正準変換であり、全作用を厳密に保存する。

構成的分解を確認する。複素数 $a,c$ に対し、

```math
G(a,c)
=
\frac1{\sqrt{|a|^2+|c|^2}}
\begin{pmatrix}
a^*&c^*\\
-c&a
\end{pmatrix}
```

とすれば、

```math
G(a,c)
\begin{pmatrix}
a\\
c
\end{pmatrix}
=
\begin{pmatrix}
\sqrt{|a|^2+|c|^2}\\
0
\end{pmatrix}
```

である。任意の $W\in U(L)$ に対し、列ごとに下から隣接2行へこの変換を掛けると、$L(L-1)/2$ 回以下で対角位相だけが残る。逆向きに並べ、残った対角位相を $D$ とすれば

```math
W
=
V_1V_2
\cdots
V_{N_W}D,
\qquad
N_W
\leq
\frac{L(L-1)}2
```

という隣接2モード変換と対角位相回転の積を得る。$D$ は $L$ 個以下の単一モード位相回転で実装する [38,39]。

逆回路は

```math
W^\dagger
=
D^\dagger
V_{N_W}^\dagger
\cdots
V_2^\dagger
V_1^\dagger
```

であり、同じ辺を逆順・逆角で使う。固定状態だけを作る $U_{\rm prep}e_1=\chi$ は、下成分を順に消去することで $L-1$ 個以下の2モード混合と位相調整に分解できる。

## D.4 準備回路と測定基底

第1の局所回路で

```math
b=e_1
\longmapsto
U_{\rm prep}e_1
=
\chi
```

とし、第2の局所回路で

```math
b
=
W\chi
```

とする。両回路はC.3節の生成子だけからなり、全位相作用を厳密に保存する。逆計算では同じ回路を逆順に使うため、密な一括生成子 $K_W$ を装置へ置かない。

信号鎖とテンプレート鎖を並べ、同じ番号の信号・テンプレートを SWAP 用の辺で結ぶ。作用レジスターは別の1次元鎖に置き、$Q_U$ を $Q_1$ の隣へ置く。基底変換、累積比較、テンプレート経路はこの有限次数グラフ上で局所になる。

## D.5 作用、閾値、累積差の読出し

読出し時のモード作用を

```math
I_k
=
\mathcal J_0|b_k|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^LI_k
=
\mathcal J_0
```

とする。角の切断接続領域を除いて $f(\vartheta)=\vartheta/(2\pi)$ とし、

```math
G_{\rm read}
=
\sum_{k=1}^L
P_kI_k
+
P_U\mathcal J_0f(\vartheta)
```

と置く。Hamilton 方程式は

```math
\dot Q_k=I_k,
\qquad
\dot Q_U=\mathcal J_0f(\vartheta),
\qquad
\dot P_k=\dot P_U=0
```

を与える。$P_k=P_U=0$ なので、信号と選択器の方程式へ入る読出し反作用は零である。単位面積流の後に

```math
Q_k=I_k,
\qquad
Q_U=u
```

となる。

続いて

```math
G_{0}^{\rm cum}
=
-P_1Q_U
```

を作用させ、次に

```math
G_j^{\rm cum}
=
P_{j+1}Q_j,
\qquad
j=1,\ldots,L-2
```

を番号順に作用させる。帰納的に

```math
Q_j
=
\sum_{r=1}^jI_r-u
=
S_j-u,
\qquad
j=1,\ldots,L-1
```

を得る。逆計算では $G_j^{\rm cum}$ を逆番号順・逆符号で使い、最後に $G_0^{\rm cum}$ を逆にする。

## D.6 双曲型増幅と滑らかな比較

累積差を

```math
G_{\rm amp}
=
\Lambda
\sum_{j=1}^{L-1}Q_jP_j
```

で増幅する。単位面積流は

```math
Q_j
\longmapsto
e^\Lambda Q_j,
\qquad
P_j
\longmapsto
e^{-\Lambda}P_j
```

である。$P_j=0$ は保たれ、逆流は $\Lambda\mapsto-\Lambda$ で得られる。

滑らかな関数を

```math
\rho(z)
=
\begin{cases}
0,&z\leq0,\\
e^{-1/z},&z>0,
\end{cases}
```

```math
\sigma(z)
=
\frac{\rho(z+1)}{\rho(z+1)+\rho(1-z)}
```

とし、

```math
h_j
=
\sigma
\left(
\frac{Q_j}{X}
\right),
\qquad
h_0=0,
\qquad
h_L=1
```

と置く。$Q_1\leq\cdots\leq Q_{L-1}$ なので $h_1\leq\cdots\leq h_{L-1}$ である。従って

```math
c_k
=
h_k-h_{k-1}
```

は非負で総和1となる。

角の切断接続領域を $\mathcal C_{\rm cut}$ とし、安全セクターを

```math
\mathcal O_k
=
\left\{
\vartheta\notin\mathcal C_{\rm cut},
\quad
Q_j\leq-X\quad(j<k),
\quad
Q_j\geq X\quad(j\geq k)
\right\}
```

とする。これらは互いに素である。補集合を $\mathcal O_\varnothing$ と定める。結果は比較ポインターセクターで判定し、後段の $Q_M$ だけでは判定しない。

入力換算幅は $w=Xe^{-\Lambda}$ である。$u$ が一様なので、

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\mathcal O_\varnothing
\right)
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

となる。境界近傍が重なれば右辺は過大評価になる。

## D.7 隣接テンプレート経路と記録

隣接生成子を

```math
Y_{j,j+1}
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

とし、$\ell_j=1-h_j$ とする。最初に

```math
G_M^{(0)}
=
P_M
```

を作用させ、$Q_M=1$ とする。続いて $j=1,\ldots,L-1$ の順に

```math
G_j^{\rm route}
=
\frac{\pi\mathcal J_0}{2}
\ell_j
t^\dagger Y_{j,j+1}t
+
P_M\ell_j
```

を作用させる。

$\mathcal O_k$ では

```math
\ell_j
=
\begin{cases}
1,&j<k,\\
0,&j\geq k,
\end{cases}
```

なので、$t=e_k$、$Q_M=k$ となる。初期テンプレートの成分は実で、各 $Y_{j,j+1}$ の流れも実回転として作用する。従って全経路で

```math
t^\dagger Y_{j,j+1}t
=
0
```

が保たれる。$P_M=0$ と合わせ、$\ell_j(Q)$ の座標依存性がポインター共役運動量へ与える反作用は零である。

$\mathcal O_\varnothing$ では複数の $\ell_j$ が中間値を取り得る。例えば $\sum_j\ell_j$ が整数でも、全 $h_j$ が平坦部にあるとは限らない。従って整数の $Q_M$ は必要な内部記録だが、十分な結果判定ではない。

## D.8 正準 SWAP 、測定後基底、保持

SWAP 生成子を

```math
G_{\rm sw}
=
i
\left(
b^\dagger t-t^\dagger b
\right)
```

とする。$\pi\mathcal J_0G_{\rm sw}/2$ の単位面積流は

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

を与える。$\mathcal O_k$ では SWAP 後に

```math
b=e_k,
\qquad
t=-W\chi
```

となる。信号へC.3節の逆局所回路 $W^\dagger$ を作用させると、

```math
b
=
W^\dagger e_k
=
|u_k\rangle
```

となる。次の時計窓は相互作用を置かない保持窓とし、比較ポインター、信号、$Q_M$ を読める状態に保つ。$\mathcal O_\varnothing$ では信号は一般に基底ベクトルではなく、結果は無反応である。

## D.9 全入力に対する逆計算

保持窓後に次を実行する。

1. 信号へ局所回路 $W$ を作用させる。
2. $-\pi\mathcal J_0G_{\rm sw}/2$ の流れで逆 SWAP する。
3. $G_j^{\rm route}$ を $j=L-1,\ldots,1$ の順に逆符号で作用させる。
4. $-G_M^{(0)}$ を作用させる。
5. $-G_{\rm amp}$ を作用させる。
6. $G_j^{\rm cum}$ を逆番号順・逆符号で作用させ、最後に $-G_0^{\rm cum}$ を作用させる。
7. $-G_{\rm read}$ を作用させる。
8. 信号へ $W^\dagger$ と $U_{\rm prep}^\dagger$ の局所回路を作用させる。

逆経路では読出しレジスターを消す前に、前向きと同じ $h_j$ と $\ell_j$ を再計算する。順序を入れ替えると逆写像にならない。

各操作は前向き流れの厳密な逆なので、安全セクターだけでなく $\mathcal O_\varnothing$ でも

```math
b=t=e_1,
```

```math
Q_k=P_k=Q_U=P_U=Q_M=P_M=0
```

へ戻る。滑らかな有限幅モデルでは、結果形成を無反応込みの粗視化で定義しながら、内部 Hamiltonian 写像そのものは全入力で厳密に可逆である。

## D.10 選択器ドリフトと時計運動量

最後に

```math
G_{\rm drift}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

を作用させる。Hamilton 方程式から

```math
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi},
\qquad
J_{\rm sel}
\longmapsto
J_{\rm sel}
```

となる。

各単独窓では $H=P_\tau+g_r(\tau)G_r$ である。$G_r$ は自分自身が生成する流れに沿って保存されるので、

```math
\Delta P_\tau
=
-\int
g_r'(\tau)G_r
\,d\tau
=
-G_r
\left[
g_r
\right]_{\rm in}^{\rm out}
=
0
```

である。窓は互いに重ならず、各窓端で $g_r=0$ なので、全周期後にも $P_\tau=E$ へ戻る。

## D.11 Poincaré 写像と長期分布

断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内の不変集合を

```math
\mathcal T_{\chi,W}
=
\left\{
b=t=e_1,
Q_k=P_k=Q_U=P_U=Q_M=P_M=0,
J_{\rm sel}=J_*,
P_\tau=E
\right\}
```

とする。自由なのは $\vartheta$ だけである。C.3節からC.10節までの写像を合成すると、

```math
\mathcal R_{\chi,W}
\left(
\vartheta
\right)
=
\vartheta+2\pi\alpha
\pmod{2\pi}
```

であり、他の全変数は定義値へ戻る。従って $\mathcal T_{\chi,W}$ は不変であり、Haar 測度の下で一意エルゴード的である。

理想累積区間の分布を

```math
p^{\rm id}
=
\left(
|\langle u_1|\chi\rangle|^2,
\ldots,
|\langle u_L|\chi\rangle|^2,
0
\right)
```

とする。実際の結果 $k$ は安全セクター $\mathcal O_k$、実際の無反応は $\mathcal O_\varnothing$ で定める。理想結果から失われた質量と無反応質量が一致するので、

```math
D_{\rm TV}
\left(
p^{\rm cyc},p^{\rm id}
\right)
=
p_{\varnothing}^{\rm cyc}
```

である。C.6節の上界により、有限 $\Lambda$ と有限切断幅で任意精度へ近づけられる。

## D.12 有限誤差に対する安全余裕

増幅前の累積差誤差を $\Delta_{\rm in}$、増幅後のポインター誤差を $\Delta_{\rm out}$ とする。入力換算された有効半幅は

```math
w_{\rm eff}
=
Xe^{-\Lambda}
+
\Delta_{\rm in}
+
e^{-\Lambda}\Delta_{\rm out}
```

である。従って

```math
\varepsilon_{\rm cmp}
\leq
\min
\left\{
1,
2(L-1)
\frac{w_{\rm eff}}{I_{\rm ph}}
\right\}
```

となる。増幅前の入力誤差は双曲型増幅で減らない。増幅後の固定出力誤差だけが入力換算で $e^{-\Lambda}$ 倍になる。

装置誤差が他にない場合、比較誤差を $\epsilon$ 以下にする十分条件は概ね

```math
\Lambda
\geq
\log
\frac{2(L-1)X}{\epsilon I_{\rm ph}}
```

である。精度を上げるほど必要な増幅率とポインター座標範囲が増える。有限温度での雑音床と長時間保持は本付録では評価しない。

## D.13 ゲート数と直列深さ

密な $W$ に対する資源上界は次である。

| 対象 | 隣接2モード混合回数 |
|---|---:|
| $W$ 1回 | $L(L-1)/2$ 以下 |
| 周期内の $W$、$W^\dagger$ 4回 | $2L(L-1)$ 以下 |
| 固定純粋準備 $U_{\rm prep}$ | $L-1$ 以下 |
| 準備と逆準備 | $2(L-1)$ 以下 |

比較剪断、テンプレート経路、逆実行はそれぞれ $O(L)$ 回である。信号モード数と物理交換辺数は増えず、1次元鎖の $L-1$ 辺を再利用する。

逐次 Givens 消去では基底回路の直列深さは $O(L^2)$ である。互いに素な辺を同じ時計層へ並列化する Clements 型配置では、基底回路の深さを $O(L)$ にできる [39]。ただし1個の時計自由度から空間的に離れた各辺へ窓信号を局所伝播させる配線自由度と遅延は、この数え上げに含めない。

## D.14 通常の位置ばねだけに限定した場合

正の位置ばね1本から得る有効2モード生成子は、対角離調を補正すれば交換方向へ近づけられる。しかし局所回転包絡は厳密には

```math
i\mathcal J_0\dot b
=
h(t)b
+
h(t)e^{2i\omega_0t}\overline b
```

を満たし、第2項が反回転項として残る。従って通常の位置ばねだけによる時間依存基底回路は、弱結合・非共鳴の近似である。

固定有限個のゲートでは、各ゲート誤差を $\delta_r$ とすれば

```math
\varepsilon_W^{\rm spr}
\leq
\sum_r\delta_r
```

と評価できる。しかし現行Q3-1定理は時間非依存 $h_L$ に限定され、順方向と逆方向の反回転誤差が無限反復で相殺されることも証明していない。古典振動子による一般複素状態の厳密表示に位置・運動量の双方の結合または符号調整が必要になることは、既存研究とも整合する [35--37]。

従って本付録では $QQ+PP$ 型の局所交換を測定装置の現行構成とする。M37の位置ばね網との同一ハードウェア化はQ1-1からQ1-4の達成条件ではなく、M0、M35の一般化課題またはQ3-5へ接続する一般統合課題である。

## D.15 永久記録の限界

本周期の $Q_M$ と比較ポインターは内部記録であり、保持窓後に逆計算される。保持窓で結果を別の外部記録へコピーすれば、その外部自由度は結果情報を保持する。Hamiltonian 流の1対1性により、その外部記録まで結果に依存しない同一点へ戻すことはできない。

永久記録を伴う反復装置では、外部自由度を拡大するか、記録を循環履歴レジスターへ移すか、弱開放系として情報とエネルギーを外へ運ぶ必要がある。$L=2$ では付録BのM38が外部記録セルとreset セル流を構成する。本付録の一般有限 $L$ のM35は、その外部過程を含まない。

## D.16 未導出事項

本付録の明示周期からは、次は導かれない。

1. 可変準備または可変基底を含む単一のエルゴード周期。
2. 高階数相関行列を1本の軌道から生成する源力学。
3. 混合性と二項分布型有限標本揺らぎ。
4. 一般有限 $L$ の複数段逐次測定、外部記録、弱開放 reset 、長距離時計配線。
5. 永久外部記録を含む有限閉鎖全系の同一点への完全帰還。
6. 無反応なしで連結入力領域全体を厳密な離散基底状態だけへ写す滑らかな有限時間流。
7. 位相担体結果と粒子局所検出の同一性。
8. 連続スペクトル極限。
9. M37の位置ばね網、M35またはM38の測定回路を含むM0の完全統合。
