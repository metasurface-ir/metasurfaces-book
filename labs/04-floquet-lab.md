---
title: 'Lab 4: Which Diffraction Orders Can Propagate?'
short_title: Floquet computational lab
---

# Lab 4: Which Diffraction Orders Can Propagate?

**Topic ID:** `ms-04-floquet-orders`

**Companions:** [Chapter 4](../chapters/04-periodic-floquet.md) and [worked examples](../chapters/04-floquet-guide.md).

**Question:** how do period, wavelength, incidence, and exterior refractive index determine the outgoing channels, and how should those channels be used in a full-wave calculation?

**Executed amplitude calculation:** the [Chapter 3 lab](03-unit-cell-lab.md) now supplies a restricted TE ridge solver with flat-interface/film limits, multiorder checks, and a validated response library. The specific solver exercises outlined later on this page remain extension briefs.

The [Chapter 5 lab](05-synthesis-lab.md) additionally computes all-channel powers for four complete six-ridge TE supercells, connecting the channel map to actual beam steering. Its geometry differs from the grating and COMSOL briefs below.

## A. Explore in your browser

Use the controls below to predict and reveal transmitted and reflected channel sets. The ray directions show allowed channels with equal visual emphasis; their lengths and colors do not encode power. Closed orders appear in the table rather than as outgoing rays.

:::{iframe} ../interactives/floquet-explorer.html
:width: 100%
:class: floquet-explorer-frame
:title: Interactive Floquet channel explorer

An analytical explorer for a one-dimensional periodic surface in isotropic lossless exterior media. It runs locally in the browser without a solver or external scripts.
:::

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/floquet-explorer.html" target="_blank" rel="noopener">Open the browser lab in a new tab</a>

Before moving a control, write down the change you expect. Try the six-element, smaller-period, glass-output, and exact-cutoff presets. Apply the propagation test separately on the incident and transmitted sides. Explain an asymmetric order set at oblique incidence.

**Deliverable:** a parameter table and three predictions checked against the explorer: one supercell case, one medium-dependent case, and one opening/closing transition.

## B. Execute the analytical notebook

**Available:** [the executed notebook](../notebooks/04-floquet-orders.ipynb). Download its editable source: {download}`../notebooks/04-floquet-orders.ipynb`. It contains its functions and data generation, needs no electromagnetic solver, and uses NumPy and Matplotlib. Optional sliders run in Jupyter with ipywidgets; the web explorer above is already interactive in the browser.

### Parameters and assumptions

| Parameter | Reference value | Meaning |
| --- | --- | --- |
| Period $\Lambda$ | $3\,\mu\mathrm m$ | Full structural repeat along $x$ |
| Wavelength $\lambda_0$ | $1.55\,\mu\mathrm m$ | Free-space wavelength |
| Incidence $\theta_i$ | $0^\circ$ | Signed angle; incidence in the $x$-$z$ plane |
| Incident/output indices | 1 and 1 | Positive real exterior refractive indices |
| Cutoff tolerance | $10^{-10}$ | Tolerance on $|q_m/n_o|-1$ |
| Additional plotted neighbors | 2 | Closed orders beyond a conservative complete channel interval |
| Incidence sweep | $-70^\circ$ to $70^\circ$ | Analytical channel-count map |
| Wavelength sweep | $0.6$ to $3.6\,\mu\mathrm m$ | Analytical channel-count map |
| Finite array sizes | 8, 24, 64 | Prescribed scalar-source array factors |

Conventions are $e^{-i\omega t}$, $e^{i\mathbf k\cdot\mathbf r}$, incidence from $z<0$, and $k_{x,m}=k_{x,i}+2\pi m/\Lambda$. The introductory model has $k_y=0$; a separate rectangular-lattice example introduces both tangential components.

### Procedure

1. Derive the Bloch multiplier and the open-order interval. Predict the reference result before running the cells.
2. Execute the notebook from a fresh kernel. Inspect the signed angles, grazing classification, outgoing square-root branch, and automatic order enumeration.
3. Compare air and glass output regions. Repeat the oblique microwave example and calculate the phase advance independently.
4. Locate a cutoff analytically, then evaluate just below, at, and just above it. Use perturbations larger than the classification tolerance.
5. Inspect the angle/wavelength channel-count map. Explain its transition boundaries without reading them as efficiency bands.
6. Check TE Fresnel power normalization at a flat interface, including a total-internal-reflection case. Explain why the nonzero supercell orders have zero amplitude there.
7. Compare finite-array factors for three lengths. Connect their peak locations to Floquet angles and their finite widths to aperture length.
8. Run the rectangular-lattice example and identify why a test using only $k_x$ could misclassify an order with nonzero $k_y$.
9. Optionally set `ENABLE_WIDGETS=True` and rerun the notebook in Jupyter to use its sliders. Saved reference outputs use this flag as `False` so the book can display its calculations independently of a live kernel.

### Evidence and acceptance

Submit the executed notebook, environment, edited parameters, reference channel sets, cutoff tests, two figures, and a short interpretation. Analytical assertions must pass. Closed channels must not acquire fabricated real angles; enumeration must include all potentially open orders; and reflected evanescent waves must decay in the outward direction rather than grow.

The numerical tolerance classifies a known analytical boundary. Changing it is not a substitute for converging a Maxwell solver. The notebook's scalar array-factor plot must not be reported as a simulated diffraction efficiency.

## C. Full-wave validation outline

**Status:** detailed outline; no full-wave model has been executed for this chapter.

**Preparation:** unit-cell geometry and numerical-convergence methods from Chapters 3 and 6. Use a solver available to the contributor and document its version and license requirements where applicable. A finite-element solver, RCWA implementation, or an appropriate FDTD setup can be used.

### C1. Begin with a flat-interface benchmark

1. Use a homogeneous cell or flat interface with known TE Fresnel coefficients. Record exterior indices, wavelength, angle, polarization, units, and reference planes.
2. Assign a computational period that permits several channel labels, for example $3\,\mu\mathrm m$ at $1.55\,\mu\mathrm m$. Predict the open set on each side analytically.
3. Apply lateral Bloch conditions consistent with the translated incident field. Use the correct outgoing modal basis or absorbing-boundary/flux treatment.
4. Compare specular amplitude and power with Fresnel theory. Verify that other listed open orders have negligible amplitude to the declared numerical tolerance.
5. Sweep incidence through a safely resolved range and compare the tangential wavevector sign and order labels. Include total internal reflection if the incident medium permits it.

**Acceptance:** numerical error decreases under refinement; the predeclared amplitude and power tolerances are met; non-specular leakage is explained; and the incident excitation remains correctly normalized. This benchmark tests the solver setup before adding patterned geometry.

### C2. Add a simple dielectric grating

Use a two-dimensional ridge grating as a manageable starting model. A suggested geometry has period $0.80\,\mu\mathrm m$, ridge width $0.40\,\mu\mathrm m$, height $0.30\,\mu\mathrm m$, ridge index 2, substrate index 1.5, and air above. Specify which side is illuminated; for the analytical cutoff comparison here, use incidence from air at $\lambda_0=1.55\,\mu\mathrm m$ and examine both exterior media.

1. Declare the geometry, material assumptions, excitation, target observables, and convergence tolerances before the sweep.
2. Predict every open channel across $0^\circ$ to $75^\circ$ incidence. The first negative order reaches grazing near $25.94^\circ$ in the index-1.5 region and $69.64^\circ$ in air. Treat the exact thresholds separately.
3. Include the full required propagating basis at every angle, including modes that become open only late in the sweep. Preserve closed harmonics needed for accurate field matching.
4. Refine at least three discretization levels for representative angles, especially resonances and neighborhoods on both sides of each cutoff. If needed, move ports farther into homogeneous regions and refine absorbing layers or harmonic truncation independently.
5. Save complex order amplitudes, order-resolved powers, total reflected/transmitted flux, and any absorption. Compare the sum of modal powers with an independent flux evaluation where available.
6. Check that the calculated beam directions agree with the analytical channel map. Inspect how the powers change as the channels open; do not prescribe their values from the channel condition.

**Acceptance:** a declared convergence criterion passes for individual observables, not only total power; modal labels are mapped to physical tangential wavevectors; all propagating channels are accounted for; and failures are retained in the report. A small conservation residual alone does not establish correct order partitioning or phase.

### C3. Optional six-post beam deflector

Use the official [COMSOL reference model](https://www.comsol.com/model/metasurface-beam-deflector-115971) or a contributor's independently documented implementation. Its six distinct Si posts at $500\,\mathrm{nm}$ pitch make a $3\,\mu\mathrm m$ repeat. The reference uses SiO2 support and a $1.55\,\mu\mathrm m$ design wavelength.

Compare an identical-post sequence, the designed sequence, and its reversed sequence. Keep period, illumination, and output normalization explicit. Plot field wavefronts and power in every propagating order. At normal incidence into air, first-order angles have magnitude about $31.1^\circ$; the calculation does not determine the favored sign or efficiency. Test those quantities with the solver rather than assigning the external model's results to a new geometry.

The application is three-dimensional. Its transverse period and the possibility of nonzero transverse orders must be checked with the two-dimensional lattice condition. A one-dimensional introductory diagram is insufficient evidence for a complete 3D port basis.

## Full-wave contribution package

| Item | Minimum content |
| --- | --- |
| Reproducible setup | Solver/version, geometry-generation instructions, materials, boundaries, excitation, reference planes |
| Channel manifest | Order labels, tangential wavevectors, side, polarization, and open/cutoff/closed classification |
| Numerical evidence | Refinement settings, per-order complex/power errors, flux checks, and failed cases |
| Results | Field plots, signed diffraction angles, order-resolved powers, and all-channel accounting |
| Interpretation | What was verified analytically, what was simulated, and what still needs a device-level or experimental check |

Use the [contribution guide](../contributing.md) and keep the solver files or archived-data links traceable to a version. A useful focused student contribution is the flat-interface benchmark, one converged ridge-grating sweep, or a carefully explained cutoff figure. The analytical notebook and browser explorer provide reusable reference tests for those contributions.
