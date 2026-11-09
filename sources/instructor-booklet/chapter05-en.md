## From analysis to synthesis

Until now, we mostly acted as analysts: given geometry and materials, calculate the scattered fields and S-parameters. Engineering often reverses the question: “Steer this normally incident wave through 45 degrees,” or “Focus it ten centimeters away.” Synthesis works backward from the requested field to a surface response and a physical structure. Analysis asks what a structure does; synthesis asks what structure could do the required job. A well-posed forward model has a specified excitation and radiation conditions; inverse design can have multiple solutions or no feasible solution.

The textbook proposes three steps: specify the input/output fields; translate them into phase, amplitude, impedance or susceptibility; then select and place physical cells from a library. The inverse problem needs analytical formulation, optimization and independent electromagnetic verification, not merely a simulation screenshot.


$$
\text{fields}\ \longrightarrow\ \text{surface response}\ \longrightarrow\ \text{geometry}.
$$


## Specify the wave transformation

Place the sheet at $z=0$ and describe its incident and desired outgoing fields. Their ratio gives a local scalar target when that approximation is appropriate. Define the phase lag as the outgoing lag minus the incident lag. The source writes a positive exponential for transmission beside this lag difference, which is algebraically inconsistent. Under our fixed positive-time convention, the ratio below uses a negative exponential; the signed transmission argument is the negative of the lag.

For steering, subtract the incident tangential phase from the outgoing one. For a metalens, compensate the extra distance to the focus. For a vortex, an integer charge produces a full $2\pi\ell$ winding; use atan2 rather than a single-quadrant arctangent. An OAM phase label alone does not guarantee extra communication capacity. Two practical obstacles remain: the normal power densities may not match, and locally periodic cells are coupled to their actual neighbors. A steep profile or strong resonance needs a supercell or finite-device check.


$$
E_{\rm inc}(\mathbf r)=A_{\rm inc}e^{-i\phi_{\rm inc}},\qquad
E_{\rm out}(\mathbf r)=A_{\rm out}e^{-i\phi_{\rm out}},\qquad\mathbf r=(x,y).
$$
$$
T(\mathbf r)=\frac{E_{\rm out}}{E_{\rm inc}}
=\frac{A_{\rm out}}{A_{\rm inc}}e^{-i\Phi},\qquad
\Phi=\phi_{\rm out}-\phi_{\rm inc}\pmod{2\pi}.
$$
$$
\Phi(x)=k_0x(\sin\theta_{\rm out}-\sin\theta_{\rm in}),\qquad
\frac{d\Phi}{dx}=k_0(\sin\theta_{\rm out}-\sin\theta_{\rm in}).
$$
$$
\Phi_{\rm lens}(x,y)=k_0\left(F-\sqrt{x^2+y^2+F^2}\right),\qquad
\Phi_{\rm vortex}(r,\varphi)=\ell\varphi,\quad\varphi=\operatorname{atan2}(y,x).
$$


## Translate fields into a macroscopic response

The next question is how fields become a physical boundary description. Define the jumps and averages on the two sides of the sheet. The GSTCs connect those jumps to electric and magnetic surface polarizations, including tangential gradients of normal polarizations. Neglecting the normal terms is an additional model assumption; small thickness alone does not justify it. The simple constitutive relations below also omit magnetoelectric coupling.

For a grounded reflective surface, a scalar impedance model is convenient. Fix an outward normal from the load into the incident region and use the associated tangential field orientation. At normal incidence, the impedance/reflection relation below provides an engineering test. A purely electric transmissive sheet may be modeled by a surface admittance acting on the average tangential electric field.

A passive local scalar load has nonnegative resistance; a reactive load is lossless. Negative resistance in this local load model requires power supplied to the port. For a spatially nonlocal surface, lateral power redistribution can invalidate a pointwise load interpretation, so global passivity is the decisive test. Large-angle transformations may require nonlocal transport, auxiliary evanescent fields, or an efficiency compromise.


$$
\Delta\mathbf E_t=\mathbf E_t^+-\mathbf E_t^-,\quad
\Delta\mathbf H_t=\mathbf H_t^+-\mathbf H_t^-,\quad
\mathbf E_{t,\rm av}=\frac{\mathbf E_t^++\mathbf E_t^-}{2},\quad
\mathbf H_{t,\rm av}=\frac{\mathbf H_t^++\mathbf H_t^-}{2}.
$$
$$
\hat{\mathbf z}\times\Delta\mathbf H
=i\omega\mathbf P_{s,t}-\hat{\mathbf z}\times\nabla_t M_{s,z},
\qquad
\Delta\mathbf E\times\hat{\mathbf z}
=i\omega\mu_0\mathbf M_{s,t}-\nabla_t(P_{s,z}/\epsilon_0)\times\hat{\mathbf z}.
$$
$$
\mathbf P_{s,t}=\epsilon_0\overline{\overline\chi}_{ee}\mathbf E_{t,\rm av},\qquad
\mathbf M_{s,t}=\overline{\overline\chi}_{mm}\mathbf H_{t,\rm av}.
$$
$$
Z_s=\eta_0\frac{1+\Gamma}{1-\Gamma},\qquad
\Gamma=\frac{Z_s-\eta_0}{Z_s+\eta_0},\qquad\operatorname{Re}Z_s\ge0.
$$
$$
\hat{\mathbf z}\times\Delta\mathbf H_t=Y_s\mathbf E_{t,\rm av}.
$$


:::{admonition} Worked exercise 1
:class: tip
For a grounded one-port surface at normal incidence, use $\eta_0\simeq377\,\Omega$ and $\Gamma_A=i$, $\Gamma_B=0.5$, $\Gamma_C=1.5$. Find each impedance and classify its local load as lossless reactive, passive lossy, or active. Why is amplitude above one incompatible with a passive isolated one-port? What changes for phase-only reflection?

```{dropdown} Show the answer

$$
Z_A=377\frac{1+i}{1-i}=377\frac{(1+i)^2}{2}=i377\,\Omega,
\quad Z_B=377\frac{1.5}{0.5}=1131\,\Omega,
\quad Z_C=377\frac{2.5}{-0.5}=-1885\,\Omega.
$$
$$
R_B=0.5^2=0.25,\quad A_B=0.75,\qquad R_C=1.5^2=2.25,
\qquad \Gamma=|\Gamma|e^{i\psi},\quad |\Gamma|=1\ \text{(lossless one-port)}.
$$


A is reactive and lossless. B is passive and dissipative: 25% is reflected and 75% absorbed. C would reflect 225% of the incident power and requires supplied energy. A phase-only profile holds the magnitude constant; an ideal lossless one-port has unit magnitude. These conclusions assume the stated isolated scalar one-port, not an arbitrary local field ratio on a nonlocal surface.
```
:::


## Phase calibration and physical cell placement

Now connect the wave mathematics to a real metal patch or dielectric element. The locally periodic approximation replaces the actual neighborhood by identical copies. Slowly changing dimensions are a useful heuristic, not a sufficient accuracy criterion. A unit-cell simulation uses phase-linked lateral boundaries and modal ports in the exterior.

Sweep patch length $L$ at fixed period $p$, substrate thickness $h$ and permittivity. Record complex $S_{11}$ or $S_{21}$, magnitude and signed argument. Useful coverage must be evaluated at an amplitude threshold, with adequate sampling near a rapid phase variation. Sensitivity to fabrication follows the phase derivative with respect to geometry. The source mentions roughly 280–300 degrees for one thin single-resonance patch design, and suggests thicker substrates, coupled resonators such as dual rings or Jerusalem crosses, and multilayer stacks. Those numbers and layer spacings are design examples, not guarantees of full phase coverage and high transmission.

Sample the desired aperture; compute its target; choose geometry from the LUT using circular phase error; then verify the complete structure. A phase-lag target must be negated before comparing with a library of signed arguments. Mutual coupling, finite pitch, finite phase states, incidence angle and fabrication all matter. A small focal ratio raises the range of local ray angles, but does not by itself change the incident angle of a normally incident plane wave. Include the appropriate incident and outgoing conditions in the library or an improved model.


$$
S_{11}(L)=|S_{11}(L)|e^{i\psi(L)},\qquad\psi(L)=\arg S_{11}(L).
$$
$$
\delta\psi\simeq\frac{d\psi}{dL}\delta L,\qquad
e_\psi=\arg\left(S\,e^{-i\psi_{\rm target}}\right),\qquad
\psi_{\rm target}=-\Phi_{\rm target}.
$$


:::{admonition} Worked exercise 1
:class: tip
The calibration phases are $[0,45,90,135,180,225,270,315]^\circ$, at patch lengths $[1.0,1.4,1.8,2.2,2.6,3.0,3.4,3.8]\,\mathrm{mm}$. For requested signed phases $[20,70,130,185,240,290,340,15]^\circ$, select the nearest states, dimensions, wrapped errors and mean absolute error. Why may the real array differ, and what final check is needed?

```{dropdown} Show the answer

$$
\psi_{\rm sel}=[0,90,135,180,225,270,0,0]^\circ,
$$
$$
L=[1.0,1.8,2.2,2.6,3.0,3.4,1.0,1.0]\,\mathrm{mm}.
$$
$$
e=\operatorname{wrap}(\psi_{\rm sel}-\psi_{\rm req})
=[-20,20,5,-5,-15,-20,20,-15]^\circ,
\qquad\overline{|e|}=\frac{20+20+5+5+15+20+20+15}{8}=15^\circ.
$$


Compare circular distances, not ordinary subtraction. In particular, 340 degrees is only 20 degrees from zero. Coupling, incidence-angle changes, phase discretization and fabrication perturb the result. Verify the full array: main-beam angle, sidelobes and grating lobes, reflected power/efficiency and actual phase profile. A near-field map is also needed to assess a focus.
```
:::


## Amplitude synthesis and power management

Phase is only half the story. Low sidelobes, Taylor or Chebyshev tapering, and holography require amplitude control. For a passive, power-normalized two-channel model, reflected power, transmitted power and absorption sum to one. If diffraction or polarization conversion opens extra ports, include them in the sum.

There are three routes to a smaller selected amplitude: dissipate energy using resistive loading; redirect it between reflection and transmission; or convert it into the orthogonal polarization. Resistive sheets or lumped resistors make the design convenient but heat the material. A lossless splitter redirects power rather than losing it. An ideal rotated half-wave plate produces a co-polarized linear amplitude proportional to $\cos2\theta$ and a cross-polarized amplitude proportional to $\sin2\theta$; a sign change also changes phase.

Changing one patch dimension generally changes amplitude and phase together. Two geometric coordinates, for example length and slot width, provide more freedom but do not guarantee independence. Build a two-dimensional complex-response library and minimize an amplitude/phase error with a wrapped phase difference. Check feasibility and coupling in the final device.


$$
|S_{11}|^2+|S_{21}|^2+A=1,\qquad A\ge0.
$$
$$
\mathcal E(L,W)=w_A\left(|S_{21}(L,W)|-|S_{21,\rm target}|\right)^2
+w_\psi\left[\arg\left(e^{i(\arg S_{21}-\psi_{\rm target})}\right)\right]^2,
\quad (L_{mn},W_{mn})=\operatorname*{arg\,min}_{L,W}\mathcal E.
$$


:::{admonition} Worked exercise 1
:class: tip
A lossless cell has $|S_{11}|=0.6$. Find its transmission amplitude and power. The target amplitudes at three positions are $[0.8,0.6,0.3]$ with signed target phases $[30,120,210]^\circ$. What reflection amplitude supports transmission 0.3 without loss? Why use two geometric variables, and how would you select them? Finally compute absorption for $|S_{11}|=0.5$, $|S_{21}|=0.4$.

```{dropdown} Show the answer

$$
|S_{21}|=\sqrt{1-0.6^2}=0.8,\qquad T=0.64,\quad R=0.36.
$$
$$
|S_{11}|=\sqrt{1-0.3^2}=\sqrt{0.91}\simeq0.954,\qquad T=0.09,\quad R=0.91.
$$
$$
A=1-0.5^2-0.4^2=1-0.25-0.16=0.59.
$$


The original cell provides the target amplitude 0.8, but its phase must also be checked. Transmission amplitude 0.3 leaves 91% reflected power. Sweep both length and slot width, save complex responses, compare amplitude and circular phase error, choose a feasible pair and verify the full array. One variable usually changes both amplitude and phase, so it does not supply independent control. Resistive loading converts 59% of input power into heat in the final example.
```
:::


## Polarization synthesis and geometric phase

Instead of changing the resonator dimensions, rotate an anisotropic cell. In its principal axes, its Jones matrix is diagonal. Specify the rotation matrix and circular basis explicitly: handedness names depend on time convention and viewing direction. With the basis and coordinate rotation below, the converted channel gains a signed geometric phase $-2\sigma\theta$. This geometric factor is independent of frequency; the dynamic phase, amplitudes and conversion efficiency generally are not.

For a half-wave response, $t_u=-t_v$ cancels the co-polarized circular channel. Near-unity conversion additionally requires near-unit transmission in both principal axes with consistent power normalization. A quarter-wave element with equal amplitudes, 90-degree retardance and equal incident components can convert linear to circular polarization. A rotated half-wave plate maps a linear input angle $\alpha$ to $2\theta-\alpha$. Geometric phase does not eliminate bandwidth limits or fabrication sensitivity.


$$
J_0=\begin{pmatrix}t_u&0\\0&t_v\end{pmatrix},\qquad
R(\theta)=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix},\qquad
J(\theta)=R(\theta)J_0R(-\theta).
$$
$$
\mathbf e_\sigma=\frac1{\sqrt2}\begin{pmatrix}1\\i\sigma\end{pmatrix},\qquad
J(\theta)\mathbf e_\sigma
=\frac{t_u+t_v}{2}\mathbf e_\sigma
+\frac{t_u-t_v}{2}e^{-2i\sigma\theta}\mathbf e_{-\sigma}.
$$
$$
\psi_{\rm PB}=-2\sigma\theta,\qquad t_u=-t_v,\qquad
\alpha_{\rm out}=2\theta-\alpha\pmod\pi.
$$


:::{admonition} Worked exercise 1
:class: tip
Find the converted-channel PB phase for $\sigma=+1$ and $\theta=30^\circ$.

```{dropdown} Show the answer
$$\psi_{\rm PB}=-2\sigma\theta=-2(+1)(30^\circ)=-60^\circ.$$

Use the explicitly defined circular basis and rotation convention.
```
:::


:::{admonition} Worked exercise 2
:class: tip
For $\sigma=-1$, what rotation gives a PB phase of $140^\circ$?

```{dropdown} Show the answer
$$140^\circ=-2(-1)\theta=2\theta\quad\Longrightarrow\quad\theta=70^\circ.$$

The result is understood modulo a half-turn for the element orientation.
```
:::


:::{admonition} Worked exercise 3
:class: tip
What cancels the co-polarized circular component?

```{dropdown} Show the answer
$$\frac{t_u+t_v}{2}=0\quad\Longleftrightarrow\quad t_u=-t_v.$$

Equal principal-axis amplitudes with a pi phase difference cancel the sum.
```
:::


:::{admonition} Worked exercise 4
:class: tip
A half-wave element has input angle $\alpha=20^\circ$ and axis angle $\theta=40^\circ$. Find the output angle.

```{dropdown} Show the answer
$$\alpha_{\rm out}=2\theta-\alpha=2(40^\circ)-20^\circ=60^\circ.$$

Angles use the same orientation convention; linear orientation is modulo 180 degrees.
```
:::


:::{admonition} Worked exercise 5
:class: tip
If both principal-axis amplitudes are 0.95 with a pi phase difference, is co-polarization cancelled? Is conversion 100%?

```{dropdown} Show the answer
$$t_u=-t_v,\qquad\eta_{\rm conv}=|t_u|^2=0.95^2=0.9025.$$

The sum cancels ideally, but incident-normalized converted power is 90.25% for equal exterior admittances. The remaining power must be accounted for in reflection or loss.
```
:::


The matrix above uses clockwise-positive coordinate angles. Measure both linear angles clockwise as well, with input vector $(\cos\alpha,-\sin\alpha)^T$, to use the stated $2\theta-\alpha$ rule. Using counterclockwise physical angles changes the rotation and PB signs together.

## Optimization and inverse design

Trial-and-error geometry tuning becomes expensive for multiband, multi-angle or multifunctional targets. Define a parameter vector and a constrained cost: field mismatch, efficiency penalty and fabrication rules. Scale the terms so their weights have an interpretable meaning.

For differentiable continuous designs, gradient methods are useful but do not guarantee a global optimum. An adjoint method avoids perturbing each pixel separately: solve the forward system, solve an objective-dependent adjoint system, and combine the fields to obtain sensitivities. The often quoted two solves apply to a single scalar objective and excitation/frequency condition; multiple conditions can require more solves. The exact signs, conjugations and prefactors depend on the chosen operator and real-valued objective.

Genetic algorithms use populations, crossover and mutation and are useful for discrete patterns; PSO moves particles using personal and group best locations. They can be expensive and provide no global guarantee. A trained forward surrogate predicts response from geometry. A tandem inverse network evaluates its proposed geometry through a frozen forward model: this addresses conflicting inverse labels but does not remove physical nonuniqueness or surrogate error. GANs and VAEs can propose freeform candidates; neither guarantees optimal bandwidth or efficiency. Finish every route with independent electromagnetic and fabrication checks, including coupling.


$$
\mathbf p=[p_1,\ldots,p_N]^T,\qquad
\min_{\mathbf p}\mathcal L(\mathbf p)
\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$
$$
\mathcal L=w_1\int_\Omega|E_{\rm sim}(\mathbf p,\mathbf r)-E_{\rm target}(\mathbf r)|^2\,d\mathbf r
+w_2(1-\eta_{\rm eff})+\operatorname{Penalty}(\mathbf p).
$$
$$
A(\mathbf p)u=b,\qquad A^\dagger\lambda=g,
\qquad
\frac{d\mathcal L}{dp_j}=-2\operatorname{Re}\left[\lambda^\dagger\frac{\partial A}{\partial p_j}u\right]
+\left.\frac{\partial\mathcal L}{\partial p_j}\right|_u.
$$


:::{admonition} Worked exercise 1
:class: tip
How do direct and inverse design differ?

```{dropdown} Show the answer


Direct design starts from geometry and evaluates its response; inverse design starts from a target and searches for feasible geometry.
```
:::


:::{admonition} Worked exercise 2
:class: tip
Write the geometric parameter vector for length, width and thickness.

```{dropdown} Show the answer
$$\mathbf p=[L,W,h]^T.$$

Each component must have a specified unit and bound.
```
:::


:::{admonition} Worked exercise 3
:class: tip
Formulate bounded inverse design.

```{dropdown} Show the answer
$$\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.$$

Minimize mismatch while respecting geometric bounds and fabrication requirements.
```
:::


:::{admonition} Worked exercise 4
:class: tip
What does a cost function measure?

```{dropdown} Show the answer
$$\mathcal L_{\rm field}=\int_\Omega|E_{\rm sim}-E_{\rm target}|^2\,d\mathbf r.$$

Mismatch between simulated and desired responses, possibly augmented by efficiency and fabrication terms.
```
:::


:::{admonition} Worked exercise 5
:class: tip
What do the weights do?

```{dropdown} Show the answer
$$\mathcal L=w_1\mathcal L_{\rm field}+w_2(1-\eta).$$

They set the relative priorities after the terms are appropriately scaled. Increasing the efficiency weight favors efficiency relative to field error.
```
:::


:::{admonition} Worked exercise 6
:class: tip
Why include a fabrication penalty?

```{dropdown} Show the answer
$$\mathcal L_{\rm total}=\mathcal L_{\rm error}+\operatorname{Penalty}.$$

It penalizes violations such as gaps or traces below the process minimum. Check hard constraints separately when a violation is unacceptable.
```
:::


:::{admonition} Worked exercise 7
:class: tip
Compare GA and PSO.

```{dropdown} Show the answer


GA evolves populations using crossover and mutation; PSO moves particles using personal and group bests. GA often suits binary patterns, while PSO commonly searches continuous dimensions.
```
:::


:::{admonition} Worked exercise 8
:class: tip
What are the input and output of a forward neural surrogate?

```{dropdown} Show the answer
$$[L,W]\ \longmapsto\ S_{21}\quad\text{or}\quad(|S_{21}|,\arg S_{21}).$$

Geometry goes in; complex scattering or amplitude and phase come out. Its accuracy is limited to the validated domain.
```
:::


:::{admonition} Worked exercise 9
:class: tip
Suggest methods for a continuous patch, a binary pattern and fast prediction after training.

```{dropdown} Show the answer


A gradient method or PSO; a genetic algorithm; and a forward surrogate, respectively. Method choice also depends on cost, differentiability and constraints.
```
:::


:::{admonition} Worked exercise 10
:class: tip
Calculate the cost for field error 0.1, efficiency 0.8, and weights 2 and 1.

```{dropdown} Show the answer
$$\mathcal L=2(0.1)+1(1-0.8)=0.2+0.2=0.4.$$

The weighted field mismatch and efficiency penalty each contribute 0.2.
```
:::


:::{admonition} Worked exercise 11
:class: tip
List three stages of simulation-based inverse design.

```{dropdown} Show the answer


Define target, cost and constraints; search the design space; independently validate the final geometry including coupling and fabrication.
```
:::


For this adjoint expression, the source vector is fixed and the state differential is defined by the following equation.

$$\left.d\mathcal L\right|_{\mathbf p}=2\operatorname{Re}(g^\dagger du).$$
