# Chapter 8: Emerging Applications of Metasurfaces in Communications Engineering

## 8.1 Introduction: from photonic physics to telecommunications towers

Instructor booklet, page 204.

Friends, by now we have learned how metasurfaces can manipulate the phase, amplitude, and polarization of electromagnetic waves at subwavelength scales, almost like magic. But a communications engineer will ask, “Where does this beautiful physics help me in a 5G or 6G network?”

The booklet's answer is: everywhere! Metasurfaces are changing communications architecture. We used to treat the propagation environment as random and uncontrollable, full of fading, shadowing, and interference, and put considerable effort into compensating with sophisticated receiver and transmitter processing. Metasurfaces let us program part of the **propagation environment itself**. In this chapter we will see how these components can replace large antennas in some applications and introduce ideas such as the **smart radio environment**.

:::{tip} From component to link
A strong beam by itself does not mean a good link. For each example also account for power at the receiver, interference, channel-training time, and control losses.
:::


## 8.2 Smart radio environments (SRE) and reconfigurable intelligent surfaces (RIS/IRS)

Instructor booklet, pages 204–211.

## 8.2.1 From adapting to the channel to programming propagation

From the first wireless generation through 5G, propagation was usually treated as **random, passive, and difficult to control**. Waves undergo path loss, multipath fading, refraction, scattering, and shadowing. Advanced coding, robust modulation, and signal processing at the transmitter (Tx) and receiver (Rx) compensate for these effects.

Moving into millimetre-wave (mmWave, $30$ to $300\,\mathrm{GHz}$) and terahertz bands (THz, about $0.1$ to $10\,\mathrm{THz}$ here) reduces wavelengths to millimetres and below. Two practical consequences follow:

1. **Severe free-space path loss.** At fixed distance and antenna gains, Friis gives received-to-transmitted power proportional to $f^{-2}$ and free-space path loss (FSPL) proportional to $f^2$.
2. **Blockage.** High-frequency waves behave quasi-optically. Concrete, foliage, or a person can block line of sight (LoS). The booklet gives $20$ to $40\,\mathrm{dB}$ as illustrative losses. If non-line-of-sight (NLoS) contributions are too weak, the link falls into outage.

A **smart radio environment (SRE)** makes part of the physical environment programmable. One tool is the **reconfigurable intelligent surface (RIS)**, also called an **intelligent reflecting surface (IRS)**. It is a two-dimensional array of switchable cells with components such as PIN diodes, varactors, or RF-MEMS switches. Digital commands from a controller connected to the base station change element amplitudes and phases.

- A wall can become a **steerable intelligent mirror**.
- A **virtual line of sight** can serve a user behind an obstruction.
- With suitable channel knowledge and degrees of freedom, phase settings can help **cancel interference** between users.

## 8.2.2 Hardware architecture and comparison with relays

Compare a passive RIS with **amplify-and-forward (AF)** and **decode-and-forward (DF)** relays.

| Feature | Active AF or DF relay | Passive RIS |
| --- | --- | --- |
| **RF chains** | Mixers, filters, ADCs, and DACs | No independent receive/transmit chain at each reflecting cell |
| **Power amplifier (PA)** | Active amplification with power and heat costs | No PA in the reflection path |
| **Thermal noise** | AF amplifies incoming noise and can add noise | No active amplification chain; overall link loss and noise still matter |
| **Duplexing** | Half-duplex or self-interference cancellation | Simultaneous scattering without an active transmitter on the surface; full-duplex operation of the network is not assured |
| **DC power** | Several to tens of watts in the examples | Milliwatts to watts for the panel, depending on bias and control |
| **Hardware cost** | Active chains and sometimes a dedicated connection | May be cheaper with printed or flexible PCBs |

Model cell $n$ as a variable load $Z_n=R_n+iX_n$ on a line of reference impedance $Z_0$:

$$
\Gamma_n=\frac{Z_n-Z_0}{Z_n+Z_0}=|\Gamma_n|e^{i\theta_n}.
$$

$Z_0\simeq377\,\Omega$ for normal incidence in free space. In the passive lossless limit $R_n\to0$, $|\Gamma_n|=1$, and varying reactance sets the phase:

$$
\theta_n=\pi-2\arctan(X_n/Z_0)\pmod{2\pi}.
$$

An ideal reactance sweep spans a phase cycle. Practical reactance range and losses limit available states, and nanosecond component switching does not establish whole-panel settling time.

## 8.2.3 Cascaded channel modeling and the $N^2$ power law

### A. Formulating the cascaded channel

Suppose a base station (BS) and a user each have one antenna (SISO). A wall-mounted RIS has $N$ cells of subwavelength pitch $d_x=d_y\le\lambda/2$. Propagation has two legs: the **forward link** from BS to cell $n$, coefficient $h_n\in\mathbb C$, and the **RIS-to-user link**, coefficient $g_n\in\mathbb C$.

$$
h_n=\alpha_n e^{-ik_0r_{1,n}},\qquad
g_n=\beta_n e^{-ik_0r_{2,n}},\qquad k_0=2\pi/\lambda.
$$

Here $r_{1,n}$ and $r_{2,n}$ are the two distances. With a Friis convention collecting directional element gain into $F_n$, the dimensionless coefficients can be written as

$$
\alpha_n=\frac{\lambda\sqrt{G_t F_n(\theta_{t,n})}}{4\pi r_{1,n}},
\qquad
\beta_n=\frac{\lambda\sqrt{G_r F_n(\theta_{r,n})}}{4\pi r_{2,n}}.
$$

$G_t$ and $G_r$ are antenna gains, and $F_n$ is the cell gain factor in the corresponding direction. **Correction.** The wavelength factor omitted in print is required if these are dimensionless Friis coefficients. Do not double count element area or gain in a calibrated link budget.

### B. Cascaded path loss

A direct path has power transfer proportional to $d^{-2}$. A single reflecting cell in the two-leg model, with directions and other factors fixed, scales as

$$
|g_n h_n|^2\propto\frac1{r_{1,n}^2r_{2,n}^2}
$$

This is **multiplicative path loss**. **Coherent phase combining** can compensate for some of the loss.

### C. Deriving the $N^2$ power law

The receiver sees the linear sum of contributions:

$$
y=\left(\sum_{n=1}^{N}g_n\Gamma_n h_n\right)x+w,
\qquad \mathbb E|x|^2=P_t,\quad w\sim\mathcal{CN}(0,\sigma^2).
$$

Substitute the lossless reflection law:

$$
y=\left(\sum_{n=1}^{N}|g_n||h_n|
 e^{i[\theta_n-k_0(r_{1,n}+r_{2,n})]}\right)x+w.
$$

To cancel differing propagation delays, set

$$
\theta_n^{\rm opt}=k_0(r_{1,n}+r_{2,n})+\phi_0\pmod{2\pi}.
$$

$\phi_0$ is a common phase. For $\phi_0=0$, the exponentials become one. If the RIS is small compared with the path lengths and amplitudes are approximately equal,

$$
y=N|g||h|e^{i\phi_0}x+w,\qquad
P_r=\mathbb E|y-w|^2=P_t|g|^2|h|^2N^2.
$$

- Ten times as many **equal coherent contributions** gives a factor of 100, or $20\,\mathrm{dB}$.
- This can partly offset two-hop loss; distance dependence remains.
- The booklet's aperture interpretation combines input collection over $NA_{\rm cell}$ and output directional gain proportional to $N$. Their ideal product gives $N^2$. Subdividing a fixed aperture does not give unlimited power.

## 8.2.4 Near-field beam focusing

The approximate Fraunhofer boundary of the far field is

$$
d_F=\frac{2D^2}{\lambda},
$$

where $D$ is the aperture's largest dimension. For an **extremely large-scale RIS (XL-RIS)** with $D=3\,\mathrm m$ at $100\,\mathrm{GHz}$ ($\lambda=3\,\mathrm{mm}$),

$$
d_F=\frac{2(3\,\mathrm m)^2}{0.003\,\mathrm m}=6000\,\mathrm m.
$$

Many urban terminals can be in the **radiative near field (Fresnel region)**. Use a **spherical wavefront** rather than a planar one.

1. **Three-dimensional beam focusing versus angular steering.** A far-field direction is $(\theta,\phi)$. A near-field design sets phase for $(x,y,z)$, so the response can decrease away from the chosen range. Physical-layer security is one motivation, but focus alone does not prevent interception.
2. **Users at the same angle.** Two users in one direction at different ranges can have different spherical responses. Independent service depends on actual range resolution, aperture, and interference.

## 8.2.5 Operational and engineering challenges

1. **Channel-estimation overhead.** Passive cells have no independent RF ADC or processing. The base station estimates the composite channel. For $N=1024$, independent pilots may occupy much of the coherence time. Sparse sensing in **semi-passive RIS** and **compressive sensing** can help when there is suitable structure.
2. **Phase-quantization errors.** Continuous varactor bias has loss, noise, and cost. One-bit and two-bit coding cause phase errors and sidelobes. With uniform rounding error, the approximate power efficiency is

$$
\eta_B\simeq\left[\frac{\sin(\pi/2^B)}{\pi/2^B}\right]^2.
$$

One bit gives $4/\pi^2\simeq40.5\%$, about $4\,\mathrm{dB}$ of loss, and two bits give about $81.1\%$.

3. **Mutual coupling at small spacing.** Small pitches, below $\lambda/4$ in some designs, constrain grating orders but strengthen near-field interaction. Switching a neighbor can change a cell's phase and magnitude. The pitch requirement depends on the angles and orders, and mutual coupling does not by itself imply nonlinear RF behavior.

## Worked problem on a reflected link and near-field focusing

::::{admonition} Try it first
:class: book-exercise

In a station hall, passing passengers sometimes block the direct path from a base station to a user. Mount a **passive RIS** on the wall. Both antennas are on its reflection side. The direct path is blocked but both RIS legs remain open.

- The $129\times129$ array lies at $z=0$, centered at the origin, with pitch $d=\lambda/2$ at $30\,\mathrm{GHz}$.
- The base station is at $(-6,0,8)\,\mathrm m$ and the user is at $(0,0,5)\,\mathrm m$.
- Unblocked direct power is $-65\,\mathrm{dBm}$, blockage adds $30\,\mathrm{dB}$ loss, noise is $-85\,\mathrm{dBm}$, and required SNR is $8\,\mathrm{dB}$.
- A calibrated link budget gives $-75\,\mathrm{dBm}$ for the RIS-only path with ideal continuous phases.
- Each pilot takes $2\,\mathrm{\mu s}$ including pattern loading. Coherence time is $2\,\mathrm{ms}$.

Explain the direct-link outage and the difference from a relay. Examine the impedance–phase law, $N^2$ scaling, focusing, phase resolution, channel overhead, and the effect of coupling.

```{dropdown} Show the full worked answer

### 1. Programming propagation: why is an alternative path needed?

$$
P_{\rm dir}=-65-30=-95\,\mathrm{dBm},\qquad
\mathrm{SNR}_{\rm dir}=-95-(-85)=-10\,\mathrm{dB}.
$$

The direct link is $18\,\mathrm{dB}$ below threshold. The RIS creates another path from the **two available legs**. The transmitter and receiver may still adapt to their channel, which now has a controllable contribution.

Separate blockage from free-space loss. At fixed antenna gain and distance, increasing frequency from $3$ to $30\,\mathrm{GHz}$ increases free-space loss by $20\,\mathrm{dB}$. The given $-65\,\mathrm{dBm}$ already refers to $30\,\mathrm{GHz}$, so do not apply that increment again.

| Option | Action on the signal | Practical consequence |
| --- | --- | --- |
| **AF** | Amplify and retransmit | Requires RF transmit hardware and power, and amplifies input noise |
| **DF** | Decode and retransmit | Regenerates data if the first hop can be decoded |
| **Passive RIS** | Scatter with controlled amplitude and phase | No amplifier in the reflection path, but controller and bias draw power |

The surface has no active relay transmitter to produce its own transmit leakage. Its loss and link noise still matter, and full-duplex operation of the network must be checked.

### 2. From cell reactance to a phase code

$$
\Gamma_n=\frac{iX_n-Z_0}{iX_n+Z_0},\qquad
|\Gamma_n|=1.
$$

Numerator and denominator both have magnitude $\sqrt{X_n^2+Z_0^2}$.

| Reactance | Reflection coefficient | Phase |
| --- | --- | --- |
| $X_n=0$ | $\mathord{-1}$ | $180^\circ$ |
| $X_n=+Z_0$ | $+i$ | $90^\circ$ |
| $X_n=-Z_0$ | $-i$ | $270^\circ$ |
| Limit $\lvert X_n\rvert\to\infty$ | $\mathord{+1}$ | $0^\circ$ |

The limiting row makes the fourth two-bit state explicit. The $377\,\Omega$ reference applies to normal free-space incidence. Calibrate real states versus angle and polarization, and record amplitude as well as phase.

### 3. The origin of cascaded $N^2$ scaling

$$
c_n=g_nh_n=a_n e^{-ik_0(r_{1,n}+r_{2,n})},\qquad
y=\left(\sum_{n=1}^{N}c_n\Gamma_n\right)x+w,\quad N=129^2=16641.
$$

Here $a_n=|g_nh_n|$ and $k_0=2\pi/\lambda$. Set $\theta_n=k_0(r_{1,n}+r_{2,n})+\phi_0$ so the contributions arrive with common phase:

$$
P_r=P_t\left(\sum_n a_n\right)^2\simeq P_tN^2a^2.
$$

Add the amplitudes and then square. Doubling the number of equal coherent terms multiplies power by four, or $6.02\,\mathrm{dB}$. Doubling just the RIS-to-user distance and refocusing gives a $6.02\,\mathrm{dB}$ power loss under $a^2\propto(r_1^2r_2^2)^{-1}$. Subdividing a fixed aperture does not keep $a$ fixed.

### 4. Near field: why is the user angle insufficient?

At $30\,\mathrm{GHz}$, $\lambda\simeq10\,\mathrm{mm}$ and $d=5\,\mathrm{mm}$. The outermost centers span $128d=0.64\,\mathrm m$ per side. Their diagonal is $D=0.64\sqrt2\simeq0.905\,\mathrm m$, giving $d_F=2D^2/\lambda\simeq164\,\mathrm m$. The two distances are $10$ and $5\,\mathrm m$, so include spherical curvature of both legs. For the cell at $(x_n,y_n,0)$,

$$
\begin{aligned}
\theta_n-\theta_{\rm center} &=
k_0(\Delta r_{1,n}+\Delta r_{2,n})\pmod{2\pi},\\
\Delta r_{1,n}&=\sqrt{(x_n+6)^2+y_n^2+8^2}-10,\\
\Delta r_{2,n}&=\sqrt{x_n^2+y_n^2+5^2}-5.
\end{aligned}
$$

At $(0.30,0,0)\,\mathrm m$, the outgoing excess path to $z=5\,\mathrm m$ is $\sqrt{5^2+0.30^2}-5\simeq8.99\,\mathrm{mm}$, requiring about $324^\circ$ of compensation. For a same-angle user at $z=10\,\mathrm m$ these become $4.50\,\mathrm{mm}$ and $162^\circ$. Changing only the range changes this cell's relative phase by about $162^\circ$. Interference and confidentiality depend on the **whole aperture response** at other positions.

### 5. Phase quantization: one bit or two?

Use the approximation $\eta_B$ for many contributions with roughly uniform error in $[-\pi/2^B,+\pi/2^B]$.

| Resolution | Efficiency | Loss | RIS power | RIS-only SNR |
| --- | --- | --- | --- | --- |
| Continuous | 100% | $0\,\mathrm{dB}$ | $\mathord{-75.00}\,\mathrm{dBm}$ | $10.00\,\mathrm{dB}$ |
| One bit | 40.5% | $3.92\,\mathrm{dB}$ | $\mathord{-78.92}\,\mathrm{dBm}$ | $6.08\,\mathrm{dB}$ |
| Two bits | 81.1% | $0.91\,\mathrm{dB}$ | $\mathord{-75.91}\,\mathrm{dBm}$ | $9.09\,\mathrm{dB}$ |

One bit misses $8\,\mathrm{dB}$, while two bits give about $1.1\,\mathrm{dB}$ margin. Include any residual $-95\,\mathrm{dBm}$ direct path by adding **complex field amplitudes**. The difference of their magnitudes at the worst phase gives about $8.1\,\mathrm{dB}$. Further loss and calibration errors can eliminate the margin. The efficiency formula does not guarantee performance for a particular code.

### 6. Channel estimation and coupling: why an ideal code may not work

**A. Training overhead.** Dividing by the known pilot gives

$$
z_m=\sum_{n=1}^{N}\Gamma_{m,n}c_n+v_m,\qquad
t_{\rm train}\ge16641(2\,\mathrm{\mu s})=33.282\,\mathrm{ms}>2\,\mathrm{ms}.
$$

The products $c_n$ are identifiable, without uniquely separating $g_n$ and $h_n$. Independently estimating every coefficient requires at least that many independent observations. With 64 groups and 64 independent patterns, such as group Hadamard patterns, training takes $128\,\mathrm{\mu s}$, or 6.4% of coherence time. Only group channels are recovered and coarse groups can spoil the focus. Geometry or sparse sensors offer other ways to reduce unknowns.

**B. Mutual coupling.** Neighboring codes can change the phase and amplitude of a cell. An isolated cell table need not predict the assembled panel. Calibrate the intended patterns on the panel and measure power or SNR at the receiver.

**Design result.** Use the full length of both legs for focusing. Before relying on two bits, verify the actual focus, that training fits in coherence time, and that the remaining SNR margin survives coupling and loss.
```
::::


## 8.3 Metasurface antennas

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


## 8.4 Metasurface lenses and orbital angular momentum

Instructor booklet, pages 218–223.

A dielectric lens changes phase through thickness or optical path length. Bulk and weight, especially at longer wavelengths, and the mismatch between curved shapes and flat PCB or semiconductor fabrication limit its use. A **metalens** applies a phase jump at a thin discontinuity.

## 8.4.1 Designing flat metalenses

**Focusing phase profile.** A point feed at $(0,0,-F)$ illuminates the plane $z=0$. At radius $r=\sqrt{x^2+y^2}$, the path and incident phase are

$$
d(r)=\sqrt{F^2+r^2},\qquad \phi_{\rm inc}(r)=-k_0d(r),\qquad k_0=\frac{2\pi}{\lambda_0}.
$$

For a plane output wave, require $\phi_{\rm inc}(r)+\Phi(r)=\Phi_0$. Use the center as the reference so that $\Phi(0)=0$ and $\Phi_0=-k_0F$. With $t=e^{i\Phi}$, the design-frequency hyperbolic phase of the aplanatic metalens is

$$
\Phi_{\rm coll}(r)=k_0\left(\sqrt{F^2+r^2}-F\right)\pmod{2\pi}.
$$

**Off-axis metalens.** For a tilted output beam, generalized Snell matching adds the tangential phase gradient of that plane wave to the radial term.

$$
\Phi(x,y)=\Phi_{\rm coll}(r)-k_0(x\sin\theta_0\cos\phi_0+y\sin\theta_0\sin\phi_0).
$$

The first term compensates curvature and the second sets direction. Combining both in a subwavelength layer is useful for microwave and terahertz transmitters.

## 8.4.2 Gradient-index metasurface lenses (Luneburg and Maxwell fisheye)

**Index profile.** In a gradient-index (GRIN) lens, varying the cells gradually changes the phase constant along the in-plane path. The Luneburg lens of radius $R$ has

$$
n(r)=\sqrt{2-(r/R)^2},\quad 0\le r\le R,\qquad
n_{\rm MF}(r)=\frac{2}{1+(r/R)^2}.
$$

The Luneburg index falls from $\sqrt2$ at the center to $1$ at the rim. Index continuity helps matching. In a real structure the impedance and guided-to-free-space transition also matter. The normalized Maxwell fisheye profile falls from $2$ to $1$ and in its ideal model gives point-to-point imaging.

**Multi-beam coverage.** In the Luneburg ray model a rim feed produces a collimated beam facing the opposite side. Rim feeds can select directions over a full turn or form simultaneous beams with a fixed lens. Metal patch density, slot size, or etch depth on a uniform dielectric can approximate the profile.

## 8.4.3 Orbital angular momentum (OAM) and spatial multiplexing

**Spin and orbital contributions.** Spin angular momentum (SAM) describes field-vector rotation in circular polarization, with two circular states labeled $s=\pm1$. OAM describes the spatial **helical wavefront**. Phase $\psi(\varphi)=l\varphi$ winds around the axis with integer topological charge $l$.

**Orthogonality and multiplexing.** With full azimuthal sampling and appropriate weighting,

$$
\frac{1}{2\pi}\int_0^{2\pi} e^{i(l_1-l_2)\varphi}\,d\varphi=\delta_{l_1,l_2}.
$$

Independent streams can therefore occupy separate modes at the same frequency and polarization. Mathematical orthogonality alone leaves usable channel count and capacity undetermined. Both terminals and sufficient power per mode are required.

**Synthesizing a vortex beam.** Dividing the surface into angular sectors approximates this profile.

$$
\Phi_{\rm OAM}(r,\varphi)=l\varphi+\Phi_{\rm focusing}(r).
$$

For a pure scalar $l\ne0$ mode, continuity and undefined azimuth on axis require the field to vanish there. A donut-shaped beam can result.

## 8.4.4 Practical limits of OAM links

1. **Beam divergence.** Among zero-radial-order beams with a common waist, the ring angle grows roughly as $\sqrt{\lvert l\rvert}$. A larger aperture collects more power.

2. **Sensitivity to misalignment.** Aperture displacement or tilt changes angular sampling and creates modal crosstalk. Fixed point-to-point line-of-sight backhaul is an example application for evaluating high-rate links.

## Worked problem on lenses, tilted beams, and OAM

::::{admonition} Try it first
:class: book-exercise

In a data-center line-of-sight link, a circular transmissive phase sheet of radius $R=30\,\mathrm{mm}$ lies at $z=0$. The feed at $(0,0,-F)$ with $F=40\,\mathrm{mm}$ illuminates it at $60\,\mathrm{GHz}$. Assume an ideal phase-only sheet.

1. Find the phase at $(15,0,0)\,\mathrm{mm}$ for an axial beam and a $30^\circ$ beam tilted toward $+x$.
2. Find the index at the center, halfway point, and rim of a Luneburg lens of this radius, and explain the effect of moving the feed.
3. What phase is required for modes $l=0$ and $l=+1$ at the same polarization? Does orthogonality survive if the receiver sees half the azimuths?
4. The beam width parameter at the receive plane is $w=60\,\mathrm{mm}$. What fraction of each mode's power enters a coaxial aperture $a=w/\sqrt2$?

```{dropdown} Show the full worked answer

### 1. Axial and tilted beams

At $60\,\mathrm{GHz}$, $\lambda_0\simeq5\,\mathrm{mm}$. The radial phase compensates the path phase. Direct substitution gives $-k_0d+\Phi_{\rm coll}=-k_0F$. At $r=15\,\mathrm{mm}$,

$$
\Delta d=\sqrt{40^2+15^2}-40\simeq2.720\,\mathrm{mm},\qquad
\Phi_{\rm coll}\simeq360^\circ\frac{2.720}{5}=195.8^\circ.
$$

In the reciprocal model, a plane wave incident from the other side focuses at the feed. The finite aperture determines angular width and spot size. For the $30^\circ$ beam in the $+x$ direction, add the linear phase.

$$
\Phi_{\rm off}=\Phi_{\rm coll}-k_0 x\sin30^\circ
=195.8^\circ-540^\circ\equiv15.8^\circ\pmod{360^\circ}.
$$

The real cell must realize that profile with adequate transmission amplitude. Broadband operation also depends on amplitude and phase dispersion.

### 2. Selecting the direction with a Luneburg lens

| Position | Calculation | Index |
| --- | --- | --- |
| Center, $r=0$ | $\sqrt2$ | $1.414$ |
| Halfway, $r=15\,\mathrm{mm}$ | $\sqrt{2-0.5^2}$ | $1.323$ |
| Rim, $r=30\,\mathrm{mm}$ | $\sqrt{2-1^2}$ | $1.000$ |

In the ideal model a $+x$ rim feed produces a beam toward $-x$. Moving it to $+y$ produces a beam toward $-y$. Selecting a rim feed changes direction using the same profile. Check impedance matching at the rim separately. A Maxwell fisheye with center index $2$ is for point-to-point imaging, with a different function from Luneburg rim-to-beam collimation.

### 3. Generating and separating modes

$$
\Phi_l(r,\varphi)=\Phi_{\rm coll}(r)+l\varphi\pmod{2\pi}.
$$

At $l=0$ the azimuthal phase is constant. At $l=+1$ the unwrapped phase at azimuths $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$ takes those four values and advances $360^\circ$ in a complete turn. Both modes can share the same linear polarization. The on-axis null holds for a pure scalar $l\ne0$ mode. Adding $l=0$ can fill it.

A receiver extracts mode $m$ by weighting by $e^{-im\varphi}$ and summing. Full coverage gives zero angular overlap. For a uniformly weighted half circle,

$$
C_{01}(2\pi)=\frac{1}{2\pi}\int_0^{2\pi}e^{i\varphi}\,d\varphi=0,\qquad
C_{01}(\pi)=\frac1\pi\int_0^\pi e^{i\varphi}\,d\varphi=\frac{2i}{\pi},\quad
\lvert C_{01}(\pi)\rvert\simeq0.637.
$$

Asymmetric reception or misalignment can mix modes. The $0.637$ is angular overlap. Physical crosstalk also depends on radial profiles, powers, and processing. A passive single-feed surface can distribute a signal over several modes. **Two independent streams** require two independent signals.

### 4. Power collected by a finite aperture

Approximate the fundamental and zero-radial-order vortex intensities at radius $\rho$ by

$$
I_0(\rho)\propto e^{-2\rho^2/w^2},\qquad
I_1(\rho)\propto\frac{2\rho^2}{w^2}e^{-2\rho^2/w^2}.
$$

Using ring area weight $\rho\,d\rho$, substitute $u=2\rho^2/w^2$ and $U=2a^2/w^2$ to obtain the normalized integrals.

$$
\eta_0=\int_0^U e^{-u}\,du=1-e^{-U},\qquad
\eta_1=\int_0^U ue^{-u}\,du=1-(1+U)e^{-U}.
$$

For $a\simeq42.4\,\mathrm{mm}$, $U=1$.

| Mode | Collected power fraction | Aperture loss |
| --- | --- | --- |
| $l=0$ | $1-e^{-1}\simeq63.2\%$ | $2.0\,\mathrm{dB}$ |
| $l=+1$ | $1-2e^{-1}\simeq26.4\%$ | $5.8\,\mathrm{dB}$ |

For equal total power the aperture collects about $3.8\,\mathrm{dB}$ less from the vortex mode. A small coaxial aperture still has azimuthal symmetry. Evaluate **power loss and modal mixing** separately. In this beam family the ring radius is roughly $w\sqrt{\lvert l\rvert/2}$. A growing $w$ or larger $\lvert l\rvert$ calls for a larger aperture. Radial compensation plus a linear gradient gives a directional beam. A Luneburg lens selects direction by feed position. An OAM link needs checks on both collected power and separation.
```
::::


## 8.5 Space–time-modulated metasurfaces and Lorentz reciprocity breaking

Instructor booklet, pages 223–229.

The **Lorentz reciprocity theorem** gives $S_{ij}=S_{ji}$ for a linear time-invariant system with reciprocal materials and consistently normalized ports. Exchanging the source and receiver at those ports leaves the transfer coefficient unchanged. Isolators and circulators require directional transfer. In in-band full duplex (IBFD), for example, a shared antenna must radiate transmitter power while protecting the low-noise amplifier (LNA) from leakage.

Ferrimagnetic circulators using materials such as YIG use magnetic bias. Bias and packaging can add volume, weight, and cost. CMOS integration and operation at millimeter-wave and terahertz frequencies are challenging. **Traveling-wave space–time modulation** provides a route to magnetless nonreciprocity.

## 8.5.1 Space–time modulation model

The impedance or reflection coefficient depends on position $x$ and time $t$. For traveling pump phase $\omega_m t-\beta_m x$, expand the local reflection coefficient as a Fourier series. A cosine is the simple zero-phase, single-harmonic case.

$$
\Gamma(x,t)=\sum_{n=-\infty}^{\infty}\Gamma_n e^{in(\omega_m t-\beta_m x)},\qquad
\omega_m=\frac{2\pi}{T_m},\quad\beta_m=\frac{2\pi}{p},\quad v_m=\frac{\omega_m}{\beta_m}.
$$

Here $T_m$ is the pumping period, $p$ the spatial period, and $v_m$ the phase speed of the pattern. For a single-tone incident wave with $k_{x0}=k_0\sin\theta_i$, local multiplication by $\Gamma$ gives

$$
\psi_{\rm inc}=A e^{i(\omega_0t-k_{x0}x)},\qquad
\psi_{\rm ref}=\sum_n A\Gamma_n e^{i[(\omega_0+n\omega_m)t-(k_{x0}+n\beta_m)x]}.
$$

**Frequency shifting** and **angular dispersion** occur together. The surface acts as a mixer and a beam deflector.

$$
\omega_n=\omega_0+n\omega_m,\qquad k_{xn}=k_{x0}+n\beta_m,\qquad
\sin\theta_{r,n}=\frac{k_0\sin\theta_i+n\beta_m}{(\omega_0+n\omega_m)/c}.
$$

This angle applies to a positive-frequency propagating order. An order with $\lvert k_{xn}\rvert>k_n$ is evanescent in the infinite-sheet model.

## 8.5.2 Harmonics and the nonreciprocity mechanism

In the figure, a carrier illuminates the metasurface patch array. Periodic drive varies the unit-cell response with time. The upper view shows free-space channels, and the lower view shows the cell mounted on a substrate and the sideband spectrum. The quantities $f_m$ and $\beta_m$ set frequency spacing and tangential momentum shifts.

```{figure} ../../assets/chapter-08/space-time-sidebands.svg
:alt: Incident wave, metasurface patch on a substrate, time-varying drive, and outgoing harmonics

Figure 8–5. Original teaching redraw of space–time modulation. Arrow directions and sizes are schematic.
```

To test reciprocity, transmit backward from the receiving port at $f_0+f_m$. The signal wavevector reverses while the pump retains its direction. Downconversion can then produce different tangential momentum and miss the original port. Thus specific ports can give $S_{2\leftarrow1}\ne S_{1\leftarrow2}$. Observing a sideband alone is insufficient.

## 8.5.3 Physical-layer applications

**In-band full duplex (IBFD).** Simultaneous transmission and reception at the same frequency can avoid time-division (TDD) or frequency-division (FDD). The spectral benefit depends on **self-interference** and each direction's data rate. With $30\,\mathrm{dBm}$ transmit power and a $\mathord{-90}\,\mathrm{dBm}$ limit, the suppression budget is $120\,\mathrm{dB}$. Isolation of order $40$ to $50\,\mathrm{dB}$ contributes to the budget, alongside analog suppression and receiver processing.

**Direct digital modulation in the air.** A conventional transmitter has an I/Q modulator, local oscillator, mixer, and PA before the antenna. In this architecture, single-tone CW illuminates the sheet and a digital code, for example from an FPGA, drives PIN diodes or varactors. Changing the desired harmonic's complex coefficient gives BPSK, QPSK, or, with amplitude and phase control, 16-QAM. A carrier source, drivers, and filtering remain part of the system.

**Doppler offset compensation.** Relative motion shifts the received frequency. A communications receiver can estimate the offset in its own link and correct it by rotating baseband samples. In monostatic reflection measurements, the factor of two in the Doppler relation comes from the round trip.

## 8.5.4 Fabrication and implementation challenges

1. **Modulation speed.** Large microwave and millimeter-wave frequency shifts require fast switching. Diode capacitance, switching loss, and pump-path synchronization impose limits.
2. **Spurious harmonics.** Other orders can take power and interfere with adjacent channels. A sinusoidal drive or four-phase code can reduce some orders. Measure the nonlinear cell response and each order's spectrum.

## Worked problem on frequency conversion and reciprocity

::::{admonition} Try it first
:class: book-exercise

An infinite reflecting metasurface lies at $z=0$, with free space on both sides and incidence in the $xz$ plane. For $f_0=10\,\mathrm{GHz}$ and $k_0=2\pi f_0/c$, take $k_{x,{\rm in}}=0.25k_0$. In the local multiplication model,

$$
\Gamma(x,t)=0.40+0.50\cos(\omega_m t-\beta_m x),\qquad f_m=200\,\mathrm{MHz},\quad\beta_m=0.70k_0.
$$

1. Find the reflected orders' frequencies, angles, and field amplitudes.
2. Exchange the upper-sideband forward and reverse ports and test reciprocity.
3. How can the upper sideband carry QPSK?
4. Is $45\,\mathrm{dB}$ isolation sufficient for a $30\,\mathrm{dBm}$ transmitter and $\mathord{-90}\,\mathrm{dBm}$ interference limit? Discuss implementation limits.

```{dropdown} Show the full worked answer

### 1. Floquet frequencies, momenta, and angles

Angles follow the sign of $k_x$ and the incident angle is $14.5^\circ$. Expanding the cosine yields two coefficients of $0.25$ for orders $\pm1$.

$$
f_n=f_0+nf_m,\qquad k_{x,n}=k_{x,{\rm in}}+n\beta_m,\qquad k_n=2\pi f_n/c.
$$

| Order | Frequency | $k_{x,n}/k_0$ | $k_n/k_0$ | Reflection angle | Relative field amplitude |
| --- | --- | --- | --- | --- | --- |
| $\mathord{-1}$ | $9.8\,\mathrm{GHz}$ | $\mathord{-0.45}$ | $0.98$ | $\mathord{-27.3^\circ}$ | $0.25$ |
| $0$ | $10.0\,\mathrm{GHz}$ | $\mathord{+0.25}$ | $1.00$ | $\mathord{+14.5^\circ}$ | $0.40$ |
| $\mathord{+1}$ | $10.2\,\mathrm{GHz}$ | $\mathord{+0.95}$ | $1.02$ | $\mathord{+68.6^\circ}$ | $0.25$ |

All three orders propagate. Orders $\lvert n\rvert\ge2$ have no Fourier coefficient in this model. A nonsinusoidal response or inter-order coupling can generate them in real cells. **Power check.** If the coefficients are TE electric field ratios, normal power flux also depends on the cosine of the angle.

$$
\frac{P_{+1,\perp}}{P_{{\rm in},\perp}}
=0.25^2\frac{\cos68.6^\circ}{\cos14.5^\circ}\simeq2.4\%.
$$

Squaring the field ratio alone leaves the power efficiency incomplete. A full balance includes transmission, loss, and energy exchange with the pump.

### 2. Which wavevector reverses?

Port 1 illuminates at $10.0\,\mathrm{GHz}$ with $k_x=+0.25k_0$. Port 2 receives the $10.2\,\mathrm{GHz}$ output at $k_x=+0.95k_0$. Reverse excitation from the same Port 2 has $k_x=-0.95k_0$. Hold the pump fixed. Order $-1$ returns the frequency to $10.0\,\mathrm{GHz}$ and gives

$$
k_{x,{\rm back}}=-0.95k_0-0.70k_0=-1.65k_0.
$$

Returning to Port 1 requires $-0.25k_0$. The calculated order is outside the radiation cone. In the ideal model $S_{2\leftarrow1}\ne0$ and $S_{1\leftarrow2}=0$. Reversing $\beta_m$ restores that path with a different bias. A spatially uniform pump, $\beta_m=0$, still generates sidebands but lacks this directional separation mechanism. A single zero channel gives no total reflected-power budget.

### 3. Direct QPSK modulation

Hold the pump at one of four phases during each symbol.

$$
\varphi_b\in\{0,\pi/2,\pi,3\pi/2\},\quad
\Gamma_b=0.40+0.50\cos(\omega_m t-\beta_m x+\varphi_b),\quad
a_{+1}=0.25e^{i\varphi_b}.
$$

| Gray-coded bits | Pump phase | Upper sideband coefficient |
| --- | --- | --- |
| 00 | $0^\circ$ | $0.25$ |
| 01 | $90^\circ$ | $+i0.25$ |
| 11 | $180^\circ$ | $\mathord{-0.25}$ |
| 10 | $270^\circ$ | $-i0.25$ |

With a single $10\,\mathrm{GHz}$ carrier, QPSK occupies the band around $10.2\,\mathrm{GHz}$. Fixed $\beta_m$ preserves the $68.6^\circ$ beam center. The lower sideband has coefficient $0.25e^{-i\varphi_b}$ and the carrier remains. Angle selection and filtering still matter. 16-QAM also requires coefficient magnitude control.

**Connection to Doppler.** If the receiver estimates a $+2\,\mathrm{kHz}$ offset, it compensates at baseband after downconversion by multiplying samples by $e^{-i2\pi(2000)t}$. This recovers the data in the receiver's own link.

### 4. Full-duplex self-interference budget

$$
P_{\rm leak}=30-45=-15\,\mathrm{dBm},\qquad
A_{\rm additional}=(-15)-(-90)=75\,\mathrm{dB}.
$$

Some suppression must precede LNA or ADC saturation. Digital cancellation cannot recover saturation distortion. The ideal zero for one frequency–direction port pair leaves three-port circulator or full-system isolation undetermined. Measure carrier leakage and other sidebands as well.

### 5. What should the experiment measure?

- **Pump timing and cell-to-cell phase.** Here $T_m=5\,\mathrm{ns}$ and $p=\lambda_0/0.70\simeq42.9\,\mathrm{mm}$. Timing and phase errors can broaden or deflect the beam. The pump and drivers require power.
- **Spurious harmonics.** Nonlinear diode response can turn sinusoidal voltage into a nonsinusoidal $\Gamma$. Measure power in the desired and neighboring bands.
- **Finite size.** Edges and fabrication errors spread $k_x$ and can fill the reverse null. Measure coefficients at the same two ports with the pump held fixed.

Pump frequency sets the sideband spacing, spatial period sets the direction, and pump phase encodes the data. The reciprocity test compares exchanged ports at the same bias.
```
::::


## 8.6 Sensing, precision localization, and integrated sensing and communications (ISAC)

Instructor booklet, pages 230–236.

## 8.6.1 Integrating sensing and communications

Radar uses pulses or frequency-modulated continuous waves (FMCW) to estimate delay, angle, and Doppler. Wireless links value throughput and bit error rate (BER), for example with OFDM. In millimeter-wave and sub-terahertz bands, spectrum is valuable and short wavelength improves angular resolution for a given aperture. Bandwidth sets delay resolution.

**Integrated sensing and communications** (ISAC) shares resources. A waveform good for throughput can have substantial correlation sidelobes. This **trade-off** extends beyond waveform and timing. A RIS or holographic DMA can shape communication beams and sensing patterns, with shared power and degrees of freedom.

## 8.6.2 RIS-aided angle estimation and localization

**Array steering and reception.** A RIS can act as a known **anchor** in a non-line-of-sight (NLoS) path. Take a uniform planar array (UPA) in the $xy$ plane with $M=M_xM_y$ cells and $d_x=d_y=\lambda/2$. Here $\theta_t$ is measured from the positive normal and $\phi_t$ from $+x$.

$$
\mu_x=\frac{2\pi d_x}{\lambda}\sin\theta_t\cos\phi_t,\qquad
\mu_y=\frac{2\pi d_y}{\lambda}\sin\theta_t\sin\phi_t.
$$

For a cell ordering consistent with the Kronecker product $\otimes$, the steering vector is

$$
\mathbf a=\mathbf a_x\otimes\mathbf a_y\in\mathbb C^{M\times1},\qquad
\mathbf a_x=[1,e^{-i\mu_x},\ldots,e^{-i(M_x-1)\mu_x}]^T,\quad
\mathbf a_y=[1,e^{-i\mu_y},\ldots,e^{-i(M_y-1)\mu_y}]^T.
$$

A single RIS crossing can be written as $\mathbf H_{\rm out}\mathbf\Phi\mathbf H_{\rm in}$. An echo with two crossings uses a RIS matrix and corresponding channels for each pass. With $\mathbf H_{\rm path}$ denoting the full path response,

$$
y(t)=\alpha\,\mathbf w^H\mathbf H_{\rm path}\mathbf f\,s(t-\tau)e^{i2\pi f_dt}+n(t),
\qquad
\mathbf\Phi=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_M}).
$$

Here $\mathbf f$ and $\mathbf w$ are transmit and receive weights. The complex $\alpha$ represents target scattering and path factors omitted from $\mathbf H_{\rm path}$. Radar cross section (RCS) is a power-domain quantity. Delay $\tau$ comes from the **total path**. For a simple monostatic case, $\tau=2R/c$ and $f_d=2v\cos\psi/\lambda$, with positive sign for approach. The noise model is $n(t)\sim\mathcal{CN}(0,\sigma^2)$.

**Cramér–Rao lower bound (CRLB).** For angle of arrival (AoA), let $\boldsymbol\theta=[\theta_t,\phi_t]^T$ and let $\boldsymbol\mu_k$ be the complex sample mean. With independent noise and real parameters, the Fisher information matrix (FIM) and unbiased-estimator bound are

$$
\mathbf J_F=\frac{2}{\sigma^2}\operatorname{Re}\sum_{k=1}^K
\left(\frac{\partial\boldsymbol\mu_k}{\partial\boldsymbol\theta}\right)^H
\left(\frac{\partial\boldsymbol\mu_k}{\partial\boldsymbol\theta}\right),\qquad
\operatorname{Cov}(\widehat{\boldsymbol\theta})\succeq\mathbf J_F^{-1}.
$$

Include other unknown parameters in the information matrix and take the corresponding block of its inverse. In the ideal coherent two-pass model, echo amplitude can scale as $M^2$ and power as $M^4$. **Angular information** also depends on pattern derivatives, aperture, and the noise model. Receive SNR already includes path gain.

## 8.6.3 Computational imaging with a dynamic metasurface

**Compressed sensing.** In synthetic aperture radar (SAR), aperture motion provides spatial samples. A programmable metasurface can instead use different phase or amplitude patterns with a **single-pixel receiver**. For pattern $p$, $g_p$ is the calibrated illumination-and-reception kernel and $\sigma$ the scene reflectivity.

$$
y_p=\iiint_{\mathcal V}g_p(\mathbf r)\sigma(\mathbf r)\,d^3\mathbf r+n_p,\qquad
\mathbf y=\mathbf A\boldsymbol\sigma+\mathbf n,\quad \mathbf A\in\mathbb C^{P\times N}.
$$

**Reconstruction by $\ell_1$ minimization.** If $P\ll N$, exploit sparsity in the scene or a suitable representation such as wavelets. For direct sparsity,

$$
\min_{\boldsymbol\sigma}\lVert\boldsymbol\sigma\rVert_1
\quad\text{s.t.}\quad
\lVert\mathbf y-\mathbf A\boldsymbol\sigma\rVert_2\le\epsilon.
$$

Pattern diversity, calibration, measurement count, and solve time determine whether single-receiver imaging is practical and timely.

## 8.6.4 Comparing sensing and communications architectures

| Criterion | Passive reflecting RIS | Active or simultaneous-sensing RIS | Dynamic metasurface antenna (DMA) |
| --- | --- | --- | --- |
| Role | Virtual line-of-sight path and environment control | Reflection and local sampling, or amplification | Waveguide-fed transmit/receive antenna |
| RF chains | No receive chain on the surface | A few dedicated sensing nodes | A few RF chains and baseband processing |
| Power | Mainly control and switching | Higher with sensors or amplifiers | Can be lower than a fully digital array |
| Localization | Centralized at the base station | Local or distributed measurement | Near-field localization and imaging |
| Complexity | Surface control and calibration | Bias, sensors, and synchronization | Feed and pattern control |
| Application | Blind-spot coverage | Environment monitoring and cooperative ISAC | Compact imager or base station |

## 8.6.5 Research directions for metasurfaces and ISAC

**1. Near-field ISAC.** For an extremely large surface (XL-RIS), the approximate Rayleigh or Fraunhofer distance $2D^2/\lambda$ increases. A spherical-wave model retains both range and angle dependence. Point focusing and same-angle range separation depend on aperture, SNR, and calibration. Bandwidth still matters for delay estimation.

**2. Edge AI.** A controller near the surface can select the next pattern based on target estimates and uncertainty. Deep reinforcement learning is a research option. Measure decision latency, training cost, and improvement over a simple policy.

## Worked problem on localization and imaging behind an obstruction

::::{admonition} Try it first
:class: book-exercise

A metal shelf blocks the direct path from a base station to a cart in a warehouse. A wall-mounted RIS sees both. The station sends data and uses known OFDM symbols for sensing. Take $f_c=30\,\mathrm{GHz}$ and $B=1\,\mathrm{GHz}$. A $16\times16$ RIS with $\lambda/2$ pitch lies in the $xy$ plane centered at the origin. The station is at $(0,0,4)\,\mathrm m$ and the target at $z>0$. The echo travels station, RIS, cart, RIS, station. After calibration, $\tau=113.33\,\mathrm{ns}$ and $f_d=+200\,\mathrm{Hz}$. Pattern fitting gives $u_x=3/13$ and $u_y=4/13$. Each $0.5\,\mathrm{ms}$ cycle has four $25\,\mathrm{\mu s}$ sensing patterns and a data interval. Observe for $40$ cycles.

Find position and radial speed, range resolution, and the angle accuracy bound. Reconstruct a sparse scene with one receive channel and discuss changes in architecture and aperture.

```{dropdown} Show the full worked answer

### 1. Combining path length and direction

The wavelength is $\lambda=c/f_c=0.01\,\mathrm m$. The round-trip distance is $2(4\,\mathrm m+R)$, so

$$
R=\frac{c\tau}{2}-4\,\mathrm m\simeq13.0\,\mathrm m,\qquad
\mu_x=\frac{3\pi}{13},\quad\mu_y=\frac{4\pi}{13}.
$$

The quantity $c\tau/2\simeq17\,\mathrm m$ is the one-way path length via the RIS. Adjacent steering-vector phases in $x$ and $y$ change by $-41.5^\circ$ and $-55.4^\circ$. The station infers them from calibrated patterns.

$$
\theta=\arcsin(5/13)\simeq22.6^\circ,\quad \phi=\operatorname{atan2}(4,3)\simeq53.1^\circ,\quad
u_z=+\sqrt{1-u_x^2-u_y^2}=\frac{12}{13},\quad
\mathbf r\simeq[3,4,12]^T\,\mathrm m.
$$

Knowledge of the target half-space resolves the sign of $u_z$.

### 2. Doppler, resolution, and data time

$$
v_{\rm toward}=\frac{\lambda f_d}{2}=1.0\,\mathrm{m/s},\quad
\Delta R\simeq\frac{c}{2B}=0.15\,\mathrm m,\quad
\Delta f_d\simeq\frac{1}{40(0.5\,\mathrm{ms})}=50\,\mathrm{Hz}.
$$

Speed is the component toward the RIS. The $15\,\mathrm{cm}$ is nominal separation of two echoes. A $50\,\mathrm{Hz}$ Doppler bin corresponds to $0.25\,\mathrm{m/s}$ with coherent phase and nearly constant speed. Four patterns take $100\,\mathrm{\mu s}$, leaving $80\%$ for communications. At $2\,\mathrm{Gbit/s}$ during the data interval, the average is $1.6\,\mathrm{Gbit/s}$. More patterns may improve angular information at the cost of data time. Simultaneous beams share power and degrees of freedom.

### 3. Cramér–Rao angle bound

After Doppler phase compensation, use the following model for four calibrated responses near the nominal direction. Offsets $\delta\theta,\delta\phi$ are in radians, $\alpha$ is the unknown complex coefficient, and $\sigma^2$ is the independent complex noise variance. Slopes $8$ and $4$ are assumed calibration values. At the center $\rho=\lvert\alpha\rvert^2/\sigma^2=100$, or $20\,\mathrm{dB}$, with $K=40$ repeats.

$$
\mathbf y=\alpha[1+8\delta\theta,\ 1-8\delta\theta,\ 1+4\delta\phi,\ 1-4\delta\phi]^T+\mathbf n.
$$

The first two outputs differ by $16\alpha\delta\theta$ plus noise. The derivative vectors are orthogonal to the common response, so unknown $\alpha$ leaves the local angle bound unchanged at the nominal point.

$$
\mathbf J_{\rm angle}=4K\rho\,\operatorname{diag}(64,16),\qquad
\operatorname{std}(\widehat\theta)\ge\frac{1}{8\sqrt{4K\rho}}\simeq0.057^\circ,\qquad
\operatorname{std}(\widehat\phi)\ge\frac{1}{4\sqrt{4K\rho}}\simeq0.113^\circ.
$$

At fixed range the bounds imply roughly $1.3\,\mathrm{cm}$ and $1.0\,\mathrm{cm}$ tangential offsets through $R\,\operatorname{std}(\widehat\theta)$ and $R\sin\theta\,\operatorname{std}(\widehat\phi)$. Range, calibration, and multipath errors are separate. A strong beam can have a shallow slope at its center. Coherent gain alone therefore gives no universal $J_F\propto M^4$ law.

### 4. Three patterns for four scene bins

In the noiseless case, record one complex sample per pattern. The rows of $\mathbf A$ are calibrated responses over the four bins.

$$
\mathbf y=\mathbf A\boldsymbol\sigma,\quad
\mathbf A=\begin{bmatrix}1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{bmatrix},\quad
\mathbf y=[2,-2,-2]^T.
$$

The data are twice the second column. The columns sum to zero and the rank is $3$, so all solutions take the form $[t,2+t,t,t]^T$.

$$
\lVert\boldsymbol\sigma\rVert_1=3\lvert t\rvert+\lvert 2+t\rvert
\ge 2+2\lvert t\rvert,\qquad
\widehat{\boldsymbol\sigma}=[0,2,0,0]^T.
$$

The minimum is at $t=0$ and the second bin contains the reflector. With noise, use constraint $\lVert\mathbf y-\mathbf A\boldsymbol\sigma\rVert_2\le\epsilon$. Nearly identical columns can defeat separation even with apparently random patterns.

### 5. Architecture and the shift to near field

| Architecture | Role in the warehouse |
| --- | --- |
| Passive RIS | Path behind shelf, with sampling at the station |
| Sensing RIS | Local receive channels for estimation or calibration, with added power and synchronization |
| DMA | Imaging patterns at the station with a few RF chains, with a separate path around the obstruction |

$$
D\simeq\sqrt2\,(15\lambda/2)=0.106\,\mathrm m,\qquad R_F\simeq2D^2/\lambda=2.25\,\mathrm m.
$$

Both $4$ and $13\,\mathrm m$ exceed this boundary. With $D=1\,\mathrm m$, it rises to $200\,\mathrm m$. Model each cell's distance to the source and target. Wavefront curvature can separate targets at the same angle but different ranges. In edge processing, direct the next four patterns near the estimate when uncertainty is low and scan more widely as uncertainty rises. Compare the benefit with decision latency and lost data time. **Takeaway.** Delay gives path length, pattern slope gives direction, and Doppler gives path-length rate.
```
::::


## 8.7 Operational challenges, industry outlook, and integration into 6G

Instructor booklet, pages 236–242.

Reconfigurable intelligent surfaces (RIS/IRS) and holographic antennas (DMAs) are two routes to a **smart and programmable radio environment**. Moving from the laboratory to a network requires assessing hardware, channel estimation, control protocols, and deployment cost together.

## 8.7.1 Hardware bottlenecks and physical limits

**1. Mutual coupling.** Currents on neighboring cells interact in a dense surface. For example, a local effective model is $\Gamma_n=f(V_n,\{V_m\}_{m\in\mathcal N_n})$, with neighbor set $\mathcal N_n$. Adjusting adjacent cells can change the response of cell $n$. A diagonal matrix of independent coefficients misses this dependence. Multi-cell models and pattern calibration help beamforming.

**2. Phase–amplitude coupling.** Series resistance $R_s$, dielectric loss, and resonance in varactor- or PIN-loaded cells cause amplitude to vary with phase. An empirical fit is

$$
\Gamma_n(\theta_n)=\alpha_n(\theta_n)e^{i\theta_n},\qquad
\alpha_n(\theta_n)=(1-\alpha_{\min})\left[\frac{\sin(\theta_n-\theta_0)+1}{2}\right]^\gamma+\alpha_{\min}.
$$

Here $\alpha_{\min}$ is minimum amplitude, $\theta_0$ a fitted phase offset, and $\gamma>0$ a shape parameter. This form reaches its minimum at $\theta_0-\pi/2$. Calculate beamforming gain from the **sum of measured complex fields**.

**3. Spatial beam squint.** A common design sets a phase gradient at $f_0$ and holds it constant across the band. For normal incidence and target angle $\theta_0$,

$$
\sin\theta(f)=\frac{f_0}{f}\sin\theta_0.
$$

The gain toward the user can fall at band edges. **True time delay** (TTD) applies a phase difference proportional to frequency, $-2\pi f\Delta\tau$. Broadband elements with suitable phase slopes can approximate it.

## 8.7.2 Channel state acquisition and cascaded-channel overhead

A passive RIS has no on-surface receive RF chain or ADC. The receiver estimates the effective channel using pilots and changes of surface pattern. For an $M$-antenna station, a single-antenna user and an $N$-cell surface,

$$
\mathbf h_{\rm total}=\mathbf h_d+\mathbf h_r^H\mathbf\Phi\mathbf G,\qquad
\mathbf v=[\beta_1e^{i\theta_1},\ldots,\beta_Ne^{i\theta_N}]^T,\qquad
\mathbf\Phi=\operatorname{diag}(\mathbf v).
$$

Here $\mathbf h_d\in\mathbb C^{1\times M}$ is the direct channel, $\mathbf G\in\mathbb C^{N\times M}$ the station-to-surface channel, and $\mathbf h_r^H\in\mathbb C^{1\times N}$ the surface-to-user channel. Rearranging the diagonal product gives

$$
\mathbf H_{\rm cas}=\operatorname{diag}(\mathbf h_r^H)\mathbf G\in\mathbb C^{N\times M},\qquad
\mathbf h_{\rm total}=\mathbf h_d+\mathbf v^T\mathbf H_{\rm cas}.
$$

Unstructured estimation has $NM$ complex cascaded coefficients and $M$ direct ones. Three methods can reduce **pilot overhead**.

- **Element grouping.** Blocks share commands, reducing dimension at the cost of wavefront control.
- **Compressed sensing.** If a few directional paths dominate, a sparse model can use fewer samples. Rich scattering or mismatch can reduce its benefit.
- **Semi-passive or hybrid RIS.** Low-power RF detectors on a few cells provide local samples. Reconstructing the rest requires informative sampling and calibration.

## 8.7.3 Technical and economic comparison with relays and reflectors

| Criterion | Flat metal reflector | Amplify-and-forward relay (AF) | Decode-and-forward relay (DF) | Passive reconfigurable RIS |
| --- | --- | --- | --- | --- |
| Control | Fixed geometry | Active amplification | Signal regeneration | Software-controlled cell state |
| Circuit power | No control power | $10$ to $100\,\mathrm W$ in booklet examples | Over $50\,\mathrm W$ in high-power examples | Milliwatts to a few watts of control power in small examples |
| Noise | Loss and thermal environment | Amplified input noise and added receiver noise | Detection and fresh transmission with possible decoding errors | No active amplification of noise |
| RF circuitry | No RF chain | LNA and PA | Baseband processing and modulator | No mixer or RF amplifier in the passive type |
| Duplex and interference | Scattering in both directions | Half-duplex or full-duplex with leakage suppression | Buffer and scheduling depend on the architecture | Two-way reflection in reciprocal designs, with possible changes to interference paths |
| Path loss | Mirror law $(d_1+d_2)^{-2}$ in a large-aperture approximation | Two hop gains, noise, and relay gain | Reception on the first hop and fresh transmission on the second | $(d_1d_2)^{-2}$ in a simple far-field model with fixed effective aperture |
| Cost | Typically simple to fabricate | Active hardware and power supply | More processing and maintenance | Depends on aperture, control, installation, and calibration |

The power figures are illustrative. Compare geometry, aperture efficiency, bandwidth, and maintenance across options. In AF, signal power follows cascaded hops while relay noise enters the budget separately.

## 8.7.4 Network requirements and integration into 6G

**1. Signaling and timely updates.** Budget channel estimation, computation, command transmission, application, and settling. In a moving environment, FPGA or ASIC control may need delays of a few milliseconds or less. A cable or auxiliary wireless channel can carry commands.

**2. Open radio access network (Open RAN).** 3GPP and the ETSI ISG RIS provide contexts for study. In a candidate O-RAN design, xApps or rApps in the radio intelligent controller (RIC) can manage policies, pattern sets, and coordination. A learning algorithm can use user locations and traffic to select patterns. The fast local loop needs an actual latency budget.

**3. Self-sustainable RIS.** Flexible solar panels or RF energy harvesting can reduce wiring when average power and storage suffice. Compare controller, switching, interface, and idle power with harvestable energy at the location.

**Chapter synthesis.** RISs, metasurface antennas, lenses, space–time modulation, and ISAC all control fields at the surface or along the propagation path. Their benefit on a network depends on link budget, training and control overhead, and installation cost and power. The next problem evaluates these together for an industrial hall.

## Worked problem on deploying a RIS in an industrial hall

::::{admonition} Try it first
:class: book-exercise

Metal shelving weakens the direct paths to moving terminals. The operator must choose among a passive RIS, a metal reflector, and a relay. The center frequency is $28\,\mathrm{GHz}$ and the band spans $26$ to $30\,\mathrm{GHz}$. The station has $M=8$ antennas and the surface has $N=32\times32=1024$ cells with pitch $d=\lambda_0/2$. The test uses normal incidence and calls for a reflection angle of $45^\circ$ toward $+x$ in the $xz$ plane. Four contributions after removing the ideal geometric phase are $1$, $0.60$, $0.80e^{i30^\circ}$, and $0.60e^{-i30^\circ}$, compared with $1$ for each ideal contribution.

Coherence time is $2\,\mathrm{ms}$. Each pattern needs eight pilots of $1\,\mathrm{\mu s}$, and the estimate retains the direct path. After training, computation takes $0.20\,\mathrm{ms}$, command transmission $0.12\,\mathrm{ms}$, and panel settling $0.03\,\mathrm{ms}$. These stages are sequential and carry no useful data. The controller, drivers, and interface average $0.25\,\mathrm W$. Evaluate hardware loss, beam squint, update time, technology choice, and local energy supply.

```{dropdown} Show the full worked answer

### 1. Adding fields and calculating hardware loss

$$
E_{\rm real}=1+0.60+0.80e^{i30^\circ}+0.60e^{-i30^\circ}\simeq2.812+i0.100,
\qquad E_{\rm ideal}=4.
$$

$$
\frac{P_{\rm real}}{P_{\rm ideal}}=\frac{\lvert2.812+i0.100\rvert^2}{16}
\simeq0.495,\qquad L\simeq3.05\,\mathrm{dB}.
$$

Hypothetically align the phases without changing magnitudes. The sum is then $3$ and the loss $-10\log_{10}(9/16)\simeq2.50\,\mathrm{dB}$. This isolates amplitude loss. Real cells can couple amplitude and phase. The four measurements alone leave coupling undetermined. Hold one cell's command fixed, change its neighbors, and measure its response under identical illumination and reception. If it varies, use multi-cell pattern calibration or a coupled model. The $3.05\,\mathrm{dB}$ applies to **this block and pattern**.

### 2. Beam angle and power toward the user

$$
\Delta\phi_0=-k_0d\sin45^\circ=-\pi\sin45^\circ,\qquad
\sin\theta(f)=\frac{f_0}{f}\sin45^\circ.
$$

| Frequency | Beam angle from normal |
| --- | --- |
| $26\,\mathrm{GHz}$ | $49.6^\circ$ |
| $28\,\mathrm{GHz}$ | $45.0^\circ$ |
| $30\,\mathrm{GHz}$ | $41.3^\circ$ |

In the fixed user direction, sum the fields geometrically for $32$ equal-amplitude cells along $x$. Omit cell dispersion and coupling in this step.

$$
\delta=\pi(f/f_0-1)\sin45^\circ,\qquad
G_{\rm rel}=\left\lvert\frac{\sin(32\delta/2)}{32\sin(\delta/2)}\right\rvert^2
\simeq0.050.
$$

At each edge this is about $13\,\mathrm{dB}$ loss toward the user. Adding it to the four-cell loss requires a joint model. Use a true time delay to hold the direction fixed.

$$
\Delta\tau=\frac{d\sin45^\circ}{c}=\frac{\sin45^\circ}{2f_0}\simeq12.6\,\mathrm{ps},\qquad
\Delta\phi(f)=-2\pi f\Delta\tau.
$$

Compare TTD cost and loss with reducing operating bandwidth or coherent aperture size.

### 3. Training and control budget

Eight orthogonal pilots per pattern resolve the effective channel from the eight antennas. In the unstructured diagonal model, separating the direct path and $N$ reflected terms requires at least $N+1$ patterns. The pattern matrix with the constant direct-path column must have full rank.

| Option | Patterns including direct path | Pilots | Training time |
| --- | --- | --- | --- |
| $1024$ independent cells | $1025$ | $8200$ | $8.20\,\mathrm{ms}$ |
| $64$ groups of $4\times4$ cells | $65$ | $520$ | $0.52\,\mathrm{ms}$ |

Independent training exceeds four coherence intervals. For the grouped surface,

$$
T_{\rm loop}=0.52+0.20+0.12+0.03=0.87\,\mathrm{ms},\qquad
T_{\rm data}=2.00-0.87=1.13\,\mathrm{ms}.
$$

Data gets $56.5\%$ of the interval. Grouping estimates only each block's effective response. An uncompensated phase slope within a block can weaken a tilted beam. Sparse estimation with dominant paths and sensing RIS with local samples are options. The former depends on model fit and the latter on calibration and sensor count. Validate the grouped model with measured patterns under strong coupling.

### 4. Choosing a technology using net rate

The service threshold is $0.60\,\mathrm{Gbit/s}$. In the assumed trial, useful rates are $0.30$ for the reflector, $0.70$ for AF, and $0.80\,\mathrm{Gbit/s}$ for DF. RIS rate during the data interval, after hardware and bandwidth effects, is $1.20\,\mathrm{Gbit/s}$ before timing overhead.

$$
R_{\rm RIS,net}=1.20(0.565)=0.678\,\mathrm{Gbit/s}.
$$

| Option | Result in the hall | Consideration |
| --- | --- | --- |
| Fixed reflector | Below threshold | Simple and no control power. Reassess for fixed routes |
| AF | Passes threshold | Amplifies noise and needs RF chains and power |
| DF | Highest trial rate | Regeneration after decoding, with processing cost, delay, and error risk |
| Grouped RIS | Margin of $0.078\,\mathrm{Gbit/s}$ | Depends on reflection path, timely updates, and calibration |

The RIS merits a field trial. If coherence drops to $1.5\,\mathrm{ms}$ with unchanged $0.87\,\mathrm{ms}$ overhead, its rate falls to $1.20(1-0.87/1.5)=0.504\,\mathrm{Gbit/s}$, below the service threshold. Compare rate, coverage stability, installation, energy, and maintenance. A passive surface can also change self-interference paths of active equipment.

### 5. Network integration and energy budget

**Control.** Select and apply fast patterns at the surface or near the base station. A slower Open RAN layer can manage policies, pattern libraries, and panel coordination. Record settling time as well as transmission time. Provide a fallback pattern for loss of the control link. This division is a candidate architecture for the example.

**Energy.** Daily load, harvested RF power, and solar energy for the assumed data are

$$
E_{\rm load}=0.25\times24=6\,\mathrm{Wh/day},\qquad
P_{\rm RF,DC}=0.40(0.10\,\mathrm{mW})=0.04\,\mathrm{mW}.
$$

RF input is $\mathord{-10}\,\mathrm{dBm}=0.10\,\mathrm{mW}$. Harvested power is a factor of $6250$ below demand. A $1\,\mathrm W$ solar panel with four equivalent sun-hours and $80\%$ efficiency gives $3.2\,\mathrm{Wh/day}$. Minimum panel rating before low-light margin is

$$
P_{\rm panel,min}=\frac{6}{4(0.8)}=1.875\,\mathrm W.
$$

A battery shifts available energy to nighttime. The average daily shortfall remains. **Takeaway.** Test deployment readiness against wideband user-direction gain, update time, net rate, and available energy together.
```
::::
