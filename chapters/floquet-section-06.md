---
title: "4.6 Propagation or evanescence of Floquet modes"
---

# 4.6 Propagation or evanescence of Floquet modes

For each Floquet order, the normal wavenumber $k_z$ follows:

$$
k_{z,mn}=\sqrt{k_0^2-k_{x,m}^2-k_{y,n}^2}.
$$

Here we meet an interesting physical fork in the road:

1. If the radicand is **positive**, $k_z$ is real and that order can propagate through space as a real beam.
2. If the radicand is **negative**, $k_z$ is imaginary. The order becomes an **evanescent wave** that stays close to the surface and cannot travel to the far field.

The source therefore writes the propagation condition as:

$$
k_{x,m}^2+k_{y,n}^2\le k_0^2.
$$

:::{note} Supplementary clarification
The equality in the source inequality is the grazing cutoff: $k_z=0$ and finite field amplitude carries zero normal power. Use strict inequality for an ordinary propagating order. In an exterior of index $n_o$, replace $k_0^2$ by $(n_ok_0)^2$. Choose the outgoing root; for distance $s>0$ away from the surface, $k_z=-i\kappa$ gives $e^{-\kappa s}$ decay.
:::

```{figure} ../assets/chapter-04/outgoing-fields.png
:alt: Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.

Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.
```
