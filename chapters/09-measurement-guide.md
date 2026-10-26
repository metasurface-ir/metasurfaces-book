# Chapter 9 worked examples and self-check

Use the [chapter](09-materials-measurement.md), [lab](../labs/09-measurement-lab.md) and [executed notebook](../notebooks/09-fabrication-measurement.ipynb) together. All numerical values below describe assigned or synthetic models; none are experimental measurements.

## Example 1: loss and dispersion

**Predict:** At the material pole, does the imaginary permittivity vanish because the real detuning is zero?

**Work:** Set f = fp = 14 GHz, ε∞ = 2, oscillator strength F = 1.1 and damping γf = 1.2 GHz. The oscillator denominator is purely negative imaginary:

$$
\epsilon_r(f_p)=\epsilon_\infty+i\frac{Ff_p}{\gamma_f}
=2+i\,12.8333.
$$

The imaginary part is positive, consistent with dissipation under exp(−iωt). Increasing damping to 2.4 GHz halves this pole value but also alters the real dispersion away from the pole. It does not justify changing only a loss-tangent parameter across the entire band.

**Check:** Evaluate the original complex fraction and the independent real/imaginary rational expressions. The notebook's illustrated spectrum is not TiO₂ or a measured substrate.

## Example 2: linewidth and ambiguity

**Predict:** Can a reflection-power spectrum tell internal and external loss apart?

**Work:** Use κₑ = 0.35 GHz and κᵢ = 0.12 GHz at f₀ = 10 GHz:

$$
\Gamma_0=\frac{0.23}{0.47}\simeq0.489362,\quad
A_0=\frac{4(0.35)(0.12)}{0.47^2}\simeq0.760525,\quad
\Delta f_{\rm FWHM}=0.94\ {\rm GHz},\quad Q_L\simeq10.6383.
$$

Swap the two halfwidths. Their sum and product are unchanged, so absorption and reflectance at every frequency are unchanged. Resonant Γ becomes −0.489362 instead. A complex measurement at a known reference plane distinguishes the resonant signs; a magnitude-only fit cannot.

**Check:** In the lossless limit κᵢ = 0, |Γ| = 1 everywhere. At κᵢ = κₑ, Γ vanishes at resonance and its phase is undefined. The formula assumes one outgoing channel and no transmission.

## Example 3: correlated tolerances

**Predict:** Is adding the two percentage tolerances in quadrature always valid?

**Work:** The baseline contributions to frequency standard deviation are a = 10(0.025/5) = 0.05 GHz and b = 10(0.04/6) = 0.066667 GHz. Thus

$$
\sigma_f=\sqrt{a^2+b^2+2\rho ab}
\simeq
\begin{cases}
0.054263\ {\rm GHz},&\rho=-0.6,\\
0.083333\ {\rm GHz},&\rho=0,\\
0.104616\ {\rm GHz},&\rho=+0.6.
\end{cases}
$$

Positive correlation increases spread because both sensitivity derivatives are negative. A +0.05 mm common width bias gives the exact nominal shift 10(5/5.05)−10 ≈ −0.09901 GHz, close to the linear −0.10 GHz.

**Check:** Compare Monte Carlo standard deviations with these local values, and repeat at smaller spreads to test the linearization. A 95% Wilson interval for acceptance estimates sampling uncertainty in the declared population; it does not certify manufacturing yield.

## Example 4: solve a small calibration

**Predict:** Does dividing by the open reading remove all one-port errors?

**Work:** Use real coefficients D = 0.02, T = 0.9 and S = 0.1 for a hand-checkable example. The three standard readings are

$$
m_{\rm short}=0.02-\frac{0.9}{1.1}=-0.7981818\ldots,\quad
m_{\rm load}=0.02,\quad
m_{\rm open}=0.02+\frac{0.9}{0.9}=1.02.
$$

The load immediately identifies D. Solving the three linear equations gives E = 0.898, S = 0.1 and T = E+DS = 0.9. A DUT with Γ = 0.4 produces m = 0.395; inversion gives

$$
\widehat\Gamma=\frac{0.395-0.02}{0.9+0.1(0.395-0.02)}
=\frac{0.375}{0.9375}=0.4.
$$

In contrast, m/mopen ≈ 0.38725. A single reference division does not identify directivity and source match.

**Check:** Forward-generate a fourth, unused standard Γ = i and recover it using the same coefficients. Add realistic uncertainty to standard responses before interpreting calibration residuals as instrument accuracy.

## Example 5: a phase discrepancy

**Predict:** Does agreement in reflectance rule out a placement mistake?

**Work:** At 10 GHz the air wavelength is 29.9792458 mm. A sample 5 mm beyond the calibrated plane adds round-trip phase

$$
\phi=\frac{4\pi d}{\lambda}\simeq2.09585\ {\rm rad}
=120.083^\circ,\qquad
\sigma_\phi=\frac{4\pi(0.05\ {\rm mm})}{29.9792458\ {\rm mm}}
\simeq0.0209585\ {\rm rad}=1.20083^\circ.
$$

Divide the port reflection by exp(2ikd) to recover the surface response. The reflectance is unchanged by this lossless correction. A positive unknown displacement creates a positive phase shift with our time convention; reversing the correction sign doubles the discrepancy.

**Check:** Compare the phase slope versus frequency with 4πd/c in radians per hertz. The normal-incidence air-path expression is not a general fixture-removal algorithm.

## Example 6: what does 95% mean?

**Predict:** Does a radius of 1.96 standard deviations enclose 95% of a circular two-dimensional Gaussian?

**Work:** For independent unit-normal coordinates, radius r has probability 1−exp(−r²/2). A radius of 1.96 encloses about 85.35%; 95% requires r = √5.991 ≈ 2.448. Transform that circle through the covariance square root to obtain an ellipse.

For the separate averaging model, |Γ| = 0.489362 and σφ = 0.0209585 rad produce the nonzero RMS floor

$$
\mathrm{RMS}_{N\to\infty}
=|\Gamma|\sqrt{2(1-e^{-\sigma_\phi^2/2})}\simeq0.010256.
$$

Averaging 100 readings reduces the assigned circular read-noise RMS from 0.002 to 0.0002, but the fixed-placement contribution remains. With both contributions the total RMS is still approximately 0.01026.

**Check:** This curve describes uncertainty across fixed-placement batches, not repeated repositioning at every reading. The full Monte Carlo cloud additionally includes uncertain standards and calibration readings; do not use the simplified floor as its complete uncertainty budget.

## Self-check and assessment

1. A grounded sample has measured specular reflectance 0.2. Must its absorption be 0.8?
2. Why can a calibration reproduce its three standards perfectly but fail on a fourth?
3. What happens to the tolerance spread if ρ changes sign?
4. Why should uncertain Γ near zero be reported in Cartesian coordinates?

**Answers:** (1) Only if other outgoing channels are absent or included; a finite or diffracting sample can scatter elsewhere. (2) Three observations fit three complex unknowns even when the assumed standards or error model are wrong. (3) Here both sensitivities are negative, so positive correlation increases spread. (4) Phase is undefined at zero, while real and imaginary components remain well-defined.

Assess a report on its explicit measurand and assumptions (25%), reproducible raw-to-corrected processing (30%), independent checks and uncertainty interpretation (30%), and clear figures, citations and limitations (15%). These are suggested lab criteria; the instructor sets course assessment weights.
