"""Regression cases from Section 1 of the October 2026 whole-book review.

Run: OPENBLAS_NUM_THREADS=1 python -m unittest discover -s tests -v
Notebooks run in temporary copies; published reference data are never edited.
"""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT),str(ROOT/'simulations')]
from simulations.source_provenance import check_reference, notebook_code_sha256, json_sha256, result_sha256
from simulations.tunable_surface import Surface, response, unwrapped_phase_deg
from simulations.materials_measurement import Experiment, uncertain_measurements, covariance_region
from design_studies import bandwidth
from scripts.validate_chapter01 import check_saved_reference


@contextlib.contextmanager
def notebook_run(name, cells=None, replacements=()):
    """Execute the actual notebook cells after student-style source edits."""
    with tempfile.TemporaryDirectory(prefix='metasurface-section01-') as folder:
        root=Path(folder)
        for directory in ('simulations','scripts'):
            shutil.copytree(ROOT/directory,root/directory,ignore=shutil.ignore_patterns('__pycache__'))
        (root/'notebooks').mkdir()
        book=json.loads((ROOT/'notebooks'/f'{name}.ipynb').read_text(encoding='utf-8'))
        for index,old,new in replacements:
            source=''.join(book['cells'][index]['source'])
            assert old in source,(name,index,old)
            book['cells'][index]['source']=source.replace(old,new).splitlines(True)
        (root/'notebooks'/f'{name}.ipynb').write_text(json.dumps(book),encoding='utf-8')
        namespace={'__name__':'__notebook__'}
        old_cwd=Path.cwd();old_show=plt.show
        try:
            os.chdir(root);plt.show=lambda:None
            with contextlib.redirect_stdout(io.StringIO()):
                for index,cell in enumerate(book['cells']):
                    if cell['cell_type']=='code' and (cells is None or index in cells):
                        exec(compile(''.join(cell['source']),f'{name}:cell{index}','exec'),namespace)
            yield namespace,root
        finally:
            plt.close('all');plt.show=old_show;os.chdir(old_cwd)


class SectionOneTests(unittest.TestCase):
    def test_ch01_nonresonant_frequency_and_saved_audit(self):
        with notebook_run('01-first-metasurface-model',replacements=[(1,'FREQUENCY_THz=200.','FREQUENCY_THz=180.')]) as (ns,root):
            record=json.loads((root/'data/chapter-01/sheet-response.json').read_text())
            self.assertAlmostEqual(record['presets']['electric']['phase_deg'],49.8207660781,places=8)
            check_saved_reference(record)
            record['presets']['electric']['phase_deg']=None
            with self.assertRaises(AssertionError):check_saved_reference(record)

    def test_ch02_edited_film_and_propagating_field(self):
        edits=[(1,'THICKNESS_UM=WAVELENGTH_UM/(4*N_FILM)','THICKNESS_UM=1.1*WAVELENGTH_UM/(4*N_FILM)'),
               (1,'FIELD_ANGLE_DEG=50.','FIELD_ANGLE_DEG=30.')]
        with notebook_run('02-waves-and-interfaces',replacements=edits) as (ns,root):
            self.assertAlmostEqual(float(ns['film_reference']['R']),.0010186172713963,places=12)
            self.assertEqual(ns['regime'],'propagating')
            self.assertAlmostEqual(ns['field_checks']['max_transmitted_flux'],.8942272088549571,places=12)
            self.assertLess(ns['field_checks']['max_transmitted_flux_error'],1e-12)
            record=json.loads((root/'data/chapter-02/waves-reference.json').read_text())
            path=root/'notebooks/02-waves-and-interfaces.ipynb'
            check_reference(record,path)
            for target in ('parameters','result','code'):
                changed=copy.deepcopy(record)
                if target=='parameters':changed['parameters']['thickness_um']*=2
                elif target=='result':changed['checks']['film_unitarity_error']=.5
                else:changed['metadata']['notebook_code_sha256']='0'*64
                with self.assertRaises(AssertionError):check_reference(changed,path)

    def test_code_hash_ignores_translation_and_outputs_but_not_code(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'notebook.ipynb'
            book={'cells':[{'cell_type':'markdown','source':['English']},
                           {'cell_type':'code','source':['x=1\n'],'outputs':[]}]}
            path.write_text(json.dumps(book));first=notebook_code_sha256(path)
            book['cells'][0]['source']=['فارسی'];book['cells'][1]['outputs']=[{'text':'output'}]
            path.write_text(json.dumps(book));self.assertEqual(first,notebook_code_sha256(path))
            book['cells'][1]['source']=['x=2\n'];path.write_text(json.dumps(book))
            self.assertNotEqual(first,notebook_code_sha256(path))

    def test_ch03_oblique_fresnel_and_domain_guard(self):
        edits=[(1,'angle_deg=0.0','angle_deg=20.0')]
        with notebook_run('03-unit-cell-library',cells=[1,3,5],replacements=edits) as (ns,root):
            self.assertAlmostEqual(ns['flat']['r'][8].real,-.216981412473,places=10)
            self.assertAlmostEqual(ns['flat']['t'][8].real,.783018587527,places=10)
            guard=ns['require_single_order_library'];Cell=ns['Cell']
            with self.assertRaisesRegex(ValueError,'only m=0'):guard(Cell(period_um=1.4))
            with self.assertRaisesRegex(ValueError,'only m=0'):guard(Cell(period_um=1.55/1.5))
            guard(Cell(n_incident=1.1,n_substrate=1.4,angle_deg=10))

    def test_ch07_edited_circuit_frequency_and_feedback_export(self):
        edits=[(1,'P=Surface()','P=Surface(resistance_ohm=150.,exponent=2.)'),
               (1,'FREQUENCY_GHZ=10.','FREQUENCY_GHZ=11.')]
        with notebook_run('07-tunable-metasurfaces',replacements=edits) as (ns,root):
            p=ns['P'];x=ns['x'];actual=ns['actual']
            states=response(11.,np.linspace(0,p.voltage_max_V,16),p)['gamma']
            desired=np.exp(2j*np.pi*x*np.sin(np.deg2rad(25.)))
            indices=np.argmin(abs(states[None,:]-desired[:,None])**2,axis=1)
            expected=abs(np.mean(states[indices]*np.exp(-2j*np.pi*x*np.sin(np.deg2rad(25.)))))**2
            self.assertAlmostEqual(actual['target_metric'],expected,places=12)
            self.assertAlmostEqual(float(x[1]-x[0]),.55,places=12)
            self.assertAlmostEqual(ns['chosen'],8.5247047198,places=6)
            record=json.loads((root/'data/chapter-07/reference.json').read_text())
            row=next(r for r in record['beams'] if r['target_deg']==25)
            circuit=next(r for r in row['variants'] if r['key']=='circuit4')
            self.assertAlmostEqual(circuit['target_metric'],expected,places=12)
            self.assertEqual(record['metadata']['operating_frequency_GHz'],11.)

    def test_ch07_zero_phase_gap_and_disconnected_segments(self):
        p=Surface(resistance_ohm=Surface().impedance_ohm)
        f=1/(2*np.pi*np.sqrt(p.inductance_nH*1e-9*p.capacitance0_pF*1e-12/9))/1e9
        g=response(f,[7.,8.,9.],p)['gamma']
        self.assertLess(abs(g[1]),1e-10)
        phase=unwrapped_phase_deg(g)
        self.assertTrue(np.isnan(phase[1]));self.assertTrue(np.isfinite(phase[[0,2]]).all())
        values=np.exp(1j*np.deg2rad([170,179,0,-179,-170]));values[2]=0
        np.testing.assert_allclose(unwrapped_phase_deg(values),[170,179,np.nan,-179,-170],equal_nan=True)

    def test_ch08_nonunity_gains_scale_every_path(self):
        with notebook_run('08-communication-links',cells=[1,5]) as (ns,root):
            original=(ns['gain0'],ns['far_gain'].copy(),ns['direct_amp'])
        with notebook_run('08-communication-links',cells=[1,5],replacements=[(1,'p = Link()','p = Link(tx_gain=10.,rx_gain=10.)')]) as (ns,root):
            self.assertAlmostEqual(ns['gain0']/original[0],100.,places=10)
            np.testing.assert_allclose(ns['far_gain']/original[1],100.)
            self.assertAlmostEqual((ns['direct_amp']/original[2])**2,100.,places=10)

    def test_ch09_resonance_tolerance_follow_parameters(self):
        with notebook_run('09-fabrication-measurement',cells=[1,5,7],replacements=[(1,'p=Experiment()','p=Experiment(resonance_GHz=12.,tolerance_GHz=.2)')]) as (ns,root):
            evidence=ns['evidence'];t=evidence['tolerance']
            self.assertEqual(t['acceptance_center_GHz'],12.)
            self.assertEqual(t['acceptance_tolerance_GHz'],.2)
            edges=np.array(t['edges_GHz'])
            for row in t['rows'].values():
                hist=np.array(row['histogram']);self.assertTrue(np.isfinite(hist).all())
                self.assertAlmostEqual(float(np.dot(hist,np.diff(edges))),1.,places=12)
            f=ns['f'];self.assertLess(f[0],12.);self.assertGreater(f[-1],12.)
            self.assertAlmostEqual(f[len(f)//2],12.)

    def test_ch09_zero_uncertainty_and_rank_one(self):
        p=Experiment(noise_rms=0,standard_phase_std_deg=0,load_std=0,position_std_mm=0)
        g,_=uncertain_measurements(2000,p)
        point=covariance_region(np.column_stack([g.real,g.imag]))
        self.assertEqual(point['rank'],0);self.assertEqual(point['sample_fraction'],1.)
        self.assertTrue(np.isfinite(point['boundary']).all())
        rng=np.random.default_rng(17);t=rng.normal(size=20000)
        line=covariance_region(np.column_stack([t,2*t]))
        self.assertEqual(line['rank'],1);self.assertAlmostEqual(line['threshold'],3.8414588207,places=8)
        self.assertAlmostEqual(line['sample_fraction'],.95,delta=.01)
        area=covariance_region(rng.normal(size=(20000,2)))
        self.assertEqual(area['rank'],2);self.assertAlmostEqual(area['threshold'],5.9914645471,places=8)
        self.assertAlmostEqual(area['sample_fraction'],.95,delta=.01)

    def test_bandwidth_intersects_separate_constraints(self):
        rows=[dict(wavelength_um=x,T=t,angle_deg=a) for x,t,a in zip([1.,2.,3.],[.9,.85,.84],[-2.,0.,2.])]
        b=bandwidth(rows,2.,.8,1.)
        self.assertEqual((b['lower_um'],b['upper_um']),(1.5,2.5))
        self.assertFalse(b['left_clipped']);self.assertFalse(b['right_clipped'])
        self.assertTrue(bandwidth(rows,2.,.8)['right_clipped'])
        self.assertIsNone(bandwidth(rows,2.,.9,1.))
        data=json.loads((ROOT/'data/design-studies/dispersion.json').read_text())
        b=bandwidth(data['rows'],1.55,.8,.213)
        self.assertAlmostEqual(b['upper_um'],1.5709596376,places=9)

    def test_dispersion_shading_uses_requirement(self):
        with notebook_run('09-dispersion',cells=[1]) as (ns,root):
            data=json.loads((ROOT/'data/design-studies/dispersion.json').read_text())
            ns.update(rows=data['rows'],design=ns['Design'](),anchor_um=1.55,efficiency_threshold=.8,angle_tolerance_deg=.213,
                      bands=[dict(efficiency=None,usable=None)])
            book=json.loads((ROOT/'notebooks/09-dispersion.ipynb').read_text(encoding='utf-8'))
            exec(''.join(book['cells'][5]['source']),ns)
            band=ns['ax'][2].patches[0]
            self.assertAlmostEqual(band.get_height(),2*.213,places=12)

    def test_inverse_budget_failure_is_saved_and_finishes(self):
        with notebook_run('11-inverse-design',replacements=[(3,'starts=2,maxfev=1000','starts=1,maxfev=1')]) as (ns,root):
            report=json.loads((root/'data/design-studies/inverse-design.json').read_text())
            self.assertEqual(report['stage'],'investigation_complete')
            self.assertEqual(len(report['optimization']['history']),1)
            self.assertFalse(report['optimization']['runs'][0]['success'])
            self.assertFalse(report['validation']['improved'])
            self.assertTrue(report['validation']['refinement_passed'])
            self.assertEqual(len(report['held_out']),4)


if __name__=='__main__':unittest.main()
