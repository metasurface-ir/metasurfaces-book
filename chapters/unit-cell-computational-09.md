---
title: "Select a geometry with a feasibility test"
---

# Select a geometry with a feasibility test

For this first design exercise, retain accepted rows with $T\geq0.8$ and minimize the absolute circular phase error. A request is feasible only when that error is at most $5^\circ$.

The saved library supplies a width near $0.24\,\mu\mathrm m$ for a target of $-100^\circ$, with $T\approx0.865$ and phase error about $0.50^\circ$. A target of $0^\circ$ remains unmet under the same criteria; the closest eligible row misses by about $43.73^\circ$. Report this result directly. Expanding the height range, changing the geometry, or revising the objective would define a subsequent design investigation.

Interpolating a response library requires additional checks. Interpolate real/imaginary parts or another representation respecting phase periodicity; verify new geometries with the solver, especially near rapid response changes. For Chapter 10, separate geometry groups before splitting data and retain numerical uncertainties. Fifty related samples at one wavelength are a teaching dataset, with no claim about general AI performance.
