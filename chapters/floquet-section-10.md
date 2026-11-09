---
title: "4.10 Floquet analysis and generalized Snell law"
---

# 4.10 Floquet analysis and generalized Snell law

In earlier chapters we met generalized Snell’s law:

$$
n_2\sin\theta_t-n_1\sin\theta_i=\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx}.
$$

When phase varies linearly, $\Phi(x)=\beta_sx$, its gradient $d\Phi/dx$ plays exactly the role of additional tangential momentum $\Delta k_x$.

Floquet analysis likewise shows that a periodic structure adds momentum $\Delta k_x=2\pi m/p$ to the wave.

Generalized Snell’s law and Floquet analysis are two sides of the same coin! Both describe a change in wave momentum. Snell’s law is usually expressed for a continuous phase profile, while Floquet analysis describes the discrete modes of a gridded, periodic structure.

:::{admonition} Textbook problem: six questions for oblique illumination
:class: tip

A metasurface periodic only along $x$ has period:

$$
p=25\,\mathrm{mm}.
$$

It operates at frequency:

$$
f=10\,\mathrm{GHz}.
$$

A plane wave arrives at an angle from the surface normal of:

$$
\theta_i=20^\circ.
$$

Assume free space surrounds the structure and that it is periodic only along x. Using Floquet analysis:

1. Calculate the free-space wavenumber and the incident tangential component.
2. Calculate the phase difference between neighboring unit cells.
3. Calculate the tangential wavenumbers for orders zero, positive one and negative one.
4. Determine which orders propagate and which are evanescent.
5. Calculate the propagation angles of the propagating orders.
6. Does this structure have a grating lobe? Explain.

```{dropdown} Show the complete worked answer

### Problem data

The period, frequency, incidence angle and free-space speed of light are:

$$
p=25\,\mathrm{mm},\qquad f=10\,\mathrm{GHz},\qquad\theta_i=20^\circ,\qquad c=3\times10^8\,\mathrm{m/s}.
$$

The structure is periodic only along x, and its surroundings are free space.

### 1. Wavelength and free-space wavenumber

The free-space wavelength is obtained from:

$$
\lambda_0=\frac{c}{f}.
$$

Substitute the frequency:

$$
\lambda_0=\frac{3\times10^8}{10\times10^9}.
$$

Therefore:

$$
\lambda_0=0.03\,\mathrm m.
$$

Equivalently:

$$
\lambda_0=30\,\mathrm{mm}.
$$

The free-space wavenumber is:

$$
k_0=\frac{2\pi}{\lambda_0}.
$$

Using $\lambda_0=0.03\,\mathrm m$ gives:

$$
k_0=\frac{2\pi}{0.03}.
$$

$$
k_0\simeq209.44\,\mathrm{rad/m}.
$$

### Incident tangential wavenumber

Because incidence is at angle $\theta_i$ from the normal, the tangential component along $x$ is:

$$
k_x=k_0\sin\theta_i.
$$

Substitution gives:

$$
k_x=209.44\sin20^\circ.
$$

Since:

$$
\sin20^\circ\simeq0.342.
$$

We have:

$$
k_x\simeq209.44\times0.342.
$$

Hence:

$$
k_x\simeq71.62\,\mathrm{rad/m}.
$$

### 2. Phase difference between neighboring cells

Floquet’s theorem gives the phase difference as:

$$
\Delta\phi=k_xp.
$$

First convert the period to meters:

$$
p=25\,\mathrm{mm}=0.025\,\mathrm m.
$$

Thus:

$$
\Delta\phi=71.62\times0.025.
$$

$$
\Delta\phi\simeq1.79\,\mathrm{rad}.
$$

To convert radians to degrees:

$$
\Delta\phi_{\rm deg}=1.79\frac{180}{\pi}.
$$

Therefore:

$$
\Delta\phi\simeq102.6^\circ.
$$

The fields in neighboring cells therefore differ in phase by approximately $102.6^\circ$.

### 3. Calculate the Floquet orders

For a one-dimensional structure, the tangential wavenumber of order $m$ is:

$$
k_{x,m}=k_x+\frac{2\pi m}{p}.
$$

First calculate the reciprocal-lattice increment:

$$
\frac{2\pi}{p}=\frac{2\pi}{0.025}.
$$

$$
\frac{2\pi}{p}\simeq251.33\,\mathrm{rad/m}.
$$

**Order zero, $m=0$:**

$$
k_{x,0}=k_x+\frac{2\pi(0)}{p}.
$$

$$
k_{x,0}=71.62\,\mathrm{rad/m}.
$$

**Positive first order, $m=+1$:**

$$
k_{x,+1}=71.62+251.33.
$$

$$
k_{x,+1}\simeq322.95\,\mathrm{rad/m}.
$$

**Negative first order, $m=-1$:**

$$
k_{x,-1}=71.62-251.33.
$$

$$
k_{x,-1}\simeq-179.71\,\mathrm{rad/m}.
$$

### 4. Propagating and evanescent orders

For a one-dimensional structure, the source writes the propagation condition as:

$$
|k_{x,m}|\le k_0.
$$

When this condition holds, the normal wavenumber is real. If instead the following holds, the order is evanescent:

$$
|k_{x,m}|>k_0.
$$

**Check order zero.** Its tangential magnitude is:

$$
|k_{x,0}|=71.62\,\mathrm{rad/m}.
$$

Since:

$$
71.62<209.44.
$$

Order zero propagates.

$$
m=0:\quad\text{propagating}.
$$

**Check the positive first order.**

$$
|k_{x,+1}|=322.95\,\mathrm{rad/m}.
$$

Since:

$$
322.95>209.44.
$$

The positive first order does not propagate; it is evanescent.

$$
m=+1:\quad\text{evanescent}.
$$

**Check the negative first order.**

$$
|k_{x,-1}|=179.71\,\mathrm{rad/m}.
$$

Since:

$$
179.71<209.44.
$$

The negative first order propagates.

$$
m=-1:\quad\text{propagating}.
$$

The two propagating orders are therefore $m=0$ and $m=-1$.

### 5. Propagation angles

The tangential wavenumber and propagation angle of an order are related by:

$$
k_{x,m}=k_0\sin\theta_m.
$$

Therefore:

$$
\sin\theta_m=\frac{k_{x,m}}{k_0}.
$$

The same relation can also be written as:

$$
\sin\theta_m=\sin\theta_i+\frac{m\lambda_0}{p}.
$$

**Angle of order zero.** For $m=0$:

$$
\sin\theta_0=\sin20^\circ.
$$

Consequently:

$$
\theta_0=20^\circ.
$$

This order follows the incident wave’s principal tangential route.

**Angle of the negative first order.** For $m=-1$:

$$
\sin\theta_{-1}=\sin20^\circ-\frac{30}{25}.
$$

$$
\sin\theta_{-1}=0.342-1.2.
$$

$$
\sin\theta_{-1}=-0.858.
$$

Thus:

$$
\theta_{-1}=\sin^{-1}(-0.858).
$$

Therefore:

$$
\theta_{-1}\simeq-59.1^\circ.
$$

The negative sign places this order on the opposite x side from the zero-order direction.

**Angle of the positive first order.** For $m=+1$:

$$
\sin\theta_{+1}=\sin20^\circ+\frac{30}{25}.
$$

$$
\sin\theta_{+1}=0.342+1.2=1.542.
$$

A sine cannot exceed one, so this order has no real propagation angle. It is evanescent.

$$
m=+1:\quad\text{evanescent}.
$$

### 6. Does a grating lobe exist?

A grating lobe becomes possible when a nonzero Floquet order can propagate through space. In this problem, the negative first order propagates at:

$$
\theta_{-1}\simeq-59.1^\circ.
$$

Besides the principal zero order, the source therefore identifies an additional diffraction beam: **this structure has a grating lobe**. It can divert some energy from the principal route and reduce metasurface efficiency.

### Final answer

$$
\lambda_0=30\,\mathrm{mm}.
$$

$$
k_x\simeq71.62\,\mathrm{rad/m}.
$$

$$
\Delta\phi\simeq1.79\,\mathrm{rad}=102.6^\circ.
$$

The Floquet orders are:

$$
m=0:\quad\text{propagating},\quad\theta_0=20^\circ.
$$

$$
m=+1:\quad\text{evanescent}.
$$

$$
m=-1:\quad\text{propagating},\quad\theta_{-1}\simeq-59.1^\circ.
$$

Because the negative first order propagates, the grating-lobe direction is approximately:

$$
\theta_{\rm grating}\simeq-59.1^\circ.
$$

```
:::

:::{note} Supplementary clarification
In the Snell relation, $\Phi$ is a phase-lag profile, so $t=Ae^{-i\Phi}$. The worked answer retains the textbook’s intermediate rounding, including $71.62$, $322.95$ and $-179.71\,\mathrm{rad/m}$. Keeping more digits gives $k_x\simeq71.6325\,\mathrm{rad/m}$ and a phase lag of $102.606^\circ$. The signed translation phase is the negative of that lag. The calculation establishes an open grating-lobe channel near $-59.1^\circ$; the actual power still requires solving scattering.

The source value $71.62$ is reproduced for traceability. Its displayed product $209.44\times0.342$ equals $71.62848$, which would normally round to $71.63$; this small arithmetic/rounding discrepancy does not change any order classification.
:::
