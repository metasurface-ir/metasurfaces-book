"""Execute Chapter 6 reference sweeps and independent numerical checks.

python scripts/validate_chapter06.py
python scripts/validate_chapter06.py --output-dir /path/to/temporary/audit

The core is a 1D normal-incidence FDFD slab, not an FDTD/FEM or patterned-cell
validation. Expected-failure demonstrations pass when their predicted failure
is observed. The optional grcwa package is not required for this script.
"""
import argparse
import csv
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'simulations'))
from numerical_methods import (MODEL_VERSION, Slab, exact_slab,
                               exact_slab_fields, phase_error_deg, solve_slab,
                               slab_sheet_approximation, summarize_result)
from unit_cell_te import Cell, solve_cell


SOURCES = [
    dict(id='schneider2010fdtd', author='John B. Schneider', year=2010,
         title='Understanding the Finite-Difference Time-Domain Method',
         url='https://eecs.wsu.edu/~schneidj/ufdtd/',
         use='Numerical dispersion and boundary context; the course core is FDFD.'),
    dict(id='meep-convergence', author='Meep project',
         title='FAQ: Checking convergence',
         url='https://meep.readthedocs.io/en/latest/FAQ/#checking-convergence',
         use='Separate approximation controls; no Meep run is claimed.'),
    dict(id='meep-pml', author='Meep project', title='Perfectly Matched Layers',
         url='https://meep.readthedocs.io/en/latest/Perfectly_Matched_Layer/',
         use='Optional PML extension; the implemented boundary is not PML.'),
    dict(id='moharam1995stable', year=1995,
         author='M. G. Moharam; Drew A. Pommet; Eric B. Grann; T. K. Gaylord',
         title='Stable implementation of the rigorous coupled-wave analysis for surface-relief gratings: enhanced transmittance matrix approach',
         journal='Journal of the Optical Society of America A', volume=12,
         pages='1077-1086', doi='10.1364/JOSAA.12.001077',
         url='https://opg.optica.org/josaa/abstract.cfm?uri=josaa-12-5-1077',
         use='Stability context; no claim to implement this exact enhanced algorithm.'),
    dict(id='li1996fourier', year=1996, author='Lifeng Li',
         title='Use of Fourier series in the analysis of discontinuous periodic structures',
         journal='Journal of the Optical Society of America A', volume=13,
         pages='1870-1876', doi='10.1364/JOSAA.13.001870',
         url='https://opg.optica.org/josaa/abstract.cfm?uri=josaa-13-9-1870',
         use='Fourier factorization extension; no TM implementation is claimed.'),
    dict(id='roy2011framework', year=2011,
         author='Christopher J. Roy; William L. Oberkampf',
         title='A comprehensive framework for verification, validation, and uncertainty quantification in scientific computing',
         journal='Computer Methods in Applied Mechanics and Engineering', volume=200,
         pages='2131-2144', doi='10.1016/j.cma.2011.03.016',
         url='https://www.sciencedirect.com/science/article/pii/S0045782511001290',
         use='Distinguish numerical verification, model error, and experimental validation.')]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scalar_complex(value):
    return dict(real=float(value.real), imag=float(value.imag))


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def boundary_equation_reference(slab):
    """Independent four-amplitude E/E' matching, with t at the exit face."""
    ne, nf = slab.n_exterior, slab.n_film
    p = np.exp(2j*np.pi*nf*slab.thickness_um/slab.wavelength_um)
    matrix = np.array([[1, -1, -1, 0], [-ne, -nf, nf, 0],
                       [0, p, 1/p, -1], [0, nf*p, -nf/p, -ne]], complex)
    r, _, _, t = np.linalg.solve(matrix, np.array([-1, -ne, 0, 0], complex))
    return r, t


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'data/chapter-06')
    args = parser.parse_args()
    start = time.perf_counter()
    slab = Slab()
    exact = exact_slab(slab)
    hashes = {name: digest(ROOT/'simulations'/name) for name in
              ['numerical_methods.py', 'waves_interfaces.py', 'unit_cell_te.py']}
    metadata = dict(schema='metasurface-numerical-methods-v1', model=MODEL_VERSION,
        parameters=asdict(slab), units='micrometers; degrees for reported phase',
        time_convention='exp(-i omega t)', field='normal-incidence tangential Ey',
        phase_references=dict(incident='one at z=0', r='z=0', t='z=thickness'),
        grid='node-centered; h=d/N; film faces on nodes; arithmetic half-cell epsilon at each face',
        flux='equal exteriors; J=Im(conj(E_j)*E_(j+1))/sin(theta); T_net=T_forward-T_backward',
        boundary='exact discrete radiation condition, or deliberately mismatched continuum multiplier',
        reference='Independent exact Chapter 2 Fresnel/Fabry-Perot film',
        source_sha256=hashes,
        environment=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
        exact=dict(r=scalar_complex(exact['r']), t=scalar_complex(exact['t']),
                   R=float(exact['R']), T=float(exact['T']), phase_deg=float(exact['phase_deg'])),
        thresholds=dict(default_complex_t=1e-4, residual=1e-10, discrete_flux_defect=1e-10,
                        domain_complex_change=1e-10, phase_amplitude_floor=1e-12),
        scope=['1D real constant indices, isotropic nonmagnetic film, equal exteriors',
               'FDFD slab benchmark is independent of the RCWA numerical method',
               'It does not independently validate the patterned ridge grating',
               'No FDTD, FEM, PML, 3D, finite array, physical dispersion, loss, or experiment was run'],
        sources=SOURCES, source_metadata_checked='2026-10-23 against primary records')

    mesh = [summarize_result(solve_slab(slab, cells=N), exact)
            for N in [4, 8, 16, 32, 64, 128, 256, 512]]
    for j, row in enumerate(mesh):
        row['observed_order'] = (None if j == 0 else
            float(np.log2(mesh[j-1]['complex_t_error']/row['complex_t_error'])))
    assert mesh[-1]['complex_t_error'] < metadata['thresholds']['default_complex_t']
    assert all(1.9 < row['observed_order'] < 2.1 for row in mesh[-4:])
    assert all(row['energy_defect'] < 1e-10 and row['algebraic_residual'] < 1e-10 for row in mesh)
    assert mesh[0]['complex_t_error'] > .5 and abs(mesh[0]['phase_error_deg']) > 40

    # Fixed physical field window: d/2 exterior padding on either side.
    fields = []
    for N in [8, 64, 512]:
        result = solve_slab(slab, N, N//2, N//2)
        reference_field = exact_slab_fields(slab, result['z_um'])
        fields.append(dict(cells=N, step_um=result['step_um'],
            left_padding_cells=N//2, right_padding_cells=N//2,
            z_um=result['z_um'].tolist(), epsilon_r=result['epsilon_r'].tolist(),
            E_real=result['E'].real.tolist(), E_imag=result['E'].imag.tolist(),
            exact_E_real=reference_field.real.tolist(), exact_E_imag=reference_field.imag.tolist(),
            current_z_um=result['current_z_um'].tolist(), current=result['current'].tolist(),
            diagnostics=summarize_result(result, exact)))
        fields[-1]['diagnostics']['max_complex_field_error'] = float(np.max(abs(result['E']-reference_field)))
        assert np.max(abs(result['current']-(1-result['R']))) < 1e-10
    assert fields[-1]['diagnostics']['max_complex_field_error'] < 1e-4

    padding = []
    matched = solve_slab(slab, 8)
    for p in range(65):
        for boundary, deembed in [('discrete','discrete'), ('continuum','discrete'),
                                  ('discrete','continuum')]:
            result = solve_slab(slab, 8, p, p, boundary, deembed)
            row = summarize_result(result, exact)
            row['padding_cells'] = p
            row['padding_um'] = p*result['step_um']
            row['complex_t_vs_matched'] = float(abs(result['t']-matched['t']))
            row['phase_drift_deg'] = float(phase_error_deg(result['t'], matched['t']))
            drift = ((result['phase_step_rad']-result['continuum_phase_step_rad'])*2*p
                     if deembed == 'continuum' else 0.)
            row['predicted_deembed_drift_deg'] = float(np.rad2deg(np.angle(np.exp(1j*drift))))
            padding.append(row)
            assert result['energy_defect'] < 1e-10 and result['current_spread'] < 1e-10
            if boundary == 'discrete' and deembed == 'discrete':
                assert row['complex_t_vs_matched'] < 1e-10
            if deembed == 'continuum':
                assert abs(row['phase_drift_deg']-row['predicted_deembed_drift_deg']) < 1e-8
            if boundary == 'continuum':
                boundary_flux = (np.sin(result['continuum_phase_step_rad'])
                                 / np.sin(result['phase_step_rad'])*abs(result['E'][-1])**2)
                assert abs(result['T_net']-boundary_flux) < 1e-10
                assert result['T_backward'] > 0
    mismatched_R = [row['R'] for row in padding if row['boundary'] == 'continuum']
    assert np.ptp(mismatched_R) > 1e-3

    # Different physical inputs, independent continuous-film benchmarks.
    benchmark_cases = [slab, Slab(.8, .23, 1.7, 1.3), Slab(1.1, .37, 2.9, 1.2),
                       Slab(.65, .11, 1.25, 1.5), Slab(2., .9, 3.2, 1.),
                       Slab(.6, .06, 2.4, 1.)]
    benchmarks = []
    exact_reference_errors = []
    for case in benchmark_cases:
        result = solve_slab(case, 1024, 17, 31)
        row = summarize_result(result)
        assert max(row['complex_t_error'], row['complex_r_error']) < 5e-4
        analytic = exact_slab(case)
        matched_r, matched_t = boundary_equation_reference(case)
        exact_reference_errors.append(float(max(abs(analytic['r']-matched_r),
                                                abs(analytic['t']-matched_t))))
        benchmarks.append(dict(parameters=asdict(case), diagnostics=row))
    assert max(exact_reference_errors) < 1e-12

    homogeneous_errors = []
    for ne in [1., 1.5, 2.]:
        case = replace(slab, n_film=ne, n_exterior=ne)
        for N in [8, 32, 128]:
            result = solve_slab(case, N, 3, 11)
            error = max(abs(result['r']), abs(result['t']-np.exp(1j*result['phase_step_rad']*N)))
            assert error < 1e-10
            homogeneous_errors.append(float(error))

    domain_errors = []
    base = solve_slab(slab, 32)
    for left, right in [(0,0), (1,0), (0,4), (4,16), (16,4), (64,64), (256,128)]:
        result = solve_slab(slab, 32, left, right)
        error = max(abs(result['r']-base['r']), abs(result['t']-base['t']))
        assert error < 1e-10
        domain_errors.append(float(error))

    rejected = 0
    bad_cases = [dict(slab=replace(slab, n_film=-1)),
                 dict(slab=replace(slab, thickness_um=0)),
                 dict(slab=replace(slab, wavelength_um=np.nan)),
                 dict(slab=replace(slab, n_exterior=1+1j)),
                 dict(slab=replace(slab, n_exterior=True)),
                 dict(cells=True), dict(cells=4.5), dict(cells=-1),
                 dict(left_padding_cells=-1), dict(right_padding_cells=2.5),
                 dict(right_boundary='pml'), dict(deembed='unknown'),
                 dict(slab=replace(slab, n_film=10), cells=2)]
    for kwargs in bad_cases:
        try:
            solve_slab(**kwargs)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError(f"Invalid mathematical/numerical input was accepted: {kwargs}")
    assert rejected == len(bad_cases)
    assert np.isnan(phase_error_deg(0, 1))
    assert abs(float(phase_error_deg(np.exp(1j*np.deg2rad(-179)),
                                   np.exp(1j*np.deg2rad(179))))-2) < 1e-10

    # Companion: same conservatively truncated RCWA family, high-order reference.
    cell = Cell()
    high = solve_cell(cell, 64)
    harmonics = []
    for M in [0, 1, 2, 4, 8, 16, 24, 32, 48, 64]:
        result = high if M == 64 else solve_cell(cell, M)
        t, r = result['t'][M], result['r'][M]
        harmonics.append(dict(half_order=M, retained_harmonics=2*M+1,
            t_real=float(t.real), t_imag=float(t.imag),
            r_real=float(r.real), r_imag=float(r.imag),
            R=result['R_total'], T=result['T_total'],
            energy_defect=result['balance_error'], algebraic_residual=result['solve_residual'],
            complex_t_error=float(abs(t-high['t'][64])),
            phase_error_deg=float(phase_error_deg(t, high['t'][64]))))
    assert harmonics[0]['complex_t_error'] > .2
    assert harmonics[-2]['complex_t_error'] < 5e-6
    assert all(row['energy_defect'] < 1e-10 for row in harmonics)

    model_comparison = []
    for d in slab.thickness_um*np.array([.01, .02, .05, .1, .2, .4, 1.]):
        case = replace(slab, thickness_um=float(d))
        model = slab_sheet_approximation(case)
        reference = exact_slab(case)
        model_comparison.append(dict(thickness_um=float(d),
            optical_thickness_rad=float(2*np.pi*case.n_film*d/case.wavelength_um),
            exact_t_real=float(reference['t'].real), exact_t_imag=float(reference['t'].imag),
            sheet_t_real=float(model['t'].real), sheet_t_imag=float(model['t'].imag),
            complex_t_difference=float(abs(model['t']-reference['t'])),
            phase_difference_deg=float(phase_error_deg(model['t'],reference['t'])),
            energy_defect=model['energy_defect']))
    assert model_comparison[0]['complex_t_difference'] < 1e-4
    assert model_comparison[-1]['complex_t_difference'] > .9
    assert max(row['energy_defect'] for row in model_comparison) < 1e-10

    # This is saved prior evidence, not a fresh Chapter 5 supercell rerun.
    chapter05_path = ROOT/'data/chapter-05/validation.json'
    chapter05 = json.loads(chapter05_path.read_text(encoding='utf-8'))
    chapter05_evidence = dict(status='read saved audit; not rerun by this script',
        path='data/chapter-05/validation.json', sha256=digest(chapter05_path),
        full_wave_refinement=chapter05['full_wave_refinement'],
        interpretation='1D TE periodic supercell harmonic refinement; not FDFD/FEM/FDTD validation of ridges')

    report = dict(status='passed', model=MODEL_VERSION, source_sha256=hashes,
        environment=metadata['environment'],
        analytic_benchmarks=dict(cases=benchmarks, tolerance_complex=5e-4,
            exact_fresnel_vs_boundary_equation_error=max(exact_reference_errors),
            interpretation='Exact model benchmark, not experimental validation'),
        homogeneous_discrete_dispersion=dict(cases=len(homogeneous_errors), max_error=max(homogeneous_errors)),
        spatial_refinement=dict(cells=[row['cells'] for row in mesh],
            final_complex_t_error=mesh[-1]['complex_t_error'],
            final_phase_error_deg=mesh[-1]['phase_error_deg'],
            final_observed_order=mesh[-1]['observed_order']),
        expected_failures=dict(
            coarse_mesh=dict(cells=4, complex_t_error=mesh[0]['complex_t_error'],
                phase_error_deg=mesh[0]['phase_error_deg'], energy_defect=mesh[0]['energy_defect'],
                algebraic_residual=mesh[0]['algebraic_residual']),
            boundary_mismatch=dict(cells=8, padding_range_cells=[0,64],
                reflection_power_span=float(np.ptp(mismatched_R)),
                reflection_amplitude=next(row['boundary_reflection_amplitude'] for row in padding
                                          if row['boundary'] == 'continuum')),
            wrong_deembedding=dict(cells=8, padding_cells_each_side=64,
                phase_drift_deg=padding[-1]['phase_drift_deg'])),
        discrete_boundary_domain_invariance=dict(cases=len(domain_errors), max_complex_change=max(domain_errors)),
        current_conservation=dict(max_field_case_spread=max(row['diagnostics']['current_spread'] for row in fields)),
        field_refinement=dict(cells=[row['cells'] for row in fields],
            max_complex_errors=[row['diagnostics']['max_complex_field_error'] for row in fields]),
        input_guards=dict(rejected_cases=rejected),
        harmonic_companion=dict(reference_half_order=64,
            M48_complex_t_difference=harmonics[-2]['complex_t_error'],
            M0_complex_t_difference=harmonics[0]['complex_t_error'],
            interpretation='RCWA harmonic convergence, with a numerical high-order reference'),
        model_comparison=dict(thin_complex_t_difference=model_comparison[0]['complex_t_difference'],
            thick_complex_t_difference=model_comparison[-1]['complex_t_difference'],
            interpretation='Difference of mathematical models; no experiment'),
        chapter05_saved_evidence=chapter05_evidence,
        limitations=metadata['scope'], runtime_seconds=time.perf_counter()-start)
    data = dict(metadata=metadata, mesh=mesh, fields=fields, padding=padding,
        harmonics_metadata=dict(parameters=asdict(cell), reference_half_order=64,
                                reference_kind='high-order numerical reference, not exact'),
        harmonics=harmonics, model_comparison=model_comparison,
        chapter05_saved_evidence=chapter05_evidence)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in [('numerical-reference.json', data), ('validation.json', report)]:
        (args.output_dir/filename).write_text(json.dumps(content, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    for filename, rows in [('mesh-sweep.csv',mesh), ('padding-sweep.csv',padding),
                           ('harmonic-sweep.csv',harmonics), ('model-comparison.csv',model_comparison)]:
        write_csv(args.output_dir/filename, rows)
    print(json.dumps(dict(status=report['status'], output_dir=str(args.output_dir),
        spatial_refinement=report['spatial_refinement'], expected_failures=report['expected_failures'],
        max_domain_change=max(domain_errors), benchmarks=len(benchmarks),
        rejected_inputs=rejected, runtime_seconds=report['runtime_seconds']), indent=2))


if __name__ == '__main__':
    main()
