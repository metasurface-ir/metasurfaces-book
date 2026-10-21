"""Analytical Chapter 1 checks; no electromagnetic geometry solver is used."""
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'simulations'))
from intro_sheet import Sheet,PRESETS,response,scattering_matrix,channel_group_delay_fs


def main():
    f=np.linspace(80.,340.,521)
    cases=[Sheet(electric_frequency_THz=fe,magnetic_frequency_THz=fm,electric_strength=ae,magnetic_strength=am)
           for fe in [180.,220.] for fm in [180.,230.] for ae in [0.,.1,.4] for am in [0.,.15,.5]]
    worst_balance=0.;worst_unitarity=0.;worst_two_sided=0.
    incoming=np.array([.3+.4j,-.2+.7j])
    for sheet in cases:
        v=response(f,sheet);S=scattering_matrix(f,sheet)
        worst_balance=max(worst_balance,float(np.max(v['balance_error'])))
        worst_unitarity=max(worst_unitarity,float(np.max(abs(np.swapaxes(S.conj(),-1,-2)@S-np.eye(2)))))
        outgoing=S@incoming
        worst_two_sided=max(worst_two_sided,float(np.max(abs(np.sum(abs(outgoing)**2,axis=-1)-np.sum(abs(incoming)**2)))))
        assert np.all(np.isfinite(v['r'])) and np.all(np.isfinite(v['t']))
    assert max(worst_balance,worst_unitarity,worst_two_sided)<1e-12
    sheet=PRESETS['electric'];v=response(f,sheet)
    u=f/sheet.electric_frequency_THz;d=1-u*u;z=sheet.electric_strength*u
    # Independent shunt-sheet algebra, avoiding the eigenchannel construction.
    electric_error=float(max(np.max(abs(v['t']-d/(d-1j*z))),np.max(abs(v['r']-1j*z/(d-1j*z)))))
    assert electric_error<1e-12
    exact=response(200.,PRESETS['electric']);assert abs(exact['t'])<1e-12 and np.isnan(exact['phase_deg'])
    balanced=response(f,PRESETS['balanced']);assert np.max(abs(balanced['r']))<1e-12
    transparent=response(f,PRESETS['transparent']);assert np.max(abs(transparent['t']-1))<1e-12
    derivative=[]
    for strength in [.08,.25,.5]:
        sheet=Sheet(electric_strength=strength,magnetic_strength=strength)
        exact=float(channel_group_delay_fs(200.,200.,strength))
        errors=[]
        for step in [.2,.1,.05]:
            vp=response(200.+step,sheet)['t'];vm=response(200.-step,sheet)['t']
            numerical=1000*np.angle(vp*np.conj(vm))/(4*np.pi*step)
            errors.append(float(abs(numerical-exact)))
        assert errors[-1]<.002 and errors[-1]<errors[0]
        derivative.append(dict(strength=strength,steps_THz=[.2,.1,.05],errors_fs=errors))
    rejected=0
    for bad in [replace(Sheet(),electric_strength=-1),replace(Sheet(),magnetic_frequency_THz=0),replace(Sheet(),electric_strength=float('nan'))]:
        try:response(200.,bad)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid sheet accepted')
    for frequency in [0.,-1.,float('nan'),float('inf')]:
        try:response(frequency)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid frequency accepted')
    reference=json.loads((ROOT/'data/chapter-01/sheet-response.json').read_text())
    digest=hashlib.sha256((ROOT/'simulations/intro_sheet.py').read_bytes()).hexdigest()
    assert digest==reference['metadata']['source_sha256']
    assert reference['presets']['electric']['phase_deg'] is None
    report=dict(status='passed',model='analytical equal-impedance specular sheet',source_sha256=digest,
                parameter_cases=len(cases),frequencies_per_case=len(f),max_power_balance_error=worst_balance,
                max_unitarity_error=worst_unitarity,max_two_sided_power_error=worst_two_sided,
                electric_shunt_complex_error=electric_error,group_delay_checks=derivative,
                input_rejections=rejected,phase_at_zero_transmission='undefined and serialized as null',
                limits=['No full-wave solver','No geometry/material calibration','No diffraction/polarization conversion','No absorption/experiment'])
    (ROOT/'data/chapter-01/validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
