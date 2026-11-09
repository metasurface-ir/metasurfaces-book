---
title: "2.14 Generalized sheet transition conditions (GSTCs)"
short_title: "2.14 Generalized sheet transition conditions (GSTCs)"
---

(ch02-source-14)=
# 2.14 Generalized sheet transition conditions (GSTCs)

Classical interface boundary conditions treat the boundary as having zero thickness, relating field jumps directly to electric and magnetic surface currents, $\mathbf J_e$ and $\mathbf J_m$. Although metasurfaces are thin compared with the wavelength, their scattering elements (meta-atoms) have physical thickness and develop electric and magnetic dipole moments when illuminated.

For a macroscopic model, we use **generalized sheet transition conditions (GSTCs)**. The metasurface is represented by an infinitesimally thin sheet with effective electric and magnetic surface susceptibility tensors, $\overline{\overline\chi}_{ee}$ and $\overline{\overline\chi}_{mm}$.

The electric and magnetic field discontinuities across the metasurface relate to equivalent surface currents as follows:

$$
\hat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf J_e,
\qquad
(\mathbf E_2-\mathbf E_1)\times\hat{\mathbf n}=\mathbf J_m.
$$

Here $\hat{\mathbf n}$ points from medium 1 to medium 2. The key feature of the GSTC constitutive model is that $\mathbf J_e$ and $\mathbf J_m$ depend on the **average fields** on the two sides and on the surface susceptibility tensors:

$$
\mathbf J_e=j\omega\varepsilon_0\overline{\overline\chi}_{ee}\mathbf E_{\mathrm{av}}
+j\omega\sqrt{\varepsilon_0\mu_0}\overline{\overline\chi}_{em}\mathbf H_{\mathrm{av}},
$$

$$
\mathbf J_m=j\omega\mu_0\overline{\overline\chi}_{mm}\mathbf H_{\mathrm{av}}
+j\omega\sqrt{\varepsilon_0\mu_0}\overline{\overline\chi}_{me}\mathbf E_{\mathrm{av}}.
$$

In these equations:

- $\mathbf H_{\mathrm{av}}=(\mathbf H_1+\mathbf H_2)/2$ and $\mathbf E_{\mathrm{av}}=(\mathbf E_1+\mathbf E_2)/2$ are the average fields on the two sides.
- $\overline{\overline\chi}_{ee}$ and $\overline{\overline\chi}_{mm}$ describe direct electric and magnetic responses.
- $\overline{\overline\chi}_{em}$ and $\overline{\overline\chi}_{me}$ describe magnetoelectric cross-coupling, which can appear in chiral or asymmetric metasurfaces and is often taken as zero in suitably symmetric structures.

### Why GSTCs matter in design

GSTCs connect macroscopic physics to microscopic metasurface design. We first determine the susceptibility tensors needed for a desired response, such as reflection, absorption, or transmission with a chosen phase. We then optimize the unit-cell geometry to realize those susceptibilities, as later chapters explore.

:::{note} The reduced GSTC model and its normal
Here the normal points from medium 1 toward medium 2, opposite to Section 2.4. The displayed susceptibility equations are a reduced tangential-polarization model. General GSTCs also contain tangential gradients of normal surface polarization and magnetization. Anisotropy and magnetoelectric coupling are distinct properties; symmetry conclusions require the actual geometry, environment, and illumination. The derivation by [Holloway and Kuester](https://arxiv.org/abs/1603.09582) provides a primary reference for the homogenized interface model.
:::

(ch02-section-10)=
### Computational connection: Give a sheet a current


Consider an ideal, local, purely electric surface at normal incidence. Let its sheet admittance be $Y_s$ in siemens, and define the dimensionless quantity $g=\eta_0Y_s$. Because there is no magnetic surface current, tangential electric continuity still gives $t=1+r$. The electric jump condition adds a shunt current:

$$
Y_i(1-r)-Y_t t=g\,t.
$$

Solving yields

$$
r=\frac{Y_i-Y_t-g}{Y_i+Y_t+g},\qquad
t=\frac{2Y_i}{Y_i+Y_t+g},\qquad
A=\frac{4Y_i\operatorname{Re}g}{|Y_i+Y_t+g|^2}.
$$

Here $Y_i=n_i$ and $Y_t=n_t$ at normal incidence. For $\operatorname{Re}g\geq0$, the sheet is passive and $R+T+A=1$. The absorbed power follows directly from $\tfrac12\operatorname{Re}Y_s|E_{\mathrm{sheet}}|^2$, rather than from unexplained missing channels.

This is also an equivalent-circuit language: the wave regions are transmission-line ports and $Y_s$ is a shunt at their junction. A capacitance per square has $Y_s=+i\omega C_s$ and an inductance has $Y_s=-i/(\omega L_s)$. Positive conductance dissipates power. 

For equal air ports and real $g=G\geq0$,

$$
A=\frac{4G}{(2+G)^2}\leq\frac12,
$$

with equality at $G=2$. A larger conductance eventually reflects more strongly instead of absorbing more. This 50% limit belongs to this one-sided, purely electric, equal-medium sheet model. A backed sheet, added magnetic response, different environment, or different illumination changes the problem.

(ch02-section-11)=
### Computational connection: Retrieve only what is identifiable


For the equal-air electric shunt at the common sheet plane,

$$
g=\frac{2(1-t)}{t}.
$$

Before applying it, check the complex continuity relation $t=1+r$, the reference planes, the exterior impedances, and the model assumptions. Near $t=0$, small errors in $t$ can produce large parameter errors; at $t=0$ this inversion is undefined. A passive model should also satisfy the appropriate energy constraints.

An arbitrary finite film or patterned ridge does not automatically meet those conditions. In particular, entrance and exit planes of a finite layer are different planes. Deembedding removes known propagation phases; it does not prove that the remaining response is a local electric shunt. A successful fit at one frequency is not a validation over wavelengths, angles, polarizations, or geometries that were not checked.

The [Chapter 1 model](01-metasurface-foundations.md) introduced two effective response channels. Its balanced electric-like/magnetic-like construction is richer than a pure electric shunt, which enforces $t=1+r$ and cannot independently specify an arbitrary transmission amplitude and phase. General susceptibility-tensor retrieval and bianisotropic sheet synthesis require more unknowns, illuminations, and consistency conditions than the scalar illustration here.

