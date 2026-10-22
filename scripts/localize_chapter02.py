"""Generate the Persian offline explorer and ZIP without duplicating equations.

Called by build_bilingual.py. Translation authors maintain explorer-strings.json;
the English template remains the sole implementation of browser physics.
"""
import html
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def explorer():
    source = (ROOT / 'templates/waves-explorer.html').read_text(encoding='utf-8')
    words = json.loads((ROOT / 'translations/fa/explorer-strings.json').read_text(encoding='utf-8'))
    head, script = source.split('<script>', 1)
    def text(match):
        value = html.unescape(match[1])
        stripped = value.strip()
        if stripped not in words:
            return match[0]
        return '>' + html.escape(value.replace(stripped, words[stripped]), quote=False) + '<'
    head = re.sub(r'>([^<>]+)<', text, head)
    head = re.sub(r'(aria-label|title)="([^"]*)"',
                  lambda m: m[1] + '="' + html.escape(words.get(html.unescape(m[2]), html.unescape(m[2])), quote=True) + '"', head)
    head = head.replace('<html lang="en">', '<html lang="fa" dir="rtl">')
    head = head.replace('</style>', '''
html[lang=fa]{font-family:Tahoma,"Segoe UI",Arial,sans-serif;line-height:1.8}
html[lang=fa] h1{line-height:1.6;letter-spacing:normal}
html[lang=fa] h2{line-height:1.8}
html[lang=fa] .eyebrow{letter-spacing:normal}
html[lang=fa] .scene,html[lang=fa] .formula,html[lang=fa] .scroll,html[lang=fa] input[type=range],html[lang=fa] output,html[lang=fa] .metric strong{direction:ltr;unicode-bidi:isolate}
html[lang=fa] .scene text{font-family:Tahoma,Arial,sans-serif;font-size:12px}
html[lang=fa] .scene .tiny{font-size:11px}
html[lang=fa] label output{float:left}
html[lang=fa] .question,html[lang=fa] .notice{border-left:0;border-right:4px solid var(--orange);border-radius:10px 0 0 10px}
html[lang=fa] .intro{max-width:none}
@media(max-width:500px){html[lang=fa] .tabs{grid-template-columns:repeat(2,minmax(0,1fr))}html[lang=fa] .metrics{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>''')
    # Preserve the entire numerical implementation byte-for-byte, including validation.
    equations, ui = script.split('const colors=', 1)
    def literal(match):
        value = match[1]
        return json.dumps(words[value], ensure_ascii=False) if value in words else match[0]
    ui = re.sub(r"'((?:\\.|[^'\\])*)'", literal, ui)
    return head + '<script>' + equations + 'const colors=' + ui


def export(stage):
    (stage / 'interactives/waves-explorer.html').write_text(explorer(), encoding='utf-8', newline='\n')
    files = ['notebooks/02-waves-and-interfaces.ipynb', 'simulations/waves_interfaces.py',
             'scripts/validate_chapter02.py', 'requirements-labs.txt', 'data/chapter-02/README.md',
             'data/chapter-02/waves-reference.json', 'data/chapter-02/waves-reference.csv',
             'data/chapter-02/validation.json', 'interactives/waves-explorer.html']
    (stage / 'scripts').mkdir(exist_ok=True)
    (stage / 'scripts/validate_chapter02.py').write_bytes((ROOT / 'scripts/validate_chapter02.py').read_bytes())
    with zipfile.ZipFile(stage / 'downloads/chapter-02-waves-fa.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(stage / file, file)
        archive.writestr('START-HERE.md', '''# اجرای فصل ۲ فارسی

بسته را کامل استخراج و ساختار پوشه‌ها را حفظ کنید.
interactives/waves-explorer.html در مرورگر و آفلاین اجرا می‌شود.
برای دفترچه از Python 3.12 و محیط مجازی استفاده کنید:

python -m pip install -r requirements-labs.txt
python -m pip install jupyterlab
python -m jupyterlab

notebooks/02-waves-and-interfaces.ipynb را باز و از هستهٔ تازه اجرا کنید.
کنترل مستقل: python scripts/validate_chapter02.py
کد و دادهٔ عددی با مرجع انگلیسی مشترک است؛ متن توضیحی فارسی است.
مدل‌ها تحلیلی و محدود به موج تخت، مرز، لایه، جونز و ورقهٔ الکتریکی‌اند.
حل‌گر هندسهٔ نقش‌دار یا تأیید قطعهٔ ساخته‌شده نیستند.
قرارداد exp(-i omega t)، پایهٔ مماسی و صفحات فاز را حفظ کنید.
''')


if __name__ == '__main__':
    raise SystemExit('Use scripts/build_bilingual.py to generate both editions.')
