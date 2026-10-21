"""Copy the Chapter 4 notebook's tagged, executed PNG outputs into chapter assets.

Run after restarting, executing, and saving the notebook:
    python scripts/export_chapter04_figures.py
Only Python's standard library is required. This does not execute the notebook.
"""
import base64
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
nb = json.loads((root/'notebooks/04-floquet-orders.ipynb').read_text(encoding='utf-8'))
destination = root/'assets/chapter-04'
destination.mkdir(parents=True, exist_ok=True)
for tag, filename in {'ch04-channel-maps': 'channel-maps.png', 'ch04-finite-array': 'finite-array.png'}.items():
    cells = [c for c in nb['cells'] if tag in c.get('metadata', {}).get('tags', [])]
    if len(cells) != 1 or cells[0].get('execution_count') is None:
        raise ValueError(f'Expected one executed cell tagged {tag}')
    images = [o['data']['image/png'] for o in cells[0].get('outputs', []) if 'image/png' in o.get('data', {})]
    if len(images) != 1:
        raise ValueError(f'Expected one saved plot for {tag}')
    data = images[0]
    (destination/filename).write_bytes(base64.b64decode(''.join(data) if isinstance(data, list) else data))
    print((destination/filename).relative_to(root))
