"""Render the shared, audited Chapter 9 arrays in English or Persian."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def render(destination,language='en'):
    assert language in ('en','fa')
    data=json.loads((ROOT/'data/chapter-09/reference.json').read_text(encoding='utf-8'))
    audit=json.loads((ROOT/'data/chapter-09/validation.json').read_text(encoding='utf-8'))
    digest=hashlib.sha256((ROOT/'simulations/materials_measurement.py').read_text(encoding='utf-8').encode()).hexdigest()
    assert data['metadata']['source_sha256']==audit['source_sha256']==digest
    assert audit['status']=='passed' and data['metadata']['parameters']==audit['parameters']
    template=(ROOT/'templates/measurement-explorer.html').read_text(encoding='utf-8')
    assert template.count('__CH09_DATA__')==1
    result=template.replace('__CH09_DATA__',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c'))
    result=result.replace('<html lang="en">',f'<html lang="{language}">',1)
    path=Path(destination);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(result,encoding='utf-8',newline='\n')
if __name__=='__main__':render(ROOT/'interactives/measurement-explorer.html')
