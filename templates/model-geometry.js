/* Original course schematics. Drawing only: no electromagnetic solver lives here.
 * Shared by exported SVG figures and offline interactive labs. Length inputs: um.
 */
(() => {
  'use strict';
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));
  const f=x=>Number(x).toFixed(3).replace(/0+$/,'').replace(/\.$/,'');
  const text=(x,y,s,extra='')=>`<text x="${x}" y="${y}" ${extra}>${esc(s)}</text>`;
  const line=(x1,y1,x2,y2,color='#647d90',extra='')=>`<path d="M${x1} ${y1}L${x2} ${y2}" fill="none" stroke="${color}" stroke-width="2" ${extra}/>`;
  const rect=(x,y,w,h,color,extra='')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${color}" ${extra}/>`;
  const arrow=(x1,y1,x2,y2,color='#174b68')=>line(x1,y1,x2,y2,color,'marker-end="url(#geom-arrow)"');
  const dim=(x1,y1,x2,y2,label)=>line(x1,y1,x2,y2,'#4b6173','marker-start="url(#geom-dim)" marker-end="url(#geom-dim)"')+text((x1+x2)/2,(y1+y2)/2-9,label,'text-anchor="middle"');
  function svg(title,description,body,height=680){
    return `<svg xmlns="http://www.w3.org/2000/svg" class="model-geometry" viewBox="0 0 800 ${height}" role="img" aria-label="${esc(title)}"><title>${esc(title)}</title><desc>${esc(description)}</desc><defs><marker id="geom-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker><marker id="geom-dim" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M10 0L0 5L10 10" fill="none" stroke="#4b6173" stroke-width="1.5"/></marker></defs><style>.model-geometry{width:100%;height:auto;display:block;background:#f8fbfd;border-radius:12px;direction:ltr}.model-geometry text{font:19px Tahoma,Arial,sans-serif;fill:#23465c}.model-geometry .small{font-size:16px}.model-geometry .heading{font-size:21px;font-weight:700}.model-geometry .label{fill:#fff;font-weight:700}</style>${body}</svg>`;
  }
  const words=fa=>fa?{
    ridge:'سلول واحد تیغه‌ای دی‌الکتریک',supercell:'ابرسلول انحراف پرتو',view:'نمای سه‌بعدی؛ برش نمایشی در راستای y',section:'مقطع x–z و صفحه‌های مرجع',air:'محیط فرودی',substrate:'زیرلایه',periodic:'مرز تناوبی',repeat:'تکرار نامحدود در x',invariant:'ناوردا در y؛ ستون منفرد نیست',schematic:'طرح هندسی؛ مقیاس دیدها یکسان نیست',input:'تابش TE',reflected:'بازتاب r',transmitted:'عبور t',slab:'لایهٔ تخت برای آزمون عددی',slabView:'برش سه‌بعدی از لایهٔ نامحدود در x و y',mesh:'شبکه فقط در راستای z است',outgoing:'مرز تابشی گسسته',padding:'فاصلهٔ بیرونی',sheet:'ورقهٔ ایده‌آل؛ مدل تحلیلی',sheetView:'مدل دو‌درگاهی؛ هندسهٔ ذره تعیین نشده است',sheetNote:'نتیجهٔ این مدل، شبیه‌سازی ذرهٔ سه‌بعدی نیست',dimension:'ضخامت صفر؛ هر دو مرجع روی ورقه',node:'نقطه‌ها گرهٔ عددی‌اند؛ لایهٔ مادی نیستند'
  }:{ridge:'Dielectric ridge unit cell',supercell:'Beam-steering supercell',view:'3D view: illustrative cut along y',section:'x–z section and reference planes',air:'Incident medium',substrate:'Substrate',periodic:'Periodic boundary',repeat:'Repeats indefinitely along x',invariant:'Invariant along y; not isolated posts',schematic:'Schematic: views use different scales',input:'TE illumination',reflected:'Reflection r',transmitted:'Transmission t',slab:'Uniform slab: numerical benchmark',slabView:'3D cut: film extends indefinitely in x and y',mesh:'Only z is discretized',outgoing:'Discrete radiation boundary',padding:'Exterior padding',sheet:'Ideal sheet: analytical model',sheetView:'Two-port model; no particle geometry assigned',sheetNote:'This response is not a simulated 3D particle',dimension:'Zero thickness; both references on the sheet',node:'Dots are numerical nodes, not material layers'};
  function ridge(p,widths,language='en'){
    const w=words(language==='fa'),multi=widths.length>1,pitch=p.period_um||p.pitch_um,h=p.height_um,L=pitch*widths.length;
    const shown=multi?widths:[widths[0],widths[0],widths[0]],displayL=pitch*shown.length;
    let s=text(28,34,multi?w.supercell:w.ridge,'class="heading"')+text(28,62,w.view,'class="small"');
    // Orthographic extrusion with visible cut ends; material dimensions remain explicit.
    const scale=Math.min(570/displayL,155/h),span=displayL*scale,left=(800-span-75)/2,base=265,depth=64;
    const poly=(points,color)=>`<polygon points="${points.map(v=>v.join(',')).join(' ')}" fill="${color}" stroke="#4c758a" stroke-width="1.2"/>`;
    s+=poly([[left,base],[left+span,base],[left+span+depth,base-40],[left+depth,base-40]],'#d6e9f4');
    s+=poly([[left,base],[left+span,base],[left+span,base+23],[left,base+23]],'#a8cadf');
    for(let j=shown.length-1;j>=0;j--){
      const x=left+(j+.5)*pitch*scale-shown[j]*scale/2,rw=shown[j]*scale,top=base-h*scale;
      s+=poly([[x,top],[x+rw,top],[x+rw+depth,top-40],[x+depth,top-40]],'#68bfc0');
      s+=poly([[x+rw,top],[x+rw+depth,top-40],[x+rw+depth,base-40],[x+rw,base]],'#1b677b');
      s+=poly([[x,top],[x+rw,top],[x+rw,base],[x,base]],multi||j===1?'#16828c':'#86bfc4');
    }
    const a=multi?left:left+pitch*scale,b=multi?left+span:left+2*pitch*scale;
    for(const x of [a,b])s+=line(x,82,x,base+31,'#8b699b','stroke-dasharray="7 5"');
    s+=dim(a,310,b,310,`${multi?'L':'Λ'} = ${f(L)} µm`)+text(400,340,w.repeat+' · '+w.invariant,'text-anchor="middle" class="small"');
    s+=arrow(58,142,58,209)+text(79,162,'+z')+arrow(58,142,118,142)+text(126,148,'x')+arrow(58,142,89,119)+text(95,115,'y');
    s+=text(28,379,w.section,'class="heading"');
    const x0=110,x1=684,z0=464,z1=577,cell=(x1-x0)/widths.length;
    s+=rect(x0,408,x1-x0,z1-408,'#edf4f8')+rect(x0,z1,x1-x0,39,'#c3deed');
    for(let j=0;j<widths.length;j++){
      const rw=widths[j]/pitch*cell,x=x0+(j+.5)*cell-rw/2;
      s+=rect(x,z0,rw,z1-z0,'#16828c',`data-width-um="${widths[j]}"`);
      if(multi)s+=text(x0+(j+.5)*cell,z0+27,String(j+1),'text-anchor="middle" class="label small"');
    }
    s+=line(90,z0,710,z0,'#9a5e3d','stroke-dasharray="7 4"')+line(90,z1,710,z1,'#9a5e3d','stroke-dasharray="7 4"');
    for(const x of [x0,x1])s+=line(x,405,x,622,'#8b699b','stroke-dasharray="7 5"');
    s+=text(116,435,`${w.air}: nᵢ = ${f(p.n_incident)}`,'class="small"')+text(118,604,`${w.substrate}: nₜ = ${f(p.n_substrate)}`,'class="small"');
    s+=text(697,469,'z = 0','class="small"')+text(697,582,'z = h','class="small"');
    s+=arrow(315,409,315,459)+text(334,421,'kᵢ (+z)','class="small"')+text(334,444,'E ∥ y (TE)','class="small"');
    s+=arrow(560,455,560,409)+text(582,428,'r','class="heading"')+arrow(560,589,560,632)+text(582,627,'t','class="heading"');
    s+=dim(73,z0,73,z1,`h`)+dim(x0,648,x1,648,`${multi?'L = '+widths.length+'Λ':'Λ'} = ${f(L)} µm`);
    if(!multi)s+=dim((x0+x1)/2-widths[0]/pitch*cell/2,548,(x0+x1)/2+widths[0]/pitch*cell/2,548,'w');
    s+=text(28,691,`h = ${f(h)} µm · nᵣ = ${f(p.n_ridge)} · n_gap = ${f(p.n_gap)} · λ₀ = ${f(p.wavelength_um)} µm`,'class="small"');
    s+=text(28,721,`${multi?'wⱼ ≈':'w ='} ${widths.map(f).join(', ')} µm`,'class="small"');
    return svg(multi?w.supercell:w.ridge,w.invariant,s,744).replace('<svg ',`<svg data-model="${multi?'supercell':'ridge'}" data-height-um="${h}" data-period-um="${L}" `);
  }
  function slab(p,N=8,padding=0,language='en'){
    const w=words(language==='fa'),d=p.thickness_um,n=p.n_exterior;
    let s=text(28,34,w.slab,'class="heading"')+text(28,62,w.slabView,'class="small"');
    s+=`<path d="M180 105H585L665 70H260Z" fill="#8ed0cb" stroke="#247d87"/><path d="M180 105H585V245H180Z" fill="#24919b"/><path d="M585 105L665 70V210L585 245Z" fill="#1b667a"/>`;
    s+=text(370,182,`nᶠ = ${f(p.n_film)}`,'text-anchor="middle" class="label"')+dim(138,105,138,245,`d`);
    s+=arrow(390,75,390,101)+text(421,96,'kᵢ (+z)')+arrow(560,263,560,298)+text(584,288,'t');
    s+=text(400,334,`${w.mesh} · d = ${f(d)} µm`,'text-anchor="middle"');
    s+=text(28,377,w.section,'class="heading"');
    const left=140,right=660,top=441,bottom=552;
    s+=rect(left,397,right-left,bottom-397,'#eef5f8')+rect(left,top,right-left,bottom-top,'#9bd3ce')+rect(left,bottom,right-left,74,'#eef5f8');
    s+=text(155,426,`nₑ = ${f(n)}`)+text(155,503,`nᶠ = ${f(p.n_film)}`)+text(155,608,`nₑ = ${f(n)}`);
    for(const y of [top,bottom])s+=line(120,y,690,y,'#9a5e3d','stroke-dasharray="7 4"');
    s+=text(697,446,'z = 0','class="small"')+text(697,557,'z = d','class="small"');
    // Display a sparse subset for large N: positions still come from the actual grid.
    const indices=N<=16?Array.from({length:N+1},(_,i)=>i):[0,1,2,N/2,N-2,N-1,N];
    s+=line(400,409,400,603,'#6f7f91');
    for(const j of indices)s+=`<circle cx="400" cy="${top+(bottom-top)*j/N}" r="${N<=16?4:3}" fill="#173e58" data-node-index="${j}"/>`;
    const bcTop=padding?397:top,bcBottom=padding?626:bottom;
    s+=line(120,bcTop,690,bcTop,'#855696','stroke-dasharray="3 4"')+line(120,bcBottom,690,bcBottom,'#855696','stroke-dasharray="3 4"');
    s+=text(65,bcTop+5,'BC−','class="small"')+text(65,bcBottom+5,'BC+','class="small"');
    s+=arrow(560,401,560,435)+text(582,424,'kᵢ')+arrow(609,435,609,400)+text(628,424,'r')+arrow(560,564,560,610)+text(582,606,'t');
    s+=text(28,656,`N = ${N} · Δz = d/N = ${Number(d/N).toPrecision(4)} µm · ${w.node}`,'class="small"');
    s+=text(28,686,`${w.padding}: ${padding} Δz = ${f(padding*d/N)} µm / side`,'class="small"');
    s+=text(28,716,`${w.outgoing} · ${N>16?(language==='fa'?'بخشی از گره‌ها نمایش داده شده':'subset of nodes shown'):w.schematic}`,'class="small"');
    return svg(w.slab,w.slabView,s,744).replace('<svg ',`<svg data-model="slab" data-cells="${N}" data-padding-cells="${padding}" data-domain-left-um="${-padding*d/N}" data-domain-right-um="${d+padding*d/N}" `);
  }
  function sheet(language='en'){
    const w=words(language==='fa');
    let s=text(28,34,w.sheet,'class="heading"')+text(28,65,w.sheetView,'class="small"');
    s+=`<path d="M180 205L570 205L660 145L270 145Z" fill="#9bd5d4" stroke="#197c87" stroke-width="3"/>`;
    s+=arrow(340,91,340,186)+text(367,117,language==='fa'?'موج فرودی':'Incident wave')+arrow(440,186,440,98)+text(463,123,'r')+arrow(440,225,440,316)+text(463,293,'t');
    s+=text(205,236,'z = 0')+text(400,355,w.dimension,'text-anchor="middle"')+text(400,391,w.sheetNote,'text-anchor="middle" class="small"');
    return svg(w.sheet,w.sheetView,s,420);
  }
  globalThis.BookGeometry={ridge,slab,sheet};
  if(typeof module!=='undefined'&&module.exports)module.exports=globalThis.BookGeometry;
})();
