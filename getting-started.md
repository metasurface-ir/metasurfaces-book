---
title: Run the computational book
short_title: Setup and run matrix
---

# Run the computational book

(setup-read)=
## Read and explore

The published book displays saved results without a Python installation. Open a browser lab from its chapter or use **Open in a new tab**. Browser labs are hosted tools; their HTML is not offered for download and is not included in the Python source bundles. Editing Python calculations requires a local Jupyter environment.

(setup-sources)=
## Choose your source files

| What you want to do | What to obtain |
| --- | --- |
| Rerun a chapter investigation | Extract its complete source ZIP from the chapter lab; preserve `notebooks/`, `simulations/`, `scripts/`, and `data/` |
| Run Chapter 4 or either Chapter 10 notebook | Download that notebook from its book page and obtain the repository's `requirements-labs.txt`; these notebooks contain their own numerical functions |
| Add material, regenerate figures/browser tools, or build both languages | Clone the [complete repository](https://github.com/metasurface-ir/metasurfaces-book); source bundles do not contain the publication exporters/templates |

For a source bundle, follow its `START-HERE.md` from the extracted root. A notebook alone is insufficient when it imports `simulations/` or reads `data/`. Downloaded Persian bundles contain translated narrative with the same executable code and reference outputs as English.

(setup-environment)=
## Prepare the scientific environment

Use Python 3.12. From the extracted bundle or repository root:

```sh
python -m venv .venv
```

Activate with `.\.venv\Scripts\Activate.ps1` in PowerShell, or `source .venv/bin/activate` on macOS/Linux. If PowerShell activation is unavailable, replace `python` below with `.\.venv\Scripts\python.exe`.

```sh
python -m pip install -r requirements-labs.txt
python -m jupyterlab
```

Choose this environment's kernel. Save parameter edits, choose **Restart Kernel and Run All Cells**, and save the completed notebook. The examples use CPU NumPy/SciPy/Matplotlib; the neural comparison also uses scikit-learn. No GPU, commercial solver, or external dataset is needed for the published examples. Optional widgets should remain disabled when saving static publication outputs.

For the separate RCWA implementation comparisons in Chapters 3/5 and ms-11, install `requirements-validation.txt` from the full checkout or the relevant complete bundle. Without `--grcwa`, audits explicitly report that comparison as unexecuted. Agreement between two RCWA implementations is not an independent numerical-family check.

(setup-run-matrix)=
## Notebook order, dependencies, and measured time

All paths below are relative to `notebooks/`. Times are approximate fresh-kernel execution measurements on 28 October 2026, Windows, Intel Core i3-5005U, Python 3.12, one BLAS thread. They include kernel startup and plots, exclude package installation/audits/builds, and are not performance guarantees. For small matrix examples, set `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1` **before** launching Jupyter (PowerShell: `$env:OPENBLAS_NUM_THREADS='1'`; shell: `export OPENBLAS_NUM_THREADS=1`).

| Chapter/lab | Notebook(s), in order | Required local inputs | Measured time |
| --- | --- | --- | --- |
| 1 | `01-first-metasurface-model.ipynb` | `intro_sheet.py` | 20 s |
| 2 | `02-waves-and-interfaces.ipynb` | `waves_interfaces.py`, `source_provenance.py` | 22 s |
| 4, before the Chapter 3 solver | `04-floquet-orders.ipynb` | Self-contained; optional ipywidgets | 13 s |
| 3 | `03-unit-cell-library.ipynb` | `unit_cell_te.py`; creates the Chapter 3 library | 18 s |
| 5 | `05-beam-steering.ipynb` → `05-wavefront-models.ipynb` | Shared TE/synthesis modules; saved Chapter 3 library; second notebook reads the first's Chapter 5 library | 13 s + 7 s |
| 6, alongside 3/5 | `06-numerical-methods.ipynb` | Numerical/film/TE modules and bundled Chapter 6 benchmark files; regenerate them with the Chapter 6 validator if needed | 11 s |
| 7 | `07-tunable-metasurfaces.ipynb` | `tunable_surface.py`; assigned circuit, scalar array and synthetic control | 20 s |
| 8 | `08-communication-links.ipynb` | `communication_link.py`; scalar aperture/channel model | 16 s |
| 9 | `09-fabrication-measurement.ipynb` | `materials_measurement.py`; generated synthetic observations | 17 s |
| 10 | `10-resonant-surrogate.ipynb` → `10-neural-comparison.ipynb` | Self-contained analytical data; comparison adds scikit-learn; either can execute independently | 10 s + 28 s |
| ms-09/10/11 | `09-dispersion.ipynb` → `10-coupling.ipynb` → `11-inverse-design.ipynb` | `design_studies.py`, TE/synthesis modules; run all three before the combined audit/export | 57 s + 18 s + 27 s |

Read the [prerequisite map](learning-path.md) for the conceptual order. A successful execution can still contain an unsuccessful optimizer or an infeasible design; retain those results and their stopping reasons.

(setup-validation)=
## Validate results; export only from a full checkout

Run audit commands from the bundle/repository root. The corresponding `scripts/validate_*.py` files are included in their complete bundles. Fixed-reference audits test the declared reference and may reject a deliberately changed experiment; adapt acceptance criteria explicitly and keep reference regressions separate.

| Investigation | Audit command after saved execution | Publication command — full repository only |
| --- | --- | --- |
| 1 | `python scripts/validate_chapter01.py` | `python scripts/export_chapter01.py` |
| 2 | `python scripts/validate_chapter02.py` | `python scripts/export_chapter02.py` |
| 3 | `python scripts/validate_chapter03.py --grcwa` | `python scripts/export_chapter03.py` |
| 4 | Independent analytical assertions in the notebook | `python scripts/export_chapter04_figures.py` |
| 5 | `python scripts/validate_chapter05.py --grcwa` | `python scripts/export_chapter05.py` |
| 6 | `python scripts/validate_chapter06.py` (also regenerates benchmark data) | `python scripts/export_chapter06.py` |
| 7 | `python scripts/validate_chapter07.py` | `python scripts/export_chapter07.py` |
| 8 | `python scripts/validate_chapter08.py` | `python scripts/export_chapter08.py` |
| 9 | `python scripts/validate_chapter09.py` | `python scripts/export_chapter09.py` |
| 10 | Notebook-held-out comparisons, invariants, and recorded optimizer status | `python scripts/export_chapter10_figures.py` |
| ms-09/10/11 | `python scripts/validate_design_studies.py --grcwa` | `python scripts/export_design_studies.py` |

Preserve units, time/space signs, reference planes, parameter values, random seeds, convergence evidence, and model limitations. A small residual, a conserved power sum, or a provenance hash alone does not establish scientific accuracy. See the [contribution workflow](contributing.md) before replacing a published reference.

(setup-build)=
## Build and preview both languages

Use the **full checkout** with Python 3.12 and Node.js 24/npm on `PATH`. In a separate `.book-env` virtual environment, activate it as above, then run:

```sh
python -m pip install -r requirements.txt
python scripts/validate_translations.py
python scripts/check_notebook_provenance.py
python scripts/build_bilingual.py
python -m http.server 8000 --directory _build/html
```

Leave `BASE_URL` empty for this local server (PowerShell: `$env:BASE_URL=''`). Visit `http://localhost:8000/` and `http://localhost:8000/fa/`. GitHub Actions sets the deployed project prefix automatically. `jupyter-book start` is useful for English authoring; the complete language switch and Persian output require the bilingual build. The build displays saved outputs and checks identities; it does not rerun all simulations. Pull requests also run the small parameter-edit regression suite.
