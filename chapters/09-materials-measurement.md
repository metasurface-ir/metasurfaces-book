# 9. Materials, fabrication, and measurement methods

A simulation predicts a resonance at 10 GHz. The fabricated sample resonates lower, and its measured phase differs by 120°. Did the material change, did the mask print too wide, or was the sample simply placed 5 mm away from the assumed reference plane? A convincing comparison must separate those explanations.

This chapter follows a device from material assumptions to fabrication variation, raw complex observations, calibration and uncertainty. Start after [wave and power conventions](02-waves-and-interfaces.md), [unit cells](03-unit-cell-design.md), and [numerical validation](06-numerical-methods.md). Use the [six worked examples](09-measurement-guide.md), [four-part browser lab](../labs/09-measurement-lab.md), and [executed notebook](../notebooks/09-fabrication-measurement.ipynb).

**Evidence boundary:** every observation in this chapter is synthetic. The material spectrum is illustrative, the resonance is an assigned effective model, and the drawing explains possible hardware. No fabricated patch, measured material, instrument calibration or experimental efficiency is claimed.

## 9.1 What must agree?

By the end, you should be able to specify a measurable quantity and its reference plane, propagate geometric tolerances, solve a three-standard calibration, distinguish uncertainty from fabrication spread, and prepare a reproducible simulation-to-measurement comparison.

The notebook's object is a **one-port resonator**, with an opaque backing and one modeled outgoing channel. A grounded patterned conductor is one possible physical interpretation. Width and effective permittivity change its assigned resonance through a local scaling law; no mesh of that patch is solved. The material oscillator is a separate exercise, not a hidden source of resonator parameters.

```{figure} ../assets/chapter-09/measurement-geometry.svg
:alt: Original schematic: a possible grounded patch, fabrication and metrology, the modeled one-port reference planes, and a separate free-space measurement concept. Dimensions are illustrative; the patch and horn fixture are not solved.

Original schematic: a possible grounded patch, fabrication and metrology, the modeled one-port reference planes, and a separate free-space measurement concept. Dimensions are illustrative; the patch and horn fixture are not solved.
```

## 9.2 Choose a material spectrum

Choose a platform together with the operating band, polarization, thermal environment and fabrication route. For a microwave printed conductor, examine conductivity, substrate dispersion/loss, thickness and roughness. For a dielectric optical element, examine the measured complex index, attainable height and minimum feature size. A high index can help confinement while making resonant dimensions sensitive to process errors. A scalar material model is inadequate when anisotropy or a bias-dependent tensor matters.

A primary example of joint material/process selection is the amorphous-TiO₂ platform and atomic-layer-deposition route reported by [Devlin et al. (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5035844/). Read the paper's material and fabrication evidence; its performance does not transfer automatically to a different wavelength or geometry. None of its figures or measured data are reproduced here.

With time dependence exp(−iωt), the illustrative relative permittivity is

$$
\epsilon_r(\omega)=\epsilon_\infty+
\frac{F\omega_p^2}{\omega_p^2-\omega^2-i\gamma\omega},
\qquad \epsilon_\infty,F,\omega_p,\gamma>0.
$$

Multiply numerator and denominator by the complex conjugate to check passivity:

$$
\operatorname{Im}\epsilon_r=
\frac{F\omega_p^2\gamma\omega}
{(\omega_p^2-\omega^2)^2+\gamma^2\omega^2}\ge0,\qquad
\langle p_{\rm loss}\rangle=\frac{\omega\epsilon_0}{2}
\operatorname{Im}\epsilon_r\,|\mathbf E|^2.
$$

For a nonmagnetic isotropic medium, use the passive branch n+iκ = √εᵣ. For positive frequency, n and κ are nonnegative in this example. Conductivity contributes +iσ/(ωε₀) to relative permittivity under the same convention. Do not add that term a second time if the measured complex permittivity already includes conduction. The familiar loss tangent ε″/ε′ is useful only with a stated convention and away from ε′ = 0.

The notebook uses f in GHz and divides every angular-frequency factor by 2π consistently. Its material pole is 14 GHz, while its separate device resonance is 10 GHz. They are different models.

```{figure} ../assets/chapter-09/materials.png
:alt: Executed illustrative material spectra. Solid curves show real parts; dashed curves show imaginary parts. Changing damping changes dispersion and loss together.

Executed illustrative material spectra. Solid curves show real parts; dashed curves show imaginary parts. Changing damping changes dispersion and loss together.
```

## 9.3 From mask to measured geometry

A design file is not the fabricated geometry. Preserve the intended mask, process conditions and observed dimensions separately.

| Stage | Possible discrepancy | Evidence to preserve |
| --- | --- | --- |
| Material preparation | Film thickness, composition, substrate permittivity | Lot, thickness map, characterized spectrum and temperature |
| Pattern definition | Exposure/printing bias, alignment, minimum gap | Mask version, nominal dimensions, process settings |
| Pattern transfer | Sidewall taper, undercut, residue, roughness | Cross-section or surface metrology with scale calibration |
| Assembly | Ground contact, spacer thickness, connector or fixture placement | Assembly record and reference-plane definition |
| Sampling | Within-wafer variation versus between-lot shifts | Spatial locations, repeated samples and sampling plan |

Photolithography, electron-beam lithography, imprinting and PCB patterning have different feature-size and throughput constraints; select a qualified process rather than transferring a generic recipe. A top-view width alone cannot identify a tapered three-dimensional profile. Start the simulation comparison with measured dimensions and uncertainty, while retaining the nominal design as a separate baseline.

## 9.4 A tractable resonator

Let κₑ and κᵢ denote external and internal frequency halfwidths, both in GHz, with κₑ > 0 and κᵢ ≥ 0. The assigned reflection amplitude has background −1:

$$
\Gamma(f)=-1+\frac{2\kappa_e}{\kappa_e+\kappa_i-i(f-f_0)},\qquad
A(f)=1-|\Gamma|^2=
\frac{4\kappa_e\kappa_i}{(\kappa_e+\kappa_i)^2+(f-f_0)^2}.
$$

Proof: combine the two terms of Γ over a common denominator; its numerator becomes κₑ−κᵢ+i(f−f₀). Subtract the numerator's squared magnitude from the denominator's. The difference is 4κₑκᵢ, which is nonnegative. Thus the assumed one-port model conserves power and is passive. The absorption full width at half maximum and the loaded quality factor are

$$
\Delta f_{\rm FWHM}=2(\kappa_e+\kappa_i),\qquad
Q_L=\frac{f_0}{2(\kappa_e+\kappa_i)},\qquad
\Gamma(f_0)=\frac{\kappa_e-\kappa_i}{\kappa_e+\kappa_i}.
$$

Critical coupling κₑ = κᵢ gives Γ(f₀) = 0. Its phase is undefined, so a dramatic phase uncertainty near that point need not mean a large complex-response error. Swapping κₑ and κᵢ preserves the whole magnitude spectrum but changes the complex response; magnitude-only fitting cannot distinguish the two branches.

Our baseline uses f₀ = 10 GHz, κₑ = 0.35 GHz and κᵢ = 0.12 GHz. These are assigned rates, not values extracted from the drawn patch. Absorption at resonance is about 0.7605 and Qₗ ≈ 10.638.

## 9.5 Propagate fabrication tolerances

Use this local scaling law as an explicit assumption, with w₀ = 5 mm and εeff,₀ = 3. It fixes the nominal resonance independently of the sketch and is not a general patch-design equation:

$$
f_0(w,\epsilon_{\rm eff})=f_{00}\frac{w_0}{w}
\sqrt{\frac{\epsilon_{{\rm eff},0}}{\epsilon_{\rm eff}}},
\qquad
\frac{\delta f_0}{f_{00}}\simeq-\frac{\delta w}{w_0}
-\frac{\delta\epsilon_{\rm eff}}{2\epsilon_{{\rm eff},0}}.
$$

Take the logarithm and differentiate to obtain the second relation. It holds locally for small variations while the other parameters and resonance branch stay fixed. For standard deviations σw, σε and correlation ρ, apply the variance of a linear combination:

$$
\sigma_f^2\simeq f_{00}^2\left[
\left(\frac{\sigma_w}{w_0}\right)^2+
\left(\frac{\sigma_\epsilon}{2\epsilon_{{\rm eff},0}}\right)^2+
2\rho\frac{\sigma_w}{w_0}\frac{\sigma_\epsilon}{2\epsilon_{{\rm eff},0}}
\right].
$$

Both sensitivities have the same sign, so positive correlation increases frequency spread. With σw = 0.025 mm and σε = 0.04, independent variation predicts σf = 0.08333 GHz. A common +0.05 mm width bias shifts the resonance by approximately −0.10 GHz; it is not reduced by fabricating more identical samples.

The notebook estimates the probability of |f₀−10 GHz| ≤ 0.12 GHz in a stipulated population. Its binomial sampling interval quantifies finite Monte Carlo sample size. It does not quantify whether the Gaussian population or the scaling law describes a fabrication line. Tolerance spread among devices and uncertainty in measuring one device are different quantities.

```{figure} ../assets/chapter-09/tolerance.png
:alt: Executed tolerance distributions and acceptance fractions. Correlation changes spread; a common width bias moves the population away from the target.

Executed tolerance distributions and acceptance fractions. Correlation changes spread; a common width bias moves the population away from the target.
```

## 9.6 Define the measurand

A measurand is the quantity you intend to measure, with conditions sufficient to interpret it. State frequency, polarization basis, incidence angle, reference planes, sample area, illumination and collection aperture. A specular co-polarized reflection coefficient, total hemispherical reflectance and beam-steering efficiency are different measurands.

| Setup | Observable | Essential qualification |
| --- | --- | --- |
| VNA with coaxial or waveguide fixture | Complex mode-to-mode S parameters | Calibrated modal ports, fixture removal, known reference impedances |
| Horn illumination and receiving antenna | Collected complex field or power | Antenna patterns, sample footprint, angular/polarization collection, background and alignment |
| Optical spectrometer and detector | Spectral power ratio within collection optics | Dark/reference readings, detector response, numerical aperture, polarization |
| Interferometric or ellipsometric measurement | Phase or polarization-dependent complex ratio | A stated reference/model and its parameter identifiability |

For a passive sample with all outgoing powers accounted for,

$$
A=1-\sum_{\alpha\in{\cal R}}R_\alpha-\sum_{\beta\in{\cal T}}T_\beta.
$$

The sets must include relevant diffraction orders, polarizations and diffuse channels. For the chapter's ideal one-port model, this reduces to 1−|Γ|². For a real opaque patterned sample, missing specular power can leave through other reflection channels. Call it apparent extinction unless the missing channels have been bounded.

Time-domain gating can suppress sufficiently separated echoes, but a finite time window also changes spectral resolution and can remove part of a resonant response. Preserve the ungated data and vary the window. Instrument calibration at cable ports does not automatically remove antennas, free-space backgrounds or sample-placement errors.

## 9.7 Solve a three-term calibration

The one-port error model uses directivity D, reflection tracking T and source match S. Section 3.1 of [NIST Technical Note 2079](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2079.pdf) provides a primary reference for these terms. Here we derive and test the model in our own notation:

$$
m=D+\frac{T\Gamma}{1-S\Gamma}.
$$

D adds a leakage offset. T scales and rotates the returned signal. The denominator sums repeated reflections between the source mismatch and DUT: Γ + SΓ² + S²Γ³ + …, when |SΓ| < 1.

Multiply by 1−SΓ and set E = T−DS. For three known reflections Γⱼ and observed readings mⱼ, solve

$$
\begin{bmatrix}
1&\Gamma_1&m_1\Gamma_1\\
1&\Gamma_2&m_2\Gamma_2\\
1&\Gamma_3&m_3\Gamma_3
\end{bmatrix}
\begin{bmatrix}D\\E\\S\end{bmatrix}
=\begin{bmatrix}m_1\\m_2\\m_3\end{bmatrix},
\qquad T=E+DS.
$$

Three distinct, sufficiently separated standards constrain three complex unknowns. Nearly identical standards make the solve ill-conditioned. Ideal short, load and open have Γ = −1, 0, +1 at the same plane in this educational example. Real standards have characterized, frequency-dependent responses and uncertainties. These ideal values are not instructions for calibrating a horn/free-space system.

Rearrange the observation equation to invert it:

$$
\widehat\Gamma=\frac{m-D}{T+S(m-D)},\qquad
\frac{\partial\widehat\Gamma}{\partial m}
=\frac{T}{[T+S(m-D)]^2}.
$$

A small inverse denominator amplifies noise. Reject singular cases instead of silently clipping the answer to a passive disk. Check an independent verification standard not used in the calibration; the audit uses Γ = i. Reproducing the three fitted standards alone is not independent verification. A nonlinear calibration can map noisy readings slightly outside |Γ| ≤ 1; investigate the uncertainty and model rather than automatically claiming gain.

## 9.8 Move the reference plane

Place the calibrated port plane at z = 0 and the sample at z = d in a uniform lossless medium, with incidence along +z. The incident wave accumulates exp(ikd); the reflected wave travels the same distance back. Under exp(−iωt),

$$
\Gamma_{\rm port}=\Gamma_{\rm surface}e^{2ikd},\qquad
\Gamma_{\rm surface}=\Gamma_{\rm port}e^{-2ikd},\qquad
\delta\phi=2k\,\delta d=\frac{4\pi f}{c}\delta d.
$$

Here k = 2πf/c for air. At 10 GHz, d = 5 mm contributes approximately +120.083°. It changes phase while preserving reflectance. Unknown placement with standard deviation 0.05 mm contributes about 1.201° phase standard deviation. A known displacement can be corrected; an uncertain displacement must also enter the uncertainty budget.

The simple factor assumes one propagation mode and no extra fixture reflections. A lossy or multimode fixture needs its own network or field model. For oblique plane-wave incidence between parallel planes, the longitudinal wave number replaces k; do not use the normal-incidence expression blindly.

```{figure} ../assets/chapter-09/calibration.png
:alt: Synthetic readings before calibration, after calibration at the port and after the known plane correction. The recovered surface response overlays the assigned truth; the port and surface powers overlap even when phases differ.

Synthetic readings before calibration, after calibration at the port and after the known plane correction. The recovered surface response overlays the assigned truth; the port and surface powers overlap even when phases differ.
```

## 9.9 Report complex uncertainty

The [JCGM guides](https://www.bipm.org/en/web/guest/publications/guides) provide the metrology reading route: GUM for uncertainty evaluation, Supplement 1 for Monte Carlo propagation and Supplement 2 for multiple outputs. Type A and Type B describe evaluation methods, not synonyms for random and systematic error. Correct a known bias where appropriate and retain uncertainty in the correction.

For our model, collect real input quantities in x and output y = [Re Γ, Im Γ]ᵀ. Linearize the actual measurement equation, including calibration and placement:

$$
\delta\mathbf y\simeq J\delta\mathbf x,\qquad
J_{ab}=\frac{\partial y_a}{\partial x_b},\qquad
\Sigma_y\simeq J\Sigma_xJ^{\mathsf T}.
$$

This follows by substituting the linearized deviations into E[δy δyᵀ]. Keep off-diagonal input covariance: the same calibration standard or material fit can correlate many frequency points. Repeated frequency points are not independent devices.

For an approximately bivariate-normal output with known covariance, the 95% probability ellipse is

$$
(\mathbf y-\boldsymbol\mu)^{\mathsf T}\Sigma_y^{-1}
(\mathbf y-\boldsymbol\mu)\le\chi^2_{2,0.95}
=-2\ln(0.05)\simeq5.991.
$$

Whiten the two Gaussian coordinates; their squared radius has cumulative probability 1−exp(−r²/2). This gives 5.991, not a radius of 1.96. Our plotted ellipse uses a sample covariance from 2,000 nonlinear Monte Carlo trials, so its 95% interpretation is approximate; the notebook also reports the observed sample fraction inside it. It describes response uncertainty, not a confidence interval for the Monte Carlo mean.

Near Γ = 0, use real and imaginary coordinates. Phase becomes undefined and its linearized uncertainty is unstable. Never interpret a narrow magnitude interval alone as evidence that phase is well determined.

## 9.10 What averaging leaves behind

In a separate simplified model, let one batch of N readings share a placement phase error δφ, while additive circular reading noise nⱼ is independent with E|nⱼ|² = σn². Across batches δφ is zero-mean Gaussian with standard deviation σφ, independent of the noise:

$$
\overline\Gamma=\Gamma e^{i\delta\phi}+\frac1N\sum_{j=1}^N n_j,\qquad
\mathbb E|\overline\Gamma-\Gamma|^2=
\frac{\sigma_n^2}{N}+2|\Gamma|^2
\left(1-e^{-\sigma_\phi^2/2}\right).
$$

Proof: the zero-mean noise makes the cross term vanish. Expand |exp(iδφ)−1|² = 2−2cos δφ and use the Gaussian characteristic function E cos δφ = exp(−σφ²/2). For small phase spread, the second term is approximately |Γ|²σφ². This is mean squared error about truth, including nonlinear bias; it is not merely variance about the output mean.

The first term falls with N, but the second stays. Calibration uncertainty, drift and model discrepancy can add further limits. Taking more readings cannot establish that the material model or the calibration standards are correct.

```{figure} ../assets/chapter-09/uncertainty.png
:alt: Executed nonlinear uncertainty cloud and a separate analytic averaging example. Placement creates a phase-dominated direction in the complex plane and a floor that independent reading averages do not remove.

Executed nonlinear uncertainty cloud and a separate analytic averaging example. Placement creates a phase-dominated direction in the complex plane and a floor that independent reading averages do not remove.
```

## 9.11 Close the evidence chain

Before comparing simulation with measurement, make the quantity, geometry, materials, polarization, bandwidth and reference planes agree. Preserve raw complex observations, standard characterizations, instrument settings, sample identifiers and metrology alongside processed plots. Keep solver convergence from Chapter 6 separate from measurement uncertainty: agreement within an uncertainty region does not by itself validate a model.

Fit only identifiable parameters. For our resonator, a power spectrum fixes the sum of halfwidths and their product but cannot label which is internal or external. A complex response, known reference plane and additional physical information resolve more than a magnitude-only fit. Report parameter covariance and test residual structure on frequencies or samples excluded from fitting.

| Independent check | What it establishes here | What remains untested |
| --- | --- | --- |
| Resonator power balance and independent coupled-mode amplitude | Algebra and passivity of the declared model | Real patch response and additional channels |
| Fourth standard Γ = i | Calibration inversion outside the three fitted standards | Accuracy of actual calibration artifacts |
| Phase reversal and frequency slope | Sign and round-trip factor | Actual sample placement and fixture response |
| Derivative refinement and Monte Carlo comparison | Local tolerance propagation | Real manufacturing distributions |
| Independent radial probability integration | 2D Gaussian ellipse threshold | Exact coverage for a nonlinear experiment |

The [lab](../labs/09-measurement-lab.md) includes six explicitly unexecuted extensions: measured material fitting, fabricated-geometry import, nonideal standards, free-space angular/polarization collection, optical power/phase measurement, and blind simulation-to-measurement comparison. These are suitable student contributions through the existing pull-request workflow. The executed baseline remains reproducible without a laboratory.

**Pause and explain:** why can two measurements have equal reflectance but disagree in phase? Why can positive correlation worsen a fabrication tolerance? Why is perfect recovery of the calibration standards insufficient? Answer before opening the worked solutions.
