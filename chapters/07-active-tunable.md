---
title: 'Chapter 7: Active, Tunable, and Intelligent Metasurfaces'
short_title: Tunable and intelligent surfaces
---

# Chapter 7: Active, Tunable, and Intelligent Metasurfaces

**Opening question:** a reflector steers a beam to one receiver. The receiver moves. Can the same manufactured surface redirect the beam by changing its control voltages, and what prevents arbitrary amplitude and phase control?

This chapter follows the chain **control → material or circuit state → complex response → aperture field → measurement → correction**. Read Chapters 2 and 4 for phasors, flux, and diffraction, Chapter 5 for synthesis, and Chapter 6 for validation. The [guide](07-tunable-guide.md), [browser lab](../labs/07-tunable-lab.md), and [executed notebook](../notebooks/07-tunable-metasurfaces.ipynb) develop one reproducible reference.

:::{note} What has been executed
A passive equivalent-impedance model, finite scalar array factors, noiseless synthetic calibration, and a slow modulation-envelope model. Independent circuit-boundary, ODE, Fourier and limiting-case checks are supplied. The patch drawing is an original explanatory schematic; no biased patch, diode, fabricated array, or control hardware has been simulated full-wave or measured here.
:::

## 7.1 Four words that describe different capabilities

A **tunable** surface changes response after fabrication. A **programmable** surface selects spatial or temporal patterns from controllable states. An **adaptive** surface changes its settings using observations. An **intelligent** system needs a defined sensing and decision process with a measurable objective; the label alone supplies no evidence of learning, autonomy, or robustness.

“Active” is used in two senses. A bias-controlled device can consume control power while remaining passive at the signal frequency. Electromagnetic gain instead requires energy delivered to the signal and an appropriate stability/noise analysis. Our circuit has nonnegative resistance and no RF gain. Its DC bias is a control parameter; the circuit does not calculate driver energy.

## 7.2 Choose a tuning mechanism by its constraints

The mechanism determines the accessible states and their dynamics. Do not transfer a switching-speed or phase-range claim from one frequency, geometry, and bias network to another.

| Mechanism | Changed quantity | What must be characterized |
| --- | --- | --- |
| PIN switch | RF connection / impedance state | State contrast, package parasitics, bias routing, RF loss |
| Varactor-like tuning | Bias-dependent capacitance | Complex response versus voltage and frequency; safe bias range |
| Liquid crystal | Orientation and permittivity tensor | Polarization, thickness, relaxation and alignment |
| Phase-change material | Complex optical constants and phase fraction | Heating, state history, repeatability and cycling |
| Electro-optic or carrier tuning | Permittivity / carrier population | Electrode overlap, loss, capacitance and drive bandwidth |
| Mechanical actuation | Geometry or separation | Displacement, stability, mechanical response and repeatability |

Examples to read critically include [Cui et al. (2014)](https://doi.org/10.1038/lsa.2014.99) on programmable coding, [Chou et al. (2016)](https://doi.org/10.1364/OE.24.024265) on electrically switched liquid-crystal diffractive waveplates, and [Wang et al. (2021)](https://doi.org/10.1038/s41565-021-00882-8) on electrically switched phase-change antennas. These demonstrate different platforms; the numerical reference below reproduces none of their devices.

## 7.3 Point to the object behind the model

```{figure} ../assets/chapter-07/tunable-cell.svg
:alt: Conceptual split patch, bias-controlled gap, grounded section and effective series RLC boundary model.

The drawing connects a possible control mechanism to an effective one-port boundary. The effective R, L and C are assigned directly, without a geometry extraction. The ground-backed model has no transmitted port. The array exercise later assigns one circuit response to each prescribed scalar source.
```

We use $e^{-i\omega t}$, normal incidence, a real positive wave impedance $Z_0$, and a reference plane on the effective surface. Set $f=10$ GHz, $L=20$ nH, $R=25\,\Omega$, $C_0=0.12$ pF, $V_j=1$ V, $M=1$, and $0\le V\le20$ V. These are effective educational parameters, not component specifications. Changing the reference plane adds propagation phase; calibration must use the same plane as the target.

## 7.4 Derive reflection and check passivity

$$
Z_s=R+iX,\qquad X=\frac{1}{\omega C(V)}-\omega L,\qquad \Gamma=\frac{Z_s-Z_0}{Z_s+Z_0}.
$$

The signs follow directly from the time convention: an inductor has impedance $-i\omega L$ and a capacitor has $i/(\omega C)$. At the surface, normalize the incident electric field to one. The reflected magnetic field has the opposite sign, so the boundary condition gives

$$
E_t=1+\Gamma,\qquad H_t=\frac{1-\Gamma}{Z_0},\qquad E_t=Z_sH_t\ \Longrightarrow\ \Gamma=\frac{Z_s-Z_0}{Z_s+Z_0}.
$$

Subtract numerator and denominator squared magnitudes to obtain the absorbed fraction:

$$
\mathcal R=|\Gamma|^2=\frac{(R-Z_0)^2+X^2}{(R+Z_0)^2+X^2},\qquad A=1-\mathcal R=\frac{4RZ_0}{(R+Z_0)^2+X^2}.
$$

For $R\ge0$, $0\le A\le1$. At $R=0$, all incident power is reflected; tuning changes phase. At $X=0$ and $R=Z_0$, $\Gamma=0$ and $A=1$: the reflection phase is undefined. The independent audit solves the two boundary equations numerically and evaluates resistive dissipation from the resulting magnetic field, rather than checking only the same closed formula twice.

## 7.5 Voltage, resonance, and sensitivity

$$
C(V)=\frac{C_0}{(1+V/V_j)^M},\qquad f_r(V)=\frac{1}{2\pi\sqrt{LC(V)}},\qquad \frac{df_r}{dV}=\frac{M f_r}{2(V_j+V)}.
$$

For positive $M$, increasing bias decreases capacitance and raises the LC resonance. The 10-GHz reference crosses resonance near 8.475 V. Its continuous nonzero-reflection phase trajectory spans about 295.27°, not 360°. Reflection magnitude also changes. Use the complex trajectory to decide reachability before choosing a codebook.

```{figure} ../assets/chapter-07/tuning.png
:alt: Complex reflection trajectory, bias-dependent phase and reflectance, and a frequency-bias absorption map.

Original executed circuit results. The dashed resonance line identifies the state where reactance changes sign. A phase range is useful only together with its amplitude, frequency and voltage bounds.
```

Sensitivity follows by differentiating the complex response. Away from a reflection zero,

$$
\frac{d\Gamma}{dV}=\frac{2Z_0}{(Z_s+Z_0)^2}\frac{dZ_s}{dV},\qquad \frac{dZ_s}{dV}=-\frac{i}{\omega C^2}\frac{dC}{dV},\qquad \frac{d\arg\Gamma}{dV}=\frac{\operatorname{Im}(\Gamma^*\,d\Gamma/dV)}{|\Gamma|^2}.
$$

A steep phase slope can amplify bias error. A phase jump near vanishing amplitude is not free wavefront control. Characterize loss, frequency span, control precision and repeatability together. Real components add bias-dependent resistance, package inductance, hysteresis and heating that this simple law omits.

## 7.6 From controllable states to a codebook

With $B$ control bits there are $Q=2^B$ commands. Their complex responses need not be equally spaced, distinct, or high magnitude. For a desired unit-magnitude aperture sample $d_j$, our declared selection rule is

$$
b_j=\operatorname*{arg\,min}_{b\in\{0,\ldots,Q-1\}}|\Gamma(V_b,f_0)-d_j|^2,\qquad V_b=\frac{bV_{\max}}{Q-1}.
$$

This minimizes a local complex-field mismatch and naturally retains amplitude penalties. It is not a global optimization of beam power or sidelobes. A global phase offset of the desired aperture is physically free in this scalar pattern, but can change which limited states are selected; searching that offset is an extension exercise. Retain the actual voltage, frequency, reference plane and calibration version with each codeword.

## 7.7 What the programmed aperture predicts

$$
d_j=e^{ik_0x_j\sin\theta_t},\qquad F(\theta)=\frac1N\sum_{j=0}^{N-1}\Gamma_j e^{-ik_0x_j\sin\theta},\qquad I(\theta)=|F(\theta)|^2.
$$

These signs follow Chapter 4: a positive phase gradient produces a positive tangential output wavevector. For $\Gamma_j=d_j$, every term at $\theta_t$ is one. The reference has 32 prescribed sources, spacing $\lambda_0/2$ at 10 GHz, normal incidence, and a target of 25°. $I$ uses the coherent unit-source reference. It is neither integrated diffraction efficiency nor antenna directivity; element patterns, vector flux, coupling and finite-ground scattering are absent.

```{figure} ../assets/chapter-07/array.png
:alt: Common-normalization scalar patterns, selected voltages across 32 positions, and target-direction metrics for ideal and circuit codebooks.

One-bit coding can leave a mirror beam. The 16-voltage circuit differs from 16 ideal phase states because it has incomplete phase coverage and state-dependent loss. The voltage plot identifies the commanded aperture behind the pattern.
```

A useful comparison is an ideal phase quantizer whose errors are uniformly distributed over $[-\pi/Q,\pi/Q]$. Averaging the complex phase error gives

$$
\left\langle e^{i\epsilon}\right\rangle=\frac{Q}{2\pi}\int_{-\pi/Q}^{\pi/Q}e^{i\epsilon}\,d\epsilon=\operatorname{sinc}(1/Q),\qquad \eta_q=\operatorname{sinc}^2(1/Q),\quad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

This is a coherent phase-error benchmark, not an exact efficiency law for a particular finite metasurface. In our finite reference, the ideal 1/2/3/4-bit target metrics are approximately 0.389/0.809/0.948/0.987; the 16-voltage circuit gives 0.844. A higher command count does not remove amplitude loss, inaccessible phases or model error.

## 7.8 Feedback makes adaptation testable

An adaptive loop needs a sensor or measured observable, an objective, a constrained controller, and a verified update. The hardware demonstration by [Ma et al. (2019)](https://doi.org/10.1038/s41377-019-0205-3) combines sensing and reprogramming. Our narrower example uses a synthetic complex-reflection measurement and a bounded scalar search; it is not machine learning or an autonomous hardware demonstration.

$$
J(V)=|\Gamma_{\rm measured}(V)-\Gamma_{\rm target}|^2,\qquad 0\le V\le V_{\max}.
$$

The nominal target is the response at 8 V. An unreported-to-controller 12% increase in $C_0$ shifts the plant. A 17-point coarse scan followed by bounded refinement recovers 9.08 V with 26 response queries in the reference. An independent equal-capacitance calculation confirms that value. For noisy or hysteretic plants, repeat measurements, track uncertainty and state history, impose a stopping budget, and test on conditions excluded from calibration. A local refinement does not guarantee a global optimum for an arbitrary plant.

```{figure} ../assets/chapter-07/feedback.png
:alt: Target, biased response and corrected response in the complex plane, with all calibration queries and best-so-far error.

The plant has one known-to-the-author perturbation and noiseless measurements. The controller sees only the returned complex response. Retaining every query makes the calibration cost and failed trials visible.
```

## 7.9 Include the control dynamics

$$
\tau\frac{dV}{dt}+V=V_{\rm cmd},\qquad V(t)=V_1+(V_0-V_1)e^{-t/\tau},\qquad t_{2\%}=-\tau\ln(0.02).
$$

For an illustrative effective driver time constant of 4 μs, a voltage step settles to 2% in 15.648 μs. This driver time constant is separate from the RF LC values. The phase is $\arg\Gamma[V(t)]$, not an assumed linear interpolation between endpoint phases. Sensor delay, computation time, communication and settling all contribute to update latency. Do not equate an FPGA clock rate with the surface settling rate.

## 7.10 Time modulation creates extra frequency channels

$$
\Gamma(t)=\sum_{\ell\in\mathbb Z}c_\ell e^{-i\ell\Omega t},\qquad c_\ell=\frac1T\int_0^T\Gamma(t)e^{i\ell\Omega t}\,dt,\qquad \omega_\ell=\omega_0+\ell\Omega.
$$

The last relation follows by multiplying the reflection envelope by $e^{-i\omega_0t}$. For a binary waveform with $\Gamma_a$ during $0\le t<DT$ and $\Gamma_b$ during the rest, integrate the two constant intervals:

$$
c_\ell=(\Gamma_a-\Gamma_b)D\operatorname{sinc}(\ell D)e^{i\pi\ell D}+\Gamma_b\delta_{\ell0}.
$$

For $D=1/2$ and ideal states $+1,-1$, the carrier vanishes and the first sideband weights are $4/\pi^2$ each; higher odd harmonics remain. This is a Fourier redistribution, not disappearance of energy. The notebook instead uses its actual circuit states at 3 and 14 V and compares instantaneous switching with the steady periodic RC response.

```{figure} ../assets/chapter-07/dynamics.png
:alt: Voltage step, nonlinear reflection phase, periodic RC waveform and sideband envelope weights.

The carrier is 10 GHz and the modulation is 20 kHz. The envelope is evaluated with the frozen-state circuit response. It omits the electromagnetic transient and pump energy; the spectral bars are not a full device power budget.
```

A frozen-state model requires modulation slow enough relative to the electromagnetic response and a valid calibrated response across the relevant band. [Zhang et al. (2018)](https://doi.org/10.1038/s41467-018-06802-0) demonstrates space–time coding with a different hardware platform. In a full time-varying calculation, include frequency conversion, pump exchange and appropriate power normalization. Passivity at each frozen bias does not by itself prove a complete modulated energy balance. Temporal modulation alone is also insufficient evidence of nonreciprocal operation; define and compare the appropriate frequency-port scattering experiments.

## 7.11 A verification ladder for a physical device

1. Measure or justify the tuning law, complex material/component data, operating limits, and state history.
2. Solve one biased cell with its actual electrodes, substrate, package and ground; verify phase planes, all channels, and convergence.
3. Test unlike neighboring states in a supercell before assuming the isolated-cell library remains accurate.
4. Test a finite aperture with illumination, element patterns, edges and measured calibration.
5. Include driver bandwidth, switching energy, thermal drift, sensor noise and latency in closed-loop tests.
6. For modulation, inspect carrier and sidebands and account for external pump work. Preserve failed configurations and the conditions under which the controller stops.

The current [Chapter 3](03-unit-cell-design.md) TE dielectric ridge solver is not a drop-in solver for a three-dimensional metallic diode-loaded patch. Use an appropriate electromagnetic/material model when moving beyond this circuit exercise. Chapter 8 will address communication-system objectives; Chapter 9 will address fabrication and measurement; [Chapter 10](10-ai-metasurfaces.md) adds learned surrogates after the data and validation problem are defined.

## 7.12 Exercises and further reading

1. Derive the absorption formula and independently calculate power dissipated in R.
2. Change R toward $Z_0$. Explain why a larger apparent phase jump can coincide with unusable reflection.
3. Compare equal-voltage and phase-aware codebooks under the same voltage range and state count.
4. Search a global target-phase offset; report both the target metric and the strongest unwanted lobe.
5. Add sensor noise to calibration. Repeat the experiment and report a voltage interval, query budget and unreachable-target case.
6. Derive the binary temporal coefficients using the declared sign convention; test duty cycles other than 1/2.
7. Design a full-wave validation that could falsify the independent-cell approximation for a programmed array.

Primary research examples are linked beside the relevant discussion. All chapter diagrams, numerical plots, explanations and code are original teaching material; no publication figures have been copied. For each paper, identify its mechanism, actual validation level and limits before comparing its results with this analytical model.
