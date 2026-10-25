"""Draw an original conceptual tuning cell; no geometry extraction is implied."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def drawing(fa=False):
    def t(x, y, en, persian, size=18, color='#183b50'):
        return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}" direction="{"rtl" if fa else "ltr"}">{escape(persian if fa else en)}</text>'
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 580" role="img" aria-labelledby="title desc">
<title id="title">Bias-controlled surface: conceptual geometry and effective circuit</title>
<desc id="desc">Split metallic patch with a tunable gap on a grounded dielectric, and a series RLC surface impedance. Effective parameters are assigned, not extracted from this geometry.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="#225c78"/></marker></defs>
<rect width="1080" height="580" rx="20" fill="#f5f9fc"/>
<g font-family="Tahoma,Arial,sans-serif">
<rect x="20" y="62" width="330" height="355" rx="12" fill="white" stroke="#c5d8e5"/>
<rect x="375" y="62" width="330" height="355" rx="12" fill="white" stroke="#c5d8e5"/>
<rect x="730" y="62" width="330" height="355" rx="12" fill="white" stroke="#c5d8e5"/>
'''
    svg += t(540, 36, 'From bias voltage to a reflected wave', 'از ولتاژ بایاس تا موج بازتابی', 24)
    svg += t(185, 97, 'A · Top view: one possible cell', 'الف · نمای بالا: یک سلول مفهومی')
    svg += '''<rect x="55" y="130" width="260" height="204" rx="8" fill="#e0edf1" stroke="#779aaa" stroke-dasharray="6 5"/>
<rect x="80" y="170" width="92" height="115" fill="#deac62" stroke="#8c622c"/>
<rect x="198" y="170" width="92" height="115" fill="#deac62" stroke="#8c622c"/>
<path d="M150 225h29m0-14v28m12-28v28m0-14h30" fill="none" stroke="#225c78" stroke-width="4"/>
<path d="M245 170V138h50" fill="none" stroke="#a93868" stroke-width="3"/>
<path d="M120 285v34H75" fill="none" stroke="#a93868" stroke-width="3"/>
'''
    svg += t(185, 153, 'Metal islands', 'جزیره‌های فلزی', 16)
    svg += t(185, 261, 'C(V)', 'C(V)', 19)
    svg += t(185, 363, 'Gap element + bias routing', 'عنصر شکاف + مسیر بایاس', 17)
    svg += t(185, 391, 'Dashed boundary: cell footprint', 'مرز خط‌چین: محدودهٔ سلول', 15)
    svg += t(540, 97, 'B · Ground-backed section', 'ب · مقطع با صفحهٔ زمین')
    svg += '''<rect x="408" y="248" width="264" height="66" fill="#d7e8ef" stroke="#7899a8"/>
<path d="M420 244h99m27 0h114M408 317h264" stroke="#ab7834" stroke-width="9"/>
<path d="M451 142v83M615 225v-83" stroke="#225c78" stroke-width="3" marker-end="url(#arrow)"/>
<path d="M401 234h278" stroke="#a93868" stroke-dasharray="5 5"/>
'''
    svg += t(450, 128, 'Incident', 'فرودی', 16)
    svg += t(615, 128, 'Reflected', 'بازتابی', 16)
    svg += t(540, 282, 'Dielectric spacer', 'لایهٔ دی‌الکتریک', 17)
    svg += t(540, 347, 'Ground: no transmission port', 'زمین: بدون درگاه عبوری', 16)
    svg += t(540, 375, 'Dashed line: effective phase plane', 'خط‌چین: صفحهٔ فاز مؤثر', 15)
    svg += t(895, 97, 'C · Assigned impedance model', 'پ · مدل امپدانس مفروض')
    svg += '''<path d="M788 148h60v28l-8 8 16 12-16 12 16 12-16 12 8 8v18
c34 0 34 22 0 22c34 0 34 22 0 22c34 0 34 22 0 22v18m-18 0h36m-36 10h36m-18 0v32h-60"
fill="none" stroke="#225c78" stroke-width="3"/>
<circle cx="788" cy="148" r="5" fill="white" stroke="#225c78" stroke-width="2"/>
<circle cx="788" cy="378" r="5" fill="white" stroke="#225c78" stroke-width="2"/>
'''
    svg += t(950, 207, 'R = 25 Ω', 'R = 25 Ω')
    svg += t(950, 281, 'L = 20 nH', 'L = 20 nH')
    svg += t(950, 356, 'C(V)', 'C(V)')
    svg += t(920, 148, 'Z₀ → Zₛ(V)', 'Z₀ → Zₛ(V)', 22)
    svg += t(540, 456, 'Control voltage → capacitance → complex reflection → programmed aperture', 'ولتاژ کنترل ← ظرفیت خازنی ← بازتاب مختلط ← دهانهٔ برنامه‌ریزی‌شده', 20)
    svg += t(540, 497, 'Schematic only. No dimensions or physical component specifications are asserted.', 'این شکل شماتیک است؛ ابعاد یا مشخصات قطعهٔ واقعی را تعیین نمی‌کند.', 17)
    svg += t(540, 529, 'The circuit values are effective teaching parameters, not extracted patch values.', 'مقادیر مدار پارامترهای مؤثر آموزشی‌اند و از هندسهٔ پچ استخراج نشده‌اند.', 17)
    svg += t(540, 558, 'Original illustration · Metasurface.ir', 'تصویر تألیفی · Metasurface.ir', 15, '#527084')
    return svg + '</g></svg>\n'


if __name__ == '__main__':
    for fa, prefix in ((False, ''), (True, 'translations/fa/')):
        path = ROOT/f'{prefix}assets/chapter-07/tunable-cell.svg'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(drawing(fa), encoding='utf-8', newline='\n')
    print('Exported original English and Persian tuning-cell schematics')
