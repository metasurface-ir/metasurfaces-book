---
title: 'Chapter 1: Self-check and Mini-project'
short_title: Review and mini-project
---

# Chapter 1: Self-check and Mini-project

Use this page after the [chapter](01-metasurface-foundations.md), [worked examples](01-foundations-guide.md), and [lab](../labs/01-first-investigation.md). Attempt each question before opening its answer. The report worksheet, {download}`../downloads/chapter-01-report-template.md`, is editable Markdown; it is also included in the lab's source ZIP.

## Q1: Which wavelength?

At 200 THz, compare a 0.8 μm dimension with the wavelength in vacuum and in a real-index medium with $n=1.5$. Does calling it subwavelength establish homogenization?

:::{dropdown} Answer
The wavelengths are approximately 1.499 μm and 0.999 μm, respectively. The ratios are about 0.534 and 0.801. Name the medium and dimension. These ratios alone establish neither a useful homogeneous sheet nor independent-cell behavior: illumination, period, coupling, resonance, and the observable still matter.
:::

## Q2: Pitch or period?

Six sites have pitch 0.65 μm. Compare a repeated six-element sequence with six different elements and a sequence of six identical elements.

:::{dropdown} Answer
For a sequence with no smaller repeating motif, the period is 3.90 μm. Identical elements preserve the 0.65 μm primitive period. A larger computational supercell can still label additional diffraction orders, but its allowed labels do not imply nonzero amplitudes. Aperture means the finite extent, rather than either period.
:::

## Q3: Same power, same field?

Compare $t=1$, $t=-1$, $t=0.8i$, and $t=0$ in the introductory equal-impedance model. Also compare phases of $179^\circ$ and $-179^\circ$.

:::{dropdown} Answer
The transmitted powers are 1, 1, 0.64, and 0. The first two fields have a relative phase of 180° at the same reference plane, despite identical power. The third has phase 90°. The zero field has no transmission phase. The circular separation of 179° and −179° is 2°, so a direct linear subtraction is misleading.
:::

## Q4: Predict the presets

At 200 THz, predict the transparent, electric-only, and balanced resonance coefficients before opening the explorer. What does detuning change?

:::{dropdown} Answer
Transparent: $(r,t)=(0,1)$. Electric-only: $(r,t)=(-1,0)$, with undefined transmission phase. Balanced: $(r,t)=(0,-1)$. Detuning generally breaks reflected cancellation and redistributes power between the two available outgoing ports. It does not introduce absorption into this lossless model. The channel coordinates are not extracted dipole moments or fabrication dimensions.
:::

## Q5: Is power balance enough?

A proposed reciprocal symmetric matrix has $r=t=1/\sqrt2$. It passes $R+T=1$ for one-sided illumination. Is it a lossless two-port model for every input?

:::{dropdown} Answer
No. Here

$$
S^\dagger S=\begin{bmatrix}1&1\\1&1\end{bmatrix}\ne I.
$$

For normalized even illumination $a=(1,1)^T/\sqrt2$, the input power is 1, but the output power is 2. For odd illumination the output vanishes. The columns must also be orthogonal: $r^*t+t^*r=0$. For the introductory model, the even/odd eigenvalues $C_e,-C_m$ have unit magnitude, establishing this stronger requirement.
:::

## Q6: Amplitude or power?

The saved Chapter 3 ridge has equal magnetic permeability on either side, normal incidence, $n_i=1$, and $n_t=1.5$. If its electric-field coefficient has $|t|^2\approx0.640$, can that number be called the transmitted power fraction?

:::{dropdown} Answer
The incident-normalized transmitted power is $T=(n_t/n_i)|t|^2\approx0.960$. For a normally incident propagating plane wave in a real nonmagnetic medium, the power flux is proportional to $n|E|^2$. This formula is restricted to the stated conditions; Chapter 2 develops more general admittance and angle factors. The worked guide shows this calculation using a saved Chapter 3 complex full-wave coefficient, without rerunning its solver or fitting the introductory sheet.
:::

## Q7: What is missing power?

A measurement collects 70% of incident power in one transmitted order. Can the other 30% be called absorption? What is missing from a phase-only design claim?

:::{dropdown} Answer
First account for reflection, other diffraction orders, polarization channels, finite collection angles, calibration, and uncertainty. Their powers need not be zero. A phase-only claim also needs amplitude/power, reference planes, illumination, normalization, geometry/material assumptions, and evidence appropriate to its claimed performance.
:::

## Q8: Does tunable imply gain?

Does external electrical control make a surface an electromagnetic amplifier or a nonreciprocal device? Does training an AI model verify either property?

:::{dropdown} Answer
Tuning changes the operating state. It does not by itself establish electromagnetic gain or nonreciprocity. Check the scattering response and energy exchange under the actual bias or time modulation. An AI prediction needs separate electromagnetic and, where claimed, experimental verification. Chapter 7 will distinguish tuning mechanisms and Chapter 10 addresses verification of learned models.
:::

## A small design investigation

**Question:** which changes preserve reflected cancellation, and which destroy it?

1. Predict the response for the four browser presets before calculating.
2. Starting from the balanced pair, change only magnetic-like strength; then restore it and change only magnetic-like resonance. Retain each parameter set.
3. Inspect at least four illumination frequencies, including and excluding resonance. State a hypothesis before each sweep and retain power beside phase.
4. Use a complex two-sided input in the notebook and verify input/output power. Explain why Q5's counterexample fails.
5. Inspect the saved full-wave row in the worked guide and recalculate its transmitted power by hand or in a short code cell. Explain the unequal-index power factor, reference-plane difference, and why no channel-strength-to-width mapping follows.
6. State one additional test needed to answer a question about a physical device. Separate a proposed test from an executed result.

Submit the executed notebook, parameter/response records, three generated figures, saved-row comparison, audit output, and a short report. A concise report of about 2–3 pages is enough if it retains the evidence. Use the worksheet download above and the [contribution workflow](../contributing.md).

## Assessment rubric

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Experiment definition | 15 | Illumination, parameters, ports, conventions, and prediction |
| Correct response reasoning | 20 | Complex coefficients, meaningful phase, and four limits |
| Reproducibility | 20 | Executed notebook, environment/source versions, data, and audit |
| Physical consistency | 20 | One-/two-sided power, unitarity, and correct full-wave flux normalization |
| Interpretation and limits | 15 | Distinction between analytical and geometry evidence; justified next test |
| Communication | 10 | Readable figures, units, captions, references, and contribution attribution |

This is a suggested teaching rubric for instructor adaptation. A well-supported negative result or unmet target is valid scientific work.

## Working glossary

| Term | Meaning in this course |
| --- | --- |
| Meta-atom | Engineered building block, rather than a literal atom |
| Pitch | Spacing between adjacent element sites |
| Primitive period | Smallest translation restoring the complete material pattern |
| Supercell | Repeated or computational group of multiple sites |
| Aperture | Finite fabricated or illuminated extent |
| Phasor | Complex amplitude with a stated time convention |
| Reference plane | Position at which a coefficient's field phase is defined |
| Channel | Specified direction/order, polarization, and port state |
| Local approximation | Response assigned from a repeated-cell environment |
| Reciprocity | Symmetry between appropriately exchanged source/receiver channels under its physical conditions |
| Unitarity | Power preservation for every incoming combination in a complete power-normalized lossless scattering model |
| Verification | Evidence checking equations, computation, or a claimed prediction within a stated scope |

Return to the [lab](../labs/01-first-investigation.md) to reproduce results. Chapter 2 will develop boundary conditions and normalization; detailed material retrieval and measurements belong to their later investigations.
