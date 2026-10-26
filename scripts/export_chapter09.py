"""Export saved notebook figures, bilingual-ready browser lab and source archive."""
import base64,json,zipfile
from pathlib import Path
from render_measurement_explorer import render
ROOT=Path(__file__).resolve().parents[1]
nb=json.loads((ROOT/'notebooks/09-fabrication-measurement.ipynb').read_text(encoding='utf-8'))
out=ROOT/'assets/chapter-09';out.mkdir(parents=True,exist_ok=True)
for name in ('materials','tolerance','calibration','uncertainty'):
    cells=[c for c in nb['cells'] if 'ch09-'+name in c.get('metadata',{}).get('tags',[])]
    assert len(cells)==1 and cells[0].get('execution_count') is not None
    png=[o['data']['image/png'] for o in cells[0].get('outputs',[]) if 'image/png' in o.get('data',{})]
    assert len(png)==1
    value=png[0];(out/(name+'.png')).write_bytes(base64.b64decode(''.join(value) if isinstance(value,list) else value))
render(ROOT/'interactives/measurement-explorer.html')
files=['notebooks/09-fabrication-measurement.ipynb','simulations/materials_measurement.py','scripts/validate_chapter09.py',
       'requirements-labs.txt','data/chapter-09/reference.json','data/chapter-09/validation.json',
       'data/chapter-09/synthetic-sweep.csv','assets/chapter-09/measurement-geometry.svg']
with zipfile.ZipFile(ROOT/'downloads/chapter-09-measurement.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    for f in files:z.write(ROOT/f,f)
    z.writestr('START-HERE.md','''# Chapter 9: materials, fabrication and measurement

Extract the whole ZIP and preserve folders. Use Python 3.12 in a virtual
environment and install requirements-labs.txt, then open JupyterLab.
Restart and run notebooks/09-fabrication-measurement.ipynb.
Run python scripts/validate_chapter09.py separately from the extracted root.
The audit evaluates declared baseline cases, not every parameter you may change.
Preserve reference.json and synthetic-sweep.csv before editing: the notebook writes them.

ALL observations are synthetic. The material oscillator is illustrative.
The resonator has assigned rates and local geometric scaling, not a solved patch.
Ideal short/load/open standards demonstrate a one-port error box, not free-space
horn calibration. The CSV is noiseless; the notebook separately propagates
characterization, reading and placement uncertainty in Monte Carlo trials.
Browser labs open on the website; this archive contains no browser HTML.
''')
print('Exported four notebook figures, browser evidence and Chapter 9 sources')
