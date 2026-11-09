---
title: "From a channel map to a periodic solver"
---

(ch04-section-10)=
# From a channel map to a periodic solver

Start with a homogeneous or flat-interface cell whose response is analytically known. Then introduce a simple grating. Use the following checks before a large parameter sweep:

1. Specify coordinates, the actual period, excitation, exterior indices, polarization, and phasor convention.
2. Apply the correct lateral Bloch phase and check that a translated incident wave satisfies it.
3. Use homogeneous exterior regions and outgoing ports or suitable absorbing boundaries. Include every propagating order across the complete sweep on both sides.
4. Match solver order labels to tangential wavevectors; a solver may index orders with a different sign or basis.
5. Normalize incident and outgoing power consistently. Compare modal power with an independent flux calculation where available.
6. Refine mesh, harmonic truncation, port distance, or domain/PML settings as appropriate. Power balance alone cannot establish convergence of each order's amplitude or phase.
7. Record reference planes, complex coefficients, failures, and the residual in all-channel power accounting.

The [full-wave lab outline](../labs/04-floquet-lab.md) gives a staged flat-interface, dielectric-grating, and optional six-pillar investigation. The official [COMSOL beam-deflector example](https://www.comsol.com/model/metasurface-beam-deflector-115971) provides a concrete six-post Si/SiO2 reference using periodic boundaries and diffraction-order ports. Its supplied geometry and solver instructions are external reference material; our executed results here are analytical.

### Beyond the introductory model

For a two-dimensional lattice,

$$
\mathbf k_{\parallel,mn}=\mathbf k_{\parallel,i}+m\mathbf G_1+n\mathbf G_2.
$$

In an isotropic lossless exterior, compare its squared magnitude with $(n_o k_0)^2$. The notebook includes a small rectangular-lattice example so that the one-dimensional condition is not mistaken for a general two-dimensional rule. Lossy, anisotropic, nonlocal, or time-modulated systems require an appropriate dispersion relation and outgoing-wave/energy-flow analysis. A real-angle `arcsin` test is not a universal classification algorithm.
