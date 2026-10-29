"""Export only saved notebook figures, a bilingual-ready explorer and source ZIP."""
from bundle_notices import write_notices
import base64,json,zipfile
from pathlib import Path
from render_communications_explorer import render
ROOT=Path(__file__).resolve().parents[1]
nb=json.loads((ROOT/'notebooks/08-communication-links.ipynb').read_text(encoding='utf-8'))
out=ROOT/'assets/chapter-08';out.mkdir(parents=True,exist_ok=True)
for name in ('focus','power','bandwidth','training'):
    cells=[c for c in nb['cells'] if 'ch08-'+name in c.get('metadata',{}).get('tags',[])]
    assert len(cells)==1 and cells[0].get('execution_count') is not None
    png=[o['data']['image/png'] for o in cells[0].get('outputs',[]) if 'image/png' in o.get('data',{})]
    assert len(png)==1
    data=png[0];(out/(name+'.png')).write_bytes(base64.b64decode(''.join(data) if isinstance(data,list) else data))
render(ROOT/'interactives/communications-explorer.html')
files=['notebooks/08-communication-links.ipynb','simulations/communication_link.py','scripts/validate_chapter08.py',
       'requirements-labs.txt','data/chapter-08/reference.json','data/chapter-08/validation.json','assets/chapter-08/link-geometry.svg']
with zipfile.ZipFile(ROOT/'downloads/chapter-08-communications.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    write_notices(z)
    for f in files:z.write(ROOT/f,f)
    z.writestr('START-HERE.md','''# Chapter 8: communication links

Extract the complete ZIP and preserve folders. Use Python 3.12, install
requirements-labs.txt in a virtual environment, and launch JupyterLab.
Restart and run notebooks/08-communication-links.ipynb.
Run python scripts/validate_chapter08.py from the extracted root separately.
The audit evaluates declared baseline cases, not every parameter you may change.
Preserve reference.json before editing: the notebook writes that file.

The model is a scalar projected-aperture approximation with assigned efficiency,
ideal phase states, a single polarization and free-space paths. It is not a
full-wave patterned surface, calibrated hardware, or measured wireless link.
Browser labs open on the book website; no browser HTML is included here.
''')
print('Exported four notebook figures, browser evidence and Chapter 8 sources')
