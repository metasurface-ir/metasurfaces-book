---
title: "Phase gradients and generalized refraction"
---

(ch04-section-09)=
# Phase gradients and generalized refraction

For a prescribed transmission phase $\Phi(x)$, tangential phase matching motivates

$$
n_t k_0\sin\theta_t-n_i k_0\sin\theta_i=\frac{d\Phi}{dx}.
$$

This connects to the generalized reflection/refraction formulation of [Yu et al.](https://doi.org/10.1126/science.1210713). It specifies a desired phase-matching relation; useful efficiency also requires an electromagnetic design that supplies the required amplitudes and boundary response.

If the complex transmission function is periodic over $\Lambda$ and makes an ideal integer phase winding $\Phi(x+\Lambda)-\Phi(x)=2\pi q$, then the average gradient is $qG$. With our Fourier convention, an ideal prescribed factor $e^{-iqGx}$ shifts the transmitted tangential wavevector to order $m=q$. A sampled or imperfect phase profile generally has additional Fourier harmonics.

:::{dropdown} Derivation: an ideal ramp, its sampled version, and spectral aliases
For a local prescribed scalar transmission $t(x)=e^{-i\Phi(x)}$, the transmitted boundary phase is $k_{x,i}x+\Phi(x)$. A constant derivative gives a single tangential wavevector $k_{x,t}=k_{x,i}+\Phi'(x)$, yielding the phase-gradient relation. A varying derivative describes local phase slope; it does not make the entire output a single plane wave.

For a periodic $t$, its exact Fourier projection is

$$
c_m=\frac1\Lambda\int_0^\Lambda t(x)e^{+imGx}\,dx,\qquad
t(x)=e^{-iqGx}\ \Longrightarrow\ c_m=\delta_{mq}.
$$

Now divide the period into $N$ equal bins and hold the ideal ramp's midpoint value constant in each bin: $t_j=e^{-i2\pi q(j+1/2)/N}$ for integer $q$. Integrating within each bin, with $\operatorname{sinc}(v)=\sin(\pi v)/(\pi v)$ and $\operatorname{sinc}(0)=1$, gives

$$
c_m=\operatorname{sinc}\!\left(\frac mN\right)\frac1N
\sum_{j=0}^{N-1}e^{-i2\pi(q-m)(j+1/2)/N}
=\begin{cases}
(-1)^\ell\operatorname{sinc}(m/N),&m=q+\ell N,\\
0,&\text{otherwise}.
\end{cases}
$$

The roots-of-unity sum reappears. For $q=1$ and $N=6$, the target coefficient has $|c_1|^2=\operatorname{sinc}^2(1/6)\approx0.912$; the closest aliases occur at $m=-5$ and $m=7$. These are squared Fourier coefficients of a prescribed boundary function, **not diffraction efficiencies**. Open-order flux factors and a realizable Maxwell solution are still required. Closed aliases are evanescent, not missing far-field energy that can simply be added to a power sum.
:::

```{figure} ../assets/chapter-04/sampled-phase-spectrum.png
:alt: Continuous and six-step midpoint-sampled phase ramps with their Fourier spectra and marked propagating order interval.
:label: fig-ch04-sampled-phase

An ideal scalar phase winding and its six-step approximation. The sampled function has aliases separated by six order labels. For normal incidence into air at $\Lambda=3\,\mu\mathrm m$ and $\lambda_0=1.55\,\mu\mathrm m$, only $m=-1,0,+1$ are open; the nearest nonzero aliases are closed. Sampling changes the coefficients while the exterior channel map remains fixed.
```

**Try a counterfactual:** reverse the phase ramp, then increase the number of steps while keeping $\Lambda$ fixed. Predict the target order, the alias spacing, and which part of the light-cone diagram stays unchanged.

A real sequence of resonant elements need not realize that ideal scalar transmission function. Material dispersion, amplitude variation, coupling, and impedance mismatch can change its performance. Floquet channels describe the periodic scattering basis; a phase-gradient design seeks to excite selected coefficients in that basis.
