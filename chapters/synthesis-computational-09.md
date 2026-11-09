---
title: "Amplitude control and polarization"
---

# Amplitude control and polarization


A single width generally changes amplitude and phase together. Synthesis of an arbitrary complex field may require additional independent geometric parameters, anisotropy, interference, multiple layers, or a more constrained target. An amplitude taper can change scalar sidelobes and peak/width tradeoffs; its physical implementation must also account for discarded, reflected, and converted power.

For an anisotropic element with principal coefficients $t_x,t_y$, rotated by $\theta$ in the laboratory plane,

$$
J(\theta)=R(\theta)
\begin{bmatrix}t_x&0\\0&t_y\end{bmatrix}R(-\theta),
\quad R(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}.
$$

Define the fixed-basis circular states $\mathbf e_\sigma=(1,(-i)\sigma)^T/\sqrt2$. Then

$$
J(\theta)\mathbf e_\sigma=
\frac{t_x+t_y}{2}\mathbf e_\sigma+
\frac{t_x-t_y}{2}e^{-2i\sigma\theta}\mathbf e_{-\sigma}.
$$

The converted component acquires phase lag $2\sigma\theta$, corresponding to signed complex phase $-2\sigma\theta$. Its amplitude is controlled by $(t_x-t_y)/2$. For an ideal lossless retarder, $t_x=e^{-i\delta/2}$ and $t_y=e^{+i\delta/2}$, so the conversion fraction is $\sin^2(\delta/2)$. A half-wave response maximizes conversion; a rotation angle by itself does not establish high efficiency.

```{figure} ../assets/chapter-05/polarization.png
:alt: Opposite geometric-phase slopes for the two defined circular basis states and conversion versus retardance.

An ideal analytical Jones model. These curves are separate from the scalar TE ridge calculation and require a vector unit-cell design for physical realization.
```

The notebook verifies these coefficients, unitary half-wave matrices, and conversion fractions. For a physical anisotropic metasurface, extract a complete, consistently normalized vector response and retain the unwanted polarization channel. [Arbabi and colleagues](https://arxiv.org/abs/1411.1494) provide a primary example of dielectric phase/polarization control.

