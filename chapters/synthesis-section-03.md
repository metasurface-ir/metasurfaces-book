---
title: "5.3 Translate fields into a macroscopic response"
---

# 5.3 Translate fields into a macroscopic response

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


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
The source says “three conditions” but enumerates two; both are retained here. No missing third condition has been invented.

Fix the normal and magnetic projection before interpreting an impedance ratio. For the grounded scalar load, choose $\hat{\mathbf n}$ pointing from the load into the incident region and use $\mathbf E_t=Z_s(\hat{\mathbf n}\times\mathbf H_t)$. The scalar magnetic denominator means that oriented projection, not an unoriented magnitude. At normal incidence this yields $Z_s=\eta_0(1+\Gamma)/(1-\Gamma)$. Reversing the normal reverses the corresponding oriented relation.

The electric-sheet admittance acts on the appropriate sheet field, normally the tangential average in a GSTC constitutive model. Neglecting normal polarizations requires their contributions to be small; thinness alone is insufficient. The susceptibility relations shown also omit magnetoelectric coupling. Equivalent electric/magnetic currents need not mean actual monopoles.

Pointwise $\operatorname{Re}Z_s\ge0$ applies to the stated local scalar load. A nonlocal passive surface may redistribute power laterally; a local field ratio with magnitude above one then need not imply global gain. The worked one-port problem has no such extra power supply or transport channels.

In the phase-only worked answer, the source reuses $\Phi$ for $\arg\Gamma$ in $\Gamma=|\Gamma|e^{i\Phi}$. This signed argument is the negative of the field phase lag used in Section 5.2; distinguish the two when mapping to a library.
:::
