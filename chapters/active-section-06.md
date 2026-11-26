# 7.6 Sensing, decisions and adaptation

Based on the instructor booklet, pages 195–199.

Place a few coherent sensing elements in the aperture to measure phase differences. A controller estimates a state, chooses a code, applies it and tests the new response. A lookup table, a trained predictor, or exploration of candidate codes can implement the decision. For a small discrete codebook, measure reward against a fixed baseline and report lost data time during exploration. Power-only sensing cannot by itself provide the signed relative phase.

$$
\Delta\arg E=-k_0d\sin\theta,\qquad \tau_{\rm loop}=\tau_{\rm sense}+\tau_{\rm decide}+\tau_{\rm write}+\tau_{\rm settle}.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

With coherent probes separated by $\lambda/2$, the downstream phase is $-60^\circ$ relative to the upstream probe. Estimate angle and state what further latency matters if probes are sampled periodically.

:::{dropdown} Show the worked answer

$\sin\theta=1/3$, so the principal angle is about 19.5°. Up to one sampling interval may elapse before the loop sees a change. The total reaction time must fit the channel dynamics.
:::
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
