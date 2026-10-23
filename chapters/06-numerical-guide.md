---
title: 'Chapter 6: Worked Examples and Learning Path'
short_title: Numerical worked examples
---

# Chapter 6: Worked Examples and Learning Path

**Question:** what would persuade you to accept a simulation result? Work through [the chapter](06-numerical-methods.md), predict each experiment, then use the [lab](../labs/06-numerical-lab.md) and [notebook](../notebooks/06-numerical-methods.ipynb) to test the prediction.

## Learning path

| Stage | Prediction | Evidence |
| --- | --- | --- |
| 1 | A tiny residual can coexist with a large wave error | Compare the three mesh diagnostics |
| 2 | Refinement changes the accumulated phase | Overlay numerical and exact fields |
| 3 | Correct face coefficients are independent of padding | Hold mesh fixed and move the boundary |
| 4 | A phase-plane error can preserve power | Change only deembedding |
| 5 | Harmonic conservation precedes amplitude convergence | Compare saved supercell refinements |
| 6 | Numerical accuracy does not remove model discrepancy | Name the omitted physics in a report |

## Example 1: define the transmitted wave before comparing it

The reference slab has wavelength $1.55\,\mu\mathrm m$, thickness $0.60\,\mu\mathrm m$, film index 2.4, exterior index 1, normal incidence, and unit incident electric amplitude at $z=0$. Transmission is measured at $z=d$. Even a uniform medium has $t=e^{ik_ed}$ with these two distinct reference planes; its transmission phase is not generally zero.

Check this limit with `Slab(n_film=1.0)`. The finite-grid counterpart is $t=e^{iN\theta}$ with zero reflection. It exactly solves the discrete system while its phase differs from the continuum result. This isolates numerical dispersion without a material interface.

## Example 2: solve accurately, predict inaccurately

For the default slab with only four film cells, the saved experiment has $|t_h-t_{\rm exact}|$ about 0.82 and circular phase error about $51^\circ$, although power balance is near floating-point precision. The coarse grid is a deliberately bad prediction.

This is possible because a real symmetric interior stencil has a conserved discrete current. A linear solver can solve that coarse conservative system accurately. Neither property establishes that its wave number or interface scattering approximates the continuum well. Inspect fields and complex coefficients instead of accepting a green conservation indicator.

## Example 3: ask whether the sequence is asymptotic

For the aligned reference slab, use $N=32,64,128,256,512$. Compare exact complex-transmission errors and their ratios. If successive errors fall by approximately four, the observed order is near two:

$$
p_{\rm exact}=\log_2\frac{|t_h-t_{\rm exact}|}{|t_{h/2}-t_{\rm exact}|}.
$$

At $N=512$ the default error is about $4.1\times10^{-5}$. This is an acceptance result for a specified observable and geometry. It does not give every high-index resonator the same required cell count. Repeat the experiment after changing material contrast or optical thickness.

When no exact answer exists, compare three complex amplitudes using the chapter's successive-difference formula. Check that an asymptotic trend exists before extrapolating. A nearly zero difference can also arise from cancellation or shared errors.

## Example 4: a monitor can introduce a phase mistake

At fixed $N=8$, add exterior grid cells without changing the slab. Matched discrete boundaries plus discrete deembedding recover the same face coefficients. Now use continuum $k_e$ to remove propagation from the same grid solution. The resulting transmission error has phase

$$
\Delta\phi=(k_h-k_e)(L_-+L_+),\qquad k_h=\theta/h.
$$

The notebook uses circular phase differences and records actual left/right distances. Power is unchanged by this unit-modulus phase factor. Correcting an extraction formula can fix this error without changing the electromagnetic solve.

## Example 5: distinguish boundary reflection from monitor phase

Replace the right outgoing ghost multiplier $e^{i\theta}$ by $e^{ik_eh}$ while holding everything else fixed. This creates a backward wave in the exterior. Padding changes its interference with the slab, so errors can oscillate rather than decrease monotonically.

Decompose forward/backward amplitudes and compare their **difference in power** with the discrete current. The squared total field at one output node contains interference and is not a transmitted-power measurement. Restoring the matched boundary removes this deliberate reflection; correcting only the monitor phase does not.

## Example 6: transfer the test to a beam-steering supercell

The saved Chapter 5 extended supercell has an almost zero power defect at low harmonic count, while its target-order power still changes upon refinement. Open-order powers must be compared on the same order labels and incident normalization. The dataset identifies which higher-order calculation is the comparison reference.

Ask for both incident-normalized target power and complex transmitted amplitude. A converged total transmitted power could conceal redistribution among open diffraction orders. Maintain the same geometry and physical wavelength during a harmonic sweep; increasing harmonics is a numerical change, increasing ridge height is a new experiment.

## Self-check and report rubric

1. **Does $R+T=1$ establish accuracy?** It checks lossless conservation within the modeled system; compare refinements and independent references as well.
2. **Does agreement of two RCWA implementations validate FEM/FDTD?** It tests implementation choices within RCWA. A different method must solve the same physical geometry with its own converged controls.
3. **Does an exact slab check validate a finite lens?** It verifies a useful limit and conventions. A finite lens adds geometry, vector fields, boundaries, and different observables.
4. **Must padding errors decrease monotonically?** No; reflections interfere coherently. Vary boundary quality separately and inspect amplitudes.
5. **Can phase error be reported at zero transmission?** Its interpretation is unstable there. Use a stated amplitude floor and complex error.

Suggested report grading: problem/conventions 20%, independent controlled experiments 30%, numerical evidence and plots 30%, interpretation/model limits/provenance 20%. Submit a failed coarse case alongside the accepted result, explaining exactly which evidence changed your decision.
