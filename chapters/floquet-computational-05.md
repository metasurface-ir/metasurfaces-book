---
title: "Open, grazing, and evanescent channels"
---

(ch04-section-05)=
# Open, grazing, and evanescent channels

In output region $o$, the homogeneous-medium dispersion relation gives

$$
k_{z,m}^2=(n_o k_0)^2-k_{x,m}^2.
$$

For an outward distance $s\geq0$ measured away from the surface, define

$$
\kappa_m=k_0\sqrt{n_o^2-q_m^2},\qquad
E_m\propto e^{-ik_{x,m}x}e^{-i\kappa_m s},
$$

with the outgoing branch: nonnegative real $\kappa_m$ for propagation and negative imaginary $\kappa_m$ for decay. In laboratory coordinates, transmitted waves have $k_z=+\kappa_m$ and reflected waves have $k_z=-\kappa_m$ because their outward directions differ.

| Condition | Classification | Interpretation |
| --- | --- | --- |
| $|q_m|<n_o$ | Open / propagating | A real normal component allows outgoing normal power |
| $|q_m|=n_o$ | Grazing cutoff | The normal component vanishes; the limiting direction is $\pm90^\circ$ |
| $|q_m|>n_o$ | Closed / evanescent | The outgoing solution decays away from the surface |

For an open order,

$$
\theta_m=\sin^{-1}\!\left(\frac{q_m}{n_o}\right).
$$

Do not clip an arbitrary value outside $[-1,1]$ and report a grazing beam. First classify the channel. The notebook uses a dimensionless tolerance around $|q_m|/n_o=1$ and reports near-cutoff cases separately. That tolerance handles floating-point classification; it is not an uncertainty estimate for wavelength, material data, or geometry.

### What does an evanescent order do?

If $\kappa_m=(-i)\alpha_m$ with $\alpha_m>0$, its amplitude varies as $e^{-\alpha_m s}$. Its amplitude decay length is $1/\alpha_m$; its intensity decay length is $1/(2\alpha_m)$. In the specified lossless homogeneous exterior, one such isolated outgoing harmonic carries no net normal time-averaged power. It can still store reactive energy, affect interface matching, and mediate coupling near the structure.

Consequently, “closed in the far field” does not mean “safe to remove from an RCWA expansion.” Near cutoff, $\alpha_m$ can be small and the decay length large. Numerical harmonic convergence and port/reference-plane placement deserve particular attention there.

:::{dropdown} Derivation: the outgoing square root and the decay length
In a source-free, homogeneous isotropic exterior, Maxwell's equations give the scalar Helmholtz equation for a Cartesian field component. Substitution of one separated harmonic gives

$$
\left(\partial_x^2+\partial_s^2+n_o^2k_0^2\right)E_m=0
\quad\Longrightarrow\quad
\kappa_m^2=n_o^2k_0^2-k_{x,m}^2.
$$

For real positive $\epsilon,\mu$, the positive real root carries energy outward when the right-hand side is positive. If it is negative, the two roots are $\pm (-i)\alpha_m$. The outgoing field in an unbounded half-space must not grow as $s\to\infty$, selecting $-i\alpha_m$:

$$
\alpha_m=k_0\sqrt{q_m^2-n_o^2},\qquad
\frac{|E_m(s)|}{|E_m(0)|}=e^{-\alpha_m s},\qquad
\frac{|E_m(s)|^2}{|E_m(0)|^2}=e^{-2\alpha_m s}.
$$

Setting each ratio to $e^{-1}$ gives the two decay lengths. “Intensity” here means squared field magnitude, not a nonzero normal power flow. Section 4.7 derives why its normal time-averaged Poynting flux is zero.
:::

```{figure} ../assets/chapter-04/outgoing-fields.png
:alt: Real-field maps and envelopes of unit-amplitude open, grazing, and evanescent TE harmonics in an outward coordinate, with their normalized normal flux.
:label: fig-ch04-outgoing

Three analytical exterior harmonics in $n_o=1$, with $q_m=0.6$, $1$, and $1.2$. Their interface electric-field amplitudes are equal, yet their normal fluxes differ. The closed harmonic oscillates along the surface and decays outward. These are basis fields, not a solved device near field.
```

**Read the picture:** at cutoff, a field may still vary along $x$ while having no phase progression in $s$. Explain why a visible field pattern alone does not establish outward power.

### Count every potentially open order

The strict interval for an open integer order is

$$
\frac{\Lambda}{\lambda_0}(-n_o-q_i)<m<
\frac{\Lambda}{\lambda_0}(n_o-q_i).
$$

The endpoints must be tested separately for grazing. The notebook enumerates a conservative enclosing integer interval and adds closed neighbors for plotting. A fixed window such as $m=-2,\ldots,2$ can silently miss channels when the period or output index increases.

For an exact-arithmetic count, call the lower and upper endpoints above $a$ and $b$. Strict inequalities give

$$
m_{\min}=\lfloor a\rfloor+1,\qquad
m_{\max}=\lceil b\rceil-1,\qquad
N_{\rm open}=\max\!\left(0,m_{\max}-m_{\min}+1\right).
$$

This formula excludes an integer endpoint automatically. Near a floating-point cutoff, use the notebook's explicit per-order classification rather than trusting a rounded endpoint.
