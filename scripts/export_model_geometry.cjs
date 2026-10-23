/* Export original, bilingual geometry figures from the same saved model inputs
 * used by the interactive labs. No physics or simulation data are modified. */
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),g=require('../templates/model-geometry.js');
const read=name=>JSON.parse(fs.readFileSync(path.join(root,name),'utf8'));
const unit=read('data/chapter-03/response-library.json'),beam=read('data/chapter-05/beam-steering.json'),slab=read('data/chapter-06/numerical-reference.json');
const selected=beam.cases.find(c=>c.name==='expanded');
for(const language of ['en','fa']){
 const prefix=language==='fa'?'translations/fa/':'';
 const figures={
  'assets/chapter-03/unit-cell-geometry.svg':g.ridge(unit.metadata.parameters,[unit.metadata.parameters.width_um],language),
  'assets/chapter-05/supercell-geometry.svg':g.ridge({...beam.metadata.library_parameters,height_um:selected.height_um},selected.widths_um,language),
  'assets/chapter-06/slab-geometry.svg':g.slab(slab.metadata.parameters,8,0,language),
  'assets/chapter-10/analytical-sheet.svg':g.sheet(language)
 };
 for(const [name,svg] of Object.entries(figures)){fs.mkdirSync(path.dirname(path.join(root,prefix+name)),{recursive:true});fs.writeFileSync(path.join(root,prefix+name),svg+'\n');}
}
console.log('Exported four original geometry figures in English and Persian');
