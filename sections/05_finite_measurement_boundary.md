@number: 5
@chapter: 本文
@title: 同じ2成分場の低ランク Bell 対モード
@status: 固定された2つの直交源チャンネル、反対称源、左右の局所モード回転を仮定すると、Bell 余弦枝作用は厳密に得られる。低ランク相関は派生量であり、独立した配置空間場ではない。一般的な結果形成は未完成である。

## 5.1 物理空間上の1つの場

Bell 粒子対に対しても、基本的な場変数は物理空間上の2成分場

```math
\boldsymbol\Phi(x)
=
\begin{pmatrix}
\Phi_1(x)\\
\Phi_2(x)
\end{pmatrix}
```

とその正準運動量だけである。2粒子の配置 $(X_A,X_B)$ 上に独立な場を置かない。

複素表示 $\zeta=\Phi_1+i\Phi_2$ を用い、第2.9節の固定モード展開から左右へ進む局在モードを

```math
z^A_{\mu r},
\qquad
z^B_{\nu r},
\qquad
\mu,\nu\in\{+,-\},
\qquad
r\in\{1,2\}
```

とする。$\mu,\nu$ は各局所分析器の2出力モード、$r$ は互いに直交する源チャンネルである。源チャンネルは、同じ場の異なる周波数、時間スロット、空間正規モードなどとして実装できる。

モード射影は場の正準1形式から誘導される。同じ固定直交基底を場座標と場運動量へ用いる限り、有限モード係数は正準である。設定または結果ごとに基底を選び直さない。

## 5.2 低ランク相関行列

左右モードの相関を

```math
C_{\mu\nu}
=
\sum_{r=1}^{2}
\eta_r
z^A_{\mu r}
\left(
z^B_{\nu r}
\right)^*
```

と定める。行列表示では

```math
C
=
\sum_{r=1}^{2}
\eta_r
z^{A,(r)}
\left(
z^{B,(r)}
\right)^\dagger.
```

従って $\operatorname{rank}C\leq2$ である。

$C$ は独立した場ではない。基礎モード $z^A,z^B$ から計算される派生量であり、独自の Poisson 括弧または独自の運動方程式を与えない。共通内部回転

```math
z^A
\longmapsto
e^{i\beta}z^A,
\qquad
z^B
\longmapsto
e^{i\beta}z^B
```

に対し、$C$ は不変である。この共役規約により、比較 Hamiltonian と保存位相作用 $\mathcal J_\phi$ の対称性を両立できる。

## 5.3 反対称源

理想源が準備する相関行列を

```math
C_0
=
\sqrt{\frac{\mathcal K}{2}}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。これは2つのランク1項へ

```math
C_0
=
\sqrt{\frac{\mathcal K}{2}}
\left[
e_+e_-^{\mathsf T}
-
e_-e_+^{\mathsf T}
\right]
```

と分解できる。従って、2つの直交源チャンネルで実係数の代表点を準備すれば、低ランク構成から $C_0$ を得られる。

この節で厳密なのは、準備された2チャンネルから $C_0$ を合成する代数である。場と対生成装置の有限 Hamiltonian が、任意の初期状態からこの反対称源へ到達することは別の準備問題である。相対位相が失われると2チャンネル間の干渉項が消えるため、源から比較器までの位相保持が必要である。

## 5.4 左右の局所分析器

設定 $a,b$ に対応するモード角を $\alpha_a,\alpha_b$ とする。左右の分析器は局所モードだけを

```math
z^{A,(r)}
\longmapsto
R(\alpha_a)z^{A,(r)},
```

```math
z^{B,(r)}
\longmapsto
R(\alpha_b)z^{B,(r)}
```

と回転する。ここで

```math
R(\alpha)
=
\begin{pmatrix}
\cos\alpha&-\sin\alpha\\
\sin\alpha&\cos\alpha
\end{pmatrix}.
```

相関行列の表示は

```math
C(a,b)
=
R(\alpha_a)
C_0
R(\alpha_b)^{\mathsf T}
```

となるが、物理的に回しているのは $C$ ではなく、A側とB側の局所場モードである。

A側の正準座標を $(Q^A_{\mu r},P^A_{\mu r})$ とすれば、回転生成子を

```math
G_A
=
\sum_r
\left(
Q^A_{+r}P^A_{-r}
-
Q^A_{-r}P^A_{+r}
\right)
```

と書ける。局所 Hamiltonian

```math
H_A
=
\dot\alpha_a(\vartheta)G_A
```

がA側だけの回転を生成する。B側も同様であり、

```math
H_{\rm analyzer}
=
H_A(a)+H_B(b)
```

は空間的に分離した局所和である。

## 5.5 結果枝振幅

結果ポート $A,B\in\{+1,-1\}$ の基底ベクトルを $e_A,e_B$ とする。結果組 $(A,B)$ に対応する相関振幅を

```math
C_{AB}(a,b)
=
e_A^{\mathsf T}
C(a,b)
e_B
```

と定め、枝作用を

```math
K_{AB}
=
|C_{AB}|^2
```

とする。

<!-- theorem-start:theorem -->
**定理（反対称対モードの余弦作用）**
反対称源 $C_0$ と実回転 $R(\alpha_a)$、$R(\alpha_b)$ の下で、

```math
K_{AB}
=
\frac{\mathcal K}{4}
\left[
1-AB\cos\Delta_{ab}
\right],
```

```math
\Delta_{ab}
=
2
\left(
\alpha_a-\alpha_b
\right)
```

が成立する。さらに、

```math
\sum_{A,B}K_{AB}
=
\mathcal K,
\qquad
\sum_BK_{AB}
=
\sum_AK_{AB}
=
\frac{\mathcal K}{2}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$\delta=\alpha_a-\alpha_b$ とする。反対称行列と回転の積を直接計算すると、同符号ポートでは

```math
K_{++}
=
K_{--}
=
\frac{\mathcal K}{2}\sin^2\delta,
```

異符号ポートでは

```math
K_{+-}
=
K_{-+}
=
\frac{\mathcal K}{2}\cos^2\delta
```

を得る。$\cos2\delta=\cos\Delta_{ab}$ を用いれば主式が従う。総和と周辺和は主式を符号について足せばよい。
<!-- theorem-end:proof -->

この定理は、設定依存する余弦作用の生成を局所モード回転から与える。結果頻度はまだ与えない。

## 5.6 物理角との対応

数式中の基本角はモード回転角 $\alpha$ であり、観測装置の表示角と常に同じとは限らない。

- 光子偏光型では $\alpha_a=a$、$\alpha_b=b$ と置けば、$\Delta_{ab}=2(a-b)$ となる。
- 平面内のスピン型測定では $\alpha_a=a/2$、$\alpha_b=b/2$ と置けば、$\Delta_{ab}=a-b$ となる。

この対応を固定せずに $\Delta_{ab}$ を物理角と呼ぶと、余弦の角度が2倍ずれる。本論文では、一般式では $\Delta_{ab}$ を用い、特定実験との比較時に $\alpha(a)$ を明示する。

## 5.7 局所結果と共同量の役割分担

A側の局所装置だけでは $C_{AB}$ を計算できない。B側のモードも必要だからである。従って $K_{AB}$ を空間的に離れた測定時刻の瞬間的な局所力へ使わない。

局所測定窓では、各側が次を行う。

1. 設定に応じて局所モードを回転する。
2. 2つの出力ポートを形成する。
3. 既存の局所結果sector $A$ または $B$ を指針へ記録する。
4. 結果ポートと源チャンネルの振幅を戻りモードへ写す。

本論文の局所装置は、既存の2値結果sectorをポートと記録へ符号化する最小模型である。連続したミクロ状態から安定な唯一結果を形成する一般測定器は構成していない。

## 5.8 有限伝播と共通未来

左右の戻りモードは、局所記録後に有限速度で共通未来領域へ伝播する。遅延応答を記号的に

```math
z_{\rm ret}^{A}(t)
=
\int
G_A(t-s)z_{\rm out}^{A}(s)\,ds,
```

```math
z_{\rm ret}^{B}(t)
=
\int
G_B(t-s)z_{\rm out}^{B}(s)\,ds
```

と書く。$G_A,G_B$ の支持は、各局所測定から共通未来比較窓までの伝播時間より前に現れない。

理想式では比較窓で

```math
z_{\rm ret}^{A}
=
z_{\rm out}^{A},
\qquad
z_{\rm ret}^{B}
=
z_{\rm out}^{B}
```

となる規格化を用いる。損失、分散、チャンネル混合、相対位相ずれは第8章の誤差へ含める。

## 5.9 位相雑音と可視度

2つの源チャンネルの相対位相に揺らぎ $\varphi$ があると、干渉項は

```math
\chi_\phi
=
\left\langle
e^{i\varphi}
\right\rangle
```

で減衰する。対称な位相雑音で $\chi_\phi$ が実なら、

```math
K_{AB}
=
\frac{\mathcal K}{4}
\left[
1
-
ABV_\phi\cos\Delta_{ab}
\right],
\qquad
V_\phi
=
\chi_\phi.
```

戻り伝達の左右利得が異なる場合は、総規格化と可視度の両方が変わる。理想 Bell 法則には、結果と設定によらない共通利得、および十分小さい相対位相雑音が必要である。

## 5.10 本章の結論

同じ物理空間上の2成分場から、2つの直交源チャンネルと左右の固定出力モードを切り出すことで、独立な6次元場を使わず Bell 余弦作用を構成できる。低ランク相関 $C$ は派生量であり、左右の局所分析器は基礎場モードだけを回す。

ここまでで得たのは $K_{AB}$ の生成である。$K_{AB}$ を共通未来で物理的な比較作用へ写し、完全履歴の境界測度と結ぶ過程を第6章と第7章で扱う。
