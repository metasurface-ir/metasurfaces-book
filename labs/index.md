# Computational investigations

The identifiers below preserve the existing course handoff, with a new AI investigation for Chapter 10. Chapter 1 provides an executed analytical introduction and a browser explorer. Chapter 2 adds executed planar interface/film/sheet and Jones models with a four-view browser explorer. Chapter 3 includes an executed full-wave TE ridge library and a browser data explorer. Chapter 4 includes an executed analytical notebook and a browser explorer. Chapter 5 verifies four full-wave supercells and adds separate scalar focusing/Jones notebooks. Chapter 6 adds an executed FDFD slab benchmark, error/field plots and a bilingual diagnostic explorer. The AI pilot includes two executed analytical notebooks. Further lab stages state their individual execution status. Chapters organize subject matter, while labs organize computational activities.

| Topic ID | Investigation | Related chapter(s) |
| --- | --- | --- |
| ms-01-waves-interfaces | [Waves, interfaces, TIR fields, antireflection, and polarization](02-waves-lab.md) | 2 |
| ms-02-scattering | [First analytical sheet investigation: channel balance, phase, power, and model limits](01-first-investigation.md) | 1, 2 |
| ms-03-sheet-response | [Electric-sheet response, coherent absorption, and guarded algebraic retrieval](02-waves-lab.md) | 2, 5 |
| ms-04-floquet-orders | [Floquet channels: browser explorer, analytical notebook, and full-wave validation outline](04-floquet-lab.md) | 4 |
| ms-05-beam-steering | [Ideal/sampled/local/full-wave beam steering with four verified supercells](05-synthesis-lab.md) | 5 |
| ms-06-polarization | [Executed analytical Jones matrices, rotated elements, geometric phase](05-synthesis-lab.md) | 2, 5 |
| ms-07-unit-cell | [Validated TE ridge library: full-wave notebook, browser explorer, and extension outlines](03-unit-cell-lab.md) | 3, 6 |
| ms-08-metalenses | [Executed scalar line-focus propagation and metrics; finite full-wave outline](05-synthesis-lab.md) | 5 |
| ms-09-dispersion | [Spectral sweeps and bandwidth metrics](09-dispersion-lab.md) | 2, 5 |
| ms-10-coupling | [Independent-cell versus supercell predictions](10-coupling-lab.md) | 3, 6 |
| ms-11-inverse-design | [Bounded optimization with independent checks](11-inverse-design-lab.md) | 5, 6, 10 |
| ms-12-research-project | [Reproducible project brief and evidence rubric](12-research-project.md) | 7, 8, 9, 10 |
| ms-13-ai-metasurfaces | [Learn, design, and verify: analytical starter and full-wave lab outlines](13-ai-metasurfaces.md) | 10 |
| ms-14-numerical-validation | [Mesh, domain, boundaries, reference planes and numerical evidence](06-numerical-lab.md) | 3, 5, 6 |
| ms-15-tunable-control | [Bias tuning, programmed arrays, feedback and temporal harmonics](07-tunable-lab.md) | 7 |
| ms-16-communications | [Aperture geometry, link budget, bandwidth and training](08-communications-lab.md) | 2, 5, 6, 7, 8 |
| ms-17-measurement | [Materials, fabrication tolerances, calibration and uncertainty](09-measurement-lab.md) | 2, 3, 6, 9 |

Chapter 7 adds an executed effective circuit, scalar array, synthetic calibration and driver/envelope model with independent checks.
## Start with an analytical investigation

The [Chapter 1 lab](01-first-investigation.md) starts with predictions and an browser explorer, then supplies an executed notebook and complete source bundle. It illustrates complex responses, effective electric-like/magnetic-like channels, reflected cancellation, transmission zeros, and spectral phase. Its analytical consistency checks are distinct from full-wave geometry validation.

## Available synthesis investigation

The [Chapter 5 lab](05-synthesis-lab.md) connects unit-cell phase coverage with actual order-resolved powers from a repeated six-ridge TE geometry. It preserves local-mask predictions and lower-performing designs as comparisons. A second executed notebook develops scalar line focusing and ideal Jones-matrix polarization control, with explicit model boundaries. The linked ms-09/10/11 labs now execute spectral sweeps, local-versus-supercell comparisons and bounded optimization. Finite-device, independent-method and robust optimization stages remain outlines.

## Available unit-cell investigation

The [Chapter 3 lab](03-unit-cell-lab.md) computes a 50-width dielectric ridge library using an original restricted TE RCWA solver. Analytical film limits, harmonic convergence, multiorder checks, and a separate grcwa implementation comparison accompany the data. Use the browser explorer to inspect the saved responses and reject unattainable phase targets. Download the complete source bundle to rerun or extend the notebook. The linked ms-10 lab now executes supercell comparisons. Further height sweeps and FEM/FDTD comparisons remain outlines.

## Available Floquet investigation

**Floquet orders: Which beams can leave a metasurface?** Work through the [Chapter 4 lab](04-floquet-lab.md), [chapter](../chapters/04-periodic-floquet.md), and [executed notebook](../notebooks/04-floquet-orders.ipynb). The analytical part maps allowed orders versus period, wavelength, incidence angle, and refractive index. The full-wave comparison remains an outline. An allowed order does not determine its power or efficiency.

This investigation follows the existing companion lesson draft and preserves its sign convention and reference examples.

### Reference conventions

Use the handoff conventions: time dependence exp(-i omega t), spatial dependence exp(i k dot r), periodicity along x, and ky = 0. The introductory model assumes homogeneous, isotropic, lossless media with positive refractive indices.

For vacuum wavelength lambda0 and period Lambda, use k0 = 2 pi / lambda0 and kx,m = ni k0 sin(theta_i) + 2 pi m / Lambda. Classify an order as open when abs(kx,m) < no k0, at grazing cutoff when equal, and closed when greater. Use a documented numerical tolerance around cutoff.

The first analytical check uses normal incidence, Lambda = 3 micrometers, lambda0 = 1.55 micrometers, and output index no = 1. The expected open orders are -1, 0, and +1, with first-order angles approximately +/-31.1 degrees. This checks channel geometry only; it provides no simulated efficiency.

Expose wavelength, period, incidence angle, refractive indices, order range, and cutoff tolerance. Include sweeps and analytic checks before adding any full-wave comparison.

## Continue across the developed chapters

Work through [ms-09: bandwidth](09-dispersion-lab.md), [ms-10: local cells and supercells](10-coupling-lab.md), then [ms-11: bounded inverse design](11-inverse-design-lab.md). Each has a full executed notebook, original plots, geometry-linked browser views and a Python-source bundle. The browser labs open in a new tab; downloads contain notebooks, code and data.
