# Contribute to the book

(contribute-route)=
## Choose a route

Contribute original explanations, corrections, investigations, figures, or translations using Markdown and Jupyter notebooks. The site supplies the layout. Coordinate a substantial contribution with the instructor before duplicating work. The instructor reviews scientific content and merges accepted pull requests.

| Route | Deliverable |
| --- | --- |
| GitHub browser editor | A small focused edit and pull request, including the paired language |
| Fork and local editor | A topic branch with source, translation, numerical evidence and build results |
| Instructor handoff | Editable `.md`/`.ipynb`, figures/data, references, dependencies, preferred credit and a clear list of executed checks |

For an original idea written first in Persian, retain that draft and prepare its English counterpart; the English notebook is the common numerical source. Ask for language review in the PR if needed. Do not claim an unreviewed machine translation has been scientifically checked.

(contribute-create)=
## Create the contribution and its counterpart

```sh
git clone https://github.com/YOUR-USERNAME/metasurfaces-book.git
cd metasurfaces-book
git switch -c codex/your-investigation
```

Use {download}`templates/chapter-section.md` or {download}`templates/lab-outline.md`. Put chapter pages in `chapters/`, instructions in `labs/`, notebooks in `notebooks/`, code in `simulations/`, results in `data/`, and figures in `assets/`. Keep the matching Persian paths under `translations/fa/`. Follow [the prerequisite map](learning-path.md) and avoid duplicating the companion site's conceptual galleries.

Translate headings, narrative, questions, captions, alt text, assumptions and interpretation. Preserve equations, units, signs, references and code identifiers. Use [the glossary](glossary.md) consistently. For notebooks, copy code cells exactly; translate Markdown cells, leave Persian source outputs empty and execution counts null. The build inserts English numerical outputs into the Persian edition and its executable bundles.

(contribute-evidence)=
## Execute and preserve scientific evidence

Save edits first; restart the English notebook kernel and run every cell in order. Record parameters, seeds, environment, reference planes and failure reasons. Explain whether a result is analytical, a prescribed scalar field, a full-wave solution, a surrogate prediction, or a measurement. Include appropriate analytical limits, observable convergence, and independent checks. Save failed optimizations as evidence, not just successful candidates.

Use the [all-chapter run/audit/export matrix](getting-started.md#setup-run-matrix). Exports require the full checkout; source bundles contain the scientific sources and their audit scripts. If a source dataset changes, rerun its dependents: Chapter 3 library → Chapter 5 steering → Chapter 5 wavefront models; regenerate Chapter 6 benchmark data before checking its notebook; run ms-09/10/11 before their combined audit/export.

For new figures, keep an original generator or a tagged notebook output. After the relevant chapter export, run:

```sh
python scripts/export_figure_provenance.py
python scripts/check_notebook_provenance.py --record YOUR-NOTEBOOK-STEM
```

`--record` stores a reviewed saved-artifact snapshot; it does not execute a notebook or certify its science. It binds code, saved outputs, registered dependencies/results and explicit parameter records. Register a new notebook and its direct/transitive local file dependencies in `GROUPS` in `scripts/check_notebook_provenance.py`. Update figure provenance export mappings if adding a new asset. See [reuse and citation](attribution.md) for imported material.

(contribute-register)=
## Register the page in both editions

1. Add the English page to `project.toc` in `myst.yml` and the equivalent entry to `translations/fa/myst.yml` (the Persian staging tree uses the same relative filenames).
2. Add `source`, `translation`, and a unique, stable `route` to `translations/languages.json`. Set the same explicit MyST `slug` in both new pages when using a custom route.
3. Add identical explicit section labels, such as `(your-investigation-checks)=`, before corresponding headings. These labels preserve a section when switching languages; translated heading text alone usually creates different anchors.
4. Compare both texts for scientific equivalence, then record only the reviewed sources:

```sh
python scripts/update_translation_lock.py chapters/your-section.md
```

The source lock is a change detector and a record of a review decision; it cannot judge translation quality. Never update every hash just to silence a failure. When a numerical rerun changes saved outputs, confirm code parity and review whether the interpretation/captions must change before recording the English notebook's new lock.

(contribute-preview)=
## Check the complete result

Use the scientific environment for the regression suite and the book environment for the build, as described in [setup](getting-started.md).

```sh
python -m unittest discover -s tests -v
python scripts/check_notebook_provenance.py
python scripts/validate_translations.py
python scripts/export_figure_provenance.py --check
python scripts/build_bilingual.py
```

Preview both languages with the local static server. Inspect equations, figures, tables, citations, shared section links, mobile layouts, keyboard controls, search results and language switches. Browser labs must open in a new tab and have no download control; Python bundles may be downloaded. An interactive change needs browser behavior checks in both languages. Use original SVG generators for changed geometry, and render each localized browser tool from its shared template/data.

CI runs a bounded parameter-edit regression set, artifact-identity checks and the strict bilingual build. It uses saved scientific results and does not rerun every notebook, expensive solver sweep, or licensed solver. Fresh-kernel execution and human scientific review remain separate requirements. Chapter 2's equation-block parity check is not a guarantee of all browser physics or complete Persian semantic equivalence.

(contribute-submit)=
## Submit a reviewable pull request

```sh
git add YOUR-CHANGED-FILES
git commit -m "Explain the investigation and its validation"
git push -u origin codex/your-investigation
```

Open a PR to `metasurface-ir/metasurfaces-book:main`. Describe the learning question, changed model/data, EN/FA coverage, execution and checks, limitations, and any AI assistance. Include your preferred contributor credit. Cite primary sources and retain third-party notices. Original book text/figures use CC BY 4.0 and original code uses MIT; contribute only material you can publish under the applicable policy in [Sources and reuse](attribution.md).

A push or successful PR build is not publication. The instructor merges accepted work; GitHub Pages updates only after the main-branch deployment succeeds and the public routes are checked.
