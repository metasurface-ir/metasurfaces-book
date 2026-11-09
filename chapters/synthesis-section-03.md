---
title: "5.3 Translate fields into a macroscopic response"
---

# 5.3 Translate fields into a macroscopic response

The next question is how fields become a physical boundary description. Define the jumps and averages on the two sides of the sheet. The GSTCs connect those jumps to electric and magnetic surface polarizations, including tangential gradients of normal polarizations. Neglecting the normal terms is an additional model assumption; small thickness alone does not justify it. The simple constitutive relations below also omit magnetoelectric coupling.

For a grounded reflective surface, a scalar impedance model is convenient. Fix an outward normal from the load into the incident region and use the associated tangential field orientation. At normal incidence, the impedance/reflection relation below provides an engineering test. A purely electric transmissive sheet may be modeled by a surface admittance acting on the average tangential electric field.

A passive local scalar load has nonnegative resistance; a reactive load is lossless. Negative resistance in this local load model requires power supplied to the port. For a spatially nonlocal surface, lateral power redistribution can invalidate a pointwise load interpretation, so global passivity is the decisive test. Large-angle transformations may require nonlocal transport, auxiliary evanescent fields, or an efficiency compromise.


$$
\Delta\mathbf E_t=\mathbf E_t^+-\mathbf E_t^-,\quad
\Delta\mathbf H_t=\mathbf H_t^+-\mathbf H_t^-,\quad
\mathbf E_{t,\rm av}=\frac{\mathbf E_t^++\mathbf E_t^-}{2},\quad
\mathbf H_{t,\rm av}=\frac{\mathbf H_t^++\mathbf H_t^-}{2}.
$$
$$
\hat{\mathbf z}\times\Delta\mathbf H
=i\omega\mathbf P_{s,t}-\hat{\mathbf z}\times\nabla_t M_{s,z},
\qquad
\Delta\mathbf E\times\hat{\mathbf z}
=i\omega\mu_0\mathbf M_{s,t}-\nabla_t(P_{s,z}/\epsilon_0)\times\hat{\mathbf z}.
$$
$$
\mathbf P_{s,t}=\epsilon_0\overline{\overline\chi}_{ee}\mathbf E_{t,\rm av},\qquad
\mathbf M_{s,t}=\overline{\overline\chi}_{mm}\mathbf H_{t,\rm av}.
$$
$$
Z_s=\eta_0\frac{1+\Gamma}{1-\Gamma},\qquad
\Gamma=\frac{Z_s-\eta_0}{Z_s+\eta_0},\qquad\operatorname{Re}Z_s\ge0.
$$
$$
\hat{\mathbf z}\times\Delta\mathbf H_t=Y_s\mathbf E_{t,\rm av}.
$$


:::{admonition} Worked exercise 1
:class: tip
For a grounded one-port surface at normal incidence, use $\eta_0\simeq377\,\Omega$ and $\Gamma_A=i$, $\Gamma_B=0.5$, $\Gamma_C=1.5$. Find each impedance and classify its local load as lossless reactive, passive lossy, or active. Why is amplitude above one incompatible with a passive isolated one-port? What changes for phase-only reflection?

```{dropdown} Show the answer

$$
Z_A=377\frac{1+i}{1-i}=377\frac{(1+i)^2}{2}=i377\,\Omega,
\quad Z_B=377\frac{1.5}{0.5}=1131\,\Omega,
\quad Z_C=377\frac{2.5}{-0.5}=-1885\,\Omega.
$$
$$
R_B=0.5^2=0.25,\quad A_B=0.75,\qquad R_C=1.5^2=2.25,
\qquad \Gamma=|\Gamma|e^{i\psi},\quad |\Gamma|=1\ \text{(lossless one-port)}.
$$


A is reactive and lossless. B is passive and dissipative: 25% is reflected and 75% absorbed. C would reflect 225% of the incident power and requires supplied energy. A phase-only profile holds the magnitude constant; an ideal lossless one-port has unit magnitude. These conclusions assume the stated isolated scalar one-port, not an arbitrary local field ratio on a nonlocal surface.
```
:::

