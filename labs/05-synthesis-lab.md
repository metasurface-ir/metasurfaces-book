---
title: 'Lab 5: Synthesize, Simulate, and Assess a Metasurface'
short_title: Synthesis computational lab
---

# Lab 5: Synthesize, Simulate, and Assess a Metasurface

**Topic IDs:** `ms-05-beam-steering` (full-wave supercell), `ms-08-metalenses` (scalar line focus), and `ms-06-polarization` (analytical Jones model).

**Companions:** [Chapter 5](../chapters/05-metasurface-synthesis.md) and [seven worked examples](../chapters/05-synthesis-guide.md).

**Question:** how much of a target wavefront survives sampling, response constraints, and interactions between different elements?

Before reading the results, use the [model and geometry guide](../models.md). Identify the object, dimensions, incident wave, invariant/repeated directions, and reference planes in the drawing.

## A. Predict the effect of a geometry sequence

Switch between the expanded library, original limited library, identical ridges, and reversed sequence. Compare incident-normalized desired-order power, the fraction conditional on transmission, local-mask estimates, and the full-wave order table. The reversed sequence's desired order is $m=-1$.

:::{iframe} ../interactives/synthesis-explorer.html
:width: 100%
:class: synthesis-explorer-frame
:title: Metasurface synthesis explorer

Four saved, validated TE ridge supercells. Controls inspect precomputed Maxwell results and their local approximations; they do not execute a solver.
:::

[Open the explorer in a full browser page](/interactives/synthesis-explorer.html), or download it for offline use: {download}`../interactives/synthesis-explorer.html`.

**Prediction:** which directions are allowed, which carry power for identical cells, and what changes after reversal? Explain why a local-mask power imbalance cannot be called physical absorption here.

**Deliverable:** a comparison of the four cases, with denominator definitions, model limits, and one symmetry prediction checked against the data. The explorer downloads a selected design together with its evidence and metadata.

## B. Execute beam synthesis and full-wave verification

**Status:** executed reference available in the [beam-steering notebook](../notebooks/05-beam-steering.ipynb).

Download the complete runnable bundle: {download}`../downloads/chapter-05-synthesis.zip`. Extract it before running. It preserves both notebooks, both Python modules, requirements, the original Chapter 3 library, Chapter 5 data, and the audit script. Use the [existing environment instructions](../getting-started.md).

Individual downloads: {download}`../notebooks/05-beam-steering.ipynb`, {download}`../simulations/metasurface_synthesis.py`, {download}`../data/chapter-05/beam-steering.json`, {download}`../data/chapter-05/extended-library.csv`, and {download}`../data/chapter-05/validation.json`. A notebook alone requires its companion modules/data; the ZIP is the easiest complete starting point.

### Inputs

| Parameter | Reference |
| --- | --- |
| Wavelength | $1.55\,\mu\mathrm m$ |
| Pitch / number of cells / supercell period | $0.65\,\mu\mathrm m$ / 6 / $3.90\,\mu\mathrm m$ |
| Ridge/gap and incident/output indices | 2.4/1 and 1/1.5, real constants |
| Illumination | Normal TE, $E_y$, $k_y=0$, incidence from $z<0$ |
| Original / expanded common height | $0.60$ / $1.80\,\mu\mathrm m$ |
| Expanded widths | 161 samples over $0.08$–$0.57\,\mu\mathrm m$ |
| Library acceptance | $T\geq0.8$ for selection; separately pass numerical checks |
| Desired order | $+1$ at approximately $15.36^\circ$ in the substrate |
| Phase references | $r$ at $z=0$, $t$ at the common bottom face |

### Procedure

1. Derive the target gradient, desired angle, and complete exterior open-order sets.
2. Restart the kernel and run the notebook. Inspect the declared height screen and distinguish exploratory curves from accepted library entries.
3. Recompute the 161-width library at $M=24$ and check each row at $M=32$. Retain complex response, power, phase, and validation metadata.
4. Search the fixed global-offset grid using unit-cell phase error, then select widths subject to $T\geq0.8$. Preserve the limited-library result as a comparison.
5. Compute exact staircase coefficients, including the sinc factor, for local reflected/transmitted estimates.
6. Solve the complete coplanar-ridge supercells for all four sequences. Account for every open order separately on each side.
7. Refine the expanded geometry over the reported $M$ sequence. Compare every final design at $M=144$ versus $192$, separately from power residuals.
8. Reconstruct the repeated field, while using modal coefficients for far-field power fractions.
9. Export geometry, selection, source hashes, conventions, full-wave powers, local estimates, and numerical changes.

### Reference acceptance

| Check | Criterion |
| --- | --- |
| Each extended-library row | $|\Delta t|<5\times10^{-4}$, $\Delta R,\Delta T<5\times10^{-4}$, phase change $<0.05^\circ$, balance error $<10^{-8}$ |
| Phase selection | All six expanded targets within $5^\circ$ after applying the stated offset |
| Full supercell refinements | Each open-order power and open complex-$t_m$ change below $10^{-4}$ at $M=144/192$ |
| All-channel lossless balance | $|1-R-T|<10^{-8}$ |
| Identical-cell embedding / mirror reversal | Complex forbidden-amplitude or mirrored-power errors below $10^{-10}$ in the specified tests |
| Separate implementation | Three matching-$M=48$ grcwa cases; refined raster power and complex-$t_0$ differences below $10^{-4}$ |

Run the numerical audit from the extracted folder or repository root:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_chapter05.py --grcwa
```

The optional comparison refines grcwa's raster from 512 to 4096 cells; the course solver uses analytic rectangle Fourier coefficients. Both use RCWA. Without `--grcwa`, the script records that this optional comparison was not run. The audit includes reference-specific configurations; adapt and revalidate them for a changed physical experiment.

**Deliverables:** executed notebook, declared objective/selection grid, both libraries, four geometry sequences, all-channel power tables, field/response figures, convergence, audit, and an interpretation of local-versus-collective differences. These are ideal infinite-periodic TE results, not finite-device or experimental efficiencies.

## C. Execute focusing and polarization models

**Status:** executed reference available in the [wavefront-model notebook](../notebooks/05-wavefront-models.ipynb). Run the beam notebook first because it writes the expanded library. Downloads: {download}`../notebooks/05-wavefront-models.ipynb` and {download}`../data/chapter-05/wavefront-models.json`.

### Scalar line-focus activity

Use a 48-cell, $31.2\,\mu\mathrm m$ aperture, design distance $30\,\mu\mathrm m$, and output index 1.5. Derive the exact path-length phase, compare continuous/sampled/local-library fields, propagate with the outgoing angular spectrum, and inspect FWHM, a consistently normalized peak, and line-intensity concentration within $\pm1\,\mu\mathrm m$.

Refine window size independently from sample spacing for **each** of the continuous, sampled-phase, and local-library apertures. The displayed reference uses $\Delta x=0.10\,\mu\mathrm m$ and a $204.8\,\mu\mathrm m$ FFT window. The window study fixes $\Delta x=0.05\,\mu\mathrm m$ and uses $102.4/204.8/409.6\,\mu\mathrm m$ windows; the grid study fixes the $409.6\,\mu\mathrm m$ window and uses $\Delta x=0.10/0.05/0.025/0.0125\,\mu\mathrm m$. Every peak uses one frozen continuous-reference denominator. Integrate between the same physical focal-window endpoints and report both the integral divided by aperture width and its fraction of each model's total line intensity. The final independent pairs check profile, FWHM, peak, fixed-window integral, and concentration changes against the limits saved in the notebook/JSON; a failed check must remain visible. The notebook also checks plane-wave phase and propagating-bin norm. These concern prescribed scalar fields; no finite-lens Maxwell validation or physical focusing-efficiency claim follows.

### Jones-matrix activity

Define the laboratory circular basis explicitly. Verify converted phase $2\sigma\theta$ for ideal half-wave elements, unconverted amplitude, and conversion fraction $\sin^2(\delta/2)$ for ideal retarders. Check analytical identities and unitarity to $10^{-12}$. Explain why this model needs a physical anisotropic vector library before device claims.

**Deliverables:** phase/field profiles, scalar metrics with denominators, window/grid changes, axial response, and Jones conversion/phase plots. State which figures come from each model and which physical effects are absent.

## D. Finite-device and independent-method outline

**Status:** outline; a finite full-wave beam deflector/metalens and an FEM/FDTD cross-check have not been executed.

Select a small aperture and preserve its full geometry, illumination beam, material model, and reference planes. Begin with matched interface/film benchmarks, then reproduce a periodic reference, then simulate finite aperture edges with appropriate absorbing boundaries. For FDTD refine mesh, PML, time decay, and source/monitor placement; for FEM refine mesh/order, exterior domain, and port/near-to-far settings.

Compare a precisely defined angular or focal observable with the local/scalar prediction. For a lens define incident power, transmitted power, focal integration region, polarization channel, and collection geometry. Do not substitute a scalar line-intensity fraction for a full-wave power measurement. Relevant methods appear in [Meep's near-to-far examples](https://meep.readthedocs.io/en/latest/Python_Tutorials/Near_to_Far_Field_Spectra/).

**Deliverables:** solver/model files, independent refinements, geometry-to-model mapping, order/angular or focal metrics, numerical cost, and unresolved differences.

## E. Amplitude, bandwidth, and robust-design outline

**Status:** outline; hologram reconstruction, a vector full-wave geometric-phase device, material-dispersive broadband optimization, and fabrication-tolerance optimization have not been run.

Choose one extension with a declared target and constraints. Examples are an amplitude-apodized scalar aperture followed by physical realization, a vector anisotropic library with desired/unwanted polarization channels, a multiwavelength design using justified dispersive materials, or a bounded geometry optimization with independent verification. Specify dimensions and fabrication limits before fitting or optimizing. Hold out wavelengths, incidence conditions, or tolerance cases where the research claim requires generalization.

**Deliverables:** objective and feasible domain, data/model/solver version, baseline, proposed design, independent verification, and a cost/robustness report. These stages connect naturally to Chapter 6 and Chapter 10.

## Contribution handoff

Preserve the topic IDs and original evidence labels. Submit code, editable notebooks, data, environment, references, plots, and an execution-status note through the [contribution guide](../contributing.md). Routine publication displays saved results; it does not rerun heavy simulations.
