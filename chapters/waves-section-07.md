---
title: "2.7 Key parameters in material and lossy media"
short_title: "2.7 Key parameters in material and lossy media"
---

(ch02-source-07)=
# 2.7 Key parameters in material and lossy media

In real media, such as FR4 or Rogers substrates and gold or copper metasurface layers, waves do more than change phase: they lose energy too. Section 2.5 described this with $\gamma=\alpha+j\beta$. To understand the physics of loss better, let's add several key parameters to our design toolbox.

### 2.7.1 Complex permittivity and loss tangent

In a real material, dielectric polarization responds with a small lag behind the electric field. This phase lag converts some wave energy into heat. We model it using complex permittivity:

$$
\varepsilon^*=\varepsilon'-j\varepsilon''.
$$

The real part, $\varepsilon'$, describes the material's ability to store electric energy; the imaginary loss parameter, $\varepsilon''$, describes dissipation associated with internal damping.

If conductivity is present as well as dielectric loss, we can gather both into an equivalent complex permittivity:

$$
\varepsilon^*=\varepsilon'-j\left(\varepsilon''+\frac\sigma\omega\right).
$$

For microwave engineers, the most tangible loss measure is the **loss tangent**: the ratio of total dissipative response to the real, energy-storage response:

$$
\tan\delta=\frac{\varepsilon''+\sigma/\omega}{\varepsilon'}.
$$

The smaller $\tan\delta$ is, with $\tan\delta\ll1$, the closer the material is to an ideal dielectric. A very low-loss-tangent substrate is one of the main ingredients in a highly efficient metasurface.

### 2.7.2 Complex intrinsic impedance

In a lossless medium, wave impedance is real. In a lossy medium it becomes complex:

$$
\eta=\sqrt{\frac{j\omega\mu}{\sigma+j\omega\varepsilon}}.
$$

A complex impedance means that electric and magnetic fields are no longer exactly in phase, reminding us that the medium absorbs wave energy. In metamaterial absorbers, carefully matching this complex response to free-space impedance is a key to **perfect absorption**.

### 2.7.3 Skin depth

A wave's amplitude decreases as it advances into a lossy material. The distance over which amplitude falls to $1/e$, about 37% of its original value, is its penetration or **skin depth, $\delta$**:

$$
\delta=\frac1\alpha.
$$

For a good conductor, such as copper or gold in the suitable regime, $\sigma\gg\omega\varepsilon$, and the familiar skin-depth approximation is:

$$
\delta\approx\sqrt{\frac2{\omega\mu\sigma}}.
$$

This has an important engineering message: at high frequencies such as microwave and terahertz frequencies, waves penetrate only a small distance into metal. Induced currents concentrate near the surface, in layers on micrometer or nanometer scales. Metasurface metal layers are therefore usually made somewhat thicker than several skin depths.

### 2.7.4 Complex refractive index in optics

If you are interested in optical metasurfaces, you probably know that optics and photonics often use refractive index rather than permittivity and permeability. In a lossy medium, index also becomes complex:

$$
\widetilde n=n-j\kappa.
$$

The real part, $n$, determines phase behavior; the **extinction coefficient**, $\kappa$, determines attenuation. It is directly related to $\alpha$ and is essential when analyzing plasmonic structures.

::::{admonition} Textbook example: FR4 substrate and copper layer
:class: book-exercise

A metasurface operates at $f=10\,\mathrm{GHz}$ on an FR4 substrate. Its substrate and copper-layer properties are:

$$
\varepsilon_r'=4.2,\qquad \tan\delta=0.02,\qquad
\sigma_{\mathrm{Cu}}=5.8\times10^7\,\mathrm{S/m}.
$$

Assume the substrate is nonmagnetic, $\mu_r=1$, and its conduction loss is negligible compared with dielectric loss.

1. Calculate the imaginary relative-permittivity parameter, $\varepsilon_r''$.
2. Find copper skin depth at $10\,\mathrm{GHz}$.
3. If the copper is $5\,\mu\mathrm m$ thick, what percentage of the initial electric-field amplitude remains at its far side?
4. Interpret the result for metasurface design.

:::{dropdown} Show / hide answer
**1. Imaginary relative permittivity.** Neglecting substrate conductivity, the loss tangent is:

$$
\tan\delta=\frac{\varepsilon_r''}{\varepsilon_r'}.
$$

Therefore:

$$
\varepsilon_r''=\varepsilon_r'\tan\delta.
$$

Substituting the values:

$$
\varepsilon_r''=4.2(0.02),\qquad \boxed{\varepsilon_r''=0.084}.
$$

The substrate's complex relative permittivity, with the question's convention, is therefore:

$$
\boxed{\varepsilon_r^*=4.2-j0.084}.
$$

The negative imaginary sign is consistent with $e^{j\omega t}$.

**2. Copper skin depth.** For a good conductor:

$$
\delta_s=\sqrt{\frac2{\omega\mu\sigma}}.
$$

First calculate angular frequency:

$$
\omega=2\pi f=2\pi(10\times10^9)\approx6.283\times10^{10}\,\mathrm{rad/s}.
$$

Also:

$$
\mu=\mu_0=4\pi\times10^{-7}\,\mathrm{H/m}.
$$

Now:

$$
\delta_s=\sqrt{\frac2{(6.283\times10^{10})(4\pi\times10^{-7})(5.8\times10^7)}}.
$$

The result is:

$$
\delta_s\approx6.6\times10^{-7}\,\mathrm m,
\qquad \boxed{\delta_s\approx0.66\,\mu\mathrm m}.
$$

**3. Field at the far side of the copper.** The amplitude-decay relation is:

$$
\frac{E(d)}{E_0}=e^{-d/\delta_s}.
$$

The thickness is $d=5\,\mu\mathrm m$, so:

$$
\frac d{\delta_s}=\frac5{0.66}\approx7.58.
$$

Consequently:

$$
\frac{E(d)}{E_0}=e^{-7.58}\approx5.1\times10^{-4}.
$$

Expressed as a percentage:

$$
\frac{E(d)}{E_0}\times100\approx0.051\%,
\qquad \boxed{E(d)\approx0.051\%\,E_0}.
$$

Only about five-hundredths of a percent of the original field amplitude remains at the far side.

**4. Interpretation.** The copper is about $d/\delta_s\approx7.6$ skin depths thick. The field is strongly attenuated before reaching the far side, and penetration into the remaining thickness is very small.

We can therefore conclude that a five-micrometer thickness is suitable for limiting penetration into the copper in this example.

Metasurface metal thickness is usually chosen to exceed several skin depths. Here it exceeds five, so the layer behaves electromagnetically as a relatively thick conductor. Real designs must still account for surface roughness, oxidation, fabrication quality and surface-current losses.
:::
::::

:::{note} Count each loss mechanism once
The source uses the superscript star to denote complex permittivity, not complex conjugation. Conductivity may be kept explicitly or included in effective complex permittivity; do not count the same loss twice. The good-conductor skin-depth approximation requires its stated conductivity-dominance conditions and is not a general optical-metal model. In a dispersive medium, stored energy cannot in general be read from the real part of permittivity alone.
:::

