@number: T
@chapter: 付録
@title: R191のブラウン巨視的スピン2結果射影読出し
@status: Q1/Q2の2結果射影読出しを、既知のブラウン巨視的スピンと吸引域捕獲へ接続する採用開放模型。R164--R190--R170経路は一般有限結果集合・作用殻型の代替実現として残す。

## T.1 目的と責務境界

R191は、2結果直交射影で固定された作用を、有限混合時間・有限温度・有限decision時間・transducer誤差・正式な無反応を含む1試行1結果の古典読出しへ変換する。本付録で新しく使う確率自由度は固定長の単磁区巨視的スピンだけである。熱揺らぎを受ける固定長磁化のFokker--Planck記述、一軸異方性下の高障壁2状態近似はBrownの古典結果に基づく [57]。Brownian spinの確率力学との関係はKubo--Hashitsume [56]、有限時間switching probabilityとの関係はGrinstein--Koch [58]を参照する。

本結果はBrownian spinや磁化反転そのものの新規性を主張しない。新しい責務は、同じ古典信号の射影作用和・作用差を吸引域境界へ直接結合し、外部でBorn確率を計算せずに結果頻度へ変えること、およびその有限誤差を共通instrument契約として切り出すことである。

R191は射影後信号の生成を担わない。結果固定後の

```math
(z,0)
\longmapsto
(P_rz,(I-P_r)z)
```

という可逆な枝分けと次段への受渡しは、第2章の既存共通射影選別機構とR181Dが担う。一般深さで作用下限を回復する方向を変えない振幅再調整もR181D/R179側に残す。

## T.2 射影作用とtransducer契約

非零信号 $Z$ と2結果直交射影 $P_++P_-=I$ に対して

```math
J_+
=\mathcal J_0 Z^\dagger P_+Z,
\qquad
J_-
=\mathcal J_0 Z^\dagger P_-Z,
```

```math
S=J_++J_->0,
\qquad
D=J_+-J_-.
```

と置く。理想Born重みは

```math
p_+=\frac{J_+}{S},
\qquad
p_-=\frac{J_-}{S}.
```

実装transducerは作用和・作用差の近似値 $\widehat S,\widehat D$ を出力し、固定安全集合上で

```math
|\widehat S-S|
\leq
\varepsilon_\Sigma S,
\qquad
|\widehat D-D|
\leq
\varepsilon_\Delta S,
\qquad
0\leq\varepsilon_\Sigma<1
```

を満たすとする。これは特定素子を定理へ固定しない抽象接続契約である。例えば同周波数RF/LC信号の対称弱pickupと二乗則検波を使えば作用に比例するDC出力を作れるが、R191本体はその実装を必要条件にしない。

実吸引域境界を

```math
\widehat u_*
=-\frac{\widehat D}{\widehat S},
```

理想境界を

```math
u_*
=-\frac DS
```

とすれば、

```math
|\widehat u_*-u_*|
\leq
\frac{\varepsilon_\Delta+\varepsilon_\Sigma}
{1-\varepsilon_\Sigma}
=: \varepsilon_u.
```

従って外部制御器が $D/S$ を除算する必要はない。作用和と作用差を別々の物理係数へ線形結合した結果として、その比が吸引域境界の位置に現れる。

## T.3 混合窓と一様方向

指針変数を固定長単磁区巨視的スピン $\boldsymbol m\in S^2$ とし、読出し軸成分を

```math
U=m_z\in[-1,1]
```

とする。混合窓では一軸異方性と軸方向biasを切り、生成子

```math
\mathcal L_{\rm mix}
=D_{\rm mix}\Delta_{S^2}
```

の等方回転拡散へ接続する。球面一様分布が唯一の定常分布であり、その $z$ 周辺は $U[-1,1]$ である。

R190Bと同じ球面スペクトル分解を使い、$S_{\rm mix}=D_{\rm mix}T_{\rm mix}$、$q=e^{-4S_{\rm mix}}$ と置けば任意の初期方向について

```math
D_{\rm TV}
\left(
\mathcal L(U_{T_{\rm mix}}),
U[-1,1]
\right)
\leq
\varepsilon_{\rm mix}
:=
\min
\left\{
1,
\frac{\sqrt{q(3-q)}}{2(1-q)}
\right\}.
```

R191ではこの混合評価だけを共通化し、R190Cの作用開口やR161の静的平方根率を使わない。

## T.4 decision potentialとBorn吸引域測度

混合終了後、実transducer出力を固定し、decision窓で

```math
V_{\rm dec}(u)
=-\frac\chi2
\left(
\widehat S u^2
+2\widehat D u
\right),
\qquad
\chi>0
```

を与える。平方完成すると

```math
V_{\rm dec}(u)
=-\frac{\chi\widehat S}{2}
(u-\widehat u_*)^2
+\text{const.}
```

である。零雑音の散逸運動を無次元時間で

```math
\dot u
=(1-u^2)(u-\widehat u_*)
```

と書けば、$u>\widehat u_*$ は $+1$、$u<\widehat u_*$ は $-1$ へ流れる。

理想transducerなら $\widehat u_*=u_*$ であり、混合分布が球面一様なら

```math
P(+)
=P(U>u_*)
=\frac{1-u_*}{2}
=\frac{J_+}{J_++J_-},
```

```math
P(-)
=\frac{J_-}{J_++J_-}.
```

従ってBorn型2値重みは、連続指針変数を直接二値へ量子崩壊させる仮定ではなく、古典的な2つの吸引域が混合分布中で占める測度として得られる。

## T.5 有限温度の軸対称stochastic LLG縮約

実装された無次元障壁強度を

```math
\widehat\Delta
=
\frac{\chi\widehat S}
{2k_{\rm B}T_{\rm dec}}
```

とする。$S\geq S_{\min}>0$ なら

```math
\widehat\Delta
\geq
\Delta_{\min}
:=
\frac{\chi(1-\varepsilon_\Sigma)S_{\min}}
{2k_{\rm B}T_{\rm dec}}.
```

軸対称Brown Fokker--Planck方程式を無次元時間 $\tau$ で

```math
\partial_\tau\rho
=
\partial_u
\left[
-(u-\widehat u_*)(1-u^2)\rho
+
\frac{1-u^2}{2\widehat\Delta}
\partial_u\rho
\right]
```

と採用し、$u=\pm1$ には零流束境界条件を置く。対応するItô SDEは

```math
dU_\tau
=
\left[
(1-U_\tau^2)(U_\tau-\widehat u_*)
-
\frac{U_\tau}{\widehat\Delta}
\right]d\tau
+
\sqrt{
\frac{1-U_\tau^2}{\widehat\Delta}
}
dW_\tau.
```

物理時間 $t$ との対応は

```math
\tau
=2D_{\rm dec}\widehat\Delta\,t
```

とする。$Y_\tau=\operatorname{artanh}U_\tau$ へ変換するとItô補正と幾何学的driftが相殺し、

```math
dY_\tau
=
(U_\tau-\widehat u_*)d\tau
+
\frac{dW_\tau}
{\sqrt{\widehat\Delta(1-U_\tau^2)}}.
```

となる。

## T.6 保護帯、初到達、有限時間上界

通常読出し経路では推定重みが両方とも固定cutoff $\tau_{\rm cut}>0$ 以上であることを要求する。保護帯幅 $g>0$、捕獲幅 $\zeta>0$ を

```math
g+\zeta<2\tau_{\rm cut}
```

と選ぶ。初期点が

```math
|U_0-\widehat u_*|<g
```

なら正式な無反応へ送る。完全一様分布でこの質量は $g$ であり、有限混合誤差を含めれば $g+\varepsilon_{\rm mix}$ 以下である。

捕獲領域を

```math
C_+
=[1-\zeta,1],
\qquad
C_-
=[-1,-1+\zeta]
```

とし、最初に到達した側を吸収記録へ写す。$m_\zeta=\zeta(2-\zeta)$ と置く。

1次元拡散のscale densityは

```math
s'(u)
=
\frac{
\exp[-\widehat\Delta(u-\widehat u_*)^2]
}{1-u^2}.
```

保護帯外から境界側へ $g/2$ だけ熱的に戻る確率を、反対basinへ到達する前の保守的failureとして数えると、両側共通に

```math
q_{\rm ret}
\leq
\min
\left\{
1,
\frac{2}
{m_\zeta\Delta_{\min}g^2}
\exp
\left(
-\frac7{16}\Delta_{\min}g^2
\right)
\right\}.
```

さらに

```math
L_{\max}
=
\operatorname{artanh}(1-\zeta)
-
\operatorname{artanh}(-1+2\tau_{\rm cut}+g)
```

とし、無次元decision時間 $T$ が

```math
T>\frac{2L_{\max}}g
```

を満たすなら、保護帯側へ戻らず時刻 $T$ まで捕獲されない確率は指数martingale評価により

```math
q_{\rm time}
\leq
\exp
\left[
-\frac{
\Delta_{\min}m_\zeta
(gT/2-L_{\max})^2
}{2T}
\right].
```

従って有限温度decision failureは

```math
\varepsilon_{\rm FP}
\leq
q_{\rm ret}+q_{\rm time}
```

で抑えられる。これはKramers高障壁漸近を定理の仮定にせず、軸対称1次元拡散のscale functionとmartingale評価から得る保守的有限時間上界である。

## T.7 端点dispatcherと完全結果空間

有限温度で $p=0,1$ を誤差零の吸引域捕獲として要求しない。実推定

```math
\widehat p_+
=\frac{\widehat S+\widehat D}{2\widehat S},
\qquad
\widehat p_-
=\frac{\widehat S-\widehat D}{2\widehat S}
```

について

```math
\min\{\widehat p_+,\widehat p_-\}
<\tau_{\rm cut}
```

なら、大きい側を決定論的経路へ送る。これは成功試行だけの再規格化ではなく全試行を定義するdispatcherである。通常経路と端点経路のどちらも、捕獲されない有限時間事象は無反応 $\varnothing$ として残す。

吸収記録の有限誤差を $\varepsilon_{\rm cap}$ とする。通常経路の完全結果分布 $P_{191}$ と理想Born分布 $P_{\rm Born}=(p_+,p_-,0)$ の全変動距離は

```math
D_{\rm TV}(P_{191},P_{\rm Born})
\leq
\varepsilon_{\rm mix}
+g
+\frac{\varepsilon_u}{2}
+q_{\rm ret}
+q_{\rm time}
+\varepsilon_{\rm cap}
=: \varepsilon_{191}^{\rm int}.
```

端点経路には

```math
\varepsilon_{191}^{\rm edge}
\leq
\tau_{\rm cut}
+\frac{\varepsilon_u}{2}
+\varepsilon_{\rm cap}
```

という保守的上界を使い、

```math
\varepsilon_{191}
=
\max
\left\{
\varepsilon_{191}^{\rm int},
\varepsilon_{191}^{\rm edge}
\right\}
```

を1ノード誤差とする。

## T.8 逐次測定への受渡し

結果 $r$ が固定された後、既存の共通射影選別機構は非規格化branch

```math
Z_r=P_rZ
```

をactive signalとして次段へ渡す。次段の2結果射影 $Q_s$ に対するR191入力は

```math
J_{s|r}
=\mathcal J_0\|Q_sP_rZ\|^2,
\qquad
S_r
=\mathcal J_0\|P_rZ\|^2.
```

従って理想条件付き確率は

```math
P(s|r)
=
\frac{\|Q_sP_rZ\|^2}
{\|P_rZ\|^2}.
```

物理信号を $P_rZ/\|P_rZ\|$ へ非線形に規格化する必要はない。有限段の射影列では条件付き確率の積がtelescopingし、R181DのLüders型完全履歴を回収する。一般深さで $\|P_rZ\|^2$ が読出し下限を下回り得る場合だけ、既存の方向を変えない振幅再調整を使う。

## T.9 Q2-2での責務

Q2-2ではR191を中央集約4結果samplerとして使わない。R180の設定先行2端構造を維持し、中央の2結果潜在選択とA、Bの各局所2結果読出しに同じR191契約を特殊化する。従って二つの物理測定端、設定順序、非信号性監査、測定設定独立性の破れの監査対象は変更しない。

## T.10 熱力学、資源、非主張

mixing、decision、captureは開放過程であり、完全cycleのresetとは区別する。decision potentialを投入する有限外部仕事、熱浴への散逸、結果情報を吸収記録へ移す過程をR191の局所収支とし、結果相関履歴を外へ排出して能動部を次試行へ戻す責務はR179へ残す。

深さ $m$ の有限逐次測定で各ノード誤差を $O(\epsilon/m)$ に取り、例えば $g=O(\epsilon/m)$ とすると、熱的retreatを同次数にする十分条件は

```math
\Delta_{\min}g^2
\gtrsim
\log\frac m\epsilon.
```

従って

```math
\Delta_{\min}
=
O
\left(
\frac{m^2}{\epsilon^2}
\log\frac m\epsilon
\right)
```

で足りる。$m$ が回路深さの多項式ならこの障壁要求も多項式である。ただし作用下限、transducerの一様較正、総熱、配線、resetを同じ装置族で多項式外部資源に閉じることはR191単独から従わない。

R191は次を主張しない。

1. Brownian spin、Néel--Brown反転、一軸異方性そのものの新規性。
2. R164/R190/R170の一般有限結果集合または作用殻実現の不要性。
3. 任意に深い測定列でbranch作用が自動的にnoise floorより上に保たれること。
4. transducer、巨視的スピン、router、記録、resetを単一閉鎖Hamiltonianへ統合したこと。
5. 空間分離Bell実験またはBell局所隠れ変数模型を構成したこと。

R191の役割は、Q1/Q2の2結果射影ノードについて既知の古典開放磁化力学を共通読出し部品として採用し、Born重み、二値化、有限温度、有限時間、無反応、逐次受渡しを一つの明示誤差契約にまとめることである。
