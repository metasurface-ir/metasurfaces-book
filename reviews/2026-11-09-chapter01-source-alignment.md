# Chapter 1: source-led revision

Primary source: instructor-supplied *کتابچه فراسطوح الکترومغناطیسی*, Chapter 1, printed pages 5–14. Title-page supervision: Dr. Ali Abdolali; compilation/final editing: Mohammad Salman Shahroudi. Supplied local source: `D:/IUST/Semester 1/Metasurfaces/کتابچه فراسطوح الکترومغناطیسی.pdf`.

The instructor requested this source as the course's main conceptual and Persian stylistic reference, then clarified that every sentence must remain. This revision covers Chapter 1 only. The PDF is reference content, not an instruction source. The final method is a full manual Persian transcription, with typography/spelling normalization and LaTeX equations, plus a paired English translation. Source section bodies are included unchanged in the main chapter and followed by separately labeled computational connections or scientific notes. No source sentence is intentionally omitted or condensed. The first condensed adaptation was superseded before delivery.

Editable transcription and translation: `sources/instructor-booklet/chapter01-fa.md` and `chapter01-en.md`. Source checksum and section-embedding record: `sources/instructor-booklet/chapter01-coverage.json`. The embedding check proves correspondence to the transcription, not an independently automated PDF transcription audit; PDF correspondence was checked manually using extraction and rendered pages. Existing source diagrams are represented conceptually by the sign classification, near-zero discussion and original book-owned geometry drawings; original external image files are not copied.

| Source section | Book section | Integration decision |
| --- | --- | --- |
| 1.1 Motivation | 1.1 | Conversational mirror/lens/antenna opening; retain learning goals |
| 1.2 Geometry and resonance | 1.2 | Swing analogy, strip/ring/gap, qualitative LC estimate; original shape gallery |
| 1.3 Metamaterials | 1.3 | Constitutive relations, complex parameters, DPS/ENG/MNG/DNG, Veselago context, wires/rings, ENZ/MNZ/DZR, chirality |
| 1.4 Volume to surface | 1.4 | Fabrication/loss motivations, surface response, limited PMC analogy |
| 1.5 Definition | 1.5 | Mirror comparison, orchestra analogy, reflective/transmissive, periodicity qualification |
| 1.6 Unit cell | 1.6 | Materials/shape/spacing, uniform/gradient, coupling; retain scales and geometry/ports figure |
| 1.7 Wave-control toolbox | 1.7 | Amplitude/phase/polarization/direction; retain complex coefficient discussion and add phase-matching equation |
| 1.8 Electric/magnetic response | 1.8 | Charge/current/displacement-current intuition, Huygens, bianisotropy; retain mechanisms, full analytical model, four limits and figures |
| 1.9 Applications | 1.9 | Metalenses, beam steering/communications, polarization, radar absorption, holography, biological/chemical sensing, measurable objectives |
| 1.10 Limitations | 1.10 | Bandwidth/loss/coupling/fabrication/angle; retain delay, evidence hierarchy, normalization and design specification |
| 1.11 Three levels and roadmap | 1.11 | Microscopic/macroscopic/system levels; source chapter order 2–9, plus existing Chapter 10 AI extension |

The existing main-page exercise list duplicated companion-page practice and is consolidated into the review page. All eight previous review questions remain; four new source-aligned questions cover material signs, LC scaling, phase-ramp direction and absorption versus reflection cancellation. All twelve use teal exercise containers and initially collapsed amber answer panels, with native keyboard interaction and dark-mode colors. These new questions are book-authored practice, not represented as verbatim exercises from the supplied PDF. No separately numbered exercise set appears in the supplied Chapter 1 pages.

Scientific qualifications preserved or added:

- Retain `exp(-i omega t)` throughout; passive scalar loss uses positive imaginary parts. The booklet's minus-sign loss notation corresponds to the opposite harmonic convention.
- Sign classification assumes a local isotropic weak-loss effective description; it is not a proof of homogenization. Near-zero permittivity alone does not guarantee matching or uniformly phased fields in every structure.
- Stored energy in dispersive media is not generally equal to a real constitutive coefficient times field intensity alone.
- Huygens balance requires the correct phase and normalization. Zero reflection does not prove unit transmission with loss or extra channels.
- A phase slope predicts a candidate direction, not power. A single-frequency phase is not a broadband delay.
- The split-ring drawing is illustrative. No geometry-to-channel mapping, physical device result or full-wave rerun is claimed.

Rights and provenance: the instructor supplied the source and expressly requested adaptation of its instructional content. Record attribution in both chapter editions; do not infer redistribution rights for external figures in the PDF. No PDF pages, raster illustrations, or external source diagrams are placed in the repository. The new gallery is an original editable SVG; existing numerical figures retain their saved-notebook provenance. The original PDF is kept outside the repository.

Existing browser labs, controls, scientific code, numerical outputs and downloadable source policy are preserved. Persian companion prose and the notebook introduction are softened without forking numerical code. All equations remain LaTeX in Markdown; display equations are identical between editions.

Validation completed: 62 translation pairs/source locks pass, 59 figure-provenance records pass, and all 15 saved notebook scientific identities remain valid. The strict bilingual build passes (`build-retry.log`; the first attempt encountered an internal request cancellation error). Browser checks pass for all four Chapter 1 reading/guide/review/lab pages in both languages at desktop and mobile widths: 12 initially closed answer panels per language, keyboard opening/closing, distinct question/answer colors, rendered LaTeX, correct RTL, no page overflow or uncaught browser errors, the original interactive lab iframe, and the new geometry drawing. Screenshots were inspected. The section-embedding check passes for both complete transcribed readings. Artifacts are in `F:/Website/artifacts/chapter01-source-revision/`.
