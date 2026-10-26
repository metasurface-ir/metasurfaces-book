# Lab ms-17: fabrication and measurement

**Question:** Which discrepancies come from the device, which from the instrument, and which from the reference plane? Predict before changing a control. This executed investigation uses synthetic data, an assigned one-port resonator and an illustrative material spectrum.

Prerequisites: Chapters 2, 3 and 6. Use the [theory](../chapters/09-materials-measurement.md) and [worked examples](../chapters/09-measurement-guide.md). Allow one session for exploration and one for a reproducible notebook report.

## Browser investigation

The four tabs use the executed notebook's saved arrays. Controls select documented cases; the browser does not run a full-wave solver or acquire hardware data. Material and tolerance models are separate. The geometry sketch identifies the possible patch and the modeled reference planes.

<p><a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/measurement-explorer.html" target="_blank" rel="noopener">Open the measurement lab in a new tab</a></p>

<div class="measurement-explorer-frame"><iframe src="../interactives/measurement-explorer.html" title="Synthetic materials, fabrication and measurement lab" width="100%" height="1700" loading="lazy"></iframe></div>

| Tab | Predict and investigate | Record |
| --- | --- | --- |
| Materials | Increase damping. Do real and imaginary permittivity both change? | Pole value, passivity sign and why this is not a measured material fit |
| Tolerances | Compare negative, zero and positive correlation; introduce a width bias | Predicted versus sampled spread, acceptance and meaning of its interval |
| Calibration | Compare raw reading, port calibration and surface-plane correction | Complex response at a selected frequency; a phase error hidden by power |
| Uncertainty | Change placement spread; increase readings in the separate averaging model | Complex ellipse, RMS about truth, and the persistent placement floor |

## Execute and inspect

Open the [executed notebook](../notebooks/09-fabrication-measurement.ipynb) or use the [Python/notebook/data source bundle](../downloads/chapter-09-measurement.zip). Extract the whole bundle, preserve directories and install requirements-labs.txt in a Python 3.12 environment. Restart and run all notebook cells. The source archive contains no browser HTML.

Run python scripts/validate_chapter09.py separately. The saved validation report checks energy balance, independent error-box algebra, a held-out fourth standard, reference-plane transport, derivative refinement, tolerance statistics and the ellipse probability threshold. It checks the declared baseline, not every parameter a student might edit.

Keep an untouched copy of data/chapter-09/synthetic-sweep.csv and reference.json before editing: the notebook rewrites them. The CSV contains frequency in GHz, raw complex readings, three complex standard readings, assigned truth and offset in mm. It is a noiseless synthetic processing exercise. Noise, standard-characterization error and placement uncertainty are introduced separately in the Monte Carlo section.

First reproduce the baseline; then change one assumption. Useful challenges are a biased width population, nearly redundant calibration standards, a common phase error in the standards, or a misplaced sample. Preserve both the original and changed evidence.

## Further computational lab outlines

These six extensions are **not executed experimental validations** in this release. Select a feasible dataset and define numerical acceptance criteria before implementing one.

| Stage | Implementation | Required evidence |
| --- | --- | --- |
| A: material characterization | Fit a passive dispersion model to original or licensed complex material data, with stated band and temperature | Source and reuse permission, units/sign convention, residuals on held-out frequencies, parameter covariance and behavior outside the fit band |
| B: fabricated geometry | Import measured width, height, taper and roughness statistics into a converged cell model | Calibrated metrology, spatial sampling, parameter correlations, numerical convergence and comparison with the nominal design |
| C: nonideal standards | Replace ideal standards with characterized complex responses and correlated uncertainty; include drift | Separate calibration and verification artifacts, conditioning, held-out residuals, uncertainty propagation without passive clipping |
| D: free-space microwave measurement | Model finite illumination, sample edges, angular/polarization collection and a justified background/reference procedure | Cable-port calibration separated from fixture calibration, ungated/gated comparisons, reference-plane control and missing-power bounds |
| E: optical characterization | Process dark/reference/sample spectra; add a phase-sensitive or ellipsometric measurement when required | Detector linearity, collection numerical aperture, spectral resolution, polarization, reference stability and identifiable optical parameters |
| F: blind device comparison | Freeze a model prediction using characterized geometry/materials, then compare independent sample data | Raw-data provenance, matched measurand, uncertainty budget, held-out samples, structured residuals and a documented model revision |

Use original or authorized datasets. Cite acquisition and modeling sources near the relevant results. Broad fabrication photographs and application illustrations can belong in the companion visual course; keep executable processing, validation and numerical evidence here.

## Deliverable

Submit a rerunnable notebook, parameter/seed record, annotated geometry and reference planes, raw and corrected complex data, one independent check, and a compact uncertainty budget. Show a failed assumption as well as a successful correction. Label every figure as a model prediction, synthetic observation or actual measurement.

For a pull request, update both language narratives, preserve shared code cells, record figure provenance and run the bilingual checks described in [contributing](../contributing.md). Instructor review should address physical assumptions and interpretation as well as code execution.
