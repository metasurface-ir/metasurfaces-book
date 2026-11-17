---
title: "Estimate convergence and choose an acceptance target"
---

# Estimate convergence and choose an acceptance target

If $Q_h=Q_*+Ch^p+o(h^p)$ over an asymptotic range, three equally refined meshes allow

$$
p_{\rm obs}=\log_2\left|\frac{Q_h-Q_{h/2}}{Q_{h/2}-Q_{h/4}}\right|,\qquad
Q_*\approx Q_{h/2}+\frac{Q_{h/2}-Q_h}{2^p-1}.
$$

Apply this to a consistently defined observable, such as complex transmission, with care near cancellations and roundoff. These estimates require an observed asymptotic trend; they are not rigorous bounds. Discontinuities, geometry staircasing, corners, and changing material representations can alter the rate. [Meep's subpixel discussion](https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/) gives examples of interface effects; our aligned scalar slab does not establish a universal second-order rate.

Select tolerances for the design decision before choosing a mesh. For example, a phase-sensitive library might require both $|\Delta t|<10^{-3}$ and a phase change below $0.1^\circ$ where transmission is appreciable. Test the worst relevant geometries and frequencies, rather than transferring one accepted mesh to every resonant structure.
