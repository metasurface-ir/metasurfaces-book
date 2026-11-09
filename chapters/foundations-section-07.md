---
title: "1.7 How does a metasurface give a wave instructions? The control toolbox"
short_title: "1.7 How does a metasurface give a wave instructions? The control toolbox"
---

# 1.7 How does a metasurface give a wave instructions? The control toolbox

When an electromagnetic wave meets a metasurface, its unit cells can change four main wave properties. Let's see which buttons appear on this “magical control panel”:

### 1. The amplitude button

The cells can absorb some wave energy to reduce its amplitude. This is a wonderful property for radar absorbers—materials that swallow waves and prevent reflection—or spatial filters.

### 2. The phase button

This may be our most frequently used button! By changing the cell's shape or size, we can create a “time delay” in transmission or reflection, equivalent to a phase change. If these phases change step by step across the surface, the wavefront tilts, focuses, or takes on the shape we want.

### 3. The polarization button

Polarization means the direction of the electric field's oscillation. Some cells, particularly asymmetric shapes such as a cross with unequal arms, can receive a vertically oscillating wave and return a horizontal or even rotating, circularly polarized wave. This means complete control over the oscillation direction!

### 4. The direction button: generalized Snell's law

Remember learning in high-school physics that “the angle of incidence equals the angle of reflection”? Well, a metasurface gets around that classical rule!

By creating a continuous phase slope—a phase gradient—across the surface, it can reflect a normally incident wave obliquely at a steep angle. This upgraded rule is called **generalized Snell's law**, the basis of beam steering.

:::{note} Four controls, with physical constraints
Reduced amplitude in one channel can result from reflection, diffraction, or polarization conversion as well as absorption. Phase at one frequency is not a broadband time delay. Polarization control needs the relative amplitudes and phases of orthogonal components. A phase gradient changes tangential momentum without breaking Maxwell's equations; it does not give the outgoing efficiency.
:::

For a local transmitted phase $\Phi(x)$, signed angles from the selected normal give the useful phase-matching picture

$$
k_t\sin\theta_t-k_i\sin\theta_i=\frac{d\Phi}{dx}.
$$

The periodic channels and their amplitudes require [Chapter 4](04-periodic-floquet.md) and the full-structure checks of [Chapter 5](05-metasurface-synthesis.md). The [dielectric-post study of Arbabi et al.](https://arxiv.org/abs/1411.1494) demonstrates a specific phase/polarization platform. A passive surface can be lossy, and external tuning alone implies neither electromagnetic gain nor nonreciprocity.

(course-phasor-convention)=
### Computational connection: complex coefficients

We use the phasor convention

$$
E(t)=\operatorname{Re}\{\widetilde E e^{+i\omega t}\},\qquad
\widetilde E=Ae^{i\phi}.
$$

This convention applies throughout the book, its notebooks and browser laboratories. The symbols $j$ and $i$ denote the same imaginary unit. A forward plane wave has the spatial factor below; later chapters use these definitions without repeating them.

$$
\widetilde{\mathbf E}(\mathbf r)=\mathbf E_0e^{-i\mathbf k\cdot\mathbf r}.
$$

The magnitude $A$ and phase $\phi$ describe the field relative to a reference. A reflection or transmission coefficient is a complex ratio of an outgoing field amplitude to the chosen incident amplitude. Its phase also depends on where the reference planes are placed.

A coefficient $t=0.8e^{i\pi/2}$ has field magnitude 0.8 and phase $90^\circ$. In equal-impedance media at normal incidence, its transmitted power fraction is $T=|t|^2=0.64$. At an interface with different impedances or oblique incidence, the correct flux factors must be included. Chapter 2 will develop those factors; the present model deliberately keeps the exterior impedances equal.

At $t=0$, the phase is undefined. Near zero amplitude, a phase can be numerically unstable and physically unhelpful for a transmitted-wave design. Keep magnitude or power beside every phase plot, and state the threshold used when reporting phase.

The wrapped phase lies on a circle. $179^\circ$ and $-179^\circ$ differ by a circular separation of $2^\circ$, not $358^\circ$. An unwrapped phase follows a continuous branch across a parameter sweep; it still needs meaningful nonzero amplitude and sufficiently fine sampling.

