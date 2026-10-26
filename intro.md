# Metasurface.ir

**Metasurfaces: From Wave Physics to Design** — a graduate companion book for investigating how electromagnetic sheets transform waves.

This book connects mathematical models, editable Jupyter notebooks, and reproducible investigations. Chapter 1 introduces physical intuition, complex responses, model assumptions, and a first analytical sheet investigation. Chapter 2 builds the electromagnetic prerequisite through waves, boundaries, polarization, films, and sheets. Chapter 3 computes a validated dielectric unit-cell library. Chapter 4 develops periodicity and diffraction. Chapter 5 connects target wavefronts to full-wave beam steering, scalar focusing, and polarization models. Chapter 6 develops solver selection and numerical validation through an independently benchmarked FDFD slab. Chapter 7 develops bias tuning, programmable arrays, synthetic feedback and temporal modulation. Chapter 8 connects finite apertures to communication channels, bandwidth and training costs. Chapter 9 connects materials and fabrication tolerances to calibrated measurements and uncertainty. Chapter 10 connects electromagnetic models to AI-assisted design. All ten chapter drafts are available for instructor review; student contributions can extend their computational and experimental evidence.

## Learn by investigating

Each investigation will start with a physical question, ask for a prediction, develop a computational model, and compare the result with a limiting case or independent calculation. Parameters, units, assumptions, and the limits of the model will be explicit.

The companion course website will provide conceptual lessons and course guidance. This book will hold computational derivations, notebooks, solver instructions, and numerical evidence. Links between the two will be added after their public URLs are verified.

## Start here

**English | فارسی:** the [Persian edition](https://metasurface-ir.github.io/metasurfaces-book/fa/) covers every developed chapter (1, 2, 3, 4, 5, 6, 7, 8, 9, and 10), its guides and labs, all published notebook narratives, and the syllabus. See [translation status and contribution instructions](translations.md) for coverage and review status.

- Identify the object behind each result in [What am I simulating?](models.md), with 3D cuts and labeled sections.
- Read the [ten-chapter syllabus](syllabus.md).
- Start with [Chapter 1: Introduction to Metasurfaces and Basic Concepts](chapters/01-metasurface-foundations.md), its [six worked examples](chapters/01-foundations-guide.md), and the [first computational investigation](labs/01-first-investigation.md).
- Explore [Chapter 2: Waves, Interfaces, and Sheets](chapters/02-waves-and-interfaces.md), its [worked examples](chapters/02-waves-guide.md), [self-check](chapters/02-waves-review.md), and [interactive/executable lab](labs/02-waves-lab.md).
- Build a response library with [Chapter 3: Unit-cell Design and Simulation](chapters/03-unit-cell-design.md), its [worked examples](chapters/03-unit-cell-guide.md), and the [full-wave lab and browser explorer](labs/03-unit-cell-lab.md).
- Begin [Chapter 4: Periodic Structures and Floquet Analysis](chapters/04-periodic-floquet.md), follow its [worked examples](chapters/04-floquet-guide.md), and use the [interactive lab](labs/04-floquet-lab.md).
- Design and verify with [Chapter 5: Metasurface Synthesis](chapters/05-metasurface-synthesis.md), its [worked examples](chapters/05-synthesis-guide.md), and [computational lab](labs/05-synthesis-lab.md).
- Test numerical accuracy with [Chapter 6](chapters/06-numerical-methods.md), its [worked guide](chapters/06-numerical-guide.md), and [interactive lab](labs/06-numerical-lab.md).
- Tune and calibrate with [Chapter 7](chapters/07-active-tunable.md), its [six worked examples](chapters/07-tunable-guide.md), and [four-part browser lab](labs/07-tunable-lab.md).
- Investigate [Chapter 8: Communications Engineering](chapters/08-communications.md), its [six worked examples](chapters/08-communications-guide.md), and [four-part browser lab](labs/08-communications-lab.md).
- Follow [Chapter 9: Materials, Fabrication, and Measurement](chapters/09-materials-measurement.md), its [six worked examples](chapters/09-measurement-guide.md), and [four-part browser lab](labs/09-measurement-lab.md).
- Begin [Chapter 10: AI and Metasurfaces](chapters/10-ai-metasurfaces.md).
- Follow the [pilot learning path and worked exercises](chapters/10-pilot-guide.md).
- Work through the [AI computational lab](labs/13-ai-metasurfaces.md), [starter notebook](notebooks/10-resonant-surrogate.ipynb), and [neural comparison](notebooks/10-neural-comparison.ipynb).
- Review the [computational environment](getting-started.md).
- Explore the [planned investigations](labs/index.md).
- Check [figure provenance and reuse guidance](attribution.md).
- Learn [how to contribute a chapter or notebook](contributing.md).

:::{note} Development status
Chapters 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 are available for instructor review. Chapter 1 is the entry point, with an executed analytical notebook and browser explorer. Chapters 3 and 5 include executed full-wave TE ridge calculations and validated libraries; Chapter 5 also verifies four complete periodic supercells. Chapters 3-5 have browser explorers. Focusing and polarization use separately labeled scalar/Jones models, and the Chapter 10 pilot uses analytical data. Further FEM/FDTD, finite-device, broadband, and fabrication investigations remain outlines. Chapter 6 adds executed FDFD convergence, fields, boundary, and reference-plane diagnostics. Chapter 7 adds an executed equivalent-circuit and control investigation. Chapter 8 adds an executed scalar aperture-to-link investigation. Chapter 9 adds synthetic material, tolerance, calibration and uncertainty investigations. Experimental and advanced solver extensions remain explicitly unexecuted outlines. The website displays saved notebook results; download source bundles/notebooks to run or modify their Python calculations.
:::
