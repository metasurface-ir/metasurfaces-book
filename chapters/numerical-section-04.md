---
title: "6.4 Retrieve bulk and sheet parameters"
---

# 6.4 Retrieve bulk and sheet parameters

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
