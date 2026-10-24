---
title: 'Chapter 4: Worked Examples and Learning Path'
short_title: Worked examples and teaching guide
---

# Chapter 4: Worked Examples and Learning Path

Read the [chapter](04-periodic-floquet.md), make predictions in the [browser explorer](../labs/04-floquet-lab.md), and then run the [notebook](../notebooks/04-floquet-orders.ipynb). This sequence connects physical intuition to calculations that can be inspected and changed.

## A suggested learning sequence

| Step | Activity | Evidence to retain |
| --- | --- | --- |
| Predict | Decide what repeats in the six-element example | A sketch labeling pitch and primitive period |
| Derive | Develop the Bloch phase and Floquet expansion | The boundary multiplier and tangential wavevector rule |
| Explore | Change wavelength, incidence, period, and output index | Channel sets, signed angles, and a cutoff prediction |
| Compute | Run the notebook from a fresh kernel | Automated analytical checks and exported figures |
| Interpret | Compare open channels, power normalization, and finite-array factors | An explanation of what each model establishes |
| Plan a solver study | Follow the full-wave lab outline | A geometry, port basis, convergence plan, and power ledger |

For a classroom session, use a repeated-symbol strip to identify the period, ask students to place equally spaced wavevector points between light-cone boundaries, and reveal the explorer's answer. A second session can address finite arrays, power normalization, and solver setup. These are teaching suggestions rather than a fixed assessment schedule.

## Example 1: six different elements

Let $p=0.5\,\mu\mathrm m$, $\Lambda=6p=3\,\mu\mathrm m$, and $\lambda_0=1.55\,\mu\mathrm m$. At normal incidence into air,

$$
q_m=m\frac{1.55}{3}\approx0.516667m.
$$

The strict open condition is $|q_m|<1$, giving $m=-1,0,+1$. Their angles are approximately $-31.11^\circ,0^\circ,+31.11^\circ$. The next orders have $|q_{\pm2}|\approx1.03333>1$, so they are evanescent in air.

If every element becomes identical, the smallest period can be $p=0.5\,\mu\mathrm m$. Then $\lambda_0/p=3.1$ and only the primitive zeroth order is open in air. A six-element *computational* cell still permits the old order labels, but smaller translation symmetry forces the extra coefficients to vanish.

**Check your reasoning:** the $3\,\mu\mathrm m$ channel map never established that either first order carries appreciable power. A scattering calculation is needed for that claim.

## Example 2: change the output medium

Keep the six-element geometry and normal incidence, but set $n_o=1.5$. The open condition becomes

$$
|m|<\frac{1.5(3)}{1.55}\approx2.90323.
$$

Orders $-2,-1,0,+1,+2$ are open. Their angles are approximately $-43.54^\circ,-20.15^\circ,0^\circ,+20.15^\circ,+43.54^\circ$. The same tangential momentum is divided by a larger exterior wavenumber, so the first-order angles shrink while additional orders become possible.

**Try next:** let $n_i\ne n_o$ and use oblique incidence. Explain why changing the incident index changes $q_i$, while changing only the output index changes the light-cone boundary.

## Example 3: oblique microwave incidence

Use $\lambda_0=30\,\mathrm{mm}$, $\Lambda=25\,\mathrm{mm}$, $n_i=n_o=1$, and $\theta_i=20^\circ$. The wavelength corresponds to 10 GHz using the rounded teaching value $c=3.00\times10^8\,\mathrm{m/s}$.

$$
q_i=\sin20^\circ\approx0.342020,\qquad
q_m=0.342020+1.2m.
$$

Thus $m=0$ has $q_0=0.342020$ and $\theta_0=20^\circ$. Order $m=-1$ has $q_{-1}\approx-0.857980$ and $\theta_{-1}\approx-59.09^\circ$. Order $m=+1$ has $q_{+1}\approx1.542020$ and is closed. All remaining integer orders are also closed.

The incident tangential wavevector is

$$
k_{x,i}=\frac{2\pi}{0.030}\sin20^\circ\approx71.63\,\mathrm{rad/m}.
$$

The field phase advance over one positive period is $k_{x,i}\Lambda\approx1.791\,\mathrm{rad}\approx102.61^\circ$. The complex multiplier is $e^{+i1.791}$ under our convention. Mapping in the reverse direction uses its inverse.

**Diagnostic:** reporting $m=+1$ as the open first order while keeping our stated equation would be a sign error. A solver using the opposite labeling convention can still describe the same physical beam if its wavevectors and labels are mapped explicitly.

## Example 4: opening a channel at cutoff

Take $\Lambda=0.8\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, $n_i=1$, and increase positive incidence. For $m=-1$,

$$
q_{-1}=\sin\theta_i-1.9375.
$$

The order first reaches the negative output light-cone boundary when

$$
\sin\theta_c=1.9375-n_o.
$$

For $n_o=1.5$, $\theta_c\approx25.94^\circ$. For air, $\theta_c\approx69.64^\circ$. At the exact threshold the order is grazing. Just below it the order is closed, and just above it the order is open. At $\theta_i=45^\circ$, the glass output supports $m=-1$ and $m=0$, whereas air supports only $m=0$.

The notebook tests points on both sides of the threshold using offsets larger than its numerical classification tolerance. A coarse angle grid can miss this change; an analytical cutoff is a useful independent check.

## Example 5: amplitude, power, and the flat-interface test

At normal incidence from $n_i=1$ to $n_t=1.5$, the TE electric-field amplitudes are $r=-0.2$ and $t=0.8$. The power fractions are

$$
R=0.04,\qquad T=\frac{n_t}{n_i}|t|^2=0.96.
$$

The power sum is one. The calculation $|r|^2+|t|^2=0.68$ mixes unnormalized field amplitudes with power fractions.

Now assign that flat interface an artificial $3\,\mu\mathrm m$ period at $\lambda_0=1.55\,\mu\mathrm m$. The air and glass channel maps list additional open orders, but a flat interface scatters only into the specular order. Continuous translational symmetry makes every other amplitude zero.

**Interpretation:** the channel map and the amplitude calculation answer different parts of the same physical problem. A correct channel map is necessary for power accounting, but does not supply its entries.

## Example 6: a scan-range spacing bound

Suppose $n_i=n_o=1$, $\lambda_0=1.55\,\mu\mathrm m$, and the full scan is $|\theta_i|\leq60^\circ$. A sufficient bound for keeping nonzero orders closed throughout the scan is

$$
\Lambda<\frac{1.55}{1+\sin60^\circ}\,\mu\mathrm m
\approx0.831\,\mu\mathrm m.
$$

The bound is stricter than the normal-incidence-only condition $\Lambda<1.55\,\mu\mathrm m$. Equality permits a grazing order at the edge of the scan. If the output index or wavelength changes, recalculate the bound rather than treating half-wavelength spacing as a universal rule.

## Example 7: a visible field without outward power

Use the outgoing-field figure in the chapter. Let $n_o=1$, $q_m=1.2$, and $\lambda_0=1.55\,\mu\mathrm m$. The channel is outside the light cone, so its outward normal wavenumber is imaginary:

$$
\alpha=\frac{2\pi}{1.55}\sqrt{1.2^2-1}\,\mu\mathrm m^{-1},\qquad
L_E=\frac1\alpha\approx0.3719\,\mu\mathrm m,\qquad
L_{|E|^2}=\frac1{2\alpha}\approx0.1860\,\mu\mathrm m.
$$

At $s=L_E$ the amplitude is $e^{-1}$ and its squared magnitude is $e^{-2}$. For this isolated TE harmonic, $\operatorname{Re}\kappa=0$, so the time-averaged normal flux is zero everywhere. The surface-parallel phase variation remains visible. On reflection, substitute $s=-z$; the outgoing field decays as you move to more negative laboratory $z$.

**Check visually:** choose a closed order in the browser and move the time-phase slider. The fringes move along the surface; the envelope and its decay length stay fixed. Explain why this pattern can matter in interface matching even though it contributes no outgoing normal power.

## Example 8: the width of a finite-array beam

For the reference air case, the positive first-order maximum is at $\theta_1\approx31.109^\circ$. Take $N=24$ equal prescribed sources with spacing $\Lambda=3\,\mu\mathrm m$ and $\lambda_0=1.55\,\mu\mathrm m$. The first nulls satisfy

$$
\sin\theta_{\rm null}=\frac{1.55}{3}\pm\frac{1.55}{24\cdot3},\qquad
\theta_{\rm null}\approx29.679^\circ,\ 32.561^\circ.
$$

The exact full width between these nulls is approximately $2.882^\circ$. Doubling $N$ halves their separation in sine-angle coordinates exactly and approximately halves the angular width away from grazing. The notebook compares the direct complex sum with the geometric-series expression and checks these zeros.

**Read the model:** these are array-factor nulls. An element radiation pattern, nonuniform illumination, coupling, or an actual Maxwell solution can change the full device pattern. Do not label this width as the measured beamwidth of the schematic ridges.

## Report checklist

Retain the conventions and units, primitive-period argument, parameters, order-enumeration bounds, cutoff tolerance, open-order sets, signed angles, and the notebook's analytical assertions. Discuss one case where an open order has zero amplitude and one reason why a closed order still matters in a solver.

For finite arrays, label the plotted quantity as a normalized scalar array factor. For a future full-wave report, add complex modal coefficients, incident-power normalization, all-channel power balance, and independent numerical refinements. An analytical angle alone does not validate a claimed efficiency.

## Connection to the rest of the course

[Chapter 3](03-unit-cell-design.md) uses these channels to compute and validate a dielectric TE unit-cell library. [Chapter 5](05-metasurface-synthesis.md) uses them to verify full-wave beam steering and develop wavefront models. [Chapter 6](06-numerical-methods.md) develops numerical convergence in more detail. [Chapter 10](10-ai-metasurfaces.md) needs a consistent channel basis when a learned model predicts a scattering response; adding or removing channels at cutoff can change both data representation and validation requirements.
