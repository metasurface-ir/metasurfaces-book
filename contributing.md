# Contribute to the book

You can help write a section, improve an explanation, add a numerical investigation, or correct an error. Every contribution uses the same book layout: you write Markdown or a Jupyter notebook, and the site supplies navigation, mathematics, captions, and styling.

## Choose a contribution route

For Persian contributions, follow the [translation workflow and coverage record](translations.md). The Persian [contribution guide](https://metasurface-ir.github.io/metasurfaces-book/fa/contributing/) explains the same process for student translators. Keep numerical models shared across languages.

| Route | Best for | What to submit |
| --- | --- | --- |
| GitHub in the browser | Corrections and short text additions | Edit a file, then propose the change in a pull request |
| A fork and a local editor | Chapters, notebooks, and figures | Push a topic branch to your fork and open a pull request |
| An instructor handoff | Contributors new to Git | Give the instructor `.md` or `.ipynb` files, figures, references, and a short description |

Open an issue before beginning a large contribution so the instructor can coordinate scope and avoid duplicate work. The instructor reviews the scientific content and merges accepted work. The live site updates automatically after a successful build and deployment.

## Edit in the browser

1. Open the [source repository](https://github.com/metasurface-ir/metasurfaces-book).
2. Navigate to a Markdown file and choose the pencil icon. GitHub may ask you to fork the repository.
3. Make a small, focused change and describe why it helps the reader.
4. Propose the change and open a pull request. Check the build result and respond to review comments.

## Add a chapter section or lab locally

Fork the repository on GitHub, then substitute your GitHub username below:

```sh
git clone https://github.com/YOUR-USERNAME/metasurfaces-book.git
cd metasurfaces-book
git switch -c chapter-10-surrogate-models
```

Copy `templates/chapter-section.md` for a text contribution or `templates/lab-outline.md` for an investigation. Put chapter text in `chapters/`, lab instructions in `labs/`, notebooks in `notebooks/`, and figures beside the relevant chapter or in `assets/`. Use descriptive file names without spaces.

Download a starting file: {download}`templates/chapter-section.md` or {download}`templates/lab-outline.md`.

Add the page to `project.toc` in `myst.yml`:

```yaml
- title: Chapter 10 - AI and Metasurfaces
  children:
    - file: chapters/10-ai-metasurfaces.md
    - file: labs/13-ai-metasurfaces.md
```

Keep related entries together. Existing entries may already provide the right place to add your page; avoid duplicating them. Install the book environment described in [Getting started](getting-started.md), preview with `jupyter-book start`, and check with `jupyter-book build --html --strict`.

```sh
git add chapters/your-section.md myst.yml
git commit -m "Add explanation of surrogate validation"
git push -u origin chapter-10-surrogate-models
```

Open a pull request from your branch to `metasurface-ir/metasurfaces-book:main`. The automated build is a formatting and configuration check; scientific correctness still requires review.

## Notebook contributions

- Use a Python 3 kernel and expose parameters in a clearly labeled cell.
- Define units, coordinate directions, phasor conventions, material models, and boundary conditions.
- Restart the kernel and run all cells in order. Save the outputs and record the environment.
- Include analytical checks, convergence studies, and independent comparisons appropriate to the model.
- Keep modest demonstration datasets in the repository; link large datasets from an archival host with a version or DOI.
- Explain what an output establishes. A synthetic response, an allowed diffraction order, and a converged full-wave efficiency are different kinds of evidence.

The publishing workflow displays saved notebook results. It does not execute all student notebooks or run licensed solvers. Do not include private data, credentials, or unapproved answer keys in submitted files.

For the Chapter 10 comparison, two figures are also displayed in the chapter. After rerunning and saving `notebooks/10-neural-comparison.ipynb`, run `python scripts/export_chapter10_figures.py` to copy its tagged plot outputs into `assets/chapter-10/`. Check the accompanying interpretation when results change. The export command needs only Python's standard library.

For Chapter 4, use `python scripts/export_chapter04_figures.py` after running and saving `notebooks/04-floquet-orders.ipynb`. Its independent browser explorer is in `interactives/floquet-explorer.html`; check its reference examples, narrow-screen layout, and control behavior when changing the equations. The `interactives/` folder is published through `project.static_files` in `myst.yml`. Numerical tables should use a supported rich-output format such as HTML, and their published rendering should be checked alongside notebook execution.

The Chapter 4 notebook exports five original figures and checks the selection rule, finite-array formula, outgoing-field decay, and sampled-phase Fourier coefficients. Keep the paired Persian notebook's prose in sync and its numerical outputs empty. The browser selects English or Persian from the document language; verify both editions, the geometry/phase controls, and the selected harmonic. Preserve the distinction between illustrative motifs, prescribed scalar fields, and a solved device. Browser launch links must open in a new tab, with no browser-lab download control.

## Chapter 1 source and data workflow

For Chapter 1, keep `notebooks/01-first-metasurface-model.ipynb` with `simulations/intro_sheet.py`. Run all cells from a fresh kernel, then `python scripts/validate_chapter01.py` and `python scripts/export_chapter01.py`. The browser template is `templates/foundations-explorer.html`; check its parity with Python, undefined transmission phase, presets, controls, offline use, and narrow-screen layout after edits. Retain the ideal-sheet assumptions and avoid interpreting analytical consistency checks as a full-wave or experimental validation.

## Chapter 2 source and data workflow

Keep `notebooks/02-waves-and-interfaces.ipynb` with `simulations/waves_interfaces.py`. Execute from a fresh kernel, then run `python scripts/validate_chapter02.py` and `python scripts/export_chapter02.py`. The editable browser source is `templates/waves-explorer.html`; verify its numerical parity with Python and its four views, coherent phase control, new-tab launch, offline operation, and mobile layout. The two SVG schematics are editable originals; the five PNGs come directly from tagged notebook cells. Preserve the tangential TM sign convention, phase references, cutoff/evanescent distinctions, and assumptions of electric-sheet retrieval.

## Chapter 3 source and data workflow

For Chapter 3, keep the notebook and `simulations/unit_cell_te.py` together. After saving a fresh execution, run `python scripts/validate_chapter03.py --grcwa` with the optional validation environment, then `python scripts/export_chapter03.py`. This updates the data audit, three figures, embedded-data explorer, and source ZIP. If you skip the optional comparison, report that explicitly. The explorer's editable template is `templates/unit-cell-explorer.html`; its published file is generated from the JSON library. Preserve the source hash, domain, phase references, and acceptance thresholds when adding data. Use a new dataset version for another physical experiment.

## Chapter 5 source and data workflow

For Chapter 5, execute `05-beam-steering.ipynb` before `05-wavefront-models.ipynb`, then run `scripts/validate_chapter05.py --grcwa` and `scripts/export_chapter05.py`. The source ZIP includes both modules and the original Chapter 3 data dependency. The editable explorer template is `templates/synthesis-explorer.html`; its published HTML embeds the generated data. Preserve the distinction between full-wave supercells, local estimates, scalar focusing, and ideal Jones matrices. Update captions and validation when results change.

## Share a folder with the instructor

Include the source page or notebook, its images/data, a requirements file if it needs additional packages, references, your name as you want it credited, and a note describing what has been executed or verified. The instructor can integrate that folder and add its table-of-contents entry. No special design software or HTML editing is required.

## Scientific and editorial review

Use original explanations and properly attributed figures. Link claims to sources and label your assumptions. If you use AI assistance, verify equations, citations, code, and numerical results yourself and describe the assistance in the pull request. Submit only material you can authorize for public publication; the repository currently has no general reuse license.

## Chapter 6 and figure provenance

Keep the numerical-methods notebook with `simulations/numerical_methods.py` and its exact-film dependency. Restart/run, validate, and export using the Chapter 6 scripts. Run `python scripts/export_figure_provenance.py` after all image exports; `--check` verifies the inventory during publication. Follow [source and reuse guidance](attribution.md): include original generators and check actual permissions for adapted material. The provenance record documents generation, not a blanket legal clearance.

## Chapter 7 evidence and exports

Edit the shared `simulations/tunable_surface.py` and English notebook, then rerun all notebook cells and `python scripts/validate_chapter07.py`. Preserve the paired Persian notebook code and translate its Markdown cells. Export original schematics with `python scripts/export_tunable_geometry.py`, and saved plots, browser evidence and sources with `python scripts/export_chapter07.py`. The browser renderer checks the model hash and reference parameters against the audit. Regenerate figure provenance, review affected Persian prose and source locks, and run the strict bilingual build. Browser labs open in a new tab; source bundles contain Python/notebook/data files, with no browser-lab HTML download.
