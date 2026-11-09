---
title: "Choose a solver that matches the structure"
---

(3-3-choose-a-solver-that-matches-the-structure)=

# Choose a solver that matches the structure

| Method | Natural use | Numerical controls to vary |
| --- | --- | --- |
| Fourier modal / RCWA | Laterally periodic structures represented as uniform layers along the propagation direction | Fourier harmonics; geometric/material representation; layer slicing for a varying vertical profile |
| Finite elements | Complex shapes, material interfaces, frequency-domain fields | Mesh, polynomial order, exterior boundaries/ports |
| FDTD | Broadband time-domain response and spatially resolved fields | Spatial grid, run time/decay, PML, source/monitor placement |

The course implementation is a restricted RCWA calculation: one rectangular patterned layer with exact Fourier coefficients. Its vertical eigenmode propagation is analytic, so there is no finite-difference $z$ mesh or staircased height to refine. The main truncation is the number of spatial harmonics. A sloped sidewall or vertically varying cell would need additional layers or another solver.

The [Meep grating and mode-decomposition tutorials](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/) provide a useful later FDTD comparison, including flux normalization and phase references. The [grcwa documentation](https://grcwa.readthedocs.io/en/latest/usage.html) describes the separate RCWA implementation used in our numerical audit. Solver conventions must be mapped before comparing signs and amplitudes.
