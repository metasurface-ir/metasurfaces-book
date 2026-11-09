---
title: "2.10 Plane-wave polarization"
short_title: "2.10 Plane-wave polarization"
---

(ch02-source-10)=
# 2.10 Plane-wave polarization

**Polarization** is a fundamental electromagnetic-wave property. It describes how the direction and geometry of the electric-field vector evolve with time at a fixed point, or equivalently within an equiphase plane. Because many structures respond differently to different electric-field directions, polarization is central to antennas, filtering networks and especially metasurfaces.

Polarization control is an important form of metasurface field engineering. Cells can be designed to preserve, attenuate, separate or completely transform incident polarization. Polarization converters, selective surfaces, and co-/cross-polarized power control therefore all depend on polarization analysis.

### 2.10.1 Equiphase planes and component representation

For a plane wave propagating along $\hat{\mathbf a}_n$, phase depends on $\omega t-\beta\hat{\mathbf a}_n\cdot\mathbf r$. Surfaces satisfying the following condition are equiphase planes:

$$
\beta\hat{\mathbf a}_n\cdot\mathbf r=\mathrm{constant}.
$$

They are perpendicular to propagation, and temporal field changes have the same phase across each plane.

To study polarization, resolve electric field into two orthogonal components transverse to propagation. For propagation along $+z$, the instantaneous field can be written:

$$
\mathbf E(z,t)=\hat{\mathbf a}_x E_{0x}\cos(\omega t-\beta z+\phi_x)
+\hat{\mathbf a}_y E_{0y}\cos(\omega t-\beta z+\phi_y).
$$

The quantities $E_{0x}$ and $E_{0y}$ are component amplitudes; $\phi_x$ and $\phi_y$ are their initial phases. Their relative amplitudes and phases determine polarization: the path traced by the electric-vector tip over one temporal cycle in an equiphase plane.

### 2.10.2 Types of plane-wave polarization

We generally classify polarization into three main types:

**A) Linear polarization:** the field-vector tip oscillates along a straight line transverse to propagation. This occurs when the relative phase, $\Delta\phi=\phi_y-\phi_x$, is zero or an integer multiple of $\pi$:

$$
\phi_y-\phi_x=m\pi,\qquad m\in\mathbb Z.
$$

The component ratio is then constant. The field's direction stays on the same line while its magnitude and sign change with time. Horizontal, vertical and tilted polarizations are different linear cases.

**B) Circular polarization:** equal orthogonal component amplitudes with phase difference $\pm\pi/2$ make the tip trace a circle. Field magnitude remains constant while its direction rotates uniformly:

$$
E_{0x}=E_{0y},\qquad \phi_y-\phi_x=\pm\frac\pi2.
$$

Rotation direction distinguishes right-handed, RHCP, and left-handed, LHCP, circular polarizations. Because references differ in whether they look with or against wave propagation, every analysis should state its viewing convention explicitly.

**C) Elliptical polarization:** the general case. The component amplitudes differ, or their relative phase differs from zero, $\pi$ or $\pm\pi/2$, and the vector tip traces an ellipse. Linear and circular polarization can be regarded as special limiting cases of elliptical polarization.

Two parameters commonly describe its geometry:

- **Ellipse tilt, $\psi$:** the major-axis angle relative to the reference axis.
- **Ellipticity angle, $\chi$:** describes the minor-to-major-axis ratio and rotation sense.

### 2.10.3 Stokes parameters and the Poincaré sphere

**Stokes parameters**, commonly $S_0,S_1,S_2,S_3$, provide a compact, comprehensive description of total intensity and polarization. Their advantage is that polarization can be described without tracking instantaneous field phase directly.

Normalizing the Stokes parameters represents a polarization state as a point on a unit **Poincaré sphere**. In this geometric picture:

- The equator represents linear polarizations.
- The two poles represent opposite circular polarizations.
- Other surface points represent elliptical polarizations.

The sphere is useful for analyzing and tracking polarization transformations, comparing states, and interpreting anisotropic-metasurface responses.

### 2.10.4 Why polarization matters in metasurfaces and communication systems

Polarization choice or control is often the foundation of system operation rather than a secondary feature. A metasurface may respond very differently to different polarizations. Important applications include:

- **Polarization conversion:** linear to circular, circular to linear, or rotation between linear directions, including cross-polarization conversion.
- **Polarization separation:** structures transparent to one polarization and reflective or absorbing to its orthogonal partner.
- **Channel-capacity increase:** orthogonal polarizations can reduce interference and support polarization multiplexing, potentially doubling information channels.
- **Satellite communications:** circular polarization reduces sensitivity to relative antenna rotation and effects such as ionospheric Faraday rotation.
- **Polarimetric radar:** the reflected polarization-scattering matrix helps identify target geometry and material properties.

### 2.10.5 Polarization mismatch and polarization loss factor

If incident polarization does not match a receiving antenna, sensor or metasurface, not all incident power is received. This **polarization mismatch** reduces system efficiency.

For two linear polarizations separated by angle $\theta$, the **polarization loss factor, PLF**, is:

$$
\mathrm{PLF}=\cos^2\theta.
$$

This simple expression applies only to two linear polarizations. In general, PLF comes from the overlap, or inner product, of the incident and receiving complex polarization vectors.

In polarization-transforming metasurface analysis, the source describes maximizing the desired co-polarized component and minimizing unwanted cross-polarized power. **Cross-polarization ratio** and related purity measures quantify the performance of polarization-transforming surfaces.

::::{admonition} Textbook example: polarization trajectory and received power
:class: book-exercise

A plane wave propagating along $+z$ has electric field:

$$
\mathbf E(z,t)=4\hat{\mathbf x}\cos(\omega t-\beta z)
+3\hat{\mathbf y}\cos\left(\omega t-\beta z+\frac\pi2\right)\,\mathrm{V/m}.
$$

Answer the following questions:

1. Identify its polarization type.
2. Find the electric-vector-tip trajectory in an equiphase plane.
3. Calculate axial ratio.
4. Find PLF for a linearly polarized receiver at $30^\circ$ to the $x$ axis.

:::{dropdown} Show / hide answer
**1. Polarization type.** Define the phase variable:

$$
\psi=\omega t-\beta z.
$$

Consequently:

$$
E_x=4\cos\psi,\qquad E_y=3\cos\left(\psi+\frac\pi2\right).
$$

Using $\cos(\psi+\pi/2)=-\sin\psi$ gives:

$$
E_y=-3\sin\psi.
$$

The component amplitudes are unequal, $E_{0x}=4$ and $E_{0y}=3$, with relative phase $\Delta\phi=\pi/2$. The polarization is therefore **elliptical**.

**2. Vector-tip trajectory.** From $E_x=4\cos\psi$, obtain $\cos\psi=E_x/4$. From $E_y=-3\sin\psi$, obtain $\sin\psi=-E_y/3$. Use $\cos^2\psi+\sin^2\psi=1$:

$$
\left(\frac{E_x}4\right)^2+\left(-\frac{E_y}3\right)^2=1.
$$

Therefore:

$$
\boxed{\frac{E_x^2}{16}+\frac{E_y^2}9=1}.
$$

This is an ellipse with major axis along $x$ and minor axis along $y$.

**3. Axial ratio.** The major and minor semiaxes are 4 and 3, respectively, so:

$$
\mathrm{AR}=\frac{E_{\mathrm{major}}}{E_{\mathrm{minor}}}=\frac43.
$$

Thus:

$$
\boxed{\mathrm{AR}=1.33},\qquad \mathrm{AR}=4:3.
$$

**4. Polarization loss factor.** The receiver's unit linear-polarization vector at $30^\circ$ is:

$$
\hat{\mathbf u}_r=\cos30^\circ\hat{\mathbf x}+\sin30^\circ\hat{\mathbf y}.
$$

We cannot apply $\mathrm{PLF}=\cos^2\theta$ directly to this elliptical wave, because that expression concerns two linear states. Use complex polarization overlap instead.

With $e^{j\omega t}$, the electric phasor is:

$$
\mathbf E_0=4\hat{\mathbf x}+j3\hat{\mathbf y}.
$$

Its normalized polarization vector is:

$$
\hat{\mathbf e}_i=\frac{4\hat{\mathbf x}+j3\hat{\mathbf y}}{\sqrt{4^2+3^2}}
=\frac{4\hat{\mathbf x}+j3\hat{\mathbf y}}5.
$$

The polarization loss factor follows from:

$$
\mathrm{PLF}=|\hat{\mathbf u}_r^{\,*}\cdot\hat{\mathbf e}_i|^2.
$$

Therefore:

$$
\mathrm{PLF}=\left|\frac{4\cos30^\circ+j3\sin30^\circ}5\right|^2.
$$

The real and imaginary contributions are in quadrature, so:

$$
\mathrm{PLF}=\frac{16\cos^230^\circ+9\sin^230^\circ}{25}.
$$

Using $\cos^230^\circ=3/4$ and $\sin^230^\circ=1/4$ gives:

$$
\mathrm{PLF}=\frac{16(3/4)+9(1/4)}{25}
=\frac{12+2.25}{25}=\frac{14.25}{25}.
$$

Thus:

$$
\boxed{\mathrm{PLF}=0.57},\qquad \boxed{\mathrm{PLF}=57\%}.
$$

The receiver therefore accepts 57% of the incident power through polarization overlap; about 43% is not received because of polarization mismatch.
:::
::::

:::{note} Check the ellipse rather than only the amplitudes
Unequal component amplitudes alone do not guarantee elliptical polarization: in-phase or opposite-phase coherent components still trace a line. A nondegenerate ellipse requires two nonzero components and a phase difference other than an integer multiple of pi. Fully polarized coherent states lie on the Poincaré sphere; partially polarized states lie inside it. Co- and cross-polarized labels specify a basis, not which output is desirable: a converter may intentionally maximize the cross-polarized channel.
:::

(ch02-section-04)=
### Computational connection: Make polarization visible

Time convention in this computational connection: $e^{+i\omega t}$.


At a fixed point, the tip of the transverse electric field can trace a line, ellipse, or circle over one period. Write a unit-norm Jones vector for propagation along positive $z$ as

$$
\mathbf j=\begin{bmatrix}\cos\alpha\\e^{i\delta}\sin\alpha\end{bmatrix},\qquad
\mathbf j^\dagger\mathbf j=1.
$$

Here $\alpha$ controls the component magnitudes and $\delta$ is the relative phase of $E_y$ with respect to $E_x$. At $z=0$,

$$
E_x(t)=\cos\alpha\cos\omega t,\qquad
E_y(t)=\sin\alpha\cos(\delta+\omega t).
$$

For $\delta=0$, the vector remains on a line. For $\alpha=45^\circ$ and $\delta=90^\circ$, the normalized state is $(1,i)^T/\sqrt2$: starting at positive $E_x$, the tip moves toward negative $E_y$ as time increases. This description specifies the axes and time convention without relying on a potentially ambiguous handedness label.

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

