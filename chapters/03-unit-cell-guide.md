---
title: 'Chapter 3: Worked Examples and Learning Path'
short_title: Unit-cell worked examples
---

# Chapter 3: Worked Examples and Learning Path

**Question:** what evidence turns a simulated response into a usable design decision?

Read [Chapter 3](03-unit-cell-design.md), make predictions in the [browser lab](../labs/03-unit-cell-lab.md), and then run the [notebook](../notebooks/03-unit-cell-library.ipynb). Begin with the channel convention in [Chapter 4](04-periodic-floquet.md) when needed.

## Suggested learning path

| Stage | Work | Evidence to retain |
| --- | --- | --- |
| 1 | Draw the cell, illumination, and reference planes | Geometry sketch and parameter table |
| 2 | Work through the interface/film limits | Complex coefficients and normalized powers |
| 3 | Compare harmonic truncations | Complex-response changes alongside power residual |
| 4 | Explore width, phase, and transmission together | Two accepted targets and an unattainable request |
| 5 | Execute and export the notebook | CSV, JSON, source version, and validation record |
| 6 | Propose a supercell or second-method comparison | Defined observable and acceptance criteria |

For a classroom demonstration, draw a phase circle and place each computed transmission coefficient on it. Changing width moves a marker along a partial arc. Ask students to point to a desired phase before showing whether the arc reaches it and whether its transmitted power passes the threshold.

## Example 1: field amplitude versus power

At normal incidence from index 1 to 1.5 with zero layer height,

$$
r=\frac{1-1.5}{1+1.5}=-0.2,\qquad t=\frac{2}{1+1.5}=0.8.
$$

The reflected power is $R=|r|^2=0.04$, while the transmitted power is $T=(1.5/1)|t|^2=0.96$. Thus $R+T=1$. The value $|t|^2=0.64$ is the squared electric-field ratio. The different wave impedances account for the difference from transmitted power.

**Prediction:** placing the same flat interface in a larger periodic cell adds available order labels. Does it create nonzero scattering into them? Continuous lateral translation symmetry keeps those amplitudes zero. The audit checks this case.

## Example 2: which channels belong in the library?

For $\Lambda=0.65\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, and normal incidence,

$$
\alpha_m=m\frac{1.55}{0.65}\approx2.3846m.
$$

Both exterior indices, 1 and 1.5, are smaller than $|\alpha_{\pm1}|$. Only order zero propagates on each side. The solver still retains closed harmonics to represent the near field and the patterned material response.

Now use $\Lambda=1.4\,\mu\mathrm m$ and $\theta_i=20^\circ$:

$$
\alpha_m=\sin20^\circ+m\frac{1.55}{1.4}.
$$

Reflection supports $m=-1,0$; transmission supports $m=-1,0,+1$. The audit computes these channels, checks their total power, and compares their order powers under incidence reversal and order relabeling. A library containing only $t_0$ would omit physically available output power here.

## Example 3: a monitor shift is a phase shift

Take the reference normal-incidence cell, $L_i=0.10\,\mu\mathrm m$ and $L_t=0.20\,\mu\mathrm m$. The raw transmission ratio gains

$$
\Delta\phi_t=\frac{2\pi}{1.55}[1(0.10)+1.5(0.20)]
\approx1.6215\,\mathrm{rad}\approx92.90^\circ.
$$

Moving the monitors leaves the device and its power response unchanged. Multiplying the raw coefficient by $e^{-i\Delta\phi_t}$ returns the phase at the two ridge faces. The notebook synthesizes three monitor placements and recovers the same complex coefficients to floating-point accuracy.

**Diagnostic:** two solvers can agree in $T$ yet show a constant phase discrepancy because they use different reference planes. Map those planes before changing the physical model.

## Example 4: conservation can hide truncation error

Retain $M=0$, then $M=1,2,4,\ldots,32$ for the central width. Inspect the executed convergence table, which uses $M=48$ as a comparison.

At low order the truncated equations still form a lossless scattering problem and can conserve power. They represent less of the patterned field. The independent quantity of interest is the change in the complex response as the representation improves.

The library therefore uses separate acceptance limits: $|\Delta t|<5\times10^{-4}$, power changes below $5\times10^{-4}$, phase changes below $0.05^\circ$, and all-channel power residual below $10^{-8}$. Each of the 50 width samples passes its $M=24$ versus $32$ comparison. The limits define this teaching investigation; a new resonant geometry requires its own convergence study.

## Example 5: select a target and reject a failed request

Require accepted rows, $T\geq0.8$, and a phase error of at most $5^\circ$. A target of $-100^\circ$ selects a width near $0.24\,\mu\mathrm m$, with $T\approx0.865$ and circular error about $0.50^\circ$.

For a target of $0^\circ$, the closest eligible width is $0.57\,\mu\mathrm m$, with $T\approx0.8245$ and a remaining error of about $43.73^\circ$. The request is unmet. A nearest-neighbor algorithm returning an index does not establish feasibility.

Try a minimum transmission of 1 in the explorer. No library geometry meets it. The interface should report an empty feasible set rather than quietly selecting a lower-transmission cell.

## Example 6: a reusable dataset and its validity domain

Consider the record at $w=0.24\,\mu\mathrm m$. Retain the real/imaginary parts of $r_0,t_0$, powers, fixed experiment parameters, reference faces, harmonic counts, refinement changes, acceptance status, environment, and source hash.

Sending only the phase would lose amplitude and make phase wrapping ambiguous. Sending width and phase without material, height, wavelength, and angle would leave the underlying experiment unspecified. Sending $t_0$ alone at a multiorder condition would omit other scattering channels.

The exported library covers one wavelength and incidence, ideal constant-index materials, TE polarization, and one ridge family. The separate wavelength plot illustrates a neighborhood but does not broaden that library's validated domain. A useful student contribution is to create another clearly versioned domain, repeat the checks, and document how it can be combined with the original.

## Report checklist and next connection

Submit your prediction, model sketch, equations/conventions, parameter changes, analytic limits, convergence table, response plots, library files, audit, and one unmet target. State which solver stages actually ran. A FEM/FDTD cross-check or a varying-neighbor supercell needs its own execution evidence.

[Chapter 5](05-metasurface-synthesis.md) now expands phase coverage and verifies four selected periodic supercells using these principles. Chapter 10 can use a broadened, validated library as an electromagnetic learning dataset. A finite-device efficiency and AI generalization require further evidence beyond these 50 related width samples.
