# Metasurface.ir

**Metasurfaces: From Wave Physics to Design** is a graduate course and computational book, published with Jupyter Book 2 in English and Persian. Both editions cover all seven developed chapters (1, 2, 3, 4, 5, 6, and 10), their teaching/lab pages, all nine notebook narratives, and the course navigation. Chapters 7–9 have syllabus outlines, not full chapters, in either language. Persian translations are prepared for instructor review.

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

The command prints an English local preview URL. To export both editions and the language switcher, run `python scripts/build_bilingual.py` with the book environment's Python. Output is in `_build/html`; the Persian edition is in `_build/html/fa`. With no `BASE_URL`, serve this folder with `python -m http.server 8000 --directory _build/html`. Jupyter Book downloads its web theme and dependencies on the first build. The ordinary `jupyter-book build --html --strict` command still builds the English content alone.

See [translation status and the student workflow](translations.md). Persian prose is in `translations/fa/`; `translations/languages.json` maps counterpart pages; `translations/source-lock.json` records reviewed English source hashes. CI checks those locks and the shared equations/code before building both editions. Numerical code, data, and saved notebook results have one authoritative source.

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

Chapters 1, 2, 3, 4, 5, 6, and 10 have developed computational materials. Start with Chapter 1's analytical sheet notebook/explorer; its audit/export scripts are `scripts/validate_chapter01.py` and `scripts/export_chapter01.py`. Chapter 2 supplies exact planar interface/film/sheet and Jones investigations; its audit/export scripts are `scripts/validate_chapter02.py` and `scripts/export_chapter02.py`. Chapter 3 supplies an executed TE ridge solver and validated library. Chapter 5 expands the library, verifies four complete periodic supercells, and adds separate scalar focusing and analytical Jones notebooks. The full-wave audits are `scripts/validate_chapter03.py --grcwa` and `scripts/validate_chapter05.py --grcwa`, with the lab and optional validation requirements. After saved notebook executions/audits, their corresponding export scripts regenerate figures, explorers, and source bundles. Chapter 6 adds an independently benchmarked FDFD slab, numerical diagnostics, original plots and a bilingual offline explorer. Run scripts/validate_chapter06.py and scripts/export_chapter06.py for its audit/exports. Further FEM/FDTD and finite-device investigations remain explicit outlines.

Chapters 1-9 follow an instructor-supplied contents outline; Chapter 10, AI and Metasurfaces, was added by the instructor. Individual pages state their development status. This repository is the authoritative editing home for this book; the original local starter in the website workspace is an earlier snapshot.

Authors retain rights to their contributions. No general reuse license has yet been selected. Submit only material you have permission to publish, and include attribution for external sources. See [source and reuse guidance](attribution.md) and the generated [figure provenance inventory](assets/provenance.json).
