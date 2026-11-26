# 7.1 Introduction and the need to move from static to dynamic surfaces

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

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
