# 8.2 Smart radio environments (SRE) and reconfigurable intelligent surfaces (RIS/IRS)

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

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
