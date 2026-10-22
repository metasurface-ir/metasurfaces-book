"""Build both editions from one checkout; shared numerical sources are never forked.

Run with the book environment's Python after installing requirements.txt.
BASE_URL may be empty or a project path such as /metasurfaces-book.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from localize_chapter02 import export

ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get('BASE_URL', '').rstrip('/')
STAGE = ROOT / '_build' / 'persian-source'


def run_book(directory, base):
    env = dict(os.environ, BASE_URL=base)
    subprocess.run([sys.executable, '-m', 'jupyter_book', 'build', '--html', '--strict', '--ci'],
                   cwd=directory, env=env, check=True)


def copy_tree(source, target):
    shutil.copytree(source, target, dirs_exist_ok=True)


def prepare_persian():
    # Delete only our generated staging directory inside this checkout's _build.
    if STAGE.resolve().parent != (ROOT / '_build').resolve():
        raise RuntimeError('Unsafe staging path')
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    for name in ('assets', 'data', 'simulations', 'styles', 'downloads', 'interactives'):
        copy_tree(ROOT / name, STAGE / name)
    for name in ('references.bib', 'requirements-labs.txt'):
        shutil.copy2(ROOT / name, STAGE / name)
    copy_tree(ROOT / 'translations' / 'fa', STAGE)
    # Reuse the already downloaded theme; the two editions use the same version.
    theme = ROOT / '_build/templates'
    if theme.is_dir():
        copy_tree(theme, STAGE / '_build/templates')
    # Numerical cells and saved numerical outputs always come from the English source.
    # Students edit only the Persian Markdown-cell sources in the translation notebook.
    for row in json.loads((ROOT / 'translations/languages.json').read_text(encoding='utf-8'))['pages']:
        if not row['source'].endswith('.ipynb'):
            continue
        original = json.loads((ROOT / row['source']).read_text(encoding='utf-8'))
        translated = json.loads((ROOT / row['translation']).read_text(encoding='utf-8'))
        assert len(original['cells']) == len(translated['cells'])
        for i, cell in enumerate(original['cells']):
            assert cell['cell_type'] == translated['cells'][i]['cell_type']
            if cell['cell_type'] == 'code':
                original['cells'][i] = cell
            else:
                original['cells'][i]['source'] = translated['cells'][i]['source']
        # This annotation explains shared English plot/table labels in the Persian edition.
        (STAGE / row['source']).write_text(json.dumps(original, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    export(STAGE)
    # Localized bundles preserve their original shared code/data and filenames.
    # Replace only notebook narratives with the assembled executable notebooks.
    import zipfile
    for name in ('chapter-01-foundations.zip', 'chapter-03-unit-cell.zip', 'chapter-05-synthesis.zip'):
        with zipfile.ZipFile(ROOT / 'downloads' / name) as original:
            with zipfile.ZipFile(STAGE / 'downloads' / name, 'w', compression=zipfile.ZIP_DEFLATED) as translated_zip:
                for item in original.infolist():
                    path = STAGE / item.filename
                    contents = path.read_bytes() if path.is_file() and (item.filename.startswith('notebooks/') or item.filename == 'downloads/chapter-01-report-template.md') else original.read(item)
                    if item.filename == 'START-HERE.md':
                        contents = ('# بستهٔ فارسی کتاب فراسطوح\n\nکل بسته را استخراج و ساختار پوشه‌ها را حفظ کنید. متن دفترچه فارسی و کد و داده با مرجع انگلیسی مشترک است. راهنمای اجرای اصلی در ادامه آمده است.\n\n').encode('utf-8') + contents
                    translated_zip.writestr(item, contents)


def decorate(output, language):
    manifest = json.loads((ROOT / 'translations/languages.json').read_text(encoding='utf-8'))
    target_base = BASE + ('/fa' if language == 'fa' else '')
    config = {'base': BASE, 'language': language, 'routes': [p['route'] for p in manifest['pages']]}
    for path in output.rglob('*.html'):
        if 'interactives' in path.parts or 'build' in path.relative_to(output).parts:
            continue
        text = path.read_text(encoding='utf-8')
        if '<html' not in text:
            continue
        # The theme hydrates its document root as English. Apply Persian direction
        # after hydration, avoiding a React document mismatch and lost styles.
        tags = (f'<script id="book-language-config" type="application/json">{json.dumps(config, ensure_ascii=False)}</script>'
                f'<script defer src="{target_base}/bilingual.js"></script>')
        text = text.replace('</body>', tags + '</body>', 1)
        # Useful metadata is present in the static HTML, before JavaScript/hydration.
        relative = path.relative_to(output).as_posix()
        route = '' if relative == 'index.html' else relative.removesuffix('/index.html').removesuffix('.html')
        if route in config['routes']:
            links = ''.join(f'<link rel="alternate" hreflang="{lang}" href="{BASE}{"/fa" if lang == "fa" else ""}/{route + "/" if route else ""}"/>' for lang in ('en', 'fa'))
            text = text.replace('</head>', links + '</head>', 1)
        path.write_text(text, encoding='utf-8', newline='\n')
    for name in ('bilingual.js', 'bilingual.css'):
        shutil.copy2(ROOT / 'styles' / name, output / name)


def main():
    subprocess.run([sys.executable, str(ROOT / 'scripts/validate_translations.py')], check=True)
    run_book(ROOT, BASE)
    decorate(ROOT / '_build/html', 'en')
    prepare_persian()
    run_book(STAGE, BASE + '/fa')
    decorate(STAGE / '_build/html', 'fa')
    output = ROOT / '_build/html/fa'
    if output.exists():
        # This is our generated language output, never an authored directory.
        assert output.resolve().parent == (ROOT / '_build/html').resolve()
        shutil.rmtree(output)
    copy_tree(STAGE / '_build/html', output)
    print('Built English and Persian editions in _build/html')


if __name__ == '__main__':
    main()
