---
title: "Specify a target field before choosing a phase"
---

# Specify a target field before choosing a phase


Here $\Phi$ denotes phase lag: $E=Ae^{-i\Phi}$. A stored library phase is instead the signed argument $\phi_j=\arg t_j$; its target is $-\Phi(x_j)$. The circular selection formula below uses that signed argument.

At a reference plane, a scalar target can be written

$$
E_{\rm out}(x)=A(x)e^{-i\Phi(x)}.
$$

For vector fields, specify two complex polarization components, or an appropriate Jones transformation. Also state wavelength, illumination, exterior media, reference planes, aperture, and the desired observable. A beam direction, target-order power, focal width, and polarization-conversion fraction are different objectives.

For time dependence $e^{+i\omega t}$ and an incident factor $e^{-ik_{x,i}x}$, a multiplicative phase contributes a local transverse wavevector

$$
k_{x,\rm out}=k_{x,i}+\frac{d\Phi}{dx}.
$$

Thus a constant gradient $g$ gives

$$
n_t\sin\theta_t=n_i\sin\theta_i+\frac{g}{k_0}.
$$

This is a wavefront-momentum relation. A realizable structure still needs a scattering calculation for its amplitudes. The [generalized-refraction work of Yu and colleagues](https://capasso.seas.harvard.edu/publications/light-propagation-phase-discontinuities-generalized-laws-reflection-and) is a foundational reference; use Chapter 4 for the discrete orders of an actually periodic geometry.

For a periodic ramp increasing by $2\pi\ell$ over $L$, $g=2\pi\ell/L$ and the intended outgoing order is $m=\ell$. A noninteger accumulated ramp does not become an arbitrary new Floquet order when the geometry is forced to repeat; the repeated pattern has its own Fourier spectrum.

