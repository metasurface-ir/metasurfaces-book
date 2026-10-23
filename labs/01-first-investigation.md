---
title: 'Lab 1: Your First Metasurface Investigation'
short_title: First computational investigation
---

# Lab 1: Your First Metasurface Investigation

**Topic ID:** `ms-02-scattering` — parameterized response and model limitations. Topic identifiers describe activities and need not equal chapter numbers.

**Companions:** [Chapter 1](../chapters/01-metasurface-foundations.md), [six worked examples](../chapters/01-foundations-guide.md), and the [executed notebook](../notebooks/01-first-metasurface-model.ipynb).

**Question:** can we change transmission phase without reflecting power, and what assumptions make that possible?

Before reading the results, use the [model and geometry guide](../models.md). Identify the object, dimensions, incident wave, invariant/repeated directions, and reference planes in the drawing.

## A. Predict and explore

Before clicking a preset, predict $R$, $T$, and whether transmission phase is meaningful. Compare no response, electric-like only, balanced, and detuned channels. Move the illumination frequency away from resonance and vary the two strengths.

:::{iframe} ../interactives/foundations-explorer.html
:width: 100%
:class: foundations-explorer-frame
:title: First metasurface analytical explorer

An ideal lossless specular sheet model, evaluated directly in the browser. It has no assigned fabrication geometry and does not run a full-wave solver.
:::

[Open the explorer in a full browser page](/interactives/foundations-explorer.html), or download an offline copy: {download}`../interactives/foundations-explorer.html`.

The reference has equal exterior impedances, normal incidence, one polarization, only specular reflection/transmission, and both coefficient reference planes at the ideal sheet. Channel strengths are dimensionless effective parameters. At zero transmitted amplitude the explorer reports phase as undefined.

**Deliverable:** predictions and observations for all four presets, one custom case with unequal strengths, and a downloaded parameter/response record. Explain why perfect balanced matching over the entire sweep is an imposed assumption rather than a verified broadband physical device.

## B. Run and audit the notebook

**Status:** executed analytical reference available. Download the complete source: {download}`../downloads/chapter-01-foundations.zip`. Extract the ZIP before opening the notebook, preserving `simulations/`, `data/`, and `notebooks/`. See the [shared environment instructions](../getting-started.md).

Individual files: {download}`../notebooks/01-first-metasurface-model.ipynb`, {download}`../simulations/intro_sheet.py`, {download}`../data/chapter-01/sheet-response.json`, {download}`../data/chapter-01/sheet-response.csv`, and {download}`../data/chapter-01/validation.json`.

### Inputs

| Parameter | Reference |
| --- | --- |
| Illumination | $200\,\mathrm{THz}$; spectral sweep 120–280 THz |
| Electric-like resonance | 200 THz |
| Magnetic-like resonance | 200 THz balanced, 230 THz detuned |
| Enabled channel strengths | 0.25, dimensionless |
| Disabled channel | Strength zero, defined as $C=1$ |
| Phase validity floor | $|t|>10^{-12}$ |
| Exterior / polarization | Equal real impedances; one polarization; normal incidence |
| Model | Reciprocal, mirror-symmetric, lossless, two specular ports |

NumPy and Matplotlib run the model on a CPU; no commercial solver, GPU, or network dataset is required. The shared `requirements-labs.txt` also supports later chapters.

Edit `CUSTOM` for the notebook's single-frequency response. The separate `PRESETS` define the four spectral comparisons; change those deliberately if you want different comparison curves.

### Procedure

1. Draw the illumination and two ports. State the time convention and reference plane.
2. Derive the transparent, electric-only, and balanced resonance limits before executing cells.
3. Restart the Python kernel and run all cells. Inspect complex coefficients, powers, and undefined phases.
4. Sweep frequency and compare the four presets, keeping phase beside amplitude/power.
5. Inspect the model's channel-vector sums. State why these are not extracted dipole moments.
6. Compare two spectral phase widths and their group delays. Check units and the numerical derivative.
7. Inspect $R+T$ and the stronger $S^\dagger S=I$ test. Explain what each check establishes.
8. Save notebook outputs and the generated CSV/JSON. Preserve the model/source version and assumptions when editing parameters.

Run the separate analytical audit from the repository or extracted bundle root:

```sh
python scripts/validate_chapter01.py
```

### Acceptance

| Check | Criterion |
| --- | --- |
| Transparent, electric-only, balanced limits | Agreement with the stated complex limits within $10^{-12}$ |
| One- and two-sided power / unitarity | Worst residual below $10^{-12}$ across the audit's 36 parameter cases and 521 frequencies |
| Independent electric-only expression | Complex-amplitude error below $10^{-12}$ |
| Group-delay derivative | Refinement reduces error; final resonance error below 0.002 fs for the specified tests |
| Zero-transmission phase | Undefined; JSON null and CSV blank |
| Input/provenance | Invalid domains rejected and saved source hash checked |

These are analytical-model consistency tests. They are not mesh/harmonic convergence, a full-wave comparison, or experimental validation.

**Deliverables:** executed notebook, prediction table, three figures, custom parameters, response files, audit, and a statement of model limits.

For a complete introductory assignment, use the [self-check answers and mini-project](../chapters/01-foundations-review.md), its suggested assessment rubric, and the editable report worksheet: {download}`../downloads/chapter-01-report-template.md`. The worksheet is also included in the source ZIP. The comparison in the worked guide uses saved Chapter 3 data; it does not add a full-wave solver run to this notebook.

## C. Connect to a physical computation

**Status:** reading/comparison activity using the already executed [Chapter 3 unit-cell lab](03-unit-cell-lab.md) and [Chapter 5 synthesis lab](05-synthesis-lab.md). No new geometry is inferred from the introductory sheet parameters.

Choose one published full-wave ridge response. Record its width, height, pitch, materials, wavelength, polarization, exterior media, phase planes, outgoing channels, and convergence evidence. Compare those requirements with the present ideal sheet. Explain why adjusting an abstract channel strength is not equivalent to selecting a ridge width without a mapping or retrieval study.

Next inspect the identical and varying supercells in Chapter 5. An allowed channel can have zero amplitude; a local cell prediction can disagree with the collective full-wave result. State which assumptions the two-port introductory model cannot represent.

**Deliverable:** a one-page comparison of analytical sheet, repeated unit cell, and supercell evidence, with one testable next question.

## D. Measurement or retrieval outline

**Status:** outline; no measurement or geometry-to-sheet retrieval is performed in this chapter.

Select a specific structure and illumination. Define calibration, reference planes, incident power, collected/reflected/transmitted angular and polarization channels, sample aperture, and uncertainty. Use appropriate complex-field or scattering-parameter measurements if phase is claimed. Fit an explicitly stated reduced model only after checking those conditions and retaining a separate validation dataset or illumination condition.

**Deliverables:** a model/measurement specification, normalization and uncertainty plan, parameter-identifiability discussion, and an independent check. Missing collected power cannot be labeled absorption until the relevant outgoing channels and collection limits are addressed.

## Share your contribution

Use the [contribution workflow](../contributing.md). Submit editable sources, references, environment, figures/data, and an execution-status note. After a saved notebook execution and audit, `python scripts/export_chapter01.py` regenerates the chapter figures, browser explorer, and source bundle. The publishing build displays saved results rather than running experiments.
