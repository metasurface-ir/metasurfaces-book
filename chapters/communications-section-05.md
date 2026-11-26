# 8.5 Space–time-modulated metasurfaces and Lorentz reciprocity breaking

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

```{figure} ../assets/chapter-08/space-time-sidebands.svg
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

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
