"""Inventory book-owned images and require each numerical PNG to match a notebook.

Run after figure exports. --check verifies the committed inventory without edits.
This records generation provenance, not a blanket copyright clearance.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def inventory():
    outputs = {}
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        notebook = json.loads(path.read_text(encoding='utf-8'))
        for i, cell in enumerate(notebook['cells']):
            for output in cell.get('outputs', []):
                encoded = output.get('data', {}).get('image/png')
                if encoded is None: continue
                raw = base64.b64decode(''.join(encoded) if isinstance(encoded, list) else encoded)
                key = hashlib.sha256(raw).hexdigest()
                outputs.setdefault(key, []).append(dict(notebook=path.relative_to(ROOT).as_posix(),
                    cell_index=i, tags=cell.get('metadata', {}).get('tags', [])))
    rows = []
    for path in sorted((ROOT/'assets').glob('chapter-*/*')):
        if path.suffix not in ('.png', '.svg'): continue
        key = hashlib.sha256(path.read_bytes()).hexdigest()
        row = dict(asset=path.relative_to(ROOT).as_posix(), sha256=key)
        if path.suffix == '.png':
            assert key in outputs, f'PNG does not match a saved notebook output: {path}'
            row.update(origin='original numerical notebook output', generators=outputs[key])
        else:
            tree = ET.parse(path)
            assert not any(el.tag.endswith('image') for el in tree.iter()), 'Embedded raster image in schematic'
            row.update(origin='original editable SVG schematic', source=row['asset'])
        rows.append(row)
    return dict(scope='generation paths of book-owned chapter images; not a general reuse license', assets=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    current = inventory()
    path = ROOT/'assets/provenance.json'
    if args.check:
        assert json.loads(path.read_text(encoding='utf-8')) == current, 'Regenerate figure provenance after exports'
    else:
        path.write_text(json.dumps(current, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f"Verified original-source correspondence for {len(current['assets'])} chapter images")
