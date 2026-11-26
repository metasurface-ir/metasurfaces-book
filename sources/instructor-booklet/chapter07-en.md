# 7. Active, tunable and intelligent metasurfaces

## 7.1 Introduction and the need to move from static to dynamic surfaces

Instructor booklet, pages 174–175.

In previous chapters we saw how metasurfaces transformed control of electromagnetic waves by manipulating subwavelength discontinuities in phase, amplitude, and polarization. The surfaces considered so far belonged to the class of static or passive metasurfaces. Their metal patch geometry, gap dimensions, and dielectric substrate properties are fixed during fabrication.

Once manufactured, a static metasurface has a fixed response. For example, if it was designed to steer a beam to $+30^\circ$, it cannot command that beam to move to $-45^\circ$ under the same illumination and operating conditions unless the structure itself is rotated or replaced.

## 7.1.1 Intrinsic limitations of static metasurfaces

1. **Inflexibility in dynamic environments.** Modern communication systems, such as advanced fifth-generation and sixth-generation systems, serve moving users. A static surface cannot track a moving beam target.
2. **Limited bandwidth at high efficiency.** Energy conservation and Bode–Fano matching constraints limit the bandwidth over which a passive resonant reflector supplies a full $360^\circ$ phase range.
3. **Symmetric reciprocal transmission.** Under Lorentz reciprocity, a linear time-invariant structure made of reciprocal materials has equal forward and reverse transmission ($S_{12}=S_{21}$). In passive systems, one way to break this symmetry is to use magnetically biased materials such as ferrites.

:::{note} Scientific note on the booklet
A static device cannot change its response on command, but it can be fabricated to support several beams or functions. Passivity does not imply reciprocity. The third point specifies reciprocal materials and presents ferrites as one route, correcting the printed absolute claim. Compare scattering parameters for consistently normalized modes.
:::

## 7.1.2 A new horizon: dynamic and active metasurfaces

Active and reconfigurable metasurfaces were developed to address these challenges. The fundamental idea is simple but transformative:

> If an external control signal can change each unit cell's electromagnetic properties in real time, such as its reflection phase, transmission coefficient, or surface impedance, the whole panel can be redefined in software.

With this capability, a single panel can act as a beamformer at one moment, an absorber at another, and a communication data modulator at a third.

## 7.1.3 Classifying dynamic metasurfaces

Scientific papers and books use several terms for these surfaces. The terms are sometimes interchanged, although they describe different structures and capabilities.

| Class | Definition and main characteristic | Typical speed listed in the booklet | Application example |
| --- | --- | --- | --- |
| Tunable | Change a physical parameter continuously or in steps across the whole sheet or in groups, without independent element control | Milliseconds to seconds | Voltage- or temperature-tuned frequency filters |
| Reconfigurable | Independently address each unit cell online, with discrete or continuous control, to change the surface function | Nanoseconds to microseconds | Reconfigurable intelligent surfaces (RIS) and array beam scanning |
| Time-varying | Rapid periodic modulation of a surface property such as $Z_s(t)$ at a frequency on the order of the carrier frequency or below | Subnanoseconds to nanoseconds | Breaking Lorentz reciprocity and frequency shifting |
| Smart or AI-driven | Embedded sensors, integrated control circuitry, and AI algorithms for deciding autonomously without an external command | Processor-dependent, on the order of milliseconds | Adaptive camouflage and automatic beam steering toward an unknown transmitter |

:::{note} Timescales and the meaning of active
These are illustrative timescales. A single element can switch much faster than a complete panel can load a new pattern and settle. A bias circuit alone does not imply RF power gain.
:::

## 7.1.4 Main areas of application

Industry and academic research have accelerated the transition toward active metasurfaces for several reasons.

1. **Next-generation networks with reconfigurable intelligent surfaces (RIS / IRS).** Turn a random, obstructed, unpredictable propagation channel into a programmable smart radio environment. A RIS on a building wall can redirect waves toward users behind concrete obstacles.
2. **Next-generation solid-state phased-array radar.** Replace heavy rotating mechanical systems for angular scanning with thin, lightweight, low-cost programmable surfaces.
3. **Direct space-to-aircraft and low-Earth-orbit (LEO) links.** Use millimetre-thick flat antennas on aircraft and vehicles for real-time tracking of Starlink satellites without moving mechanical parts.
4. **Ultrafast modulators on photonic and terahertz chips.** Use optical excitation or phase-change materials to switch and modulate optical and terahertz signals at terabit-per-second data rates.

:::{note} From proposed application to working device
These are the application motivations described in the booklet. Coverage behind a wall, system cost, tracking, and data rate in a given design depend on the geometry, power, technology, and tests of the full link.
:::


## 7.2 Physical actuation mechanisms and elements

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


## 7.3 Digital, programmable, and coding metasurfaces

Instructor booklet, pages 181–185.

Before 2014, the prevailing approach described metasurfaces in terms of continuous material parameters such as permittivity $\epsilon$ and permeability $\mu$, or a continuous surface impedance $Z_s$. Although analytically precise, this classical approach did not connect directly to digital processing and computer science.

In a pioneering 2014 article, Tie Jun Cui and colleagues introduced coding, digital, and programmable metasurfaces. This approach linked electromagnetic physics with information theory and digital logic. [Cui and colleagues' article](https://doi.org/10.1038/lsa.2014.99)

## 7.3.1 Digital unit cells: one-bit, two-bit, and multibit

The central idea is to map continuous reflection or transmission phases onto discrete states represented as binary digits.

1. **One-bit coding.** The simplest case uses two distinct states with a $180^\circ$ or $\pi$ radian phase difference. Element ‘0’ has $\phi_0=0^\circ$, or a reference phase $\phi_{\rm ref}$, and $|R_0|\approx1$. Element ‘1’ has $\phi_1=180^\circ$, or $\Delta\phi=\pi$ from the reference, and equal magnitude $|R_1|\approx1$. In practice a designed unit cell can obtain this phase difference by switching a PIN diode or changing the reflecting patch dimensions.
2. **Two-bit coding.** To control the wavefront more precisely and avoid unwanted radiation symmetry, the resolution rises to four states with $90^\circ$ or $\pi/2$ steps. Codes ‘00’, ‘01’, ‘10’, and ‘11’ represent $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$.
3. **Multibit coding.** An $N$-bit metasurface divides phase into $2^N$ discrete, equally spaced states:

$$
\phi_m=m\frac{2\pi}{2^N},\qquad m\in\{0,1,\ldots,2^N-1\}.
$$

More bits reduce phase quantization error and can increase main-beam gain, at the cost of a more complex bias network.

## 7.3.2 The coding matrix and array theory for predicting scattering

Consider a two-dimensional array of subwavelength $D_x\times D_y$ unit cells in $M$ rows and $N$ columns. The digital coding matrix represents the state of the entire sheet:

$$
\Gamma=
\begin{bmatrix}
\gamma_{11}&\gamma_{12}&\cdots&\gamma_{1N}\\
\gamma_{21}&\gamma_{22}&\cdots&\gamma_{2N}\\
\vdots&\vdots&\ddots&\vdots\\
\gamma_{M1}&\gamma_{M2}&\cdots&\gamma_{MN}
\end{bmatrix},\qquad\gamma_{mn}\in\{0,1\}.
$$

Each cell's complex reflection coefficient is $R_{mn}=A_{mn}e^{i\phi_{mn}}$. When a normally incident plane wave illuminates the surface, the scattered far field follows from the array factor:

$$
f(\theta,\varphi)=f_e(\theta,\varphi)
\sum_{m=1}^{M}\sum_{n=1}^{N} A_{mn}
e^{i[\phi_{mn}+k_0 x_n\sin\theta\cos\varphi+k_0 y_m\sin\theta\sin\varphi]},
$$

$$
x_n=D_x(n-\tfrac12),\qquad y_m=D_y(m-\tfrac12),\qquad k_0=2\pi/\lambda_0.
$$

Here $f_e$ is the single-element radiation pattern. The indices follow the exercise's convention, with columns along $x$ and rows along $y$. Shifting the origin only changes the overall phase.

## 7.3.3 Wave behaviors for elementary coding sequences

Changing the sequence of codes on the surface can produce different electromagnetic behaviors.

1. **Periodic alternating sequence: deflection and beam splitting.** A symmetric one-bit sequence $\Gamma=[000\ldots111\ldots]$ with $L$ zeros followed by $L$ ones has spatial period $\Lambda=2LD_x$. With ideal balanced opposite coefficients the mean is zero. The Fourier expansion contains spatial harmonics $\pm2\pi/\Lambda$. For propagating first orders, the two symmetric directions satisfy

$$
\sin\theta=\pm\frac{\lambda_0}{\Lambda}=\pm\frac{\lambda_0}{2LD_x}.
$$

2. **Two-bit phase gradient: dominant single-beam steering.** With the unidirectional phase sequence ‘00, 01, 10, 11, …’, the phase pattern breaks reflection symmetry and forms the gradient $d\phi/dx=(\pi/2)/D_x$. For this gradient, the far-field sign used above gives the dominant order at

$$
\sin\theta=-\frac{\lambda_0}{4D_x}.
$$

3. **Pseudo-random sequence: radar cross-section reduction.** With an irregular arrangement of binary codes, reflected waves have irregular phases and can interfere destructively. Concentrated specular energy can spread over the hemisphere as diffuse scattering. The booklet gives $10$ to $20\,\mathrm{dB}$ as illustrative reductions. The actual reduction depends on the code, angle, band, and structure response.

:::{note} Steering-sign correction and the diffraction condition
The printed sign in the second item is positive, but the chapter's array factor and worked solution give a negative angle for a positive gradient. A dominant order does not carry all the incident power.
:::

## 7.3.4 Hardware control architecture and real-time FPGA implementation

To put these ideas into a real system with online control, use the following architecture:

1. **Decision and processing layer.** Tracking or optimization algorithms, such as a genetic algorithm or AI, compute the coding matrix.
2. **High-speed FPGA or SoC distribution layer.** The chip's parallel organization allows new code frames to be loaded at high rates.
3. **Shift registers and drivers.** Deliver control voltages to the diode cathodes and anodes at the back of the surface.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

A programmable reflecting metasurface contains $8\times8$ cells. Centre-to-centre spacing in both $x$ and $y$ is $D=10\,\mathrm{mm}$. A normally incident plane wave illuminates it at $f_0=10\,\mathrm{GHz}$. Columns run along $x$ and rows along $y$. The angle $\theta$ is measured from the normal in the $xz$ plane, positive toward $+x$.

All ideal states have unit reflection magnitude. One-bit codes 0 and 1 have phases $0^\circ$ and $180^\circ$. In the two-bit case, 00, 01, 10, and 11 have phases $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$.

| Pattern | Coding |
| --- | --- |
| A: periodic one-bit | Every row has the column sequence 0,0,1,1,0,0,1,1. |
| B: two-bit gradient | Every row has 00,01,10,11,00,01,10,11. |
| C: pseudo-random one-bit | Scatter 32 zeros and 32 ones over the sheet without repeating a specified periodic block. |

Suppose each cell has two control inputs. An FPGA sends a full frame over a single serial line at a $20\,\mathrm{MHz}$ clock. Simultaneous latching and driver settling take $1\,\mathrm{\mu s}$ after transmission.

1. If a cell's ideal phase is $130^\circ$, which states are selected by one-, two-, and three-bit coding?
2. Use the array factor to find the main beam angles for A and the dominant beam for B. How can B's direction be reversed?
3. In C, what is the reflected field exactly at broadside? Does reduced reflection in that direction mean energy was absorbed?
4. How long does it take to send and apply one frame? What do the processor, FPGA, shift register, and driver do?

```{dropdown} Show the full worked answer

### 1. From continuous phase to a digital code

A $b$-bit metasurface has $2^b$ states. For uniform states the phase step is $360^\circ/2^b$. Select the nearest state on the phase circle.

| Bits | Phase step | Nearest phase to $130^\circ$ | Phase error magnitude |
| --- | --- | --- | --- |
| One | $180^\circ$ | $180^\circ$ | $50^\circ$ |
| Two | $90^\circ$ | $90^\circ$ | $40^\circ$ |
| Three | $45^\circ$ | $135^\circ$ | $5^\circ$ |

Nearest-state rounding has a maximum error of half the phase step. More bits permit a more accurate wavefront, but the cell must realize more states with acceptable phase and amplitude. **The bit count determines the number of phase states. Their arrangement determines the beam pattern.**

### 2. Patterns A and B: why two beams in one case and one dominant beam in the other?

First compute

$$
\lambda_0=\frac{c}{f_0}=30\,\mathrm{mm},\qquad D=\lambda_0/3.
$$

In the $xz$ cut, the geometrical phase difference between adjacent columns is $\psi=k_0D\sin\theta$. The eight rows are identical for A and B, so their array factor reduces to a column sum:

$$
AF(\theta)=8\sum_{q=0}^{7}R_qe^{iq\psi},\qquad \psi=k_0D\sin\theta.
$$

The factor eight comes from the coherent sum of the eight rows. The actual far-field pattern is the array factor times the element pattern. The calculation below is for the ideal array factor.

**Pattern A: periodic one-bit code.** The column reflection coefficients are

$$
R_q=[+1,+1,-1,-1,+1,+1,-1,-1].
$$

The period is four cells, so $\Lambda=4D=40\,\mathrm{mm}$. For the first diffraction orders,

$$
\sin\theta_\pm=\pm\frac{\lambda_0}{\Lambda}=\pm\frac{30}{40}=\pm0.75,
\qquad \theta_\pm\simeq\pm48.6^\circ.
$$

The real coefficients give $AF(-\theta)=AF^*(\theta)$, producing equal magnitudes in symmetric directions. At broadside $\psi=0$ and the sum vanishes. Thus the ideal zero order or specular reflection is suppressed and two symmetric main beams appear.

:::{note} Order angle and finite-array peak
The $48.6^\circ$ value follows from the spatial period. To find the exact peak for eight columns, maximize $|AF|$ itself. Direct maximization of the given eight-column sum gives peaks near $\pm45.0^\circ$. The shift comes from the finite-aperture envelope.
:::

**Pattern B: two-bit phase gradient.** Now

$$
R_q=[1,i,-1,-i,1,i,-1,-i]=e^{iq\pi/2},
\qquad AF(\theta)=8\sum_{q=0}^{7}e^{iq(\pi/2+\psi)}.
$$

The dominant beam requires $\pi/2+k_0D\sin\theta=2\pi\ell$, with $\ell\in\mathbb Z$. For $\ell=0$,

$$
\sin\theta=\frac{-\pi/2}{k_0D}=-\frac{\lambda_0}{4D}=-0.75
\quad\Rightarrow\quad \theta\simeq-48.6^\circ.
$$

Other $\ell$ values give $|\sin\theta|>1$ and are not propagating. A positive $90^\circ$ phase step per column produces a negative beam angle. Reverse the gradient to $-90^\circ$ by repeating 00,11,10,01 to move the dominant beam to $+48.6^\circ$.

**Numerical check.** In the desired direction all 64 contributions add coherently and $|AF|=64$. At the mirror angle $+48.6^\circ$, the terms alternate in sign and $AF=0$. That ideal null at one angle does not eliminate sidelobes or real device losses.

### 3. Pattern C: eliminating broadside reflection versus absorbing energy

At broadside there is no position-dependent phase. The ideal sum is independent of where the signs are placed:

$$
AF(0)=32(+1)+32(-1)=0.
$$

Both A and C have a broadside null, but their scattering differs.

- A's periodic arrangement has distinct spatial harmonics and concentrates most scattering into two directions.
- A suitable aperiodic arrangement in C can spread scattering among more directions. Knowing only the counts of zeros and ones cannot determine peak directions or levels. Insert the **full code matrix** into the array factor.

The null comes from **destructive interference**. Amplitude errors or a departure from $180^\circ$ phase separation can turn it into a nonzero minimum. This calculation cannot specify a fixed reduction in measured reflection in decibels.

### 4. Implementation: from the code matrix to cell voltages

Each frame has two bits for each of 64 cells:

$$
N_{\rm bits}=64\times2=128\,\mathrm{bit}.
$$

The fixed interface still uses 128 bits for a one-bit pattern. Send phases $0^\circ$ and $180^\circ$ as 00 and 10. Sending one bit per cycle gives

$$
t_{\rm send}=\frac{128}{20\times10^6}=6.4\,\mathrm{\mu s},\qquad
t_{\rm update}=6.4+1.0=7.4\,\mathrm{\mu s}.
$$

| Hardware | Task |
| --- | --- |
| Processor or controller | Selects or computes the coding matrix for the requested function. |
| FPGA | Sends the bits in order and commands a simultaneous latch after the frame. |
| Shift register with output register | Stores the new frame while the outputs retain the previous pattern, then updates the outputs together. |
| Drivers | Convert logic codes to appropriate bias voltages or currents. |

Simultaneous latching matters. Updating each output as its bit arrives would expose incomplete patterns and temporarily steer the beam as the frame loads. The $7.4\,\mathrm{\mu s}$ runs from the start of an already prepared frame to settled driver outputs. It excludes computation of the matrix and any extra cell delay.

**Summary.** All three patterns used the same sheet. The periodic binary sequence created two symmetric beams. The two-bit gradient sent a dominant beam to one side. The balanced irregular code canceled broadside reflection through interference. The design chain goes from wave objective to code matrix, cell reflection coefficients, and far-field pattern.
```
::::


## 7.4 Reconfigurable intelligent surfaces (RIS / IRS) in sixth-generation communications

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


## 7.5 Time-varying metasurfaces and breaking Lorentz reciprocity

Instructor booklet, pages 190–195.

The metasurfaces considered so far, including programmable and reconfigurable ones, were treated as time-invariant in each held state. Phase and amplitude states were changed on a timescale much longer than the radio-wave period $T_0=1/f_0$, so the material properties were treated as constant during the interaction with the wave.

When properties such as permittivity $\epsilon(t)$, conductivity $\sigma(t)$, or surface impedance $Z_s(t)$ are modulated during an observation, the structure enters the time-varying or space–time coding regime. Frequency conservation, time symmetry, and the conditions for Lorentz reciprocity must then be revisited. The modulation need not be comparable to the carrier frequency to create sidebands, as the exercise shows.

## 7.5.1 Physics of time-varying systems: energy and frequency

Classical linear electromagnetics has two important translation symmetries:

1. **Spatial translation symmetry.** Symmetry along a surface conserves tangential momentum, or the tangential wave-number component. Gradient metasurfaces break this spatial symmetry and deflect beams through the generalized Snell law.
2. **Time translation symmetry.** Noether's theorem relates time translation to energy conservation. In a linear time-invariant medium, frequency channels are independent: a steady response to a single-frequency wave cannot introduce a different frequency.

Modulating the structure with period $T_m$ and angular frequency $\omega_m=2\pi/T_m$ breaks continuous time translation and allows the incident frequency to change:

$$
\omega_{\rm out}=\omega_0+n\omega_m,\qquad n=0,\pm1,\pm2,\ldots
$$

Frequency conversion can result from linear time-varying modulation and does not require a nonlinear response to the incident wave's intensity. Include the modulator's energy supply in the full energy balance.

## 7.5.2 Mathematical formulation: Maxwell's equations with time-varying conditions

With local time-varying permittivity, the constitutive relation is

$$
D(t)=\epsilon_0\epsilon_r(t)E(t).
$$

In a nonmagnetic medium without free charge or current, Maxwell's equations give the one-dimensional wave equation

$$
\frac{\partial^2E(z,t)}{\partial z^2}-\mu_0\frac{\partial^2D(z,t)}{\partial t^2}=0.
$$

The second time derivative of displacement follows by the product rule:

$$
\frac{\partial^2D}{\partial t^2}=\epsilon_0
\left[\epsilon_r(t)\frac{\partial^2E}{\partial t^2}
+2\frac{d\epsilon_r}{dt}\frac{\partial E}{\partial t}
+\frac{d^2\epsilon_r}{dt^2}E(t)\right].
$$

The time derivatives of permittivity indicate that the modulation source, or pump, can exchange energy with the electromagnetic field.

### Space–time reflection coefficient

If the reflection coefficient of a cell at $z=0$ is modulated periodically, $\Gamma(t+T_m)=\Gamma(t)$, and the Fourier expansion is

$$
\Gamma(t)=\sum_{n=-\infty}^{\infty}a_n e^{in\omega_m t},\qquad
a_n=\frac{1}{T_m}\int_0^{T_m}\Gamma(t)e^{-in\omega_m t}\,dt.
$$

For a monochromatic incident wave $E_{\rm inc}(t)=E_0e^{i\omega_0t}$, the instantaneous reflection-coefficient model gives a reflected combination of frequency harmonics:

$$
E_{\rm ref}(t)=\Gamma(t)E_{\rm inc}(t)
=E_0\sum_{n=-\infty}^{\infty}a_ne^{i(\omega_0+n\omega_m)t}.
$$

This is the basis for direct data modulation at a metasurface, where mixing can take place on the sheet without a separate conventional radio mixer.

## 7.5.3 Breaking Lorentz reciprocity

Under Lorentz reciprocity for linear time-invariant media with reciprocal constitutive relations, a consistently defined scattering matrix is symmetric ($S_{12}=S_{21}$). Transmission from mode A to mode B equals the corresponding transmission from B to A.

Traditional approaches use ferrites with an external magnetic bias. Static bias hardware may be bulky, costly, and difficult to integrate into planar circuits. Space–time-varying metasurfaces offer a route that avoids this form of magnetic bias.

### Traveling-wave modulation

If the surface property varies with time and also moves continuously along the surface like a traveling wave,

$$
Z_s(x,t)=Z_0[1+M\cos(\beta_m x-\omega_m t)].
$$

Here $\beta_m$ is modulation wave number and $\omega_m$ is angular frequency. Space–time dispersion can differ for propagation along $+x$ and $-x$:

- **Wave traveling with the modulation ($+x$).** If phase matching holds, it can couple to the pump and convert up to $\omega_0+\omega_m$.
- **Wave traveling opposite the modulation ($-x$).** The matching condition differs. Depending on the design, the wave may reflect or convert to a lower frequency.

This asymmetry can give $S_{21}\ne S_{12}$ for a pair of corresponding channels. In a time-varying system, specify the frequency and mode at each port before comparing them.

:::{note} What follows from a traveling pump
Up- or down-conversion does not follow from the direction of travel alone. Frequency and momentum matching, modal overlap, polarization, and coupling set the actual paths. The exercise tests reciprocity for two specified channels in the reflection model.
:::

## 7.5.4 Nonreciprocal devices based on space–time metasurfaces

These structures offer a way to design planar high-frequency devices without a magnet:

1. **Optical and radio isolators.** Pass the signal in one direction, for example from a transmitter to an antenna, while suppressing reflection back to the source. The ideal targets are $|S_{21}|\approx1$ and $|S_{12}|\approx0$.
2. **Nonmagnetic circulators.** Three-port devices for radar or in-band full-duplex communications direct the transmitter to the antenna and the returning antenna wave to the receiver while isolating the sensitive receiver from transmit power.
3. **Planar parametric amplifiers.** Transfer energy from the modulation source to a weak radio wave without a conventional transistor amplifier in the signal path.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

A reflecting metasurface in air is illuminated at $f_0=10\,\mathrm{GHz}$. Its modulation frequency is $f_m=100\,\mathrm{MHz}=0.1\,\mathrm{GHz}$. Use the simplified model $E_{\rm ref}=\Gamma E_{\rm inc}$ in two cases.

- **Case A: uniform time modulation.**

$$
\Gamma_A(t)=0.6+0.4\cos(\Omega t),\qquad \Omega=2\pi f_m.
$$

  Illumination is normal.

- **Case B: traveling space–time modulation.**

$$
\Gamma_B(x,t)=0.6+0.4\cos(\Omega t-Kx),\qquad K=0.6k_0,\quad k_0=2\pi f_0/c.
$$

  The wave is incident in the $xz$ plane with $k_{x,\rm in}=+0.6k_0$. The sheet is sufficiently extended along $x$ to neglect edge effects.

1. Which reflected frequencies appear in A, and what are their relative amplitudes and powers? Is a nonlinear response needed?
2. In a time-varying dielectric, what extra terms appear in $\partial_t^2D$? What role does the modulation source play in the energy balance?
3. In B, find the frequency and angle of each order. Define the reverse frequency-conversion experiment and determine whether that path works in reverse.
4. How does this result relate to isolators, circulators, and parametric amplifiers?

```{dropdown} Show the full worked answer

### 1. Time modulation: sidebands without a nonlinear response

Expand the cosine:

$$
\Gamma_A(t)=0.6+0.2e^{i\Omega t}+0.2e^{-i\Omega t}.
$$

For incident wave $E_{\rm inc}=E_0 e^{i\omega_0t}$, the reflected field is

$$
E_{\rm ref}=E_0\left[0.6e^{i\omega_0t}
+0.2e^{i(\omega_0+\Omega)t}+0.2e^{i(\omega_0-\Omega)t}\right].
$$

At normal incidence and reflection, all three components have the same wave impedance in the air model. Relative power is the squared field coefficient.

| Order $n$ | Reflected frequency | Amplitude relative to $E_0$ | Share of incident power |
| --- | --- | --- | --- |
| $\mathord{-1}$ | $9.9\,\mathrm{GHz}$ | 0.2 | 4% |
| 0 | $10.0\,\mathrm{GHz}$ | 0.6 | 36% |
| $\mathord{+1}$ | $10.1\,\mathrm{GHz}$ | 0.2 | 4% |

There are no higher orders in this model because $\Gamma_A$ has only three nonzero Fourier coefficients. Doubling incident amplitude doubles all three field amplitudes. The process is therefore linear in the input signal. Frequency conversion comes from the **time-dependent reflection coefficient**.

Here $f_m$ is only one percent of $f_0$ and the sidebands still appear. The modulation need not be comparable to the carrier. What matters is that the modulation continues during the observation and the structure cannot be considered constant throughout it.

### 2. Maxwell's equations: where does the wave energy go or come from?

For a simple lossless, instantaneous dielectric with $D=\varepsilon(t)E$,

$$
\frac{\partial^2D}{\partial t^2}
=\varepsilon\frac{\partial^2E}{\partial t^2}
+2\dot{\varepsilon}\frac{\partial E}{\partial t}+\ddot{\varepsilon}E.
$$

The last two terms vanish in a time-invariant medium. The electric term in Poynting's theorem reveals the modulation's role in the energy balance:

$$
E\frac{\partial D}{\partial t}
=\frac{\partial}{\partial t}\!\left(\frac12\varepsilon E^2\right)
+\frac12\dot{\varepsilon} E^2.
$$

The final term describes energy exchange between the field and the modulation mechanism. Include the modulation source in the full balance.

The three reflected components in A sum to 44% of incident power. $\Gamma(t)$ alone cannot tell us whether the remaining 56% was absorbed, transmitted, or exchanged with the modulator. The model specifies **reflection** only.

### 3. Space–time modulation: frequency and tangential wave number both change

In B the modulation terms are proportional to $e^{\pm i(\Omega t-Kx)}$. Multiplication by the incident wave gives each order both a frequency shift and a tangential wave-number shift:

$$
f_n=f_0+nf_m,\qquad k_{x,n}=k_{x,\rm in}+nK.
$$

A propagating order in air requires

$$
|k_{x,n}|\le k(f_n)=2\pi f_n/c,\qquad
\sin\theta_n=\frac{k_{x,n}}{k(f_n)}.
$$

Use the **wave number at each order's own frequency** to calculate its angle.

| Order | Frequency | Tangential wave number | Result |
| --- | --- | --- | --- |
| $\mathord{-1}$ | $9.9\,\mathrm{GHz}$ | 0 | Propagates at broadside, $\theta_{-1}=0^\circ$ |
| 0 | $10.0\,\mathrm{GHz}$ | $+0.6k_0$ | Reflected beam at $\theta_0=\arcsin(0.6)\approx+36.9^\circ$ |
| $\mathord{+1}$ | $10.1\,\mathrm{GHz}$ | $+1.2k_0$ | $1.2k_0>1.01k_0$. Evanescent, with no far-field beam. |

The forward conversion channel connects an oblique $10\,\mathrm{GHz}$ input to a normal $9.9\,\mathrm{GHz}$ output.

**How do we define the reverse experiment?** Exchange the same two channels. Simply illuminating from the opposite angle with $10\,\mathrm{GHz}$ is a different test. Keep the modulation traveling in the same direction in both experiments.

- **Reverse input:** normally incident $9.9\,\mathrm{GHz}$ with $k_x=0$.
- **Output to test:** $10\,\mathrm{GHz}$ traveling back along the original path toward the source. Reversing propagation requires $k_x=-0.6k_0$.

Conversion from $9.9$ to $10\,\mathrm{GHz}$ uses order $+1$. Under the same modulation it supplies $+K$:

$$
k_{x,\rm out}=0+K=+0.6k_0.
$$

The wave can return to $10\,\mathrm{GHz}$, but exits in a different direction and does not return to the original channel. This is nonreciprocity of the **conversion path** in the ideal model.

Each channel is defined by **frequency and direction of propagation**. The correct comparison is between corresponding entries of a multifrequency scattering matrix. The result does not establish nonreciprocity at the carrier itself. Sidebands indicate modulation; different transmission between the exchanged channels indicates nonreciprocity.

### 4. From the example to a practical device

| Device | What does this example explain, and what remains to establish? |
| --- | --- |
| Isolator | A returning wave can be sent to another frequency or direction so that it does not reach the source. Establishing isolation requires measuring forward insertion loss and reverse rejection. A zero reverse channel alone does not establish low forward loss. |
| Circulator | Route the wave to a third port, for example $1\to2$, $2\to3$, and $3\to1$. One deflected beam illustrates routing. A complete circulator must establish all three paths. |
| Parametric amplifier | Pump energy can provide gain if transferred to the signal. Up-conversion alone does not imply amplification. Power in the desired output channel must exceed input signal power. The example's data do not show that gain. |

**Summary.** Time modulation determines which frequencies are generated. Spatial modulation determines their propagation directions. Directional motion of the modulation can prevent the same conversion path from being restored in the reverse experiment.
```
::::


## 7.6 Self-adaptive and learning metasurfaces

Instructor booklet, pages 195–199.

The reconfigurable metasurfaces studied so far depended on external computation or on continued intervention by an operator. In field applications such as interference protection, high-speed radio links to moving objects, or biosensing, the electromagnetic environment can change rapidly.

If every change requires external measurements, transmission to a central computer, heavy processing, and new control codes, processing latency can undermine real-time performance. The proposed approach integrates physical sensing and onboard processors into self-adaptive or cognitive metasurfaces.

## 7.6.1 An autonomous metasurface and its physical closed loop

A self-adaptive metasurface should sense local changes without an external command. It can observe incidence angle, polarization, frequency, power level, and even physical changes such as bending. It then makes a decision and changes its electromagnetic configuration.

A three-stage closed loop implements this:

1. **Sense.** Embed electromagnetic sensors such as RF Schottky power detectors, angle sensors that use local phase difference, polarization sensors, and near-field sampling probes.
2. **Decide.** Process the sensor signals with an embedded processor. Examples include a compact neural network on an FPGA, a low-power microcontroller, or analog neuromorphic circuitry.
3. **Act.** Generate new bias voltages for PIN diodes, varactors, graphene, or phase-change films to shape the beam. The booklet describes submicrosecond actuation as an example. Actual timing depends on loading the codes and settling the devices.

## 7.6.2 Sensor-integrated meta-atoms

A major challenge is integrating a sensor with a reflective or transmissive patch without detuning the resonance or reducing radiation gain. Two principal approaches are described:

- **Sparse sensing array.** Equip only a small fraction of cells, for example 1–5%, with RF detectors. Reconstruct the field from measurements at those points using interpolation or a statistical model.
- **Weakly coupled probing.** A small microstrip line or coupling aperture behind the radiating patch samples a small fraction of incident power, below 1% or below $-20\,\mathrm{dB}$, and delivers it to a Schottky detector under the dielectric. In an ideal system without loss, transmission, or other scattering channels, the remaining power may be reflected. A probe fraction below 1% does not by itself establish above 99% reflection.

## 7.6.3 Machine-learning architectures for intelligent metasurfaces

Optimization methods such as genetic algorithms and particle swarm optimization (PSO) may converge too slowly for a real-time deadline. A pretrained model can produce an answer in one pass, without an iterative search during operation. The booklet's $O(1)$ description applies only to the fixed number of passes for a fixed model. Inference time depends on model size and hardware.

### 1. Feedforward deep neural networks (DNN)

Train the network with an inverse mapping:

- **Input:** sensed field conditions, such as input power $P_{\rm in}$, estimated incidence angle $\theta_{\rm inc}$, and target direction $\theta_{\rm target}$.
- **Output:** the array of surface control codes, $\Gamma=[C_1,C_2,\ldots,C_N]$.

Lightweight processing cores can perform the inference. The nanosecond-to-microsecond times discussed in the booklet depend on the network, hardware, and type of computation. Whole-surface adjustment includes sensing, writing, and settling.

### 2. Deep reinforcement learning (DRL)

When a precise model of the environment is unavailable, for example after a room layout changes or an unexpected obstacle enters, define the following:

- The metasurface acts as the **agent**.
- Its **state** or observation includes received signal power.
- An **action** changes the cell phases.
- The **reward** is an improvement in SNR or data rate.

The agent can search for useful patterns through trial and error without a prior channel model. Learning does not guarantee a global optimum, convergence, or performance in a new environment.

## 7.6.4 Applications of self-adaptive metasurfaces

1. **Adaptive electromagnetic camouflage.** This proposed application senses illumination conditions and changes the scattering pattern to modify radar cross section. Performance depends on angle, frequency band, and testing of the actual device.
2. **Deformation self-compensation.** Mechanical changes alter phases on a flexible metasurface mounted on an aircraft or smart clothing. Strain gauges report the deformation to the controller, which adjusts phases to recover the focused beam.
3. **Smart radio walls.** When people or vehicles block a radio path, a metasurface wall can redirect its reflected beam toward the user. Continuity of the link must be tested under actual conditions.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

People walking through a corridor sometimes block the direct path between an access point and a user terminal. A wall-mounted $16\times16$ reflecting metasurface supplies an alternative path. The operating frequency is $10\,\mathrm{GHz}$, the cell pitch is $d=\lambda_0/2$, and each cell permits $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$. Assume equal reflection amplitude for all four states.

Only 8 of the 256 cells have sensors. Two adjacent sensors along $x$ use a coherent receiver to measure the incident phase difference. At one instant the right sensor reads $-90^\circ$ relative to the left. Assume a plane wave in the $xz$ plane. The initial aim is to reflect at broadside to the wall.

- Each probe samples $0.5\%$ of local power. Local incident power is $-30\,\mathrm{dBm}$ and the sensing receiver's minimum detectable power is $-58\,\mathrm{dBm}$.
- Sensing and feature extraction take $8\,\mathrm{\mu s}$, neural-network inference on the FPGA takes $4\,\mathrm{\mu s}$, and bias settling takes $1.6\,\mathrm{\mu s}$. Four parallel lines send data without overhead at $20\,\mathrm{Mbit/s}$ each. The characteristic channel variation time is $1\,\mathrm{ms}$.
- After the initial setting, an obstacle changes the corridor multipath. The user terminal can report SNR. To study bending, assume one cell moves $4\,\mathrm{mm}$ normal to the wall toward the space in front of it.

Find the incident angle and initial phase code. Evaluate the probe power budget and loop latency. Compare pretrained inference with learning from receiver feedback. Find a phase correction for the displaced cell.

```{dropdown} Show the full worked answer

### 1. Sparse sensing: from phase difference to incidence angle

First find the fraction of instrumented cells:

$$
\frac{8}{256}\times100=3.125\%.
$$

The sensing array is sparse. In the single-plane-wave model we need not measure the field at all 256 cells to find the $x$ slope. Define the incident angle by $k_{x,\rm inc}=k_0\sin\theta_{\rm inc}$, so a positive angle means positive tangential wave number. The right-minus-left phase is

$$
\Delta\phi_{\rm sense}=-k_{x,\rm inc}d=-k_0d\sin\theta_{\rm inc}.
$$

With $d=\lambda_0/2$, $k_0d=\pi$, hence

$$
-\pi/2=-\pi\sin\theta_{\rm inc}
\quad\Rightarrow\quad \theta_{\rm inc}=+30^\circ.
$$

The calculation uses **coherent phase measurement**. A power detector alone cannot measure relative phase. With several simultaneous incident waves, one pair's phase difference may not identify the direction of any one wave. More sensors and a suitable estimation model are then needed.

### 2. Weakly coupled probe: is the sample measurable?

Power coupling is $0.005$:

$$
10\log_{10}(0.005)\simeq-23.0\,\mathrm{dB},\qquad
P_{\rm sample}=-30-23.0=-53.0\,\mathrm{dBm}.
$$

Ignoring extra path loss, this is about $5\,\mathrm{dB}$ above the stated threshold. The power budget permits sampling. Precise angle estimation also requires phase accuracy and calibration of the two channels.

Weak coupling does not guarantee $99.5\%$ reflected power. The $0.5\%$ describes only the probe's share. Material loss, bias circuitry, and other scattering channels are excluded. **Sparse sensing** reduces the number of instrumented cells; **weak coupling** limits the power sampled at each instrumented cell.

### 3. Decide and act: how is the beam redirected to broadside?

At $x_m=md$, the incident wave has phase $-k_{x,\rm inc}x_m$. The surface compensates the incident slope so that the columns add coherently at broadside:

$$
\Delta\phi_{\rm act}=k_{x,\rm inc}d=\pi\sin30^\circ=\pi/2.
$$

Set the first column to zero, then repeat $[0^\circ,90^\circ,180^\circ,270^\circ]$ four times over sixteen columns. No $y$ gradient is needed, so use the sequence in all sixteen rows. In this case there is no phase-rounding loss, because all required phases already belong to the two-bit codebook. Other angles do not necessarily share this property.

This simple geometry gives an analytical code without a neural network. The response can be a **benchmark for the pretrained network**: from estimated angle, sensed power, and target direction, it should produce a code with similar performance. Calibration data can help because actual cell phases and mutual interactions may differ from the ideal model. Inference avoids an iterative run-time search, but its cost depends on model size and hardware. The $4\,\mathrm{\mu s}$ figure is an assumption for this implementation.

### 4. Loop latency: network speed versus system speed

Four states require two bits per cell, or 512 bits. The aggregate line rate is $80\,\mathrm{Mbit/s}$:

$$
t_{\rm load}=\frac{512}{80\times10^6}=6.4\,\mathrm{\mu s}.
$$

With sequential stages, time from sensing to a settled surface is

$$
\begin{aligned}
t_{\rm loop}&=t_{\rm sense}+t_{\rm decide}+t_{\rm load}+t_{\rm settle}\\
&=(8+4+6.4+1.6)\,\mathrm{\mu s}=20\,\mathrm{\mu s}.
\end{aligned}
$$

This is 2% of the $1\,\mathrm{ms}$ channel timescale, so local adjustment is faster than the changes specified. Periodic sensing adds the wait until the next sample. If decisions depend on a user report, include report transmission and reception time separately. A $20\,\mathrm{\mu s}$ local loop does not guarantee uninterrupted communication.

### 5. Learning from feedback: when the incident angle is insufficient

After blockage, the wave reaching the wall may still arrive at about $30^\circ$, while the wall-to-user path changes. A controller that observes only the incident angle might retain the old code despite falling SNR. This is why receiver feedback matters.

Suppose the controller can try three preselected codes. The **action** is choosing a code, and the **observation** can include estimated angle and latest reported SNR. Define reward as SNR improvement over the reference code under the same channel conditions.

| Tested code | Reported SNR | Reward relative to reference |
| --- | --- | --- |
| A: reference | $8\,\mathrm{dB}$ | $0\,\mathrm{dB}$ |
| B: first alternative | $12\,\mathrm{dB}$ | $+4\,\mathrm{dB}$ |
| C: second alternative | $7\,\mathrm{dB}$ | $-1\,\mathrm{dB}$ |

If the channel remains approximately constant during the trials, B is the best **among the tested options**. Update estimated scores as new rewards arrive so one noisy observation does not determine the decision. If B's previous score was 2 and update rate $\alpha=0.5$,

$$
Q_{\rm new}(B)=Q_{\rm old}(B)+\alpha[r_B-Q_{\rm old}(B)]
=2+0.5(4-2)=3.
$$

This is a simple selection and feedback-learning exercise. In a larger problem a network can estimate code values or a selection policy from observations. A **pretrained network** proposes a code from sensed conditions. **Feedback learning** measures what the code actually did to the current link. The controller still decides, and the reported SNR is a measurement rather than a surface command.

### 6. Bending compensation: from measured displacement to phase correction

At $10\,\mathrm{GHz}$ the wavelength is about $30\,\mathrm{mm}$. Suppose strain sensors and a calibrated mechanical model estimate $\delta z=+4\,\mathrm{mm}$. Displacement outward shortens both the incident and outgoing paths. A shorter path increases the received phase:

$$
\begin{aligned}
\Delta\phi_{\rm geom}
&=k_0\delta z(\cos\theta_{\rm inc}+\cos\theta_{\rm out})\\
&=\frac{360^\circ}{30\,\mathrm{mm}}(4\,\mathrm{mm})(\cos30^\circ+\cos0^\circ)
\simeq+89.6^\circ.
\end{aligned}
$$

Add about $-89.6^\circ$ to the original cell phase. The nearest two-bit correction is $-90^\circ$, one state backward. For example, $180^\circ$ becomes $90^\circ$. The residual phase error is about $0.4^\circ$. This calculation treats only the **geometrical displacement**. Phase correction alone is insufficient if bending also rotates the patch, detunes resonance, or changes reflection amplitude.

**Summary.** Surface sensors estimated the incident direction. The controller applied a reflection code in time. User feedback revealed whether the code improved the link. The same architecture can convert mechanical sensor data into phase corrections. Its success depends on observability, whole-loop speed, and an appropriate feedback criterion.
```
::::


## 7.7 Research directions, open challenges, and Chapter 7 summary

Instructor booklet, pages 199–202.

Active, tunable, and intelligent metasurfaces are changing rapidly. Topics previously considered as electromagnetic theory or laboratory proofs of concept have moved toward commercialization in wireless communications, phased-array radar, and all-optical processing. This section reviews research directions that can motivate graduate theses and follow-on study.

## 7.7.1 Emerging research and topics for further study

### 1. Transmitting and reflecting surfaces, and active surfaces (STAR-RIS / Active RIS)

**Problem context.** Conventional passive RIS can consume relatively little power but, in the two-hop far-field model, experience cascaded path loss $P_r\propto(d_1d_2)^{-2}$. A reflection-only surface cannot serve users behind it on a transmitted path.

**Research directions:**

- **STAR-RIS or intelligent omni-surfaces.** Cells reflect some power and transmit some to enable coverage on both sides. Protocols include energy splitting (ES), partitioning elements by mode (MS), and time switching (TS). Independent transmission and reflection phases are a modeling assumption that can be limited in passive hardware by coupling and power constraints. [STAR protocols](https://arxiv.org/abs/2104.01421) · [Coupled phase model](https://arxiv.org/abs/2110.02374)
- **Low-power active RIS.** Embed low-noise amplifiers (LNAs) or other gain elements at the cells to reduce the effect of cascaded path loss without a complete conventional phased-array transmitter and receiver. Account for bias, noise, and amplifier stability.

### 2. Analog electromagnetic computing and in-place optical deep learning

**Problem context.** Moving data continuously between memory and processor in the von Neumann architecture can cost substantial energy and time.

**Research direction.** Programmable metasurfaces can act as physical neural layers. Instead of a matrix multiplication in a digital computer, waves pass through diffractive layers and implement operations such as spatial differentiation, an analog Fourier transform, solution of a class of integro-differential equations, or image classification. The booklet points to diffractive deep neural networks ($D^2NN$). Wave propagation is fast, and a passive layer may use little control energy. Near-zero consumption for the element does not apply to the complete system including its source, detectors, and readout.

### 3. Radiative near-field effects and focusing with extremely large-scale RIS (XL-RIS)

**Problem context.** Enlarging the physical aperture for higher gain increases the Rayleigh far-field boundary

$$
r_{\rm Rayleigh}=\frac{2D^2}{\lambda_0}
$$

from a few metres toward tens or hundreds of metres in large examples. Receivers and obstacles then lie in the radiative near field (Fresnel region).

**Research directions:**

- Replace plane waves with spherical wavefronts.
- Move from angular beam steering to three-dimensional beam focusing. The focus has a radial distance $R$ as well as an angle. This can enable denser spatial multiplexing. Verify separation and interference for the actual aperture, bandwidth, and users.

### 4. Space–time metasurfaces and direct data transmitters

**Problem context.** Heterodyne architectures and conventional transmitters use mixers, filters, and digital-to-analog converters (DACs), which can occupy space and draw power.

**Research direction.** A time-switched metasurface can modulate RF directly. A sinusoidal carrier illuminates it, and phase or amplitude switching puts QPSK, 16‑QAM, or FSK on the scattered wave. The booklet mentions nanosecond switching and the possibility of removing more than 70% of RF-chain blocks for such architectures. This percentage was not measured in the chapter and depends on the reference architecture, sidebands, control circuits, and full system. Frequency conversion also occurs in the linear time-varying model of Section 7.5.

### 5. Sustainability and energy harvesting for self-powered surfaces

**Problem context.** Deploying very large numbers of diode cells in cities may require extensive DC wiring or periodic battery replacement, challenging environmental and economic sustainability.

**Research direction.** Hybrid cells can shape the information beam while converting some ambient RF or light into DC using RF harvesting or small transparent solar cells. The goal is to supply some control and FPGA energy. Compare harvested power with the actual whole-circuit budget.

## 7.7.2 Open technical challenges and industrial bottlenecks

Moving from ideal simulation to a working prototype exposes several engineering problems:

1. **DC bias lines and unwanted interference.** Feeding thousands of diodes requires dense copper traces. Poorly designed lines can act as parasitic antennas that alter resonance and radiation. High-RF-impedance bias lines or buried multilayer vias are options to investigate.
2. **State-dependent mutual coupling.** Switching one cell changes local loading and neighboring surface currents. Actual amplitudes and phases can therefore differ from the local periodic approximation (LPA).
3. **Real-time channel estimation with low pilot overhead.** Passive cells cannot separate their own cascaded signals. When suitable structure exists, designed pilots, compressed sensing, and machine learning can help estimate the control channel.

## 7.7.3 Comparison of intelligent metasurface mechanisms and architectures

This table collects the main features considered in Chapter 7. Response times are qualitative examples from the booklet and need not describe the same measurement or level of integration across technologies.

| Technology | Response or modulation speed | Power | Physical mechanism | Main advantage | Main limitation |
| --- | --- | --- | --- | --- | --- |
| PIN diode | Fast, on the order of nanoseconds | Moderate ON-state DC | Resistance and capacitance switching | Mature, low-cost industrial design | Discrete states and static power |
| Varactor diode | Moderate, on the order of microseconds for system tuning in this comparison | Very low reverse leakage | Continuous change of junction capacitance | Continuous phase, with $0$ to $360^\circ$ a suitable cell-design objective | $Q$ degradation at high frequency and high-power nonlinearity |
| $\mathrm{VO_2}$ | Picoseconds to nanoseconds for the fast transition | High for thermal stabilization | Insulator-to-metal transition | Strong terahertz and optical response | Volatility, heating, and intermediate ohmic loss |
| GST | Tens of nanoseconds | Zero while holding state | Amorphous-to-crystalline transition | Stable nonvolatile memory | Limited cycling and high reset pulse |
| Graphene | Very fast intrinsic response, subpicosecond | Low | Gate field changes Fermi level | Terahertz tunability and flexibility | Film uniformity and quality over large areas |
| Space–time modulation | Depends on pump frequency | Depends on the switching hardware | Breaks time symmetry, for example $d\epsilon/dt\ne0$ | Potential nonreciprocity and mixer-free modulation | Unwanted harmonics and power efficiency |
| Self-adaptive or AI-driven | Microseconds in an implementation dependent on network and hardware | Moderate to high processor power | Closed-loop sensing, decisions, and actuation | Autonomous decisions | Sensor–antenna coupling and circuit integration |

## 7.7.4 Chapter 7 summary

We followed metasurfaces from static devices to dynamic, time-varying, and autonomous systems.

- Microwave diodes and emerging materials such as phase-change media and graphene change a fixed electromagnetic response.
- Digital coding formulates how matrices of zeros and ones rearrange waves in space.
- Reconfigurable intelligent surfaces alter radio channels and can help build smart radio environments.
- Space–time variation adds the time dimension and can produce nonreciprocity in specified channels without a magnetic bias.
- Integrating local sensing and deep networks gives a route to self-adaptive and cognitive metasurfaces.
