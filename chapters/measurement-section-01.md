# 9.1 Materials, substrates, and electromagnetic response from microwaves to optics

Instructor booklet, pages 244–248.

So far we have mostly looked at cell geometry. Now ask what **the material itself** does. From microwaves through terahertz, infrared, and visible frequencies, reconsider the perfect electrical conductor (PEC) and quasistatic approximations in light of thickness, wavelength, and material response.

## 9.1.1 From classical conductivity to Drude–Lorentz

At microwave frequencies, copper (Cu), aluminum (Al), and gold (Au) can often be modeled as good conductors with constant conductivity $\sigma_{\rm dc}$. For thickness many skin depths,

$$
\delta_s=\sqrt{\frac{1}{\pi f\mu\sigma_{\rm dc}}},\qquad
R_s=\frac{1}{\sigma_{\rm dc}\delta_s}=\sqrt{\frac{\pi f\mu}{\sigma_{\rm dc}}}.
$$

Compare field frequency with the electron collision rate to assess the constant-conductivity limit. The **Drude model** describes free carriers. Add Lorentz oscillators for interband transitions.

$$
\varepsilon_r(\omega)=\varepsilon_\infty-\frac{\omega_p^2}{\omega(\omega-i\gamma)}
+\sum_{k=1}^K\frac{f_k\omega_{0k}^2}{\omega_{0k}^2-\omega^2+i\omega\Gamma_k},\quad
\omega_p=\sqrt{\frac{n_e e^2}{m^*\varepsilon_0}},\quad \gamma=\frac{1}{\tau_s}.
$$

Here $\varepsilon_\infty$ is the high-frequency background, $n_e$ carrier density, $m^*$ effective mass, and $\tau_s$ relaxation time. Ohmic damping and interband absorption can weaken plasmonic resonances. Choose a metal or high-index dielectric based on the band and loss budget.

## 9.1.2 Microwave and millimeter-wave substrates

Dielectric loss affects the $Q$ and reflection efficiency of a resonant patch or ring.

$$
\varepsilon=\varepsilon'-i\varepsilon''=\varepsilon'(1-i\tan\delta).
$$

| Substrate | Properties and application |
| --- | --- |
| High-frequency laminates (Rogers, Taconic) | Booklet examples use $\varepsilon_r\simeq2.2$ and $\tan\delta\simeq0.0009$ for RT/duroid 5880. RO4003C and RO4350B illustrate $\varepsilon_r\simeq3.48$ to $3.66$ and loss near $0.003$ for multilayer PCB processes. |
| Low-temperature co-fired ceramic (LTCC) | Mechanical strength and three-dimensional integration of lines and vias, including examples above $60\,\mathrm{GHz}$. |
| FR-4 | Low-cost glass fiber and epoxy, with example loss tangent around $0.02$ and process- and frequency-dependent permittivity. |

These are representative example values. For a design, use the data for the actual material, frequency, permittivity measurement method, and production tolerance.

## 9.1.3 Tunable materials at terahertz and optical frequencies

Where PIN-diode or varactor parasitics and loss limit their use, tune intrinsic conductivity or refractive index $n=\sqrt{\varepsilon_r\mu_r}$.

**Graphene.** The Kubo sheet conductivity has intraband and interband parts. Gate voltage $V_g$ moves the Fermi level $\mu_c$ and shifts the surface plasmon-polariton (SPP) resonance.

$$
\sigma_g=\sigma_{\rm intra}+\sigma_{\rm inter},\qquad
\sigma_{\rm intra}=
\frac{-ie^2 k_BT}{\pi\hbar^2(\omega-i2\Gamma)}
\left[\frac{\mu_c}{k_BT}+2\ln(1+e^{-\mu_c/(k_BT)})\right].
$$

**Vanadium dioxide (VO₂).** The insulator-to-metal transition (IMT) occurs near $68^\circ\mathrm C$ in example films. A sigmoid approximates the change of several orders of magnitude.

$$
\sigma(T)=\sigma_{\rm ins}+\frac{\sigma_{\rm met}-\sigma_{\rm ins}}{1+\exp[-(T-T_c)/\Delta T]}.
$$

Optical or electrical heating can change transmission, reflection, and absorption. Film and substrate geometry determine the power in each state.

**Chalcogenide GST ($\mathrm{Ge_2Sb_2Te_5}$).** Laser pulses or electrical heating can switch this nonvolatile phase-change material between amorphous and crystalline states. Both refractive index and extinction change. The state persists without continuous holding power.

## Worked problem on material selection across three bands

::::{admonition} Try it first
:class: book-exercise

Consider three samples at $10\,\mathrm{GHz}$, near $1\,\mathrm{THz}$, and at $1.55\,\mu\mathrm m$. Copper is $18\,\mu\mathrm m$ thick with $\sigma_{\rm dc}=5.8\times10^7\,\mathrm{S/m}$. Compare substrates with $\tan\delta=0.0009,0.003,0.020$, $p_e=0.70$, and $Q_{\rm other}=200$. For gold use $\varepsilon_\infty=9.5$, $\omega_p=1.37\times10^{16}\,\mathrm{rad/s}$, and $\gamma=10^{14}\,\mathrm{s^{-1}}$. Tune graphene from $0.20$ to $0.45\,\mathrm{eV}$. A $100\,\mathrm{nm}$ VO₂ film has conductivities $10$ and $10^5\,\mathrm{S/m}$ and $T_c=68^\circ\mathrm C,\Delta T=2^\circ\mathrm C$. A $200\,\mathrm{nm}$ GST layer has $\tilde n_a=4-i0.02$ and $\tilde n_c=6-i0.50$. Evaluate loss, resonance, and wave response.

```{dropdown} Show the full worked answer

### 1. Copper at microwave frequencies

$$
\delta_s\simeq0.66\,\mu\mathrm m,\quad
t/\delta_s\simeq27,\quad R_s\simeq0.026\,\Omega/\square.
$$

Current flows near the surface. Doubling thickness in this regime does not halve $R_s$. PEC helps estimate fields and geometry, but its $R_s=0$ cannot predict ohmic $Q$.

### 2. Substrate and resonance linewidth

$$
Q_d^{-1}\simeq p_e\tan\delta,\qquad
Q_{\rm tot}^{-1}=Q_{\rm other}^{-1}+Q_d^{-1},\qquad
\Delta f\simeq f_0/Q_{\rm tot}.
$$

| Example | $\tan\delta$ | $Q_d$ | $Q_{\rm tot}$ | $\Delta f$ |
| --- | --- | --- | --- | --- |
| RT/duroid 5880 | $0.0009$ | $1587$ | $178$ | $56\,\mathrm{MHz}$ |
| RO4000 | $0.003$ | $476$ | $141$ | $71\,\mathrm{MHz}$ |
| FR-4 | $0.020$ | $71$ | $53$ | $190\,\mathrm{MHz}$ |

FR-4 broadens the line through added damping. Efficiency and useful phase bandwidth require separating internal loss from radiative coupling. Changes in permittivity and field distribution may require retuning the geometry. PCB or LTCC integration also affects material choice.

### 3. Penetration and loss in gold

$$
\omega=2\pi c/\lambda_0\simeq1.216\times10^{15}\,\mathrm{rad/s},\quad
\omega/\gamma\simeq12.2,\quad
\varepsilon_m=\varepsilon_\infty-\frac{\omega_p^2}{\omega^2+\gamma^2}
-i\frac{\omega_p^2\gamma}{\omega(\omega^2+\gamma^2)}\simeq-116.6-i10.4.
$$

With $\mu_r\simeq1$, the decaying branch is $\tilde n_m\simeq0.48-i10.81$. Amplitude decays as $e^{-k_0\kappa z}$.

$$
\ell_E=\lambda_0/(2\pi\kappa)\simeq22.8\,\mathrm{nm},\qquad \ell_P=\ell_E/2.
$$

For an illustrative oscillator with $f_k=0.5$ and $\omega_{0k}/\Gamma_k=10$, at transition center $\Delta\varepsilon_L=f_k\omega_{0k}/(i\Gamma_k)=-i5$. Away from center the real part changes too. The oscillator is illustrative and is not fitted to gold.

### 4. Three tuning mechanisms

**Graphene.** For $\mu_c\gg k_BT$ with intraband dominance, Drude weight is proportional to $\mu_c$. For fixed geometry in the quasistatic model, $f_{\rm res}\propto\sqrt{\mu_c}$ and $1.0\sqrt{0.45/0.20}=1.50\,\mathrm{THz}$. Scattering and coupling also determine line width and depth.

**VO₂.** At $T_c$ conductivity is $50005\,\mathrm{S/m}$. Ten and ninety percent points follow from $T_c\mp\Delta T\ln9$, or $63.6$ and $72.4^\circ\mathrm C$. The model has no hysteresis. For a thin resistive film in air at normal incidence,

$$
g=\eta_0\sigma t,\qquad R=\left(\frac{g}{2+g}\right)^2,\quad
T=\left(\frac{2}{2+g}\right)^2,\quad A=1-R-T.
$$

$g$ goes from $0.000377$ to $3.77$. The insulating state transmits almost all power. The metallic state gives $42.7\%$ reflection, $12.0\%$ transmission, and $45.3\%$ absorption. Thickness and backing structure matter.

**GST.** Neglecting interface reflections and multiple passes,

$$
\lvert\Delta\phi\rvert=\frac{2\pi}{1.55}(6-4)(0.20)\simeq1.62\,\mathrm{rad}\simeq93^\circ,\qquad
P/P_0=e^{-2k_0\kappa t}.
$$

The crystalline state adds $93^\circ$ of phase delay. Internal power survival is $0.968$ in the amorphous state and $0.445$ in the crystalline state. These values account only for internal absorption. Count switching energy and optical loss separately from holding power.
```
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
