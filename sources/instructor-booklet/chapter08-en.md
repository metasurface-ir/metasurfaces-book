# Metasurfaces in communications engineering

## 8.1 From a component to a communication system

Based on the instructor booklet, pages 204.

In a link, a surface matters only through the field at a receiver, the interference it creates or suppresses, and the overhead needed to set it. Start with a baseline link. Draw the transmitter, aperture and receiver, then decide whether you need coverage, focusing, frequency conversion or sensing. The same sheet can perform different tasks under different illumination and control.

$$
\mathrm{SNR}=P_t|h_{\rm eff}|^2/P_{\rm noise}.
$$

## 8.2 Programmable propagation and near-field focusing

Based on the instructor booklet, pages 204–211.

A reflecting panel can create a virtual line of sight around an obstruction, but it intercepts finite power. Each coefficient includes two distances, angle and polarization factors, and a measured complex state response. Equalize total path phases for a near-field focus. Two users along one ray may see different spherical wavefront curvatures, but measure both focal responses before claiming range discrimination. Train the channel using independent patterns and count pilot overhead. Judge performance with the direct field included coherently.

$$
h=\sum_n B_n\Gamma_n e^{-ik_0(r_{tn}+r_{nr})}+h_d,\quad \phi_n=k_0(r_{tn}+r_{nr})+\phi_0.
$$

## Worked exercise from the reading

In the source's training comparison, 16 grouped patterns take a total of 128 µs. What fraction of a 2 ms coherence interval is lost? What do grouped pilots identify?

```{dropdown} Show the worked answer
:class: solution

The fraction is $128/2000=6.4\%$. Grouped observations identify group responses when the pattern matrix has sufficient rank. Individual coefficients inside a group remain unresolved.
```

## 8.3 Leaky-wave, cavity and holographic antennas

Based on the instructor booklet, pages 211–218.

A periodic perturbation makes a guided wave radiate through a visible Floquet harmonic. Its leakage rate controls the usable aperture and beamwidth. A partially reflecting sheet over a ground plane makes a Fabry–Pérot cavity. Choose height to close the round-trip phase and consider leakage and bandwidth together. In holographic synthesis, interfere a known guided reference with a target radiating wave. Pattern the sheet with the resulting beat spatial frequency and verify unwanted harmonics with the actual feed and finite aperture.

$$
\beta_m=\beta_{\rm sw}+2\pi m/p,\quad \sin\theta_m=\beta_m/k_0,\qquad 2k_0 h=\psi_{\rm PRS}+\psi_{\rm g}+2\pi q.
$$

## Worked exercise from the reading

At normal incidence the cavity example has $\psi_{\rm PRS}=-108^\circ$. Take the PEC phase as $+180^\circ$. Find the smallest positive height in the phase-only model.

```{dropdown} Show the worked answer
:class: solution

The reflection phase sum is 72 degrees, so $h=\lambda/10$ for $q=0$. The phase condition alone cannot predict radiation efficiency or usable bandwidth.
```

## 8.4 Metalenses and orbital angular momentum

Based on the instructor booklet, pages 218–223.

At radius $\rho$ a normally illuminated lens must compensate the extra path to the focus. The curvature is generally hyperbolic, with a quadratic approximation near the axis. Phase gradient gives a local change in tangential momentum. Adding an azimuthal phase creates winding of charge $\ell$. Phase winding is spatial structure and is distinct from circular polarization. Finite receive aperture, misalignment and mode mixing determine whether multiplexing provides useful independent channels.

$$
\Phi(\rho,\varphi)=k_0(\sqrt{f^2+\rho^2}-f)+\ell\varphi.
$$

## Worked exercise from the reading

For $\ell=1$, list the additional phase at azimuths 0°, 90°, 180° and 270°. What happens if the receiver collects only a central disk?

```{dropdown} Show the worked answer
:class: solution

The phases are 0°, 90°, 180° and 270° modulo one turn. For a regular vortex field of nonzero charge the on-axis field vanishes. The collected power then depends on the radial mode profile and receiving radius.
```

## 8.5 Space-time modulation in a communication link

Based on the instructor booklet, pages 223–229.

A traveling pump shifts the frequency and transverse momentum of each harmonic together. Program the complex coefficient of a selected sideband to encode symbols. Its phase can track pump phase in the first order. Finite switching rates, control skew, spurious sidebands and leakage into the receive band all affect system performance. A duplex link needs a budget for residual self-interference at the receiver.

$$
f_m^{\rm out}=f_0+m f_{\rm pump},\quad k_{x,m}=k_{x,0}+mK,\quad a_1=0.25e^{i\varphi_b}.
$$

```{figure} ../assets/chapter-08/space-time-sidebands.svg
:alt: Incident wave, mounted unit cell and outgoing sidebands

Original teaching schematic for Figure 8–5. Arrow directions and lengths are schematic.
```

## Worked exercise from the reading

For a normal 10 GHz input, use a 200 MHz pump and $K=0.70k_0$. Find the upper sideband angle and show the QPSK symbols available from four pump phases.

```{dropdown} Show the worked answer
:class: solution

The upper sideband is at 10.2 GHz, hence $\sin\theta=0.70/1.02$ and $\theta\simeq43.3^\circ$. Pump phases $0,\pi/2,\pi,3\pi/2$ yield $0.25\{1,i,-1,-i\}$. Their equal modeled magnitudes do not account for frequency-dependent hardware loss.
```

## 8.6 Integrated sensing, localization and imaging

Based on the instructor booklet, pages 230–236.

A common waveform can carry data and probe the scene. Round-trip delay gives path length, while coherent element responses provide angle. A separable rectangular aperture has a Kronecker steering vector. In a coded imaging aperture, each mask gives a linear combination of scene cells. Check singular values or column coherence to see whether two candidate locations can be separated. A dynamic metasurface antenna can trade more masks for fewer RF chains.

$$
\tau=2L/c,\qquad \mathbf a=\mathbf a_y\otimes\mathbf a_x,\qquad \mathbf y=\mathbf A\mathbf x+\mathbf n.
$$

## Worked exercise from the reading

In the booklet's local angular model the four response factors are $1+8\delta\theta,1-8\delta\theta,1+4\delta\phi,1-4\delta\phi$, all multiplied by the same unknown complex echo $\alpha$. How can a noiseless estimator eliminate $\alpha$?

```{dropdown} Show the worked answer
:class: solution

Divide each pair difference by its sum. The two ratios are $8\delta\theta$ and $4\delta\phi$. The ratio is undefined at zero echo and becomes unstable at low SNR. The angular approximation is local.
```

## 8.7 Hardware, training cost and network integration

Based on the instructor booklet, pages 236–242.

Real state phases and amplitudes are coupled. Wideband steering can squint, a large cascade can take too long to estimate, and stale control commands can erase the gain. Compare passive, active and hybrid surfaces at equal coverage and available time, including noise, control traffic, installation and maintenance. Treat network integration as an engineering and interoperability question whose requirements should be checked for the intended system.

$$
\Gamma_n=\alpha_n(\theta_n)e^{i\theta_n},\qquad \tau_{\rm data}=\max(0,T_c-\tau_{\rm train}-\tau_{\rm ctrl}).
$$

## Worked exercise from the reading

If training and control consume 1.13 ms in a 2 ms coherence interval, how much remains? What is DC output from −10 dBm of harvested RF at 40% conversion?

```{dropdown} Show the worked answer
:class: solution

There are 0.87 ms left, or 43.5%. The incident RF power is 0.10 mW, so the harvested DC is 0.04 mW before downstream losses. Compare it with the complete duty-cycle-dependent budget.
```
