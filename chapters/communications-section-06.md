# 8.6 Sensing, precision localization, and integrated sensing and communications (ISAC)

Instructor booklet, pages 230–236.

## 8.6.1 Integrating sensing and communications

Radar uses pulses or frequency-modulated continuous waves (FMCW) to estimate delay, angle, and Doppler. Wireless links value throughput and bit error rate (BER), for example with OFDM. In millimeter-wave and sub-terahertz bands, spectrum is valuable and short wavelength improves angular resolution for a given aperture. Bandwidth sets delay resolution.

**Integrated sensing and communications** (ISAC) shares resources. A waveform good for throughput can have substantial correlation sidelobes. This **trade-off** extends beyond waveform and timing. A RIS or holographic DMA can shape communication beams and sensing patterns, with shared power and degrees of freedom.

## 8.6.2 RIS-aided angle estimation and localization

**Array steering and reception.** A RIS can act as a known **anchor** in a non-line-of-sight (NLoS) path. Take a uniform planar array (UPA) in the $xy$ plane with $M=M_xM_y$ cells and $d_x=d_y=\lambda/2$. Here $\theta_t$ is measured from the positive normal and $\phi_t$ from $+x$.

$$
\mu_x=\frac{2\pi d_x}{\lambda}\sin\theta_t\cos\phi_t,\qquad
\mu_y=\frac{2\pi d_y}{\lambda}\sin\theta_t\sin\phi_t.
$$

For a cell ordering consistent with the Kronecker product $\otimes$, the steering vector is

$$
\mathbf a=\mathbf a_x\otimes\mathbf a_y\in\mathbb C^{M\times1},\qquad
\mathbf a_x=[1,e^{-i\mu_x},\ldots,e^{-i(M_x-1)\mu_x}]^T,\quad
\mathbf a_y=[1,e^{-i\mu_y},\ldots,e^{-i(M_y-1)\mu_y}]^T.
$$

A single RIS crossing can be written as $\mathbf H_{\rm out}\mathbf\Phi\mathbf H_{\rm in}$. An echo with two crossings uses a RIS matrix and corresponding channels for each pass. With $\mathbf H_{\rm path}$ denoting the full path response,

$$
y(t)=\alpha\,\mathbf w^H\mathbf H_{\rm path}\mathbf f\,s(t-\tau)e^{i2\pi f_dt}+n(t),
\qquad
\mathbf\Phi=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_M}).
$$

Here $\mathbf f$ and $\mathbf w$ are transmit and receive weights. The complex $\alpha$ represents target scattering and path factors omitted from $\mathbf H_{\rm path}$. Radar cross section (RCS) is a power-domain quantity. Delay $\tau$ comes from the **total path**. For a simple monostatic case, $\tau=2R/c$ and $f_d=2v\cos\psi/\lambda$, with positive sign for approach. The noise model is $n(t)\sim\mathcal{CN}(0,\sigma^2)$.

**Cramér–Rao lower bound (CRLB).** For angle of arrival (AoA), let $\boldsymbol\theta=[\theta_t,\phi_t]^T$ and let $\boldsymbol\mu_k$ be the complex sample mean. With independent noise and real parameters, the Fisher information matrix (FIM) and unbiased-estimator bound are

$$
\mathbf J_F=\frac{2}{\sigma^2}\operatorname{Re}\sum_{k=1}^K
\left(\frac{\partial\boldsymbol\mu_k}{\partial\boldsymbol\theta}\right)^H
\left(\frac{\partial\boldsymbol\mu_k}{\partial\boldsymbol\theta}\right),\qquad
\operatorname{Cov}(\widehat{\boldsymbol\theta})\succeq\mathbf J_F^{-1}.
$$

Include other unknown parameters in the information matrix and take the corresponding block of its inverse. In the ideal coherent two-pass model, echo amplitude can scale as $M^2$ and power as $M^4$. **Angular information** also depends on pattern derivatives, aperture, and the noise model. Receive SNR already includes path gain.

## 8.6.3 Computational imaging with a dynamic metasurface

**Compressed sensing.** In synthetic aperture radar (SAR), aperture motion provides spatial samples. A programmable metasurface can instead use different phase or amplitude patterns with a **single-pixel receiver**. For pattern $p$, $g_p$ is the calibrated illumination-and-reception kernel and $\sigma$ the scene reflectivity.

$$
y_p=\iiint_{\mathcal V}g_p(\mathbf r)\sigma(\mathbf r)\,d^3\mathbf r+n_p,\qquad
\mathbf y=\mathbf A\boldsymbol\sigma+\mathbf n,\quad \mathbf A\in\mathbb C^{P\times N}.
$$

**Reconstruction by $\ell_1$ minimization.** If $P\ll N$, exploit sparsity in the scene or a suitable representation such as wavelets. For direct sparsity,

$$
\min_{\boldsymbol\sigma}\lVert\boldsymbol\sigma\rVert_1
\quad\text{s.t.}\quad
\lVert\mathbf y-\mathbf A\boldsymbol\sigma\rVert_2\le\epsilon.
$$

Pattern diversity, calibration, measurement count, and solve time determine whether single-receiver imaging is practical and timely.

## 8.6.4 Comparing sensing and communications architectures

| Criterion | Passive reflecting RIS | Active or simultaneous-sensing RIS | Dynamic metasurface antenna (DMA) |
| --- | --- | --- | --- |
| Role | Virtual line-of-sight path and environment control | Reflection and local sampling, or amplification | Waveguide-fed transmit/receive antenna |
| RF chains | No receive chain on the surface | A few dedicated sensing nodes | A few RF chains and baseband processing |
| Power | Mainly control and switching | Higher with sensors or amplifiers | Can be lower than a fully digital array |
| Localization | Centralized at the base station | Local or distributed measurement | Near-field localization and imaging |
| Complexity | Surface control and calibration | Bias, sensors, and synchronization | Feed and pattern control |
| Application | Blind-spot coverage | Environment monitoring and cooperative ISAC | Compact imager or base station |

## 8.6.5 Research directions for metasurfaces and ISAC

**1. Near-field ISAC.** For an extremely large surface (XL-RIS), the approximate Rayleigh or Fraunhofer distance $2D^2/\lambda$ increases. A spherical-wave model retains both range and angle dependence. Point focusing and same-angle range separation depend on aperture, SNR, and calibration. Bandwidth still matters for delay estimation.

**2. Edge AI.** A controller near the surface can select the next pattern based on target estimates and uncertainty. Deep reinforcement learning is a research option. Measure decision latency, training cost, and improvement over a simple policy.

## Worked problem on localization and imaging behind an obstruction

::::{admonition} Try it first
:class: book-exercise

A metal shelf blocks the direct path from a base station to a cart in a warehouse. A wall-mounted RIS sees both. The station sends data and uses known OFDM symbols for sensing. Take $f_c=30\,\mathrm{GHz}$ and $B=1\,\mathrm{GHz}$. A $16\times16$ RIS with $\lambda/2$ pitch lies in the $xy$ plane centered at the origin. The station is at $(0,0,4)\,\mathrm m$ and the target at $z>0$. The echo travels station, RIS, cart, RIS, station. After calibration, $\tau=113.33\,\mathrm{ns}$ and $f_d=+200\,\mathrm{Hz}$. Pattern fitting gives $u_x=3/13$ and $u_y=4/13$. Each $0.5\,\mathrm{ms}$ cycle has four $25\,\mathrm{\mu s}$ sensing patterns and a data interval. Observe for $40$ cycles.

Find position and radial speed, range resolution, and the angle accuracy bound. Reconstruct a sparse scene with one receive channel and discuss changes in architecture and aperture.

```{dropdown} Show the full worked answer

### 1. Combining path length and direction

The wavelength is $\lambda=c/f_c=0.01\,\mathrm m$. The round-trip distance is $2(4\,\mathrm m+R)$, so

$$
R=\frac{c\tau}{2}-4\,\mathrm m\simeq13.0\,\mathrm m,\qquad
\mu_x=\frac{3\pi}{13},\quad\mu_y=\frac{4\pi}{13}.
$$

The quantity $c\tau/2\simeq17\,\mathrm m$ is the one-way path length via the RIS. Adjacent steering-vector phases in $x$ and $y$ change by $-41.5^\circ$ and $-55.4^\circ$. The station infers them from calibrated patterns.

$$
\theta=\arcsin(5/13)\simeq22.6^\circ,\quad \phi=\operatorname{atan2}(4,3)\simeq53.1^\circ,\quad
u_z=+\sqrt{1-u_x^2-u_y^2}=\frac{12}{13},\quad
\mathbf r\simeq[3,4,12]^T\,\mathrm m.
$$

Knowledge of the target half-space resolves the sign of $u_z$.

### 2. Doppler, resolution, and data time

$$
v_{\rm toward}=\frac{\lambda f_d}{2}=1.0\,\mathrm{m/s},\quad
\Delta R\simeq\frac{c}{2B}=0.15\,\mathrm m,\quad
\Delta f_d\simeq\frac{1}{40(0.5\,\mathrm{ms})}=50\,\mathrm{Hz}.
$$

Speed is the component toward the RIS. The $15\,\mathrm{cm}$ is nominal separation of two echoes. A $50\,\mathrm{Hz}$ Doppler bin corresponds to $0.25\,\mathrm{m/s}$ with coherent phase and nearly constant speed. Four patterns take $100\,\mathrm{\mu s}$, leaving $80\%$ for communications. At $2\,\mathrm{Gbit/s}$ during the data interval, the average is $1.6\,\mathrm{Gbit/s}$. More patterns may improve angular information at the cost of data time. Simultaneous beams share power and degrees of freedom.

### 3. Cramér–Rao angle bound

After Doppler phase compensation, use the following model for four calibrated responses near the nominal direction. Offsets $\delta\theta,\delta\phi$ are in radians, $\alpha$ is the unknown complex coefficient, and $\sigma^2$ is the independent complex noise variance. Slopes $8$ and $4$ are assumed calibration values. At the center $\rho=\lvert\alpha\rvert^2/\sigma^2=100$, or $20\,\mathrm{dB}$, with $K=40$ repeats.

$$
\mathbf y=\alpha[1+8\delta\theta,\ 1-8\delta\theta,\ 1+4\delta\phi,\ 1-4\delta\phi]^T+\mathbf n.
$$

The first two outputs differ by $16\alpha\delta\theta$ plus noise. The derivative vectors are orthogonal to the common response, so unknown $\alpha$ leaves the local angle bound unchanged at the nominal point.

$$
\mathbf J_{\rm angle}=4K\rho\,\operatorname{diag}(64,16),\qquad
\operatorname{std}(\widehat\theta)\ge\frac{1}{8\sqrt{4K\rho}}\simeq0.057^\circ,\qquad
\operatorname{std}(\widehat\phi)\ge\frac{1}{4\sqrt{4K\rho}}\simeq0.113^\circ.
$$

At fixed range the bounds imply roughly $1.3\,\mathrm{cm}$ and $1.0\,\mathrm{cm}$ tangential offsets through $R\,\operatorname{std}(\widehat\theta)$ and $R\sin\theta\,\operatorname{std}(\widehat\phi)$. Range, calibration, and multipath errors are separate. A strong beam can have a shallow slope at its center. Coherent gain alone therefore gives no universal $J_F\propto M^4$ law.

### 4. Three patterns for four scene bins

In the noiseless case, record one complex sample per pattern. The rows of $\mathbf A$ are calibrated responses over the four bins.

$$
\mathbf y=\mathbf A\boldsymbol\sigma,\quad
\mathbf A=\begin{bmatrix}1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{bmatrix},\quad
\mathbf y=[2,-2,-2]^T.
$$

The data are twice the second column. The columns sum to zero and the rank is $3$, so all solutions take the form $[t,2+t,t,t]^T$.

$$
\lVert\boldsymbol\sigma\rVert_1=3\lvert t\rvert+\lvert 2+t\rvert
\ge 2+2\lvert t\rvert,\qquad
\widehat{\boldsymbol\sigma}=[0,2,0,0]^T.
$$

The minimum is at $t=0$ and the second bin contains the reflector. With noise, use constraint $\lVert\mathbf y-\mathbf A\boldsymbol\sigma\rVert_2\le\epsilon$. Nearly identical columns can defeat separation even with apparently random patterns.

### 5. Architecture and the shift to near field

| Architecture | Role in the warehouse |
| --- | --- |
| Passive RIS | Path behind shelf, with sampling at the station |
| Sensing RIS | Local receive channels for estimation or calibration, with added power and synchronization |
| DMA | Imaging patterns at the station with a few RF chains, with a separate path around the obstruction |

$$
D\simeq\sqrt2\,(15\lambda/2)=0.106\,\mathrm m,\qquad R_F\simeq2D^2/\lambda=2.25\,\mathrm m.
$$

Both $4$ and $13\,\mathrm m$ exceed this boundary. With $D=1\,\mathrm m$, it rises to $200\,\mathrm m$. Model each cell's distance to the source and target. Wavefront curvature can separate targets at the same angle but different ranges. In edge processing, direct the next four patterns near the estimate when uncertainty is low and scan more widely as uncertainty rises. Compare the benefit with decision latency and lost data time. **Takeaway.** Delay gives path length, pattern slope gives direction, and Doppler gives path-length rate.
```
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
