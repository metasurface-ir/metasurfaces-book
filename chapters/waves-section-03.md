---
title: "2.3 Properties and types of electromagnetic media"
short_title: "2.3 Properties and types of electromagnetic media"
---

(ch02-source-03)=
# 2.3 Properties and types of electromagnetic media

In electromagnetic analysis, field behavior depends strongly on the medium in which the fields propagate. Imagine running: an asphalt road, a sandy beach, and water certainly do not feel the same! Electromagnetic waves face the same sort of distinction. A material's intrinsic permittivity, $\varepsilon$, magnetic permeability, $\mu$, and conductivity, $\sigma$, determine how the wave behaves there.

We can therefore classify electromagnetic media from several perspectives:

### 2.3.1 Linear and nonlinear media

- **Linear medium:** the simplest and best-behaved case. Its material parameters, $\varepsilon$, $\mu$, and $\sigma$, are fixed and do not depend on electric- or magnetic-field strength. In simple terms, doubling the field doubles the response. The field-to-flux relationships are straightforward and linear:

$$
D=\varepsilon E,\qquad B=\mu H,\qquad J=\sigma E.
$$

- **Nonlinear medium:** what if increasing field strength changes the medium's behavior? Here material parameters depend directly on the applied field's amplitude and intensity. The relationships no longer form straight lines, and exciting effects such as **harmonic generation** can occur, with many applications in nonlinear optics and advanced metasurfaces.

::::{admonition} Textbook example: a linear material response
:class: book-exercise

A linear medium has permittivity $\varepsilon=4\varepsilon_0$. If its electric field increases to $E=3E_0$, find the new electric flux density in terms of $\varepsilon_0$ and $E_0$.

:::{dropdown} Show / hide answer
For a linear medium:

$$
D=\varepsilon E.
$$

Therefore:

$$
D=(4\varepsilon_0)(3E_0).
$$

Consequently:

$$
\boxed{D=12\varepsilon_0E_0}.
$$

Tripling the field also triples the electric flux density.
:::
::::

### 2.3.2 Homogeneous and inhomogeneous media

- **Homogeneous medium:** its fundamental parameters are identical everywhere and do not depend on position, $(x,y,z)$.
- **Inhomogeneous medium:** its physical properties change from one point to another. In mathematical terms, the parameters are functions of position rather than fixed numbers:

$$
\varepsilon=\varepsilon(x,y,z),\qquad
\mu=\mu(x,y,z),\qquad
\sigma=\sigma(x,y,z).
$$

:::{tip} Metasurface design connection
Creating this “artificial inhomogeneity” is one of the key techniques in metasurface design. By intelligently placing different cells beside one another, we create an inhomogeneous arrangement that bends or reshapes the wavefront as desired!
:::

::::{admonition} Textbook example: is the medium homogeneous?
:class: book-exercise

A medium has $\varepsilon(x,y,z)=\varepsilon_0(2+x)$. Is it homogeneous or inhomogeneous?

:::{dropdown} Show / hide answer
It is inhomogeneous because its permittivity depends on $x$. Even if $\mu$ and $\sigma$ are fixed, spatial dependence of one material parameter is enough to make the medium inhomogeneous.
:::
::::

### 2.3.3 Isotropic and anisotropic media

- **Isotropic medium:** no direction is preferred. Its properties are the same in every direction, so $\varepsilon$ and $\mu$ can be expressed as simple scalars.
- **Anisotropic medium:** its response depends on the direction of the applied field. Walking through it is like walking through a forest whose clear paths run only north to south! Permittivity and permeability must now be described as tensors, or matrices:

$$
\mathbf D=\overline{\overline\varepsilon}\mathbf E,
\qquad
\begin{bmatrix}D_x\\D_y\\D_z\end{bmatrix}
=\begin{bmatrix}
\varepsilon_{xx}&\varepsilon_{xy}&\varepsilon_{xz}\\
\varepsilon_{yx}&\varepsilon_{yy}&\varepsilon_{yz}\\
\varepsilon_{zx}&\varepsilon_{zy}&\varepsilon_{zz}
\end{bmatrix}
\begin{bmatrix}E_x\\E_y\\E_z\end{bmatrix}.
$$

This tensor behavior gives engineers remarkable freedom to control waves in complicated media.

::::{admonition} Textbook example: an anisotropic response
:class: book-exercise

The medium obeys:

$$
\begin{bmatrix}D_x\\D_y\end{bmatrix}
=\begin{bmatrix}2\varepsilon_0&0\\0&5\varepsilon_0\end{bmatrix}
\begin{bmatrix}E_x\\E_y\end{bmatrix}.
$$

If the field points only along $x$, find $D_x$ and $D_y$.

:::{dropdown} Show / hide answer
Matrix multiplication gives:

$$
\begin{bmatrix}D_x\\D_y\end{bmatrix}
=\begin{bmatrix}2\varepsilon_0&0\\0&5\varepsilon_0\end{bmatrix}
\begin{bmatrix}E_0\\0\end{bmatrix}.
$$

Thus:

$$
D_x=2\varepsilon_0E_0,\qquad D_y=0.
$$

Therefore:

$$
\boxed{D_x=2\varepsilon_0E_0,\qquad D_y=0}.
$$

The response coefficients along $x$ and $y$ differ, so the medium is anisotropic.
:::
::::

### 2.3.4 Lossless and lossy media

- **Lossless medium:** a communication engineer's paradise! This ideal medium dissipates no electromagnetic energy as heat. Its conductivity is zero, $\sigma=0$, and its permittivity and permeability have no imaginary parts.
- **Lossy medium:** the case we usually encounter in practice. It has electrical conductivity, $\sigma>0$, or dielectric/magnetic losses represented by imaginary material parameters. The wave gradually loses energy and becomes weaker as it propagates.

::::{admonition} Textbook example: which medium is lossless?
:class: book-exercise

Which of these media is lossless?

A) $\sigma=0$, $\varepsilon=\varepsilon'$ and $\mu=\mu'$.

B) $\sigma=0.01\,\mathrm{S/m}$.

C) $\sigma=0$, $\varepsilon=\varepsilon'-j\varepsilon''$, with nonzero $\varepsilon''$.

:::{dropdown} Show / hide answer
Option A is lossless: conductivity is zero and the material parameters have no imaginary parts. B and C are lossy:

- In B, conductivity is positive.
- In C, permittivity has a nonzero imaginary part.
:::
::::

### 2.3.5 Time-invariant and time-varying media

- **Time-invariant medium:** its material properties do not depend on time. Perform an experiment today and repeat it tomorrow, and the medium behaves in the same way.
- **Time-varying medium:** its parameters change with time, $t$. Imagine a metasurface whose properties change almost instantaneously, in a fraction of a second, perhaps under an applied voltage: this is the frontier of programmable, time-varying metasurfaces!

