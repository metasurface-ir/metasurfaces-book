"""Original vector schematic for Chapter 9; no third-party artwork."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
for lang in ('en','fa'):
    labels=(['From a possible device to a defensible measurement',
        'A. Possible grounded patch','Top view: width w','Section: conductor / dielectric / ground',
        'Concept only; geometry is not solved','B. Preserve the fabrication evidence',
        'Mask + material','Pattern transfer','Metrology','Nominal ≠ fabricated geometry',
        'C. Modeled one-port measurement','Instrument','Error box','Port plane','Surface plane',
        'Three known standards at the port plane','Known propagation: exp(2ikd)',
        'D. Separate free-space extension','Illumination','Receiver','Finite sample',
        'Collect angles + polarizations; qualify the fixture',
        'Synthetic data only. Panel C is the executed algebra; panel D is an unexecuted extension.']
        if lang=='en' else
        ['از دستگاه ممکن تا اندازه‌گیری مستند',
         'الف. وصلهٔ زمین‌دار ممکن','نمای بالا: پهنای w','مقطع: رسانا / دی‌الکتریک / زمین',
         'فقط مفهوم؛ هندسه حل نمی‌شود','ب. شواهد ساخت را حفظ کنید',
         'ماسک و ماده','انتقال الگو','مترولوژی','هندسهٔ اسمی ≠ هندسهٔ ساخته‌شده',
         'پ. اندازه‌گیری تک‌درگاهی مدل‌شده','ابزار','جعبهٔ خطا','صفحهٔ درگاه','صفحهٔ سطح',
         'سه استاندارد معلوم در صفحهٔ درگاه','انتشار معلوم: exp(2ikd)',
         'ت. توسعهٔ جداگانهٔ فضای آزاد','روشن‌سازی','گیرنده','نمونهٔ محدود',
         'زاویه‌ها و قطبش‌ها را جمع‌آوری و نگه‌دارنده را بررسی کنید',
         'فقط دادهٔ مصنوعی. پنل پ جبر اجراشده و پنل ت توسعهٔ اجرا‌نشده است.'])
    def t(x,y,s,size=17,color='#18354b'):
        return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}">{escape(s)}</text>'
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="720" viewBox="0 0 1100 720" role="img">'
    svg+='<title>'+escape(labels[0])+'</title><rect width="1100" height="720" rx="16" fill="#f3f7fa"/>'
    svg+='<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#087f8c"/></marker></defs>'
    svg+='<g font-family="Segoe UI,Tahoma,sans-serif">'+t(550,36,labels[0],25)
    for x,y in [(20,60),(560,60),(20,365),(560,365)]:
        svg+=f'<rect x="{x}" y="{y}" width="520" height="290" rx="12" fill="white" stroke="#cedbe4"/>'
    svg+=t(280,91,labels[1],21)
    svg+='<path d="M55 142L185 125L228 190L98 207Z" fill="#dae7e8"/><path d="M83 151L171 140L200 183L112 195Z" fill="#d49443"/>'
    svg+='<path d="M55 142V161L98 226V207 M98 226L228 209V190" fill="#9cafb9" stroke="#78909c"/>'
    svg+=t(140,255,labels[2],16)
    svg+='<rect x="294" y="166" width="205" height="55" fill="#dbe9e6"/><path d="M333 164H461" stroke="#d49443" stroke-width="9"/><path d="M294 225H499" stroke="#677f8b" stroke-width="7"/>'
    svg+='<path d="M333 140H461" stroke="#18354b"/><path d="M333 133V147M461 133V147" stroke="#18354b"/>'
    svg+=t(397,128,'w₀ = 5 mm',15)+t(397,198,'εeff,₀ = 3',16)+t(397,255,labels[3],13)
    svg+=t(280,319,labels[4],16,'#8a5620')
    svg+=t(820,91,labels[5],21)
    for i,label in enumerate(labels[6:9]):
        x=582+i*168
        svg+=f'<rect x="{x}" y="157" width="143" height="74" rx="10" fill="{["#e6f4f3","#fff0de","#eee9f7"][i]}"/>'
        svg+=t(x+71,200,label,17)
        if i<2:svg+=f'<path d="M{x+146} 194h18" stroke="#087f8c" stroke-width="2" marker-end="url(#arrow)"/>'
    svg+=t(820,280,'w, height, sidewall, roughness' if lang=='en' else 'پهنا، ارتفاع، دیواره و زبری',17)
    svg+=t(820,319,labels[9],16,'#8a5620')
    svg+=t(280,398,labels[10],21)
    svg+='<rect x="40" y="454" width="100" height="70" rx="8" fill="#e5edf3"/><rect x="168" y="454" width="120" height="70" rx="8" fill="#eee9f7"/>'
    svg+=t(90,484,labels[11],16)+t(228,479,labels[12],16)+t(228,506,'D, T, S',16)
    svg+='<path d="M140 489H168M288 489H490" stroke="#087f8c" stroke-width="3" marker-end="url(#arrow)"/>'
    svg+='<path d="M332 441V546M490 441V546" stroke="#e18431" stroke-width="3" stroke-dasharray="7 5"/>'
    svg+=t(332,430,labels[13],14)+t(486,430,labels[14],14)+t(412,470,'d = 5 mm',15)+t(413,540,'Γport → Γsurface',14)
    svg+=t(280,579,labels[15],16)+t(280,615,labels[16],16)
    svg+=t(820,398,labels[17],21)
    svg+='<path d="M650 458L675 472L642 508L627 483Z M965 458L940 472L973 508L988 483Z" fill="#8ca4b1"/>'
    svg+='<path d="M653 494L810 586L961 494" fill="none" stroke="#087f8c" stroke-width="3" marker-end="url(#arrow)"/>'
    svg+='<path d="M720 583H900L928 600H748Z" fill="#dbe9e6"/>'
    for x in range(730,891,25):svg+=f'<path d="M{x} 586h17l12 9h-17Z" fill="#d49443"/>'
    svg+=t(656,438,labels[18],16)+t(966,438,labels[19],16)+t(810,559,labels[20],16)
    svg+=t(820,633,labels[21],14)
    svg+=t(550,694,labels[22],16)+'</g></svg>\n'
    path=ROOT/('' if lang=='en' else 'translations/fa')/'assets/chapter-09/measurement-geometry.svg'
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(svg,encoding='utf-8',newline='\n')
print('Exported original English and Persian measurement schematics')
