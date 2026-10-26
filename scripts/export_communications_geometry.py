"""Create an original editable diagram; no external illustration is used."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
for lang in ('en','fa'):
    labels=(['A communication link through a finite aperture','Transmitter','Receiver / target',
        'Optional direct path','Reflective aperture: z = 0','Enlarged aperture','0.48 m × 0.48 m',
        'Midpoint samples; phase commands','Possible loaded patch','Load / bias','Concept only; geometry not solved',
        'Drawing is schematic; nodes and distances belong to the stated scalar model.']
        if lang=='en' else
        ['پیوند مخابراتی از طریق دهانهٔ محدود','فرستنده','گیرنده / هدف',
         'مسیر مستقیم اختیاری','دهانهٔ بازتابی: z = 0','بزرگ‌نمایی دهانه','0.48 m × 0.48 m',
         'نمونه‌های میانی؛ فرمان فاز','پچ بارگذاری‌شدهٔ ممکن','بار / بایاس','فقط مفهوم؛ هندسه حل نشده',
         'شکل شماتیک است؛ گره‌ها و فاصله‌ها متعلق به مدل اسکالر اعلام‌شده‌اند.'])
    def t(x,y,s,size=17,color='#18354b'):
        return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}">{escape(s)}</text>'
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="520" viewBox="0 0 1080 520" role="img">'
    svg+='<title>'+escape(labels[0])+'</title><rect width="1080" height="520" rx="16" fill="#f4f8fa"/>'
    svg+='<g font-family="Segoe UI,Tahoma,sans-serif">'+t(540,35,labels[0],25)
    svg+='<path d="M70 430H595 M325 430V75" stroke="#ccd7df" stroke-width="2"/>'
    svg+=t(590,452,'x',17)+t(310,85,'z',17)
    svg+='<path d="M100 110L325 425L530 245" fill="none" stroke="#087f8c" stroke-width="4"/>'
    svg+='<path d="M100 110L530 245" fill="none" stroke="#b8803b" stroke-width="3" stroke-dasharray="8 7"/>'
    for x,y in [(100,110),(530,245)]:svg+=f'<circle cx="{x}" cy="{y}" r="9" fill="#18354b"/>'
    svg+=t(105,78,labels[1])+t(113,145,'(−10, 0, 20) m',14)+t(520,210,labels[2])+t(520,278,'(8, 0, 12) m',14)
    svg+=t(345,150,labels[3],15,'#966323')
    svg+='<path d="M305 419H345L353 433H297Z" fill="#e18431"/>'
    svg+=t(325,469,labels[4],16)
    svg+='<path d="M345 419L660 220" stroke="#98a8b4" stroke-width="1.5" stroke-dasharray="5 5"/>'
    svg+=t(790,78,labels[5],21)+t(790,105,labels[6],16)
    for y in range(8):
        for x in range(8):
            svg+=f'<rect x="{690+x*24}" y="{120+y*17}" width="22" height="15" fill="hsl({(x*37+y*19)%360},45%,58%)" rx="2"/>'
    svg+=t(790,280,labels[7],15)
    svg+='<rect x="658" y="305" width="360" height="163" rx="12" fill="white" stroke="#cedbe4"/>'
    svg+=t(842,332,labels[8],18)
    svg+='<rect x="685" y="349" width="86" height="66" fill="#dce6ed"/><path d="M694 357H725V408H694Z M733 357H762V408H733Z" fill="#cc8d44"/><rect x="724" y="376" width="11" height="12" fill="#18354b"/>'
    svg+='<path d="M735 383H805" stroke="#18354b"/>'
    svg+=t(900,388,labels[9],16)+t(840,448,labels[10],15)
    svg+=t(540,502,labels[11],15)+'</g></svg>\n'
    path=ROOT/('' if lang=='en' else 'translations/fa')/'assets/chapter-08/link-geometry.svg'
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(svg,encoding='utf-8')
print('Exported two original geometry schematics')
