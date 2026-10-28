"""Language-independent identities for saved notebook code and JSON results.

These hashes detect stale or changed artifacts; they are not a proof that an
unsaved editor buffer was executed or a substitute for independent physics checks.
"""
import hashlib
import json
from pathlib import Path


def json_sha256(value):
    encoded = json.dumps(value, sort_keys=True, separators=(',', ':'),
                         ensure_ascii=False, allow_nan=False).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


def notebook_code_sha256(path):
    notebook = json.loads(Path(path).read_text(encoding='utf-8'))
    code = [''.join(cell['source']).replace('\r\n', '\n')
            for cell in notebook['cells'] if cell['cell_type'] == 'code']
    return json_sha256(code)


def result_sha256(record):
    payload = dict(record)
    payload['metadata'] = dict(record['metadata'])
    payload['metadata'].pop('result_payload_sha256', None)
    return json_sha256(payload)


def check_reference(record, notebook_path):
    metadata = record['metadata']
    assert metadata['notebook_code_sha256'] == notebook_code_sha256(notebook_path), 'Saved notebook code differs; save and rerun all cells.'
    assert metadata['parameters_sha256'] == json_sha256(record['parameters']), 'Recorded parameters changed.'
    assert metadata['result_payload_sha256'] == result_sha256(record), 'Saved result payload changed.'
