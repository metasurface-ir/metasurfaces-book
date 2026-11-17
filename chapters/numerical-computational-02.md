---
title: "Choose the problem before the solver"
---

# Choose the problem before the solver

First specify illumination, material law, geometry, boundary conditions, the quantity to report, and an accuracy target. A large field image is useful only if its normalization, location, and numerical controls are known.

| Method | Natural use in this course | Controls that need independent refinement |
| --- | --- | --- |
| Exact planar/interface or sheet model | Limits, signs, phase planes, inexpensive design intuition | Physical approximation and parameter validity; no spatial mesh exists |
| RCWA / Fourier modal method | Periodic, layered structures and diffraction channels | Harmonic truncation, material Fourier representation; layer slicing when geometry varies along propagation |
| FDFD | A frequency-domain boundary-value problem on a spatial grid | Mesh, interface representation, boundaries, domain/monitor placement, linear solve |
| FEM | Vector fields on meshes fitted to complex geometries | Element size/order, curved geometry, ports/boundaries, solver tolerance |
| FDTD | Time-resolved fields and spectra from a time-domain excitation | Spatial/time steps, source spectrum, run duration, interface treatment, domain and absorbers |
| Surface integral / BEM | Scattering with suitable piecewise homogeneous regions | Surface mesh, quadrature, linear solve, and background Green function assumptions |

The [Meep introduction](https://meep.readthedocs.io/en/latest/Introduction/) describes its space/time discretization. [MFEM's Maxwell notes](https://mfem.org/maxwell-notes/) explain tangentially conforming edge elements. [SCUFF-EM's implementation documentation](https://github.com/HomerReid/scuff-em/blob/master/doc/docs/forDevelopers/Implementation.md) describes surface-current discretization. These are method references; none of those packages is executed in this lab.

Our ridge RCWA code propagates modal fields analytically through a uniform layer. It has no time step or z mesh to refine. Comparing it with grcwa tests another implementation of the same method family. The new slab FDFD comparison exercises a different family, for the slab geometry only.
