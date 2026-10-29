---
title: Prerequisite map and reading paths
short_title: Learning path
slug: learning-path
---

# Prerequisite map and reading paths

(path-core)=
## A route from fields to evidence

**1 → 2 → core of 4 → 3 → 5**, with **6 alongside the numerical work**, is the recommended first computational path. Chapter numbers describe subjects, not a compulsory teaching calendar.

| Step | Read and do | Ready to continue when you can… |
| --- | --- | --- |
| Foundations | [Chapter 1](chapters/01-metasurface-foundations.md) and its first investigation | Identify the modeled object, distinguish field amplitude from power, and state what is idealized |
| Electromagnetic tools | [Chapter 2](chapters/02-waves-and-interfaces.md) | Use the phasor/sign convention, choose an outgoing branch, normalize flux and name the phase reference planes |
| Allowed channels | [Chapter 4](chapters/04-periodic-floquet.md), especially Bloch phase, order selection, cutoff and power | Predict the open reflected/transmitted orders without interpreting an allowed direction as an efficiency |
| Geometry to response | [Chapter 3](chapters/03-unit-cell-design.md) | Check an interface/film, refine harmonics and distinguish total power from a target order's power |
| Numerical evidence | [Chapter 6](chapters/06-numerical-methods.md), alongside 3 and 5 | Separate residual, conservation, observable convergence, reference-plane errors and model discrepancy |
| Design and verify | [Chapter 5](chapters/05-metasurface-synthesis.md) | Select feasible cells, test the complete periodic supercell and label scalar focusing/Jones approximations |

(path-branches)=
## Choose an application branch

| Destination | Preparation | Useful next investigation |
| --- | --- | --- |
| [7 — Tuning and control](chapters/07-active-tunable.md) | 2's sheet/circuit response; 5's prescribed arrays; 6's validation habits | Reachable complex states, bias control and temporal-envelope limits |
| [8 — Communication links](chapters/08-communications.md) | 2's power/coherence; 5's finite aperture; 6's error checks; 7 for programmable hardware context | Geometry, coherent path sums, bandwidth and training overhead |
| [9 — Materials and measurement](chapters/09-materials-measurement.md) | 2's complex scattering and reference planes; 3's geometry; 6's error categories | Calibration, correlated fabrication error and synthetic uncertainty |
| [10 — AI and metasurfaces](chapters/10-ai-metasurfaces.md) | 1–2 for the analytical starter; 3/5/6 before a geometry-based full-wave extension | Split data by design, compare simple baselines and independently test proposed candidates |

Basic Python arrays/plots, complex arithmetic, linear algebra, derivatives and probability are useful prerequisites. Revisit them when a lab first uses them; no commercial solver is required for the executed core.

(path-cross-labs)=
## Cross-chapter laboratories and capstone

Follow [ms-09 bandwidth](labs/09-dispersion-lab.md) after 2/5, [ms-10 coupling](labs/10-coupling-lab.md) after 3/6, and [ms-11 bounded design](labs/11-inverse-design-lab.md) after 5/6 with 10's held-out-validation discipline. The three notebooks are separate investigations and share a source bundle.

Finish with [ms-12: the reproducible research project](labs/12-research-project.md). Select one bounded question with an affordable baseline and explicit evidence. Experimental/device-scale extensions need a separately approved scope and access plan.

For each investigation: **predict → run → check → explain the limits**. Use [setup and measured runtimes](getting-started.md) to plan computation, and [the glossary and conventions](glossary.md) when changing chapters.
