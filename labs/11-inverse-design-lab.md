---
title: 'ms-11: Bounded optimization with independent checks'
short_title: Inverse design lab
---

# ms-11: Bounded optimization with independent checks

**Chapters 5, 6 and 10.** Can six physical width changes improve the Chapter 5 design? Build a direct-solver baseline for later AI comparisons. Separate **search**, **selection** and **validation**.

**Executed:** two reproducible bounded Powell searches, complete objective histories, frozen-candidate harmonic checks, withheld wavelengths, fourteen width perturbations and a separate grcwa comparison with raster refinement. No global optimum, fabrication yield, independent FEM/FDTD or experiment is claimed.

## What can the optimizer change?

Only the six ridge widths change. Height 1.8 µm, pitch 0.65 µm, constant real indices, normal TE incidence and design wavelength 1.55 µm stay fixed. The air/ridge/substrate model and two phase planes remain the same. The interactive drawing shows both designs; the notebook plots their actual x–z sections together.

<iframe src="../interactives/design-studies.html?lab=inverse" title="Bounded optimization geometry and validation explorer" width="100%" height="1650" loading="lazy" style="border:0;border-radius:14px"></iframe>

<a href="../interactives/design-studies.html?lab=inverse" target="_blank" rel="noopener">Open the browser lab in a new tab</a> · [Executed notebook](../notebooks/11-inverse-design.ipynb) · [Complete source bundle](../downloads/design-studies.zip)

Controls inspect saved results; they do not run an optimizer in the browser. All plots and geometry views come from recorded parameters.

## State the design problem

$$
\underset{\mathbf w}{\operatorname{maximize}}\quad T_{+1}(\mathbf w;\lambda_0),\qquad
0.08\ \mu\mathrm m\leq w_j\leq0.57\ \mu\mathrm m,\quad j=1,\ldots,6.
$$

Use incident-normalized power, not the desired fraction of transmitted power. The bounds preserve positive ridges and gaps; they are not certified foundry rules. Start from the Chapter 5 baseline and a seeded perturbation of it. Each search allows at most 1,000 objective evaluations at M=32. Retain the **best feasible point evaluated**, including starting points, even if a run terminates at a worse point.

This local derivative-free search is a transparent small-dimensional baseline, not evidence that Powell is best for general metasurface design. See the [SciPy Powell documentation](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-powell.html) for bounds and stopping behavior.

## Run and freeze the candidate

Extract the complete ZIP, install `requirements-labs.txt` in Python 3.12 and restart/run `notebooks/11-inverse-design.ipynb`. Also install `requirements-validation.txt` to repeat the published grcwa check. Without grcwa, the notebook explicitly records that check as unexecuted; the ordinary optimization still runs.

1. **Baseline:** run the original geometry at search and verification resolutions. Preserve it even when a later search fails to improve.
2. **Search:** save every objective query, best-so-far value, seed, budget and stopping reason. `success=True` certifies neither global optimality nor improvement over the start.
3. **Select and freeze:** choose the highest objective among search evaluations and record the widths before the checks below. If these checks subsequently select a different design, they become development data and require new validation cases.

## Challenge the selected result

| Check | Change | Evidence and limitation |
| --- | --- | --- |
| Harmonic refinement | M=32, 64, 96, 144, 192 | Compare efficiency and complex target amplitude at fixed geometry/phase planes |
| Separate implementation | grcwa at matched M=48; 4096/8192 raster cells | All retained reflected/transmitted orders; same RCWA method family |
| Withheld operation | λ=1.45, 1.50, 1.60, 1.65 µm | Both baseline and selected design; absent from the objective |
| Geometry errors | All widths or each separately shifted by ±5 nm | Fourteen deterministic scenarios, not yield or a probability model |
| Numerical identities | Bounds, flux, uniform embedding and mirror symmetry | Catch implementation/setup errors; not experimental validation |

A design can improve the objective wavelength while degrading elsewhere. Report that tradeoff. A nominal single-wavelength search is not robust or broadband optimization. [ms-09](09-dispersion-lab.md) supplies the analysis needed for a separate spectral objective.

## Deliverable and extensions

Submit both geometries, objective/bounds, complete history, actual evaluation counts, worse/failed starts, refined values, withheld comparisons and limitations. Run all three notebooks, then `python scripts/validate_design_studies.py`; add `--grcwa` to repeat the implementation comparison. This audits the published reference, not arbitrary edited parameters.

**AI comparison outline:** use the same physical widths, materials and objective. Reserve geometry-disjoint surrogate tests. Count training-label generation in the full-wave budget, and check final proposals with the same frozen-candidate protocol. Chapter 10's abstract resonant coordinate is not automatically a ridge width: a geometry-to-response surrogate needs geometry-labeled data.

**Robust/multiwavelength outline:** define training wavelengths/errors first, optimize their specified objective, then reserve new conditions for validation. Adjoint gradients, topology optimization, real-process fabrication rules, FEM/FDTD and experiment remain extensions.

## Sources and links

[Pestourie and colleagues](https://arxiv.org/abs/1808.04215) discuss optimization with local approximations and Maxwell comparisons. This original restricted direct-supercell example does not reproduce their devices or figures. Follow the [source and reuse guide](../attribution.md).

Return to [Chapter 5](../chapters/05-metasurface-synthesis.md), [Chapter 6](../chapters/06-numerical-methods.md) or [Chapter 10](../chapters/10-ai-metasurfaces.md).
