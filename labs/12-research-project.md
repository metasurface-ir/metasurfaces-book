---
title: ms-12 — Reproducible metasurface research project
short_title: ms-12 · Research project
slug: research-project
---

# ms-12 — Reproducible metasurface research project

(project-question)=
## One question, one defensible claim

Investigate one measurable question using a declared model and an affordable baseline. Your contribution is the evidence connecting assumptions to a conclusion, including a negative result. A high efficiency, an attractive image, or a low machine-learning error alone is not the project.

Choose a feasible route: a bounded TE-library/supercell comparison (3/5/6), tuning and reachability in an assigned circuit (7), a scalar link tradeoff (8), synthetic calibration/uncertainty (9), or a held-out surrogate comparison (10). These are starting points, not claims of new experimental or unrestricted 3D capability. Use [the prerequisite map](../learning-path.md) and the existing notebooks before proposing a new solver.

(project-proposal)=
## Proposal template

Submit a short proposal before launching a large sweep. Copy this structure into your own Markdown file:

```text
Title and contributors:
Question and falsifiable hypothesis:
Physical object/geometry and observed quantity (with units):
Model, assumptions, excluded effects, sign and phase-plane conventions:
Baseline and why it is a fair comparison:
Editable parameters, bounds, data split and random seeds:
Analytical limit and planned convergence/independent checks:
Compute budget: solver calls, mesh/harmonics, memory, wall time:
Stopping rule and fallback if the planned run exceeds the budget:
Data/image sources, versions, reuse terms and credit:
Deliverables, paired-language plan and division of work:
```

Distinguish design variables from numerical-resolution controls. Declare the metric and acceptance threshold before inspecting the final candidates. In a learning project, freeze held-out data before model selection; in an optimization project, count failed and verification calls as part of the total cost.

(project-milestones)=
## Milestones with evidence gates

| Milestone | Evidence to bring to review | Continue when… |
| --- | --- | --- |
| 1. Scope and baseline | Proposal, labeled geometry, reproducible baseline and cost of a small pilot | Units, conventions, inputs and success/failure criteria are unambiguous |
| 2. Trust the calculation | Analytical/limiting check, residual/power checks where applicable, and at least two justified refinements | The reported observable is stable to the declared tolerance, or its unresolved error is explicit |
| 3. Run the investigation | Bounded parameter/design trials with all histories, seeds and failed cases retained | The comparison holds relevant physics, budgets and normalization fixed |
| 4. Challenge the conclusion | Independent implementation/method, held-out cases, or a separately justified cross-check; uncertainty/sensitivity study | Evidence supports the claim within its stated model and domain |
| 5. Reproduce and communicate | Fresh-kernel run, data/environment record, source/translation, figures and concise report | Another student can follow the instructions and explain both the finding and its limits |

Dates, assessment weights, team size, and access to specialist software are instructor decisions. A failed milestone can motivate a smaller question; document that decision and retain the earlier results.

(project-budget)=
## Computational budget and stopping rules

Time a small representative calculation before allocating the full sweep. Estimate total wall time as cost per call × calls, then include refinement, validation, failed searches and plotting. Record memory use when increasing grid or harmonic count. For surrogate work, include training-data generation and independent candidate verification in the comparison budget.

Choose explicit limits for evaluations, mesh/harmonic size and wall time in the proposal. Stop when a limit is reached or the model's validity domain is violated. Save the current candidate, history, residuals, convergence flags and stopping reason. Reduce the scope or seek an instructor decision before increasing an agreed budget; do not silently discard an unsuccessful run.

(project-rubric)=
## Evidence rubric

| Criterion | Convincing evidence | Needs revision |
| --- | --- | --- |
| Physical question and model | Geometry, assumptions, observable, units, reference planes and scope agree | The plotted result has no clear object or uses an unsupported physical interpretation |
| Baseline and comparison | Comparable inputs, normalization, resolution, data splits and total compute accounting | A gain comes from a changed budget, normalization or test leakage |
| Numerical reliability | Relevant limits, refinement of the actual observable and independent checks with tolerances | Only residual/power conservation, a single resolution, or a single favorable case |
| Uncertainty and failure | Correlations/assumptions stated; failed trials and uncertainty limits retained | Only best runs; an uncertainty region or error bar has no declared meaning |
| Reproducibility and communication | Fresh-kernel execution, accessible inputs, environment, paired narrative, source-linked figures and clear limitations | Missing dependencies/data, stale outputs, unsupported citations or unexplained figures |

The instructor assigns weights. The rubric assesses evidence, not whether a design happened to outperform its baseline.

(project-deliverables)=
## Reproducibility deliverables

Deliver the proposal and final claim; editable notebook/code with parameters; immutable raw inputs plus generated result tables; environment and source commit; geometry and figure generators; audit/refinement results; all search histories and seeds; source/permission records; and a short report with limitations and one next experiment. Separate synthetic data from measured data. Preserve large datasets in a versioned archive with a stable identifier and retrieval instructions.

Add English/Persian narrative using [the contribution workflow](../contributing.md), shared scientific code, and a clear execution order. In the report state what you actually ran, what remained an outline, and what would change your conclusion. Submit by PR or an instructor handoff folder. Acceptance and publication follow scientific review, the bilingual build and a successful deployment.
