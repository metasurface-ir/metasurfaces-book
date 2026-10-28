"""Attach the book's content/code notices and citation metadata to source ZIPs."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FILES = ('LICENSE', 'LICENSES/MIT.txt', 'LICENSES/CC-BY-4.0.txt', 'CITATION.cff', 'CONTRIBUTORS.md', 'VERSION')


def write_notices(archive):
    for name in FILES:
        if name not in archive.namelist():
            archive.write(ROOT / name, name)
