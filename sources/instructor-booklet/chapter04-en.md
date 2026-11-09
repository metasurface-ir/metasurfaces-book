## 4.1 Introduction: a world of repeating patterns

Dear friends, welcome to Chapter 4! In the previous chapter, we learned how to design our Lego bricks—the meta-atoms—and give them shape in software. In the real world, however, a metasurface contains tens, hundreds, and sometimes millions of these bricks. What happens when an electromagnetic wave meets this enormous army of cells? Does the wave see each cell separately?

The answer is no! The wave experiences a collective response. In this chapter, we want to look at the problem from the wave’s point of view. We want to understand how the physics changes when a wave enters a setting with repeating patterns. We will meet a powerful tool called Floquet’s theorem, the common language of periodic structures. It explains why the spacing between our bricks must not exceed a certain limit—otherwise thieves called “grating lobes” can steal our wave’s energy!

## 4.2 Periodic electromagnetic structures and the unit cell

In metasurface design, we almost always encounter some form of spatial periodicity. A unit cell repeats along one or two axes in the plane and forms a regular array.

If repetition occurs in only one direction, we call the structure one-dimensionally periodic. If it occurs along two in-plane directions, we call it two-dimensionally periodic. For example, a cell repeated with period $p_x$ along $x$ and period $p_y$ along $y$ forms a two-dimensional metasurface array.

The unit cell plays exactly the role of a basic building block, and the entire structure is assembled from its repeated copies. Why does this matter? If the structure is infinitely periodic, we do not need to simulate the whole large array! Mathematics lets us obtain the field behavior throughout an infinite city by looking at just one house. This is where Mr. Floquet enters the story.

## 4.3 Floquet theorem: the language of periodicity

Floquet’s theorem is one of the most fundamental tools for analyzing periodic structures. It states that, in a periodic medium or structure, the electromagnetic fields in neighboring cells differ only by a specified phase factor.

In other words, the shape of the field repeats identically in different cells, but its phase changes from one cell to the next.

Let us use a metaphor. Imagine walking down a street lined with exactly identical trees, planted at exactly equal spacings. The scene—the field-amplitude pattern—you see beside the first tree is the same as the scene beside the tenth! What has changed is your spatial position, representing phase, along the street.

### Mathematical statement of Floquet’s theorem

Suppose a structure repeats along $x$ with period $p$. If its electric field at a point is $E(x)$, Floquet’s theorem gives the field in the next cell, at $x+p$, as follows:

$$
E(x+p)=E(x)e^{-ik_xp}.
$$

Here:

- $p$ is the structural period along $x$.
- $k_x$ is the tangential wavevector component along $x$.
- $e^{-ik_xp}$ is the phase factor between neighboring cells.

This relation shouts: “Move from one cell to the next, and the overall field pattern repeats, while its phase turns by an amount $k_xp$!”

If the structure is periodic along both $x$ and $y$, as in a two-dimensional metasurface, the more general relation is:

$$
E(x+p_x,y+p_y)=E(x,y)e^{-i(k_xp_x+k_yp_y)}.
$$

Alternatively, write the translations along each direction separately:

$$
E(x+p_x,y)=E(x,y)e^{-ik_xp_x}.
$$

$$
E(x,y+p_y)=E(x,y)e^{-ik_yp_y}.
$$

In very simple language, Floquet’s theorem tells us: “If the structure repeats, repeat the field too—just shift its phase!”

## 4.4 Tangential wavevector and incidence angle

To understand $k_x$ and $k_y$, picture a plane wave arriving at our metasurface at angle $\theta$ from the normal. If the surface lies in the $xy$ plane and the wave propagates in the $xz$ plane, its tangential wavevector along $x$ is:

$$
k_x=k_0\sin\theta.
$$

Here $k_0=2\pi/\lambda_0$ is the free-space wavenumber and $\lambda_0$ is the wavelength. The phase difference between neighboring cells along $x$ therefore becomes:

$$
\Delta\phi=k_xp=k_0p\sin\theta.
$$

This relation is extremely important! Why? It shows that oblique illumination excites different cells with different phases. The first cell receives one phase, and its neighbor feels the wave slightly later and receives another.

:::{admonition} Example 1: phase difference between neighboring cells
:class: tip

A metasurface operates at $10\,\mathrm{GHz}$ with period $p=10\,\mathrm{mm}$. The wavelength at this frequency is $\lambda_0=30\,\mathrm{mm}$. Find the neighboring-cell phase difference when the wave arrives at $\theta=30^\circ$.

```{dropdown} Show the complete worked answer

$$
\Delta\phi=k_0p\sin\theta=\left(\frac{2\pi}{30}\right)\times10\times\sin30^\circ.
$$

$$
\Delta\phi=\left(\frac{2\pi}{30}\right)\times10\times0.5=\frac{\pi}{3}.
$$

The neighboring-cell phase difference is therefore $60^\circ$.

```
:::

**Golden tip:** at normal incidence, $\theta=0$, so $\sin0=0$ and $\Delta\phi=0$. All metasurface cells are then excited in phase and at the same time.

## 4.5 Floquet modes and diffraction orders

Floquet’s theorem does more than connect fields in neighboring cells. It reveals a greater secret: the field scattered by a periodic structure can be decomposed into several branches, or spatial modes!

When a wave meets a periodic array, the repeating structure can add spatial momentum to the wave or subtract it. For a one-dimensional structure, the tangential wavenumber of Floquet order $m$ is:

$$
k_{x,m}=k_x+\frac{2\pi m}{p}.
$$

Here:

- $m=0,\pm1,\pm2,\ldots$ labels the Floquet or diffraction order.
- $k_x$ is the incident wave’s initial tangential momentum.
- $2\pi m/p$ is the spatial momentum added by our periodic lattice.

For a two-dimensional structure, extend the relation along both directions:

$$
k_{x,m}=k_x+\frac{2\pi m}{p_x}.
$$

$$
k_{y,n}=k_y+\frac{2\pi n}{p_y}.
$$

In simple terms, each Floquet order $(m,n)$ is a possible pathway for the wave’s energy. Order zero, $m=0$, is the principal, well-behaved reflection or transmission route. The higher orders, $m=\pm1,\pm2,\ldots$, are the mischievous beams that try to divert energy into other directions!

## 4.6 Propagation or evanescence of Floquet modes

For each Floquet order, the normal wavenumber $k_z$ follows:

$$
k_{z,mn}=\sqrt{k_0^2-k_{x,m}^2-k_{y,n}^2}.
$$

Here we meet an interesting physical fork in the road:

1. If the radicand is **positive**, $k_z$ is real and that order can propagate through space as a real beam.
2. If the radicand is **negative**, $k_z$ is imaginary. The order becomes an **evanescent wave** that stays close to the surface and cannot travel to the far field.

The source therefore writes the propagation condition as:

$$
k_{x,m}^2+k_{y,n}^2\le k_0^2.
$$

## 4.7 Grating lobes: energy thieves

One of our most important jobs as metasurface designers is to prevent unwanted Floquet modes from entering the propagation region. These unwanted propagating diffraction modes are called **grating lobes**. They are energy thieves and can severely reduce our design’s efficiency.

For normal incidence, $k_x=0$, on a one-dimensional structure, the tangential component of order $m$ is:

$$
k_{x,m}=\frac{2\pi m}{p}.
$$

To prevent the first orders, $m=\pm1$, from propagating, their tangential momentum must exceed $k_0$, making the preceding section’s radicand negative:

$$
\left|\frac{2\pi}{p}\right|>k_0\quad\Longrightarrow\quad\frac{2\pi}{p}>\frac{2\pi}{\lambda_0}\quad\Longrightarrow\quad p<\lambda_0.
$$

To escape the energy thieves at normal incidence, the essential condition is therefore that the period $p$ be smaller than the wavelength.

In metasurfaces, we usually go further and choose $p<\lambda_0/2$, or even $p<\lambda_0/3$. The source describes this as making the structure appear completely homogeneous to the wave, without grating lobes or unwanted diffraction.

:::{admonition} Example: a 20 mm period
:class: tip

Let $p=20\,\mathrm{mm}$ and $f=10\,\mathrm{GHz}$, so $\lambda_0=30\,\mathrm{mm}$. What happens to the first Floquet orders?

```{dropdown} Show the complete worked answer

Because $p<\lambda_0$, the first orders do not propagate: they remain evanescent. In the source’s intuitive description, all our energy safely stays in order zero, $m=0$.

```
:::

:::{admonition} Example: a 40 mm period
:class: tip

At the same frequency, what happens if we build larger cells with $p=40\,\mathrm{mm}$?

```{dropdown} Show the complete worked answer

Because $p>\lambda_0$, the first orders escape into the propagation region. Our energy can now split: some follows the main route and some goes into unwanted diffraction.

```
:::

## 4.8 Diffraction angles of Floquet orders

If the surrounding medium is free space, it is easy to calculate each Floquet order’s propagation angle using $k_{x,m}=k_0\sin\theta_m$. Substituting the previous relations gives a familiar and beautiful equation:

$$
\sin\theta_m=\sin\theta_i+\frac{m\lambda_0}{p}.
$$

This relation tells us the angle at which order $m$ is launched! Remember, however, that a real beam angle exists only if the right-hand side lies between $-1$ and $1$: a sine cannot lie outside that interval.

:::{admonition} Example: diffraction angles for a 45 mm period
:class: tip

Let $p=45\,\mathrm{mm}$, $f=10\,\mathrm{GHz}$, $\lambda_0=30\,\mathrm{mm}$, and normal incidence $\theta_i=0$. What happens to the first and second positive orders?

```{dropdown} Show the complete worked answer

For the first order, $m=1$:

$$
\sin\theta_1=0+\frac{30}{45}=0.667\quad\Longrightarrow\quad\theta_1\approx41.8^\circ.
$$

The source describes an unwanted beam propagating at $41.8^\circ$! For the second order, $m=2$, the sine would be $1.33$, which is impossible; the second order therefore does not propagate.

```
:::

## 4.9 Periodic boundaries and Floquet ports in simulation

Now we understand why Chapter 3 used periodic boundaries and Floquet ports.

Periodic boundaries—the room-of-mirrors metaphor—in CST or HFSS numerically impose the phase relation $E(x+p)=E(x)e^{-ik_xp}$ on the unit-cell walls. A Floquet port is a window that can inject or receive energy separately in the Floquet modes $(m,n)$ and provide the amplitude and phase plots extracted in the previous chapter.

## 4.10 Floquet analysis and generalized Snell law

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
