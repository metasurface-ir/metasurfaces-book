---
title: "6.2.2 FDTD: the Yee lattice and leapfrog updates"
---

# 6.2.2 FDTD: the Yee lattice and leapfrog updates

Hello again! FEM made us work with a large frequency-domain matrix. Now turn the camera toward time: what happens when a light-speed pulse reaches the metal and dielectric cells? How do fields dance, resonances form and reflection/transmission emerge? This is the appeal of FDTD, introduced by Kane Yee in 1966.

```{figure} ../assets/chapter-06/yee-staggering.svg
:alt: Original schematic of electric edges, magnetic face components and staggered times. This is a grid layout, not an extra physical resonator.

Original schematic of electric edges, magnetic face components and staggered times. This is a grid layout, not an extra physical resonator.
```

Standard explicit FDTD does not solve a giant matrix at every step. Its updates move forward like dominoes. Start from Faraday and conductive Ampère–Maxwell:

$$
\nabla\times\mathbf E=-\mu\frac{\partial\mathbf H}{\partial t},\qquad\nabla\times\mathbf H=\epsilon\frac{\partial\mathbf E}{\partial t}+\sigma\mathbf E.
$$

The electric curl changes the magnetic field and the magnetic curl changes the electric field. Yee’s idea was to stagger them in both space and time so that they advance one another in a leapfrog sequence.

## 1. Spatial and temporal staggering

Put electric components on cell edges and magnetic components at face centers. Four electric edges surround a magnetic face flux, mimicking the integral curl relation. The electric components are evaluated at integer times; magnetic components are at half times. This supports centered, second-order differences in smooth regions.

$$
t_E=n\Delta t,(n+1)\Delta t,\ldots,\qquad t_H=(n-\tfrac12)\Delta t,(n+\tfrac12)\Delta t,\ldots.
$$

| Component | Position in cell indices | Time |
|---|---|---|
| $E_x$ | $(i+\frac12,j,k)$ | $n\Delta t$ |
| $E_y$ | $(i,j+\frac12,k)$ | $n\Delta t$ |
| $E_z$ | $(i,j,k+\frac12)$ | $n\Delta t$ |
| $H_x$ | $(i,j+\frac12,k+\frac12)$ | $(n+\frac12)\Delta t$ |
| $H_y$ | $(i+\frac12,j,k+\frac12)$ | $(n+\frac12)\Delta t$ |
| $H_z$ | $(i+\frac12,j+\frac12,k)$ | $(n+\frac12)\Delta t$ |

The notation records spatial and time counters compactly:

$$
F(i\Delta x,j\Delta y,k\Delta z,n\Delta t)\equiv F^n(i,j,k).
$$

## 2. Derive the updates step by step

### Central differences

Taylor expansion gives symmetric spatial and temporal approximations with second-order truncation error:

$$
\frac{df}{dx}(x_0)=\frac{f(x_0+\Delta x/2)-f(x_0-\Delta x/2)}{\Delta x}+\mathcal O(\Delta x^2).
$$

$$
\frac{\partial f}{\partial t}(t_0)=\frac{f(t_0+\Delta t/2)-f(t_0-\Delta t/2)}{\Delta t}+\mathcal O(\Delta t^2).
$$

### Magnetic update

Expand the x-component of Faraday. The consistent rearranged equation used by the source’s update is

$$
\frac{\partial H_x}{\partial t}=\frac1\mu\left(\frac{\partial E_y}{\partial z}-\frac{\partial E_z}{\partial y}\right).
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
The first equality on page 130 prints the same spatial difference with $-\mu\partial_tH_x$ on the right, then rearranges it as though the sign were positive. The correct Faraday component is $\partial_yE_z-\partial_zE_y=-\mu\partial_tH_x$; the update immediately below is correct. This is an algebraic typo, not a new convention.
:::

Evaluate at $(i,j+\frac12,k+\frac12)$ and time $n\Delta t$. First write the time difference, then the two spatial differences:

$$
\left.\partial_tH_x\right|^n\approx\frac{H_x^{n+1/2}(i,j+\tfrac12,k+\tfrac12)-H_x^{n-1/2}(i,j+\tfrac12,k+\tfrac12)}{\Delta t}.
$$

$$
D_zE_y^n=\frac{E_y^n(i,j+\tfrac12,k+1)-E_y^n(i,j+\tfrac12,k)}{\Delta z},\quad D_yE_z^n=\frac{E_z^n(i,j+1,k+\tfrac12)-E_z^n(i,j,k+\tfrac12)}{\Delta y}.
$$

Substitute these three differences and multiply by the time step:

$$
\frac{H_x^{n+1/2}-H_x^{n-1/2}}{\Delta t}=\frac1\mu(D_zE_y^n-D_yE_z^n).
$$

$$
\begin{aligned}H_x^{n+1/2}(i,j+\tfrac12,k+\tfrac12)&=H_x^{n-1/2}(i,j+\tfrac12,k+\tfrac12)\\&+\frac{\Delta t}{\mu\Delta z}[E_y^n(i,j+\tfrac12,k+1)-E_y^n(i,j+\tfrac12,k)]\\&-\frac{\Delta t}{\mu\Delta y}[E_z^n(i,j+1,k+\tfrac12)-E_z^n(i,j,k+\tfrac12)].\end{aligned}
$$

See how direct it is? Future magnetic field equals its previous value plus circulation of the surrounding electric field. Obtain the other components by cyclic permutation.

### Conductive electric update

$$
\epsilon\partial_tE_x+\sigma E_x=\partial_yH_z-\partial_zH_y.
$$

Evaluate this at $(i+\frac12,j,k)$ and $(n+\frac12)\Delta t$. Electric fields are stored at integer times: use a centered difference for the derivative and the average of the two neighboring times for the conductive term.

$$
\left.\partial_tE_x\right|^{n+1/2}\approx\frac{E_x^{n+1}-E_x^n}{\Delta t},\qquad E_x^{n+1/2}\approx\frac{E_x^{n+1}+E_x^n}{2}.
$$

$$
D_yH_z^{n+1/2}=\frac{H_z^{n+1/2}(i+\tfrac12,j+\tfrac12,k)-H_z^{n+1/2}(i+\tfrac12,j-\tfrac12,k)}{\Delta y}.
$$

$$
D_zH_y^{n+1/2}=\frac{H_y^{n+1/2}(i+\tfrac12,j,k+\tfrac12)-H_y^{n+1/2}(i+\tfrac12,j,k-\tfrac12)}{\Delta z}.
$$

$$
(\nabla_h\times\mathbf H)_x^{n+1/2}=D_yH_z^{n+1/2}-D_zH_y^{n+1/2}.
$$

$$
\epsilon\frac{E_x^{n+1}-E_x^n}{\Delta t}+\sigma\frac{E_x^{n+1}+E_x^n}{2}=(\nabla_h\times\mathbf H)_x^{n+1/2}.
$$

Collect the new electric field on the left and the old field on the right:

$$
E_x^{n+1}\left(\frac\epsilon{\Delta t}+\frac\sigma2\right)=E_x^n\left(\frac\epsilon{\Delta t}-\frac\sigma2\right)+(\nabla_h\times\mathbf H)_x^{n+1/2}.
$$

Multiply by the time step:

$$
E_x^{n+1}(\epsilon+\sigma\Delta t/2)=E_x^n(\epsilon-\sigma\Delta t/2)+\Delta t(\nabla_h\times\mathbf H)_x^{n+1/2}.
$$

Finally divide by the coefficient of the new field:

$$
E_x^{n+1}=C_aE_x^n+C_b(\nabla_h\times\mathbf H)_x^{n+1/2}.
$$

$$
C_a=\frac{1-\sigma\Delta t/(2\epsilon)}{1+\sigma\Delta t/(2\epsilon)}=\frac{2\epsilon-\sigma\Delta t}{2\epsilon+\sigma\Delta t},\quad C_b=\frac{\Delta t/\epsilon}{1+\sigma\Delta t/(2\epsilon)}=\frac{2\Delta t}{2\epsilon+\sigma\Delta t}.
$$

For $\sigma=0$, $C_a=1$ and $C_b=\Delta t/\epsilon$: there is no Ohmic dissipation, and curl H drives the electric update.

## 3. Stability: the Courant condition

Can we enlarge the time step arbitrarily to finish sooner? Definitely not. For the standard explicit Yee scheme, information must propagate fast enough on the numerical grid. The CFL bound depends on the fastest wave speed and all spatial steps:

$$
\Delta t\le\frac{1}{v_{\max}\sqrt{\Delta x^{-2}+\Delta y^{-2}+\Delta z^{-2}}}.
$$

For equal cubic steps and fastest speed c,

$$
\Delta x=\Delta y=\Delta z=\Delta,\qquad\Delta t\le\frac{\Delta}{c\sqrt3}\approx0.577\frac\Delta c.
$$

Light moves only a little over half a cell per step at this three-dimensional stability limit. Exceed it and unstable numerical modes can grow instead of representing physics.

## 4. Boundaries and practical advantages

A finite computer cannot store open space. PML approximates outgoing radiation by absorbing waves near the outer boundary; lateral periodic boundaries reproduce an infinite cell array. A short Gaussian pulse plus Fourier transforms can provide broadband reflection, transmission and phase in one run.

The source emphasizes time-varying/nonlinear elements such as varactors and graphene, and efficient field-array storage and GPU parallelization. Compared with a large frequency-domain factorization, the explicit update can be attractive.

:::{admonition} Scientific clarification — separate from the source
:class: note
CFL is a stability condition, not an accuracy certificate. Interfaces and material dispersion can require extra treatment and tighter bounds. PML is not reflection-free at finite resolution. Broadband spectra require adequate source bandwidth, reference normalization and run duration; high-Q resonances decay slowly. Nonlinear responses do not generally define a single linear S-matrix. [Meep’s introduction](https://meep.readthedocs.io/en/stable/Introduction/) explains the Yee grid and Courant factor.
:::

:::{admonition} Worked problem
:class: tip
An x-polarized wave travels along +z from free space into a lossy dielectric: $\epsilon=4\epsilon_0$, $\mu=\mu_0$, $\sigma=0.02\,\mathrm{S/m}$. Use $\Delta z=1\,\mathrm{mm}$, $c=3\times10^8\,\mathrm{m/s}$ and $\Delta t=0.99\Delta z/c$.

1. Derive the one-dimensional updates for $E_x,H_y$.
2. Calculate the lossy electric-update coefficients.
3. From $E_x^n(k)=2.5$, $E_x^n(k+1)=3.1\,\mathrm{V/m}$ and $H_y^{n-1/2}(k+1/2)=4.0\times10^{-3}\,\mathrm{A/m}$, find the new H. Then, as a separate supplied state, use neighboring new H values $3.6\times10^{-3}$ and $2.8\times10^{-3}\,\mathrm{A/m}$ to update E from 2.5 V/m.
4. What happens if CFL is violated?
5. Why is the method useful for broadband metasurfaces?

```{dropdown} Show the complete worked answer

### a. Reduce Maxwell to one dimension

$$
\partial_zE_x=-\mu\partial_tH_y,\qquad\partial_zH_y=-\sigma E_x-\epsilon\partial_tE_x.
$$

$$
\partial_tH_y=-\mu^{-1}\partial_zE_x,\qquad\partial_tE_x=\epsilon^{-1}(-\partial_zH_y-\sigma E_x).
$$

Store E at integer positions/times and H at half positions/times. Centering Faraday gives

$$
\frac{H_y^{n+1/2}(k+\tfrac12)-H_y^{n-1/2}(k+\tfrac12)}{\Delta t}=-\frac{E_x^n(k+1)-E_x^n(k)}{\mu\Delta z}.
$$

$$
H_y^{n+1/2}(k+\tfrac12)=H_y^{n-1/2}(k+\tfrac12)-\frac{\Delta t}{\mu\Delta z}[E_x^n(k+1)-E_x^n(k)].
$$

Use the centered time derivative and half-sum conductivity term in Ampère:

$$
\epsilon\frac{E_x^{n+1}(k)-E_x^n(k)}{\Delta t}+\sigma\frac{E_x^{n+1}(k)+E_x^n(k)}2=-\frac{H_y^{n+1/2}(k+\tfrac12)-H_y^{n+1/2}(k-\tfrac12)}{\Delta z}.
$$

$$
E_x^{n+1}(k)(\epsilon/\Delta t+\sigma/2)=E_x^n(k)(\epsilon/\Delta t-\sigma/2)-\frac{H_y^{n+1/2}(k+\tfrac12)-H_y^{n+1/2}(k-\tfrac12)}{\Delta z}.
$$

$$
E_x^{n+1}(k)=C_aE_x^n(k)-C_b[H_y^{n+1/2}(k+\tfrac12)-H_y^{n+1/2}(k-\tfrac12)],\quad C_b=\frac{\Delta t/(\epsilon\Delta z)}{1+\sigma\Delta t/(2\epsilon)}.
$$

Here the one-dimensional coefficient includes the spatial-step factor, unlike the coefficient multiplying a discrete curl above.

### b. Coefficients

$$
\Delta z=10^{-3}\,\mathrm m,\quad\Delta t=0.99\frac{10^{-3}}{3\times10^8}=3.3\times10^{-12}\,\mathrm s.
$$

$$
\epsilon=4(8.854\times10^{-12})=3.5416\times10^{-11}\,\mathrm{F/m}.
$$

$$
\frac{\sigma\Delta t}{2\epsilon}=\frac{0.02(3.3\times10^{-12})}{2(3.5416\times10^{-11})}=\frac{6.6\times10^{-14}}{7.0832\times10^{-11}}\approx9.32\times10^{-4}.
$$

$$
C_a=\frac{1-9.32\times10^{-4}}{1+9.32\times10^{-4}}\approx\frac{0.999068}{1.000932}\approx0.99814\approx0.9981.
$$

$$
\frac{\Delta t}{\epsilon\Delta z}=\frac{3.3\times10^{-12}}{(3.5416\times10^{-11})(10^{-3})}=\frac{3.3\times10^{-12}}{3.5416\times10^{-14}}\approx93.18.
$$

$$
C_b\approx\frac{93.18}{1.000932}\approx93.09\approx93.1.
$$

### c. Two numerical updates

$$
\Delta E=3.1-2.5=0.6\,\mathrm{V/m},\qquad\mu_0=4\pi\times10^{-7}\,\mathrm{H/m}.
$$

$$
\frac{\Delta t}{\mu\Delta z}=\frac{3.3\times10^{-12}}{(4\pi\times10^{-7})(10^{-3})}\approx\frac{3.3\times10^{-12}}{1.2566\times10^{-9}}\approx2.626\times10^{-3}.
$$

$$
\Delta H=(2.626\times10^{-3})(0.6)=1.576\times10^{-3}\,\mathrm{A/m}.
$$

$$
H_y^{n+1/2}(k+\tfrac12)=4.0\times10^{-3}-1.576\times10^{-3}=2.424\times10^{-3}\,\mathrm{A/m}.
$$

Now use the separately given new-H pair for the electric update:

$$
\Delta H_y=3.6\times10^{-3}-2.8\times10^{-3}=0.8\times10^{-3}=8\times10^{-4}\,\mathrm{A/m}.
$$

$$
C_aE_x^n=0.9981(2.5)=2.49525,\qquad C_b\Delta H_y=93.1(8\times10^{-4})=0.07448.
$$

$$
E_x^{n+1}(k)=2.49525-0.07448\approx2.421\,\mathrm{V/m}.
$$

### d–e. Stability and broadband response

Beyond CFL, nonphysical amplitudes and oscillations grow and the explicit solve can diverge. A short pulse contains many frequencies; transform its response and a reference run to obtain broadband reflection/transmission amplitudes, phases and resonances. This can avoid a separate time-domain run for every frequency, subject to bandwidth and convergence limits.

```
:::
