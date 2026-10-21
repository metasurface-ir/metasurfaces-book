"""Scientific checks for the restricted TE solver and saved Chapter 3 library.

python scripts/validate_chapter03.py --grcwa
The optional comparison requires requirements-validation.txt. It compares an
independent RCWA implementation, not a different numerical method or experiment.
"""
import argparse
from dataclasses import replace
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'simulations'))
from unit_cell_te import Cell, solve_cell, film_reference, sample_ey


def grcwa_result(cell, half_order, pixels):
    import grcwa
    obj = grcwa.obj(2*half_order+3, [cell.period_um, 0], [0, cell.period_um/100],
                    1/cell.wavelength_um, np.deg2rad(cell.angle_deg), 0, verbose=0)
    obj.Add_LayerUniform(0, cell.n_incident**2)
    obj.Add_LayerGrid(cell.height_um, pixels, 1)
    obj.Add_LayerUniform(0, cell.n_substrate**2)
    obj.Init_Setup()
    assert obj.nG == 2*half_order+1 and np.all(obj.G[:, 1] == 0)
    # Independent FFT convolution: average the rectangle over each raster cell.
    dx = cell.period_um/pixels
    edges = np.linspace(-cell.period_um/2, cell.period_um/2, pixels+1)
    overlap = np.maximum(0, np.minimum(edges[1:], cell.width_um/2)-np.maximum(edges[:-1], -cell.width_um/2))
    eps = cell.n_gap**2 + (cell.n_ridge**2-cell.n_gap**2)*overlap/dx
    obj.GridLayer_geteps(eps)
    obj.MakeExcitationPlanewave(0, 0, 1, 0)
    R, T = obj.RT_Solve(normalize=1, byorder=1)
    E, _ = obj.Solve_FieldFourier(2, 0)
    return dict(R=np.asarray(R), T=np.asarray(T), t0=complex(E[1][0]),
                alpha=np.asarray(obj.kx)*cell.wavelength_um/(2*np.pi))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grcwa', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT/'data/chapter-03/validation.json')
    args = parser.parse_args()
    report = dict(environment=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
                  solver_sha256=hashlib.sha256((ROOT/'simulations/unit_cell_te.py').read_bytes()).hexdigest())
    c = Cell()
    errors = []
    for angle in [0., 20., 45.]:
        for height in [0., .17, .6]:
            for width, index in [(0., c.n_gap), (c.period_um, c.n_ridge)]:
                cell = replace(c, width_um=width, height_um=height, angle_deg=angle)
                result = solve_cell(cell, 8)
                r, t = film_reference(cell, index)
                errors.extend([abs(result['r'][8]-r), abs(result['t'][8]-t)])
    assert max(errors) < 1e-10
    report['analytic_films'] = dict(cases=18, max_complex_error=max(errors))
    flat = solve_cell(replace(c, period_um=3., height_um=0), 8)
    assert max(np.max(np.abs(np.delete(flat['r'], 8))), np.max(np.abs(np.delete(flat['t'], 8)))) < 1e-10
    assert abs(flat['T_total']-.96) < 1e-10
    report['artificial_supercell_flat_interface'] = 'nonzero orders have zero amplitude'
    multi = replace(c, period_um=1.4, width_um=.5, angle_deg=20.)
    plus, minus = solve_cell(multi, 24), solve_cell(replace(multi, angle_deg=-20.), 24)
    assert set(plus['orders'][plus['qi'].real>0]) == {-1, 0}
    assert set(plus['orders'][plus['qt'].real>0]) == {-1, 0, 1}
    mirror_error = max(np.max(abs(plus['R']-minus['R'][::-1])), np.max(abs(plus['T']-minus['T'][::-1])))
    assert mirror_error < 1e-10 and plus['balance_error'] < 1e-10
    report['multiorder_mirror'] = dict(reflected_open=[-1, 0], transmitted_open=[-1, 0, 1], max_order_power_error=float(mirror_error))
    result = solve_cell(c, 24)
    x = np.linspace(-c.period_um/2, c.period_um/2, 101)
    boundary_fields = sample_ey(c, result, x, np.array([-1e-8, 0., c.height_um, c.height_um+1e-8]))
    jump = max(np.max(abs(boundary_fields[0]-boundary_fields[1])), np.max(abs(boundary_fields[2]-boundary_fields[3])))
    assert jump < 1e-5
    report['field_continuity'] = dict(offset_um=1e-8, max_field_difference=float(jump))
    rejected = 0
    for bad in [replace(c, width_um=-.1), replace(c, height_um=-.1), replace(c, n_ridge=-1),
                replace(c, wavelength_um=0), replace(c, angle_deg=90), replace(c, width_um=float('nan')),
                replace(c, period_um=1.55)]:
        try:
            solve_cell(bad, 8)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('Invalid input or exact cutoff was accepted')
    for M in [-1, 1.5, True]:
        try:
            solve_cell(c, M)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('Invalid harmonic order was accepted')
    report['input_guards'] = dict(rejected_cases=rejected)
    library = json.loads((ROOT/'data/chapter-03/response-library.json').read_text())
    assert library['metadata']['source_sha256'] == report['solver_sha256']
    assert library['rows'] and all(row['accepted'] for row in library['rows'])
    library_cell = Cell(**library['metadata']['parameters'])
    spot_errors = []
    for row in library['rows'][::max(1, len(library['rows'])//5)] + library['rows'][-1:]:
        reference = solve_cell(replace(library_cell, width_um=row['width_um']), 48)
        spot_errors.append(abs(complex(row['t_real'], row['t_imag'])-reference['t'][48]))
    assert max(spot_errors) < library['metadata']['thresholds']['delta_complex_t']
    report['library'] = dict(rows=len(library['rows']), all_accepted=True,
                            refinement=f"{library['metadata']['harmonics']} vs {library['metadata']['check_harmonics']} harmonics at every width", M48_spot_cases=len(spot_errors),
                            max_spot_complex_error=max(spot_errors),
                            max_width_delta_t=max(row['delta_t'] for row in library['rows']),
                            phase_span_deg=library['metadata']['unwrapped_phase_span_deg'])
    if args.grcwa:
        comparisons = []
        cases = [replace(c, width_um=width, angle_deg=angle) for width in [.15, .325, .5] for angle in [0., 20.]]
        cases += [multi, replace(multi, angle_deg=-20.)]
        for cell in cases:
            ours = solve_cell(cell, 16)
            records = []
            for pixels in [256, 2048]:
                external = grcwa_result(cell, 16, pixels)
                mapping = np.array([np.argmin(abs(ours['alpha']-a)) for a in external['alpha']])
                assert max(abs(ours['alpha'][mapping]-external['alpha'])) < 1e-10
                dp = max(np.max(abs(ours['R'][mapping]-external['R'])), np.max(abs(ours['T'][mapping]-external['T'])))
                dt = abs(ours['t'][16]-external['t0'])
                records.append(dict(raster_pixels=pixels, max_order_power_error=float(dp), complex_t0_error=float(dt)))
            assert records[-1]['max_order_power_error'] < 1e-4 and records[-1]['complex_t0_error'] < 1e-4
            comparisons.append(dict(width_um=cell.width_um, period_um=cell.period_um, angle_deg=cell.angle_deg, comparisons=records))
        report['independent_implementation'] = dict(package='grcwa', version=importlib.metadata.version('grcwa'),
                interpretation='Separate RCWA implementation, with a separately refined raster representation. Not an FDTD/FEM or experimental comparison.',
                half_order=16, tolerance=1e-4, cases=comparisons)
    else:
        report['independent_implementation'] = dict(status='not run; use --grcwa with requirements-validation.txt')
    report['status'] = 'passed'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
