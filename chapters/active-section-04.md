# 7.4 Reconfigurable intelligent surfaces (RIS / IRS) in sixth-generation communications

Instructor booklet, pages 185–190.

Networks beyond fifth-generation and toward sixth-generation communications are an important driver of metasurfaces moving from physics laboratories into industry and standards. At millimetre-wave and sub-terahertz frequencies, signals experience severe path attenuation and blockage of line of sight by environmental obstacles.

In the classical approach, only the transmitter and receiver were optimized. Wireless propagation was considered random and uncontrollable. Reconfigurable intelligent surfaces (RIS), also called intelligent reflecting surfaces (IRS), change that paradigm and open the possibility of a programmable smart radio environment (SRE).

## 7.4.1 Operation and differences from conventional radio relays

A RIS is a two-dimensional array of digitally controlled subwavelength cells. By controlling incident waves' phase and amplitude it can create a virtual line of sight between the transmitter and receiver.

| Feature | Conventional active relay (AF or DF) | Passive reflecting surface (RIS / IRS) |
| --- | --- | --- |
| Amplification and RF chains | Active receiving and transmitting chains and a power amplifier, sized for the architecture | No RF amplifier or power-hungry transmit chain |
| Power consumption | Tens to hundreds of watts in the booklet's examples | Lower, on the order of milliwatts for control and bias in low-power examples |
| Thermal noise | AF can amplify incoming noise and add its own noise. | Does not regenerate or amplify the signal. Loss and system noise still matter. |
| Duplexing | Frequency or time separation, or self-interference cancellation | Simultaneous scattering without an active transmitter on the sheet. System interference remains possible. |
| Hardware cost | Often higher due to the active chains | Potentially economical for deployment at scale, depending on count, control, and installation |

The table describes the booklet's comparison for a passive RIS. Power draw, cost, and duplex operation depend on the implementation.

## 7.4.2 Cascaded channel and path-loss model

With $K_t$ transmit antennas, $K_r$ receive antennas, and $N$ reflecting cells, the received signal along the surface path is modeled as

$$
\mathbf y=\mathbf H_r\Phi\mathbf H_t\mathbf x+\mathbf n.
$$

- $\mathbf x$ is the transmitted signal with total power $P_t$.
- $\mathbf H_t\in\mathbb C^{N\times K_t}$ is the transmitter-to-RIS channel.
- $\mathbf H_r\in\mathbb C^{K_r\times N}$ is the RIS-to-receiver channel. With one receive antenna write it as $\mathbf h_r^H$.
- $\mathbf n\sim\mathcal{CN}(\mathbf 0,\sigma^2 I_{K_r})$ is additive white Gaussian noise.
- $\Phi$ is the diagonal matrix of surface response coefficients:

$$
\Phi=\operatorname{diag}(\beta_1 e^{i\theta_1},\beta_2 e^{i\theta_2},\ldots,\beta_N e^{i\theta_N}).
$$

Here $\beta_n\in[0,1]$ is reflection amplitude (ideally approximately one) and $\theta_n\in[0,2\pi)$ is the phase the $n$th cell applies. The receiver matrix dimensions and diagonal separators have been made consistent with these definitions.

### Cascaded path loss (the fourth-power distance law)

If the transmitter is distance $d_1$ from the RIS and the receiver is distance $d_2$, the simple far-field passive-element model with approximately common distances gives the product of the two path losses and the coherent element sum:

$$
P_r\propto P_t G_tG_rG_{\rm cell}^2
\frac{\lambda^4}{(4\pi)^4d_1^2d_2^2}
\left|\sum_{n=1}^{N}\beta_n e^{i(\theta_n-\psi_n)}\right|^2,
\qquad
\psi_n=k_0(d_{1,n}+d_{2,n}).
$$

$\psi_n$ is the phase delay from propagation. Setting $\theta_n=\psi_n$ aligns the reflected signals constructively at the receiver. With identical unit contributions the squared sum becomes $N^2$:

$$
P_{r,\mathrm{opt}}\propto\frac{N^2}{d_1^2d_2^2}.
$$

The factor $N^2$ means that enlarging the array and adding equal contributions can partly compensate for two-hop path loss. Merely subdividing a fixed area does not hold the contribution of each cell constant.

## 7.4.3 Joint active and passive beamforming

The objective in a RIS-assisted system can be maximizing data rate, Shannon capacity, or signal-to-interference-plus-noise ratio (SINR). For a single-antenna user without interference, a joint optimization is

$$
\begin{aligned}
\max_{\mathbf w,\Phi}\quad&
\log_2\!\left(1+\frac{|\mathbf h_r^H\Phi\mathbf H_t\mathbf w|^2}{\sigma^2}\right)\\
\text{s.t.}\quad& \|\mathbf w\|^2\le P_t,\quad |\Phi_{nn}|\le1,\quad \theta_n\in\mathcal F.
\end{aligned}
$$

$\mathbf w$ is the transmitter's active precoding vector. $\Phi$ is the passive phase configuration. $\mathcal F$ is the allowed set, continuous over $[0,2\pi)$ or discrete, for example $\{0,\pi\}$ for one-bit coding.

Coupling between $\mathbf w$ and $\Phi$ and the cell constraints make the problem nonconvex. Common approaches include:

1. **Alternating optimization (AO).** Hold one variable fixed while optimizing the other, then iterate.
2. **Semidefinite relaxation (SDR).** Lift the phases to a rank-one matrix and relax the rank constraint in a semidefinite program.
3. **Deep reinforcement learning (DRL).** Use channel state information (CSI) to select a useful phase configuration.

## 7.4.4 Channel-estimation challenges in RIS

A primary technical bottleneck is obtaining the cascaded channel $\mathbf h_r^H\Phi\mathbf H_t$. Passive cells cannot independently send pilots or process observations locally. Approaches include:

1. **Semi-passive RIS.** Equip a small fraction of cells with sensors and readout circuits to obtain channel observations at the surface.
2. **Time-coded pilots.** Change patterns or turn cell blocks on and off in distinct time slots to separate channel components.
3. **Compressed sensing.** If the angular channel at millimetre-wave frequencies is sparse, exploit that structure to reduce the number of measurements.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

In a building corridor, a wall blocks the direct path from a base station to a user. A passive RIS is mounted on a side wall visible from both ends. The transmitter-to-RIS distance is $d_1=10\,\mathrm m$, and the RIS-to-receiver distance is $d_2=15\,\mathrm m$.

Begin with one transmit and one receive antenna and model the surface as four independent reflecting blocks, each of which can represent a group of cells. Before applying the RIS phases, their complex cascaded channel coefficients are

$$
\mathbf c=a[1,-i,-1,i]^{\mathsf T},\qquad a>0.
$$

All reflection magnitudes are one. At full transmit power $P_t$, a single block delivers $-90\,\mathrm{dBm}$ and the receiver noise power is also $-90\,\mathrm{dBm}$. Ignore the direct path and other transmitters' interference.

1. How does the RIS create an alternative path? How does it differ from an active relay?
2. Find the optimum continuous and one-bit RIS phases. Compare received power, SNR, and spectral efficiency.
3. If the RIS-to-user distance doubles, how does power change? Under what assumptions does the $N^2$ law hold?
4. With two transmit antennas, how do we jointly adjust transmitter and RIS beamforming?
5. If $\mathbf c$ is unknown, how can we estimate it from pilots without the RIS transmitting a pilot itself?

```{dropdown} Show the full worked answer

### 1. Creating an alternative path: the RIS does not generate a new signal

The transmitter illuminates the RIS, which aligns the reflected contributions at the user. The link follows transmitter, RIS, and receiver, so the wave need not cross the blocking wall.

An AF relay amplifies and retransmits the received signal and may amplify incoming noise. A DF relay decodes the data and retransmits it. The passive RIS in this problem uses neither an RF amplifier nor a data decoder. It consumes control and bias power, but the reflected wave takes its energy from the incident wave. Constructive addition concentrates some of that power toward the user.

### 2. Phase alignment: adding amplitudes versus adding powers

With block reflection coefficient $v_n=e^{i\theta_n}$, the single-antenna link is

$$
y=h_{\rm eff}x+\eta,\qquad
h_{\rm eff}=\sum_{n=1}^4 c_n v_n,\qquad
\mathrm{SNR}=\frac{P_t|h_{\rm eff}|^2}{\sigma^2}.
$$

Single-block power equals noise power, so $P_ta^2/\sigma^2=1$. It suffices to calculate $|h_{\rm eff}/a|^2$.

**First case: all RIS phases zero.** Then $h_{\rm eff}=a(1-i-1+i)=0$. Visibility of the two legs alone does not guarantee a useful link. The four ideal contributions cancel at the receiver.

**Second case: continuous phase control.** Choose each block phase to cancel the phase of its channel:

$$
\boldsymbol\theta^\star=[0^\circ,90^\circ,180^\circ,270^\circ].
$$

Each product $c_nv_n$ is $a$. Amplitude is four times and power sixteen times the single-block values:

$$
h_{\rm eff}=4a,\qquad \mathrm{SNR}=16,\qquad
P_r=-90+10\log_{10}(16)\simeq-77.96\,\mathrm{dBm}.
$$

**Third case: one-bit control with $0^\circ$ and $180^\circ$.** We can flip signs but cannot rotate imaginary contributions onto the real axis. With $\boldsymbol\theta_{\rm 1bit}=[0^\circ,180^\circ,180^\circ,0^\circ]$,

$$
h_{\rm eff}=a(1+i+1+i)=a(2+2i),\qquad |h_{\rm eff}|^2=8a^2.
$$

This choice is optimal. The real pair can supply at most $2a$ along the real axis and the imaginary pair at most $2a$ along the imaginary axis. Power cannot exceed $(2a)^2+(2a)^2=8a^2$.

Using Shannon's $R=\log_2(1+\mathrm{SNR})$ with linear SNR:

| Configuration | Received power | Linear SNR | Ideal spectral efficiency (bit/s/Hz) |
| --- | --- | --- | --- |
| One block, reference | $-90\,\mathrm{dBm}$ | 1 | 1.00 |
| Four blocks, optimal one-bit phases | $-80.97\,\mathrm{dBm}$ | 8 | 3.17 |
| Four blocks, optimal continuous phases | $-77.96\,\mathrm{dBm}$ | 16 | 4.09 |

One-bit control costs approximately $3\,\mathrm{dB}$ relative to continuous phases in this example. This penalty depends on the channel phases and is not a universal value for one-bit RIS.

### 3. Cascaded path loss and the scope of the $N^2$ law

In the simple far-field model, hold directional gains fixed and retune RIS phases after the user moves:

$$
P_r\propto\frac{1}{d_1^2d_2^2},\qquad
\frac{P_{r,\rm new}}{P_{r,\rm old}}=\left(\frac{15}{30}\right)^2=\frac14.
$$

Received power drops about $6.02\,\mathrm{dB}$, to roughly $-83.98\,\mathrm{dBm}$ for continuous phases. Doubling **both** distances gives $1/16$ of the power, a $12.04\,\mathrm{dB}$ decrease. The fourth power comes from scaling both legs by the same factor.

$N$ equal-amplitude, in-phase contributions produce amplitude proportional to $N$ and power proportional to $N^2$. Subdividing a fixed-area sheet does not keep individual contributions fixed. Calculate each block separately in the near field or with uneven illumination.

### 4. Joint beamforming: what do the transmitter and RIS do?

Keep one receive antenna and use two transmit antennas. For a fixed RIS pattern, suppose the effective two-antenna channel is

$$
\mathbf g=\mathbf h_r^H\Phi\mathbf H_t=a[4,\ 2i].
$$

$\mathbf g$ is a row vector. The transmitter chooses $\mathbf w$ to maximize $|\mathbf g\mathbf w|^2$ subject to $\|\mathbf w\|^2\le P_t$. The single-user maximum-ratio transmission (MRT) solution is

$$
\mathbf w^\star=\sqrt{P_t}\frac{\mathbf g^H}{\|\mathbf g\|}
=\sqrt{\frac{P_t}{20}}\begin{bmatrix}4\\-2i\end{bmatrix}.
$$

The $-i$ in the second weight cancels the $+i$ phase of its channel, so the contributions align. Linear SNR is 20, compared with 16 from the first antenna alone at the same total power and with the same RIS pattern.

Changing $\mathbf w$ changes the illumination of the blocks. A practical approach is alternating optimization:

1. Hold the RIS fixed and update $\mathbf w$ for the effective channel.
2. Hold $\mathbf w$ fixed and align the RIS blocks. The four-block binary example permits enumeration of all $2^4=16$ patterns.
3. Repeat until improvement is small.

Optimizing each step with the other variable fixed does not guarantee a global optimum. Large arrays make exhaustive enumeration impractical. Approximations such as semidefinite relaxation or learning-based methods can be used.

### 5. Channel estimation: four pilots, four unknowns

A passive RIS cannot generate an RF pilot. The **transmitter sends a known pilot**, and the RIS changes only its reflection pattern. Assume the channel is constant over four slots. In the original single-antenna model, divide the received observations by the known pilot:

$$
\mathbf z=B\mathbf c+\boldsymbol\nu,\qquad
B=\begin{bmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{bmatrix}.
$$

Each row is one RIS pattern, with signs representing $0^\circ$ and $180^\circ$. Isolating the block contributions does not require turning each block off. The columns are orthogonal and $B^{\mathsf T}B=4I$. The least-squares estimate and noiseless observations are

$$
\widehat{\mathbf c}=\frac14B^{\mathsf T}\mathbf z,\qquad
\frac{\mathbf z}{a}=[0,\ 2-2i,\ 0,\ 2+2i]^{\mathsf T}.
$$

Substitution recovers $\mathbf c/a=[1,-i,-1,i]^{\mathsf T}$. The first observation alone was insufficient. All-zero phases give zero output because the block contributions cancel.

The method estimates **cascaded coefficients**, without necessarily separating transmitter-to-RIS and RIS-to-receiver channels. Many pilots can consume a substantial fraction of coherence time. Grouping cells trades control resolution for fewer unknowns. Compressed sensing can reduce measurements in angularly sparse channels, and a semi-passive RIS can collect information through embedded sensors.

**Summary.** Geometry determined how much power reached the surface and receiver. Channel estimation determined the phase of each contribution. Joint transmitter and RIS control determined whether those contributions reinforced or canceled one another.
```
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
