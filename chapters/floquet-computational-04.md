---
title: "Derive the Floquet orders"
---

(ch04-section-04)=
# Derive the Floquet orders

Expand the periodic factor in a Fourier series:

$$
u(x,z)=\sum_{m=-\infty}^{\infty}u_m(z)e^{-imGx}.
$$

Substituting gives

$$
E(x,z)=\sum_m u_m(z)e^{-ik_{x,m}x},\qquad
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
Suppose the actual primitive period is $p$ and the computational period is $\Lambda=Np$. The periodic field factor $u=e^{+ik_{x,i}x}E$ then has period $p$. Split its supercell Fourier integral into $N$ identical intervals:

$$
u_m=\frac{1}{Np}\int_0^{Np}u(x)e^{+i2\pi mx/(Np)}\,dx
=\frac{1}{Np}\int_0^p u(\xi)e^{+i2\pi m\xi/(Np)}\,d\xi
\sum_{j=0}^{N-1}e^{+i2\pi mj/N}.
$$

For integer $m$, the finite sum is a roots-of-unity sum:

$$
\sum_{j=0}^{N-1}e^{+i2\pi mj/N}
=\begin{cases}N,&m=N\ell,\quad\ell\in\mathbb Z,\\0,&m\notin N\mathbb Z.\end{cases}
$$

When the ratio is not one, the geometric-series numerator is $1-e^{+i2\pi m}=0$; when it is one, add $N$ ones directly. Therefore six identical cells allow nonzero supercell coefficients only at $m=6\ell$. The statement concerns the solved field's symmetry; it does not assume isolated, uncoupled elements.

The [cell-versus-supercell lab](../labs/10-coupling-lab.md) tests this extinction with an executed TE solver using a different geometry ($p=0.65\,\mu\mathrm m$, $N=6$). Its uniform-array control compares the same physical harmonic cutoff in primitive-cell and supercell calculations. The six unequal elements in the opening puzzle do not have this smaller translation symmetry.
:::
