# 9.4 Microwave and millimeter-wave measurement setups

Instructor booklet, pages 260–265.

After fabrication, decide **what to measure**. A modal reflection coefficient, a near-field map, and peak beam direction are different measurements. Cables, antennas, alignment, and room echoes affect them differently.

## 9.4.1 Free-space measurements and anechoic chambers

Carbon-loaded foam pyramids reduce wall reflection in an anechoic chamber. In a **monostatic** arrangement, one horn transmits and receives, usually recording raw $S_{11}$ for coaxial reflection. In a **bistatic** arrangement, the transmitter stays at $\theta_i$ and the receiving horn moves along an arc in $\theta_r$. This measures patterns for anomalous reflection.

```{figure} ../assets/chapter-09/reflection-reference.svg
:alt: Shared transmit-receive horn on the left and a separate angular receive horn on the right

Teaching schematic of reflection fixtures. In (a), one horn handles the round trip. In (b), a separate receiver moves on an arc.
```

$$
R\gtrsim 2D^2/\lambda_0.
$$

For the Fraunhofer estimate take the largest relevant aperture dimension $D$ and check the shortest sweep wavelength. In a short chamber, dielectric lenses can form a focused Gaussian beam with the sample at its waist. Check spot size, phase, amplitude, and edges.

## 9.4.2 Calibration and time gating

A vector network analyzer (VNA) measures complex response. In **TRL**, the Thru, Reflect, and Line standards determine fixture error terms. The through path, reflect standard, and phase-shifted line need consistent geometry and coupling. An added length near $\lambda/4$ gives an example one-way phase difference at design frequency. TRL performance depends on band and standard design.

In a coaxial reflection comparison with an equal-sized metal plate, subtract the background from both **complex traces**, then normalize to the reference. This is a separate step from solving TRL error terms.

$$
\Gamma_{\rm MS}\simeq-\frac{S_{\rm sample}-S_{\rm iso}}{S_{\rm ref}-S_{\rm iso}}.
$$

In **time gating**, an IFFT converts the frequency trace into delay. Apply a Hann or Tukey window around the sample pulse and use an FFT to return to frequency. Bandwidth and window shape determine delay resolution. A narrow gate can cut off a real resonance tail and cannot separate a coincident echo.

## 9.4.3 Guided measurement in a waveguide

A cell or a few cells can sit between WR-series rectangular waveguide flanges. A guided fixture provides repeatable geometry and mode excitation without a large chamber. PEC walls and the nonuniform $\mathrm{TE}_{10}$ field generally do not reproduce free-space periodic excitation. Report the mode, reference plane, and fixture.

## 9.4.4 Near-field scanning and the plane-wave spectrum

For metalenses and beams with orbital angular momentum (OAM), a complex aperture-field map exposes how the design works. An open-ended waveguide probe on an $X$–$Y$–$Z$ stage records a field component on a plane. After probe calibration, the near-to-far-field transform (NFFF) follows from the plane-wave spectrum (PWS).

$$
F(k_x,k_y)=\iint E(x,y,z_0)e^{i(k_xx+k_yy)}\,dx\,dy.
$$

Only $k_x^2+k_y^2\le k_0^2$ propagates to the far field. For a quantitative three-dimensional pattern, account for polarization, vector components, probe response, windowing, and scan aperture.

## Worked problem on measuring a 28 GHz panel

::::{admonition} Try it first
:class: book-exercise

A panel with $D=160\,\mathrm{mm}$ is measured with $50\,\mathrm{mm}$ horns at $6\,\mathrm m$. Measure coaxial reflection in the uniform state and the $+30^\circ$ beam in the beamforming state. At $28\,\mathrm{GHz}$, $S_{\rm iso}=0.010+i0.005$, $S_{\rm ref}=-0.090+i0.005$, and $S_{\rm sample}=0.010+i0.065$. A $26$ to $30\,\mathrm{GHz}$ sweep in $10\,\mathrm{MHz}$ steps gives a sample pulse at $40\,\mathrm{ns}$ and echo at $42\,\mathrm{ns}$. In WR-28 with $a=7.112,b=3.556\,\mathrm{mm}$ the states give $S_{11}=0.83\angle-20^\circ$ and $0.76\angle150^\circ$. After separating the incident field, a complex $320\times320\,\mathrm{mm^2}$ scan with $4\,\mathrm{mm}$ pitch peaks at $k_x=293\,\mathrm{rad/m},k_y\simeq0$. Determine the setups, calibrations, and meaning of each result.

```{dropdown} Show the full worked answer

### 1. Geometry and far field

$$
\lambda_0\simeq10.71\,\mathrm{mm},\quad
R_F(28\,\mathrm{GHz})\simeq4.78\,\mathrm m,\quad R_F(30\,\mathrm{GHz})\simeq5.12\,\mathrm m.
$$

The panel has the larger aperture, and $6\,\mathrm m$ passes the sweep criterion. Check amplitude uniformity and room echoes separately. Use monostatic reflection for the coaxial result and bistatic $S_{21}(\theta_r)$ for the beam. A relative pattern gives the peak. Absolute efficiency requires calibrated power and pattern integration. A focused beam can serve a local test.

### 2. Complex subtraction and reference

$$
S_{\rm sample}-S_{\rm iso}=i0.060,\qquad
S_{\rm ref}-S_{\rm iso}=-0.100,\qquad
\Gamma_{\rm MS}=i0.60=0.60\angle90^\circ.
$$

Magnitude is $20\log_{10}(0.60)\simeq-4.44\,\mathrm{dB}$ and channel power is $0.36$ relative to the plate. Remaining power can occupy other angles, polarizations, transmission, or absorption. Position error $0.5\,\mathrm{mm}$ changes the round trip by $1\,\mathrm{mm}$, or about $33.6^\circ$. A one-way increase $\lambda_0/4\simeq2.68\,\mathrm{mm}$ gives $90^\circ$ phase and serves as a Line only in a consistent fixture. At normal incidence the metal reference is coaxial. Dividing a $+30^\circ$ measurement by its weak off-axis reflection is invalid.

### 3. Time gate

$$
\Delta t_{\rm res}\sim 1/(4\,\mathrm{GHz})=0.25\,\mathrm{ns},\qquad
T_{\rm amb}=1/(10\,\mathrm{MHz})=100\,\mathrm{ns},\qquad
2R/c\simeq40\,\mathrm{ns}.
$$

Separation of $2\,\mathrm{ns}$ allows gating if the resonant tail is short enough. Subtract complex background from sample and reference, use identical IFFT and gate settings, transform back, and take the ratio. Test for truncation by making a small change in gate width and checking response stability.

### 4. Comparing waveguide-mode responses

$$
f_{c,10}=c/(2a)\simeq21.1\,\mathrm{GHz},\qquad f_{c,20}=f_{c,01}\simeq42.2\,\mathrm{GHz},\qquad
\Delta\phi=150^\circ-(-20^\circ)=170^\circ.
$$

In-band only $\mathrm{TE}_{10}$ propagates away from the sample, although higher modes can be evanescent near it. Returned modal powers are $0.83^2\simeq69\%$ and $0.76^2\simeq58\%$. Both the $10^\circ$ phase shortfall and amplitude inequality matter in panel modeling. Waveguide data alone do not give the free-space response.

### 5. Peak of the near-field spectrum

The $4\,\mathrm{mm}$ pitch is below $\lambda_0/2\simeq5.36\,\mathrm{mm}$, adequate for propagating components. Evanescent or subwavelength detail can require finer sampling. With aligned axes and a corrected field component,

$$
k_0\simeq586.4\,\mathrm{rad/m},\qquad \theta_r=\arcsin(293/586.4)\simeq+30.0^\circ,
\qquad \Delta k_x\sim 2\pi/(0.320\,\mathrm m)\simeq19.6\,\mathrm{rad/m}.
$$

The corresponding resolution scale near the peak is about $2.2^\circ$. Low noise can permit better estimation of one peak center. Zero-padding only refines the display grid. Check with a bistatic scan or a wider near-field scan. Coaxial reflection, waveguide modal reflection, and beam peak each depend on their own geometry and reference.
```
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
