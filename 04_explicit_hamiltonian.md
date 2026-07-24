@number: E
@chapter: 付録E
@title: 証明台帳と数値検証仕様
@status: 主張ごとの証明状態、最小 Monte Carlo check、今後の有限-flow 検証。

## E.1 証明状態

- **[K]** Bell--CHSH theorem、measurement-dependent simulation、time-symmetric classification、classical Hamiltonian measurement。
- **[F]** 第4章の local rotations、pointer shifts、difference action、comparator shift。
- **[F|R]** fixed terminal condition を用いた terminal compatibility と setting-dependent posterior。
- **[F|R|E|P]** exact joint cosine law、equilibrium no-signalling、CHSH value。
- **[F]** one-pair sublevel volume、two-pair shell density、linear multiplicity uniqueness。
- **[F]** action-register invariant shell 上の messenger polar phase $\vartheta_m=S/\hbar_{\rm eff}$。
- **[R]** terminal return condition を physical full-history measure に用いる原理。
- **[O]** `[R]` の dynamical または cosmological selection。
- **[O]** equilibrium preparation `[E]` の operational stability。
- **[O]** generic finite bath から phase-locked high-visibility source を得る機構。
- **[C/O]** massive pointers、finite-width pulses、anharmonic soft modesを含む完全 mechanical realization。

## E.2 algebraic Monte Carlo check

Model A の Liouville 積分を数値的に検査する最小 algorithm は次である。

1. 各 setting pair について $A,B=\pm1$ を独立に一様 sampling する。
2. $E_s$ を $[0,E_{\max}]$ から一様 sampling する。
3. $I_-=I_0(1-AB\cos\Delta)$ を計算する。
4. numerical integration のため $E_s\leq\kappa I_-$ の sample を terminal-compatible と数える。
5. compatible sample の全 outcome frequencies、marginals、correlation を計算する。

この accept/reject は physical trial selection の提案ではなく、phase-space indicator integral を Monte Carlo 積分する数値手段である。

## E.3 reference parameters

検証用に

$$
r=1,
\qquad
I_0=\frac12,
\qquad
\kappa=1,
\qquad
E_{\max}=2\kappa I_0=1
$$

を用いる。$E_{\max}$ は全角度を覆う最小 cutoff である。標準 CHSH angles を四設定対に用い、各 $4\times10^5$、合計 $1.6\times10^6$ base samples を生成する。解析予測は

$$
E_{00}=E_{01}=E_{10}
=
-\frac1{\sqrt2},
$$

$$
E_{11}=+\frac1{\sqrt2},
\qquad
|\mathcal S|=2\sqrt2.
$$

実装スクリプト `tools/verify_explicit_model.py` は乱数 seed、accepted counts、marginals、correlations、CHSH を出力する。

## E.4 参照実行結果

固定 seed 20260719 で上の設定を走らせると、accepted histories は各 setting pair で約 $2.0\times10^5$、acceptance rate は約 $0.5$ となった。数値結果は

$$
|\mathcal S|_{\rm MC}
=
2.83026,
$$

$$
\max_{a,b,X}
\left|
P_{\rm MC}(X=+1\mid a,b)-\frac12
\right|
=
2.47\times10^{-3},
$$

であり、解析値 $2\sqrt2=2.82843\ldots$ と equilibrium marginal $1/2$ に sampling error 内で一致した。最大 joint-frequency error は $2.29\times10^{-3}$ であった。この結果は algebraic phase-volume integral の実装照合であり、`[R]`、`[E]`、`[P]` の物理的導出を検証するものではない。

## E.5 full Hamiltonian integration

algebraic sampling は Hamiltonian map の数値誤差を検査しない。次の段階では $H_{\rm tot}$ の canonical equations を symplectic integrator で解き、以下を測る。

$$
\epsilon_{\rm symp}
=
\lVert
(D\Phi)^TJD\Phi-J
\rVert,
$$

$$
\epsilon_H
=
\max_t
\frac{|H(t)-H(0)|}{1+|H(0)|},
$$

$$
\epsilon_{\rm map}
=
\max
\left|
\Pi_R(T)-\kappa I_-+H_s
\right|.
$$

ideal map へ収束しても Bell law が自動的に正しいとは限らない。terminal volume を actual numerical flow から再積分する必要がある。

## E.6 robustness grid

次の parameter を独立に走査する。

- phase width $\sigma_\Theta$。
- amplitude ratio $r_A/r_B$。
- comparator pulse width と pointer mass。
- terminal resolution $\varepsilon$。
- soft-mode anharmonicity $\gamma$。
- additional outcome-dependent soft pair 数 $d$。
- seed-sector imbalance $q_{AB}-1/4$。
- clock energy margin と pulse overlap。

各点で $V$、higher harmonics、$\epsilon_{\rm NS}$、$\epsilon_Z$、$D_{\rm TV}$、$|\mathcal S|$ を同時に報告する。

## E.7 pass/fail criteria

中心模型の finite regularization が成功したと判定する最低条件は次である。

1. 同じ $G_R$ と同じ Hamiltonian parameter を全 setting へ用いる。
2. full outcome law が規格化され、未検出 trial を除外しない。
3. $V>1/\sqrt2$ と $\epsilon_{\rm NS}\to0$ が同じ parameter region で成立する。
4. $Z_{a,b}$ の setting dependence が calibration error 以下である。
5. return-volume exponent が $1$ に収束し、higher harmonics が制御される。
6. measurement dependence が source posterior で直接検出される。
7. biased-preparation intervention が signalling を生まない理由を full apparatus model で説明できる。

最後の条件を満たさない場合、本模型は equilibrium-restricted toy model としては成立しても、普遍的な測定理論としては未完成である。

## E.8 結論

本論文の解析定理は単純な Monte Carlo integration で確認できるが、物理的主張の核心は finite-width apparatus と preparation intervention にある。Bell value 単独ではなく、measurement dependence、no-signalling、setting normalization、return exponent、preparability を同じ model run で監査する必要がある。
