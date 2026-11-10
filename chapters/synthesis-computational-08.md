---
title: "Synthesize a focusing wavefront"
---

# Synthesize a focusing wavefront


For normal incidence and a focus at $(0,f)$ in a homogeneous output medium, equal accumulated phase gives

$$
\Phi(x)=-k_t\left(\sqrt{x^2+f^2}-f\right)+\phi_0.
$$

For a point focus in two transverse dimensions, replace $x^2$ with $x^2+y^2$. At oblique incidence subtract the incident tangential phase $k_{x,i}x+k_{y,i}y$ as well. The paraxial limit is $\Phi(x)\approx-k_tx^2/(2f)$; the exact profile avoids that approximation in the target path length, while a scalar aperture model still has its own limits.

The executed example uses a **cylindrical line focus**: 48 pitch-wide cells, aperture $D=31.2\,\mu\mathrm m$, design distance $f=30\,\mu\mathrm m$, wavelength $1.55\,\mu\mathrm m$, and output index 1.5. It compares a continuous ideal aperture, a sampled phase aperture, and an aperture assigned the expanded library's complex local coefficients.

Scalar angular-spectrum propagation is

$$
U(x,z)=\mathcal F^{-1}\left\{\widetilde U(k_x,0)
e^{-izk_z(k_x)}\right\},\qquad k_z=\sqrt{k_t^2-k_x^2},\quad\operatorname{Im}k_z\le0,
$$

with the square-root branch chosen to have nonnegative real part and nonpositive imaginary part for forward propagation/decay. The FFT assumes a periodic computational window, so pad the aperture and refine window size and spatial spacing independently. An exact sampled plane wave checks propagation phase. These are checks of the scalar model, not a full-wave finite-lens validation.

```{figure} ../assets/chapter-05/focus.png
:alt: Prescribed aperture phases and scalar line-focus profiles for continuous, sampled, and local-library fields.

The library aperture includes local amplitude and phase, including its selected global phase offset. That offset does not change the propagated intensity, so the plotted absolute phases need not coincide. Scalar propagation is an approximation to a possible finite device and has no full-wave focusing-efficiency claim.
```

At the design plane, the saved continuous profile has FWHM about $0.971\,\mu\mathrm m$, and the local-library model about $0.985\,\mu\mathrm m$. The notebook also reports peak squared field relative to the continuous reference and the fraction of modeled line intensity in a stated $\pm1\,\mu\mathrm m$ window. Those are scalar line metrics, not a physical focusing-power efficiency or two-dimensional encircled energy. A finite aperture can shift the axial intensity maximum away from the design distance.

