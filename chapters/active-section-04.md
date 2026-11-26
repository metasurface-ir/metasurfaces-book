# 7.4 Reflecting surfaces and cascaded channels

Based on the instructor booklet, pages 185–190.

A passive RIS scatters the incident signal through programmable coefficients. A relay receives and retransmits and may add amplifier noise or incur a time-slot cost. In an independent-cell link model, each RIS term contains the two propagation factors and the cell response. In the far field of a fixed element the corresponding power scales with the inverse square of each leg. Separate joint base-station precoding, RIS programming, and the pilots required to estimate channel coefficients.

$$
h_{\rm eff}=h_d+\sum_n h_{rn}\Gamma_n h_{tn},\qquad y_p=\sum_n a_{pn}h_{rn}h_{tn}+w_p.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

Four cascaded coefficients are $1,i,-1,-i$. Compare all-on, continuous alignment, and a binary code with coefficients ±1.

:::{dropdown} Show the worked answer

All-on gives zero. Complex conjugate phases give a sum of 4 and power 16. The code $(1,1,-1,-1)$ gives $2+2i$ and power 8, about 3 dB down in this example. Four independent pilot patterns can recover four unknown products in the noiseless model.
:::
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
