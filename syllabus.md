# Provisional syllabus

The starting outline combines nine chapter headings from the instructor-supplied Persian contents excerpt with the instructor's requested Chapter 10, **AI and Metasurfaces**. The PDF contains three contents pages, not the full chapter text. The English translations and lab ideas below are provisional. The instructor's forthcoming topic list will determine the final scope and order.

## Audience and prerequisites

Graduate students in electrical engineering, electromagnetics, photonics, or related disciplines. Suggested preparation: Maxwell equations, phasors, plane waves, boundary conditions, linear algebra, and basic Python. A short refresher can accompany the first investigations.

## Proposed learning outcomes

By completing the course, students should be able to formulate a metasurface scattering problem, choose an appropriate sheet or full-wave model, design a response under physical constraints, and assess numerical and experimental evidence critically.

## Chapter map

| Chapter | Working title from the supplied contents | Proposed computational work |
| --- | --- | --- |
| 1 | [Introduction to metasurfaces and basic concepts](chapters/01-metasurface-foundations.md) | Executed analytical sheet model, phase/amplitude/power, electric-like/magnetic-like channels, conservation, and model limits |
| 2 | [Electromagnetic waves and interaction with metasurfaces](chapters/02-waves-and-interfaces.md) | Executed Fresnel/field/film/Jones/sheet models, four-view browser explorer, coherent absorption, and checked shunt retrieval |
| 3 | [Unit-cell design and simulation](chapters/03-unit-cell-design.md) | Executed TE ridge solver, analytical/RCWA validation, complex-response library, field plots, and constrained phase selection |
| 4 | [Periodic structures, Floquet analysis, and diffraction orders](chapters/04-periodic-floquet.md) | Executed channel maps, browser explorer, worked examples, and a periodic-port validation outline |
| 5 | [Metasurface synthesis](chapters/05-metasurface-synthesis.md) | Executed full-wave beam steering, expanded library, scalar line focusing, Jones/geometric phase, and further design outlines |
| 6 | Numerical modeling and simulation methods | Solver selection, mesh/domain convergence, benchmarks, power balance |
| 7 | Active, tunable, and intelligent metasurfaces | Bias/state-dependent response models and tuning constraints |
| 8 | Emerging applications in communications engineering | Beam control and system-level performance investigations |
| 9 | Materials, fabrication, and measurement methods | Tolerance analysis, measured-data processing, uncertainty |
| 10 | [AI and Metasurfaces](chapters/10-ai-metasurfaces.md) | Physically informed datasets, surrogate models, inverse design, uncertainty, and full-wave verification |

Chapter 6 may be introduced earlier as a methods strand, so students establish validation habits before building a unit-cell library. Chapters 7-9 have only chapter-level headings in the supplied excerpt; their detailed coverage remains open.

## Chapter 1: Metasurface foundations

The [chapter](chapters/01-metasurface-foundations.md), [six worked examples](chapters/01-foundations-guide.md), [lab](labs/01-first-investigation.md), and [executed notebook](notebooks/01-first-metasurface-model.ipynb) introduce structured interfaces, scales, complex coefficients, interference, electric/magnetic response, model hierarchy, and evidence. The browser explorer calculates a reciprocal lossless sheet response directly and works offline.

The ideal two-port model assumes equal exterior impedances, normal incidence, one polarization, and specular ports only. Analytical limits, full matrix unitarity, two-sided power, an independent electric-only expression, derivative refinements, and input guards are checked. It has no geometry or full-wave/experimental validation. Comparisons link to existing full-wave Chapters 3 and 5. Chapter 2 develops electromagnetic waves and boundary descriptions; Chapter 6 is next in the current development plan.

The [review and mini-project](chapters/01-foundations-review.md) adds eight self-check answers, a suggested grading rubric, a working glossary, and an editable report worksheet. The chapter includes an original geometry/port schematic; the worked guide illustrates delay and calculates flux normalization for one existing full-wave library row.

## Chapter 2: Waves, interfaces, and sheets

The [chapter](chapters/02-waves-and-interfaces.md), [nine worked examples](chapters/02-waves-guide.md), [review](chapters/02-waves-review.md), [lab](labs/02-waves-lab.md), and [executed notebook](notebooks/02-waves-and-interfaces.ipynb) establish Maxwell/phasor conventions, plane waves, power flux, polarization, Fresnel boundaries, evanescent fields, coherent films, scattering parameters, electric sheets, and equivalent circuits. Original schematics and five numerical figures support prediction-first explanations.

The offline browser explorer directly evaluates interface, film, polarization/analyzer, and electric-sheet models. Benchmarks include Brewster and critical angles, independent field flux and film boundary-equation checks, power-normalized reciprocity/unitarity/passivity, Jones identities, coherent two-beam absorption, and continuity/phase-plane guards for sheet retrieval. These are restricted exact planar models, not patterned-geometry or experimental validation. Chapter 6 will develop numerical methods after the foundational sequence.

## Chapter 3: Unit-cell design and simulation

The [chapter](chapters/03-unit-cell-design.md), [six worked examples](chapters/03-unit-cell-guide.md), [computational lab](labs/03-unit-cell-lab.md), and [executed notebook](notebooks/03-unit-cell-library.ipynb) build an original one-dimensional TE RCWA solver and a 50-width dielectric response library. The browser explorer selects precomputed responses and reports feasible/unmet phase targets. The downloadable source bundle preserves the solver, environment, notebook, data, and audit.

Validation includes interface/uniform-film limits, width-wise harmonic refinements, six higher-order spot checks, multiorder symmetry/field checks, and eight comparisons with the separate grcwa implementation. The reference covers a lossless, constant-index ridge grating at one wavelength/incidence and has incomplete phase coverage. FEM/FDTD, additional height sweeps, and varying-neighbor supercells are detailed lab outlines.

For the currently developed material, study Chapter 4's channel conventions before Chapter 3's amplitudes, then continue to [Chapter 5 synthesis](chapters/05-metasurface-synthesis.md). Chapter 6's numerical-validation methods accompany the computational work.

## Chapter 4: Periodicity and diffraction

The [chapter](chapters/04-periodic-floquet.md), [worked examples](chapters/04-floquet-guide.md), [interactive lab](labs/04-floquet-lab.md), and [executed notebook](notebooks/04-floquet-orders.ipynb) develop Bloch phases, diffraction orders, cutoff, evanescent decay, medium-dependent channel sets, and power normalization. Finite-array factors connect discrete Floquet directions to angular lobes. A rectangular-lattice example introduces the two-dimensional condition.

The browser explorer runs without a Python installation. The notebook includes analytical interface checks and optional Jupyter sliders. The full-wave lab progresses from a flat-interface benchmark to a dielectric grating, with an optional six-post beam deflector. Those solver stages are outlines awaiting implementation and convergence evidence.

## Chapter 5: Metasurface synthesis

The [chapter](chapters/05-metasurface-synthesis.md), [seven worked examples](chapters/05-synthesis-guide.md), [lab](labs/05-synthesis-lab.md), [beam-steering notebook](notebooks/05-beam-steering.ipynb), and [wavefront-model notebook](notebooks/05-wavefront-models.ipynb) connect target fields to geometry and verification. A new common-height 161-width library supports four complete six-ridge supercell calculations: limited, expanded, identical, and reversed. Harmonic refinements, primitive embedding, mirror tests, and a separate grcwa comparison accompany order-resolved powers. The explorer inspects these saved data.

Focusing is an executed scalar cylindrical-line model with independent FFT window/grid checks. Polarization is an analytical Jones model with geometric-phase/conversion checks. Neither is a full-wave finite metalens or vector response of the TE ridges. Further independent-method, finite-device, material-dispersive, holography, and robust-design investigations remain outlines.

## Chapter 10: AI and Metasurfaces

The [Chapter 10 pilot](chapters/10-ai-metasurfaces.md), [worked exercises](chapters/10-pilot-guide.md), and [computational lab](labs/13-ai-metasurfaces.md) are available for instructor review. They cover:

- **Problem formulation:** distinguish forward response prediction, inverse geometry design, and optimization using a learned surrogate. Define physical objectives and fabrication constraints before selecting a model.
- **Dataset construction:** version geometry, material dispersion, polarization, incidence conditions, solver settings, and convergence evidence. Define training, validation, and held-out test sets that avoid leakage between closely related geometries or sweeps.
- **Forward surrogates:** begin with a simple regression baseline, then compare a neural model on the same data and split. Consider complex response or phase-periodic representations rather than treating wrapped phase as an ordinary scalar.
- **Inverse design:** compare a conventional bounded optimizer with surrogate-assisted optimization. Introduce non-unique designs and possible generative approaches after establishing the baseline.
- **Physics and uncertainty:** test power accounting, reciprocity or symmetry where applicable, confidence away from training data, and sensitivity to fabrication variation.
- **Independent verification:** run selected predictions through a converged electromagnetic solver and report response error, design success, total data-generation/training/verification cost, and model limitations.

The proposed capstone is to build a surrogate from a validated unit-cell library, use it to propose a design, and test that design independently. The completed introductory pilot uses a synthetic resonant-sheet dataset: a kernel starter and an executed comparison of retrieval, interpolation, kernel regression, and a small neural network. Four lab stages specify the progression from analytical learning to full-wave data, constrained inverse design, and active learning. The full-wave dataset, solver, and assessment for later stages remain to be selected.

## Reusable module pattern

1. **Question and prediction:** state what the model should reveal.
2. **Theory bridge:** summarize the required concepts and link to the companion lesson.
3. **Notebook:** expose physical and numerical parameters with units.
4. **Validation:** compare analytic limits, convergence, and independent results where appropriate.
5. **Exercises and discussion:** vary assumptions, diagnose failures, and connect to research.

## Research project

Students will eventually pose a design question, justify the model, preserve inputs and outputs, and report both performance and uncertainty. Assessment weights, teaching schedule, software access, and project requirements remain to be set by the instructor.
