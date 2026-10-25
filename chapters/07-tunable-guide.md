---
title: 'Chapter 7: Worked Examples and Learning Path'
short_title: Tuning worked examples
---

# Chapter 7: Worked Examples and Learning Path

Predict before moving a control. Use the [chapter](07-active-tunable.md) for the derivations, the [lab](../labs/07-tunable-lab.md) to inspect saved evidence, and the [notebook](../notebooks/07-tunable-metasurfaces.ipynb) to change assumptions. All examples use the declared equivalent circuit, not a solved metallic patch.

## 1. Find the resonant bias

At 10 GHz with $L=20$ nH, resonance requires $C_r=1/(\omega^2L)$. Invert the capacitance law before searching numerically:

$$
C_r=\frac{1}{\omega^2L}=0.0126651\ {\rm pF},\qquad V_r=V_j\left[\left(\frac{C_0}{C_r}\right)^{1/M}-1\right]=8.47482\ {\rm V}.
$$

This value is inside the 0–20 V control range. Increasing bias moves the resonance upward in frequency. Verify that the absorption maximum follows this curve in the frequency–voltage map. If the calculated voltage lies outside the allowed range, the resonance is unreachable with this control law; clipping it does not solve the original design requirement.

## 2. Separate a useful phase from a reflection zero

$$
X=0:\qquad \Gamma_r=\frac{R-Z_0}{R+Z_0},\qquad A_r=\frac{4RZ_0}{(R+Z_0)^2}.
$$

For $R=25\,\Omega$ and $Z_0=376.7303\,\Omega$, $\Gamma_r\approx-0.87554$, so the reflected fraction is about 0.7666 and absorption about 0.2334. If instead $R=Z_0$, the reflection is zero and its phase is undefined. A plot that assigns a clean phase at this zero is hiding the singularity.

**Independent check:** solve $1+\Gamma=Z_sH_t$ and $1-\Gamma=Z_0H_t$ as two linear equations. The ratio of resistive dissipation to incident power is $RZ_0|H_t|^2$. It must equal $A$. This tests the boundary formulation as well as the closed expression.

## 3. Compare bits with reachable electromagnetic states

$$
\eta_q=\operatorname{sinc}^2(1/2^B),\qquad B=1,2,3,4:\quad \eta_q\approx0.4053,\ 0.8106,\ 0.9496,\ 0.9872.
$$

These are uniform phase-error averages. The executed finite 32-source array at 25° instead gives approximately 0.3890, 0.8086, 0.9483 and 0.9868. The phase errors at its particular sample positions are not a continuous uniform distribution. Sixteen equally spaced voltage commands give 0.8440 because their complex states have incomplete phase coverage and variable magnitude.

**Why the mirror beam?** For ideal one-bit states $\Gamma_j=\pm1$, the aperture is real. Hence $F(-\theta)=F(\theta)^*$ and the intensity is symmetric. With nonzero steering, selecting a maximum on one side does not remove the equal mirror maximum. The reported “peak angle” is the first maximum on the sampled angle grid. All these values are scalar target-direction metrics, not integrated efficiencies.

## 4. Check feedback against a hidden-parameter calculation

The target is the nominal response at $V_t=8$ V. The synthetic plant has $C_0^{\rm plant}=1.12C_0$, while all other parameters stay fixed. The controller receives complex measurements, not this parameter. Equal capacitance supplies an independent answer:

$$
\frac{1.12C_0}{(1+V_*/V_j)^M}=\frac{C_0}{(1+V_t/V_j)^M}\quad\Longrightarrow\quad V_*=V_j\left[1.12^{1/M}(1+V_t/V_j)-1\right]=9.08\ {\rm V}.
$$

The saved search uses 26 measurement queries and recovers this value. Inspect all queries, including poor trials. The coarse search costs 17 queries before refinement even starts. With noise, a single tiny residual does not certify reliable calibration; repeat the final measurement and evaluate conditions withheld from fitting. If a changed plant puts the independent answer outside 0–20 V, report an unreachable target and the remaining complex error.

## 5. Derive a settling time and a driver bandwidth

$$
\frac{|V(t)-V_1|}{|V_0-V_1|}=e^{-t/\tau},\qquad t_{2\%}=-\tau\ln0.02=15.6481\ \mu{\rm s}\quad(\tau=4\ \mu{\rm s}).
$$

For a small sinusoidal voltage command with the same $e^{-i\Omega t}$ convention, the driver transfer function is $H_d(\Omega)=1/(1-i\Omega\tau)$. Its magnitude falls to $1/\sqrt2$ at $f_{\rm 3dB}=1/(2\pi\tau)=39.79$ kHz. This bandwidth describes voltage response. The complex reflection follows a nonlinear map of voltage, so its large-signal switching waveform and spectral weights require evaluating $\Gamma[V(t)]$. Neither number is a measured property of a physical varactor or an FPGA.

## 6. Explain where a suppressed carrier goes

Let an ideal reflection envelope alternate between $+1$ and $-1$ with duty cycle $D=1/2$. Substitute into the derived coefficient formula:

$$
c_0=0,\qquad c_{+1}=\frac{2i}{\pi},\qquad c_{-1}=-\frac{2i}{\pi},\qquad |c_{\pm1}|^2=\frac4{\pi^2}\approx0.405285.
$$

The first pair accounts for about 0.81057 of the mean-square envelope. The remaining 0.18943 lies in higher odd harmonics; a two-bar spectrum is incomplete. Parseval gives $\sum_\ell|c_\ell|^2=\langle|\Gamma(t)|^2\rangle=1$ for this ideal waveform. With $e^{-i\omega t}$, positive $\ell$ means $\omega_0+\ell\Omega$. The plotted reference uses actual circuit states at 3 and 14 V; its carrier is therefore not required to vanish. A finite RC transition changes the waveform and its coefficients. Envelope Parseval is not a full electromagnetic pump-and-sideband power balance.

## Assessment and evidence

| Criterion | Weight | Evidence to submit |
| --- | --- | --- |
| Model and conventions | 20% | Geometry, reference plane, time convention and declared omissions |
| Derivation and independent checks | 25% | Boundary power, resonance, feedback or Fourier check |
| Controlled comparison | 25% | Same normalization and bounds; one failed or unreachable case |
| Reproducibility | 20% | Editable notebook, parameters, environment and query/data logs |
| Interpretation | 10% | Supported claim, uncertainty and next physical validation |
