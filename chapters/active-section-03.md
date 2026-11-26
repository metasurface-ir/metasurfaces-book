# 7.3 Digital states, coding and hardware

Based on the instructor booklet, pages 181–185.

With b bits the ideal equally spaced phase codebook has $2^b$ states. The aperture sum uses the calibrated complex reflection of each cell. Periodic alternating states generate diffraction orders, a phase ramp shifts the dominant beam, and a balanced irregular code can cancel the broadside sum. Cancellation in one direction redistributes power and must be distinguished from absorption. An FPGA can load a code through serial-to-parallel shift registers and latch rows together. Include update time and switching transients in the budget.

$$
F(u,v)=\sum_{m,n}\Gamma_{mn}e^{ik_0d(mu+nv)},\qquad \phi_q=2\pi q/2^b.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

An 8-by-8 array with $d=\lambda/2$ uses a $+90^\circ$ phase increment per column. Where is the main beam? What happens to the normal sum with 32 coefficients at +1 and 32 at −1?

:::{dropdown} Show the worked answer

The phase per column is $\pi/2+\pi u$. The visible peak is at $u=-1/2$, or $-30^\circ$ in the steering cut. At normal observation all propagation factors equal one, so the balanced sum is zero. The off-axis pattern depends on where the signs are placed.
:::
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
