"""Copy tagged, saved notebook PNG outputs into the chapter assets.

Run after restarting and executing the comparison notebook, from any directory:
    python scripts/export_chapter10_figures.py
No additional Python packages are required. This does not execute the notebook.
"""
import base64
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
notebook = json.loads((root / "notebooks/10-neural-comparison.ipynb").read_text(encoding="utf-8"))
destination = root / "assets/chapter-10"
destination.mkdir(parents=True, exist_ok=True)

for tag, filename in {
    "ch10-model-comparison": "model-comparison.png",
    "ch10-inverse-comparison": "inverse-comparison.png",
    "ch10-passivity-locus": "passivity-locus.png",
}.items():
    cells = [cell for cell in notebook["cells"] if tag in cell.get("metadata", {}).get("tags", [])]
    if len(cells) != 1 or cells[0].get("execution_count") is None:
        raise ValueError(f"Expected one executed cell tagged {tag}")
    outputs = [out["data"]["image/png"] for out in cells[0].get("outputs", [])
               if "image/png" in out.get("data", {})]
    if len(outputs) != 1:
        raise ValueError(f"Expected exactly one saved PNG for {tag}")
    data = outputs[0]
    path = destination / filename
    path.write_bytes(base64.b64decode("".join(data) if isinstance(data, list) else data))
    print(path.relative_to(root))
