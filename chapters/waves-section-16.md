---
title: "2.16 Equivalent-circuit modeling of metasurfaces"
short_title: "2.16 Equivalent-circuit modeling of metasurfaces"
---

(ch02-source-16)=
# 2.16 Equivalent-circuit modeling of metasurfaces

Full-wave numerical tools such as CST or HFSS provide detailed electromagnetic analysis, but they can be time-consuming and may not directly explain a structure's physical behavior. When the unit-cell size is much smaller than the operating wavelength, $a\ll\lambda$, quasistatic approximations can support **lumped equivalent-circuit models** of meta-atoms.

We map physical features to resistance ($R$), inductance ($L$), and capacitance ($C$):

- **Inductance ($L$):** metallic current paths have inductive behavior. A longer or narrower path generally increases the equivalent inductance.
- **Capacitance ($C$):** gaps between adjacent metal regions and dielectric substrates contribute capacitance.
- **Resistance ($R$):** represents metal ohmic losses and substrate dielectric losses.

### Resonance frequency

Many meta-atoms, including split-ring resonators and crossed patches, resonate near a characteristic frequency. A series or parallel RLC circuit approximates this response, with resonance frequency:

$$
f_r=\frac1{2\pi\sqrt{LC}}.
$$

This useful relation suggests how to lower the resonance frequency: lengthen the current path to increase $L$, or reduce gaps to increase $C$.

### Transmission-line model

To analyze propagation through a metasurface, represent free space or the surrounding dielectric as a transmission line of characteristic impedance $Z_0$. In free space, $Z_0=120\pi\approx377\,\Omega$. The sheet is then represented by a shunt impedance, $Z_{\mathrm{ms}}$, or shunt admittance, $Y_{\mathrm{ms}}$.

Once the equivalent impedance is known, transmission-line theory gives reflection and transmission (the S-parameters). For example, the reflection coefficient, $\Gamma$ or $S_{11}$, for a structure illuminated from free space is:

$$
S_{11}=\frac{Z_{\mathrm{in}}-Z_0}{Z_{\mathrm{in}}+Z_0}.
$$

Here $Z_{\mathrm{in}}$ is the input impedance of the combined metasurface and the structure behind it.

Circuit modeling is a useful tool for initial predictions, rapid optimization, and analytical design before detailed numerical simulation.

::::{admonition} Booklet example: RLC resonance and geometry changes
:class: book-exercise

A split-ring meta-atom is represented by a series RLC circuit with $L=4\,\mathrm{nH}$, $C=1\,\mathrm{pF}$, and $R=50\,\Omega$. The surrounding free-space impedance is $Z_0=377\,\Omega$. Using the equivalent-circuit model, calculate:

1. The initial resonance frequency.
2. The series-circuit impedance at resonance.
3. The reflection coefficient at resonance.
4. The reflected power percentage at this frequency.
5. The new resonance frequency if geometry changes increase the inductance to $L'=9\,\mathrm{nH}$ while keeping capacitance fixed, and interpret the change.

:::{dropdown} Show / hide the solution
**1. Initial resonance frequency.** For the RLC circuit:

$$
f_r=\frac1{2\pi\sqrt{LC}}.
$$

First convert to SI units: $L=4\,\mathrm{nH}=4\times10^{-9}\,\mathrm H$ and $C=1\,\mathrm{pF}=1\times10^{-12}\,\mathrm F$. Therefore:

$$
f_r=\frac1{2\pi\sqrt{(4\times10^{-9})(1\times10^{-12})}}.
$$

The product is $LC=4\times10^{-21}$, giving:

$$
\sqrt{LC}=2\times10^{-10.5}\simeq6.325\times10^{-11}.
$$

Consequently:

$$
f_r=\frac1{2\pi(6.325\times10^{-11})},\qquad\boxed{f_r\simeq2.52\,\mathrm{GHz}}.
$$

**2. Circuit impedance at resonance.** The series RLC impedance is:

$$
Z_{\mathrm{RLC}}=R+j\left(\omega L-\frac1{\omega C}\right).
$$

At resonance, the imaginary part vanishes because $\omega_rL=1/(\omega_rC)$. Thus $Z_{\mathrm{RLC}}=R$, giving:

$$
\boxed{Z_{\mathrm{RLC}}=50\,\Omega}.
$$

The circuit is purely resistive: the inductive and capacitive reactances cancel.

**3. Reflection coefficient.** Assuming that the structure's input impedance equals the RLC impedance:

$$
\Gamma=S_{11}=\frac{Z_{\mathrm{in}}-Z_0}{Z_{\mathrm{in}}+Z_0}.
$$

At resonance $Z_{\mathrm{in}}=50\,\Omega$, so:

$$
S_{11}=\frac{50-377}{50+377}=\frac{-327}{427},
\qquad\boxed{S_{11}\simeq-0.766}.
$$

The negative sign indicates a $180^\circ$ reflected-wave phase reversal. The magnitude is $|S_{11}|\simeq0.766$.

**4. Reflected power percentage.** The reflected power fraction is:

$$
R=|S_{11}|^2.
$$

Therefore:

$$
R=(0.766)^2\simeq0.587,\qquad\boxed{R\simeq58.7\%}.
$$

Approximately 58.7 percent of the incident power is reflected at resonance.

**5. New resonance frequency.** With $L'=9\,\mathrm{nH}=9\times10^{-9}\,\mathrm H$ and unchanged $C=1\times10^{-12}\,\mathrm F$:

$$
f_r'=\frac1{2\pi\sqrt{L'C}}.
$$

Therefore:

$$
f_r'=\frac1{2\pi\sqrt{(9\times10^{-9})(1\times10^{-12})}}.
$$

Now $L'C=9\times10^{-21}$ and $\sqrt{L'C}\simeq9.487\times10^{-11}$. Therefore:

$$
f_r'=\frac1{2\pi(9.487\times10^{-11})},\qquad\boxed{f_r'\simeq1.68\,\mathrm{GHz}}.
$$

**6. Interpretation.** The resonance decreases from $f_r\simeq2.52\,\mathrm{GHz}$ to $f_r'\simeq1.68\,\mathrm{GHz}$. Thus **increasing inductance lowers the resonance frequency**, consistent with:

$$
f_r\propto\frac1{\sqrt L}.
$$

Physically, lengthening or narrowing metallic current paths can increase the meta-atom's equivalent inductance, shifting its response to lower frequencies.

**Final answer:**

$$
\boxed{f_r\simeq2.52\,\mathrm{GHz}},\quad
\boxed{Z_{\mathrm{RLC}}=50\,\Omega},\quad
\boxed{S_{11}\simeq-0.766},\quad
\boxed{R\simeq58.7\%}.
$$

Increasing the inductance from 4 to 9 nanohenries gives:

$$
\boxed{f_r'\simeq1.68\,\mathrm{GHz}}.
$$

Increasing $L$ therefore shifts the resonance toward lower frequencies.
:::
::::

:::{note} A resonator impedance is not automatically a sheet input impedance
The source RLC example explicitly assumes that the whole one-port input impedance equals the series-resonator impedance. Under that assumption its reflection calculation is valid. For an unbacked shunt sheet, however, the load seen at the input is the parallel combination of the sheet and the transmitted-medium admittance. The computational sheet derivation in Section 2.14 gives that two-port result. A resonance estimate also needs a valid circuit topology and material model before it predicts a physical device.
:::

(ch02-section-12)=
### Computational connection: Where did the missing light go?


Return to the air-surrounded sheet with $g=2$. One incident beam gives $r=-1/2$, $t=1/2$, and $A=1/2$. Now illuminate it coherently from both sides, with total incoming power normalized to one:

$$
\mathbf a=\frac{1}{\sqrt2}\begin{bmatrix}1\\e^{-i\phi}\end{bmatrix},\qquad
S=\frac12\begin{bmatrix}-1&1\\1&-1\end{bmatrix}.
$$

Adding the outgoing field contributions before calculating their powers gives

$$
A_{\mathrm{two\ sided}}=1-\|S\mathbf a\|^2=\frac{1+\cos\phi}{2}.
$$

At $\phi=0$, every outgoing amplitude vanishes: the ideal model absorbs all the incoming power. At $\phi=\pi$, the electric field at the sheet is a node and absorption vanishes. The material parameter has not changed. The incident coherent state has changed, so its overlap with the dissipative scattering channel has changed.

```{figure} ../assets/chapter-02/sheet-response.png
:alt: Original analytical sheet results comparing the one-sided absorption bound with phase-controlled two-sided coherent absorption.

The one-sided and two-sided experiments have different incident states and the same explicit power normalization. Perfect two-sided absorption here requires exact sheet parameters and coherent excitation at the stated reference planes; it is not a fabricated-device result.
```

This is an entry point to coherent perfect absorption, a research topic developed by [Chong, Ge, Cao, and Stone](https://arxiv.org/abs/1003.4968). Our shunt derivation illustrates a restricted analytical example and does not reproduce their slab calculation. An experiment would additionally need controlled phase, matched spatial modes, calibrated power, material dispersion/loss, and uncertainty.

(ch02-section-13)=
### Computational connection: Carry this into the next chapters


Before accepting any metasurface response, ask:

1. Which field basis, time convention, and reference planes define its complex coefficients?
2. Which admittance or channel normalization converts those coefficients to power?
3. Which waves propagate, which decay, and which are at cutoff?
4. Which boundary currents or geometry support the proposed transformation?
5. Does the model conserve or dissipate power appropriately for every relevant illumination?
6. Which independent condition would test the claimed retrieval or design?

Chapter [3](03-unit-cell-design.md) adds patterned geometry and a full-wave library; Chapter [4](04-periodic-floquet.md) adds diffraction channels; Chapter [5](05-metasurface-synthesis.md) assembles transformations. Chapter [10](10-ai-metasurfaces.md) uses data that must preserve exactly these conventions. Continue with the [nine worked examples](02-waves-guide.md), [computational lab](../labs/02-waves-lab.md), and [self-check and mini-project](02-waves-review.md).

For an independent foundational route, the [Cornell ECE 3030 handouts](https://ocw.ece.cornell.edu/courses/ece-3030-electromagnetic-fields-and-waves-2/ece-3030-lectures-notes-and-handouts-2/) cover plane waves, polarization, interfaces, and multilayers. [MIT's optics lecture notes](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/lecture-notes/) provide complementary wave and polarization material. The supplementary computational derivations, figures, and experiments are original course material; the primary reading is attributed to the instructor-supplied booklet below.

(ch02-section-14)=
### Computational connection: Linked computational investigations


Continue with [ms-09: spectral bandwidth](../labs/09-dispersion-lab.md), [ms-10: independent cells versus supercells](../labs/10-coupling-lab.md), and [ms-11: bounded optimization with independent checks](../labs/11-inverse-design-lab.md). These executed studies use the same explicit ridge geometry and connect spectral response, model approximation and design validation. The inverse-design study is a direct full-wave baseline for later AI comparisons.

Primary reading: instructor-supplied *Electromagnetic Metasurfaces Booklet*, Chapter 2, printed pages 15–69. Supervision: Dr. Ali Abdolali; compilation/final editing: Mohammad Salman Shahroudi. Persian prose is transcribed with typographic normalization; English is its paired translation. All nine source diagrams have original vector counterparts. The boundary table is shortened and corrected with instructor authorization. Source rights remain with their respective holders; the original PDF and raster illustrations are not redistributed.
