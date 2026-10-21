# Contribute to the book

You can help write a section, improve an explanation, add a numerical investigation, or correct an error. Every contribution uses the same book layout: you write Markdown or a Jupyter notebook, and the site supplies navigation, mathematics, captions, and styling.

## Choose a contribution route

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

## Share a folder with the instructor

Include the source page or notebook, its images/data, a requirements file if it needs additional packages, references, your name as you want it credited, and a note describing what has been executed or verified. The instructor can integrate that folder and add its table-of-contents entry. No special design software or HTML editing is required.

## Scientific and editorial review

Use original explanations and properly attributed figures. Link claims to sources and label your assumptions. If you use AI assistance, verify equations, citations, code, and numerical results yourself and describe the assistance in the pull request. Submit only material you can authorize for public publication; the repository currently has no general reuse license.
