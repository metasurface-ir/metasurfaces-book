"""Audit the published ms-09/10/11 reference; optional --grcwa replay.

Run the three notebooks first. New physical configurations need their own
acceptance criteria; this audit intentionally checks the stated baseline.
"""
import argparse
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'simulations'))
from design_studies import Design, passband, bandwidth, order_metrics, grcwa_check
from unit_cell_te import Cell, film_reference


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grcwa', action='store_true')
    args = parser.parse_args()
    data = {n:json.loads((ROOT/'data/design-studies'/f'{n}.json').read_text(encoding='utf-8'))
            for n in ['dispersion', 'coupling', 'inverse-design']}
    baseline = Design()
    for record in data.values():
        for name, digest in record['metadata']['sources'].items():
            assert hashlib.sha256((ROOT/'simulations'/name).read_text(encoding='utf-8').encode()).hexdigest() == digest
        expected = json.loads(json.dumps(asdict(baseline)))
        assert record['metadata']['parameters'] == expected
    # Bandwidth logic: disconnected windows, failed anchor, clipped edge, bad grid.
    band = passband([1,2,3,4,5], [-1,1,-1,1,-1], 2)
    assert band['lower_um'] == 1.5 and band['upper_um'] == 2.5
    assert passband([1,2,3,4,5], [-1,1,-1,1,-1], 3) is None
    assert passband([1,2,3], [1,1,1], 2)['left_clipped']
    assert passband([1,2,3], [-1,1,1], 2)['right_clipped']
    rejected = 0
    for x,y,a in [([1,1,2],[1,1,1],1), ([1,2,3],[1,np.nan,1],2), ([1,2,3],[1,1,1],2.5)]:
        try: passband(x,y,a)
        except ValueError: rejected += 1
    assert rejected == 3
    spectral = data['dispersion']
    assert len(spectral['rows']) == len(spectral['comparison']) == 161
    delta = max(abs(a['T']-b['T']) for a,b in zip(spectral['rows'],spectral['comparison']))
    assert delta < 1e-3 and np.isclose(delta, spectral['max_power_change'])
    for row in spectral['rows']:
        assert 0 <= row['T'] <= row['total_T']+1e-12 <= 1+1e-10
        assert row['balance_error'] < 1e-9 and row['residual'] < 1e-9
    edge_change = 0.
    for name,angle in [('efficiency',None),('usable',.5)]:
        b = bandwidth(spectral['rows'], 1.55, .8, angle)
        assert b == spectral['bandwidths'][-1][name]
        previous = spectral['bandwidths'][-2][name]
        edge_change = max(edge_change, abs(b['lower_um']-previous['lower_um']),abs(b['upper_um']-previous['upper_um']))
        assert not b['left_clipped'] and not b['right_clipped']
    assert edge_change < .001  # 1 nm acceptance for the two sampled grids.
    coupling = data['coupling']
    assert len(coupling['cases']) == 5 and coupling['uniform_embedding_error'] < 1e-10
    assert coupling['forbidden_amplitude'] < 1e-10
    for c in coupling['cases']:
        assert c['harmonic_power_change'] < 1e-4 and c['local_harmonic_change'] < 1e-4
        assert abs(sum(c['full_T'])+sum(c['full_R'])-1) < 1e-9
        assert np.isclose(np.mean(c['widths_um']), np.mean(baseline.widths_um))
    inverse = data['inverse-design']; history = inverse['optimization']['history']
    assert len(history) <= 2000 and len(inverse['optimization']['runs']) == 2
    best = -np.inf
    for row in history:
        assert all(.08 <= w <= .57 for w in row['widths_um'])
        best = max(best,row['T']); assert row['best_T'] == best
    assert inverse['optimization']['best']['T'] == best
    assert any(row['T'] == best and row['widths_um'] == inverse['selected_parameters']['widths_um'] for row in history)
    selected = Design(**inverse['selected_parameters'])
    results = inverse['refinement']
    current = order_metrics(selected.solve(192)); original = order_metrics(baseline.solve(192))
    assert abs(current['T']-results[-1]['selected']['T']) < 1e-10
    assert current['T'] > original['T']
    complex_change = abs(complex(current['t_real'],current['t_imag'])-complex(results[-2]['selected']['t_real'],results[-2]['selected']['t_imag']))
    assert complex_change < 1e-4
    assert abs(current['T']-results[-2]['selected']['T']) < 1e-4
    assert len(inverse['held_out']) == 4 and all(r['wavelength_um'] != 1.55 for r in inverse['held_out'])
    assert len(inverse['perturbations']) == 14
    # Independent analytic uniform-film limit of the actual supercell solver.
    uniform = replace(baseline, widths_um=(baseline.pitch_um,)*6)
    solved = uniform.solve(24)
    film = Cell(period_um=3.9, width_um=3.9, height_um=1.8)
    r,t = film_reference(film,2.4)
    film_error = max(abs(r-solved['r'][24]),abs(t-solved['t'][24]))
    assert film_error < 1e-10
    # Mirror invariance is a physical symmetry, independent of the search path.
    a = selected.solve(48); b = replace(selected,widths_um=tuple(reversed(selected.widths_um))).solve(48)
    mirror_error = max(abs(a['T']-b['T'][::-1]).max(),abs(a['R']-b['R'][::-1]).max())
    assert mirror_error < 1e-10
    external = inverse['independent_implementation']
    if args.grcwa:
        checks=[]
        for pixels in [4096,8192]:
            other=grcwa_check(selected,48,pixels); indices=other['orders']+48
            error=max(abs(a['R'][indices]-other['R']).max(),abs(a['T'][indices]-other['T']).max())
            checks.append(dict(pixels=pixels,max_order_power_error=float(error)))
        assert checks[-1]['max_order_power_error'] < 1e-4
        external=dict(status='passed; separate RCWA implementation, same method family',checks=checks)
    report=dict(status='passed',sources=spectral['metadata']['sources'],spectral_samples=161,
        max_spectral_harmonic_power_change=delta,band_edge_grid_change_um=edge_change,
        uniform_embedding_error=coupling['uniform_embedding_error'],uniform_film_complex_error=float(film_error),
        mirror_order_power_error=float(mirror_error),bandwidth_input_guards=rejected,
        objective_evaluations=len(history),baseline_T=original['T'],selected_T=current['T'],
        selected_refinement_complex_change=float(complex_change),independent_implementation=external,
        scope='Fixed reference studies; no FEM/FDTD, finite-device, measured material or experimental validation')
    (ROOT/'data/design-studies/validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__': main()
