# 8.3 Leaky-wave, cavity and holographic antennas

Based on the instructor booklet, pages 211–218.

A periodic perturbation makes a guided wave radiate through a visible Floquet harmonic. Its leakage rate controls the usable aperture and beamwidth. A partially reflecting sheet over a ground plane makes a Fabry–Pérot cavity. Choose height to close the round-trip phase and consider leakage and bandwidth together. In holographic synthesis, interfere a known guided reference with a target radiating wave. Pattern the sheet with the resulting beat spatial frequency and verify unwanted harmonics with the actual feed and finite aperture.

$$
\beta_m=\beta_{\rm sw}+2\pi m/p,\quad \sin\theta_m=\beta_m/k_0,\qquad 2k_0 h=\psi_{\rm PRS}+\psi_{\rm g}+2\pi q.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

At normal incidence the cavity example has $\psi_{\rm PRS}=-108^\circ$. Take the PEC phase as $+180^\circ$. Find the smallest positive height in the phase-only model.

:::{dropdown} Show the worked answer

The reflection phase sum is 72 degrees, so $h=\lambda/10$ for $q=0$. The phase condition alone cannot predict radiation efficiency or usable bandwidth.
:::
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
