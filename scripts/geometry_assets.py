"""Embed the one shared drawing implementation in standalone offline explorers."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def embed_geometry(template):
    marker = '__MODEL_GEOMETRY_JS__'
    assert template.count(marker) == 1, 'Expected one shared geometry implementation marker'
    return template.replace(marker, (ROOT/'templates/model-geometry.js').read_text(encoding='utf-8'))
