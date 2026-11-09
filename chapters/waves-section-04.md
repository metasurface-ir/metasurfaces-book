---
title: "2.4 Boundary conditions between two media"
short_title: "2.4 Boundary conditions between two media"
---

(ch02-source-04)=
# 2.4 Boundary conditions between two media

The differential form of Maxwell's equations describes fields at a continuous point. To find a unique solution to an electromagnetic problem, we must also specify its initial and boundary conditions. Without them, a problem may have infinitely many solutions. In microwave and metasurface engineering, boundary conditions therefore matter as much as the governing equations: the boundaries determine the final field response and how the wave behaves.

Boundary conditions relate fields on either side of an interface. It can be a real interface between two materials, such as air and a dielectric, or an ideal artificial boundary used in a simulation. We usually decompose each field at the interface into two components, as in Figure 1:

- **Normal component, $F_n$:** perpendicular to the surface; its relations follow from the divergence equations, or Gauss laws.
- **Tangential component, $F_t$:** in the interface plane; its relations follow from the curl equations, Faraday and Ampère laws.

```{figure} ../assets/chapter-02/textbook-normal-tangential.svg
:alt: Redrawing of textbook page 22: the field at a two-medium boundary is resolved into normal and tangential components.

Textbook Figure 1: field decomposition at a real or artificial boundary. The vertical arrow is the normal component, $F_n$, the arrow along the interface is $F_t$, and the diagonal arrow is the total field, $\mathbf F$. The picture applies to $\mathbf E$, $\mathbf H$, $\mathbf D$, and $\mathbf B$. Original book redrawing based on source page 22.
```

### 2.4.1 Deriving boundary relations for normal components

To find the normal electric-flux-density relation, we apply the integral form of Gauss law, $\nabla\cdot\mathbf D=\rho$, to a tiny cylindrical volume—a Gaussian pillbox—straddling the interface, as in Figure 2:

$$
\oiint_S\mathbf D\cdot d\mathbf s=Q_{\mathrm{enclosed}}
\quad\Longrightarrow\quad
\iint_{\mathrm{down}}\mathbf D\cdot d\mathbf s
+\iint_{\mathrm{up}}\mathbf D\cdot d\mathbf s=\rho_s\Delta S.
$$

```{figure} ../assets/chapter-02/textbook-gauss-pillbox.svg
:alt: A Gaussian pillbox straddles the boundary; outward area vectors point up at the upper cap and down at the lower cap.

Textbook Figure 2: Gaussian pillbox with one cap in each medium. The cap arrows indicate opposite outward area directions; normal field components and the interface normal are also shown. Original redrawing of source page 23.
```

To obtain a relation exactly at the interface, shrink the cylinder height to zero, $h\to0$. Its side area vanishes, so no finite side flux remains. Taking $\hat{\mathbf n}$ from medium 2 toward medium 1, with $d\mathbf s_1=\Delta S\hat{\mathbf n}$ and $d\mathbf s_2=-\Delta S\hat{\mathbf n}$, converts the cap integrals into products:

$$
-D_{n2}\Delta S+D_{n1}\Delta S=\rho_s\Delta S
\quad\Longrightarrow\quad
\hat{\mathbf n}\cdot(\mathbf D_1-\mathbf D_2)=D_{n1}-D_{n2}=\rho_s.
$$

The jump in normal electric flux density is exactly the free surface-charge density, $\rho_s$. Figure 3 shows how different charges affect the field lines: positive surface charge, $\rho_s>0$, makes the normal component stronger in medium 1 and directs field lines outward from the surface.

```{figure} ../assets/chapter-02/textbook-surface-charge.svg
:alt: Positive, zero and negative surface-charge cases; field-line density differs above and below the surface according to charge sign.

Textbook Figure 3: from left to right, $\rho_s>0$, $\rho_s=0$, and $\rho_s<0$. The normal-field jump is related to surface charge. Original three-panel redrawing of source page 23.
```

Similarly, because there are no magnetic monopoles, $\nabla\cdot\mathbf B=0$, there is no magnetic surface charge, and normal magnetic flux density is continuous:

$$
B_{n1}=B_{n2}.
$$

### 2.4.2 Deriving boundary relations for tangential components

To find the tangential electric-field condition, apply Faraday–Lenz induction to a closed rectangular contour straddling the interface, as in Figure 4:

$$
\oint_C\mathbf E\cdot d\boldsymbol\ell
=-\frac{\partial}{\partial t}\iint_S\mathbf B\cdot d\mathbf s.
$$

```{figure} ../assets/chapter-02/textbook-electric-loop.svg
:alt: A rectangular loop straddles the boundary; opposite horizontal segments have opposite integration directions, with half-heights indicated on the vertical segments.

Textbook Figure 4: a thin Faraday-law loop with horizontal length $a$ and total height $h$. Contributions on opposite sides carry signs from the contour direction. Original redrawing of source page 24.
```

Integrating around a rectangle of width $a$ and height $h$, remembering that opposite segments have opposite directed lengths, gives:

$$
E_{x1}a+E_{y1}\frac h2+E_{y2}\frac h2
-E_{x2}a-E_{y1}\frac h2-E_{y2}\frac h2
=-\frac{\partial B}{\partial t}(ha).
$$

For a finite rate of magnetic-flux change, $\partial B/\partial t$, shrinking the loop height to zero makes the right-hand side vanish. Terms involving $h/2$ vanish as well. Consequently:

$$
E_{x1}=E_{x2}\quad\Longrightarrow\quad
\hat{\mathbf n}\times(\mathbf E_1-\mathbf E_2)=0.
$$

The tangential electric field is therefore continuous across the interface. Figure 5 compares correct and incorrect representations of that continuity.

```{figure} ../assets/chapter-02/textbook-tangential-continuity.svg
:alt: Three panels compare tangential-field continuity: matching components in the first, mismatched components in the second and third.

Textbook Figure 5: the correct case is on the left; the middle and right cases are incorrect. The tangential components must agree, rather than the entire field vectors. Original redrawing of source page 24.
```

Now consider the tangential magnetic field, $\mathbf H$. Applying Ampère–Maxwell law to a similar contour, Figure 6, gives:

$$
\oint_C\mathbf H\cdot d\boldsymbol\ell
=\iint_S\left(\mathbf J+\frac{\partial\mathbf D}{\partial t}\right)\cdot d\mathbf s.
$$

```{figure} ../assets/chapter-02/textbook-magnetic-loop.svg
:alt: Rectangular magnetic-field integration loop across a boundary, with dots representing surface current normal to the drawing plane.

Textbook Figure 6: Ampère loop for the magnetic field and surface-current sheet. Dots indicate current directed out of the drawing plane. Original redrawing of source page 25.
```

Expanding the contour integral as before and taking $h\to0$ removes the displacement-current contribution, $\partial D/\partial t$. At an ordinary dielectric interface, the conduction-current density is finite, so its contribution also vanishes, giving $H_{x1}=H_{x2}$: continuity of the field.

If the lower medium is a conductor, current can instead concentrate into an infinitely thin layer as $h$ approaches zero. We then obtain a **surface-current density, $\mathbf J_s$**:

$$
\mathbf J_s=\lim_{h\to0}(\mathbf J h).
$$

The equation now becomes:

$$
H_{x1}-H_{x2}=J_s.
$$

Its general vector form, with $\hat{\mathbf n}$ pointing from medium 2 to medium 1, is:

$$
\hat{\mathbf n}\times(\mathbf H_1-\mathbf H_2)=\mathbf J_s.
$$

### 2.4.3 Ideal boundaries and their metasurface connection

If medium 2 is a perfect electric conductor, or PEC, time-varying electromagnetic fields do not penetrate it, and the fields inside are zero: $\mathbf H_2=0$ and $\mathbf E_2=0$. The neighboring surface-current relation then takes its simplest form:

$$
\mathbf J_s=\hat{\mathbf n}\times\mathbf H_1.
$$

At a PEC boundary, such as a ground plane behind a metasurface, the induced surface-current density is determined directly by the tangential magnetic field outside the conductor.

:::{tip} Key connection
By patterning metasurface cells, we manipulate these surface currents, $\mathbf J_s$, and surface-charge distributions, $\rho_s$, to create the field discontinuities needed to control a wavefront.
:::

### Corrected summary table: boundary relations to keep beside us

Let's gather the derivation results in one table. The normal $\hat{\mathbf n}$ points from medium 2 to medium 1; $\rho_s$ and $\mathbf J_s$ are free surface charge and current. The media are linear and isotropic, and **there is no magnetic surface current in this table**. The PEC column concerns time-varying fields with zero interior field.

| Quantity | Ordinary boundary with electric surface charge/current | No surface sources | Outside a PEC: medium 2 is the conductor |
| --- | --- | --- | --- |
| Tangential electric field | $\hat{\mathbf n}\times(\mathbf E_1-\mathbf E_2)=0$ | $\mathbf E_{t1}=\mathbf E_{t2}$ | $\mathbf E_{t1}=0$ |
| Normal magnetic field | $\mu_1H_{n1}=\mu_2H_{n2}$ | Same relation; $H_n$ itself need not be continuous when permeability changes | $H_{n1}=0$ |
| Normal electric field | $\varepsilon_1E_{n1}-\varepsilon_2E_{n2}=\rho_s$ | $\varepsilon_1E_{n1}=\varepsilon_2E_{n2}$ | $E_{n1}=\rho_s/\varepsilon_1$ |
| Tangential magnetic field | $\hat{\mathbf n}\times(\mathbf H_1-\mathbf H_2)=\mathbf J_s$ | $\mathbf H_{t1}=\mathbf H_{t2}$ | $\mathbf J_s=\hat{\mathbf n}\times\mathbf H_1$ |
| Tangential magnetic flux density | $\hat{\mathbf n}\times(\mathbf B_1/\mu_1-\mathbf B_2/\mu_2)=\mathbf J_s$ | $\mathbf B_{t1}/\mu_1=\mathbf B_{t2}/\mu_2$ | $\mathbf B_{t1}=\mu_1(\mathbf J_s\times\hat{\mathbf n})$; not generally zero |
| Normal magnetic flux density | $B_{n1}=B_{n2}$ | Same relation | $B_{n1}=0$ |
| Tangential electric flux density | $\mathbf D_{t1}/\varepsilon_1=\mathbf D_{t2}/\varepsilon_2$ | Same relation | $\mathbf D_{t1}=0$ |
| Normal electric flux density | $D_{n1}-D_{n2}=\rho_s$ | $D_{n1}=D_{n2}$ | $D_{n1}=\rho_s$ |

Why does the PEC tangential magnetic-flux entry matter? A conductor's surface current can create a tangential magnetic field, so zero field inside does not imply zero tangential field outside. We also use tangential electric-field continuity only when magnetic surface current is absent; a magnetic equivalent sheet or GSTC model requires reconsidering that assumption. Across an artificial boundary within one unchanged material, all components are continuous when there are no surface sources, so that case needs no repeated column.

*Editorial note:* with the instructor's authorization, the source's page-26 table has been scientifically corrected and shortened by removing repeated columns. This replaces that table; its derivations and accompanying diagrams remain.

::::{admonition} Textbook example: electric field across an interface
:class: book-exercise

Two dielectric media meet at $z=0$. Medium 1, at $z>0$, has relative permittivity $\varepsilon_{r1}=4$; medium 2, at $z<0$, has $\varepsilon_{r2}=2$. There is no free surface charge, $\rho_s=0$. Just below the interface, the field is $\mathbf E_2=(3,0,-4)\,\mathrm{V/m}$. Calculate $\mathbf E_1$ just above the interface in medium 1.

```{figure} ../assets/chapter-02/textbook-electric-interface-example.svg
:alt: Two dielectric half-spaces with a horizontal boundary and vertical z axis; medium 1 is above and medium 2 below.

Textbook example diagram from page 27: the interface is $z=0$, with media 1 and 2 above and below, respectively. Original book redrawing.
```

:::{dropdown} Show / hide answer
First resolve the known field, $\mathbf E_2$, into tangential components in the $xy$ plane and a normal component along $z$:

$$
\mathbf E_{2t}=(3,0,0),\qquad \mathbf E_{2n}=(0,0,-4).
$$

First apply tangential electric-field continuity. The boundary relation says that the tangential component does not change:

$$
\mathbf E_{1t}=\mathbf E_{2t}=(3,0,0).
$$

Next consider the normal component. Since $\rho_s=0$, Gauss law requires normal electric flux density to be continuous:

$$
\mathbf D_{1n}=\mathbf D_{2n}\quad\Longrightarrow\quad
\varepsilon_1\mathbf E_{1n}=\varepsilon_2\mathbf E_{2n}.
$$

Substituting $\varepsilon=\varepsilon_0\varepsilon_r$ gives:

$$
\varepsilon_0\varepsilon_{r1}\mathbf E_{1n}
=\varepsilon_0\varepsilon_{r2}\mathbf E_{2n}
\quad\Longrightarrow\quad 4\mathbf E_{1n}=2(0,0,-4).
$$

$$
\mathbf E_{1n}=\frac24(0,0,-4)=(0,0,-2)\,\mathrm{V/m}.
$$

Finally, combine the normal and tangential components to obtain the electric field in medium 1:

$$
\boxed{\mathbf E_1=\mathbf E_{1t}+\mathbf E_{1n}=(3,0,-2)\,\mathrm{V/m}}.
$$

As the physics requires, the tangential $x$ component passes through unchanged. The normal $z$ component changes because the permittivity changes, and its magnitude decreases.
:::
::::

::::{admonition} Textbook example: magnetic field with a surface current
:class: book-exercise

A uniform surface current $\mathbf J_s=4\hat{\mathbf a}_y\,\mathrm{A/m}$ flows at the boundary of two nonmagnetic dielectric media, $\mu_1=\mu_2=\mu_0$, as shown. Just inside medium 2, at $x<0$, the magnetic field is $\mathbf H_2=(2,3,-1)\,\mathrm{A/m}$. Find $\mathbf H_1$ just inside medium 1, at $x>0$. The unit normal toward medium 1 is $\hat{\mathbf n}=\hat{\mathbf a}_x$.

```{figure} ../assets/chapter-02/textbook-magnetic-interface-example.svg
:alt: Two half-spaces meet in the yz plane; the x axis points into medium 1 and the surface-current arrow lies along y.

Textbook example diagram from page 28: the interface normal points along positive $x$, and the surface current lies along $y$. Original book redrawing.
```

:::{dropdown} Show / hide answer
First resolve the known magnetic field into its normal component along $x$ and tangential component in the $yz$ plane:

$$
\mathbf H_{2n}=(2,0,0)\,\mathrm{A/m},\qquad
\mathbf H_{2t}=(0,3,-1)\,\mathrm{A/m}.
$$

First consider the normal component. Both media have $\mu_1=\mu_2=\mu_0$, and normal magnetic flux is continuous, $B_{n1}=B_{n2}$, so normal magnetic field is also continuous:

$$
\mathbf H_{1n}=\mathbf H_{2n}=(2,0,0)\,\mathrm{A/m}.
$$

Next consider the tangential component. Free surface current makes it discontinuous, according to:

$$
\hat{\mathbf n}\times(\mathbf H_1-\mathbf H_2)=\mathbf J_s
\quad\Longrightarrow\quad
\mathbf H_{1t}-\mathbf H_{2t}=\mathbf J_s\times\hat{\mathbf n}.
$$

Using the normal $\hat{\mathbf n}=\hat{\mathbf a}_x$ from medium 2 to medium 1, rearrange to find the tangential field in medium 1:

$$
\mathbf H_{1t}=\mathbf H_{2t}+(\mathbf J_s\times\hat{\mathbf n}).
$$

Substitute the current $\mathbf J_s=4\hat{\mathbf a}_y$ and normal $\hat{\mathbf a}_x$:

$$
\mathbf J_s\times\hat{\mathbf n}
=(4\hat{\mathbf a}_y)\times\hat{\mathbf a}_x
=4(\hat{\mathbf a}_y\times\hat{\mathbf a}_x)
=-4\hat{\mathbf a}_z=(0,0,-4).
$$

Now add this result to the tangential field in medium 2:

$$
\mathbf H_{1t}=(0,3,-1)+(0,0,-4)=(0,3,-5)\,\mathrm{A/m}.
$$

Finally, combine the normal and tangential components to obtain the total magnetic field in medium 1:

$$
\boxed{\mathbf H_1=\mathbf H_{1n}+\mathbf H_{1t}=(2,3,-5)\,\mathrm{A/m}}.
$$

**Interpreting the result:** normal magnetic flux continuity leaves the $x$ component unchanged. The surface-current sheet creates a tangential magnetic-field jump given by the current crossed with the unit normal.
:::
::::

### 2. Ideal boundaries: playing with PEC and PMC

When analyzing and simulating metasurface unit cells, we often use two hypothetical ideal boundaries:

**A) Perfect electric conductor, PEC:** a medium with infinite conductivity, $\sigma\to\infty$, in which the electric field approaches zero.

- **Boundary condition:** $\hat{\mathbf n}\times\mathbf E=0$; tangential electric field is zero.
- **Reflection:** waves return with a $180^\circ$ phase change, $\Gamma=-1$. This is the ground plane we commonly place behind reflective metasurfaces.

**B) Perfect magnetic conductor, PMC:** this surface does not exist in nature, but it is the mathematical dual of a PEC and has infinite impedance.

- **Boundary condition:** $\hat{\mathbf n}\times\mathbf H=0$; tangential magnetic field is zero.
- **Reflection:** waves return without a phase change, $\Gamma=+1$. Designing a high-impedance surface, or HIS, is an attempt to create an artificial PMC.

### 3. Real-world boundaries: the Leontovich condition, SIBC

Real metals, such as copper and gold, are not perfect conductors; their conductivity is finite, $\sigma<\infty$. The electromagnetic wave penetrates a short distance into the metal, called the skin depth and denoted by $\delta$.

The **Leontovich surface-impedance boundary condition** connects the tangential fields using the surface impedance, $Z_s$:

$$
\mathbf E_t=Z_s(\hat{\mathbf n}\times\mathbf H_t).
$$

Surface impedance is complex:

$$
Z_s=R_s+jX_s=\sqrt{\frac{j\omega\mu}{\sigma}}.
$$

- **Surface resistance, $R_s$:** represents ohmic loss—the effect we seek in an absorbing metasurface.
- **Surface reactance, $X_s$:** represents near-field storage of electric, capacitive energy or magnetic, inductive energy.

### 4. A preview of metasurfaces: generalized sheet transition conditions

The cases above concerned classical homogeneous surfaces. Modern metasurfaces can be **inhomogeneous and graded**. To analyze them, we extend classical boundary relations into **generalized sheet transition conditions, GSTCs**. The field discontinuities, $\Delta\mathbf E$ and $\Delta\mathbf H$, connect directly to the unit cells' electric and magnetic dipole moments. This is precisely where metasurface engineering begins!

:::{note} Read the boundary assumptions with the table
The normal in this source section points from medium 2 toward medium 1. The corrected table assumes ordinary interfaces without equivalent magnetic surface current; an electric surface current can still be present. Tangential electric continuity is not a universal rule once magnetic sheet currents are introduced. PEC statements describe the exterior of an ideal conductor with zero interior time-varying field. The tangential exterior magnetic field can be nonzero and supports surface current. Section 2.14 and the computational connections instead explicitly use the normal from medium 1 toward medium 2; reverse the normal and field difference together.
:::

(ch02-section-05)=
### Computational connection: Ask what is continuous


Place the interface at $z=0$, with unit normal $\widehat{\mathbf n}=\widehat{\mathbf z}$ pointing from region 1 to region 2. Integrating the curl equations across an infinitesimal loop gives the tangential jump conditions

$$
\widehat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf J_s,\qquad
\widehat{\mathbf n}\times(\mathbf E_2-\mathbf E_1)=-\mathbf M_s.
$$

$\mathbf J_s$ is an electric surface-current density in A/m. $\mathbf M_s$ is an equivalent magnetic surface-current density in V/m under this sign convention; it is a useful field-equivalence description, not a requirement for literal magnetic monopoles. With neither surface current, the tangential electric and magnetic fields are continuous. Normal components satisfy the corresponding flux laws; tangential continuity does not mean every Cartesian component of every field is continuous.

```{figure} ../assets/chapter-02/sheet-boundaries.svg
:alt: Interface normal, tangential field jumps, and an electric sheet represented by a shunt admittance at one reference plane.

Boundary conditions connect a field transformation to the current needed to support it. The local electric shunt considered here is one restricted example; general tensor, magnetic, and bianisotropic sheet synthesis requires additional relations.
```

The entire planar interface has the same boundary relation at every $x$. The incident, reflected, and transmitted fields must therefore have matching tangential phase factors:

$$
k_x=n_i k_0\sin\theta_i=n_t k_0\sin\theta_t.
$$

This is phase matching and, for propagating transmission, Snell's law. A periodic surface can add reciprocal-lattice wavevectors, as developed in [Chapter 4](04-periodic-floquet.md). A desired phase profile is consequently a scattering specification, not a replacement for Maxwell's boundary conditions.

