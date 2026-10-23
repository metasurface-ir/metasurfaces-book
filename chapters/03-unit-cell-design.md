---
title: 'Chapter 3: Unit-cell Design and Simulation'
short_title: Unit-cell design
description: Compute complex unit-cell responses, preserve phase references, verify numerical convergence, and build a reusable dielectric response library.
---

# Chapter 3: Unit-cell Design and Simulation

**Central question:** how can a geometry become a trustworthy entry in a metasurface design library?

Suppose a design calls for a transmitted phase of $-100^\circ$ and at least 80% transmitted power. A width sweep produces many colorful phase values. Which geometry should you choose? Before choosing, establish what field was normalized, where its phase was measured, which outgoing channels were included, and whether increasing numerical resolution changes the answer.

This computational chapter builds that chain of evidence. It follows the [Floquet conventions of Chapter 4](04-periodic-floquet.md), then calculates the amplitudes those channels carry. The [worked examples](03-unit-cell-guide.md), [lab and browser explorer](../labs/03-unit-cell-lab.md), and [executed notebook](../notebooks/03-unit-cell-library.ipynb) share one original Python solver and one exported dataset.

:::{note} Evidence available
The reference run is a full-wave, frequency-domain calculation for a **one-dimensional dielectric ridge grating under TE illumination**. It includes analytical interface/film checks, harmonic refinements, a separate grcwa implementation comparison, near-field reconstruction, and 50 accepted library entries. A two-dimensional lattice of posts, a finite metasurface, TM polarization, material dispersion, and fabrication are outside this reference model. Additional FEM/FDTD and supercell investigations are prepared as lab extensions.
:::

## 3.1 Outcomes and prerequisites

After completing the investigation, you should be able to:

1. Specify geometry, materials, illumination, periodicity, and reference planes unambiguously.
2. Extract complex reflection/transmission and convert field amplitudes into power.
3. Explain a Fourier-modal unit-cell calculation and its numerical truncation.
4. Distinguish algebraic residuals, conservation checks, and numerical convergence.
5. Export a versioned response library and select a geometry with explicit feasibility criteria.
6. Identify when a periodic-cell prediction needs a supercell or finite-device test.

Prerequisites are Maxwell boundary conditions, phasors, Fresnel coefficients, Fourier series, eigenvectors, and basic Python. Reading Sections 4.1–4.7 first provides the channel geometry. [Chapter 1](01-metasurface-foundations.md) and [Chapter 2](02-waves-and-interfaces.md) supply the earlier foundation.

## 3.2 Define the electromagnetic experiment

A unit cell describes a structure repeated indefinitely under a specified Bloch excitation. Its response includes interactions with that repeated environment. When every ridge width changes, the entire periodic environment changes along with it.

The reference cell has a ridge centered at $x=0$, width $w$, height $h$, period $\Lambda$, and invariance along $y$. The layer occupies $0<z<h$. Air lies above it at $z<0$ and a homogeneous substrate below at $z>h$. Illumination travels toward positive $z$.

| Quantity | Reference value | Role |
| --- | --- | --- |
| $\Lambda$ | $0.65\,\mu\mathrm m$ | Repeat along $x$ |
| $w$ | $0.08$–$0.57\,\mu\mathrm m$ | Swept ridge width, 50 samples |
| $h$ | $0.60\,\mu\mathrm m$ | Fixed patterned-layer thickness |
| $\lambda_0$ | $1.55\,\mu\mathrm m$ | Free-space wavelength |
| $n_r$, $n_g$ | 2.4, 1.0 | Ridge and gap indices |
| $n_i$, $n_t$ | 1.0, 1.5 | Incident medium and substrate |
| $\theta_i$ | $0^\circ$ | Reference incidence |
| Polarization | TE, $\mathbf E=\hat{\mathbf y}E_y$, $k_y=0$ | Scalar Maxwell reduction |

All indices are positive, real, constant, and nonmagnetic. They define an ideal dielectric model without assigning measured material properties. A research library should use a stated dispersion model and measured or otherwise justified optical constants.

We use $e^{-i\omega t}$ and $e^{i\mathbf k\cdot\mathbf r}$. The incident $E_y$ equals one at $z=0$; reflected coefficients are referenced to $z=0$ and transmitted coefficients to $z=h$. Keeping these two reference faces fixed makes the width comparison meaningful.

## 3.3 Choose a solver that matches the structure

| Method | Natural use | Numerical controls to vary |
| --- | --- | --- |
| Fourier modal / RCWA | Laterally periodic structures represented as uniform layers along the propagation direction | Fourier harmonics; geometric/material representation; layer slicing for a varying vertical profile |
| Finite elements | Complex shapes, material interfaces, frequency-domain fields | Mesh, polynomial order, exterior boundaries/ports |
| FDTD | Broadband time-domain response and spatially resolved fields | Spatial grid, run time/decay, PML, source/monitor placement |

The course implementation is a restricted RCWA calculation: one rectangular patterned layer with exact Fourier coefficients. Its vertical eigenmode propagation is analytic, so there is no finite-difference $z$ mesh or staircased height to refine. The main truncation is the number of spatial harmonics. A sloped sidewall or vertically varying cell would need additional layers or another solver.

The [Meep grating and mode-decomposition tutorials](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/) provide a useful later FDTD comparison, including flux normalization and phase references. The [grcwa documentation](https://grcwa.readthedocs.io/en/latest/usage.html) describes the separate RCWA implementation used in our numerical audit. Solver conventions must be mapped before comparing signs and amplitudes.

## 3.4 Channels, complex amplitudes, and power

For retained integer orders $m=-M,\ldots,M$, define

$$
\alpha_m=\frac{k_{x,m}}{k_0}=n_i\sin\theta_i+m\frac{\lambda_0}{\Lambda},\qquad
q_{o,m}=\sqrt{n_o^2-\alpha_m^2}.
$$

The outgoing root has nonnegative real and imaginary parts. A positive real $q$ gives a propagating channel; a positive imaginary $q$ gives outward decay. At exact cutoff $q=0$, this implementation requests a parameter perturbation rather than using a singular grazing basis.

The exterior expansions are

$$
E_y^{(i)}(x,z)=e^{ik_0(\alpha_0x+q_{i,0}z)}+
\sum_m r_m e^{ik_0(\alpha_mx-q_{i,m}z)},\quad z<0,
$$

$$
E_y^{(t)}(x,z)=\sum_m t_m e^{ik_0[\alpha_mx+q_{t,m}(z-h)]},\quad z>h.
$$

For these **electric-field** TE amplitudes, the order powers relative to incident normal flux are

$$
R_m=\frac{\operatorname{Re}q_{i,m}}{q_{i,0}}|r_m|^2,\qquad
T_m=\frac{\operatorname{Re}q_{t,m}}{q_{i,0}}|t_m|^2.
$$

Closed exterior orders have zero normal outgoing power in these lossless half-spaces. Sum every open order to obtain $R$ and $T$. For this lossless model, $R+T=1$ to numerical accuracy. With absorption in a more general solver, the missing fraction requires a consistent dissipated-power calculation.

At the library reference parameters, $\lambda_0/\Lambda\approx2.385$, exceeding both exterior indices. Only $m=0$ is open, so $T=1.5|t_0|^2$ and $R=|r_0|^2$. If period, wavelength, or angle changes, enumerate the channels again. A zeroth-order library becomes incomplete when other orders open.

For an open zeroth-order channel, the power-normalized coefficient is $S_{21}=\sqrt{q_{t,0}/q_{i,0}}\,t_0$. Record whether a solver exports this quantity or an electric-field ratio. Reciprocity comparisons require compatible normalization, channel directions, reference planes, and the appropriate reversal of transverse wavevectors.

## 3.5 Derive the restricted TE Fourier model

For a nonmagnetic scalar permittivity and $E_y(x,z)$,

$$
\frac{\partial^2E_y}{\partial x^2}+\frac{\partial^2E_y}{\partial z^2}+k_0^2\epsilon_r(x)E_y=0.
$$

Write $E_y=\sum_m E_m(z)e^{ik_0\alpha_mx}$ and expand $\epsilon_r(x)$ as a Fourier series. Projection onto the retained harmonics gives

$$
\frac{d^2\mathbf E}{dz^2}+k_0^2(\boldsymbol\epsilon-\mathbf A^2)\mathbf E=0,
\qquad \epsilon_{mn}=\epsilon_{m-n},\quad A_{mn}=\alpha_m\delta_{mn}.
$$

For a centered rectangle with fill fraction $f=w/\Lambda$,

$$
\epsilon_\ell=n_g^2\delta_{\ell0}+(n_r^2-n_g^2)f\,\operatorname{sinc}(\ell f),
\qquad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

These coefficients are analytic, including the $\ell=0$ limit. There is no pixel grid in the course solver. The matrix is Hermitian for these real-index materials, and its eigenproblem is

$$
(\boldsymbol\epsilon-\mathbf A^2)\mathbf W=\mathbf W\mathbf Q^2.
$$

The square roots in $\mathbf Q$ again use nonnegative real/imaginary branches. The derivative-mode matrix is $\mathbf V=\mathbf W\mathbf Q$. To avoid exponentially growing transfer factors, define forward coefficients $\mathbf a$ at the top face and backward coefficients $\mathbf b$ at the bottom face:

$$
\mathbf E(z)=\mathbf W\left[e^{ik_0\mathbf Qz}\mathbf a+
e^{ik_0\mathbf Q(h-z)}\mathbf b\right],\qquad
\mathbf P=e^{ik_0\mathbf Qh}.
$$

Continuity of $E_y$ and its normal derivative, for common permeability, yields

$$
\begin{bmatrix}
\mathbf V+\mathbf Q_i\mathbf W & (\mathbf Q_i\mathbf W-\mathbf V)\mathbf P\\
(\mathbf V-\mathbf Q_t\mathbf W)\mathbf P & -\mathbf V-\mathbf Q_t\mathbf W
\end{bmatrix}
\begin{bmatrix}\mathbf a\\\mathbf b\end{bmatrix}
=\begin{bmatrix}2\mathbf Q_i\mathbf e_0\\\mathbf 0\end{bmatrix}.
$$

Here $\mathbf Q_i$ and $\mathbf Q_t$ are diagonal exterior matrices and $\mathbf e_0$ excites order zero. Recover

$$
\mathbf r=\mathbf W(\mathbf a+\mathbf P\mathbf b)-\mathbf e_0,
\qquad \mathbf t=\mathbf W(\mathbf P\mathbf a+\mathbf b).
$$

The code implements these equations in `solve_cell`. Its `sample_ey` function reconstructs fields inside and outside the ridge layer. `film_reference` supplies a separate scalar Fresnel/Fabry-Perot benchmark. See [Moharam and Gaylord's foundational formulation](https://doi.org/10.1364/JOSA.71.000811) for the broader RCWA method.

:::{warning} Polarization is part of the formulation
This TE reduction uses a continuous tangential electric field at the vertical dielectric interfaces. Changing the input label to TM does not implement TM Maxwell equations or the required Fourier treatment of discontinuous material products. A general vector solver needs its own formulation and convergence evidence.
:::

```{figure} ../assets/chapter-03/fields.png
:alt: Real TE electric field and squared field amplitude around three repeated dielectric ridges.

Original full-wave field reconstruction for the central cell. Outgoing evanescent harmonics contribute to the near field. The squared field amplitude is distinct from power and energy density.
```

## 3.6 Extract phase at stated reference planes

A phase is meaningful relative to an excitation and a plane. Suppose an incident monitor is $L_i$ above the ridge and an output monitor $L_t$ below it. If both measured ratios use incident $E_y$ at $z=-L_i$, then

$$
r_{\rm mon}=r\,e^{2ik_0q_iL_i},\qquad
t_{\rm mon}=t\,e^{ik_0(q_iL_i+q_tL_t)}.
$$

Removing these homogeneous propagation phases returns the two face-referenced coefficients. The notebook tests this algebra with synthesized monitor offsets; the RCWA calculation itself matches directly at the two interfaces.

The wrapped phase $\arg t$ jumps at $\pm180^\circ$. For a smooth parameter sweep, phase unwrapping can reveal the continuous path. The path can be misleading near $|t|=0$, where phase is poorly defined and numerical noise becomes dominant. Keep amplitude beside every phase plot and use a stated amplitude/power threshold for design.

For comparing a response with a desired phase, use the circular difference

$$
\Delta\phi=\arg\left[t\,e^{-i\phi_\star}\right].
$$

The direct subtraction $179^\circ-(-179^\circ)$ gives $358^\circ$, while their circular separation is $2^\circ$. For a change in height, even a bare homogeneous propagation path changes phase. Define a common physical comparison plane or a clearly stated background reference before attributing that change entirely to the ridge response.

## 3.7 Validate before exporting

Three questions require separate evidence:

| Question | Check | Limitation |
| --- | --- | --- |
| Was the truncated linear system solved? | Relative algebraic residual | Does not assess harmonic truncation |
| Is power accounted for? | All-channel $|1-R-T|$ | A conservative truncated model can still predict inaccurate amplitudes |
| Does numerical refinement change the response? | Complex-amplitude, power, and meaningful phase changes with $M$ | Agreement of finite truncations is an empirical test, not a rigorous error bound |

The reference investigation passes 18 analytical interface/uniform-film cases. At normal incidence with $h=0$, it returns $r=-0.2$, $t=0.8$, $R=0.04$, and $T=0.96$. A larger artificial period gives additional open labels with zero amplitudes at that flat interface.

For every width, the library compares $M=24$ with $M=32$: 49 versus 65 harmonics. It requires $|\Delta t|<5\times10^{-4}$, changes in $R$ and $T$ below $5\times10^{-4}$, a circular phase change below $0.05^\circ$, and power residual below $10^{-8}$. The saved run's worst $|\Delta t|$ is about $6.59\times10^{-6}$. Six additional points are checked at $M=48$.

The audit also tests reflected/transmitted order sets at oblique incidence, mirror-related order powers, input guards, and reconstructed field continuity. Eight cases are compared against grcwa at matching harmonic count, while its independent raster representation is refined from 256 to 2048 samples. At the fine raster, the largest complex zeroth-order transmission difference is below $8\times10^{-7}$. Both codes use RCWA; a comparison using FEM/FDTD and any experimental validation remain future work.

The notebook's spectral-neighborhood plot provides an exploratory illustration at fixed harmonic order. Its wavelengths are outside the exported single-wavelength library domain and require their own convergence studies before library acceptance.

## 3.8 Build a response library a colleague can reuse

A useful record preserves more than width and phase:

- **Experiment:** geometry, units, material model, wavelength, angle, polarization, and primitive period.
- **Response:** complex amplitudes, order labels, total and order-resolved powers where necessary, and phase reference planes.
- **Evidence:** solver/source version, environment, numerical controls, refinement changes, residuals, and acceptance thresholds.
- **Scope:** supported parameter domain, excluded physics, and known incomplete design coverage.

The reference JSON combines this metadata with the 50 rows; its CSV is convenient for plotting and later model fitting. The width in each row overrides the illustrative central width in the metadata. Preserve different experiments as versioned datasets rather than merging rows with incompatible references.

```{figure} ../assets/chapter-03/library.png
:alt: Transmission and reflection versus ridge width, wrapped and unwrapped transmission phase, and the complex transmission trajectory.

The computed width sweep spans about $132.04^\circ$ continuously. This height and width range do not provide complete $360^\circ$ coverage, even before imposing a minimum transmission requirement.
```

## 3.9 Select a geometry with a feasibility test

For this first design exercise, retain accepted rows with $T\geq0.8$ and minimize the absolute circular phase error. A request is feasible only when that error is at most $5^\circ$.

The saved library supplies a width near $0.24\,\mu\mathrm m$ for a target of $-100^\circ$, with $T\approx0.865$ and phase error about $0.50^\circ$. A target of $0^\circ$ remains unmet under the same criteria; the closest eligible row misses by about $43.73^\circ$. Report this result directly. Expanding the height range, changing the geometry, or revising the objective would define a subsequent design investigation.

Interpolating a response library requires additional checks. Interpolate real/imaginary parts or another representation respecting phase periodicity; verify new geometries with the solver, especially near rapid response changes. For Chapter 10, separate geometry groups before splitting data and retain numerical uncertainties. Fifty related samples at one wavelength are a teaching dataset, with no claim about general AI performance.

## 3.10 From a periodic library to a real device

A local-periodicity approximation assigns a cell the response it would have in an infinite array of identical neighbors. A wavefront-shaping device places different geometries next to one another. Their coupling and collective diffraction can alter the response.

Before claiming device efficiency, assemble an appropriate supercell or finite structure, include its actual outgoing channels, and compare its scattering with the library-based prediction. Sharp gradients, resonant near fields, aperture edges, and rapidly changing neighboring geometries deserve particular attention. An element library is an input to that test, rather than a completed beam-deflector simulation.

For a research cell, add physical material dispersion, relevant loss, geometric tolerances, and solver checks appropriate to the chosen fabrication geometry. [Chapter 4](04-periodic-floquet.md) supplies channel bookkeeping; [Chapter 5](05-metasurface-synthesis.md) develops synthesis, and [Chapter 6](06-numerical-methods.md) develops numerical validation.

## 3.11 Exercises

1. Specify the smallest set of metadata that makes a complex transmission coefficient reproducible. Explain why a phase value without reference planes is incomplete.
2. Derive the TE power factors from the normal component of the time-averaged Poynting vector.
3. Derive the rectangle Fourier coefficients, including $w=0$ and $w=\Lambda$. What changes when the ridge is translated laterally?
4. Explain why $M=0$ can conserve power while disagreeing with a higher-order calculation. Distinguish exterior propagating channels from retained internal Fourier harmonics.
5. Use the notebook to change $h$. Reassess phase coverage, transmission, and convergence; define how you will compare phases between different heights.
6. Repeat an oblique-incidence calculation. Enumerate open orders in both media and retain all their powers.
7. Compare two interpolations near a wrapped-phase jump. Verify a proposed intermediate width with a new Maxwell solve.
8. Define a multi-parameter library for Chapter 10, including grouped data splits and numerical-uncertainty records.
9. Design a supercell comparison that tests the local-periodicity approximation. State an observable and acceptance threshold before running it.

Continue with the [six worked examples](03-unit-cell-guide.md) and [computational lab](../labs/03-unit-cell-lab.md). Download source and data there to extend the calculation through a pull request.
