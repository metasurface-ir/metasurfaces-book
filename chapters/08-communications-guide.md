# Chapter 8 worked examples and self-check

Use these six examples to audit the [chapter](08-communications.md) and [computational lab](../labs/08-communications-lab.md). Values below refer to the saved 28-GHz reference, unless stated otherwise. Each example separates a mathematical check from a physical assumption.

## Example 1: normalize a reflecting aperture

**Predict:** Does received power fall as the inverse square of the total broken-path length?

**Work:** In the coherent broadside far field, the first propagation leg determines incident flux, the physical area determines captured power, and the aperture directs that power toward the receiver. Apply receiving effective area only once:

$$
P_r=\left(\frac{P_tG_tA}{4\pi r_t^2}\right)\eta\left(\frac{4\pi A}{\lambda^2}\right)\frac{1}{4\pi r_r^2}\left(\frac{G_r\lambda^2}{4\pi}\right)=\frac{P_t\eta G_tG_rA^2}{16\pi^2r_t^2r_r^2}.
$$

For A = 0.2304 m², efficiency 0.8, unity antenna gains and broadside distances 1000 and 1200 m, channel amplitude is approximately $1.367\times10^{-8}$. This is the far-field audit case, not the reference near-field geometry. Doubling only the first distance divides received power by four; doubling both divides it by sixteen. A single inverse-square factor for the total path would fail this benchmark.

**Check:** Area squared cancels four powers of distance. The result is a dimensionless channel power gain. This argument assumes an ideal aperture, far-field spreading and matched polarization.

## Example 2: focusing and finite phase states

**Predict:** Can a plane phase ramp and a spherical phase law be equivalent at finite distance?

**Work:** For each sample calculate both propagation distances and cancel their sum. The leading neglected plane-wave term is quadratic in aperture coordinate. It shrinks with either node distance but grows with aperture size and frequency. With D equal to the square’s diagonal:

$$
\lambda_0=\frac{299792458}{28\times10^9}\simeq 0.010707\ \mathrm m,\qquad \frac{2D^2}{\lambda_0}=\frac{4(0.48)^2}{0.010707}\simeq86.1\ \mathrm m.
$$

The actual node distances are 22.36 and 14.42 m. In the saved calculation, plane-law target power is 0.59553 of the spherical result, a loss of about 2.25 dB. Two-bit spherical rounding gives 0.80999, about 0.915 dB loss. The two errors arise from different operations and need not combine additively in dB when both are applied.

**Check:** Uniformly distributed two-bit rounding errors yield $(\sin(\pi/4)/(\pi/4))^2=8/\pi^2\simeq0.81057$. Agreement with the finite result is a useful comparison, not proof that every phase map has this loss.

## Example 3: a complete link budget

**Predict:** Is a −87-dB channel necessarily unusable?

**Work:** Power gain in dB adds to transmit power in dBm. Compute noise independently and subtract in dB; then convert to linear SNR for the capacity expression.

$$
\begin{aligned}P_r[\mathrm{dBm}]&=10-87.1582=-77.1582,\\P_n[\mathrm{dBm}]&=-173.9752+10\log_{10}(10^8)+7=-86.9752,\\\gamma[\mathrm{dB}]&=9.8170,\qquad\gamma=10^{9.8170/10}\simeq9.59,\\R&=100\times10^6\log_2(1+9.59)\simeq340.43\ \mathrm{Mbit/s}.\end{aligned}
$$

The thermal density uses 290 K; −174 dBm/Hz is a rounded mnemonic. No direct path is included here. Increasing bandwidth while keeping total transmit power fixed also increases noise, so rate is not generally proportional to bandwidth. The flat-channel assumption must remain valid.

**Check:** If transmit power tends to zero, the rate tends to zero. A negative SNR in dB is a positive linear ratio below one; it must not be inserted as a negative number inside the logarithm.

## Example 4: the common phase can help or hurt

**Predict:** Does adding a reflecting path always improve a direct link?

**Work:** For this algebraic example only, take equal direct and surface amplitudes a. Their combined power gain is

$$
|a+ae^{i\phi}|^2=2a^2(1+\cos\phi)=4a^2\cos^2(\phi/2).
$$

At 0°, the gain is four times either isolated gain; at 180°, it vanishes. The supplied browser instead uses its geometry-derived, unequal amplitudes and therefore does not reach a perfect null. The isolated-surface focusing law leaves a common phase free: use it to align with the direct channel when that channel is known.

**Check:** A fixed unknown phase cannot be modeled by adding powers unless a stated averaging mechanism removes the cross term. Under uniformly random relative phase, the ensemble mean is $2a^2$, but instantaneous fades remain.

## Example 5: phase errors and delay errors

**Predict:** Are independent phase errors equivalent to a common timing error?

**Work:** For equal weights, divide the Gaussian-error mean by the ideal coherent power:

$$
\frac{\mathbb E|h_s|^2}{|h_{\mathrm{ideal}}|^2}=\frac1N+\left(1-\frac1N\right)e^{-\sigma^2}.
$$

For many samples and 30° rms phase error, this approaches $e^{-(\pi/6)^2}\simeq0.760$. A common phase error leaves isolated-path power unchanged. Thus spatial correlation is part of the uncertainty model, not a minor detail.

Now consider two paths differing by 0.03 m. A 1-GHz frequency offset after fixed-phase compensation leaves

$$
\Delta\psi=\frac{2\pi(10^9)(0.03)}{299792458}\simeq0.629\ \mathrm{rad}\simeq36.0^\circ.
$$

A relative time-delay design can cancel that difference across frequency in the ideal model. It needs nonnegative delays referenced to the longest path; it does not require a physically negative delay.

**Check:** A frequency-dependent common phase does not defocus a single path, but relative frequency-dependent phase does.

## Example 6: choose a training budget

**Predict:** Must the densest focal codebook give the highest useful rate?

**Work:** For the displaced user, use the measured-in-the-model best candidate and account for every tested pilot. In a 200-symbol block:

$$
R_{\mathrm{net},17}=(1-17/200)(304.192)=278.336\ \mathrm{Mbps},\qquad R_{\mathrm{net},65}=(1-65/200)(334.770)=225.969\ \mathrm{Mbps}.
$$

K = 65 has the better gross channel, but pays for 48 additional pilot symbols. The optimum can change with coherence time, user position, noise or a hierarchical search. The browser varies coherence time without pretending to rerun a noisy channel estimator.

**Check:** At K = 0 the time factor is one, although the model must then explain where the state knowledge came from. At K equal to the coherence length no data symbols remain.

## Self-check and a short report

1. **Why not use Chapter 7’s normalized array intensity directly as link gain?** It omits incident flux, physical area, two-leg spreading and receiving effective area.
2. **Why does refining the midpoint grid not give an N² gain?** Each sample’s area decreases so the integral retains the same physical aperture.
3. **Is the smallest quadrature error the most accurate hardware prediction?** No. It only improves solution of the declared model; hardware-model discrepancy remains.
4. **Does a mean-power phase-error curve predict outage?** No. It does not provide the tail distribution or threshold.
5. **Can the wideband gain plot be called a data-rate spectrum?** No. Specify power spectral density, noise, equalization and hardware dispersion first.
6. **What changes for two simultaneous users?** Both user channels and inter-stream interference enter the optimization; one focused beam is insufficient evidence of two good links.

Submit a geometry diagram, three prediction/result comparisons, a derivation with units, one independent check, and one failed or misleading design. Suggested assessment: 25% physical assumptions, 25% derivation/units, 25% reproducibility/checks, and 25% interpretation and limitations. Use original plots; cite external hardware or channel data where introduced.
