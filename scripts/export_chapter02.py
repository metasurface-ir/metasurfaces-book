"""Export saved Chapter 2 plots, editable explorer, and standalone lab bundle."""
import base64
import hashlib
import json
from pathlib import Path
import zipfile
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'simulations'))
from source_provenance import check_reference
notebook=json.loads((ROOT/'notebooks/02-waves-and-interfaces.ipynb').read_text(encoding='utf-8'))
destination=ROOT/'assets/chapter-02';destination.mkdir(parents=True,exist_ok=True)
figures={'ch02-interface':'interface-power.png','ch02-tir':'tir-field.png',
         'ch02-film':'film-interference.png','ch02-polarization':'polarization.png',
         'ch02-sheet':'sheet-response.png','ch02-retrieval-conditioning':'retrieval-conditioning.png'}
for tag,name in figures.items():
    cells=[c for c in notebook['cells'] if tag in c.get('metadata',{}).get('tags',[])]
    assert len(cells)==1 and cells[0].get('execution_count') is not None
    images=[o['data']['image/png'] for o in cells[0].get('outputs',[]) if 'image/png' in o.get('data',{})]
    assert len(images)==1
    data=images[0]
    (destination/name).write_bytes(base64.b64decode(''.join(data) if isinstance(data,list) else data))
reference=json.loads((ROOT/'data/chapter-02/waves-reference.json').read_text(encoding='utf-8'))
assert hashlib.sha256((ROOT/'simulations/waves_interfaces.py').read_bytes()).hexdigest()==reference['metadata']['source_sha256']
audit=json.loads((ROOT/'data/chapter-02/validation.json').read_text(encoding='utf-8'))
assert audit['status']=='passed'
assert audit['source_sha256']==reference['metadata']['source_sha256']
check_reference(reference, ROOT/'notebooks/02-waves-and-interfaces.ipynb')
assert all(audit['provenance'][key]==reference['metadata'][key] for key in audit['provenance']), 'Audit and data provenance differ.'
(ROOT/'interactives/waves-explorer.html').write_text((ROOT/'templates/waves-explorer.html').read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
files=['notebooks/02-waves-and-interfaces.ipynb', 'simulations/waves_interfaces.py', 'simulations/source_provenance.py', 'scripts/validate_chapter02.py', 'requirements-labs.txt', 'data/chapter-02/README.md', 'data/chapter-02/waves-reference.json', 'data/chapter-02/waves-reference.csv', 'data/chapter-02/validation.json']
with zipfile.ZipFile(ROOT/'downloads/chapter-02-waves.zip','w',compression=zipfile.ZIP_DEFLATED) as archive:
    for file in files:archive.write(ROOT/file,file)
    archive.writestr('START-HERE.md','''# Chapter 2: waves, interfaces, and sheets

Extract the complete ZIP and preserve notebooks/, simulations/, scripts/, data/,
and assets/. Browser labs are hosted on the book website.

For Python, use Python 3.12 in a virtual environment. Install requirements-labs.txt
and open notebooks/02-waves-and-interfaces.ipynb in JupyterLab. Restart its kernel
and run all cells. NumPy and Matplotlib perform these calculations on a CPU;
the shared requirements also support later course notebooks. No commercial
solver, GPU, or downloaded dataset is required after installing the environment.
Run python scripts/validate_chapter02.py from this extracted root for the audit.

The calculations are exact restricted planar interface/film/electric-sheet and
Jones models. They do not discretize a patterned metasurface or validate a
fabricated device. Preserve the time/basis/reference-plane conventions and model
limitations when modifying results. The film and electric sheet are distinct
models, and arbitrary film coefficients cannot be retrieved as a zero-thickness
electric shunt without validating the model and phase planes first.
''')
print('Exported six figures, offline explorer, and chapter-02-waves.zip')
