@number: I
@chapter: 付録
@title: M52 source-driven setting-pre paired-Hopf receiver
@status: M52の選択blockを単一試行sourceとして使う決定論的開放receiverを定義し、R180Bのpaired位相、template方向、有限時間吸引率、作用収支を証明する。有限閉鎖Hamiltonian liftとR180Cの装置統合は主張しない。

## I.1 目的と旧M48からの変更

旧M48は設定前の内部等重みseedをA設定に応じた2枝へroutingし、固定spin-flip tensorからsinglet型2翼rayを作った。現行receiverではこの独立sourceを使わない。M52の実際の1試行末端信号 $V$ をA設定basisでblock分解し、R180Aが選んだblockを物理sourceとしてpaired-Hopf流へ渡す。

従って本付録では、試行集団の交差moment

```math
\mathbb E
\left[
z_Az_B^{\mathsf T}
\right]
```

を計算して単一試行templateへ書き戻さない。旧M48で必要だったHaar seed、等重みcell、安全盆 $h_x=0$、設定別seed tableも現行主線から外れる。branch重みはM52信号のprojector作用 $p_{s|x}(V)$ から生じる。

M52のhold signal、branch pointer、選択block port、receiver carrier、pump、sink、clockは別の物理自由度として数える。解析上の方向 $b=w/\|w\|$ は、controllerが未知係数を測って書き込む命令ではない。選択された未規格化block $w$ を固定portから注入し、Hopf飽和が動径を標準化する。

## I.2 template分解

安全枝について規格化templateを

```math
a,b\in\mathbb C^2,
\qquad
a^\dagger a=b^\dagger b=1
```

とする。2翼receiver信号 $z_A,z_B\in\mathbb C^2$ を

```math
c_A=a^\dagger z_A,
\qquad
p_A=(I_2-aa^\dagger)z_A,
```

```math
c_B=b^\dagger z_B,
\qquad
p_B=(I_2-bb^\dagger)z_B
```

と分ける。従って

```math
z_A=c_Aa+p_A,
\qquad
z_B=c_Bb+p_B,
\qquad
a^\dagger p_A=b^\dagger p_B=0.
```

paired scalarを

```math
m
=
\frac{c_A+\overline{c_B}}2,
\qquad
d
=
\frac{c_A-\overline{c_B}}2
```

と置く。逆変換は

```math
c_A=m+d,
\qquad
c_B=\overline m-\overline d
```

である。$d=0$ かつ $p_A=p_B=0$ なら

```math
z_A=ma,
\qquad
z_B=\overline m b.
```

$|m|=1$ では2翼が同じ位相を反対符号で持つpaired fiberになる。

標準source loadでは、branch pointerが既知の $a=u_{s,x}$ をA carrierへ送り、M52の選択blockを係数読出しなしにB carrierへ注入する。

```math
z_A(0)=a,
\qquad
z_B(0)=w_{s,x}=\sqrt{p_{s|x}}\,b.
```

このとき

```math
p_A(0)=p_B(0)=0,
\qquad
m_0=\frac{1+\sqrt{p_{s|x}}}{2},
\qquad
d_0=\frac{1-\sqrt{p_{s|x}}}{2}.
```

$p_{s|x}\geq\tau$ なら $m_0\geq(1+\sqrt\tau)/2>0$ であり、下の吸引に必要な非零bright seedを独立に仮定する必要はない。一般入口状態に対する定理は有限source-load偏差も許す。

## I.3 採用開放方程式

準備portの窓関数を $\lambda_{\rm PH}(t)\geq0$ とし、有効時間を

```math
\tau_{\rm PH}(t)
=
\int_{t_{\rm in}}^t
\lambda_{\rm PH}(s)\,ds
```

とする。以下ではdotを $\tau_{\rm PH}$ 微分とする。

```math
\dot m
=
g(1-|m|^2)m,
\qquad
\dot d
=
-\kappa_{\rm p}d,
```

```math
\dot p_A
=
-\kappa_\perp p_A,
\qquad
\dot p_B
=
-\kappa_\perp p_B,
\qquad
g,\kappa_{\rm p},\kappa_\perp>0.
```

元のreceiver信号では

```math
\dot z_A
=
\left[
g(1-|m|^2)m
-\kappa_{\rm p}d
\right]a
-\kappa_\perp p_A,
```

```math
\dot z_B
=
\overline{
\left[
g(1-|m|^2)m
+\kappa_{\rm p}d
\right]
}b
-\kappa_\perp p_B.
```

準備窓中は $a,b$ をtemplate holdで固定する。窓終了後に $\lambda_{\rm PH}$ を零へし、$z_A,z_B$ を局所holdへ移して中央couplerを切る。有限hold誤差と切替反作用はR180Cの条件へ残す。

各項の役割は次の通りである。

| 項 | 役割 | 外部境界 |
|---|---|---|
| $g(1-|m|^2)m$ | paired bright modeへのpumpと単位動径飽和 | pump sourceとlimiterを必要とする |
| $-\kappa_{\rm p}d$ | 2翼のpaired位相差を減衰 | dark sinkへ作用を送る |
| $-\kappa_\perp p_A$ | A template直交成分を減衰 | A transverse sinkを必要とする |
| $-\kappa_\perp p_B$ | B template直交成分を減衰 | B transverse sinkを必要とする |
| $\lambda_{\rm PH}$ | source port、pump、sinkの接続と切断 | clock、切替仕事、残留相関を外部帳簿へ残す |

## I.4 exact solutionと有限時間率

$R=|m|^2$ とすると

```math
\dot R
=
2g(1-R)R.
```

$m_0\neq0$ なら

```math
R(\tau)
=
\frac1{
1+
\left(
R_0^{-1}-1
\right)e^{-2g\tau}
}.
```

$\dot m/m$ は実数なので $m$ の位相は保存される。$\alpha=\arg m_0$ とすれば

```math
m(\tau)
=
e^{i\alpha}\sqrt{R(\tau)}.
```

他の成分は

```math
d(\tau)
=
e^{-\kappa_{\rm p}\tau}d_0,
```

```math
p_A(\tau)
=
e^{-\kappa_\perp\tau}p_A(0),
\qquad
p_B(\tau)
=
e^{-\kappa_\perp\tau}p_B(0)
```

である。

有界初期集合

```math
0<r_-
\leq
|m_0|
\leq
r_+<\infty,
```

```math
|d_0|
\leq
d_+,
\qquad
\|p_A(0)\|
\leq
p_+,
\qquad
\|p_B(0)\|
\leq
p_+
```

を固定する。logistic解から有限定数 $C_r$ を選んで

```math
\left|
\sqrt{R(\tau)}-1
\right|
\leq
C_re^{-2g\tau}
```

とできる。従って

```math
\begin{aligned}
\left\|
z_A-e^{i\alpha}a
\right\|
&\leq
C_re^{-2g\tau}
+d_+e^{-\kappa_{\rm p}\tau}
+p_+e^{-\kappa_\perp\tau},\\
\left\|
z_B-e^{-i\alpha}b
\right\|
&\leq
C_re^{-2g\tau}
+d_+e^{-\kappa_{\rm p}\tau}
+p_+e^{-\kappa_\perp\tau}.
\end{aligned}
```

本文の $K_{180}$ と $\gamma_{180}$ は例えば

```math
K_{180}
=
2C_r+2d_++2p_+,
\qquad
\gamma_{180}
=
\min
\left\{
2g,\kappa_{\rm p},\kappa_\perp
\right\}
```

と選べる。

<!-- theorem-start:proof -->
**証明（R180B）**

$R=|m|^2$ のlogistic方程式、$m$ の位相保存、$d,p_A,p_B$ の線形減衰を上の通り解く。template分解の逆変換へ代入し、三角不等式と有界初期集合を使えば2翼の有限時間吸引上界を得る。証明終。
<!-- theorem-end:proof -->

## I.5 作用様量と開放収支

```math
N_{\rm rec}
=
|m|^2+|d|^2+
\|p_A\|^2+
\|p_B\|^2
```

と置く。採用流から

```math
\dot N_{\rm rec}
=
2g(1-|m|^2)|m|^2
-2\kappa_{\rm p}|d|^2
-2\kappa_\perp
\left(
\|p_A\|^2+
\|p_B\|^2
\right)
```

を得る。$|m|<1$ ではpumpからbright作用が入り、$|m|>1$ ではlimiter側へ戻る。paired差と直交成分はsinkへ流れる。この式はreceiver内部の局所作用収支であり、M52 source、branch latch、template hold、clock、切断器、局所測定、記録、fresh交換を含む総エネルギー保存式ではない。

位相体積の収縮、sink entropy、設定情報流、切替仕事を零とはしない。温度、熱流、微視的環境Hamiltonianを指定していないため、熱力学量の総和を閉じない。

## I.6 singletと旧paired fiber

singletではR180Aから

```math
a=u_{s,x},
\qquad
b=-\mathsf E\overline{u_{s,x}},
\qquad
p_{s|x}=\frac12
```

を得る。R180Bの吸引先は

```math
z_A
=
e^{i\alpha}u_{s,x},
\qquad
z_B
=
-e^{-i\alpha}
\mathsf E\overline{u_{s,x}}.
```

B側のglobal signを位相 $\alpha\mapsto\alpha+\pi$ またはtemplate位相へ吸収すれば、旧M48のspin-flip paired fiberと同じ局所ray、作用、Born応答になる。

ただし生成機構は異なる。旧M48は内部fair seedと設定別安全盆routingから枝を作った。R180ではM52信号のprojector作用が枝重みを作り、選択block自体がB templateを運ぶ。従って旧交差momentを現行M52信号と同一視しない。

## I.7 開放模型監査

| 監査項目 | R180Bで明示する内容と限界 |
|---|---|
| 状態 | $m,d,p_A,p_B$ と物理template hold $a,b$ |
| 初期条件 | $m_0$ は零から離れ、全成分を有限compact集合に制限する |
| 雑音 | paired-Hopf流自体は決定論的。白色雑音、Itô規約、定常確率測度を使わない |
| 駆動と散逸 | bright pump、paired差sink、2つのtransverse sink、準備窓を分ける |
| source | M52の選択された未規格化blockを物理portから受ける。係数表を外部入力しない |
| 有限時間 | $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ で評価する |
| 切断 | template hold、pump、sinkを切り、2翼局所holdへ渡す。反作用評価はR180Cの条件 |
| 熱力学 | $N_{\rm rec}$ の局所収支だけを計算し、総仕事・総熱・総entropyは未閉鎖 |
| ミクロ由来 | 全driftは現象論的に採用する。具体的流体、回路、振動子bath、有限閉鎖Hamiltonianからは未導出 |

## I.8 反証条件と非主張

次のいずれかが必要ならR180Bの物理的receiver解釈は成立しない。

- M52の未知block係数を外部で測定してからtemplateを書き込む。
- 選択blockを集団momentへ縮約し、別試行のcarrierを再準備する。
- template holdの反作用が有限時間誤差内に抑えられない。
- $m_0=0$ を有限時間で自発的に非零へすることを上の方程式だけから要求する。
- node枝を捨てて成功試行だけを再規格化する。
- R180B単独から切断後局所性、Born branch状態数、記録、reset、総熱力学を結論する。

R180Bはsource-driven paired-Hopf吸引だけを閉じる。M52 hold、projector latch、source port、pump、sink、2翼R170を同じ装置へ統合する条件はR180Cに残す。
