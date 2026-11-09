---
title: 'Chapter 5: Metasurface Synthesis'
short_title: Metasurface synthesis
description: Connect target wavefronts to sampled phase profiles, realizable geometries, full-wave diffraction, scalar focusing, and polarization control.
---

# Chapter 5: Metasurface Synthesis

**Central question:** how do we turn a desired outgoing wave into a physical design and evidence that it works?

Chapter 4 identifies the channels a periodic structure can support. Chapter 3 computes how a repeated unit cell responds. Synthesis connects a desired field to geometry, then tests the assembled structure. A target phase profile is a useful starting point; its realization must also satisfy amplitude, polarization, power, and fabrication constraints.

We develop a complete teaching example: a six-cell dielectric beam deflector, selected from periodic-cell data and verified as a full-wave supercell. We then introduce focusing with a scalar aperture model and polarization control with analytical Jones matrices. The [worked examples](05-synthesis-guide.md), [computational lab](../labs/05-synthesis-lab.md), [beam-steering notebook](../notebooks/05-beam-steering.ipynb), and [wavefront-model notebook](../notebooks/05-wavefront-models.ipynb) preserve their separate evidence levels.

:::{note} What has been executed
The beam-steering case uses an original one-dimensional, lossless TE RCWA calculation for an infinitely repeated six-ridge supercell. It includes an expanded unit-cell library, four geometry sequences, all-channel powers, harmonic refinements, and a separate grcwa implementation comparison. Focusing uses scalar angular-spectrum propagation of a prescribed aperture field. Polarization uses ideal analytical Jones matrices. Neither is a full-wave finite metalens or a vector response calculation of the TE ridges. Materials are ideal real constant indices; fabrication and physical broadband performance are outside these runs.
:::

```{figure} ../assets/chapter-05/supercell-geometry.svg
:alt: Three-dimensional cut and x-z cross-section of the expanded six-ridge supercell with ordered widths, common height, incident wave and period.

This saved expanded design has h = 1.80 µm and L = 6Λ = 3.90 µm. All six ridges are solved together, and the entire sequence repeats. The case controls update widths and height together with the diffraction powers. Focusing and Jones examples later in this chapter are separate models.
```



The reading adapts textbook pages 89–118 into seven sections and nineteen worked-question panels. Repeated derivations and substitutions are consolidated, rather than transcribed sentence by sentence. Sign inconsistencies and ideal-model limitations are corrected explicitly. The original computational content, geometry, interactive lab and notebooks remain available below.

- [5.1 From analysis to synthesis](synthesis-section-01.md)
- [5.2 Specify the wave transformation](synthesis-section-02.md)
- [5.3 Translate fields into a macroscopic response](synthesis-section-03.md)
- [5.4 Phase calibration and physical cell placement](synthesis-section-04.md)
- [5.5 Amplitude synthesis and power management](synthesis-section-05.md)
- [5.6 Polarization synthesis and geometric phase](synthesis-section-06.md)
- [5.7 Optimization and inverse design](synthesis-section-07.md)
- [Outcomes and the synthesis chain](synthesis-computational-01.md)
- [Specify a target field before choosing a phase](synthesis-computational-02.md)
- [A phase gradient does not set efficiency](synthesis-computational-03.md)
- [Spatial sampling and phase quantization](synthesis-computational-04.md)
- [Build a realizable phase library](synthesis-computational-05.md)
- [Verify the complete beam-deflector geometry](synthesis-computational-06.md)
- [Validate synthesis at more than one level](synthesis-computational-07.md)
- [Synthesize a focusing wavefront](synthesis-computational-08.md)
- [Amplitude control and polarization](synthesis-computational-09.md)
- [Objectives, constraints, and research extensions](synthesis-computational-10.md)
- [Exercises](synthesis-computational-11.md)
- [## Linked computational investigations](synthesis-computational-12.md)
