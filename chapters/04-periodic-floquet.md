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

The incident and transmitted half-spaces are homogeneous, isotropic, lossless media with positive real permittivity and permeability, and positive real indices $n_i$ and $n_t$. We set $k_y=0$ initially. Materials inside a future scattering structure may be more complicated; the real-index channel tests below apply to its homogeneous exterior regions.

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

```{figure} ../assets/chapter-04/period-and-phase.png
:alt: Repeated unequal and identical ridge motifs with element pitch and full repeat marked, together with incident-field phasors at corresponding positions.
:label: fig-ch04-period-phase

Original schematic and incident-phase calculation: $p=0.5\,\mu\mathrm m$, $\Lambda=3\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, $n_i=1$, and $\theta_i=12^\circ$. Unequal widths illustrate a six-element motif; they are not a solved device. Translation restores the material pattern while rotating the field phasor by $k_{x,i}\Lambda$. Identical elements also admit the shorter translation $p$.
```

**Predict from the drawing:** if the six elements become identical, which distance changes in the smallest material repeat, and does the incident wave's phase advance across the original $3\,\mu\mathrm m$ distance change?

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

:::{dropdown} Derivation: why the driven field inherits the incident phase
Assume a linear, periodic Maxwell problem with one plane-wave excitation and a unique outgoing scattering solution. Translate both fields by $\Lambda$ and remove the known incident phase:

$$
\widetilde{\mathbf E}(x,z)=e^{-ik_{x,i}\Lambda}\mathbf E(x+\Lambda,z),\qquad
\widetilde{\mathbf H}(x,z)=e^{-ik_{x,i}\Lambda}\mathbf H(x+\Lambda,z).
$$

The translated material coefficients are unchanged. The translated incident wave acquires $e^{ik_{x,i}\Lambda}$, which the prefactor cancels; the outgoing condition is unchanged too. Thus the tilded and original fields solve the same problem. Uniqueness makes them equal, yielding the Bloch relation. Multiplying the field by $e^{-ik_{x,i}x}$ then gives the periodic function $u$ used above.

This argument concerns a driven response, not an arbitrary sum of eigenmodes. At a lossless singularity with a nonunique homogeneous solution, specify the causal response by a limiting-absorption prescription; do not silently assume uniqueness. A finite array, a defect, or an excitation containing several tangential wavevectors also requires a different treatment or a superposition of Bloch sectors.
:::

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

:::{dropdown} Proof: why an artificial supercell cannot create new scattering orders
Suppose the actual primitive period is $p$ and the computational period is $\Lambda=Np$. The periodic field factor $u=e^{-ik_{x,i}x}E$ then has period $p$. Split its supercell Fourier integral into $N$ identical intervals:

$$
u_m=\frac{1}{Np}\int_0^{Np}u(x)e^{-i2\pi mx/(Np)}\,dx
=\frac{1}{Np}\int_0^p u(\xi)e^{-i2\pi m\xi/(Np)}\,d\xi
\sum_{j=0}^{N-1}e^{-i2\pi mj/N}.
$$

For integer $m$, the finite sum is a roots-of-unity sum:

$$
\sum_{j=0}^{N-1}e^{-i2\pi mj/N}
=\begin{cases}N,&m=N\ell,\quad\ell\in\mathbb Z,\\0,&m\notin N\mathbb Z.\end{cases}
$$

When the ratio is not one, the geometric-series numerator is $1-e^{-i2\pi m}=0$; when it is one, add $N$ ones directly. Therefore six identical cells allow nonzero supercell coefficients only at $m=6\ell$. The statement concerns the solved field's symmetry; it does not assume isolated, uncoupled elements.

The [cell-versus-supercell lab](../labs/10-coupling-lab.md) tests this extinction with an executed TE solver using a different geometry ($p=0.65\,\mu\mathrm m$, $N=6$). Its uniform-array control compares the same physical harmonic cutoff in primitive-cell and supercell calculations. The six unequal elements in the opening puzzle do not have this smaller translation symmetry.
:::

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

:::{dropdown} Derivation: the outgoing square root and the decay length
In a source-free, homogeneous isotropic exterior, Maxwell's equations give the scalar Helmholtz equation for a Cartesian field component. Substitution of one separated harmonic gives

$$
\left(\partial_x^2+\partial_s^2+n_o^2k_0^2\right)E_m=0
\quad\Longrightarrow\quad
\kappa_m^2=n_o^2k_0^2-k_{x,m}^2.
$$

For real positive $\epsilon,\mu$, the positive real root carries energy outward when the right-hand side is positive. If it is negative, the two roots are $\pm i\alpha_m$. The outgoing field in an unbounded half-space must not grow as $s\to\infty$, selecting $+i\alpha_m$:

$$
\alpha_m=k_0\sqrt{q_m^2-n_o^2},\qquad
\frac{|E_m(s)|}{|E_m(0)|}=e^{-\alpha_m s},\qquad
\frac{|E_m(s)|^2}{|E_m(0)|^2}=e^{-2\alpha_m s}.
$$

Setting each ratio to $e^{-1}$ gives the two decay lengths. “Intensity” here means squared field magnitude, not a nonzero normal power flow. Section 4.7 derives why its normal time-averaged Poynting flux is zero.
:::

```{figure} ../assets/chapter-04/outgoing-fields.png
:alt: Real-field maps and envelopes of unit-amplitude open, grazing, and evanescent TE harmonics in an outward coordinate, with their normalized normal flux.
:label: fig-ch04-outgoing

Three analytical exterior harmonics in $n_o=1$, with $q_m=0.6$, $1$, and $1.2$. Their interface electric-field amplitudes are equal, yet their normal fluxes differ. The closed harmonic oscillates along the surface and decays outward. These are basis fields, not a solved device near field.
```

**Read the picture:** at cutoff, a field may still vary along $x$ while having no phase progression in $s$. Explain why a visible field pattern alone does not establish outward power.

### Count every potentially open order

The strict interval for an open integer order is

$$
\frac{\Lambda}{\lambda_0}(-n_o-q_i)<m<
\frac{\Lambda}{\lambda_0}(n_o-q_i).
$$

The endpoints must be tested separately for grazing. The notebook enumerates a conservative enclosing integer interval and adds closed neighbors for plotting. A fixed window such as $m=-2,\ldots,2$ can silently miss channels when the period or output index increases.

For an exact-arithmetic count, call the lower and upper endpoints above $a$ and $b$. Strict inequalities give

$$
m_{\min}=\lfloor a\rfloor+1,\qquad
m_{\max}=\lceil b\rceil-1,\qquad
N_{\rm open}=\max\!\left(0,m_{\max}-m_{\min}+1\right).
$$

This formula excludes an integer endpoint automatically. Near a floating-point cutoff, use the notebook's explicit per-order classification rather than trusting a rounded endpoint.

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

:::{dropdown} Derivation: TE/TM power factors and why powers add by order
For $e^{-i\omega t}$, Faraday's law for a TE harmonic gives $\mathbf H=(\mathbf k\times\mathbf E)/(\omega\mu)$. With $\mathbf E=\hat{\mathbf y}E_y$, take the cross product and then the time-averaged Poynting vector:

$$
H_x=-\frac{k_z}{\omega\mu}E_y,\qquad
H_z=\frac{k_x}{\omega\mu}E_y,\qquad
\langle S_z\rangle=-\frac12\operatorname{Re}(E_yH_x^*)
=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\mu}\right)|E_y|^2.
$$

Divide the transmitted flux by the incident flux to obtain $T_m$. On the reflected side the outward flux is $-\langle S_z\rangle$, so a positive reflected power uses $\kappa_m$ rather than the negative laboratory $k_z$. For $k_z=\pm i\alpha$ and real $\mu$, the real part is zero: one outgoing evanescent harmonic carries no average normal power.

For TM, Ampère's law gives $\mathbf E=-(\mathbf k\times\mathbf H)/(\omega\epsilon)$. Using $\mathbf H=\hat{\mathbf y}H_y$ gives, away from $k_z=0$ for the last expression,

$$
E_x=\frac{k_z}{\omega\epsilon}H_y,\qquad
\langle S_z\rangle=\frac12\operatorname{Re}\!\left(\frac{k_z}{\omega\epsilon}\right)|H_y|^2
=\frac12\operatorname{Re}\!\left(\frac{\omega\epsilon}{k_z}\right)|E_x|^2.
$$

Thus TE $E_y$, TM $H_y$, and TM tangential $E_x$ coefficients require different stated normalizations. Evaluate cutoff using bounded physical fields or a limit; the $E_x$ admittance formula is singular at $k_z=0$.

Finally, average the outgoing field's normal flux across a full period. Products of distinct orders contain $e^{i(k_{x,m}-k_{x,n})x}$, and

$$
\frac1\Lambda\int_0^\Lambda e^{i(k_{x,m}-k_{x,n})x}\,dx
=\frac1\Lambda\int_0^\Lambda e^{i(m-n)Gx}\,dx=\delta_{mn}.
$$

This orthogonality removes cross terms between distinct orders. It justifies summing modal powers in homogeneous exterior planes even when the local Poynting pattern has interference fringes. It does not say that distinct orders never interfere locally or that evanescent fields can be removed from interface matching.
:::

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

:::{dropdown} Derivation: geometric series, first nulls, and aperture width
Define $\psi=\Lambda(k_{x,i}-n_ok_0\sin\theta)$. Sum the geometric series when $e^{i\psi}\ne1$:

$$
\mathcal A_N=\frac{1-e^{iN\psi}}{N(1-e^{i\psi})}
=e^{i(N-1)\psi/2}\frac{\sin(N\psi/2)}{N\sin(\psi/2)}.
$$

At $\psi=2\pi\ell$, the original sum gives $\mathcal A_N=1$; this is a removable singularity of the quotient. The matching condition is $k_{x,o}=k_{x,i}-\ell G$, hence the Floquet label is $m=-\ell$ in our convention.

For $N>1$, the first nulls adjacent to a maximum satisfy $\delta\psi=\pm2\pi/N$. Their locations in sine-angle coordinates are exact when they remain in the physical angular domain:

$$
\left|\sin\theta_{\rm null}-\sin\theta_m\right|=\frac{\lambda_0}{N\Lambda n_o}.
$$

For a narrow lobe away from grazing, linearize $\sin\theta$ about $\theta_m$ to obtain the full width between these first nulls, in radians:

$$
\Delta\theta_{\rm null}\approx\frac{2\lambda_0}{N\Lambda n_o\cos\theta_m}.
$$

Doubling $N$ approximately halves this width. Near grazing, use the exact sine-angle nulls; one null may fall outside the visible region and the small-angle approximation fails. $N\Lambda$ is the width scale of this uniformly weighted source model, not a claim about a particular fabricated aperture.
:::

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

:::{dropdown} Proof of the scan bound
Let $s_i=n_i\sin\theta_{\max}$ and $d=\lambda_0/\Lambda>0$. For every nonzero integer $m$, the reverse triangle inequality gives

$$
|q_i+md|\geq |m|d-|q_i|\geq d-s_i>n_o
\qquad\text{if}\qquad d>n_o+s_i.
$$

Thus all nonzero orders are strictly outside the light cone over the stated scan. At equality, an edge incidence and the oppositely signed first order can touch the cone. The proof is about channel geometry: an allowed extra channel can still have zero amplitude, and an element radiation pattern can suppress a finite-array maximum without changing this bound.
:::

## 4.9 Phase gradients and generalized refraction

For a prescribed transmission phase $\Phi(x)$, tangential phase matching motivates

$$
n_t k_0\sin\theta_t-n_i k_0\sin\theta_i=\frac{d\Phi}{dx}.
$$

This connects to the generalized reflection/refraction formulation of [Yu et al.](https://doi.org/10.1126/science.1210713). It specifies a desired phase-matching relation; useful efficiency also requires an electromagnetic design that supplies the required amplitudes and boundary response.

If the complex transmission function is periodic over $\Lambda$ and makes an ideal integer phase winding $\Phi(x+\Lambda)-\Phi(x)=2\pi q$, then the average gradient is $qG$. With our Fourier convention, an ideal prescribed factor $e^{iqGx}$ shifts the transmitted tangential wavevector to order $m=q$. A sampled or imperfect phase profile generally has additional Fourier harmonics.

:::{dropdown} Derivation: an ideal ramp, its sampled version, and spectral aliases
For a local prescribed scalar transmission $t(x)=e^{i\Phi(x)}$, the transmitted boundary phase is $k_{x,i}x+\Phi(x)$. A constant derivative gives a single tangential wavevector $k_{x,t}=k_{x,i}+\Phi'(x)$, yielding the phase-gradient relation. A varying derivative describes local phase slope; it does not make the entire output a single plane wave.

For a periodic $t$, its exact Fourier projection is

$$
c_m=\frac1\Lambda\int_0^\Lambda t(x)e^{-imGx}\,dx,\qquad
t(x)=e^{iqGx}\ \Longrightarrow\ c_m=\delta_{mq}.
$$

Now divide the period into $N$ equal bins and hold the ideal ramp's midpoint value constant in each bin: $t_j=e^{i2\pi q(j+1/2)/N}$ for integer $q$. Integrating within each bin, with $\operatorname{sinc}(v)=\sin(\pi v)/(\pi v)$ and $\operatorname{sinc}(0)=1$, gives

$$
c_m=\operatorname{sinc}\!\left(\frac mN\right)\frac1N
\sum_{j=0}^{N-1}e^{i2\pi(q-m)(j+1/2)/N}
=\begin{cases}
(-1)^\ell\operatorname{sinc}(m/N),&m=q+\ell N,\\
0,&\text{otherwise}.
\end{cases}
$$

The roots-of-unity sum reappears. For $q=1$ and $N=6$, the target coefficient has $|c_1|^2=\operatorname{sinc}^2(1/6)\approx0.912$; the closest aliases occur at $m=-5$ and $m=7$. These are squared Fourier coefficients of a prescribed boundary function, **not diffraction efficiencies**. Open-order flux factors and a realizable Maxwell solution are still required. Closed aliases are evanescent, not missing far-field energy that can simply be added to a power sum.
:::

```{figure} ../assets/chapter-04/sampled-phase-spectrum.png
:alt: Continuous and six-step midpoint-sampled phase ramps with their Fourier spectra and marked propagating order interval.
:label: fig-ch04-sampled-phase

An ideal scalar phase winding and its six-step approximation. The sampled function has aliases separated by six order labels. For normal incidence into air at $\Lambda=3\,\mu\mathrm m$ and $\lambda_0=1.55\,\mu\mathrm m$, only $m=-1,0,+1$ are open; the nearest nonzero aliases are closed. Sampling changes the coefficients while the exterior channel map remains fixed.
```

**Try a counterfactual:** reverse the phase ramp, then increase the number of steps while keeping $\Lambda$ fixed. Predict the target order, the alias spacing, and which part of the light-cone diagram stays unchanged.

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
