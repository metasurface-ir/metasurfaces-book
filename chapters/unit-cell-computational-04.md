---
title: "Channels, complex amplitudes, and power"
---

# Channels, complex amplitudes, and power

For retained integer orders $m=-M,\ldots,M$, define

$$
\alpha_m=\frac{k_{x,m}}{k_0}=n_i\sin\theta_i+m\frac{\lambda_0}{\Lambda},\qquad
q_{o,m}=\sqrt{n_o^2-\alpha_m^2}.
$$

The outgoing root has nonnegative real and nonpositive imaginary parts. A positive real $q$ gives a propagating channel; a negative imaginary $q$ gives outward decay. At exact cutoff $q=0$, this implementation requests a parameter perturbation rather than using a singular grazing basis.

The exterior expansions are

$$
E_y^{((-i))}(x,z)=e^{-ik_0(\alpha_0x+q_{i,0}z)}+
\sum_m r_m e^{-ik_0(\alpha_mx-q_{i,m}z)},\quad z<0,
$$

$$
E_y^{(t)}(x,z)=\sum_m t_m e^{-ik_0[\alpha_mx+q_{t,m}(z-h)]},\quad z>h.
$$

For these **electric-field** TE amplitudes, the order powers relative to incident normal flux are

$$
R_m=\frac{\operatorname{Re}q_{i,m}}{q_{i,0}}|r_m|^2,\qquad
T_m=\frac{\operatorname{Re}q_{t,m}}{q_{i,0}}|t_m|^2.
$$

Closed exterior orders have zero normal outgoing power in these lossless half-spaces. Sum every open order to obtain $R$ and $T$. For this lossless model, $R+T=1$ to numerical accuracy. With absorption in a more general solver, the missing fraction requires a consistent dissipated-power calculation.

At the library reference parameters, $\lambda_0/\Lambda\approx2.385$, exceeding both exterior indices. Only $m=0$ is open, so $T=1.5|t_0|^2$ and $R=|r_0|^2$. If period, wavelength, or angle changes, enumerate the channels again. A zeroth-order library becomes incomplete when other orders open.

For an open zeroth-order channel, the power-normalized coefficient is $S_{21}=\sqrt{q_{t,0}/q_{i,0}}\,t_0$. Record whether a solver exports this quantity or an electric-field ratio. Reciprocity comparisons require compatible normalization, channel directions, reference planes, and the appropriate reversal of transverse wavevectors.
