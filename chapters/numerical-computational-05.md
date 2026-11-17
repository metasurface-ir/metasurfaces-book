---
title: "See conservation fail as an accuracy certificate"
---

# See conservation fail as an accuracy certificate

```{figure} ../assets/chapter-06/convergence.png
:alt: Logarithmic mesh-refinement plot comparing complex transmission error, algebraic residual, and discrete power imbalance.

Three diagnostics answer different questions. A coarse conservative system can have a tiny residual and power defect while its complex transmission remains inaccurate. The benchmark error falls with spatial refinement.
```

For the published slab, $\lambda_0=1.55\,\mu\mathrm m$, $d=0.60\,\mu\mathrm m$, $n_f=2.4$, and $n_e=1$. Predict which plotted curve will change most before doubling $N$. Inspect circular phase error as well as power. Phase differences use $\arg(t_h t_{\rm exact}^*)$, and cease to be informative near a transmission zero.

```{figure} ../assets/chapter-06/fields.png
:alt: Real electric fields and pointwise errors for coarse and refined meshes compared with the exact slab field.

Field agreement is checked at the same physical coordinates and incident normalization. Fine grids improve phase accumulation and interference; the shaded interval is the physical film.
```
