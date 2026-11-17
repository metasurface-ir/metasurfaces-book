---
title: "6.2.4 FIT: topology first, materials second"
---

# 6.2.4 FIT: topology first, materials second

FIT, introduced by Thomas Weiland, starts from Maxwell’s integral laws. The source describes it as an important basis of CST’s transient solver. Instead of differentiating point samples first, integrate along oriented edges and through oriented faces on a primal mesh and an interleaved dual mesh.

```{figure} ../assets/chapter-06/integral-unknowns.svg
:alt: Left: the four oriented edge voltages in the FIT worked problem. Right: the support of one RWG function used in MoM.

Left: the four oriented edge voltages in the FIT worked problem. Right: the support of one RWG function used in MoM.
```

$$
\oint_{\partial A}\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_A\mathbf B\cdot d\mathbf A,\qquad\oint_{\partial\widetilde A}\mathbf H\cdot d\mathbf l=\frac{d}{dt}\int_{\widetilde A}\mathbf D\cdot d\mathbf A+\int_{\widetilde A}\mathbf J\cdot d\mathbf A.
$$

$$
\int_{\partial V}\mathbf D\cdot d\mathbf A=Q_e,\qquad\int_{\partial V}\mathbf B\cdot d\mathbf A=0.
$$

## 1. Integral unknowns

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\quad\widehat b_j=\int_{A_j}\mathbf B\cdot d\mathbf A,\quad\widehat h_i=\int_{\widetilde L_i}\mathbf H\cdot d\mathbf l,\quad\widehat d_j=\int_{\widetilde A_j}\mathbf D\cdot d\mathbf A.
$$

These are electric edge voltages, primal-face magnetic fluxes, dual-edge magnetic line integrals and dual-face electric fluxes. Their units and orientations differ from pointwise field samples.

## 2. Incidence matrices and Maxwell grid equations

C maps primal edges to oriented face circulations, the dual curl does the same on the dual grid, and S sums oriented face fluxes over a closed cell. Entries are only 0 and ±1: geometry incidence rather than material properties.

$$
C\widehat{\mathbf e}=-\frac d{dt}\widehat{\mathbf b},\quad\widetilde C\widehat{\mathbf h}=\frac d{dt}\widehat{\mathbf d}+\widehat{\mathbf j},\quad S\widehat{\mathbf b}=0,\quad\widetilde S\widehat{\mathbf d}=\mathbf q.
$$

$$
SC=0,\qquad\widetilde S\widetilde C=0,\qquad\widetilde S\widehat{\mathbf j}=-\frac d{dt}\mathbf q.
$$

“The boundary of a boundary is empty”: shared edge contributions cancel on the surface of a closed cell. Apply the dual divergence to Ampère’s equation and charge continuity follows. These topological identities are exact on the chosen mesh.

## 3. Close the system with material matrices

$$
\widehat{\mathbf d}=M_\epsilon\widehat{\mathbf e},\qquad\widehat{\mathbf h}=M_{\mu^{-1}}\widehat{\mathbf b},\qquad\widehat{\mathbf j}=M_\sigma\widehat{\mathbf e}.
$$

These matrices contain material parameters and area/length factors. They may be diagonal on suitable orthogonal grids with simple isotropic constitutive laws; this is not a universal property.

| Law | Continuous form | FIT form |
|---|---|---|
| Faraday | $\nabla\times E=-\partial_tB$ | $C\widehat e=-\partial_t\widehat b$ |
| Ampère | $\nabla\times H=\partial_tD+J$ | $\widetilde C\widehat h=\partial_t\widehat d+\widehat j$ |
| Electric Gauss | $\nabla\cdot D=\rho$ | $\widetilde S\widehat d=q$ |
| Magnetic Gauss | $\nabla\cdot B=0$ | $S\widehat b=0$ |
| Continuity | $\nabla\cdot J=-\partial_t\rho$ | $\widetilde S\widehat j=-\partial_tq$ |

## 4. FIT, FDTD and curved boundaries

On a regular Cartesian grid, conventional constitutive discretization plus explicit staggered time integration can produce the same Yee updates. The viewpoints differ: differential samples versus integral unknowns and incidence. FIT itself can also be formulated in the frequency domain.

A conventional rectangular mesh staircases curved metal/dielectric boundaries. The source describes conformal boundary treatments and CST’s PBA as ways to account for cut areas and improve geometry without refining the entire box. It highlights broadband pulse analysis, active/time-varying elements, and periodic polarization/phase characterization.

:::{admonition} Scientific clarification — separate from the source
:class: note
The source initially says all FIT error enters constitutive relations, then correctly qualifies that statement in its worked example. Incidence identities are exact; final accuracy also depends on geometry, material approximations, time stepping, boundaries and finite resolution. A “perfect” boundary-approximation name does not imply zero numerical error.
:::

:::{admonition} Worked problem
:class: tip
A square primal face of side $\Delta=1\,\mathrm{mm}$ lies in xy with normal +z and counterclockwise circulation. Edge reference directions 1,2 agree with traversal and 3,4 oppose it. At time n, voltages are $[0.30,0.20,0.10,0.05]\,\mathrm V$; initial flux is $2.00\times10^{-10}\,\mathrm{Wb}$ and $\Delta t=1.0\,\mathrm{ps}$.

1. Calculate circulation and the corresponding C row.
2. Update magnetic flux.
3. In vacuum, with primal area $\Delta^2$ and dual length $\Delta$, find the dual magnetic line integral.
4. Explain magnetic Gauss preservation from SC=0.
5. Relate regular-grid explicit FIT to Yee FDTD; is FIT only time domain?

```{dropdown} Show the complete worked answer

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\qquad(C\widehat{\mathbf e}^{,n})_f=\widehat e_1^n+\widehat e_2^n-\widehat e_3^n-\widehat e_4^n.
$$

$$
(C\widehat{\mathbf e}^{,n})_f=0.30+0.20-0.10-0.05=0.35\,\mathrm V,\qquad C_{f,\{1,2,3,4\}}=[1,1,-1,-1].
$$

These signs come from orientation, not permittivity or permeability. Faraday on staggered times gives

$$
C\widehat{\mathbf e}=-\frac{d\widehat{\mathbf b}}{dt},\qquad\frac{\widehat b^{n+1/2}-\widehat b^{n-1/2}}{\Delta t}=-(C\widehat{\mathbf e}^{,n})_f.
$$

$$
\widehat b^{n+1/2}=\widehat b^{n-1/2}-\Delta t(C\widehat{\mathbf e}^{,n})_f=2.00\times10^{-10}-(1.0\times10^{-12})(0.35)=1.9965\times10^{-10}\,\mathrm{Wb}.
$$

The unit check is volts times seconds equals webers. To obtain a magnetic line integral, topology alone is insufficient: use the material relation.

$$
\widehat h=M_{\mu^{-1}}\widehat b\approx\frac{\widetilde\ell}{\mu_0A}\widehat b,\quad A=\Delta^2,\quad\widetilde\ell=\Delta.
$$

$$
\widehat h^{n+1/2}\approx\frac{\widehat b^{n+1/2}}{\mu_0\Delta}=\frac{1.9965\times10^{-10}}{(4\pi\times10^{-7})(10^{-3})}\approx0.159\,\mathrm A.
$$

$$
\widehat h=\int_{\widetilde L}\mathbf H\cdot d\mathbf l,\qquad H\approx\widehat h/\widetilde\ell\approx159\,\mathrm{A/m}.
$$

The line integral has amperes as its unit, not amperes per meter. The final conversion assumes approximately uniform H; material interfaces and complicated grids require a better constitutive approximation.

$$
SC=0,\qquad SC\widehat{\mathbf e}=-S\frac{d\widehat{\mathbf b}}{dt}\quad\Longrightarrow\quad\frac d{dt}(S\widehat{\mathbf b})=0.
$$

Hence an initially zero discrete magnetic divergence stays zero under a compatible update. This preserves consistent initial data; it does not repair inconsistent initial fluxes. On a regular Cartesian mesh with standard material matrices and leapfrog time stepping, FIT can give the Yee updates. Its integral/topological formulation also admits frequency-domain solutions.

```
:::
