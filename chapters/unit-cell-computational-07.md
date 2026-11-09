---
title: "Validate before exporting"
---

(3-7-validate-before-exporting)=

# Validate before exporting

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
