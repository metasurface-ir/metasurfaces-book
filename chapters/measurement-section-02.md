# 9.2 Microstructure fabrication and deposition

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

```{figure} ../assets/chapter-09/etch-cross-section.svg
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

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
