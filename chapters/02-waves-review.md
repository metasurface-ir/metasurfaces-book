---
title: 'Chapter 2: Self-check and Wave Detective Project'
short_title: Wave detective self-check
---

# Chapter 2: Self-check and Wave Detective Project

Attempt these questions after the [chapter](02-waves-and-interfaces.md), then open the answers. The [worked examples](02-waves-guide.md) show the intermediate calculations; the [lab](../labs/02-waves-lab.md) supplies the browser, notebook, source bundle, and audit. Keep a prediction log: a prediction that fails for a clear reason is useful evidence of learning.

## Q1: Which way is the power?

A wave in air has $\widetilde{\mathbf E}=E_0\widehat{\mathbf y}e^{ik_0z}$ with time dependence $e^{-i\omega t}$. Which direction must its magnetic field point? What happens when you reverse the propagation direction while keeping electric polarization along $y$?

:::{dropdown} Answer
For positive-$z$ propagation, $\mathbf H=(\widehat{\mathbf z}\times\mathbf E)/\eta_0$ points along negative $x$. Then $\operatorname{Re}(\mathbf E\times\mathbf H^*)$ points along positive $z$. Reversing propagation reverses the magnetic relation. Keeping its sign unchanged would give a wrong flux direction and a wrong reflection boundary equation.
:::

## Q2: Is a large field evidence of gain?

An interface from $n_i=1.5$ to $n_t=1$ gives $r=0.2$ and $t=1.2$. A report calls $|t|^2=1.44$ its transmitted power fraction and declares gain. Diagnose the report and give the correct power balance.

:::{dropdown} Answer
The report omitted the admittance factor. At normal incidence in these real nonmagnetic media, $T=(n_t/n_i)|t|^2=0.96$ and $R=0.04$. Their sum is one. Electric-field coefficients and power-normalized S parameters are different quantities; a field amplitude exceeding one does not establish amplification.
:::

## Q3: What rotates in a Jones vector?

For $(E_x,E_y)^T=(1,i)^T/\sqrt2$ at $z=0$, describe the electric-field trajectory under our time convention. What fraction passes an ideal linear analyzer? Would multiplying the entire Jones vector by one global phase change its polarization ellipse?

:::{dropdown} Answer
The real components are proportional to $(\cos\omega t,\sin\omega t)$, so the tip moves from positive $E_x$ toward positive $E_y$. A linear analyzer transmits $1/2$ at every orientation. A global phase shifts the timing of the same trajectory and does not change the polarization ellipse; relative component phase can change it. A handedness name needs an explicit viewing convention. A single Jones vector does not describe unpolarized light.
:::

## Q4: Why is there a minus sign?

Derive the two scalar continuity equations for a bare interface using incident tangential electric amplitude one. Why does the magnetic equation contain $1-r$? Which polarization becomes reflectionless at the air-to-glass Brewster angle?

:::{dropdown} Answer
Tangential electric continuity gives $1+r=t$. The backward wave has the opposite signed magnetic-to-electric relation, giving $Y_i(1-r)=Y_t t$. Solving yields $r=(Y_i-Y_t)/(Y_i+Y_t)$ and $t=2Y_i/(Y_i+Y_t)$. At $\theta_B=\arctan(1.5)\approx56.31^\circ$, the TM admittances match and TM reflection vanishes. TE reflection generally remains. All coefficients here use the same tangential electric axis; a rotating reflected-$p$ basis can change an amplitude sign.
:::

## Q5: Where is the transmitted field?

Above the glass-to-air critical angle, the transmitted normal power is zero. Does the field vanish everywhere in air? What distinguishes an amplitude decay length from an intensity decay length? What caution applies at exact TM cutoff?

:::{dropdown} Answer
The transmitted field can be nonzero and decay as $e^{-\kappa z}$, while $\operatorname{Re}Y_t=0$ gives zero net transmitted normal flux. Its amplitude $1/e$ length is $1/\kappa$ and its intensity $1/e$ length is $1/(2\kappa)$. At exact cutoff, the TM admittance expression is singular: use limits. Vanishing tangential $E_x$ coefficient does not by itself imply that the complete transmitted vector field vanishes.
:::

## Q6: Why can an extra layer help?

An ideal normal-incidence antireflection layer joins $n_0=1$ to $n_2=1.5$. Find its quarter-wave index/thickness at $\lambda_d=0.6\,\mu\mathrm m$. If its reflectance is zero, must the transmission coefficient be 1 with zero phase?

:::{dropdown} Answer
Choose $n_f=\sqrt{1.5}\approx1.224745$ and $d=\lambda_d/(4n_f)\approx0.122474\,\mu\mathrm m$. The two reflected contributions cancel at the design condition. With entrance and exit phase references, the electric coefficient is $t=i\sqrt{1/1.5}\approx0.816497i$, giving $T=1$. Its field amplitude and phase are not fixed by the statement $R=0$ alone. The perfect cancellation belongs to the stated wavelength, angle, indices, and coherence model.
:::

## Q7: Is this a valid sheet retrieval?

Empty air is described by $r=0,t=1$ at one common plane. Moving only the output reference downstream by $\lambda_0/4$ gives $t=i$. A retrieval $g=2(1-t)/t$ then returns negative conductance. What should you check before declaring an active material? How does fixed absolute amplitude uncertainty affect retrieval near $t=0$?

:::{dropdown} Answer
The formula assumes coincident reference planes and an equal-air local electric shunt. The shifted data fail $t=1+r$: $i\ne1$. Remove the known propagation phase before testing the model. The negative conductance is an interpretation error here. The derivative $dg/dt=-2/t^2$ means a fixed absolute field uncertainty can produce a large absolute parameter uncertainty near zero transmission; at zero the inverse is undefined. Deembedding and one fitted value do not establish a general local sheet model for a finite film or patterned structure.
:::

## Q8: Does phase change dissipation?

A purely electric equal-air sheet has $g=2$, $r=-1/2$, and $t=1/2$. What is its one-sided absorption? What is absorbed for equal coherent counterpropagating beams of total unit input power and relative phase $0$, $90^\circ$, or $180^\circ$? Does this contradict the one-sided absorption bound?

:::{dropdown} Answer
One-sided absorption is $1-R-T=1/2$. With $\mathbf a=(1,e^{i\phi})^T/\sqrt2$, the two-sided fraction is $(1+\cos\phi)/2$, giving 1, $1/2$, and 0 at those phases. The input state has changed, so the original one-sided bound is not contradicted. The incoming fields must be coherent and must have the stated mode and phase relation. Sum their outgoing complex amplitudes before calculating powers. The result is an analytical prediction, not a claim about an implemented absorber.
:::

## The wave detective project

**Task:** prepare an evidence report resolving the chapter's three puzzles: a transmitted amplitude above one, a field with no outgoing normal-power channel, and phase-controlled absorption by an unchanged sheet.

1. **Predict:** sketch the incident/outgoing fields and state your predicted amplitudes, powers, or limits before evaluating them.
2. **Reproduce:** run the analytical notebook from a fresh kernel. Retain its environment, parameter values, source version, and audit.
3. **Challenge:** change one quantity at a time: exterior index/angle, film optical thickness, Jones relative phase, and sheet conductance or illumination phase. Include one case where the initial prediction fails.
4. **Diagnose:** deliberately test one wrong normalization, reference-plane interpretation, or growing evanescent branch on paper. Explain which physical or consistency check exposes the error; preserve the valid model in your submitted computational source.
5. **Connect:** inspect one saved response in the [Chapter 3 library](../notebooks/03-unit-cell-library.ipynb). State its geometry, polarization, indices, wavelength, phase planes, power denominator, and open channels. Explain what the present uniform-interface or local-sheet models do not represent.
6. **Propose:** write one independent test that would be needed for a specific physical sample. Identify calibration and uncertainty if you propose a measurement.

Submit the executed notebook, at least one parameter record from the browser, the generated figures, a compact prediction/result table, audit output, and a report of about 3–4 pages. Include a failed prediction and its correction. Mark proposed or unexecuted work clearly. Students can share editable Markdown/notebooks through the existing [contribution workflow](../contributing.md).

## Suggested rubric

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Problem definition | 15 | Illumination, media, basis, time convention, and reference planes |
| Derivation and physical reasoning | 20 | Correct Maxwell/boundary signs and interpretation |
| Predictions and figures | 20 | Meaningful changes of parameters; readable axes, units, and captions |
| Verification and model limits | 20 | Limiting cases, residuals, rejected assumptions, and a justified next test |
| Power and coherence | 15 | Correct admittance factors, input denominator, and complex-field superposition |
| Reproducibility and attribution | 10 | Executed source, environment/data, references, and collaboration/AI assistance |

This rubric is a proposed teaching aid for instructor adaptation. A well-explained negative result or rejected model can earn full scientific credit; an attractive figure without the correct denominator cannot replace the reasoning.

## A working glossary

| Term | Meaning used here |
| --- | --- |
| Phasor | Complex peak amplitude with a stated harmonic time convention |
| Wave impedance | Electric-to-magnetic field ratio for the specified propagating plane wave |
| Tangential admittance | Signed magnetic-to-tangential-electric ratio; dimensionless $Y$ here is scaled by $\eta_0$ |
| TE / TM | Electric / magnetic field transverse to the plane of incidence |
| Jones vector | Two coherent complex transverse electric components in a stated basis |
| Evanescent wave | Field decaying into a region through imaginary longitudinal wavevector |
| Cutoff | Boundary between longitudinal propagation and decay, requiring separate limiting treatment |
| Reference plane | Spatial plane at which an amplitude and its phase are defined |
| Deembedding | Removing known propagation or fixture effects to change the response reference |
| Power-normalized S parameter | Coefficient between amplitudes whose squared norms represent port power |
| Sheet admittance | Local surface-current response per tangential electric field, in siemens |
| Coherence | A sufficiently stable phase relation for the relevant field cross terms to be retained |

Continue to [Chapter 3](03-unit-cell-design.md) for geometry-dependent amplitudes, [Chapter 4](04-periodic-floquet.md) for outgoing diffraction channels, or repeat a doubtful result in the [lab](../labs/02-waves-lab.md) before proceeding.
