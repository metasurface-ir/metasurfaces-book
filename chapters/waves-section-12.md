---
title: "2.12 Reflection and refraction at oblique incidence"
short_title: "2.12 Reflection and refraction at oblique incidence"
---

(ch02-source-12)=
# 2.12 Reflection and refraction at oblique incidence

### 2.12.1 Geometry and the wave vector

When the incidence angle relative to the surface normal is nonzero, the wave vector $\mathbf k$ describes propagation. Take the incidence plane as $xz$ and the interface as $z=0$:

- **Incident wave vector:** $\mathbf k_i=k_1(\hat{\mathbf a}_x\sin\theta_i+\hat{\mathbf a}_z\cos\theta_i)$.
- **Reflected wave vector:** $\mathbf k_r=k_1(\hat{\mathbf a}_x\sin\theta_r-\hat{\mathbf a}_z\cos\theta_r)$.
- **Transmitted (refracted) wave vector:** $\mathbf k_t=k_2(\hat{\mathbf a}_x\sin\theta_t+\hat{\mathbf a}_z\cos\theta_t)$.

Here $k_1=\omega\sqrt{\mu_1\varepsilon_1}$ and $k_2=\omega\sqrt{\mu_2\varepsilon_2}$.

### 2.12.2 Phase matching and the classical Snell laws

Field continuity at every point on the interface, $z=0$, requires identical spatial phase dependence along the interface coordinate $x$ for all three waves (**phase matching**):

$$
k_{ix}=k_{rx}=k_{tx}\quad\Longrightarrow\quad
k_1\sin\theta_i=k_1\sin\theta_r=k_2\sin\theta_t.
$$

Two familiar laws of geometrical optics follow from this fundamental relation:

**1. Law of reflection:**

$$
\theta_r=\theta_i.
$$

**2. Snell's law of refraction:**

$$
n_1\sin\theta_i=n_2\sin\theta_t,
\qquad n=\sqrt{\varepsilon_r\mu_r}.
$$

### 2.12.3 Parallel (TM) and perpendicular (TE) polarizations

At oblique incidence, the fields depend on their polarization relative to the **plane of incidence**, which contains the surface normal and the wave vector:

- **Perpendicular polarization (TE or s):** the electric field $\mathbf E$ is perpendicular to the incidence plane, along $\hat{\mathbf a}_y$.
- **Parallel polarization (TM or p):** the magnetic field $\mathbf H$ is perpendicular to the incidence plane, while the electric field lies within it.

### 2.12.4 Fresnel coefficients

Applying the boundary conditions to tangential $\mathbf E$ and $\mathbf H$ gives the Fresnel reflection and transmission coefficients.

For TE polarization:

$$
\Gamma_{\mathrm{TE}}=
\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}
{\eta_2\cos\theta_i+\eta_1\cos\theta_t},
\qquad
\tau_{\mathrm{TE}}=
\frac{2\eta_2\cos\theta_i}{\eta_2\cos\theta_i+\eta_1\cos\theta_t}
=1+\Gamma_{\mathrm{TE}}.
$$

For TM polarization:

$$
\Gamma_{\mathrm{TM}}=
\frac{\eta_2\cos\theta_t-\eta_1\cos\theta_i}
{\eta_2\cos\theta_t+\eta_1\cos\theta_i},
\qquad
\tau_{\mathrm{TM}}=
\frac{2\eta_2\cos\theta_i}{\eta_2\cos\theta_t+\eta_1\cos\theta_i}.
$$

### 2.12.5 Brewster angle and total internal reflection

**Brewster angle ($\theta_B$, or polarizing angle):** the incidence angle at which the TM reflection coefficient vanishes, $\Gamma_{\mathrm{TM}}=0$. For two nonmagnetic dielectrics, $\mu_1=\mu_2=\mu_0$:

$$
\theta_B=\arctan\sqrt{\frac{\varepsilon_2}{\varepsilon_1}}
=\arctan\left(\frac{n_2}{n_1}\right).
$$

At this angle, the reflected wave is entirely TE polarized.

**Critical angle and total internal reflection (TIR):** when a wave travels from a higher-index medium toward a lower-index medium, $n_1>n_2$, incidence beyond the critical angle, $\theta_i>\theta_c$, satisfies:

$$
\theta_c=\arcsin\left(\frac{n_2}{n_1}\right).
$$

No power passes into the second medium and all incident power is reflected. The field in medium 2 becomes an **evanescent wave**, decaying exponentially along the interface normal, $+z$, while propagating along the surface, $+x$.

::::{admonition} Booklet example: TE oblique incidence
:class: book-exercise

A TE-polarized plane wave strikes a lossless dielectric obliquely from air. The interface is $z=0$ and the incidence plane is $xz$. The media have the following properties:

$$
\varepsilon_{r1}=1,\quad\mu_{r1}=1,\qquad
\varepsilon_{r2}=4,\quad\mu_{r2}=1.
$$

The incidence angle relative to the interface normal is $\theta_i=30^\circ$, and the incident electric-field amplitude is $E_{0i}=10\,\mathrm{V/m}$. Assuming both media are lossless:

1. Calculate each medium's refractive index and intrinsic impedance.
2. Find the reflection and refraction angles.
3. Find the TE electric-field reflection and transmission coefficients and the reflected and transmitted electric-field amplitudes.
4. Calculate the reflected and transmitted power fractions and check energy conservation.

:::{dropdown} Show / hide the solution
**1. Refractive indices and intrinsic impedances.** The refractive index is:

$$
n=\sqrt{\mu_r\varepsilon_r}.
$$

For medium 1, $n_1=\sqrt{(1)(1)}=1$, and for medium 2, $n_2=\sqrt{(1)(4)}=2$. Therefore:

$$
\boxed{n_1=1,\qquad n_2=2}.
$$

The intrinsic impedance is:

$$
\eta=\eta_0\sqrt{\frac{\mu_r}{\varepsilon_r}},\qquad \eta_0\simeq377\,\Omega.
$$

For medium 1:

$$
\eta_1=377\sqrt{\frac11}=377\,\Omega.
$$

For medium 2:

$$
\eta_2=377\sqrt{\frac14}=\frac{377}2=188.5\,\Omega.
$$

Consequently:

$$
\boxed{\eta_1=377\,\Omega,\qquad\eta_2=188.5\,\Omega}.
$$

**2. Reflection and refraction angles.** The reflection law gives $\theta_r=\theta_i=30^\circ$. Snell's law gives the refraction angle:

$$
n_1\sin\theta_i=n_2\sin\theta_t.
$$

Substituting the values:

$$
1\times\sin30^\circ=2\sin\theta_t.
$$

Since $\sin30^\circ=0.5$:

$$
\sin\theta_t=\frac{0.5}2=0.25.
$$

Therefore:

$$
\theta_t=\sin^{-1}(0.25),\qquad \boxed{\theta_t\simeq14.48^\circ}.
$$

The wave enters a higher-index medium and therefore bends toward the normal: $\theta_t<\theta_i$.

**3. TE reflection and transmission coefficients.** The TE electric-field reflection coefficient is:

$$
\Gamma_{\mathrm{TE}}=\frac{\eta_2\cos\theta_i-\eta_1\cos\theta_t}
{\eta_2\cos\theta_i+\eta_1\cos\theta_t}.
$$

Using $\cos30^\circ\simeq0.866$ and $\cos14.48^\circ\simeq0.968$:

$$
\Gamma_{\mathrm{TE}}
=\frac{(188.5)(0.866)-(377)(0.968)}{(188.5)(0.866)+(377)(0.968)}
=\frac{163.24-364.94}{163.24+364.94}
\simeq-0.382.
$$

The negative reflection coefficient indicates a $180^\circ$ phase reversal of the reflected electric field. For the tangential electric field in TE polarization:

$$
\tau_{\mathrm{TE}}=1+\Gamma_{\mathrm{TE}}.
$$

Therefore:

$$
\tau_{\mathrm{TE}}=1-0.382,\qquad\boxed{\tau_{\mathrm{TE}}\simeq0.618}.
$$

**4. Reflected and transmitted field amplitudes.** The reflected electric-field amplitude is:

$$
E_{0r}=\Gamma_{\mathrm{TE}}E_{0i}.
$$

Substituting:

$$
E_{0r}=(-0.382)(10),\qquad \boxed{E_{0r}\simeq-3.82\,\mathrm{V/m}}.
$$

The negative sign represents a $180^\circ$ phase difference relative to the incident field. Its magnitude is $|E_{0r}|\simeq3.82\,\mathrm{V/m}$.

The transmitted electric-field amplitude is:

$$
E_{0t}=\tau_{\mathrm{TE}}E_{0i}.
$$

Therefore:

$$
E_{0t}=(0.618)(10),\qquad\boxed{E_{0t}\simeq6.18\,\mathrm{V/m}}.
$$

**5. Power coefficients and conservation.** For lossless media, the reflected power fraction is the squared magnitude of the field reflection coefficient:

$$
R=|\Gamma_{\mathrm{TE}}|^2.
$$

Therefore:

$$
R=(-0.382)^2\simeq0.146,\qquad\boxed{R\simeq14.6\%}.
$$

The transmitted power fraction is not simply $|\tau_{\mathrm{TE}}|^2$, because both the impedance and propagation angle change. For TE polarization:

$$
T=\frac{\eta_1\cos\theta_t}{\eta_2\cos\theta_i}|\tau_{\mathrm{TE}}|^2.
$$

Substituting:

$$
T=\frac{(377)(0.968)}{(188.5)(0.866)}(0.618)^2
\simeq2.236(0.382)\simeq0.854.
$$

Approximately:

$$
\boxed{T\simeq85.4\%}.
$$

Checking energy conservation:

$$
R+T=0.146+0.854,\qquad\boxed{R+T=1}.
$$

Energy is conserved. Neither medium absorbs power, so $A=0$ and $R+T+A=1$.
:::
::::

:::{note} Which field coefficient and which power direction?
At Brewster incidence a surviving reflected wave is TE only if the input contains a TE component; a purely TM input has zero reflection. In lossless half-space total internal reflection, the transmitted net normal power is zero, while an evanescent field and tangential energy flux may remain. The source's TM transmission coefficient refers to the full electric amplitude, whereas the numerical model below uses the tangential electric component. Its continuity relation is t=1+r. Compare complete vector fields and bases before comparing signs or amplitudes.
:::

(ch02-section-06)=
### Computational connection: Derive the interface response


Take the plane of incidence to be $xz$. **TE** has electric field along $y$. **TM** has magnetic field along $y$ and electric field in the $xz$ plane. We compare the same tangential electric component on each side: $E_y$ for TE and $E_x$ for TM. Define

$$
s=n_i\sin\theta_i,\qquad q_j=\frac{k_{z,j}}{k_0}=\sqrt{n_j^2-s^2},
$$

choosing the outgoing/decaying root, with nonnegative real and nonpositive imaginary parts for these lossless positive-index half-spaces. Our dimensionless tangential wave admittance is

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

(ch02-section-07)=
### Computational connection: Brewster, evanescence, and cutoff


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
q_t=(-i)\gamma,\qquad\gamma=\sqrt{s^2-n_t^2}>0,\qquad
\widetilde E_t\propto e^{-ik_xx}e^{-k_0\gamma z}.
$$

The transmitted field can be nonzero while $\operatorname{Re}Y_t=0$, giving $T=0$ and $R=1$. Its amplitude decay length is $\ell_E=1/(k_0\gamma)$; the intensity decay length is half as large. It is incorrect to interpret $T=0$ as proof that the entire transmitted field vanishes. It is also incorrect to interpret a nonzero evanescent amplitude as a nonzero outgoing normal-power channel.

```{figure} ../assets/chapter-02/tir-field.png
:alt: Original analytical total-internal-reflection field and evanescent decay visualization.

The field penetrates the second medium while its net transmitted normal power is zero for this single, semi-infinite lossless interface. Adding another nearby interface would define a different tunneling problem.
```

At exact grazing cutoff, formulas containing $1/q_t$ need limiting treatment. For TM, $t$ defined from tangential $E_x$ tends to zero, but the factor relating $E_z$ to $E_x$ can diverge so that the complete transmitted field need not vanish. Approach cutoff from either side and report it separately; do not evaluate a singular intermediate admittance as if it were an ordinary finite propagating channel.

