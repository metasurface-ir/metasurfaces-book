"""Detect stale saved notebook code, outputs, input files, and result identities.

Recording a snapshot is not proof of execution or scientific correctness. Run
affected notebooks from fresh kernels and review them before using --record.
The normal check uses only the standard library and never runs scientific code.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'simulations'))
from source_provenance import notebook_code_sha256, json_sha256

GROUPS = {
    '01-first-metasurface-model': (['intro_sheet.py'], [], ['chapter-01/sheet-response.json', 'chapter-01/sheet-response.csv']),
    '02-waves-and-interfaces': (['waves_interfaces.py', 'source_provenance.py'], [], ['chapter-02/waves-reference.json', 'chapter-02/waves-reference.csv']),
    '03-unit-cell-library': (['unit_cell_te.py'], [], ['chapter-03/response-library.json', 'chapter-03/response-library.csv']),
    '04-floquet-orders': ([], [], []),
    '05-beam-steering': (['unit_cell_te.py', 'metasurface_synthesis.py'], ['chapter-03/response-library.json'], ['chapter-05/beam-steering.json', 'chapter-05/extended-library.csv']),
    '05-wavefront-models': (['unit_cell_te.py', 'metasurface_synthesis.py'], ['chapter-05/beam-steering.json'], ['chapter-05/wavefront-models.json']),
    '06-numerical-methods': (['numerical_methods.py', 'waves_interfaces.py', 'unit_cell_te.py'], ['chapter-05/beam-steering.json', 'chapter-06/numerical-reference.json', 'chapter-06/model-comparison.csv', 'chapter-06/harmonic-sweep.csv'], ['chapter-06/notebook-experiment.json']),
    '07-tunable-metasurfaces': (['tunable_surface.py'], [], ['chapter-07/reference.json', 'chapter-07/validation.json']),
    '08-communication-links': (['communication_link.py'], [], ['chapter-08/reference.json']),
    '09-fabrication-measurement': (['materials_measurement.py'], [], ['chapter-09/reference.json', 'chapter-09/synthetic-sweep.csv']),
    '09-dispersion': (['design_studies.py', 'unit_cell_te.py', 'metasurface_synthesis.py'], [], ['design-studies/dispersion.json']),
    '10-coupling': (['design_studies.py', 'unit_cell_te.py', 'metasurface_synthesis.py'], [], ['design-studies/coupling.json']),
    '11-inverse-design': (['design_studies.py', 'unit_cell_te.py', 'metasurface_synthesis.py'], [], ['design-studies/inverse-design.json']),
    '10-resonant-surrogate': ([], [], []),
    '10-neural-comparison': ([], [], []),
}

# This notebook executes its audit as part of its saved investigation.
SCRIPT_DEPENDENCIES = {'07-tunable-metasurfaces': ['scripts/validate_chapter07.py']}


def file_hash(path):
    text = path.read_text(encoding='utf-8').replace('\r\n', '\n')
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def parameters(value, prefix=''):
    """Collect explicitly named parameter records; other inputs remain in hashes."""
    result = {}
    if isinstance(value, dict):
        for key, child in value.items():
            location = prefix + '/' + key
            if 'parameters' in key.lower():
                result[location] = child
            else:
                result.update(parameters(child, location))
    return result


def snapshot(name, root=ROOT):
    path = root / 'notebooks' / (name + '.ipynb')
    notebook = json.loads(path.read_text(encoding='utf-8'))
    cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
    assert all(cell.get('execution_count') is not None for cell in cells if ''.join(cell['source']).strip()), f'Unexecuted code: {name}'
    assert not any(o.get('output_type') == 'error' for c in cells for o in c.get('outputs', [])), f'Saved execution error: {name}'
    modules, inputs, results = GROUPS[name]
    dependencies = (['simulations/' + p for p in modules] + ['data/' + p for p in inputs]
                    + SCRIPT_DEPENDENCIES.get(name, []) + ['requirements-labs.txt'])
    parameter_records = {}
    for filename in results:
        if filename.endswith('.json'):
            parameter_records[filename] = parameters(json.loads((root / 'data' / filename).read_text(encoding='utf-8')))
    return dict(code_sha256=notebook_code_sha256(path),
                saved_outputs_sha256=json_sha256([cell.get('outputs', []) for cell in cells]),
                dependencies={p: file_hash(root / p) for p in dependencies},
                generated_files={'data/' + p: file_hash(root / 'data' / p) for p in results},
                parameter_fields=parameter_records, parameter_fields_sha256=json_sha256(parameter_records))


def check_record(name, record, root=ROOT):
    current = snapshot(name, root)
    for key, value in current.items():
        assert record.get(key) == value, f'{name}: stale {key}; execute, review, and record the affected notebook again'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', nargs='*', metavar='NOTEBOOK', help='Record all notebooks, or selected stems, after fresh execution and review')
    args = parser.parse_args()
    path = ROOT / 'data/notebook-provenance.json'
    records = json.loads(path.read_text(encoding='utf-8')) if path.exists() else dict(
        schema=1, scope='Saved-artifact identity only; fresh-kernel execution and human scientific review are separate requirements.', notebooks={})
    assert set(GROUPS) == {p.stem for p in (ROOT / 'notebooks').glob('*.ipynb')}, 'Register every notebook and its file dependencies'
    if args.record is not None:
        for name in args.record or GROUPS:
            assert name in GROUPS, f'Unknown notebook: {name}'
            records['notebooks'][name] = snapshot(name)
        path.write_text(json.dumps(records, indent=2, ensure_ascii=False, allow_nan=False) + '\n', encoding='utf-8')
    assert set(records['notebooks']) == set(GROUPS), 'Missing notebook provenance records'
    for name in GROUPS:
        check_record(name, records['notebooks'][name])
    print(f'Passed: {len(GROUPS)} saved notebook code/output identities, registered dependencies/results, and explicitly recorded parameter fields. Execution and scientific correctness are not inferred from hashes.')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, KeyError, FileNotFoundError) as exc:
        sys.exit(str(exc))
