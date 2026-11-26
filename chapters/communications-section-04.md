# 8.4 Metasurface lenses and orbital angular momentum

Instructor booklet, pages 218–223.

A dielectric lens changes phase through thickness or optical path length. Bulk and weight, especially at longer wavelengths, and the mismatch between curved shapes and flat PCB or semiconductor fabrication limit its use. A **metalens** applies a phase jump at a thin discontinuity.

## 8.4.1 Designing flat metalenses

**Focusing phase profile.** A point feed at $(0,0,-F)$ illuminates the plane $z=0$. At radius $r=\sqrt{x^2+y^2}$, the path and incident phase are

$$
d(r)=\sqrt{F^2+r^2},\qquad \phi_{\rm inc}(r)=-k_0d(r),\qquad k_0=\frac{2\pi}{\lambda_0}.
$$

For a plane output wave, require $\phi_{\rm inc}(r)+\Phi(r)=\Phi_0$. Use the center as the reference so that $\Phi(0)=0$ and $\Phi_0=-k_0F$. With $t=e^{i\Phi}$, the design-frequency hyperbolic phase of the aplanatic metalens is

$$
\Phi_{\rm coll}(r)=k_0\left(\sqrt{F^2+r^2}-F\right)\pmod{2\pi}.
$$

**Off-axis metalens.** For a tilted output beam, generalized Snell matching adds the tangential phase gradient of that plane wave to the radial term.

$$
\Phi(x,y)=\Phi_{\rm coll}(r)-k_0(x\sin\theta_0\cos\phi_0+y\sin\theta_0\sin\phi_0).
$$

The first term compensates curvature and the second sets direction. Combining both in a subwavelength layer is useful for microwave and terahertz transmitters.

## 8.4.2 Gradient-index metasurface lenses (Luneburg and Maxwell fisheye)

**Index profile.** In a gradient-index (GRIN) lens, varying the cells gradually changes the phase constant along the in-plane path. The Luneburg lens of radius $R$ has

$$
n(r)=\sqrt{2-(r/R)^2},\quad 0\le r\le R,\qquad
n_{\rm MF}(r)=\frac{2}{1+(r/R)^2}.
$$

The Luneburg index falls from $\sqrt2$ at the center to $1$ at the rim. Index continuity helps matching. In a real structure the impedance and guided-to-free-space transition also matter. The normalized Maxwell fisheye profile falls from $2$ to $1$ and in its ideal model gives point-to-point imaging.

**Multi-beam coverage.** In the Luneburg ray model a rim feed produces a collimated beam facing the opposite side. Rim feeds can select directions over a full turn or form simultaneous beams with a fixed lens. Metal patch density, slot size, or etch depth on a uniform dielectric can approximate the profile.

## 8.4.3 Orbital angular momentum (OAM) and spatial multiplexing

**Spin and orbital contributions.** Spin angular momentum (SAM) describes field-vector rotation in circular polarization, with two circular states labeled $s=\pm1$. OAM describes the spatial **helical wavefront**. Phase $\psi(\varphi)=l\varphi$ winds around the axis with integer topological charge $l$.

**Orthogonality and multiplexing.** With full azimuthal sampling and appropriate weighting,

$$
\frac{1}{2\pi}\int_0^{2\pi} e^{i(l_1-l_2)\varphi}\,d\varphi=\delta_{l_1,l_2}.
$$

Independent streams can therefore occupy separate modes at the same frequency and polarization. Mathematical orthogonality alone leaves usable channel count and capacity undetermined. Both terminals and sufficient power per mode are required.

**Synthesizing a vortex beam.** Dividing the surface into angular sectors approximates this profile.

$$
\Phi_{\rm OAM}(r,\varphi)=l\varphi+\Phi_{\rm focusing}(r).
$$

For a pure scalar $l\ne0$ mode, continuity and undefined azimuth on axis require the field to vanish there. A donut-shaped beam can result.

## 8.4.4 Practical limits of OAM links

1. **Beam divergence.** Among zero-radial-order beams with a common waist, the ring angle grows roughly as $\sqrt{\lvert l\rvert}$. A larger aperture collects more power.

2. **Sensitivity to misalignment.** Aperture displacement or tilt changes angular sampling and creates modal crosstalk. Fixed point-to-point line-of-sight backhaul is an example application for evaluating high-rate links.

## Worked problem on lenses, tilted beams, and OAM

::::{admonition} Try it first
:class: book-exercise

In a data-center line-of-sight link, a circular transmissive phase sheet of radius $R=30\,\mathrm{mm}$ lies at $z=0$. The feed at $(0,0,-F)$ with $F=40\,\mathrm{mm}$ illuminates it at $60\,\mathrm{GHz}$. Assume an ideal phase-only sheet.

1. Find the phase at $(15,0,0)\,\mathrm{mm}$ for an axial beam and a $30^\circ$ beam tilted toward $+x$.
2. Find the index at the center, halfway point, and rim of a Luneburg lens of this radius, and explain the effect of moving the feed.
3. What phase is required for modes $l=0$ and $l=+1$ at the same polarization? Does orthogonality survive if the receiver sees half the azimuths?
4. The beam width parameter at the receive plane is $w=60\,\mathrm{mm}$. What fraction of each mode's power enters a coaxial aperture $a=w/\sqrt2$?

```{dropdown} Show the full worked answer

### 1. Axial and tilted beams

At $60\,\mathrm{GHz}$, $\lambda_0\simeq5\,\mathrm{mm}$. The radial phase compensates the path phase. Direct substitution gives $-k_0d+\Phi_{\rm coll}=-k_0F$. At $r=15\,\mathrm{mm}$,

$$
\Delta d=\sqrt{40^2+15^2}-40\simeq2.720\,\mathrm{mm},\qquad
\Phi_{\rm coll}\simeq360^\circ\frac{2.720}{5}=195.8^\circ.
$$

In the reciprocal model, a plane wave incident from the other side focuses at the feed. The finite aperture determines angular width and spot size. For the $30^\circ$ beam in the $+x$ direction, add the linear phase.

$$
\Phi_{\rm off}=\Phi_{\rm coll}-k_0 x\sin30^\circ
=195.8^\circ-540^\circ\equiv15.8^\circ\pmod{360^\circ}.
$$

The real cell must realize that profile with adequate transmission amplitude. Broadband operation also depends on amplitude and phase dispersion.

### 2. Selecting the direction with a Luneburg lens

| Position | Calculation | Index |
| --- | --- | --- |
| Center, $r=0$ | $\sqrt2$ | $1.414$ |
| Halfway, $r=15\,\mathrm{mm}$ | $\sqrt{2-0.5^2}$ | $1.323$ |
| Rim, $r=30\,\mathrm{mm}$ | $\sqrt{2-1^2}$ | $1.000$ |

In the ideal model a $+x$ rim feed produces a beam toward $-x$. Moving it to $+y$ produces a beam toward $-y$. Selecting a rim feed changes direction using the same profile. Check impedance matching at the rim separately. A Maxwell fisheye with center index $2$ is for point-to-point imaging, with a different function from Luneburg rim-to-beam collimation.

### 3. Generating and separating modes

$$
\Phi_l(r,\varphi)=\Phi_{\rm coll}(r)+l\varphi\pmod{2\pi}.
$$

At $l=0$ the azimuthal phase is constant. At $l=+1$ the unwrapped phase at azimuths $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$ takes those four values and advances $360^\circ$ in a complete turn. Both modes can share the same linear polarization. The on-axis null holds for a pure scalar $l\ne0$ mode. Adding $l=0$ can fill it.

A receiver extracts mode $m$ by weighting by $e^{-im\varphi}$ and summing. Full coverage gives zero angular overlap. For a uniformly weighted half circle,

$$
C_{01}(2\pi)=\frac{1}{2\pi}\int_0^{2\pi}e^{i\varphi}\,d\varphi=0,\qquad
C_{01}(\pi)=\frac1\pi\int_0^\pi e^{i\varphi}\,d\varphi=\frac{2i}{\pi},\quad
\lvert C_{01}(\pi)\rvert\simeq0.637.
$$

Asymmetric reception or misalignment can mix modes. The $0.637$ is angular overlap. Physical crosstalk also depends on radial profiles, powers, and processing. A passive single-feed surface can distribute a signal over several modes. **Two independent streams** require two independent signals.

### 4. Power collected by a finite aperture

Approximate the fundamental and zero-radial-order vortex intensities at radius $\rho$ by

$$
I_0(\rho)\propto e^{-2\rho^2/w^2},\qquad
I_1(\rho)\propto\frac{2\rho^2}{w^2}e^{-2\rho^2/w^2}.
$$

Using ring area weight $\rho\,d\rho$, substitute $u=2\rho^2/w^2$ and $U=2a^2/w^2$ to obtain the normalized integrals.

$$
\eta_0=\int_0^U e^{-u}\,du=1-e^{-U},\qquad
\eta_1=\int_0^U ue^{-u}\,du=1-(1+U)e^{-U}.
$$

For $a\simeq42.4\,\mathrm{mm}$, $U=1$.

| Mode | Collected power fraction | Aperture loss |
| --- | --- | --- |
| $l=0$ | $1-e^{-1}\simeq63.2\%$ | $2.0\,\mathrm{dB}$ |
| $l=+1$ | $1-2e^{-1}\simeq26.4\%$ | $5.8\,\mathrm{dB}$ |

For equal total power the aperture collects about $3.8\,\mathrm{dB}$ less from the vortex mode. A small coaxial aperture still has azimuthal symmetry. Evaluate **power loss and modal mixing** separately. In this beam family the ring radius is roughly $w\sqrt{\lvert l\rvert/2}$. A growing $w$ or larger $\lvert l\rvert$ calls for a larger aperture. Radial compensation plus a linear gradient gives a directional beam. A Luneburg lens selects direction by feed position. An OAM link needs checks on both collected power and separation.
```
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
