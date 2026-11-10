# Chapter 5: primary reading

## 5.1 From analysis to synthesis

Hello everyone! So far, we have mostly played the role of an analyst. Someone gave us a structure, unit cell or layer and said: “Work out what this does to an electromagnetic wave. How much does it reflect, and how much does it transmit?” We call this the forward problem, or analysis.

But real engineering reverses the story—and makes it more interesting! A client or problem statement does not normally say “I have this cell.” It says: “I have a normally incident plane wave, and I want this surface to deflect it through 45 degrees,” or “I want that plane wave focused ten centimeters away—a flat lens.”

What is our job now? We must work backward from that final wish and find the structure, dimensions and impedance distribution that could perform the trick. This reverse-engineering process is metasurface synthesis, or solving an inverse problem. To remember the difference, compare the two viewpoints:

| Viewpoint | Analysis / forward | Synthesis / inverse |
| --- | --- | --- |
| Starting point | Cell geometry and material are specified | Incident wave and desired output field |
| Goal | Scattered fields and S-parameters | Optimal cell shape, dimensions and layout |
| Mathematical difficulty | Well-defined, with a unique answer | Often nonunique or ill-posed |
| Tools | Full-wave simulators such as CST/HFSS | Analytical formulation, phase optics and optimization |

### Synthesis roadmap: three steps to a metasurface

When synthesizing a metasurface from scratch, follow these three steps in order:

1. **Wave transformation:** calculate the incident and desired outgoing phases and amplitudes on the surface, and their differences.
2. **Macroscopic response:** determine the local phase shift, transmission/reflection coefficient or surface impedance.
3. **Microscopic implementation:** consult the unit-cell library and place a cell with the required geometrical dimensions at each location.

$$
\text{wave requirements}\ \longrightarrow\ \text{surface response}\ \longrightarrow\ \text{physical implementation}.
$$

## 5.2 Specify the wave transformation

Let us unpack the first step using simple mathematics. Imagine our metasurface as an infinitely thin sheet of paper spread across $z=0$. The wave arriving from the source has an incident electric field:

$$
E_{\rm inc}(\mathbf r)=A_{\rm inc}(\mathbf r)e^{-i\phi_{\rm inc}(\mathbf r)}.
$$

The wave we wish to leave the surface, whether reflected or transmitted, is the desired outgoing field:

$$
E_{\rm out}(\mathbf r)=A_{\rm out}(\mathbf r)e^{-i\phi_{\rm out}(\mathbf r)}.
$$

Here $\mathbf r=(x,y)$ denotes each position on the surface. Classroom question: what must the surface do to the input to produce the output? Simple! Its transmission/reflection response $T(\mathbf r)$ must multiply the input:

$$
E_{\rm out}=T E_{\rm inc}.
$$

In the ideal lossless phase-only picture, let $A_{\rm inc}=A_{\rm out}=1$. The source writes the local phase shift as follows:

$$
T(\mathbf r)=e^{i\Phi(\mathbf r)}.\qquad\text{[as printed in the source]}
$$

The key to the first step is the following simple difference:

$$
\Phi(x,y)=\phi_{\rm out}(x,y)-\phi_{\rm inc}(x,y)\pmod{2\pi}.
$$

Subtract the input phase from the output phase to find the phase change required at every position!

### Three applications you should know

### 1. Beam steering and generalized Snell law

Suppose a plane wave arrives at $\theta_{\rm in}$ and must leave at $\theta_{\rm out}$. A plane wave’s surface phase varies as $k_0x\sin\theta$, so its input and output phases are:

$$
\phi_{\rm inc}(x)=k_0x\sin\theta_{\rm in}.
$$

$$
\phi_{\rm out}(x)=k_0x\sin\theta_{\rm out}.
$$

Their difference gives a linear phase gradient:

$$
\Phi(x)=k_0x(\sin\theta_{\rm out}-\sin\theta_{\rm in}).
$$

Differentiate with respect to x to recover generalized Snell law:

$$
\frac{d\Phi}{dx}=k_0(\sin\theta_{\rm out}-\sin\theta_{\rm in}).
$$

In everyday language: to bend the wave, increase the cell phase shift with a constant slope from left to right!

### 2. Focusing a beam: a metalens

We want a normally incident plane wave, $\phi_{\rm inc}=0$, to arrive in phase at one axial focal point a distance $F$ away. The geometrical distance from $(x,y)$ to the focus is $\sqrt{x^2+y^2+F^2}$. Compensating the delay of longer paths requires a hyperbolic phase bowl:

$$
\Phi(x,y)=\frac{2\pi}{\lambda_0}\left(F-\sqrt{x^2+y^2+F^2}\right).
$$

### 3. Vortex beams and orbital angular momentum

To create a twisted, tornado-like beam of topological charge $\ell$, which the source proposes for communication multiplexing, make the surface phase linear in azimuth $\varphi$:

$$
\Phi(r,\varphi)=\ell\varphi.
$$

In Cartesian coordinates, the source uses $\varphi=\arctan(y/x)$. On making one complete turn around the center, $2\pi$ radians, the phase winds by $2\pi\ell$!

### Real-world obstacles

Everything looks beautiful on paper, but practice brings two important physical obstacles:

1. **Power-density mismatch:** sharply deflecting a broad beam changes its cross-section and local power density. Changing only phase can send power into unwanted sidelobes or parasitic reflections and reduce efficiency.
2. **Locality assumption:** the formulas treat each cell as living in its own world, independent of neighbors. In practice, steep phase gradients bring near-field mutual coupling, so the cell response differs from the response calculated individually.

## 5.3 Translate fields into a macroscopic response

We have expressed the desired input and output fields on $z=0$ for steering or focusing. Now comes the million-dollar question: how do we turn those paper fields into an equivalent physical specification?

The metasurface acts like a magical two-dimensional boundary: a wave arrives, meets the boundary and changes course as we wish. To find the required behavior, we must return to boundary conditions.

### 5.3.1 Generalized sheet transition conditions

In traditional electromagnetics we learned tangential electric-field continuity, $\mathbf E_{t1}=\mathbf E_{t2}$. A metasurface deliberately breaks this continuity in a controlled way, using generalized sheet transition conditions, GSTCs.

Define the jumps and averages on the interface:

$$
\Delta\mathbf E_t=\mathbf E_t(0^+)-\mathbf E_t(0^-).
$$

$$
\Delta\mathbf H_t=\mathbf H_t(0^+)-\mathbf H_t(0^-).
$$

$$
\mathbf E_{t,\rm av}=\frac{\mathbf E_t(0^+)+\mathbf E_t(0^-)}{2}.
$$

$$
\mathbf H_{t,\rm av}=\frac{\mathbf H_t(0^+)+\mathbf H_t(0^-)}{2}.
$$

These jumps arise directly from electric and magnetic surface polarization densities:

$$
\hat{\mathbf z}\times\Delta\mathbf H=i\omega\mathbf P_{s,t}-\hat{\mathbf z}\times\nabla_tM_{s,z}.
$$

$$
\Delta\mathbf E\times\hat{\mathbf z}=i\omega\mu_0\mathbf M_{s,t}-\nabla_t(P_{s,z}/\epsilon_0)\times\hat{\mathbf z}.
$$

If the structure is very thin and does not produce strong normal components, $P_{s,z}\approx0$ and $M_{s,z}\approx0$, the description becomes tidy:

$$
\mathbf P_{s,t}=\epsilon_0\overline{\overline\chi}_{ee}\cdot\mathbf E_{t,\rm av}.
$$

$$
\mathbf M_{s,t}=\overline{\overline\chi}_{mm}\cdot\mathbf H_{t,\rm av}.
$$

The electric and magnetic surface-susceptibility tensors determine the physical identity of our surface.

### 5.3.2 Local surface impedance: the practical version

To be honest, full susceptibility tensors can complicate many projects unnecessarily. Particularly for reflective metasurfaces with a metal ground plane, local surface impedance is a welcome simplification.

### A. Reflection

With no field behind the ground plane, calculate the ratio of tangential electric and magnetic fields at the surface:

$$
\mathbf E_t(x,y)=Z_s(x,y)[\hat{\mathbf z}\times\mathbf H_t(x,y)].
$$

$$
Z_s(x,y)=\frac{E_{t,\rm inc}(x,y)+E_{t,\rm ref}(x,y)}{H_{t,\rm inc}(x,y)+H_{t,\rm ref}(x,y)}.
$$

Simply add your incident and desired reflected fields, divide, and obtain the required impedance at every point!

### B. Transmission

For thin layers without a ground plane, a surface admittance can represent the magnetic-field jump:

$$
\hat{\mathbf z}\times(\mathbf H_t^+-\mathbf H_t^-)=Y_s(x,y)\mathbf E_t(x,y).
$$

### 5.3.3 Reality check: can we build this surface?

When the formulas deliver $Z_s(x,y)$, do not rush excitedly into a full-wave simulation! First check the physical conditions.

### 1. Passivity

Can the surface operate without a battery or amplifier?

$$
\operatorname{Re}Z_s(x,y)\ge0.
$$

- If $\operatorname{Re}Z_s=0$, excellent: the surface is purely reactive and lossless, $Z_s=iX_s$, using inductive and capacitive behavior.
- If $\operatorname{Re}Z_s>0$, some energy becomes heat: the surface is lossy.
- If $\operatorname{Re}Z_s<0$, that point requires gain, impossible for the stated passive local load.

### 2. Local power mismatch

Suppose normal incidence must be redirected to $70^\circ$. Because $\cos0\ne\cos70^\circ$, equal field amplitudes do not preserve normal power through corresponding areas. Insisting on a purely local impedance can require regions that generate power and others that dissipate it.

What can we do? Use evanescent modes and nonlocal coupling to redistribute power along the surface, or optimize a reactive approximation with $\operatorname{Re}Z_s=0$ and accept some efficiency loss.

:::{admonition} Worked exercise
:class: tip
A reflective metasurface has a metallic ground plane and is modeled by a local surface impedance $Z_s$. At one frequency the desired reflection coefficients at three points are

$$\Gamma_A=i,\qquad\Gamma_B=0.5,\qquad\Gamma_C=1.5.$$

Assume normal incidence in free space, $\eta_0=120\pi\simeq377\,\Omega$, and use $Z_s=\eta_0(1+\Gamma)/(1-\Gamma)$.

1. Calculate the impedance at A, B and C.
2. Classify each point: lossless reactive; passive dissipative; or active and requiring energy generation.
3. Explain why $|\Gamma|>1$ is incompatible with a passive surface in this model.
4. If only the phase changes across the surface and reflected amplitude stays constant, how does $|\Gamma|$ vary?

```{dropdown} Show the worked answer

### 1. Surface impedance at A

$$
Z_{s,A}=\eta_0\frac{1+i}{1-i}.
$$

To simplify, multiply numerator and denominator by the conjugate of the denominator, namely $1+i$.

$$
Z_{s,A}=\eta_0\frac{(1+i)(1+i)}{(1-i)(1+i)}.
$$

The denominator is

$$
(1-i)(1+i)=2.
$$

The numerator is

$$
(1+i)^2=1+2i+i^2=2i.
$$

Therefore,

$$
Z_{s,A}=\eta_0\frac{2i}{2}.
$$

$$
Z_{s,A}=i\eta_0.
$$

Substitute $\eta_0$:

$$
Z_{s,A}\simeq i377\,\Omega.
$$

The real part is zero:

$$
\operatorname{Re}Z_{s,A}=0.
$$

Thus point A is purely reactive and lossless.

### 2. Surface impedance at B

At B,

$$
\Gamma_B=0.5.
$$

Hence

$$
Z_{s,B}=\eta_0\frac{1+0.5}{1-0.5}.
$$

$$
Z_{s,B}=\eta_0\frac{1.5}{0.5}.
$$

$$
Z_{s,B}=3\eta_0.
$$

Substitute the free-space impedance:

$$
Z_{s,B}=3(377).
$$

The result is

$$
Z_{s,B}\simeq1131\,\Omega.
$$

Here,

$$
\operatorname{Re}Z_{s,B}>0.
$$

The surface is passive, but converts some wave power into heat. The reflection amplitude is

$$
|\Gamma_B|=0.5.
$$

Some power is reflected and the remainder is dissipated. With no transmitted power, the reflected-power coefficient is

$$
R=|\Gamma_B|^2=(0.5)^2=0.25.
$$

Thus about 25% is reflected and 75% is absorbed or dissipated.

### 3. Surface impedance at C

At C,

$$
\Gamma_C=1.5.
$$

Therefore,

$$
Z_{s,C}=\eta_0\frac{1+1.5}{1-1.5}.
$$

$$
Z_{s,C}=\eta_0\frac{2.5}{-0.5}.
$$

$$
Z_{s,C}=-5\eta_0.
$$

Consequently,

$$
Z_{s,C}=-5(377).
$$

$$
Z_{s,C}\simeq-1885\,\Omega.
$$

At this point,

$$
\operatorname{Re}Z_{s,C}<0.
$$

To produce this reflection coefficient the surface must supply energy. A completely passive surface cannot do this: an amplifier, external source or other active mechanism is required.

### 4. Classify the surface points

| Point | Reflection coefficient | Surface impedance | Behavior |
|---|---|---|---|
| A | $i$ | $i377\,\Omega$ | Lossless and reactive |
| B | $0.5$ | $1131\,\Omega$ | Passive and dissipative |
| C | $1.5$ | $-1885\,\Omega$ | Active; supplied energy required |

Thus A is reactive and lossless; B is passive but dissipative; C is active and cannot be realized by the passive local surface assumed here.

### 5. Why is a magnitude above one incompatible with passivity?

The reflected-power coefficient is

$$
R=|\Gamma|^2.
$$

At C,

$$
R_C=|1.5|^2=2.25.
$$

The reflected power would be 225% of the incident power. This is possible only if the surface adds energy from another source. Therefore,

$$
|\Gamma|>1\quad\Longrightarrow\quad R>1.
$$

This is impossible for the passive local one-port. The impedance expresses the same active behavior through

$$
\operatorname{Re}Z_s<0.
$$

### 6. Pure phase control

If only reflected phase varies and amplitude remains constant, write

$$
\Gamma(x,y)=|\Gamma|e^{i\Phi(x,y)}.
$$

Here $|\Gamma|$ does not vary across the surface; only its phase changes. For an ideal lossless surface,

$$
|\Gamma|=1.
$$

Therefore,

$$
\Gamma(x,y)=e^{i\Phi(x,y)}.
$$

Under these conditions,

$$
R=|\Gamma|^2=1.
$$

All incident power is reflected; its direction, wavefront or phase changes. In a real design, phase control alone does not always realize the desired transformation: power-density mismatch can produce unwanted reflection, sidelobes, or a need for loss and gain.

**Conceptual point.** A phase profile alone does not specify a complete physical metasurface. Amplitude, phase and passivity must be checked together.

```
:::

## 5.4 Phase calibration and physical cell placement

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

## 5.5 Amplitude synthesis and power management

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

## 5.6 Polarization synthesis and geometric phase

Until now we mostly changed cell dimensions—patch length, slot radius and so on—to tune phase and amplitude. This is called dynamic, or resonant, phase control.

But suppose we want very broad bandwidth, or relief from nanometer- and micrometer-scale fabrication tolerances. Can a simple rotation control phase without changing cell dimensions or resonance? The answer is geometric phase, also called Pancharatnam–Berry (PB) phase.

### 5.6.1 Jones matrix and anisotropic cells

Use the Jones matrix to analyze a cell under different polarizations. An anisotropic element, such as a rectangular patch or dipole, responds differently along its principal axes $u$ and $v$:

$$
J_{\rm local}=\begin{bmatrix}t_u&0\\0&t_v\end{bmatrix}=\begin{bmatrix}A_ue^{i\phi_u}&0\\0&A_ve^{i\phi_v}\end{bmatrix}.
$$

### 5.6.2 Rotate the element and illuminate it circularly

Now rotate the element in its plane through $\theta$ relative to $x$, and illuminate it with a circularly polarized wave. Write its Jones vector as

$$
\mathbf E_{\rm inc}^{\sigma}=\frac1{\sqrt2}\begin{bmatrix}1\\i\sigma\end{bmatrix}.
$$

The source labels $\sigma=+1$ as LCP and $\sigma=-1$ as RCP. The transmitted or reflected field from the rotated cell is

$$
\mathbf E_{\rm out}=J(\theta)\mathbf E_{\rm inc}^{\sigma}=\underbrace{\frac{t_u+t_v}{2}\mathbf E_{\rm inc}^{\sigma}}_{\text{co-polarized}}+\underbrace{\frac{t_u-t_v}{2}e^{-i2\sigma\theta}\mathbf E_{\rm inc}^{-\sigma}}_{\text{cross-polarized}}.
$$

Two very important conclusions follow.

**1. PB phase law.** The component whose circular polarization is reversed receives a phase shift $\Phi=\pm2\theta$. Rotate the cell $90^\circ$ and the phase changes $180^\circ$; sweep the orientation through $180^\circ$ and the phase spans the full $360^\circ$ ($2\pi$) range.

**2. Frequency independence of the geometric factor.** The source emphasizes that $2\theta$ itself has no dependence on frequency or patch dimensions and calls it geometric and topological. The response multiplying that factor still needs the qualification below.

### 5.6.3 The half-wave condition for complete conversion

To direct maximum power into the controlled geometric-phase channel, cancel the co-polarized amplitude and maximize the cross-polarized one:

$$
\frac{t_u+t_v}{2}=0\quad\Longrightarrow\quad t_u=-t_v.
$$

The cell should act as a half-wave plate (HWP), with:

- equal principal-axis amplitudes, $|t_u|=|t_v|\approx1$;
- a $180^\circ$ phase difference, $\Delta\phi=|\phi_u-\phi_v|=180^\circ=\pi$.

The source illustrates this with phase zero along $u$ and $180^\circ$ along $v$. When the equal unit-amplitude and half-wave conditions hold, polarization-conversion efficiency (PCE) reaches 100% and all input energy enters the PB-modulated wave.

### 5.6.4 Other polarization transformations

By adjusting the Jones matrix and cell thickness, we can also make:

- **Linear-to-circular converters:** a quarter-wave plate (QWP) with equal principal-axis amplitudes and $90^\circ$ retardance converts linear input at $45^\circ$ to the axes into circular polarization.
- **Linear polarization rotators:** chiral structures or half-wave plates rotate the electric-field orientation in the plane.

This flexibility opens the way to lenses, holograms and intelligent surfaces.

:::{admonition} Worked exercise
:class: tip
A cell illuminated by circular polarization with $\sigma=+1$ is rotated through $30^\circ$. What is the cross-polarized geometric phase?

```{dropdown} Show the worked answer

The geometric-phase relation is

$$
\Phi_{\rm PB}=-2\sigma\theta.
$$

Therefore,

$$
\Phi_{\rm PB}=-2(+1)(30^\circ)=-60^\circ.
$$

So

$$
\Phi_{\rm PB}=-60^\circ.
$$

```
:::

:::{admonition} Worked exercise
:class: tip
For $\sigma=-1$, find the rotation producing geometric phase $140^\circ$.

```{dropdown} Show the worked answer

We have

$$
\Phi_{\rm PB}=-2\sigma\theta.
$$

Insert the given phase and spin:

$$
140^\circ=-2(-1)\theta.
$$

$$
140^\circ=2\theta.
$$

Thus

$$
\theta=70^\circ.
$$

```
:::

:::{admonition} Worked exercise
:class: tip
What relation between $t_u$ and $t_v$ cancels the co-polarized component?

```{dropdown} Show the worked answer

We require

$$
\frac{t_u+t_v}{2}=0.
$$

Consequently,

$$
t_u=-t_v.
$$

The two responses have equal amplitudes and a $180^\circ$ phase difference.

```
:::

:::{admonition} Worked exercise
:class: tip
A half-wave plate receives linear polarization at $\alpha=20^\circ$, while its axis is at $\theta=40^\circ$ to the reference. Find the output polarization angle.

```{dropdown} Show the worked answer

For a half-wave plate,

$$
\alpha_{\rm out}=2\theta-\alpha.
$$

Hence

$$
\alpha_{\rm out}=2(40^\circ)-20^\circ.
$$

$$
\alpha_{\rm out}=60^\circ.
$$

```
:::

:::{admonition} Worked exercise
:class: tip
An anisotropic half-wave cell has $|t_u|=|t_v|=0.95$ and $180^\circ$ retardance. Is co-polarization ideally cancelled? Can conversion efficiency be 100%?

```{dropdown} Show the worked answer

Equal amplitudes and half-wave retardance give

$$
t_u=-t_v.
$$

Thus co-polarization is ideally cancelled. However,

$$
|t_u|=|t_v|=0.95<1.
$$

The corresponding normalized power is

$$
|t_u|^2=|t_v|^2=(0.95)^2=0.9025.
$$

Thus the converted fraction of incident power is 90.25%, not 100%, for equal external wave admittances. The correct retardance cancels co-polarization, but unit principal-axis amplitudes are also required for complete incident-power conversion. The missing 9.75% must be accounted for in reflection, loss or other channels.

```
:::

## 5.7 Optimization and inverse design

So far our synthesis has mostly followed a forward, heuristic route: choose a familiar rectangular patch, split ring or cross, simulate it in CST or HFSS, obtain its calibration curve, and assemble cells using local periodicity.

But complicated, multifunctional requirements—multiple bands, several incidence angles or nonlinear phase/amplitude relationships—can defeat manual trial and error or reduce efficiency. Inverse design and optimization algorithms change how we search.

**Traditional route:** specified geometry → electromagnetic simulation → inspect response → manually adjust dimensions, in a time-consuming loop.

**Inverse route:** desired response → optimization or AI → automatic synthesis of a candidate geometry.

### 5.7.1 Write synthesis as an optimization problem

The goal is a geometric parameter vector $\mathbf p=[p_1,p_2,\ldots,p_N]^T$ minimizing a specified cost:

$$
\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$

The cost measures the mismatch between simulated fields $E_{\rm sim}$ or scattering parameters $S_{\rm sim}$ and the desired response $E_{\rm target}$:

$$
\mathcal L(\mathbf p)=w_1\int_\Omega\|E_{\rm sim}(\mathbf p,\mathbf r)-E_{\rm target}(\mathbf r)\|^2\,d\mathbf r+w_2(1-\eta_{\rm eff})+\operatorname{Penalty}(\mathbf p).
$$

Here:

- $w_1,w_2$ weight the priorities of different design objectives.
- $\eta_{\rm eff}$ is useful output-power efficiency.
- $\operatorname{Penalty}$ penalizes violations of fabrication rules (DRC), such as slots or lithographic traces below the process minimum.

### 5.7.2 Gradients and the adjoint method

For continuous geometric parameters, the source presents gradient methods as a fast route to an optimum. But computing each partial derivative $\partial\mathcal L/\partial p_i$ by perturbing one variable and repeating the simulation becomes extremely expensive for thousands of pixels—potentially months of work!

The adjoint-state method addresses this bottleneck and resembles backpropagation in neural networks.

1. **Forward simulation:** excite the structure with the original source and record $E_{\rm fwd}$.
2. **Adjoint simulation:** place a virtual source at the output, with amplitude related to response error, and excite the structure to obtain $E_{\rm adj}$.
3. **Extract the gradient:** combine the two fields point by point to obtain sensitivity to material changes across the surface. The source gives the schematic relation

$$
\frac{\partial\mathcal L}{\partial\epsilon(\mathbf r)}\propto\operatorname{Re}\{E_{\rm fwd}(\mathbf r)\cdot E_{\rm adj}(\mathbf r)\}.
$$

Thus, in the source’s single-objective setting, gradients for all pixels or parameters are obtained with only two field solves: a major computational saving. The exact derivative and solve count need the qualifications below.

### 5.7.3 Metaheuristic and stochastic algorithms

When the response landscape is highly nonconvex with many local minima, or variables are discrete—binary metal/no-metal pixels, for example—ordinary gradients can get trapped or be inapplicable. Evolutionary and swarm methods provide alternatives.

**Genetic algorithm (GA).** Encode pixels as binary chromosomes: zero for dielectric and one for copper. Crossover and mutation evolve patterns over generations. The source emphasizes that unexpected, innovative patterns can emerge to meet the target.

**Particle swarm optimization (PSO).** Particles move through geometric parameter space, adjusting their motion according to personal best $p_{\rm best}$ and group best $g_{\rm best}$ experiences.

### 5.7.4 Deep-learning approaches

Deep neural networks can act as very fast surrogate models for numerical simulators. The source describes examples where synthesis after training drops from hours to a fraction of a second.

**Forward network.** Input geometry such as $[L,W]$ and rapidly estimate amplitude, phase or the scattering matrix.

**Inverse and tandem networks.** Desired phase/amplitude goes in and geometry comes out. The difficulty is one-to-many mapping: several geometries can give the same electromagnetic response, creating conflicting training labels. In a tandem architecture, a pretrained, frozen forward network follows the inverse network, so training loss is measured on the predicted physical response. The source says this completely resolves nonuniqueness; the separate note explains the distinction between resolving label conflict and removing physical nonuniqueness.

**Generative models (GANs and VAEs).** These enable freeform design beyond standard squares and circles, producing complex patterns. The source describes them as offering the highest scattering efficiency and bandwidth; these are design aspirations, not a guarantee of global optimality.

:::{admonition} Worked exercise
:class: tip
State the main difference between direct and inverse design.

```{dropdown} Show the worked answer

In direct design, choose a geometry first and simulate its electromagnetic response. If the result is unsuitable, manually modify the geometry. In inverse design, specify the desired response first, then use optimization or AI to find a geometry that can produce it.

```
:::

:::{admonition} Worked exercise
:class: tip
A cell is described by length, width and thickness. Write its geometric parameter vector.

```{dropdown} Show the worked answer

Define the vector as

$$
\mathbf p=\begin{bmatrix}L\\W\\h\end{bmatrix}.
$$

Here $L$ is cell length, $W$ is cell width, and $h$ is the thickness of its metal or dielectric layer.

```
:::

:::{admonition} Worked exercise
:class: tip
Write inverse design as an optimization problem for geometric parameters that realize a desired electromagnetic response.

```{dropdown} Show the worked answer

Collect the geometric parameters into

$$
\mathbf p=\begin{bmatrix}p_1\\p_2\\\vdots\\p_N\end{bmatrix}.
$$

Choose them to minimize cost:

$$
\min_{\mathbf p}\mathcal L(\mathbf p).
$$

Fabrication bounds usually apply, giving

$$
\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$

$\mathcal L$ is design error or cost, $\mathbf p_{\min}$ contains minimum allowed geometric values, and $\mathbf p_{\max}$ contains the maximum values. The aim is a geometry with minimal electromagnetic mismatch while respecting fabrication limits.

```
:::

:::{admonition} Worked exercise
:class: tip
What does the cost function measure in inverse design?

```{dropdown} Show the worked answer

It measures the mismatch between simulated and desired responses. Smaller mismatch indicates a better design under the chosen objective. For example, use field error:

$$
\mathcal L=\int_\Omega\|E_{\rm sim}-E_{\rm target}\|^2\,d\mathbf r.
$$

Efficiency and fabrication limits can also be included.

```
:::

:::{admonition} Worked exercise
:class: tip
Explain $w_1,w_2$ in $\mathcal L=w_1\mathcal L_{\rm field}+w_2(1-\eta_{\rm eff})$.

```{dropdown} Show the worked answer

They set relative priorities:

- $w_1$ controls the importance of reducing field or electromagnetic-response error.
- $w_2$ controls the importance of increasing efficiency.

Increasing $w_2$ gives greater priority to efficiency, with other scaling held fixed.

```
:::

:::{admonition} Worked exercise
:class: tip
Why include a penalty term in the cost?

```{dropdown} Show the worked answer

It discourages designs that are unsuitable or impossible to fabricate. If a slot or metal trace is narrower than the process minimum, add a cost:

$$
\mathcal L_{\rm total}=\mathcal L_{\rm error}+\operatorname{Penalty}.
$$

$\mathcal L_{\rm error}$ measures electromagnetic mismatch and Penalty is the additional cost of violating fabrication limits. This guides the search toward designs that perform well and can be made.

```
:::

:::{admonition} Worked exercise
:class: tip
Give one simple difference between GA and PSO.

```{dropdown} Show the worked answer

GA evolves designs through generations, crossover and mutation. PSO moves particles through the design space using their personal and collective best experiences. Typically GA suits discrete variables and binary patterns; PSO is used for numerical, continuous parameters.

```
:::

:::{admonition} Worked exercise
:class: tip
What are the input and output of a forward neural network for metasurfaces?

```{dropdown} Show the worked answer

Input is cell geometry, for example

$$
[L,W].
$$

Output is the electromagnetic response, for example

$$
|S_{21}|,\qquad\arg S_{21}.
$$

More generally, it predicts response amplitude and phase.

```
:::

:::{admonition} Worked exercise
:class: tip
Suggest a method for (a) continuous patch length/width optimization; (b) a binary metal pattern; (c) fast cell-response prediction after training.

```{dropdown} Show the worked answer

(a) A gradient method or PSO. (b) A genetic algorithm. (c) A forward neural network as a surrogate model.

```
:::

:::{admonition} Worked exercise
:class: tip
A cost is $\mathcal L=w_1E_{\rm field}+w_2(1-\eta)$. Calculate it for $w_1=2$, $w_2=1$, $E_{\rm field}=0.1$, $\eta=0.8$.

```{dropdown} Show the worked answer

First,

$$
1-\eta=1-0.8=0.2.
$$

Therefore,

$$
\mathcal L=2(0.1)+1(0.2).
$$

$$
\mathcal L=0.2+0.2.
$$

The result is

$$
\mathcal L=0.4.
$$

A smaller value indicates closer agreement with the selected combined objective.

```
:::

:::{admonition} Worked exercise
:class: tip
List the three main stages of simulation- and optimization-based inverse design.

```{dropdown} Show the worked answer

1. **Define the target and cost:** specify amplitude, phase, efficiency and fabrication limits.
2. **Search the design space:** use gradients, adjoints, GA, PSO or neural models as appropriate.
3. **Validate the final geometry:** simulate the complete structure and compare actual and target responses, accounting for mutual coupling and fabrication limits.

```
:::

