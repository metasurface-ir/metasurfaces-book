"""Embed original geometry code and saved numerical data; no live physics."""
import json
from pathlib import Path
from geometry_assets import embed_geometry

ROOT = Path(__file__).resolve().parents[1]


def render(destination, language='en'):
    def read(name):
        return json.loads((ROOT/'data/design-studies'/name).read_text(encoding='utf-8'))
    inverse = read('inverse-design.json')
    inverse['evaluations'] = len(inverse['optimization']['history'])
    del inverse['optimization']  # Download keeps the full auditable search history.
    data = dict(dispersion=read('dispersion.json'), coupling=read('coupling.json'), inverse=inverse)
    data['dispersion'].pop('comparison')
    template = (ROOT/'templates/design-studies.html').read_text(encoding='utf-8')
    html = embed_geometry(template).replace('__LANG__', language).replace('__DIR__', 'rtl' if language == 'fa' else 'ltr')
    html = html.replace('__STUDY_DATA__', json.dumps(data, separators=(',', ':')).replace('</', '<\\/'))
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    render(ROOT/'interactives/design-studies.html')
