---
title: "Outcomes and the synthesis chain"
---

# Outcomes and the synthesis chain


By completing the chapter, you should be able to:

1. Derive beam-steering and focusing phase profiles under stated wave conventions.
2. Explain spatial sampling, phase quantization, and incomplete library coverage.
3. Select geometries using circular phase errors and power constraints.
4. Distinguish a local-cell prediction from a full-wave assembled structure.
5. Report incident-normalized target power and conditional diffraction purity separately.
6. Analyze a scalar line focus and define its numerical metrics honestly.
7. Derive geometric phase in an explicitly defined circular basis.

The working sequence is **target field → representation → realizable response → geometry → independent verification**. At each arrow, retain the assumptions being introduced. Prerequisites are the [Chapter 4 channel conventions](04-periodic-floquet.md), [Chapter 3 complex responses](03-unit-cell-design.md), Fourier series, and basic linear algebra.

| Model | Question answered | Evidence supplied here |
| --- | --- | --- |
| Ideal continuous mask | What spatial field would produce the desired wave? | Analytical phase profiles |
| Sampled/local mask | What does discretization and a unit-cell library predict? | Exact staircase coefficients and selected responses |
| Periodic full-wave structure | What do the coupled ridges actually scatter? | Converged TE supercell order powers |
| Scalar finite aperture | How does a prescribed finite field propagate? | Line-focus profiles and window/grid checks |
| Analytical Jones matrix | How does a stated anisotropic response transform polarization? | Geometric phase and conversion fractions |

