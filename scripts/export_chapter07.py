"""Export saved Chapter 7 plots and source bundle; no simulation is run here."""
from bundle_notices import write_notices
import base64
import json
from pathlib import Path
import zipfile
from render_tunable_explorer import render

ROOT = Path(__file__).resolve().parents[1]
nb = json.loads((ROOT/'notebooks/07-tunable-metasurfaces.ipynb').read_text(encoding='utf-8'))
destination = ROOT/'assets/chapter-07'
destination.mkdir(parents=True, exist_ok=True)
for name in ('tuning', 'array', 'feedback', 'dynamics'):
    cells = [c for c in nb['cells'] if f'ch07-{name}' in c.get('metadata', {}).get('tags', [])]
    assert len(cells) == 1 and cells[0].get('execution_count') is not None
    images = [o['data']['image/png'] for o in cells[0].get('outputs', []) if 'image/png' in o.get('data', {})]
    assert len(images) == 1
    encoded = images[0]
    (destination/f'{name}.png').write_bytes(base64.b64decode(''.join(encoded) if isinstance(encoded, list) else encoded))
render(ROOT/'interactives/tunable-explorer.html')
files = ['notebooks/07-tunable-metasurfaces.ipynb', 'simulations/tunable_surface.py',
         'scripts/validate_chapter07.py', 'requirements-labs.txt',
         'data/chapter-07/validation.json', 'data/chapter-07/reference.json',
         'assets/chapter-07/tunable-cell.svg']
with zipfile.ZipFile(ROOT/'downloads/chapter-07-tunable.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    write_notices(archive)
    for name in files:
        archive.write(ROOT/name, name)
    archive.writestr('START-HERE.md', '''# Chapter 7: tuning, coding and feedback

Extract the complete ZIP and keep its folders. Use Python 3.12, create a virtual
environment, install requirements-labs.txt, and launch JupyterLab. Restart and
run notebooks/07-tunable-metasurfaces.ipynb from the extracted folder structure.
Run python scripts/validate_chapter07.py for the fixed reference audit.
The audit checks its declared reference cases, not every parameter you may edit.
Preserve the reference data before rerunning: the notebook writes reference.json.

The model is an assigned effective impedance, prescribed scalar array, synthetic
noiseless feedback and slow modulation envelope. The drawing is schematic; no
physical patch, diode or fabricated device has been simulated or measured.
Array intensity and envelope harmonic weights are not device efficiencies.
The browser lab is available on the book website.
''')
print('Exported four saved plots, the tunable explorer, and the Chapter 7 source bundle')
