"""Render the bilingual explorer from executed, source-locked Python evidence."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(destination, language='en'):
    assert language in ('en', 'fa')
    data = json.loads((ROOT/'data/chapter-07/reference.json').read_text(encoding='utf-8'))
    audit = json.loads((ROOT/'data/chapter-07/validation.json').read_text(encoding='utf-8'))
    digest = hashlib.sha256((ROOT/'simulations/tunable_surface.py').read_text(encoding='utf-8').encode()).hexdigest()
    assert data['metadata']['source_sha256'] == digest, 'Execute the notebook after changing the model'
    assert audit['status'] == 'passed'
    assert audit['source_sha256'] == digest, 'Validate the current model'
    assert data['metadata']['parameters'] == audit['parameters'], 'Published explorer requires the audited reference parameters'
    template = (ROOT/'templates/tunable-explorer.html').read_text(encoding='utf-8')
    assert template.count('__CH07_DATA__') == 1
    result = template.replace('__CH07_DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'))
    result = result.replace('<html lang="en">', f'<html lang="{language}">', 1)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(result, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    render(ROOT/'interactives/tunable-explorer.html')
