@number: B
@chapter: 付録
@title: 粗視化作用の $C^1$ 評価
@status: 時間粗視化誤差と Fourier 切断誤差を分離し、主定理の評価を補足する。

## B.1 Gaussian 増分の正確な表示

条件付き Gaussian 過程の増分 $\Delta_hX(t)=X(t+h)-X(t)$ に対して

```math
\E^R|\Delta_hX(t)|^2
=
|\mu^R(t+h)-\mu^R(t)|^2
+\Tr\left[
C^R(t+h,t+h)+C^R(t,t)-2C^R(t+h,t)
\right]
```

が厳密に成立する。従って粗視化作用の運動項は、条件付き平均と共分散だけで計算できる。

有限 $N$ でも同じ式が成立する。$C_N^R-C^R=O(1/N)$ なので、増分2乗の有限モード誤差は粗い評価で $O(1/N)$、$h^{-2}$ を掛けた作用誤差は $O(1/(Nh^2))$ となる。

## B.2 時間対角の展開

極限拡散について、$X_t=x$ を固定した短時間増分は

```math
\Delta_hX
=
b_+^R(x,t)h
+\sqrt{2\nu}\Delta_hW
+O_{L^2}(h^{3/2})
```

である。流れの空間依存と雑音の相関による交差項まで含めて平均すると

```math
\E^R
\left[
|\Delta_hX|^2\mid X_t=x
\right]
=
2d\nu h
+h^2
\left[
|b_+^R(x,t)|^2
+2\nu\nabla\cdot b_+^R(x,t)
\right]
+O(h^3).
```

線形流れでは3階剰余を平均・微分した量も一様に有界である。$m/(2h^2)$ を掛けると

```math
\frac m{2h^2}\E^R|\Delta_hX|^2
-\frac{md\nu}{h}
=
\E^R
\left[
\frac m2|b_+^R|^2
+m\nu\nabla\cdot b_+^R
\right]
+O(h).
```

積分上端を $T-h$ で止めたことによる欠落も $O(h)$ である。

## B.3 なぜ発散項が残るか

雑音の主要項 $2d\nu h$ だけを差し引いても、流れと短時間雑音の交差効果は $h^2$ の有限項として残る。それが

```math
m\nu\nabla\cdot b_+^R
```

である。この項を落とすと、極限は正しい Guerra--Morato 作用にならず、Nelson 表示の負の Fisher 項も得られない。

## B.4 Fourier 切断誤差

付録Aの評価から

```math
\|C_N^R-C^R\|_{C^1(K;C([0,T]^2))}
\leq
\frac{C_KT^2}{N}
```

である。増分共分散は4つの共分散値の線形結合なので、

```math
\left|
\E_N^R|\Delta_hX_N|^2
-
\E^R|\Delta_hX|^2
\right|_{C^1(K)}
\leq
\frac{C_KT^2}{N}.
```

従って運動項の差は

```math
\frac{C_KT^2}{Nh^2}
```

で抑えられる。この評価は最適とは限らないが、$N(h/T)^2\to\infty$ という単純な対角極限を与える。

## B.5 2次ポテンシャル

$U(x,t)=x^{\mathsf T}K(t)x/2+\ell(t)^{\mathsf T}x+c(t)$ なら

```math
\E^R[U(X_t,t)]
=
\frac12\mu^R(t)^{\mathsf T}K(t)\mu^R(t)
+\frac12\Tr[K(t)C^R(t,t)]
+\ell(t)^{\mathsf T}\mu^R(t)
+c(t).
```

従ってポテンシャル期待値とそのパラメータ第1微分は、$\mu_N^R$ と $C_N^R$ の $O(1/N)$ 収束から直接従う。これは運動項の $O(1/(Nh^2))$ より小さく、主定理の右辺へ吸収できる。

一般の滑らかな非2次ポテンシャルでは、Gaussian モーメント展開または一様可積分性を用いて同様の結果を拡張できる可能性がある。しかし第1微分には解写像の応答と $\nabla U$ の積が現れるため、本論文では証明が閉じる2次範囲に限定する。

## B.6 パラメータ第1微分

作用を $\theta_j$ で微分すると、平均、共分散、条件付き Schur 項、ポテンシャル係数の微分が現れる。基本行列の微分公式と $R\geq r_*I$ により、全ての係数は $K$ 上で一様有界である。

時間対角展開を微分した剰余も $O(h)$、Fourier 尾部を微分した誤差も $O(T^2/(Nh^2))$ である。有限個の $\theta_j$ について最大を取れば

```math
\|\mathcal A_{N,h}^{R,U}-\mathcal A_{\GM}^{R,U}\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+\frac{T^2}{Nh^2}
\right)
```

を得る。

## B.7 対角尺度の選択

$h/T=N^{-\alpha}$ と置くと、2つの誤差は

```math
N^{-\alpha},
\qquad
N^{2\alpha-1}
```

である。両者を同じ次数にするには $\alpha=1/3$ とすればよい。従って

```math
h_N=TN^{-1/3},
\qquad
\varepsilon_N=O(N^{-1/3})
```

となる。ここで $\varepsilon_N$ は全評価誤差を表す。

この選択は、粗視化窓を短くしすぎると未解像の Fourier 尾部が増幅され、長くしすぎると局所 Nelson 作用から外れる、という物理的な釣り合いを表す。
