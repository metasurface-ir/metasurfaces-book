---
title: 'Lab 10: Learn, design, and verify a metasurface response'
short_title: AI computational lab
---

# Lab 10: Learn, design, and verify a metasurface response

**Topic ID:** `ms-13-ai-metasurfaces`

**Companion:** [Chapter 10](../chapters/10-ai-metasurfaces.md)

**Question:** can a surrogate predict unseen responses and propose a design that survives verification?

The investigation has four stages. Stage A is the completed analytical pilot, with two executed notebooks. Stages B-D are detailed computational lab outlines for student contributions, with required inputs, procedures, deliverables, and review criteria defined in advance. They have not been executed with full-wave data.

| Stage | Central question | Present status | Preparation |
| --- | --- | --- | --- |
| A | Does learning help on a transparent synthetic example? | Two executable notebooks and worked exercises | Complex amplitudes, linear algebra, basic Python |
| B | Can a surrogate reproduce a converged unit-cell library? | Full-wave lab outline | Chapters 2, 3, 4, and 6 |
| C | Does an optimized design survive independent verification? | Full-wave lab outline | Stage B; synthesis and tolerances from Chapters 5 and 9 |
| D | Which new simulations are worth acquiring? | Active-learning lab outline | Stage B, optionally C; basic statistical uncertainty |

Use the [pilot guide](../chapters/10-pilot-guide.md) for the teaching sequence, worked examples, and report criteria.

Before reading the results, use the [model and geometry guide](../models.md). Identify the object, dimensions, incident wave, invariant/repeated directions, and reference planes in the drawing.

## A. Learn a synthetic resonant response

**Available:** [the executed starter notebook](../notebooks/10-resonant-surrogate.ipynb). It uses NumPy and Matplotlib, requires no GPU, and contains its data generator. The model is a synthetic lossless resonant sheet with a dimensionless design coordinate, as derived in Chapter 10.

Continue with [the executed neural comparison](../notebooks/10-neural-comparison.ipynb), which adds scikit-learn, complex linear interpolation, three neural initializations, circular phase metrics, and inverse proposals for every method.

Download the editable sources: {download}`../notebooks/10-resonant-surrogate.ipynb` and {download}`../notebooks/10-neural-comparison.ipynb`. The [environment instructions](../getting-started.md) explain how to run them. Both notebooks contain their data generators and can be downloaded and run independently.

### Learning goals

Separate training, model selection, and testing; preserve whole geometries in each split; compare nearest retrieval, interpolation, kernel regression, and a small neural model; and verify inverse proposals using the exact analytical model.

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
| MLP hidden layers | $(16)$, $(32)$, or $(32,32)$ | Small architecture search on validation data |
| MLP L2 coefficient | $10^{-4}$ or $10^{-2}$ | Six architecture/regularization candidates in total |
| MLP initializations | 24 for selection; 42 and 73 for repeats | Initialization variability without test-based seed selection |
| Phase amplitude threshold | 0.1 | Exclude undefined or weak-amplitude phase, with excluded fraction reported |

### Procedure

1. Derive the lossless power identity and check the resonant and off-resonant limits.
2. Generate complex transmission spectra, preserving a unique ID for every design coordinate.
3. Split IDs before model fitting. Do not split frequency rows independently.
4. In the starter, fit a nearest-neighbor baseline and select kernel length scale/regularization using validation data only. Evaluate the frozen model, then perform and verify the inverse search.
5. In the comparison, reproduce the same generator and split. Add linear interpolation and an MLP. Standardize inputs using training data only; choose architecture/regularization on validation complex RMSE. Freeze the chosen configuration before running the additional initializations.
6. Evaluate all frozen methods on the held-out geometries. Report complex, power, amplitude, worst-case, and masked phase errors, plus physical consistency. Plot every test geometry's error and a fixed example spectrum. Use the complex-transmission disk and signed implied-absorption diagnostic to distinguish artificial loss from implied gain in the reconstructed shunt model; neither quantity is measured material absorption.
7. Create the target analytically. Search each continuous surrogate on the same grid, retrieve an actual training design for the nearest baseline, and evaluate all selected coordinates with the exact formula.
8. Compare predicted and verified target errors. Explain the method ranking without assuming a neural network should win. Plan a separate extension with fewer training designs or a withheld interval; declare that extension's protocol before inspecting its test results.

### Evidence and deliverables

Submit both notebooks run from fresh kernels, the train/validation/test IDs, all validation candidates, selected hyperparameters, optimizer warnings, three neural runs, test metrics, and overlays of target, predicted, and analytically verified spectra. Report the maximum power-balance residual of the generator and its two-port unitarity check. Declare the search-grid resolution and retrieval candidate count; agreement within one grid spacing does not prove a continuous global optimum.

The starter's assertions check split separation, finite outputs, and the analytical conservation identity. Its reported errors measure performance on this chosen toy problem. There is no claimed accuracy threshold for a real device.

**Acceptance:** a fresh execution finishes without cell errors; physical assertions and split checks pass; tuning uses validation data only; warnings remain documented; every reported model uses the same test spectra; and inverse performance is measured using the generator as well as the surrogate. Optimizer warnings are not automatically disqualifying, but a warned fit must not be labeled converged.

**Interpret the reference run:** KRR has the lowest test complex RMSE. The selected MLP improves on nearest retrieval but does not beat linear interpolation. Its three initializations do not establish a confidence interval. Three stronger-regularization candidate fits report L-BFGS warnings; none is selected, and all three runs of the selected configuration finish without warnings. These outcomes are part of the teaching example, not results to hide or tune away using the test set.

## B. Replace the generator with a validated unit-cell library

**Status:** outline; no full-wave spectral dataset is supplied for this stage. For a smaller fixed-wavelength extension, reuse the saved [Chapter 3 ridge library](../notebooks/03-unit-cell-library.ipynb), split complete widths into training/validation/test sets, and preserve its TE polarization, geometry, phase references, and power normalization. That reuse is a surrogate experiment on existing full-wave data, not a new electromagnetic run. A frequency-spectral task requires an additional converged library.

**Prerequisites:** periodic boundary conditions, Floquet ports, S-parameter normalization, and a solver convergence study. Choose one geometry family and one material model before scaling up the dataset.

**Inputs and setup:** choose an available RCWA, finite-element, or FDTD solver; provide its version and runnable setup. Begin with one or two continuous geometry parameters, one polarization, and a documented band. Set the design objective's required accuracy before choosing mesh/harmonic and learning tolerances. A period that opens extra diffraction channels requires recording those channels, not assuming a two-port model.

### Procedure

1. Define the design bounds, units, period, substrate/superstrate, polarization, frequency band, and incidence conditions.
2. Converge representative cells in mesh size or harmonic order, including resonances and extreme geometries. Define a convergence tolerance justified by the design objective.
3. Save complex coefficients, channel identities, reference planes, and all-channel power balance. Record failures rather than silently removing difficult samples.
4. Split by geometry. Reserve a further interval or family for a clearly labeled extrapolation challenge.
5. Compare retrieval/interpolation, kernel regression, and a small neural network on exactly the same data split.
6. Sweep training-library size while keeping a common evaluation set. Record failures and solver costs as well as successfully retained samples. Fit every scaler using the corresponding training subset.
7. Re-simulate three predeclared held-out geometries with tighter numerical settings, including a resonant or boundary case. Compare the change in solver response with surrogate error; do not use these test outcomes to choose model settings.

### Dataset contract

| File or field | Minimum content |
| --- | --- |
| Manifest | Dataset version, solver/version, units, phasor convention, mode ordering, normalization, material source, reference planes |
| Geometry table | Stable geometry ID, parameter values and units, bounds, simulation status and failure reason |
| Response arrays | Complex coefficients, frequency/angle/polarization coordinates, and identified propagating channels |
| Split file | Explicit training/validation/test IDs; separate domain-shift challenge IDs if used |
| Convergence record | Representative cases, refinement settings, differences in the chosen observable, acceptance tolerance |
| Reproduction instructions | Environment, model-generation scripts, execution command, and location of archived raw outputs |

Use a portable array format that preserves complex values or documents separate real/imaginary arrays. Store small example data with the contribution; archive large files with a stable version. Never silently substitute zero for a failed solver result.

**Deliverables:** a versioned dataset manifest, solver setup, environment file, split IDs, learning curves, spectral error distributions, and three independently re-simulated test examples. Explain the difference between the solver's numerical uncertainty and the surrogate's prediction error.

**Acceptance:** the dataset can be regenerated or traced to archived solver outputs; the predeclared solver convergence criterion passes; test cases never determine model settings; and claimed accuracy is backed by per-device and aggregate metrics. If a criterion fails, report it and restrict the claim.

**Discussion:** if the apparent learning error is smaller than the solver's convergence difference, what accuracy can you actually claim? If prediction fails near a diffraction cutoff, would more data, a different representation, or a revised physical model address the cause?

## C. Inverse design under physical and fabrication constraints

**Status:** outline; follows Stage B.

Choose a target with explicit amplitude, phase, bandwidth, or polarization requirements. Start with a target from a known feasible library cell, then introduce a target whose feasibility is unknown.

**Inputs:** the frozen Stage B dataset and surrogate, design bounds, minimum-feature rules, a target spectrum or response specification, and an electromagnetic-call budget. Set one objective for all methods, for example frequency-weighted complex response mismatch plus a documented robustness penalty. State whether phase errors are meaningful across the entire target band.

### Procedure

Compare (i) the nearest response in the library, (ii) a bounded optimizer using the surrogate, and (iii) a conventional search with a matched electromagnetic-solver budget. An optional tandem network or conditional generative model is an extension after the baselines work.

For each method, report the same objective, constraints, allowed calls, and stopping rule. Verify several candidates with a converged solver. Test fabrication perturbations and evaluate whether a unit-cell approximation is adequate for the intended array; a complete-device claim requires a suitable device-level calculation.

1. Declare target cases, objective weights, success tolerance, constraints, and optimization budget before running the search.
2. Establish the best existing library response and record its actual geometry.
3. Run bounded surrogate search and a conventional solver-based search. Separate the shared data-generation cost from per-task search cost; report both total and amortized budgets.
4. Select a fixed number of candidates per method for converged re-simulation, including failures. Compute the same target objective from predictions and verified outputs.
5. Apply a documented fabrication perturbation distribution with stated units and correlations. Report nominal, average, and adverse-case performance separately. Sampled adverse cases are not a certified worst-case bound.
6. If the design is intended for a spatially varying array, assess coupling and finite-aperture effects using an appropriate supercell or device model before making an array-level claim.

**Deliverables:** target specification, candidate geometries, surrogate and verified responses, constraint checks, perturbation results, and a cost table including dataset generation. Explain failures and infeasible targets rather than selecting only successful examples.

**Acceptance:** no candidate violates a hard constraint; the same declared objective and budget accounting are used for all methods; every claimed successful design passes the predeclared tolerance in a converged verification calculation; and failed or unverified targets remain visible. A failed target can still produce a complete, useful lab report.

**Discussion:** did optimization expose an error that average test RMSE missed? Does a known-feasible target pass while an unknown target fails? What evidence would distinguish model error, optimizer failure, and physical infeasibility?

## D. Uncertainty and active learning

**Status:** outline; follows Stage B or C.

Under a fixed budget of new solver evaluations, compare random sampling with an explicitly defined acquisition rule. Possible signals include ensemble disagreement, distance from training data, or estimated improvement in the design objective.

**Inputs:** a common initial training library, an unlabeled candidate pool, a validation set for fixed model choices, a sealed test set, and a budget expressed in attempted solver calls. With a precomputed pool, hide labels until acquisition and count every label reveal as a call; label that experiment as a replay study rather than an online solver run.

### Procedure

1. Fix initial IDs, candidate-pool IDs, test IDs, model settings, batch size, number of rounds, and at least three random seeds before acquisition.
2. Use random acquisition as the baseline. As one concrete alternative, train an ensemble and choose designs with the largest mean spectral variance, $a(g)=M^{-1}\sum_j \operatorname{Var}_k[\widehat t_j^{(k)}(g)]$, where complex variance uses squared modulus about the ensemble mean. The ensemble must not access unqueried labels.
3. Acquire the same number of new simulations per round for each strategy. Log chosen IDs, acquisition scores, failures, and cumulative attempted calls. Specify how failures and already-selected points are handled before running the experiment.
4. Retrain using acquired labels and training-only preprocessing. Keep model-selection rules fixed. Save each round's model or evaluation predictions.
5. After the acquisition schedule is complete, reveal the fixed test labels and evaluate all saved rounds. Plot learning curves against cumulative electromagnetic calls across seeds; do not use those test curves to steer acquisition or tune the reported run.
6. Compare ensemble spread with observed held-out error and report overconfident failures. Test a separately declared shifted interval if useful. If claiming interval coverage, define how intervals were calibrated without using the final test set and measure their empirical coverage.
7. For a design-oriented extension, verify the final selected design with the converged solver and add its cost to the ledger.

**Deliverables:** acquisition history, data/version records, fixed-test learning curves, uncertainty-versus-error plots, and the final independently verified design. Explain when the extra modeling overhead is justified.

For a prediction-only study, the verified-design deliverable is optional and no inverse-design benefit should be claimed.

**Acceptance:** strategies begin from identical information for each paired seed; budgets include failed calls; no test feedback reaches the acquisition loop; repeated runs and uncertainty failures are reported; and any claimed saving compares matched verified accuracy or matched budgets. An ensemble's small spread is never accepted as a substitute for a solver check.

**Discussion:** does the acquisition rule spend all its budget at boundaries? Does uncertainty remain small where all ensemble members share the same bias? When does random sampling perform just as well?

## Suggested student contribution packages

| Package | A manageable contribution |
| --- | --- |
| Data and physics | One unit-cell family, convergence report, and documented sample data |
| Baselines | A reusable interpolation or kernel model with held-out evaluation |
| Neural model | Extend the supplied small-network comparison to a documented full-wave dataset |
| Design and robustness | A constrained inverse objective plus solver and tolerance checks |
| Teaching | Clear figures, worked derivations, and exercises connected to the notebook |

Use the [contribution guide](../contributing.md) and the lab template. Keep each pull request focused enough for a scientific review. These packages are suggestions; they do not assign work to named students.
