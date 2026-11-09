---
title: "2.13 Generalized Snell law"
short_title: "2.13 Generalized Snell law"
---

(ch02-source-13)=
# 2.13 Generalized Snell law

The classical **Snell law** assumes phase continuity at the interface between homogeneous media. Metasurfaces allow an **abrupt phase shift** across a thickness much smaller than a wavelength. This idea was formulated in 2011 by Capasso and colleagues, introducing the **generalized Snell law**.

Suppose a metasurface lies between media with refractive indices $n_i$ and $n_t$, imposing a spatial phase profile $\Phi(x)$ along the interface. The surface phase gradient, $d\Phi/dx$, contributes additional momentum to phase matching. The relation between incidence angle $\theta_i$ and refraction angle $\theta_t$ becomes:

$$
n_t\sin\theta_t-n_i\sin\theta_i=\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx}.
$$

Here $\lambda_0$ is the vacuum wavelength. In terms of the wave-number magnitudes, $k_i$ and $k_t$, the engineering form is:

$$
k_t\sin\theta_t-k_i\sin\theta_i=\frac{d\Phi}{dx}.
$$

Similarly, reflection into the first medium, of refractive index $n_i$, obeys:

$$
\sin\theta_r-\sin\theta_i=\frac{\lambda_0}{2\pi n_i}\frac{d\Phi}{dx}.
$$

**Physical interpretation:** the $d\Phi/dx$ term shows how a designed phase gradient redirects reflected and transmitted beams (**anomalous reflection/refraction**). This principle underlies flat lenses, beam deflectors, and holographic metasurfaces.

::::{admonition} Booklet example: phase gradients and anomalous angles
:class: book-exercise

A phase-gradient metasurface lies between air and a dielectric. Let $n_1=1$, $n_2=1.5$, and $\lambda_0=10\,\mathrm{mm}$. A wave arrives at $\theta_i=20^\circ$. The imposed phase gradient along $x$ is:

$$
\frac{d\Phi}{dx}=100\,\mathrm{rad/m}.
$$

Use the generalized Snell law to find:

1. The anomalous reflection angle $\theta_r$.
2. The anomalous refraction angle $\theta_t$.
3. The phase difference between adjacent unit cells separated by $p=5\,\mathrm{mm}$.
4. The reflection and refraction angles when the phase gradient is zero.

:::{dropdown} Show / hide the solution
**Wavelength conversion.** First convert millimeters to meters: $\lambda_0=10\,\mathrm{mm}=0.01\,\mathrm m$. Also, $\sin20^\circ\simeq0.342$.

**Anomalous reflection angle.** The generalized reflection law is:

$$
\sin\theta_r-\sin\theta_i=\frac{\lambda_0}{2\pi n_1}\frac{d\Phi}{dx}.
$$

Solving for $\sin\theta_r$:

$$
\sin\theta_r=\sin\theta_i+\frac{\lambda_0}{2\pi n_1}\frac{d\Phi}{dx}.
$$

Substituting the given values:

$$
\sin\theta_r=\sin20^\circ+\frac{0.01}{2\pi(1)}(100).
$$

The phase-gradient contribution is:

$$
\frac{0.01\times100}{2\pi}=\frac1{2\pi}\simeq0.159.
$$

Therefore:

$$
\sin\theta_r=0.342+0.159\simeq0.501.
$$

Consequently:

$$
\theta_r=\sin^{-1}(0.501),\qquad\boxed{\theta_r\simeq30.1^\circ}.
$$

The phase gradient changes the reflection angle from its classical value of $20^\circ$ to approximately $30.1^\circ$.

**Anomalous refraction angle.** The generalized refraction law is:

$$
n_2\sin\theta_t-n_1\sin\theta_i=\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx}.
$$

Solving for $\sin\theta_t$:

$$
n_2\sin\theta_t=n_1\sin\theta_i+\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx}.
$$

Substituting the values:

$$
1.5\sin\theta_t=(1)(\sin20^\circ)+\frac{0.01}{2\pi}(100).
$$

Therefore:

$$
1.5\sin\theta_t=0.342+0.159=0.501.
$$

Consequently:

$$
\sin\theta_t=\frac{0.501}{1.5}\simeq0.334.
$$

Thus:

$$
\theta_t=\sin^{-1}(0.334),\qquad\boxed{\theta_t\simeq19.5^\circ}.
$$

The anomalous refraction angle is approximately $19.5^\circ$.

For comparison, the classical Snell law without a phase gradient gives:

$$
n_1\sin\theta_i=n_2\sin\theta_{t,\mathrm{classic}},
\qquad
\sin\theta_{t,\mathrm{classic}}=\frac1{1.5}\sin20^\circ\simeq0.228.
$$

Therefore:

$$
\boxed{\theta_{t,\mathrm{classic}}\simeq13.2^\circ}.
$$

Thus, the phase gradient changes the refraction angle from $13.2^\circ$ to approximately $19.5^\circ$.

**Phase difference between neighboring cells.** For cells separated by $p$:

$$
\Delta\Phi=\frac{d\Phi}{dx}p.
$$

The cell spacing is $p=5\,\mathrm{mm}=0.005\,\mathrm m$, so:

$$
\Delta\Phi=(100)(0.005),\qquad\boxed{\Delta\Phi=0.5\,\mathrm{rad}}.
$$

Expressed in degrees:

$$
\Delta\Phi=0.5\times\frac{180}\pi,\qquad\boxed{\Delta\Phi\simeq28.6^\circ}.
$$

The required phase difference between adjacent cells is 0.5 radians, approximately $28.6^\circ$.

**Without a phase gradient.** Set $d\Phi/dx=0$.

The reflection law becomes:

$$
\sin\theta_r-\sin\theta_i=0.
$$

Thus $\sin\theta_r=\sin\theta_i$, giving:

$$
\boxed{\theta_r=\theta_i=20^\circ}.
$$

The refraction law becomes:

$$
n_2\sin\theta_t-n_1\sin\theta_i=0,
\qquad n_1\sin\theta_i=n_2\sin\theta_t.
$$

This is the classical Snell law. Therefore:

$$
\boxed{\theta_t\simeq13.2^\circ}.
$$

**Results.** With $d\Phi/dx=100\,\mathrm{rad/m}$:

$$
\boxed{\theta_r\simeq30.1^\circ},\qquad
\boxed{\theta_t\simeq19.5^\circ},\qquad
\boxed{\Delta\Phi=0.5\,\mathrm{rad}\simeq28.6^\circ}.
$$

Without a phase gradient:

$$
\boxed{\theta_r=20^\circ},\qquad \boxed{\theta_t\simeq13.2^\circ}.
$$

The imposed phase gradient adds an effective tangential component to the wave vector and changes the reflection and refraction angles from their classical values.
:::
::::

:::{note} An allowed direction still needs an efficiency
A phase gradient predicts a candidate tangential wave number. A propagating angle exists only when the resulting sine lies between -1 and 1. Reflection and transmission generally have separately defined phase profiles; equal gradients in the example are an assumption. Signs depend on the phase convention. The law alone does not determine efficiency, unwanted diffraction, or coupling. See [Yu and colleagues' original 2011 paper](https://capasso.seas.harvard.edu/publications/light-propagation-phase-discontinuities-generalized-laws-reflection-and) and Chapters 4–5 for the periodic and full-wave checks.
:::

