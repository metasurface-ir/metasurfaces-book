---
title: "Finite arrays and grating lobes"
---

(ch04-section-08)=
# Finite arrays and grating lobes

An infinite periodic calculation produces discrete Floquet directions. A finite illuminated array has angular lobes with nonzero width. For $N$ equally spaced prescribed scalar sources with identical weights and the incident phase progression, a normalized array factor is

$$
\mathcal A_N(\theta)=\frac1N\sum_{j=0}^{N-1}
\exp\!\left[-ij\Lambda(k_{x,i}-n_o k_0\sin\theta)\right].
$$

Its maxima occur at the same tangential matching conditions when they lie inside the output light cone. Increasing $N$ narrows the peaks. The notebook computes the sum directly, avoiding a removable $0/0$ singularity in a sine-ratio formula.

:::{dropdown} Derivation: geometric series, first nulls, and aperture width
Define $\psi=\Lambda(k_{x,i}-n_ok_0\sin\theta)$. Sum the geometric series when $e^{-i\psi}\ne1$:

$$
\mathcal A_N=\frac{1-e^{-iN\psi}}{N(1-e^{-i\psi})}
=e^{-i(N-1)\psi/2}\frac{\sin(N\psi/2)}{N\sin(\psi/2)}.
$$

At $\psi=2\pi\ell$, the original sum gives $\mathcal A_N=1$; this is a removable singularity of the quotient. The matching condition is $k_{x,o}=k_{x,i}-\ell G$, hence the Floquet label is $m=-\ell$ in our convention.

For $N>1$, the first nulls adjacent to a maximum satisfy $\delta\psi=\pm2\pi/N$. Their locations in sine-angle coordinates are exact when they remain in the physical angular domain:

$$
\left|\sin\theta_{\rm null}-\sin\theta_m\right|=\frac{\lambda_0}{N\Lambda n_o}.
$$

For a narrow lobe away from grazing, linearize $\sin\theta$ about $\theta_m$ to obtain the full width between these first nulls, in radians:

$$
\Delta\theta_{\rm null}\approx\frac{2\lambda_0}{N\Lambda n_o\cos\theta_m}.
$$

Doubling $N$ approximately halves this width. Near grazing, use the exact sine-angle nulls; one null may fall outside the visible region and the small-angle approximation fails. $N\Lambda$ is the width scale of this uniformly weighted source model, not a claim about a particular fabricated aperture.
:::

```{figure} ../assets/chapter-04/finite-array.png
:alt: Normalized squared scalar array factors for three finite array lengths, with analytical Floquet angles marked as vertical lines.
:label: fig-ch04-array

Prescribed scalar array factors for 8, 24, and 64 repeated sources. The vertical markers are analytical Floquet directions. This plot does not include an element radiation pattern, mutual coupling, vector boundary matching, or a power-normalized metasurface efficiency.
```

In scanning-array language, unwanted additional visible maxima are grating lobes. Suppose all incidence angles satisfy $|\theta_i|\leq\theta_{\max}$ and the zeroth order remains open. A sufficient condition to keep every nonzero order closed throughout that scan is

$$
\frac{\lambda_0}{\Lambda}>n_o+n_i\sin\theta_{\max}.
$$

For equal unit indices and the limiting full scan toward $90^\circ$, this becomes the familiar strict half-wavelength-spacing condition. At normal incidence alone the corresponding bound is $\Lambda<\lambda_0/n_o$. Always state the medium, wavelength, scan range, and whether equality means an excluded grazing case. For a broadband requirement, check the smallest relevant wavelength and the actual dispersion.

:::{dropdown} Proof of the scan bound
Let $s_i=n_i\sin\theta_{\max}$ and $d=\lambda_0/\Lambda>0$. For every nonzero integer $m$, the reverse triangle inequality gives

$$
|q_i+md|\geq |m|d-|q_i|\geq d-s_i>n_o
\qquad\text{if}\qquad d>n_o+s_i.
$$

Thus all nonzero orders are strictly outside the light cone over the stated scan. At equality, an edge incidence and the oppositely signed first order can touch the cone. The proof is about channel geometry: an allowed extra channel can still have zero amplitude, and an element radiation pattern can suppress a finite-array maximum without changing this bound.
:::
