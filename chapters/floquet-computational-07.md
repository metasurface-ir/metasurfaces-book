---
title: "Channel existence and diffraction efficiency"
---

(ch04-section-07)=
# Channel existence and diffraction efficiency

Knowing $k_{x,m}$ and $k_{z,m}$ identifies the available basis waves. Solving Maxwell's boundary-value problem determines their amplitudes. A symmetry-forbidden order, an unpatterned interface, or destructive interference can give zero amplitude in an open channel.

To convert amplitudes into power, state their normalization. For a TE wave represented by $E_y$ in an isotropic lossless medium,

$$
\langle S_z\rangle=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\mu}\right)|E_y|^2.
$$

For an open transmitted order with $t_m=E_{y,m}^{(t)}/E_{y,i}$,

$$
T_m=\frac{k_{z,m}^{(t)}/\mu_t}{k_{z,i}/\mu_i}|t_m|^2.
$$

With equal permeabilities, the factor is $n_t\cos\theta_m/(n_i\cos\theta_i)$. This expression is for the stated TE electric-field amplitude. A TM coefficient defined using tangential $E_x$ needs a different admittance factor; using $H_y$ gives a corresponding expression with $\epsilon$ in place of $\mu$. For compatible **power-normalized** port amplitudes, squared magnitude directly gives the power fraction.

For a passive scattering problem, use all outgoing propagating channels and any genuine absorption:

$$
\sum_{m\in\mathcal P_r}R_m+
\sum_{m\in\mathcal P_t}T_m+A=1.
$$

At exact grazing, a bounded field amplitude has zero normal flux. Power normalization becomes delicate as the normal component approaches zero. A closed-channel field coefficient should not be counted as an extra far-field power fraction.

:::{dropdown} Derivation: TE/TM power factors and why powers add by order
Faraday's law for a TE harmonic gives $\mathbf H=(\mathbf k\times\mathbf E)/(\omega\mu)$. With $\mathbf E=\hat{\mathbf y}E_y$, take the cross product and then the time-averaged Poynting vector:

$$
H_x=-\frac{k_z}{\omega\mu}E_y,\qquad
H_z=\frac{k_x}{\omega\mu}E_y,\qquad
\langle S_z\rangle=-\frac12\operatorname{Re}(E_yH_x^*)
=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\mu}\right)|E_y|^2.
$$

Divide the transmitted flux by the incident flux to obtain $T_m$. On the reflected side the outward flux is $-\langle S_z\rangle$, so a positive reflected power uses $\kappa_m$ rather than the negative laboratory $k_z$. For $k_z=\pm (-i)\alpha$ and real $\mu$, the real part is zero: one outgoing evanescent harmonic carries no average normal power.

For TM, Ampère's law gives $\mathbf E=-(\mathbf k\times\mathbf H)/(\omega\epsilon)$. Using $\mathbf H=\hat{\mathbf y}H_y$ gives, away from $k_z=0$ for the last expression,

$$
E_x=\frac{k_z}{\omega\epsilon}H_y,\qquad
\langle S_z\rangle=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\epsilon}\right)|H_y|^2
=\frac12\operatorname{Re}\!\left(\frac{\omega\epsilon}{k_z}\right)|E_x|^2.
$$

Thus TE $E_y$, TM $H_y$, and TM tangential $E_x$ coefficients require different stated normalizations. Evaluate cutoff using bounded physical fields or a limit; the $E_x$ admittance formula is singular at $k_z=0$.

Finally, average the outgoing field's normal flux across a full period. Products of distinct orders contain $e^{-i(k_{x,m}-k_{x,n})x}$, and

$$
\frac1\Lambda\int_0^\Lambda e^{-i(k_{x,m}-k_{x,n})x}\,dx
=\frac1\Lambda\int_0^\Lambda e^{-i(m-n)Gx}\,dx=\delta_{mn}.
$$

This orthogonality removes cross terms between distinct orders. It justifies summing modal powers in homogeneous exterior planes even when the local Poynting pattern has interference fringes. It does not say that distinct orders never interfere locally or that evanescent fields can be removed from interface matching.
:::

### An analytical amplitude benchmark

At a flat nonmagnetic interface, translational invariance permits only the physical specular response, even if an artificial periodic cell lists many open channels. At normal incidence from $n_i=1$ to $n_t=1.5$, the TE Fresnel amplitudes are $r=-0.2$ and $t=0.8$. Thus $R=0.04$, $T=1.5|0.8|^2=0.96$, and $R+T=1$. Squaring $t$ alone would incorrectly report $T=0.64$.

The notebook checks this case and a total-internal-reflection limit. These are analytical interface checks, not simulations of a patterned metasurface. For numerical mode/flux normalization examples, see the official [Meep mode-decomposition tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/).
