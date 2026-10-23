"""Export six original notebook plots and a Python/notebook source bundle."""
import base64
import json
from pathlib import Path
import zipfile
from render_design_studies import render

ROOT=Path(__file__).resolve().parents[1]
figures={
    '09-dispersion.ipynb': {'ms09-spectrum':'chapter-05/dispersion-spectrum.png','ms09-diagnostics':'chapter-05/dispersion-diagnostics.png'},
    '10-coupling.ipynb': {'ms10-comparison':'chapter-03/coupling-comparison.png','ms10-field':'chapter-03/coupling-field.png'},
    '11-inverse-design.ipynb': {'ms11-search':'chapter-10/inverse-search.png','ms11-checks':'chapter-10/inverse-checks.png'}}
audit=json.loads((ROOT/'data/design-studies/validation.json').read_text(encoding='utf-8'))
assert audit['status']=='passed'
for notebook,tags in figures.items():
    nb=json.loads((ROOT/'notebooks'/notebook).read_text(encoding='utf-8'))
    for tag,name in tags.items():
        cells=[c for c in nb['cells'] if tag in c.get('metadata',{}).get('tags',[])]
        assert len(cells)==1 and cells[0].get('execution_count') is not None
        images=[o['data']['image/png'] for o in cells[0].get('outputs',[]) if 'image/png' in o.get('data',{})]
        assert len(images)==1
        image=images[0]
        (ROOT/'assets'/name).write_bytes(base64.b64decode(''.join(image) if isinstance(image,list) else image))
render(ROOT/'interactives/design-studies.html')
files=['notebooks/'+n for n in figures]
files += ['simulations/'+n for n in ['design_studies.py','unit_cell_te.py','metasurface_synthesis.py']]
files += ['scripts/validate_design_studies.py','requirements-labs.txt','requirements-validation.txt',
          'assets/chapter-05/supercell-geometry.svg']
files += [p.relative_to(ROOT).as_posix() for p in (ROOT/'data/design-studies').glob('*') if p.is_file()]
with zipfile.ZipFile(ROOT/'downloads/design-studies.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
    for name in files: archive.write(ROOT/name,name)
    archive.writestr('START-HERE.md','''# Computational labs ms-09, ms-10, ms-11

Extract the whole archive and preserve notebooks/, simulations/, data/, scripts/.
Use Python 3.12, install requirements-labs.txt and launch JupyterLab from this
folder. Restart and run 09-dispersion.ipynb, 10-coupling.ipynb, then
11-inverse-design.ipynb. Figures and results regenerate from the exposed inputs.
One BLAS thread is recommended for these small matrices. CPU only.

Install requirements-validation.txt to run the optional grcwa comparison.
Without it, the inverse notebook records that check as unexecuted. The published
reference includes it. Run python scripts/validate_design_studies.py --grcwa
after the notebooks. The validator checks the fixed published configuration;
edited physical parameters require new convergence and acceptance criteria.

Browser labs are available online at:
https://metasurface-ir.github.io/metasurfaces-book/dispersion-lab/
https://metasurface-ir.github.io/metasurfaces-book/coupling-lab/
https://metasurface-ir.github.io/metasurfaces-book/inverse-design-lab/

Restricted 1D lossless TE periodic ridges. Real constant indices; no measured
material dispersion, finite devices, FEM/FDTD or experiment. All plots and
geometry views are original. Retain assumptions, references and provenance.
''')
print('Exported six original plots, browser explorer and Python/notebook bundle')
