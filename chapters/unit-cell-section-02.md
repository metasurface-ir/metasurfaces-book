---
title: "3.2 Choosing the meta-atom geometry: tuning resonators"
---

# 3.2 Choosing the meta-atom geometry: tuning resonators

The first question in a metasurface design class is: “What shape should this unit cell have?” The geometrical elements placed on the substrate are called **meta-atoms**. As a designer, you have countless choices: a square patch, a split-ring resonator (SRR), a cross, or even an H-shaped element.

Why do the shapes differ, and which should we choose? Recall the equivalent circuit in Section 2.16. A geometrical pattern on the substrate behaves approximately as an $LC$ resonator under electromagnetic illumination.

- **Capacitance $C$:** gaps between neighboring metal elements, or inside an element, store electric energy.
- **Inductance $L$:** surface-current paths along the metal store magnetic energy.

Its familiar resonance estimate is

$$
f_r=\frac{1}{2\pi\sqrt{LC}}.
$$

Changing a dimension, such as a cross-arm length, changes $L$ and $C$. The resonance moves, and the phase at our operating frequency changes. This is how geometry controls phase!

We can broadly distinguish two families, chosen according to the application:

### Resonant elements

Patches, disks, and crosses change their response when their dimensions change. This is useful for linear polarization. Sweeping a dimension, such as patch width, can sweep the transmitted or reflected phase from zero to nearly $360^\circ$.

### Geometric-phase elements

Here is an ingenious alternative. With circularly polarized illumination, we may keep the dimensions fixed and rotate an anisotropic element, such as a rectangle or ellipse, through an angle $\theta$. The converted circular-polarization channel acquires a geometric phase of $2\theta$ or $-2\theta$. The source describes the constant amplitude under rotation as an important advantage.

$$
\Delta\Phi=\pm2\theta.
$$

:::{note} What that promise assumes
A single resonance does not guarantee useful full-circle phase coverage at high amplitude. The $LC$ model is an approximation. For geometric phase, the conversion amplitude is rotation-independent only under the appropriate symmetry, illumination, and approximately half-wave response; conversion efficiency can be low. The sign depends on the chosen circular-polarization basis and whether phase means a signed argument or a lag.
:::

```{figure} ../assets/chapter-03/source-geometries.svg
:alt: Patch, disk, cross, split ring and dipole resting on dielectric slabs, with gap and current-path annotations.

Figure 3.2a. Five possible meta-atoms. Gap and current-path annotations identify conceptual capacitive and inductive regions, not extracted circuit values.
```

```{figure} ../assets/chapter-03/source-pb.svg
:alt: Identical rectangular elements on a substrate rotated through zero, forty-five and ninety degrees.

Figure 3.2b. Fixed dimensions, different rotation angles. The geometric-phase relation applies to the converted circular-polarization channel.
```
