---
title: "2.11 Normal-incidence plane-wave reflection and transmission"
short_title: "2.11 Normal-incidence plane-wave reflection and transmission"
---

(ch02-source-11)=
# 2.11 Normal-incidence plane-wave reflection and transmission

### 2.11.1 Introduction

So far, our wave has traveled through an infinite homogeneous medium without interruption. Real optical and metasurface devices are full of boundaries. When a wave reaches a change in permittivity or permeability, it must divide its response: some energy returns to medium 1 as reflection, while some crosses into medium 2 as transmission.

Reflection and transmission underpin multilayer systems, antireflection coatings and especially metasurfaces. Our design art is to control their amplitudes, phases and polarizations. We begin with the simplest case: a plane wave normally incident on a flat interface.

### 2.11.2 Geometry and initial assumptions

Two linear, homogeneous, isotropic media meet at $z=0$. Medium 1 occupies the left half-space, $z<0$, and medium 2 the right half-space, $z>0$. Their electromagnetic properties are:

- **Medium 1:** intrinsic impedance $\eta_1$ and complex propagation constant $\gamma_1$.
- **Medium 2:** intrinsic impedance $\eta_2$ and complex propagation constant $\gamma_2$.

```{figure} ../assets/chapter-02/textbook-normal-incidence.svg
:alt: Redrawing of normal incidence: incident propagation toward the interface, reflected propagation away, and transmission into medium 2, with electric and magnetic directions indicated.

Normal-incidence geometry from source page 50. The boundary is $z=0$. Horizontal arrows show propagation; vertical arrows show electric field. Crosses indicate magnetic field into the page and dots out of it. With $x$ upward and $z$ rightward, positive $y$ points into the page. Original book redrawing with vector-consistent directions.
```

Suppose a uniform wave approaches the boundary from medium 1 along $+z$. At $z=0$, two new waves appear:

1. **Reflected wave:** returns through medium 1 along $-z$.
2. **Transmitted wave:** enters medium 2 and continues along $+z$.

### 2.11.3 Incident, reflected and transmitted phasors

Without losing generality for this setting, choose incident electric field along $\hat{\mathbf a}_x$ and magnetic field along $\hat{\mathbf a}_y$. With $e^{j\omega t}$, the incident phasors in medium 1 are:

$$
\widetilde{\mathbf E}_i(z)=\hat{\mathbf a}_x E_{i0}e^{-\gamma_1z},
\qquad
\widetilde{\mathbf H}_i(z)=\hat{\mathbf a}_y\frac{E_{i0}}{\eta_1}e^{-\gamma_1z}.
$$

The reflected wave travels along $-z$. Its fields are:

$$
\widetilde{\mathbf E}_r(z)=\hat{\mathbf a}_x E_{r0}e^{+\gamma_1z},
\qquad
\widetilde{\mathbf H}_r(z)=-\hat{\mathbf a}_y\frac{E_{r0}}{\eta_1}e^{+\gamma_1z}.
$$

:::{tip} Engineering sign check
The minus sign in reflected magnetic field is not a typo! Reversing propagation to $-z$ reverses the magnetic-field relation so that the Poynting vector, $\mathbf E\times\mathbf H$, follows the right-hand rule.
:::

Finally, transmission into medium 2 along $+z$ gives:

$$
\widetilde{\mathbf E}_t(z)=\hat{\mathbf a}_x E_{t0}e^{-\gamma_2z},
\qquad
\widetilde{\mathbf H}_t(z)=\hat{\mathbf a}_y\frac{E_{t0}}{\eta_2}e^{-\gamma_2z}.
$$

The unknown amplitudes are $E_{r0}$ and $E_{t0}$. Boundary conditions hold the key to finding them.

### 2.11.4 Deriving reflection and transmission from boundary conditions

At a simple boundary without free surface charge or current, the total tangential electric and magnetic fields are continuous at $z=0$:

$$
\left.\widetilde{\mathbf E}_{1,\mathrm{tan}}\right|_{z=0}
=\left.\widetilde{\mathbf E}_{2,\mathrm{tan}}\right|_{z=0}
\quad\Longrightarrow\quad E_{i0}+E_{r0}=E_{t0}.
$$

$$
\left.\widetilde{\mathbf H}_{1,\mathrm{tan}}\right|_{z=0}
=\left.\widetilde{\mathbf H}_{2,\mathrm{tan}}\right|_{z=0}
\quad\Longrightarrow\quad
\frac{E_{i0}}{\eta_1}-\frac{E_{r0}}{\eta_1}=\frac{E_{t0}}{\eta_2}.
$$

Solving these two equations for the two unknowns yields the key parameters:

**Electric-field reflection coefficient, $\Gamma$:** the reflected-to-incident amplitude ratio:

$$
\Gamma\equiv\frac{E_{r0}}{E_{i0}}=\frac{\eta_2-\eta_1}{\eta_2+\eta_1}.
$$

This relation shows that, for this interface problem, reflection is caused by intrinsic-impedance mismatch, $\eta_1\ne\eta_2$.

**Electric-field transmission coefficient, $\tau_E$:** the transmitted-to-incident amplitude ratio:

$$
\tau_E\equiv\frac{E_{t0}}{E_{i0}}=\frac{2\eta_2}{\eta_2+\eta_1}.
$$

Comparing the formulas shows that $1+\Gamma=\tau_E$.

### 2.11.5 Power balance: reflected and transmitted energy

Alongside field amplitude, designers need transmitted and reflected powers. Time-averaged Poynting flux gives the **power reflectance, $R$**:

$$
R\equiv\frac{\langle S_r\rangle}{\langle S_i\rangle}
=|\Gamma|^2=\left|\frac{\eta_2-\eta_1}{\eta_2+\eta_1}\right|^2.
$$

In lossless media, **power transmittance, $T$**, is:

$$
T\equiv\frac{\langle S_t\rangle}{\langle S_i\rangle}
=\frac{\eta_1}{\eta_2}|\tau_E|^2
=\frac{4\eta_1\eta_2}{(\eta_1+\eta_2)^2}.
$$

Without material loss, energy conservation takes its familiar form:

$$
R+T=1.
$$

### 2.11.6 Special engineering cases

- **Perfect impedance matching, $\eta_1=\eta_2$:** here $\Gamma=0$ and $\tau_E=1$. The wave does not notice the boundary, and all power crosses without reflection, $R=0,T=1$.
- **Perfect electric conductor, PEC:** the ideal-metal impedance approaches zero, $\eta_2\to0$, giving $\Gamma=-1$. All power reflects, with $R=1,T=0$; no wave penetrates, and tangential electric field at the metal surface is zero.

### 2.11.7 Standing waves and wave impedance

The reflected wave means that the total field in medium 1 is no longer a single traveling wave. Interference between the forward and backward waves creates a spatial pattern whose field amplitude varies between maxima and minima. The **standing-wave ratio (SWR)** describes these variations:

$$
\mathrm{SWR}=\frac{|E_{\max}|}{|E_{\min}|}
=\frac{1+|\Gamma|}{1-|\Gamma|}.
$$

This ratio is 1 for perfect matching and infinite for reflection from an ideal metal.

Furthermore, in the presence of reflection the electric-to-magnetic field ratio is no longer simply $\eta_1$! We introduce a position-dependent **wave impedance ($Z_w$)**. If the positive distance from the boundary is $d=-z$, the input impedance follows the familiar transmission-line expression:

$$
Z_{\mathrm{in}}(d)=\eta_1
\frac{\eta_2+j\eta_1\tan(\beta_1d)}{\eta_1+j\eta_2\tan(\beta_1d)}.
$$

For an ideal metallic surface (PEC), $\Gamma=-1$ and a **complete standing wave** forms. The average transmitted power is zero, $\langle\mathbf S\rangle=0$, while energy exchanges between the electric and magnetic fields in space.

::::{admonition} Booklet example: normal incidence from air onto a dielectric
:class: book-exercise

A plane wave of frequency $f=100\,\mathrm{MHz}$ travels through free space (medium 1) and strikes a lossless dielectric with $\varepsilon_{r2}=4$ normally. Its incident electric field is:

$$
\mathbf E_i(z,t)=\hat{\mathbf a}_x10\cos(\omega t-\beta_1z)\,\mathrm{V/m}.
$$

:::{dropdown} Show / hide the solution
The impedances are:

$$
\eta_1=\eta_0\approx120\pi\,\Omega,
\qquad
\eta_2=\frac{\eta_0}{\sqrt4}=60\pi\approx188.5\,\Omega.
$$

The amplitude reflection and transmission coefficients are:

$$
\Gamma=\frac{60\pi-120\pi}{60\pi+120\pi}=-\frac13,
\qquad \tau_E=1+\Gamma=\frac23.
$$

The reflected and transmitted field amplitudes are:

$$
E_{r0}=\Gamma E_{i0}=-\frac{10}3\,\mathrm{V/m},
\qquad E_{t0}=\tau_E E_{i0}=\frac{20}3\,\mathrm{V/m}.
$$

The power coefficients are also straightforward to calculate:

$$
R=|\Gamma|^2=\frac19\approx11.1\%,
\qquad
T=\frac{\eta_1}{\eta_2}|\tau_E|^2
=2\left(\frac23\right)^2=\frac89\approx88.9\%.
$$

Energy conservation, $R+T=1$, is satisfied.
:::
::::

### 2.11.9 Connection to metasurface engineering

Our analysis so far has concerned natural material boundaries. **Metasurfaces** change what we can do at these boundaries! Instead of relying on bulk materials, we arrange an array of subwavelength unit cells on the interface.

These artificial structures induce electric and magnetic surface currents, $\mathbf J_s$ and $\mathbf M_s$, modifying the classical boundary conditions into generalized sheet transition conditions (GSTCs):

$$
\hat{\mathbf a}_z\times(\widetilde{\mathbf H}_2-\widetilde{\mathbf H}_1)=\mathbf J_s,
\qquad
(\widetilde{\mathbf E}_2-\widetilde{\mathbf E}_1)\times\hat{\mathbf a}_z=\mathbf M_s.
$$

By designing the geometry of these elements, we can control the effective surface impedance, $Z_s$, point by point. This capability enables, for example:

- **Perfect absorbers:** matching the surface input impedance to the free-space impedance, $\eta_1$, to eliminate reflection.
- **Phase-controlling metasurfaces:** applying a nonuniform surface phase to redirect reflected or transmitted wavefronts, as we will see in the **generalized Snell law** below.

:::{note} Matching and absorption are separate questions
Zero reflection establishes matching under the stated illumination. Perfect absorption additionally requires zero outgoing transmission and every other propagating output channel to vanish. A free-standing electric sheet is a two-port system; a ground-backed structure can act as a one-port system. Do not transfer the matching or absorption condition between them without accounting for the backing and its input impedance.
:::

(ch02-section-08)=
### Computational connection: Add a film and keep the phase

Time convention in this computational connection: $e^{-i\omega t}$.


Can adding a material layer reduce reflection? At normal incidence, let a lossless film of index $n_f$ and thickness $d$ lie between media $n_0$ and $n_2$. Use the single-interface coefficients $r_{ab}=(n_a-n_b)/(n_a+n_b)$ and $t_{ab}=2n_a/(n_a+n_b)$, and define

$$
\delta=k_0n_fd=\frac{2\pi n_fd}{\lambda_0}.
$$

Successive round trips have a coherent phase factor $e^{2i\delta}$. Summing their geometric series, or solving the four boundary equations, gives

$$
r_{\mathrm{film}}=\frac{r_{0f}+r_{f2}e^{2i\delta}}{1+r_{0f}r_{f2}e^{2i\delta}},\qquad
t_{\mathrm{film}}=\frac{t_{0f}t_{f2}e^{i\delta}}{1+r_{0f}r_{f2}e^{2i\delta}}.
$$

The incident reference is at the entrance $z=0$; the transmitted amplitude is defined at the exit $z=d$. The fractions are $R=|r_{\mathrm{film}}|^2$ and $T=(n_2/n_0)|t_{\mathrm{film}}|^2$.

For the design wavelength $\lambda_d$, choose $n_f=\sqrt{n_0n_2}$ and $d=\lambda_d/(4n_f)$. Then $\delta=\pi/2$, the reflected contributions cancel, and $R=0$. The mechanism uses interference under specific conditions, not disappearance of the interfaces or absorption of the reflected beam.

```{figure} ../assets/chapter-02/film-interference.png
:alt: Original coherent thin-film response showing wavelength-dependent reflection and transmission around the quarter-wave antireflection condition.

An exact normal-incidence, constant-index analytical film. Perfect antireflection at the design condition does not establish a real material's broadband performance.
```

Moving a reference plane changes phase even in a uniform medium. If only the output plane moves a distance $\ell$ downstream, $t_{\mathrm{new}}=t\,e^{ik_z\ell}$. This fact matters when comparing a zero-thickness sheet, a finite-height ridge, measured S parameters, and a stored training dataset.

