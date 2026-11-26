# Active, tunable and intelligent metasurfaces

## 7.1 Why move beyond a static surface?

Based on the instructor booklet, pages 174–175.

An etched pattern can shape multiple beams, but its response is fixed once fabricated. A tunable surface changes an operating parameter, a reconfigurable surface switches spatial patterns, and an adaptive surface uses observations to choose a pattern. An RF active cell can supply signal gain and requires a separate power and noise budget. A biased switch can remain RF passive.

$$
\Gamma(x,y;\mathbf u)=A(x,y;\mathbf u)e^{i\phi(x,y;\mathbf u)}.
$$

## 7.2 Actuation mechanisms

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

## 7.3 Digital states, coding and hardware

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

## 7.4 Reflecting surfaces and cascaded channels

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

## 7.5 Time variation and frequency channels

Based on the instructor booklet, pages 190–195.

If a boundary coefficient changes during an RF cycle, the field and coefficient multiply in time and convolve in frequency. A traveling modulation also supplies tangential momentum. Compare the exchanged input and output modes with the pump unchanged when testing nonreciprocity. A conversion path alone establishes neither isolation over a band nor gain. Count pump power and other propagating modes.

$$
\Gamma(x,t)=\sum_m a_m e^{im(\Omega t-Kx)},\quad \omega_m=\omega_0+m\Omega,\quad k_{x,m}=k_{x,0}+mK.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

A 10 GHz input has $k_x=0.6k_0$. Use $f_m=100$ MHz and $K=0.6k_0$. Find the lower sideband direction and the transverse momentum of the opposite-frequency order under the same pump at normal incidence.

:::{dropdown} Show the worked answer

For $m=-1$, the output is 9.9 GHz with $k_x=0$. Starting at 9.9 GHz and $k_x=0$, the $m=+1$ order at 10 GHz has $k_x=+0.6k_0$. The spatially reversed version of the original input would have $-0.6k_0$. A physical comparison also specifies polarization, normalization and leakage paths.
:::
::::

## 7.6 Sensing, decisions and adaptation

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

## 7.7 Research directions and deployment limits

Based on the instructor booklet, pages 199–202.

Hybrid sensing and reflecting surfaces trade aperture area and power for better observability. In-wave analog processing uses the physical scattering operator, whose useful bandwidth and repeatability require measurement. Large apertures bring near-field focusing, time modulation can shift some transmitter functions onto the surface, and energy harvesting must be tested against the full controller budget. For each proposal compare calibration, wiring, switching, loss, thermal drift and robustness to unseen conditions.

$$
R_{\rm F}\simeq 2D^2/\lambda,\qquad P_{\rm dc}=\eta_{\rm rect}P_{\rm RF,in}.
$$
