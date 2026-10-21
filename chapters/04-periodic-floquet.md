---
title: 'Chapter 4: Periodic Structures and Floquet Analysis'
short_title: Periodicity and diffraction
description: Derive Bloch phases and diffraction channels, distinguish cutoff from propagation, and connect channel maps to validated periodic simulations.
---

# Chapter 4: Periodic Structures and Floquet Analysis

**Central question:** which beams can leave a periodic metasurface, and what calculation tells us how much power they carry?

Imagine six different elements spaced by $500\,\mathrm{nm}$. Repeat that six-element sequence and illuminate it at a free-space wavelength of $1.55\,\mu\mathrm m$. Can the surface scatter into a nonzero angle in air? Make a prediction before choosing a formula: does the relevant period equal the element spacing or the length of the complete repeated sequence?

This chapter develops the translation symmetry, the allowed wavevectors, and the numerical checks needed to answer that question. The [browser explorer](../labs/04-floquet-lab.md) and [editable notebook](../notebooks/04-floquet-orders.ipynb) calculate channel geometry. The lab also specifies a later full-wave calculation for the channel amplitudes.

:::{note} Evidence available in this chapter
The channel maps, limiting cases, finite-array factors, and flat-interface power checks have analytical models and executable code. The periodic-grating and metasurface solver investigations are detailed lab outlines. No full-wave efficiency or fabricated-device performance is claimed for those structures.
:::

## 4.1 Goals and conventions

After this chapter, you should be able to:

1. Identify a primitive period and distinguish it from an element pitch or computational supercell.
2. Derive the Bloch phase and the tangential wavevectors of Floquet orders.
3. Classify each order separately in the reflection and transmission media, including grazing cutoff.
4. Explain why an allowed channel can have zero amplitude and why closed orders still matter numerically.
5. Set up a periodic scattering calculation and assess its order-resolved power and convergence.

Prerequisites are plane waves, phasors, tangential boundary conditions, Fourier series, and basic complex algebra. The [worked examples and teaching guide](04-floquet-guide.md) include a short learning path.

We use time dependence $e^{-i\omega t}$ and spatial dependence $e^{i\mathbf k\cdot\mathbf r}$. The surface is near $z=0$, periodic along $x$ with period $\Lambda$, and invariant along $y$ in the introductory model. A plane wave arrives from $z<0$ and travels toward positive $z$. Angles are signed from the relevant outward surface normal, with a positive angle having positive $k_x$.

The incident and transmitted half-spaces are homogeneous, isotropic, lossless media with positive real indices $n_i$ and $n_t$. We set $k_y=0$ initially. Materials inside a future scattering structure may be more complicated; the real-index channel tests below apply to its homogeneous exterior regions.

| Symbol | Meaning |
| --- | --- |
| $\lambda_0$, $k_0=2\pi/\lambda_0$ | Free-space wavelength and wavenumber |
| $\Lambda$, $G=2\pi/\Lambda$ | Structural period and reciprocal-lattice spacing |
| $k_{x,i}=n_i k_0\sin\theta_i$ | Incident tangential wavevector |
| $m\in\mathbb Z$ | Diffraction-order label under our sign convention |
| $n_o$ | Index of the output region being examined: $n_i$ for reflection or $n_t$ for transmission |

## 4.2 Find the pattern that actually repeats

A translation by a primitive period restores the complete material distribution. Translating by one pitch in a row of different pillars generally replaces one geometry with another. Translating by the complete sequence restores it. For six distinct elements separated by $p=0.5\,\mu\mathrm m$, a possible primitive period is $\Lambda=6p=3\,\mu\mathrm m$.

The word *possible* matters: if the sequence itself has a smaller repeating subset, use that smaller period. A numerical cell may contain several primitive cells for convenience, but its extra order labels do not create new physical scattering mechanisms.

For example, place six identical elements inside a computational cell of length $6p$. The structure still has period $p$. In an expansion using $6p$, the smaller translation symmetry forces nonzero coefficients to occur only at supercell orders $m=6\ell$. Other supercell channels may lie inside the output light cone but have zero amplitude.

:::{tip} A physical demonstration
Draw six different symbols on a strip and repeat the strip. Slide a transparent copy until every symbol matches. Repeat with six identical symbols. The smallest matching translation changes, even though the spacing between adjacent symbols does not.
:::

## 4.3 Translation symmetry and the Bloch phase

For one incident plane wave, the driven scattering solution lies in the same Bloch sector as the excitation. A field component can be written

$$
E(x,z)=e^{ik_{x,i}x}u(x,z),\qquad u(x+\Lambda,z)=u(x,z).
$$

It follows that

$$
E(x+\Lambda,z)=e^{ik_{x,i}\Lambda}E(x,z).
$$

This is a phase relation between paired lateral boundaries. At normal incidence the multiplier is one. At oblique incidence, an ordinary zero-phase periodic condition generally represents a different excitation.

The boundary mapping direction matters. If a solver defines destination $x+\Lambda$ from source $x$, the multiplier under our convention is $e^{+ik_{x,i}\Lambda}$. Reversing the mapping requires its inverse. Some solvers use a different phasor or built-in phase convention. Verify the actual translated plane wave instead of copying a sign from a screenshot.

### Bloch wavevectors differing by a reciprocal vector

Replacing $k_{x,i}$ by $k_{x,i}+\ell G$ leaves the translation multiplier unchanged because $e^{i\ell G\Lambda}=1$. This is the origin of reciprocal-lattice equivalence. It relabels harmonics; it does not change their physical tangential wavevectors when the labels are shifted consistently. The incident wavevector remains fixed by the physical incidence condition.

## 4.4 Derive the Floquet orders

Expand the periodic factor in a Fourier series:

$$
u(x,z)=\sum_{m=-\infty}^{\infty}u_m(z)e^{imGx}.
$$

Substituting gives

$$
E(x,z)=\sum_m u_m(z)e^{ik_{x,m}x},\qquad
\boxed{k_{x,m}=k_{x,i}+\frac{2\pi m}{\Lambda}}.
$$

All harmonics have the same Bloch multiplier. The periodic pattern permits tangential momentum changes in integer multiples of $G$. Material properties and boundary conditions determine the coefficients $u_m$.

The following dimensionless form makes the design parameters easier to compare:

$$
q_i=n_i\sin\theta_i,\qquad
q_m=\frac{k_{x,m}}{k_0}=q_i+m\frac{\lambda_0}{\Lambda}.
$$

In a wavevector diagram, the orders are equally spaced points along the tangential axis. Changing incidence translates the whole set; changing $\lambda_0/\Lambda$ changes its spacing.

```{mermaid}
flowchart TD
    A[Identify the actual repeat distance] --> B[Compute the incident Bloch phase]
    B --> C[Enumerate tangential Floquet wavevectors]
    C --> D[Classify channels in each exterior medium]
    D --> E[Solve for complex amplitudes]
    E --> F[Normalize power and verify convergence]
```

## 4.5 Open, grazing, and evanescent channels

In output region $o$, the homogeneous-medium dispersion relation gives

$$
k_{z,m}^2=(n_o k_0)^2-k_{x,m}^2.
$$

For an outward distance $s\geq0$ measured away from the surface, define

$$
\kappa_m=k_0\sqrt{n_o^2-q_m^2},\qquad
E_m\propto e^{ik_{x,m}x}e^{i\kappa_m s},
$$

with the outgoing branch: nonnegative real $\kappa_m$ for propagation and positive imaginary $\kappa_m$ for decay. In laboratory coordinates, transmitted waves have $k_z=+\kappa_m$ and reflected waves have $k_z=-\kappa_m$ because their outward directions differ.

| Condition | Classification | Interpretation |
| --- | --- | --- |
| $|q_m|<n_o$ | Open / propagating | A real normal component allows outgoing normal power |
| $|q_m|=n_o$ | Grazing cutoff | The normal component vanishes; the limiting direction is $\pm90^\circ$ |
| $|q_m|>n_o$ | Closed / evanescent | The outgoing solution decays away from the surface |

For an open order,

$$
\theta_m=\sin^{-1}\!\left(\frac{q_m}{n_o}\right).
$$

Do not clip an arbitrary value outside $[-1,1]$ and report a grazing beam. First classify the channel. The notebook uses a dimensionless tolerance around $|q_m|/n_o=1$ and reports near-cutoff cases separately. That tolerance handles floating-point classification; it is not an uncertainty estimate for wavelength, material data, or geometry.

### What does an evanescent order do?

If $\kappa_m=i\alpha_m$ with $\alpha_m>0$, its amplitude varies as $e^{-\alpha_m s}$. Its amplitude decay length is $1/\alpha_m$; its intensity decay length is $1/(2\alpha_m)$. In the specified lossless homogeneous exterior, one such isolated outgoing harmonic carries no net normal time-averaged power. It can still store reactive energy, affect interface matching, and mediate coupling near the structure.

Consequently, “closed in the far field” does not mean “safe to remove from an RCWA expansion.” Near cutoff, $\alpha_m$ can be small and the decay length large. Numerical harmonic convergence and port/reference-plane placement deserve particular attention there.

### Count every potentially open order

The strict interval for an open integer order is

$$
\frac{\Lambda}{\lambda_0}(-n_o-q_i)<m<
\frac{\Lambda}{\lambda_0}(n_o-q_i).
$$

The endpoints must be tested separately for grazing. The notebook enumerates a conservative enclosing integer interval and adds closed neighbors for plotting. A fixed window such as $m=-2,\ldots,2$ can silently miss channels when the period or output index increases.

## 4.6 Two output media, two channel maps

Apply the classification separately with $n_o=n_i$ for reflection and $n_o=n_t$ for transmission. Both sides share $k_{x,m}$, but their light-cone boundaries differ. A larger refractive index can support additional propagating orders.

For $\Lambda=3\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, and normal incidence, air supports $m=-1,0,+1$. An output medium with $n_o=1.5$ supports $m=-2,-1,0,+1,+2$. At oblique incidence, the set can become asymmetric: negative and positive order labels need not open together.

```{figure} ../assets/chapter-04/channel-maps.png
:alt: Tangential wavevector positions relative to air and glass light cones, and an incidence-wavelength map of the number of open transmitted orders.
:label: fig-ch04-channels

Analytical channel geometry from the executed notebook. The map counts possible outgoing channels. No scattering amplitude or diffraction efficiency is assigned to them.
```

## 4.7 Channel existence and diffraction efficiency

Knowing $k_{x,m}$ and $k_{z,m}$ identifies the available basis waves. Solving Maxwell's boundary-value problem determines their amplitudes. A symmetry-forbidden order, an unpatterned interface, or destructive interference can give zero amplitude in an open channel.

To convert amplitudes into power, state their normalization. For a TE wave represented by $E_y$ in an isotropic lossless medium,

$$
\langle S_z\rangle=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\mu}\right)|E_y|^2.
$$

For an open transmitted order with $t_m=E_{y,m}^{(t)}/E_{y,i}$,

$$
T_m=\frac{k_{z,m}^{(t)}/\mu_t}{k_{z,i}/\mu_i}|t_m|^2.
$$

With equal permeabilities, the factor is $n_t\cos\theta_m/(n_i\cos\theta_i)$. This expression is for the stated TE electric-field amplitude. A TM coefficient defined using tangential $E_x$ needs a different admittance factor; using $H_y$ gives a corresponding expression with $\epsilon$ in place of $\mu$. For compatible **power-normalized** port amplitudes, squared magnitude directly gives the power fraction.

For a passive scattering problem, use all outgoing propagating channels and any genuine absorption:

$$
\sum_{m\in\mathcal P_r}R_m+
\sum_{m\in\mathcal P_t}T_m+A=1.
$$

At exact grazing, a bounded field amplitude has zero normal flux. Power normalization becomes delicate as the normal component approaches zero. A closed-channel field coefficient should not be counted as an extra far-field power fraction.

### An analytical amplitude benchmark

At a flat nonmagnetic interface, translational invariance permits only the physical specular response, even if an artificial periodic cell lists many open channels. At normal incidence from $n_i=1$ to $n_t=1.5$, the TE Fresnel amplitudes are $r=-0.2$ and $t=0.8$. Thus $R=0.04$, $T=1.5|0.8|^2=0.96$, and $R+T=1$. Squaring $t$ alone would incorrectly report $T=0.64$.

The notebook checks this case and a total-internal-reflection limit. These are analytical interface checks, not simulations of a patterned metasurface. For numerical mode/flux normalization examples, see the official [Meep mode-decomposition tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/).

## 4.8 Finite arrays and grating lobes

An infinite periodic calculation produces discrete Floquet directions. A finite illuminated array has angular lobes with nonzero width. For $N$ equally spaced prescribed scalar sources with identical weights and the incident phase progression, a normalized array factor is

$$
\mathcal A_N(\theta)=\frac1N\sum_{j=0}^{N-1}
\exp\!\left[ij\Lambda(k_{x,i}-n_o k_0\sin\theta)\right].
$$

Its maxima occur at the same tangential matching conditions when they lie inside the output light cone. Increasing $N$ narrows the peaks. The notebook computes the sum directly, avoiding a removable $0/0$ singularity in a sine-ratio formula.

```{figure} ../assets/chapter-04/finite-array.png
:alt: Normalized squared scalar array factors for three finite array lengths, with analytical Floquet angles marked as vertical lines.
:label: fig-ch04-array

Prescribed scalar array factors for 8, 24, and 64 repeated sources. The vertical markers are analytical Floquet directions. This plot does not include an element radiation pattern, mutual coupling, vector boundary matching, or a power-normalized metasurface efficiency.
```

In scanning-array language, unwanted additional visible maxima are grating lobes. Suppose all incidence angles satisfy $|\theta_i|\leq\theta_{\max}$ and the zeroth order remains open. A sufficient condition to keep every nonzero order closed throughout that scan is

$$
\frac{\lambda_0}{\Lambda}>n_o+n_i\sin\theta_{\max}.
$$

For equal unit indices and the limiting full scan toward $90^\circ$, this becomes the familiar strict half-wavelength-spacing condition. At normal incidence alone the corresponding bound is $\Lambda<\lambda_0/n_o$. Always state the medium, wavelength, scan range, and whether equality means an excluded grazing case. For a broadband requirement, check the smallest relevant wavelength and the actual dispersion.

## 4.9 Phase gradients and generalized refraction

For a prescribed transmission phase $\Phi(x)$, tangential phase matching motivates

$$
n_t k_0\sin\theta_t-n_i k_0\sin\theta_i=\frac{d\Phi}{dx}.
$$

This connects to the generalized reflection/refraction formulation of [Yu et al.](https://doi.org/10.1126/science.1210713). It specifies a desired phase-matching relation; useful efficiency also requires an electromagnetic design that supplies the required amplitudes and boundary response.

If the complex transmission function is periodic over $\Lambda$ and makes an ideal integer phase winding $\Phi(x+\Lambda)-\Phi(x)=2\pi q$, then the average gradient is $qG$. With our Fourier convention, an ideal prescribed factor $e^{iqGx}$ shifts the transmitted tangential wavevector to order $m=q$. A sampled or imperfect phase profile generally has additional Fourier harmonics.

A real sequence of resonant elements need not realize that ideal scalar transmission function. Material dispersion, amplitude variation, coupling, and impedance mismatch can change its performance. Floquet channels describe the periodic scattering basis; a phase-gradient design seeks to excite selected coefficients in that basis.

## 4.10 From a channel map to a periodic solver

Start with a homogeneous or flat-interface cell whose response is analytically known. Then introduce a simple grating. Use the following checks before a large parameter sweep:

1. Specify coordinates, the actual period, excitation, exterior indices, polarization, and phasor convention.
2. Apply the correct lateral Bloch phase and check that a translated incident wave satisfies it.
3. Use homogeneous exterior regions and outgoing ports or suitable absorbing boundaries. Include every propagating order across the complete sweep on both sides.
4. Match solver order labels to tangential wavevectors; a solver may index orders with a different sign or basis.
5. Normalize incident and outgoing power consistently. Compare modal power with an independent flux calculation where available.
6. Refine mesh, harmonic truncation, port distance, or domain/PML settings as appropriate. Power balance alone cannot establish convergence of each order's amplitude or phase.
7. Record reference planes, complex coefficients, failures, and the residual in all-channel power accounting.

The [full-wave lab outline](../labs/04-floquet-lab.md) gives a staged flat-interface, dielectric-grating, and optional six-pillar investigation. The official [COMSOL beam-deflector example](https://www.comsol.com/model/metasurface-beam-deflector-115971) provides a concrete six-post Si/SiO2 reference using periodic boundaries and diffraction-order ports. Its supplied geometry and solver instructions are external reference material; our executed results here are analytical.

### Beyond the introductory model

For a two-dimensional lattice,

$$
\mathbf k_{\parallel,mn}=\mathbf k_{\parallel,i}+m\mathbf G_1+n\mathbf G_2.
$$

In an isotropic lossless exterior, compare its squared magnitude with $(n_o k_0)^2$. The notebook includes a small rectangular-lattice example so that the one-dimensional condition is not mistaken for a general two-dimensional rule. Lossy, anisotropic, nonlocal, or time-modulated systems require an appropriate dispersion relation and outgoing-wave/energy-flow analysis. A real-angle `arcsin` test is not a universal classification algorithm.

## 4.11 Exercises and discussion

1. Derive the Bloch multiplier for a translation by $-\Lambda$. Explain why the multiplier alone cannot identify the incident diffraction-order label.
2. Solve the six-element opening puzzle for air and for an output index of 1.5. Calculate each open angle.
3. Using $\lambda_0=30\,\mathrm{mm}$, $\Lambda=25\,\mathrm{mm}$, and $\theta_i=20^\circ$ in air, calculate the phase advance and every open order. Which sign of the first order propagates?
4. Find the incidence angle where $m=-1$ reaches grazing for $\Lambda=0.8\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, $n_i=1$, and $n_o=1.5$. Repeat for $n_o=1$.
5. Explain how a computational supercell can list propagating channels that have zero amplitude because the actual primitive period is smaller.
6. Derive the TE power factor and explain how the definition of a TM field coefficient changes the normalization.
7. Compare finite arrays of different lengths. Which features are determined by periodicity, which by aperture length, and which are absent from the scalar model?
8. Design a numerical convergence study near a diffraction cutoff. Distinguish a channel-classification tolerance from a solver convergence tolerance.
9. Propose a full-wave experiment that separates an incorrect period, incorrect Bloch phase, omitted output channel, and poor phase-gradient design.

Continue with the [worked examples](04-floquet-guide.md), [browser explorer and lab](../labs/04-floquet-lab.md), and [executed notebook](../notebooks/04-floquet-orders.ipynb).

## References and further reading

- Yu et al., *Light Propagation with Phase Discontinuities: Generalized Laws of Reflection and Refraction*, Science 334, 333-337 (2011). [Article](https://doi.org/10.1126/science.1210713); [author's publication page](https://capasso.seas.harvard.edu/publications/light-propagation-phase-discontinuities-generalized-laws-reflection-and).
- COMSOL, [Diffraction Grating Theory](https://doc.comsol.com/6.4/doc/com.comsol.help.roptics/roptics_ug_optics.6.74.html). A software reference for grating directions; distinguish ray-direction models from full-wave amplitude calculations.
- COMSOL, [Metasurface Beam Deflector, Application ID 115971](https://www.comsol.com/model/metasurface-beam-deflector-115971). A periodic six-post reference geometry and solver example.
- Meep, [Mode Decomposition](https://meep.readthedocs.io/en/latest/Python_Tutorials/Mode_Decomposition/). Official diffraction and modal-power examples for a future solver implementation.

The derivations, figures, exercises, and exploratory code in this chapter are original course material. The browser and notebook models state their assumptions explicitly so that their claims can be extended through later full-wave validation.
