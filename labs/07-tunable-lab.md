---
title: 'Lab 7: Tune, Program, and Calibrate a Reflector'
short_title: Tunable control lab
---

# Lab 7: Tune, Program, and Calibrate a Reflector

**Lab ID: `ms-15-tunable-control`.** Start with [Chapter 7](../chapters/07-active-tunable.md) and its [worked guide](../chapters/07-tunable-guide.md). Prerequisites are phasors and power in Chapter 2, diffraction in Chapter 4, synthesis in Chapter 5, and independent validation in Chapter 6. Identify the possible cell and the assigned equivalent circuit before reading a plot.

## Explore the reference

The four tabs select saved Python results: a voltage/frequency sweep, a programmed 32-source aperture, driver dynamics and temporal harmonics, and the full calibration query history. The browser runs no full-wave solver. The geometry is explanatory; RF circuit parameters are assigned directly. Frequency is 10 GHz in the array, dynamics and feedback tabs.

<iframe class="tunable-explorer-frame" src="../interactives/tunable-explorer.html" title="Tunable surface, array, dynamics and feedback explorer" width="100%" height="1550" loading="lazy" style="border:0;border-radius:14px"></iframe>

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/tunable-explorer.html" target="_blank" rel="noopener">Open the browser lab in a new tab</a> · [Download executable notebook and model sources](../downloads/chapter-07-tunable.zip)

## Predict, change one control, explain

| Investigation | Prediction to record | Observable |
| --- | --- | --- |
| A: tunable cell | Which direction does resonance move with voltage? | Complex trajectory, phase and reflected fraction |
| B: coding | Will 16 voltage commands equal 16 ideal phases? | Cell-state pattern, target metric and unwanted lobes |
| C: dynamics | Does a linear voltage step give linear phase? | Voltage/phase versus time and temporal harmonics |
| D: feedback | Can nominal 8 V recover the target after a capacitance shift? | All queries, error and independently predicted bias |

1. At 10 GHz, compare 0 V, the resonant bias and 20 V. Record magnitude as well as phase; identify an unreachable complex target.
2. Steer to 25° using ideal one-bit, two-bit and four-bit states, then the 16-voltage circuit. Keep the common normalization. Explain the binary mirror beam.
3. Compare instantaneous 3/14-V switching with the 4-μs RC waveform at 20 kHz. Explain why the carrier and multiple sidebands change together.
4. Inspect the 17-point scan and refinement. Count all 26 measurements and compare the selected voltage with the independent 9.08-V answer.
5. In the notebook, change one assumption: resistance, phase offset, codebook, plant error, duty cycle or driver time constant. Preserve the baseline and report one case that fails the original objective.

## Reproduce and validate

Extract the complete ZIP and preserve its folders. Use Python 3.12, create a virtual environment, install `requirements-labs.txt`, and launch JupyterLab. Restart and run [the notebook](../notebooks/07-tunable-metasurfaces.ipynb). NumPy, SciPy and Matplotlib run on a CPU. No hardware, GPU or commercial solver is needed. The first code cell exposes physical and sampling parameters; the shared model is `simulations/tunable_surface.py`.

Run `python scripts/validate_chapter07.py` from the extracted root. It checks the independent boundary solve, passivity, lossless and matched limits, array symmetry and bounds, quantization quadrature, calibration answer, an independent ODE solution, temporal Fourier coefficients and Parseval. The audit evaluates its declared reference cases; a passing baseline does not certify a modified experiment. Preserve `data/chapter-07/reference.json` before rerunning the notebook, which writes that file. In a full checkout, after execution and validation, run `python scripts/export_tunable_geometry.py` and `python scripts/export_chapter07.py`. Publication rejects browser evidence made with changed model code or parameters that no longer match the reference audit.

## Further computational and experimental lab outlines

These are proposed extensions, **not executed device validations** in this release.

| Stage | Required work | Acceptance evidence |
| --- | --- | --- |
| A: calibrated states | Replace the assumed tuning law with documented complex response versus frequency and bias | Reference-plane consistency, repeated measurements and uncertainty; hold out some states |
| B: physical biased cell | Model the actual conductor, substrate, package and bias routing with an appropriate full-wave solver | Mesh/boundary convergence, all relevant channels and material/component provenance |
| C: unlike neighbors | Compare programmed pairs/supercells and a finite aperture with the local library | Complex-error and power comparisons at matched physical conditions |
| D: robust feedback | Add noise, hysteresis, drift, latency and a query budget | Repeated trials, unseen conditions, stopping rule and unreachable targets |
| E: temporal modulation | Solve the electromagnetic transient or a justified frequency-coupled model | Carrier and sidebands, convergence, pump work and port-power normalization |

## Deliverable

Submit the edited notebook, environment and parameters, three annotated comparisons, one failed case, an independent numerical check, and a short model-limit statement. Keep unit-cell/array drawings beside the results they explain. Separate scalar array intensity from efficiency and Fourier envelope weights from a full device energy balance. Attribute external data and use original plots following [the reuse guide](../attribution.md). The worked guide provides self-check values and a rubric.
