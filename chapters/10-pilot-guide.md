---
title: 'Chapter 10 pilot: learning path and worked exercises'
short_title: Pilot guide and exercises
---

# Chapter 10 pilot: learning path and worked exercises

Use this page to work through the complete introductory pilot and decide when you are ready to extend it. The pilot combines graduate-level problem formulation with a deliberately small calculation whose assumptions and errors can be inspected.

## The learning path

| Step | Activity | Evidence you should produce |
| --- | --- | --- |
| 1. Predict | Read Chapter 10 Sections 10.1-10.4; derive the resonant-sheet limits | A forward/inverse problem statement and a geometry-level split diagram |
| 2. Learn a baseline | Run the [starter notebook](../notebooks/10-resonant-surrogate.ipynb) | Generator checks, validation choice, held-out errors, and verified inverse proposal |
| 3. Compare models | Read Section 10.5 and run the [neural comparison](../notebooks/10-neural-comparison.ipynb) | Four-method comparison, three neural initializations, phase masking, and power diagnostics |
| 4. Challenge the result | Read Sections 10.6-10.9 and work the examples below | Explanation of inverse ambiguity, optimization risk, and the limits of the evidence |
| 5. Report | Complete [Lab A](../labs/13-ai-metasurfaces.md) | A reproducible notebook and a short scientific interpretation |
| 6. Plan a device study | Review Lab B-D outlines | A proposed full-wave dataset, constraints, validation protocol, and solver budget |

**Suggested teaching use:** one session for the physical model, splitting, and kernel notebook; a second for neural comparison and inverse verification. Assign reading and the written interpretation between or after sessions. This is a planning suggestion, not a fixed course timetable.

Chapter 10 is the first chapter we have developed as a complete publishing and teaching example. Students still need the electromagnetic foundations. Before full-wave Lab B, complete the relevant material from Chapters 2, 3, 4, and 6. Before fabrication-aware Lab C, connect Chapters 5 and 9. Developing the book in this order does not change the eventual prerequisite order for learning it.

## Before opening Python

Try these four predictions:

1. At resonance, will the synthetic sheet transmit or reflect? What happens to transmission phase there?
2. If a retrieved spectrum conserves power perfectly, does it necessarily predict the requested geometry accurately?
3. Will a more flexible network necessarily beat interpolation with 40 smooth, one-dimensional training examples?
4. Can an optimizer find a model's errors more effectively than a random test set does?

Return to your answers after inspecting the actual numerical tables. The value of the pilot is the reasoning that connects a calculation to its claim.

## Worked example 1: conservation and resonance

Starting from $r=-\gamma/(\gamma-i\Delta)$ and $t=-i\Delta/(\gamma-i\Delta)$,

$$
|r|^2+|t|^2=\frac{\gamma^2+\Delta^2}{\gamma^2+\Delta^2}=1.
$$

At $\Delta=0$, $r=-1$ and $t=0$: total reflection with a phase reversal. At $|\Delta|=\gamma$, both power fractions are $1/2$. As $|\Delta|/\gamma$ grows, $r\to0$ and $t\to1$.

For the complete symmetric two-port matrix, also check $r^*t+t^*r=0$. The product $r^*t=i\gamma\Delta/(\gamma^2+\Delta^2)$ has zero real part, so the off-diagonal terms vanish. This verifies unitarity for the analytical model. It does not prove that an arbitrary learned output obeys it.

**Interpretation:** transmission phase is undefined at its exact zero. A numerical phase reported there is not a usable physical target. Phase metrics must state an amplitude threshold and the excluded fraction.

## Worked example 2: the phase branch cut

Let $t=e^{i179^\circ}$ and $\widehat t=e^{-i179^\circ}$. Ordinary subtraction gives $-358^\circ$. The circular difference is

$$
\arg(\widehat t t^*)=2^\circ.
$$

The complex-amplitude error is

$$
|\widehat t-t|=2\sin(1^\circ)\approx0.03490.
$$

Both amplitudes are one, so the example is well away from a transmission zero. A regression target that stores real and imaginary parts has no discontinuity at this branch cut. It still needs enough data to learn the response.

**Try next:** reduce one amplitude to $0.01$ while keeping its phase. Explain why a small circular phase error would now hide a large amplitude error.

## Worked example 3: what counts as an unseen example?

Suppose 80 geometries each contribute 101 frequencies. Randomly splitting all 8080 frequency rows can put the same geometry in every set. A test frequency near a training frequency may then be easy to predict without learning how an unseen geometry behaves.

For a new-geometry claim, shuffle the 80 geometry IDs and allocate 40 complete spectra to training, 20 to validation, and 20 to testing. Fit normalization on the 40 training geometries; choose model settings using validation error; report test results after choices are frozen. The model can still interpolate within the geometric range, so call this a held-out geometry test, not evidence for arbitrary shapes or materials.

A harder, distinct experiment can reserve a contiguous interval of $g$. An interior withheld interval tests interpolation across a gap; a withheld interval beyond the training range tests extrapolation. Specify the interval and the remaining training/validation rules in advance. Keep all results from that experiment separate from the pilot's reference split.

**Interpretation:** split design is part of the scientific question, not merely a data-processing convenience.

## Worked example 4: inverse ambiguity and surrogate error

For $y=x^2$, both $x=-1$ and $x=1$ produce $y=1$. A deterministic inverse predictor trained with squared design error on equally common labels minimizes

$$
\tfrac12[(\widehat x-1)^2+(\widehat x+1)^2]=\widehat x^2+1
$$

at $\widehat x=0$. Yet its forward response is zero. Averaging valid inverse solutions can produce an invalid solution.

A tandem model instead penalizes a proposed design's response through a fixed forward surrogate. This avoids directly averaging conflicting labels, but it introduces another question: is the surrogate correct at the proposed design? If it predicts $\widehat F(x)=1$ while the actual response is $F(x)=0.6$, a zero surrogate loss still leaves a response error of $0.4$.

**Verification procedure:** enforce design bounds, retain several candidate designs, evaluate each with the original physical model, and compare the same objective before and after verification. For a full-wave claim, establish convergence and check the relevant output channels. Adding new training examples does not justify reusing a previously inspected test set for model selection.

## Worked example 5: when does the training library pay for itself?

Use a hypothetical cost model, with all times measured in seconds:

| Cost | Assumption |
| --- | --- |
| Initial library | 2000 solver calls at 30 s each: 60000 s |
| Training | 600 s |
| Conventional design task | 200 solver calls: 6000 s per task |
| Surrogate search per task | 60 s |
| Independent verification per task | 5 solver calls: 150 s |

For $Q$ repeated tasks using the same valid library, the surrogate workflow costs $60600+210Q$, whereas conventional search costs $6000Q$. The former is cheaper when

$$
Q>\frac{60600}{6000-210}\approx10.47.
$$

Under these assumptions, the first integer break-even is **11 tasks**. These are invented teaching costs, not timings from the notebook. If materials change, the target lies outside the library's domain, or retraining is required, the calculation changes. Failed simulations and additional verification belong in the cost ledger. Equal time budgets also do not guarantee equal solution quality: compare verified target performance.

## Pilot report and review criteria

Submit the two notebooks with saved outputs and a short interpretation, or one combined report that links to both. A reviewer should be able to locate:

- **Physical meaning:** convention, normalization, synthetic design mapping, resonance and conservation checks.
- **Reproducibility:** package versions, editable parameters, all split IDs, validation candidates, chosen settings, and optimizer status.
- **Comparison:** identical held-out geometries, simple baselines, all neural seeds, complex/power/phase errors, and the phase exclusion fraction.
- **Inverse evidence:** the objective, bounds, grid spacing or library candidate count, proposed coordinates, and predicted versus verified errors.
- **Interpretation:** at least one limitation that the numerical results cannot resolve, and a specific full-wave experiment that would address it.

A high-quality report can conclude that a neural network was unnecessary for this small task. A model ranking without split information or verification is incomplete. A convergence warning should be explained, not removed from the saved record.

## What is complete, and what comes next?

The Chapter 10 **introductory pilot** comprises the chapter, these worked exercises, both executed analytical notebooks, and the four detailed lab outlines. Full-wave dataset generation, fabricated-device validation, tandem/generative implementations, and active-learning experiments are future work described in Labs B-D.

The next authoring step is the foundational wave/Floquet and numerical-validation material that those labs need. The [syllabus](../syllabus.md) keeps the ten-chapter course map visible while the chapters are developed.
