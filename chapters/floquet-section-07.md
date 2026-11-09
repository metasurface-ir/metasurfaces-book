---
title: "4.7 Grating lobes: energy thieves"
---

# 4.7 Grating lobes: energy thieves

One of our most important jobs as metasurface designers is to prevent unwanted Floquet modes from entering the propagation region. These unwanted propagating diffraction modes are called **grating lobes**. They are energy thieves and can severely reduce our design’s efficiency.

For normal incidence, $k_x=0$, on a one-dimensional structure, the tangential component of order $m$ is:

$$
k_{x,m}=\frac{2\pi m}{p}.
$$

To prevent the first orders, $m=\pm1$, from propagating, their tangential momentum must exceed $k_0$, making the preceding section’s radicand negative:

$$
\left|\frac{2\pi}{p}\right|>k_0\quad\Longrightarrow\quad\frac{2\pi}{p}>\frac{2\pi}{\lambda_0}\quad\Longrightarrow\quad p<\lambda_0.
$$

To escape the energy thieves at normal incidence, the essential condition is therefore that the period $p$ be smaller than the wavelength.

In metasurfaces, we usually go further and choose $p<\lambda_0/2$, or even $p<\lambda_0/3$. The source describes this as making the structure appear completely homogeneous to the wave, without grating lobes or unwanted diffraction.

:::{admonition} Example: a 20 mm period
:class: tip

Let $p=20\,\mathrm{mm}$ and $f=10\,\mathrm{GHz}$, so $\lambda_0=30\,\mathrm{mm}$. What happens to the first Floquet orders?

```{dropdown} Show the complete worked answer

Because $p<\lambda_0$, the first orders do not propagate: they remain evanescent. In the source’s intuitive description, all our energy safely stays in order zero, $m=0$.

```
:::

:::{admonition} Example: a 40 mm period
:class: tip

At the same frequency, what happens if we build larger cells with $p=40\,\mathrm{mm}$?

```{dropdown} Show the complete worked answer

Because $p>\lambda_0$, the first orders escape into the propagation region. Our energy can now split: some follows the main route and some goes into unwanted diffraction.

```
:::

:::{note} Supplementary clarification
The textbook’s “all energy stays in order zero” means that no nonzero far-field order is open in the stated free-space, normal-incidence example. Absorption may still occur, and order zero includes reflection and transmission. Small pitch alone does not prove homogenization. Opening an order does not guarantee nonzero power in it. For oblique incidence and different exterior indices, check both half-spaces separately.
:::
