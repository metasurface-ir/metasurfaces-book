---
title: "5.5 Amplitude synthesis and power management"
---

# 5.5 Amplitude synthesis and power management

All right, friends! We have learned to shape a wavefront by controlling the phase of reflection or transmission: steer a beam or concentrate it at a focus. But in electromagnetic engineering, phase is only half the story!

Suppose we want a metasurface antenna with extremely low sidelobes, using a Taylor or Chebyshev distribution, or a high-resolution electromagnetic hologram. Phase alone will not do: the reflected or transmitted amplitude must also be controlled locally at each point.

### 5.5.1 Energy conservation in a passive cell

Before reaching for formulas, let us see what physics allows. For the passive two-channel cell considered here, energy conservation gives

$$
|S_{11}|^2+|S_{21}|^2+A=1.
$$

Here $|S_{11}|^2$ is reflectance, $|S_{21}|^2$ is transmittance, and $A$ is absorptance or material loss. This simple equation offers three main ways to set a desired amplitude:

1. **Loss:** turn surplus power into heat with resistance, $A>0$.
2. **Lossless reflection/transmission partitioning:** change how power is divided without dissipating it.
3. **Polarization conversion:** send surplus power into an orthogonal polarization.

### 5.5.2 Physical methods of amplitude control

### 1. Resistive loading

The simplest way to reduce amplitude locally is to introduce controlled loss: resistive sheets, lumped resistors or finite-conductivity materials increase the real part of surface impedance, $Z_s=R_s+iX_s$, with $R_s>0$. The source describes the advantage as a simple, independent one-port design. The major disadvantage is heat generation and reduced overall antenna or metasurface efficiency.

### 2. Lossless reflection/transmission partitioning

For lossless dielectrics, $A\approx0$, so the balance reduces to

$$
|S_{11}|^2+|S_{21}|^2=1.
$$

For example, to obtain reflection amplitude $|S_{11}|=0.6$, arrange for the remaining power to be transmitted:

$$
|S_{21}|=\sqrt{1-0.6^2}=0.8.
$$

Power has not disappeared; it has been directed behind the sheet.

### 3. Polarization conversion and interference

One clever trick in anisotropic metasurfaces is local rotation. An $x$-polarized incident wave can partly convert into $y$ polarization. If the receiver detects only $x$, the co-polarized amplitude can be controlled by the element angle $\theta$, proportional to $\cos2\theta$ for the half-wave case. The remaining power enters the orthogonal, cross-polarized channel instead of being dissipated.

### 5.5.3 Can amplitude and phase be controlled independently?

The designer’s biggest headache is this: how do we change amplitude without disturbing phase, and vice versa? Changing patch dimensions normally changes both. The source proposes at least two geometric degrees of freedom to separate the tasks.

$$
L\longrightarrow\Phi,\qquad W\longrightarrow|S|.
$$

Consider a rectangular patch with a central slot:

- Total length $L$ adjusts resonance frequency and phase shift.
- Slot width or depth $W$ adjusts coupling, radiation or amplitude attenuation.

A two-dimensional parameter sweep in CST or HFSS produces a response matrix:

$$
S_{11}(L,W)=|S_{11}(L,W)|e^{i\Phi(L,W)}.
$$

The placement algorithm then selects a pair $(L_{mn},W_{mn})$ at each point to meet the target amplitude and phase. The source describes this as independent control; the achievable degree of independence must be checked for the actual cell.

:::{admonition} Worked exercise
:class: tip
At the operating frequency a transmissive cell has $|S_{11}|=0.6$ and is lossless, $A=0$. Three surface positions require transmission amplitudes $[0.8,0.6,0.3]$ and phases $[30,120,210]^\circ$. Two geometric variables are available: $L$ primarily controls phase and $W$ primarily controls amplitude.

1. Calculate transmission amplitude for the original cell from energy conservation.
2. Can it provide amplitude 0.8? Explain.
3. Find lossless reflection amplitude when the desired transmission amplitude is 0.3.
4. Why does changing only $L$ usually fail to control amplitude and phase independently?
5. Propose a practical method for choosing $(L,W)$.
6. How does resistive amplitude reduction affect efficiency?

```{dropdown} Show the worked answer

### 1. Transmission amplitude from energy conservation

For the lossless cell,

$$
|S_{11}|^2+|S_{21}|^2=1.
$$

Insert the given reflection amplitude:

$$
|S_{11}|=0.6.
$$

$$
(0.6)^2+|S_{21}|^2=1.
$$

$$
0.36+|S_{21}|^2=1.
$$

Therefore,

$$
|S_{21}|^2=0.64.
$$

And hence

$$
|S_{21}|=0.8.
$$

Thus reflection amplitude 0.6 gives transmission amplitude 0.8 in the ideal lossless case. Amplitudes are not added directly: powers, the squared magnitudes of the scattering parameters, enter energy conservation.

### 2. Can the cell provide transmission amplitude 0.8?

Yes. The result above gives

$$
|S_{21}|=0.8.
$$

So a cell with

$$
|S_{11}|=0.6.
$$

can provide this amplitude in the ideal lossless case. Its transmitted power is

$$
T=|S_{21}|^2=(0.8)^2=0.64.
$$

The reflected power is

$$
R=|S_{11}|^2=(0.6)^2=0.36.
$$

Thus

$$
R+T=0.36+0.64=1.
$$

All incident power is divided between reflection and transmission; none becomes heat. Matching the target phase remains a separate requirement.

### 3. Reflection for transmission amplitude 0.3

For a lossless cell,

$$
|S_{11}|^2+|S_{21}|^2=1.
$$

Set

$$
|S_{21}|=0.3.
$$

Then

$$
|S_{11}|^2+(0.3)^2=1.
$$

$$
|S_{11}|^2+0.09=1.
$$

$$
|S_{11}|^2=0.91.
$$

Consequently,

$$
|S_{11}|=\sqrt{0.91}\simeq0.954.
$$

In this case,

$$
T=|S_{21}|^2=0.09.
$$

$$
R=|S_{11}|^2=0.91.
$$

About 9% is transmitted and 91% reflected.

### 4. Why is changing only length insufficient?

In a simple patch, changing $L$ shifts resonance. Two things happen together:

1. Reflection or transmission phase changes.
2. Reflection or transmission amplitude also changes.

In general,

$$
S_{21}(L)=|S_{21}(L)|e^{i\Phi(L)}.
$$

Both quantities depend on $L$:

$$
|S_{21}|=|S_{21}(L)|.
$$

$$
\Phi=\Phi(L).
$$

One variable does not normally provide enough freedom to select both independently. The phase may be right while amplitude misses its target. At least two geometric variables are proposed:

$$
(L,W).
$$

$L$ can primarily tune phase, while $W$ adjusts coupling or radiation and hence amplitude. Complete independence is usually idealized: $W$ may still perturb phase, and $L$ may still perturb amplitude. The aim is to minimize this cross influence.

### 5. Selecting the parameter pair

First sweep both $L$ and $W$ over the allowed ranges and record the response for every pair:

$$
S_{21}(L,W)=|S_{21}(L,W)|e^{i\Phi(L,W)}.
$$

At each surface point define an error function:

$$
\mathcal E(L,W)=w_A\left(|S_{21}(L,W)|-|S_{21,\rm target}|\right)^2+w_\Phi[\Delta\Phi(L,W)]^2.
$$

Here $w_A$ weights amplitude error, $w_\Phi$ weights phase error, and $\Delta\Phi$ is the phase difference accounting for $360^\circ$ periodicity. Choose the pair minimizing this error at each $(x_m,y_n)$:

$$
(L_{mn},W_{mn})=\operatorname*{arg\,min}_{L,W}\mathcal E(L,W).
$$

The practical workflow is:

1. Build a cell library over different $L,W$ values.
2. Extract $S_{21}$ or $S_{11}$ amplitude and phase for every state.
3. Compare each response with the target amplitude and phase.
4. Select the closest feasible pair at each surface point.
5. Simulate the full array and refine cells whose performance is degraded by mutual coupling.

### 6. Effect of surface resistance

Resistive loading converts some electromagnetic energy into heat. The balance becomes

$$
|S_{11}|^2+|S_{21}|^2+A=1.
$$

With

$$
A>0.
$$

For example, suppose

$$
|S_{11}|=0.5.
$$

And

$$
|S_{21}|=0.4.
$$

Then

$$
R=|S_{11}|^2=0.25.
$$

$$
T=|S_{21}|^2=0.16.
$$

Hence

$$
A=1-R-T.
$$

$$
A=1-0.25-0.16=0.59.
$$

Therefore,

$$
A=0.59.
$$

59% of the incident power is dissipated in the material or resistor. The advantage is simplicity and local amplitude reduction. The disadvantage is lower total efficiency: surplus power becomes heat instead of entering a useful channel.

### Recap

Amplitude synthesis must control both factors in

$$
S_{21}=|S_{21}|e^{i\Phi}.
$$

Or, for reflection,

$$
S_{11}=|S_{11}|e^{i\Phi}.
$$

Phase alone is insufficient for precise beam shaping or sidelobe reduction. The three routes are absorption, reflection/transmission partitioning, and transfer to orthogonal polarization. Resistance is simple but reduces efficiency. Partitioning and polarization conversion can reduce loss, but require multiport or anisotropic structures and more careful design. Finally, two geometric degrees of freedom and full-wave array validation are needed for the independent-control approach discussed here.

```
:::


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
The two-channel power equation assumes power-normalized port amplitudes, or equivalent field amplitudes in equal-impedance channels. With other diffraction orders or polarizations, sum their normalized powers too. In unequal media, a field transmission amplitude needs its wave-admittance factor before squaring gives a power fraction.

The $\cos2\theta$/$\sin2\theta$ amplitude split assumes an appropriate half-wave anisotropic element and polarization analyzer. Resistive loading need not provide independent phase/amplitude control. Two geometric variables are a useful minimum for a generic two-real-number target, but not a guarantee: local response-map rank, passivity and accessible geometry still restrict the achievable complex response. Scale amplitude and phase errors consistently before choosing weights.
:::
