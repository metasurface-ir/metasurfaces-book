---
title: "2.9 Poynting vector and power flux"
short_title: "2.9 Poynting vector and power flux"
---

(ch02-source-09)=
# 2.9 Poynting vector and power flux

Understanding how fields transport energy is a central part of wave analysis. The **Poynting vector** describes energy-transfer rate per unit area: it gives the energy-flow direction and power flux. It is especially important in metasurfaces, where reflection, transmission, absorption and energy loss determine performance.

In the time domain, instantaneous Poynting vector is the field cross product:

$$
\mathbf S(t)=\mathbf E(t)\times\mathbf H(t).
$$

The fields $\mathbf E(t)$ and $\mathbf H(t)$ are instantaneous electric and magnetic fields. Their cross product tells us where energy moves at each instant and how much power crosses a unit area. Poynting-vector units are watts per square meter, $\mathrm{W/m^2}$.

In many engineering problems we use harmonic phasor fields with $e^{j\omega t}$. The quantity of greatest practical interest is then **time-averaged power**. Its Poynting vector is:

$$
\mathbf P_{\mathrm{ave}}=\frac12\operatorname{Re}\{\mathbf E\times\mathbf H^*\}.
$$

The star denotes complex conjugation, and $\operatorname{Re}\{\cdot\}$ takes the real part.

Taking the real part matters because $\mathbf E\times\mathbf H^*$ is generally complex. Its real part corresponds to net transported, active power. Its imaginary part is associated with reactive power: oscillatory energy exchange between fields and the medium without net energy transport.

In a uniform plane wave in a lossless medium, the fields are perpendicular and their amplitude ratio is set by intrinsic impedance. Average power density is then:

$$
\mathbf P_{\mathrm{ave}}=\frac{|\mathbf E_0|^2}{2\eta}\hat{\mathbf a}_n.
$$

Here $|\mathbf E_0|$ is electric-field amplitude and $\hat{\mathbf a}_n$ is the propagation unit vector. Average power density scales with electric amplitude squared and inversely with intrinsic impedance.

Equivalently, using the magnetic field:

$$
\mathbf P_{\mathrm{ave}}=\frac{\eta|\mathbf H_0|^2}{2}\hat{\mathbf a}_n.
$$

These expressions are equivalent in lossless media and are widely used for incident, transmitted and reflected powers.

### Power balance in metasurfaces

The Poynting vector is our main tool for **power balance** in a metasurface. When a wave arrives, some incident power is reflected, some transmitted, and some may be absorbed through ohmic, dielectric or resonant losses. Energy conservation gives:

$$
P_{\mathrm{inc}}=P_{\mathrm{ref}}+P_{\mathrm{tr}}+P_{\mathrm{abs}}.
$$

Here $P_{\mathrm{inc}}$ is incident power, $P_{\mathrm{ref}}$ reflected power, $P_{\mathrm{tr}}$ transmitted power, and $P_{\mathrm{abs}}$ absorbed power. Accordingly, power reflection, transmission and absorption coefficients are:

$$
R=\frac{P_{\mathrm{ref}}}{P_{\mathrm{inc}}},\qquad
T=\frac{P_{\mathrm{tr}}}{P_{\mathrm{inc}}},\qquad
A=\frac{P_{\mathrm{abs}}}{P_{\mathrm{inc}}}.
$$

For a passive structure, energy conservation requires their sum to equal one:

$$
R+T+A=1.
$$

These relations make quantitative performance assessment possible. For example:

- A **perfect metamaterial absorber** aims for vanishing transmission and reflection, making $A$ as close to one as possible.
- A **phase-controlling reflectarray** usually aims for $R$ close to one and $A$ as small as possible.

The Poynting vector therefore bridges field descriptions and energy analysis. Electric and magnetic fields describe local wave behavior; their Poynting vector shows how those fields carry and distribute energy through space.

::::{admonition} Textbook example: a metasurface power account
:class: book-exercise

A uniform plane wave propagates in a lossless medium with electric phasor:

$$
\mathbf E(z)=20\hat{\mathbf x}e^{-j\beta z}\,\mathrm{V/m}.
$$

The medium has intrinsic impedance $\eta=200\,\Omega$. The wave reaches a passive metasurface with power coefficients $R=0.16$ and $T=0.64$. Taking $20\,\mathrm{V/m}$ as peak phasor amplitude, answer:

1. Find the magnetic-field vector.
2. Calculate the incident average Poynting vector.
3. Find the absorbed-power fraction.
4. For effective surface area $S=0.02\,\mathrm{m^2}$, calculate incident, reflected, transmitted and absorbed powers.
5. Check power balance.

:::{dropdown} Show / hide answer
**1. Magnetic field.** The wave travels along positive $z$, so $\hat{\mathbf k}=\hat{\mathbf z}$. Its electric and magnetic fields obey:

$$
\mathbf H=\frac1\eta\hat{\mathbf k}\times\mathbf E.
$$

Substituting:

$$
\mathbf H(z)=\frac1{200}\hat{\mathbf z}\times(20\hat{\mathbf x}e^{-j\beta z}).
$$

Since $\hat{\mathbf z}\times\hat{\mathbf x}=\hat{\mathbf y}$, we obtain:

$$
\mathbf H(z)=0.1\hat{\mathbf y}e^{-j\beta z}\,\mathrm{A/m}.
$$

Thus:

$$
\boxed{\mathbf H(z)=0.1\hat{\mathbf y}e^{-j\beta z}\,\mathrm{A/m}}.
$$

**2. Average Poynting vector.** For a plane wave in a lossless medium:

$$
\mathbf P_{\mathrm{ave}}=\frac{|E_0|^2}{2\eta}\hat{\mathbf k}.
$$

Therefore:

$$
\mathbf P_{\mathrm{ave}}=\frac{20^2}{2(200)}\hat{\mathbf z}
=\frac{400}{400}\hat{\mathbf z}.
$$

Consequently:

$$
\boxed{\mathbf P_{\mathrm{ave}}=1\hat{\mathbf z}\,\mathrm{W/m^2}}.
$$

Average power density is $1\,\mathrm{W/m^2}$, directed along positive $z$.

**3. Absorbed fraction.** Passive power balance gives:

$$
R+T+A=1.
$$

Therefore:

$$
A=1-R-T.
$$

Substituting:

$$
A=1-0.16-0.64=0.20.
$$

The absorbed fraction is therefore 20%:

$$
\boxed{A=20\%}.
$$

**4. Individual powers.** Incident power is power density times area:

$$
P_{\mathrm{inc}}=P_{\mathrm{ave}}S.
$$

Therefore:

$$
P_{\mathrm{inc}}=(1)(0.02),\qquad \boxed{P_{\mathrm{inc}}=0.02\,\mathrm W}.
$$

Reflected power:

$$
P_{\mathrm{ref}}=RP_{\mathrm{inc}}=0.16(0.02)=0.0032\,\mathrm W.
$$

Or:

$$
\boxed{P_{\mathrm{ref}}=3.2\,\mathrm{mW}}.
$$

Transmitted power:

$$
P_{\mathrm{tr}}=TP_{\mathrm{inc}}=0.64(0.02)=0.0128\,\mathrm W.
$$

Or:

$$
\boxed{P_{\mathrm{tr}}=12.8\,\mathrm{mW}}.
$$

Absorbed power:

$$
P_{\mathrm{abs}}=AP_{\mathrm{inc}}=0.20(0.02)=0.004\,\mathrm W.
$$

Or:

$$
\boxed{P_{\mathrm{abs}}=4\,\mathrm{mW}}.
$$

**5. Checking power balance.** The sum of reflected, transmitted and absorbed powers is:

$$
P_{\mathrm{ref}}+P_{\mathrm{tr}}+P_{\mathrm{abs}}
=0.0032+0.0128+0.004=0.020\,\mathrm W.
$$

The incident power is $P_{\mathrm{inc}}=0.020\,\mathrm W$, so:

$$
P_{\mathrm{ref}}+P_{\mathrm{tr}}+P_{\mathrm{abs}}=P_{\mathrm{inc}}.
$$

Power balance holds, and the passive structure is consistent with energy conservation.
:::
::::

(ch02-section-03)=
### Computational connection: A field is not a power meter

Time convention in this computational connection: $e^{-i\omega t}$.


For phasors defined as peak amplitudes, the time-averaged power-flux density is

$$
\langle\mathbf S\rangle=\frac12\operatorname{Re}\{\widetilde{\mathbf E}\times\widetilde{\mathbf H}^{\,*}\}.
$$

The factor $1/2$ belongs to the peak-amplitude convention. For a normally incident propagating wave in a real medium,

$$
\langle S_z\rangle=\frac{|E|^2}{2\eta}=\frac{n|E|^2}{2\eta_0}.
$$

An electric amplitude therefore does not have the same power weighting in two different media. A transmitted amplitude of 1.2 in air can carry less power than an incident amplitude of 1 in glass. At oblique incidence, the normal flux and chosen field component introduce additional factors; we will collect them in a wave admittance.

:::{tip} A prediction before the derivation
At normal incidence from $n_i=1.5$ to $n_t=1$, suppose $t=1.2$. Calculate $T=(n_t/n_i)|t|^2$ before deciding whether the interface amplifies the wave. The answer is 0.96. The remaining 0.04 can be reflected without any gain or absorption.
:::

Power is only one observable. The fields $t=1$ and $t=-1$ have equal transmitted power in the same normalization, but they interfere differently with a fixed reference. Always retain amplitude and phase together when the design concerns a complex wavefront.

