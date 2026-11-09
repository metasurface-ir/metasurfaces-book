---
title: "Chapter 3: Unit-cell design and simulation"
---

# Chapter 3: Unit-cell design and simulation

Roll up your sleeves! Follow the textbook from the meta-atom to the complete array, then use the retained computational investigation to test what a response library can actually support.

The primary reading follows printed pages 70–78 of the instructor-supplied booklet. Its numbering jumps from 3.2 to 3.4 and from 3.6 to 3.9; the six reading pages here use consecutive numbering. The worked steering and metalens examples retain their data and calculations. Typographical repetitions in the source answer are normalized. Scientific qualifications are identified separately.

- [3.1 Introduction: why a unit cell?](unit-cell-section-01.md)
- [3.2 Choosing the meta-atom geometry: tuning resonators](unit-cell-section-02.md)
- [3.3 Reading the scattering parameters](unit-cell-section-03.md)
- [3.4 Parametric sweeps: building a design dictionary](unit-cell-section-04.md)
- [3.5 Array design: from building blocks to a surface](unit-cell-section-05.md)
- [3.6 Simulating the complete array](unit-cell-section-06.md)

## Computational connections retained

- [Outcomes and prerequisites](unit-cell-computational-01.md)
- [Define the electromagnetic experiment](unit-cell-computational-02.md)
- [Choose a solver that matches the structure](unit-cell-computational-03.md)
- [Channels, complex amplitudes, and power](unit-cell-computational-04.md)
- [Derive the restricted TE Fourier model](unit-cell-computational-05.md)
- [Extract phase at stated reference planes](unit-cell-computational-06.md)
- [Validate before exporting](unit-cell-computational-07.md)
- [Build a response library a colleague can reuse](unit-cell-computational-08.md)
- [Select a geometry with a feasibility test](unit-cell-computational-09.md)
- [From a periodic library to a real device](unit-cell-computational-10.md)
- [Exercises](unit-cell-computational-11.md)
- [Linked computational investigations](unit-cell-computational-12.md)

**Central question:** how can a geometry become a trustworthy entry in a metasurface design library?

Suppose a design calls for a transmitted phase of $-100^\circ$ and at least 80% transmitted power. A width sweep produces many colorful phase values. Which geometry should you choose? Before choosing, establish what field was normalized, where its phase was measured, which outgoing channels were included, and whether increasing numerical resolution changes the answer.

This computational chapter builds that chain of evidence. It follows the [Floquet conventions of Chapter 4](04-periodic-floquet.md), then calculates the amplitudes those channels carry. The [worked examples](03-unit-cell-guide.md), [lab and browser explorer](../labs/03-unit-cell-lab.md), and [executed notebook](../notebooks/03-unit-cell-library.ipynb) share one original Python solver and one exported dataset.

:::{note} Evidence available
The reference run is a full-wave, frequency-domain calculation for a **one-dimensional dielectric ridge grating under TE illumination**. It includes analytical interface/film checks, harmonic refinements, a separate grcwa implementation comparison, near-field reconstruction, and 50 accepted library entries. A two-dimensional lattice of posts, a finite metasurface, TM polarization, material dispersion, and fabrication are outside this reference model. Additional FEM/FDTD and supercell investigations are prepared as lab extensions.
:::

```{figure} ../assets/chapter-03/unit-cell-geometry.svg
:alt: The simulated ridge unit cell: three-dimensional cut and x-z section with periodic boundaries, dimensions, TE illumination and scattering reference planes.

The reference width is 0.325 µm; the library sweeps w while keeping period, height and materials fixed. The ridges extend indefinitely along y and repeat along x. Purple dashed lines identify one unit cell. The lab drawing updates with the selected width.
```
