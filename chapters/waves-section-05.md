---
title: "2.5 Plane waves"
short_title: "2.5 Plane waves"
---

(ch02-source-05)=
# 2.5 Plane waves

After Maxwell's equations and boundary conditions, the next step is one of their most important solutions: the **plane wave**. It is the simplest and most fundamental model for electromagnetic propagation in a homogeneous medium. In many metasurface problems, the initial illumination is modeled as a plane wave, and reflected, transmitted and scattered fields are analyzed using the same representation.

A plane wave has parallel planar equiphase surfaces. At a given instant, field phase is constant across a specified plane and changes only along the propagation direction. For propagation along $z$, the field depends only on $z$ and $t$. We can then express it as the sum of two traveling waves:

$$
\mathbf E(z,t)=\mathbf E^+(z,t)+\mathbf E^-(z,t).
$$

Here $\mathbf E^+$ propagates along $+z$, and $\mathbf E^-$ along $-z$.

This representation matters because illumination of a surface can often be decomposed into plane waves traveling in different directions: its plane-wave spectrum. Amplitude, phase, propagation vector and the electric-to-magnetic field relation therefore underpin reflection, transmission, absorption, scattering and polarization-conversion analysis.

### 2.5.1 The electromagnetic wave equation

In a linear, homogeneous, isotropic, time-invariant medium without free sources, Maxwell's equations are:

$$
\nabla\times\mathbf E=-\mu\frac{\partial\mathbf H}{\partial t},
\qquad
\nabla\times\mathbf H=\sigma\mathbf E+\varepsilon\frac{\partial\mathbf E}{\partial t}.
$$

Here $\varepsilon$ is permittivity, $\mu$ permeability, and $\sigma$ conductivity. In a lossless medium, set $\sigma=0$, simplifying Ampère–Maxwell law to:

$$
\nabla\times\mathbf H=\varepsilon\frac{\partial\mathbf E}{\partial t}.
$$

To obtain the electric-field wave equation, take the curl of Faraday's law:

$$
\nabla\times(\nabla\times\mathbf E)
=-\mu\frac{\partial}{\partial t}(\nabla\times\mathbf H).
$$

Substituting Ampère–Maxwell law gives:

$$
\nabla\times(\nabla\times\mathbf E)
=-\mu\varepsilon\frac{\partial^2\mathbf E}{\partial t^2}.
$$

The vector identity also tells us:

$$
\nabla\times(\nabla\times\mathbf E)
=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E.
$$

Without free charge, $\nabla\cdot\mathbf D=0$. The assumed homogeneous medium obeys $\mathbf D=\varepsilon\mathbf E$, giving $\nabla\cdot\mathbf E=0$. The identity therefore simplifies to:

$$
\nabla\times(\nabla\times\mathbf E)=-\nabla^2\mathbf E.
$$

Equating the two results yields the **electric-field wave equation**:

$$
\nabla^2\mathbf E=\mu\varepsilon\frac{\partial^2\mathbf E}{\partial t^2}.
$$

Since the wave speed is $v=1/\sqrt{\mu\varepsilon}$, we can write its standard form:

$$
\nabla^2\mathbf E=\frac1{v^2}\frac{\partial^2\mathbf E}{\partial t^2}.
$$

Exactly the same reasoning gives the magnetic-field equation:

$$
\nabla^2\mathbf H=\frac1{v^2}\frac{\partial^2\mathbf H}{\partial t^2}.
$$

These relations show that electric and magnetic fields propagate as waves in the absence of free sources.

In free space, propagation speed equals the speed of light:

$$
v=c=\frac1{\sqrt{\mu_0\varepsilon_0}}\approx3\times10^8\,\mathrm{m/s}.
$$

In a material medium, the propagation speed is:

$$
v=\frac1{\sqrt{\mu\varepsilon}}=\frac c{\sqrt{\mu_r\varepsilon_r}}.
$$

Most nonmagnetic dielectric design materials have $\mu_r\approx1$, so:

$$
v\approx\frac c{\sqrt{\varepsilon_r}}.
$$

:::{tip} Key design connection
Changing substrate permittivity changes the effective wavelength, accumulated phase and unit-cell resonance dimensions. This makes the relation especially important in metasurface design.
:::

### 2.5.2 A one-dimensional wave-equation solution

For simplicity, suppose the field varies spatially only along $z$. Each Cartesian component, $i=x,y,z$, then obeys:

$$
\frac{\partial^2 E_i(z,t)}{\partial z^2}
=\frac1{v^2}\frac{\partial^2 E_i(z,t)}{\partial t^2}.
$$

The general solution is the sum of two traveling waves:

$$
E_i(z,t)=f_i(z-vt)+g_i(z+vt).
$$

The function $f_i(z-vt)$ travels along $+z$, while $g_i(z+vt)$ travels along $-z$.

For a sinusoidal, harmonic wave, write:

$$
E_i(z,t)=A_i\sin\left[\omega\left(t-\frac zv\right)\right]
+B_i\sin\left[\omega\left(t+\frac zv\right)\right].
$$

Or in the more familiar form:

$$
E_i(z,t)=A_i\sin(\omega t-\beta z)+B_i\sin(\omega t+\beta z).
$$

Here:

$$
\beta=\frac\omega v.
$$

We call $\beta$ the **phase constant**, or wavenumber: it measures phase change per unit length. It is related to wavelength by:

$$
\beta=\frac{2\pi}{\lambda}\quad\Longrightarrow\quad
\lambda=\frac{2\pi}{\beta}.
$$

The relation between phase speed, angular frequency and phase constant is:

$$
v=\frac\omega\beta.
$$

Using $\omega=2\pi f$ gives:

$$
v=f\lambda.
$$

These relations matter because the unit cell's **subwavelength condition** usually refers to the effective wavelength inside the medium, not just the free-space wavelength. On a high-permittivity substrate, the effective wavelength decreases, so the resonant dimensions must be chosen smaller as well.

### 2.5.3 The plane-wave phasor representation

Microwave frequency-domain analysis represents sinusoidal fields with phasors. The source book uses $e^{j\omega t}$. The real field corresponding to a vector phasor, $\mathbf E(z)$, is:

$$
\mathbf E(z,t)=\operatorname{Re}\{\mathbf E(z)e^{j\omega t}\}.
$$

The operator $\operatorname{Re}$ takes the real part. With this time convention, a plane wave traveling along $+z$ has phasor:

$$
\mathbf E(z)=\mathbf E_0e^{-j\beta z}.
$$

Its corresponding real field is:

$$
\mathbf E(z,t)=\operatorname{Re}\{\mathbf E_0e^{-j\beta z}e^{j\omega t}\}.
$$

By contrast, a wave traveling along $-z$ has phasor:

$$
\mathbf E(z)=\mathbf E_0e^{+j\beta z}.
$$

The spatial phase sign therefore determines propagation direction. With $e^{j\omega t}$, $e^{-j\beta z}$ travels along $+z$ and $e^{+j\beta z}$ travels along $-z$.

This convention is retained throughout the source book's subsequent wave-impedance, reflection/transmission, surface-impedance and GSTC relations.

### 2.5.4 Electric and magnetic fields in a plane wave

In a **uniform plane wave**, electric field, magnetic field and propagation direction are mutually perpendicular. For propagation along the unit vector $\hat{\mathbf k}$:

$$
\mathbf H=\frac1\eta\hat{\mathbf k}\times\mathbf E.
$$

Equivalently:

$$
\mathbf E=\eta\mathbf H\times\hat{\mathbf k}.
$$

Here $\eta$ is the medium's **intrinsic impedance**, found from:

$$
\eta=\sqrt{\frac\mu\varepsilon}.
$$

In free space:

$$
\eta_0=\sqrt{\frac{\mu_0}{\varepsilon_0}}\approx120\pi\,\Omega\approx377\,\Omega.
$$

For a nonmagnetic dielectric, $\mu_r\approx1$, intrinsic impedance is:

$$
\eta=\frac{\eta_0}{\sqrt{\varepsilon_r}}.
$$

The ratio of electric-field amplitude to magnetic-field amplitude therefore depends only on the medium:

$$
\frac{|\mathbf E|}{|\mathbf H|}=\eta.
$$

As a wave enters a different medium, a change in intrinsic impedance can cause a mismatch and therefore reflection. This simple principle is the **physical foundation of impedance-matching metasurfaces, absorbers, and antireflection coatings**.

In a uniform plane wave, the perpendicularity relations are:

$$
\mathbf E\perp\mathbf H,\qquad
\mathbf E\perp\hat{\mathbf k},\qquad
\mathbf H\perp\hat{\mathbf k}.
$$

Thus $\mathbf E$, $\mathbf H$, and $\hat{\mathbf k}$ form a **right-handed system**, and both fields are **transverse** to propagation.

### 2.5.5 A plane wave in a lossy medium

In a lossless medium, the propagation constant contains only a phase term, $\gamma=j\beta$. In a lossy medium, amplitude decreases as well as phase changing. We define a complex propagation constant:

$$
\gamma=\alpha+j\beta.
$$

Here $\alpha$ is the **attenuation constant**, measured in nepers per meter, $\mathrm{Np/m}$, and $\beta$ is the phase constant, measured in $\mathrm{rad/m}$.

For propagation along $\hat{\mathbf k}$, the propagation factor becomes:

$$
e^{-\gamma\hat{\mathbf k}\cdot\mathbf r}
=e^{-\alpha\hat{\mathbf k}\cdot\mathbf r}
e^{-j\beta\hat{\mathbf k}\cdot\mathbf r}.
$$

The first, real exponential describes amplitude decay along propagation; the second, imaginary exponential describes phase change. A plane-wave field in a lossy medium can therefore be written:

$$
\mathbf F(\mathbf r)=\hat{\mathbf a}_F F_0e^{-\gamma\hat{\mathbf k}\cdot\mathbf r}.
$$

The field $\mathbf F$ can be electric or magnetic, and the unit vector $\hat{\mathbf a}_F$ specifies its polarization.

Loss, whether ohmic or dielectric, can be desirable in an absorber because it turns wave energy into heat and reduces reflection. In a highly efficient transmissive or reflective metasurface, however, loss is generally undesirable because it wastes power that could have entered the useful outgoing wave.

### 2.5.6 Connecting plane waves to metasurface design

Plane waves are the basic language of metasurface analysis. Many designs specify an incident plane wave with a given amplitude, phase, polarization and incidence angle:

$$
\mathbf E_i(\mathbf r)=\mathbf E_{0i}e^{-j\mathbf k_i\cdot\mathbf r}.
$$

Its interaction with the surface produces reflected and transmitted fields, which can also be represented using plane-wave spectra:

$$
\mathbf E_r(\mathbf r)=\mathbf E_{0r}e^{-j\mathbf k_r\cdot\mathbf r},
\qquad
\mathbf E_t(\mathbf r)=\mathbf E_{0t}e^{-j\mathbf k_t\cdot\mathbf r}.
$$

Uniform metasurfaces usually follow ordinary reflection and Snell refraction laws. In a phase-gradient surface, gradual structural variation can change the tangential wavevector, allowing the reflected or transmitted direction to be engineered through generalized Snell's law.

Each **unit cell** must give the incident plane wave a specified local response. That may mean changing phase, amplitude, absorption, polarization or propagation direction, or creating a desired near-field or far-field distribution.

We therefore needed a precise plane-wave framework before introducing reflection/transmission coefficients, surface impedance and GSTCs. A plane wave is the standard input to many metasurface problems; the surface's response is interpreted through its changes to that wave's amplitude, phase, polarization and direction.

::::{admonition} Textbook example: a ten-gigahertz wave in a dielectric
:class: book-exercise

A plane wave propagates in a homogeneous, lossless, nonmagnetic dielectric with $\varepsilon_r=4$ and $\mu_r=1$. Its frequency is $f=10\,\mathrm{GHz}$. Using $e^{j\omega t}$, its electric field is:

$$
\mathbf E(z)=12\hat{\mathbf x}e^{-j\beta z}\,\mathrm{V/m}.
$$

Answer the following questions:

1. Calculate propagation speed.
2. Find wavelength and phase constant $\beta$.
3. Identify propagation direction.
4. Calculate the corresponding magnetic field.
5. Write the time-domain electric and magnetic fields at $z=\lambda/8$.

:::{dropdown} Show / hide answer
**1. Propagation speed.** For a nonmagnetic dielectric:

$$
v=\frac c{\sqrt{\varepsilon_r}}.
$$

Therefore:

$$
v=\frac{3\times10^8}{\sqrt4},\qquad
\boxed{v=1.5\times10^8\,\mathrm{m/s}}.
$$

**2. Wavelength and phase constant.** Wavelength follows from:

$$
\lambda=\frac vf.
$$

Using $f=10\,\mathrm{GHz}=10^{10}\,\mathrm{Hz}$:

$$
\lambda=\frac{1.5\times10^8}{10^{10}}=1.5\times10^{-2}\,\mathrm m.
$$

Thus:

$$
\boxed{\lambda=15\,\mathrm{mm}}.
$$

The phase constant is:

$$
\beta=\frac{2\pi}\lambda.
$$

Therefore:

$$
\beta=\frac{2\pi}{1.5\times10^{-2}}\approx418.9\,\mathrm{rad/m}.
$$

Consequently:

$$
\boxed{\beta\approx418.9\,\mathrm{rad/m}}.
$$

**3. Propagation direction.** With $e^{j\omega t}$, the spatial factor $e^{-j\beta z}$ indicates propagation along positive $z$. The direction is therefore $+z$.

**4. Magnetic field.** Intrinsic impedance follows from:

$$
\eta=\frac{\eta_0}{\sqrt{\varepsilon_r}}.
$$

Using $\eta_0\approx377\,\Omega$:

$$
\eta=\frac{377}2=188.5\,\Omega.
$$

For the plane wave:

$$
\mathbf H=\frac1\eta\hat{\mathbf k}\times\mathbf E.
$$

Here $\hat{\mathbf k}=\hat{\mathbf z}$ and $\mathbf E=12\hat{\mathbf x}e^{-j\beta z}$, so:

$$
\mathbf H=\frac1{188.5}\hat{\mathbf z}\times(12\hat{\mathbf x}e^{-j\beta z}).
$$

Since $\hat{\mathbf z}\times\hat{\mathbf x}=\hat{\mathbf y}$, we obtain:

$$
\mathbf H(z)=\frac{12}{188.5}\hat{\mathbf y}e^{-j\beta z}.
$$

Therefore:

$$
\boxed{\mathbf H(z)\approx0.0637\hat{\mathbf y}e^{-j\beta z}\,\mathrm{A/m}}.
$$

The electric field, magnetic field and propagation direction, $\hat{\mathbf z}$, are mutually perpendicular and form a right-handed system.

**5. Fields at $z=\lambda/8$.** First evaluate the phase:

$$
\beta z=\frac{2\pi}\lambda\frac\lambda8=\frac\pi4.
$$

The electric phasor at this position is:

$$
\mathbf E\left(\frac\lambda8\right)=12\hat{\mathbf x}e^{-j\pi/4}\,\mathrm{V/m}.
$$

The magnetic phasor is:

$$
\mathbf H\left(\frac\lambda8\right)=0.0637\hat{\mathbf y}e^{-j\pi/4}\,\mathrm{A/m}.
$$

Using $e^{j\omega t}$, the real fields are:

$$
\mathbf E\left(\frac\lambda8,t\right)=12\hat{\mathbf x}\cos\left(\omega t-\frac\pi4\right)\,\mathrm{V/m},
\qquad
\mathbf H\left(\frac\lambda8,t\right)=0.0637\hat{\mathbf y}\cos\left(\omega t-\frac\pi4\right)\,\mathrm{A/m}.
$$

Consequently:

$$
\boxed{\mathbf E\left(\frac\lambda8,t\right)=12\hat{\mathbf x}\cos\left(\omega t-\frac\pi4\right)\,\mathrm{V/m}},
\qquad
\boxed{\mathbf H\left(\frac\lambda8,t\right)=0.0637\hat{\mathbf y}\cos\left(\omega t-\frac\pi4\right)\,\mathrm{A/m}}.
$$

Both fields have the same phase, and average power travels along positive $z$.
:::
::::

(ch02-section-02)=
### Computational connection: Give a wave a direction

Time convention in this computational connection: $e^{-i\omega t}$.


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

