---
title: "Build a frequency-domain slab calculation"
---

# Build a frequency-domain slab calculation

Use $k_0=2\pi/\lambda_0$, and $E_y(z)$ at normal incidence. The slab occupies $0<z<d$, with real indices $n_f$ inside and $n_e$ on both sides:

$$
\frac{d^2 E}{dz^2}+k_0^2 n^2(z)E=0,\qquad
E(z<0)=e^{-ik_ez}+r e^{+ik_ez},\qquad
E(z>d)=t e^{-ik_e(z-d)},\qquad k_e=k_0n_e.
$$

Thus $r$ is referenced to the entrance face and $t$ to the exit face. The incident field at the entrance has unit amplitude. The exact benchmark is Chapter 2's independent Fresnel-film formula.

Place both faces on nodes, use $h=d/N$, and replace the second derivative by a centered stencil:

$$
E_{j-1}+\bigl[(k_0h)^2\varepsilon_j-2\bigr]E_j+E_{j+1}=0.
$$

Interior nodes use $\varepsilon_j=n_f^2$, exterior nodes use $n_e^2$, and each face node uses $(n_f^2+n_e^2)/2$. This interface average applies to our scalar tangential electric field and aligned slab; it is not a universal prescription for normal electric components, metals, curved corners, or general vector Maxwell equations.

A uniform exterior supports a discrete traveling wave with phase step $\theta$:

$$
4\sin^2(\theta/2)=(k_eh)^2,\qquad
\theta=2\arcsin(k_eh/2),\qquad k_eh<2.
$$

The grid cutoff is a mathematical domain limit, not an accuracy recommendation. Even safely below cutoff, numerical dispersion can be substantial. The implementation requires $k_0h\max(n_f,n_e)<2$ in both media. Admissible coarse grids may still be inaccurate and are retained to expose that failure.

The right outgoing ghost value is $E_{J+1}=e^{-i\theta}E_J$. On the left, add a known incident wave and impose outgoing behavior on the reflected part. These discrete outgoing boundaries are exact for the homogeneous exterior stencil. They are **not a PML**. A deliberately mismatched option uses $e^{-ik_eh}$ on the right to reveal small artificial reflections.
