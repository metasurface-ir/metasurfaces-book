---
title: "5.2 Specify the wave transformation"
---

# 5.2 Specify the wave transformation

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



:::{admonition} Scientific clarification — separate from the primary reading
:class: note
The printed $T=e^{+i\Phi}$ conflicts algebraically with the preceding fields and the definition $\Phi=\phi_{\rm out}-\phi_{\rm inc}$. Taking their ratio gives

$$
T=\frac{E_{\rm out}}{E_{\rm inc}}=\frac{A_{\rm out}}{A_{\rm inc}}e^{-i\Phi},\qquad\arg T=-\Phi\pmod{2\pi}.
$$

The steering and focusing expressions in the reading describe phase lag. Library phases are signed complex arguments, so match them to $-\Phi$, not $+\Phi$. This is the correction used in the existing computational work.

For a vortex, use $\varphi=\operatorname{atan2}(y,x)$ to retain all quadrants. The complex-field winding has the opposite sign to a phase-lag winding; physical OAM also depends on propagation direction and basis. A helical phase does not by itself multiply communication capacity: distinct usable channels, apertures and a receiver model must be demonstrated. The simple scalar ratio assumes nonzero input and an appropriate local scalar transformation.
:::

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
