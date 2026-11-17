---
title: "6.1 Why numerical simulation?"
---

# 6.1 Why numerical simulation?

In previous chapters we saw how electromagnetic theory describes waves at discontinuities and in effective media. Maxwell’s differential and integral equations give a beautiful, complete description of electric and magnetic fields. Mathematical beauty, however, does not make real engineering problems easy to solve.

Closed-form analytical solutions exist for only a few simple, highly symmetric canonical geometries: spheres through Mie theory, infinite cylinders, planar half-spaces, and simple rectangular or circular waveguides. Move away from these geometries and an exact analytical answer becomes extremely complicated, if it is available at all.

## 1. Why do metasurfaces need a numerical solution?

Metasurfaces deliberately use dense arrays of complicated subwavelength elements: split-ring resonators, symmetric or asymmetric patches, crosses, fractals and metal–dielectric multilayers. These are not simple canonical objects.

Three effects make the physics demanding: sharp edges concentrate fields and can produce singular behavior; reactive near fields couple neighboring cells strongly; and material/structural dispersion together with multilayer substrates makes the response depend on frequency and angle. A cell interacts with its neighbors as well as the incident wave.

Lumped RLC circuits and transmission-line approximations provide valuable physical insight, but are insufficient on their own for precise loss, bandwidth and fabrication predictions. Computational electromagnetics (CEM) and full-wave simulation fill that gap.

## 2. Full-wave simulation as virtual prototyping

The source calls methods full-wave when they solve Maxwell’s equations by discretizing space, time or boundaries rather than replacing the field problem by a simplified physical circuit. This virtual laboratory shortens design cycles: simulate and optimize before paying for cleanroom lithography or PCB fabrication.

Couple the solver to genetic, adjoint-gradient or machine-learning algorithms to synthesize the target amplitude and phase. Field visualizations also reveal surface currents, dielectric dissipation and hotspots that are difficult to measure directly in a laboratory.

## 3. Our roadmap

Section 6.2 compares differential/integral and frequency/time-domain methods, starting with FEM, FDTD, MoM and FIT and then adding RCWA. Section 6.3 develops unit cells, periodic boundaries and Floquet ports. Section 6.4 retrieves bulk and sheet parameters. Section 6.5 addresses meshes, convergence, ports and finite arrays.

:::{admonition} Scientific clarification — separate from the source
:class: note
“Full-wave” does not mean assumption-free or automatically accurate. Geometry, constitutive laws, source models, finite resolution and artificial boundaries still matter. The existing executed slab benchmark below deliberately shows excellent discrete power conservation alongside a wrong continuum prediction.
:::
