---
title: "4.10 Floquet analysis and generalized Snell law"
---

# 4.10 Floquet analysis and generalized Snell law

For a phase-lag profile $\Phi(x)$, generalized Snell law takes the form below. A linear profile $\Phi(x)=\beta_s x$ adds a tangential wavevector $\beta_s$. Floquet analysis instead supplies the discrete reciprocal-lattice increments. They are two views of tangential momentum change: a continuous phase-profile description and the discrete channels of a periodic lattice. For a repeated phase ramp, the complete complex transmission must repeat; a ramp changing by $2\pi q$ over a superperiod selects the corresponding nominal order. Neither description determines coupling efficiency.


$$
n_2\sin\theta_t-n_1\sin\theta_i
=\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx},\qquad t(x)=A(x)e^{-i\Phi(x)}.
$$
$$
\Phi(x)=\beta_sx,\qquad\Delta k_x=\beta_s,
\qquad\Delta k_{x,m}=\frac{2\pi m}{p}.
$$


:::{admonition} Worked exercise: oblique illumination
:class: tip
A one-dimensional free-space lattice has $p=25\,\mathrm{mm}$ at $10\,\mathrm{GHz}$ and incident angle $20^\circ$. Calculate the incident wavevector, adjacent-cell phase lag, wavevectors and propagation status for orders $0,+1,-1$, their real angles, and whether a grating-lobe channel is open.

```{dropdown} Show the worked answer

$$
\lambda_0=\frac{3\times10^8}{10\times10^9}=0.03\,\mathrm m,
\quad k_0=\frac{2\pi}{0.03}\simeq209.44\,\mathrm{rad/m}.
$$
$$
k_x=k_0\sin20^\circ\simeq71.63\,\mathrm{rad/m},\qquad
\Delta\phi=k_x(0.025)\simeq1.7908\,\mathrm{rad}\simeq102.606^\circ.
$$
$$
G=\frac{2\pi}{0.025}\simeq251.33\,\mathrm{rad/m},\qquad
\begin{aligned}
k_{x,0}&\simeq71.63\,\mathrm{rad/m},\\
k_{x,+1}&\simeq322.96\,\mathrm{rad/m},\\
k_{x,-1}&\simeq-179.69\,\mathrm{rad/m}.
\end{aligned}
$$
$$
|k_{x,0}|<k_0,\qquad |k_{x,+1}|>k_0,\qquad |k_{x,-1}|<k_0.
$$
$$
\sin\theta_m=\sin20^\circ+\frac{30m}{25},\qquad
\theta_0=20^\circ,\quad\theta_{-1}\simeq-59.09^\circ,
\quad\sin\theta_{+1}\simeq1.542>1.
$$

The zero and negative-first orders propagate; the positive-first order is evanescent. The negative angle places the latter propagating beam on the negative-x side. A grating-lobe pathway is open at approximately $-59.1^\circ$; its power requires a scattering calculation. The source rounds $k_x$ to $71.62$ and obtains $322.95$ and $-179.71$; the values above keep more digits. For a physical Floquet translation, the signed phase shift is $-102.606^\circ$.
```
:::

