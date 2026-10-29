# Metasurface.ir

**Metasurfaces: From Wave Physics to Design** is a graduate course and computational book, published with Jupyter Book 2 in English and Persian. Both editions cover all ten chapter drafts, their teaching/lab pages, all fifteen notebook narratives, and the course navigation. Further experimental and advanced solver extensions remain explicitly unexecuted lab outlines. Persian translations are prepared for instructor review.

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

All ten chapters have developed computational materials. Start with Chapter 1's analytical sheet notebook/explorer; its audit/export scripts are `scripts/validate_chapter01.py` and `scripts/export_chapter01.py`. Chapter 2 supplies exact planar interface/film/sheet and Jones investigations; its audit/export scripts are `scripts/validate_chapter02.py` and `scripts/export_chapter02.py`. Chapter 3 supplies an executed TE ridge solver and validated library. Chapter 5 expands the library, verifies four complete periodic supercells, and adds separate scalar focusing and analytical Jones notebooks. The full-wave audits are `scripts/validate_chapter03.py --grcwa` and `scripts/validate_chapter05.py --grcwa`, with the lab and optional validation requirements. After saved notebook executions/audits, their corresponding export scripts regenerate figures, explorers, and source bundles. Chapter 6 adds an independently benchmarked FDFD slab, numerical diagnostics, original plots and a bilingual offline explorer. Run scripts/validate_chapter06.py and scripts/export_chapter06.py for its audit/exports. Further FEM/FDTD and finite-device investigations remain explicit outlines.

Chapters 1-9 follow an instructor-supplied contents outline; Chapter 10, AI and Metasurfaces, was added by the instructor. Individual pages state their development status. This repository is the authoritative editing home for this book; the original local starter in the website workspace is an earlier snapshot.

Original prose, figures and generated data use CC BY 4.0; original software and notebook code use MIT. Authors retain ownership, and third-party terms remain in force. See [LICENSE](LICENSE), [citation metadata](CITATION.cff), [credits](CONTRIBUTORS.md), [source and reuse guidance](attribution.md), and the generated [figure provenance inventory](assets/provenance.json).

Chapter 8 is an executed bilingual scalar aperture-to-communication-link investigation. Its reproducibility entry points are notebooks/08-communication-links.ipynb and scripts/validate_chapter08.py; figure/browser/source exports are in scripts/export_chapter08.py. It does not claim full-wave or measured-link validation.

Chapter 9 adds material spectra, correlated fabrication tolerances, synthetic one-port calibration, reference-plane correction and complex uncertainty. Reproduce notebooks/09-fabrication-measurement.ipynb and scripts/validate_chapter09.py; export with scripts/export_measurement_geometry.py and scripts/export_chapter09.py. All measurements in its baseline are synthetic. The book has 62 paired pages and 15 shared numerical notebooks, with a [reading path](learning-path.md) and [capstone brief](labs/12-research-project.md).

CI runs the bounded parameter-edit tests, saved-artifact identity checks and strict bilingual build. It does not execute the full notebook suite. See [setup and measured runtimes](getting-started.md) and [the contribution workflow](contributing.md) for fresh execution, review and publication. Each build publishes `build-info.json` with its source commit and snapshot version.
