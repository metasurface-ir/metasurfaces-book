---
title: 'Chapter 2: Electromagnetic Waves and Their Interaction with Metasurfaces'
short_title: Waves, boundaries, and sheets
description: Derive the wave, polarization, boundary, and power language needed to design and verify a metasurface, through predictions, exact analytical experiments, and a coherent-absorption finale.
---

# Chapter 2: Electromagnetic Waves and Their Interaction with Metasurfaces

**Central question:** what must a surface do to the electromagnetic field, and how can we tell whether it has done it?

A field crosses from glass into air and its transmitted electric amplitude grows to **1.2 times** the incident amplitude. A lossless interface leaves a transmitted field on the other side while transmitting **no net normal power**. A sheet that absorbs at most half of a single incident beam absorbs **all** of two suitable beams. None of these statements violates energy conservation. Each asks us to distinguish a field from a power, a local field from a propagating channel, or one illumination from another.

These are our three puzzles. Make an initial prediction for each, then return to them after working through the chapter. The [browser lab](../labs/02-waves-lab.md) lets you vary the experiments without installing software; the [executed notebook](../notebooks/02-waves-and-interfaces.ipynb) exposes their equations and checks. The [worked examples](02-waves-guide.md) and [self-check](02-waves-review.md) provide a second path through the same ideas.

:::{note} The computation and its scope
This chapter evaluates analytical plane-wave, single-interface, coherent thin-film, Jones-vector, and local electric-sheet models. Bulk media have positive real constant refractive indices and permeability $\mu_0$. The film and sheet calculations use normal incidence; the interface calculation includes TE/TM oblique incidence. A sheet may dissipate through a nonnegative conductance. These calculations do not simulate a patterned geometry, retrieve a fabricated material, or establish a broadband physical device. Chapters [3](03-unit-cell-design.md) and [5](05-metasurface-synthesis.md) supply separate full-wave geometry examples.
:::

## 2.1 A route through the prerequisites

By the end of this chapter, you should be able to derive rather than memorize the flat-interface response; calculate its power with the correct admittance; distinguish propagation, evanescence, and grazing cutoff; express coherent polarization states with Jones vectors; and decide whether proposed scattering coefficients could describe a stated sheet.

| Stop | Question to predict | Tool to develop |
| --- | --- | --- |
| Waves | Which way does energy travel? | Phasors, $\mathbf E$, $\mathbf H$, and Poynting flux |
| Polarization | Can intensity stay fixed while the field changes? | Relative component phase and Jones matrices |
| An interface | Can $|t|$ exceed one without gain? | Boundary conditions and flux normalization |
| Critical angles | Can a field exist without carrying normal power away? | Complex longitudinal wavevector |
| A film | Can adding material reduce reflection? | Coherent interference and phase reference |
| A sheet | Can phase change absorption? | Surface current, scattering channels, and coherence |

Keep a small record beside every calculation: illumination, material model, basis, time convention, reference planes, and power denominator. This is the foundation for every later unit-cell library, diffraction efficiency, and learned response in the book.

## 2.2 Give a wave a direction

We use real physical fields obtained from complex phasors:

$$
\mathbf E(\mathbf r,t)=\operatorname{Re}\{\widetilde{\mathbf E}(\mathbf r)e^{-i\omega t}\},\qquad
\widetilde{\mathbf E}(\mathbf r)=\mathbf E_0e^{i\mathbf k\cdot\mathbf r}.
$$

Thus a positive real $k_z$ with $e^{ik_z z-i\omega t}$ travels toward positive $z$. At a fixed phase, $k_z z-\omega t$ is constant. A complex $k_z=i\kappa$ with $\kappa>0$ instead contributes $e^{-\kappa z}$: it decays into the positive-$z$ half-space. Choosing the opposite square-root branch would make it grow away from a passive interface.

Maxwell's equations in a homogeneous source-free region become

$$
\nabla\times\widetilde{\mathbf E}=i\omega\mu\widetilde{\mathbf H},\qquad
\nabla\times\widetilde{\mathbf H}=-i\omega\varepsilon\widetilde{\mathbf E},\qquad
\nabla\cdot\widetilde{\mathbf D}=0,\qquad\nabla\cdot\widetilde{\mathbf B}=0.
$$

Substituting the plane-wave form gives

$$
\mathbf k\times\mathbf E_0=\omega\mu\mathbf H_0,\qquad
\mathbf k\cdot\mathbf E_0=0,\qquad
k^2=\omega^2\mu\varepsilon.
$$

For a complex wavevector, this dispersion relation uses $\mathbf k\cdot\mathbf k$, rather than $\mathbf k^*\cdot\mathbf k$. The distinction matters for an evanescent wave.

For a propagating wave in our nonmagnetic real-index media,

$$
k=nk_0,\quad k_0=\frac{2\pi}{\lambda_0},\quad
\eta=\sqrt{\frac{\mu}{\varepsilon}}=\frac{\eta_0}{n},\quad
\mathbf H_0=\frac{1}{\eta}\widehat{\mathbf k}\times\mathbf E_0.
$$

The magnetic field is fixed by the electric field and propagation direction. It cannot be assigned an independent sign. In particular, reversing the propagation direction reverses the relevant electric-to-magnetic relation. That sign creates the $1-r$ term in the interface derivation below.

## 2.3 A field is not a power meter

For phasors defined as peak amplitudes, the time-averaged power-flux density is

$$
\langle\mathbf S\rangle=\frac12\operatorname{Re}\{\widetilde{\mathbf E}\times\widetilde{\mathbf H}^{\,*}\}.
$$

The factor $1/2$ belongs to the peak-amplitude convention. For a normally incident propagating wave in a real medium,

$$
\langle S_z\rangle=\frac{|E|^2}{2\eta}=\frac{n|E|^2}{2\eta_0}.
$$

An electric amplitude therefore does not have the same power weighting in two different media. A transmitted amplitude of 1.2 in air can carry less power than an incident amplitude of 1 in glass. At oblique incidence, the normal flux and chosen field component introduce additional factors; we will collect them in a wave admittance.

:::{tip} A prediction before the derivation
At normal incidence from $n_i=1.5$ to $n_t=1$, suppose $t=1.2$. Calculate $T=(n_t/n_i)|t|^2$ before deciding whether the interface amplifies the wave. The answer is 0.96. The remaining 0.04 can be reflected without any gain or absorption.
:::

Power is only one observable. The fields $t=1$ and $t=-1$ have equal transmitted power in the same normalization, but they interfere differently with a fixed reference. Always retain amplitude and phase together when the design concerns a complex wavefront.

## 2.4 Make polarization visible

At a fixed point, the tip of the transverse electric field can trace a line, ellipse, or circle over one period. Write a unit-norm Jones vector for propagation along positive $z$ as

$$
\mathbf j=\begin{bmatrix}\cos\alpha\\e^{i\delta}\sin\alpha\end{bmatrix},\qquad
\mathbf j^\dagger\mathbf j=1.
$$

Here $\alpha$ controls the component magnitudes and $\delta$ is the relative phase of $E_y$ with respect to $E_x$. At $z=0$,

$$
E_x(t)=\cos\alpha\cos\omega t,\qquad
E_y(t)=\sin\alpha\cos(\delta-\omega t).
$$

For $\delta=0$, the vector remains on a line. For $\alpha=45^\circ$ and $\delta=90^\circ$, the normalized state is $(1,i)^T/\sqrt2$: starting at positive $E_x$, the tip moves toward positive $E_y$ as time increases. This description specifies the axes and time convention without relying on a potentially ambiguous handedness label.

```{figure} ../assets/chapter-02/polarization.png
:alt: Original time-domain polarization ellipses and analyzer responses calculated from coherent Jones vectors.

Relative phase changes the field trajectory even when the total Jones-vector norm stays fixed. State the time convention and viewing axes before assigning a handedness name.
```

An ideal retarder aligned with the axes can have

$$
J_\delta=\begin{bmatrix}1&0\\0&e^{i\delta}\end{bmatrix},\qquad
J_\delta^\dagger J_\delta=I.
$$

It changes relative phase while preserving power in this ideal model. An analyzer with real unit axis $\mathbf u_\beta=(\cos\beta,\sin\beta)^T$ transmits the fraction

$$
I_\beta=|\mathbf u_\beta^\dagger\mathbf j|^2.
$$

For linear input this becomes Malus's law; for a normalized circular state it is $1/2$ for every analyzer angle. These are coherent, fully polarized models. A single Jones vector does not represent unpolarized or partially coherent light. Chapter [5](05-metasurface-synthesis.md) builds ideal Jones transformations; a physical element still needs conversion and leakage data.

## 2.5 Ask what is continuous

Place the interface at $z=0$, with unit normal $\widehat{\mathbf n}=\widehat{\mathbf z}$ pointing from region 1 to region 2. Integrating the curl equations across an infinitesimal loop gives the tangential jump conditions

$$
\widehat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf J_s,\qquad
\widehat{\mathbf n}\times(\mathbf E_2-\mathbf E_1)=-\mathbf M_s.
$$

$\mathbf J_s$ is an electric surface-current density in A/m. $\mathbf M_s$ is an equivalent magnetic surface-current density in V/m under this sign convention; it is a useful field-equivalence description, not a requirement for literal magnetic monopoles. With neither surface current, the tangential electric and magnetic fields are continuous. Normal components satisfy the corresponding flux laws; tangential continuity does not mean every Cartesian component of every field is continuous.

```{figure} ../assets/chapter-02/sheet-boundaries.svg
:alt: Interface normal, tangential field jumps, and an electric sheet represented by a shunt admittance at one reference plane.

Boundary conditions connect a field transformation to the current needed to support it. The local electric shunt considered here is one restricted example; general tensor, magnetic, and bianisotropic sheet synthesis requires additional relations.
```

The entire planar interface has the same boundary relation at every $x$. The incident, reflected, and transmitted fields must therefore have matching tangential phase factors:

$$
k_x=n_i k_0\sin\theta_i=n_t k_0\sin\theta_t.
$$

This is phase matching and, for propagating transmission, Snell's law. A periodic surface can add reciprocal-lattice wavevectors, as developed in [Chapter 4](04-periodic-floquet.md). A desired phase profile is consequently a scattering specification, not a replacement for Maxwell's boundary conditions.

## 2.6 Derive the interface response

Take the plane of incidence to be $xz$. **TE** has electric field along $y$. **TM** has magnetic field along $y$ and electric field in the $xz$ plane. We compare the same tangential electric component on each side: $E_y$ for TE and $E_x$ for TM. Define

$$
s=n_i\sin\theta_i,\qquad q_j=\frac{k_{z,j}}{k_0}=\sqrt{n_j^2-s^2},
$$

choosing the outgoing/decaying root, with nonnegative real and imaginary parts for these lossless positive-index half-spaces. Our dimensionless tangential wave admittance is

$$
Y_j^{\mathrm{TE}}=q_j,\qquad Y_j^{\mathrm{TM}}=\frac{n_j^2}{q_j}.
$$

The physical admittance is $Y_j/\eta_0$. To see the signs, use the signed tangential magnetic component $h=-H_x$ for TE and $h=H_y$ for TM. A forward wave has $h=YE_{\mathrm{tan}}/\eta_0$; a backward wave has the opposite relation. With incident tangential electric amplitude one, continuity gives

$$
1+r=t,\qquad Y_i(1-r)=Y_t t.
$$

Solving these two equations yields the Fresnel coefficients in our basis:

$$
\boxed{r=\frac{Y_i-Y_t}{Y_i+Y_t}},\qquad
\boxed{t=\frac{2Y_i}{Y_i+Y_t}}.
$$

For a propagating incident channel, $Y_i$ is real and positive. Its normal power fractions are

$$
R=|r|^2,\qquad T=\frac{\operatorname{Re}Y_t}{Y_i}|t|^2.
$$

For a lossless single interface, $R+T=1$. At normal incidence, $Y_j=n_j$ for both polarizations: from air to glass, $r=-0.2$, $t=0.8$, $R=0.04$, and $T=0.96$.

:::{warning} A TM sign that is easy to miss
Some references define reflected TM amplitude along a polarization unit vector that rotates with the reflected wave. Here the reflected and incident coefficients both multiply a common tangential $x$ direction. Their amplitude signs can therefore differ from those references while the physical vector fields and powers agree. Compare conventions before treating a sign difference as an error. At normal incidence, our TE and TM tangential-electric coefficients agree.
:::

```{figure} ../assets/chapter-02/wave-geometry.svg
:alt: Incident, reflected, and transmitted wavevectors; the interface normal; and TE/TM tangential component conventions.

The geometry, polarization basis, and reference plane are part of the definition of a scattering coefficient. Positive normal power leaves the interface into the transmitted half-space.
```

## 2.7 Brewster, evanescence, and cutoff

For nonmagnetic dielectric media, TM reflection vanishes when the two TM admittances match. Substituting Snell's law gives

$$
\tan\theta_B=\frac{n_t}{n_i}.
$$

For air to glass, $\theta_B\approx56.31^\circ$. The TE wave at that angle still reflects. Brewster cancellation is polarization dependent; it does not say that every field at that interface is reflectionless.

```{figure} ../assets/chapter-02/interface-power.png
:alt: Analytical TE/TM reflected and transmitted normal powers versus incidence angle, including Brewster and critical-angle behavior.

Keep field coefficients and normal power separate. The same admittance expressions account for ordinary refraction, the TM reflection zero, and total internal reflection within their stated domain.
```

If $n_i>n_t$, the critical angle satisfies $\sin\theta_c=n_t/n_i$. For glass to air, $\theta_c\approx41.81^\circ$. Above it,

$$
q_t=i\gamma,\qquad\gamma=\sqrt{s^2-n_t^2}>0,\qquad
\widetilde E_t\propto e^{ik_xx}e^{-k_0\gamma z}.
$$

The transmitted field can be nonzero while $\operatorname{Re}Y_t=0$, giving $T=0$ and $R=1$. Its amplitude decay length is $\ell_E=1/(k_0\gamma)$; the intensity decay length is half as large. It is incorrect to interpret $T=0$ as proof that the entire transmitted field vanishes. It is also incorrect to interpret a nonzero evanescent amplitude as a nonzero outgoing normal-power channel.

```{figure} ../assets/chapter-02/tir-field.png
:alt: Original analytical total-internal-reflection field and evanescent decay visualization.

The field penetrates the second medium while its net transmitted normal power is zero for this single, semi-infinite lossless interface. Adding another nearby interface would define a different tunneling problem.
```

At exact grazing cutoff, formulas containing $1/q_t$ need limiting treatment. For TM, $t$ defined from tangential $E_x$ tends to zero, but the factor relating $E_z$ to $E_x$ can diverge so that the complete transmitted field need not vanish. Approach cutoff from either side and report it separately; do not evaluate a singular intermediate admittance as if it were an ordinary finite propagating channel.

## 2.8 Add a film and keep the phase

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

## 2.9 Normalize a scattering matrix

For propagating ports with real positive admittance, scale each incoming/outgoing tangential field by $\sqrt{Y_j/(2\eta_0)}$. The resulting amplitudes have squared magnitude equal to normal power flux. Write

$$
\mathbf b=S\mathbf a,\qquad P_{\mathrm{in}}=\mathbf a^\dagger\mathbf a,\qquad
P_{\mathrm{out}}=\mathbf b^\dagger\mathbf b.
$$

A lossless complete scattering description requires $S^\dagger S=I$. A passive one requires $\mathbf a^\dagger(I-S^\dagger S)\mathbf a\geq0$ for every input. Reciprocity and mirror symmetry are separate properties; a substrate can break the latter without breaking the former.

For our bare interface between two propagating channels,

$$
S=\begin{bmatrix}r&\tau\\\tau&-r\end{bmatrix},\qquad
\tau=\frac{2\sqrt{Y_iY_t}}{Y_i+Y_t}.
$$

The opposite reflection signs follow our field bases and port arrangement. $S$ is symmetric and unitary. Raw electric-field transmission coefficients from opposite sides need not be equal; their power-normalized counterparts are equal here. An evanescent solution with zero normal flux cannot be normalized as an independent unit-power propagating port by dividing by $\sqrt{\operatorname{Re}Y}$.

## 2.10 Give a sheet a current

Consider an ideal, local, purely electric surface at normal incidence. Let its sheet admittance be $Y_s$ in siemens, and define the dimensionless quantity $g=\eta_0Y_s$. Because there is no magnetic surface current, tangential electric continuity still gives $t=1+r$. The electric jump condition adds a shunt current:

$$
Y_i(1-r)-Y_t t=g\,t.
$$

Solving yields

$$
r=\frac{Y_i-Y_t-g}{Y_i+Y_t+g},\qquad
t=\frac{2Y_i}{Y_i+Y_t+g},\qquad
A=\frac{4Y_i\operatorname{Re}g}{|Y_i+Y_t+g|^2}.
$$

Here $Y_i=n_i$ and $Y_t=n_t$ at normal incidence. For $\operatorname{Re}g\geq0$, the sheet is passive and $R+T+A=1$. The absorbed power follows directly from $\tfrac12\operatorname{Re}Y_s|E_{\mathrm{sheet}}|^2$, rather than from unexplained missing channels.

This is also an equivalent-circuit language: the wave regions are transmission-line ports and $Y_s$ is a shunt at their junction. Under $e^{-i\omega t}$, a capacitance per square has $Y_s=-i\omega C_s$ and an inductance has $Y_s=+i/(\omega L_s)$. Positive conductance dissipates power. An engineering convention using $e^{+i\omega t}$ reverses these reactive signs.

For equal air ports and real $g=G\geq0$,

$$
A=\frac{4G}{(2+G)^2}\leq\frac12,
$$

with equality at $G=2$. A larger conductance eventually reflects more strongly instead of absorbing more. This 50% limit belongs to this one-sided, purely electric, equal-medium sheet model. A backed sheet, added magnetic response, different environment, or different illumination changes the problem.

## 2.11 Retrieve only what is identifiable

For the equal-air electric shunt at the common sheet plane,

$$
g=\frac{2(1-t)}{t}.
$$

Before applying it, check the complex continuity relation $t=1+r$, the reference planes, the exterior impedances, and the model assumptions. Near $t=0$, small errors in $t$ can produce large parameter errors; at $t=0$ this inversion is undefined. A passive model should also satisfy the appropriate energy constraints.

An arbitrary finite film or patterned ridge does not automatically meet those conditions. In particular, entrance and exit planes of a finite layer are different planes. Deembedding removes known propagation phases; it does not prove that the remaining response is a local electric shunt. A successful fit at one frequency is not a validation over wavelengths, angles, polarizations, or geometries that were not checked.

The [Chapter 1 model](01-metasurface-foundations.md) introduced two effective response channels. Its balanced electric-like/magnetic-like construction is richer than a pure electric shunt, which enforces $t=1+r$ and cannot independently specify an arbitrary transmission amplitude and phase. General susceptibility-tensor retrieval and bianisotropic sheet synthesis require more unknowns, illuminations, and consistency conditions than the scalar illustration here.

## 2.12 Where did the missing light go?

Return to the air-surrounded sheet with $g=2$. One incident beam gives $r=-1/2$, $t=1/2$, and $A=1/2$. Now illuminate it coherently from both sides, with total incoming power normalized to one:

$$
\mathbf a=\frac{1}{\sqrt2}\begin{bmatrix}1\\e^{i\phi}\end{bmatrix},\qquad
S=\frac12\begin{bmatrix}-1&1\\1&-1\end{bmatrix}.
$$

Adding the outgoing field contributions before calculating their powers gives

$$
A_{\mathrm{two\ sided}}=1-\|S\mathbf a\|^2=\frac{1+\cos\phi}{2}.
$$

At $\phi=0$, every outgoing amplitude vanishes: the ideal model absorbs all the incoming power. At $\phi=\pi$, the electric field at the sheet is a node and absorption vanishes. The material parameter has not changed. The incident coherent state has changed, so its overlap with the dissipative scattering channel has changed.

```{figure} ../assets/chapter-02/sheet-response.png
:alt: Original analytical sheet results comparing the one-sided absorption bound with phase-controlled two-sided coherent absorption.

The one-sided and two-sided experiments have different incident states and the same explicit power normalization. Perfect two-sided absorption here requires exact sheet parameters and coherent excitation at the stated reference planes; it is not a fabricated-device result.
```

This is an entry point to coherent perfect absorption, a research topic developed by [Chong, Ge, Cao, and Stone](https://arxiv.org/abs/1003.4968). Our shunt derivation illustrates a restricted analytical example and does not reproduce their slab calculation. An experiment would additionally need controlled phase, matched spatial modes, calibrated power, material dispersion/loss, and uncertainty.

## 2.13 Carry this into the next chapters

Before accepting any metasurface response, ask:

1. Which field basis, time convention, and reference planes define its complex coefficients?
2. Which admittance or channel normalization converts those coefficients to power?
3. Which waves propagate, which decay, and which are at cutoff?
4. Which boundary currents or geometry support the proposed transformation?
5. Does the model conserve or dissipate power appropriately for every relevant illumination?
6. Which independent condition would test the claimed retrieval or design?

Chapter [3](03-unit-cell-design.md) adds patterned geometry and a full-wave library; Chapter [4](04-periodic-floquet.md) adds diffraction channels; Chapter [5](05-metasurface-synthesis.md) assembles transformations. Chapter [10](10-ai-metasurfaces.md) uses data that must preserve exactly these conventions. Continue with the [nine worked examples](02-waves-guide.md), [computational lab](../labs/02-waves-lab.md), and [self-check and mini-project](02-waves-review.md).

For an independent foundational route, the [Cornell ECE 3030 handouts](https://ocw.ece.cornell.edu/courses/ece-3030-electromagnetic-fields-and-waves-2/ece-3030-lectures-notes-and-handouts-2/) cover plane waves, polarization, interfaces, and multilayers. [MIT's optics lecture notes](https://ocw.mit.edu/courses/2-71-optics-spring-2014/pages/lecture-notes/) provide complementary wave and polarization material. The explanations, derivations, figures, and experiments in this chapter are original course material.

## Linked computational investigations

Continue with [ms-09: spectral bandwidth](../labs/09-dispersion-lab.md), [ms-10: independent cells versus supercells](../labs/10-coupling-lab.md), and [ms-11: bounded optimization with independent checks](../labs/11-inverse-design-lab.md). These executed studies use the same explicit ridge geometry and connect spectral response, model approximation and design validation. The inverse-design study is a direct full-wave baseline for later AI comparisons.
