---
title: 'Chapter 1: Worked Examples and Learning Path'
short_title: Foundations worked examples
---

# Chapter 1: Worked Examples and Learning Path

**Question:** what can you predict before opening an electromagnetic solver?

Read [Chapter 1](01-metasurface-foundations.md), make predictions in the [browser lab](../labs/01-first-investigation.md), and then inspect or run the [notebook](../notebooks/01-first-metasurface-model.ipynb). The notebook and browser calculate an ideal sheet response; neither assigns a physical geometry.

## Learning path

| Stage | Activity | Evidence to retain |
| --- | --- | --- |
| 1 | Draw the structure and illumination | Element, pitch, period, aperture, and reference planes |
| 2 | Interpret complex coefficients | Amplitude, phase, and appropriate power normalization |
| 3 | Predict four sheet limits | A written prediction before using each preset |
| 4 | Change detuning and strength | Complex response and conservation checks |
| 5 | Examine frequency dependence | Phase plus amplitude, and a stated spectral metric |
| 6 | Compare evidence levels | An analytical claim, a full-wave claim, and their limits |

For a handmade demonstration, draw two complex arrows on movable cards. Arrange them head-to-tail to make zero, then align them to make a nonzero sum. Relate the construction to the model's reflected and transmitted channel combinations. The cards illustrate complex addition; they do not measure the radiated fields of a physical meta-atom.

## Example 1: wavelength in the relevant medium

At $200\,\mathrm{THz}$,

$$
\lambda_0=\frac{299.792458}{200}\,\mu\mathrm m\approx1.499\,\mu\mathrm m.
$$

In a real-index medium with $n=1.5$, the wavelength is approximately $0.999\,\mu\mathrm m$. A dimension of $0.8\,\mu\mathrm m$ is therefore about $0.53\lambda_0$ but $0.80\lambda$ in that medium. Always name the wavelength used in a “subwavelength” statement.

This conversion does not provide a homogenization theorem. Period, illumination, resonance, coupling, and the observable still determine whether an effective description is useful.

## Example 2: the same power can have a different phase

For equal exterior impedances at normal incidence, $t=1$ and $t=-1$ both give $T=1$. Their phases differ by $180^\circ$ at the same reference plane. Interfering either field with a fixed reference can distinguish them.

The coefficient $t=0.8i$ gives $T=0.64$ and phase $90^\circ$ in the same normalization. At $t=0$, transmitted power is zero and phase is undefined. Reporting a phase there cannot establish a useful transmitted-wave design.

**Prediction:** if a solver reports only transmitted intensity, can it distinguish the first two coefficients? The intensity alone does not retain that relative phase.

## Example 3: an electric-like resonance

At $f=f_e$ and nonzero electric-like strength, $C_e=-1$. With the magnetic-like channel disabled, $C_m=1$, so

$$
r=\frac{-1-1}{2}=-1,\qquad t=\frac{-1+1}{2}=0.
$$

The ideal sheet reflects all incident power. Its reflected field has a sign change, while its transmitted phase is undefined. The notebook stores the missing phase as null/blank rather than treating it as a physical zero-degree phase.

## Example 4: a balanced pair at resonance

Now match the two channels, so $C_e=C_m=-1$:

$$
r=0,\qquad t=-1,\qquad R=0,\qquad T=1.
$$

The two reflected contributions cancel, and the transmitted coefficient retains a $180^\circ$ phase relative to the transparent reference. The model can therefore illustrate unit transmission with nonzero phase. It does not identify a ridge width, material, or fabricated sample that achieves the response.

Change the magnetic-like resonance to $230\,\mathrm{THz}$ while keeping illumination at $200\,\mathrm{THz}$. Predict whether cancellation remains, then inspect the detuned preset. The model remains lossless, so the response redistributes power between its two ports.

## Example 5: two-sided illumination is a stronger check

For $S=\begin{bmatrix}r&t\\t&r\end{bmatrix}$, take the normalized even input $(1,1)^T/\sqrt2$. Its output is multiplied by $r+t=C_e$. The odd input $(1,-1)^T/\sqrt2$ is multiplied by $r-t=-C_m$.

Both eigenvalues have unit magnitude. Thus this model preserves power for arbitrary combinations of the two incoming waves, not only the one-sided reference. The audit verifies the full unitary matrix and a general complex two-sided excitation.

The equality $R+T=1$ for one incident direction would be insufficient by itself to establish every matrix constraint for a general proposed model.

## Example 6: phase slope and delay

For the balanced model at resonance, the exact channel derivative gives

$$
\tau_g(f_0)=\frac{1000\times2}{\pi a f_0[\mathrm{THz}]}\;\mathrm{fs}.
$$

At $f_0=200\,\mathrm{THz}$ and $a=0.25$, the group delay is about $12.73\,\mathrm{fs}$. Reducing $a$ makes the spectral phase transition sharper and increases its peak delay. The notebook compares a numerical derivative with the closed form and keeps amplitude beside phase.

The derivative concerns this imposed balanced analytical channel. It does not establish material dispersion, an achromatic geometry, or a geometry-specific bandwidth.

## Reading a research result

Choose a metasurface figure or abstract and record the illumination, structure/material model, target quantity, normalization, and evidence level. Distinguish analytical, simulated, and experimental results. Check whether “efficiency” refers to incident power, transmitted power, one polarization, or a finite collection region.

For physical context, read [Decker et al. on dielectric Huygens surfaces](https://openresearch-repository.anu.edu.au/items/46257eed-cdcb-4814-93fb-868f9c087777) or [Arbabi et al. on phase and polarization control](https://arxiv.org/abs/1411.1494). Their structures and measured/simulated results are external references, not outputs of this introductory model.

## Report checklist

Submit predictions, parameter changes, complex coefficients, power and phase plots, assumptions, checks, and a paragraph describing a claim the model cannot support. A successful report can conclude that more geometry/material information is needed. The [lab](../labs/01-first-investigation.md) provides the runnable source and a bridge to existing full-wave results.
