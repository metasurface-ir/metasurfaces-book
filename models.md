---
title: What Am I Simulating?
short_title: Model and geometry guide
---

# What Am I Simulating?

Start each investigation by identifying the object, its environment, the incident wave, and the response being measured. These original drawings depict the models used in this book. The ridge and film cuts show a finite visible portion of structures that extend indefinitely; a drawn edge does not create a simulated finite device.

## A map from structure to result

| Chapter | Object or model | What the result describes |
| --- | --- | --- |
| [1](chapters/01-metasurface-foundations.md) | Ideal sheet with two equivalent response channels | Analytical specular reflection and transmission; no particle shape assigned |
| [2](chapters/02-waves-and-interfaces.md) | Planar interface, uniform film, electric sheet, or specified Jones element | Boundary scattering, interference, or polarization in that restricted model |
| [3](chapters/03-unit-cell-design.md) | Identical dielectric ridges repeated along x, invariant along y | Complex scattering of a periodic ridge environment as its width changes |
| [4](chapters/04-periodic-floquet.md) | A periodic interface with stated period and illumination | Allowed diffraction channels; motif shape and scattering powers are not solved |
| [5](chapters/05-metasurface-synthesis.md) | Six different ridges forming one repeated supercell | Collective reflected/transmitted order powers; separate scalar/Jones exercises use their own models |
| [6](chapters/06-numerical-methods.md) | A uniform dielectric slab, infinite along x and y | Numerical approximation to a known film-scattering problem |
| [7](chapters/07-active-tunable.md) | Assigned bias-dependent impedance and prescribed scalar sources | Reachable reflection, coding, synthetic calibration and slow modulation; no solved patch geometry |
| [8](chapters/08-communications.md) | Square reflective aperture and two free-space propagation legs | Scalar channel, ideal phases, assigned efficiency and noise; no solved patch or measured wireless link |
| [10](chapters/10-ai-metasurfaces.md) | Synthetic analytical resonant sheet | Learning and inverse-search performance on analytical data; no fabricated unit cell |

## Chapter 3: one ridge width, repeated everywhere

```{figure} assets/chapter-03/unit-cell-geometry.svg
:alt: Three-dimensional cut of repeated dielectric ridges and an x-z section of one periodic cell, showing width, height, period, illumination, materials, and reflection/transmission planes.

The dashed boundaries enclose one unit cell. The neighboring ridges have the same width; changing the slider changes that width in every cell. The visible ridge ends are illustrative cuts along the invariant y direction. The numerical field varies in x and z, with electric field along y.
```

Read the phase and power as the response of this entire repeated environment. The material indices are ideal model inputs, not a claim about a measured material. The [unit-cell explorer](labs/03-unit-cell-lab.md) updates the drawing from the selected saved width.

## Chapter 5: six widths act together

```{figure} assets/chapter-05/supercell-geometry.svg
:alt: Three-dimensional and cross-sectional geometry of the saved expanded six-ridge beam-steering design, showing the order of ridge widths and the full repeat length.

This is the saved expanded beam-steering design. Its full six-ridge sequence repeats with L = 6Λ = 3.90 µm. A purple boundary marks the whole supercell. The solver calculates the collective scattering of this geometry, including coupling and every open diffraction order.
```

Changing a case in the [synthesis explorer](labs/05-synthesis-lab.md) changes the widths and common height in the drawing together with the saved results. Reversing the sequence mirrors the design and exchanges positive/negative order powers. These ridges are not a finite metalens: the later focus plots propagate prescribed scalar aperture fields and do not simulate a fabricated focusing structure.

## Chapter 6: a film benchmark, with numerical nodes

```{figure} assets/chapter-06/slab-geometry.svg
:alt: Three-dimensional cut through a uniform dielectric film and its one-dimensional grid, with film faces, incident/reflected/transmitted waves, and discrete radiation boundaries.

The slab is physically uniform along x and y. Only z is discretized. Dots denote numerical field nodes, not extra material layers. In the reference drawing N = 8 and the computational boundaries lie on the two film faces; exterior padding moves those boundaries. Reflection is referenced to z = 0, transmission to z = d.
```

The [numerical explorer](labs/06-numerical-lab.md) changes the displayed mesh count and padding annotation with its controls. Refining N changes the numerical approximation while preserving the physical film. Its fields and errors benchmark a solver method; they are not the results of a patterned metasurface simulation.

## Chapter 7: a control mechanism and its effective model

```{figure} assets/chapter-07/tunable-cell.svg
:alt: Conceptual split patch, grounded section and assigned RLC boundary. Geometry is explanatory; the effective parameters are not extracted from it.

Conceptual split patch, grounded section and assigned RLC boundary. Geometry is explanatory; the effective parameters are not extracted from it.
```

The [Chapter 7 explorer](labs/07-tunable-lab.md) links bias to a complex-response trajectory and displays the 32 selected aperture states. Its cell drawing is a possible physical concept. The numerical object is the assigned circuit; array intensity omits coupling and element patterns. This original schematic is generated by `scripts/export_tunable_geometry.py`.

## Chapters 1 and 10: draw the equivalent model honestly

```{figure} assets/chapter-10/analytical-sheet.svg
:alt: An ideal zero-thickness sheet illuminated from one side, with reflected and transmitted wave arrows and a shared phase reference on the sheet.

The ideal sheet is a two-port boundary description. No pillar, ring, split-ring, or physical thickness has been assigned. Chapter 1 varies equivalent response channels; Chapter 10's abstract design coordinate tunes its analytical generator rather than a specified nanostructure.
```

A learned response does not establish a physical geometry. Connecting it to a ridge or another manufactured shape requires a geometry-dependent electromagnetic dataset and fresh verification.

## Before interpreting any plot

1. Point to the object and name every direction in which it repeats or remains invariant.
2. Read the geometric parameters, material indices, wavelength, illumination, and polarization.
3. Identify the physical reference planes and distinguish numerical nodes/boundaries from material interfaces.
4. Name the plotted quantity: field, complex amplitude, incident-normalized order power, scalar intensity, or model-prediction error.
5. Keep the geometry and model label with exported results. These drawings use the book's saved parameter files and the original shared renderer `templates/model-geometry.js`; they are generated without external artwork.

The same six-ridge geometry now anchors [ms-09 spectral sweeps](labs/09-dispersion-lab.md), [ms-10 local/supercell comparisons](labs/10-coupling-lab.md), and [ms-11 bounded width optimization](labs/11-inverse-design-lab.md). Their browser drawings follow the saved wavelength, width contrast or selected candidate.

## Chapter 8: aperture geometry and the communication link

The [Chapter 8 geometry](chapters/08-communications.md) shows a transmitter, reflective square aperture, receiver and optional direct path. A loaded-patch inset is a possible implementation only. Integration samples carry area weights; they are not separately normalized antennas. The [explorer](labs/08-communications-lab.md) moves the receiver while retaining the programmed target, and displays the corresponding aperture phase and gain. The shared model is simulations/communication_link.py.
