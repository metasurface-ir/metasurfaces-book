# Chapter 6 numerical-methods reference data

These original calculations compare a one-dimensional finite-difference
frequency-domain (FDFD) dielectric slab with an independent exact Fresnel film.
They also inspect the existing Chapter 3 TE RCWA solver's harmonic convergence.
No FEM, FDTD, PML, 3D, finite-device, fabricated-device, or experimental run is
claimed. The slab benchmark does not independently validate the patterned ridge.

From the source-bundle/repository root, with `requirements-labs.txt` installed:

```text
python scripts/validate_chapter06.py
```

The script checks the model and regenerates the saved JSON/CSV files. To keep
the reference data unchanged while checking an edited implementation, use:

```text
python scripts/validate_chapter06.py --output-dir path/to/temporary-audit
```

The optional `grcwa` dependencies are not needed. NumPy and SciPy perform the
calculations. Source hashes, runtime, software versions, numerical tolerances,
parameter values, mathematical conventions, scope, and primary sources are
preserved in the JSON files. The saved audit applies to the stated parameters,
not every possible edited slab or ridge geometry.

## Physical model and phase planes

Lengths are micrometers. The convention is `exp(-i omega t)`. A film of real
constant index `n_film` fills `0 <= z <= thickness_um`, with the same real
constant `n_exterior` on either side. Materials are isotropic, nonmagnetic,
lossless, and nondispersive. Illumination is normal-incidence tangential Ey.

The grid is node-centered, with `h = thickness_um / cells`; both film faces are
nodes. Interior/exterior nodes have their material's epsilon. Each interface
node uses the arithmetic half-cell average epsilon. This is appropriate for
this scalar tangential-E problem and is not a general TM/vector averaging rule.

The exterior discrete wave has `theta = 2 asin(k0*n_exterior*h/2)` per step.
The exact discrete outgoing ghost relation uses `exp(i theta)`. Reflection is
referenced to z=0; forward transmission is referenced to z=thickness_um. The
incident field is normalized to one at z=0. Numerical field arrays always use
this correct discrete normalization, including rows demonstrating incorrect
deembedding of the reported scattering coefficient.

`right_boundary=continuum` deliberately replaces the right ghost multiplier
by `exp(i k0*n_exterior*h)` and produces a small artificial reflected wave.
`deembed=continuum` deliberately removes monitor propagation with the wrong
wave number for the finite-difference lattice. These are different errors.

Equal exterior indices make `R=|r|^2` and `T_forward=|t|^2`. With a mismatched
right boundary, `T_backward` is nonzero and `T_net=T_forward-T_backward` is
the transmitted **net** flux. `T` is a documented alias of `T_forward`.
Use `T_net` for `energy_defect=|1-R-T_net|`; the total field magnitude at the
right boundary is not the outgoing wave amplitude when reflection is present.
The returned discrete current is
`Im(conj(E_j)*E_(j+1))/sin(theta)` at the midpoint between adjacent nodes.

## Data API for the notebook and offline explorer

`numerical-reference.json` contains:

- `metadata`: physical inputs, conventions, exact complex r/t, hashes,
  environment, thresholds, sources, and limitations.
- `mesh`: N=4,8,16,32,64,128,256,512. Scalar rows include `t_real`, `t_imag`,
  `r_real`, `r_imag`, `phase_deg`, `phase_error_deg`, `complex_t_error`,
  `complex_r_error`, `power_T_error`, `energy_defect`, `algebraic_residual`,
  `current_spread`, and observed order. The first observed order is null.
- `fields`: N=8,64,512 over the same physical window `[-d/2,3d/2]`. Each record
  has `z_um`, `epsilon_r`, `E_real`, `E_imag`, `exact_E_real`, `exact_E_imag`,
  `current_z_um`, `current`, and scalar `diagnostics`. The field is complex Ey,
  not a local power or energy density.
- `padding`: 195 rows, covering 0..64 exterior cells on each side at fixed N=8
  for `(boundary,deembed)` equal to `(discrete,discrete)`,
  `(continuum,discrete)`, or `(discrete,continuum)`. All mesh diagnostics are
  present, together with `padding_cells`, `padding_um`,
  `complex_t_vs_matched`, `phase_drift_deg`, and
  `predicted_deembed_drift_deg`. The last prediction applies to the deliberately
  wrong deembedding; it is zero for correctly deembedded rows. A mismatch at a
  lossless distant boundary causes oscillations and does not disappear merely
  by increasing the padding length.
- `harmonics`: RCWA M=0,1,2,4,8,16,24,32,48,64 with a numerical M=64 reference;
  this reference is not exact. `harmonics_metadata` gives the ridge inputs.
  Each row distinguishes complex response error, energy defect, and residual.
- `model_comparison`: a centered thin-film electric-sheet approximation versus
  the continuous exact slab as thickness changes. Both use identical entrance
  and exit reference planes. This is a difference between mathematical models,
  not measured-device error. It has no finite-difference mesh to refine.
- `chapter05_saved_evidence`: an explicitly labelled, hashed extract of the
  existing Chapter 5 audit, not a fresh supercell run by this script.

The CSV files preserve the corresponding flat mesh, padding, harmonic, and
model-comparison tables. The JSON is convenient for embedding offline in a
browser explorer; selecting a saved row does not run a solver in JavaScript.

`validation.json` records independent exact-film parameter checks, a separate
four-amplitude interface-equation check of the exact Fresnel phase conventions,
homogeneous discrete propagation, spatial order, current conservation, domain
invariance, input guards, harmonic refinement, and expected failure examples.
Expected failures are successful teaching diagnostics when the predicted error
is observed. A small residual or energy defect alone is never an acceptance
criterion for the scattering response.

All figures derived from these data are original course outputs. Cite the
method references without copying source figures or prose.
