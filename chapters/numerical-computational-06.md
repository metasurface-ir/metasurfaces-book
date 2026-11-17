---
title: "Move a monitor without moving the device"
---

# Move a monitor without moving the device

Suppose incident/reflected amplitudes are extracted at a left node a distance $L_-$ from the entrance and transmission at a right node $L_+$ after the exit. With local incident normalization, the raw coefficients satisfy

$$
r_{\rm mon}=r_0 e^{-2ik_hL_-},\qquad
t_{\rm mon}=t_d e^{-ik_h(L_-+L_+)},\qquad k_h=\theta/h.
$$

Deembed using the **same propagation law as the solved grid**. Using continuum $k_e$ instead leaves an error proportional to $(k_h-k_e)L$. Powers can remain unchanged while phase drifts. With the deliberately mismatched right boundary, forward and backward waves coexist in the output region; report their net flux separately. Here $t_{\rm mon}$ denotes the forward-wave coefficient obtained by decomposing the two traveling waves; the squared total field at one monitor node is not forward transmitted power.

$$
J_{j+1/2}=-\operatorname{Im}(E_j^*E_{j+1}),\qquad
T_{\rm net}=T_{\rm forward}-T_{\rm backward}.
$$

The grid current is constant in a real-index source-free region. It is proportional to physical flux in the continuum limit; normalization by the incident discrete current makes it the appropriate finite-grid conservation check. Equal exterior indices give the same current weight for incoming and outgoing amplitudes.

```{figure} ../assets/chapter-06/boundaries.png
:alt: Independent padding sweep showing stable face-referenced amplitudes with matched boundaries, boundary-induced reflection, and phase drift from wrong deembedding.

Hold the film mesh fixed while varying padding. Correct discrete boundaries and deembedding give invariant face coefficients. Boundary mismatch and a reference-plane error leave distinct signatures.
```

In a larger FEM/FDTD simulation, open boundaries commonly use absorbing layers. PML performance still requires thickness and separation checks; see the [Meep PML documentation](https://meep.readthedocs.io/en/latest/Perfectly_Matched_Layer/). Do not move geometry, change mesh, and enlarge the absorber in one sweep and call the result a mesh-convergence study.
