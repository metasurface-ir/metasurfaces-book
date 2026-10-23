---
title: 'Lab 6: When Is a Simulation Accurate?'
short_title: Numerical validation lab
---

# Lab 6: When Is a Simulation Accurate?

**Question:** how can a perfectly balanced simulation mislead a designer? Predict what will happen when the film mesh is refined, then compare the same observables at the same physical reference planes.

Read [Chapter 6](../chapters/06-numerical-methods.md) and its [worked examples](../chapters/06-numerical-guide.md). The [executed notebook](../notebooks/06-numerical-methods.ipynb) is the authoritative calculation. The source bundle contains the solver, notebook, reference data, validator, and standalone explorer.

## Explore the saved evidence

The controls select saved Python calculations; they do not solve Maxwell's equations in the browser. All values correspond to the published slab and specified numerical settings. Broad intuition diagrams and classroom demonstrations are reserved for the companion course site.

<iframe src="../interactives/numerical-explorer.html" title="Mesh, field and boundary validation explorer" width="100%" height="1130" loading="lazy" style="border:0;border-radius:14px"></iframe>

[Open the explorer](../interactives/numerical-explorer.html) · [Download complete executable sources](../downloads/chapter-06-numerical.zip)

## Run the investigation

Extract the complete ZIP, preserve its folders, use Python 3.12, install `requirements-labs.txt`, and launch JupyterLab. Open `notebooks/06-numerical-methods.ipynb`, restart the kernel, and run all cells. NumPy/SciPy/Matplotlib run on a CPU. No commercial solver, GPU, network dataset, or optional grcwa package is required. Saved outputs document the published run; edits create a new experiment.

Run `python scripts/validate_chapter06.py` from the extracted root for independent checks. In a full checkout, after executing/saving and validating, run `python scripts/export_chapter06.py` to regenerate figures, explorer, and ZIP. Physical inputs and numerical controls are separate in the first parameter cell. Revalidate changed parameters; the fixed benchmark audit describes the stated reference cases.

## Executed stages and student tasks

| Stage | Change only | Predict and report |
| --- | --- | --- |
| A: mesh | Cells through the film | Complex transmission error, circular phase error, power defect, algebraic residual, field error |
| B: domain | Exterior padding at fixed mesh | Face-referenced coefficient invariance and actual monitor distances |
| C: boundary | Right outgoing multiplier | Backward-wave power and oscillatory padding dependence |
| D: extraction | Discrete versus continuum deembedding | Phase drift while powers remain unchanged |
| E: harmonics | RCWA retained orders | Differences in target-order power with tiny conservation error |

1. Save a prediction before changing a control. Which diagnostic certifies the assembled equations, and which compares with the independent physical reference?
2. Find a coarse mesh that balances power but fails $|t-t_{\rm exact}|<10^{-3}$. Then identify the first sampled mesh satisfying that amplitude target. Also test a $0.1^\circ$ phase criterion where transmission exceeds a stated floor.
3. Compute observed convergence order using four consecutive fine meshes. State the range used, and explain why a coarse or roundoff-limited range is unsuitable.
4. Move only the exterior boundary. Compare the matched case, the deliberately mismatched case, and wrong deembedding. Use outgoing/backward flux rather than the squared total field at a single node.
5. Inspect the Chapter 5 harmonic companion. State why the highest retained result is a comparison reference, and why RCWA agreement does not constitute experimental validation.
6. Change one physical input, rerun, and assess whether the published mesh remains sufficient. Preserve the original result alongside the new one.

## Further lab outlines

These stages are **not executed** in this release.

- **FDTD slab:** reproduce the same slab and phase planes in a time-domain solver. First normalize against an empty-domain run. Refine spatial resolution, duration/field decay, source bandwidth, absorber thickness, and absorber separation independently. Compare complex amplitudes over a stated band, keeping the constitutive model identical.
- **FEM patterned cell:** reproduce one Chapter 3 ridge with matched geometry, periodic phase, polarization, and outgoing order normalization. Refine element size/order and boundaries independently. Compare all open-order powers and face-referenced amplitudes; archive the model and solver version.
- **Finite device:** begin with a modest finite array. Separate finite-size/illumination changes from numerical refinements. State why its far-field observable differs from an infinite periodic supercell efficiency.
- **Material/model uncertainty:** vary a documented refractive-index or geometric uncertainty only after numerical controls pass. Report sensitivity separately from discretization error; do not treat assumed uncertainty as a measured distribution.

## Deliverable

Submit an editable notebook, parameters/environment, data and original plots, one rejected coarse case, one accepted result, a table of independent refinement controls and tolerances, and a paragraph on unsupported claims. Include figure provenance and references following [the source and reuse guide](../attribution.md). The [worked guide](../chapters/06-numerical-guide.md) supplies self-check answers and a suggested rubric.
