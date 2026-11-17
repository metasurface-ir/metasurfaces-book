---
title: "6.2.3 Method of moments: solve for the currents"
---

# 6.2.3 Method of moments: solve for the currents

If FEM and FDTD mesh the whole volume, MoM asks a practical question: why mesh empty space when a suitable integral formulation can solve only the object? It is especially useful for radiation, scattering, frequency-selective surfaces and thin metal arrays. The source names FEKO and integral solvers in CST as examples.

## 1. From fields to a surface integral equation

The incident wave induces surface currents. Those currents behave like microscopic antennas and radiate the scattered field. The total field is their sum. At a PEC surface its tangential component vanishes:

$$
\mathbf E_{\rm total}=\mathbf E_{\rm inc}+\mathbf E_{\rm scat},\qquad[\mathbf E_{\rm scat}(\mathbf J_s)]_t=-\mathbf E_{{\rm inc},t}.
$$

Choose the integral-operator sign so that the excitation is on the right:

$$
\mathcal L(\mathbf J_s)=\mathbf E_{{\rm inc},t}.
$$

The unknown is surface-current density, the operator is linear integral–differential, and the input is the tangential incident field. A suitable outgoing Green function already contains radiation to infinity: a free-space surface-integral model needs no exterior PML or arbitrary air-box truncation.

## 2. Triangles and RWG basis functions

Mesh the surface into triangles. Each Rao–Wilton–Glisson function lives on two triangles sharing an oriented edge. Current crosses that common edge continuously in the appropriate normal-to-edge component; the surface divergence is piecewise defined.

$$
\mathbf f_n(\mathbf r)=\begin{cases}\dfrac{\ell_n}{2A_n^+}(\mathbf r-\mathbf r_n^+),&\mathbf r\in T_n^+,\\\dfrac{\ell_n}{2A_n^-}(\mathbf r_n^--\mathbf r),&\mathbf r\in T_n^-,\\0,&\text{elsewhere}.\end{cases}
$$

The edge length and triangle areas enter explicitly. Expand the total current using unknown coefficients:

$$
\mathbf J_s(\mathbf r)\approx\sum_{n=1}^NI_n\mathbf f_n(\mathbf r).
$$

## 3. Galerkin testing and the impedance matrix

$$
\left\langle\mathbf f_m,\mathcal L\!\left(\sum_{n=1}^NI_n\mathbf f_n\right)\right\rangle=\langle\mathbf f_m,\mathbf E_{{\rm inc},t}\rangle,\qquad m=1,\ldots,N.
$$

$$
[Z]_{N\times N}[I]_{N\times1}=[V]_{N\times1}.
$$

Each impedance entry measures coupling from one basis current to one test function. The coefficient vector describes current amplitudes/phases, and the excitation vector is the tested incident field. The usual matrix is dense because distant currents still interact.

| Quantity | Physical meaning | Typical numerical cost/shape |
|---|---|---|
| $Z$ | Mutual field coupling | Dense complex matrix; $\mathcal O(N^2)$ storage |
| $I$ | Current coefficients | $N\times1$ vector |
| $V$ | Tested incident field | $N\times1$ vector |
| Solve $ZI=V$ | Coupled response | Dense direct factorization typically $\mathcal O(N^3)$ |

## 4. The bottleneck and MLFMM

With hundreds of thousands of unknowns, a dense matrix can exhaust memory. Multilevel fast multipole methods compute nearby interactions directly and approximate distant interactions through hierarchical clusters and multipole representations. In iterative solvers such as GMRES, typical storage and matrix–vector products can approach O(N log N).

## 5. Periodic MoM

For an infinite cell array, replace the free-space Green function by its Floquet-periodic sum:

$$
G_{\rm per}(\mathbf r,\mathbf r^{\prime})=\sum_{p,q\in\mathbb Z}G(\mathbf r,\mathbf r^{\prime}+pD_x\hat{\mathbf x}+qD_y\hat{\mathbf y})e^{-i(k_{x0}pD_x+k_{y0}qD_y)}.
$$

Only one cell is meshed, but its interaction with the repeated array enters the operator. Periodic Green sums still need accurate evaluation and convergence treatment.

:::{admonition} Worked problem
:class: tip
For a PEC patch expanded in three RWG functions, use

$$Z=\begin{bmatrix}50+20i&10-5i&5+2i\\10-5i&45+18i&8-4i\\5+2i&8-4i&40+15i\end{bmatrix}\,\Omega,\quad V=\begin{bmatrix}1\\0.8e^{-i30^\circ}\\0.4e^{i45^\circ}\end{bmatrix}\,\mathrm V.$$

1. Explain where Z, I and V come from.
2. Solve for complex current coefficients and give their magnitudes/phases.
3. Why are off-diagonal entries nonzero?
4. Estimate dense complex128 matrix storage for N=50,000 (16 bytes/entry).
5. What does MLFMM reduce, and is total solve time always O(N log N)?

```{dropdown} Show the complete worked answer

$$
\mathbf J_s\approx\sum_nI_n\mathbf f_n,\quad\sum_nZ_{mn}I_n=V_m,\quad Z_{mn}=\langle\mathbf f_m,\mathcal L\{\mathbf f_n\}\rangle,\quad V_m=\langle\mathbf f_m,\mathbf E_{{\rm inc},t}\rangle.
$$

The operator sign is defined to put incident excitation on the right. Convert the excitation to Cartesian form:

$$
0.8e^{-i30^\circ}=0.6928-0.4000i,\qquad0.4e^{i45^\circ}=0.2828+0.2828i.
$$

$$
\begin{bmatrix}50+20i&10-5i&5+2i\\10-5i&45+18i&8-4i\\5+2i&8-4i&40+15i\end{bmatrix}\begin{bmatrix}I_1\\I_2\\I_3\end{bmatrix}=\begin{bmatrix}1\\0.6928-0.4000i\\0.2828+0.2828i\end{bmatrix}.
$$

The source reports the following approximate solution; the independently recomputed answer is provided after this panel.

$$
I_1\approx0.01735-0.00854i,\quad I_2\approx0.00856-0.00819i,\quad I_3\approx0.00555+0.00513i\quad\mathrm A.\quad\text{[printed]}
$$

| Coefficient | Printed magnitude | Printed phase |
|---|---|---|
| $I_1$ | 19.33 mA | $-26.2^\circ$ |
| $I_2$ | 11.85 mA | $-43.7^\circ$ |
| $I_3$ | 7.56 mA | $42.8^\circ$ |

Currents differ because each basis feels both direct excitation and every other basis current. For example, $Z_{12}=10-5i\,\Omega$ represents coupling from basis 2 to test 1. Geometry, frequency, background and integral formulation determine those entries; reciprocity can give complex symmetry under appropriate testing, not Hermitian symmetry in general.

$$
M=16N^2\,\mathrm{byte},\quad M(50000)=16(50000)^2=40\times10^9\,\mathrm{byte}\approx40\,\mathrm{GB}\approx37.3\,\mathrm{GiB}.
$$

This is just the matrix: vectors, factorization, preconditioners and solver workspaces need more. Quadrupling N to 200,000 multiplies storage by sixteen:

$$
M(200000)=640\,\mathrm{GB}\approx596\,\mathrm{GiB}.
$$

MLFMM accelerates repeated ZI products by separating near and far interactions. Total time also includes iteration count, setup and preconditioning:

$$
T_{\rm total}\approx n_{\rm iter}T_{\rm matvec}+T_{\rm setup}+T_{\rm preconditioner}.
$$

A poorly conditioned problem can require many iterations. Do not replace a per-product scaling statement by an unconditional total-time guarantee.

```
:::

:::{admonition} Independent numerical check
:class: note
Solving the supplied matrix directly gives

$$
I_1=0.01704858-0.00527665i,\quad I_2=0.00672893-0.00912228i,\quad I_3=0.00680192+0.00682485i\quad\mathrm A.
$$

$$
|I|=[17.84649,11.33554,9.63559]\,\mathrm{mA},\quad\arg I=[-17.19763,-53.58613,45.09640]^\circ.
$$

The relative residual of the printed current vector is about 0.168, whereas the recomputed vector gives about $3.4\times10^{-16}$. This discrepancy is too large to be rounding. The independent [worked-arithmetic report](../data/chapter-06/textbook-checks.json) and reproducible checker preserve both cases.
:::
