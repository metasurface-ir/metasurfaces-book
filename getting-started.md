# Computational environment

## Read the book

The published book will be readable in a browser without installing Python. Saved notebook outputs can be displayed in the static site. Running or modifying calculations requires a local Jupyter environment or a separately configured hosted kernel.

## Build this starter locally

Use Python 3.12 and Node.js 24. Run these commands from the book directory in PowerShell:

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

## Computational labs

No solver environment is installed by this starter. We will add NumPy, plotting, Jupyter kernels, and any required numerical solver when the first lab is implemented, then record compatible versions and execute the notebook before publication.

Full-wave solvers such as COMSOL, FDTD, or RCWA will have separate setup and validation instructions. Routine book publication will use saved results rather than rerunning expensive simulations.
