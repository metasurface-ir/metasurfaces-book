# Metasurface.ir

**Metasurfaces: From Wave Physics to Design** is an English graduate course and computational book, published with Jupyter Book 2.

**Read:** https://metasurface-ir.github.io/metasurfaces-book/

**Contribute:** read [the contribution guide](contributing.md). Students can submit Markdown, Jupyter notebooks, original figures, or corrections through pull requests. The instructor reviews contributions before publication. You can also give the instructor a content folder for integration.

## Local editing

Install Python 3.12 and Node.js 24 (including npm), then:

```sh
python -m venv .venv
# Windows:
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\jupyter-book.exe start
# macOS/Linux: use .venv/bin/python and .venv/bin/jupyter-book instead.
```

The command prints a local preview URL. To export HTML, use `jupyter-book build --html --strict` from the same environment. Jupyter Book downloads its web theme and dependencies on the first build.

## Structure

| Path | Purpose |
| --- | --- |
| `myst.yml` | Book title, repository link, and table of contents |
| `intro.md`, `syllabus.md` | Welcome and chapter map |
| `chapters/` | Chapter text and worked derivations |
| `labs/` | Computational investigations and lab briefs |
| `notebooks/` | Editable notebooks with saved results |
| `simulations/` | Parameterized electromagnetic solver source |
| `data/chapter-03/` | Unit-cell response library, metadata, and numerical audit |
| `interactives/`, `downloads/` | Browser explorers and downloadable source bundles |
| `templates/` | Copyable contribution templates |
| `.github/workflows/pages.yml` | Build checks and automatic publication |

Only entries in `project.toc` appear in the sidebar. Add a new page there to publish it. Markdown and notebooks share the same book theme automatically.

## Publication

Pull requests run the book build. Merging into `main` rebuilds and deploys the site with GitHub Actions. Wait for the deployment job to succeed, then inspect the live page. The repository prefix is configured automatically by the workflow.

Heavy electromagnetic simulations run separately; the book publishes saved outputs and reproducible instructions. Label analytical, synthetic, simulated, and experimental results clearly.

## Editorial status

Chapters 3, 4, and 10 have developed computational materials. Chapter 3 supplies an executed TE ridge RCWA solver, validated response library, field plots, browser data explorer, and source ZIP. Its numerical audit can be reproduced with `python scripts/validate_chapter03.py --grcwa` after installing the lab and optional validation requirements. Regenerate its figures/explorer/ZIP with `python scripts/export_chapter03.py` after saving the notebook and audit. Further FEM/FDTD, supercell, and finite-device investigations remain explicit outlines.

Chapters 1-9 follow an instructor-supplied contents outline; Chapter 10, AI and Metasurfaces, was added by the instructor. Individual pages state their development status. This repository is the authoritative editing home for this book; the original local starter in the website workspace is an earlier snapshot.

Authors retain rights to their contributions. No general reuse license has yet been selected. Submit only material you have permission to publish, and include attribution for external sources.
