# 証明状態と理論の境界

## 第I部主定理：線形 Gaussian パラメータ $C^1$ 収束

次の範囲で完結した定理として記述する。

- finite Fourier--Gaussian driving。
- time-dependent coefficient を許す linear flow。
- Gaussian initial distribution。
- positive finite-resolution terminal record。
- quadratic 以下の external potential。
- compact smooth finite-dimensional parameter family。
- $h_N\to0$ かつ $N(h_N/T)^2\to\infty$。

この条件で、

$$
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\rm GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+
\frac{T^2}{Nh^2}
\right).
$$

$h_N=TN^{-1/3}$ なら $O(N^{-1/3})$ である。$C^1$ は指定した finite-dimensional parameter set $K$ 上の norm であり、arbitrary infinite-dimensional path variation ではない。

## 第II部主定理：二モード台帳 Bell compatibility

仮定：

1. `[H]` finite Hamiltonian local apparatus、common-future comparator、相補的 internal-clock realization。
2. `[P]` phase-locked source と visibility $V$。
3. `[S]` independent sign-flip symmetric preparation。
4. `[M]` fixed-total-action two-mode entrance measure。
5. `[R]` time-symmetric boundary-statistical principle。
6. source support 上の working range

   $$
   0\leq E_*+\kappa I_-\leq E_\ell.
   $$

このとき

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV_{\rm eff}\cos\Delta_{ab}
\right],
$$

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V.
$$

## 厳密に導出した部分

### finite apparatus

- local messenger rotation。
- bright momentum shift。
- anchor pointer shift。
- common-future difference action。
- return pair と center pair から二つの内部時計対への canonical transformation。
- $P_c=0$ 上の相補的時計運動。
- relative-clock shift

  $$
  \Pi_R=E_*+\kappa I_- -h.
  $$

- terminal half-space と順序付き時計向き保存条件の同値性。

### geometry and measure

- quadratic difference action

  $$
  \overline I_-^{AB}
  =
  I_0
  \left[
  1-ABV\cos\Delta_{ab}
  \right].
  $$

- two-mode fixed-action shell

  $$
  p(h)=\frac1{E_\ell}.
  $$

- symmetric sector mass

  $$
  w_{AB}=\frac14.
  $$

- terminal-compatible weight

  $$
  W_{AB}
  =
  \frac{w_{AB}}{E_\ell}
  \left[
  E_*+\kappa\overline I_-^{AB}
  \right].
  $$

### Bell audit

- local deterministic response at fixed complete microstate。
- measurement independence failure。
- setting-independent normalization $Z_{a,b}$。
- equilibrium no-signalling。
- $|\mathcal S|=2\sqrt2V_{\rm eff}$。
- minimal coarse posterior の

  $$
  D_{\rm TV}(c,c')
  =
  \frac{V_{\rm eff}}2|c-c'|.
  $$

## 条件付きまたは未導出の部分

### `[R]`

`[R]` は Hamilton equations、finiteness、recurrence、time reversal、または相補的時計運動量だけからは導いていない。相補時計は

$$
G_R
=
\mathbf1_{\{\Pi_R(T)\geq0\}}
$$

の半空間を向き保存条件として導くが、$\Pi_R(T)<0$ の軌道も Hamiltonian 解として残る。physical history ensemble を指定する独立原理が必要である。

branch-wise boundary preparation と同一履歴 matching を追加すれば、

$$
d\nu
\propto
\rho_S(z_i)
G_R(z_f)
\delta
\left(
z_f-\Phi^Tz_i
\right)
d\Gamma_i\,d\Gamma_f
$$

から `[R]` の積形式を条件付きで得る。ただし matching rule 自体は未導出である。

### mixing

fixed shell Liouville entrance measure を直接準備すれば $p(h)=1/E_\ell$ は厳密である。一つの deterministic microstate の long-time histogram から同じ分布を得るには、

$$
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}
$$

という coarse-grained mixing assumption が必要である。arbitrary fine-grained density の strong convergence は起こらない。

### preparation

`[S]` は symmetric preparation macrostate と invariant reference measure を採用する統計条件を含む。arbitrary biased preparation に対する no-signalling は証明していない。

### uniqueness

quadratic comparator、two-mode ledger、cos law、Tsirelson value が、より深い Hamiltonian principle から一意に選ばれることは証明していない。

## 否定結果

- local record 後の forward shared-bath coupling は outcome-sector Liouville mass を変えない。
- result-dependent residence time は trial-number frequency を変えない。
- timeout または incomplete trial exclusion は postselection を生む。
- $N>1$ ledger mode の cumulative weight

  $$
  F_N(x)
  =
  1-
  \left(
  1-\frac{x}{E_\ell}
  \right)^N
  $$

  は nonlinear で、高調波を生む。
- Bell cosine law は Wallstrom circulation quantization を含意しない。
- 同じ scalar readout に対する二つの相補的 terminal half-space を等重みで平均すると

  $$
  \frac12
  \left[
  \frac{x}{E_\ell}
  +
  1-\frac{x}{E_\ell}
  \right]
  =
  \frac12
  $$

  となり、Bell の cos 項が消える。

## 最重要の未解決問題

1. branch-wise boundary preparation と matching をより大きな closed-boundary physical theory から導けるか。
2. finite nonlinear mixer について必要な mixing window と perturbation tolerance を定量化できるか。
3. biased preparation apparatus を含めても no-signalling symmetry が回復するか。
4. two-mode ledger の isolation と action conservation を mechanical model でどこまで保てるか。
5. quadratic comparator と Tsirelson bound を追加原理から選べるか。
6. 順序付き時計 sector と comparator kick を時間反転共変な doubled model に完成できるか。
7. Nelson phase と source action-angle phase を結び、Wallstrom quantization へ進めるか。
