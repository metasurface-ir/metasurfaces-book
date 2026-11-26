# 9.4 Free-space, waveguide and near-field measurements

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

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
