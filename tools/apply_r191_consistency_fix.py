#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, new: str, label: str) -> str:
    pattern = re.compile(rf"(?ms)^{re.escape(start)}\n.*?(?=^{re.escape(end)}\n)")
    out, count = pattern.subn(new.rstrip() + "\n\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"{label}: section replacement count={count}")
    return out


NEW_A16 = r'''@number: P
@chapter: 付録
@title: M54段階的射影選別と測定後状態受渡し
@status: R181Dが共通射影作用保持機構、R191の2結果選択・吸収記録、可逆選別機構、必要な方向を変えない振幅再調整、階数1の測定後状態受渡しを段階的に合成し、完全結果誤差と資源境界を証明する。R164/R190/R170の作用殻型経路は代替実現として別に扱う。

## P.1 目的と節点状態

深さ $m$ の二分段階的射影選別を考える。節点 $u\in\{0,1\}^{k-1}$ の入力記憶部を $Z_u\neq0$、2子への直交射影を $P_{u,0},P_{u,1}$ とする。

```math
P_{u,0}+P_{u,1}=I,
\qquad
P_{u,0}P_{u,1}=0.
```

未処理射影作用を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
=\mathcal J_0Z_u^\dagger Z_u
```

とする。節点の能動状態には信号 $Z_u$、2個の作用保持指針変数、R191のブラウン巨視的スピン、吸収記録 $Y$、選別機構用作業領域、必要なら方向を変えない振幅再調整接続端を含める。R191の混合・decision浴、R179の流出／リセット浴は環境接続部として別に扱い、解析上のBorn確率を制御器へ書き込まない。

R164/R190/R170の正則化作用殻は一般有限結果集合または独立な作用殻型代替実現にだけ用い、本節のR191主線と同じ試行で重複使用しない。

## P.2 R191節点契約と端点dispatcher

結果 $0$ をR191の $+$、結果 $1$ を $-$ に対応させ、

```math
S=J_{u,0}+J_{u,1},
\qquad
D=J_{u,0}-J_{u,1}
```

を作用和・作用差transducerへ渡す。実装値 $\widehat S,\widehat D$ から

```math
\widehat u_*=-\frac{\widehat D}{\widehat S},
\qquad
\widehat p_{u,0}=\frac{1-\widehat u_*}{2},
\qquad
\widehat p_{u,1}=\frac{1+\widehat u_*}{2}
```

を解析上定める。理想重み $p_{u,b}=J_{u,b}/J_\Sigma$ との偏差はR191の

```math
|\widehat u_*-u_*|\leq\varepsilon_u
```

から各成分で高々 $\varepsilon_u/2$ である。

固定閾値 $0<\tau_{\rm cut}\leq1/2$ を取り、$\min_b\widehat p_{u,b}<\tau_{\rm cut}$ なら大きい側を決定論的端点経路へ送り、それ以外はR191の混合--decision--捕獲を走らせる。保護帯、有限温度retreat、有限時間未捕獲はR191の完全結果誤差 $\varepsilon_{191,k}$ に含め、成功結果だけを再規格化しない。

```math
\tau_{\rm state}
:=
\tau_{\rm cut}-\frac{\varepsilon_u}{2}>0
```

を仮定すれば、無反応でない選択結果 $b$ の理想作用重みは

```math
p_{u,b}\geq\tau_{\rm state}
```

である。これは後段の射影選別機構に必要な状態方向Lipschitz下限をR191のdispatcherから直接供給する。

## P.3 R191吸収記録と可逆選別機構

R191が有限decision時間後に $Y=b\in\{0,1\}$ を吸収記録へ固定したときだけ、信号と未使用作業領域上の選別機構

```math
F_{u,b}
=
\begin{pmatrix}
P_{u,b}&P_{u,1-b}\\
P_{u,1-b}&-P_{u,b}
\end{pmatrix}
```

を開く。直交性から

```math
F_{u,b}^\dagger F_{u,b}=I,
\qquad
F_{u,b}^2=I,
```

かつ

```math
F_{u,b}(Z_u,0)
=(P_{u,b}Z_u,P_{u,1-b}Z_u)
```

である。非選択成分を消去せず作業領域へ保持するので、選別機構自体はユニタリな実正準写像である。R191が無反応を返した場合は $F_{u,0},F_{u,1}$ のどちらも作用させない。

## P.4 選別機構誤差と条件付き状態方向

理想選択成分を $v=P_{u,b}Z_u$、実装後を $\widetilde v$ とし、

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|.
```

P.2から無反応でない安全結果では

```math
\|v\|
\geq
\sqrt{\tau_{\rm state}}\,\|Z_u\|.
```

$\eta_F<\sqrt{\tau_{\rm state}}$ なら規格化写像のLipschitz評価により

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{2\eta_F}
{\sqrt{\tau_{\rm state}}-\eta_F}
=:\varepsilon_{\rm proj}.
```

この下限は物理的な状態依存除算ではない。R191の固定dispatcherパラメータとtransducer誤差上界から解析的に得る安全集合境界である。

## P.5 階数1 射影子の測定後状態の受け渡し

階数1節点 $P_{u,b}=|b_u\rangle\langle b_u|$ では、安全結果について

```math
v=P_{u,b}Z_u
=\alpha_b|b_u\rangle,
\qquad
\frac{vv^\dagger}{v^\dagger v}=P_{u,b}.
```

従ってR191が結果を選んだ後、P.3の可逆選別機構そのものが選択後信号を射影子像へ物理的に移す。実装信号の規格化第2モーメント $C_{u,b}^{\rm out}$ は

```math
D_{\rm tr}
\left(
C_{u,b}^{\rm out},P_{u,b}
\right)
\leq
\varepsilon_{\rm proj}
```

を満たす。選択後成分を物理的に単位ノルムへ規格化する必要はなく、同じ未規格化成分を次段へ渡せる。

### P.5.1 階数1 射影子の測定後状態の受け渡し

前項の結論は、結果条件付き統計だけではなく、同一試行の実正準信号に対する物理的経路分解である。結果別固有状態テンプレートを別に準備せず、外部制御器が $\alpha_b$ または $p_{u,b}$ を読み出す必要もない。固定小深度では次段R191が新しい2作用の和と差を直接読むため、中間の振幅再調整を省略できる。

## P.6 方向を変えない振幅再調整

一般深さQ2-4で選択後作用が読出し下限を下回り得る場合だけ、選別機構後の選択後信号へR181Aの $\kappa=0$ 接続端を開く。

```math
\dot Z=g(J_*-Z^\dagger Z)Z.
```

方向 $Z/\|Z\|$ は一定で、作用 $r=Z^\dagger Z$ は

```math
\dot r=2gr(J_*-r)
```

に従う。P.2の下限 $r(0)\geq\tau_{\rm state}r_{\rm in}$ と固定入力作用区間から、目標相対動径誤差 $\eta_R$ に必要な時間を試行前に一様に選べる。固定小深度Q1/Q2-1/Q2-3では作用下限を直接保証できるなら本段を省略してよい。

## P.7 望遠鏡和と完全結果誤差

理想節点核を $K_k$、実装核を $\widetilde K_k$ とする。過去の安全履歴 $h_{k-1}$ 上で

```math
\sup_{h_{k-1}}
D_{\rm TV}
\left(
\widetilde K_k(h_{k-1},\cdot),
K_k(h_{k-1},\cdot)
\right)
\leq\bar\varepsilon_k
```

とする。$\bar\varepsilon_k$ にはR191の完全結果誤差 $\varepsilon_{191,k}$、必要な局所記録誤差、制御付き選別機構誤差、必要な場合の振幅再調整誤差、転送誤差、および前段状態方向誤差からこの節点核へ伝播した偏差を各1回だけ含める。R191主線ではR164/R190/R170代替経路の正則化、混合、固定誤差を重複加算しない。

Markov核の縮約性と望遠鏡和から

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^m\bar\varepsilon_k.
```

理想核の積は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2}{\|Z_0\|^2}
```

と望遠鏡型に縮約する。無反応を同じ完全履歴空間に保持し、成功履歴だけを再規格化しない。

<!-- theorem-start:proof -->
**証明（R181D）**

P.1が射影作用保持、P.2がR191の2結果核と安全作用下限、P.3が結果固定後の1対1な経路分解、P.4--P.5.1が条件付き状態方向誤差、P.6が必要時だけの作用下限回復を与える。各段の完全結果核誤差を一度だけ $\bar\varepsilon_k$ に集約し、Markov核の縮約性と望遠鏡和を適用すれば上式を得る。理想節点では未規格化作用比が連鎖的に相殺され、Lüders型逐次分布に一致する。証明終。
<!-- theorem-end:proof -->

## P.8 資源と反証条件

$m=n$ の一般深さで各節点誤差を $O(\epsilon/n)$ に配分する。R191では

```math
\tau_{\rm cut},g,\varepsilon_u,\varepsilon_{\rm cap}
=O(\epsilon/n),
\qquad
\Delta_{\min}g^2
\gtrsim
\log(n/\epsilon)
```

を十分条件に選べるため、

```math
\Delta_{\min}
=O\!\left(
\frac{n^2}{\epsilon^2}
\log\frac n\epsilon
\right)
```

で足りる。$\tau_{\rm state}=O(\epsilon/n)$ なら状態方向誤差を $O(\epsilon/n)$ にする十分条件として $\eta_F=O((\epsilon/n)^{3/2})$ を取れ、依然として逆多項式精度である。一般深さではP.6の振幅再調整を残す。

R164/R190/R170の作用殻型代替経路を選ぶ場合、その正則化、混合、renewal、固定時間と資源は代替経路だけの台帳へ計上する。

次のいずれかが避けられなければR181Dの主張は成立しない。

1. Born確率表または振幅表を外部制御器へ入力する。
2. R191の結果固定前に選別機構を開き、結果成分像を混在させる。
3. 端点dispatcherに状態依存除算または指数精度を要する。
4. 非選択成分または振幅再調整環境を同じ能動状態へ不可逆に消去する。
5. 無反応を除外して成功試行だけを再規格化する。
6. 深さ $n$ のR191、選別、転送誤差を多項式予算へ同時に収められない。
'''


def patch_a16() -> None:
    write("sections/A16_m54_projector_tree_receiver.md", NEW_A16)


def patch_common() -> None:
    path = "sections/02_common_canonical_modules.md"
    s = read(path)
    s = re.sub(
        r"^@status:.*$",
        "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。R191をQ1/Q2の2結果射影読出し主線、R164/R190/R170を一般有限結果集合・作用殻型の代替経路、R161/R162をQ3移動経路として分離し、R181A--R181Dを準備、テンソル積状態生成、永続ゲート、段階的射影選別読出しの正本として置く。",
        s,
        count=1,
        flags=re.M,
    )
    s = s.replace(
        "R190/R179はQ1/Q2の静的選択浴、R170は吸収指針変数固定として扱う。",
        "Q1/Q2の2結果射影読出しはR191を主線とする。R190/R179/R170は一般有限結果集合・作用殻型の代替経路として扱い、Q3ではR161/R162の移動経路を使う。",
    )
    lines = []
    for line in s.splitlines():
        if line.startswith("| Q1 |"):
            line = "| Q1 | W型2モード静的状態構成 | $|\\Lambda|=2$、2結果 $X$ | R181A、R140 | R191、R143/R181D；R164/R190/R170は代替 |"
        elif line.startswith("| Q2-1 |"):
            line = "| Q2-1 | 2ビット記憶部の静的状態構成 | $|\\Lambda|=4$、段階的射影選別 $X$ | R181B、R181C | R191、R181D |"
        elif line.startswith("| Q2-2 |"):
            line = "| Q2-2 | 2ビット記憶部＋設定先行受信機構 | $|\\Lambda|=4$、2翼局所 $X$ | R181B/R181C、R180 | 中央・局所R191、R180C |"
        elif line.startswith("| Q2-3 |"):
            line = "| Q2-3 | 3ビット永続記憶部 | $|\\Lambda|=8$ | R181Bを2回、R181C、R177 | R191、R181D |"
        elif line.startswith("| Q2-4 |"):
            line = "| Q2-4 | 一般 $n$ ビット記憶部 | $|\\Lambda|=2^n$ | R181Aの振幅再調整用接続端、R179、R181C | R191、R181D；R164/R190/R170は代替 |"
        lines.append(line)
    s = "\n".join(lines) + ("\n" if s.endswith("\n") else "")
    s = s.replace(
        "Q1/Q2の静的状態構成では、各操作面または末端読出し面でR164の条件付き分布へ有限時間整合し、必要な結果成分を固定して記録する。",
        "Q1/Q2の2結果静的状態構成では、各測定面で射影作用を保持してR191へ渡し、ブラウン巨視的スピンの混合--decision--捕獲から排他的結果を固定する。一般有限結果集合または作用殻型の代替実現ではR164/R190/R170を用いる。",
    )
    new_213 = r'''## 2.13 M54共通射影作用・選別機構：作用保持・R191読出し・可逆選別

出力ビット $k$ に対する計算基底射影を $P_{k,0},P_{k,1}$ とし、

```math
P_{k,0}+P_{k,1}=I,
\qquad
P_{k,0}P_{k,1}=0,
```

```math
J_{k,b}(Z)=\mathcal J_0Z^\dagger P_{k,b}Z
```

を未使用指針変数へ保持する。信号と作業領域の2貯蔵部上に

```math
F_{k,b}
=
\begin{pmatrix}
P_{k,b}&P_{k,1-b}\\
P_{k,1-b}&-P_{k,b}
\end{pmatrix}
```

を置く。

<!-- theorem-start:lemma -->
**補題（直交射影子作用保持機構と対合 選別機構）**

$F_{k,b}^\dagger F_{k,b}=I$、$F_{k,b}^2=I$ であり、未使用作業領域に対して

```math
F_{k,b}(Z,0)=(P_{k,b}Z,P_{k,1-b}Z)
```

と作用する。作用保持機構を信号に対する制御剪断として実装すれば、未使用容量運動量上で $J_{k,0},J_{k,1}$ を保持し、理想信号 $Z$ を変更しない。計算基底ビット射影子と選別機構はビットラベルだけから一様に生成でき、$2^n$ 成分の列挙を必要としない。
<!-- theorem-end:lemma -->

この補題自身は確率的な結果選択を行わない。2結果射影測定の排他的選択と固定はR191を主線とし、一般有限結果集合または作用殻型の代替実現はR170が担う。**共通射影選別機構** の主線は

1. 未処理射影作用 $J_{k,0},J_{k,1}$ の保持、
2. R191による2結果選択と吸収記録、
3. 必要ならR112または系列固有機構による局所記録、
4. 固定結果で制御した対合選別機構 $F_{k,b}$、
5. 一般深さで必要な場合だけ方向を変えない振幅再調整、
6. 次節点または外部接続端への転送

である。R181Dはこの列を段階的に合成する。R164/R190/R170経路を選ぶ場合は段階2だけを代替し、R191と同じ選択誤差を二重計上しない。R180Aは同じ作用保持補題と対合選別機構を中央潜在結果成分の受渡しへ使う兄弟特殊化である。'''
    s = replace_section(s, "## 2.13 M54共通射影容量・選別機構：容量固定・R170選択固定・可逆選別", "## 2.14 R181D：M54段階的射影選別・測定後状態受渡し定理", new_213, "2.13")
    new_214 = r'''## 2.14 R181D：M54段階的射影選別・測定後状態受渡し定理

第 $k$ 段、履歴節点 $u$ の入力を $Z_u\neq0$ とし、直交射影 $P_{u,0},P_{u,1}$ に対する未処理作用を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

とする。各節点は第2.8.2節R191へこの2作用を渡し、結果 $b\in\{0,1\}$ または無反応を得る。固定閾値 $\tau_{\rm cut}$ とR191のtransducer境界誤差 $\varepsilon_u$ に対し

```math
\tau_{\rm state}
=\tau_{\rm cut}-\frac{\varepsilon_u}{2}>0
```

を仮定すれば、無反応でない選択結果の理想作用重みは $p_{u,b}\geq\tau_{\rm state}$ である。R191の吸収記録を固定した後に $F_{u,b}$ を作用し、非選択成分を作業領域へ保持する。一般深さで作用下限の回復が必要な場合だけR181Aの方向を変えない振幅再調整を使う。

<!-- theorem-start:theorem -->
**定理（R181D：M54段階的射影選別・測定後状態受渡し定理）**

理想節点を深さ $m$ まで合成すると、葉 $y=(y_1,\ldots,y_m)$ の確率は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2}{\|Z_0\|^2}
```

となる。入力分布誤差を $\varepsilon_{\rm in}$、安全履歴上の第 $k$ 節点のR191読出し、制御付き選別機構、必要な振幅再調整、転送、前段状態方向偏差の次節点への伝播を各1回だけまとめた実装誤差を $\bar\varepsilon_k$ とすれば、無反応を含む完全結果分布について

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^m\bar\varepsilon_k.
```

選別機構作用素誤差が $\eta_F<\sqrt{\tau_{\rm state}}$ なら選択後の規格化状態方向誤差は

```math
\varepsilon_{u,b}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}.
```

階数1節点では理想選択後信号 $P_{u,b}Z_u$ は射影子像そのものであり、物理的に単位ノルムへ規格化せず同じ試行の次段へ直接渡せる。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

完全証明と一般深さの資源境界は付録Pに置く。R164/R190/R170の作用殻型代替経路を選ぶ場合は、その正則化・混合・固定誤差をR191誤差と同時に加えない。'''
    s = replace_section(s, "## 2.14 R181D：M54段階的射影選別・測定後状態受渡し定理", "## 2.15 R178Dの本線退役：有限閉鎖リセットの情報容量境界", new_214, "2.14")
    s = s.replace(
        "+\\frac{n\\delta}{1+\\delta}\n+2n(\\tau+\\gamma)\n+\\sum_{j=1}^n\\bar\\varepsilon_j.",
        "+\\sum_{j=1}^n\\bar\\varepsilon_j.",
    )
    s = s.replace(
        "$\\eta_{\\rm gate}=O(\\epsilon/d)$ とし、$\\tau,\\gamma,\\bar\\varepsilon_j$ はそれぞれ $O(\\epsilon/n)$ と選ぶ。R191主線では $g,\\varepsilon_u,\\varepsilon_{\\rm cap}=O(\\epsilon/n)$ とし、$\\Delta_{\\min}g^2\\gtrsim\\log(n/\\epsilon)$ を十分条件に取る。",
        "$\\eta_{\\rm gate}=O(\\epsilon/d)$、$\\bar\\varepsilon_j=O(\\epsilon/n)$ とする。R191主線では $\\tau_{\\rm cut},g,\\varepsilon_u,\\varepsilon_{\\rm cap}=O(\\epsilon/n)$ とし、$\\Delta_{\\min}g^2\\gtrsim\\log(n/\\epsilon)$ を十分条件に取る。",
    )
    write(path, s)


def patch_status() -> None:
    path = "PROJECT_STATUS.md"
    s = read(path)
    s = s.replace(
        "R181Aは物理テンプレート準備、R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部ゲート、R170は静的な排他的選択・固定、R181Dはその下流の段階的射影選別と測定後状態受渡しを与える。R180AはR181Dではなく共通射影容量固定補題とR170を使う兄弟特殊化である。",
        "R181Aは物理テンプレート準備、R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部ゲート、R191はQ1/Q2の2結果排他的選択・吸収記録、R181Dはその下流の可逆射影選別と測定後状態受渡しを与える。R170は一般有限結果集合・作用殻型の代替経路へ残す。R180AはR181Dではなく共通射影作用保持補題とR191を使う兄弟特殊化である。",
    )
    lines=[]
    for line in s.splitlines():
        if line.startswith("| Q1-2 |"):
            line = "| Q1-2 | 達成 | M54のW2静的状態構成 | R187によるM37のW2制御用信号系＋R191ブラウン巨視的スピン読出し接続部 | Q1 W型2モード測定・Zeno手順（旧M47） | R140、R143--R144、R181A、R181D、R187、R189A--R189C、R191 | Born分布、同軸反復分布、異軸逐次分布と有限2回Zeno証人を導出。2結果主線はR191、R164/R190/R170は作用殻型代替実現。全測定部分系の単一ミクロ装置統合は強化課題 |"
        elif line.startswith("| Q2-1 |"):
            line = "| Q2-1 | 条件付き達成 | M54静的状態構成 | 永続4モード記憶部と逆演算用補助部／作業領域 | テンソル積状態の生成、ゲート、末端段階的射影選別 | R112、R181A、R181B、R181C、R181D、R191 | R191の作用和・作用差transducer、ブラウン巨視的スピン、吸収記録、既存選別機構、必要な再調整を一つの装置へ接続することを条件とする |"
        elif line.startswith("| Q2-2 |"):
            line = "| Q2-2 | 条件付き達成 | M54静的状態構成 | 永続4モード記憶部と2翼局所測定機構 | R180設定先行2端Hopf受信機構 | R112、R180A、R180B、R180C、R181A、R181B、R181C、R191 | 固定一重項、固定有限設定族、準備先行、非空間分離、採用開放法則に限定。中央R191と2翼局所R191を含む開放装置接続、自由設定、空間分離、一般状態は未達 |"
        elif line.startswith("| Q2-3 |"):
            line = "| Q2-3 | 条件付き達成 | M54三部分系静的状態構成 | 永続8モード記憶部と逆演算用補助部／作業領域 | 二段ゲート合成と末端段階的射影選別 | R112、R177、R181A、R181B、R181C、R181D、R191 | R191とR181Dの末端開放接続、および固定3入力を越える一般サイズの資源効率は未達 |"
        elif line.startswith("| Q2-4 |"):
            line = "| Q2-4 | 条件付き達成 | M54一般静的状態構成 | $2^n$ 受動直接モード記憶部＋一様開放浴 interface | 一般ゲート列と逐次段階的射影選別 | R112、R179、R181A、R181B、R181C、R181D、R186、R191 | 静的部分系配線、射影作用保持、R191読出し、制御付き選別機構、方向を変えない振幅再調整、開放リセット/供給接続部を一つの一様装置族へ接続し、R186の多項式精度条件を満たすことを示す。R164/R190/R170は代替経路、R178Dは必須依存にしない |"
        lines.append(line)
    s="\n".join(lines)+("\n" if s.endswith("\n") else "")
    s = s.replace(
        "3. R187のM37のW2信号系にR181Aの供給源／ポンプ、R164作用殻、R161/R162の衝突、選択・固定、R181Dの選別機構/方向を変えない振幅再調整、R143局所記録を同じ具体装置・時計自由度で接続し、共通射影選別機構による測定後状態の受け渡し、永久記録、リセットまでの周期総収支を閉じる。",
        "3. R187のM37 W2信号系にR181Aの供給源／ポンプ、射影作用保持、R191のブラウン巨視的スピン読出し、R181Dの選別機構／必要な振幅再調整、記録を同じ具体装置・時計自由度で接続し、測定後状態受渡し、永久記録、リセットまでの周期総収支を閉じる。R164/R190/R170代替経路の統合は独立な強化課題とする。",
    )
    s = s.replace(
        "4. R180Cについて、M54末端SWAP、共通射影容量固定機構、中央R170潜在選択、2端Hopf受信機構のポンプと排出先、中央切断、2翼局所R170、R112局所記録、未使用素子の供給を同じ具体装置と時計自由度へ統合する。",
        "4. R180Cについて、M54末端SWAP、共通射影作用保持機構、中央R191潜在選択、2端Hopf受信機構のポンプと排出先、中央切断、2翼局所R191、R112局所記録、未使用素子の供給を同じ具体装置と時計自由度へ統合する。",
    )
    write(path,s)


def patch_q2_receiver() -> None:
    path="sections/05_m54_setting_pre_receiver.md"
    s=read(path)
    s=s.replace("3. R180Cは中央切断、2翼のR170選択・固定とR112局所記録、Bell監査、未使用素子帰還を条件付きで合成する。","3. R180Cは中央切断、2翼のR191選択・吸収記録とR112局所記録、Bell監査、未使用素子帰還を条件付きで合成する。")
    s=s.replace("R180Aは第2.13節の共通直交射影容量固定・対合選別補題とR170選択・固定を使い、R181Dの段階的射影選別定理そのものには依存しない。$S=S_{\\rm lock}$ は中央で固定された潜在A結果であり、外部結果として直接記録しない。切断後にA翼のR170選択・固定とR112局所記録が一意な外部A記録を作る。","R180Aは第2.13節の共通直交射影作用保持・対合選別補題とR191を使い、R181Dの段階的射影選別定理そのものには依存しない。$S=S_{\\rm lock}$ は中央R191で固定された潜在A結果であり、外部結果として直接記録しない。切断後にA翼の局所R191とR112局所記録が一意な外部A記録を作る。")
    s=s.replace("有限装置では保持、基底分離器、射影結果の固定機構、作用殻、混合、衝突、ブロック保持の誤差と無反応を完全結果集合上で加える。","有限装置では保持、基底分離器、射影作用保持、中央R191の完全結果誤差、ブロック保持誤差を完全結果集合上で各1回だけ加える。")
    new55=r'''## 5.5 2翼の局所R191読出し

R180Bが作る各翼の非零2モード信号 $z_A,z_B$ に対し、局所分析器後の直交射影 $P_{\ell,+},P_{\ell,-}$（$\ell=A,B$）から

```math
J_{\ell,b}
=\mathcal J_0 z_\ell^\dagger P_{\ell,b}z_\ell,
\qquad b\in\{+1,-1\}
```

を未使用作用保持指針変数へ写し、各翼の独立なR191へ渡す。理想R191では

```math
P_\ell(b\mid z_\ell)
=\frac{J_{\ell,b}}{J_{\ell,+}+J_{\ell,-}}
```

である。A翼とB翼には別々のブラウン巨視的スピン、混合浴、decision浴、吸収記録を置き、中央切断後は完全共通原因 $\Lambda$ に条件付けて局所R191核を積にする。R164/R190/R170の局所作用殻経路は代替実現として残すが、R191主線と同時に使わない。

R180B終了後の方向誤差は連続状態空間上の有界距離で評価し、固定有限設定族の安全域上で局所R191結果核へLipschitz伝播させる。R191自身の混合、transducer、有限温度retreat、有限decision時間、捕獲記録は各翼の $\varepsilon_{191}^{A,B}$ に各1回だけ含める。'''
    s=replace_section(s,"## 5.5 2翼の局所整合","## 5.6 R180B：供給源駆動 2端Hopf吸引",new55,"5.5")
    s=s.replace("各翼には中央結果成分作用殻と異なる未使用局所2結果作用殻を置く。","各翼には中央R191とは異なる未使用の局所ブラウン巨視的スピンと作用保持指針変数を置く。")
    s=s.replace("A分析器は $a_{s,x}=u_{s,x}$ を結果 $A=s$ の安全井戸へ写す。B分析器は $b_{s,x}(V)$ を基底 $u_{b,y}$ で分析する。分析器終了後に各局所信号を固定し、各翼でR170の収集・選択・固定を走らせ、その後R112局所記録を作用する。","A分析器は $a_{s,x}=u_{s,x}$ を2結果作用へ写す。B分析器は $b_{s,x}(V)$ を基底 $u_{b,y}$ で分析する。分析器終了後に各局所信号の2作用を保持し、各翼でR191を走らせ、その吸収記録をR112局所記録へ移す。")
    old_formula=r'''\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{\rm ray}^{54}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{\rm latch}
+2\tau\\
&+
C_\tau\varepsilon_{\rm block}
+L_{\rm fib}K_{180}
e^{-\gamma_{180}T_{\rm PH}}
+\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}\\
&+
\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{170}^{A}
+\varepsilon_{170}^{B}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
\end{aligned}'''
    new_formula=r'''\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{\rm ray}^{54}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{191}^{\rm cen}
+C_{\rm safe}\varepsilon_{\rm block}\\
&+
L_{\rm fib}K_{180}e^{-\gamma_{180}T_{\rm PH}}
+\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{191}^{A}
+\varepsilon_{191}^{B}\\
&+
\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
\end{aligned}'''
    s=replace_once(s,old_formula,new_formula,"5.9 error formula")
    s=s.replace("$\\varepsilon_{\\rm latch}$ は中央射影子容量、作用殻、有限混合、衝突、内部結果固定、$\\varepsilon_{\\rm block}$ は選択ブロック保持とテンプレート接続端を表す。$\\varepsilon_{170}^{A,B}$ は各翼のR170選択・固定誤差であり、直前に独立項として明示した正則化・有限混合と二重計数しない。","$\\varepsilon_{191}^{\\rm cen}$ は中央2作用保持後のR191完全結果誤差、$\\varepsilon_{\\rm block}$ は選択ブロック保持とテンプレート接続端を表す。$\\varepsilon_{191}^{A,B}$ は各翼の局所R191完全結果誤差であり、各R191内部の混合・保護帯・有限温度・未捕獲を別項として二重計数しない。")
    s=s.replace("R180AのM54信号保持、共通射影容量固定機構、中央R170選択・固定、選択ブロックの接続端","R180AのM54信号保持、共通射影作用保持機構、中央R191選択・吸収記録、選択ブロックの接続端")
    s=s.replace("特に、M54 保持から射影結果の固定機構までの反作用、結果成分 指針変数から未規格化ブロックの供給接続端への物理的経路選択、テンプレート接続端と2端Hopf受信機構のポンプと排出先の両立、中央切断後の未使用局所作用殻の積因子化、全窓を共有する単一時計自由度は未統合である。","特に、M54保持から射影作用保持・中央R191までの反作用、吸収記録から未規格化ブロックの供給接続端への物理的経路選択、テンプレート接続端と2端Hopf受信機構のポンプと排出先の両立、中央切断後の2個の局所R191の条件付き積、全窓を共有する単一時計自由度は未統合である。")
    s=s.replace("切断後に2つのR170で局所選択を固定し、R112局所記録を後段へ分離して作用する","切断後に2つの局所R191で選択と吸収記録を行い、R112局所記録を後段へ分離して作用する")
    s=s.replace("$U_x^\\dagger\\otimes I_2$、第2.13節の共通射影子作用容量固定機構、R164の容量比に対する作用殻状態数、有限再平衡化を使う","$U_x^\\dagger\\otimes I_2$、第2.13節の共通射影作用保持機構、中央R191の2結果読出しを使う")
    write(path,s)


def patch_q2_proof() -> None:
    path="sections/A4_m54_receiver_cycle_proofs.md"
    s=read(path)
    s=re.sub(r"^@status:.*$","@status: R180Aの条件付きブロック代数、中央R191選択、節点切断、2翼局所R191、R180Cの局所応答・Bell監査・有限誤差・弱開放帰還を証明する。",s,count=1,flags=re.M)
    newd2=r'''## D.2 R180Aの中央R191選択

第2.13節の直交射影子作用保持機構を物理保持信号 $\widetilde V$ と2つの直交射影子 $\Pi_s^x$ へ適用し、

```math
J_s
=\mathcal J_0\widetilde V^\dagger\Pi_s^x\widetilde V
=\mathcal J_0r^2p_{s|x}(V)
```

を固定する。理想未使用運動量が零なら保持機構から信号への反作用は零である。2作用 $J_+,J_-$ を中央R191へ渡すと、理想吸引域測度は

```math
P(S=s\mid\widetilde V,x)
=\frac{J_s}{J_++J_-}
=p_{s|x}(V).
```

中央R191の有限混合、transducer、保護帯、有限温度retreat、有限decision時間、吸収記録を $\varepsilon_{191}^{\rm cen}$ にまとめる。結果 $S=s$ を固定した後に第2.13節の対合選別機構を制御し、対応する未規格化ブロック $\widetilde w_{s,x}$ を供給接続端へ渡す。入力係数または $r$ を外部制御器へ公開しない。R164/R190/R170の作用殻型選択は代替経路としてのみ残す。

選択結果 $s$ に対する理想B応答を

```math
P(B=b\mid s,V,x,y)
=\frac{|u_{b,y}^\dagger w_{s,x}|^2}{p_{s|x}(V)}
```

とすれば

```math
P(S=s,B=b\mid V,x,y)
=\left|\left(u_{s,x}^\dagger\otimes u_{b,y}^\dagger\right)V\right|^2.
```

<!-- theorem-start:proof -->
**証明（R180A）**

D.1がブロックと射影作用の等式を与える。中央R191の理想2結果重みは保持作用比 $J_s/(J_++J_-)=p_{s|x}$ である。選択結果の条件付きB応答を掛ければテンソル積Born重みになる。有限装置では中央R191、保持、選別、接続端の偏差を完全結果集合上で各1回だけ加える。証明終。
<!-- theorem-end:proof -->'''
    s=replace_section(s,"## D.2 R180Aの作用殻選択","## D.3 節点切断と方向安定性",newd2,"D.2")
    newd5=r'''## D.5 R180切断面と局所R191誤差

R180B終了後の2翼信号方向は、理想方向 $(a_{s,x},b_{s,x}(V))$ から有界距離 $K_{180}e^{-\gamma_{180}T_{\rm PH}}$ 以内にある。固定有限設定族と中央結果成分の安全域では、局所分析器と局所射影作用保持はこの方向誤差に対して一様Lipschitzである。

中央R191結果 $s$ と連動位相を完全共通原因 $\Lambda$ に含め、切断後にはA翼・B翼それぞれに未使用のR191指針変数を置く。理想局所核を $K_{A,0}^x,K_{B,0}^y$、実装核を $K_A^x,K_B^y$ とし、

```math
D_{\rm TV}(K_A^x,K_{A,0}^x)\leq\varepsilon_{191}^{A},
\qquad
D_{\rm TV}(K_B^y,K_{B,0}^y)\leq\varepsilon_{191}^{B}
```

とする。切断後の環境初期化の積因子化偏差を $\varepsilon_{\rm prod}$ とすれば、結果形成前の偏差は粗く

```math
\varepsilon_{\rm fib}
\leq
\varepsilon_{191}^{\rm cen}
+C_{\rm safe}\varepsilon_{\rm block}
+L_{\rm fib}K_{180}e^{-\gamma_{180}T_{\rm PH}}
+\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{191}^{A}
+\varepsilon_{191}^{B}
```

で抑えられる。R191主線ではR164/R190/R170の正則化、混合、固定誤差をこの式へ同時に加えない。連続信号測度を理想状態方向支持測度と全変動距離で比較せず、結果核へ写した後の全変動距離だけを用いる。'''
    s=replace_section(s,"## D.5 R180強整合ファイバー","## D.6 局所応答と非信号性",newd5,"D.5")
    s=s.replace("各分析器終了後に局所信号を固定し、各翼のR170選択・固定を走らせ、その後R112局所記録を作用する。未使用作用殻、浴接続部、ノイズ初期種、記録素子が条件付き積なら、二つの局所測定機構も条件付き積になる。","各分析器終了後に局所2作用を保持し、各翼のR191を走らせ、その後R112局所記録を作用する。未使用ブラウン巨視的スピン、局所浴接続部、熱浴初期種、記録素子が条件付き積なら、二つの局所測定機構も条件付き積になる。")
    s=s.replace("分離器、結果成分作用、中央R170、ブロック保持、2端Hopf、位置整合、切断、条件付き積偏差、局所R191、R112局所記録、時計自由度を各1回だけ数えると本文の $\\varepsilon_{180}^{\\rm cyc}$ になる。","分離器、結果成分作用、中央R191、ブロック保持、2端Hopf、切断、条件付き積偏差、2個の局所R191、R112局所記録、時計自由度を各1回だけ数えると本文の $\\varepsilon_{180}^{\\rm cyc}$ になる。")
    s=s.replace("D.5が局所粒子位置ファイバー、D.6が切断後の条件付き積測定機構","D.5が中央・局所R191の有限誤差、D.6が切断後の条件付き積測定機構")
    s=s.replace("結果相関情報、ポンプ・排出先・作用殻の環境履歴はR179の流出浴へ流す。","結果相関情報、ポンプ・排出先・R191浴の環境履歴はR179の流出浴へ流す。")
    write(path,s)


def patch_q1() -> None:
    path="sections/03_m47_controlled_w_instrument.md"
    s=read(path)
    s=s.replace("R164/R190/R179/R170の作用殻・粒子位置・記録誤差は別部分系なのでR187へ吸収しない。","R191の読出し・吸収記録誤差は別部分系なのでR187へ吸収しない。R164/R190/R170の作用殻型代替経路を選ぶ場合もその誤差をR187へ吸収しない。")
    s=s.replace("## 3.6 M54静的/R170のQ1二結果成分特殊化","## 3.6 M54静的/R191のQ1二結果成分特殊化")
    s=s.replace("R170と共通の選択・固定共通部で安全な結果成分 $s$ を固定した後、R181Dの制御付き射影選別機構を作用させる。","R191で安全な結果成分 $s$ を吸収記録へ固定した後、R181Dの制御付き射影選別機構を作用させる。")
    s=s.replace("次の測定面に到達した時点で、改めてR164、R190、R179、R170を有限時間だけ作用させる。","次の測定面に到達した時点で、改めてR191を有限時間だけ作用させる。")
    s=s.replace("分析器終了後、R164--R190--R179の静的選択後にR170の吸収指針変数を固定し、3.11のR143局所記録で安全な結果成分 $s$ を記録する。","分析器終了後、R191で安全な結果成分 $s$ を吸収記録へ固定し、必要なら3.11の局所記録へ結果を写す。")
    s=s.replace("$\\eta_F<\\sqrt\\tau$ なら","$\\eta_F<\\sqrt{\\tau_{\\rm state}}$ なら")
    s=s.replace("\\frac{2\\eta_F}{\\sqrt\\tau-\\eta_F}","\\frac{2\\eta_F}{\\sqrt{\\tau_{\\rm state}}-\\eta_F}")
    new313=r'''## 3.13 R143：Q1 W型2モード読出しと射影選別機構受渡し

Q1の1段測定では、R140の分析器後に左右2作用を保持し、R191で排他的結果を選択・吸収記録する。R181Dの階数1選別機構が同一試行信号を対応する射影子像へ移し、必要なら局所記録へ結果を写す。有限W型の左右空間コントラストによる位置読出しは独立な代替・診断であり、R191主線のBorn重み生成には使わない。

<!-- theorem-start:theorem -->
**定理（R143：Q1 W型2モード読出しと射影選別機構受渡し）**

固定純粋入力、測定軸 $\boldsymbol n$、有限観測時間について、R181A/R187の信号準備、R140分析器、左右射影作用保持、R191、R181Dの階数1選別機構を同じ安全集合で実行できるとする。準備誤差を $\varepsilon_{\rm prep}$、分析器とW2接続誤差を $\varepsilon_{\rm ctrl}+\varepsilon_{2m}$、R191完全結果誤差を $\varepsilon_{191}$、選別・転送を含む節点誤差を $\varepsilon_{\rm node}^{\rm dist}$ とする。このとき

```math
\varepsilon_{\rm inst}
\leq
\varepsilon_{\rm prep}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{191}
+\varepsilon_{\rm node}^{\rm dist}
```

で理想2結果Born分布との差を抑えられる。無反応を同じ完全結果集合に残す。

R191のdispatcherから得る $\tau_{\rm state}>0$ と選別機構誤差 $\eta_F<\sqrt{\tau_{\rm state}}$ に対し、安全結果 $s$ の条件付き出力共分散は

```math
D_{\rm tr}
\left(C_s^{\rm out},|s\rangle\langle s|\right)
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}
=:\varepsilon_{\rm node}^{\rm state}.
```

結果別固有状態テンプレート、外部トモグラフィー、成功試行の再規格化は使わない。
<!-- theorem-end:theorem -->

R143の利用単位は1回の測定であり、複数回履歴はR144で合成する。左右空間位置を直接読む旧有限コントラスト経路はW型固有の代替検証として3.9--3.11に残し、その $\eta_W$ や再平衡化誤差をR191主線へ重複加算しない。'''
    s=replace_section(s,"## 3.13 R143：Q1 W型2モード読出しと射影選別機構受渡し","## 3.14 同軸反復と異軸逐次測定",new313,"3.13")
    s=s.replace("各測定面でR164--R190--R179--R170を有限時間だけ走らせる。","各測定面でR191を有限時間だけ走らせる。")
    new317=r'''## 3.17 誤差・熱力学・資源台帳

Q1のR191主線では1段結果分布誤差を

```math
\varepsilon_{Q1}^{\rm dist}
=
\varepsilon_{\rm prep}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{191}
+\varepsilon_{\rm node}^{\rm dist}
```

と整理し、R191内部の混合、transducer、保護帯、有限温度retreat、有限decision時間、吸収記録を別項として二重加算しない。安全結果の測定後状態誤差は

```math
\varepsilon_{Q1}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}
```

で別管理する。R144では各段の結果分布誤差と次段へ伝わる状態方向誤差を有限和へ入れる。

熱力学台帳では分析器仕事、R191のmixing/decision浴、吸収記録、可逆選別機構、必要な振幅再調整、リセットを分ける。R164/R190/R170の作用殻型代替経路を選ぶ場合、その作用殻仕事・混合・renewal・固定資源は代替経路だけへ計上する。有限閉鎖Hamiltonian全系への統合は固定目標ではない。

1段のR191主線の能動装置は、2モード信号、作用保持指針変数、ブラウン巨視的スピン、吸収記録、選別機構用作業領域、必要な記録素子と傾斜制御からなる。固定有限段では未規格化選択成分を次段へ直接渡し、一般深さで作用下限が必要な場合だけ方向を変えない振幅再調整を使う。'''
    s=replace_section(s,"## 3.17 誤差・熱力学・資源台帳","## 3.18 W2走行中作用容量の有限正準保持",new317,"3.17")
    new319=r'''## 3.19 W2走行中階数1射影選別の有限時間接続

R189A終了後は固定済み左右作用 $\bar J_L,\bar J_R$ を走行中W2信号から切り離してR191へ渡し、その吸収記録 $S_{\rm lock}\in\{L,R,\varnothing\}$ が固定された後に制御付き選別機構を開く。中間測定では傾斜、局所外部記録、方向を変えない振幅再調整を使わない。

<!-- theorem-start:theorem -->
**定理（R189B：W2走行中階数1射影選別有限時間接続）**

R189Aの保持中心時刻を $t_\ell$ とする。保持済み2作用をR191へ渡し、有限decision時間後に潜在結果 $S_{\rm lock}$ を固定する。安全結果 $b$ ではR181Dの階数1対合選別機構 $F_b$ を有限時間 $\tau_F$ だけ作用し、その完了時刻を実効測定時刻 $t_m$ と定める。全操作中で零傾斜Rabi項を停止しない。

選別機構単独の理想作用を $F_b$、有限実装・接続端・時計偏差を含む誤差を $\eta_F^{\rm run}$ とすれば

```math
\eta_F^{\rm run}
\leq
\eta_F
+\Omega_\kappa\tau_F
+\varepsilon_{\rm port,F}
+\varepsilon_{\rm clk,F}.
```

また

```math
|p_b(t_m)-p_b(t_\ell)|
\leq
\varepsilon_{\rm lat},
\qquad
\varepsilon_{\rm lat}
=\frac{\Omega_\kappa}{2}(t_m-t_\ell).
```

従って実効測定時刻のBorn分布との全変動距離は

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+\varepsilon_{191}^{\rm mid}
+\varepsilon_{\rm lat}
```

で抑えられる。R191の無反応は完全結果へ残す。選別時刻で $p_b(t_m)\geq p_*>0$ かつ $\eta_F^{\rm run}<\sqrt{p_*}$ なら

```math
\varepsilon_{189B}^{\rm state}
\leq
\frac{2\eta_F^{\rm run}}{\sqrt{p_*}-\eta_F^{\rm run}}.
```

無反応では $F_L,F_R$ のどちらも作用させず、W2信号は零傾斜Rabiを継続する。
<!-- theorem-end:theorem -->

固定有限回のZeno証人では各安全結果に固定正下限を取れるため、中間振幅再調整を省ける。'''
    s=replace_section(s,"## 3.19 W2走行中階数1射影選別の有限時間接続","## 3.20 R189C：有限2回Rabi--Zeno比較",new319,"3.19")
    s=s.replace("測定運転と同じR189A、固定済み容量R170系、選択結果固定、時計自由度、待ち時間を用いるが","測定運転と同じR189A、R191読出し、吸収記録、時計自由度、待ち時間を用いるが")
    s=s.replace("作用保持、作用殻、開放浴選択、選択結果固定、待ち時間だけによる抑制を別に監査できる。","作用保持、R191のmixing/decision、吸収記録、待ち時間だけによる抑制を別に監査できる。")
    s=s.replace("固定精度のR170後半と有限選別時間を保ったまま","固定精度のR191 decision時間と有限選別時間を保ったまま")
    s=s.replace("R164/R170/R181DについてQ1測定統計で既に採用している指定誤差条件の下で","R191/R181DについてQ1測定統計で採用する指定誤差条件の下で")
    s=s.replace("+\\frac{\\delta}{1+\\delta}\n+\\varepsilon_{170}^{\\rm cap}","+\\varepsilon_{191}^{\\rm mid}")
    s=s.replace("$p_*=0.10$ と $\\tau+\\gamma<p_*$","$p_*=0.10$ と $\\tau_{\\rm state}<p_*$")
    s=s.replace("固定済み容量からの作用殻・R190/R179/R170静的選択部分系","固定済み2作用からのR191ブラウン巨視的スピン読出し部分系")
    s=s.replace("R140、R143--R144、R161、R164、R168、R170、R179、R181A、R181D、R187、R189A--R189C、R190A--R190C","R140、R143--R144、R168、R181A、R181D、R187、R189A--R189C、R191")
    write(path,s)

    path="sections/A2_m47_controlled_w_instrument_proofs.md"
    s=read(path)
    newb19=r'''## B.19 R189Bの固定済み容量R191選択と走行中射影選別

R189Aで得た固定済み未処理容量 $\bar J_L,\bar J_R$ を走行中W2信号から切り離し、R191の作用和・作用差入力へ渡す。R189Aの作用比誤差を $\varepsilon_{189A}$、R191の完全結果誤差を $\varepsilon_{191}^{\rm mid}$ とすれば、保持中心時刻 $t_\ell$ の理想Born分布との差は両者の和以下である。

規格化W2状態に対して $|\dot p_b|\leq\Omega_\kappa/2$ なので、R191 decisionと選別機構が完了する実効時刻 $t_m$ までの時間ずれは

```math
\varepsilon_{\rm lat}
\leq
\frac{\Omega_\kappa}{2}(t_m-t_\ell)
```

である。従って本文R189Bの

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+\varepsilon_{191}^{\rm mid}
+\varepsilon_{\rm lat}
```

を得る。

対合選別機構は自己共役かつ $F_b^2=I$ なので、信号と未使用作業領域上で有限二次生成子から実装できる。零傾斜Rabiを同時に残したことによるDuhamel偏差を $\Omega_\kappa\tau_F$、有限実装・接続端・時計偏差を加えたものを $\eta_F^{\rm run}$ とする。選別時刻で $p_b(t_m)\geq p_*$ なら付録Pの規格化写像Lipschitz評価から

```math
D_{\rm tr}(C_b^{\rm out},P_b)
\leq
\frac{2\eta_F^{\rm run}}{\sqrt{p_*}-\eta_F^{\rm run}}
```

を得る。階数1射影子では理想選択成分は入力振幅にかかわらず $P_b$ の像にある。固定有限回ではこの正の作用下限を次段まで保持できるため中間振幅再調整を用いない。証明終。'''
    s=replace_section(s,"## B.19 R189Bの固定済み容量選択と走行中射影選別","## B.20 R189Cの有限2回Zeno核と空操作対照",newb19,"B.19")
    s=s.replace("その後の固定済み容量R170系は信号から切り離され","その後の固定済み容量R191読出しは信号から切り離され")
    s=s.replace("一方、固定 $\\delta,p_*,\\tau,\\gamma$ と固定目標誤差に対するR164作用殻、R161混合、R190/R179静的選択、結果固定、有限選別機構の所要時間は各条件付き定理の範囲で有限値として先に選べる。","一方、固定 $p_*$ と固定目標誤差に対するR191の混合・decision・捕獲時間と有限選別機構の所要時間は各定理の範囲で有限値として先に選べる。")
    s=s.replace("固定済み容量R170系、終端R143/R181D読出し","中間R191、終端R143/R181D読出し")
    s=s.replace("固定済み容量からの作用殻と開放浴選択interface、選択機構","固定済み2作用からのR191ブラウン巨視的スピン接続部、吸収記録")
    s=s.replace("本証明はR164の作用容量--作用殻境界、R190作用殻混合、R179 renewal、R170 指針変数、R189A作用保持機構、R189B選別機構をM37の元の局所ばね座標と共通Hamiltonian無限浴から一つの単一ミクロ装置として導出しない。","本証明はR191の作用和・作用差transducer、ブラウン巨視的スピン、吸収記録、R189A作用保持機構、R189B選別機構をM37の元の局所ばね座標と共通Hamiltonian無限浴から一つの単一ミクロ装置として導出しない。R164/R190/R170作用殻型代替経路の単一装置統合も別の強化課題である。")
    write(path,s)


def patch_errors() -> None:
    path="sections/08_errors_resources_open_targets.md"
    s=read(path)
    s=re.sub(r"^@status:.*$","@status: M54から派生するQ1/Q2のR191 2結果読出し、R164/R190/R170作用殻型代替経路、Q3の開放jump状態構成、R180受信機構、M37物理実装層を横断比較し、誤差、資源、反証条件、未完成目標を整理する。",s,count=1,flags=re.M)
    s=s.replace("2. R164の有限幅・結果成分間の非対称誤差を、R170の作用殻誤差と系列固有測定機構誤差へ重ねて入れる。","2. R191主線で、R191内部に含めた混合・保護帯・有限温度・捕獲誤差を系列固有測定機構誤差へ重ねて入れる。作用殻型代替経路ではR164/R190/R170の同じ偏差を重複計上しない。")
    s=s.replace("4. R180Cの積因子化誤差を各翼の局所R170誤差へ吸収した上で再び加える。","4. R180Cの積因子化誤差を各翼の局所R191誤差へ吸収した上で再び加える。")
    s=s.replace("R170は容量生成や有限衝突装置を抱えず、上流の静的選択分布を吸収指針変数へ固定する。","R170は一般有限結果集合・作用殻型の代替経路で、上流の静的選択分布を吸収指針変数へ固定する。Q1/Q2の2結果R191主線ではこの誤差項を同時に使わない。")
    old_q1=re.compile(r"(?ms)^## 8\.4 Q1の系列固有誤差\n.*?(?=^### 8\.4\.1 R187)")
    new_q1=r'''## 8.4 Q1の系列固有誤差

R143のR191主線では結果分布誤差と測定後状態誤差を分ける。

```math
\varepsilon_{143}^{\rm dist}
\leq
\varepsilon_{\rm prep}
+\varepsilon_{\rm ctrl}
+\varepsilon_{2m}
+\varepsilon_{191}
+\varepsilon_{\rm node}^{\rm dist}.
```

R191内部の混合、transducer、保護帯、finite-temperature retreat、有限時間未捕獲、捕獲記録をここへ再加算しない。安全結果の測定後状態は

```math
\varepsilon_{143}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt{\tau_{\rm state}}-\eta_F}
```

で別に評価する。R144の固定 $N$ 段逐次測定では

```math
D_{\rm TV}(p_N^{\rm obs},p_N^{\rm id})
\leq
\sum_{j=1}^{N}\varepsilon_{{\rm inst},j}
+
\sum_{j=1}^{N-1}\delta_{{\rm state},j}
```

とする。固定有限列ではR191の指針変数と選別機構用作業領域をR179の開放リセットで再使用し、結果相関履歴を流出浴へ流す。

R189CのQ1-2達成証人では中間R189Aで保持した2作用をR191へ渡し、局所記録と中間振幅再調整を使わない。固定 $N=2$ の正の履歴重みには $p_*=0.10$ の安全下限を取れるため、R191 decision時間を有限に固定した後に $\Omega_\kappa\to0$ として時間ずれを小さくできる。R164/R190/R170の作用殻型実現は代替経路として残し、R191主線の誤差へ重複加算しない。

'''
    s,count=old_q1.subn(new_q1,s,count=1)
    if count!=1: raise RuntimeError("8.4 replacement failed")
    write(path,s)


def patch_verify() -> None:
    path=".github/workflows/verify.yml"
    s=read(path)
    s=s.replace("          grep -Fq 'R170の吸収指針変数' sections/A16_m54_projector_tree_receiver.md\n","          grep -Fq 'R191の2結果選択・吸収記録' sections/A16_m54_projector_tree_receiver.md\n          grep -Fq 'R191による2結果選択と吸収記録' sections/02_common_canonical_modules.md\n          ! grep -Fq '結果成分の排他的選択と固定は第2章R170が担う' sections/A16_m54_projector_tree_receiver.md\n          ! grep -Fq '\\frac{m\\delta}{1+\\delta}' sections/A16_m54_projector_tree_receiver.md\n")
    write(path,s)


def main() -> None:
    patch_a16()
    patch_common()
    patch_status()
    patch_q2_receiver()
    patch_q2_proof()
    patch_q1()
    patch_errors()
    patch_verify()
    print("R191 consistency patch applied")


if __name__ == "__main__":
    main()
