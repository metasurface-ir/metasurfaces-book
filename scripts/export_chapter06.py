"""Export original saved Chapter 6 figures, bilingual explorer, and source ZIP.

Execute the notebook and validate_chapter06.py before running this script.
This exporter never runs a simulation.
"""
from bundle_notices import write_notices
import base64
import hashlib
import json
from pathlib import Path
import zipfile

from render_numerical_explorer import render

ROOT = Path(__file__).resolve().parents[1]
nb = json.loads((ROOT/'notebooks/06-numerical-methods.ipynb').read_text(encoding='utf-8'))
destination = ROOT/'assets/chapter-06'
destination.mkdir(parents=True, exist_ok=True)
for tag, name in {'ch06-convergence':'convergence.png', 'ch06-fields':'fields.png',
                  'ch06-boundaries':'boundaries.png', 'ch06-harmonics':'harmonics.png'}.items():
    cells = [c for c in nb['cells'] if tag in c.get('metadata', {}).get('tags', [])]
    assert len(cells) == 1 and cells[0].get('execution_count') is not None
    images = [o['data']['image/png'] for o in cells[0].get('outputs', []) if 'image/png' in o.get('data', {})]
    assert len(images) == 1
    data = images[0]
    (destination/name).write_bytes(base64.b64decode(''.join(data) if isinstance(data, list) else data))
reference = json.loads((ROOT/'data/chapter-06/numerical-reference.json').read_text(encoding='utf-8'))
audit = json.loads((ROOT/'data/chapter-06/validation.json').read_text(encoding='utf-8'))
assert audit['status'] == 'passed'
for name, digest in reference['metadata']['source_sha256'].items():
    assert hashlib.sha256((ROOT/'simulations'/name).read_bytes()).hexdigest() == digest
render(ROOT/'interactives/numerical-explorer.html', language='en')
files = ['notebooks/06-numerical-methods.ipynb', 'simulations/numerical_methods.py', 'simulations/waves_interfaces.py', 'simulations/unit_cell_te.py', 'scripts/validate_chapter06.py', 'requirements-labs.txt', 'data/chapter-05/beam-steering.json', 'data/chapter-05/validation.json', 'assets/chapter-06/slab-geometry.svg']
files += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'data/chapter-06').glob('*')) if p.is_file()]
with zipfile.ZipFile(ROOT/'downloads/chapter-06-numerical.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    write_notices(archive)
    for name in files: archive.write(ROOT/name, name)
    archive.writestr('START-HERE.md', '''# Chapter 6 numerical methods

Extract the complete ZIP and preserve its folders. With Python 3.12 create a
virtual environment, install requirements-labs.txt, and launch JupyterLab.
Restart and run notebooks/06-numerical-methods.ipynb. It imports the simulations/
modules and reads the explicitly labeled fixed RCWA data. Modified slab
parameters generate a separate data/chapter-06/notebook-experiment.json.

Run python scripts/validate_chapter06.py from the extracted root for the fixed
benchmark audit. It writes reference data and a validation report. A successful
reference audit does not certify a newly modified physical configuration.
The browser explorer is hosted on the book website and selects saved data.

This is a 1D lossless equal-exterior FDFD slab with a discrete radiation boundary.
It is not FDTD, FEM, PML, finite-device or experimental validation. The separate
RCWA companion is a restricted periodic TE calculation. Keep its model labels,
reference planes, conventions, scope and source provenance when sharing results.
''')
print('Exported four figures, numerical explorer, and Chapter 6 source ZIP')
