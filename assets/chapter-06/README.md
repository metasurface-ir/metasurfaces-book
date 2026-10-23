# Original Chapter 6 numerical figures

All four PNGs are exported byte-for-byte from tagged saved Matplotlib outputs
in `notebooks/06-numerical-methods.ipynb` by `scripts/export_chapter06.py`.

| Output | Cell tag | Evidence |
| --- | --- | --- |
| convergence.png | ch06-convergence | Complex wave error versus residual and discrete flux defect |
| fields.png | ch06-fields | Exact/FDFD field comparison at common coordinates |
| boundaries.png | ch06-boundaries | Independent padding, boundary mismatch and deembedding diagnostics |
| harmonics.png | ch06-harmonics | Single-cell and saved Chapter 5 supercell harmonic refinement |

The generating code and calculations are original to this course; no external
image or publisher artwork is used. The slab is normal-incidence tangential Ey,
lossless, isotropic, nonmagnetic, with equal exterior media and face-referenced
coefficients. Its radiation condition matches the discrete exterior, not a PML.
The reference benchmark is the independently implemented exact Chapter 2 film.
The RCWA panels have their own fixed geometry and high-order comparison
references; neither is an exact patterned-device or experimental benchmark.

See `data/chapter-06/README.md` and its JSON metadata for parameters, source
hashes, numerical controls, environment and references. The notebook parameter
cell changes the slab experiment; saved RCWA reference cases remain explicit.
