# 8. Emerging applications in communications engineering

A surface can form a bright beam while delivering a disappointing communication link. The missing questions are how much power reaches the aperture, where the receiver is, how the direct path interferes, and how long the controller spends finding a useful state. This chapter turns those questions into an executable investigation.

Start after [wave and power conventions](02-waves-and-interfaces.md), [synthesis](05-metasurface-synthesis.md), and [tunable control](07-active-tunable.md). Use the [worked examples](08-communications-guide.md), [browser lab](../labs/08-communications-lab.md), and [executed notebook](../notebooks/08-communication-links.ipynb) together.

## 8.1 From a device to a system

By the end, you should be able to derive a coherent phase law from geometry, distinguish physical area from numerical sample count, construct a dimensionally consistent link budget, and evaluate a training-versus-rate tradeoff.

| Application | Useful objective | What must also be measured or modeled |
| --- | --- | --- |
| Coverage around an obstruction | Received power and outage at actual user locations | Direct-path blockage, aperture illumination, polarization and scattering |
| Near-field focusing | Power within a receiver region | Range as well as angle, motion and focal depth |
| Wideband beam control | Rate across occupied bandwidth | Dispersion, delays, frequency-dependent hardware and noise |
| Multiuser access | Sum rate, fairness or interference suppression | Joint channels, scheduler and transmit precoder |
| Joint sensing and communication | Communication rate plus localization accuracy | Echo geometry, ambiguity, noise and calibration |

The notebook executes the first three as restricted channel investigations and an idealized training experiment. Multiuser operation and sensing are extension outlines. A passive RF response can redirect incident energy; it does not supply RF amplification. Bias electronics can still consume DC power.

## 8.2 Draw the actual experiment

A square aperture lies in z = 0. Both nodes are in z > 0, so this is reflection. The transmitter is at (−10, 0, 20) m and the target at (8, 0, 12) m. The reference frequency is 28 GHz, aperture side 0.48 m, and assumed power efficiency 0.8. Transmit and receive gains are unity; transmit power is 10 dBm. The noise calculation uses 100 MHz, 290 K and a 7-dB receiver noise figure.

The 96 × 96 midpoint grid has 5-mm spacing. Its tiles discretize an aperture integral and a prescribed phase function. They are not 9,216 independently calibrated antennas. The small loaded-patch drawing is a possible physical realization only; no patch dimensions, substrate or bias circuit are solved here. A physical implementation requires Chapter 7’s state constraints and Chapter 6’s validation.

```{figure} ../assets/chapter-08/link-geometry.svg
:alt: Original geometry: transmitter, reflective aperture, receiver and optional direct path; enlarged aperture and conceptual loaded-patch inset.

Original geometry: transmitter, reflective aperture, receiver and optional direct path; enlarged aperture and conceptual loaded-patch inset.
```

## 8.3 A channel with explicit normalization

Use the book’s time convention $e^{-i\omega t}$, so an outgoing path contributes $e^{+ikr}$. For sample j, let $r_{tj}$ and $r_{rj}$ be the node-to-sample distances and let $c_{tj}=z_t/r_{tj}$ and $c_{rj}=z_r/r_{rj}$ be positive direction cosines. The declared scalar model is

$$
h_s(f)=\sum_{j=1}^{N}a_j\Gamma_j(f)e^{ik(r_{tj}+r_{rj})},\qquad a_j=\frac{\Delta A\sqrt{\eta G_tG_r c_{tj}c_{rj}}}{4\pi r_{tj}r_{rj}},\qquad |\Gamma_j|\leq1.
$$

The ratio of area to two distances makes each amplitude dimensionless. The factor $\eta$ is an assigned power loss, included once through its square root; $\Gamma_j$ is the additional normalized complex command. The separable cosine pattern is a **declared reciprocal aperture approximation**, not an exact vector-scattering formula for arbitrary reflection angles. Antenna gains are assumed constant over the aperture. Coupling, polarization conversion, edge currents, material dispersion and environmental multipath are omitted.

Why this scale? In the broadside far field, power intercepted by area A is approximately $P_tG_tA/(4\pi r_t^2)$. Assign aperture directivity $4\pi A/\lambda^2$, apply efficiency, propagate to the receiver, and multiply by its effective area $G_r\lambda^2/(4\pi)$. This gives

$$
\frac{P_r}{P_t}\simeq \frac{\eta G_tG_r A^2}{(4\pi)^2r_t^2r_r^2}=|h_s|^2\quad\text{(broadside, coherent far field).}
$$

The coherent sum recovers that limit. It does not prove an all-angle power balance in the Fresnel region. The implementation conservatively rejects nodes closer to the center than the larger of twice the side and ten wavelengths; this numerical guard is not a universal validity boundary. The reference nodes are well separated from individual samples, but not in the aperture’s asymptotic far field. Read [Özdogan, Björnson and Larsson](https://arxiv.org/abs/1911.03359) for a physical-optics far-field derivation with its own polarization and angular factors; do not substitute our cosine ansatz for that exact setup.

## 8.4 Derive the focusing phase

Write $d_j=r_{tj}+r_{rj}$. With positive $a_j$, the triangle inequality gives

$$
|h_s|\leq \sum_j a_j|\Gamma_j|\leq\sum_j a_j.
$$

Equality is possible with unit-magnitude commands when all terms share a phase. Hence

$$
\Gamma_j^\star(f_0)=e^{-ik_0d_j+i\phi_0},\qquad h_s(f_0)=e^{i\phi_0}\sum_j a_j.
$$

The global phase $\phi_0$ does not alter the isolated surface-path power, but it matters when another path is present. With realizable state magnitudes below one, optimize complex states; replacing them with phase-only unit coefficients overstates performance. The reference uses ideal continuous phase, a plane-wave approximation, and two-bit phase rounding. These are prescribed states, not measured hardware.

```{figure} ../assets/chapter-08/focus.png
:alt: Left: commanded aperture phase. Right: received-power gain along a receiver-plane cut for fixed spherical, plane and two-bit commands. All curves use one ideal-target reference.

Left: commanded aperture phase. Right: received-power gain along a receiver-plane cut for fixed spherical, plane and two-bit commands. All curves use one ideal-target reference.
```

## 8.5 Curvature, area and sample count

Let $\mathbf u_t$ and $\mathbf u_r$ point from the aperture center toward the nodes. Expanding distance about the center gives

$$
r_{\alpha j}=r_{\alpha0}-\mathbf u_\alpha\cdot\boldsymbol\rho_j+\frac{|\boldsymbol\rho_j|^2-(\mathbf u_\alpha\cdot\boldsymbol\rho_j)^2}{2r_{\alpha0}}+\mathcal O\!\left(\frac{|\boldsymbol\rho_j|^3}{r_{\alpha0}^2}\right),\qquad \alpha\in\{t,r\}.
$$

The plane law keeps only constant and linear terms. Its phase error includes curvature on **both** legs. The common $2D^2/\lambda$ guideline, with D the largest aperture dimension, is a scale to inspect, not an abrupt physical transition. For our square, taking D as the diagonal gives about 86 m, compared with node distances 22.36 and 14.42 m. The executed plane-law gain is only 0.596 of the spherical target gain.

At fixed area, $\Delta A=A/N$ decreases when N increases. At broadside with approximately equal distances,

$$
h_s\simeq N\frac{A}{N}\frac{\sqrt{\eta G_tG_r}}{4\pi r_t r_r}=\frac{A\sqrt{\eta G_tG_r}}{4\pi r_t r_r}.
$$

There is no gain from merely subdividing the same integral. If instead each physical cell retains its area while N increases, total area grows; far-field coherent power can then scale as $N^2$ over the regime where the assumptions hold. [Björnson and Sanguinetti](https://arxiv.org/abs/2002.04960) show why far-field scaling cannot be extrapolated to an arbitrarily large surface at fixed node positions. The notebook sweeps both mesh density and physical area so students can see the distinction.

## 8.6 Add the direct path as a field

A narrowband SISO baseband observation, with $\mathbb E|x|^2=1$, is

$$
y=\sqrt{P_t}(h_d+h_s)x+n,\qquad P_r=P_t|h_d+h_s|^2.
$$

For a constant direct amplitude b and focused surface amplitude a, reference phase to the direct path and expand the modulus:

$$
|b+ae^{i\phi}|^2=a^2+b^2+2ab\cos\phi,\qquad (a-b)^2\leq |h_d+h_s|^2\leq(a+b)^2.
$$

Adding powers would discard the cross term. It is justified only under an explicit incoherence/averaging assumption. The notebook uses a direct Friis amplitude with an assigned 10-dB excess power loss and sweeps a common phase offset. That loss is a teaching parameter, not a measured blockage model. The main focusing, bandwidth and training investigations omit the direct path so their comparisons remain interpretable.

```{figure} ../assets/chapter-08/power.png
:alt: Separate experiments: mesh refinement at fixed area, physical-area sweep, and coherent direct-path interference. The interference panel keeps the aperture and endpoints fixed.

Separate experiments: mesh refinement at fixed area, physical-area sweep, and coherent direct-path interference. The interference panel keeps the aperture and endpoints fixed.
```

## 8.7 Power, noise and rate

For a receiver at reference temperature T, bandwidth B and linear noise factor F,

$$
P_n=k_{\mathrm B}TBF,\qquad \gamma=\frac{P_t|h_d+h_s|^2}{P_n},\qquad R=B\log_2(1+\gamma).
$$

This is a single-user complex-AWGN capacity benchmark under perfect decoding/channel knowledge, flat response across B and ideal Gaussian signaling. It is not measured throughput: coding, modulation constraints, pilots, packet overhead, interference, channel variation and implementation losses change the result. The 100-MHz reference is narrow relative to the demonstrated multi-GHz gain variation; changing B without checking flatness is not valid.

Here the noise is −86.975 dBm, isolated surface-path gain −87.158 dB, received power −77.158 dBm and SNR 9.817 dB. The gross benchmark is 340.427 Mbps. Convert SNR to linear units before taking the logarithm. A 3-dB power increase roughly doubles rate only at low SNR; at high SNR it adds approximately one bit/s/Hz.

## 8.8 Finite states and uncertain phase

For M equally spaced ideal phases, nearest rounding gives error within $[-\pi/M,\pi/M]$. If errors are uniformly distributed, integrating $e^{i\epsilon}$ gives mean phasor $\operatorname{sinc}(1/M)$, using normalized sinc. Its square is a useful large-array benchmark, not an exact finite-layout law. Our two-bit finite aperture gives a target-power ratio of 0.810, close to $8/\pi^2$.

For independent Gaussian phase errors with standard deviation $\sigma$ in radians, expand the squared sum into diagonal and off-diagonal terms. Each cross term contains two independent errors; their characteristic functions multiply to $e^{-\sigma^2}$. Thus

$$
\mathbb E|h_s|^2=\sum_j a_j^2+e^{-\sigma^2}\left[\left(\sum_j a_j\right)^2-\sum_j a_j^2\right].
$$

At zero error, the coherent limit returns. At very large independent error, only the diagonal sum remains. Correlated errors behave differently: a common phase error changes the isolated path phase but not its magnitude. The notebook’s seeded Monte Carlo checks the mean, not reliability tails. Outage requires a distribution and a rate threshold.

## 8.9 Bandwidth and delay

Freeze the phase designed at $f_0$. At the target, a residual path phase proportional to frequency offset remains:

$$
h_s(f)=\sum_j a_j e^{i2\pi(f-f_0)d_j/c},\qquad \Delta\psi_{j\ell}=\frac{2\pi(f-f_0)(d_j-d_\ell)}{c}.
$$

A phase setting cancels path differences at one frequency. An ideal relative-delay law can cancel them throughout a band under our nondispersive-amplitude assumption. With this time convention, a delay contributes $e^{+i\omega\tau}$. Choose

$$
\tau_j=\frac{d_{\max}-d_j}{c}\geq0,\qquad e^{i2\pi f\tau_j}e^{i2\pi f d_j/c}=e^{i2\pi f d_{\max}/c}.
$$

The common phase is irrelevant to isolated received power. The ideal-delay curve is a benchmark; real delay hardware adds loss, dispersion and limits. [Yang et al.](https://arxiv.org/abs/2304.00440) study frequency-dependent near-field patterns and channel estimation in a substantially richer wideband system. Our notebook isolates the geometric mechanism; it does not reproduce their estimator.

```{figure} ../assets/chapter-08/bandwidth.png
:alt: Fixed-phase gain at the target and lateral beam displacement at 25, 28 and 31 GHz. The ideal-delay curve assumes frequency-independent weights and omits a direct path.

Fixed-phase gain at the target and lateral beam displacement at 25, 28 and 31 GHz. The ideal-delay curve assumes frequency-independent weights and omits a direct path.
```

## 8.10 Training consumes useful time

A beam is useful only after the system selects it. In the executed experiment, a user is at x = 8.37 m and z = 12 m. Search K focal points on x = 4–12 m, with one noiseless power observation per point; K = 1 uses x = 8 m. Choose the largest observed power. For a coherence block of $T_c$ symbols, charging K pilot symbols gives

$$
R_{\mathrm{net}}=\left(1-\frac{K}{T_c}\right)B\log_2(1+\gamma_{\mathrm{selected}}),\qquad 0\leq K\leq T_c.
$$

With $T_c=200$, the best **tested** net rate occurs at K = 17: 278.34 Mbps. K = 65 gives a higher gross rate but only 225.97 Mbps after training. This is neither a universal optimal K nor a channel-estimation algorithm. It assumes known candidate geometry, noiseless selection, no switching latency, and a constant channel throughout the block. Add those costs before claiming deployment performance.

```{figure} ../assets/chapter-08/training.png
:alt: Independent Gaussian phase-error mean with Monte Carlo uncertainty, and gross versus net rate for exhaustive noiseless beam selection.

Independent Gaussian phase-error mean with Monte Carlo uncertainty, and gross versus net rate for exhaustive noiseless beam selection.
```

## 8.11 Verification and next investigations

The numerical audit compares the coherent midpoint sum with adaptive continuous quadrature, checks an independent nested-loop off-target calculation, tests reciprocity, the broadside far-field scale, zero reflection, coherent bounds, sinc and Gaussian identities, noise/rate units and input guards. At 96 samples per side, the coherent amplitude differs from adaptive integration by about $1.46\times10^{-8}$ relative. That tiny integration error does not remove the much larger uncertainty of the chosen physical model.

For multiuser operation, replace the scalar objective with user channels and a transmit precoder. The received SINR contains interference from every simultaneously transmitted stream; maximizing one user’s field is not generally optimal for fairness or sum rate. For sensing, formulate a round-trip channel and delay/angle observable rather than interpreting a communication beam plot as localization accuracy. The [lab outlines](../labs/08-communications-lab.md) specify the missing implementation and acceptance evidence.

All figures and derivations here are original teaching material. The three primary papers linked beside the relevant discussion supply background and model comparisons; no paper figure, dataset or numerical performance claim is reproduced. Chapter 9 will connect these abstractions to materials, fabrication, calibration and measurement.
