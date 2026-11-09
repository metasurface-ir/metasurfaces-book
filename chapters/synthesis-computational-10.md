---
title: "Objectives, constraints, and research extensions"
---

# Objectives, constraints, and research extensions


An optimization objective can penalize complex-response mismatch, undesired orders, and fabrication sensitivity. For example, combine a target-order reward with a penalty on unwanted transmitted/reflected powers, subject to allowed widths, gaps, heights, material properties, and passivity. State the illumination and weighting of wavelengths/angles before optimization. Preserve independent verification conditions rather than selecting them after seeing the best result.

The implemented calculation uses discrete phase matching and a global-offset grid. It does not execute a full geometry optimizer, hologram reconstruction, robust tolerance study, or active learning. Those are useful lab/project extensions connecting to Chapters 6 and 10. A broadband claim additionally requires material dispersion and wavelength-dependent scattering, not only recalculating a monochromatic phase formula.

