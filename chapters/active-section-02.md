# 7.2 Physical actuation mechanisms and elements

Instructor booklet, pages 175–181.

To turn a static structure into a dynamic metasurface, we must change each cell's local surface impedance ($Z_s=R_s+iX_s$) or boundary conditions through an external control signal. Physically there are two main routes:

1. **Integrate lumped semiconductor components.** Load resonator gaps with PIN diodes, varactors, or transistors.
2. **Use tunable or responsive materials.** Use materials whose local permittivity $\epsilon$ or conductivity $\sigma$ changes under voltage, temperature, light, or mechanical stress, such as liquid crystals, graphene, and phase-change materials.

This section examines how these technologies work, their equivalent circuits, their advantages, and their limitations.

## 7.2.1 Solid-state electronic tuning

One of the most common and developed methods in the microwave and millimetre-wave bands up to about $40\,\mathrm{GHz}$ is to use integrated semiconductor components.

### 1. PIN diodes (discrete phase switching)

The PIN diode is widely used in digital coding metasurfaces. It offers two distinct operating states.

- **Forward bias (ON).** The diode behaves as a small resistance $R_{\rm on}$, typically $1$ to $3\,\Omega$, in series with a small parasitic inductance $L_{\rm on}$ on the order of a fraction of a nanohenry.
- **Reverse bias (OFF).** The diode behaves as a small capacitance $C_{\rm off}$, typically $0.02$ to $0.1\,\mathrm{pF}$, in parallel with a large resistance $R_{\rm off}>10\,\mathrm{k\Omega}$.

Switching between ON and OFF shifts the unit-cell resonance and creates a discrete phase step at the operating frequency, commonly designed to be $180^\circ$ for one-bit coding.

- **Advantages.** Fast switching on the order of nanoseconds, simple digital control with $0\,\mathrm V/3.3\,\mathrm V$ logic, and low insertion loss.
- **Disadvantages.** ON-state DC consumption (several milliamperes of sustained current per cell can create thermal problems in arrays of thousands of elements) and high-power nonlinearity (risk of saturation and unwanted harmonics).

### 2. Varactor diodes (continuous phase tuning)

If the design requires smooth continuous phase control between $0$ and $360^\circ$ rather than discrete phases, a varactor diode can be used.

- The varactor works in reverse bias. Increasing the reverse voltage $V_{\rm rev}$ widens the depletion region, so the junction capacitance $C_v$ decreases monotonically:

$$
C_v(V)=\frac{C_0}{(1+V_{\rm rev}/V_{\rm bi})^\gamma}.
$$

Here $C_0$ is the zero-bias capacitance, $V_{\rm bi}$ the built-in junction potential, and $\gamma$ the doping-profile exponent.

- **Equivalent circuit.** A variable capacitance $C_v(V)$ in series with loss resistance $R_s$ and connection inductance $L_s$.
- **Figure of merit.** The varactor quality factor,

$$
Q=\frac{1}{2\pi f C_v R_s}
$$

falls at high frequencies and can reduce reflection magnitude at particular phases.

- **Advantages.** Continuous phase adjustment with no steps and nearly zero steady DC consumption (leakage current on the order of nanoamperes).
- **Disadvantages.** A multichannel analog voltage network with DACs, sensitivity to bias-line voltage noise, and a more limited operating range than PIN switches in some designs.

## 7.2.2 Phase-change materials

Moving from microwaves toward terahertz and optical frequencies shrinks cells to a few micrometres or a few hundred nanometres. Conventional soldering or placement of discrete elements is impractical at these dimensions. Phase-change materials enter as integrated thin films.

### 1. Vanadium dioxide ($\mathrm{VO_2}$)

Vanadium dioxide exhibits a thermally driven insulator-to-metal transition.

- **Transition mechanism.** At room temperature, $\mathrm{VO_2}$ has an insulating monoclinic structure and low conductivity ($\sigma\approx10\,\mathrm{S/m}$). Above a critical temperature $T_c\approx68^\circ\mathrm C$, it transitions to metallic rutile and conductivity rises by four to five orders of magnitude ($\sigma\approx10^5$ to $10^6\,\mathrm{S/m}$).
- **Excitation approaches.** Direct heating, local Joule heating with a voltage pulse, or ultrafast optical laser pulses.
- **Applications.** Switchable terahertz absorbers and ultrafast optical switches.

### 2. Chalcogenide alloys ($\mathrm{GST:Ge_2Sb_2Te_5}$)

Germanium–antimony telluride alloys are nonvolatile, whereas $\mathrm{VO_2}$ is volatile.

- After switching between amorphous (low refractive index and optical transparency) and crystalline (higher refractive index and conductive loss) states, the material requires no external energy source to retain its state.
- Switching uses nanosecond laser or electrical pulses. A short, high-power pulse melts and rapidly quenches the film to amorphize it. A longer, moderate pulse anneals it to the crystalline state.

## 7.2.3 Two-dimensional materials: graphene metasurfaces

Graphene, a single atomic layer of $sp^2$-hybridized carbon, offers distinctive tunability in the terahertz and far infrared bands.

### 1. Kubo surface conductivity

The complex graphene conductivity $\sigma_g=\sigma_{\rm intra}+\sigma_{\rm inter}$ follows from the Fermi–Dirac distribution. When intraband conductivity dominates at terahertz frequencies,

$$
\sigma_{\rm intra}(\omega,\mu_c,\Gamma,T)
\simeq
\frac{-i e^{2}k_BT}{\pi\hbar^{2}(\omega-i2\Gamma)}
\left[\frac{\mu_c}{k_BT}+2\ln\!\left(1+e^{-\mu_c/(k_BT)}\right)\right].
$$

Here $\mu_c$ is the graphene chemical potential and $\Gamma=1/(2\tau)$ is the carrier scattering parameter for relaxation time $\tau$.

:::{note} Conductivity correction
The equation printed on page 177 omits the imaginary prefactor and has the opposite sign on the damping term. The expression above matches Chapter 1's time convention and has nonnegative real and negative imaginary parts in the lossy intraband limit. [Hanson's Kubo conductivity expression](https://doi.org/10.1063/1.2891452)
:::

### 2. Electrostatic tuning

Applying external gate bias $V_g$ between graphene and a conductor changes the carrier density and shifts chemical potential:

$$
|\mu_c|\approx\hbar v_F\sqrt{\pi|n_s|}
\approx\hbar v_F\sqrt{\frac{\pi\epsilon_d|V_g-V_{\rm Dirac}|}{e\,d}}.
$$

The capacitor approximation uses the absolute gate-dielectric permittivity $\epsilon_d$ and thickness $d$. Changing $\mu_c$ from zero to roughly $1\,\mathrm{eV}$ can shift graphene from dielectric-like behavior toward metal-like behavior capable of supporting surface plasmon polaritons (SPPs). This property enables compact terahertz lenses and phase shifters.

## 7.2.4 Comparing actuation technologies

The table summarizes engineering criteria for choosing an actuation mechanism. The ranges are illustrative values from the booklet and depend on the component, excitation method, and integration.

| Mechanism | Frequency range | Switching time | DC consumption | Volatility | Main advantage | Main challenge |
| --- | --- | --- | --- | --- | --- | --- |
| PIN diode | Microwave to Ka band, below $40\,\mathrm{GHz}$ | 1–50 ns | ON-state milliwatts per cell | Volatile | Mature and inexpensive | Power in large arrays |
| Varactor | Microwave, below $20\,\mathrm{GHz}$ | 10–100 ns | Very small, on the order of nanowatts | Volatile | Continuous phase control | High-frequency $Q$ degradation |
| Liquid crystal | Millimetre wave to terahertz, above $60\,\mathrm{GHz}$ | 1–100 ms | Near zero | Volatile | Low cost, integrated fabrication | Slow response |
| $\mathrm{VO_2}$ phase change | Terahertz to optical | Subpicosecond to nanosecond | Active drive required | Volatile | Large modulation depth | Operating temperature and hysteresis |
| GST phase change | Infrared to optical | 10–500 ns | Zero while holding state | Nonvolatile | Retains state without power | Limited switching endurance |
| Graphene | Terahertz and far infrared | Picoseconds | Very small | Volatile | Nanoscale dimensions, gate tuning | Limited optical coupling efficiency |

## Problem statement

::::{admonition} Try it first
:class: book-exercise

An indoor communications system uses a reflecting metasurface at $10\,\mathrm{GHz}$. The wave is normally incident, and the surface must redirect the reflected beam from $+30^\circ$ to $-45^\circ$ in under $1\,\mathrm{ms}$. Angles are measured from the surface normal in the $xz$ plane.

The metasurface has $32\times32$ cells, spaced $p=7.5\,\mathrm{mm}$ centre to centre. Two microwave-cell options are proposed.

| Option | Problem data |
| --- | --- |
| PIN diode | Two reflection states with almost equal magnitudes and phases $0^\circ$ and $180^\circ$. Each ON cell draws $5\,\mathrm{mA}$ from a $3.3\,\mathrm V$ source. |
| Varactor diode | $C_0=1\,\mathrm{pF}$, $V_{\rm bi}=1\,\mathrm V$, $\gamma=0.5$, and series resistance $R_s=1\,\Omega$. The reverse bias is adjustable. |

The group has three related projects: a **terahertz switch that returns to its initial state after excitation is removed**, an **infrared pixel that retains its state with the power off**, and a **terahertz phase shifter continuously controlled by gate voltage**.

1. Why cannot a static metasurface meet the link requirement? Find the adjacent-column phase difference for both beam directions.
2. Code the first four columns for both directions with PIN diodes. What DC power is drawn if half the array cells are ON? What beam-steering limitation follows from one-bit coding?
3. Find varactor capacitance and quality factor at zero, $3$, and $8\,\mathrm V$ reverse bias. Do these data establish a full $360^\circ$ of reflection phase control?
4. How do beam switching, time modulation, and adaptive control differ? If the surface impedance is modulated at $1\,\mathrm{MHz}$, where do the first sidebands appear?
5. Choose from $\mathrm{VO_2}$, GST, graphene, and liquid crystal for the three related projects. Explain each choice.

```{dropdown} Show the full worked answer

### 1. Why must the surface be reconfigurable?

A static surface may be designed to generate several beams, but under fixed illumination it cannot change the phase pattern on command and move a beam from one user to another. The main difference between the two desired directions in this problem is the **phase gradient on the surface**.

The free-space wavelength is

$$
\lambda_0=\frac{c}{f}=\frac{3\times10^8}{10^{10}}=30\,\mathrm{mm},
\qquad p=\frac{\lambda_0}{4}.
$$

If column $q$ has reflection phase $\phi_q$, its far-field contribution toward $\theta_r$ is proportional to $e^{i(\phi_q+k_0qp\sin\theta_r)}$. To align every column in the desired direction,

$$
\Delta\phi=\phi_{q+1}-\phi_q=-k_0p\sin\theta_r,\qquad
k_0p=\frac{2\pi p}{\lambda_0}=\frac{\pi}{2}=90^\circ.
$$

| Desired direction | Adjacent-column phase step |
| --- | --- |
| $+30^\circ$ | $-90^\circ\sin30^\circ=-45^\circ$ |
| $-45^\circ$ | $-90^\circ\sin(-45^\circ)=+63.6^\circ$ |

Changing users changes both the magnitude and sign of the phase gradient. A global bias that only adds a common phase cannot do this. This geometry requires at least separate control of the columns. Independent control of individual cells is needed to change the pattern in both surface directions.

### 2. PIN diode: simple coding, with a power cost and beam-pattern limitation

Start with zero reference phase at column $q=0$. At each column, select the nearest ideal phase on the phase circle and break a tie in favor of code 0. Codes 0 and 1 represent $0^\circ$ and $180^\circ$ respectively.

| Desired direction | Ideal phases of the first four columns | One-bit code |
| --- | --- | --- |
| $+30^\circ$ | $\mathord{(0^\circ,-45^\circ,-90^\circ,-135^\circ)}$ | $[0,0,0,1]$ |
| $-45^\circ$ | $\mathord{(0^\circ,+63.6^\circ,+127.3^\circ,+190.9^\circ)}$ | $[0,0,1,1]$ |

The ON diode is approximately a small resistance with series parasitic inductance. The OFF diode is approximately a small capacitance with large leakage resistance. Changing the electrical load changes the resonator response. A $180^\circ$ phase difference is not intrinsic to the diode. The problem assumes a cell designed to provide it at $10\,\mathrm{GHz}$.

With half of the $1024$ cells ON,

$$
N_{\rm ON}=512,\qquad I_{\rm DC}=512(5\,\mathrm{mA})=2.56\,\mathrm A,\qquad
P_{\rm DC}=3.3(2.56)\approx8.45\,\mathrm W.
$$

This is power drawn from the bias supply. Some may be dissipated outside the diodes, and additional controller consumption is excluded. Meeting the $1\,\mathrm{ms}$ limit requires sending the code, updating the drivers, and settling the complete array in time.

**Important one-bit limitation.** Under normal incidence, equal magnitudes, and exactly $0^\circ$ and $180^\circ$ phases, cell reflection coefficients are real, proportional to $+1$ and $-1$. The array factors at $+\theta$ and $-\theta$ are therefore complex conjugates and have equal magnitudes. The code can create a beam in the desired direction, but cannot remove the mirror beam by itself. A single dominant beam on one side calls for multibit or continuous control, or another design that breaks this symmetry.

### 3. Varactor: continuously variable capacitance, with phase range set by the cell

Increasing reverse bias widens the depletion layer and lowers the junction capacitance. For the given data,

$$
C_v=\frac{C_0}{(1+V_{\rm rev}/V_{\rm bi})^{0.5}},\qquad
Q\simeq\frac{1}{2\pi f C_v R_s}.
$$

For example, at $3\,\mathrm V$,

$$
C_v=\frac{1}{\sqrt{1+3}}\,\mathrm{pF}=0.500\,\mathrm{pF},
\qquad
Q\simeq\frac{1}{2\pi(10^{10})(0.5\times10^{-12})(1)}=31.8.
$$

| Reverse bias | Capacitance $C_v$ | Approximate $Q$ at $10\,\mathrm{GHz}$ |
| --- | --- | --- |
| $0\,\mathrm V$ | $1.000\,\mathrm{pF}$ | 15.9 |
| $3\,\mathrm V$ | $0.500\,\mathrm{pF}$ | 31.8 |
| $8\,\mathrm V$ | $0.333\,\mathrm{pF}$ | 47.7 |

This $Q$ belongs to the varactor's simplified series-capacitance and resistance model. It excludes lead inductance and is not the cell $Q$.

Capacitance versus voltage cannot determine the cell phase range. Simulate or measure $S_{11}(V)$ at the operating frequency and inspect both its phase and magnitude. A state may have the desired phase but reflect so weakly that it is unusable. Even with low steady-state varactor leakage, the voltage and control circuits draw power.

**Engineering decision.** PIN control is suitable if digital simplicity is the priority and a mirror beam is acceptable. Consider a varactor or multibit PIN design for a single-sided beam with less phase error, provided the complete array meets its phase, loss, and response-time requirements.

### 4. Tuning, reconfiguration, time modulation, and adaptation

The same panel illustrates the distinction.

| Operating mode | What happens here? |
| --- | --- |
| Tunable | A common voltage shifts the resonance of every cell. |
| Reconfigurable | The controller changes the column bias pattern, then holds it. Each settled beam reflects at the carrier. |
| Time-varying | The controller intentionally modulates impedance periodically to create new frequency components. |
| Self-adaptive | The system uses feedback such as link quality or estimated user location to select a pattern. This need not require AI. |

For $f_m=1\,\mathrm{MHz}$ time modulation, the first reflected sidebands occur at $f_0\pm f_m$:

$$
f_-=9.999\,\mathrm{GHz},\qquad f_+=10.001\,\mathrm{GHz}.
$$

Steering with a fixed bias pattern is not by itself evidence of nonreciprocity. The presence of sidebands is also insufficient. Compare the responses of the corresponding forward and reverse channels.

### 5. Material choices for the three related projects

| Requirement | Choice | Reason |
| --- | --- | --- |
| Terahertz switch that resets after excitation is removed | $\mathrm{VO_2}$ | Heating can drive the insulator–metal transition and a large change in conductivity. The initial state returns after sufficient cooling past the return threshold. Account for hysteresis and cooling time. |
| Infrared pixel that retains its state without power | GST | The amorphous or crystalline state persists after excitation. Writing the state requires energy, but holding it requires no continuous drive. |
| Continuously tunable terahertz phase shifter | Graphene | Gate voltage changes carrier density, chemical potential, and complex sheet conductivity. This can tune transmission or reflection phase. The usable range also depends on cell geometry and coupling. |

To understand graphene tuning, hold the gate dielectric thickness and permittivity fixed. In the capacitor approximation,

$$
|\mu_c|\propto\sqrt{|V_g-V_{\rm Dirac}|}.
$$

Increasing distance from the Dirac bias from $1$ to $4\,\mathrm V$ approximately **doubles** $|\mu_c|$. This calculation tells us about chemical potential; it does not determine the reflection phase directly.

**When is liquid crystal a good choice?** When continuous tuning or integrated fabrication is important and millisecond or longer response is acceptable. Without measured response data it is not a confident choice for the stringent under-$1\,\mathrm{ms}$ whole-panel requirement.

**Takeaway.** Begin with the required function. Must the phase gradient change, the wave frequency shift, or the material state persist without power? Then check that changing the device or material inside the cell and array actually supplies the needed phase, magnitude, and response time.
```
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
