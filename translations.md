---
title: Translation status and contribution guide
short_title: English / فارسی
---

# English and Persian editions

Use **English | فارسی** in the header to open the corresponding page. English keeps its existing URLs; the Persian edition lives under `/fa/`. A page without a Persian counterpart leads to the translation-status page rather than silently presenting English as a translation.

The Persian edition covers every developed chapter: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10. It includes every published chapter guide, self-check/project page, computational lab, all fifteen notebook narratives, the complete syllabus, lab index/template, setup/contribution guides, homepage, and bilingual glossary. These translations are prepared for instructor review; technical terminology and pedagogical wording can be improved through pull requests.

| Material | Persian status |
| --- | --- |
| Homepage and navigation | Available |
| All ten developed chapters, their worked examples, self-check/project pages and labs | Available |
| All fifteen notebook narratives | Available; numerical cells and saved outputs are shared |
| Chapter 2 interactive controls and interpretation | Available; same JavaScript equations as English |
| Chapter 6 browser explorer | Fully localized controls, captions, and interpretation; shared saved numerical data |
| Chapter 4 Floquet explorer and expanded derivations | Persian controls, structure/phasor labels and field interpretation; paired proofs and shared notebook calculations |
| Two Chapter 2 schematics | Persian labels available |
| Computational plots, numerical tables and other shared scientific browser tools | Shared English scientific labels; Persian captions, lab instructions and glossary explain them |
| Syllabus, lab index/template, glossary, setup, and contribution instructions | Available |
| Chapter 9 | Paired theory, worked guide, lab and notebook; Persian schematic and fully localized four-tab browser tool |

## Contribute a translation

1. Coordinate a page with the instructor in an issue. Work on one page or a small coherent set.
2. Follow [the normal contribution route](contributing.md). Put Persian Markdown under `translations/fa/`, preserving the equivalent English folder and file names.
3. Add a matched entry to `translations/languages.json` and the Persian table of contents in `translations/fa/myst.yml`. Match the existing English URL slug explicitly in the manifest.
4. Keep equations, signs, units, parameter names, citations, model limits, and reference planes intact. Translate captions and alt text. Add terminology decisions to [the glossary](glossary.md).
5. The Persian notebook file contains translated Markdown cells and the same code sources, with no duplicated saved outputs. The bilingual builder combines its prose with the current English notebook's numerical cells and outputs. Change the shared English numerical source when a numerical correction is needed.
6. For a reviewed translation, record the English source's SHA-256 in `translations/source-lock.json`. If that source changes later, the build fails until the translation is reviewed and its hash updated. Never update the hash without checking the changed meaning.
7. Run `python scripts/validate_translations.py`, then `python scripts/build_bilingual.py` in the [book environment](getting-started.md). Preview `_build/html` and check both languages, mathematics, captions, mobile navigation, and language links. `jupyter-book start` remains useful for English content, but the bilingual build adds the Persian edition and switcher.
8. Open a pull request with the original page, translated page, translation status, terminology choices, and checks performed. The instructor reviews scientific accuracy before accepting it.

The build stages copies of shared data, figures, and simulation modules; contributors maintain one authoritative numerical source. The Persian ZIP contains the executable translated notebook and the shared model. Theme controls are localized by the small maintained layer in `styles/bilingual.js`; language direction and equation/code isolation are in `styles/bilingual.css`. When changing the theme, verify these controls again.

Browser search is separate in each edition and searches the translated pages available in that edition. Existing English links remain valid. The site does not send book text to an external translation service.


The [model and geometry guide](models.md), four original geometry figures, and model drawings in Chapters 1, 3, 5 and 6 explorers have Persian counterparts/labels. The geometry renderer is shared. Other existing scientific plot/interface labels retain the scope above.

The three ms-09/10/11 lab guides and notebooks are available in both languages. Their shared browser explorer has Persian controls, geometry labels and interpretation; numerical plot labels inside notebooks remain shared. There are 62 matched published pages.

Chapter 7 includes translated chapter/guide/lab/notebook prose, a Persian unit-cell/circuit schematic and fully localized browser controls and interpretation. Numerical notebook plot labels remain shared; Persian captions explain each panel.

Chapter 8 has paired chapter/guide/lab/notebook prose, an original Persian geometry schematic and a fully localized four-tab browser lab. All scientific code and saved numerical data remain shared.

All ten chapter drafts now have English and Persian editions. Chapter 9 shares its scientific code, saved synthetic observations and uncertainty samples between editions. Further experimental and advanced numerical lab outlines still require implementation and instructor review.
