---
title: 'Chapter 2: Nine Worked Examples'
short_title: Waves worked examples
---

# Chapter 2: Nine Worked Examples

**Question:** which simple calculation would expose a wrong sign, a wrong normalization, or an unsupported physical interpretation?

These examples accompany the [chapter](02-waves-and-interfaces.md), [browser/notebook lab](../labs/02-waves-lab.md), and [self-check](02-waves-review.md). They use $e^{-i\omega t}$, spatial $e^{i\mathbf k\cdot\mathbf r}$, peak electric amplitudes, and positive real nonmagnetic bulk indices. Predict the sign or limiting behavior before reading each calculation.

## 1. Find the magnetic-field sign

A plane wave propagates along positive $z$ in air, with electric phasor $\widetilde{\mathbf E}=E_0\widehat{\mathbf y}e^{ik_0z}$. Maxwell's relation gives

$$
\widetilde{\mathbf H}=\frac{1}{\eta_0}\widehat{\mathbf z}\times\widetilde{\mathbf E}
=-\frac{E_0}{\eta_0}\widehat{\mathbf x}e^{ik_0z}.
$$

Thus $\mathbf E\times\mathbf H^*$ points along positive $z$, as required. Reverse the wavevector while keeping electric polarization along the same $y$ direction: the magnetic field reverses, and the power flux points along negative $z$.

**Check:** an implementation using the same electric-to-magnetic sign for both propagation directions will give the wrong boundary equation. This is the physical origin of $Y_i(1-r)$ rather than $Y_i(1+r)$.

## 2. Can a passive interface give t = 1.2?

At normal incidence from glass $(n_i=1.5)$ to air $(n_t=1)$,

$$
r=\frac{1.5-1}{1.5+1}=0.2,\qquad
t=\frac{2(1.5)}{1.5+1}=1.2.
$$

The powers are

$$
R=0.04,\qquad T=\frac{1}{1.5}(1.2)^2=0.96.
$$

There is no gain: the electric field has a different power weighting in the two media. Reversing the illumination gives $r=-0.2$ and $t=0.8$, but the transmitted power remains 0.96. The power-normalized transmission amplitude is $\tau=\sqrt{0.96}\approx0.97980$ in either direction.

**Prediction to retain:** a field coefficient and a power-normalized S parameter can be different numbers without disagreeing physically.

## 3. Make only one polarization reflectionless

For air to glass,

$$
\theta_B=\arctan(1.5)\approx56.3099^\circ.
$$

At this angle, $\cos\theta_i=2/\sqrt{13}$ and $\cos\theta_t=3/\sqrt{13}$. The TM admittances agree:

$$
Y_i^{\mathrm{TM}}=\frac{1}{\cos\theta_i}=\frac{\sqrt{13}}2,
\qquad Y_t^{\mathrm{TM}}=\frac{1.5}{\cos\theta_t}=\frac{\sqrt{13}}2.
$$

Therefore $r_{\mathrm{TM}}=0$. For TE,

$$
r_{\mathrm{TE}}=-\frac5{13},\qquad R_{\mathrm{TE}}=\frac{25}{169}\approx0.14793.
$$

This calculation uses the common tangential-electric basis. A conventional reflected $p$-unit-vector coefficient may have the opposite sign from our TM coefficient, while its zero and power agree. Brewster matching is a polarization-specific condition, rather than a universal reflectionless interface.

## 4. A field beyond total reflection

Take glass to air at $\theta_i=45^\circ$ and $\lambda_0=0.6\,\mu\mathrm m$. The critical angle is $\arcsin(1/1.5)\approx41.8103^\circ$, so transmission is evanescent. Here

$$
q_i=\frac3{\sqrt8},\qquad q_t=\frac{i}{\sqrt8}.
$$

For TE,

$$
r=\frac{3-i}{3+i}=0.8-0.6i,\qquad t=1+r=1.8-0.6i.
$$

The transmitted amplitude is nonzero, yet $T=0$ because $\operatorname{Re}Y_t=0$. Meanwhile $R=|r|^2=1$. Its amplitude decay length is

$$
\ell_E=\frac{1}{k_0/\sqrt8}=\frac{\sqrt8\lambda_0}{2\pi}\approx0.2701\,\mu\mathrm m.
$$

At $z=\ell_E$, the electric amplitude is reduced by $e^{-1}$; intensity is reduced by $e^{-2}$. There is no distant transmitted beam in this semi-infinite lossless problem. Another interface within the decay region would define a different experiment.

## 5. Turn a line into a circle

Start with $\mathbf j_{\mathrm{in}}=(1,1)^T/\sqrt2$. Apply the ideal retarder $J=\operatorname{diag}(1,i)$:

$$
\mathbf j_{\mathrm{out}}=\frac1{\sqrt2}\begin{bmatrix}1\\i\end{bmatrix}.
$$

At a fixed $z=0$, its physical field has $E_x=\cos\omega t/\sqrt2$ and $E_y=\sin\omega t/\sqrt2$. Its tip moves from positive $E_x$ toward positive $E_y$. The norm stays one because $J^\dagger J=I$.

For a linear analyzer at any angle $\beta$,

$$
I_\beta=\frac12|\cos\beta+i\sin\beta|^2=\frac12.
$$

An analyzer therefore gives the same transmitted intensity for every angle, even though the incident field vector rotates in time. A global phase applied to both Jones components changes neither the polarization ellipse nor this intensity; a relative phase can change the ellipse.

## 6. Add material to remove reflection

Match air $(n_0=1)$ to glass $(n_2=1.5)$ at $\lambda_d=0.6\,\mu\mathrm m$ with an ideal constant-index film:

$$
n_f=\sqrt{1.5}\approx1.224745,\qquad
d=\frac{0.6}{4\sqrt{1.5}}\approx0.122474\,\mu\mathrm m.
$$

Then $\delta=\pi/2$, $r_{0f}=r_{f2}$, and the numerator of the film reflection coefficient is $r_{0f}-r_{f2}=0$. Thus $R=0$ and $T=1$. The transmitted electric coefficient at the film exit is

$$
t=i\sqrt{\frac{n_0}{n_2}}\approx0.816497i.
$$

Zero reflection does not imply unit electric amplitude or zero transmission phase. The phase above includes propagation from the entrance reference to the exit reference. The cancellation is exact for the stated ideal design condition; real dispersion and fabrication errors need their own study.

## 7. The reference plane

At one common plane in air, an absent sheet has $r=0,t=1$, so the electric-shunt retrieval gives $g=2(1-t)/t=0$. Now leave the incident reference fixed and move the output plane downstream by $\lambda_0/4$. The measured transmission becomes $t_{\mathrm{new}}=i$ through propagation alone.

Blindly inserting it into the same-plane shunt formula produces

$$
g_{\mathrm{wrong}}=\frac{2(1-i)}{i}=-2-2i.
$$

The apparent negative conductance would falsely suggest an active sheet in empty space. The continuity check already rejects this data interpretation: $i\ne1+0$. Removing the known propagation factor restores $t=1$. Deembedding is necessary here; it is not, by itself, evidence that an arbitrary finite structure is a local sheet.

## 8. Read a shunt and its uncertainty

For equal air ports and $g=2$,

$$
r=-\frac12,\quad t=\frac12,\quad R=T=\frac14,\quad A=\frac12.
$$

Inverting $t=1/2$ recovers $g=2$. In contrast, a purely reactive $g=2i$ gives $t=(1-i)/2$, $r=(-1-i)/2$, and $R=T=1/2$ with $A=0$. Reactive current changes scattering and stores/releases energy without net cycle-averaged dissipation in this ideal model.

For the inverse relation $g=2/t-2$, the sensitivity is

$$
\frac{dg}{dt}=-\frac2{t^2},\qquad
|\Delta g|\approx\frac{2|\Delta t|}{|t|^2}.
$$

Thus a fixed absolute uncertainty in the measured complex field can cause a large absolute parameter error near a transmission zero. At exactly zero the inverse is undefined. Good retrieval retains complex $r$ and $t$, verifies $t=1+r$ at the same plane, checks passivity, and tests another independent illumination or frequency before making a broader claim.

The notebook now makes this sensitivity test directly editable. Its controlled perturbation changes both coefficients consistently with the synthetic shunt relation; a separate printed continuity residual shows why independent measurement errors need their own model test. Compare the exact finite error with the derivative estimate, and report the ratio of perturbation magnitude to transmission. The approximation requires that ratio to be much smaller than one.

```{figure} ../assets/chapter-02/retrieval-conditioning.png
:alt: Exact inferred sheet-parameter error and the local derivative estimate as transmission decreases, with their ratio plotted against relative field perturbation.

Original deterministic sensitivity calculation from the analytical sheet inverse. A small absolute field error becomes a large parameter error near zero transmission. The local estimate loses validity when the perturbation is comparable to transmission; these are synthetic model-consistent perturbations, not measured uncertainty.
```

## 9. Absorb two beams with their phase

Keep $g=2$ and illuminate coherently from both sides with $\mathbf a=(1,e^{i\phi})^T/\sqrt2$. The input power is one. Multiplying by the equal-air scattering matrix gives

$$
b_1=\frac{-1+e^{i\phi}}{2\sqrt2},\qquad
b_2=\frac{1-e^{i\phi}}{2\sqrt2}.
$$

Then

$$
P_{\mathrm{out}}=|b_1|^2+|b_2|^2=\frac{1-\cos\phi}{2},\qquad
A=\frac{1+\cos\phi}{2}.
$$

Equal phase gives $A=1$; opposite phase gives $A=0$; a phase difference of $90^\circ$ gives $A=1/2$. The one-sided 50% bound has not been violated under its original assumptions: we changed the illumination. Add fields at each outgoing port before squaring, rather than adding the two separate one-sided power results and discarding interference.

This is an exact analytical prediction for the specified sheet and coherent inputs. Experiments would additionally need spatial-mode matching, phase control, calibration, and a material implementation. For the broader research context, see [Chong et al. on coherent perfect absorption](https://arxiv.org/abs/1003.4968).

## A teaching sequence

Use Examples 1–2 as a ten-minute diagnostic before introducing a numerical solver. Use 3–4 to test polarization and complex wavevectors; 5–6 to connect phase to observable changes; 7–8 to critique a retrieval; and 9 as a capstone prediction. Two moving arrows on paper can illustrate the outgoing complex-field sums before any calculation.

Continue with the [lab](../labs/02-waves-lab.md), then try the [self-check and mini-project](02-waves-review.md). The numerical notebook and browser are tools for checking a prediction, not substitutes for stating its assumptions.
