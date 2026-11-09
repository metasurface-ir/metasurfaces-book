---
title: "4.8 Diffraction angles of Floquet orders"
---

# 4.8 Diffraction angles of Floquet orders

If the surrounding medium is free space, it is easy to calculate each Floquet order’s propagation angle using $k_{x,m}=k_0\sin\theta_m$. Substituting the previous relations gives a familiar and beautiful equation:

$$
\sin\theta_m=\sin\theta_i+\frac{m\lambda_0}{p}.
$$

This relation tells us the angle at which order $m$ is launched! Remember, however, that a real beam angle exists only if the right-hand side lies between $-1$ and $1$: a sine cannot lie outside that interval.

:::{admonition} Example: diffraction angles for a 45 mm period
:class: tip

Let $p=45\,\mathrm{mm}$, $f=10\,\mathrm{GHz}$, $\lambda_0=30\,\mathrm{mm}$, and normal incidence $\theta_i=0$. What happens to the first and second positive orders?

```{dropdown} Show the complete worked answer

For the first order, $m=1$:

$$
\sin\theta_1=0+\frac{30}{45}=0.667\quad\Longrightarrow\quad\theta_1\approx41.8^\circ.
$$

The source describes an unwanted beam propagating at $41.8^\circ$! For the second order, $m=2$, the sine would be $1.33$, which is impossible; the second order therefore does not propagate.

```
:::

:::{note} Supplementary clarification
The result gives an allowed direction; an actual beam also needs nonzero coupling. At normal incidence the negative first order is allowed by symmetry too. At $|\sin\theta_m|=1$, classify grazing cutoff separately.
:::
