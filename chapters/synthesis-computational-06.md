---
title: "Verify the complete beam-deflector geometry"
---

# Verify the complete beam-deflector geometry


The reference has six centered ridges per supercell, each with pitch $p=0.65\,\mu\mathrm m$, so $L=3.90\,\mu\mathrm m$. The wavelength is $1.55\,\mu\mathrm m$, with ridge/gap indices 2.4/1, incident index 1, substrate index 1.5, and normal TE incidence. All ridges within a sequence share one height.

The desired transmitted order $m=+1$ has

$$
\theta_{t,+1}=\arcsin\left(\frac{1.55}{1.5\times3.90}\right)
\approx15.36^\circ.
$$

Reflection supports $m=-2,\ldots,+2$, while transmission supports $m=-3,\ldots,+3$. Each channel receives its own complex coefficient and power normalization. This geometry and illumination differ from the six-post COMSOL example cited in Chapter 4.

For the full-wave model, the Chapter 3 TE Fourier equations are extended to all six coplanar rectangles. Their exact permittivity coefficients are

$$
\epsilon_\ell=n_g^2\delta_{\ell0}+
(n_r^2-n_g^2)\sum_j\frac{w_j}{L}
\operatorname{sinc}\left(\frac{\ell w_j}{L}\right)e^{-2\pi (-i)\ell x_j/L}.
$$

The complete Maxwell boundary problem is solved at the common top and bottom faces. All retained Fourier harmonics interact through this material matrix. Face-referenced decaying propagation factors avoid growing evanescent transfer factors.

For the local comparison, a staircase made from the individual cell coefficients gives estimated order powers $\operatorname{Re}(q_{t,m})|C_m|^2/q_{i,0}$, and an analogous reflected estimate. These are model predictions. Their total need not equal one, because the interfaces and differing neighbors were not solved collectively.

```{figure} ../assets/chapter-05/orders.png
:alt: Local staircase predictions and full-wave order powers for limited, expanded, identical, and reversed ridge sequences.

The local-cell design is tested against the full repeated geometry. Identical cells suppress nonzero supercell amplitudes; reversing a sequence reverses the order-power distribution.
```

The expanded design directs about **85.54% of incident power** into $m=+1$. Its total transmission is about 91.14%, so the desired order contains about **93.85% of transmitted power**. Report the denominator: these two percentages describe different observables. The local staircase estimate of target-order power is about 80.27%.

The original limited library gives about 38.62% incident-normalized power in $m=+1$ for its selected sequence. It is retained as an informative constrained design, not omitted because its performance is lower. Six identical ridges have zero nonzero-order amplitudes to numerical accuracy, even though those directions are allowed. Reversing the expanded sequence puts the dominant transmitted power in $m=-1$.

```{figure} ../assets/chapter-05/field.png
:alt: Real electric-field reconstruction across two repeated six-ridge supercells and the substrate.

Full-wave field reconstruction of an infinitely repeated TE supercell. Order-resolved modal powers, rather than the field image alone, establish the far-field fractions.
```

