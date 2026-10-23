# Linked design studies: ms-09, ms-10, ms-11

Authoritative generators are notebooks/09-dispersion.ipynb,
notebooks/10-coupling.ipynb and notebooks/11-inverse-design.ipynb. Each JSON
contains the fixed physical inputs, units, normalized-text source hashes,
environment, numerical controls and computed values. All widths/lengths are in
micrometers. TE Ey, exp(-i omega t), r at z=0, t at z=height. Constant positive
real indices and an infinite periodic six-ridge sequence; not a finite device.

- dispersion.json: 161 wavelengths at M=96/144, connected efficiency/useful
  passbands for 41/81/161 spectral grids, clipping flags and frequency widths.
- coupling.json: five width contrasts, local and full order powers, independent
  cell/supercell harmonic refinement, exact identical-array embedding control.
- inverse-design.json: every bounded objective evaluation, seeds and budgets,
  stopping messages, best queried candidate, frozen-candidate checks, withheld
  wavelengths, deterministic width perturbations and optional grcwa comparison.
- validation.json: replay checks, analytic film and mirror symmetry tests.

Run all three notebooks before scripts/validate_design_studies.py --grcwa.
Install requirements-validation.txt for grcwa. It is a separate RCWA
implementation, not independent FEM/FDTD validation. A saved reference audit
does not certify edited parameters. Preserve the original result when exploring.

Use scripts/export_design_studies.py to export tagged notebook figures and the
Python/notebook ZIP. The browser explorer selects saved data; it is hosted on
the book site and is not included in downloads. The figures are original outputs.
