"""Export Chapter 1 notebook figures, standalone explorer, and source bundle."""
from bundle_notices import write_notices
import base64
import hashlib
import json
from pathlib import Path
import zipfile
from geometry_assets import embed_geometry

ROOT=Path(__file__).resolve().parents[1]
n=json.loads((ROOT/'notebooks/01-first-metasurface-model.ipynb').read_text(encoding='utf-8'))
destination=ROOT/'assets/chapter-01';destination.mkdir(parents=True,exist_ok=True)
for tag,name in {'ch01-response':'response.png','ch01-phasors':'phasors.png','ch01-delay':'delay.png'}.items():
    cells=[c for c in n['cells'] if tag in c.get('metadata',{}).get('tags',[])]
    assert len(cells)==1 and cells[0].get('execution_count') is not None
    images=[o['data']['image/png'] for o in cells[0].get('outputs',[]) if 'image/png' in o.get('data',{})]
    assert len(images)==1
    data=images[0];(destination/name).write_bytes(base64.b64decode(''.join(data) if isinstance(data,list) else data))
reference=json.loads((ROOT/'data/chapter-01/sheet-response.json').read_text())
assert hashlib.sha256((ROOT/'simulations/intro_sheet.py').read_bytes()).hexdigest()==reference['metadata']['source_sha256']
(ROOT/'interactives/foundations-explorer.html').write_text(embed_geometry((ROOT/'templates/foundations-explorer.html').read_text(encoding='utf-8')),encoding='utf-8')
files=['notebooks/01-first-metasurface-model.ipynb', 'simulations/intro_sheet.py', 'requirements-labs.txt', 'scripts/validate_chapter01.py', 'data/chapter-01/README.md', 'downloads/chapter-01-report-template.md', 'data/chapter-01/sheet-response.json', 'data/chapter-01/sheet-response.csv', 'data/chapter-01/validation.json', 'assets/chapter-10/analytical-sheet.svg']
with zipfile.ZipFile(ROOT/'downloads/chapter-01-foundations.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
    write_notices(archive)
    for file in files:archive.write(ROOT/file,file)
    archive.writestr('START-HERE.md','''# Chapter 1 source bundle

Extract the complete ZIP. Use Python 3.12 and install requirements-labs.txt in
a virtual environment, then launch JupyterLab. Open the notebook in notebooks/
and restart/run all cells. Preserve simulations/ and data/ alongside notebooks/.
The model needs NumPy/Matplotlib only; the shared requirements also support the
later course labs. It runs without a commercial solver, GPU, or network dataset.
Run python scripts/validate_chapter01.py from this folder for analytical checks.

This is a lossless equal-impedance specular sheet model, not a full-wave device.
Preserve that model label and its assumptions when sharing or editing results.
''')
print('Exported three figures, an offline explorer, and chapter-01-foundations.zip')
