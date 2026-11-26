# 9.5 Retrieving effective parameters

Based on the instructor booklet, pages 265–270.

Choose the model before inversion. A symmetric homogeneous slab supports impedance and index retrieval, a ground-backed one-port supports an input surface impedance, and a symmetric electric sheet supports shunt admittance. Shift reference planes first. For slab retrieval use phase continuity and physical checks to choose the logarithm branch, then reconstruct both measured coefficients. A very small transmission, uncertain sample thickness or calibration drift can magnify uncertainty.

$$
z^2=\frac{(1+r)^2-t^2}{(1-r)^2-t^2},\quad n_m=\frac{-\arg T+2\pi m+i\ln|T|}{k_0d},\quad Z_s=\eta\frac{1+r}{1-r},\quad Y_s=\frac2\eta(1/t-1).
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

An internal slab factor has magnitude 0.90 and phase $+120^\circ$ at $d=\lambda_0/3$. Calculate the principal index and neighboring branch spacing.

:::{dropdown} Show the worked answer

$k_0d=2\pi/3$, so $n_0=-1+i\ln(0.90)/(2\pi/3)\simeq-1-i0.0503$. The real spacing is 3. Attenuation fixes the imaginary part for the assumed propagation model, while one frequency alone cannot distinguish the real branches.
:::
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
