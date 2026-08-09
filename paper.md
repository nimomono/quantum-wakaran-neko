# 概要


本論文は、有限自由度の古典Hamiltonian 系を基礎とし、量子力学に特徴的な可逆力学、測定操作、空間包絡、Bell 型統計が、どの仮定と誤差の下で現れ得るかを検証する。単一量子ビット型装置、空間振動子網、一般有限基底装置、Bell 二側履歴を別模型として明示し、未完成の統一模型を先取りしない。

第1の主結果は、2モード正準担体M38によるQ1--Q3の構成である。信号を

```math
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}},
\qquad
I_{\rm ph}
=
\mathcal J_0b^\dagger b
=
\mathcal J_0
```

とする。共通位相 $b\mapsto e^{i\gamma}b$ に不変な操作・測定代数へ縮約すると、

```math
S^3/U(1)
\simeq
\mathbb{CP}^1
\simeq
S^2
```

を得る。Bloch ベクトル $\boldsymbol r=b^\dagger\boldsymbol\sigma b$ は

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

を満たす。局所位相回転と $QQ+PP$ 交換の有限列は同じ2モード担体上で任意の $SU(2)$ を厳密に生成する。

駆動作用・角変数を加えた時間非依存Hamiltonian は、回転座標で

```math
i\dot c
=
\frac12
\left(
\Delta\sigma_z+\Omega\sigma_x
\right)c
```

となる。従って

```math
P_{1\to2}(t)
=
\frac{\Omega^2}{\Omega^2+\Delta^2}
\sin^2
\left(
\frac{\sqrt{\Omega^2+\Delta^2}}{2}t
\right)
```

が厳密に得られる。Q1は、Bloch 球、共通位相不変性、任意の $SU(2)$、Rabi 振動について達成と判定する。

Q2では、任意の Bloch 軸 $\boldsymbol n$ の2結果作用比

```math
p_s(\boldsymbol n)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
```

をM35型の滑らかな作用選択器へ渡す。安全結果 $s$ では測定後信号が厳密に固有状態 $|\boldsymbol n,s\rangle$ となる。滑らかな有限時間Hamiltonian 流は連結入力領域全体を相異なる2固有状態だけへ写せないため、比較境界近傍を正式な無反応結果とする。無反応率は有限増幅で任意に小さくできる。

2つの独立選択器角を用い、周期末に2次元トーラス上の無理数平行移動を行う。同軸再測定では反対符号の安全結果が生じず、異軸 $\boldsymbol n,\boldsymbol m$ の理想共同分布は

```math
P(s,t)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
\frac{1+st\boldsymbol n\cdot\boldsymbol m}{2}
```

となる。有限幅分布との全変動距離は2段の無反応率の和以下である。Q2は、無反応を除外せず、制御された任意精度で達成と判定する。

Q3では、滑らかな比較ポインターを外部記録セルへ正準剪断でコピーした後、第2測定、第1測定の順で内部逆計算する。装置は準備点へ戻り、記録は外部セルに残る。装置偏差と外部空モードの交換角を $\phi$ とすると、

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta
```

である。完全交換または部分収縮により、旧装置状態は使用済み外部セルへ移る。有限個の能動自由度、永久記録セル流、reset セル流、局所作用・角時計を合わせ、次周期の準備集合へ任意精度で戻る弱開放完全周期を構成する。有限 $N$ 周期は有限閉鎖Hamiltonian 系へ埋め込めるが、無期限運転は外部セル供給を要する。Q3も制御された任意精度で達成と判定する。

第2の主結果は、別模型M37による空間Schrödinger 型包絡である。位置だけで局所結合した有限実古典振動子網を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

とする。局所回転包絡は反回転項を含む厳密式

```math
i\mathcal J_0\dot b
=
h_Lb
+
h_Le^{2i\omega_0t}\overline b
```

を満たす。行列平方根を使う正常モード包絡は厳密だが一般に非局所である。弱結合量

```math
\eta
=
\frac{2\|h_L\|}{\mathcal J_0\omega_0}
<1
```

の下で、自然時間における局所包絡と目標Schrödinger 型解の差を $O(\eta)$ で抑える。Q9は、有限実振動子、実対称時間非依存演算子、弱結合・有限時間の範囲で達成と判定する。

第3の結果は、M35による一般有限 $L$ の固定基底測定である。任意有限基底変換を隣接2モード回路へ分解し、作用読出し、累積比較、滑らかな無反応領域、測定後状態、内部逆計算、無理数回転を $3L+4$ 正準対で構成する。長期分布と理想Born 型分布の距離は

```math
D_{\rm TV}
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

である。一般有限 $L$ の外部記録、弱開放 reset、複数段測定、長距離時計配線は未完成なので、Q5は部分達成である。

第4の結果はBell 型二側履歴模型M36である。反対称な左右集団交差相関から

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

が代数的に得られる。独立局所Haar 角の基準測度を、余弦区間への整合事象 $G$ で条件付けると、余弦共同確率、非信号周辺、標準設定でのCHSH値 $2\sqrt2$、設定分布保存を得る。完全履歴測度は設定依存なので、Bell の前提違反は測定設定独立性にある。

ただし、余弦区間を単一試行の源変数から生成する有限Hamiltonian 、整合支持 $G$ の物理的必然性、完全境界流束測度の結果非依存因子化は未導出である。Q7は条件付き模型として部分達成である。

本文は8章から成る。第1章で記述層、測度、主結果の確立度を示す。第2章と第3章でM37の空間包絡、第4章でM38のQ1--Q3、第5章でM35の一般有限基底測定、第6章でBell 二側履歴、第7章で誤差と資源、第8章で反証条件と未完成ベンチマークを扱う。正常モード変換、作用区間、一般測定装置、Bell 境界、2モード完全周期の詳細は付録A--Eへ置く。

# 記述層、測度、主結果の範囲

> **位置づけ：** M38の2モード完全装置、M37の空間振動子網、M35の一般有限基底装置、M36のBell 二側履歴を分離する。Q1は厳密、Q2とQ3は制御された任意精度、Q9は弱結合・有限時間で達成とする。Q5とQ7は部分達成であり、未構成のM0と統一母測度を現行定理の仮定に使わない。


## 問題設定

本論文の目的は、明示的な古典Hamiltonian 系から、量子力学に特徴的な可逆力学と確率構造が有効理論として現れ得る範囲を明らかにすることである。量子力学をミクロHamiltonian の入力には使わず、得られた力学、測定操作、統計を判定するときに比較対象として使う。

有限次元Schrödinger 方程式を実正準座標へ写すことだけでは、量子力学の創発にならない。本稿は次を分けて要求する。

1. $L=2$ の同じ正準担体上で、状態空間、可逆操作、Rabi 振動を構成する。
2. その担体を滑らかな測定後状態、逐次測定、記録、reset へ接続する。
3. 空間Schrödinger 型包絡は、通常の位置結合を持つ有限実振動子網から誤差付きで導く。
4. 一般有限 $L$ の測定回路と完全周期を、$L=2$ の達成から分離して評価する。
5. Bell 統計は二側履歴支持に依存する条件付き模型として監査する。

M38は1と2、M37は3、M35は4、M36は5を担う。これらを1つのM0へ統合したとは主張しない。

## 5つの記述層

| 層 | 変数 | 主な法則 | 確立度 |
|---|---|---|---|
| M37ミクロ振動子層 | $q,p$ | 位置ばね結合 $H_{\rm micro}$ | 厳密 |
| M37局所有効包絡層 | $b$ | 反回転項を含む厳密式、$h_L$ による有限時間近似 | 近似誤差付き |
| M38の2モード装置層 | 2モード信号、2段測定器、局所時計、外部セル | $SU(2)$、Rabi 振動、逐次測定、記録、逆計算、reset | 厳密または明示誤差付き |
| M35の一般有限基底層 | $L$ モード信号、テンプレート、作用・記録レジスター、時計 | 隣接2モード回路、滑らかな比較、SWAP 、内部逆計算 | 固定プログラムで厳密または明示誤差付き |
| M36のBell 二側履歴層 | 局所結果角、未来角、終端支持 | 条件付き履歴測度 | 支持条件に依存 |

M37の正常モード包絡 $\widetilde b$ は、ミクロ振動子を解析するための厳密だが一般に非局所な正準変数である。独立した非局所物理場として追加しない。

M38とM35の任意複素基底変換は、局所位相回転と $QQ+PP$ 交換の有限列で実装する。$QQ+PP$ 交換は運動量間結合を含むため、M37の位置ばね網と同じハードウェアではない。$L=2$ のQ1--Q3はM38内部で閉じ、M37との統合を達成条件へ入れない。

## 現行測度と将来の統一測度

理想有効担体の調製集団については

```math
C_M(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
d_td_t^\dagger
\right]
```

と相関行列を定める。$\mu_{\mathcal P,M}$ は調製条件 $\mathcal P$ とプログラム $M$ を固定した集団測度であり、補助統計理論に使う。

M35の固定純粋準備 $\chi$ と固定基底 $W$ の周期では、

```math
d\mu_{\chi,W}^{\rm M35}
=
\frac{d\vartheta}{2\pi}
\otimes
\delta_*
```

がPoincaré 不変測度になる。$\delta_*$ は選択器角以外の内部準備集合を表す。

M38の固定2軸プログラムでは、

```math
d\mu_{\chi,\boldsymbol n,\boldsymbol m}^{\rm M38}
=
\frac{d\vartheta_1d\vartheta_2}{(2\pi)^2}
\otimes
\delta_*
```

が理想Poincaré 不変測度になる。$1,\alpha_1,\alpha_2$ の有理数体上の1次独立性により、2角平行移動は一意エルゴード的である。

Bell 側では制約前基準測度を $\nu_{\rm B}^0$、二側整合事象を $G$ とし、

```math
d\mu_{\rm B}
=
4\mathbf1_G
\,d\nu_{\rm B}^0
```

を使う。

これらの測度は役割が異なる。可変調製、可変基底、空間伝播、Bell 境界、外部記録までを同じ反復系へ統合する将来目標の母測度を $\mu_*$ と書く。本稿は $\mu_*$ の存在、不変性、エルゴード性を現行定理の仮定に使わない。

## 主結果1A：2モード可逆力学

M38の固定作用面を

```math
I_{\rm ph}
=
\frac12
\sum_{j=1}^2
\left(
Q_j^2+P_j^2
\right)
=
\mathcal J_0
```

とする。共通位相に不変なBloch 写像により、有効状態空間は $S^2$ になる。Bloch 成分のPoisson 代数は

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

である。任意の実ベクトル $\boldsymbol\Omega$ に対する

```math
H_{\boldsymbol\Omega}
=
\frac{\mathcal J_0}{2}
b^\dagger
\left(
\boldsymbol\Omega\cdot\boldsymbol\sigma
\right)b
```

は

```math
\dot{\boldsymbol r}
=
\boldsymbol\Omega\times\boldsymbol r
```

を厳密に与える。局所位相回転と2モード交換のEuler 分解により、任意の $SU(2)$ を同じ担体上で実装できる。

駆動作用・角変数を加えた自律Hamiltonian は、共鳴振幅、一般化Rabi 振動数、離調による振幅低下を厳密に与える。従ってQ1はM38内部で達成である。

## 主結果1B：任意軸と逐次測定

任意の Bloch 軸 $\boldsymbol n$ と結果 $s=\pm1$ に対し、M38の出力作用比は

```math
p_s(\boldsymbol n)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
```

である。安全セクターでは正準SWAP 後の信号が厳密に $|\boldsymbol n,s\rangle$ となる。

滑らかな有限時間Hamiltonian 流の連続性により、連結入力領域全体を相異なる2固有状態だけへ写すことはできない。本稿は比較境界の遷移領域を正式な無反応結果とし、無反応率を

```math
\delta_j
\leq
2\frac{w_{{\rm eff},j}}{\mathcal J_0}
+
\varepsilon_{{\rm cut},j}
```

で抑える。

同軸再測定では反対符号の安全結果が生じない。異軸測定では独立な2選択器を使い、理想共同分布

```math
P(s,t)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
\frac{1+st\boldsymbol n\cdot\boldsymbol m}{2}
```

を得る。無反応を含む実分布との距離は $\delta_1+\delta_2$ 以下である。従ってQ2は制御された任意精度で達成である。

## 主結果1C：永久記録と弱開放周期

滑らかな比較ポインター $\Pi_j(z)$ と空の外部記録セルを

```math
G_{\rm rec}
=
\sum_{j=1}^2
P_j^R\Pi_j(z)
```

で結合する。理想入口 $P_j^R=0$ では装置へ反作用せず、記録座標だけが移動する。記録後に第2段、第1段の順で逆計算すれば、内部装置は準備点へ戻り、記録は外部セルへ残る。

外部空モードとの正準交換は

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta
```

を与える。完全交換では装置偏差を空セルへ置換し、部分交換では収縮する。局所作用・角時計、外部記録セル、reset セル流を加えると、固定有限プログラムの能動装置は次周期の準備集合へ任意精度で戻る。

有限 $N$ 周期は外部セルを含む有限閉鎖Hamiltonian 系へ埋め込める。無期限運転では外部セル流が必要であり、情報と旧偏差を消去していない。従ってQ3は制御された任意精度で達成である。

## 主結果2：局所振動子網からの空間包絡

M37の有限実振動子網を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

とする。局所包絡は反回転項を含む厳密式

```math
i\mathcal J_0\dot b
=
h_Lb
+
h_Le^{2i\omega_0t}\overline b
```

を満たす。厳密正常モード生成子と目標生成子の差は、$\eta=2\|h_L\|/(\mathcal J_0\omega_0)<1$ の下で

```math
\left\|h_{\rm ex}-h_L\right\|
\leq
\frac{\|h_L\|^2}
{2\mathcal J_0\omega_0(1-\eta)^{3/2}}
```

である。自然時間では局所包絡状態誤差を $O(\eta)$ で抑える。Q9は有限自由度、実対称時間非依存演算子、弱結合・有限時間の範囲で達成である。

## 主結果3：一般有限基底測定

M35は任意の有限 $L$、固定純粋準備、固定基底について、$3L+4$ 正準対の内部測定周期を構成する。任意基底変換を隣接2モード回路へ分解し、滑らかな安全結果、無反応、測定後状態、内部逆計算、無理数回転による長期頻度を得る。

Q9の規格化包絡 $\widehat b_{\rm mic}$ と目標状態 $\chi_L$ について、任意有限基底の作用比分布は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\langle\widehat b_{\rm mic},\chi_L\rangle
\right|^2
}
```

を満たす。この数学的インターフェースはM37とM35の同一ハードウェア化を意味しない。

一般有限 $L$ の複数段測定、永久外部記録、弱開放 reset、長距離時計配線は未完成なので、Q5は部分達成である。

## 主結果4：条件付きBell 二側履歴

左右の反対称集団交差相関を規格化すると、

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

を得る。独立局所Haar 角の半円分割から4結果の基準密度 $1/4$ を得る。未来角が記録済み結果の余弦区間へ入る事象を $G$ とし、物理履歴を $G$ に支持させれば、余弦共同確率、非信号周辺、標準設定でのCHSH値 $2\sqrt2$ を得る。完全履歴測度は設定依存なので、Bell の測定設定独立性は成立しない。

単一試行変数からの余弦区間多重度、$G$ の物理的必然性、完全境界流束の因子化は未解決である。Q7は仮説依存の条件付き模型として部分達成である。

## 導出状態

| 主張 | 導出状態 | 主な制限 |
|---|---|---|
| M38のBloch 球と共通位相縮約 | 厳密結果 | 固定作用面、採用操作・測定代数 |
| M38の任意の $SU(2)$ | 厳密結果 | $QQ+PP$ と局所位相回転 |
| M38の自律Rabi 振動 | 厳密結果 | 固定2モード模型 |
| 任意の Bloch 軸の安全測定後状態 | 厳密結果 | 無反応込み |
| 同軸・異軸逐次測定分布 | 明示誤差付き結果 | 固定純粋入力、固定2軸、非混合 |
| 外部記録剪断と内部逆計算 | 厳密結果 | 理想空記録セル |
| 外部セル交換 reset | 厳密写像と誤差上界 | 外部セル準備幅、有限流路 |
| M38の完全周期 | 明示誤差付き結果 | 固定有限プログラム、弱開放 |
| M37の局所位置結合振動子網 | 厳密結果 | 有限自由度、時間非依存 |
| M37のSchrödinger 型局所包絡 | 近似結果 | $\eta<1$、有限時間 |
| M35の一般有限基底周期 | 厳密または明示誤差付き | 固定純粋準備、固定基底 |
| Bell 二側履歴統計 | 仮説依存結果 | 余弦区間と支持 $G$ を採用 |
| 全プログラム共通のM0と $\mu_*$ | 予想・未解決 | 統一周期は未構成 |

Q2とQ3の「達成」は、任意の $\epsilon>0$ に対して有限装置の無反応率、分布誤差、周期帰還誤差を $\epsilon$ 未満にできることを意味する。有限資源で誤差が厳密に零であることを意味しない。

## 本論文が主張しないこと

本論文は次を主張しない。

1. 量子力学の全構造を導出したこと。
2. M37、M38、M35、M36を1つのM0へ統合したこと。
3. M38の $QQ+PP$ 操作をM37の位置ばねだけから導いたこと。
4. M37とM38が同じハードウェアであること。
5. 一般有限 $L$ の完全操作・測定周期を閉じたこと。
6. 可変調製・可変基底を含む統一エルゴード周期。
7. 無理数回転が独立同分布または二項分布型有限標本統計を与えること。
8. 無反応なしに滑らかな有限時間Hamiltonian で連結入力領域全体を厳密な2固有状態だけへ写すこと。
9. 有限閉鎖系の固定容量で永久記録を無期限に蓄積すること。
10. 異なる結果履歴を外部記録ごと同じ位相点へ押しつぶすこと。
11. reset の熱力学的最小仕事、総エネルギー収支、資源下界を導いたこと。
12. 局所包絡作用がM37のミクロ発展中に厳密保存されること。
13. 正常モード包絡が局所物理場であること。
14. 位相担体のセル選択が粒子の局所検出そのものであること。
15. 粒子の連続軌道、Wallstrom 問題、連続スペクトルを含む一般Born 則。
16. Bell 余弦区間を単一試行のミクロ源から導いたこと。
17. Bell 二側測度を通常の前向き初期値問題の不変測度として生成したこと。
18. 一般Tsirelson 原理または外部設定介入に対する統計安定性。

配置拡散・Nelson経路、旧2成分誘導場、旧位置作用殻、前周期記憶模型は現行主線に採用しない。再利用価値のある結果と不採用理由は研究メモまたは版履歴で管理する。

## 本文と付録の構成

第2章と第3章はM37によるQ9のミクロ導出を扱う。第4章はM38によるQ1--Q3、第5章はM35によるQ5の一般有限基底部分、第6章はM36によるQ7の条件付きBell 二側履歴、第7章は各模型の誤差と資源、第8章は未完成目標と反証条件を扱う。

付録Aは正常モード正準変換、付録Bは相関行列と作用選択、付録CはM35の一般有限基底装置、付録DはBell 境界模型、付録EはM38の2モード完全周期を扱う。

# 局所結合された実古典振動子網

> **位置づけ：** 位置だけで結合した有限古典振動子網、局所回転包絡の厳密方程式、正常モード包絡への正準変換は有限次元で厳密である。局所包絡の Schrödinger 型発展と局所作用保存は弱結合・有限時間の近似である。


## 3つの記述層

本稿の力学側は、次の3層を区別する。

1. ミクロ層は、実位置 $q_i$ と実運動量 $p_i$ を持つ有限個の古典振動子である。
2. 有効担体層は、搬送振動を除いた局所複素包絡 $b_i$ である。
3. 測定装置層は、第4章のM38と第5章のM35で、作用読出し、比較、正準SWAP 、記録、逆計算を行う正準制御系である。

ミクロ層から有効担体層への移行はQ9の対象である。M38は $L=2$ のQ1--Q3、M35は一般有限 $L$ のQ5を扱う。任意の装置用正準混合がM37の局所ばね網だけで実装できるとは仮定せず、M37とM38の同一ハードウェア化も主張しない。

振動子の個数を $L<\infty$、共通質量を $M_{\rm osc}>0$、搬送周波数を $\omega_0>0$ とする。$M_{\rm osc}$ はミクロ振動子の質量であり、第3章に現れる有効質量 $m$ と区別する。固定作用尺度 $\mathcal J_0>0$ は正準座標の規格化に使う。

## ミクロ Hamiltonian

実正準対を

```math
\left\{q_i,p_j\right\}
=
\delta_{ij}
```

とし、時間非依存な有限振動子網を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

で定める。$A=A^{\mathsf T}$ は実対称である。局所グラフ $G=(V,E)$ 上では

```math
A
=
D_\delta+L_\kappa
```

とし、成分表示を

```math
H_{\rm micro}
=
\sum_i
\left[
\frac{p_i^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_0^2q_i^2}{2}
+
\frac{\delta_iq_i^2}{2}
\right]
+
\frac12
\sum_{\{i,j\}\in E}
\kappa_{ij}
\left(q_i-q_j\right)^2
```

と書ける。ここで $\kappa_{ij}=\kappa_{ji}\geq0$ である。$D_\delta$ は対角離調、$L_\kappa$ は重み付きグラフ Laplacian である。

安定条件は

```math
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
>
0
```

である。離調 $\delta_i$ は負でもよいが、全剛性行列は正定値でなければならない。本章では浴、散逸、環境残差を加えない。閉鎖有限振動子網だけでQ9の基準定理を構成する。

## 局所正準座標と回転包絡

各振動子に局所的な規格化座標

```math
Q
=
\sqrt{M_{\rm osc}\omega_0}\,q,
\qquad
P
=
\frac{p}{\sqrt{M_{\rm osc}\omega_0}}
```

を導入する。これは頂点ごとに独立な正準変換であり、$\{Q_i,P_j\}=\delta_{ij}$ を保つ。局所複素振幅と回転包絡を

```math
a
=
\frac{Q+iP}{\sqrt{2\mathcal J_0}},
\qquad
b(t)
=
e^{i\omega_0t}a(t)
```

と定める。複素数は実2次元正準平面の表示であり、量子的な生成消滅演算子ではない。

摂動行列に対応する有効演算子を

```math
h_0
=
\frac{\mathcal J_0}{2M_{\rm osc}\omega_0}A
```

とする。$A$ が局所疎行列なら $h_0$ も同じグラフ上で局所的である。

## 反回転項を含む厳密方程式

<!-- theorem-start:theorem -->
**定理（局所回転包絡の厳密方程式）**
第2.2節のミクロ Hamiltonian に対し、局所回転包絡は厳密に

```math
i\mathcal J_0\dot b
=
h_0b
+
h_0e^{2i\omega_0t}\overline b
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
規格化座標で Hamiltonian は

```math
H_{\rm micro}
=
\frac{\omega_0}{2}
\left(P^{\mathsf T}P+Q^{\mathsf T}Q\right)
+
\frac{1}{2M_{\rm osc}\omega_0}
Q^{\mathsf T}AQ
```

となる。$Q=\sqrt{\mathcal J_0/2}(a+\overline a)$ を代入し、複素 Poisson 括弧を使うと

```math
i\mathcal J_0\dot a
=
\mathcal J_0\omega_0a
+
h_0
\left(a+\overline a\right)
```

を得る。$b=e^{i\omega_0t}a$ へ移れば結論が従う。
<!-- theorem-end:proof -->

第2項は反回転項である。位置結合だけの実ばね網では、この項を厳密に消すことはできない。従って

```math
i\mathcal J_0\dot b
=
h_0b
```

をミクロ方程式として最初から置くのは正しくない。第3章で、反回転項の効果を正常モード変換と弱結合展開により有限時間で評価する。

## 局所作用は厳密保存量ではない

局所包絡から作る作用を

```math
I_{\rm loc}(t)
=
\mathcal J_0b(t)^\dagger b(t)
```

とする。厳密方程式から

```math
\frac{dI_{\rm loc}}{dt}
=
2
\operatorname{Im}
\left[
b^\dagger h_0
e^{2i\omega_0t}
\overline b
\right]
```

となり、一般には零でない。保存されるのはミクロエネルギーであり、局所回転包絡の作用ではない。

この点は第5章との接続で重要である。測定器へ入る直前の $I_{\rm loc}$ を読み、その時点の作用比 $I_k/I_{\rm loc}$ を使う単発測定は定義できる。しかし、伝播中の局所作用を厳密保存量として扱ったり、準備から測定まで自動的に同じ規格化が保たれると主張したりしてはならない。

## 厳密正常モード包絡

正定値行列

```math
\Omega
=
\left(
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
\right)^{1/2}
```

を定める。$\Omega$ を使って正常モード正準振幅 $c$ を作り、搬送回転を除いた厳密包絡を

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

とする。付録Aで正準変換を明示し、厳密に

```math
i\mathcal J_0\dot{\widetilde b}
=
h_{\rm ex}\widetilde b,
\qquad
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

が成立することを示す。

$\widetilde b$ は厳密に $\mathcal J_0\widetilde b^\dagger\widetilde b$ を保存する。ただし $\Omega$ の行列平方根を含むので、一般には各頂点だけで定義できる局所変数ではない。役割分担は次の通りである。

| 包絡 | 局所性 | 発展 | 作用保存 |
|---|---|---|---|
| $b$ | 頂点ごとに局所 | 反回転項を含めて厳密 | 一般には近似 |
| $\widetilde b$ | 一般には非局所 | $h_{\rm ex}$ で厳密 | 厳密 |
| 有効解 $b_L$ | 目標グラフ上で局所 | $h_L$ で近似 | 有効模型内で厳密 |

## 目標グラフ演算子との係数対応

有限空間グラフの重みを $g_{ij}=g_{ji}\geq0$ とし、

```math
\left(L_G\chi\right)_i
=
\sum_{j:\{i,j\}\in E}
g_{ij}
\left(\chi_i-\chi_j\right)
```

とする。目標とする実対称演算子を

```math
h_L
=
\frac{\mathcal J_0^2}{2m}L_G
+
V_L,
\qquad
V_L
=
\operatorname{diag}
\left(V_1,\ldots,V_L\right)
```

とする。古典パラメータを

```math
\kappa_{ij}
=
\frac{M_{\rm osc}\omega_0\mathcal J_0}{m}
g_{ij},
\qquad
\delta_i
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}
V_i
```

と選べば $h_0=h_L$ になる。従って、Laplacian の疎結合構造と局所ポテンシャルの形は、局所ばね結合と固有周波数離調から得られる。

一方、$m$ と $\mathcal J_0$ の値はこの対応式の設計パラメータである。特定の普遍定数または粒子質量がミクロ振動子網から必然的に選ばれることは示していない。

## 適用範囲

位置ばね結合から直接得られる $A$ と $h_L$ は実対称である。磁場に対応する Peierls 位相、一般の複素 hopping、運動量に比例する結合は本定理に含まれない。これらを厳密に実装するには、位置と運動量の両方を結ぶ追加の正準結合が必要になる。

本稿のQ9定理は時間非依存 $A$ に限定する。時間依存 $A(t)$ が有界であるだけでは不十分である。$2\omega_0$ 近傍の Fourier 成分が反回転項と共鳴し得るため、時間依存駆動には例えば

```math
\frac{\sup_t\left\|h_L(t)\right\|}
{\mathcal J_0\omega_0}
\ll1,
\qquad
\frac{\sup_t\left\|\dot h_L(t)\right\|}
{\mathcal J_0\omega_0^2}
\ll1
```

のような低速条件、または明示的な非共鳴条件が別に必要である。M38のQ1はこの位置ばね近似を使わず厳密に閉じる。時間依存M37を同じハードウェアへ統合する課題は、Q9を超える一般化として第8章に残す。

## 既知の古典振動子表示との関係

有限次元 Schrödinger 方程式を古典正準座標または結合振動子へ写すこと自体は既知である [34--37]。特に、位置結合だけを用いる弱結合近似と、位置・運動量の両結合を用いる厳密写像は先行研究で区別されている [35--37]。

本稿は次を新規性として主張しない。

1. 複素ベクトルを2倍次元の実ベクトルで表すこと。
2. 任意の Hermitian 行列を設計済み2次 Hamiltonian へ埋め込むこと。
3. 結合振動子が Schrödinger 型運動を近似できること。

本稿で追加するのは、局所位置結合網について反回転項を落とさない厳密式、正常モード生成子との作用素誤差、有限時間状態誤差、局所包絡誤差から有限基底測定分布への伝播を同じ誤差台帳で接続することである。

# Schrödinger 型包絡と有限時間誤差

> **位置づけ：** 厳密正常モード生成子、目標演算子との作用素誤差上界、局所包絡の有限時間状態誤差、局所作用変動の上界は厳密に評価できる。Schrödinger 型発展は弱結合・弱離調・有限時間の範囲で成立する近似結果である。


## 弱結合パラメータ

第2章の係数対応により $h_0=h_L$ とする。このとき

```math
A
=
\frac{2M_{\rm osc}\omega_0}{\mathcal J_0}h_L
```

であり、厳密正常モード生成子は

```math
h_{\rm ex}
=
\mathcal J_0\omega_0
\left[
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/2}
-I
\right]
```

となる。作用素ノルムによる無次元弱結合パラメータを

```math
\eta
=
\frac{\left\|A\right\|}
{M_{\rm osc}\omega_0^2}
=
\frac{2\left\|h_L\right\|}
{\mathcal J_0\omega_0}
```

とする。以下では $\eta<1$ を仮定する。この十分条件により

```math
I+
\frac{2h_L}{\mathcal J_0\omega_0}
>
0
```

が保証され、ミクロ剛性行列も正定値になる。

## 生成子の作用素誤差

<!-- theorem-start:theorem -->
**定理（正常モード生成子の誤差上界）**
$h_L=h_L^\dagger$、$\eta<1$ とする。このとき

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

```math
X
=
\frac{2h_L}{\mathcal J_0\omega_0}
```

と置くと $\|X\|=\eta$ である。$f(x)=\sqrt{1+x}$ の2階微分は

```math
f''(x)
=
-\frac{1}{4}
\left(1+x\right)^{-3/2}
```

であり、$[-\eta,\eta]$ 上で $|f''(x)|\leq[4(1-\eta)^{3/2}]^{-1}$ である。実対称 $h_L$ を対角化して各固有値へ Taylor の剰余評価を適用すると

```math
\left\|
\sqrt{I+X}-I-\frac12X
\right\|
\leq
\frac{\left\|X\right\|^2}
{8\left(1-\eta\right)^{3/2}}
```

を得る。$\mathcal J_0\omega_0$ を掛ければ結論が従う。
<!-- theorem-end:proof -->

主項は

```math
h_{\rm ex}
=
h_L
-
\frac{h_L^2}{2\mathcal J_0\omega_0}
+
O
\left(
\frac{\left\|h_L\right\|^3}
{\mathcal J_0^2\omega_0^2}
\right)
```

である。補正 $h_L^2$ は一般に元のグラフより長距離の結合を含む。これは、厳密正常モード生成子が局所目標演算子と一致せず、局所性が弱結合近似として回復することを示す。

## 厳密包絡の有限時間誤差

同じ初期値 $\widetilde b(0)$ から始める厳密解と目標有効解を

```math
\widetilde b(t)
=
e^{-ih_{\rm ex}t/\mathcal J_0}
\widetilde b(0),
```

```math
\widetilde b_L(t)
=
e^{-ih_Lt/\mathcal J_0}
\widetilde b(0)
```

とする。Duhamel 公式から

```math
\sup_{0\leq t\leq T}
\left\|
\widetilde b(t)-\widetilde b_L(t)
\right\|
\leq
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
\left\|\widetilde b(0)\right\|
```

を得る。自然な有効時間を

```math
T
=
c_T
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とすれば、相対誤差上界は

```math
\frac{c_T\eta}
{4\left(1-\eta\right)^{3/2}}
```

であり、固定 $c_T$ に対して $O(\eta)$ である。誤差は時間に比例して蓄積するため、$T$ を無制限に伸ばせる定理ではない。

## 局所包絡と厳密包絡の差

正定値行列

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2}
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

を定め、

```math
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

とする。付録Aの Bogoliubov 型正準変換は

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)}
```

である。逆変換も同じ $U_s,V_s$ を使う。

```math
\delta_{\rm loc}(\eta)
=
\left(1-\eta\right)^{-1/4}-1
```

と置くと、全時刻で

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}(\eta)
\left\|\widetilde b(0)\right\|
```

が成立する。$\delta_{\rm loc}=O(\eta)$ である。厳密だが非局所な包絡と、局所だが反回転項を持つ包絡の差を、この量で制御する。

## 局所包絡の Schrödinger 型近似

実際の局所初期値 $b(0)$ から始める目標解を

```math
b_L(t)
=
e^{-ih_Lt/\mathcal J_0}b(0)
```

とする。

<!-- theorem-start:theorem -->
**定理（局所包絡の有限時間近似）**
$\eta<1$ とする。第2章のミクロ解から作る局所包絡 $b(t)$ は

```math
\sup_{0\leq t\leq T}
\left\|
b(t)-b_L(t)
\right\|
\leq
\varepsilon_{\rm car}(T)
\left\|\widetilde b(0)\right\|
```

を満たす。ここで

```math
\varepsilon_{\rm car}(T)
=
2\delta_{\rm loc}(\eta)
+
\frac{
T\left\|h_L\right\|^2
}{
2\mathcal J_0^2\omega_0
\left(1-\eta\right)^{3/2}
}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$b(t)$ と $\widetilde b(t)$ の変換差、$\widetilde b(t)$ と同じ初期値を持つ有効解の生成子差、初期時刻での $b(0)$ と $\widetilde b(0)$ の変換差に三角不等式を適用する。中間の有効発展はユニタリなので初期差のノルムを保存する。前2節の上界を代入すれば結論が従う。
<!-- theorem-end:proof -->

自然時間 $T=O(\mathcal J_0/\|h_L\|)$ では $\varepsilon_{\rm car}=O(\eta)$ である。本稿で「局所古典振動子網から Schrödinger 型発展を導く」とは、この有限時間近似定理を意味する。

## 局所作用の変動

厳密包絡作用を

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
```

とする。これは保存される。局所作用との相対差は

```math
\left|
\frac{I_{\rm loc}(t)}{I_{\rm ex}}-1
\right|
\leq
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
```

である。従って局所作用は弱結合領域で $O(\eta)$ だけ振動し得る。局所作用を厳密保存量とする旧記述は、有効層内部の近似としてのみ維持する。

## 干渉と節

有効模型内で入力1モードを等分岐し、2経路に位相 $\phi_1,\phi_2$ を蓄積して再結合すると

```math
\chi_+
=
\frac{e^{i\phi_1}+e^{i\phi_2}}{2},
\qquad
\chi_-
=
\frac{e^{i\phi_1}-e^{i\phi_2}}{2}
```

となり、

```math
p_+
=
\cos^2
\left(
\frac{\phi_1-\phi_2}{2}
\right),
\qquad
p_-
=
\sin^2
\left(
\frac{\phi_1-\phi_2}{2}
\right)
```

を得る。理想暗出力は $\phi_1-\phi_2=\pi$ で零になる。

ミクロ局所包絡では、反回転項と正常モード補正により出力方向が $O(\eta)$ だけずれる。暗出力確率の誤差は振幅誤差の2乗だけとは限らない。規格化と任意有限基底測定を含む安全な上界は、第5章で全変動距離として与える。

## 数値検算

8振動子の1次元鎖に弱い調和型離調を加え、固定目標 $h_L$ に対して $\omega_0$ を変えた。初期局所包絡は乱数種 `20260809` の複素ベクトルを規格化し、観測時刻を

```math
T
=
\frac{\mathcal J_0}{\left\|h_L\right\|}
```

とした。作用素誤差は $\|h_{\rm ex}-h_L\|$、局所状態誤差は $\|b(T)-b_L(T)\|$ である。

| $\omega_0$ | $\eta$ | 作用素誤差 | 局所状態誤差 | 規格化状態の距離 |
|---:|---:|---:|---:|---:|
| 20 | 0.1793 | 0.07391 | 0.03045 | 0.02890 |
| 40 | 0.08967 | 0.03849 | 0.01928 | 0.01690 |
| 80 | 0.04483 | 0.01966 | 0.01078 | 0.00959 |

全例で作用素上界、厳密包絡の状態上界、局所包絡の状態上界、局所作用変動上界を満たした。$\omega_0=40$ から80への倍増で作用素誤差は1.96分の1、局所状態誤差は1.79分の1になり、弱結合極限での $O(\eta)$ 収束と整合する。この表は `tools/verify_envelope_reduction.py` から再現できる。

## Q9の達成判定

本稿の固定されたQ9達成基準は、局所位置結合振動子網から空間格子上の Schrödinger 型時間発展を、近似範囲と誤差を伴って導くことである。本章は次を与えた。

1. 有限個の実古典振動子からなる局所位置結合 Hamiltonian 。
2. 反回転項を含む局所包絡の厳密方程式。
3. 厳密正常モード包絡と生成子 $h_{\rm ex}$。
4. 目標実対称 $h_L$ との係数対応。
5. 弱結合・弱離調・有限時間の作用素誤差と状態誤差。
6. 再現可能な数値検算。

従って、Q9はこの限定された有限実対称模型について達成と判定する。これは量子力学の必然的創発を示す結果ではなく、局所古典振動子網における制御された Schrödinger 型有効力学である。

## Q9を超えて残る一般化

次はQ9の固定達成基準を超える一般化であり、本章の結論に含めない。

1. $\mathcal J_0$ と有効質量 $m$ の普遍的な値の導出。
2. 一般の複素 Hermitian 演算子と磁場結合。
3. 時間依存駆動に対する一様な非共鳴定理。
4. 非線形ミクロ結合に対する閉包。
5. 一般連続極限と境界条件の一様誤差。
6. 粒子の連続軌道、局所検出、位相量子化。
7. Born 則、Bell 統計、唯一結果形成のミクロ導出。

特に最後の3項は、Schrödinger 型包絡が得られただけでは従わない。第4章のM38と第5章のM35で測定装置を別模型として検討する。

# 2モード単一量子ビット型操作・測定・弱開放周期

> **位置づけ：** M35と同じ2モード正準信号担体を使うM38を構成し、Bloch 球、共通位相不変性、任意の $SU(2)$ 操作、自律Rabi 振動、任意軸の2段測定、永久外部記録、内部逆計算、外部セル交換 reset を接続する。Q1は厳密、Q2とQ3は無反応と装置誤差を含む制御された任意精度で達成する。M37との同一ハードウェア化は主張しない。


## M38と主張範囲

本章では、$L=2$ に限定した単一量子ビット型装置M38を構成する。信号担体は2つの実正準対

```math
(Q_1,P_1),
\qquad
(Q_2,P_2)
```

であり、複素正準振幅を

```math
b
=
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix},
\qquad
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}}
```

と定める。全位相作用は

```math
I_{\rm ph}
=
\frac12
\sum_{j=1}^2
\left(
Q_j^2+P_j^2
\right)
=
\mathcal J_0 b^\dagger b
```

である。本章では固定作用面

```math
I_{\rm ph}=\mathcal J_0
```

を使うので、$b^\dagger b=1$ である。

M38は次の3層からなる。

1. 同じ2モード信号担体上の可逆操作層。
2. M35を $L=2$ に特殊化し、独立な2つの選択器を持たせた逐次測定層。
3. 外部記録セル、外部 reset セル、局所作用・角時計を加えた弱開放周期層。

任意の操作、測定軸、初期純粋状態を1つの可変プログラム装置で切り替えるとは主張しない。固定した有限プログラムごとに有限Hamiltonian を構成する。M38の信号担体はM35の測定信号と同じであるが、M37の位置ばね網と同じハードウェアではない。M37はQ9の空間Schrödinger 型包絡、M38はQ1--Q3の最小装置を担う。

## 固定作用面とBloch 球

共通位相変換

```math
b
\longmapsto
e^{i\gamma}b
```

は $I_{\rm ph}$ が生成する正準変換である。本章で使う操作量 $b^\dagger A b$、出力作用 $|(Wb)_s|^2$、比較ポインターはこの変換に不変である。

Bloch ベクトルを

```math
\boldsymbol r
=
b^\dagger\boldsymbol\sigma b
```

と定める。実正準座標では

```math
r_x
=
\frac{Q_1Q_2+P_1P_2}{\mathcal J_0},
```

```math
r_y
=
\frac{Q_1P_2-P_1Q_2}{\mathcal J_0},
```

```math
r_z
=
\frac{
Q_1^2+P_1^2-Q_2^2-P_2^2
}{2\mathcal J_0}
```

となる。

<!-- theorem-start:proposition -->
**命題（固定作用面の共通位相縮約）**
固定作用面 $I_{\rm ph}=\mathcal J_0$ は $S^3$ である。写像 $b\mapsto\boldsymbol r$ は

```math
|\boldsymbol r|=1
```

を満たし、同じBloch ベクトルを持つ2点は共通位相だけ異なる。従って、採用する操作・測定代数に対する有効状態空間は

```math
S^3/U(1)
\simeq
\mathbb{CP}^1
\simeq
S^2
```

である。
<!-- theorem-end:proposition -->

正準Poisson 括弧から

```math
\{b_j,b_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

が従うので、Bloch 成分は

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

を満たす。この縮約は、古典位相空間で共通位相変数が存在しないという主張ではない。採用する操作量と測定量が共通位相を識別しないことを表す。

有限次元量子力学を実Hamiltonian 系として表示できること自体は既知である [34]。本章の追加内容は、この表示をM35型の滑らかな測定、逐次記録、逆計算、外部セル reset へ接続した点にある。

## 任意のSU(2) 操作

任意の実ベクトル $\boldsymbol\Omega$ に対し、信号Hamiltonian を

```math
H_{\boldsymbol\Omega}
=
\frac{\mathcal J_0}{2}
b^\dagger
\left(
\boldsymbol\Omega\cdot\boldsymbol\sigma
\right)b
```

と置く。Hamilton方程式は

```math
i\dot b
=
\frac12
\left(
\boldsymbol\Omega\cdot\boldsymbol\sigma
\right)b,
```

```math
\dot{\boldsymbol r}
=
\boldsymbol\Omega\times\boldsymbol r
```

となる。全位相作用は厳密に保存される。

M35で使う局所位相回転と2モード交換の生成子は

```math
G_{Z,j}
=
\frac{Q_j^2+P_j^2}{2},
```

```math
G_X
=
Q_1Q_2+P_1P_2
```

である。前者の相対位相回転と後者の交換回転を有限回合成すれば、Euler 分解

```math
U
=
e^{-i\alpha\sigma_z/2}
e^{-i\beta\sigma_x/2}
e^{-i\gamma\sigma_z/2}
```

により任意の $U\in SU(2)$ を同じ2モード担体上で厳密に実装できる。

<!-- theorem-start:theorem -->
**定理（2モード正準担体上の任意のSU(2)）**
任意の $U\in SU(2)$ に対し、$G_{Z,1}$、$G_{Z,2}$、$G_X$ の有限パルス列が存在し、その信号部分の正準写像は $b\mapsto Ub$ と一致する。各パルスは $I_{\rm ph}$ を保存し、逆操作はパルス順序と符号を反転して得られる。
<!-- theorem-end:theorem -->

これは固定された操作ごとの構成である。全ての $U$ を1本のエルゴード周期が自動的に列挙すること、位置ばねだけで $G_X$ を厳密に実装することは含まない。

## 自律Rabi 振動

駆動用の作用・角変数を $(J_d,\tau_d)$ とし、次の自律Hamiltonian を置く。

```math
H_{\rm Rabi}
=
\omega_dJ_d
+
\frac{\omega_q}{4}
\left(
Q_1^2+P_1^2-Q_2^2-P_2^2
\right)
```

```math
\quad
+
\frac{\Omega}{2}
\left[
\cos\tau_d
\left(
Q_1Q_2+P_1P_2
\right)
+
\sin\tau_d
\left(
Q_1P_2-P_1Q_2
\right)
\right].
```

$H_{\rm Rabi}$ は時計を含む有限自由度の時間非依存Hamiltonian である。相互作用は $J_d$ に依存しないので

```math
\dot\tau_d=\omega_d
```

が厳密に成立する。$b=e^{-i\tau_d\sigma_z/2}c$ と置くと、回転座標では

```math
i\dot c
=
\frac12
\left(
\Delta\sigma_z+\Omega\sigma_x
\right)c,
\qquad
\Delta=\omega_q-\omega_d
```

となる。

<!-- theorem-start:proposition -->
**命題（自律2モードRabi 公式）**
初期状態を $b(0)=e_1$ とする。第2モードへの作用比は

```math
P_{1\to2}(t)
=
\frac{\Omega^2}{\Omega^2+\Delta^2}
\sin^2
\left(
\frac{\sqrt{\Omega^2+\Delta^2}}{2}t
\right)
```

である。従って共鳴時の完全振動、一般離調での振動数、駆動強度依存性、離調による振幅低下が同じ有限自律Hamiltonian から厳密に従う。
<!-- theorem-end:proposition -->

このRabi 模型はM38の $QQ+PP$ と交差位置・運動量結合を使う。M37の時間依存位置ばね近似、反回転補正、Bloch--Siegert型補正はQ1の達成条件に使わない。

## 任意の Bloch 軸の測定

測定軸を単位ベクトル $\boldsymbol n$、結果を $s\in\{+1,-1\}$ とする。射影成分を

```math
P_s(\boldsymbol n)
=
\frac{
I+s\boldsymbol n\cdot\boldsymbol\sigma
}{2}
```

と定める。$W_{\boldsymbol n}\in SU(2)$ を

```math
W_{\boldsymbol n}
|\boldsymbol n,s\rangle
=
e_s
```

となるように選ぶ。第5章のM35作用選択器を $L=2$ に特殊化すると、2つの出力作用比は

```math
p_s(\boldsymbol n)
=
\left|
\langle\boldsymbol n,s|b\rangle
\right|^2
=
\frac{
1+s\boldsymbol n\cdot\boldsymbol r
}{2}
```

となる。

有限幅比較では、作動結果 $+1$、$-1$ と無反応 $\varnothing$ を完全結果集合とする。入力換算有効半幅を $w_{{\rm eff},j}$、角切断接続領域のHaar 質量を $\varepsilon_{{\rm cut},j}$ とすると、測定段 $j$ の無反応率は

```math
\delta_j
\leq
2\frac{w_{{\rm eff},j}}{\mathcal J_0}
+
\varepsilon_{{\rm cut},j}
```

で抑えられる。安全結果 $s$ では正準SWAP 後の信号は厳密に $|\boldsymbol n,s\rangle$ となり、測定前情報はテンプレートへ退避する。無反応試行を除外して2値分布を再規格化しない。

## 滑らかな厳密2値測定の連続性障害

滑らかな有限時間Hamiltonian 流は初期値に連続に依存する。この事実は、有限幅比較器で無反応領域を残す理由を与える。

<!-- theorem-start:theorem -->
**定理（連結入力に対する厳密2値像の障害）**
連結な初期領域 $X$ と、滑らかな有限時間Hamiltonian 流から得る連続写像 $F:X\to Y$ を考える。出力信号が全入力について相異なる2点 $y_+$、$y_-$ のいずれかだけを取り、両方が実現されると仮定すると矛盾する。
<!-- theorem-end:theorem -->

連続像 $F(X)$ は連結であるが、$\{y_+,y_-\}$ の2点集合で両点を含む部分集合は連結でない。従って、次の4条件は同時には成立しない。

1. 滑らかな有限時間Hamiltonian 流。
2. 連結な選択器入力領域。
3. 無反応または遷移領域がないこと。
4. 全入力を2つの異なる固有状態だけへ写すこと。

M38は安全セクターで厳密な固有状態を作り、その間を正式な無反応結果とする。無反応率を任意に小さくできるが、有限資源で厳密に零とはしない。

## 同軸反復測定

第1測定の軸を $\boldsymbol n$ とし、安全結果 $s$ が得られたとする。信号は厳密に $|\boldsymbol n,s\rangle$ である。新しい空テンプレートと独立選択器を持つ第2測定段も同じ軸に設定すれば、理想作用比は

```math
p_t
=
\delta_{ts}
```

となる。

有限幅でも反対符号の安全結果は生じない。第2段の結果は同じ符号または無反応であり、

```math
P_{\rm safe}(-s\mid s)=0,
\qquad
P(\varnothing\mid s)\leq\delta_2
```

である。ここでも無反応を除く条件付き確率だけを表示して反復性を主張しない。

## 異軸逐次測定

第1軸を $\boldsymbol n$、第2軸を $\boldsymbol m$ とする。第1段の安全結果 $s$ の後、信号は $|\boldsymbol n,s\rangle$ なので、第2段の理想条件付き重みは

```math
P(t\mid s)
=
\left|
\langle\boldsymbol m,t|\boldsymbol n,s\rangle
\right|^2
=
\frac{
1+st\boldsymbol n\cdot\boldsymbol m
}{2}.
```

従って理想共同分布は

```math
\pi_{st}
=
\frac{
1+s\boldsymbol n\cdot\boldsymbol r
}{2}
\frac{
1+st\boldsymbol n\cdot\boldsymbol m
}{2}.
```

2段の選択器角を $(\vartheta_1,\vartheta_2)$ とし、周期末に

```math
(\vartheta_1,\vartheta_2)
\longmapsto
(\vartheta_1+2\pi\alpha_1,
\vartheta_2+2\pi\alpha_2)
\pmod{2\pi}
```

と進める。$1,\alpha_1,\alpha_2$ が有理数体上で1次独立なら、この平行移動は2次元トーラス上で一意エルゴード的であり、Haar 測度は積測度になる。

<!-- theorem-start:theorem -->
**定理（2選択器による異軸逐次測定）**
固定純粋入力、固定軸 $\boldsymbol n,\boldsymbol m$、独立な2つの選択器、互いに重ならない時計窓を仮定する。零幅極限の長期共同頻度は $\pi_{st}$ に一致する。有限幅では結果空間を $\{+1,-1,\varnothing\}^2$ とし、理想分布を無反応成分0で拡張すれば、実分布 $p^{(2)}$ は

```math
D_{\rm TV}
\left(
p^{(2)},\pi
\right)
\leq
\delta_1+\delta_2
```

を満たす。
<!-- theorem-end:theorem -->

同じ選択器角を2段で再利用すると、第1結果で条件付けた後の第2角の一様性が一般に失われるため採用しない。一意エルゴード性は長期頻度を与えるが、結果列の独立同分布性や二項分布型有限標本揺らぎは与えない。

## 外部記録への正準コピー

各測定段の滑らかな比較ポインターと角切断指標から、結果コード $\Pi_j(z)$ を作る。$\Pi_j$ は安全な正結果で $+1$、安全な負結果で $-1$、比較遷移域または角切断接続域からなる無反応領域で $(-1,1)$ の値を取る滑らかな関数とする。外部記録セル $(Q_j^R,P_j^R)$ への記録生成子を

```math
G_{\rm rec}
=
\sum_{j=1}^2
P_j^R\Pi_j(z)
```

とする。理想空記録セル $Q_j^R=P_j^R=0$ から単位面積パルスを作用させると

```math
Q_j^R
\longmapsto
Q_j^R+\Pi_j(z),
\qquad
P_j^R
\longmapsto
P_j^R
```

となる。$P_j^R=0$ なので、記録窓中の装置変数 $z$ への反作用は零である。有限な $P_j^R$ 準備誤差は記録反作用として誤差台帳へ入れる。

記録後は、$Q_j^R$ が正安全域、負安全域、中間域のどこにあるかをそれぞれ $+1$、$-1$、無反応として読む。不連続な離散ラベルをHamiltonian で直接コピーせず、滑らかな比較ポインターをコピーするため、前節の連続性障害を再導入しない。

## 内部逆計算と外部セル reset

第2測定、第1測定の順に前向き操作を逆実行する。装置内部状態を $z$、結果 $y$ の記録値を $R_y$ と略記すると、理想写像は

```math
(z_0,0_R)
\longmapsto
(z_y,0_R)
\longmapsto
(z_y,R_y)
\longmapsto
(z_0,R_y)
```

となる。装置は準備状態へ戻り、外部記録は残る。全写像は正準的で1対1であり、結果情報を消去せず外部セルへ移している。

有限誤差と長期運転のため、装置の準備値からの偏差モードを $\delta a_j$、毎周期流入する外部空モードを $\eta_{n,j}$ とする。固定並進後の複素正準座標で、交換生成子を

```math
G_{\rm rst}
=
i\mathcal J_0
\sum_j
\left(
\delta a_j^*\eta_{n,j}
-
\eta_{n,j}^*\delta a_j
\right)
```

とする。交換角を $\phi$ とすると

```math
\delta a_j^+
=
\cos\phi\,\delta a_j^-
+
\sin\phi\,\eta_{n,j},
```

```math
\eta_{n,j}^+
=
-\sin\phi\,\delta a_j^-
+
\cos\phi\,\eta_{n,j}
```

である。$\phi=\pi/2$ では完全交換、$0<|\cos\phi|<1$ では装置偏差の収縮になる。旧装置状態は使用済み外部モードへ移り、Hamiltonian 可逆性は失われない。

1周期の内部逆計算残差を $\varepsilon_{\rm cyc}$、流入セル幅を $\|\eta_n\|\leq\sigma_E$ とすると、

```math
\limsup_{n\to\infty}
\|\delta a_n\|
\leq
\frac{
\varepsilon_{\rm cyc}
+
|\sin\phi|\sigma_E
}{
1-|\cos\phi|
}
```

を得る。結合強度を $g$ とすれば交換時間は

```math
T_{\rm rst}
=
\frac{\phi}{g}
```

である。弱い結合でも接触時間を長くすれば完全交換へ到達できる。本稿で「弱開放」と呼ぶのは結合強度または単位時間当たり交換が弱いという意味であり、1周期のreset 効果が必ず微小という意味ではない。

## 局所時計と資源

全ての操作を1つの作用・角時計 $(J_c,\tau_c)$ で自律化する。互いに重ならない時計窓を $g_r(\tau_c)$、各局所生成子を $G_r$ とし、

```math
H_{\rm cyc}
=
\Omega_cJ_c
+
\Omega_c
\sum_r
g_r(\tau_c)G_r
```

と置く。各窓は

```math
\int g_r(\tau_c)\,d\tau_c=1
```

に規格化する。$\dot\tau_c=\Omega_c$ なので、各生成子の流れが単位パルス面積で実行される。窓が重ならず、各 $G_r$ が自身の流れで保存される理想構成では

```math
\Delta J_c
=
-\int g_r'(\tau_c)G_r\,d\tau_c
=0
```

であり、時計作用も各窓後に戻る。$J_c$ に十分な正の余裕を持たせれば、周期中も正作用領域に保てる。

M35の正準対数は $3L+4$ なので、$L=2$ の1段測定は10正準対である。2段装置で信号2対と時計1対だけを共有する単純上界は

```math
2+2\times7+1=17
```

正準対である。2つの外部記録セルは1周期当たり2対を使う。信号、テンプレート、作用・閾値・内部記録を全て外部空モードと交換する保守的上界は1周期当たり14対である。選択器2対は無理数平行移動を続け、時計1対は周期運動を続けるので、この14対には含めない。

$N$ 周期を完全な有限閉鎖Hamiltonian 系へ埋め込む単純上界は、輸送自由度を除いて

```math
17+16N
```

正準対である。能動装置の大きさは一定だが、永久記録と使用済みreset 状態の保存量は $O(N)$ で増える。無期限運転だけが外部からのセル供給と使用済みセルの流出を必要とする。

$L=2$ の能動装置は1つの局所セル内へ置けるため、一般有限 $L$ で残る長距離時計配線問題は生じない。有限なパルス面積誤差、時計窓の重なり、外部セルの有限準備幅は最終誤差へ加える。

## 完全周期定理と達成判定

2段測定の前向き順序は、準備、任意の $SU(2)$ 操作、第1測定、第2測定、増幅、外部記録である。その後に第2測定、第1測定、準備回路を逆計算し、最後に外部空モード交換を行う。

<!-- theorem-start:theorem -->
**定理（2モード弱開放完全操作・測定周期）**
固定純粋入力、固定された有限 $SU(2)$ 操作列、固定された2つのBloch 軸、任意の $\epsilon>0$ に対し、有限個の正準自由度からなる能動装置と外部記録・reset セル流路を構成できる。安全結果の測定後信号は厳密な対応固有状態である。無反応を含む2段結果分布と理想逐次射影分布の全変動距離、記録誤差、周期末準備集合からの偏差を全て $\epsilon$ 未満に選べる。全系の写像は正準的で1対1であり、装置は次周期の準備集合へ戻り、結果履歴と旧装置偏差は外部流へ残る。
<!-- theorem-end:theorem -->

理想Poincaré 写像は

```math
(z_*,\vartheta_1,\vartheta_2)
\longmapsto
\left(
z_*,
\vartheta_1+2\pi\alpha_1,
\vartheta_2+2\pi\alpha_2
\right)
```

である。誤差は、正準状態誤差、状態方向誤差、比較境界移動量、結果分布の全変動距離の順に変換して評価する。異なる単位の誤差を直接加えない。

以上により、Q1はBloch 球、共通位相不変性、任意の $SU(2)$、Rabi 振動を厳密に満たす。Q2は任意軸、排他的安全結果、測定後固有状態、同軸反復、異軸逐次測定を制御された任意精度で満たす。Q3は永久外部記録、内部逆計算、弱開放 reset、次周期復帰を制御された任意精度で満たす。

Q1--Q3の達成は、M38内部の固定純粋入力・固定有限プログラムに限る。次は含まない。

1. M37とM38の同一ハードウェア化。
2. 一般有限 $L$ の2段完全周期。
3. 可変プログラム全体の統一エルゴード測度。
4. 独立同分布または二項分布型有限標本揺らぎ。
5. 有限閉鎖系の固定容量で永久記録を無期限に蓄積すること。
6. 無反応なしの厳密2値測定。
7. reset の熱力学的最小仕事または総エネルギー収支。

これらはQ1--Q3を別の未確立仮説へ移したものではない。M38の達成範囲を超える一般化、資源評価、M0への統合課題である。

# 滑らかな局所有限基底測定周期

> **位置づけ：** M35について、固定純粋準備・固定有限基底・一般有限Lの局所基底回路、滑らかな比較、無反応結果、測定後状態、内部逆計算、無理数回転Poincaré 写像を構成する。M38で閉じたL=2のQ1--Q3と分離し、一般有限Lの外部記録、弱開放 reset、逐次基底一般化はQ5へ残す。


## 一般作用区間公式

$L$ 個の位相担体モードを $b\in\mathbb C^L$ とする。測定する有限直交基底を $\{|u_k\rangle\}_{k=1}^L$ とし、これを標準基底へ移すユニタリ正準混合 $W$ を

```math
W|u_k\rangle
=
e_k
```

で定める。出力モードの作用と全位相作用は

```math
I_k
=
\mathcal J_0
\left|
\left(Wb\right)_k
\right|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^L I_k
```

である。累積作用を

```math
S_0=0,
\qquad
S_k
=
\sum_{j=1}^kI_j
```

とする。選択器角 $\vartheta\in[0,2\pi)$ から

```math
u
=
\frac{\vartheta}{2\pi}
I_{\rm ph}
```

を作り、$S_{k-1}\leq u<S_k$ を結果 $k$ とする。境界を除けば結果区間は互いに素で全区間を覆うため、各試行で結果は唯一である。

<!-- theorem-start:theorem -->
**定理（一般作用区間公式）**
選択器角が $(b,W,\mathcal P)$ の下で条件付き一様であり、比較失敗または記録失敗を結果依存に除外しないとする。このとき

```math
P(k\mid b,W)
=
\frac{I_k}{I_{\rm ph}}
```

であり、集団平均は

```math
P(k\mid W,\mathcal P)
=
\mathbb E
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
W,\mathcal P
\right]
```

となる。
<!-- theorem-end:theorem -->

この定理は階数1を要求しない。固定作用下の高階数公式、全作用変動の共分散補正、相関行列との関係は付録Bにまとめる。本章の自律周期定理は、1本の軌道上の固定純粋準備に限定する。

## 固定純粋準備と必要自由度

準備状態を

```math
\chi\in\mathbb C^L,
\qquad
\chi^\dagger\chi=1
```

とし、全作用を $I_{\rm ph}=\mathcal J_0$ に固定する。信号 $b$ に加え、同じ $L$ モードのテンプレート $t$ を置く。周期開始時は

```math
b=e_1,
\qquad
t=e_1
```

とする。

作用読出し用に $L$ 個の正準対 $(Q_k,P_k)$、閾値用に $(Q_U,P_U)$、内部結果記録用に $(Q_M,P_M)$、選択器に $(\vartheta,J_{\rm sel})$、時計に $(\tau,P_\tau)$ を用いる。従って明示構成の正準対数は

```math
L+L+L+1+1+1+1
=
3L+4
```

である。作用レジスターのうち $Q_1,\ldots,Q_{L-1}$ は、読出し後に累積比較ポインターとして再利用する。これは最小数の主張ではない。

## Q9包絡から Born 型分布への誤差伝播

第3章のミクロ局所包絡を測定時刻 $T$ で規格化し、

```math
\widehat b_{\rm mic}(T)
=
\frac{b(T)}{\left\|b(T)\right\|}
```

とする。目標有効状態を

```math
\chi_L(T)
=
\frac{b_L(T)}{\left\|b_L(T)\right\|}
```

とする。任意の有限基底変換 $W$ に対し、実際の作用比と目標 Born 型重みを

```math
p_k^{\rm mic}
=
\left|
\left(W\widehat b_{\rm mic}\right)_k
\right|^2,
\qquad
p_k^L
=
\left|
\left(W\chi_L\right)_k
\right|^2
```

と定める。

<!-- theorem-start:proposition -->
**命題（包絡方向誤差から測定分布誤差への伝播）**
任意のユニタリ $W$ について、全変動距離は

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\left\langle
\widehat b_{\rm mic},
\chi_L
\right\rangle
\right|^2
}
\leq
\left\|
\widehat b_{\rm mic}-\chi_L
\right\|
```

を満たす。
<!-- theorem-end:proposition -->

最初の不等式は純粋状態間の距離が任意の射影成分分布の全変動距離を上から抑えること、2番目は単位ベクトルのノルム評価から従う。ここでは量子測定を仮定していない。左辺は古典作用比を同じ基底 $W$ で比較した量である。

第3章の有限時間上界と $\delta_{\rm loc}<1$ を使うと、

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\varepsilon_{\rm dist}(T),
```

```math
\varepsilon_{\rm dist}(T)
=
\min
\left\{
1,
\frac{
2\varepsilon_{\rm car}(T)
}{
1-\delta_{\rm loc}(\eta)
}
\right\}
```

を得る。$\varepsilon_{\rm dist}$ は包絡方向のずれが測定分布へ伝わる誤差であり、環境誤差ではない。

本章の自律周期は $I_{\rm ph}=\mathcal J_0$ の固定準備を使う。Q9から直接渡す単発入力で全局所作用が変動する場合は、測定時点の実際の $I_{\rm ph}(T)$ を読み、閾値も同じ値で規格化する必要がある。この受渡しを同じ局所反復装置へ組み込む問題は、一般有限 $L$ のQ5、および空間局所検出へ接続するQ13に残す。$L=2$ の完全周期は第4章のM38で独立に扱う。

## 任意有限基底の局所正準回路

信号モードの実正準座標を $(Q_j^b,P_j^b)$ とする。単一モード位相回転と隣接2モード交換の生成子を

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

とする。複素振幅では $G_{Z,j}=\mathcal J_0|b_j|^2$、$G_{X,j}=\mathcal J_0(b_j^*b_{j+1}+b_{j+1}^*b_j)$ である。両者の流れは全作用を厳密に保存する。

$G_{Z,j}-G_{Z,j+1}$ と $G_{X,j}$ の交換子方向は、隣接モード間の虚交換生成子を与える。従って局所位相回転と実交換の有限列で任意の隣接 $U(2)$ 変換を作れる。

任意の $W\in U(L)$ には、隣接する2行だけに作用する Givens 変換を順に左から掛ける消去法を適用できる。下三角成分を下から消去すると、

```math
N_W
\leq
\frac{L(L-1)}2
```

個の隣接2モード変換と最後の対角位相へ分解できる [38,39]。固定状態だけを準備する $U_{\rm prep}e_1=\chi$ は $L-1$ 個以下の隣接2モード変換で足りる。逆変換は順序を逆にし、各回転角を反転すれば厳密に得られる。

この回路は、1次元鎖の $L-1$ 本の交換辺を時計順に再利用する。密な $W$ の情報は非局所結合本数ではなく、$O(L^2)$ 個の時計窓と回転角に保存される。互いに重ならない辺を並列化する Clements 型配置では、基底変換の直列深さを $O(L)$ に整理できる [39]。

ただし $G_{X,j}$ は位置間結合だけでなく運動量間結合を含む。これは明示的な有限古典 Hamiltonian だが、M37の通常の位置ばね網と同じハードウェアではない。位置ばねだけに限定すると反回転項を伴う近似になるため、本章では採用しない。

## 作用読出しと累積比較ポインター

局所回路により $b=W\chi$ を作った後、各モード作用を

```math
I_k
=
\mathcal J_0|b_k|^2
```

とする。固定準備では $\sum_kI_k=\mathcal J_0$ である。読出し生成子を

```math
G_{\rm read}
=
\sum_{k=1}^L P_kI_k
+
P_U\mathcal J_0f(\vartheta)
```

とする。角の切断近傍を除き $f(\vartheta)=\vartheta/(2\pi)$ とする。全レジスター運動量を0から始めると、単位面積流の後に

```math
Q_k=I_k,
\qquad
Q_U=u
```

となり、入口信号と選択器への読出し反作用は零である。$P_UI_{\rm ph}f(\vartheta)$ を使わず、既知の $\mathcal J_0$ を使うため、固定準備周期では閾値レジスターを全信号モードへ結合しない。

次に局所剪断を

```math
G_{0}^{\rm cum}
=
-P_1Q_U,
```

```math
G_j^{\rm cum}
=
P_{j+1}Q_j,
\qquad
j=1,\ldots,L-2
```

の順に作用させる。すると

```math
Q_j
=
S_j-u
=:
d_j,
\qquad
j=1,\ldots,L-1
```

となる。作用が非負なので

```math
d_1
\leq
d_2
\leq
\cdots
\leq
d_{L-1}
```

である。入口で共役運動量が0なので、剪断は読出した値を壊さない。

有限保持窓の比較余裕を作るため、

```math
G_{\rm amp}
=
\Lambda
\sum_{j=1}^{L-1}Q_jP_j
```

を作用させる。流れは

```math
Q_j
\longmapsto
e^\Lambda d_j,
\qquad
P_j
\longmapsto
e^{-\Lambda}P_j
```

であり、符号と正準性を保存する。これは吸引的なラッチではなく、有限時間の双曲型増幅である。

## 滑らかな比較と完全結果集合

平坦部を持つ滑らかな段差関数を

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
\frac{
\rho(z+1)
}{
\rho(z+1)+\rho(1-z)
}
```

と定める。出力比較幅を $X>0$ とし、

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

とする。$Q_j$ の単調性から

```math
0
\leq
h_1
\leq
\cdots
\leq
h_{L-1}
\leq
1
```

となる。差

```math
c_k
=
h_k-h_{k-1}
```

は $c_k\geq0$、$\sum_kc_k=1$ を満たす。ただし遷移領域の $c_k$ を実結果または追加確率と解釈しない。

角の切断点を滑らかに接続する領域を $\mathcal C_{\rm cut}$ とする。結果 $k$ の安全セクターを

```math
\mathcal O_k
=
\left\{
\vartheta\notin\mathcal C_{\rm cut},
\qquad
Q_j\leq-X\quad(j<k),
\qquad
Q_j\geq X\quad(j\geq k)
\right\}
```

とする。各 $\mathcal O_k$ は互いに素で、内部では $h_j$ が厳密に0または1となる。残りを正式な無反応結果

```math
\mathcal O_{\varnothing}
=
\left(
\bigcup_{k=1}^L
\mathcal O_k
\right)^c
```

へ含める。従って結果集合は $\{1,\ldots,L,\varnothing\}$ で全入力を覆い、無反応試行を除いて再規格化しない。

入力換算半幅は

```math
w
=
Xe^{-\Lambda}
```

である。選択角の切断接続領域の Haar 質量を $\varepsilon_{\rm cut}$ とすると、

```math
P(\varnothing)
\leq
\min
\left\{
1,
2(L-1)
\frac{w}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
\right\}
```

を得る。安全セクター内部では、境界までの余裕より小さい有限変動に対して結果は変わらない。

## 隣接テンプレート経路と内部記録

隣接テンプレートモードの生成子を

```math
Y_{j,j+1}
=
-i|j\rangle\langle j+1|
+
i|j+1\rangle\langle j|
```

とし、

```math
\ell_j
=
1-h_j
```

と置く。最初に $P_M$ の単位面積流で $Q_M=1$ とし、$j=1,\ldots,L-1$ の順に

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

安全な結果 $k$ では $\ell_j=1$ が $j<k$、$\ell_j=0$ が $j\geq k$ なので、

```math
t:
e_1
\longmapsto
e_2
\longmapsto
\cdots
\longmapsto
e_k,
```

```math
Q_M
=
1+
\sum_{j=1}^{L-1}\ell_j
=
k
```

となる。各経路流で $t^\dagger Y_{j,j+1}t=0$ が保存され、$P_M=0$ なので、比較ポインターの共役運動量への反作用は零である。

無反応領域ではテンプレートと $Q_M$ が中間値を取り得る。$Q_M$ が偶然整数になる遷移点もあるため、結果判定に $Q_M$ 単独を使わず、必ず $\mathcal O_k$ と組み合わせる。

## 正準 SWAP と測定後状態

信号とテンプレートを交換する生成子を

```math
G_{\rm sw}
=
i
\left(
b^\dagger t
-
t^\dagger b
\right)
```

とする。Hamiltonian $\pi\mathcal J_0G_{\rm sw}/2$ を単位面積だけ作用させると、

```math
b\longmapsto t,
\qquad
t\longmapsto-b
```

となる。安全な結果 $k$ では SWAP 直前に $b=W\chi$、$t=e_k$ なので、直後は

```math
b=e_k,
\qquad
t=-W\chi
```

である。信号へ局所回路として実装した $W^\dagger$ を作用させれば、

```math
b_{\rm post}
=
W^\dagger e_k
=
|u_k\rangle
```

となる。測定前情報は消えず、テンプレートへ退避している。無反応では基底状態を主張しない。

<!-- theorem-start:theorem -->
**定理（安全セクターの条件付き測定後状態）**
固定純粋準備 $\chi$、固定基底 $\{|u_k\rangle\}$、安全セクター $\mathcal O_k$ の下で、結果 $k$ の測定直後の信号相関行列は

```math
C_k^{\rm post}
=
|u_k\rangle
\langle u_k|
```

である。無反応を含む無条件相関行列には、無反応領域の中間状態が別項として残る。
<!-- theorem-end:theorem -->

これは全系の非可逆な射影ではない。全系では正準 SWAP であり、信号部分だけを縮約すると測定前情報がテンプレートへ移ったように見える。

## 反復可能性の範囲

安全な結果 $k$ の直後に同じ基底変換を施すと

```math
Wb_{\rm post}
=
e_k
```

なので、新しい空テンプレートを持つ第2装置では同じ結果が確率1で得られる。ただし現在の装置のテンプレートには $-W\chi$ が保持されている。同じ装置をその場で再使用するには、先に内部逆計算を完了するか、別の空テンプレートを用意する必要がある。

## 内部記録保持と完全逆計算

保持窓では、結果を比較ポインターセクター、信号、内部記録から読める。続いて次の順に逆操作する。

1. 信号へ局所回路 $W$ を作用させる。
2. 逆 SWAP を作用させる。
3. 隣接テンプレート経路を逆順・逆角で実行し、$Q_M$ の初期移動を逆にする。
4. 双曲型増幅を逆実行する。
5. 累積剪断を逆順に実行する。
6. 作用・閾値読出しを逆実行する。
7. 信号へ局所回路 $W^\dagger$、$U_{\rm prep}^\dagger$ を作用させる。

前向き写像全体の厳密な逆を使うため、この帰還は無反応領域を含む。周期末には信号、テンプレート、全レジスターとその共役運動量が準備値へ戻る。

この逆計算は永久記録を消しているのではない。途中で作った情報を元の信号・選択器状態へ戻している。周期を越えて保持する外部記録まで同じ有限閉鎖系内で結果非依存の同一点へ戻すことは要求しない。

## 1本の自律 Hamiltonian

時計を

```math
(\tau,P_\tau),
\qquad
\tau\in S^1,
\qquad
H_{\rm clk}=P_\tau
```

とする。互いに重ならない滑らかな時計窓 $g_r(\tau)$ と各局所生成子 $G_r$ を用いて、

```math
H_{\chi,W}^{\rm cyc}
=
P_\tau
+
\sum_{r=1}^{N_{\rm cyc}(L,W)}
g_r(\tau)G_r
```

という1本の有限自律 Hamiltonian にまとめられる。$W$ と $W^\dagger$ の4回の使用は同じ局所回路の順方向・逆方向であり、準備と逆準備も同様である。

最後の生成子を

```math
G_{\rm drift}
=
2\pi\alpha J_{\rm sel},
\qquad
\alpha\notin\mathbb Q
```

とする。各窓の生成子はその窓内で保存され、窓端で $g_r=0$ なので、時計運動量 $P_\tau$ も1周期後に準備値へ戻る。1個の時計変数から空間的に離れた各局所辺へ窓信号を物理的に配る配線は、本章の代数構成には含めず、一般有限 $L$ のQ5に残す。$L=2$ では全能動装置を1つの局所セルへ置く第4章の構成を使う。

## Poincaré 写像と不変測度

Poincaré 断面 $\Sigma_{\chi,W}=\{\tau=0\}$ 内で、信号、テンプレート、全レジスター、全共役運動量、選択器作用、時計運動量を準備値へ固定した集合を $\mathcal T_{\chi,W}$ とする。自由変数は $\vartheta$ だけである。

<!-- theorem-start:theorem -->
**定理（滑らかな固定有限基底周期の不変測度）**
$L<\infty$、$\chi^\dagger\chi=1$、固定基底変換 $W$、互いに重ならない単位面積時計窓、$\alpha\notin\mathbb Q$ を仮定する。前節までの滑らかな局所回路を合成すると、$\mathcal T_{\chi,W}$ 上の Poincaré 写像は

```math
\mathcal R_{\chi,W}:
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi}
```

であり、他の全内部変数を準備値へ戻す。従って

```math
d\mu_{\chi,W}^{\rm cyc}
=
\frac{d\vartheta}{2\pi}
\otimes
\delta_{\rm reset}
```

は不変であり、$\mathcal R_{\chi,W}$ はこの測度に関して一意エルゴード的である。
<!-- theorem-end:theorem -->

滑らか化後も前向き写像と逆向き写像が厳密に打ち消し合うため、不変性とエルゴード性は比較境界を除外せずに成立する。結果の離散性は、安全セクターと無反応セクターからなる粗視化で定義する。

## 無反応込みの Born 型長期頻度

理想分布を

```math
p^{\rm id}
=
\left(
p_1,\ldots,p_L,0
\right),
\qquad
p_k
=
\left|
\langle u_k|\chi\rangle
\right|^2
```

とする。滑らかな周期の長期結果分布を $p^{\rm cyc}$ とする。安全セクターでは理想累積区間と同じ結果になり、失われた作動質量は全て無反応成分へ入る。従って

```math
D_{\rm TV}
\left(
p^{\rm cyc},p^{\rm id}
\right)
=
p^{\rm cyc}_{\varnothing}
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

である。任意の $\epsilon>0$ に対し $\Lambda$ を十分大きくし、角切断幅を十分小さくすれば、右辺を $\epsilon$ 未満にできる。

<!-- theorem-start:theorem -->
**定理（局所滑らか測定周期による Born 型頻度）**
任意の有限 $L$、固定純粋準備 $\chi$、固定有限直交基底 $\{|u_k\rangle\}$、任意の $\epsilon>0$ に対し、$3L+4$ 正準対からなる有限自律 Hamiltonian 周期を構成できる。相互作用は、局所位相回転、隣接2モード交換、局所読出し、隣接剪断、双曲型増幅、隣接テンプレート経路、正準 SWAP からなる。結果集合は $\{1,\ldots,L,\varnothing\}$ であり、各試行の結果は一意である。安全な結果 $k$ では測定後信号が厳密に $|u_k\rangle$ となり、無反応領域を含む全内部変数が周期末に準備値へ戻る。長期結果分布は

```math
D_{\rm TV}
\left(
p^{\rm cyc},
\left(
|\langle u_1|\chi\rangle|^2,
\ldots,
|\langle u_L|\chi\rangle|^2,
0
\right)
\right)
<
\epsilon
```

を満たすように選べる。
<!-- theorem-end:theorem -->

無理数回転は混合的ではない。従って長期平均は Born 型重みに任意精度で一致するが、結果列は独立同分布でなく、二項分布型有限標本揺らぎを一般には再現しない。

Q9からの入力誤差と装置誤差を含めると、安全な和上界は

```math
D_{\rm TV}^{\rm obs}
\leq
\varepsilon_{\rm dist}
+
\varepsilon_{\rm prep}
+
\varepsilon_W
+
\varepsilon_{\rm read}
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm clk}
```

となる。理想局所正準回路では $\varepsilon_W=0$ であり、Q9の出力を直接入力する場合は周期内準備誤差 $\varepsilon_{\rm prep}$ を省ける。

## 空間セル基底と主張の範囲

$W=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応する場合、$\psi_i=\chi_i/\sqrt{\Delta V}$ と定めれば、階数1状態では

```math
p_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。ただし、これは位相担体の空間セル基底を標本化する式である。粒子座標がセル $i$ の局所検出器を作動させること、粒子と選択モードが同期すること、粒子が連続軌道を持つことは別の導出を要する。

本章は、固定純粋準備・固定有限基底・有限次元・任意精度という範囲で、Q5の一般有限 $L$ 測定部分を与える。$L=2$ の任意の Bloch 軸、同軸反復、異軸逐次測定、永久外部記録、弱開放 reset は第4章のM38で閉じる。一般有限 $L$ については、複数段の独立選択器、外部記録・reset セル流、長距離時計配線、完全周期の資源増加が残るため、Q5は部分達成である。一般混合状態を1本の軌道から生成すること、混合的有限標本統計、粒子の局所検出、連続スペクトルも本章の結果に含めない。

# 4成分 Bell 重みと二側履歴測度

> **位置づけ：** 反対称な集団交差相関の4成分重みを一般有限基底作用重みと代数的に比較する。独立な局所 Haar 角から基準セクター密度1/4を導き、二側整合条件の下で Bell 余弦共同確率、設定分布保存、非信号性を得る。集団量を単一試行で読み取る装置は仮定せず、試行ごとの余弦区間生成と整合支持条件の物理的必然性は未導出とする。


## 左右位相担体と反対称交差相関

左右に2モードずつを置き、単一試行の局所モード振幅を $z^{A,\omega},z^{B,\omega}\in\mathbb C^2$ とする。調製条件と Bell プログラムを固定した集団平均として

```math
\Xi
=
\mathbb E
\left[
z^{A,\omega}
\left(z^{B,\omega}\right)^{\mathsf T}
\right]
\in
\mathbb C^{2\times2}
```

を定める。$\Xi$ は集団統計量であり、単一試行の正準変数ではない。反対称源条件を

```math
\Xi_0
=
\sqrt{\frac{\mathcal K}{2}}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
\mathcal K>0
```

とする。$\mathcal K=\operatorname{tr}(\Xi_0\Xi_0^\dagger)$ は集団交差相関の規格化量である。単一試行ごとの保存作用と同一視しない。反対称源集団の反復可能な物理準備は本章の入力条件であり、結論ではない。

行優先ベクトル化を

```math
\operatorname{rvec}\Xi
=
\begin{pmatrix}
\Xi_{++}\\
\Xi_{+-}\\
\Xi_{-+}\\
\Xi_{--}
\end{pmatrix}
```

と定め、規格化4成分ベクトルを

```math
\chi_{\rm B}
=
\frac{\operatorname{rvec}\Xi_0}{\sqrt{\mathcal K}}
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\
1\\
-1\\
0
\end{pmatrix}
```

とする。$\chi_{\rm B}$ は左右の局所担体集団から作る派生交差相関の4次元表示である。独立した非局所実在場または単一試行の4モード粒子状態として追加しない。

## 局所分析器とテンソル積表示

設定 $x,y$ に対応する局所分析器角を $\alpha_x,\beta_y$ とする。平面回転を

```math
R(\gamma)
=
\begin{pmatrix}
\cos\gamma&-\sin\gamma\\
\sin\gamma&\cos\gamma
\end{pmatrix}
```

とする。左右の分析器は

```math
z^A
\longmapsto
R(\alpha_x)z^A,
\qquad
z^B
\longmapsto
R(\beta_y)z^B
```

と局所的に作用する。左右の正準変数は分離しているので、生成子 $G_A,G_B$ は $\{G_A,G_B\}=0$ を満たし、分析器 Hamiltonian は局所和として書ける。

交差相関と4成分表示は

```math
\Xi_{xy}
=
R(\alpha_x)
\Xi_0
R(\beta_y)^{\mathsf T},
```

```math
\chi_{xy}
=
\left[
R(\alpha_x)
\otimes
R(\beta_y)
\right]
\chi_{\rm B}
```

となる。テンソル積表示は、左右の局所正準回転の交差相関への作用をまとめたものである。

## 4成分作用重み

結果対 $A,B\in\{+1,-1\}$ に対応する規格化重みを

```math
w_{AB}^{xy}
=
\left|
\left(\chi_{xy}\right)_{AB}
\right|^2
=
\frac{
\left|
\left(\Xi_{xy}\right)_{AB}
\right|^2
}{
\mathcal K
}
```

とする。直接計算すると

```math
w_{++}^{xy}
=
w_{--}^{xy}
=
\frac12
\sin^2
\left(
\alpha_x-\beta_y
\right),
```

```math
w_{+-}^{xy}
=
w_{-+}^{xy}
=
\frac12
\cos^2
\left(
\alpha_x-\beta_y
\right)
```

である。$\Delta_{xy}=2(\alpha_x-\beta_y)$ とすれば、

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

となる。規格化前の集団重みを

```math
K_{AB}^{xy}
=
\mathcal K
w_{AB}^{xy}
```

とする。

<!-- theorem-start:proposition -->
**命題（Bell 集団重みと4成分作用重みの代数的同型）**
反対称な集団交差相関と左右局所回転の下で、規格化重み $K_{AB}^{xy}/\mathcal K$ は、4成分ベクトル $\chi_{\rm B}$ に局所テンソル積回転を施した成分の絶対値2乗に一致する。従ってBell 余弦集団重みは、第5章の有限基底作用重みと同じ代数構造を持つ。
<!-- theorem-end:proposition -->

この同値は線形代数上の同型であり、単粒子側のテンプレート SWAP 測定器を Bell 装置へ適用したことを意味しない。$\chi_{\rm B}$ と $w_{AB}^{xy}$ は集団相関から計算した量であり、単一試行の Hamiltonian が直接読み取れる正準レジスターではない。Bell では左右の結果が共通未来へ情報が届く前に局所的に形成される必要がある。

## 局所結果生成

A側とB側に固定作用の正準角

```math
\phi_A,\phi_B
\in
[0,2\pi)
```

を置く。理想局所結果を

```math
A_x(\phi_A)
=
\operatorname{sgn}
\cos
\left(
\phi_A-2\alpha_x
\right),
```

```math
B_y(\phi_B)
=
\operatorname{sgn}
\cos
\left(
\phi_B-2\beta_y
\right)
```

とする。零点は零測度境界である。各応答は同じ翼の設定と局所角だけを参照する。A側の式に $y$ はなく、B側の式に $x$ はない。

実装では符号関数を滑らかな有限幅比較へ置き換える。結果の厳密2値化に関する連続性の制限は第4章と同じであり、境界近傍だけを誤差領域とする。

## 制約前基準測度

設定生成器のマクロセクター確率を $\pi_x,\pi_y$ とする。局所結果角と共通未来角 $\theta_F$ を独立な Haar 角とし、制約前基準測度を

```math
d\nu_{\rm B}^0
=
\pi_x\pi_y
\frac{d\phi_A}{2\pi}
\frac{d\phi_B}{2\pi}
\frac{d\theta_F}{2\pi}
```

とする。各局所応答は円周を等しい2つの半円へ分けるので、

```math
\nu_{\rm B}^0
\left(
A
\mid
x
\right)
=
\frac12,
\qquad
\nu_{\rm B}^0
\left(
B
\mid
y
\right)
=
\frac12
```

である。独立性から

```math
q_{AB}^{xy}
:=
\nu_{\rm B}^0
\left(
A,B
\mid
x,y
\right)
=
\frac14
```

を全設定・全結果について得る。最小模型では、基準セクター密度の共通性は仮定でなく局所 Haar 角と半円分割の帰結である。

## 共通未来区間と整合事象

固定した反対称源プログラムについて、4結果を $++,+-,-+,--$ の順に並べ、累積重みを

```math
T_0=0,
\qquad
T_1=w_{++}^{xy},
```

```math
T_2
=
w_{++}^{xy}+w_{+-}^{xy},
\qquad
T_3
=
T_2+w_{-+}^{xy},
\qquad
T_4=1
```

とする。$r_F=\theta_F/(2\pi)$ とし、各結果対の区間 $\mathcal I_{AB}^{xy}\subset[0,1)$ を対応する累積区間とする。その長さは

```math
\left|
\mathcal I_{AB}^{xy}
\right|
=
w_{AB}^{xy}
```

である。区間境界は、反対称源条件と設定角から計算される Bell プログラムのパラメータである。単一試行の $z^{A,\omega},z^{B,\omega}$ から集団相関 $\Xi$ を推定して区間を作るとはしない。

左右で既に記録された結果を $A_x(\phi_A),B_y(\phi_B)$ とする。二側整合事象を

```math
G
=
\left\{
r_F
\in
\mathcal I_{A_x(\phi_A),B_y(\phi_B)}^{xy}
\right\}
```

と定める。未来角は結果を作らない。局所結果を持つ履歴と、プログラムされた集団余弦区間が整合するかだけを制約する。この区間法則をミクロ源と局所装置から試行ごとに生成する機構は未完成である。

## 整合体積と設定分布

固定した $x,y,A,B$ について、局所角の結果セクター体積は $1/4$、未来角区間の体積は $w_{AB}^{xy}$ である。従って

```math
\nu_{\rm B}^0
\left(
A,B,G
\mid
x,y
\right)
=
\frac14
w_{AB}^{xy}
```

となる。全結果について和を取ると、

```math
\nu_{\rm B}^0
\left(
G
\mid
x,y
\right)
=
\frac14
\sum_{A,B}
w_{AB}^{xy}
=
\frac14
```

である。整合事象の総基準体積は設定に依存しない。

## 二側履歴測度と共同確率

物理的履歴を、初期側の準備条件と終端側の整合条件 $G$ の双方を満たす Hamiltonian 軌道として定める。二側履歴測度を

```math
d\mu_{\rm B}
=
4\mathbf1_G
\,d\nu_{\rm B}^0
```

とする。$\nu_{\rm B}^0(G)=1/4$ なので規格化されている。

<!-- theorem-start:theorem -->
**定理（最小 Bell 二側履歴測度）**
反対称源、左右局所回転、独立局所 Haar 角、独立未来 Haar 角、整合支持条件 $G$ を仮定する。このとき

```math
P_{\mu_{\rm B}}
\left(
A,B
\mid
x,y
\right)
=
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

であり、設定分布は

```math
P_{\mu_{\rm B}}(x,y)
=
\pi_x\pi_y
```

のまま保たれる。
<!-- theorem-end:theorem -->

この定理では、局所結果セクター体積 $1/4$ と、集団反対称源から代数的に得た未来区間長 $w_{AB}^{xy}$ の積を二側条件で規格化している。ただし区間長を物理的境界法則として採用するため、共同確率を完全なミクロ装置から無条件に導出した結果ではない。

## 一般基準密度との関係

完全装置では、時計流束、境界面の Jacobian 、付随自由度、解多重度、記録失敗率が結果対に依存する可能性がある。これらをまとめた一般基準密度を $q_{AB}^{xy}$ とすれば、共同確率は

```math
P(A,B\mid x,y,G)
=
\frac{
q_{AB}^{xy}K_{AB}^{xy}
}{
\sum_{A',B'}
q_{A'B'}^{xy}K_{A'B'}^{xy}
}
```

となる。最小模型の $q_{AB}^{xy}=1/4$ を完全模型へ拡張するには、少なくとも次が必要である。

1. 付随測度が局所結果セクターから独立である。
2. 境界面の Jacobian が4結果で共通である。
3. 各結果に対応する Hamiltonian 解の多重度が共通である。
4. 戻り伝播、比較、記録の失敗率が結果依存でない。

従って本章は、最小因子化模型での基準密度を導出するが、一般完全模型での共通性を無条件には主張しない。

## 非信号性と CHSH 値

余弦重みを一側について和を取ると、

```math
\sum_B
w_{AB}^{xy}
=
\frac12,
\qquad
\sum_A
w_{AB}^{xy}
=
\frac12
```

である。従って

```math
P(A\mid x,y)
=
P(A\mid x)
=
\frac12,
```

```math
P(B\mid x,y)
=
P(B\mid y)
=
\frac12
```

となる。測定設定独立性は破れるが、理想対称模型の観測周辺は非信号である。

相関は

```math
E(x,y)
=
-\cos
2
\left(
\alpha_x-\beta_y
\right)
```

である。標準角

```math
\alpha_0=0,
\qquad
\alpha_1=\frac{\pi}{4},
\qquad
\beta_0=\frac{\pi}{8},
\qquad
\beta_1=-\frac{\pi}{8}
```

に対し、

```math
\left|
S_{\rm CHSH}
\right|
=
2\sqrt2
```

を得る。これは反対称4成分状態と平面内2出力に対する値であり、一般 Tsirelson 原理の導出ではない。

## 測定設定独立性

完全ミクロ履歴を

```math
\Lambda
=
\left(
\phi_A,
\phi_B,
\theta_F,
\Lambda_{\rm src},
\ldots
\right)
```

とする。物理測度では

```math
d\mu_{\rm B}
\left(
\Lambda
\mid
x,y
\right)
=
4
\mathbf1_{G_{xy}}(\Lambda)
d\nu_{\rm B}^0(\Lambda)
```

であり、$G_{xy}$ は設定を通じて余弦区間に依存する。従って一般に

```math
\mu_{\rm B}
\left(
d\Lambda
\mid
x,y
\right)
\neq
\mu_{\rm B}
\left(
d\Lambda
\right)
```

である。 Bell の前提違反は測定設定独立性にある。局所応答は $A=A(x,\phi_A)$、$B=B(y,\phi_B)$ のままであり、反対側の設定を引数に持たない。 Bell の定理は正しく、本模型はその前提を満たさない。

設定分布保存は、完全ミクロ履歴の設定独立性を回復しない。観測される $P(x,y)$ が制約前と同じことと、$P(\Lambda\mid x,y)=P(\Lambda)$ は別の条件である。

## 二側境界値問題としての意味

物理順序として確立している部分は、局所分析器、局所結果形成、局所記録、有限速度の情報伝送までである。共通未来では、固定プログラムが設定 $x,y$ に対応する区間 $\mathcal I_{AB}^{xy}$ を参照し、記録済み結果との整合性を判定する条件付き模型を考える。

時刻 $t_0$ の準備面と時刻 $t_F$ の終端面

```math
\mathcal B_F
=
\left\{
r_F
\in
\mathcal I_{AB}^{xy}
\right\}
```

の両方を満たす軌道を解集合とする。Hamiltonian 流を $\Phi_T$ とすれば、許される初期状態は $\Phi_T^{-1}(\mathcal B_F)$ である。最小因子化模型では、Liouville 体積保存と未来角の独立 Haar 密度により、固定結果セクターでの引戻し体積は終端区間体積に比例する。完全模型では、付随測度、境界 Jacobian、解多重度の結果非依存性が別に必要である。

これは終端から過去へ制御力を送る機構ではない。初期条件だけでなく終端条件も満たす全履歴を物理的解とする二側境界値問題である。一方、$G$ を物理法則として課さず、制約前候補を全て前向き生成して $G^c$ を実験後に捨てれば、25%だけを残す事後選別になる。その解釈は採用しない。

重要な未完成点は、$\Xi$ が集団量であるため、単一試行の装置が $\Xi$ を読み取って4区間を作ることはできない点である。本章では反対称源プログラムから解析的な余弦区間を指定する。単一試行の源変数と局所相互作用から同じ区間多重度が自然に生じる有限 Hamiltonian は構成していない。

## 主張の範囲

本章で得たものは次である。

1. Bell 余弦重みと有限 $L=4$ 作用重みの代数的同値。
2. 左右の局所 Hamiltonian によるテンソル積回転。
3. 独立局所 Haar 角と半円分割からの基準セクター密度 $1/4$。
4. 整合事象の総基準体積 $1/4$ と設定独立性。
5. 二側履歴測度の下での Bell 共同確率と設定分布保存。
6. 理想対称条件での非信号性、 CHSH 値、 Bell 前提監査。

一方、次は示していない。

1. 反対称源の反復可能な物理準備。
2. 集団相関 $\Xi$ を使わず、単一試行変数から余弦区間多重度を生成すること。
3. 二側整合支持条件 $G$ の物理的必然性。
4. $\mu_{\rm B}$ を通常の前向き自律 Hamiltonian の Poincaré 不変測度として生成すること。
5. 付随自由度と境界 Jacobian を含む完全模型での基準密度因子化。
6. 外部設定介入に対する統計安定性。
7. 非対称準備または有限比較幅の下での一般非信号条件。
8. 平面内2出力を超える一般複合測定と一般 Tsirelson 原理。

# 誤差、反復周期、性能と資源

> **位置づけ：** M38のQ1--Q3誤差、M37からM35への分布誤差、一般有限基底装置、Bell 二側履歴の性能指標を分離して集計する。Q2とQ3の達成は任意精度を意味し、有限資源での零誤差や総エネルギー最適性を意味しない。量子ゲート型計算機の実装コストを扱うQ8は未着手である。


## 対象範囲

本章は次の4つを同一視せずに集計する。

1. M38の2モード操作、2段測定、外部記録、弱開放 reset 。
2. M37の局所振動子網による空間伝播。
3. M35の一般有限基底内部測定周期。
4. M36の条件付きBell 二側履歴模型。

M38はQ1--Q3を閉じるが、M37との同一ハードウェア化を含まない。M37からM35への接続は、状態方向誤差から有限基底分布誤差への数学的上界であり、同一装置の構成ではない。M0への統合、一般有限 $L$ の完全周期、量子計算機としての規模依存性は別の課題である。

## M38の誤差台帳

M38の理想逐次分布と観測分布の全変動距離を、次の無次元誤差へ分ける。

```math
D_{\rm TV}^{\rm M38}
\leq
\delta_1+\delta_2
+
\varepsilon_{\rm op}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm inv}
+
\varepsilon_{\rm rst}
+
\varepsilon_{\rm port}.
```

| 誤差 | 内容 | 現行評価 |
|---|---|---|
| $\delta_1,\delta_2$ | 2段比較器の無反応質量 | 各段で $2w_{{\rm eff},j}/\mathcal J_0+\varepsilon_{{\rm cut},j}$ 以下 |
| $\varepsilon_{\rm op}$ | $SU(2)$ パルス面積、順序、生成子の実装誤差 | 理想正準回路では0、有限列の和上界 |
| $\varepsilon_{\rm clk}$ | 時計窓面積、重なり、作用帰還誤差 | 非重複理想窓では0 |
| $\varepsilon_{\rm rec}$ | 記録セルの共役運動量幅と読出し幅 | $T_R\sigma_PK_\Pi$ から状態誤差へ換算 |
| $\varepsilon_{\rm inv}$ | 第2段、第1段、準備回路の逆計算残差 | 理想逆回路では0 |
| $\varepsilon_{\rm rst}$ | 外部セル幅と交換角誤差 | 収縮上界で評価 |
| $\varepsilon_{\rm port}$ | 外部セルの流入・流出と接触時間のずれ | 個別実装で評価 |

比較幅の入力換算量は

```math
w_{\rm eff}
=
Xe^{-\Lambda}
+
\Delta_{\rm in}
+
e^{-\Lambda}\Delta_{\rm out}
```

である。増幅前誤差は双曲型増幅で減らない。増幅後の固定出力誤差だけが入力換算で小さくなる。

異なる単位の誤差を表のまま加えない。付録Eの順序に従い、正準状態誤差を状態方向誤差へ、状態方向誤差を比較境界移動量へ、境界移動量をHaar 質量と全変動距離へ変換する。上式の各 $\varepsilon$ は最終的に全変動距離へ換算した後の量である。

## M37からM35への分布誤差

測定時刻の規格化局所包絡を $\widehat b_{\rm mic}$、目標有効状態を $\chi_L$ とする。任意有限基底について

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\langle\widehat b_{\rm mic},\chi_L\rangle
\right|^2
}
```

である。装置誤差を加える場合は

```math
D_{\rm TV}^{\rm M35}
\leq
\varepsilon_{\rm dist}(T)
+
\varepsilon_{\rm prep}
+
\varepsilon_W
+
\varepsilon_{\rm read}
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm clk}
```

とする。

| 誤差 | 内容 | 現行評価 |
|---|---|---|
| $\varepsilon_{\rm dist}$ | M37の局所包絡と目標状態の方向差 | 第3章と第5.3節の解析上界 |
| $\varepsilon_{\rm prep}$ | 初期作用、相対位相、伝播時刻の再現誤差 | 完全準備系で未評価 |
| $\varepsilon_W$ | M35局所基底回路の誤差 | 理想 $QQ+PP$ 回路では0 |
| $\varepsilon_{\rm read}$ | 作用・閾値読出しと累積剪断の誤差 | 理想入口では0 |
| $\varepsilon_{\rm cmp}$ | 滑らかな比較幅 | $2(L-1)w_{\rm eff}/I_{\rm ph}$ 以下 |
| $\varepsilon_{\rm cut}$ | 角切断の接続領域 | 接続幅のHaar 質量 |
| $\varepsilon_{\rm clk}$ | 一般有限 $L$ の時計配線誤差 | 物理配線は未評価 |

第3章の自然時間では $\varepsilon_{\rm dist}=O(\eta)$ である。目標精度を $\epsilon$ とする単純な十分条件は

```math
\omega_0
=
O
\left(
\frac{\|h_L\|}{\mathcal J_0\epsilon}
\right)
```

である。最適性は主張しない。

## M38の資源

M38の単純上界は次である。

| 装置 | 正準対数 |
|---|---:|
| Q1の信号担体 | 2 |
| 自律Rabi 装置 | 3 |
| $L=2$ M35測定1段 | 10 |
| 信号と時計を共有する2段測定器 | 17 |
| 外部記録セル | 2対／周期 |
| 外部 reset セル | 最大14対／周期 |

2段測定器の17対は

```math
2+2\times7+1
```

からなる。共有するのは信号2対と時計1対であり、各段はテンプレート2、作用2、閾値1、内部記録1、選択器1の7対を持つ。

$N$ 周期を有限閉鎖Hamiltonian 系へ埋め込む単純上界は

```math
17+16N
```

正準対である。輸送自由度は含まない。能動装置は一定サイズだが、永久記録と使用済みreset 状態の保存量は $O(N)$ で増える。有限閉鎖系の固定容量で無期限記録を行うとは主張しない。

## 一般有限基底装置の資源

M35の一般有限 $L$ 構成は

```math
N_{\rm pair}^{\rm meas}
=
3L+4
```

正準対を使う。内訳は信号 $L$、テンプレート $L$、作用レジスター $L$、閾値1、内部記録1、選択器1、時計1である。

任意の密な基底変換 $W$ は

```math
N_W
\leq
\frac{L(L-1)}2
```

個の隣接2モード混合と対角位相へ分解できる。逐次Givens 消去の深さは $O(L^2)$、互いに素な辺を並列化する配置では $O(L)$ である。累積剪断とテンプレート経路は $O(L)$ である。

一般有限 $L$ の複数段装置では、独立選択器、テンプレート、外部記録・reset セルの数が段数とともに増える。空間的に離れた各辺への時計配線と伝播遅延も必要になる。Q5の完全周期資源は未評価である。

## 動作時間、作用、エネルギー

M38とM35の各時計窓はパルス面積を指定する。最大結合強度を制限しなければ物理時間を任意に短縮できるので、絶対動作時間の主張にはならない。意味のある評価には最大生成子ノルムまたは最大結合強度を固定する必要がある。

reset 交換の接触時間は

```math
T_{\rm rst}
=
\frac{\phi}{g}
```

である。弱結合では接触時間が長くなる。比較精度を上げると双曲型増幅率 $\Lambda$ とポインター座標範囲が増える。

M37のミクロエネルギーは厳密保存される。M38の各理想正準パルスと外部セル交換も全Hamiltonian 内では可逆である。しかし、準備装置、時計、記録媒体、外部セル輸送、低エントロピーセル供給まで含む総エネルギー収支は計算していない。Landauer 原理を引用するだけでは、具体的なreset の熱・仕事収支にならない [17,18]。

## 反復可能性

反復には3つの意味がある。

1. 安全な測定後信号を新しい第2測定段へ渡す同軸または異軸逐次測定。
2. 外部記録後に内部逆計算し、同じ能動装置で次周期を始めること。
3. 外部記録と使用済みreset セルまで含む全系を結果非依存の同一点へ戻すこと。

M38は1と2を構成する。3はHamiltonian 流の1対1性と両立せず、要求しない。有限 $N$ なら履歴を有限個の外部セルへ保存し、全系を有限閉鎖Hamiltonian として扱える。無期限運転では空セル流入と使用済みセル流出を持つ弱開放系として扱う。

M35の一般有限 $L$ では内部逆計算は構成済みだが、複数段測定と外部セル流は未構成である。

## Bell 側の性能指標

Bell 模型では、共同分布だけでなく次を別々に監査する。

```math
\epsilon_{\rm joint}
=
\max_{x,y}
\frac12
\sum_{A,B}
\left|
P_{\rm obs}(A,B\mid x,y)
-w_{AB}^{xy}
\right|,
```

```math
\epsilon_{\rm ns}^{A}
=
\max_{x,y,y',A}
\left|
P(A\mid x,y)-P(A\mid x,y')
\right|,
```

```math
\epsilon_{\rm ns}^{B}
=
\max_{x,x',y,B}
\left|
P(B\mid x,y)-P(B\mid x',y)
\right|.
```

現行最小模型では非信号誤差が解析的に零である。非対称比較幅、伝送損失、境界Jacobianを含む完全模型の上界は未導出である。設定分布、整合支持質量、結果別基準密度、事後除外率も別に記録する。

## 導出済み部分と残る資源評価

本稿は次を定量化した。

1. M38のBloch 球、$SU(2)$、Rabi 遷移公式。
2. M38の2段無反応率と全変動距離上界。
3. 外部記録剪断の反作用上界、reset 交換の収縮上界。
4. M38の能動正準対数17と外部セル数。
5. M37の作用素誤差、状態誤差、局所作用変動。
6. M37からM35への有限基底分布誤差。
7. M35の正準対数 $3L+4$ と基底回路深さ。
8. Bell 共同誤差と非信号誤差の分離。

残る課題は、強度制約下の絶対動作時間、総エネルギー収支、雑音耐性、M38の長期安定性、資源下界、一般有限 $L$ の完全周期、多体系での規模依存性である。これらは各目標の検証項目であり、$n$ 量子ビット回路の実装コストを扱うQ8の達成とは数えない。Q8は未着手である。

# 反証条件と未完成ベンチマーク

> **位置づけ：** Q1--Q3はM38の範囲で達成、Q9はM37の限定範囲で達成である。Q5とQ7は部分達成、Q4、Q6、Q8は未着手、Q10--Q13は未達であり、達成済み主張の反証条件と未完成目標の合格条件を分けて示す。


## Zeno 効果（Q4）

Q4では、第4章のRabi 遷移とM38型測定を同じ周期内で接続する。未測定の短時間生存確率と、有限間隔で測定を繰り返した生存確率を比較し、

```math
P_{\rm surv}(T;N)
```

の測定回数 $N$ と間隔 $T/N$ への依存性を導く必要がある。

Hamiltonian を測定中に停止するだけ、摩擦で遷移を抑えるだけ、無反応試行を除外するだけではZeno 効果と判定しない。各測定の外部記録、テンプレート供給、reset セル消費、有限幅誤差を含めても遷移抑制が残ることを示す。

## 一般有限Lへの拡張（Q5）

M35は一般有限 $L$ の任意基底回路、Born 型長期頻度、測定後状態、内部逆計算を与える。Q5を閉じるには、第4章のM38で構成した要素を一般有限 $L$ へ拡張する必要がある。

1. 一般有限 $L$ の有効純粋状態空間と共通位相縮約。
2. 任意の $U(L)$ 操作と一般時間依存駆動。
3. 独立選択器を持つ複数段の異基底逐次測定。
4. 外部記録セルへの結果非依存正準コピー。
5. 一般有限 $L$ の外部 reset セル交換。
6. 空間的に離れた各辺への時計配線と遅延上界。
7. 自由度、時計窓数、外部セル数の規模依存性。

$L=2$ の達成を、記号だけ $L$ へ置き換えることでは合格としない。

## 2量子ビット型結合ゲート（Q6）

2つの論理部分系とテンソル積構造を有限古典正準変数へ明示し、少なくとも1種類のエンタングリングゲートを構成する必要がある。合格条件は次である。

1. 入力論理基底と一般重ね合わせの定義。
2. 外付け行列演算でない明示Hamiltonian 。
3. 全基底入力に対する作用。
4. 積状態から非分離な相関を作ること。
5. 局所操作だけへ分解できないこと。
6. 有限時間忠実度と資源上界。

Q1の2モード $SU(2)$ 操作だけではQ6の達成にならない。

## Bell 型測定統計（Q7）

現行M36は余弦共同確率、CHSH値、非信号性、設定分布保存、測定設定独立性の不成立を同じ条件付き二側測度で示す。残る課題は次である。

1. 反対称集団相関の反復可能な準備。
2. 集団量 $\Xi$ を読まずに単一試行変数から余弦区間多重度を作ること。
3. 整合支持 $G$ の物理的必然性。
4. 完全境界流束測度の結果非依存因子化。
5. 非対称誤差下の非信号上界。
6. 外部設定介入の意味論。
7. M38の局所測定装置との接続。
8. 平面内2出力を超える一般Tsirelson 原理。

$G^c$ の試行を実験後に捨てて25%だけ残す実装は、採用する二側模型ではなく事後選別なので反証になる。

## 量子ゲート型計算機の実装コスト（Q8）

Q8には、$n$ 量子ビット、回路深さ $d$、目標誤差 $\epsilon$ に対する少なくとも次の増加率が必要である。

1. 信号と補助装置の正準対数。
2. 局所結合数と最大並列度。
3. 時計窓数と動作時間。
4. 制御角、比較器、reset セルの必要精度。
5. 永久記録と使用済みセルの容量。
6. 隠れた指数コストの有無。

M38の17対と1周期当たり16外部セルは $n=1$ の予備値であり、Q8の達成とは数えない。

## 位相量子化（Q10）

有限グラフ上で辺位相差を定義するだけでは、連続空間の単価性、節の生成・消滅、閉路変形に対する巻数保存を得られない。Q10には少なくとも次が必要である。

1. 辺内部の補間場または許容配置条件。
2. 非零領域での閉路巻数の整数性。
3. 節を通る位相すべりの有限Hamiltonian 記述。
4. 格子細分化に対する巻数の安定性。
5. 追加量子化条件を別の形で仮定していないこと。

閉路位相を数値的に丸めて整数へ投影するだけでは達成としない。

## 束縛状態（Q11）

時間非依存 $h_L$ の固有ベクトルが有効解として存在することはQ9から従う。しかしQ11は、井戸型・調和型ポテンシャルについて次を要求する。

1. 有限振動子パラメータからのスペクトルと固有ベクトル。
2. 格子幅、領域幅、搬送周波数に対する収束。
3. 基底状態と複数の励起状態の節構造。
4. エネルギー測定器との接続。
5. 弱開放条件下の状態選択または安定性。

固有ベクトルを初期条件として入れるだけでは、状態選択を示したことにならない。

## トンネル効果（Q12）

障壁高、幅、入射エネルギーを掃引し、透過率を目標Schrödinger 解と比較する。少なくとも

```math
\epsilon_{\rm tun}
=
\max_{r\in\mathcal R}
\left|
T_{\rm micro}(r)-T_L(r)
\right|
```

を有限領域 $\mathcal R$ で評価する。熱浴温度、古典的共鳴、障壁越えエネルギーの寄与を分離し、熱活性化だけで同じ透過率を説明できないことを検査する。

## 2重スリット干渉（Q13）

第3章の2経路干渉は位相担体の出力作用を与えるが、粒子検出を導かない。Q13には次が必要である。

1. 各検出セルに局所的な単一試行変数だけからなる結合。
2. 有限観測窓の時間積分流束。
3. 作動、無反応、複数作動を含む完全結果集合。
4. 各試行で唯一の局所記録を得る条件。
5. 検出網内の信号伝播速度と比較時間。
6. スリット開閉に対する分布と総検出率の変化。

点粒子の連続軌道は1つの候補だが、Q13の必須形式とはしない。

## 達成済み主張の反証条件

現行主張は、次のいずれかが起きれば反証または範囲縮小が必要である。

1. 固定作用面のBloch ベクトルが単位球面を満たさない。
2. $G_Z,G_X$ の有限列が目標 $SU(2)$ を再構成しない、または正準性・作用を保存しない。
3. 自律Rabi Hamiltonian の数値軌道が解析遷移公式と一致しない。
4. 同軸再測定で反対符号の安全結果が生じる。
5. 異軸共同分布の全変動距離が $\delta_1+\delta_2$ を超える。
6. 外部記録剪断が理想空セル入口で装置へ反作用する。
7. 記録後の逆計算で内部装置が準備値へ戻らない。
8. 外部セル交換が正準性を失う、または収縮上界を破る。
9. $L=2$ M35測定段の正準対数を10以外として資源評価する。
10. M37の $\eta<1$ の例で生成子上界または有限時間上界が破れる。
11. M35の無反応込み分布が導出上界を超える。
12. Bell 最小測度で設定分布または一側周辺が設定依存になる。
13. 集団相関 $\Xi$ を単一試行の正準変数として再導入する。
14. M37とM38を同一ハードウェアとして暗黙に扱う。
15. 未構成のM0または $\mu_*$ を現行定理の仮定として使う。
16. 生成物と章別正本で式、結果ID、目標の現在地が一致しない。

## 最重要の未解決問題

Q1--Q3をM38で閉じた後の中心課題は、次の3本に分かれる。

1. Q4とQ5側では、M38のRabi 遷移、逐次測定、外部セル周期をZeno 効果と一般有限 $L$ へ拡張する。
2. Q7側では、集団交差相関を単一試行で読まず、余弦区間多重度と二側支持をミクロHamiltonian の解空間から作る。
3. Q10--Q13側では、M37の空間包絡を位相量子化、束縛状態、トンネル、局所検出へ拡張する。

M37、M38、M35、M36を1つのM0と統一母測度へまとめることは、その後の統合目標である。特にM37とM38の同一ハードウェア化はQ3の達成条件ではなく、空間伝播と最小測定装置を同じ物理系へ接続する追加課題である。

# 付録

# 正常モード正準変換と局所包絡誤差

> **位置づけ：** 有限実振動子網の正常モード包絡、局所包絡との Bogoliubov 型変換、作用素誤差、有限時間誤差、局所作用変動を有限次元の行列関数として証明する。


## 正常モード分解

第2章の剛性行列を

```math
K
=
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
```

とし、$K>0$ を仮定する。実直交行列 $O$ と正の固有周波数 $\omega_r$ により

```math
K
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1^2,\ldots,\omega_L^2
\right)
O
```

と書ける。行列平方根は

```math
\Omega
=
K^{1/2}
=
O^{\mathsf T}
\operatorname{diag}
\left(
\omega_1,\ldots,\omega_L
\right)
O
```

である。

正常座標を $x=Oq$、$\pi=Op$ とすれば、

```math
H_{\rm micro}
=
\sum_{r=1}^L
\left[
\frac{\pi_r^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_r^2x_r^2}{2}
\right]
```

となる。

## 厳密正準振幅

行列表記で

```math
c
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}}\,
\Omega^{1/2}q
+
\frac{i}{\sqrt{M_{\rm osc}}}
\Omega^{-1/2}p
\right]
```

と定める。$\Omega$ は実対称正定値なので、

```math
\left\{c_r,c_s^*\right\}
=
-\frac{i}{\mathcal J_0}
\delta_{rs}
```

が成立する。従って $(c,c^*)$ は複素正準座標である。

逆変換は

```math
q
=
\sqrt{
\frac{\mathcal J_0}{2M_{\rm osc}}
}
\Omega^{-1/2}
\left(c+\overline c\right),
```

```math
p
=
-i
\sqrt{
\frac{M_{\rm osc}\mathcal J_0}{2}
}
\Omega^{1/2}
\left(c-\overline c\right)
```

である。Hamiltonian は

```math
H_{\rm micro}
=
\mathcal J_0
c^\dagger\Omega c
```

となり、

```math
i\dot c
=
\Omega c
```

を得る。

## 厳密回転包絡

搬送回転を除いた

```math
\widetilde b(t)
=
e^{i\omega_0t}c(t)
```

を定めると、

```math
i\mathcal J_0
\dot{\widetilde b}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
\widetilde b
```

となる。従って

```math
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

である。また

```math
I_{\rm ex}
=
\mathcal J_0
\widetilde b^\dagger\widetilde b
=
\mathcal J_0c^\dagger c
```

は厳密保存量である。

## 局所振幅との正準変換

局所振幅は

```math
a
=
\frac{1}{\sqrt{2\mathcal J_0}}
\left[
\sqrt{M_{\rm osc}\omega_0}\,q
+
\frac{i}{\sqrt{M_{\rm osc}\omega_0}}p
\right]
```

である。

```math
s
=
\left(
\frac{\Omega}{\omega_0}
\right)^{1/2},
\qquad
U_s
=
\frac12
\left(s+s^{-1}\right),
\qquad
V_s
=
\frac12
\left(s-s^{-1}\right)
```

と置く。$q,p$ の表示を代入すると

```math
c
=
U_sa
+
V_s\overline a
```

を得る。$U_s^2-V_s^2=I$ なので逆変換は

```math
a
=
U_sc
-
V_s\overline c
```

である。回転包絡では

```math
\widetilde b(t)
=
U_sb(t)
+
V_se^{2i\omega_0t}\overline{b(t)},
```

```math
b(t)
=
U_s\widetilde b(t)
-
V_se^{2i\omega_0t}
\overline{\widetilde b(t)}
```

となる。

## 局所変換差の上界

$h_0=h_L$ なら

```math
s
=
\left(
I+
\frac{2h_L}{\mathcal J_0\omega_0}
\right)^{1/4}
```

である。$\eta=2\|h_L\|/(\mathcal J_0\omega_0)<1$ なので、$s$ の固有値は

```math
\left(1-\eta\right)^{1/4}
\leq
s_r
\leq
\left(1+\eta\right)^{1/4}
```

を満たす。

各正の実数 $s_r$ について

```math
\left|
\frac{s_r+s_r^{-1}}{2}-1
\right|
+
\left|
\frac{s_r-s_r^{-1}}{2}
\right|
=
\max
\left\{
s_r-1,
s_r^{-1}-1
\right\}
```

である。従って

$|\log s_r|$ が増えると上式の両項が同時に増え、許容区間では $s_r<1$ 側の最大偏差が $s_r>1$ 側の最大偏差以上である。このため $\|U_s-I\|$ と $\|V_s\|$ の上界を同じ端点で取ることができ、

```math
\left\|U_s-I\right\|
+
\left\|V_s\right\|
\leq
\left(1-\eta\right)^{-1/4}-1
=
\delta_{\rm loc}(\eta)
```

を得る。逆変換と $\|\overline v\|=\|v\|$ から

```math
\left\|
b(t)-\widetilde b(t)
\right\|
\leq
\delta_{\rm loc}
\left\|\widetilde b(t)\right\|
```

である。$\|\widetilde b(t)\|$ は保存されるので本文の一様上界が従う。

## 生成子の Taylor 上界

```math
X
=
\frac{2h_L}{\mathcal J_0\omega_0}
```

と置く。$h_L$ は実対称なので $X$ を直交対角化できる。各固有値 $x\in[-\eta,\eta]$ に対し Taylor の定理から

```math
\left|
\sqrt{1+x}-1-\frac{x}{2}
\right|
\leq
\frac{x^2}
{8\left(1-\eta\right)^{3/2}}
```

である。従って

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

となる。

## Duhamel 評価

Hermitian 行列 $H_1,H_2$ に対し、

```math
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
=
-\frac{i}{\mathcal J_0}
\int_0^t
e^{-iH_1(t-s)/\mathcal J_0}
\left(H_1-H_2\right)
e^{-iH_2s/\mathcal J_0}
\,ds
```

である。両指数の作用素ノルムは1なので、

```math
\left\|
e^{-iH_1t/\mathcal J_0}
-
e^{-iH_2t/\mathcal J_0}
\right\|
\leq
\frac{t}{\mathcal J_0}
\left\|H_1-H_2\right\|
```

を得る。$H_1=h_{\rm ex}$、$H_2=h_L$ とすれば本文第3.3節の上界になる。

局所初期値 $b(0)$ を使う場合は、

```math
\begin{aligned}
\left\|b(t)-e^{-ih_Lt/\mathcal J_0}b(0)\right\|
\leq{}&
\left\|b(t)-\widetilde b(t)\right\|
\\
&+
\left\|
\widetilde b(t)
-e^{-ih_Lt/\mathcal J_0}\widetilde b(0)
\right\|
\\
&+
\left\|
e^{-ih_Lt/\mathcal J_0}
\left[
\widetilde b(0)-b(0)
\right]
\right\|
\end{aligned}
```

と分解し、両端の変換差と中央の生成子差を加える。

## 局所作用変動

```math
e(t)
=
b(t)-\widetilde b(t)
```

と置くと、$\|e(t)\|\leq\delta_{\rm loc}\|\widetilde b(t)\|$ である。従って

```math
\begin{aligned}
\left|
\left\|b(t)\right\|^2
-
\left\|\widetilde b(t)\right\|^2
\right|
\leq{}&
2
\left\|\widetilde b(t)\right\|
\left\|e(t)\right\|
+
\left\|e(t)\right\|^2
\\
\leq{}&
\left(
2\delta_{\rm loc}
+
\delta_{\rm loc}^2
\right)
\left\|\widetilde b(t)\right\|^2.
\end{aligned}
```

$\mathcal J_0$ を掛ければ本文第3.6節の局所作用上界を得る。

## 規格化写像

非零ベクトル $x,y$ に対し、

```math
\left\|
\frac{x}{\left\|x\right\|}
-
\frac{y}{\left\|y\right\|}
\right\|
\leq
\frac{2\left\|x-y\right\|}
{\left\|y\right\|}
```

である。$x=b(T)$、$y=b_L(T)$ とし、

```math
\left\|b_L(T)\right\|
=
\left\|b(0)\right\|
\geq
\left(1-\delta_{\rm loc}\right)
\left\|\widetilde b(0)\right\|
```

を使えば、第4.4節の規格化状態誤差が従う。

## 適用限界

本付録は有限次元、時間非依存、実対称 $h_L$ を扱う。$\eta<1$ は十分条件であり最適条件ではない。負の固有値を持つ $h_L$ も、全剛性が正定値であれば含む。

時間依存行列では各時刻の行列平方根が一般に可換でなく、正常モード基底の回転項が加わる。非線形結合では正常モード生成子自体が状態依存になる。これらへ本文の上界をそのまま適用しない。

# 相関行列、作用区間、無理数回転の補助結果

> **位置づけ：** 理想有効担体の相関行列を補助統計モデルとして整理し、本文第4章と第5章の確率式、不変測度、長期頻度、有限幅上界、Bell 基準体積を証明する。


## 理想有効担体と相関行列

この節だけでは、実正準対から

```math
d_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

を作り、設計済み有効 Hamiltonian

```math
H_{\rm eff}
=
d^\dagger h_Ld
```

を置く。これは第2章の位置ばね網そのものではなく、測定回路を記述する理想正準制御層である。この層内部では

```math
i\mathcal J_0\dot d
=
h_Ld,
\qquad
\mathcal J_0d^\dagger d
=
\operatorname{const}
```

が厳密に成立する。

調製条件 $\mathcal P$ とプログラム $M$ を固定した集団について

```math
C_M(t)
=
\mathbb E_{\mu_{\mathcal P,M}}
\left[
d_t d_t^\dagger
\right]
```

と定める。$C_M$ は正半定値 Hermitian 行列であり、単一試行に追加する物質または正準変数ではない。

## 相関行列の交換子発展

同じ集団の全試行が共通の $h_L(t)$ に従うなら、

```math
\begin{aligned}
i\mathcal J_0
\frac{d}{dt}
\left(dd^\dagger\right)
={}&
h_Ldd^\dagger
-
dd^\dagger h_L
\end{aligned}
```

なので、

```math
i\mathcal J_0\dot C_M
=
\left[h_L,C_M\right]
```

を得る。時間発展作用素を $U$ とすれば

```math
C_M(t)
=
U(t,t_0)
C_M(t_0)
U(t,t_0)^\dagger
```

である。従って跡、全固有値、階数、

```math
\mathcal P_C
=
\frac{\operatorname{tr}C^2}
{\left(\operatorname{tr}C\right)^2}
```

で定める純度が保存される。閉鎖線形発展だけでは高階数集団を階数1へ純化できない。

局所包絡 $b$ の厳密ミクロ発展には反回転項があるため、この交換子方程式を $b$ の厳密集団方程式として使わない。Q9のミクロ集団へ適用する場合は、第3章の包絡誤差を残す必要がある。

## 階数1条件

$C=\Lambda\chi\chi^\dagger$、$\Lambda>0$、$\chi^\dagger\chi=1$ とする。$\chi$ と直交する任意の $v$ について

```math
0
=
v^\dagger Cv
=
\mathbb E
\left|
v^\dagger d
\right|^2
```

なので、$v^\dagger d=0$ がほとんど確実に成立する。有限次元直交補空間の基底を取れば、ある複素確率変数 $c^\omega$ が存在して

```math
d^\omega
=
c^\omega\chi
```

がほとんど確実に成立する。逆も明らかなので、階数1相関と共通射影方向は同値である。

交換子発展の下では、共通位相を選んで

```math
i\mathcal J_0\dot\chi
=
h_L\chi
```

とできる。この結果は理想有効層内部では厳密であるが、Q9のミクロ導出を置き換えない。

## 近似階数1と閉包残差

$C$ の最大固有値を $\lambda_1$、主固有ベクトルを $\chi$ とし、

```math
C
=
\lambda_1\chi\chi^\dagger
+
E,
\qquad
E\geq0
```

とする。階数欠陥を

```math
\varepsilon_{\rm rank}
=
\frac{\operatorname{tr}E}
{\operatorname{tr}C}
```

とする。ユニタリ $W$ の出力 $k$ が理想因子に対して節を持つなら、

```math
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
\leq
\varepsilon_{\rm rank}
```

である。

残差付き有効式

```math
i\mathcal J_0\dot d
=
h_Ld+r
```

では

```math
i\mathcal J_0\dot C
=
\left[h_L,C\right]
+
D_C,
```

```math
D_C
=
\mathbb E
\left[
rd^\dagger-dr^\dagger
\right]
```

であり、

```math
\left\|D_C\right\|
\leq
2
\left(
\mathbb E\left\|r\right\|^2
\right)^{1/2}
\left(
\mathbb E\left\|d\right\|^2
\right)^{1/2}
```

を満たす。4次以上の Hamiltonian では $D_C$ が高次モーメントを含むため、$C$ だけの閉包は自動的に成立しない。

## 作用区間選択

固定した $b,W$ に対し、$I_k\geq0$、$I_{\rm ph}=\sum_kI_k>0$ とする。$u$ が $[0,I_{\rm ph})$ 上で一様なら、結果事象

```math
E_k
=
\left\{
S_{k-1}\leq u<S_k
\right\}
```

の Lebesgue 長は $S_k-S_{k-1}=I_k$ である。従って

```math
P(E_k\mid b,W)
=
\frac{I_k}{I_{\rm ph}}
```

となる。境界集合 $\{u=S_k\}$ は有限集合なので零測度である。

選択器角 $\vartheta$ が $(b,W,\mathcal P)$ の下で条件付き Haar 分布なら、$u=I_{\rm ph}\vartheta/(2\pi)$ は条件付き一様である。条件付き期待値を取れば、

```math
P(k\mid W,\mathcal P)
=
\mathbb E
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
W,\mathcal P
\right]
```

を得る。

## 固定作用公式と共分散補正

$I_{\rm ph}=I_0$ が集団で固定されるとする。$I_k=\mathcal J_0|(Wb)_k|^2$ なので、

```math
\mathbb E[I_k]
=
\mathcal J_0
\left(
WCW^\dagger
\right)_{kk},
```

```math
\mathbb E[I_{\rm ph}]
=
\mathcal J_0
\operatorname{tr}C
=
I_0
```

である。従って

```math
P_k
=
\frac{
\left(WCW^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
```

を得る。

全作用が変動する場合、$r_k=I_k/I_{\rm ph}$ と置けば $I_k=I_{\rm ph}r_k$ だから、

```math
\mathbb E[I_k]
=
\mathbb E[I_{\rm ph}]
\mathbb E[r_k]
+
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
```

である。$P_k=\mathbb E[r_k]$ を解けば本文の共分散恒等式を得る。

## 無理数円回転の不変性

正規化角 $r=\vartheta/(2\pi)\in\mathbb R/\mathbb Z$ を用い、

```math
R_\alpha(r)
=
r+\alpha
\pmod1,
\qquad
\alpha\notin\mathbb Q
```

とする。円周 Haar 測度 $m$ は平行移動不変なので、任意の可測集合 $A$ に対し

```math
m
\left(
R_\alpha^{-1}A
\right)
=
m(A)
```

である。従って $m$ は不変確率測度である。

一意性を Fourier 係数で示す。$R_\alpha$ の不変確率測度を $\nu$ とし、整数 $n$ に対する Fourier 係数を

```math
\widehat\nu(n)
=
\int_0^1
e^{-2\pi inr}
\,d\nu(r)
```

とする。不変性から

```math
\widehat\nu(n)
=
e^{-2\pi in\alpha}
\widehat\nu(n)
```

を得る。$n\neq0$ かつ $\alpha\notin\mathbb Q$ なら $e^{-2\pi in\alpha}\neq1$ なので、$\widehat\nu(n)=0$ である。$\widehat\nu(0)=1$ と合わせ、全 Fourier 係数が Haar 測度と一致する。三角多項式の一様稠密性により $\nu=m$ である。

## 一意エルゴード性と区間頻度

連続関数 $f$ の時間平均を

```math
A_Nf(r)
=
\frac1N
\sum_{j=0}^{N-1}
f
\left(
r+j\alpha
\right)
```

とする。 Fourier モード $f_n(r)=e^{2\pi inr}$ に対し、$n\neq0$ なら

```math
A_Nf_n(r)
=
e^{2\pi inr}
\frac{
1-e^{2\pi inN\alpha}
}{
N
\left(
1-e^{2\pi in\alpha}
\right)
}
```

であり、$N\to\infty$ で $r$ に一様に零へ収束する。$n=0$ では1である。三角多項式近似により、任意の連続 $f$ について

```math
A_Nf(r)
\longrightarrow
\int_0^1f(s)\,ds
```

が一様に成立する。従って回転は一意エルゴード的である。

区間指示関数は端点で不連続だが、端点近傍を除いて上下から連続関数で挟める。よって任意の半開区間 $[a,b)$ について

```math
\lim_{N\to\infty}
\frac1N
\sum_{j=0}^{N-1}
\mathbf1_{[a,b)}
\left(
r+j\alpha
\right)
=
b-a
```

である。これを長さ $p_k$ の結果区間へ適用すると Born 型長期頻度を得る。

## 無理数回転は混合的でない

Haar 空間上の非定数 Fourier モード $f_n$ に対し、

```math
f_n\circ R_\alpha^j
=
e^{2\pi inj\alpha}f_n
```

である。従って相関

```math
\int
f_n
\overline{f_n\circ R_\alpha^j}
\,dm
=
e^{-2\pi inj\alpha}
```

の絶対値は1のままで零へ収束しない。よって無理数回転は混合的でない。一意エルゴード性から長期平均は得られるが、独立同分布型の有限標本揺らぎは従わない。

## 有限幅境界の測度上界

固定作用 $I_{\rm ph}$ の区間内に $L-1$ 個の内部境界 $S_1,\ldots,S_{L-1}$ がある。各境界の半幅 $w$ 近傍は長さ高々 $2w$ なので、一様測度と和集合上界から

```math
\mu_{\chi,W}^{\rm cyc}
\left(
\min_{1\leq k<L}
|u-S_k|<w
\right)
\leq
2(L-1)
\frac{w}{I_{\rm ph}}
```

を得る。境界近傍が重なれば左辺はさらに小さい。

角の切断点近傍では、$f(\vartheta)=\vartheta/(2\pi)$ を円周上の滑らかな関数へ置き換える必要がある。その近傍の Haar 幅を $\varepsilon_{\rm cut}$ とすれば、無反応結果の全質量は右辺に $\varepsilon_{\rm cut}$ を加えて抑えられる。

## 高階数集団に必要な追加自由度

固定作用殻上の源状態を $b^\omega$ とし、選択器角が $b^\omega$ の下で条件付き一様なら、

```math
P(k)
=
\mathbb E_\omega
\left[
\left|
\left(Wb^\omega\right)_k
\right|^2
\right]
=
\left(
WCW^\dagger
\right)_{kk}
```

である。ただし、本文の1次元不変トーラスでは $b^\omega=\chi$ が固定される。高階数 $C$ を単一軌道の時間平均として得るには、$b^\omega$ を動かす別の不変力学と、その力学に条件付けても選択器角が Haar 分布を保つ積構造または十分な結合条件が必要である。

## 4成分 Bell 重み

規格化反対称行列を

```math
\widehat\Xi_0
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
```

とする。$d=\alpha_x-\beta_y$ と置くと、回転の積を直接計算して

```math
R(\alpha_x)
\widehat\Xi_0
R(\beta_y)^{\mathsf T}
=
\frac1{\sqrt2}
\begin{pmatrix}
\sin d&\cos d\\
-\cos d&\sin d
\end{pmatrix}
```

を得る。成分の絶対値2乗は

```math
w_{++}=w_{--}
=
\frac12\sin^2d,
\qquad
w_{+-}=w_{-+}
=
\frac12\cos^2d
```

である。$\sin^2d=(1-\cos2d)/2$、$\cos^2d=(1+\cos2d)/2$ から

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos2d
\right]
```

が従う。また全成分の和は1である。

## 局所 Haar 角の基準セクター

固定設定 $x$ に対し、$A_x(\phi_A)=\operatorname{sgn}\cos(\phi_A-2\alpha_x)$ の正負領域はそれぞれ長さ $\pi$ の半円である。従って

```math
P_0(A\mid x)
=
\frac12
```

である。B側も同様であり、$\phi_A,\phi_B$ の独立性から

```math
q_{AB}^{xy}
=
P_0(A,B\mid x,y)
=
\frac14
```

を得る。

未来角区間の長さが $w_{AB}^{xy}$ なので、積測度により

```math
\nu_{\rm B}^0
\left(
A,B,G
\mid
x,y
\right)
=
\frac14w_{AB}^{xy}
```

である。全結果の和と $\sum_{A,B}w_{AB}^{xy}=1$ から

```math
\nu_{\rm B}^0
\left(
G
\mid
x,y
\right)
=
\frac14
```

を得る。

## 二側条件付けと設定分布保存

$d\mu_{\rm B}=4\mathbf1_G\,d\nu_{\rm B}^0$ とする。固定設定で

```math
P_{\mu_{\rm B}}(A,B\mid x,y)
=
\frac{
\nu_{\rm B}^0(A,B,G\mid x,y)
}{
\nu_{\rm B}^0(G\mid x,y)
}
=
w_{AB}^{xy}
```

である。また

```math
P_{\mu_{\rm B}}(x,y)
=
4\pi_x\pi_y
\nu_{\rm B}^0(G\mid x,y)
=
\pi_x\pi_y
```

なので、設定生成器の分布は保たれる。

## 非信号周辺と測定設定独立性

余弦重みを一側で和を取ると、$B=\pm1$ の線形項が相殺して

```math
\sum_Bw_{AB}^{xy}
=
\frac12
```

となる。B側周辺も同様である。これは理想反対称源と共通基準密度に依存する。

一方、$d\mu_{\rm B}(\Lambda\mid x,y)=4\mathbf1_{G_{xy}}(\Lambda)d\nu_{\rm B}^0(\Lambda)$ であり、$G_{xy}$ は設定依存である。従って設定分布が保たれても、完全履歴の測定設定独立性は一般に成立しない。

## 一般基準密度

付随自由度を含む基準測度が各結果セクター上で密度 $q_{AB}^{xy}$ を持つなら、

```math
\nu^0(A,B,G\mid x,y)
\propto
q_{AB}^{xy}K_{AB}^{xy}
```

である。条件付き規格化により

```math
P(A,B\mid x,y,G)
=
\frac{
q_{AB}^{xy}K_{AB}^{xy}
}{
\sum_{A',B'}
q_{A'B'}^{xy}K_{A'B'}^{xy}
}
```

を得る。$q_{AB}^{xy}$ が4結果で共通なら余弦則へ戻る。非共通補正は共同分布と周辺分布へ同時に入るため、完全模型では結果別密度を独立に検査する必要がある。

# 局所滑らか有限基底測定周期の完全正準構成

> **位置づけ：** M35の一般有限L構成について、局所2モード回路、累積比較ポインター、無反応を含む結果集合、信号、テンプレート、レジスター、選択器、時計の全写像を追跡する。L=2の2段測定、外部記録、弱開放 reset は付録Eで扱う。


## 正準自由度

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

## 時計窓と自律化

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

## 隣接2モード回路による任意ユニタリ

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

## 準備回路と測定基底

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

## 作用、閾値、累積差の読出し

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

## 双曲型増幅と滑らかな比較

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

## 隣接テンプレート経路と記録

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

## 正準 SWAP 、測定後基底、保持

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

## 全入力に対する逆計算

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

へ戻る。滑らかな有限幅模型では、結果形成を無反応込みの粗視化で定義しながら、内部 Hamiltonian 写像そのものは全入力で厳密に可逆である。

## 選択器ドリフトと時計運動量

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

## Poincaré 写像と長期分布

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

## 有限誤差に対する安全余裕

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

## ゲート数と直列深さ

密な $W$ に対する資源上界は次である。

| 対象 | 隣接2モード混合回数 |
|---|---:|
| $W$ 1回 | $L(L-1)/2$ 以下 |
| 周期内の $W$、$W^\dagger$ 4回 | $2L(L-1)$ 以下 |
| 固定純粋準備 $U_{\rm prep}$ | $L-1$ 以下 |
| 準備と逆準備 | $2(L-1)$ 以下 |

比較剪断、テンプレート経路、逆実行はそれぞれ $O(L)$ 回である。信号モード数と物理交換辺数は増えず、1次元鎖の $L-1$ 辺を再利用する。

逐次 Givens 消去では基底回路の直列深さは $O(L^2)$ である。互いに素な辺を同じ時計層へ並列化する Clements 型配置では、基底回路の深さを $O(L)$ にできる [39]。ただし1個の時計自由度から空間的に離れた各辺へ窓信号を局所伝播させる配線自由度と遅延は、この数え上げに含めない。

## 通常の位置ばねだけに限定した場合

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

と評価できる。しかし現行Q9定理は時間非依存 $h_L$ に限定され、順方向と逆方向の反回転誤差が無限反復で相殺されることも証明していない。古典振動子による一般複素状態の厳密表示に位置・運動量の双方の結合または符号調整が必要になることは、既存研究とも整合する [35--37]。

従って本付録では $QQ+PP$ 型の局所交換を測定装置の現行構成とする。M37の位置ばね網との同一ハードウェア化はQ1--Q3の達成条件ではなく、M0、Q5またはQ13へ接続する一般統合課題である。

## 永久記録の限界

本周期の $Q_M$ と比較ポインターは内部記録であり、保持窓後に逆計算される。保持窓で結果を別の外部記録へコピーすれば、その外部自由度は結果情報を保持する。Hamiltonian 流の1対1性により、その外部記録まで結果に依存しない同一点へ戻すことはできない。

永久記録を伴う反復装置では、外部自由度を拡大するか、記録を循環履歴レジスターへ移すか、弱開放系として情報とエネルギーを外へ運ぶ必要がある。$L=2$ では付録EのM38が外部記録セルとreset セル流を構成する。本付録の一般有限 $L$ のM35は、その外部過程を含まない。

## 未導出事項

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

# Bell 二側履歴模型の条件付き実装と因子化条件

> **位置づけ：** 局所分析器、局所記録、未来区間比較、境界面の引戻しを単一試行変数で記述する。集団交差相関を単一試行で読み取る操作は除き、余弦区間のミクロ生成と二側支持条件の必然性を未導出事項として残す。


## 集団量と単一試行量

単一試行 $\omega$ の左右担体を $z^{A,\omega},z^{B,\omega}$ とする。交差相関

```math
\Xi
=
\mathbb E
\left[
z^{A,\omega}
\left(z^{B,\omega}\right)^{\mathsf T}
\right]
```

は集団量である。従って、単一試行の正準状態へ $\Xi$ を座標として追加したり、Hamiltonian が $\Xi$ を直接読んだりすることはできない。

本付録の単一試行変数は次に限定する。

1. 左右の2モード局所担体。
2. 設定生成器 $x,y$ と局所分析器角 $\alpha_x,\beta_y$。
3. 局所結果角 $\phi_A,\phi_B$。
4. 局所結果記録 $(Q_{M_A},P_{M_A})$、$(Q_{M_B},P_{M_B})$。
5. 共通未来角 $(\theta_F,J_F)$。
6. 設定と記録を未来領域へ運ぶ伝送自由度。
7. 区間境界、比較、逆計算に使う補助レジスター。
8. 時計 $(\tau,P_\tau)$。

反対称源条件 $\Xi=\Xi_0$ は調製集団の条件であり、単一試行の等式ではない。

## 局所分析器

A側とB側の平面回転生成子を $G_A,G_B$ とし、

```math
\left\{G_A,G_B\right\}
=
0
```

とする。局所分析器 Hamiltonian を

```math
H_{\rm an}
=
g_A(\tau)\alpha_xG_A
+
g_B(\tau)\beta_yG_B
```

とする。$g_A,g_B$ は空間的に分離した局所窓を表す。単一試行では

```math
z^{A,\omega}
\longmapsto
R(\alpha_x)z^{A,\omega},
\qquad
z^{B,\omega}
\longmapsto
R(\beta_y)z^{B,\omega}
```

と作用する。集団平均を後から取れば交差相関は

```math
\Xi_0
\longmapsto
R(\alpha_x)
\Xi_0
R(\beta_y)^{\mathsf T}
```

と変換する。

## 局所結果形成と記録

理想局所応答を

```math
A_x(\phi_A)
=
\operatorname{sgn}
\cos
\left(
\phi_A-2\alpha_x
\right),
```

```math
B_y(\phi_B)
=
\operatorname{sgn}
\cos
\left(
\phi_B-2\beta_y
\right)
```

とする。局所記録 Hamiltonian 候補は

```math
H_{\rm ptr}
=
g_{M_A}(\tau)
P_{M_A}A_x(\phi_A)
+
g_{M_B}(\tau)
P_{M_B}B_y(\phi_B)
```

である。$P_{M_A}=P_{M_B}=0$ の理想入口では局所結果角への反作用は零であり、単位面積パルス後に $Q_{M_A}=A$、$Q_{M_B}=B$ となる。

符号関数は不連続である。滑らかな有限幅関数へ置き換えると、零点近傍だけで記録が中間値になる。比較幅が結果別に異なると基準密度 $q_{AB}^{xy}$ を歪める。

## 有限速度の情報伝送

設定と局所記録を戻りモードへ正準交換し、有限速度で共通未来へ伝播させる。伝送 Hamiltonian を

```math
H_{\rm ret}
=
H_{\rm ret}^{A}
+
H_{\rm ret}^{B}
```

とする。各項は同じ翼の局所自由度と伝送モードだけを結合し、分離中に反対翼を参照しない。共通未来へ到着した後に $(x,y,A,B)$ を同じ局所領域で比較できる。

伝送効率、到着時刻、分散が結果に依存する場合、その因子は一般基準密度へ含める。本付録は理想的な完全交換だけを使う。

## 余弦区間プログラム

反対称源集団について、設定角から

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB
\cos
2\left(\alpha_x-\beta_y\right)
\right]
```

を計算する固定プログラムを置く。累積境界を

```math
T_0=0,
\qquad
T_1=w_{++}^{xy},
\qquad
T_2=T_1+w_{+-}^{xy},
```

```math
T_3=T_2+w_{-+}^{xy},
\qquad
T_4=1
```

とする。設定は単一試行変数なので、既知の解析関数を可逆算術回路で評価する候補は書ける。しかし、この回路は余弦重みの物理的起源を導かない。反対称な集団相関から得た式を装置プログラムへ入力している。

将来必要なのは、集団相関を読むことなく、単一試行の源変数と局所 Hamiltonian の解多重度から同じ区間長が生じる構成である。本付録はその構成を持たない。

## 共通未来角と整合判定

共通未来角から

```math
r_F
=
\frac{\theta_F}{2\pi}
```

を作る。記録済み結果 $(A,B)$ に対応する累積区間を $\mathcal I_{AB}^{xy}$ とし、理想整合指示関数を

```math
\zeta_G
=
\mathbf1
\left[
r_F
\in
\mathcal I_{Q_{M_A},Q_{M_B}}^{xy}
\right]
```

とする。整合レジスター $(Q_G,P_G)$ への候補は

```math
H_{\rm cmp}
=
g_G(\tau)
P_G\zeta_G
```

である。$\zeta_G$ は未来角から結果を生成しない。$Q_{M_A},Q_{M_B}$ は既に局所領域で記録されており、共通未来では整合性だけを計算する。

前向き計算後に算術レジスターを逆順・逆符号で戻すことはできる。永久外部記録は同じ閉鎖周期の準備点へ戻らない。

## 二側境界面と引戻し

準備時刻を $t_0$、共通未来時刻を $t_F$ とし、終端境界面を

```math
\mathcal B_F
=
\left\{
r_F
\in
\mathcal I_{AB}^{xy}
\right\}
```

とする。Hamiltonian 流 $\Phi_T$ のうち、準備面と $\mathcal B_F$ の双方を満たす軌道だけを物理的解とする。許容初期集合は

```math
\Phi_T^{-1}
\left(
\mathcal B_F
\right)
```

である。最小因子化模型では、Hamiltonian 流の Liouville 体積保存と未来角の独立 Haar 密度により、固定した局所結果セクター内で、この引戻し集合の体積は未来区間体積に比例する。完全模型で同じ比例を得るには、第D.8節の付随測度、境界 Jacobian、解多重度に関する因子化条件が必要である。

この境界面は Hamiltonian の力項ではない。初期値問題へ未来から制御信号を加えるのでなく、解集合の支持を定める。なぜこの二側境界法則を採用すべきかは未解決である。

## 基準測度の因子化

最小模型では

```math
d\nu_{\rm B}^0
=
\pi_x\pi_y
\frac{d\phi_A}{2\pi}
\frac{d\phi_B}{2\pi}
\frac{d\theta_F}{2\pi}
```

を使う。完全正準境界面上の Liouville 流束測度を $d\nu_{\rm full}^0$ とすると、最小結果へ還元する十分条件は

```math
d\nu_{\rm full}^0
=
d\nu_{\rm B}^0
\,d\nu_{\rm aux}
```

と因子化し、$d\nu_{\rm aux}$ の総質量、境界 Jacobian、解多重度が $A,B$ に依存しないことである。この条件が破れる場合、結果別係数 $q_{AB}^{xy}$ を残す必要がある。

一般式は

```math
P(A,B\mid x,y,G)
=
\frac{
q_{AB}^{xy}w_{AB}^{xy}
}{
\sum_{A',B'}
q_{A'B'}^{xy}w_{A'B'}^{xy}
}
```

である。$q_{AB}^{xy}=1/4$ は最小因子化模型では局所 Haar 角から導けるが、完全装置では別に検証しなければならない。

## 設定分布保存と介入

最小模型では $\nu_{\rm B}^0(G\mid x,y)=1/4$ が設定に依存しないため、二側条件付け後も $P(x,y)=\pi_x\pi_y$ である。これは観測された設定頻度の保存である。

一方、外部介入で設定レジスターだけを変更し、他のミクロ境界変数を固定した分布は、条件付き観測分布 $\mu_{\rm B}(\cdot\mid x,y)$ と同じとは限らない。二側境界模型の介入意味論は未構成であり、設定分布保存だけから介入安定性を結論しない。

## 有限幅と結果依存誤差

完全模型で別々に測るべき誤差は次である。

1. 局所結果比較の遷移領域質量。
2. 左右結果角の非一様性と相互相関。
3. 結果別の伝送損失と到着失敗率。
4. 設定から余弦区間を計算する算術残差。
5. 未来区間境界の比較幅。
6. 結果別の境界 Jacobian と解多重度。
7. 逆計算後の全正準変数残差。
8. 外部記録を含む長期反復時の容量増加。

共同確率、一側周辺、設定分布、事後除外率を別々に検証する。1個の有効誤差へまとめると、非信号性の破れと共同相関の破れを区別できない。

## 未導出事項

本付録からは次は導かれない。

1. 一般初期集団からの反対称交差相関の準備。
2. 集団相関を使わない単一試行の余弦区間多重度。
3. 二側整合支持条件 $G$ の物理的必然性。
4. $\mu_{\rm B}$ を通常の前向き Poincaré 写像の不変測度として生成すること。
5. 付随自由度を含む完全境界流束測度の結果非依存因子化。
6. 滑らかな有限幅比較での厳密2値結果。
7. 外部設定介入に対する二側統計の安定性。
8. 永久記録を含む有限閉鎖全系の完全再初期化。
9. 平面内2出力を超える一般 Tsirelson 原理。

# 2モード完全周期の正準構成と誤差上界

> **位置づけ：** M38の共通位相縮約、SU(2) 生成子、Rabi 解、2選択器トーラス、連続性障害、外部記録剪断、外部セル交換 reset、局所時計、完全周期写像を検算可能な形で与える。


## Hopf 写像の繊維

固定作用面では

```math
b
=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\qquad
|z_1|^2+|z_2|^2=1
```

である。Bloch 成分は

```math
r_x=2\operatorname{Re}(z_1^*z_2),
\qquad
r_y=2\operatorname{Im}(z_1^*z_2),
\qquad
r_z=|z_1|^2-|z_2|^2
```

となる。直接計算すると

```math
r_x^2+r_y^2+r_z^2
=
4|z_1|^2|z_2|^2
+
\left(|z_1|^2-|z_2|^2\right)^2
=1
```

を得る。

$r_z\neq-1$ なら、Bloch ベクトルから代表元を

```math
b(\boldsymbol r)
=
\begin{pmatrix}
\sqrt{(1+r_z)/2}\\
(r_x+ir_y)/\sqrt{2(1+r_z)}
\end{pmatrix}
```

と選べる。南極では $b=(0,1)^{\mathsf T}$ を選ぶ。同じ $\boldsymbol r$ を持つ別の規格化ベクトルはこの代表元の共通位相倍である。従ってHopf 写像の各繊維は $U(1)$ 軌道である。

## Bloch 成分のPoisson 代数

複素正準振幅は

```math
\{b_j,b_k^*\}
=
-\frac{i}{\mathcal J_0}\delta_{jk}
```

を満たす。Hermitian行列 $A,B$ に対し

```math
F_A=b^\dagger A b,
\qquad
F_B=b^\dagger B b
```

と置くと、

```math
\{F_A,F_B\}
=
-\frac{i}{\mathcal J_0}
b^\dagger[A,B]b
```

である。Pauli 行列の交換関係

```math
[\sigma_i,\sigma_j]
=
2i\epsilon_{ijk}\sigma_k
```

を代入すれば

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

が従う。

## SU(2) 生成子の正準流

$G_{Z,j}$ の時間 $\theta$ の流れは

```math
b_j
\longmapsto
e^{-i\theta}b_j
```

であり、他のモードを変えない。$G_X$ の時間 $\theta$ の流れは

```math
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix}
\longmapsto
e^{-i\theta\sigma_x}
\begin{pmatrix}
b_1\\
b_2
\end{pmatrix}
```

である。相対位相回転

```math
e^{-i\theta\sigma_z/2}
```

は $G_{Z,1}$ と $G_{Z,2}$ に逆符号の半角パルスを加えて得る。従って $Z$--$X$--$Z$ のEuler 分解を各正準流へ置き換えれば、任意の $SU(2)$ を有限パルスで実装できる。

各生成子 $G$ は自身の流れで保存される。時計窓 $g(\tau)$ の面積が目標角に等しければ、パルス形状によらず同じ正準写像を得る。

## Rabi 回転座標

第4.4節の信号部分は

```math
i\dot b
=
\frac12
\left[
\omega_q\sigma_z
+
\Omega
\left(
\cos\tau_d\,\sigma_x
+
\sin\tau_d\,\sigma_y
\right)
\right]b
```

を与える。恒等式

```math
\cos\tau_d\,\sigma_x
+
\sin\tau_d\,\sigma_y
=
e^{-i\tau_d\sigma_z/2}
\sigma_x
e^{i\tau_d\sigma_z/2}
```

を使い、$b=e^{-i\tau_d\sigma_z/2}c$ と置く。$\dot\tau_d=\omega_d$ なので

```math
i\dot c
=
\frac12
\left[
(\omega_q-\omega_d)\sigma_z
+
\Omega\sigma_x
\right]c
```

となる。定生成子の指数関数

```math
e^{-it(\Delta\sigma_z+\Omega\sigma_x)/2}
=
\cos\frac{\Omega_Rt}{2}\,I
-
i\sin\frac{\Omega_Rt}{2}
\frac{\Delta\sigma_z+\Omega\sigma_x}{\Omega_R},
```

```math
\Omega_R
=
\sqrt{\Delta^2+\Omega^2}
```

を $e_1$ へ作用させれば、第4.4節の遷移公式を得る。

## 任意軸の作用比

規格化信号のBloch 表示は

```math
bb^\dagger
=
\frac12
\left(
I+\boldsymbol r\cdot\boldsymbol\sigma
\right)
```

である。従って

```math
p_s(\boldsymbol n)
=
b^\dagger P_s(\boldsymbol n)b
=
\operatorname{tr}
\left[
bb^\dagger P_s(\boldsymbol n)
\right]
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
```

となる。第1結果 $s$ の後は $\boldsymbol r=s\boldsymbol n$ なので、別軸 $\boldsymbol m$ について

```math
p_t(\boldsymbol m\mid s)
=
\frac{1+st\boldsymbol n\cdot\boldsymbol m}{2}
```

が従う。同軸 $\boldsymbol m=\boldsymbol n$ では反対符号の作用区間長が零になる。

## 2次元トーラスの一意エルゴード性

Poincaré 写像を

```math
R_{\boldsymbol\alpha}(\boldsymbol\vartheta)
=
\boldsymbol\vartheta+2\pi\boldsymbol\alpha
\pmod{2\pi},
\qquad
\boldsymbol\alpha=(\alpha_1,\alpha_2)
```

とする。整数ベクトル $k\in\mathbb Z^2\setminus\{0\}$ に対し

```math
k\cdot\boldsymbol\alpha
\notin
\mathbb Z
```

であることは、$1,\alpha_1,\alpha_2$ の有理数体上の1次独立性と同値である。Fourier 指標の軌道平均は

```math
\frac1N
\sum_{n=0}^{N-1}
e^{ik\cdot(\boldsymbol\vartheta+2\pi n\boldsymbol\alpha)}
\longrightarrow0
```

となる。三角多項式の稠密性から、連続関数の軌道平均はトーラスHaar 積分へ収束する。境界がHaar 零の結果集合についても指示関数近似により長期頻度が得られる。

第1結果集合のHaar 幅は $p_s(\boldsymbol n)$、その安全結果後の第2集合の条件付き幅は $p_t(\boldsymbol m\mid s)$ である。2角の積測度から

```math
P(s,t)
=
p_s(\boldsymbol n)
p_t(\boldsymbol m\mid s)
```

が従う。有限幅で理想結果が変わり得るのは、第1または第2の無反応集合に入る試行だけである。合併上界により

```math
D_{\rm TV}
\leq
P(\mathcal O_{\varnothing,1})
+
P(\mathcal O_{\varnothing,2})
\leq
\delta_1+\delta_2
```

となる。

## 連続性障害

滑らかなHamiltonian $H$ の有限時間流 $\Phi_T$ は、解が存在する領域で微分同相写像である。信号部分への射影を $\pi_{\rm sig}$ とすれば

```math
F
=
\pi_{\rm sig}\circ\Phi_T
```

は連続である。連結集合 $X$ の連続像 $F(X)$ は連結である。相異なる2点だけからなり両点を含む像は非連結なので、全入力を2点だけへ送る滑らかな結果写像は存在しない。

M35とM38では、平坦な安全セクター間に滑らかな遷移領域を置き、その全体を無反応結果とする。従って信号像は遷移領域で連続につながり、定理と矛盾しない。

## 2段写像と逆計算順序

第1測定段の前向き正準写像を $M_1$、第2段を $M_2$、外部記録剪断を $C_R$ とする。第1段のテンプレートを $t_1$、第2段を $t_2$ とし、両方を空準備する。前向き写像は

```math
M_2M_1
```

である。第1安全結果の後の信号を第2段が測定するため、順序を交換してはならない。

記録後の内部逆計算は

```math
M_1^{-1}M_2^{-1}
```

である。合成全体は

```math
\left(M_1^{-1}M_2^{-1}\right)
C_R
\left(M_2M_1\right).
```

記録セルの共役運動量が零なら、$C_R$ は内部変数を変えない。従って内部制限は恒等写像になり、記録座標だけが結果コード分だけ平行移動する。

無反応領域でも $M_1$ と $M_2$ は滑らかな正準写像として定義されているので、同じ逆計算が成立する。離散結果が定義されないことと、逆写像が存在しないことを混同しない。

## 外部記録剪断の正準性

1つの記録セルについて

```math
G_{\rm rec}
=
P^R\Pi(z)
```

とする。Hamilton方程式は

```math
\dot Q^R=\Pi(z),
\qquad
\dot P^R=0,
```

```math
\dot z
=
P^R X_{\Pi}(z)
```

である。$P^R=0$ の理想入口では $z$ が固定され、$Q^R$ だけが移動する。これはHamiltonian 流なので正準性は自動的に成立する。

$|P^R|\leq\sigma_P$ なら、記録窓長を $T_R$、対象領域でのHamiltonian ベクトル場上界を $\|X_\Pi\|\leq K_\Pi$ として

```math
\|\Delta z\|
\leq
T_R\sigma_PK_\Pi
```

を得る。この量を $\varepsilon_{\rm rec}$ の状態誤差へ入れる。

## 外部セル交換と収縮

1つの装置偏差 $a$ と外部偏差 $e$ について

```math
G
=
i\mathcal J_0
\left(a^*e-e^*a\right)
```

とする。交換角を流れ時間 $\phi$ とすれば

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

この行列は直交かつユニタリであり、実正準座標ではシンプレクティックである。$\phi=\pi/2$ では $a^+=e^-$、$e^+=-a^-$ となる。

内部周期後の加法残差を $\xi_n$ とし、

```math
a_{n+1}
=
c a_n+s e_n+\xi_n,
\qquad
c=\cos\phi,
\qquad
s=\sin\phi
```

と書く。$|c|<1$、$\|e_n\|\leq\sigma_E$、$\|\xi_n\|\leq\varepsilon_{\rm cyc}$ なら反復により

```math
\|a_n\|
\leq
|c|^n\|a_0\|
+
\frac{1-|c|^n}{1-|c|}
\left(
|s|\sigma_E+\varepsilon_{\rm cyc}
\right).
```

従って第4.10節の極限上界が従う。

## 作用・角時計の帰還

1つの窓について

```math
H
=
\Omega_cJ_c
+
\Omega_cg(\tau_c)G(z)
```

とする。$\dot\tau_c=\Omega_c$ である。$G$ は自身のHamiltonian 流で保存されるので、窓中の $G$ は一定である。時計作用の変化は

```math
\Delta J_c
=
-\int
\Omega_cg'(\tau_c)G\,dt
=
-G\int g'(\tau_c)\,d\tau_c
=0
```

となる。支持が交わらない複数窓では同じ計算を順に適用できる。

窓が重なる場合、または窓中に別のHamiltonian が $G$ を変える場合はこの厳密帰還を使えない。有限誤差は

```math
|\Delta J_c|
\leq
\int
|g'(\tau_c)|
|G(\tau_c)-G_*|
\,d\tau_c
```

で評価し、時計誤差へ入れる。

## 正準対数

$L=2$ のM35測定段の内訳は次である。

| 対象 | 正準対数 |
|---|---:|
| 信号 | 2 |
| テンプレート | 2 |
| 作用レジスター | 2 |
| 閾値 | 1 |
| 内部記録 | 1 |
| 選択器 | 1 |
| 時計 | 1 |
| 合計 | 10 |

2段では信号と時計だけを共有する。各段の固有部分はテンプレート2、作用2、閾値1、内部記録1、選択器1の7対なので、合計は17対である。

外部交換の14対は、共有信号2対と、各段のテンプレート2、作用2、閾値1、内部記録1を合計した12対からなる。選択器と時計は理想Poincaré 写像の一部なので交換しない。外部記録2対を加え、1周期当たり16対の外部セルを使う。

## 完全周期の誤差合成

誤差を次の4層に分ける。

1. 正準状態誤差 $\varepsilon_z$。
2. 規格化信号方向誤差 $\varepsilon_{\rm dir}$。
3. 比較境界の入力換算移動量 $\Delta_{\rm cmp}$。
4. 結果分布の全変動距離 $\varepsilon_{\rm TV}$。

パルス、時計、記録反作用、逆計算、reset セル幅は最初に $\varepsilon_z$ へ評価する。信号作用が零から離れた領域で規格化写像のLipschitz上界を使い $\varepsilon_{\rm dir}$ へ移す。作用読出しと累積差の微分上界を使って $\Delta_{\rm cmp}$ へ移し、最後に境界近傍のHaar 質量へ変換する。

2段分布について、安全な和上界は

```math
\varepsilon_{\rm TV}
\leq
\delta_1+\delta_2
+
\varepsilon_{\rm op}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm inv}
+
\varepsilon_{\rm rst}
+
\varepsilon_{\rm port}
```

の形になる。右辺の各装置誤差は、前段の変換を通して全変動距離へ換算した後の無次元量を表す。

有限個のパルスと有限個の滑らかな写像だけを使うため、各誤差源を十分小さく選べば任意の $\epsilon>0$ に対して $\varepsilon_{\rm TV}<\epsilon$ と周期末偏差 $<\epsilon$ を同時に満たせる。有限幅を零、時計誤差を零、外部セル幅を零と置いた理想極限では、内部Poincaré 写像は2角の平行移動を除いて恒等写像である。

この証明は、固定プログラムごとに必要な窓数が有限であることを使う。可変プログラム全体、一般有限 $L$、無限記録容量、熱力学的最小コストへ一様な資源上界を与えるものではない。

# 参考文献


- [1] J. S. Bell, ``On the Einstein Podolsky Rosen Paradox,'' Physics Physique Fizika 1, 195--200 (1964). <https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195>
- [2] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, ``Proposed Experiment to Test Local Hidden-Variable Theories,'' Physical Review Letters 23, 880--884 (1969). <https://doi.org/10.1103/PhysRevLett.23.880>
- [3] E. Nelson, ``Derivation of the Schrödinger Equation from Newtonian Mechanics,'' Physical Review 150, 1079--1085 (1966). <https://doi.org/10.1103/PhysRev.150.1079>
- [4] F. Guerra and L. M. Morato, ``Quantization of Dynamical Systems and Stochastic Control Theory,'' Physical Review D 27, 1774--1786 (1983). <https://doi.org/10.1103/PhysRevD.27.1774>
- [5] K. Yasue, ``Stochastic Calculus of Variations,'' Journal of Functional Analysis 41, 327--340 (1981). <https://doi.org/10.1016/0022-1236(81)90079-3>
- [6] J.-C. Zambrini, ``Stochastic Mechanics According to E. Schrödinger,'' Physical Review A 33, 1532--1548 (1986). <https://doi.org/10.1103/PhysRevA.33.1532>
- [7] K. B. Wharton, ``Time-Symmetric Boundary Conditions and Quantum Foundations,'' Symmetry 2, 272--283 (2010). <https://doi.org/10.3390/sym2010272>
- [8] K. B. Wharton and N. Argaman, ``Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics,'' Reviews of Modern Physics 92, 021002 (2020). <https://doi.org/10.1103/RevModPhys.92.021002>
- [9] M. J. W. Hall, ``Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence,'' Physical Review Letters 105, 250404 (2010). <https://doi.org/10.1103/PhysRevLett.105.250404>
- [10] M. S. Leifer and M. F. Pusey, ``Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?,'' Proceedings of the Royal Society A 473, 20160607 (2017). <https://doi.org/10.1098/rspa.2016.0607>
- [11] C. J. Wood and R. W. Spekkens, ``The Lesson of Causal Discovery Algorithms for Quantum Correlations,'' New Journal of Physics 17, 033002 (2015). <https://doi.org/10.1088/1367-2630/17/3/033002>
- [12] G. W. Ford, M. Kac, and P. Mazur, ``Statistical Mechanics of Assemblies of Coupled Oscillators,'' Journal of Mathematical Physics 6, 504--515 (1965). <https://doi.org/10.1063/1.1704304>
- [13] H. Mori, ``Transport, Collective Motion, and Brownian Motion,'' Progress of Theoretical Physics 33, 423--455 (1965). <https://doi.org/10.1143/PTP.33.423>
- [14] R. Zwanzig, ``Nonlinear Generalized Langevin Equations,'' Journal of Statistical Physics 9, 215--220 (1973). <https://doi.org/10.1007/BF01008729>
- [15] B. Jamison, ``Reciprocal Processes,'' Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 30, 65--86 (1974). <https://doi.org/10.1007/BF00532864>
- [16] J. L. Doob, ``Conditional Brownian Motion and the Boundary Limits of Harmonic Functions,'' Bulletin de la Société Mathématique de France 85, 431--458 (1957). <https://doi.org/10.24033/bsmf.1495>
- [17] R. Landauer, ``Irreversibility and Heat Generation in the Computing Process,'' IBM Journal of Research and Development 5, 183--191 (1961). <https://doi.org/10.1147/rd.53.0183>
- [18] C. H. Bennett, ``The Thermodynamics of Computation: A Review,'' International Journal of Theoretical Physics 21, 905--940 (1982). <https://doi.org/10.1007/BF02084158>
- [19] T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). <https://doi.org/10.1103/PhysRevA.49.1613>
- [20] H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). <https://arxiv.org/abs/2309.10969>
- [21] H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). <https://arxiv.org/abs/2406.04571>
- [22] N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). <https://doi.org/10.1119/1.3456564>
- [23] S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). <https://doi.org/10.3389/fphy.2020.00139>
- [24] G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). <https://doi.org/10.1007/978-3-319-41285-6>
- [25] C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). <https://doi.org/10.3934/dcds.2014.34.1533>
- [26] Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). <https://doi.org/10.1007/s10957-015-0803-z>
- [27] H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). <https://doi.org/10.2514/3.3166>
- [28] J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). <https://doi.org/10.1209/0295-5075/113/60009>
- [29] M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). <https://doi.org/10.1088/1751-8121/ab7cfe>
- [30] J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). <https://doi.org/10.1063/5.0207422>
- [31] J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). <https://jmlr.org/papers/v22/20-1260.html>
- [32] C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). <https://doi.org/10.1214/13-PS220>
- [33] M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). <https://doi.org/10.1103/PhysRevE.83.061112>
- [34] A. Heslot, ``Quantum Mechanics as a Classical Theory,'' Physical Review D 31, 1341--1348 (1985). <https://doi.org/10.1103/PhysRevD.31.1341>
- [35] J. S. Briggs and A. Eisfeld, ``Coherent Quantum States from Classical Oscillator Amplitudes,'' Physical Review A 85, 052111 (2012). <https://doi.org/10.1103/PhysRevA.85.052111>
- [36] J. S. Briggs and A. Eisfeld, ``Quantum Dynamics Simulation with Classical Oscillators,'' Physical Review A 88, 062104 (2013). <https://doi.org/10.1103/PhysRevA.88.062104>
- [37] T. E. Skinner, ``Exact Mapping of the Quantum States in Arbitrary N-Level Systems to the Positions of Classical Coupled Oscillators,'' Physical Review A 88, 012110 (2013). <https://doi.org/10.1103/PhysRevA.88.012110>
- [38] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, ``Experimental Realization of Any Discrete Unitary Operator,'' Physical Review Letters 73, 58--61 (1994). <https://doi.org/10.1103/PhysRevLett.73.58>
- [39] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, ``Optimal Design for Universal Multiport Interferometers,'' Optica 3, 1460--1465 (2016). <https://doi.org/10.1364/OPTICA.3.001460>
