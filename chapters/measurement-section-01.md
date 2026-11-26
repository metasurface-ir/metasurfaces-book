# 9.1 Materials and substrate response

Based on the instructor booklet, pages 244–248.

At microwave frequencies good conductors are often characterized by conductivity and skin depth. At optical frequencies carriers have inertia and bound charges can resonate, so use a dispersive Drude–Lorentz description. Dielectric loss, conductor loss and radiation contribute to the resonator linewidth. Compare substrates at the same frequency and field filling factor. A phase-change film, graphene sheet or electro-optic material can trade tunability against insertion loss and control complexity.

$$
\epsilon_r=\epsilon_\infty-\frac{\omega_p^2}{\omega^2-i\gamma\omega}+\sum_j\frac{f_j\omega_{0j}^2}{\omega_{0j}^2-\omega^2+i\Gamma_j\omega},\quad Q_d\approx\frac1{p_e\tan\delta}.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

A thermal film has conductivity rising from 10 to $10^5$ S/m with a logistic transition centered at $T_c$ and width scale $\Delta T$. Find the midpoint conductivity and the 10–90% temperature interval.

:::{dropdown} Show the worked answer

At the midpoint $\sigma=50005$ S/m. Solving $p=(1+e^{-(T-T_c)/\Delta T})^{-1}$ gives $T_{10,90}=T_c\mp\Delta T\ln9$. Hysteresis and thermal settling would require additional measurements.
:::
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
