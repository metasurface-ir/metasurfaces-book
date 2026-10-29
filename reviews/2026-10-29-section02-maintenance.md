# Section 2 — Documentation, bilingual workflow, and site maintenance

Scope: G1–G8 of the 27 October whole-book review. Section 1 was deployed separately in PR #22. This patch does not implement the Section 3 scientific learning expansions.

| Finding | Change |
| --- | --- |
| G1 — Publication status | Corrected Chapters 1/6, overview/project wording, translation counts and README; developed chapters and still-unexecuted extensions remain distinguished in both languages. |
| G2 — Downloads | Setup distinguishes hosted browser labs, complete Python source bundles, standalone notebooks and full-repository exporters. Browser HTML remains excluded from downloadable bundles. |
| G3 — Bilingual workflow | Aligned setup and contribution guides with all 15 notebook dependencies, order, measured runtimes, audits, exports, source/translation registration, shared numerical code, review and PR/publication steps. Added Persian contribution templates. |
| G4 — Validation | Added CI parameter-edit regressions and saved notebook code/output/dependency/result identities, including explicit parameter fields. Narrowed the Chapter 2 browser parity claim and added paired help-page section/anchor checks. Fresh execution and scientific/translation review remain separate requirements. |
| G5 — Learning infrastructure | Added the bilingual prerequisite map and ms-12 capstone brief: proposal, baseline, milestones, computational budget/stopping rules, evidence rubric and reproducibility deliverables. Expanded the glossary and notation/conventions table. |
| G6 — Navigation | Profiled Chapter 2/4 language switches before changes. Added shared section labels and language links to nearby/explicit sections; kept nested-prefix full navigation. Limited interface translation work to known controls. An experimental earlier startup caused a React hydration error in extended testing and was removed; the verified load grace period is retained. |
| G7 — Reuse and citation | With the instructor's delegated choice, added CC BY 4.0 for original content/figures/generated data and MIT for original code. Added scope/full notices, CITATION.cff, contributor/assistance credits, VERSION, build-info.json and a third-party source/permission record template. All source-bundle exporters attach notices and citation metadata. |
| G8 — Interface translation | Replaced the body-wide text walker with explicit interface roots. Scientific prose, cited titles and search-result excerpts are excluded from theme-word replacement. |

## Evidence and limits

All 15 notebooks were executed from fresh kernels on 28 October; Chapter 6 was executed again after its benchmark audit regenerated inputs. The chapter audits and the combined design-study audit passed, including the optional grcwa comparisons. These support the models stated in the book, not experimental or unrestricted full-wave device validity.

The 16 regression tests pass. Saved-artifact identities cover all 15 notebooks and their registered file dependencies/results; recording a hash does not prove execution or scientific correctness. The 62 English–Persian pairs and 58 original chapter-image provenance entries pass their automated checks. CITATION.cff passes the official Citation File Format schema. Source locks record reviewed source changes and shared-code parity, not certified Persian semantic equivalence.

Local evidence files are in `F:/Website/artifacts/section02-maintenance/`; the files are development artifacts, not portable student dependencies.

The final strict bilingual build passes. All 18 source ZIPs linked from the built editions contain matching scientific code, the content/code license notices and citation/credit/version files, with no browser HTML. The Chapter 2 audit also passes after extracting each language's bundle. The built-HTML scan found 4,162 internal link/image/iframe targets and no missing files. The local build identity correctly marks the uncommitted working tree as modified; CI will identify its exact checked-out commit.

Final local browser checks pass for all 124 book page URLs and 16 rendered pages across English/Persian. The selected setup, contribution, glossary, learning-path, capstone, attribution and Chapter 2/4 pages have no detected equation errors, missing image alt attributes, page-wide overflow at 390 px or uncaught page errors. Shared Chapter 2/4 sections survive switches in both directions. English and Persian search preserve the title “Light Propagation with Phase Discontinuities,” keep language-prefixed result routes, and support returning from a result without uncaught page errors. Selected mobile screenshots were inspected; the capstone title was aligned with its page heading to avoid duplication.

### Navigation observations

The same local project-prefix server and browser harness measured three switches per target language on each large page. The quantity is click-to-restored-language-control time, including document navigation. Runs were made before and after the changes; cache state and other machine activity can affect these small samples.

| Page / target language | Before median | After median |
| --- | --- | --- |
| Chapter 2 / Persian | 2,074 ms | 1,703 ms |
| Chapter 2 / English | 1,871 ms | 1,421 ms |
| Chapter 4 / Persian | 2,708 ms | 1,718 ms |
| Chapter 4 / English | 1,980 ms | 1,620 ms |

These are local observations, not a controlled performance study or a promise for GitHub Pages. Full document navigation remains deliberate because each edition has a separate router and the Persian edition needs its nested prefix. The final code retains the proven load/hydration grace period; less interface-scanning work and shared section links were retained, while the unsafe earlier-start experiment was discarded. Splitting chapters is not justified by these limited measurements alone.

## Remaining scope

Scientific/editorial acceptance, translation terminology refinements and course assessment weights remain instructor decisions. The browser checks are targeted regression checks, not a complete accessibility certification. Section 3 and later review sections remain untouched.
