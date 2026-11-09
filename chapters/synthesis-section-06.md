---
title: "5.6 Polarization synthesis and geometric phase"
---

# 5.6 Polarization synthesis and geometric phase

Instead of changing the resonator dimensions, rotate an anisotropic cell. In its principal axes, its Jones matrix is diagonal. Specify the rotation matrix and circular basis explicitly: handedness names depend on time convention and viewing direction. With the basis and coordinate rotation below, the converted channel gains a signed geometric phase $-2\sigma\theta$. This geometric factor is independent of frequency; the dynamic phase, amplitudes and conversion efficiency generally are not.

For a half-wave response, $t_u=-t_v$ cancels the co-polarized circular channel. Near-unity conversion additionally requires near-unit transmission in both principal axes with consistent power normalization. A quarter-wave element with equal amplitudes, 90-degree retardance and equal incident components can convert linear to circular polarization. A rotated half-wave plate maps a linear input angle $\alpha$ to $2\theta-\alpha$. Geometric phase does not eliminate bandwidth limits or fabrication sensitivity.


$$
J_0=\begin{pmatrix}t_u&0\\0&t_v\end{pmatrix},\qquad
R(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix},\qquad
J(\theta)=R(\theta)J_0R(-\theta).
$$
$$
\mathbf e_\sigma=\frac1{\sqrt2}\begin{pmatrix}1\\i\sigma\end{pmatrix},\qquad
J(\theta)\mathbf e_\sigma
=\frac{t_u+t_v}{2}\mathbf e_\sigma
+\frac{t_u-t_v}{2}e^{-2i\sigma\theta}\mathbf e_{-\sigma}.
$$
$$
\psi_{\rm PB}=-2\sigma\theta,\qquad t_u=-t_v,\qquad
\alpha_{\rm out}=2\theta-\alpha\pmod\pi.
$$


:::{admonition} Worked exercise 1
:class: tip
Find the converted-channel PB phase for $\sigma=+1$ and $\theta=30^\circ$.

```{dropdown} Show the answer
$$\psi_{\rm PB}=-2\sigma\theta=-2(+1)(30^\circ)=-60^\circ.$$

Use the explicitly defined circular basis and rotation convention.
```
:::


:::{admonition} Worked exercise 2
:class: tip
For $\sigma=-1$, what rotation gives a PB phase of $140^\circ$?

```{dropdown} Show the answer
$$140^\circ=-2(-1)\theta=2\theta\quad\Longrightarrow\quad\theta=70^\circ.$$

The result is understood modulo a half-turn for the element orientation.
```
:::


:::{admonition} Worked exercise 3
:class: tip
What cancels the co-polarized circular component?

```{dropdown} Show the answer
$$\frac{t_u+t_v}{2}=0\quad\Longleftrightarrow\quad t_u=-t_v.$$

Equal principal-axis amplitudes with a pi phase difference cancel the sum.
```
:::


:::{admonition} Worked exercise 4
:class: tip
A half-wave element has input angle $\alpha=20^\circ$ and axis angle $\theta=40^\circ$. Find the output angle.

```{dropdown} Show the answer
$$\alpha_{\rm out}=2\theta-\alpha=2(40^\circ)-20^\circ=60^\circ.$$

Angles use the same orientation convention; linear orientation is modulo 180 degrees.
```
:::


:::{admonition} Worked exercise 5
:class: tip
If both principal-axis amplitudes are 0.95 with a pi phase difference, is co-polarization cancelled? Is conversion 100%?

```{dropdown} Show the answer
$$t_u=-t_v,\qquad\eta_{\rm conv}=|t_u|^2=0.95^2=0.9025.$$

The sum cancels ideally, but incident-normalized converted power is 90.25% for equal exterior admittances. The remaining power must be accounted for in reflection or loss.
```
:::


The matrix above uses clockwise-positive coordinate angles. Measure both linear angles clockwise as well, with input vector $(\cos\alpha,-\sin\alpha)^T$, to use the stated $2\theta-\alpha$ rule. Using counterclockwise physical angles changes the rotation and PB signs together.

```{figure} ../assets/chapter-03/source-pb.svg
:alt: Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.

Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.
```

