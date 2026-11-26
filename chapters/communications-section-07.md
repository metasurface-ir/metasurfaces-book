# 8.7 Operational challenges, industry outlook, and integration into 6G

Instructor booklet, pages 236–242.

Reconfigurable intelligent surfaces (RIS/IRS) and holographic antennas (DMAs) are two routes to a **smart and programmable radio environment**. Moving from the laboratory to a network requires assessing hardware, channel estimation, control protocols, and deployment cost together.

## 8.7.1 Hardware bottlenecks and physical limits

**1. Mutual coupling.** Currents on neighboring cells interact in a dense surface. For example, a local effective model is $\Gamma_n=f(V_n,\{V_m\}_{m\in\mathcal N_n})$, with neighbor set $\mathcal N_n$. Adjusting adjacent cells can change the response of cell $n$. A diagonal matrix of independent coefficients misses this dependence. Multi-cell models and pattern calibration help beamforming.

**2. Phase–amplitude coupling.** Series resistance $R_s$, dielectric loss, and resonance in varactor- or PIN-loaded cells cause amplitude to vary with phase. An empirical fit is

$$
\Gamma_n(\theta_n)=\alpha_n(\theta_n)e^{i\theta_n},\qquad
\alpha_n(\theta_n)=(1-\alpha_{\min})\left[\frac{\sin(\theta_n-\theta_0)+1}{2}\right]^\gamma+\alpha_{\min}.
$$

Here $\alpha_{\min}$ is minimum amplitude, $\theta_0$ a fitted phase offset, and $\gamma>0$ a shape parameter. This form reaches its minimum at $\theta_0-\pi/2$. Calculate beamforming gain from the **sum of measured complex fields**.

**3. Spatial beam squint.** A common design sets a phase gradient at $f_0$ and holds it constant across the band. For normal incidence and target angle $\theta_0$,

$$
\sin\theta(f)=\frac{f_0}{f}\sin\theta_0.
$$

The gain toward the user can fall at band edges. **True time delay** (TTD) applies a phase difference proportional to frequency, $-2\pi f\Delta\tau$. Broadband elements with suitable phase slopes can approximate it.

## 8.7.2 Channel state acquisition and cascaded-channel overhead

A passive RIS has no on-surface receive RF chain or ADC. The receiver estimates the effective channel using pilots and changes of surface pattern. For an $M$-antenna station, a single-antenna user and an $N$-cell surface,

$$
\mathbf h_{\rm total}=\mathbf h_d+\mathbf h_r^H\mathbf\Phi\mathbf G,\qquad
\mathbf v=[\beta_1e^{i\theta_1},\ldots,\beta_Ne^{i\theta_N}]^T,\qquad
\mathbf\Phi=\operatorname{diag}(\mathbf v).
$$

Here $\mathbf h_d\in\mathbb C^{1\times M}$ is the direct channel, $\mathbf G\in\mathbb C^{N\times M}$ the station-to-surface channel, and $\mathbf h_r^H\in\mathbb C^{1\times N}$ the surface-to-user channel. Rearranging the diagonal product gives

$$
\mathbf H_{\rm cas}=\operatorname{diag}(\mathbf h_r^H)\mathbf G\in\mathbb C^{N\times M},\qquad
\mathbf h_{\rm total}=\mathbf h_d+\mathbf v^T\mathbf H_{\rm cas}.
$$

Unstructured estimation has $NM$ complex cascaded coefficients and $M$ direct ones. Three methods can reduce **pilot overhead**.

- **Element grouping.** Blocks share commands, reducing dimension at the cost of wavefront control.
- **Compressed sensing.** If a few directional paths dominate, a sparse model can use fewer samples. Rich scattering or mismatch can reduce its benefit.
- **Semi-passive or hybrid RIS.** Low-power RF detectors on a few cells provide local samples. Reconstructing the rest requires informative sampling and calibration.

## 8.7.3 Technical and economic comparison with relays and reflectors

| Criterion | Flat metal reflector | Amplify-and-forward relay (AF) | Decode-and-forward relay (DF) | Passive reconfigurable RIS |
| --- | --- | --- | --- | --- |
| Control | Fixed geometry | Active amplification | Signal regeneration | Software-controlled cell state |
| Circuit power | No control power | $10$ to $100\,\mathrm W$ in booklet examples | Over $50\,\mathrm W$ in high-power examples | Milliwatts to a few watts of control power in small examples |
| Noise | Loss and thermal environment | Amplified input noise and added receiver noise | Detection and fresh transmission with possible decoding errors | No active amplification of noise |
| RF circuitry | No RF chain | LNA and PA | Baseband processing and modulator | No mixer or RF amplifier in the passive type |
| Duplex and interference | Scattering in both directions | Half-duplex or full-duplex with leakage suppression | Buffer and scheduling depend on the architecture | Two-way reflection in reciprocal designs, with possible changes to interference paths |
| Path loss | Mirror law $(d_1+d_2)^{-2}$ in a large-aperture approximation | Two hop gains, noise, and relay gain | Reception on the first hop and fresh transmission on the second | $(d_1d_2)^{-2}$ in a simple far-field model with fixed effective aperture |
| Cost | Typically simple to fabricate | Active hardware and power supply | More processing and maintenance | Depends on aperture, control, installation, and calibration |

The power figures are illustrative. Compare geometry, aperture efficiency, bandwidth, and maintenance across options. In AF, signal power follows cascaded hops while relay noise enters the budget separately.

## 8.7.4 Network requirements and integration into 6G

**1. Signaling and timely updates.** Budget channel estimation, computation, command transmission, application, and settling. In a moving environment, FPGA or ASIC control may need delays of a few milliseconds or less. A cable or auxiliary wireless channel can carry commands.

**2. Open radio access network (Open RAN).** 3GPP and the ETSI ISG RIS provide contexts for study. In a candidate O-RAN design, xApps or rApps in the radio intelligent controller (RIC) can manage policies, pattern sets, and coordination. A learning algorithm can use user locations and traffic to select patterns. The fast local loop needs an actual latency budget.

**3. Self-sustainable RIS.** Flexible solar panels or RF energy harvesting can reduce wiring when average power and storage suffice. Compare controller, switching, interface, and idle power with harvestable energy at the location.

**Chapter synthesis.** RISs, metasurface antennas, lenses, space–time modulation, and ISAC all control fields at the surface or along the propagation path. Their benefit on a network depends on link budget, training and control overhead, and installation cost and power. The next problem evaluates these together for an industrial hall.

## Worked problem on deploying a RIS in an industrial hall

::::{admonition} Try it first
:class: book-exercise

Metal shelving weakens the direct paths to moving terminals. The operator must choose among a passive RIS, a metal reflector, and a relay. The center frequency is $28\,\mathrm{GHz}$ and the band spans $26$ to $30\,\mathrm{GHz}$. The station has $M=8$ antennas and the surface has $N=32\times32=1024$ cells with pitch $d=\lambda_0/2$. The test uses normal incidence and calls for a reflection angle of $45^\circ$ toward $+x$ in the $xz$ plane. Four contributions after removing the ideal geometric phase are $1$, $0.60$, $0.80e^{i30^\circ}$, and $0.60e^{-i30^\circ}$, compared with $1$ for each ideal contribution.

Coherence time is $2\,\mathrm{ms}$. Each pattern needs eight pilots of $1\,\mathrm{\mu s}$, and the estimate retains the direct path. After training, computation takes $0.20\,\mathrm{ms}$, command transmission $0.12\,\mathrm{ms}$, and panel settling $0.03\,\mathrm{ms}$. These stages are sequential and carry no useful data. The controller, drivers, and interface average $0.25\,\mathrm W$. Evaluate hardware loss, beam squint, update time, technology choice, and local energy supply.

```{dropdown} Show the full worked answer

### 1. Adding fields and calculating hardware loss

$$
E_{\rm real}=1+0.60+0.80e^{i30^\circ}+0.60e^{-i30^\circ}\simeq2.812+i0.100,
\qquad E_{\rm ideal}=4.
$$

$$
\frac{P_{\rm real}}{P_{\rm ideal}}=\frac{\lvert2.812+i0.100\rvert^2}{16}
\simeq0.495,\qquad L\simeq3.05\,\mathrm{dB}.
$$

Hypothetically align the phases without changing magnitudes. The sum is then $3$ and the loss $-10\log_{10}(9/16)\simeq2.50\,\mathrm{dB}$. This isolates amplitude loss. Real cells can couple amplitude and phase. The four measurements alone leave coupling undetermined. Hold one cell's command fixed, change its neighbors, and measure its response under identical illumination and reception. If it varies, use multi-cell pattern calibration or a coupled model. The $3.05\,\mathrm{dB}$ applies to **this block and pattern**.

### 2. Beam angle and power toward the user

$$
\Delta\phi_0=-k_0d\sin45^\circ=-\pi\sin45^\circ,\qquad
\sin\theta(f)=\frac{f_0}{f}\sin45^\circ.
$$

| Frequency | Beam angle from normal |
| --- | --- |
| $26\,\mathrm{GHz}$ | $49.6^\circ$ |
| $28\,\mathrm{GHz}$ | $45.0^\circ$ |
| $30\,\mathrm{GHz}$ | $41.3^\circ$ |

In the fixed user direction, sum the fields geometrically for $32$ equal-amplitude cells along $x$. Omit cell dispersion and coupling in this step.

$$
\delta=\pi(f/f_0-1)\sin45^\circ,\qquad
G_{\rm rel}=\left\lvert\frac{\sin(32\delta/2)}{32\sin(\delta/2)}\right\rvert^2
\simeq0.050.
$$

At each edge this is about $13\,\mathrm{dB}$ loss toward the user. Adding it to the four-cell loss requires a joint model. Use a true time delay to hold the direction fixed.

$$
\Delta\tau=\frac{d\sin45^\circ}{c}=\frac{\sin45^\circ}{2f_0}\simeq12.6\,\mathrm{ps},\qquad
\Delta\phi(f)=-2\pi f\Delta\tau.
$$

Compare TTD cost and loss with reducing operating bandwidth or coherent aperture size.

### 3. Training and control budget

Eight orthogonal pilots per pattern resolve the effective channel from the eight antennas. In the unstructured diagonal model, separating the direct path and $N$ reflected terms requires at least $N+1$ patterns. The pattern matrix with the constant direct-path column must have full rank.

| Option | Patterns including direct path | Pilots | Training time |
| --- | --- | --- | --- |
| $1024$ independent cells | $1025$ | $8200$ | $8.20\,\mathrm{ms}$ |
| $64$ groups of $4\times4$ cells | $65$ | $520$ | $0.52\,\mathrm{ms}$ |

Independent training exceeds four coherence intervals. For the grouped surface,

$$
T_{\rm loop}=0.52+0.20+0.12+0.03=0.87\,\mathrm{ms},\qquad
T_{\rm data}=2.00-0.87=1.13\,\mathrm{ms}.
$$

Data gets $56.5\%$ of the interval. Grouping estimates only each block's effective response. An uncompensated phase slope within a block can weaken a tilted beam. Sparse estimation with dominant paths and sensing RIS with local samples are options. The former depends on model fit and the latter on calibration and sensor count. Validate the grouped model with measured patterns under strong coupling.

### 4. Choosing a technology using net rate

The service threshold is $0.60\,\mathrm{Gbit/s}$. In the assumed trial, useful rates are $0.30$ for the reflector, $0.70$ for AF, and $0.80\,\mathrm{Gbit/s}$ for DF. RIS rate during the data interval, after hardware and bandwidth effects, is $1.20\,\mathrm{Gbit/s}$ before timing overhead.

$$
R_{\rm RIS,net}=1.20(0.565)=0.678\,\mathrm{Gbit/s}.
$$

| Option | Result in the hall | Consideration |
| --- | --- | --- |
| Fixed reflector | Below threshold | Simple and no control power. Reassess for fixed routes |
| AF | Passes threshold | Amplifies noise and needs RF chains and power |
| DF | Highest trial rate | Regeneration after decoding, with processing cost, delay, and error risk |
| Grouped RIS | Margin of $0.078\,\mathrm{Gbit/s}$ | Depends on reflection path, timely updates, and calibration |

The RIS merits a field trial. If coherence drops to $1.5\,\mathrm{ms}$ with unchanged $0.87\,\mathrm{ms}$ overhead, its rate falls to $1.20(1-0.87/1.5)=0.504\,\mathrm{Gbit/s}$, below the service threshold. Compare rate, coverage stability, installation, energy, and maintenance. A passive surface can also change self-interference paths of active equipment.

### 5. Network integration and energy budget

**Control.** Select and apply fast patterns at the surface or near the base station. A slower Open RAN layer can manage policies, pattern libraries, and panel coordination. Record settling time as well as transmission time. Provide a fallback pattern for loss of the control link. This division is a candidate architecture for the example.

**Energy.** Daily load, harvested RF power, and solar energy for the assumed data are

$$
E_{\rm load}=0.25\times24=6\,\mathrm{Wh/day},\qquad
P_{\rm RF,DC}=0.40(0.10\,\mathrm{mW})=0.04\,\mathrm{mW}.
$$

RF input is $\mathord{-10}\,\mathrm{dBm}=0.10\,\mathrm{mW}$. Harvested power is a factor of $6250$ below demand. A $1\,\mathrm W$ solar panel with four equivalent sun-hours and $80\%$ efficiency gives $3.2\,\mathrm{Wh/day}$. Minimum panel rating before low-light margin is

$$
P_{\rm panel,min}=\frac{6}{4(0.8)}=1.875\,\mathrm W.
$$

A battery shifts available energy to nighttime. The average daily shortfall remains. **Takeaway.** Test deployment readiness against wideband user-direction gain, update time, net rate, and available energy together.
```
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
