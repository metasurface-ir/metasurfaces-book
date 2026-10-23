---
title: 'Lab 3: Build and Validate a Unit-cell Response Library'
short_title: Unit-cell computational lab
---

# Lab 3: Build and Validate a Unit-cell Response Library

**Topic ID:** `ms-07-unit-cell`

**Companions:** [Chapter 3](../chapters/03-unit-cell-design.md), [six worked examples](../chapters/03-unit-cell-guide.md), and [executed notebook](../notebooks/03-unit-cell-library.ipynb).

**Question:** can a width sweep meet a desired transmission phase and power, and what evidence makes the resulting library reusable?

Before reading the results, use the [model and geometry guide](../models.md). Identify the object, dimensions, incident wave, invariant/repeated directions, and reference planes in the drawing.

## A. Predict and inspect in your browser

The explorer contains 50 saved full-wave TE ridge responses. Move the width slider and observe the geometry, complex transmission trajectory, phase, power, and convergence record. Enter a target phase and minimum transmitted power. Distinguish a nearest eligible candidate from one meeting the $5^\circ$ phase-error criterion.

:::{iframe} ../interactives/unit-cell-explorer.html
:width: 100%
:class: unit-cell-explorer-frame
:title: Interactive unit-cell response library

An explorer of a validated, precomputed dielectric TE ridge library. Browser controls select saved data without running a Maxwell solver.
:::

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/unit-cell-explorer.html" target="_blank" rel="noopener">Open the browser lab in a new tab</a>

Before revealing the answer, predict whether this geometry can achieve every phase at $T\geq0.8$. Test targets $-160^\circ$, $-100^\circ$, $-50^\circ$, and $0^\circ$. Then raise the minimum power to 1 and explain the empty eligible set.

**Deliverable:** two satisfactory targets and one unmet request, with width, complex amplitude, power, circular phase error, and the relevant model limits. Record the selected row and its source metadata for attribution and reuse.

## B. Run the full-wave reference notebook

Download the complete runnable source: {download}`../downloads/chapter-03-unit-cell.zip`. Extract the ZIP before opening the notebook. It includes `simulations/unit_cell_te.py`, the notebook, requirements, reference data, and the audit script. The notebook requires its companion solver module; cloning the repository preserves the same folder structure.

Individual files: {download}`../notebooks/03-unit-cell-library.ipynb`, {download}`../simulations/unit_cell_te.py`, {download}`../data/chapter-03/response-library.csv`, {download}`../data/chapter-03/response-library.json`, and {download}`../data/chapter-03/validation.json`.

### Inputs and assumptions

Use the [computational environment](../getting-started.md) and `requirements-labs.txt`. NumPy, SciPy, and Matplotlib run the TE solver on a CPU; optional Jupyter controls use ipywidgets. No commercial solver, network dataset, or GPU is required.

The reference is a rectangular ridge invariant along $y$, with period $0.65\,\mu\mathrm m$, height $0.60\,\mu\mathrm m$, width samples $0.08$–$0.57\,\mu\mathrm m$, and wavelength $1.55\,\mu\mathrm m$. Ridge/gap indices are 2.4/1, exterior indices 1/1.5, and incidence is normal TE. These are ideal, lossless, constant-index materials. Reflection is referenced to the top face and transmission to the bottom face.

### Procedure

1. Sketch the experiment and enumerate its exterior open orders using Chapter 4. Predict the effect of changing width.
2. Restart the notebook kernel and run all cells. Record the environment and the source hash embedded in the library metadata.
3. Inspect the zero-height interface and zero/full-width film checks. Compare complex amplitudes against the independent scalar film formula.
4. Compare harmonic truncations and explain why power balance alone cannot establish convergence.
5. Inspect the reconstructed real field and squared amplitude. Explain the role of closed harmonics near the ridge.
6. Generate all 50 widths at $M=24$ and compare every row with $M=32$. Check power, complex-amplitude, and phase changes.
7. Inspect the spectral-neighborhood illustration. Identify which results are inside the exported library's validated domain.
8. Select geometries for constrained phase targets. Report an unmet target rather than labeling the nearest row as successful.
9. Inspect the synthesized monitor-offset test and its de-embedded phase. State that this is an algebraic reference-plane check.
10. Export the CSV/JSON and preserve the notebook. Optional Jupyter sliders inspect saved rows when `ENABLE_WIDGETS=True`; use `False` for the static reference publication.

### Acceptance and evidence

| Check | Reference criterion |
| --- | --- |
| Interface and film coefficients | Complex-amplitude errors below $10^{-10}$ for the specified 18 cases |
| Row-wise harmonic refinement | $|\Delta t|<5\times10^{-4}$ and changes in $R,T$ below $5\times10^{-4}$ |
| Meaningful transmission phase | Circular refinement change below $0.05^\circ$ |
| Lossless all-channel balance | $|1-R-T|<10^{-8}$ |
| Higher-order spot audit | Six library widths checked at $M=48$ against the complex-amplitude threshold |
| Separate implementation | Eight grcwa cases, with 256/2048 raster refinement; fine-grid order-power and complex-$t_0$ differences below $10^{-4}$ |

Run the additional audit from the repository root:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_chapter03.py --grcwa
```

The optional dependency is grcwa 0.1.2; it is used for validation, while the notebook uses the original course solver. Running the script without `--grcwa` still executes the other numerical checks and records that the optional comparison was not run. Do not present that new record as a completed external comparison.

The separate implementation uses the same RCWA method family. Its raster representation is checked separately, while the course solver uses exact rectangle coefficients. An FDTD/FEM comparison would supply another form of numerical evidence.

**Deliverables:** executed notebook; source/version; model sketch; analytical and convergence tables; field, library, and spectral figures; CSV/JSON; validation audit; phase-selection report; and a clear statement of the library domain. Changing parameters defines a new experiment and requires renewed validation.

## C. Extend the library: student computational outline

**Purpose:** investigate whether adding height as a degree of freedom improves phase coverage without sacrificing transmission.

**Inputs:** the reference code, a documented width/height grid, fixed wavelength/angle/material model, a minimum feature/gap rule, and proposed convergence thresholds. Begin with three heights and a coarse width grid; refine only where the response changes rapidly.

**Procedure:** establish common physical phase planes when comparing heights, apply the analytical limits, sweep widths/heights, repeat numerical refinements, classify all exterior orders, and export separate experiment metadata. Use circular phase errors and meaningful amplitude thresholds. Test interpolation with fresh solves at geometries absent from the original grid.

**Deliverables:** coverage and transmission maps, accepted/rejected entries, independent interpolation checks, and a versioned dataset. Explain any coverage gaps. A full phase circle is an outcome to assess rather than an assumed success condition.

**Status:** the [Chapter 5 lab](05-synthesis-lab.md) now executes a common-height screen and a new fixed-height, 161-width library. The broader two-parameter library investigation described here remains an extension outline.

## D. Compare numerical methods: FEM or FDTD outline

**Purpose:** compare the same complex TE response using another numerical method.

Begin with a flat interface, then a uniform film, then three ridges matching the reference parameters. Use Bloch/periodic lateral boundaries and outward ports or absorbing boundaries vertically. Define TE by its actual field direction. Match material constants and all amplitude reference faces.

For FDTD, refine spatial grid, simulation decay/run time, PML, and source/monitor offsets. For FEM, refine mesh/order and port/domain placement. Enumerate open orders and compare their power-normalized coefficients. Remove homogeneous propagation before comparing complex phase. Set tolerances before reviewing the results and report numerical cost and unresolved differences.

**Deliverables:** solver/version and model file, convergence records, a coefficient/reference-plane mapping, and a table of complex and power differences. The [Meep mode-decomposition tutorials](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/) provide relevant grating, phase, and normalization examples.

**Status:** outline; the published reference has been compared with another RCWA implementation, while this FEM/FDTD stage has not been executed.

## E. Test local periodicity: supercell outline

**Purpose:** determine when differing neighbors invalidate the independent periodic-cell approximation.

Choose several accepted geometries and arrange them in an explicitly repeated supercell. Compare a sequence with slowly changing widths against one with abrupt neighboring changes. Predict scattering with a clearly stated local model, then simulate the complete supercell with appropriate channel accounting. Compare complex order amplitudes and target-order power after harmonizing reference planes and normalization.

**Deliverables:** geometry sequence, local prediction, full-supercell results, converged order-resolved powers, and an explanation of disagreement. Do not interpret the local mask's Fourier amplitudes directly as full-wave powers without its normalization/model assumptions.

**Status:** [Chapter 5](05-synthesis-lab.md) now includes a full-wave comparison for selected six-ridge periodic sequences, including identical and reversed controls. The broader neighbor-gradient study described here and a finite-aperture beam deflector remain extension outlines.

## Contribution handoff

Keep the stable topic ID `ms-07-unit-cell`. Submit sources, environment, data, figures, references, validation, and an explicit execution-status note through the [contribution workflow](../contributing.md). Accepted work inherits the shared book layout and navigation. Heavy calculations remain separate from routine Pages deployment.
