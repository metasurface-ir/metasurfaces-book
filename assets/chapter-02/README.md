# Original Chapter 2 figures

The two SVG schematics are original editable vector drawings of geometry,
polarization, reference planes, and boundary conditions. The six PNG figures
are copied byte-for-byte from tagged Matplotlib outputs in the executed Chapter 2
notebook by `scripts/export_chapter02.py`.

The plots show exact restricted planar analytical models. In particular, the
TIR map is an analytical field reconstruction, not a discretized simulation of a
patterned surface. Preserve captions, assumptions, and the generating notebook
when editing or sharing the figures.

`retrieval-conditioning.png` comes from the `ch02-retrieval-conditioning`
notebook cell. It compares a deterministic model-consistent complex perturbation
with the local inverse derivative; it is not measured uncertainty or a material
retrieval. Its numerical arrays are retained under `retrieval_conditioning` in
`data/chapter-02/waves-reference.json`.
