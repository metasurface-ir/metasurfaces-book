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

## Run the Chapter 10 notebooks

From the repository root, install the optional notebook environment into the same virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-labs.txt
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

Open `10-resonant-surrogate.ipynb` first, then `10-neural-comparison.ipynb`. Select the environment's Python kernel and choose **Restart Kernel and Run All Cells**. Each notebook records its numerical package versions. Parameters are in its first code cell; the data are generated locally. The neural comparison also uses scikit-learn and runs several small CPU fits; a GPU is unnecessary.

Both notebooks are downloadable from their book pages and can run independently. If you download a notebook alone, install the packages in the repository's `requirements-labs.txt`. Saved outputs show the published reference run; edited parameters produce a new experiment and may change results or optimizer behavior.

The comparison intentionally preserves optimizer warnings from unsuccessful validation candidates. Check the selected-model and repeat-run status separately from the trial table. An execution that finishes is not evidence that every optimizer met its convergence criterion.

## Further computational labs

The analytical starter needs no electromagnetic solver. Future full-wave labs will specify their own solver versions, licenses where applicable, data inputs, and execution environments.

Full-wave solvers such as COMSOL, FDTD, or RCWA will have separate setup and validation instructions. Routine book publication will use saved results rather than rerunning expensive simulations.
