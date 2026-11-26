# 8.3 Metasurface antennas

Instructor booklet, pages 211–218.

Phased-array radar, low Earth orbit (LEO) satellites, and massive multiple-input multiple-output (Massive MIMO) systems steer beams electronically. An active array uses phase shifters, power and low-noise amplifiers (PAs and LNAs), and a feed network. The costs include **power consumption, heat removal, and packaging complexity**. At millimeter-wave frequencies, microstrip or waveguide distribution losses also matter. A thin surface can instead radiate a guided wave progressively into space.

## 8.3.1 Metasurface leaky-wave antennas

**How does the surface wave radiate?** On a dielectric slab, if the phase constant $\beta_{\rm sw}$ exceeds the free-space wavenumber $k_0$, the external field decays normal to the slab. Periodic loading with period $p$ creates Floquet spatial harmonics.

$$
\beta_m=\beta_{\rm sw}+\frac{2\pi m}{p},\qquad m\in\mathbb Z.
$$

An order lies within the **radiation cone** when $-k_0<\beta_m<k_0$. A typical design brings $m=-1$ into this interval. Matching the tangential component gives the angle from the surface normal.

$$
\sin\theta_{\rm rad}=\frac{\beta_{\rm sw}-2\pi/p}{k_0}.
$$

Frequency changes both $k_0$ and $\beta_{\rm sw}$. The beam can scan from backward through broadside into the forward sector. An open stopband can appear near broadside. Cell symmetry and loading must be designed and checked for scanning through that region.

**Leakage and aperture illumination.** Take $x$ along the feed and write the propagation constant as $\beta-i\alpha$. With material losses neglected, $\alpha$ is amplitude attenuation due to radiation.

$$
P(x)=P_0e^{-2\alpha x},\qquad q(x)=-\frac{dP}{dx}.
$$

Varying cell geometry changes $\alpha$ along the aperture. Taylor and Chebyshev distributions are examples of sidelobe-reducing tapers. Strong initial leakage leaves less power for the far end. Specify the desired illumination first, then calculate the required leakage.

## 8.3.2 Fabry–Pérot cavity antennas

A feed lies between a perfectly conducting ground plane and a **partially reflecting surface** (PRS). A fraction of the field transmits at each encounter and the rest returns to the cavity. PRS reflection magnitudes in example designs can range from $0.8$ to $0.95$. For the outgoing fields to add in phase, the round-trip phase must be a multiple of $2\pi$.

$$
\Delta\phi=-\frac{4\pi h\cos\theta}{\lambda}+\psi_{\rm GND}+\psi_{\rm PRS}=-2m\pi.
$$

At broadside, with $\psi_{\rm GND}=\pi$,

$$
h=\lambda\left[\frac{\psi_{\rm PRS}+\pi}{4\pi}+\frac{m}{2}\right].
$$

Choose a branch with a practical positive height. For PRS phase near $\pi$, the first nonzero height is near $\lambda/2$. Zero phase gives $\lambda/4$. Negative reflection phase can yield $\lambda/10$ or $\lambda/20$ at the design frequency. A **high-impedance surface** (HIS) and an **artificial magnetic conductor** (AMC) illustrate reflection-phase engineering. This freedom matters in low-profile and conformal antennas. A target such as gain above $20\,\mathrm{dBi}$ also depends on aperture, loss, matching, and bandwidth.

## 8.3.3 Metasurface holographic antennas

A coaxial feed can launch a radial reference wave on the surface. The desired radiating wave is the object wave. For direction $(\theta_0,\phi_0)$, the reference and object fields on the surface are

$$
\Psi_{\rm ref}=A_{\rm ref}e^{-i\beta_{\rm sw}\rho},\qquad
\Psi_{\rm rad}=A_{\rm rad}e^{-ik_0(x\sin\theta_0\cos\phi_0+y\sin\theta_0\sin\phi_0)}.
$$

Record their interference by varying the local impedance. For normalized fields, a simple model is

$$
Z_s=i\left[X_0+M\operatorname{Re}\left(\Psi_{\rm ref}^*\Psi_{\rm rad}\right)\right].
$$

Here $X_0$ is the base reactance and $M$ the modulation depth. Illuminating the pattern with the reference wave leaks part of the wave into the desired direction. In a **dynamic metasurface antenna** (DMA), varactor biases or PIN-diode states rewrite the pattern. The beam can change at fixed frequency. Update rate, calibration, port count, and channel rank bound its application in Massive MIMO.

## 8.3.4 Comparing antenna architectures

| Feature | Active electronically scanned array (AESA) | Leaky-wave antenna | Dynamic holographic antenna (DMA) |
| --- | --- | --- | --- |
| RF chains | A chain and ADC/DAC per channel in a fully digital design | One or a few feed ports | One or several chains per subarray |
| Beam control | Phase shifters or digital weights | Frequency or cell tuning | Varactor or PIN diode |
| Power | Kilowatts in some large radars | Little control power for a fixed passive structure | Tens of watts for some panel controllers |
| Feed network | Line and power distribution losses | Waveguide or substrate-integrated waveguide (SIW) | Surface-wave feed |
| Structure | Multilayer circuits, RF packaging, and heat sinks | Low-profile sheet or waveguide | Thin sheet with bias network |

Power depends on system size and function. In analog and hybrid active arrays, several elements can share one RF chain. When selecting an architecture, count **independent data streams** separately from beams.

## Worked problem on metasurface antennas

::::{admonition} Try it first
:class: book-exercise

At $30\,\mathrm{GHz}$, the guided wave of a leaky-wave antenna has $\beta_{\rm sw}=1.6k_0$. Order $m=-1$ should radiate at $\sin\theta=0.2$. Its aperture is $L=0.15\,\mathrm m$ long and should radiate $80\%$ of the input power in a lossless model. A second design is a cavity with a perfectly conducting ground and an inward-facing PRS reflection coefficient $0.9e^{-i108^\circ}$. A third design is a one-dimensional end-fed hologram with $X_0=200\,\Omega$, $M=30\,\Omega$, and $\beta_{\rm sw}=1.6k_0$.

1. Find the leaky-wave period, radiating orders, and angle at several frequencies.
2. Compare constant leakage with uniform illumination.
3. Find the cavity height for broadside radiation.
4. Find the reactance profiles for two symmetric directions at fixed frequency.
5. Choose an architecture for each application.

```{dropdown} Show the full worked answer

### 1. Period, radiating orders, and frequency scan

$$
\lambda_0=10\,\mathrm{mm},\qquad p=\frac{\lambda_0}{1.6-0.2}\simeq7.14\,\mathrm{mm},\qquad \theta=\arcsin(0.2)\simeq11.5^\circ.
$$

The ratios $\beta_m/k_0$ for orders $0$, $-1$, and $-2$ are $1.6$, $0.2$, and $-1.2$. Only the $-1$ order radiates. Finite-aperture sidelobes can still occur. Approximating $\beta_{\rm sw}/k_0=1.6$ as constant,

$$
\sin\theta(f)=1.6-\frac{42\,\mathrm{GHz}}{f}.
$$

| Frequency | $\sin\theta$ | Angle |
| --- | --- | --- |
| $25\,\mathrm{GHz}$ | $\mathord{-0.08}$ | $\mathord{-4.6^\circ}$ |
| $26.25\,\mathrm{GHz}$ | $0$ | $0^\circ$ |
| $30\,\mathrm{GHz}$ | $0.20$ | $11.5^\circ$ |

Check for a stopband at broadside. In a broadband link, the change in angle with frequency is called beam squint.

### 2. Constant leakage and uniform illumination

$$
\alpha_{\rm const}=-\frac{\ln(0.2)}{2L}\simeq5.36\,\mathrm{m}^{-1},\qquad q(x)=2\alpha P(x).
$$

In this case, radiated power per unit length at the far end is $0.2$ of its initial value. For uniform power illumination,

$$
q=\frac{0.8P_0}{L},\qquad \frac{P(x)}{P_0}=1-\frac{0.8x}{L},\qquad
\alpha(x)=\frac{0.8}{2L(1-0.8x/L)}.
$$

Leakage increases from $2.67\,\mathrm{m}^{-1}$ to $13.33\,\mathrm{m}^{-1}$. For aperture field $A(x)$, $q\propto\lvert A\rvert^2$. A Taylor taper can reduce sidelobes and broaden the main lobe.

### 3. Cavity height

$$
-720^\circ\frac{h}{\lambda_0}+180^\circ-108^\circ=0
\quad\Longrightarrow\quad h=\frac{\lambda_0}{10}=1\,\mathrm{mm}.
$$

Zero PRS phase gives $2.5\,\mathrm{mm}$. With $180^\circ$ phase, the first nonzero height is $5\,\mathrm{mm}$. In the in-phase ray sum,

$$
E_{\rm out}=\frac{E_1}{1-0.9}=10E_1.
$$

$E_1$ is the outgoing field on the first pass. The ratio is relative to that field. Antenna gain also requires matching, aperture size, loss, and bandwidth to be accounted for.

### 4. Holographic steering at fixed frequency

$$
K=\beta_{\rm sw}-k_0\sin\theta,\qquad Z_s(x)=i[200+30\cos(Kx)]\,\Omega.
$$

For $+11.5^\circ$, $K=1.4k_0$ and the pattern period is $7.14\,\mathrm{mm}$. Multiplying the reference wave by the cosine yields the two components $\tfrac12 e^{-i(\beta_{\rm sw}\mp K)x}$. Their phase constants are $0.2k_0$ and $3k_0$. The latter lies outside the radiation cone. For $-11.5^\circ$, use $K=1.8k_0$ and period $5.56\,\mathrm{mm}$. In a tunable array the physical pitch stays fixed. Sampling and calibration must support the shorter pattern.

### 5. Architecture choice

| Need | Choice and reason |
| --- | --- |
| Frequency-driven angle scan | Leaky-wave antenna using dispersion |
| Fixed low-profile broadside beam | Fabry–Pérot cavity with engineered reflection phase |
| Steering at fixed frequency | DMA with a rewritable hologram |
| Multiple independent data streams | Phased array or DMA with adequate ports and rank |

A single RF port can transmit one signal on several beams. Independent streams require independent degrees of freedom. Include hybrid architectures, distribution losses, and control circuit power in the hardware comparison.
```
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
