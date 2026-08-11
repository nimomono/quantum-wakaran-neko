@number: 7
@chapter: 本文
@title: 初期共通原因型2担体Bell測定周期
@status: M41について、設定前の積Haar基準測度、設定生成、設定と独立なM39の4モード状態準備、A中央枝選択、A担体の局所状態準備、選択済みBブロックの正準SWAP、A局所確認測定とB局所測定、永久外部記録、内部逆計算、弱開放resetを1本の前向き周期へまとめる。singlet型固定プログラムでは余弦共同確率、非信号性、CHSH値 $2\sqrt2$、平面内2出力族のTsirelson上界を制御された任意精度で得る。Q2-2は操作的接続の意味で条件付き達成であり、4モード状態全体の設定非依存な2部分系分配、準備後の設定変更、空間的分離、一般Tsirelson原理は含まない。

## 7.1 M41の採用範囲と因果順序

本章では、初期共通原因型のBell装置M41を採用する。設定依存分布を測定開始面へ直接仮定せず、設定がまだ離散記録になっていない開始面の基準測度と、有限Hamiltonian準備写像を先に置く。1周期の因果順序は次である。

1. 設定選択器、源選択器、局所選択器、時計を開始面へ準備する。
2. 設定レジスターに $x,y$ を生成する。
3. M39の中央4モード担体に目的状態を準備する。
4. A設定 $x$ に対応する階数2ブロック作用を読み、A中央枝選択で源枝 $A$ を選ぶ。
5. 選択済み枝から2つの物理的2モード担体 $d^A,d^B$ を準備する。
6. 中央源と両担体の結合を停止する。
7. A側ではA局所確認測定、B側ではB局所測定を行い、結果を別々の外部記録へ写す。両Hamiltonianは可換である。
8. 観測後に測定器、転送器、源選択器、A基底回路、源準備、設定生成器を逆計算する。
9. 有限残差を外部resetセルへ交換し、選択器角を平行移動する。

本章では、段階4を「A中央枝選択」、段階7のA側操作を「A局所確認測定」と呼んで区別する。A結果 $A$ はA中央枝選択で先に形成される。A局所確認測定は、準備済みの $|A_x\rangle$ を別のAポインターで測り、同じ $A$ を確定的に外部記録する操作であって、新しい確率的A結果を作らない。

この順序では、A局所確認測定またはA側の局所記録が形成された後にB側へ条件を送らない。B担体は中央準備部でA担体と同時に作られ、測定中のA--B直接結合はない。一方、設定 $x$ はA中央枝選択より前に中央準備へ入り、準備後の隠れた状態は $x$ に依存する。Bellの測定設定独立性を満たさない機構はここにある。

「初期共通原因型」は、設定角、源選択器角、局所選択器角が測定前の1つのHamiltonian 周期に属することを指す。設定、singlet状態、枝ラベルを設定前開始面で同時に設定依存標本化することを意味しない。開始面の自由角は積Haar測度を持ち、設定を生成し、設定と独立にsingletを準備した後、A設定を使う前向きHamiltonian 写像が枝ラベルと2担体状態を作る。

過去に検討したAからBへの逐次依存型と二側境界型は、M41と異なる因果仮定を使うため現行本文の根拠にしない。比較、不採用理由、再検討条件は論文外の研究メモで管理する。

## 7.2 M39からの入力契約

M39の4モード固定作用担体を

```math
c
=
\begin{pmatrix}
c_{00}\\
c_{01}\\
c_{10}\\
c_{11}
\end{pmatrix},
\qquad
c^\dagger c=1
```

と書く。論理添字だけでは2つの物理担体にならない。本章はM39の状態全体を2担体へ複製または転送しない。A基底で1つの階数2ブロックを選んだ後、A担体を選択結果の局所状態へ準備し、選択済みBブロックだけをB担体へ可逆に移す。

平面内設定 $x$ のA基底を

```math
|+_x\rangle
=
\cos\frac{x}{2}|0\rangle
+
\sin\frac{x}{2}|1\rangle,
```

```math
|-_x\rangle
=
-\sin\frac{x}{2}|0\rangle
+
\cos\frac{x}{2}|1\rangle
```

とする。$W_x|A_x\rangle=e_A$ を満たす実直交ユニタリを用い、

```math
c^x
=
\left(W_x\otimes I_2\right)c
=
\begin{pmatrix}
c_+^x\\
c_-^x
\end{pmatrix},
\qquad
c_A^x\in\mathbb C^2
```

と階数2ブロックへ分ける。各ブロック作用と枝重みは

```math
I_A^x
=
\mathcal J_0
\left\|
c_A^x
\right\|^2,
\qquad
p_A^x
=
\frac{I_A^x}{\mathcal J_0},
\qquad
\sum_Ap_A^x=1
```

である。

Q2-2の基本入力にはsinglet型状態

```math
c_{\rm s}
=
|\Psi^-\rangle
=
\frac{
|01\rangle-|10\rangle
}{\sqrt2}
```

を使う。第6章のM39で得た

```math
|\Phi^+\rangle
=
\frac{
|00\rangle+|11\rangle
}{\sqrt2}
```

へ局所操作 $Z_A\otimes X_B$ を作用させれば、$c_{\rm s}$ を同じ4モードHamiltonian層で準備できる。singlet型では任意の $x$ について

```math
I_+^x
=
I_-^x
=
\frac{\mathcal J_0}{2}
```

である。この固定作用性が、後段の局所測定器と古典的作用側チャネルを単純化する。

## 7.3 設定前基準測度と設定生成

開始面の自由角を、設定選択器 $\xi_A,\xi_B$、源選択器 $\vartheta_{\rm s}$、局所選択器 $\vartheta_A,\vartheta_B$ とする。全てを独立な円角として

```math
d\mu_0
=
\frac{d\xi_A}{2\pi}
\frac{d\xi_B}{2\pi}
\frac{d\vartheta_{\rm s}}{2\pi}
\frac{d\vartheta_A}{2\pi}
\frac{d\vartheta_B}{2\pi}
\otimes
\delta_{z_*}
```

を置く。$\delta_{z_*}$ は信号、テンプレート、読出しレジスター、時計作用、外部空セルの準備値を表す。$\mu_0$ には、まだ測定開始面の2担体状態も枝ラベルも存在しない。

有限設定集合を使う場合、$\xi_A,\xi_B$ の円周を所定の長さへ分割し、滑らかな比較器で設定レジスター $x,y$ を作る。CHSH検査では各側2設定を等しい半円へ割り当てる。比較境界の遷移領域は正式な設定無反応として無条件記録に残し、安全設定対ごとの条件付き共同分布と混同しない。

固定した安全設定対 $x,y$ に対する前向き準備写像を $T_{xy}$ とする。測定開始面の条件付き測度は

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

である。$T_{xy}$ は、M39準備、階数2作用読出し、A担体準備、Bブロック正準SWAPを滑らかな時計窓で合成した有限Hamiltonian写像である。従って設定依存性は、初期分布へ求める答えを書いたものではなく、設定生成後の前向き準備力学から生じる。

1つの自律周期では、$1$ と全ての角増分が有理数体上で1次独立になるよう選ぶ。Poincaré写像は角トーラスの平行移動になり、長期頻度は積Haar測度に一致する。ただし結果列の独立同分布性は従わない。

## 7.4 階数2ブロック作用選択

源選択器では、2つのブロック作用 $I_+^x,I_-^x$ と閾値

```math
u_{\rm s}
=
\mathcal J_0
f(\vartheta_{\rm s})
```

を正準レジスターへ読む。$f$ は角の切断接続領域を除いて $\vartheta_{\rm s}/(2\pi)$ と一致する。理想零幅では

```math
A=+1
\quad\Longleftrightarrow\quad
0\leq u_{\rm s}<I_+^x,
```

```math
A=-1
\quad\Longleftrightarrow\quad
I_+^x\leq u_{\rm s}<\mathcal J_0
```

とする。従って

```math
P_{\rm id}
\left(
A\mid x
\right)
=
\frac{I_A^x}{\mathcal J_0}
=
p_A^x
```

である。

入力換算比較半幅を $w_{\rm s}$、角切断領域のHaar質量を $\varepsilon_{{\rm cut},{\rm s}}$ とすると、結果集合を $\{+1,-1,\varnothing\}$ とした滑らかな選択器の無反応率は

```math
\delta_{\rm s}
\leq
2\frac{w_{\rm s}}{\mathcal J_0}
+
\varepsilon_{{\rm cut},{\rm s}}
```

である。安全結果では枝ラベルは排他的であり、遷移領域をどちらかの枝へ割り当てない。

<!-- theorem-start:proposition -->
**命題（R107：滑らかな階数2ブロック作用選択）**

任意の規格化4モード入力 $c$、固定設定 $x$、任意の $\epsilon>0$ に対し、有限個の正準レジスターと滑らかな時計窓からなる階数2作用選択器を構成できる。安全結果 $A$ の長期頻度は $I_A^x/\mathcal J_0$ に一致し、無反応を含む実分布と理想枝分布の全変動距離を $\epsilon$ 未満にできる。選択はM39担体のブロック作用を直接読み、外部から枝重みを入力しない。
<!-- theorem-end:proposition -->

## 7.5 枝条件付き2担体準備

安全枝 $A$ の下で、A側とB側の2モード担体を

```math
d^A
=
\sqrt{\frac{I_{\rm loc}}{\mathcal J_0}}
|A_x\rangle,
\qquad
d^B
=
-c_A^x
```

と準備する。$I_{\rm loc}>0$ はA担体の固定作用である。singlet型では

```math
I_{\rm loc}
=
I_B
=
\mathcal J_0
\left(d^B\right)^\dagger d^B
=
\frac{\mathcal J_0}{2}
```

と選べる。

この準備は4モード状態全体のコピーまたは2担体への転送ではない。A担体は選択結果に対応する局所状態として準備し、選択済みBブロックだけをB担体と正準SWAPする。B担体の旧テンプレート、未選択ブロック、枝選択レジスター、A担体の旧テンプレートは中央作業領域に残す。全ての情報を保持するため、観測後に同じ枝制御を使って逆準備できる。

安全枝で $I_A^x>0$ のとき、B担体の規格化方向は

```math
|\beta_A^x\rangle
=
\frac{c_A^x}{\sqrt{p_A^x}}
```

である。A枝を読まない非選択B状態は

```math
C_B^{\rm ns}(x)
=
\sum_A
c_A^x
\left(c_A^x\right)^\dagger
=
\operatorname{Tr}_A
\left(
cc^\dagger
\right)
```

となり、A基底 $x$ に依存しない。Aの異なる枝を結ぶ交差項は非選択B状態に残らない。

ここでB側の枝間コヒーレンスが失われる時点は、後段のA局所確認測定ではなく、中央準備部のA中央枝選択と2担体準備である。A設定を用いた非選択操作を中央準備まで実行し、A結果を読まない場合にも、B側は上式の縮約状態になる。後段のA局所確認測定からBへ作用が伝わるとは解釈しない。

<!-- theorem-start:proposition -->
**命題（R108：枝条件付き2担体準備と非選択B状態）**

R107の安全枝ごとに、選択済みBブロックをB物理担体へ正準SWAPし、A物理担体を対応する基底方向へ準備できる。未選択ブロックと旧テンプレートを保持するため全写像は可逆である。枝を読まないB相関行列は $\operatorname{Tr}_A(cc^\dagger)$ に一致してA設定に依存せず、枝間コヒーレンスの消失は中央準備段で生じる。M39の非因子化状態全体を2物理担体へ移したとは主張しない。
<!-- theorem-end:proposition -->

## 7.6 A局所確認測定とB局所測定

中央結合を停止した後、A担体には設定 $x$、B担体には設定 $y$ のM35型2モード測定器を結合する。両側の正準変数を分け、

```math
H_{\rm meas}
=
H_A
+
H_B,
\qquad
\left\{
H_A,H_B
\right\}
=0
```

とする。$H_A$ はA担体、A選択器、Aポインター、A記録セルだけに、$H_B$ はB側の対応する変数だけに依存する。従って測定中に反対側の設定、結果、ポインターをHamilton方程式へ入れない。

A担体は既に $|A_x\rangle$ 方向なので、安全域のA局所確認測定は同じ $A$ を確定的に記録する。確率的なA結果を作るのは第7.4節のA中央枝選択であり、ここではない。A局所確認測定は中央源の枝ラベルを直接外部記録へコピーする操作ではなく、別のA物理担体と局所ポインターの相互作用である。

B基底回路を $W_y$ とし、B出力モード作用を

```math
K_B^{Axy}
=
\mathcal J_0
\left|
\left(
W_yd^B
\right)_B
\right|^2,
\qquad
\sum_BK_B^{Axy}
=
I_B
```

とする。singlet型では $I_B=\mathcal J_0/2$ が全枝で固定されるため、閾値

```math
u_B
=
\frac{\mathcal J_0}{2}
f(\vartheta_B)
```

を使うM38の固定作用測定器をそのまま再利用できる。安全なB結果の条件付き頻度は

```math
P_{\rm id}
\left(
B\mid A,x,y
\right)
=
\frac{K_B^{Axy}}{I_B}
=
\left|
\langle B_y|\beta_A^x\rangle
\right|^2
```

である。

各側の滑らかな結果ポインターは、別々の理想空外部記録セルへ正準剪断で写す。結果集合は各側とも $\{+1,-1,\varnothing\}$ とし、無反応を除いて共同分布を再規格化しない。

## 7.7 一般状態の可変作用測定

一般のM39入力では $I_B=I_A^x$ が枝ごとに変わる。装置内で $K_B/I_B$ を除算せず、実際の全作用と同じ次数で閾値を作る。

```math
D_B
=
K_+^{Axy}
-
I_B
f(\vartheta_B)
```

の符号を滑らかに比較すれば、理想零幅では区間長が $K_+^{Axy}/I_B$ になる。$I_B=0$ の枝では全比較量が0となるため、正式な無反応へ送る。

条件付き誤差は小さい $I_B$ で増幅されるが、無条件誤差では源枝重みと掛けたときに分母が消える。B比較の入力換算半幅を $w_B$ とすると、2枝を合計した無条件無反応率は

```math
P
\left(
\varnothing_B
\right)
\leq
4\frac{w_B}{\mathcal J_0}
+
\varepsilon_{{\rm cut},B}
+
\varepsilon_{\rm act}
```

で抑えられる。$\varepsilon_{\rm act}$ は零作用近傍のテンプレート準備を正式な無反応へ送る作用切断質量であり、固定された正の枝作用下限を要求せず任意に小さくできる。

<!-- theorem-start:proposition -->
**命題（R109：可変作用2モード担体の局所作用比測定）**

任意の規格化4モード入力について、R107の枝選択とR108の転送に続けて、B担体の実際の全作用 $I_B$ で閾値を同次化する局所測定器を構成できる。安全枝の条件付き頻度は $K_B^{Axy}/I_B$、源枝と合わせた無条件頻度は $K_B^{Axy}/\mathcal J_0$ に一致する。零作用枝と作用切断域を無反応に含めることで、無条件誤差上界は正の枝作用下限を必要としない。全ての非零枝へ一様な条件付き精度を要求する場合だけ作用下限が必要である。
<!-- theorem-end:proposition -->

Q2-2の達成判定は、$\varepsilon_{\rm act}=0$ とできるsinglet型固定作用特殊化を使う。一般状態ではB全作用がA枝と設定の古典的側チャネルになり得るため、作用側チャネルが存在しないとは主張しない。

## 7.8 外部記録、逆計算、全周期

1周期の前向き観測と帰還を次の順に固定する。

1. 設定 $x,y$ を設定レジスターへ生成する。
2. M39で $c_{\rm s}$ を中央4モード担体へ準備する。
3. $W_x\otimes I_2$ を作用させる。
4. 階数2作用選択器で源枝を選ぶ。
5. A担体を枝対応状態へ準備し、選択済みBブロックをB担体へ正準SWAPする。
6. 中央準備結合を停止する。
7. A局所確認測定とB局所測定を実行する。
8. A、B結果と無反応を外部記録へコピーする。
9. B局所測定、A局所確認測定、BブロックSWAP、A担体準備、A中央枝選択、A基底回路、M39準備、設定生成を逆順で戻す。
10. 有限残差を外部resetセルへ交換する。
11. 全選択器角を無理数平行移動する。

外部記録セルの共役運動量が0なら、記録剪断は能動部へ反作用しない。従って記録後に前向き写像の厳密な逆を実行できる。無反応領域でも前向き写像は滑らかな正準写像なので、同じ逆計算が成立する。

能動部と角ベクトルを $(z_*,\boldsymbol\vartheta)$ と書くと、理想Poincaré写像は

```math
\left(
z_*,
\boldsymbol\vartheta
\right)
\longmapsto
\left(
z_*,
\boldsymbol\vartheta
+
2\pi\boldsymbol\alpha
\right)
```

である。永久記録列と使用済みresetセルは帰還断面の $z_*$ に含めない。固定有限回なら必要な記録・resetセルを最初から含む有限閉鎖Hamiltonian系に埋め込める。無期限運転では空セルの流入と使用済みセルの流出を持つ弱開放系として扱う。

<!-- theorem-start:theorem -->
**定理（R110：M41初期共通原因型Bell測定周期）**

固定された有限設定集合、M39のsinglet型準備、任意の $\epsilon>0$ に対し、有限個の正準自由度と滑らかな時計窓からなるM41能動周期、および外部記録・resetセル流路を構成できる。設定前基準測度は積Haar測度であり、測定開始面の設定依存状態は前向きHamiltonian準備写像から生じる。A結果は2担体準備前のA中央枝選択で形成され、2担体準備後のA局所確認測定は同じ結果を確定的に記録する。2担体準備後の局所測定Hamiltonianは可換で、無反応を含む共同記録分布と理想分布の全変動距離、記録誤差、周期末能動部偏差を全て $\epsilon$ 未満にできる。全写像は正準的で1対1であり、結果履歴と旧装置偏差を外部流へ残す。
<!-- theorem-end:theorem -->

## 7.9 Born型共同分布

理想零幅で源枝とB局所測定を合成すると、

```math
\begin{aligned}
P_{\rm id}
\left(
A,B\mid x,y
\right)
&=
\frac{I_A^x}{\mathcal J_0}
\frac{K_B^{Axy}}{I_A^x}\\
&=
\left|
\langle A_x,B_y|c\rangle
\right|^2
\end{aligned}
```

となる。$I_A^x=0$ の項は0と定める。最初の因子は源選択器の作用区間、2番目はB局所選択器の作用区間から生じる。目的の共同重みを初期測度へ直接置いていない。

A局所確認測定は安全枝でA中央枝選択の結果 $A$ を確定的に確認するため、外部に記録されるA結果を使っても同じ共同分布になる。A、B、源の選択器角は開始面で独立であり、同じ角を複数段へ再利用しない。

この式は一般M39入力にも成立するが、一般状態の測定後テンプレートには第7.7節の作用切断誤差が加わる。singlet型では全枝作用が固定なので、その誤差を必要としない。

## 7.10 singlet余弦則、非信号性、CHSH値

singlet型では

```math
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac14
\left[
1
-
AB\cos(x-y)
\right]
```

となる。従って相関は

```math
E(x,y)
=
\sum_{A,B}
AB
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
-\cos(x-y)
```

である。

一側周辺は

```math
\sum_A
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac12,
\qquad
\sum_B
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac12
```

なので、反対側の設定に依存しない。より一般には、第7.5節の非選択B相関行列から

```math
\sum_A
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\langle B_y|
\operatorname{Tr}_A
\left(
cc^\dagger
\right)
|B_y\rangle
```

が従う。

CHSH設定を

```math
x_0=0,
\qquad
x_1=\frac{\pi}{2},
\qquad
y_0=\frac{\pi}{4},
\qquad
y_1=-\frac{\pi}{4}
```

とすると、

```math
\left|
E_{00}
+
E_{01}
+
E_{10}
-
E_{11}
\right|
=
2\sqrt2
```

を得る。

平面内の任意の4設定では、単位ベクトルを $\boldsymbol a_i,\boldsymbol b_j$ として

```math
|S|
\leq
\left\|
\boldsymbol b_0+\boldsymbol b_1
\right\|
+
\left\|
\boldsymbol b_0-\boldsymbol b_1
\right\|
\leq
2\sqrt2
```

である。これはM41が実装したsinglet型、平面内2出力相関族の上界であり、一般測定族を拘束するTsirelson原理の導出ではない。

<!-- theorem-start:proposition -->
**命題（R111：singlet余弦統計とBell前提監査）**

R110の理想singlet型周期は、余弦共同確率、設定に依存しない一側周辺、標準CHSH値 $2\sqrt2$、平面内2出力族の上界 $2\sqrt2$ を与える。測定段階の局所Hamiltonianは可換だが、測定開始面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。
<!-- theorem-end:proposition -->

## 7.11 測定設定独立性と局所因子化

測定開始面の完全変数 $\Lambda$ には、2担体状態、源枝レジスター、中央作業領域、局所選択器角を含める。B担体は

```math
d^B
=
-c_A^x
```

なので、

```math
\mu_{\rm meas}
\left(
d\Lambda\mid x,y
\right)
\neq
\mu_{\rm meas}
\left(
d\Lambda
\right)
```

が一般に成立する。singlet型でも非選択B相関行列は $x$ に依存しないが、枝ラベルと条件付きB方向を含む完全な古典分解は $x$ に依存する。

一方、中央結合を停止した後の応答は

```math
P
\left(
A,B
\mid
\Lambda,x,y
\right)
=
P_A
\left(
A
\mid
\Lambda_A,x
\right)
P_B
\left(
B
\mid
\Lambda_B,y
\right)
```

と因子化できる。反対側の設定または結果を局所Hamilton方程式へ入れない。Bell不等式の破れは、この測定段階の局所因子化を破るのではなく、$\Lambda$ と設定の独立性を満たさないことで可能になる [1,2,9,23]。

観測周辺の非信号性は、測定設定独立性とは別の性質である。M41ではsinglet対称性により前者を保つが、準備後に設定レジスターだけを外部から変更した場合の統計は保証しない。設定は2担体準備より前に決まり、同じ準備周期へ入る必要がある。

## 7.12 前向き誤差と帰還誤差

観測開始から外部記録までに分布へ入る前向き誤差を

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

とする。$\delta_{\rm set}$ は設定無反応、$\delta_{\rm s}$ は源無反応、$\delta_A^{\rm loc},\delta_B^{\rm loc}$ は局所測定無反応、$\varepsilon_{\rm tr}$ は転送誤差、$\varepsilon_{\rm act}$ は一般状態の作用切断、$\varepsilon_{\rm rec}$ は記録誤差である。singlet型では $\varepsilon_{\rm act}=0$ とできる。

観測後の逆計算とresetは

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

と別に管理する。既に記録された同じ周期の分布へ $\varepsilon_{\rm ret}$ を遡って加えず、次周期の準備誤差へ渡す。

理想分布が非信号的で、各設定対の実分布が理想分布から全変動距離 $\epsilon_{\rm fwd}$ 以下なら、

```math
\left|
P_{\rm obs}
\left(
B\mid x,y
\right)
-
P_{\rm obs}
\left(
B\mid x',y
\right)
\right|
\leq
2\epsilon_{\rm fwd}
```

である。無反応を数値0として相関を計算すると、

```math
\left|
S_{\rm obs}
-
S_{\rm id}
\right|
\leq
8\epsilon_{\rm fwd}
```

を得る。従って

```math
\epsilon_{\rm fwd}
<
\frac{\sqrt2-1}{4}
```

なら、有限誤差下でも $|S_{\rm obs}|>2$ を保証できる。

## 7.13 Q2-2の達成判定と除外事項

固定目標Q2-2の「2つの測定端への接続」には、次の2つの読み方を区別する。

| 接続の意味 | 要求 | M41の判定 |
|---|---|---|
| 操作的接続 | Q2-1出力を利用し、2つの物理的測定端で局所測定・記録を行って目標共同統計を得る | 達成 |
| 状態的接続 | Q2-1の非因子化4モード状態全体を保存したまま、設定選択前に2つの独立物理部分系へ分配する | 未達・主張しない |

M41の「条件付き達成」の条件は、Q2-2を前者の操作的接続として読むことである。有限幅や誤差を小さくするパラメータ条件ではない。この解釈の下で、M41のsinglet型固定プログラムは合格条件を次の範囲で満たす。

| 合格条件 | 根拠 |
|---|---|
| Q2-1出力を利用した2つの物理的測定端 | R107、R108 |
| A中央枝選択を非選択操作として見たときB枝間コヒーレンスを失う | R108 |
| 測定中のA--B直接結合なし | R110 |
| A局所確認測定、B局所測定、各側の永久外部記録 | R110 |
| Born型共同分布とsinglet余弦則 | R110、R111 |
| CHSH不等式の破れ | R111 |
| 平面内2出力族のTsirelson上界 | R111 |
| 非信号性 | R111 |
| 測定設定独立性の破れ | R110、R111 |
| 有限幅、無反応、帰還 | R107、R109、R110 |

従ってQ2-2は、操作的接続の意味で、固定有限設定、準備先行、非空間分離、singlet型、無反応込み、制御された任意精度の範囲で条件付き達成と判定する。次は達成範囲に含めない。

1. M39の非因子化4モード状態全体の、設定非依存な2物理部分系への状態的分配。
2. 2担体準備後に自由に変更されるA設定またはB設定。
3. 空間的に隔たった設定選択、長距離空間分離、有限伝播速度を持つ時計配線。
4. 一般非singlet状態での作用側チャネルの不存在。
5. 有限資源で無反応なしの厳密2値測定。
6. 一般測定族を拘束するTsirelson原理。
7. 選択器列の独立同分布性と二項分布型有限標本揺らぎ。
8. 永久記録を含む有限閉鎖系全体の同一点帰還。
9. 多量子ビットへ多項式資源で拡張すること。
10. 標準的な空間分離Bell実験またはBell局所性の実験検証。

M41はBellの定理を否定しない。設定が共通過去の準備過程へ入るためBellの測定設定独立性を満たさない、前向き有限Hamiltonianモデルである。
