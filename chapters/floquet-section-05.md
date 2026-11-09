---
title: "4.5 Floquet modes and diffraction orders"
---

# 4.5 Floquet modes and diffraction orders

Floquet’s theorem does more than connect fields in neighboring cells. It reveals a greater secret: the field scattered by a periodic structure can be decomposed into several branches, or spatial modes!

When a wave meets a periodic array, the repeating structure can add spatial momentum to the wave or subtract it. For a one-dimensional structure, the tangential wavenumber of Floquet order $m$ is:

$$
k_{x,m}=k_x+\frac{2\pi m}{p}.
$$

Here:

- $m=0,\pm1,\pm2,\ldots$ labels the Floquet or diffraction order.
- $k_x$ is the incident wave’s initial tangential momentum.
- $2\pi m/p$ is the spatial momentum added by our periodic lattice.

For a two-dimensional structure, extend the relation along both directions:

$$
k_{x,m}=k_x+\frac{2\pi m}{p_x}.
$$

$$
k_{y,n}=k_y+\frac{2\pi n}{p_y}.
$$

In simple terms, each Floquet order $(m,n)$ is a possible pathway for the wave’s energy. Order zero, $m=0$, is the principal, well-behaved reflection or transmission route. The higher orders, $m=\pm1,\pm2,\ldots$, are the mischievous beams that try to divert energy into other directions!

:::{note} Supplementary clarification
These are possible channels. A channel can be open yet have zero amplitude because of symmetry or destructive interference. The structure and boundary matching determine its amplitude.
:::

```{figure} ../assets/chapter-04/channel-maps.png
:alt: Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.

Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.
```
