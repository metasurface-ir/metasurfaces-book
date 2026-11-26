# Materials, fabrication and measurements

## 9.1 Materials and substrate response

Based on the instructor booklet, pages 244–248.

At microwave frequencies good conductors are often characterized by conductivity and skin depth. At optical frequencies carriers have inertia and bound charges can resonate, so use a dispersive Drude–Lorentz description. Dielectric loss, conductor loss and radiation contribute to the resonator linewidth. Compare substrates at the same frequency and field filling factor. A phase-change film, graphene sheet or electro-optic material can trade tunability against insertion loss and control complexity.

$$
\epsilon_r=\epsilon_\infty-\frac{\omega_p^2}{\omega^2-i\gamma\omega}+\sum_j\frac{f_j\omega_{0j}^2}{\omega_{0j}^2-\omega^2+i\Gamma_j\omega},\quad Q_d\approx\frac1{p_e\tan\delta}.
$$

## Worked exercise from the reading

A thermal film has conductivity rising from 10 to $10^5$ S/m with a logistic transition centered at $T_c$ and width scale $\Delta T$. Find the midpoint conductivity and the 10–90% temperature interval.

```{dropdown} Show the worked answer
:class: solution

At the midpoint $\sigma=50005$ S/m. Solving $p=(1+e^{-(T-T_c)/\Delta T})^{-1}$ gives $T_{10,90}=T_c\mp\Delta T\ln9$. Hysteresis and thermal settling would require additional measurements.
```

## 9.2 Fabrication and deposition

Based on the instructor booklet, pages 248–254.

Printed boards are practical for microwave patterns and multilayer routing, but registration, roughness and minimum gaps matter. Optical lithography uses a mask and transfer process. Electron-beam writing achieves small features at low throughput, while nanoimprint trades master fabrication for replication. Deposition and etching set material, thickness, sidewalls and roughness. Measure the fabricated geometry and propagate its uncertainty through the response.

$$
f_0=\frac1{2\pi\sqrt{LC}},\qquad C\propto g^{-1}\implies f_0/f_{00}\simeq\sqrt{g/g_0}.
$$

## Worked exercise from the reading

For $g_0=3.0\,\mu\mathrm m$, use the source's geometric model to find the allowable gap for a resonance shift within ±3%. Does a ±0.5 µm process meet it?

```{dropdown} Show the worked answer
:class: solution

Squaring the frequency limits gives $3(0.97)^2\le g\le3(1.03)^2$, or approximately 2.823–3.183 µm. A symmetric tolerance must be about ±0.177 µm or tighter. The ±0.5 µm process fails this screening model.
```

## 9.3 Packaging, bias isolation and integration

Based on the instructor booklet, pages 254–260.

Model a mounted PIN with its series resistance, lead inductance and off-state capacitance. A surface-mount package, bare die or flip-chip attachment has different RF parasitics and assembly constraints. Route bias through structures that limit RF leakage. A shorted quarter-wave branch transforms to a high input impedance at the design frequency. Verify bias isolation across the band with the actual stack, return currents and control transitions. Shift-register loading and latching must match the array update requirement.

$$
Z_{\rm on}\simeq R_s+i\omega L_s,\quad Z_{\rm off}\simeq i\omega L_s+\frac1{i\omega C_{\rm off}},\quad Z_{\rm in}=iZ_0\tan(\beta\ell).
$$

## Worked exercise from the reading

At 28 GHz, a packaged diode has $R_s=2\,\Omega$ and $L_s=0.30\,\mathrm{nH}$. Calculate its on-state impedance and explain what happens as a shorted bias branch moves off its quarter-wave frequency.

```{dropdown} Show the worked answer
:class: solution

$\omega L_s=2\pi(28\times10^9)(0.30\times10^{-9})=52.8\,\Omega$, so $Z_{\rm on}\simeq2+i52.8\,\Omega$. Near the quarter-wave condition, the magnitude of the shorted branch impedance declines away from the design frequency. Actual loss further limits the peak.
```

## 9.4 Free-space, waveguide and near-field measurements

Based on the instructor booklet, pages 260–265.

A free-space VNA setup uses transmitting and receiving horns, a sample plane and a reference. Establish the illumination footprint, polarization, alignment and phase plane before interpreting the data. Use background subtraction only for a stable additive contribution, and check reference normalization and gating separately. A waveguide fixture probes the supported guide mode and needs its own modal impedance. A near-field scan transforms a sufficiently sampled complex aperture field to its radiation spectrum, subject to scan truncation and probe correction.

$$
r_{\rm cal}=r_{\rm ref}\frac{S_{\rm sample}-S_{\rm bg}}{S_{\rm ref}-S_{\rm bg}}.
$$

## Worked exercise from the reading

The calibrated magnitudes of two states are 0.83 and 0.76 in the measured reflection mode. Their phase separation is 170°. Find the modal power fractions and phase error relative to 180°.

```{dropdown} Show the worked answer
:class: solution

The power fractions are $0.83^2\simeq0.689$ and $0.76^2\simeq0.578$. Separation is 10° short. Missing measured-mode power can include absorption, diffraction, polarization conversion or spillover.
```

## 9.5 Retrieving effective parameters

Based on the instructor booklet, pages 265–270.

Choose the model before inversion. A symmetric homogeneous slab supports impedance and index retrieval, a ground-backed one-port supports an input surface impedance, and a symmetric electric sheet supports shunt admittance. Shift reference planes first. For slab retrieval use phase continuity and physical checks to choose the logarithm branch, then reconstruct both measured coefficients. A very small transmission, uncertain sample thickness or calibration drift can magnify uncertainty.

$$
z^2=\frac{(1+r)^2-t^2}{(1-r)^2-t^2},\quad n_m=\frac{-\arg T+2\pi m+i\ln|T|}{k_0d},\quad Z_s=\eta\frac{1+r}{1-r},\quad Y_s=\frac2\eta(1/t-1).
$$

## Worked exercise from the reading

An internal slab factor has magnitude 0.90 and phase $+120^\circ$ at $d=\lambda_0/3$. Calculate the principal index and neighboring branch spacing.

```{dropdown} Show the worked answer
:class: solution

$k_0d=2\pi/3$, so $n_0=-1+i\ln(0.90)/(2\pi/3)\simeq-1-i0.0503$. The real spacing is 3. Attenuation fixes the imaginary part for the assumed propagation model, while one frequency alone cannot distinguish the real branches.
```
