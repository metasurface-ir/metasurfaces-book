# Chapter 9: Materials, Fabrication Technologies, and Measurement Methods

## 9.1 Materials, substrates, and electromagnetic response from microwaves to optics

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


## 9.2 Microstructure fabrication and deposition

Instructor booklet, pages 248–254.

To choose a process, first ask **which dimension controls the response**. It could be patch length, a gap, or pillar height. Subwavelength elements may span roughly $\lambda/10$ to $\lambda/2$, with smaller critical features assessed separately.

| Band | Process family | Booklet example of tolerance scale |
| --- | --- | --- |
| Microwave, $1$ to $30\,\mathrm{GHz}$ | PCB and multilayer fabrication | About $20$ to $50\,\mu\mathrm m$ |
| Terahertz, $0.1$ to $10\,\mathrm{THz}$ | Optical lithography and micromachining | About $0.5$ to $1\,\mu\mathrm m$ |
| Infrared and optical, $100$ to $700\,\mathrm{THz}$ | EBL, FIB, or nanoimprint | About $2$ to $10\,\mathrm{nm}$ |

These scales are illustrative. For example, over $0.1$ to $10\,\mathrm{THz}$ the free-space wavelength is about $3\,\mathrm{mm}$ to $30\,\mu\mathrm m$. Measure tolerance on the final part.

## 9.2.1 Printed circuit boards for microwave and millimeter-wave structures

Start with a low-loss copper-clad laminate, such as RO4003C or RT/duroid 5880. Low-profile foil, for example with $R_q<0.5\,\mu\mathrm m$, helps reduce roughness loss. Apply dry-film or spin-coated photoresist, expose through a UV mask, develop, and wet-etch the unprotected copper, for example with ferric or cupric chloride. Mask accuracy, development, and etching all matter.

**Undercutting.** Etchant attacks laterally as well, so a trace can become trapezoidal in cross-section. For copper thickness $t$, bottom width $w_b$, and top width $w_t$,

$$
u=\frac{w_b-w_t}{2},\qquad \mathrm{EF}=\frac{2t}{w_b-w_t}=\frac t u.
$$

```{figure} ../../assets/chapter-09/etch-cross-section.svg
:alt: Trapezoidal copper cross-section on a substrate with top width, bottom width, and undercut labeled

Teaching schematic of wet-etched copper. Each upper edge recedes by $u$. The figure is schematic.
```

The same small deviation can noticeably shift a narrow patch resonance. In a multilayer PCB the RF patches, continuous or slotted ground, and DC control occupy separate layers. Mechanical or UV laser drilling and via plating create plated through-holes (PTH). Low-loss prepreg such as RO4450 has thickness and permittivity and belongs in the model.

## 9.2.2 Cleanroom photolithography and deposition

As gaps reach a few micrometers, first check PCB process capability. Cleanroom options include contact or projection photolithography, chrome-on-quartz masks, and Deep UV at $193$ or $248\,\mathrm{nm}$ in suitable systems. Negative SU-8 resist can form thick high-aspect-ratio dielectric structures.

- **E-beam evaporation:** Metal vapor leaves a crucible in vacuum and condenses on the substrate. Directional deposition helps lift-off.
- **DC/RF magnetron sputtering:** Argon ions eject atoms from a target. Check resist sidewall coverage on lift-off patterns.
- **Adhesion layer:** A few nanometers of Ti or Cr, for example $3$ to $10\,\mathrm{nm}$, can improve adhesion to glass, quartz, or silicon and can add optical loss.

In **lift-off**, pattern resist with an undercut profile, then deposit metal on the exposed substrate and on the resist. Removing the resist lifts the metal on top of it and leaves the substrate pattern. This deliberate undercut differs from unwanted copper undercut in PCB etching.

## 9.2.3 Nanolithography for meta-optics

Si or $\mathrm{TiO_2}$ pillars and plasmonic structures can need features around $50$ to $300\,\mathrm{nm}$. **EBL** writes directly on resists such as PMMA or ZEP520A without a mask, useful for precision prototypes or masters. Sub-$10\,\mathrm{nm}$ capability is process-dependent and serial writing is slow. **FIB**, for example with $\mathrm{Ga^+}$, is useful for direct milling and local editing. Check damage and implantation.

For a silicon pillar at or above aspect ratio $10{:}1$, lithography defines the pattern and etching transfers it into the material. In Bosch **DRIE**, $\mathrm{SF_6}$ etching alternates with $\mathrm{C_4F_8}$ sidewall passivation. Measure wall angle and scalloping. In **nanoimprint** (NIL), a master mold replicates the pattern in a curable polymer. A final silicon device usually still needs pattern transfer.

## 9.2.4 Additive fabrication and flexible patterns

SLA and DLP cure resin for curved microwave structures, Luneburg lenses, and three-dimensional reflectors. The nominal step can be of order $25\,\mu\mathrm m$. Measure finished-part accuracy. Inkjet, screen, or roll-to-roll printing deposits silver ink onto Kapton polyimide or PET and uses sintering to develop conductivity. For a flexible surface measure response after bending.

## Worked problem on tolerances in four processes

::::{admonition} Try it first
:class: book-exercise

There are four samples. A $30\,\mathrm{GHz}$ reflecting PCB has $18\,\mu\mathrm m$ copper, patch top and bottom lengths $2.976$ and $3.000\,\mathrm{mm}$, and resonance limit $\pm100\,\mathrm{MHz}$. A $1\,\mathrm{THz}$ structure has a $3.0\pm0.5\,\mu\mathrm m$ gap and $\pm3\%$ resonance limit. The $1.55\,\mu\mathrm m$ silicon metalens pillar has diameter $150\,\mathrm{nm}$, height $1.50\,\mu\mathrm m$, wall deviation $0.5^\circ$, and allowed diameter difference $10\,\mathrm{nm}$. A rigid curved part for $30\,\mathrm{GHz}$ uses $n=1.6$ with height error $\pm25\,\mu\mathrm m$. Its flexible counterpart needs a conductive film pattern. For each design choose a process and acceptance measurement.

```{dropdown} Show the full worked answer

### 1. PCB patch undercut

$$
u=(3000-2976)/2=12\,\mu\mathrm m,\quad \mathrm{EF}=18/12=1.5,\quad
L_{\rm eff}\simeq(3.000+2.976)/2=2.988\,\mathrm{mm}.
$$

With the geometric mean-of-lengths approximation and $f_0\propto1/L_{\rm eff}$, $f_{\rm built}=30(3.000/2.988)\simeq30.1205\,\mathrm{GHz}$. A shift of $+120.5\,\mathrm{MHz}$ fails the limit. If coupons show a repeatable $12\,\mu\mathrm m$ mean reduction, add that length to the next design and remeasure. In a multilayer build, alignment, vias, and bonding layers matter. The via cross-section checks connectivity while coupon resonance tests the combined errors on the wave.

### 2. Terahertz gap

In an $LC$ model with $C\propto1/g$ and constant $L$,

$$
f(g)=\frac{1}{2\pi\sqrt{LC}}\simeq f_0\sqrt{g/g_0},\qquad
f(2.5\,\mu\mathrm m)\simeq0.913\,\mathrm{THz},\quad
f(3.5\,\mu\mathrm m)\simeq1.080\,\mathrm{THz}.
$$

The $-8.7\%$ to $+8.0\%$ variation exceeds $\pm3\%$. Invert the inequality to find the gap limits.

$$
3(0.97)^2\le g/(\mu\mathrm m)\le3(1.03)^2
\quad\Rightarrow\quad 2.823\lesssim g/(\mu\mathrm m)\lesssim3.183.
$$

A symmetric tolerance of $\pm0.177\,\mu\mathrm m$ or better is needed. For metal on quartz, test precise lithography and lift-off on a coupon. Directional evaporation limits wall coverage, while sputtering can connect films on the sidewall. **The final fabricated gap** is the acceptance quantity. Account for fringing fields in a real design.

### 3. Metalens pillar profile

$$
\mathrm{AR}=h/D=1500/150=10{:}1,\quad
\lvert\Delta D\rvert=2h\tan0.5^\circ\simeq26.2\,\mathrm{nm},\quad
\alpha_{\max}=\arctan[10/(2\times1500)]\simeq0.191^\circ.
$$

In the frustum approximation the sample exceeds the $10\,\mathrm{nm}$ limit. Use EBL for prototypes and masters, FIB for local edits with implantation considered, anisotropic etching for silicon profiles, and NIL to replicate a verified master. Measure height, top and bottom diameters, and wall roughness together.

### 4. Rigid or flexible part

For SLA/DLP, if height error replaces that thickness of air with resin at near-normal incidence,

$$
\lvert\Delta\phi\rvert\simeq \frac{2\pi}{\lambda_0}(n-1)\lvert\Delta h\rvert
=\frac{360^\circ}{10}(1.6-1)(0.025)=0.54^\circ.
$$

This fits a $2^\circ$ height-error budget. Loss, refractive index after cure, and overall shape need separate checks. For a flexible pattern, consider inkjet for prototyping and screen or roll-to-roll printing for replication. Measure trace width, gaps, post-sintering sheet resistance, and RF response before and after bending.
```
::::


## 9.3 Assembly and integration of reconfigurable elements

Instructor booklet, pages 254–260.

A programmable metasurface combines three parts. The RF layer contains patches, slots, and diodes. A continuous or slotted ground separates fields from the rear circuitry, while plated vias provide a reference path. Behind it, bias routing, current buffers, converters, and an FPGA turn commands into cell voltages and currents. The connection and return path can change the patch response.

## 9.3.1 PIN diodes and varactors

In digital coding, a PIN diode conducts under forward bias, for example $5$ to $15\,\mathrm{mA}$. Under reverse bias, for example $0$ to $-5\,\mathrm V$, junction capacitance and leakage matter. A two-state model is

$$
Z_{\rm ON}=R_s+i\omega L_s,\qquad
Z_{\rm OFF}=i\omega L_s+\frac{1}{i\omega C_t+1/R_p},\qquad
f_c=\frac1{2\pi R_s C_t}.
$$

Booklet example ranges are $R_s=0.8$ to $3\,\Omega$, $L_s=0.1$ to $0.5\,\mathrm{nH}$, and $C_t=0.02$ to $0.15\,\mathrm{pF}$. The quantity $f_c$ is a figure of merit. At millimeter wavelengths consider GaAs or another high-$f_c$ diode, then check the package and parasitics, which can erase state contrast even with a high figure of merit.

For continuous tuning use a **varactor** with reverse-bias magnitude $V_R$. Here $C_{j0}$ is zero-bias capacitance, $V_{\rm bi}$ the built-in potential, and $\gamma$ the junction parameter.

$$
C_v=\frac{C_{j0}}{(1+V_R/V_{\rm bi})^\gamma},\qquad Q_v=\frac1{\omega R_s C_v}.
$$

Series resistance can change with bias as well. Changes in resonance and varactor current lead to **phase–amplitude coupling**.

## 9.3.2 High-frequency packaging and attachment

| Method | Structure and limitation |
| --- | --- |
| SMT / reflow | DFN, QFN, 0402, or 0201 packages. Pads and solder paths can become part of the RF geometry. |
| Wire bonding | Bare die, with $15$ to $25\,\mu\mathrm m$ gold or aluminum wire. An example scale is $0.8\,\mathrm{nH/mm}$. Short, parallel, or ribbon bonds can reduce inductance. |
| Flip-chip | An inverted die with micro-bumps around $20$ to $50\,\mu\mathrm m$. Connection inductance can be around $0.05\,\mathrm{nH}$ in examples. Include the return path. |

## 9.3.3 RF and DC bias isolation

RF leakage into bias wiring steals aperture power, can make the wiring radiate, and can bring digital clock noise into the band. A $\lambda_g/4$ line terminated near an RF short presents a large impedance at the patch. A radial stub can provide a virtual RF ground while leaving the DC route available. Choose an RF choke using impedance and self-resonant-frequency data. A high-sheet-resistance line, for example Cr or nichrome, may suit a low-current bias. Check DC voltage drop and settling.

## 9.3.4 Digital control and FPGA drivers

A $32\times32$ panel would otherwise require one pin per $1024$ cells. A serial-in parallel-out (SIPO) shift register, such as a 74HC595 or a high-voltage HV507 driver, receives frames over an interface such as SPI. A common latch prevents intermediate states from reaching the panel. The stated clock rate does not account for settling, cell-to-cell skew, or driver limits. With half of one thousand $10\,\mathrm{mA}$ diodes on, current is about $5\,\mathrm A$. Design rail capacity, heat distribution, thermal vias, and heat sink together.

## Worked problem on integrating a 28 GHz panel

::::{admonition} Try it first
:class: book-exercise

A $32\times32$ panel at $28\,\mathrm{GHz}$ uses one PIN diode per cell for nearly $180^\circ$ phase difference. The diode has $R_s=2\,\Omega,C_t=0.10\,\mathrm{pF},I_f=10\,\mathrm{mA},V_f=0.9\,\mathrm V$ with negligible off leakage. Total connection inductances for SMT, wire bond, and flip-chip are $0.30,0.20,0.05\,\mathrm{nH}$. For the varactor version use $C_{j0}=0.40\,\mathrm{pF},V_{\rm bi}=0.80\,\mathrm V,\gamma=0.5$, and $2$ and $3\,\Omega$ at reverse biases $0$ and $12\,\mathrm V$. The bias line has $Z_0=60\,\Omega,\varepsilon_{\rm eff}=2.8$. A choke has SRF $18\,\mathrm{GHz}$ and a resistive path is $10\,\mathrm{k\Omega}$. Shift clock is $20\,\mathrm{MHz}$, deadline $10\,\mu\mathrm s$, latch and settle time $0.6\,\mu\mathrm s$, and rail $3.3\,\mathrm V$. Evaluate assembly, continuous tuning, bias, loading time, and heat.

```{dropdown} Show the full worked answer

### 1. Assembly screening

$$
f_c=1/(2\pi R_s C_t)\simeq796\,\mathrm{GHz},\qquad
1/(\omega C_t)\simeq56.84\,\Omega.
$$

| Attachment | $\omega L_s$ | $Z_{\rm ON}$ | $Z_{\rm OFF}$ |
| --- | --- | --- | --- |
| SMT | $52.78\,\Omega$ | $2+i52.78\,\Omega$ | $-i4.06\,\Omega$ |
| Wire bond | $35.19\,\Omega$ | $2+i35.19\,\Omega$ | $-i21.65\,\Omega$ |
| Flip-chip | $8.80\,\Omega$ | $2+i8.80\,\Omega$ | $-i48.04\,\Omega$ |

The printed problem omits numeric screening limits. To reproduce its decision, use **illustrative limits** $\lvert Z_{\rm ON}\rvert\le10\,\Omega$ and $\lvert Z_{\rm OFF}\rvert\ge40\,\Omega$. Flip-chip passes with $9.02$ and $48.04\,\Omega$. For SMT, the connection and $C_t$ resonate near $1/(2\pi\sqrt{L_s C_t})=29.1\,\mathrm{GHz}$, making the off impedance small in-band. The final test is $\angle(\Gamma_{\rm ON}/\Gamma_{\rm OFF})$ near $180^\circ$, with adequate amplitudes in both states and a common phase reference. Include pads, solder, vias, and patch.

### 2. Varactor at two biases

$$
C_v(0)=0.40\,\mathrm{pF},\qquad C_v(12)=0.40/\sqrt{1+12/0.80}=0.10\,\mathrm{pF}.
$$

$Q_v$ rises from $7.1$ to $18.9$ because the capacitance decrease outweighs the resistance increase. This is the series-varactor branch quality factor. For the cell, tabulate $V_R$, $\angle\Gamma$, and $\lvert\Gamma\rvert$. For similar phases choose the better amplitude. Near zero bias also test for unintended conduction under RF swing.

### 3. Bias network

$$
\lambda_g=c/(f\sqrt{\varepsilon_{\rm eff}})\simeq6.40\,\mathrm{mm},\qquad
\ell=\lambda_g/4\simeq1.60\,\mathrm{mm},\qquad Z_{\rm in}=iZ_0\tan(\beta\ell).
$$

An RF short at the far end looks open from the patch at design frequency. A radial stub approximates that condition. At $5\%$ higher frequency, neglecting dispersion, $\lvert Z_{\rm in}\rvert\simeq60\lvert\tan(1.05\pi/2)\rvert\simeq762\,\Omega$. This is not a measured isolation in decibels. A choke with $18\,\mathrm{GHz}$ SRF requires in-band data at $28\,\mathrm{GHz}$. The $10\,\mathrm{k\Omega}$ path drops $100\,\mathrm V$ for an on-state PIN, but only $1\,\mathrm{mV}$ for an assumed $0.1\,\mu\mathrm A$ varactor leakage. Check settling.

### 4. Frame loading and heat

$$
t_1=1024/(20\,\mathrm{MHz})+0.6\,\mu\mathrm s=51.8\,\mu\mathrm s,\qquad
t_8=128/(20\,\mathrm{MHz})+0.6\,\mu\mathrm s=7.0\,\mu\mathrm s.
$$

Eight parallel chains of sixteen eight-bit registers meet the timing for a **ready frame**. A latch keeps intermediate patterns off the panel. Computation time and driver skew are separate, and current buffers supply the diodes.

$$
I_{\rm rail}=512(10\,\mathrm{mA})=5.12\,\mathrm A,\qquad
P_{\rm rail}=16.90\,\mathrm W,\quad P_{\rm PIN}=4.61\,\mathrm W,\quad P_{\rm series}=12.29\,\mathrm W.
$$

Most heat is in linear drivers or current limiters. With all cells on, the totals are $10.24\,\mathrm A$ and about $33.8\,\mathrm W$. Test supply, bypassing, and heat sink at the worst allowed pattern and check transient rail droop at the latch. Separate three acceptance tests: mounted-cell response, RF leakage to bias, and supply and temperature stability.
```
::::


## 9.4 Microwave and millimeter-wave measurement setups

Instructor booklet, pages 260–265.

After fabrication, decide **what to measure**. A modal reflection coefficient, a near-field map, and peak beam direction are different measurements. Cables, antennas, alignment, and room echoes affect them differently.

## 9.4.1 Free-space measurements and anechoic chambers

Carbon-loaded foam pyramids reduce wall reflection in an anechoic chamber. In a **monostatic** arrangement, one horn transmits and receives, usually recording raw $S_{11}$ for coaxial reflection. In a **bistatic** arrangement, the transmitter stays at $\theta_i$ and the receiving horn moves along an arc in $\theta_r$. This measures patterns for anomalous reflection.

```{figure} ../../assets/chapter-09/reflection-reference.svg
:alt: Shared transmit-receive horn on the left and a separate angular receive horn on the right

Teaching schematic of reflection fixtures. In (a), one horn handles the round trip. In (b), a separate receiver moves on an arc.
```

$$
R\gtrsim 2D^2/\lambda_0.
$$

For the Fraunhofer estimate take the largest relevant aperture dimension $D$ and check the shortest sweep wavelength. In a short chamber, dielectric lenses can form a focused Gaussian beam with the sample at its waist. Check spot size, phase, amplitude, and edges.

## 9.4.2 Calibration and time gating

A vector network analyzer (VNA) measures complex response. In **TRL**, the Thru, Reflect, and Line standards determine fixture error terms. The through path, reflect standard, and phase-shifted line need consistent geometry and coupling. An added length near $\lambda/4$ gives an example one-way phase difference at design frequency. TRL performance depends on band and standard design.

In a coaxial reflection comparison with an equal-sized metal plate, subtract the background from both **complex traces**, then normalize to the reference. This is a separate step from solving TRL error terms.

$$
\Gamma_{\rm MS}\simeq-\frac{S_{\rm sample}-S_{\rm iso}}{S_{\rm ref}-S_{\rm iso}}.
$$

In **time gating**, an IFFT converts the frequency trace into delay. Apply a Hann or Tukey window around the sample pulse and use an FFT to return to frequency. Bandwidth and window shape determine delay resolution. A narrow gate can cut off a real resonance tail and cannot separate a coincident echo.

## 9.4.3 Guided measurement in a waveguide

A cell or a few cells can sit between WR-series rectangular waveguide flanges. A guided fixture provides repeatable geometry and mode excitation without a large chamber. PEC walls and the nonuniform $\mathrm{TE}_{10}$ field generally do not reproduce free-space periodic excitation. Report the mode, reference plane, and fixture.

## 9.4.4 Near-field scanning and the plane-wave spectrum

For metalenses and beams with orbital angular momentum (OAM), a complex aperture-field map exposes how the design works. An open-ended waveguide probe on an $X$–$Y$–$Z$ stage records a field component on a plane. After probe calibration, the near-to-far-field transform (NFFF) follows from the plane-wave spectrum (PWS).

$$
F(k_x,k_y)=\iint E(x,y,z_0)e^{i(k_xx+k_yy)}\,dx\,dy.
$$

Only $k_x^2+k_y^2\le k_0^2$ propagates to the far field. For a quantitative three-dimensional pattern, account for polarization, vector components, probe response, windowing, and scan aperture.

## Worked problem on measuring a 28 GHz panel

::::{admonition} Try it first
:class: book-exercise

A panel with $D=160\,\mathrm{mm}$ is measured with $50\,\mathrm{mm}$ horns at $6\,\mathrm m$. Measure coaxial reflection in the uniform state and the $+30^\circ$ beam in the beamforming state. At $28\,\mathrm{GHz}$, $S_{\rm iso}=0.010+i0.005$, $S_{\rm ref}=-0.090+i0.005$, and $S_{\rm sample}=0.010+i0.065$. A $26$ to $30\,\mathrm{GHz}$ sweep in $10\,\mathrm{MHz}$ steps gives a sample pulse at $40\,\mathrm{ns}$ and echo at $42\,\mathrm{ns}$. In WR-28 with $a=7.112,b=3.556\,\mathrm{mm}$ the states give $S_{11}=0.83\angle-20^\circ$ and $0.76\angle150^\circ$. After separating the incident field, a complex $320\times320\,\mathrm{mm^2}$ scan with $4\,\mathrm{mm}$ pitch peaks at $k_x=293\,\mathrm{rad/m},k_y\simeq0$. Determine the setups, calibrations, and meaning of each result.

```{dropdown} Show the full worked answer

### 1. Geometry and far field

$$
\lambda_0\simeq10.71\,\mathrm{mm},\quad
R_F(28\,\mathrm{GHz})\simeq4.78\,\mathrm m,\quad R_F(30\,\mathrm{GHz})\simeq5.12\,\mathrm m.
$$

The panel has the larger aperture, and $6\,\mathrm m$ passes the sweep criterion. Check amplitude uniformity and room echoes separately. Use monostatic reflection for the coaxial result and bistatic $S_{21}(\theta_r)$ for the beam. A relative pattern gives the peak. Absolute efficiency requires calibrated power and pattern integration. A focused beam can serve a local test.

### 2. Complex subtraction and reference

$$
S_{\rm sample}-S_{\rm iso}=i0.060,\qquad
S_{\rm ref}-S_{\rm iso}=-0.100,\qquad
\Gamma_{\rm MS}=i0.60=0.60\angle90^\circ.
$$

Magnitude is $20\log_{10}(0.60)\simeq-4.44\,\mathrm{dB}$ and channel power is $0.36$ relative to the plate. Remaining power can occupy other angles, polarizations, transmission, or absorption. Position error $0.5\,\mathrm{mm}$ changes the round trip by $1\,\mathrm{mm}$, or about $33.6^\circ$. A one-way increase $\lambda_0/4\simeq2.68\,\mathrm{mm}$ gives $90^\circ$ phase and serves as a Line only in a consistent fixture. At normal incidence the metal reference is coaxial. Dividing a $+30^\circ$ measurement by its weak off-axis reflection is invalid.

### 3. Time gate

$$
\Delta t_{\rm res}\sim 1/(4\,\mathrm{GHz})=0.25\,\mathrm{ns},\qquad
T_{\rm amb}=1/(10\,\mathrm{MHz})=100\,\mathrm{ns},\qquad
2R/c\simeq40\,\mathrm{ns}.
$$

Separation of $2\,\mathrm{ns}$ allows gating if the resonant tail is short enough. Subtract complex background from sample and reference, use identical IFFT and gate settings, transform back, and take the ratio. Test for truncation by making a small change in gate width and checking response stability.

### 4. Comparing waveguide-mode responses

$$
f_{c,10}=c/(2a)\simeq21.1\,\mathrm{GHz},\qquad f_{c,20}=f_{c,01}\simeq42.2\,\mathrm{GHz},\qquad
\Delta\phi=150^\circ-(-20^\circ)=170^\circ.
$$

In-band only $\mathrm{TE}_{10}$ propagates away from the sample, although higher modes can be evanescent near it. Returned modal powers are $0.83^2\simeq69\%$ and $0.76^2\simeq58\%$. Both the $10^\circ$ phase shortfall and amplitude inequality matter in panel modeling. Waveguide data alone do not give the free-space response.

### 5. Peak of the near-field spectrum

The $4\,\mathrm{mm}$ pitch is below $\lambda_0/2\simeq5.36\,\mathrm{mm}$, adequate for propagating components. Evanescent or subwavelength detail can require finer sampling. With aligned axes and a corrected field component,

$$
k_0\simeq586.4\,\mathrm{rad/m},\qquad \theta_r=\arcsin(293/586.4)\simeq+30.0^\circ,
\qquad \Delta k_x\sim 2\pi/(0.320\,\mathrm m)\simeq19.6\,\mathrm{rad/m}.
$$

The corresponding resolution scale near the peak is about $2.2^\circ$. Low noise can permit better estimation of one peak center. Zero-padding only refines the display grid. Check with a bistatic scan or a wider near-field scan. Coaxial reflection, waveguide modal reflection, and beam peak each depend on their own geometry and reference.
```
::::


## 9.5 Retrieving effective parameters from measurements

Instructor booklet, pages 265–270.

**Homogenization** replaces microstructure with an equivalent model. A bulk slab may be described by $\varepsilon_{\rm eff}$ and $\mu_{\rm eff}$. For a thin surface, an input impedance $Z_s$ or sheet admittance $Y_s$ can answer a better-posed question. VNA data give parameters for **the chosen model and reference plane**.

## 9.5.1 Slab model and the Nicholson–Ross–Weir method

For a symmetric homogeneous slab of thickness $d$ in identical media, with reference planes at its faces and normal single-mode incidence, let $\Gamma$ be the single-interface reflection and $T=e^{-ik_0n_{\rm eff}d}$ the one-way propagation factor. Summing internal reflections gives

$$
S_{11}=\frac{\Gamma(1-T^2)}{1-\Gamma^2 T^2},\qquad
S_{21}=\frac{T(1-\Gamma^2)}{1-\Gamma^2 T^2}.
$$

In this example $z_{\rm eff}$ is normalized to the surrounding air. The $S^2$ terms below are complex squares. For passive material, check propagation and continuity when selecting the root compatible with $\lvert\Gamma\rvert\le1$ and $\operatorname{Re}z_{\rm eff}\ge0$.

$$
X=\frac{S_{11}^{2}-S_{21}^{2}+1}{2S_{11}},\quad
\Gamma=X\pm\sqrt{X^2-1},\quad z_{\rm eff}=\frac{1+\Gamma}{1-\Gamma},\quad
T=\frac{S_{11}+S_{21}-\Gamma}{1-(S_{11}+S_{21})\Gamma}.
$$

Taking the logarithm introduces a **branch index**. Verify the sign by substitution into the definition of $T$. Then recover the relative slab properties.

$$
n_{\rm eff}=\frac{i\ln T}{k_0 d}
=\frac{-[\arg T+2\pi m]+i\ln\lvert T\rvert}{k_0d},\quad m\in\mathbb Z,\qquad
\varepsilon_{\rm eff}=\frac{n_{\rm eff}}{z_{\rm eff}},\quad
\mu_{\rm eff}=n_{\rm eff}z_{\rm eff}.
$$

Ambiguity follows **electrical thickness**. Phase continuity or group delay $\tau_g=-d\arg T/d\omega$ tracks changes but cannot determine a constant $2\pi$ offset. Start from a valid low-frequency limit or independent reference when available. Interpret $v_g=c/[n+\omega\,dn/d\omega]$ in the simple low-loss model. The condition $0<v_g<c$ is not a universal branch test. Near $S_{11}=0$, the form for $X$ is ill-conditioned. Use a stable formulation or fit and reconstruct the scattering data.

## 9.5.2 Grounded surfaces and transmitting sheets

A **grounded surface** at normal incidence has a closed transmission channel. Obtain **input impedance** from $\Gamma=S_{11}$ at the surface reference plane.

$$
S_{11}=\frac{Z_s-\eta_0}{Z_s+\eta_0},\qquad
Z_s=\eta_0\frac{1+S_{11}}{1-S_{11}}=R_s+iX_s.
$$

$R_s$ includes loss seen at this port. $X_s>0$ is inductive and $X_s<0$ capacitive. Zero reflection requires both $R_s=\eta_0$ and $X_s=0$. The formula $\phi_{\rm ref}=\pi-2\arctan(X_s/\eta_0)$ modulo $2\pi$ applies only when $R_s=0$.

For an **electric-only sheet** between identical air regions, tangential electric field is continuous and $t=1+r$. Surface current follows from the magnetic-field jump.

$$
Y_s=\frac{1-r-t}{\eta_0 t}=\frac{2}{\eta_0}\frac{1-t}{t},\qquad Z_s=\frac1{Y_s}.
$$

The factor of two appears only after substituting $r=t-1$. If $t=1+r$ fails beyond uncertainty, check calibration and reference planes before considering magnetic, coupled, or finite-thickness models.

## 9.5.3 Measurement error and fabrication tolerance

**Copper surface roughness** on the skin-depth scale can affect loss. The ratio $R_q/\delta_s$ alone does not determine a correction factor. **Permittivity tolerance** shifts resonance in the simple $f_0\propto1/\sqrt{\varepsilon_r}$ model. **Solder and pad parasitics** alter $L$, $C$, and cell phase. Report coupon averages and cell-to-cell variation separately.

$$
\frac{\Delta f_0}{f_0}\simeq-\frac12\frac{\Delta\varepsilon_r}{\varepsilon_r}.
$$

| Method | Target quantity | Scope |
| --- | --- | --- |
| NRW | $n_{\rm eff}$, $\varepsilon_{\rm eff}$, $\mu_{\rm eff}$ | Slab of specified thickness, with branch and reference checks |
| Surface impedance | $R_s$, $X_s$, and phase | Grounded thin surface, sensitive to reference plane |
| Waveguide | Modal $S_{11}$ and $S_{21}$ | Controlled fixture and small sample, for a specified geometry and mode |
| Calibrated free space | Reflection or transmission pattern | Variable angles, with alignment, echo reduction, and calibration |

## Worked problem on three models for three samples

::::{admonition} Try it first
:class: book-exercise

For normal incidence in air, slab A with $d=10\,\mathrm{mm}$ at $10\,\mathrm{GHz}$ has $S_{11}=0.28012+i0.13032$ and $S_{21}=-0.40447+i0.74749$. An independent propagation reference gives $-144^\circ$ at $6\,\mathrm{GHz}$. Phase decreases continuously to $10\,\mathrm{GHz}$, crossing $-180^\circ$ once. For grounded surface B at $28\,\mathrm{GHz}$, $S_{11}=-i0.50$ and $S_{21}\simeq0$. For sheet C at that frequency, $r=-0.40-i0.20$ and $t=0.60-i0.20$. Sample B has $\varepsilon_r=3.50\pm0.05$ and $Q_L=150$. With $\eta_0\simeq377\,\Omega$, retrieve each model and evaluate resonance sensitivity.

```{dropdown} Show the full worked answer

### 1. Slab A and branch selection

$$
X\simeq2.60,\quad \Gamma=2.60\pm2.40,\quad
\Gamma_{\rm passive}\simeq0.20,\quad z_{\rm eff}\simeq1.50,\quad
T\simeq-0.450+i0.7794.
$$

$\lvert T\rvert\simeq0.90$ and principal phase is $+120^\circ$. With $k_0d=2\pi/3$, using principal phase alone gives $n'\simeq-1$. The $-144^\circ$ anchor and decreasing phase require $m=-1$ and $\arg T+2\pi m=-240^\circ$.

$$
n_{\rm eff}\simeq2.00-i0.0503,\qquad
\varepsilon_{\rm eff}\simeq1.333-i0.0335,\qquad
\mu_{\rm eff}\simeq3.00-i0.0755.
$$

Both branches have the same $\lvert T\rvert$. The phase exceeds $180^\circ$ even at $d=\lambda_0/3$. Substitute back into the slab model to reconstruct $S_{11}$ and $S_{21}$. This checks the inversion. Test homogenization against additional frequencies, thicknesses, or angles.

### 2. Grounded surface B input impedance

$$
Z_s=377\frac{1-i0.50}{1+i0.50}
=377\frac{0.75-i1.00}{1.25}
=226.2-i301.6\,\Omega.
$$

The real part is positive and the reactance capacitive. This result includes patch, substrate, and ground. Since $R_s\ne0$, the lossless phase formula does not apply. With no other channels and zero transmission, $1-\lvert S_{11}\rvert^2=75\%$ is absorption. With diffraction or cross-polarization, this is the share not returned to the measured channel.

### 3. Sheet C admittance

The data satisfy $t=1+r$. For unit incident field, $J_s=(1-r-t)/\eta_0$ and sheet field is $t$. Thus

$$
\frac{1}{t}=\frac{0.60+i0.20}{0.60^2+0.20^2}=1.50+i0.50,\quad
Y_s=\frac{1+i}{377}\,\mathrm S\simeq(2.65+i2.65)\,\mathrm{mS},\quad
Z_s\simeq188.5-i188.5\,\Omega.
$$

This $Z_s$ is the ratio of field to current on the sheet itself. The grounded model describes the input seen at its own reference plane.

### 4. Resonance error budget

$$
\lvert\Delta f_0\rvert\simeq\frac{28\,\mathrm{GHz}}2\frac{0.05}{3.50}=200\,\mathrm{MHz},\qquad
\Delta f_{\rm res}\simeq\frac{28\,\mathrm{GHz}}{150}=187\,\mathrm{MHz}.
$$

Increasing permittivity lowers resonance. The estimated shift is comparable to the linewidth. If much of the field resides in air, the sensitivity can be lower. Determine it by a numerical sweep or measurement.

| Factor | Check |
| --- | --- |
| Reference plane | A $0.5\,\mathrm{mm}$ offset at $28\,\mathrm{GHz}$ gives about $33.6^\circ$ round-trip error. Check reference position first. |
| Copper roughness | $\delta_s\simeq0.40\,\mu\mathrm m$, so $1$ to $2\,\mu\mathrm m$ roughness is substantial. Assess loss independently. |
| Solder and pad parasitics | Measure several assembled coupons to distinguish systematic bias from cell-to-cell spread. |
```
::::
