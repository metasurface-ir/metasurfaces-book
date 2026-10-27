"""Independent checks for the exact planar Chapter 2 teaching models.

Execute/save the Chapter 2 notebook first. This audit checks its module and
numerical-code identities, recorded parameters and saved result payload,
then writes data/chapter-02/validation.json. No patterned-geometry solver,
material-data fit, or fabricated-device measurement is performed here.
"""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'simulations'))
import waves_interfaces as waves
from source_provenance import check_reference


def maximum(value):
    return float(np.max(np.abs(value)))


def check(value, limit, message):
    error = maximum(value)
    if not np.isfinite(error) or error > limit:
        raise AssertionError(f'{message}: error {error:.6g} exceeds {limit:.6g}')
    return error


def boundary_solve(n1, nf, n2, thickness, wavelength):
    """Solve four E/H interface equations, without the closed-form film formula.

    Unknowns are reflected r, internal forward/backward fields a/b, and t at
    the EXIT face. Incident tangential E=1 is referenced to the entrance face.
    """
    phase = 2 * np.pi * nf * thickness / wavelength
    forward, backward = np.exp(1j * phase), np.exp(-1j * phase)
    matrix = np.array([
        [1, -1, -1, 0],
        [-n1, -nf, nf, 0],
        [0, forward, backward, -1],
        [0, nf * forward, -nf * backward, -n2]
    ], dtype=complex)
    solution = np.linalg.solve(matrix, [-1, -n1, 0, 0])
    return solution[0], solution[3], maximum(matrix @ solution - [-1, -n1, 0, 0])


def main():
    digest = hashlib.sha256((ROOT / 'simulations/waves_interfaces.py').read_bytes()).hexdigest()
    reference_path = ROOT / 'data/chapter-02/waves-reference.json'
    if not reference_path.exists():
        raise FileNotFoundError('Execute/save the Chapter 2 notebook before running this audit.')
    reference = json.loads(reference_path.read_text(encoding='utf-8'))
    assert reference['metadata']['source_sha256'] == digest, 'Simulation module hash differs.'
    check_reference(reference, ROOT/'notebooks/02-waves-and-interfaces.ipynb')

    interface_errors = []
    interface_cases = 0
    for n1, n2 in [(1., 1.), (1., 1.5), (1.5, 1.), (1.2, 2.3)]:
        angles = np.array([0., 10., 25., 40., 50., 65., 80.])
        for pol in ['TE', 'TM']:
            value = waves.interface(n1, n2, angles, pol)
            interface_errors.append(check(value['R'] + value['T'] - 1, 2e-12, 'Interface power'))
            interface_errors.append(check(value['t'] - 1 - value['r'], 2e-12, 'Interface tangential E'))
            # Independent angle-form expressions use Snell's law directly.
            ci = np.cos(np.deg2rad(angles))
            ct = np.sqrt((1 - (n1 / n2 * np.sin(np.deg2rad(angles)))**2).astype(complex))
            if pol == 'TE':
                expected_r = (n1 * ci - n2 * ct) / (n1 * ci + n2 * ct)
                expected_t = 2 * n1 * ci / (n1 * ci + n2 * ct)
            else:
                expected_r = (n1 * ct - n2 * ci) / (n1 * ct + n2 * ci)
                expected_t = 2 * n1 * ct / (n1 * ct + n2 * ci)
            interface_errors.append(check(value['r'] - expected_r, 2e-12, 'Fresnel angle-form r'))
            interface_errors.append(check(value['t'] - expected_t, 2e-12, 'Fresnel angle-form t'))
            interface_cases += len(angles)
    for pol in ['TE', 'TM']:
        normal = waves.interface(1., 1.5, 0., pol)
        check(normal['r'] + .2, 1e-14, 'Air/glass r')
        check(normal['t'] - .8, 1e-14, 'Air/glass t')
        check(normal['R'] - .04, 1e-14, 'Air/glass R')
        check(normal['T'] - .96, 1e-14, 'Air/glass T')
        # Equal media remain transparent even at valid near-grazing incidence.
        grazing = waves.interface(1., 1., np.array([89., 89.99999, 89.9999999]), pol)
        check(grazing['r'], 1e-10, 'Matched-medium grazing reflection')
        check(grazing['t'] - 1, 1e-10, 'Matched-medium grazing transmission')
        assert np.all(grazing['regime'] == 'propagating')
    brewster = float(np.rad2deg(np.arctan(1.5)))
    check(waves.interface(1., 1.5, brewster, 'TM')['r'], 1e-13, 'Brewster zero')
    critical = float(np.rad2deg(np.arcsin(1 / 1.5)))
    for pol, expected_r, expected_t in [('TE', 1, 2), ('TM', -1, 0)]:
        cutoff = waves.interface(1.5, 1., critical, pol)
        assert str(cutoff['regime']) == 'cutoff'
        check(cutoff['r'] - expected_r, 1e-13, 'Critical-angle r')
        check(cutoff['t'] - expected_t, 1e-13, 'Critical-angle tangential t')
        check(cutoff['T'], 1e-13, 'Critical-angle normal flux')
        if pol == 'TM':
            assert np.isnan(cutoff['phase_deg']), 'Zero tangential t has no phase.'
        below = waves.interface(1.5, 1., critical - 1e-5, pol)
        above = waves.interface(1.5, 1., critical + 1e-5, pol)
        assert str(below['regime']) == 'propagating' and below['T'] > 0
        assert str(above['regime']) == 'evanescent' and abs(above['t']) > 0
        check(above['T'], 1e-13, 'TIR normal transmitted flux')
        assert above['q2'].imag > 0, 'Evanescent wave must decay toward positive z.'

    field_errors = []
    x = np.linspace(-.4, .6, 13)[None, :]
    z = np.array([-.7, -.2, 0., .1, .4, .8])[:, None]
    for n1, n2, angle in [(1., 1.5, 35.), (1.5, 1., 50.)]:
        value = waves.interface(n1, n2, angle, 'TE')
        field = waves.te_interface_fields(x, z, n1, n2, angle, .6)
        field_errors.append(check(field['normal_flux'] - value['T'], 2e-12, 'Exact TE normal Poynting flux'))
        eps = 1e-10
        left = waves.te_interface_fields(0., -eps, n1, n2, angle, .6)
        right = waves.te_interface_fields(0., eps, n1, n2, angle, .6)
        field_errors.append(check(left['E'] - right['E'], 2e-8, 'Interface near-face E continuity'))
        field_errors.append(check(left['Hx_eta0'] - right['Hx_eta0'], 2e-8, 'Interface near-face H continuity'))
    decay_z = np.array([0., .1, .3, .7])
    tir = waves.interface(1.5, 1., 50., 'TE')
    field = waves.te_interface_fields(0., decay_z, 1.5, 1., 50., .6)
    expected_decay = np.exp(-2 * np.pi / .6 * tir['q2'].imag * decay_z)
    decay_error = check(np.abs(field['E'] / field['E'][0]) - expected_decay, 1e-13, 'TIR amplitude decay')

    film_errors, film_matrix_residuals, film_unitarity, film_reciprocity = [], [], [], []
    film_cases = 0
    for n1, nf, n2 in [(1., 1.4, 1.5), (1.5, 2.2, 1.), (1., 1., 1.), (1.2, 2.4, 1.7)]:
        for thickness in [0., .07, .2, .53]:
            for wavelength in [.45, .8]:
                value = waves.film(n1, nf, n2, thickness, wavelength)
                r, t, residual = boundary_solve(n1, nf, n2, thickness, wavelength)
                film_errors.append(check([value['r'] - r, value['t'] - t], 3e-12, 'Four-boundary-equation film solution'))
                film_matrix_residuals.append(residual)
                film_errors.append(check(value['R'] + value['T'] - 1, 3e-12, 'Film power'))
                S = waves.film_scattering(n1, nf, n2, thickness, wavelength)
                film_unitarity.append(check(S.conj().T @ S - np.eye(2), 3e-12, 'Film two-port unitarity'))
                film_reciprocity.append(check(S[0, 1] - S[1, 0], 3e-12, 'Power-normalized film reciprocity'))
                film_cases += 1
    nf = np.sqrt(1.5)
    ar = waves.film(1., nf, 1.5, .6 / (4 * nf), .6)
    check(ar['r'], 1e-13, 'Quarter-wave antireflection')
    check(ar['T'] - 1, 1e-13, 'Quarter-wave transmitted power')
    check(ar['t'] - 1j * np.sqrt(1 / 1.5), 1e-13, 'Quarter-wave exit-plane phase')
    homogeneous = waves.film(1.7, 1.7, 1.7, .23, .6)
    check(homogeneous['r'], 1e-14, 'Homogeneous-film reflection')
    check(homogeneous['t'] - np.exp(2j * np.pi * 1.7 * .23 / .6), 1e-13, 'Homogeneous-film propagation phase')
    zeros = waves.film(1., 2.3, 1.5, 0., .6)
    bare = waves.interface(1., 1.5)
    check([zeros['r'] - bare['r'], zeros['t'] - bare['t']], 1e-13, 'Zero-thickness film limit')

    sheet_balance, joule_errors, passive_excess, sheet_reciprocity = [], [], [], []
    sheet_cases = 0
    for n1, n2 in [(1., 1.), (1., 1.5), (1.5, 1.)]:
        for G in [0., .2, 2., 6.]:
            for B in [-3., 0., 4.]:
                value = waves.sheet(G, B, n1, n2)
                joule = G / n1 * abs(value['t'])**2
                sheet_balance.append(check(value['R'] + value['T'] + value['A'] - 1, 3e-12, 'Sheet all-channel balance'))
                joule_errors.append(check(value['A'] - joule, 1e-13, 'Independent sheet Joule dissipation'))
                check(value['t'] - 1 - value['r'], 1e-13, 'Sheet E continuity')
                S = waves.sheet_scattering(G, B, n1, n2)
                eigenvalues = np.linalg.eigvalsh(S.conj().T @ S)
                excess = max(0., float(eigenvalues[-1] - 1))
                passive_excess.append(check(excess, 3e-12, 'Sheet passivity for arbitrary coherent inputs'))
                sheet_reciprocity.append(check(S[0, 1] - S[1, 0], 1e-13, 'Sheet reciprocity'))
                if G == 0:
                    check(S.conj().T @ S - np.eye(2), 3e-12, 'Reactive-sheet unitarity')
                sheet_cases += 1
        optimum = waves.sheet(n1 + n2, 0., n1, n2)
        check(optimum['A'] - n1 / (n1 + n2), 1e-13, 'Unequal-index one-sided absorption bound')
        for factor in [.5, 2.]:
            assert waves.sheet(factor * (n1 + n2), 0., n1, n2)['A'] < optimum['A']
    phase = np.linspace(0., 360., 17)
    coherent = waves.coherent_sheet(2., 0., phase)
    coherent_error = check(coherent['absorbed'] - (1 + np.cos(np.deg2rad(phase))) / 2, 1e-13, 'Coherent perfect-absorption phase law')
    check(coherent['outgoing'] + coherent['absorbed'] - 1, 1e-13, 'Coherent input normalization')

    retrieval_errors, retrieval_cases = [], 0
    for n1, n2 in [(1., 1.), (1., 1.5), (1.5, 1.)]:
        for G in [.1, 1., 2.]:
            for B in [-2., 0., 2.]:
                value = waves.sheet(G, B, n1, n2)
                retrieved = waves.retrieve_sheet(value['r'], value['t'], n1, n2)
                retrieval_errors.append(check(retrieved - (G + 1j * B), 1e-12, 'Sheet retrieval round trip'))
                retrieval_cases += 1
    rejected_retrievals = 0
    for r, t in [(-1., 0.), (-1 + 1e-10, 1e-10), (0., .8), (ar['r'], ar['t'])]:
        try:
            waves.retrieve_sheet(r, t)
        except ValueError:
            rejected_retrievals += 1
        else:
            raise AssertionError('An unstable or incompatible retrieval was accepted.')

    stokes_errors, analyzer_errors, polarization_cases = [], [], 0
    for alpha in [0., 23., 45., 90.]:
        for delta in [-90., 0., 35., 90., 180.]:
            value = waves.polarization(alpha, delta, 17.)
            orthogonal = waves.polarization(alpha, delta, 107.)
            stokes_errors.append(check(value['I']**2 - value['Q']**2 - value['U']**2 - value['V']**2, 1e-13, 'Pure-state Stokes norm'))
            analyzer_errors.append(check(value['analyzer_power'] + orthogonal['analyzer_power'] - value['I'], 1e-13, 'Orthogonal analyzer powers'))
            polarization_cases += 1
    for alpha in [0., 23., 45., 90.]:
        for beta in [0., 17., 45., 90.]:
            value = waves.polarization(alpha, 0., beta)
            analyzer_errors.append(check(value['analyzer_power'] - np.cos(np.deg2rad(alpha - beta))**2, 1e-13, 'Malus law'))
    circular = waves.polarization(45., 90., 0.)
    check([circular['Q'], circular['U'], circular['V'] - 1], 1e-13, 'Coordinate-defined circular Stokes state')
    check([circular['Ex'].real - 1 / np.sqrt(2), circular['Ey'].real, circular['Ex'].imag, circular['Ey'].imag - 1 / np.sqrt(2)], 1e-13, 'Jones time-convention quarter-cycle orientation')

    invalid_calls = [
        lambda: waves.interface(n1=0), lambda: waves.interface(n2=np.inf),
        lambda: waves.interface(angle_deg=-1), lambda: waves.interface(angle_deg=90),
        lambda: waves.interface(n1=1 + .1j), lambda: waves.interface(polarization='mixed'),
        lambda: waves.film(thickness_um=-1), lambda: waves.film(wavelength_um=0),
        lambda: waves.film(nf=-1), lambda: waves.sheet(conductance=-.1),
        lambda: waves.sheet(susceptance=np.nan), lambda: waves.sheet(n1=0),
        lambda: waves.retrieve_sheet(0, np.nan),
        lambda: waves.retrieve_sheet(0, 1, minimum_amplitude=0),
        lambda: waves.polarization(alpha_deg=np.nan),
        lambda: waves.polarization(delta_deg=np.inf),
        lambda: waves.te_interface_fields(np.nan, 0),
        lambda: waves.te_interface_fields(0, 0, wavelength_um=-1)
    ]
    rejected_inputs = 0
    for call in invalid_calls:
        try:
            call()
        except ValueError:
            rejected_inputs += 1
        else:
            raise AssertionError('Invalid physical input was accepted.')

    report = dict(
        status='passed', model_version=waves.MODEL_VERSION, source_sha256=digest,
        simulation_module_hash_checked=True,
        notebook_code_hash_checked=True,
        parameters_hash_checked=True,
        result_payload_hash_checked=True,
        provenance={key:reference['metadata'][key] for key in
                    ('notebook_code_sha256','parameters_sha256','result_payload_sha256')},
        interface=dict(parameter_cases=interface_cases, max_error=max(interface_errors),
                       matched_grazing_angles_deg=[89., 89.99999, 89.9999999],
                       brewster_deg=brewster, critical_deg=critical,
                       exact_cutoff_and_adjacent_regimes='passed'),
        fields=dict(regimes=2, max_flux_or_near_face_error=max(field_errors),
                    max_evanescent_amplitude_error=decay_error),
        film=dict(parameter_cases=film_cases, independent_method='four E/H boundary equations solved as a 4x4 linear system',
                  max_complex_or_power_error=max(film_errors),
                  max_boundary_solve_residual=max(film_matrix_residuals),
                  max_unitarity_error=max(film_unitarity), max_reciprocity_error=max(film_reciprocity),
                  quarter_wave_zero_and_exit_phase='passed', zero_thickness_and_homogeneous_limits='passed'),
        sheet=dict(parameter_cases=sheet_cases, max_balance_error=max(sheet_balance),
                   max_joule_error=max(joule_errors), max_passivity_excess=max(passive_excess),
                   max_reciprocity_error=max(sheet_reciprocity),
                   unequal_index_absorption_optima='passed', coherent_phase_cases=len(phase),
                   max_coherent_absorption_error=coherent_error),
        retrieval=dict(parameter_cases=retrieval_cases, max_complex_error=max(retrieval_errors),
                       rejected_unstable_or_incompatible_cases=rejected_retrievals),
        polarization=dict(jones_cases=polarization_cases, malus_cases=16,
                          max_stokes_error=max(stokes_errors), max_analyzer_error=max(analyzer_errors),
                          coordinate_time_convention='passed'),
        invalid_input_rejections=rejected_inputs,
        scope=['Exact planar analytical models only', 'Positive real nonmagnetic bulk indices',
               'Passive electric sheet with coincident reference planes',
               'No patterned full-wave geometry or fabricated-device validation']
    )
    destination = ROOT / 'data/chapter-02/validation.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
