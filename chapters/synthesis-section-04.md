---
title: "5.4 Phase calibration and physical cell placement"
---

# 5.4 Phase calibration and physical cell placement

All right, friends: we now know what the wave wants (Section 5.2), and we translated that request into impedance and surface response (Section 5.3). Time to roll up our sleeves! How do we design a metal patch or dielectric element on a printed circuit board (PCB) that produces the required phase and impedance?

This is the beating heart of metasurface engineering: connecting wave mathematics to the practical world of full-wave simulators such as CST and HFSS.

### 5.4.1 Local periodicity: the assumption that rescues us

The first practical challenge is heterogeneity: the first cell differs from the second and third. Simulating the entire large structure at once can exceed the available memory. This is where a clever local periodicity approximation (LPA) helps.

**Main idea.** Assume dimensions vary gently between neighboring cells, $|\Delta L|\ll\lambda$. To simulate one cell, treat it as embedded in an infinite array of identical copies.

**Boundary setup in CST or HFSS:**

- Lateral walls in $x$ and $y$: Unit Cell or Periodic boundaries, with the appropriate Floquet excitation setup.
- Excitation along $z$: a plane-wave Floquet port.

This turns a many-centimeter simulation into a fast calculation of a millimeter-scale element.

### 5.4.2 The phase calibration curve: a designer’s map

How do physical dimensions connect to the electromagnetic response? Consider a reflective cell with a square metal patch of side $L$ and period $p$, on a dielectric substrate of thickness $h$ and permittivity $\epsilon_r$. Sweep a geometric parameter, usually $L$, from a minimum to a maximum and record reflection or transmission phase at the operating frequency.

$$
S_{11}=|S_{11}|e^{i\Phi_{\rm ref}(L)}.
$$

$$
\Phi_{\rm ref}(L)=\arg S_{11}.
$$

The source gives two essential requirements for a suitable cell:

1. **Full $360^\circ$ ($2\pi$) phase coverage:** cover $-180^\circ$ to $+180^\circ$, avoiding a blind phase interval.
2. **A gentle slope near resonance:** an extremely steep phase response makes small fabrication errors—even a few micrometers—strongly perturb the phase.

### 5.4.3 Strategies for a full phase range

The source describes a simple single-resonant patch on a thin substrate as often providing only about $280^\circ$–$300^\circ$. It proposes the following routes to full coverage.

### 1. Increase substrate thickness

Increasing $h$ moves the patch away from the ground plane and can widen the phase range, at the expense of a thicker structure.

### 2. Couple multiple resonances

Use multi-resonant elements such as concentric dual rings or a Jerusalem cross. The source describes two nearby resonances as smoothing the phase slope and extending coverage beyond $360^\circ$.

### 3. Stack multiple layers

For transmissive surfaces in particular, three or four metal layers with spacings around $\lambda/4$ can act as a band-pass filter. The source presents this as a route to full phase coverage and high transmission, $|S_{21}|\approx1$.

### 5.4.4 Spatial sampling and cell placement

After calibration, proceed step by step. **1. Sample the surface:** divide it into points $(x_m,y_n)$ using a period around $p\approx\lambda/3$ to $\lambda/5$. **2. Calculate the ideal phase** at each point using Section 5.2:

$$
\Phi_{\rm req}(x_m,y_n)=\phi_{\rm out}(x_m,y_n)-\phi_{\rm inc}(x_m,y_n).
$$

**3. Dimensional mapping:** use the lookup table to find $L_{mn}$ for the required phase and place the corresponding element.

$$
\Phi_{\rm req}(x_m,y_n)\xrightarrow{\text{Lookup table}}L(x_m,y_n).
$$

**4. Full-wave verification:** build the entire array, apply the incident wave and inspect the far-field radiation pattern to assess beam formation. For a focus, the focal field must also be inspected.

### 5.4.5 Practical nonidealities

Actual performance differs somewhat from the theoretical prediction. The source identifies three main causes.

**1. Mutual coupling.** The periodic model assumes identical neighbors. In the real array, adjacent cell dimensions differ; capacitive and inductive near-field interactions shift the phase.

**2. Spatial quantization.** A continuous phase profile becomes a staircase on a grid of pitch $p$. The source recommends a smaller pitch, for example $p\le\lambda/5$, to reduce discretization losses and improve efficiency.

**3. Oblique-incidence sensitivity.** Cell phase changes with incidence angle. The source recommends local-angle calibration for demanding lens designs with small focal ratio $F/D$.

:::{admonition} Worked exercise
:class: tip
A reflective metasurface consists of square metal patches. Sweeping patch side length in a unit-cell simulation gives the following calibration at the operating frequency. Initially neglect mutual coupling.

| $L$ (mm) | $\Phi_{\rm ref}$ |
|---|---|
| 1.0 | $0^\circ$ |
| 1.4 | $45^\circ$ |
| 1.8 | $90^\circ$ |
| 2.2 | $135^\circ$ |
| 2.6 | $180^\circ$ |
| 3.0 | $225^\circ$ |
| 3.4 | $270^\circ$ |
| 3.8 | $315^\circ$ |

Eight successive positions along $x$ require $\Phi_{\rm req}=[20,70,130,185,240,290,340,15]^\circ$.

1. Choose the nearest available phase at each position.
2. Find the corresponding patch length.
3. Calculate each phase error.
4. Find the mean absolute phase error.
5. Explain why the final array may differ from the calibration prediction.
6. State the final simulation and the quantities to inspect.

```{dropdown} Show the worked answer

### 1. Select the nearest calibration phase

For each requested phase choose the nearest phase available in the table.

### Position 1

Requested phase:

$$
\Phi_{\rm req,1}=20^\circ.
$$

Distance from $0^\circ$:

$$
|20-0|=20^\circ.
$$

Distance from $45^\circ$:

$$
|20-45|=25^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,1}=0^\circ.
$$

$$
L_1=1.0\,\mathrm{mm}.
$$

### Position 2

Requested phase:

$$
\Phi_{\rm req,2}=70^\circ.
$$

Distance from $45^\circ$:

$$
|70-45|=25^\circ.
$$

Distance from $90^\circ$:

$$
|70-90|=20^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,2}=90^\circ.
$$

$$
L_2=1.8\,\mathrm{mm}.
$$

### Position 3

Requested phase:

$$
\Phi_{\rm req,3}=130^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,3}=135^\circ.
$$

$$
L_3=2.2\,\mathrm{mm}.
$$

### Position 4

Requested phase:

$$
\Phi_{\rm req,4}=185^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,4}=180^\circ.
$$

$$
L_4=2.6\,\mathrm{mm}.
$$

### Position 5

Requested phase:

$$
\Phi_{\rm req,5}=240^\circ.
$$

Distance from $225^\circ$:

$$
|240-225|=15^\circ.
$$

Distance from $270^\circ$:

$$
|240-270|=30^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,5}=225^\circ.
$$

$$
L_5=3.0\,\mathrm{mm}.
$$

### Position 6

Requested phase:

$$
\Phi_{\rm req,6}=290^\circ.
$$

Distance from $270^\circ$:

$$
|290-270|=20^\circ.
$$

Distance from $315^\circ$:

$$
|290-315|=25^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,6}=270^\circ.
$$

$$
L_6=3.4\,\mathrm{mm}.
$$

### Position 7

Requested phase:

$$
\Phi_{\rm req,7}=340^\circ.
$$

Distance from $315^\circ$:

$$
|340-315|=25^\circ.
$$

Remember phase periodicity:

$$
340^\circ\equiv-20^\circ\pmod{360^\circ}.
$$

The distance to $0^\circ$ is only $20^\circ$, so choose zero.

$$
\Phi_{\rm sel,7}=0^\circ.
$$

$$
L_7=1.0\,\mathrm{mm}.
$$

### Position 8

Requested phase:

$$
\Phi_{\rm req,8}=15^\circ.
$$

Thus the nearest phase and its patch length are

$$
\Phi_{\rm sel,8}=0^\circ.
$$

$$
L_8=1.0\,\mathrm{mm}.
$$

### 2. Final phase-to-length mapping

| Position | Required phase | Selected phase | Length (mm) |
|---|---|---|---|
| 1 | $20^\circ$ | $0^\circ$ | 1.0 |
| 2 | $70^\circ$ | $90^\circ$ | 1.8 |
| 3 | $130^\circ$ | $135^\circ$ | 2.2 |
| 4 | $185^\circ$ | $180^\circ$ | 2.6 |
| 5 | $240^\circ$ | $225^\circ$ | 3.0 |
| 6 | $290^\circ$ | $270^\circ$ | 3.4 |
| 7 | $340^\circ$ | $0^\circ$ | 1.0 |
| 8 | $15^\circ$ | $0^\circ$ | 1.0 |

The fabricated patch-length sequence is therefore

$$
\mathbf L=[1.0,1.8,2.2,2.6,3.0,3.4,1.0,1.0]\,\mathrm{mm}.
$$

### 3. Calculate phase errors

Define phase error by

$$
e_\Phi=\Phi_{\rm sel}-\Phi_{\rm req}.
$$

Because phase repeats every $360^\circ$, express the error in approximately $[-180^\circ,+180^\circ]$.

| Position | Required phase | Selected phase | Error |
|---|---|---|---|
| 1 | $20^\circ$ | $0^\circ$ | $-20^\circ$ |
| 2 | $70^\circ$ | $90^\circ$ | $+20^\circ$ |
| 3 | $130^\circ$ | $135^\circ$ | $+5^\circ$ |
| 4 | $185^\circ$ | $180^\circ$ | $-5^\circ$ |
| 5 | $240^\circ$ | $225^\circ$ | $-15^\circ$ |
| 6 | $290^\circ$ | $270^\circ$ | $-20^\circ$ |
| 7 | $340^\circ$ | $0^\circ$ | $+20^\circ$ |
| 8 | $15^\circ$ | $0^\circ$ | $-15^\circ$ |

For position 7, treat the selected $0^\circ$ as $360^\circ$:

$$
360^\circ-340^\circ=20^\circ.
$$

Therefore its error is

$$
e_{\Phi,7}=+20^\circ.
$$

### 4. Mean absolute phase error

First sum the absolute errors:

$$
\sum|e_\Phi|=20+20+5+5+15+20+20+15.
$$

$$
\sum|e_\Phi|=120^\circ.
$$

There are eight positions, so

$$
\overline{|e_\Phi|}=\frac{120}{8}.
$$

The result is

$$
\overline{|e_\Phi|}=15^\circ.
$$

This error comes from phase quantization and the finite number of available calibration states.

### 5. Why does the real array differ?

A calibration table usually comes from one periodically repeated cell. Several effects change the response in the real array.

**a. Mutual coupling:** identical neighbors were assumed in the cell simulation, but adjacent patches in the array have different lengths. Their near fields interact and shift the actual phase away from the table.

**b. Phase quantization:** the desired profile is continuous, whereas the table supplies only discrete values such as $0^\circ$, $45^\circ$, $90^\circ$, and so on. Each target must be approximated by a nearby available state.

**c. Incidence angle:** oblique illumination changes cell response. A normal-incidence table may then be insufficient.

**d. Fabrication errors:** small changes in patch length or width, substrate thickness or dielectric properties alter both reflection amplitude and phase.

### 6. Final simulation and quantities to inspect

After mapping phase to dimensions, construct the complete array in a full-wave simulator such as CST or HFSS. Inspect:

- the far-field radiation pattern;
- the main-lobe angle;
- sidelobes and grating lobes;
- reflection coefficient and overall efficiency;
- agreement between the actual and requested phase profiles.

Thus the full array must be simulated and its far field evaluated. The main question is whether the reflected beam forms at the requested angle.

### Answer recap

$$
\mathbf L=[1.0,1.8,2.2,2.6,3.0,3.4,1.0,1.0]\,\mathrm{mm}.
$$

$$
\mathbf e_\Phi=[-20,+20,+5,-5,-15,-20,+20,-15]^\circ.
$$

$$
\overline{|e_\Phi|}=15^\circ.
$$

Unlike the earlier problems, this exercise directly addresses three practical ideas: phase calibration, phase-to-geometry mapping and quantization error. It then connects them to mutual coupling and the need for full-wave verification.

```
:::


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
Small neighboring dimension changes are a useful LPA heuristic, not a proof of weak coupling. Resonance, long-range interactions and steep wavefront changes may still require a supercell or finite-array calculation. Floquet ports excite/collect along the propagation direction; the lateral boundaries supply periodicity.

The $280^\circ$–$300^\circ$ range, multilayer spacings and resonance strategies are examples, not universal guarantees. Phase coverage must be evaluated together with amplitude, loss, fabrication limits and numerical convergence. Decreasing pitch does not monotonically guarantee efficiency, since coupling and realizability also change.

A low $F/D$ means large output angles for a normally illuminated lens; it does not automatically mean the incident wave is oblique. Angle-dependent calibration must follow the actual incident illumination and relevant outgoing/coupled fields. A focal point is checked in the focal region, not by a far-field beam plot alone. In the LUT exercise, the numbers are signed calibration arguments and must be compared on a circle.
:::


```{figure} ../assets/chapter-03/source-array-cell.svg
:alt: Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.

Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.
```
