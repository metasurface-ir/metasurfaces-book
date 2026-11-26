# 8.7 Hardware, training cost and network integration

Based on the instructor booklet, pages 236–242.

Real state phases and amplitudes are coupled. Wideband steering can squint, a large cascade can take too long to estimate, and stale control commands can erase the gain. Compare passive, active and hybrid surfaces at equal coverage and available time, including noise, control traffic, installation and maintenance. Treat network integration as an engineering and interoperability question whose requirements should be checked for the intended system.

$$
\Gamma_n=\alpha_n(\theta_n)e^{i\theta_n},\qquad \tau_{\rm data}=\max(0,T_c-\tau_{\rm train}-\tau_{\rm ctrl}).
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

If training and control consume 1.13 ms in a 2 ms coherence interval, how much remains? What is DC output from −10 dBm of harvested RF at 40% conversion?

:::{dropdown} Show the worked answer

There are 0.87 ms left, or 43.5%. The incident RF power is 0.10 mW, so the harvested DC is 0.04 mW before downstream losses. Compare it with the complete duty-cycle-dependent budget.
:::
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
