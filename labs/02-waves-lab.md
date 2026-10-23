---
title: 'Lab 2: Waves, Interfaces, and a Sheet That Listens to Phase'
short_title: Waves and interfaces lab
---

# Lab 2: Waves, Interfaces, and a Sheet That Listens to Phase

**Primary topic ID:** `ms-01-waves-interfaces`. Additional introductory activities support `ms-03-sheet-response` and `ms-06-polarization`; these activity identifiers need not equal chapter numbers.

**Question:** can you distinguish a field effect, a power transfer, and a change in coherent illumination before you trust a simulation or retrieval?

Read the [chapter](../chapters/02-waves-and-interfaces.md), use the [nine worked examples](../chapters/02-waves-guide.md), and retain a prediction log. The [self-check and project](../chapters/02-waves-review.md) provide answer guidance, deliverables, and a suggested rubric.

## A. Predict in the browser

**Status:** executable analytical browser exploration. It evaluates equations directly, without a full-wave solver, external dataset, or installation. The standalone HTML also works offline.

:::{iframe} ../interactives/waves-explorer.html
:width: 100%
:class: waves-explorer-frame
:title: Electromagnetic waves, interfaces, films, polarization, and sheets explorer

Original analytical experiments in wave amplitudes, flux, phase, and response assumptions.
:::

[Open the explorer in a full browser page](/interactives/waves-explorer.html), or download an offline copy: {download}`../interactives/waves-explorer.html`.

Use the corresponding experiment controls to investigate:

1. **Amplitude versus power:** compare air-to-glass and glass-to-air normal incidence. Predict $r,t,R,T$ and explain why $|t|>1$ is possible without gain.
2. **Angle and polarization:** locate the air-to-glass TM Brewster minimum. Compare TE at the same angle, then reverse the index contrast and cross the critical angle.
3. **Evanescence:** retain a total-internal-reflection case with nonzero transmitted field coefficient but zero net normal transmitted power. State the decaying branch and distinguish field decay from normal power transfer.
4. **Film interference:** compare an uncoated interface with the quarter-wave antireflection design. Change wavelength or thickness while retaining the other parameters.
5. **Polarization:** compare a linear state, a circular state, and an ellipse. Predict a linear analyzer's response. State the axes and time convention before describing rotation.
6. **Sheet response:** compare a passive resistive and a reactive electric sheet. Identify the assumptions behind the one-sided 50% absorption bound.

Keep a downloaded parameter/response record, one failed prediction and its explanation, and a short statement of what the browser does not calculate. At exact TM cutoff, use the stated limiting interpretation rather than treating an infinite intermediate admittance as an ordinary field value.

## B. Run the analytical notebook

**Status:** executed analytical reference available. The notebook covers the interface, film, polarization, electric-sheet retrieval, and coherent two-sided illumination. It does not run a patterned-geometry Maxwell solver.

Download the complete source: {download}`../downloads/chapter-02-waves.zip`. Extract the ZIP before running it, preserving the `notebooks/`, `simulations/`, `scripts/`, and `data/` folders. Follow the [shared environment instructions](../getting-started.md). The calculations use ordinary CPU-based numerical libraries; no commercial solver or GPU is required.

Individual files: {download}`../notebooks/02-waves-and-interfaces.ipynb`, {download}`../simulations/waves_interfaces.py`, {download}`../data/chapter-02/waves-reference.json`, {download}`../data/chapter-02/waves-reference.csv`, and {download}`../data/chapter-02/validation.json`.

| Setting | Reference experiment or convention |
| --- | --- |
| Time and space | $e^{-i\omega t}$, $e^{i\mathbf k\cdot\mathbf r}$ |
| Geometry | Interface near $z=0$; incidence from $z<0$; plane of incidence $xz$ |
| Field basis | Common tangential $E_y$ for TE, $E_x$ for TM |
| Bulk media | Positive real constant indices, $\mu=\mu_0$ |
| Interface benchmark | $n_i=1$, $n_t=1.5$; reverse for total internal reflection |
| Film benchmark | Normal incidence, $\lambda_d=0.6\,\mu\mathrm m$, $n_f=\sqrt{1.5}$, $d=\lambda_d/(4n_f)$ |
| Sheet | Normal incidence; local purely electric admittance $g=\eta_0Y_s$ |
| Retrieval reference | Equal air media, common sheet plane, $t=1+r$, nonzero transmission |
| Polarization | Coherent Jones components and an explicitly stated Cartesian/time convention |
| Power | Normal flux, with the appropriate admittance and total input denominator |

### Procedure

1. Write the electric and magnetic signs for forward and backward waves. Derive the bare-interface equations before executing cells.
2. Restart the kernel and run all cells. Inspect complex amplitudes beside their correctly normalized powers.
3. Reproduce normal incidence, Brewster cancellation, and a total-internal-reflection case. Check the root branch and treat grazing cutoff separately.
4. Calculate a quarter-wave film response and change its optical thickness. Retain the entrance/exit phase references.
5. Inspect the Jones trajectory and analyzer response. Compare global and relative phase changes.
6. Compare a reactive and resistive sheet. Check surface-current continuity and the power dissipated by its conductance.
7. Retrieve the known synthetic shunt only under its valid same-plane assumptions. Run the notebook's controlled retrieval-error experiment: change the fixed complex perturbation's magnitude/direction, compare exact and linearized parameter errors, and report perturbation magnitude relative to transmission. Its perturbed reflection preserves the model continuity deliberately; independently noisy coefficients need a separate residual check. Identify an incompatible response rather than forcing a fit.
8. For $g=2$ in air, compare one-sided illumination with normalized equal-power two-sided inputs. Calculate outgoing field sums before powers; sweep relative phase and explain the coherent-absorption result.
9. Save the executed notebook, generated figures, CSV/JSON, parameter records, and audit output. Preserve the model, source version, and assumptions when modifying an experiment.

### What must agree?

| Check | Interpretation |
| --- | --- |
| Air/glass normal incidence | $r=-0.2$, $t=0.8$, $R=0.04$, $T=0.96$ |
| Reverse interface | $r=0.2$, $t=1.2$ with the same $R,T$ |
| TM Brewster condition | Reflection zero at $\arctan(n_t/n_i)$ in the stated medium model |
| Total internal reflection | Decay into the second half-space; $R=1$, $T=0$ without assuming the whole field vanishes |
| Quarter-wave film | Reflected cancellation and $T=1$ at the ideal design condition |
| Polarization | Retarder norm preservation, analyzer projection, and stated rotation convention |
| Passive sheet | $R+T+A=1$ and nonnegative dissipated power |
| Sheet retrieval | Known synthetic parameter recovered only when the model and phase-plane checks hold |
| Coherent illumination | Total output calculated from $S\mathbf a$; phase-controlled absorption under normalized total input |

The saved audit states numerical thresholds and residuals for its test domain. Report these rather than declaring a calculation accurate because a plot looks smooth. Analytical identities and independent formulations check this model; they are not mesh convergence or validation of a patterned device.

## C. Connect fields to a geometry

**Status:** a reproducible comparison activity using already published full-wave data. No new ridge simulation or geometry-to-sheet retrieval is performed by this lab.

Choose one accepted response from the [Chapter 3 unit-cell library](../notebooks/03-unit-cell-library.ipynb). Record geometry, media, wavelength, polarization, reference planes, complex coefficients, and power fractions. Recalculate its incident-normalized transmitted power with its correct exterior flux factor. Compare that with $|t|^2$ and with the equal-air ideal sheet.

Now ask whether $t=1+r$ at a common sheet plane is even the appropriate model test for that finite-height, substrate-supported structure. Identify the information needed before fitting any sheet parameters. A finite layer's entrance and exit coefficients cannot be inserted blindly into a zero-thickness shunt inverse.

**Deliverable:** a one-page evidence comparison connecting a uniform-interface benchmark, a local sheet, and a patterned full-wave cell. Identify a claim that each model can support and an additional test that it cannot replace.

## D. An optional physical investigation

**Status:** a proposed later-course extension, not an executed measurement or an additional requirement for completing the introductory lab.

Choose a microwave or optical apparatus suited to one experiment: interface reflection, a thin-film spectrum, polarization analysis, or coherent two-sided absorption. Specify the material/bias model, excitation and spatial mode, phase planes, detector collection, calibration, uncertainty, and safe operating procedure under the laboratory's own rules. Distinguish a normal-power measurement from a local-field probe. A coherent absorption test also needs controlled relative phase and a measured total input denominator.

Predict the measurable observable before collecting data. Retain a separate condition for checking a fitted model; state finite-aperture, material-dispersion, and alignment limitations. Fabrication, experimental uncertainty, and more general retrieval belong to their detailed later investigations.

## Share a result that can be checked

Use the [wave detective project and rubric](../chapters/02-waves-review.md), and submit editable sources through the [contribution workflow](../contributing.md). Include references, environment, source/data versions, figures, conventions, residuals, and execution status. Keep the distinction between an executed analytical result, reused full-wave data, and a proposed experiment visible in the report.
