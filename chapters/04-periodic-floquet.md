---
title: 'Chapter 4: Periodic Structures, Floquet Analysis, and Diffraction Orders'
short_title: Periodicity and diffraction
description: Derive Bloch phases and diffraction channels, distinguish cutoff from propagation, and connect channel maps to validated periodic simulations.
---

# Chapter 4: Periodic Structures, Floquet Analysis, and Diffraction Orders

**Central question:** which beams can leave a periodic metasurface, and what calculation tells us how much power they carry?

Imagine six different elements spaced by $500\,\mathrm{nm}$. Repeat that six-element sequence and illuminate it at a free-space wavelength of $1.55\,\mu\mathrm m$. Can the surface scatter into a nonzero angle in air? Make a prediction before choosing a formula: does the relevant period equal the element spacing or the length of the complete repeated sequence?

This chapter develops the translation symmetry, the allowed wavevectors, and the numerical checks needed to answer that question. The [browser explorer](../labs/04-floquet-lab.md) and [editable notebook](../notebooks/04-floquet-orders.ipynb) calculate channel geometry. The lab also specifies a later full-wave calculation for the channel amplitudes.

:::{note} Evidence available in this chapter
The channel maps, limiting cases, finite-array factors, and flat-interface power checks have analytical models and executable code. The periodic-grating and metasurface solver investigations are detailed lab outlines. No full-wave efficiency or fabricated-device performance is claimed for those structures.
:::


The primary reading now follows the full textbook chapter, printed pages 79–88: all ten sections, four short examples, and the six-part problem with its complete worked solution. Source wording and steps are retained with normalized typography and LaTeX. Scientific qualifications are marked separately. The computational pages below add proofs, original figures, the interactive lab and the notebook.

- [4.1 Introduction: a world of repeating patterns](floquet-section-01.md)
- [4.2 Periodic electromagnetic structures and the unit cell](floquet-section-02.md)
- [4.3 Floquet theorem: the language of periodicity](floquet-section-03.md)
- [4.4 Tangential wavevector and incidence angle](floquet-section-04.md)
- [4.5 Floquet modes and diffraction orders](floquet-section-05.md)
- [4.6 Propagation or evanescence of Floquet modes](floquet-section-06.md)
- [4.7 Grating lobes: energy thieves](floquet-section-07.md)
- [4.8 Diffraction angles of Floquet orders](floquet-section-08.md)
- [4.9 Periodic boundaries and Floquet ports in simulation](floquet-section-09.md)
- [4.10 Floquet analysis and generalized Snell law](floquet-section-10.md)
- [What will we learn to calculate?](floquet-computational-01.md)
- [Find the pattern that actually repeats](floquet-computational-02.md)
- [Translation symmetry and the Bloch phase](floquet-computational-03.md)
- [Derive the Floquet orders](floquet-computational-04.md)
- [Open, grazing, and evanescent channels](floquet-computational-05.md)
- [Two output media, two channel maps](floquet-computational-06.md)
- [Channel existence and diffraction efficiency](floquet-computational-07.md)
- [Finite arrays and grating lobes](floquet-computational-08.md)
- [Phase gradients and generalized refraction](floquet-computational-09.md)
- [From a channel map to a periodic solver](floquet-computational-10.md)
- [Exercises and discussion](floquet-computational-11.md)
- [References and further reading](floquet-computational-12.md)
