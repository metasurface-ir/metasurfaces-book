"""Original vector redrawings of all nine Chapter 2 textbook diagrams.

Only geometry and simple callout letters appear in SVG. Mathematical definitions
and equations stay in the accompanying MyST LaTeX captions and source reading.
The instructor-supplied reference PDF is not copied into the repository.
"""
from pathlib import Path
import html,json

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'assets/chapter-02'
INK='#17394c';TEAL='#137c86';GOLD='#b66c12';GRAY='#dce6ed'
def line(x1,y1,x2,y2,color=INK,arrow=False,dash=False):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2.4"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="6 5"' if dash else '')+'/>'
def text(x,y,value,color=INK,anchor='start'):
    return f'<text x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}">{html.escape(value)}</text>'
def label(x,y,n):return f'<circle cx="{x}" cy="{y}" r="13" fill="white" stroke="{TEAL}"/>'+text(x,y+5,n,TEAL,'middle')
def save(name,body,description,width=760,height=340):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(description)}</title><desc id="desc">Original vector reconstruction of the textbook's conceptual geometry. Letter callouts are defined in the LaTeX caption. This is not simulation output.</desc>
<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto-start-reverse"><path d="M0 0L7 3.5L0 7Z" fill="context-stroke"/></marker></defs>
<rect width="100%" height="100%" rx="12" fill="#f6f9fc"/>
<g font-family="Arial,sans-serif" font-size="17">{body}</g></svg>'''
    (DEST/f'textbook-{name}.svg').write_text(svg,encoding='utf-8')

def render():
    DEST.mkdir(exist_ok=True)
    b=f'<rect x="80" y="170" width="600" height="130" fill="{GRAY}"/>'
    b+=line(80,170,680,170)+text(110,135,'Medium 1')+text(110,220,'Medium 2')
    b+=line(330,170,330,55,TEAL,True)+line(330,170,510,170,GOLD,True)+line(330,170,510,55,INK,True)
    b+=line(330,55,510,55,dash=True)+line(510,55,510,170,dash=True)
    b+=text(314,42,'N',TEAL)+text(518,180,'T',GOLD)+text(520,55,'F')+line(245,170,245,100,arrow=True)+text(225,95,'n')
    save('normal-tangential',b,'Normal and tangential components at a two-medium boundary')

    b=f'<path d="M110 190Q380 140 650 190L650 270Q380 220 110 270Z" fill="{GRAY}"/>'
    b+='<ellipse cx="380" cy="100" rx="100" ry="27" fill="white" stroke="#17394c" stroke-width="2"/>'
    b+='<path d="M280 100V245A100 27 0 0 0 480 245V100" fill="none" stroke="#17394c" stroke-width="2"/>'
    b+='<path d="M280 245A100 27 0 0 1 480 245" fill="none" stroke="#17394c" stroke-width="2" stroke-dasharray="6 4"/>'
    b+=line(380,85,380,30,TEAL,True)+line(380,250,380,310,TEAL,True)+text(398,50,'Top area')+text(398,302,'Bottom area')
    b+=line(350,145,350,90,GOLD,True)+line(350,235,350,180,GOLD,True)+text(310,142,'D1')+text(310,232,'D2')
    b+=line(520,175,520,110,arrow=True)+text(531,113,'n')
    save('gauss-pillbox',b,'Gaussian pillbox straddling a charged interface')

    b=''
    for i,kind in enumerate(['Positive','Zero','Negative']):
        cx=135+i*245;b+=f'<path d="M{cx-90} 240Q{cx} 80 {cx+90} 240" fill="none" stroke="{INK}" stroke-width="2"/>'
        b+=text(cx,65,kind,anchor='middle')
        for dx in [-35,0,35]:
            b+=line(cx+dx,245,cx+dx,177,TEAL,True)
            b+=line(cx+dx,177,cx+dx,95 if kind=='Positive' else 125,TEAL,True)
            if kind!='Zero':b+=text(cx+dx,170,'+' if kind=='Positive' else '−',GOLD,'middle')
        if kind=='Negative':
            for dx in [-18,18]:b+=line(cx+dx,245,cx+dx,178,TEAL,True)
        if kind=='Positive':
            for dx in [-18,18]:b+=line(cx+dx,172,cx+dx,95,TEAL,True)
    save('surface-charge',b,'Positive zero and negative surface-charge field-line comparisons')

    for magnetic in [False,True]:
        b=f'<rect x="100" y="175" width="560" height="120" fill="{GRAY}"/>'+line(90,175,690,175)
        b+=text(115,100,'Medium 2')+text(115,265,'Medium 1')
        b+=line(250,110,530,110,arrow=True)+line(530,110,530,235,arrow=True)+line(530,235,250,235,arrow=True)+line(250,235,250,110,arrow=True)
        b+=line(390,275,390,60,TEAL,True)+text(403,63,'y')+line(570,175,570,255,TEAL,True)+text(583,250,'n')
        b+=line(260,175,650,175,arrow=True)+text(660,180,'x')+text(375,95,'a')+text(540,132,'h/2')+text(540,225,'h/2')
        letter='H' if magnetic else 'E'
        b+=text(300,102,letter+'2')+text(300,262,letter+'1')
        b+=line(320,135,450,135,GOLD,True)+line(320,214,450,214,GOLD,True)
        if magnetic:
            for x in range(290,500,28):b+=f'<circle cx="{x}" cy="175" r="7" fill="white" stroke="{GOLD}"/><circle cx="{x}" cy="175" r="2.3" fill="{GOLD}"/>'
            b+=text(605,155,'J',GOLD)
        save('magnetic-loop' if magnetic else 'electric-loop',b,'Shrinking rectangular loop for '+('magnetic-field jump and surface current' if magnetic else 'electric-field tangential continuity'))

    b=''
    for i,title in enumerate(['Correct','Incorrect','Incorrect']):
        x=20+250*i;b+=line(x+10,175,x+225,175)+text(x+115,65,title,TEAL if i==0 else GOLD,'middle')
        b+=text(x+15,140,'1')+text(x+15,220,'2')
        b+=line(x+70,165,x+170,125,TEAL,True)
        b+=line(x+70,190,x+(170 if i==0 else (135 if i==1 else 205)),230 if i!=2 else 190,TEAL,True)
    save('tangential-continuity',b,'One matching and two mismatched tangential electric-field components')

    b=f'<rect x="90" y="170" width="580" height="120" fill="{GRAY}"/>'+line(90,170,670,170)
    b+=line(380,275,380,45,TEAL,True)+text(391,48,'z')+line(180,170,620,170,arrow=True)+text(630,177,'x')
    b+=text(135,95,'Medium 1')+text(135,240,'Medium 2')+label(420,115,'1')+label(420,225,'2')
    save('electric-interface-example',b,'Electric-field example with upper and lower dielectric half-spaces')

    b=f'<path d="M290 70L460 115L460 285L290 240Z" fill="{GRAY}" stroke="{INK}" stroke-width="2"/>'
    b+=line(165,190,650,190,arrow=True)+text(663,197,'x')+line(290,270,290,35,arrow=True)+text(304,38,'z')
    b+=line(290,240,485,292,arrow=True)+text(494,299,'y')
    b+=line(320,135,425,163,GOLD,True)+text(390,130,'J')+line(360,190,550,190,TEAL,True)+text(560,180,'n')
    b+=text(140,250,'Medium 2')+text(540,250,'Medium 1')
    save('magnetic-interface-example',b,'Magnetic-field example with a surface-current sheet and positive-x normal')

    b=f'<path d="M430 80L615 125L615 290L430 245Z" fill="{GRAY}" stroke="{INK}" stroke-width="2"/>'
    b+=line(110,200,700,200,arrow=True)+text(710,207,'z')+line(430,295,430,35,arrow=True)+text(442,39,'x')
    b+=line(160,150,380,150,TEAL,True)+text(190,130,'Incident',TEAL)+line(380,80,160,80,GOLD,True)+text(190,60,'Reflected',GOLD)
    b+=line(475,150,680,150,TEAL,True)+text(520,130,'Transmitted',TEAL)
    for x,y in [(280,150),(280,80),(560,150)]:b+=line(x,y,x,y-45,TEAL,True)
    for x,y,inward in [(315,150,True),(315,80,False),(595,150,True)]:
        b+=f'<circle cx="{x}" cy="{y}" r="9" fill="white" stroke="{GOLD}" stroke-width="1.8"/>'
        if inward:b+=line(x-5,y-5,x+5,y+5,GOLD)+line(x-5,y+5,x+5,y-5,GOLD)
        else:b+=f'<circle cx="{x}" cy="{y}" r="2.5" fill="{GOLD}"/>'
    b+=text(160,280,'Medium 1')+text(520,310,'Medium 2')
    save('normal-incidence',b,'Incident reflected and transmitted plane waves at normal incidence')

    pages={'normal-tangential':22,'gauss-pillbox':23,'surface-charge':23,'electric-loop':24,'tangential-continuity':24,'magnetic-loop':25,'electric-interface-example':27,'magnetic-interface-example':28,'normal-incidence':50}
    manifest={'source':'Instructor-supplied Persian booklet, Chapter 2, printed pages 15–69','scope':'All nine embedded source diagrams plus the page-26 boundary table (recreated in LaTeX/Markdown)','figures':[{'source_page':page,'asset':f'assets/chapter-02/textbook-{name}.svg','method':'original vector redrawing; equations and symbol definitions remain LaTeX in captions'} for name,page in pages.items()],'table':{'source_page':26,'location':'Section 2.4 source reading','method':'eight-row four-column Markdown/LaTeX table, shortened and corrected with instructor authorization; PEC tangential B and assumptions explicitly corrected'}}
    (ROOT/'sources/instructor-booklet/chapter02-figures.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Rendered all nine textbook diagram counterparts and recorded the boundary table.')
if __name__=='__main__':render()
