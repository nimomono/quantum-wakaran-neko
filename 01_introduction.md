@number: 5
@chapter: 第5章
@title: return phase volume と標準 cosine 則
@status: [F|R|E|P] 明示 Hamiltonian から joint cosine law を導出。二種類の return realization を区別。

## 5.1 relative geometry

第4章の局所 pulse 後の messenger を

$$
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
$$

$$
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
$$

とする。相対角を

$$
\Delta_{a,b}
=
\phi(a)-\phi(b)
+\Theta_A-\Theta_B
$$

と置く。common-future difference action は

$$
I_-
=
\frac14\lVert u_A-u_B\rVert^2
$$

なので、実二次形式の恒等式から

$$
I_-
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{a,b}
\right]
$$

を得る。

cosine は確率公理または複素振幅から導入されたのではない。二つの実 canonical vector の Euclidean inner product

$$
u_A\cdot u_B
=
ABr_Ar_B\cos\Delta_{a,b}
$$

として現れている。

理想 source では

$$
r_A=r_B=r,
\qquad
I_0=\frac{r^2}{2},
\qquad
\Theta_A-\Theta_B=\Phi_0
$$

なので

$$
I_-
=
I_0
\left[
1-AB\cos\{\phi(a)-\phi(b)+\Phi_0\}
\right].
$$

## 5.2 Model A：sublevel-volume realization

soft pair の基準 density を Liouville measure に関して

$$
\rho_s(q_s,p_s)
=
\frac{
\mathbf1_{\{H_s\leq E_{\max}\}}
}{\Omega_1(E_{\max})}
$$

とする。一 harmonic pair の sublevel volume は

$$
\Omega_1(E)
=
\int_{H_s\leq E}dq_s,dp_s
=
\frac{2\pi}{\omega_s}E.
$$

第4章の comparator と terminal condition は

$$
G_R=1
\quad\Longleftrightarrow\quad
H_s\leq\kappa I_-
$$

である。従って、$\kappa I_-\leq E_{\max}$ の範囲で

$$
h_{a,b}(A,B)
=
P_0(H_s\leq\kappa I_-)
=
\frac{\kappa I_-}{E_{\max}}.
$$

全角度と全 outcome でこの条件を満たすには、理想等振幅模型で

$$
E_{\max}\geq2\kappa I_0
$$

と取ればよい。

## 5.3 joint law の規格化

`[E]` により基準 outcome sector を

$$
P_0(A,B\mid a,b)=\frac14
$$

とする。terminal-compatible unnormalized weight は

$$
W_{A B}(a,b)
=
\frac14
\frac{\kappa I_0}{E_{\max}}
\left[
1-AB\cos\Delta_{a,b}
\right]
$$

である。

四 outcome の和は

$$
\sum_{A,B}W_{AB}(a,b)
=
\frac{\kappa I_0}{E_{\max}},
$$

なぜなら

$$
\sum_{A,B}AB=0
$$

だからである。正規化因子は setting に依存しない。従って

$$
\boxed{
P_R(A,B\mid a,b)
=
\frac14
\left[
1-AB\cos\Delta_{a,b}
\right]
}
$$

を得る。

これは通常の正の確率である。$-1\leq\cos\Delta\leq1$ なので

$$
0\leq P_R(A,B\mid a,b)\leq\frac12.
$$

量子論的な負 weight、複素 measure、signed path integral は使用していない。

## 5.4 Model B：literal return-to-ready realization

Model A の terminal region は通常の有限体積を持ち、cosine law を全角度で厳密に与える。ただし $\Pi_R\geq0$ は half-space condition であり、文字通りの ready state への return ではない。

literal return を表すため、二つの soft harmonic pair

$$
H_s=H_{s,1}+H_{s,2}
$$

を用いる。二 pair の shell density は convolution により

$$
g_2(E)
=
\int
\delta(E-H_{s,1}-H_{s,2})d\Gamma_s
=
\frac{(2\pi)^2}{\omega_1\omega_2}E.
$$

comparator 後の

$$
\Pi_R(T)=\kappa I_- -H_s
$$

に対して ideal ready boundary

$$
\Pi_R(T)=0
$$

を surface conditioning として課すと、未読 soft mode の multiplicity は

$$
h(I_-)
\propto
\int
\delta(H_s-\kappa I_-)d\Gamma_s
=
g_2(\kappa I_-)
\propto I_-.
$$

従って Model A と同じ joint law が得られる。

有限分解能 ready cell

$$
|\Pi_R(T)|\leq\varepsilon
$$

では、$\kappa I_->\varepsilon$ かつ cutoff 端から離れた領域で

$$
\int_{\kappa I_- -\varepsilon}^{\kappa I_-+\varepsilon}
g_2(E)dE
=
\frac{8\pi^2\varepsilon\kappa}{\omega_1\omega_2}I_-
$$

が厳密に線形である。$I_-=0$ における完全な zero channel まで再現するには $\varepsilon\to0$ の surface limit を用いる。標準 CHSH angles では全 outcome の $I_-$ が正なので、十分小さい有限 $\varepsilon$ でも線形領域に置ける。

## 5.5 二つの realization の役割

Model A と Model B を混同してはならない。

- Model A は ordinary positive-volume conditioning による、全角度で厳密な existence proof である。
- Model B は time-reversal-even な ready surface $\Pi_R=0$ に近く、物理的 return 解釈を明瞭にするが、有限幅では endpoint correction を持つ。

本論文の中心定理には Model A を用い、`[R]` の物理的動機と apparatus calibration には Model B を用いる。

## 5.6 phase noise と visibility

一般に

$$
\Theta_A-\Theta_B
=
\Phi_0+\delta
$$

とし、$r_A,r_B,\delta$ に source distribution を許す。ただしその分布は outcome sign と setting に依存しないとする。linear return weight を平均すると

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV
\cos\{\phi(a)-\phi(b)+\Phi_0+\delta_0\}
\right],
$$

ここで

$$
V
=
\frac{
2\left|
\left\langle
r_A r_B e^{i\delta}
\right\rangle
\right|
}{
\left\langle
r_A^2+r_B^2
\right\rangle
},
$$

$$
\delta_0
=
\arg
\left\langle
r_A r_B e^{i\delta}
\right\rangle.
$$

Cauchy--Schwarz inequality から $0\leq V\leq1$ である。$V=1$ には等 amplitude と完全 phase lock が必要である。amplitude mismatch、phase diffusion、return-mode leakage はすべて visibility を低下させる。

## 5.7 analyzer angle の表現

本模型が直接生成するのは

$$
\cos[\phi(a)-\phi(b)+\Phi_0]
$$

である。physical analyzer angle と canonical phase の写像 $\phi$ は対象の表現による。

- planar spin-like realization では $\phi(a)=a$ と置ける。
- linear polarization-like realization では double-angle representation $\phi(a)=2a$ が必要になる。

この角度写像は return rule に挿入するのではなく、局所 analyzer Hamiltonian の calibration で独立に測定すべきである。

## 5.8 なぜ線形 volume が標準 cosine を選ぶか

一般の scalar multiplicity を $F(I_-)$ とする。等 amplitude で

$$
I_-(AB=+1)=s(1-c),
$$

$$
I_-(AB=-1)=s(1+c),
\qquad
c=\cos\Delta
$$

なので、相関は

$$
E_F(s,c)
=
\frac{
F[s(1-c)]-F[s(1+c)]
}{
F[s(1-c)]+F[s(1+c)]
}.
$$

同じ apparatus が任意の $s>0$ と $|c|<1$ について

$$
E_F(s,c)=-c
$$

を与えると要求する。$x=s(1-c)$、$y=s(1+c)$ と置けば

$$
yF(x)=xF(y)
$$

が任意の $x,y>0$ に対して成立するため

$$
F(x)=Cx
$$

が従う。

従って一つの固定 amplitude で cosine に fit するだけでは不十分である。同じ apparatus を異なる common amplitude scale で用いたときにも cosine が保たれる scale robustness が、linear Liouville volume を選ぶ実験的判定になる。

## 5.9 非線形 volume と反証可能性

$d$ 個の harmonic soft pair が setting-dependent energy budget を共有する sublevel model では

$$
\Omega_d(E)\propto E^d
$$

となる。$d\neq1$ なら joint law は一般に純粋 cosine でなく、高調波を含む。anharmonic normal form、finite cutoff、追加 soft channel も同様に deviation を生じる。

従って「bath mode が多いほど quantum law に近づく」のではない。setting-dependent 部分が有効に一つの linear phase-volume channel へ縮約され、他 mode が全 outcome に共通の因子として相殺される必要がある。

## 5.10 本章の結論

標準 cosine は二つの独立な幾何から生じる。角度依存性は二つの実 canonical vectors の quadratic difference action、確率への線形変換は一 harmonic pair の sublevel volume、または二 harmonic pair の shell densityから生じる。終端関数へ cosine を直接書き込まず、通常の正の Liouville measure の積分として joint law を得た。
