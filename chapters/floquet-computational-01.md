---
title: "What will we learn to calculate?"
---

(ch04-section-01)=
# What will we learn to calculate?

After this chapter, you should be able to:

1. Identify a primitive period and distinguish it from an element pitch or computational supercell.
2. Derive the Bloch phase and the tangential wavevectors of Floquet orders.
3. Classify each order separately in the reflection and transmission media, including grazing cutoff.
4. Explain why an allowed channel can have zero amplitude and why closed orders still matter numerically.
5. Set up a periodic scattering calculation and assess its order-resolved power and convergence.

Prerequisites are plane waves, phasors, tangential boundary conditions, Fourier series, and basic complex algebra. The [worked examples and teaching guide](04-floquet-guide.md) include a short learning path.

The surface is near $z=0$, periodic along $x$ with period $\Lambda$, and invariant along $y$ in the introductory model. A plane wave arrives from $z<0$ and travels toward positive $z$. Angles are signed from the relevant outward surface normal, with a positive angle having positive $k_x$.

The incident and transmitted half-spaces are homogeneous, isotropic, lossless media with positive real permittivity and permeability, and positive real indices $n_i$ and $n_t$. We set $k_y=0$ initially. Materials inside a future scattering structure may be more complicated; the real-index channel tests below apply to its homogeneous exterior regions.

| Symbol | Meaning |
| --- | --- |
| $\lambda_0$, $k_0=2\pi/\lambda_0$ | Free-space wavelength and wavenumber |
| $\Lambda$, $G=2\pi/\Lambda$ | Structural period and reciprocal-lattice spacing |
| $k_{x,i}=n_i k_0\sin\theta_i$ | Incident tangential wavevector |
| $m\in\mathbb Z$ | Diffraction-order label under our sign convention |
| $n_o$ | Index of the output region being examined: $n_i$ for reflection or $n_t$ for transmission |
