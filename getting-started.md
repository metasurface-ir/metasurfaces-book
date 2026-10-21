# Computational environment

## Read the book

The published book is readable in a browser without installing Python. Saved notebook outputs are displayed in the static site. Running or modifying calculations requires a local Jupyter environment or a separately configured hosted kernel.

## Build this starter locally

Use Python 3.12 and Node.js 24 with npm. Run these commands from the book directory in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\jupyter-book.exe build --html
```

The generated website is written to `_build/html/`. For a local development server:

```powershell
.\.venv\Scripts\jupyter-book.exe start
```

Open the local URL printed by the command. On macOS/Linux the executable is `.venv/bin/jupyter-book`.

## Start with the Chapter 1 notebook

For a first computational activity, use the [Chapter 1 lab](labs/01-first-investigation.md). Its browser explorer runs online or offline without Python. To edit calculations, install `requirements-labs.txt` in a Python 3.12 environment and extract the complete source ZIP, preserving `notebooks/`, `simulations/`, and `data/`. Open `01-first-metasurface-model.ipynb`, restart its kernel, and run all cells. It imports `simulations/intro_sheet.py` and generates response CSV/JSON files.

The model needs NumPy and Matplotlib, with no electromagnetic solver, GPU, or network dataset. Run `python scripts/validate_chapter01.py` from the extracted folder or repository root for the analytical audit. After saving the notebook and audit, `python scripts/export_chapter01.py` updates its three figures, standalone browser explorer, and source ZIP. The explorer template is `templates/foundations-explorer.html`. The model is an ideal sheet, with no assigned physical geometry.

## Run the Chapter 10 notebooks

From the repository root, install the optional notebook environment into the same virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-labs.txt
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

Open `10-resonant-surrogate.ipynb` first, then `10-neural-comparison.ipynb`. Select the environment's Python kernel and choose **Restart Kernel and Run All Cells**. Each notebook records its numerical package versions. Parameters are in its first code cell; the data are generated locally. The neural comparison also uses scikit-learn and runs several small CPU fits; a GPU is unnecessary.

Both notebooks are downloadable from their book pages and can run independently. If you download a notebook alone, install the packages in the repository's `requirements-labs.txt`. Saved outputs show the published reference run; edited parameters produce a new experiment and may change results or optimizer behavior.

The comparison intentionally preserves optimizer warnings from unsuccessful validation candidates. Check the selected-model and repeat-run status separately from the trial table. An execution that finishes is not evidence that every optimizer met its convergence criterion.

## Run the Chapter 4 notebook

Use the same `requirements-labs.txt` environment and open `04-floquet-orders.ipynb`. Restart the kernel and run all cells. NumPy and Matplotlib produce the analytical reference outputs; ipywidgets supplies optional sliders when `ENABLE_WIDGETS=True`. Keep the flag `False` when saving a static reference for publication, so the page can display its results without a live widget session.

The [Chapter 4 lab](labs/04-floquet-lab.md) also embeds a standalone HTML explorer. Its controls run in the browser with no Python kernel or network data service. The explorer can be opened in its own page or downloaded for offline use.

## Run the Chapter 3 full-wave notebook

Use the same `requirements-labs.txt` environment. Clone the repository or extract the complete ZIP from the [Chapter 3 lab](labs/03-unit-cell-lab.md), then open `notebooks/03-unit-cell-library.ipynb`. The notebook imports `simulations/unit_cell_te.py`; preserve both folders. Restart the kernel and run all cells. It generates response-library CSV/JSON files in `data/chapter-03/` and displays field, response, spectral, and validation results. These are CPU calculations for a restricted one-dimensional dielectric TE model.

To reproduce the additional audit, run from the extracted folder or repository root:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-validation.txt
.\.venv\Scripts\python.exe scripts/validate_chapter03.py --grcwa
```

The optional grcwa dependency is required only for the separate implementation comparison. Both implementations use RCWA. Without `--grcwa`, the audit records that this optional comparison was not run. Editing physical or numerical parameters requires renewed validation and a new dataset version. The fixed reference audit describes the published experiment.

Run `python scripts/export_chapter03.py` after saving the executed notebook and audit to update its chapter figures, offline data explorer, and source ZIP. The explorer displays saved data rather than running Python in the browser. Optional Jupyter controls also inspect the computed rows; set `ENABLE_WIDGETS=True` locally and keep it `False` for the saved static reference.

## Run the Chapter 5 synthesis notebooks

Use `requirements-labs.txt` and extract the complete source ZIP from the [Chapter 5 lab](labs/05-synthesis-lab.md), or clone the repository. Preserve the `simulations/`, `data/`, and `notebooks/` folders. Run `05-beam-steering.ipynb` first, then `05-wavefront-models.ipynb`; the second reads the library generated by the first. Restart each kernel and run all cells.

The first notebook computes an expanded library, geometry selection, full-wave supercells, local estimates, and convergence. The second executes scalar line-focus propagation and analytical Jones models. They use CPU NumPy/SciPy/Matplotlib with no licensed solver or GPU. Install `requirements-validation.txt` and run `python scripts/validate_chapter05.py --grcwa` for the optional separate RCWA implementation comparison. Its fixed reference cases need adaptation when changing the experiment.

After saved notebook executions and audit, `python scripts/export_chapter05.py` exports six original figures, the embedded-data browser explorer, and the source ZIP. Keep the scalar/Jones and full-wave evidence labels when contributing edited results. The browser explorer only selects saved cases.

## Further computational labs

The analytical starters need no electromagnetic solver. Chapters 3 and 5 supply restricted TE solvers. Further full-wave labs will specify their own solver versions, licenses where applicable, data inputs, and execution environments.

Full-wave solvers such as COMSOL, FDTD, or RCWA will have separate setup and validation instructions. Routine book publication will use saved results rather than rerunning expensive simulations.
