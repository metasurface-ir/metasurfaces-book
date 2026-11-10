---
title: "5.6 Polarization synthesis and geometric phase"
---

# 5.6 Polarization synthesis and geometric phase

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


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
The PDF’s first sentence on page 111 is incomplete and its 5.6.2 heading is absent. The bridge sentence and heading above restore the logical connection without claiming to recover missing wording.

To reproduce the printed decomposition with $\mathbf e_\sigma=(1,i\sigma)^T/\sqrt2$, define $R(\alpha)=\left[\begin{smallmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{smallmatrix}\right]$ and $J(\theta)=R(-\theta)J_{\rm local}R(\theta)$: positive $\theta$ is a clockwise physical rotation. The computational notebook instead uses counterclockwise $J=R(\theta)DR(-\theta)$ with $\mathbf e_\sigma=(1,-i\sigma)^T/\sqrt2$. Both give the printed signed PB argument $-2\sigma\theta$ in their explicitly defined bases. Their $\sigma$ labels must not be interchanged without converting the basis. LCP/RCP labels also depend on viewing and propagation direction.

The geometric exponential is frequency independent, but $t_u,t_v$, conversion efficiency, loss and dynamic phase remain dispersive. PB phase alone does not remove fabrication sensitivity or make an achromatic lens. Zero and $180^\circ$ are one example; any common phase with a $\pi$ difference works. Cancelling co-polarization is not the same as converting all incident power.
:::


```{figure} ../assets/chapter-03/source-pb.svg
:alt: Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.

Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.
```
