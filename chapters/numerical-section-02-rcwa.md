---
title: "6.2.5 RCWA: periodic fields in Fourier space"
---

# 6.2.5 RCWA: periodic fields in Fourier space

General volume/surface methods offer geometric flexibility but can require large meshes and long runs. Many metasurfaces have two useful features: periodicity in xy and layers along z. RCWA, associated with Moharam and Gaylord’s 1981 work and also called the Fourier modal method, exploits that structure.

Instead of sampling every point with a spatial mesh, expand materials and fields in Fourier series. The retained harmonics satisfy coupled propagation equations. “Rigorous” means a Maxwell solution for the stated model, with truncation and geometry approximations still requiring convergence.

## 1. Slice the structure

Each layer is invariant along z and may vary periodically in x,y. Sloped or curved profiles are approximated by multiple thin slices. Slice thickness and harmonic count are separate controls.

## 2. Expand material and apply the correct factorization

$$
\epsilon_r(x,y)=\sum_{p=-P}^P\sum_{q=-Q}^Q\widetilde\epsilon_{pq}e^{i(pG_xx+qG_yy)},\qquad G_x=2\pi/\Lambda_x,\quad G_y=2\pi/\Lambda_y.
$$

The source’s material series uses a positive Fourier sign while its field basis below uses a negative sign. The material convolution must therefore use the corresponding reversed coefficient indices; one can equivalently reindex the material series.

Li’s factorization rules address products of discontinuous functions. In TM and high-contrast structures, simply multiplying truncated coefficient arrays can converge poorly. The inverse rule involves $[\epsilon^{-1}]^{-1}$ in the appropriate component relation; this is not generally the same finite matrix as $[\epsilon]$.

## 3. Expand the Bloch field

$$
\mathbf E(x,y,z)=\sum_{m=-M}^M\sum_{n=-N}^N\mathbf S_{mn}(z)e^{-i(k_{xm}x+k_{yn}y)},\quad k_{xm}=k_{x0}+2\pi m/\Lambda_x,\quad k_{yn}=k_{y0}+2\pi n/\Lambda_y.
$$

Each index pair identifies a diffraction order. Tangential derivatives become diagonal wavenumber matrices. Eliminating longitudinal components gives a coupled ordinary differential/eigenvalue problem:

$$
\partial_x\longrightarrow-iK_x,\quad\partial_y\longrightarrow-iK_y,\qquad\frac{d^2\mathbf S_t}{dz^2}=\Omega^2\mathbf S_t.
$$

With solutions proportional to exp(λz), imaginary λ describes lossless propagation and real λ an evanescent pair. In lossy media λ is generally complex; choose outgoing/decaying solutions consistently.

## 4. Couple layers stably

Transfer matrices can combine growing and decaying evanescent exponentials and become badly conditioned. Scattering matrices connect incoming to outgoing waves, and can be composed with the Redheffer star product.

$$
\begin{bmatrix}\mathbf c_{\rm out}^{+}\\\mathbf c_{\rm out}^{-}\end{bmatrix}=S\begin{bmatrix}\mathbf c_{\rm in}^{+}\\\mathbf c_{\rm in}^{-}\end{bmatrix},\qquad e^{+|\lambda|d}\ \text{versus}\ e^{-|\lambda|d}.
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
The source calls S-matrix coupling “100% stable and noise-free for infinitely many layers.” It greatly improves numerical conditioning, but finite precision, resonances, singular blocks, truncation and factorization still matter. It is not an unconditional stability guarantee.
:::

| Feature | RCWA | FEM | FDTD |
|---|---|---|---|
| Discretization | Fourier harmonics; layer slices if needed | Volume elements/edge fields | Staggered space/time grid |
| Periodicity | Built into Bloch basis | Paired boundary constraints | Periodic/Bloch grid boundaries |
| Curved/sloped geometry | May require many slices | Flexible fitted mesh | Staircasing or conformal treatment |
| Typical use | Periodic diffraction and libraries | Complex vector devices | Pulses and time evolution |
| Cost | Dense modal matrices grow with harmonic count | Mesh and linear solver dependent | Volume, time steps and duration dependent |

The source emphasizes rapid library generation, direct order-power outputs, and dielectric metasurface optimization, with an illustrative “two minutes versus 0.2 seconds” comparison. Timings are examples, not reproducible performance guarantees across geometries and tolerances. A converged calculation, not the solver’s name, determines usable accuracy.

:::{admonition} Worked problem
:class: tip
A one-dimensional air/air grating has $\Lambda=800\,\mathrm{nm}$ and illumination $\lambda_0=600\,\mathrm{nm}$, $\theta_i=30^\circ$. For $m=-2,-1,0,1,2$, calculate $k_{x,m}/k_0$, classify orders and give real outgoing angles. Why retain evanescent harmonics?

1. Calculate the normalized tangential wavenumbers.
2. Classify each order and calculate the real exit angles.
3. Explain why evanescent harmonics must be retained until convergence.

```{dropdown} Show the complete worked answer

$$
k_{x,m}=k_0\sin\theta_i+2\pi m/\Lambda,\qquad k_0=2\pi/\lambda_0.
$$

$$
\frac{k_{x,m}}{k_0}=\sin\theta_i+m\frac{\lambda_0}{\Lambda}=0.5+0.75m,\quad\sin30^\circ=0.5,\quad\frac{600}{800}=0.75.
$$

| m | Substitution | Normalized tangential wavenumber | Type | Angle |
|---|---|---|---|---|
| −2 | $0.5-1.5$ | −1 | Grazing threshold | $-90^\circ$ limit |
| −1 | $0.5-0.75$ | −0.25 | Propagating | $\arcsin(-0.25)\approx-14.48^\circ$ |
| 0 | $0.5$ | 0.50 | Propagating | $30^\circ$ |
| +1 | $0.5+0.75$ | 1.25 | Evanescent | No real angle |
| +2 | $0.5+1.5$ | 2.00 | Evanescent | No real angle |

$$
k_{z,m}^2=k_0^2-k_{x,m}^2,\qquad |k_{x,m}|<k_0:\ \text{propagating};\quad |k_{x,m}|>k_0:\ \text{evanescent};\quad |k_{x,m}|=k_0:\ k_{z,m}=0.
$$

Only −1 and 0 are ordinary power-carrying far-field orders in this list. At −2 the normal flux of an ideal finite-amplitude grazing wave is zero. Evanescent fields can still resolve edges and interfaces and couple into propagating harmonics. Increase retained harmonics until the actual order powers and phases converge, especially near the grazing threshold.

```
:::
