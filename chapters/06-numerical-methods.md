---
title: "Chapter 6: Numerical Modeling and Simulation Methods"
---

(chapter-06-overview)=
# Chapter 6: Numerical Modeling and Simulation Methods

Start with the instructor-supplied primary reading, printed pages 121–176 of the updated booklet. Follow the five major sections and the five method pages in Section 6.2. All seven worked problems are included with intermediate calculations and expandable answers. Separately labeled corrections address source algebra, boundary signs and model assumptions.

The existing executed slab benchmark, figures, interactive explorer, guide and notebook remain available as computational connections. The new worked-arithmetic checker verifies the supplied examples; it is distinct from a full-wave device simulation.

- [6.1 Why numerical simulation?](numerical-section-01.md)
- [6.2 Families of full-wave methods](numerical-section-02.md)
- [6.2.1 Finite elements: from strong form to edge unknowns](numerical-section-02-fem.md)
- [6.2.2 FDTD: the Yee lattice and leapfrog updates](numerical-section-02-fdtd.md)
- [6.2.3 Method of moments: solve for the currents](numerical-section-02-mom.md)
- [6.2.4 FIT: topology first, materials second](numerical-section-02-fit.md)
- [6.2.5 RCWA: periodic fields in Fourier space](numerical-section-02-rcwa.md)
- [6.3 Periodic cells, Floquet ports and phase planes](numerical-section-03.md)
- [6.4 Retrieve bulk and sheet parameters](numerical-section-04.md)
- [6.5 Practical meshing and convergence](numerical-section-05.md)
- [What you should learn](numerical-computational-01.md)
- [Choose the problem before the solver](numerical-computational-02.md)
- [Four different questions about error](numerical-computational-03.md)
- [Build a frequency-domain slab calculation](numerical-computational-04.md)
- [See conservation fail as an accuracy certificate](numerical-computational-05.md)
- [Move a monitor without moving the device](numerical-computational-06.md)
- [Estimate convergence and choose an acceptance target](numerical-computational-07.md)
- [Transfer the habit to patterned metasurfaces](numerical-computational-08.md)
- [A reproducible simulation record](numerical-computational-09.md)
- [Linked computational investigations](numerical-computational-10.md)

(chapter-06-computational-benchmark)=
## The computational benchmark

**Can a calculation conserve power to fifteen digits and still predict the wrong transmitted wave?** Yes. This chapter lets you produce that result, diagnose it, and improve it.

In [Chapter 2](02-waves-and-interfaces.md), a planar film had an exact scattering solution. We now solve the same physical problem by finite differences and compare the results. The benchmark separates errors in the numerical method from uncertainty about the physical structure. We then revisit the harmonic refinements of Chapters 3 and 5.

Use the [worked examples](06-numerical-guide.md), [interactive lab](../labs/06-numerical-lab.md), and [executed notebook](../notebooks/06-numerical-methods.ipynb). Prerequisites are Chapter 2, linear systems, and complex numbers; the RCWA comparison also uses Chapters 3–5. Study this methods strand before trusting a new response library.

```{figure} ../assets/chapter-06/slab-geometry.svg
:alt: A three-dimensional cut of the uniform film and a one-dimensional z grid, showing physical faces, incoming/reflected/transmitted waves and radiation boundaries.

The benchmark object is a uniform film, infinite along x and y: d = 0.60 µm, film index 2.4, exterior index 1.0. Numerical nodes are not extra layers. This reference sketch shows N = 8 and zero exterior padding; the explorer updates mesh and padding labels from its controls.
```
