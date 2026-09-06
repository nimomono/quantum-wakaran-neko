@number: 8
@chapter: 本文
@title: 誤差、資源、反証条件、未完成目標
@status: M54から派生するQ1/Q2 static profileとQ3 spatial profile、R180 receiver、M37 backendを横断比較し、R161/R162、R181A--R181D、有限資源、反証条件、未完成目標を整理する。

## 8.1 誤差を1回だけ数える規約

上流の物理偏差を複数の結果式へ伝播させる場合、最初に現れる誤差項へだけ入れる。特に次を禁止する。

1. 同じM37包絡誤差をR135の第2モーメント誤差とR168のray誤差へ同時に加える。
2. R164の有限幅・枝非対称誤差を、R170の作用殻誤差と系列固有instrument誤差へ重ねて入れる。
3. R180Aの同じblock保持偏差を $\varepsilon_{\rm split}$、$\varepsilon_{\rm latch}$、$C_\tau\varepsilon_{\rm block}$ へ重ねて入れる。
4. R180Cの積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。
5. 無反応質量を理想分布差と実装失敗へ2回加える。
6. M54の同じtransverse偏差をR181Aのray誤差、R135の初期共分散誤差、系列固有準備誤差へ重ねて入れる。

全ての理想分布と実分布は同じ完全結果集合へ埋め込む。成功試行だけで再規格化しない。

## 8.2 M54/R181A共通開放準備の誤差と資源

M54の安全事象を $G_*$、$q_*=(R_*^2-a_*^2)/a_*^2$ とする。準備切断面の上流誤差を

```math
\varepsilon_{54}
\leq
\varepsilon_{\rm seed}
+\varepsilon_{\rm ray}
+\varepsilon_{\rm cut},
```

```math
\varepsilon_{\rm seed}=P(G_*^c),
\qquad
\varepsilon_{\rm ray}
\leq
\sqrt{q_*}e^{-\kappa\tau_{\rm prep}}
```

と分ける。$\varepsilon_{\rm seed}$ は完全結果集合の無反応質量、$\varepsilon_{\rm ray}$ は安全試行の方向誤差、$\varepsilon_{\rm cut}$ はport切断とM54から下流registerへの受渡し誤差である。M54の最小方程式は雑音零なので、有限bath雑音を仮定した誤差項をここへ暗黙に入れない。

目標ray誤差 $\epsilon_{\rm p}>0$ に対し、

```math
\tau_{\rm prep}
\geq
\frac{1}{\kappa}
\log\frac{\sqrt{q_*}}{\epsilon_{\rm p}}
```

を選べる。$a_*\downarrow0$ ではseed無反応質量を減らせる場合があるが $q_*$ が増え、準備時間、動的範囲、pump作用が増える。$\kappa\to\infty$ で時間だけを縮める場合も、sink結合強度と排熱率の資源を別に数える。

R181Aが定量化するのは縮約drift後の有限時間収束である。pump仕事、sink熱、template保持、clock切替、port履歴、有限bath交換の総収支は未導出であり、$\varepsilon_{54}$ が小さいことから熱力学的コストが小さいとは結論しない。M54のray誤差をR135で伝播した後、同じ偏差をR168または系列固有誤差へ再加算しない。

## 8.3 共通R170誤差

M54 static profile固定入力時刻instrumentの共通台帳は

```math
\varepsilon_{170}
\leq
\varepsilon_{\rm hold}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
+\varepsilon_{\varnothing}
```

である。各項の意味は次の通りである。

| 項 | 物理的由来 |
|---|---|
| $\varepsilon_{\rm hold}$ | 入力時刻の信号SWAPと保持controller |
| $\varepsilon_{\rm cap}$ | 信号作用から枝容量への結合 |
| $\varepsilon_{\rm shell}$ | 作用殻有限幅、枝対称性、fiber準備 |
| $\varepsilon_{\rm mix}$ | R161の有限時間再平衡化 |
| $\varepsilon_{\rm coll}$ | R162の有限セル・有限エネルギー衝突近似 |
| $\varepsilon_{\rm lock}$ | 入射停止、辺閉鎖、枝固定 |
| $\varepsilon_{\rm rec}$ | 局所記録pointerの有限幅と時計窓 |
| $\varepsilon_{\rm clk}$ | 操作順序とパルス面積のずれ |
| $\varepsilon_{\varnothing}$ | 閾値、境界、overflowを含む無反応質量 |

混合項は

```math
\varepsilon_{\rm mix}
\leq
C_\delta e^{-\lambda_\delta\tau_X},
\qquad
\lambda_\delta
=
\kappa_Xa_{\min}
\frac{\delta q_{\min}}{1+\delta}
\lambda_G
```

で抑えられる。$\delta\downarrow0$ では一様混合率下界が $O(\delta)$ まで低下し得る。

## 8.4 Q1の系列固有誤差

R143は共通R170を初期操作面と分析器後操作面へ適用し、Q1 W型固有項を加える。

```math
\begin{aligned}
\varepsilon_{143}
\leq{}&
\varepsilon_{170}^{\rm in}
+\varepsilon_{170}^{\rm out}
+\varepsilon_{\rm Hopf}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}\\
&+
\eta_W
+\varepsilon_{\rm lock}^{W}
+\varepsilon_{\rm br}
+\varepsilon_{\rm post}.
\end{aligned}
```

$\varepsilon_{\rm Hopf}$ はR181AのW型2モード系の有限準備、$\varepsilon_{\rm ctrl}$ は傾斜制御、$\varepsilon_{2m}$ は高モード漏れ、$\eta_W$ は左右有限コントラスト、$\varepsilon_{\rm br}$ は結果別template交換、$\varepsilon_{\rm post}$ は条件付き状態更新である。

R144の固定 $N$ 段逐次測定では、各段の1段instrument誤差と段間条件付き状態誤差を有限和で抑え、無反応を含む完全履歴を $O(N)$ 個の有限record cellへ保持する。ここでは永久記録、内部逆計算、周期末resetを要求しない。これらを含む反復装置化では、使用済みcellと永久記録が周期数 $K$ に対してさらに $O(K)$ 以上増える。作用容量、fiber、Hopf pump、controller、記録、resetを同じ有限局所Hamiltonian周期へ統合し、仕事・熱・エントロピー収支を閉じることは実装・熱力学的強化課題として残るが、Q1-2の達成条件には含めない。Q1-2の固定目標上の残件は、同じ明示的ミクロモデルで零傾斜Rabi対照とR144有限段測定を接続し、全履歴と対照を保ったZeno抑制を有限誤差で示すことである。

### 8.4.1 R187のM37--W2 carrier誤差と資源

R187を使うQ1制御では、carrier側の誤差を

```math
\varepsilon_{187}
\leq
d_0
+
C_U\sqrt{r_\kappa}
+
\left(1+\varepsilon_{\rm stat}(\eta)\right)^{m_U}-1
+
\varepsilon_{\rm sw}
+
\varepsilon_{\rm cal}
```

と分ける。ここで $r_\kappa=J_\kappa/G_\kappa$、$d_0$ はR181A sourceまたは固定canonical portからM37最低2正常modeへの投入誤差、$C_U\sqrt{r_\kappa}$ は傾斜時のspectral dressing・cluster切替・dressed生成子補正、$\varepsilon_{\rm stat}$ は局所包絡と較正済み厳密正常modeの時間一様差、$\varepsilon_{\rm sw}$ はsmooth ramp近似、$\varepsilon_{\rm cal}$ は傾斜値とhold角の較正誤差である。

```math
\varepsilon_{\rm stat}(\eta)
=
\frac{2\delta_{\rm loc}(\eta)}
{1-\delta_{\rm loc}(\eta)},
\qquad
\delta_{\rm loc}(\eta)
=
(1-\eta)^{-1/4}-1.
```

各static区間では厳密M37正常mode生成子 $f_{\omega_0}(h)$ と有効W型生成子が固有ベクトルを共有するため、実hold時間を厳密低2分裂で較正する。従って長いRabi時間へR86の $T\|h\|^2/\omega_0$ 型Duhamel上界をそのまま掛けず、carrier誤差は固定有限wordの $\varepsilon_{\rm stat}$ で監査する。同じ偏差を $\varepsilon_{\rm ctrl}$、$\varepsilon_{2m}$、R135 trace誤差へ重複加算しない。

弱link $\kappa\downarrow0$ では

```math
J_\kappa=O(\kappa),
\qquad
G_\kappa\to g_*>0,
\qquad
T_U
=
O\!\left(
\frac{\mathcal J_0}{J_\kappa}
\right).
```

従って任意精度構成は有限だが、総時間は発散し得る。代表傾斜は $|F_\kappa|=O(\sqrt{J_\kappa G_\kappa})$、smooth化の一例では $\tau_{\rm sw}=O(r_\kappa^{1/4})$ の短いrampを使う。必要carrier周波数、weak-link設定精度、分裂・hold時間の相対較正精度、switch時刻分解能を別々に報告する。R187はQ1のcarrier-level実装結果であり、Q2-4の多項式外部制御条件を満たすという主張には使わない。

R187のcanonical W2 portは全mode直交変換の先頭2正準対を使い、高modeを捨てない。R181A pump/source、R164作用殻、R161/R162 collision、R170/R143記録の物理資源はこの台帳へ吸収せず、Q1測定sectorの別項として残す。

## 8.5 Q2-1の誤差と資源

M54ではtensor-lift、同じ永続registerのhold、clock、各gate、外部bathへの漏れ、末端ray、Born型instrumentを分ける。長さ $L$ の回路誤差は

```math
\varepsilon_{\rm circ}
\leq
\varepsilon_{\rm lift}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm clock}
+\sum_{r=1}^{L}\varepsilon_r
+\varepsilon_{\rm leak}
+\varepsilon_{\rm ray}
+\frac{\delta}{1+\delta}
+\varepsilon_{170}^{\rm end}
+f_\varnothing
```

とする。中間handoff、経路pairing、coherent decoderを独立項として加えない。$Z_S$ は同じregisterに留まり、R181Dは末端で同次元canonical SWAPと容量latchを使うためである。$f_\varnothing$ は最初の失敗段階ごとに排他的に数え、成功試行だけを再規格化しない。各gateはmode別誤差の粗い和でなく、状態bath全体のglobal phaseを除くoperator normで抑える。R181Dの未統合境界は $\varepsilon_{170}^{\rm end}$ の構成条件として残す。

## 8.6 Q2-2の誤差とBell監査

R180CはM54の実際の末端信号、R180Aのsetting-pre block receiver、R180Bのpaired-Hopf流、2つの局所R170を条件付き積因子化の下で合成する。設定対ごとの完全周期誤差を

```math
\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{54}^{\rm src}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{\rm latch}
+2\tau\\
&+
C_\tau\varepsilon_{\rm block}
+L_{\rm fib}K_{180}e^{-\gamma_{180}T_{\rm PH}}
+\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}\\
&+
\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}\\
&+
\varepsilon_{170,{\rm rest}}^{A}
+\varepsilon_{170,{\rm rest}}^{B}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}.
\end{aligned}
```

ここで $2\tau$ は一般状態の小作用blockを無反応へ送る切断質量、$C_\tau=O(\!\left(\tau^{-1/2}\right))$ は安全域の規格化感度である。$\varepsilon_{170,{\rm rest}}^{A,B}$ は、明示済みの正則化・有限混合と、別項の記録・clockを除いた局所R170残差であり、同じ段を二重に数えない。固定singletでは各枝作用が $1/2$ なので、$\tau<1/2$ ならnode項は零にする。理想singlet分布からの全変動距離が $\varepsilon_{180}^{\rm cyc}$ 以下なら、一側周辺の反対設定による差は $2\varepsilon_{180}^{\rm cyc}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{180}^{\rm cyc}$ 以下である。

```math
\varepsilon_{180}^{\rm cyc}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。

| Bell前提 | R180 receiverでの位置 |
|---|---|
| 切断後局所性 | R180Cの装置統合条件の下で完全共通原因へ条件付けて局所因子化 |
| 測定設定独立性 | A設定が中央準備へ入るため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻で決まる |
| 事後選別 | 無反応を完全結果集合へ残す |
| 非信号性 | 理想対称性で成立し、有限差を上の誤差で抑える |

従ってBellの定理を否定しない。自由設定、空間分離、一般状態receiverは達成範囲に含まない。

## 8.7 Q3のM54 spatial--M37 moving-matching誤差

Q3ではR164と同じ条件付き分布 $\pi^\delta(X\mid Z)$ を確率源として共有する。Q1・Q2はR161 static specialization、Q3は同じR161のmoving specializationを使う。M42/R172--R174は現行依存から退役する。

M37を使わない理想M54 spatial signal sectorではR161 moving matchingは厳密であり、背景容量は保存量 $S=Z^\dagger Z$ を使う。M37局所ばね実装では開始作用 $S_{\rm ref}=\|b(0)\|^2$ を単一試行ごとにlatchし、背景容量を $|b_i(t)|^2+\delta q_iS_{\rm ref}$ とする。局所包絡の非保存作用 $\|b(t)\|^2$ を輸送中に背景へ書き戻さない。rank-one統計から厳密な $|\psi|^2$ と比較するときだけ

```math
\varepsilon_\delta
=
\frac{\delta}{1+\delta}
```

を加える。M37局所ばね実装では

```math
\varepsilon_{\rm car\to rate}(T)
=
T L_\delta(\eta)\varepsilon_{\rm car}(T)
```

とし、

```math
\begin{aligned}
\varepsilon_{184}(T)
\leq{}&
\varepsilon_{\rm prep}
+\varepsilon_{\rm init}
+\varepsilon_\delta
+T L_\delta(\eta)\varepsilon_{\rm car}(T)\\
&+\varepsilon_{\rm step}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm over}
+\varepsilon_{\rm clk}
+\varepsilon_{\rm rec}
\end{aligned}
```

とする。同じR86偏差をR135統計診断とrate誤差へ二重加算しない。

$\Delta=\delta_{\rm loc}(\eta)$ に対し

```math
L_\delta(\eta)
=
\frac{h_1}
{\mathcal J_0(1-\Delta)^2}
\left[
\frac{
\sqrt2(1+\sqrt{1+\Delta^2})
}{
\delta q_{\min}
}
+
\frac{
2(1+\delta)
}{
\delta^2q_{\min}^2
}
\right].
```

固定有限格子では有限だが、$\delta\downarrow0$ で概ね $O(\delta^{-2})$ のrate感度が現れる。finite collision部分は付録N.4の一般有界有向率補題だけで閉じ、退役R173を現行依存に使わない。

Q3-2の理想M54 spatial層ではR185により

```math
\varepsilon_{185}^{\rm ideal}
\leq
mC_{\rm lat}a^2
+
mC_{\rm reg}(\delta)
```

と分けられ、node-free compact sectorで $C_{\rm reg}(\delta)=O(\delta)$ である。finite collision近似から $D_+D_-X$ と $D_-D_+X$ までの追加誤差 $\varepsilon_{\rm bath}^{\rm acc}$ は未導出なのでQ3-2は部分達成に留める。R184の $L_\delta\varepsilon_{\rm car}$ だけをNewton加速度誤差へ流用しない。

R124の理想トンネル型増分を $\alpha>0$、R125の理想干渉分布距離を $\Delta_{\rm int}>0$ とする。各運転の誤差が $\varepsilon_{184}$ 以下なら観測差は

```math
\alpha-2\varepsilon_{184},
\qquad
\Delta_{\rm int}-2\varepsilon_{184}
```

以上である。Q3-4AとQ3-5の条件付き達成はこの正の余裕と単一装置統合条件の下で維持する。

Q3-4BではR182の同じ静的W型過程を $0$、$T_{1/2}$、$T_{\rm per}$ の三時刻で評価し、同じM54 spatial profile粒子をR161/R184で輸送する。初期R164 matchingは一度だけ行い、終時刻に再標本化しない。M54準備、M54 spatial profile/M37 signal、初期作用殻、finite collision bath、半周期・一周期clock、終位置記録の単一装置統合を条件として残す。

## 8.8 static matchingの正則化資源発散

正則化により $\pi_i^\delta\geq\delta q_{\min}/(1+\delta)$ なので、有効自由エネルギー幅は

```math
\max_iE_i^\delta-
\min_iE_i^\delta
\leq
\Theta
\log
\frac{1+\delta}{\delta q_{\min}}.
```

同時に次の資源交換がある。

| 極限 | 必要になり得る資源 |
|---|---|
| $\delta\downarrow0$ | 有効地形幅 $O(\!\log\delta^{-1})$ |
| $\delta\downarrow0$ | 混合時間 $\Omega(\delta^{-1})$ |
| $\delta\downarrow0$ | 衝突流束 $\Omega(\delta^{-1/2})$ |
| 一様有限幅殻 | 剛性 $\Omega(\delta^{-2})$ |
| 周期数 $N$ | fresh cellと永久記録が少なくとも $O(N)$ |

有限資源を固定したまま厳密node、無期限熱化、永久記録、resetを同時に達成したとは扱わない。

## 8.9 Q2の根拠モデル、共通ハードウェア努力目標、ブラックボックス資源分類

Q2-1からQ2-4は、次の根拠モデルと根拠結果から互いに独立に判定する。独立とは他のQ2目標の達成ラベルを前提にしないという意味であり、同じ模型または部品定理を複数の目標で使うことは禁止しない。目標ごとに担体、浴、clock、準備・読出し原理が異なっても、それだけでは不達としない。

- Q2-1：M54 static profileを使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D。
- Q2-2：M54 static profileとR180 receiverを使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D、R180A--R180C。
- Q2-3：M54三部分系static profileを使う。R112、R161、R162、R164、R170、R177、R181A--R181Dを根拠とする。
- Q2-4：M54を使う。根拠結果はR112、R161、R162、R164、R170、R181A--R181D、R178D、R179、R186。

規模 $N$ ごとの一様な共通ハードウェア族へ統合することは、固定目標の達成条件ではなく実装努力目標である。将来これを主張する場合は、同じ物理port、永続状態浴、相互作用区間族、clock・制御bus、準備interface、Born型読出し・記録interfaceを共有する具体的な装置族を示す。共通の正準代数またはinstrument契約だけでは同一装置とみなさない。

Q2-4ではblack-box operational resourceとreported internal resourceを分ける。外部から装置を利用するためのprogram、制御、時間、精度、試行回数は前者として多項式上界を要求する。受動的な浴自由度、正準対、coherent経路、静的結合、状態容量、受動並列度、装置体積、総bath容量、総熱は後者として規模を報告し、一様な有限規則から生成する限り指数的でもよい。ただし内部資源が外部interfaceへ露出した次の操作はreported internal resourceには残さない。

1. 各モードを個別に初期化、設定、較正、同期、リセットする操作。
2. 指数個の係数、配線、時刻窓、結果枝を外部から指定すること。
3. 回路ごとの物理的な配線変更、全モード走査、全枝読出し。
4. 指数的に細かい精度、小さい成功率、長い準備・混合・実行時間。

Q1とQ2はM54の同じ完全状態型と外部interfaceから派生する。ただし全規模で同じ製造済みハードウェアを共有するところまでは統合していない。この未完成性は個別達成判定を変更しない。R180CはM54末端から2翼記録までのreceiver内部統合をQ2-2自身の条件とする。

## 8.10 Q2-3の3量子ビット型二段ゲート合成

3つのQ1型、すなわち2状態の論理部分系を $A,B,C$ とし、2つの2量子ビット型結合ゲートを $A$--$B$、続いて $B$--$C$ へ作用させる。ここでQ1型とは論理状態空間を指し、3台のQ1 W型2モードprotocol装置またはQ1との共通ハードウェアを要求する語ではない。最小検査列の一つは

```math
|+\rangle_A|0\rangle_B|0\rangle_C
\longmapsto
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|111\rangle}{\sqrt2}.
```

R181Bをgate列の前に2回作用させて $a\otimes b\otimes c$ を作り、第1ゲート後も同じM54永続状態bathを保持する。枝を測定せず、共同momentから新しい入力を再準備しない。さらにAへ $T=\operatorname{diag}(1,e^{i\pi/4})$ を作用させ、2つのゲートと最初のHadamardを逆順に戻す。R177の理想coherent出力は

```math
P(000)=\cos^2\frac{\pi}{8},
\qquad
P(100)=\sin^2\frac{\pi}{8},
```

完全dephasing出力は両者が $1/2$ であり、全変動距離は $1/(2\sqrt2)$ である。coherent側と混合側の装置誤差の和がこの値未満なら正の識別余裕が残る。

R181Bは3入力の有限tensor-lift、R181Cは同じ8mode register上の2つの二次gate zoneと逆演算、R177は上の識別余裕を与える。R181Dが末端Born型instrumentへの条件付き接続を与えるため、Q2-3は条件付き達成である。残る条件は容量pointer--作用殻境界、有限fiber混合の枝対称性、SWAPから記録までの単一clock統合である。8modeが受動的に存在すること自体は失敗条件ではない。失敗条件は中間で統計量へ縮約して再準備すること、または各modeを外部から個別に初期化、較正、同期、address、読出し、resetすることである。

## 8.11 Q2-4多項式外部制御による量子出力サンプリング

Q2-4では、固定有限普遍ゲート集合から与えられる $n$ 量子ビット・深さ $d$ の回路について、全gateを終えた回路末尾から1つの出力標本を生成する。古典装置の結果空間は

```math
\{0,1\}^n\cup\{\varnothing\}
```

とし、$\varnothing$ は無反応または失敗を表す。量子回路の目標分布にも零重みの $\varnothing$ を加え、同じ完全結果空間上の全変動距離を $\epsilon$ 以下にする。成功試行だけを再規格化しない。

次を個別に $\operatorname{poly}(n,d,1/\epsilon)$ で抑える。

1. 回路記述、コンパイル時間、外部プログラム、外部指定係数の個数とbit記述長。
2. 外部制御channel数、ゲート命令数、制御列長、addressするport数。
3. 準備、初期化、実行、混合、測定、記録、必要な場合のリセットを含む総時間。
4. 外部制御のエネルギー、作用、結合強度、周波数、動的範囲。
5. 制御、初期化、時刻、読出しの精度と、それを指定するbit数。
6. 外部から個別にaddress、設定、較正、回収するcell、履歴、記録、仕事、排熱portの個数。受動bank内部のcell総数と総熱はここへ含めない。
7. 無反応・失敗確率と期待試行回数。

一方、signal、anti-register、work、history、cold、spentを含む指数的な受動自由度と受動状態容量を許す。装置体積、総bath容量、総熱は指数的でもよい。これは通常の意味の効率的古典simulationを主張する基準ではない。

この資源規約は内部costを無視するためではなく、比較対象をblack-box operational complexityへ固定するためのものである。内部mode数、静的coupler数、装置体積、総熱は別のreported internal resourceとして保持する。量子計算機と同等の総物理資源効率は主張しない一方、内部の指数構造がmode別較正、指数精度、指数時間、指数試行回数として外部へ露出する場合はQ2-4の失敗とする。

M54は $L=2^n$ 個のsignal modeを使うが、R181Cにより固定有限局所gateをspectator sectorへ同じ係数でbroadcastし、作用素norm誤差をsector数の和ではなく最大値で抑える。R181Dは各bitでraw容量 $J_{u,b}$ とregularized容量 $A_{u,b}^\delta$ を分け、R164/R170でselectorを形成してから可逆filterを開く。確率 $\tau$ 未満の枝とguardを $\varnothing$ に残すため、切断誤差は $2n(\tau+\gamma)$ 以下であり、事後選別を使わない。

選択成分はR181Aのradial-only portで標準作用へ戻す。未知の条件付き確率を読み出すsqueezeではなく、$\tau$ の下限から固定repump時間を選ぶ。深さ $n$ の完全結果誤差は入力誤差、$n\delta/(1+\delta)$、$2n(\tau+\gamma)$、各node実装誤差の和で抑える。R178DはHamiltonian workだけの逆掃除と、結果・開放散逸履歴をspent側へ残す境界を与える。

R179は同一静的couplerと受動clockによるpartial SWAPを反復し、active残差を幾何的にaggregate cold floorまで縮める。root source、R162 collision cell、selector、filter workをbankから供給し、使用済み状態をspentへ送る。旧fair-bit、dyadic threshold、aperture tapeは現行因果鎖に使わない。

R186はこのblack-box規約に対する製造誤差とnoiseの境界を与える。疎な静的coupler誤差はprojective operator normで、独立mode phase noiseは平均fidelityで、projector latchの相対係数誤差は容量の相対誤差で評価でき、いずれもsector数の粗い和を取らない。一方、各modeへ信号振幅と無関係なadditive作用を注入し $Q_{\rm add}\succeq\sigma^2I_{2^n}$ となる場合は、横方向noise作用が $(2^n-1)\sigma^2$ に比例する。poly signal作用とpoly時間のまま精度を保つには指数noise suppressionが必要となるため、現在のM54 direct-mode実装に対する障害条件である。

以上は各構成部品と合成誤差・資源の定理を与える。ただし、静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、実際の製造ばらつきと運転中noiseがR186の正の頑健性条件を満たしてextensive additive-noise障害を回避することが残る。この条件の下でQ2-4を条件付き達成とする。

## 8.12 反証条件

現行主張は次の検査に失敗した場合に縮小または撤回する。

| 対象 | 反証条件 |
|---|---|
| M54/R181A | 実変数driftと複素式が一致しない、安全seed上のray距離が指数上界を破る、無反応質量を落とさずM54 static分布へ接続できない |
| Q1 W型2モードprotocol/R143 | Hopf方向が有限時間で準備できない、R170特殊化後もBorn型枝と局所記録が一致しない、結果別状態更新が失敗する |
| M54/R181B--R177 | tensor-liftの正規化または正準性が破れる、集団momentから再準備する、同じregisterを保持できない、参照系相関または逆演算fringeが壊れる、各modeの個別外部制御が必要、R181Dの完全結果誤差境界を満たさない |
| M54/R180A--R180C | 実際の末端信号でなく集団momentを再注入する、block作用と枝重みが一致しない、paired-Hopf流が選択templateへ吸引しない、R180Cの単一装置境界を満たさない、切断後因子化が破れる、局所R170応答が反対翼設定を参照する、無反応込みでCHSH誤差上界を満たさない |
| M54/R181A--R181D・R178D・R179・R186 | sectorごとの誤差を指数個へ粗く加算する、selector lock前にfilterを開く、projector filterが正準でない、希少枝を事後除外する、状態依存除算または確率依存squeezeを使う、使用済みcellを履歴なしにblankへ戻す、単一の一様装置族へ統合できない、または実装noiseがR186のextensive additive-noise障害を回避せず指数精度を要求する |
| M37/R86・R135 | 有限時間包絡上界または第2モーメント持上げ上界を超える |
| R182 | W型固定低位スペクトル・密度・節が格子収束しない、Rayleigh十分条件から障壁下二重項が得られない、functional calculusの共有固有空間または分裂相対上界を破る、中央障壁込み半周期鏡映・一周期回帰が成立しない |
| M54 spatial/R161--R184 | 局所master方程式がM37辺流を再現しない、正則化全変動上界を破る、有限衝突近似が安全領域で収束しない、終時刻に同じ粒子を記録できない |
| Q3-2 | 目標とする作用または時間対称Newton則を縮約前に仮定する、外部から仮定したSchrödinger方程式を書き換えるだけで済ませる、前進・後退平均微分と誤差を同じ確率過程上で定義できない |
| Q3-3C | W型低位スペクトルの格子・領域収束を示せない、または同じ固有基底の有限環境純位相緩和と対角占有率保存を閉じられない |
| Q3-4B | 2モード作用比を空間領域占有率へ同一視する、外部駆動・傾斜切替・障壁低下を使う、最低二重項の障壁値未満条件、第3状態との間隔、半周期移送、一周期回帰、位置読出しのいずれかを欠く |
| Q3-6 | 単価性または整数巻数を外部条件として置く、非整数モノドロミーを丸めて除く、節を介した位相すべりと細分化安定性を同じ構成で扱えない |
| R168 | 可変作用集団でray平均を第2モーメントへ補正なしに置換する、安全事象外を再規格化して消す |
| R170 | 混合上界、局所記録の排他性、履歴単射性、正の処理時間のいずれかを満たさない |
| Q2共通ハードウェア努力目標 | 同一装置を主張しながら目標ごとに担体、浴、準備・読出し原理を交換する、または装置族を一様な有限規則で生成できない |
| Q2-3二段ゲート合成 | 第1ゲート後の単一試行状態を破壊せず第2区間へ渡せない、中間共同モーメントから再準備する、GHZ--$T$--逆演算の $1/(2\sqrt2)$ 余裕が全装置誤差を上回らない |
| Q2-4 | 受動モードごとの設定・較正・読出し、指数長の係数表、回路別配線、指数時間または指数精度が必要になる。総bath容量と総熱が指数的であることだけでは反証にならない |

数値的一致だけで厳密結果を宣言せず、解析上界と独立に回帰検査する。

## 8.13 固定目標の残件と実装強化課題

固定目標上の未完成事項は次である。

1. Q1-2について、同じ零傾斜Rabi対照と反復R143/R170測定を接続し、全履歴、tilt対照、有限誤差、資源を含む正のZeno抑制余裕を示す。
2. Q3-2について、M54 spatial profile--M37--有限衝突bathの縮約から、前進・後退平均微分を持つ同じ確率過程と、Nelson流の作用変分または時間対称Newton則を有限時間誤差付きで導く。
3. Q3-6について、閉路巻数、homotopy不変性、節を介した位相すべり、R86細分化安定性、非整数seamのエネルギー発散を統合する。
4. Q2-1について、R181Dの容量pointer--作用殻境界、有限fiber混合、固定、記録を単一clock scheduleで閉じる。
5. Q2-3について、同じR181D末端条件を8mode特殊化で閉じ、R177の識別余裕より小さい全装置誤差を選ぶ。
6. Q2-4について、M54の静的sector配線、projector latch、R170 collision、selector lock、controlled filter、radial repump、blank/spent bank、clockを一つの具体的な一様装置族へ統合し、各局所誤差の独立な物理上界を与える。

次は固定目標の達成判定と分けて管理する実装・熱力学的強化課題である。

1. M54のpump、transverse sink、template、clockを有限bath、仕事源、排熱先へ持ち上げ、雑音と準備誤差と総収支を同じ模型で閉じる。
2. R170の作用容量結合、作用殻fiber内平衡化、信号保持、衝突bath、枝固定、記録をQ1・Q2の1つの有限局所Hamiltonianへ統合する。
3. Q1 W型2モードprotocolのM54準備から結果別状態更新、永久記録、resetまでの周期総収支を閉じる。
4. R180CのM54末端SWAP、setting-pre block latch、paired-Hopf pump・sink、中央切断、2翼局所R170、controller、fresh cell流を同じ具体装置とclockへ統合する。
5. Q3-4A・Q3-4B・Q3-5でM54切断面、M37担体、初期作用殻、M54 spatial profile局所辺bath、clock、終位置記録までを同じ有限局所装置へ統合する。Q3-4Bでは半周期・一周期のclock精度も同じ装置台帳に含める。
6. 連続空間、多粒子を扱う。
7. Q2共通ハードウェア努力目標として、同じ物理port、永続状態浴、相互作用区間族、制御bus、準備・読出しinterfaceをQ2-1からQ2-4で共有する一様な装置族を得る。

Q1-1、Q3-1、Q3-3A、Q3-3B、Q3-3Cは達成、Q1-2とQ3-2は部分達成、Q2-1、Q2-2、Q2-3、Q2-4、Q3-4A、Q3-4B、Q3-5は条件付き達成、Q3-6は未達である。Q2-1とQ2-3の条件はR181Dの末端物理接続、Q2-2の条件はR180Cのreceiver内部単一装置統合、Q2-4の条件はM54部品の一様装置統合へ集約される。Q2共通ハードウェア族は判定外の努力目標として未完成であり、その成否を個別判定へ遡及させない。

## 8.14 M37からQ1制御へ進む強化課題

新しい主線はM37、W型低2モード、Q1制御の順とする。固定目標の定義やQ2依存関係は変更しない。静的R86と射影内R140の既存達成に加え、第6.17節の区間合成と第3.5.1節の残差を同じ時間窓で閉じる必要がある。

| 誤差・資源 | 数える対象 |
|---|---|
| 包絡誤差 | 全定傾斜区間と有限切替。再準備で区間誤差を消さない |
| 低モード状態誤差 | 漏れ振幅と低モード内位相補正。漏れ確率の二乗評価と区別 |
| 制御誤差 | 合成角、時刻、切替幅、作用の変動、準備誤差 |
| 入力一様性 | 相対位相と初期共通位相を含む実線形写像のノルム |
| 資源 | 全Rabi時間、carrier周波数、間隔、結合強度、制御帯域、外部仕事 |

B.5の漏れ確率を全変動距離へ直接加える旧評価は採用しない。R143の誤差和では、実際の全状態または分布比較を満たす $\varepsilon_{2m}$ を使う。理想2準位担体のQ1-1達成と、全W型・M37実装の任意精度強化は分ける。全W型測定の誤差予算もこの追加条件に依存する。

優先順は、物理係数の対応、静的Rabi、有限傾斜列、準備・読出し境界、共同担体への接続、同一装置の統合である。ゲート列からの有効伝播は補助実装として研究メモで管理し、Q3全過程の独立導出とは呼ばない。