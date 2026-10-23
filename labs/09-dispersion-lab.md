---
title: 'ms-09: Spectral sweeps and bandwidth metrics'
short_title: Spectral bandwidth lab
---

# ms-09: Spectral sweeps and bandwidth metrics

**Chapters 2 and 5.** A good beam deflector at one wavelength can lose efficiency or send light in the wrong direction nearby. Predict which requirement limits its useful band, then test the fixed Chapter 5 geometry.

**Executed:** 161 wavelengths, two harmonic resolutions, three spectral grids, target efficiency, angular acceptance and modal group delay. Constant real indices isolate structural dispersion; measured material dispersion, absorption and finite apertures are outside this model.

## What are we simulating?

```{figure} ../assets/chapter-05/supercell-geometry.svg
:alt: Six unequal dielectric ridges, repeated as a supercell, with TE illumination and two phase reference planes.

The six-ridge sequence repeats every 3.9 µm. Height is 1.8 µm, pitch 0.65 µm and ridge index 2.4; y is invariant. Gaps and the incident region contain air; substrate index is 1.5. This exact geometry stays fixed throughout the sweep.
```

Use normal incidence, electric field along y and time dependence exp(−iωt). Reference reflection to z=0 and transmission to z=h. Sweep **vacuum wavelength**, keeping widths, pitch, height and indices fixed. Redesigning a different cell for each wavelength does not demonstrate a single broadband device.

## Explore, then run

<iframe src="../interactives/design-studies.html?lab=dispersion" title="Spectral bandwidth and geometry explorer" width="100%" height="1650" loading="lazy" style="border:0;border-radius:14px"></iframe>

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/design-studies.html?lab=dispersion" target="_blank" rel="noopener">Open the browser lab in a new tab</a> · [Executed notebook](../notebooks/09-dispersion.ipynb) · [Complete source bundle](../downloads/design-studies.zip)

The browser selects saved calculations. Extract the complete ZIP, preserve folders, install `requirements-labs.txt` in Python 3.12, launch JupyterLab and restart/run `notebooks/09-dispersion.ipynb`. Physical inputs, performance requirements and numerical controls are separate parameters. One BLAS thread is efficient for these small matrices.

## Define the metric first

For incident-normalized TE power and the target angle at normal incidence:

$$
T_{+1}=\frac{\operatorname{Re}q_{t,+1}}{q_{i,0}}|t_{+1}|^2,\quad q=k_z/k_0,\qquad
\theta_{+1}=\sin^{-1}\!\left(\frac{\lambda}{n_t L}\right).
$$

The **efficiency band** requires T₊₁≥0.8. The **useful band** also requires |θ₊₁(λ)−θ₊₁(1.55 µm)|≤0.5°. Choose the connected passing interval containing 1.55 µm. Interpolate its threshold crossings and flag edges clipped by the scan. Report Δλ, Δλ/λ₀ and frequency width:

$$
\Delta f=c\left(\lambda_{\rm low}^{-1}-\lambda_{\rm high}^{-1}\right).
$$

Total transmission and T₊₁/ΣTₘ answer different questions; neither replaces incident-normalized efficiency. A threshold band is distinct from resonance FWHM. The substrate's m=±4 orders reach grazing at 1.4625 µm. The grid avoids this exact singular point and records the changing open-channel count.

## Investigation sequence

1. **Predict:** explain why angle and complex response vary even with constant refractive indices.
2. **Sweep:** compare target efficiency, total transmission and angle over 1.36–1.74 µm. Identify which requirement sets each useful-band edge.
3. **Resolve:** compare 41, 81 and 161 samples at the same harmonic resolution. Report edge changes rather than unsupported decimal places. Do not merge disconnected passing windows.
4. **Refine independently:** compare M=96/144 at every wavelength. Small power-balance error does not replace refinement. Narrow features can require further spectral and harmonic resolution.
5. **Differentiate:** for exp(−iωt), compute τ=d arg(t₊₁)/dω. Sort frequency, unwrap phase, mask weak transmission and neighboring derivative stencils, and compare 81/161-point derivatives. This is modal delay at fixed faces, not detector arrival time; power convergence does not guarantee derivative convergence.
6. **Change the requirement:** repeat with another threshold or angular tolerance while preserving the device.

## Deliverable and extensions

Submit the geometry, editable notebook, original plots, both bandwidth definitions, edge/clipping reports, spectral/harmonic sensitivity and model limits. Run all three new notebooks, then `python scripts/validate_design_studies.py` for the fixed published-reference audit. It does not certify arbitrary edited designs.

**Further outline:** add a documented causal dispersive material model and check its range, passivity and absorption. Finite-aperture spectra, multiwavelength optimization, independent FEM/FDTD and measured-device bandwidth remain extensions.

## Sources and next lab

Use [Chapter 2](../chapters/02-waves-and-interfaces.md) for flux and phase conventions and [Chapter 5](../chapters/05-metasurface-synthesis.md) for the design. The Fourier method is discussed by [Moharam and Gaylord](https://opg.optica.org/josa/abstract.cfm?uri=josa-71-7-811). Our calculations and figures are original. Follow the [source and reuse guide](../attribution.md).

Next: [ms-10, independent cells versus a supercell](10-coupling-lab.md).
