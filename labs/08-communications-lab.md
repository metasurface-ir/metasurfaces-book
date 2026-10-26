# Lab ms-16: aperture-to-link investigations

**Chapters:** 2, 5, 6, 7, 8. **Status:** executed scalar channel model and independent analytical/numerical checks; device and measured-link stages remain outlines.

Study the [chapter](../chapters/08-communications.md), [six worked examples](../chapters/08-communications-guide.md), and [executed notebook](../notebooks/08-communication-links.ipynb). The browser below displays the notebook’s saved data; no Python installation is needed.

<iframe class="communications-explorer-frame" src="../interactives/communications-explorer.html" title="Aperture geometry, link power, bandwidth and training explorer" width="100%" height="1700" loading="lazy" style="border:0;border-radius:14px"></iframe>

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/communications-explorer.html" target="_blank" rel="noopener">Open the browser lab in a new tab</a> · [Download executable notebook and model sources](../downloads/chapter-08-communications.zip)

## Predict, inspect, explain

| Investigation | Prediction | Evidence to record |
| --- | --- | --- |
| Geometry and focus | Does the plane law focus as strongly as the spherical law? | Geometry, phase map, common-reference cut and target loss |
| Power and interference | Does an extra path always help? | Maximum/minimum received power, common phase, SNR and assumptions |
| Bandwidth | Does a frozen 28-GHz phase law keep the beam at x = 8 m? | Target penalty and sampled peak at 25, 28 and 31 GHz |
| Training and errors | Does testing 65 beams beat testing 17? | Gross/net rates at 100, 200 and 500 symbols; phase-error interpretation |

1. Compare spherical, plane and two-bit laws at x = 8 m, then move the receiver by 0.4 m without reprogramming.
2. Sweep the common phase of the direct-plus-assisted path. Explain the cross term before changing transmit power.
3. Compare 25, 28 and 31 GHz at the same receiver; distinguish movement of the sampled lateral peak from a complete three-dimensional focal volume.
4. Inspect each training budget. State why the user at 8.37 m differs from the reference target at 8 m.
5. Rerun the notebook with one changed assumption. Keep the original results and include a case that fails your objective.

## Reproduce and audit

Extract the complete source ZIP and preserve its directories. Use Python 3.12 and a virtual environment, install requirements-labs.txt, then launch JupyterLab and restart/run the notebook. The first code cell exposes the reference parameters; the shared model is simulations/communication_link.py. Calculations use a CPU.

Run the following command:

```
python scripts/validate_chapter08.py
```

from the extracted root. This audit checks declared baseline cases; it does not certify arbitrary edited parameters. The notebook writes data/chapter-08/reference.json, so preserve that file before experimentation. The audit records its model hash and parameters in validation.json. In a complete repository checkout, run the geometry and figure exporters after notebook execution and validation:

```
python scripts/export_communications_geometry.py
python scripts/export_chapter08.py
python scripts/export_figure_provenance.py
```

The browser renderer rejects stale model hashes or mismatched audited parameters. Numerical source and data are shared between languages. Persian notebook narratives and browser controls are translated; scientific notebook plot labels are shared.

## Further computational lab outlines

The following stages are **not executed validations** in this release. Agree numerical tolerances and a fixed comparison budget before implementation.

| Stage | Implementation task | Acceptance evidence |
| --- | --- | --- |
| A: calibrated hardware | Replace ideal coefficients with a frequency/angle/bias-dependent complex library | Units and reference planes; held-out state checks; passivity and all propagating channels; no duplicate efficiency factor |
| B: electromagnetic cross-check | Compare a finite aperture or justified subproblem against a converged vector solver | Mesh/domain convergence, polarization, edge/coupling error, matched receiver power definition |
| C: noisy beam training | Add complex Gaussian pilot noise, finite pilot energy, switching time and receiver motion | Repeat seeded trials; report selection errors, outage with confidence intervals, total pilot energy and net rate |
| D: wideband link | Allocate a fixed total power across subcarriers; include measured dispersion and appropriate cyclic prefix | Noise per subcarrier, delay-spread check, frequency-grid refinement and integrated rate; compare fixed phase and feasible delay hardware |
| E: multiuser scheduling | Define two or more channels and a transmit precoder; optimize one clearly stated fairness/sum-rate objective | Baseline without RIS, equal power and overhead budgets, SINR including interference, held-out positions |
| F: sensing extension | Build a round-trip channel with explicit transmitter/target/receiver geometry and noisy observations | Delay/angle ambiguity, localization error across repeated trials and calibration uncertainty; no inference from beamwidth alone |

Use authorized or original data and cite the acquisition/model source. The companion visual course can host broad application illustrations; keep runnable models, numerical comparisons and validation evidence in this book.

## Deliverable

Submit the notebook and parameter file, an annotated geometry drawing, three comparisons on consistent normalization, one independent calculation, and a brief limitations statement. Report whether each quantity is a channel gain, received power, rate benchmark, mean over errors, or measured result. The [worked guide](../chapters/08-communications-guide.md) supplies self-check answers and a rubric.
