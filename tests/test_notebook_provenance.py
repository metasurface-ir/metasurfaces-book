"""Ensure stale scientific evidence fails without requiring a solver sweep."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.check_notebook_provenance import snapshot, check_record


class NotebookProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.name = '08-communication-links'
        self.files = {
            'requirements-labs.txt': 'numpy==2.4.6\n',
            'simulations/communication_link.py': 'GAIN = 1\n',
            'data/chapter-08/reference.json': json.dumps({'parameters': {'gain': 1}, 'power': 2}),
        }
        self.notebook = {'cells': [
            {'cell_type': 'markdown', 'source': ['Narrative']},
            {'cell_type': 'code', 'source': ['gain = 1\n', 'print(2)'], 'execution_count': 1,
             'outputs': [{'output_type': 'stream', 'name': 'stdout', 'text': ['2\n']}]}]}
        self.files['notebooks/' + self.name + '.ipynb'] = json.dumps(self.notebook)
        self.restore()
        self.record = snapshot(self.name, self.root)

    def restore(self):
        for name, text in self.files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')

    def write_notebook(self, notebook):
        (self.root / 'notebooks' / (self.name + '.ipynb')).write_text(json.dumps(notebook), encoding='utf-8')

    def test_detects_code_output_dependency_result_and_parameter_changes(self):
        for kind in ('code', 'output', 'module', 'pins', 'result', 'parameter'):
            with self.subTest(kind=kind):
                self.restore()
                book = copy.deepcopy(self.notebook)
                if kind in ('code', 'output'):
                    if kind == 'code': book['cells'][1]['source'][0] = 'gain = 10\n'
                    else: book['cells'][1]['outputs'][0]['text'] = ['20\n']
                    self.write_notebook(book)
                else:
                    file = {'module': 'simulations/communication_link.py', 'pins': 'requirements-labs.txt',
                            'result': 'data/chapter-08/reference.json', 'parameter': 'data/chapter-08/reference.json'}[kind]
                    value = {'module': 'GAIN = 10\n', 'pins': 'numpy==0.0.1\n',
                             'result': '{"parameters":{"gain":1},"power":20}',
                             'parameter': '{"parameters":{"gain":10},"power":2}'}[kind]
                    (self.root / file).write_text(value, encoding='utf-8')
                with self.assertRaisesRegex(AssertionError, 'stale'):
                    check_record(self.name, self.record, self.root)

    def test_narrative_and_platform_line_endings_do_not_invalidate_science(self):
        book = copy.deepcopy(self.notebook)
        book['cells'][0]['source'] = ['Translated narrative']
        self.write_notebook(book)
        (self.root / 'simulations/communication_link.py').write_bytes(b'GAIN = 1\r\n')
        check_record(self.name, self.record, self.root)

    def test_missing_execution_and_saved_errors_are_rejected(self):
        for state in ('missing', 'error'):
            with self.subTest(state=state):
                book = copy.deepcopy(self.notebook)
                if state == 'missing': book['cells'][1]['execution_count'] = None
                else: book['cells'][1]['outputs'] = [{'output_type': 'error', 'ename': 'ValueError'}]
                self.write_notebook(book)
                with self.assertRaises(AssertionError): snapshot(self.name, self.root)

    def test_ci_scientific_pins_match_notebook_environment(self):
        def pins(path):
            return dict(line.strip().split('==', 1) for line in path.read_text().splitlines()
                        if line.strip() and not line.startswith('#') and '==' in line)
        full = pins(ROOT / 'requirements-labs.txt')
        for package, version in pins(ROOT / 'requirements-checks.txt').items():
            self.assertEqual(full[package], version, package)


if __name__ == '__main__':
    unittest.main()
