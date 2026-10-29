"""Record explicitly selected English sources after reviewing their Persian pair."""
import argparse
import json
from validate_translations import ROOT, digest

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('sources', nargs='+', help='Reviewed repository-relative English paths; no wildcard or implicit all-pages mode')
args = parser.parse_args()
manifest = json.loads((ROOT / 'translations/languages.json').read_text(encoding='utf-8'))
pairs = {row['source']: row['translation'] for row in manifest['pages']}
path = ROOT / 'translations/source-lock.json'
lock = json.loads(path.read_text(encoding='utf-8'))
for source in args.sources:
    if source not in pairs or not (ROOT / pairs[source]).is_file():
        parser.error(f'Not a registered English–Persian pair: {source}')
    lock[source] = digest(ROOT / source)
path.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Recorded {len(args.sources)} explicitly selected source locks. This records your review decision; it does not judge translation quality.')
