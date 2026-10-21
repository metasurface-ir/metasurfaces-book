# Chapter 5 synthesis evidence

Run `notebooks/05-beam-steering.ipynb` first. It reads the original Chapter 3
library, screens five heights, builds a 161-width library at a common 1.8 um
height, checks every new row at M=24/32, and chooses six widths using a fixed
global-phase-offset search. The objective uses unit-cell phase error before
any supercell verification. It calculates limited, expanded, identical, and
reversed supercells at M=144 and 192, retaining all open-order powers.

`beam-steering.json` contains the parameters, conventions, source hashes,
selection, libraries, geometry sequences, complex transmitted coefficients,
local staircase estimates, full-wave powers, and refinement changes.
`extended-library.csv` is the convenient tabular export. Material indices
are ideal real constants, with no dispersion, loss, or experimental calibration.
The six-ridge supercell repeats indefinitely along x and is invariant along y.

Next run `notebooks/05-wavefront-models.ipynb`. Its output
`wavefront-models.json` records scalar cylindrical-line-focus metrics, FFT
window/grid refinements, and separate ideal Jones-matrix checks. Those models
are not a full-wave finite metalens or a vector response calculation of the TE
ridges. Line-intensity concentration is not a physical focusing efficiency.

`python scripts/validate_chapter05.py --grcwa` generates `validation.json`.
Install requirements-labs.txt and optional requirements-validation.txt first.
The audit checks identical-cell embedding, forbidden supercell coefficients,
mirror reversal, quantized-ramp coefficients, scalar plane-wave propagation,
Gaussian FWHM, and geometric phase. It checks saved source hashes/refinements,
then compares three supercells with grcwa at matching M=48, independently
refining grcwa's cell-averaged raster from 512 to 4096 samples. Both solvers
use RCWA; this is a separate implementation, not FEM/FDTD validation.

The saved reference uses 0.65 um pitch, 1.55 um wavelength, incident/output
indices 1/1.5, ridge/gap indices 2.4/1, and normal TE Ey illumination.
Reflection and transmission are referenced to the top and bottom faces.
After editing, rerun both notebooks, adapt the reference-specific audit to the
new experiment where required, and preserve a new dataset version. Never mix
rows with different phase planes or material/illumination conventions.

After a saved execution/audit, `python scripts/export_chapter05.py` copies
six tagged notebook PNGs, embeds the exact beam-steering dataset in the browser
explorer, and packages a source ZIP. Routine Pages publication displays saved
outputs instead of running the simulations.
