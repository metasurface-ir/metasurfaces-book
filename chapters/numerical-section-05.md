---
title: "6.5 Practical meshing and convergence"
---

# 6.5 Practical meshing and convergence

After mastering the equations, practical details separate a trustworthy simulation from a misleading one. Let us review local meshing, convergence, port placement and finite-array effects.

## 1. Mesh where the field needs it

Thin sharp metal edges can support singular fields. A coarse edge mesh can misrepresent local energy and shift the resonance. Refine gaps, corners and material discontinuities locally while keeping smooth exterior regions coarser. The source invokes Meixner’s edge behavior as the physical reason.

The source stresses matching meshes on paired periodic FEM faces and warns that uncontrolled interpolation can corrupt phase. More generally, use a boundary pairing supported by the discretization: matching meshes or a verified nonconforming/mortar constraint. A mismatch is not automatically invalid if the formulation handles it consistently.

## 2. Convergence targets

$$
\max_{ij}|S_{ij}^{(n)}-S_{ij}^{(n-1)}|<\delta_{\rm target}.
$$

The source gives 0.02 as an illustrative default and suggests 0.005–0.01 for phase-sensitive designs. Treat these as starting values, not accuracy guarantees. Compare the actual complex observable, phase away from zeros, power, and an independent refinement; two successive meshes may share a bias.

In time-domain runs, allow stored resonant energy to decay. The source lists −30, −40 and −50 dB relative-energy stopping levels. Ending early truncates the response and can create spectral ripples; inspect the spectrum’s stability as run duration increases, especially for high-Q resonances.

## 3. Hidden port and air-box mistakes

| Control | Source’s practical warning/example | What must actually be checked |
|---|---|---|
| Port height | Very short gap, below $\lambda/4$; suggested height $\lambda_0/2$ | Independent port-distance and evanescent-mode refinement |
| Port modes | Only fundamental retained; source suggests 2 or 6–10 modes | Count open orders and both polarizations; refine evanescent content |
| Deembedding | Wrong or forgotten reference plane | Complex response at the declared physical surface |

The suggested distances and counts are not universal. A normal-incidence large-period array may have many open orders; an oblique deeply subwavelength array may have only the fundamental spatial order.

## 4. When the finite array must be solved

Steep neighboring phase changes and array-edge truncation can invalidate local periodicity. The source gives phase-step ranges π/2 to 2π/3 and arrays of 10×10 to 30×30 as illustrative warning cases, then recommends finite-array checks with domain-decomposed FEM or MLFMM-accelerated MoM.

Those are examples, not universal breakdown thresholds or solver recommendations. Compare a uniform reference, a supercell with unequal neighbors and a finite array at the observables the design needs. Include illumination, aperture and edge termination. The existing coupling lab below is a direct computational connection.
