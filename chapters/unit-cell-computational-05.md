---
title: "Derive the restricted TE Fourier model"
---

# Derive the restricted TE Fourier model

For a nonmagnetic scalar permittivity and $E_y(x,z)$,

$$
\frac{\partial^2E_y}{\partial x^2}+\frac{\partial^2E_y}{\partial z^2}+k_0^2\epsilon_r(x)E_y=0.
$$

Write $E_y=\sum_m E_m(z)e^{-ik_0\alpha_mx}$ and expand $\epsilon_r(x)$ as a Fourier series. Projection onto the retained harmonics gives

$$
\frac{d^2\mathbf E}{dz^2}+k_0^2(\boldsymbol\epsilon-\mathbf A^2)\mathbf E=0,
\qquad \epsilon_{mn}=\epsilon_{m-n},\quad A_{mn}=\alpha_m\delta_{mn}.
$$

For a centered rectangle with fill fraction $f=w/\Lambda$,

$$
\epsilon_\ell=n_g^2\delta_{\ell0}+(n_r^2-n_g^2)f\,\operatorname{sinc}(\ell f),
\qquad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

These coefficients are analytic, including the $\ell=0$ limit. There is no pixel grid in the course solver. The matrix is Hermitian for these real-index materials, and its eigenproblem is

$$
(\boldsymbol\epsilon-\mathbf A^2)\mathbf W=\mathbf W\mathbf Q^2.
$$

The square roots in $\mathbf Q$ again use nonnegative real/imaginary branches. The derivative-mode matrix is $\mathbf V=\mathbf W\mathbf Q$. To avoid exponentially growing transfer factors, define forward coefficients $\mathbf a$ at the top face and backward coefficients $\mathbf b$ at the bottom face:

$$
\mathbf E(z)=\mathbf W\left[e^{-ik_0\mathbf Qz}\mathbf a+
e^{-ik_0\mathbf Q(h-z)}\mathbf b\right],\qquad
\mathbf P=e^{-ik_0\mathbf Qh}.
$$

Continuity of $E_y$ and its normal derivative, for common permeability, yields

$$
\begin{bmatrix}
\mathbf V+\mathbf Q_i\mathbf W & (\mathbf Q_i\mathbf W-\mathbf V)\mathbf P\\
(\mathbf V-\mathbf Q_t\mathbf W)\mathbf P & -\mathbf V-\mathbf Q_t\mathbf W
\end{bmatrix}
\begin{bmatrix}\mathbf a\\\mathbf b\end{bmatrix}
=\begin{bmatrix}2\mathbf Q_i\mathbf e_0\\\mathbf 0\end{bmatrix}.
$$

Here $\mathbf Q_i$ and $\mathbf Q_t$ are diagonal exterior matrices and $\mathbf e_0$ excites order zero. Recover

$$
\mathbf r=\mathbf W(\mathbf a+\mathbf P\mathbf b)-\mathbf e_0,
\qquad \mathbf t=\mathbf W(\mathbf P\mathbf a+\mathbf b).
$$

The code implements these equations in `solve_cell`. Its `sample_ey` function reconstructs fields inside and outside the ridge layer. `film_reference` supplies a separate scalar Fresnel/Fabry-Perot benchmark. See [Moharam and Gaylord's foundational formulation](https://doi.org/10.1364/JOSA.71.000811) for the broader RCWA method.

:::{warning} Polarization is part of the formulation
This TE reduction uses a continuous tangential electric field at the vertical dielectric interfaces. Changing the input label to TM does not implement TM Maxwell equations or the required Fourier treatment of discontinuous material products. A general vector solver needs its own formulation and convergence evidence.
:::

```{figure} ../assets/chapter-03/fields.png
:alt: Real TE electric field and squared field amplitude around three repeated dielectric ridges.

Original full-wave field reconstruction for the central cell. Outgoing evanescent harmonics contribute to the near field. The squared field amplitude is distinct from power and energy density.
```
