# Computational environment

## Read the book

The published book will be readable in a browser without installing Python. Saved notebook outputs can be displayed in the static site. Running or modifying calculations requires a local Jupyter environment or a separately configured hosted kernel.

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

## Run the Chapter 10 notebook

From the repository root, install the optional notebook environment into the same virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-labs.txt
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

Open `10-resonant-surrogate.ipynb`, select the environment's Python kernel, and choose **Restart Kernel and Run All Cells**. The notebook records the Python, NumPy, and Matplotlib versions in its output. Parameters are in its first code cell; the data are generated locally.

The notebook is also downloadable from its page in the book. If you download it alone, install NumPy, Matplotlib, and JupyterLab using the versions in the repository's `requirements-labs.txt`.

## Further computational labs

The analytical starter needs no electromagnetic solver. Future full-wave labs will specify their own solver versions, licenses where applicable, data inputs, and execution environments.

Full-wave solvers such as COMSOL, FDTD, or RCWA will have separate setup and validation instructions. Routine book publication will use saved results rather than rerunning expensive simulations.
