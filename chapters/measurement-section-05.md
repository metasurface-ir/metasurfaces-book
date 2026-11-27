# 9.5 Retrieving effective parameters from measurements

Instructor booklet, pages 265–270.

**Homogenization** replaces microstructure with an equivalent model. A bulk slab may be described by $\varepsilon_{\rm eff}$ and $\mu_{\rm eff}$. For a thin surface, an input impedance $Z_s$ or sheet admittance $Y_s$ can answer a better-posed question. VNA data give parameters for **the chosen model and reference plane**.

## 9.5.1 Slab model and the Nicholson–Ross–Weir method

For a symmetric homogeneous slab of thickness $d$ in identical media, with reference planes at its faces and normal single-mode incidence, let $\Gamma$ be the single-interface reflection and $T=e^{-ik_0n_{\rm eff}d}$ the one-way propagation factor. Summing internal reflections gives

$$
S_{11}=\frac{\Gamma(1-T^2)}{1-\Gamma^2 T^2},\qquad
S_{21}=\frac{T(1-\Gamma^2)}{1-\Gamma^2 T^2}.
$$

In this example $z_{\rm eff}$ is normalized to the surrounding air. The $S^2$ terms below are complex squares. For passive material, check propagation and continuity when selecting the root compatible with $\lvert\Gamma\rvert\le1$ and $\operatorname{Re}z_{\rm eff}\ge0$.

$$
X=\frac{S_{11}^{2}-S_{21}^{2}+1}{2S_{11}},\quad
\Gamma=X\pm\sqrt{X^2-1},\quad z_{\rm eff}=\frac{1+\Gamma}{1-\Gamma},\quad
T=\frac{S_{11}+S_{21}-\Gamma}{1-(S_{11}+S_{21})\Gamma}.
$$

Taking the logarithm introduces a **branch index**. Verify the sign by substitution into the definition of $T$. Then recover the relative slab properties.

$$
n_{\rm eff}=\frac{i\ln T}{k_0 d}
=\frac{-[\arg T+2\pi m]+i\ln\lvert T\rvert}{k_0d},\quad m\in\mathbb Z,\qquad
\varepsilon_{\rm eff}=\frac{n_{\rm eff}}{z_{\rm eff}},\quad
\mu_{\rm eff}=n_{\rm eff}z_{\rm eff}.
$$

Ambiguity follows **electrical thickness**. Phase continuity or group delay $\tau_g=-d\arg T/d\omega$ tracks changes but cannot determine a constant $2\pi$ offset. Start from a valid low-frequency limit or independent reference when available. Interpret $v_g=c/[n+\omega\,dn/d\omega]$ in the simple low-loss model. The condition $0<v_g<c$ is not a universal branch test. Near $S_{11}=0$, the form for $X$ is ill-conditioned. Use a stable formulation or fit and reconstruct the scattering data.

## 9.5.2 Grounded surfaces and transmitting sheets

A **grounded surface** at normal incidence has a closed transmission channel. Obtain **input impedance** from $\Gamma=S_{11}$ at the surface reference plane.

$$
S_{11}=\frac{Z_s-\eta_0}{Z_s+\eta_0},\qquad
Z_s=\eta_0\frac{1+S_{11}}{1-S_{11}}=R_s+iX_s.
$$

$R_s$ includes loss seen at this port. $X_s>0$ is inductive and $X_s<0$ capacitive. Zero reflection requires both $R_s=\eta_0$ and $X_s=0$. The formula $\phi_{\rm ref}=\pi-2\arctan(X_s/\eta_0)$ modulo $2\pi$ applies only when $R_s=0$.

For an **electric-only sheet** between identical air regions, tangential electric field is continuous and $t=1+r$. Surface current follows from the magnetic-field jump.

$$
Y_s=\frac{1-r-t}{\eta_0 t}=\frac{2}{\eta_0}\frac{1-t}{t},\qquad Z_s=\frac1{Y_s}.
$$

The factor of two appears only after substituting $r=t-1$. If $t=1+r$ fails beyond uncertainty, check calibration and reference planes before considering magnetic, coupled, or finite-thickness models.

## 9.5.3 Measurement error and fabrication tolerance

**Copper surface roughness** on the skin-depth scale can affect loss. The ratio $R_q/\delta_s$ alone does not determine a correction factor. **Permittivity tolerance** shifts resonance in the simple $f_0\propto1/\sqrt{\varepsilon_r}$ model. **Solder and pad parasitics** alter $L$, $C$, and cell phase. Report coupon averages and cell-to-cell variation separately.

$$
\frac{\Delta f_0}{f_0}\simeq-\frac12\frac{\Delta\varepsilon_r}{\varepsilon_r}.
$$

| Method | Target quantity | Scope |
| --- | --- | --- |
| NRW | $n_{\rm eff}$, $\varepsilon_{\rm eff}$, $\mu_{\rm eff}$ | Slab of specified thickness, with branch and reference checks |
| Surface impedance | $R_s$, $X_s$, and phase | Grounded thin surface, sensitive to reference plane |
| Waveguide | Modal $S_{11}$ and $S_{21}$ | Controlled fixture and small sample, for a specified geometry and mode |
| Calibrated free space | Reflection or transmission pattern | Variable angles, with alignment, echo reduction, and calibration |

## Worked problem on three models for three samples

::::{admonition} Try it first
:class: book-exercise

For normal incidence in air, slab A with $d=10\,\mathrm{mm}$ at $10\,\mathrm{GHz}$ has $S_{11}=0.28012+i0.13032$ and $S_{21}=-0.40447+i0.74749$. An independent propagation reference gives $-144^\circ$ at $6\,\mathrm{GHz}$. Phase decreases continuously to $10\,\mathrm{GHz}$, crossing $-180^\circ$ once. For grounded surface B at $28\,\mathrm{GHz}$, $S_{11}=-i0.50$ and $S_{21}\simeq0$. For sheet C at that frequency, $r=-0.40-i0.20$ and $t=0.60-i0.20$. Sample B has $\varepsilon_r=3.50\pm0.05$ and $Q_L=150$. With $\eta_0\simeq377\,\Omega$, retrieve each model and evaluate resonance sensitivity.

```{dropdown} Show the full worked answer

### 1. Slab A and branch selection

$$
X\simeq2.60,\quad \Gamma=2.60\pm2.40,\quad
\Gamma_{\rm passive}\simeq0.20,\quad z_{\rm eff}\simeq1.50,\quad
T\simeq-0.450+i0.7794.
$$

$\lvert T\rvert\simeq0.90$ and principal phase is $+120^\circ$. With $k_0d=2\pi/3$, using principal phase alone gives $n'\simeq-1$. The $-144^\circ$ anchor and decreasing phase require $m=-1$ and $\arg T+2\pi m=-240^\circ$.

$$
n_{\rm eff}\simeq2.00-i0.0503,\qquad
\varepsilon_{\rm eff}\simeq1.333-i0.0335,\qquad
\mu_{\rm eff}\simeq3.00-i0.0755.
$$

Both branches have the same $\lvert T\rvert$. The phase exceeds $180^\circ$ even at $d=\lambda_0/3$. Substitute back into the slab model to reconstruct $S_{11}$ and $S_{21}$. This checks the inversion. Test homogenization against additional frequencies, thicknesses, or angles.

### 2. Grounded surface B input impedance

$$
Z_s=377\frac{1-i0.50}{1+i0.50}
=377\frac{0.75-i1.00}{1.25}
=226.2-i301.6\,\Omega.
$$

The real part is positive and the reactance capacitive. This result includes patch, substrate, and ground. Since $R_s\ne0$, the lossless phase formula does not apply. With no other channels and zero transmission, $1-\lvert S_{11}\rvert^2=75\%$ is absorption. With diffraction or cross-polarization, this is the share not returned to the measured channel.

### 3. Sheet C admittance

The data satisfy $t=1+r$. For unit incident field, $J_s=(1-r-t)/\eta_0$ and sheet field is $t$. Thus

$$
\frac{1}{t}=\frac{0.60+i0.20}{0.60^2+0.20^2}=1.50+i0.50,\quad
Y_s=\frac{1+i}{377}\,\mathrm S\simeq(2.65+i2.65)\,\mathrm{mS},\quad
Z_s\simeq188.5-i188.5\,\Omega.
$$

This $Z_s$ is the ratio of field to current on the sheet itself. The grounded model describes the input seen at its own reference plane.

### 4. Resonance error budget

$$
\lvert\Delta f_0\rvert\simeq\frac{28\,\mathrm{GHz}}2\frac{0.05}{3.50}=200\,\mathrm{MHz},\qquad
\Delta f_{\rm res}\simeq\frac{28\,\mathrm{GHz}}{150}=187\,\mathrm{MHz}.
$$

Increasing permittivity lowers resonance. The estimated shift is comparable to the linewidth. If much of the field resides in air, the sensitivity can be lower. Determine it by a numerical sweep or measurement.

| Factor | Check |
| --- | --- |
| Reference plane | A $0.5\,\mathrm{mm}$ offset at $28\,\mathrm{GHz}$ gives about $33.6^\circ$ round-trip error. Check reference position first. |
| Copper roughness | $\delta_s\simeq0.40\,\mu\mathrm m$, so $1$ to $2\,\mu\mathrm m$ roughness is substantial. Assess loss independently. |
| Solder and pad parasitics | Measure several assembled coupons to distinguish systematic bias from cell-to-cell spread. |
```
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
