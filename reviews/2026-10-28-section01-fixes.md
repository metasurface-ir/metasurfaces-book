# Section 1 reliability fixes — 28 October 2026

This patch addresses the 14 confirmed scientific/software findings in Section 1 of the 27 October whole-book review. The English and Persian notebooks share identical numerical code. The published reference outputs, figures, data, audit reports, and source bundles were regenerated where affected.

## Findings and resolutions

| Finding | Resolution | Regression evidence |
| --- | --- | --- |
| F3 — Chapter 1 frequency edit | Separate the fixed 200 THz zero-transmission fixture from the edited experiment. The saved-result audit uses the recorded frequency and parameters and requires undefined phase only below the amplitude threshold. | At 180 THz the notebook finishes and records the valid electric-only phase, approximately 49.820766°. An incorrectly null saved phase is rejected. |
| F2 — Chapter 2 film and field regime | Keep a separate quarter-wave regression. Apply conservation to the edited film and derive field labels and flux checks from the actual propagation regime. | A 10% thickness increase gives R ≈ 0.0010186173; a 30° field example is propagating and has transmitted flux ≈ 0.8942272089. |
| F4 — Chapter 2 provenance | Name the simulation-module hash check accurately. Add separate notebook-code, parameter, and result-payload hashes, validate them during audit/export, and include the helper in both source bundles. | Code, parameter, and result tampering are rejected. Narrative translations and saved output changes do not change the code hash. |
| F1 — Chapter 3 oblique reference | Calculate the flat-interface Fresnel expectations from the actual incidence angle and exterior indices. | At 20°, r ≈ −0.2169814125 and t ≈ 0.7830185875 pass. |
| F5 — Chapter 3 multiorder edits | Explicitly restrict this library to a propagating zeroth transmitted order with no additional open or grazing exterior orders. Reject unsupported edits before solving or selecting cells. | The 1.4 μm period and an exact first-order cutoff are rejected with a domain message; an admissible changed-index case passes. This patch does not implement an all-order library. |
| D1 — Chapter 7 parameter propagation | Pass the edited circuit, frequency, and spacing through all beam, dynamics, feedback, and export calculations. Keep physical pitch fixed when frequency changes and record both pitch and normalized spacing. | A changed 150 Ω, exponent-2 circuit at 11 GHz agrees with an independent array sum and exports the same result; spacing becomes 0.55 wavelengths. |
| D4 — Chapter 7 feedback expectation | Derive the equal-capacitance bias from the edited capacitance law. Record target reachability and achieved complex error separately. | Exponent 2 yields approximately 8.52470472 V without a false assertion against the default 9.08 V. |
| D5 — Chapter 7 phase gaps | Mask weak reflection amplitudes, unwrap each connected valid segment separately, export undefined phase as JSON null, and break browser curves at those gaps. | The matched-resonance phase is undefined; disconnected segments do not unwrap across the gap. Browser rendering is checked separately. |
| A1 — Chapter 8 gain consistency | Apply the assigned transmit/receive gains to the aperture channel, far-field comparison, and direct path. Derive affected plot labels from the experiment. Populate browser frequency choices from the exported profile keys, including decimal keys such as `28.0`. | Setting both gains to 10 multiplies each path's power by 100. All three browser frequency choices work in both languages. |
| A2 — Chapter 9 parameter-derived plots | Derive histogram edges and acceptance shading from the sampled distribution and edited specification. Expose frequency-scan offsets and require the scan to bracket the edited resonance. | At 12 GHz with a 0.2 GHz tolerance, all histograms remain finite and integrate to one; the scan brackets and samples 12 GHz. |
| A3 — Chapter 9 degenerate uncertainty | Use rank-aware covariance regions: point, line, or ellipse. Check coverage only in the supported subspace, with an orthogonal roundoff check. | Zero uncertainty produces a finite point with full sample coverage. Rank-one and rank-two Gaussian tests use their respective chi-square thresholds. |
| D2 — ms-09 bandwidth intersection | Interpolate the efficiency and angle constraints independently, then intersect their anchor-connected passing intervals. | A manufactured constraint-switching case returns [1.5, 2.5] μm; the saved 0.213° case has an upper edge of approximately 1.5709596376 μm. |
| D3 — ms-09 angular shading | Use the same angular tolerance for calculation, shading, and legend. | With a 0.213° tolerance, the plotted shaded width is 0.426°. |
| D6 — ms-11 unsuccessful searches | Save optimization history and stopping reasons before refinement checks; retain validation flags and independent-check outcomes without discarding an unsuccessful investigation. Strict reference-success gates remain in the reference auditor. | A one-evaluation search finishes, saves its unsuccessful status and history, records no improvement, and retains refinement and held-out checks. |

## Validation

- The 12 tests in `tests/test_section01_regressions.py` pass; several tests cover more than one finding. These execute edited notebook code in temporary copies without overwriting reference data.
- Nine affected/dependent reference notebooks were executed afresh: Chapters 1, 2, 3, 7, 8, 9 and ms-09, ms-10, ms-11. The coupling notebook was rerun because its shared simulation module changed.
- Chapter 1/2/3/7/8/9 and design-study reference audits pass, including the Chapter 3 and design-study comparisons against `grcwa`.
- All 60 English–Persian page pairs pass the translation/source-lock checks. All 58 chapter-image provenance entries pass.
- The strict bilingual build passes. The final Chapter 8 selector repair was rendered into both local editions and checked against those outputs.
- All 120 book page URLs return HTTP 200 on the local project-prefix preview. All 18 affected/dependent notebook pages pass language-link, image-loading, equation-rendering, and 390 px layout checks, with no uncaught page errors.
- All 20 standalone browser-lab pages pass view-switching, mobile-width, and no-download-control checks. Chapters 7, 8, and 9 additionally pass their detailed control/data and keyboard-tab checks in both languages. Injected missing-phase fixtures confirm curve breaks, undefined readouts, and finite axes even when every phase sample is absent.
- All 18 source ZIPs linked from the built English/Persian lab pages contain matching numerical code and no browser HTML. The Chapter 2 validator also passes after extracting each language's bundle, including its new provenance helper.
- All five changed chapter figures and selected rendered English/Persian screenshots were inspected.

The regression command is `python -m unittest discover -s tests -v` in an environment with `requirements-labs.txt` installed. Setting `OPENBLAS_NUM_THREADS=1` before starting Python keeps the small cases fast. The complete publishing build is `python scripts/build_bilingual.py` with the book environment and its Node/npm dependencies available.

## Limits and scope

The regressions cover the reported parameter edits and selected limiting cases, not every possible combination of edits. Scientific checks establish behavior of the declared analytical, scalar, circuit, and TE RCWA models; they do not establish fabricated-device or unrestricted 3D validity. Provenance hashes detect mismatched saved artifacts, not whether unsaved editor content was executed, and do not replace physical validation. The browser checks are not a complete accessibility certification. Local build and browser checks do not themselves establish a live deployment.

This patch stops at Section 1. Documentation/site maintenance, optional learning additions, and later extensions remain for the instructor's next instruction. Browser laboratories retain the hosted/new-tab workflow; source ZIPs contain executable scientific sources without browser HTML.
