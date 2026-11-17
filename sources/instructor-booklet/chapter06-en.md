# Chapter 6: paired textbook reading

## 6.1 Why numerical simulation?

In previous chapters we saw how electromagnetic theory describes waves at discontinuities and in effective media. Maxwell’s differential and integral equations give a beautiful, complete description of electric and magnetic fields. Mathematical beauty, however, does not make real engineering problems easy to solve.

Closed-form analytical solutions exist for only a few simple, highly symmetric canonical geometries: spheres through Mie theory, infinite cylinders, planar half-spaces, and simple rectangular or circular waveguides. Move away from these geometries and an exact analytical answer becomes extremely complicated, if it is available at all.

## 1. Why do metasurfaces need a numerical solution?

Metasurfaces deliberately use dense arrays of complicated subwavelength elements: split-ring resonators, symmetric or asymmetric patches, crosses, fractals and metal–dielectric multilayers. These are not simple canonical objects.

Three effects make the physics demanding: sharp edges concentrate fields and can produce singular behavior; reactive near fields couple neighboring cells strongly; and material/structural dispersion together with multilayer substrates makes the response depend on frequency and angle. A cell interacts with its neighbors as well as the incident wave.

Lumped RLC circuits and transmission-line approximations provide valuable physical insight, but are insufficient on their own for precise loss, bandwidth and fabrication predictions. Computational electromagnetics (CEM) and full-wave simulation fill that gap.

## 2. Full-wave simulation as virtual prototyping

The source calls methods full-wave when they solve Maxwell’s equations by discretizing space, time or boundaries rather than replacing the field problem by a simplified physical circuit. This virtual laboratory shortens design cycles: simulate and optimize before paying for cleanroom lithography or PCB fabrication.

Couple the solver to genetic, adjoint-gradient or machine-learning algorithms to synthesize the target amplitude and phase. Field visualizations also reveal surface currents, dielectric dissipation and hotspots that are difficult to measure directly in a laboratory.

## 3. Our roadmap

Section 6.2 compares differential/integral and frequency/time-domain methods, starting with FEM, FDTD, MoM and FIT and then adding RCWA. Section 6.3 develops unit cells, periodic boundaries and Floquet ports. Section 6.4 retrieves bulk and sheet parameters. Section 6.5 addresses meshes, convergence, ports and finite arrays.

:::{admonition} Scientific clarification — separate from the source
:class: note
“Full-wave” does not mean assumption-free or automatically accurate. Geometry, constitutive laws, source models, finite resolution and artificial boundaries still matter. The existing executed slab benchmark below deliberately shows excellent discrete power conservation alongside a wrong continuum prediction.
:::

## 6.2 Families of full-wave methods

We classify methods by the governing equations—differential or integral—and by frequency or time domain. The following five pages keep the source’s order and derivations. They explain how the equations become computable unknowns, not just which software button to press.

FEM uses a weak field formulation and edge degrees of freedom; FDTD staggers fields in space and time; MoM solves for currents using an integral operator; FIT separates mesh topology from constitutive approximations; RCWA expands periodic fields into coupled Fourier harmonics.

## 6.2.1 Finite elements: from strong form to edge unknowns

All right, let us meet the electromagnetic engineer’s versatile toolkit: the finite element method. FEM, used in packages such as HFSS and COMSOL, rests on variational analysis and solves boundary-value problems in complicated geometries. Let us look under the hood.

## 1. Derive the strong vector wave equation

Start from the curl equations, with an impressed current source:

$$
\nabla\times\mathbf E=-i\omega\mathbf B,\qquad\nabla\times\mathbf H=i\omega\mathbf D+\mathbf J_{\rm imp}.
$$

The material relations are

$$
\mathbf D=\epsilon_0\overline{\overline\epsilon}_r\mathbf E,\qquad\mathbf B=\mu_0\overline{\overline\mu}_r\mathbf H.
$$

To keep the algebra approachable, the source reduces these tensors to effective complex scalars. Eliminate the magnetic field using Faraday’s law:

$$
\mathbf H=-\frac{1}{i\omega\mu_0\mu_r}\nabla\times\mathbf E.
$$

Multiply by the inverse permeability, then take another curl:

$$
\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H.
$$

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0\nabla\times\mathbf H.
$$

Insert Ampère–Maxwell:

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0(i\omega\epsilon_0\epsilon_r\mathbf E+\mathbf J_{\rm imp}).
$$

With the free-space wavenumber, the result is

$$
k_0^2=\omega^2\mu_0\epsilon_0,\qquad\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

That is the strong form. Directly demanding classical second derivatives everywhere is awkward near material discontinuities and sharp edges. The weak form lowers the differentiability required of the approximation.

## 2. Weighted residuals and integration by parts

$$
\mathbf R=\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E+i\omega\mu_0\mathbf J_{\rm imp}.
$$

Instead of forcing zero residual at every point, multiply by a test field and integrate over the volume. The source initially writes an unconjugated test field:

$$
\int_V\mathbf W\cdot[\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E],dV=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.
$$

The vector identity and divergence theorem move one curl to the test function:

$$
\int_V\mathbf W\cdot\nabla\times\mathbf A,dV=\int_V(\nabla\times\mathbf W)\cdot\mathbf A,dV-\int_{\partial V}(\mathbf W\times\mathbf A)\cdot\hat{\mathbf n},dS.
$$

The printed source then gives the following boundary-sign form. The separate correction immediately below matters for implementation.

$$
\int_V[\mu_r^{-1}(\nabla\times\mathbf W)\cdot(\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf W\cdot\mathbf E],dV+i\omega\mu_0\int_{\partial V}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
For an outward normal, the integration identity and $\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H$ give a **minus** sign on the boundary term on the left:

$$
a(\mathbf E,\mathbf W)-i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.
$$

Here $a$ is the volume curl–curl minus mass form and complex Galerkin testing uses $\mathbf W^*$. For an outgoing exterior wave, $\hat{\mathbf n}\times\mathbf H=-Y\mathbf E_t$; the resulting matrix boundary contribution is therefore positive $i\omega\mu_0 B_Y$. The source’s later symbolic admittance definition uses the opposite sign. Normal orientation, boundary admittance and weak form must be converted together. [MFEM’s weak-curl derivation](https://mfem.org/fem_weak_form/) provides the integration identity.

For implementation with the outward normal, make the corrected boundary definition and right-hand side explicit:

$$
\hat{\mathbf n}\times\mathbf H=-Y\mathbf E_t+\mathbf g_{\rm inc},\qquad[K-k_0^2M+i\omega\mu_0B_Y]\mathbf e=\mathbf f.
$$

$$
f_i=-i\omega\mu_0\int_V\mathbf N_i^*\cdot\mathbf J_{\rm imp}\,dV+i\omega\mu_0\int_{S_{\rm rad}}\mathbf N_{i,t}^*\cdot\mathbf g_{\rm inc}\,dS.
$$
Here $B_Y$ contains positive load/outgoing admittances on their respective surfaces. This corrects the signs together, rather than changing one boundary term in isolation.
:::

The attraction is clear: only first curls remain, tangential continuity fits naturally, and boundary physics enters through surface integrals.

## 3. Boundary conditions

At PEC, tangential electric trial and test traces vanish. An impedance boundary represents a thin conductive layer such as graphene without meshing its atomic thickness. The source writes the surface relation using $Z_s$:

$$
\int_{S_{\rm IBC}}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=\frac1{Z_s}\int_{S_{\rm IBC}}(\hat{\mathbf n}\times\mathbf W)\cdot(\hat{\mathbf n}\times\mathbf E),dS.\quad\text{[source boundary definition]}
$$

A radiation boundary approximates infinity with a Robin-type outgoing condition. It is an approximation to be tested, not an exact transparent boundary at every angle.

## 4. Edge elements rather than ordinary nodal fields

Ordinary nodal vector interpolation can enforce inappropriate continuity across material interfaces and permit spurious modes. Nédélec edge elements instead preserve tangential continuity while allowing the normal field behavior required by the material interface.

## 5. Assemble the sparse system

$$
([K]-k_0^2[M]+ik_0[B])\{e\}=\{f\}.
$$

Stiffness, mass and boundary matrices can be large but sparse because local basis functions overlap only nearby elements. The normalization of the boundary matrix determines its displayed prefactor. The source illustrates cavity eigenfrequencies and graphene impedance boundaries, and uses “a thousand times faster” as an enthusiastic example of avoiding a very fine thin-layer mesh.

:::{admonition} Scientific clarification — separate from the source
:class: note
Edge elements help control spurious modes but do not eliminate every nullspace or modeling error automatically. Thin-sheet replacement needs a valid constitutive model; speedup depends on mesh, solver and accuracy. No commercial FEM run is claimed here.
:::

:::{admonition} Worked problem
:class: tip
A cell is periodic in $x,y$ and contains an inhomogeneous dielectric, a thin conducting layer modeled on $S_{\rm IBC}$ by $Z_s$, and a first-order radiation boundary above. Assume scalar $\epsilon_r,\mu_r$ and known $\mathbf J_{\rm imp}$.

1. Derive the electric weak form with impedance and radiation terms.
2. Expand the field in Nédélec edge functions and give volume/boundary matrix entries.
3. Explain why edge elements are suitable.

```{dropdown} Show the complete worked answer

The source starts with the governing equation, tests with the conjugate field, and writes

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

$$
\int_V\mu_r^{-1}(\nabla\times\mathbf W^*)\cdot(\nabla\times\mathbf E),dV-k_0^2\int_V\epsilon_r\mathbf W^*\cdot\mathbf E,dV+i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

Keep the source’s symbolic boundary definitions for this transcription; apply the correction above when implementing an outward-normal model:

$$
\hat{\mathbf n}\times\mathbf H=Y_s\mathbf E_t,\quad Y_s=Z_s^{-1},\qquad\hat{\mathbf n}\times\mathbf H\approx Y_{\rm rad}\mathbf E_t+\mathbf g_{\rm inc}.
$$

The unknown-field part enters the boundary matrix; the known incident term enters the right-hand side. An internal sheet requires fields on both sides and a magnetic-field jump, rather than a one-sided boundary imposed without change.

$$
\mathbf E_h(\mathbf r)=\sum_{j=1}^{N_e}e_j\mathbf N_j(\mathbf r),\qquad\mathbf W=\mathbf N_i.
$$

$$
[K-k_0^2M+i\omega\mu_0(B_{\rm IBC}+B_{\rm rad})]\mathbf e=\mathbf f.\quad\text{[source symbolic definitions]}
$$

$$
K_{ij}=\int_V\mu_r^{-1}(\nabla\times\mathbf N_i^*)\cdot(\nabla\times\mathbf N_j),dV,\qquad M_{ij}=\int_V\epsilon_r\mathbf N_i^*\cdot\mathbf N_j,dV.
$$

$$
(B_{\rm IBC})_{ij}=\int_{S_{\rm IBC}}Y_s\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS,\qquad(B_{\rm rad})_{ij}=\int_{S_{\rm rad}}Y_{\rm rad}\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS.
$$

$$
f_i=-i\omega\mu_0\left[\int_V\mathbf N_i^*\cdot\mathbf J_{\rm imp},dV+\int_{S_{\rm rad}}\mathbf N_{i,t}^*\cdot\mathbf g_{\rm inc},dS\right].\quad\text{[source symbolic definitions]}
$$

Link paired edge degrees of freedom by the Floquet phase, including edge orientations. Periodicity is not merely another independent boundary matrix. Tangential electric continuity is physical at an ordinary material interface, while the normal electric component need not be continuous. Edge functions accommodate precisely that distinction and help control spurious wave modes.

The challenge is combining integration-by-parts signs, the correct thin-layer model and Floquet constraints consistently.

```
:::

## 6.2.2 FDTD: the Yee lattice and leapfrog updates

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

## 6.2.3 Method of moments: solve for the currents

If FEM and FDTD mesh the whole volume, MoM asks a practical question: why mesh empty space when a suitable integral formulation can solve only the object? It is especially useful for radiation, scattering, frequency-selective surfaces and thin metal arrays. The source names FEKO and integral solvers in CST as examples.

## 1. From fields to a surface integral equation

The incident wave induces surface currents. Those currents behave like microscopic antennas and radiate the scattered field. The total field is their sum. At a PEC surface its tangential component vanishes:

$$
\mathbf E_{\rm total}=\mathbf E_{\rm inc}+\mathbf E_{\rm scat},\qquad[\mathbf E_{\rm scat}(\mathbf J_s)]_t=-\mathbf E_{{\rm inc},t}.
$$

Choose the integral-operator sign so that the excitation is on the right:

$$
\mathcal L(\mathbf J_s)=\mathbf E_{{\rm inc},t}.
$$

The unknown is surface-current density, the operator is linear integral–differential, and the input is the tangential incident field. A suitable outgoing Green function already contains radiation to infinity: a free-space surface-integral model needs no exterior PML or arbitrary air-box truncation.

## 2. Triangles and RWG basis functions

Mesh the surface into triangles. Each Rao–Wilton–Glisson function lives on two triangles sharing an oriented edge. Current crosses that common edge continuously in the appropriate normal-to-edge component; the surface divergence is piecewise defined.

$$
\mathbf f_n(\mathbf r)=\begin{cases}\dfrac{\ell_n}{2A_n^+}(\mathbf r-\mathbf r_n^+),&\mathbf r\in T_n^+,\\\dfrac{\ell_n}{2A_n^-}(\mathbf r_n^--\mathbf r),&\mathbf r\in T_n^-,\\0,&\text{elsewhere}.\end{cases}
$$

The edge length and triangle areas enter explicitly. Expand the total current using unknown coefficients:

$$
\mathbf J_s(\mathbf r)\approx\sum_{n=1}^NI_n\mathbf f_n(\mathbf r).
$$

## 3. Galerkin testing and the impedance matrix

$$
\left\langle\mathbf f_m,\mathcal L\!\left(\sum_{n=1}^NI_n\mathbf f_n\right)\right\rangle=\langle\mathbf f_m,\mathbf E_{{\rm inc},t}\rangle,\qquad m=1,\ldots,N.
$$

$$
[Z]_{N\times N}[I]_{N\times1}=[V]_{N\times1}.
$$

Each impedance entry measures coupling from one basis current to one test function. The coefficient vector describes current amplitudes/phases, and the excitation vector is the tested incident field. The usual matrix is dense because distant currents still interact.

| Quantity | Physical meaning | Typical numerical cost/shape |
|---|---|---|
| $Z$ | Mutual field coupling | Dense complex matrix; $\mathcal O(N^2)$ storage |
| $I$ | Current coefficients | $N\times1$ vector |
| $V$ | Tested incident field | $N\times1$ vector |
| Solve $ZI=V$ | Coupled response | Dense direct factorization typically $\mathcal O(N^3)$ |

## 4. The bottleneck and MLFMM

With hundreds of thousands of unknowns, a dense matrix can exhaust memory. Multilevel fast multipole methods compute nearby interactions directly and approximate distant interactions through hierarchical clusters and multipole representations. In iterative solvers such as GMRES, typical storage and matrix–vector products can approach O(N log N).

## 5. Periodic MoM

For an infinite cell array, replace the free-space Green function by its Floquet-periodic sum:

$$
G_{\rm per}(\mathbf r,\mathbf r^{\prime})=\sum_{p,q\in\mathbb Z}G(\mathbf r,\mathbf r^{\prime}+pD_x\hat{\mathbf x}+qD_y\hat{\mathbf y})e^{-i(k_{x0}pD_x+k_{y0}qD_y)}.
$$

Only one cell is meshed, but its interaction with the repeated array enters the operator. Periodic Green sums still need accurate evaluation and convergence treatment.

:::{admonition} Worked problem
:class: tip
For a PEC patch expanded in three RWG functions, use

$$Z=\begin{bmatrix}50+20i&10-5i&5+2i\\10-5i&45+18i&8-4i\\5+2i&8-4i&40+15i\end{bmatrix}\,\Omega,\quad V=\begin{bmatrix}1\\0.8e^{-i30^\circ}\\0.4e^{i45^\circ}\end{bmatrix}\,\mathrm V.$$

1. Explain where Z, I and V come from.
2. Solve for complex current coefficients and give their magnitudes/phases.
3. Why are off-diagonal entries nonzero?
4. Estimate dense complex128 matrix storage for N=50,000 (16 bytes/entry).
5. What does MLFMM reduce, and is total solve time always O(N log N)?

```{dropdown} Show the complete worked answer

$$
\mathbf J_s\approx\sum_nI_n\mathbf f_n,\quad\sum_nZ_{mn}I_n=V_m,\quad Z_{mn}=\langle\mathbf f_m,\mathcal L\{\mathbf f_n\}\rangle,\quad V_m=\langle\mathbf f_m,\mathbf E_{{\rm inc},t}\rangle.
$$

The operator sign is defined to put incident excitation on the right. Convert the excitation to Cartesian form:

$$
0.8e^{-i30^\circ}=0.6928-0.4000i,\qquad0.4e^{i45^\circ}=0.2828+0.2828i.
$$

$$
\begin{bmatrix}50+20i&10-5i&5+2i\\10-5i&45+18i&8-4i\\5+2i&8-4i&40+15i\end{bmatrix}\begin{bmatrix}I_1\\I_2\\I_3\end{bmatrix}=\begin{bmatrix}1\\0.6928-0.4000i\\0.2828+0.2828i\end{bmatrix}.
$$

The source reports the following approximate solution; the independently recomputed answer is provided after this panel.

$$
I_1\approx0.01735-0.00854i,\quad I_2\approx0.00856-0.00819i,\quad I_3\approx0.00555+0.00513i\quad\mathrm A.\quad\text{[printed]}
$$

| Coefficient | Printed magnitude | Printed phase |
|---|---|---|
| $I_1$ | 19.33 mA | $-26.2^\circ$ |
| $I_2$ | 11.85 mA | $-43.7^\circ$ |
| $I_3$ | 7.56 mA | $42.8^\circ$ |

Currents differ because each basis feels both direct excitation and every other basis current. For example, $Z_{12}=10-5i\,\Omega$ represents coupling from basis 2 to test 1. Geometry, frequency, background and integral formulation determine those entries; reciprocity can give complex symmetry under appropriate testing, not Hermitian symmetry in general.

$$
M=16N^2\,\mathrm{byte},\quad M(50000)=16(50000)^2=40\times10^9\,\mathrm{byte}\approx40\,\mathrm{GB}\approx37.3\,\mathrm{GiB}.
$$

This is just the matrix: vectors, factorization, preconditioners and solver workspaces need more. Quadrupling N to 200,000 multiplies storage by sixteen:

$$
M(200000)=640\,\mathrm{GB}\approx596\,\mathrm{GiB}.
$$

MLFMM accelerates repeated ZI products by separating near and far interactions. Total time also includes iteration count, setup and preconditioning:

$$
T_{\rm total}\approx n_{\rm iter}T_{\rm matvec}+T_{\rm setup}+T_{\rm preconditioner}.
$$

A poorly conditioned problem can require many iterations. Do not replace a per-product scaling statement by an unconditional total-time guarantee.

### Independent corrected calculation

Solving the supplied matrix directly gives

$$
I_1=0.01704858-0.00527665i,\quad I_2=0.00672893-0.00912228i,\quad I_3=0.00680192+0.00682485i\quad\mathrm A.
$$

$$
|I|=[17.84649,11.33554,9.63559]\,\mathrm{mA},\quad\arg I=[-17.19763,-53.58613,45.09640]^\circ.
$$

The relative residual of the printed current vector is about 0.168, whereas the recomputed vector gives about $3.4\times10^{-16}$. This discrepancy is too large to be rounding. The independent [worked-arithmetic report](../data/chapter-06/textbook-checks.json) and reproducible checker preserve both cases.

```
:::

## 6.2.4 FIT: topology first, materials second

FIT, introduced by Thomas Weiland, starts from Maxwell’s integral laws. The source describes it as an important basis of CST’s transient solver. Instead of differentiating point samples first, integrate along oriented edges and through oriented faces on a primal mesh and an interleaved dual mesh.

```{figure} ../assets/chapter-06/integral-unknowns.svg
:alt: Left: the four oriented edge voltages in the FIT worked problem. Right: the support of one RWG function used in MoM.

Left: the four oriented edge voltages in the FIT worked problem. Right: the support of one RWG function used in MoM.
```

$$
\oint_{\partial A}\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_A\mathbf B\cdot d\mathbf A,\qquad\oint_{\partial\widetilde A}\mathbf H\cdot d\mathbf l=\frac{d}{dt}\int_{\widetilde A}\mathbf D\cdot d\mathbf A+\int_{\widetilde A}\mathbf J\cdot d\mathbf A.
$$

$$
\int_{\partial V}\mathbf D\cdot d\mathbf A=Q_e,\qquad\int_{\partial V}\mathbf B\cdot d\mathbf A=0.
$$

## 1. Integral unknowns

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\quad\widehat b_j=\int_{A_j}\mathbf B\cdot d\mathbf A,\quad\widehat h_i=\int_{\widetilde L_i}\mathbf H\cdot d\mathbf l,\quad\widehat d_j=\int_{\widetilde A_j}\mathbf D\cdot d\mathbf A.
$$

These are electric edge voltages, primal-face magnetic fluxes, dual-edge magnetic line integrals and dual-face electric fluxes. Their units and orientations differ from pointwise field samples.

## 2. Incidence matrices and Maxwell grid equations

C maps primal edges to oriented face circulations, the dual curl does the same on the dual grid, and S sums oriented face fluxes over a closed cell. Entries are only 0 and ±1: geometry incidence rather than material properties.

$$
C\widehat{\mathbf e}=-\frac d{dt}\widehat{\mathbf b},\quad\widetilde C\widehat{\mathbf h}=\frac d{dt}\widehat{\mathbf d}+\widehat{\mathbf j},\quad S\widehat{\mathbf b}=0,\quad\widetilde S\widehat{\mathbf d}=\mathbf q.
$$

$$
SC=0,\qquad\widetilde S\widetilde C=0,\qquad\widetilde S\widehat{\mathbf j}=-\frac d{dt}\mathbf q.
$$

“The boundary of a boundary is empty”: shared edge contributions cancel on the surface of a closed cell. Apply the dual divergence to Ampère’s equation and charge continuity follows. These topological identities are exact on the chosen mesh.

## 3. Close the system with material matrices

$$
\widehat{\mathbf d}=M_\epsilon\widehat{\mathbf e},\qquad\widehat{\mathbf h}=M_{\mu^{-1}}\widehat{\mathbf b},\qquad\widehat{\mathbf j}=M_\sigma\widehat{\mathbf e}.
$$

These matrices contain material parameters and area/length factors. They may be diagonal on suitable orthogonal grids with simple isotropic constitutive laws; this is not a universal property.

| Law | Continuous form | FIT form |
|---|---|---|
| Faraday | $\nabla\times E=-\partial_tB$ | $C\widehat e=-\partial_t\widehat b$ |
| Ampère | $\nabla\times H=\partial_tD+J$ | $\widetilde C\widehat h=\partial_t\widehat d+\widehat j$ |
| Electric Gauss | $\nabla\cdot D=\rho$ | $\widetilde S\widehat d=q$ |
| Magnetic Gauss | $\nabla\cdot B=0$ | $S\widehat b=0$ |
| Continuity | $\nabla\cdot J=-\partial_t\rho$ | $\widetilde S\widehat j=-\partial_tq$ |

## 4. FIT, FDTD and curved boundaries

On a regular Cartesian grid, conventional constitutive discretization plus explicit staggered time integration can produce the same Yee updates. The viewpoints differ: differential samples versus integral unknowns and incidence. FIT itself can also be formulated in the frequency domain.

A conventional rectangular mesh staircases curved metal/dielectric boundaries. The source describes conformal boundary treatments and CST’s PBA as ways to account for cut areas and improve geometry without refining the entire box. It highlights broadband pulse analysis, active/time-varying elements, and periodic polarization/phase characterization.

:::{admonition} Scientific clarification — separate from the source
:class: note
The source initially says all FIT error enters constitutive relations, then correctly qualifies that statement in its worked example. Incidence identities are exact; final accuracy also depends on geometry, material approximations, time stepping, boundaries and finite resolution. A “perfect” boundary-approximation name does not imply zero numerical error.
:::

:::{admonition} Worked problem
:class: tip
A square primal face of side $\Delta=1\,\mathrm{mm}$ lies in xy with normal +z and counterclockwise circulation. Edge reference directions 1,2 agree with traversal and 3,4 oppose it. At time n, voltages are $[0.30,0.20,0.10,0.05]\,\mathrm V$; initial flux is $2.00\times10^{-10}\,\mathrm{Wb}$ and $\Delta t=1.0\,\mathrm{ps}$.

1. Calculate circulation and the corresponding C row.
2. Update magnetic flux.
3. In vacuum, with primal area $\Delta^2$ and dual length $\Delta$, find the dual magnetic line integral.
4. Explain magnetic Gauss preservation from SC=0.
5. Relate regular-grid explicit FIT to Yee FDTD; is FIT only time domain?

```{dropdown} Show the complete worked answer

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\qquad(C\widehat{\mathbf e}^{,n})_f=\widehat e_1^n+\widehat e_2^n-\widehat e_3^n-\widehat e_4^n.
$$

$$
(C\widehat{\mathbf e}^{,n})_f=0.30+0.20-0.10-0.05=0.35\,\mathrm V,\qquad C_{f,\{1,2,3,4\}}=[1,1,-1,-1].
$$

These signs come from orientation, not permittivity or permeability. Faraday on staggered times gives

$$
C\widehat{\mathbf e}=-\frac{d\widehat{\mathbf b}}{dt},\qquad\frac{\widehat b^{n+1/2}-\widehat b^{n-1/2}}{\Delta t}=-(C\widehat{\mathbf e}^{,n})_f.
$$

$$
\widehat b^{n+1/2}=\widehat b^{n-1/2}-\Delta t(C\widehat{\mathbf e}^{,n})_f=2.00\times10^{-10}-(1.0\times10^{-12})(0.35)=1.9965\times10^{-10}\,\mathrm{Wb}.
$$

The unit check is volts times seconds equals webers. To obtain a magnetic line integral, topology alone is insufficient: use the material relation.

$$
\widehat h=M_{\mu^{-1}}\widehat b\approx\frac{\widetilde\ell}{\mu_0A}\widehat b,\quad A=\Delta^2,\quad\widetilde\ell=\Delta.
$$

$$
\widehat h^{n+1/2}\approx\frac{\widehat b^{n+1/2}}{\mu_0\Delta}=\frac{1.9965\times10^{-10}}{(4\pi\times10^{-7})(10^{-3})}\approx0.159\,\mathrm A.
$$

$$
\widehat h=\int_{\widetilde L}\mathbf H\cdot d\mathbf l,\qquad H\approx\widehat h/\widetilde\ell\approx159\,\mathrm{A/m}.
$$

The line integral has amperes as its unit, not amperes per meter. The final conversion assumes approximately uniform H; material interfaces and complicated grids require a better constitutive approximation.

$$
SC=0,\qquad SC\widehat{\mathbf e}=-S\frac{d\widehat{\mathbf b}}{dt}\quad\Longrightarrow\quad\frac d{dt}(S\widehat{\mathbf b})=0.
$$

Hence an initially zero discrete magnetic divergence stays zero under a compatible update. This preserves consistent initial data; it does not repair inconsistent initial fluxes. On a regular Cartesian mesh with standard material matrices and leapfrog time stepping, FIT can give the Yee updates. Its integral/topological formulation also admits frequency-domain solutions.

```
:::

## 6.2.5 RCWA: periodic fields in Fourier space

General volume/surface methods offer geometric flexibility but can require large meshes and long runs. Many metasurfaces have two useful features: periodicity in xy and layers along z. RCWA, associated with Moharam and Gaylord’s 1981 work and also called the Fourier modal method, exploits that structure.

Instead of sampling every point with a spatial mesh, expand materials and fields in Fourier series. The retained harmonics satisfy coupled propagation equations. “Rigorous” means a Maxwell solution for the stated model, with truncation and geometry approximations still requiring convergence.

## 1. Slice the structure

Each layer is invariant along z and may vary periodically in x,y. Sloped or curved profiles are approximated by multiple thin slices. Slice thickness and harmonic count are separate controls.

## 2. Expand material and apply the correct factorization

$$
\epsilon_r(x,y)=\sum_{p=-P}^P\sum_{q=-Q}^Q\widetilde\epsilon_{pq}e^{i(pG_xx+qG_yy)},\qquad G_x=2\pi/\Lambda_x,\quad G_y=2\pi/\Lambda_y.
$$

The source’s material series uses a positive Fourier sign while its field basis below uses a negative sign. The material convolution must therefore use the corresponding reversed coefficient indices; one can equivalently reindex the material series.

Li’s factorization rules address products of discontinuous functions. In TM and high-contrast structures, simply multiplying truncated coefficient arrays can converge poorly. The inverse rule involves $[\epsilon^{-1}]^{-1}$ in the appropriate component relation; this is not generally the same finite matrix as $[\epsilon]$.

## 3. Expand the Bloch field

$$
\mathbf E(x,y,z)=\sum_{m=-M}^M\sum_{n=-N}^N\mathbf S_{mn}(z)e^{-i(k_{xm}x+k_{yn}y)},\quad k_{xm}=k_{x0}+2\pi m/\Lambda_x,\quad k_{yn}=k_{y0}+2\pi n/\Lambda_y.
$$

Each index pair identifies a diffraction order. Tangential derivatives become diagonal wavenumber matrices. Eliminating longitudinal components gives a coupled ordinary differential/eigenvalue problem:

$$
\partial_x\longrightarrow-iK_x,\quad\partial_y\longrightarrow-iK_y,\qquad\frac{d^2\mathbf S_t}{dz^2}=\Omega^2\mathbf S_t.
$$

With solutions proportional to exp(λz), imaginary λ describes lossless propagation and real λ an evanescent pair. In lossy media λ is generally complex; choose outgoing/decaying solutions consistently.

## 4. Couple layers stably

Transfer matrices can combine growing and decaying evanescent exponentials and become badly conditioned. Scattering matrices connect incoming to outgoing waves, and can be composed with the Redheffer star product.

$$
\begin{bmatrix}\mathbf c_{\rm out}^{+}\\\mathbf c_{\rm out}^{-}\end{bmatrix}=S\begin{bmatrix}\mathbf c_{\rm in}^{+}\\\mathbf c_{\rm in}^{-}\end{bmatrix},\qquad e^{+|\lambda|d}\ \text{versus}\ e^{-|\lambda|d}.
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
The source calls S-matrix coupling “100% stable and noise-free for infinitely many layers.” It greatly improves numerical conditioning, but finite precision, resonances, singular blocks, truncation and factorization still matter. It is not an unconditional stability guarantee.
:::

| Feature | RCWA | FEM | FDTD |
|---|---|---|---|
| Discretization | Fourier harmonics; layer slices if needed | Volume elements/edge fields | Staggered space/time grid |
| Periodicity | Built into Bloch basis | Paired boundary constraints | Periodic/Bloch grid boundaries |
| Curved/sloped geometry | May require many slices | Flexible fitted mesh | Staircasing or conformal treatment |
| Typical use | Periodic diffraction and libraries | Complex vector devices | Pulses and time evolution |
| Cost | Dense modal matrices grow with harmonic count | Mesh and linear solver dependent | Volume, time steps and duration dependent |

The source emphasizes rapid library generation, direct order-power outputs, and dielectric metasurface optimization, with an illustrative “two minutes versus 0.2 seconds” comparison. Timings are examples, not reproducible performance guarantees across geometries and tolerances. A converged calculation, not the solver’s name, determines usable accuracy.

:::{admonition} Worked problem
:class: tip
A one-dimensional air/air grating has $\Lambda=800\,\mathrm{nm}$ and illumination $\lambda_0=600\,\mathrm{nm}$, $\theta_i=30^\circ$. For $m=-2,-1,0,1,2$, calculate $k_{x,m}/k_0$, classify orders and give real outgoing angles. Why retain evanescent harmonics?

1. Calculate the normalized tangential wavenumbers.
2. Classify each order and calculate the real exit angles.
3. Explain why evanescent harmonics must be retained until convergence.

```{dropdown} Show the complete worked answer

$$
k_{x,m}=k_0\sin\theta_i+2\pi m/\Lambda,\qquad k_0=2\pi/\lambda_0.
$$

$$
\frac{k_{x,m}}{k_0}=\sin\theta_i+m\frac{\lambda_0}{\Lambda}=0.5+0.75m,\quad\sin30^\circ=0.5,\quad\frac{600}{800}=0.75.
$$

| m | Substitution | Normalized tangential wavenumber | Type | Angle |
|---|---|---|---|---|
| −2 | $0.5-1.5$ | −1 | Grazing threshold | $-90^\circ$ limit |
| −1 | $0.5-0.75$ | −0.25 | Propagating | $\arcsin(-0.25)\approx-14.48^\circ$ |
| 0 | $0.5$ | 0.50 | Propagating | $30^\circ$ |
| +1 | $0.5+0.75$ | 1.25 | Evanescent | No real angle |
| +2 | $0.5+1.5$ | 2.00 | Evanescent | No real angle |

$$
k_{z,m}^2=k_0^2-k_{x,m}^2,\qquad |k_{x,m}|<k_0:\ \text{propagating};\quad |k_{x,m}|>k_0:\ \text{evanescent};\quad |k_{x,m}|=k_0:\ k_{z,m}=0.
$$

Only −1 and 0 are ordinary power-carrying far-field orders in this list. At −2 the normal flux of an ideal finite-amplitude grazing wave is zero. Evanescent fields can still resolve edges and interfaces and couple into propagating harmonics. Increase retained harmonics until the actual order powers and phases converge, especially near the grazing threshold.

```
:::

## 6.3 Periodic cells, Floquet ports and phase planes

A practical metasurface may contain thousands or millions of elements. Translational symmetry reduces an exactly repeated array to one cell. For a graded device, local periodicity is an additional approximation: replace each cell’s real neighbors by identical copies to build its response library.

Gentle geometric variation can make this useful, but strong unequal-cell coupling and sensitive resonances can invalidate it. Exact solution of periodic boundary conditions does not establish LPA validity for a nonuniform array.

## 1. Pair opposite faces with the Bloch phase

$$
\mathbf E(x+\Lambda_x,y,z)=\mathbf E(x,y,z)e^{-ik_{x0}\Lambda_x},\qquad\mathbf E(x,y+\Lambda_y,z)=\mathbf E(x,y,z)e^{-ik_{y0}\Lambda_y}.
$$

$$
k_{x0}=k_0\sin\theta\cos\varphi,\quad k_{y0}=k_0\sin\theta\sin\varphi.
$$

Normal incidence gives zero phase shift; oblique incidence does not. In software, pair the correct source/destination faces and map mesh or degrees of freedom with their orientations. The source mentions primary/secondary (formerly master/slave) in HFSS and Unit Cell boundaries in CST. Interface names are software-version dependent.

## 2. Floquet ports and channel accounting

A Floquet port excites/collects plane-wave harmonics rather than a metallic waveguide mode. Each spatial order supports polarization states; select the incident mode and retain every propagating outgoing channel, including converted polarization. Higher diffraction orders may open with frequency or angle.

$$
k_{xm}=k_{x0}+2\pi m/\Lambda_x,\quad k_{yn}=k_{y0}+2\pi n/\Lambda_y,\quad k_{z,mn}=\sqrt{k_0^2-k_{xm}^2-k_{yn}^2}.
$$

In air, a conservative no-higher-order condition over incidence angles up to the specified maximum is

$$
\Lambda_{x,y}<\frac{\lambda_0}{1+\sin\theta_{\max}}.
$$

This is a channel-opening condition, not a statement of reflectance or LPA accuracy. Recalculate it for other exterior refractive indices.

## 3. Deembed to the physical surface

The phase reported at a port contains travel through its air gap. Remove that known propagation to compare cells at the same physical plane. At oblique incidence the vertical separation uses the normal wavenumber, not the full free-space wavenumber.

$$
\phi_{\rm port}=\phi_{\rm surface}-2k_{z,00}d_{\rm port}\pmod{2\pi}.
$$

The source recommends separating the port from strong near fields and discusses quarter-/half-wavelength distances. Later it correctly explains that no fixed wavelength fraction is sufficient for every structure: near-cutoff evanescent fields can decay very slowly. Shift the port and increase retained modes independently until the desired complex response is stable.

| Setting | HFSS terminology in source | CST terminology in source | Physical check |
|---|---|---|---|
| Lateral pairing | Primary/secondary | Unit Cell | Paired Bloch phase |
| Excitation | Floquet port | Floquet expansion | Incoming wave and polarization |
| Angles | Scan angles | Scan/phase settings | Same tangential wavevector |
| Reference plane | Deembedding | Reference-plane distance | Complex coefficient at same surface |
| Mode count | Port-mode selection | Floquet-mode selection | All open channels plus refinement |

:::{admonition} Worked problem
:class: tip
A square cell has $\Lambda_x=\Lambda_y=10\,\mathrm{mm}$ at $f=10\,\mathrm{GHz}$. Air-side illumination is at $\theta=30^\circ,\varphi=0$, with +z upward. The port lies 10 mm above the surface and reports reflection phase −110°.

1. Explain LPA and a failure scenario.
2. Find wavelength, tangential wavenumbers and paired-face phases.
3. Classify (0,0), (−1,0), (+1,0), (0,+1), and determine whether any other air-side order is open.
4. Check the conservative period bound up to 30° and explain what it guarantees.
5. Choose port modes and discuss port distance.
6. Calculate the surface reflection phase using the given deembedding relation.
7. Give a logical setup sequence.

```{dropdown} Show the complete worked answer

LPA replaces the slowly varying neighborhood by an infinite identical array; abrupt changes, resonance and unequal-cell coupling can defeat it. Now calculate the wave quantities:

$$
\lambda_0=\frac{3\times10^8}{10\times10^9}=0.03\,\mathrm m=30\,\mathrm{mm},\qquad k_0=\frac{2\pi}{30}=\frac\pi{15}\,\mathrm{rad/mm}.
$$

$$
k_{x0}=\frac\pi{15}\sin30^\circ\cos0=\frac\pi{30}\,\mathrm{rad/mm},\qquad k_{y0}=0.
$$

$$
k_{x0}\Lambda_x=\frac\pi{30}(10)=\frac\pi3=60^\circ,\qquad E(x+\Lambda_x,y,z)=E(x,y,z)e^{-i60^\circ},\quad E(x,y+\Lambda_y,z)=E(x,y,z).
$$

The x-paired field lags by 60°; the y pair has no phase difference. Respect the mapping direction and edge orientation.

$$
\frac{k_{xm}}{k_0}=0.5+3m,\qquad\frac{k_{yn}}{k_0}=3n,\qquad(k_{xm}/k_0)^2+(k_{yn}/k_0)^2<1\quad\text{for an open air channel}.
$$

| Order | $k_x/k_0$ | $k_y/k_0$ | Squared sum | Result |
|---|---|---|---|---|
| (0,0) | 0.5 | 0 | 0.25 | Propagating |
| (−1,0) | −2.5 | 0 | 6.25 | Evanescent |
| (+1,0) | 3.5 | 0 | 12.25 | Evanescent |
| (0,+1) | 0.5 | 3 | 9.25 | Evanescent |

$$
k_{z,00}=k_0\sqrt{1-0.25}=k_0\cos30^\circ=\frac{\sqrt3}{2}k_0.
$$

No order is missed: for $n\ne0$, $|3n|\ge3>1$; for $n=0,m\ne0$, the minimum $|0.5+3m|$ is 2.5. Thus only (0,0) propagates on this air side. This says nothing yet about its power.

$$
\frac{\lambda_0}{1+\sin\theta_{\max}}=\frac{30}{1+0.5}=20\,\mathrm{mm},\qquad10\,\mathrm{mm}<20\,\mathrm{mm}.
$$

Higher air-side orders remain closed up to 30°. This does not guarantee unit reflection: absorption, transmission and converted polarization still need accounting, and the opposite medium needs its own channel check. Retain both TE and TM states of the fundamental if conversion is possible, and all propagating modes on any second port. Add evanescent modes as near-field and port-distance convergence require.

$$
\phi_{\rm surface}=\phi_{\rm port}+2k_{z,00}d_{\rm port}\pmod{360^\circ}.
$$

$$
2k_{z,00}d_{\rm port}=2\left(\frac{2\pi}{30}\cos30^\circ\right)(10)=\frac{2\pi\sqrt3}{3}\,\mathrm{rad}.
$$

$$
\Delta\phi=360^\circ\frac{2(10)(0.8660)}{30}\approx207.85^\circ,\qquad\phi_{\rm surface}=-110^\circ+207.85^\circ=97.85^\circ\pmod{360^\circ}.
$$

The result follows the explicitly specified reference-plane relation. Confirm the sign on a simple structure before copying deembedding distances between software packages.

Setup order: define the physical cell and materials; pair lateral faces with the calculated phase; excite the required polarization and retain outgoing modes; refine mesh, port modes and spacing independently; extract amplitude/phase and move the reference plane. PBC solves the identical infinite array, LPA extends it approximately to a graded array, and deembedding removes known propagation.

```
:::

## 6.4 Retrieve bulk and sheet parameters

How can a complicated subwavelength metal/dielectric array be replaced by a homogeneous medium? Homogenization assigns a macroscopic model to microscopic structure. Bulk media use effective permittivity and permeability; thin sheets use surface impedance or electric, magnetic and magnetoelectric response tensors.

## 1. A symmetric slab and its scattering coefficients

For the source’s NRW-type retrieval, a slab of thickness $d$ with normalized wave impedance $z$ and index $n$ lies between identical air half-spaces. Illumination is normal. Reflection and transmission include internal multiple reflections; symmetry/reciprocity give $S_{11}=S_{22}$ and $S_{21}=S_{12}$ in the stated scalar model.

$$
S_{11}=\frac{R(1-T^2)}{1-R^2T^2},\qquad S_{21}=\frac{T(1-R^2)}{1-R^2T^2}.
$$

$$
R=\frac{z-1}{z+1},\qquad T=e^{-ik_0nd}=e^{-i(\omega/c)nd}.
$$

Here R is an interface field-reflection coefficient, not reflected power, and T is propagation inside the equivalent slab, not the measured S21. The source repeats these forward equations before performing the inversion; keeping those roles separate is essential.

## 2. Retrieve impedance, propagation and index

$$
z=\pm\sqrt{\frac{(1+S_{11})^2-S_{21}^2}{(1-S_{11})^2-S_{21}^2}}.
$$

Choose the physically admissible root, with nonnegative real impedance for the passive branch in this model. Then recover propagation:

$$
T=\frac{S_{21}}{1-S_{11}(z-1)/(z+1)}.
$$

The source writes the following logarithmic equality. Its second expression has the opposite signs to those implied by the first one:

$$
n=-\frac1{ik_0d}\ln T=\frac1{k_0d}[-i\ln|T|+\operatorname{Arg}T+2\pi m].\quad\text{[printed; inconsistent expansion]}
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
From $T=e^{-ik_0nd}$, the consistent branch formula is

$$
n_m=\frac{-\operatorname{Arg}T+2\pi m+i\ln|T|}{k_0d},\quad m\in\mathbb Z.
$$

For a decaying passive forward wave, $|T|\le1$ gives $\operatorname{Im}n\le0$. This fixes the expansion without changing the course convention. Choose the root/branch using the physical model and frequency continuity, not one inequality alone. The [Smith et al. primary retrieval paper](https://arxiv.org/abs/physics/0111203) is a reference; translate its convention before using its formulas.
:::

$$
\epsilon_{\rm eff}=n/z,\qquad\mu_{\rm eff}=nz.
$$

## 3. Branch ambiguity and numerical sensitivity

A principal argument jumps at its branch cut. Thick samples can admit several index branches; unwrap phase with a physical anchor, compare multiple thicknesses and use causality/passivity where appropriate. Starting at low frequency can help only when a justified low-frequency branch is available.

The source warns of unstable ratios near scattering zeros and suggests constrained fitting. Small S21 makes logarithms and ratios sensitive, but S11=0 by itself is not generally singular: a matched slab can be perfectly well behaved. Inspect the actual denominators and uncertainty.

## 4. Thin sheets and grounded input impedances

Bulk parameters of an extremely thin patterned sheet depend strongly on the assigned effective thickness. A sheet boundary can be more meaningful. The source’s electric-only sheet assumes tangential E continuity and a magnetic-field jump produced by electric surface current:

$$
\mathbf E_{t1}=\mathbf E_{t2}=\mathbf E_t,\qquad\hat{\mathbf n}\times(\mathbf H_{t1}-\mathbf H_{t2})=\mathbf J_s,\qquad\mathbf E_t=Z_s\mathbf J_s.
$$

The normal in this jump must point from region 2 into region 1. More general electric/magnetic sheets need GSTCs rather than this electric-only relation. A grounded structure has no transmission and supplies an input impedance at its chosen reference plane:

$$
S_{21}=0,\qquad Z_s=\eta_0\frac{1+S_{11}}{1-S_{11}}=R_s+iX_s.
$$

For nearly lossless reflection, the source states Rs≈0 and prints the following phase-only shortcut:

$$
X_s=-\frac{\eta_0}{2}\cot\left(\frac{\arg S_{11}}2\right).\quad\text{[printed; incorrect]}
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
For $S_{11}=e^{i\phi}$, direct factorization gives

$$
\frac{1+e^{i\phi}}{1-e^{i\phi}}=i\cot(\phi/2),\qquad X_s=\eta_0\cot(\phi/2).
$$

The printed shortcut has both a sign and a factor-of-two error. Branch choice cannot repair that algebra. Use the full complex ratio when |S11| differs from one.
:::

For a symmetric ungrounded shunt-sheet model, the source prints

$$
Y_s=\frac2{\eta_0}\frac{1-S_{21}-S_{11}}{S_{21}}.\quad\text{[printed]}
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
For a purely electric zero-thickness sheet in identical exterior media, $t=1+r$ and the consistent extraction is

$$
Y_s=\frac2{\eta_0}\left(\frac1t-1\right)=-\frac{2r}{\eta_0t}.
$$

With $t=1+r$, the printed expression is twice this value. A general FSS or metalens may have magnetic or magnetoelectric response; an arbitrary pair r,t cannot always be represented by one electric shunt admittance.
:::

| Structure | Suitable model | Extracted response |
|---|---|---|
| Bulk symmetric material | Homogeneous slab, NRW-type inversion | $\epsilon,\mu$ with branch and thickness checks |
| Grounded reflective surface | One-sided input impedance | $R_s,X_s$ at a specified plane |
| Ungrounded thin sheet | Electric/magnetic sheet or GSTC model | Sheet admittance/impedance or tensors |
| Chiral/anisotropic sheet | Full polarization-resolved response | Appropriate tensor/coupling parameters |

:::{admonition} Worked problem
:class: tip
Structure A is a passive symmetric slab in air, $d=6\,\mathrm{mm}$ and $f=10\,\mathrm{GHz}$, with face-referenced $S_{11}=-0.30i$, $S_{21}=0.60-0.20i$.

1. Retrieve z and choose its physical root.
2. Recover internal propagation T.
3. Calculate n on branch m=0.
4. Calculate effective permittivity and permeability.
5. Explain the principal-argument jump from +179° to −179°.

Structure B is grounded, with $S_{21}=0$ and $S_{11}=e^{-i120^\circ}$, using $\eta_0=377\,\Omega$.

6. Find the full complex surface/input impedance.
7. Find its resistance and reactance.
8. Check the phase-only shortcut against the full ratio.
9. Explain why unique bulk permittivity and permeability cannot be retrieved from this grounded one-port alone.

```{dropdown} Show the complete worked answer

### A. The printed calculation, followed by an independent correction

First establish the units and phase thickness:

$$
\lambda_0=\frac{3\times10^8}{10^{10}}=0.03\,\mathrm m=30\,\mathrm{mm},\qquad k_0=\frac{2\pi}{30}=\frac\pi{15}\approx0.20944\,\mathrm{rad/mm}.
$$

$$
k_0d=0.20944(6)\approx1.25664.
$$

The source expands the numerator and denominator correctly up to this point:

$$
1+S_{11}=1-0.30i,\qquad(1+S_{11})^2=1-0.60i-0.09=0.91-0.60i.
$$

$$
S_{21}^2=(0.60-0.20i)^2=0.36-0.24i-0.04=0.32-0.24i.
$$

$$
(1+S_{11})^2-S_{21}^2=(0.91-0.60i)-(0.32-0.24i)=0.59-0.36i.
$$

$$
1-S_{11}=1+0.30i,\quad(1-S_{11})^2=0.91+0.60i.
$$

$$
(1-S_{11})^2-S_{21}^2=(0.91+0.60i)-(0.32-0.24i)=0.59+0.84i.
$$

It then prints the following division and root; these values are not the result of that ratio:

$$
\frac{0.59-0.36i}{0.59+0.84i}\approx0.0135-0.6305i,\quad z\approx\pm(0.565-0.558i).\quad\text{[printed]}
$$

Using nonnegative real impedance, the source selects its positive-real root, then continues:

$$
z\approx0.565-0.558i,\quad z-1=-0.435-0.558i,\quad z+1=1.565-0.558i.\quad\text{[printed]}
$$

$$
R=\frac{z-1}{z+1}\approx-0.171-0.418i.\quad\text{[printed]}
$$

$$
S_{11}R=(-0.30i)(-0.171-0.418i)=-0.1254+0.0513i.\quad\text{[printed]}
$$

$$
1-S_{11}R=1.1254-0.0513i,\qquad T=\frac{0.60-0.20i}{1.1254-0.0513i}\approx0.540-0.153i.\quad\text{[printed]}
$$

$$
|T|\approx\sqrt{0.540^2+(-0.153)^2}\approx0.561,\quad\arg T\approx\tan^{-1}(-0.153/0.540)\approx-15.8^\circ.\quad\text{[printed]}
$$

The printed index calculation uses its inconsistent logarithm expansion, with m=0:

$$
\operatorname{Re}n=\frac{-0.276}{1.25664}\approx-0.220,\quad\ln(0.561)\approx-0.579,\quad\operatorname{Im}n=\frac{0.579}{1.25664}\approx0.461.\quad\text{[printed]}
$$

$$
n\approx-0.220+0.461i,\quad\epsilon_{\rm eff}=\frac{-0.220+0.461i}{0.565-0.558i}\approx-0.602+0.221i.\quad\text{[printed]}
$$

$$
\mu_{\rm eff}=(-0.220+0.461i)(0.565-0.558i)\approx0.133+0.383i.\quad\text{[printed]}
$$

The source calls positive Im n attenuation; with its stated negative spatial exponent it instead gives growth. The corrected branch below fixes this.

### Branch continuity

A smoothly increasing phase can move from 179° to 181°, while its principal argument jumps to −179°. Inserting that jump directly creates a spurious index discontinuity of magnitude

$$
|\Delta\operatorname{Re}n|=\frac{2\pi}{k_0d}.
$$

Unwrap the ±2π jumps consistently across frequency and choose the remaining branch with a physical anchor. Multiple thicknesses and causal/passive constraints can help, but unwrapping alone does not establish a valid homogeneous model.

### B. Grounded sheet: the full complex ratio

$$
S_{21}=0,\quad S_{11}=e^{-i120^\circ}=\cos(-120^\circ)+i\sin(-120^\circ)=-\frac12-i\frac{\sqrt3}{2}.
$$

$$
1+S_{11}=\frac12-i\frac{\sqrt3}{2},\qquad1-S_{11}=\frac32+i\frac{\sqrt3}{2}.
$$

$$
\frac{1+S_{11}}{1-S_{11}}=\frac{\frac12-i\frac{\sqrt3}{2}}{\frac32+i\frac{\sqrt3}{2}}=-\frac{i}{\sqrt3}\approx-0.5774i.
$$

$$
Z_s\approx377(-0.5774i)\approx-217.6i\,\Omega,\qquad R_s\approx0,\quad X_s\approx-217.6\,\Omega.
$$

The source’s rounded full-ratio result is correct: essentially lossless capacitive behavior. It then attempts its incorrect shortcut:

$$
\arg S_{11}/2=-60^\circ,\quad\cot(-60^\circ)=-1/\sqrt3\approx-0.5774.
$$

$$
-\frac{377}{2}(-0.5774)=188.5(0.5774)\approx108.8\,\Omega.\quad\text{[value implied by printed shortcut]}
$$

The source nevertheless returns −217.6 Ω and calls this agreement. It is not agreement: no branch choice turns that expression into the full-ratio result. The correct shortcut is

$$
X_s=377\cot(-60^\circ)=-\frac{377}{\sqrt3}\approx-217.66\,\Omega.
$$

A grounded one-port does not supply the through-propagation data needed to identify unique bulk n,z. Assigning an arbitrary effective thickness changes bulk ε,μ; a surface/input-impedance model is often more natural. A grounded substrate can itself have a bulk model, but reflection from the whole stack alone does not uniquely identify all its bulk parameters.

### Independent corrected calculation

**Independently recomputed structure A.** The source’s arithmetic errors start at the complex division, before the logarithm-sign error. Recompute without rounding intermediate values:

$$
\frac{0.59-0.36i}{0.59+0.84i}=0.04337098-0.67191800i,\quad z=0.59861811-0.56122425i.
$$
$$
R=-0.11380516-0.39102176i,\quad1-S_{11}R=1.11730653-0.03414155i.
$$
$$
T=0.54196943-0.16244094i,\quad|T|=0.56578965,\quad\arg T=-16.68470563^\circ.
$$
$$
n_0=\frac{i\log T}{k_0d}=0.23173202-0.45321990i.
$$
$$
\epsilon_{\rm eff}=0.58379246-0.20978551i,\quad\mu_{\rm eff}=-0.11563901-0.40135927i.
$$

Substituting these z,n into the two forward slab equations recovers the supplied S11,S21 to floating-point accuracy. This is an algebraic round-trip check for the assumed symmetric slab; a single frequency still cannot establish homogenization, unique branch selection or a broadband causal material model.

```
:::

## 6.5 Practical meshing and convergence

After mastering the equations, practical details separate a trustworthy simulation from a misleading one. Let us review local meshing, convergence, port placement and finite-array effects.

## 1. Mesh where the field needs it

Thin sharp metal edges can support singular fields. A coarse edge mesh can misrepresent local energy and shift the resonance. Refine gaps, corners and material discontinuities locally while keeping smooth exterior regions coarser. The source invokes Meixner’s edge behavior as the physical reason.

The source stresses matching meshes on paired periodic FEM faces and warns that uncontrolled interpolation can corrupt phase. More generally, use a boundary pairing supported by the discretization: matching meshes or a verified nonconforming/mortar constraint. A mismatch is not automatically invalid if the formulation handles it consistently.

## 2. Convergence targets

$$
\max_{ij}|S_{ij}^{(n)}-S_{ij}^{(n-1)}|<\delta_{\rm target}.
$$

The source gives 0.02 as an illustrative default and suggests 0.005–0.01 for phase-sensitive designs. Treat these as starting values, not accuracy guarantees. Compare the actual complex observable, phase away from zeros, power, and an independent refinement; two successive meshes may share a bias.

In time-domain runs, allow stored resonant energy to decay. The source lists −30, −40 and −50 dB relative-energy stopping levels. Ending early truncates the response and can create spectral ripples; inspect the spectrum’s stability as run duration increases, especially for high-Q resonances.

## 3. Hidden port and air-box mistakes

| Control | Source’s practical warning/example | What must actually be checked |
|---|---|---|
| Port height | Very short gap, below $\lambda/4$; suggested height $\lambda_0/2$ | Independent port-distance and evanescent-mode refinement |
| Port modes | Only fundamental retained; source suggests 2 or 6–10 modes | Count open orders and both polarizations; refine evanescent content |
| Deembedding | Wrong or forgotten reference plane | Complex response at the declared physical surface |

The suggested distances and counts are not universal. A normal-incidence large-period array may have many open orders; an oblique deeply subwavelength array may have only the fundamental spatial order.

## 4. When the finite array must be solved

Steep neighboring phase changes and array-edge truncation can invalidate local periodicity. The source gives phase-step ranges π/2 to 2π/3 and arrays of 10×10 to 30×30 as illustrative warning cases, then recommends finite-array checks with domain-decomposed FEM or MLFMM-accelerated MoM.

Those are examples, not universal breakdown thresholds or solver recommendations. Compare a uniform reference, a supercell with unequal neighbors and a finite array at the observables the design needs. Include illumination, aperture and edge termination. The existing coupling lab below is a direct computational connection.
