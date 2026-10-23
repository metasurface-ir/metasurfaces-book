"""Export saved notebook figures, explorer data, and a Chapter 3 source bundle.

Run after saving the executed notebook and numerical audit. Standard library only.
The explorer embeds saved data and does not run RCWA in the browser.
"""
import base64
import hashlib
import json
from pathlib import Path
import zipfile
from geometry_assets import embed_geometry

ROOT = Path(__file__).resolve().parents[1]
nb = json.loads((ROOT/'notebooks/03-unit-cell-library.ipynb').read_text(encoding='utf-8'))
destination = ROOT/'assets/chapter-03'
destination.mkdir(parents=True, exist_ok=True)
for tag, name in {'ch03-fields':'fields.png', 'ch03-library':'library.png', 'ch03-spectra':'spectra.png'}.items():
    cells = [c for c in nb['cells'] if tag in c.get('metadata', {}).get('tags', [])]
    assert len(cells) == 1 and cells[0].get('execution_count') is not None
    images = [o['data']['image/png'] for o in cells[0].get('outputs', []) if 'image/png' in o.get('data', {})]
    assert len(images) == 1
    data = images[0]
    (destination/name).write_bytes(base64.b64decode(''.join(data) if isinstance(data, list) else data))
library_path = ROOT/'data/chapter-03/response-library.json'
library = json.loads(library_path.read_text())
assert library['metadata']['source_sha256'] == hashlib.sha256((ROOT/'simulations/unit_cell_te.py').read_bytes()).hexdigest()
template = embed_geometry((ROOT/'templates/unit-cell-explorer.html').read_text(encoding='utf-8'))
assert template.count('__CH03_LIBRARY_DATA__') == 1
(ROOT/'interactives/unit-cell-explorer.html').write_text(template.replace('__CH03_LIBRARY_DATA__', json.dumps(library, separators=(',', ':'))), encoding='utf-8')
files = ['notebooks/03-unit-cell-library.ipynb', 'simulations/unit_cell_te.py',
         'requirements-labs.txt', 'requirements-validation.txt', 'scripts/validate_chapter03.py',
         'data/chapter-03/response-library.json', 'data/chapter-03/response-library.csv',
         'data/chapter-03/validation.json', 'data/chapter-03/README.md',
         'interactives/unit-cell-explorer.html', 'assets/chapter-03/unit-cell-geometry.svg']
download = ROOT/'downloads/chapter-03-unit-cell.zip'
download.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(download, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for file in files:
        archive.write(ROOT/file, file)
    archive.writestr('START-HERE.md', '''# Chapter 3 source bundle

Extract the entire ZIP. Use Python 3.12. From this folder:

    python -m venv .venv
    .venv/Scripts/python -m pip install -r requirements-labs.txt
    .venv/Scripts/python -m jupyterlab notebooks

On macOS/Linux replace .venv/Scripts/python with .venv/bin/python.
Open 03-unit-cell-library.ipynb; restart its Python kernel and run all cells.
The notebook finds simulations/unit_cell_te.py from this folder structure.
It regenerates response-library.json and .csv in data/chapter-03/.
The saved validation.json describes the published reference, not your edited run.
After editing, rerun scripts/validate_chapter03.py. For its optional --grcwa
comparison also install requirements-validation.txt. See the data README.
''')
print('Exported three figures, an embedded-data explorer, and', download.relative_to(ROOT))
