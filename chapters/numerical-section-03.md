---
title: "6.3 Periodic cells, Floquet ports and phase planes"
---

# 6.3 Periodic cells, Floquet ports and phase planes

A practical metasurface may contain thousands or millions of elements. Translational symmetry reduces an exactly repeated array to one cell. For a graded device, local periodicity is an additional approximation: replace each cell’s real neighbors by identical copies to build its response library.

Gentle geometric variation can make this useful, but strong unequal-cell coupling and sensitive resonances can invalidate it. Exact solution of periodic boundary conditions does not establish LPA validity for a nonuniform array.

## 1. Pair opposite faces with the Bloch phase

$$
\mathbf E(x+\Lambda_x,y,z)=\mathbf E(x,y,z)e^{-ik_{x0}\Lambda_x},\qquad\mathbf E(x,y+\Lambda_y,z)=\mathbf E(x,y,z)e^{-ik_{y0}\Lambda_y}.
$$

$$
k_{x0}=k_0\sin\theta\cos\varphi,\quad k_{y0}=k_0\sin\theta\sin\varphi.
$$

Normal incidence gives zero phase shift; oblique incidence does not. In software, pair the correct source/destination faces and map mesh or degrees of freedom with their orientations. The source mentions primary/secondary (formerly master/slave) in HFSS and Unit Cell boundaries in CST. Interface names are software-version dependent.

## 2. Floquet ports and channel accounting

A Floquet port excites/collects plane-wave harmonics rather than a metallic waveguide mode. Each spatial order supports polarization states; select the incident mode and retain every propagating outgoing channel, including converted polarization. Higher diffraction orders may open with frequency or angle.

$$
k_{xm}=k_{x0}+2\pi m/\Lambda_x,\quad k_{yn}=k_{y0}+2\pi n/\Lambda_y,\quad k_{z,mn}=\sqrt{k_0^2-k_{xm}^2-k_{yn}^2}.
$$

In air, a conservative no-higher-order condition over incidence angles up to the specified maximum is

$$
\Lambda_{x,y}<\frac{\lambda_0}{1+\sin\theta_{\max}}.
$$

This is a channel-opening condition, not a statement of reflectance or LPA accuracy. Recalculate it for other exterior refractive indices.

## 3. Deembed to the physical surface

The phase reported at a port contains travel through its air gap. Remove that known propagation to compare cells at the same physical plane. At oblique incidence the vertical separation uses the normal wavenumber, not the full free-space wavenumber.

$$
\phi_{\rm port}=\phi_{\rm surface}-2k_{z,00}d_{\rm port}\pmod{2\pi}.
$$

The source recommends separating the port from strong near fields and discusses quarter-/half-wavelength distances. Later it correctly explains that no fixed wavelength fraction is sufficient for every structure: near-cutoff evanescent fields can decay very slowly. Shift the port and increase retained modes independently until the desired complex response is stable.

| Setting | HFSS terminology in source | CST terminology in source | Physical check |
|---|---|---|---|
| Lateral pairing | Primary/secondary | Unit Cell | Paired Bloch phase |
| Excitation | Floquet port | Floquet expansion | Incoming wave and polarization |
| Angles | Scan angles | Scan/phase settings | Same tangential wavevector |
| Reference plane | Deembedding | Reference-plane distance | Complex coefficient at same surface |
| Mode count | Port-mode selection | Floquet-mode selection | All open channels plus refinement |

:::{admonition} Worked problem
:class: tip
A square cell has $\Lambda_x=\Lambda_y=10\,\mathrm{mm}$ at $f=10\,\mathrm{GHz}$. Air-side illumination is at $\theta=30^\circ,\varphi=0$, with +z upward. The port lies 10 mm above the surface and reports reflection phase −110°.

1. Explain LPA and a failure scenario.
2. Find wavelength, tangential wavenumbers and paired-face phases.
3. Classify (0,0), (−1,0), (+1,0), (0,+1), and determine whether any other air-side order is open.
4. Check the conservative period bound up to 30° and explain what it guarantees.
5. Choose port modes and discuss port distance.
6. Calculate the surface reflection phase using the given deembedding relation.
7. Give a logical setup sequence.

```{dropdown} Show the complete worked answer

LPA replaces the slowly varying neighborhood by an infinite identical array; abrupt changes, resonance and unequal-cell coupling can defeat it. Now calculate the wave quantities:

$$
\lambda_0=\frac{3\times10^8}{10\times10^9}=0.03\,\mathrm m=30\,\mathrm{mm},\qquad k_0=\frac{2\pi}{30}=\frac\pi{15}\,\mathrm{rad/mm}.
$$

$$
k_{x0}=\frac\pi{15}\sin30^\circ\cos0=\frac\pi{30}\,\mathrm{rad/mm},\qquad k_{y0}=0.
$$

$$
k_{x0}\Lambda_x=\frac\pi{30}(10)=\frac\pi3=60^\circ,\qquad E(x+\Lambda_x,y,z)=E(x,y,z)e^{-i60^\circ},\quad E(x,y+\Lambda_y,z)=E(x,y,z).
$$

The x-paired field lags by 60°; the y pair has no phase difference. Respect the mapping direction and edge orientation.

$$
\frac{k_{xm}}{k_0}=0.5+3m,\qquad\frac{k_{yn}}{k_0}=3n,\qquad(k_{xm}/k_0)^2+(k_{yn}/k_0)^2<1\quad\text{for an open air channel}.
$$

| Order | $k_x/k_0$ | $k_y/k_0$ | Squared sum | Result |
|---|---|---|---|---|
| $(0,0)$ | 0.5 | 0 | 0.25 | Propagating |
| $(-1,0)$ | $-2.5$ | 0 | 6.25 | Evanescent |
| $(+1,0)$ | 3.5 | 0 | 12.25 | Evanescent |
| $(0,+1)$ | 0.5 | 3 | 9.25 | Evanescent |

$$
k_{z,00}=k_0\sqrt{1-0.25}=k_0\cos30^\circ=\frac{\sqrt3}{2}k_0.
$$

No order is missed: for $n\ne0$, $|3n|\ge3>1$; for $n=0,m\ne0$, the minimum $|0.5+3m|$ is 2.5. Thus only (0,0) propagates on this air side. This says nothing yet about its power.

$$
\frac{\lambda_0}{1+\sin\theta_{\max}}=\frac{30}{1+0.5}=20\,\mathrm{mm},\qquad10\,\mathrm{mm}<20\,\mathrm{mm}.
$$

Higher air-side orders remain closed up to 30°. This does not guarantee unit reflection: absorption, transmission and converted polarization still need accounting, and the opposite medium needs its own channel check. Retain both TE and TM states of the fundamental if conversion is possible, and all propagating modes on any second port. Add evanescent modes as near-field and port-distance convergence require.

$$
\phi_{\rm surface}=\phi_{\rm port}+2k_{z,00}d_{\rm port}\pmod{360^\circ}.
$$

$$
2k_{z,00}d_{\rm port}=2\left(\frac{2\pi}{30}\cos30^\circ\right)(10)=\frac{2\pi\sqrt3}{3}\,\mathrm{rad}.
$$

$$
\Delta\phi=360^\circ\frac{2(10)(0.8660)}{30}\approx207.85^\circ,\qquad\phi_{\rm surface}=-110^\circ+207.85^\circ=97.85^\circ\pmod{360^\circ}.
$$

The result follows the explicitly specified reference-plane relation. Confirm the sign on a simple structure before copying deembedding distances between software packages.

Setup order: define the physical cell and materials; pair lateral faces with the calculated phase; excite the required polarization and retain outgoing modes; refine mesh, port modes and spacing independently; extract amplitude/phase and move the reference plane. PBC solves the identical infinite array, LPA extends it approximately to a graded array, and deembedding removes known propagation.

```
:::
