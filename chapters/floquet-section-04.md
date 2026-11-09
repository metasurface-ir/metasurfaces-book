---
title: "4.4 Tangential wavevector and incidence angle"
---

# 4.4 Tangential wavevector and incidence angle

To understand $k_x$ and $k_y$, picture a plane wave arriving at our metasurface at angle $\theta$ from the normal. If the surface lies in the $xy$ plane and the wave propagates in the $xz$ plane, its tangential wavevector along $x$ is:

$$
k_x=k_0\sin\theta.
$$

Here $k_0=2\pi/\lambda_0$ is the free-space wavenumber and $\lambda_0$ is the wavelength. The phase difference between neighboring cells along $x$ therefore becomes:

$$
\Delta\phi=k_xp=k_0p\sin\theta.
$$

This relation is extremely important! Why? It shows that oblique illumination excites different cells with different phases. The first cell receives one phase, and its neighbor feels the wave slightly later and receives another.

:::{admonition} Example 1: phase difference between neighboring cells
:class: tip

A metasurface operates at $10\,\mathrm{GHz}$ with period $p=10\,\mathrm{mm}$. The wavelength at this frequency is $\lambda_0=30\,\mathrm{mm}$. Find the neighboring-cell phase difference when the wave arrives at $\theta=30^\circ$.

```{dropdown} Show the complete worked answer

$$
\Delta\phi=k_0p\sin\theta=\left(\frac{2\pi}{30}\right)\times10\times\sin30^\circ.
$$

$$
\Delta\phi=\left(\frac{2\pi}{30}\right)\times10\times0.5=\frac{\pi}{3}.
$$

The neighboring-cell phase difference is therefore $60^\circ$.

```
:::

**Golden tip:** at normal incidence, $\theta=0$, so $\sin0=0$ and $\Delta\phi=0$. All metasurface cells are then excited in phase and at the same time.

:::{note} Supplementary clarification
The example assumes free space and the rounded speed of light used by the textbook. In a medium of index $n_i$, use $k_x=n_i k_0\sin\theta_i$. The phrase “later” is an intuition for phase lag, not a calculation of signal arrival or group delay.
:::
