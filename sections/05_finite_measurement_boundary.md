@number: 5
@chapter: 本文
@title: 有限 Hamiltonian 装置部品と2境界履歴集団
@status: 最小結果符号化モデル、終端比較器、全履歴測度を分離し、`[R]` を独立な2境界統計原理として明示する。

## 5.1 第II部の目的

第2章から第4章は、観測座標の線形 Gaussian 経路法則と Nelson 作用形式を扱った。そこから Bell 型結果重みは出ない。Bell 実験を記述するには、少なくとも次の構造が必要である。

1. 左右の測定設定制御器。
2. 局所的に確定する2値記録。
3. 設定と結果符号を共通未来へ運ぶ伝達ベクトル。
4. 2つの伝達ベクトルを比較する、設定名を直接参照しない二次形式。
5. 比較結果と未読の作用分配変数を照合する終端座標。
6. 終端整合履歴を物理的集団とする2境界統計原理。

本章では、これらを有限 Hamiltonian 部品として定式化し、各部品が何を実現するかを分けて示す。局所装置は結果符号を指針へ写す最小符号化モデルであり、一般の測定相互作用ではない。一般の局所パルスは短時間極限で所望の正準写像へ近づく。第7章の終端比較器だけは、保存量との交換関係を用いて有限幅でも厳密な読出しを与える。

## 5.2 正準変数

1試行の第II部に必要な正準変数を次のように取る。

- 伝達ベクトル対：$(Q_A,P_A)$、$(Q_B,P_B)$。
- 結果種対：$(s_A,\pi_A)$、$(s_B,\pi_B)$。
- 測定設定制御対：$(a,\alpha)$、$(b,\beta)$。
- 応答モード対：$(x_A,p_A)$、$(x_B,p_B)$。
- 固定指針対：$(Y_A,\Pi_A)$、$(Y_B,\Pi_B)$。
- 局所有限浴対：$(r_{Xj},\varpi_{Xj})$、$X=A,B$、$1\leq j\leq n_X$。
- 作用分配用の正準対：$(q_s,p_s)$、$(q_0,p_0)$。
- 終端比較対：$(Y_R,\Pi_R)$。
- 相補時計中心対：$(\bar\tau,P_c)$。
- 自律順序時計対：$(\vartheta,J_c)$。

伝達ベクトルの作用を

```math
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
X=A,B
```

とする。作用分配系の2つの作用は

```math
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
```

```math
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right)
```

である。装置部品を自律時計で接続した形式的な全 Hamiltonian は

```math
H_{\rm tot}
=
H_{\rm src}
+H_{\rm ctrl}
+H_{\rm msg}
+H_{\rm seed}
+H_{\rm ptr}
+H_{\rm bath}
+H_\ell
+H_{\rm mix}
+H_{\rm cmp}
+H_{\rm or}
+H_{\rm clk}.
```

と書ける。各項の具体形と誤差の地位は付録Cにまとめる。この式は部品表であり、全自由項を含む有限幅発展が各理想正準写像を厳密に実行するという意味ではない。比較窓については、必要な全項を第7.1節で1本の Hamiltonian として明示する。

## 5.3 結果種と測定設定制御器

$s_X$ を円周座標とし、互いに等しい Liouville 体積を持つ2つの平坦領域 $\Sigma_X^+$、$\Sigma_X^-$ を取る。滑らかな周期関数 $\sigma$ を

```math
\sigma(s)
=
+1
\qquad
\left(
s\in\Sigma^+
\right),
```

```math
\sigma(s)
=
-1
\qquad
\left(
s\in\Sigma^-
\right)
```

とし、2領域の間だけで滑らかに補間する。基準準備は補間領域に台を持たない。したがって実際の台上で

```math
\sigma'(s)=0.
```

局所結果を

```math
A=\sigma(s_A),
\qquad
B=\sigma(s_B)
```

とする。負符号領域の指示関数は

```math
\chi_-(s)
=
\frac{1-\sigma(s)}2
```

である。

測定設定は制御座標の初期巨視領域で決まる。全試行に同じ Hamiltonian 関数を用い、

```math
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
```

という粗視化写像で設定を読み出す。以下では制御座標自体を簡単に $a,b$ と書く。

この最小モデルでは結果種を明示的に置き、$A$ と $B$ は測定設定や到来する伝達ベクトルに依存しない。したがって、この部品は結果を生成する測定器ではなく、既存の2値符号を応答モードと固定指針へ写す結果符号化器である。

より一般の局所決定論応答

```math
A=\mathscr A(a,\lambda_A),
\qquad
B=\mathscr B(b,\lambda_B)
```

を扱うには、設定 $a$、到来変数、局所微視状態を結合する具体的な局所 Hamiltonian 前処理を追加する必要がある。本論文はその一般前処理を構成せず、第7章では上の最小結果符号化モデルを用いる。Bell 監査に必要な局所因子化は満たすが、これだけで一般の物理的測定過程を実現したとはみなさない。

## 5.4 自律パルス Hamiltonian

時計角 $\vartheta$ 上に、互いに重ならない滑らかなパルス形 $f_{\nu,\epsilon}(\vartheta)$ を置き、

```math
\int f_{\nu,\epsilon}(\vartheta)d\vartheta=1
```

と規格化する。全 Hamiltonian に

```math
H_{\rm clk}
=
\Omega J_c
```

とパルス項

```math
H_{\rm pulse}
=
\Omega
\sum_\nu
f_{\nu,\epsilon}(\vartheta)K_\nu
```

を加える。各 $K_\nu$ は $J_c$ に依存しないため、

```math
\dot\vartheta
=
\frac{\partial H_{\rm tot}}{\partial J_c}
=
\Omega
```

が厳密に成立する。$J_c$ はパルスの反作用を受け、拡張した全 Hamiltonian のエネルギーは保存される。

ただし、自由 Hamiltonian $H_0$ もパルス中に同時に働く。したがって、一般にはパルスの全流れが生成子 $K_\nu$ の単位流れと厳密に一致するわけではない。パルスの時間幅を $\epsilon_\nu$ とし、有界な適用領域 $\mathcal K$ 上で関係する Hamiltonian ベクトル場と第1微分が有界なら、

```math
\sup_{z\in\mathcal K}
\left\|
\Phi_{\rm full}^{(\nu)}(z)
-
e^{X_{K_\nu}}z
\right\|
\leq
C_{\mathcal K}\epsilon_\nu
```

となる。詳細は付録C.3に示す。以後、局所分析と指針固定の式は短時間パルス極限の理想写像として書き、有限幅では $O(\epsilon_\nu)$ の補正を伴うものとする。

この自律化は、測定設定ごとに異なる Hamiltonian を外から挿入する操作ではない。測定設定は位相空間内の制御器状態、操作順序は同じ時計軌道上の異なる区間である。$(\vartheta,J_c)$ は操作順序時計であり、第5.9節の相補的内部時計とは別自由度である。

## 5.5 局所分析器と応答モード

A 側の分析器生成子を

```math
K_A^{\rm an}
=
-\left[
\phi(a)
+\pi\chi_-(s_A)
\right]I_A
-x_A\sigma(s_A)
```

とし、B 側も同様に

```math
K_B^{\rm an}
=
-\left[
\phi(b)
+\pi\chi_-(s_B)
\right]I_B
-x_B\sigma(s_B)
```

とする。

$K_A^{\rm an}$ の単位流れのパラメータを $\tau$ とすると、結果種の平坦領域上で

```math
\frac{dQ_A}{d\tau}
=
-\theta_A P_A,
\qquad
\frac{dP_A}{d\tau}
=
\theta_A Q_A,
```

```math
\theta_A
=
\phi(a)+\pi\chi_-(s_A),
```

および

```math
\frac{dp_A}{d\tau}
=
\sigma(s_A)=A,
\qquad
\frac{dx_A}{d\tau}=0
```

を得る。応答運動量を $p_A^{\rm in}=0$ に準備すれば、理想写像では

```math
p_A^{\rm out}=A.
```

伝達ベクトルは

```math
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm out}
=
R[\theta_A]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
=
A R[\phi(a)]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
```

となる。B 側も

```math
p_B^{\rm out}=B,
```

```math
u_B^{\rm out}
=
B R[\phi(b)]u_B^{\rm in}
```

を満たす。有限幅の全流れでは、これらの右辺に第5.4節の $O(\epsilon_{\rm an})$ 補正が加わる。補正が平坦領域と指針領域の幅より十分小さいことを、局所装置の適用条件とする。

応答モードは測定設定パルスと局所結果種に応答する一時変数である。結果確率を生成する浴ではない。各軌道の $A,B$ は結果種と局所 Hamiltonian 流れで一意に決まる。

## 5.6 固定指針への記録

滑らかな平坦関数 $\zeta(p)$ を

```math
\zeta(p)=+1
\quad
\left(
|p-1|<\delta_p
\right),
```

```math
\zeta(p)=-1
\quad
\left(
|p+1|<\delta_p
\right)
```

となるよう取る。固定指針への転写生成子を

```math
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
```

とする。単位流れでは

```math
\frac{d\Pi_X}{d\tau}
=
\zeta(p_X),
\qquad
\frac{dY_X}{d\tau}=0,
\qquad
\frac{dp_X}{d\tau}=0.
```

したがって理想写像で $\Pi_X^{\rm in}=0$ なら

```math
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B.
```

2つの互いに交わらない巨視領域

```math
\Gamma_X^+
=
\left\{
\Pi_X>\frac12
\right\},
\qquad
\Gamma_X^-
=
\left\{
\Pi_X<-\frac12
\right\}
```

を指針記録とする。有限幅補正が $1/2$ の領域間隔より十分小さければ、記録符号は変わらない。固定指針対はこの後の共通未来比較器から切り離すため、比較段階は過去の指針符号を変更しない。

応答モードには、記録後に有限局所浴

```math
H_{{\rm bath},X}
=
\sum_{j=1}^{n_X}
\left[
\frac{\varpi_{Xj}^2}{2m_{Xj}}
+\frac{m_{Xj}\omega_{Xj}^2r_{Xj}^2}{2}
\right]
+\epsilon_X x_X
\sum_{j=1}^{n_X}
c_{Xj}r_{Xj}
```

を結合できる。これは応答モードの一時情報と位相情報を複数自由度へ分散し、有限観測窓での再読出し誤差を小さくする。ただし有限閉鎖浴は真の散逸を与えず、十分長時間では再帰を持つ。記録の主張は

```math
\tau_{\rm lock}
\ll
\tau_{\rm cmp}
\ll
T_{{\rm rec},X}
```

の範囲に限る。

## 5.7 共通未来への伝播

局所記録時刻を $t_A,t_B$、両伝達ベクトルが同じ時空領域へ到達できる時刻を $t_C$、終端時刻を $T$ とし、

```math
t_A,t_B<t_C<T
```

とする。$t_C$ より前の結合図は

```math
(u_A,s_A,a,x_A,Y_A,\Gamma_{{\rm bath},A})
```

と

```math
(u_B,s_B,b,x_B,Y_B,\Gamma_{{\rm bath},B})
```

に分離する。A 側の Hamiltonian は B 側の測定設定、結果種、指針を含まず、B 側も同様である。

$t_C$ 以後に2つの伝達ベクトルを同じ比較器へ入れる。これは局所記録後の時間的な共通未来における通常の相互作用であり、空間的に分離した記録形成へ遠隔力を導入しない。第7章で現れる測定設定依存性は、共通未来の相互作用自体が過去を変更するためではなく、その相互作用を含む全軌道へ `[R]` を適用するためである。

## 5.8 終端関数と履歴測度

初期超曲面上の全微視状態を

```math
z_i=(\lambda,\eta,\xi_A,\xi_B)
```

とする。$\lambda$ は結果応答を完結させる生成源と局所装置の変数、$\eta$ は後に積分する作用分配系、混合器、終端比較対などの未読変数、$\xi_A,\xi_B$ は測定設定制御変数である。基準準備では

```math
\rho_S(\lambda,\eta,\xi_A,\xi_B)
=
\rho_S(\lambda,\eta)
\rho_A(\xi_A)
\rho_B(\xi_B)
```

とする。

終端時刻 $T$ に、全測定設定と全結果に共通な非負関数

```math
G_R:\Gamma\longrightarrow[0,\infty)
```

を固定する。`[R]` による条件付き履歴測度は

```math
d\mu_R^{a,b}(\lambda,\eta)
=
\frac{
\rho_S(\lambda,\eta)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
}{
Z_{a,b}
}
d\lambda\,d\eta.
```

$\lambda$ を固定して未読変数を積分した終端整合度を

```math
h_{a,b}(\lambda)
=
\int
\rho_S(\eta\mid\lambda)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
d\eta
```

と定義すると、生成源超曲面上の事後分布は

```math
\rho_R(\lambda\mid a,b)
=
\frac{
\rho_S(\lambda)h_{a,b}(\lambda)
}{
Z_{a,b}
}
```

となる。

<!-- theorem-start:proposition -->
**命題（終端整合度の判定条件）**
全測定設定対に対して同一の事後分布 $\rho_R(\lambda)$ が存在するための必要十分条件は、ある非負関数 $h(\lambda)$ と正定数 $c_{a,b}$ が存在して

```math
h_{a,b}(\lambda)
=
c_{a,b}h(\lambda)
```

がほとんど至る所で成立することである。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
上式が成立すれば $c_{a,b}$ は規格化で消える。逆に事後分布が全測定設定で同じなら、

```math
\frac{h_{a,b}(\lambda)}{Z_{a,b}}
=
\frac{h_{a',b'}(\lambda)}{Z_{a',b'}}
```

なので、各終端整合度は共通関数へ比例する。
<!-- theorem-end:proof -->

したがって固定した $G_R$ であっても、その Hamiltonian 引き戻し

```math
G_R\circ\Phi_{a,b}^{T}
```

が生成源変数を測定設定に依存して再重みづけし得る。

## 5.9 相補的内部時計による終端半空間の正準実現

終端比較対 $(Y_R,\Pi_R)$ に中心対 $(\bar\tau,P_c)$ を加え、2つの内部時計対を

```math
\tau_A
=
\bar\tau+\frac{Y_R}{2},
\qquad
\tau_B
=
\bar\tau-\frac{Y_R}{2},
```

```math
\varrho_A
=
\frac{P_c}{2}+\Pi_R,
\qquad
\varrho_B
=
\frac{P_c}{2}-\Pi_R
```

で定める。実際、

```math
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R
```

なので、これは正準変換である。

内部時計の自由 Hamiltonian を

```math
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
```

とする。中心・相対変数では

```math
H_{\rm or}
=
\frac{\Pi_R^2}{M_\tau}
+
\left(
\frac{1}{4M_\tau}
+
\frac{\kappa_c}{2}
\right)
P_c^2.
```

相補的領域

```math
P_c=0
```

は自由運動と、$\bar\tau$ に依存しない比較パルスの双方で保存される。この領域では

```math
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
```

```math
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
```

したがって $\Pi_R>0$ は A 時計が正向き、B 時計が負向きの順序付き相補性を表す。これは2粒子が実験室時刻に対して逆向きに伝播するという意味ではない。左右の粒子と伝達ベクトルは通常どおり生成源から局所装置、共通未来へ進み、反対になるのは内部時計または境界情報の向きである。

<!-- theorem-start:proposition -->
**命題（終端半空間の相補時計実現）**
$P_c=0$、比較パルス直前の $\Pi_R=E_*>0$ とする。比較生成子を

```math
K_R
=
Y_R
\left(
h-\kappa I_-
\right)
```

とし、$g_R(t)=\Omega f_R[\vartheta(t)]$ の時間積分を1とする。比較窓の自由 Hamiltonian が $h$ と $I_-$ を保存するなら、

```math
\dot\Pi_R
=
g_R(t)
\left(
\kappa I_- -h
\right),
\qquad
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}
```

である。$Y_R$ はパルス中も一般に動くが、$\dot\Pi_R$ は $Y_R$ に依存しない。したがって有限幅パルスの後に厳密に

```math
\Pi_R(T)
=
E_*+\kappa I_- -h.
```

順序付き時計向きが終端まで保存される条件

```math
\varrho_A(T)\geq0,
\qquad
\varrho_B(T)\leq0
```

は

```math
\Pi_R(T)\geq0
```

と必要十分である。
<!-- theorem-end:proposition -->

証明の要点は

```math
\{h,K_R\}
=
\{I_-,K_R\}
=
0
```

である。比較パルスは作用分配系と差動モードの角変数を動かし得るが、読出しに必要な2つの作用は変えない。完全な比較窓 Hamiltonian と積分は第7.1節および付録C.6に示す。

これにより $\Pi_R$ は任意の終端運動量ではなく2時計の相対運動量、$E_*$ は時計向きが反転するまでの初期運動量余裕、$G_R=\mathbf1_{\{\Pi_R(T)\geq0\}}$ は順序付き向き保存条件と読める。

ただし Hamilton 方程式は $\Pi_R(T)<0$ の軌道を禁止しない。この軌道では

```math
\varrho_A(T)<0,
\qquad
\varrho_B(T)>0
```

となり、時計向きが交換されるだけである。したがって相補的時計は終端半空間の形を導くが、その半空間に入る履歴だけを物理的集団とする `[R]` までは導かない。

## 5.10 `[R]` と事後選別

数式上、

```math
\rho_R
\propto
\rho_S G_R\circ\Phi^T
```

は、実験後の棄却抽出と同じ条件付き確率に見える。本論文が `[R]` を物理的な境界原理として用いるためには、少なくとも次を要求する。

1. $G_R$ は Bell データを見る前に装置の終端巨視領域として固定する。
2. 全測定設定と全結果に同じ終端装置と分解能を用いる。
3. 実現した指針記録を後から除外しない。
4. 終端幅、作用分配系の総エネルギー、比較尺度を独立な較正で決める。
5. 外部開始数、指針記録数、終端完了数の関係を報告する。

これらを満たせず、観測済み試行の一部を捨てて初めて Bell 値が出るなら、本構成は検出事後選別に退化する。`[R]` を公理として書くだけでは、この操作上の区別は保証されない。

## 5.11 本章の結論

局所分析器、応答モード、固定指針、有限局所浴、設定伝達ベクトル、共通未来への伝播、終端履歴測度を有限正準部品の中に配置した。ただし局所装置は結果符号化器であり、一般の測定相互作用ではない。局所パルスの理想写像には有限幅で $O(\epsilon)$ の補正がある。

終端比較対は相補的内部時計の相対対として正準実現できる。比較生成子を線形な $K_R=Y_R(h-\kappa I_-)$ としたことで、内部時計の自由運動により $Y_R$ が変化しても、終端運動量の読出しは厳密に保たれる。

結果頻度を定める原理は、局所浴の散逸、指針の保持時間、比較速度、時計相補性のいずれでもない。物理的履歴集団を定める `[R]` と、次章で導く終端整合体積である。
