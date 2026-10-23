"""Render an offline Chapter 6 explorer from saved, hash-checked data.

Public integration API: render(output_path, language='en', data_path=None).
This script reads numerical results and never launches a physics solver.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = '__CH06_NUMERICAL_DATA__'


def render(output_path, language='en', data_path=None):
    """Write one complete offline HTML file; return its absolute Path."""
    if language not in ('en', 'fa'):
        raise ValueError("language must be 'en' or 'fa'.")
    data_path = ROOT/'data/chapter-06/numerical-reference.json' if data_path is None else Path(data_path)
    data = json.loads(data_path.read_text(encoding='utf-8'))
    if data['metadata']['schema'] != 'metasurface-numerical-methods-v1':
        raise ValueError('Unsupported numerical dataset schema.')
    for name, expected in data['metadata']['source_sha256'].items():
        actual = hashlib.sha256((ROOT/'simulations'/name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Stale numerical data for {name}; rerun validate_chapter06.py.')
    if [row['cells'] for row in data['mesh']] != [4,8,16,32,64,128,256,512]:
        raise ValueError('The explorer requires the declared eight saved mesh cases.')
    if len(data['padding']) != 195:
        raise ValueError('The explorer requires three complete saved padding sweeps.')
    template = (ROOT/'templates/numerical-explorer.html').read_text(encoding='utf-8')
    if template.count(MARKER) != 1:
        raise ValueError('The template must contain exactly one numerical data marker.')
    embedded = json.dumps(data, separators=(',', ':'), ensure_ascii=False, allow_nan=False)
    embedded = embedded.replace('<', '\\u003c')
    html = template.replace(MARKER, embedded)
    if language == 'fa':
        html = html.replace('<html lang="en" dir="ltr">', '<html lang="fa" dir="rtl">', 1)
    destination = Path(output_path).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding='utf-8')
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--language', choices=['en','fa'], default='en')
    parser.add_argument('--data', type=Path)
    args = parser.parse_args()
    destination = args.output or (ROOT/'interactives/numerical-explorer.html' if args.language == 'en'
                                 else ROOT/'translations/fa/interactives/numerical-explorer.html')
    print(render(destination, language=args.language, data_path=args.data))


if __name__ == '__main__':
    main()
