---
title: 'Lab 10: Learn, design, and verify a metasurface response'
short_title: AI computational lab
---

# Lab 10: Learn, design, and verify a metasurface response

**Topic ID:** `ms-13-ai-metasurfaces`

**Companion:** [Chapter 10](../chapters/10-ai-metasurfaces.md)

**Question:** can a surrogate predict unseen responses and propose a design that survives verification?

The investigation has four stages. Stage A supplies a runnable analytical starter. Stages B-D are computational lab outlines for student contributions, with required inputs and validation defined in advance.

## A. Learn a synthetic resonant response

**Available:** [the executed starter notebook](../notebooks/10-resonant-surrogate.ipynb). It uses NumPy and Matplotlib, requires no GPU, and contains its data generator. The model is a synthetic lossless resonant sheet with a dimensionless design coordinate, as derived in Chapter 10.

Download the editable source: {download}`../notebooks/10-resonant-surrogate.ipynb`. The [environment instructions](../getting-started.md) explain how to run it.

### Learning goals

Separate training, model selection, and testing; preserve whole geometries in each split; compare a nearest-neighbor baseline with kernel regression; and verify an inverse proposal using the exact analytical model.

### Editable parameters

| Parameter | Default | Purpose |
| --- | --- | --- |
| Design coordinate $g$ | $0.05$ to $0.95$ | Synthetic design family |
| Normalized frequency $\Omega$ | $0.8$ to $1.2$, 101 samples | Response spectrum |
| Geometry samples | 80 | Complete spectra before splitting |
| Training / validation / test | 40 / 20 / 20 geometries | Distinct uses of data |
| Random seed | 24 | Reproducible split |
| Target design coordinate | 0.623 | Creates a feasible target for the inverse exercise |
| Candidate search | 901 designs over $[0.05,0.95]$ | Bounded inverse search |

### Procedure

1. Derive the lossless power identity and check the resonant and off-resonant limits.
2. Generate complex transmission spectra, preserving a unique ID for every design coordinate.
3. Split IDs before model fitting. Do not split frequency rows independently.
4. Fit a nearest-neighbor baseline and select kernel length scale/regularization using validation data only.
5. Evaluate both methods on the untouched test set. Plot errors by geometry and overlay an example spectrum.
6. Create the target analytically, search the surrogate on the candidate grid, and evaluate the selected design with the exact formula.
7. Compare predicted and verified target errors. Repeat with fewer training designs and discuss the effect of data coverage.

### Evidence and deliverables

Submit a notebook run from a fresh kernel, the train/validation/test IDs, selected hyperparameters, test metrics, and an overlay of target, predicted, and analytically verified spectra. Report the maximum power-balance residual of the generator. Declare the search-grid resolution; agreement within one grid spacing does not prove a continuous global optimum.

The starter's assertions check split separation, finite outputs, and the analytical conservation identity. Its reported errors measure performance on this chosen toy problem. There is no claimed accuracy threshold for a real device.

## B. Replace the generator with a validated unit-cell library

**Status:** outline; no full-wave dataset is supplied.

**Prerequisites:** periodic boundary conditions, Floquet ports, S-parameter normalization, and a solver convergence study. Choose one geometry family and one material model before scaling up the dataset.

1. Define the design bounds, units, period, substrate/superstrate, polarization, frequency band, and incidence conditions.
2. Converge representative cells in mesh size or harmonic order, including resonances and extreme geometries. Define a convergence tolerance justified by the design objective.
3. Save complex coefficients, channel identities, reference planes, and all-channel power balance. Record failures rather than silently removing difficult samples.
4. Split by geometry. Reserve a further interval or family for a clearly labeled extrapolation challenge.
5. Compare retrieval/interpolation, kernel regression, and a small neural network on exactly the same data split.

**Deliverables:** a versioned dataset manifest, solver setup, environment file, split IDs, learning curves, spectral error distributions, and three independently re-simulated test examples. Explain the difference between the solver's numerical uncertainty and the surrogate's prediction error.

**Acceptance:** the dataset can be regenerated or traced to archived solver outputs; the predeclared solver convergence criterion passes; test cases never determine model settings; and claimed accuracy is backed by per-device and aggregate metrics. If a criterion fails, report it and restrict the claim.

## C. Inverse design under physical and fabrication constraints

**Status:** outline; follows Stage B.

Choose a target with explicit amplitude, phase, bandwidth, or polarization requirements. Start with a target from a known feasible library cell, then introduce a target whose feasibility is unknown.

Compare (i) the nearest response in the library, (ii) a bounded optimizer using the surrogate, and (iii) a conventional search with a matched electromagnetic-solver budget. An optional tandem network or conditional generative model is an extension after the baselines work.

For each method, report the same objective, constraints, allowed calls, and stopping rule. Verify several candidates with a converged solver. Test fabrication perturbations and evaluate whether a unit-cell approximation is adequate for the intended array; a complete-device claim requires a suitable device-level calculation.

**Deliverables:** target specification, candidate geometries, surrogate and verified responses, constraint checks, perturbation results, and a cost table including dataset generation. Explain failures and infeasible targets rather than selecting only successful examples.

## D. Uncertainty and active learning

**Status:** outline; follows Stage B or C.

Under a fixed budget of new solver evaluations, compare random sampling with an explicitly defined acquisition rule. Possible signals include ensemble disagreement, distance from training data, or estimated improvement in the design objective.

Keep a fixed held-out evaluation set outside the acquisition loop. Run multiple seeds. Evaluate learning curves against total electromagnetic calls, not merely model epochs. Check whether uncertainty tracks observed error and whether the acquisition strategy repeatedly misses narrow resonances or boundaries.

**Deliverables:** acquisition history, data/version records, fixed-test learning curves, uncertainty-versus-error plots, and the final independently verified design. Explain when the extra modeling overhead is justified.

## Suggested student contribution packages

| Package | A manageable contribution |
| --- | --- |
| Data and physics | One unit-cell family, convergence report, and documented sample data |
| Baselines | A reusable interpolation or kernel model with held-out evaluation |
| Neural model | A small network compared fairly with the existing baselines |
| Design and robustness | A constrained inverse objective plus solver and tolerance checks |
| Teaching | Clear figures, worked derivations, and exercises connected to the notebook |

Use the [contribution guide](../contributing.md) and the lab template. Keep each pull request focused enough for a scientific review. These packages are suggestions; they do not assign work to named students.
