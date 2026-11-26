# 7.2 Actuation mechanisms

Based on the instructor booklet, pages 175–181.

A PIN diode switches between two impedances. A reverse-biased varactor changes capacitance continuously, but its series loss and package inductance limit the available phase range. Liquid crystal changes its effective permittivity through molecular alignment. VO₂ undergoes a conductivity transition, whereas GST can retain a programmed phase without continuous holding power. Graphene gating moves the chemical potential and is relevant at terahertz and optical frequencies. Compare usable phase swing, loss, switching and settling time, array drive power, and required state retention at the intended frequency.

$$
C_v=C_0(1+V_R/V_j)^{-m},\qquad Q_v\simeq(\omega C_vR_s)^{-1},\qquad |\mu_c|\propto\sqrt{|V_g-V_D|}.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

At 10 GHz, a 32-by-32 panel uses 7.5 mm pitch. Estimate phase steps for steering to +30° and −45°, and DC power if every PIN draws 5 mA from 3.3 V. For a 1 pF varactor with $V_j=1$ V, $m=1/2$, and $R_s=1\,\Omega$, calculate capacitance and Q at 3 V.

:::{dropdown} Show the worked answer

For normal incidence, $\Delta\phi=-k_0d\sin\theta$, giving approximately $-45^\circ$ and $+63.6^\circ$. The all-on DC estimate is $1024(3.3)(0.005)=16.9$ W before driver overhead. The varactor gives 0.50 pF and $Q\simeq31.8$. Neither value determines the full cell phase range or full panel settling time.
:::
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
