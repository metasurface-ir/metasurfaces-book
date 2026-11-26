# 7.5 Time-varying metasurfaces and breaking Lorentz reciprocity

Instructor booklet, pages 190–195.

The metasurfaces considered so far, including programmable and reconfigurable ones, were treated as time-invariant in each held state. Phase and amplitude states were changed on a timescale much longer than the radio-wave period $T_0=1/f_0$, so the material properties were treated as constant during the interaction with the wave.

When properties such as permittivity $\epsilon(t)$, conductivity $\sigma(t)$, or surface impedance $Z_s(t)$ are modulated during an observation, the structure enters the time-varying or space–time coding regime. Frequency conservation, time symmetry, and the conditions for Lorentz reciprocity must then be revisited. The modulation need not be comparable to the carrier frequency to create sidebands, as the exercise shows.

## 7.5.1 Physics of time-varying systems: energy and frequency

Classical linear electromagnetics has two important translation symmetries:

1. **Spatial translation symmetry.** Symmetry along a surface conserves tangential momentum, or the tangential wave-number component. Gradient metasurfaces break this spatial symmetry and deflect beams through the generalized Snell law.
2. **Time translation symmetry.** Noether's theorem relates time translation to energy conservation. In a linear time-invariant medium, frequency channels are independent: a steady response to a single-frequency wave cannot introduce a different frequency.

Modulating the structure with period $T_m$ and angular frequency $\omega_m=2\pi/T_m$ breaks continuous time translation and allows the incident frequency to change:

$$
\omega_{\rm out}=\omega_0+n\omega_m,\qquad n=0,\pm1,\pm2,\ldots
$$

Frequency conversion can result from linear time-varying modulation and does not require a nonlinear response to the incident wave's intensity. Include the modulator's energy supply in the full energy balance.

## 7.5.2 Mathematical formulation: Maxwell's equations with time-varying conditions

With local time-varying permittivity, the constitutive relation is

$$
D(t)=\epsilon_0\epsilon_r(t)E(t).
$$

In a nonmagnetic medium without free charge or current, Maxwell's equations give the one-dimensional wave equation

$$
\frac{\partial^2E(z,t)}{\partial z^2}-\mu_0\frac{\partial^2D(z,t)}{\partial t^2}=0.
$$

The second time derivative of displacement follows by the product rule:

$$
\frac{\partial^2D}{\partial t^2}=\epsilon_0
\left[\epsilon_r(t)\frac{\partial^2E}{\partial t^2}
+2\frac{d\epsilon_r}{dt}\frac{\partial E}{\partial t}
+\frac{d^2\epsilon_r}{dt^2}E(t)\right].
$$

The time derivatives of permittivity indicate that the modulation source, or pump, can exchange energy with the electromagnetic field.

### Space–time reflection coefficient

If the reflection coefficient of a cell at $z=0$ is modulated periodically, $\Gamma(t+T_m)=\Gamma(t)$, and the Fourier expansion is

$$
\Gamma(t)=\sum_{n=-\infty}^{\infty}a_n e^{in\omega_m t},\qquad
a_n=\frac{1}{T_m}\int_0^{T_m}\Gamma(t)e^{-in\omega_m t}\,dt.
$$

For a monochromatic incident wave $E_{\rm inc}(t)=E_0e^{i\omega_0t}$, the instantaneous reflection-coefficient model gives a reflected combination of frequency harmonics:

$$
E_{\rm ref}(t)=\Gamma(t)E_{\rm inc}(t)
=E_0\sum_{n=-\infty}^{\infty}a_ne^{i(\omega_0+n\omega_m)t}.
$$

This is the basis for direct data modulation at a metasurface, where mixing can take place on the sheet without a separate conventional radio mixer.

## 7.5.3 Breaking Lorentz reciprocity

Under Lorentz reciprocity for linear time-invariant media with reciprocal constitutive relations, a consistently defined scattering matrix is symmetric ($S_{12}=S_{21}$). Transmission from mode A to mode B equals the corresponding transmission from B to A.

Traditional approaches use ferrites with an external magnetic bias. Static bias hardware may be bulky, costly, and difficult to integrate into planar circuits. Space–time-varying metasurfaces offer a route that avoids this form of magnetic bias.

### Traveling-wave modulation

If the surface property varies with time and also moves continuously along the surface like a traveling wave,

$$
Z_s(x,t)=Z_0[1+M\cos(\beta_m x-\omega_m t)].
$$

Here $\beta_m$ is modulation wave number and $\omega_m$ is angular frequency. Space–time dispersion can differ for propagation along $+x$ and $-x$:

- **Wave traveling with the modulation ($+x$).** If phase matching holds, it can couple to the pump and convert up to $\omega_0+\omega_m$.
- **Wave traveling opposite the modulation ($-x$).** The matching condition differs. Depending on the design, the wave may reflect or convert to a lower frequency.

This asymmetry can give $S_{21}\ne S_{12}$ for a pair of corresponding channels. In a time-varying system, specify the frequency and mode at each port before comparing them.

:::{note} What follows from a traveling pump
Up- or down-conversion does not follow from the direction of travel alone. Frequency and momentum matching, modal overlap, polarization, and coupling set the actual paths. The exercise tests reciprocity for two specified channels in the reflection model.
:::

## 7.5.4 Nonreciprocal devices based on space–time metasurfaces

These structures offer a way to design planar high-frequency devices without a magnet:

1. **Optical and radio isolators.** Pass the signal in one direction, for example from a transmitter to an antenna, while suppressing reflection back to the source. The ideal targets are $|S_{21}|\approx1$ and $|S_{12}|\approx0$.
2. **Nonmagnetic circulators.** Three-port devices for radar or in-band full-duplex communications direct the transmitter to the antenna and the returning antenna wave to the receiver while isolating the sensitive receiver from transmit power.
3. **Planar parametric amplifiers.** Transfer energy from the modulation source to a weak radio wave without a conventional transistor amplifier in the signal path.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

A reflecting metasurface in air is illuminated at $f_0=10\,\mathrm{GHz}$. Its modulation frequency is $f_m=100\,\mathrm{MHz}=0.1\,\mathrm{GHz}$. Use the simplified model $E_{\rm ref}=\Gamma E_{\rm inc}$ in two cases.

- **Case A: uniform time modulation.**

$$
\Gamma_A(t)=0.6+0.4\cos(\Omega t),\qquad \Omega=2\pi f_m.
$$

  Illumination is normal.

- **Case B: traveling space–time modulation.**

$$
\Gamma_B(x,t)=0.6+0.4\cos(\Omega t-Kx),\qquad K=0.6k_0,\quad k_0=2\pi f_0/c.
$$

  The wave is incident in the $xz$ plane with $k_{x,\rm in}=+0.6k_0$. The sheet is sufficiently extended along $x$ to neglect edge effects.

1. Which reflected frequencies appear in A, and what are their relative amplitudes and powers? Is a nonlinear response needed?
2. In a time-varying dielectric, what extra terms appear in $\partial_t^2D$? What role does the modulation source play in the energy balance?
3. In B, find the frequency and angle of each order. Define the reverse frequency-conversion experiment and determine whether that path works in reverse.
4. How does this result relate to isolators, circulators, and parametric amplifiers?

```{dropdown} Show the full worked answer

### 1. Time modulation: sidebands without a nonlinear response

Expand the cosine:

$$
\Gamma_A(t)=0.6+0.2e^{i\Omega t}+0.2e^{-i\Omega t}.
$$

For incident wave $E_{\rm inc}=E_0 e^{i\omega_0t}$, the reflected field is

$$
E_{\rm ref}=E_0\left[0.6e^{i\omega_0t}
+0.2e^{i(\omega_0+\Omega)t}+0.2e^{i(\omega_0-\Omega)t}\right].
$$

At normal incidence and reflection, all three components have the same wave impedance in the air model. Relative power is the squared field coefficient.

| Order $n$ | Reflected frequency | Amplitude relative to $E_0$ | Share of incident power |
| --- | --- | --- | --- |
| $\mathord{-1}$ | $9.9\,\mathrm{GHz}$ | 0.2 | 4% |
| 0 | $10.0\,\mathrm{GHz}$ | 0.6 | 36% |
| $\mathord{+1}$ | $10.1\,\mathrm{GHz}$ | 0.2 | 4% |

There are no higher orders in this model because $\Gamma_A$ has only three nonzero Fourier coefficients. Doubling incident amplitude doubles all three field amplitudes. The process is therefore linear in the input signal. Frequency conversion comes from the **time-dependent reflection coefficient**.

Here $f_m$ is only one percent of $f_0$ and the sidebands still appear. The modulation need not be comparable to the carrier. What matters is that the modulation continues during the observation and the structure cannot be considered constant throughout it.

### 2. Maxwell's equations: where does the wave energy go or come from?

For a simple lossless, instantaneous dielectric with $D=\varepsilon(t)E$,

$$
\frac{\partial^2D}{\partial t^2}
=\varepsilon\frac{\partial^2E}{\partial t^2}
+2\dot{\varepsilon}\frac{\partial E}{\partial t}+\ddot{\varepsilon}E.
$$

The last two terms vanish in a time-invariant medium. The electric term in Poynting's theorem reveals the modulation's role in the energy balance:

$$
E\frac{\partial D}{\partial t}
=\frac{\partial}{\partial t}\!\left(\frac12\varepsilon E^2\right)
+\frac12\dot{\varepsilon} E^2.
$$

The final term describes energy exchange between the field and the modulation mechanism. Include the modulation source in the full balance.

The three reflected components in A sum to 44% of incident power. $\Gamma(t)$ alone cannot tell us whether the remaining 56% was absorbed, transmitted, or exchanged with the modulator. The model specifies **reflection** only.

### 3. Space–time modulation: frequency and tangential wave number both change

In B the modulation terms are proportional to $e^{\pm i(\Omega t-Kx)}$. Multiplication by the incident wave gives each order both a frequency shift and a tangential wave-number shift:

$$
f_n=f_0+nf_m,\qquad k_{x,n}=k_{x,\rm in}+nK.
$$

A propagating order in air requires

$$
|k_{x,n}|\le k(f_n)=2\pi f_n/c,\qquad
\sin\theta_n=\frac{k_{x,n}}{k(f_n)}.
$$

Use the **wave number at each order's own frequency** to calculate its angle.

| Order | Frequency | Tangential wave number | Result |
| --- | --- | --- | --- |
| $\mathord{-1}$ | $9.9\,\mathrm{GHz}$ | 0 | Propagates at broadside, $\theta_{-1}=0^\circ$ |
| 0 | $10.0\,\mathrm{GHz}$ | $+0.6k_0$ | Reflected beam at $\theta_0=\arcsin(0.6)\approx+36.9^\circ$ |
| $\mathord{+1}$ | $10.1\,\mathrm{GHz}$ | $+1.2k_0$ | $1.2k_0>1.01k_0$. Evanescent, with no far-field beam. |

The forward conversion channel connects an oblique $10\,\mathrm{GHz}$ input to a normal $9.9\,\mathrm{GHz}$ output.

**How do we define the reverse experiment?** Exchange the same two channels. Simply illuminating from the opposite angle with $10\,\mathrm{GHz}$ is a different test. Keep the modulation traveling in the same direction in both experiments.

- **Reverse input:** normally incident $9.9\,\mathrm{GHz}$ with $k_x=0$.
- **Output to test:** $10\,\mathrm{GHz}$ traveling back along the original path toward the source. Reversing propagation requires $k_x=-0.6k_0$.

Conversion from $9.9$ to $10\,\mathrm{GHz}$ uses order $+1$. Under the same modulation it supplies $+K$:

$$
k_{x,\rm out}=0+K=+0.6k_0.
$$

The wave can return to $10\,\mathrm{GHz}$, but exits in a different direction and does not return to the original channel. This is nonreciprocity of the **conversion path** in the ideal model.

Each channel is defined by **frequency and direction of propagation**. The correct comparison is between corresponding entries of a multifrequency scattering matrix. The result does not establish nonreciprocity at the carrier itself. Sidebands indicate modulation; different transmission between the exchanged channels indicates nonreciprocity.

### 4. From the example to a practical device

| Device | What does this example explain, and what remains to establish? |
| --- | --- |
| Isolator | A returning wave can be sent to another frequency or direction so that it does not reach the source. Establishing isolation requires measuring forward insertion loss and reverse rejection. A zero reverse channel alone does not establish low forward loss. |
| Circulator | Route the wave to a third port, for example $1\to2$, $2\to3$, and $3\to1$. One deflected beam illustrates routing. A complete circulator must establish all three paths. |
| Parametric amplifier | Pump energy can provide gain if transferred to the signal. Up-conversion alone does not imply amplification. Power in the desired output channel must exceed input signal power. The example's data do not show that gain. |

**Summary.** Time modulation determines which frequencies are generated. Spatial modulation determines their propagation directions. Directional motion of the modulation can prevent the same conversion path from being restored in the reverse experiment.
```
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
