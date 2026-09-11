# 退役したR190--R170作用殻型測定経路

このメモは、draft-88でR191がQ1/Q2の2結果射影読出しを直接担うようになった後も本文に残っていたR190A--R190CとR170の旧主線を保存する。今回の縮約では、固定Q1/Q2の必須因果鎖から外し、Q3の初期配置はR164、反復装置のopen resetはR179、2結果読出しはR191へ責務を分離した。

ここに保存する定理は反証されたものではない。2作用LC殻、Drude混合、対称作用開口、静的吸収pointerという別の物理実現候補として、比較・将来拡張用に保持する。現行Q1/Q2の誤差予算へ重複加算しない。

### 2.8.1 R190A--R190C：2作用LC殻Drude混合と静的平方根衝突接続

R164だけからR161静的特殊化の平方根分割は一意に従わない。ここでは、固定済み正作用容量を2作用LC殻へ渡し、無限自由度の等方Drude浴で作用分配だけを混合した後、対称な作用開口を使う一つの具体的十分条件を与える。R190系列はR162を置き換えず、静的 $j=0$ の平方根率に対する作用殻明示表示の物理接続だけを担う。

<!-- theorem-start:theorem -->
**定理（R190A：2作用LC殻の作用保存型Drude混合）**

固定済み正作用容量 $\widehat A_i>0$ を取り、2つの同周波数LCモードの作用を $K_i,I_i\geq0$ として

```math
K_i+I_i=\widehat A_i
```

とする。対応するSchwinger型作用方向を $\boldsymbol n_i\in S^2$ とし、各生成子成分へ同型な無限古典調和浴をcounterterm込みで結合する。浴の記憶 核を

```math
\Gamma_{\rm D}(t)
=
\frac{g_{\rm D}}{\tau_{\rm D}}
e^{-t/\tau_{\rm D}},
\qquad
g_{\rm D}>0,
\quad
\tau_{\rm D}>0
```

とし、初期浴を固定した作用方向に条件付けたFDT整合Gaussian平衡状態から取る。

このとき全拡大Hamiltonian軌道で

```math
K_i(t)+I_i(t)=\widehat A_i
```

が厳密に保存される。浴自由度を消去した縮約運動は指数記憶を持つ一般化Langevin方程式であり、reaction variableを加えると有限次元のDrude fast--slow系へ書き直せる。

その短記憶極限を回転拡散係数 $D_{\rm rot}>0$ の球面拡散 $\boldsymbol N_t$、

```math
\operatorname{Gen}(\boldsymbol N)
=
D_{\rm rot}\Delta_{S^2}
```

とする。固定有限時間 $T$ では、同一Brownian運動上のcouplingを選んで

```math
W_1
\left(
\mathcal L(\boldsymbol n_i^{\tau_{\rm D}}(T)),
\mathcal L(\boldsymbol N_T)
\right)
\leq
C_{\rm str}
\left(
g_{\rm D},
D_{\rm rot}T
\right)
\sqrt{
D_{\rm rot}\tau_{\rm D}
}
```

とできる。$C_{\rm str}$ の一つの保守的明示式は付録Sに置く。有限長・有限モード浴への持ち上げは本定理の主張に含めない。
<!-- theorem-end:theorem -->

<!-- theorem-start:lemma -->
**補題（R190B：2作用分配の有限時間一様化）**

```math
X_i
=
\frac{I_i}{\widehat A_i}
=
\frac{1-n_{i,z}}2
\in[0,1]
```

とする。R190Aの理想回転拡散極限では

```math
\mathcal L_X
=
D_{\rm rot}
\left[
x(1-x)\partial_x^2
+
(1-2x)\partial_x
\right]
```

であり、唯一の定常分布は $U[0,1]$、スペクトルギャップは $2D_{\rm rot}$ である。$S=D_{\rm rot}T$、$q=e^{-4S}$ とすると任意の初期作用分配について

```math
D_{\rm TV}
\left(
\mathcal L(X_i(T)),
U[0,1]
\right)
\leq
\varepsilon_{\rm mix}^{190}(S)
:=
\min
\left\{
1,
\frac{\sqrt{q(3-q)}}{2(1-q)}
\right\}.
```

有限記憶 Drude系では

```math
W_1
\left(
\mathcal L(X_i^{\tau_{\rm D}}(T)),
U[0,1]
\right)
\leq
\eta_{190}(T),
```

```math
\eta_{190}(T)
=
\frac12
C_{\rm str}
\left(
g_{\rm D},
D_{\rm rot}T
\right)
\sqrt{
D_{\rm rot}\tau_{\rm D}
}
+
\varepsilon_{\rm mix}^{190}
\left(
D_{\rm rot}T
\right).
```

従って

```math
\sup_{0\leq x\leq1}
\left|
P
\left(
X_i^{\tau_{\rm D}}(T)\leq x
\right)
-
x
\right|
\leq
\sqrt{2\eta_{190}(T)}.
```
<!-- theorem-end:lemma -->

<!-- theorem-start:theorem -->
**定理（R190C：対称作用開口から静的平方根核への接続）**

正作用容量 $\widehat A_i,\widehat A_j>0$ と対称開口定数 $c_{ij}^{\rm ap}=c_{ji}^{\rm ap}>0$ を固定し、

```math
0
\leq
\alpha_{ij}
:=
c_{ij}^{\rm ap}
\sqrt{
\frac{\widehat A_j}{\widehat A_i}
}
\leq1
```

とする。結果成分 $i$ の混合作用 $I_i=\widehat A_iX_i$ に対し、理想通過条件を

```math
I_i^2
<
\left(
c_{ij}^{\rm ap}
\right)^2
\widehat A_i\widehat A_j
```

とする。R190Bの混合窓後に作用する有限Hamiltonian scattererの通過・反射誤差を $\varepsilon_{\rm sc}$ とすれば、

```math
\left|
P(i\to j)
-
c_{ij}^{\rm ap}
\sqrt{
\frac{\widehat A_j}{\widehat A_i}
}
\right|
\leq
\sqrt{
2\eta_{190}(T)
}
+
\varepsilon_{\rm sc}.
```

理想極限では

```math
\widehat A_iP(i\to j)
=
\widehat A_jP(j\to i)
=
c_{ij}^{\rm ap}
\sqrt{
\widehat A_i\widehat A_j
}.
```

特に $\widehat\pi_i=\widehat A_i/\sum_k\widehat A_k$ とし、試行 frequency $\nu_{ij}$ を

```math
\nu_{ij}c_{ij}^{\rm ap}
=
\kappa_Xa_{ij}
```

と校正すれば、各試行前の履歴条件付き作用比分布が同じ再混合誤差内にある場合に

```math
k_{i\to j}
=
\kappa_Xa_{ij}
\sqrt{
\frac{\widehat\pi_j}{\widehat\pi_i}
}
```

というR161静的平方根率を有限条件付き核誤差で回収する。反復衝突列のMarkov化にはこの履歴条件付き再混合を別条件として要求し、R190A--R190Cだけから独立同分布のfreshnessを主張しない。
<!-- theorem-end:theorem -->

完全証明、$C_{\rm str}$、Jacobi縮約、CDF評価、作用開口scatterer、反復時の再混合条件、正則化資源は付録Sに置く。R162の一般有向率、有限骨格全履歴、時間依存率、非零確率流、Q3移動特殊化は従来どおりR162が担う。

## 2.9 R170：固定作用容量入力の静的選択・吸収指針変数固定

R170を、一般有限結果集合、作用殻型の代替経路、Q3固定時刻診断で共有する静的選択・固定の正本として残す。Q1/Q2の2結果射影ノードではR191を主読出しとし、R170と同じ誤差を二重計上しない。R170を用いる代替経路では、上流が正の固定済み作用容量 $\widehat A_i$ を保持し、R164/R190/R179が与える静的選択過程を有限時間走らせる。選択分布が目標容量比へ近づいた後は選択浴を切り、結果を開放吸収指針変数へ写して固定する。有限閉鎖Hamiltonianで入射停止、辺閉鎖、平坦域保持、全微視的履歴の1対1保存まで構成することはR170の必要条件にしない。

<!-- theorem-start:theorem -->
**定理（R170：固定作用容量入力の静的選択・吸収指針変数固定）**

有限結果集合 $\mathcal I$ に対して

```math
\widehat A_i>0,
\qquad
\widehat\pi_i
=
\frac{\widehat A_i}{\sum_j\widehat A_j}
```

を固定する。時刻 $t_s$ で静的選択変数 $X$ が

```math
D_{\rm TV}
\left(
\mathcal L(X_{t_s}),
\widehat\pi
\right)
\leq
\varepsilon_{\rm sel}
```

を満たすとする。$t_s$ で選択浴を切り、指針変数 $Y\in\{\varnothing\}\cup\mathcal I$ を $Y=\varnothing$ から開始する。固定区間では現在の $X=i$ に対して $\varnothing\to i$ だけを共通捕獲率 $\gamma>0$ で許し、一度 $Y=i$ になった後は吸収状態とする。

固定時間 $T_L$ の後、

```math
P(Y=\varnothing)
=
e^{-\gamma T_L}
```

であり、指針変数の有限漏れまたは捕獲実装誤差を $\varepsilon_{\rm ptr}$ とすれば

```math
D_{\rm TV}
\left(
\mathcal L(Y),
\widehat\pi
\right)
\leq
\varepsilon_{\rm sel}
+
e^{-\gamma T_L}
+
\varepsilon_{\rm ptr}.
```

安全な吸収状態 $Y=i$ は後段の記録、制御付き射影選別機構、転送を直接制御できる。外部記録はR112または系列固有機構、容量生成と保持はR181D、R189A、R180Aなどの上流結果が担い、同じ偏差をR170へ重複加算しない。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

**系（R170選択結果の局所記録）**

R170の吸収指針変数をR112または系列固有記録機構へ誤差 $\varepsilon_{\rm rec}$ 以内で写すと、外部観測分布の全変動誤差は

```math
\varepsilon_{170}^{\rm obs}
\leq
\varepsilon_{\rm sel}
+
e^{-\gamma T_L}
+
\varepsilon_{\rm ptr}
+
\varepsilon_{\rm rec}
```

で抑えられる。記録は固定済み結果のデータ処理であり、Born型重みを新たに生成しない。

**系（共通選択・記録安定性）**

理想分布 $p,p'$ と実分布 $q,q'$ が $D_{\rm TV}(q,p)\leq\varepsilon$、$D_{\rm TV}(q',p')\leq\varepsilon'$ を満たせば

```math
D_{\rm TV}(q,q')
\geq
D_{\rm TV}(p,p')-\varepsilon-\varepsilon'.
```

従って理想分布間の分離が誤差和より大きければ、開放指針変数固定後にも区別可能性が残る。この系をR124/R125の識別とR180CのBell監査へ共通に用いる。
