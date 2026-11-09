---
title: "2.15 Scattering matrices and S-parameters in metasurfaces"
short_title: "2.15 Scattering matrices and S-parameters in metasurfaces"
---

(ch02-source-15)=
# 2.15 Scattering matrices and S-parameters in metasurfaces

At microwave and optical frequencies, directly measuring voltages and currents can be difficult or impossible. We therefore use **scattering parameters**, or **S-parameters**, to analyze high-frequency networks and periodic structures such as metasurfaces. They relate the incident and outgoing traveling waves at the network ports.

A metasurface simulation commonly uses a single **unit cell** with periodic boundary conditions, representing the structure as a **two-port network**:

- **Port 1:** the side receiving the incident wave.
- **Port 2:** the side through which the transmitted wave leaves.

The scattering matrix is defined by:

$$
\begin{bmatrix}V_1^-\\V_2^-\end{bmatrix}
=\begin{bmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{bmatrix}
\begin{bmatrix}V_1^+\\V_2^+\end{bmatrix}.
$$

Here $V_n^+$ is the wave amplitude entering port $n$, and $V_n^-$ is the outgoing (reflected or transmitted) amplitude. Two parameters are particularly useful:

### 1. Reflection coefficient ($S_{11}$)

This is the reflected-to-incident wave ratio at port 1 when port 2 is matched, $V_2^+=0$:

$$
S_{11}=\frac{V_1^-}{V_1^+}=|S_{11}|e^{j\angle S_{11}}.
$$

- **Magnitude ($|S_{11}|$):** describes the reflected response, corresponding to the transmission-line coefficient $\Gamma$. Reflectarrays often aim for $|S_{11}|$ close to 1, or 0 dB.
- **Phase ($\angle S_{11}$):** describes the reflected-wave phase. Changing the meta-atom dimensions changes this phase, allowing the phase gradients used in generalized Snell-law designs.

### 2. Transmission coefficient ($S_{21}$)

This is the wave leaving port 2 relative to the wave incident at port 1:

$$
S_{21}=\frac{V_2^-}{V_1^+}=|S_{21}|e^{j\angle S_{21}}.
$$

- **Magnitude ($|S_{21}|$):** describes the transmitted response, corresponding to $\tau$. Transmitarrays generally aim to maximize transmission.
- **Phase ($\angle S_{21}$):** controls the transmitted-wave phase and thus the wavefront on the other side of the metasurface.

### Connection to absorption

Energy conservation gives the absorbed power fraction, $A$, from the S-parameter magnitudes:

$$
A=1-|S_{11}|^2-|S_{21}|^2.
$$

An absorber aims to minimize both reflection, $S_{11}$, and transmission, $S_{21}$, bringing absorption toward 100 percent.

S-parameters also support the retrieval of effective properties, such as $n_{\mathrm{eff}}$ and $Z_{\mathrm{eff}}$. Later chapters examine these procedures and their simulation requirements.

::::{admonition} Booklet example: from scattering parameters to power
:class: book-exercise

A metasurface unit cell is simulated as a two-port network. At the operating frequency, $|S_{11}|=0.2$ and $|S_{21}|=0.8$. Only port 1 is illuminated, and port 2 is matched, $V_2^+=0$. Calculate:

1. The percentage of reflected power.
2. The percentage of transmitted power.
3. The percentage of absorbed power.
4. Whether the metasurface is predominantly transmitting or absorbing, explaining your answer.

:::{dropdown} Show / hide the solution
**1. Reflected power.** The reflection-amplitude magnitude is $|S_{11}|$. The reflected power fraction is:

$$
R=|S_{11}|^2.
$$

Substituting the given value:

$$
R=(0.2)^2=0.04.
$$

As a percentage:

$$
\boxed{R=4\%}.
$$

Thus, 4 percent of the incident power is reflected.

**2. Transmitted power.** The transmitted power fraction is:

$$
T=|S_{21}|^2.
$$

Therefore:

$$
T=(0.8)^2=0.64.
$$

As a percentage:

$$
\boxed{T=64\%}.
$$

Thus, 64 percent of the incident power passes through the metasurface.

**3. Absorption.** When reflection and transmission are the only outgoing channels:

$$
A=1-|S_{11}|^2-|S_{21}|^2.
$$

Substituting:

$$
A=1-(0.2)^2-(0.8)^2=1-0.04-0.64=0.32.
$$

The absorbed percentage is:

$$
\boxed{A=32\%}.
$$

**4. Energy conservation.** Reflected, transmitted, and absorbed power fractions must sum to one:

$$
R+T+A=1.
$$

Substituting the results:

$$
0.04+0.64+0.32=1.
$$

Therefore, $R+T+A=1$ and energy is conserved.

**5. Predominant response.** Transmission accounts for 64 percent, reflection for 4 percent, and absorption for 32 percent. Most power passes through the structure, so the response is predominantly **transmitting**, with some absorption.

For an ideal transmitting metasurface, $|S_{21}|$ should approach one while $|S_{11}|$ and absorption decrease. For an ideal absorber, both $|S_{11}|$ and $|S_{21}|$ should approach zero.

**Final answer:**

$$
\boxed{R=4\%},\qquad \boxed{T=64\%},\qquad\boxed{A=32\%}.
$$

The structure is predominantly **transmitting**.
:::
::::

:::{note} Magnitude is an amplitude, not a power fraction
For properly power-normalized propagating port waves, reflected and transmitted fractions are the squared magnitudes of the relevant S-parameters. The magnitudes themselves are amplitude ratios. Raw electric transmission coefficients require the corresponding admittance ratio. The two-term absorption formula applies only when those are all outgoing channels: include other polarizations and diffraction orders before identifying missing power as absorption. The two-port example assumes power-wave normalization, a matched receiving port, and no other outgoing modes.
:::

(ch02-section-09)=
### Computational connection: Normalize a scattering matrix

Time convention in this computational connection: $e^{-i\omega t}$.


For propagating ports with real positive admittance, scale each incoming/outgoing tangential field by $\sqrt{Y_j/(2\eta_0)}$. The resulting amplitudes have squared magnitude equal to normal power flux. Write

$$
\mathbf b=S\mathbf a,\qquad P_{\mathrm{in}}=\mathbf a^\dagger\mathbf a,\qquad
P_{\mathrm{out}}=\mathbf b^\dagger\mathbf b.
$$

A lossless complete scattering description requires $S^\dagger S=I$. A passive one requires $\mathbf a^\dagger(I-S^\dagger S)\mathbf a\geq0$ for every input. Reciprocity and mirror symmetry are separate properties; a substrate can break the latter without breaking the former.

For our bare interface between two propagating channels,

$$
S=\begin{bmatrix}r&\tau\\\tau&-r\end{bmatrix},\qquad
\tau=\frac{2\sqrt{Y_iY_t}}{Y_i+Y_t}.
$$

The opposite reflection signs follow our field bases and port arrangement. $S$ is symmetric and unitary. Raw electric-field transmission coefficients from opposite sides need not be equal; their power-normalized counterparts are equal here. An evanescent solution with zero normal flux cannot be normalized as an independent unit-power propagating port by dividing by $\sqrt{\operatorname{Re}Y}$.

