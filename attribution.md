---
title: Sources, licenses, and citation
short_title: Sources and reuse
---

# Sources, licenses, and citation

(reuse-policy)=
## Reuse policy

The instructor has selected **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** for original book prose, figures/schematics and generated datasets, and **[MIT](https://opensource.org/license/mit)** for original software/code cells. The [LICENSE scope](https://github.com/metasurface-ir/metasurfaces-book/blob/main/LICENSE) separates those parts, including mixed notebooks and generated HTML. Both allow adaptation and commercial reuse subject to their terms; credit the source, identify changes for CC BY material, and retain the MIT copyright/permission notice for software. The full notices travel with the source bundles.

Third-party material and dependencies retain their own terms. Citing a paper does not license its figures or text for inclusion. Project names do not imply endorsement or grant trademark rights. Authors retain ownership while granting the applicable license; contributions must be compatible with this policy.

(reuse-provenance)=
## Trace figures and numerical evidence

The [figure inventory](https://github.com/metasurface-ir/metasurfaces-book/blob/main/assets/provenance.json) records the sources and hashes of the original chapter figures. Numerical PNGs come from tagged saved notebook outputs. SVG schematics have editable generators; four geometry views share `templates/model-geometry.js`, and chapter-specific geometry exporters are recorded with their assets. The Persian Chapter 2 and Chapter 9 schematics translate their labels. The inventory contains no reproduced publisher artwork.

The [notebook identity record](https://github.com/metasurface-ir/metasurfaces-book/blob/main/data/notebook-provenance.json) binds saved code, outputs, registered local dependencies/results and explicit parameter fields. Neither inventory proves physical validity, fresh execution, translation quality, or third-party permission. Keep the generating notebook, parameters, reference planes, model limits and exact source commit with a reused result. Computation remains authoritative here; the companion site can link to the relevant numerical source.

(reuse-third-party)=
## Record imported material before publication

Use the [third-party record template](https://github.com/metasurface-ir/metasurfaces-book/blob/main/templates/third-party-record.md). Record creator, direct source, version/retrieval date, checksum, actual license or permission, required credit and modifications. For a material dataset, add units, measurement conditions, band, uncertainty and the original observations; a fitted curve is a derived result.

Write original explanations, cite primary scientific sources and verify bibliographic details. Retain required notices alongside any imported material. An openly readable paper or downloadable image is not automatically reusable under this book's license. Resolve uncertain permissions with the instructor before including that specific material. Do not upload private permission correspondence or credentials.

(reuse-citation)=
## Cite a reproducible version

Use [CITATION.cff](https://github.com/metasurface-ir/metasurfaces-book/blob/main/CITATION.cff) for machine-readable citation metadata and [VERSION](https://github.com/metasurface-ir/metasurfaces-book/blob/main/VERSION) for the snapshot label. Cite the exact Git commit and notebook/data path when reporting a numerical result. No DOI or peer-reviewed status is implied by a snapshot label. The deployed [build identity](https://metasurface-ir.github.io/metasurfaces-book/build-info.json) records the source revision used for the site.

Example: *Metasurface.ir contributors. Metasurface.ir: Metasurfaces — From Wave Physics to Design. Snapshot [VERSION], commit [full SHA], notebook [path], accessed [date].* Replace brackets with the actual version used, not a moving `main` link alone.

(reuse-credit)=
## Contributor and assistance credits

See [CONTRIBUTORS.md](https://github.com/metasurface-ir/metasurfaces-book/blob/main/CONTRIBUTORS.md) and the Git/PR history for credits. Students should supply their preferred public name and role. Cited researchers are credited for their scientific work and are not implied to endorse or review this book.

Describe AI assistance in each PR and record actual checks of equations, citations, code and results. AI tools are not human authors. Scientific and editorial acceptance remains the instructor's responsibility; saved outputs or an automated build do not replace that review.
