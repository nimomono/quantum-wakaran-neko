@number: A4
@chapter: 付録
@title: M41初期共通原因周期の正準構成と誤差上界
@status: 本文第7章のR107からR111を支える。設定前基準測度、階数2作用読出し、枝条件付き2担体転送、可変作用測定、外部記録、逆計算、積Haar長期頻度、singlet固定作用特殊化を明示する。空間輸送、準備後の設定変更、一般Tsirelson原理は扱わない。

## D.1 正準変数と開始面

中央4モード担体を $c\in\mathbb C^4$、2つの局所2モード担体を $d^A,d^B\in\mathbb C^2$ とする。各複素モードは

```math
z_j
=
\frac{Q_j+iP_j}
{\sqrt{2\mathcal J_0}}
```

で実正準対から作る。中央担体の作用は $\mathcal J_0c^\dagger c=\mathcal J_0$ に固定する。

源選択器には次を置く。

1. 階数2ブロック作用レジスター $(Q_+^{\rm s},P_+^{\rm s})$、$(Q_-^{\rm s},P_-^{\rm s})$。
2. 源閾値レジスター $(Q_U^{\rm s},P_U^{\rm s})$。
3. 源枝レジスター $(Q_M^{\rm s},P_M^{\rm s})$。
4. 源選択器 $(\vartheta_{\rm s},J_{\rm s})$。

A、B局所測定器は、それぞれM35の $L=2$ コアを持つ。すなわち2モードテンプレート、2作用レジスター、1閾値レジスター、1内部記録、1選択器を持つ。A、Bの外部結果記録セルを $(Q_A^R,P_A^R)$、$(Q_B^R,P_B^R)$ とする。

設定生成には2つの設定選択器 $(\xi_A,J_{\xi_A})$、$(\xi_B,J_{\xi_B})$ と2つの設定レジスターを使う。全操作を1つの作用・角時計 $(\tau,J_\tau)$ の互いに重ならない窓へ配置する。転送制御に必要な滑らかな旗は、源比較ポインターと枝レジスターから作り、新しい確率変数として置かない。

開始面では、信号とテンプレートを指定準備値へ、全読出しレジスターと外部空記録の共役運動量を0へ置く。自由角だけに積Haar測度を置く。この開始面は有限次元であり、目的の共同結果分布を直接含まない。

## D.2 設定選択器と前向き準備写像

有限設定集合 $\mathcal X,\mathcal Y$ と所定の設定頻度 $\pi_x,\pi_y$ を固定する。円周を長さ $2\pi\pi_x$、$2\pi\pi_y$ の区間へ分け、M35と同じ平坦部を持つ滑らかな比較器で安全設定を作る。全境界遷移領域を設定無反応へ送る。

安全設定 $x,y$ が生成された後、固定singlet型源を設定と独立に準備する。A設定レジスター $x$ は中央担体の階数2分解に使う固定回路 $W_x\otimes I_2$ を選び、B設定レジスター $y$ は2担体転送後のB局所測定回路 $W_y$ だけを選ぶ。従って $W_y$ を源準備へ先回りして作用させない。

設定前の積測度を $\mu_0$、安全設定対に対応する全準備写像を $T_{xy}$ とする。$T_{xy}$ は有限個のHamiltonian流の合成なのでシンプレクティックであり、

```math
\mu_{\rm meas}^{xy}
=
\left(T_{xy}\right)_\#
\mu_0
\left(
\cdot
\mid x,y
\right)
```

は通常の前向き押出しである。終端支持、未来角、実験後の条件付き除外は使わない。

設定比較の入力換算半幅の総和を $w_{\rm set}$、切断接続領域の積Haar質量を $\varepsilon_{{\rm cut},{\rm set}}$ とすれば、

```math
\delta_{\rm set}
\leq
C_{\rm set}w_{\rm set}
+
\varepsilon_{{\rm cut},{\rm set}}
```

と書ける。$C_{\rm set}$ は固定有限設定分割の境界本数から決まる有限定数である。

## D.3 階数2作用読出し

$c^x=(W_x\otimes I_2)c$ を2つのBブロック $c_+^x,c_-^x$ に分け、

```math
I_A^x
=
\mathcal J_0
\left(c_A^x\right)^\dagger c_A^x
```

とする。読出し生成子を

```math
G_{\rm s}^{\rm read}
=
P_+^{\rm s}I_+^x
+
P_-^{\rm s}I_-^x
+
P_U^{\rm s}
\mathcal J_0
f(\vartheta_{\rm s})
```

とする。全レジスター運動量を0から始めると、単位面積流の後に

```math
Q_A^{\rm s}=I_A^x,
\qquad
Q_U^{\rm s}
=
\mathcal J_0f(\vartheta_{\rm s})
```

となる。読出し反作用は、対応するレジスター運動量が0なので入口信号に現れない。

累積差

```math
D_{\rm s}
=
I_+^x
-
\mathcal J_0
f(\vartheta_{\rm s})
```

を局所剪断で作り、双曲型増幅後の符号を平坦な滑らか比較関数へ入れる。安全正枝では旗 $(\ell_+,\ell_-)=(1,0)$、安全負枝では $(0,1)$ となる。遷移領域ではどちらの旗も離散結果として読まず、源無反応に分類する。

角切断を除く理想区間長は $I_A^x/\mathcal J_0$ なので、源選択器のHaar頻度は枝作用比に一致する。比較半幅 $w_{\rm s}$ に対する無反応質量は

```math
\delta_{\rm s}
\leq
2\frac{w_{\rm s}}{\mathcal J_0}
+
\varepsilon_{{\rm cut},{\rm s}}
```

である。

## D.4 条件付き正準SWAP

2つの複素2モードブロック $u,v$ の交換生成子を

```math
G_{\rm sw}(u,v)
=
i
\left(
u^\dagger v
-
v^\dagger u
\right)
```

とする。Hamiltonian $\pi\mathcal J_0G_{\rm sw}/2$ の単位面積流は

```math
u\longmapsto v,
\qquad
v\longmapsto-u
```

を与える。

B担体を零テンプレートへ準備し、互いに重ならない2窓で

```math
G_{\rm tr,B}
=
\ell_+
G_{\rm sw}
\left(
c_+^x,d^B
\right)
+
\ell_-
G_{\rm sw}
\left(
c_-^x,d^B
\right)
```

を作用させる。安全枝では旗が厳密に0または1なので、選択済みブロックだけがB担体へ移る。選択済み中央ブロックにはBの旧零テンプレートが、未選択ブロックには元の振幅が残る。

A担体は固定作用 $I_{\rm loc}$ の標準方向へ準備する。安全枝 $A$ と設定 $x$ に対して標準方向を $|A_x\rangle$ へ送る局所 $SU(2)$ 回路を、同じ旗で制御して作用させる。この回路はA担体の作用を保存する。旗の共役レジスター運動量を0へ準備し、各制御生成子が自身の窓で保存されるため、安全域では旗レジスターへの読出し反作用はない。

前向き転送写像を $T_A^{\rm tr}$ とすると、外部記録後の逆転送は同じ旗を保持したまま

```math
\left(
T_A^{\rm tr}
\right)^{-1}
```

を逆順で作用させる。中央4モード状態、A、Bテンプレート、枝レジスターは準備値へ戻る。選択済み情報を複製も消去もしていない。

## D.5 非選択B相関行列

源選択器の理想枝頻度は $p_A^x=\|c_A^x\|^2$ であり、安全枝の規格化B方向は

```math
|\beta_A^x\rangle
=
\frac{c_A^x}{\sqrt{p_A^x}}
```

である。枝を読まないB相関行列は

```math
\begin{aligned}
C_B^{\rm ns}(x)
&=
\sum_A
p_A^x
|\beta_A^x\rangle
\langle\beta_A^x|\\
&=
\sum_A
c_A^x
\left(c_A^x\right)^\dagger.
\end{aligned}
```

$W_x$ の第 $A$ 行を行ベクトル $w_A^x$ とすると、

```math
c_A^x
=
\left(
 w_A^x
\otimes I_2
\right)c.
```

完全性 $\sum_A(w_A^x)^\dagger w_A^x=I_2$ を使えば、

```math
C_B^{\rm ns}(x)
=
\operatorname{Tr}_A
\left(
cc^\dagger
\right)
```

を得る。従ってA設定による分解は変わり得るが、非選択B相関行列は変わらない。

singlet型では

```math
C_B^{\rm ns}
=
\frac12I_2,
\qquad
p_+^x=p_-^x=\frac12
```

である。各条件付きB方向はA方向と反対で、全作用は常に $\mathcal J_0/2$ である。

## D.6 A局所確認測定

A担体は

```math
d^A
=
\sqrt{
\frac{I_{\rm loc}}{\mathcal J_0}
}
|A_x\rangle
```

である。A基底回路を作用させると、作用は一方の出力モードへ全て集まる。

```math
K_{A'}^{Ax}
=
I_{\rm loc}
\delta_{A'A}
```

従ってM35の $L=2$ 作用区間測定は、安全域で $A$ を確定的に返す。比較境界と角切断接続域だけを無反応とする。

この測定は源枝レジスターを外部記録へ直接コピーしない。A担体のモード作用をA局所読出しレジスターへ写し、A局所テンプレートとSWAPして測定後方向を作り、A局所結果ポインターを外部記録へ剪断する。源変数とA局所変数は別の正準対である。

## D.7 B可変作用測定

B基底回路後のモード作用を

```math
K_B
=
\mathcal J_0
\left|
\left(
W_yd^B
\right)_B
\right|^2,
\qquad
K_++K_-=I_B
```

とする。可変全作用を同じ局所測定器内で読む生成子を

```math
G_B^{\rm read}
=
P_+^BK_+
+
P_-^BK_-
+
P_U^BI_B
f(\vartheta_B)
```

とする。入口で $P_+^B=P_-^B=P_U^B=0$ なら、B信号と選択器への読出し反作用は0である。累積差

```math
D_B
=
K_+
-
I_Bf(\vartheta_B)
```

を増幅して滑らかに比較する。

$I_B>0$ の理想零幅では、

```math
P
\left(
B
\mid
A,x,y
\right)
=
\frac{K_B}{I_B}
```

である。条件付き無反応上界は $2w_B/I_B+\varepsilon_{{\rm cut},B}$ となる。源枝確率 $I_B/\mathcal J_0$ と掛け、2枝を和すると、

```math
\sum_A
\frac{I_A^x}{\mathcal J_0}
\frac{2w_B}{I_A^x}
\leq
4\frac{w_B}{\mathcal J_0}
```

を得る。零作用枝は源確率0であり、正式な無反応にしても理想共同分布を変えない。

測定後B方向を安全結果 $B$ へ厳密にそろえるには、テンプレート作用を実際の $I_B$ へ合わせる。$I_{\rm sup}>\mathcal J_0$ の固定正作用供給対を用意し、読出した $I_B$ に応じた2モード交換でテンプレート作用 $I_B$ と残余作用 $I_{\rm sup}-I_B$ へ分ける。上端は $I_{\rm sup}-I_B>0$ なので特異にならず、$I_B$ が作用切断 $\eta_{\rm act}$ 以上の領域では交換角を滑らかに選べる。$I_B<\eta_{\rm act}$ を無反応へ送ると、その無条件質量は

```math
\sum_{A:
I_A^x<\eta_{\rm act}}
\frac{I_A^x}{\mathcal J_0}
\leq
2\frac{\eta_{\rm act}}{\mathcal J_0}
=:
\varepsilon_{\rm act}
```

である。従って固定された正の枝作用下限を仮定せず、無条件誤差を任意に小さくできる。

singlet型では $I_B=\mathcal J_0/2$ が既知なので、最初から同じ作用のテンプレートを準備できる。作用切断、可変角生成、全作用側チャネルは不要である。

## D.8 局所Hamiltonianの可換性

A局所正準変数の集合を $\Gamma_A$、B側を $\Gamma_B$ とし、

```math
\Gamma_A\cap\Gamma_B
=
\varnothing
```

とする。中央転送窓が終了した後は、全ての中央結合係数を0にする。局所測定生成子は

```math
H_A
=
H_A
\left(
\Gamma_A;x
\right),
\qquad
H_B
=
H_B
\left(
\Gamma_B;y
\right)
```

なので、

```math
\left\{
H_A,H_B
\right\}
=0.
```

従って局所流は順序を交換できる。

```math
\Phi_{\rm meas}
=
\Phi_A\Phi_B
=
\Phi_B\Phi_A
```

局所結果は同じ側の担体、設定、選択器だけで決まる。中央作業領域は測定中に両側へ結合しない。

この可換性は装置内の代数的局所性である。2装置間の距離、信号伝播円錐、空間的に隔たった設定選択は導入していない。

## D.9 外部記録と逆実行順序

A、B局所結果ポインターから滑らかな結果コード $\Pi_A,\Pi_B$ を作り、

```math
G_{\rm rec}
=
P_A^R\Pi_A
+
P_B^R\Pi_B
```

を作用させる。$P_A^R=P_B^R=0$ の理想入口では、内部変数への反作用は0で、外部記録座標だけが移動する。

設定生成を $M_{\rm set}$、M39の固定singlet型準備を $U_{\rm src}$、A基底回路を $U_x$、源選択を $M_{\rm s}$、2担体転送を $T_{\rm tr}$、局所測定を $M_A,M_B$ とする。前向き観測写像は

```math
\Phi_{\rm fwd}
=
C_R
M_BM_A
T_{\rm tr}
M_{\rm s}
U_x
U_{\rm src}
M_{\rm set}
```

である。中央転送後は $M_A$ と $M_B$ が可換だが、転送より前へ動かしてはならない。

記録後の能動部逆計算は

```math
\Phi_{\rm inv}
=
M_{\rm set}^{-1}
U_{\rm src}^{-1}
U_x^{-1}
M_{\rm s}^{-1}
T_{\rm tr}^{-1}
M_A^{-1}
M_B^{-1}
```

である。従って能動部への制限は

```math
\Phi_{\rm inv}
\Phi_{\rm fwd}
\big|_{\rm active}
=
I
```

となり、外部記録だけが残る。無反応領域でも各写像は滑らかで可逆なので同じ式が成立する。

有限残差はM38と同じ正準交換で外部空セルへ移す。交換前の能動偏差を $a$、流入空セルを $e$ とすると、

```math
\begin{pmatrix}
a^+\\
e^+
\end{pmatrix}
=
\begin{pmatrix}
\cos\phi&\sin\phi\\
-\sin\phi&\cos\phi
\end{pmatrix}
\begin{pmatrix}
a^-\\
e^-
\end{pmatrix}.
```

完全交換では旧偏差が使用済みセルへ移る。情報消去または非正準収縮ではない。

## D.10 積Haar頻度とBorn型共同分布

源選択器角とB局所選択器角は開始面で独立である。固定設定 $x,y$ と理想安全領域で、

```math
\begin{aligned}
P(A,B\mid x,y)
&=
P(A\mid x)
P(B\mid A,x,y)\\
&=
\frac{I_A^x}{\mathcal J_0}
\frac{K_B^{Axy}}{I_A^x}\\
&=
\frac{K_B^{Axy}}{\mathcal J_0}.
\end{aligned}
```

一方、

```math
K_B^{Axy}
=
\mathcal J_0
\left|
\langle B_y|c_A^x\rangle
\right|^2
=
\mathcal J_0
\left|
\langle A_x,B_y|c\rangle
\right|^2.
```

従って

```math
P(A,B\mid x,y)
=
\left|
\langle A_x,B_y|c\rangle
\right|^2.
```

$I_A^x=0$ の枝は左辺、右辺とも0である。この分母消去により、稀な枝の条件付き誤差が無条件共同分布で固定作用下限を要求しない。

全角ベクトルのPoincaré写像を

```math
\boldsymbol\vartheta
\longmapsto
\boldsymbol\vartheta
+
2\pi\boldsymbol\alpha
\pmod{2\pi}
```

とする。$1$ と $\boldsymbol\alpha$ の全成分が有理数体上で1次独立なら、有限次元トーラス上で一意エルゴード的である。境界がHaar零である理想結果集合と、滑らかな有限幅結果集合の長期頻度は対応する積Haar体積に一致する。

## D.11 singlet特殊化

singlet係数行列を

```math
C_{\rm s}
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

とする。平面内A基底で左から回転すると、各行ノルムは $1/\sqrt2$ である。従って

```math
I_A^x
=
\frac{\mathcal J_0}{2}.
```

条件付きB方向は、全体位相を除いてA結果と反対の固有方向である。

```math
|\beta_A^x\rangle
\simeq
|-A_x\rangle
```

従って

```math
\left|
\langle B_y|\beta_A^x\rangle
\right|^2
=
\frac12
\left[
1
-
AB\cos(x-y)
\right].
```

源枝確率 $1/2$ を掛ければ本文第7.10節の共同分布を得る。

一側周辺は各結果について $1/2$ である。完全な古典状態分布は、条件付きB方向と枝ラベルを含むため $x$ に依存するが、2次の非選択B相関行列は $I_2/2$ で一定である。測定設定独立性の破れと非信号性を同じ性質として扱わない。

## D.12 誤差合成

理想共同分布を、A、B、設定、源の全無反応成分を0とした拡張結果空間へ埋め込む。各前向きモジュールの条件付き全変動誤差を順に合成すると、

```math
\begin{aligned}
\epsilon_{\rm fwd}
\leq{}&
\delta_{\rm set}
+
\delta_{\rm s}
+
\delta_A^{\rm loc}
+
\delta_B^{\rm loc}\\
&+
\varepsilon_{\rm tr}
+
\varepsilon_{\rm act}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}^{\rm fwd}
\end{aligned}
```

を得る。有限個のMarkov核の合成に対する全変動距離の三角不等式を使っており、異なる単位の正準状態誤差は境界移動量とHaar質量へ換算してから加える。

局所B比較だけを取り出すと、

```math
\delta_B^{\rm loc}
\leq
4\frac{w_B+\Delta_B}{\mathcal J_0}
+
\varepsilon_{{\rm cut},B},
```

ここで $\Delta_B$ は読出し、転送、時計誤差を入力作用幅へ換算した量である。singlet型では枝作用が固定なので、枝別にも

```math
\delta_{B\mid A}^{\rm loc}
\leq
4\frac{w_B+\Delta_B}{\mathcal J_0}
+
\varepsilon_{{\rm cut},B}
```

と一様に書ける。

帰還誤差は

```math
\varepsilon_{\rm ret}
\leq
\varepsilon_{\rm inv,A}
+
\varepsilon_{\rm inv,B}
+
\varepsilon_{\rm inv,tr}
+
\varepsilon_{\rm inv,s}
+
\varepsilon_{\rm inv,x}
+
\varepsilon_{\rm inv,src}
+
\varepsilon_{\rm inv,set}
+
\varepsilon_{\rm rst}
+
\varepsilon_{\rm clk}^{\rm ret}
```

とし、次周期の準備誤差へ入れる。観測後の逆計算誤差を、既に外部記録された同じ観測の共同分布へ加えない。

## D.13 有限資源と主張境界

M41の能動部は、次の有限モジュールの合成である。

| モジュール | 固定有限資源 |
|---|---|
| M39中央源 | 4信号正準対と有限時計窓 |
| 設定生成 | 2選択器と2設定レジスター |
| 階数2源選択 | 2作用、1閾値、1枝記録、1選択器 |
| 2担体転送 | A、B各2信号対と有限条件付きSWAP窓 |
| 局所測定 | A、B各1個のM35型2モードコア |
| 外部記録 | 1周期当たりA、B各1セル |
| reset | 交換対象ごとの外部空セル |
| 自律化 | 共有する1作用・角時計 |

同じ信号、時計、読出しレジスターを複数モジュール間で共有できるため、表の行を単純加算した数を最小資源数とはしない。重要なのは、固定設定集合と固定有限回について全モジュール数と窓数が有限であることである。

固定 $K$ 周期では、永久記録と使用済みreset状態を含めても有限閉鎖Hamiltonian系へ埋め込める。必要な外部セル数は $O(K)$ で増える。無期限運転には空セル流入と使用済みセル流出が必要である。

本付録は次を証明しない。

1. 2担体準備後の設定変更に対する同じ統計。
2. 空間輸送、有限伝播速度、局所時計同期。
3. 一般状態におけるB作用側チャネルの不存在。
4. 無反応なしの滑らかな厳密2値測定。
5. 全非零枝に一様な有限資源条件付き精度。
6. 独立同分布型の有限標本揺らぎ。
7. 一般測定族に対するTsirelson原理。
8. 永久記録を含む全閉鎖系の同一点帰還。
