"""Check translation correspondence, shared code, and source review locks."""
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    # Git checkouts on Windows/Linux must have the same textual source identity.
    text = path.read_text(encoding='utf-8').replace('\r\n', '\n')
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def validate():
    manifest = json.loads((ROOT / 'translations/languages.json').read_text(encoding='utf-8'))
    lock = json.loads((ROOT / 'translations/source-lock.json').read_text(encoding='utf-8'))
    for path, reviewed in lock.items():
        assert digest(ROOT / path) == reviewed, f'English source changed; review the translation and update source-lock.json: {path}'
    routes = set()
    for row in manifest['pages']:
        source, translated = ROOT / row['source'], ROOT / row['translation']
        assert source.is_file() and translated.is_file(), f'Missing translation pair: {row}'
        assert row['route'] not in routes, 'Duplicate translation URL'
        routes.add(row['route'])
        assert digest(source) == lock[row['source']], f'English source changed; review Persian translation and update source-lock.json: {row["source"]}'
        text = translated.read_text(encoding='utf-8')
        assert re.search('[\u0600-\u06ff]', text), f'No Persian text in {translated}'
        assert '@@EQ' not in text, 'Unresolved authoring placeholder'
        if source.suffix == '.ipynb':
            en, fa = (json.loads(p.read_text(encoding='utf-8')) for p in (source, translated))
            assert len(en['cells']) == len(fa['cells'])
            for a, b in zip(en['cells'], fa['cells']):
                assert a['cell_type'] == b['cell_type']
                if a['cell_type'] == 'code':
                    assert a['source'] == b['source'], 'Numerical notebook code must be shared'
                    assert not b['outputs'], 'Translation source must not fork saved numerical outputs'
                else:
                    assert re.search('[\u0600-\u06ff]', ''.join(b['source']))
        if source.suffix == '.md' and source.parent.name == 'chapters':
            equations = lambda value: re.findall(r'\$\$.*?\$\$', value, re.S)
            assert equations(source.read_text(encoding='utf-8')) == equations(text), 'Display equations differ between editions'
            assert len(re.findall(r'^## ', source.read_text(encoding='utf-8'), re.M)) == len(re.findall(r'^## ', text, re.M)), 'A translated chapter or guide section is missing'
            figures = lambda value: re.findall(r'```\{figure\} ([^\n]+)', value)
            assert figures(source.read_text(encoding='utf-8')) == figures(text), 'Chapter figures must match'
    from localize_chapter02 import explorer
    original = (ROOT / 'templates/waves-explorer.html').read_text(encoding='utf-8')
    localized = explorer()
    physics = lambda value: value.split('<script>', 1)[1].split('const colors=', 1)[0]
    assert physics(original) == physics(localized), 'Browser equations differ between languages'
    for name in ('wave-geometry.svg', 'sheet-boundaries.svg'):
        ET.parse(ROOT / 'translations/fa/assets/chapter-02' / name)
    toc_files = re.findall(r'- file: (.+)', (ROOT / 'myst.yml').read_text(encoding='utf-8'))
    assert set(toc_files) == {row['source'] for row in manifest['pages']}, 'Every published English page must have a Persian counterpart'
    print(f'Passed: {len(routes)} language pairs covering the complete table of contents, source review locks, all chapter display equations/figures, all notebook code and browser physics, two localized SVGs')


if __name__ == '__main__':
    try:
        validate()
    except (AssertionError, KeyError) as exc:
        sys.exit(str(exc))
