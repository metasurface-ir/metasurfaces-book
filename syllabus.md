# Provisional syllabus

The starting outline combines nine chapter headings from the instructor-supplied Persian contents excerpt with the instructor's requested Chapter 10, **AI and Metasurfaces**. The PDF contains three contents pages, not the full chapter text. The English translations and lab ideas below are provisional. The instructor's forthcoming topic list will determine the final scope and order.

## Audience and prerequisites

Graduate students in electrical engineering, electromagnetics, photonics, or related disciplines. Suggested preparation: Maxwell equations, phasors, plane waves, boundary conditions, linear algebra, and basic Python. A short refresher can accompany the first investigations.

## Proposed learning outcomes

By completing the course, students should be able to formulate a metasurface scattering problem, choose an appropriate sheet or full-wave model, design a response under physical constraints, and assess numerical and experimental evidence critically.

## Chapter map

| Chapter | Working title from the supplied contents | Proposed computational work |
| --- | --- | --- |
| 1 | Introduction to metasurfaces and basic concepts | Explore electric/magnetic responses and model assumptions |
| 2 | Electromagnetic waves and interaction with metasurfaces | Fresnel amplitudes and power, polarization, sheet response, S parameters, equivalent circuits |
| 3 | Unit-cell design and simulation | Parameter sweeps, response retrieval, phase libraries, array assembly |
| 4 | Periodic structures, Floquet analysis, and diffraction orders | Open-channel maps, diffraction angles, cutoff, periodic-port validation |
| 5 | Metasurface synthesis | Beam steering, focusing, amplitude and polarization control, geometric phase, inverse design |
| 6 | Numerical modeling and simulation methods | Solver selection, mesh/domain convergence, benchmarks, power balance |
| 7 | Active, tunable, and intelligent metasurfaces | Bias/state-dependent response models and tuning constraints |
| 8 | Emerging applications in communications engineering | Beam control and system-level performance investigations |
| 9 | Materials, fabrication, and measurement methods | Tolerance analysis, measured-data processing, uncertainty |
| 10 | AI and Metasurfaces | Physically informed datasets, surrogate models, inverse design, uncertainty, and full-wave verification |

Chapter 6 may be introduced earlier as a methods strand, so students establish validation habits before building a unit-cell library. Chapters 7-9 have only chapter-level headings in the supplied excerpt; their detailed coverage remains open.

## Chapter 10: AI and Metasurfaces

The following scope is proposed for the instructor's review:

- **Problem formulation:** distinguish forward response prediction, inverse geometry design, and optimization using a learned surrogate. Define physical objectives and fabrication constraints before selecting a model.
- **Dataset construction:** version geometry, material dispersion, polarization, incidence conditions, solver settings, and convergence evidence. Define training, validation, and held-out test sets that avoid leakage between closely related geometries or sweeps.
- **Forward surrogates:** begin with a simple regression baseline, then compare a neural model on the same data and split. Consider complex response or phase-periodic representations rather than treating wrapped phase as an ordinary scalar.
- **Inverse design:** compare a conventional bounded optimizer with surrogate-assisted optimization. Introduce non-unique designs and possible generative approaches after establishing the baseline.
- **Physics and uncertainty:** test power accounting, reciprocity or symmetry where applicable, confidence away from training data, and sensitivity to fabrication variation.
- **Independent verification:** run selected predictions through a converged electromagnetic solver and report response error, design success, total data-generation/training/verification cost, and model limitations.

The proposed capstone is to build a surrogate from a validated unit-cell library, use it to propose a design, and test that design independently. Begin with a small, reproducible dataset and modest hardware requirements. Final model families, dataset, software, and assessment remain undecided. No AI model or dataset is supplied in this scaffold.

## Reusable module pattern

1. **Question and prediction:** state what the model should reveal.
2. **Theory bridge:** summarize the required concepts and link to the companion lesson.
3. **Notebook:** expose physical and numerical parameters with units.
4. **Validation:** compare analytic limits, convergence, and independent results where appropriate.
5. **Exercises and discussion:** vary assumptions, diagnose failures, and connect to research.

## Research project

Students will eventually pose a design question, justify the model, preserve inputs and outputs, and report both performance and uncertainty. Assessment weights, teaching schedule, software access, and project requirements remain to be set by the instructor.
