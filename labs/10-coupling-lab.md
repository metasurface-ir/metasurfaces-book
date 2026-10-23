---
title: 'ms-10: Independent-cell versus supercell predictions'
short_title: Coupling and local models lab
---

# ms-10: Independent-cell versus supercell predictions

**Chapters 3 and 6**, using the Chapter 5 supercell. Does assembling individually simulated cells preserve their responses? Compare two models of the **same geometry**, with matched wavelength, materials, polarization and phase planes.

**Executed:** five width-contrast cases, primitive-cell and supercell harmonic refinements, an exact uniform-array control, all open-order powers and a full-wave field map. The model is a restricted 1D, lossless, infinite-periodic TE structure.

## Identify the two environments

```{figure} ../assets/chapter-05/supercell-geometry.svg
:alt: Actual six-ridge supercell with unequal neighbors and full-sequence periodic boundaries.

In the full-wave geometry, six different ridges repeat together. In each local calculation, one ridge instead repeats every 0.65 µm among identical neighbors. Both use height 1.8 µm, the same indices and the same r/t reference planes.
```

The independent cells are **not isolated particles**: each is a periodic-array calculation with interactions among identical neighbors. Replacing those neighbors can change its response. The local reconstruction also removes within-cell field variation and evanescent structure. The discrepancy cannot be assigned uniquely to one coupling coefficient.

## Explore, then run

<iframe src="../interactives/design-studies.html?lab=coupling" title="Local-cell and supercell geometry comparison" width="100%" height="1650" loading="lazy" style="border:0;border-radius:14px"></iframe>

<a href="https://metasurface-ir.github.io/metasurfaces-book/interactives/design-studies.html?lab=coupling" target="_blank" rel="noopener">Open the browser lab in a new tab</a> · [Executed notebook](../notebooks/10-coupling.ipynb) · [Complete source bundle](../downloads/design-studies.zip)

The slider selects five saved geometries and their results. To rerun, extract the ZIP, install `requirements-labs.txt` in Python 3.12 and restart/run `notebooks/10-coupling.ipynb`. The notebook overlays actual ridge outlines on |Eᵧ/Eincident|. Field amplitude is not a local power-density map.

## Construct a fair comparison

Vary width contrast while preserving the mean:

$$
w_j(\alpha)=\bar w+\alpha(w_j^{\rm base}-\bar w),\qquad 0\leq\alpha\leq1.
$$

At α=0 the ridges are identical; at α=1 the baseline design is recovered. α measures geometric contrast, not physical coupling strength. Solve each width in its own primitive periodic cell, then construct an equal-cell-width staircase:

$$
\widetilde t_m=\operatorname{sinc}\!\left(\frac{m}{N}\right)\frac1N\sum_{j=0}^{N-1}t_j
\exp\!\left[-2\pi i m\frac{j+1/2}{N}\right],\quad N=6.
$$

Here sinc(u)=sin(πu)/(πu). Apply the same expression to rⱼ. Convert amplitude to power using each **supercell order's** longitudinal wavevector. The stitched field need not conserve power; retain its raw R+T rather than renormalizing it.

## Investigation sequence

1. **Control:** embed a uniform primitive array in the larger period. With matched physical Fourier cutoffs (M_super=6M_cell), compare complex r₀/t₀ and confirm that orders not divisible by six vanish. Only the zero primitive order propagates at this wavelength.
2. **Refine:** compare local-cell half-orders 24/32 and supercell half-orders 144/192. Inspect every open reflected/transmitted order. A small flux defect does not validate a model approximation.
3. **Vary contrast:** compare target efficiency, all transmitted orders and local R+T. Do not assume monotonic error with α; resonances can change it.
4. **Inspect fields:** locate ridge boundaries and the two reference planes in the field map. Explain why maximum pointwise electric field need not coincide with maximum outgoing target-order power.
5. **Separate errors:** report refinement changes separately from model discrepancy. Identify both changed-neighborhood response and the removal of within-cell field structure.

## Deliverable and extensions

Submit the geometry family, both model definitions, uniform control, convergence table, all open-order powers, original field plot and interpretation. Run all three new notebooks and `python scripts/validate_design_studies.py` for the fixed reference audit.

**Further outline:** permute widths, vary pitch or build an adjacent-cell library. Preserve a uniform control and converge each new geometry. Finite arrays, independent FEM/FDTD and direct extraction of an interaction matrix remain unexecuted extensions.

## Sources and next lab

[Pestourie and colleagues](https://arxiv.org/abs/1808.04215) discuss locally periodic approximations and full-Maxwell comparisons. Our ridge study is an original teaching calculation, not a reproduction of their device or figures. Use [Chapter 3](../chapters/03-unit-cell-design.md) for cell extraction and [Chapter 6](../chapters/06-numerical-methods.md) for numerical evidence. Follow the [source and reuse guide](../attribution.md).

Next: [ms-11, bounded optimization with independent checks](11-inverse-design-lab.md).
