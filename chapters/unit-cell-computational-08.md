---
title: "Build a response library a colleague can reuse"
---

(3-8-build-a-response-library-a-colleague-can-reuse)=

# Build a response library a colleague can reuse

A useful record preserves more than width and phase:

- **Experiment:** geometry, units, material model, wavelength, angle, polarization, and primitive period.
- **Response:** complex amplitudes, order labels, total and order-resolved powers where necessary, and phase reference planes.
- **Evidence:** solver/source version, environment, numerical controls, refinement changes, residuals, and acceptance thresholds.
- **Scope:** supported parameter domain, excluded physics, and known incomplete design coverage.

The reference JSON combines this metadata with the 50 rows; its CSV is convenient for plotting and later model fitting. The width in each row overrides the illustrative central width in the metadata. Preserve different experiments as versioned datasets rather than merging rows with incompatible references.

```{figure} ../assets/chapter-03/library.png
:alt: Transmission and reflection versus ridge width, wrapped and unwrapped transmission phase, and the complex transmission trajectory.

The computed width sweep spans about $132.04^\circ$ continuously. This height and width range do not provide complete $360^\circ$ coverage, even before imposing a minimum transmission requirement.
```
